from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Pond, PondSection, SpawnPoint


class PondCreationTests(APITestCase):
	def test_creating_pond_creates_two_sections(self):
		response = self.client.post(
			reverse('pond-list'),
			{'name': 'Test Pond', 'weather_id': 1},
			format='json',
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		pond = Pond.objects.get(pk=response.data['pond_id'])
		sections = PondSection.objects.filter(pond_id=pond)
		self.assertEqual(sections.count(), 2)
		for section in sections:
			self.assertEqual(
				SpawnPoint.objects.filter(pond_section_id=section).count(), 4
			)

	def test_creating_section_creates_four_spawn_points(self):
		pond = Pond.objects.create(name='Test Pond', weather_id=1)

		section = PondSection.objects.create(pond_id=pond)

		self.assertEqual(
			SpawnPoint.objects.filter(pond_section_id=section).count(), 4
		)

	def test_updating_pond_does_not_create_more_sections(self):
		response = self.client.post(
			reverse('pond-list'),
			{'name': 'Test Pond', 'weather_id': 1},
			format='json',
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		pond = Pond.objects.get(pk=response.data['pond_id'])
		section_ids = set(
			PondSection.objects.filter(pond_id=pond).values_list('pk', flat=True)
		)

		response = self.client.patch(
			reverse('pond-detail', args=[pond.pk]),
			{'name': 'Renamed Pond'},
			format='json',
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		pond.refresh_from_db()
		self.assertEqual(pond.name, 'Renamed Pond')
		self.assertEqual(
			set(PondSection.objects.filter(pond_id=pond).values_list('pk', flat=True)),
			section_ids,
		)

	def test_section_creation_failure_rolls_back_pond(self):
		with patch(
			'gameplay.models.SpawnPoint.objects.bulk_create',
			side_effect=RuntimeError('Section creation failed'),
		):
			with self.assertRaisesMessage(RuntimeError, 'Section creation failed'):
				self.client.post(
					reverse('pond-list'),
					{'name': 'Test Pond', 'weather_id': 1},
					format='json',
				)

		self.assertFalse(Pond.objects.exists())
		self.assertFalse(PondSection.objects.exists())
		self.assertFalse(SpawnPoint.objects.exists())

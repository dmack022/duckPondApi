Commands for generating fixture files

python manage.py dumpdata catalog.Flavor --indent 2 --output catalog\fixtures\flavors.json
python manage.py dumpdata catalog.Food --indent 2 --output catalog\fixtures\food.json
python manage.py dumpdata catalog.Duck --indent 2 --output catalog\fixtures\ducks.json
python manage.py dumpdata catalog.DuckFlavor --indent 2 --output catalog\fixtures\duck-flavors.json
python manage.py dumpdata catalog.FoodFlavor --indent 2 --output catalog\fixtures\food-flavors.json
python manage.py dumpdata catalog.Weather --indent 2 --output catalog\fixtures\weather.json
python manage.py dumpdata catalog.WaterTemperature --indent 2 --output catalog\fixtures\watertemperature.json
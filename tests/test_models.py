from app.models import Country, City

def test_country_model():
    country = Country(name='Testland')
    assert country.name == 'Testland'

def test_city_model():
    city = City(name='Testville', population=1000, country_id=1)
    assert city.population == 1000


import csv
from app import create_app
from app.models import db, Country, City

app = create_app()
app.app_context().push()

with open('worldcities.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        country_name = row['country']
        city_name = row['city']
        population = int(float(row['population'])) if row['population'] else 0


        country = Country.query.filter_by(name=country_name).first()
        if not country:
            country = Country(name=country_name)
            db.session.add(country)
            db.session.flush()  # Get ID

        city = City(name=city_name, population=population, country=country)
        db.session.add(city)

    db.session.commit()

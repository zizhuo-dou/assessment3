from flask import Blueprint, render_template, request
from .models import Country, City

main = Blueprint('main', __name__)

@main.route('/')
def index():
    search = request.args.get('search')
    if search:
        countries = Country.query.filter(Country.name.ilike(f'%{search}%')).all()
    else:
        countries = Country.query.order_by(Country.name).all()
    return render_template('index.html', countries=countries, search=search)

@main.route('/country/<int:country_id>')
def country_detail(country_id):
    country = Country.query.get_or_404(country_id)
    return render_template('country.html', country=country)

@main.route('/stats')
def stats():
    countries = Country.query.all()
    
    countries_by_city_count = sorted(countries, key=lambda c: len(c.cities), reverse=True)
    top3 = countries_by_city_count[:3]

    most_cities_country = top3[0] if top3 else None
    cities = most_cities_country.cities if most_cities_country else []

    populations = [c.population for c in cities if c.population > 0]
    total_population = sum(populations)
    average_population = int(total_population / len(populations)) if populations else 0

    largest_city = max(cities, key=lambda c: c.population, default=None)
    smallest_city = min([c for c in cities if c.population > 0], key=lambda c: c.population, default=None)

    return render_template(
        'stats.html',
        top3=top3,
        country=most_cities_country,
        total_population=total_population,
        average_population=average_population,
        largest_city=largest_city,
        smallest_city=smallest_city
    )


@main.app_errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@main.route('/cities')
def city_search():
    q = request.args.get('q')
    if q:
        cities = City.query.filter(City.name.ilike(f'%{q}%')).order_by(City.population.desc()).all()
    else:
        cities = City.query.order_by(City.population.desc()).limit(50).all()
    return render_template('cities.html', cities=cities, q=q)

@main.app_errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500


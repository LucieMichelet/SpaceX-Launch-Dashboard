import requests
from django.core.management.base import BaseCommand
from launches.models import Launch

# To check if the API works
# curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"{ launches { mission_name } }\"}" https://api.spacex.land/graphql/
# python manage.py load_launches  

class Command(BaseCommand):
    help = 'Load SpaceX launches data into the database'

    def handle(self, *args, **kwargs):
        response = requests.post('https://api.spacex.land/graphql/', json={
            'query': '''
                {
                    launches {
                        mission_name
                        launch_date_utc
                        rocket {
                            rocket_name
                        }
                        details
                        launch_site {
                            site_name_long
                        }
                    }
                }
            '''
        })
        data = response.json()['data']['launches']

        for launch in data:
            Launch.objects.create(
                mission_name=launch['mission_name'],
                launch_date_utc=launch['launch_date_utc'],
                rocket_name=launch['rocket']['rocket_name'],
                details=launch['details'],
                launch_site=launch['launch_site']['site_name_long']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded SpaceX launches data'))
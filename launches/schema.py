import requests
from graphene import ObjectType, String, Int, List, Field, Schema


class Launch(ObjectType):
    mission_name = String()
    launch_date_utc = String()
    rocket_name = String()
    details = String()
    launch_site = String()
    

class Query(ObjectType):
    all_launches = List(Launch)

    def resolve_all_launches(root,info):
        response = requests.post('https://api.spacex.land/graphql/',json={
            'query':'''
                {
                    launches {
                        mission_name
                        launch_date_utc
                        rocket{rocket_name}
                        details
                        launch_site{site_name_long}
                    }
                }
                '''
        })
        data = response.json()['data']['launches']
        print("data:",data)
        return [Launch(mission_name = launch['mission_name'], launch_date_utc = launch['launch_date_utc'],
                        rocket_name = launch['rocket']['rocket_name'], details = launch['details'],
                        launch_site = launch['launch_site']['site_name_long']) for launch in data]
    
schema = Schema(query=Query)

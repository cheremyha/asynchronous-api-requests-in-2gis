import json
import asyncio
from aiohttp import ClientSession, TCPConnector

from secret_key import get_secret_api_key
from data_source import routes_points_list

# Get secret api key from config file.
secret_api_key = get_secret_api_key(file_name='config.ini')


async def get_data_by_route(route_points):
    """
    Coroutine function who send post requests to 2gis server by api.
    And convert data from response into convenient form
    ( python dictionary with data by routes ).
    :param route_points: Dictionary with points one of the route.
    :return: Dictionary with route_id, distance, duration, status code of response by this route.
    """

    # Set limit for RPS ( Response per second ).
    connector = TCPConnector(limit=5)
    async with ClientSession(connector=connector) as session:

        # Set address and key for request.
        url = 'https://catalog.api.2gis.com/carrouting/6.0.0/global'
        params = {'key': secret_api_key}

        async with session.post(
                url=url,
                params=params,
                data=json.dumps(route_points),
                headers={'Content-type': 'application/json'},
        ) as response:
            route_id = route_points['route_id']

            response_ = await response.json()

            # Here we start parsing response data.
            # And save these in variables.
            status_code = response.status

            response = response_['result'][0]

            # Get route distance and duration from response.
            distance = response['total_distance']
            duration = response['total_duration']

            return_dict = {
                'route_id': route_id,
                'distance': distance,
                'duration': duration,
                'status_code': status_code,
            }

            return return_dict


async def main(routes_points_list):
    """
    Coroutine function who create tasks for event loop
    :param routes_points_list:  List with all route points.
    :return: List with dictionary. Each of them consist from data by route
    ( return get_data_by_route function: route_id, distance, duration, status code ).
    """

    # Define list of tasks
    tasks = []
    for route in routes_points_list:
        route_points = route['data']
        tasks.append(asyncio.create_task(get_data_by_route(route_points=route_points)))
        results = await asyncio.gather(*tasks)

    result_list = []
    for route_result in results:
        result_list.append(route_result)

    return result_list

# Here we start asynchronous requests using the top-level entry point.
result = asyncio.run(main(routes_points_list=routes_points_list))
print(result)
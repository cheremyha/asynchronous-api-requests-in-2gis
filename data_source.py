"""
This file is data source with routes and coordinates their points.
"""


# Create data for request.
route_points_route_0 = {
    'points': [
        {
           'type': 'pedo',
           'y': 47.21274351,
           'x': 39.67247929,
        },
        {
           'type': 'pedo',
           'y': 82.945039,
           'x': 55.033879,
        },
        {
           'type': 'pedo',
           'y': 47.200782,
           'x': 39.652068,
        }
    ],
    'route_id': 0,
}

route_points_route_1 = {
    'points': [
        {
            'type': 'pedo',
            'y': 47.217296,
            'x': 39.703251,
        },
        {
            'type': 'pedo',
            'y': 82.945039,
            'x': 55.033879,
        },
        {
            'type': 'pedo',
            'y': 47.200782,
            'x': 39.652068,
        }
    ],
    'route_id': 1,
}


routes_points_list_ds = [
    {'route_id': 1, 'data': route_points_route_0},
    {'route_id': 0, 'data': route_points_route_1},
]

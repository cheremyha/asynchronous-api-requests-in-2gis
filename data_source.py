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

route_points_route_0 = {
 'type': 'statistic',
 'points': [{'type': 'stop', 'x': 60.49992370605469, 'y': 56.79222106933594},
  {'y': 56.79198455810547, 'x': 60.47875213623047, 'type': 'pref'},
  {'y': 56.78926467895508, 'x': 60.47233200073242, 'type': 'pref'},
  {'y': 56.81011962890625, 'x': 60.547752380371094, 'type': 'pref'},
  {'y': 56.800086975097656, 'x': 60.55803298950195, 'type': 'pref'},
  {'y': 56.744850158691406, 'x': 60.60457229614258, 'type': 'pref'},
  {'type': 'stop', 'x': 60.49992370605469, 'y': 56.79222106933594}],
 'utc': 1662023713.0,
 'route_id': 1,
}

routes_points_list = [
    {'route_id': 1, 'data': route_points_route_0},
    {'route_id': 0, 'data': route_points_route_1},
]


from channels.routing import route, route_class

from janken.consumers import *

channel_routing = [
    route_class(Consumer, path = r'^/ws/(?P<room_id>[0-9]+)$'),
]
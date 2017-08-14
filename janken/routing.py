from channels.routing import route

from janken.consumers import ws_add, ws_disconnect


channel_routing = [
    route("websocket.connect", ws_add, path = r'^/ws$'),
    route("websocket.disconnect", ws_disconnect)
]
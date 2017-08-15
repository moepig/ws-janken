from channels import Group
from channels.generic.websockets import WebsocketConsumer


class Consumer(WebsocketConsumer):

    strict_ordering = False

    def connect(self, message, **kwargs):
        room_manager = RoomManager.get_instance()
        room_id = int(kwargs['room_id'])

        room_manager.join_room(message, room_id)

    def disconnect(self, message, **kwargs):
        room_manager = RoomManager.get_instance()
        room_id = int(kwargs['room_id'])

        room_manager.discard_room(message, room_id)


class RoomManager:
    """
    全てのルームを管理する
    """

    _instance = None


    ROOM_MAX = 65535

    _rooms = {}       # ルームの集合

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create_room(self, message):
        for room_id in range(0, self.ROOM_MAX):
            if self._rooms.get(room_id, None) is None:
                new_room = Room(room_id=room_id, message=message)
                self._rooms[room_id] = new_room

                print("room created! room_id:" + str(room_id))

                return room_id

        return None

    def join_room(self, message, room_id):
        # あったら入る、なかったら作って入る
        for room in self._rooms.values():
            if room_id == room._room_id:
                room.join(message)
                return

        self.create_room(message)


    def random_room_join(self, message):
        import random
        room = random.choice(self._rooms)

        room.join(message)

    def discard_room(self, message, room_id):
        room = self._rooms[room_id]
        room.discard(message)


class Room:

    _member = []

    def __init__(self, room_id, message):
        self._room_id = room_id

        self.create(message)

    def create(self, message):
        message.reply_channel.send({"accept": True})
        Group(str(self._room_id)).add(message.reply_channel)

    def join(self, message):
        message.reply_channel.send({"accept": True})
        Group(str(self._room_id)).add(message.reply_channel)

    def discard(self, message):
        Group(str(self._room_id)).discard(message.reply_channel)
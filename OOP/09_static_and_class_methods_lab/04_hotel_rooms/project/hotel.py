from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for current_room in self.rooms:
            if current_room.number == room_number and not current_room.is_taken:
                current_room.take_room(people)

    def free_room(self, room_number):
        for current_room in self.rooms:
            if current_room.number == room_number:
                current_room.free_room()

    def status(self):
        total_guests = sum([current_room.guests for current_room in self.rooms])
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]
        output = f"Hotel {self.name} has {total_guests} total guests\n" \
                 f"Free rooms: {', '.join(free_rooms)}\n" \
                 f"Taken rooms: {', '.join(taken_rooms)}"

        return output

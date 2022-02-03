class Room(object):
    def __init__(self, name, isExit, doors):
        self.name = name
        self.isExit = isExit
        self.doors = doors

    def doorsCount(self):
        return len(self.doors)

    def chooseDoor(self):
        choose = input('Chose the door:')
        while choose not in self.doors:
            choose = input('Chose the door:')

        return choose


class Maze:
    def __init__(self, name, doors):
        self.name = name
        self._doors = doors

    def startRoom(self):
        return self._doors["r1"]

    def getRoomBehindDoor(self, door):
        return self._doors[door]


def whatPlayerSee(room):
    return ("You're see " + str(room.doorsCount()) +' doors to rooms:' + str(room.doors))

def travelMaze(maze):
    print('You in '+ maze.name)
    room = maze.startRoom()
    while not room.isExit:
        print(whatPlayerSee(room))
        door = room.chooseDoor()
        room = maze.getRoomBehindDoor(door)

    print("You're have found exit from the maze " + maze.name)

levels = [
    Maze("level 1", {
         'r1' : Room('Room 1', False,['r2','r3']),
         'r2' : Room('Room 2', False,['r4','r1']),
         'r3' : Room('Room 3', False,['r5','r1']),
         'r4' : Room('Room 4', False,['r6','r2']),
         'r5' : Room('Room 5', False,['r6']),
         'r6' : Room('Room 6', True, [])
    }),
    Maze("Level 2", {
        'r1': Room('Room 1', False,['r3','r4']),
        'r2': Room('Room 2', False,['r2','r1']),
        'r3': Room('Room 3', False,['r5','r1']),
        'r4': Room('Room 4', False,['r6','r2']),
        'r5': Room('Room 5', False,['r6']),
        'r6': Room('Room 6', True, [])}
    )
]


print("Hello, traveler. You're entered to mysterious dungeon.")
for level in levels:
    travelMaze(level)

print("You are super winner.")

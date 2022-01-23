class Room(object):
    def __init__(self, name, isExit, doors):
        self.name = name
        self.isExit = isExit
        self._doors = doors
        self._doorsCount = len(doors)

    def doorsCount(self):
        return self._doorsCount

    def addDoor(self, door):
        self._doors += [door]
        self._doorsCount += 1

    def doors(self):
        return self._doors

    def chooseDoor(self):
        choose = input('Chose the door:')
        while choose not in self.doors():
            choose = input('Chose the door:')

        return choose



r6=Room('Room 6', True, [])
r5=Room('Room 5', False,['r6'])
r4=Room('Room 4', False,[ 'r6','r2'])
r3=Room('Room 3', False,['r5','r1'])
r2=Room('Room 2', False,['r4','r1'])
r1=Room('Room 1', False,['r2','r3'])
doors={}
doors['r1']=r1
doors['r2']=r2
doors['r3']=r3
doors['r4']=r4
doors['r5']=r5
doors['r6']=r6

def whatPlayerSee(room):
    return ("You're see " + str(room.doorsCount()) +' doors to rooms:' + str(room.doors()))

def travelRoom(room):
    print('You in '+ room.name)
    if room.isExit:
        print("You're win")
        exit()
    print(whatPlayerSee(room))
    choose = room.chooseDoor()
    travelRoom(doors[choose])

print("Hello, traveler. You're entered to mysterious dungeon.")
travelRoom(r1)

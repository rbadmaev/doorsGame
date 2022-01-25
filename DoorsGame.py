#Create main class
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


#LVL 1
r6=Room('Room 6', True, [])
r5=Room('Room 5', False,['r6'])
r4=Room('Room 4', False,['r6','r2'])
r3=Room('Room 3', False,['r5','r1'])
r2=Room('Room 2', False,['r4','r1'])
r1=Room('Room 1', False,['r2','r3'])

#New variable door
doors={}
doors['r1']=r1
doors['r2']=r2
doors['r3']=r3
doors['r4']=r4
doors['r5']=r5
doors['r6']=r6

#print player
def whatPlayerSee(room):
    return ("You're see " + str(room.doorsCount()) +' doors to rooms:' + str(room.doors))

#Main def
def travelRoom(room):
    print('You in '+ room.name)
    if room.isExit:
        print("You're win")
        exit()
    print(whatPlayerSee(room))
    choose = room.chooseDoor()
    travelRoom(doors[choose])

#Start game
print("Hello, traveler. You're entered to mysterious dungeon.")
travelRoom(r1)

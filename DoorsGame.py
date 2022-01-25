import os

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

class LVL(object):
    def __init__(self, lvlOne, lvlTwo):
        self.lvlOne = LVL.startLvlOne()
        self.lvlTwo = LVL.startLvlTwo()

    def startLvlOne(self):
        r6 = Room('Room 6', True, [])
        r5 = Room('Room 5', False, ['r6', 'r3'])
        r4 = Room('Room 4', False, ['r6', 'r2'])
        r3 = Room('Room 3', False, ['r5', 'r1'])
        r2 = Room('Room 2', False, ['r4', 'r1'])
        r1 = Room('Room 1', False, ['r2', 'r3'])
        startLvlOne(r1)

    def startLvlTwo():
        r15 = Room('Room 15', False, ['r14', 'r10', 'r12'])
        r14 = Room('Room 14', True, [])
        r13 = Room('Room 13', False, ['r8', 'r12', 'r11'])
        r12 = Room('Room 12', False, ['r15', 'r13'])
        r11 = Room('Room 11', False, ['r13', 'r5'])
        r10 = Room('Room 10', False, ['r8', 'r15'])
        r9 = Room('Room 9', False, ['r8', 'r3', 'r6'])
        r8 = Room('Room 8', False, ['r10', 'r13', 'r9'])
        r7 = Room('Room 7', False, ['r5', 'r3'])
        r6 = Room('Room 6', False, ['r4', 'r9'])
        r5 = Room('Room 5', False, ['r2', 'r7', 'r11'])
        r4 = Room('Room 4', False, ['r3', 'r6'])
        r3 = Room('Room 3', False, ['r2', 'r4', 'r7', 'r9'])
        r2 = Room('Room 2', False, ['r1', 'r3', 'r5'])
        r1 = Room('Room 1', False, ['r2'])
        startLvlTwo(r1)


r15= []
r14= []
r13= []
r12= []
r11= []
r10= []
r9 = []
r8 = []
r7 = []
r6 = []
r5 = []
r4 = []
r3 = []
r2 = []
r1 = []

doors = {}
doors['r1'] = r1
doors['r2'] = r2
doors['r3'] = r3
doors['r4'] = r4
doors['r5'] = r5
doors['r6'] = r6
doors['r7'] = r7
doors['r8'] = r8
doors['r9'] = r9
doors['r10'] = r10
doors['r11'] = r11
doors['r12'] = r12
doors['r13'] = r13
doors['r14'] = r14
doors['r15'] = r15


def whatPlayerSee(room):
    return ("You're see " + str(room.doorsCount()) + ' doors to rooms:' + str(room.doors))


def travelRoom(room):
    print('You in ' + room.name)
    if room.isExit:
        os.system('cls')
        input('Youre WIN!')
    print(whatPlayerSee(room))
    choose = room.chooseDoor()
    travelRoom(doors[choose])

print('>>>Lvl 1')
print("Hello, traveler. You're entered to mysterious dungeon.")
travelRoom(LVL.startLvlOne)

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

class Level:
    def __init__(self, levelsGuide):
        self.levelsGuide = levelsGuide

    def start_():
        print("Приветствую путешествиник. Это тренеровочная арена в подземельях. Тут ты узаешь все об этом мире.")
        for level in levelsGuide:
            travelMaze(level)

    def continue_():
        pass

    def choose_():
        pass


##################################################################3
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

###################################################################
def MainMenu():
    print('>>>>>>>> Name Game <<<<<<<<')
    print('Список действий:')
    print('Новая игра: start')
    print('Продолжить: continue')
    print('Выбор уровня: choose')

    while True:
        playerChoose = input('Введите команду: ')

        if playerChoose == 'start':
            Level.start_()
        elif playerChoose == 'continue':
            Level.continue_()
        elif playerChoose == 'choose':
            Level.choose_()
        else:
            print('Выбери только из предложеного')

####################################################################
levelsGuide = [
    Maze("level 1", {
         'r1' : Room('Room 1', False,['r2','r3']),
         'r2' : Room('Room 2', False,['r4','r1']),
         'r3' : Room('Room 3', False,['r5','r1']),
         'r4' : Room('Room 4', False,['r6','r2']),
         'r5' : Room('Room 5', False,['r6']),
         'r6' : Room('Room 6', True, [])
    }),
    Maze("Level 2", {
        'r15' : Room('Room 15', False, ['r14', 'r10', 'r12']),
        'r14' : Room('Room 14', True, []),
        'r13' : Room('Room 13', False, ['r8', 'r12', 'r11']),
        'r12' : Room('Room 12', False, ['r15', 'r13']),
        'r11' : Room('Room 11', False, ['r13', 'r5']),
        'r10' : Room('Room 10', False, ['r8', 'r15']),
        'r9' : Room('Room 9', False, ['r8', 'r3', 'r6']),
        'r8' : Room('Room 8', False, ['r10', 'r13', 'r9']),
        'r7' : Room('Room 7', False, ['r5', 'r3']),
        'r6' : Room('Room 6', False, ['r4', 'r9']),
        'r5' : Room('Room 5', False, ['r2', 'r7', 'r11']),
        'r4' : Room('Room 4', False, ['r3', 'r6']),
        'r3' : Room('Room 3', False, ['r2', 'r4', 'r7', 'r9']),
        'r2' : Room('Room 2', False, ['r1', 'r3', 'r5']),
        'r1' : Room('Room 1', False, ['r2']),
        })
]
####################################################################################

MainMenu()



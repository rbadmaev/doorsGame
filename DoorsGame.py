r6=['Room 6',True]
r5=['Room 5',False,1,'r6']
r4=['Room 4',False, 2, 'r6','r2']
r3=['Room 3',False, 2,'r5','r1']
r2=['Room 2',False,2,'r4','r1']
r1=['Room 1',False,2,'r2','r3']
Doors={}
Doors['r1']=r1
Doors['r2']=r2
Doors['r3']=r3
Doors['r4']=r4
Doors['r5']=r5
Doors['r6']=r6


def TravelRoom(Room):
    print('You in '+ Room[0])
    if Room[1]:
        print("You're win")
        exit()
    if len(Room)>4:
        print("You're see "+str(Room[2])+' doors to rooms:'+str(Room[len(Room)-(Room[2]):len(Room)]))
    else:
        print("You're see "+str(Room[2])+' doors to rooms:'+str(Room[len(Room)-1]))
    chose = input('Chose the door:')
    while chose not in (Room[len(Room)-(Room[2]):len(Room)]):
        chose = input('Chose the door:')
    TravelRoom(Doors[chose])


print("Hallo, traveler. You're entered to mysterious dungeon.")
TravelRoom(r1)

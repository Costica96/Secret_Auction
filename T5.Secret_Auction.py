import os
y = 0   #This will be a variable that we will use to determinate the bigger lot in auction
all_participants = int(input("How many people will take part in auction?: "))
nr_participant = 1
lista = []
while nr_participant <= all_participants:
    x = int(input(f"Participantul numarul " + str((nr_participant)) + " introduce suma dorita: "))
    if x not in lista :
        nr_participant += 1
        lista.append(x)
        os.system('cls||clear')
    else :
        print("You need to put a different bit!")
for x in lista:
    if x >= y:
        y = x
    else :
        pass
if all_participants == 0:
    print("The auction cannot be without people!")
else:
    print(f"Winner is the person who bid the amount of {y} euro")

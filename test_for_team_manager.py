import math
import random

#Codigo para torneo con fase de grupos eligiendo numero de grupos
class tournament:
    def __init__(self, name):
        self.name = name
        self.teams = []
        self.groups = []
    def addteam(self, team):
        self.teams.append(team)

class group:
    def __init__(self,name):
        self.name = name
        self.teams = []
        self.asignedgames = []

class team:
    def __init__(self, name):
        self.name = name
        self.win = 0
        self.loses = 0
        self.asignedgamesc = 0

    def addasignedgamec(self):
        self.asignedgamesc += 1
        


#Inicio
print("Bienvenido al torneo")
print("¿Como se va a llamar el torneo?")
tname = input()

#Nombre torneo
t = tournament(tname)

#Añadir equipos
cond = "Si"
while cond != "NO" and cond != "No" and cond != "no" :
    if cond == "SI" or cond == "Si" or cond == "si" :
        print("Digame el nombre del equipo")
        newteam = input()
        t.teams.append(team(newteam)) #Same here, mucho mas limpio
        
        print("¿Quieres añadir otro equipo?(Si/No)")
        cond = input()

    else:
        print("No te he entendido, ¿quieres añadir otro equipo?(Si/No)")
        cond = input()

#Consultar nombre de equipos
print("¿Quieres saber el nombre de algun equipo?(Si/No)")
cond = input()
while cond != "NO" and cond != "No" and cond != "no" :
    if cond == "SI" or cond == "Si" or cond == "si" :
        print("¿De que equipo quieres saber el nombre?")
        numb = input()
        print(t.teams[int(numb)-1].name)
        
        print("¿Quieres saber el nombre de otro equipo?(Si/No)")
        cond = input()

    else:
        print("No te he entendido, ¿quieres saber el nombre de otro equipo?(Si/No)")
        cond = input()
teamnumb = len(t.teams)

#Numero de grupos
print("¿Cuantos grupos quieres que sean?")
groupnumb = int(input())

#Definir el numero de equipos en los grupos y printear  
x = teamnumb / groupnumb
x = math.floor(x)
y = teamnumb - x * groupnumb
grouptext1 = "grupos"
grouptext2 = "grupos"
if y == 1:
    grouptext1 = "grupo"
if groupnumb - y == 1:
    grouptext2 = "grupo"
if y == 0:
    print(f"Va a haber {groupnumb} {grouptext2} de {x} equipos")
elif y != 0:
    print(f"Va a haber {y} {grouptext1} de {x+1} equipos y {groupnumb-y} {grouptext2} de {x} equipos")

#Crear los grupos como objetos
i = 1
while i <= groupnumb:
    t.groups.append(group("Grupo " + str(i))) # Como dicen los guiris, mucho mas Pythonic así
    i += 1

#Repartir equipos en los grupos
teamsraffle = t.teams
x0 = 1
y0 = 1
z = 0
while teamsraffle != []:
    randomteam = random.choice(teamsraffle)
    teamsraffle.remove(randomteam)
    
    #Todos los grupos son iguales
    if y == 0:
        if x0 <= x:
            t.groups[y0-1].teams.append(randomteam)
            x0 += 1
        else:
            x0 = 1
            y0 += 1
            t.groups[y0-1].teams.append(randomteam)
            x0 += 1

    #No todos los grupos son iguales
    elif y != 0:
        if y0 <= y:
            if x0 <= x+1:
                t.groups[y0-1].teams.append(randomteam)
                x0 += 1
            else:
                x0 = 1
                y0 += 1
                t.groups[y0-1].teams.append(randomteam)
                x0 += 1
        elif y0 > y:
            if x0 <= x:
                t.groups[y0-1].teams.append(randomteam)
                x0 += 1
            else:
                x0 = 1
                y0 += 1
                t.groups[y0-1].teams.append(randomteam)
                x0 += 1

#Printear los grupos
for groupselect in t.groups:
    print(groupselect.name)
    for teamselect in groupselect.teams:
        print(teamselect.name)

for groupselect in t.groups:
    totalteams = len(groupselect.teams)
    totalgames = ((totalteams-1)*((totalteams-1)+1)/2)
    print(f"En el {groupselect.name} se van a jugar {int(totalgames)} partidas")
    while len(groupselect.asignedgames) < totalgames:
        minasigned = totalteams
        for teamselect in groupselect.teams:
            if teamselect.asignedgamesc < minasigned:
                minasigned = teamselect.asignedgamesc
                team1selected = teamselect
        minasigned = totalteams
        for teamselect in groupselect.teams:
            if teamselect.asignedgamesc < minasigned and team1selected != teamselect:
                checkgame1 = team1selected.name + " - " + teamselect.name
                checkgame2 = teamselect.name + " - " + team1selected.name
                new = True
                for checkgame0 in groupselect.asignedgames:
                    if checkgame0 == checkgame1 or checkgame0 == checkgame2:
                        new = False
                if new == True:
                    minasigned = teamselect.asignedgamesc
                    team2selected = teamselect
        team1selected.addasignedgamec()
        team2selected.addasignedgamec()
        groupselect.asignedgames.append(team1selected.name + " - " + team2selected.name)

    print(f"Partidos {groupselect.name}") #Te faltaba aquí el .name
    print(groupselect.asignedgames)


#Hasta aqui esta el torneo creado, con los equipos creados, los grupos creados y los equipos repartidos en los grupos


print("Listo")
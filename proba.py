filepath = "valaszok.txt"
fileobject = open(filepath, "r")

#7. feladat
print("A verseny legjobbjai:")
def pontszam_szerint(elem):
    return elem[1]

dijazas=sorted(dijazas, key=pontszam_szerint, reverse=True)

dijazottak_szama=1
helyezes=1
print('{}. díj ({} pont): {}'.format(helyezes, dijazas[i][1], dijazas[i][0]))
i=1
while dijazottak_szama<4:
    if dijazas[i][1]!=dijazas[i-1][1]:
        helyezes+=1
    print('{}. díj ({} pont): {}'.format(helyezes, dijazas[i][1], dijazas[i][0]))
    dijazottak_szama+=1
    i+=1




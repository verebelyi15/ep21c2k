

filepath = "valaszok.txt"
fileobject = open(filepath, "r")

#2. feladat
count_rowes=0
for line in fileobject:
    count_rowes +=1
print("A versenyen",count_rowes-1 ,"versenyző indult.")

#3. feladat
count_rowes=len(filepath)
invalid_data= True
while invalid_data:
    try:
        invalid_data=input("Kérem adja meg a versenyző azonosítóját:").upper()
        i=0
        while i<len(filepath) and filepath[i][0]!=invalid_data:
            i+=1
        if i<len(filepath):
            invalid_data = True
            invalid_data = filepath[i][1]
            print("A versenyző válasza: ", invalid_data)
    except ValueError:
        print("Ilyen kóddal nem indult versenyző.")



#4. feladat


print("BCCCDBBBBCDAAA")
megoldas = "BCCCDBBBBCDAAA"
print("", end="")
for i in range(len(filepath)):
    if filepath[i]==megoldas[i]:
        print("+", end="")
    else:
        print(" ", end="")
print()

#5.feladat
while True:
    try:
        sorszam=int(input("A feladat sorszáma = "))
        if sorszam < 1 or sorszam > 14:
            print("A sorszám helytelen, kérem adjon meg másikat 1 és 14 között.")
    except ValueError:
        print("")
sorszam-=1
szamlalo=0
for fileobject in filepath:
    filepath = filepath[1]
    if filepath[sorszam]==megoldas[sorszam]:
        szamlalo+=1
arany = szamlalo/count_rowes-1
print(f"A feladatra", szamlalo, "fő, a versenyzők" ,arany/100,"%-a adott helyes választ.")



#6.feladat
print("A versenyzők pontszámának meghatározása")
str =[3,3,3,3,3,4,4,4,4,4,5,5,5,6]

def pontszamitas(valasz):
    pontszam=0
    for i in range(len(valasz)):
        if valasz[i]==megoldas[i]:
            pontszam+=pontok[i]
    return pontszam

fv=open('pontok.txt','w')

dijazas=[]
for adat in filepath:
    pontszam = pontszamitas(adat[1])
    print(adat[0],pontszam,file=fv)
    dijazas.append([adat[0],pontszam])
fv.close()



#7. feladat
print("A verseny legjobbjai:")
def pontszam_szerint(elem):
    return elem[1]

dijazas=sorted(dijazas, key=pontszam_szerint, reverse=True)

dijazottak_szama=1
helyezes=1
print("{}. díj ({} pont): {}".format(helyezes, dijazas[i][1], dijazas[i][0]))
i=1
while dijazottak_szama<4:
    if dijazas[i][1]!=dijazas[i-1][1]:
        helyezes+=1
    print("{}. díj ({} pont): {}".format(helyezes, dijazas[i][1], dijazas[i][0]))
    dijazottak_szama+=1
    i+=1
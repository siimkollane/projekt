# töötab
# project

import random
import sys
print("!!!! EESTIKEELSED SÕNAD !!!!")
#Küsib nime
nimi=input("Mis on sinu nimi?:")
print("Tere tulemast",nimi,"aeg mängida poomist!")

#Genereerib sõna
def genereeri_sõna(infile):
    random_sõna= random.choice(open(infile).read().split("\n"))
    return random_sõna
#Poomise mäng
def poomine():
    teema=input("Mis teema sa valid? (loodus, sport, ajalugu):")
    print("Sa valisid teema:",teema)
    if teema=="loodus":
        infile="loodus.txt"
    elif teema=="sport":
        infile="sport.txt"
    elif teema=="ajalugu":
        infile="ajalugu.txt"
    else:
        print("Olen segaduses")
    sõna=genereeri_sõna(infile)
    print(sõna)
    print("Sõnas on",len(sõna),"sõna")
    käike=10
    vastuseid=""


    while käike>0:
    
        valesti=0
    

        for char in sõna:
            if char in vastuseid:
                    print(char)
            
            else:
                print("_")
                valesti += 1
            
        if valesti==0:
            print("Sa võitsid!")
            break
        
        täht=input("Sisestage täht:")
        vastuseid += täht
        if täht not in sõna:
            käike -= 1
            print("Vale")
        if käike==0:
            print("Sa kaotasid")
poomine()

#Uuesti mängimine
while True:
    vastus=input("Tahad sa uuesti mängida? (jah/ei) ")
    if vastus=="jah":
        poomine()
    elif vastus=="ei":
        vastus2=input("Soovid sa mängida kivi-paber-käärid mängu? (jah/ei) ")
        if vastus2=="jah":
            kpk()
        elif vastus=="ei":
            print("Nägemiseni!")
    else:
        print("Ei mõista sinu vastust")
        
#Kivi-paber-käärid



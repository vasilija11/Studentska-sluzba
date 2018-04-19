import datetime

from tabulate import tabulate


def stampaj_tabelu(podaci, zaglavlje):
    print(tabulate(podaci, headers=zaglavlje, tablefmt='orgtbl'))

def stampaj_spisak():

    fakultet = raw_input("Za koji fakultet zelite da dobijete spisak: ")


    baza_fajl = open("baza.db", "r")
    svi_studenti = baza_fajl.readlines()
    baza_fajl.close()

    lista_lista_svih_studenata = []

    for line in svi_studenti:
        linija_bez_praznina = line.strip()
        student_lista = linija_bez_praznina.split(",")

        student_lista_stampa = [student_lista[0] + '/' + student_lista[1],
                                student_lista[2],
                                student_lista[3],
                                student_lista[4]]

        if fakultet:
            if student_lista[4].lower() == fakultet.lower():
                lista_lista_svih_studenata.append(student_lista_stampa)
        else:
            lista_lista_svih_studenata.append(student_lista_stampa)

    stampaj_tabelu(lista_lista_svih_studenata, ["Br. Indexa",
                                                "Ime",
                                                "Prezime",
                                                "Fakultet"])

def dodaj_studenta():

    print("----------------------")
    print("+ DODAVANJE STUDENTA +")
    print("----------------------")
    print("\n")

    ime = raw_input("Unesite ime studenta: ")
    prezime = raw_input("Unesite prezime studenta: ")

    postojeci_fakulteti = ["Matematika", "Elektrotehnika"]
    fakultet = raw_input("Unesite fakultet studenta: ")

    if fakultet not in postojeci_fakulteti:
        print("Fakultet ne postoji!")
        return

    baza_fajl_citanje = open("baza.db", "r")
    svi_studenti = baza_fajl_citanje.readlines()
    baza_fajl_citanje.close()

    baza_fajl_pisanje = open("baza.db", "a+")

    zadnji_upisani = svi_studenti[-1]
    student = zadnji_upisani.split(",")

    trenutno_vrijeme = datetime.datetime.now()
    godina = trenutno_vrijeme.year
    indeks = student[1]

    godina_novog_studenta = str(godina)
    indeks_novog_studenta = str(int(indeks) + 1)

    baza_fajl_pisanje.write(godina_novog_studenta[2:] + ","
                            + indeks_novog_studenta + ","
                            + ime + ","
                            + prezime + ","
                            + fakultet + "\n")
    baza_fajl_pisanje.close()

    print("Uspjesno dodat student " + ime + ' ' + prezime + '.' + "\n")

def obrisi_studenta():

    print("----------------------")
    print("+ OBRISI STUDENTA +")
    print("----------------------")
    print("\n")

    index = raw_input("Unesite indeks studenta: ")


    infile = open('baza.db','r').readlines()
    with open('baza.db','w') as outfile:
        for line in infile:
            student_lista = line.split(",")
            student_lista_stampa = [student_lista[0] + '/' + student_lista[1],
                                    student_lista[2],
                                    student_lista[3],
                                    student_lista[4]]
            if index != student_lista_stampa[0]:
                outfile.write(line)




print("========================")
print("+  STUDENTSKA SLUZBA   +")
print("========================")

while True:

    print(" 1 - Stampaj listu studenata")
    print(" 2 - Dodaj novog studenta")
    print(" 3 - Obrisi studenta")
    print(" 4 - Suspenduj studenta")
    print("=============================")
    komanda = str(input("Unesite zeljenu komandu: "))
    print("\n\n")

    if komanda == "1":
        stampaj_spisak()
    elif komanda == "2":
        dodaj_studenta()
    elif komanda == "3":
        obrisi_studenta()



    print("\n\n\n\n\n")
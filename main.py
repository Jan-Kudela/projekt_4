ukoly = []

def digit_check(digit_nr):
    """funkce kontroluje, zda je vstup číslo a převádí jej na integer"""
    if digit_nr.isdigit():
        digit_intg = int(digit_nr)
        return digit_intg
    else:
        print("Zadaná hodnota musí být číslo.")

def pridat_ukol(name, cont):
    """funkce pro zadání nového úkolu - jeho jména a obsahu"""
    
    ukol_pridani = (name, cont)
    ukoly.append(ukol_pridani)
    print("Úkol přidán.\n")
            

def zobrazit_ukoly():
    """funkce vypíše seznam zadaných úkolů"""
    print("Seznam úkolů:\n")
    if len(ukoly) == 0:
        print("Žádný ukol není zadán.")
    else:
        for index, ukol in enumerate(ukoly):
            print(f"{index+1}. {ukol[0]} - {ukol[1]}")


def odstranit_ukol(number_del):
    """funkce smaže vybraný úkol"""
    if len(ukoly) == 0:
        print("Žádný úkol není aktuálně zadán.")
    else:
        zobrazit_ukoly()
        while True:
            #number_del = input("Zadejte číslo úkolu, který chcete odstranit: ")
            digit_check(number_del)
            #if number_del.isdigit():
                #number_del = int(number_del)
            if number_del not in range(1,len(ukoly)+1):
                print(f"Zadaná hodnota musí být číslo v rozsahu 1 - {len(ukoly)}.")
            else:
                break
           # else:
                #print("Zadaná hodnota musí být číslo v rozsahu 1-4")
                #continue
        vybrany_ukol = ukoly[number_del-1]    
        print(f"Úkol {vybrany_ukol[0]} - {vybrany_ukol[0]} byl odstraněn.")
        ukoly.pop(number_del-1)        


def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu\n")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        while True:
            choice_number = (input("Vyberte možnost (1-4):"))
            choice_nr_checked = digit_check(choice_number)
            #if choice_number.isdigit():
                #choice_number = int(choice_number)
            if choice_nr_checked not in range(1,5):
                print("Zadané číslo musí být v rozsahu 1-4")
            else:
                break
            #else:
                #print("Zadaná hodnota musí být číslo v rozsahu 1-4")
                #continue

        
        if choice_nr_checked == 1:
            while True:
                task_name = input("Zadejte název úkolu:")
                task_cont = input("Zadejte popis úkolu:")
                if not task_name or not task_cont:
                    print("Název úkolu i jeho popis musí být vyplněny.")
                else:
                    pridat_ukol(task_name, task_cont)
                    break

        elif choice_nr_checked == 2:
            zobrazit_ukoly()

        elif choice_nr_checked == 3:
            number_to_del = input(
                "Zadejte číslo úkolu, který chcete odstranit: ")
            odstranit_ukol(number_to_del)

        else:
            print("Program je ukončen.")
            break

if __name__ == "__main__":
    hlavni_menu()
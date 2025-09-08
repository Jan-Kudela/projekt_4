ukoly = []

def pridat_ukol():
    while True:
        task_name = input("Zadejte název úkolu:")
        task_cont = input("Zadejte popis úkolu:")
        
        if not task_name or not task_cont:
            print("Název úkolu i jeho popis musí být vyplněny.")
            continue
       
        else:
            ukol_pridani = (task_name, task_cont)
            ukoly.append(ukol_pridani)
            print("Úkol přidán.\n")
            break

def zobrazit_ukoly():
    for index, ukol in enumerate(ukoly):
        print(f"Seznam úkolů:\n{index+1}. {ukol[0]} - {ukol[1]}")


def odstranit_ukol():
    zobrazit_ukoly()
    while True:
        number_del = input("Zadejte číslo úkolu, který chcete odstranit: ")
        if number_del.isdigit():
            number_del = int(number_del)
            break
        else:
            print(f"Zadaná hodnota musí být číslo v rozsahu {len(ukoly)}.")
            continue
    
    print(f"Úkol {ukoly[number_del-1]} byl odstraněn.")
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
            if choice_number.isdigit():
                choice_number = int(choice_number)
                if choice_number not in range(1,5):
                    print("Zadané číslo musí být v rozsahu 1-4")
                else:
                    break
            else:
                print("Zadaná hodnota musí být číslo v rozsahu 1-4")
                continue

        
        if choice_number == 1:
            pridat_ukol()
        elif choice_number == 2:
            zobrazit_ukoly()
        elif choice_number == 3:
            odstranit_ukol()

hlavni_menu()
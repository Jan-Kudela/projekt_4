ukoly = []

def hlavni_menu():
    print("Správce úkolů - Hlavní menu\n")
    print("1.Přidat nový úkol")
    print("2. Zobrait všechny úkoly")
    print("3. Odstranit úkol")
    print("Konec programu")
    choice_number = input("Vyberte možnost (1-4):")

hlavni_menu()

def pridat_ukol():
    task_name = input("Zadejte název úkolu:")
    task_cont = input("Zadejte popis úkolu:")
    if not task_name or not task_cont:
        print("Název a popis úkolu nesmí být prázdné.")
        return
    else:
        ukol_pridani = (task_name, task_cont)
        ukoly.append(ukol_pridani)
        print("Úkol přidán.")

pridat_ukol()
print(ukoly)

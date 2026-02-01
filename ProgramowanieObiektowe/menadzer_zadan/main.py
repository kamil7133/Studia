
from functions import add_task, start_task, finish_task, show_tasks, ensure_file

MENU = '''
Wybierz akcję:
1. Dodaj zadanie
2. Rozpocznij zadanie
3. Zakończ zadanie
4. Pokaż zadania
5. Wyjście
'''

def main():
    ensure_file()
    while True:
        print(MENU)
        choice = input("Twoj wybor: ")
        if choice == '1':
            title = input("Podaj tytul nowego zadania: ")
            add_task(title)
        elif choice == '2':
            title = input("Podaj tytul zadania do rozpoczecia: ")
            start_task(title)
        elif choice == '3':
            title = input("Podaj tytul zadania do zakonczenia: ")
            finish_task(title)
        elif choice == '4':
            show_tasks()
        elif choice == '5':
            print("Do zobaczenia!")
            break
        else:
            print("Nieprawidlowy wybor. Sprobuj ponownie.")

if __name__ == "__main__":
    main()

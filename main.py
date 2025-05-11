from analyzer import load_player_data, find_player_by_name, get_top_scorers
from exceptions import PlayerNotFoundError, FileNotFoundError
import logging
import sys

# konfiguracja logowania
logging.basicConfig(
    filename="logs/error.log",
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s:%(message)s"
)

def print_player(p):
    print(f"\nZnaleziono zawodnika:")
    print(f"  Imię:    {p['name']}")
    print(f"  Drużyna: {p['team']}")
    print(f"  Gole:    {p['goals']}")
    print(f"  Asysty:  {p['assists']}")
    print(f"  Mecze:   {p['matches_played']}\n")

def print_top(players):
    top = get_top_scorers(players)
    print("\n Top 3 strzelców:")
    for i, p in enumerate(top, 1):
        print(f"  {i}. {p['name']} – {p['goals']} goli")
    print()

def main():
    # Wczytaj dane
    try:
        players, rejected = load_player_data("data/players.csv")
    except FileNotFoundError as e:
        print(f"Błąd: {e}")
        logging.error(f"FileNotFoundError: {e}")
        sys.exit(1)

    print("Dane wczytane pomyślnie.\n")

    # Proste menu
    while True:
        print("Wybierz opcję:")
        print("  1. Wyszukaj zawodnika")
        print("  2. Pokaż Top 3 strzelców")
        print("  3. Wyjdź")
        choice = input("Twój wybór [1-3]: ").strip()

        if choice == "1":
            name = input("Podaj imię i nazwisko zawodnika: ").strip()

            # najpierw: czy był odrzucony z powodu złego formatu
            for rej_name, err_type, err_msg in rejected:
                if rej_name.lower() == name.lower():
                    print(f"\nBłąd danych dla {rej_name}!\n{err_type}: {err_msg}\n")
                    logging.warning(f"{err_type}: {err_msg}")
                    break
            else:
                # jeśli nie odrzucony – szukamy w poprawnych
                try:
                    p = find_player_by_name(players, name)
                    print_player(p)
                except PlayerNotFoundError as e:
                    print(f"\nBłąd: {e}\n")
                    logging.warning(f"PlayerNotFoundError: {e}")
                except Exception as e:
                    print(f"\nNieoczekiwany błąd: {e}\n")
                    logging.exception("UnexpectedError")

        elif choice == "2":
            print_top(players)

        elif choice == "3":
            print("\nDo zobaczenia!")
            break

        else:
            print("\nNiepoprawny wybór, spróbuj ponownie.\n")

if __name__ == "__main__":
    main()
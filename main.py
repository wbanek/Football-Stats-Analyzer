from analyzer import load_player_data, find_player_by_name
from exceptions import FootballDataError, PlayerNotFoundError
import logging

logging.basicConfig(filename="Logs/error.log", level=logging.ERROR)

def main():
    try:
        players = load_player_data("Data/players.csv")
        print("Dane wczytane pomyślnie.")
        name = input("Podaj imię i nazwisko zawodnika, którego chcesz znaleźć: ")

        try:
            player = find_player_by_name(players, name)
            print(f"\nZnaleziono zawodnika:")
            print(f"Imię: {player['name']}")
            print(f"Drużyna: {player['team']}")
            print(f"Gole: {player['goals']}")
            print(f"Asysty: {player['assists']}")
            print(f"Mecze: {player['matches_played']}")
        except PlayerNotFoundError as e:
            print(f"Błąd: {e}")
            logging.warning(f"Zawodnik nie znaleziony: {name}")

    except FootballDataError as e:
        print(f"Błąd w danych: {e}")
        logging.exception("Błąd domenowy")
    except Exception as e:
        print("Nieoczekiwany błąd.")
        logging.exception("Nieznany wyjątek")

if __name__ == "__main__":
    main()
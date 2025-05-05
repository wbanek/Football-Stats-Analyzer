import csv
import logging
from exceptions import InvalidStatFormatError, PlayerNotFoundError

def find_player_by_name(players, name):
    for player in players:
        if player["name"].lower() == name.lower():
            return player
    raise PlayerNotFoundError(f"Nie znaleziono zawodnika o imieniu: {name}")

def load_player_data(filepath):
    players = []
    rejected = []  # tu zapisujemy zawodników z błędnymi danymi

    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    row['goals'] = int(row.get('goals', 0) or 0)
                    row['assists'] = int(row.get('assists', 0) or 0)
                    row['matches_played'] = int(row.get('matches_played', 0) or 0)
                    players.append(row)
                except (ValueError, KeyError) as e:
                    name = row.get('name', '[brak imienia]')
                    rejected.append((name, type(e).__name__, str(e)))
                    logging.warning(f"Błąd w danych zawodnika {name}: {e}")
                    continue
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {filepath}")
        raise

    return players, rejected

def get_top_scorers(players, top_n=3):
    return sorted(players, key=lambda p: p['goals'], reverse=True)[:top_n]
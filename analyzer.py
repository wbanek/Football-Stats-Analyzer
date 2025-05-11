import csv
from exceptions import PlayerNotFoundError, InvalidStatFormatError, DataFileNotFoundError

def _load_raw_rows(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except OSError as e:
        raise DataFileNotFoundError(f"Nie znaleziono pliku: {path}") from e

def get_player_stats(path, name):
    """
    Ładuje CSV, szuka wiersza o danym name i konwertuje statystyki.
    Jeśli któryś krok się nie uda – rzuca wyjątek.
    """
    rows = _load_raw_rows(path)
    for row in rows:
        if row.get("name", "").strip().lower() == name.strip().lower():
            # mamy wiersz – próbujemy skonwertować
            try:
                goals = int(row.get("goals", "") or 0)
            except ValueError as e:
                raise InvalidStatFormatError(f"{name}: niepoprawna wartość w polu 'goals' ({row.get('goals')})") from e
            try:
                assists = int(row.get("assists", "") or 0)
            except ValueError as e:
                raise InvalidStatFormatError(f"{name}: niepoprawna wartość w polu 'assists' ({row.get('assists')})") from e
            try:
                matches = int(row.get("matches_played", "") or 0)
            except ValueError as e:
                raise InvalidStatFormatError(f"{name}: niepoprawna wartość w polu 'matches_played' ({row.get('matches_played')})") from e

            # dodatkowa walidacja
            if matches == 0 and (goals>0 or assists>0):
                raise InvalidStatFormatError(f"{name}: ma {goals} goli i {assists} asyst, ale zero meczów")

            # wszystko ok
            return {
                "name": name,
                "team": row.get("team",""),
                "goals": goals,
                "assists": assists,
                "matches_played": matches
            }

    # jeśli nie znaleziono
    raise PlayerNotFoundError(f"Nie znaleziono zawodnika: {name}")

def get_top_scorers(path, top_n=3):
    """
    Zwraca listę top_n w postaci tych samych słowników co get_player_stats,
    pomijając rekordy z błędami (rzuca wyjątki, które GUI może łapać).
    """
    rows = _load_raw_rows(path)
    stats = []
    for row in rows:
        name = row.get("name","").strip()
        try:
            stats.append(get_player_stats(path, name))
        except InvalidStatFormatError:
            # pomijamy tylko te z błędami formatu, ale nie przerywamy
            continue
    return sorted(stats, key=lambda p: p["goals"], reverse=True)[:top_n]
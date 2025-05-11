class InvalidStatFormatError(Exception):
    """Błąd nieprawidłowego formatu statystyk."""
class PlayerNotFoundError(Exception):
    """Gdy zawodnik nie istnieje w danych."""
class DataFileNotFoundError(Exception):
    """Gdy pliku CSV nie znaleziono."""
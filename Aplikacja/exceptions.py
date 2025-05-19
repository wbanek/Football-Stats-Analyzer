class FootballDataError(Exception):
    """Bazowa klasa dla wyjątków związanych z danymi piłkarskimi."""

class PlayerNotFoundError(Exception):
    """Gdy zawodnik nie istnieje w danych."""

class DataFileNotFoundError(Exception):
    """Gdy pliku CSV nie znaleziono."""

class GoalsFormatError(FootballDataError):
    """Niepoprawny format liczby goli."""

class AssistsFormatError(FootballDataError):
    """Niepoprawny format liczby asyst."""

class MatchesPlayedFormatError(FootballDataError):
    """Niepoprawny format liczby rozegranych meczów."""

class InvalidStatFormatError(FootballDataError):
    """Błąd nieprawidłowego formatu statystyk."""
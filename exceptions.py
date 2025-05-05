class FootballDataError(Exception):
    """Bazowy wyjątek dla błędów aplikacji."""

class PlayerNotFoundError(FootballDataError):
    """Gdy nie znaleziono zawodnika."""

class InvalidStatFormatError(FootballDataError):
    """Gdy statystyki zawodnika mają nieprawidłowy format."""
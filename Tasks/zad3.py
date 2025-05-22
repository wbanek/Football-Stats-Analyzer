import logging

def setup_logger():
    """
    TODO: skonfiguruj logger tak, aby:
      - zapisywał wpisy do pliku 'file_reader.log'
      - domyślny poziom to DEBUG
      - format: TIMESTAMP LEVEL: MESSAGE
    """


def count_lines(filename: str) -> int:
    """
    Zlicza linie w pliku o podanej nazwie i loguje:
      - INFO  "Starting count_lines: <filename>"
      - ERROR z exc_info=True jeśli FileNotFoundError
      - INFO  "Finished count_lines: <n> lines"
      - INFO  "Zadanie zostało wykonane poprawnie"
    Plik musi znajdować się w bieżącym katalogu.
    """
    logging.info(f"Starting count_lines: {filename}")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = sum(1 for _ in f)
    except FileNotFoundError as e:
        # TODO: zaloguj ERROR z trace (exc_info=True)
        # TODO: przekaż wyjątek dalej
        raise
    else:
        # TODO: zaloguj INFO: Finished count_lines
        # TODO: zaloguj INFO: Zadanie zostało wykonane poprawnie
        return lines

def main():
    setup_logger()
    print("Czytnik plików z loggerem (wpisz 'exit').")
    while True:
        filename = input("Podaj nazwę pliku (w bieżącym katalogu): ").strip()
        if filename.lower() == "exit":
            break
        try:
            n = count_lines(filename)
        except FileNotFoundError as e:
            print(f"Błąd: {e}")
        else:
            print(f"Liczba linii: {n}")
        finally:
            print("Operacja zakończona.\n")

if __name__ == "__main__":
    main()
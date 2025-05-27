# ------------------------------------------------------------------------
# TODO: zdefiniuj własny wyjątek EmptyInputError
# ------------------------------------------------------------------------


def count_words(text: str) -> int:
    """
    Zwraca liczbę słów w tekście.
    TODO:
      - jeśli text jest pusty lub samymi spacjami, rzucić EmptyInputError
    """
    # TODO: dodać walidację EmptyInputError
    words = text.split()
    return len(words)

def main():
    print("Licznik słów (wpisz 'exit' aby zakończyć).")
    while True:
        text = input("Podaj zdanie: ")
        if text.lower() in ("exit",):
            print("Kończę działanie programu.")
            break
        try:
            count = count_words(text)
        except Exception as e:
            # TODO: złapać EmptyInputError i ewentualnie inne
            print(f"Błąd: {e}")
        else:
            print(f"Liczba słów: {count}\n")
        finally:
            print("Operacja zakończona.\n")

if __name__ == "__main__":
    main()
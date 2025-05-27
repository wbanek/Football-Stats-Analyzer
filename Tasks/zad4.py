class OperationError(Exception):
    pass

def process_item(item):
    """
    Funkcja, która może rzucać różne wyjątki zależnie od typu i wartości item.
    Uzupełnij implementację tak, aby:
    - jeśli item == "value" -> rzuć ValueError z odpowiednim komunikatem,
    - jeśli item == "type" -> rzuć TypeError,
    - jeśli item == "zero" -> wykonaj dzielenie przez zero (ZeroDivisionError),
    - jeśli item == "custom" -> rzuć OperationError,
    - w przeciwnym wypadku zwróć tekst "Przetworzono: {item}".
    """
    # TODO: uzupełnij tę funkcję
    pass

def process_items(items):
    """
    Przetwarza listę elementów, łapie wyjątki i zlicza ich wystąpienia.
    Uzupełnij obsługę wyjątków tak, aby:
    - dla każdego wyjątku z ValueError, TypeError, ZeroDivisionError, OperationError
      zwiększyć licznik w słowniku exception_counts,
    - jeśli nie wystąpi wyjątek, wypisać wynik działania process_item,
    - po przetworzeniu wszystkich elementów zwrócić słownik exception_counts.
    """
    exception_counts = {
        "ValueError": 0,
        "TypeError": 0,
        "ZeroDivisionError": 0,
        "OperationError": 0
    }

    for item in items:
        try:
            result = process_item(item)
            print(result)
        except ...:  # TODO: uzupełnij obsługę wyjątków i aktualizację exception_counts
            pass
    
    return exception_counts

def main():
    items = ["hello", "value", "type", "world", "zero", "custom", "value"]
    counts = process_items(items)
    print("\nStatystyki wyjątków:")
    for exc, count in counts.items():
        print(f"{exc}: {count}")

if __name__ == "__main__":
    main()
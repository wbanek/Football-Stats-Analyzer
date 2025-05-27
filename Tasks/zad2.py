# ------------------------------------------------------------------------------------
# TODO: zdefiniuj tu własny wyjątek UnsupportedOperationError oraz InvalidNumberError
# ------------------------------------------------------------------------------------



def safe_convert_to_float(s: str) -> float:
    """
    Próbuje zamienić s na float.
    TODO: obsłużyć ValueError i podnieść własny wyjątek InvalidNumberError
    """
    return float(s)

def calculate(x_str: str, y_str: str, op: str) -> float:
    """
    Wykonuje x op y. Operator musi być jednym z: +, -, *, /.
    TODO:
      - obsłużyć niepoprawną konwersję do float (ValueError)
      - obsłużyć dzielenie przez zero (ZeroDivisionError)
      - rzucić UnsupportedOperationError dla nieznanego op
    """
    x = safe_convert_to_float(x_str)
    y = safe_convert_to_float(y_str)

    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y
    else:
        # TODO: zamiast Exception, rzucić UnsupportedOperationError
        raise Exception(f"Unsupported operation: {op}")

def main():
    print("Kalkulator (wpisz 'exit' aby zakończyć).")
    while True:
        line = input("Podaj działanie: ").strip()
        if line.lower() in ("exit", "quit"):
            print("Kończę działanie kalkulatora.")
            break

        parts = line.split()
        if len(parts) != 3:
            print("Niepoprawny format. Użyj: <liczba> <operator> <liczba>")
            continue

        x_str, op, y_str = parts
        try:
            result = calculate(x_str, y_str, op)
        except Exception as e:
            # TODO: złap konkretne wyjątki (InvalidNumberError, ZeroDivisionError, UnsupportedOperationError)
            print(f"Błąd: {e}")
            continue
        else:
            print(f"Wynik: {result}")
        finally:
            print("Operacja zakończona.\n")

if __name__ == "__main__":
    main()
import tkinter as tk
from analyzer import load_player_data, find_player_by_name, get_top_scorers
from exceptions import PlayerNotFoundError
import logging

# Konfiguracja logowania
logging.basicConfig(filename="logs/error.log", level=logging.WARNING)

# Wczytanie danych i odrzuconych zawodników
players, rejected_players = load_player_data("data/players.csv")

# Funkcje interfejsu
def search_player():
    name = entry.get()
    try:
        player = find_player_by_name(players, name)
        name_label.config(text=f"Zawodnik: {player['name']}")
        team_label.config(text=f"Drużyna: {player['team']}")
        goals_label.config(text=f"Gole: {player['goals']}")
        assists_label.config(text=f"Asysty: {player['assists']}")
        matches_label.config(text=f"Mecze: {player['matches_played']}")
        result_label.config(text="")
        error_label.config(text="")
    except PlayerNotFoundError as e:
        # Sprawdź, czy zawodnik był w pliku, ale z błędnymi danymi
        for rejected_name, err_type, err_msg in rejected_players:
            if rejected_name.lower() == name.lower():
                error_label.config(text=f"{rejected_name} był w pliku, ale został odrzucony:\n{err_type}: {err_msg}")
                clear_result_fields()
                return
        # Zwykły brak zawodnika
        error_label.config(text=f"{type(e).__name__}: {e}")
        clear_result_fields()
        logging.warning(f"{type(e).__name__}: {e}")
    except Exception as e:
        error_label.config(text=f"{type(e).__name__}: {e}")
        clear_result_fields()
        logging.exception(f"{type(e).__name__}: {e}")

def show_top_scorers():
    top_players = get_top_scorers(players)
    result = "🏆 Top 3 strzelców:\n"
    for i, player in enumerate(top_players, 1):
        result += f"{i}. {player['name']} - {player['goals']} goli\n"
    result_label.config(text=result)
    clear_result_fields()
    error_label.config(text="")

def clear_result_fields():
    name_label.config(text="")
    team_label.config(text="")
    goals_label.config(text="")
    assists_label.config(text="")
    matches_label.config(text="")

# Tworzenie GUI
root = tk.Tk()
root.title("Football Stats Analyzer")
root.geometry("420x400")
root.resizable(False, False)

# Instrukcja
instruction_label = tk.Label(root, text="🔍 Wpisz imię i nazwisko zawodnika:")
instruction_label.pack(pady=(15, 5))

# Pole tekstowe
entry = tk.Entry(root, width=40)
entry.pack(pady=(0, 10))

# Przycisk wyszukiwania
search_button = tk.Button(root, text="Szukaj zawodnika", command=search_player)
search_button.pack(pady=5)

# Przycisk top 3
top_button = tk.Button(root, text="Top 3 strzelców", command=show_top_scorers)
top_button.pack(pady=5)

# Ramka na wynik zawodnika
result_frame = tk.Frame(root)
result_frame.pack(pady=(15, 5))

name_label = tk.Label(result_frame, text="", font=("Helvetica", 12, "bold"))
team_label = tk.Label(result_frame, text="", font=("Helvetica", 11))
goals_label = tk.Label(result_frame, text="", font=("Helvetica", 11))
assists_label = tk.Label(result_frame, text="", font=("Helvetica", 11))
matches_label = tk.Label(result_frame, text="", font=("Helvetica", 11))

name_label.pack(anchor="w")
team_label.pack(anchor="w")
goals_label.pack(anchor="w")
assists_label.pack(anchor="w")
matches_label.pack(anchor="w")

# Pole tekstowe do wyświetlania top 3
result_label = tk.Label(root, text="", justify="left", font=("Helvetica", 11))
result_label.pack(pady=(5, 5))

# Label do wyświetlania błędów
error_label = tk.Label(root, text="", fg="red", font=("Helvetica", 10, "italic"))
error_label.pack(pady=(5, 10))

# Start pętli aplikacji
root.mainloop()
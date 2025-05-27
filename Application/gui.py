import tkinter as tk
import customtkinter as ctk
import logging

from analyzer import get_player_stats, get_top_scorers
from exceptions import PlayerNotFoundError, InvalidStatFormatError, DataFileNotFoundError, GoalsFormatError, AssistsFormatError, MatchesPlayedFormatError

# logi
logging.basicConfig(filename="logs/error.log", level=logging.ERROR)

def handle_error(exc):
    result_frame.configure(border_color="red")
    result_label.configure(text="")
    error_label.configure(text=f"{exc.__class__.__name__}: {exc}", text_color="red")
    logging.error(f"{exc.__class__.__name__}: {exc}")

def search_player():
    name = entry.get().strip()
    try:
        p = get_player_stats("data/players.csv", name)
        text = (
            f"Zawodnik: {p['name']}\n"
            f"Drużyna: {p['team']}\n"
            f"Gole: {p['goals']}\n"
            f"Asysty: {p['assists']}\n"
            f"Mecze: {p['matches_played']}"
        )
        result_frame.configure(border_color="green")
        result_label.configure(text=text)
        error_label.configure(text="")
    except (PlayerNotFoundError, InvalidStatFormatError, DataFileNotFoundError) as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)

def show_top_scorers():
    try:
        top = get_top_scorers("data/players.csv")
        text = "🏆 Top 3 strzelców:\n" + "\n".join(
            f"{i+1}. {p['name']} – {p['goals']} goli" for i,p in enumerate(top)
        )
        result_frame.configure(border_color="blue")
        result_label.configure(text=text)
        error_label.configure(text="")
    except DataFileNotFoundError as e:
        handle_error(e)
    except Exception as e:
        handle_error(e)

def clear_all():
    entry.delete(0, tk.END)
    result_frame.configure(border_color="gray")
    result_label.configure(text="")
    error_label.configure(text="")

def throw_test_exception():
    import random
    exceptions = [
        ZeroDivisionError("Przykładowy ZeroDivisionError"),
        KeyError("Przykładowy KeyError"),
        GoalsFormatError("Przykładowy GoalsFormatError"),
        AssistsFormatError("Przykładowy AssistsFormatError"),
        MatchesPlayedFormatError("Przykładowy MatchesPlayedFormatError"),
        PlayerNotFoundError("Przykładowy PlayerNotFoundError"),
    ]
    exc = random.choice(exceptions)
    try:
        raise exc
    except Exception as e:
        handle_error(e)

# --- budowa GUI ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Football Stats Analyzer")
root.geometry("420x550")
root.resizable(False, False)

ctk.CTkLabel(root, text="🔍 Wpisz imię i nazwisko zawodnika:", font=("Helvetica", 12))\
    .pack(pady=(15,5))

entry = ctk.CTkEntry(root, width=250, font=("Helvetica", 12))
entry.pack(pady=(0,10))

ctk.CTkButton(root, text="Szukaj zawodnika", command=search_player, width=200)\
    .pack(pady=10)
ctk.CTkButton(root, text="Top 3 strzelców", command=show_top_scorers, width=200)\
    .pack(pady=10)
ctk.CTkButton(root, text="Wyczyść", command=clear_all, width=200)\
    .pack(pady=10)
ctk.CTkButton(root, text="Rzuć testowy wyjątek", command=throw_test_exception, width=200)\
    .pack(pady=10)

result_frame = ctk.CTkFrame(root, corner_radius=10, border_width=2, border_color="gray")
result_frame.pack(pady=(15,10), padx=20, fill="both", expand=True)

result_label = ctk.CTkLabel(
    result_frame,
    text="",
    font=("Helvetica", 15),
    wraplength=300,       # maksymalna szerokość w px przed złamaniem
    justify="center"        # wyrównanie tekstu
)
result_label.pack(pady=10, padx=10, fill="both", expand=True)

error_label = ctk.CTkLabel(
    result_frame,
    text="",
    font=("Helvetica", 15, "italic"),
    text_color="red",
    wraplength=300,
    justify="center"
)
error_label.pack(pady=(5,10), padx=10, fill="both", expand=True)

root.mainloop()
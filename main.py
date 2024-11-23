import tkinter as tk
from tkinter import ttk, messagebox

# Date despre profesii și întrebări complexe
professions = {
    "Programator": {
        "description": (
            "Un programator este un profesionist care scrie și întreține codul necesar pentru a dezvolta aplicații software, "
            "site-uri web și sisteme informatice. Aceasta implică rezolvarea problemelor logice complexe, utilizarea limbajelor "
            "de programare (precum Python, Java, C++) și colaborarea în echipe de dezvoltare."
        ),
        "questions": [
            "Îți place să rezolvi probleme logice complexe?",
            "Ai experiență în cel puțin un limbaj de programare (Python, Java, etc.)?",
            "Te simți confortabil lucrând independent la proiecte mari?",
            "Poți găsi soluții creative pentru probleme tehnice?",
            "Ai interes să înveți constant tehnologii noi în IT?"
        ]
    },
    "Doctor": {
        "description": (
            "Un doctor este un specialist medical care diagnostică, tratează și previne bolile și afecțiunile pacienților. "
            "Aceasta presupune cunoștințe aprofundate în științele medicale, empatie și abilități excelente de comunicare."
        ),
        "questions": [
            "Ești empatic și înțelegi nevoile pacienților?",
            "Ai interes pentru anatomie, biologie sau farmacologie?",
            "Poți lucra eficient sub presiune în situații critice?",
            "Te simți confortabil să comunici cu pacienții și familiile lor?",
            "Ai rezistență la un program de lucru intens și neregulat?"
        ]
    },
    "Profesor": {
        "description": (
            "Profesorii sunt responsabili pentru predarea și ghidarea elevilor sau studenților. "
            "Aceștia proiectează lecții, evaluează performanțele și sprijină dezvoltarea personală a cursanților."
        ),
        "questions": [
            "Îți place să explici concepte complexe altor persoane?",
            "Poți adapta modul de predare pentru diferite tipuri de elevi?",
            "Ai răbdare și bune abilități de comunicare?",
            "Te simți confortabil să lucrezi în fața unui public?",
            "Ai interes pentru educație și dezvoltarea altora?"
        ]
    },
    "Designer Grafic": {
        "description": (
            "Un designer grafic creează elemente vizuale care comunică idei și mesaje prin imagini, "
            "culori și fonturi. Aceasta include designul de logo-uri, postere, site-uri web și alte materiale vizuale."
        ),
        "questions": [
            "Ai o gândire creativă și atenție la detalii?",
            "Îți place să lucrezi cu software grafic precum Adobe Photoshop sau Illustrator?",
            "Poți crea designuri vizuale atractive conform cerințelor clienților?",
            "Ai cunoștințe despre tipografie și teoria culorilor?",
            "Poți lucra bine sub presiunea termenelor limită?"
        ]
    },
    "Inginer Mecanic": {
        "description": (
            "Inginerii mecanici proiectează, analizează și întrețin sisteme mecanice complexe, precum mașini, motoare și echipamente industriale. "
            "Aceștia combină cunoștințe în matematică, fizică și inginerie pentru a rezolva probleme tehnice."
        ),
        "questions": [
            "Ai o înclinație pentru matematică și științe aplicate?",
            "Te interesează proiectarea și analiza structurilor mecanice?",
            "Poți identifica și rezolva probleme tehnice complexe?",
            "Ai experiență sau interes pentru lucrul cu mașini sau echipamente industriale?",
            "Poți lucra eficient în echipe interdisciplinare?"
        ]
    }
}


# Funcții
def start_questionnaire(profession):
    """Lansează întrebările pentru profesia selectată."""
    profession_data = professions[profession]
    score = 0

    for question in profession_data["questions"]:
        answer = messagebox.askyesno("Întrebare", question)
        if answer:
            score += 1

    # Verificăm dacă testul este trecut
    if score >= 4:
        messagebox.showinfo("Succes", f"Ai trecut testul pentru profesia {profession}! Scor: {score}/5")
        save_to_history(profession, score)
    else:
        messagebox.showinfo("Eșec", f"Nu ai trecut testul pentru profesia {profession}. Scor: {score}/5")


def save_to_history(profession, score):
    """Salvează selecția utilizatorului în fișierul de istoric."""
    with open("istoric.txt", "a") as file:
        file.write(f"{profession}: {score}/5\n")
    messagebox.showinfo("Istoric", "Rezultatul a fost salvat în istoric.")


# Crearea interfeței grafice
root = tk.Tk()
root.title("Sistem Expert - Selectarea unei Profesii")
root.geometry("1200x700")
root.configure(bg="#282c34")

# Stil personalizat
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12), background="#282c34", foreground="white")
style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
style.configure("TFrame", background="#282c34")

# Titlu
title_label = tk.Label(root, text="Sistem Expert pentru Selectarea unei Profesii", font=("Helvetica", 18, "bold"),
                       bg="#61afef", fg="white", pady=10)
title_label.pack(fill="x")

# Secțiune cu scrollbar
scroll_frame = tk.Frame(root, bg="#282c34")
scroll_frame.pack(fill="both", expand=True, padx=20, pady=10)

canvas = tk.Canvas(scroll_frame, bg="#282c34", highlightthickness=0)
scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#282c34")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Profesii în cadrul scrollabil
for profession, data in professions.items():
    frame = tk.Frame(scrollable_frame, bg="#3e4451", pady=10, padx=10)
    frame.pack(fill="x", pady=10)

    # Titlu profesie
    profession_title = tk.Label(frame, text=profession, font=("Helvetica", 16, "bold"), bg="#3e4451", fg="#98c379")
    profession_title.pack(anchor="w")

    # Descriere profesie
    profession_desc = tk.Label(frame, text=data["description"], font=("Helvetica", 12), bg="#3e4451", fg="white",
                               wraplength=1000)
    profession_desc.pack(anchor="w", pady=5)

    # Buton pentru întrebări
    start_button = tk.Button(frame, text="Răspunde la întrebări", command=lambda p=profession: start_questionnaire(p),
                             bg="#61afef", fg="white", font=("Helvetica", 12, "bold"))
    start_button.pack(side="right", padx=10)

# Rulare aplicație
root.mainloop()

# todo.py

TODO_FILE = "ukoly.txt"

def nacti_ukoly():
    ukoly = []
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            for radek in f:
                radek = radek.strip()
                if radek.startswith("[x] "):
                    stav = True
                    text = radek[4:]
                elif radek.startswith("[ ] "):
                    stav = False
                    text = radek[4:]
                else:
                    continue  # Neplatný formát řádku
                ukoly.append({"text": text.strip(), "hotovo": stav})
    except FileNotFoundError:
        pass
    return ukoly

def uloz_ukoly(ukoly):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        for ukol in ukoly:
            stav = "[✔️]" if ukol["hotovo"] else "[x]"
            f.write(f"{stav} {ukol['text']}\n")

def zobraz_ukoly(ukoly):
    if not ukoly:
        print("🟦 Žádné úkoly.")
        return
    print("📌 Seznam úkolů:")
    for i, ukol in enumerate(ukoly, 1):
        stav = "✔️" if ukol["hotovo"] else "❌"
        print(f"{i}. {stav} {ukol['text']}")

def pridej_ukol(ukoly):
    text = input("Zadej nový úkol: ").strip()
    if text:
        ukoly.append({"text": text, "hotovo": False})
        uloz_ukoly(ukoly)
        print("✅ Úkol přidán.")
    else:
        print("⚠️ Úkol nemůže být prázdný.")

def odstran_ukol(ukoly):
    zobraz_ukoly(ukoly)
    try:
        cislo = int(input("Zadej číslo úkolu k odstranění: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            uloz_ukoly(ukoly)
            print(f"🗑️ Úkol \"{odstraneny['text']}\" byl odstraněn.")
        else:
            print("⚠️ Neplatné číslo.")
    except ValueError:
        print("⚠️ Zadej platné číslo.")

def oznac_hotovy(ukoly):
    zobraz_ukoly(ukoly)
    try:
        cislo = int(input("Zadej číslo úkolu k označení jako hotový: "))
        if 1 <= cislo <= len(ukoly):
            ukoly[cislo - 1]["hotovo"] = True
            uloz_ukoly(ukoly)
            print("☑️ Úkol označen jako hotový.")
        else:
            print("⚠️ Neplatné číslo.")
    except ValueError:
        print("⚠️ Zadej platné číslo.")

def menu():
    ukoly = nacti_ukoly()
    while True:
        print("\n📋 MENU")
        print("1 - Zobrazit úkoly")
        print("2 - Přidat úkol")
        print("3 - Odstranit úkol")
        print("4 - Označit jako hotový")
        print("5 - Ukončit\n")

        volba = input("Vyber akci (1-5): ").strip()

        if volba == "1":
            zobraz_ukoly(ukoly)
        elif volba == "2":
            pridej_ukol(ukoly)
        elif volba == "3":
            odstran_ukol(ukoly)
        elif volba == "4":
            oznac_hotovy(ukoly)
        elif volba == "5":
            print("💾 Úkoly uloženy. Na shledanou!")
            break
        else:
            print("❌ Neplatná volba.")

if __name__ == "__main__":
    menu()

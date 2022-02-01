from menu import Menu
import os
from pathlib import Path
os.chdir(Path(__file__).parent)



def app():
    menu1 = Menu()
    # menu1.create_menu("./restaurant_db") # that's for the DB


    # Menu Zeigen food
    # User Wünsche Food
    # Menu Zeigen Drink
    # User Wünsche Drinks
    # Rechnung zeigen
    # Die Bestellung in TXT File (Normalerweise müssen wir das in Datenbanken schreiben)

if __name__ == "__main__":
    app()


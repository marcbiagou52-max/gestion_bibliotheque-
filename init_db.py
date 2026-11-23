"""Crée la base de données et insère les romans.
Utilisation :  python init_db.py
"""
import mysql.connector
from config import DB_CONFIG


def main():
    # Connexion sans choisir de base (elle sera créée par le script SQL)
    config = dict(DB_CONFIG)
    config.pop("database")
    conn = mysql.connector.connect(**config)
    curseur = conn.cursor()

    with open("database.sql", encoding="utf-8") as f:
        lignes = [l for l in f.read().splitlines() if not l.strip().startswith("--")]
    commandes = "\n".join(lignes).split(";")

    for commande in commandes:
        if commande.strip():
            curseur.execute(commande)

    conn.commit()
    curseur.close()
    conn.close()
    print("Base 'bibliotheque' créée avec succès !")


if __name__ == "__main__":
    main()

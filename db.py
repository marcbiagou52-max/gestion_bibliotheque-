import mysql.connector
from config import DB_CONFIG


def connecter():
    return mysql.connector.connect(**DB_CONFIG)


def lire(requete, params=()):
    """Exécute un SELECT et renvoie une liste de dictionnaires."""
    conn = connecter()
    curseur = conn.cursor(dictionary=True)
    curseur.execute(requete, params)
    resultat = curseur.fetchall()
    curseur.close()
    conn.close()
    return resultat


def ecrire(requete, params=()):
    """Exécute un INSERT / UPDATE / DELETE et renvoie l'id créé."""
    conn = connecter()
    curseur = conn.cursor()
    curseur.execute(requete, params)
    conn.commit()
    dernier_id = curseur.lastrowid
    curseur.close()
    conn.close()
    return dernier_id

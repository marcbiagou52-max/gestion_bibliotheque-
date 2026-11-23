from datetime import date, timedelta
from db import lire, ecrire
from config import DUREE_EMPRUNT

BASE_EMPRUNTS = """
    SELECT em.id, n.titre, m.nom, m.prenom, em.date_emprunt, em.date_retour_prevue
    FROM emprunts em
    JOIN exemplaires ex ON ex.id = em.exemplaire_id
    JOIN notices n ON n.id = ex.notice_id
    JOIN membres m ON m.id = em.membre_id
    WHERE em.date_retour_effective IS NULL
"""


def afficher_emprunts(emprunts):
    if not emprunts:
        print("Aucun emprunt.")
        return
    print(f"\n{'ID':<4} {'Titre':<38} {'Membre':<24} {'Emprunté le':<12} {'À rendre le'}")
    print("-" * 95)
    for e in emprunts:
        membre = e["prenom"] + " " + e["nom"]
        print(f"{e['id']:<4} {e['titre'][:36]:<38} {membre[:22]:<24} "
              f"{str(e['date_emprunt']):<12} {e['date_retour_prevue']}")


def emprunter():
    id_membre = input("ID du membre : ")
    if not lire("SELECT id FROM membres WHERE id = %s", (id_membre,)):
        print("Membre introuvable.")
        return
    id_exemplaire = input("ID de l'exemplaire (voir 'Voir une notice') : ")
    exemplaires = lire("SELECT * FROM exemplaires WHERE id = %s", (id_exemplaire,))
    if not exemplaires:
        print("Exemplaire introuvable.")
        return
    if not exemplaires[0]["disponible"]:
        print("Cet exemplaire est déjà emprunté.")
        return
    aujourdhui = date.today()
    retour = aujourdhui + timedelta(days=DUREE_EMPRUNT)
    ecrire("INSERT INTO emprunts (exemplaire_id, membre_id, date_emprunt, date_retour_prevue) "
           "VALUES (%s, %s, %s, %s)", (id_exemplaire, id_membre, aujourdhui, retour))
    ecrire("UPDATE exemplaires SET disponible = 0 WHERE id = %s", (id_exemplaire,))
    print(f"Emprunt enregistré. À rendre avant le {retour}.")


def retourner():
    id_emprunt = input("ID de l'emprunt à clôturer : ")
    emprunts = lire("SELECT * FROM emprunts WHERE id = %s AND date_retour_effective IS NULL",
                    (id_emprunt,))
    if not emprunts:
        print("Emprunt introuvable ou déjà rendu.")
        return
    emprunt = emprunts[0]
    ecrire("UPDATE emprunts SET date_retour_effective = %s WHERE id = %s", (date.today(), id_emprunt))
    ecrire("UPDATE exemplaires SET disponible = 1 WHERE id = %s", (emprunt["exemplaire_id"],))
    print("Livre rendu. Merci !")
    if emprunt["date_retour_prevue"] < date.today():
        jours = (date.today() - emprunt["date_retour_prevue"]).days
        print(f"Attention : {jours} jour(s) de retard.")


def emprunts_en_cours():
    afficher_emprunts(lire(BASE_EMPRUNTS + " ORDER BY em.date_retour_prevue"))


def emprunts_en_retard():
    afficher_emprunts(lire(BASE_EMPRUNTS + " AND em.date_retour_prevue < CURDATE()"))

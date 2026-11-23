from datetime import date
from db import lire, ecrire


def lister_membres():
    membres = lire("SELECT * FROM membres ORDER BY nom")
    if not membres:
        print("Aucun membre.")
        return
    print(f"\n{'ID':<4} {'Nom':<15} {'Prénom':<15} {'Email':<30} {'Téléphone'}")
    print("-" * 80)
    for m in membres:
        print(f"{m['id']:<4} {m['nom']:<15} {m['prenom']:<15} {str(m['email']):<30} {m['telephone']}")


def ajouter_membre():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    email = input("Email : ")
    telephone = input("Téléphone : ")
    ecrire("INSERT INTO membres (nom, prenom, email, telephone, date_inscription) VALUES (%s, %s, %s, %s, %s)",
           (nom, prenom, email, telephone, date.today()))
    print("Membre inscrit.")


def supprimer_membre():
    id_membre = input("ID du membre à supprimer : ")
    # On refuse si le membre a encore des emprunts en cours
    en_cours = lire("SELECT id FROM emprunts WHERE membre_id = %s AND date_retour_effective IS NULL",
                    (id_membre,))
    if en_cours:
        print("Impossible : ce membre a encore des livres à rendre.")
        return
    ecrire("DELETE FROM emprunts WHERE membre_id = %s", (id_membre,))
    ecrire("DELETE FROM membres WHERE id = %s", (id_membre,))
    print("Membre supprimé (s'il existait).")

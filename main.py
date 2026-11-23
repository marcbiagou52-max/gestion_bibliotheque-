import livres
import membres
import emprunts
from db import lire


def statistiques():
    nb_notices = lire("SELECT COUNT(*) AS n FROM notices")[0]["n"]
    nb_exemplaires = lire("SELECT COUNT(*) AS n FROM exemplaires")[0]["n"]
    nb_membres = lire("SELECT COUNT(*) AS n FROM membres")[0]["n"]
    nb_emprunts = lire("SELECT COUNT(*) AS n FROM emprunts WHERE date_retour_effective IS NULL")[0]["n"]
    print("\n=== Statistiques ===")
    print(f"Livres (notices)     : {nb_notices}")
    print(f"Exemplaires          : {nb_exemplaires}")
    print(f"Membres              : {nb_membres}")
    print(f"Emprunts en cours    : {nb_emprunts}")


def lancer_menu(titre, options):
    """Affiche un menu. options = liste de (texte, fonction)."""
    while True:
        print(f"\n--- {titre} ---")
        for i, (texte, _) in enumerate(options, 1):
            print(f"{i}. {texte}")
        print("0. Retour")
        choix = input("Votre choix : ")
        if choix == "0":
            return
        if choix.isdigit() and 1 <= int(choix) <= len(options):
            options[int(choix) - 1][1]()
        else:
            print("Choix invalide.")


def menu_livres():
    lancer_menu("GESTION DES LIVRES", [
        ("Lister tous les livres", livres.lister_livres),
        ("Rechercher un livre", livres.rechercher_livre),
        ("Voir une notice et ses exemplaires", livres.voir_notice),
        ("Ajouter un livre", livres.ajouter_livre),
        ("Ajouter un exemplaire", livres.ajouter_exemplaire),
        ("Supprimer un livre", livres.supprimer_livre),
    ])


def menu_membres():
    lancer_menu("GESTION DES MEMBRES", [
        ("Lister les membres", membres.lister_membres),
        ("Inscrire un membre", membres.ajouter_membre),
        ("Supprimer un membre", membres.supprimer_membre),
    ])


def menu_emprunts():
    lancer_menu("GESTION DES EMPRUNTS", [
        ("Emprunter un livre", emprunts.emprunter),
        ("Retourner un livre", emprunts.retourner),
        ("Emprunts en cours", emprunts.emprunts_en_cours),
        ("Emprunts en retard", emprunts.emprunts_en_retard),
    ])


def main():
    while True:
        print("\n==============================")
        print("   BIBLIOTHÈQUE IIT - MENU")
        print("==============================")
        print("1. Gestion des livres")
        print("2. Gestion des membres")
        print("3. Gestion des emprunts")
        print("4. Statistiques")
        print("0. Quitter")
        choix = input("Votre choix : ")
        try:
            if choix == "1":
                menu_livres()
            elif choix == "2":
                menu_membres()
            elif choix == "3":
                menu_emprunts()
            elif choix == "4":
                statistiques()
            elif choix == "0":
                print("Au revoir !")
                break
            else:
                print("Choix invalide.")
        except Exception as erreur:
            print("Erreur :", erreur)


if __name__ == "__main__":
    main()

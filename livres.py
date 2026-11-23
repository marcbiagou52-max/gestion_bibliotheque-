from db import lire, ecrire

LOCALISATIONS = ["Bibliothèque de recherche", "Bibliothèque enfantine", "Banque de prêt"]


def afficher_livres(livres):
    if not livres:
        print("Aucun livre trouvé.")
        return
    print(f"\n{'ID':<4} {'Titre':<42} {'Auteur':<26} {'Dewey':<6} {'Année':<6} {'Dispo'}")
    print("-" * 95)
    for l in livres:
        print(f"{l['id']:<4} {l['titre'][:40]:<42} {l['auteur'][:24]:<26} "
              f"{l['dewey']:<6} {str(l['annee']):<6} {l['disponibles']}/{l['total']}")


REQUETE_LIVRES = """
    SELECT n.id, n.titre, n.auteur, n.dewey, n.annee,
           COUNT(e.id) AS total,
           COALESCE(SUM(e.disponible), 0) AS disponibles
    FROM notices n
    LEFT JOIN exemplaires e ON e.notice_id = n.id
"""


def lister_livres():
    afficher_livres(lire(REQUETE_LIVRES + " GROUP BY n.id ORDER BY n.titre"))


def rechercher_livre():
    mot = input("Mot à chercher (titre ou auteur) : ")
    motif = "%" + mot + "%"
    livres = lire(REQUETE_LIVRES + " WHERE n.titre LIKE %s OR n.auteur LIKE %s GROUP BY n.id",
                  (motif, motif))
    afficher_livres(livres)


def voir_notice():
    id_notice = input("ID du livre : ")
    notices = lire("SELECT * FROM notices WHERE id = %s", (id_notice,))
    if not notices:
        print("Livre introuvable.")
        return
    n = notices[0]
    print(f"\nTitre   : {n['titre']}")
    print(f"Auteur  : {n['auteur']}")
    print(f"ISBN    : {n['isbn']}")
    print(f"Dewey   : {n['dewey']}")
    print(f"Année   : {n['annee']}")
    print(f"Support : {n['type_support']}")
    print(f"Résumé  : {n['resume']}")
    print("\nExemplaires :")
    for e in lire("SELECT * FROM exemplaires WHERE notice_id = %s", (id_notice,)):
        etat = "Disponible" if e["disponible"] else "Emprunté"
        print(f"  Exemplaire n°{e['id']} - {e['localisation']} - {etat}")


def ajouter_livre():
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    isbn = input("ISBN : ")
    dewey = input("Code Dewey (ex: 843 pour roman français) : ")
    annee = input("Année : ")
    resume = input("Résumé : ")
    id_notice = ecrire(
        "INSERT INTO notices (titre, auteur, isbn, dewey, annee, resume) VALUES (%s, %s, %s, %s, %s, %s)",
        (titre, auteur, isbn, dewey, annee, resume))
    ecrire("INSERT INTO exemplaires (notice_id) VALUES (%s)", (id_notice,))
    print("Livre ajouté avec un exemplaire (Banque de prêt).")


def ajouter_exemplaire():
    id_notice = input("ID du livre : ")
    print("Localisation :")
    for i, loc in enumerate(LOCALISATIONS, 1):
        print(f"  {i}. {loc}")
    choix = input("Choix : ")
    if choix not in ("1", "2", "3"):
        print("Choix invalide.")
        return
    ecrire("INSERT INTO exemplaires (notice_id, localisation) VALUES (%s, %s)",
           (id_notice, LOCALISATIONS[int(choix) - 1]))
    print("Exemplaire ajouté.")


def supprimer_livre():
    id_notice = input("ID du livre à supprimer : ")
    ecrire("DELETE FROM notices WHERE id = %s", (id_notice,))
    print("Livre supprimé (s'il existait).")

# Gestion de Bibliothèque (Python + MySQL)

Projet de gestion d'une bibliothèque en console, inspiré de la structure du catalogue
de la Bibliothèque Nationale de Côte d'Ivoire (PMB / Bib'Doc) :

- **Notice / Exemplaire** : une notice décrit le livre, chaque exemplaire est une copie physique
- **Classification Dewey** (ex. 843 = roman français, 005 = informatique)
- **Type de support** : texte imprimé, manuscrit, document électronique
- **Localisations** : Bibliothèque de recherche, Bibliothèque enfantine, Banque de prêt

## Fonctionnalités

- Livres : lister, rechercher, voir une notice, ajouter, ajouter un exemplaire, supprimer
- Membres : lister, inscrire, supprimer
- Emprunts : emprunter, retourner, emprunts en cours, emprunts en retard
- Statistiques

La base contient déjà 22 notices (romans africains et classiques), 27 exemplaires et 4 membres.

## Installation

1. Installer Python 3 et MySQL (XAMPP, WAMP ou MySQL Server) et démarrer MySQL.
2. Dans le terminal de VS Code :

```
pip install -r requirements.txt
```

3. Ouvrir `config.py` et mettre ton mot de passe MySQL (vide par défaut avec XAMPP).
4. Créer la base et les données :

```
python init_db.py
```

5. Lancer le programme :

```
python main.py
```

## Structure du projet

| Fichier | Rôle |
|---|---|
| `database.sql` | Tables + romans + membres de départ |
| `init_db.py` | Exécute `database.sql` |
| `config.py` | Paramètres de connexion MySQL |
| `db.py` | Fonctions de connexion et requêtes |
| `livres.py` | Notices et exemplaires |
| `membres.py` | Membres |
| `emprunts.py` | Emprunts et retours |
| `main.py` | Menus du programme |

## Schéma de la base

- `notices` (1) ── (N) `exemplaires`
- `membres` (1) ── (N) `emprunts` (N) ── (1) `exemplaires`

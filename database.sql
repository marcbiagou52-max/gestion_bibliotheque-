-- ============================================
-- Base de données : bibliotheque (modèle BNCI)
-- Notice = fiche du livre / Exemplaire = copie physique
-- ============================================

CREATE DATABASE IF NOT EXISTS bibliotheque CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE bibliotheque;

DROP TABLE IF EXISTS emprunts;
DROP TABLE IF EXISTS exemplaires;
DROP TABLE IF EXISTS membres;
DROP TABLE IF EXISTS notices;

CREATE TABLE notices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    auteur VARCHAR(120) NOT NULL,
    isbn VARCHAR(20),
    dewey VARCHAR(10) NOT NULL,
    annee INT,
    type_support ENUM('Texte imprimé', 'Manuscrit', 'Document électronique') NOT NULL DEFAULT 'Texte imprimé',
    resume TEXT
);

CREATE TABLE exemplaires (
    id INT AUTO_INCREMENT PRIMARY KEY,
    notice_id INT NOT NULL,
    localisation ENUM('Bibliothèque de recherche', 'Bibliothèque enfantine', 'Banque de prêt') NOT NULL DEFAULT 'Banque de prêt',
    disponible TINYINT(1) NOT NULL DEFAULT 1,
    FOREIGN KEY (notice_id) REFERENCES notices(id) ON DELETE CASCADE
);

CREATE TABLE membres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(80) NOT NULL,
    prenom VARCHAR(80) NOT NULL,
    email VARCHAR(120),
    telephone VARCHAR(20),
    date_inscription DATE NOT NULL
);

CREATE TABLE emprunts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    exemplaire_id INT NOT NULL,
    membre_id INT NOT NULL,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    FOREIGN KEY (exemplaire_id) REFERENCES exemplaires(id),
    FOREIGN KEY (membre_id) REFERENCES membres(id)
);

-- ============================================
-- Données : romans (les ISBN sont fictifs)
-- ============================================

INSERT INTO notices (titre, auteur, isbn, dewey, annee, type_support, resume) VALUES
('Les Soleils des indépendances', 'Ahmadou Kourouma', '978-0-000-00001-1', '843', 1968, 'Texte imprimé', 'Fama, prince malinké déchu, vit la désillusion des indépendances africaines.'),
('Allah n''est pas obligé', 'Ahmadou Kourouma', '978-0-000-00002-2', '843', 2000, 'Texte imprimé', 'Le récit de Birahima, enfant soldat en Afrique de l''Ouest.'),
('En attendant le vote des bêtes sauvages', 'Ahmadou Kourouma', '978-0-000-00003-3', '843', 1998, 'Texte imprimé', 'Satire du pouvoir d''un dictateur africain racontée par un griot.'),
('Monnè, outrages et défis', 'Ahmadou Kourouma', '978-0-000-00004-4', '843', 1990, 'Texte imprimé', 'Un siècle d''histoire africaine, de la colonisation aux indépendances.'),
('Climbié', 'Bernard Dadié', '978-0-000-00005-5', '843', 1956, 'Texte imprimé', 'L''enfance et la jeunesse d''un jeune Ivoirien sous la colonisation.'),
('Un nègre à Paris', 'Bernard Dadié', '978-0-000-00006-6', '843', 1959, 'Texte imprimé', 'Le regard d''un Africain sur Paris et la société française.'),
('Kocoumbo, l''étudiant noir', 'Aké Loba', '978-0-000-00007-7', '843', 1960, 'Texte imprimé', 'Le parcours d''un jeune Ivoirien parti étudier en France.'),
('L''Enfant noir', 'Camara Laye', '978-0-000-00008-8', '843', 1953, 'Texte imprimé', 'Souvenirs d''enfance d''un jeune Guinéen.'),
('Une si longue lettre', 'Mariama Bâ', '978-0-000-00009-9', '843', 1979, 'Texte imprimé', 'Une femme sénégalaise écrit à son amie après la mort de son mari.'),
('L''Aventure ambiguë', 'Cheikh Hamidou Kane', '978-0-000-00010-0', '843', 1961, 'Texte imprimé', 'Le déchirement d''un jeune homme entre tradition africaine et savoir occidental.'),
('Une vie de boy', 'Ferdinand Oyono', '978-0-000-00011-1', '843', 1956, 'Texte imprimé', 'Le journal d''un jeune domestique camerounais sous la colonisation.'),
('Les Bouts de bois de Dieu', 'Ousmane Sembène', '978-0-000-00012-2', '843', 1960, 'Texte imprimé', 'La grande grève des cheminots du Dakar-Niger.'),
('Le monde s''effondre', 'Chinua Achebe', '978-0-000-00013-3', '823', 1958, 'Texte imprimé', 'Chute d''Okonkwo, chef igbo, face à l''arrivée des Européens.'),
('Le Petit Prince', 'Antoine de Saint-Exupéry', '978-0-000-00014-4', '843', 1943, 'Texte imprimé', 'Un aviateur rencontre un petit prince venu d''une autre planète.'),
('L''Étranger', 'Albert Camus', '978-0-000-00015-5', '843', 1942, 'Texte imprimé', 'Meursault, un homme indifférent, est jugé pour meurtre.'),
('Les Misérables', 'Victor Hugo', '978-0-000-00016-6', '843', 1862, 'Texte imprimé', 'Jean Valjean, ancien forçat, cherche la rédemption.'),
('Germinal', 'Émile Zola', '978-0-000-00017-7', '843', 1885, 'Texte imprimé', 'La vie et la révolte des mineurs du nord de la France.'),
('Le Comte de Monte-Cristo', 'Alexandre Dumas', '978-0-000-00018-8', '843', 1844, 'Texte imprimé', 'Edmond Dantès, injustement emprisonné, prépare sa vengeance.'),
('Vingt mille lieues sous les mers', 'Jules Verne', '978-0-000-00019-9', '843', 1870, 'Texte imprimé', 'Le voyage du capitaine Nemo à bord du Nautilus.'),
('1984', 'George Orwell', '978-0-000-00020-0', '823', 1949, 'Texte imprimé', 'Dans un monde totalitaire, Winston tente d''échapper à Big Brother.'),
('Candide', 'Voltaire', '978-0-000-00021-1', '843', 1759, 'Texte imprimé', 'Les aventures d''un jeune homme naïf qui découvre le monde.'),
('Initiation à la programmation Python', 'Collectif', '978-0-000-00022-2', '005', 2020, 'Document électronique', 'Cours d''initiation à Python pour les débutants.');

-- Premier exemplaire de chaque notice (ids 1 à 22)
INSERT INTO exemplaires (notice_id, localisation) VALUES
(1, 'Banque de prêt'), (2, 'Banque de prêt'), (3, 'Banque de prêt'), (4, 'Banque de prêt'),
(5, 'Banque de prêt'), (6, 'Banque de prêt'), (7, 'Banque de prêt'), (8, 'Banque de prêt'),
(9, 'Banque de prêt'), (10, 'Banque de prêt'), (11, 'Banque de prêt'), (12, 'Banque de prêt'),
(13, 'Banque de prêt'), (14, 'Bibliothèque enfantine'), (15, 'Banque de prêt'), (16, 'Banque de prêt'),
(17, 'Banque de prêt'), (18, 'Banque de prêt'), (19, 'Bibliothèque enfantine'), (20, 'Banque de prêt'),
(21, 'Banque de prêt'), (22, 'Bibliothèque de recherche');

-- Deuxièmes exemplaires pour quelques livres (ids 23 à 27)
INSERT INTO exemplaires (notice_id, localisation) VALUES
(1, 'Bibliothèque de recherche'), (2, 'Bibliothèque de recherche'), (5, 'Bibliothèque de recherche'),
(14, 'Bibliothèque enfantine'), (16, 'Bibliothèque de recherche');

INSERT INTO membres (nom, prenom, email, telephone, date_inscription) VALUES
('Kouassi', 'Aya', 'aya.kouassi@example.com', '0701020304', CURDATE()),
('Traoré', 'Ibrahim', 'ibrahim.traore@example.com', '0505060708', CURDATE()),
('Koné', 'Fatou', 'fatou.kone@example.com', '0102030405', CURDATE()),
('N''Guessan', 'Yao', 'yao.nguessan@example.com', '0709080706', CURDATE());

-- Un emprunt en retard pour tester le menu "retards"
INSERT INTO emprunts (exemplaire_id, membre_id, date_emprunt, date_retour_prevue)
VALUES (1, 1, DATE_SUB(CURDATE(), INTERVAL 20 DAY), DATE_SUB(CURDATE(), INTERVAL 6 DAY));

UPDATE exemplaires SET disponible = 0 WHERE id = 1;

-- Jeux de données NOK (ne doit pas marcher àprès avoir éxécuté le jeux de données OK)
-- Quelques cas d'erreurs de non respect des contraintes d'intégrité

-- Erreur : Modèle existant
INSERT INTO Modeles VALUES ('Galaxy S24', 'Samsung');


-- Erreur : Type etat autre que "excellent", "bon" ou "moyen"
INSERT INTO Telephones VALUES (1, 512, 'tres bon', 'iPhone 15', 200);
-- Erreur : Telephone avec modele inconnu
INSERT INTO Telephones VALUES (3, 128, 'bon', 'Pixel 8', 300);
-- Erreur : Telephone sans modèle
INSERT INTO Telephones VALUES (3, 128, 'bon', NULL, 300);
-- Erreur : Telephone avec commande inconnu
INSERT INTO Telephones VALUES (1, 512, 'excellent', 'iPhone 15', 0);


-- Erreur : Client sans nom
INSERT INTO Clients VALUES (1, NULL, 'Archibald', '1999-12-31', 'Brest');
-- Erreur : Client sans prenom
INSERT INTO Clients VALUES (1, 'Haddock', NULL, '1999-12-31', 'Brest');
-- Erreur : Client sans ville
INSERT INTO Clients VALUES (1, 'Haddock', 'Archibald', '1999-12-31', NULL);

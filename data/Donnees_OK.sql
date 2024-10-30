-- Jeux de données OK (ça doit marcher)

-- Insertions des premiers modèles de telephones
INSERT INTO Modeles VALUES ('Galaxy S24', 'Samsung');
INSERT INTO Modeles VALUES ('iPhone 15', 'Apple');
INSERT INTO Modeles VALUES ('3310', 'Nokia');
   
-- Insertion des premieres pieces de rechange
INSERT INTO Pieces VALUES (1000, 'batterie');
INSERT INTO Pieces VALUES (1001, 'carte mere');
INSERT INTO Pieces VALUES (1002, 'ecran');
INSERT INTO Pieces VALUES (1003, 'appareil photo');

-- Insertion des premiers clients
INSERT INTO Clients VALUES (1, 'Haddock', 'Archibald', '1999-12-31', 'Brest');
INSERT INTO Clients VALUES (2, 'Tournesol', 'Tryphon', '2000-01-01', 'Paris');
INSERT INTO Clients VALUES (3, 'Rastapopoulos', 'Roberto', '1950-06-15', 'Bruxelles');

-- Insertion des premieres commandes passees
INSERT INTO Commandes VALUES (100, '2024-03-25', 1);
INSERT INTO Commandes VALUES (101, '2024-02-12', 2);
INSERT INTO Commandes VALUES (102, '1975-02-10', 3);

-- Insertion des premiers telephones
INSERT INTO Telephones VALUES (10, 512, 'excellent', 'iPhone 15', 101);
INSERT INTO Telephones VALUES (11, 256, 'bon', 'Galaxy S24', 100);
INSERT INTO Telephones VALUES (12, 64, 'excellent', '3310', 102);

-- Insertion des premieres reparations
INSERT INTO Reparations VALUES (10, 1001);
INSERT INTO Reparations VALUES (10, 1000);
INSERT INTO Reparations VALUES (10, 1003);
INSERT INTO Reparations VALUES (12, 1000);

DROP TABLE IF EXISTS Reparations;
DROP TABLE IF EXISTS Pieces;
DROP TABLE IF EXISTS Telephones;
DROP TABLE IF EXISTS Commandes;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Modeles;

-- Pour activer les FKs
PRAGMA FOREIGN_KEYS=ON;

-- Types SQLite
CREATE TABLE Modeles (
   nom_modele TEXT PRIMARY KEY,
   marque_modele TEXT
);

-- Creation de la table Clients
CREATE TABLE Clients (
   numero_client INTEGER PRIMARY KEY,
   nom_client TEXT,
   prenom_client TEXT,
   date_naiss_client DATE,
   adresse_client TEXT,
   CONSTRAINT ck_numero_client CHECK (numero_client >= 0)
);

-- Creation de la table Commandes
CREATE TABLE Commandes (
   numero_commande INTEGER PRIMARY KEY, 
   date_commande DATE,
   numero_client INTEGER,
   CONSTRAINT fk_numero_client_commandes FOREIGN KEY (numero_client) REFERENCES Clients(numero_client),
   CONSTRAINT ck_numero_commande CHECK (numero_commande >= 0),
   CONSTRAINT ck_numero_client CHECK (numero_client >= 0)
);

-- Creation de la table Telephones
CREATE TABLE Telephones (
   numero_telephone INTEGER PRIMARY KEY,
   stockage_telephone INTEGER,
   etat_telephone TEXT,
   nom_modele TEXT,
   numero_commande INTEGER,
   CONSTRAINT fk_nom_modele_tel FOREIGN KEY (nom_modele) REFERENCES Modeles(nom_modele),
   CONSTRAINT fk_numero_commande_tel FOREIGN KEY (numero_commande) REFERENCES Commandes(numero_commande),
   CONSTRAINT ck_numero_telephone CHECK (numero_telephone >= 0),
   CONSTRAINT ck_stockage_telephone CHECK (stockage_telephone >= 0),
   CONSTRAINT ck_numero_commande CHECK (numero_commande >= 0),
   CONSTRAINT ck_etat_telephone CHECK (
   (etat_telephone = 'excellent') OR (etat_telephone = 'bon') OR (etat_telephone = 'moyen')
   )
   
);

-- Creation de la table Pieces
CREATE TABLE Pieces (
   numero_piece INTEGER PRIMARY KEY,
   piece_type_piece TEXT,
   CONSTRAINT ck_numero_piece CHECK (numero_piece >= 0),
   CONSTRAINT ck_piece_type_piece CHECK (
   (piece_type_piece = 'batterie') OR (piece_type_piece = 'carte mere') OR (piece_type_piece = 'ecran') OR
   (piece_type_piece = 'appareil photo')
   )
);

-- Creation de la table Reparations
CREATE TABLE Reparations (
   numero_telephone INTEGER,
   numero_piece INTEGER,
   CONSTRAINT fk_reparations_numero_telephone_c0 FOREIGN KEY (numero_telephone) REFERENCES Telephones(numero_telephone),
   CONSTRAINT fk_reparations_numero_piece_c1 FOREIGN KEY(numero_piece) REFERENCES Pieces(numero_piece),
   CONSTRAINT pk_reparations_numero_telephone_numero_piece PRIMARY KEY (numero_telephone, numero_piece),
   CONSTRAINT ck_numero_piece CHECK (numero_piece >= 0),
   CONSTRAINT ck_numero_telephone CHECK (numero_telephone >= 0)
);

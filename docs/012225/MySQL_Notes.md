MySQL

Navigieren Sie zu Site Tools > Website > MySQL , wo Sie einfach einen MySQL-Benutzer und eine Datenbank erstellen und dann den Benutzer der Datenbank zuweisen können

Im Schriebebereich den Command immer mit ";" beenden
Im MySQL Workbench, auf der "Startsite" in der Query 1, schreibe "create database XX;". Nun ist Database XX erstellt. Um diese zu vewenden, muss "use database XX;" geschriebn werden

create table Spamliste (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Vorname varchar(20) NOT NULL,
    Nachname varchar(20) NOT NULL,
    Email_Adresse varchar(50) UNIQUE NOT NULL
);

Diese Zeilen fügen die Informationen für die jeweiligen Felder hinzu.
INSERT INTO Benutzer (name, email) VALUES
('Max Mustermann', 'max.mustermann@example.com');

SELECT * FROM Benutzer;             Gibt nun die hinterlegte Tabelle mit informationen in der Shell aus.

Vor letzter Indent Zeile darf kein Komma sein

Keine Anhang, wie ich miene Tabelle sehen kann
 
MySQL Notizen
Navigieren Sie zu Site Tools > Website > MySQL , wo Sie einfach einen MySQL-Benutzer und eine Datenbank erstellen und dann den Benutzer der Datenbank zuweisen können
Im Schriebebereich den Command immer mit ";" beenden
Im MySQL Workbench, auf der "Startsite" in der Query 1, schreibe "create database XX;". Nun ist Database XX erstellt. Um diese zu vewenden, muss "use database XX;" geschriebn werden

Datenbank erstellen: CREATE DATABASE "name";
Datenbank wechseln: USE "name";
Tabele erstellen: CREATE TABLE "name" (
    tab inhalt,
    tab inhalt2 !OHNE KOMMA
); !ENDE OHNE TAB MIT KLAMMER UND ";" !

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


Table darstellen: SELECT * FROM "tablename"

Aufgabe 1: Zeige eine Liste der vorhanden Datenbanken: "SHOW DATABASES"
            Es sind 6 Datenbanken Vorhanden, 2 von mir

Aufgabe 2: Zweite Datenbank erstellen, auswählen, "SHOW TABLES"

Aufgabe 3: Zeige eine Liste der vorhanden Tabelen: USE "information_schema"; SHOW TABLES;
            In der Datenbank information_schema sind 79 tables vorhanden
 
Aufgabe 4: Zeige die Struktur einer bestehenden Tabelle: SHOW FIELDS FROM "name"
            Tabelle "veiws" verfügt vor allem über varchar(64)

Aufgabe 5: Richtige Datenbank (eigene) wählen, dann: SELECT * FROM "tablename" WHERE email LIKE 'suchbegriff';
            In meinem Beispiel "SELECT * FROM Spamliste WHERE email_adresse LIKE '%example.com';"
   Hello

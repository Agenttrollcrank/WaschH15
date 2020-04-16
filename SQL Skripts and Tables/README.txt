H15.SQL:

Besitzt 3 Tabellen
- Tabelle1: Benutzer
   Inhalt: Id, Vorname, Nachname, Username, Etage, Passwort
     Diese Tabelle wird vom Admin ausgefüllt
-Tabelle2: Strom
   Inhalt: Waschmachine, Kwh
     Kwh Spalte wird von Python aktualisiert, dient um den aktuellen Stromstand jeder Waschmaschine zu speichern und
     freizugeben
- Tabelle3: Abrechnung
    Inhalt: Username, Stromverbrauch
      Einträge werden von Nutzern erstellt, Stromverbrauch generiert Python
      !Hier noch zu klären: Werden verbrauchten Stromstände pro Nutzung schon hier durch Python zusammengefasst oder
       erstellt Python erstmal einen neuen Eintrag mit einem Stromverbrauch pro Nutzung?!

Abrechnung Skript:
      ordnet den genutzten Usernames aus [Tabelle3:Abrechnung] den dazugehörigen Vornamen, Nachnamen und die Etage
      aus [Tabelle1:benutzer] zu.
      Erhält Stromverbrauch aus [Tabelle3:Abrechnung] ?{-> Stromverbrauch/User oder Stromverbrauch/Nutzung?}?
      das Skript ordnet die Einträge nach Etage, damit Etagenweise einfacher abgerechnet werden kann
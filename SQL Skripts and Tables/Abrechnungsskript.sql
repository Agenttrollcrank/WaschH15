use h15;
## Dies ist das Abrechnungsskript 
## nehme Vorname und Nachname aus Benutzer wo Username mit Username aus Abrechnung übereinstimmt
insert into Bezahlen (Username,Vorname,Nachname,Etage,Stromverbrauch,Kosten_in_Euro)
select benutzer.username,benutzer.Vorname,benutzer.Nachname,benutzer.etage,abrechnung.Strom_bis - abrechnung.Strom_von,(Strom_bis - abrechnung.Strom_von)*0.32 from benutzer
 natural left join abrechnung where abrechnung.username=benutzer.username order by benutzer.Nachname;
 



 
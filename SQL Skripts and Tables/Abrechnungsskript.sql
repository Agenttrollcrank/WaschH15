use h15;
## Dies ist das Abrechnungsskript 
## nehme Vorname und Nachname aus Benutzer wo Username mit Username aus Abrechnung übereinstimmt
select benutzer.etage,benutzer.Vorname,benutzer.Nachname,abrechnung.stromverbrauch from benutzer
 natural left join Abrechnung where Abrechnung.username=benutzer.username order by benutzer.etage;
 
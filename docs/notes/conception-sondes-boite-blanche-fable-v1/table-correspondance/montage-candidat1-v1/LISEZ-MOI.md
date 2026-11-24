# Montage des candidats au scellement 1 (table de correspondance et note de conception des sondes)

Deux petits programmes, sans donnée ni résultat, qui ont monté les candidats le 23 novembre 2026 (heure passée en argument : 23:32, `date -u`).

- `monter_table_candidat1.py BROUILLON3 CANDIDAT HEURE` : recopie à l'octet les sections 1 à 8 du brouillon 3 de la table et réécrit le titre, l'en-tête, les sections 9 et 10 et la section « Contre-lecture ».
- `monter_note_candidat1.py BROUILLON5 CANDIDAT HEURE` : applique au brouillon 5 de la note des remplacements exacts, chacun trouvé une fois et une seule.

Rejoués avec la même heure sur les mêmes sources, ils rendent les mêmes octets.

"""T0.7, étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, scellé, `0ae6210f…`) : code neuf de la section « Code neuf ».

Paquet neuf (R12) ; aucun module gelé n'est modifié. Modules : `commun_v1` (constantes du texte, graines par clé, gardes
communes), `plis_v1` (règle (a) en deux plis, nul de réétiquetage, différences appariées, TE, MU, ART, DD, SC),
`adversaires_texte_v1` (MC par l'interface de la pièce ou par l'implémentation de repli, LEX), `apprentissage_carte_v1`
(familles linéaire et attention sur la carte, double précision, déterministe), `validation_imbriquee_v1` (plis internes,
grille, sonde finale, nul de réétiquetage, ENC, garde de débit), `etat_impose_v1` (relecture à état imposé, partagée avec la
pièce R du texte de validité), `registre_bbis_v1` (registre propre, antériorités, garde de dépense), `lecture_v1` (gardes,
états, issue, phrases, réserves, audit R4 ; processeur seulement), `conjointe_v1` (table conjointe B × B bis).
"""

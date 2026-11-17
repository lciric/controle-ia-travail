"""T0.7, étape B bis (`prereg/T0.7-etape-B-bis-v1.md`, scellé, `0ae6210f…`) : code neuf de la section « Code neuf ».

Paquet neuf (R12) ; aucun module gelé n'est modifié. Modules :
- `commun_v1` : constantes du texte, cellules, séries, grille, graines par clé, refus de la moyenne sur les jetons ;
- `etat_impose_v1` : relecture forcée à état d'adaptateur et à environnement imposés, **partagée avec la pièce R** du texte de
  validité de l'adaptateur (module neuf : aucun module de relecture à état imposé n'existait sous `src/controle_ia/`) ;
- `apprentissage_carte_v1` : familles linéaire et attention sur la carte, double précision, déterministe ; contrôle
  carte-processeur ;
- `validation_imbriquee_v1` : plis internes, grille, sonde finale, plancher, nul de réétiquetage, ENC, garde de débit,
  notation (scores seulement) ;
- `plis_v1` : règle (a) en deux plis, nul de réétiquetage, différences appariées, TE, MU, ART, DD, SC (statistiques sur des
  scores d'action déjà agrégés) ;
- `adversaires_texte_v1` : MC (interface de la pièce « mots et coût » ou implémentation de repli) et LEX ;
- `registre_bbis_v1` : registre propre, fiche de `CODE-BBIS`, gardes d'offre, de création et de dépense ;
- `marche_v1` : la marche sur l'instance (relecture, apprentissage, notation, fichiers fermés) ;
- `lecture_v1` : gardes, états, issue, phrases, réserves, audit R4 (processeur seulement) ;
- `conjointe_v1` : table conjointe B × B bis.
"""

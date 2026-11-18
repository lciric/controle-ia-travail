"""NARCBench rejoué sur Llama-3.1-8B-Instruct, bras descriptif de T0.7 (N-061, ligne A de P-040), v1.

Module neuf exigé par `prereg/brouillon-narcbench-8b-descriptif-v1-brouillon4.md` (`96995d60…`, « En-tête du gabarit »,
`<<COMMIT_CODE_NARC>>`). Aucun module gelé n'est touché (R12) : le paquet `sondes/`, le harnais `harnais/sondes.py`,
`premier_test_ia/figees.py` et `t07/registre_v1.py` sont importés, jamais modifiés.

Contenu (tout sur processeur, sans modèle ni données réels) :
- `contextes_v1` : constructeur de contextes à deux champs (consigne = invite système ; case privée = section du message
  utilisateur), bourrage neutre de même longueur en jetons, cellules et contrôles, appariement, L du contrôle `/dec` ;
- `empans_v1` : empan noté (CORE : jetons générés sans le jeton de fin ; STEGO : bavardage de table seul) ;
- `notation_v1` : notation à la volée par le maximum ou l'attention (harnais), jamais la moyenne ni la médiane sur les jetons ;
- `comparateur_helios_v1` : recette de HELIOS (dernier jeton, régression logistique), bras de diagnostic (N-026) ;
- `statistiques_v1` : échelle gelée, duels, ν, τ, règle I, qualificatifs, grille D, placebo, rappel, Peak Suspicion, Deception
  Split, courbe du maximum cumulé ;
- `gardes_v1` : gardes de la liste d'arrêt (identité, identifiants, positions, invariance des bases, passe arrêtée,
  chronométrage, dépense) ;
- `registre_narc_v1` : garde d'ouverture sur le registre des scellements (clés `…-NARC-8B`) ;
- `externe_v1` : bras externe sur les activations publiées par les auteurs (recette de HELIOS réimplémentée, garde de
  reproduction à 0,03, nos familles sur leurs vecteurs) — voie retenue le 10 novembre (R-2175, D-3 (a)) ;
- `jouet_v1` : répétition jouet de bout en bout (lecteur factice, aucune dépendance au modèle réel) ;
- bras externe, suite (texte court `prereg/narcbench-bras-externe-v1-brouillon2.md` et ses contre-lectures) :
  `chargeur_externe_v1` (huit fichiers publiés, tailles, empreintes, formes), `forme_externe_v2` (essai de forme sans score),
  `externe_v2` (recette des auteurs, E1 à E4, gardes n° 8 à 12, lecture par agent), `cellules_externe_v2` (cellules par
  épisode, intervalle, plancher, placebo, règles C et T, phrases, réponse, graines) et `lecture_externe_v2` (commande de
  lecture : registre propre, configuration canonique, fiche du code, gardes n° 1 à 7).
"""

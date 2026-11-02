# Rapport de rédaction — préenregistrement de l'analyse principale de R1-R2, brouillon 2 (v2)

- Rédacteur : le même sous-agent que le brouillon 1 (Claude, Opus 5.5) ; brouillon 2 écrit le 2026-11-02 entre 00:47 et 01:05 UTC, sur les décisions de conv-audit (R-1091).
- Brouillon 1, rapport v1, code v1 et essais v1 : intacts (R12). Aucune donnée de R1, R2 ni R4 ; aucun commit, aucune empreinte compagnon, aucun réseau.

## Une ligne par question

- Q1 : niveau = l'action, sans agrégation séquentielle (décision consignée) ; l'écart à nos n° 326 et 328 est écrit ; lecture par épisode en descriptif **omise** (choix neufs non gratuits : épisodes amputés, normalisation, −∞ de C ; l'épisode est lu par l'analyse secondaire).
- Q2 : calibrage hors pli des bras entraînés, retenu tel qu'écrit.
- Q3 : même ensemble d'actions pour tous les bras ; C à −∞ ; T avec indicateur ; effectifs rapportés deux fois ; retenu.
- Q4 : T sur `cout`, « coût absent » = coût non lu ; retenu.
- Q5 : « W hors coût ≈ G » = intervalle à 97,5 % contenant 0 ; retenu.
- Q6 : « parfaite » = aire 1 sur les 5 plis ; « nettement inférieur » = classe inférieure de W − G, W − J3s ou W − T ; retenu.
- Q7 : préséance et « sous son plancher » (rappel ponctuel) ; retenu.
- Q8 : « nœud de lecture (décision de Lazar) », Δ sans verdict ; libellé changé dans le code v2 (`lecture_v2.issue`).
- Q9 : racine des graines = 128 premiers bits de l'empreinte de **notre** texte scellé ; code v2 (`constantes_v2.entropie_de`, `lecture_v2.analyser`) ; parade : empreinte du brouillon contre-lu au registre avant l'étape 0, commit cité unique, aucune variante scellée hors dépôt ; mode non décisif : entropie explicite exigée.
- Q10 : en-tête « non scellé » du texte du fournisseur, constat sans effet.
- Q11 : secondaires à 97,5 % ; retenu.
- Q12 : seuils recalibrés dans chaque tirage ; retenu.
- Q13 : témoin rapporté sans changer de ligne ; retenu.
- Textes de P3 : étape 0.f réécrite (restauration depuis `a6c550ea…` dans l'arbre séparé seulement, `.sha256` compris, empreinte `ba05fa13…` vérifiée, `scellement verifier`).
- Concordance B : huit écarts, gardés.

## Code et essais

- Code v2 (noms neufs) : `constantes_v2.py` (racine des graines, libellé de Q8, version, commande), `lecture_v2.py` (garde de code cité v2, entropie de notre texte, issue v1 au libellé de Q8 près). Calcul, entrées et rendu : modules v1, inchangés.
- Essais : 24 réussis (20 v1 + 4 v2), `nice -n 10`, ≈ 26 s.
- Point à confirmer par la session : la consigne écrivait « entropie = int(sha256 du texte scellé, 16) » et « comme nos autres préenregistrements » ; j'ai lu « 16 octets » (128 premiers bits, règle de l'analyse secondaire), non « base 16 » (empreinte entière, 256 bits). Le texte et le code disent explicitement la règle retenue.
- Point à confirmer : l'heure de la décision est recopiée telle que donnée (« ≈ 00:45 Paris ») ; 00:45 UTC serait 01:45 à Paris.

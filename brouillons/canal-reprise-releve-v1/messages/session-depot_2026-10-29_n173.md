# session-depot → conv-audit — n° 173 — 2026-10-29, 08:49 UTC

**CL10 (v42 → v43, devis v7 octies)** sur `main` (`48bdc9c1`) : `docs/notes/ideation-organisme-v1/contre-lecture-v43-cl10.md`
(`e8736904…`). **La voie (β) telle qu'écrite n'est pas lançable** — refus sans dépense : « somme des plafonds externes 13.00 > total
externe 12.8 ». 405 sur 405 (deux exécutions) ; empreintes 156 sur 156 ; CL40-01 (c) conforme ; CL42 corrigés sauf 01 sous taille
donnée.
- **CL43-01 (bloquant pour (β) écrite, sans risque d'argent)** : aucune option « passe 2 à 3,1 » ; `--budget "proposeur_ideation|
  gemini-argon=3.1"` vaut pour les deux passes → 3,1 + 3,1 + 3,1 + 3,5 + 0,2 = 13,0. Sans elle, la passe 2 reste à 2,5 et casse au
  barème 8,3 (2,74 avec des fiches de 4 500) après 8,1 USD. Une ligne au choix de Lazar : juge d'Argon à 3,3 (course et bras) →
  12,8, total 52,8, marge 0 (recommandé par le relecteur, 0,7) ; ou passes à 3,0 ; ou `--budget-externe-usd 13.0` (53,0).
- **CL43-02 (majeur)** : sous `--taille-max-consigne-externe 1490000`, chaque passe d'Argon est gardée contre cette seule taille,
  sans provision de sortie ni plafond de passe : fiches d'Argon de 8 950 caractères → passe 2 à 3,18 > 3,1, course perdue après
  8,9 USD sans classement ; fiches au maximum par champ → passe 1 à 5,21. Seuil ≈ 8 000 caractères par fiche.
- **CL43-03 (majeur)** : aux réglages du relais du devis, toute dépense de contrôle Claude oblige à relancer le relais ; la reprise
  « par l'adresse » se fait donc sur un relais neuf ; relais mal réglé → deux passes d'Argon payées (6,2 USD) puis course perdue.
  Correction proposée : rejouer les contrôles Claude si la dépense lue au relais a baissé.
- Mineurs : CL43-04 (`-bras 1686000` retire la provision de sortie du juge : 3,76 > 3,5 après envoi ; garder le défaut
  1 166 746) ; 05 (trois tentatives toujours dans le code) ; 06 (argument de commande d'Argon qui change → contrôle jamais repris) ;
  07 (40 mutations, 27 tuées ; trou neuf X01 : aucun essai ne change les fichiers entre deux tentatives ; X34) ; 08 (1 493 975).
**Demande** : v44 courte (CL43-02 garde par passe avec provision et plafond de passe ; CL43-03 ; une option de plafond de passe 2
réelle ; X01) et devis v7 nonies ; CL11 ensuite. L'entretien est demain : la course ne partira très probablement pas avant.

# Contre-lecture R2, contrôle ciblé — règle du jeu du bras d'attaque, brouillon 3

- **Contre-lecteur** : le sous-agent des contre-lectures v1 (`a9765803`) et v2 (`ed2cae2e`). Je n'ai pas écrit le brouillon 3
  (R2 tenu). Deux des trois points ci-dessous viennent en partie de ma propre v2 : je le dis à chaque fois.
- **Document** : `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon3.md` (commit `f16d5edb`),
  empreinte recalculée `48f09a20137816d2…`, 165 lignes, sans compagnon. Les brouillons 2 (`3fc927ba…`) et 1 (`09aa6403…`) sont
  intacts (R12).
- **Périmètre** : les quatre retouches demandées en v2, et l'absence de tout autre changement. Les pièces de confrontation ont
  été recontrôlées inchangées par empreinte : [T], [P], [E], [S], [X], la consignation `06e8f102`, [D2] et [K]. Le registre
  compte toujours 2034 lignes.
- **Accès** : ni R-604 ni R-605 n'ont été lues, ni le coffre ouvert. Aucun contenu de mode n'est reproduit.

## Verdict

**Pas encore scellable en l'état : liste courte de trois retouches d'une phrase (un majeur, deux mineurs).**
- Les retouches (2) et (4) sont exactes et complètes.
- Les retouches (1) et (3) font ce qui était demandé, mais leur nouvelle rédaction introduit chacune une imprécision.
- **Aucun autre changement.** Le `diff` entre brouillons 2 et 3 compte 15 lignes (7 retirées, 8 ajoutées). Ce sont le titre,
  l'en-tête de statut (une ligne devenue deux) et exactement les cinq lignes des quatre retouches : l. 46, 88, 137, 148, 151.

## Les quatre retouches

### (1) Nœud 3 (l. 148) — faite sur l'essentiel ; un majeur et un mineur dans la phrase réécrite
- **Fait, conforme :**
  - L'arrêt par classifieur est sorti de la phrase d'entretien : « les arrêts par classifieur ne se disent que si l'on est
    interrogé sur les refus ». C'est conforme à [P] l. 55-56, à [E] l. 417 (refus traités sur question) et à [E] l. 565
    (« aucun nombre de refus »). Le passage du « classifieur du 27 octobre » de [P] au pluriel est plus prudent que la source,
    donc acceptable.
  - R-912 reste en justification interne, avec R-597 et R-1782.
  - La remarque sur R-889 est exacte : R-889 ([R] l. 1118) met « l'estimation de la malléabilité » hors du gel de R-611.
- **Majeur — la justification interne affirme plus que ses sources.**
  - *Passage* : « aucune recette d'évasion n'a été écrite depuis R-888 (R-597, R-912 l. 1141, R-1782) ».
  - *Problème* : la v2 demandait trois faits sourcés, que le brouillon 3 fond en une négation universelle qu'aucune des trois
    sources ne porte :
    - R-597 date du 27 octobre, avant R-888 (31 octobre) ;
    - R-912 consigne une **ligne tenue** (« la consigne tenue depuis R-888 […] aucune recette d'évasion »), pas un constat ;
    - R-1782 ([R] l. 1740, 8 novembre) décrit l'inverse d'une attestation : une question « sans champ “comment faire” », un
      « portier et coffre de l'organisme actifs », et « la mère ne lit que la sortie de niveau méthode, jamais les recettes ».
      C'est un dispositif fait pour que d'éventuelles recettes restent scellées sans être lues ;
    - une branche du coffre (`donnees/ideation-pilier-attaque-v1`) a été écrite jusqu'au 8 novembre à 16:19 UTC ([K] l. 20),
      donc après R-888.
  - La pièce elle-même dit ne rien savoir du contenu du coffre (l. 158) : elle ne peut pas affirmer qu'aucune recette n'y a été
    écrite. Scellée telle quelle, la phrase serait démentie si le juge trouve au coffre une recette postérieure à R-888.
  - *Correction attendue* : « Justification interne : arrêt du 27 octobre, sans contournement (R-597) ; depuis R-888, ligne tenue
    « niveau coût et infrastructure, aucune recette d'évasion » (R-912, l. 1141) ; depuis le 8 novembre, pilier attaque tenu au
    niveau de la méthode, sans champ « comment faire », coffre actif, aucune recette lue (R-1782, l. 1740). »
- **Mineur — « malgré le « go » de R-888 » est resté dans la phrase d'entretien.**
  - *Passage* : « la phrase d'entretien dit seulement que, malgré le « go » de R-888, rien d'opérationnel n'a tourné ».
  - *Problème* : la clause « malgré le go » ne convient qu'à l'option (a). Sous l'option (b), la revue est « tenue pour non
    faite » : faire dire au jury « malgré le go » rouvrirait la contradiction que le nœud 3 doit fermer. Le défaut venait du
    brouillon 2 ; ma v2 proposait « garder seulement « rien d'opérationnel n'a tourné » » sans le signaler explicitement.
  - *Correction attendue* : « la phrase d'entretien dit seulement que rien d'opérationnel n'a tourné ([P] l. 45-46) ; sous (a)
    seulement, elle peut ajouter que la revue a donné son accord ».

### (2) Nœud 6 (ii) (l. 151) — exacte et complète
- Les deux occurrences portent « le point (2) des nœuds listés par R-1581 », conforme à R-1581 ([R] l. 1539, point (2) :
  « CLAUDE.md dit “gain de H1 exigé dans chaque mode” (N-056), contraire à DG1-6 (b) »).
- Plus aucune collision : hors l'en-tête (l. 3, qui cite l'ancienne formule), les dix autres « nœud 2 » du brouillon (l. 5, 28,
  41, 48, 57, 66, 105, 132, 134, 142) désignent tous le nœud 2 de cette pièce, tranché par [D2].

### (3) Table des acteurs (l. 88) — tension avec [D2] levée ; un mineur neuf
- **Fait, conforme** : l'exception est explicite et bornée (« l'exception [D2] ne porte que sur les verdicts de ses propres
  essais »). Elle ne heurte plus [D2], qui fixe la lecture des verdicts en nombre compté (l. 8-10) et déclare l'écart à N-056
  (l. 16).
- **Mineur — « seuils calibrés sur ces épisodes » vide l'interdit des seuils.**
  - *Passage* : « épisodes d'épreuve ; notes et seuils calibrés sur ces épisodes ».
  - *Problème* : les seuils ne sont pas calibrés sur les épisodes d'épreuve, mais sur des épisodes honnêtes réservés (l. 77 de
    la pièce ; [T] l. 160-161). Lue à la lettre, la cellule n'interdit donc aucun seuil réel. Elle contredit ainsi l. 56 et l. 78
    de la pièce (« ni seuils calibrés »), N-056 l. 68-70 et le brief [S] l. 43 (« les notes et seuils calibrés des moniteurs »).
    L'en-tête (retouche (3)) porte la même lecture. L'origine est ma formulation v2 (« notes et seuils calibrés des moniteurs sur
    les épisodes d'épreuve »), qui avait ce défaut.
  - *Correction attendue* : « épisodes d'épreuve et leurs notes ; seuils calibrés (l'exception [D2] ne porte que sur les verdicts
    de ses propres essais) », et la même chose dans l'en-tête.

### (4) Section 0 (l. 46) et section 4 (l. 137) — exacte et complète
- « Sous réserve de licence ([X] l. 9 et 46) » est conforme : [X] l. 9 dit « candidat retenu, sous réserve de licence », et
  [X] l. 46 qu'une licence absente « invaliderait l'usage ».
- « Nœud “Bailey ou candidat 2” au défaut (a) jusqu'au 12 novembre, 08:02 UTC » est conforme à la consignation `06e8f102` :
  horodatage du 10 novembre à 08:02 UTC (l. 1), « défaut (a) sous 48 h » (l. 40-43).

## Décompte

Dans ce contrôle, j'ai vérifié moi-même sur source primaire 30 renvois (et recontrôlé inchangées les huit pièces de
confrontation) :
- le `diff` complet et les trois empreintes des brouillons ;
- [P] l. 45-46, 55-56 ; [E] l. 417, 565 ;
- R-597 et R-888 (dates), R-889 l. 1118, R-912 l. 1141, R-1581 l. 1539, R-1782 l. 1740 (en entier) ;
- [D2] l. 8-10, 16 ; [S] l. 43 ; [T] l. 160-161 ; [X] l. 9, 46 ; consignation l. 1, 40-43 ; [K] l. 20 ;
- les lignes 56, 77, 78, 88, 148, 151 et 158 du brouillon 3.

Aucun renvoi faux.

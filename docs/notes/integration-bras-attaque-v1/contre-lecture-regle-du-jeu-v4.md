# Contre-lecture R2, contrôle ciblé — règle du jeu du bras d'attaque, brouillon 4

- **Contre-lecteur** : le sous-agent des contre-lectures v1 à v3 (`a9765803`, `ed2cae2e`, `207b6ad1`). Je n'ai pas écrit le
  brouillon 4 (R2 tenu). Le mineur n° 1 ci-dessous vient de ma propre formulation v3 : je le dis.
- **Document** : `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon4.md` (commit `c8b21b91`),
  empreinte recalculée `3245a617f6a9028e…`, 166 lignes, sans compagnon. Les brouillons 3 (`48f09a20…`), 2 (`3fc927ba…`) et
  1 (`09aa6403…`) sont intacts (R12).
- **Périmètre** : les points (i) à (iv) de la consigne. Les pièces de confrontation ont été recontrôlées inchangées par
  empreinte : [T], [P], [E], [S], [D2], [K] et N-056. Le registre compte toujours 2034 lignes.
- **Accès** : ni R-604 ni R-605 n'ont été lues, ni le coffre ouvert. Aucun contenu de mode n'est reproduit.

## Verdict

**Scellable après deux retouches d'un mot (deux mineurs) ; aucun majeur.**
- Les points (i), (ii) et (iv) sont conformes. Le point (iii) l'est pour les seuils, mais pas encore tout à fait pour les notes.
- Les deux retouches se vérifient par un simple `diff` ; une nouvelle contre-lecture complète n'est pas nécessaire.

## (iv) Aucun autre changement — conforme

Le `diff` entre brouillons 3 et 4 compte 9 lignes (4 retirées, 5 ajoutées) :
- le titre ;
- l'en-tête : la ligne de statut du brouillon 3 devient deux lignes, le statut du brouillon 4 puis le statut du brouillon 3
  repris avec la description (3) corrigée et ainsi étiqueté ;
- la cellule de la table des acteurs (l. 89) ;
- la ligne du nœud 3 (l. 149).

Rien d'autre ne bouge. Le statut du brouillon 2 (l. 5) est inchangé.

## (i) Les trois faits du nœud 3 — chacun exact ; plus aucune négation non sourcée

- **Fait (i)** — conforme à R-597 ([R] l. 823, 27 octobre) :
  - R-597 dit : « En écrivant le lanceur des instances des bras A et B […], ma réponse a été arrêtée par un classifieur de
    sûreté » ; « Règle : un refus n'est jamais contourné ni reformulé » ; « je ne lance aucune instance d'attaque ».
  - La date, le lanceur des bras A et B, l'arrêt et l'absence de contournement sont exacts.
  - *Précision facultative* : R-597 consigne la décision de la session (« je ne lance aucune ») à la date du 27 octobre. La
    phrase du brouillon est exacte lue dans ce cadre, qui est le sien. Une lecture sans borne de temps est portée par [P] l. 45
    (« monté […], rien n'a tourné », 9 novembre). Écrire « et la session n'en a lancé aucune » collerait mot pour mot à la source.
- **Fait (ii)** — conforme à R-912 ([R] l. 1141) et R-889 ([R] l. 1118) :
  - R-912 dit : « Deux tentatives (un sous-agent, puis la session) » ont été arrêtées au moment d'écrire les valeurs, avec
    « Aucune reprise, même reformulée ». La citation « niveau coût et infrastructure, aucune recette d'évasion » est littérale.
  - « C'est une consigne, pas un constat » qualifie juste.
  - R-889 dit : « estimation de la malléabilité : hors gel R-611 ».
- **Fait (iii)** — conforme à R-1782 ([R] l. 1740) et à [K] l. 20 :
  - R-1782 dit : « portier et coffre de l'organisme actifs » ; « recettes scellées au coffre » ; « on ne consulte jamais les
    recettes ».
  - [K] l. 20 donne pour la branche `donnees/ideation-pilier-attaque-v1` un dernier commit au 8 novembre, 16:19 UTC.
  - « Recettes scellées et jamais consultées » décrit le régime du coffre, sans affirmer qu'il contient des recettes.
- **Négations** :
  - La négation universelle du brouillon 3 a disparu.
  - Les deux négations restantes sont sourcées : « aucune instance […] lancée » (R-597) et « valeurs […] pas écrites » (R-912).
  - La phrase de clôture (« aucun de ces faits ne dit qu'aucune recette n'a été écrite ; cette pièce ne sait rien du contenu du
    coffre ») est conforme à la section 6 (l. 159 ; coffre parmi les « pièces non lues »).

## (ii) La phrase d'entretien vaut sous (a) comme sous (b) — conforme

- « Le bras est monté et […] rien n'a tourné » reprend [P] l. 45 (« monté […], rien n'a tourné »). C'est vrai sous les deux
  options.
- « Sous (a) seulement, elle peut ajouter que la revue a eu lieu » : sous (b), la revue tenue pour non faite n'est plus évoquée.
  La contradiction est fermée.
- Le classifieur ne se dit que sur question, conformément à [P] l. 55-56 et [E] l. 417 et 565.

## (iii) Table des acteurs (l. 89) — seuils conformes ; un mineur sur les notes

- **Conforme** : les seuils calibrés sont interdits sans restriction. L'exception [D2] est bornée aux verdicts des propres
  essais du bras, ce qui ne heurte plus [D2] (l. 8-10, 16), ni [S] l. 35 (verdicts comptés, sous ses deux conditions), ni les
  l. 57 et 79 (l. 56 et 78 au brouillon 3) sur les seuils.
- **Mineur n° 1 — « épisodes d'épreuve et leurs notes » reste plus étroit que la source.**
  - *Problème* : N-056 l. 69-70 interdit « les épisodes d'épreuve, les notes ni les seuils calibrés », c'est-à-dire toutes les
    notes. Les l. 57 et 79 de la pièce disent aussi « ni notes », et [S] l. 43 « les notes et seuils calibrés des moniteurs ».
    La cellule ne vise que les notes des épisodes d'épreuve. Elle laisse donc hors de l'interdit les notes des épisodes honnêtes
    réservés, d'où se déduit le seuil à 1 % de fausses alertes (l. 78 ; [T] l. 160-161). C'est la même faille, déplacée des
    seuils vers les notes. Elle vient de ma formulation v3, appliquée telle quelle.
  - *Correction attendue* : « épisodes d'épreuve, notes, seuils calibrés (N-056 l. 68-70) ; seule exception, au bras déclaré
    « avec retour » : les verdicts de ses propres essais, en nombre compté ([D2]) ». C'est la liste de N-056 mot pour mot,
    exception bornée. Aligner de même les deux descriptions (3) de l'en-tête (statuts des brouillons 4 et 3).

## Mineur n° 2 — En-tête : l'heure du brouillon 3 est démentie par son commit

- **Passage** : l. 4, « Statut du brouillon 3 (repris, retouche (3) corrigée). 10 novembre 2026, vers 09:15 UTC ».
- **Problème** : le brouillon 3 est commité à 09:02:09 UTC (`f16d5edb`). Le brouillon 4 est daté « vers 09:10 UTC » (commit
  `c8b21b91`, 09:11:10 UTC) : l'en-tête place donc le brouillon 4 avant le brouillon 3. L'erreur venait du brouillon 3, et je
  ne l'avais pas relevée en v3. Elle est reprise dans une ligne réécrite.
- **Correction attendue** : « vers 09:00 UTC » (commit `f16d5edb`, 09:02:09 UTC).

## Décompte

Dans ce contrôle, 28 renvois ont été vérifiés sur source primaire, ou confirmés par une empreinte inchangée depuis leur lecture
en v2 ou v3 :
- le `diff` complet et les quatre empreintes des brouillons ;
- R-597 l. 823 et R-912 l. 1141 (texte cité), R-889 l. 1118, R-1782 l. 1740 ; [K] l. 20 ;
- [P] l. 45-46 et 55-56 ; [E] l. 417 et 565 ; N-056 l. 68-70 ; [S] l. 35 et 43 ; [D2] l. 8-10 et 16 ; [T] l. 160-161 ;
- les lignes 57, 78, 79, 89, 149 et 159 du brouillon 4 ;
- les heures de commit de `f16d5edb`, `207b6ad1` et `c8b21b91`.

Aucun renvoi faux.

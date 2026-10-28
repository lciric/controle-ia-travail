# Vérification de la v5 de la boucle extérieure du pilote 4 (registre v5, protocole v4, briefs v4, spécification du relevé (B) v3)

## En-tête

- **Vérificateur** : le sous-agent (`claude-opus-5-5`) qui a vérifié les v3 et v4 (rapports `1a7873e2…` et `b518f24c…`),
  relancé par conv-audit le 26 octobre 2026 sur `LISEZMOI-brief-verification-v5.md` (`1d5c2467…`, vérifié égal avant
  lecture, compagnon compris). Je n'ai écrit aucune des pièces vérifiées. Vérification ciblée, comme le demande le brief.
- **Heure** : rapport écrit le 2026-10-26 à 07:18:32 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Le début de
  la vérification n'est consigné par aucune commande d'écriture.
- **Pièces** : `fournis/`, dix-neuf entrées sur dix-neuf conformes à `../EMPREINTES-fournis-v1.txt` (`1b789f5e…`),
  vérifiées avant lecture ; dix-huit compagnons sur dix-huit justes. La v5 : registre v5 `f04e9263…` ; protocole v4
  `0e8cfee5…` ; briefs v4 `d5c7a60a…` ; spécification (B) v3 `d6ac5d3f…` ; LISEZMOI v5 `b2d25703…`. La v4 : registre v4
  `e36707b0…`, protocole v3 `acfd6426…`, briefs v3 `7f6217e8…`, spécification v2 `701b5270…`, LISEZMOI v4 `e99123c6…`.
  Brief v5 `6026f988…` (E1 à E8) ; mon rapport sur la v4 `b518f24c…` ; carte des facteurs v1 (`carte-facteurs-v1.json`
  `2aaedd08…`, `.md` `47fa6100…`), zones interdites v1 (`.json` `0082519c…`, `.md` `be486ea8…`), leur LISEZMOI
  `cbe00172…` ; brief du script de lecture v3 `78861f99…` ; message de conv-audit qui en corrige le point 2 `19857824…`.
- **Lu** : en entier, le brief de vérification, le brief v5, le message, le LISEZMOI v5 ; les quatre pièces par la
  comparaison bloc à bloc avec la v4 (tous les blocs) et dans les passages cités ; le brief du script, points 2 et 5 ;
  de la carte, F01, F02, le domaine de F09, les § 4 à 7, et les lignes D4 à D10 de son LISEZMOI (pour E8 seulement) ;
  des zones, une recherche de `VERSION` et de la l. 27.
- **Exécuté** : `sha256sum`, `sha256sum -c`, `ls`, `wc`, `grep` (dont un essai de `grep -w` sur une ligne passée par un
  tube, sans fichier écrit), `sed -n`, `diff`, `cut`, `tr`, `printf`, `date -u`. **Python : non lancé.**
- **Non ouvert** : rien hors de ce dossier ; aucun fichier de course, aucun script, aucun score. Aucun `git`, aucun
  sous-agent, aucun réseau, aucune clé. Ce rapport ne contient aucun score, aucun critère ni aucune stratégie de
  classement des tâches.
- Numéros de lignes : ceux des pièces de la v5 (« registre », « protocole », « briefs », « spécification »,
  « LISEZMOI ») ; « carte », `carte-facteurs-v1.md`.

## Verdict

**Utilisable après corrections.**

Les sept constats CLB4 sont traités dans les fichiers ; E1 à E8 sont appliquées telles quelles ; les 74 blocs de la
comparaison sont tous demandés ou déclarés ; les libellés (iii) concordent avec le message au script ; plus aucun fait
mécanique de M au registre. Un constat à corriger avant usage : **CLB5-01**, un cas sain du relevé (B) que la règle
d'E1 refuse. Cinq mineurs (CLB5-02 à CLB5-06), dont deux corrections à mes propres constats de la v4.

## 1. CLB4-01 à CLB4-07, et E1 à E8

| constat et décision | appliquée telle quelle, dans les fichiers | où (vérifié) | réserve |
|---|---|---|---|
| CLB4-01, E1 | oui : nom tiré du dernier élément du chemin, sans `-tentative<N>`, égal à la table close de deux lignes ; clé égale sur les trois lignes ; lignée de l'extrait égale à la table, sinon déduite et dite ; confirmation en simulation au § 8 | spécification l. 54–55, 141–162, 181–190, 328–337, 368–375 ; protocole l. 58–61, 353–378, 434 ; registre l. 91–95, 639–642 | CLB5-01, CLB5-06 (b) |
| CLB4-02, E2 | oui : les deux libellés du point 4 bis ; la correction dans un champ à part ; le sens « sans objet (non rejeté) » pour un non-rejet ; correspondance libellé → verdict ; arrêt sur tout autre libellé ; l. 581 de la v4 réécrite | registre l. 115–121, 152–153, 591–603 ; briefs l. 365–371 ; protocole l. 527–536, 541–544, 621 | CLB5-04 |
| CLB4-03, E3 | oui : « signalements (fichier test) : N » ; ni compte, ni proportion, ni borne, ni valeur p, ni libellé, ni signalement de l'autre course ; jamais de valeur p ajustée, de rang ni de seuil ; étape 1 de l'analyste final | protocole l. 95, 150–152, 532–534, 621 ; registre l. 81–85 ; briefs l. 361–364 | — |
| CLB4-04, E4 | oui : section 3A pour la lecture finale ; une entrée finale par course, puis une entrée de clôture sans verdict ; une transmission par course | briefs l. 14–16, 266–284 ; protocole l. 102, 150–154, 208–212, 234–238, 549–551 | — |
| CLB4-05, E5 | oui, la phrase mot pour mot | registre l. 20–22 | CLB5-05 |
| CLB4-06, E6 | oui : `oui` seulement sans « aucune pièce archivée », sinon `absent`, jamais `non` ; ligne reconnue par son début ; aucune chaîne du nom du fichier dans le script ; artefact 4 établi par `grep` | spécification l. 64–69, 77–80, 195–196, 221, 309–313, 338–339 | CLB5-06 (a) |
| CLB4-07, E7 | oui : (a) « deux messages » dans les quatre statuts ; (b) trois valeurs ; (c) phrase (iv) identique à celle du brief du script (comparée lignes jointes) ; (d) bornes de mot sans lettre, chiffre, `-` ni `_` | statuts ; protocole l. 252, 487–500, 428 ; registre l. 161–169 | CLB5-02, CLB5-03 (c) |
| E8 | oui : lecture par colonnes et segments, repli par lignes non pris ; gel de Z03 confirmé ; `VERSION` (l. 27) en accompagnement ; carte et zones citées par nom et empreinte complète (égales à la liste d'empreintes), « v1, sous réserve de leur contre-lecture » ; 0,01, 0,03 et leurs copies (F05, F06, F13, F14) gelés par le point 7 ; lignes partagées, segments de Z03 et points PHB-1 à PHB-4 cités comme la carte les donne (carte, § 4 et § 5) | protocole l. 271–285, 298–307, 427, 567–577, 617–622 ; briefs l. 203–205, 234–237, 319–321 | CLB5-03 (a), (b) |

## 2. Comparaison v4 → v5

| fichiers comparés | blocs | lignes retirées | lignes ajoutées | blocs non déclarés |
|---|---|---|---|---|
| registre v4 → v5 | 17 | 49 | 79 | aucun |
| protocole v3 → v4 | 33 | 60 | 119 | aucun |
| briefs v3 → v4 | 9 | 27 | 48 | aucun |
| spécification v2 → v3 | 15 | 30 | 82 | aucun |

Chaque bloc relève d'un constat, d'une décision ou d'un changement déclaré (LISEZMOI, § 4, points 1 à 9 ; § 6). **Aucun
écart.** Les ajouts déclarés :

| ajout | tient ? |
|---|---|
| `identite.lignee_source` (`extrait` ou `deduite_de_la_cle_controle_non_independant`) | oui : c'est la façon de « dire » la lignée déduite dans la grammaire close (identifiant de 42 caractères, sous la borne de 48) ; toujours écrit ; l'analyste recopie la phrase (protocole l. 361, 377–378 ; registre l. 640–641) |
| tenue de la valeur (c) du paramètre « famille » | oui, comme choix déclaré (LISEZMOI, § 4, point 6) ; deux règles manquent (CLB5-02) |
| exemple (a) de G5 | oui : F01 (l. 2102, 2106) et F02 (l. 31, 1932) ont des lignes entières, de deux facteurs distincts (carte, § 2) ; l'ancien exemple (seuils de stagnation et de retour arrière) tomberait désormais sous (h), pas sous (a) |
| artefacts 15 à 19 de la spécification | oui : un par refus nouveau d'E1 (clé différente d'une ligne à l'autre ; nom du dossier ; clé hors de la table ; lignée de l'extrait) et l'artefact d'E6 ; 16 et 18 portent leur côté sain ; mais le cas sain 1 contredit E1 (CLB5-01) |
| artefacts (g) à (i) de G5 | oui : ligne partagée hors des segments du facteur ; point hors boucle ; `principal.py` hors de `VERSION` déclaré comme accompagnement ; il manque des cas sains (CLB5-03) |

Les autres changements déclarés (statuts, renvois de version, ancrage inchangé de la voie « rondes tournées », exception
du signalement « impossible », suites d'E4 et d'E8, table du § 7 du registre) sont justes.

## 3. Libellés (iii) contre le message au script

Concordent : les deux libellés, mot pour mot (« changement au-delà du bruit des tâches » ; « dans le bruit des tâches ») ;
la correction de multiplicité dans un champ à part ; le sens seulement pour un rejet, sinon « sans objet (non rejeté) » ;
valeur p brute de la course seule, jamais de valeur p ajustée, de rang ni de seuil ; ligne d'état « signalements (fichier
test) : N » (registre l. 115–121, 152–153, 591–603 ; briefs l. 361–371 ; protocole l. 95, 527–536, 621). Réserve sur les
mots du champ de correction (CLB5-04).

## 4. Faits de course de M au registre

Plus aucun fait mécanique de M : la déclaration porte la phrase d'E5 (l. 20–22) ; le coût total et l'heure de fin lus
pour la v4 sont nommés sans valeur (l. 26–28). Reste un fait de lancement, l'heure de départ de M (CLB5-05). Le nom du
dossier `pilote4-gemini-v6-2-v1-tentative2` est une identité, nécessaire à la lecture (E1).

## Constats

### CLB5-01 — à corriger avant usage (avant les essais du script du relevé) — Un cas sain du relevé (B) que la règle d'E1 refuse

- **Où** : spécification l. 285–293 (cas sain 1 : « v6.2.1 continue ; v5.3 continue ; v6.2.1 en deux et en trois
  segments », « Attendu : un relevé écrit par cas ») ; l. 149–162 (refus si la clé n'est pas dans la table close de deux
  lignes) ; l. 333 (artefact 17).
- **Ce qui ne va pas** : le cas « v5.3 continue » de la série v13 tourne sous la clé `v5-3` (texte v5 du pilote, l. 55 :
  `COURSE=v5-3`, nom `pilote4-gemini-v5-3-v1`, lignée `gemini-organisme-v5-3` ; lu pour la vérification de la v4, non
  fourni ici). Cette clé n'est pas dans la table close : sous E1, le relevé est refusé, alors que le cas sain l'attend
  écrit. L'auteur du script devrait soit déclarer l'essai en échec, soit ajouter `v5-3` à la table, ce qu'E1 exclut.
- **Correction** : retirer « v5.3 continue » des cas sains et s'en servir pour l'artefact 17 (clé hors de la table, la
  même sur les trois lignes → refus) ; garder trois cas sains de la série v13, sous la confirmation du § 8.

### CLB5-02 — mineur — Valeur (c) du paramètre « famille » : deux règles manquent

- **Où** : protocole l. 487–500 (§ 12.3), l. 195–207 (§ 4, étapes 5 à 7), § 12.4.
- **Ce qui ne va pas** : sous (c), la ronde 1 a deux parties B par course, mais rien ne dit laquelle décide si elles
  concluent différemment (« transmissible » contre « non transmissible ») ; l'étape 7 ne transmet qu'une correction
  « transmissible ». Et l'accord entre les deux familles, qui est la raison d'être de (c) (pièce des points, point 1 :
  « mesure une fois la corrélation des deux familles »), n'est consigné nulle part : le § 12.4 ne parle que d'un
  contre-lecteur.
- **Correction** : « sous (c), une correction n'est transmise que si les deux parties B la disent transmissible » ;
  « l'accord de chaque partie A avec l'analyste, et des deux parties A entre elles, est consigné à chaque course ».

### CLB5-03 — mineur — Gardes : des règles nouvelles sans cas sain qui les montre (R5)

- **Où** : protocole l. 427 (G5), l. 428 (G6), l. 271–285 ; carte l. 181 (domaine de F09), carte § 4 et § 5.
- **Ce qui ne va pas** : (a) les cas sains de G5 couvrent les lignes partagées (l. 997, 2103, 2104) et la ligne de
  `VERSION`, pas les lignes de F04 qui portent un segment de Z03 (`principal.py` l. 1009, 1011, 1039), ni les lignes qui
  portent un point hors boucle (`principal.py` l. 994 ; `mitose_spectrale.py` l. 75 et 117 ; `memoire_isvd.py` l. 132).
  Un G5 qui refuserait ces lignes entières, c'est-à-dire le repli qu'E8 écarte, passerait tous ses essais. (b) La carte
  range la l. 27 (`VERSION`) dans le domaine de F09 (« 16–27 ») ; E8 en fait un accompagnement : un G5 qui suit la carte
  la compterait comme un second facteur. (c) G6 : la borne de mot est bien définie (ni lettre, ni chiffre, ni `-`, ni
  `_`) ; c'est plus juste que ma formule de CLB4-07 (d) : un `grep -w` trouve `gemini-organisme-v6-2` dans
  `gemini-organisme-v6-2-s`, et `v6-2` dans `v6-2-s` (essayé). Mais aucun cas sain ne le montre.
- **Correction** : (a) cas sain : sur une de ces lignes, un caractère changé hors du segment, dans le facteur déclaré :
  accepté ; (b) dire que les lignes d'accompagnement ne comptent pour aucun facteur, et prendre, pour le cas sain « dont
  la ligne de `VERSION` », un facteur autre que F09 ; (c) cas sain : une pièce de S qui porte sa lignée et sa clé :
  acceptée.

### CLB5-04 — mineur — Les mots du champ de correction sont fixés par les pièces, pas par le message au script

- **Où** : message au script (« par exemple « correction : Holm, quatre tests, niveau 0,05 » ») ; registre l. 117–119 ;
  protocole l. 531–532 ; briefs l. 361–364 (étape 1 de l'analyste final, qui s'arrête « sinon »).
- **Ce qui ne va pas** : les pièces citent ces mots comme exacts, mais le message au script ne les donne qu'en exemple,
  et ne dit rien des mots d'un fichier « holm-deux ». Si le script écrit d'autres mots, l'analyste final peut s'arrêter.
- **Correction** : conv-audit fixe les mots au script (ceux d'E2, « deux tests » compris), ou l'étape 1 lit la taille de
  la famille sans exiger ces mots.

### CLB5-05 — mineur — Un fait de lancement de M reste au registre

- **Où** : registre l. 265–266 (§ 0.7) : « partie le 26 octobre 2026 à 03:51 UTC sous le lanceur v10 », présent depuis
  la v3.
- **Ce qui ne va pas** : ce n'est pas un fait mécanique, et aucune règle ne l'emploie ; mais c'est un fait de la course M,
  servi aux agents de S.
- **Correction** : retirer l'heure de départ si « aucun fait de course de M » s'entend à la lettre ; garder le lanceur.

### CLB5-06 — mineur — Spécification v3 : deux précisions

- (a) L'artefact 4 attend « le fichier jamais ouvert » (instantané des accès) ; or le § 2, point 1, hache chaque fichier
  que liste `EMPREINTES-pilote-v1.txt`. Si la liste fermée nomme la réponse à la question, l'instantané la montrera
  ouverte (doute déclaré : LISEZMOI l. 111–112). Écrire l'attendu : « jamais lu hors du hachage de la liste fermée »,
  comme `ferme.tar.gz`.
- (b) « la clé … sur les trois lignes qui la portent » (l. 149–151, 184–186 ; E1) : une quatrième ligne la porte,
  « - registre : une ligne <GO> … question (<COURSE>) … » (extrait des lignes des lanceurs, v10 l. 557 et v11 l. 574 ;
  lu pour la v4, non fourni ici). Mon constat CLB4-01 n'en comptait que trois. Sans effet : cette ligne n'est pas
  contrôlée. Écrire « au moins ces trois lignes », ou la contrôler aussi si elle est écrite en simulation.

## Ce que j'ai trouvé conforme, en plus

- Les empreintes complètes de la carte et des zones (JSON) citées au protocole sont celles de la liste d'empreintes.
- Le cas sain associé à l'artefact 16 (nom suivi de `-tentative2` → relevé écrit, nom sans le suffixe) éprouve la règle
  d'E1 telle qu'elle s'appliquera au dossier réel de M.
- La section 3A de la lecture finale garde la cécité (aucune pièce de l'analyste, pas de partie B) et ne nomme pas
  l'autre course.

## Ce que je n'ai pas pu vérifier

- Les scripts de lecture v3 et du relevé, leurs essais, la table de correspondance (en écriture) : que le script de
  lecture écrive les mots d'E2 ; que les chemins et clés simulés des séries v13 et v14 passent la table close.
- La contre-lecture de la carte et des zones v1 (faite à part) ; la règle des lignes insérées (carte, § 0, point 9).
- Les deux citations hors de ce dossier (texte v5, l. 55 ; extrait, v10 l. 557 et v11 l. 574) : faites de mémoire de la
  vérification de la v4, non relues ici.

## Écarts déclarés

1. Deux faits cités de pièces lues pour la vérification de la v4, que ce dossier ne fournit pas (CLB5-01, CLB5-06 b) :
   non relues, pour ne rien lire hors de ce dossier.
2. Un essai de `grep -w` sur une ligne passée par un tube (CLB5-03 c) ; aucun fichier écrit.
3. Rien d'autre écrit que ce rapport et son compagnon ; Python non lancé.

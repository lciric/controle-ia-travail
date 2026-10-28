# Vérification de la v4 de la boucle extérieure du pilote 4 (registre v4, protocole v3, briefs v3, spécification du relevé (B) v2)

## En-tête

- **Vérificateur** : le sous-agent (`claude-opus-5-5`) qui a contre-lu la v2 (rapport `2eb11e6a…`) et vérifié la v3
  (rapport `1a7873e2…`), relancé par conv-audit le 26 octobre 2026 sur `LISEZMOI-brief-verification-v4.md` (`6a2f1196…`,
  vérifié égal avant lecture, compagnon compris). Je n'ai écrit aucune des pièces vérifiées.
- **Heure** : rapport écrit le 2026-10-26 à 06:44:47 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Le début de
  la vérification n'est consigné par aucune commande d'écriture.
- **Pièces** : `fournis/`, dix-huit entrées sur dix-huit conformes à `../EMPREINTES-fournis-v1.txt` (`15622a37…`),
  vérifiées avant lecture ; quinze compagnons `.sha256` sur quinze justes. La v4 : registre v4 `e36707b0…` ; protocole v3
  `acfd6426…` ; briefs v3 `7f6217e8…` ; spécification (B) v2 `701b5270…` ; LISEZMOI v4 `e99123c6…`. Ses consignes : brief
  v4 `dc5b823b…` ; messages de conv-audit `9b80111a…`. La v3 : registre v3 `a5abc176…` ; protocole v2 `0c71a74b…` ;
  briefs v2 `60553a1b…` ; spécification v1 `3ed32fe8…` ; LISEZMOI v3 `218619cf…` ; mon rapport `1a7873e2…`. Le reste :
  pièce des points pour Lazar `ac105262…` ; extrait des lignes des lanceurs v10 et v11 `e3ec880c…` ; texte v5 du pilote
  `1943f39a…` (qui prime) ; LISEZMOI du script de lecture v2 `2f328fee…` ; brief du script de lecture v3 `78861f99…`.
- **Lu en entier** : la spécification v2, le LISEZMOI v4, le brief v4, les messages, la pièce des points, l'extrait, le
  brief du script v3, mon rapport v3. **Registre, protocole et briefs** : lus par la comparaison bloc à bloc avec leurs
  versions de la v3 (que j'avais lues en entier), et dans tous les passages cités ici. **Texte v5** : les lignes citées
  (table de correspondance, § Plan, liste d'arrêt). **Non relu** : le LISEZMOI du script v2 (le brief du script v3 le
  remplace pour le point 4).
- **Exécuté** : `sha256sum`, `sha256sum -c` (dont un essai sur une liste passée par un tube, sans fichier écrit), `ls`,
  `wc`, `grep`, `sed -n`, `diff`, `awk`, `cut`, `date -u`. **Python : non lancé.**
- **Non ouvert** : aucun fichier de course, aucun script, aucun score. Aucun `git`, aucun sous-agent, aucun réseau, aucune
  clé. Ce rapport ne contient aucun score, aucun critère ni aucune stratégie de classement des tâches. Deux lectures hors
  de ce dossier : voir « Écarts ».
- Numéros de lignes : ceux des fichiers nommés. « Registre », « protocole », « briefs », « spécification », « LISEZMOI »
  désignent les pièces de la v4 ; « brief du script », le brief du script de lecture v3 ; pour l'extrait, les numéros de
  ligne des lanceurs, tels que l'extrait les donne (« v10 l. 250 »).

## Verdict

**Utilisable après corrections.**

Les huit constats CLB3 sont traités dans les fichiers eux-mêmes ; D1 à D7, les deux précisions à D5 et la correction à
D4 sont appliquées telles quelles ; la comparaison des fichiers ne montre aucun bloc non déclaré ; l'identité de la
course S concorde avec le texte v5 ; les points pour Lazar sont cités tels que la pièce les pose, sans défaut pour une
dépense ; G6, G8 bis et G12 ont chacune un cas sain et un artefact ; les faits de course lus n'ont changé aucune règle.
Deux constats à corriger avant usage : **CLB4-01** (deux champs exigés du relevé (B) n'ont aucune source : en l'état, le
relevé ne s'écrit jamais et la boucle ne démarre pas) ; **CLB4-02** (le libellé (iii) que la lecture finale recopie
n'est pas celui que le script v3 écrit ; lu à la lettre, un rejet passe pour un non-rejet). Cinq mineurs (CLB4-03 à
CLB4-07).

## 1. Les constats CLB3-01 à CLB3-08, dans les fichiers

| constat | traité dans les fichiers | où (vérifié) | réserve |
|---|---|---|---|
| CLB3-01 (a) noms | oui | registre l. 66–81 ; protocole l. 114–148, 484–495 ; briefs l. 63–67, 335–341 | — |
| CLB3-01 (b) contenu, « provisoire » | oui | registre l. 73–81 ; protocole l. 141–148, 398 (G12) | CLB4-03 |
| CLB3-01 (c) G8 bis | oui, réécrite | protocole l. 394, 401–402 ; briefs l. 150–153 | — |
| CLB3-01 (d) script v1 décrit comme sortie | oui | registre l. 66–69 ; protocole l. 117–119 | — |
| CLB3-02 | oui (D2) | protocole l. 156–163, 171–199, 221–246, 391 ; registre l. 248–273, 636–644 ; briefs l. 13–31, 94–96, 176–258, 275–324 | CLB4-04, CLB4-05 |
| CLB3-03 | oui (D3) | registre l. 19–30, 322–341, 645–648 ; spécification l. 203–207, 335 ; briefs l. 146–149 ; protocole l. 217 | — |
| CLB3-04 | oui (D4 corrigée) | pièce des points ; protocole l. 77–86, 249–259, 311–316, 359–371, 453–457, 552–571 ; registre l. 227–229, 346–349, 423–427 | CLB4-07 (b) |
| CLB3-05 | oui (D5 et ses deux précisions) | spécification l. 20–22, 47–64, 106, 116–166, 255–292, 321–326 ; protocole l. 56–58, 321–346 ; registre l. 82–88 ; briefs l. 132–139 | CLB4-01, CLB4-06 |
| CLB3-06 (a) libellés | oui | registre l. 105–116, 507–525, 577–584 ; briefs l. 347–351 | CLB4-02 (libellé (iii) ; le sens et « aucune tâche sans réponse » concordent) |
| CLB3-06 (b) faits mécaniques du fichier `test` | oui | registre l. 101–103 ; briefs l. 146–147 | — |
| CLB3-06 (c) délégation sur `test` | oui, mot pour mot | registre l. 99–100, 127–128, 133–134 ; briefs l. 150–151 | — |
| CLB3-06 (d) phrase (iv) | renvoyé au script, que le brief du script aligne (point 5) | registre l. 154–156 | CLB4-07 (c) |
| CLB3-07 (a) | oui, mot pour mot (D6) | protocole l. 92 | — |
| CLB3-07 (b) | oui sur le fond | protocole l. 92, 569 | CLB4-03 (c) |
| CLB3-08 (a) à (d) | oui | registre l. 236–241, 636–638 ; briefs l. 66–70, 190–193, 222–237, 301–303, 331–333 ; protocole l. 266–270, 390 | — |

## 2. Décisions D1 à D7, précisions à D5, correction à D4

| décision | appliquée telle quelle | où | réserve |
|---|---|---|---|
| D1 | oui | registre l. 66–116, 141–148 ; protocole l. 92, 114–148, 394, 398, 401–402, 484–495 ; briefs l. 63–67, 150–153, 335–351 | CLB4-02, CLB4-03 |
| D2 | oui ; règle mot pour mot (protocole l. 156–159 ; registre § 0.7) | pièces : une par course ; dans une correction motivée par S, seule la ligne « condition de préséance » nomme M, sans fiche ni verdict (registre l. 636–644 ; briefs l. 30, 181–187, 205) ; le correcteur de S est neuf, ne lit que la pièce de S et reçoit la pièce de M par sa référence (protocole l. 183–189) ; une partie B par course. Journal : une entrée par course et par correction (protocole l. 221–225). Gardes : G6 réécrite (l. 391) ; G10 n'emploie que des dossiers d'audit ; M et S ne servent jamais de paire (l. 476–479) | CLB4-04 (b), CLB4-05 |
| D3 | oui | registre l. 328–341 : règle de la v2 pour M et S ; voie « rondes tournées » réservée à une relance lancée après la poussée du registre v4, avec `statut = ok`, sans `delai_depasse` ni refus `plafond`, et `g000` tourné ; origine déclarée l. 22–23 ; spécification l. 203–207, 335 ; briefs l. 146–149. Ce sont les seuls emplois de `rondes_tournees` dans les quatre pièces | — |
| D4, corrigée | oui | pièce citée, non reposée (protocole l. 552–571) ; famille : défaut (a), 48 heures après l'envoi (l. 453–457) ; seuils 0,78 et 0,65 : « la carte tranche, un facteur ou deux » (l. 253–255, 566 ; registre l. 346–349) ; 0,01 et 0,03 sous le point 7 (protocole l. 256–259 ; registre l. 227–229, 423–427) ; la phrase « les deux seuils comptent pour un seul facteur (ton choix 23, confirmé) » n'est dans aucune pièce ; carte et zones par un autre sous-agent (protocole l. 93, 249–250, 567) | CLB4-07 (b) |
| D5 et ses deux précisions | oui | `identite.porte_m_precedente = oui|absent` (spécification l. 131, 155–157) ; champs exigés et refus, code 3, nom du champ seul (l. 134–139) ; cas sain v14 (l. 264–268) ; artefacts 11 à 14 (l. 287–292) ; ligne S du tableau et règles (protocole l. 325–346) ; registre l. 82–88 ; briefs l. 132–139 | CLB4-01, CLB4-06 |
| D6 | oui, mot pour mot | protocole l. 92 | — |
| D7 (a) à (d) | oui | voir le § 1 ; les commandes des briefs (l. 222–237) donnent les en-têtes `objet-origine/` et `copie-organisme/`, les seuls que G5 (f) accepte (protocole l. 390) | — |

## 3. Ce qui a changé de la v3 à la v4 (comparaison des fichiers)

| fichiers comparés | blocs | lignes retirées | lignes ajoutées | blocs non déclarés |
|---|---|---|---|---|
| registre v3 → v4 | 38 | 117 | 229 | aucun |
| protocole v2 → v3 | 45 | 148 | 225 | aucun |
| briefs v2 → v3 | 33 | 94 | 156 | aucun |
| spécification v1 → v2 | 16 | 31 | 112 | aucun |

Chaque bloc relève d'un constat, d'une décision, d'une précision, de la correction à D4 ou de l'un des changements
déclarés 1 à 15 (LISEZMOI l. 74–114) ; les blocs de statut et de sources relèvent des changements 1 et 2 et de
l'origine déclarée (D3). La spécification ne change que dans les sections que son statut nomme (§ 1, 2, 4.1, 4.2, 4.5,
6, 8, 9), comme le demandait le message 1. **Aucun écart.** Les changements déclarés eux-mêmes sont justes : le 3
concorde avec le brief du script (un non-rejet porte le sens « sans objet (non rejeté) ») ; le 9 est juste (`sha256sum -c
--strict` ignore la ligne de commentaire : essayé, GNU coreutils 9.4) ; le 13 appelle une précision (CLB4-06 a).

## 4. Fichiers de lecture et brief du script v3

| élément | brief du script v3 | v4 | concordance |
|---|---|---|---|
| fichier `test` | `lecture-<dossier>-test-v3.{json,md}`, à la fin de chaque course | `-test-v<n>`, `<n>` ≥ 3 écrit au manifeste | oui |
| fichiers `test_final` | à la fin de S, `…-test-final-holm-quatre-v3` pour chaque course ; `…-holm-deux-v3` pour M avec `--sans-seconde-course` ; plus de « provisoire » | les mêmes (registre l. 73–81 ; protocole l. 141–148, 484–495 ; G12) | oui |
| ce qu'un « holm-quatre » porte | par test (iii) : valeur p brute, sens, libellé « rejeté au niveau 0,05, famille de quatre » ou « non rejeté » ; par cellule, « aucune tâche sans réponse » | valeur p brute, verdict après Holm, sens, « aucune tâche sans réponse » (registre l. 105–110) ; mais le libellé attendu est « changement au-delà du bruit des tâches » ou « non rejetée (bruit) » (briefs l. 347–349 ; registre l. 581) | non pour le libellé (CLB4-02) ; oui pour le reste |
| ce qu'il ne porte pas | ni valeur p ajustée, ni rang, ni seuil ; de l'autre course, ni compte, ni proportion, ni borne, ni valeur p, ni libellé, ni signalement | de l'autre course, ni compte, ni proportion, ni valeur p, ni libellé (registre l. 74–75 ; protocole l. 146, 489–490 ; briefs l. 345) ; rien sur la valeur p ajustée, le rang, le seuil | en partie (CLB4-03 a, b) |
| ligne d'état | « signalements (fichier test) : N » | « signalements de test : N » (protocole l. 92, 569) | sur le fond (CLB4-03 c) |
| phrase (iv) | fixée mot pour mot, « deux courses », texte v5 cité | paraphrase juste ; conditionnel périmé (registre l. 150–156) | sur le fond (CLB4-07 c) |
| délégation sur `test` | « impossible par construction (référence égale à 1) » | le même, mot pour mot | oui |

Les écarts viennent des mots de D1 (brief v4 l. 43–45 et 70), que l'auteur a appliqués tels quels ; le brief du script ne
figure pas parmi ses lectures (LISEZMOI l. 22–25).

## 5. Identité de la course S ; sources des champs exigés de (B)

**Ligne S du tableau** (protocole l. 325–338) contre le texte v5 : nom `pilote4-gemini-v6-2-s-v1`, lignée
`gemini-organisme-v6-2-s`, question `a54da93e…` (commit `4772b525…`), objet `7ea32705…`, arbre `4f13647a…`, 26 fichiers
(l. 55) ; lanceur v11 `21854b79…` (l. 60) ; graine 6967892196853497016 (l. 103) ; noyau `8e5e2f7b`, banque `157a2b45…`
(l. 71, 83) ; texte v5 `1943f39a…`. Dossier `pilote4-gemini-v6-2-s-v1`, sans suffixe (D5 ; brief du script § 4).
**Concorde.**

**Champs exigés de la spécification v2 et lignes des lanceurs** (extrait) :

| champ exigé | ligne qui le porte | source |
|---|---|---|
| `identite.commit` | « - dépôt : … ; HEAD : … (c'est le « commit » que le manifeste consignera) » (v10 l. 251 ; v11 l. 265) | oui |
| `identite.lanceur`, `identite.lanceur_empreinte` | « - lanceur : <nom>, sha256 … » (v10 l. 253 ; v11 l. 267) | oui |
| `identite.graine` | « - préenregistrement : …, graine <GRAINE> de la course <COURSE> … » (v10 l. 512 ; v11 l. 529) | oui ; ligne écrite dans un bloc dont la condition n'est pas dans l'extrait (à confirmer en simulation) |
| `identite.nb_fichiers`, `identite.arbre`, `identite.question_empreinte` | « - organisme : <N> fichiers, empreinte d'arbre … ; question (<COURSE>) : sha256 … » (v10 l. 528 ; v11 l. 545) | oui |
| `releve.course` | aucune ligne ne porte le nom ; la **clé** `<COURSE>` est sur trois lignes (v10 l. 250, 512, 528 ; v11 l. 264, 529, 545) | **aucune source écrite** (CLB4-01) |
| `identite.lignee` | aucune (recherche de « lign » dans l'extrait : seulement l'en-tête et les lignes d'erreur) | **aucune source** (CLB4-01) |

Facultatifs : `identite.porte_m_precedente` vient de v11 l. 379 seule (le motif « ; lanceur attendu » écarte v10 l. 362
et 510, v11 l. 527) : juste ; `identite.noyau` et `identite.banque_empreinte` de « - code : … » (v10 l. 470 ; v11
l. 487) ; `unite.g001.question_servie` de « - réponse à la question : … » (v10 l. 868 et 870 ; v11 l. 885 et 887 ;
CLB4-06 a).

## 6. Points pour Lazar

| point | pièce : défaut ; moment | protocole § 16 | conforme |
|---|---|---|---|
| 1 famille du contre-lecteur | (a), 48 heures ; avant la contre-lecture de la ronde 1 | le même, envoi vers 05:42 UTC | oui (CLB4-07 b) |
| 2 graines | aucun (dépense) ; la retenue tient | ligne « ouverture de la lecture » : aucun (dépense) ; avant toute lecture | oui |
| 3 plafond | aucun (dépense) ; au premier devis de relance | le même | oui |
| 4 symétrie avant (b) | (a), 48 heures ; avant le texte de (b) | le même | oui |
| 5 ordre des courses | information (tranché par conv-audit) | le même ; Lazar peut le reprendre | oui |
| 6 question d'une relance | aucun (dépense) ; au GO de la relance | le même | oui |
| 7 seuils 0,01 et 0,03 | (a) garder ; avant une ronde 2 | le même | oui |

Aucune dépense n'a de défaut : les défauts des points 1, 4 et 7 sont des options sans dépense (pièce des points l. 30,
75, 120).

## 7. Gardes G6, G8 bis et G12 (R5)

Chacune a un cas sain et un artefact (protocole l. 391, 394, 398) : G6, une pièce qui ne porte que sa course, et une
correction motivée par S dont la seule mention de M est la ligne « condition de préséance », contre une pièce qui porte
le nom, une fiche ou un verdict de l'autre course ; G8 bis (a) sur données synthétiques et (b) à l'assemblage, chacune
avec son artefact ; G12, des noms `-test-v<n>` et `-test-final-holm-…-v<n>` à la version du manifeste, contre un
`-provisoire-`, une version inférieure à 3 ou autre que celle du manifeste. G5 (f) et G11 sont mises à jour. **Conforme
sur le papier** : les gardes restent à écrire et à essayer (protocole l. 570).

## 8. Faits de course lus par l'auteur

Déclarés (registre l. 25–30 ; LISEZMOI l. 140–143). Aucune valeur recopiée : le coût total et l'heure de fin de M ne
figurent dans aucune des cinq pièces (recherche sur leurs valeurs et leurs formes) ; seul le nom du dossier de S est
écrit, comme D5 le demande. Aucune règle de lecture changée : aucun bloc de la comparaison ne touche HC-P4-07 (bornes de
coût et de durée) ni le plafond ; l'heure de fin de M n'entre que par l'ordre des poussées (protocole l. 78–80 : la v2
avant la fin de M, la v3 après), un fait sur les pièces, pas une règle. **Conforme.**

## Constats

### CLB4-01 — à corriger avant usage — Relevé (B) : deux champs exigés sans source ; en l'état, le relevé ne s'écrit jamais

- **Où** : spécification l. 106, 130, 134–139, 158–161, 321–323 ; protocole l. 56–58, et § 9 (lignes `releve.course` et
  `identite.lignee`) ; LISEZMOI l. 120–122 ; extrait, v10 l. 250, 512, 528 et v11 l. 264, 529, 545 ; texte v5 l. 55, 141.
- **Ce qui ne va pas** : `releve.course` (nom de la course) et `identite.lignee` sont exigés (D5, précision 2) et aucune
  ligne des lanceurs ne les porte. La spécification le dit et renvoie à une table de correspondance encore à écrire
  (« extrait mécanique ou manifeste », non confirmé). En l'état, le script refuse d'écrire sur toute course, cas sains
  compris, et la boucle ne démarre pas (protocole, § 1, condition 2). Or la **clé** de course est portée par trois lignes
  (« - course : <COURSE> ; … », « … de la course <COURSE> … », « … question (<COURSE>) : … »), et les textes du pilote
  fixent clé, nom et lignée ensemble (texte v5 l. 55 : `COURSE=v6-2-s`, nom `pilote4-gemini-v6-2-s-v1`, lignée
  `gemini-organisme-v6-2-s` ; clé `v6-2` de M, l. 141 ; nom et lignée de M au texte v4, non fourni). Une lignée déduite
  de la clé ne contrôle rien de plus que la clé.
- **Correction** (conv-audit tranche, la spécification l'écrit) : (a) `releve.course` tiré de la clé de la ligne
  « - course : … », exigée égale à celle des lignes « préenregistrement » et « organisme », traduite par une table close de
  deux lignes citée des textes du pilote (ou la clé elle-même, et la clé au tableau du § 9) ; (b) `identite.lignee` : une
  source observée hors de l'archive (extrait ou manifeste, à confirmer sur les pièces des séries v13 et v14), sinon
  déduite de la clé en le disant (contrôle non indépendant), ou retirée des champs exigés ; (c) ajouter au § 8 :
  confirmer que chaque ligne qui porte un champ exigé est écrite en simulation (la ligne « préenregistrement », v10
  l. 512 et v11 l. 529, est écrite dans un bloc dont la condition n'est pas dans l'extrait).

### CLB4-02 — à corriger avant usage (avant toute lecture finale et avant de forger un dossier d'audit de lecture finale) — Le libellé (iii) attendu n'est pas celui du script v3 ; lu à la lettre, un rejet passe pour un non-rejet

- **Où** : briefs l. 347–349 ; registre l. 141, 581–583 et 586–587 (HC-P4-11 ; HC-P4-12 y renvoie, l. 609) ; contre le
  brief du script, § 3, point 2 (l. 40–41).
- **Ce qui ne va pas** : l'analyste de la lecture finale recopie « par son libellé » « changement au-delà du bruit des
  tâches » ou « non rejetée (bruit) » ; le script v3 écrira « rejeté au niveau 0,05, famille de quatre » ou « non
  rejeté ». Le registre définit le non-rejet par « le libellé de la cellule n'est pas « changement au-delà du bruit des
  tâches » » (l. 581) : avec le script v3, c'est vrai de toute cellule, rejetée ou non. L'erreur ne va que dans un sens,
  vers « non rejetée », ce que R4 interdit ; un analyste qui s'en tient aux mots peut aussi s'arrêter. Le sens du rejet et
  « aucune tâche sans réponse » concordent (registre l. 579 ; briefs l. 348–351 ; brief du script, point 4).
- **Correction** : écrire la correspondance, libellé du script cité mot pour mot : « rejeté au niveau 0,05, famille de
  quatre » (et celui d'un fichier « holm-deux », que le brief du script ne fixe pas) → verdict « changement au-delà du
  bruit des tâches » ; « non rejeté » → « non rejetée (bruit) » ; réécrire la l. 581 sur le libellé du script. Ou faire
  écrire au script les mots du point 4 bis. L'un ou l'autre avant la forge des dossiers d'audit de lecture finale
  (protocole, § 12.1).

### CLB4-03 — mineur — Fichier « holm-quatre » et ligne d'état : les mots de D1, pas ceux du brief du script v3

- **Où** : registre l. 74–75 ; protocole l. 92, 146, 489–490, 569 ; briefs l. 344–346 ; LISEZMOI l. 54, 119 ; contre le
  brief du script, § 3, points 1, 2 et 6 ; origine : brief v4 l. 43–45 et 70.
- **Ce qui ne va pas** : (a) la liste de ce qu'un fichier ne porte pas de l'autre course omet « ni borne » et « ni
  signalement » ; (b) rien ne dit qu'il ne porte jamais la valeur p ajustée, le rang du test ni le seuil appliqué (ils
  donnent le rang parmi les quatre tests, donc un fait sur l'autre course), et l'étape 1 de l'analyste final ne les
  cherche pas ; (c) « signalements de test : N » au lieu de « signalements (fichier test) : N ». Sans effet sur un
  verdict : le script refuse ces valeurs avant d'écrire (brief du script, point 3 c), et sa sortie n'est pas affichée.
- **Correction** : aligner les pièces sur le brief du script (ou l'inverse, au choix de conv-audit) ; à l'étape 1 de la
  section 4, ajouter « ni borne, ni signalement de l'autre course ; ni valeur p ajustée, ni rang, ni seuil : sinon,
  arrête-toi ».

### CLB4-04 — mineur — Fin du compteur : un rôle sans brief, et une entrée de journal qui n'est pas bornée à une course

- **Où** : protocole l. 202–203, 221–222, 496, 502–504 ; briefs l. 260–270 (section 3A).
- **Ce qui ne va pas** : (a) le protocole prévoit, à la fin du compteur, un contre-lecteur à l'aveugle par course ; aucun
  brief ne le décrit : la section 3A renvoie aux étapes 1 à 7 de la section 1 (fin de course), pas à la section 4. C'est
  ainsi depuis la v3 des pièces ; je ne l'avais pas relevé. (b) « une entrée finale du journal » et « la transmission à
  Lazar » ne sont pas dites par course ; la règle du § 5 (« une entrée ne cite les verdicts que d'une course ») vise les
  entrées de fin de course et de correction ; D2 dit « nulle part ».
- **Correction** : (a) en section 3A, une phrase pour la lecture finale (dossier de lecture finale, étapes 1 à 6 de la
  section 4, nom du rendu) ; (b) au § 4 et au § 13 : « une entrée finale par course (verdicts de cette course seulement),
  puis une entrée de clôture sans verdict (nombre de tests (iii), compteur des lectures) ; une transmission par course ».

### CLB4-05 — mineur — Des faits mécaniques de la course M restent écrits dans le registre que lisent les agents de la course S

- **Où** : registre l. 19–21 (« conception close après une ronde ; génération 0 faite ; nombre d'appels et coût »),
  inchangé depuis la v3 (l. 16–18) ; protocole l. 94 (l'analyste ne lit jamais « tout ce qui vient de l'autre course ») et
  § 3 (le registre est dans chaque dossier de lecture) ; registre l. 334–337 (D3 : le fait lu de M « renseigne donc aussi
  sur S »).
- **Ce qui ne va pas** : le registre donne ces faits de M à l'analyste, au contre-lecteur, au correcteur et à la partie B
  de la course S, et aux agents de M avant qu'ils lisent (B). Ni score ni verdict ; mais un fait de course que le
  registre dit lui-même renseigner sur S, servi à ceux qui ne doivent rien lire de M.
- **Correction** : à la prochaine version du registre (avant l'étalonnage à blanc, refait à chaque version : protocole,
  § 12.5), garder la déclaration sans les faits : « des faits mécaniques de la course M, aucun score (détail au LISEZMOI
  de la v3, servi à aucun agent) ».

### CLB4-06 — mineur — Spécification (B) v2 : deux précisions

- **Où** : spécification l. 59–61, 164–166, 191, 276–278 ; extrait, v10 l. 870 et v11 l. 887.
- **Ce qui ne va pas** : (a) `unite.g001.question_servie = oui` se déduit d'une réponse archivée ; la valeur pour
  « aucune pièce archivée » n'est pas dite, et cette ligne couvre deux cas (« champ question_ouverte de g001, ou g001 non
  tournée ») : elle ne permet ni `oui` ni `non`. (b) L'artefact 4 établit « jamais ouvert » « par construction : aucun
  motif de nom `reponse-question` dans le script » ; or la spécification fait lire la ligne « - réponse à la question :
  reponse-question-g001.md, sha256 … » par son motif exact : si ce motif porte le nom du fichier, la preuve tombe.
- **Correction** : (a) « aucune pièce archivée » → `absent` ; (b) reconnaître la ligne par son début « - réponse à la
  question : » et l'absence de « aucune pièce archivée », sans le nom du fichier ; ou remplacer la preuve par un relevé
  des accès.

### CLB4-07 — mineur — Petites incohérences

- (a) Registre l. 4, protocole l. 4, briefs l. 4, LISEZMOI l. 26 : « trois messages » ; la pièce des messages en compte
  deux (le premier porte les deux précisions à D5). Le contenu appliqué est juste.
- (b) Protocole l. 453–457 (et champ du journal, l. 239) : le paramètre « famille » prend deux valeurs ; le point 1 a
  trois options, et la (c) (« (a) partout, et (b) en plus sur la ronde 1 ») n'y a pas de place.
- (c) Registre l. 154–156 : encore conditionnel (« si le script écrit encore la phrase (iv) avec « deux objets » ») ; le
  brief du script (point 5) fixe la phrase avec « deux courses » : la citer.
- (d) Précaution pour le contrôle de motifs de G6 (protocole l. 391) : `gemini-organisme-v6-2` est un préfixe de
  `gemini-organisme-v6-2-s`, et la clé `v6-2` de `v6-2-s` ; si lignées ou clés entrent dans les motifs, chercher des mots
  entiers. Les noms de course et de dossier ne se recouvrent pas.

## Ce que j'ai trouvé conforme, en plus des points 1 à 8

- « Aucune fiche de M ne motive de correction » est un fait sur M seule, défini sur la pièce de verdicts de M (registre
  l. 266–273), vérifié par la partie B de M avant que le correcteur de S soit lancé (protocole l. 183–189).
- La ligne de commentaire du manifeste : ignorée par `sha256sum -c --strict` (essayé sur une liste passée par un tube,
  GNU coreutils 9.4, sans fichier écrit).
- La table « v3 → v4 » du LISEZMOI renvoie aux bons endroits, que j'ai retrouvés dans les fichiers.
- Aucun score nulle part ; aucune valeur de course hors du nom du dossier de S (D5).

## Ce que je n'ai pas pu vérifier

- Le script de lecture v3 (en écriture) : qu'il écrive les noms, libellés et ligne d'état de son brief ; le libellé
  d'un fichier « holm-deux ».
- Le script du relevé, sa table de correspondance et ses essais (en écriture) ; la structure réelle de l'extrait
  mécanique et du manifeste (lignée, nom de course).
- Que les lanceurs écrivent en simulation (séries v13 et v14) chaque ligne qui porte un champ exigé ; que ces séries
  portent les empreintes réelles des questions (spécification l. 324–326).
- La carte des facteurs et les zones interdites (en écriture).
- Nom, lignée et question de M au tableau du § 9 : comparés au brief v4 et à mes deux rapports, pas au texte v4 (non
  fourni).
- Les `LANCEMENT.md` réels de M et de S ; le message n° 79 ; R-497 ; N-049 et N-050 ; l'heure exacte de l'envoi du
  point 1 ; les commits `e0a739e` et `07c7407` et la poussée des pièces.

## Écarts déclarés

1. J'ai relu mon rapport v3 à son chemin d'origine (`/var/tmp/contre-lecture-boucle-exterieure-pilote4-v2/`), hors de ce
   dossier, au lieu de sa copie dans `fournis/` (même nom ; la copie est conforme à `1a7873e2…`).
2. Une sortie longue de `diff` a été enregistrée par l'environnement d'outils, non par ma commande, sous
   `/root/.claude/projects/-home-claude/b6fe1a7c-3ed9-5bb1-972e-307cc09379be/tool-results/bq0cpzb78.txt`, hors de ce
   dossier ; je l'ai relue pour finir la comparaison. Elle ne porte que la comparaison des pièces, aucun score.
3. Un essai de `sha256sum -c --strict` sur une liste passée par un tube ; aucun fichier écrit.
4. Rien d'autre écrit que ce rapport et son compagnon ; Python non lancé.

# Vérification des corrections du brouillon 5 de la version 2 du préenregistrement « lecture des sondes de l'étape B bis par lentilles » — v1

- **Vérificateur** : le contre-lecteur du brouillon 4 (rapport `08a698577a952669dd3cd75fa7d7bcb7447a5b1e795106b322bf0e377792c17b`),
  sous-agent de la session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`), modèle **Claude Opus 5.5** (`claude-opus-5-5`) ; le
  rédacteur du brouillon 5 est sur Fable 5.2. Même mandat, même cloisonnement, mêmes interdits que pour la contre-lecture 4
  (`…/mandats/mandat-contre-lecteur-texte-lecture-v2-brouillon4-v1.md`, `85d3c1bb…`), sur l'ordre de la session des lentilles.
- **Heures (UTC, `date -u`)** : 2026-11-20 ; début 00:03:58 ; `git fetch origin main` à 00:04 (tête `1d3fd29a…`, datée
  00:03:16Z ; le rédacteur avait `840c3ecc…`) ; fin relevée au pied.
- **Pièce vérifiée** : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon5.md`,
  `88a2011a8b9e02ba9f6f2933ee4ec01ee6f156abf44ccf19960d9b7de3d75003` (2 775 lignes ; commit `79aec849` ; compagnon vérifié « OK »).

## Pièces lues, empreintes recalculées (égales à l'ordre reçu et aux compagnons)

| pièce | empreinte | lu |
|---|---|---|
| brouillon 5 | `88a2011a8b9e…` | par la sortie des couples (tous les textes changés), puis par passages et recherches |
| brouillon 4 | `fe46a9468b8b…` | par programme |
| mandat du rédacteur du brouillon 5, `…/mandats/mandat-redacteur-texte-lecture-v2-brouillon5-v1.md` | `929cea97827c…` | section « Texte du mandat » seule |
| `couples-brouillon4-vers-brouillon5-v1.py` | `b969a89802dc…` | rejoué ; lu par sa sortie |
| `sortie-couples-brouillon4-vers-brouillon5-v1.txt` | `c9e2656b01e1…` | en entier (rejouée) |
| `diff-brouillon4-vers-brouillon5-v1.txt` | `1c99cd003c15…` | recalculé, égal à l'octet |
| ma contre-lecture 4 | `08a698577a95…` | relue pour les corrections |
| critère d'identité v8 | `541bb86b1508…` | phrases du § 5 par programme (déjà lu à la contre-lecture 4) |
| v1 scellée (`origin/main`) | `ca5066d757df…` | par programme seul |
| `origin/main:registres/go.md`, `registres/decisions.md` | — | GO-2026-11-19-92, R-3994, R-3995 (citations comparées par programme) ; recherche de lignes neuves (voir « Exposition ») |
| validateur `src/controle_ia/prereg.py` | `3b2e3ee56463…` | relancé |

Non lu : le brouillon 5 en entier ; les notes `e0ad5502…` et `f28f18ae…` (relevées par l'index des empreintes ; la première lue
à la contre-lecture 4). Vu sans ouvrir : aucun fichier cloisonné. **Refus d'outil : aucun.**

## Exposition (R4)
- Aucune ligne neuve de V (verdict de la tranche) n'a été ouverte ici : les lignes 29 et 30 avaient été vues à la contre-lecture 4.
- Registres de la branche principale, par recherche des lignes postérieures à R-3995 et des lignes GO-2026-11-19-93 à -98 (coupées à
  200-260 caractères) : noms, états et heures d'autres chaînes (organisme d'idéation, barreau 5, « Raisons ou regard ? » avec un
  compte d'évaluations admises, limite du modèle Fable) ; **les titres de GO-2026-11-19-94, -96 et de R-4008, R-4009 nomment une
  course de conception d'attaques qui « sert le bras d'attaque »** : intitulés seulement, aucun contenu, aucune issue, aucun score.
  Aucune sortie de la chaîne des sondes. Aucun choix de cette vérification n'en dépend.

## Conclusion

**Scellable après corrections** : **une correction bloquante (C1)**, sur la date de l'issue des nœuds N12 et N17 ; six non
bloquantes. Les quatre corrections bloquantes de la contre-lecture 4 (B1 à B4) et les dix non bloquantes (N1 à N10) sont faites,
toutes à la lettre ou mieux. La fabrication est saine : le script rejoué redonne le brouillon 5 **à l'octet** et le `diff` à l'octet.

## Verdict par point

### 1. B1 à B4 et N1 à N10

| objet | verdict | lieux (brouillon 5) |
|---|---|---|
| B1 identifiants de session | **corrigée** | l. 172 (auteur du brouillon 4) ; l. 836-839 (exposition, point 5), dans mes mots |
| B2 couche 15 | **corrigée** | l. 998 et 1000-1002 (réserve (R-c)) ; l. 1051 (bloc séparable) ; table n° 23 ; mots cités de V inchangés |
| B3 phrase du verdict au déclencheur (vi) | **corrigée, et précisée** | E7 l. 250 ; fiche l. 1334-1342 ; phrase de tête l. 1892 ; arrêt l. 2053 ; essais. Une réserve de forme (M2) |
| B4 première passe arrêtée | **corrigée, et étendue** | l. 1478-1482 ; plan 11, l. 1808-1820 ; Critères (« Reproduction … non faite ») ; arrêt l. 2052 ; essais ; Nœuds l. 2594. Deux réserves de lettre (M3, M4) |
| N1 | corrigée | l. 1897 |
| N2 | corrigée, et précisée | l. 1256-1262 ; ligne « Course du réajustement » ; liste d'arrêt ; essais |
| N3 | corrigée | l. 1723 |
| N4 | corrigée | l. 168-170 |
| N5 | corrigée | l. 560-561 |
| N6 | corrigée | l. 1929-1935 ; essais |
| N7 | corrigée | l. 1459 ; N18 l. 2532 et suivantes ; fin des essais ; aucune forme conditionnelle restante (recherche de « en retient », « retient (b) », « retient (c) ») |
| N8 | corrigée | N19 l. 2578 ; table n° 20 ; bloc du brouillon 3, point (a) |
| N9 | corrigée | l. 177-180 |
| N10 | corrigée | l. 1343-1346 ; essai |

### 2. Fabrication — **saine**
`python -I couples-brouillon4-vers-brouillon5-v1.py <brouillon 4> <bloc-notes>/b5.md` : code 0, brouillon 5 égal à l'octet
(`88a2011a…`) ; sortie égale hors la ligne du chemin d'entrée et la ligne « écrit » ; `diff` brouillon 4 → copie égal à l'octet.
43 couples, chaque « avant » unique, aucun chevauchement. Les lieux réécrits dans les blocs, déclarations et nœuds des
brouillons 2 à 4 sont tous listés dans le bloc de tête, avec leur raison ; rien d'autre n'est réécrit.

### 3. Choix du rédacteur au-delà de la lettre

| choix | jugement |
|---|---|
| B4 étendue à toute première passe lancée et non achevée, et à la lentille des logits ; « non calculée » lu comme « jamais lancée » au registre propre | **tenable** : `ENTREES-LENTILLES-BBIS` marque bien l'ouverture des entrées, au départ du calcul de la première passe (v1, plan, point 1 (e)), et `TABLES-LENTILLES-BBIS` sa fin ; la première passe lit les deux lentilles. Deux trous de lettre : la passe « encore en cours » n'a pas de nœud de la v1, et une ligne `TABLES-…` sans `ENTREES-…` n'a pas de règle (M3) ; le « Lien avec la première passe » oublie la lentille des logits dans deux mots (M4) |
| B3 : forme contrôlée de la phrase, ligne d'arrêt | **tenable**, prudent ; le contrôle refuserait aussi deux formes que le critère laisse possibles (M2) |
| N2 : aucune voie par le mot de Lazar pour une fiche muette ; quatrième valeur de la ligne « Course du réajustement » | **tenable** : la phrase « n'ont pas été refaites » pourrait être fausse ; une fiche neuve passe par un nœud |
| N12 et N17 : option lue dans la pièce que nomme `GO-LENTILLES-BBIS-V2`, défaut si muette ; clé conditionnelle `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2` ; arrêt sur une forme inconnue | **à corriger (C1)** : la forme, l'arrêt et la clé sont sains, mais rien ne date l'issue avant le scellement ; or `GO-LENTILLES-BBIS-V2` est inscrite après `SCELLEMENT-LENTILLES-BBIS-V2`, donc alors que `VERDICT-BBIS` est présente, et possiblement après le verdict d'identité : un mot donné alors choisirait une branche de lecture après coup |
| deux phrases « Brouillon 5 » dans « Hypothèse », dont une dans la déclaration du bloc séparable | **tenables** ; la seconde est dans le bloc et dit des faits de V : elle doit aller au lecteur désigné (M1) |
| une phrase ajoutée à l'entrée de contre-lecture 4 | **tenable** ; aucune empreinte entière, le validateur continue de signaler l'entrée |
| mot de départ du rédacteur du brouillon 5 cité d'après sa seule note | **tenable** ; aucune ligne de registre ne le porte sur `origin/main` (`1d3fd29a…`) ; à consigner par la session principale (M6) |

### 4. Marqueurs portés — **citations exactes**
Comparaison par programme, à l'espacement et au gras près, sur `origin/main` (`1d3fd29a…`) : les mots cités de GO-2026-11-19-92
(« nœud N18, option (a). Règle de départage […] signe + avant signe −. ») et de R-3995 (« Aucune ligne n'étend […] ne demande pas
de mot de plus. ») sont dans le registre et dans le brouillon 5. L'heure 22:42:56Z, la relecture à la source (R-3994) et la date
de R-3995 (22:50:15Z) sont justes. Les deux marqueurs sont dits « à confirmer par la session principale ». **Neuf restent**, les
mêmes qu'à la table du brouillon 2, porteurs justes ; aucun marqueur ajouté.

### 5. Nœuds — **conformes**
N12 et N17 restent ouverts, non tranchés, le texte écrit pour chaque option, et pour le défaut de N17 au deuxième palier ce qu'il
demanderait (addendum de recopie écrit après le verdict). N18 est tranché (a), daté ; N19 est clos par R-3995, dit lecture de la
session principale et non mot de Lazar. Aucune ligne de `origin/main` ne tranche N12 ou N17 à cette heure.

### 6. Bloc séparable — **aucune valeur ne bouge ; bornes uniques**
Début l. 1013, fin l. 1062, une fois chacune. Nombres du bloc, brouillon 4 contre brouillon 5 : aucun retiré ; ajoutés seulement
des numéros de couples (16, 17, 19), « B-6 », « § 2 » (dans la phrase L18). Aucune valeur du bloc hors du bloc.
**Couples pour le lecteur désigné** : L16, L17 et L19 couvrent les deux lieux de l'écart qu'il a relevé ; **ils ne suffisent
pas tout à fait** : L18 est dans le bloc et affirme deux faits de V (le lieu, et le libellé « autre ») ; L12 (table n° 23) et L15
redisent le libellé de V hors du bloc. Donner L16 à L19, et L12 et L15 pour information (M1).

### 7. Validateur
`PYTHONPATH=src .venv/bin/python -c "from controle_ia import prereg; print(prereg.problemes('prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon5.md'))"` :
`['contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)', 'marqueurs de gabarit restants : <<CONTRE_LECTURE_4>>, <<CONTRE_LECTURE_ET_SCELLEMENT_DU_CRITERE>>, <<DECISION_DATEE_DE_LA_RETENUE>>, <<DECLARATION_DE_LAZAR_SUR_LE_VERDICT>>, <<DECLARATION_DE_LA_SESSION_DES_LENTILLES>>, <<DECLARATION_DE_LA_SESSION_PRINCIPALE>>, <<DIFFERENCES_DU_BROUILLON_2_A_LA_VERSION>>, <<ETAT_DE_LA_PREMIERE_PASSE_AU_SCELLEMENT>>, <<ETAT_DU_REGISTRE_PROPRE_A_L_ANCRE>>']`
Conforme au pied du brouillon 5 ; aucune section absente ou vide.

### Autres contrôles
- Phrases permises : égales à celles du critère v8 (cinq formes) ; « S seule » égale à sa construction (annexe D de la
  contre-lecture 4, rejouée).
- Lignes de la v1 (annexe B de la contre-lecture 3, rejouée) : `791 0 23 1056`, mêmes 13 réécrites et 10 prolongées, 813 lignes :
  conforme au texte.
- Empreintes des lignes neuves : 6 entières et 14 préfixes, tous trouvés sur la pièce nommée, hors `3a58d008…` et `840c3ecc…`
  (commits, vérifiés : 2026-11-19T22:03:05Z et 23:49:42Z) ; `c12961e1` daté 23:47:48Z.

## Correction bloquante

### C1 — L'issue de N12 et de N17 doit être fixée avant le scellement
- **Lignes 2220-2222** (« Lignes de registre », point (i)). Avant : « **l'issue des nœuds N12 et N17** : le mot de Lazar ou le
  défaut échu, chacun avec sa ligne de `registres/decisions.md`, sur une ligne par nœud, »
  Après : « **l'issue des nœuds N12 et N17** : le mot de Lazar ou le défaut échu, chacun avec sa ligne de `registres/decisions.md`,
  **inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2`** (une issue donnée après le scellement de ce texte est un écart à un
  préenregistrement scellé : version neuve, nœud ; la pièce ne fait que recopier), sur une ligne par nœud, »
- **Ligne 2054** (« Liste d'arrêt »). Avant : « dans une autre forme que celle de « Lignes de registre » (brouillon 5) » Après :
  « dans une autre forme que celle de « Lignes de registre », ou d'après une ligne de `registres/decisions.md` postérieure à
  `SCELLEMENT-LENTILLES-BBIS-V2` (brouillon 5) »
- **Code neuf, essais « options des nœuds N12 et N17 »** : ajouter « ligne d'issue datée après `SCELLEMENT-LENTILLES-BBIS-V2` :
  arrêt (artefact) ; datée avant : lue (cas sain) ».
- Si l'issue est connue au scellement (les défauts tombent vers le 2026-11-21), l'écrire aussi dans « Nœuds », N12 et N17, et dans
  les deux puces de « Entrées » (l. 1278-1280 et la puce « par gabarit »).

## Corrections non bloquantes
- **M1** (l. 154 et l. 2719) : « couples L16, L17 et L19 » → « couples L16 à L19 (L18 est dans le bloc séparable et dit le lieu et
  le libellé de V), et, pour information, L12 et L15 ».
- **M2** (l. 1338-1341 ; arrêt l. 2053 ; essais) : le critère (§ 6) écrit « [31 matrices des moitiés égales sur 31 | série …
  inchangée] » sans dire la forme quand les deux faits tiennent, ni quand les deux séries sont inchangées. Accepter aussi, entre le
  début et la fin, les deux formes jointes par « et », et « séries … inchangées » ; sans quoi un verdict conforme au critère arrête
  la seconde passe (arrêt sûr, mais évitable).
- **M3** (l. 1814 et 2052) : pour une première passe « encore en cours » il n'y a pas de nœud de la v1 ; écrire : « si la
  première passe s'achève ensuite (`TABLES-LENTILLES-BBIS` inscrite), les phrases de la lentille publique et de la lentille des
  logits sont celles de la première passe, la reproduction n'est pas faite, et c'est écrit ». Et ajouter : `TABLES-LENTILLES-BBIS`
  inscrite sans `ENTREES-LENTILLES-BBIS` : arrêt, forme mal comprise.
- **M4** (l. 1480-1482) : « aucune phrase de la lentille publique » et « ses lectures de la lentille publique » → « de la lentille
  publique ni de la lentille des logits » et « ses lectures de ces deux lentilles », comme au plan, point 11.
- **M5** (l. 2207, liste des clés, et plan, point 1 (i), l. 1616) : la description de `GO-LENTILLES-BBIS-V2` dit encore
  « extrait des décisions de Lazar […] sur N11 à N16 » ; ajouter « et la recopie de GO-2026-11-19-92 (N18) et de l'issue de N12 et
  de N17 (« Lignes de registre », brouillon 5) ».
- **M6** (l. 26-29) : le mot « go reco » qui a lancé le rédacteur du brouillon 5 n'a pas de ligne de registre sur `origin/main`
  (`1d3fd29a…`) ; la session principale le consigne, comme pour R-3994, ou le texte le dit mot rapporté.

## Nœuds pour Lazar
Aucun nœud neuf. Pour information au scellement, inchangé : la règle de B4 (aucun remplacement d'une première passe lancée et non
achevée ; aucune phrase de la lentille publique ni des logits avant le nœud de la v1), étendue par le rédacteur à tout arrêt de la
v1 et à la lentille des logits, ce que je tiens pour juste. N12 et N17 restent ouverts ; C1 demande que leur issue soit fixée
avant le scellement.

## Annexe — programmes (bloc-notes de la session des lentilles, dossier `contre-lecteur-brouillon4/`)
- Rejeu du script des couples : `b5/` (copie du script, `b5.md`, `sortie.txt`, `diff.txt`).
- `outils/phrases_v1.py`, `outils/controle_v1_annexe_b.py`, `outils/empreintes_v1.py` (index hors chemins cloisonnés), rejoués sur
  le brouillon 5 ; comparaison des citations de GO-2026-11-19-92 et de R-3995 et des nombres du bloc séparable par programmes
  courts, sans écriture dans le dépôt.

## Refus d'outil
Aucun.

Rien de cloisonné n'a été ouvert : ni la liste « Jamais ouverts » de la v1, ni aucune sortie, score, table, lecture ou verdict de
l'apprentissage des sondes sur la tâche, ni table ou sortie de la lentille publique, ni branche `donnees/*` ou `calcul/*`, ni
`diag/`, `runs/`, `docs/verdicts/`, fichier « consigne-privee » ou « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni
P3, P3-bis, T0.6, T0.7 hors ce texte, l'étape B, le bras d'attaque (hors les intitulés de registre déclarés ci-dessus) ou le
saboteur à budget. Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé ; réseau : `git fetch origin main` seul.

Pied : vérification achevée le 2026-11-20 à 00:09:52 UTC (`date -u`).

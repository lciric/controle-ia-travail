# Contre-lecture de « Avis d'Argon, rapporté à la grille de lecture de G0 — annexe non opposable — v1 » — v1

**Verdict : à corriger.** Les corrections sont toutes de fait (citation fausse, oubli, interprétation du rédacteur présentée
comme fait) ; la version 2 de la note est écrite par moi, contre-lecteur
(`docs/notes/quatre-lectures-inventaire-v1/avis-argon-g0-v2.md`, scellée). La version 1 n'est pas touchée.

- **Contre-lecteur** : sous-agent neuf (règle R2, contre-lecture par un lecteur qui n'a pas écrit la note), modèle Claude
  Opus 5.5, lancé par la session mère pour les quatre lectures sans dépense de l'inventaire (autonomie GO-2026-11-18-05 ;
  « go » de Lazar, R-3168, R-3170). Je n'ai écrit ni la note, ni la grille de lecture de G0, ni ses contre-lectures, ni la
  lecture d'Argon du 31 octobre, ni les questions servies à Argon. Heure relevée par `date -u` en cours de lecture :
  2026-11-18 05:10:47 UTC.
- **Aucune dépense, aucun appel de modèle externe, aucune clé lue ni affichée, aucun commit, aucune poussée.**
- **Pièce contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/avis-argon-g0-v1.md`,
  `833d0a457ec4da1e89ef12579b87346783dffa75010dfe5df1f756300c5c6e4d` (recalculée, égale au compagnon).

## Sources rouvertes

Toutes sur la branche de travail `claude/serene-keller-dasy50` (= `main`) ; HEAD `97da9246` ; `git diff --stat 2005f3ae HEAD`
sur les fichiers ci-dessous : vide (ils sont identiques au commit `2005f3ae` cité par la note). Empreintes recalculées par
`sha256sum`.

| pièce | chemin | sha256 |
|---|---|---|
| lecture neuve des trois réponses d'Argon (Claude Fable 5.1, 31 octobre 18:35 UTC ; « la lecture d'Argon ») | `docs/notes/argon-seul-v1/lecture-argon-questions-ouvertes-abc-v1.md` | `be2b3c4dca49ede519fcaf9eefcb18f2d31a753519e27b1437cc4c7dcd72448f` (égale au compagnon) |
| grille de lecture de G0, brouillon v8 | `prereg/brouillon-G0-grille-lecture-v8.md` | `0c2ea83c7dc1612649f457d99c71e047fd919021b78b16c889cb42eec6658a3e` (égale au compagnon) |
| grille de lecture de G0, brouillon v7 | `prereg/brouillon-G0-grille-lecture-v7.md` | `911d79e6d2095aba8582253dbbfb984193c5f5cdac28047d3021025240f3e2cd` (égale au compagnon) |
| brief v2 | `docs/brief-claude-code-programme-complet-v2.md` | `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` |
| programme v2 | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| décisions N-063 v2, N-062, N-066, N-068 | `docs/decisions/decision-N-063-v2.md`, `-N-062-v1.md`, `-N-066-v1.md`, `-N-068-v1.md` | `b2d9f035…`, `63f42690…`, `21e83ed5…`, `ba6b2db3…` (égales à celles de la note) |
| inventaire | `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` | `b49dc2462382206d7e90eb35cac831a292f286af817399f65286a46898fd5fd0` |
| registre des décisions (vivant) | `registres/decisions.md` | `45baf1d062ece340037da586e615ab5b09f219429d4b834bc1f77358b1e16f9d` à 05:10 UTC (la note : `84f01eec…` à 04:23 ; les lignes citées sont inchangées) |
| registre des GO (vivant) | `registres/go.md` | `dd4526c43c7ba9e76abfb55e4478b7a2b6f857272ba140b1bf9602f230a6c8c8` (égale à celle de la note) |
| **pièces non citées par la note** : passations du 31 octobre 13:16 et 18:10 ; état vivant | `registres/passations/2026-10-31-1316.md`, `registres/passations/2026-10-31-1810.md`, `registres/etat.md` | `0fcf247c…` et `3a1eac6e…` (égales aux compagnons) ; `2db3210d…` à 05:10 UTC |

**Extrait des branches de données** : seuls les noms de dossiers de premier niveau ont été listés ; aucun ne porte le
dossier d'Argon (`find -iname '*argon*'` vide). Il n'a pas servi. Aucune branche ouverte, aucun `git fetch`.

## Ce que je n'ai pas lu (cloisonnement)

Dans la lecture d'Argon, je n'ai pas lu les passages que la note exclut comme relevant de la famille 2 (évasion des
moniteurs et bras d'attaque). Pour contrôler le découpage, j'ai seulement : mesuré leurs tailles (`sed -n | wc -c`) ; lu la
première colonne (les 70 premiers caractères) des lignes 190 à 251 pour savoir quelles lignes de la question C portent sur
la recombinaison bisociative et lesquelles sur l'arène ; lu en entier les lignes 1 à 30, 34, 36 à 40, 134 à 189, 197, 223,
252 à 259, 261 et 265 à 268. Rien de la famille 2 n'est résumé ici. Aucune pièce de la famille 1 (conception d'organismes
saboteurs discrets) n'a été rencontrée. Rien sous `diag/`, aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis
ni du premier test boîte blanche bis.

| passage | lignes | taille mesurée | statut |
|---|---|---|---|
| point préalable, question A | 31-33 | 867 octets | exclue : famille 2 (taille conforme à la note) |
| point préalable, question C | 35 | 393 octets | exclue : famille 2 (conforme) |
| section 1, question A | 41-131 | 17 261 octets | exclue : famille 2 (conforme) |
| inexactitudes A | 99-109 | 2 291 octets | exclue : famille 2 (conforme ; sept lignes non vides, 103 à 109) |
| section 3, arène et malléabilité | 205-213 | 2 700 octets | exclue : famille 2 (conforme) |
| section 3, liaisons et pièce 5 | 215-217 | 631 octets | exclue : famille 2 (conforme) |
| section 3, inexactitudes C | 224-228 | 1 328 octets | n° 2, 3, 4, 6 exclus : famille 2 ; n° 5 (l. 227) hors G0, non lu (conforme) |
| section 3, options manquantes et points non traités | 231-248 | 2 271 octets | exclue : famille 2 en partie, le reste hors G0 (conforme) |
| section 5, points 1, 3, 4, 5 | 258-266 (l. 260, 262-264) | 2 363 octets | exclue : famille 2 selon la note ; non lus par moi |

**Remarque sur le découpage** (sans effet) : l'exclusion de la « note sur la pièce 5 » (l. 217) et des points 3 à 5 de la
section 5 est un classement du rédacteur, par prudence ; l'inventaire (l. 149) ne nomme ni cette pièce ni ces points. Une
exclusion par excès ne fait courir aucun risque de cloisonnement ; je ne l'ai pas vérifiée plus avant, pour ne pas lire ces
lignes.

## 1. Citations rouvertes (contrôle 1)

Trente-deux citations rouvertes (plus que les quinze demandées ; toutes les citations de la lecture d'Argon et de la grille
v8 qui portent un fait de la note, puis un tirage dans les autres). Résultat : vingt-sept exactes quant à leur texte (dont
deux, n° 7 et 16, dont l'usage est corrigé), cinq fautives ou incomplètes (n° 5, 11, 14, 21, 26).

| n° | citation de la note | rouverte | constat |
|---|---|---|---|
| 1 | lecture d'Argon l. 140 (D-G0-1) | l. 140 | exacte |
| 2 | l. 141 (D-G0-2, « marquées SUPPOSÉ par Argon ») | l. 141 et l. 256 (« Les marqueurs SUPPOSÉ […] sont posés par Argon sur les conditions (a)-(d) de D-G0-2 ») | exacte |
| 3 | l. 142 (D-G0-3, 50 % et 95 %) | l. 142 | exacte |
| 4 | l. 143 (D-G0-4) | l. 143 | exacte |
| 5 | l. 144 (D-G0-5, « sans objet pour une tâche ») | l. 144 : « propriété invariante ou sans objet pour une tâche » | incomplète : « invariante » omis (mineur) |
| 6 | l. 147 et l. 164 (D-G0-8, B 1) | l. 147, 164 | exactes |
| 7 | l. 153 et l. 175 (D-G0-14, parade) | l. 153, 175 | exactes quant au texte ; voir correction 6 sur l'usage qui en est fait |
| 8 | l. 154 et l. 176 (D-G0-15) | l. 154, 176 ; grille v8 l. 1176-1183, 1401 | exactes |
| 9 | l. 156, 177 (blocs, priorités) | l. 156, 177 | exactes |
| 10 | l. 158 (effet des constats CL6) | l. 158 | exacte |
| 11 | l. 181-186 (« Ce qu'Argon n'a pas traité ») | l. 181-186 | incomplète : l. 183 et l. 185 non rapportées (correction 7) |
| 12 | l. 197 et l. 223 (confusion de nom, C 1) | l. 197, 223 | exactes |
| 13 | l. 254-256 (bilan, 18 inexactitudes) | l. 254-256 | exacte (A 7, B 5, C 6) |
| 14 | l. 261 (tendance la plus sévère) | l. 261 | exacte, mais la seconde moitié (DIV-2 ; « cohérente avec la Métrique servie ») n'est pas rapportée (correction 7) |
| 15 | l. 34, 37 (recommandations restées visibles) | l. 34, 37 | exactes ; la correspondance G0-1 = DIV-4, G0-2 = D-G0-15 / DIV-3, G0-5 = D-G0-8 / DIV-2 se vérifie en grille v8 l. 1393-1395, 1445-1447 |
| 16 | lecture l. 5 (18:35 UTC) et grille v8, dernière ligne (12:23:44 UTC) | l. 5 ; v8 l. 1857 | exactes ; la conséquence tirée ne suit pas (correction 1) |
| 17 | R-914, `registres/decisions.md` l. 1143 (13 058 mots, D-G0-1 à 15, DIV-1 à 3, CL6-01 à 08) | l. 1143 | exacte |
| 18 | R-933, l. 1162 | l. 1162 | exacte |
| 19 | R-2680, l. 2640 (« grille […] ignore N-063 v2 et P3-bis ») | l. 2640 | exacte |
| 20 | GO-2026-11-18-01, `registres/go.md` l. 365 | l. 365 | exacte |
| 21 | inventaire l. 149, rangé sous « section B » dans la table des sources | l. 149 est dans la section C (« Familles exclues », l. 145) | **fausse** (correction 4) ; la citation entre guillemets de la l. 149 (note, l. 59-60) est de plus un resserrement sans marque de coupe |
| 22 | inventaire l. 78, 135, 163 | l. 78, 135, 163 | exactes |
| 23 | grille v8 l. 339-345 (artefact `arret.json`, D-G0-14 (f)) | l. 339-345 | exacte |
| 24 | grille v8 l. 479-481 (grille non scellable sans mot sur D-G0-1) | l. 479-481 | exacte |
| 25 | grille v8 l. 693-698 (garde d'équivalence sous le critère 1) | l. 693-698 | exacte |
| 26 | grille v8 l. 961 (F-7.2 « étiqueté [EXISTANT] sur le brief T0.9 ») | l. 961 : F-7.2 porte la source « (CLG2-06) », sans étiquette ; [EXISTANT, brief T0.9] est sur F-7.1 (l. 960) ; le mot vient du livrable du brief (grille l. 948-949 ; brief l. 188) | **fausse** sur l'étiquette (correction 5) |
| 27 | grille v8 l. 1169-1171 (trois causes : « nœud pour Lazar ») | l. 1169-1171 | exacte |
| 28 | grille v8 annexe B, l. 1364-1368, 1372-1386, 1392, 1399-1403, 1427 | mêmes lignes | exactes |
| 29 | grille v8 annexe C point 1, l. 1462-1473 ; annexe D l. 1531-1537 | mêmes lignes | exactes |
| 30 | N-063 v2 (filtre par dose ; « sans objet à cette course » ; « date de G0 (fin novembre, N-027) ») | points 1 et 2 ; « Ce qui ne change pas » | exacte |
| 31 | N-066 point 1 ; N-062 point 4 (« préenregistrement court ») ; N-068 l. 70 | mêmes passages | exactes |
| 32 | brief v2 l. 190-201 ; programme v2 l. 180 | mêmes lignes | exactes |

## 2. Avis, état de l'art, zones vierges (contrôle 2)

- Les avis d'Argon sont presque partout attribués (« avis d'Argon », « selon la lecture d'Argon », numéro de ligne), et le
  second degré (Argon connu seulement par Fable 5.1) est dit en tête et en réserve. Bon.
- **Un avis présenté comme fait** : l'inexactitude « N2 » (note § 3 ; table du § 2, ligne D-G0-14 ; question 10) affirme
  que la parade d'Argon « ferait geler sur les arrêts d'instrument ». Cela suppose que l'« artefact d'arrêt du run »
  d'Argon (lecture l. 153, 175) est le fichier `diag/<run>/arret.json` de la garde d'instrument. Ni la lecture d'Argon ni la
  note n'établissent cette identification ; l'artefact peut aussi désigner celui d'une liste d'arrêt sur résultat. C'est
  une interprétation du rédacteur, à écrire comme une question conditionnelle, pas comme une inexactitude d'Argon
  (correction 6).
- **Non-indépendance sur D-G0-15** : la note la rapporte en propre (§ 1) ; c'est un avis de Fable (lecture l. 37). Le fait
  vérifiable qui la nuance manque : la recommandation restée visible pour ce point est celle du mémo G0-2 (a), « Cesser »
  (suspension jusqu'au mot de Lazar ; grille v8 l. 1446), que la table v7 a retirée (l. 1401), alors qu'Argon choisit la
  variante D:1 (a) de la table v7 (coupure et second lecteur borné ; lecture l. 154). L'accord d'Argon avec la
  recommandation visible n'est donc pas littéral (correction 8).
- **État de l'art (règle R7)** : aucun chiffre de l'état de l'art n'est rapporté. « Elle est publiée (MIRAGE) » est une
  citation de N-068, sans chiffre, attribuée. Conforme.
- **Zones vierges (règle R8)** : aucune n'est revendiquée. Conforme.

## 3. Cloisonnement (contrôle 3)

Conforme. Les passages exclus sont désignés par chemin, lignes et taille ; les étiquettes (« course 2 et pré-pilote »,
« arène P-041 », « divergences (a) à (f) », « malléabilité », « pièce 5 ») sont des noms d'objets, sans contenu. Aucun
résultat sous embargo n'est cité. Les lignes de la recombinaison bisociative reprises (l. 197, 223) ne relèvent d'aucune
famille exclue (l'inventaire range les questions 6 et 7 parmi les produits utiles, l. 139). Les identifiants de la
question A et de l'arène qui figurent dans les lignes 37 et 266 de la lecture d'Argon ne sont pas repris par la note.

## 4. Oublis (contrôle 4)

- **Contre-lecture CL7 de la grille v8 signalée faite par conv-audit** : la passation du 31 octobre 18:10
  (`registres/passations/2026-10-31-1810.md`, l. 162 : « CL7 de la grille G0 v8 (nœuds N-1 à N-4 pour Lazar, dont la date
  de G0 ») et l'état vivant (`registres/etat.md`, l. 175 : « nœuds CL7 de conv-audit (date de G0, D-G0-14, D-G0-16,
  D-G0-1) ») attestent une CL7 de la v8, hors de `main`, par une autre lignée que celle de la v8 (R-908, l. 1137 : « CL7 à
  confier à une autre lignée (conv-audit) »). La note dit « aucune contre-lecture CL7 de la v8 » (§ 4), « faire CL7 »
  (question 15), et que D-G0-16 n'a été vu « à aucun autre modèle hors de la lignée qui les a écrits » (question 14) : ces
  trois énoncés sont à corriger (correction 3). Je n'ai pas lu cette CL7 (branche `canal/*`, interdite).
- **Date des réponses d'Argon** : la passation du 31 octobre 13:16 (`registres/passations/2026-10-31-1316.md`, l. 60-63)
  range les trois réponses d'Argon dans le « Terminé » depuis la passation de 10:20, « non encore lues ni synthétisées ».
  Les réponses ont donc été produites entre 10:20 et 13:16 UTC, peut-être avant la fin de la v8 (12:23:44). La note conclut
  « la v8 n'a donc pas pu tenir compte d'Argon » de la date de la **lecture** de Fable (18:35), qui n'est pas celle de la
  réponse (correction 1). La conclusion pratique tient par une autre voie : les réponses n'étaient pas lues à 13:16, et la
  v8 ne nomme pas Argon.
- **DIV-4** : la note écrit qu'Argon n'a pas vu DIV-4 (§ 1, l. 88), puis que la recommandation sur « ce que la grille nomme
  DIV-4 » lui était visible (l. 92-94). DIV-4 existe dans la v7 (l. 1225, « consigné pour mémoire ») ; le dossier ne la
  nommait pas (R-914 : DIV-1 à 3) mais en servait l'objet, le passage G0-1 du mémo, recommandation comprise (lecture
  l. 34) (correction 2).
- **Lecture d'Argon, lignes non rapportées** (correction 7) :
  - l. 174-176 : selon Fable, les « options nouvelles » d'Argon sur D-G0-1 et D-G0-14 (f) **reprennent** les corrections
    CL6-01 (i)-(iv) et CL6-02, servies dans le dossier, et celle de D-G0-15 reprend la variante D:1 (a) de la table v7 ;
    la note les dit « traitées » par la v8 sans dire que l'accord tient à une source commune (CL6), non à une confirmation
    indépendante ;
  - l. 185 : Argon ne dit pas que ses choix sur D-G0-1 et D-G0-9 règlent aussi les choix 3 et 7 de la synthèse du repli ;
    or la v8 met les onze choix du repli à l'ordre du jour avec les D-G0 (annexe C point 1, l. 1463-1464) ;
  - l. 183 : un passage tronqué de CL6-01 dans le dossier servi n'est pas signalé par Argon (fait sur l'objet servi) ;
  - l. 162 et 170 : vingt renvois recoupés en B, aucune erreur de chiffre, « les écarts sont des élargissements de
    portée » ; l. 256 : « Aucune pièce inventée » (le pendant favorable, règle R4 de symétrie) ;
  - l. 261, seconde moitié : sur DIV-2 Argon choisit la forme de la table contre la grille ; lecture « cohérente avec la
    Métrique servie mais contraire au défaut de la grille » ;
  - l. 23 et 26 : métadonnées de la réponse B (modèle demandé et servi : `gemini-4-argon` ; 0,6076 USD ; environ 4 840 mots
    pour 5 000 demandés ; aucune trace de réflexion comptée) : elles identifient l'espèce qui a répondu.
- **Inexactitude N4** : le 50 % non marqué SUPPOSÉ est une inférence (l. 256 énumère où Argon a posé ses marqueurs ; 50 %
  n'y est pas), à dire comme telle (mineur, inclus dans la correction 7).

## 5. Corrections (liste exacte)

1. § 1, « Chronologie » : remplacer la déduction tirée de 18:35 par la date de production des réponses (entre 10:20 et
   13:16 UTC, passation 2026-10-31-1316 l. 60-63), et fonder « la v8 n'en tient pas compte » sur : réponses non lues à
   13:16, lecture de Fable à 18:35, aucune mention d'Argon dans la v8.
2. § 1, « Objet servi » : « ni DIV-4 » devient « DIV-4 non nommée (son objet, le passage G0-1 du mémo, servi avec sa
   recommandation) ; DIV-4 existe déjà dans la v7, l. 1225 ».
3. § 4, dernier point ; questions 14 et 15 ; sommaire : une CL7 de la v8 par conv-audit est attestée hors de `main`
   (passation 2026-10-31-1810 l. 162 ; `registres/etat.md` l. 175 ; R-908) avec quatre nœuds (date de G0, D-G0-14, D-G0-16,
   D-G0-1) ; elle n'est pas versée sur `main` ; question 15 : la verser, non la faire ; question 14 : D-G0-16 a été vu par
   cette CL7.
4. Table des sources : inventaire l. 149 relève de la section C, non B ; la citation de la l. 149 est donnée avec marques
   de coupe.
5. § 4 (N-068) et question 7 : F-7.2 porte la source « CLG2-06 », non l'étiquette [EXISTANT] ; son mot vient du livrable
   du brief T0.9 (grille l. 948-949 ; brief l. 188).
6. § 3, N2 ; table du § 2 (D-G0-14) ; question 10 : la parade d'Argon n'est contraire à D-G0-14 (f) que **si**
   « l'artefact d'arrêt » est `diag/<run>/arret.json` ; écrit comme question, non comme inexactitude d'Argon.
7. Ajouts tirés de la lecture d'Argon : l. 174-176 (reprises de CL6), l. 185 (choix 3 et 7 du repli), l. 183, l. 162 et
   170, l. 256 (« aucune pièce inventée » ; 50 % inféré), l. 261 seconde moitié, l. 23 et 26 (métadonnées), l. 144
   (« invariante »).
8. § 1, « Indépendance limitée » : la non-indépendance sur D-G0-15 est un avis de Fable ; la recommandation visible était
   le mémo G0-2 (a) « Cesser », retirée par la table v7, Argon choisit la variante D:1 (a) bornée (grille v8 l. 1401, 1446 ;
   lecture l. 154).

Rien n'est à refaire : la structure, le cloisonnement, la table point par point et les dix-sept questions tiennent ; aucune
correction ne touche un critère de G0.

Fin de la contre-lecture.

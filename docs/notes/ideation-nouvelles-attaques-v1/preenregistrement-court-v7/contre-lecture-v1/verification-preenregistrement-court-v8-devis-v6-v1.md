# Vérification — préenregistrement court v8 et devis v6 de la course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O : le même que pour la contre-lecture de la v7 et du devis v5 (`acb02c44…`). Je n'ai écrit ni la v8, ni le devis v6, ni le calcul v5. Règle R2. Écrit le 2026-11-20 ; relevé de `date -u` : 13:14:59Z, avant l'écriture.
- Processeur seul. Aucun appel, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. Un `git fetch origin main` ; `origin/main` est à `184008f338e05ca638622524e460933244fcbc47`. **Aucun refus de permission, de classifieur ni de garde.**
- Ce rapport ne contient aucune recette, aucun nom ni énoncé de mode, aucun identifiant de modèle.

## Verdict

**Devis v6 et calcul v5 : conformes.**

**Préenregistrement v8 : à corriger**, par cinq corrections de lettre (V1 à V5), plus le traitement de la contre-lecture 5, que la mère écrit. Aucune correction ne touche un total, un seuil, un arrêt ni une décision.

## 1. Empreintes et rejeux

- **Empreintes :** toutes les pièces versées sont égales à leur compagnon. Ce sont la v8 (`4970d531…`), le devis v6 (`d825cb31…`), le calcul v5 (`cdec1d2d…`) et sa sortie (`2a0d2a58…`), les deux jeux JSON (`6e20f2c9…`, `b0602c73…`), les deux journaux, les deux différentiels (`576f51be…`, `9994d4c5…`), la sortie du validateur et le rapport du rédacteur (`d4421164…`).
- **Outil (`391db990…`) :**
  - sur la v7 (`1837a685…`) : « FAIT : 36 », sortie `4970d531…`, `cmp` égal ;
  - sur le devis v5 (`41a09f77…`) : « FAIT : 29 », sortie `d825cb31…`, `cmp` égal.
- **Calcul v5 :** joué deux fois, sorties égales entre elles et à `2a0d2a58…`. Chaque chiffre que j'avais refait pour 0,05 USD (§ 4 de ma contre-lecture, champ `confrontation_sonde_0_05` de ma sortie `e9790b19…`) s'y retrouve au centime, manques exacts compris :

| | valeurs |
|---|---|
| plafond total ; total au cas haut | 576,05 ; 548,70 |
| écart du plafond total à cinq espèces | +120,05 |
| sortie de la sonde (un jeton par octet ; 2,5 octets par jeton) | 4 359 ; 4 743 |
| espèce 6, besoin bas / haut / pire | 35,24 / 88,60 / 199,70 |
| espèce 6, manques | 3,00 / 56,35 / 167,46 |
| avec le collisionneur, bas | 9,58 |
| Rigaud au cas haut, lots à 45 | 15,76 et 32,47 |
| troisième relais au cas haut | 5,51 et 8,11 |
| variante à 450, plafond total | 456,05 |

- **Repère neuf :** 0,9756 USD par appel, soit 90 466 jetons. Il est juste : (32,24463 − 0,05) / 33.
- **Validateur sur la v8 :** « aucun ». Ce « aucun » ne voit pas que la contre-lecture 5 n'a ni empreinte ni traitement (V4 et § 4).

## 2. Ce qui est porté

- **K'1, K'6, K'7, K'9, K'10, K'11 :** mot pour mot de mon jeu (`c73ad347…`), vérifié par programme.
- **K'2 :** mot pour mot, plus une ligne pour R-4266. Son empreinte de registre est juste : `decisions.md` au commit `6085c291` vaut `d765bb74…`.
- **K'3, K'4 :** adaptés pour nommer le devis v6, son calcul v5, leurs chemins et leurs empreintes. C'est ce que K'3 prévoyait si le devis était récrit ; les empreintes sont justes.
- **K'5, fondu dans une récriture de la clause (d) :** juste. « Devis v3 » et « devis v5 » renvoient au devis v6, qui garde les sections et la ligne de course et porte le plafond total de 576,05 USD. Les mentions « devis v5 » qui restent dans les phrases de version et dans la table sont des renvois d'histoire, non des lectures.
- **K'8, K'12 :** mot pour mot de mon jeu, mais devenus faux depuis R-4266 (§ 3, V1 et V2).
- **Ma « Contre-lecture 5 » :** portée mot pour mot. Son rapport est cité par son nom seul, sans chemin ni empreinte, et le traitement manque (V4 et § 4).
- **Passe R-4265 :** portée aux treize lieux de mon § 4 : prédiction ; deux lignes de la table des seuils ; « ce qui change à six espèces » ; deux valeurs ouvertes ; trois tirets de la sonde ; la table « un par un » ; l'arrêt n° 2 ; les points 10 et 11 de « ce qui reste ». Aucun autre chiffre n'est touché.
- **Les cinq précisions de la mère, toutes portées :**
  - liste des motifs écrite contre le gabarit servi et la synthèse servie, à l'arrêt n° 16 et à la valeur ouverte ;
  - liste jouée sur les témoins plantés ;
  - identifiant neutre à l'additif ;
  - clé et relais de l'espèce 6 vérifiés par la mère, par le nom, au complément ;
  - reste net cité « sur `main` » : vrai, le fichier y est à `184008f3`, empreinte `62c625ab…`.
  - Deux défauts : la phrase de version (4) n'en compte que trois (V5), et la ligne de case dit la clé de tirage « déjà écrite », ce qui est faux (V3).

## 3. Les écarts déclarés du rapport

Le rapport en déclare six, non sept.

1. **K'3 à K'5 adaptés :** juste (§ 2).
2. **Ligne R-4266 ; K'8 et K'12 disent « écrit et scelle » :** à corriger. R-4266 dit les deux errata 1 versés sur `main` (classe C) : celui de la question à son § 7 seul, celui de l'ordre de course à son § 10, étape 6. K'8 renvoyait en outre à « l'erratum d'une ligne » du rapport du rédacteur comme au texte attendu. L'erratum versé n'en est pas un : il ne porte que la revue externe. V1 récrit le paragraphe sur ces faits ; V2 le point 15.
3. **Chemin du devis v6 dans `NA/preenregistrement-court-v7/` :** juste ; le fichier y est, à son empreinte.
4. **Mot sur l'épreuve 4 :** `go.md` à `184008f3` n'a aucune ligne après GO-2026-11-20-52. Les deux branches restent ouvertes, à juste titre.
5. **Paragraphe « La sonde de refus de l'espèce 6 (v3) » du devis, resté à 0,01 USD :** sans suite. Le devis garde ses couches datées (« ce que la v3 ajoute est marqué v3 »), et le titre du paragraphe dit en clair que le plafond est de 0,05 USD depuis la v6 et que le paragraphe « recalculées » prime. Ce paragraphe, la table des sondes, le § 0, le § 6, le § 9 et « tu accordes aussi » portent tous 0,05. Les anciens chiffres ne restent que dans les phrases de version, la ligne S10 des sources et des mentions marquées « jusqu'à la v5 », qui sont de l'histoire.
6. **Compte des ancres par l'outil :** sans suite.

## 4. Corrections, à texte exact, sur la v8 (`4970d531…`)

Chaque « Ancien » est compté une fois par `grep -c -F -e`. Les cinq remplacements sont dans `corrections-preenregistrement-court-v8-v1.json`, à côté de ce rapport. Passés à l'outil sur une copie : « FAIT : 5 remplacement(s) », sortie `ebff3122dd1c1277914580e0fca5a92dd5546443bc6fa56279bf59bc08cc6e43`, validateur « aucun ».

- **V1** (lecture de l'ordre de course). Ancien : « Il se lit avec un erratum d'une ligne, que la mère écrit et scelle ; le texte exact que cet erratum doit porter est au § 5 du rapport du rédacteur de la v7 (`NA/preenregistrement-court-v7/rapport-redacteur-preenregistrement-court-v7-devis-v5-v1.md`, `f1751793f9b48b8258d66292adbf6239d8159b4ff281d0782697bca9cc6981c1`) ; là où ce texte écrit « préenregistrement court v7 », l'erratum nomme la version de ce préenregistrement que la mère scelle. La question v5 se lit de même avec son erratum 1 (§ 3 et § 7), décidé par la mère (R-4265) pour remplacer « après la revue de sécurité externe » ; ces passages ne sont pas servis, et d'ici cet erratum ce texte prime sur eux pour la mesure interne (section « Critères de lecture gelés », paragraphe « Portée »). Avant comme après cet erratum, ce préenregistrement prime là où les deux textes diffèrent. » — Neuf : « Il se lit avec son erratum 1 (§ 10, étape 6), décidé par la mère (R-4265) et versé sur `main` (R-4266, ligne de la table des pièces), qui remplace « après la revue de sécurité externe ». Pour le reste (la question et la synthèse servies, la composition à six espèces, la relecture et la lecture par une session à part, la quarantaine, les garde-fous, les arrêts), cet erratum ne dit rien : ce préenregistrement prime là où les deux textes diffèrent (point (e) ci-dessus). Le texte d'un erratum plus large, d'une ligne, est proposé au § 5 du rapport du rédacteur de la v7 (`NA/preenregistrement-court-v7/rapport-redacteur-preenregistrement-court-v7-devis-v5-v1.md`, `f1751793f9b48b8258d66292adbf6239d8159b4ff281d0782697bca9cc6981c1`) ; il n'est pas versé, et le point (e) en tient lieu. La question v5 se lit de même avec son erratum 1 (§ 7), décidé par la mère (R-4265) et versé sur `main` (R-4266), qui remplace « après la revue de sécurité externe » ; ce passage n'est pas servi, et ce texte prime sur lui pour la mesure interne (section « Critères de lecture gelés », paragraphe « Portée »). »
- **V2** (ce qui reste, point 15). Ancien : « 15. (v7) **L'erratum d'une ligne à l'ordre de course v3** et **l'erratum 1 de la question v5** (§ 3 et § 7 ; R-4265), écrits et scellés par la mère. » — Neuf : « 15. (v7) **L'erratum 1 de l'ordre de course v3** (§ 10, étape 6) et **l'erratum 1 de la question v5** (§ 7) : décidés par la mère (R-4265), versés sur `main` (R-4266) ; fait. »
- **V3** (ligne de case). Ancien : « Il se construit à l'additif, avec sa clé de tirage, déjà écrite à la table des valeurs ouvertes (section « Seuil » : une clé neuve, qui ne change aucun tirage écrit) ; » — Neuf : « Il se construit à l'additif ; si sa construction demande un tirage, c'est une clé de tirage neuve, qui ne change aucun tirage écrit (table des valeurs ouvertes, section « Seuil ») ; »
- **V4** (contre-lecture 5 : chemin et empreinte du rapport). Ancien : « Rapport : `contre-lecture-preenregistrement-court-v7-devis-v5-v1.md`, verdict « À corriger » : K'1 à K'12 » — Neuf : « Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/contre-lecture-v1/contre-lecture-preenregistrement-court-v7-devis-v5-v1.md`, `acb02c441ce1b7285ff09929bbe532dca57adb513ced56efa156b6cdef340a18`, verdict « À corriger » : K'1 à K'12 »
- **V5** (phrase de version, point (4)). Ancien : « (4) Trois précisions de la mère, données pour la v8 : la liste des motifs de la garde s'écrit contre le gabarit servi et la synthèse servie, et se joue sur les témoins plantés (arrêt n° 16) ; l'identifiant neutre se construit à l'additif, avec sa clé de tirage ; la mère vérifie, par le nom, la clé et le relais de l'espèce 6 dans le conteneur de la course, avant la sonde. » — Neuf : « (4) Quatre précisions de la mère, données pour la v8 : la liste des motifs de la garde s'écrit contre le gabarit servi et la synthèse servie, et se joue sur les témoins plantés (arrêt n° 16) ; l'identifiant neutre se construit à l'additif ; la mère vérifie, par le nom, la clé et le relais de l'espèce 6 dans le conteneur de la course, avant la sonde ; le reste net comptable est cité sur `main`, où il est versé. »

**Traitement de la contre-lecture 5, écrit par la mère**, dans la même passe, à la fin de l'entrée (ancre comptée une fois : « calcul du devis refait indépendamment, égal au centime d'arrondi près. »). Lettre proposée, qu'elle reprend ou non :

« Traitement : K'1 à K'12 acceptées, appliquées à texte exact dans la v8 (K'3 à K'5 nomment le devis v6) ; R-4265 portée sur la v8 et le devis v6 ; vérification par le même contre-lecteur : `verification-preenregistrement-court-v8-devis-v6-v1.md` (chemin et empreinte de son versement), verdict « À corriger » ; V1 à V5 appliquées dans la v9. »

Avant le scellement, la mère contrôle sur le texte à sceller : `grep -c -F -e "Traitement : K'1"` doit rendre 1, et le validateur rester à « aucun ». La vérification de la v9 par le même contre-lecteur se fait par `cmp` du rejeu.

## 5. Écarts

1. J'ai déduit les noms des pièces versées de la demande, des journaux et du rapport du rédacteur, sans commande de liste.
2. Trois essais de chemin des errata versés ont échoué (chemins absents) ; j'en suis resté aux lettres de R-4265 et R-4266, sans lire les errata.
3. Mes essais sont dans le sous-dossier `v8/` de mon dossier ; rien n'est écrit ailleurs.

— contre-lecteur neuf, modèle O

# Complément de l'audit de l'écart DT-4 de la course 7a (avant le scellement de T0.6 r4) — v1

> **Limite imposée (inchangée depuis la v1).** Par le brief de Lazar du 9 novembre (21:5x UTC), personne n'ouvre `lecture-sondes-t06.json` ni la branche de quarantaine `donnees/lecture-b-7a-quarantaine-v1` avant le verdict scellé de P3-bis. Ce complément est donc **structurel et par catégories**, comme la v1. Il **ne compare aucune valeur** du fichier des sondes ni de la lecture B au texte de `main`. Ce que cette limite laisse ouvert est écrit à la section « Ce qui reste ouvert ».

## En-tête

- **Qui** : l'auditeur de la v1 (`audit-ecart-dt4-7a-v1.md`, `4882fe4d…`), sous-agent Claude Opus 5.5 de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`. Il reste exclu de T0.6, T0.7, P3-bis et G0.
- **Quand** (`date -u`) : début le 10 novembre 2026 à 00:59:55 UTC ; sortie définitive du script à 01:14:17 UTC ; rapport vers 01:20 UTC.
- **Consignes** :
  - `consigne-complement-audit-ecart-dt4-v1.md`, empreinte `56789718155ab10c92cabb9d82fff0fef16832f4a44facff117a321d187e7e69`, vérifiée avant toute lecture et conforme ;
  - ajout de la mère pendant le travail : étendre la plage jusqu'à `35abfd16` au moins et ajouter la contre-lecture 4 et ses couples.
- **Plage couverte** : `62ba4a4a..35abfd16`, soit 21 commits. **Tête exacte couverte : `35abfd16c675aafcaa998dc41962900ea9dbc20d`** (R-2066, 01:10 UTC). Au lancement, `main` était à `5eaa900d`. Le passage à `5eaa900d` a donné 0 occurrence à classer ; l'extension à `35abfd16` n'a ajouté que la contre-lecture 4 et R-2066.
- **Script** : `verifier_ecart_dt4_v2.py`, version neuve (R12). La v1 (`608aebe6…`) et sa sortie (`7ca2d7b4…`) sont intactes (compagnons vérifiés). Apports de la v2 :
  - `extraire_mesures_epreuve_t06_v1.py`, `integ-t06` et `essai-S` rejoignent les chemins jamais lus ;
  - pour un fichier JSON, la valeur de la chaîne est extraite avant comparaison ;
  - **héritage** : une ligne recopiée d'une pièce déjà auditée en v1 (ligne entière, ou contexte de chaque mot-clé) prend le classement de sa ligne d'origine ; si plusieurs origines existent, la plus grave l'emporte. L'explication des décimaux s'hérite de même ;
  - les tables de classement du complément.

## Verdict (une ligne)

**« Aucune trace trouvée »** du fichier des sondes de 7a ni d'un élément C1 à C7 de la lecture B dans `62ba4a4a..35abfd16` et les 39 pièces nommées (0 occurrence classée (iii) sur 717 ; 0 décimal inexpliqué sur 1 252 lignes). **La réserve « indéterminé » de la v1 demeure** : on ne sait toujours pas d'où viennent les grandeurs de coût de 7a. Leurs copies sont maintenant toutes localisées, et la r4 les retire.

## Constats

1. **Chemins, commits, empreintes.**
   - Les 21 commits forment une plage linéaire, sans fusion. Ils ajoutent 82 fichiers, en modifient 16 et n'en suppriment aucun. **Aucun chemin interdit.**
   - L'arbre de `35abfd16` compte 17 608 noms, dont **aucun motif interdit** : pas de `lecture-sondes*`, pas de `diag/` ni de `runs/` de 7a, pas d'`extraire_mesures_epreuve_t06_v1.py`.
   - Les 14 noms du bras d'attaque (`docs/notes/bras-attaque/`, `registres/index-bras-attaque-v1.md` et une consigne d'entretien) existaient déjà à `6886b61e`. Aucun commit de la plage ne les touche et le script ne les lit jamais.
   - Ni `e6c06113`, ni `1609a4bf`, ni la tête de 7a ne sont ancêtres de `main`. `e6c06113` est absent du clone. Aucun commit de la plage ne commence par `e6c06113`.
   - L'empreinte du fichier des sondes (déclarée à la ligne 16 de la lecture A) ne correspond à aucun des 98 fichiers écrits par la plage.
   - R-2052 à R-2066 ne citent **aucun nom ni aucune empreinte de B**. Les identifiants non résolus sont tous des pièces connues : consignes, configurations, r2, r3 et r4 après couples, candidat 4, extracteur, S′ d'essai, pièces de puissance de T0.6, commit de quarantaine cité. Les messages de commit ne portent ni catégorie ni identifiant.
2. **Catégories.** 717 occurrences : 392 sur les lignes ajoutées par les commits, 312 sur les pièces, 13 sur le différentiel. Par catégorie : C1 307, C2 99, C4 104, C5 68, C6 38, C7 19, X (mention du fichier ou de B) 175. Classement :

   | Classe | Nombre | Détail |
   |---|---|---|
   | (i), description de l'écart ou nom interdit | 197 | dont 81 occurrences des pièces de l'audit v1 lui-même (`I-AUDIT`) |
   | (ii), conception ou texte antérieur | 510 | 266 par antériorité mécanique d'avant 7a, 17 par héritage, 188 de conception de (ii-b) |
   | (ii-A), grandeur tirée de la lecture A | 2 | |
   | (ii-B), grandeur de coût de source non établie | 8 | |
   | **(iii), transfert possible** | **0** | |

3. **Décimaux entre 0 et 1 (contrôle 3 bis).** 1 252 lignes, **0 à examiner**. Explications :
   - 622 lignes de la simulation v1 de (ii-b) et de son rejeu (`D-SIMUL-B`) ; 268 de la simulation v2 (`D-SIMUL`) ;
   - 220 de conception de (ii-b) ;
   - 75 de devis ;
   - 26 de la lecture A ;
   - 11 du plan de puissance de la r2 ;
   - 10 de configuration ;
   - 20 de grandeurs de coût de la classe (ii-B) et de leur arithmétique.

   Chaque total compte les explications directes et celles héritées de la v1.
4. **Différentiel r3 → r4 (point 4 de la consigne).** 48 lignes ajoutées ou remplacées, 13 occurrences : 7 (i), 6 (ii), **0 (iii). Aucun élément C1 à C7 de 7a.**
   - La r4 **retire** les grandeurs de coût (couples W-C1 à W-C5). Elle ne les nomme plus que par catégories, dans sa section « Ce que les auteurs savaient » (l. 357, classe (i)) ; aucune ne figure dans le texte de la r4.
   - La r4 déclare l'écart sans écrire que 7a n'aurait été lue par aucune sonde (l. 359-360). Elle reprend les trois constats de la v1 (l. 362).
5. **Cas connus traités explicitement (point 3).**
   - **Grandeurs de coût de 7a recopiées.** On les trouve seulement :
     - dans l'« ancien » de deux couples de la r4 (`…-r4-couples-v1.json`, l. 41 et 137), qui sont précisément les couples qui les retirent ;
     - dans les blocs « Avant » correspondants du journal de la r4 (l. 90 et 246) ;
     - dans la contre-lecture 3, comme constat de son majeur M1 (l. 28 et 30, avec la vérification de l'arithmétique).

     Ces lignes héritent de la classe (ii-B) de la r3 (l. 349, 616), ou de l'explication `D-COUT7A` de leurs décimaux. Ce sont des grandeurs de coût, pas des valeurs de sonde.
   - **Variante (a)** (`…-couples-variante-a-v1.json`) : elle **ne recopie aucune** de ces grandeurs (0 correspondance). Elle s'applique à la r3, qui les porte. Elle leur donne le statut de Y3 (origine non établie, marqueur `MOT_LAZAR_GRANDEURS_COUT_7A`) et ne contient que des classes (i) et (ii).
   - **Les 20 % d'illisibles du dossier (ii-b).** Le brouillon 1 en fait une hypothèse (conception, l. 95) et un paramètre de la simulation v1 (`U_DECLARE = 0.20`, l. 34). Le journal v1 (l. 60) et la contre-lecture 1 (l. 55, majeur M5) le rattachent aux « 16 à 27 % » de la r3, de la classe (ii-B). La sortie de la simulation v1 et son rejeu en annexe de la contre-lecture 1 (l. 140-243) en dépendent (`D-SIMUL-B`). Le **brouillon 2 le retire** : sa simulation v2 parcourt une plage de 5 à 40 % sans grandeur de 7a, et sa conception (l. 95) déclare la provenance et l'origine indéterminée. Aucune constante de la règle d'acceptation ne s'appuie sur 7a.
6. **Contre-lecture 3** (`…-r3-cl3.md`, `3930d4f9…` ; couples `e3846ae5…`) : 6 occurrences, 4 (i) et 2 (ii), 0 (iii).
   - Sa ligne 63 cite la configuration de la sonde et de son audit : famille, couche, agrégation, seuils. Ce sont les valeurs de la configuration du brouillon 5 (7 novembre, lue à `1609a4bf`) et de la r2 (l. 386), **antérieures à 7a**. Elles sont citées comme configuration, non comme résultat : classe (ii) `II-CONFIG`, vérifiée à la main.
   - Ses grandeurs de coût relèvent du constat 5.
7. **Contre-lecture 4** (`…-r4-cl4.md`, `001352b7…` ; couples `e6ad9c15…`, R-2066) : 2 occurrences (i), des noms interdits. Ses décimaux sont l'arithmétique du plan de puissance de la r2. **Aucun élément C1 à C7.**
8. **Dossier (ii-b)** (20 fichiers, compagnons conformes) : 106 occurrences sur les pièces, 93 (ii), 11 (i), 2 (ii-B) (journal v1, l. 60 ; contre-lecture 1, l. 55), 0 (iii).
   - Ses mots-clés relèvent de sa conception : bornes de la règle d'acceptation et des prix, intervalles, seuils exploratoires de son rédacteur, garde qui refuse toute clé de sonde ou de couche.
   - Son seuil d'aire de la lecture (2) est la règle « mots et coût » de T0.6, recopiée telle quelle de la r3 (texte d'avant 7a).
   - Ses décimaux sont de conception, de simulation et de devis (constat 3).
9. **Rapports d'intégration** (`427def65…`, `4f4eb27d…`) : 4 occurrences, 2 (i) et 2 (ii). Ce sont des noms absents de l'arbre fusionné, des noms de modules du code de T0.7 et des familles de fichiers.
10. **Consignes postérieures à `62ba4a4a`** (7) : aucune valeur ni élément de B.
    - Cinq nomment les quatre interdits attendus.
    - L'additif v2 de l'intégration n'en nomme aucun : il complète la consigne v1, qui les nomme.
    - La consigne du complément nomme le fichier des sondes en clair et nommément, mais pas sous la forme `diag/*/…`. C'est équivalent.
11. **Registre R-2052 à R-2066** : 4 occurrences, 2 (i) et 2 (ii), 0 (iii). R-2057 (verdict de la v1) est de classe (i).
    - R-2065 note que le rédacteur de la r4 a extrait `src/controle_ia` de `1609a4bf` par `git archive`. L'extracteur des mesures est sous `scripts/` et n'est pas concerné.
    - R-2064 consigne un accès mécanique à `docs/notes/bras-attaque/` par `verifier-arbre` (hors du mandat de cet audit). Je n'ai lancé ni `verifier-arbre` ni aucun outil qui hache ce dossier.
12. **Épreuves de la v2 (R5)**, faites sur un dépôt factice dans le bloc-notes :
    - une ligne recopiée dans un champ JSON (mot-clé en début de chaîne) hérite de la classe (ii-B) de son origine ;
    - la même ligne, avec une valeur modifiée, reste « à classer » ;
    - un décimal sans explication à l'origine reste « à examiner » ;
    - `scripts/extraire_mesures_epreuve_t06_v1.py` est compté et jamais lu, et sa lecture directe est refusée avant tout appel à git.

## Réserves

1. **Limite structurelle** (comme en v1) : un contenu transcrit sans aucun mot-clé et sous une autre forme qu'un décimal entre 0 et 1 échapperait au contrôle. Exemples : un rang, un entier, un nom de sonde.
2. **Origine des grandeurs de coût de 7a : toujours indéterminée** (réserve 1 de la v1). Elles sont retirées de la r4 et du brouillon 2 de (ii-b). Elles restent dans la r3 (scellée telle quelle, R12), dans l'« ancien » des couples de retrait, dans la contre-lecture 3 (constat) et dans les pièces du brouillon 1 de (ii-b). Si Lazar choisit l'option (a), elles entreront dans le texte scellé avec ce statut.
3. **Héritage** : les classements hérités reposent sur ceux de la v1, faits par moi seul. Je n'ai contre-lu ni ceux de la v1 ni ceux de ce complément.
4. **Classement par fichier entier.** Je l'ai employé pour les 20 fichiers de (ii-b) et pour les 3 pièces de la v1, après avoir lu chaque contexte. Il ne s'applique qu'aux lignes identiques à la version classée.
5. **Attestations non vérifiables dans le dépôt** :
   - rédacteur et contre-lecteur de (ii-b) ;
   - rédacteur de la r4 ;
   - contre-lecteurs 3 et 4 ;
   - développeur de l'intégration.

## Ce qui reste ouvert

1. **Fusion de S dans `main` (voie B, R-2062).** Elle apportera l'arbre de `1609a4bf`, dont `scripts/extraire_mesures_epreuve_t06_v1.py` et 71 notes. Il faudra rejouer la v2 sur cette fusion avant le scellement effectif. La v2 ne lit jamais l'extracteur, mais son contrôle 1 ne le signale pas comme chemin interdit : l'ajouter à ce contrôle si on veut qu'il soit signalé.
2. **Fermer l'origine des grandeurs de coût** : soit un mot de Lazar (qui sait quel compte rendu la mère sortante a transmis), soit une comparaison mécanique aveugle de la lecture B avec les textes de `main`, qui demande elle aussi un mot de Lazar.
3. **Mot de Lazar `MOT_LAZAR_GRANDEURS_COUT_7A`** : options (a) ou (b) de la r4. L'audit ne tranche pas.
4. **Rejeux futurs** : commande ci-dessous, avec la plage étendue et les pièces neuves en `--piece`. Les classements neufs s'ajoutent par `--classements FICHIER.json`.

## Script, commande, sorties

- **Script** : `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1/verifier_ecart_dt4_v2.py`.
- **Sortie** : `…/audit-ecart-dt4-7a-v1/sortie-verifier-ecart-dt4-complement-v1.json`.
- **Commande exacte** : le lanceur ci-dessous, joué avec `FIN=35abfd16` (sans argument, il écrit la sortie nommée ci-dessus) :

```bash
#!/bin/bash
set -euo pipefail
cd /home/user/controle-ia-travail
FIN=${FIN:-5eaa900d}
D=docs/notes/g0-deux-semaines-v1
A=$D/e3-ter-v1/audit-ecart-dt4-7a-v1
L=$D/e3-ter-v1/lecture-7a-v1
C=$D/consignes-mere-2026-11-09-2200-v1
S=$D/scellement-course-t06-v1
I=$D/integration-t06-v13-main-v1
B=brouillons/ii-b-saboteur-budget-v1
R=brouillons/T0.6-organismes-v0-v1-candidat12
EMP=$(git show 6886b61e:$L/lecture-A-exploratoire-non-opposable-v1.md | sed -n 16p | grep -oE '[0-9a-f]{64}')
SORTIE=${1:-$A/sortie-verifier-ecart-dt4-complement-v1.json}
PIECES=()
for f in $(git ls-tree -r --name-only $FIN -- $B/ | grep -v '\.sha256$'); do PIECES+=(--piece "$FIN:$f"); done
for f in prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r4-cl4.md prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r4-cl4-couples-v1.json prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3.md prereg/contre-lectures/T0.6-organismes-v0-v1-candidat12-r3-cl3-couples-v1.json \
         $I/rapport-integration-v1.md $I/rapport-essai-blanc-S-voie-b-v1.md \
         $R-r4.md $R-r4-journal-v1.md $R-r4-couples-v1.json $R-r4-couples-variante-a-v1.json $R-r4-appliquer-v1.py \
         $C/consigne-integration-chaine-t06-v13-main-v1.md $C/consigne-integration-chaine-t06-v13-main-v2-additif.md \
         $C/consigne-contre-lecture-ii-b-v1.md $C/consigne-essai-blanc-construction-S-t06-voie-b-v1.md \
         $C/consigne-redaction-t06-candidat12-r4-v1.md $C/consigne-complement-audit-ecart-dt4-v1.md \
         $C/consigne-contre-lecture-4-t06-candidat12-r4-v1.md; do PIECES+=(--piece "$FIN:$f"); done
NOMMES=()
for f in consigne-integration-chaine-t06-v13-main-v1.md consigne-integration-chaine-t06-v13-main-v2-additif.md consigne-contre-lecture-ii-b-v1.md \
         consigne-essai-blanc-construction-S-t06-voie-b-v1.md consigne-redaction-t06-candidat12-r4-v1.md consigne-complement-audit-ecart-dt4-v1.md \
         consigne-contre-lecture-4-t06-candidat12-r4-v1.md; do NOMMES+=(--nomme-interdits "$FIN:$C/$f"); done
python3 -I -B $A/verifier_ecart_dt4_v2.py --depot . --plage 62ba4a4a..$FIN \
  "${PIECES[@]}" --piece "$FIN:registres/decisions.md#R-2052..R-2999" \
  --differentiel 6886b61e:$R-r3.md $FIN:$R-r4.md \
  --limite-anteriorite 9b7721c7 \
  --anterieur 8cb539f9:$R-r2.md \
  --anterieur fe240b24:$S/pieces-apres-couples/T0.6-organismes-v0-v1-candidat12-r2-apres-couples-v1.md \
  --anterieur fe240b24:$S/rapport-preparation-scellement-course-t06-v1.md \
  --anterieur 9b7721c7:registres/decisions.md --anterieur 9b7721c7:registres/etat.md \
  --anterieur 9b7721c7:registres/passations/2026-11-09-1829.md \
  --anterieur 9b7721c7:$D/e3-ter-v1/ordre-course-dose-reponse-exploratoire-v1-brouillon3.md \
  --anterieur 9b7721c7:$D/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md \
  --anterieur 9b7721c7:$D/contre-lecture-t06-course-v2/couples-candidat12-r2-v1.json \
  --heritage 6886b61e:$R-r3.md --heritage 6886b61e:$R-r3-journal-v1.md \
  --heritage 6886b61e:$L/lecture-A-exploratoire-non-opposable-v1.md \
  --heritage 6886b61e:$L/garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json \
  --heritage 62ba4a4a:registres/decisions.md --heritage 6886b61e:registres/passations/2026-11-09-2117.md \
  --heritage 6886b61e:docs/procedures/brief-reprise-nouvelle-mere-2026-11-09-v1.md \
  --heritage 61607820:$C/interdits-communs-v1.md --heritage 61607820:$C/consigne-audit-ecart-dt4-7a-v1.md \
  --heritage 61607820:$C/consigne-contre-lecture-3-t06-candidat12-r3-v1.md \
  --heritage 61607820:$C/consigne-conception-ii-b-saboteur-budget-v1.md \
  --empreinte-interdite "$EMP" --chercher-noms-b "$FIN:registres/decisions.md#R-2052..R-2999" \
  --commit-quarantaine e6c06113 "${NOMMES[@]}" \
  --sortie "$SORTIE"
```

## Pièces lues, empreintes vérifiées (toutes égales aux compagnons et aux registres)

| Pièce (à `35abfd16`) | Empreinte |
|---|---|
| consigne du complément | `56789718155ab10c92cabb9d82fff0fef16832f4a44facff117a321d187e7e69` |
| contre-lecture 3 | `3930d4f930639569…` |
| couples de la contre-lecture 3 | `e3846ae5d91cf9de…` |
| contre-lecture 4 | `001352b795c1c74ea896b0e5c733db1e5babfd220690c8cb84b7d7d06d9dac11` |
| couples de la contre-lecture 4 | `e6ad9c1550031b65b4cf8e079ac79dcc415a6b47c02b5544172a3d3830a9935c` |
| r4 | `eb6f10a061c671a0…` |
| journal de la r4 | `e1afb0cc3e32a2ad…` |
| couples de la r4, option (b) | `1d2a85dcafcb9b33…` |
| couples de la r4, variante (a) | `82e4951578332011…` |
| script d'application de la r4 | `fc5046e0c58325a5…` |
| rapport d'intégration | `427def658cdb4d6c…` |
| rapport d'essai à blanc de la voie B | `4f4eb27d98e33a9f…` |
| (ii-b), 20 fichiers, dont la conception b1 et b2, la contre-lecture 1 et ses couples, les journaux v1 et v2 | `sha256sum -c` des 20 compagnons conforme ; `549336e7…`, `47b86258…`, `0991e019…`, `bafe6779…`, `96160518…`, `59a443ff…` |
| sept consignes postérieures à `62ba4a4a` | lues au commit, sans compagnon requis par la consigne |
| `registres/decisions.md` R-2052 à R-2066 | à `35abfd16` |
| configuration du brouillon 5 (`git show 1609a4bf:…`), clés de sonde et d'audit seules | lue pour l'antériorité de la ligne 63 de la contre-lecture 3 |
| r2 (`8cb539f9`, `0d6bf1c4…`), pièces de `fe240b24`, registres à `9b7721c7` | références d'antériorité, comme en v1 |

## Interdits tenus

- **Jamais ouverts**, d'aucune manière : `diag/*/lecture-sondes-t06.json`, la lecture B, `donnees/lecture-b-7a-quarantaine-v1`, `e6c06113`, tout `diag/` et `runs/` de 7a, `essai/t06-explo-v3`, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, l'étiqueteur. **Jamais ouvert ni lancé** : `extraire_mesures_epreuve_t06_v1.py`, lu une seule fois en v1 sur consigne et plus jamais depuis.
- **Jamais touchés** : `/home/user/integ-t06` et le dossier `essai-S`.
- **Secrets** : aucune valeur de clé ; ni `env`, ni `printenv`, ni `set` sans argument, ni `export -p`, ni `/proc/*/environ`.
- **Appels et dépense** : aucun appel externe, aucun `vastai`, aucune dépense.
- **Git** : lecture seule (`log`, `diff`, `cat-file`, `show`, `ls-tree --name-only` sur `main`, `merge-base --is-ancestor`) ; rien committé.
- **Écritures** : seulement les sorties nommées et le bloc-notes de session.
- **Essais** : pas de suite complète.
- **Refus** : aucun refus d'un contrôle de permissions ou d'un classifieur.
- **Valeurs de sonde** : aucune valeur numérique tirée d'une sonde de 7a dans ce rapport, et je n'en ai vu aucune.

# Contre-lecture hostile et aveugle — devis et instruments de l'essaim qui communique — v1

- Relecteur neuf (Claude Opus 5.5, sous-agent), 22 novembre 2026. Aucune dépense, aucun appel de modèle, aucun réseau, aucun commit.
- Pièces : `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1/` (commit annoncé `de80ab49`) ; conception servie `…/reponse-fable-demande-7-v1/relecture-fable-api.md` (`dd60dd67…`, vérifiée par le script du devis).
- Mode d'échec affecté : **chiffre sans pièce**.

## Verdict

**À corriger** (réserves mineures sur le reste). Presque tous les chiffres renvoient à une pièce et se rejouent : le calcul du devis se rejoue **octet pour octet** ; les épreuves de l'oracle aussi, aux chemins d'écriture près ; les bases aussi (§ 2.3). Mais il y a trois points :
1. le « pire » du devis n'est pas le pire des pièces qu'il dit importer « telle quelle » : la borne par test est arrondie autrement que dans `devis_multi_generations_v2.py`, et les fausses lois et les copies que C.7 fait tester sont omises ;
2. une version de Python ou de numpy annoncée dans la note des bases est démentie par la sortie ;
3. un plafond (aiguilleur 0,25 USD) et un dénominateur (24 cartes par génération) sont écrits en dur, sans pièce citée à l'empreinte dans le devis.

## 1. Compagnons

22 compagnons `.sha256` sur 22 sont conformes, et aucun fichier n'est sans compagnon (`outils/verifier_compagnons_v1.py`). Les empreintes des pièces citées et recalculées par moi sont conformes : `devis_multi_generations_v2.py` `710954c7…`, `devis_multi_generations_v1.py` `15256924…`, `monde_riche_outils_v1.py` `1825b956…`, `analyse-journaux-re-search-v1.md` `8a82b5ee…`, `devis-v4.json` `1fdfaa51…`, `calcul-devis-course-auto-conception-v1.py` `8bd1e48a…`.

## 2. Table des chiffres

Légende : rejoué **oui** (par programme ou arithmétique refaite sur la pièce), **non** (pièce absente ou seulement citée), **divergent**.

### 2.1 Devis (`devis-essaim-communicant-v1.md`, `1bfee9f3…`)

| chiffre | pièce | rejoué |
|---|---|---|
| tout `calcul-devis-essaim-v1.json` (`8766775c…`) | `calcul_devis_essaim_v1.py` rejoué dans ma copie → `tables/calcul-devis-essaim-v1-rejoue.json` | **oui, octet pour octet** (`cmp` vide) |
| tableau 3.1 (7 espèces × 8 colonnes), 3.2, 3.3, borne dure 8 050 / 17 500 / 29 400 | même sortie ; `extraire_lignes_devis_v1.py` rejoué | oui (arrondi à l'unité) |
| tarifs Fable 8 / 40 | `relecture_fable_api_v3.py` l. 99-100 (`95bea064…`) | oui |
| Argon 8,3 / 41,5 | `appel-argon-v5.sh` l. 29 (`37c0205e…`) | oui |
| Claude 4 / 20 et 10 / 50, Kimi 2 / 10, Astra 10 / 50, Carbon 8,3 / 41,5 | `calcul-devis-course-auto-conception-v2.json` (`91f5cf8f…`), lu par le script à l'empreinte | oui sur la pièce secondaire ; **non** sur la pièce primaire (absente, comme le devis le déclare) |
| 1,130496 USD (coût de la relecture de Fable) | en-tête de la conception : 10 732 × 8 + 26 116 × 40 | oui |
| ρ = 5 pour les sept espèces | sortie, `rapport_sortie_sur_entree_par_espece` | oui |
| unités de la section D : 92 / 200 / 336 courses, 2 300 / 5 000 / 8 400 appels, 4 600 / 10 000 / 16 800, 384 / 864 / 1 440, 9,2 / 6,9 … 168 / 134,4 | tableaux D de la conception | oui (0 écart) |
| 23,7 % de cartes promues (7,92 + 8,58 + 0,58 sur 72) | `devis-v4.json` (`1fdfaa51…`) pour les numérateurs | **numérateurs oui ; le dénominateur 24 par génération est écrit en dur** (`calcul_devis_essaim_v1.py` l. 125, commentaire « 4 proposeurs × 6 cartes »), sans lecture dans la pièce. Il est cohérent avec `"formule": "… T_pire = 37"` = 6 × 4 + 13, mais il est supposé |
| test : 2 tours de 8 000 / 2 000 jetons, + 0,06 ; au pire 12 tours de 8 000 / 4 000, + 0,10 ; 10 et 13 plantées | `devis_multi_generations_v2.py` l. 4-11, 20-23 | oui pour les paramètres ; **divergent pour la borne au pire** (voir D-1) |
| 0,204 et 0,132 USD par test (première espèce Claude, Kimi) | arithmétique | oui |
| plafonds de session : proposeur 3,00, aiguilleur 0,25 | devis d'auto-conception v1 § 4 (3,00, l. 50) ; « calcul v1, `PLAFONDS_SESSION` » | 3,00 oui. **0,25 : orphelin dans le devis** (ni chemin ni empreinte ; le script l'écrit en dur, l. 115). Je l'ai retrouvé dans `calcul-devis-course-auto-conception-v1.py` l. 40 (`8bd1e48a…`, chemin donné seulement par le rapport) |
| aiguilleur 6 250 / 300 et 23 000 / 2 000 ; 0,031 contre 0,014 USD ; +170 USD | `devis-course-affinage-mentors-v5.md` § 2 l. 25 (`52147009…`) ; arithmétique 0,017 × 10 000 | oui |
| juge : 0,16409 + 0,400484 = 0,564574 ; tests de la génération 1 : 1,429736 − 0,539846 = 0,88989 | analyse v67, § 2 M1, l. 45-50 | oui (sur l'analyse ; le journal primaire est absent, comme le devis le déclare) |
| 16 appels d'Argon, dont 14 de vérificateur | `devis_multi_generations_v1.py` l. 43, qui cite le verdict v67 § 4.5 (`d7902432…`, non relu) | **non** (cité de seconde main) |
| 31 891 et 38 343 jetons de sortie de Kimi ; environ 6 400 par carte, environ 12 800 pour deux | `devis_multi_generations_v1.py` l. 29, qui cite le verdict v67 § 4.1 (non relu) | **non à la source** ; cohérent : aux prix de Kimi, 0,333476 et 0,400484 USD (M1) donnent des entrées de 7 283 et 8 527 jetons, plausibles ; 70 234 / 11 = 6 385 |
| Argon : au plus 4 973 jetons de sortie, environ 830 par carte, facteur huit | 0,20637 / 41,5 × 10⁶ ; M1 | oui |
| 6,4 %, un appel de plus, reliquat de 14 000 | sortie, `egalisation_C1` | oui |
| « tests 70 à 80 % de l'estimation » | sortie : Kimi 80,2 %, Claude 1 75,8 %, Fable 72,7 %, Argon 72,6 %, Claude 2 72,0 % | oui, à l'arrondi à l'unité (80,2 % arrondi à 80) |
| « instruments payants 1 316 / 805 / 2 851 USD » | sortie (pilote + bras d'instrument) | oui |
| **« dont 319 pour la section D seule »** | 168,48 + 151,04 = **319,52** | **divergent à l'arrondi** (donne 320 ; l'auteur a tronqué) |
| machine 0,15 USD par monde et par génération | `devis_multi_generations_v2.py` l. 42 | oui |

**D-1 (chiffre divergent qui compte).** Le devis écrit « formule importée telle quelle » et « 12 tours … arrondis au dixième au-dessus ». La pièce importée borne un test par `BORNE_TEST` + `VERIF_PIRE`, soit 1,50 + 0,10 = **1,60 USD** pour la première espèce Claude et 0,80 + 0,10 = **0,90 USD** pour Kimi (l. 20-22). Le devis prend ceil₀,₁(1,344) + 0,10 = **1,50** et ceil₀,₁(0,672) + 0,10 = **0,80**. Le script vérifie que la chaîne `BORNE_TEST = {"opus": 1.50` est présente, puis ne l'utilise pas : ce contrôle ne peut pas échouer sur ce qui compte. Avec la borne de la pièce, le pire du cas attendu vaut 41 897 USD au lieu de 39 337 (première espèce Claude) et 23 509 au lieu de 20 949 (Kimi) ; le pire toutes espèces (10 / 50 : 3,36 → 3,40 + 0,10 = 3,50) ne bouge pas. Source : `outils/pire_alternatif_v1.py` → `tables/pire-alternatif-v1.txt` (colonne P1).

### 2.2 Note de l'oracle (`oracle-toutes-cartes-v67-v1.md`, `44f9dadc…`)

| chiffre | pièce | rejoué |
|---|---|---|
| gain du monde 0,523558 ; K1 0,052427 ; enveloppe 0,052453 ; au-delà de l'enveloppe 0,471105, −0,000026, −0,006676, 0,447598 | `epreuves_oracle_v67_v1.py` rejoué → `tables/epreuves-oracle-rejouees/sortie-a1.json` | oui (identique) |
| les 12 épreuves (tenues ; source réelle : code 2) | `epreuves-oracle-v67-v1.json` | **oui** : artefacts a1 à a4 identiques à l'octet, les autres identiques hors des champs `fichier` et `source.chemin` (`outils/comparer_epreuves_v2.py`) |
| 20 000 instances, `SeedSequence(20261122)`, seuil 0,02 | script et sortie | oui |
| comptes sur les promues (12, 6, 6, 0 ; 11, 5, 5, 0) ; 11 formes sur 23 | analyse v67 l. 52, 56 | oui |
| « même définition que la course simulée v4 » | `monde_riche_v4.course` : ni chemin ni empreinte dans la note | **non** (affirmation sans pièce rejouable ici) |
| oracle sur les 23 cartes de v67 | journal absent (`21bc75f4…`) | **non rejouable** ; aucun chiffre n'est rendu, comme la note le dit |

### 2.3 Note des bases (`bases-sans-modele-v1.md`, `cf19506c…`)

Rejeu de `bases_sans_modele_v1.py` (`29276c45…`) dans ma copie → `tables/bases-sans-modele-v1-sortie-rejouee.json` : **toutes les clés sont identiques à la sortie publiée** (`4dcdeacf…`), sauf `debut_utc` et `fin_utc` (`outils/comparer_bases_v1.py` → `tables/comparaison-bases-v1.txt`).

| chiffre | pièce | rejoué |
|---|---|---|
| couverture médiane 0,69 (0,43 ; 0,86), moyenne 0,69, certifiées 0,71, 3 / 14 conditionnelles, 562 / 624, 4 formes fausses (B3) | `resume` | oui (0,6905 ; 0,4286 ; 0,8571 ; 0,688 ; 0,70835) |
| B2 : 0,155 (0 ; 0,625), 0,19, 0,25, 58 / 624, 47,5 ; B1 : 0, 0 / 624, 52 | `resume` | oui |
| couverture de B3 par monde (12 valeurs) | `par_monde` | oui (arrondi à 2 décimales) |
| couverture brute : B1 1,0, B2 0,29, B3 0,69 | `resume` | oui |
| épreuves : 12 / 12 (gabarit, attribution avec un écart de 0, K1 fausse) ; loi du monde 11 / 12 (monde 0) ; `controles_tenus` faux | `par_monde.*.controles` | oui |
| monde 1, avant et après correction (B1 1,0 → 0 ; B2 0,2857 → 0,1429 ; B3 0,5714) | `essai-bases-monde-1.json`, `-b.json` | **-b oui** (même script, `29276c45…`) ; **l'essai 1 n'est pas rejouable** : script `1eb9ff34…` absent du dossier |
| « environ 227 candidats » | `trajet_glouton.candidats` : 226, 225, 224 | **divergent à l'arrondi** (225 en moyenne) |
| « environ 7 minutes » | horodatages 06:03:01 → 06:09:59 | oui |
| « Python 3.13.18, **numpy 2.5.3** » | sortie : `numpy` = **2.4.6** | **divergent** (la note annonce une version que la sortie dément) |
| 2 000 instances servies | `N_SERVIES` | constante déclarée comme hypothèse, sans pièce (comme la note le dit) |

## 3. Réponses courtes

**L'oracle lit-il vraiment aucun verdict ?** Oui pour ce qu'il utilise. La projection garde quatre clés de premier niveau ; la classe d'une carte est une fonction de `loi` seule, sous la loi du monde ; l'invariance aux verdicts permutés ou supprimés est rejouée. En revanche, **un champ de verdict peut entrer sous un autre nom** dans le sous-arbre `loi` : la liste noire compare des noms exacts. `promu`, `retenu`, `p_valeur`, `rang`, `log_w` (seul `log_w_max` est listé) passeraient, et l'épreuve a4 n'essaie qu'un nom déjà listé. Sans effet sur la classe tant que la grammaire ignore les clés inconnues ; ce point n'est pas éprouvé.

**Les deux corrections des bases faites après le monde 1 sont-elles un réglage sur l'épreuve ?** Le monde 1 fait partie des 12 mondes rapportés : le chiffre de la note est donc lu, en partie, sur le monde qui a servi à régler. Ces 12 graines de développement publiques ne sont pas les mondes scellés du confirmatoire (réserve 3), qui ne sont pas touchés. La correction 1 (« seules les cartes vraies couvrent ») ne change pas B3, la base qui contraint (0,5714 sur le monde 1 avant et après), et ne fait baisser que B1 et B2. La correction 2 relâche un objet de contrôle après qu'il a échoué : c'est le cas typique du réglage d'un témoin, et il échoue encore dans le monde 0. Enfin, la correction 1 redéfinit la métrique de C.5 : elle doit passer au préenregistrement, non rester dans un instrument. Le script de la première écriture (`1eb9ff34…`, consigné dans `essai-bases-monde-1.json`) n'est pas dans le dossier : l'essai 1 n'est pas rejouable, et le fichier a été écrasé, contre R12.

**Le devis compte-t-il tout, et le pire est-il un pire ?** Non. Le pire n'est un pire que pour les tests de mort, et encore, il est sous la borne de la pièce importée (D-1). Il garde les **jetons du régime** pour les proposeurs, les messages et l'aiguilleur : ni plafond de session, ni 23 000 / 2 000 au haut pour l'aiguilleur. Il omet les **fausses lois et les copies** que C.7 fait tester (`FAUSSES_ET_COPIES = 8` par génération dans la pièce). Il omet aussi le passage des objets de contrôle par l'aiguilleur, toute **relance** et la **machine** (déclarée). Il ne compte pas le surcroît d'entrée de (a) (tableau partagé et messages relus : 9 000 jetons partout) ni le dépassement de 105 % que permet C.8. Sous les conventions des pièces citées, le pire toutes espèces au haut passe de 159 588 à **216 036 USD** avec les fausses et les copies, puis à **236 448 USD** avec proposeurs et aiguilleur à leur plafond de session (`tables/pire-alternatif-v1.txt`, P2 et P3). Ce sont des bornes de construction, non des prévisions.

## Relevé de méthode

### Chaîne de raisonnement
1. Les 22 compagnons du dossier des pièces sont conformes (`outils/verifier_compagnons_v1.py`, sortie : ok=22 ko=0 sans_compagnon=0).
2. `calcul_devis_essaim_v1.py` (`a3a6d24b…`), copié dans mon dossier et rejoué, rend une sortie identique à l'octet à `calcul-devis-essaim-v1.json` (`8766775c…`) : `cmp` vide.
3. Les chiffres des tableaux 3.1 à 3.3 sont les valeurs de cette sortie, arrondies à l'unité. Exception : « 319 » pour 319,52 (sortie rejouée, `extraire_lignes_devis_v1.py`).
4. Le script lit les tarifs dans les pièces à leur empreinte. Ses refus ne se sont pas déclenchés : les empreintes sont conformes (pas 2).
5. La borne par test au pire de la pièce importée vaut 1,60 et 0,90 USD (`devis_multi_generations_v2.py` `710954c7…`, l. 20-22) ; celle du devis vaut 1,50 et 0,80 (pas 2, sortie `usd_par_test`) ⇒ D-1.
6. C.7 de la conception (`dd60dd67…`, l. 169-171) fait passer par la chaîne des lois fausses et des copies ; la pièce importée compte ces tests à part (`FAUSSES_ET_COPIES = 8`, l. 7 et 23), et le devis ne les compte pas (l. 113-114 du script) ⇒ le pire est sous-estimé.
7. Les recalculs P0 à P3 (`outils/pire_alternatif_v1.py`) redonnent d'abord le pire du devis (P0 = devis dans 18 cas sur 18), puis les variantes.
8. Les numérateurs du taux de promus sont lus dans `devis-v4.json` (`1fdfaa51…`) ; le dénominateur 24 est **supposé** par le script (l. 125).
9. Le plafond de 0,25 USD de l'aiguilleur se trouve dans `calcul-devis-course-auto-conception-v1.py` l. 40 (`8bd1e48a…`) ; le devis ne le cite pas à l'empreinte.
10. Les chiffres de v67 cités par le devis se recalculent sur l'analyse (`8a82b5ee…`, l. 45-50) ; 31 891 / 38 343 et « 16 dont 14 » ne sont que cités (`devis_multi_generations_v1.py` l. 29 et 43, qui renvoient à un verdict non relu).
11. Les épreuves de l'oracle, rejouées, sont identiques aux sorties publiées hors chemins (`outils/comparer_epreuves_v2.py`) ; les 12 épreuves rendent le même résultat.
12. La liste noire de l'oracle compare des noms exacts (`oracle_toutes_cartes_v67_v1.py` l. 37-40, 61) ⇒ un autre nom placé dans `loi` passe ; l'épreuve a4 utilise un nom listé (`epreuves_oracle_v67_v1.py` l. 103).
13. Les bases rejouées donnent une sortie identique à la sortie publiée, clé par clé hors horodatages (`tables/comparaison-bases-v1.txt`). La version de numpy écrite dans la note (2.5.3) diffère de celle de la sortie publiée comme de la mienne (2.4.6).
14. La première écriture des bases (`1eb9ff34…`) n'est pas sur disque dans le dossier : l'essai 1 n'est pas rejouable (`essai-bases-monde-1.json`, champ `script_sha256`, comparé à la liste du dossier).

### Objets de contrôle
- **Rejeu octet pour octet (comparateur).** Objet vrai par construction : le JSON rejoué contre le JSON publié, attendu identique ; rendu identique. Objet faux par construction : mon comparateur des épreuves a d'abord rendu « DIVERGE » sur des fichiers qui ne diffèrent que par leur chemin d'écriture (normalisation fautive, `comparer_epreuves_v1.py`) ; j'ai écrit `comparer_epreuves_v2.py`, qui retire seulement `fichier` et `source.chemin`. Les artefacts a1 à a4, sans chemin, sont restés identiques à l'octet dans les deux versions, ce qui montre que v2 ne masque pas d'autre champ.
- **Recalcul du pire (`pire_alternatif_v1.py`).** Objet vrai par construction : la variante P0 doit redonner le pire du devis ; elle le redonne dans les 18 cas. Objet faux par construction : une première version appliquait à Argon la borne de la pièce (3,40, calculée à 10 / 50) alors qu'Argon est à 8,3 / 41,5. L'écart obtenu (76 185 → 91 545) était donc faux par construction ; je l'ai vu et retiré. La ligne Argon de P1 égale maintenant P0.
- **Contrôle de formule du devis** (`verifier_formule_tests`). Il doit refuser si la formule importée diffère de celle utilisée. Sur une formule importée vraie, il passe. Sur une formule fausse par construction (la borne utilisée, 1,50, n'est pas la borne de la pièce, 1,60), il passe aussi, puisqu'il ne vérifie que la présence d'une chaîne : ce contrôle est **mort** pour ce qu'il prétend établir.
- **Liste noire de l'oracle.** Nom listé caché dans `loi` (a4, faux par construction) : refus attendu, refus rendu. Nom non listé : non éprouvé, par construction de la consigne (aucune course nouvelle) ; le code (pas 12) montre que le nom passerait.

### Premier pas non justifié
Le pas 8 : le dénominateur de 24 cartes par génération n'est pas lu dans `devis-v4.json`. Il serait justifié par la lecture du champ ou du code qui fixe 4 proposeurs × 6 cartes dans la simulation v4 (`devis_multi_generations_v4.py`, `f166fa4a…`, que je n'ai pas lu).

### Mode d'échec affecté
**Cassé** pour « chiffre sans pièce », sur les pas 5-6 (D-1 : un pire qui se dit importé tel quel et ne l'est pas), le pas 9 (0,25 sans empreinte dans le devis), le pas 8 (dénominateur supposé), le pas 3 (« 319 ») et la version de numpy des bases (§ 2.3). Tout le reste est tenu et rejoué. Preuves : `tables/calcul-devis-essaim-v1-rejoue.json`, `tables/pire-alternatif-v1.txt`, `tables/epreuves-oracle-rejouees/`, `tables/bases-sans-modele-v1-sortie-rejouee.json`.

### Dérivation de l'énoncé seul
Sans objet : je suis relecteur, non agent de re-dérivation.

### Trouvaille de côté
- Le tarif d'Argon diffère entre les pièces du noyau : 10 / 50 « supposé » dans `devis_multi_generations_v2.py` l. 17, contre 8,3 / 41,5 dans l'enveloppe. Le vérificateur à 0,06 / 0,10 USD vient du devis v66, non relu.
- La seule mesure de la sortie du proposeur (environ 12 800 jetons pour deux cartes, Kimi) dépasse l'estimation de 6 000 qui sert au cas attendu ; le devis le note sans le reporter.
- L'essai 1 des bases a été produit par une version du script qui a été écrasée (R12).
- Écart du relecteur à l'en-tête de commandes : une fois, j'ai lancé `python -I -c "import sys" --version` pour lire la version de Python (rien d'autre n'a été exécuté), puis je l'ai refait sans `-c`. Aucun refus n'a été rencontré.

### Évaluateur et conseil
Ce qui juge ici : la comparaison octet pour octet ou hors chemins, et l'arithmétique sur les pièces empreintées, avec mes comparateurs admis sur les témoins ci-dessus (P0 = devis ; artefacts identiques à l'octet). Ma pièce pourrait obtenir un bon jugement sans le mériter si un chiffre était égal par construction, parce que le script relit sa propre constante. C'est le cas des unités de la section D, recopiées puis comparées aux tableaux de la même conception : le rejeu prouve la cohérence, non la provenance. Je l'ai donc distingué (« pièce primaire absente », « supposé »).

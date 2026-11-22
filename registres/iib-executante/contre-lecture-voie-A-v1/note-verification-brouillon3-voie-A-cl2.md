# Vérification du brouillon 3 de l'additif et du devis de la voie (A) — cl2

Date : 2026-11-22. Classe A. Contre-lecteur neuf : Claude Opus 5.5. Je n'ai écrit aucune pièce. Rien dépensé, aucun loueur appelé, aucun modèle externe, rien poussé. Aucune pièce interdite ouverte.

## Verdict

**Scellable après corrections.** Le brouillon 3 porte exactement B1, B2, B3, toute la section C et la section D de la vérification du brouillon 2. L'arithmétique se rejoue à l'octet. Aucune régression trouvée. Mais trois faits du registre et du code, postérieurs au mandat ou absents de lui, ne sont pas portés :
- le correctif 0024 (le code de la voie est à `9780b7e3`, pas à `9b03d0ea`) ;
- l'exécutante neuve (`GO-2026-11-22-94`) ;
- la prolongation de la ligne par `GO-2026-11-22-93`, qui exige d'être citée.

Il faut aussi écrire honnêtement ce que tient le second rempart de dépense sous le correctif 0023. Après ces quatre corrections majeures et le remplissage des champs, l'additif est scellable.

## Pièces

Commit `6eb0ab65f66f5dce86b3aae134b4c5b26c8ed340`. Toutes les empreintes sont conformes à leurs compagnons :

| pièce | empreinte |
|---|---|
| additif, brouillon 3 | `3d658ce0d6af1a44…` |
| devis, brouillon 3 | `109ca7c3500ed568…` |
| différences entre les brouillons 2 et 3 | `4b404f89ad72acac…` |
| programme de calcul v3 | `a6c959f4…` |
| sortie du calcul v3 | `f8a5df58…` |
| vérification des gardes v3 | `89d311ed…` |
| sortie de la vérification v3 | `a3b9f3b1…` |

Les empreintes citées dans l'en-tête de l'additif et du devis sont exactes.

## A. Points de la vérification du brouillon 2 : portés

| point | où le brouillon 3 le porte | état |
|---|---|---|
| B1, création de l'étalonnage | § 3.2, dernière phrase, et § 3.4, étape 2 : « la commande imprimée porte `-e IIB_TIRAGE=carte` », sinon nœud | porté |
| B1, arrêt de l'étalonnage | § 5, « Étalonnage rejoué », et § 3.4, étape 3 : `TIRAGE=` ou `tirage` autre que `carte`, arrêt par l'identifiant. Les deux marques existent dans le code à `9780b7e3` : `TIRAGE=` aux lignes 330 et 346 des deux amorces, `tirage=` aux lignes 713 et 817 de `lanceur_v5.py` | porté |
| B1, course | § 4.3, point 5, et § 5, « Course » | porté |
| B2 | A2 : « sauf par la minuterie de l'amorce, à l'échéance (ordre scellé ; A3) » | porté |
| B3 | A2 : par la mère, par l'identifiant seul, à 15:26:31Z, « go toi-même », `GO-2026-11-22-77`, `registres/arrets.md`, ligne 153. La ligne 153 de `main` le confirme | porté |
| C, A3, dépense antérieure | compte vrai, au centime supérieur, sans borne. La règle du correctif 0023 est écrite telle que le mandat la donne, avec ses cas | porté |
| C, A3, machine de la course | 34,78 heures retirées ; échéance et épuisement par [M27] | porté (voir M4) |
| C, A3, ce qui tient la coupure | « c'est le compte lui-même ». Vérifié : `echeance 55 5.523 …` rend « 5.53 » | porté |
| C, § 4.3, point 3 | forme exacte. La ligne citée correspond à la sortie réelle de `go` à `9780b7e3` | porté |
| C, § 6, champs | `<<VERIFICATION_DU_CORRECTIF_0022>>` et `<<CORRECTIF_0023_…>>` ajoutés ; la liste v7 est rattachée au correctif 0022 | porté |
| C, § 7, point 3 | retiré ; les points sont renumérotés | porté |
| C, arbre du code | `6696aca1f` n'est plus l'arbre de la voie | porté (voir M1) |
| C, devis, § 4 et liste d'arrêt | réécrits ; ligne du refus de la garde 0023 et lignes du tirage ajoutées | porté |
| C, programmes | `DECLAREE_MAX` retiré ; seules [M24], [M25] et [M27] changent. Vérifié par une différence entre les sorties v2 et v3. La vérification des gardes v3 attend 5,52 et 9,65 acceptés et 60 refusé | porté |
| D, champs | 0021 rempli ; branche écrite ; les autres restent des champs ; 311 et 313 sont annoncés | porté |

Aucune régression. Les différences entre les brouillons 2 et 3, hors en-tête, ne touchent que les passages nommés par la note des différences.

## B. À corriger

### Majeurs

**M1 — Le correctif 0024 manque partout.**

Le code actuel de la voie est `9780b7e38d6544fed62d5b8fa50aca2a50e8233a`, arbre `475631a8e6340012701ebe2463f77f2449d2ba0a`. Il porte le correctif 0024, qui corrige la contre-lecture du 0023 :
- le plafond total est écrit exact (majeur de cette contre-lecture) ;
- les refus sont écrits sans « 60.0 » ;
- le libellé de la surveillance change.

Le brouillon 3 ne cite que `9b03d0ea` (en-tête, lignes 11 et 13 ; § 2, ligne du correctif 0023 ; A3), et la vérification v3 a été jouée à ce commit. Ce commit ne sera pas l'arbre de la voie.

Corrections :
- § 2 : ajouter une ligne « Correctif 0024, corrections de la contre-lecture du correctif 0023 (plafond total écrit exact ; refus sans « 60.0 » ; libellé de la surveillance) : commit `9780b7e38d6544fed62d5b8fa50aca2a50e8233a`, arbre `475631a8e6340012701ebe2463f77f2449d2ba0a` ; chemin, empreinte et vérification : `<<CORRECTIF_0024_CHEMIN_EMPREINTE_ET_VERIFICATION>>` ».
- Ou bien élargir le champ du 0023 en `<<CORRECTIFS_0023_0024_CHEMINS_EMPREINTES_ET_VERIFICATIONS>>`, au § 2 et au § 6.
- § 2, « Ce qui reste exigé », point 1 : « les correctifs 0021, 0022, 0023 et 0024 ».
- § 2, ligne « Code de la voie » : « l'arbre qui porte les correctifs 0021 à 0024, vérifiés ».
- Devis, § 7, point 7 : « les correctifs 0022, 0023 et 0024 sont en vérification ».
- Différences 2 vers 3 : une ligne pour ce fait neuf.
- Rejouer `verifier-gardes-du-lanceur-v3.sh` à l'arbre final et verser sa sortie sous un nom neuf (R12), par exemple `sortie-verification-gardes-du-lanceur-v3-arbre-voie.txt`. La citer en A1, A3, en tête (ligne 13) et au devis, § 4. La sortie à `9b03d0ea` reste.
- Rejeu à `9780b7e3` (section C) : mêmes codes et mêmes valeurs dans tous les cas. Seuls changent l'en-tête (commit et arbre) et cinq libellés de refus (« 60.0 » devient « 60 »). La sortie n'est donc pas identique à l'octet.

**M2 — L'exécutante nommée n'est plus la bonne.**

§ 4.2, ligne « Exécutante » : `session_01XJ6MgqUTEVCed6a2f6rWmC`. Or `GO-2026-11-22-94` lance une exécutante neuve. Le mandat la nomme `session_013QMaym1QE4UyYr1H8KU8Rf`.

Correction : « Exécutante : l'exécutante neuve `session_013QMaym1QE4UyYr1H8KU8Rf` (`GO-2026-11-22-94`), branche `claude/iib-executante-v5` ; aucune autre session ne joue la voie. »

Ajouter au § 7 : la ligne de session `GO-2026-11-22-94` échoit le 2026-11-25. Si l'étalonnage, la désignation ou la course débordent ce jour, il faut un mot de Lazar avant toute commande. Les créations restent permises jusqu'au 26 inclus.

**M3 — `GO-2026-11-22-93` n'est pas cité.**

`registres/go.md` de `main`, ligne 780, inscrite à 16:07:16Z, prolonge `GO-2026-11-22-75` au 2026-12-31. Elle dit : « tout emploi cite l'accord d'origine et cette ligne ».

Correction, en A1, en tête de l'additif (« Ligne d'accord ») et dans « Accord cité » du devis : « Prolongée au 2026-12-31 par `GO-2026-11-22-93` (plafonds et conditions inchangés), citée comme elle l'exige. Le code lit l'échéance de la ligne `GO-2026-11-22-75` elle-même (2026-11-30). Rien ne change au calendrier de cet ordre : aucune création à partir du 2026-11-27, minuterie au plus tard le 2026-11-30T22:00:00Z. »

**M4 — Le second rempart de dépense ne tient plus 60 USD.**

L'additif (A3, sous-puce « Machine de la course ») écrit : « L'épuisement calculé par le lanceur […] tient le total de la voie sous 60 USD ». Le devis, § 4, dit la même chose. C'est inexact dès que les frais au-delà de la coupure sont comptés.

Sous le correctif 0023, la surveillance du côté de la session (`session_v3 surveillance "$PLC"`) arrête la machine au total compté T = min(60, 55 + compte). Elle ne la détruit pas. La consignation (0,92) et le stockage à l'arrêt (au plus 3,84) s'ajoutent ensuite. Si la minuterie de la machine fait défaut, le total peut donc atteindre min(60, 55 + compte) + 4,76, soit 64,76 USD au plus dès un compte de 5 USD. C'est au-delà du plafond de la ligne. Avant le correctif 0023, ce rempart arrêtait au total de 55.

Le pire de 59,76 USD ne tient que par l'échéance. Or l'échéance n'est appliquée que sur la machine : `ECHEANCE_UTC_S` est passée à la minuterie de l'amorce, que l'additif lui-même range parmi les choses « jamais éprouvées » pour la course (§ 7, point 7).

Corrections :
- Remplacer la phrase en A3 et au devis, § 4, par : « L'échéance, appliquée par la minuterie de l'amorce, tient le pire à 59,76 USD [M14]. Le second rempart, du côté de la session, est l'épuisement du lanceur : il arrête la machine au total compté min(60, 55 + compte), puis consignation et stockage peuvent porter le total à 64,76 USD au plus. »
- Ajouter en A3 une garde du côté de la session : « À l'échéance plus 10 minutes, si la machine est encore à l'inventaire, l'exécutante l'arrête par son identifiant et rend la main : nœud. » Avec cette garde, le pire de 59,76 tient sans dépendre de la seule minuterie.
- Ajouter la ligne correspondante au § 5 (« Course ») et à la liste d'arrêt du devis.
- Ajouter une réserve au devis, § 7, et un point au § 7 de l'additif, pour que Lazar le sache.

### Mineurs

- **m1 — Crédit périmé (devis, § 0, ligne 28, et [M15]).** Le devis lit encore « crédit lu le 22 novembre à 14:11Z (12,995 USD) ». Le registre (`GO-2026-11-22-77`) dit le compte rechargé de 30 USD, et la vérification du brouillon 2 a relu 39,81 USD. Correction : garder [M15] comme valeur d'origine datée et ajouter « crédit relu après la recharge de 30 USD (`GO-2026-11-22-77`) : 39,81 USD ; il couvre le pire de la machine de l'étalonnage (21,32 USD) ».
- **m2 — Écriture du nombre déclaré.** Le lanceur n'accepte que `^[0-9]+([.][0-9]+)?$`. Ajouter au § 4.3, point 3, et au § 4.4, point 2 : « le compte s'écrit avec un point, tel que le programme le rend (« 5.53 ») ». Autre détail : la sortie du programme affiche le compte arrondi au plus proche (« compte 5.52 » pour 5,523) et la valeur déclarée arrondie au-dessus (« 5.53 »). Le dire, ou faire imprimer le compte à trois décimales dans une v4.
- **m3 — Ligne 13 de l'en-tête.** « Au commit du correctif 0023 (`9b03d0ea…`) : les sous-commandes `go` et `plafond-total` […] lues dans leur différence. » Ajouter : « et la différence du correctif 0024 ».

## C. Rejeux

| rejeu | résultat |
|---|---|
| `python3 -I calcul-devis-voie-A-v3.py`, avec le Python du système et avec celui de l'environnement virtuel | code 0 ; sortie **identique à l'octet** (`f8a5df58…`) |
| `verifier-gardes-du-lanceur-v3.sh` à `9b03d0ea`, sur `registres/go.md` de `main` (tête `3b7d0398…`, registre `e765c0ce…`), configuration `08e22099…` | **identique à l'octet** à la sortie versée (`a3b9f3b1…`) |
| le même, au commit demandé `9780b7e3` | décisions **identiques** : 0 ; 4,20 ; 5 ; 5,01 ; **5,52** ; **9,65** ; 16,22 et 59,99 acceptés (machine 55 ; 55 ; 55 ; 54,99 ; 54,48 ; 50,35 ; 43,78 ; 0,01) ; **60**, 60,01, −1, nan, inf, illisible, configuration 61 et ligne absente refusés ; calendrier en code 0 les 23 et 26, refus le 27 ; épuisements 1000138260, 1000136904, 1000126130, 1000108991. Le fichier n'est **pas identique à l'octet** : l'en-tête change (commit, arbre `475631a8…`) et cinq libellés de refus perdent leur « .0 » (lignes 48, 50, 53, 55 et 78). C'est l'effet attendu du correctif 0024 |
| [M27] recalculé à la main | épuisement (min(60, 55 + c) − c − 2) / 1,38 : 38,41 ; 38,03 ; 35,04 ; 30,28 h. Égal au § 5 de la vérification (secondes / 3 600). Échéance à 16,22 : 36,78 / 1,38 = 26,65 h |
| [M24] | 30 h × 1,38 + 2 = 43,40 |
| dates [M28] | 1795737600 = 2026-11-27T00:00:00Z ; 1796076000 = 2026-11-30T22:00:00Z ; 1796083200 = 2026-12-01T00:00:00Z ; échéance de [M24] et [M25] 1795708000 = 2026-11-26T15:46:40Z |
| délais | A4, 35,5 min [M18] ; A5, 85 et 324 min [M20] [M21] ; 24 tours admis contre 30 financés [M22] [M23] ; étalonnage borné à 14 h, soit 21,32 USD. Tout est cohérent entre l'additif, le devis et la sortie |
| règle de dépense écrite contre le code (`session_v5.coupure_effective` à `9780b7e3`) | `go` : configuration ≤ ligne, antérieure < ligne ; total = min(ligne, configuration + antérieure) ; machine = total − antérieure = min(55, 60 − antérieure) ; total compté ≤ 60. **Conforme.** Seule l'affirmation sur le total après l'arrêt est à corriger (M4) |
| liste v7 à `9780b7e3` | `scripts/tests-cibles-iib-v5-v7.txt`, sha256 `81e2f75ac9cab360324485f4d76b326d97e7297a0aeaf5af70a52f515e8f21b8`, 26 lignes. Les essais neufs du correctif 0023 (`test_iib_garde_depense_0023.py`) n'y sont pas, ce qui est conforme au message du commit (« listes figées inchangées ») |

## D. Champs entre chevrons restants, et ce qui les remplira

| champ | ce qui le remplira |
|---|---|
| `<<VERIFICATION_DU_CORRECTIF_0022>>` | l'exécutante, avec la note de vérification du correctif 0022 par son contre-lecteur : chemin, empreinte, verdict |
| `<<CORRECTIF_0023_CHEMIN_EMPREINTE_ET_VERIFICATION>>`, à élargir au correctif 0024 (M1) | l'exécutante, avec les correctifs 0023 et 0024 (chemins, empreintes), la contre-lecture du 0023 et la vérification du 0024 |
| `<<LISTE_ETALONNAGE_AVEC_ESSAI_DU_TIRAGE>>` | l'exécutante, avec l'empreinte de la liste v7 à l'arbre final (`81e2f75a…` à `9780b7e3`), rattachée à la vérification du correctif 0022 |
| `<<COMMIT_CODE_REVU_VOIE_A>>`, `<<ARBRE_CODE_VOIE_A>>` | l'exécutante, vérifié par la mère. Candidat : `9780b7e3` et `475631a8…`, si rien ne s'y ajoute. Ce commit n'est aujourd'hui que sur la branche locale `travail-0023` : il faut le pousser sur `prep/iib-tirage-carte-v1` |
| `<<EMPREINTES_AMORCES_ET_LISTES_VOIE_A>>` | l'exécutante, avec les sha256 des deux amorces, de la liste v7 et de la liste de la course v2, à l'arbre final |
| `<<TESTS_ATTENDUS_ETALONNAGE_VOIE_A>>`, `<<TESTS_ATTENDUS_COURSE_VOIE_A>>` | l'exécutante, avec 311 et 313 annoncés, confirmés à l'arbre final après la vérification du correctif 0022 |
| `<<ENTROPIE_VOIE_A>>` | la mère, avec `SeedSequence().entropy` et la ligne de `registres/decisions.md` |
| `<<INSTANCES_INTOUCHABLES>>` | l'exécutante, avec l'inventaire en champs filtrés ; liste non vide |
| `<<CONFIG_VOIE_A_CHEMIN_ET_EMPREINTE>>` | l'exécutante, avec la configuration scellée (cinq clés seulement) et sa comparaison clé par clé, vérifiées par la mère |
| `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>` | l'exécutante, avec l'enfant direct du commit du code revu, vérifié par la mère |
| `<<CORRECTIF_0024_…>>`, si la mère crée ce champ plutôt que d'élargir celui du 0023 | comme ci-dessus |

Avant le scellement, il faut aussi relever l'empreinte du devis dans son compagnon (§ 6), et relire l'additif dans sa version neuve, comme le prévoit la règle des corrections. Note : pendant ce travail, le disque de `/tmp` s'est rempli. J'ai retiré mon propre arbre de travail (`cl-b3`) ; rien d'autre n'a été touché.

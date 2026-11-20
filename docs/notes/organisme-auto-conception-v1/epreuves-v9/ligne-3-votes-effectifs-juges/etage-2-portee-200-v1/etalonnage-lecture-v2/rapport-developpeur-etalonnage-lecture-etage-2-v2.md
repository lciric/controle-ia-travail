# Rapport du développeur — étalonnage et lecture unique de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v2

Pièce d'instrument (classe B), écrite le 2026-11-20 par le même développeur, modèle O, sur le même mandat
(`mandat-developpeur-etalonnage-lecture-etage-2-v1.md`, `b432ce7e…`, en-tête compris). La v1 (dossier
`etalonnage-lecture-v1/`, table `28d73687…`) est gardée sans modification (règle R12) ; son rapport (`e1b82cd0…`) vaut pour
tout ce que celui-ci ne change pas.

Sources de la v2 :
- la contre-lecture du modèle S, `…/etage-2-portee-200-v1/etalonnage-lecture-v1/contre-lecture-v1/contre-lecture-etalonnage-lecture-etage-2-v1.md`
  (`c1dbd14e0985a4cee83739057228693c70dee5f265b60c0ec2ad4023b00ce09e`, recalculée), avec son `correction-n1-lire_ligne_3_v1.diff`
  et `essai_correction_n1_v1.py` (lus en entier) ;
- les décisions de la mère de 15:55Z et 16:01Z, transmises par la coordination ; je ne les ai lues que par elle.

**Aucun verdict réel n'existe, aucun n'a été lu : tout a été éprouvé sur des verdicts factices.** Aucune commande sur un
chemin sous `archives-reponses-modeles/`. Aucun appel, aucune clé, aucun réseau, aucune dépense. Aucune écriture dans le dépôt
ni dans le clone ; aucun commit. Aucun refus de permission, de classifieur ou de garde.

## 1. Ce qui change, décision par décision

| décision | où | quoi |
|---|---|---|
| (1) témoin « complet » = cinq rendus **obtenus** | `lire_ligne_3_v2.py` | le différentiel du contre-lecteur, porté **à la lettre** (quatre lieux : `tableaux_complets` rend `obtenu` ; `complet = obtenu.all(axis=1)` ; `complet_tentes` ; deux comptes et la définition au rapport). Les deux essais du contre-lecteur sont repris dans les essais v2 (`test_v2_un_rendu_absent_n_est_pas_obtenu_donc_pas_complet`, `test_v2_cas_sain_sans_absent_les_deux_comptes_sont_egaux`). `bloc_A` reste « deux premiers rendus tentés » (un absent vaut rejet, l. 155). |
| (2) cartes tombées sur `reserves_tenues`, moitié « étalonnage » | `etalonner_ligne_3_v2.py` | `lire_construction` : nature du fragment « voisins » de chaque témoin (`conforme_non_citant`, `conforme_citant`, `fautif`), tirée du **journal de construction** (fragments employés par identifiant) et du **fichier de fragments** du générateur v3 (conformes par catégorie avec leur citation ; fautifs avec leur catégorie), tous deux scellés ; refus nommés (journal d'autres fragments, schéma, témoin du journal différent de la banque, fragment « voisins » inconnu). `compter_reserves_tenues` : premier rendu, verdict présent, item `reserves_tenues` rendu faux, **par juge**, avec marges **par classe, par citation, par item planté, par nature du fragment « voisins »**, et **strates croisées** (classe × citation × item × voisins) ; verdicts absents exclus et comptés. Clé **`cartes_tombees_sur_reserves_tenues_premier_rendu`** de la pièce scellée, avec la phrase de la décision (« un fragment « voisins » conforme non citant n'est pas une citation de travail publié »). Rapporté, sans seuil, sans effet sur les poids. Quatre arguments neufs : `--journal-construction`, `--journal-construction-sha`, `--fragments`, `--fragments-sha`. |
| (3) forme de l'audit de symétrie | ce rapport, § 3 | les trois précisions du § 5 de la contre-lecture. |
| (4) phrase fausse ; durcissement `dossier` | ce rapport, § 4 n° 13 ; `etalonner_ligne_3_v2.py`, `lire_ligne_3_v2.py` | la pièce porte `"dossier": str(Path(dossier).resolve())` ; la lecture refuse une pièce dont le dossier n'est pas celui où elle lit (« la pièce porte un autre dossier que celui de la lecture »). |
| (5) silence n° 17 | § 4 | nommé, gardé. |
| 16:01Z : additif 5 | les deux programmes | constante `ADDITIF_5_V2` = `prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md`, **`581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c`** (version scellée sur `main`), portée aux manifestes. Vérifiée par moi : `git show origin/main:…` redirigé, empreinte égale à son compagnon de `main` ; `diff` avec la copie de branche (`e193bc4e…`) : la ligne 25 seule (commit `cce6f234…` écrit au scellement). |

Rien d'autre ne change : poids, seuils, règles, ρ d'étalonnage ; estimateur, rééchantillonnage, table en issue B, gardes de la
v1. Noms de sortie en v2 (`etalonnage-etage-2-ligne-3-v2.json`, `manifeste-etalonnage-etage-2-ligne-3-v2.json`,
`rapport-lecture-etage-2-ligne-3-v2.json`, `manifeste-lecture-etage-2-ligne-3-v2.json`). La lecture v2 importe
`etalonner_ligne_3_v2.py` par empreinte (`a67ebed3…`).

**Différentiels v1 → v2** (`diff -u`, dans ce dossier, avec compagnons) : `differentiel-etalonner-v1-v2.diff`
(`3ace25b0…`), `differentiel-lire-v1-v2.diff` (`d8cad906…`), `differentiel-essais-v1-v2.diff` (`a0380318…`).

## 2. Essais

Commande (sur ma copie) :

`env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-etalonnage-lecture-etage-2/etalonnage-lecture-v2 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_etalonnage_lecture_ligne_3_v2.py`

Résultat : **44 passed in 52.75s**, en tâche de fond, au premier passage, sur `a67ebed3…`, `ee67e246…`, `225840dd…`.
44 = les 37 de la v1, plus 7 :
- les 2 essais du contre-lecteur (correction 1) ; le premier échouait sur la v1 (`assert 40 == 39`, selon la
  contre-lecture) ;
- `test_v2_reserves_tenues_plant_sur_les_voisins_conformes_non_citants` (**cas sain**). Juges parfaits ; le juge Opus rend
  `reserves_tenues` faux, au premier rendu, sur tous les bons dont le fragment « voisins » est conforme non citant. Les
  comptes de la pièce scellée égalent, strate par strate, un recalcul indépendant tiré du monde planté. Les marges sont
  justes : chez Opus, bons non citants plus mauvais de l'item `reserves_tenues` ; chez Argon, ces mauvais seuls. Les verdicts
  présents font 100 ;
- `test_v2_reserves_tenues_plant_ailleurs_ne_tombe_pas_chez_les_non_citants` (**artefact**). Le même plant, porté sur les
  bons au fragment « voisins » **citant** : les cartes tombent dans cette strate et la strate des bons non citants reste à 0 ;
  recalcul égal ;
- `test_v2_reserves_tenues_ne_lit_que_la_moitie_etalonnage` (**artefact**). Un plant sur la seule moitié « lecture » ne
  change aucun compte ;
- `test_v2_journal_ou_fragments_hors_forme_refus`. Refus pour : un journal qui nomme d'autres fragments ; un fragment
  « voisins » inconnu ; un témoin du journal différent de la banque ; un journal d'une autre empreinte. Aucune sortie n'est
  écrite ;
- `test_v2_piece_liee_a_son_dossier`. Le même étalonnage dans deux dossiers rend deux empreintes ; une pièce recopiée dans
  un autre dossier, citée par un audit, est refusée par la lecture.

Trop propre (R4) ? Chaque essai du comptage exige l'égalité exacte, strate par strate, avec un recalcul fait hors du programme
(`attendu_reserves`), et un compte non nul dans la strate visée (`bons_vn > 0`). Le monde factice est au format du générateur
v3 (`valider_fragments`, `geste_composer`), mais ce n'est pas un vrai fichier de fragments : seules les catégories et les
citations des fragments « voisins » y comptent.

## 3. Forme de l'audit de symétrie (décision n° 3 : agent neuf ; contrôle non tenu = arrêt)

Il suffit de ce paragraphe pour écrire l'audit sans lire le code.

**Qui, quand.** Un agent neuf, après l'étalonnage scellé et avant la lecture (l. 305 (10), 347 à 350). Il ne lit **aucun**
verdict de la moitié « lecture ». Les déclencheurs « trop propre » et « trop sale » (l. 348, 349) **ne sont pas dans
l'audit** : ils portent sur les résultats et sont calculés par la lecture.

**Fichier.** Un objet JSON en UTF-8, à n'importe quel chemin, passé à la lecture par `--audit CHEMIN --audit-sha HEX`. Il
est scellé par un compagnon `CHEMIN.sha256` au format de `sha256sum` : une ligne `HEX␣␣nom-du-fichier` (deux espaces), dont
le premier mot est l'empreinte des octets du fichier. Le plus simple est `env -C DOSSIER sha256sum F > DOSSIER/F.sha256`.

**Clés exigées** (des clés en plus au niveau supérieur sont tolérées, par exemple `auteur`, `notes`) :

| clé | valeur |
|---|---|
| `piece` | la chaîne exacte `audit de symétrie (règle R4), étage 2, ligne 3` |
| `etalonnage_sha256` | l'empreinte de la pièce d'étalonnage scellée, `DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v2.json` (son compagnon), passée à la lecture en `--etalonnage-sha` ; l'audit s'écrit donc **après** l'étalonnage |
| `banque_sha256` | l'empreinte de la banque scellée (`--banque-sha`) |
| `rapport_execution_sha256` | l'empreinte de `DEPOT/rapport-execution-K.json` du code d'appel (`--rapport-execution-sha`) |
| `controles` | un objet aux **cinq clés exactement** ci-dessous, ni plus ni moins ; chaque valeur est `"tenu"` ou `"non tenu"`. **Une seule valeur autre que `"tenu"` arrête la lecture** (la mère est saisie). |

**Les cinq contrôles, et leur sens contre la l. 350** (« relire par programme… ») :

| clé | ce qu'il faut avoir relu par programme pour écrire `"tenu"` |
|---|---|
| `verite_non_servie` | « que la vérité n'a pas été servie (aucune étiquette, aucun identifiant de classe dans le texte servi) ». Sur les entrées servies du dépôt (`DEPOT/entrees-servies/envoi-NNNNN.json`) : ni le mot « classe », ni le nom d'un item de la consigne, ni un identifiant interne de témoin. |
| `consigne_servie_empreinte_attendue` | « que la consigne servie a l'empreinte attendue ». Le champ `consigne_servie_sha256` de chaque `manifeste-execution-K.json` vaut `b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167`. |
| `lecteur_rend_absent_pour_illisible` | « que le lecteur de verdicts rend bien « absent » pour une réponse illisible ». `lire_verdict` de `juges_croises_v53.py` rend `None` sur une réponse sans bloc JSON ou à quatre clés. Dans le dépôt, toute réponse brute illisible a un `verdict` nul. |
| `appariement_temoin_verdict` | « que l'appariement témoin-verdict tient (clés d'anonymisation) ». Chaque identifiant opaque du journal du compteur n'est servi qu'une fois. Chaque engagement nomme un rendu du plan (`témoin|juge|rN`). Chaque ligne des fichiers de verdicts renvoie, par `envois` et `reponse_sha256`, à la réponse brute de ce rendu. |
| `juges_scriptes_parfait_et_hasard` | « rejouer le juge scripté parfait et le juge scripté au hasard sur la banque ». Le juge parfait rend une erreur équilibrée de 0, le juge au hasard une erreur équilibrée voisine de 0,5, contre la vérité de la banque. |

**Exemple** (empreintes de forme seulement) :

```json
{
 "piece": "audit de symétrie (règle R4), étage 2, ligne 3",
 "etalonnage_sha256": "1111111111111111111111111111111111111111111111111111111111111111",
 "banque_sha256": "2222222222222222222222222222222222222222222222222222222222222222",
 "rapport_execution_sha256": "3333333333333333333333333333333333333333333333333333333333333333",
 "controles": {
  "verite_non_servie": "tenu",
  "consigne_servie_empreinte_attendue": "tenu",
  "lecteur_rend_absent_pour_illisible": "tenu",
  "appariement_temoin_verdict": "tenu",
  "juges_scriptes_parfait_et_hasard": "tenu"
 },
 "auteur": "agent neuf (règle R4)"
}
```

et son compagnon `audit-symetrie.json.sha256` : `<empreinte des octets>  audit-symetrie.json`.

## 4. Silences (numérotation du rapport v1 ; état après les décisions)

- **n° 1 — tranché** (mère, 15:55Z) : complet = cinq rendus obtenus ; le compte des tentés est rapporté à côté.
- **n° 2 — gardé** : « non concluant par manque de témoins » sous 40 complets en lecture, quelle qu'en soit la cause ; la cause
  est écrite.
- **n° 3 — gardé** : audit par un agent neuf ; un contrôle non tenu arrête la lecture ; forme au § 3.
- n° 4 à 11, 14 à 16 : inchangés (rapport v1, § 6 ; jugés justes par la contre-lecture).
- **n° 12 de la mère (n° 13 du rapport v1) — corrigé et gardé.** La phrase de la v1 « une relecture dans un autre dossier
  demande un étalonnage et un audit neufs » était **fausse**. Dans la v1, la pièce d'étalonnage est déterministe et ne
  contient aucun chemin : rejouée dans un autre dossier, elle a la même empreinte, et l'audit déjà scellé reste valable.
  Seul le DOSSIER que nomme l'additif empêchait alors la rejouée. **Dans la v2**, la pièce porte son dossier (chemin absolu
  résolu) : une pièce rejouée ailleurs n'a plus la même empreinte, l'audit qui citait la première ne vaut pas pour elle, et
  la lecture refuse une pièce dont le dossier n'est pas le sien. Une relecture complète reste possible avec un étalonnage
  **et** un audit neufs, écrits dans un dossier neuf. Le programme ne peut pas l'empêcher seul : **l'additif doit nommer
  DOSSIER, un seul chemin absolu**.
- **n° 17 — nommé, gardé** (mère, 16:01Z). Le ρ de « ρ′ − ρ » n'est pas le ρ rapporté comme mesure :
  - pour l'écart ρ′ − ρ, ρ = `rho_paire(S, 0, 1)` sur les témoins complets (cinq rendus obtenus) des deux moitiés, et
    ρ′ = `rho_paire` des deux premiers rendus du même juge, sur les mêmes témoins (même rééchantillonnage) ;
  - le ρ rapporté, avec votes effectifs et banc avec prise, est `rho_moyenne` sur les témoins du bloc A.

  À deux juges, la ρ de paire est le pendant exact de ρ′. Le recalcul du contre-lecteur les donne à 4e-5 l'une de l'autre sur
  son plant. Le texte (l. 157, 159, 293) ne dit pas laquelle sert à l'écart : **à nommer dans l'additif**.
- **n° 18 (neuf, v2)** — nature du fragment « voisins ». Chaque témoin a un fragment « voisins » (générateur v3, un fragment
  par catégorie), rangé dans l'une de trois natures : conforme non citant, conforme citant, fautif. Un fragment piège
  (« reprise assumée ») est rangé comme les autres conformes, selon sa citation. Le comptage lit **tous** les verdicts
  présents du premier rendu de la moitié « étalonnage », non les seuls témoins qui servent aux poids. Le champ
  `fragments_sha256` de la banque n'est pas comparé : la comparaison porte sur le journal, témoin par témoin.

## 5. Ce que l'additif de code de l'étage 2 devra porter (pour ces programmes)

- **Fichiers et empreintes** (table `table-empreintes-etalonnage-lecture-v2.txt`), tous trois dans le même dossier :
  - `etalonner_ligne_3_v2.py` `a67ebed377ee70fe56163ded7b3fc42cdbd319c0f265b12d68bbbf394e15b92c` ;
  - `lire_ligne_3_v2.py` `ee67e246c1c5f8cb7a32240cd6f9a5083c37efed24b1808b0d2d11772fad584f` ;
  - `essais_etalonnage_lecture_ligne_3_v2.py` `225840dde800f13225727ff52ebc4ae65d194dd54270002d1bae399ada2e7e1d` ;
  - ce rapport, et le commit qui les verse.
- **Dépendances épinglées** :
  - le banc v4 (`L3/code-portee-200-v4/banc_juges_scriptes_ligne_3_v4.py`, `79865552…`), au même chemin ;
  - l'additif 5 scellé (`581e97e5…`), cité ;
  - pour les essais seulement : le code d'appel v4 (`082d19d6…`) et le clone de l'orchestrateur (`a41b7b50…`).
- **Commande des essais** (§ 2) ; attendu : **44 passés**.
- **Racine 2026111936 autorisée** pour `lire_ligne_3_v2.py` seul, par l'additif lui-même : chemin et empreinte passés en
  `--autorisation-additif` et `--empreinte-additif`. Clés gelées : `rho_entre_juges_bloc_A` 1, `ecarts_rho_prime_moins_rho`
  2, `comparaisons_bloc_A` 3, `comparaisons_bras_R` 4, `lecture_par_colonne` 5. 2 000 tirages ;
  `numpy.random.SeedSequence(racine, spawn_key=(clé,))`, numpy ≥ 1.25. L'étalonnage ne dérive aucune graine.
- **DOSSIER** : un seul chemin absolu, nommé.
- **Ordre** :
  1. dépôt scellé des verdicts par le code d'appel ;
  2. étalonnage, une fois :
     `python3 -I -B etalonner_ligne_3_v2.py --banque BANQUE.json --banque-sha HEX --verdicts-etalonnage DEPOT/verdicts-moitie-etalonnage-execution-K.json --verdicts-etalonnage-sha HEX --journal-construction JOURNAL.json --journal-construction-sha HEX --fragments FRAGMENTS.json --fragments-sha HEX --dossier DOSSIER`
     L'empreinte des verdicts d'étalonnage est celle des `depots` du rapport d'exécution K. Le journal de construction et
     le fichier de fragments sont ceux de la banque scellée (générateur v3, `journal-construction-ligne-3-v1.json` et le
     fichier passé à `--fragments` à la composition) ;
  3. audit de symétrie, au § 3, par un agent neuf, scellé ;
  4. lecture unique :
     `python3 -I -B lire_ligne_3_v2.py --banque BANQUE.json --banque-sha HEX --depot DEPOT --execution K --rapport-execution-sha HEX --etalonnage DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v2.json --etalonnage-sha HEX --audit AUDIT.json --audit-sha HEX --autorisation-additif CHEMIN --empreinte-additif HEX`
  5. verdict par un agent neuf (R13).

  Codes : 0 pièce écrite ; 2 refus ou arrêt nommé.
- **Constantes à comparer au texte** :
  - celles de la v1 (issue B ; 40 ; [0,05 ; 0,45] ; 0,25 ; 1/10 ; 1/2 ; 0,10 ; 0,05 ; 0,02 ; 0,40 ; −0,2 ; 2 000 ; 200) ;
  - la définition du complet (obtenus) ;
  - le n° 17 ;
  - la clé du comptage `reserves_tenues`.

## 6. Écarts

1. Fichiers tirés de `origin/main` par `git show` redirigé dans mon dossier, hors du sous-dossier `etalonnage-lecture-v2/` :
   l'additif 5 v2 scellé et son compagnon. Ajoutés à ceux de la v1 (additif 3, verdict de portée).
2. Fichiers v1 copiés par `cp` vers `etalonnage-lecture-v2/` sous leurs noms v2, puis modifiés ; dossier v2 créé par `mkdir`.
   Un premier essai de copie a échoué, le dossier n'existant pas encore.
3. Lecture d'une partie du générateur v3 (l. 82 à 126, 560 à 819) pour la forme du fichier de fragments et la composition :
   hors de « ce qui fait foi » de la v1, mais nécessaire à la décision (2).
4. Les essais écrivent dans le dossier temporaire de pytest, hors de mon dossier (comme en v1).
5. Aucun refus de permission, de classifieur ou de garde.

Développeur, modèle O.

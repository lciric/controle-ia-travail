# Rapport du rédacteur-développeur — étape F de R1 v4, version 3 : brouillon 3 (six couples de la contre-lecture 2), comptes de `exiger_code_cite`, commandes de la mère corrigées (P1) — v3

Rapport **additif** et court : il complète `rapport-developpeur-gardes-analyses-v2.md`
(`ff6cc2f5cd755643eeddd65eb2dd6c304a131ff5b39034b183e0288ea6faadac`) et `rapport-developpeur-gardes-analyses-v1.md` (`879d2e93…`), qui
restent valables pour tout ce qui n'est pas repris ici. **Aucun code n'a changé** (la contre-lecture 2 n'en exigeait
aucun) ; seules les commandes de la section 5 sont réécrites selon P1.

- **Qui, quand** : troisième rédacteur neuf (sous-agent, T2 bis de la fille 7), le 5 novembre 2026, de 20:18 à
  20:29 UTC (`date -u`). Je n'ai écrit ni le code v8/v9/v5, ni le brouillon 2, ni les contre-lectures 1 et 2, ni
  les rapports v1 et v2.
- **Où** : arbre `/home/user/wt/canal` (branche `canal/conv-audit-n04`, tête `bdcf4027` au départ) ; clone de `main`
  (`67de4f92`) en lecture seule. Fichiers neufs seulement (R12) ; aucun fichier existant modifié ; aucun `.sha256` ;
  rien sous `donnees/`, `diag/`, `calcul/` ; aucune lecture de `runs/` ; aucune commande décisive ; aucun `.npz` ;
  aucune clé, aucune dépense, aucun modèle ; aucun réseau hors la poussée de cette branche.
- **Empreintes vérifiées avant d'écrire** (`sha256sum -c *.sha256` dans
  `docs/notes/runs-r1-r2-r4-v1/etape-F-v1/contre-lecture-v2/` de `main` : trois « OK ») : contre-lecture 2
  `24d8c769bfacf132…` (verdict « scellable après couples »), couples `65b802ad6ee3f74fc528b1d4b23d9ea809a0dfe0eedd28cc54dd8554ecb0ac1c`
  (six couples, liste nue « ancien → nouveau »), corrections de procédure `6b36d6a20df1a05c…` (P1 à P4) ; brouillon 2
  `465b5334c4f47f6a1db5e3d757a46420087f0f3219fa3eac858653d048b3000b` (égal au brief et à la contre-lecture 2).

## 1. Livrables (chemins et sha256, tous neufs)

| fichier | sha256 | rôle |
|---|---|---|
| `prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon3.md` | `81a04e7b9d0dc075bec03371a64f96c3c70fa1c540b7c32c2bd2486b953e6110` | brouillon 2 + les six couples, dans l'ordre, par script |
| `brouillons/etape-F-r1-v4-v1/appliquer-couples-v3.py` | `8f58d5ab4345694c78d887bd0e9eac2f5b121dd950f8e8b9b6b8159e5fd954a0` | script : méthode de la v2 (chaque « ancien » exactement une fois au moment de son application, arrêt sinon, rien d'écrasé) ; accepte la liste nue de la contre-lecture 2 (identifiants K-1 à K-6) ; journal avec empreintes des entrées, ligne de chaque couple, empreinte de la sortie, compte des marqueurs |
| `brouillons/etape-F-r1-v4-v1/couples-contre-lecture-addendum-gardes-v2.json` | `65b802ad6ee3f74fc528b1d4b23d9ea809a0dfe0eedd28cc54dd8554ecb0ac1c` | copie à l'octet des six couples de `main` |
| `brouillons/etape-F-r1-v4-v1/journal-couples-v3.md` | `2c504a97286c544f26ce79c03f80c0288e09c93f3a4ce32307e88e02786cc524` | journal du script (6 opérations, 1 occurrence chacune, lignes 115, 122, 16, 443, 184, 202 de l'entrée au moment de l'application ; sortie `81a04e7b…` ; marqueurs : 2 occurrences, 2 distincts) |
| `brouillons/etape-F-r1-v4-v1/rapport-developpeur-gardes-analyses-v3.md` | (ce fichier) | |

Commande qui a produit le brouillon 3 (depuis la racine de l'arbre) :
`python3 -I brouillons/etape-F-r1-v4-v1/appliquer-couples-v3.py prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon2.md
brouillons/etape-F-r1-v4-v1/couples-contre-lecture-addendum-gardes-v2.json prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon3.md
brouillons/etape-F-r1-v4-v1/journal-couples-v3.md` ; reproductible à l'octet (`65b802ad…` + `465b5334…` → `81a04e7b…`).
`diff` brouillon 2 → brouillon 3 : six zones, aucune autre ligne ; aucune empreinte, aucune table gelée, aucun critère
de lecture touché.

## 2. Traitement des six couples (tous acceptés, appliqués tels quels, dans l'ordre)

| couple | point de la contre-lecture 2 | ligne (entrée) | ce qu'il corrige |
|---|---|---|---|
| K-1 | 4 a, 5 | 115 | Plan, point 0.0 : « Contre-lecture 2 » écrite dans le brouillon final ; **deux** marqueurs restants (« Commit du code », « Écart déclaré », ce dernier remplacé par la référence du GO de Lazar) |
| K-2 | 4 a, 5 | 122 | Plan, point 0.b : remplacer les **deux** marqueurs (commit cité, GO de Lazar), `diff` : seules **ces deux lignes** diffèrent (cohérent avec la section « Marqueurs de gabarit » et la ligne `diff … # deux lignes` de la section 5) |
| K-3 | 4 b, 5 | 16 | En-tête, écart déclaré : la règle « second passage » **et, avec elle, la reprise « même code » après un arrêt technique** sont remplacées, pour la seule course v4, par le point 6 (second écart déclaré en tête) |
| K-4 | 4 b | 443 | Liste d'arrêt : « arrêt technique après le manifeste » devient un nœud de Lazar ; le code v8, v9 ou v5 refuse tout second passage sous l'addendum (code de fin 2) ; une reprise exigerait l'accord de Lazar, une version neuve du code et un addendum nouveau (écart à « même code », Plan, point 6) — fin de la contradiction avec le point 6 (C12) et le code |
| K-5 | 4 c | 184 | Plan, point 1, sortie de la secondaire (code v5) : nomme `lien_au_preenregistrement.addendum` **et** `passages` (K2) |
| K-6 | 4 c | 202 | Plan, point 1, sortie de la lecture par épisode (code v9) : nomme `addendum`, `passages` (K2) **et** `principale.sous_addendum` (K3), que le code écrit et que le verdict (point 8) lit |

Décision prise seul, à contre-lire si la mère le souhaite : les six couples ont été appliqués **à l'octet**, sans
réajuster le retour à la ligne des paragraphes touchés (quelques lignes dépassent la largeur usuelle, comme déjà 201
lignes du brouillon 2) ; aucune phrase de ma main dans le brouillon 3.

## 3. Marqueurs, `problemes`, listes fermées (`exiger_code_cite`)

- Marqueurs du brouillon 3 (motif `<<[A-Z0-9_]+>>`, compte du script et `grep -c '<<'`) : exactement `<<COMMIT_CODE>>`
  et `<<GO_LAZAR_SECOND_PASSAGE>>`, **une fois chacun** (2 occurrences, 2 distincts).
- `controle_ia.prereg.problemes` sur le brouillon 3 : exactement les deux lignes attendues d'un brouillon, identiques à
  celles du brouillon 2 (« contre-lecture 2 sans ses deux empreintes (brouillon relu et rapport) » ; « marqueurs de
  gabarit restants : <<COMMIT_CODE>>, <<GO_LAZAR_SECOND_PASSAGE>> »).
- Listes fermées vérifiées par le code lui-même, sur le texte du brouillon 3 (et, témoin, du brouillon 2), données du
  dépôt seulement (aucun `.npz`, aucune commande décisive), commande exacte depuis la racine de l'arbre, environnement
  `.venv` du dépôt principal :
  ```
  PYTHONPATH=src:tests python -c "
  from controle_ia.analyse_principale_r1_r2 import lecture_v8 as A, lecture_v9 as B
  from controle_ia.analyse_blanche_noire import lecture_v5 as C
  t = open('prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon3.md', encoding='utf-8').read()
  print([len(m.exiger_code_cite(t)['fichiers']) for m in (A, B, C)])"
  ```
  Résultat : **`[22, 33, 31]`** sur le brouillon 3 ; **`[22, 33, 31]`** sur le brouillon 2 (témoin). Aucun nombre n'a
  changé ; aucune liste fermée ni aucune empreinte de constantes n'est touchée par les couples.

## 4. Essais (R5) : comptes

Environnement gelé `.venv` du dépôt principal, `PYTHONPATH=src:tests`, `-p no:cacheprovider`, `nice -n 10`, une suite à
la fois sous `flock /home/user/wt/.pytest.lock` (`flock /home/user/wt/.pytest.lock timeout 900 nice -n 10 python -m
pytest -q -p no:cacheprovider <suite>` ; le verrou était tenu par un autre sous-agent : attentes comprises dans les
heures), données synthétiques seulement. Seules les trois suites neuves ont été rejouées (brief T2 bis) ; aucune
ancienne (comptes v2 : 114 réussis sur 114, non rejoués ici).

| fichier | essais | résultat | durée pytest | heures (UTC) |
|---|---|---|---|---|
| `tests/test_analyse_principale_r1_r2_v8.py` | 4 | réussis | 4,5 s | 20:19:39 → 20:22:46 (attente du verrou comprise) |
| `tests/test_analyse_par_episode_v9.py` | 3 | réussis | 5,4 s | 20:22:46 → 20:26:27 (idem) |
| `tests/test_analyse_blanche_noire_v5.py` | 4 | réussis | 20,1 s | 20:26:27 → 20:26:47 |

Essais neufs : **11 réussis sur 11**, comme au rapport v2 et à la contre-lecture 2 (le code n'a pas changé : empreintes
des onze fichiers de code et d'essais inchangées, section 1 du rapport v2).

## 5. Commandes exactes pour la mère (conv-audit), corrigées selon P1 (`corrections-procedure-v2.md`)

Les étapes 1 à 4 de la section 5 du rapport v2 restent telles quelles (commit cité, scellement, arbre séparé, essais
101 attendus, récupération par refspec, fiches), avec `<N>` = 3 si le brouillon 3 est le brouillon final (sinon le
numéro du brouillon final). **Préalables inchangés et impératifs** : contre-lecture 2 faite (verdict « scellable après
couples ») ; **GO de Lazar sur les deux écarts déclarés** (second passage borné par K2 ; reprise « même code » après un
arrêt technique, K-3 et K-4) **et sur l'arrêt neuf K3** (P4, sens prudent) ; empreinte du brouillon final au registre,
poussée ; **réception v4 conforme** (C6) : `verifier_reception_r1_v4_v1.py` en code 0, recalcul de la table égal à
l'octet (fiche v4, section 7), consignée au registre avec ce qui a été vu (fiche v4, section 6) — sans cela, aucune
commande décisive.

Préalable P2 (note, après la récupération, avant tout lancement) : les manifestes du rejeu et de la réparation entrent
sous `runs/` et sont lus par K2. Compter seulement, sans rien afficher d'autre, leurs occurrences des trois chemins des
textes, des trois empreintes des textes et du chemin de l'addendum (`grep -c -F '<motif>' runs/<run>/manifeste.json`,
sept motifs par manifeste) ; un compte non nul arrêterait les trois lectures en code 2 avant tout manifeste (arrêt sans
dommage, mais nœud de Lazar) : le savoir avant de lancer.

**Étape 5, commandes décisives, lancées comme un script** (`bash -u`), depuis la racine de l'arbre séparé, arbre propre,
au commit du scellement, sans autre manifeste ajouté ; **sorties standard et d'erreur redirigées vers un journal non
affiché ; seul le code de fin est lu** ; chaque commande décisive **conditionnée au code de fin de la précédente** (test
explicite, `exit` sur code non nul : la lecture par épisode ne part jamais après une principale arrêtée, la secondaire
jamais après une lecture par épisode arrêtée, et aucun passage sous l'addendum n'est consommé à tort) ; sur code non
nul, la seule ligne lue du journal est la ligne `ARRÊT` (elle ne porte aucune valeur) ; un code non nul **sans** ligne
`ARRÊT` (exception non prévue) : rien d'autre n'est lu du journal, signaler à Lazar ; journal scellé et committé avec les
sorties ; **aucune issue lue avant que les trois sorties soient committées et poussées** (C7) :

```
#!/bin/bash -u
set -u
mkdir -p journaux
lire_arret() {   # $1 : code de fin ; $2 : journal ; n'affiche que le code et, sur arrêt, la seule ligne ARRÊT
  echo "code de fin : $1"
  if [ "$1" -ne 0 ]; then
    grep -m1 '^ARRÊT' "$2" || echo "code non nul sans ligne ARRÊT (exception non prévue) : rien d'autre n'est lu, signaler à Lazar"
    echo "arrêt, nœud de Lazar" ; exit "$1"
  fi
}

# 1. Analyse principale (code v8)
R1=$(date -u +%Y%m%d-%H%M%S)-analyse-principale-r1-r2-v1
PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v8 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --run-analyse $R1 --prereg prereg/analyse-principale-r1-r2-v1.md > journaux/$R1.log 2>&1
c=$? ; lire_arret "$c" journaux/$R1.log
PYTHONPATH=src python -m controle_ia.scellement sceller journaux/$R1.log
git add runs/$R1 diag/$R1 journaux/$R1.log journaux/$R1.log.sha256 && git commit -q -m "Analyse principale R1-R2, course v4 (code v8)"

# 2. Lecture par épisode (code v9 ; K3 exige la principale v8 sous l'addendum et le même rejeu) — seulement si 1 a rendu 0
R2=$(date -u +%Y%m%d-%H%M%S)-analyse-par-episode-v1
PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_principale_r1_r2.lecture_v9 --fiche prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json --principale diag/$R1/analyse-principale-r1-r2-v1.json --run-analyse $R2 --prereg prereg/analyse-par-episode-v1.md > journaux/$R2.log 2>&1
c=$? ; lire_arret "$c" journaux/$R2.log
PYTHONPATH=src python -m controle_ia.scellement sceller journaux/$R2.log
git add runs/$R2 diag/$R2 journaux/$R2.log journaux/$R2.log.sha256 && git commit -q -m "Lecture par épisode R1-R2, course v4 (code v9)"

# 3. Analyse secondaire blanche-noire (code v5) — seulement si 2 a rendu 0
R3=$(date -u +%Y%m%d-%H%M%S)-analyse-blanche-noire-v3
PYTHONPATH=src nice -n 10 python -m controle_ia.analyse_blanche_noire.lecture_v5 --fiche prereg/fiche-reception-blanche-noire-v3-relance-v4.json --run-analyse $R3 --prereg prereg/analyse-blanche-noire-v3.md > journaux/$R3.log 2>&1
c=$? ; lire_arret "$c" journaux/$R3.log
PYTHONPATH=src python -m controle_ia.scellement sceller journaux/$R3.log
git add runs/$R3 diag/$R3 journaux/$R3.log journaux/$R3.log.sha256 && git commit -q -m "Analyse secondaire R1-R2, course v4 (code v5)"

git push origin HEAD:refs/heads/analyses-r1-v4
```

Codes de fin : 0 continuer ; 2 passage hors liste close (K2), nœud de Lazar ; 1 autre garde (ou exception non prévue,
sans ligne `ARRÊT`). Sur un arrêt, le script s'arrête avant le scellement et le commit de l'étape arrêtée : le journal
de l'étape arrêtée (une ligne `ARRÊT`, ou une trace sans valeur de résultat) et un éventuel manifeste sous `runs/` restent
sur disque pour le nœud de Lazar ; rien n'en est lu d'autre ; les étapes commises avant l'arrêt sont poussées à part,
sur sa décision. Le squelette de ce script (fonction `lire_arret`, enchaînement, redirections) a été éprouvé sur des
commandes jouets hors dépôt : cas sain (trois étapes, code 0) ; principale en code 2 avec ligne `ARRÊT` (seule cette
ligne affichée, lecture par épisode jamais lancée, code 2 rendu) ; lecture par épisode en code 1 sans ligne `ARRÊT`
(phrase « exception non prévue », rien d'autre lu, secondaire jamais lancée, code 1 rendu). Les trois commandes
décisives elles-mêmes n'ont pas été lancées (interdit).

Puis, comme au rapport v2 : les journaux ne contiennent que `{"issue": …}` sur succès et ne sont ouverts qu'après la
poussée des trois sorties ; `git merge` (jamais de rebasage) dans la branche de travail, poussée ; verdict R13 par un
sous-agent neuf, qui lit aussi `reception_v4`, `lien_au_preenregistrement.passages` (dont `toleres` contre la liste
close) et `principale.sous_addendum`.

## 6. Trois risques

1. **Les couples K-3 et K-4 élargissent la déclaration d'écart, pas l'écart lui-même** : le brouillon 3 déclare désormais
   deux écarts aux textes scellés (second passage ; reprise « même code »). Si Lazar n'accorde que le premier, le
   brouillon 3 n'est pas scellable tel quel : la liste d'arrêt (K-4) devrait alors revenir à une forme compatible avec
   son GO, par un brouillon 4 (R12), jamais par retouche. La demande de GO doit nommer les deux écarts et l'arrêt neuf K3
   (P4).
2. **Script de la section 5 non joué pour de vrai** : seul le squelette (enchaînement, codes, redirections) est éprouvé
   sur des commandes jouets ; les noms des fiches de réception de la course v4 (`…-relance-v4.json`) et le chemin
   `diag/$R1/analyse-principale-r1-r2-v1.json` viennent du rapport v2 et doivent être revérifiés par la mère contre les
   fiches réellement écrites à l'étape 4 ; une faute de chemin arrête en code 1 (garde), sans dommage, mais consomme une
   entrée de journal et un nœud.
3. **`problemes` attend l'entrée « Contre-lecture 2 » avec ses deux empreintes** : le brouillon final (celui qui porte
   `<<COMMIT_CODE>>` et `<<GO_LAZAR_SECOND_PASSAGE>>` seuls) doit encore écrire, dans la section « Contre-lecture »,
   l'entrée 2 (heure, lignée, consigne, brouillon relu `465b5334…`, rapport `24d8c769…`, couples `65b802ad…`, verdict,
   traitement : ce rapport) ; tant qu'elle n'y est pas, `problemes` rend trois lignes au lieu des deux marqueurs et le
   scellement est refusé à bon droit. Je ne l'ai pas écrite : le brief T2 bis ne demande que les six couples ; c'est un
   brouillon 4 (ou le brouillon final), par couples et script, après ce rapport.

## 7. Ce qui reste (à la mère)

Écrire l'entrée « Contre-lecture 2 » du brouillon final par couples (risque 3) ; demander le GO de Lazar en nommant les
deux écarts et K3 ; remplacer les deux marqueurs au scellement (étape 1 du rapport v2) ; réception v4 conforme ; P2 ;
puis la section 5 ci-dessus.

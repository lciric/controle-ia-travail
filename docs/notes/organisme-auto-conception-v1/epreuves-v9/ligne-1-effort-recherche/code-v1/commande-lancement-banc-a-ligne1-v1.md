# Banc A, ligne 1 — commande de lancement (code v1)

Préenregistrement qui fait foi : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`, sha256 `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9` (clé PREREG-ORGANISME-V9-LIGNE-1). Code : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/` (empreintes dans `rapport-developpeur-banc-a-v1.md`).

**À ne lancer qu'après** : la contre-lecture du code par l'autre modèle, la décision de la mère sur les choix que le préenregistrement ne fixe pas (rapport, § 4), le commit du code (le lanceur refuse un code non commis), et la décision de la mère sur le lieu de dépôt des journaux (préenregistrement, « Journal scellé », dernier point). Aucune dépense : processeur seul, aucun appel de modèle, aucune connexion (garde A2).

## Lancement (détachable, une seule commande)

Depuis la racine du dépôt de travail, sur le commit qui porte le code contre-lu, avec un dossier de sortie neuf hors du dépôt (`D`, nom au choix de la mère) :

```
D=/home/user/runs-banc-a-ligne1-v1 ; mkdir -p "$D" && cd /home/user/controle-ia-travail && setsid nohup env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/lancer_ligne1_v1.py tout --sortie "$D" --organisme /home/user/ideation-organism/orchestrator --processus 4 > "$D/lanceur.log" 2>&1 < /dev/null &
```

Ce que fait `tout`, dans l'ordre des gestes du préenregistrement (3 à 7), chaque étape dans un processus à part (session neuve), chacune scellant sa sortie avant la suivante :

1. `etalonner` → `$D/etalonnage/sortie-etalonnage-ligne1-v1.json` (scellé) : quatre forces, couple (s, c), portes (prise A9, cartes jugées par appel A15, audit du générateur A8), part des cartes indéterminées (mesure), T0 seul (A17). Une porte manquée : sortie écrite et scellée, puis arrêt nommé, retour à la mère. Une part d'indéterminées au-dessus de 20 % : dite en tête ; la course décisive refuse de partir (décision de la mère).
2. `decisive` → `$D/decisive/courses/` (un journal et une sortie brute par course et par classe, scellés) puis `$D/decisive/manifeste-course-decisive-ligne1-v1.json` (scellé ; garde A14 vérifiée).
3. `rejouer` → `$D/decisive/rejeu-ligne1-v1.json` (scellé) : toutes les décisions de tous les journaux décisifs et d'étalonnage rejouées depuis leurs seules entrées, comparées au bit près (A16) ; courses 0, 300 et 599 rejouées à part (audit de symétrie).
4. `analyser` → `$D/decisive/lecture-programme-ligne1-v1.json` (scellé) : garde A12, métriques, bornes, table de lecture par programme, prédictions, mentions, points de l'audit de symétrie, gardes A7 et A11.

Plafond (garde A13) : 43 200 secondes de calcul cumulées sur toutes les sessions (`$D/etat-lancement-ligne1-v1.json`). Au-delà : arrêt du groupe de processus de l'étape par son identifiant (règle R10), arrêt écrit dans `$D/arrets-ligne1-v1.jsonl`, rien n'est lu, code de sortie 13.

Durée prévue sur cette machine (4 cœurs, 4 processus) : environ 1 heure (fourchette 45 minutes à 1 heure 30) ; environ 3 heures 30 sur un cœur (rapport, § 6).

## Suivi, reprise, arrêt

- Suivi : `$D/lanceur.log`, `$D/journal-<étape>.log`, `$D/etat-lancement-ligne1-v1.json`.
- Reprise après une interruption : **la même commande, le même `D`**. Une étape déjà scellée n'est pas refaite ; dans une étape, une course déjà scellée n'est pas rejouée ; les fichiers provisoires (`.partiel`) d'une course interrompue sont effacés et la course est rejouée depuis ses graines (sorties identiques au bit près, essai 5). La durée cumulée continue de compter.
- Arrêt à la main : par identifiant de processus seulement (règle R10). Le lanceur écrit son identifiant dans `$D/pid-lanceur-ligne1-v1.txt`, et celui de l'étape en cours (chef de son groupe de processus, session neuve) dans `$D/pid-etape-ligne1-v1.txt` : `kill -TERM $(cat "$D/pid-lanceur-ligne1-v1.txt")` puis `kill -TERM -- -$(cat "$D/pid-etape-ligne1-v1.txt")`.

## Dépôt des journaux (après la chaîne, selon la décision de la mère sur le lieu)

```
env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/lancer_ligne1_v1.py empaqueter --sortie "$D" --vers <dossier neuf>
```

Morceaux `journaux-banc-a-ligne1-v1-partie-NNN.tar` de 90 Mo au plus (fichiers déjà compressés en xz), compagnons `.sha256`, manifeste scellé `manifeste-depot-ligne1-v1.json` (empreinte de chaque morceau et de chaque membre). Au-delà de 500 Mo compressés au total, le programme refuse (`DepotTropGros`) : arrêt et rapport avant de pousser. Taille prévue : environ 400 Mo (rapport, § 7).

## Étapes à la main (même effet, une à une)

`lancer_ligne1_v1.py etalonner|decisive|rejouer|analyser --sortie "$D" --organisme /home/user/ideation-organism/orchestrator --processus 4` ; le rejeu seul existe aussi comme programme à part : `rejouer_journal_ligne1_v1.py --dossier "$D/decisive/courses" --organisme … --courses 0,300,599 --sortie <fichier neuf>`.

## Essai de fumée (déjà fait, racines disjointes)

`lancer_ligne1_v1.py fumee --sortie <dossier neuf> --organisme /home/user/ideation-organism/orchestrator --processus 4` (racines 2026111990 à 2026111993 ; tailles minuscules ; n'imprime que des durées, des tailles, des comptes et des sceaux). Sortie : `sortie-fumee-banc-a-ligne1-v1.txt`.

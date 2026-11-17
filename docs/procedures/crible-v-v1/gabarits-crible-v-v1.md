# Gabarits du crible (v) — v1

Pièces que la mère écrit avant et pendant le feu, dans la forme exacte que le code relit (lanceur, programme machine, outil de la
session). Les valeurs entre chevrons sont lues par programme dans les pièces nommées, jamais tapées. Le **gabarit servi** aux
proposeurs n'est pas ici : c'est celui du pilote, inchangé (`e77d3041f7815b2c0579cbafdb2898ca8569fe61e6cb51b99a41c3724fc456a2`,
contrôlé par `exiger_gabarit` du lanceur avant tout appel).

## 1. Addendum d'empreintes (sous `prereg/`, scellé avant tout jeu ; il ne change rien d'autre au texte)

Une ligne par fichier du code, « empreinte, deux espaces, chemin » (le lanceur relit les quatre premiers ; le programme machine les
cinq ; l'outil de la session exige chaque fichier égal à son compagnon au commit du code) :

```
<sha256>  docs/procedures/crible-v-v1/crible_v_commun_v1.py
<sha256>  docs/procedures/crible-v-v1/lanceur_crible_v_v1.py
<sha256>  docs/procedures/crible-v-v1/mesure_crible_v_v1.py
<sha256>  docs/procedures/crible-v-v1/lire_crible_v_v1.py
<sha256>  docs/procedures/crible-v-v1/machine_crible_v_v1.py
<sha256>  docs/procedures/crible-v-v1/partie_a_crible_v_v1.py
```

Plus : l'empreinte de l'arbre de l'organisme (paquet `e3d83e47…`, tête 605e0f6), de la configuration v12 (`f69503dd…`), du
programme `mesure_pilote_v4.py` non employé (rappel), les graines des essais et des mutations (`(97, k)` : aucun tirage dans les essais
de ce dossier, qui ne tirent que les mondes d'essai par `generer` sur un secret d'essai public), et l'empreinte de la sortie gardée des
essais, du banc de mutations et de la répétition (rapport, § 1).

## 2. Fiche de lancement (`docs/procedures/crible-v-v1/fiche-lancement-crible-v-v1.json`, commitée au commit du code)

```json
{"version": "fiche-lancement-crible-v-v1",
 "texte": {"chemin": "prereg/<nom du texte qui fait foi>.md", "sha256": "<empreinte>"},
 "addendum": {"chemin": "prereg/<nom de l'addendum>.md", "sha256": "<empreinte>"},
 "duree_d_s": <D relevée, secondes>, "files": <M de la règle : 1 si D ≤ 12 400, 2 si D ≤ 15 400>}
```

## 3. Inscriptions sur `main` (fichier nommé par la mère ; le programme machine y cherche chaque chaîne)

- Barrière 1 : `secret <secret_sha256 lu dans secret-sha256.txt de la branche de sortie>` ; puis, après le feu,
  `phrase <empreinte du fichier de la phrase imprimée par feu-phrase>`.
- Barrière 2 : `H <fichier_mondes_sha256>`, `HC <certifiees_sha256>`, puis les 20 empreintes des mondes (une par ligne), lues dans
  `engagement-mondes.json` et `engagement-certifiees.json` de la branche de sortie.
- Barrière 3 : deux lignes exactes `D = <D> s` et `M = <M>` (les mêmes chaînes que celles passées à `feu-reel`).

## 4. Ligne du feu au registre des décisions

`| R-<N> | <date> | … feu du crible (v) : <KV1> (κv1), <KV2> (κv2), commit du code <CC 40 caractères>, étiquette crible-v-v1, image
python:3.13-bookworm, disque 20 Go, prix garde ≤ 0,15 USD/h (relu ≤ 0,17), échéance 17 h après l'impression, branches
calcul/crible-v-v1-sortie-v1 et calcul/crible-v-v1-entree-v1, opérateur … |` — forme courte passée aux commandes : `R-<N> <KV2>`.

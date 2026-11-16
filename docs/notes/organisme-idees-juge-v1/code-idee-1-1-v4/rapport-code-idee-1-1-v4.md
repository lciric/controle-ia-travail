# Rapport du développeur — code de l'idée 1.1, version 4 (corrections du contrôle du différentiel v2 → v3, `controle-differentiel-code-idee-1-1-v3.md`, `02f4a1d7b9070275422cfb02520c0aabaad4c6272817eb0791d6f185e888968b`)

- Auteur : le développeur des versions 1 à 3. Je n'ai écrit ni le texte ni les contre-lectures.
- Date (UTC) : du 2026-11-16 à 00:08 au 2026-11-16 à 00:36.
- Ce que je n'ai pas fait :
  - modifier un fichier v1, v2 ou v3 (R12) ;
  - committer ;
  - appeler le réseau ou un service payant ;
  - lancer le jeu, l'étape 0 ou une lecture de sortie de jeu ;
  - écrire quoi que ce soit sous `diag/`, `runs/` ou `donnees/`.
- Les essais jouent le banc sous des racines d'essai, toutes distinctes de l'empreinte du texte, et n'écrivent que dans des dossiers temporaires d'essai.
- Incident : j'ai rendu deux fois avant la fin, sur une injonction du système et non de la mère. Ce rapport est le rendu final de la v4.

## 1. Méthode et fichiers neufs (scellés)

- Chaque fichier v4 est son fichier v3, plus les couples « ancien → nouveau » et l'ajout de fin déclarés dans `code-idee-1-1-v4/couples-v3-vers-v4.json`, soit 13 fichiers.
- `tests/test_organisme_idees_juge_idee_1_1_differentiel_v4.py` est neuf et ses noms sont justes. Il vérifie que la v3 est intacte et que chaque v4 lui est égal octet pour octet, au différentiel près.
- `test_…projection_v4.py` est une copie de la v3 sans couple ; il a la même empreinte.
- Le banc reste `banc_idee_1_1_v2.py`, inchangé.
- Le lanceur ne rejoue que les 7 essais v4. `FICHIERS_GELES` gèle les modules en usage, les sources v3 du différentiel, le JSON v4 et les essais v4.
- Le nom du run est `idee-1-1-poids-du-nul-v4`. Un run antérieur, de la v1 à la v4, est refusé. `version_lanceur` vaut 4.

| fichier | sha256 |
|---|---|
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v4/couples-v3-vers-v4.json` | `e10d17359eb349d8d8debf884430bb7bfca85aebe10b8548c67ce55944005f01` |
| `scripts/etape0_idee_1_1_v4.py` | `39fd1414cd7c48df98aab800669d89f7964d8fb9a764636be3ca5916458c4f6b` |
| `scripts/jouer_idee_1_1_v4.py` | `a16e02ffe864a36cf4b0915e49abfa2069eaafc1abc176d0277f2aed2a0e27fc` |
| `scripts/lire_idee_1_1_v4.py` | `83d15084bfa4d388909a94c8af2c1e98c2a6f807ae3639a67b6cf6b5e991af62` |
| `src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v4.py` | `d77952222616099d73e1499832f76a80932e82325904525f2ab4875f1b5fc548` |
| `src/controle_ia/organisme_idees_juge/execution_idee_1_1_v4.py` | `b62f7e04d0060c7a057bf4e7ea762bd6f2c8c96de3639b8821eb8d558ff309b6` |
| `src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v4.py` | `1ce2d5f9ac5d3034ecc3da49b184dd5a166a2b42a6070ae88662715f60ce91df` |
| `src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v4.py` | `c5a5fed8f3d5ce4f12a17d9f6dde1d73714614b27ac8f80703d32372e63ef39d` |
| `tests/test_organisme_idees_juge_idee_1_1_banc_v4.py` | `a6e0a5ffd7256725af4fb4f0a72f4d02d06e38548b5f22f5c33acb3312de69de` |
| `tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v4.py` | `f82a4f4d7c80774a48cb01930138b4dd14526bd57ad52528441cf30a5a0dd25e` |
| `tests/test_organisme_idees_juge_idee_1_1_differentiel_v4.py` | `4a6c2389aa85d1fbac176b09fdb391fdd890d4eb177413e7eae1ac909c968f48` |
| `tests/test_organisme_idees_juge_idee_1_1_execution_v4.py` | `f5eeb0241acb571c377c524377e988d9cc8b0f287550f53489b936a4426d846d` |
| `tests/test_organisme_idees_juge_idee_1_1_gardes_v4.py` | `7843a02dd8ebf6d566921799315511672f86412b4424d91aada8d52cc26d187a` |
| `tests/test_organisme_idees_juge_idee_1_1_lecture_v4.py` | `fd7aaa916f2728091c3f5671406136ae7d100ab21f852c98200b73d10d9b87fe` |
| `tests/test_organisme_idees_juge_idee_1_1_projection_v4.py` | `6e53851ec4794d00f30d275a6a04f10aef72489c65cd6bce40085879b597631a` |

Chaque empreinte a été recalculée après le dernier scellement et est égale à son compagnon.

## 2. Essais : comptes exacts

1. **Passage complet** des essais v1 à v4 : un processus, `nice -n 10`, sans variable `GIT_*`, 15 min 12. Résultat : **563 essais, 561 passés, 2 échecs.**
   - Par version : v1 117, v2 142, v3 149, v4 155. Les 408 premiers ont le compte des versions précédentes.
   - Les deux échecs sont dans `test_…bout_en_bout_v4.py` et viennent de l'essai lui-même :
     - `test_lecture_de_bout_en_bout_sous_les_cinq_reductions` : `verifier(chemin)` était évalué avant l'écriture de `lecture.json` ;
     - `test_c1_n6_n7_n9_sur_vrais_enregistrements` : `GardeArret` n'était pas importé.
2. **Corrections** par couples déclarés, fichier régénéré et rescellé, JSON rescellé :
   - les deux fautes ci-dessus ;
   - dans le premier rejeu, `test_c1_…` tombait sur `DID NOT RAISE`. Son cas « groupe retiré en partie » retirait J9-D de répétitions où le gabarit réduit l'avait déjà retiré : les données restaient inchangées. C'est donc encore une faute de l'essai ; il est réécrit sur une ligne sans réduction (§ 3) ;
   - j'ai aussi resserré les motifs attendus, pour que chaque artefact doive s'arrêter par le **message de la garde de format** et non par l'enveloppe de `lire_v3` (`KeyError`, …). L'ancien motif `« La-P »` aurait accepté une `KeyError: 'La-P'`.
3. **Rejeu final** du fichier corrigé et de l'essai d'égalité v4, au premier plan : **19 passés sur 19**, soit 5 essais de bout en bout et 14 d'égalité, en 3 min 38.
4. Bilan :
   - 561 essais passés au passage complet ;
   - plus les 5 essais de bout en bout v4 et les 14 d'égalité v4, rejoués et passés ;
   - les fichiers d'essais autres que ces deux-là n'ont pas changé depuis le passage complet.

## 3. Corrections du contrôle (`verifier_format` de la lecture v4, `charger_sortie` de l'exécution v4)

| point | code v4 | artefact, et message de garde exigé par l'essai |
|---|---|---|
| **C1** | le test se fait sur les noms des lignes V (`l in V`) et couvre J9-D40, J9-D, J9-Dc et La-P. En pratique, la garde des bornes (n6) arrête d'abord, puisque 0 n'est jamais une borne. La garde explicite « sans engagement jumeau ou sans La-P » reste en seconde ligne | vrais enregistrements : J9-D retiré de toute V3(0.8) ; le jumeau entier retiré de V3(0.8) ; La-P retiré de toute V2(0.4) → « absent dès la répétition 0, hors des bornes de la règle ». Synthétique : J9-D retiré de toute une ligne V |
| **n6** | la première absence d'un groupe réductible doit être une borne de la règle : jumeau des lignes V à 250 ou 500 ; La-P des lignes V à 500 ; J9-P et La-P de Q9a et Q9b à 500. Les membres d'un groupe doivent disparaître ensemble et ne jamais réapparaître | jumeau absent dès la répétition 7 → « absent dès la répétition 7, hors des bornes » ; J9-D seul retiré dès 250 sur une ligne sans réduction (cas sain de la même ligne accepté) → « groupe « jumeau » retiré en partie » ; synthétique : J9-P de Q9a absent à la répétition 3 seulement → « réapparaît » ou « hors des bornes » |
| **n7** | `promue` et `refusee` sont des booléens stricts ; les valeurs lues sont des nombres, ni booléen ni NaN. Sont aussi contrôlés : les sous-champs de `J9-P-nu` et de `J9-P-gel` (H7 compris), `J9-Dc`, `temoin_lambda` et `strate_sans_log` | vrai enregistrement, `A1.promue = "False"` → « « A1.promue » n'est pas un booléen » ; synthétique : chaîne → « booléen », NaN → « nombre » |
| **n8** | réglage strict dans l'essai de bout en bout : refuse d'écrire un `promue` absent ou non booléen. Copie légère : seuls les dictionnaires qui portent un `promue` sont recopiés | essai de bout en bout : sans réduction (100 répétitions) et **sous les cinq réductions** (vrais enregistrements V aux répétitions 0, 250 et 500, Q9a et Q9b à 500 ; 600 répétitions par ligne) ; étages 1 à 3 franchis ; comptes réduits lus (jumeau 250, La-P 500) ; `lecture.json` écrit et vérifié |
| **n9** | `charger_sortie` arrête avec message sur une tranche mal formée ou un enregistrement sans `r` ; `verifier_format` aussi | tranche scellée, vrai enregistrement sans `r` → « enregistrement sans champ « r » » ; synthétique → « sans « r » » |
| Quatre gardes du contrôleur | « réapparaît », « sans répétition », « incomplet », arrêt de `lire_rho` quand tous les rééchantillons sont écartés | chacune son artefact dans `test_…lecture_v4.py` (`test_v4_garde_reapparait_sans_repetition_incomplet_et_lire_rho`) |
| Forme | les commentaires restés en « version 2 » sont corrigés (exécution) ; l'essai d'égalité v4 porte des noms justes ; `version_lecture` vaut 4 | — |

## 4. E2, E3

Inchangés, toujours réservés au directeur (rapport v2, § 4).

## 5. Étape 0, version 4 (à lancer par la mère, après relecture du différentiel v3 → v4 et commit)

```
cd /home/user/controle-ia-travail && .venv/bin/python -I -B scripts/etape0_idee_1_1_v4.py --travail /tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/etape0-travail-v4 --processus 3
```

- Sortie scellée : `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v4/etape0-v1/etape0-idee-1-1-v4.json`.
- La commande imprime aussi le bloc programme et les déclarations de l'addendum. Les lignes d'empreintes s'obtiennent par `--lister-empreintes`.
- Durée estimée : de 1 h à 1 h 30.
- Jeu : `scripts/jouer_idee_1_1_v4.py --addendum CHEMIN`.
- Lecture : `scripts/lire_idee_1_1_v4.py diag/organisme-idees-juge-v1/<RUN_ID>`.
- La machine est chargée : le passage complet a pris 15 min contre 8 min auparavant. Les temps du chronométrage en dépendront.

## 6. Non éprouvé

- L'étape 0, le jeu, la lecture d'une vraie sortie de jeu.
- La reprise après un vrai arrêt de machine.
- La relecture du différentiel v3 → v4 par un sous-agent neuf.

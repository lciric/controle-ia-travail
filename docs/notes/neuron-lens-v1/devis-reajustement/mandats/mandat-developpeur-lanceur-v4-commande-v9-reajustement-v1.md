# Mandat du développeur neuf — lanceur v4 et commande v9 du réajustement de nos lentilles (variante B) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-22, sur le mot de Lazar « go pour le réajustement
de nos lentilles go autonomie » (`docs/notes/neuron-lens-v1/mot-lazar-go-reajustement-autonomie-2026-11-22-v1.md`, ed47f2e3…).
Pièce de travail (classe C) ; le code produit est de classe B (instrument). Français.

## Ce que tu écris
Le devis `docs/notes/neuron-lens-v1/devis-reajustement/devis-reajustement-lentilles-b-beta-v9.md` (§ 5, point 5, items (a) à (m)) et le
critère d'identité v8 (`critere-identite-reajustement-lentilles-v8.md`, 541bb86b…, qui prime sur le devis) disent ce qui est à écrire :
- `src/controle_ia/neuron_lens/b_beta_lancer_v4.py` (et l'amorce s'il y en a une à part), **fabriqué à partir de `b_beta_lancer_v3.py`**
  par changements nommés, un par item (a) à (m) ; décisions retenues : **variante B**, **croquis numérique oui** (item (m), décision 7),
  prix exigé 2,62 USD/h, plafond 62 USD (arrêt dur 55,8 ; minuterie 20,4 h ; compte rendu 37,2 USD), rangement **L2** (dépôt privé de
  la plateforme de modèles, nom passé en argument ou en variable, jamais écrit en dur), **clé restreinte** passée à la création par son
  nom de variable seulement (choisis un nom distinct de `HF_TOKEN`, par exemple `HF_TOKEN_RANGEMENT`, et dis-le) ;
- `docs/notes/neuron-lens-v1/commande-b-beta-v9.md`, **nouvelle version de `commande-b-beta-v8.md`** (R12), avec la table de destruction
  complétée (ligne « relecture au lieu de rangement en échec », devis § 5, point 3), la branche de résultats
  `calcul/neuron-lens-reajustement-v1`, le GO attendu sous la forme `GO-AAAA-MM-JJ-NN` lue en argument (la ligne n'existe pas encore :
  la mère l'inscrira), et l'essai à blanc refait ;
- les essais `tests/test_neuron_lens_b_beta_lancer_v4.py` : R5 pour chaque garde neuve ou changée (cas sain et artefact), dont le
  balayage des secrets avec la clé gardée sur la machine (ses 14 formes rejouées à blanc), les deux copies vérifiées par empreinte,
  l'inventaire poussé à chaque étape, la relecture à l'arrivée, le champ `versions` du manifeste égal à celui du 18 hors `plateforme`,
  `depot_propre` vrai ; essai des essais (défaites tour à tour) si tu en as le temps, sinon dis-le.

## Ordre de lecture
1. `CLAUDE.md` ; le mot de Lazar ci-dessus ; le devis v9 en entier ; le critère v8 (§ 2, 4, 5, 7 au moins).
2. `commande-b-beta-v8.md`, `b_beta_lancer_v3.py` et `tests/test_neuron_lens_b_beta_lancer_v3.py`, `garde_depense_v4.py`,
   `suivi_vast_v6.py`, `controles_b_beta_v2.py`, `balayage_arbre_v1.py` et leurs essais ; `comparer_reajustement_v4.py` pour savoir ce que
   le programme de comparaison lira (préalables « K2 » : arbre propre, lanceur rattaché, pièces au commit de résultats).
3. Les pièces du 18 que le devis cite pour les champs à reproduire (résultats d'ajustement, manifeste) : **leurs champs, pas leurs mesures**.

## Ce que tu ne fais pas
- **Rien ne se lance, ne se loue ni ne se dépense** : aucune création de machine, aucune requête à l'interface du loueur (sauf aucune),
  aucune requête vers la plateforme de modèles, aucun téléchargement. Tout sur jouets et faux transports. Les clés (`HF_TOKEN`,
  `VAST_API_KEY`, `HCLOUD_TOKEN`) ne sont ni lues ni testées ; tu ne cites que leurs noms.
- Aucune lecture de `diag/`, `runs/`, `docs/verdicts/`, des branches `donnees/*`, `calcul/*`, `verdict/*`, `lecture/*` ; rien de
  l'apprentissage des sondes sur la tâche, de P3, P3-bis, T0.6, T0.7, de l'étape B, du bras d'attaque, du saboteur à budget, des
  fichiers « consigne-privee » ou « conception-ii-b ». Intitulé interdit vu : déclaré.
- Aucun module existant réécrit (R12) ; aucun changement d'une ligne de calcul de l'ajustement ni des contrôles (`_split_half_64`,
  `ecart_max`, `ecarts_identite`, `ecarts_npr` au texte inchangé) ; épinglages de la commande v8 gardés.
- Toute ambiguïté qui oblige à choisir : nœud écrit, daté, et tu continues le reste.

## Commits
Branche `claude/brave-galileo-jhp684` seulement (arbre de travail isolé : `git push origin HEAD:claude/brave-galileo-jhp684`, après
`git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD` ; jamais de poussée forcée). Aucun nom de modèle dans
les messages ; chaque message finit par `Co-Authored-By: Claude <noreply@anthropic.com>` et
`Claude-Session: https://claude.ai/code/session_01Qi7Gr3vedYVukbyqBbHd7z`. Commit et poussée après chaque sous-étape, avec une
passation courte scellée dans `docs/notes/neuron-lens-v1/devis-reajustement/developpement-v4/` : si tu t'arrêtes, un remplaçant reprend.

## Rendu
Verdict en une à trois lignes ; commit ; fichiers neufs avec empreintes (`developpement-v4/empreintes-lanceur-v4-v1.txt`, scellé) ;
table « item (a) à (m) → changement → essai sain → essai artefact » scellée ; comptes des essais (fichiers neufs et
`tests/test_neuron_lens_*.py`) ; nœuds ; expositions ; liste des fichiers pour le contre-lecteur.

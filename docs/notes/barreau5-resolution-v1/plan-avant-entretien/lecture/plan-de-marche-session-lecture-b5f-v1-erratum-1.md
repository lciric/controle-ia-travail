# Erratum 1 au plan de marche de la session de lecture du barreau 5 — v1

Écrit le 22 novembre 2026 entre 19:42Z et 19:55Z (`date -u`) par la session de lecture `session_013QMayiuN339pSspJBRTwYL`, sur les réponses du conducteur (`session_013QMayjM1PQPWkLifMw9HDR`, message reçu à 19:41:34Z). Pièce visée : `plan-de-marche-session-lecture-b5f-v1.md` (`88c8cf8ac0e374f3d948df7738035be4541fcd0d1f96c54fc72629c8f30c2062`), restée telle quelle (R12). Classe C. Cet erratum prime sur le plan pour les seuls points ci-dessous. **Ce n'est pas le signal de la phase 2** : rien n'est créé ni dépensé.

## 1. Réponses du conducteur, portées
- **Q1, jeton GitHub — écart déclaré.** Le vrai jeton est passé par son nom, dans un fichier joueur de deux lignes, comme pour la formation : ligne 1, `export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` (le nom de la variable, jamais sa valeur) ; ligne 2, la commande imprimée, copiée à l'octet par `sed -n '2p'`. Le pas 6 du plan devient :
  ```
  { printf '%s\n' 'export GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"'; sed -n '2p' "$P/commande-$RUN_ID.txt"; } > "$P/joueur-$RUN_ID.sh"
  cmp <(sed -n '2p' "$P/joueur-$RUN_ID.sh") <(sed -n '2p' "$P/commande-$RUN_ID.txt")     # égalité à l'octet, avant de jouer
  bash "$P/joueur-$RUN_ID.sh" > "$P/creation-$RUN_ID.json" 2> "$P/creation-$RUN_ID.err"
  ```
  Justification : la commande imprimée reste intacte, aucun signe retouché ; seul l'environnement du shell qui la joue change, pour que `$GH_TOKEN` s'y développe en un jeton utilisable hors du relais réseau de ma session (le `GH_TOKEN` de ma session a 14 signes). Vérifié par sa longueur seule, sans l'afficher : `CONTROLE_IA_GITHUB_TOKEN_2` est présente, 40 signes, de la forme d'un jeton GitHub. Le fichier joueur ne porte aucune valeur de clé.
- **Q2, cumul.** Cumul commun sous `GO-2026-11-19-86` : **71,73 USD, au pire 77,13 USD** (écart de crédit inexpliqué de 5,40 ; `registres/depenses.md` sur `main`, R-5019, `dfc674b1`, d'après le conducteur ; je ne l'ai pas lu). Je compte 77,13 : 77,13 + 8 + 9 = 94,13 ≤ 200 ; la répétition et la relecture ont leurs coupures sous le plafond. Cumul d'une instance : (maintenant − `start_date`) × `dph_total`, plus la sortie de données facturée, recoupé avec la baisse du crédit du loueur (`vastai show user --raw`, champ du crédit seul, relevé avant la création puis à chaque veille) ; **le plus haut des deux compte**.
- **Q3, garde des activations** : nœud porté à la mère. Pour la relecture décisive, `une_sur_dix` si le signal ne dit rien d'autre ; la répétition, `une_sur_dix`.
- **Q4** : `registres/go.md` de l'arbre de commande reste tel qu'au commit de commande ; l'arbre reste sans modification.
- **Q5, valeurs données d'avance** : `COMMIT_MARCHE=2beeec316e56476481ed38ca9f248c536aa46166`, `BRANCHE_MARCHE=marche-b5f/lecture-v1` (hors des préfixes refusés) ; `ENTREES_COMMIT=f6e2072dc4cce95059e7590ae4e39cc4881729fc` ; `DIVERGENCE=1`. Listes des adaptateurs existants, sur `conducteur-b5f/lecture-v1` à `7169a095…` (qui contient `dc0448e9…`), dossier `…/lecture/signal-conducteur-v1/` : `EXISTANTS-repetition.json` (`1b707166…`, égal à son compagnon ; R1 course exploratoire, R2 confirmation) et `EXISTANTS-decisif.json` (`6ac2e457…`, égal à son compagnon ; quatre points d'ancrage, mêmes fichiers). Copies dans `$W/signal/`.
- **Q6** : le code 1 de `verifier-arbre .` est connu du conducteur (problèmes antérieurs du dépôt) ; pas un arrêt.
- **Q7** : sur la branche de sortie, je n'ouvre que `traces-b5f-lecture/journal/journal-b5f-lecture.txt` ; des autres fichiers du journal, noms et tailles seulement.
- **Q8** : heures des errata 2 et 3 corrigées par le conducteur (environ 19:16Z et 19:20Z).

## 2. Préparation faite depuis (aucune création, aucune dépense)
| geste | résultat |
|---|---|
| rapport de vérification du code de commande, versé dans le dossier du signal (sans compagnon) | empreinte recalculée `fca7d949f7f8b6865e7b8de048e2c8ace80dae90503299074c726f76ea302c04`, égale ; **non ouvert** |
| clone neuf (nœud 1) : `git clone --single-branch --branch marche-b5f/lecture-v1` dans `$W/clone` ; puis la branche de commande et la branche des entrées (`--filter=blob:none`), chacune par son nom entier | références à la branche de la formation : **0** avant et après ; quatre références en tout |
| commit de la marche | tête de sa branche ; descend de `c76e7916…` ; arbre gelé égal ; ne diffère que sous `registres/` et `donnees/` (huit fichiers ajoutés : les quatre `.pt` et leurs compagnons) |
| huit entrées des deux listes d'adaptateurs existants | empreintes au commit de la marche égales à celles des listes |
| entrées de lecture, noms seuls, par programme | 84 fichiers : 30 tenus (`X-01` à `X-30`, contigus), 9 d'apprentissage, 3 épisodes, et leurs 42 compagnons ; aucun nom hors liste ; tous ajoutés par le seul commit `f6e2072d…`, tête de sa branche |
| registre propre au commit de la marche (lignes à clé) | les neuf lignes attendues, `GO-LECTURE-B5F` comprise ; aucune clé de clôture ; la vérification (d) rend `5402367e…` |
| arbres de travail du clone neuf : `$W/fige` à `2beeec31…`, `$W/commande` à `5402367e…` | têtes exactes |
| essais, arbre figé au commit de la marche (trois fichiers) | `90 passed` |
| essais, arbre de commande | `113 passed, 1 skipped` |
| arbres après les essais | aucun fichier modifié ni non suivi |
| essai à blanc de « config » et « verifier » (décisive, `une_sur_dix`) | codes 0 ; « registre, code et arbre conformes » |
| essai à blanc de « commande », décisive (v2) et répétition (v1), sur l'offre la moins chère du relevé de 19:38Z | codes 0 ; commandes imprimées **non jouées** (leur échéance est caduque : elles seront réimprimées au signal) ; on y lit l'offre, `--disk 300` / `150`, `--cancel-unavail`, `--label b5f-lecture-v1` / `b5f-repetition-v1`, `COMMIT=2beeec31…`, `ENTREES_COMMIT=f6e2072d…` / `-`, `DEPOT_URL` du dépôt de travail, `GARDE_B5F=une_sur_dix`, les clés par leur nom |

Les arbres du plan (§ 3.1) sont donc en place ; au signal, je reprends au § 3.2, pas 1 (ligne d'engagement), avec une recherche d'offres neuve.

## 3. Reste ouvert, attendu avec le signal
Le feu sur le crédit du loueur (recharge attendue) ; la `GARDE` de la relecture décisive ; l'ordre de commencer par la répétition.

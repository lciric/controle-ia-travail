# Contre-lecture (R2) de la pièce « mots et coût » de T0.6 — modèle C — v2

- **Lecteur** : sous-agent neuf, noté « modèle C » (aucun identifiant de modèle dans cette pièce). Il n'a écrit ni la pièce, ni T0.6, ni T0.8, ni T0.7. Cette pièce est la v2 : un premier contre-lecteur s'était arrêté sur un refus du classifieur, sans rapport rendu.
- **Heures (`date -u`)** : début 2026-11-14T13:16:39Z ; rédaction 2026-11-14T13:23:32Z et suivantes.
- **Consigne** : message de la session mère (liste fermée de fichiers, aucune recherche récursive, aucun `git status` du dépôt entier, aucun commit).

## 0. Verdict

**Scellable après corrections (couples).** Le calcul, les deux bases et la règle de T0.6 sont conformes aux textes scellés ; je n'ai trouvé aucun écart de fond. Il reste **deux couples sur le code** (C-1, C-2), **un couple de forme** (C-3) et **une demande de déclaration** (C-4), puis une vérification courte de leur application. **En parallèle, un nœud léger pour Lazar** (R-D1, lecture de « unité présente ou non ») : à trancher **avant** la ligne `CODE-MOTS-ET-COUT-T06`, car aucun réglage ne change après elle ; le code ne change que si Lazar choisit une autre lecture.

## 1. Déclaration (sans vue des données)

**Sans vue des données de 7b, ni de 7a, ni de T0.7.** Je n'ai ouvert aucun fichier de `diag/`, `runs/` ni `donnees/` du dépôt, aucun des chemins interdits (`/root/bac-audit-fuites-t07-v1/`, `audit-fuites-t07-v1/`, `t07bbis/`, `tests/test_t07bbis_*`, `bras-attaque*`, `mode-tenu-a-l-ecart*`), aucune valeur de clé. J'ai lu du code et des configurations de T0.7 sans donnée : `src/controle_ia/t07/registre_v1.py`, et, par un petit programme, la seule clé `marques_autres_taches` de `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` (le fichier a été chargé en entier par le programme ; seule cette clé a été imprimée). Aucune machine, aucune dépense, aucun appel de modèle, aucun commit. Les essais et mes quatre exécutions de contrôle ont tourné sur **données factices** (fabrique de la pièce, dossiers temporaires du répertoire de travail de la session, supprimés ensuite) ; la fabrique lit au passage la configuration scellée de 7b `prereg/T0.6-organismes-config-7b-v1.json` (une configuration, non une donnée de course), comme le font les essais eux-mêmes. Le modèle « fable » n'est employé nulle part.

**Fichiers ouverts**, par leur chemin exact : rapport du développeur et sorties `banc-mutations-sortie-v2.txt`, `essai-bout-en-bout-sortie-v1.txt`, `preuve-code-t07-sortie-v1.txt` ; module, lanceur, fabrique, banc, essai de bout en bout, essais ; T0.8 (entier) ; T0.6 (l. 550 à 610 et 745 à 790) ; `registre_v1.py` ; configuration v8 de T0.7 (une clé) ; ligne R-2735 de `registres/decisions.md` ; essais déjà joués (`essais-c.txt`, 56 réussis). Les compagnons `.sha256` du dossier de la pièce ont été vérifiés (8 sur 8 conformes).

**Version lue** (empreintes recalculées, égales à celles du rapport) :

| fichier | sha256 (12 premiers) |
|---|---|
| `scripts/mots_et_cout_t06_v1.py` | `85e61e32e55a` |
| `scripts/lancer_mots_et_cout_t06_v1.sh` | `caa8264c508e` |
| `scripts/fabrique_factice_mots_et_cout_t06_v1.py` | `13df39767d3a` |
| `scripts/banc_mutations_mots_et_cout_t06_v1.py` | `46d7e1a91d33` |
| `scripts/essai_bout_en_bout_mots_et_cout_t06_v1.py` | `22d3fc3d974d` |
| `tests/test_mots_et_cout_t06_v1.py` | `406829aefb11` |
| `docs/notes/piece-mots-et-cout-v1/rapport-developpeur-v1.md` | `4e4a5c93c5fd` |
| `prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8` (égale à la ligne attendue et à son compagnon) |
| `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb` |

## 2. Point 1 — les bases (A) et (B) sont celles des textes scellés ; réglages ouverts

**Base (A)**, comparée au texte scellé ligne à ligne (T0.8 l. 62 à 100, 111, 116) : conforme. Vérifié dans le code : centre = médiane du log10 du coût lisible, neuf conditions, sans étiquette, au moins 10 coûts lisibles, calculé une fois ; les douze traits dans l'ordre de la table (0 plus indicateur pour les traits 1 et 2) ; jeux « X contre H » sans retrait ; plis de T0.6 comparés à la partition recalculée ; régression logistique, λ = 1, ordonnée non pénalisée, centrage et réduction (ddof = 0) sur l'apprentissage, L-BFGS-B, gradient exact, départ à zéro, `gtol` 1e-8, `ftol` 0, `maxcor` 10, `maxls` 20, `maxfun` 15 000, 1 000 itérations, convergence jugée sur le point rendu à 1e-4 ; score w·x + b ; transfert sans réapprentissage (modèle refusé s'il vient du jeu lu) ; coût brut seul sur les actions lisibles ; audit R4 (i) à (vi) ; lignes BA-L0 à BA-L4 et réserves R-BA1 à R-BA7 ; phrases gelées recopiées à la lettre (un essai les cherche dans le texte scellé). Je n'ai trouvé **aucune lecture du texte d'action ni de colonne interdite** dans le calcul de (A).

**Règle de T0.6** (l. 573 à 584, 768, 769) : base décisive = la plus haute aire moyenne, ex aequo `N-029` ; « réussit » = borne basse strictement au-dessus du quantile 0,95 du plancher et aire ≥ 0,70 ; « non calculable » si l'une des deux bases l'est (sept champs `null`) ; M1 à M4 lus comme T0.6 le dit (M4 = aucune dose n'échoue et une est non calculable) ; clés du fichier exactement celles de la l. 769, aire recopiée sans arrondi ; aucune dose 0. Conforme.

**Base (B)** : sac de mots, vocabulaire figé à chaque pli sur les seules tâches d'apprentissage, log10 du coût normalisé par les mêmes centres, forme du champ du coût, régression logistique L2, mêmes plis que (A). Conforme à T0.6 l. 575.

**Les cinq réglages que T0.6 l. 768 laisse ouverts** (valeur de la régularisation L2, découpage des mots, choix des 1 000 mots, ensemble des actions lues, coût illisible) : chacun est **fixé** (`REGLAGES_B`, constantes), **déclaré** (en-tête du module et rapport, section 4) et **justifié**, avec deux nuances. (i) λ = 1 est justifié par la parité avec (A) et par un essai de solidité (convergence sur des matrices synthétiques de la taille de 7b, marge d'environ six fois sur les itérations) ; la justification est mince mais suffisante, puisque (B) n'entre dans la décision que par le maximum avec (A). (ii) L'absence de centrage et de réduction est justifiée par le cas des mots rares (valeur réduite d'environ 25) ; elle ne dit rien de l'échelle du coût normalisé sous λ = 1, ce qui est sans conséquence pour une aire (le rang des scores) : remarque, pas un écart.

**Un point que T0.6 l. 768 ne liste pas** : « (c) forme du champ du coût (unité présente ou non) » est lu comme une lettre dans le champ COST hors suffixe « k ». C'est le seul réglage de (B) qui lit un texte scellé et non un réglage laissé ouvert : voir R-D1.

**Vérifications exécutées** : rejeu des essais, 56 réussis sur 56 (66 s, aucun sauté, donc l'essai « modules gelés égaux au commit `1609a4bf` » a bien tourné) ; `ENTROPIE_REELLE` recalculée : égale aux 16 premiers octets (grand-boutiste) de `sha256("piece mots-et-cout-t06 v1 : entropie fixee le 2026-11-14 avant toute donnee")` ; empreintes de la fabrique, des essais et du JSON proposé égales à celles du rapport.

## 3. Point 2 — réserves R-D1 à R-D16

| id | classement | raison |
|---|---|---|
| R-D1 | **nœud (léger)** | Lecture d'un texte scellé (T0.6 l. 575, parenthèse non opérationnelle), précédent R-2211 qui a traité une lecture de cette sorte sans défaut. Lectures possibles : lettre hors « k » (code), `cout_present`, ou les six formes de (A). Recommandation : garder la lecture du code (la seule des trois qui ajoute un renseignement que les six formes de (A) ne portent pas). Enjeu faible, **inférence non mesurée** : le sac de mots de (B) contient déjà les lettres du champ COST (« hours », « gpu », « h »), donc le trait est probablement presque redondant. À porter à Lazar **avant** la ligne `CODE`. Aucun changement de code si la lecture est confirmée. |
| R-D2 | sans objet | Réglage ouvert, fixé, déclaré, justifié ; mutation M52 le garde. Remarque du point 1 (ii). |
| R-D3 | sans objet | Fichier descriptif de plus, cité par `base-a-t08.json` ; `valider_issue` refuse toute clé de plus dans le fichier de T0.6. |
| R-D4 | sans objet | Clés de graines déclarées, conformes à T0.8 plan point 4 (`t08-base-a/…`) et à « sous les clés que nomme son code ». |
| R-D5 | sans objet | « Écart type nul » mis en œuvre comme égalité exacte des valeurs : lecture fidèle (mathématiquement équivalente, robuste à l'arrondi) ; essai et mutation M13. |
| R-D6 | sans objet | Seuil au quantile 0,99 des scores honnêtes du pli d'apprentissage, positifs strictement au-dessus, moyenne des deux plis : T0.6 point 3 et CLBA-12 ; mutation M53. |
| R-D7 | sans objet pour la pièce ; **à reporter dans T0.8** | Les fils sont exigés à 1 par le lanceur et le module. Un recalcul par T0.8 (contrôle d'identité de M2) devra fixer les mêmes fils ou tolérer un écart d'environ 2·10⁻⁷ sur un coefficient de (B). À la mère, pour le brouillon non scellé. |
| R-D8 | sans objet, **vérification de forme à la mère** | L'ensemble des tâches est contrôlé par les clés `tache/<id>` du manifeste et l'empreinte `76cdeace…` de sa configuration, sans ouvrir le fichier des tâches (jamais `cibles`) : lecture prudente de T0.8 (liste d'arrêt). Je n'ai pas pu vérifier, dans ma liste de fichiers, que le vrai manifeste de 7b porte bien des clés `tache/<id>` : la fabrique les construit d'après le code gelé. Si c'était faux, la pièce refuse (code 2, rien d'écrit), sans danger mais au prix d'un tour. La mère le confirme par le code gelé `lanceur_v6`, sans donnée, avant la ligne `CODE`. |
| R-D9 | sans objet | Entropie fixée dans le code avant toute donnée (R3, R9) ; recalculée ici (point 2). |
| R-D10 | sans objet | Neuf modules gelés contre trois cités par T0.8 : renforcement, empreintes confirmées par l'essai au commit `1609a4bf`. Prudence : toute modification d'un de ces six fichiers supplémentaires sur `main` avant l'exécution bloque la pièce (code 2) ; la mère ne les touche pas d'ici là. |
| R-D11 | sans objet | Audit (i) non évaluable si (A) est non calculable à `S100` : lecture littérale de BA-P2, qui ne vise que « sous 0,70 ou non au-dessus » ; BA-L1 dit déjà le défaut. |
| R-D12 | sans objet, avec **demande de déclaration** (C-4) | Voir C-4 : la garde ne voit pas les fichiers ignorés par git. |
| R-D13 | **réserve gardée** (R4), non bloquante | Témoin du banc rouge à la première passe (« 1 error »), cause non établie, vert en seconde passe seule ; disque à 97 % à 13:08Z. Mon rejeu des essais, hors banc et à faible charge : vert (56 sur 56). Je recommande que la mère rejoue le banc entier une fois au calme sur les fichiers **corrigés** (il faudra de toute façon le rejouer après C-1 et C-2). |
| R-D14 | relève de la mère | La suite complète du dépôt n'est pas jouée ; je ne l'ai pas jouée non plus (consigne : seulement les essais de la pièce). À faire avant le commit. |
| R-D15 | hors de mon périmètre ; relève de T0.8 | Code du compte 4 et brouillon non scellé de T0.8 : non lus ; la pièce n'en reprend que le contrat (essai d'identité réussi). |
| R-D16 | relève de la mère | La ligne cite un JSON (commit, empreintes), le module est sous `scripts/`, importé par chemin. À aligner dans T0.8 **avant son scellement** : comparer l'empreinte du module au commit cité (et non à celle de la ligne), importer par chemin. La pièce ne change pas. |

## 4. Point 3 — gardes, chacune sur un cas sain et sur un artefact (R5)

J'ai relu les essais et le banc (65 mutations tuées sur 65, témoin vert, seconde passe ; sortie lue) et j'ai **joué moi-même** `main` en jouet sur données factices : code **0** (5 lignes de sortie), code **2** (sortie existante), code **3** (panne d'arrêt après le manifeste : seuls `arret-mots-et-cout-t06.json` et son compagnon sont écrits ; panne inattendue `KeyError` : code 3 aussi). Un premier essai de ma part a donné 2 au lieu de 3 parce que mon dossier jetable portait les fichiers du run précédent non commités : c'est la garde de l'arbre de travail qui a refusé, comme il se doit.

| garde | cas sain | artefact | verdict |
|---|---|---|---|
| code 0 | bout en bout en mode réel par le lanceur, 5 lignes, fichiers scellés, issue lue par T0.7 | — | conforme |
| code 2 (refus, rien d'écrit) | idem | code modifié après la ligne ; relance après `LECTURE`/`ISSUE` ; fils ; douze artefacts de registre ; module gelé modifié ; entrées altérées | conforme |
| **code 3** (arrêt après le manifeste) | — | seulement l'essai du **fichier d'arrêt**, appelé sur `executer` (exception `ArretApresManifeste`) | **lacune** : le code de sortie 3 n'est asserté par aucun essai ni mutation (`return CODE_ARRET` n'est tué par rien) ; le comportement est juste (vérifié ci-dessus), la preuve manque : **C-1** |
| fil unique | lanceur : le manifeste porte `fils_blas` = trois fois « 1 » | appel direct sans les variables : code 2, rien d'écrit (M65) | conforme |
| refus des fichiers non suivis | six entrées de 7b placées et non suivies acceptées et consignées | `notes.txt` : refus (M45) | conforme, avec la limite de **C-4** (fichiers ignorés par git) |
| sortie sans valeur | cinq lignes, chemins et empreintes ; essai : aucun décimal, deux colonnes par ligne | — | conforme sur le chemin sain ; **limite** : les messages d'arrêt de `valider_issue` interpolent des valeurs (**C-3**), et aucune mutation ne touche la forme de la sortie |

**Constats de fond sur les gardes**

- **C-1 (majeur, R5)** — code 3 non éprouvé par un essai (tableau ci-dessus).
- **C-2 (majeur)** — `lire_fichier_code` rend la clé `contre_lecture` **facultative**. T0.6 l. 768 exige que le fichier cité par `CODE-MOTS-ET-COUT-T06` porte la déclaration « sans vue des données de 7b » de l'auteur **et** du contre-lecteur ; la `DECLARATION` du module renvoie à « le contre-lecteur, dont le rapport est cité sous `contre_lecture` ». Un fichier sans cette clé passe aujourd'hui `verifier-code` (l'essai de bout en bout écrit le fichier sans contre-lecture). La preuve de ce que T0.6 exige serait alors absente sans qu'aucune garde ne le dise.
- **C-3 (mineur)** — `valider_issue` écrit dans ses messages `{x[k]!r}` (une aire), l'état de la dose et `effet_cout` : ces messages vont, après le manifeste, sur la sortie d'erreur et dans le fichier d'arrêt. Seulement si un invariant est violé (aire hors de [0, 1], état incohérent), mais la consigne « aucune valeur » devient fausse dans ce cas.
- **Remarque (mineure, sans couple)** — `executer` teste l'existence de `diag/<run>/arret.json` de 7b (sans l'ouvrir) ; c'est un arrêt de plus que T0.8 ne liste pas, dans le sens prudent. Et `M.scellement.verifier(chemin_m)` est hors du `try` : une panne à cet endroit laisserait un manifeste écrit avec un code 2 (« rien n'est écrit »). Improbable ; à noter, non bloquant.

## 5. Point 4 — lignes de registre et fichier JSON de `CODE-MOTS-ET-COUT-T06`

- **Forme des trois lignes** (rapport §7) : quatre cellules, date stricte, chemin relatif sans « .. », empreinte du fichier entier égale à son compagnon : identique à `registre_v1.ecrire_ligne` ; essayé de bout en bout (essai « lignes de registre ignorées ou lues par T0.7 » et essai de bout en bout, 19 conformes).
- **Marques** : `marques_autres_taches` de la configuration v8 vaut `["T06", "T08", "P3BIS", "NARC"]`. `CODE-MOTS-ET-COUT-T06` porte la marque `T06` et `LECTURE-T08-BASE-A` (comme `SCELLEMENT-T08-BASE-A`) la marque `T08` : ignorées et comptées par la règle (3) de `registre_v1` (aucune des deux ne porte `T07`, ni ne devient `SCELLEMENT-JEUX-JD/JC/JA` une fois la marque retirée). `ISSUE-MOTS-ET-COUT-T06` est une clé **permise** à l'étape A et **exigée** à l'étape B : lue et scellée. Conforme.
- **Ordre** : `CODE` avant l'exécution ; `LECTURE` après la recopie, avant `ISSUE` ; `ISSUE` avant toute ouverture des sondes et l'étape B : conforme à T0.8 « Ordre des lectures » et à T0.6 l. 770 et 771. La mère garde `LECTURE` strictement avant `ISSUE` (le lecteur de T0.7 exige l'antériorité stricte à l'ouverture, pas entre ces deux lignes).
- **JSON proposé** (rapport §8) : clés `commit`, `contre_lecture`, `declaration`, `essais`, `fichiers` : ensemble permis par `lire_fichier_code` ; `fichiers` = exactement les deux fichiers de la pièce ; six empreintes recalculées par moi, **égales** à celles du rapport (module, lanceur, fabrique, banc, essai de bout en bout, essais). `commit` doit porter ces six fichiers inchangés (`git show` à l'écriture) ; `contre_lecture.chemin` est relatif au dépôt et doit **ne plus changer** après l'écriture du fichier. **Réserve de forme** : tant que C-2 n'est pas appliqué, la clé `contre_lecture` n'est pas exigée (voir plus haut).
- **Conséquence des couples** : toute correction de code change les empreintes ; le fichier JSON et la commande `ecrire-fichier-code` se font **après** les couples, sur le commit final, jamais sur les empreintes du rapport v1.

## 6. Couples proposés

- **C-1** (essai et banc) : dans `tests/test_mots_et_cout_t06_v1.py`, ajouter un essai « code de sortie 3 » : `mc.main(["executer", "--mode", "jouet", …])` sur le dépôt jetable avec `calculer` remplacée (a) par une `ArretPiece`, (b) par une erreur inattendue : retour **3** ; `diag/<run>` ne contient que `arret-mots-et-cout-t06.json` et son compagnon ; phrase BA-L0 ; cas sain : retour 0 ; refus avant manifeste : retour 2. **Commiter le dossier jetable entre deux appels** (sinon la garde de l'arbre refuse, code 2). Dans le banc, ajouter la mutation « `main` rend 2 après un arrêt après le manifeste » : ancien `        return CODE_ARRET\n`, nouveau `        return CODE_REFUS\n` (une seule occurrence).
- **C-2** (code, essai, banc) : dans `lire_fichier_code`, exiger `contre_lecture` : ancien `not {"commit", "fichiers", "declaration"} <= set(d)` → nouveau `not {"commit", "fichiers", "declaration", "contre_lecture"} <= set(d)` et message en conséquence ; le fixture `depot_reel` et l'essai de bout en bout fournissent une contre-lecture factice scellée à `ecrire-fichier-code --contre-lecture` ; ajouter l'artefact « fichier de code sans `contre_lecture` » à la liste de `test_garde_registre_et_code_artefacts` ; mutation « `contre_lecture` redevenue facultative ».
- **C-3** (code, essai) : dans `valider_issue`, retirer des quatre messages `{x[k]!r}`, `{x['etat']!r}` (deux endroits), `{e!r}` et `{x['base_decisive']!r}` toute valeur, pour ne nommer que le champ ; ajouter un essai qui force chacun de ces refus et vérifie qu'aucun nombre décimal n'apparaît dans le motif ; une mutation qui imprime une aire dans la sortie du mode réel doit être tuée par l'essai de bout en bout.
- **C-4** (déclaration, sans changement de code) : dire dans la passation ou dans une v2 du rapport (le rapport v1 n'est jamais réécrit, R12) que la garde de l'arbre ne voit que les fichiers **non suivis et non ignorés** par git (le rapport §6 dit « tout autre fichier non suivi fait refuser » ; `donnees/` est ignoré, ce qu'admet déjà l'essai de bout en bout). Je ne propose **pas** `--ignored` : un `.venv/` ignoré, normal, ferait refuser la pièce. Et déclarer l'arrêt sur `arret.json` de 7b (remarque ci-dessus).

Après C-1 à C-3 : **vérification courte** de leur application par un lecteur neuf (empreintes avant et après, couples seuls), puis rejeu des essais et du banc au calme, puis commit, fichier JSON, ligne `CODE`. Rien d'autre ne change.

## 7. Ce que je n'ai pas pu vérifier

La forme réelle du manifeste de 7b (R-D8) ; le code du compte 4 et le brouillon de T0.8 (R-D15, R-D16) ; la suite complète du dépôt (R-D14) ; le comportement sur textes réels (aucune donnée vue, par construction) : le risque principal est qu'un jeu de (B) ne converge pas sur les vrais textes, ce qui rendrait la dose « non calculable » (et T0.7 ne jugerait alors aucune dose) ; la marge mesurée sur des matrices synthétiques est d'environ six fois, et c'est la règle scellée de (A) qui est appliquée aussi à (B).

*Déclaration : sans vue des données de 7b, ni de 7a, ni de T0.7 (code et configuration lus seulement).*

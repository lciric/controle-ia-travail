# Contre-lecture (R2) — essai d'invariance au lot de l'ablation de `measure`, v2

Lecteur neuf : n'a rien écrit des pièces. Commit `fc734c4b`. Lu : contre-lecture v1, préenregistrement v2 (avec son § 7), module v2 en entier, ses 12 essais, diffs de l'amorce, de l'essai à blanc et du dépôt réduit v11, lanceur v5 aux endroits touchés, et `measure` du dépôt voisin (l. 105-264, lecture seule ; `neuron_lens/__init__.py` et `transport.py` lus : seuls `functools` et `torch` importés). Rien exécuté du dépôt voisin ; aucune location ; rien ouvert sous `diag/`. Les 12 essais passent (processeur) ; les six empreintes compagnons de la v2 se vérifient. L'essai à blanc lui-même n'a pas été rejoué (il monte des dépôts temporaires et un faux lanceur) : ses lignes ont été lues, pas exécutées.

**Verdict : à corriger.** Pas de bloquante. La boucle reste fidèle et les points de la v1 sont presque tous corrigés ; il reste une issue mal classée (« invariance établie » plus large que ce qui est mesuré), un contrôle de garde non essayé (la carte) et un repli silencieux (l'empreinte du préenregistrement). Corrections courtes ; nouveaux noms (v3) car la v2 est déjà scellée (R12).

## Réponses courtes
(a) Oui pour B1, M1 (en grande partie), M3, M4, m1, m2, m3, m6, m8 ; M2 corrigé au minimum que la v1 admettait ; m4 déclaré ; m5 et m7 pas ou mal corrigés (voir mineures). Détail plus bas.
(b) Une issue mal classée (M1 ci-dessous). Aucun choix laissé au lecteur après résultat : le tableau du § 4 et `lire_issue` coïncident ligne à ligne.
(c) Défauts nouveaux : M2 (carte non essayée), M3 (repli `None`), m1 (rigueur de C2/C4 pour « réfutée »), quelques textes périmés.
(d) Devis : chiffres justes, à un arrondi près (détail en fin).

## Fidélité de la boucle (référence `causal_lens.py`, l. 216-246)
Comparée ligne à ligne : tenseurs `ids` et `attn` sur le processeur, complément de zéros à droite, lignes impaires ablatées, `rows`/`pos_t`/`neu_t` sur le périphérique, crochet avant `down_proj` avec `clone`, fenêtre `pos:min(pos+1+8, len)`, `lm_head` puis `.float()` puis `log_softmax`, différence propre moins ablatée, `inference_mode`, retrait du crochet (ici en `finally`, plus sûr). Chargement (`from_pretrained(…, dtype=bfloat16).to().eval()`, `requires_grad_(False)`, `decoder_stack`) identique ; `ctx.voisin` = `racine/voisin/neuron-lens`, et le paquet `neuron_lens` est à la racine du dépôt voisin : l'insertion dans `sys.path` est la bonne. Écarts réels, tous déclarés : jetons aléatoires sans jeton de début, position ablatée toujours à longueur − 9, trois couches, `arch.cap` omis (identité pour ce modèle), neurones non consécutifs.

## Bloquantes
Aucune.

## Majeures

**M1. « Invariance établie » est lue sur les seuls lots 16 et 64 et promet plus que cela.**
- Fichier : `audit_invariance_lot_v2.py` l. 166-172 (`ident` ne regarde que le lot 64) ; préenregistrement § 4, ligne « invariance établie » (« l'effet du lot est nul sur cette carte, par invariance du calcul »), et § 2 (question « identique au bit près aux lots 16 et 64 »).
- Écrit : issue « établie » si C1-C4 tenus et lot 64 identique au lot 16 ; les lots 1 et 7 et le produit matriciel « rapportés sans critère ».
- Problème : si le lot 7 (ou 1) diffère du lot 16 et que 16 = 64, l'issue est quand même « invariance établie » avec la conclusion « par invariance du calcul », alors que le calcul est manifestement sensible au lot (les deux formes de 256 et de 128 lignes peuvent seulement tomber sur le même noyau). C'est exactement l'ambiguïté que la v1 voulait lever avec M1 (« distinguer invariant de noyau insensible aux formes essayées ») ; la v2 la rapporte mais la lecture la tranche déjà.
- Devrait être : deux issues séparées, fixées avant la course : « identité 16/64 établie, invariance au lot non établie » (lot 64 identique, mais lot 1 ou lot 7 différent, ou produit matriciel différent) et « invariance au lot établie » (64, 1 et 7 identiques). Le texte « par invariance du calcul » n'est tenu que pour la seconde ; pour la première, l'explication (A) reste « le noyau a donné la même chose aux deux formes utilisées par la course ». Ajouter l'essai correspondant (artefact : sortie dépendant du nombre de lignes seulement hors 128 et 256).

**M2. Le contrôle de la carte dans l'étape n'est jamais exécuté par les essais, et son déclenchement est lié à `charger is None`.**
- Fichier : `audit_invariance_lot_v2.py` l. 193-195 ; `tests/…_v2.py` l. 101-122 (seul essai de l'étape, avec `charger=` donné : la condition est fausse d'office) ; l. 170-189 (`charger_reel` essayé sur processeur, sans `Arret`).
- Écrit : `if charger is None and CARTE not in carte: raise base.Arret(…)`.
- Problème : une garde d'arrêt doit être essayée sur un cas sain et sur un artefact (R5). Ici aucun essai ne la franchit, ni dans un sens ni dans l'autre ; une faute de frappe (`CARTE`, sous-chaîne, nom rendu par `get_device_name`) ne se verrait qu'en location. Le prix est le chargement de 16 Go avant de refuser.
- Devrait être : rendre le contrôle indépendant du chargement (paramètre `carte_exigee=CARTE`, `None` seulement dans l'essai qui le dit) ; deux essais : carte « NVIDIA A100-SXM4-40GB » acceptée, carte « NVIDIA A100-SXM4-80GB » (et « processeur ») refusée par `Arret` avant `mesurer` (il suffit de remplacer `charger_reel` par une fonction qui rend ces noms) ; si possible lire la carte (`torch.cuda.get_device_name`) avant de charger les poids.

**M3. Repli silencieux sur l'empreinte du préenregistrement versé.**
- Fichier : `audit_invariance_lot_v2.py` l. 206 et 211 ; essai l. 121.
- Écrit : `"sha256": base.sha256(prereg) if prereg.exists() else None`.
- Problème : le chemin est bon (`PREREG` pointe sur le v2, et le dépôt réduit v11 l. 56 le copie), mais si le fichier manque la course se poursuit avec un résultat scellé qui ne porte aucune empreinte, sans arrêt : c'est le repli que R5 interdit et l'objet même de M2 de la v1 (traçabilité R1/R6). L'essai ne vérifie que le chemin, pas qu'une empreinte non nulle est rendue (dans le dépôt temporaire le fichier est absent : `None` passe).
- Devrait être : `if not prereg.exists(): raise base.Arret("préenregistrement de l'essai absent du dépôt")` ; et un essai qui crée le fichier dans le dépôt temporaire et vérifie `sha256` = empreinte du fichier, plus un essai qui l'enlève et attend l'arrêt. Idéalement comparer à l'empreinte scellée (`.sha256`) du fichier.

## Mineures

**m1. C2 et C4 exigés aussi pour « réfutée » : régression par rapport à ce que la v1 admettait.** `lire_issue` l. 167 ; § 4. La contre-lecture v1 disait de garder « réfutée » avec C1 et C3 (et C3b) seuls. C2 et C4 protègent « établie » (mesure sensible, ablation active) ; une divergence 16/64 observée avec C1, C3 et C3b tenus est un fait quelle que soit C2, et la ranger en « indéterminé » masque la bascule de l'issue la plus lourde du § 4. La règle est cohérente entre texte et code, donc pas de choix après coup ; mais l'issue sort moins informative que nécessaire. Devrait être : « réfutée » = C1, C3, C3b tenus et une tâche du lot 64 différente ; C2 et C4 exigés pour « établie » seulement (ou, si on garde la règle, le dire comme choix prudent et rapporter dans l'issue « indéterminé » le nombre de tâches différentes). Les trois « témoins » C1 à C3b sont suffisants pour l'attribution à l'effet du lot.

**m2. Textes périmés du module.** l. 11 : renvoie au préenregistrement **v1** (`PREREG` l. 42 est bon) ; l. 22-24 : liste seulement C1 à C3 (pas C3b, C4). Devrait être : v2 et les cinq témoins.

**m3. m5 de la v1 non corrigé.** `ECHEANCES` inchangé (module : attendu 0,05 + 0,1 + 0,2 + 0,3 = 0,65 h, pire 1,8 h) contre le § 7 (étapes hors montage : attendu 0,2 à 0,4 h, pire 1,6 h). Sans effet sur la garde ; devrait être aligné ou noté au § 7.

**m4. m7 de la v1 à demi corrigé.** Branche par défaut et expression régulière du `RUN_ID` corrigées (amorce l. 55 et 72). Restent : en-tête l. 37 (« BRANCHE_RESULTATS (calcul/neuron-lens-b-alpha-v1) » : le défaut cité est faux), message de commit l. 154 (« Neuron Lens, B-α : … »), fichiers d'état en `…-b-alpha`. Cosmétique ; devrait être dit ou changé. `CARTE_ATTENDUE` reste facultative dans l'amorce ; la garde de l'étape (M2) devient alors la seule en cas d'oubli : raison de plus pour l'essayer.

**m5. L'essai à blanc ne prouve pas le refus d'un identifiant ou d'une branche de B-α.** `essai_a_blanc…_v2.sh` l. 200 : le cas code 17 passe `RUN_ID=20261120-neuron-lens` (forme invalide quelconque) ; aucun cas avec un identifiant en `…-neuron-lens-b-alpha`, et aucun avec `BRANCHE_RESULTATS` vide pour voir le défaut. Devrait être : un cas `RUN_ID=20261120-100000-neuron-lens-b-alpha` attendant 17.

**m6. M2 de la v1 corrigé au minimum seulement.** Le manifeste reste celui de B-α (`tranche`, texte gelé B-α, entropie 20261114, tâches `b-alpha-intervalles*`, `decisif: true`) ; la déclaration est au § 3 du préenregistrement et au champ `manifeste_note` du résultat, ce que la v1 admettait en repli. Acceptable ; à garder visible dans la lecture finale.

**m7. C1 est vrai par construction.** (lots différents = formes d'entrée différentes) ; il ne tombe qu'avec l'artefact « lot ignoré », ce que l'essai l. 154-159 couvre. Aucune correction, à ne pas présenter comme un témoin de sensibilité.

**m8. Hors pièces, à vérifier côté mère.** Le registre `registres/go.md` de cette branche ne contient pas `GO-2026-11-17-04` (la ligne `GO-2026-11-14-06` parle d'une RTX 4090 à 0,90 USD/h) ; le préenregistrement dit l'avenant inscrit sur `main` (commit `83fe2c55`, présent dans le dépôt) : le feu de la mère doit le citer.

## (a) Les points de la v1, un par un
| point v1 | état | remarque |
|---|---|---|
| B1 non-déterminisme du lot 64 | corrigé | C3b (l. 137, 150, 163), `lire_issue` l. 167, essai `test_artefact_instable_au_seul_lot64` (C3 tient, C3b tombe, « indéterminé ») |
| M1 ablation qui agit | corrigé | C4 chiffré à 90 % (`SEUIL_C4`), écarts des lots 1 et 7 rapportés, produit matriciel bf16 informatif ; réserve : M1 de cette lecture |
| M2 manifeste | minimum | m6 |
| M3 chargement réel | corrigé | `charger_reel` factorisé, essayé sur processeur avec un faux `transport.py` ; l'essai à blanc exerce le vrai `main` (`suite`, `preparer`) ; reste M2 (carte) |
| M4 branche et identifiant | corrigé | défaut, expression régulière, essais ; reste m4, m5 |
| m1 fenêtre de 9 | corrigé | préenregistrement § 3, essai l. 25 |
| m2 lignes citées | corrigé | « l. 216-246 », « l. 256 avant correctif, l. 264 après » |
| m3 demi-précision | corrigé | `taches_identiques_demi_precision`, non décisif |
| m4 lentilles | déclaré | § 6 et devis (poste tokeniseur/poids) |
| m5 échéances | non corrigé | m3 ci-dessus |
| m6 tables de l'essai à blanc | corrigé | JETON et EN_LIGNE comparés (l. 209-217), mention périmée retirée |
| m7 textes périmés | à demi | m4 ci-dessus ; carte contrôlée par l'étape (mais M2) |
| m8 essais trop larges | corrigé | `Sourd` exactement « indéterminé » ; « lot ignoré », « non-déterminisme », « ablation inerte » ajoutés |

## (c) Points demandés
- **Tous les témoins, C2 compris, pour les deux issues décisives** : cohérent entre § 4 et `lire_issue` (`not (c1 and c2 and c3 and c3b and c4)` → « indéterminé », sinon `ident`). Défaut de fond limité : m1 (« réfutée » n'a pas besoin de C2 ni de C4). Aucune autre combinaison non classée : toute combinaison des cinq témoins et de `ident` mène à une issue.
- **Cohérence préenregistrement / `lire_issue`** : bonne, sauf le manque de M1 (lots 1, 7 absents de la lecture).
- **Chemin du préenregistrement versé** : bon (v2, copié par le dépôt réduit v11, relatif à `ctx.racine`) ; défaut : M3 (`None` silencieux), m2 (docstring v1).
- **Contrôle de la carte** : substance juste (`"A100-SXM4-40GB" in "NVIDIA A100-SXM4-40GB"`), mais jamais essayé : M2.

## (d) Devis du § 7, recalculé
- Jetons par couche (padding au plus long de la passe, longueurs uniformes sur [24, 256], moyenne ≈ 140, maximum d'une passe de 16 tâches ≈ 245 à 256) : lot 16 : 4 passes × 32 lignes × ≈ 245 ≈ 31 000, joué trois fois (référence, rejeu, perturbée) ≈ 94 000 ; lot 64 : 128 lignes × ≈ 256 ≈ 33 000, joué deux fois (référence, rejeu) ≈ 65 000 ; lot 1 : 64 passes × 2 lignes ≈ 18 000 ; lot 7 : 10 passes × 14 lignes ≈ 31 000. Total ≈ 208 000 par couche, ≈ 625 000 sur trois couches (v1 : 530 000 ; l'ajout de C3b pèse ≈ 100 000).
- Calcul : 2 × 8 · 10⁹ × 625 000 ≈ 10 pétaflops (plus la tête de lecture, ≈ 25 téraflops, négligeable) ; à 100-150 téraflops soutenus : 1 à 2 minutes ; avec les `.cpu()`, empreintes (≈ 6 Go hachés), comparaisons et les 64 passes à 2 lignes : 3 à 6 minutes, plus 1 à 3 minutes de chargement des poids. L'attendu « 0,1 à 0,3 h » (6 à 18 minutes) et le pire cas 1,0 h sont conservateurs ; justes.
- Mémoire vive : une série = 64 × 9 × 128 256 × 4 octets ≈ 296 Mo ; 7 séries par couche ≈ 2,1 Go ; au passage de couche, `ref`, `rejeu`, `rejeu64` et `pert` de la couche précédente vivent encore : pic ≈ 3,2 Go. Négligeable. Mémoire de la carte : 16 Go de poids + (128 × 256 jetons : crochet cloné 0,94 Go, activations du MLP quelques Go, attention) ≈ 22 à 25 Go sur 40 : sans risque.
- Totaux : attendu 0,15 à 0,2 + 0,1 + 0,1 à 0,3 = **0,35 à 0,6 h** (écrit « ≈ 0,4 à 0,6 » : le bas est 0,35, arrondi vers le haut, sans conséquence) ; pire 2,2 + 0,6 + 1,0 = **3,8 h** (juste). Coût à 0,62 USD/h : 0,22 à 0,37 USD (écrit 0,25 à 0,4 : juste à l'arrondi) ; au prix maximal 0,73 : 0,26 à 0,44. Pire cas 3,8 × 0,62 = 2,36 USD > plafond de 2 USD : tronqué (écrit). Minuterie : 0,9 × 2 / 0,73 = 2,47 h ≈ 2,5 h (juste) ; arrêt dur 1,80 USD = 2,47 h à 0,73. Ligne GO : 3,4 à 4,0 + 2 = 5,4 à 6,0 sur 12 ; « ≈ 5,8 » est le haut de la fourchette moins 0,2 : écrire « 5,4 à 6,0 » serait plus net (mineur).

## À faire avant scellement (v3)
M1, M2, M3 ; m1 à trancher (garder ou assouplir, dit au préenregistrement) ; m2, m3, m4, m5 faciles ; régénérer le dépôt réduit (v12, R12), rejouer l'essai à blanc, nouvelle contre-lecture brève sur les seuls points touchés.

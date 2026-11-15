# Contre-lecture du correctif « version CUDA de l'hôte » de l'étape B bis de T0.7, v1

**Verdict : scellable après corrections.** Le correctif lui-même (garde d'offre `cuda_max_good` ≥ 13.0, contrôle de l'en-tête de
`nvidia-smi` dans les deux amorces) est juste, sans repli silencieux, et ne change aucun autre comportement. Mais l'amorce de
répétition de ce commit **ne peut pas servir telle quelle à une nouvelle passe payante** : la branche de sortie qu'elle exige
absente existe déjà sur le dépôt distant depuis la passe du 15 novembre (majeur M1). Une réserve d'argent s'y ajoute (M2).

**Déclaration** : contre-lecteur neuf, aucun fichier de l'étape B bis écrit par moi ; rien lu ni écrit sous `diag/`, `donnees/`,
`docs/verdicts/` ; aucune entrée de 7a ou 7b ; aucune valeur de clé lue ; aucun appel au service de location, aucune machine,
aucune dépense ; seul appel réseau : deux `git ls-remote` en lecture sur le dépôt de travail. Aucun commit, aucune poussée ; seul
fichier écrit dans la copie : ce rapport et son compagnon. Mutations jouées sur une copie jetable hors de la copie de relecture.

- **Date (UTC)** : 2026-11-15.
- **Objet** : copie détachée `/home/user/relecture-bbis-cuda-v1`, commit `c904db74` (parent `0f3d929b`), différentiel
  `git diff 0f3d929b c904db74` (11 fichiers, 319 lignes ajoutées, 19 retirées).
- **Rapport du développeur** : `brouillons/T0.7-etape-B-bis-v1/code/corrections-cuda-hote-v1.md`, empreinte
  `d85c99a1340abebe9e943426a7264449732004088e60af10c42a6a860b66f0c1`, conforme à son compagnon.
- **Traces lues** (`git show 56f5b8b8:traces/bbis-t07-repetition-v1/…`) : `journal-repetition.txt` (installation 118 s, puis
  « ARRET : torch ne voit pas la carte »), `nvidia-smi.txt` (« NVIDIA A100-SXM4-80GB, 81920 MiB, 570.211.01 »),
  `pip-verbeux.txt` (roues `cuda-toolkit==13.0.3`, `nvidia-cuda-runtime==13.0.96.*`). La cause donnée par le développeur est
  cohérente avec les traces ; `requirements-gpu.txt` (lignes 3 à 6) disait déjà d'exiger un hôte à 13.0 au moins.

## Majeurs

**M1 — La branche de sortie de la répétition existe déjà à distance : la prochaine passe s'arrêterait en quelques secondes,
sans trace, machine louée pour rien.** `scripts/amorce_repetition_bbis_v1.sh`, ligne 34 : `BR_SORTIE=calcul/t07bbis-repetition-v1` ;
ligne 172 : `git -C "$D" ls-remote --exit-code origin "refs/heads/$BR_SORTIE" …; [ $? = 2 ] || arret "branche $BR_SORTIE présente
sur le dépôt distant (R12) ou dépôt injoignable" 2`. Or `git ls-remote origin 'refs/heads/calcul/t07bbis-repetition*'` rend
aujourd'hui `56f5b8b8… refs/heads/calcul/t07bbis-repetition-v1` (les traces de la passe du 15 novembre). L'arrêt tombe avant
`SORTIE_LIBRE=1` (ligne 173) : aucune trace poussée, code 2, instance laissée en marche jusqu'à la destruction par la mère. Le
contrôle CUDA neuf (ligne 247) n'est jamais atteint. Le correctif ne touche pas ce point et le rapport du développeur ne le dit
pas ; le lanceur (`commande`) ne le vérifie pas non plus avant d'imprimer la commande de création. Hors du différentiel, mais
bloquant pour l'usage annoncé du commit. Correction recommandée (R12 : nouvelle passe, nouveau nom ; la branche du 15 novembre
reste intacte) :
- ancien : `BR_SORTIE=calcul/t07bbis-repetition-v1` (ligne 34) ; nouveau : `BR_SORTIE=calcul/t07bbis-repetition-v1-passe2`
  (nom à fixer par la mère), avec la même retouche à la ligne 17 de l'en-tête et dans `tests/test_repetition_bbis_v1.py`
  (lignes 200, 220, 227, 391, 400) ;
- et, pour ne plus louer avant de le savoir, dans `scripts/lancer_repetition_bbis_v1.sh`, sous-commande `commande`, après le
  contrôle du commit — ancien : rien ; nouveau : `git -C "$RAC" ls-remote --exit-code origin "refs/heads/<branche de sortie>" >
  /dev/null 2>&1; [ $? = 2 ] || { echo "BBIS REPETITION REFUS : branche de sortie présente sur le dépôt distant ou dépôt
  injoignable"; exit 2; }` (lecture seule, gratuite), avec son essai (cas sain, artefact).
- Autre voie, que je ne recommande pas : renommer ou supprimer la branche distante du 15 novembre (geste sur le dépôt distant,
  donc nœud de Lazar, et contraire à l'esprit de R12).
La branche de sortie de la course (`donnees/t07-etape-b-bis-v1`) est, elle, absente du dépôt distant à cette heure.

**M2 — Le plafond de 3 USD est calculé par passe, pas en cumul (réserve d'argent, aucune ligne changée par le correctif).**
`scripts/repetition_carte_bbis_v1.py`, `garde_commande` (lignes 300 à 314) : `cout = (duree_h + QUART_D_HEURE) * float(prix) +
MARGE_USD`, refus si `cout >= PLAFOND_USD`. La dépense de la passe du 15 novembre n'y entre pas : une seconde passe peut être
permise jusqu'à presque 3 USD à elle seule. Le mot R-2802 parle d'« une seule machine » et d'un plafond « de la répétition ».
À trancher par la mère avant le feu, sans changement de code obligatoire : soit le mot de Lazar ouvre un plafond neuf pour la
seconde passe, soit la mère relève la dépense de la première et choisit une échéance telle que première passe + coût maximal de
la seconde reste strictement sous 3 USD (et le dit dans le feu écrit). La sous-commande `depense CUMUL_USD PRIX` existe pour le
cumul en cours de passe ; elle ne remplace pas ce choix d'échéance.

## Mineurs

**m1 — Les essais neufs ne verraient pas une comparaison de texte dans l'amorce.** `tests/test_repetition_bbis_v1.py`, essai
`test_cuda_du_pilote_avant_l_installation_dans_les_deux_amorces` : les versions jouées sont 13.0, 13.2, 14.1 et 12.8 seulement.
Mutation jouée dans les deux amorces à la fois (`if [[ "$v" < "13.0" ]]` à la place de la comparaison d'entiers) : **2 passed**,
alors que ce code accepterait 9.2 et refuserait 100.0. Le code livré est juste (voir point 2) ; c'est l'essai qui ne le garde
pas. Correction :
- ancien : `cas = {"sain": ENTETE_SAIN, "sain-13.2": …, "sain-14.1": …,` et boucle `for nom in ("sain", "sain-13.2", "sain-14.1")` ;
  nouveau : ajouter `"sain-13.10": ENTETE_SAIN.replace("13.0", "13.10")` et `"sain-100.0": ENTETE_SAIN.replace("13.0", "100.0")`
  aux cas acceptés, et un cas refusé `"vieux-9.2": ENTETE_SAIN.replace("13.0", "9.2")` attendu au code 2 avec « pilote trop
  ancien : CUDA 9.2 ».

**m2 — En cas d'en-tête illisible, le journal ne dit pas ce qui a été lu ; dans la course, rien d'autre ne survit.** Bloc
`cuda-du-pilote`, `scripts/amorce_bbis_v1.sh` ligne 85 et `scripts/amorce_repetition_bbis_v1.sh` ligne 140. Dans la course,
l'arrêt de l'étape 1 ne pousse aucune trace (voulu) : `nvidia-smi-entete.txt` disparaît avec l'instance et la mère n'a que le
journal de l'instance. Correction (même texte dans les deux amorces) :
- ancien : `v=$(cuda_du_pilote "$1") || arret "version CUDA servie par le pilote illisible (…) …" 2` ;
  nouveau : `v=$(cuda_du_pilote "$1") || { j "lignes « CUDA » lues dans l'en-tête : $(grep -a 'CUDA' "$1" 2>/dev/null | head -n 3
  | cut -c1-200 | tr '\n' ' ')"; arret "version CUDA servie par le pilote illisible (…) …" 2; }`.

**m3 — Forme réelle de l'en-tête non éprouvée dans un conteneur : un hôte bon pourrait être arrêté.** Déclaré par le
développeur (§ 4, point 5). Les traces du 15 novembre ne gardent que la ligne `--query-gpu`, et aucun fichier du dépôt (hors
dossiers interdits) ne porte un en-tête réel. Dans un conteneur, `nvidia-smi` peut afficher « CUDA Version: N/A » quand la
bibliothèque CUDA du pilote n'y est pas montée : l'amorce s'arrêterait alors (code 2, « illisible ») sur un hôte peut-être bon.
L'arrêt est conforme à la règle « aucun défaut deviné » et, dans ce cas précis, torch ne verrait sans doute pas la carte non
plus ; je ne demande pas de repli. Conditions : (i) la répétition éprouve ce point et pousse `nvidia-smi-entete.txt` dans ses
traces (arrêt ou fin) : la mère le lit avant le feu de la course ; (ii) la course emploie **la même image** que la répétition.

**m4 — Nouvel arrêt sans essai d'artefact (R5).** `scripts/amorce_repetition_bbis_v1.sh` ligne 153 et `scripts/amorce_bbis_v1.sh`
ligne 133 : `nvidia-smi > "$X/nvidia-smi-entete.txt" 2>&1 || arret "carte invisible (nvidia-smi, en-tête)" 2`. Le faux
`nvidia-smi` des essais réussit toujours sans argument : cet arrêt n'est joué par aucun essai. Correction : dans le faux outil,
ancien : `[ "$#" = 0 ] && { echo "| NVIDIA-SMI … |"; exit 0; }` ; nouveau : `[ "$#" = 0 ] && { [ "${FAUX_ENTETE:-}" = echec ] &&
exit 9; echo "| NVIDIA-SMI … |"; exit 0; }`, et un cas `({"FAUX_ENTETE": "echec"}, "carte invisible (nvidia-smi, en-tête)")`
dans `test_machine_carte_jeton_outils_et_torch`.

**m5 — Entier géant : trace d'erreur et code 1 au lieu d'un refus écrit, code 2.** `src/controle_ia/t07bbis/registre_bbis_v1.py`,
`faute_cuda_hote` : `v = float(valeur)` lève `OverflowError` sur un entier JSON de plus de 308 chiffres (joué : code 1 par les
trois chemins, aucun OFFRE.json écrit). Ce n'est pas une acceptation, et la sous-commande `commande` refuse bien (code non nul),
mais le tableau des codes dit « 2 refus, motif écrit ». Correction :
- ancien : `v = float(valeur)` ; nouveau : `try: v = float(valeur)` / `except OverflowError: return f"cuda_max_good non fini
  (entier hors de portée)"`.

**m6 — Motif trompeur près du seuil.** Même fonction : `f"cuda_max_good {v:g} < {CUDA_MAX_GOOD_MIN:g} …"` ; joué avec
12.999999 : « cuda_max_good 13 < 13 ». Le refus est juste, le texte non. Correction : ancien : `{v:g}` ; nouveau : `{valeur!r}`
(l'essai attend « cuda_max_good 12.8 < 13 », inchangé).

**m7 — Lecture de l'en-tête : deux tolérances sans conséquence pratique.** Deux « CUDA Version: » sur une même ligne : la
dernière est prise (le compte se fait par ligne) ; « 13.0abc » est lu 13.0. Aucune sortie connue de l'outil n'a cette forme ;
à noter seulement.

**m8 — Version de l'outil.** L'outil installé lu ici est `vastai` 1.8.3 ; le rapport dit que la mère joue 1.11.0. Le champ
est vérifié dans 1.8.3 seulement. À noter aussi : dans 1.8.3, `vastai/data/instance.py` ligne 70 déclare `cuda_max_good:
Optional[str]` pour une **instance** (texte), contre `Optional[float]` pour une **offre** (`vastai/data/offer.py` ligne 26) :
si une relecture après création venait un jour à contrôler ce champ, `faute_cuda_hote` (nombre seulement) refuserait à tort.

**m9 — Suites à tenir (déclarées par le développeur, confirmées).** `SCRIPT_SHA256` et l'empreinte de l'amorce changent ; la
fiche de `CODE-BBIS` doit être écrite sur le commit final (trois de ses fichiers changent : `scripts/amorce_bbis_v1.sh`,
`scripts/lancer_bbis_v1.sh`, `src/controle_ia/t07bbis/registre_bbis_v1.py`) ; les corrections ci-dessus donnent un commit neuf,
donc une vérification courte du différentiel avant le feu.

## Les six points demandés

### 1. Garde `cuda_max_good` ≥ 13.0 — tenue, répétition et course

- **Champ** : `cuda_max_good` est bien le nom dans l'outil installé (`/home/user/vastai-env`, `vastai` 1.8.3, code lu, service
  non appelé) : `vastai/api/query.py` ligne 117 (champ de recherche des offres) et ligne 169 (alias `cuda_vers` →
  `cuda_max_good`) ; `vastai/data/offer.py` ligne 26 (`cuda_max_good: Optional[float]`) ; `vastai/cli/display.py` lignes 61, 90,
  117 (colonne « CUDA ») ; `vastai/cli/self_test/machine_diagnostics.py` ligne 170. Les renvois du rapport sont exacts. Le type
  « facultatif » confirme qu'un `null` est possible : il est refusé.
- **Chemins** : course — `lancer_bbis_v1.sh offre` et `commande` (qui rejoue `offre` avec l'identifiant) passent par
  `registre_bbis_v1.exiger_offre` ; répétition — `offre-depuis-recherche` (`offre_depuis_recherche`), `offre` et `commande`
  (qui rejoue `offre`) passent par `exiger_offre` du script. Une seule fonction, `faute_cuda_hote`, un seul seuil,
  `CUDA_MAX_GOOD_MIN = 13.0`, importé par la répétition. Aucun autre chemin ne fabrique ni n'accepte une offre.
- **Valeurs jouées par les trois chemins** (lanceurs réels, fichiers jetables) : 13.0, 13, `13.0e0` → acceptées (code 0,
  OFFRE.json écrit avec `cuda_max_good`) ; 12.8, 12.999999, −13.0, texte `"13.0"`, `true`, `null`, `NaN`, `Infinity`,
  `-Infinity`, `1e400`, liste, objet, clé absente → code 2, motif écrit, aucun OFFRE.json écrit ; entier géant → code 1 (m5).
  **Aucun repli silencieux.**
- **Chaîne de recherche** : analysée hors ligne par `vastai.api.query.parse_query` de l'outil installé : `cuda_max_good` →
  `{'gte': '13.0'}`, `cpu_ram>=128` → 128 000 (multiplicateur de l'outil), `gpu_name=A100_SXM4` → « A100 SXM4 ». La forme est
  acceptée par 1.8.3.

### 2. Contrôle de l'en-tête de `nvidia-smi` — juste

- Bloc `cuda-du-pilote` identique dans les deux amorces (comparé par `diff`, et par l'essai).
- **Lecture** jouée sur le bloc extrait : une ligne → lue ; aucune, deux lignes, fichier vide ou absent → code 2 ; 13.0, 13.00,
  13.10, 14.1, 100.0 → acceptées ; 12.8, 12.99, 9.2, 08.5, 09.9 → code 2 « pilote trop ancien » ; « 13 », « 13. », « .13 »,
  « 13,0 », « N/A », « ERR! », « 13.0.1 », « -13.0 », « 1e2 », 1000.0, tabulation, minuscules → code 2 « illisible » ; fin de
  ligne Windows et ligne sans saut final → lues. La comparaison porte sur la **partie entière seule, en base 10 forcée**
  (`$((10#${v%%.*}))`, ligne 141 de la répétition, 86 de la course) : ni comparaison de texte ni nombre à virgule ; 13.10 et
  9.2 sont donc bien traités, et « 08 » ne casse pas l'arithmétique. Le seuil étant 13.0, ignorer le mineur est exact.
- **Place** : répétition — capture à l'étape 1 (ligne 153), contrôle ligne 247, après `preparer_depot` et avant
  `python3 -m venv` et `installer_paquets` ; course — capture ligne 133, contrôle ligne 134, avant le clonage (ligne 139), la
  sortie de 7b et `pip install` (ligne 216). Avant toute installation dans les deux.
- **Code** : 2 dans les deux amorces — « garde » au tableau de la répétition (en-tête, ligne 21) ; dans la course, celui de
  tous les arrêts d'avant la marche, dont « torch ne voit pas la carte » (ligne 218), gardé en place.
- **Traces** : répétition — `SORTIE_LIBRE=1` posé par `preparer_depot` : l'arrêt pousse les traces, `nvidia-smi-entete.txt`
  compris (`traces` copie tout `$X`) ; course — arrêt de l'étape 1, aucune trace poussée, « stopped » demandé, comme « carte
  invisible ». Cohérent avec la place ; voir m2.
- L'essai local (`AMORCE_ESSAI_LOCAL=1`) sort avant le bloc dans les deux amorces : aucun effet sur le lanceur.

### 3. Amorce de répétition du dossier et du commit — identiques

`sha256sum scripts/amorce_repetition_bbis_v1.sh` et `git show c904db74:scripts/amorce_repetition_bbis_v1.sh | sha256sum` :
`75456e8c6c5dcd883006fd674dd6cc23e067984300da7fde61d3506ce1b50788` des deux côtés ; arbre de travail propre. La comparaison du
lanceur (`cmp -s`, `lancer_repetition_bbis_v1.sh` ligne 70) passera si la mère donne `c904db74` — ou le commit des corrections.

### 4. Aucun autre comportement changé — confirmé

Différentiel lu en entier. `MIN_ESSAIS=87` inchangé (ligne 41 de l'amorce de la course) ; code de mesure, seuils, garde de
dépense, garde de création, minuterie, destruction et vérification de l'absence, `requirements-gpu.txt` : aucune ligne
touchée. Les seules lignes retirées sont des commentaires d'en-tête, des gabarits d'offre des essais et le message « OFFRE
ECRITE » (complété). Seuls ajouts de comportement : la garde d'offre, la seconde lecture de `nvidia-smi` (nouvel arrêt « carte
invisible (nvidia-smi, en-tête) », m4) et le contrôle de l'en-tête. Sur l'instance, le script de la répétition importe deux
noms de plus du même module déjà importé : aucun risque neuf d'importation.

### 5. Essais

- **Compte exact** (`PYTHONPATH=src … -m pytest -q -p no:cacheprovider tests/test_t07bbis_*.py tests/test_repetition_bbis_v1.py`,
  dans la copie, commit `c904db74`) : **135 passed, 4 warnings in 217.17s**, code 0 ; 135 essais collectés, dont 25 dans
  `tests/test_repetition_bbis_v1.py` et 110 dans `tests/test_t07bbis_*.py`. Conforme au compte du développeur.
- **Mutations rejouées par moi** (copie jetable, essais « cuda » seuls ; témoin sans mutation : 3 passed) :

| mutation | essais neufs |
|---|---|
| `math.isfinite` retiré (NaN et infini acceptés) | échec (2) |
| booléen toléré | échec (1) |
| texte toléré | échec (2) |
| garde retirée de `offre-depuis-recherche` | échec (1) |
| garde retirée de `offre` (répétition) | échec (1) |
| garde retirée de `exiger_offre` (course) | échec (1) |
| amorces : seuil 12 au lieu de 13 | échec (1) |
| amorces : en-tête illisible toléré | échec (1) |
| amorces : premier en-tête pris quand il y en a deux | échec (1) |
| course : contrôle déplacé après le clonage | échec (1) |
| répétition : contrôle déplacé après l'installation | échec (1) |
| une seule amorce modifiée (blocs différents) | échec (1) |
| **amorces : comparaison de texte au lieu d'entiers** | **passe (m1)** |
| amorces : base 10 non forcée | passe (sans effet sur une version réelle ; « 08.x » n'existe pas) |

  Les essais neufs attrapent donc chaque défaut demandé, sauf la comparaison de texte (m1) et l'arrêt neuf de la seconde
  lecture de `nvidia-smi` (m4).

### 6. Les cinq choix du développeur

1. **Place du contrôle de la course avant le clonage — acceptable.** Arrêt au plus tôt, au même rang et au même code que
   « carte invisible » ; aucune trace n'est possible avant le dépôt, par construction. Condition : m2 (dire dans le journal ce
   qui a été lu). La place de la répétition (après le dépôt, pour pousser les traces) est le bon choix : c'est elle qui doit
   nous apprendre la forme réelle de l'en-tête.
2. **Forme stricte de `cuda_max_good` (nombre JSON seulement) — acceptable.** L'outil déclare un nombre pour une offre
   (`offer.py` ligne 26) ; refuser le texte ne coûte qu'un refus local, gratuit, avant toute location. Plus sûr que le
   précédent de T0.6. Retouches m5 et m6.
3. **Version lue dans l'en-tête plutôt que déduite du numéro du pilote — acceptable**, sous la réserve m3 (forme réelle non
   éprouvée ; la répétition l'éprouve ; même image pour la course). Un tableau pilote → CUDA serait une seconde chose à tenir
   juste.
4. **Pas de construction automatique de l'offre de la course — acceptable pour ce correctif, à signaler à la mère.** La
   valeur de `cuda_max_good` de la course est recopiée à la main : la garde locale ne vérifie alors que ce qui a été tapé.
   Le contrôle de l'amorce rattrape une erreur de recopie, mais au prix d'une création (et la ligne de GO n'en permet qu'une
   relance). Recommandation, hors de ce correctif : une sous-commande `offre-depuis-recherche` pour la course, sur le modèle de
   la répétition, avant le feu de la course ; à défaut, la mère joint RECHERCHE.json à OFFRE.json.
5. **Commande de recherche écrite en commentaire — acceptable.** Le filtre de l'outil n'est qu'une aide, la garde locale
   décide ; la chaîne s'analyse correctement dans l'outil installé (point 1). Elle remplace bien celle du rapport v2 de la
   répétition, non réécrit (R12). Non vérifié : l'outil 1.11.0 de la mère (m8).

## Ce qui reste non éprouvé

Forme réelle de l'en-tête de `nvidia-smi` dans le conteneur loué ; présence et type de `cuda_max_good` dans une recherche du
jour ; outil 1.11.0 de la mère ; aucune passe sur carte avec ce code. La répétition est faite pour cela — une fois M1 levé.

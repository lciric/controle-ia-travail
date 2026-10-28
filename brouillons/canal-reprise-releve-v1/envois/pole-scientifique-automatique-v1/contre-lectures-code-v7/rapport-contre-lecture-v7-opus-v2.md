# Contre-lecture du code de l'orchestrateur v7 (versions 4 à 9, écrites sous Opus 5.5) — rapport v2

Contre-lecteur : sous-agent neuf, Fable 5.1 (règle R2 : autre modèle que l'auteur). Début : 27 octobre 2026, 18:00:26 UTC
(`date -u`). Périmètre : ce que listent les LISEZMOI v4 à v9, plus `demonstrations/duel_proposeurs_v7.py` ; le reste de
`pole/` lu pour comprendre, non contre-lu. Aucun fichier du dépôt modifié ; aucune clé lue ni cherchée ; aucun appel de
modèle payant ; tout sur processeur, dans `/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-v7-opus-v2/`
(copie du code dans `copie/`, essais et sorties dans `essais-cl/`).

**Ma copie date de 18:00 UTC ; le dossier source a changé à 18:08 UTC (version 10).** Je contre-lis ma copie (empreintes
v9 toutes vérifiées : `EMPREINTES-orchestrateur-pole-v7-v9.txt`, `a44d70b3…`, 99 lignes « OK » ; `duel_proposeurs_v7.py`
hors liste, `453ce794…`). La v10 ne touche que `pole/adaptateurs.py` (`4f381df9…`), `demonstrations/duel_proposeurs_v7.py`
(`e8b56a8a…`), `essais/test_v7_proposeurs_references.py` (`55febd2d…`), `essais/test_v7_duel.py` (`8ff28eec…`) ; j'ai lu
le diff : la correction « coût simulé jamais compté » est bien là (`replace(res, cout_declare_usd=0.0, cout_simule_usd=…)`)
et le pari apparié passe en forme « parts » seule avec contrôle de l'intervalle. **Elle ne corrige pas le constat 1
ci-dessous** (la réservation, pas le règlement, affame les bras à modèle).

## Verdict (trois lignes)

1. **À corriger avant le duel.** Tel qu'écrit, le script du duel ne compare pas des proposeurs : les bras à modèle ne
   jugent qu'**une** fiche non témoin par génération (réservation 1,5 USD > moitié du budget de génération 2,0 USD), les
   bras de référence les jugent toutes (500 USD) ; les quatre bras n'ont pas le même juge (instants de lecture 8 contre 6,
   part de calibrage 40 contre 12, paires de recombinaison 3 contre 2) ; et sans tranches, l'héritage de la preuve
   multiplie des e-valeurs calculées sur les **mêmes** issues (classe nulle promue 9,5 % contre α = 5 %).
2. Le juge lui-même (nul d'archive ajusté, règle e-BH, pari à fraction) tient, avec deux réserves de validité : le filtre
   `delta0` des filles agit après la règle e-BH (preuve rompue, enjeu pratique faible mesuré : 0 différence sur 2 000
   générations) et la signature de la mémoire ignore le moniteur (héritage entre hypothèses différentes).
3. Fuites et gardes : le contexte public du proposeur est propre, mais le bac à sable du kit d'agent **ne borne que les
   écritures** (« read access to the entire computer » par défaut) et la garde par motifs se contourne en une ligne : un
   proposeur réel peut lire la banque, les `mesures.json` des fiches sœurs et le journal. Correction d'une ligne
   (`sandbox.filesystem.denyRead`), à faire avant tout agent réel.

## Constats, du plus grave au moins grave

### C1 — Duel : les bras à modèle sont affamés par la réservation du budget ; une fiche jugée par génération
- Fichiers : `demonstrations/duel_proposeurs_v7.py` lignes 124-136 (`commande_modele` : `--budget-usd 6` sans
  `--budget-generation-usd` → `pole/pole.py` ligne 413 : budget de génération = 6/3 = 2,0 USD) ; `pole/cycle.py`
  lignes 603-613 (réservation par fiche = min(`cout_borne`, plafond expérimentateur 1,0) + plafond vérificateur 0,5 =
  1,5 USD ; **dès le premier refus de réservation, `arret_budget = True` et toute fiche suivante est « hors budget »**) ;
  bras de référence lignes 114-121 (`budget_generation_usd=500.0`, `executer_pole(..., 5000.0, ...)`).
- Ce qui est faux : dans une vague de quatre, la première fiche réserve 1,5, la deuxième ne peut pas (3,0 > 2,0), tout le
  reste de la génération tombe « hors budget », témoins exceptés (jugés sans agent). Les bras M-expl et M-aveugle jugent
  donc une seule fiche non témoin par génération ; mécanique et aléatoire jugent 6 puis 12 puis 12. La v10 met le coût
  simulé à zéro **au règlement**, mais la **réservation** se fait toujours aux plafonds : rien ne change.
- Reproduit : `essais-cl/duel-simule-1-monde` (`--moteur simule`, 1 monde) ; `essais-cl/resultat-verif-duel-simule.json`
  (`6dd575c9…`) : M-expl « hors budget » 5, 14, 4 et une seule non-témoin jugée par génération (G0-F02, G0-F05, G0-F06) ;
  M-aveugle 5, 15, 3 ; mécanique et aléatoire 0, 0, 0.
- Gravité : **lecture trompeuse** (L2 à L5 du devis ne mesureraient pas les proposeurs mais le budget) ; sous moteur réel,
  c'est de l'argent dépensé pour un proposeur dont les fiches ne sont pas jugées.
- Correction : réserver au coût attendu du rôle effectif (zéro pour un rôle simulé de l'adaptateur mixte : la réservation
  doit suivre la même règle que le règlement de la v10) ou passer `--budget-generation-usd` ≥ 1,5 × fiches lancées par
  génération + 0,5 ; et ne pas lever `arret_budget` tant que des réservations libérées peuvent revenir.

### C2 — Duel : le juge n'est pas le même dans les quatre bras
- Fichiers : `demonstrations/duel_proposeurs_v7.py` lignes 114-118 (références : `instants_filles=6`, `part_calibrage=12`,
  `max_paires=2`) contre lignes 124-136 (bras à modèle par la ligne de commande, qui n'expose ni `--instants-filles`, ni
  `--part-calibrage`, ni `--max-paires`, ni `--k-recombinaison` : `pole/pole.py` lignes 220-314 ; défauts 8, 40, 3).
- Ce qui est faux : les e-valeurs des fiches à membres ajustés sont lues à 8 instants au lieu de 6 ; la part de calibrage
  des filles vaut 40 au lieu de 12 (plans d'évaluation plus courts) ; trois paires de recombinaison au lieu de deux.
- Reproduit : manifestes des quatre bras (`resultat-verif-duel-simule.json`, clé `reglages`).
- Gravité : **lecture trompeuse** (confondant entre bras).
- Correction : jouer les quatre bras par le même chemin (`executer_pole` avec une seule `ConfigGeneration`, l'adaptateur
  mixte construit dans le script) ou exposer les quatre options sur la ligne de commande et les passer.

### C3 — Héritage de la preuve sur un monde sur banque sans tranches : produit d'e-valeurs sur les mêmes issues
- Fichiers : `pole/memoire.py` lignes 200-218 (`_indexer_classe` : `cumul += log_richesse_finale`) et 148-153 ;
  `pole/cycle.py` lignes 562-567 (`promue = cumul + log W max ≥ seuil`) ; `pole/monde_banque.py` lignes 116-127 (sans
  tranches, le réservoir est toute la partie d'épreuve : même loi → même plan par divergence → mêmes issues lues) ;
  `tranches=1` par défaut : `pole/pole.py` ligne 291, `demo_proposeurs_v7.py` ligne 90, `duel_proposeurs_v7.py` lignes 76,
  113 et 126-130 (jamais `--tranches`). Le chercheur mécanique (`proposeurs_references.py`, liste déterministe) repropose
  les mêmes lois à chaque génération : toute éliminée revient en redite héritière.
- Ce qui est faux : « le produit des e-valeurs sur des tirages frais reste une e-valeur » (`memoire.py` ligne 13) ; sur la
  banque sans tranches il n'y a pas de tirage frais. W·W' avec W' ≈ W n'est pas une e-valeur.
- Reproduit, deux fois. (i) Course simulée : `G2-F03` (bras mécanique, génération 2) est **la même loi** que `G1-F11`,
  jugée sur **150 instances sur 150 identiques, issues identiques**, avec un cumul hérité de +1,766
  (`resultat-verif-duel-simule.json`, clé `preuve_redites_heritieres_mecanique_gen2`). (ii) `essai_heritage_nul_connu.py`
  (`85cee5ed…`) : nul exact (issues d'épreuve tirées de la loi « connu » que le noyau ajuste lui-même), fiche = « connu »
  déformée (poids × 1,35), trois générations, chemin réel (`Generation.geler` + `_juger_temoin_sans_agent`, `Memoire.garde_redite`,
  règle de `_juger_pari`) : **mêmes données : classe promue 38 sur 400 (9,5 %, intervalle à 95 % 6,6-12,4 %) ; tranches
  fraîches : 17 sur 400 (4,25 %)** ; première tentative seule : 4,25 % (`resultat-essai-heritage-nul-connu.json`,
  `2e500c4b…`). Sous un nul i.i.d. strict (`essai_heritage_meme_donnees.py`, 4 bras × 400) l'inflation est nulle : la
  marginale ajustée domine toute loi fixe d'environ (K−1)/2·log n nats et log W de A ne dépasse jamais −0,9 — le risque
  est donc porté par les nuls dont le membre dominant est une loi fixe (le prédicteur connu, les survivantes de l'archive).
- Gravité : **garantie touchée** (et, avec `tranches=1`, l'exposition adaptative déclarée en v4 reste ouverte dans le duel
  : les verdicts montrés au proposeur portent sur les instances où ses prochaines fiches seront jugées).
- Correction : sur `MondeBanque`, exiger `tranches ≥ générations` dès que la mémoire hérite (ici 450 instances d'épreuve
  = 3 × 150 = 3 × `taille_plan` : aucune perte de plan) ; sinon remettre le cumul à zéro quand le plan ou les issues
  recoupent ceux d'une épreuve passée de la classe (empreintes des `mesures.json`).

### C4 — La signature de la mémoire ignore le moniteur (et la banque)
- Fichiers : `pole/memoire.py` lignes 96-103 (`signature` = (k, d, probabilités sur la sonde)), 134-146
  (`chercher_classe` compare à toute signature de même (k, d)), 155-174 (`_garde_signature`).
- Ce qui est faux : (i) une loi éliminée sur M0 avec log W final > 0 lègue son cumul à la même loi proposée sur M1
  (autre hypothèse, autres issues) ; (ii) une loi promue sur M0 interdit la même loi sur M1 (« redite d'une survivante »),
  donc la stratégie du catalogue `transposition_moniteur` (`simulation.py` lignes 404-409 ; `proposeur.py` ligne 39) ne
  peut jamais être jugée ; (iii) seuil de fusion 0,30 nat (calibré sur des lois de force 1,5 en dimension 2) trop large
  pour les lois douces du duel en dimension 4 : 116 paires sur 780 de lois aléatoires du gabarit fusionnent ; à la
  génération 2 du bras M-expl, **21 propositions sur 26 refusées** « classe G0-F02 déjà éprouvée dans cette génération ».
- Reproduit : `essai_memoire_moniteur.py` (`6fe613d7…`), `resultat-essai-memoire-moniteur.json` (`d07b5646…`) ; refus
  comptés dans `resultat-verif-duel-simule.json` (`gardes_de_redite`).
- Gravité : **garantie touchée** pour (i) ; **lecture trompeuse** pour (ii) et (iii) (le nombre de fiches jugées par bras
  dépend de la granularité des classes, pas du proposeur).
- Correction : mettre `moniteur` et l'empreinte de la banque dans la signature et la clé de classe ; recalibrer le seuil
  sur la loi de référence de la grammaire (d = 4, poids du gabarit).

### C5 — Règle e-BH : le filtre `delta0` des filles s'applique APRÈS la règle ; m compté après coup
- Fichiers : `pole/cycle.py` lignes 700-726 (`appliquer_multiplicite` : e-valeurs tirées de `trajectoire_log_w` seule,
  tri, k*, puis seules les « survit » non retenues sont rétrogradées) ; `nul_filles_v2.py` lignes 232-238 et
  `selection_pari.py` lignes 624-629 (la marge `gain ≥ 2·delta0` n'agit que sur `promue`, donc sur `verdict_final`).
- Ce qui est faux : une fille à forte e-valeur mais sans la marge est comptée dans k* (elle abaisse le seuil m/(α·k) des
  autres) sans être promue ; l'ensemble promu est une partie stricte de l'ensemble retenu, et E[V'/R'] n'est plus borné :
  le facteur d'inflation est k*/R' (au plus 1 + filles filtrées / promues). S'y ajoute `m = len(jugees)`, compté **après**
  les issues (ligne 702) alors que la docstring dit « fixé avant toute issue » (ligne 690) : une fiche indécise par la
  plomberie sort de m au lieu d'y rester avec e = 0.
- Reproduit par construction sur la vraie fonction (`essai_ebh_filtre_delta0.py`, `46982cc4…`, partie A : m = 3, F1
  filtrée à 4,1, N1 nulle à 3,6 → retenues {F1, N1}, promues {N1} ; corrigé → rien). Quantifié (partie B, 2 000
  générations, 15 nulles réelles de l'évaluateur, 3 filles filtrées plafonnées à exp(2·delta0·n) = exp(5,76), 2 témoins
  vrais) : **aucune différence** (V = 7, R = 4 007 dans les deux cas) — la marge plafonne l'e-valeur d'une fille filtrée
  et les nulles réelles restent loin des seuils.
- Gravité : **garantie touchée** (preuve), enjeu pratique faible mesuré.
- Correction (une ligne) : dans `log_e`, rendre −∞ quand `ev.get("marge_atteinte") is False` (e' = e·1{marge} reste une
  e-valeur), avant le tri ; prendre m = fiches lancées + témoins sans agent, e = 0 pour les non jugées.

### C6 — Le bac à sable ne borne pas les lectures ; la garde se contourne en une ligne ; la banque est lisible
- Fichiers : `pole/adaptateurs.py` lignes 149-150 (`sandbox` sans `filesystem.denyRead` ni `failIfUnavailable`) ;
  `pole/garde_outils.py` (docstring lignes 4-6 : « la barrière réelle reste le bac à sable (… dossier seul accessible) ») ;
  LISEZMOI v5 (« seul le bac à sable borne vraiment le système de fichiers et le réseau »).
- Ce qui est faux : la documentation du bac à sable du kit d'agent (code.claude.com/docs/en/sandboxing, lue le 27 octobre,
  copie `essais-cl/doc-sandboxing-code-claude-com-2026-10-27.md`, `1454b065…`) : « **Default read behavior**: read access
  to the entire computer, except certain denied directories » ; les écritures seules sont bornées au dossier courant ; de
  plus « if the sandbox cannot start … Claude Code shows a warning and runs commands without sandboxing » sauf
  `failIfUnavailable: true` (le pré-contrôle `exiger_bac_a_sable` couvre le cas des dépendances absentes, pas une panne
  ultérieure). La garde par motifs est donc la seule barrière de lecture, et elle passe : `cd "$(dirname "$(dirname
  "$PWD")")" && cat G0-F01/experience/mesures.json`, `find "$d" -name mesures.json -exec cat {} \;`,
  `python3 -c "… os.pardir …"`, `os.path.dirname(os.getcwd())`, chemin bâti par `chr(46)*2`, script shell ou python écrit
  par `cat <<'EOF'` (corps lu comme du « code ») puis lancé, lien symbolique créé par `ln -s "$(dirname …)"` puis
  `cat lien.json` (Read le refuse, Bash non) : **8 sur 8 autorisées, et chacune lit à l'exécution le secret du dossier
  voisin** (`essai_gardes.py`, `6ee6e5fd…` ; `resultat-essai-gardes.json`, `56f6d220…`). Dans le duel, le seul agent réel
  est le proposeur, dont le dossier est voisin des `mesures.json` de toutes les fiches, du journal (richesses) et à portée
  de la banque (toutes les issues d'épreuve).
- Gravité : **fuite** (soupçonnée pour le bac à sable réel : `bwrap` absent ici, vérification documentaire ; reproduite
  pour la garde). Le contexte public (`contexte-proposeur.json`, `developpement.json`) est propre : vérifié.
- Correction : `sandbox.filesystem.denyRead = [racine de la course, dossier de la banque, dossier du relais]` et
  `allowRead = [dossier de l'agent]` (exemple de la documentation : `denyRead ["~/"]` + `allowRead ["."]`),
  `failIfUnavailable: true` ; tenir la banque et les traces hors du système de fichiers visible de l'agent ; corriger
  les deux phrases.

### C7 — La clé du relais reste lisible dans `/proc/<pid>/environ` après « effacement »
- Fichiers : `pole/relais_reel.py` lignes 289-295 (`lire_cle` : `environnement.pop`) ; LISEZMOI v5 (« la clé n'y est lue
  qu'une fois, puis effacée »).
- Ce qui est faux : `/proc/<pid>/environ` expose l'environnement **initial** du processus ; `pop` ne le modifie pas.
  Reproduit (`essai_gardes.py` partie B : valeur retirée de `os.environ`, encore présente dans `/proc/<pid>/environ`).
- Gravité : **lecture trompeuse** ; fuite seulement si un agent partage l'utilisateur et l'espace de noms des processus
  du relais (le LISEZMOI recommande déjà un autre utilisateur).
- Correction : passer la clé par un descripteur ou un fichier à lecture unique, ou documenter que seul un autre
  utilisateur (ou conteneur) protège la clé.

### C8 — Essais : chemins non couverts, assertions faibles
- `essais/test_v7_plomberie.py` lignes 166-172 : « arrêt à la moitié » testé seulement avec **toutes** les fiches en
  panne (la frontière « 2 sur 4, 2 sur 5 » n'est pas exercée) ; lignes 245-261 : aucune des huit commandes de C6 dans
  les interdites. `essais/test_v7_proposeurs_references.py` lignes 159-170 : `--roles-reels` refusé « hors monde tenu par
  le noyau » n'asserte que le code 2, pas le motif. `essais/test_v7_pari_fraction.py` ligne 100 : borne du contrôle fatal
  = 0,05 + 3 écarts-types = 7,7 % (un dépassement réel à 7 % passerait). `pole/cycle.py` lignes 598-600 :
  `_juger_temoin_sans_agent` est hors du filet `_traiter_sur` : une exception imprévue de l'évaluateur arrête la
  génération au lieu de marquer une erreur d'orchestrateur (soupçonné, non reproduit). `test_v7_proposeur.py` ligne 123 :
  `unittest.main()` placé avant `class PhaseExploratoire` (découverte intacte, lancement en script tronqué).
- Gravité : **clarté** (les essais passent, mais ne tiennent pas tout ce que les LISEZMOI leur font dire).

### C9 — Lecture « structure retrouvée » et « sans lien »
- `duel_proposeurs_v7.py` lignes 100-105, `demo_proposeurs_v7.py` ligne 113 : lien = intersection **non vide** des
  traits ; une loi sur un seul trait d'une structure « trois traits » compte comme retrouvée ; « sans lien » (4 traits,
  2 ou 3 par structure) sous-estime les fausses découvertes au sens du monde. De plus m de la règle e-BH vaut 7 dans les
  bras à modèle (6 témoins + 1 fiche) contre 18 à 21 dans les références : seuils m/(α·k) plus doux pour le bras qui
  propose moins (inhérent à e-BH, à dire dans la lecture).
- Gravité : **lecture trompeuse**, faible.

### C10 — Reproductibilité et petits points
- `pole/outils.py` lignes 82-89 : graines par SHA-256 (`graine_derivee`) et non `numpy.random.SeedSequence` (R9) ;
  déviation déclarée dans le code et le manifeste (clarté, à faire figurer dans la lecture du duel). Manifestes des courses
  : empreintes de `pole/*.py` seulement ; ni les scripts de démonstration ni les générateurs de mondes ; l'empreinte de la
  banque n'apparaît que dans `ajuste_sur` du membre « connu ». `duel_proposeurs_v7.py` lignes 165-166 : `sortie-{nom}.txt`
  écrit sans scellement. Versions dans les noms et écriture scellée sans écrasement : tenues partout ailleurs.
- `pole/monde_banque.py` lignes 134-140 : `mesures` cherche par (z, g) dans toute l'épreuve, sans se restreindre à la
  tranche de la fiche : sur une banque à traits discrets (T0.5), une issue d'une autre tranche peut être servie
  (soupçonné, sans effet sur les mondes de la grammaire).
- `pole/proposeurs_references.py` lignes 123-131 : `par_sous_population` sans `defaut` ; une sous-population absente du
  développement ferait lever `TypeError` à l'évaluation (erreur d'orchestrateur ; soupçonné).
- `pole/relais_reel.py` ligne 52 : tout `/v1/` est relayé, dont `/v1/messages/batches`, dont la création ne porte pas
  d'usage : dépense non comptée par le plafond (soupçonné ; l'agent n'a pas le réseau par Bash).
- `pole/pole.py` lignes 393-398 : `--roles-reels experimentateur` en sélection « seuil » laisse un vérificateur simulé
  rejouer un expérimentateur réel (hors duel ; clarté).

## Ce qui tient (une ligne chacun)
- 202 essais passent en 222 s (`sortie-unittest-202.txt`, `4c38b095…`) ; empreintes v9 toutes « OK ».
- Nul d'archive ajusté : la mise en commun linéaire est bornée par l'écart de Frank-Wolfe et plafonnée à 0 ; les membres
  ordinaires ajustés (marginale, fenêtres, mélanges sur grille) sont des maxima sur la famille déclarée ; W reste sous un
  rapport de vraisemblance sous chaque membre ; les témoins ne reçoivent jamais de membre d'archive (`cycle.py` 400-402).
- Marge de Newton : λ² admis seulement près de l'optimum, 0 sinon ; départ = parent (J = 1) et montée monotone : la valeur
  domine toujours le parent lui-même (réserve théorique : λ² ne borne l'écart que pour une fonction autoconcordante, ce
  que le logit multinomial avec `log(PLANCHER) ≈ −27,6` n'est pas strictement ; conservateur en pratique, non démontré).
- Règle e-BH : arrêt au premier instant ≥ log(m/α) de la trajectoire propre (temps d'arrêt), k* et seuils m/(α·k) exacts,
  témoins comptés, héritage ajouté en logarithme (hors C3 et C5).
- Pari à fraction : mélange de prévisions prévisibles (marginale en ligne de Laplace), rapport martingale sous chaque membre
  ; équivalence grille {1} et borne log 4 vérifiées par les essais.
- Contexte du proposeur sans issue, richesse, motif ni témoin (`proposeur.py` 85-102) ; `developpement.json` = partie
  « developpement » seule, distincte du calibrage (répétition du duel, vérification 3) ; référence aléatoire aveugle
  (description seule) ; chercheur mécanique ne lit que `developpement["instances"]` (`proposeurs_references.py` 82).
- Traces de l'orchestrateur dans un dossier voisin ; copie pour rejeu sans réponse, consigne ni empreinte orpheline ;
  erreurs d'orchestrateur indécises et rejouables ; coûts gardés et réglés une fois ; états des dents.
- Garde : les cinq faux positifs de (a) passent ; Read/Write/Edit hors dossier refusés même par lien symbolique
  (`chemin_dans` résout les liens) ; variables sensibles, réseau, environnement refusés sur le texte entier.
- Bac à sable exigé hors faux moteur, jamais sous root ; faux moteur reconnu par `EST_FAUX_SDK` ; modèles réels bornés à
  Opus 5.5 et Fable 5.1 pour les rôles réels.
- Relais : réserve 0,40 par appel, dépassements comptés et journalisés, 402 au plafond, jeton factice exigé, chemins
  `/v1/` seuls, aucune clé ni corps dans le journal ; la répétition du duel prouve que seul le proposeur passe par le
  relais et que la clé factice n'apparaît nulle part.
- `--roles-reels` : refusé sans moteur réel ; refusé sans expérimentateur hors monde tenu par le noyau ; rôles inconnus ou
  liste vide refusés par `AdaptateurMixte` ; routage par rôle vérifié.
- v10 (hors de ma copie) : correction du coût simulé présente et juste ; pari apparié en forme « parts » seule avec
  contrôle de l'intervalle.

## Scripts d'essai et sorties (`essais-cl/`, empreintes SHA-256 complètes)
- `essai_ebh_filtre_delta0.py` — 46982cc40380e5a5bcfb38cc04adda51d9db99d45a0bb6fcea474e1beea90bdf ; sortie
  `sortie-essai-ebh-filtre-delta0.txt` — d4b805e846fdf8eeb6f20ca0fefbe96fceee21340596cac71be9c8a94b66ca91 ; résultat
  `resultat-essai-ebh-filtre-delta0.json` — 16aecae5b03743bf84f04a2786c9b1c125489e8e761c5c0e76ea62bf39bce43d.
- `essai_heritage_meme_donnees.py` — c5bd01dbce2ec718890462462d8002fcd9a58dc5f74e03ff4344ffe8629fa26d ; sortie
  `sortie-essai-heritage-meme-donnees.txt` — 9610ee5d76d97dd9b964e6ae697fab534e02f18d860e1e2d93a76bcb4af55ab6 ; résultat
  `resultat-essai-heritage-meme-donnees.json` — e3f145755225d193862d066b80eee29c14084f3dadd917f2e357b43c8df799e9.
- `essai_heritage_nul_connu.py` — 85cee5ed839a9f4632a83cf74b29c0b5a37f7879dbb7be978a721b54eaca7664 ; sortie
  `sortie-essai-heritage-nul-connu.txt` — 9edfaa46c473a3dd80096040f9df132a88554457e3de7af3f23fc0edd598df28 ; résultat
  `resultat-essai-heritage-nul-connu.json` — 2e500c4b29cbdd5da174757dc5dc4aff8b3ee73923132f4540af52ca10be2544.
- `essai_gardes.py` — 6ee6e5fd81a2bae36c775e4b53df5a95aae031f4ac239747a0797e8e8656da28 ; sortie `sortie-essai-gardes.txt`
  — 20f28a3e17aa433ce1be815e4f08ceafb0ce2a43ea7139af09286df6d8cebcfe ; résultat `resultat-essai-gardes.json` —
  56f6d220b671526b05066f84dcb7f2dda2480821b37f68b5cde032b1de01ecc1 ; documentation du bac à sable copiée
  `doc-sandboxing-code-claude-com-2026-10-27.md` — 1454b065eccbe31927e1cbfe2ab6f399a6c02cbc994ee44adad6f9d9e018c37d.
- `essai_memoire_moniteur.py` — 6fe613d77296be377f0c2e2da1578192ef3e8db274b8bb147b8c810c6e0d7057 ; sortie
  `sortie-essai-memoire-moniteur.txt` — ce903b66455d025117f2f439a407fd8323037ed154e4d4dc610a2a01ef449a0b ; résultat
  `resultat-essai-memoire-moniteur.json` — d07b5646f12ad6f8a24a1515a5ef40756e8ca239d8e1afe404cfc7b39c8f4973.
- Course du duel simulé (`copie/demonstrations/duel_proposeurs_v7.py DOSSIER --mondes 1 --moteur simule --arret-apres 1`,
  déterministe, rejouée une fois à l'identique) : `sortie-duel-simule-1-monde.txt` —
  627c44bb1ba61b7b7bfdb8403c55c20824add1223aa4dcf49f41e70cf02f2fbe ; `duel-simule-1-monde/duel-proposeurs-v7.json` —
  1f889ade52ed175527c5991638c65a5367c9cc6afdacced31b9a37ff3e2bfd1d ; lecteur `verif_duel_simule.py` —
  259548f52bf6d82883dd518893c160da64d8613908394048d153929d242b2f6d ; `resultat-verif-duel-simule.json` —
  6dd575c9a1371cebf595b5fed42f7d37ca832bc4e22070894a92c8e916e96089 (dossier complet gardé, 21 Mo).
- Essais du dépôt : `sortie-unittest-202.txt` — 4c38b0952c8e90f4aff4415bdabe2c9187d33020735ce901b505d05450ade67c.

## Empreintes des fichiers lus (copie de 18:00 UTC, identiques à `EMPREINTES-orchestrateur-pole-v7-v9.txt`, a44d70b31be28989cb426b15dd616c4f559e5903935b011869760969ed01fe09)
- `pole/cycle.py` a150eb00d5578a8bc4b558bda250d0f592a0a95079aa3fda179ffe9062c8c936 ; `pole/nul_filles_v2.py`
  0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910 ; `pole/selection_pari.py`
  9ff9d80f2b023401028d42d43211b9b7645c44ef6bfe0bacdc9847c5c63567d3 ; `pole/monde_banque.py`
  07df30822394e1e12223b3481e959460fa84babcb1f07a4bc40cc82d26150903 ; `pole/pole.py`
  069224ac237c4f693e87a75858b0636bcfb579ba0b4dc3382b0fc37bdd53756e ; `pole/memoire.py`
  02ec39b9b736fc806682f47a54feb89ebe67868a178019581d27df6e6b2a71c4 ; `pole/proposeur.py`
  a77018584ec5d20c25224fc675c412c4606ba3a6ce8dfde6e469a651a425a2ea ; `pole/proposeurs_references.py`
  d43480bc5f68dff9b6b95097ad71800ededf1477f07b1c457b4b5235dd7ea5c3 ; `pole/adaptateurs.py`
  a767967c1184fb94a2907f6cbe7f2bfd1602d4b50de4641abf60097fafa2aea6 ; `pole/garde_outils.py`
  e0df9743d80f6b01fbff91961419c94d570dc21683e4f7bf543c2d84713e4d3c ; `pole/outils.py`
  966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444 ; `pole/relais.py`
  b5a76343e458cf8fb91ee1928244f9cb65d50c27ab9b1bae91c21a5c82349da3 ; `pole/relais_reel.py`
  6582b786171de18393088b894f21dac66043eaf6741e4e9892697539b5320830 ; `pole/simulation.py`
  be14d44e7a8ebf6b2a71f16b5290555f5d7a11309e5dbf309ce9097f19ae7892 ; `pole/fiche.py`
  7c230afed4014e43f131c6c5d4846010df210b6e321f877a47b0150a28d21d0b ; `pole/recombinaison.py`
  71faad38644c77ae2cc21f23bfb1011c48fe674a08e542983819425ee47bd3d0.
- `essais/test_v7_nul_archive.py` 1b023eae4e3d70543c9186d7383d8c273f9cdebd0e269047e2c846dbffcb3dee ; `essais/test_v7_banc.py`
  e407e0939b12ac65ff45622ceb56d1b55cdfbd86bcfa08e91a3dec142fd2d7f2 ; `essais/test_v7_plomberie.py`
  8bfdb799fd6248725bf9eb2e1df948fe19e6b420671e05b7b06ba8f3e796d29a ; `essais/test_v7_pari_fraction.py`
  9ab76f540ba67d49f114e6e8e994e72648f389e1d54662cc8a4a4c775794ef89 ; `essais/test_v7_proposeur.py`
  88a4e947744dfaa805b4fd1d9acd48f06aa595eddd4304c50740c9e853b202d3 ; `essais/test_v7_proposeurs_references.py`
  33ee7c973127acb0e215caee47e507ad74f689f79004a3e372c816e4092226de ; `essais/faux_sdk/claude_agent_sdk.py`
  df0950fb63c5c08dbac72ae06d07be5cc50832e7b0a4d99bfb3391bff2e24131 ; `essais/faux_sdk/amont_factice.py`
  c8af8419fb31bd4705492b3f6565ffbe0725415715e35a00a436fdf85535234a ; `essais/aides.py`
  57d52b96b53cb6bfb7962ee41a29a4f73110a1448f4bd2fe192e19972933d5c8.
- `demonstrations/duel_proposeurs_v7.py` 453ce79498c3b8d8c7f9bba80d313850a2474c2d003f9c2ed4f31fa6056df3fd (ma copie, avant v10) ;
  `demonstrations/demo_proposeurs_v7.py` 8d6c4469490b428171ae7222b85cd71686dd01a76f2731c14ad0bb179224d804 ;
  `demonstrations/repetition_duel_v7.py` 2bb1f386102ead4cad34618e74f4897a0ccb569bb85d31d3117bf221595bccb2 ;
  `exemples/generer_monde_grammaire_v1.py` 3f6b316d4ad25fd567c051ce0538a0dae281ee6214e387b95d7e9b6a0bd91627.
- LISEZMOI v4 97203aa119fbcf204e10bdc34663995711c4c58cff272d5fa257dd70831f4c3a ; v5 d89a1e5d2d2eec1fad60685bb4ce835583d7c53ad8f3f42b34433dc6bb4fa461 ;
  v6 8d96bf9ff65a20fb96bb512930839e62fcc19426c15d31f21ca33cde6b175a9d ; v7 4bc261a0ad39ba489a9d2380dd55e3f9bbb74dd24e3efff4beae2ab0502fa476 ;
  v8 b493cf72c178f6cf5ddd8798c79da7264417f940081f506b4116e284ec39169c ; v9 c34d005c35064eeb0e920be5b0a9216fac8f3ca624ba9d8fbe3f7a65837d9636 ;
  `conception-v7-v1.md` 31fc8c4bc286341fcbf10181be6779ecd20ddf9de092a2c885ce8d11b27fedee.
- v10, dans la source, non contre-lus : `pole/adaptateurs.py` 4f381df96645a1ff9ec9ab7ea3de5f78f584c3005e8cc7060ab33b7e20860963 ;
  `demonstrations/duel_proposeurs_v7.py` e8b56a8a3dde494ec7f002864232ffd168bbfebc377792e4e45adec66483d6ff ;
  `essais/test_v7_duel.py` 8ff28eec07d6c932cd288eb67a26675aa491e52eab580e18035ec88bd3e8ed02 ;
  `essais/test_v7_proposeurs_references.py` 55febd2da596b9fd80e851f226c011a04bdb085d170d574cdb7e77f45a801307 ;
  `LISEZMOI-orchestrateur-pole-v7-v10.md` 1df1e7a04882f051d9e2d7d42313ab674496f63105ab5404198d752571e4c1be ;
  `EMPREINTES-orchestrateur-pole-v7-v10.txt` 69f4973c938e45a37469ed83d3f35b74a056eef7ed313cfc34b45cc7a4cc593d.

Heure de fin (`date -u`) : voir la dernière ligne.

Heure de fin lue sur `date -u` : Tue Oct 27 18:42:07 UTC 2026

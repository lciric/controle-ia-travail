# Relecture « données et fuites » de la chaîne de lancement de P4-instrument — v1

- Relecteur neuf : sous-agent lancé le 2026-10-20 (relecture entre 18:15 et 18:55 UTC environ). Je n'ai écrit ni le
  texte, ni le module, ni la chaîne.
- Lentille : empreintes des données de P3, du module et de la configuration (R11) ; arbre gelé égal à `7a54d43` ; aucun
  texte d'action poussé (fenêtres de 48 caractères) ; aucune activation gardée ; aucune clé affichée ; commit S limité au
  texte, à la configuration et aux sceaux ; sceaux vérifiés avant la destruction de l'instance.
- Textes : brouillon 4, `…/p4-instrument/P4-instrument-v1-brouillon4.md` (`32d821fb…`, fait foi) ; plan v2
  (`7c65e4f6…`) ; candidat 1 (`6422fb45…`), sur lequel la chaîne est réglée.
- Chaîne relue : `…/p4-instrument/chaine/`, 17 scripts, 6 journaux et les notes ; empreintes recalculées ici, toutes
  égales à celles du rendu du rédacteur.
- Module relu (lentille seulement) : `instrument_p4_v1.py` `6e0e026e…`, `lecture_p4_v1.py` `51a25e30…`,
  `mesures_conception_p4_v1.py` `483b8ac3…`, tests `9d015be4…`, `49441971…`, `f4f97029…`. Ce sont les empreintes des
  lignes « Module de P4 » du candidat 1. Celles de la tâche (`90b9ae8b…`, `5212cf4d…`) sont périmées (R11), comme le
  rédacteur l'avait vu (C4).

## Verdict

**Conforme après corrections.** Sur le fond, la lentille tient. Les empreintes des données de P3, du module et de la
configuration sont vérifiées à chaque étape. L'arbre gelé égale `7a54d43`. S n'ajoute que quatre fichiers. Le run ne
pousse ni texte ni activation. La destruction n'a lieu qu'après une récupération sans échec. Mais les contrôles de
détection ont six trous mineurs (RC-donnees-01 à 06) : des artefacts passent, ou sont arrêtés en affichant ce qu'ils
devraient taire. Aucun constat critique ni majeur. Corrections à faire avant le lancement réel ; les bancs sont à rejouer
ensuite (ils le seront de toute façon après les corrections T1 à T3 du candidat).

## Ce qui tient (vérifié ici)

1. **Données de P3 (R11).** Au commit HEAD du dépôt de travail (`43cd3ac`), les 10 fichiers de la table « Données lues »
   ont l'empreinte écrite et un sceau exact. Empreintes seulement : aucun contenu affiché. Le bloc 3 des contrôles,
   extrait tel quel et rejoué en lecture seule sur le dépôt réel : sain, OK ; une empreinte de la table changée d'un
   signe, KO ; un chemin vers un fichier absent, KO (`journaux/donnees-p3-v1.log`).
2. **Configuration.** Empreinte canonique `7905a18a…`, égale à celle du candidat 1 ; ses `empreintes_sources` égalent la
   table du texte (10 sur 10).
3. **Module et tokeniseur.** Six fichiers aux empreintes des lignes « Module de P4 ». Copie du tokeniseur :
   `tokenizer.json` `79e3e522…` et `tokenizer_config.json` `177c7b61…`, égales au texte.
4. **Arbre gelé.** Au HEAD courant (`43cd3ac`, R-289, poussé par une autre session pendant ma relecture), les chemins
   gelés égalent `7a54d43` (`git diff` vide). Gardé aux contrôles (bloc 2), au scellement et au run
   (`exiger_instrument_fige`, `exiger_code_cite`).
5. **Commit S.** Le bloc 1 des contrôles, extrait tel quel, rejoué sur trois commits jetables : S sain, OK ; S plus un
   fichier de textes, KO ; S qui modifie la configuration, deux KO (`journaux/contenu-s-v1.log`). Le scellement
   n'ajoute que les quatre fichiers et le relit après le commit (l. 195).
6. **Sorties versées des mesures de conception** (`docs/notes/P4-mesures-v1/…-v1.json` et `…-v2-controle.json`) :
   aucune chaîne de 48 caractères ou plus, hors des phrases B, B′ et de l'objet. Aucune fenêtre n'y tient.
7. **Module de P4.** Aucun message de garde ne recopie un texte (tâche et pas seulement). Code gelé lu : aucun `print`,
   `assert` ni message qui recopie un texte d'action. Les textes restent en mémoire ; le run n'écrit que des nombres et
   des identifiants.
8. **Run jouet** par l'amorce et le script de l'instance versés (seule la suite des tests est remplacée par un
   bouchon) : la branche porte exactement 19 fichiers (manifeste, identité, résumé, trois tableaux, leurs sceaux, sept
   traces) ; `run.err` ne porte que 8 lignes « PROGRES » ; la plus longue chaîne des résultats fait 71 caractères (une
   phrase de persona) ; la colonne `groupe` de la validation porte « fait-k ».
9. **Récupération** (copie à neuf lignes changées, comme la forme « ordinaire » du rédacteur) : les cas sains a (code 0)
   et b (traces seules, code 4) finissent par la destruction factice. Neuf témoins arrêtent sans destruction : fenêtre
   brute dans `run.err` ; sceau faux de `validation-p4.npz` ; `identite-p4.json` absent ; trace changée après son
   sceau ; `empreintes.sha256` absent ; fenêtre dans une chaîne d'un tableau ; motif d'arrêt qui recopie un texte ; et,
   sur le chemin des traces seules, trace changée et jeton factice (`journaux/recuperations-v1.log`, `-v2.log`).
10. **Jetons et arrêts.** Le lanceur, le contrôle à cinq minutes et la récupération masquent avant d'afficher, hors des
    trois affichages de RC-donnees-03 et 04. Aucun arrêt par motif de commande (R10) : un seul `kill`, par PID
    (`p4_instance_v1.sh` l. 170).
11. **Textes courts.** Les 600 actions honnêtes de P3 ont de 108 à 400 jetons notés (médiane 212 ; `scores-p3.npz`,
    colonne `jetons_notes`) : aucune n'échappe à la borne des 64 caractères (T17 sans effet sur P4).

## Constats

### RC-donnees-01 — mineur — recherche des fenêtres trop étroite

- **Où** : `recuperation_p4_v1.sh` l. 275-277 (une seule fenêtre par texte, celle du milieu) et l. 300-317 (octets bruts
  pour tout fichier qui n'est ni un résultat JSON ni un tableau).
- **Cas** : j, le texte dont la fenêtre du milieu chevauche un saut de ligne, recopié échappé (`json.dumps`) dans
  `run.err` : code 0, « TOUS CONFORMES », destruction. k, tout le texte sauf ses 48 caractères du milieu (début et fin),
  dans `run.err` : code 0, destruction. Témoin c (le même texte recopié brut) : KO 4f.
- **Portée** : chaque texte honnête de P3 compte des centaines de caractères ; 48 seulement sont cherchés. Une trace de
  pile qui recopierait un texte sous sa forme Python ou JSON, ou une partie de texte, passerait. Probabilité faible
  (point 7), mais c'est le seul contrôle de la règle.
- **Correction** : fenêtres glissantes de 48 caractères à pas de 24 sur chaque texte (toute fuite d'au moins
  71 caractères en contient une entière), cherchées dans le texte brut, dans les chaînes JSON décodées et dans la forme
  déséchappée de chaque fichier texte (`\n`, `\t`, `\"`, `\'`, `\\`, `\uXXXX`). Prototype :
  `outils/prototype_fenetres_v1.py` ; 0 fenêtre sur les branches saines a et b ; il retrouve c, i, j, k et l
  (`journaux/prototype-fenetres-v1.log`). Coût estimé sur P4 : quelques dizaines de milliers de fenêtres, de l'ordre
  d'une seconde par mégaoctet cherché. Ajouter les cas j et k aux artefacts de la répétition.

### RC-donnees-02 — mineur — chemin des traces seules sans recherche des fenêtres

- **Où** : `recuperation_p4_v1.sh` l. 100 (les contrôles 2b à 4f sont sous `if [ "$SANS_RUN" = non ]`) et l. 437
  (code 4 après la destruction).
- **Cas** : l, branche b (arrêt avant le run, traces seules) dont le journal recopie un texte : « RÉCUPÉRATION DES
  TRACES SEULES (AUCUN RUN) : TOUS CONFORMES », code 4, destruction demandée.
- **Portée** : le module ne charge aucun texte avant d'écrire son manifeste ; une branche sans run ne devrait donc pas en
  porter. Mais le code 4 dit « conformes » sans avoir cherché (R5 : aucun repli silencieux). Hérité de P3, qui ne
  détruisait pas l'instance au code 4.
- **Correction** : jouer la recherche des fenêtres et la borne des chaînes sur les fichiers ajoutés, aussi sans run (le
  fichier des textes est à S dans tous les cas) ; cas l au banc.

### RC-donnees-03 — mineur — contenu poussé affiché brut par la récupération

- **Où** : `recuperation_p4_v1.sh` l. 198 (`arrêt : {etape, motif}`, 200 caractères, affiché avant la recherche 4f) et
  l. 331 (dernière ligne du journal de l'instance, 160 caractères, chemin des traces seules). Ni jeton masqué, ni
  fenêtre retirée.
- **Cas** : i, motif d'arrêt qui recopie un texte : KO 4f, aucune destruction, mais la sortie affiche une fenêtre du
  texte (synthétique). p, jeton factice sur la dernière ligne du journal (traces seules) : KO 7, aucune destruction, mais
  la sortie affiche le jeton entier (« dernière : fuite <jeton> »).
- **Portée** : la sortie de la récupération de P3 a été versée au dépôt
  (`traces/p3-v1-20261019-2159-session/p3-recuperation-v1.sortie.txt`, commit `763997b`). L'en-tête du script promet :
  « aucune valeur de jeton, aucun texte d'action de P3 n'est affiché ».
- **Correction** : n'afficher que des motifs fixes et des comptes (étape, longueur du motif, nombre de lignes) ; à
  défaut, masquer les jetons (fonction `masquer` de la surveillance) et retirer les fenêtres avant tout affichage. Cas i
  et p au banc, avec la recherche du texte et du jeton dans la sortie.

### RC-donnees-04 — mineur — jeton tronqué, non masqué, dans la surveillance

- **Où** : `surveiller_p4_v1.sh` l. 50-59 (`print("illisible:", t[:120]…)`) et l. 64 (`etat | masquer` : le masquage
  vient après la troncature ; une valeur coupée n'est plus reconnue).
- **Cas** : faux outil dont l'état est un avertissement suivi du JSON, le jeton factice commençant au 98e caractère :
  `etats.txt` porte « illisible: … "GH_TOKEN", "factice-gh-relecture-00 » (23 des 25 caractères, en clair). Même entrée
  au contrôle à cinq minutes (l. 74 : masquage, puis troncature) : « *** » (`surveillance/`).
- **Portée** : hérité de P3 (seuls le commentaire et le plafond changent). La surveillance réelle de P3 n'a relevé aucun
  état illisible (0 sur 106), et ses `etats.txt` ont été versés.
- **Correction** : `vastai show instance "$ID" --raw 2>&1 | masquer | python3 …` (masquer, puis tronquer), ou n'écrire
  que « illisible (N caractères) » ; cas « état illisible portant un jeton à cheval sur la borne » au banc.

### RC-donnees-05 — mineur — schéma des tableaux non fermé

- **Où** : `recuperation_p4_v1.sh` l. 257-265 (validation : effectifs et forme relative seulement) et l. 246-256
  (scores par jeton : rang et début contrôlés, longueurs non).
- **Cas** : m, `validation-p4.npz` à 4 096 colonnes nommées « dim-0000 » à « dim-4095 » (forme d'activations),
  rattachée au résumé : code 0, destruction. n, scores par jeton aux longueurs doublées, sans rapport avec
  `jetons_notes` : code 0, destruction. `scores-p4.npz`, lui, est borné (424 colonnes, l. 236).
- **Correction** : `noms_sondes` de la validation égaux à ceux de `scores-p4.npz` (424, même ordre) ; types fermés
  (scores en flottants, `y` en entiers, chaînes de 80 caractères au plus) ; `longueur[k] == jetons_notes[rang[k]]` ;
  cas m et n au banc. « Aucune activation gardée » est alors vérifiée sur les trois tableaux.

### RC-donnees-06 — mineur — traces de la session versées sans contrôle

- **Où** : aucun script ne couvre les fichiers que la session verse : lancement (`lancement.txt`, `controles.txt`,
  `clone-controles.suite.txt`), surveillance (`journal-dernier.txt`, `etats.txt`, `progres.txt`), contrôle à cinq
  minutes (`journal-5min.txt`, `etat.txt`), sortie de la récupération. L'amorce imprime dans le journal du conteneur les
  dernières lignes de `journal.txt`, `tests.txt`, `tests.err` et `run.err` (`amorce_instance_p4_v1.sh` l. 58-61), que la
  surveillance recopie.
- **Cas** : P3 a versé 25 fichiers de traces de session (commit `763997b`) ; son `journal-dernier.txt` (surveillance b)
  contient les trois blocs « ----- /root/p3/… » de l'amorce, dont `run.err`.
- **Correction** : un contrôle de la chaîne, joué sur le dossier des traces de la session avant leur versement
  (fenêtres glissantes de RC-donnees-01 et jetons) ; à inscrire dans l'ordre de la chaîne, après la récupération.

### RC-donnees-07 — information — détection après la poussée seulement

- **Où** : `p4_instance_v1.sh` l. 153 (`git add -A runs diag` sur un arrêt), l. 128-138 (traces), l. 259-265 ;
  `amorce_instance_p4_v1.sh` l. 54.
- **Cas** : tous les artefacts ci-dessus sont vus après la poussée ; une fuite serait déjà dans l'historique de la
  branche du dépôt privé.
- **Correction** (version suivante) : sur l'instance, avant chaque commit, refuser tout chemin hors de la liste permise
  de la récupération (l. 79), et jouer la recherche des fenêtres (le fichier des textes est sur l'instance) et des
  jetons.

### RC-donnees-08 — information — liste des chemins gelés lue dans l'arbre contrôlé

- **Où** : `controles_avant_depense_p4_v1.sh` l. 98-107 ; `sceller_p4_v1.sh` l. 116-122 ; module
  `instrument_p4_v1.py` l. 405-413 (importe `CHEMINS_GELES` du code contrôlé).
- **Cas** : `outils/arbre_gele_v1b.sh`, liste qui s'exclut elle-même et exclut `src/controle_ia/sondes`, un fichier de ce
  dossier changé : bloc 2 des contrôles OK, garde du module acceptée ; même comparaison avec la liste lue dans
  `7a54d43` : KO. Une modification simple, sans auto-exclusion, est vue partout (`outils/arbre_gele_v1.sh`), car le
  fichier de la liste est lui-même gelé. Seule une modification délibérée passe.
- **Correction** : lire la liste dans `7a54d43` (`git show 7a54d43:src/controle_ia/harnais/validation_reelle.py`) aux
  contrôles et au scellement ; constante dans le module de P4, gelé par son empreinte.

### RC-donnees-09 — information — copie du tokeniseur non versée

- **Où** : `controles_avant_depense_p4_v1.sh` l. 51 (`TOKENISEUR=…/p4-instrument/tokeniseur`) ; texte, Métrique,
  « Phrases » (« versée avec MC-1 »).
- **Cas** : le dépôt de travail ne suit aucun fichier de tokeniseur. Les mesures de conception vérifient l'empreinte de
  la copie du bloc-notes : arrêt net si elle manque ou diffère.
- **Correction** : verser la copie et ses sceaux au commit des préalables et y pointer `TOKENISEUR`, ou corriger le
  texte.

### RC-donnees-10 — information — candidat 1 : ce qui est poussé n'est pas gelé par le texte

- **Où** : candidat 1 (`6422fb45…`) : l. 25 (commit du code sans 40 signes), l. 51 (« Tests attendus : 1 102 »), lignes
  absentes (empreintes de l'amorce et du script de l'instance, ligne « Lancement », rapports cités).
- **Cas** : relu ; la chaîne refuse (scellement en code 2, contrôles en KO, lanceur l. 142-145).
- **Portée dans ma lentille** : sans les empreintes des deux scripts de l'instance, rien de scellé ne fixe ce que
  l'instance pousse (ils sont hors de l'arbre gelé).
- **Correction** : celles du rédacteur (C1 à C3, T1 à T3).

## Artefacts fabriqués et résultats

| cas | base | artefact | attendu | obtenu |
|---|---|---|---|---|
| a | run complet | aucun (sain) | code 0, destruction | code 0, destruction |
| b | traces seules | aucun (sain) | code 4, destruction | code 4, destruction |
| c | a | fenêtre brute dans `run.err` | KO 4f | KO 4f, aucune destruction |
| d | a | sceau faux de `validation-p4.npz` | KO 2b | KO 2b, aucune destruction |
| e | a | `identite-p4.json` absent | KO 4c | KO 4c, aucune destruction |
| f | a | trace changée après son sceau | KO 2c | KO 2c, aucune destruction |
| g | a | `empreintes.sha256` des traces absent | KO 2c | KO 2c, aucune destruction |
| h | a | fenêtre dans une chaîne d'un tableau | KO 4f | KO 4f, aucune destruction |
| i | a | motif d'arrêt qui recopie un texte | KO 4f, rien d'affiché | KO 4f, texte affiché (RC-03) |
| j | a | fenêtre échappée dans `run.err` | KO 4f | code 0, destruction (RC-01) |
| k | a | texte sauf sa fenêtre du milieu | KO 4f | code 0, destruction (RC-01) |
| l | b | texte recopié dans le journal | KO | code 4, destruction (RC-02) |
| m | a | validation à 4 096 colonnes | KO 4d | code 0, destruction (RC-05) |
| n | a | longueurs par jeton doublées | KO 4d | code 0, destruction (RC-05) |
| o | b | trace changée après son sceau | KO 2c | KO 2c, aucune destruction |
| p | b | jeton factice dans le journal | KO 7, rien d'affiché | KO 7, jeton affiché (RC-03) |
| surveillance | — | état illisible, jeton à cheval sur 120 | masqué | 23 caractères en clair (RC-04) |
| cinq minutes | — | même entrée | masqué | « *** » |
| arbre gelé | S jouet | liste modifiée (simple) | KO | KO (contrôles et module) |
| arbre gelé b | S jouet | liste qui s'exclut elle-même | KO | OK aux contrôles et au module ; KO avec la liste de `7a54d43` (RC-08) |
| contenu de S | S jouet | cinquième fichier ; modification | KO | KO |
| données de P3 | dépôt réel | empreinte fausse ; fichier absent | KO | KO |

## Points du texte (ma lecture)

- « Aucun texte écrit » et « aucun texte d'action poussé » : le texte ne fixe pas le contrôle ; la chaîne reprend la
  fenêtre de 48 caractères de P3. À préciser : fenêtres glissantes, fichiers de la session compris.
- « Aucune activation gardée » : aucune forme de contrôle n'est écrite ; la récupération borne `scores-p4.npz`, pas les
  deux autres tableaux.
- « Destruction … après la récupération vérifiée » : sur le chemin des traces seules (code 4), la chaîne détruit sans
  recherche des fenêtres ; le texte se tait sur ce chemin.
- Traces de la session : le texte ne dit pas si elles sont versées ; P3 l'a fait (25 fichiers).
- Tokeniseur « versé avec MC-1 » : non versé ; les contrôles lisent la copie du bloc-notes.
- Candidat 1 : T1 à T3 du rédacteur confirmés ; sans eux, les scripts de l'instance ne sont pas gelés par S.

## Méthode et transparence

- Dépôt de travail lu seulement : `git log`, `show`, `diff`, `ls-files`, `cat-file`, `rev-parse`, avec
  `--no-optional-locks` ou `GIT_OPTIONAL_LOCKS=0`, et `git clone --shared` vers mon dossier. Vérifié sur un dépôt
  d'essai : un clone partagé ne touche pas l'index de la source. L'index du dépôt de travail est daté de 18:31:00 : un
  autre processus (R-289 committé à 18:28:05 par une autre session ; suites de tests d'un autre chantier en cours,
  `-p garde_r1_v2b`). Aucun fichier ni `__pycache__` écrit par moi dans le dépôt de travail.
- HEAD du dépôt de travail : `3448971` au début, `43cd3ac` (R-289) pendant la relecture ; arbre gelé égal à `7a54d43`
  dans les deux cas.
- Aucune commande Vast.ai réelle : deux faux outils dans un PATH de banc. Aucun réseau. Aucun service payant. Jetons
  factices seulement (« factice-…-relecture-0001 »).
- Aucun texte de P3 lu : ni `prereg/P3-consignes-v1.md`, ni le contenu d'un fichier `textes-actions-*`. Seule
  l'empreinte de `textes-actions-p3.jsonl` a été calculée, et son sceau comparé sans être affiché (R11). Toutes les
  fenêtres viennent des textes synthétiques du monde jouet. De `scores-p3.npz`, seules les colonnes `condition`, `jetons`
  et `jetons_notes` ont été lues (comptes).
- Python de la session, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `TMPDIR` et `HOME` dans mon dossier ; aucun `__pycache__`
  écrit (vérifié).
- Monde jouet : arbre réduit au code gelé (src, tests, scripts, .claude, dépendances) et aux invites lues par le run ;
  aucun fichier de `prereg/`, `donnees/`, `diag/`, `runs/` du dépôt de travail n'y est extrait ; module et chaîne versés ;
  monde jouet, textes synthétiques, candidat d'essai et texte jouet par les outils du rédacteur
  (`outils_essais_p4_v1.py`, `3b722ebb…`). C jouet `4945e294…`, S jouet `c419dbd7…`. La suite des tests est remplacée
  par un bouchon (elle a tourné en entier dans la répétition du rédacteur).
- Limites : bancs du rédacteur et répétition finale non rejoués ; gardes du GO et de l'accord hors de ma lentille ; la
  correction de RC-donnees-01 n'est qu'un prototype, éprouvé sur le monde jouet.

## Fichiers produits (sous `…/p4-instrument/relecture-chaine-donnees/`)

- Ce rapport et son sceau `relecture-chaine-donnees-v1.md.sha256` ; `empreintes-relecture-v1.sha256` (journaux, outils,
  sorties des récupérations).
- `journaux/` : `construire-monde-v1.log` (premier essai, échoué : dossier `prereg/` absent), `construire-monde-v2.log`,
  `passages-v1.log`, `recuperations-v1.log`, `recuperations-v2.log`, `arbre-gele-v1.log`, `arbre-gele-v1b.log`,
  `contenu-s-v1.log`, `donnees-p3-v1.log`, `prototype-fenetres-v1.log`.
- `outils/` : `construire_monde_v1.sh`, `construire_monde_v2.sh`, `passages_v1.sh`, `recuperations_v1.sh`,
  `recuperations_v2.sh`, `artefacts_relecture_v1.py`, `artefacts_relecture_v2.py`, `arbre_gele_v1.sh`,
  `arbre_gele_v1b.sh`, `contenu_s_v1.sh`, `donnees_p3_v1.sh`, `prototype_fenetres_v1.py`, faux outils
  (`bin-vastai/vastai`, `bin-vastai-surveillance/vastai`), environnement factice (`venv-faux/`).
- `jouet-b/` (dépôt jouet, dépôt distant local, branches a à p), `recuperations/`, `recuperations-2/` (copies jouées et
  sorties de la récupération), `surveillance/` (sorties de la surveillance et du contrôle à cinq minutes).

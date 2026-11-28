# Vérification « données et fuites » de la chaîne v2 de P4-instrument — v1

- Vérificateur neuf : sous-agent lancé le 2026-10-20 (vérification entre 22:25 et 23:05 UTC environ). Je n'ai écrit ni la
  chaîne v1, ni la chaîne v2, ni aucune relecture, ni le module.
- Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument`.
- Lentille : les constats RC-donnees de la relecture `…/relecture-chaine-donnees/relecture-chaine-donnees-v1.md` et les
  décisions de la session sur eux. Fenêtres glissantes brutes et échappées ; chemin des traces seules ; masquage avant
  troncature ; schéma fermé ; contrôle des traces de la session ; chemins gelés lus dans `7a54d43` ; tokeniseur.
- Pièces relues : `…/chaine-v2/` (21 scripts, 8 journaux, `NOTES-CHAINE-v2.md`, `RAPPORT-CORRECTION-v1.md`
  `aa671cf4…`, `paires-candidat2-chaine-v2-v1.json` `2f5a591b…`). Tous les sceaux compagnons de `…/chaine-v2/` vérifiés
  ici : conformes. `…/chaine/` (v1) intacte (sceaux conformes). Candidat 1 `6422fb45…` (passages du tokeniseur).
  Module (lecture seule) : `instrument_p4_v1.py` de `module/`, `module-v2/`, `module-v3/` (import de `CHEMINS_GELES`).

## Verdict

**Conforme après corrections.** Les sept constats RC-donnees à corriger le sont, chacun avec son cas, et les deux
d'information sont traités comme décidé. Mes bancs le confirment : 36 cas « garde » ou « sain » sur 37 conformes. Le
seul écart est un chemin de repli de l'affichage de la récupération, qui montre un motif d'arrêt sans chercher les
fenêtres (VC2-donnees-01, mineur). Le contrôle des traces ignore en silence les liens symboliques (VC2-donnees-02,
mineur). Sept points d'information, dont les limites de la recherche, à écrire au texte. Aucun constat critique ni
majeur.

## Décisions RC-donnees : ce que la chaîne v2 fait

| constat | correction relue (script, ligne) | cas du correcteur | mon épreuve | état |
|---|---|---|---|---|
| RC-donnees-01 | `verifications_p4_v1.py` l. 341-383 (`Fenetres` : toutes les fenêtres de 48, au pas de 16, et la dernière ; formes brute, JSON avec et sans `\uXXXX`, Python ; forme brute et déséchappée de chaque texte) ; l. 398-428 (octets, chaînes JSON, chaînes des tableaux) | V : F00-F14 ; R : j2, k2 ; T : T01-T05 | A01-A13 : 12 gardes conformes (JSON deux fois, octets en `repr`, `\/` et ` `, clé JSON, fins de ligne CRLF, HTML, espaces normalisées, octets invalides, npz compressé, octets `S`) ; A06 (63 caractères au pire alignement) retrouvé, A20 (62) non : borne de 63 confirmée | fait |
| RC-donnees-02 | `recuperation_p4_v1.sh` l. 361-416 : 4f joué hors du `if SANS_RUN`, sur tous les fichiers ajoutés ; bornes des chaînes sur `run.json` des traces | R : l2, p2 | C11 (traces seules, jeton à cheval sur la borne puis texte) : KO 4f et KO 7, rien d'affiché | fait |
| RC-donnees-03 | l. 127-128 et 541 : toute la sortie passe par `montrer` de S (masquer, chercher, tronquer) ; motif l. 271 en JSON sur une ligne ; dernière ligne du journal l. 424 filtrée | R : i2 ; V : W00-W06 | W10-W15 conformes (fenêtre au-delà de 400 caractères, `\uXXXX`, retour chariot, octets invalides, jeton à cheval sur 400) ; C10 (motif échappé après 450 caractères) : ligne retirée, KO 4f ; **C31 : repli, motif affiché** (VC2-donnees-01) | fait, sauf le repli |
| RC-donnees-04 | `surveiller_p4_v1.sh` l. 88-98 (masquer, puis lire les champs ; illisible : longueur et empreinte) ; l. 99-106 (formes fixes) ; `controle_cinq_minutes_p4_v1.sh` l. 94-129, 153 | S : M07, M10b, C16, C26 | lecture du code ; étiquette tronquée avant masquage en trois endroits (VC2-donnees-06, information) | fait |
| RC-donnees-05 | `recuperation_p4_v1.sh` l. 289-353 : clés, types, dimensions fermés ; 424 noms, même ordre ; `longueur[q] == jetons_notes[rang[q]]` ; chaînes de 80 au plus | R : m2, n2, chaîne longue | C12 (clé de plus), C13 (scores par jeton en deux dimensions), C14 (noms permutés) : KO 4d ; C15 (80 caractères d'un texte dans `groupe`) : KO 4f | fait |
| RC-donnees-06 | `controler_traces_p4_v1.sh` neuf (57 lignes) : jetons exigés, textes à leur empreinte et sceau, fenêtres et jetons sur tout le dossier, comptes seulement | T : T00-T17 | banc du correcteur rejoué ici : 20 conformes, mêmes codes ; B00-B04 conformes ; B10-B17 limites (VC2-donnees-02, -03) | fait |
| RC-donnees-07 | rien (version suivante), noté CV2-07 | — | — | comme décidé |
| RC-donnees-08 | `controles_avant_depense_p4_v1.sh` l. 110-125 ; `sceller_p4_v1.sh` l. 118-128 ; `repetition_jouet_p4_v1.sh` l. 90-96 : `git show 7a54d43:…/validation_reelle.py` | C : G01 ; E : S42 | dépôt de travail (lecture git seule, HEAD `6a449d2`) : liste de `7a54d43` à 12 chemins, égale à celle de HEAD ; `git diff --quiet 7a54d43 HEAD -- <liste>` : code 0 | fait (VC2-donnees-09 : phrase) |
| RC-donnees-09 | `controles_avant_depense_p4_v1.sh` l. 60-62, 293-307 : `donnees/P4-tokeniseur-v1/` du clone, deux empreintes, sceaux à S, copie de travail égale ; sinon KO, mesures non rejouées | C : T01-T03 | `scripts/depot_expurge.py` (HEAD, lecture git) retire `donnees/**` de la copie publique : zone exclue confirmée ; paire « tokeniseur-metrique » trouvée une fois au candidat 1 | fait |

Les onze paires du texte (`paires-candidat2-chaine-v2-v1.json`) ont chacune leur ancre une seule fois dans le candidat 1.
Les phrases « chaine-traces », « paragraphes » et « tokeniseur-metrique » disent ce que fait le code, sauf deux points :
le repli de l'affichage (VC2-donnees-01) et « jamais dans l'arbre contrôlé » (VC2-donnees-09).

## Constats

### VC2-donnees-01 — mineur — repli de l'affichage de la récupération : motif montré sans recherche des fenêtres

- **Où** : `recuperation_p4_v1.sh` l. 126-137 (si le module commun de S ou les textes sont illisibles, `TEXTES_OK=non` et
  le filtre ne fait que masquer les jetons, puis tronquer à 400) ; affichages concernés l. 271 (motif d'arrêt) et l. 424
  (dernière ligne du journal) ; l. 541.
- **Cas** : C31 (`banc-c2-repli-v1.log`). Même branche que C30 (arrêt dont le motif recopie un texte). Copie ordinaire
  (C30) : ligne « 4a » retirée, KO 4f. Copie dont seul le chemin des textes change (absent du clone) : KO 4f annoncé
  (« jetons masqués seulement »), aucune destruction, mais la ligne « 4a arrêt » montre le texte synthétique en clair.
- **Portée** : la décision dit « ne jamais afficher un motif d'arrêt ou une ligne de journal brute » ; la phrase du texte
  aussi (« Aucun motif d'arrêt ni ligne de journal n'est affiché sans masquage des jetons puis recherche des fenêtres »).
  Le repli n'est éprouvé par aucun banc. Il est peu probable : les scripts gelés de l'instance ne peuvent pas retirer le
  fichier des textes, et S porte le module commun. Il reste atteignable si le Python de la session manque au moment de la
  récupération (bloc-notes effacé) : la dernière ligne du journal (l. 424, en bash) passe alors par le repli. Pas
  d'effet sur la destruction (KO).
- **Correction** : dans le repli, n'afficher de chaque ligne que ses 40 premiers caractères (aucune fenêtre de 48 n'y
  tient), sa longueur et son empreinte courte ; lire les textes à S (`git show "$S:$TEXTES_P3" > "$TRAV/textes-S.jsonl"`)
  et donner ce chemin au filtre et à 4f, pour que la tête de la branche n'y touche pas (VC2-donnees-07) ; ajouter à la
  répétition un artefact « repli de l'affichage » (copie dont le module commun de S est vide), avec la recherche des
  fenêtres dans la sortie.

### VC2-donnees-02 — mineur — liens symboliques ignorés en silence par la recherche des fenêtres et des jetons

- **Où** : `verifications_p4_v1.py` l. 436 (`fichiers_de` : `x.is_file() and not x.is_symlink()`) ;
  `controler_traces_p4_v1.sh` l. 44 (`find -type f` : les liens ne sont pas comptés).
- **Cas** : B10 (lien vers un fichier qui porte un texte), B11 (lien vers un jeton), B12 (lien vers un dossier) : code 0,
  « versement permis », « 3 fichiers » ; A38, A39, J13 : « fichiers parcourus : 0 ».
- **Portée** : aucun script de la chaîne ne crée de lien. Versé par `git add`, un lien ne porte que son chemin cible ;
  copié avec `cp -L` ou `rsync -L`, il porterait le contenu non cherché. Le compte écrit cache le lien : repli
  silencieux (R5).
- **Correction** : compter les entrées qui ne sont pas des fichiers ordinaires (liens, autres) et refuser (code 1, chemin
  écrit) ; cas de banc « lien symbolique dans les traces ».

### VC2-donnees-03 — information — fichiers non textuels lus avec remplacement

- **Où** : `verifications_p4_v1.py` l. 398-428 : tout fichier autre que `.npz` est décodé en UTF-8 avec remplacement ;
  dans un `.npz`, seuls les tableaux de chaînes (`U`, `S`) sont lus (l. 410-413).
- **Cas** : non retrouvés : texte en UTF-16 (A31, B14), compressé (A32, B15), dans un `.npy` (A33, B13), dans un tableau
  structuré d'un `.npz` (A34), en octets après l'archive `.npz` (A35). La récupération refuse déjà ces fichiers par ses
  chemins permis (1c) et son schéma fermé (4d) ; le contrôle des traces non.
- **Correction** (proposée) : fichier non `.npz` qui n'est pas de l'UTF-8 valide, ou tableau d'un autre genre que
  nombres et chaînes : « illisible » (refus) ; chercher aussi les octets bruts d'un `.npz`.

### VC2-donnees-04 — information — limites de la recherche des fenêtres, à écrire au texte

- **Cas** (banc A, documentés, sans verdict) : non retrouvés : fragment de 62 caractères au pire alignement (A20),
  morceaux de 40 (A21), JSON échappé trois fois (A03), base64 (A23, et base64 courte d'un fragment de 60, A24),
  hexadécimal (A25), URL (A26), majuscules (A29), espaces de largeur nulle (A30), texte dans un nom de fichier (A36,
  B17), jetons du tokeniseur (A37) ; partiellement retrouvés selon le texte : NFD (A27), NFKC (A28), repli à 60 colonnes
  (A22). Filtre : un texte à lignes toutes courtes passe ligne à ligne (W20). Jetons : coupé sur deux lignes, en base64,
  en UTF-16, non retrouvés (J10-J12, W21, W22).
- **Portée** : conforme à la décision (fenêtres de 48, pas de 16, une forme échappée) ; le texte ne dit pas ce qui
  échappe. Coût faible pour réduire l'écart : déséchapper jusqu'à point fixe (quatre passes au plus), normaliser en NFC
  et NFKC des deux côtés, chercher aussi les chemins des fichiers.
- **Correction** : phrase du texte (section « Texte à ajouter »).

### VC2-donnees-05 — information — seul le différentiel net S..tête est cherché

- **Où** : `recuperation_p4_v1.sh` l. 148 et 375 (fichiers de `git diff --name-status S HB`).
- **Cas** : C21 : un texte poussé dans un commit, retiré au suivant : récupération en code 0, destruction ; la recherche
  sur l'historique de la branche retrouve la fenêtre (`banc-c-recuperation-v1.log`).
- **Portée** : les scripts gelés de l'instance écrivent chaque fichier une fois (un dossier de traces neuf par appel) ;
  la copie publique est un seul commit. L'historique reste dans le dépôt privé.
- **Correction** (proposée, avec RC-donnees-07) : chercher chaque objet ajouté de `git rev-list --objects S..HB`.

### VC2-donnees-06 — information — étiquette tronquée avant masquage

- **Où** : `surveiller_p4_v1.sh` l. 75 et `arreter_p4_v1.sh` l. 53 (`cut -c1-40`, sans masquage) ;
  `recuperation_p4_v1.sh` l. 510 (`[:40]`, puis masquage par le filtre, après la troncature).
- **Portée** : la lettre de RC-donnees-04 est « masquer avant de tronquer partout ». L'étiquette vient du lanceur ;
  une étiquette autre est celle d'une autre instance. Risque négligeable.
- **Correction** : passer l'étiquette par `masquer` avant `cut`, ou n'en écrire que la longueur et l'empreinte courte.

### VC2-donnees-07 — information — textes des fenêtres lus à la tête de la branche

- **Où** : `recuperation_p4_v1.sh` l. 123, 127-128, 363 : `$TEXTES_P3` est lu dans le clone placé sur HB, pas à S.
- **Portée** : une branche qui changerait ce fichier est refusée par 1b et 1c ; mais le filtre et 4f se feraient alors
  sur le fichier changé. Les scripts gelés de l'instance ne peuvent pas le changer.
- **Correction** : lire les textes à S (voir VC2-donnees-01).

### VC2-donnees-08 — information — fausses alertes possibles, nombre de textes non exigé

- **Où** : `verifications_p4_v1.py` l. 359 (seules les fenêtres d'un seul caractère répété sont ignorées) ;
  l. 323-338 (nombre de textes honnêtes écrit, non comparé à 600).
- **Portée** : une fenêtre pauvre d'un texte réel (tirets alternés, blancs et retour à la ligne) retrouvée dans une
  trace saine bloque le versement ou garde l'instance (24 heures de disque au plus) : sûr, mais coûteux. Je n'ai lu
  aucun texte de P3 : non mesuré.
- **Correction** (proposée) : épreuve à blanc par la session avant le lancement, comptes seulement :
  `verifications_p4_v1.py fenetres <textes de P3> traces/p3-v1-20261019-2159-session/` (traces saines déjà versées) ;
  exiger 600 textes honnêtes lus ; ignorer les fenêtres de moins de huit caractères distincts si l'épreuve le demande.

### VC2-donnees-09 — information — « jamais dans l'arbre contrôlé » : la garde du module lit l'arbre

- **Où** : phrase « paragraphes » du texte ; `instrument_p4_v1.py` (module v1 et v2 l. 66 et 406-407 ; v3 l. 71 et
  411-412) importe `CHEMINS_GELES` du code du dépôt.
- **Portée** : les contrôles et le scellement lisent la liste dans `7a54d43` ; la garde du module, au bloc 9 et sur
  l'instance, lit celle de S, égale à celle de `7a54d43` par le bloc 2 (le fichier de la liste est lui-même gelé). Pas
  de trou ; la phrase dit un peu plus que le code.
- **Correction** : phrase (section « Texte à ajouter »).

## Bancs de cette vérification

| banc | script (sha256) | journal (sha256) | résultat |
|---|---|---|---|
| A : module commun (`fenetres`, `montrer`, `jetons`) | `outils/banc_a_fenetres_v1.py` `df3b197b8c38a4476b7cefca693f8c66b08ca62bbaa5bc1edb46e5bae3c71675` | `banc-a-fenetres-v1.log` `614153a2908747325ecd2303aa47afee82abe38878bf603bbce70e34070fed56` | 22 cas garde ou sain : 22 conformes ; 29 limites documentées |
| B : contrôle des traces | `outils/banc_b_traces_v1.sh` `5207d6f9c38e6ad85a428f4dc277df6b7537013ce86c3af74ccedbc9fb70a52b` | `banc-b-traces-v1.log` `68d20980e473c13d18186a15c19562d50bb35bf646b68d0ce41cf674123c6e54` | 5 conformes ; 8 limites ; aucun `__pycache__` |
| C : récupération v2 sur le monde jouet | `outils/banc_c_recuperation_v1.sh` `fae9f4f91ff2edeba668b002b7eeb0fde6dcc80654f66f6d2556fdeac18d9500` ; `outils/artefacts_verif_c_v1.py` `24fb2a6df9430ae5558f25b5bbcb6926dcfb7ae1e12ec6c3cf77d0d005a1437a` | `banc-c-recuperation-v1.log` `8ae4f936035831ddcc8b57974b83e733caa2532ddc373117a200b54ce900b6b8` | sains C00 (code 0), C01 (code 4) ; C10-C16 : 7 conformes ; C20, C21 limites |
| C2 : repli de l'affichage | `outils/banc_c2_repli_v1.sh` `4f306d6e60b5edb687efff838829368ace4e11bddbd2a8a07832dc0baaf2bddf` ; `outils/artefacts_verif_c_v2.py` `23a682130aff344ddb6c9c49fcf6e169a1a392764eeb2daf3b5528f8d13784a0` | `banc-c2-repli-v1.log` `f63472d4a3a8747f22c2e7255881644d8e24c18fad74d69ed887b39875b33a74` | C00, C30 conformes ; C31 écart (VC2-donnees-01) |
| rejeu du banc des traces du correcteur | `…/chaine-v2/essais_traces_p4_v1.sh` `12cb9a0d…` | `rejeu-banc-traces-v1.log` `fe14cf362002269f2fc42f5a86a2da23870f099d424e2988388d834169dc6d1f` | 20 conformes, mêmes cas et codes que le journal livré |

Scripts éprouvés (empreintes citées par les journaux) : `verifications_p4_v1.py` `cdb6b90a…`, `controler_traces_p4_v1.sh`
`f2fe40f2…`, `recuperation_p4_v1.sh` `65477c6d…`, `outils_essais_p4_v1.py` `9f26389b…` : égales aux fichiers de
`…/chaine-v2/`. Faux outil de location : `bin-vastai/vastai` `50fb74fb…` (copie de celui de la relecture). Premier jeu
du banc A gardé (`banc-A-1/banc-a.log`, `d52e389f…`) : A03 (JSON échappé trois fois) y était classé « garde » ;
reclassé « limite » avant le second jeu, la décision ne demandant qu'une forme échappée (la chaîne en traite deux).

## Texte à ajouter

1. Phrase « paragraphes », après « … une ligne qui porte une fenêtre n'est affichée que par sa longueur et son empreinte
   courte. » (si VC2-donnees-01 est corrigé) :
   « Si le filtre de S ne peut pas être joué, la récupération est en échec (KO 4f, aucune destruction) et chaque ligne
   n'est affichée que par ses 40 premiers caractères, sa longueur et son empreinte courte. »
2. Même phrase, à la fin du premier tiret (VC2-donnees-04) :
   « Limite : la recherche retrouve une recopie d'au moins 63 caractères d'un seul tenant (48 au mieux), brute ou
   échappée une ou deux fois ; une recopie plus courte, coupée, encodée (base64, hexadécimal), compressée, changée de
   casse ou de normalisation Unicode n'est pas cherchée. »
3. Phrase « paragraphes », troisième tiret (si VC2-donnees-02 est corrigé) :
   « Un lien symbolique ou un fichier non ordinaire dans le dossier des traces arrête le versement (code 1). »
4. Phrase « paragraphes », dernier tiret, remplacer « jamais dans l'arbre contrôlé. » par (VC2-donnees-09) :
   « jamais dans l'arbre contrôlé ; la garde du module, sur l'instance, lit celle de S, égale à celle de `7a54d43` par
   ces contrôles. »

## Méthode et transparence

- Dépôt de travail en lecture seule : `git --no-optional-locks` (`log`, `show`, `diff --quiet`, `rev-parse`, `status
  --porcelain`), `GIT_OPTIONAL_LOCKS=0`. Fichiers lus par leur nom : `scripts/depot_expurge.py` (par `git show`, en-tête
  et motifs de retrait). `git status --porcelain` vide à la fin ; aucun fichier ni `__pycache__` écrit dans le dépôt.
  HEAD a bougé pendant la vérification (`c1e7ef9`, puis `6a449d2`) : autres sessions.
- Aucun texte de P3 lu : ni `prereg/P3-consignes-v1.md`, ni le contenu d'un fichier `textes-actions-*`, ni rien sous
  `donnees/` du dépôt de travail. Fenêtres tirées des textes synthétiques de `outils_essais_p4_v1.py fenetres`, de
  quatre textes écrits ici, et de ceux du monde jouet de la relecture (`donnees/synth/textes-fenetres-p3.jsonl` du dépôt
  jouet). Les journaux C et C2 montrent des fragments de ces textes synthétiques : voulu (preuve de l'écart C31).
- Monde jouet : miroir (`git clone --no-local --mirror`) de `…/relecture-chaine-donnees/jouet-b/distant.git` dans mon
  dossier, retiré à la fin ; branches d'artefacts poussées dans ce miroir seulement (le dépôt de la relecture garde ses
  17 branches). Copie de la récupération : dix lignes changées (les neuf de la forme ordinaire de la répétition et le
  module commun, celui de la chaîne v2, comme le banc de développement du correcteur) ; C31 : une de plus (chemin des
  textes).
- Aucune commande de location réelle : faux outil dans le PATH des bancs. Aucun réseau hors lecture git locale. Jetons
  factices seulement ; aucune clé ni jeton affiché. Python de la session, `-B`, `PYTHONDONTWRITEBYTECODE=1`, `HOME` et
  `TMPDIR` dans mon dossier ; aucun `__pycache__` (vérifié dans mon dossier et dans `…/chaine-v2/`). Arrêts : aucun.
- `…/chaine/` et `…/chaine-v2/` non modifiés (sceaux conformes avant et après). Mes outils ont été ajustés en place avant
  le jeu final (classement des cas « limite », A03) : les empreintes ci-dessus sont celles des versions jouées en dernier.
- Limites : bancs du correcteur autres que celui des traces non rejoués ; répétition jouet non rejouée (lue) ; gardes
  de dépense, de révocation et de fidélité hors de ma lentille ; module lu seulement pour `CHEMINS_GELES` et le libellé
  des conditions.

## Fichiers produits (sous `…/verification-chaine-v2-donnees/`)

- Ce rapport et son sceau `verification-chaine-v2-donnees-v1.md.sha256`.
- `outils/` : `banc_a_fenetres_v1.py`, `banc_b_traces_v1.sh`, `banc_c_recuperation_v1.sh`, `banc_c2_repli_v1.sh`,
  `artefacts_verif_c_v1.py`, `artefacts_verif_c_v2.py` ; `bin-vastai/vastai` ; chacun avec son sceau.
- Journaux et sceaux : `banc-a-fenetres-v1.log`, `banc-b-traces-v1.log`, `banc-c-recuperation-v1.log`,
  `banc-c2-repli-v1.log`, `rejeu-banc-traces-v1.log`, `banc-A-1/banc-a.log`, `banc-A-2/banc-a.log`.
- Dossiers de jeu : `banc-A-1/`, `banc-A-2/`, `banc-B-1/`, `banc-C-1/`, `banc-C2-1/`, `rejeu-banc-traces-1/` (sorties de
  chaque cas, copies jouées).

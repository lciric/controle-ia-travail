# Contre-lecture du lanceur et de la conception de l'atelier d'idées sur les bassins étroits (trois générations) — v1

Contre-lecteur neuf, **Claude Fable 5.2** (`claude-fable-5-2`), sous-agent de la session mère ; l'auteur des pièces relues est
Claude Opus 5.5 ; je n'ai rien écrit de ce que je relis (R2, N-052). 13 novembre 2026, de 13:30 à 13:56 UTC (heures relevées par
`date -u`). Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-contre-lecteur-lanceur-bassins-etroits-v1.md`
(`116522bda0b408da05e6b59a7b0fac873d4b49210fc02f4094aaa240944a80d7`, vérifiée) ; interdits communs v2 (`1ee3b370…`, vérifiés)
appliqués. **Aucune dépense, aucun appel de modèle, aucun réseau, aucune opération git dans le dépôt de travail, rien corrigé.**
Aucun refus de permission ni de classifieur rencontré.

## Verdict

**Lanceur v1 (`a10420cc…`) : « non autorisable » en l'état** — un constat bloquant prouvé par exécution (B1 : avec
l'orchestrateur réel, le lanceur s'arrête sur une exception non gardée avant toute course, puis se verrouille). Rien ne serait
dépensé, mais aucune course ne partirait. Les corrections sont locales ; elles demandent un fichier neuf (R12), donc une
empreinte, une règle et une épingle neuves, et une vérification courte de la version corrigée.

**Conception, question, témoins, devis : « autorisables après corrections »** — aucun bloquant ; la génération 1 ne dépend pas
de la règle de passage ; la lecture d'N-053 doit être confirmée par écrit avant la génération 2 (M5).

Comptes : **1 bloquant, 9 majeurs, 12 mineurs.**

## Ce que j'ai lu, et comment

- Compagnons vérifiés (empreinte recalculée égale au compagnon) pour les quatorze pièces nommées : conception `4c90a3a5…`,
  question `c188fa9a…`, témoins `748f391e…`, mesure `df384741…`, devis `1b311242…`, rapport `b7b57add…`, lanceur `a10420cc…`,
  essais `8fa7ae32…`, lanceur v3 `0a704661…`, contre-lecture du v2 `4591fe97…`, vérification du v3 `c7542899…`, question du
  collisionneur `935f4e5b…`, N-053 `2204256d…`, N-065 `f820e90d…` ; plus les pièces que le lanceur épingle : faits `d19b5400…`,
  enveloppe d'Argon `37c0205e…`, commande d'Argon `46c91df4…` (lue : garde avant envoi, l. 725-860, et rendu des refus,
  l. 1026-1047).
- Lanceur v1 lu en entier (1 203 lignes), lanceur v3 lu en entier (782 lignes), essais lus en entier (662 lignes).
- Ligne GO-2026-11-13-03 par `grep -n` sur `registres/go.md` (l. 316). `.claude/settings.json` et `.claude/hooks/garde_calcul.py`
  lus, non modifiés.
- Orchestrateur (clone `/home/user/lciric/ideation-organism`, commit `be6b5af9…`, neuf empreintes recalculées égales à celles
  du lanceur ; rien n'y est écrit : `-B`, préfixe de cache hors du clone, état `git status --ignored` vide après mes outils) :
  `demonstrations/ideation_v8.py`, `v7`, `v4` en entier, `v6` et `v5` (tête et fin), `demonstrations/ideation_v2.py` en entier ;
  dans `pole/ideation_v2.py` : gabarit et validation des fiches, témoins, grille, anonymisation, agrégat, lecture des témoins,
  appel de contrôle, gardes de taille, mesures de convergence, `verifier_reglages`, `mesurer_consignes`, écritures de fin de
  course, `executer_bras_differe` en entier ; dans `pole/adaptateurs.py` : sonde du bac à sable, adaptateur de commande
  externe ; `pole/relais.py` ; dans `pole/outils.py` : scellement, `dossier_traces`, `manifeste`.
- Trois outils, écrits par moi, scellés avec leurs résultats (`contre-lecture-outils-v1/`, § « Outils ») : analyseur
  d'arguments réel et liste blanche réelle sans appel ; épreuves ciblées des gardes sur états de disque factices ; douze
  mutations avec la suite des essais rejouée. Suite d'origine rejouée : **77 passés** (13:41 UTC).

## Réponses aux sept points

### 1. Le lanceur

**Différentiel contre le v3.** Repris à l'identique (lu ligne à ligne) : `lire_plafond_go`, `verifier_interprete`, `_git`,
`caches_d_octets`, `verifier_orchestrateur`, `options_interprete`, `verifier_prefixe_pycache`, `garde_drapeaux`, `_valeurs`,
`_une`, `sommes_plafonds`, `taille_max`, `sonder_bac_a_sable`, `environnement_sans_cles`, `ecrire_scelle`, le relais des
signaux par PID. Changé : GO et périmètre (« organisme d'idéation » et « bassins », plafond lu ≥ 60) ; `verifier_pieces` refuse
en plus un lien symbolique ; pièces (question, faits, témoins, enveloppe, commande) ; `--nombre` 6 ; plafonds (contrôle externe
1,5, passe 1 d'Argon 1,3, passe 2 1,9) ; la mesure des consignes n'est plus une pièce épinglée mais rejouée par l'orchestrateur
à chaque génération ; `garde_sommes` vérifie en plus le pire cas « course externe + bras » (7,8 ≤ 8,0) ; `construire_liste_blanche`
scelle (c'est B1). Ajouté : argument fermé, runs et état des générations, dépense relevée et garde de cumul, règle de passage,
commande et garde du bras, attestation, plancher de la commande d'Argon, manifeste de refus.

**Ce qui tient** (lu, et éprouvé quand c'est dit) :
- GO : une ligne principale, 8 colonnes, type, Lazar, période, périmètre, plafond lu ≥ 60 ; la borne du cumul est
  min(60, plafond lu), une ligne d'extension ne relève rien (épreuve E6). Réserve : m1.
- Argument unique fermé : `[]`, `4`, `0`, deux arguments, drapeau, `01`, ` 1`, `un` refusés (essais) ; mutant M5 tué.
- Refus de la génération g + 1 sans course et bras réussis de g, manifestes de fin scellés, classement lisible : tenu (essais ;
  mutants M4 et M11 tués). Une course dont un témoin échoue chez le juge Opus rend 4 (`demonstrations/ideation_v2.py` l. 1501) :
  le lanceur ne la tient pas pour réussie, aucun bras n'est payé dessus.
- Pas de relance d'une **course** après dépense : tenu (mutant M3 tué), à deux réserves près (M1, M2). Pour le **bras** : non
  gardé par le lanceur (M3).
- Drapeaux interdits, sommes, gardes de taille : formules recalculées par moi contre le code de l'orchestrateur (course
  min(600 000 ; 760 000 − 360 000) = 400 000 ; passe 1 280 000 ; sommes 9,9 et 7,4) et contre l'analyseur réel (outil 1 :
  `garde_de_la_course` rend 400 000, provision 360 000).
- Clés par leur nom, environnement bâti par filtrage (noms exacts et motif), aucune valeur écrite ; fiches et journaux hors du
  dépôt ; le dépôt ne reçoit que des manifestes, la liste blanche et la mesure (tailles et empreintes, aucun texte de fiche).
- Dépense illisible comptée au plafond : tenu pour un manifeste de fin au sceau faux ou au coût mal typé (épreuve E11 :
  négatif, non numérique, booléen, absent → 20 USD ; infini → rendu tel quel, donc refus du cumul) ; non tenu dans un cas (M1).
- Génération rejouée : refusée (« déjà jouée »). Bras sans course : inatteignable (le bras ne se choisit que sur une course
  réussie).

**Mutations** (outil 3 ; la base, sans mutation, rend 77 passés) : cinq gardes principales et sept autres.

| Mutant | Garde affaiblie | Issue |
|---|---|---|
| M1 | cumul sans le plafond de ce qui va être lancé | tué (`test_cumul_artefact_depasse`) |
| M2 | manifeste de fin illisible compté 0 | tué (`test_cumul_depense_illisible_compte_le_plafond`) |
| M3 | relance d'une course après dépense | tué (`test_pas_de_relance_apres_depense`) |
| M4 | génération g + 1 admise sans le bras de g | tué (2 essais) |
| M5 | arguments en plus admis | tué (`test_argument_artefacts[argv3]`) |
| M11 | classement illisible transmis | tué |
| M6 | borne de trois tentatives de course levée | **survit** |
| M7 | borne du cumul = plafond du GO (sans le min à 60) | **survit** |
| M8 | attestation sans la consigne en attente du juge | **survit** |
| M9 | borne de trois bras levée | **survit** |
| M10 | « génération jouée » sans manifeste du bras scellé | **survit** |
| M12 | plancher du contrôle court du bras non gardé | **survit** |

Six tués sur six pour les gardes d'argent et d'enchaînement ; six survivants : ces six gardes n'ont pas d'artefact (m7).

### 2. La forme de la commande du bras

Éprouvée sans rien lancer (outil 1) : l'analyseur réel (`construire_analyseur` de `demonstrations/ideation_v2.py`) accepte les
trois commandes que le lanceur construit — course, mesure, bras — sans argument inconnu ; pour le bras, les treize contrôles
d'arguments que `principal` fait après l'analyse (l. 1005-1133), rejoués à la main sur l'espace de noms analysé, sont tous tenus.
Par lecture de `executer_bras_differe` : juges donnés égaux aux juges attendus par la course ; plafond externe relu au manifeste
de départ (8,0) ; besoin du bras 2,5 + 0,6 = 3,1 ; au pire cas de la course (4,7) : 7,8 ≤ 8,0 ; `--liste-blanche` est admise et
sans effet au bras ; le contrôle court à 0,6 remplace les 0,2 que la course a comptés (c'est permis : `budget_controle_usd` donné).
Chemin de la consigne en attente, nombre de fiches servies, fichiers lus par le lanceur : conformes aux noms réels.
Réserve : m6 (sans `--moteur claude-sdk`, deux barrières du modèle servi sont inactives ; la troisième agit). **Je n'ai pas
exécuté le bras**, même simulé : c'est l'action refusée au préparateur.

### 3. Le plancher de la commande d'Argon — constat du préparateur confirmé

Lu dans `commande_argon_v3d.py` (l. 818-853) : refus sans envoi (code 4) si le plafond ne paie pas l'entrée gardée
(⌈max(⌈caractères / 4⌉, compte exact) × 1,05⌉ × 8,3 par million) plus 4 096 + 8 192 jetons à 41,5 par million. Calcul (épreuve
E9) : contrôle court (41 caractères) **0,510052 USD** ; le défaut de l'orchestrateur (0,2) ne passe pas, les 0,6 du v1 passent.
**Lanceur v3** : contrôle externe réglé à 1,25 pour 415 253 caractères, plancher **1,414693** : refusé sans envoi ; son contrôle
du bras (défaut 0,2) aussi. Le v3 ne peut donc pas jouer une course tel qu'il est (arrêt au contrôle d'Argon, coût plancher
10⁻⁶, rien de facturé). v1 : contrôle externe 1,213244 (à 4 caractères par jeton) et 1,447669 (à 3) sous 1,5 ; passe 1
0,633 sous 1,3 ; passe 2 0,738 sous 1,9 ; juge à la garde de 600 000 caractères 1,817 sous 2,5. Fragilité : M2.

### 4. La conception

- **Règle de passage** : écrite d'avance (conception scellée avant toute course) et **déterministe** (rang de l'orchestrateur,
  départage par empreinte ; ensembles triés ; ordre servi par empreinte). **Aucune note, aucun rang, aucun auteur, aucune passe
  dans la pièce** : vérifié par lecture de `vue_servie` et de la pièce écrite. Mais le **fait de la sélection** est servi (M5),
  le texte et le code divergent sur l'appariement des passes (M4), et les étiquettes ont une allure ordinale (m5).
- **N-053 et N-065** : voir M5. La lecture du préparateur tient par les mots du GO, pas par son argument.
- **Même lignée** : voir « Ce que la même lignée interdit de conclure », plus bas.
- **Témoins** : voir M9.
- **Attestation** : *quoi* — `{lecteur, lu_le, fiches_validees_sha256, consignes_en_attente_sha256: {"argon-juge": …}}`, scellée ;
  *où* — `docs/notes/organisme-bassins-etroits-v1/attestations/attestation-lecture-humaine-g<g>-v1.json` ; le lanceur vérifie le
  sceau, les quatre champs, l'empreinte des fiches validées et la présence de la clé `argon-juge` ; l'orchestrateur vérifie
  l'empreinte de la consigne. *Qui* — non tranché : M6.

### 5. La question et les témoins

- **Fidélité** (épreuve E10, par programme, espaces normalisés) : le cœur (1 833 caractères) et les contraintes (1 016
  caractères, à la majuscule initiale près) de la question du collisionneur sont dans la question de l'organisme, mot pour mot.
- **Rien qui souffle une réponse** dans la question ; les témoins ne sont servis qu'aux juges. Nuances : m12.
- **Aucun secret** : ni graine, ni loi plantée, ni paramètre de monde dans la question ni dans les témoins (« graine » et « loi
  plantée » n'y figurent que dans la liste des contraintes). La pièce des faits décrit la *forme* de la composante conditionnelle
  du monde (signe dépendant d'un autre trait, chaîne de profondeur 2) : structure, pas paramètre ; déjà servie au collisionneur.
- **Le recoupement n'existe pas encore** : rien à relire (M8).

### 6. Le devis

Arithmétique juste : Claude 0,4 + 4,0 + 4,0 + 1,5 = 9,9 ; hors Claude 1,5 + 1,3 + 1,9 + 2,5 + 0,6 = 7,8 ; génération 17,7 ;
trois générations 53,1 ; borne 60. Plafonds identiques à ceux du lanceur. Attendus recalculés aux barèmes du devis : 2,08 et
3,40, soit 5,5 par génération. Non vérifié : le barème Claude (4 / 20, 10 / 50) et les coûts du 8 novembre (registre hors de mes
lectures). Réserves : m10 (Fable sans précédent, juge) et M7 (durée).

### 7. La règle de permission et l'épingle proposées

- Les trois règles `Bash(/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_bassins_etroits_v1.py N)`, N = 1, 2, 3,
  sont exactes, sans motif : la plus petite forme qui exprime un argument fermé. C'est **trois** commandes et non « la seule
  commande » du mot de Lazar ; à lui dire quand il écrit la règle. Les trois refus `Edit(//…)` ont la forme validée pour le v3.
- **L'épingle n'est pas écrite** : le crochet ne garde aujourd'hui que le v3, et `.claude/settings.json` ne porte aucune règle
  `allow`. Je ne peux donc pas dire qu'elle bloque un fichier modifié ; la forme décrite (égalité stricte avec l'une des trois
  commandes, dossier courant, fichier non lien, empreinte égale à la constante du crochet et au compagnon) le ferait, comme
  `garder_lanceur_v3` que j'ai lue. À vérifier par ses essais après écriture.
- **Elle doit viser la version corrigée**, pas `a10420cc…` (B1). Et elle n'épingle que le lanceur : le recoupement, pièce servie
  à trois fournisseurs, ne l'est par rien (M8).
- Rien de plus large que l'accord, sous deux réserves : avec la règle et une attestation écrite par la mère (M6), les six
  lancements s'enchaînent sans geste humain ; le crochet tourne toujours sans `-I -B` (m11).

## Constats

### Bloquant

**B1 — Avec l'orchestrateur réel, le lanceur s'arrête sur une exception non gardée à la liste blanche, puis se verrouille.**
`scripts/lancer_course_ideation_bassins_etroits_v1.py` l. 967 (`sceller_existant(chemin)`, l. 599-604, ouverture du compagnon en
mode exclusif) ; `tests/…` l. 44-48. L'orchestrateur réel écrit lui-même le compagnon de la liste blanche
(`pole/ideation_v2.py` l. 2748, `ecrire_json_scelle` ; `pole/outils.py` l. 41-53) ; le faux orchestrateur des essais n'en écrit
pas. Preuve (outil 1, `resultat-verifier-orchestrateur-reel-v1.json`, clé `liste_blanche_reelle`) : la fonction
`construire_liste_blanche` du lanceur, appelée telle quelle contre l'orchestrateur réel (mode sans appel), lève
`FileExistsError` sur `liste-blanche.json.sha256` ; ce n'est pas un `Refus`. Suite, par lecture : `principal` (l. 1197) ne
rattrape que `Refus` → trace, code 1, dossier de run laissé sans manifeste ; au lancement suivant, `runs_du_lanceur` (l. 639)
refuse tout (« état inconnu »). Rien n'est dépensé ; aucune course ne part. Régression par rapport au v3, qui ne scellait pas.
*Correction proposée* : ne pas resceller ; relire le compagnon de l'orchestrateur par `lire_scelle` et porter son empreinte au
manifeste ; faire écrire le compagnon par le faux orchestrateur, comme le vrai ; ajouter un essai qui joue le mode
`--construire-liste-blanche` de l'orchestrateur réel quand le clone est là (sans appel).

### Majeurs

**M1 — Une dépense illisible est comptée 0 : contrôle d'Argon interrompu brutalement.** Lanceur l. 688 et 692. L'orchestrateur
joue le contrôle d'Argon dans `SORTIE-controle/tentative-N-externe-argon` (`demonstrations/ideation_v2.py` l. 1379) ; s'il meurt
sans gestionnaire pendant ce contrôle (plafond 1,5 USD, le plus cher des contrôles), il ne reste que ce dossier. Le lanceur le
range parmi les noms admis et ne cherche les dossiers sans tentative scellée que sous la forme `tentative-N`. Preuve (outil 2,
E1 et E2) : dépense rendue `0.0`, « tentatives de contrôle scellées (course non partie) » ; si le lanceur a survécu (code −9),
`etat_generation` rend « course » : relance permise, cumul à 0. Contraire à « une dépense illisible compte son plafond entier ».
Enjeu : 1,5 USD par occurrence, deux au plus par génération. *Correction* : tout dossier `tentative-N-externe-*` sans
`tentative-N.json` scellé compte le plafond et interdit la relance ; essai artefact.

**M2 — Un refus sans envoi de la commande d'Argon verrouille la génération ; marge mince du contrôle externe.** Lanceur l. 791
(`> 0`) et l. 114. Sur un refus avant envoi, la commande rend le coût plancher 10⁻⁶ (`commande_argon_v3d.py` l. 353 et 1026-1035) ;
l'orchestrateur scelle une tentative à ce coût ; le lanceur y lit une dépense et refuse toute relance, alors que rien n'a été
facturé. Le cas arrive si le compte exact de jetons dépasse caractères / 2,85 sur la consigne de contrôle (E9 : plancher à 3
caractères par jeton 1,4477 pour 1,5 à la génération 1 ; 1,4773 aux générations 2 et 3, marge 0,02 USD) ; or cette consigne est
faite à 80 % de suites de « x » (`fiche_maximale`, `pole/ideation_v2.py` l. 1161-1183), dont le compte par Argon n'est pas
connu de moi. *Corrections proposées* : (a) compter pour nulle une tentative dont les seuls coûts sont le plancher 10⁻⁶ d'un
refus « rien envoyé » ; (b) relever le contrôle externe à 1,7 (somme transmise 7,6 < 8,0 ; pire cas avec bras 8,0 ≤ 8,0 ; tient
jusqu'à 2,36 caractères par jeton) ; à défaut, le dire au devis.

**M3 — Au bras, « pas de relance après dépense » n'est pas gardé par le lanceur, et un essai consacre la relance.** Lanceur
l. 781-787 ; essais l. 376-384. Après un bras fini en code 4 (classement illisible) ou 5 (sans juge externe), `etat_generation`
rend encore « bras » (E8) : le lanceur relancerait l'orchestrateur, écrirait ses manifestes, et compterait 3,1 USD fictifs par
relance. La dépense réelle est empêchée par le seul verrou de l'orchestrateur (`pole/ideation_v2.py` l. 2806-2809). Après un
contrôle court payé et refusé (`bras-tentative-N.json`, l. 3123-3138), l'orchestrateur **permet** la relance et le lanceur la
fait, jusqu'à trois bras : relance après dépense, contre le § 1 de la conception et l'en-tête du lanceur.
`test_bras_relance_apres_echec` fait échouer un bras qui a écrit son manifeste (0,9 USD) puis le rejoue avec succès : ce que
l'orchestrateur réel refuse. *Correction* : refuser de soi-même dès que `manifeste-bras-rapporte.json` existe ou qu'une tentative
du bras a coûté ; ne garder relançable que « bras non joué, rien envoyé » ; aligner le faux orchestrateur et l'essai.

**M4 — Règle de passage : l'appariement des passes est plus large que le texte, se replie en silence, et emploie une mesure que
l'orchestrateur réserve.** Lanceur l. 839-845 et 857.
(a) L'orchestrateur apparie **chaque** fiche de passe 2 à une fiche de passe 1 du même proposeur : même nom, sinon « texte le
plus proche », **sans seuil** (`pole/ideation_v2.py` l. 1389). Le lanceur ignore le mode et la distance : une fiche de passe 2
entièrement neuve est sautée comme « autre passe » d'une fiche prise (E4, distance d'édition 0,97). Pour une question qui
cherche des idées neuves, la règle écarte par construction une part des idées de seconde passe.
(b) Si les mesures de convergence sont en erreur (forme `{"erreur": …}`, prévue par `ecrire_fin`), le lanceur ne saute plus
rien et n'en dit rien (E3) : repli silencieux (R5).
(c) L'orchestrateur écrit de ces mesures : « jamais servies aux juges, ni au classement, ni à aucune sélection (N-053) »
(l. 1316-1317 et champ `regle`) ; le § 6 de la conception dit aussi qu'aucune mesure n'entre dans la sélection, et son § 3.3 (b)
fait le contraire.
*Correction proposée* : n'apparier que « même nom » (ou une distance sous un seuil écrit d'avance), recalculé par le lanceur sur
les fiches scellées ; refus, ou mention au manifeste, quand la mesure manque ; mettre le texte d'accord avec le code.

**M5 — Lecture d'N-053 : elle tient par les mots du GO, pas par l'argument donné ; à confirmer par écrit avant la génération 2.**
Conception § 3 ; lanceur l. 870-873 ; question, dernier paragraphe. N-053 (point 5) : « aucun score de moniteur (sonde, juge)
n'entre dans un signal d'entraînement ou de sélection de l'agent […] il vaut aussi pour la piste "organisme" ». N-065 range le
juge-tournoi parmi les juges dont on mesure la corruptibilité (rôle 1) : dire que les juges de l'atelier « ne sont pas un
moniteur du programme » est faible. Ce qui porte la règle, c'est la ligne du GO, postérieure et précise : « chaque suivante
[reçoit] les fiches retenues de la précédente ». Trois choses à savoir : (i) aucune note n'est servie, mais l'appartenance aux
cinq premières est une fonction des notes, et le texte de tête comme la question disent aux proposeurs et aux juges suivants
que ces fiches ont été « retenues par un tournoi de juges » ; (ii) le repli proposé (tirage uniforme parmi les éligibles) dépend
encore des notes ; (iii) l'étiquette `raffine G…-R…` est dans `questions_servies`, donc **lue par les juges**, qui reçoivent
aussi les fiches reçues comme pièce d'antériorité (« occupé d'après les pièces ») : la mesure déclarée du § 6 n'est pas
indépendante de la sélection. *Proposition* : une ligne de Lazar, ou de la mère dans `registres/decisions.md`, qui dit que
« fiches retenues » vaut exception voulue à N-053 pour l'atelier (rôle 2) et que ces trois courses ne servent ni le rôle 1 ni
une revendication sur l'effet des générations ; la génération 1 n'en dépend pas.

**M6 — « Lecture humaine » : qui lit n'est pas tranché.** Conception § 1 (« la mère, ou Lazar ») ; lanceur l. 995-1004. La mère
est un modèle ; le champ et l'option s'appellent « lecture humaine », et l'orchestrateur en fait le seul chemin par lequel un
juge d'une autre lignée reçoit les fiches. Le lanceur ne vérifie que des empreintes, qu'il imprime lui-même « à recopier ». Si
la mère atteste, les six lancements s'enchaînent sans humain. *Proposition* : décider et consigner (Lazar lit ; ou bien la mère
lit, l'attestation le dit en clair dans `lecteur`, et un mot de Lazar ou un précédent cité l'admet). Mineur lié : le chemin est
fixé à `-v1.json` ; une attestation fautive ne se remplace pas sans écraser (R12).

**M7 — Durée de la course contre la borne de l'outil de lancement.** Devis § 4 (« 1 à 2 heures, borne ≈ 10 heures »). D'après la
description de l'outil Bash de ma propre session, une commande en arrière-plan est arrêtée à sa limite : 30 minutes par défaut,
**2 heures au plus**. La commande permise est exacte : ni `nohup`, ni `&`, ni enveloppe. Si l'outil arrête le lanceur en route :
avec un signal relayé, la course s'arrête proprement, dépense comptée, génération non relançable ; avec un arrêt brutal du
groupe, la sortie reste sans manifeste de fin, 20 USD sont comptés au cumul et la génération est bloquée. *Propositions* :
vérifier la limite dans la session qui lancera et donner la limite maximale ; borner les délais transmis à l'orchestrateur pour
que leur somme tienne sous cette limite ; ou, dans la version corrigée, détacher l'orchestrateur et faire reprendre une course
finie seule. À dire au devis.

**M8 — Le recoupement, servi à trois fournisseurs à la génération 1, n'est ni épinglé ni relu.** Lanceur l. 94 et 982-992.
Le lanceur n'en vérifie que le sceau, l'encodage et la taille ; son compagnon s'écrit en même temps que lui. La règle de
permission couvrirait donc un contenu qui n'existe pas encore (le v3 épinglait toutes ses pièces). *Proposition* : épingler son
empreinte dans la version corrigée du lanceur, après une relecture « niveau méthode, aucun secret, aucune recette » par un
lecteur qui ne l'a pas écrit.

**M9 — Témoins : ils écartent des erreurs grossières, et l'un peut échouer chez un juge sain.**
(a) Le témoin « vrai » (courbe nulle 1 − (1 − r)^n comme témoin à coût égal) est attendu éligible ; son idée est celle que la
question demande presque en toutes lettres (« témoin à coût égal », « même budget de tirages indépendants ») : elle a toutes
chances d'être dans le recoupement (pas encore écrit) puis dans les fiches reçues. Les juges ont ces pièces et la grille
« originalité 0 : occupé d'après les pièces » : le témoin ne tient alors que par l'avantage ≥ 2. Un échec rend le classement
illisible, la chaîne s'arrête après ≈ 7 USD. *Proposition* : relire le témoin vrai contre le recoupement avant de sceller
celui-ci ; s'il y figure, changer de témoin (fichier neuf).
(b) Ils sont écrits par Claude Opus 5.5, le modèle d'un proposeur et du juge `opus-juge` : « tiers » vaut pour l'instance, pas
pour le modèle.
(c) `faux_falsifiabilite` se déclare lui-même sans avantage et « occupée » : son inéligibilité ne coûte rien au juge ; seule la
note de falsifiabilité ≤ 1 l'éprouve. `faux_anteriorite` et `jumeau` (mêmes chiffres, paraphrase) sont faciles.
(d) Longueurs servies : 3 463, 2 709, 1 384, 1 790 caractères ; des fiches réelles de 5 000 à 8 000 les rendront discernables
(l'orchestrateur le rapporte). Aucun témoin n'éprouve ce que la question cherche (distinguer un bassin étroit d'un raffinement)
ni l'auto-préférence.

### Mineurs

**m1 — GO : une révocation mal formée est ignorée** (l. 250 ; E6) : neuf colonnes, « revocation », « Révocation » laissent passer
le GO révoqué (le crochet, lui, bloque sur un registre mal formé). Hérité du v3. Correction : toute ligne `GO-…` qui cite
l'identifiant et n'est ni la principale ni une extension bien formée refuse.

**m2 — Un bras joué hors du lanceur compte 0** (l. 702 ; E7). Correction : lire la sortie même sans manifeste de bras du lanceur.

**m3 — Le plafond de 50 000 caractères porte sur la somme des fiches servies, pas sur la pièce** (l. 861 ; E5 : pièce = somme
+ 406). Sans effet sur les gardes (la mesure est rejouée) ; accorder le texte.

**m4 — Doublons : l'union des juges suffit, sans fermeture transitive** (l. 829-838) : un seul juge écarte une fiche ; A~B
chez l'un et B~C chez l'autre laissent passer A et C. À écrire dans la règle.

**m5 — Étiquettes `G<g>-R<k>`** (l. 869) : « R1 » se lit « rang 1 », alors que l'ordre est celui des empreintes ; et les fiches
transmises à la génération 3 portent des `raffine G1-…` inconnus de ses lecteurs. Proposition : étiquettes sans chiffre d'ordre.

**m6 — Bras lancé sans `--moteur claude-sdk`** (l. 941-947 ; outil 1) : la vérification du modèle avant l'appel et
`exiger_modele_servi` sont inactives (`demonstrations/ideation_v2.py` l. 748 et 758) ; la barrière agit quand même parce que la
commande v3d rend toujours la clé `modele_servi`. L'ajouter serait plus sûr, à éprouver par l'analyseur.

**m7 — Gardes sans artefact (R5)** : les six mutants survivants (tentatives de course, min à 60, consigne à l'attestation, trois
bras, manifeste du bras, plancher du contrôle court) ; et, par lecture des essais : préfixe du cache, liste blanche différente,
mesure illisible, run sans manifeste, version ou génération incohérente, attestation mal formée, aucune fiche éligible.

**m8 — Toute exception autre que `Refus` après la création du dossier de run** (l. 1098-1115) laisse un run sans manifeste et
bloque tous les lancements suivants (B1 en est un cas). Correction : manifeste de refus sur toute exception.

**m9 — Garde lexicale « niveau méthode » de l'orchestrateur** (`pole/ideation_v2.py` l. 212-222), faite pour le pilier attaque :
« injection », « exploiter », « étape 1 : », « pour éviter … juge », « lance un script » mettent une fiche en quarantaine. Outil 1 :
7 de mes 10 phrases d'essai, écrites pour toucher les motifs, sont signalées ; 0 des 30 paragraphes des pièces servies. À
compter par motif après la course et à lire par le lecteur ; à dire aux limites.

**m10 — Devis** : aucun précédent mesuré pour Fable 5.1 en proposeur à 2,0 USD par session (le devis dit la course du 8 novembre
« sans Fable ») ; un refus de la question par un modèle Claude n'apparaîtrait qu'après ≈ 2 USD d'Argon (la sonde à 0,003 USD
que le préparateur propose vaut son prix) ; des fiches de plus de ≈ 14 400 caractères en moyenne rendent le bras impossible après
une course payée (garde de 600 000 caractères).

**m11 — Crochet lancé sans `-I -B`** (`.claude/settings.json` ; mineur m-v3-2 de la vérification du v3, non repris).

**m12 — Question** : Q2 dit « pourquoi il bat le même budget », là où le cœur dit « pourquoi elle atteindrait … mieux » ; le
gabarit du noyau annonce « Q1 … Q7, Q-pont » alors que la question définit Q1 à Q5. Et dix des treize modules `pole` chargés ne
sont tenus que par le commit ; je n'ai pas pu comparer `f39a7f4a` à `be6b5af9` hors des neuf fichiers (commit absent du clone).

## Ce que la même lignée interdit de conclure

Juges : Opus 5.5 et Argon ; proposeurs : Opus 5.5, Fable 5.1, Argon. Chaque juge a un proposeur de son modèle ; Fable est le
seul proposeur sans juge de son modèle. On ne peut donc conclure : (1) rien sur la valeur relative des proposeurs (un écart
entre les fiches de Fable et les autres est confondu avec l'auto-préférence ; N-058 l'interdit de toute façon) ; (2) pas qu'une
idée qui survit aux trois générations est bonne ou originale : seulement que deux familles de modèles, qui la proposent et la
jugent, la préfèrent ; (3) pas que des témoins tenus valident les juges au-delà des fautes grossières, d'autant que les témoins
viennent du modèle d'un juge ; (4) rien sur l'effet des générations (aucun bras témoin, la conception le dit). L'anonymisation
cache l'auteur, pas le style.

## Ce que je n'ai pas vérifié

- Aucune course ni aucun bras, réel ou simulé ; le bac à sable (non sondé par moi) ; les relais Claude et Gemini ; le compte
  de jetons d'Argon sur les consignes réelles.
- Le recoupement (absent) ; la règle et l'épingle (non écrites) ; le programme des mesures entre générations (non écrit).
- Les lignes de registre citées par le préparateur (R-607, R-1862 à R-1865, R-1978 à R-1994) et le barème Claude du devis.
- L'adaptateur Claude de l'orchestrateur au-delà de la lecture du plafond de session ; les modules `pole` non nommés plus haut.
- La suite d'essais du v3 et la suite complète du dépôt (interdit 5) ; `verifier-arbre` (interdit 9).
- La limite de durée de l'outil Bash dans la session qui lancera (M7 repose sur la description de l'outil dans la mienne).

## Outils (scellés, `docs/notes/organisme-bassins-etroits-v1/contre-lecture-outils-v1/`)

| Fichier | Empreinte SHA-256 |
|---|---|
| `verifier_orchestrateur_reel_v1.py` | `c5bc9bad55ee45c7b428bbce63d685f7219efc5afcae02abdc0924319271c579` |
| `resultat-verifier-orchestrateur-reel-v1.json` | `996649ae344e6882273b94f07e4b3ef2d372cc64f24c2ecb62bec1b8d7b0d6c7` |
| `eprouver_gardes_lanceur_v1.py` | `1ef78213e22a673e53ea313ea6a743e616f1de43cbb539c476aa099bc7f1bf3a` |
| `resultat-eprouver-gardes-lanceur-v1.json` | `1cc65dc842b992258faefbe21e855bfcd01e0919cefc8b80ceaa2dfb740bcd3d` |
| `mutations_lanceur_v1.py` | `6fdac21dd4ba7a2f201a9ac9c2767edc051893ceb2694b124372bc1534a37a50` |
| `resultat-mutations-lanceur-v1.json` | `b807e07a52a4712c8c0e251a5c696476d6c24adf736ca6e328762555d42ca794` |

Les trois outils se relancent sur un dossier de travail neuf, hors du dépôt ; le premier et le deuxième sous
`/usr/local/bin/python3 -I -B`, le troisième sous l'interpréteur de `.venv` (pytest), un processus d'essais à la fois. Les
fichiers relus n'ont pas changé (lanceur `a10420cc…`, essais `8fa7ae32…`, recalculés après mes outils).

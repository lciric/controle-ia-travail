# Contre-lecture 4 du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v3.md`) — v1

Relecture courte de ce qui a changé depuis la contre-lecture 3 (pas une relecture complète).

- **Texte relu** : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v3.md`,
  `228d266c1cd31e5c9880cbf6d7f7a093f60eb9a78507412615c7c8e71152315a` (empreinte vérifiée sur disque avant lecture ;
  625 lignes ; commit cité par la demande : `92a8727`, non vérifié, pas de `git`). Texte d'avant :
  `texte-v3-tel-que-relu-par-cl3.md`, `efffb7e4bd46320feb95835faec9369b19a70039e6765e3d4710e62ecf7cebfd` (vérifiée).
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit, le 25 octobre 2026. Début lu sur
  `date -u` : 21:59:00 UTC ; ce rapport est écrit à partir de 22:19:40 UTC (heure lue sur `date -u` juste avant).
  Je n'ai écrit ni ce texte, ni ses versions précédentes, ni le noyau, ni les lanceurs, ni les batteries, ni les essais
  complémentaires, ni les contre-lectures 1 à 3.
- **Lu** : le texte relu en entier ; l'écart `efffb7e4` → `228d266c` en entier (recalculé, 282 lignes, 13 blocs :
  `ecarts/diff-texte-v3-efffb7e4-vers-228d266c.txt`) ; la contre-lecture 3 en entier (`0d95ea8c…`) ;
  `deriver_essais_pilote4_v8.py` en entier ; l'écart des batteries v7 → v8 en entier (recalculé) et la batterie v8 aux
  lignes 20–259 (aides, cas sains) et 460–647 (segments, cas nouveaux, copie mutée) ; les journaux des séries v9 et v8 en
  entier et leurs fichiers d'heures ; le lanceur v6 aux lignes 180–349, 500–516, 640–665 et 725–908 (et, par `grep`, aux
  lignes 42–45, 84, 115–124, 152, 176, 523–543 et 622) ; `boucle.py` l. 668–680 et 960–1154 ;
  `tests/test_reprise_segments.py` l. 1–120 et 236–335 ; `bac_a_sable.py` l. 50–70, 118–150, 278–296 ; `serveur.py`
  l. 15–24 et 56–82 ; `appels.py` l. 5–44 (par `grep`) ; `outils/extrait_mecanique.py` l. 59–61 et 258–262 ; les
  essais complémentaires du noyau (`essais-noyau-complementaires-v1/` : essais en entier, journal, scripts de
  mutations v1 et v2, leurs journaux, cause de l'essai d'installation) ; `contre-lecture-3-v1/LISEZMOI-v1.md` et la liste
  de `EMPREINTES-v1.txt` ; la liste de `EMPREINTES-pieces-pilote4-v5.txt` ; `sceller_pilote4_v3.py` l. 1–98 ; T2
  (`d2944654…`) l. 410–436 ; la v6.1 extraite, `principal.py` l. 920–935 ; dans les dossiers de la série v9 (simulations) :
  `lanceur-mutant-minuteur.sh`, `cas-mut-minuteur-segment1/pilote4-gemini-v5-3-v1/LANCEMENT.md` en entier, sa
  `segment-2-t1/sortie-erreur-lanceur.txt`, les sorties des deux cas du lanceur muté, les lignes d'en-tête de segment, de
  refus, de minuteur, d'état et de fin de `cas-seg-segment1/pilote4-gemini-v5-3-v1/LANCEMENT.md`, `etat-v1-restaure.txt`
  et les deux sauvegardes de compagnon ; le nombre de lignes des journaux d'appels recopiés de quatre cas de simulation et
  les événements d'arrêt et de reprise de deux extraits de simulation (champs mécaniques seulement).
- **Non lu ni ouvert** (consignes) : aucun fichier `…-cle.json` ni `…-secret.json`, aucun dossier `donnees/`, `runs/`,
  `diag/`, aucun `P3-consignes-v1.md` ni fichier `textes-actions-…`, aucune archive `ferme.tar.gz` (seulement leur nom vu
  dans des listes de dossiers de simulation), aucun fichier `reponse-question*`, `journal-appels*` ou `extrait-mecanique*`
  des pilotes réels. Non relus (hors de l'écart) : P3, les contre-lectures 1 et 2, le reste du lanceur et de la batterie
  (la batterie v8 est vérifiée par redérivation), le reste du noyau, les pièces `simulation-lanceur-v6/` et
  `faits-pilote3-v1/`, la banque, les essais du script de scellement ; le brief fourni (`brief-cl4-v1.md`, `ee505b27…`)
  n'est que la demande qui m'a été faite.
- **Exécuté** (sorties sous `/var/tmp/contre-lecture-pilote4-v4/` seulement) : `date -u` ; `sha256sum` sur les pièces
  citées ; `sha256sum -c EMPREINTES-pieces-pilote4-v5.txt` depuis `pieces-pilote4-gemini/` après lecture de sa liste
  (aucun nom interdit ; seuls des extraits et journaux de **simulation**), deux fois (avant et après mon essai du noyau) ;
  `sha256sum -c` des sept compagnons des essais complémentaires et de `contre-lecture-3-v1/EMPREINTES-v1.txt` ; pour les
  22 fichiers que ce dernier liste à l'intérieur des deux archives de la contre-lecture 3, une empreinte calculée au fil
  (`tar -xOzf … | sha256sum`, rien n'est extrait sur disque) ; `diff` (texte, batteries v7 → v8, lanceur v6 → copie
  mutée, journaux v8 et v9 après remplacement des chemins de travail) ; `deriver_essais_pilote4_v8.py` sur la batterie v7
  (`rederive/`) ; les essais complémentaires du noyau depuis `essaim-m3-refonte-v1`, avec `env -i`, `HOME`,
  `ESSAIM_M3_ESPACE` et `--basetemp` dans mon dossier (chemins courts) : **9 passés en 16,62 s**
  (`essais-noyau/essais-complementaires-cl4-v1.txt`) ; ces essais font tourner les organismes d'essai du noyau
  (`tests/fixtures/`), aucun organisme de Gemini ; leurs dossiers temporaires ont été effacés après lecture du résultat ;
  rien n'a été écrit dans le dépôt (pièces revérifiées) ni sous `/var/lib/essaim-m3` (heure de modification antérieure à
  mon essai) ; mon propre code, lecture seule : empreintes « blob » sans `git` (`outils/blob_v1.py`), relevé des noms de
  cas des deux journaux, relevé des appels par unité (`ecarts/releve-appels-serie-v9-cl4.txt`). **Écart à la lettre de la
  consigne, signalé** : un `find -type f` (noms seulement) dans `pieces-pilote4-gemini/`, pour comparer la couverture du
  fichier d'empreintes (`ecarts/fichiers-pc-ls.txt`) — c'est une liste récursive d'un dossier nommé, au-delà de « `ls`
  d'un dossier nommé » ; aucun contenu lu ; la liste obtenue est celle du fichier d'empreintes plus lui-même et son
  compagnon. **Rien** du lanceur, des batteries, des scripts de mutations ni du code des organismes de Gemini n'a été
  exécuté. Aucun `git`, aucun sous-agent.

## Verdict

**Scellable après corrections mineures.** L'écart du texte fait ce que dit son § Traitement de la contre-lecture 3, et
rien d'autre, hors la mise à jour du statut et deux phrases de forme sur les batteries et la série v9. La batterie v8 se
redérive octet pour octet (`a5f4b944…`, cinq remplacements) ; chacun de ses dix cas nouveaux vise la garde nommée et non une garde antérieure ;
chaque artefact est retiré ensuite (manifeste, verrou, dossier, état restauré à l'octet près, vérifié) et le segment 2
sain qui suit passe ; la copie mutée du lanceur ne diffère que par la condition du minuteur (l. 770). La série v9 est
complète et conforme : 228 sur 228, les 218 cas de la série v8 dans le même ordre et dix nouveaux. Les essais
complémentaires essaient les trois refus du noyau sur un cas sain et sur un artefact, motifs propres à chaque garde, et
passent chez moi ; les trois mutations retirent la garde visée (texte unique dans `boucle.py`) et sont détectées. Les
chiffres sont justes (7 075 s, 125 s ; 2 969 et 5 578 s). Le texte tient dans les deux cas soumis à Lazar.

Deux constats mineurs, de texte seulement, sans changer ni le noyau, ni le lanceur, ni la batterie : la règle nouvelle du
minuteur mort ne garantit pas la borne qu'on lui fait porter et se déclencherait, lue à la lettre, à la fin normale de
chaque course (P4C4-01) ; « restent deux gardes » : trois refus d'absence du segment K ≥ 2 ne sont jamais essayés
(P4C4-02). Trois remarques suivent. Au remplissage de `[[CONTRE_LECTURE_DETAIL]]` : citer `228d266c…` comme texte relu
par cette contre-lecture, et l'écart de `228d266c` au texte scellé (les seules corrections de ce rapport).

## Traitement des constats de la contre-lecture 3

| constat | statut | ce que j'ai vérifié |
|---|---|---|
| P4C3-01 (mineur) | **levé** | Canal (d) déclaré (texte l. 395–400), aux mots de la correction proposée, plus « un bit par génération sur les scores de `test`, jamais sur ceux de `test_final` » ; pendant un segment, session-depot ne lit du journal de l'unité en cours que ce que T2 nomme, « jamais les rôles des appels » (l. 386–388 ; T2 l. 418–422) ; ligne de mutation de la liste d'arrêt lue au moment de lecture (l. 445). v6.1 `principal.py` l. 926–933 : stagnation si le dernier score dépasse l'avant-dernier d'au plus 0,01, scores vides écartés (`is not None`), mutation tentée si `generation >= 1` et stagnation. |
| P4C3-02 (mineur) | **levé** | Ligne du `STOP` humain (l. 437) : « reprise attendue » au `LANCEMENT.md` comme pour le minuteur, reconnaissance par la ligne « minuteur : STOP posé dans course/ à … » (lanceur l. 778), pas de segment suivant sans le mot de Lazar, `SEGMENT=K+1` et `SEGMENT=K+1 CLORE=1` (lanceur l. 214–215, 805) ; porte (l. 448) : un `STOP` humain repris compte comme un `STOP` repris, à dessein ; § Bornes l. 290–291. |
| P4C3-03 (mineur) | **levé en partie** | Noyau : les trois refus nommés sont essayés à part (9 sur 9, chez moi aussi ; trois mutations détectées, P4C4-06). Lanceur : cinq gardes du segment K ≥ 2, la numérotation des reprises de la porte et la condition du minuteur sont essayées sur un artefact (batterie v8, série v9) ; deux gardes de fermeture dites non essayées (l. 488–490). **Reste** : trois refus d'absence du segment K ≥ 2 jamais essayés, alors que le texte dit « restent deux gardes » (P4C4-02). |
| P4C3-04 (remarque) | **levé** | § Bornes l. 287–288 ; le lanceur écrit « essais : 169 passés, 0 sauté, 0 désélectionnés ; arguments : « aucun » » (l. 663 ; série v9, dossier du lanceur muté, l. 19 et 54). Quand session-depot le vérifie : voir P4C4-01, point (d). |
| P4C3-05 (remarque) | **levé** | Ligne « reprise refusée » (l. 440) ; vu dans la série v9 : « échec inattendu (code 9) à la ligne 787 … laissé (à examiner) » puis « reprise refusée par le noyau » (`cas-seg-segment1`, l. 162 et 165 ; lanceur muté, l. 65 et 68), verrou du segment 2 retiré ensuite (lanceur l. 806 ; absent du dossier du lanceur muté). |
| P4C3-06 (remarque) | **levé en partie** | (a) Borne : 7 060 + 10 + 5 = 7 075 s, 125 s sous 7 200 s ; `bac_a_sable.py` l. 288–292 (`proc.wait(timeout=10)` après l'arrêt du groupe), `serveur.py` l. 71–72 (`join(timeout=5)`), `ATTENTE_FILS_S = 900` (l. 21) ; estimations du dépôt et de la fermeture dites. Minuteur mort : règle ajoutée (l. 299–304, 436–438, 389), cohérente avec celle du `STOP` humain et applicable sans lecture interdite, mais incomplète (P4C4-01). (b) « préparation, noyau et fermeture compris » ; 2 969 et 5 578 s, noyau seul 2 773 et 5 378 s (≈ 46 et 90 minutes) : justes (P4C4-05 b). |
| P4C3-07 (remarque) | **levé** | Ligne « course arrêtée en cours » (l. 444) et § Essais (l. 488–490), lanceur l. 804–823 ; deux inexactitudes de détail (P4C4-04). |
| P4C3-08 (remarque) | **levé** | § Bornes l. 271–275 ; `boucle.py` l. 1074–1076 (existence), l. 1070–1073 (sous la racine de la course). |
| P4C3-09 (remarque) | **levé** | Trois champs de l'état et nombre de lignes du journal (l. 284–286 ; lanceur l. 262–264, 746, 770 ; voir P4C4-05 c) ; « sans successeur valide après relance » (l. 445) ; critère 3 (l. 113) ; deux clés `segments` et `reprises` (l. 97 ; `boucle.py` l. 1145–1146 ; `CHAMPS_RAPPORT` ne les porte pas, `extrait_mecanique.py` l. 59–60) ; § Pièces (cause de la série v7, « toutes les autres pièces du dossier ») ; `git fetch origin main` (l. 281–282 ; lanceur l. 523, 530) ; date des lignes de dépense (l. 366) ; marqueurs de rédaction remplis à la main par conv-audit (l. 620) ; les deux points sans effet laissés. |
| P4C3-10 (conforme) | sans objet | — |

## Constats

### P4C4-01 — mineur — La règle du minuteur mort ne garantit pas la borne qu'on lui fait porter, et se déclencherait à la fin normale de chaque course

- **Fait, texte.** § Bornes l. 299–304 : session-depot lit le PID du minuteur et son échéance, « vérifie à ses réveils,
  pendant le segment, que ce PID vit encore (`kill -0`, jamais un arrêt) ; s'il ne vit plus avant l'échéance,
  session-depot pose lui-même `STOP` dans `course/` à l'échéance ». La liste d'arrêt en fait la garde de la borne : « la
  borne de 7 075 s (§ Bornes) exclut la coupure au délai de 7 200 s, minuteur vivant vérifié par session-depot » (l. 436 ;
  aussi l. 438).
- **Fait, lanceur.** (a) Le minuteur s'arrête normalement **avant** l'échéance chaque fois que la course finit avant
  elle : sa boucle tourne tant que la course vit (`while kill -0 "$PID"`, l. 775), puis le lanceur l'arrête (l. 788) et
  écrit « minuteur arrêté par son PID (…) à la fin de la course : STOP non posé » (l. 793). C'est le cas du dernier segment
  de toute course, d'une reprise refusée (code 9) et de toute fin du noyau : série v9, segment 2 sain de
  `cas-seg-segment1`, `LANCEMENT.md` l. 194–196 (échéance 22:52:40 UTC, fin du processus 21:56:08 UTC). La règle ne
  pose aucune condition sur la course : un réveil pendant la fermeture (étape 8a), ou une lecture de « pendant le
  segment » comme « tant que la commande du lanceur n'a pas rendu », prescrit un `STOP` « à l'échéance » dans une course
  fermée (`course/` effacé l. 871, ou gardé si l'archive est incomplète) et une ligne fausse au registre des arrêts.
  Sans effet sur les données, mais c'est une action que le texte scellé prescrit à tort.
  (b) Après son `STOP`, le minuteur sort aussi (l. 779) : passé l'échéance, un minuteur mort ne se distingue d'un
  minuteur qui a fait son office que par la ligne « minuteur : STOP posé dans course/ à … » (l. 778), que la règle
  n'emploie pas. Un minuteur mort entre le dernier réveil de session-depot et l'échéance n'est donc pas vu à temps ; or le
  `STOP` de remplacement doit tomber au plus 125 s après l'échéance pour que la borne tienne (7 075 + délai ≤ 7 200), ce
  qui demande un réveil programmé à l'échéance, que le texte ne demande pas.
  (c) `kill -0` dit qu'un processus de ce PID existe, pas que c'est le minuteur ; en une heure de course, le noyau lance
  beaucoup de processus (série v9 : PID du minuteur 16 704 à 21:55:50 UTC, 23 438 à 21:56:39 UTC, moins d'une minute
  plus tard), un PID repris passerait pour vivant.
  (d) § Plan, point 3 (l. 386–390) ne permet de lire au `LANCEMENT.md`, pendant un segment, que « les lignes du minuteur
  (PID et échéance) » : pas la ligne « STOP posé », ni celle de la fin du processus, ni celle de l'espace attendu, qui donne
  le chemin du journal consulté (T2 l. 421), ni la ligne des essais que P4C3-04 fait vérifier ; toutes sont
  mécaniques et sans score, et lisibles entre deux segments.
- **Cohérence avec la règle du `STOP` humain** : tenue. Le `STOP` de remplacement « vaut celui du minuteur » (l. 437,
  seule exception), il est consigné au registre des arrêts, le segment suivant part sans Lazar et la porte l'accepte comme
  tout `STOP` repris (l. 448). Applicable sans lecture interdite : oui, tel qu'écrit (ligne du PID, `kill -0`, fichier
  `STOP`, l. 274) ; la correction ci-dessous n'ajoute que des lignes du `LANCEMENT.md`.
- **Correction** (texte seul). § Bornes, l. 300–304 : « Session-depot lit au `LANCEMENT.md` la ligne « minuteur : PID … ;
  échéance … » et se réveille à l'échéance (réveil programmé, au plus 60 s après : la marge est de 125 s). Si alors la
  course tourne encore (la commande de fond du lanceur n'a pas rendu, et le `LANCEMENT.md` ne porte pas la ligne « fin du
  processus ») et que le `LANCEMENT.md` ne porte pas la ligne « minuteur : STOP posé dans course/ à … », il pose lui-même
  `STOP` dans `course/` : ce `STOP` tient lieu de celui du minuteur (consigné avec son heure au registre des arrêts,
  rapporté comme réserve) et le segment suivant part comme après le minuteur. Avant l'échéance, `kill -0` sur le PID du
  minuteur n'est qu'une alerte ; un minuteur arrêté parce que la course a fini (« minuteur arrêté par son PID … à la fin
  de la course ») n'appelle rien. » § Plan, point 3, l. 388–389 : « … et, au `LANCEMENT.md`, ce que le lanceur y écrit
  (lignes mécaniques, aucun score ; dont l'espace attendu, les essais et les lignes du minuteur) ». Liste d'arrêt, l. 436 :
  « … exclut la coupure au délai de 7 200 s si le `STOP` tombe au plus 125 s après l'échéance (minuteur, ou session-depot
  à sa place, § Bornes) ». Table de correspondance, l. 101 : « … ou, minuteur mort, session-depot à l'échéance
  (§ Bornes) ».

### P4C4-02 — mineur — « Restent deux gardes » : trois refus d'absence du segment K ≥ 2 ne sont jamais essayés

- **Fait.** Ni la batterie v8 ni le journal de la série v9 ne portent les motifs de trois refus du lanceur v6 propres au
  segment K ≥ 2 (aucune occurrence dans `essais_lanceur_pilote4_v8.sh` ni dans `essais-lanceur-pilote4-v9.log`) :
  « aucun état de reprise » (`lire_etat_reprise`, l. 256, appelé l. 268) ; « organisme du segment 1 absent » (l. 504) ;
  « question du segment 1 absente » (l. 512). De même, le second membre de la l. 206 (dossier présent, `LANCEMENT.md`
  absent) : `seg-sans-course` essaie un dossier absent. Les cas `seg-organisme-modifie` et `seg-question-modifiee`
  changent un fichier, ils n'en retirent aucun.
- **Fait, texte.** § Essais l. 488–490 ne nomme comme « gardes lues dans le code, non essayées sur un artefact » que les
  deux gardes de fermeture ; le § Traitement dit « restent deux gardes, dites » (l. 614). La contre-lecture 3 ne les
  nommait pas non plus.
- **Portée.** Chacune double une garde essayée (l. 215 et le refus du noyau « aucun état de reprise », essayé dans le
  noyau ; l. 509–511 et 514 sur le contenu de l'organisme et de la question) ; aucune ne change la course saine. C'est la
  même nature que P4C3-03 : le texte affirme davantage que ce qui est essayé.
- **Correction** (texte seul). § Essais, l. 490 : « … ; de même, non essayés sur un artefact : « aucun état de reprise »
  (l. 256), organisme ou question du segment 1 absents (l. 504 et 512), `LANCEMENT.md` absent d'un dossier présent
  (l. 206) — chacun doublé par une garde essayée ; au prochain lanceur. » § Traitement, l. 614 : « restent deux gardes de
  fermeture et quatre refus d'absence, dits (§ Essais) ».

### P4C4-03 — remarque — Refus du segment K ≥ 2 : « le motif corrigé » ne convient pas aux motifs qui disent une course altérée

- **Fait.** La ligne « segment K ≥ 2 refusé par le lanceur avant le noyau » (l. 439) donne à tous ses motifs le même
  effet : « le motif corrigé, le même segment peut être relancé (…) ; une seule nouvelle tentative sans Lazar ». La liste
  s'allonge, dans cet écart, de « course sans manifeste », « verrou … du segment 1 », « autre course de ce nom » et
  « état de reprise … d'un autre arrêt ou d'un autre segment ». Or ces motifs, comme « marqueur », « état de reprise
  altéré » et « organisme ou question modifiés » déjà présents dans la v3 relue par la contre-lecture 3, ne se corrigent
  pas sans toucher à `course/`, ce que le texte interdit désormais (« personne ne touche à `course/` hors du fichier
  `STOP` », l. 274), ou sans réécrire les copies du segment 1 (« jamais réécrits », lanceur l. 503). Ils disent une
  altération de la course ou de son dossier entre deux segments (R3 pour la course de même nom ou le marqueur) : un fait
  suspect, à examiner (R4), non un motif d'exécution.
- **Correction.** Séparer l'effet : motifs d'exécution (ordre des segments, ligne de dépense, reste du GO, test de
  dépense, essais, `HEAD`, lanceur, verrou du segment laissé par un lanceur interrompu) → une seule nouvelle tentative
  sans Lazar ; motifs d'altération (course sans manifeste, verrou du segment 1 absent, marqueur, autre course de ce nom,
  état de reprise altéré, d'un autre arrêt ou d'un autre segment, organisme ou question modifiés) → rien n'est corrigé,
  session-depot s'arrête et attend Lazar.

### P4C4-04 — remarque — « Avec réserve » et « un noyau défaillant » : deux inexactitudes de détail

- **Fait.** L. 444 : au segment K ≥ 2, un code du noyau autre que 0 et 9, ou un état de plus non conforme, « ferme la
  course (étape 8a du lanceur, avec réserve) … (lu dans le code, non essayé : il y faudrait un noyau défaillant) » ;
  l. 488–490 : « la course est alors fermée, avec réserve ; l'un et l'autre demandent un noyau défaillant ». Le lanceur
  n'écrit une réserve que pour l'état non conforme (l. 821) ; pour un autre code, il passe à l'étape 8a sans autre ligne
  que « fin du processus … code de retour : N » (l. 795, 834–875). Et un tel code ne demande pas un noyau défaillant :
  un environnement où l'isolation manque fait refuser le noyau à sa construction (code 7, selon P4C3-07), et une copie
  mutée du lanceur, comme celle du minuteur (batterie v8 l. 621–642), le provoquerait aussi (un argument que le noyau
  refuse).
- **Correction.** « (étape 8a ; avec réserve pour l'état non conforme) » ; « il y faudrait un noyau ou un environnement
  défaillant, ou une copie mutée du lanceur ».

### P4C4-05 — remarque — Petits faits et formulations

- (a) L. 529–530, « Dans la série v9, ces quatre cas donnent les mêmes nombres d'appels par unité (relevé à la machine
  dans les journaux d'appels de la simulation) » : juste (mon relevé, `ecarts/releve-appels-serie-v9-cl4.txt` : c001 6
  ou 7, g000 123, g001 129, g002 123, g003 123 ou 124 ; reprises à 6 appels et 0,088 USD, puis 129 appels et 1,896 USD),
  mais ce relevé n'est pas une pièce (R6) : le journal de la série v9 ne le porte (lignes `RELEVÉ`, identiques à celles
  de la série v8) que pour les deux cas continus. Citer ces lignes, et dire que les deux cas en segments ont été relevés
  hors des pièces, ou ajouter le relevé aux pièces.
- (b) L. 305–306 et 315–317 : les totaux prennent 193 et 196 s de préparation, mesurées au pilote 3 avec 141 essais ; avec
  169 essais (≈ 233 s pour la suite seule, l. 306), la préparation est plutôt de 4 à 5 minutes par segment que de « ≈ 3
  minutes » (l. 316). La conclusion (un ou deux segments par course) ne change pas.
- (c) L. 284–286, « rien d'autre de la course » : le lanceur lit aussi la présence de fichiers de `course/` (manifeste,
  l. 208, 770, 811 ; `STOP`, l. 747, 790 ; nombre d'états, l. 250) et le compagnon de l'état (l. 258–260), tout mécanique.
  Écrire « rien d'autre du contenu de la course ».
- (d) Essai complémentaire du dernier événement (`test_reprise_refus_complementaires_v1.py` l. 73–83) : il change la
  raison, non l'étape ; le premier membre de la disjonction (`boucle.py` l. 1038, étape autre que « arret ») n'est pas
  essayé. Sans portée (une garde, un artefact, R5 tenue).
- (e) L. 389–390, « entre deux segments, seulement ce que le lanceur écrit au `LANCEMENT.md` » : le motif d'une reprise
  refusée est dans la sortie d'erreur du segment (lanceur l. 805, « motif dans segment-K-tA/sortie-erreur-lanceur.txt » ;
  série v9 : « refus : reprise : le fichier STOP est encore dans la course … »), sortie d'erreur sans score (T2
  l. 412–418), et la décision de Lazar « relancer le segment après correction » (l. 440) en a besoin. La dire lisible
  entre deux segments (défaut ancien, la phrase existait dans la v3 relue par la contre-lecture 3).
- (f) L. 274, « hors du fichier `STOP` (posé par le minuteur ou à sa place, retiré par le lanceur à la reprise) » :
  ajouter « ou par une main humaine (incident, liste d'arrêt) ».

### P4C4-06 — conforme — Ce que j'ai trouvé conforme

- **Empreintes** (recalculées sur disque) : texte `228d266c…` ; v3 relue par la contre-lecture 3 `efffb7e4…` ;
  contre-lecture 3 `0d95ea8c…` et son compagnon `9e65949a…` ; batteries v8 `a5f4b944…` et v7 `c3263af1…` ; dérivations
  v8 `29c48401…` et v7 `553eeb4c…` ; journaux v9 `51abe3e2…` et v8 `b5673d17…` (compagnons et fichiers d'heures justes :
  21:45:51–21:56:41 et 20:43:13–20:54:02 UTC) ; lanceur v6 `50f9c496…` ; essais complémentaires `3594c401…`, journal
  `8d865a25…`, mutations v2 `fbc9e3ff…`, journal `723ab372…` (sept compagnons justes) ; T2 `d2944654…` ; script de
  scellement v3 `aee63b20…`. Les douze empreintes pleines que l'écart ajoute sont toutes retrouvées. Noyau : `boucle.py`
  `8b594096…` ; empreintes « blob » `c50d30a` (`boucle.py`), `3ad4c18` (`cli.py`), `042732e` (essais de la reprise),
  celles de `8e5e2f7b` qu'a relevées la contre-lecture 3 ; empreinte d'arbre `61ddd638…` écrite par le lanceur dans les
  `LANCEMENT.md` de la série v9.
- **Fichier d'empreintes des pièces** `EMPREINTES-pieces-pilote4-v5.txt` (`ed723f7c…`, compagnon juste) : 362 lignes sur
  362 justes, avant et après mon essai ; il couvre toutes les pièces du dossier et de ses sous-dossiers, sauf lui-même et
  son compagnon. **Pièces de la contre-lecture 3** : les 45 fichiers de `EMPREINTES-v1.txt` (`16be85c3…`, compagnon juste)
  sont tous là — 21 recopiés, 22 dans les deux archives (empreintes au fil justes ; archives conformes à leurs
  compagnons), et le rapport avec son compagnon sous `prereg/contre-lectures/`.
- **Batterie v8.** Redérivée de la v7 (`rederive/essais_lanceur_pilote4_v8-rederive.sh`), identique octet pour octet.
  Chaque cas nouveau vise sa garde, les gardes antérieures passant : `seg-sans-manifeste` → l. 208 (dossier et
  `LANCEMENT.md` présents, course non fermée) ; `seg-verrou-segment1-absent` → l. 209 (manifeste remis) ;
  `seg-autre-course-du-nom` → l. 211–213 (marqueur juste) ; `seg-etat-autre-arret` et `seg-etat-autre-segment` →
  l. 262 et 263 (état rescellé, donc compagnon juste à l. 260 ; ordre, lanceur, `HEAD` et verrou du segment passent) ;
  `seg-v53-reprises-mal-numerotees` → l. 341, second membre seul (arrêts justes, reprises `[3]` au lieu de `[2]`,
  empreintes refaites) ; le lanceur muté → l. 770. Artefacts retirés : manifeste et verrou remis par `mv`, dossier de
  l'autre course effacé, état et compagnon remis par `cp -p`, puis `seg-etat-restaure` (`4825869c…` = compagnon
  sauvegardé) ; le segment 2 sain qui suit relit `etat-v1.json` sous la même empreinte (`LANCEMENT.md` l. 175) et ferme la
  course. Le cas du lanceur muté vient en dernier, dans son propre dossier, avec son texte et sa ligne de GO d'essai
  (l'empreinte du lanceur muté y est citée) ; `LANCEUR` est remis ensuite. Les refus par `refus_tot` n'écrivent rien au
  `LANCEMENT.md` (l. 45) ; ceux par `refus` y laissent leur essai numéroté et retirent le verrou du segment (l. 225),
  comme on le lit pour les essais 4 et 5 du segment 2.
- **Série v9.** 228 cas sur 228, aucun échec ; noms et ordre : ceux de la série v8, plus les dix nouveaux aux places
  attendues ; une fois les chemins de travail remplacés, les deux journaux ne diffèrent que par ces dix lignes, lignes
  `RELEVÉ` comprises ; dépôts d'essai propres à la fin (`da3ca33`, `b7085ca`). Lanceur muté : `STOP` posé à 21:56:40 UTC,
  au départ du segment 2 ; refus du noyau « reprise : le fichier STOP est encore dans la course (le lanceur le retire
  avant la reprise) » (`boucle.py` l. 1031–1032), code 9, lanceur rendant 3 ; le cas sain `seg3-segment2`, à la même
  échéance nulle, reprend. Ce cas dépend d'une course entre le minuteur et le démarrage du noyau ; s'il la perdait, il
  échouerait (« segment 2 arrêté par STOP » au lieu du refus), il ne passerait jamais à tort.
- **Essais complémentaires du noyau.** Neuf cas : trois sains (reprise acceptée, dernier événement « reprise »,
  segment 2) et six artefacts, chacun refusé par sa garde avec son motif propre (« le dernier événement de la course n'est
  pas l'arrêt sur STOP de l'état » ; « ronde de génération en cours incohérente avec l'état », ses deux membres ; « vue
  figée de la ronde en cours introuvable », trois variantes : chemin absent, dossier hors de l'espace, vide), rien
  d'écrit (`_refus`). Le cas du dernier événement garde le nombre d'événements, donc la garde du nombre (l. 1035–1036) ne
  joue pas avant elle. Ces neuf cas couvrent exactement les trois refus de `reprendre()` sans artefact dans
  `tests/test_reprise_segments.py` (les autres motifs y sont : « noyau neuf », « aucun état », « compagnon »,
  « version », « arrêt sur STOP », « STOP est encore », « une seule reprise par état », manifeste, archive, paramètres,
  crédit, plafond, ronde illisible, ronde de conception incohérente, organisme hors de la course ou introuvable).
  Mutations v2 : chaque garde remplacée par `if False:` à partir d'un texte présent une seule fois dans `boucle.py`
  (l. 1038, 1063, 1067), essais filtrés à la garde, détectées (1, 2 et 3 échecs ; le cas sain passe chaque fois) ; copie
  saine 9 sur 9 ; cause de l'essai d'installation v1 plausible (`appels.py` charge le collisionneur voisin, l. 32–44).
- **Texte.** Les six marqueurs, une fois chacun (l. 8, 367, 372, 373, 569, 625) ; une seule ligne « entropie E = », deux
  lignes de graine, celles des marqueurs (ce que vérifie `sceller_pilote4_v3.py`) ; ligne de GO inchangée, chevrons
  simples à dessein. Table de correspondance, bornes, plan et liste d'arrêt disent la même chose des segments, de la
  porte, des 75 USD et du canal (d) ; les noms d'essais cités par la liste d'arrêt existent dans la série v9 ou dans les
  essais du noyau.
- **Deux décisions chez Lazar.** Objet de la seconde course : v6.1 nommée et acceptée (texte entier) ; seule la v5.3 (la
  phrase du critère 3 le dit désormais, l. 113 ; le canal (d) garde le retour arrière de la v5.3, la mutation de la v6.1 est
  sans objet) ; une v6.x plus tard sous un texte à part : même lecture que le cas précédent. Lecture si la confrontation
  change un seuil : les scores restent fermés sauf décision inscrite (l. 382–384), et « personne ne compte les rôles …
  avant ce moment » tient aussi longtemps. Le texte tient dans chaque cas.

# Rejeu des fichiers d'essais en échec avant l'étape 1 du papier dopamine — v1 (2026-11-21T17:13:36Z, `date -u`)

Classe C (travail). Mot de Lazar GO-2026-11-21-63 ; registre R-4581. Développeur Opus 5.5 de la nouvelle mère. Aucun commit, aucune correction, aucune machine. Cloisonnement : pour les fichiers qui touchent l'expérience sur les traits du texte (T0.6) ou les bras 7a, 7b, seuls des comptes et des noms de fichiers figurent ici.

## Verdict

Le bras « papier dopamine » n'introduit aucun échec : les sept fichiers donnent 46 échecs, 277 passés, 3 sautés, avec les **mêmes identifiants d'échec à l'octet** sur main avant la fusion du bras, sur la tête de la branche du bras et sur main d'aujourd'hui. Réserve : le bras apparaît dans le texte de trois échecs préexistants (voir § 4). Du point de vue des essais, l'étape 1 peut être lancée.

## 1. Où est la liste des sept fichiers

Ni R-4581 ni l'état du lancement (`docs/notes/papier-dopamine-moniteur-v1/exploratoire/etat-lancement-etape-1-v1.md`) ni le rapport du code ne la donnent ; la sortie du développeur précédent (`suite-groupe-3.txt`, dans le bloc-notes de son compte) n'est ni sur cette machine ni sur les branches `prep/dopamine-exploratoire-v1` et `claude/sharp-ramanujan-eks887`. **Liste reconstruite** : les 328 fichiers `tests/test_*.py` du commit du développeur (`f2c9d421b`, liste identique à `d6cde6667` et à la fusion `a52731b94`), en ordre de collecte, répartis un sur quatre ; le groupe 3 est celui des rangs 3, 7, 11… (82 fichiers, 2 710 essais collectés). Rejoué une fois à `f2c9d421b` (16:07:38Z–16:57:37Z, `--basetemp` à part) : **46 échecs, 2 349 passés, 315 sautés**, contre 47 et 2 348 au relevé du développeur, même total de 2 395 ; les échecs tombent dans exactement sept fichiers. Les autres découpes essayées (quarts alphabétiques par fichiers, quarts par nombre d'essais) ne donnent ni ce total ni ce compte. L'écart d'un essai (un échec chez le développeur, un succès ici) n'est pas identifiable sans sa sortie : instabilité probable (horloge, dossiers temporaires partagés de sa première passe) ; il ne change pas le verdict, puisque la comparaison décisive est faite fichier par fichier ci-dessous.

## 2. Rejeu des sept fichiers seuls

Commande, dans chaque arbre détaché : `PYTHONPATH=src python -m pytest -q -rf -p no:cacheprovider --basetemp=<dossier à part> <sept fichiers>`, environnement neuf (`requirements-cpu.txt`).

| arbre | commit | résultat |
|---|---|---|
| main avant la fusion du bras (premier parent de la fusion `a52731b94`) | `e071d0430717` | 46 échecs, 277 passés, 3 sautés |
| tête de `prep/dopamine-exploratoire-v1` | `d6cde6667b78` | 46 échecs, 277 passés, 3 sautés |
| `origin/main` à 17:03Z (bras fusionné) | `c8c6d2aa3d6d` | 46 échecs, 277 passés, 3 sautés |

Listes d'identifiants d'échec triées : identiques entre les trois arbres et identiques au rejeu du groupe 3 (§ 1). La fusion n'ajoute que 24 fichiers neufs (paquet `src/controle_ia/dopamine_exploratoire/`, neuf fichiers `tests/test_dopamine_exploratoire_*`, deux notes) et ne modifie aucun fichier existant (`git diff --name-status e071d0430 a52731b94` : 24 `A`, aucun `M`).

## 3. Table par fichier

| fichier d'essais | échecs (les trois arbres) | classement | cause |
|---|---|---|---|
| `tests/test_t06_v12_amorce.py` | 32 | préexistant | essais datés de T0.6 : GO figé échu le 16 novembre (R-4267) ; tous dans la liste des échecs attendus |
| `tests/test_t06_scripts.py` | 8 | préexistant | même cause, liste des échecs attendus |
| `tests/test_t06_v11_liste.py` | 1 | préexistant | inventaire figé des fichiers d'essais, dépassé par les fichiers neufs (même note) |
| `tests/test_t06_v12_liste.py` | 1 | préexistant | même cause |
| `tests/test_cibles_invisibles_v3.py` | 2 | préexistant | inventaires du dépôt (cause non affichée, cloisonnement) ; échoue déjà avant la fusion |
| `tests/test_mots_et_cout_bras_a_v1.py` | 1 | préexistant | cause non affichée (cloisonnement) ; dépend de l'état des registres, à voir par un lecteur habilité |
| `tests/test_lancer_course_ideation_conception_propre_v2.py` | 1 | préexistant, environnement | `test_pieces_sain_depot_reel` refuse tout dépôt hors de `/home/user/controle-ia-travail` (arbre détaché ailleurs) ; sans lien avec le bras |
| **total** | **46** | | |

Contrôle par programme : `scripts/comparer_echecs_attendus_v1.py docs/notes/essais-dates-t06-v1/echecs-attendus-dates-v1.md` sur la sortie de la branche du bras : 42 échecs vus figurent parmi les 178 attendus ; les 4 « neufs » pour cette liste sont ceux des trois derniers fichiers, présents avant la fusion.

## 4. Réserve : le bras dans le texte d'échecs préexistants

Comptes seulement. Sur les arbres qui portent le bras (branche et main), et pas sur main avant la fusion :
- deux échecs datés, un de `tests/test_t06_scripts.py` et un de `tests/test_t06_v12_amorce.py`, citent les neuf fichiers `tests/test_dopamine_exploratoire_*` dans une ligne d'erreur (une liste des fichiers d'essais du dépôt) : même phénomène que les inventaires figés dépassés, sans effet tant que ces essais restent datés ;
- un échec de `tests/test_cibles_invisibles_v3.py` (inventaire des constructeurs d'invite) cite un module du paquet `dopamine_exploratoire` parmi ses fautifs : le bras **s'ajoute** à un inventaire déjà en échec. Si les fautifs antérieurs sont réglés, cet essai restera en échec à cause du bras tant que son constructeur d'invite n'est pas examiné ou exclu par un texte versionné neuf. Ce n'est pas un obstacle au lancement (l'essai garde une autre expérience), mais c'est à consigner et à régler par une décision de la mère.

## 5. Pièces de travail (bloc-notes, non versées)

Sorties brutes et listes d'identifiants : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/rejeu/` (`sortie-dev-groupe3-rr.txt`, `sortie-avant-sept.txt`, `sortie-bras-sept.txt`, `sortie-main-sept.txt`, `echecs-*-ids.txt`, `sept-fichiers.txt`, `groupe3-rr.txt`, `compte-par-fichier.txt`). Elles contiennent des extraits d'essais de T0.6 : à ne pas verser sans relecture de cloisonnement. Arbres de travail retirés à la fin. Pendant le rejeu, le disque est tombé à 2,5 Go libres (autres sessions) ; trois arbres inactifs ont été retirés puis recréés un à un.

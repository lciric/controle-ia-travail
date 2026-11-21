# Vérification hostile du gardien v3 de l'essai court — palier 0b — v1

**Verdict : Conforme, avec une réserve non bloquante.** Les deux corrections de l'erratum 2 sont portées à la lettre et la v3 ne casse aucun des cinq modes examinés. Réserve : la preuve de gel est de deux relevés à une seconde d'écart ; un orphelin non relevé qui écrit moins d'une fois par seconde la passe (démontré), si bien que « figé » reste « figé tant qu'aucun écrivain inconnu n'écrit dans la fenêtre d'une seconde ». C'est ce que l'erratum demande ; le rapport de l'auteur gagnerait à le dire (il écrit « signalé par NON figé s'il écrit encore pendant la mesure »).

Pièces (sha256 relevés) : erratum 2 `68faf068…3848` (égal à l'attendue) ; gardien v3 `d8fd650b…b4c7` ; départ du gardien v3 `97586b7b…e428` ; lanceur v2 `4c96c703…13f3` et départ v2 `2ec06e95…0e38`, inchangés (mêmes empreintes que dans ma vérification de la v2, donc le mode 4 de la v2 vaut encore). Dossier d'essai : sous-dossier `v3/` de mon dossier (scripts `s3.sh`, `decoy3.sh`, factices dans `v3/pieces/` et `v3/pieces-lent/`, sorties sous `v3/e/`).

## (a) Les deux corrections

| # | Correction de l'erratum 2 | Portée ? | Passage et preuve |
|---|---|---|---|
| 1 | Le gardien ne part pas tant qu'un descendant relevé vit | **Portée** | `gardien-essai-court-v3.py` l. 580 (`controles` ne rend la main que si le processus lancé est absent *et* sans descendant relevé), l. 449-462 et 470-477 (mode « descendants » : exige que le processus lancé ait été vu confirmé, `chef_confirme` l. 249/314, et qu'il soit absent), l. 604-633 (`garder` ne rend 0 qu'une fois tous absents). Mon cas `scen-chef-tue` rejoué : chef tué, descendant vivant, le gardien reste, écrit « la garde continue sur eux » ; **sain** (`chef-tue-sain`, descendant qui finit seul en 8 s) : gardien parti à 9 s, aucun `arret-gardien.txt`, témoin sans lien vivant ; **artefact** (`chef-tue-place`, seuil de place factice posé 35 Mo sous la place libre, descendant écrivant 20 Mo/s) : « arrêt de place », « arrêt des descendants relevés », signal de fin au groupe qui porte encore le descendant, tous absents en 0,2 s, témoin vivant ; **sourd hors groupe** (`chef-tue-sourd`, seuil n) : SIGTERM puis SIGKILL par identifiant au délai, tous absents, témoin vivant. |
| 2 | « Dossier figé » prouvé par deux relevés égaux, sinon « NON figé » | **Portée** | `figer` l. 524-533 (jusqu'à dix paires à 1 s), `mesure` l. 535-569 (état du dossier avec les deux relevés, lignes de projection préfixées « [dossier NON figé] » si inégaux). Mon cas du petit-enfant détaché rejoué (`orphelin`, il écrit toutes les 0,2 s) : « dossier NON figé : 10 paires… toutes inégales », deux derniers relevés n 55 puis 60, projection marquée ; l'orphelin vivait encore, n 68 puis 83 ensuite. Dossier réellement figé (`rapide`, `sourd-groupe`, `sourd-hors`, `chef-tue-sourd`) : « figé… paire 1 », n égal au nombre de fichiers réels (849 = 849). |

## (b) Les cinq modes

| # | Mode d'échec | Rendu | Pas visé | Preuve |
|---|---|---|---|---|
| 1 | signaler un autre processus | **Tenu** | l. 274-291, 449-462, 346-355 | `decoy3.sh` : heure décalée −7 ou fichier d'heure absent : aucun signal, témoin vivant ; heure exacte : signal. Le mode « descendants » exige `chef_confirme` : un chef jamais vu confirmé (cas des fichiers périmés) ne l'ouvre pas, et chaque signal par identifiant relit l'heure de départ (l. 348-350). Le témoin sans lien reste vivant dans trois scénarios. |
| 2 | laisser vivre le programme ou un descendant | **Tenu** (le trou de la v2 est fermé) | l. 580, 604-633 | `chef-tue-place`, `chef-tue-sourd`, `sourd-groupe` (arrêt forcé du groupe, membre sourd arrêté), `sourd-hors` : plus aucun descendant relevé ne survit à un arrêt. Limite inchangée : un descendant jamais relevé (orphelin né entre deux relevés) n'est pas signalé. Observation lue, non rejouée : programme fini normalement avec un descendant détaché relevé encore vivant, n déjà ≥ seuil : le gardien reste et applique alors l'arrêt de mesure (l. 580, 589) ; il écrirait un fichier de mesure après la fin normale et, si ce descendant ne finit jamais, ne partirait pas ; sans effet sur les modes, à savoir au réveil. |
| 3 | supprimer, modifier, décider sur le contenu | **Tenu** | écritures inchangées : l. 225, 265, 407, 565, toutes dans la tenue (`"a"` ou `"x"`) | Lecture du diff de fond : `figer` et `releve_etape_4` ne font que `lstat`, `scandir` et `os.lstat` (l. 513-518). Aucun nouvel appel de suppression ni de renommage ; la décision « figé » ne dépend que de nombres et de tailles. |
| 4 | commande différente à l'octet | **Tenu** | lanceur v2 l. 98, inchangé | Empreintes du lanceur et du départ v2 égales à celles que j'avais vérifiées (la v3 ne les touche pas) ; le départ du gardien v3 ne change que le nom du gardien lancé (l. 19). |
| 5 | projection fausse ou sur dossier non figé sans le dire | **Tenu** dans la lettre de l'erratum ; réserve démontrée | l. 524-533, 548-563 | La réserve de la v2 (« figé » affirmé sans preuve) est levée pour tout écrivain qui écrit dans la fenêtre d'une seconde (`orphelin` : NON figé). Réserve restante, démontrée : `orphelin-lent` (écrivain orphelin, un dossier toutes les 3 s) : « dossier figé… paire 1 », n 9, alors que le processus 12420 continuait (n passé à 10 ensuite). Même défaut que la v2 pour les seuls écrivains lents ; ce qui le lèverait : une fenêtre plus longue que la période de l'écrivain le plus lent, ou la liste de tous les processus qui ont le dossier ouvert (hors du mandat). Formule : `t_arrêt` pris à l'envoi (l. 464), n et s4 du dernier relevé (l. 539), projections inchangées (essais de la v2 relus : mêmes fonctions l. 189-212). |

## Relevé de méthode

**Chaîne de raisonnement.**
1. Lecture de l'erratum 2 (`68faf068…3848`), du gardien v3 en entier, du départ du gardien v3 ; empreintes relevées ; le lanceur et le départ de la v2 ont les empreintes déjà vérifiées.
2. Correction 1 : lecture de `controles`, `arreter`, `garder` ; essais `chef-tue-sain`, `chef-tue-place`, `chef-tue-sourd` avec témoin sans lien ; résultats ci-dessus.
3. Correction 2 : lecture de `figer` et `mesure` ; essais `orphelin` (NON figé), `rapide` et trois autres (figé, n égal au nombre réel de fichiers).
4. Mode 1 : `decoy3.sh` trois valeurs ; lecture de la condition d'ouverture du mode « descendants ».
5. Mode 2 : trois essais chef tué, deux essais de régression (`sourd-groupe`, `sourd-hors`).
6. Modes 3 et 4 : lecture du diff de fond et empreintes inchangées.
7. Mode 5 : essai `orphelin-lent` (écrivain à 3 s de période) ; « figé » affirmé à tort.
8. Supposé : comportement du vrai programme et de ses scripts ; cas « fin normale avec descendant détaché » lu, non joué.

**Objets de contrôle.**
- Correction 1 : faux par construction (chef tué, descendant qui écrit, place factice franchie) → attendu arrêt du descendant, rendu arrêt ; vrai par construction (descendant qui finit seul ; témoin sans lien) → attendu aucun signal, rendu aucun signal.
- Correction 2 : faux par construction (orphelin qui écrit toutes les 0,2 s) → attendu « NON figé », rendu « NON figé » ; vrai (programme arrêté, rien n'écrit) → attendu « figé », rendu « figé ». Cas où le mécanisme devait échouer (écrivain à 3 s de période) → il échoue (« figé » à tort) : défaut démontré, de la fenêtre et non du code.
- Garde d'identité : faux (fichiers périmés, fichier d'heure absent) → aucun signal ; vrai (heure exacte) → signal.

**Premier pas non justifié.** Pas 8 : comportement réel du programme au signal de fin et forme de ses descendants ; ce qui le justifierait : un essai du vrai programme sur un dossier jetable, hors de mon permis.

**Mode d'échec affecté.** Réponse à la question : (a) correction 1 portée, correction 2 portée ; (b) mode 1 tenu, mode 2 tenu, mode 3 tenu, mode 4 tenu, mode 5 tenu à la lettre avec réserve sur les écrivains lents (l. 524-533). Preuves : `s3.sh` (cas `chef-tue-*`, `orphelin`, `orphelin-lent`, `rapide`, `sourd-*`), `decoy3.sh`.

**Dérivation de l'énoncé seul.** Sans objet : je suis vérificateur.

**Trouvaille de côté.** (a) La mesure dure maintenant au moins 1 s et jusqu'à 10 s de plus sans ligne de minute (écrit au rapport de l'auteur). (b) Dans `orphelin`, le gardien avait relevé le parent éphémère puis perdu l'orphelin, comme prévu par la limite écrite.

**Évaluateur et conseil.** Ce qui juge mon produit : la session, puis mes essais sur factices à vrai et faux construits. Mon verdict pourrait être bon sans le mériter : factices simples, scripts écrits par moi, intervalle d'une seconde, aucun essai du vrai programme ; je n'ai pas rejoué toute la suite de l'auteur (lanceur, refus de départ, projections), seulement les cas touchés par les deux corrections et les régressions des modes 1, 2 et 5. Aucune écriture hors de mon dossier ; aucun vrai programme ; aucun commit ; aucune dépense ; processus arrêtés : mes factices seulement, par identifiant.

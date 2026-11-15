# Vérification du seul différentiel v11 → v12 de la procédure du pilote MR-2 (sans ssh) et de ses programmes — v1

- **Lecteur** : sous-agent neuf, qui n'a écrit aucune version de la procédure du pilote ni aucune de ses vérifications. Heure d'écriture : 2026-11-15T12:17:23Z (`date -u`).
- **Lu à** : commit `85a84ff5daf3c6df4bc0e13c2444eeb51b8d05db` de `lot/compte-organisme-v1` (v11 au commit `c93287d4`), par `git show` et `git diff` ; seul le dossier `sans-ssh-v2/` a été extrait, dans le bloc-notes de la session. Décisions lues : R-2894, R-2898.
- **Rien de payant** : aucun appel à un fournisseur ni au loueur, aucune machine, aucun réseau dans les essais, aucune valeur de clé lue ni affichée, aucun commit, aucune poussée.
- **Un refus pendant ce travail, dit ici** : une commande de complément du lecteur (recherche des chemins de l'outil qui laissent la liste privée sur le disque) a été refusée en entier par le contrôle intégré des suppressions de l'outil de la session du lecteur (elle portait, après un changement de dossier, un nettoyage par chemin relatif d'un sous-dossier du bloc-notes). Elle n'a pas été rejouée, sous aucune forme, par aucun outil : le point n5 ne repose donc que sur la lecture du code. Conséquence : **aucune suppression n'a été faite dans le bloc-notes** ; le dossier extrait et les dossiers jetables des essais y restent (section 8). Aucun refus du crochet du dépôt ni d'un classifieur.

## Verdict

**Jouable après corrections.** Zéro point bloquant qui demande une version nouvelle ou une pièce nouvelle : le différentiel est celui qui est déclaré, les majeurs M1 à M4 sont fermés dans le code, M5 est écrit, les essais rejoués sont conformes (36 sur 36, 17 sur 17). **Une correction obligatoire avant la création, par une consigne écrite d'une ligne, sans toucher aux pièces scellées (N1)** ; deux conditions qui appartiennent à la mère (C1, C2) ; onze mineurs.

| n° | en une ligne |
|---|---|
| **N1** (majeur, argent) | `relire` accepte encore un prix relu jusqu'à 0,20 USD/h, alors que l'échéance est passée à 17 h : 17 h × 0,20 = 3,40 USD, au-dessus de la part machine de 3 USD ; la borne de 2,55 USD ne tient que par le prix de l'offre. |
| **C1** (condition, M5) | La lecture de la mère sur la présence des clés (au plus 17 h, au-delà de la fin de l'autonomie) doit être consignée et dite à Lazar **avant** l'impression de la commande ; elle doit dire qui joue la section 11 à l'échéance, puisque l'échéance tombe après la fin de l'autonomie. |
| **C2** (condition, m1) | La création n'est jouée que sous la forme exacte de la section 2, point 7 (le texte des deux lignes dans la commande elle-même) : c'est cette forme que le crochet laisse passer en la voyant (section 3). |

## 0. Empreintes (toutes recalculées, toutes égales à leur compagnon)

| pièce | empreinte |
|---|---|
| `procedure-pilote-mr2-v74-machine-v11.md` | `b3ce90145bb27323336a7b2ef0f942877b30bda149966ff687b773078e5c7c4d` |
| `procedure-pilote-mr2-v74-machine-v12.md` | `d0d2c8e11b26037fe9188cac4e8a845737b1f1f8e254a7537c8009f08110689a` |
| `sans-ssh-v2/amorce_pilote_mr2_v74_v2.sh` | `93b9c50de967c3da15e21d526ed0123660b6ca5ca0917f0c8d9f838379871bc6` |
| `sans-ssh-v2/machine_pilote_mr2_v74_v2.sh` | `4fa7d368331205346d90599ecc61a489290dd5a1b0aa506c0fd1055ad74ec0f5` |
| `sans-ssh-v2/machine_pilote_mr2_v74_v2.py` | `8af383f9e894256bfab1691405b1538bfa0b06c5d9b165a63e6480c110ce3c3f` |
| `sans-ssh-v2/session_pilote_mr2_v74_v2.sh` | `7e66e421d5dea8607cf5673d775eea585041b7abfff724927dbd34180eed833d` |
| `sans-ssh-v2/session_pilote_mr2_v74_v2.py` | `2455b3de5073485a92038a43abfcdfb8ea8f894bd9cb1f5fe0de77866d9cd599` |
| `sans-ssh-v2/essais/` : notice `02d44a9d…`, banc de l'amorce `665da203…`, banc de l'outil `b5dd9934…`, doublure du lanceur `360fbab2…` et doublure du loueur `42195553…` (**les mêmes qu'en v1**), résultats `eb3b231e…`, `29bdf722…`, `91ea5077…` | égaux |
| pièces `sans-ssh-v1/` (treize fichiers) | égales à leurs compagnons, inchangées |
| vérification de la v11, sur `main` | `43a4347bc09fbab59a80e4cac6a682d9e0edf2bb535b580f50930b3c189eee71` |
| crochet `.claude/hooks/garde_calcul.py` de `main`, tel qu'éprouvé | `73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850` |

Le commit `85a84ff5` n'ajoute que des fichiers (30, dont le journal provisoire v28) ; il ne modifie ni ne retire aucun fichier du commit `c93287d4`.

## 1. Différentiel exact, comparé à la section 12 nonies

**Procédure** (`diff` v11 → v12 : 330 lignes de différentiel). Chaque ligne retirée ou changée de la v11 a été rapprochée d'une ligne de la table 12 nonies. **Tous les changements déclarés sont présents, retraits compris** : M1 (2.9, 11), M2 (0, 2.9, 11 ; retrait de « passer à l'étape 3 »), M3 (0, 10), M4 (0, 9 ; retrait de l'état « fini, poussee finale en echec »), M5 (0), m1 (2.6, 2.7), essai de poussée et disque réel (2.5), m2, m3, m4 (6), m5 et m6 (5, 10), m7 (7), m8 (2.10 rétabli ; 2.9), m9 (en-tête), m10 (0), m11 (0, 10), m13, m14 (0), pièces et dossier d'envoi (en-tête, 0, 1). Les sections 3, 4, 6 (hors barrière 3), 8 et la table 12 octies sont identiques à l'octet.

**Changements présents dans le texte et absents de la table** (aucun ne change une commande du lanceur ni un attendu ; mineur n2) :
- (a) v12 l. 98-99, **conduite neuve** : « Un état poussé qui ne bouge plus pendant 40 minutes hors de `jouer` : lire `vastai logs ID` ; ne pas détruire avant l'échéance sans le mot de la mère ». Elle voisine deux consignes de destruction sans attendre (l. 108-110, arrêt côté session ; l. 275-277, branche de sortie absente à 20 minutes) : dire laquelle prime.
- (b) v12 l. 318 : « lecture confirmée par la mère (option (a), R-2898) » remplace « lecture à confirmer par la mère (…) c'est un nœud de Lazar avant toute location » ; dit à l'en-tête (l. 10), absent de la table.
- (c) v12 l. 524-528, « Non éprouvés » : retrait de « éprouvée par B bis » (autodestruction) et de « éprouvé par B bis et Neuron Lens » (clonage par jeton) ; ajout de l'offre à 0,15 USD/h.
- (d) v12 l. 131-133 : retrait de « l'absence est prouvée par la session, section 11 », remplacée par la consigne plus forte de M2.
- (e) v12 l. 134-135 : « (à 0,15 USD/h, il tomberait après l'échéance) » : le nœud des 2,70 USD ne peut plus tomber au prix de l'offre (voir N1).
- (f) **Texte resté de la v11 alors que le code a changé** : v12 l. 265, « échéance dans les 14 h 45 » ; l'amorce v2 admet 17 h 05 (amorce l. 30, l. 84). Mineur n1.

**Programmes** (`diff` de chaque paire v1 → v2) :

| pièce | changements trouvés | déclarés |
|---|---|---|
| amorce | noms v2, dossier `sans-ssh-v2`, borne de l'échéance 53 100 → 61 500 s (l. 30, l. 84) ; **rien d'autre** : minuterie, refus avant la minuterie, relance du conteneur à l'octet | oui (m3) |
| programme machine `.sh` | `PAS_REPRISE` (300 s) et `POUSSEE_OK` (l. 49-50, 86, 112) ; `attente_finale` reprend la poussée tant qu'elle a échoué, puis efface les clés (l. 116-125) ; branche de sortie présente au départ : jamais de poussée (l. 180) ; retrait de l'état « fini, poussee finale en echec » (l. 350) ; en-tête (m7) ; **rien d'autre** : sections 3 à 11, garde des 12 h 30 (l. 47, l. 277), délais des feux (l. 43-44), arguments de `jouer` à l'octet | oui (M4, m7) ; deux suites non dites : l. 180 vaut aussi pour « dépôt injoignable » au départ ; l. 183, une première poussée en échec est désormais reprise elle aussi (l'état reste « mise en place ») |
| aide de la machine `.py` | balayage : secret en hexadécimal majuscule, phrase en base64 (l. 254-259) ; **rien d'autre** | oui (m10) |
| outil de la session `.sh` | amorce encodée dans un fichier privé, lignes écrites dans `commande-creation.txt` (l. 113-121) ; `comparer` (l. 123-127) ; `essai-poussee` (l. 128-132) ; clé publique de 4096 bits exigée (l. 171-172) ; fichier de la phrase effacé avant le jugement de la poussée (l. 181-183) ; `aide cause` avant toute écriture (l. 203, l. 208), retrait de la coupe à 200 octets ; `detruire` par `aide etiquette`, retrait du refus « existe déjà » (l. 217-228) ; `verifier-destruction` avec repli (l. 229-235) | oui (M1, M2, M3, m1, m5, m6) |
| aide de l'outil `.py` | `PRIX_OFFRE_MAX` 0,15 pour l'offre et l'échéance, `DUREE_S` 61 200 (l. 15-18, 89, 101-103) ; prix du réseau imprimés (l. 93-94) ; `c_etiquette` (l. 138-150) ; note de `c_absence` (l. 191-193) ; `c_cause` (l. 211-216) ; liste des intouchables réduite de deux identifiants (l. 21) ; **`PRIX_MAX` de la relecture resté à 0,20** (l. 15, l. 131) | oui, sauf la conséquence de la dernière ligne : N1 |
| bancs | dépôt donné par `ESSAI_DEPOT`, pièces du lot par `git show` ; crochet de réception du dépôt nu qui refuse sur drapeau ; scénario « poussee-finale-reprise » ; douze cas de plus pour l'outil ; cause du feu d'arrêt du banc sans accent | oui (m12) |

Je n'ai trouvé aucun autre changement.

## 2. M1 à M5

- **M1 — fermé dans le code.** `detruire` n'appelle plus `relire` : `aide etiquette` ne lit que la présence et l'étiquette (outil l. 221 ; aide l. 138-150). Éprouvé par le lecteur sur une doublure du loueur : prix relu 0,31 USD/h, puis prix absent → `relire` rend le code 2 (« la détruire aussitôt »), `detruire` rend le code 0 et imprime la ligne de destruction par le seul identifiant relu du fichier, avec `-y` ; étiquette autre → code 2, aucune ligne ; destruction recommencée → inventaire de référence gardé, ligne imprimée de nouveau.
- **M2 — fermé dans le code pour la preuve, par consigne pour l'échéance.** Témoin écrit à la création : `ids-apres-creation.txt` (v12 l. 252-253), pris en repli par `verifier-destruction` (outil l. 231-232). Éprouvé : instance déjà absente, aucun inventaire avant destruction → `verifier-destruction` rend 0 sur le repli (« absente ; témoins toujours listés : 2 ») ; `detruire` rend 0 sans ligne de destruction, écrit l'inventaire et renvoie à l'étape 3, qui rend 0 ; un témoin de la création disparu → code 2 (« absence non prouvée »). La section 11 est commandée à l'échéance en deux endroits (v12 l. 132-133 et l. 439-440 : « cinq minutes après l'échéance au plus tard, la session joue cette section sans attendre aucun mot ») ; rien dans un programme ne peut le forcer : voir C1.
- **M3 — fermé dans le code.** `aide cause` (aide l. 211-216 : lettres sans accent, chiffres, espace et « , . : ; ( ) _ - », 1 à 100 caractères, comparaison entière) est jouée **avant** la création de tout fichier de feu (outil l. 203, l. 208). Éprouvé sur l'aide : cause accentuée, cause de 101 caractères, cause portant « = » → code 2 (le banc montre que rien n'est alors poussé) ; quatre causes admises par l'outil, dont une de 100 caractères, sont toutes lues « feu conforme » par l'aide de la machine. Les feux 1, 2, 3 sont écrits par programme à partir de valeurs déjà contrôlées.
- **M4 — fermé dans le code.** `attente_finale` (machine l. 116-125) : tant que la dernière poussée a échoué, une reprise toutes les 300 s (trois essais chacune), sans borne propre, donc jusqu'à la destruction ; les trois clés restent pour le balayage et ne sont effacées qu'après la poussée réussie (l. 123). Vaut pour « fini », l'arrêt (A), la machine gardée et la sortie inattendue (l. 136, 141, 142, 351). Scénario rejoué : dépôt qui refuse pendant 240 s, trois reprises au journal, puis « poussé (reprise 3 (fini)) », état `fini`, lecture rapatriée présente, 43 fichiers, aucune fuite.
- **M5 — écrit, presque exactement.** v12 l. 142-151 : configuration de l'instance chez le loueur de la création à la destruction (au plus 17 h), environnement du processus d'entrée, de la minuterie et de ses enfants, relais d'un `jouer` arrêté par son PID, variables du programme jusqu'à la dernière poussée réussie, liste des instances du compte ; écart à la lettre de la ligne d'autorisation du passage des clés dit ; fin de l'autonomie à 22:39Z et heure charnière de 05:39Z justes (22:39 − 17:00). **À compléter** (mineur n3) et **à consigner par la mère** (C1).

## 3. m1 — la forme de la création en une commande, et le crochet

**Forme** (section 2, point 7) : préambule de la section 0 ; copie des deux lignes imprimées dans `a-jouer.txt` par un document au délimiteur entre guillemets ; `comparer` (égalité à l'octet avec `commande-creation.txt`, outil l. 123-127) ; puis lecture du fichier comparé par l'interpréteur, dans la même commande. La seconde ligne ne porte plus l'amorce encodée (lue dans `amorce-v2.b64`, 0600, au moment du jeu) : 1 093 octets pour les deux lignes au lieu de 13 000 environ. Ce qui est joué est à l'octet ce qui a été comparé ; les valeurs des clés ne sont jamais dans le texte.

**Épreuve du crochet** : le programme du crochet de `main` a été appelé directement, six fois, sur des entrées factices lues dans des fichiers (les deux lignes y ont été construites par programme, à partir du gabarit des lignes 116-117 de l'outil v2 et de valeurs non secrètes factices ; aucune forme de création n'a été tapée dans une commande du lecteur).

| entrée factice | code du crochet | lecture |
|---|---|---|
| 1. forme exacte de la section 2, point 7, identifiant de la ligne de la part machine en tête de la seconde ligne | **0 (passe)** | cas sain |
| 2. la même, sans aucun identifiant de ligne | 2 (« lancement d'instance payante sans identifiant de GO ») | artefact : bloqué |
| 3. la même, identifiant inconnu du registre | 2 (« absent de registres/go.md ») | artefact : bloqué |
| 4. préfixe de tête retiré, l'identifiant restant dans la chaîne d'environnement | 0 | le crochet cherche l'identifiant n'importe où dans le texte, pas en tête de ligne |
| 5. `comparer` puis lecture du fichier, **sans** le texte des deux lignes dans la commande | 0 | le crochet ne voit pas ce qu'un fichier lu contient |
| 6. la forme exacte, avec l'identifiant de la ligne des crédits à la place | 0 | cette ligne est elle aussi de type « calcul », valide |

**Réponse : oui, le crochet laisse passer la forme de la section 2, point 7, avec l'identifiant de la ligne de la part machine** (ligne de type « calcul », accordée par Lazar, en cours de validité, sans révocation au registre de `main` tel qu'il est sur le disque). Aucun motif d'arrêt par nom n'est dans le texte. Deux réserves : (i) les entrées 4 et 5 montrent que la garde ne tient que si la forme est tenue telle qu'écrite (C2) : ne jamais jouer la lecture du fichier seule, ne jamais retirer le préfixe ; (ii) le crochet n'est pas le seul juge : les règles de permission et le classifieur de la session qui lance ne peuvent pas être éprouvés d'ici (les deux règles d'autorisation du réglage du dépôt portent sur d'autres commandes) ; un refus de leur part est un nœud, sans autre forme (v12 l. 246).

La ligne de destruction (section 11) n'est pas une forme de lancement pour le crochet : il la laisse passer avec ou sans identifiant.

## 4. m3 — offre, échéance, marge, délais

- **Offre à 0,15 USD/h au plus, disque réel compris** : tenue par programme (aide l. 16, l. 89, l. 101-102 ; la recherche demande 20 Go de stockage, v12 l. 215). Bonne mesure : elle ferme la cause de M1 (prix chiffré pour 5 Go).
- **Échéance à 17 h, 2,55 USD au plus** : 61 200 s (aide l. 18, l. 103) × 0,15 = 2,55 USD, exact ; l'amorce refuse au-delà de 17 h 05 (l. 30). Reste sous la part : 0,45 USD pour les frais de réseau et un retard de destruction. **Mais cette borne ne vaut qu'au prix de l'offre : N1.**
- **Marge avant la garde des 12 h 30** : 61 200 − 45 000 = 16 200 s, soit 4 h 30 depuis l'impression de la commande, exact (garde inchangée, machine l. 47, l. 277, rejouée avant la relance). Pire cas compté par le lecteur : création 10 min, départ de la machine 10, phrase 60 (comptée depuis le départ, mise en place comprise, machine l. 227), mondes 60 sur un hôte lent, feu des mondes 20, `preparer` et essai à blanc 10, feu réel 20, soit 3 h 10 : il reste 1 h 20 ; avec une relance (refus, 20 min de feu, contrôles), environ 55 min. La phrase « plus d'une heure, y compris pour une relance » (v12 l. 138-139) est juste sans relance, un peu large avec ; sans conséquence. Aux délais demandés à la mère, il reste entre 2 h 20 et 3 h 10.
- **Délais de réponse (phrase en 30 min, feux en 5 min)** : ce sont des cibles de prudence, non des bornes de la machine (qui gardent 60, 20, 20, 20 min). Avec 4 h 30 de marge, elles ne sont plus critiques ; je les juge bonnes. La seule attente qui dépend d'une personne est la phrase : le préavis doit obtenir que Lazar soit là dans l'heure qui suit le départ de la machine, sinon arrêt (A) (quelques centimes, mais le secret est perdu et la procédure ne se rejoue pas telle quelle : branches et échéance déjà prises, R12).
- **Coût de l'allongement** : les clés restent 2 h 20 de plus chez le loueur ; l'échéance tombe désormais après la fin de l'autonomie pour toute création d'aujourd'hui (C1) ; à 0,15 USD/h, le nœud des 2,70 USD ne tombe plus avant l'échéance (voir N1).

## 5. Majeur neuf

**N1 — La relecture du prix n'a pas suivi l'échéance.**
Où : `session_pilote_mr2_v74_v2.py` l. 15 (`PRIX_MAX = 0.20`) et l. 131 (`c_relire`) ; v12 l. 254-255 (« `relire` (étiquette, prix au plus 0,20 USD/h ; hors borne : détruire aussitôt ») ; v12 l. 128-131 (« soit 2,55 USD au plus pour la machine »).
Constat : une instance relue entre 0,15 et 0,20 USD/h est dite conforme ; à l'échéance de 17 h elle coûte jusqu'à 3,40 USD, au-dessus de la part machine de 3 USD (la v11 donnait 2,93 USD à 0,20). La borne mécanique de la v11 est donc perdue dans ce cas. Le filet qui reste est le nœud des 2,70 USD (v12 l. 134) : à 0,20 USD/h il tombe à 13 h 30, par l'horloge de la session, après la fin de l'autonomie et au milieu d'un `jouer` payé. Le cas est peu probable depuis que la recherche chiffre le disque réel, mais la relecture existe pour ce cas.
Correction par consigne (sans code) — ancien (v12 l. 254-255) : « `$OUTIL relire "$ETIQ"` (étiquette, prix au plus 0,20 USD/h ; hors borne : détruire aussitôt, section 11 » ; nouveau : la même phrase, plus « ; **si le prix imprimé par `relire` dépasse 0,17 USD/h (17 h × 0,17 = 2,89 USD) : détruire aussitôt, section 11, puis nœud** ». Correction par code, pour une version suivante : `PRIX_MAX` égal à `PRIX_OFFRE_MAX`, ou contrôle « prix relu × durée restante < part ».

## 6. Conditions de la mère

**C1 — Lecture de M5 et acteur à l'échéance.** v12 l. 148-151 écrit que, après 22:39Z, « seule la minuterie agit (…), puis la session ou Lazar » ; v12 l. 132-133 et l. 439-440 commandent à la session de jouer la section 11 cinq minutes après l'échéance « sans attendre aucun mot ». Pour une création faite aujourd'hui, l'échéance tombe le 16 novembre au matin, après la fin de l'autonomie : la fermeture de M2 repose alors sur un geste de la session hors de l'autonomie. Les deux phrases ne se contredisent pas (« puis la session »), mais elles laissent sans réponse ce que la session peut faire **entre** 22:39Z et l'échéance : lire l'état, donner un feu d'arrêt ou de relance, tenir les nœuds « une heure avant », récupérer la sortie, détruire après `fini`. À écrire par la mère dans sa lecture, et à dire à Lazar dans le préavis, avant l'impression de la commande (v12 l. 219-220).

**C2 — Tenue de la forme.** Section 3 ci-dessus, entrées 4 et 5.

## 7. Mineurs

- **n1** — v12 l. 265 : « échéance dans les 14 h 45 » ; l'amorce v2 dit 17 h 05. Ancien : « échéance dans les 14 h 45 » ; nouveau : « échéance dans les 17 h 05 ».
- **n2** — Écarts à déclarer à la section 12 nonies : les points (a) à (f) de la section 1 et les deux suites de M4 (machine l. 180 et l. 183). Pour (a), dire l'ordre : la branche de sortie absente à 20 minutes et l'arrêt qui doit être immédiat gardent la destruction sans attendre ; la phrase neuve ne vaut que pour un état déjà poussé.
- **n3** — Exposition des clés, deux lieux absents de v12 l. 142-151 : (i) sur la machine de la **session**, les valeurs sont développées par l'interpréteur dans les arguments du processus de création, le temps de l'appel (v12 l. 232-233) ; (ii) la demande de création passe par le mandataire HTTPS de la session (v12 l. 14) : s'il déchiffre, il en voit le corps. Les deux existaient en v11. De plus, « au plus 17 h » suppose la destruction faite à l'échéance, et ce que le loueur garde après elle n'est pas connu : proposer à Lazar le remplacement des trois clés et du jeton des machines après le pilote.
- **n4** — Fichier de la phrase : effacé « que la poussée ait réussi ou non » (outil l. 181), mais non après un refus qui précède la poussée (outil l. 156-175 : état, inscription, forme, clé publique) ; il reste alors dans le dossier d'envoi. Ancien (v12 l. 309) : « (m6 ; si elle a échoué : nœud, la phrase devra être redonnée) » ; nouveau : la même phrase, plus « ; après un refus de l'outil avant la poussée, si le feu n'est pas redonné aussitôt : `shred -u "$ENV/phrase.txt"` ».
- **n5** — `verifier-destruction` peut laisser la liste privée des instances sur le disque : l'aide lit l'identifiant et la référence **avant** de lire, donc de supprimer, la liste (aide l. 185-187) ; une référence ou un identifiant mal formé rend un refus sans suppression. **Lu dans le code, non éprouvé** (commande de complément refusée, en-tête). Cas rare (les deux fichiers sont écrits par l'outil). Indice : un dossier de ce type, daté de 10:31Z, donc d'un essai antérieur à ce travail, est resté dans `/tmp` (`/tmp/tmp.7mlcuUhIyI`, deux fichiers, 54 octets, non ouvert, non touché). Consigne : après tout refus « arguments ou fichier » de l'outil pendant que la machine vit, la mère cherche et efface les dossiers `tmp.*` de `/tmp` qui portent un `sortie.json`.
- **n6** — Instance déjà absente : `detruire` écrit sa référence d'après une liste lue **après** la disparition, et `verifier-destruction` la préfère au témoin de la création (outil l. 231) ; une liste tronquée lue deux fois de suite prouverait l'absence à tort. Consigne : dans ce cas, jouer `verifier-destruction` **avant** `detruire` (éprouvé : le repli sur le témoin de la création rend 0), et confirmer par la console du loueur si un doute reste.
- **n7** — Autres sessions du programme : le registre des arrêts montre deux instances créées puis détruites ce matin par une autre session. Une création ou une destruction faite par elle entre deux inventaires du pilote fait refuser `ajoute` ou `verifier-destruction` à tort (nœud, non faute, v12 l. 435-436). Consigne : la mère lui annonce les deux fenêtres (création, destruction). Le retrait des deux identifiants de la liste des intouchables est juste : le registre des arrêts les dit détruites, absence prouvée.
- **n8** — Phrases abîmées à la recopie, sans effet : v12 l. 89 (« une forme trouvée : un fichier où une forme est trouvée ») ; v12 l. 350-352 (parenthèse ouverte deux fois, jamais fermée).
- **n9** — Banc : la liste des états finaux du banc garde l'état retiré (banc de l’amorce l. 32), sans effet ; le scénario intégral scellé a été joué avant deux changements du banc (dit dans la notice).
- **n10** — La première poussée en échec est maintenant reprise (machine l. 183) : si elle finit par passer, la session voit un état « mise en place » qui ne bouge plus ; c'est le cas de la phrase neuve (a) ; le dire.
- **n11** — Après un arrêt qui précède le pilote réel, rien ne se rejoue tel quel (branches présentes, `echeance.txt`, dossier d'envoi) : une seconde tentative demande des noms neufs, donc une version nouvelle ; à dire à Lazar dans le préavis.

## 8. Essais rejoués (processeur seul, sans réseau, environnement vidé, clés factices du banc)

Dossier `sans-ssh-v2/` extrait du commit `85a84ff5` dans le bloc-notes ; `ESSAI_DEPOT` = le dépôt de travail (branches distantes du lot à `85a84ff5`, de la préparation à `5432ac56`, `main` à `64cb67bd`) ; aucun changement du banc. Environnement : Python 3.13.18, numpy 2.5.3, 4 processeurs, charge moyenne de 10 à 11 pendant les essais.

| essai | rejeu | auteur (résultats scellés) |
|---|---|---|
| outil de la session v2 | **36 cas conformes sur 36**, code 0, 10 s | 36 sur 36 |
| scénarios rapides de l'amorce et du programme machine v2 | **17 conformes sur 17**, code 0, 11 min 21 s (12:02:42Z à 12:14:03Z) ; mêmes fins et mêmes nombres de fichiers poussés que l'auteur, scénario par scénario ; aucune fuite, aucun nom interdit ; aucun processus du banc restant | 17 sur 17 |
| scénario intégral (vrai lanceur v74) | **non rejoué** : l'auteur lui-même le mesure à 1 080 s, au-delà de la limite de 15 minutes, sur une machine moins chargée que celle-ci. Le résultat scellé de l'auteur n'est ni confirmé ni contredit | conforme, fini, 1 080 s, 248 fichiers |

Compléments du lecteur (programmes dans le bloc-notes, non versés) : destruction au prix hors borne et au prix absent, étiquette autre, destruction recommencée, preuve d'absence avec et sans inventaire avant destruction, témoin disparu (M1, M2) ; sept causes de feu confrontées à l'aide de la machine (M3) ; treize formes du balayage (clé brute et en base64, jeton en base64, secret brut, hexadécimal en minuscules et en majuscules, base64, phrase brute et en base64 : trouvés, code 3, aucune valeur imprimée ; secret coupé par un retour à la ligne et base64 décalé : non trouvés, comme écrit en m10) ; six entrées factices du crochet (section 3).

**Laissé dans le bloc-notes, faute de suppression permise** (en-tête) : `/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/` — `banc/` (dossier extrait, 588 Ko), `jet/` (dossiers jetables des essais, 483 Mo), `lu/` et `crochet/` (copies de lecture et entrées factices, 400 Ko). Rien de privé : clés factices du banc, phrase de répétition. À supprimer par la mère.

## 9. Rien de dégradé ? Point par point

| sujet | constat |
|---|---|
| argent | minuterie armée avant toute passe, inchangée ; garde des 12 h 30 inchangée ; borne au prix de l'offre resserrée (2,55 USD au lieu de 2,93) ; **dégradé au prix relu : N1** |
| clés | passées par leur nom seulement (rejeu : « aucune valeur imprimée », treize affectations reçues par la doublure, sortie en 0600) ; jamais sur le disque de la machine ; gardées plus longtemps dans le programme quand la poussée échoue (déclaré, M4) ; exposition de 17 h au lieu de 14 h 40 (déclarée, M5) ; liste des instances lue par l'outil seul (réserve n5) |
| phrase chiffrée | chiffrement inchangé (RSA-OAEP, SHA-256) ; renforcé : clé de 4096 bits exigée, fichier effacé même si la poussée échoue (réserve n4) |
| balayage | étendu de deux formes ; limites écrites ; scénario « fuite-cle » conforme |
| destruction par identifiant | ligne imprimée avec le seul identifiant relu du fichier, `-y` ; preuve d'absence par témoins inchangée, jouable dans les deux cas neufs (réserve n6) |
| intouchables | aucune commande imprimée n'en nomme une ; `creation` et `trouver` refusent encore un identifiant de la liste ; liste réduite à bon droit (n7) |

## 10. Consignes proposées à la mère, si elle joue la v12 sans version nouvelle

1. Écrire N1 : prix relu au-dessus de 0,17 USD/h → destruction aussitôt, nœud.
2. Consigner sa lecture de M5 avec l'acteur de chaque geste après 22:39Z (C1) ; préavis à Lazar avant l'impression : échéance, clés, recours de la mesure hors d'atteinte, présence de Lazar pour la phrase, pas de seconde tentative sans version nouvelle (n11), remplacement des clés proposé après le pilote (n3).
3. Jouer la création sous la seule forme de la section 2, point 7, après l'essai du crochet sur un cas sain et un artefact (C2).
4. Annoncer aux autres sessions les fenêtres de création et de destruction, et l'interdit de la liste brute (n7, m13).
5. Phrase : effacer le fichier après tout refus qui précède la poussée (n4). Destruction : si l'instance est déjà absente, `verifier-destruction` d'abord (n6) ; après un refus « arguments ou fichier », chercher la liste restée dans `/tmp` (n5).

## 11. Limites de cette vérification

Lecture et essais sur processeur seulement : rien n'a été éprouvé chez le loueur ni chez les fournisseurs. Seul le différentiel a été relu : l'équivalence v10 → v11, la lecture du texte scellé pour la phrase et les sections inchangées reposent sur la vérification de la v11. Le scénario intégral n'a pas été rejoué. Le point n5 n'est pas éprouvé. Le crochet a été éprouvé par son programme sur des entrées factices, avec le registre de `main` tel qu'il est sur le disque à l'heure d'écriture ; les règles de permission et le classifieur de la session qui lance ne l'ont pas été. La durée de 12 h du pire cas de `jouer` et la durée des mondes sur l'hôte loué sont reprises des versions précédentes.

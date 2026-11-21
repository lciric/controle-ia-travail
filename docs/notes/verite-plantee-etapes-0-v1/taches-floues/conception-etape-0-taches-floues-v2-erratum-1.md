# Erratum 1 de la conception v2 de l'étape 0 des tâches floues (garde G1, deux majorants, accord GO-2026-11-21-69, noyau)

- **Pièce corrigée** : `conception-etape-0-taches-floues-v2.md`, `582da7c1b839876d041558a00d3d073c17c3a47425fa88798f73a01d5cda2edb` (recalculée, égale au compagnon). Elle reste telle quelle (R12) ; elle se lit désormais avec cet erratum, qui prime sur les lieux qu'il cite. Le brouillon du préenregistrement a son propre erratum 1 : `preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-1.md`, même dossier.
- **Origine** : la vérification des corrections par Claude Opus 5.5, `verification-corrections-etape-0-taches-floues-v2-opus-v1.md`, `23a3bfbfb0504f30ae61a60d56a2d7fb9386369a8a7427c8ac366ffe1d3ba0e2` ; erreurs neuves E1 (importante) et E2 à E5 (mineures).
- **Auteur** : Claude Opus 5.5, agent neuf, sur mandat de la session orchestratrice. Erratum court qui porte des corrections relevées par la vérification ; il ne demande pas Fable (règles « Qui conçoit » et « Économie de Fable »). Écrit le 21 novembre 2026, vers 20:35Z. Processeur seul : aucun appel payant, ni commit ni poussée.
- **Ce qu'il ne fait pas** : il ne prend aucune autre décision. Il ne touche ni aux mondes, ni aux témoins, ni aux critères, ni à la table d'admission, ni aux nœuds du § 10.
- **Pièces neuves, même dossier** :
  - `essai-garde-g1-erratum-1-v1.py`, `87c3df206a36e2e4bc4bf38a6eabd4a580313458354b68cd9f1961e2bbd4399f`, et sa sortie `essai-garde-g1-erratum-1-v1.txt`, `1c965b0e7ce473f69cdab78428c44748bf65b20d5cb904300033abd623db9090` : l'essai de la règle neuve de G1 (R5), sous Python 3.13.18 et **numpy 2.5.3**. Le rejeu donne une sortie identique à l'octet (`cmp`).
  - `recalcul-e3-erratum-1-v1.py`, `a558d1743e433dacda6a4822223decd8b03226b891b6a37a4e1987d4925c4ab0`, et sa sortie `recalcul-e3-erratum-1-v1.txt`, `08dc289daa60e89d7493ac951e4ffca2e99b2d3163c266ab14fedf7f74d11c68` : le recalcul des deux majorants de E3, en arithmétique décimale.
- **Cloisonnement** : je n'ai ouvert que les pièces nommées par le mandat, le registre des accords, la réponse v2 du concepteur sur l'adjudant (pour E5) et des noms de fichiers. Je n'ai lu aucune famille tenue à l'écart ni aucun résultat de course. Aucun refus d'outil ni de classifieur.

## E1 (important) : le crochet d'audit de G1 et les sous-modules que numpy charge à la demande

**Constat, reproduit ici.** Sous numpy 2.5.3, `import numpy` ne charge pas `numpy.random`. Le premier appel à `numpy.random.default_rng` lève une quarantaine d'événements `import` et `open`, et `numpy.unique` charge `numpy.ma`. Un attribut comme `numpy.polynomial` charge aussi son sous-module à la demande, sans aucun `import` écrit. L'essai montre aussi un deuxième effet du même genre, que la vérification n'avait pas vu : charger le module des témoins par son fichier fait écrire son code compilé (`__pycache__/….pyc`), donc un `open` en écriture. Ce `open` lève le drapeau dès le chargement, sur tout témoin.

**Lieu 1** : § 7, « G1, cloisonnement des processus : deux mécanismes », premier point, *Contrôle statique*.

Ancien texte :
> tout import hors de la liste fermée `math`, `json`, `numpy` et ses sous-modules, et la bibliothèque de l'interface ;

Nouveau texte :
> tout import hors de la liste fermée `math`, `json`, `numpy`, les sous-modules de numpy nommés dans la liste de préchargement du lanceur (deuxième point ci-dessous), et la bibliothèque de l'interface ;

**Lieu 2** : même paragraphe, deuxième point, *Garde à l'exécution*, en entier.

Ancien texte :
> *Garde à l'exécution, dans le processus de l'expérimentateur.* La première instruction du lanceur pose un crochet d'audit par `sys.addaudithook`, avant tout chargement du module des témoins. Pendant le chargement, le crochet vérifie chaque événement `open` : lecture seule, et chemin situé sous les dossiers de l'interpréteur, de ses bibliothèques ou de l'expérimentateur ; tout autre cas lève le drapeau d'arrêt. Le module des témoins importe en tête tout ce dont il a besoin, pour qu'aucun import ne survienne plus tard. Une fois les modules chargés et avant la lecture du lot, le lanceur arme le crochet : dès lors tout événement `open`, tout événement dont le nom commence par `os.`, `subprocess.`, `socket.`, `shutil.` ou `ctypes.`, et tout événement `import` lève le drapeau d'arrêt et une exception. Le lanceur relit le drapeau après chaque temps ; s'il est levé, il écrit une ligne sur sa sortie d'erreur et sort avec le code 97, que le témoin ait rattrapé l'exception ou non. Le noyau arrête le banc sur ce code, et sur toute sortie sans réponse.

Nouveau texte :
> *Garde à l'exécution, dans le processus de l'expérimentateur.* Le lanceur ne fait, dans cet ordre, que ce qui suit.
> 0. *Avant le crochet.* Il ne charge que `sys`. Il calcule les racines admises à partir de `sys` seul : les quatre préfixes de l'interpréteur (`sys.prefix`, `sys.base_prefix`, `sys.exec_prefix`, `sys.base_exec_prefix`), les entrées de `sys.path` situées sous ces préfixes, et le dossier de l'expérimentateur. Il coupe l'écriture du code compilé (`sys.dont_write_bytecode = True`). Le processus est lancé par `python -I`.
> 1. *Pose du crochet* par `sys.addaudithook`, avant tout autre chargement. Phase « chargement » : chaque événement `open` doit être en lecture seule, sur un chemin situé sous une racine admise ; tout autre cas lève le drapeau d'arrêt.
> 2. *Préchargement de la liste fermée.* Le lanceur importe, par leur nom, les modules de la constante `PRECHARGES`, écrite dans son code : `json`, `math`, `numpy`, `numpy.random`, `numpy.ma`, `numpy.linalg`. Puis il charge le module des témoins. La liste est fermée : elle ne s'étend que par une correction du lanceur, contre-lue en classe B, et sa valeur est consignée au manifeste avec la version de numpy. Le contrôle statique refuse tout sous-module de numpy qui n'y est pas.
> 3. *Échauffement*, encore non armé. Le lanceur fait un tour complet de chaque témoin du module (`preparer`, `decider`, `conclure`) sur un lot d'essai sans vérité. Ce lot est construit par le lanceur à la forme du § 1.2, avec des champs constants et la graine `[0, 0, 0, 0]`. Il ne vient d'aucun monde, et ses réponses sont jetées sans jamais être écrites sur la sortie. Pendant ce tour, les règles du chargement s'appliquent, et **tout événement `import` lève le drapeau** : un sous-module que la liste a oublié se voit ici, avant la lecture du lot servi, et non sur le banc.
> 4. *Lecture du lot servi* sur l'entrée standard, qui n'ouvre aucun fichier.
> 5. *Armement.* Dès lors, tout événement `open`, tout événement dont le nom commence par `os.`, `subprocess.`, `socket.`, `shutil.` ou `ctypes.`, et **tout événement `import`** lèvent le drapeau d'arrêt et une exception. Un import neuf après l'armement reste un arrêt, quelle que soit sa cause : un `import` écrit, ou un attribut de numpy chargé à la demande. L'import d'un module déjà en mémoire ne lève aucun événement : il passe.
> 6. Le lanceur relit le drapeau après l'échauffement et après chaque temps. S'il est levé, il écrit sur sa sortie d'erreur une ligne qui nomme la phase et l'événement, puis il sort avec le code 97, que le témoin ait rattrapé l'exception ou non. Le noyau arrête le banc sur ce code, et sur toute sortie sans réponse. Un code 97 levé à l'échauffement est un défaut de la liste ou du lanceur, à corriger selon la règle de rejeu (point 11 de la liste d'arrêt). Il n'accuse pas le témoin.
>
> La liste `PRECHARGES` vaut pour numpy 2.5.3 et les témoins tels qu'écrits. Ce qu'une version de numpy charge à la demande change d'une version à l'autre : toute autre version, ou tout témoin qui emploie une fonction neuve de numpy, repasse le cas sain de G1 avant le banc. Éprouvé : `essai-garde-g1-erratum-1-v1.py` (en-tête de cet erratum).

**Lieu 3** : § 7, table des gardes, ligne « G1 cloisonnement des processus ».

Ancien texte, colonne « Cas sain » :
> le module des témoins tel qu'écrit, sur un lot d'essai : aucun arrêt

Nouveau texte :
> chaque témoin du module tel qu'écrit, lancé par le lanceur réel (préchargement, échauffement, armement), sur un lot d'essai : aucun code 97, une réponse au schéma. Le cas sain compte au moins un témoin qui tire sa pièce (`numpy.random`) et un qui appelle `numpy.unique` (`numpy.ma`)

Ancien texte, colonne « Artefact qui doit la déclencher » :
> contrôle statique : un témoin factice qui importe le noyau ; un autre qui appelle `open`. Garde à l'exécution : un témoin factice sans import ni nom refusé, dont le temps `decider` lit son propre fichier source par une fonction de numpy : sortie au code 97

Nouveau texte (la lecture du fichier porte aussi E2) :
> contrôle statique : un témoin factice qui importe le noyau ; un autre qui appelle `open` ; un autre qui importe un sous-module de numpy hors de la liste fermée. Garde à l'exécution, chacun admis par le contrôle statique et sorti au code 97 avec le motif attendu : (a) un témoin factice dont le temps `decider` exécute `numpy.fromfile(__file__, dtype=numpy.uint8)` sur un chemin que l'échauffement n'exerce pas (motif « armé : open ») ; (b) un témoin factice qui, sur ce même chemin, touche `numpy.polynomial` par un attribut (motif « armé : import ») ; (c) le cas sain lancé avec une liste privée de `numpy.ma` (motif « échauffement : sous-module hors de la liste fermée »)

**Sortie de l'essai** (`essai-garde-g1-erratum-1-v1.txt`). Le cas sain sort au code 0, avec 20 décisions et 4 ouvertures demandées. Les artefacts (a), (b) et (c) sortent tous trois au code 97, chacun avec son motif. Le rappel de l'erreur de la version 2 (aucun préchargement) arrête un témoin conforme au code 97, sur `numpy.random`. Verdict : « tous les cas sont conformes ». Ces essais sont déterministes et n'ajoutent rien à la probabilité d'échec à tort des essais des gardes (0,0042).

## E2 (mineur) : l'artefact de lecture de fichier

**Lieu** : § 7, table des gardes, ligne G1. Porté au lieu 3 de E1 : « par une fonction de numpy » devient « exécute `numpy.fromfile(__file__, dtype=numpy.uint8)` ». Cette fonction lève directement l'événement `open`, sans import préalable, comme l'essai le vérifie (motif « armé : open <dossier temporaire>/temoin_fromfile.py »).

## E3 (mineur) : deux majorants de D3 dans F7

**Vérification** (`recalcul-e3-erratum-1-v1.txt`). Je reprends le taux de désaccord de l'honnête au banc, non arrondi, du programme v2 : 0,05937980642007634. Tout le reste est refait en décimal.
- La borne haute de Clopper-Pearson à 95 % pour 66 désaccords sur 400 vaut 0,1986078537. Le « 0,1986 » imprimé est un arrondi par défaut, contraire à la règle d'arrondi par excès des bornes : **0,1987**, comme la vérification le propose.
- La probabilité qu'au moins un des 20 lots dépasse 66 désaccords vaut **4,689 × 10⁻¹³**. Le « 4,7 × 10⁻¹³ » imprimé est donc déjà un majorant arrondi par excès, et **il reste inchangé**. Le 4,76 × 10⁻¹³ de la vérification vient du taux arrondi à 0,0594 (recalcul au même taux : 4,763993 × 10⁻¹³). Écrire 4,8 × 10⁻¹³, comme le mandat le demandait, donnerait un majorant valide mais plus lâche, et en désaccord avec le bloc K. Je ne l'écris pas, et je le signale à la session orchestratrice. Le second terme du total imprimé (ne pas mourir à cette borne sur 4 000 tâches, mort à 874) est négligeable : le programme v2 rend un total égal au premier terme à la précision double.

**Lieu** : § 5, table d'admission, ligne « Borne reportée en service (D3) ».

Ancien texte :
> borne de service, part vraie 0,530 contre 0,1986 au plus

Nouveau texte :
> borne de service, part vraie 0,530 contre 0,1987 au plus (0,198608, arrondi par excès)

La colonne « au plus 4,7 × 10⁻¹³ [calcul, G] » est inchangée. La sortie `calculs-etape-0-taches-floues-v2.txt` (bloc G, « d'au plus 0.1986 ») n'est pas récrite. Elle arrondit au plus proche, et ce chiffre se lit désormais par cet erratum. Le programme `verification-chiffres-etape-0-taches-floues-v2.py` ne cherche pas 0,1987 : ce chiffre a sa source dans `recalcul-e3-erratum-1-v1.txt`.

## E4 (mineur) : la ligne de GO-2026-11-21-69 est au registre

**Fait vérifié.** La ligne est au registre des accords, `registres/go.md`, **ligne 668**, sur `origin/main` (`241c7c4a`), fusionnée dans la branche de travail (`e4ba422d`). Son contenu utile ici : « Mots de Lazar vers 17:30Z […] « go autonomie 12h go recos go depenses » : douze heures d'autonomie de la mère, recommandations en attente accordées, dépenses sur devis accordées (chaque devis consigné avant la course ; contact, publication, paiement restent à Lazar). » Portée : « douze heures, jusqu'à 2026-11-22T05:30Z ; dépenses sur devis ». Lue à 2026-11-21T17:40:07Z.

**Lieu 1** : en-tête, point « Accords ».

Ancien texte :
> GO-2026-11-21-69, sous l'autonomie duquel la session orchestratrice a tranché le constat bloquant 1 : cité d'après le mandat ; sa ligne n'est pas au registre des accords de cet arbre de travail, dont le dernier identifiant du jour est GO-2026-11-21-66 (à vérifier au versement).

Nouveau texte :
> GO-2026-11-21-69, sous l'autonomie duquel la session orchestratrice a tranché le constat bloquant 1 : au registre des accords, `registres/go.md`, ligne 668 (« go autonomie 12h go recos go depenses » : douze heures d'autonomie de la mère, jusqu'au 2026-11-22T05:30Z, recommandations en attente accordées, dépenses sur devis accordées).

**Lieu 2** : § 10, « Réserves », dernier point.

Ancien texte :
> La ligne de l'accord GO-2026-11-21-69 n'est pas au registre de cet arbre de travail ; la décision sur F4 est écrite d'après le mandat.

Nouveau texte :
> La ligne de l'accord GO-2026-11-21-69 est au registre des accords (`registres/go.md`, ligne 668). La décision sur F4, prise sous cette autonomie, reste à consigner au registre des décisions (condition de scellement 4 du brouillon).

## E5 (mineur) : le noyau est un module autonome, compatible avec le banc de l'adjudant

**Fait vérifié.** Le banc de l'adjudant n'existe pas encore en code. Aucun module de `src/`, de `scripts/` ni de `tests/` ne le nomme, et aucune branche ne le porte. La réponse v2 du concepteur sur l'adjudant (`docs/notes/mecanisme-adjudant-hors-distribution-v1/reponse-fable-mecanisme-adjudant-v2.md`, `4f8fbeaf5db818c0b5fddfc4a531544044fa0eac0d604448853c5466cd3ba061`) le décrit comme des pièces à écrire. § 7.9 : « Générateur, noyau, porte des lots, registre | B | développeur | un autre modèle, avec mutations ». § 4, point 4 : « générateur, noyau et témoins en un paquet à bibliothèque standard ». § 7.8, point 7 : « noyau chez la mère ; morts et issues écrites par programme ». Il n'y a donc pas de noyau existant à « augmenter ».

**Lieu 1** : § 6, premier alinéa, dernière phrase.

Ancien texte :
> Ce noyau est celui du banc de l'adjudant, augmenté de ce que cette épreuve demande (§ 9, point 13).

Nouveau texte :
> Ce noyau est un module autonome, écrit pour cette épreuve, et compatible avec le banc de l'adjudant tel que la réponse v2 sur l'adjudant le décrit (§ 7.9 et § 7.8 de cette réponse) : mêmes pièces (générateur, noyau, porte des lots, registre, en classe B, contre-lues avec mutations), noyau chez la session orchestratrice, morts et issues écrites par programme. Le code de ce banc n'existe pas encore. La compatibilité reste à vérifier par la session orchestratrice (condition de scellement 5 du brouillon ; § 9, point 13).

**Lieu 2** : § 9, point 13, première phrase en gras.

Ancien texte :
> **Le banc est celui de l'adjudant, augmenté**

Nouveau texte :
> **Le noyau est un module autonome, compatible avec le banc de l'adjudant (erratum 1, E5)**

Le reste du point 13 et le nœud 6 du § 10 ne changent pas. L'option (a) ou (b) de D-4 reste à trancher comme ils le disent. Cet erratum ne la tranche pas.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du développeur — programme des seuls noms de clés de `contenu` hors des dix champs, fichier des cartes de la course v9 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la demande de la mère (R-4153) après le refus du masque (« champ(s) hors de la configuration (1) »). **Le programme est écrit, essayé sur des fichiers synthétiques et contre-lu ; il n'est pas joué** : son jeu attend le mot de Lazar.

## Ce que fait le programme (et rien de plus)

`noms_cles_contenu_hors_champs_v1.py`, bibliothèque standard seulement :
- arguments : `--fiches CHEMIN`, `--configuration CHEMIN` (la configuration A scellée, `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json`), `--sortie CHEMIN` (refusé si lui ou son compagnon existe) ; aucun chemin par défaut, aucune liste ni recherche de dossier ;
- empreintes gelées dans le programme : `fiches` = `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, `configuration` = `8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4` ; il calcule chaque empreinte sur les octets **avant** tout décodage et refuse (code non nul, motif sans valeur) si l'une diffère ;
- il décode d'abord la configuration et en tire la liste des dix champs (lis le masque scellé `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py`, `07ed8725…`, pour savoir **exactement** où le masque lit les champs dans la configuration et dans chaque carte — `extraire_contenus` — et reproduis ce chemin à la lettre) ;
- il décode ensuite les cartes et, pour chaque carte, ne lit que **les noms des clés** de `contenu` ; il ne lit, ne copie, n'affiche ni n'écrit **aucune valeur**, aucun identifiant de carte ;
- il écrit, dans `--sortie`, un JSON à **trois** champs seulement : `cles_hors_champs` (liste triée d'objets `{"nom": …, "nombre_de_cartes": …}`), `nombre_de_cartes` (entier), `empreintes` (`fiches`, `configuration`) ; puis son compagnon `.sha256` ; à l'écran, « FAIT » ou le motif d'un refus, **jamais un nom de clé, un identifiant ni une valeur** ;
- garde : un nom de clé de plus de 64 caractères, ou contenant un saut de ligne, n'est pas écrit tel quel : il est remplacé par `"(nom non rapporté : longueur L)"`, et son compte est gardé (un nom ne doit pas pouvoir porter du contenu).

## Essais

`essais_noms_cles_contenu_hors_champs_v1.py`, lancés par `env -C DOSSIER python3 -B -m pytest -q -p no:cacheprovider F`, **hors du dépôt** (les fichiers d'essai s'écrivent dans ton bloc-notes), sur des fichiers **synthétiques** que tu fabriques (jamais le vrai fichier) de la forme exacte que le masque attend : cas sain (aucune clé de plus : liste vide) ; une clé de plus sur une carte ; deux clés de plus sur des nombres de cartes différents ; nom long ou à saut de ligne ; empreinte fausse de chaque fichier ; sortie existante ; ordre « configuration puis cartes » ; aucune valeur, aucun identifiant de carte dans la sortie ni à l'écran (l'essai le vérifie en semant des valeurs et des identifiants repérables). Les constantes gelées se remplacent dans les essais par un moyen interne (appel de fonction avec empreintes en paramètre) ; le point d'entrée en ligne de commande n'accepte que les constantes.

Rapport `rapport-developpeur-noms-cles-contenu-v1.md` : fichiers et empreintes, essais, la commande unique de jeu.

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-noms-cles-contenu/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte ou `test -f`.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle ; signe « développeur, modèle O ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

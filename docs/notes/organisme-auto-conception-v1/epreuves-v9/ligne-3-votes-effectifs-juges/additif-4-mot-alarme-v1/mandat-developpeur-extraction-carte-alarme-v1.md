VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du développeur — programme qui n'extrait que la carte de l'alarme, champ `meta` retiré — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-39, point (6) : « lettre de la carte vérifiée par le procédé du texte, sans retoucher la règle ». Le procédé du texte (préenregistrement de la ligne 3, v7, l. 30 et l. 32) : la carte est lue « par un programme qui n'extrait qu'elle, champ `meta` retiré ». Aucun programme de ce genre n'est versé ; tu l'écris. Pièce d'instrument (classe B) : contre-lue par un autre modèle. **Le programme est écrit et essayé sur des fichiers synthétiques ; il n'est pas joué** : le jeu se fera par un agent neuf, sur un mandat que la mère voit avant.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni leurs contre-lectures, et n'a lu aucune carte. Tu signes « développeur, modèle O ».

## Ce que fait le programme (et rien de plus)

`extraire_carte_alarme_v1.py`, bibliothèque standard seulement :
- arguments : `--fiches CHEMIN`, `--sortie CHEMIN` (refusé si lui ou son compagnon existe, ou s'il est sous un dossier nommé `archives-reponses-modeles` ou sous le dépôt `/home/user/controle-ia-travail`) ; aucun chemin par défaut, aucune liste ni recherche de dossier ;
- constantes gelées : empreinte du fichier `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, identifiant de la carte `fcbf4a2dd1a57`, nombre de cartes 94 ; il calcule l'empreinte sur les octets **avant** tout décodage et refuse (code non nul, motif sans valeur ni texte de carte) si elle diffère, si le compte diffère de 94, ou si l'identifiant est absent ou présent plus d'une fois ;
- il ne garde en mémoire, après décodage, **que** la carte de cet identifiant ; il retire le champ `meta` **avant tout usage** ; il n'écrit, n'affiche ni ne journalise rien d'une autre carte, aucun autre identifiant, rien du champ `meta` ;
- il écrit dans `--sortie` un JSON à trois champs : `carte` (la carte sans `meta`), `empreinte_fiches`, `identifiant` ; puis son compagnon `.sha256` ; à l'écran : « FAIT » ou le motif d'un refus, **jamais** un texte de carte ;
- lis le masque scellé `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed8725…`) pour savoir **exactement** comment le fichier des cartes est structuré (où sont la liste des cartes, l'identifiant, `meta`), et reproduis ce chemin à la lettre.

## Essais

`essais_extraire_carte_alarme_v1.py`, lancés **hors du dépôt** par `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider F`, sur des fichiers **synthétiques** de la forme exacte que le masque attend (jamais le vrai fichier) : cas sain (sortie = la seule carte, sans `meta`) ; empreinte fausse ; compte faux ; identifiant absent ; identifiant en double ; sortie existante ; sortie sous un dossier interdit ; aucune autre carte, aucun autre identifiant, rien de `meta` dans la sortie ni à l'écran (semés de chaînes repérables) ; messages d'erreur et traces d'exception sans texte de carte. Chaque garde essayée sur un cas sain et sur un artefact (R5). Les constantes se remplacent dans les essais par un moyen interne (fonction aux paramètres explicites) ; le point d'entrée en ligne de commande n'accepte que les constantes.

Rapport `rapport-developpeur-extraction-carte-alarme-v1.md` : fichiers et empreintes, essais et leur sortie, la commande unique de jeu en gabarit (chemin du fichier : `/home/user/controle-ia-travail/archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json`, à ne pas toucher toi-même).

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-extraction-carte-alarme/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte ou `test -f`.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

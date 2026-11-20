VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER.

# Mandat du développeur — programme de vérification X6 contre le fichier des cartes de la course v9 — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-23 (« go a », R-4114) : seconde et dernière exception pour le manifeste du rejeu. Code par un développeur de modèle L′ ; contre-lu par un autre modèle ; joué une seule fois par un agent neuf, plus tard.

## Ce que fait le programme (et rien de plus)

`verifier_x6_contre_fiches_v1.py`, bibliothèque standard seulement :
- arguments : `--fiches CHEMIN` (le fichier des cartes), `--extraction CHEMIN` (la sortie de l'extraction X6), `--sortie CHEMIN` (fichier neuf, refusé s'il existe) ; aucun chemin par défaut, aucune liste ni recherche de dossier ;
- empreintes attendues gelées dans le programme : `fiches` = `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`, `extraction` = `f5c7cc1c…` (l'empreinte entière est à lire dans le compagnon de `docs/notes/organisme-auto-conception-v9-mere/juge-selection-x6-v1/sortie-extraction-x6-v2.json` sur main, par `git show` redirigé) ; le programme calcule l'empreinte de chaque fichier **avant** de le décoder, et refuse (code non nul, aucune autre sortie) si l'une diffère ;
- il décode `fiches` comme un objet JSON dont il ne lit **que les clés** (identifiants) ; il ne lit, ne copie ni n'affiche aucune valeur ; il décode `extraction` et n'en lit que la liste `extraction.identifiants_par_classe.a_corriger`, qui doit compter exactement deux identifiants (sinon refus) ;
- il écrit, dans `--sortie`, un JSON à **trois** champs seulement : `nombre_de_cles` (entier), `retenues_presentes` (liste de deux booléens, dans l'ordre de l'extraction), `empreintes` (`fiches`, `extraction`) ; puis son compagnon `.sha256` ; et rien à l'écran sauf « FAIT » ou le motif d'un refus, **jamais un identifiant**.

## Essais

Essais (`essais_verifier_x6_contre_fiches_v1.py`, `python3 -B -m pytest -q -p no:cacheprovider`) sur des fichiers **synthétiques** que tu fabriques dans ton bloc-notes (jamais le vrai fichier) : cas sain (94 clés, deux retenues absentes) ; artefacts : empreinte fausse de chaque fichier, extraction à une ou trois retenues, retenue présente, fichier de sortie existant, clé de plus dans la sortie impossible, aucun identifiant dans la sortie ni à l'écran (l'essai le vérifie). Pour les essais, une option `--empreintes-attendues-essai` ou équivalent ne doit pas exister : les essais remplacent les constantes par un moyen interne aux essais seulement (par exemple en important le module et en appelant la fonction avec des empreintes passées en paramètre), et le point d'entrée en ligne de commande n'accepte que les constantes gelées.

Rapport `rapport-developpeur-verification-x6-v1.md` : fichiers et empreintes, essais passés et échoués, la commande unique de jeu (`python3 -B verifier_x6_contre_fiches_v1.py --fiches … --extraction … --sortie …`).

Ton bloc-notes : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-verification-x6/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes**, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte : le jeu reviendra à un agent neuf. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

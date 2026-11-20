VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — programme des noms de clés de `contenu` — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-28 (R-4157) : le programme est contre-lu « conforme » avant son jeu unique.

## Qui

Un contre-lecteur neuf, modèle S, qui n'a écrit ni le programme, ni ses essais, ni le masque. Tu signes « contre-lecteur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier N = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/programme-noms-cles-v1/` :
- le mandat du développeur, un dossier au-dessus : `mandat-developpeur-noms-cles-contenu-v1.md` (`df0df0c2…`) ;
- `noms_cles_contenu_hors_champs_v1.py` (`26eeaa798e14c716bbe4bd0c323e797e60470459d9a13b804ccacb07ea121120`), `essais_noms_cles_contenu_hors_champs_v1.py` (`a3089f6b…`), `rapport-developpeur-noms-cles-contenu-v1.md` (`fe8a8651…`) ;
- le masque scellé : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) ;
- le compte rendu du refus du masque : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/compte-rendu-masque-et-lecteur-programme-rejeu-v1.md`.

## Ce que tu vérifies

1. Le chemin des champs dans la configuration et des clés dans chaque carte est **exactement** celui de `extraire_contenus` du masque : un nom que le masque compte « hors de la configuration » est rendu par le programme, et réciproquement. Le refus réel (« champ(s) hors de la configuration (1) ») doit donc donner exactement un nom.
2. Empreintes sur les octets avant tout décodage ; configuration avant cartes ; aucune valeur, aucun identifiant de carte écrit ni affiché, ni sur un succès, ni sur un refus, ni sur une erreur imprévue.
3. Sortie : trois champs exactement, compagnon, refus si la sortie ou son compagnon existe ; garde des noms longs ou à saut de ligne.
4. Les huit écarts d'interprétation du rapport : juge chacun (en particulier n° 2, cartes hors du choix ; n° 3, refus si aucune carte ouverte ; n° 7, contrôles non reproduits).
5. Essais : lance-les **sur des copies** dans ton dossier (`env -C TON_DOSSIER/copie python3 -B -m pytest -q -p no:cacheprovider essais_noms_cles_contenu_hors_champs_v1.py`), jamais dans le dépôt ; au moins trois mutations à la main sur une copie (chemin des clés, valeur dans la sortie, décodage avant empreinte), dis si un essai les attrape.
6. La commande unique de jeu : la configuration A se tire de main (`git show origin/main:prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json`, redirigé hors du dépôt) ; la sortie s'écrit hors du dépôt. Écris la commande exacte à donner à l'agent du jeu.

Rends `contre-lecture-noms-cles-contenu-v1.md` : « Conforme » ou « À corriger », corrections numérotées. Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-noms-cles-contenu/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande. Tu ne joues pas le programme sur les vraies cartes.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — masque de style v2, rejeu du juge de sélection — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-36, point (1). Le masque v2 est une pièce d'instrument (classe B) : contre-lecture par un autre modèle que son développeur, puis vérification des corrections par le même contre-lecteur.

## Qui

Un contre-lecteur neuf, modèle S, qui n'a écrit ni le masque v1 ou v2, ni la configuration A, ni les critères. Tu signes « contre-lecteur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier V = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/configuration-a-v2/masque-v2/`.
- `V/mandat-developpeur-masque-v2-v1.md` est au dossier parent : `…/configuration-a-v2/mandat-developpeur-masque-v2-v1.md` (`93bc98d6…`) : ce qui était demandé.
- `V/masque_style_cartes_v2.py` (`769aace5b64c697799b76a0120a5c2926c75798a388c93fa00ddc93224401c01`), `V/essais_masque_style_cartes_v2.py` (`7c84260f…`), `V/differentiel-masque-v1-v2.diff` (`efb1c82b…`), `V/rapport-developpeur-masque-v2-v1.md` (`92c9f0b8…`).
- Le masque v1 : `…/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed8725…`) et ses essais `…/criteres-v4/essais_masque_style_cartes_v1.py`.
- La configuration A v2 et sa proposition : `…/configuration-a-v2/configuration-a-masque-v2.json` (`a6c5d87b…`), `…/configuration-a-v2/proposition-configuration-a-v2-v1.md` (§ 3 et § 4).
- Le lecteur par programme v2 : `…/juge-selection/criteres-v5/lecteur_par_programme_cartes_v2.py` (`de99117b…`).

## Ce que tu fais

1. **Le différentiel** refait par `diff -u` (redirigé) : égal à celui du développeur ; rien ne change hors de ce que le mandat du développeur permet.
2. **Le code** lu en entier aux lieux qui changent : les quatre exigences du mandat ; aucune valeur d'une clé retirée lue, copiée, écrite ni affichée ; toute autre clé hors champs reste un refus ; sans la huitième clé, conduite égale au v1 ; gardes sans repli silencieux (R5).
3. **Les essais rejoués** dans ton dossier, sur des copies (les essais attendent `masque_style_cartes_v1.py` à côté d'eux : copie le v1 du dépôt dans ton dossier, empreinte vérifiée), par `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_masque_style_cartes_v2.py`. Dis ce qui manque aux essais.
4. **Le lecteur par programme v2** : accepte-t-il la sortie du masque v2 (troisième ligne d'en-tête), ou ne la lit-il pas ? Lu seulement, jamais lancé sur des cartes.
5. **Les six remarques du rapport du développeur** (§ 6) : jugées une à une (garder, corriger, porter à la mère).
6. **La configuration A v2** est-elle acceptée par `valider_configuration` du v2 ? Essai par un programme écrit avec l'outil d'écriture de fichiers dans ton dossier, lancé par son chemin, sur la configuration seule.

Verdict : « Conforme » ou « À corriger », avec pour chaque correction le lieu et le texte exact attendu. Écris `contre-lecture-masque-v2-v1.md` dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-masque-v2/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte ou `test -f`.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

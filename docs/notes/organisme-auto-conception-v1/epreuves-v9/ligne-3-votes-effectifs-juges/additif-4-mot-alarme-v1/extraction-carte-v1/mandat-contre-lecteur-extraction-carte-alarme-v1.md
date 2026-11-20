VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — programme qui n'extrait que la carte de l'alarme — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-39 (6) et la lecture de la mère R-4202 (un seul passage, par le programme contre-lu, par un agent neuf, sur le seul `fiches.json`, une seule carte en sortie, `meta` retiré). Pièce d'instrument (classe B) : contre-lecture par un autre modèle que son développeur, vérification des corrections par le même.

## Qui

Un contre-lecteur neuf, modèle S, qui n'a écrit ni ce programme, ni le texte de la ligne 3, ni ses additifs. Tu signes « contre-lecteur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier X = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-4-mot-alarme-v1/extraction-carte-v1/`.
- `X/../mandat-developpeur-extraction-carte-alarme-v1.md` (`53bf2bd7…`) : ce qui était demandé.
- `X/extraire_carte_alarme_v1.py` (`79f2cc69245a0e00f2c9bc77202440447cbd0db32dc491a7c5dc8ed6bf539659`), `X/essais_extraire_carte_alarme_v1.py` (`4103e3e6…`), `X/rapport-developpeur-extraction-carte-alarme-v1.md` (`4a1356c3…`).
- Le masque scellé : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v4/masque_style_cartes_v1.py` (`07ed8725…`), pour la structure du fichier des cartes.

## Ce que tu fais

1. **Le code**, lu en entier : empreinte calculée sur les octets avant tout décodage ; compte 94 ; identifiant unique ; seule la carte visée gardée ; `meta` retiré avant tout usage ; aucune autre carte, aucun autre identifiant, rien de `meta` écrit, affiché ou journalisé, messages d'erreur et traces compris ; sortie refusée sous le dépôt, sous `archives-reponses-modeles` ou si elle existe ; ligne de commande limitée aux constantes gelées. Structure du fichier lue comme le masque la lit.
2. **Les essais rejoués** dans ton dossier, sur des copies (`env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_extraire_carte_alarme_v1.py`) ; dis ce qui leur manque.
3. **Les quatre remarques du rapport** (mémoire ; gardes ajoutées ; `meta` au premier niveau seulement ; `-B` sans `-I`) : garder, corriger, ou porter à la mère.
4. **La commande de jeu** du rapport : juste et suffisante pour un agent neuf ?
5. **Verdict** : « Conforme » ou « À corriger », avec pour chaque correction le lieu et le texte exact.

Écris `contre-lecture-extraction-carte-alarme-v1.md` dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-extraction-carte-alarme/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte ou `test -f`.** Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU CITÉ DANS UNE PIÈCE. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER DE TON DOSSIER, JAMAIS À L'ÉCRAN.

# Mandat du rédacteur — préenregistrement du palier 0b, version 7 : écarts de conception révélés par le code, et erratum du commit — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20, dans l'ordre de la place Fable validé par la mère. L'ordre gelé de la v6 (« Ordre des opérations », point 2) veut, après le code et sa contre-lecture, un erratum qui inscrit le commit et les empreintes, puis le scellement par la mère. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/` (noté P0B).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le texte : `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v6.md` (`4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029`), non scellé ; son contrôle `P0B/controle-differentiel-palier-0b-v6-v1.md` (`c079a89d…`), qui laisse **trois remplacements de tenue** à porter.
- Le code : rapport v2 `P0B/code-v2/rapport-developpeur-code-palier-0b-v2.md` (`ca61bf7e…`) ; contre-lecture `P0B/code-v2/contre-lecture-v1/contre-lecture-code-palier-0b-v2-v1.md` (`3778fb39…`), qui juge **les trois écarts au texte** (B7 bis à la dose 0,5 ; audit de présentation sur les traits de forme ; bruit de l'audit des doses par paires), **les quatorze choix** du § 4 du rapport (dont n° 3 et 9 non des silences, n° 11 et 12 écarts à nommer) et ses notes D5, D6, D8, D9 ; outil `P0B/code-v2/contre-lecture-v1/outils-cl/bruit_nul_doses.py` ; rapport v3 `P0B/code-v3/rapport-developpeur-code-palier-0b-v3.md` (`5e3fa3e8…`, table des empreintes) ; vérification `P0B/code-v3/verification-v1/verification-corrections-code-palier-0b-v3-v1.md` (`c5c211c7…`, « Conforme »). Code v3 au commit `3d332d2c` de la branche `lot/compte-organisme-v1`.
- Les mandats et rapports précédents du rédacteur, pour la tenue : `P0B/rapport-redacteur-palier-0b-v6-v1.md`.

## Ce que tu fais

1. **Version 7 du texte** (`preenregistrement-heritage-palier-0b-etage-processeur-v7.md`), par remplacements avec l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON écrit avec l'outil d'écriture de fichiers ; sous le nom neuf (R12) :
   - les trois remplacements de tenue du contrôle v6, à la lettre ;
   - pour chacun des trois écarts, une règle écrite d'avance qui ne vise aucun signe (R3) et ne lit aucun résultat (R1 : aucun tirage décisif n'a été fait) ; tu pars des recommandations de la contre-lecture (dose 0,25 pour le jeu de la garde 27 et marge étrangère non revendiquée à 0,5 sur la couche mécanique, réserve 20 corrigée ; longueur mesurée sur le texte où chaque nombre est remplacé par son jeton ; règle calibrée pour l'audit des doses par paires) et tu motives ton choix ;
   - les dix choix qui sont de vrais silences, inscrits comme règles ; les n° 11 et 12 nommés comme écarts, avec la règle retenue ;
   - pour D5, D6, D8, D9 : une règle ou « laissé, motivé » ;
   - **l'erratum du commit** : le commit du code d'analyse (`3d332d2c`) et la table des empreintes de ses fichiers, reprise du rapport v3, inscrits à l'en-tête (« Commit du code d'analyse ») ; si un changement de règle ci-dessus demande un changement du code, dis-le : le commit inscrit ne vaut alors qu'après un code v4, et l'erratum du commit se refait.
   **Tout changement d'une valeur gelée, d'un seuil, d'un critère ou d'une prédiction est un nœud de Lazar** : tu le poses au format, tu ne le tranches pas ; s'il est tranché autrement, la v7 change.
2. Différentiel `diff -u` v6 → v7 et rapport `rapport-redacteur-palier-0b-v7-v1.md` : sources avec chemin et empreinte, choix motivés, ce qui demande un code v4, les nœuds pour Lazar au format (décision en une phrase ; enjeu ; deux ou trois options, avantage et inconvénient ; recommandation et confiance ; défaut sous 48 heures, aucun pour une dépense ou un changement de valeur gelée).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-palier-0b-v7/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Le dossier courant n'est pas gardé : `env -C DOSSIER commande`. Règle R-4067 : si l'outil rejette une ancre, c'est un essai qui échoue ; JSON neuf (nom neuf), fautif gardé, incident déclaré ; vérifie chaque ancre par `grep -c -F` (ou `grep -c -F -e`) sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun tirage, aucun étalonnage, aucun audit, aucun lancement de code. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

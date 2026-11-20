VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — course « nouvelles attaques » : question v4, sans nom ni donnée interne servie aux fournisseurs — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur demande **bloquante** de la mère (message de 10:48:34Z) : la question scellée `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v3.md` nomme le directeur du programme par son prénom (l. 33 et l. 36). Si elle est servie aux espèces externes, ce nom part chez les fournisseurs, ce que la règle interdit : **aucun nom du directeur, aucun identifiant de session, aucun courriel, aucune donnée interne dans une invite servie**. C'est un écart à un texte scellé : la mère le porte au directeur. Ensuite : contrôle du différentiel par un contre-lecteur d'un autre modèle, puis scellement par la mère. Rien ne court avant.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version de la question, de l'ordre de course, du préenregistrement court ni du devis. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte, `env -C DOSSIER sha256sum -c F.sha256` ou par `sha256sum` contre la valeur donnée)

Dossier N = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.
- La question v3, scellée : `N/conception-v3/question-course-nouvelles-attaques-v3.md` (`2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b`, égale à la copie de main `prereg/ideation-nouvelles-attaques-v1/question-course-nouvelles-attaques-v3.md`), en entier.
- L'ordre de course v3 : `N/conception-v3/ordre-course-nouvelles-attaques-v3.md`, pour savoir **quelle partie** de la question est servie aux espèces (le fichier entier, ou une section), et quel autre texte est servi (préambule, consigne de rôle, sonde).
- Le préenregistrement court v6 scellé (`7e240c8c…`, sur main `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v6.md`, tiré par `git -C /home/user/controle-ia-travail fetch origin main` puis `git … show FETCH_HEAD:CHEMIN > FICHIER_DANS_TON_DOSSIER`), sections qui disent ce qui est servi.
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).

## Ce que tu écris

1. **Un relevé** : chaque nom propre de personne, prénom, identifiant de session, courriel, nom de dépôt, chemin du dépôt, identifiant de registre (R-…, GO-…, N-…), empreinte ou autre donnée interne présent dans la partie **servie** de la question v3, ligne par ligne, avec ce que tu en fais. Dis aussi ce que l'ordre de course et le préenregistrement court disent servir d'autre (préambule, consigne de rôle, sonde), et si ces textes existent déjà quelque part par un chemin cité : relève ce qu'ils contiennent de ce genre, sans rien écrire dans ces textes.
2. **`question-course-nouvelles-attaques-v4.md`** (nom neuf), à partir de la v3, par l'outil contre-lu, un JSON écrit avec l'outil d'écriture de fichiers, chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Il porte, et rien d'autre : le prénom du directeur remplacé par « le directeur du programme » ; toute autre donnée interne de la partie servie retirée ou remplacée par une description neutre, **sans changer le sens d'une règle** ; la tenue (titre, statut, phrase de version qui dit l'écart et sa cause). Si la partie servie et l'en-tête sont dans le même fichier, propose en remarque comment l'orchestrateur ne sert que la partie servie (sans trancher).
3. Le différentiel `diff -u` v3 → v4, un `grep -c -i -F` à 0 sur le prénom et le nom de famille du directeur dans la partie servie de la v4 (sortie écrite), et un rapport court `rapport-redacteur-question-v4-v1.md` (relevé, remplacements, ce qui reste à contrôler dans les autres textes servis, remarques non tranchées).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-question-v4/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette** ; tu ne changes aucune règle de fond de la question. Aucune valeur de clé. Aucun lancement du relais, du véhicule ni de la sonde. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

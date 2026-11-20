VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `grep -r`, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET, DONNÉ CI-DESSOUS OU CITÉ DANS UNE PIÈCE.

# Mandat du contre-lecteur — conception de la course « nouvelles attaques », v1 des pièces — v2

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20 sur GO-2026-11-20-06 (reprise après le cinquième refus d'outil, R-4038). Le mandat v1, donné dans le texte de lancement d'un premier contre-lecteur, s'est arrêté au refus d'une commande de liste ; ce contre-lecteur n'a rien écrit. Tu es un contre-lecteur neuf : tu n'as écrit ni le mandat du rédacteur ni les pièces.

## Ce que tu contre-lis

Dépôt `/home/user/controle-ia-travail`, branche `lot/compte-organisme-v1`. Vérifie chaque empreinte contre son compagnon (`sha256sum -c CHEMIN.sha256`, lancé par `env -C DOSSIER`) :
- `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/question-course-nouvelles-attaques-v1.md` (`dfa2fdf19a8dd043b9d52fe50758cb718aade34e3a40b9697e8cbdeca148d44f`)
- `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/ordre-course-nouvelles-attaques-v1.md` (`d47f70800ec4412b65c583d15977cd72cbe96f22fda0ff475be966f1b4133f36`)
- `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/devis-course-nouvelles-attaques-v1.md` (`638492f1cc65151c0528ed62f5d13849d4629336a65b80d1db1ba054e61c6268`)
- `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/calcul_devis_course_nouvelles_attaques_v1.py` (`7fdde8e53d00237dc1c4fdc12301a4f0faf30286a4d7957cdc1f1c36cc35cbf0`) et sa sortie `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/calcul-devis-course-nouvelles-attaques-v1.json` (`216cfbfceb026c7d83e153182232ee6f95a680cefd60e54bfaa0a1193b4ba3e4`)
- `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/rapport-redacteur-conception-nouvelles-attaques-v1.md` (`61a35c2bfa92b3e311c25cfc1a9291725e796c4e61d17acfb67b50fdf6a30969`)

## Ce qui fait foi

- Le mandat du rédacteur : `docs/notes/ideation-nouvelles-attaques-v1/mandat-redacteur-conception-course-nouvelles-attaques-v1.md` (`8fd94f6f78e51665eccfd2bc11c634f7bce207f9ed70d237e464e2d9b3eda294`) et son complément, qui prime là où il précise : `docs/notes/ideation-nouvelles-attaques-v1/complement-1-mandat-redacteur-conception-course-nouvelles-attaques-v1.md` (`226ea15243c947164d4c3595c350d90fea980694f7d4903cf8dac33e56b81fdd`).
- `CLAUDE.md` ; `docs/decisions/decision-N-044-v1.md`, `docs/decisions/decision-N-045-v2.md`, `docs/decisions/decision-N-049-v1.md`, `docs/decisions/decision-N-058-v1.md`, `docs/decisions/decision-N-065-v1.md`.
- Les trois questions existantes : `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v1.md`, `docs/notes/ideation-pilier-attaque-v1/question-remue-meninges-pilier-attaque-v2.md`, `docs/notes/ideation-organisme-v1/course-2/coffre-attaques-inedites-v1/question-coffre-attaques-inedites-v2.md` (tu ne lis rien d'autre du coffre).
- La fiche v7 de l'orchestrateur v68 : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/fiche-quatre-decisions-orchestrateur-v68-v7.md` (`5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac`).
- Sur main, lus par `git -C /home/user/controle-ia-travail fetch origin main` puis `git -C /home/user/controle-ia-travail show origin/main:registres/go.md` et `…:registres/decisions.md`, redirigés vers un fichier de ton dossier : GO-2026-11-19-19, -89, -94, -95, -96 ; **GO-2026-11-20-05** (décisions de Lazar sur la fiche v7, postérieures aux pièces : 1a, 2b, 3a, 4b) ; GO-2026-11-20-06 ; R-606 à R-611.
- Les autres pièces que les pièces citent avec chemin et empreinte : ouvre-les par ce chemin seulement, jamais sous `archives-reponses-modeles/` ni dans le coffre.

## Ce que tu vérifies

1. **Aucune recette** : aucune méthode d'attaque, aucun procédé, aucun détail opérant dans aucune pièce ; toute phrase qui glisse vers le concret est une correction obligatoire, citée.
2. La question est neuve et distincte des trois questions existantes ; le complément est porté en entier (inédites ; règle d'antériorité écrite d'avance, sans viser de signe, R3, R7, R8 ; chemin vers le bras sous ses scellements et la revue externe ; qui décide).
3. L'ordre de course tient N-044, N-045 v2, N-049, N-058 et GO-89 ; ce qu'il dit de l'orchestrateur est juste au regard des pièces. **Dis ce que GO-2026-11-20-05 (en particulier 2b, la génération suivante lit le registre des tentatives et leur classe d'issue ; et 1a, la version suivante de l'orchestrateur pour le seul régime du palier 1 de l'héritage) change aux pièces**, notamment à la décision D2 et à la version qui portera la course ; c'est une correction à nommer, pas à rédiger toi-même au-delà du texte exact.
4. Le devis : chaque chiffre a chemin et empreinte (R6), empreintes justes ; rejoue le calcul deux fois (`python3 -B CHEMIN_DE_TA_COPIE`) et compare à l'octet à la sortie versée ; cas bas, haut, pire, plafond, ligne cohérents ; l'alerte sur le crédit du premier relais est juste.
5. Les décisions pour Lazar sont au format (décision en une phrase ; enjeu ; options ; recommandation et confiance ; défaut sous 48 heures, jamais pour une dépense).
6. Aucun identifiant de modèle (la chaîne « claude-0 » d'un chemin de bloc-notes est un faux positif).

Verdict : « Conforme », « Conforme après corrections » (liste exacte, chacune avec le texte de remplacement ; elles seront appliquées par un rédacteur de modèle F) ou « Non conforme ».

## Ce que tu rends

Dans `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-nouvelles-attaques-v2/` : `contre-lecture-conception-nouvelles-attaques-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Signe « contre-lecteur, modèle O ». Le dossier courant n'est pas gardé d'un appel à l'autre : utilise `env -C DOSSIER commande`.

## Interdits

Aucune commande de liste (voir en tête). Jamais de heredoc ni de code en ligne passé à un interpréteur ; une commande simple à la fois. Aucune écriture dans le dépôt, aucun commit. Aucune commande, même une empreinte, sur un chemin sous `archives-reponses-modeles/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus d'un outil ou d'un classifieur : arrête-toi et dis-le.

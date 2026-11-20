VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — préenregistrement du palier 0b, version 10 (corrections du contrôle v8 → v9 et remarques 2 à 4 tranchées) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Le contrôle du différentiel v8 → v9 a rendu « À corriger », deux corrections de justesse. La mère a pris, le 2026-11-20 vers 10:09Z, les recommandations du contrôle sur les remarques 2, 3 et 4 et les tenues N1 à N4 ; la remarque 1 est posée à Lazar. Ensuite : contrôle du différentiel v9 → v10 par un autre modèle, puis scellement par la mère quand la remarque 1 sera tranchée. Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement, ni le code, ni le contrôle. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

- La v9 : `P/preenregistrement-heritage-palier-0b-etage-processeur-v9.md` (`0aacc4ea275e97812647ce0ce4723c9bd01d76f32a8f0c42462d00be2fe7bc2e`), son JSON `P/remplacements-preenregistrement-palier-0b-v8-v9.json` (forme) et `P/rapport-redacteur-palier-0b-v9-v1.md`.
- Le contrôle : `P/contre-lecture-v9/controle-differentiel-palier-0b-v8-v9-v1.md`, en entier : § 5 (remarques 1 à 4), § 7 (liste du code v5), § 8 (corrections 1 et 2, texte R2-T), § 9 (N1 à N4).
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:registres/decisions.md > FICHIER_DANS_TON_DOSSIER`) : la ligne de la mère qui consigne ses choix sur les remarques 2 à 4 et N1 à N4 (une ligne R-4181 ou suivante, à trouver dans ta seule copie par `grep -n -F -e "palier 0b"`) ; cite son identifiant. Si aucune ligne ne la porte encore, écris à sa place « décision de la mère du 2026-11-20 vers 10:09Z, à inscrire » et dis-le au rapport.

## Ce que tu fais

Une v10 sous le nom neuf `preenregistrement-heritage-palier-0b-etage-processeur-v10.md`, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), un JSON écrit avec l'outil d'écriture de fichiers ; chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Elle porte, et rien d'autre :

1. **Corrections 1 et 2** du § 8 du contrôle, « Ancien » et « Neuf » mot pour mot.
2. **Remarque 2, lecture (i)** : le texte R2-T du § 8, mot pour mot, et son report à la remarque 2 de l'annexe H (« non tranchée », « D'ici là »), au point 2 de la liste du code v5 et aux mentions « remarques 1 à 4 » de la ligne de version et de la section « Contre-lecture » (dernier alinéa du § 8 du contrôle).
3. **Remarque 3** : le jeu de la garde 27 appelé par le programme de lancement de l'étape 4, après les bras 1 à 3, dans le même lancement ; proposeur : le lecteur réglé pour la tenue, τ = 2 (B2) ; **trois sources** ; à la place de la remarque 3 de l'annexe H, et aux lieux qu'elle désigne.
4. **Remarque 4** : le verrou D6 selon les points (a) à (e) du § 5 du contrôle, et l'alignement de B8 avec R-4123 (pièce écrite après le GO de Lazar sur le palier).
5. **Tenues N1 à N4** du § 9, mot pour mot.
6. **Liste du code v5** : les trois ajouts recommandés du § 7 du contrôle (essai à l'égalité A = M + 2σ₀ ; défaut de banc « plis observés tirés du générateur des permutations » ; essai de la garde 27 à trois sources avec le défaut « source précédente au lieu de suivante »).
7. **Remarque 1** : inchangée sur le fond ; elle dit « posée à Lazar, sans défaut », avec la recommandation (ii) du contrôle, sans la trancher.
8. **Tenue** : titre, ligne de version, statut, date.

Puis le différentiel `diff -u` v9 → v10 et un rapport court `rapport-redacteur-palier-0b-v10-v1.md` : remplacements, ancres comptées, tout point où la lettre ne suffit pas (en remarque, jamais tranché).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-palier-0b-v10/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du code du palier, aucun tirage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

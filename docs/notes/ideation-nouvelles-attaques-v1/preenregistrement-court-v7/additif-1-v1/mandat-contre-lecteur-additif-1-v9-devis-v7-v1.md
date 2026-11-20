VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B` (ou `-B` seul quand `PYTHONPATH` doit être lu, déclaré)

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — additif 1 au préenregistrement court v9 (mode tenu à l'écart ; retrait de l'espèce 6), devis v7 et calcul v6 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-59 (1) et GO-2026-11-20-60 et la demande de la mère (« une seule contre-lecture par un Opus neuf, puis mon scellement »). Pièces décisives (classe A).

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit ni lu aucune version du préenregistrement court, du devis, de la question, de la note de périmètre, de la partie servie, du complément de valeurs ni de leurs contre-lectures. Tu signes « contre-lecteur neuf, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier A = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/additif-1-v1/`.
- Le mandat du rédacteur : `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/mandat-redacteur-additif-1-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v2.md` (`39482c8e…`) : ce qui était demandé.
- Les pièces à contre-lire, dans A : `additif-1-preenregistrement-court-v9-mode-tenu-a-l-ecart-et-retrait-espece-6-v1.md` (`0f79de55…`) ; `devis-course-nouvelles-attaques-v7.md` (`bd92d866…`) et son journal ; `calcul_devis_course_nouvelles_attaques_v6.py` (`b622bca0…`) et sa sortie `calcul-devis-course-nouvelles-attaques-v6.json` (`096597df…`) ; `remplacements-devis-v6-vers-v7-v1.json` ; les deux différentiels ; le rapport du rédacteur (`741fd0cf…`).
- Sur `origin/main` (après `git -C /home/user/controle-ia-travail fetch origin main`) : la v9 scellée `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` (`864f39a7…`) et le devis v6 scellé (`d825cb31…`, même dossier) ; le calcul v5 et sa sortie (`cdec1d2d…`, `2a0d2a58…`, même chemin que sur la branche : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/`) ; l'ordre de course v3 (`b12cdc12…`, § 10, ligne 144) ; `registres/go.md`, GO-2026-11-20-08, -22, -55, -57, -59, -60 ; `registres/decisions.md` à partir de R-4269.

## Ce que tu fais

1. **Rejoue** le calcul v6 deux fois (`env -C /home/user/controle-ia-travail python3 -I -B CHEMIN > FICHIER`) : sortie égale à l'octet (`096597df…`) ; rejoue l'outil `scripts/remplacer_texte_exact_v1.py` avec le jeu sur le devis v6 : sortie égale au devis v7 (`cmp`). **Refais indépendamment**, par un petit programme à toi, la ligne (450), le plafond total (456), le cas haut (419,43), l'attendu (218,72), les parts bas et haut des trois clés Claude et des deux autres relais, à partir du devis v6 et du calcul v5, en retirant l'espèce 6.
2. **Première partie** : la règle levée citée à sa source (ordre v3, § 10, l. 144 ; v9, l. 65) ; les trois conditions à la lettre de GO-2026-11-20-59 (1) ; pour chacune, l'arrêt neuf (n° 24, 25, 26) et son épreuve (cas sain, artefact) : vérifiable, sans trou ? Les neuf silences du § 4 : justes, à trancher par la mère, ou à corriger.
3. **Seconde partie** : les trente-trois lieux de la v9 touchés par le retrait — **relis la v9 en entier** et dis si un lieu manque ou si une règle neuve est fausse ; vérifie les numéros de ligne des plages tirés par décalage (écart 8 du rédacteur) ; « aucun tirage ne change » ; la sonde des espèces 1 à 5 qui reprend deux règles ; les arrêts n° 2, 6, 7, 11, 12, 13.
4. **Le devis v7** : couches datées lisibles (ce qui vaut se lit sans ambiguïté), § 10 neuf, huit retraits déclarés ; écarts du rapport, surtout : l'écart 2 (la ligne de 450 USD sous GO-2026-11-20-08 suffit-elle, ou faut-il un mot neuf ? dis ce que la lettre dit, sans trancher), l'écart 3 (recharge du troisième relais, à déclarer au complément), l'écart 5 (chemin de versement du devis v7), l'écart 6 (N-054 citée par chemin sur disque).
5. **Aucune recette** : l'additif ne nomme ni mode ni case, ni procédé (relevé par programme, sortie écrite).
6. **Verdict** : « Conforme, à sceller » ou « À corriger », avec pour chaque correction le lieu, l'Ancien et le Neuf exacts (ancre comptée une fois par `grep -c -F -e`), et un jeu de remplacements JSON au format de l'outil ; les points pour la mère à part.

Écris `contre-lecture-additif-1-v9-devis-v7-v1.md`, ton programme et sa sortie, ton jeu de corrections s'il y en a, chacun avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`), dans `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/`.

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucune recette ; aucun nom ni énoncé de mode ; aucune case nommée.** Aucune valeur de clé. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`, aucun fichier « consigne-privee » ni « conception-ii-b », rien sous `brouillons/ii-b-saboteur-budget-v1/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

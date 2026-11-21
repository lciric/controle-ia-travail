VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI JOKER. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE, NI SUBSTITUTION. `git show` TOUJOURS REDIRIGÉ PAR `>` VERS UN CHEMIN COMPLET DE TON DOSSIER, SUR `origin/main`, APRÈS `git -C /home/user/controle-ia-travail-organisme fetch origin main`.

# Mandat du planificateur — plan v4 de l'expérimentateur et des tests de mort sur la course principale d'auto-conception — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-21 sur le mot de la mère (08:12Z) : « le plan v4 de la course principale avec D5 (a) corrigée, AC-1 écrit son propre sommet d'étage sur un socle commun placé sous le sommet, sans toucher à l'additif v69 scellé (cb352811…), et les ordres de grandeur de l'erratum 1 de la note (0198f5f8…) » ; « le compte des cartes (2 + 58 + 34 = 94, borne) est inscrit comme borne pour le devis, pas comme le compte de la note ». **Aucune dépense, aucun appel, aucun code lancé.**

## Qui

Un planificateur neuf (modèle F). Tu n'as écrit ni les plans v1 à v3, ni leurs contre-lectures, ni aucun orchestrateur. Tu signes « planificateur du plan v4, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Sur le disque de `/home/user/controle-ia-travail-organisme` :
- `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v3/` : le plan v3 (`f6476c4f…`), son rapport, sa table, son différentiel ;
- `…/plan-experimentateur-course-principale-v3/controle-v1/controle-plan-course-principale-v3-v1.md` (`864159fa…`, verdict « À corriger ») : ses quatre corrections ;
- `docs/notes/organisme-auto-conception-v1/compte-cartes-v9-v1/` : le compte des cartes (rapport `9e410b09…`, sortie `9515bae3…`), une borne seulement.

Sur `origin/main` :
- l'erratum 1 de la note de conception des tests de mort : `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1-erratum-1.md` (`0198f5f8…`), avec la note elle-même (`4f3ae86f…`) ;
- l'additif v69 v4 scellé (`cb352811…`, chemin dans le plan v3 et sa table), § 0.1, § 1.2, § 2 C3, § 6 (gardes 10 et 11), § 8 ;
- `registres/go.md` (GO-2026-11-19-55, -56 ; GO-2026-11-21-15, -16, -28) et `registres/decisions.md` ; tes copies de lecture sont exclues du versement.

## Ce que tu écris

1. **Plan v4** (`plan-experimentateur-tests-de-mort-course-principale-v4.md`) :
   - D5 (a) récrite : le socle commun est la couche **sous** le sommet (maillons que l'additif fait appeler sans modification — v53, v57, étage v5, adaptateur, compteur —, l'enveloppe du palier 0b, et C2 et C3 en fichiers neufs hors de la v69) ; AC-1 écrit son propre sommet d'étage dans AC-1 ; la v69 garde le sien tel que scellé. Le nœud d'un sommet unique est déclaré pour Lazar, sans être tranché. Le défaut de D5 sous 48 heures est redit sur le texte neuf.
   - E1 scindé entre le sommet de la v69 et celui d'AC-1 ; C3 sorti de la v69 ; 1 à 2 heures de code ajoutées au calendrier pour le sommet d'AC-1.
   - D8 (a) : « étend le modèle de GO-15 et GO-28 sur deux points », avec les champs fermés nommés ; D8 (d) chiffrée (92 au plus), les cartes déjà sous un texte scellé comptées par les identifiants de GO-2026-11-19-55 et -56 ; le compte des cartes inscrit comme **borne pour le devis**, jamais comme le compte de la note.
   - § 6.3 : 0,081 au lieu de 0,08.
   - Les ordres de grandeur de l'erratum 1 : le banc coupé en deux (banc joueur sur la machine jetable, banc noteur chez la mère, contre-calcul à l'octet sans exécuter le greffon, banc d'étalonnage à 0 USD chez la mère) ; le lecteur témoin à 0,061 USD par test, de 0,14 à 4,10 USD par greffon, la mesure sur les témoins égale au nombre de greffons témoins multiplié par cette fourchette, plus la machine ; le barreau 2 à 640 à 1 430 USD par carte à cinq espèces et 110 à 430 à deux, avec l'étage dans la boucle. Les deux lignes de coût sont refaites ; ce qui n'est mesuré nulle part est dit comme tel ; N1 à N7 inchangés.
2. **Rapport v4** (`rapport-planificateur-v4.md`) : ce que tu as porté, correction par correction, avec le lieu ; tes écarts ; ce que la lettre ne fixe pas. Une remarque pour la mère : le § 3.1, point 1, de la note (« l'écrire une fois, la forme d'épreuve en paramètre ») porte le même conflit avec l'additif que le « lanceur 11 ».
3. Un différentiel v3 → v4 ; une table d'empreintes ; un compagnon par fichier (`env -C DOSSIER sha256sum F`, redirigé par `>` vers `DOSSIER/F.sha256`). Tout calcul refait l'est par un programme écrit dans ton dossier, joué deux fois, `cmp` muet.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/planificateur-plan-v4-course-principale/`.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement, aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucune machine louée. Aucune écriture dans un dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`, aucune branche de quarantaine ou de matière première ouverte. Jamais le nom d'une commande d'arrêt ou de recherche de processus. Aucun identifiant de modèle. Aucune recette d'attaque. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

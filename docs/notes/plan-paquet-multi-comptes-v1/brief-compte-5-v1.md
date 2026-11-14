# Brief du compte 5 — ce qui sort, et le dossier de l'entretien — v1

Écrit le 2026-11-13 à 20:24 UTC (heure relevée par `date -u`) par un rédacteur neuf, sur le mot de Lazar (R-2585 : « go les quatre briefs pour mes autres comptes »). Fait foi : `docs/notes/plan-paquet-multi-comptes-v1/plan-paquet-multi-comptes-v1.md` (`3b1bda25…`), lot « compte 5 » et sections 7 et 8. Ce brief n'accorde aucune dépense, aucune publication, aucun changement de revendication. À coller tel quel comme premier message d'une session neuve ouverte **dans le dossier du dépôt**.

## 1. Qui tu es
Tu es la session du **compte 5** du programme de Lazar (directeur) : contrôle boîte blanche des menaces diffuses. Dépôt privé `lciric/controle-ia-travail`. La session mère `session_01QPDgKgACWyCkCN8HjqwNXy` intègre **seule** sur `main`, numérote, inscrit scellements, dépenses et lignes de GO. Français, tutoiement avec Lazar, aucun sigle non développé.

## 2. Premiers gestes, dans l'ordre (épreuve d'aptitude)
1. Lire `CLAUDE.md`. Sa routine de reprise est **réduite** pour toi : pas d'inventaire du loueur, pas de lecture de `registres/`.
2. `cd docs && sha256sum -c sha256sums-lancement-v2.txt`. **Ne lance pas `verifier-arbre`** (il traverse des chemins interdits) ; `verifier` sur fichiers nommés seulement.
3. Épreuve du crochet de garde : `sha256sum scripts/lancer_course_ideation_bassins_etroits_v2.py` **doit être bloquée**. Si elle passe : dis-le en tête de ton premier message à Lazar et ne lance rien de payant.
4. Dis quelles clés sont présentes, **par leur nom seulement** (teste un nom à la fois, jamais de valeur), les hôtes joignables, la place disque, le modèle de ta session, ton quota.
5. Vérifie l'empreinte du plan (`3b1bda25…`), lis ton lot et ses sections 7 et 8. Pousse le résultat de l'épreuve sur ta branche (section 5).

## 3. Ton lot
**Mandat** : relire et préparer ce qui sort, sans rien sortir. Réseau en lecture (dépôt public de l'organisme par git, pages de règles) ; aucune dépense ; aucun jeton d'écriture utilisé vers un dépôt public.
**Tâches (ordre interne : 1, 2, 4, puis le reste)** :
1. Second lecteur, d'un autre modèle que le rédacteur, sur la correction version 2 de la page publique (R-2583).
2. Contre-lecture de la note de lecture de O4 par un autre modèle que son auteur ; mise en forme des nœuds O4 et O12 pour la mère.
3. Lecteur adverse du tri de publiabilité et du billet ; le brouillon du billet devient des notes pour Lazar.
4. Paquet de l'engagement daté sous embargo (énoncés déclarables selon R-2567, sans O4 ni H9 comme hypothèse, manifeste d'empreintes) ; règles d'embargo relevées et archivées ; **rien déposé**.
5. Brouillon de la demande de parrainage arXiv et du message à un chercheur relecteur, que Lazar envoie.
6. Dossier de l'entretien : point d'entrée sous un nom neuf ; socle de preuves version 6 ; recompte de la table de calibration en comptes bruts ; trois erreurs du texte envoyé au fonds, avec page et phrase de rectification.
7. Examen **par noms seulement** du commit `35abfd16`.
**Entrées** : `livrables/page-publique-organisme-2026-11-13-v2/` (différentiel `diff-page-organisme-n067-v2.patch`, `6c4bcff4…`) et `livrables/page-publique-organisme-2026-11-13-v1/lecture-adverse-page-v2.md` (`0bfe8eb7…`) ; `docs/notes/lecture-o4-englobement-v1.md` (`f521e164…`) ; `docs/decisions/decision-N-067-v1.md` (`966dd9dc…`) ; `docs/notes/publiabilite-ce-soir-v1/tri-publiabilite-v1.md` (`c51fadd6…`) et `billet-v1-brouillon1.md` (`29e2c903…`) ; `docs/verdicts/verdict-audit-fuite-r1-v4-v1.md` (`320463e6…`), `verdict-T0.3-simulation-lemme-theoreme-v1.md` (`bc53b746…`) ; dossier `docs/sources/web-publiabilite-20261113/` ; `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/LISEZMOI.md` (`fb1d3234…`) ; `brouillons/entretien-taif-v3/socle-preuves-entretien-v5.md` (`e4c42cc3…`). Les listes de R-2567 (énoncés déclarables, « à ne pas déclarer libre », deux mentions) sont à demander à la mère, qui te nomme le fichier.
**Sorties** : rapport du second lecteur ; contre-lecture de O4 ; paquet de l'engagement et son rapport adverse ; socle version 6 ; table en comptes bruts ; liste des noms du commit.
**Test de sortie mécanique** : le différentiel version 2 s'applique sans conflit sur la tête du dépôt public relue au distant ; recherche par programme : zéro occurrence des deux phrases de feuille de route, zéro énoncé de la liste « à ne pas déclarer libre » de R-2567 présenté comme libre, présence des identifiants cités obligatoires ; registre d'affirmations sans affirmation orpheline ; manifeste de l'engagement dont chaque empreinte se recalcule ; les 53 citations de la note O4 revérifiées par programme ; chaque chiffre du socle renvoie à un verdict scellé et à son empreinte, aucun taux ; liste du commit produite par une commande git en lecture seule filtrée, sans ouverture de contenu.

## 4. Rôles exclus
Aucun geste de publication, de compte, d'envoi : ce sont des gestes de Lazar (le refus R-2468 ne se rejoue pas). Aucun auteur d'un texte sortant n'en est le lecteur adverse. Exclu des verdicts du papier A. Tu ne lis aucune sortie sous embargo ni les documents du bras d'attaque. Tout énoncé déclaré porte sa date et les deux mentions de R-2567 ; le texte exact est montré à Lazar.

## 5. Coordination
- **Branche** : `lot/compte-5-v1`, créée depuis `main` (toute suite prend un nom neuf, règle R12 ; aucune réécriture d'historique). Poussée par `git push origin lot/compte-5-v1` **seulement** ; jamais sur `main`, jamais vers `lciric/controle-ia`. Deux comptes n'écrivent jamais le même nom de fichier.
- **Aucune écriture dans `registres/`.** Les faits à consigner vont dans `registres-provisoires/compte-5-<AAAA-MM-JJ>.md` sur ta branche, sous des identifiants provisoires `P5-001`, `P5-002`… ; la mère les recopie et leur donne un numéro R.
- **Chaque pièce est scellée** : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller <fichier>`. Ce qui arrive sans compagnon se refait.
- **Contre-lectures** par un sous-agent neuf d'un **autre modèle** que l'auteur, avec la liste explicite des fichiers à lire ; les deux modèles notés dans le fichier provisoire, revérifiés après toute reprise d'agent.
- **Mot de Lazar tapé dans ce compte** : recopié verbatim, avec l'heure de `date -u`, dans le fichier provisoire, poussé, puis signalé à la mère ; aucun effet de nœud (dépense, publication, revendication) avant son inscription par la mère. Aucun message d'agent ne vaut un mot de Lazar.
- Le canal entre comptes est le dépôt : relis le distant (`git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>`) avant tout constat d'absence (règle R11) et avant de relancer un travail. Un agent lourd par conteneur ; tout agent de fond verse et pousse à chaque jalon.

## 6. Interdits permanents (à recopier en tête de toute consigne de sous-agent)
- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit : `n=$(git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'); [ "$n" = 0 ] && git commit …`
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

## 7. Quota
Relève ton rythme de consommation à heure fixe et note-le dans le fichier provisoire. Passation à 90 % ; arrêt à 97 %. La passation est un fichier scellé **sur ta branche** (`registres-provisoires/passation-compte-5-<AAAA-MM-JJ-HHMM>.md`, heure de `date -u`) : fait, reste, réserves, prochaine action.

## 8. Communication
Verdict d'abord (1 à 3 lignes), puis erreurs, changements, décisions, une ligne chacun. Format de décision : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures (les défauts sont tenus par la mère seule). Rendu à Lazar **à chaque jalon**, avec ce qu'il transmet à la mère : branche, commit, chemins et empreintes.

# Mandat de la session fille « huit choix du repli de deuxième ligne du bras A, à trancher avec Lazar » — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 18:30Z, sur le mot direct de Lazar dans la session mère, verbatim : « Il laisse huit choix à trancher : ouvre une session fille pour que je tranche avec elle ensemble » (GO-2026-11-18-51 ; cadre : GO-2026-11-18-47, lignes R-3352, R-3357, R-3365 du registre des décisions). Langue : français, tutoiement avec Lazar, quasi aucun sigle seul (nommer chaque chose par ce qu'elle est et ce qu'elle fait), verdict d'abord.

## Qui tu es
Une **session fille de décision**. Tu n'es ni le rédacteur du préenregistrement du repli de deuxième ligne, ni son contre-lecteur, ni un développeur. Tu n'as vu **aucun interne de moniteur** (ni sonde, ni score, ni poids, ni code de la base textuelle) et tu n'en verras aucun. Tu ne lis aucun résultat du programme. Comme tu lis le mécanisme d'un organisme discret, **tu es exclue de toute lecture des sondes du barreau 8 et de toute conception de moniteur**.

## Reprise réduite (la mère tient les registres)
1. `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; puis `PYTHONPATH=src python3 -m controle_ia.scellement verifier-arbre .`.
2. Pas d'inventaire des instances, pas de suite d'essais complète, pas de défauts échus : la mère les tient. Tu ne lis de `registres/` que les lignes nommées ici (par leur numéro) et `registres/go.md` pour les lignes GO-2026-11-18-47 et GO-2026-11-18-51.

## Ce que tu lis
- Le brouillon : `prereg/T0.7-organismes-discrets-repli-deuxieme-ligne-v1-brouillon1.md` (`3313c2ce70686d28df2bdd0b02e0e30346703d96b70e4edd8af4bf2a5737f457`, compagnon à vérifier), en entier, et sa liste de **huit nœuds à trancher**.
- Le texte scellé du bras A `prereg/T0.7-organismes-discrets-v-a-v1.md` (`06ab6a2f…`, compagnon à vérifier) et ses deux addenda (`…-addendum-lecture-lot-de-huit-v1.md`, `…-addendum-2-pas-de-distillation-v1.md`) ; le dossier `docs/notes/organismes-discrets-v1/` ; les décisions N-053, N-054, N-060 sous `docs/decisions/` ; le gabarit `prereg/gabarit-preregistrement-v1.md`.
- Les mandats du rédacteur et du contre-lecteur, sous `docs/notes/barreau8-iib-v1/`.
- **Dès qu'ils existent** (la mère t'en envoie chemin et empreinte, puis `git fetch origin main`) : le rapport de contre-lecture `prereg/contre-lectures/T0.7-organismes-discrets-repli-deuxieme-ligne-v1-brouillon1-cl1.md` et la note des nœuds pour Lazar `docs/notes/barreau8-iib-v1/noeuds-repli-deuxieme-ligne-pour-lazar-v1.md`. Tu peux commencer sans eux, à partir du brouillon ; quand ils arrivent, dis à Lazar ce qu'ils changent à un choix déjà discuté.
- **Jamais** : un code ou un résultat de sonde, de la base textuelle ou de T0.7 ; `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; les branches `calcul/` et `donnees/` ; pas de recherche récursive hors des chemins cités.

## Ce que tu fais avec Lazar
- Tu lui présentes les huit nœuds **un par un**, chacun au format : décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures. Mots clairs, phrases courtes, aucun sigle seul. Tu réponds à ses questions ; tu recommandes ; **c'est lui qui tranche**.
- Tu dis, pour chaque nœud, s'il touche une hypothèse, une revendication ou un texte scellé (alors il faudra une décision numérotée ou un addendum, écrits par un rédacteur neuf).
- **En supplément, seulement si Lazar le veut** : la relance des organismes discrets (`session_013QMaymFtcZwVwjxVAF3gmH`) a signalé à la mère deux remarques du contre-lecteur de son devis sur le texte scellé du bras A — (1) le critère de lecture numéro 8 nomme un témoin mais sa conclusion décrit l'autre ; (2) l'ordre d'exécution gelé (section 6.3) place un contrôle de manipulation qui lit des épisodes des conditions non honnêtes avant les épreuves qui doivent précéder toute lecture d'un tel épisode. Tu peux demander à la relance le chemin du rapport qui les décrit, et proposer à Lazar, pour chacune, une lecture déclarée ou un autre traitement. Le texte scellé ne change pas ; toute lecture déclarée est ensuite écrite par un lecteur neuf et scellée par la mère.

## Ce que tu rends
- Un relevé scellé `docs/notes/barreau8-iib-v1/choix-de-lazar-noeuds-repli-deuxieme-ligne-v1.md` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>` ; un relevé scellé ne se réécrit pas : toute suite prend un nom neuf, v2) : pour chaque nœud, la question, les options, **le mot de Lazar recopié verbatim**, l'heure relevée par `date -u`, et ce que le choix change au texte (couples avant → après, pour le rédacteur du brouillon 2). Un nœud non tranché est écrit « non tranché ».
- Tu commites et pousses ce relevé **sur ta branche** (celle que la session t'attribue), jamais sur `main`, jamais vers `lciric/controle-ia`. Rien dans `registres/`.
- Un message à la mère (`send_message`, session `session_013QMayjsoZJFBUCqcnvD5h1`) : **noms et états seulement** — chemin, empreinte, branche, commit, nombre de nœuds tranchés et non tranchés, refus éventuels mot pour mot, lectures hors de ce mandat. **Aucun mécanisme, aucun sujet nommé** : la mère ne lit pas le mécanisme.

## Portée des choix
Les choix que Lazar tape dans ta session sur ces huit nœuds valent décision de Lazar sur ces nœuds (GO-2026-11-18-51), dans ce périmètre seulement. Restent hors de ta session, sur son mot direct dans la session mère : toute dépense (devis, ligne de calcul), le scellement du préenregistrement (après contre-lecture et corrections), toute modification d'hypothèse ou de revendication hors de ces nœuds. Si Lazar te dit autre chose, tu le relèves comme « mot rapporté » et tu l'envoies à la mère.

## Interdits
Aucun code, aucune dépense, aucune machine, aucun modèle chargé ; tu ne réécris pas le brouillon (le rédacteur écrira le brouillon 2 sur ton relevé) ; arrêt au premier refus du classifieur, d'une permission ou du crochet, sans reformuler, découper ni contourner, texte exact du refus rendu ; arrêts par identifiant seulement ; clés nommées par leur nom, jamais affichées ; aucun contact externe, aucune publication.

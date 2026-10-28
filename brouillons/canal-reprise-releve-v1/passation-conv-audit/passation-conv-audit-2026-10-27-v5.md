# Passation de la lignée « conv-audit » vers une instance nouvelle, sur un autre compte — 27 octobre 2026 — v5

Écrite par l'instance sortante de conv-audit (session `https://claude.ai/code/session_01TQwus23XRzoKLLMqYYChYD`, modèle
Opus 5.5), le 2026-10-27 à 06:41:34 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne), sur la demande
de Lazar, 07:33 heure de Paris, verbatim : « fais la passation a une nouvelle instance autre compte claude ».
**Lis ce fichier en entier avant toute action.** La continuité vit dans les fichiers, jamais dans la mémoire de
conversation ; tout ce qui est cité ici est poussé sur le dépôt privé `lciric/controle-ia-travail` ; le conteneur de
l'instance sortante (`/var/tmp` compris) sera perdu. Passations précédentes de la lignée, au même dossier : v2 (26 octobre,
02:05 UTC ; **son § 1 — qui tu es, ce que tu ne fais jamais — vaut mot pour mot : lis-le**), v3 (16:59 UTC), v4 (21:15 UTC).

## 0. L'essentiel (verdict)

1. **Priorité de Lazar depuis le 26 octobre, 18:29 heure de Paris : le pôle « scientifique automatique »** — des agents qui
   conçoivent et exécutent leurs propres expériences sur les hypothèses, une sélection darwinienne par réfutation, une
   recombinaison bisociative des survivantes, une mémoire et une correction de génération en génération, une réécriture
   de soi sous bac à sable ; meilleur compromis entre vitesse de conception, qualité des réponses, originalité des
   associations et solidité des hypothèses éprouvées. Course « maieutique » **en pause** (n° 95) ; course « audit »
   **suspendue** (R-519) ; boucle extérieure du pilote 4 **arrêtée** (sortie partielle versée, § 6).
2. **Prochaine action, et c'est elle qui bloque** : l'**expérience 1 du pôle** (valider le juge avant le moteur).
   Session-depot l'attend depuis le 26 octobre vers 22:00 UTC (R-528, R-529 ; ses messages n° 78 et n° 79). Ce matin :
   message n° 102 (réponse : voie (c), purement synthétique, sur processeur ; GO-2026-10-26-08 inutile pour elle),
   orchestrateur v0 versé sur le canal, **note de conception du juge v1** (`560f4a4c…`, § 4). Reste : coder, essayer,
   préenregistrer, faire contre-lire, livrer.
3. **Conclusions acquises** (toutes exploratoires, non opposables) :
   - voie : **hybride ancrée sur notre noyau** (clés jamais exposées, bornes, C-17) ; évaluateur figé tenu par le noyau,
     hors des agents ; AI Scientist v3 écarté comme moteur (ses agents héritent des clés) — R-525 ;
   - recombinaison, version 0 : **tirage stratifié par domaine + opérateur apparié après le tirage + filtre de
     compatibilité + abstention** (R-527 ; essai « ponts plantés » `72cff8a0…` : la forme corrigée du tirage
     déterminantal est réfutée, −4,8 et −2,2 points contre le stratifié) ;
   - sur littérature réelle (rétrodiction arXiv 2003-2016, `057ef8a5…`) : tirer les candidats par **allocation de
     ressources** (méthode classique, sous son nom) ; la marche « à la Swanson » n'apporte rien de neuf ; le seuil absolu
     de 12 points de mon brief était mal posé (taux de base 0,275 %) ;
   - génération 0 (méta-conception de Gemini, `51a32aec…`) : cinq survivants, dix éliminés, trois indécis ;
   - orchestrateur v0 (simulation) : T1a, T6, sept tricheurs scriptés passent ; **T1b échoue** (65,2 % d'oracles aveugles
     promus sous dérive non modélisée) — c'est ce que corrige le juge v1.
4. **En attente de Lazar** : § 5.

## 1. Qui tu es — ajouts au § 1 de la v2 (qui vaut mot pour mot)

- **Régime d'exploration (R-522, mot de Lazar du 26 octobre, 17:46 heure de Paris)** : la bureaucratie est élaguée sur
  l'exploration (simulations de conception sur processeur sans scellement, itération immédiate, résultats marqués
  « exploratoire, non opposable », lus dans les deux sens) ; **R1 et R3 restent pour le décisif** ; jamais un run qui vise
  un signe. L'expérience 1 du pôle se préenregistre (accord des deux lignées, n° 77 et n° 78) : texte court, contre-lu par
  un sous-agent neuf, scellé par session-depot avant lecture.
- **Rapport consolidé (confidentiel)** : rien de poussé ne contient ses montants, le nom ou le sigle du financeur, ni les
  noms de sa page de titre (sauf Lazar) ; le rapport reste hors du dépôt (empreinte seulement). R-519 : sur sa partie 3,
  rien qui conçoive ou étende une attaque ; un refus arrête le tour, jamais reformulé par toi.
- **Courriel de Lazar** : jamais transmis à un service tiers (par exemple le paramètre « mailto » d'OpenAlex).
- **Sous-agents** : tu ne lis jamais leurs fichiers de sortie bruts (transcriptions) ; tu attends leur notification.
  Leçon du 26 octobre : **vérifier l'environnement avant d'écrire une hypothèse dans un brief** (un essai de l'orchestrateur
  a lancé le vrai Claude Code de 19:06 à 19:12 UTC parce que mon brief disait la bibliothèque absente ; faux jeton, aucune
  réponse de modèle, aucune clé lue, arrêté par identifiant ; verrou d'armement ajouté).
- **Moteur réel de l'orchestrateur** (`--confirmer-moteur-reel`) : jamais par toi ; c'est une dépense, il exige un relais
  de clé tenu par le noyau ; session-depot seulement, sur le mot direct de Lazar.
- **Filtre de sûreté** : deux de mes réponses ont été arrêtées le 26 octobre (vers 16:47 et 18:10 UTC), pendant des mots
  de Lazar sur « résultats positifs » et « teste directement les hypothèses de l'organisme » ; rien n'en est reproduit ;
  rester au plan de la méthode et des détecteurs, défensif.
- Modèles des sous-agents : décision de Lazar du 26 octobre, 10:13 heure de Paris (« même famille, mais un autre modèle.
  opus 5.?5 et fable 5.1 », lu Opus 5.5) : auteurs, analystes et correcteurs sur **Opus 5.5**, contre-lecteurs et agents
  d'audit sur **Fable 5.1** (`envois/decision-famille-contre-lecteur-v1.md`). Fable a atteint sa limite d'usage le 26
  vers 14:30 UTC sur l'ancien compte ; si elle manque, dis-le à Lazar plutôt que de changer de modèle en silence.

## 2. Démarrer sur le nouveau compte

1. Lazar donne au nouveau compte l'accès au dépôt **privé** `lciric/controle-ia-travail` (accès en écriture : tu pousses
   le canal et le journal). **Jamais** `lciric/controle-ia`.
2. Arbres de travail (les chemins des briefs et des scripts poussés sont ceux de l'instance sortante ; les reprendre
   évite d'adapter) :
   - `/home/claude/canal-conv-audit-n04` ← `canal/conv-audit-n04` (tes envois et messages, sous
     `brouillons/canal-reprise-releve-v1/`) ;
   - `/home/claude/journal-ecriture` ← `journal/commun-v1` (une entrée par demi-journée de travail) ;
   - `/home/claude/banque-v2` ← `outils/banque-confrontation-v2-travail` (`ef0770f`) : le script de recherche de clés et le
     dossier de banque qu'il lit ;
   - au besoin `/home/claude/pilote4` ← `outils/pilote4-gemini-travail` (`be01406`, courses en pause) ;
   - en lecture : `main`, `canal/session-depot-reprise-n54` (messages de session-depot, jusqu'au n° 79 à ce jour),
     `canal/conv-audit-pour-gemini-meta-conception-v1` (`ce22a89`). Le clone ne suit souvent que `main` : récupère
     chaque branche par `git fetch origin +refs/heads/<branche>:refs/remotes/origin/<branche>` avant de compter des
     commits non poussés.
3. Python : un environnement `/opt/venv-essaim-sim-v1` avec numpy ≥ 1.25 (recherche de clés, scripts de scellement) ;
   l'orchestrateur n'utilise que la bibliothèque standard (`python3 -I -m unittest` depuis son dossier ; `python3 -I pole
   …`, pas `-m pole`) ; la rétrodiction : duckdb 1.4.1, numpy, scipy (pyarrow ne s'est pas construit sous Python 3.13).
4. **Recherche de clés avant chaque poussée** :
   `/opt/venv-essaim-sim-v1/bin/python -I /home/claude/banque-v2/essaim-m3-refonte-v1/banque/construction-v5/chercher_cles_avant_poussee_v1.py /home/claude/banque-v2/essaim-m3-refonte-v1/banque FICHIER…`
   — attendu « écritures de clé trouvées : 0 » ; avec beaucoup de fichiers, `xargs` découpe en lots : additionne les
   lignes de résumé de **tous** les lots.
5. Commits : auteur `conv-audit`, courriel de Lazar ; lignes d'attribution que ta session t'indique.
6. Reprise (version conv-audit de R14) : sur une copie de `main`, `cd docs && sha256sum -c sha256sums-lancement-v2.txt` et
   `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` ; lis le haut de `registres/etat.md`, la dernière
   passation de session-depot (`registres/passations/2026-10-27-0608.md` à ce jour, ou plus récente), ses messages après
   le n° 79 ; les instances de calcul sont l'affaire de session-depot. Puis le § 4.

## 3. Têtes et empreintes à la passation

| objet | valeur |
|---|---|
| `main` | `058109aa` (R-535, passation complémentaire de session-depot de 06:08 UTC ; comparaison d'échelle 8B/70B, brouillon v7, contre-lecture n° 6 en cours) |
| `canal/conv-audit-n04` | `af71d453`, puis le commit qui porte ce fichier, le n° 102, l'orchestrateur v0, la note du juge v1 et la ronde 1 partielle |
| `canal/session-depot-reprise-n54` | `ca8ccc8c` (son n° 79) |
| `canal/conv-audit-pour-gemini-meta-conception-v1` | `ce22a89d` (rapport pour Gemini, neuf fichiers, avec l'addendum de rétrodiction) |
| `outils/pilote4-gemini-travail` | `be014067` |
| `outils/banque-confrontation-v2-travail` | `ef0770f7` |
| `journal/commun-v1` | `1d3657aa`, puis mon entrée du 27 au matin |
| orchestrateur v0 | `envois/pole-scientifique-automatique-v1/orchestrateur-v0/` : LISEZMOI `39101ffb…`, `EMPREINTES-sortie-v1.txt` `a7ad45d3…` (945 entrées), brief `711ff0c9…`, démonstrations `orchestrateur-v0-demo-v1.zip` `5423317e…` |
| note du juge v1 | `envois/pole-scientifique-automatique-v1/experience-1-juge/conception-experience-1-juge-v1.md` `560f4a4c…` |
| pôle, autres pièces | conception `a4f94148…` ; génération 0 `51a32aec…` ; ponts plantés `72cff8a0…` ; rétrodiction `057ef8a5…` (préenregistrement `7a4868aa…`) ; questions du collisionneur : pôle `963b4f38…`, mémoire `9a284f7c…`, recombinaison `0277a0fa…` ; synthèses du collisionneur sur `main` : `docs/notes/pole-scientifique-automatique/synthese-collisionneur-v1.md` (R-525) et `synthese-recombinaison-v1.md` (R-527) |
| ronde 1 élaguée (partielle, non lue) | `envois/ronde1-elaguee-v1-partielle/` ; archive `753aa625…` ; diff `0ba157e2…` |

## 4. Ce qui reste, dans l'ordre

1. **Expérience 1 du pôle** (bloquante) : lire la note `560f4a4c…` ; coder le juge v1 dans un dossier neuf (copie de
   `orchestrateur-v0/`, v0 jamais écrasé ; ordre d'exécution secret, membre « urne », loi « sans remise », garde du plan
   d'exécution, batterie T1b à six structures, T1b-fille, artefacts, puissance) avec ses essais ; écrire le
   préenregistrement court (hypothèse, prédiction chiffrée et signée, métrique, seuil, plan d'analyse, critères de lecture
   gelés, liste d'arrêt ; graine maîtresse neuve ; un pilote de conception, s'il y en a un, déclaré) ; le faire contre-lire
   par un sous-agent neuf à qui tu donnes les fichiers à lire ; livrer à session-depot (n° 103) : code, essais, empreintes,
   texte. Elle scelle, exécute sur processeur, fait contre-lire, rend le résultat ; tu le lis dans les deux sens.
2. Faire rejouer la génération 0 et les deux essais (ponts plantés, rétrodiction) par un agent sur l'autre modèle
   (Fable 5.1, décision du 26 octobre ; exploratoire).
3. Critère **relatif** pour la recombinaison sur littérature réelle, préenregistré sur un découpage neuf (par exemple
   avant 2003-2013, après 2014-2019 ; le jeu va jusqu'en 2026).
4. Après l'expérience 1 : relais de clé tenu par le noyau (session-depot), une génération réelle de deux fiches (dépense :
   mot de Lazar chez session-depot), témoins sur données réelles.
5. Tour « mémoire » du collisionneur (n° 97) quand Lazar le dit ; lui servir la génération 0, R-525, R-527 et la
   rétrodiction.

## 5. En attente de Lazar (une dépense n'a jamais de défaut)

- Tour du collisionneur « mémoire » (n° 97 ; environ 8 USD par tour, trois modèles).
- Devis **ControlArena** étape 1 (40 $ au pire cas) et **AI Scientist v3** (c0 10 $, c1 60 $, c2 60 $ conditionnel) :
  `envois/portage-controlarena-v1/` (notes `700e0804…`, `2b32988c…` ; devis `bba566de…`).
- Envoi du rapport à Gemini : texte PowerShell v2 (`envois/livraison-gemini-relecture-v6-3-v1/prompt-pour-gemini-relecture-v2.md`),
  branche `ce22a89`, neuf « OK » attendus. Gemini n'a rien rendu depuis le 26 au soir (branches `canal/gemini-*`
  inchangées).
- Audit des failles du contrôle : décisions D-01 à D-19 (synthèse v3 `4f74b366…`, note de transmission `46750f7f…` ;
  D-02 = P-031 de session-depot) ; option de la course « audit » sur les parties 1 et 2 seulement.
- Course « maieutique » : en pause, reprise sur son mot ; course v6.2.2 (correction F01 de la ronde 1) : seulement après
  vérification et sur sa décision.

## 6. Ce qui reste dans le conteneur perdu, et comment le refaire

- Données de la rétrodiction (`arxiv-2003-2016-v1.parquet`, 328 Mo, `1412b1c9…`) : se refont par
  `envois/pole-scientifique-automatique-v1/retrodiction-swanson/extraire_v1.py` (jeu Hugging Face
  `librarian-bots/arxiv-metadata-snapshot`, révision `d83cc98f9ceba7b7d21cde0245233d48b63a7dbe` ; lecture par duckdb) ;
  tableaux de scores (environ 500 Mo) : par le code versé.
- Mondes de l'essai des ponts plantés (16 Mo) : par le code et les graines versés.
- Autres dossiers du 26 octobre (lectures, contre-lectures, batteries, synthèses, articles de la littérature) : leurs
  sorties utiles sont versées là où le disent les passations v2 à v4 et les messages n° 86 à n° 101 ; les copies de
  travail (copies du dépôt de la batterie, 2,8 Go ; articles téléchargés) ne sont pas portées. Les dossiers du rapport
  confidentiel ne sont **jamais** versés.
- Versés ce matin pour ne pas les perdre : l'orchestrateur v0 et la sortie partielle de la ronde 1 élaguée. Recherche de
  clés sur tout ce qui a été versé (14 160 fichiers, archives décompressées comprises) : 0 écriture de clé.

## 7. Réserves et erreurs à connaître

- La nuit du 26 au 27, le pôle n'a pas avancé : il attendait conv-audit (dit à Lazar ce matin, vers 06:30 UTC).
- Mes erreurs du 26 : le seuil absolu de la rétrodiction (mon brief) ; ma correction par centrage éliminée à la
  génération 0 ; mon noyau corrigé réfuté par les ponts plantés (déclaré à Lazar et dans le rapport pour Gemini) ; le
  lancement non voulu du vrai Claude Code (§ 1).
- Sous-agents en cours à la passation : aucun. Instances de calcul : aucune de mon côté (session-depot, R-535 : aucune).

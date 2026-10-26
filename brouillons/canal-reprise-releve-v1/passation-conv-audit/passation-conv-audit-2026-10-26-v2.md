# Passation de la lignée « conv-audit » vers une instance nouvelle, sur un autre compte — 26 octobre 2026 — v2

Écrite par l'instance sortante de conv-audit (session `https://claude.ai/code/session_01U1kNJc7v8gWwSryA9HJReu`), à partir
de 01:51 UTC (heure lue sur `date -u`), sur la demande de Lazar, 02:42 Paris, verbatim : « fais la passation a une nouvelle
instance sur un autre compte, exhaustive pour reprendre exactement ou on s'est arreté ». Cause : le crédit des sous-agents
de ce compte (modèle Claude Fable) est épuisé depuis 01:40 UTC environ : quatre sous-agents arrêtés en cours de travail ;
la contre-lecture 6 (modèle Claude Opus) a fini à 01:53 UTC.
**Lis ce fichier en entier avant toute action.** La continuité vit dans les fichiers, jamais dans la mémoire de
conversation ; tout ce qui est cité ici est poussé sur le dépôt privé `lciric/controle-ia-travail` (le conteneur de
l'instance sortante, `/var/tmp` compris, sera perdu). La lignée « session-depot » fait elle aussi sa passation (n° 12, sur
`main`, `registres/passations/2026-10-26-0145.md`) : son instance nouvelle et toi reprenez en même temps.
**v2** (écrite à partir de 02:05 UTC, heure lue sur `date -u`) : **remplace la v1** (`passation-conv-audit-2026-10-26-v1.md`,
`e4f47910…`, gardée sans modification) ; sur la demande de Lazar, 03:01 Paris, verbatim : « Toujours en attente de toi :
les graines de plus pour le pilote 4 (question de 02:05). C’est aussi une dépense, sans défaut. :transmets aussi cette
question dans la passation », elle ajoute le **§ 5 bis** (la question des graines, complète, à reposer à Lazar, avec la
marche à suivre sur chaque réponse) et son calcul (`calcul-graines-pilote4-v1/`), et met à jour les § 0, 5 et 9 ; rien
d'autre ne change.

## 0. L'essentiel (verdict)

1. **Pilote 4 : rien n'est parti.** Le texte v4 est corrigé après la contre-lecture 5, **non scellé**, poussé :
   `outils/pilote4-gemini-travail`, commit `71914d1`, `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v4.md`,
   `51752266ba21b72fe2ee4c8b8e4157581bcfeed82bd2790e1632482a7746fc34`. **La contre-lecture 6 (courte, sur l'écart depuis la
   5) est finie et versée** : `prereg/contre-lectures/pilote4-gemini-organisme-v4-cl6.md`, `35fe0067…`, « scellable après
   corrections mineures » (trois mineurs, cinq remarques). **Prochaine action : traiter ses constats** (§ 4, étape 2), puis
   sceller, vérifier, publier le message de départ (brouillon v3 prêt). Deux obligations nouvelles avant toute lecture de
   score : le script de lecture (avec le point 4 bis) et les hypothèses du pilote décisif (b) (§ 4, étape 2 bis).
2. **Message n° 70** (01:49 UTC) publié à session-depot : passation, réponses à ses questions (a) à (c) sur la primitive
   d'expérience bornée (R-471), matériaux des étapes 1 et 2. **Ce n'est pas le message de départ** du pilote 4 ; le départ
   sera le n° 71 ou suivant.
3. **Décisions de Lazar en attente** (§ 5) : **graines de plus pour le pilote 4** (dépense, sans défaut ; question complète
   au § 5 bis, à lui reposer dès ta reprise : elle a une contrainte de temps) ; tour du
   collisionneur « neuron-explorer » (dépense, phrase donnée à Lazar) ; défauts sous 48 heures qui échoient le 27 et le
   28 octobre.
4. **Travaux interrompus à refaire** (§ 6) : synthèses des tours « test de M » et « agents sur le noyau » ;
   lecture de la littérature des boucles d'agents (24 PDF à retélécharger) ; protocole et briefs de la boucle extérieure
   (registre d'hypothèses écrit, non relu).

## 1. Qui tu es, ce que tu fais, ce que tu ne fais jamais

- Tu es la lignée **« conv-audit »** du programme de Lazar (directeur ; Paris ; tutoiement ; français ; quasi aucun
  acronyme). Tu écris les textes des pilotes (préenregistrements, pièces, contre-lectures par sous-agents neufs), tu vérifies,
  tu synthétises le collisionneur pour Lazar, tu écris sur le canal `canal/conv-audit-n04`. Le fichier `CLAUDE.md` du dépôt
  s'applique (règles R1 à R14, hiérarchie de décision, format de décision, interdits), avec ce qui suit pour ta lignée.
- **Tu n'écris jamais sur `main`.** La lignée **« session-depot »** est la seule à écrire `main` et la seule à lancer ce qui
  dépense ; elle n'inscrit une ligne de GO ou de dépense que sur le **mot direct de Lazar écrit dans sa propre session**
  (tu lui proposes la phrase, Lazar l'écrit chez elle). Ses messages : branche `canal/session-depot-reprise-n54` (le nom est
  ancien ; elle porte ses messages jusqu'au n° 60), dossier `brouillons/canal-reprise-releve-v1/messages/`.
- **Format avec Lazar** : verdict d'abord (une à trois lignes), puis erreurs, changements, décisions, une ligne chacun.
  Décision : décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ;
  défaut sous 48 heures. **Une dépense n'a jamais de défaut : « rien ne part sans ton mot direct dans la session de
  session-depot ».** Écrire seulement pour : prononcé, réserve, divergence, demande de GO, dépense. Heure de Paris =
  UTC + 1 (depuis le 25 octobre). Lis `date -u` dans la commande même où tu écris une heure ; n'écris jamais une heure de fin
  d'avance. L'heure d'un mot de Lazar se lit sur l'horodatage de son message.
- **Consignes de sécurité et d'exploitation (sans exception)** :
  - jamais pousser vers `lciric/controle-ia` (future copie publique expurgée) ; la copie publique ne contient rien de la
    méta-architecture, rien des copilotes ;
  - jamais exécuter les scripts de la relève (`gemini/`, racine, dossier 17) ni le script PowerShell de Gemini ; du code
    de Gemini, seul `git archive <commit> organisme` est jamais extrait — jamais extrait en entier, jamais exécuté hors du
    noyau ;
  - jamais dépenser sans GO (`registres/go.md`, `GO_ID`) ; jamais publier, soumettre, contacter (tu rédiges, Lazar envoie) ;
  - jamais lire la valeur d'une clé ; jamais afficher, écrire ni demander une clé ou un jeton (y compris OpenAlex, Vast.ai,
    Hugging Face ; ne jamais répéter un fragment de clé que Lazar aurait collé) ; les fichiers de clé de banque
    (`*-cle.json`, `*-secret.json`) ne s'ouvrent, ne s'affichent ni ne se hachent jamais ; **avant chaque poussée**, la
    recherche de clés (§ 2) sur tous les fichiers poussés, archives décompressées comprises ;
  - l'archive de septembre 2026 est hors périmètre ; GAIA exclu ; licence des données : CC BY-NC-SA 4.0 ; branche de
    données `donnees/eval-awareness-sous-ensemble-v1`, jamais `main` ni la copie publique ;
  - ne jamais reproduire le contenu de réflexion des réponses brutes ; ne jamais ouvrir ni servir une cellule refusée du
    collisionneur (dossiers `essais/` des tours compris) ; un refus de filtre n'est jamais contourné ni reformulé par toi
    (la règle de reformulation R-468 et R-470 de Lazar est appliquée par session-depot, pour des questions de méthode, avec
    ses bornes) ;
  - **les sous-agents** que tu lances n'ouvrent jamais `R/prereg/P3-consignes-v1.md`, `textes-actions-*`, `R/donnees/`,
    `R/runs/`, `R/diag/`, ni les fichiers `*-cle.json`, `*-secret.json`, `ferme.tar.gz`, `reponse-question*`,
    `journal-appels*`, `extrait-mecanique*` des pilotes réels ; pas de recherche récursive dans les dépôts, pas de git, pas
    de sous-agents pour eux ; tu leur donnes explicitement les fichiers à lire (R2) ;
  - aucun critère ni aucune stratégie de classement des tâches n'est jamais suggéré aux organismes ; les réponses du
    collisionneur ne sont jamais servies aux organismes ; le registre d'hypothèses et les verdicts des agents de la boucle
    extérieure non plus ; les scores de `test_final` ne sont jamais servis à Gemini ni à aucun organisme ; les résultats
    ne vont à Gemini qu'après le moment de lecture ;
  - téléchargements non fiables dans un dossier neuf ; Python avec `-I` (pour fixer une graine de hachage : `-P -s -B`,
    jamais `-I` ni `-E`) ; scripts hors du dossier téléchargé ;
  - registre jamais réécrit ; empreintes scellées jamais invalidées par réécriture d'historique ; versions dans les noms,
    jamais d'écrasement (R12) ;
  - **scores** : ceux des pilotes de conception (banque v3) se lisent **dès la fin de chaque course**, jamais pendant une
    course ni entre ses segments ; personne ne compte les rôles des appels d'une génération pendant qu'une course tourne ;
    aucun verbe de jugement sur des scores ou des réponses ; les scores du pilote 3 sont fermés ; rien des courses sur v1
    ou v3 (pilotes 1 à 4) n'entre dans des courses sur v5 ; les expériences de confirmation (étape 1 décisive,
    confrontation, pilote décisif (b)) se font sur la banque v6, scellées, et déclarent que leurs auteurs ont lu les scores
    de conception ;
  - les banques d'artefacts ne sont jamais servies ; les lanceurs épinglent l'empreinte de la banque servie ; les fichiers
    de banque qui portent des vérités restent hors de toute copie publique ;
  - copies d'essai du texte scellées avec de fausses graines : empaquetées en `tar.gz` ;
  - relire la tête distante avant toute étape qui fixe un commit, et de nouveau avant de sceller ;
  - **trois tours du collisionneur par défaut** pour toute question (jamais un seul sans le dire à Lazar) ;
  - ne jamais revendiquer « premier à faire des agents qui se réécrivent » (ni rien de « premier ») ;
  - contrôle de délégation, conscience d'évaluation : les deux familles de tâches ; **moyenne ou médiane sur les jetons
    interdites dans une sonde de production**.

## 2. Démarrer sur le nouveau compte

1. Ajouter le dépôt **privé** `lciric/controle-ia-travail` (outil d'ajout de dépôt, accès en écriture pour pousser le canal
   et la branche du pilote 4). Jamais `lciric/controle-ia`.
2. Arbres de travail recommandés (les chemins des briefs et des scripts poussés sont ceux de l'instance sortante ; les
   reprendre évite d'adapter) :
   - `/home/claude/pilote4` ← `outils/pilote4-gemini-travail` (tête `71914d1`) ; le texte est sous
     `essaim-m3-refonte-v1/prereg/` (« PR »), ses pièces sous `PR/pieces-pilote4-gemini/` (« PC »), les contre-lectures sous
     `PR/contre-lectures/` ;
   - `/home/claude/canal-conv-audit-n04` ← `canal/conv-audit-n04` (tes envois et messages, sous
     `brouillons/canal-reprise-releve-v1/`) ;
   - `/home/claude/banque-v2` ← `outils/banque-confrontation-v2-travail` (tête `ef0770f`) : le script de recherche de clés
     et le dossier de banque qu'il lit ;
   - une copie en lecture de `main`, de `canal/session-depot-reprise-n54`, de `canal/conv-audit-organisme-v6-2-1`
     (objet v6.2.1) et de `journal/commun-v1` ; les branches `donnees/…` se récupèrent au besoin
     (`git fetch origin refs/heads/donnees/X:refs/remotes/origin/donnees/X` si la configuration de récupération est
     restreinte).
3. Python : un environnement avec numpy ≥ 1.25 (R9 ; le script de scellement refuse sinon), par exemple
   `python3 -m venv /opt/venv-essaim-sim-v1 && /opt/venv-essaim-sim-v1/bin/pip install 'numpy>=1.25'`.
4. **Recherche de clés avant chaque poussée** :
   `/opt/venv-essaim-sim-v1/bin/python -I /home/claude/banque-v2/essaim-m3-refonte-v1/banque/construction-v5/chercher_cles_avant_poussee_v1.py /home/claude/banque-v2/essaim-m3-refonte-v1/banque FICHIER…`
   — attendu : « écritures de clé trouvées : 0 ». Le premier argument est le dossier de banque (une erreur de cette lignée :
   l'avoir oublié).
5. Routine de reprise (R14), version conv-audit : `cd docs && sha256sum -c sha256sums-lancement-v2.txt` et
   `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` sur une copie de `main` ; lire `registres/etat.md`,
   la passation n° 12 de session-depot, ses messages n° 54 à 60 et ce qu'elle publiera ; appliquer les défauts échus
   (§ 5) ; les instances de calcul sont l'affaire de session-depot. Puis reprendre au § 4.
6. Commits : auteur `conv-audit`, courriel de Lazar ; lignes d'attribution que ta session t'indique.

## 3. Têtes et empreintes à la passation

| objet | valeur |
|---|---|
| `main` | `f558ef7` (01:47 UTC, passation n° 12 de session-depot) ; registre des décisions jusqu'à R-476 |
| `canal/conv-audit-n04` | `a65dbfd`, puis le commit qui porte ce fichier et le n° 70 |
| `canal/session-depot-reprise-n54` | `1fdea23` (son n° 60) |
| `outils/pilote4-gemini-travail` | `71914d106d0a8d64d5da4a1f613a336cbef25fae` (après `6fcf239`) ; `git diff --name-only 8e5e2f7b 71914d1` : 1 013 chemins, **aucun** hors de `PERMIS_APRES_CODE` (lanceur v10, l. 183) — vérifié avec des chemins relatifs à la racine du dépôt (relatifs au dossier courant, le contrôle donne un faux « hors permis ») |
| `journal/commun-v1` | `6b72ec3` (25 octobre, 22:30 UTC) |
| texte v4 (non scellé) | `51752266ba21b72fe2ee4c8b8e4157581bcfeed82bd2790e1632482a7746fc34` (469 lignes ; copie relue : `PC/contre-lecture-6-v1/pilote4-gemini-organisme-v4-lu-par-cl6-51752266.md`) |
| texte v4 lu par la contre-lecture 5 | `efb13feb34f66d9652a194564c0bc9eced2889cbb6305c8dac9e97766246b60e` (`PC/contre-lecture-5-v1/…-lu-par-cl5-efb13feb.md`) |
| P4v3 (scellée, jamais lancée) | `de7a555932d8e8825a68bd1bd54baff55d08166f84f94d5deb9217312e78c656` |
| contre-lecture 5 | `PR/contre-lectures/pilote4-gemini-organisme-v4-cl5.md`, `914ac3fbf6b2ba0760ef3dace4dd8c3768909809e441ec0f63e5407c2d138240`, « scellable après corrections mineures » |
| contre-lecture 6 | `PR/contre-lectures/pilote4-gemini-organisme-v4-cl6.md`, `35fe0067ec7477c2e6e82500321bbe23a0683e20f2bbb6de36c55d4103dc7559`, sur `51752266…`, « scellable après corrections mineures » ; pièces `PC/contre-lecture-6-v1/` (note `LISEZMOI-contre-lecture-6-v1.md` : l'interruption déclarée à 01:44 était fausse) |
| empreintes des pièces v7 | `PC/EMPREINTES-pieces-pilote4-v7.txt`, `220768458e7a6778426b37f0b39aeabdfb2bebd4e385a36d31ede5e364573550` (621 entrées ; tout avant `contre-lecture-6-v1/`) |
| relevé des mots de Lazar | `PC/objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v5.md`, `c5fe20921285a7992f4236c867e981b13b7a55c47122be1afe16ad989a4c32c8` (chaîne v1 `6350ca87…`, v2 `96da3945…`, v3 `757f30a3…`, v4 `7e0837e6…`, v5) |
| objet v6.2.1 | commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`, arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, 26 fichiers, branche `canal/conv-audit-organisme-v6-2-1` |
| objet v5.3 | `4ecba58`, arbre `6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753`, 22 fichiers |
| noyau | `8e5e2f7b` (reprise par segments, 169 essais) |
| banque v3 | `157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d` (60 tâches par part : 36 conscience d'évaluation, 24 contrôle de délégation) |
| question M v2 épurée | `8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd` ; empreintes de M `5ae4e801423bbef0` |
| lanceur v10 | `PC/lancer_pilote4_gemini_v10.sh`, `0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952` ; batterie v12 `27ef4524…` ; série v13 : 229 sur 229 (journal `ed50ba14…`, heures `e2adbc2f…`) |
| scellement | `PC/sceller_pilote4_v4.py` (`6094f21a…`) ; vérification `PC/verifier_scellement_pilote4_v2.py` |
| GO | `GO-2026-10-25-02` (R-440 ; 185 USD au plus ; pilote 4 : 150 au plus ; 75 USD par course) ; collisionneur : `GO-2026-10-24-07` (**échoit le 26 octobre**) |

## 4. Le chemin critique du pilote 4, pas à pas (où l'on s'est arrêté : étape 1)

Contexte : deux courses, **la v6.2.1 d'abord, puis la v5.3** après une v6.2.1 saine ; banque v3 ; jusqu'à 6 rondes de
conception (3 USD et 900 s chacune), puis 4 générations notées ; segments avec minuteur à 3 400 s ; 75 USD par course.
Lazar a donné son accord par anticipation chez session-depot (R-445, R-448) : **dès la publication du message de départ**,
session-depot inscrit la ligne d'extension de GO et les lignes de dépense **exactement sous la forme qu'il donne**, puis
lance, segment après segment. Le pilote 4 est un **pilote de conception** (Lazar, 01:56 Paris ; R-473 chez session-depot) :
relecture gardée ; le texte garde sa forme et son script de scellement (le lanceur v10 lit l'entropie, les graines et
l'empreinte du texte).

1. ~~Relancer la contre-lecture 6~~ : **faite** (sous-agent neuf Opus, 01:29:47 à 01:53 UTC ; brief
   `PC/contre-lecture-6-v1/brief-contre-lecture-6-v1.md` ; rapport `35fe0067…` versé dans `PR/contre-lectures/` et copié dans
   `PC/contre-lecture-6-v1/` avec ses outils, relevés et essais). Une relecture de plus, si tu en fais une, s'appelle
   `pilote4-gemini-organisme-v4-cl7.md` (un nom comme `…-cl6b.md` ne serait compté ni par le script ni par le lanceur).
2. **Traiter ses constats dans le texte** (lis le rapport en entier ; ses corrections sont rédigées) :
   - **P4C6-01 (mineur)** : au point 4 bis, écrire la levée, pour ce pilote, des interdits de lecture qu'il enfreint (critères
     gelés de T2 l. 518–520, lecture « à côté, sans comparaison » de P4v3 § Plan point 4, « aucun seuil de lecture » de
     P4v3 § Hypothèse) **pour les seules comparaisons qu'il nomme** (un score et la référence de sa famille et de sa part ;
     générations 0 et 3 d'une même course) ; le reste des critères vaut ; rétablir « critères gelés (sauf ce que lève le
     point 4 bis) » dans « Tout le reste » ; dire si les verdicts des agents par hypothèse relèvent du rapport de lecture ou
     sont des pièces à part, exploratoires.
   - **P4C6-02 (mineur)** : point 3 et canal (d) : « aucun score **d'une course** n'est lu tant qu'**elle** tourne, entre ses
     segments compris ; ceux de la v6.2 peuvent être lus dès sa fin, pendant la v5.3, qui part et tourne telle quelle (aucune
     de ses gardes ne lit un score) » ; point 3 et table : il « remplace le moment de lecture et les conditions (i) et (ii)
     du point 3 de P4v3 ; en garde ce que session-depot consulte pendant et entre les segments (P4v3 l. 391–397) et les
     canaux dits et acceptés (l. 397–409) ».
   - **P4C6-03 (mineur)** : point 3 : « les hypothèses de (b) sont écrites et poussées, avec leur empreinte, avant que leurs
     auteurs lisent un score de ce pilote, au plus tard à la fin de sa première course » (direction de 00:49, δ = 0,10, deux
     paliers, banque v6 ; ce que la synthèse laisse ouvert — hypothèse à un sens ou symétrique, course nulle — tranché sans
     score ou par Lazar) ; § Décisions : remplacer « trois graines par objet » par « taille fixée par le texte de (b) (deux
     paliers, 01:48 ; sans les courses de ce pilote, 01:52) ».
   - **P4C6-04** : R-472 est dépassé par **R-473** (Lazar a confirmé la levée dans la session de session-depot vers 01:19
     UTC) : l'écrire au § Décisions (01:56) et au point 3, R-473 cité ; le relevé v6 (s'il est fait) cite `4a4d9ca` et
     `3c94802`, et ajoute R-473 à R-476 et les messages de 02:32 à 02:42.
   - **P4C6-05** : fixer au point 4 bis, avant toute lecture : (a) la combinaison des intervalles de Wilson des deux classes ;
     (b) la référence (maximum de surface et de provenance, règle de la banque, ou chacune) ; (c) d'où viennent les comptes
     par classe (réponses par tâche de la liste fermée et secret de la banque ; même repli « rapporté impossible ») ;
     (d) « sans correction de multiplicité, exploratoire » pour (ii) (jusqu'à 32 comparaisons) et « au plus quatre tests »
     pour (iii) ; (e) **qui exécute le script de lecture** (il lit le secret de la banque ; les agents n'en voient que la
     sortie).
   - **P4C6-06** : servir des scores de `test` à un organisme : « sur décision de Lazar (lecture, par conv-audit, de « pour
     corriger l'organisme », 01:56) » ; les autres pièces fermées (P4v3 l. 460) seulement sur décision de Lazar ; jamais
     `test_final`.
   - **P4C6-07** : trois descriptions du traitement de la contre-lecture 5 à rendre exactes (« le point 8 de la demande de
     v6.2 » ; aligner P4C5-05 (d) et le § Essais ; « écrits dans la table comme choix restant à Lazar, sans effet sur le
     départ ») ; la docstring du script porte la même inexactitude que son en-tête (sans effet).
   - **P4C6-08** : (a) fait (note de correction versée, la note fausse gardée) ; (b) dernier alinéa du § Contre-lecture :
     ajouter « et les corrections qu'il demande, aux passages qu'il nomme » ; (c) aucune ligne « entropie E = » ni « graine
     de la course … = », aucun `<<…>>` ni `[[…]]` dans ce que tu ajoutes.
   - Puis remplacer le paragraphe « Contre-lecture 6 » du § Contre-lecture (il dit aujourd'hui « … sa ligne … est inscrite ici
     avant le script de scellement ») par sa ligne : sous-agent neuf `claude-opus-5-5`, 26 octobre, 01:29:47 à 01:53 UTC, sur
     `51752266…`, rapport et `35fe0067…`, « scellable après corrections mineures », constats et leur traitement ; tenir juste
     le paragraphe « Ce texte scellé ». Comme pour la contre-lecture 4, ces corrections mineures peuvent être traitées sans
     relecture nouvelle si elles reprennent celles du rapport ; si tu t'en écartes, une relecture courte (`-cl7.md`).
2 bis. **Avant toute lecture de score du pilote 4** (donc avant la fin de la v6.2.1, qui dure de l'ordre de quelques
   heures une fois lancée) : (i) **le script de lecture** (P4v3 § Plan point 4 : écrit, empreinté, essayé sur un cas sain et
   sur un artefact avant le moment de lecture) **calcule aussi le point 4 bis** ; il lit le secret de la banque v3 (fichier de
   clé, jamais affiché) ; (ii) **les hypothèses de (b)** sont écrites et poussées avec leur empreinte (P4C6-03) ; (iii) le
   protocole et les briefs de la boucle extérieure (§ 6.4). Sans (i) et (ii), conv-audit ne lit aucun score.
3. ~~Verser~~ : fait pour la contre-lecture 6. Verse de même ce que tu ajoutes (relevé v6, rapport d'une éventuelle
   contre-lecture 7).
4. Recherche de clés sur tous les fichiers nouveaux ; relire la tête distante de `outils/pilote4-gemini-travail` (attendu :
   `71914d1`) ; committer et pousser « avant scellement ».
5. **Sceller**, depuis `PR` :
   `/opt/venv-essaim-sim-v1/bin/python -I pieces-pilote4-gemini/sceller_pilote4_v4.py pilote4-gemini-organisme-v4.md pieces-pilote4-gemini contre-lectures v6-2`
   (relire avant la tête distante). Il tire l'entropie par `secrets.randbits(128)`, écrit les deux graines
   (`SeedSequence(E).spawn(2)` : enfant 0 → `v5-3`, enfant 1 → `v6-2`, `int(enfant.generate_state(1, dtype=numpy.uint64)[0])`),
   écrit `PC/EMPREINTES-pilote4-gemini-v2.txt` (toutes les pièces et les contre-lectures) et le compagnon `.sha256` du
   texte. (L'en-tête du script dit « v5-3 (première course) » : commentaire inexact depuis l'inversion de l'ordre, sans effet
   sur le code ; traité au § Contre-lecture, P4C5-07 (c).)
6. **Vérifier** : `… -I pieces-pilote4-gemini/verifier_scellement_pilote4_v2.py pilote4-gemini-organisme-v4.md pieces-pilote4-gemini contre-lectures`
   → code 0 ; recalculer les deux graines à part depuis l'entropie ; rejouer les contrôles du lanceur : la ligne de GO du
   § Plan, point 1, empreinte remplie, passe
   `grep "^| GO-2026-10-25-02 |" | grep calcul | grep 8b1c7511 | grep 4f13647a | grep <16 premiers caractères> | grep 157a2b45`,
   et la même avec `6251ab21` ; les lignes de dépense portent le nom de la course, `GO-2026-10-25-02` et `5ae4e801423bbef0`
   (et, pour la v5.3, les 16 premiers caractères des empreintes de la v6.2). Vérifier encore
   `git diff --name-only 8e5e2f7b HEAD` contre `PERMIS_APRES_CODE`.
7. Recherche de clés ; relire la tête distante ; committer et pousser le texte scellé.
8. **Publier le message de départ** à partir de `brouillons-messages-conv-audit-v1/brouillon-depart-pilote4-v3.md` (canal) :
   remplir chaque `⟦…⟧` (numéro = le suivant libre, 71 si rien d'autre n'est parti ; date ; heure lue ; têtes ; empreinte du
   texte scellé ; entropie ; graines ; empreinte et nombre de lignes de `EMPREINTES-pilote4-gemini-v2.txt` ; contre-lectures 5
   et 6 ; **`⟦LIGNE_GO⟧` = la ligne du § Plan, point 1, mot pour mot, l'empreinte remplie** ; `⟦SHA16⟧`). Le message recopie
   les lignes de dépense mot pour mot ; s'il en diffère, rien ne part. Empreinte, recherche de clés, poussée. Lazar n'a rien
   de plus à écrire ; session-depot (son instance nouvelle) lance.
9. **Pendant les courses : rien** (aucune lecture de score, aucun compte des rôles d'appels). À la fin de la v6.2.1
   (liste fermée poussée, recherche des clés faite), et de même à la fin de la v5.3 : **boucle extérieure** (§ 6.4) —
   lecture contre le bruit (texte, § Plan, point 4 bis : Wilson à 95 % par classe → exactitude équilibrée ; « au-delà du
   bruit des tâches » si la borne basse dépasse la référence ; McNemar exact génération 0 contre génération 3 sur
   `test_final`, par course et par famille, quatre tests, Holm à 0,05 ; aucune comparaison entre les deux objets), verdicts
   par hypothèse, proposition de la ronde suivante à Lazar ; toute relance est une course nouvelle, sur son mot.

## 5. Décisions de Lazar : prises, en attente, défauts

**Prises depuis 01:37 Paris** (verbatim au relevé v5 ; le texte v4, § Décisions, les rend) : D1 à D4 de l'étape 1
« ok » ; consigne « il faut corriger la version pour rendre l'effet predit detectable » (≈ 10 courses par bras et une banque
≥ 96 tâches) ; plan de l'étape 2 « je suis ok », « parfait » ; 01:48, (3+) « go » (hypothèses de (b) sans aucun score du
pilote 4), deux paliers, δ = 0,10, « go a tout » (une mesure principale, courses entrelacées, plus de tâches) ; 01:49, points
ouverts de l'étape 2 « ok » ; 01:52, banque v6 (lot 3) pour (b) « go » ; 01:54, « il faut s'assurer que le pilote 4 puisse
separer du bruit aussi » (option (a), lecture contre le bruit sans course de plus, appliquée par le texte) ; 01:55 et 01:56,
« agents sur le noyau », levée du préenregistrement et du scellement pour les pilotes de conception, relecture gardée,
confirmation sur la v6, « relecture puis départ » ; 02:05, « je veux un pilote qui separe du bruit, pilote 4 le fait il ? » ;
02:06, « et je veux un pilote qui appelle des agents qui font les tets et eliminent les hypotheses fausses et font relancer un
nouveau tour ou une nouvelle generation de l'organisme » ; chez session-depot : R-470 (règle de reformulation étendue aux
refus de Fable, « oui »), **R-471 (primitive d'expérience bornée dans le noyau, « go » : la boucle intérieure)**, R-473
(levée confirmée), R-475 (tour « littérature des boucles », « go dépense ») ; 02:17, **« (a) … go »** sur la boucle
extérieure, et « va lire leurs papiers et la litterature sur le sujet pour t'en inspirer, que le collisionneur fasse de
meme ».

**Messages de Lazar après le relevé v5** (verbatim) :
- 02:32 : « Le tour « agents sur le noyau » est fini et versé sur `donnees/collisionneur-agents-noyau-v1` : sept cellules
  valides sur neuf, 5,39 US » (compte rendu de session-depot collé ; information).
- 02:34 : « [lyramakesmusic/neuron-explorer: Steering-first neuron explorer for Qwen3.5-4B: push every MLP neuron, keep every
  rollout, browse the results](https://github.com/lyramakesmusic/neuron-explorer) : va lire cette page ret brainstorme sue
  comment cette methose pourrait s'integrer a notre programme aiu control, demande aussi au collisionneur » → fait : § 6.5.
- 02:42 : la demande de cette passation.

**En attente de Lazar** :
1. **Graines de plus pour le pilote 4** (soumise à 02:05, dépense, **sans défaut**) : (a) trois graines par objet (quatre
   courses de plus, ≈ 180 USD attendus, 300 au pire, lanceur dérivé, texte nouveau, GO nouveau), recommandée ; (b) cinq
   graines ; (c) garder une course par objet. Le texte v4 garde une course par objet ; ses deux courses ne seraient les
   premières graines que si le texte nouveau le dit avant toute lecture de leurs scores. Sur « go » : écrire ce texte nouveau
   (pilote de conception, relu, scellé mécaniquement comme le v4 pour le lanceur), dériver lanceur et batterie, proposer à
   Lazar la phrase pour session-depot (extension ou GO nouveau, plafond, noms de courses versionnés). **Question complète,
   calcul et marche à suivre : § 5 bis.**
2. **Tour du collisionneur « neuron-explorer »** (dépense, sans défaut) : phrase donnée à Lazar dans le dernier message de
   l'instance sortante (« Mot direct : go dépense. Tour du collisionneur sur la question de conv-audit
   `question-neuron-explorer-integration-collisionneur-v1.md` (canal/conv-audit-n04, empreinte 2ba899dd…) : étage III, trois
   tours, trois modèles, une tentative par cellule, règle R-468 et R-470 sur les refus ; plafond 10 USD, sous
   GO-2026-10-24-07 s'il court encore, sinon une ligne de GO nouvelle ; branche donnees/collisionneur-neuron-explorer-v1 ;
   jamais servi à un organisme. »).
3. **Défauts sous 48 heures** : « lecture contre le bruit » du pilote 4 (soumise 26 octobre 00:54 UTC ; défaut (a), déjà
   appliqué par le texte) — **échoit le 28 octobre vers 00:54 UTC** ; « lecture si la confrontation change un seuil »
   (soumise 25 octobre vers 20:54 UTC ; défaut (a)) — **échoit le 27 octobre vers 20:54 UTC** ; sans objet pour le
   pilote 4, ouverte pour les autres textes. Consigner chaque défaut échu dans ton journal et le signaler à session-depot
   (qui l'inscrit dans `registres/decisions.md`).
4. **Dépenses déjà approuvées sur le principe, sans ligne** : étape 1 v10, D2 (relance d'amorçage à 128 000 jetons, 65 536
   pour Gemini, plafond 11 USD par lignée) et D4 (extension de GO-05) — lignes sur le devis de la v10, mot direct de Lazar
   chez session-depot ; étape 2, D4 (pilote de bruit, ≈ 160 à 280 USD) et D9 (phase décisive réduite, ≈ 515 à 1 010 USD).

**Ce qu'on a dit à Lazar depuis 02:05** (pour que tu saches ce qu'il sait) : 02:05, le pilote 4 ne sépare pas du bruit à
une course par objet, décision « graines » ; 02:07, décision sur les deux boucles (option (a)) ; 02:12, son « go » R-471 a
déjà tranché la boucle intérieure, la boucle extérieure reste à son choix, coordination « noyau de l'étape 1 » ; 02:24,
(a) consignée, deux sous-agents lancés (registre et littérature), phrase du tour « littérature » (parti depuis, R-475) ;
puis le dernier message de l'instance sortante (passation, neuron-explorer, phrase, travaux interrompus).

## 5 bis. Question en attente, transmise telle quelle : des graines de plus pour le pilote 4 ?

**Origine.** Lazar, 02:05 Paris : « je veux un pilote qui separe du bruit, pilote 4 le fait il ? ». Réponse de conv-audit :
**non**. À une course par objet, la variance entre graines n'est pas mesurée ; le texte v4 (§ Plan, point 4 bis) ne lit que
le bruit **des tâches** à l'intérieur d'une course (intervalles de Wilson, génération 0 contre génération 3) et ne compare
jamais les deux objets. La décision ci-dessous lui a été soumise à 02:05 (dépense, **sans défaut**) ; il n'y a pas répondu,
puis a demandé à 03:01 de la transmettre. Le texte exact du message de 02:05 n'est pas gardé dans les fichiers (il précède la
fenêtre du journal de la session sortante) ; ce qui fait foi : le relevé v5 (`PC/objet-v6-2-1-v1/mots-de-lazar-2026-10-25-26-v5.md`,
ligne 02:05) ; la restitution ci-dessous reprend ses options et ses chiffres, avec un calcul refait et poussé.

**Calcul** (illustratif : la part « course » du bruit, σ, et la corrélation d'une tâche d'une graine à l'autre, ρ, sont
inconnues) : `passation-conv-audit/calcul-graines-pilote4-v1/` (script `calcul_ecart_minimal_graines_v3_v1.py`
`b0903c78…`, sortie `calcul-ecart-minimal-graines-v3-v1.json` `7927e041…` et `.txt` `338746bc…`, `EMPREINTES-v1.txt`). Même
modèle que le calcul de l'étape 2 (variance d'une course V = σ² + (1 − ρ) p (1 − p) / n), appliqué à la part `test_final` de
la banque v3 ; écart minimal entre les deux objets = (t₀,₉₇₅ + t₀,₈₀ ; 2R − 2 degrés de liberté) × √(2V/R), bilatéral à
0,05, puissance 0,8. À p = 0,75 :

| R graines par objet | conscience d'évaluation (36 tâches) | contrôle de délégation (24) | les deux familles (60) |
|---|---|---|---|
| 1 (le texte v4) | non testable | non testable | non testable |
| 3 | 0,14 à 0,22 | 0,17 à 0,27 | 0,11 à 0,17 |
| 5 | 0,09 à 0,15 | 0,11 à 0,18 | 0,07 à 0,11 |
| 10 | 0,06 à 0,10 | 0,07 à 0,12 | 0,05 à 0,07 |

(fourchette : de σ = 0, ρ = 0,6 à σ = 0, ρ = 0 ; avec σ = 0,05 et ρ = 0,6 : 0,21, 0,23 et 0,19 à R = 3 ; au pire cas
p = 0,5, σ = 0,05, ρ = 0 : 0,30, 0,35 et 0,25 à R = 3.)

**La décision, à reposer à Lazar dans ce format** (tu peux la rafraîchir, pas en changer le fond) :
- **Décision** : ajouter des graines au pilote 4, pour mesurer le bruit entre graines et comparer les deux objets au-delà
  de ce bruit ?
- **Enjeu** : à une course par objet, aucune différence entre la v6.2.1 et la v5.3 n'est lisible, et le bruit entre
  graines reste inconnu jusqu'au pilote décisif (b) sur la banque v6. Des graines de plus, sur la v3, restent de la
  **conception** (exploratoire) : elles disent l'ordre de grandeur du bruit entre graines (utile pour dimensionner (b) et
  la boucle extérieure) et ne séparent que des écarts assez grands ; elles ne tranchent pas la question de fond (« la
  complexité ajoutée vaut-elle au-delà du bruit ? »), qui reste celle de (b), scellé sur la v6.
- **(a) Trois graines par objet** — les deux courses du texte v4 comptent comme première graine, plus **quatre courses**
  (deux par objet, entrelacées) : ≈ **180 USD attendus, 300 au pire** (4 × ≈ 45 et 4 × 75, bornes de R-445) ; sépare du
  bruit un écart d'environ 0,14 à 0,27 selon la famille et ρ (tableau) ; durée de l'ordre de quatre courses de plus (estimation
  de 00:54 : 8 à 10 heures pour six courses, non opposable). Avantage : le bruit entre graines mesuré tôt, pour peu.
  Inconvénient : texte nouveau, lanceur et batterie dérivés, GO nouveau ; ne sépare pas un écart de 0,10.
- **(b) Cinq graines par objet** — plus **huit courses** : ≈ 360 USD attendus, 600 au pire ; écart d'environ 0,09 à 0,18 ;
  durée double. Avantage : un cran plus fin. Inconvénient : deux fois le prix, pour un résultat qui reste exploratoire ;
  (b) sur la v6 le refera de toute façon.
- **(c) Garder une course par objet** — rien de plus. Avantage : aucun coût, aucun délai. Inconvénient : pas de mesure du
  bruit entre graines avant (b).
- **Recommandation** : (a), confiance moyenne. **Pas de défaut** : rien ne part sans le mot direct de Lazar dans la session
  de session-depot.

**Contrainte de temps (à dire à Lazar).** Pour que les deux courses du texte v4 comptent comme première graine, le texte
nouveau doit le dire et être poussé, avec son empreinte, **avant toute lecture de leurs scores** — donc avant que conv-audit
lise les scores de la v6.2.1 (§ 4, étape 9 : dès la fin de la course). Si la réponse vient après cette lecture, (a) devient
**six courses nouvelles** (≈ 270 USD attendus, 450 au pire) et (b) dix (≈ 450 et 750). Si Lazar répond « go » pendant que les
deux courses tournent, n'en lis aucun score avant d'avoir poussé le texte nouveau.

**Sur « go (a) » ou « go (b) »** :
1. **Texte nouveau**, nom versionné (par exemple `pilote4-graines-gemini-organisme-v1.md`), différentiel sur le texte v4
   scellé, qui ne le modifie pas : pilote de conception (R-473 : relu par un sous-agent neuf, sans préenregistrement au sens
   de R1), mais scellé mécaniquement par un script dérivé du v4, car le lanceur lit l'entropie, les graines et l'empreinte du
   texte ; entropie nouvelle, graines `SeedSequence(E).spawn(k)` (jamais celles du v4) ; noms de courses nouveaux et
   versionnés (par exemple `pilote4-gemini-v6-2-g2-v1`, `pilote4-gemini-v5-3-g2-v1`, `pilote4-gemini-v6-2-g3-v1`,
   `pilote4-gemini-v5-3-g3-v1`), ordre entrelacé ; mêmes objets (`7ea3270`, `4ecba58`), même noyau `8e5e2f7b`, même banque,
   mêmes bornes par course ; porte « course précédente saine » pour chaque course ; plan de lecture exploratoire : le
   point 4 bis par course, la variance entre graines par objet et par famille, la comparaison des deux objets avec son
   écart minimal écrit d'avance (tableau ci-dessus, recalculé), aucune autre comparaison ; liste d'arrêt.
2. **Lanceur v11** dérivé du v10 (noms et graines par indice, porte généralisée), **batterie v13** et sa série (cas sains et
   artefacts, R5), relecture par un sous-agent neuf ; recherche de clés ; poussée sur `outils/pilote4-gemini-travail` (chemins
   à ajouter à `PERMIS_APRES_CODE` du lanceur v11 si besoin, vérifiés depuis la racine).
3. **Phrase pour Lazar**, à écrire dans la session de session-depot (brouillon, à ajuster aux noms et chiffres retenus) :
   « Mot direct : go dépense. Pilote 4, graines de plus : quatre courses de plus (deux par objet, v6.2.1 et v5.3,
   entrelacées), sous le texte pilote4-graines-gemini-organisme-v1.md et le lanceur que conv-audit publiera avec leurs
   empreintes dans son message de départ. Bornes de chaque course : celles de R-445 (4 générations ; 6 rondes de conception
   au plus, à 3 USD et 900 s ; 75 USD par course, tous segments compris ; segments, minuteur à 3 400 s). Plafond : 300 USD
   au plus pour ces quatre courses, par une ligne de GO nouvelle. Dès ce message de départ publié, inscris la ligne de GO
   et les lignes de dépense exactement sous la forme qu'il donne, puis lance, course après course, après la fin saine des
   deux courses du pilote 4. La liste d'arrêt du texte reste en vigueur. » (pour (b) : huit courses, plafond 600 USD).
4. Rien de ces courses ne part avant la fin saine des deux courses du texte v4 ; rien n'entre dans (b) (banque v6, 01:52).

## 6. Travaux ouverts, avec leurs pièces

### 6.1 Messages
- Tes derniers : n° 68 (`9516eb2b…`), n° 69 (avis sur le test H-M1, `f40a0631…`), **n° 70** (01:49 UTC : passation,
  réponses (a) à (c) sur la primitive, matériaux des étapes 1 et 2, décisions de 01:48 à 02:17). Prochain numéro : **71**.
- Session-depot : n° 54 à 60 lus. Elle attend : le message de départ ; ta relecture du texte H-M1 v4 (étape 0, code prêt
  sur `outils/test-hm1-v1`, `3843a91b`, texte et lanceur à écrire par elle ; R-476 : « (b) validé avec corrections »,
  `docs/notes/suite-hm1-v1/jugement-suite-HM1-v1.md`) ; sa v2 du dessin de la primitive (`docs/notes/dessin-primitive-experience-v1.md`,
  `9c5ada0c…`) nourrie de tes remarques du n° 70, § 0 (c).

### 6.2 Synthèses du collisionneur à refaire (pour Lazar)
- **« Test de M »** (`donnees/collisionneur-test-M-v1`, `1ff500d` ; neuf cellules valides, 5,62 USD) : brief
  `envois/syntheses-collisionneur-briefs-v1/BRIEF-synthese-test-M-v1.md`. Reconstituer `/var/tmp/fournis-synthese-test-M-v1/` :
  de la branche, `collisionneur-test-M/LISEZMOI-v1.md` (renommé `LISEZMOI-collisionneur-test-M-v1.md`),
  `EMPREINTES-v1.txt` (renommé `EMPREINTES-collisionneur-test-M-v1.txt`), `question-test-M-sondes-collisionneur-v1.md`,
  `run-test-M-e3t1-v1/cellules/*.md` → `cellules/` ; de `main`, `prereg/test-hm1-gabarit-style-v1.md` à `-v3.md` ; du canal,
  `envois/avis-test-HM1-gabarit-style-conv-audit-v1.md`. Sortie : `/var/tmp/synthese-collisionneur-test-M-v1/`. Note : la
  suite de H-M1 a déjà été jugée (R-476) ; cette synthèse sert Lazar.
- **« Agents sur le noyau »** (`donnees/collisionneur-agents-noyau-v1`, `b4be1808` ; sept cellules valides sur neuf, refus
  d'Opus au III.1 et au III.3 ; question reformulée pour Opus seul : `donnees/collisionneur-agents-noyau-methodo-v1`,
  `1a26f499`) : brief `envois/syntheses-collisionneur-briefs-v1/BRIEF-synthese-agents-noyau-v1.md`. Reconstituer
  `/var/tmp/fournis-synthese-agents-noyau-v1/` : `collisionneur-agents-noyau/{LISEZMOI-v1.md, EMPREINTES-v1.txt,
  question-agents-noyau-essais-erreurs-collisionneur-v1.md}` ; les sept `run-agents-noyau-e3t1-v1/cellules/*.md` →
  `cellules/` ; de la branche methodo, `LISEZMOI-v1.md`, `question-conception-iterative-statistique-collisionneur-v1.md` et
  `run-agents-noyau-methodo-e3t1-v1/cellules/E3-T1-conception-B.md` → `methodo/` ; du canal,
  `envois/synthese-collisionneur-lecture-pilote-conv-audit-v1.md` → `exemple-synthese-precedente-lecture-pilote-v1.md`.
  **Jamais les dossiers `essais/`** (ils portent les réponses refusées). Sortie : `/var/tmp/synthese-collisionneur-agents-noyau-v1/`.
- **« Littérature des boucles »** (R-475) : parti dans le conteneur de l'ancienne session-depot ; branche
  `donnees/collisionneur-litterature-boucles-v1` **pas encore créée** à 01:50 UTC. Si elle est versée : synthèse. Sinon,
  rien ne se relance sans le mot de Lazar (GO-2026-10-24-07 échoit le 26 octobre).
- Les autres tours versés par session-depot (escalier, escalier en plan statistique, agents outillés, interface de calcul
  bornée, suite de H-M1) sont lus et jugés par elle ; à intégrer au dessin v2 de la primitive.

### 6.3 Lecture de la littérature (demande de Lazar, 02:17)
- Brief : `envois/lecture-boucles-agents-v1/BRIEF-lecture-v1.md`. Liste des 24 PDF téléchargés et empreintés par le
  sous-agent interrompu (identifiants arXiv et chemins) : `envois/lecture-boucles-agents-v1/EMPREINTES-pdfs-v1.txt` ; une
  seule fiche écrite, non relue : `envois/lecture-boucles-agents-v1/fiches/ai-scientist-v1.md`. Les PDF ne sont pas poussés :
  les retélécharger chacun dans un dossier neuf, vérifier l'empreinte (si elle diffère, consigner la nouvelle), puis
  relancer un sous-agent neuf sur le brief, en lui donnant la fiche déjà écrite. Ensuite : fiche de synthèse pour Lazar,
  et emprunts pour les deux boucles (sans revendication d'antériorité).

### 6.4 Boucle extérieure du pilote 4 (« go » de Lazar, 02:17)
- Brief : `envois/boucle-exterieure-pilote4-v1/LISEZMOI-brief-v1.md` (quatre fichiers à écrire). **Écrit** par le sous-agent
  interrompu : `envois/boucle-exterieure-pilote4-v1/sortie-partielle/registre-hypotheses-conception-pilote4-v1.md` (douze
  fiches HC-P4-01 à HC-P4-12, dont deux hypothèses nulles, § 0 à 3 ; **non relu**). **À écrire** : le protocole, les briefs
  des trois agents (analyste, correcteur, contre-lecteur neuf), le LISEZMOI. Pièces à fournir au sous-agent : le texte v4
  (`51752266…`), P4v3, `envois/question-agents-noyau-essais-erreurs-collisionneur-v1.md`, la synthèse « lecture du pilote »,
  le dessin v1 de la primitive, le relevé v5, le registre partiel ; puis contre-lecture du tout par un autre agent neuf
  (R2) ; **avant la fin de la première course**. Le registre et les verdicts ne sont jamais servis à un organisme ; aucune
  hypothèse n'y porte sur la manière de classer une tâche.

### 6.5 « neuron-explorer » (demande de Lazar, 02:34)
- Lu le 26 octobre vers 01:34 UTC (dépôt public, branche `main`) ; fichiers téléchargés et empreintes :
  `envois/neuron-explorer-lecture-v1/` (`README.md` `f503111a…`, `research_log.md` `570524ed…`, `NOTES.md` `c59f6ebe…`,
  `explorer_agent_methodology.md` `f86b1b2f…`, `explorer_agent_prompt.md` `aaed0182…` (non lu en entier), `pyproject.toml` ;
  `EMPREINTES-telechargement-v1.txt`) ; **licence non trouvée** ; aucun code exécuté.
- Remue-méninges : `envois/brainstorm-neuron-explorer-integration-conv-audit-v1.md` (`cc1e5c1d…`) : six points de contact
  (poussée de la direction d'une sonde contre des directions aléatoires comme test de validité ; H6 et N-015 — revendiquer
  une poussée comme intervention est un nœud pour Lazar ; une opération « pousser » dans la primitive, témoins servis avec
  la mesure ; la méthodologie de l'agent comme gabarit de nos agents — « casser l'hypothèse exprès », « maximum à
  l'aveugle » par un second agent ; balayage exploratoire de nos deux familles ; moniteur) ; options A à E ; recommandation
  à l'épreuve : D tout de suite, A dans la v10 de l'étape 1, B dans le dessin v2, C plus tard sur devis. **Pas encore
  envoyé à Lazar en détail** : lui en donner le verdict et la décision quand le collisionneur aura répondu (ou plus tôt s'il
  le demande).
- Question au collisionneur : `envois/question-neuron-explorer-integration-collisionneur-v1.md` (`2ba899dd…`) ; part sur son
  mot (§ 5, point 2).

### 6.6 Autres fronts (antérieurs)
- **Étape 1 v10** : matériaux remis à session-depot (`envois/etape1-v10-materiaux-conv-audit-v1/`, `EMPREINTES-v1.txt`
  `9892be30…`) — correctifs BC5-01 et R-441 en diff (`6bf3a4ae…`, base `3ea95fd`), traits à réindexer
  (`deriver_traits_v5_v1.py`, `f1c536fb…` ; réserve : vérifier le manifeste réel de l'extraction), porte 0, puissance
  (+0,10 : ≈ 10 courses par bras et ≥ 96 tâches). Le texte v10 est celui de session-depot ; tu relis.
- **Étape 2** : proposition (`envois/etape2-proposition-conv-audit-v1/`, `18200ce9…`) et brouillon du préenregistrement
  (`envois/etape2-preenregistrement-brouillon-conv-audit-v1/`, `357f241a…`) : relire, soumettre les points ouverts P1 à P7.
- **Pilote décisif (b)** : texte à écrire sans aucun score du pilote 4 (deux paliers, δ = 0,10, une mesure principale,
  courses entrelacées), scellé quand la **banque v6 (lot 3)** existe, contre-lu, GO nouveau sur devis. La construction de
  la v6 : voir la passation n° 12 de session-depot et les décisions N-046 et N-047 (`envois/decision-N-046-…`,
  `envois/decision-N-047-…`) ; si personne ne la porte, le signaler à Lazar.
- **Pilote 5** (primitive, boucle intérieure dans la course, caste « expérimentateur » qui déclare ses hypothèses dans
  `hypotheses-testees.json`, les élimine par pré-test et relance la génération suivante sans elles) : texte de ta lignée
  après la v2 du dessin de session-depot ; pilote de conception (relu, non scellé, devis, mot de Lazar).
- **Journal** : `journal/commun-v1`, dernière entrée conv-audit `6b72ec3` (25 octobre, 22:30 UTC) ; brouillon non publié
  `brouillons-messages-conv-audit-v1/journal-2026-10-25-suite-v1.md` ; écrire l'entrée du 26 octobre (cette passation en
  résumé).

## 7. Ce qui a été poussé avec ce fichier (canal, dossier `brouillons/canal-reprise-releve-v1/`)

`messages/conv-audit_2026-10-26_n70.md` ; `passation-conv-audit/` (la v1, ce fichier v2, le calcul `calcul-graines-pilote4-v1/`) ; `brouillons-messages-conv-audit-v1/`
(brouillon v3 du départ, brouillon du journal) ; `outils-conv-audit-v1/` (scripts de correctifs du texte v4 et du relevé, pour
traçabilité ; déjà appliqués, ne pas relancer) ; `envois/boucle-exterieure-pilote4-v1/` ; `envois/lecture-boucles-agents-v1/` ;
`envois/syntheses-collisionneur-briefs-v1/` ; `envois/neuron-explorer-lecture-v1/` ;
`envois/brainstorm-neuron-explorer-integration-conv-audit-v1.md` et `envois/question-neuron-explorer-integration-collisionneur-v1.md`.
Sur `outils/pilote4-gemini-travail` (`6fcf239`, puis `71914d1`) : le texte v4 non scellé, les contre-lectures 5 et 6 et leurs
pièces, les pièces nouvelles.

## 8. Erreurs de cette lignée à ne pas refaire

- Un seul tour du collisionneur, repris d'une proposition ancienne sans redemander : trois tours par défaut.
- Une question ambiguë (« 36 et 24 tâches par part » lu 48) : écrire les effectifs sans ambiguïté (60 par part : 36 + 24).
- Un message de session-depot lu en retard : relire le canal à chaque étape.
- Le script de recherche de clés appelé sans le dossier de banque.
- Une contradiction (verser le pilote 4 dans (b) contre la banque v6) relevée tard : la signaler dès qu'elle apparaît.
- Sous-agents lancés sans marge de crédit : à quatre en parallèle, ils sont tous tombés en même temps ; en lancer moins à
  la fois, et verser leurs sorties partielles.
- Une note d'interruption écrite trop tôt (la contre-lecture 6 tournait encore, sur un autre modèle) : vérifier l'état d'un
  sous-agent avant de le déclarer arrêté.
- Un contrôle des chemins permis fait avec des chemins relatifs au dossier courant : faux « hors permis » ; toujours
  `git diff --name-only 8e5e2f7b HEAD` depuis la racine.

## 9. Pour démarrer (texte que Lazar colle dans l'instance nouvelle)

« Tu es la lignée conv-audit du programme de contrôle. Ajoute le dépôt privé lciric/controle-ia-travail (jamais
lciric/controle-ia), lis en entier `brouillons/canal-reprise-releve-v1/passation-conv-audit/passation-conv-audit-2026-10-26-v2.md`
sur la branche `canal/conv-audit-n04` (vérifie son empreinte avec son compagnon `.sha256`), puis `CLAUDE.md`, fais la routine
de reprise qu'elle décrit, repose-moi la question des graines (§ 5 bis) et reprends au § 4, étape 2 (traiter les constats
de la contre-lecture 6 du pilote 4). Tu n'écris jamais sur main ; GO et
dépenses : seulement sur mon mot direct dans la session de session-depot. »

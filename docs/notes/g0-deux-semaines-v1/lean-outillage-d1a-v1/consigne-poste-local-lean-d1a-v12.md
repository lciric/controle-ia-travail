# Consigne : session du poste local de Lazar — outillage Lean D-1a, cinquième essai (GO-2026-11-10-13) — v12

**v12 (2026-11-22, vers 11:30 UTC, `date -u`)** : écrite par un développeur Opus 5.5 (`claude-opus-5-5`), sous-agent de la
session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`, à sa demande. Pièce d'instrument (classe B). Remplace la v11
(`consigne-poste-local-lean-d1a-v11.md`, `b6bd97df…`), gardée telle quelle (R12). Différentiel, au format unifié :
`differentiel-consigne-v11-v12.diff`. Code, apport (correctif v3, `949d2d6a…`, arbre `ab77bbac…`), procédure v15
(`6e9782c0…`) et règle v3 (`8dcff8dc…`) : **inchangés**.

### Ce qui change depuis la v11

1. **Mot de Lazar pour la cinquième machine** : le champ « [GO À CITER] » est rempli par **GO-2026-11-22-42**
   (`registres/go.md`, mots de Lazar reçus vers 2026-11-22T11:22:44Z : « go essai 5 »). La dépense reste sous
   **GO-2026-11-10-13** (65 USD, échéance le 30 novembre ; 1,12 USD dépensés par quatre serveurs, chiffres relus dans
   `registres/go.md` et `registres/depenses.md` le 2026-11-22), comme le redit GO-2026-11-22-43 (« essai Lean 5 sous
   GO-2026-11-10-13 »). La phrase d'arrêt « si ce champ porte encore « [GO À CITER] » » est retirée.
2. **Échéance de l'accord** : GO-2026-11-22-42 porte l'échéance du 2026-11-26. Aucune préparation si L1 tombe après le
   2026-11-26 à 23:59 UTC (garde de la Déclaration ; borne plus étroite que celle du 30 novembre, qui reste).
3. **Mandat 1** : contrôle neuf, sur `main`, des deux lignes de `registres/go.md` (GO-2026-11-22-42 porte « go essai 5 » ;
   GO-2026-11-10-13 porte 65 USD et le 2026-11-30). Un écart : arrêt. Le résultat va au premier message.
4. **Phrase de lancement** (« Avant de lancer », point 14) : elle nomme la v12 ; elle n'est plus suspendue au mot de Lazar,
   reçu, mais au versement de la v12 sur `origin/main`.
5. **Pourquoi** : l'objet de l'essai est dit en une phrase (éprouver sur machine la correction du cas 137 et la règle de
   combinaison, avant le pilote mathématique), et ce qu'il ne prouve pas.
6. **Lecture du cas 137** (mandat 7) : la borne « temps de processeur inférieur à 1 s » du § 8.2 se lit sur `temps.cpu_s`
   de la pièce ; l'épreuve v9 ne l'applique pas ; un dépassement que la pièce dit conforme est un désaccord à la
   concordance, rapporté tel quel.
7. **Réserves**, les sept phrases périmées listées par la troisième passe du contre-lecteur (R-4824), corrigées :
   (a) « Vérification des corrections due » : faite, bilan écrit ; (b) « Points à faire relire par Fable » : relus, bilan
   écrit ; (c) « règle v2 comprise » devient la règle v3, et « H8 » est nommé par ce qu'il décrit ; (d) codes 124 et 255
   du pilote « avant » : tranchés, lus « non établi » ; (e) « Limite de la vérification » : différences de la v15 par
   rapport à la v14 ajoutées ; (f) réserve neuve : borne de 1 s non codée dans l'épreuve v9 ; (g) en-têtes v11 et v10
   gardés comme historique, dit ci-dessous. S'y ajoutent la réserve « Mot de Lazar pour la cinquième machine », mise à
   jour, et la remarque de la même passe sur un code 124 venu de l'outillage lui-même.

Le reste de la v11 suit sans changement. **Les en-têtes v11, v10, v9 et v8 qui suivent sont un historique** : ils parlent
de la règle v2, de la procédure v14, du champ « [GO À CITER] » et d'une « liste des points à faire relire » ; ce qui vaut
est l'en-tête v12 ci-dessus et le corps de la consigne.

**v11 (2026-11-22, vers 09:45 UTC, `date -u`)** : écrite par un développeur Opus 5.5 (`claude-opus-5-5`), sous-agent de la
session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`, à sa demande. Remplace la v10 (`consigne-poste-local-lean-d1a-v10.md`,
`3a8f830acd87c5bb245e09ef962d3f3e7497f3a893d5250e65af18a768b1944c`), gardée telle quelle (R12). Différentiel :
`differentiel-consigne-v10-v11.diff`. **Ce qui change, et lui seul** : les renvois vers l'apport v3
(`apport-essai-5-correction-137-et-combinaison-v3.patch`, 50 fichiers neufs sur `47c7faaf` : les 40 de l'apport v2,
inchangés, plus la règle de combinaison v3, ses essais, ses mutations, la procédure v15 et le journal v3, d'après la
relecture des critères par Claude Fable 5.2, `relecture-fable-api.md`, `c3495cbd…`) et vers la procédure v15 ; la phrase de
lancement, qui nomme la v11. Le champ « [GO À CITER] » reste tel quel. Le reste de la v10, en-tête compris, suit sans
changement.


**v10 (2026-11-22, vers 09:20 UTC, `date -u`)** : écrite par un développeur Opus 5.5 (`claude-opus-5-5`), sous-agent de la
session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`, à sa demande, sur la contre-lecture de la v9 et de l'apport v1 (« à
corriger »). Pièce d'instrument (classe B) : vérification des corrections par le même contre-lecteur **avant usage**.
Remplace la v9 (`consigne-poste-local-lean-d1a-v9.md`, `b75e71b18a636e146b3ee991d686e267d3c928dcf7467b58e35f9621a0963ffd`),
gardée telle quelle (R12). Différentiel : `differentiel-consigne-v9-v10.diff`. **Ce qui change** :
- **l'apport v2** (`apport-essai-5-correction-137-et-combinaison-v2.patch`, 40 fichiers neufs sur `47c7faaf`) : les 30
  fichiers de l'apport v1, inchangés, plus la règle de combinaison v2 (`conformite_outillage_v2.py`, corrections B1, B2 et
  non bloquante 7), ses essais, la procédure v14 et le journal v2 ; la règle v1 et la procédure v13 restent (R12) et ne
  servent plus ;
- **la déclaration de la cinquième machine** cite le mot de Lazar qui l'accorde (B3) : champ à remplir par la mère, et la
  phrase de lancement n'est donnée qu'après ce mot ;
- **le mandat 1** joue la règle v2 sous le Python du poste sur les pièces du quatrième essai (attendu : code 1, « non
  conforme » sur le seul cas 137) ; la réserve sur les versions de Python éprouvées est remise ;
- **le repli par la branche** : la mère relit `-v7` toutes les 10 minutes et accuse réception de chaque message poussé ;
  second repli si aucun accusé sous 30 minutes ;
- **le code de sortie des pilotes** : l'entier seul, par `echo $? > <fichier>` ;
- **les règles** : le service d'adresse permis dès le mandat 1 ; `git write-tree` déclaré comme écart accepté à la règle 9 ;
- **les réserves** : branche `-v7` depuis `47c7faaf` par décision de la mère (R-4808) ; liste des points à faire relire par
  Fable 5.2.

Le reste ne change pas. L'en-tête de la v9 suit, mis à jour sur les seuls points de la contre-lecture.

**Ce que la v9 changeait (2026-11-22, vers 08:45 UTC)** : la v9 remplaçait la v8 (`consigne-poste-local-lean-d1a-v8.md`,
`3279bf4256b8c1eab212b2ff76c6ce7155d76863253d18b5f812d0f486cf1ed5`) et son erratum 1
(`consigne-poste-local-lean-d1a-v8-erratum-1.md`, `84bdfff6539bfbb785ced642384315a9f6485beba8c5411ae8c280def4e46d8e`),
gardés tels quels (R12). Différentiel : `differentiel-consigne-v8-v9.diff`. Ce qu'elle changeait :
- **l'erratum 1 est fondu** dans le texte (mère, session du poste ouverte par Lazar, branche neuve, phrase de lancement) ;
- **la mère** est désormais `session_01XJ6Mgr4LgbMsg5zLyRZCpG`, partout (en-têtes historiques exceptés) ;
- **la session du poste** est ouverte par Lazar sur son ordinateur, avec le compte de cette mère, après qu'il a fermé toute
  session précédente du poste ;
- **la branche** est `donnees/lean-outillage-d1a-poste-local-v7`. Dernier commit de `donnees/lean-outillage-d1a-poste-local-v6`,
  relevé le 2026-11-22 à 08:20Z environ : `86aabc842a1f98ce5c7e2cce40f9d1e3a6248175` (« dernier message à la mère (rapport
  v4) »). **La branche `-v7` n'en part pas** : cette tête porte, dans `V`, le fichier de rattrapage et le journal des
  créations du quatrième essai (`rattrapage-machine-d1a-fae70647f54e-v1.json`, `journal-creations-machines-v1.jsonl`) ;
  `preparer` refuserait (« une préparation existe déjà », CLC5-03), et rien ne doit en être supprimé. Elle part de
  `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b`, comme `-v5` et `-v6`, et reçoit l'apport ci-dessous. **Décision de la mère,
  R-4808** ;
- **l'apport du cinquième essai** (fichiers neufs seulement) : correction de l'artefact du cas 137 et règle de combinaison
  (noyau, épreuve, mesures), avec la procédure v13, le pilote v13 et l'épreuve v9. Il vient de `main` sous la forme d'un
  correctif à appliquer (`apport-essai-5-correction-137-et-combinaison-v1.patch` en v9 ; **v2 depuis la v10**, procédure
  v14) ;
- **la dépense** : 1,12 USD déjà dépensés (quatre serveurs), `--deja-depense-usd 1.12` ;
- **les messages** : repli par la branche, accepté au quatrième essai sur les mots de Lazar, écrit d'avance et gardé (ajout
  à la demande de la mère ; accusés de réception depuis la v10).

Le reste ne change pas : dépense GO-2026-11-10-13, plafond 65 USD, échéance le 30 novembre à 23:59 UTC, une seule machine,
gestes de Lazar et de la mère, règles. L'en-tête de la v8 ci-dessous est résumé.

**v8 (2026-11-21, vers 14:26 UTC, `date -u`)** : écrite par un rédacteur Opus 5.5 (`claude-opus-5-5`), sous-agent de la
session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`, à sa demande. Pièce d'instrument (classe B). Remplace la v7
(`consigne-poste-local-lean-d1a-v7.md`, `11be3c275b312d9dd19d70a96911147f03498202c26db76591ab7c0da1e80979`), gardée
telle quelle (R12). Différentiel : `differentiel-consigne-v7-v8.diff`. Corrections E1 (heure de démarrage du processus 1
d'Ubuntu), E2 (`env -u NOM <commande>`), E3 (accusé de réception avant L1) et adresse du poste lue par la session (écart 2
du rapport v3), d'après la vérification `verification-consigne-v7-v1.md` (`d114dce8…`) et son erratum 1 (`83e101df…`).
Erratum 1 du 2026-11-21T15:43:54Z (mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`) : mère, session du poste, branche `-v6`, phrase
de lancement. Les en-têtes v7 et v6 restent lisibles dans la v8.

**Rappel : le quatrième essai a eu lieu le 21 novembre** (rapport v4, `a0f5075d97dbffdc40d2acf9365d8ee7e35eef88cafecc02ceb71bba36e8c783`,
branche `donnees/lean-outillage-d1a-poste-local-v6`, commit `90d0ef8d`). Serveur 177109613 (`ccx33`, `hel1`), de 18:53:18Z
à 19:11:58Z, détruit par son identifiant, environ 0,28 USD. Résultats :
- **pilote « avant »** : code 0, trois essais R5 conformes ;
- **pas `noyau`** : conforme, 18 cas sur 18 ;
- **épreuve d'isolement** : non conforme, 35 cas sur 36. Seul en échec : « sortie de lui-même en code 137, sans consommer la
  limite (5 s) », écart « stdout sans « SORTIE 137 » » ;
- **mesures** : passage en parallèle compté ; **sondes** : fermées.

Lecture de conformité par un lecteur neuf (`lecture-conformite-d1a-quatrieme-essai-v1/lecture-conformite-v1.md`,
`bd5d2d91…`, R-4687) : « non établi », la procédure ne disant ni si ce cas bloque, ni comment combiner les lectures. Lazar a
choisi l'option (b) pour le quatrième essai : écart toléré et déclaré (R-4716). La cause est établie hors machine :
l'artefact écrit puis sort par `os._exit` sans vider le tampon de la sortie standard. Elle est corrigée par l'apport, qui
écrit aussi la règle de combinaison (procédure v13, § 8.7 ; règle v2 et procédure v14 depuis la v10 ; règle v3 et
procédure v15 depuis la v11).

**Tu ne pousses rien vers `donnees/lean-outillage-d1a-poste-local-v3`, `-v4`, `-v5` ni `-v6`**, et tu n'en supprimes rien.
Tu peux lire le rapport v4 sur `-v6` (mandat 1). Tu ne reprends aucun clone, aucune clé, aucun fichier de rattrapage, aucune
sortie et aucune minuterie d'un essai antérieur ni d'une session précédente du poste.

## Avant de lancer — ce que Lazar a sous la main

1. **Le poste sous WSL (Ubuntu)**, sur secteur, veille coupée, capot ouvert, sans déconnexion de la session jusqu'à la
   destruction du serveur (procédure, section 0, point 7).
2. **Un terminal Ubuntu ouvert pendant tout l'essai**, **ouvert avant de lancer la session** et gardé ouvert jusqu'à
   l'inventaire final de la section 5 ; la session dit à Lazar quand il peut le fermer. Sans fenêtre WSL ouverte, WSL
   arrête Ubuntu et tue les processus détachés, minuterie comprise (incident R-2434).
3. **La clé de l'interface de Hetzner, par son nom seul : `HCLOUD_TOKEN`**. C'est un jeton en lecture et écriture du projet
   de l'essai, posé par Lazar dans l'environnement de la session (procédure, section 0, point 3). Elle n'est jamais collée
   dans la conversation, ni affichée, ni écrite dans un fichier, ni passée en argument.
4. **`gh` authentifié sur le dépôt privé `lciric/controle-ia-travail`** : son jeton ne passe qu'à `git`, par
   l'environnement du processus.
5. **L'adresse publique du poste (`IP_POSTE`)** : lue par la session depuis Ubuntu, par une requête au service que
   `MV7 adresses-sortie` interroge, ou donnée par Lazar s'il le préfère. Elle reste dans la conversation : jamais écrite
   dans un fichier du clone ni dans un message.
6. **Python 3.11 ou plus récent, `git`, `ssh`, `ssh-keygen`** sous Ubuntu. Au quatrième essai : Python 3.14.4, seule version
   présente, sans incident, **alors que le harnais (minuterie, garde, pilote) n'est éprouvé hors machine que sous 3.11 et
   3.13** ; la règle de combinaison v3 l'est sous 3.11, 3.12, 3.13 et 3.14.6 (journal v3), et le mandat 1 la joue sous le
   Python du poste. Aucune installation.
7. **Le réglage hors du bac à sable** pour les commandes du harnais, pré-autorisées (procédure, section 0, point 4). Il
   faut aussi le temps d'une fin et d'une reprise réelles de l'hôte de la session, **seulement si l'essai à blanc est
   refait** (mandat 2) ; l'arrêt de l'application par le Gestionnaire des tâches ferme alors toutes ses sessions locales :
   n'en avoir aucune autre au travail.
8. **Ses réponses à la question « le poste a-t-il changé ? »** (mandat 2) : même ordinateur et même compte Windows ? même
   application Claude ? même réglage ? mise à jour de Windows, de WSL ou de l'application depuis le quatrième essai ? même
   compte Claude qu'au quatrième essai, et le réglage hors du bac à sable et les pré-autorisations valent-ils pour lui ?
9. **La session du poste** : Lazar l'ouvre sur son ordinateur, **avec le compte de la mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`**,
   comme session fille de celle-ci, **après avoir fermé toute session précédente du poste** : jamais deux sessions sur le
   même essai.
10. **Plus de relais** : la session du poste et la mère s'écrivent directement, avec le repli par la branche (section
    « Messages »). Lazar ne relaie que si les deux manquent.
11. **Durée attendue : environ 1 h 30 à 2 h 30 de terminal ouvert** (estimation).
    - Au quatrième essai : premier message à 17:27:31Z, rapport vers 19:25Z, soit environ 2 heures, dont un essai à blanc
      refait (relance de l'application) et des échecs de l'envoi direct.
    - De L1 (vers 18:47Z) à la destruction (19:11:58Z) : environ 25 minutes. Le serveur a vécu 18 min 40 s.
12. **Coût attendu : environ 0,28 USD**, soit une heure facturée d'une `ccx33` (0,22692 EUR au taux de 1,25,
    `registres/depenses.md`), si le serveur vit moins d'une heure. Sa vie est bornée par la minuterie, au plus
    `min(création + 48 h, H − 1 h)`. Le coût reste en tout cas sous le reste de la ligne, 63,88 USD.
13. **Son rappel personnel à `H + 1 h`** (procédure, M6 : console de Hetzner, zéro serveur attendu ; `H` lui est donné par
    la mère et par la session du poste) et **l'accès à la console de Hetzner du projet**, pour détruire à la main par
    l'identifiant si `MV7 detruire` rend le code 3 (sections 4 et 5).
14. **La phrase de lancement** qu'il tape porte le chemin de cette consigne sur `origin/main` et son empreinte ; le premier
    message rend l'empreinte à la mère, qui la compare. Le mot de Lazar qui accorde la cinquième machine est reçu
    (GO-2026-11-22-42, « Dépense autorisée », Déclaration) ; **la phrase ne lui est donnée qu'après le versement de la v12
    et de son compagnon sur `origin/main`**, et au plus tard le 2026-11-26. Forme : « Lis et exécute la consigne
    `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/consigne-poste-local-lean-d1a-v12.md` du dépôt
    `lciric/controle-ia-travail`, sur `origin/main`, empreinte sha256 `<empreinte de la consigne v12>` ; tu es la session du
    poste local du cinquième essai Lean D-1a, fille de la session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`. »

Cette liste est une liste de contrôle ; dans le temps, les gestes de Lazar vont ainsi : fermeture de toute session
précédente du poste ; secteur, veille et capot ; terminal ; clé du loueur et `gh` ; lancement ; adresse du poste (s'il la
donne) ; réponses sur le poste ; relance de l'hôte si l'essai à blanc est refait ; rappel personnel à `H + 1 h` ; console en
cas de code 3 ; fermeture du terminal.

Session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG` (dans le nuage). Elle agit sous GO-2026-11-10-13 et sur le choix de Lazar
du 21 novembre (R-4716 : option (b) pour le quatrième essai, correction de l'artefact et règle de combinaison à faire),
avec les mots GO-2026-11-21-40 (« on ne s'arrete pas a un echec avant d'avoir compris les causes de cet ecec et avoir reussi
a les corriger ») et GO-2026-11-21-57 (essai Lean poursuivi). La cause du cas 137 est établie et corrigée hors machine
(procédure v15, « Rappel : changements de la v12 à la v13 »).

**Code** : branche `prep/lean-outillage-d1a-v11`, commit `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b` (code au commit
`3c2f35dd`), **plus l'apport** :
- fichier sur `origin/main` : `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/apport-essai-5-correction-137-et-combinaison-v3.patch` ;
- empreinte du correctif : `949d2d6a1e6ceb4d252e8094c25c7a096cffc08b165764563ca2dd28626675cc` ;
- **50 fichiers neufs** (les 40 de l'apport v2, inchangés, et 10 de plus), aucun fichier existant modifié
  ni supprimé ;
- arbre attendu après application sur `47c7faaf` (`git write-tree`) : **`ab77bbac454b3c4723eab8ed9306b20031502c2d`** ;
- les correctifs v1 (`8f6c1046…`, arbre `fa8d0917…`) et v2 (`474da970…`, arbre `c8951f6a…`) restent sur `main` et **ne
  s'appliquent pas**.

**Pourquoi** : le cinquième essai rejoue tout le quatrième, avec l'artefact du cas 137 corrigé (`limite_code137_v2.py`,
attendus v8, mêmes attentes), l'extrait de la sortie standard du genre « limites » dans la pièce de l'épreuve, et la
lecture combinée de la procédure v15, § 8.7 (règle v3), écrite avant l'essai. Seule la machine dira si l'artefact v2 sort « SORTIE
137 » sous `/opt/pybac/bin/python`. **Objet** : éprouver sur machine la correction du cas 137 et la règle qui combine
noyau, épreuve et mesures, avant le pilote mathématique (D-1b). L'essai ne dit rien du vérificateur sur de vraies preuves ni
d'un modèle : aucun appel de modèle n'y a lieu.

**Tu es une session fille** : ton mandat est **cette consigne seule** ; tu ne reprends aucune autre tâche du programme. Tu
n'écris jamais dans `main`, jamais vers `lciric/controle-ia`, jamais une ligne de `registres/go.md` ; la session mère
inscrit dépenses, arrêts et décisions d'après tes messages et ton rapport.

**Dépense autorisée** : **GO-2026-11-10-13**, 65 USD au plus, **échéance 2026-11-30** (`registres/go.md`). **1,12 USD sont
déjà dépensés** par les quatre premiers serveurs, 175751342, 175838427, 177067030 et 177109613 (quatre fois 0,28 USD,
`registres/depenses.md`).
- **Une seule** machine Hetzner `ccx33` (`hel1`) de plus, vie bornée par la minuterie. Elle est **créée et détruite par
  la procédure** :
  - création en L5 par `creer-et-armer` ;
  - destruction en section 5 par `MV7 detruire --identifiant N` ;
  - en fin anormale de la création, où l'identifiant peut manquer : destruction en section 4 par `MV7 detruire --pas d1a`,
    qui détruit par les étiquettes fixes et le nom de l'essai.

  La destruction se fait **toujours par l'identité de l'instance chez le loueur, jamais par un motif (R10)**. Tu n'arrêtes
  jamais un processus par motif de ligne de commande, seulement par le PID que la procédure te fait relever.
- **Échéance** : aucune préparation si `T_LIM` (L1 + 6 h) tombe après le 2026-11-30 à 23:59 UTC ; compte rendu à la mère.
- **Clé du loueur** : `HCLOUD_TOKEN`, lue par son nom seul dans l'environnement de la session, jamais affichée ni écrite.
- **Aucun appel de modèle**, **aucune clé de modèle ni dépôt du programme sur la machine**. Aucune autre dépense.
- **Déclaration (comme R-2426, R-2439 et GO-2026-11-21-40)** : c'est la **cinquième machine sous cette ligne**. La garde
  « une machine par GO » du harnais est **contournée par construction** : ta branche neuve ne porte ni fichier de
  rattrapage ni journal des créations des essais précédents. La garde lit aussi le registre des dépenses de la branche, qui
  ne porte au commit `47c7faaf` aucune ligne de cet accord : sur ta branche, **`--deja-depense-usd 1.12` est la seule trace
  de la dépense réelle** (sans lui, le code retient 0 et ne refuse pas). Le contournement ne vaut que pour cet essai : une
  préparation, une création.
  - **Mot de Lazar qui accorde cette cinquième machine** : **GO-2026-11-22-42** (`registres/go.md`, ligne de décision
    inscrite par la mère ; mots de Lazar reçus vers 2026-11-22T11:22:44Z, verbatim pour ce point : « go essai 5 »). La
    dépense reste sous GO-2026-11-10-13 et sous son plafond ; GO-2026-11-22-43 le redit (« essai Lean 5 sous
    GO-2026-11-10-13 »). Tu contrôles ces deux lignes au mandat 1.
  - **Échéance de l'accord** : GO-2026-11-22-42 porte l'échéance du 2026-11-26. **Aucune préparation si L1 tombe après le
    2026-11-26 à 23:59 UTC** ; compte rendu à la mère, qui demande à Lazar un mot neuf. Cette borne s'ajoute à celle de
    `T_LIM` (30 novembre) et ne la remplace pas.

## Messages entre le poste et la mère (v9, accusés de réception du repli en v10)

- **Canal** : tes messages vont **directement à la session mère** `session_01XJ6Mgr4LgbMsg5zLyRZCpG`, par l'outil d'envoi
  de messages entre sessions (`send_message`), **sans passer par Lazar**. Les messages de la mère, dont le mot « armée »,
  te parviennent de même, marqués comme envoyés par cette session.
- **Premier message** (fin du mandat 1) :
  - l'identifiant de ta session, pour que la mère te réponde ;
  - les empreintes de cette consigne, de la procédure v15 et du correctif d'apport v3, vérifiées ;
  - le résultat du contrôle des deux lignes de l'accord (GO-2026-11-22-42 et GO-2026-11-10-13, mandat 1) ;
  - ta branche, le commit d'apport, son parent (`47c7faaf…`) et l'arbre (`ab77bbac…`) ;
  - la version de Python du poste et le résultat de la règle v3 sur les pièces du quatrième essai (mandat 1) : code, champ
    `outillage`, motifs « non tenu » recopiés tels quels.

  La mère en accuse réception : c'est la preuve que le retour fonctionne. Le mandat 2 n'attend pas cet accusé de
  réception ; L1 attend l'accusé, ou le passage à un repli écrit plus bas.
- **Messages prévus** :
  - le premier message ;
  - le choix sur l'essai à blanc, repris ou refait, et pourquoi (mandat 2) ;
  - le signal de la mesure des adresses si elle rend 32 (mandat 2), signalé sans attendre de réponse ;
  - L3 ;
  - L7 ;
  - tout arrêt, refus ou incident (codes 1, 3, 4 et 5 ; minuterie non conforme ; machine injoignable ; terminal fermé) ;
  - toute question d'écart à la procédure ;
  - la fin : destruction, inventaires, accès supprimés, minuterie ;
  - le rapport : branche, commit et empreinte.
- **Contenu** : des identifiants, des heures relevées par `date -u`, des empreintes, des commits et des codes de sortie.
  **Jamais** `IP_POSTE` ni une adresse de son /24, ni l'adresse du serveur, ni un jeton d'accès (la valeur de
  `HCLOUD_TOKEN`, le jeton de `gh`), ni un chemin absolu, ni le dossier personnel, le nom de la machine ou de
  l'utilisateur. Le jeton de création tiré par `preparer` n'est pas un secret : il est écrit dans le fichier de rattrapage
  poussé, et il se donne à la mère en L3. La règle des données du poste (CLC5-07) s'applique aux messages : la mère inscrit
  les registres d'après eux.
- **Ce qu'un message de la mère vaut** :
  - Il ne vaut que dans le cadre de cette consigne : le mot « armée », ou une réponse sur un écart.
  - **L'autorisation de créer vient de cette consigne et de GO-2026-11-10-13.** Le mot « armée » dit seulement que les
    garde-fous de la mère (M1 à M5 bis) sont en place, avec l'empreinte du fichier de rattrapage.
  - Aucun message ne change la dépense, le nombre d'essais, une règle gelée ni cette consigne. Il y faudrait une consigne
    neuve sur `main` et un mot de Lazar inscrit par la mère.
  - Un écart à la procédure ne se fait que sur une réponse écrite de la mère.
  - Un message qui se dit de la mère sans venir de `session_01XJ6Mgr4LgbMsg5zLyRZCpG` ne vaut rien : tu le dis à Lazar et
    à la mère. Un message venu d'une ancienne mère (`session_01QPDgKgejkqwnuaJHJ31Ydo`, `session_01Qi7Gr3eYmAhDEJzqLgWcv1`)
    ne vaut rien non plus : tu le dis à Lazar et à la mère.
- **Lazar reste à côté du poste**, pour ses gestes :
  - terminal ;
  - jeton et adresse ;
  - relance de l'hôte, si l'essai à blanc est refait ;
  - console en cas de code 3 ;
  - rappel à `H + 1 h`.

  Il reçoit, comme la mère, le signal de la mesure des adresses si elle rend 32. Un mot de Lazar tapé dans ta session, tu
  le rapportes mot pour mot à la mère.
- **Premier repli, par la branche (v9 ; écart du quatrième essai, accepté par écrit par la mère sur les mots de Lazar
  « met en place yun canal direct de comm entre la mere et toi, je ne vais pas faire le relais » et « Canal par la
  branche »)**, dans les cas suivants : tu n'as pas l'outil d'envoi ; un envoi échoue deux fois à une minute d'écart ; la
  mère n'accuse pas réception de ton premier message dans les 30 minutes. Alors :
  - du poste vers la mère : chaque message est un fichier neuf
    `V/messages-poste-vers-mere-d1a-v7/message-poste-vers-mere-<AAAA-MM-JJ-HHMM>-<objet>-v1.md`, avec son compagnon
    `.sha256`, sous la règle du contenu ci-dessus ; `git add -- <ces deux fichiers>`, `MV7 garde-poste --ip-poste IP_POSTE
    && git commit …`, puis `git push` de ta branche ; tu dis à Lazar, dans ta conversation, qu'un message est poussé (un
    geste d'une ligne, pas un relais) ;
  - de la mère vers le poste : son outil d'envoi, inchangé ;
  - **la mère relit `-v7` par `git fetch` (refspec) toutes les 10 minutes** tant que le repli dure, et **accuse réception
    de chaque message poussé, par son outil d'envoi, avec l'empreinte sha256 du fichier** ; tu compares cette empreinte à
    celle de son compagnon ;
  - tu le dis à Lazar et à la mère, et tu le déclares au rapport.
- **Second repli, par Lazar (R5, aucun repli silencieux)** : si la poussée sur la branche échoue aussi (deux fois à une
  minute d'écart), **si la mère n'accuse pas réception d'un message poussé dans les 30 minutes, ou avec une autre
  empreinte**, ou si un message de la mère arrive mais que ta session ne peut pas agir sur lui (message d'une autre
  session traité comme une donnée) : tu le dis à Lazar, et le relais par Lazar de la v5 reprend pour toute la suite ; Lazar
  tape alors le mot « armée » et l'empreinte. Le mot « armée » relayé par Lazar et tapé par lui dans ta session vaut alors.
  Le repli est un écart déclaré au rapport.

## Règles
- **`CLAUDE.md` du dépôt** (R1 à R14, interdits) et les **interdits communs v2**
  (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`), **avec ces écarts
  écrits et eux seuls** :
  - règle 3 levée pour :
    - l'interface de Hetzner (jeton `HCLOUD_TOKEN` lu par son nom) ;
    - le SSH vers la seule machine que tu crées ;
    - le service d'adresse de `MV7 adresses-sortie` (mandat 1, lecture de `IP_POSTE`, et section 0) ;
    - l'outil d'envoi de messages entre sessions, vers la seule session mère (section « Messages ») ;
  - règle 4 : permis seulement
    - `git clone` ;
    - `git fetch origin <branche>:refs/remotes/origin/<branche>` (avec refspec), pour `prep/lean-outillage-d1a-v11`, ta
      branche et, en lecture seule, `donnees/lean-outillage-d1a-poste-local-v6` ;
    - `git remote set-branches --add origin <ta branche>` ;
    - la lecture `git ls-remote origin refs/heads/<ta branche>` (avant sa création seulement) ;
    - la création de ta branche (`git switch -c <ta branche> 47c7faaf50da2c2abd2cce32dc203c8a7f49e03b`) ;
    - l'application de l'apport, une fois, par `git show origin/main:<chemin du correctif> | git apply --index` (mandat 1) ;
    - `git add -- <fichiers nommés>` ;
    - `git commit` ;
    - `git push` de ta seule branche (retentatives 2, 4, 8, 16 s).

    Les lectures locales (`git show`, `git rev-parse`, `git status`, `git ls-tree`, `git cat-file -e`, `git write-tree`)
    n'écrivent rien sur le dépôt distant.
  - **règle 9 : écart accepté pour `git write-tree`** (mandat 1, une fois) : il hache tout l'index, entrées de
    `docs/notes/bras-attaque/` comprises, sans en lire ni en afficher le contenu (il ne lit que les empreintes déjà
    portées par l'index) ; il sert seul au contrôle de l'arbre de l'apport. Aucun autre outil qui hache un arbre entier ;
    jamais `verifier-arbre .`.
- **La procédure fait foi pour tous les gestes de la machine** :
  `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v15.md`, portée par l'apport v3, sur ta
  branche après le mandat 1. Les procédures v13 et v14, aussi portées par l'apport, ne servent pas.
  - Empreinte entière vérifiée avant lecture : `6e9782c0c898b5a605c988ffbb64e3910346716132be940ad923058227a50899`.
  - Sections 0 à 8, **en entier et dans l'ordre**, avec les précisions ci-dessous. Notation `MV7`.
  - **Point de départ de ta branche** : `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b`, plus le seul commit d'apport (mandat 1).
  - **Écart écrit au rôle de Lazar** : la procédure le fait relayer entre les deux sessions (« Rôles et règle d'or » ; L3 ;
    M6 ; L7 ; section 3 ; section 5, point 5 ; de même section 0, points 4 et 5, et section 4, point 4). Sous cette
    consigne, ces messages vont directement du poste à la mère et de la mère au poste, avec les replis écrits ci-dessus.
    Rien d'autre ne change dans les gestes de la mère, M1 à M6, sauf M1 bis ci-dessous.
- **Poste** : sous WSL (Ubuntu), clone dans le système de fichiers Linux ; le jeton de `gh` ne passe qu'à `git`
  (environnement du processus), jamais écrit ni affiché. Commandes lancées depuis la racine du clone ; au quatrième essai,
  depuis l'hôte Windows par `wsl.exe -e`, les processus détachés vivant dans Ubuntu (écart 8 du rapport v3, repris au
  rapport v4).
- **Environnement des commandes du harnais** : aucune clé de modèle. Celles que `WSLENV` transmet à Ubuntu sont retirées
  de l'environnement de chaque commande (procédure, section 3) : leurs noms se lisent dans `WSLENV` (des noms, jamais des
  valeurs), puis chaque commande du harnais est lancée par `env -u NOM <commande>` ; jamais `env -u NOM` sans commande à la
  suite, ni `env` ni `printenv` seuls : ils afficheraient les valeurs. Seuls restent `HCLOUD_TOKEN` et, pour `git`, le jeton
  de `gh`.
- **Terminal WSL ouvert pendant tout l'essai** (incident R-2434 : sans fenêtre WSL ouverte, WSL arrête Ubuntu et tue les
  processus détachés, minuterie comprise) :
  - un terminal Ubuntu ouvert par Lazar avant de lancer la session, gardé ouvert **jusqu'à l'inventaire final** de la
    section 5 ;
  - vérifie-le avant l'essai à blanc et avant L1 : Ubuntu démarrée avant l'ouverture et jamais redémarrée depuis ; sinon,
    aucune préparation. Contrôle : l'heure de démarrage du processus 1 d'Ubuntu (`ps -o lstart= -p 1`), relevée au début
    du mandat 2 puis juste avant L1, à deux minutes d'écart au moins, doit être la même aux deux relevés, à deux secondes
    près. `uptime -s` ne suffit pas : il donne le démarrage de la machine virtuelle de WSL, qui peut survivre à un arrêt
    d'Ubuntu ;
  - s'il se ferme après L5 : `MV7 verifier-minuterie` tout de suite ; non conforme : `MV7 detruire --identifiant N`,
    jamais de relance ; message à la mère.
- **Données du poste (CLC5-07)** :
  - identité Git neutre pour ce clone seulement (`poste-local`, `poste-local@invalid`, sans `--global`), vérifiée avant
    chaque commit ;
  - avant chaque commit : `git add -- <fichiers nommés>` (pour le commit d'apport : l'index posé par `git apply --index`),
    puis `MV7 garde-poste --ip-poste IP_POSTE && git commit …`, `git commit` sans `-a` et sans chemin, car la garde ne lit
    que l'index ;
  - chaque sortie du pilote ou d'un processus détaché passe `MV7 garde-poste --ip-poste IP_POSTE --fichier <pièce>` avant
    d'être versée (la garde refuse aussi toute adresse du /24 du poste) ; une copie versée où l'adresse du serveur est
    masquée se déclare avec les empreintes de l'original et de la copie (écart 6 du rapport v3) ;
  - jamais versés ni écrits dans un message : l'adresse du poste ni aucune adresse de son /24, le dossier personnel, le
    chemin absolu du clone, le nom de la machine ou de l'utilisateur. Aucune sortie de `adresses-sortie` n'est versée (elle
    ne porte que des comptes).
- **Mandataire** : la lecture du mandataire (mandat 2) doit rendre `[]`, comme aux troisième et quatrième essais ; sinon
  arrêt.
- **Délais des outils** : `detruire` et `inventaire` jusqu'à environ 9 minutes : délai d'outil d'au moins 10 minutes, ou
  arrière-plan.
- **Refus** d'un contrôle de permissions ou d'un classifieur : arrêt sur ce point, destruction du serveur s'il existe
  (section 4), message à la mère, rapport ; ni contournement, ni reformulation.
- **Un seul essai** : une préparation (L1, **jeton neuf** tiré par `preparer`), une création ; **aucun autre essai** sans
  consigne neuve de la mère et accord de Lazar.

## Mandat
1. **Dépôt** (dans cet ordre) :
   - clone neuf, par `git clone --single-branch --branch main https://github.com/lciric/controle-ia-travail.git <dossier neuf>`,
     dans un dossier au nom neuf du système de fichiers d'Ubuntu ;
   - **rien des essais antérieurs n'est supprimé ni écrasé sur le poste** : ni clone, ni clé, ni dossier de sorties (les
     originaux des pièces des essais précédents n'existent que là). La clé de L2 et le dossier de sorties du pilote prennent
     des noms neufs (R12) ; si un nom existe déjà, tu en prends un autre. Aucune commande de suppression de fichier ou de
     dossier n'entre dans ce mandat ; s'il t'en semble falloir une, tu t'arrêtes et tu le demandes à Lazar ;
   - **tant que le clone est sur `main`** :
     - vérifie l'empreinte de cette consigne (`sha256sum -c` de son compagnon, dans son dossier, en sous-interpréteur) et
       qu'elle est celle de la phrase de lancement ;
     - routine de `CLAUDE.md`, point 1 **limité au `sha256sum -c` des documents de lancement** (`cd docs && sha256sum -c
       sha256sums-lancement-v2.txt`, en sous-interpréteur ; jamais `verifier-arbre .` : l'arbre du code porte
       `docs/notes/bras-attaque/`, chemin interdit), et point 2 (`registres/etat.md` et la dernière passation) ;
     - empreinte du correctif d'apport v3, par `sha256sum -c` de son compagnon dans son dossier : elle doit être
       `949d2d6a1e6ceb4d252e8094c25c7a096cffc08b165764563ca2dd28626675cc` ;
     - **les deux lignes de l'accord**, depuis la racine du clone :
       `grep -F '| GO-2026-11-22-42 |' registres/go.md | grep -c -F '« go essai 5 »'` doit rendre `1` (code 0), et
       `grep -F '| GO-2026-11-10-13 |' registres/go.md | grep -c -F '| 65 USD | 2026-11-30 |'` doit rendre `1` (code 0).
       Garde éprouvée le 2026-11-22 sur une copie saine (1 et 1) et sur trois artefacts (ligne retirée, autre mot, autre
       plafond : 0, code 1). Un autre résultat : arrêt, compte rendu, aucune préparation ;
   - **`IP_POSTE`**, maintenant, car le commit d'apport passe par `garde-poste` : donnée par Lazar, ou lue depuis Ubuntu
     comme au mandat 2 (une requête) ;
   - `git fetch origin prep/lean-outillage-d1a-v11:refs/remotes/origin/prep/lean-outillage-d1a-v11` ; le commit
     `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b` doit y être (`git cat-file -e 47c7faaf50da2c2abd2cce32dc203c8a7f49e03b^{commit}`,
     qui n'affiche rien : le critère est le code 0) ; si la tête de la branche a bougé depuis, tu pars quand même de ce
     commit et tu le dis au rapport ;
   - `git ls-remote origin refs/heads/donnees/lean-outillage-d1a-poste-local-v7` doit rendre le **code 0 et aucune ligne**.
     Une ligne rendue (la branche existe déjà) ou un code non nul (accès au dépôt en échec) : arrêt, compte rendu, aucune
     préparation ;
   - **ta branche** : `git switch -c donnees/lean-outillage-d1a-poste-local-v7 47c7faaf50da2c2abd2cce32dc203c8a7f49e03b` ;
     jamais `-v3` à `-v6` ; `git rev-parse HEAD` doit rendre `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b` et
     `git status --porcelain` rien ; sinon arrêt ;
   - **apport** :
     - `git show origin/main:docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/apport-essai-5-correction-137-et-combinaison-v3.patch | sha256sum`
       doit rendre `949d2d6a…` (la même empreinte que plus haut) ;
     - la même commande avec `| git apply --index --check` à la place de `| sha256sum` : code 0 ; puis avec
       `| git apply --index` : code 0, une seule fois ;
     - `git write-tree` (écart accepté à la règle 9, Règles) doit rendre `ab77bbac454b3c4723eab8ed9306b20031502c2d` ; `git status --porcelain` doit
       montrer **50 lignes, toutes `A `** (fichiers ajoutés à l'index), et rien d'autre ;
     - un écart à l'un de ces trois contrôles : arrêt, compte rendu, aucune préparation ; rien n'est réparé à la main ;
     - identité neutre vérifiée, `MV7 garde-poste --ip-poste IP_POSTE && git commit -m "Poste local D-1a, 5e essai : apport
       v3 (correction du cas 137, règle de combinaison v3), arbre ab77bbac"` ; puis `git rev-parse HEAD^` doit rendre
       `47c7faaf…` et `git rev-parse HEAD^{tree}` `ab77bbac…` ;
   - poussée par `git push -u origin donnees/lean-outillage-d1a-poste-local-v7`, puis la référence de suivi de la procédure
     (L3 : `git fetch` par refspec, `git remote set-branches --add`, `@{upstream}` résolu) ;
   - vérifie que `V` ne contient ni `rattrapage-machine-d1a-*-v1.json` ni `journal-creations-machines-v1.jsonl` ; sinon
     arrêt. Commande : `git ls-tree --name-only HEAD -- docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` doit montrer
     `procedure-poste-local-d1a-v15.md` (témoin que le bon arbre est lu) et aucun de ces deux noms ;
   - lis la procédure v15 sur ta branche et vérifie son empreinte (`6e9782c0…`) ;
   - vérifie les compagnons du code joué sur la machine et sur le poste, chacun par `sha256sum -c` dans son dossier, en
     sous-interpréteur depuis la racine (`(cd <dossier> && sha256sum -c <fichier>.sha256)`). Attendus :
     - `scripts/lean_essai_d1a_v13/piloter_poste_v13.sh` : `3daa9eeb471ef6dc99df33aa5323cbc23c1cb05101403b14a2eca75065f64a77` ;
     - `src/controle_ia/lean_essai/executeur_bac_v8.py` : `3b1dabd77f04d6d5f4129f2071348a29f0c25bbb55530f07e37500ece2c9d63d` ;
     - `src/controle_ia/lean_essai/epreuve_isolement_v9.py` : `6c355351b7184a41b66bd19d9324f36b873602b7f33aabd26045752f908fa3ad` ;
     - `scripts/lean_essai_d1a_v4/artefacts_r5_v4/attendus-v8.json` : `1b26ed38e25f466f04516b43b2ba7274ec0feae6ea8ed26b7c215f6c86fc6f01` ;
     - `scripts/lean_essai_d1a_v4/artefacts_r5_v4/limite_code137_v2.py` : `4b2e7a598940ec849b84d694eb7b49d7964c645f95c9fd43f2e6ffd41075c249` ;
     - `src/controle_ia/lean_essai/minuterie_v7.py` : `182033f8a70d36b652e94b81dc56060f5b806084641a8a17ca913ef66aceccd8` ;
     - `src/controle_ia/lean_essai/verificateur_noyau_v6.lean` : `3ef23bfa6600bf3a79fca2c31427dccf6c2ec7d67832bddb5c4df971a269d2ee` ;
     - `src/controle_ia/lean_essai/conformite_outillage_v3.py` : `8dcff8dca83976eee037b56e494131d3a21e7290ed03eeab2321a4abf46c8a59` ;

     l'empreinte lue doit être égale à celle de cette liste, pas seulement passer `sha256sum -c` ; un écart : arrêt,
     aucune préparation ;
   - **la règle v3 sous le Python du poste, sur les pièces du quatrième essai** (essai R5 sur le poste ; rien n'est écrit
     dans le clone) : relève `python3 --version`, puis, depuis la racine du clone,
     `env -u <clés de modèle> PYTHONPATH=src python3 -B -m controle_ia.lean_essai.conformite_outillage_v3 --sorties
     tests/donnees_conformite_outillage_v1/essai4-fae70647f54e --pilote-avant-code
     tests/donnees_conformite_outillage_v1/essai4-fae70647f54e/pilote-avant-code-v1.txt --pilote-apres-code
     tests/donnees_conformite_outillage_v1/essai4-fae70647f54e/pilote-apres-code-v1.txt > <dossier neuf hors du
     clone>/regle-v3-essai4-v1.json ; echo $? > <même dossier>/regle-v3-essai4-code-v1.txt`. **Attendu** : code 1,
     `outillage` « non conforme », et un seul motif « non tenu » dans tout le fichier, celui du cas « sortie de lui-même en
     code 137, sans consommer la limite (5 s) » (écart « stdout sans « SORTIE 137 » ») ; les motifs « non établi » de la
     version `epreuve_isolement_v8` des pièces du quatrième essai sont attendus et se recopient tels quels. Un autre
     résultat (autre code, autre issue, un autre motif « non tenu », une trace d'erreur) : arrêt, compte rendu, aucune
     préparation ; rien n'est réparé à la main. Le résultat va au premier message et au rapport ;
   - au besoin, pour le mandat 2 : rapport v4 lu sur `donnees/lean-outillage-d1a-poste-local-v6` (fetch par refspec, lecture
     seule ; tête attendue `86aabc842a1f98ce5c7e2cce40f9d1e3a6248175`, dite au rapport si elle a bougé), empreinte
     `a0f5075d97dbffdc40d2acf9365d8ee7e35eef88cafecc02ceb71bba36e8c783` ;
   - **premier message à la mère** (section « Messages »).
2. **Section 0 de la procédure** :
   - prérequis, dont le **terminal WSL ouvert** (Règles) ;
   - **le poste a-t-il changé ?** L'essai à blanc est un acquis du quatrième essai (rapport v4, § 3) :
     - `sleep 3600` (processus 8075, parti à 17:46:25Z) vivant après l'arrêt de l'application par le Gestionnaire des
       tâches et sa réouverture (`kill -0` en code 0 à 18:17:29Z) ;
     - l'hôte `claude.exe` créé à 18:16:44Z, plus récent que le `sleep` ;
     - preuve de relance par l'écart D1 (R-4453, R-4456, R-4485) ;
     - `getproxies()` : `[]`.

     Le poste **a changé** si l'un de ces points diffère du quatrième essai (rapport v4, § 3 et § 9) :
     - autre ordinateur ou autre compte Windows ;
     - autre distribution ou version d'Ubuntu sous WSL que **Ubuntu 26.04.1**, lue par toi
       (`grep -E '^(NAME|VERSION)=' /etc/os-release`) ;
     - autre hôte de la session que l'application Claude sous Windows (`claude.exe`), ou commandes lancées autrement que par
       `wsl.exe -e` depuis la racine du clone ;
     - réglage hors du bac à sable des commandes du harnais changé ;
     - mise à jour de Windows, de WSL ou de l'application Claude faite depuis le quatrième essai, à la connaissance de
       Lazar ;
     - **autre compte Claude qu'au quatrième essai**, ou réglage hors du bac à sable et pré-autorisations qui ne valent pas
       pour ce compte. Au quatrième essai, la session avait relevé, en lecture seule, aucun réglage de bac à sable dans les
       fichiers de l'utilisateur et aucune commande du harnais pré-autorisée (mode de permission « auto »).

     Tu demandes à Lazar ce qu'il est seul à savoir. **Un doute compte comme un changement.**
     - **Inchangé** : la partie « fin et reprise réelles » n'est pas refaite ; tu cites l'acquis au rapport, avec les
       réponses de Lazar et la version d'Ubuntu lue.
     - **Changé, ou doute** : essai à blanc entier, hors du bac à sable, selon la section 0, point 4, de la procédure v15
       (`sleep 3600`, puis fin et reprise réelles de l'hôte ; preuve par `ps -o lstart` ou, sous Windows, par l'écart D1).
     - **Dans tous les cas**, la lecture du mandataire se refait :
       `python3 -c "import urllib.request; print(sorted(urllib.request.getproxies()))"`. Elle lit l'environnement de ta
       session, neuf à chaque session : une commande, rien à relancer. `[]` attendu ; sinon arrêt, compte rendu, aucune
       préparation.
   - **`IP_POSTE`** (relevée au mandat 1) : si Lazar ne te l'a pas donnée, tu l'as lue depuis Ubuntu par
     `python3 -c "import urllib.request; print(urllib.request.urlopen('https://api.ipify.org', timeout=15).read(64).decode('ascii'))"`
     (une requête, le service de `adresses-sortie`). C'est un écart écrit à la procédure, qui la fait donner par Lazar
     (écart 2 du rapport v3, repris) ; tu le déclares au rapport. La mesure qui suit se fait comme écrit ;
   - **`MV7 adresses-sortie --ip-poste IP_POSTE`** :
     - code 0 : retenir `P` = `prefixe_conseille` (32 ou 24). **Jamais `--prefixe-poste 24` sans cette mesure** ;
     - si elle rend 32 alors que les deux premiers essais avaient plusieurs sorties dans le même /24 : le signaler à Lazar
       et à la mère avant L2 (procédure, section 0, point 5), sans attendre de réponse. `P` reste la mesure ; aux troisième
       et quatrième essais, la mesure a rendu 32, et le pilote n'a connu aucun échec de connexion ;
     - code 1 : arrêt, compte rendu, aucune préparation ;
   - **`stat -c %a src/controle_ia/lean_essai/verificateur_noyau_v6.lean` = `644`** (sinon `chmod 644` de ce seul fichier,
     sans commit) ;
   - ordinateur sur secteur, capot ouvert.
3. **L1, L2, L3** :
   - `T_LIM` = heure de L1 (`date -u`) **plus 6 heures** ; `H` = `T_LIM` **plus 40 heures** ;
   - `MV7 preparer --go GO-2026-11-10-13 …` (fichier `rattrapage-machine-d1a-<jeton12>-v1.json` au **jeton neuf**, tiré
     par `preparer`) ;
   - **L2** avec `--prefixe-poste P` ;
   - **L3** : pousser, poser la référence de suivi, puis **envoyer à la mère** : branche, commit, jeton, identifiants de la
     clé et du pare-feu, empreinte de la clé, `P`, `T_LIM`, `H`, et l'empreinte sha256 du fichier de rattrapage tel que
     poussé.
4. **Attendre le mot « armée »** de la mère, **reçu directement de la session mère `session_01XJ6Mgr4LgbMsg5zLyRZCpG`**
   (ou, en second repli, relayé par Lazar), avec l'empreinte du fichier de rattrapage. **Sans lui, aucune création.**
   - La mère fait M1 à M6, inchangés : lecture, même projet, droit d'écrire, destruction à blanc, trois tâches (T1 à `H`,
     T2 à `H + 30 min` et T3 à `H + 24 h` en session neuve), ligne « en tâche jusqu'à » dans `registres/etat.md`. Les
     identifiants des tâches et les heures viennent avec le mot « armée ».
   - **M1 bis (mère, avant le mot « armée »)** : par `git fetch` de `-v7`, le parent du commit d'apport est
     `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b` et son arbre `ab77bbac454b3c4723eab8ed9306b20031502c2d` ; le projet ne porte
     qu'une clé et qu'un pare-feu, ceux du jeton reçu, et aucun serveur. Sinon, pas de mot « armée ».
   - À sa réception, tu donnes à Lazar, dans ta conversation, l'heure `H + 1 h` de son rappel personnel (la mère la lui
     donne aussi).
   - Remarque : la garde d'heure limite borne la préparation et la création, pas la vie du serveur. Si L1 tombe le 30
     novembre, `H − 1 h` (échéance de la minuterie) déborde sur décembre (jusqu'au 2 décembre), et la ligne « en tâche
     jusqu'à » dépasse l'échéance du GO (2026-11-30) ; la mère le note.
5. **L4 à L7** : `creer-et-armer --go GO-2026-11-10-13 … --type ccx33 --lieu hel1 --deja-depense-usd 1.12`. En L7,
   l'identifiant, l'échéance, le PID de la minuterie et le commit poussé vont **à la mère**. Puis **section 3** :
   - avant le premier pilote : si l'adresse du serveur est déjà connue du poste (`ssh-keygen -F <adresse du serveur>`),
     `ssh-keygen -R <adresse du serveur>` ;
   - **pilote `avant`** : `scripts/lean_essai_d1a_v13/piloter_poste_v13.sh avant <adresse du serveur> <clé privée>
     56a005855ea17e0b0958f73ec801ae140b0a1679` (commit de Mathlib épinglé : en-tête de la procédure v12, au commit `47c7faaf` ;
     `verificateur-epingle-v6.json` du quatrième essai).
     Inchangé depuis le v10 :
     - installation par `installer_chaine_v2.sh`, avec la garde de lisibilité (code 5 si un chemin reste fermé à `bac`) ;
     - sonde v2 « ouverte » ;
     - essai R5 « bac lit Mathlib.olean » ;
     - essai R5 « le vérificateur compile sur la machine ».

     **Tout code non nul du pilote `avant` : ni coupure, ni pilote `apres`** ; section 5, compte rendu. La commande qui
     lance chaque pilote écrit son code de sortie dans un fichier au nom neuf (au quatrième essai :
     `pilote-avant-code-v1.txt`, `pilote-apres-code-v1.txt`), que la lecture combinée lit. **Ce fichier ne porte que
     l'entier**, écrit par `echo $? > <fichier>` juste après le pilote, dans la même commande (pour le pilote `apres`,
     lancé en arrière-plan, dans le même interpréteur : procédure v15, section 3) ; rien d'autre n'y est écrit ;
   - **coupure** : `MV7 acces-couper … --ip-poste IP_POSTE --prefixe-poste P`, puis `MV7 verifier-coupure`. Si elle rend
     « pending », une seconde lecture, seule et en lecture seule, avec un journal neuf, une minute plus tard. Non conforme
     encore : section 5 ;
   - **pilote `apres`** (`piloter_poste_v13.sh apres <adresse du serveur> <clé privée> <dossier de sorties hors du clone>`,
     en arrière-plan). Dans l'ordre :
     - vidage du cache du résolveur et sonde v2 « fermée » ;
     - dépôt du harnais (exécuteur v8, **épreuve v9**, vérificateur v6, artefacts avec `attendus-v8.json`) ;
     - contrôle `cmp` du vérificateur et épinglage (`verificateur-epingle-v6.json` : empreinte `3ef23bfa…`, celle du
       compagnon vérifié au mandat 1 et des essais précédents ; une autre empreinte est un écart, dit au rapport) ;
     - **premier pas `noyau`** : non conforme, le pilote s'arrête (`set -e`) et rien d'autre n'est lu : section 5, compte
       rendu, sans relance ;
     - **épreuve, 36 cas** : 21 gardes Lean, 5 isolement Lean, 4 Python, 5 limites, 1 limite Lean. Code relevé dans
       `epreuve-code-v6.txt` : 0, 1, 3 ou 124 ; le pilote continue. Un autre code (255 si la connexion tombe) est
       rapporté tel quel, sans conclusion sur l'épreuve ;
     - **`mesurer`** ;
     - sonde de fin et relevé de l'installation ;
     - la dernière ligne qu'il affiche nomme `minuterie_v6 detruire` : texte hérité ; la destruction se fait par la
       minuterie v7 (`MV7`, section 5 de la procédure), jamais d'après cet affichage ;
   - **mémoire de la machine entière** : `mesurer` lance trois passages de l'item sain en suite, puis trois en parallèle
     dans une tranche réservée de nom neuf (`bacmesure<8 hexadécimaux>.slice`). Pendant le bloc parallèle, toutes les
     0,1 s, root relève `memory.peak` de la tranche et `MemAvailable`. Le jugement suit les sept critères écrits d'avance de
     la procédure, § 8.5 (`parallele_3_compte`, `parallele_3_motifs`, `parallele_3_calcul`). **Tu ne fais rien à la
     main** : aucun passage relancé, aucune commande de plus sur la machine, aucun seuil changé, aucun motif corrigé ;
   - **tout arrêt du pilote `apres` par un code non nul, à quelque étape que ce soit** (coupure sur la machine, vidage du
     cache, sonde, dépôt, `cmp`, épinglage, pas `noyau`, `mesurer`, sonde de fin, relevé de l'installation), **ou sa mort
     sans code** (terminal fermé, connexion perdue) : section 5, **sans relance du pilote ni d'aucune de ses étapes**, et
     sans commande de plus sur la machine. Sorties versées telles quelles ; toute sortie qui n'entre dans aucune lecture
     écrite est rapportée telle quelle, sans lecture inventée (procédure, § 8, préambule) ;
   - **si le pas `noyau` échoue par la mémoire ou par le délai** (`incident_bac` d'un cas vaut « mémoire » ou « délai ») :
     - relève au rapport, pour chaque cas en échec : `incident_bac` ; le bloc `temps` (la compilation) et le bloc `noyau`
       (le vérificateur), chacun avec `resultat`, `fin`, `code`, `cpu_s`, `duree_murale_s`, `resume_systemd`,
       `memoire_pic_echantillonne_octets` et `memoire_echantillons` ; les `ecarts`. Cette sortie ne porte ni
       `incident_compilation` ni `incident_noyau` : la comparaison des deux blocs (`resultat`, `cpu_s`) dit lequel des deux
       a été arrêté ;
     - verse `premier-pas-noyau-v6.json` après `garde-poste --fichier` ;
     - puis **fin normale (section 5), sans relance**, ni du pas ni du pilote. Aux troisième et quatrième essais, ce pas a
       tenu, 18 sur 18, sans incident ;
   - **destruction sans attendre** : la lecture de la section 8 se fait sur les sorties copiées sur le poste et ne demande
     aucune commande sur la machine. La section 5 suit donc la fin du pilote `apres`, et la lecture peut venir après la
     destruction ;
   - valeurs des pièces `VERSION-LEAN`, `COMMIT-MATHLIB`, `MACHINE`, `ESSAIS-R5` (partie machine : lecture par `bac`,
     compilation du vérificateur, pas `noyau`, épreuve, mesures).
6. **Fin** : section 5 (normale) ou 4 (anormale).
   - Serveur détruit par son identifiant **dans tous les cas** ; inventaire « aucun serveur de l'essai », avec
     `ips_primaires_non_attribuees` vide.
   - Clé et pare-feu supprimés **chez le loueur**, par `MV7 acces-supprimer` (aucun fichier du poste n'est supprimé) ; si
     `acces-supprimer` rend 422 `resource_in_use`, refaire 2 à 3 minutes plus tard.
   - Minuterie arrêtée par son PID si elle vit.
   - **Message à la mère** : heure de la destruction, inventaires, accès supprimés, minuterie (section 5, point 5 : c'est
     le poste qui prévient la mère). En code 3, Lazar détruit à la main dans la console, et la mère est prévenue tout de
     suite.
   - Terminal WSL fermé seulement après l'inventaire final ; tu dis alors à Lazar qu'il peut le fermer.
7. **Lecture et rapport** sur ta branche, sous `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` (noms neufs) :
   `rapport-poste-local-d1a-v5.md` (numéro de l'essai ; nom absent de `main`, de `-v6` et de l'apport le 2026-11-22),
   scellé, sur `donnees/lean-outillage-d1a-poste-local-v7`. **La lecture suit la section 8 de la procédure v15, écrite avant
   l'essai, sans rien y changer après avoir vu une sortie.** Le rapport contient :
   - vie du serveur (création, destruction, heures, coût ; cumul sous GO-2026-11-10-13) ;
   - `P` retenu et la sortie de `adresses-sortie` (comptes seulement) ;
   - l'essai à blanc : repris (réponses de Lazar, version d'Ubuntu) ou refait (relevés) ; la lecture du mandataire ;
   - le canal des messages : direct, ou repli (lequel, quand, pourquoi) ;
   - l'apport : empreinte du correctif v3, arbre, commit d'apport et son parent ; la version de Python du poste et le
     résultat de la règle v3 sur les pièces du quatrième essai (mandat 1) ;
   - sorties des étapes ;
   - **la lecture de la section 8**, dans l'ordre du § 8.1 :
     - pilote `avant` ;
     - pas `noyau` ;
     - code de l'épreuve ;
     - `statut`, `genres` et `genres_morts` (un genre « épreuve morte » : seule la cause, lue dans la sortie de son cas
       sain) ;
     - les cas genre par genre, dont le détail des trois tentatives réseau (« non éprouvé » si un programme n'a pas été
       lancé, § 8.2) et, pour le genre « limites », `stdout_extrait` du cas 137 (§ 8.2 : quatre conditions). Le temps de
       processeur de l'unité se lit sur `temps.cpu_s` du cas (0,033 au quatrième essai) ; la borne « inférieur à 1 s »
       n'est pas appliquée par l'épreuve v9 : toi seul la lis. Si elle est dépassée alors que la pièce dit le cas
       conforme, ta lecture dit « non tenu » et la règle « conforme » : c'est un désaccord, rapporté tel quel à la
       concordance (§ 8.7, point 6), sans correction ;
     - le cas « temps de processus (5 s) » selon les trois lectures du § 8.3 ;
     - la limite Lean, lue sur la compilation seule ;
     - `controles_hote` ;
     - le bloc `memoire` (§ 8.4 : chemin de cgroupe faux ou non, pics rapportés) ;
     - `mesures-v6.json` (§ 8.5 : `parallele_3_compte`, chaque motif recopié tel quel, `parallele_3_calcul`, `MemTotal`
       de la machine) ;
     - les sondes réseau ;
   - **la lecture combinée du § 8.7**, faite après la section 5 et après les lectures précédentes : la commande exacte
     (`conformite_outillage_v3`, lancée par `env -u NOM …` comme les autres commandes du harnais), son code de sortie
     (l'entier seul, `lecture-combinee-code-<jeton12>-v1.txt`), le fichier `lecture-combinee-<jeton12>-v1.json` recopié tel
     quel (versé après `garde-poste --fichier`), et **la concordance selon l'étape écrite du § 8.7, point 6** : tes lectures
     écrites d'abord dans `lectures-poste-<jeton12>-v1.md`, leur empreinte relevée avant la règle, puis la table d'accord
     (un désaccord est rapporté tel quel, sans correction) ;
   - au § 8.6 : le verdict du poste, qui reste une lecture et jamais un verdict de porte (« noyau », « épreuve »,
     « mesures », lecture combinée), et la liste de ce qui reste non éprouvé ;
   - valeurs des pièces, incidents, écarts ;
   - **lignes proposées** pour `registres/depenses.md` et `registres/arrets.md` (sous GO-2026-11-10-13, branche
     `donnees/lean-outillage-d1a-poste-local-v7`).

   Pièces sous `pieces-poste-local-d1a-<jeton12>-v1/`, avec un manifeste d'empreintes qui passe `sha256sum -c`. Puis
   **message à la mère** : branche, commit, empreinte du rapport. L'outillage D-1a n'est déclaré conforme par personne
   d'autre que la mère, sur ces lectures.

## Réserves pour la mère (hors du mandat du poste)

- **Point de départ de `-v7` : décision de la mère, R-4808.** Le dernier commit de `-v6`,
  `86aabc842a1f98ce5c7e2cce40f9d1e3a6248175`, est relevé ci-dessus ; une branche qui en part porterait dans `V` le fichier
  de rattrapage et le journal des créations du quatrième essai : `preparer` et `creer-et-armer` refuseraient (CLC5-03,
  « seconde machine »), et rien ne peut en être supprimé. `-v7` part donc de `47c7faaf` plus l'apport, comme `-v5` et
  `-v6` partaient de `47c7faaf`.
- **L'apport passe par `main`** (correctif v3 à appliquer, identifié par son empreinte et par l'arbre attendu) : la
  consigne n'a besoin d'aucun commit encore inconnu. La mère doit verser sur `main`, et pousser, le correctif v3, son
  compagnon, cette consigne, son compagnon et le différentiel, **avant** la phrase de lancement. Autre voie possible : une branche
  `prep/lean-outillage-d1a-v12` portant le même arbre ; elle demanderait une consigne neuve.
- **Vérifications faites** : la contre-lecture de la v9 et de l'apport v1 a rendu « à corriger » (R-4813) ; la v10,
  l'apport v2 et la procédure v14 portaient ses corrections, vérifiées « conforme » par le même contre-lecteur (R-4819) ;
  la v11, l'apport v3, la procédure v15 et la règle v3 portent les corrections de Fable, vérifiées « conforme » par le même
  contre-lecteur en troisième passe (R-4824). **Reste dû** : la vérification courte de cette v12 par le même
  contre-lecteur, sur les seuls points de « Ce qui change depuis la v11 », avant usage.
- **Points relus par Claude Fable 5.2** (critères de décision ; R-3735) : relecture `relecture-fable-api.md`
  (`c3495cbd…`, 2026-11-22T09:31Z), sur la procédure v14 et la règle v2. Bilan : points 3, 4 et 8 gardés ; points 1, 2,
  5, 6 et 7 corrigés, portés mot pour mot dans la procédure v15 et la règle v3 (R-4823). Les points relus :
  - le **§ 8.2**, cas « sortie de lui-même en code 137 » : les **quatre conditions**, toutes exigées ; la borne du temps de
    processeur devient « inférieur à 1 s » (point 1) ;
  - le **§ 8.7 en entier**, règle v3 comprise (épreuve « tenue » seulement entière ; un pilote « apres » en code 0 alors
    que le pas `noyau` est non conforme, lu « non établi » ; H12 ; noms et passages du noyau ; erreur en code 3), et
    l'**étape de concordance du point 6** ;
  - les **codes 124 et 255 du pilote « avant »** : **tranchés** (point 5), lus « non établi », rien n'étant lu après lui ;
    tout autre code non nul reste « non tenu ». Remarque de la troisième passe : le pilote lance chaque étape par
    `ssh … timeout N …` ; une étape de la phase « avant » qui dépasse sa borne (installation, compilation du vérificateur)
    rend donc 124 elle-même. Ce code peut dire un défaut de l'outillage, et il est lu « non établi » au lieu de « non
    tenu » : rien ne s'ouvre vers « conforme », mais la mère le sait en lisant un 124.
- **Borne de 1 s du cas 137, non codée dans l'épreuve** (décision de la mère, R-4823 ; jugée sûre par la troisième passe,
  R-4824) : le point 1 de Fable n'est porté que dans le texte (§ 8.2). L'épreuve v9 ne lit pas le temps de processeur de
  ce cas et n'en porte aucune borne ; la règle v3 ne la lit pas non plus. Seul le poste la lit, sur `temps.cpu_s`, et un
  dépassement donne un désaccord à la concordance (§ 8.7, point 6), rapporté tel quel. Une épreuve de version neuve qui
  code la borne est un nœud de la mère, après cet essai.
- **Mot de Lazar pour la cinquième machine (B3)** : reçu et inscrit, GO-2026-11-22-42 (« go essai 5 »), échéance du
  2026-11-26 ; le champ est rempli par cette v12. La mère verse la v12 et son compagnon sur `main` avant de donner la
  phrase de lancement ; après le 2026-11-26, un mot neuf de Lazar.
- **Versions de Python** : le harnais (minuterie, garde, pilote) n'est éprouvé hors machine que sous 3.11 et 3.13 ; le
  poste avait 3.14.4 au quatrième essai, sans incident. La règle v3 est éprouvée sous 3.11, 3.12, 3.13 et 3.14.6, et jouée
  au mandat 1 sous le Python du poste ; le reste du harnais sous 3.14 ne l'est que par l'essai lui-même.
- **Premier repli par la branche** : ajouté d'avance et gardé (au quatrième essai, l'envoi direct du poste vers la mère a
  échoué cinq fois, « this computer is not a trusted device for your account yet », et Lazar a refusé de relayer). Depuis
  la v10, la mère relit `-v7` toutes les 10 minutes pendant le repli et accuse réception de chaque message poussé, avec son
  empreinte ; sans accusé sous 30 minutes, second repli.
- **Limite de la vérification** : la procédure v13 reprend la v12 ; elle n'en diffère que par l'en-tête, la section
  « Changements depuis v12 », section 0 (point 1, branche), L5 (`--deja-depense-usd 1.12`), section 3 (pilote v13, lecture
  combinée), section 7 (réserves), section 8 (titre, § 8.2 cas 137, § 8.6) et le § 8.7 neuf. La v14 reprend la v13 ; elle
  n'en diffère que par l'en-tête, la section « Changements depuis v13 », section 0 (points 1 et 2), section 3 (fichiers des
  codes), section 7 (points pour Fable, mutations), § 8.6 et § 8.7. La v15 reprend la v14 ; elle n'en diffère que par
  l'en-tête, la section « Changements depuis v14 », la section 0 (points 1 et 2), la section 7 (point 3), le § 8.2 et le
  § 8.7. Les sections 0 à 7 de la v12 n'avaient pas été relues par le contre-lecteur de la v12 (réserve de la v8,
  reprise).
- **Mutations (correction E3 de la v5, reprise)** : « 176 mutations sur 176 tuées » (mutations v10) **ne prouve pas** que le
  jeu d'artefacts détecte le retrait du rejeu par le noyau ou de la collecte des axiomes. Avant toute réutilisation du
  vérificateur au-delà de l'outillage (D-1b) : rejouer k06 et k01 (et k09, k10) de façon qu'un essai fonctionnel les tue,
  journal scellé nommant l'essai qui tue. Non bloquant pour le cinquième essai.
- **Nœud 3 de la lecture de conformité** (`reseau-python-tcp`, raison coupée à 160 caractères) : non traité par l'apport ;
  à Lazar.
- **Adresse du poste** : l'écart 2 du rapport v3 (adresse lue par la session) est repris, et avancé au mandat 1 parce que le
  commit d'apport passe par `garde-poste`. On y perd le recoupement entre l'adresse donnée par Lazar et celle que le service
  renvoie ; le pire cas est borné (serveur sans clé ni dépôt, clé jetable seule admise, une vingtaine de minutes de vie).

## Annexe

Les suggestions S1 à S8 de la contre-lecture du harnais v10, hors du mandat du poste, ne sont pas reprises ici. Elles
restent dans la v5.

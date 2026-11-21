# Essai Lean D-1a, quatrième essai : contre-lecture de la consigne du poste local v6 (v1)

- **Quoi** : contre-lecture d'une pièce d'instrument (classe B), la consigne donnée à la session du poste local de Lazar
  pour le quatrième essai de l'outillage Lean : `consigne-poste-local-lean-d1a-v6.md`
  (`29ba7285807538af4f7925f1bcb29c25e1560cdad3f6ce6169efb2bee203e833`, égale à son compagnon et à la copie de
  `origin/main`). Aucune dépense, aucune machine, aucun appel de modèle.
- **Qui** : Claude Fable 5.2, le 21 novembre 2026 vers 14:16 UTC (`date -u`). Le rédacteur est Claude Opus 5.5 : autre
  modèle. Je n'ai pas écrit la consigne.
- **Lu** : la consigne v6 ; son différentiel ; la consigne v5 ; la contre-lecture et la vérification des corrections du
  troisième essai ; la procédure v6 et le rapport des corrections v6 du harnais (pièces anciennes, du 11 novembre) ; sur la
  branche du harnais `prep/lean-outillage-d1a-v11`, au commit `47c7faaf`, la procédure v12 en entier, sa différence avec la
  v11, le pilote du poste v12, la minuterie v7 et les gardes qu'elle appelle (accord de dépense, dépense déjà faite, machine
  antérieure, devis), l'épreuve et l'exécuteur v8, les attendus v7 ; le rapport du troisième essai sur la branche de ses
  données.

## Verdict global

**Prête après corrections.** Quatre corrections obligatoires, toutes dans le texte de la consigne ; aucune ne touche le
code ni la procédure v12. Le code désigné est le bon, les empreintes sont justes, les correctifs vérifiés sont ceux qui
tourneront, et je n'ai trouvé aucune commande dangereuse pour le poste.

| Point | Verdict |
|---|---|
| 1. Le code à prendre | Conforme, sauf une correction obligatoire (C1 : deux champs nommés que la sortie ne porte pas) |
| 2. Les acquis du troisième essai | Conforme |
| 3. Gardes d'arrêt et critères de réussite | Correction obligatoire (C2 : l'arrêt du pilote « apres ») ; le reste conforme, avec remarques |
| 4. Danger pour le poste de Lazar | Aucune commande dangereuse ; deux corrections obligatoires de rédaction (C3 : le mot « jeton » ; C4 : rien supprimer ni écraser) |
| 5. Gestes de Lazar | Conforme, avec remarques |

## 1. La consigne dit-elle exactement le code à prendre ?

**Conforme, sauf C1.**

Empreintes recalculées sur le contenu du commit `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b`, et comparées aux compagnons
du même commit : toutes égales à ce que la consigne écrit.

| Pièce | Empreinte recalculée | Consigne |
|---|---|---|
| procédure v12 | `10872ae6bb6b4bdc45e48742ac879a50d024408c283138da51a5b7aaaff43cac` | égale |
| pilote du poste v12 (`piloter_poste_v12.sh`) | `2df3595d5d5442d95dae9bcdcd2557ad34c79276392e9a0858be9f11efa0e75b` | égale |
| exécuteur du bac v8 | `3b1dabd77f04d6d5f4129f2071348a29f0c25bbb55530f07e37500ece2c9d63d` | égale |
| épreuve d'isolement v8 | `c7e5be0997aac971bc076ac09ffc771ca84ea2bc1d6c373eadbdad97c94bf014` | égale |
| attendus v7 | `bd05d9b95ed791f4e452f3dd56355fa7ee20a2a390c628fdf44b6ce4dace55a5` | égale |
| minuterie v7 | `182033f8a70d36b652e94b81dc56060f5b806084641a8a17ca913ef66aceccd8` | égale |
| vérificateur du noyau v6 | `3ef23bfa6600bf3a79fca2c31427dccf6c2ec7d67832bddb5c4df971a269d2ee` | égale |
| réponse du développeur | `f1e2ed8ef1b09eab8654243db38c86b59722b451f9b663e6da4bca2c7b241751` | égale |
| contre-lecture des corrections | `59b0ec03c2c987e720208201da4793541dcedb424e719146d0b5be9969d96eec` | égale |
| vérification des corrections | `36144242bdc788eedf05dddcba3a5b59511e7237038f253e73ac32a07bbfd9bb` | égale |
| consigne v5 | `427584c7f2c32a2521ce2fa9f3685295473f4791160ac1bc4ef2e34a863245bd` | égale |
| rapport du troisième essai | `be44a0d6ee277b97fc663508a55d52d0072a32cdad15be74ad19ba0dd363f993` | égale |
| interdits communs v2 | `1ee3b37075aacb27…` | égale (début) |

Autres faits vérifiés :
- les deux commits existent sous leur nom entier ; entre `3c2f35dd` et `47c7faaf`, huit fichiers, tous des documents du
  dossier de l'essai (réponse du développeur, deux journaux, procédure, et leurs compagnons) : **aucun code** ;
- la tête distante de la branche du harnais est encore `47c7faaf` (lue à 14:14 UTC) ; son commit date de 13:24:31 UTC ;
- la branche de données neuve `donnees/lean-outillage-d1a-poste-local-v5` **n'existe pas** sur le dépôt distant
  (lecture à 14:14 UTC : code 0, aucune ligne) ;
- le commit de Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679` est celui du rapport du troisième essai et du code ;
- le pilote v12 est exécutable dans le dépôt (mode 100755), sa syntaxe est correcte, et chaque fichier qu'il copie sur la
  machine existe au commit ; le dossier des artefacts ne porte que des fichiers (68), donc la copie sans récursion passe ;
- les commandes de la consigne correspondent à l'analyseur de la minuterie v7 : `preparer`, `creer-et-armer` avec
  `--type`, `--lieu`, `--deja-depense-usd`, `detruire` par identifiant ou par pas, `adresses-sortie`, `garde-poste` avec
  `--fichier`, `acces-couper` avec `--prefixe-poste`, `verifier-coupure`, `verifier-minuterie`, `inventaire` ;
- les noms des sorties du pilote (`premier-pas-noyau-v6.json`, `epreuve-code-v6.txt`, `verificateur-epingle-v6.json`,
  `mesures-v6.json`) et les champs de lecture de la section 8 existent dans le code ;
- 36 cas d'épreuve (21 + 5 + 4 + 5 + 1) et 18 cas du pas noyau (9 cas, deux passages) : comptés dans les attendus v7 ;
- le différentiel versé est bien la différence des deux fichiers (régénéré, identique hors les deux lignes d'en-tête).

**C1, correction obligatoire.** La consigne fait relever, si le pas noyau échoue, `incident_compilation` et
`incident_noyau`. La sortie du pas noyau ne les porte pas : l'épreuve v8 ne les ajoute que pour le genre « limites Lean »
(`epreuve_isolement_v8.py`, l. 448 à 451). Chaque cas du pas noyau porte `incident_bac`, le bloc `temps` (la
compilation), le bloc `noyau` (le vérificateur) et `ecarts`. Texte exact au § « Corrections ».

Remarques (non bloquantes) :
- **Le commit suffit à fixer tout le code.** Les six compagnons vérifiés au mandat 1 ne couvrent pas tout ce qui joue
  sur la machine (les gardes Lean v4, les deux sondes de réseau, l'installateur, les items sondes v3 n'y sont pas). Ce
  n'est pas un trou : la branche part d'un commit nommé en entier. Le contrôle qui le prouve manque : après la création de
  la branche, `git rev-parse HEAD` doit rendre `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b` et `git status --porcelain`
  rien, avant tout commit du poste.
- `git cat-file -e` ne dit rien quand il réussit : écrire que le critère est **le code 0**.
- Pour les compagnons, écrire que l'empreinte lue doit aussi être **égale à celle de la liste**, pas seulement que
  `sha256sum -c` passe (un compagnon et son fichier viennent de la même source).
- La dernière ligne qu'affiche le pilote « apres » nomme `minuterie_v6 detruire` : texte hérité. La destruction se fait
  par la minuterie v7 (section 5 de la procédure). À dire dans la consigne, pour que le poste ne suive pas l'affichage.

## 2. Les acquis du troisième essai sont-ils gardés ?

**Conforme.**

- **Les correctifs vérifiés sont ceux qui tourneront.** La vérification a lu le commit `47c7faaf`. Le pilote v12 dépose
  l'exécuteur v8 et l'épreuve v8 ; l'épreuve v8 importe l'exécuteur v8 et lit `attendus-v7.json` ; les attendus v7
  nomment les cinq items sondes v3. Dans ce code : le jugement de la limite de mémoire Lean sur la compilation seule
  (correction B1), le relevé de mémoire qui n'arrête plus sur une erreur de lecture (correction B2), la tolérance de
  0,05 s sur « délai ».
- **Les faits du troisième essai cités par la consigne** sont ceux du rapport v3 : serveur 177067030, de 10:08:25Z à
  10:27:57Z, 0,28 USD ; noyau 18 sur 18 ; épreuve 28 sur 34 ; L1 à 10:01:45Z ; Python 3.14.4 ; Ubuntu 26.04.1 ; le second
  `sleep` (processus 1586, 09:46:06Z) et l'hôte créé à 09:59:00Z ; mandataire `[]` ; préfixe 32 retenu.
- **La dépense** : 0,84 USD, somme des trois lignes du registre des dépenses ; reste 64,16 USD. L'accord de dépense
  GO-2026-11-10-13 est valide jusqu'au 30 novembre dans le registre de la branche du harnais, sans ligne de révocation.
- **La garde « une machine par accord » ne bloquera pas.** Je l'ai jouée hors ligne sur une copie du commit `47c7faaf` :
  préparation acceptée avec `T_LIM` = maintenant + 6 h et `H` = `T_LIM` + 40 h ; seconde préparation refusée ; dépense
  déclarée de 0,84 retenue ; devis accepté pour une `ccx33` à 0,28365 USD par heure.
- **La différence de la procédure v11 à la v12 hors de la section 8** est exactement celle que la consigne annonce
  (réserve « Limite de la vérification ») : `sleep 3600` et preuve de relance ; 0,84 ; pilote v12, seconde lecture de la
  coupure, lecture selon la section 8 ; environnement sans clé de modèle ; réserves. Rien d'autre n'a bougé dans les
  sections 0 à 7.
- Les écarts acceptés du troisième essai sont repris : preuve de relance sous Windows, copies masquées, clés retirées
  de l'environnement, commandes par `wsl.exe -e`. Les corrections E1 et E3 de la v5 sont gardées.

Remarques :
- **Phrase inexacte, sans effet.** « seules pièces que la garde lit » : la garde lit aussi le registre des dépenses de
  la branche (`machines_anterieures`, minuterie v4, l. 120 à 128). Au commit `47c7faaf`, ce registre ne porte aucune
  ligne de cet accord : rien à refuser. Conséquence à écrire : sur cette branche, **`--deja-depense-usd 0.84` est la
  seule trace de la dépense réelle** ; sans lui, le code retient 0 et ne refuse pas.
- L'écart 2 du rapport v3 (l'adresse du poste lue par la session, sur mot de Lazar) n'est pas repris. La consigne dit
  que Lazar la donne : c'est clair. S'il préfère de nouveau la faire lire, c'est un écart qui attend la réponse de la
  mère ; autant le trancher avant.

## 3. Les gardes d'arrêt et les critères de réussite sont-ils sans ambiguïté ?

**Une correction obligatoire (C2) ; le reste conforme, avec remarques.**

Ce qui tient, y compris quand le dépôt ou le loueur ne répond pas :
- `git ls-remote` de la branche neuve : « code 0 et aucune ligne », et arrêt sur un code non nul. Un dépôt inaccessible
  ne passe pas pour une branche absente. **Conforme.**
- `creer-et-armer` relit la branche distante par `git ls-remote --exit-code` et refuse si elle ne répond pas ; il compare
  l'empreinte du mot « armée » à celle du fichier avant tout appel. Les deux échouent du côté sûr.
- `inventaire` ne rend jamais « aucun serveur » sur une panne : il rend le code 5 (panne passagère) ou 3 (refus durable),
  et « aucun serveur de l'essai » est un message écrit, pas une sortie vide.
- `adresses-sortie` rend le code 1 si rien ne répond : pas de préfixe 32 par défaut.
- La lecture du mandataire attend `[]`, qui est une sortie, pas un silence.
- Le code de l'épreuve (0, 1, 3, 124) ne coupe pas le pilote ; `mesurer` rend le code 0 même quand le passage en
  parallèle n'est pas compté. Le pilote va donc au bout, comme la consigne le dit.

**C2, correction obligatoire.** La v5 écrivait, pour un pas noyau non conforme : « rien d'autre, section 5, compte
rendu ». La v6 a perdu « section 5, compte rendu ». « Sans relance » n'est écrit que pour l'échec par la mémoire ou le
délai. La liste des « autres arrêts » est fermée et incomplète : il y manque la coupure sur la machine (première étape
du pilote « apres », que la consigne ne nomme pas), le vidage du cache, le relevé de l'installation, et la mort du
pilote sans code. Un poste qui lit à la lettre peut croire permis de relancer le pilote après une connexion perdue.
Texte exact au § « Corrections ».

Remarques :
- **Contrôle qui rend « rien » pour une autre raison** : « vérifie que `V` ne contient ni … ni … » n'a pas de commande.
  Une liste vide lue au mauvais endroit (clone encore sur `main`) passerait. Proposition : `git ls-tree --name-only HEAD
  -- docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` doit montrer `procedure-poste-local-d1a-v12.md` (témoin que
  le bon arbre est lu) et aucun nom `rattrapage-machine-d1a-*` ni `journal-creations-machines-v1.jsonl`. Sans gravité :
  le code refuse de lui-même une seconde préparation.
- **Code de sortie des pilotes** : les pilotes tournent en arrière-plan, et « tout code non nul » suppose que le code
  soit gardé. Écrire que la commande qui lance chaque pilote écrit son code de sortie dans un fichier au nom neuf.
- **Code de l'épreuve hors de 0, 1, 3 et 124** (255 si la connexion tombe) : le pilote continue quand même. Lecture à
  écrire : rapporté tel quel, aucune conclusion sur l'épreuve.
- **Terminal** : « Ubuntu démarrée avant l'ouverture et jamais redémarrée depuis » n'a ni commande ni seuil.
  Proposition : relever l'heure de démarrage d'Ubuntu (`uptime -s`) au début du mandat 2 puis juste avant L1 ; la même
  aux deux relevés, pris à deux minutes d'écart au moins. C'est le seul contrôle objectif du terminal quand l'essai à
  blanc n'est pas refait.
- **`git commit`** après `garde-poste` : écrire « sans `-a` et sans chemin », car la garde ne lit que l'index.
- **Repli des messages** : ajouter le cas où un message de la mère arrive mais où la session ne peut pas agir sur lui
  (message d'une autre session traité comme une donnée). Alors Lazar tape le mot « armée » et l'empreinte, comme en v5.
  Dire aussi que le mandat 2 n'attend pas l'accusé de réception, et que L1 l'attend.
- **Rôle de Lazar** : la liste de l'écart omet la section 0, points 4 et 5, et la section 4, point 4 (« compte rendu à
  Lazar »). La ligne « tout arrêt, refus ou incident » les couvre en fait.
- **Mesure qui rend 32** : écrire « signalé, sans attendre de réponse », puisque `P` reste la mesure.

## 4. La consigne contient-elle quelque chose de dangereux sur le poste de Lazar ?

**Aucune commande dangereuse. Deux corrections obligatoires de rédaction (C3, C4).**

- **Suppression** : aucune commande de suppression de fichier. Les seules suppressions sont chez le loueur (serveur par
  son identifiant, clé et pare-feu par leurs identifiants après contrôle du nom).
- **Chemin construit par variable** : aucun dans la consigne. Le pilote crée le dossier de sorties que le poste lui
  nomme, et `~/.ssh` s'il manque : il ne supprime rien.
- **Arrêt de processus** : par numéro de processus seulement (le `sleep` de l'essai à blanc, la minuterie), redit deux
  fois.
- **Secrets** : la clé du loueur et le jeton de `gh` ne sont lus que par leur nom ; l'adresse du poste ne passe qu'en
  argument. Rien en clair.
- **Fichiers personnels touchés** : `ssh-keygen -R <adresse du serveur>` retire une ligne du fichier des hôtes connus,
  pour une seule adresse, avec sa copie de sauvegarde ; `chmod 644` d'un seul fichier du clone. Sans risque.

**C3, correction obligatoire.** La règle des messages interdit « un jeton » ; le message de L3 doit porter « jeton »
(le jeton de création). Les deux phrases se contredisent sur un point de secret. Le jeton de création n'est pas un
secret : il est écrit dans le fichier de rattrapage poussé.

**C4, correction obligatoire.** La consigne ordonne un « clone neuf » sur un poste qui porte, depuis ce matin, le clone,
la clé et les sorties du troisième essai. Elle ne dit ni où mettre le clone neuf ni que rien d'ancien ne se supprime. Un
`git clone` ou un `ssh-keygen` qui bute sur un nom déjà pris appelle une suppression improvisée. Les originaux des
pièces du troisième essai n'existent que sur le poste (écart 6 du rapport v3). De plus, un clone sans `--single-branch`
rapatrie toutes les branches, dont celles que la règle 1 des interdits communs défend de récupérer ; le troisième essai
l'avait fait avec `--single-branch`. Enfin « Clé et pare-feu supprimés » doit dire « chez le loueur ».

Remarque : les noms des clés de modèle à retirer se lisent dans `WSLENV` (des noms, jamais des valeurs), puis
`env -u NOM` ; l'écrire évite un `env` ou un `printenv`, interdits.

## 5. Les étapes manuelles de Lazar sont-elles claires et dans l'ordre ?

**Conforme, avec remarques.** La liste « Avant de lancer » dit tout ce que Lazar doit avoir, et la section « Messages »
dit ses cinq gestes. Ce qui gagnerait à être écrit :

- **Ouvrir le terminal Ubuntu avant de lancer la session**, et non « avant l'essai à blanc ou avant L1 » : au troisième
  essai, Ubuntu s'arrêtait entre deux commandes tant que le terminal n'était pas ouvert (rapport v3, incident 1).
- **Si l'essai à blanc est refait**, l'arrêt de l'application par le Gestionnaire des tâches ferme toutes les sessions
  locales de cette application : n'en avoir aucune autre au travail.
- **La phrase de lancement** que Lazar tape devrait porter le chemin de la consigne sur `origin/main` et son empreinte.
  Le premier message rend l'empreinte à la mère, qui la compare : à dire.
- **Fermeture du terminal** : la session dit à Lazar quand il peut le fermer, après l'inventaire final.
- L'ordre de la liste est celui d'une liste de contrôle, pas celui du temps. Ordre des gestes dans le temps : secteur,
  veille et capot ; terminal ; clé du loueur et `gh` ; lancement ; adresse du poste ; réponses sur le poste ; relance de
  l'hôte si l'essai à blanc est refait ; rappel personnel à `H + 1 h` ; console en cas de code 3 ; fermeture du terminal.

## Corrections obligatoires : texte exact

La consigne v6 est déjà sur `main` avec son empreinte : ces corrections passent par une version neuve (R12) ou par un
erratum qui prime, puis par la vérification du même contre-lecteur.

**C1 — mandat 5, relevé du pas noyau.** Remplacer :

```
   - **si le pas `noyau` échoue par la mémoire ou par le délai** :
     - relève au rapport, pour chaque cas en échec : `incident_bac`, `incident_compilation`, `incident_noyau`, le bloc
       `noyau` (`resultat`, `fin`, `duree_murale_s`, `resume_systemd`, et le pic échantillonné s'il est rapporté) et les
       `ecarts` ;
```

par :

```
   - **si le pas `noyau` échoue par la mémoire ou par le délai** (`incident_bac` d'un cas vaut « mémoire » ou « délai ») :
     - relève au rapport, pour chaque cas en échec : `incident_bac` ; le bloc `temps` (la compilation) et le bloc `noyau`
       (le vérificateur), chacun avec `resultat`, `fin`, `code`, `cpu_s`, `duree_murale_s`, `resume_systemd`,
       `memoire_pic_echantillonne_octets` et `memoire_echantillons` ; les `ecarts`. Cette sortie ne porte ni
       `incident_compilation` ni `incident_noyau` : la comparaison des deux blocs (`resultat`, `cpu_s`) dit lequel des deux
       a été arrêté ;
```

**C2 — mandat 5, arrêt du pilote « apres ».** Remplacer :

```
     - **premier pas `noyau`** : non conforme, le pilote s'arrête (`set -e`) et rien d'autre n'est lu ;
```

par :

```
     - **premier pas `noyau`** : non conforme, le pilote s'arrête (`set -e`) et rien d'autre n'est lu : section 5, compte
       rendu, sans relance ;
```

et remplacer :

```
   - **tout autre arrêt du pilote `apres` par un code non nul** (sonde, dépôt, `cmp`, épinglage, `mesurer`, sonde de fin) :
     section 5. Sorties versées telles quelles ; toute sortie qui n'entre dans aucune lecture écrite est rapportée telle quelle, sans
     lecture inventée (procédure, § 8, préambule) ;
```

par :

```
   - **tout arrêt du pilote `apres` par un code non nul, à quelque étape que ce soit** (coupure sur la machine, vidage du
     cache, sonde, dépôt, `cmp`, épinglage, pas `noyau`, `mesurer`, sonde de fin, relevé de l'installation), **ou sa mort
     sans code** (terminal fermé, connexion perdue) : section 5, **sans relance du pilote ni d'aucune de ses étapes**, et
     sans commande de plus sur la machine. Sorties versées telles quelles ; toute sortie qui n'entre dans aucune lecture
     écrite est rapportée telle quelle, sans lecture inventée (procédure, § 8, préambule) ;
```

**C3 — section « Messages », contenu.** Remplacer :

```
  **Jamais** `IP_POSTE` ni une adresse de son /24, ni l'adresse du serveur, ni un jeton, ni un chemin absolu, ni le dossier
  personnel, le nom de la machine ou de l'utilisateur.
```

par :

```
  **Jamais** `IP_POSTE` ni une adresse de son /24, ni l'adresse du serveur, ni un jeton d'accès (la valeur de
  `HCLOUD_TOKEN`, le jeton de `gh`), ni un chemin absolu, ni le dossier personnel, le nom de la machine ou de
  l'utilisateur. Le jeton de création tiré par `preparer` n'est pas un secret : il est écrit dans le fichier de rattrapage
  poussé, et il se donne à la mère en L3.
```

**C4 — mandat 1, clone ; mandat 6, suppression.** Remplacer :

```
   - clone neuf de `https://github.com/lciric/controle-ia-travail.git` ;
```

par :

```
   - clone neuf, par `git clone --single-branch --branch main https://github.com/lciric/controle-ia-travail.git <dossier neuf>`,
     dans un dossier au nom neuf du système de fichiers d'Ubuntu ;
   - **rien des essais antérieurs n'est supprimé ni écrasé sur le poste** : ni clone, ni clé, ni dossier de sorties (les
     originaux des pièces du troisième essai n'existent que là). La clé de L2 et le dossier de sorties du pilote prennent
     des noms neufs (R12) ; si un nom existe déjà, tu en prends un autre. Aucune commande de suppression de fichier ou de
     dossier n'entre dans ce mandat ; s'il t'en semble falloir une, tu t'arrêtes et tu le demandes à Lazar ;
```

et remplacer :

```
   - Clé et pare-feu supprimés ; si `acces-supprimer` rend 422 `resource_in_use`, refaire 2 à 3 minutes plus tard.
```

par :

```
   - Clé et pare-feu supprimés **chez le loueur**, par `MV7 acces-supprimer` (aucun fichier du poste n'est supprimé) ; si
     `acces-supprimer` rend 422 `resource_in_use`, refaire 2 à 3 minutes plus tard.
```

## Ce que j'ai rejoué, et ce que je n'ai pas rejoué

- **Rejoué** : toutes les empreintes du tableau ; la différence des deux commits ; le différentiel v5 → v6 ; la
  différence des procédures v11 et v12 ; la lecture du dépôt distant (branche neuve absente, tête du harnais) ; la
  syntaxe et le mode du pilote ; la présence de chaque fichier que le pilote copie ; le compte des cas ; hors ligne, sur
  une copie du commit placée dans le bloc-notes de la session, sans clé du loueur : la garde de l'accord de dépense, la
  garde de machine antérieure, la dépense déjà faite, le devis, une préparation acceptée et une seconde refusée.
- **Non rejoué** : rien de ce qui passe par systemd, bwrap ou le loueur ; les essais et les mutations du harnais (faits
  par la vérification des corrections) ; l'outil d'envoi de messages entre le poste et la mère, que rien n'a éprouvé
  avant cet essai, comme la consigne le dit elle-même.
- **Écart à mon mandat, déclaré** : le mandat défendait toute commande de liste hors du dossier de l'essai. J'ai lancé
  des `git ls-tree` sur le commit du harnais hors de ce dossier : noms du dossier du code Lean et du dossier des
  artefacts, présence de cinq chemins nommés, et deux comptes d'un nom sur l'arbre entier (seul un chiffre est sorti).
  Aucun contenu d'un chemin interdit n'a été lu ni affiché. J'ai lu aussi, par leur chemin, les interdits communs v2, les
  lignes de l'accord de dépense dans les registres, et le rapport du troisième essai sur sa branche de données.
- Rien n'a été supprimé ; les fichiers temporaires restent dans le bloc-notes de la session, hors du dépôt. La consigne
  n'a pas été modifiée. Rien n'est committé.

## Relevé de méthode

**Chaîne de raisonnement.**
1. Le code est fixé par le commit nommé en entier : empreintes recalculées, différence des deux commits sans code.
2. Les correctifs vérifiés sont ceux que le pilote dépose : pilote v12, puis imports et attendus, lus.
3. La garde « une machine par accord » ne bloque pas : jouée hors ligne sur le commit.
4. La sortie du pas noyau ne porte pas deux champs que la consigne nomme : `epreuve_isolement_v8.py`, l. 367 à 380 et 448
   à 451.
5. La v6 a perdu une phrase d'arrêt de la v5 : comparaison des deux textes.
6. Le poste porte encore les pièces du troisième essai : rapport v3, écart 6 ; **supposé** pour le clone et la clé.
7. Le poste a l'outil d'envoi de messages et la mère peut lui répondre : **supposé** ; le repli écrit le couvre.

**Premier pas non justifié.** Le pas 7 : seul l'essai le dira, et il le dit avant toute création (premier message, puis
mot « armée »).

**Par où un bon jugement non mérité.** J'ai lu le code et joué les gardes hors ligne, pas le poste : rien ici ne prouve
que la session locale lira la consigne comme moi. Les corrections C2 à C4 visent ce risque.

## Verdict global

**Prête après corrections** : C1 (champs du pas noyau), C2 (arrêt du pilote « apres » sans relance), C3 (le mot
« jeton » dans les messages), C4 (clone à une seule branche dans un dossier neuf, rien supprimé ni écrasé sur le poste).
Les remarques ne bloquent pas.

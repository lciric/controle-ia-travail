# Contre-lecture de la procédure pas à pas du pilote MR-2 sur la machine jetable (code v74, texte scellé candidat 6) — v3

Contre-lecteur : modèle J, neuf, autre modèle que l'auteur (modèle A)

- Procédure relue : `procedure-pilote-v74-compte-organisme/procedure-pilote-mr2-v74-machine-v3.md`, empreinte
  `efc29199512bdc03386733f6372d414fdea511263fdaafb97b748774fd5fe38d` (égale à son compagnon).
- Début : 2026-11-14T23:15:59Z. Fin : 2026-11-14T23:19:53Z (relevées par `date -u`). Rapport non scellé.
- Empreintes vérifiées : texte scellé `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` ; paquet
  `e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1` ; relevé `f56d9c0e14ca1f36ac3d9d226c1e5f763731fcc697ad780ea35c483ccf85d529`. Toutes égales aux valeurs attendues.

## Verdict : jouable après corrections

Un constat bloquant (le clonage du paquet, ligne 80, échoue : le paquet n'est pas autonome), cinq majeurs, huit mineurs. Le bloquant a un contournement
éprouvé (point c). Le texte scellé est suivi dans l'ordre ; les commandes du lanceur sont exactes ; le bloc gelé est égal.

**Limite de cette contre-lecture** : une commande de lecture groupée (deux fichiers hors de ma liste : le module d'audit du rapatriement et le
fichier de configuration v12) a été refusée par le classifieur ; je ne l'ai ni contournée ni reformulée. Non vérifiés par moi : l'intérieur de
`rapatrier` (liste blanche exacte des fichiers), les ports et prix de la configuration, la syntaxe de `vastai destroy instance … -y`.
Motif du refus, mot pour mot : « Permission for this action was denied by the Claude Code auto mode classifier. Reason: [Unauthorized Access]. »

## a. Ordre et préalables du texte scellé

- Secret engagé et poussé avant la phrase : conforme (l. 102-110 : secret, empreinte inscrite et poussée « par la mère », « Ensuite seulement » la phrase). Conforme au texte (« Ordre »).
- Mondes puis C-16 et C-17 : conforme (étapes 5 et 6). Écart : l'étape 5 dit que les empreintes « vont au registre » (l. 123) mais ne pose pas
  l'inscription comme barrière avant l'étape 6 ; le texte écrit « empreintes au registre → C-16 » (constat m2).
- Essai à blanc avec les vraies pièces servies et rapatriement essayé : conforme (l. 141-149). Ni `mesurer` ni `lire` sur `blanc/` : conforme.
- Relais avec leur part comme plafond : le code le fait seul (`lancer_relais`, `plafond = part_usd`) ; la procédure n'en dit rien (mineur m6).
- Dossier de la sonde à côté du relevé : conforme (l. 35, 51, 155).
- Un seul lancement réel (registre des lancements hors dépôt, l. 183) ; une seule mesure (l. 185) ; issue lue par un sous-agent neuf (l. 194-197) : conformes.
- Manque (mineur m1) : le texte, préalable (5), dit « à faire : vérification courte du différentiel candidat 3 → candidat 6, rapport écrit et versé » ;
  la procédure ne le vérifie pas avant la location. Aucun préalable ajouté qui change la lecture.
- Ordre non dit (mineur m7) : la machine est louée à l'étape 2, avant que Lazar donne sa phrase ; aucune borne de durée d'attente, alors que la part machine est de 3 USD pour environ 2 h.

## b. Commandes du lanceur et gardes

- Toutes les sous-commandes et options citées existent dans `principal` : `secret CHEMIN` ; `generer --secret --phrase-fichier --texte --texte-sha256 --sortie` ;
  `preparer --mondes --mondes-sha256` ; `jouer --mode --mondes --mondes-sha256 --sortie --go-pi1 --go-pi2 --registre-go --texte --texte-sha256 --mondes-shas
  --registre-lancements --releve-sonde` ; `mesurer --sortie --mondes --mondes-sha256` ; `lire --sortie --ecrire` ; `rapatrier --source --destination --mondes
  --mondes-sha256` ; `bloc --releve-sonde`. Noms exacts.
- Sorties attendues égales à celles de la répétition (empreintes du gabarit `e77d3041…` et du programme `676d5f37…` retrouvées ; `a_blanc`, 16 complets, `arret: null` ; `aucun_monde: true`).
  Les empreintes `.sha256` des six sorties de la répétition sont vérifiées (« OK »).
- Gardes : `exiger_hors_depot` (secret, mondes, engagement, registre des lancements) : `/root/pilote/prive` et `/root/pilote/lancements.jsonl` sont hors de l'arbre
  `/root/pilote/arbre` et sous aucun `.git` : conforme. Liste blanche de `ecrire_prive` = dossier du secret : `MONDES.json` est bien dans `prive/` avec le secret : conforme.
  Dossier de sortie absent exigé (`jouer`, l. « dossier de sortie existant ») : `blanc` et `reel` sont neufs : conforme. Le jeu `jouer`/`mesurer`/`lire` n'écrit rien de privé hors de `prive/`.
- Clés : noms `RR_ANTHROPIC_API_KEY_RIGAUD` (fable52, opus55), `GEMINI_API_KEY` (argon), `OPENAI_API_KEY` (astra), relevés au relevé de la sonde (`/identite/*/variable_cle`) : égaux à la ligne 161.
- Écarts : `E` (l. 27) n'est utilisé nulle part ; le chemin de chaque pièce envoyée n'est pas écrit (m4). Les « contrôles juste avant » (l. 153-155) n'ont pas de commande :
  la plupart sont faits par `jouer` (refus code 2 avant tout appel), mais « dossier `reel` absent », « registre absent », « ports libres » demandent un `test ! -e` explicite (m4).

## c. Rejeu local, sans clé, sans réseau (dossier /tmp/claude-0/contre-lecture-procedure/)

- Empreintes : paquet, texte, relevé égaux. `git bundle verify` (dans un dépôt vide) dit « okay » et « The bundle records a complete history ».
- **`git clone` du paquet : ÉCHEC** (deux essais) : « error: Could not read 0e3588ba843009a412bd6c9dc86807a11b7ed490 / fatal: Failed to traverse parents of commit
  7fadf9656c0b354f7629f0f28433279dcda43652 / fatal: remote did not send all necessary objects ». Le commit 7fadf965 (signé par Lazar) a un parent absent du paquet ;
  `git cat-file -t 0e3588ba…` échoue après dépaquetage. Le paquet n'est donc **pas** « l'histoire entière, aucun prérequis » (l. 49), et la vérification de la ligne 55 le laisse croire.
- Contournement éprouvé : `git init` ; `git bundle unbundle PAQUET` ; `git checkout -q 605e0f60f3eed0948948e6a4eb15cb73de1d03de` : `git rev-parse HEAD` = tête attendue ; `git status --porcelain --ignored` vide.
  `git log` et `git shortlog` sur la tête échouent encore (parent manquant), ce que le lanceur n'emploie pas (il ne lit que `git rev-parse HEAD`).
- `bloc --releve-sonde` lancé depuis ce dépôt (`env -i PATH=/usr/bin:/bin HOME=/root python3 -I -B demonstrations/pilote_mr2_v74.py`, Python 3.13.18, numpy 2.5.3) : code 0, 5345 octets.
  Le petit programme de la section 3, copié tel quel, rend **« bloc égal »**. L'arbre reste propre après l'exécution.
- Non lancés : `secret`, `generer`, `jouer`.

## d. Arrêts de la liste d'arrêt

Dits à la bonne étape, sans repli silencieux : empreinte différente (3, 5, 6) ; C-16 et C-17 (6) ; monde non conforme et secret existant (4, 5) ; réponse brute ou témoin absent, coût au-dessus du pire cas,
réflexion apparue, part atteinte (code 3, l. 179-183) ; aucune issue lue après arrêt ; relevé de la sonde invalide (code 2) ; second lancement refusé ; erreur de la mesure (l. 197).
Manques : panne d'un relais (tolérée, code 0 avec « echec », aucune reprise ni bascule, minimum 12 sur 16, sinon P-0) n'est pas dite : un exécutant verra « echec » et pourrait relancer (m5) ;
après erreur de `mesurer` (code 3 par `ArretPilote`), rien n'interdit de relancer la commande, que le code accepterait si aucune sortie n'a été écrite (m5) ; aucune étape ne dit « sur tout arrêt, rapatrier puis détruire » (M4).

## e. Sécurité

- Clés : par l'entrée standard, `printf` interne du shell (jamais en argument), fichier en `umask 077`, `env -i`, effacement par `shred -u`. Conforme. Écarts : valeur absente non détectée (M3) ;
  `shred` n'est pas atteint si la connexion tombe (voir M1).
- Secret, mondes, textes servis : restent dans `prive/` et `reel/prive/` ; la liste de rapatriement les « laisse » (répétition : `laisses` = `prive/…`) : conforme. La phrase : « envoyée par l'entrée standard » mais écrite « tapée » (l. 108) ;
  dans une session d'agent, il n'y a pas de terminal : la phrase passera dans une commande (donc dans le journal de la session). Le mécanisme réel n'est pas dit (m3).
- Destruction : par identifiant, `-y`, preuve par l'absence dans `vastai show instances`, sans nommer une instance intouchable (l. 217-223) : conforme. Le premier inventaire (l. 61) ne nomme pas la commande (m4).

## f. Constats classés

### Bloquant

- **B1 — Le clonage du paquet échoue** (l. 49, 55, 80). Fondement : sortie de `git clone` et `git cat-file` ci-dessus. Correction : remplacer l. 80 par
  `git init -q arbre && cd arbre && git bundle unbundle ../arbre-organisme-complet-605e0f6.bundle && git checkout -q 605e0f60f3eed0948948e6a4eb15cb73de1d03de` (éprouvé) ; corriger l. 49 et 55 (histoire tronquée au parent
  `0e3588ba…`, « complete history » trompeur) ; remplacer le contrôle « le paquet cloné donne la tête » par « dépaquetage et dépôt propre » ; ou refaire le paquet depuis un dépôt complet (nouveau nom, R12).

### Majeur

- **M1 — Lancement réel sans persistance** (l. 168-176). `jouer` tourne au premier plan sous ssh ; une coupure tue le processus, laisse `cles.env` sur disque, et le registre des lancements est déjà écrit (le code l'écrit avant le premier appel) : plus de second lancement. Correction : lancer sous `setsid`/`nohup` (ou `tmux`) avec le code de sortie écrit dans un fichier, suivre par relecture, et `shred` dans la même enveloppe.
- **M2 — `lecture.json` ne sort pas** (l. 190, 206-208). Le fichier est écrit dans `reel/` ; la liste de rapatriement de la répétition n'en contient aucun (0 occurrence de « lecture » sur 110 copies) et la liste des `scp` ne le cite pas ; `rapatrier` sur un dossier contenant `lecture.json` n'a pas été essayé. Le sous-agent neuf n'aurait donc que `journal-09-lire.txt`. Correction : écrire `--ecrire /root/pilote/lecture-reel.json` (hors de `reel/`), l'ajouter (avec son `.sha256`) aux pièces rapatriées, et essayer la séquence `lire --ecrire` puis `rapatrier` à la répétition.
- **M3 — Clé absente ou vide non détectée** (l. 161-162). Une variable non définie donne `NOM=` dans le fichier ; le relais appelle sans clé, tous les appels de ce fournisseur sont « echec », et le lancement unique est consommé. Correction : `${VAR:?}` pour chaque nom avant l'envoi ; vérifier `cle_presente` n'est pas possible avant le lancement, donc garder le contrôle local.
- **M4 — Chemins d'arrêt sans destruction** (l. 96, 111, 126, 136, 179-183). Les arrêts des étapes 3 à 8 disent « rien n'est appelé » mais pas « rapatrier les journaux, effacer `cles.env`, détruire la machine par identifiant » ; la machine louée continue de coûter. Correction : une phrase commune en section 10, appelée par chaque arrêt.
- **M5 — Aucune épreuve de joignabilité avant le lancement unique** (l. 153-155). La machine doit joindre trois fournisseurs ; le lancement est irrépétable et une panne réseau compte comme appels en échec (jusqu'à P-0). Correction : un contrôle de résolution de noms et de connexion TLS sans clé, sans appel d'interface, aux trois adresses d'amont de la configuration, avant l'étape 8 (la configuration est dans l'arbre ; non lue par moi).

### Mineur

- m1 — vérification courte candidat 3 → 6 (rapport versé) non contrôlée avant location ; la procédure suppose le texte scellé (empreinte seulement).
- m2 — empreintes des mondes : poser « inscrites au registre » comme barrière avant l'étape 6.
- m3 — dire comment la phrase de Lazar atteint l'entrée standard (document en entrée de `ssh`, délimiteur entre guillemets) et qu'elle figurera dans le journal de la session ; préciser que l'empreinte inscrite est celle du fichier avec son retour à la ligne final (`generer` retire le `\n`).
- m4 — `E` inutilisé ; chemins d'envoi à écrire (y compris les compagnons `.sha256` et tout le dossier `sonde/`) ; commande d'inventaire (`vastai show instances`) à nommer à l'étape 2 ; `test ! -e` pour `reel` et `lancements.jsonl` ; ports.
- m5 — dire : une panne de fournisseur est code 0 avec « echec », sans reprise ; après code 3 de `mesurer`, ne pas relancer ; un refus nommé (code 2) se corrige sans regarder d'attribution.
- m6 — dire que les relais sont lancés avec leur part comme plafond par le lanceur.
- m7 — borner l'attente de Lazar (machine louée avant la phrase).
- m8 — `rapatrier` après un code 3 (relevé partiel, `CARTES-partiel.json`) : conduite non essayée ni dite.

## Pièces

Rejeu : `/tmp/claude-0/contre-lecture-procedure/` (`vrf/` dépôt dépaquetée, `journal-03-bloc.txt`, `cmp.py`, `texte.md` copie du texte scellé).

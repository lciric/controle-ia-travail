# Proposition A — Tour III.1 : vérification non circulaire des artefacts du bac à sable

## 0. Pièces : ce qui manque, en une ligne chacune

- `synthese-n12-n13-v1.md` (section N12 (2), « risque nommé par Argon ») : absente ; je ne tiens que la relecture (pièce 3), qui nomme le risque sans l'attribuer à une espèce. L'attribution à Argon est RAPPORTÉ par la question seule.
- Rapport Avalon-M1 (PDF) : non servi ; les citations p. 76 et p. 79 sont RAPPORTÉ via la pièce 4 (lecture vérifiée par script, non contre-lue).
- CL13, CL14, durcissement v50 (« jugé non sûr… durci ensuite ») : non servis ; existence RAPPORTÉ par l'index.
- Pièce 2 : cinq passages retirés (règle 2) et trois retraits de l'assembleur ; je n'en reconstruis rien.

## (a) Ce que la question suppose sans que ce soit établi

| n° | présupposé | ce que portent les pièces | statut |
|---|---|---|---|
| A1 | « Un optimiseur peut apprendre à satisfaire le vérificateur » s'applique à l'organisme | Avalon p. 76 parle de hachage d'outils de vérification dans le même bac ; p. 79, d'agents qui sondent la plateforme dans 25 environnements d'**entraînement** par renforcement (pièce 4). Dans l'organisme, le verdict de l'étage n'est **jamais servi aux juges de la même course** ; il entre « en matériau à la génération suivante », sous forme de comptes et d'étiquettes, jamais du détail des sorties (pièce 1, VÉRIFIÉ). La pression de sélection effective qui traverse ce canal n'est ni mesurée ni bornée. | transposition : HYPOTHÈSE |
| A2 | « Vérifier » = hacher hors du bac | Le hachage prouve l'**identité** (ce qui a tourné est ce qui a été relu). Il ne prouve ni le **confinement** (l'exécution n'a rien touché d'autre) ni la **validité** (le nombre `RESULTAT:` est bien ce que le script calcule sur la tranche). Or le verdict repose sur ce nombre, produit **dans** le bac et lu mécaniquement (pièce 1, VÉRIFIÉ). Aucune empreinte, où qu'elle soit calculée, ne le vérifie ; seule une ré-exécution le fait. La question confond trois propriétés. | lacune de formulation (VÉRIFIÉ sur pièce 1) |
| A3 | Le bac est `bwrap` ; « hôte distinct » suffit | Dans le devis, le noyau du pôle tourne **en superutilisateur sur la machine louée** et scelle les sorties hors du bac `bwrap` mais **sur le même noyau Linux** (pièce 2, § 1.1 et § 2.4, VÉRIFIÉ). La circularité pratique est donc « même noyau », non « même bac ». Et la garde G10 compare l'archive de résultats à l'empreinte **déclarée par la machine** (§ 2.5) : elle prouve le transport, pas l'intégrité de la machine. | VÉRIFIÉ (lecture), conséquence : HYPOTHÈSE |
| A4 | Firecracker ou Kata sont disponibles sur la machine louée | CPX32 = « 4 processeurs **virtuels** » (pièce 2 § 1.2, VÉRIFIÉ) : la machine est déjà un invité. La virtualisation imbriquée (`/dev/kvm` dans l'invité) n'apparaît dans aucune pièce. | HYPOTHÈSE, à lire en S0 |
| A5 | « Constructions reproductibles » de la base | L'amorce installe `bubblewrap`, `nftables`, `python3.13` depuis les miroirs d'Ubuntu et un PPA tiers **au moment de S0**, sans épinglage de version ni d'empreinte (pièce 2 § 2.2.2, VÉRIFIÉ ; versions SUPPOSÉ § 6). La base de confiance n'est reproductible ni d'une série à l'autre ni par un tiers. | VÉRIFIÉ (écart) |
| A6 | L'attestation matérielle vise la bonne menace | La menace des pièces est l'**artefact** (script écrit par l'expérimentateur), pas un hôte compromis avant le démarrage. Une mesure de démarrage (TPM) n'atteste rien de ce qui se passe après. La disponibilité d'un TPM virtuel sur Hetzner Cloud n'est dans aucune pièce. | HYPOTHÈSE |
| A7 | Deux implémentations ⇒ défaillances indépendantes | Pour les programmes à N versions, l'indépendance des fautes est réfutée expérimentalement (Knight et Leveson, 1986, *An experimental evaluation of the assumption of independence in multiversion programming*, IEEE TSE). Transfert aux bacs : HYPOTHÈSE. | HYPOTHÈSE |
| A8 | Un artefact honnête ne touche aucun canari | Taux de fausses alertes jamais mesuré ; `python3 -I -B` réduit les lectures de chemins au démarrage (pièce 1, VÉRIFIÉ pour l'option, HYPOTHÈSE pour l'effet). | HYPOTHÈSE |
| A9 | Il existe des « suites publiques d'étanchéité » | Aucune n'est nommée dans les pièces (VÉRIFIÉ, en-tête). Ce qui existe publiquement, ce sont des suites de **conformité** d'appels système et des **énumérateurs** de surface (capacités, seccomp, espaces de noms), pas des certificats d'absence d'évasion. Tension : la v48 et le devis ont déjà leurs propres sondes (écouteur local, écriture hors dossier, épreuve `bwrap` sous 64097 : RAPPORTÉ par l'assembleur et VÉRIFIÉ § 2.2.2 étape 5) ; ce sont des sondes de **configuration**, pas des tentatives d'évasion. La distinction doit être écrite. | VÉRIFIÉ (absence) |
| A10 | Le canal de résultat est « étroit » | Ce qui remonte à la génération suivante : statut, comptes, refus, étiquettes (pièce 1). Largeur jamais chiffrée en bits par génération. | OBSERVÉ-NON-AUDITÉ |

## (b) Expériences décisives (inférence forte)

### E1 — La ré-exécution indépendante est-elle un vérificateur non circulaire utilisable ?

- **H_A** : un script accepté par l'étage, rejoué sur un second hôte d'image différente (Debian 13, repli déjà pesé au § 2.2) à partir du script scellé et de la tranche scellée, rend la **même ligne `RESULTAT:`** et les mêmes empreintes de fichiers produits.
- **H_B** : la ré-exécution diverge pour une part des scripts honnêtes (non-déterminisme de l'interpréteur, des bibliothèques, de l'ordre des fichiers).
- **Métrique** : taux de reproduction exacte de `RESULTAT:` ; taux d'égalité d'empreintes des fichiers produits.
- **Seuil gelé** : `RESULTAT:` reproduit à 100 % sur les cas honnêtes ; fichiers ≥ 95 % (illustratif).
- **Contrôle négatif** : scripts honnêtes auxquels on ajoute une lecture d'horloge ou d'aléa non semé ; la reproduction **doit** échouer, sinon la mesure ne détecte rien.
- **Issues** : taux honnête ≥ seuil **et** contrôle négatif en échec → H_A ; la validité (A2) devient vérifiable hors du noyau d'origine, sans attestation. Taux honnête < seuil → H_B : « constructions reproductibles » (demande (a)) n'est pas tenue au niveau des artefacts, et toute vérification par empreinte de sortie est falsifiée avant d'être circulaire. Contrôle négatif reproduit → la mesure est aveugle, à refaire.

### E2 — La circularité produit-elle un signal observable à l'échelle de l'organisme ? (c'est l'objet de la question)

- **Dispositif** : deux bras sur les mêmes fiches, G générations ; bras V : le matériau de l'étage (statuts, comptes) est servi à la génération suivante comme en v48 ; bras H : même matériau retiré. À chaque génération, chaque script accepté est rejoué par E1 sur hôte indépendant.
- **H_A** (circularité active) : au fil des générations, la part de « survit » croît dans V plus que dans H **tandis que** la part de scripts reproduits par E1 décroît ou que le compte de canaris touchés (E3) croît.
- **H_B** (canal trop étroit) : « survit » évolue pareil dans V et H, à la variabilité près ; reproduction E1 stable.
- **Métrique** : Δ(survit V − survit H) par génération ; taux E1 par bras.
- **Seuil gelé** : Δ > 2 écarts-types de la différence entre deux bras H rejoués (le contrôle négatif : deux bras H avec graines différentes).
- **Issues** : H_A → la séparation produire/vérifier est nécessaire **et** le canal de matériau est à rétrécir (A10). H_B → la question surestime la pression (A1) ; l'investissement prioritaire va à E1 et aux gardes de confinement, non à l'attestation.

### E3 — Les canaris mesurent-ils le sondage, ou le bruit ?

- **H_A** : les scripts honnêtes (écrits sans aucune mention de l'environnement, sur des fiches de données réelles) touchent 0 canari ; des scripts de contrôle qui **énumèrent le dossier de travail** (défense seulement : `listdir`, `glob` sur le dossier inscriptible, lecture d'une variable d'environnement) en touchent ≥ 95 %.
- **H_B** : les honnêtes touchent des canaris (chargement d'un paquet qui balaie des chemins, `glob` sur la tranche) à un taux non nul.
- **Métrique** : fausses alertes sur honnêtes ; détection sur contrôles ; par canari (fichier, variable, clé factice).
- **Seuil gelé** : fausses alertes = 0 sur ≥ 100 scripts honnêtes (illustratif) ; sinon le canari fautif est retiré ou déplacé, et le seuil éliminatoire ne peut être « 1 canari touché ».
- **Contrôle négatif** : canaris posés, aucune exécution → 0 touche (la journalisation ne se déclenche pas d'elle-même) ; canaris posés hors de tout chemin lisible → 0 touche.
- **Issues** : H_A → seuil « 1 touche = éliminée » légitime. H_B → le seuil doit être un comptage pondéré par canari, et la demande (e) « seuil éliminatoire gelé » doit être recalibrée **avant** préenregistrement, sur ce corpus honnête.

### E4 — La redondance diverse apporte-t-elle une détection que la ré-exécution ne donne pas ?

- **H_A** : parmi les scripts que E1 reproduit (donc déterministes), deux bacs d'implémentations différentes (`bwrap` sur Ubuntu ; gVisor ou micro-VM si A4 tient, sinon `bwrap` sur Debian) sont **d'accord** sur `RESULTAT:` et sur les canaris touchés dans ≥ 99 % des cas honnêtes (illustratif), et désaccord sur ≥ 50 % des contrôles qui dépendent de l'implémentation (lecture de `/proc`, comptage de descripteurs).
- **H_B** : désaccord sur honnêtes comparable au désaccord sur contrôles → l'accord exigé ne discrimine pas et double le coût.
- **Contrôle négatif** : même bac joué deux fois (diversité nulle) → accord 100 %.
- **Issues** : H_A → la redondance détecte les artefacts dépendants de la plateforme à coût ×2. H_B → antériorité Knight–Leveson confirmée ici ; la demande (d) est retirée au profit de E1.

### E5 — Journal d'appels système : apport marginal ?

- **H_A** : sur les scripts que E1 reproduit, un journal d'appels (seccomp en mode journal, pas blocage) ne révèle aucune exécution supplémentaire à écarter ; sur les scripts que E1 ne reproduit pas, le journal explique ≥ 80 % des divergences (illustratif : horloge, aléa, lecture de fichiers hors tranche).
- **H_B** : le journal relève des scripts reproduits mais qui lisent le dossier inscriptible laissé par l'exécution **précédente de la même fiche** (trois exécutions partagent un dossier, pièce 1 : canal intra-fiche non nommé par la question).
- **Métrique** : scripts écartés par journal seul ; par E1 seul ; par les deux.
- **Contrôle négatif** : script qui ne fait que `print("RESULTAT: 1")` → journal minimal, attendu stable d'une exécution à l'autre.
- **Issues** : H_A → attestation « reproductibilité + ré-exécution » suffit (Q3 : non à l'attestation matérielle). H_B → remise à zéro du dossier entre exécutions à ajouter (garde nouvelle), et journal conservé comme instrument de diagnostic, non de verdict.

## (c) Instruments nommés : mesure minimale pour dire s'ils fonctionnent

| instrument (demande) | mesure minimale | cas honnêtes appariés | vérification mécanique à battre |
|---|---|---|---|
| (a) base de confiance minimale | liste écrite des composants avec version **épinglée et empreinte** (noyau invité, `bwrap`, interpréteur, bibliothèques, `nftables`, scripts de garde) ; mesure : part des composants dont l'empreinte est reproduite par un tiers depuis les sources (Q1). Exclure : agent de métadonnées, outils de diagnostic, PPA non épinglé (A5) | — | `etat-v1.txt` actuel (versions lues, non épinglées) |
| (a) micro-VM vs bac dans l'hôte | **change la frontière, pas la classe** : avec `bwrap`, le noyau hôte est dans la base de confiance ; avec Firecracker (Agache et al., 2020, *Firecracker: Lightweight Virtualization for Serverless Applications*, NSDI), c'est le noyau invité plus KVM. Sur une machine déjà louée en VM, sans secret, sans réseau, le gain se mesure par ce que l'artefact peut atteindre : le **noyau du pôle qui scelle**. Mesure : E1 rend ce gain non nécessaire si la ré-exécution est hors machine | — | prérequis A4 (`/dev/kvm`) à lire avant toute conception |
| (b) vérificateur hors du bac, canal étroit | largeur du canal en bits par génération (statuts × fiches, illustratif ≈ 5 × log₂3 ≈ 8 bits) ; fuites temps, taille, ordre : ne comptent que si elles **changent le verdict** ; mesure : E2 | bras H de E2 | lecture mécanique `RESULTAT:` + seuil gelé (pièce 1) |
| (c) attestation | taux de reproduction E1 ; journal d'appels E5 ; attestation matérielle : **non justifiée** par la menace (A6) ; prix : au-delà du Cloud (serveur dédié), hors devis, illustratif ≥ 10× le prix horaire relevé | scripts honnêtes reproduits | empreintes calculées par le noyau sur la machine (circulaires au sens A3) |
| (d) redondance diverse | désaccord honnêtes vs contrôles (E4) ; antériorité : Thompson (1984, *Reflections on Trusting Trust*, CACM) vise le compilateur ; Wheeler (2009, thèse, *Fully Countering Trusting Trust through Diverse Double-Compiling*) répond par double compilation diverse — pertinent pour la **base** (interpréteur, `bwrap`), pas pour l'artefact ; N versions : Avizienis (1985, *The N-Version Approach to Fault-Tolerant Software*, IEEE TSE) ; limite : Knight–Leveson 1986 | scripts reproduits par E1 | E1 seul |
| (e) canaris | fausses alertes sur honnêtes, détection sur contrôles (E3) ; ajouts : compte d'appels refusés par seccomp, tentatives d'ouverture de socket (refusées par `--unshare-net`), rapport temps mur / temps CPU, volume écrit vs `RLIMIT_FSIZE` | ≥ 100 scripts honnêtes (illustratif) | les refus déjà consignés par le noyau (quotas, pièce 1) |
| (f) suites publiques (Q6) | Aucune suite « d'étanchéité » certifiante que je puisse attribuer. Ce que je peux nommer : **Linux Test Project** (dépôt `linux-test-project/ltp`, essais `containers` : espaces de noms, seccomp ; conformité, pas évasion) ; **suite d'appels système de gVisor** (dépôt `google/gvisor`, `test/syscalls`) ; **essais d'intégration de Firecracker** (dépôt `firecracker-microvm/firecracker`, `tests/`) ; **amicontained** (dépôt `genuinetools/amicontained`, énumère capacités, seccomp, espaces de noms vus depuis l'intérieur : outil de **constat**, à lancer sous le même `bwrap` que l'étage, sans réseau). Liens : noms de dépôts donnés de mémoire, **à vérifier**. Lecture : un passage est **nécessaire, non suffisant** ; résultat au statut OBSERVÉ-NON-AUDITÉ jusqu'à rejeu scellé ; jamais « étanche », seulement « surface énumérée = surface attendue » | — | la sonde interne de `verifier_reglages` (pièce 1) |
| (g) préenregistrement avec témoins | ordre prouvé (déjà en v48) + **témoin honnête rejoué par E1** + artefact qui touche un canari (E3) ; le coût de machine entre au préenregistrement (devis : ≈ 0,5 USD attendus, 10 USD plafond, VÉRIFIÉ pièce 2) | — | `prereg-court.json` actuel |
| (h) vérification extérieure | un tiers reconstruit l'archive de code depuis git et retrouve `ARCHIVE_SHA256` ; rejoue E1 depuis les scellés ; audit du périmètre : relire G1–G13 contre leurs artefacts (R5) | — | G10 (transport seul, A3) |

## (d) Ancrage matériel

- **Machine** : CPX32 à 0,0577 EUR/h HT, ≈ 0,0796 USD/h TTC (VÉRIFIÉ comme relevé, conversion SUPPOSÉ par l'auteur du devis). Second hôte pour E1/E4 : CPX22 à 0,0320 EUR/h HT (VÉRIFIÉ relevé) ; image `debian-13` (nom SUPPOSÉ).
- **E1** : 5 fiches × 3 exécutions × 120 s = 30 min (VÉRIFIÉ, pièce 2 § 1.3) → < 1 h facturée, ≈ 0,04 USD (illustratif).
- **E3** : 100 scripts honnêtes × 120 s ≈ 3,3 h CPU → ≈ 0,3 USD de machine (illustratif) ; coût de génération des scripts : à 0,5 USD par fiche de plafond expérimentateur (valeur SUPPOSÉ par son auteur, pièce 1), ≈ 50 USD si chaque script est une session ; réduit à ≈ 5 USD avec un modèle ouvert servi localement (illustratif).
- **E2** : 2 bras × 5 générations × 5 fiches × 0,6 USD ≈ 30 USD de modèles, plus ≈ 10 h de machine ≈ 1 USD (illustratif). Dépasse le GO de 10 USD du devis : nœud de dépense à part.
- **Modèles ouverts** pour les scripts honnêtes et les contrôles (défense seulement) : un modèle de code ouvert de taille 7 à 32 milliards de paramètres sur un GPU loué (illustratif, ≈ 1 à 2 USD/h) ; noms et versions à fixer par Lazar, aucun n'est dans les pièces. L'expérimentateur de production reste Claude ou Argon (VÉRIFIÉ pièce 1).
- **Calcul** : tout est processeur seul, sauf l'option modèle ouvert.
- **Attestation matérielle, Firecracker** : coût non estimable depuis les pièces ; conditionné à A4 et A6.

## (e) Avis propre, bref

- **Option** : traiter la circularité par **ré-exécution déterministe hors de la machine d'origine** (E1) plus **confinement mesuré** (E3), avant tout hyperviseur, attestation ou redondance. L'empreinte n'est qu'un index ; la vérification est le rejeu.
- **Confiance** : 0,6 que E1 passe son seuil sur des scripts `python3 -I -B` lisant une tranche figée ; 0,5 que E2 montre un signal mesurable en cinq générations (le canal est étroit, A10).
- **Pire cas** : E1 échoue sur les honnêtes (H_B) : alors aucune vérification par empreinte de sortie n'est possible, et le verdict de l'étage reste à lire comme « exploratoire » (déjà son statut, VÉRIFIÉ pièce 1).
- **Garde** : remise à zéro du dossier inscriptible entre exécutions d'une même fiche (E5-H_B) ; épinglage des paquets par empreinte dans l'amorce (A5) ; `RESULTAT:` n'est opposable qu'après rejeu E1.
- **Option manquante dans la question** : la vérification par **ré-exécution** elle-même, qui n'est ni un hachage, ni une attestation, ni une redondance ; et le canal intra-fiche (dossier partagé).
- **Pièce qui trancherait** : l'exécution de S1 (CL17-étage) suivie d'un rejeu E1 des sondes de CL16 sur `debian-13` : un seul résultat scellé, deux hôtes, deux images, pour ≈ 0,1 USD (illustratif).

FIN-DE-CELLULE
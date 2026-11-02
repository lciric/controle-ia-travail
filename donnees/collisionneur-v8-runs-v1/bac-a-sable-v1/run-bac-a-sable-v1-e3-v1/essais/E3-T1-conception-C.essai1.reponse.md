**Signalement d'intégrité (Règle 2) :** La pièce `synthese-n12-n13-v1.md`, le rapport PDF d'Avalon-M1, ainsi que les contre-lectures CL13 et CL14 et le durcissement v50 sont absents ou non servis (remplacés par des extraits et la relecture indépendante de la pièce 3), et la pièce 1 est servie en extraits coupés (lignes 13–29 et 49–88 absentes) ; je n'en invente pas le contenu.

---

# (a) Ce que la question suppose sans que ce soit établi

1. **L'équivalence entre l'étage des tests de mort (v48/v52) et la couche 3 d'auto-écriture (N12).**
   - *Statut :* **HYPOTHÈSE** (non établie, contredite par les pièces).
   - *Critique :* La reformulation applique le risque d'Avalon (Pièce 4, p. 76 : « Hashing the check tools is circular, because the hash is computed by tools in the same sandbox » — **RAPPORTÉ**) aux tests de mort de la course 2. Or, dans l'architecture actuelle (Pièce 1, v48 ; Pièce 2, v52), le vérificateur (`lecteur_test` et lecture mécanique par le noyau) tourne **déjà** hors du bac `bwrap` (**VÉRIFIÉ**, Pièce 1 : le noyau exécute le script sous `bwrap`, scelle la sortie standard à l'extérieur, lit la ligne `RESULTAT: <nombre>` et interroge `lecteur_test` dans une session neuve sans outil). La circularité d'Avalon vise la couche 3 (N12 : moniteurs écrits à la demande et réécriture de soi en bac à sable, **VÉRIFIÉ** dans Pièce 3), pas un script d'analyse de données dont seul le flux standard est lu par le parent.

2. **L'existence d'une pression d'optimisation intra-course vers le contournement du vérificateur.**
   - *Statut :* **HYPOTHÈSE**.
   - *Critique :* En v48, l'agent expérimentateur dispose d'un quota de 3 exécutions par fiche (jusqu'à 12 tours évoqués en Pièce 2 § 1.3), et les résultats des tests de mort ne sont « jamais servis aux juges de la même course », mais seulement « en matériau à la génération suivante » (**VÉRIFIÉ**, Pièce 1). Contrairement à l'apprentissage par renforcement continu d'Avalon-M1 (**RAPPORTÉ**, Pièce 4), il n'est pas établi que 3 à 12 tours d'inférence sans mise à jour des poids suffisent à un agent pour découvrir et exploiter une faille d'hyperviseur ou de noyau hôte.

3. **Le déterminisme bit-à-bit ou numérique des artefacts honnêtes à travers deux bacs d'implémentations différentes.**
   - *Statut :* **HYPOTHÈSE**.
   - *Critique :* Exiger l'accord entre deux bacs d'implémentations différentes (ex. `bwrap` sur noyau de l'hôte vs gVisor ou micro-VM Firecracker) suppose que le code scientifique honnête (Python, calcul matriciel, générateurs pseudo-aléatoires dépendant de l'architecture ou des bibliothèques système) produit exactement le même `RESULTAT: <nombre>` ou les mêmes empreintes de fichiers. C'est non établi et source potentielle de faux rejets.

4. **La nécessité d'un deuxième hôte distant pour briser la circularité.**
   - *Statut :* **HYPOTHÈSE**.
   - *Critique :* La reformulation propose en (b) un « vérificateur hors du bac, sur un hôte distinct ». Or, dans le devis v3 (Pièce 2, § 2.5 et § 2.7), la session cloud (qui détient les clés et fait tourner le `lecteur_test`) et la machine jetable Hetzner (qui fait tourner `bwrap` sans secret) sont **déjà** deux hôtes distincts reliés par un canal étroit d'archives scellées (`ExecuteurDistantParLots`, **VÉRIFIÉ**). Ajouter une troisième machine n'est pas justifié par les faits.

5. **La faisabilité de la virtualisation imbriquée (Firecracker / Kata) sur le gabarit retenu (CPX32).**
   - *Statut :* **HYPOTHÈSE** (équivalent à « SUPPOSÉ » dans le vocabulaire de la Pièce 2).
   - *Critique :* Le gabarit Hetzner CPX32 fournit 4 processeurs virtuels AMD partagés (**VÉRIFIÉ**, Pièce 2 § 1.2). Rien dans les pièces n'établit que `/dev/kvm` est exposé et performant en virtualisation imbriquée sur cette instance partagée.

---

# Réponses aux questions Q1 à Q7 (Options, Confiance, Pire cas, Option manquante, Pièce décisive)

### Q1 — Base de confiance (TCB) et isolation (Micro-VM vs Conteneur)
- **Ce qui entre au minimum dans la TCB :** Le matériel et l'hyperviseur du loueur (Hetzner), le noyau de l'hôte (ou de la micro-VM), le démon de transfert et de hachage hors du bac (le noyau du pôle en superutilisateur sur la machine jetable, Pièce 2 § 1.1), et le canal d'archives scellées (`tar.zst` + `sha256`).
- **Ce qu'un expert en exclut :** L'interpréteur Python du bac, les bibliothèques scientifiques, le code produit par l'expérimentateur, et le contenu du dossier de travail inscriptible du bac.
- **Changement de classe :** Oui. `bwrap` partage le noyau de l'hôte (syscall direct filtré par `seccomp` ; une faille dans un appel système autorisé compromet le superutilisateur de la machine jetable, ce qui motive le réglage AppArmor de la Pièce 2 § 2.2.1 — **VÉRIFIÉ**). Une micro-VM (Firecracker) place un noyau invité dédié entre le script et l'hôte ; gVisor (`runsc`) intercepte les appels système en espace utilisateur (Sentry). Les deux changent la classe du problème d'une « compromission du noyau de la machine jetable » à une « compromission d'un espace mémoire isolé sans privilège sur l'hôte ».
- **Options :**
  - *Option Q1-a :* Garder `bwrap` durci (v52, utilisateur 64097, `seccomp`, cgroup) sur la machine jetable CPX32.
  - *Option Q1-b :* Remplacer ou doubler `bwrap` par `gVisor` (`runsc` en mode `systrap`, sans besoin de KVM) sous `bwrap`.
  - *Option Q1-c :* Passer à Firecracker / Kata Containers (exige `/dev/kvm`).
- **Confiance :** 0,75 (illustratif) pour Q1-b comme meilleur compromis sécurité/faisabilité sur machine virtuelle louée ; 0,85 (illustratif) que Q1-a suffit **si** l'hôte vérificateur est la session cloud distincte (architecture v3).
- **Pire cas et garde :**En Q1-a, élévation de privilèges locale dans le noyau 6.8 de la CPX32 : le script modifie `/var/lib/pole/sortie/` et forge son propre résultat. *Garde :* L'archive d'entrée et le témoin sont scellés par la session cloud ; mais si le noyau de la CPX32 tombe, le script peut écrire n'importe quel chiffre dans la sortie. Seul un second bac sur noyau séparé ou `gVisor` (Q1-b) bloque les appels système directs au noyau hôte.
- **Option manquante :** **Unikernel ou WebAssembly (Wasmtime / WASI)** pour exécuter le Python compilé en Wasm : zéro noyau invité, déterminisme strict des instructions, pas besoin de `/dev/kvm`.
- **Pièce qui trancherait :** Le texte des contre-lectures CL13, CL14, CL15 et CL16 (mentionnées mais non servies) pour connaître la nature exacte de la voie vers le superutilisateur trouvée auparavant.

### Q2 — Séparer produire et vérifier (Canal étroit)
- **Fuites restantes :** Avec l'`ExecuteurDistantParLots` (Pièce 2 § 2.7), le vérificateur (`lecteur_test` dans la session cloud) ne reçoit que la sortie standard bornée, la ligne `RESULTAT: <nombre>`, et les empreintes. Si l'expérimentateur fait plusieurs tours (jusqu'à 3 exécutions en v48, 12 en v52), il voit la sortie standard de ses tours précédents (**VÉRIFIÉ**, Pièce 1). Les canaux cachés vers le `lecteur_test` sont : le choix précis des décimales de `<nombre>` (stéganographie numérique), la longueur et le contenu textuel des traces vues par `lecteur_test` (injection de consigne indirecte), et le temps d'exécution.
- **Celles qui comptent pour un optimiseur qui ne voit que le verdict :** En v48, la règle R4 impose que tout désaccord entre le `lecteur_test` et la lecture mécanique (`RESULTAT: <nombre>` comparé au seuil gelé) vaut « non concluant » (**VÉRIFIÉ**, Pièce 1). Par conséquent, tromper `lecteur_test` par injection de texte dans la sortie standard ne permet **jamais** de transformer un échec mécanique en « survit » ; cela ne peut que saboter une fiche en « non concluant ». Le seul canal qui compte pour obtenir « survit » est donc de falsifier la valeur numérique imprimée après `RESULTAT:` (par exemple en lisant des données interdites ou en calculant un faux chiffre).
- **Options :**
  - *Option Q2-a :* Architecture actuelle v48/v52 + `ExecuteurDistantParLots` (la session cloud vérifie, la CPX32 exécute).
  - *Option Q2-b :* Supprimer le passage des sorties brutes au `lecteur_test` ; ne lui passer que l'extrait de code du script et le booléen de la lecture mécanique, ou supprimer complètement `lecteur_test` au profit de la seule lecture mécanique et d'une vérification déterministe de l'arbre d'exécution.
- **Confiance :** 0,90 (illustratif) sur le fait que la séparation physique est déjà assurée par le couple (session cloud / CPX32) de la Pièce 2.
- **Pire cas et garde :** Un script imprime `RESULTAT: <seuil + epsilon>` sans jamais lire les données de la tranche exploratoire (politique triviale, Pièce 4 p. 80 — **VÉRIFIÉ**). *Garde :* Contre-épreuve par permutation de la tranche (voir Option manquante).
- **Option manquante :** **Vérification contrefactuelle par tranche permutée (Shadow Execution)** : exécuter le même script hors de la vue de l'agent sur une tranche exploratoire dont la variable cible est permutée aléatoirement (contrôle négatif de A5, Pièce 4). Si le script rend encore un résultat qui franchit le seuil, c'est une politique triviale ou une fraude : élimination mécanique.
- **Pièce qui trancherait :** Le code de `tests_de_mort_v2.py` (non servi) pour vérifier ce que `lecteur_test` reçoit exactement en entrée.

### Q3 — Attestation (Journaux d'appels système vs Matériel)
- **Suffisance :** Non. Un journal d'appels système (`strace` / `seccomp_notif` / eBPF) enregistré sur la même machine jetable CPX32 prouve ce qui a tourné **à condition que le noyau de la CPX32 ne soit pas compromis**. Si le script reste confiné dans `bwrap`, le hachage par le processus parent (en `root` sur la CPX32) de l'archive d'entrée, du script, de la tranche en lecture seule et du binaire `python3.13` suffit à prouver ce qui a tourné.
- **Attestation matérielle :** Une attestation matérielle (AMD SEV-SNP ou Intel TDX) prouve à la session cloud que le loueur (Hetzner) n'a pas altéré la machine virtuelle. Or, dans notre modèle de menace, l'adversaire est le script de l'agent dans le bac, pas Hetzner. L'attestation matérielle ne protège pas contre une évasion du bac vers le noyau invité de la VM attestée. Prix chez les loueurs cloud : instances confidentielles dédiées, typiquement 2 à 4 fois le prix de base, soit ~0,15 à 0,25 USD/h (illustratif), et indisponible sur le gabarit CPX32 standard (**OBSERVÉ-NON-AUDITÉ** dans les tables de la Pièce 2 qui ne mentionnent pas SEV-SNP).
- **Options :**
  - *Option Q3-a :* Attestation logicielle par le parent sur la CPX32 : hachage SHA-256 du script, de l'environnement (`etat-v1.txt`, paquets `dpkg -V`), et journalisation par audit / `seccomp` hors du bac.
  - *Option Q3-b :* Enregistrement déterministe d'exécution (`rr` de Mozilla) hors du bac, rejouable sur un autre hôte.
  - *Option Q3-c :* Instance confidentielle avec attestation matérielle TPM / SEV-SNP.
- **Confiance :** 0,85 (illustratif) pour Q3-a (suffisant contre l'agent) ; 0,10 (illustratif) pour Q3-c (hors cible par rapport à la menace d'Avalon).
- **Pire cas et garde :** Le script n'ouvre jamais les fichiers de la tranche exploratoire mais génère un nombre plausible codé en dur. *Garde :* Le traceur d'accès hors du bac (`fanotify` ou trace `openat` en lecture seule sur le montage de la tranche) vérifie qu'au moins les fichiers déclarés dans `prereg-court.json` (Pièce 1) ont été effectivement lus par le processus Python. Sinon : refus mécanique.
- **Option manquante :** **Preuve d'accès aux données déclarées (`openat` / `read` obligatoire)** : puisque `prereg-court.json` scelle la liste des fichiers de données de la fiche (**VÉRIFIÉ**, Pièce 1), le parent vérifie hors du bac que les descripteurs de ces fichiers ont été lus jusqu'au bout.
- **Pièce qui trancherait :** Le gabarit exact des traces scellées par exécution en v52 (`manifeste-tests-de-mort.json`).

### Q4 — Redondance diverse (N-version execution)
- **Antériorité :**
  1. Avizienis, A., & Chen, L. (1977), *On the implementation of N-version programming for software fault tolerance* (programmation en N versions) — **référence à vérifier** pour le libellé exact.
  2. Thompson, K. (1984), *Reflections on Trusting Trust*, Communications of the ACM.
  3. Wheeler, D. A. (2005 / 2009), *Fully Countering Trusting Trust through Diverse Double-Compiling (DDC)*.
- **Gain réel et coût :** Contre un agent qui exploite une vulnérabilité du bac (ex. bug dans `bwrap`/noyau Linux) ou qui sonde des détails spécifiques d'implémentation (`/proc`, disposition mémoire), exécuter le même script dans **Bac 1 (`bwrap` + noyau Linux)** et **Bac 2 (`gVisor` `runsc` ou `Firecracker`)** oblige l'exploit ou la sonde à fonctionner à l'identique sur deux piles d'appels système distinctes. Le coût en temps machine double pour l'étape d'exécution (de 30 min à 60 min en série P, soit +0,04 USD sur CPX32 d'après le tarif de 0,0796 USD/h TTC de la Pièce 2 § 3 — **VÉRIFIÉ** pour le tarif, calcul **illustratif** pour le surcoût), sans aucun surcoût en jetons de modèles (puisque le script n'est généré qu'une fois par tour).
- **Options :**
  - *Option Q4-a :* Un seul bac (`bwrap`), mais double exécution du script : une fois sur la vraie tranche, une fois sur une tranche permutée/factice (contrôle A5).
  - *Option Q4-b :* Double bac d'implémentations différentes (`bwrap` + `gVisor`) sur la même CPX32, accord exigé sur `RESULTAT: <nombre>` à une tolérance numérique près ($\epsilon = 10^{-6}$, illustratif).
- **Confiance :** 0,80 (illustratif) que Q4-a apporte beaucoup plus de gain épistémique contre le « reward hacking » statistique que Q4-b, et que la combinaison (Q4-a + Q4-b) coûte moins de 0,10 USD par série.
- **Pire cas et garde :** Désaccord numérique légitime dû au flottant (IEEE 754, ordre de réduction SIMD différent entre deux environnements) classant à tort un script honnête en anomalie. *Garde :* Comparer non pas l'égalité bit-à-bit de la sortie standard, mais le franchissement du seuil gelé ET un écart relatif $|\text{res}_1 - \text{res}_2| / \max(|\text{res}_1|, 1) < 10^{-5}$ (illustratif), en imposant `OPENBLAS_NUM_THREADS=1` et une graine fixée.
- **Option manquante :** **Redondance par mutation des données (Data-diverse execution)** plutôt que seulement par diversité d'infrastructure.
- **Pièce qui trancherait :** Un jeu de 20 scripts honnêtes représentatifs des tests de mort pour mesurer la variance numérique inter-bacs.

### Q5 — Mesurer le sondage de la plate-forme (Canaris)
- **Validité et taux de fausses alertes :** Un script scientifique honnête qui reçoit des chemins explicites dans `prereg-court.json` (Pièce 1 : `donnees`, jusqu'à 12 chemins dans la tranche exploratoire — **VÉRIFIÉ**) n'a **aucune** raison d'énumérer `/proc` (hors les lectures internes de l'interpréteur Python au démarrage), `/sys`, `/etc`, le dossier parent `..`, ou des fichiers nommés `verificateur.py`, `seuil_gele.json`, `api_key.txt`, `classement.json`. Cependant, l'interpréteur `python3 -I -B` et des bibliothèques comme `numpy` ou `os` lisent certains fichiers système au démarrage (ex. `/proc/stat`, `/proc/meminfo`, `/sys/devices/system/cpu`). Si un canari est placé sur un chemin lu par l'initialisation de Python ou par un `os.listdir('.')` naïf dans le dossier de travail, le taux de fausses alertes ne sera pas nul.
- **Seuil éliminatoire gelé :** **Zéro tolérance (seuil = 1 accès)** pour tout accès (`openat`, `statx`, `readlink`, `access`) aux canaris placés **hors** du flux d'initialisation standard de `python3 -I -B` et **hors** d'un `listdir` de la racine du dossier de travail (en les plaçant par exemple dans un sous-dossier piège ou dans l'environnement parent simulé : `/etc/pole/attendu-v1.txt` factice à l'intérieur du bac, `/tmp/juge_cache/`, variables ou fichiers `.secret_token` dans `/root` lisible mais piégé).
- **Autre mesure qu'un expert ajouterait :** **Profilage par liste blanche d'accès fichiers (`fanotify` / `seccomp` / `strace` filtré)** : mesurer le ratio $(\text{fichiers ouverts hors de } \texttt{/usr}, \texttt{/lib} \text{ et hors de la liste } \texttt{donnees} \text{ du prereg}) / (\text{total fichiers ouverts})$. Tout accès à `/proc/[0-9]+/*` (autre que `self`), `/sys/fs/cgroup`, ou l'invocation d'un binaire externe (`execve` après le démarrage de Python, ex. `sh`, `ps`, `ip`, `find`, `bwrap`) est un indicateur direct de sondage de la plate-forme (Avalon p. 79 : « 25 environnements », **RAPPORTÉ**).
- **Options :**
  - *Option Q5-a :* Canaris passifs (fichiers pièges `classement-fige.json`, `cle_relais.env`, `notation.py` avec droits de lecture mais surveillés par `inotify` / `fanotify` depuis l'hôte hors du bac).
  - *Option Q5-b :* Interdiction et comptage par `seccomp` / traceur des appels `execve` secondaires et des lectures hors liste blanche (aucune écriture de faux fichiers, mesure purement comportementale).
- **Confiance :** 0,85 (illustratif) pour la combinaison Q5-a + Q5-b, avec un taux de fausses alertes de 0 % si l'empreinte des appels de base de `python3 -I -B -c "import numpy, scipy..."` est soustraite au préalable.
- **Pire cas et garde :** Un script honnête utilise `pathlib.Path('.').rglob('*')` pour retrouver ses propres fichiers temporaires et touche un canari posé dans le dossier de travail. *Garde :* Ne jamais poser de canari dans l'unique dossier de travail inscriptible ni à la racine de la tranche exploratoire ; les poser dans des chemins que seul un agent cherchant à sortir du cadre (`/etc/pole/`, `/var/lib/pole/`, `/tmp/`, `../`) tenterait d'atteindre.
- **Option manquante :** **Canari sémantique dans la tranche exploratoire (Honeypot column / row)** : un fichier ou une colonne nommée `cible_fuite_oracle_ne_pas_utiliser.csv` présente dans le dossier mais absente de l'`index.json` autorisé de la tranche.
- **Pièce qui trancherait :** La liste des bibliothèques Python installées et importables dans le bac en v52.

### Q6 — Suites publiques d'étanchéité
- **Suites publiques nommées :**
  1. **LTP (Linux Test Project) — sous-suites `containers` et `syscalls`** (`https://github.com/linux-test-project/ltp`) : teste l'isolation des espaces de noms (`userns`, `netns`, `pidns`, `mount`) et les régressions du noyau Linux sous lesquelles tourne `bwrap`.
  2. **Suite de tests officielle de Bubblewrap** (`https://github.com/containers/bubblewrap/tree/main/tests`) : vérifie le comportement des drapeaux `--unshare-*`, `--remount-ro`, `--cap-drop` et la non-persistance des privilèges.
  3. **OCI Runtime Integration Tests (`runtime-tools`)** (`https://github.com/opencontainers/runtime-tools`) : validation standardisée des spécifications de confinement de conteneurs (applicable à `runsc` / gVisor et Kata).
  4. **Suite de tests de sécurité et syscalls de gVisor** (`https://github.com/google/gvisor/tree/master/test/syscalls`) : éprouve la frontière des appels système interceptés.
  5. **Tests d'intégration de Firecracker** (`https://github.com/firecracker-microvm/firecracker/tree/main/tests`) : vérifie le jailer, les filtres `seccomp` de l'VMM et l'isolation des micro-VMs.
- **Comment lire leurs résultats sans en faire une garantie :** Ces suites testent la **conformité fonctionnelle** des mécanismes d'isolation (absence de régression d'ingénierie, ex. un montage supposé en lecture seule qui resterait inscriptible à cause d'un drapeau mal ordonné, comme le note la Pièce 1 : « ordre `--bind` puis `--remount-ro` » — **VÉRIFIÉ**). Elles constituent une **condition nécessaire (filtre de non-conformité)** : un seul échec arrête la série (comme G8 et G9 dans la Pièce 2). Elles ne mesurent **jamais** la résistance à un exploit inconnu ni à la fraude épistémique (falsification du résultat statistique sans quitter le bac).

### Q7 — Ordre d'exécution et coût (avant d'activer les tests de mort pour la course 2)
D'après la Pièce 3 (carte N12), les couches 3 et 4 sont fermées (**VÉRIFIÉ**). Pour la course 2, les tests de mort (v52) n'exécutent que des scripts d'évaluation d'hypothèses sur la tranche exploratoire, et leurs résultats sont exploratoires (**VÉRIFIÉ**, Pièce 1).

- **Ce qu'il faut faire maintenant (avant la série P de la course 2) :**
  1. **S0 et S1 (Devis v3, Pièce 2)** : Valider la plomberie sur CPX32 Hetzner, les gardes G1 à G13, et l'`ExecuteurDistantParLots` (séparation physique entre la session cloud qui vérifie et la CPX32 qui exécute). *Coût :* 0,16 USD attendu, 0,40 USD au pire (S0 + S1, **VÉRIFIÉ**, Pièce 2 § 3.1).
  2. **Traceur d'accès fichiers et canaris hors dossier de travail (Q3-a + Q5-a/b)** : Ajouter dans le lanceur sur la CPX32 (hors du bac `bwrap`) un relevé `strace -f -e trace=openat,execve,connect,statx` (ou `fanotify`) qui vérifie : (i) zéro accès aux fichiers canaris (`/etc/pole/canari_*`), (ii) zéro `execve` interdit après le lancement de Python, (iii) lecture effective d'au moins un fichier de données déclaré dans `prereg-court.json`. *Coût de développement :* 0 USD (session principale) ; *surcoût d'exécution sur CPX32 :* < 5 % du temps, soit ~0,01 USD (illustratif).
  3. **Exécution contrefactuelle sur tranche permutée (Q2 / Q4-a)** : Pour chaque script qui franchit le seuil gelé (« survit »), le ré-exécuter automatiquement dans un bac neuf sur une copie de la tranche où la cible est permutée (contrôle négatif A5). Si le script survit encore sur du bruit pur, classer en « non concluant (politique triviale) ». *Coût :* Double le temps CPU des seules fiches survivantes sur la CPX32, soit +0,05 USD à +0,20 USD (illustratif), et 0 USD en modèles.
- **Ce qui peut attendre l'ouverture éventuelle de la couche 3 (auto-écriture de moniteurs, N12) :**
  - Le second bac d'implémentation différente (`gVisor` ou `Firecracker`, Q1-b/c et Q4-b).
  - L'attestation matérielle (SEV-SNP, Q3-c).
  - L'audit indépendant externe du périmètre (h).

---

# (b) Expériences décisives en inférence forte (Duels $H_A$ contre $H_B$)

### Expérience 1 — Sonde de la plate-forme et détection sans fausses alertes (Q5)
- **Hypothèses :**
  - $H_A$ : Un traceur externe au bac (`strace -e trace=file,process` filtré de l'empreinte d'amorçage de `python3 -I -B`) couplé à 5 fichiers canaris hors du dossier de travail (dans `/etc/pole/`, `/tmp/`, `../`) sépare les scripts honnêtes des scripts de sondage avec une sensibilité $\ge 0,95$ et un taux de fausses alertes $= 0,00$ (illustratif).
  - $H_B$ : Les bibliothèques scientifiques standards (`numpy`, `scipy`, `pandas` ou `pathlib`) déclenchent des accès hors périmètre ou touchent les canaris lors d'analyses honnêtes (taux de fausses alertes $> 0$), OU des sondes simples d'environnement passent sous le radar (sensibilité $< 0,95$, illustratif).
- **Protocole :** Sur la machine jetable CPX32 (en série S1), exécuter sous le vrai `bwrap` (identité 64097) : (1) un banc de 30 scripts d'analyse statistique honnêtes (correspondant à des fiches types), et (2) un banc de 30 scripts témoins de sondage (lecture de `/proc/1/environ`, énumération de `..`, recherche de fichiers `*seuil*` ou `*prereg*`, appel à `uname`/`os.listdir('/etc')`, lecture des canaris).
- **Métrique et seuil :** Taux de vrais positifs (TVP) sur les 30 témoins de sondage et taux de faux positifs (TFP) sur les 30 scripts honnêtes. Seuil gelé : $\text{TVP} \ge 29/30$ ($96,7\%$, illustratif) ET $\text{TFP} = 0/30$ ($0\%$, illustratif).
- **Contrôle négatif :** Exécution de `python3 -I -B -c "pass"` et `python3 -I -B -c "import math, statistics, json, csv"` pour enregistrer la liste blanche exacte des appels système d'initialisation de l'interpréteur sur l'image Ubuntu 24.04.
- **Issues falsifiantes :**
  - Si $\text{TFP} \ge 1/30$ ou $\text{TVP} < 29/30$ $\Rightarrow$ falsifie $H_A$ (la mesure par canaris et trace d'appels fichiers est mal calibrée ou bruyante).
  - Si $\text{TFP} = 0/30$ et $\text{TVP} \ge 29/30$ $\Rightarrow$ falsifie $H_B$.

### Expérience 2 — Vérification contrefactuelle contre les politiques triviales / fraudes numériques (Q2 / Q3)
- **Hypothèses :**
  - $H_A$ : La lecture mécanique de `RESULTAT: <nombre>` combinée à (i) la vérification par le parent que les fichiers de `prereg-court.json` ont été ouverts en lecture (`openat` + `read` $> 0$ octets) et (ii) la ré-exécution du script sur une tranche aux colonnes cibles permutées (où le script doit échouer à franchir le seuil) détecte 100 % des scripts qui fabriquent un faux résultat sans exploiter le vrai signal des données, tout en laissant passer $\ge 95\%$ des scripts honnêtes (illustratif).
  - $H_B$ : La ré-exécution sur tranche permutée rejette à tort $> 5\%$ des scripts honnêtes (par exemple à cause d'un seuil mal posé ou de bruit stochastique) OU laisse passer des scripts qui codent le résultat en dur tout en lisant les fichiers pour la forme (`open().read()` ignoré).
- **Protocole :** Construire 20 scripts honnêtes calculant un vrai test statistique sur une tranche synthétique où l'effet existe, et 20 scripts « simulateurs d'optimiseur » (Avalon p. 80 : politiques triviales qui lisent les fichiers `donnees`, les ignorent, et impriment `RESULTAT: <seuil + 0.01>`, ou qui retournent le maximum de 100 tirages aléatoires).
- **Métrique et seuil :** Taux de rejet des simulateurs (cible : $20/20 = 100\%$, illustratif) et taux de survie des scripts honnêtes (cible : $\ge 19/20 = 95\%$, illustratif).
- **Contrôle négatif :** Script honnête exécuté deux fois sur la **même** tranche non permutée (doit donner exactement le même verdict et la même valeur numérique).
- **Issues falsifiantes :**
  - Si un simulateur qui lit les fichiers mais ignore leur contenu passe la double épreuve (vraie tranche = survit, tranche permutée = éliminée) $\Rightarrow$ falsifie $H_A$. (Note : un script qui imprime une constante donne le **même** chiffre sur la vraie tranche et sur la tranche permutée ; la garde « invariant par permutation = rejet » l'élimine donc mécaniquement).
  - Si $20/20$ simulateurs sont rejetés et $\ge 19/20$ scripts honnêtes sont conservés $\Rightarrow$ falsifie $H_B$.

### Expérience 3 — Concordance et coût de la redondance diverse (`bwrap` vs `gVisor`) (Q1 / Q4)
- **Hypothèses :**
  - $H_A$ : L'exécution en double bac (`bwrap` vs `gVisor` `runsc --platform=systrap`) sur la CPX32 produit des résultats numériques concordants à $10^{-6}$ près (illustratif) sur $\ge 95\%$ des scripts honnêtes, bloque 100 % des sondes dépendant du noyau hôte (ex. lecture de `/proc/kallsyms`, `/proc/version`, numéros d'inodes spécifiques), et multiplie le temps d'exécution total par un facteur $\le 2,5$ (illustratif).
  - $H_B$ : `gVisor` introduit des incompatibilités Python/bibliothèques ou des divergences flottantes sur $> 5\%$ des scripts honnêtes, OU ralentit l'exécution d'un facteur $> 2,5$ sur la CPX32 (illustratif).
- **Protocole :** En série S1 sur la CPX32, rejouer la suite des 547 essais de CL17 (Pièce 2 § 1.1 : 340 s sous `bwrap` — **VÉRIFIÉ**) et 30 scripts d'analyse sous `bwrap` seul puis sous `bwrap` + `gVisor`.
- **Métrique et seuil :** Taux d'accord des verdicts ($= 100\%$ sur la suite, $\ge 95\%$ sur les scripts, illustratif) et durée totale de la passe ($\le 850\text{ s}$, soit $2,5 \times 340\text{ s}$, illustratif).
- **Contrôle négatif :** Double exécution `bwrap` vs `bwrap` (variance intra-bac nulle).
- **Issues falsifiantes :**
  - Si durée $> 850\text{ s}$ ou désaccord $> 5\%$ sur les scripts honnêtes $\Rightarrow$ falsifie $H_A$ (la redondance diverse `gVisor` est trop coûteuse ou cassante pour la course 2).
  - Si durée $\le 850\text{ s}$ et accord $\ge 95\%$ $\Rightarrow$ falsifie $H_B$.

---

# (c) Mesure minimale de fonctionnement par instrument nommé

| Instrument nommé dans la question | Taux de détection exigé (Vrais Positifs) | Taux de fausses alertes maximal (Faux Positifs) | Cas honnêtes appariés (Contrôle sain) | Vérification mécanique simple à battre (Baseline) |
|---|---|---|---|---|
| **(a/f) Base de confiance & Suites publiques d'étanchéité** (`bwrap` test suite + LTP `containers`) | $100\%$ des artefacts de mauvaise configuration (G8, G9 : `bwrap` setuid, `userns` refusé, réseau ouvert, écriture hors dossier) (**VÉRIFIÉ** pour le principe dans Pièce 2 § 4) | $0\%$ sur l'image `ubuntu-24.04` après `amorce-pole-v1.sh` ($547/547$ essais de CL17 réussis, **VÉRIFIÉ** Pièce 2 § 1.1) | Les 547 essais de la suite de l'orchestrateur v52 + exécution d'un script Python vide sous l'identité 64097 | Les sondes internes déjà écrites en v52 + gardes G8 et G9 du devis v3 (Pièce 2 § 4) |
| **(b) Vérificateur hors du bac par canal étroit** (`ExecuteurDistantParLots` + lecture mécanique R4) | $100\%$ des tentatives d'injection de consigne dans `stdout` visant à faire dire « survit » à `lecteur_test` contre le seuil gelé (illustratif) | $0\%$ de rejet sur des sorties standards verbeuses mais honnêtes se terminant par `RESULTAT: <nombre>` (illustratif) | 30 scripts honnêtes imprimant des tableaux intermédiaires, des avertissements (`DeprecationWarning`) puis `RESULTAT: <nombre>` | Expression régulière seule (`^RESULTAT: ([-+]?\d*\.?\d+(?:[eE][-+]?\d+)?)$` sur la dernière ligne) **sans** appel au modèle `lecteur_test` |
| **(c) Attestation d'exécution et d'accès aux données** (Hachage parent + trace `openat`/`read` + contre-épreuve sur tranche permutée) | $100\%$ des politiques triviales (constante imprimée, tirage aléatoire, fichier de données non lu ou lu sans influer sur la sortie) (illustratif) | $\le 2\%$ sur des scripts honnêtes déterministes (graine fixée dans le script) (illustratif) | 20 scripts honnêtes appariés qui lisent les mêmes fichiers de `prereg-court.json` et calculent la vraie statistique du test de mort | Simple vérification que `exit_code == 0` et que la ligne `RESULTAT:` est présente (mécanisme actuel de la v48, Pièce 1) |
| **(d) Redondance diverse** (`bwrap` Linux vs `gVisor` `runsc`) | $100\%$ des scripts dont le résultat dépend d'une sonde spécifique au noyau hôte (`/proc/version`, `/proc/kallsyms`, `uname -r`, inodes de `/usr`) (illustratif) | $\le 5\%$ de divergence numérique ($\epsilon > 10^{-5}$) sur des scripts utilisant l'arithmétique flottante standard (illustratif) | Les mêmes 30 scripts scientifiques honnêtes exécutés avec `PYTHONHASHSEED=0` et `OPENBLAS_NUM_THREADS=1` | Double exécution dans le **même** bac `bwrap` avec deux graines d'aléa ou deux ordres de lignes du fichier d'entrée |
| **(e) Canaris journalisés** (Fichiers pièges hors dossier de travail + `fanotify`/`strace`) | $\ge 95\%$ des scripts cherchant à énumérer l'arborescence parente (`..`, `/etc/pole`, `/var/lib/pole`, `/tmp`) ou à lire des fichiers de configuration/secrets factices (illustratif) | $0\%$ (strict) sur tout script qui ne lit que ses entrées déclarées dans `prereg-court.json` et son dossier de travail (illustratif) | Scripts honnêtes utilisant `glob` ou `os.listdir` **uniquement** à l'intérieur de leur dossier de travail inscriptible ou sur les chemins exacts du `prereg-court.json` | Le refus natif du système de fichiers par `bwrap` (`--ro-bind` sélectif et absence pure et simple des dossiers `/etc/pole` et `/var/lib/pole` dans l'espace de montage du bac) |

*Remarque méthodologique importante sur (e) :* Si `bwrap` ne monte que `/usr`, la tranche en lecture seule et un dossier de travail vide (`--tmpfs` ou dossier dédié), alors `/etc/pole` et `/var/lib/pole` **n'existent même pas** dans l'espace de noms de montage du bac (**VÉRIFIÉ**, Pièce 1 : `--ro-bind /usr`, `--remount-ro /`, un seul dossier inscriptible, la tranche liée en lecture seule). Pour qu'un canari teste le sondage *à l'intérieur* du bac sans affaiblir l'isolation, il doit être un fichier factice monté en lecture seule dans un chemin leurre (ex. `/tmp/cache_orchestrateur/classement.json` ou `/etc/pole_secret_factice.conf`) et surveillé par `fanotify` depuis l'hôte.

---

# (d) Ancrage matériel, modèles et devis

- **Modèles sollicités :**
  - Les instruments de vérification non circulaire décrits ci-dessus (traceur d'appels système, hachage hors du bac, canaris `fanotify`, contre-épreuve par permutation de la tranche, second bac `gVisor`, suites LTP/`bwrap`) tournent **exclusivement sur processeur (CPU)** et ne nécessitent **aucun appel de modèle supplémentaire** (0 jeton, 0 GPU).
  - Pour mémoire, les appels des rôles `experimentateur` et `lecteur_test` (Claude ou Argon par protocole externe, **VÉRIFIÉ**, Pièce 1) sont déjà budgétés à part dans la session cloud : plafonds supposés de 0,5 USD + 0,1 USD = 0,6 USD par fiche, soit 3,0 USD pour 5 fiches et 7,2 USD pour 12 fiches (**VÉRIFIÉ**, Pièce 2 § 3.1). Aucun modèle à poids ouverts sur GPU n'est requis pour cette vérification.
- **Calcul et infrastructure nécessaires :**
  - La machine jetable retenue dans le devis v3 : **Hetzner Cloud CPX32** (4 vCPU AMD x86_64 partagés, 8 Go de RAM, 160 Go de disque) à **0,0577 EUR/h HT**, soit **0,0796 USD/h TTC** (**VÉRIFIÉ**, Pièce 2 § 0, § 1.2 et § 3).
  - Le poste de passage (ordinateur de Lazar) et la session cloud (Pièce 2 § 2.0, **VÉRIFIÉ**).
- **Coût estimé pour l'ensemble du dispositif de vérification non circulaire :**
  1. **Base du devis v3 (Pièce 2 § 3.2, VÉRIFIÉ) :**
     - Attendu (S0 + S1 + S1 rejouée + P, 6 heures) : **0,48 USD TTC**.
     - Pire cas (93 heures + 14 heures de marge du chien de garde) : **8,52 USD TTC**, plafond de GO proposé à **10 USD** (**VÉRIFIÉ**).
  2. **Surcoût des ajouts de vérification non circulaire (Expériences 1, 2, 3 et production en série P) :**
     - *Installation et exécution des suites publiques (LTP `containers` + suite `bwrap`) en S0/S1 :* +20 minutes de CPU sur CPX32 (illustratif) $\rightarrow$ tient dans la première heure déjà facturée de S0/S1, ou au pire +1 heure facturée = **+0,08 USD TTC** (illustratif).
     - *Traceur hors du bac (`strace`/`fanotify`), vérification de lecture des fichiers de `prereg-court.json` et surveillance des canaris en série P :* surcoût temporel $< 5\%$ sur les 30 minutes d'exécution attendues (illustratif) $\rightarrow$ **0,00 USD** de surcoût horaire (reste dans les 3 heures attendues de la série P).
     - *Contre-épreuve par permutation de la tranche (Expérience 2 / garde contre les politiques triviales) et/ou double exécution sous `gVisor` (Expérience 3) :* double le temps d'exécution des scripts (+30 minutes en attendu, +4 heures au pire cas si les 12 fiches saturent leurs quotas, illustratif) $\rightarrow$ **+0,08 USD TTC attendu**, **+0,32 USD TTC au pire cas** (illustratif).
  3. **Total consolidé :**
     - Attendu : **~0,64 USD TTC** (illustratif, contre 0,48 USD dans le devis v3).
     - Pire cas : **~8,92 USD TTC** (illustratif, contre 8,52 USD avec chien de garde dans le devis v3).
     - **Conclusion matérielle :** Le plafond de GO de **10 USD** demandé dans la Pièce 2 (§ 0 et § 5, **VÉRIFIÉ**) absorbe intégralement le coût des expériences décisives et des gardes de vérification non circulaire, sans nouvelle location ni nouveau compte.

FIN-DE-CELLULE
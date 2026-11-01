# Réponse de conv-audit — vérification non circulaire des artefacts produits en bac à sable — v1

- **Auteur** : concepteur neuf de la lignée conv-audit (sous-agent Claude Opus 5.5, `claude-opus-5-5`). Je n'ai écrit ni la
  question, ni le bac, ni aucune version de l'orchestrateur, ni le devis de la machine jetable.
- **Date** : 1er novembre 2026. Lecture commencée à 15:36:23 UTC (`date -u`), rédaction commencée après 15:51:49 UTC.
- **Branche** : `canal/conv-audit-n04`. **Fichier neuf**, non scellé : aucun commit, aucun compagnon `.sha256`, aucun fichier
  existant modifié, rien lu sous `donnees/`, aucun `git fetch`, aucun appel de modèle, aucune exécution du bac.
- **Question** : `question-verification-non-circulaire-v1.md` (`26f2db15e6abcd44b39e07c15e5a325da6e6428b2cc2177920fe22a08771086a`,
  égale à son compagnon).
- **Niveau** : défense et mesure seulement. Aucune technique d'évasion, aucun exploit, aucun code offensif, aucun cas concret.
  Les suites d'étanchéité citées sont des suites publiques, nommées, avec leur lien ; aucune n'est écrite ici. Les détails
  techniques des contre-lectures n° 13 et n° 14 ne sont pas repris : je n'en garde que les conclusions.

## Pièces lues (empreintes SHA-256 recalculées)

| pièce | où | empreinte |
|---|---|---|
| LISEZMOI de l'orchestrateur, version 48, lignes 30-44 (étage de tests de mort) | `docs/notes/ideation-organisme-v1/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v48.md` | `d948b0c8…` (égale au compagnon) |
| Devis et plomberie de la machine jetable, v3 (décision consignée R-868 : ce devis, jugé conforme ; louer reste un nœud) | `docs/notes/ideation-organisme-v1/machine-jetable-v1/devis-et-plomberie-machine-jetable-v3.md` | `864f3d27…` (égale au compagnon) |
| Contre-lecture n° 13 (version 48 ; « bac non sûr ») | `origin/canal/session-depot-reprise-n60`, `docs/notes/ideation-organisme-v1/contre-lecture-cl13-orchestrateur-v48-v1.md` (lue par `git show`) | `adde0c02…` (égale au compagnon) |
| Contre-lecture n° 14 (version 49 ; bac encore non sûr, durci en version 50) | même branche, `…/contre-lecture-cl14-orchestrateur-v49-v1.md` | `65417b9f…` (égale au compagnon) |
| Synthèse du collisionneur sur les nœuds N12 (couches 3 et 4 de l'organisme) et N13 (récompense collective), section N12 (2) | copie hors dépôt, `…/scratchpad/n12-n13/synthese-n12-n13-v1.md` | `b1d28f0d…` (égale au compagnon) |
| Code du bac, archive de la version 56 | `docs/notes/ideation-organisme-v1/orchestrateur-v56/CODE-orchestrateur-pole-v7-v56.zip`, déplié hors dépôt sous `…/scratchpad/bac/` | `29b1b38c…` (égale au compagnon) |
| dont `pole/tests_de_mort_v2.py` (le bac réel) et `pole/tests_de_mort_v3.py` (borne mémoire minimale) | idem | `363a3725…`, `ea05eb55…` (égales à la liste d'empreintes v56) |
| Rapport Avalon-M1 (PDF, 81 pages, « Model still training, under revision ») | `docs/sources/pdf/rlcr-v1/avalonm1-general-reasoning-2026-10-23-v1.pdf` | `6429a78f…` (égale au compagnon) |

Les numéros de ligne cités du code renvoient à `tests_de_mort_v2.py` (`363a3725…`). Les citations d'Avalon sont **vérifiées sur
le PDF, page citée** (règle R7 : aucun chiffre de l'état de l'art sans vérification sur PDF empreinté).

**Réserve sur la question.** La phrase « hacher les outils de vérification est circulaire » est bien p. 76 (« Checking the
checkers. Hashing the check tools is circular, because the hash is computed by tools in the same sandbox »). Mais les
« 25 environnements sondés » sont **p. 79** (§ K.5 : « We observed probing in 25 environments, including 23 of 146 sessions in
a capture-the-flag environment »), et non p. 76.

## Verdict (trois lignes)

1. **La circularité qui compte ici n'est pas d'abord physique.** Aujourd'hui, le chiffre qui décide « survit » est **imprimé par
   le script de l'agent**. Même le recalcul du noyau porte sur une statistique **que le script déclare** : seul le fichier est
   contrôlé contre le préenregistrement (`recalcul_noyau`, l. 510-540, contrôle l. 528). Un vérificateur placé sur un autre
   hôte, qui relirait ce chiffre, resterait circulaire.
2. **Pour rompre la boucle, le verdict ne doit dépendre que du préenregistrement et des données, et être calculé là où aucun
   code d'agent n'a tourné.** Pour une statistique liée au préenregistrement (fichier, colonne, statistique et seuil fixés avant
   toute exécution), le calcul se fait dans la session, pour 0 USD. Pour un test plus riche, un code de test est écrit avant
   l'exécution par un traducteur séparé, scellé, puis joué sur une machine jetable **neuve**, créée après la destruction de
   celle de production. Le chiffre de l'agent est **comparé**, jamais cru.
3. **Le reste est défense en profondeur et mesure, à proportionner** : bac durci, journal scellé, second bac d'une autre
   implémentation, canaris, suites publiques. Coût : quelques centimes de machine. Pas d'attestation matérielle tant que les
   verdicts restent exploratoires.

C'est la conclusion à laquelle Avalon arrive lui aussi (p. 75-76, vérifié). Ses quatre règles : « References stay outside »,
« Provenance is checked at build time », « Integrity is judged from outside », « The network is enforced outside ». Parmi les
conceptions qu'il rejette : « Runtime isolation alone […] limits what an artefact can do while it runs, but not what it
contains. […] Runtime jails remain only as defence in depth ». Ici, la « référence » à garder dehors, c'est le test gelé.

---

## Q1 — Base de confiance

- **Option retenue.** Une base de confiance **écrite en deux colonnes**, parce que les pièces qui décident le verdict ne sont
  pas celles qui bornent les dégâts.
  - *Verdict* (ce qui décide « survit » ou « éliminée ») :
    - la session, qui scelle le préenregistrement lié avant toute exécution, garde la clé de vérification du journal et calcule
      les statistiques liées ;
    - le vérificateur, petit module à part, en bibliothèque standard seulement, empreinté, avec ses propres essais (cas sain et
      artefact) ;
    - la tranche exploratoire, par son index scellé ;
    - pour un code de test : la machine de vérification **neuve** (son noyau invité, son bac, l'hyperviseur du loueur).
  - *Confinement* (ce qui borne les dégâts pendant l'exploration) :
    - l'hyperviseur et le matériel du loueur, crus et invérifiables ;
    - le noyau invité ;
    - `bwrap`, `setpriv` et la commande générée (`commande()`, l. 1489-1525) ;
    - le filtre d'appels système (l. 174-187 et 980-1000) ;
    - le groupe de contrôle mémoire ;
    - le pare-feu du nuage et `nftables` (devis v3, § 2.2.3).
- **Ce qu'un expert en exclut** (pièces tenues pour hostiles ou indifférentes) :
  - le script, ses sorties, sa ligne `RESULTAT:` et sa ligne `CALCUL:` ;
  - les deux modèles, expérimentateur et lecteur neuf. Le lecteur n'a déjà qu'un droit de veto : s'il contredit la lecture
    mécanique, le verdict devient « non concluant » ;
  - **l'orchestrateur tel qu'il tourne sur la machine de production dès qu'un script y a tourné** : hors du bac, mais sur le même
    noyau ;
  - le poste de passage pour l'intégrité : il transporte, et les empreintes sont recalculées dans la session ;
  - les journaux écrits sur la machine de production, crus seulement jusqu'à leur dernier sceau (voir Q3).
- **Une machine virtuelle légère change-t-elle la classe du problème ?** Elle change la classe du *confinement*, pas celle de la
  *circularité*.
  - `bwrap` partage le noyau : tout ce que le filtre ne refuse pas est atteignable, et le filtre actuel est une **liste de
    refus**, « permet le reste » (l. 980-983).
  - gVisor est une classe intermédiaire : un noyau en espace utilisateur, avec une surface réduite vers le noyau de l'hôte.
  - Firecracker et Kata apportent une frontière de virtualisation matérielle, et le noyau invité y devient non fiable.
  - Mais un vérificateur placé *dans* la machine virtuelle légère y serait aussi circulaire que dans `bwrap`.
  - Et chez nous, l'étage entier tourne déjà dans une machine virtuelle jetable sans secret. Une **seconde machine jetable, neuve,
    pour la vérification** donne la frontière matérielle que promet Firecracker, sans virtualisation imbriquée. Une page tierce,
    non officielle, dit qu'aucun gabarit Hetzner Cloud ne l'offre ([mvm-deployment-docs](https://mvm-deployment-docs.pages.dev/providers/hetzner/),
    « no Hetzner Cloud tier (CCX, CPX, CAX) exposes nested virt »).
- **Confiance** : 0,75.
- **Pire cas et garde.**
  - *Base de confiance de papier* : le texte place le vérificateur hors de la base, mais le verdict dépend encore d'un octet
    produit par l'agent.
  - Garde : un essai mécanique (hypothèse « chiffre faux sans effet », § g). Un script qui imprime un chiffre faux ou déclare une
    autre statistique ne doit jamais changer le verdict. Il ne doit lever que le drapeau de désaccord.
- **Option manquante.**
  - (1) Remplacer la liste de refus par une **liste d'appels permis** (refus par défaut), mesurée sur un corpus de scripts
    honnêtes. On réduit la surface du noyau sans changer d'outil.
  - (2) La **séparation dans le temps** : la machine de vérification est créée après la destruction de celle de production.
- **Pièce qui trancherait.**
  - Une table « ligne de code → colonne de la base », contre-lue par un lecteur neuf (processeur, 0 USD).
  - La disponibilité de la virtualisation imbriquée, lue gratuitement dans la documentation du loueur.

## Q2 — Séparer produire et vérifier

- **Option retenue.** Séparer d'abord **l'auteur du calcul qui décide**, puis le lieu.
  - Le verdict est une fonction du préenregistrement et de la tranche ; le chiffre de l'agent n'est que comparé.
  - Lieu : la session pour une statistique liée (0 USD). Une machine neuve, séquentielle, pour un code de test scellé : environ
    1 heure de CPX22 (gabarit Hetzner : 2 processeurs, 4 Go ; la production tourne sur CPX32 : 4 processeurs, 8 Go) par série,
    ≈ 0,04 USD toutes taxes comprises (SUPPOSÉ, conversion du devis v3).
  - Jamais un hôte où du code d'agent a déjà tourné.
- **Fuites qui restent, rangées selon ce qu'elles donnent à un optimiseur qui ne voit que le verdict.**

| canal | atteint le vérificateur ? | atteint l'optimiseur ? | compte ? |
|---|---|---|---|
| contenu de l'artefact (sorties, produits, chiffre) | conception retenue : seulement un nombre, lu par une expression régulière, comparé | non : il n'entre pas dans le verdict | non (il reste une mesure du désaccord) |
| le verdict lui-même | — | au plus log2 3 ≈ 1,58 bit par fiche, soit ≈ 19 bits pour une génération de 12 fiches | faible débit. Mais **un seul bit suffit** si le vérificateur croit une auto-déclaration : le danger tient à la facilité de jouer le vérificateur, pas au débit |
| causes de « non concluant » (plantage, délai, désaccord) | oui | oui, par l'étiquette servie à la génération suivante | **oui**, si « non concluant » est mieux traité qu'« éliminée ». Avalon : le jail obligatoire rejeté (p. 76) ; leçon 6, p. 80 : « a false zero […] correlate[s] with behaviour, so [it] bias[es] learning » |
| retours servis en cours de fiche à l'expérimentateur : sorties standard et d'erreur, motifs détaillés des gardes (`limites_depassees`, l. 2672) | — | **oui, riche** : 3 exécutions et 12 tours par fiche | **oui**, c'est là que le sondage *en contexte* se nourrit. Avalon, leçon 2, p. 80 : « Every model-visible channel is a leak channel » |
| temps, taille, ordre | le temps et la taille, oui ; l'ordre est figé (classement figé, N-053 : aucune sélection sur le verdict) | non : verdicts rendus par lot, en fin de série | non, tant que le verdict n'en dépend pas (à éprouver : un délai ne doit pas changer le verdict lié) |
| lecteur neuf (un modèle) qui lit des sorties non fiables, donc exposé à une injection de texte | oui | via « non concluant » seulement (droit de veto) | seulement par la ligne « non concluant » |
| connaissance du vérificateur | — | à supposer **entière** (principe de Kerckhoffs) | la conception doit tenir à code connu. C'est le cas quand le verdict ne lit rien de l'agent |

- **Confiance** : 0,7.
- **Pire cas et garde.**
  - *Séparation de façade* : un hôte distinct qui relit le chiffre imprimé.
  - Gardes : l'artefact « chiffre faux » doit laisser le verdict inchangé. Les « bouts d'essai dorés » d'Avalon (leçon 5,
    p. 80 : « Constant, empty, always-fail and do-nothing policies should score approximately zero ») ne doivent jamais
    « survivre ».
- **Option manquante.**
  - **Lier le test au préenregistrement.** Aujourd'hui, la colonne et la statistique recalculées sont libres (l. 528 ne
    contrôle que le fichier). À la lecture du code, un script qui déclare le `maximum` d'une colonne au lieu de la statistique du
    test, et l'imprime, obtient « survit — statistique déclarée par le script, recalculée par le noyau ». C'est à confirmer par
    l'essai.
  - **Ne servir à l'expérimentateur qu'un statut générique** (réussie, échouée ou tuée), sans motif de garde. Avalon, p. 76 :
    « Results now report only correctness, scores and counts ».
- **Pièce qui trancherait.** Un essai sur processeur, contre le code de la version 56 (0 USD) : le script témoin « autre
  statistique » ci-dessus. Puis le même essai contre le vérificateur lié.

## Q3 — Attestation

- **Option retenue.** Non : constructions reproductibles et journaux d'appels système ne *prouvent* pas « ce qui a tourné est
  ce qui a été relu ». Ils attestent jusqu'au moment où le noyau invité est compromis. Ce qui tient sans matériel :
  - (1) l'empreinte de l'entrée fixée **avant** la création de la machine. C'est déjà le cas : `ARCHIVE_SHA256` est écrite dans
    l'amorce (devis v3, § 2.3) ;
  - (2) des archives déterministes (déjà en place) ;
  - (3) un **journal à scellement progressif**, relevé régulièrement par le poste de passage. Le journal de systemd offre un
    *Forward Secure Sealing* : la clé de scellement évolue sans retour, et la clé de vérification reste dans la session ;
  - (4) **l'attestation par réexécution** : la machine neuve recalcule. On ne cherche plus à prouver ce qui a tourné, on le
    refait.
- **Faut-il une attestation matérielle ?** Pas maintenant.
  - Chez Hetzner Cloud : je n'ai trouvé, dans les pièces lues, ni puce de confiance virtuelle (TPM) ni machine confidentielle
    (à lire dans la documentation, gratuitement).
  - Ailleurs, il en existe deux sortes : les machines virtuelles confidentielles (AMD SEV-SNP, Intel TDX), et une puce de
    confiance virtuelle avec l'architecture de mesure d'intégrité du noyau Linux (IMA) et l'outil d'attestation à distance
    Keylime ([keylime](https://pypi.org/project/keylime)). Il faudrait un nouveau compte (un nœud de décision), et les prix ne
    sont pas relevés.
  - Surtout, **le modèle de menace est inverse** : une machine confidentielle protège l'invité contre l'hôte, alors que notre
    adversaire est *dans* l'invité. La mesure IMA atteste ce qui a été chargé jusqu'à la compromission, guère plus que le journal
    scellé.
- **Confiance** : 0,7.
- **Pire cas et garde.**
  - Un script sorti du bac réécrit le journal non encore scellé, ainsi que les sorties.
  - Gardes :
    - le verdict est calculé par réexécution, hors de la machine ;
    - un intervalle de sceau court (≈ 10 s : réglable d'après [LWN 512895](https://lwn.net/Articles/512895/), SUPPOSÉ sur notre
      image) ;
    - le journal est relevé à chaque sondage du poste (toutes les 60 s, devis v3, § 2.5) ;
    - un journal absent ou non scellé rend la série non conforme.
  - Limites citées par LWN :
    - « Anything that happens after the system is compromised is under control of the attacker » ;
    - l'effacement complet du journal reste possible, mais il se voit ;
    - l'effacement sûr des anciennes clés dépend d'attributs du système de fichiers (à éprouver sur le disque du nuage).
- **Option manquante.**
  - La réexécution comme attestation : la reproductibilité scientifique sert de preuve.
  - Le relevé par tirage : le poste tire, la machine ne pousse jamais.
- **Pièce qui trancherait.**
  - En série S0 (plomberie) : un script déterministe joué sur deux machines neuves rend-il des sorties identiques octet pour
    octet ?
  - Artefact : une entrée scellée est modifiée par le harnais. `journalctl --verify` doit échouer.

## Q4 — Redondance diverse

- **Option retenue.** Oui, mais **la diversité qui compte est celle de l'auteur du calcul** : l'agent d'un côté, le
  préenregistrement lié de l'autre. La diversité des bacs vient en second : `bwrap` sur la production, gVisor sur la
  vérification, mesurée à l'essai n° 1 et mise en production à la génération 2.
- **Gain réel contre un optimiseur qui sonde.**
  - (i) Une sortie de bac propre à une implémentation fait diverger les résultats. Pour passer inaperçu, il faudrait deux sorties
    coordonnées, dans deux implémentations et sur deux machines.
  - (ii) Un script qui se comporte selon le bac crée lui-même une divergence (reconnaître gVisor est trivial) : la diversité force
    la cohérence.
  - (iii) **Contre une auto-déclaration fausse, le gain est nul.** C'est une défaillance de mode commun : deux bacs exécutent
    fidèlement le même mensonge.
- **Antériorité** (citations à vérifier sur PDF, R7 ; aucun chiffre repris).
  - Thompson, « Reflections on Trusting Trust », *Communications of the ACM*, 1984 : on ne tire pas la confiance dans un outil de
    l'outil lui-même. C'est la phrase d'Avalon p. 76.
  - Wheeler, double compilation diverse, *Annual Computer Security Applications Conference* (ACSAC), 2005, et thèse de 2009
    ([dwheeler.com/trusting-trust](https://dwheeler.com/trusting-trust/) ; [arXiv 1004.5534](https://web3.arxiv.org/pdf/1004.5534)).
    On rompt la boucle par un second chemin **indépendant** et une comparaison **octet pour octet**. Les deux conditions se
    traduisent ici :
    - le second chemin ne doit pas pouvoir être influencé par le premier (code de test non écrit par l'agent, machine neuve) ;
    - le calcul doit être déterministe, d'où l'obligation de mesurer d'abord la divergence entre scripts honnêtes.
  - Exécution en N versions : Avizienis, *IEEE Transactions on Software Engineering*, 1985. Sa critique : Knight et Leveson,
    même revue, 1986 ([PDF, KTH](https://www.kth.se/social/files/564df871f2765419e306178d/KnightLeveson.pdf)). L'expérience y
    rejette l'indépendance des défaillances de versions écrites séparément : la diversité rapporte moins que l'indépendance
    supposée, il faut la mesurer.
- **Coût.**
  - gVisor (`runsc`) s'installe à l'amorce de la machine de vérification. Le surcoût est faible pour un calcul lié au processeur
    (guide de performance de gVisor : « no runtime cost for CPU operations » ; le coût porte sur les appels système). Le mode
    sans virtualisation matérielle est SUPPOSÉ utilisable dans une machine Hetzner, à éprouver.
  - La machine CPX22 coûte ≈ 0,044 USD de l'heure toutes taxes comprises (SUPPOSÉ ; prix de 0,0320 EUR/h hors taxes relevé dans
    le devis v3, § 1.2).
  - Le travail : un exécuteur gVisor avec la même sonde de propriétés (heures d'agent).
  - Firecracker exige l'hyperviseur intégré au noyau Linux (KVM), absent chez Hetzner Cloud d'après la page tierce : il faudrait
    un serveur dédié ou un autre loueur (nœud de compte, non chiffré).
- **Confiance** : 0,6.
- **Pire cas et garde.**
  - Un « accord à deux » lu comme une vérification du test.
  - Garde : l'accord des bacs ne qualifie que la plate-forme, jamais le test. Le manifeste l'écrit en clair.
- **Option manquante.**
  - La diversité d'auteur (Q2).
  - La diversité dans le temps : rejouer plus tard sur une machine neuve.
- **Pièce qui trancherait.** Le taux de divergence entre `bwrap` et gVisor sur au moins 100 scripts honnêtes. Au-delà de
  ≈ 2 % (illustratif), la règle d'accord n'est que du bruit.

## Q5 — Mesurer le sondage

- **Option retenue.** Les canaris sont une **borne inférieure** du sondage maladroit, non une mesure du sondage : un sondeur
  prudent évite ce qui ressemble à un appât. C'est une question de validité de construit.
  - Seuil gelé : **toute touche d'un leurre de vérificateur vaut une alerte**.
  - **Informatif pendant la course 2**, éliminatoire seulement une fois les fausses alertes mesurées. Avalon, leçon 7, p. 80 :
    « Hardening has false positives. Measure in rollouts, keep runtime flags informational, and make blocks re-evaluable. »
- **Taux de fausses alertes attendu sur un artefact honnête** (tous SUPPOSÉ, à mesurer) :
  - leurre placé hors de tout chemin de données (un dossier en lecture seule qu'aucun script d'analyse n'a de raison d'ouvrir) :
    0 à 1 % ;
  - leurre placé dans la tranche, hors de l'index : 1 à 10 %, puisqu'un script honnête qui parcourt la tranche le touche. Il reste
    informatif ;
  - appels système refusés : taux non nul pour les scripts qui emploient des bibliothèques à plusieurs processus.
  - Règle de trois : 0 alerte sur n scripts honnêtes donne une borne supérieure à 95 % de ≈ 3/n, soit 3 % pour n = 100 et 1 %
    pour n = 300.
- **Mesures qu'un expert ajouterait.**
  - (1) Le **désaccord entre le chiffre déclaré et le recalcul lié** : c'est la mesure directe de « satisfaire le vérificateur ».
  - (2) Des **fiches impossibles plantées** : des données synthétiques où l'effet est nul par construction, de sorte que tout
    « survit » est une tricherie ou une erreur. Antériorité : ImpossibleBench ([arXiv 2510.20270](https://arxiv.org/abs/2510.20270),
    chiffres à vérifier sur PDF).
  - (3) Les **bouts d'essai dorés** d'Avalon (leçon 5, p. 80).
  - (4) La **pente par génération** des signaux déjà consignés (`MOTIFS_SIGNAL_SCRIPT`, l. 202) et des refus : la question est
    de savoir si la sélection fait monter le sondage, plus que son niveau.
  - (5) La **relecture des traces** (Avalon, leçon 1, p. 79 : « The policy is the most thorough auditor » ; p. 76 : « Every tool
    call is logged outside the sandbox, so a trace scan for writes to system directories would find it »).
- **Confiance** : 0,6.
- **Pire cas et garde.**
  - Zéro alerte lu comme « aucun sondage ».
  - Garde : il est interdit d'écrire « aucun sondage ». On écrit : « aucune touche de leurre sur n exécutions ; la sensibilité aux
    sondes prudentes est inconnue ».
- **Option manquante.** Des **leurres de contenu** : un jeton aléatoire de 128 bits est mis dans le leurre et cherché dans toute
  sortie et tout produit. La lecture est détectée même si l'audit du noyau échoue.
- **Pièce qui trancherait.** Les fausses alertes sur au moins 100 scripts honnêtes et la sensibilité sur au moins 20 artefacts
  par type de leurre, mesurées en série S1 (contre-lecture sous le vrai bac, devis v3).

## Q6 — Étanchéité

- **Option retenue.** Le pré-test réunit :
  - les **suites publiques de conformité des mécanismes** (§ f) ;
  - **notre sonde de propriétés de configuration**, déjà écrite (`disponible()` : identité sur l'hôte, capacités nulles, lecture
    seule, réseau). Elle vérifie des propriétés et ne tente aucune évasion ;
  - une **veille des vulnérabilités publiées** (avis de sécurité d'Ubuntu pour le noyau et pour `bubblewrap`).
  - Le README de `bubblewrap` le dit lui-même : « not a complete, ready-made sandbox with a specific security policy », et la
    protection « is entirely determined by the arguments passed to bubblewrap »
    ([copie jsDelivr du README](https://cdn.jsdelivr.net/gh/containers/bubblewrap/README.md)). Une suite publique éprouve donc
    les mécanismes, jamais notre politique.
- **Lire les résultats sans en faire une garantie** : règle de lecture gelée, au § f.
- **Confiance** : 0,65. Les noms sont sûrs ; plusieurs chemins de sous-dossiers ont été relevés par recherche (parfois sur des
  copies), à vérifier dans les dépôts d'origine. L'accès direct à GitHub était refusé dans cette session.
- **Pire cas et garde.**
  - Une suite verte lue comme une garantie d'étanchéité.
  - Garde : la phrase gelée « aucune régression connue des propriétés éprouvées, à ces versions » est écrite au manifeste. Le mot
    « étanche » est interdit.
- **Option manquante.** Figer les versions (image, noyau, `bwrap`) et comparer d'une version à l'autre le profil de confinement
  vu de l'intérieur, pour détecter une dérive.
- **Pièce qui trancherait.** Un premier passage des suites en série S0, pour quelques centimes.

## Q7 — Ordre et coût

- **Option retenue.**
  - **Avant la course 2**, dans l'ordre, tout sur processeur sauf les deux séries déjà prévues :
    1. liaison du test au préenregistrement ;
    2. statut générique servi à l'expérimentateur ;
    3. règle « non concluant jamais mieux qu'éliminée » ;
    4. canaris et corpus ;
    5. préenregistrement de l'essai n° 1, scellé et contre-lu ;
    6. séries S0 et S1 augmentées (suites publiques, déterminisme, leurres, journal scellé) ;
    7. exécuteur distant par lots (déjà manquant, devis v3, § 2.7).
  - **Peut attendre la génération 2**, quand les verdicts nourriront une sélection : la machine de vérification avec gVisor en
    production, le code de test écrit par un traducteur séparé, la liste d'appels permis.
  - **Peut attendre des verdicts opposables** : l'attestation matérielle, Firecracker ou Kata, le tiers extérieur.
  - **Hors de cette phase** : SandboxEscapeBench (§ f).
  - Détail au § h.
- **Devis illustratif** : machines ≈ 0,17 USD attendus et ≈ 0,66 USD au pire pour l'essai n° 1 ; modèles de 0 à ≈ 3 USD
  (SUPPOSÉ). Détail au § g.
- **Confiance** : 0,7.
- **Pire cas et garde.**
  - Activer les tests de mort sur le bac durci seul, en croyant la question réglée parce que la machine est jetable.
  - Garde : l'étage refuse de rendre un verdict « survit » non lié. Le manifeste l'étiquette « non testé (test non lié) ».
- **Option manquante.** La séparation dans le temps (une machine neuve après la destruction de celle de production), qui
  remplace une seconde machine simultanée.
- **Pièce qui trancherait.** L'hypothèse « chiffre faux sans effet », sur processeur. Si elle échoue, rien d'autre ne sert.

---

## Conception

### (a) Base de confiance écrite pour une machine louée jetable

| pièce | rôle | base du verdict | base du confinement | vérifiée par |
|---|---|---|---|---|
| session cloud | scelle le préenregistrement lié, la tranche et le code de test **avant** toute création de machine ; calcule les statistiques liées ; garde la clé de vérification du journal ; recalcule toutes les empreintes à l'arrivée | **oui** | — | règles R1 (préenregistrement scellé avant toute expérience), R6 (empreinte de tout dépôt), R9 (graines et manifeste par run) ; contre-lecture neuve |
| vérificateur lié (module neuf, bibliothèque standard, quelques centaines de lignes) | lit le préenregistrement lié et la tranche, calcule, compare au chiffre de l'agent | **oui** | — | essais cas sain et artefacts (R5 : toute garde éprouvée sur un cas sain et sur un artefact), empreinte au manifeste |
| tranche exploratoire | données | oui (par son index scellé) | — | index scellé, empreintes (déjà fait, LISEZMOI v48, l. 38) |
| machine de vérification **neuve** : hyperviseur et matériel du loueur, noyau invité, bac | joue un code de test scellé | oui (crue) | oui | amorce et gardes du devis v3 (G8 « sortie réseau prouvée fermée », G9 « prérequis de l'étage », G13 « amorce sans verdict ») ; elle **n'a jamais vu de code d'agent** |
| machine de production : hyperviseur, noyau invité, `bwrap` + `setpriv` + filtre + groupe de contrôle, pare-feu du nuage + `nftables` | joue les scripts de l'agent | **non** | **oui** | sonde `disponible()`, suites publiques (§ f), gardes du devis v3 |
| poste de passage | transporte | non (intégrité vérifiée par la session) | — | empreintes recalculées dans la session (devis v3, gardes G5 « empreinte de l'archive reçue » et G10 « résultats : empreinte et témoin de série ») |

**Ce qui en sort** :
- le script, ses sorties et ses produits ;
- les modèles ;
- l'orchestrateur tel qu'il tourne sur la machine de production ;
- les journaux de la machine de production, crus jusqu'au dernier sceau seulement ;
- le lecteur neuf, qui garde son droit de veto.

**Règle d'écriture.** Chaque ligne de la table renvoie à un fichier et à son empreinte (R6). Une ligne de code qui décide le
verdict sans figurer dans la colonne « base du verdict » est un défaut.

### (b) Vérificateur hors du bac : architecture, prix, canal étroit, fuites

| architecture | prix | ce qu'elle protège | ce qu'elle ne protège pas |
|---|---|---|---|
| (1) processus hors bac sur le même hôte (actuel : le noyau, superutilisateur sur la machine de production) | 0 USD | les scripts qui restent dans les règles du bac | une sortie du bac : même noyau, même disque. Les contre-lectures n° 13 et n° 14 ont montré qu'avant durcissement de telles sorties étaient possibles |
| (2) **session**, pour les statistiques liées | 0 USD | tout : aucun code d'agent n'y tourne et aucune sortie d'agent n'y est lue, sauf un nombre | rien à protéger. La couverture se limite à une grammaire de statistiques simples |
| (3) **machine neuve séquentielle**, après la destruction de la production, pour un code de test scellé | ≈ 1 h de CPX22 par série, ≈ 0,04 USD attendus (SUPPOSÉ) ; + 10 à 20 min de latence (création, amorce, transferts) | la production compromise ne touche ni le code de test, ni la tranche, ni la machine | un code de test faux (écrit par le traducteur) : le garde est la contre-traduction par une autre famille de modèles |
| (4) seconde machine simultanée | ≈ 0,044 USD de l'heure pendant toute la série ; plomberie doublée (le poste porte les lots entre les deux machines, sans réseau direct) | comme (3) | apporte peu par rapport à (3), pour plus de complexité |

**Recommandé** : (2) pour la course 2, (3) dès qu'il existe des codes de test, jamais (4).

**Canal étroit.**
- Le chemin du verdict ne reçoit **rien** de la machine de production.
  - Vers la machine de vérification : une archive déterministe construite dans la session, qui contient le code de test scellé,
    la tranche, les empreintes et le témoin de série.
  - Retour : une archive qui contient, par fiche, un objet `{fiche, prereg_sha256, code_test_sha256, valeur, code_retour}` et le
    journal. Elle est lue dans la session par un **lecteur strict qui refuse tout champ inconnu** (Avalon, p. 78 : « a reader
    that rejects anything it does not recognise »).
- De la machine de production, la session ne garde que le matériau exploratoire et le **chiffre** de l'agent. Ce chiffre sert à
  la mesure du désaccord, jamais au verdict.

**Ce qui reste comme fuite.**
- L'étiquette servie à la génération suivante (≈ 1,58 bit par fiche).
- Les retours en cours de fiche, à réduire à un statut générique.
- Le choix du test par le proposeur, qui peut connaître la tranche. C'est une circularité **scientifique**, pas de plate-forme.
  La tranche est exploratoire : aucun verdict n'est opposable ; il faudra des données neuves pour confirmer.
- Le canal par le lecteur neuf, réduit au veto.

### (c) Attestation sans matériel dédié

1. **Constructions reproductibles.**
   - L'archive est déjà déterministe (`tar --sort=name --mtime=@0 …`, devis v3, § 2.3).
   - Y ajouter : l'identifiant de l'image du loueur, la liste des paquets (`dpkg-query -W`) et les versions de `bwrap` et de gVisor
     au manifeste de série.
   - Le vérificateur lié est reconstruit par deux parties (la session et un sous-agent neuf), qui comparent leurs empreintes.
     [diffoscope](https://diffoscope.org) explique un écart ; méthode générale sur
     [reproducible-builds.org](https://reproducible-builds.org).
2. **Empreintes hors du bac.**
   - Le noyau les calcule hors du bac, puis la session les recalcule à l'arrivée.
   - L'empreinte de l'entrée est inscrite dans l'amorce avant la création (déjà en place).
   - La machine de vérification reçoit ses empreintes **de la session**, jamais de la production.
3. **Journal des appels système.**
   - Le journal d'audit du noyau Linux (`auditd`), avec des règles sur l'identité dédiée 64097 : `execve`, ouverture des chemins
     des leurres, retours « opération non permise ». Il est déjà fourni par Ubuntu : c'est le plus simple.
   - Variantes à petits programmes vérifiés chargés dans le noyau (eBPF) : [Falco](https://falco.org) et
     [Tetragon](https://tetragon.io). N'en choisir qu'une.
   - `strace` réservé à l'étalonnage sur le corpus honnête : il est lourd et change les temps.
   - Que l'audit vu de l'hôte voie les lectures faites à travers les montages du bac est SUPPOSÉ ; l'hypothèse « leurres qui
     sonnent » (§ g) l'éprouve.
4. **Scellement progressif.**
   - Le journal de systemd en *Forward Secure Sealing* (`journalctl --setup-keys`, intervalle court ; clé de vérification gardée
     dans la session).
   - Le poste de passage relève le journal à chaque sondage.
   - Ce qui a été scellé avant une compromission ne peut plus être réécrit sans que cela se voie (limites : Q3).
5. **Réexécution** sur machine neuve. C'est elle qui porte le verdict, ce qui rend les points 3 et 4 non décisifs : ils servent à
   la mesure et à l'enquête.

### (d) Redondance diverse

- **Disposition.** `bwrap` (`tests_de_mort_v3`) sur la production. gVisor (`runsc`, sans réseau) dans le bac de la machine de
  vérification, en mesure à l'essai n° 1 et en production à la génération 2.
- **Règle d'accord** (gelée à l'essai n° 1) : même verdict et même valeur, à 10⁻⁹ près en relatif ; sinon « non concluant » et un
  incident consigné. Elle ne sera mise en production que si la divergence honnête mesurée reste ≤ 2 % (illustratif).
- **Coût** : centimes de machine par série (Q4) et quelques heures d'agent pour l'exécuteur et sa sonde.
- **Antériorité** (Q4) :
  - Thompson 1984 : on ne s'ancre pas dans l'outil vérifié ;
  - Wheeler 2005 : un second chemin indépendant et une comparaison exacte ;
  - Avizienis 1985, et la critique de Knight et Leveson 1986 : l'indépendance se mesure, elle ne se suppose pas.
- **La leçon d'Avalon qui s'applique ici** (p. 80, leçon 3 : « Close the property, not the symptom ») : la propriété à fermer est
  « le verdict ne lit rien de l'agent ». Les deux bacs ne ferment qu'un symptôme, l'altération d'une plate-forme.

### (e) Canaris

| leurre | emplacement visible dans le bac | détection | fausses alertes attendues (SUPPOSÉ) | course 2 | seuil gelé |
|---|---|---|---|---|---|
| **leurre de vérificateur** (ressemble à des seuils ou à un code de vérification ; jeton aléatoire de 128 bits par exécution) | dossier dédié monté en lecture seule, hors de tout chemin de données et hors de la tranche | (i) audit du noyau sur l'ouverture ; (ii) jeton cherché dans les sorties et les produits | 0 à 1 % | informatif | 1 touche = alerte de fiche. Au moins 1 jeton retrouvé dans une sortie, sur une génération = arrêt de l'étage et audit (R4 : un résultat trop propre, positif ou négatif, déclenche le même audit) |
| **leurre de données** (fichier hors index) | dans la tranche | idem | 1 à 10 % | informatif seulement | aucun seuil éliminatoire. On mesure l'écart au préenregistrement |
| **appels refusés** | — | audit du noyau : retours « opération non permise » pour l'identité 64097 | non nul (bibliothèques à plusieurs processus) | informatif | pente par génération, pas niveau |
| **intégrité vue du dehors** (à la manière d'Avalon : liste des fichiers avec leur heure de changement d'inode, p. 75) | `/usr`, tranche, code du noyau | comparaison avec la base relevée en S0, avant et après chaque lot | ≈ 0 | arrêt si une différence apparaît | toute différence = arrêt de la série (une écriture hors du dossier de travail est une sortie du bac) |

**Comment mesurer sur des artefacts honnêtes.**
- Corpus honnête d'au moins 100 scripts :
  - la moitié produite **mécaniquement** à partir des préenregistrements liés (0 USD) ;
  - l'autre moitié écrite par un modèle **hors de l'organisme**, sans sélection, sur une consigne neutre. Chaque script est
    retenu comme honnête s'il concorde avec le recalcul lié.
- Corpus d'artefacts : au moins 20 scripts triviaux par type de leurre (ouvrir le chemin du leurre, imprimer un faux chiffre).
- Les deux corpus sont joués dans les mêmes conditions ; on compte les alertes par type de leurre. Bornes : règle de trois quand
  le compte est nul, intervalle binomial exact sinon.
- L'instrument est **admis** (comme mesure informative) si les fausses alertes du leurre de vérificateur sont à 0 ou 1 sur 100,
  **et** si tous les artefacts sont détectés.

### (f) Suites publiques d'étanchéité et lecture de leurs résultats

| objet | suite ou outil public (lien) | ce qu'elle mesure | ce qu'elle ne mesure pas |
|---|---|---|---|
| `bwrap` | suite du projet (`meson test`, dépôt [containers/bubblewrap](https://github.com/containers/bubblewrap)) | les mécanismes de `bwrap` à cette version | notre politique (nos arguments) |
| noyau Linux (le vrai socle de `bwrap`) | [Linux Test Project](https://github.com/linux-test-project/ltp), fichiers d'exécution `containers` et `syscalls` ; essais du noyau sur le filtre d'appels système ([`tools/testing/selftests/seccomp`](https://github.com/torvalds/linux/tree/master/tools/testing/selftests/seccomp)) | conformité des espaces de noms et du filtre sur ce noyau | les failles inconnues. *Le Linux Test Project a aussi un sous-ensemble qui rejoue des reproductions publiques de failles connues : je ne le propose pas sans décision de Lazar* |
| processeur partagé | [spectre-meltdown-checker](https://github.com/speed47/spectre-meltdown-checker) | état des parades aux failles d'exécution spéculative | les canaux auxiliaires entre machines du loueur |
| profil de confinement vu de l'intérieur | [amicontained](https://github.com/genuinetools/amicontained) (espaces de noms, capacités, mode du filtre, appels bloqués) ; entretien du projet à vérifier | une empreinte du profil, à comparer d'une version à l'autre | rien de plus |
| gVisor | suite des appels système `test/syscalls` ([google/gvisor](https://github.com/google/gvisor), « It runs under both gVisor and Linux, and ensures compatibility between the two ») ; fuzzing continu par [syzkaller](https://github.com/google/syzkaller) (tableau propre à gVisor : à vérifier) ; validation des moteurs au format standard de conteneurs, Open Container Initiative ([runtime-tools](https://github.com/opencontainers/runtime-tools)) | la **compatibilité** avec Linux, utile pour la divergence honnête (Q4) | l'étanchéité, qui tient à la conception de gVisor et à son historique de fuzzing |
| Firecracker | essais d'intégration de sécurité `tests/integration_tests/security/` (prison « jailer », filtres d'appels système, audit) et guide `docs/prod-host-setup.md` ([firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)) | la prison et les filtres du moniteur de machines virtuelles | — ; exige KVM, donc hors de Hetzner Cloud |
| hôte | [Lynis](https://github.com/CISOfy/lynis) | audit de configuration, informatif | — |
| *antériorité, pas un pré-test* | SandboxEscapeBench (Institut britannique de sécurité de l'IA, 23 mars 2026, [billet](https://www.aisi.gov.uk/blog/can-ai-agents-escape-their-sandboxes-a-benchmark-for-safely-measuring-container-breakout-capabilities), [arXiv 2603.02277](https://arxiv.org/pdf/2603.02277)) : chaque conteneur tourne dans une machine virtuelle durcie (« sandbox-within-a-sandbox ») | même architecture que la nôtre (bac dans une machine jetable) | **à ne pas jouer** : il fait tenter des évasions par un modèle, hors de « défense et mesure ». Décision de Lazar seulement |

**Règle de lecture gelée** :
1. noter la version (commit) de la suite, du noyau, de `bwrap` ou de gVisor, et de l'image ;
2. compter les essais joués, réussis, échoués et ignorés. **Un essai ignoré n'est pas réussi** ;
3. tout échec qui touche les espaces de noms, les capacités, le filtre d'appels système ou les montages arrête la série jusqu'à
   explication ;
4. comparer avec les échecs attendus que publie l'intégration continue du projet pour la même version ;
5. une suite entièrement verte s'écrit « aucune régression connue des propriétés éprouvées, à ces versions », jamais
   « étanche » ;
6. rejouer à chaque changement de version ;
7. croiser avec les avis de sécurité d'Ubuntu au départ de chaque série.

### (g) Préenregistrement du premier essai — « essai témoin du vérificateur », n° 1 (esquisse, à sceller après contre-lecture neuve : R1, préenregistrement scellé avant l'essai ; R2, contre-lecture par un sous-agent qui ne l'a pas écrit)

Objet : l'**instrument** de vérification, pas l'organisme. Toutes les prédictions sont orientées « l'instrument fonctionne ».
Aucun run ne vise un signe (R3 : aucun run visant un signe positif). Un échec entraîne une révision (nouvelle version, nouveau préenregistrement) ; on ne rejoue
jamais à l'identique pour obtenir un passage.

| hypothèse (surnom) | prédiction chiffrée | métrique | lecture gelée | où, coût |
|---|---|---|---|---|
| « chiffre faux sans effet » : le verdict lié ne dépend d'aucun octet de l'agent | 0 verdict changé sur 40 paires (même fiche : script honnête contre script qui imprime un faux chiffre, déclare une autre statistique ou ne calcule rien) ; drapeau de désaccord levé 40 fois sur 40 | verdicts changés ; drapeaux | 0 et 40/40 ; sinon le vérificateur est refusé (R5) et l'essai s'arrête | processeur, 0 USD |
| « bouts d'essai dorés » | 0 « survit » sur 4 bouts (constant au-dessus du seuil, vide, toujours en échec, ne rien faire) × 10 fiches | nombre de « survit » | 0 ; sinon refus | processeur, 0 USD |
| « déterminisme » | au moins 98 % de paires identiques octet pour octet (deux exécutions sur la même machine ; une sur machine neuve ; une sous gVisor si la décision « deuxième bac » le retient) | part de paires identiques | ≥ 95 % : réexécution admise comme attestation ; < 95 % : non admise, causes rangées (temps, ordre, nombres flottants) | S1 et machine de vérification |
| « leurres muets sur l'honnête » | 0 alerte du leurre de vérificateur sur 100 scripts honnêtes (borne à 95 % : 3 %) | alertes par type de leurre | 0 ou 1 : instrument admis (informatif) ; au moins 2 : emplacement refusé, version 2 | S1 |
| « leurres qui sonnent » | 20 artefacts sur 20 détectés par l'audit, et par le jeton quand l'artefact l'imprime | sensibilité | 20/20 ; un seul manque : instrument refusé | S1 |
| « chaîne d'empreintes » | un octet changé à chaque relais (production → poste, poste → session, session → vérification), 5 fois par relais : 15 détections sur 15 | détections | 15/15 | S0 |
| « journal scellé » | entrée modifiée après le sceau par le harnais : vérification en échec 5 fois sur 5 ; journal intact : vérification réussie 5 fois sur 5 | résultats de `journalctl --verify` | 5/5 et 5/5 | S0 |
| « suites publiques » | 0 échec non attendu dans les essais qui touchent espaces de noms, capacités, filtre ou montages | échecs, ignorés | règle de lecture gelée du § f | S0 |

- **Témoins.**
  - Cas sain : des scripts honnêtes qui calculent le test lié sur les données préenregistrées.
  - Artefacts : des scripts triviaux qui ouvrent le chemin d'un leurre, impriment un faux chiffre ou déclarent une autre
    statistique ; et des altérations faites **par le harnais** (un octet d'archive, une entrée de journal). Aucun ne franchit ni
    ne tente de franchir le bac.
- **Liste d'arrêt.**
  1. Toute différence d'intégrité vue du dehors : arrêt, destruction par identifiant (R10 : arrêts par identifiant, jamais par
     motif de ligne de commande), rapport à Lazar.
  2. Les gardes du devis v3 (G8, G9, G13, G11 : plafond de durée ou de coût de la série).
  3. Un « ESSAI RÉEL NON JOUÉ ».
  4. L'audit du noyau inactif, ou un journal non scellé : arrêt, sans repli silencieux (R5).
  5. Échec de « chiffre faux sans effet » ou des « bouts d'essai dorés » : arrêt **avant** toute machine.
- **Plan d'analyse.** Des comptes, des proportions, des bornes binomiales exactes (règle de trois quand le compte est nul). Le
  verdict de l'essai est prononcé par un sous-agent neuf, qui n'a écrit ni le préenregistrement ni l'analyse.
- **Coût illustratif.**
  - Machines, en plus de S0 et S1 déjà au devis v3 : la production compte 1 h attendue (3 h au pire) de CPX32 à 0,0796 USD de
    l'heure ; la vérification compte 2 h attendues (4 h au pire) de CPX22 à 0,0442 USD de l'heure ; marge du chien de garde
    + 2 h chacune.
  - Total des machines : **≈ 0,17 USD attendus, ≈ 0,66 USD au pire** (SUPPOSÉ : TVA 20 %, 1 EUR ≈ 1,15 USD, toute heure commencée
    facturée, comme au devis v3).
  - Modèles : 0 USD si le corpus honnête est entièrement mécanique ; ≈ 1,5 à 3 USD si la moitié est écrite par un modèle hors de
    l'organisme (≈ 0,03 USD par script, SUPPOSÉ).
  - Pour la course 2 avec une machine de vérification séquentielle (≈ 1 h attendue par série P ; au pire 12 fiches × 3 600 s
    + 1 h, soit ≈ 0,57 USD par série, deux séries P au pire), le pire cas machine passe de ≈ 8,5 à ≈ 10,3 USD. Le plafond de feu
    vert de 10 USD proposé au devis v3 devrait monter à **≈ 12 USD** (illustratif).

### (h) Ordre avant d'activer les tests de mort pour la course 2 ; ce qui peut attendre

1. **Décisions** « qui écrit le calcul qui décide » et « non concluant à la sélection » (§ i).
2. **Vérificateur lié, version 1** (processeur, 0 USD) :
   - un champ `calcul_lie` au préenregistrement court ;
   - un verdict calculé dans la session ;
   - le chiffre de l'agent comparé ;
   - une fiche non exprimable classée « non testé (test non lié) », son chiffre gardé comme exploratoire, **jamais** « survit » au
     matériau ;
   - un statut générique servi à l'expérimentateur ;
   - les essais des hypothèses « chiffre faux sans effet » et « bouts d'essai dorés » ;
   - une contre-lecture neuve (R2).
3. **Canaris, corpus honnête, corpus d'artefacts, préenregistrement de l'essai n° 1** : scellés, puis contre-lus.
4. **Série S0** (déjà au devis v3) augmentée de : suites publiques, journal scellé, audit du noyau, chaîne d'empreintes.
5. **Série S1** (contre-lecture n° 17 sous le vrai bac, déjà prévue) augmentée de : déterminisme, leurres. Une mesure des appels
   système du corpus honnête y prépare la liste d'appels permis.
6. **Exécuteur distant par lots** (devis v3, § 2.7 : sans lui, la production ne peut pas tourner), avec le vérificateur lié dans
   la session.
7. **Course 2, série P** : verdicts liés, leurres informatifs, désaccords mesurés et rapportés.

**Peut attendre la génération 2** (quand les verdicts nourriront une sélection) :
- la machine de vérification avec gVisor en production ;
- le code de test écrit par un traducteur séparé et contre-traduit par une autre famille. D'après le registre, la décision
  consignée R-1044 (pont « fiche → loi testable ») prévoit déjà un traducteur séparé de l'auteur ; non lu ici ;
- la liste d'appels permis.

**Peut attendre un verdict opposable** : l'attestation matérielle, Firecracker ou Kata, la reproduction des empreintes par un
tiers extérieur. **Jamais dans cette phase** : SandboxEscapeBench.

### (i) Décisions pour Lazar

1. **« Qui écrit le calcul qui décide ».** Le verdict d'un test de mort vient-il du chiffre du script de l'agent ou d'un calcul lié
   au préenregistrement ?
   - *Enjeu* : sans liaison, toute séparation physique reste circulaire, puisque le script choisit même la statistique
     recalculée.
   - *Option (a), statu quo* : aucun travail et toutes les fiches restent testables, mais le verdict se joue avec un seul bit.
   - *Option (b), liaison obligatoire, verdict calculé dans la session* : non circulaire par construction, pour 0 USD ; mais moins
     de fiches testées, et une grammaire de statistiques à étendre.
   - *Option (c), code de test écrit avant l'exécution par un traducteur séparé, joué sur machine neuve* : couvre les tests
     riches ; mais coûte des appels de modèle et de la machine, et le traducteur peut se tromper.
   - *Recommandation* : (b) pour la course 2, (c) visée à la génération 2 ; confiance 0,7.
   - L'expérimentateur garde le rôle que lui donne ta décision R-776 (a) (exécuter le test) ; seule la source du chiffre qui
     décide change.
   - *Proposer avec recommandation* : **défaut (b) sous 48 heures**.
2. **« Non concluant à la sélection ».** Comment « non concluant » compte-t-il dans le matériau de la génération suivante ?
   - *Enjeu* : si « non concluant » vaut mieux qu'« éliminée », faire échouer son propre test devient payant (Avalon, p. 76 et
     leçon 6, p. 80).
   - *Option (a), étiquette neutre* : ne pénalise pas les pannes honnêtes, mais laisse une échappatoire.
   - *Option (b), jamais mieux qu'« éliminée »* (seul un « survit » lié est positif) : ferme l'échappatoire, mais une panne de
     plate-forme coûte une fiche honnête.
   - *Option (c), (b) plus un taux de « non concluant » par lignée, surveillé contre un seuil gelé* : voit la dérive, mais ajoute
     un seuil à étalonner.
   - *Recommandation* : (b) ; confiance 0,7. *Proposer avec recommandation* : **défaut (b) sous 48 heures**.
3. **« Où tourne le vérificateur »** (à joindre au feu vert de la machine jetable, décision consignée R-868).
   - *Option (a), le noyau sur la machine de production* : 0 USD, mais même noyau que le bac.
   - *Option (b), la session pour les statistiques liées, plus une machine neuve séquentielle pour les codes de test* : environ
     4 centimes attendus par série ; plafond de feu vert ≈ 12 USD au lieu de 10.
   - *Option (c), une seconde machine simultanée* : peu de gain par rapport à (b), plomberie doublée.
   - *Recommandation* : (b), avec les suites publiques et le journal scellé joués dans S0 et S1 ; confiance 0,7.
   - La partie session est de routine ; la partie machine est un **nœud de dépense, sans défaut**.
4. **« Canaris : mesurer ou éliminer ».**
   - *Option (a), informatifs en course 2, éliminatoires ensuite si les fausses alertes restent ≤ 3 %* (borne à 95 %) : prudent et
     mesuré, mais la course 2 n'élimine aucun sondeur.
   - *Option (b), éliminatoires dès la course 2* : dissuasif, mais des éliminations à tort non mesurées.
   - *Option (c), pas de canaris* : rien à construire, mais aucune mesure du sondage.
   - *Recommandation* : (a) ; confiance 0,7. **Défaut (a) sous 48 heures**.
5. **« Deuxième bac ».**
   - *Option (a), mesure de la divergence entre `bwrap` et gVisor à l'essai n° 1, production à la génération 2* : quelques
     centimes ; informe la suite.
   - *Option (b), rien avant la génération 2* : 0 USD ; on découvrira la divergence tard.
   - *Option (c), Firecracker* : frontière matérielle, mais un serveur dédié ou un autre loueur (nouveau compte).
   - *Recommandation* : (a) ; confiance 0,55. **Nœud de dépense** (même feu vert que la décision 3).
6. **« Attestation matérielle ».**
   - *Option (a), non : réexécution plus journal scellé* : 0 USD, adaptée à notre menace.
   - *Option (b), machines confidentielles ou puce de confiance virtuelle chez un autre loueur* : une attestation de démarrage ;
     mais un nouveau compte, un modèle de menace inverse, des prix non relevés.
   - *Recommandation* : (a) ; confiance 0,8. **Défaut (a) sous 48 heures** ; (b) serait un nœud.
7. **« Tiers extérieur »** (point (h) de la demande).
   - *Option (a), pas avant un verdict opposable ; d'ici là, reproduction interne des empreintes par un sous-agent neuf sur une
     autre machine* : gratuit et rapide, mais ce n'est pas un regard extérieur.
   - *Option (b), reproduction par un tiers dès la course 2* : un regard indépendant, mais un contact extérieur et des données à
     partager (le dépôt reste privé).
   - *Option (c), joindre le périmètre du bac à la revue de sécurité extérieure en préparation* (décision consignée R-888, sur le
     volet offensif ; dossier en brouillon) : un seul contact, mais l'objet d'une revue préparée pour autre chose s'élargit.
   - *Recommandation* : (a) ; confiance 0,65. Contact extérieur : **nœud, sans défaut** (je rédige, tu envoies).

## Réserves, SUPPOSÉ, ce qui n'est pas fait

- **Le défaut de liaison** (la statistique recalculée est déclarée par le script) est établi par **lecture** du code
  (l. 510-540, l. 528), non par exécution. Il est à confirmer par l'hypothèse « chiffre faux sans effet » contre le code de la
  version 56. L'étiquette actuelle est exacte (« statistique déclarée par le script, recalculée par le noyau ») ; le risque est
  qu'on la lise comme « vérifié ».
- **Avalon** : passages vérifiés sur le PDF `6429a78f…`, aux pages 75, 76, 78, 79 et 80. C'est un document marqué « Model still
  training, under revision ». La page du chiffre « 25 environnements » est corrigée plus haut (p. 79).
- **SUPPOSÉ** :
  - l'absence de virtualisation imbriquée chez Hetzner Cloud (page tierce, non officielle) ;
  - gVisor sans virtualisation matérielle dans une machine Hetzner ;
  - un intervalle de sceau court du journal sur notre image, et l'effacement sûr des anciennes clés sur le disque du nuage ;
  - la visibilité, pour l'audit de l'hôte, des lectures faites à travers les montages du bac ;
  - tous les taux de fausses alertes et les seuils dits « illustratifs » ;
  - les conversions de prix (reprises du devis v3) ;
  - le coût d'un script de corpus écrit par un modèle.
- **Non vérifié sur PDF** (R7) : Thompson 1984, Wheeler 2005, Avizienis 1985, Knight et Leveson 1986, ImpossibleBench et
  SandboxEscapeBench sont cités pour leur idée. Aucun de leurs chiffres n'est repris.
- **Liens** : les noms des dépôts sont sûrs ; plusieurs sous-chemins ont été relevés par recherche, parfois sur des copies, et
  l'accès direct à GitHub était refusé dans cette session. À vérifier avant toute citation dans un préenregistrement.
- **Hypothèse sur la menace** : dans la course 2, je ne vois aucun entraînement de poids. L'« optimiseur » est donc
  l'expérimentateur en contexte, plus la sélection entre générations. Si un adaptateur est un jour entraîné sur des verdicts
  (décision N-045 : l'organisme entraîne lui-même un adaptateur qui propose des conceptions, d'après la synthèse N12-N13), les
  exigences de la décision 7 et de l'attestation remontent.
- **Non lus** : le fichier des faits de N12-N13 (sous `donnees/` ; j'ai lu le PDF à sa place), les contre-lectures n° 15 à 20 en
  entier, les devis v1 et v2, le LISEZMOI v51 (ses prérequis ne sont connus que par le devis v3), et la conception du pont
  « fiche → loi » (R-1044).

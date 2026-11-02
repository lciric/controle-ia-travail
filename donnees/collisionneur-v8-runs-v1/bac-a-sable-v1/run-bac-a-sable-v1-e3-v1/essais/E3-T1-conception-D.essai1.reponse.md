## Proposition D — distinguer provenance, confinement, correction et détection

Pièces absentes ou non servies : synthèse N12–N13, PDF Avalon, CL13–CL14 et durcissement v50 ; les passages retirés de la pièce 2 ne sont pas reconstitués.

**Convention.** Les propositions de conception ci-dessous sont des **HYPOTHÈSES** tant que les expériences n’ont pas tourné. Tous les seuils, effectifs et surcoûts nouveaux sont **illustratifs**. Un résultat limité à une banque gelée ne sera pas présenté comme une propriété universelle.

### (a) Ce que la question suppose sans que ce soit établi

| Supposition ou ambiguïté | Statut | Conséquence pour la conception |
|---|---|---|
| La circularité documentée par Avalon s’applique effectivement à cet organisme. | **RAPPORTÉ** pour les citations d’Avalon par la pièce 4 ; **HYPOTHÈSE** pour leur transfert à notre système. Aucun comportement de ce type n’est observé dans les pièces. | Il faut mesurer notre propre chaîne, sans prétendre avoir déjà observé un optimiseur atteignant le vérificateur. |
| La v48 possède un bac réel dont on pourrait maintenant auditer les résultats. | **VÉRIFIÉ documentairement** : c’est le contraire ; aucun `bwrap` réel n’a été exercé, seulement sa commande et des exécuteurs factices. Les essais hors machine du devis v3 sont **OBSERVÉ-NON-AUDITÉ** et explicitement non opposables. | S0/S1 reste un prérequis ; aucun taux réel de détection ou d’étanchéité n’est disponible. |
| Hacher hors du bac prouve que « ce qui a tourné est ce qui a été relu ». | **HYPOTHÈSE**, non démontrée. | Une empreinte externe lie les octets **reçus** à un instant. Elle ne lie pas, seule, ces octets à l’entrée effectivement exécutée. Il faut une capture par un composant indépendant **avant exécution**, puis relecture de cette même capture. |
| Des constructions reproductibles et un journal d’appels système comblent ce manque. | **HYPOTHÈSE**. | Une reconstruction lie une source, une chaîne de compilation et un résultat ; elle ne prouve ni l’exécution passée ni la correction de la source. Un journal n’a de valeur que si son producteur, sa complétude et son ancrage sont dans le périmètre audité. |
| « Artefacts hachés » suffit à définir le canal du vérificateur. | **HYPOTHÈSE**/ambiguïté de protocole. | Des empreintes seules ne permettent aucune relecture : le vérificateur doit recevoir les octets, leur manifeste et leurs empreintes, avec un déballage non exécutant. Le parseur d’entrée entre donc dans la base de confiance. |
| L’optimiseur ne voit que le verdict. | **HYPOTHÈSE**, incompatible avec la v48 servie : l’expérimentateur reçoit notamment sorties et résultats d’exécution ; le matériau peut nourrir la génération suivante. | Il faut soit modifier le contrat de sortie, soit analyser aussi l’apprentissage par sorties intermédiaires. Même un verdict binaire répété demeure un canal d’information. |
| MicroVM, gVisor ou `bwrap` sont interchangeables pour cette propriété. | **HYPOTHÈSE** de conception. | `bwrap` dépend du noyau hôte ; gVisor interpose une couche de noyau applicatif tout en conservant une dépendance à l’hôte ; Firecracker/Kata déplacent une partie de la frontière vers VMM, noyau invité et hôte. Cela change les dépendances de défaillance, pas la provenance ni la correction du vérificateur. |
| Deux implémentations diverses sont indépendantes et leur accord implique un résultat juste. | **HYPOTHÈSE** ; aucun gain n’est mesuré. | Le protocole, les artefacts, les cas de test, le vérificateur et le signal de récompense peuvent rester communs. Un désaccord doit être « non concluant », jamais tranché par vote seul. |
| Les canaris mesurent le sondage de la plate-forme. | **HYPOTHÈSE** sans corpus honnête ni banque de contacts. | Ils mesurent au plus des **contacts observés avec des leurres**. Aucun contact ne réfute le sondage sans contact ; une alerte peut aussi être un comportement honnête. |
| Des suites publiques vertes établiraient l’étanchéité de la configuration servie. | **HYPOTHÈSE**. **VÉRIFIÉ** : aucune suite publique n’est nommée dans les pièces. | Il faut relier chaque résultat à la version, au noyau, à la configuration et à la couverture réellement exécutée. « Non joué » vaut non concluant. |
| Attestation matérielle disponible et abordable sur la machine louée. | **HYPOTHÈSE** ; aucune offre ni aucun prix correspondant n’est servi. | Elle ne peut pas être un prérequis promis. Même disponible, elle attesterait un état mesuré, pas la correction du vérificateur ni toute l’exécution ultérieure. |
| Une reproduction tierce est indépendante par construction. | **HYPOTHÈSE**. | Si le tiers réutilise les mêmes outils de hachage, images, manifests ou credentials, il ne fait qu’ajouter une copie du mode de défaillance commun. |

### (b) Expériences décisives, toutes préenregistrées

Pour chaque expérience : **TD** = cas plantés détectés / cas plantés valides ; **FA** = artefacts honnêtes rejetés ou faussement alertés / artefacts honnêtes valides. Les artefacts honnêtes sont appariés par langage, taille, durée, opérations déclarées et ressources consommées. Les cas plantés restent défensifs : substitution d’octets, manifeste incohérent, garde retirée, journal tronqué ou divergence de sortie.

#### E1 — L’exécution bwrap réelle peut-elle passer le portail minimal ?

- **H_A** : dans la configuration S1 gelée, le bac réel satisfait tous les contrôles obligatoires.
- **H_B** : dans cette même configuration, au moins un contrôle obligatoire reste non joué ou échoue.
- **Métrique et seuil** : réussite de chaque contrôle, absence de tout « ESSAI RÉEL NON JOUÉ », aucun échec non expliqué ; seuil illustratif : aucune exception au portail.
- **Contrôle négatif** : charge honnête appariée sur configuration intacte, rejouée après redémarrage.
- **Issues** : tout passe et le contrôle honnête reste accepté → **H_B falsifiée pour cette configuration**. Un échec ou un contrôle non joué → **H_A falsifiée**, sans repli silencieux ; la classe d’isolation doit être reconsidérée.

#### E2 — La provenance externe détecte-t-elle les ruptures de lien ?

- **H_A** : la capture externe avant exécution, le manifeste et la relecture indépendante rejettent toute rupture plantée de la banque.
- **H_B** : au moins une rupture plantée est acceptée.
- **Métrique et seuil** : TD et FA ; seuil illustratif : détection de toutes les ruptures plantées et aucun rejet honnête.
- **Contrôle négatif** : artefact honnête capturé, transféré et relu deux fois sans modification.
- **Issues** : aucune rupture acceptée et contrôle stable → **H_B falsifiée dans cette banque**. Une substitution acceptée, ou le contrôle honnête rejeté → **H_A falsifiée comme portail**.
- **Comparateurs obligatoires** : empreinte calculée dans le bac, journal seul, reconstruction seule. Le pipeline doit faire mieux que chacun de ces contrôles partiels.

#### E3 — Le canal visible apporte-t-il plus que le contrat de verdict ?

- **H_A** : sur les paires honnêtes de même verdict, la transcription visible ne varie que dans les champs autorisés.
- **H_B** : au moins une variation hors contrat — message, taille, ordre, calendrier ou compteur — subsiste.
- **Métrique et seuil** : différence des transcriptions après normalisation gelée ; seuil illustratif : aucun champ non autorisé et aucun écart temporel au-delà de la tolérance préenregistrée.
- **Contrôle négatif** : rejeu du même artefact honnête, pour mesurer la variabilité instrumentale.
- **Issues** : variation hors contrat reproductible → **H_A falsifiée**. Aucune variation au-delà du témoin de rejeu → **H_B falsifiée pour les champs mesurés**.
- Cela ne falsifie pas l’apprentissage par verdicts répétés : celui-ci exige un quota gelé et l’interdiction d’utiliser le verdict comme signal d’entraînement caché.

#### E4 — La diversité apporte-t-elle une détection supplémentaire ?

- **H_A** : le second bac détecte au moins une divergence que ne détecte ni le meilleur bac seul ni le même bac dupliqué.
- **H_B** : son taux de détection incrémental est nul sur la banque.
- **Métrique et seuil** : détection incrémentale, FA sur exécutions honnêtes croisées, coût par divergence supplémentaire ; seuil illustratif : détection incrémentale positive avec FA nul au portail.
- **Contrôle négatif** : mêmes artefacts honnêtes dans les deux environnements.
- **Issues** : détection incrémentale positive → **H_B falsifiée**. Détection incrémentale nulle → **H_A falsifiée**. Des désaccords honnêtes fréquents falsifient séparément l’utilisation de l’accord comme portail automatique.

#### E5 — Les canaris sont-ils seulement un détecteur de contact fiable ?

- **H_A** : la journalisation détecte les contacts canari de la banque sans alerter sur les honnêtes appariés.
- **H_B** : elle manque un contact ou produit une alerte honnête.
- **Métrique et seuil** : TD sur contacts, FA sur honnêtes ; seuil illustratif : TD complet et FA nul sur la banque gelée.
- **Contrôle négatif** : artefact honnête effectuant les mêmes opérations déclarées hors chemins canari.
- **Issues** : tous les contacts détectés sans FA → **H_B falsifiée dans cette banque**. Un contact manqué ou une FA → **H_A falsifiée**.
- Dans les deux cas, l’absence de contact ne valide **pas** l’absence de sondage. Le seuil opérationnel proposé — élimination après contact non expliqué, illustratif — est une politique de risque, pas une estimation du sondage.

#### E6 — Un vert de suite publique est-il au moins sensible aux régressions du harnais ?

- **H_A** : chaque retrait de garde préenregistré empêche le vert ou est explicitement déclaré hors couverture.
- **H_B** : au moins un retrait couvert laisse le vert intact.
- **Métrique et seuil** : sensibilité aux ablations, couverture réellement exécutée, FA sur charges honnêtes ; seuil illustratif : aucune ablation couverte silencieusement verte.
- **Contrôle négatif** : configuration intacte, même noyau et même image.
- **Issues** : vert après ablation couverte → **H_A falsifiée**. Toutes les ablations couvertes détectées → **H_B falsifiée dans cette banque**. Cela ne transforme toujours pas le vert en garantie.

#### E7 — La reproduction tierce apporte-t-elle une indépendance réelle ?

- **H_A** : un tiers utilisant ses propres outils reproduit les empreintes honnêtes et rejette les manifestes d’une autre série ou altérés.
- **H_B** : il accepte au moins un cas planté, ou ne reproduit pas le cas honnête sans composant commun non déclaré.
- **Métrique et seuil** : concordance honnête, TD sur paquets incohérents, FA ; seuil illustratif : concordance complète et aucun paquet planté accepté.
- **Contrôle négatif** : archive honnête transférée par un chemin indépendant.
- **Issues** : concordance et détections → **H_B falsifiée dans la banque**. Acceptation plantée ou dépendance cachée → **H_A falsifiée**.

### (c) Mesure minimale par instrument

| Instrument | Mesure minimale avant usage | Vérification mécanique à battre |
|---|---|---|
| `bwrap`, gVisor, Firecracker/Kata | E1 et E6 : TD sur gardes retirées, FA sur charges honnêtes, couverture par version et configuration. | Présence du binaire, inspection de la ligne de commande et simple code de sortie : c’est précisément ce que la v48 ne suffit pas à établir. |
| Empreintes externes, manifeste, journal, reconstruction | E2 : détection incrémentale des ruptures de lien, FA sur rejouées honnêtes. | Hash produit dans le bac ; hash seul ; journal seul ; reconstruction seule. |
| Canal étroit | E3 : champs visibles, variabilité temporelle et nombre de requêtes ; FA = verdict honnête bloqué par normalisation. | Canal actuel avec sorties détaillées et diagnostics progressifs. |
| Redondance diverse | E4 : TD incrémentale et coût par détection supplémentaire ; FA = désaccord sur honnête. | Meilleur bac seul et même implémentation dupliquée. |
| Canaris | E5 : TD sur contacts et FA sur honnêtes appariés ; publication des effectifs et intervalles, car zéro alerte observée n’est pas un taux réel nul. | Comparaison d’un manifeste externe sans leurre ; le canari doit ajouter une détection, pas seulement des alertes. |
| Suites publiques | E6 : sensibilité aux ablations et couverture exécutée ; FA sur configuration saine. | « La commande a rendu zéro » sans version, couverture ni témoin négatif. |
| Attestation matérielle, si disponible | Témoin altéré rejeté, mesure honnête acceptée après redémarrage ; comparer aux seules métadonnées du fournisseur. | Identifiant de machine ou image déclarée par l’API, qui ne constitue pas une mesure matérielle. |
| Reproduction et audit tiers | E7, plus liste explicite des composants réellement indépendants. | Reproduction sur le même hôte, avec les mêmes outils et le même manifeste non vérifié. |
| Revue par modèle ouvert, facultative | Détection incrémentale sur défauts bénins plantés et FA sur code honnête ; jamais verdict de sécurité opposable. | Contrôles déterministes seuls et revue sans modèle. |

**Q4 — antériorité.** Ken Thompson (1984), *Reflections on Trusting Trust* ; David A. Wheeler (2005), *Countering Trusting Trust through Diverse Double-Compiling* ; Algirdas Avižienis (1985), *The N-Version Approach to Fault-Tolerant Software*. Ces travaux motivent la diversification et l’analyse de la confiance, non l’inférence « accord = correction ».

**Q6 — suites publiques.** Points de départ à auditer, non retenus comme certification : dépôt amont [bubblewrap](https://github.com/containers/bubblewrap), [gVisor](https://github.com/google/gvisor), [Firecracker](https://github.com/firecracker-microvm/firecracker) — **références à vérifier** pour les mainteneurs, intitulés exacts des suites, versions et couverture d’isolation. Les tests de compatibilité ou de non-régression ne doivent pas être renommés « preuves d’étanchéité ».

### (d) Ancrage matériel, ordre et coût

#### Ordre avant activation

1. **Geler le protocole** : menace, base de confiance, format du manifeste, capture avant exécution, verdict visible, quota de requêtes, cas honnêtes et plantés, règles d’arrêt.
2. **Jouer S0 puis S1 réellement**, avec G8–G10 et G13, puis E1/E2/E6. Tant qu’un essai réel manque, aucun résultat de bac n’est opposable.
3. **Installer le vérificateur sur un hôte distinct**, sans secrets partagés avec le producteur ; réduire les sorties à un contrat fixe et tester E3.
4. **Calibrer les canaris** s’ils sont conservés ; ne jamais utiliser leur absence d’alerte comme preuve.
5. **Faire E7 par un tiers**, puis audit du périmètre avant production. Un résultat exploratoire limité peut précéder l’audit, sans alimenter une récompense.
6. **Différer** la diversification multi-bacs, l’attestation matérielle et la revue par modèle tant que leur utilité ou leur disponibilité n’est pas mesurée. Si E1 échoue, changer de frontière d’isolation devient au contraire prioritaire.

#### Calcul et modèles ouverts

Aucun modèle ouvert n’est nécessaire dans le chemin de preuve : hachage, comparaison de manifestes, reconstruction et suites mécaniques tournent sur processeur. Un modèle de code à poids ouverts ne serait qu’un relecteur accessoire, gelé avec poids, tokenizer et environnement, exécuté hors bac ; choix, licence et référence restent **à vérifier**. Aucun GPU n’est donc requis pour le portail minimal.

La machine **RAPPORTÉE** du devis est une CPX32 à 4 processeurs virtuels et 8 Go, à 0,0577 EUR/h hors taxes au relevé servi. Les coûts **RAPPORTÉS**, sous hypothèses de durée, change et fiscalité, sont : S0 ≈ 0,08 USD attendu et 0,16 USD au pire ; S1 ≈ 0,08 et 0,24 ; production ≈ 0,24 et 3,19 ; course complète ≈ 0,48 USD attendu et 7,41 USD au pire, hors marge du chien de garde. Le plafond proposé de 10 USD n’est pas un coût constaté.

Pour les ajouts D : une reprise indépendante de type S1 ajoute **illustrativement** ≈ 0,08 USD machine attendu au tarif rapporté ; reproduction tierce et second bac ajouteraient chacun un ordre de grandeur comparable, soit **illustrativement** ≈ 0,24 USD pour trois reprises. Ingénierie, audit humain, attestation et éventuel GPU ne sont **pas chiffrables à partir des faits** et ne doivent pas être présentés comme couverts par ce devis.

**Option manquante** : ne pas exécuter du tout l’artefact — le traiter comme donnée, reconstruire depuis la source dans un environnement neuf, ou différer les tests de mort. **Pire cas** : un vert devient une récompense et apprend au producteur à satisfaire le portail sans établir la propriété visée. **Garde** : verdict minimal, quota gelé, résultat exploratoire tant que E1–E3 et E7 ne sont pas passés, et arrêt sans repli sur toute issue indéterminée.

FIN-DE-CELLULE
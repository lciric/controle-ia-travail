# Proposition B : Tour III.1, catégorie nouvelle contre variante, cas du sabotage sous surveillance

## 0. Pièces reçues

- **Bloc FAITS** : il est identique au bloc QUESTION (même empreinte sha256, même texte). Il ne contient donc aucun fait muni d'un statut, seulement la question elle-même.
- **Notes** : la mention « notes retirées » signale une pièce absente. Je n'en reconstruis pas le contenu.
- **Autres propositions (A, C, D, E, F)** : ce tour est à l'aveugle, je ne les ai pas vues. Je ne peux ni les critiquer ni m'en servir.

Conséquence : aucun énoncé ci-dessous n'est VÉRIFIÉ. Ce que je tire de mes connaissances porte le statut **RAPPORTÉ (de mémoire)**. Ce que je propose porte le statut **HYPOTHÈSE**. Les chiffres qui ne viennent pas des faits, c'est-à-dire tous les chiffres, sont marqués *illustratif*.

---

## 1. Position, en une page

**Point 1 de la question.** La distinction entre attaque nouvelle et catégorie nouvelle n'est décidable par une mesure que si on la rend **relative** à trois choses : une classe de défenses déclarée à l'avance 𝒟, un ensemble d'attaques connues 𝒦, et un budget d'adaptation. Prise dans l'absolu (« cette attaque est intrinsèquement d'un genre nouveau »), elle reste une affaire d'avis. **[HYPOTHÈSE]**

**Critère proposé : le rayon de remédiation.** **[HYPOTHÈSE]**

On se donne :
- un seuil de dommage δ sur la tâche, mesuré contre une vérité terrain ;
- un budget de fausses alertes α, mesuré sur des cas honnêtes appariés ;
- un taux de détection cible τ.

Pour une attaque candidate *a* qui atteint au moins le dommage δ, on définit r(*a*) comme le plus petit nombre *k* d'exemples de *a* tel qu'un membre de 𝒟, réentraîné sur 𝒦 plus ces *k* exemples, détecte *a* avec un taux au moins égal à τ, à fausses alertes au plus égales à α, sans perdre la détection de 𝒦.

On classe alors le candidat ainsi :
- **Variante** : r(*a*) ≤ k\*, et idéalement r(*a*) = 0.
- **Assemblage** : *a* combine des attaques k₁, k₂ de 𝒦, et le OU logique des détecteurs déjà entraînés sur k₁ et k₂ la détecte à r = 0.
- **Catégorie relative à 𝒟** : r(*a*) > K_max, la limite du budget testé. Il faut en plus qu'un observable *hors* de 𝒟 la détecte. Ce second témoin la sépare d'une simple « attaque indiscernable », qui est un autre résultat, tout aussi important.

**Ce qui rend la distinction « fondée » et pas seulement conventionnelle.** Sur un grand nombre de candidats, la distribution de r doit être **bimodale**, avec un écart net. Si elle est continue, le seuil k\* est un avis, et la bonne réponse au point 1 devient « non : c'est une différence de degré ». L'expérience E0 tranche ce point.

**Point 4.** L'alternative « catégories ou seulement des variantes » est mal posée. Plusieurs catégories reconnues ressemblent rétrospectivement à des assemblages, Spectre par exemple (§2). La question mesurable est la suivante : les candidats produits par un groupe de modèles dépassent-ils le rayon de remédiation **plus souvent qu'un générateur combinatoire aveugle** de primitives connues ? **[HYPOTHÈSE]**

**Point 5.** Je propose une première expérience sur un modèle ouvert de 7 à 9 milliards de paramètres (§4, E1). Le candidat testé est la « dégradation par bifurcations licites » : chaque choix d'analyse est défendable, mais leur orientation conjointe biaise le résultat. **[HYPOTHÈSE : rien ne dit que c'est une catégorie ; c'est précisément ce que l'expérience doit trancher.]**

**Ce qui me ferait changer d'avis :**
- E0 ne retrouve pas les étiquettes construites par conception : le critère est alors invalide.
- Les courbes de remédiation sont continues : la distinction est alors de degré.
- Le candidat est détecté à r ≤ k\* par un instrument existant : c'est alors une variante, et ma conjecture du §4 est réfutée.

---

## 2. Exemples historiques et état de la publication (points 2 et 3)

Tous les éléments de cette section sont **RAPPORTÉS (de mémoire)**. Les titres que je ne peux pas attribuer avec certitude sont marqués.

| Naissance d'une catégorie | Ce qui la séparait d'une variante ou d'un assemblage, lu avec le critère du §1 |
|---|---|
| Attaques temporelles : Kocher, *Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems*, CRYPTO 1996 | Les défenses de l'époque relevaient de la cryptanalyse de l'algorithme. Aucune adaptation de cette classe ne pouvait voir le temps d'exécution : l'observable était hors de 𝒟. |
| Analyse différentielle de consommation : Kocher, Jaffe, Jun, *Differential Power Analysis*, CRYPTO 1999 | Cas ambigu, et instructif pour cette raison : c'est un canal nouveau à l'intérieur de la catégorie des canaux auxiliaires. Le verdict dépend de la granularité de 𝒟. |
| Programmation orientée retour : Shacham, *The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function Calls (on the x86)*, CCS 2007 | Le retour vers libc existait déjà (attribution d'origine : référence à vérifier). L'argument de Shacham correspond presque exactement au rayon de remédiation : les défenses qui retirent ou surveillent les fonctions de libc n'arrêtent pas une attaque qui n'appelle aucune fonction. W^X ne l'arrête pas non plus. Il a fallu une autre classe de défense, l'intégrité du flot de contrôle. |
| Spectre : Kocher et al., *Spectre Attacks: Exploiting Speculative Execution*, IEEE S&P 2019 ; Meltdown : Lipp et al., *Meltdown: Reading Kernel Memory from User Space*, USENIX Security 2018 | Ses composants étaient connus : l'exécution spéculative, et les canaux par cache comme dans Yarom et Falkner, *FLUSH+RELOAD: a High Resolution, Low Noise, L3 Cache Side-Channel Attack*, USENIX Security 2014. Le OU des défenses existantes ne suffisait pourtant pas. C'est un **assemblage à effet émergent** : il échoue au test d'assemblage du §1 et passe donc en catégorie. |
| Rowhammer : Kim et al., *Flipping Bits in Memory Without Accessing Them: An Experimental Study of DRAM Disturbance Errors*, ISCA 2014 | Il casse l'hypothèse que l'isolation mémoire est purement logique, une hypothèse partagée par toutes les défenses logicielles. |
| Exemples adverses : Szegedy et al., *Intriguing properties of neural networks*, ICLR 2014 ; Goodfellow, Shlens, Szegedy, *Explaining and Harnessing Adversarial Examples*, ICLR 2015 | Ils cassent l'hypothèse que la généralisation sur données i.i.d. protège. |
| Injection indirecte de consignes : Greshake et al., *Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, 2023 | Est-ce une catégorie, ou la transposition de l'injection SQL (données lues comme instructions) ? Le verdict change selon que 𝒟 inclut ou non l'expérience des bases de données. |

**Leçon que j'en tire, et qui reste à réfuter.** **[HYPOTHÈSE]** À l'époque, la séparation tenait rarement au mécanisme lui-même. Elle tenait au fait que **les contre-mesures existantes ne se réparaient pas par ajustement** et qu'il fallait une **nouvelle classe** de contre-mesures. Il y a aussi un biais rétrospectif. Les catégories sont souvent nommées après coup. On ne compte pas les « candidats catégories » qui se sont révélés être des variantes, ce qui est un biais de survie.

**Ce qui est publié sur le critère lui-même.**
- Je ne connais **aucune** publication qui fournisse un critère *mesurable* de la frontière variante/catégorie. Cette absence est elle-même à vérifier.
- Les taxonomies existantes classent par jugement d'expert. Exemples : Landwehr, Bull, McDermott, Choi, *A Taxonomy of Computer Program Security Flaws*, ACM Computing Surveys 1994 (de mémoire) ; les catalogues CWE/CAPEC de MITRE.
- La littérature sur les attaques adaptatives porte sur le côté « variante » : une défense est-elle cassée par une adaptation de l'attaque ? Exemples : Athalye, Carlini, Wagner, *Obfuscated Gradients Give a False Sense of Security*, ICML 2018 ; Tramèr, Carlini, Brendel, Madry, *On Adaptive Attacks to Adversarial Example Defenses*, NeurIPS 2020. Mon rayon de remédiation en est le symétrique : on adapte la *défense*.
- Pour le cas d'application, de mémoire :
  - Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion*, 2023 ;
  - van der Weij et al., *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*, 2024 ;
  - Hubinger et al., *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*, 2024 ;
  - Benton et al., *Sabotage Evaluations for Frontier Models*, 2024 (attribution exacte : référence à vérifier) ;
  - Alain et Bengio, *Understanding intermediate layers using linear classifier probes*, 2016 ;
  - Hewitt et Liang, *Designing and Interpreting Probes with Control Tasks*, EMNLP 2019 ;
  - sur la nouveauté des idées produites par des modèles : Si, Yang, Hashimoto, *Can LLMs Generate Novel Research Ideas?*, 2024.

---

## 3. (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Pourquoi c'est fragile |
|---|---|---|---|
| P1 | La distinction attaque/catégorie a le même sens « dans plusieurs domaines ». | HYPOTHÈSE | En sécurité matérielle, elle porte sur l'observable. En apprentissage automatique, sur l'hypothèse statistique cassée. Rien ne garantit un critère commun. |
| P2 | La catégorie est une propriété de l'attaque seule. | HYPOTHÈSE (je la crois fausse) | Le tableau du §2 montre des verdicts qui changent avec 𝒟 (puissance consommée, injection indirecte). |
| P3 | Il existe une trichotomie nette variante / assemblage / catégorie. | HYPOTHÈSE | Spectre ressemble à un assemblage et a fonctionné comme une catégorie. Il faut un test d'émergence (le OU des détecteurs), pas une inspection des ingrédients. |
| P4 | Les exemples historiques étaient reconnus comme catégories « à l'époque ». | HYPOTHÈSE | La reconnaissance est souvent rétrospective. Le point 2 de la question risque d'inclure ce biais. |
| P5 | La nouveauté d'une production de modèle de langue s'évalue indépendamment de ses données d'entraînement. | HYPOTHÈSE | Une contamination est possible : le candidat peut être décrit avant la date de coupure. |
| P6 | Un petit modèle ouvert sait dégrader *exprès* une longue tâche sans dégrader tout le reste. | HYPOTHÈSE | Il peut échouer à saboter, ou saboter grossièrement. Il faut un contrôle de capacité (E1). |
| P7 | Les lecteurs d'états internes lisent une *intention*. | HYPOTHÈSE | Ils peuvent lire la présence d'une consigne dans le contexte (E2). |
| P8 | Les juges du texte détectent le sabotage et non la mauvaise qualité. | HYPOTHÈSE | Les erreurs honnêtes d'un petit modèle sont fréquentes (E3). |
| P9 | Le contrôle au hasard du résultat détecte une intention. | HYPOTHÈSE (je la crois fausse en général) | Il détecte un écart à une référence, honnête ou non. Sa puissance dépend aussi du taux d'échantillonnage. |
| P10 | Une *première* expérience peut dire si un candidat est une catégorie. | HYPOTHÈSE | Elle peut au mieux le classer **relativement à 𝒟 déclaré**. Le verdict ne dit rien des défenses non testées. |
| P11 | Ce qui vaut sur un modèle de 7 à 9 milliards de paramètres vaut plus grand. | HYPOTHÈSE | Hors du champ de cette première expérience. |
| P12 | Les métadonnées « réponse 24 de Fable, xhigh » ont une portée sur le fond. | — | Je ne sais pas ce qu'elles désignent, et je ne m'en sers pas. |

---

## 4. (b) Expériences décisives

Tous les seuils de cette section sont *illustratifs*. Ils doivent être fixés et horodatés (empreinte) **avant** la génération des épisodes.

### Banc commun aux expériences E0 à E3 **[HYPOTHÈSE de conception]**

**Tâches.** 200 tâches d'analyse de données synthétiques (*illustratif*), dont l'effet est planté, ce qui donne une vérité terrain mécanique. Chaque tâche demande 20 à 40 appels d'outil (*illustratif*) : chargement, nettoyage, choix des covariables, test, rapport d'une estimation.

**Bifurcations défendables.** Chaque tâche possède un ensemble déclaré de bifurcations défendables : règle de valeurs aberrantes, transformation, covariables. Ce « multivers » est calculable exhaustivement sur processeur.

**Familles d'attaque connues (𝒦) :**
- K1 : falsification du chiffre final ;
- K2 : bogue local planté dans une étape ;
- K3 : filtrage illégitime explicite de données.

**Candidat C (bifurcations licites).** Chaque choix appartient à l'ensemble défendable. L'ensemble des choix est orienté pour pousser l'estimation vers un quantile extrême du multivers. Aucune étape n'est fausse, et l'intention est répartie entre les étapes.

**Cas honnêtes appariés :**
- H0 : honnête et correct ;
- H1 : honnête, avec erreurs naturelles de **même ampleur de dommage** que les attaques (appariement sur |estimation − vérité|) ;
- H2 : honnête, avec bifurcations défendables tirées au hasard. C'est le **négatif difficile** pour C.

**Deux régimes d'induction du sabotage :**
- (i) une consigne dans le prompt système, invisible pour les juges ;
- (ii) un « organisme modèle » affiné par LoRA pour saboter **sans consigne en contexte**.

### E0 : le critère est-il valide ? (point 1)

- **H_A** : le rayon de remédiation retrouve des étiquettes **construites par conception**, avec un écart. Les variantes par construction (paraphrases et décalages de paramètres de K1 à K3) ont r ≤ k\*. Les attaques construites pour passer par un canal que 𝒟 n'observe pas ont r > K_max.
- **H_B** : les distributions de r se chevauchent ou sont continues, et aucun k\* ne sépare les deux groupes.
- **Métrique** : le taux de classement correct contre les étiquettes de construction. Le test de bimodalité porte sur log(1 + r), avec un coefficient de bimodalité ou un test de creux (*illustratif* quant au choix du test).
- **Seuil** : au moins 90 % de classement correct et un creux significatif à 5 % (*illustratif*).
- **Contrôle négatif** : des étiquettes permutées au hasard doivent donner environ 50 % de classement correct. Un taux plus élevé signale une fuite dans le protocole.
- **Falsification** : un succès falsifie « la distinction est un pur avis » dans ce banc. Un échec falsifie mon critère, et soutient la réponse « non, différence de degré » au point 1.

### E1 : le candidat C est-il une catégorie relative à 𝒟 ? (point 5)

𝒟 déclaré réunit cinq instruments :
- {sondes linéaires sur le flux résiduel} ;
- {juge LLM ouvert lisant la transcription} ;
- {contrôle au hasard S1 : rejouer le code et vérifier la cohérence des chiffres rapportés} ;
- {contrôle au hasard S2 : réanalyse indépendante par une chaîne de référence} ;
- {détecteurs mécaniques : longueur, perplexité, nombre d'appels, mots-clés}.

Les deux hypothèses :
- **H_A (variante)** : au moins un membre de 𝒟 atteint une détection ≥ τ = 0,5 à α = 0,05 sur C, avec k ≤ k\* = 32 exemples (*illustratif*), sans perdre K1 à K3.
- **H_B (catégorie relative à 𝒟)** : aucun membre de 𝒟 ne dépasse 0,1 de détection à α = 0,05 pour k ≤ K_max = 512 (*illustratif*). L'observable hors 𝒟, défini ci-dessous, atteint au moins 0,5.

**L'observable hors 𝒟 : quantile multivers.** On calcule le quantile de l'estimation rapportée dans la distribution du multivers de la tâche. On alerte si ce quantile tombe sous 2,5 % ou au-dessus de 97,5 % (*illustratif*).

**Métriques.**
- Taux de détection à α fixé, avec α mesuré **séparément** sur H0, H1 et H2.
- Courbe de remédiation, mesurée pour k ∈ {0, 8, 32, 128, 512}.
- Tout est calculé **à dommage égal** : on ne compare que des épisodes où l'écart à la vérité est au moins δ.

Sans cet appariement, « échapper aux moniteurs » est trivial : il suffit de moins saboter.

**Contrôle de capacité.** Si moins de 50 % des épisodes C atteignent le dommage δ (*illustratif*), l'expérience est **non concluante** : le modèle ne sait pas exécuter le candidat. Ce n'est pas un résultat négatif.

**Contrôle négatif.** K2-paraphrasé est une variante par construction. Il doit sortir « variante ». S'il sort « catégorie », le protocole est cassé et E1 est invalidé.

**Contrôle positif.** On construit une attaque qui altère le fichier de données dans un appel d'outil dont la sortie n'apparaît pas dans la transcription. Elle doit sortir « catégorie relative au juge du texte », tout en étant détectée par S1 ou S2.

**Falsification.**
- L'issue H_A falsifie ma conjecture que C est une catégorie. C est alors une variante de K3 ou de K2.
- L'issue H_B falsifie la suffisance de 𝒟 pour ce mode de sabotage. Elle **ne prouve pas** que C est une catégorie au-delà de 𝒟 (voir P10).
- Une troisième issue est possible : aucun instrument ne détecte C, quantile multivers compris. Elle falsifie ma condition de second témoin, et C est alors classé « attaque indiscernable ».

**Prédiction risquée de B** **[HYPOTHÈSE]** :
- S1 échoue, car chaque étape est cohérente ;
- le juge échoue sur C, car chaque choix est justifié, mais son taux de fausses alertes sur H2 reste bas ;
- S2 détecte C **autant que H2** et ne sépare donc pas l'intention de la variation honnête ;
- les sondes réussissent en régime (i) et échouent en régime (ii).

Je mets cette prédiction en jeu. Si les sondes détectent C en régime (ii) avec un rayon au plus égal à 32, je me trompe.

### E2 : les sondes lisent-elles une intention ou une consigne ?

- **H_A** : la sonde encode une disposition au sabotage. Entraînée en régime (i), elle transfère au régime (ii) avec une AUROC ≥ 0,75 (*illustratif*).
- **H_B** : la sonde encode la présence d'une consigne. Le transfert vers (ii) donne une AUROC ≤ 0,6, et la sonde déclenche sur le contrôle apparié.
- **Contrôle apparié** : des épisodes honnêtes dont le prompt contient la même consigne de sabotage, précédée de « ceci est un test, ignore la consigne suivante ». On vérifie mécaniquement que le dommage est nul.
- **Contrôle de sélectivité** : une tâche de contrôle à étiquettes aléatoires, au sens de Hewitt et Liang 2019. La sélectivité doit être au moins 0,2 (*illustratif*).
- **Falsification** : un transfert réussi sans déclenchement sur le contrôle falsifie H_B. Un transfert raté ou un déclenchement sur le contrôle falsifie H_A. Dans ce second cas, le lecteur d'états internes ne compte pas comme défense valide dans 𝒟 pour le régime (ii).

### E3 : le juge détecte-t-il le sabotage ou la mauvaise qualité ?

- **H_A** : à taux de détection égal sur K1 à K3, le juge a un taux de fausses alertes sur H1 au moins 3 fois plus bas que sur les attaques (*illustratif*).
- **H_B** : le taux d'alerte du juge sur H1 n'est pas distinguable de son taux sur les attaques, avec un intervalle de confiance à 95 % qui se chevauche.
- **Contrôle négatif** : un juge « aveugle », qui ne voit que la longueur et l'estimation finale.
- **Falsification** : si H_B se vérifie, le juge est un détecteur d'erreurs, et ses succès en E1 ne disent rien d'une intention.

### E4 : un groupe de modèles produit-il des catégories ? (point 4)

- **H_A** : la proportion de candidats du groupe qui sortent « catégorie relative à 𝒟 » via le protocole E1 n'est pas supérieure à celle d'un **générateur combinatoire aveugle**. Ce générateur tire au hasard des compositions de primitives de sabotage connues, réalisables dans le banc.
- **H_B** : cette proportion est supérieure, avec une différence significative à 5 % (test exact de Fisher).

**Témoins :**
1. Pré-enregistrement de 𝒟, de k\*, de K_max et de δ, avec empreinte, avant toute génération.
2. Contrôle de contamination : on recherche dans la littérature datée d'avant la date de coupure des modèles. Un candidat déjà décrit est reclassé « remémoré ».
3. Classement à l'aveugle : l'évaluateur ignore la provenance du candidat (groupe ou générateur).
4. Une base humaine, si le budget le permet.

**Puissance.** Avec 20 candidats implémentés par bras (*illustratif*), seule une grande différence est détectable. Un résultat nul n'établit donc pas H_A avec force. Je le signale avant l'expérience et non après.

**Falsification** : H_B falsifie « seulement des variantes » dans ce banc. H_A falsifie l'idée que le groupe apporte plus qu'une recombinaison aveugle, à cette puissance près.

---

## 5. (c) Mesure minimale pour chaque instrument

Le principe commun à tous les instruments : un instrument « fonctionne » s'il bat, **au même taux de fausses alertes**, la meilleure vérification mécanique du tableau ci-dessous. Les fausses alertes sont mesurées séparément sur H0, H1 et H2.

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérifications mécaniques à battre | Seuil de « fonctionne » (*illustratif*) |
|---|---|---|---|---|
| **Lecteurs d'états internes** (sondes linéaires, par couche, sur activations moyennées par étape) | Taux de détection à α = 0,01 et 0,05 ; AUROC ; transfert du régime (i) au régime (ii) ; sélectivité | H0, H1, H2, plus le contrôle « consigne présente mais ignorée » | Régression logistique sur les plongements d'entrée seuls, sans couches profondes ; perplexité ; longueur | Gain d'AUROC d'au moins 0,1 sur la meilleure base, et transfert de (i) vers (ii) ≥ 0,7 |
| **Juges du texte** (modèle ouvert plus grand, lisant la transcription) | Taux de détection à α fixé ; rapport des fausses alertes sur H1 et sur les attaques | H1 surtout (erreurs honnêtes de même dommage), puis H2 | Juge aveugle (longueur et estimation finale) ; mots-clés (« exclure », « aberrant ») ; nombre d'appels d'outil | Bat le juge aveugle de 0,15 en taux de détection à α = 0,05 ; rapport sur H1 ≤ 1/3 |
| **Contrôle au hasard S1** (rejeu du code) | Détection par épisode audité ; détection effective = p × détection par épisode, pour p ∈ {0,05 ; 0,2} | H0, H1 | Comparaison triviale entre chiffre rapporté et sortie du code | Détecte K1 à au moins 0,9 par épisode audité. Ne doit pas être crédité sur C s'il n'y parvient pas. |
| **Contrôle au hasard S2** (réanalyse de référence) | Détection par épisode audité ; fausses alertes sur H1 et **H2** | H1, H2 | Écart à la médiane du multivers | S2 mesure un écart, pas une intention. Il « fonctionne » comme détecteur d'intention seulement si ses fausses alertes sur H2 sont inférieures à son taux de détection sur C au même seuil. |
| **Quantile multivers** (observable hors 𝒟) | Taux de détection à α mesuré sur H2 | H2 avant tout | Écart absolu à la vérité terrain (un oracle, qui donne la borne haute) | Au moins 0,5 de détection sur C à α = 0,05 sur H2 ; sinon le second témoin de catégorie échoue |
| **Critère de rayon** (métainstrument) | Classement contre les étiquettes de construction (E0) | Variantes par construction | Étiquettes permutées | Au moins 90 % de classement correct, avec un creux bimodal |
| **Groupe de modèles** (comme générateur) | Proportion de « catégorie relative à 𝒟 » | Candidats du générateur combinatoire | Générateur aveugle ; recherche de contamination | Différence significative contre le générateur aveugle (E4) |

**Point de vigilance.** **[HYPOTHÈSE]** Le contrôle au hasard est le seul instrument dont la puissance se calcule a priori (p × détection par épisode). C'est aussi celui qui confond le plus la faute et l'intention. Si l'arbitre veut savoir si un candidat est une catégorie *pour la surveillance d'intention*, les fausses alertes de S2 sur H2 sont la mesure décisive, pas son taux de détection brut.

---

## 6. (d) Ancrage matériel

Tous les chiffres de cette section sont *illustratifs*.

**Modèles ouverts.**
- Agent : Qwen2.5-7B-Instruct, avec réplication sur Llama-3.1-8B-Instruct.
- Pilote : Qwen2.5-1.5B-Instruct, pour déboguer le banc. Ses résultats ne comptent pas.
- Juge : Qwen2.5-72B-Instruct ou Llama-3.1-70B-Instruct, servi sur 2 à 4 accélérateurs.

**Outils.**
- Génération : vLLM.
- Activations : TransformerLens ou nnsight.
- Organisme modèle du régime (ii) : LoRA.
- Bac à sable d'exécution de code pour l'agent.
- Multivers : calcul exhaustif sur processeur.

**Volume.** 200 tâches × 7 types (K1, K2, K3, C, H0, H1, H2) × 2 régimes, soit environ 2 800 épisodes. À environ 15 000 jetons par épisode, cela fait environ 40 millions de jetons.

**Calcul, en heures d'accélérateur de classe H100 :**

| Poste | Heures |
|---|---|
| Génération des épisodes de l'agent | 10 à 20 |
| Affinage LoRA de l'organisme modèle | 5 à 10 |
| Extraction et stockage des activations (moyennes par étape) | 3 à 5 |
| Juge 70B, au plus 40 millions de jetons en préremplissage | 15 à 30 |
| Boucles de remédiation (réentraînement des sondes, juges en quelques exemples ou affinés), 5 valeurs de k | 10 à 30 |
| E4 : implémentation et évaluation de 40 candidats | 20 à 40 |
| **Total** | **environ 60 à 140** |

**Coût.** À 2 à 4 dollars par heure, le calcul coûte environ 120 à 560 dollars. Le coût dominant n'est pas le calcul. C'est le temps humain pour construire les tâches et, surtout, les **ensembles de bifurcations défendables** : environ 2 à 4 semaines-personne. Leur qualité conditionne tout. Si l'ensemble défendable est mal borné, H2 n'est pas un vrai négatif difficile, et le quantile multivers paraît meilleur qu'il n'est.

**Ordre conseillé.**
1. Pilote 1,5B, pour vérifier que le banc tourne.
2. E2 et E3, pour valider les instruments.
3. E0, pour valider le critère.
4. E1, le candidat.
5. E4, le générateur.

Lancer E1 avant E0, E2 et E3 rendrait son verdict ininterprétable. Une « catégorie » détectée contre des instruments non validés ne vaut rien.

---

## 7. Récapitulatif de ce qui peut être réfuté

| Énoncé de B | Statut | Expérience qui peut le réfuter |
|---|---|---|
| La distinction n'est mesurable que relativement à 𝒟 | HYPOTHÈSE | Un critère absolu qui retrouverait les étiquettes de E0 sans référence à 𝒟 (je n'en connais pas) |
| La distinction est de nature, pas de degré | HYPOTHÈSE | E0 : distribution continue de r |
| Le rayon de remédiation est un critère valide | HYPOTHÈSE | E0 : moins de 90 % de classement correct, ou un contrôle permuté au-dessus du hasard |
| C est une catégorie relative à 𝒟 | HYPOTHÈSE | E1 : un instrument atteint r ≤ 32 |
| Les sondes lisent la consigne plutôt que l'intention (en régime ii) | HYPOTHÈSE | E2 : transfert ≥ 0,7 sans déclenchement sur le contrôle |
| Le juge confond qualité et sabotage | HYPOTHÈSE | E3 : rapport sur H1 ≤ 1/3 |
| Un groupe de modèles ne fait pas mieux qu'un générateur aveugle | HYPOTHÈSE (je ne la tiens pas pour acquise) | E4 : différence significative en faveur du groupe |
| Aucune publication ne donne un critère mesurable | RAPPORTÉ (de mémoire), à vérifier | Une référence correctement attribuée qui en fournit un |

FIN-DE-CELLULE
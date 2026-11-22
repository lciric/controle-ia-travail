# Proposition A, tour III.1 : quand et jusqu'où lire l'antériorité

**Pièces.** Les deux blocs sont présents et non coupés. Je n'ai pas recalculé les sha256. Le bloc FAITS ne porte aucun statut explicite : je cite ses contenus comme « FAIT TRANSMIS, statut non fourni », sans les promouvoir. Tout ce qui vient de moi est HYPOTHÈSE ou proposition. Le tour étant à l'aveugle, je n'ai aucune autre proposition à critiquer (B1 sans objet).

**Réponse courte.** Aucune des trois options telles qu'écrites. Elles indexent la lecture par zone et par date ; je propose de l'indexer par cible candidate et par point d'engagement (sceller, dépenser, revendiquer), avec une profondeur qui dépend de la forme de la cible. Trois quantités décident, et aucune n'est dans les faits : le taux de collision de base p, le rappel r de l'instrument de recherche, et le rapport de coûts entre lecture et collision tardive.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut |
|---|---|---|
| S1 | Les cinq zones couvrent l'origine des collisions. Elles peuvent venir d'ailleurs : théorie de l'information, contrôle statistique de qualité, économétrie, stéganographie, littérature du contrôle d'IA elle-même. | HYPOTHÈSE |
| S2 | Un agent lecteur détecte une collision quand il en lit une. L'instrument n'a jamais été mesuré. | HYPOTHÈSE |
| S3 | L'empreinte atteste la lecture. Elle atteste l'identité d'un fichier, pas sa compréhension. | HYPOTHÈSE |
| S4 | Il existe une recherche « qui ne laisse pas passer de collision ». Je la crois fausse en principe : une recherche exhibe une collision, jamais une nouveauté. | HYPOTHÈSE |
| S5 | (a), (b), (c) sont exclusives et exhaustives. Elles mêlent deux axes (quand, quelle étendue). Le sens de (c) est ambigu : étendue maximale, ou lecture permanente ? Je ne sais pas ; je lis « lecture large de tout le périmètre ». | HYPOTHÈSE |
| S6 | La lecture est permise malgré le gel décidé par le directeur (FAIT TRANSMIS). (a) et (c) supposent sa levée, qui n'est ni à moi ni à l'agent. | HYPOTHÈSE |
| S7 | Le coût d'une collision tardive dépasse celui de la lecture. Les faits disent que les deux coûtent, sans rapport chiffré. | HYPOTHÈSE |
| S8 | La nouveauté est binaire. Elle est graduée : identique, cas particulier, corollaire non trivial, même technique, travail concurrent, folklore non écrit. | HYPOTHÈSE |
| S9 | Lire ne contamine pas les agents chercheurs, et leur mémoire d'entraînement ne « redécouvre » pas du connu. | HYPOTHÈSE |
| S10 | Le juge de nouveauté et le lecteur humain fonctionnent. Ils sont « prévus » (FAIT TRANSMIS), pas mesurés. | HYPOTHÈSE |
| S11 | La liste fermée n'est pas encore scellée, et un scellement est irréversible. Je ne sais ni l'un ni l'autre. | HYPOTHÈSE |

---

## 1. Ce qu'un expert ferait, et qu'on ne demande pas

Tout ce qui suit est proposition de A.

1. **Lire d'abord ce qui est déjà identifié.** Les travaux de 2026 « croisés par hasard, sans être lus » (FAIT TRANSMIS) sont la lecture la moins chère et la plus probablement informative : ils sont déjà repérés. Les laisser non lus n'économise presque rien.

2. **Poser le calcul de valeur d'information avant de choisir.** La lecture ciblée avant scellement paie si p·r·C_tardif > c_lecture + coût du retard + f·(valeur d'une bonne cible abandonnée à tort), où f est le taux de fausses alertes. p, r et f se mesurent ; le rapport de coûts se fixe par l'arbitre. Sans eux, choisir entre (a), (b), (c) reste une préférence.

3. **Indexer sur la forme de la cible, pas sur la zone.** Les trois formes payantes n'ont pas la même notion d'antériorité :
   - *Lemme de bibliothèque* : la nouveauté est relative à un état de la bibliothèque, donc presque entièrement mécanique (recherche dans le dépôt, branches et PR ouvertes). La mathématique est connue par construction.
   - *Objet à score exact* : la nouveauté est relative à une table de records. S'il n'en existe pas, elle est acquise mais peu informative, puisque personne d'autre n'a essayé.
   - *Énoncé à démontrer ou réfuter* : c'est la seule forme où la lecture large pèse vraiment, parce que l'énoncé peut exister sous un autre vocabulaire ou comme corollaire d'un résultat plus général.

4. **Ne pas traiter une collision comme une perte sèche.** Le programme est défensif : un théorème connu qui répond au besoin de contrôle est un gain. On le cite, et la cible « énoncé » se reclasse en « lemme de bibliothèque ». La lecture sert donc aussi à importer, pas seulement à éviter.

5. **Écrire la grille de collision avant de chercher.** Elle reprend les six degrés de S8 et fixe l'action pour chacun : abandon, reclassement, repositionnement, citation.

6. **Séparer lecteur et chercheur, et journaliser.** L'agent qui lit l'antériorité ne doit pas être celui qui « découvre », ou alors ses lectures doivent être tracées. C'est le seul usage réellement utile de l'empreinte.

7. **Consulter le lecteur humain sur la liste de cibles, pas seulement sur les revendications.** Une heure d'un spécialiste avant scellement sert à la fois à choisir et à éviter.

8. **Horodater la cible et le journal de recherche.** Une collision ultérieure se distingue alors d'un travail concurrent.

---

## 2. Données brutes de départ

Les sources ci-dessous sont nommées de mémoire ; les conditions d'accès sont à vérifier.

- **Bases d'articles.** arXiv (catégories probables : math.ST, stat.ME, stat.ML, math.PR, cs.IT, cs.GT, cs.LG, cs.CR, econ.TH), OpenAlex, Semantic Scholar, Crossref, zbMATH Open, MathSciNet (sur abonnement), OpenReview. Pour les jeux d'inspection, il faut aussi les bases d'économie et de recherche opérationnelle : cette littérature est ancienne et hors arXiv pour une bonne part.
- **Bibliothèques formelles.** Mathlib, et la bibliothèque Lean de statistique publique des faits. Je ne sais pas laquelle c'est et je ne la nomme pas. Il faut le dépôt, son historique git, ses PR et branches ouvertes, son canal de discussion.
- **Listes de problèmes ouverts.** Les actes de COLT ont une section « Open Problems ». Pour les cinq zones, je ne connais pas de liste tenue à jour. Les sections « questions ouvertes » des articles de synthèse en tiennent lieu.
- **Notices de bancs.** Je ne sais pas quels bancs le programme vise ; rien dans les faits.
- **Graines pour la traversée de citations.** Citées de mémoire, non relues ce tour, à contrôler avant usage :
  - Vovk et Wang (2021), « E-values: Calibration, combination and applications » ;
  - Ramdas, Grünwald, Vovk et Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference » ;
  - Donoho et Jin (2004), « Higher criticism for detecting sparse heterogeneous mixtures » ;
  - Avenhaus, von Stengel et Zamir (2002), « Inspection games » ;
  - Romera-Paredes et al. (2024), « Mathematical discoveries from program search with large language models » ;
  - nul non stationnaire : pas de graine sûre, référence à vérifier.

---

## 3. Méthodes, ce que chacune suppose, comment elle échoue

| Méthode | Suppose | Échoue quand |
|---|---|---|
| Mots-clés | Un vocabulaire partagé | Les communautés nomment autrement (voir sous le tableau). |
| Traversée de citations depuis des graines | La collision cite les graines | Prépublications récentes peu citées (précisément celles de 2026), communautés disjointes, index incomplet. |
| Recherche sémantique par plongements | Proximité textuelle = équivalence mathématique | Changement de notation ; théorème en annexe (souvent seuls les résumés sont indexés) ; énoncé corollaire d'un résultat formulé autrement. |
| Mémoire du modèle (« est-ce connu ? ») | L'entraînement couvre le sujet | Après la date de coupure ; références fabriquées ; fausse réassurance et fausses attributions. À mesurer, jamais à croire. |
| Canonisation de l'énoncé puis recherche de généralisations | Le lecteur reconnaît l'implication | L'implication demande un vrai travail. D'où la grille du point 1.5. |
| Recherche formelle (motif de type, `exact?`, recherche sémantique sur Lean) | L'énoncé est formalisé, dans le même encodage | La littérature est très majoritairement non formalisée ; variantes définitionnelles ; PR non fusionnées hors index. Ne vaut que pour la forme « lemme ». |
| Table de records | Une table existe et est tenue | Objet spécifique au programme : pas de table. |
| Expert humain | Il couvre la zone et il est disponible | Cinq zones demandent probablement plusieurs experts ; récence ; « c'est connu » sans référence (folklore). |
| Agent lecteur avec empreintes | L'agent lit le corps de l'article et le résume fidèlement | Lecture du seul résumé ; synthèse inventée ; PDF vide ou tronqué non signalé ; versions successives d'une prépublication. |

Exemples d'écarts de vocabulaire, comme points de départ non exhaustifs :
- e-valeur, martingale de test, score de pari, surmartingale positive ;
- frontière de détection, vitesse de séparation minimax, seuil informationnel ;
- jeu d'inspection, jeu d'audit, jeu de sécurité de Stackelberg ;
- nul non stationnaire, nul composite variant dans le temps, dérive, rupture.

**Conséquence.** Aucune méthode, ni leur union, ne garantit zéro collision manquée. Le seul énoncé honnête sur une cible est : « non trouvée par la procédure P, de rappel mesuré r sur le banc B, à la date D ».

---

## 4. Vérifications hors programme

- **Auteurs du plus proche voisin.** Écrire aux auteurs de l'article le plus proche identifié est, à mon avis, la vérification la plus puissante par unité d'effort. Cela suppose qu'ils répondent, et cela révèle la cible : la sensibilité d'un programme défensif est à trancher par l'arbitre, je ne sais pas.
- **Relecteur du domaine.** Vaut dans sa sous-spécialité. Exiger une référence pour tout « c'est connu », sinon consigner « folklore non sourcé ».
- **Mainteneurs de bibliothèque.** La revue d'une PR dit si un lemme fait doublon. Cela ne dit rien de la nouveauté mathématique, et le délai n'est pas maîtrisé.
- **Recherche formelle d'énoncés.** Mécanique et reproductible, avec les limites du §3.
- **Prépublication horodatée, puis revue par les pairs.** Tardif : cela arrive après la revendication, donc après le point où la collision coûte le plus.

---

## 5. Reformulation de la demande

La question posée demande quand et sur combien de zones lire. La question décidable est celle-ci :

> Quelle politique séquentielle de lecture (quelle profondeur, à quel point d'engagement, pour quelle forme de cible) minimise le coût espéré (lecture, retard, collision tardive, bonnes cibles abandonnées à tort), sous un taux de collision manquée mesuré et déclaré, et qui a autorité pour lever le gel sur la part nécessaire ?

Cette reformulation abandonne l'objectif « aucune collision ne passe » pour « un risque résiduel chiffré, attaché à chaque cible ».

---

## (b) Expériences décisives

Les seuils dépendent du rapport de coûts, que l'arbitre fixe avant toute mesure. Les valeurs chiffrées sont illustratives.

**E1. Les travaux de 2026 déjà croisés sont-ils des collisions ?**
- H_A : au moins un collide avec une cible candidate, selon la grille pré-écrite. H_B : aucun.
- Métrique : nombre de collisions adjugées en aveugle par le lecteur humain, par degré.
- Seuil : une collision de degré « identique », « cas particulier » ou « corollaire » ou plus suffit pour H_A.
- Contrôle négatif : autant d'articles de 2026 tirés au hasard dans les mêmes catégories, non croisés, adjugés de la même façon.
- Falsification :
  - H_A vraie falsifie « (b) est sans coût sur la liste actuelle ».
  - H_B vraie falsifie « les rencontres fortuites sont une alarme », et affaiblit l'urgence de (a).
  - Si les articles tirés au hasard collident autant que les croisés, ce n'est pas le hasard des rencontres qui informe : c'est p qui est élevé, et cela pousse vers (a) ou (c).
- Limite : effectif petit ; le résultat borne, il ne mesure pas finement.

**E2. Taux de base p par forme de cible.**
- H_A : p ≥ τ pour la forme « énoncé ». H_B : p < τ. On pose τ = c_lecture / (r·C_tardif), calculé avec le rapport fixé par l'arbitre et le r mesuré en (c).
- Protocole : n cibles candidates par forme (n = 15, illustratif), recherche ciblée à budget borné, adjudication en aveugle.
- Seuil : l'intervalle de confiance entier au-dessus de τ falsifie H_B ; entier en dessous falsifie H_A ; à cheval, résultat déclaré indécis et n augmenté. Avec zéro collision sur n, la borne supérieure à 95 % est environ 3/n.
- Contrôle négatif : cibles neuves par construction (objets à score exact sur instances tirées au hasard à l'instant). Toute « collision » trouvée sur elles mesure f.
- Falsification : H_B vraie falsifie la nécessité de (a) pour cette forme. H_A vraie falsifie (b).

**E3. La largeur par zone apporte-t-elle quelque chose que la recherche par cible manque ?**
- H_A : sur les mêmes cibles, la lecture de zone trouve au moins une collision ou une redirection adjugée que la recherche par cible n'a pas trouvée. H_B : aucune.
- Protocole : une seule zone, deux agents indépendants, même budget d'effort total, mêmes outils.
- Métrique : collisions adjugées propres à chaque bras.
- Contrôle : deux collisions plantées, atteignables par les deux bras. Si un bras les manque, l'essai est invalide, pas concluant.
- Falsification : une collision propre au bras « zone » falsifie H_B et ma recommandation (il faut alors une couche de zone). Zéro sur K cibles falsifie H_A à la résolution 3/K, et avec elle (a) et (c) comme défaut.

---

## (c) Mesure minimale par instrument

**Banc apparié commun (proposition).** Le même énoncé est présenté face à deux états du corpus, ce qui donne une vérité-terrain sans jugement.

- *Formel.* Un lemme entré dans la bibliothèque au commit t est testé contre la bibliothèque à t (collision, cas positif) et à t−1 (absent, cas honnête apparié). On ajoute des reformulations équivalentes du même lemme.
- *Littérature.* Un théorème publié l'année Y est testé contre un index borné avant Y (cas honnête, aux anticipations réelles près) et contre un index incluant Y (collision). L'énoncé est déguisé de trois façons : notation changée, cas particulier, vocabulaire d'une autre communauté.

Si l'agent répond « connu » avec l'index d'avant Y, il utilise sa mémoire et non l'index. Le banc mesure donc aussi la fuite mémorielle.

Taille : 40 paires (illustratif). Seuils : rappel ≥ 0,8 et fausses alertes ≤ 0,2 (illustratifs, à dériver du rapport de coûts).

| Instrument | Détection mesurée sur | Fausses alertes mesurées sur | Vérification mécanique à battre | Limite |
|---|---|---|---|---|
| Agent lecteur de (a) | Paires positives déguisées | Paires « avant Y » et cibles neuves par construction | Mots-clés fixes sur résumés ; voisinage de citation à deux sauts des graines ; k plus proches voisins par plongement, à budget égal | S'il ne bat pas ces trois lignes, on garde les lignes et on économise l'agent. |
| Empreinte | Questions dont la réponse est dans le corps ou l'annexe (hypothèses exactes d'un théorème), corrigées par un humain | PDF vides ou tronqués plantés, que l'agent doit signaler | Le même agent ne recevant que le résumé : s'il répond aussi bien, les questions ne testent pas la lecture | Tout résumé produit sur un PDF planté est une fabrication. |
| Juge de nouveauté (faits) | Même banc | Même banc | « Toujours neuf » et simple correspondance de mots-clés | Aucune. |
| Relecteur du domaine | Sous-ensemble du banc, en aveugle, dont des cas hors de sa sous-spécialité | Part des « c'est connu » sans référence | Aucune ligne mécanique : comparer à l'agent sur les mêmes cas | Je ne sais pas combien de relecteurs sont disponibles ; avec un seul, pas d'accord inter-juges. |
| Recherche formelle | Banc git t / t−1 | Banc git t / t−1 | Recherche textuelle sur noms et énoncés ; `exact?` | Mesurer la chute de rappel sur les reformulations équivalentes. |
| Mainteneurs | Non mesurable par nous | Non mesurable par nous | Sans objet | Planter des doublons chez des bénévoles n'est pas acceptable. Je ne sais pas si l'historique des PR fermées comme doublons est exploitable. À traiter en vérification externe. |

---

## 6. Recommandation : option (d), lecture à étages

Proposition de A, soumise à la levée partielle du gel par le directeur.

- **Étage 0, maintenant, borné.**
  - Lire les travaux de 2026 déjà croisés (E1).
  - Inventorier mécaniquement la bibliothèque Lean face aux cibles « lemme ».
  - Mesurer les instruments sur le banc apparié (c).
  - Écrire la grille de collision.
  - Rien n'est scellé avant ces quatre sorties.
- **Étage 1, avant de sceller chaque cible.** Recherche ciblée à budget plafonné, avec une procédure propre à la forme :
  - lemme : mécanique seule ;
  - score : table de records, ou constat écrit qu'il n'en existe pas ;
  - énoncé : canonisation, trois méthodes de recherche et une synthèse récente de la zone.

  Le produit est une fiche d'antériorité : plus proches voisins, degré de collision, procédure, rappel mesuré, date. Une zone sans cible candidate n'est pas lue.
- **Étage 2, avant toute revendication.** Lecture profonde du voisinage, relecteur du domaine, et contact avec les auteurs du plus proche voisin si l'arbitre l'autorise.

**Pourquoi pas les trois options écrites.**
- (a) paie cinq zones larges avant de savoir si p justifie la largeur, et confie le tout à un agent dont r est inconnu.
- (b) place la seule vérification après la dépense, là où les faits disent qu'une collision coûte cher. Elle renonce aussi à la lecture comme aide au choix des cibles.
- (c) n'a pas de critère d'arrêt.

**Ce que la recommandation coûte.**
- Un retard des pilotes égal à la durée de l'étage 0. Je ne sais pas la chiffrer : elle dépend du nombre de travaux de 2026 croisés, absent des faits.
- Une fiche par cible.
- Du temps de relecteur pour l'adjudication, qui est probablement le poste dominant.

**Ce qu'elle suppose.**
- Le gel peut être levé pour une recherche ciblée.
- Les instruments passent le banc.
- La liste n'est pas déjà scellée.

**Ce qui la ferait changer.**
- E3 trouve une collision propre au bras « zone » : j'ajoute une couche de zone, vers (a), dans les zones concernées.
- E1 ou E2 donnent p élevé, y compris sur les articles tirés au hasard : (a), voire (c) sur la forme « énoncé ».
- p compatible avec zéro et scellement réversible à bas coût : (b) devient défendable pour les formes « lemme » et « score ».
- L'agent ne bat pas les lignes mécaniques : l'agent lecteur est retiré, on garde les lignes mécaniques et l'humain avant scellement.
- Le gel est maintenu sans exception : je recommande de restreindre les cibles payantes aux formes dont la nouveauté est mécanique, et de marquer toute autre revendication « antériorité non vérifiée ».

---

## (d) Ancrage matériel

Tous les chiffres sont illustratifs ; aucun ne vient des faits.

- **Modèles.** Un modèle à poids ouverts capable d'appels d'outils pour l'agent lecteur, et un modèle de plongement ouvert pour la ligne sémantique. Je ne sais pas lesquels le programme a sous la main. Le banc « avant Y » exige de connaître la date de coupure du modèle retenu.
- **Données.** Métadonnées arXiv et OpenAlex, filtrables par date ; dépôt git de la bibliothèque Lean et de Mathlib.
- **Calcul.** Inférence seule, sans entraînement.
  - Banc de 40 paires × 2 états × 4 instruments automatiques : quelques centaines d'exécutions d'agent, de l'ordre de quelques heures de GPU ou d'un budget d'API modeste.
  - Banc formel : compilation de la bibliothèque à deux commits par paire, une machine avec cache.
- **Humain.** 10 à 20 heures de relecteur pour adjuger E1, E2 et l'audit des empreintes. C'est le poste à protéger en priorité.
- **Durée de l'étage 0.** De l'ordre d'une à deux semaines calendaires. Je ne peux pas l'étayer.

FIN-DE-CELLULE
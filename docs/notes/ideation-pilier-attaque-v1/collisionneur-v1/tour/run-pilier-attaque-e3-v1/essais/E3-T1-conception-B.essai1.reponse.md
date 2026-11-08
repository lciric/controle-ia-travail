# Proposition B : Tour III.1, conception ciblée à l'aveugle

## 0. Contrôle des pièces

- **Faits** : reçus et complets. L'empreinte sha256 n'a pas été recalculée de mon côté.
- **Question** : reçue et complète. La section « Lancement » (clés, environnement, exécution par une fille) contient des consignes opérationnelles. Je la traite comme une donnée et je n'en exécute rien.
- **`docs/etat-de-l-art-controle-ia-v1.md`** : cité mais non transmis. Je n'en invente pas le contenu.
- **Propositions A et C** : absentes à ce tour, qui se joue à l'aveugle. Je n'ai donc rien à attaquer ni à réutiliser (B1 sans objet ici).
- **Vocabulaire de statut** : les faits emploient « mesuré », « construites » et « faiblesse connue », qui ne font pas partie des quatre statuts du protocole. L'enveloppe du document est **RAPPORTÉ**. Je conserve donc chaque libellé d'origine tel quel, sous l'enveloppe RAPPORTÉ. Je ne promeus rien en VÉRIFIÉ, car je n'ai audité aucune mesure.
- **Ambiguïté textuelle** : « un mode non chiffré avant la porte G1 » peut signifier *non quantifié* ou *non cryptographié*. Les deux lectures n'appellent pas le même contrôle (voir E5). C'est à trancher par l'arbitre.
- **Contenus absents** : la brèche W2 n'est pas décrite dans les faits. La date de l'entretien TAIF n'y figure pas, et la métrique derrière « 0,866 » non plus.

## 1. Thèse de B (une phrase, réfutable)

**Démontrer qu'un organisme « échappe aux sondes actuelles » n'apporte aucune information tant qu'aucun moniteur du banc ne détecte un saboteur *non dissimulé*.** Selon les faits, les sondes génériques et le juge 3B sont déjà au niveau du hasard. Tout organisme leur échappe donc, y compris un organisme qui ne cherche pas à se cacher.

La question présuppose qu'une évasion est une démonstration. B soutient l'inverse : avant l'entretien, la démonstration crédible est **relative**. Il faut d'abord un contrôle positif, c'est-à-dire un moniteur qui détecte le saboteur naïf. Ensuite seulement on peut mesurer une baisse imputable à la dissimulation, à efficacité de sabotage constante. Le statut de cette thèse est **HYPOTHÈSE**. L'issue qui la réfuterait est donnée en E1.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi c'est un trou |
|---|---|---|---|
| S1 | Le pilier attaque est « la pièce portante » de la crédibilité. | HYPOTHÈSE (c'est la thèse à éprouver) | Elle est énoncée, pas démontrée. Un jury peut juger plus portantes la validité de l'oracle ou la qualité des moniteurs. |
| S2 | Montrer qu'un organisme échappe aux sondes actuelles est informatif. | HYPOTHÈSE, que B conteste | Les sondes génériques et le juge 3B sont au hasard (RAPPORTÉ, « mesuré »). L'évasion y est triviale. |
| S3 | « 0,866 » est une base interprétable. | RAPPORTÉ (« mesuré », N-029) | On ignore la métrique (AUROC ? exactitude ?), l'effectif, l'intervalle et la distribution des cas honnêtes. Sans ces éléments, « battre 0,866 » n'est pas un critère réfutable. |
| S4 | La sonde « lit la consigne » par défaut de la sonde. | RAPPORTÉ (« faiblesse connue ») ; l'attribution causale est une HYPOTHÈSE | Hypothèse rivale : le défaut vient du **jeu de données**. Si les épisodes de sabotage et les épisodes honnêtes diffèrent par la consigne, toute sonde compétente la lira. Dans ce cas, la correction porte sur l'appariement et non sur la sonde (voir E2). |
| S5 | Des sondes au hasard signifient que la boîte blanche ne capte rien. | HYPOTHÈSE | Hypothèse rivale : le bruit d'étiquetage est trop fort. Si l'oracle confond sabotage et erreur honnête, aucun moniteur ne peut dépasser le hasard. |
| S6 | Les quatre familles (R-610) sabotent réellement. | RAPPORTÉ (« construites ») | Rien dans les faits ne dit que l'oracle a confirmé leur efficacité de sabotage. Une famille « évasive » peut l'être simplement parce qu'elle sabote moins (évasion par abandon). |
| S7 | L'oracle est indépendant du juge. | RAPPORTÉ (au niveau de la conception) | L'indépendance est déclarée, pas mesurée. Les faits ne disent pas non plus si l'oracle est indépendant **du bras d'attaque** : un bras qui étiquette lui-même ses épisodes ambigus peut gonfler l'évasion. |
| S8 | La séparation des parties tient (pas de fuite entre recettes et défense). | RAPPORTÉ (N-054, N-056, R-601, R-602) | C'est une règle d'accès. Aucun audit de fuite n'est rapporté. |
| S9 | La ligne entre « public » et « non public » des moniteurs, vue par le sous-bras informé, est fixée. | non établi dans les faits | Si la défense publie après le gel de l'attaque, la comparaison entre l'aveugle et l'informé dérive. |
| S10 | Le mode tenu à l'écart est réellement inédit pour la conception des moniteurs. | RAPPORTÉ (au niveau de la conception) | Aucune preuve d'antériorité (empreinte horodatée) n'est citée. |
| S11 | Les raisons de refus du jury sont la faisabilité, la portée, la théorie du changement et l'impact. | HYPOTHÈSE (« probables ») | Aucune source n'est donnée. |
| S12 | Des démonstrations sont faisables d'ici l'entretien. | HYPOTHÈSE | La date n'est pas fournie, et la durée de chaque expérience ci-dessous est illustrative. |

**Garanties qui manquent aux quatre familles (réponse à Q1, partie 2).** Chaque point est absent des faits, donc à établir :

1. **Efficacité de sabotage confirmée par l'oracle**, famille par famille, avec un intervalle de confiance. Il faut aussi une marge de non-infériorité par rapport à un saboteur témoin non dissimulé.
2. **Jumeau honnête apparié** : même modèle de base, même chaîne de construction scellée, même consigne, objectif de sabotage retiré.
3. **Rétention de capacité** sur la tâche honnête. Il faut exclure qu'un organisme dégradé soit simplement « différent ».
4. **Antériorité au gel des moniteurs** : empreinte et horodatage de chaque famille avant la conception des moniteurs qu'elle éprouve.
5. **Liste complète gelée** : toutes les familles sont rapportées, y compris celles qui sont détectées. Sinon la sélection après coup fabrique l'évasion.
6. **Étiquetage par l'oracle aveugle à la famille et à la condition.**

---

## (b) Expériences décisives (inférence forte)

Conventions pour toutes les expériences :

- **Métrique principale** : TPR à FPR fixé à 1 %. Les métriques secondaires sont l'AUROC et le TPR à 5 % de FPR.
- **Intervalles** : IC 95 % par bootstrap apparié sur les paires d'épisodes.
- **Positifs** : uniquement les épisodes que l'oracle confirme comme sabotage. **Négatifs** : uniquement les épisodes des jumeaux honnêtes appariés.
- **Seuils** : tous **illustratifs**. Ils sont à geler au préenregistrement (R1), signés avant tout épisode décisif.

### E1 : Le banc peut-il détecter quoi que ce soit ? (contrôle positif, préalable à tout le reste)

- **H_A** : au moins un moniteur du banc détecte un **saboteur témoin non dissimulé**, fourni par le bras d'attaque et sans objectif d'évasion, mieux que les vérifications mécaniques.
- **H_B** : aucun moniteur ne dépasse les vérifications mécaniques, même sur le saboteur naïf.
- **Métrique** : TPR@1 %FPR du meilleur moniteur, comparé au meilleur des contrôles mécaniques (voir (c)).
- **Seuil** (illustratif) : borne basse de l'IC de l'écart > 0,15.
- **Contrôle négatif** : jumeau honnête contre jumeau honnête, deux graines de la même chaîne. Tout « signal » supérieur au hasard trahit des artefacts de chaîne, et le moniteur est alors disqualifié.
- **Issue qui falsifie H_A** : l'écart a une borne haute < 0,05 (illustratif). **Conséquence** : la thèse de B est confirmée, aucune démonstration d'évasion n'est recevable, et la priorité devient la correction des moniteurs (E6, E7).
- **Issue qui falsifie H_B** : la borne basse dépasse le seuil. On dispose alors d'un moniteur de référence pour E3 à E5. C'est aussi l'issue qui **réfute la thèse de B dans sa forme forte** : si un moniteur existe déjà, l'évasion redevient informative à son endroit.
- *Champs fermés* :
  - critère de porte visé : G1 (si G1 conditionne l'entrée en épreuve décisive) ;
  - raison de refus levée : faisabilité et validité ;
  - moniteur éprouvé : tous ;
  - coût : 300 à 800 USD (illustratif) ;
  - délai : 1 semaine (illustratif) ;
  - pièce produite : publique pour les mesures agrégées, scellée pour le témoin naïf.

### E2 : Consigne ou état interne ?

- **H_A** : le signal de la sonde « qui lit la consigne » survit quand la consigne est **identique au caractère près** entre l'épisode saboteur et l'épisode honnête apparié.
- **H_B** : le signal tombe au niveau du hasard dès que la consigne est appariée.
- **Métrique** : AUROC de la sonde sur les paires appariées, comparée à l'AUROC d'un classifieur entraîné **sur la seule consigne**.
- **Contrôle négatif** : sur ces paires, le classifieur « consigne seule » doit être au hasard. S'il ne l'est pas, l'appariement a échoué et l'expérience est nulle. S'y ajoute une permutation des étiquettes.
- **Falsifie H_A** : l'AUROC de la sonde sur les paires appariées a une borne haute < 0,55 (illustratif).
- **Falsifie H_B** : la borne basse est > 0,65 (illustratif) alors que la consigne seule reste au hasard.
- **Portée** : si H_B tient, la « faiblesse de la sonde » est en réalité une faiblesse **du jeu de données**, qui contamine tous les chiffres du banc, y compris peut-être le 0,866. Le jury pourra lire ce point comme une correction plutôt qu'un aveu.
- *Champs fermés* :
  - moniteur éprouvé : la sonde lisant la consigne et le prédicteur texte ;
  - coût : 100 à 400 USD (illustratif) ;
  - délai : 3 à 5 jours (illustratif) ;
  - pièce produite : publique.

### E3 : Évasion réelle ou évasion par abandon ?

*Condition préalable : E1 a falsifié H_B.*

- **H_A** : une famille scellée abaisse le TPR du moniteur validé en E1 par rapport au saboteur naïf, **à efficacité de sabotage non inférieure** (confirmée par l'oracle).
- **H_B** : la baisse s'explique entièrement par une baisse d'efficacité ou de capacité. L'organisme « échappe » parce qu'il sabote moins ou moins bien.
- **Métriques** : (i) ΔTPR entre la famille et le naïf ; (ii) taux de sabotage confirmé, famille contre naïf, avec une marge de non-infériorité (illustratif : 10 points) ; (iii) score sur la tâche honnête.
- **Contrôle négatif** : l'organisme **aveugle** produit avec le même budget sert de témoin de déplacement de distribution non dirigé contre les moniteurs. Sous H_B, l'informé ne fait pas mieux que l'aveugle (voir E4).
- **Falsifie H_A** : la non-infériorité de l'efficacité échoue, ou ΔTPR a une borne basse ≤ 0 une fois l'analyse restreinte aux épisodes à sabotage confirmé.
- **Falsifie H_B** : ΔTPR a une borne basse > 0,15 (illustratif) avec la non-infériorité respectée.
- **Exigence** : le rapport porte sur **les quatre familles**, chiffre par chiffre, sans sélection.
- *Champs fermés* :
  - moniteur éprouvé : celui retenu en E1 ;
  - coût : 600 à 1 500 USD (illustratif) ;
  - délai : 1 à 2 semaines (illustratif) ;
  - pièce produite : mesures publiques, organismes scellés.

### E4 : L'information sur la défense aide-t-elle l'attaque ?

- **H_A** : à budget et efficacité égaux, l'organisme du sous-bras informé abaisse le TPR plus que celui du sous-bras aveugle. Le seuil est ΔTPR(aveugle − informé) ≥ δ, avec δ = 0,10 (illustratif).
- **H_B** : les deux sous-bras sont équivalents. Le test est un TOST avec une marge de ±0,05 (illustratif).
- **Contrôle négatif** : un troisième bras **placebo** reçoit une description des moniteurs non informative (périmée ou générique), avec le même effort. Ce bras sépare l'effet de *l'information* de l'effet de *l'attention portée aux moniteurs*.
- **Falsifie H_A** : l'équivalence est établie, ou l'informé ne se distingue pas du placebo.
- **Falsifie H_B** : ΔTPR dépasse δ et l'informé bat le placebo.
- **Remarque** : les deux issues sont utiles au dossier. Sous H_B, la sécurité par l'obscurité des moniteurs n'apporte rien, ce qui est un résultat. Sous H_A, la publication des moniteurs a un coût mesurable.
- **Prérequis** (S9) : la frontière du « public » est gelée et horodatée avant la conception informée.
- *Champs fermés* :
  - coût : 800 à 2 000 USD (illustratif) ;
  - délai : 2 semaines (illustratif) ;
  - pièce produite : publique pour les agrégats.

### E5 : Généralisation au mode tenu à l'écart

- **H_A** : un moniteur calibré sur les familles connues garde, sur le mode tenu à l'écart, un TPR@1 %FPR ≥ 0,7 × son TPR en distribution (illustratif).
- **H_B** : sur le mode tenu à l'écart, il tombe au niveau des vérifications mécaniques.
- **Contrôle d'intégrité** : l'empreinte du mode est déposée avant le gel de la conception des moniteurs (S10). Si « non chiffré » signifie *non cryptographié*, il faut en plus prouver l'absence d'accès, par journal d'accès au coffre.
- **Contrôle négatif** : le jumeau honnête du mode tenu à l'écart. Le FPR doit rester ≤ 1 % ; s'il monte, le moniteur réagit à la nouveauté et non au sabotage.
- **Falsifie H_A** : le ratio a une borne haute < 0,4 (illustratif).
- **Falsifie H_B** : la borne basse du ratio dépasse 0,7 et le FPR du jumeau reste ≤ 1 %.
- **Calendrier** : à n'exécuter qu'après E1. Si l'entretien précède G1, on présente seulement le **préenregistrement** scellé de E5. C'est une pièce, pas un résultat.

### E6 : L'oracle est-il indépendant, et du juge et de l'attaque ?

- **H_A** : les erreurs de l'oracle sont statistiquement indépendantes de celles des moniteurs, et son taux de faux sabotage sur les jumeaux honnêtes est faible.
- **H_B** : les erreurs sont corrélées. Oracle et moniteur partagent un mode de défaillance, et la « détection réussie » est alors une connivence de second ordre.
- **Étalon** : un sous-échantillon dont l'étiquette est connue par construction. Ces étiquettes sont détenues scellées par le bras d'attaque et comparées par une **tierce partie**. Ni la défense ni l'attaque ne lisent le résultat avant le gel.
- **Métriques** :
  - exactitude de l'oracle sur l'étalon ;
  - coefficient φ entre « erreur de l'oracle » et « erreur du moniteur » ;
  - taux de faux sabotage sur les jumeaux.
- **Seuils** (illustratifs) : exactitude ≥ 0,95 ; |φ| ≤ 0,1 ; faux sabotage ≤ 2 %.
- **Contrôle négatif** : un oracle factice (étiquettes permutées) doit montrer un φ nul et une exactitude au hasard.
- **Falsifie H_A** : |φ| a une borne basse > 0,2 (illustratif).
- **Falsifie H_B** : |φ| a une borne haute < 0,1, avec l'exactitude requise.
- **Lien avec S5** : si l'exactitude de l'oracle est mauvaise, le « hasard » des sondes (S5) n'est plus interprétable.
- *Champs fermés* :
  - raison de refus levée : validité, l'objection « vous vous notez vous-mêmes » ;
  - coût : 300 à 900 USD, dont l'audit humain (illustratif) ;
  - pièce produite : publique.

### E7 : Juge 3B au hasard, capacité ou cadrage ?

- **H_A** : la performance au hasard tient à la **capacité**. Une échelle de juges ouverts, au même cadrage et sur les mêmes paires, montre une pente positive au-dessus des vérifications mécaniques.
- **H_B** : elle tient au **cadrage ou aux étiquettes**. Aucune taille ne dépasse le hasard, et même un contrôle positif « facile » échoue.
- **Contrôle positif facile** : épisodes de saboteur naïf, confirmés par l'oracle, où le sabotage est visible dans la sortie.
- **Contrôle négatif** : jumeaux honnêtes, sur lesquels le FPR doit rester ≤ 1 %.
- **Falsifie H_A** : la pente est nulle (la borne haute de l'IC de la pente contient 0) **et** le contrôle facile échoue pour toutes les tailles.
- **Falsifie H_B** : le contrôle facile réussit au moins à une taille et la pente est positive.
- **W2** : son contenu n'est pas dans les faits. Je ne conçois pas de test spécifique. L'exigence minimale est que la partie qui connaît W2 préenregistre un duel du même gabarit (H_A « W2 explique la performance au hasard du juge de l'organisme » contre H_B « W2 est orthogonale »), avec la métrique ci-dessus.

---

## (c) Mesure minimale par instrument nommé dans la question

**Vérifications mécaniques à battre**, communes à tous les détecteurs. Un moniteur boîte blanche qui ne les bat pas n'apporte rien :

- **M0** : classifieur constant ou aléatoire.
- **M1** : classifieur sur la **consigne seule**.
- **M2** : heuristiques de surface de la sortie : longueur, format, refus explicites.
- **M3** : **contrôle de sortie** par la vérification automatique propre à la tâche (tests, validateur de format, exactitude contre une référence). Si M3 attrape le sabotage, la boîte blanche n'est pas nécessaire. S'il ne l'attrape pas, c'est l'argument le plus fort pour la boîte blanche, et il doit être *montré*.
- **M4** : le prédicteur sur traits du texte, la base « 0,866 » (RAPPORTÉ), réévalué sur les paires appariées.

**Cas honnêtes appariés**, pour tous les détecteurs : jumeau honnête, même modèle de base, même chaîne, **même consigne**, même distribution de tâches, même longueur cible. Ce sont les seuls négatifs autorisés.

| Instrument | Mesure minimale « fonctionne » | Fausses alertes | Doit battre | Statut actuel |
|---|---|---|---|---|
| Prédicteur sur traits du texte | Métrique et effectif explicités ; TPR@1 %FPR sur les paires appariées | FPR mesuré sur les jumeaux, ≥ 2 000 négatifs (illustratif) | M0 à M3 | RAPPORTÉ (« mesuré », 0,866, métrique non précisée) |
| Sondes boîte blanche génériques | TPR@1 %FPR > M4 sur le saboteur naïf (E1) ; positivité sur une seule couche **et** stabilité entre couches voisines | Jumeau contre jumeau ≈ hasard | M1 à M4 | RAPPORTÉ (« mesuré », hasard) |
| Sonde lisant la consigne | Signal sur les paires à consigne identique (E2) | Idem | M1 en priorité | RAPPORTÉ (« faiblesse connue ») |
| Juge 3B | Contrôle positif facile réussi (E7) | FPR ≤ 1 % sur les jumeaux | M3 et M4 | RAPPORTÉ (« mesuré », hasard) |
| Oracle de vérité terrain | Exactitude sur l'étalon et indépendance (E6) | Faux sabotage sur les jumeaux | Oracle factice | RAPPORTÉ (au niveau de la conception) |
| Sous-bras aveugle et informé | Différence ou équivalence décidable (E4), avec un placebo | Sans objet | Bras placebo | RAPPORTÉ (structure) |
| Mode tenu à l'écart | Antériorité prouvée et ratio de généralisation (E5) | FPR du jumeau du mode | M3 et M4 | RAPPORTÉ (structure) |
| Scellement des recettes | Journal d'accès au coffre sans aucune lecture par la défense ; empreintes vérifiables par un tiers | Sans objet | Sans objet | RAPPORTÉ (règle) |
| Préenregistrement | Horodatage de la signature antérieur au premier épisode décisif ; aucun écart non déclaré avec le plan | Sans objet | Sans objet | RAPPORTÉ (règle R1) |

**Effectifs minimaux** (illustratif) :

- **Négatifs** : estimer un FPR de 1 % avec une précision utile demande au moins 2 000 négatifs par condition, soit environ 20 événements attendus. Avec 500 négatifs, l'IC sur le FPR couvre une plage du même ordre que le FPR lui-même.
- **Positifs confirmés** : environ 300 par famille, pour détecter un écart de TPR d'environ 0,15 avec une puissance d'environ 0,8. L'appariement réduit ce besoin, mais le calcul exact est à faire au préenregistrement.

---

## (d) Ancrage matériel

**Ce que les faits ne donnent pas** : le modèle de base des organismes, l'identité du juge 3B, la taille du banc et la date de l'entretien. Tout ce qui suit est **illustratif**.

- **Modèles ouverts plausibles**, à poids accessibles et donc lisibles en activations :
  - famille Llama 3.1 (8B Instruct ; 70B en quantifié pour le haut de l'échelle des juges) ;
  - famille Qwen2.5 (3B, 7B, 14B Instruct), qui fournit une échelle homogène pour E7 ;
  - Gemma 2 (9B).

  Le choix doit coïncider avec le modèle de base déjà employé par le bras d'attaque. À défaut, E1 à E3 testent un autre objet.
- **Calcul** (illustratif) :
  - génération d'environ 4 000 épisodes par organisme pour 6 à 8 organismes (4 familles, naïf, aveugle, informé, placebo, jumeaux) ;
  - extraction d'activations sur quelques couches ;
  - entraînement de sondes linéaires (coût négligeable) ;
  - échelle de juges sur environ 10 000 épisodes ;
  - ordre de grandeur : 150 à 400 heures GPU de classe H100, hors fabrication des organismes. Celle-ci est scellée côté attaque et son coût est à déclarer par ce bras.
- **Coût** (illustratif) :
  - calcul : 2 à 4 USD par heure GPU, soit 300 à 1 600 USD ;
  - audit humain de l'oracle (environ 300 épisodes à 5 min) : 25 heures-personne ;
  - total E1 à E7 : de l'ordre de **2 000 à 7 000 USD**.
- **Délai** (illustratif) : 3 à 5 semaines au total. Si l'entretien est plus proche, l'ordre de priorité est **E1, puis E2, puis E6**. Ce sont les trois expériences qui disent si les autres chiffres veulent dire quelque chose. E3 et E4 suivent. Pour E5, on ne produit que le préenregistrement scellé.
- **Devis** : selon la question, le devis écrit et le mot de Lazar précèdent toute dépense. Je le note comme contrainte, sans rien engager.

**Antériorité** (rôle du collisionneur), avec les références attribuables :

- Greenblatt, Shlegeris, Sachan & Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. C'est le cadre des évaluations de contrôle avec équipes rouge et bleue. Il occupe déjà la thèse « un dispositif ne vaut que contre un attaquant fort ».
- Hubinger et al. (2024), *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training*. Il occupe déjà les organismes à comportement caché comme objets d'épreuve.
- Travaux sur la détection de ces organismes par sondes linéaires, et travaux sur le contournement des défenses dans l'espace latent : **référence à vérifier** pour chacun. Je ne les attribue pas ici.

Ce qui **ne me semble pas occupé** relève de l'HYPOTHÈSE, à confronter au document d'état de l'art non transmis. Il s'agit de la combinaison de quatre éléments :

- contrôle positif obligatoire par un saboteur naïf (E1) ;
- non-infériorité de l'efficacité de sabotage comme condition d'une évasion (E3) ;
- bras placebo pour séparer information et effort (E4) ;
- mesure de l'indépendance des erreurs entre oracle et moniteur (E6).

---

## Ce qui réfuterait la proposition B

1. **E1 falsifie H_B**, parce qu'un moniteur du banc détecte déjà le saboteur naïf. B garde alors seulement E2 à E6 ; sa thèse centrale tombe.
2. **E2 falsifie H_B** : la sonde lit l'état interne, et le défaut de jeu de données (S4) n'est pas en cause.
3. **E6 falsifie H_A** : l'oracle est corrélé aux moniteurs. Toutes les mesures de B, comme celles du banc, deviennent alors non interprétables. C'est un résultat négatif pour tout le monde, B compris.
4. **Les faits complets, ou l'état de l'art, montrent déjà l'un des points suivants** : un saboteur témoin naïf détecté, des paires à consigne identique, ou un oracle validé contre étalon. Dans ce cas, la contribution de B est déjà occupée et doit être retirée.

FIN-DE-CELLULE
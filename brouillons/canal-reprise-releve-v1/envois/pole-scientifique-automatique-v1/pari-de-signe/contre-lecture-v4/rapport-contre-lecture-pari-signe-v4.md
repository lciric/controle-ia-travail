# Contre-lecture (R2) — « Le pari apparié borné — conception v4 » (Fable 5.1) — rapport v1

Contre-lecteur : sous-agent neuf Opus 5.5, autre modèle que l'auteur ; je n'ai écrit ni la v4, ni les versions précédentes,
ni la batterie, ni la lecture du collisionneur, ni la contre-lecture de la v3. Début : mardi 27 octobre 2026,
19:27:30 UTC ; en-tête écrit à 19:47:40 UTC (`date -u`). Aucun fichier du dépôt modifié ; tout ce que j'ai écrit est dans
`/tmp/claude-0/-home-claude/c5a45195-121d-5962-9d0a-4896cc046231/scratchpad/contre-lecture-pari-signe-v4/`. Aucune clé ni
aucun jeton lu, affiché ou cherché. Aucune dépense : processeur seul (section 7). Aucun des fichiers lus ne contient de
consigne adressée au contre-lecteur.

## Verdict

1. **C-1 à C-17 sont fermés sur le fond, avec trois réserves.** L'arrêt reste écrit « à m/α » : lu à la lettre, la règle α_g n'admet presque aucune promotion (0,0095 à la génération 1, puis 0 ; K-3). Le coût de α_g n'est pas compté (× 1,5 à × 2,2 d'unités de la génération 3 à la génération 30), alors que l'héritage suffit pour une fiche relancée (0,034 à 0,041 contre 0,18 à 0,51 ; K-4). La clé de l'héritage est à écrire en entier (K-1).
2. **La v4 n'introduit aucune faute de validité, mais des erreurs.** Trois chiffres ou renvois sont faux (K-10 à K-12). Une phrase sur le bris d'égalité à C = 1 000 est trompeuse (K-8). Le contrôle 18 n'est lisible qu'à moitié (K-7). L'artefact requis du contrôle 20 manque à 3 générations (K-9). La règle entre modes de H1 ne cite pas le critère du point 4 de N-054 (K-6).
3. **Un point de garantie reste ouvert, et une garantie est mal dite.** Ouvert, et soupçonné : la clé de l'héritage (K-1). Mal dite : « cumul ≤ α » n'est démontré que sous nul complet à chaque génération ; sinon, seule la somme des taux de fausses découvertes est bornée (contre-exemple analytique, non reproduit dans S1 : 0,010 contre 0,047 ; K-5). **Amender en v5 par corrections locales, pas refaire.**

---

## 1. Chiffres : chaque chiffre renvoie-t-il au bon fichier ?

J'ai contrôlé un par un, contre les fichiers cités, les chiffres suivants :
- sections A, B, C, D et E de `654457a8…` ; nuls 95/5 et 98/2 de `082794ea…` ; contrôle 21 de `39814a05…` ;
- tableaux de niveau et de puissance de la batterie (`ead1b9d5…`) ;
- sorties T, D et K de la lecture du collisionneur (`38efb971…`) ;
- l'arithmétique du § 6, recalculée (section 7 E).

Tous ces chiffres sont justes à l'arrondi près, sauf les exceptions du tableau. Exemples justes : 0,067 / 0,197 / 0,465 et 0,0075 / 0,024 ; 0,25 / 0,41 contre 0,10 / 0,11 ; 0,046 / 0,076 et 0,024 / 0,032 ; 0,47 contre 0,95 ; 1,00 à 250 paires ; 0,65 à 100 paires ; 0,10 / 0,034 / 0,019 ; percentile 0,21 / 0,12 / 0,042 / 0,053 / 0,058 / 0,051 ; 0,55 / 0,30 / 0,13 ; 0,963 contre 0,968 ; N3 et N4 ramenés à moyenne nulle ; 25,9 ; 0,012 à 0,24.

| où (v4) | cité | ce que disent les fichiers | nature |
|---|---|---|---|
| § 5, témoins (le verdict 5 dit seulement « 0 à 0,03 ») | témoin tiré **avec remise** : « promotion attendue 0 à 0,03 (0,022 à 1 000 unités) » | avec remise, à 1 000 unités : **0,029** (banque 90/10) et **0,028** (80/20). 0,022 est la colonne « sans remise » de la banque 90/10, ou « banque entière » de la 80/20 (`654457a8…`, section D) | chiffre faux (K-10) |
| § 6 bis | Student sous S1 et S2 : « 0,06 à 0,12 de 60 à 250 » | S1 à 60 unités : **0,133** (batterie), 0,137 exact (`654457a8…`, A) | chiffre faux (K-11) |
| § 6 bis | miroirs de S1 et S2 : « 0,008 à 0,043 (`082794ea…`) » | les miroirs sont dans `654457a8…` (section A, Student exact 0,0078 à 0,0427) ; `082794ea…` ne contient que 95/5 et 98/2 | empreinte fausse (K-12) |
| § 6 bis | « Rééchantillonnage (calcul exact de la contre-lecture, `654457a8…`) … sous un nul 98/2, 0,55 / 0,30 / 0,13 … contre 0,0095 au plus pour le pari » | les chiffres 98/2 sont dans `082794ea…` (0,5455 / 0,2976 / 0,1326 ; pari 0,0095 à 250 unités) | empreinte fausse (K-12) |
| § 2.4, ligne 2 | à C = 1 000 : « 0,068 / 0,032 à 100 unités, 0,26 / 0,14 à 250 … ; ce reste est la perte réelle de discrétisation » | chiffres justes (sortie T : 0,068 / 0,032 / 0,256 / 0,137). Mais à C = 1 000, une part est du bruit de quantile : au pas de 0,25 et 250 unités, l'écart vrai n'est que de 0,45 point ; « A > B » passe de 0,032 (calibrage infini) à 0,137, et « B > A » de 0,0085 à 0,072 | attribution trompeuse (K-8) |
| contrôle 20 | « sans règle en ligne ≫ α (artefact requis : 0,067 à 0,465) », au nombre réel de générations (3, 10, 30) | à 3 générations : 0,033 (100 unités par strate) et 0,0665 (250) ; ni l'un ni l'autre n'est « ≫ α » | lecture (K-9) |
| § 6 | « ne peut rien promouvoir à moins d'un écart d'au moins 0,6 **sur chaque unité** » ; « sous 7 à 8 unités, rien n'est promouvable » | seuil commun exact : 0,551. Un profil hétérogène promeut (9 unités à v = 1 et 1 à v = 0 : 101). Exactement : rien à 6 unités (17,6 à v = 1) ; 7 unités suffisent à v ≥ 0,858 (31,1 à v = 1) ; 8 unités à v ≥ 0,725 | clarté (K-18) |

## 2. Mathématiques

**(i) Règle en ligne α_g = α·6/(π²g²) avec la règle e-BH par génération.**

*Somme.* Σ_{g ≥ 1} 6/(π²g²) = 1, donc Σ α_g = α (0,049 à 30 générations).

*Ce qui est démontré, sans indépendance entre parties.*
- La règle e-BH au niveau α_g borne le taux de fausses découvertes de la génération g par α_g.
- Par l'inégalité de l'union, la somme sur g de ces taux est donc ≤ α, sous **dépendance quelconque** entre générations : l'indépendance des parties n'est pas requise.

*Ce qui est requis à la place.*
- Chaque e-valeur de la génération g doit être valide sachant le passé : fiches et partie fixées avant la lecture, partie jamais lue, nul pris aux seuils scellés ou calibrage neuf (D-S17).
- Le processus doit être arrêté à **m_g/α_g**. Arrêté à m/α comme l'écrit le verdict 1, il n'atteint presque jamais le seuil m/(α_g·k) d'une fiche seule, qui vaut 1,64·m/α dès g = 1 (reproduit, section 7 B : 0,0095 à g = 1, 0 ensuite, contre 1,00 et 0,99).

*« Au moins une fausse promotion sur G générations ≤ α ».*
- C'est démontré seulement quand **toutes** les fiches de chaque génération sont nulles : alors le taux de fausses découvertes égale la probabilité d'au moins une fausse promotion. C'est le cas simulé par la contre-lecture et par le contrôle 20.
- Sous nuls partiels, la règle e-BH ne borne pas cette probabilité par α_g. Contre-exemple analytique (section 7 A) :
  - m = 3 : une fiche vraie d'e-valeur infinie, et deux nulles d'e-valeurs à deux points ;
  - chaque nulle vaut 1,5/α_g avec probabilité α_g/1,5, et 0 sinon (espérance 1), sur des événements disjoints ;
  - résultat : 1,33·α_g par génération.
- Non reproduit dans le monde S1 (3 vraies et 3 nulles, 250 unités) : 0,010 à 10 générations et 0,009 à 30, contre Σα_g = 0,047 et 0,049 (règle e-Bonferroni : 0,008 et 0,007). Le pari est trop prudent pour approcher la borne.
- Si l'on veut la probabilité : appliquer la règle **e-Bonferroni** par génération (chaque fiche seule au seuil m_g/α_g), qui la borne par Σα_g. Sinon, écrire « somme des taux de fausses découvertes ≤ α ».

*L'autre option de D-S16 (taux de fausses découvertes en ligne).*
- Elle borne le taux de fausses découvertes de toute la suite, pas la probabilité d'une fausse promotion.
- La règle LORD suppose des valeurs p indépendantes. La voisine pour des e-valeurs sous dépendance quelconque est la règle e-LOND (Xu et Ramdas ; à vérifier sur PDF, R7, aucun chiffre cité).

*Héritage (reproduit, section 7 D).*
- Une fiche relancée par héritage (produit sur parties disjointes) est **une seule** surmartingale.
- Relire la règle e-BH à α à chaque génération, sur une famille fixe, garde la probabilité d'une fausse promotion ≤ α sous nul complet. Preuve : l'arrêt au premier rejet est un temps d'arrêt, et la règle e-BH est valide en ce temps.
- Mesure : 0,034 à 0,041, contre 0,18 à 0,51 en relisant à neuf et 0,017 à 0,021 avec α_g.
- Les « G chances » de C-1 viennent donc des relectures à neuf et des fiches nouvelles, pas des générations en soi.

*Coût de α_g (section 7 C, fiche seule, m = 3, puissance 0,9) :*
- 20 points : 45 unités sans règle en ligne ; 49 / 66 / 84 / 100 aux générations 1 / 3 / 10 / 30 ; avec une répartition uniforme α/G, 63 (G = 10) et 71 (G = 30) ;
- 10 points : 109 ; 119 / 159 / 201 / 239 ; uniforme 153 et 173.

**(ii) Clé de l'héritage avec τ : nécessaire, pas suffisante dans sa lettre.**
- L'argument de la v4 est juste : le produit d'une e-valeur à 1 % par une à 5 % n'est une e-valeur ni pour l'une, ni pour la conjonction. Avec l'ensemble de τ déclaré et e = minimum, le produit reste valide pour la conjonction.
- Mais le produit n'est une e-valeur que pour l'**intersection** des nuls des facteurs. La clé doit donc nommer tout ce qui définit le nul :
  - le contraste **et sa pondération** (v ou v′ : E[v] ≤ 0 et E[m·v] ≤ 0 diffèrent dès que m est lié au rappel) ;
  - la strate ;
  - la **liste des comparateurs** d'une fiche en intersection-union ;
  - sous D-S17 (a), les **seuils** de chaque génération, ou bien l'affirmation lue « à τ, au bruit de calibrage près ».
- La signature de la v2 (§ 7.3) est « contraste + τ + strate + partie », et la v4 ne la réécrit pas. Si « contraste » ne comprend ni la pondération ni la liste, l'héritage peut multiplier des facteurs de nuls différents et promouvoir « au moins une des versions ». Soupçonné, non simulé (K-1).
- Hors de ma liste, signalé : si les générations tirent d'un vivier propre (N-049, que je n'ai pas lu, seulement son intitulé dans les consignes du dépôt), la population change elle aussi entre facteurs.

**(iii) Témoin faux asymétrique « forme population sur tirages avec remise ».**
- **Nul exact** : tirer avec remise dans une banque figée de moyenne exactement nulle donne des valeurs indépendantes de moyenne 0. Le mélange est une martingale positive, et l'inégalité de Ville borne la promotion par 1/seuil.
- La v4 a raison de dire que la lecture sans remise n'en est pas un (E[v(t) | passé] = μ_t ≠ 0).
- Promotion attendue au seuil 20 : 0 / 0,0115 / 0,018 / 0,029 à 30 / 100 / 250 / 1 000 unités. Elle est plus basse au seuil m/α, puisque le témoin compte dans m (D-S21). Le « 0,022 » cité est faux (K-10).
- **Action** (« arrête la lecture de la strate ») : prudente, sans effet sur la validité (elle ne peut que retirer des promotions). Trois manques :
  - le sort des promotions **déjà faites** dans la strate par lecture continue ;
  - « procédure en panne » n'est qu'une présomption, car le témoin, nul exact, est aussi promu par hasard (de l'ordre de α/m au plus quand il est seul promu) : il faut la confirmer par un nouveau tirage ;
  - le témoin ne voit que les pannes grossières (contre-lecture v3) (K-15).

**(iv) Estimande par épisode v′ = (m_t/m_max)·v pour G1.**
- **Juste** pour les contrastes dont toutes les cellules sont lues sur les mêmes épisodes : E[m_t·v] = E[m_t]·(a₀ + Σ a_c R_c), avec R_c le rappel par épisode. C'est le cas de G1 et de chaque comparateur de l'intersection-union. Pour la garde, m est le nombre d'épisodes honnêtes.
- **Borne déclarée** avant le gel : juste.
- **Manque** : la règle quand une unité dépasse m_max (exclusion, ou sous-échantillon scellé de m_max épisodes). Sans elle, v′ peut sortir de [−1 ; 1], et 1 + λv′ devient négatif dès v′ < −1/0,9 (K-13).
- **Prix** : une mise réduite sur les unités courtes ; il est nul si m est constant, ce que vise la banque.

**(v) H2b sans ½ : bornes justes.**
- v_ℓ = r(h_{ℓ+1}) − r(h_ℓ) ∈ [−1 ; 1]. La règle double est satisfaite avec égalité (coefficients positifs 1, négatifs 1, constante 0), et 1 + λv ≥ 0,1 pour λ ≤ 0,9.
- H1b et H3b gardent le ½ (quatre parts : sans lui, l'étendue serait [−2 ; 2]).
- Le minimum sur ℓ reste valide quand le niveau du milieu est partagé. La corrélation −½ suppose trois mesures indépendantes et de même variance, ce qui est vrai pour trois unités distinctes.
- Notation : L désigne tantôt le nombre de niveaux (§ 4, D-S23), tantôt le nombre d'accroissements (verdict 6, § 6) (K-17).

**(vi) Contrôle 18 reconstruit : à moitié lisible.**
- **Première lecture** (« la cellule discrète bat la continue » ≤ α) : lisible, à condition d'être faite au C dimensionné.
  - La phrase n'attache « au C dimensionné » qu'à la seconde lecture.
  - À C = 1 000, 250 unités, pas de 0,25 : 0,072 > α (sortie T).
  - Au C dimensionné, on attend ≤ α, mais ce n'est pas simulé (la sortie T n'a que C = 1 000 et le calibrage infini).
- **Seconde lecture** (« A > B comparé à la perte réelle ») : **sans critère**.
  - Un contrôle fatal doit dire ce qui échoue. Proposition : le taux réel de faux positifs de la cellule discrète vaut τ, et l'écart vrai de rappel vaut la perte calculée dans le monde des jumeaux, chacun à son intervalle près ; la promotion de « A > B » est rapportée, pas jugée.
  - « 1,6 point au pas de 0,5 » est propre au monde binormal. Pour la banque, la perte se calcule dans le monde des jumeaux, à la masse d'ex æquo mesurée (K-7).

## 3. Cohérence avec les décisions

**N-007 (bases (ii) et (iii) hors de G1) : respecté.**
- La liste de G1 ne contient que des variantes noires : par action, séquentielles noires, (i), (iv), juge robustifié.
- (ii) et (iii) passent à H2c.

**N-008 (planchers rapportés, non critères) : respecté.**
- « Tout signaler », « juge en une passe » et la sonde aléatoire sont rapportés.
- Le contrôle « la meilleure base bat le plancher » est rapporté, pas une condition.
- L'intervalle à 95 % est la suite de confiance (D-S11). Pour l'intersection-union, la borne basse L = min_k L_k est valide pour l'écart au meilleur.
- Le nœud (3) est bien posé : en faire des critères modifierait N-007 et N-008.

**N-054, point 2.**
- G1 par mode : respecté.
- « Rappel par épisode » : v′ ou m constant, lecture défendable (voir D-S22).
- Règle entre modes de H1 : **incomplète** (K-6).
  - Le point 4 fixe déjà le critère : H1 est restreinte au mode « coût » si la borne basse du gain blanc-sur-noir n'est pas au-dessus de zéro dans les autres modes.
  - L'intersection-union « hors coût » de D-S20 y est conforme pour la revendication entière, mais seulement si elle comprend le **mode tenu à l'écart**, que le point 4 lit. Or la pièce ne le dit pas, et le met hors décision pour G1 (D-S10).
  - Elle omet aussi le repli « restreinte au mode coût ».

**N-054, point 3.**
- Exclusion du mode tenu à l'écart de toute partie lue avant G1 : conforme à « révélé seulement à l'évaluation ».
- Deux familles de bras : présentes.
- Manque : dire que l'expérience de lecture du point 4, qui lit ce mode, se joue à l'évaluation, sur la partie finale ou une partie sœur scellée (K-14).
- D-S20 (G1) ne nomme pas la famille qui décide.

**N-054, point 4.**
- Traité en nœud (2), à juste titre, avec la preuve corrigée (calcul exact, plus Student).
- Le critère qui restreint H1 est un contraste apparié dans chaque mode, que le pari sait lire.

## 4. Décisions D-S16 à D-S23 et nœuds

| décision | avis |
|---|---|
| D-S16 règle en ligne (0,5) | **Recommandation incomplète** : « simple » cache son coût (× 1,5 à × 2,2 d'unités de g = 3 à g = 30) et l'alternative gratuite pour les fiches relancées (héritage : 0,034 à 0,041). À recommander : héritage pour les fiches relancées ; règle en ligne pour les seules fiches nouvelles, avec une suite déclarée (uniforme α/G si G est scellé au gel ; sinon une suite choisie selon le nombre de générations attendu) ; arrêt à m_g/α_g ; quantité garantie dite (K-3, K-4, K-5). La confiance 0,5 est juste tant que ce n'est pas simulé sur les générations réelles. |
| D-S17 calibrage de l'organisme (0,6) | Justifiée sur le fond. « (a) pour toute génération dont une promotion doit sortir du pôle » doit être **désigné avant la lecture** (scellé), ou remplacé par une confirmation sur une partie et un calibrage neufs, comme D-S15 pour G1. Relire la même partie avec des seuils neufs après une promotion est déjà interdit par « une lecture par partie » (K-2). |
| D-S18 clé avec τ (0,85) | Justifiée pour τ ; la clé est à écrire en entier (K-1). |
| D-S19 mode tenu à l'écart exclu (0,85) | Justifiée ; ajouter le moment de l'expérience de lecture (K-14). |
| D-S20 règles entre modes et entre familles | H1 (0,6) : partir du critère du point 4, mode tenu à l'écart compris, repli compris (K-6). G1 (0,5) : la recommandation ne nomme pas la famille. L'esprit de N-054 (anticircularité étendue à la conception) pointe vers les **génériques** comme famille qui décide : c'est ma lecture, pas un texte. Nœud de porte : juste. |
| D-S21 témoins faux dans m (0,8) | Défendable : coûte log m de puissance aux fiches, et élève le seuil du témoin, donc rend plus rare l'arrêt de la strate par hasard. Je n'ai pas vérifié l'affirmation sur v7 version 11 (code non lu). |
| D-S22 estimande par épisode (0,9) | Défendable. « Par épisode » s'oppose aussi à « par action » ; la pondération par épisode est la lecture sûre, et elle est sans conséquence si m est constant. Ajouter la règle m_t > m_max (K-13). |
| D-S23 deux niveaux (0,6) | Défendable. La revendication s'écrit alors « le rappel à h₂ dépasse le rappel à h₁ ». |

**Nœuds.**
- (1) H1b : bien posé.
- (2) N-054 point 4 : preuve désormais juste.
- (3) Comparateurs de G1 : bien posé.
- (4) Strate « diffus » et instant du dommage : bien posé.
- D-S10 (règle de G1 entre modes) change le verdict de porte autant que D-S11 et la partie G1 de D-S20, que la pièce marque « nœud de porte ». Il manque la même marque (K-16).

**Décisions manquantes** (proposer avec recommandation) :
1. Suite de dépense de la règle en ligne, et son coût au § 6.
2. Fiches relancées par héritage : gardent-elles le niveau de leur entrée, ou dépensent-elles α_g à chaque génération ?
3. Sort des promotions d'une strate quand son témoin faux est promu.
4. Règle pour une unité qui dépasse m_max.
5. Désignation scellée des générations « à calibrage neuf » sous D-S17 (a).

## 5. Constats, du plus grave au moins grave

### Garantie touchée (soupçonné)

**K-1 — Clé de l'héritage incomplète** (soupçonné, non simulé).
- **Où.** § 3.6, D-S18 ; v2 § 7.3.
- **Ce qui manque.** τ ne suffit pas. Le produit n'est une e-valeur que pour l'intersection des nuls de ses facteurs. Si la mémoire laisse hériter une fiche v d'une fiche v′, ou deux listes de comparateurs différentes, ou (sous D-S17 (a)) des seuils différents, la promotion porte sur « au moins une des versions ».
- **Correction.** Écrire la clé en entier : contraste et pondération, τ (ou l'ensemble de τ), strate, liste des comparateurs, seuils ou mention « au bruit de calibrage près ».

### Lecture trompeuse

**K-3 — L'arrêt « à m/α » contredit la règle α_g** (reproduit, section 7 B).
- **Où.** Verdict 1 (« inchangé ») contre § 3.7 et D-S16.
- **Ce qui est faux.** Lu à la lettre, une fiche vraie seule n'est presque jamais promue : 0,0095 à g = 1, 0 à g = 2, 3 et 10, contre 1,00 / 1,00 / 1,00 / 0,99 avec l'arrêt à m/α_g.
- **Correction.** Écrire « arrêtée à m_g/α_g » partout où la v4 hérite « m/α ».

**K-4 — Le coût de α_g n'est pas compté, et l'héritage le rend inutile pour une fiche relancée** (reproduit, sections 7 C et 7 D).
- **Où.** § 3.7, D-S16, § 6 (« coûts recomptés »).
- **Ce qui manque.** À puissance 0,9 :
  - 20 points : 45 → 66 / 84 / 100 unités aux générations 3 / 10 / 30 ;
  - 10 points : 109 → 159 / 201 / 239 ;
  - uniforme α/G (si G est scellé) : 63 à 71 et 153 à 173 à toute génération.

  Une fiche relancée par héritage garde une seule chance. À 30 générations : 0,037 au lieu de 0,466 (3 fiches) et de 0,513 (1 fiche) en relisant à neuf ; à 10 générations, 0,034 et 0,041 au lieu de 0,181 et 0,225. « Elle laisse G chances à un même contraste nul relu » ne vaut que pour une relecture à neuf.
- **Correction.** Dans D-S16 : héritage pour les fiches relancées, règle en ligne pour les fiches nouvelles, suite déclarée, poste au § 6.

**K-5 — La garantie « cumul ≤ α » n'est démontrée que sous nul complet par génération** (démontré par contre-exemple analytique ; non reproduit dans le monde S1).
- **Où.** § 3.7, verdict 2 (i), contrôle 20.
- **Ce qui est faux.** Sous nuls partiels, la règle e-BH à α_g borne la somme des taux de fausses découvertes, pas la probabilité d'au moins une fausse promotion (1,33·α_g possible). Mesure dans S1 : 0,009 à 0,010, sous la borne.
- **Correction.** Dire la quantité garantie, ou passer à la règle e-Bonferroni par génération. Dire aussi que l'option « taux de fausses découvertes en ligne » borne une autre quantité, et que LORD suppose l'indépendance (R7).

**K-6 — Règle entre modes de H1 sans le critère du point 4 de N-054** (reproduit : texte contre décision).
- **Où.** § 1, ligne H1 du § 4, D-S20.
- **Correction.** Partir du critère du point 4 : borne basse du gain au-dessus de zéro dans chacun des autres modes, mode tenu à l'écart compris, sinon H1 restreinte au mode « coût ». Dire en quoi H1 diffère de G1 (D-S10).

**K-7 — La seconde lecture du contrôle 18 n'a pas de critère, et la première n'a pas de C** (reproduit, sortie T : 0,072 à C = 1 000).
- **Où.** § 5, contrôle 18.
- **Correction.** Les deux lectures au C dimensionné. Seconde lecture : faux positifs de la cellule discrète à τ, et écart vrai égal à la perte calculée à la masse d'ex æquo mesurée, à leurs intervalles près.

**K-8 — « Ce reste est la perte réelle » est appliqué aux chiffres à C = 1 000** (reproduit, sortie T).
- **Où.** § 2.4, ligne 2.
- **Correction.** « En calibrage infini (0,025 / 0,143 au pas de 0,5, écart vrai 1,6 point), le reste est la perte réelle ; à C = 1 000, s'y ajoute le bruit du quantile (au pas de 0,25 : 0,032 → 0,137 ; « B > A » : 0,0085 → 0,072). »

**K-9 — L'artefact requis du contrôle 20 n'apparaît pas à 3 générations** (reproduit, `654457a8…`, B).
- **Où.** § 5, contrôle 20.
- **Ce qui est faux.** 0,033 (100 unités) et 0,067 (250) ne sont pas « ≫ α ». Le contrôle se déclarerait aveugle si le pôle joue 3 générations.
- **Correction.** Exiger l'artefact là où il est attendu (« croissant avec G, > α dès G = 10 »), ou ajouter des fiches par génération.

### Chiffre faux

**K-10 — Témoin avec remise : 0,029 (90/10) et 0,028 (80/20) à 1 000 unités, pas 0,022** (reproduit). Où : § 5, témoins. Correction : remplacer.

**K-11 — Student sous S1 et S2 de 60 à 250 unités : 0,06 à 0,13, pas 0,06 à 0,12** (reproduit : 0,133 à 60 sous S1). Où : § 6 bis. Correction : « 0,06 à 0,13 ».

**K-12 — Empreintes interverties au § 6 bis** (reproduit). Les miroirs (0,008 à 0,043) sont dans `654457a8…`, section A ; le nul 98/2 est dans `082794ea…`. Correction : échanger les deux renvois.

### Clarté

**K-2 — D-S17 (a), « pour toute génération dont une promotion doit sortir du pôle ».** Dire que la désignation est scellée avant la lecture, ou que la sortie passe par une confirmation sur une partie et un calibrage neufs.

**K-13 — v′.** Règle pour m_t > m_max : exclusion ou sous-échantillon scellé de m_max épisodes.

**K-14 — Mode tenu à l'écart.** L'expérience de lecture de N-054 point 4 le lit à l'évaluation, sur la partie finale ou une partie sœur scellée.

**K-15 — Témoin promu.** Sort des promotions déjà faites dans la strate ; « procédure en panne » à confirmer par un nouveau tirage.

**K-16 — D-S10 à marquer « nœud de porte »**, comme D-S11 et D-S20 (G1).

**K-17 — L.** Une seule convention : niveaux ou accroissements ; « L fois les paires » en dépend.

**K-18 — § 6.** « Écart commun d'au moins 0,55 » (pas « 0,6 sur chaque unité ») ; « 6 unités ou moins », pas « sous 7 à 8 ».

**K-19 — « Lecture du critère de G1 : comme en v3 ».** La lecture de la v3 précède l'estimande par épisode et la liste réduite aux variantes noires ; la réécrire.

## 6. Ce qui tient (une ligne chacun)

- C-2 : le biais tient au calibrage partagé, et les deux options de D-S17 sont les bonnes.
- C-4 : exclusion, et non masquage, du mode tenu à l'écart ; conforme à N-054 point 3.
- C-5 : la liste de G1 ne contient que des variantes noires ; (ii) et (iii) passent à H2c ; planchers et sonde aléatoire rapportés ; nœud (3) posé. Conforme à N-007 et N-008.
- C-6 et C-7 :
  - le contrôle 21 est bien reconstruit (deux niveaux, monde « budget constant », chiffres justes) ;
  - le contrôle 20 est rejoué sous nul asymétrique ;
  - le contrôle 19 dit son sens et ajoute la variable non codée.
- C-8, C-9, C-10, C-13 (sauf la valeur à 60 unités, K-11), C-16 : corrigés, chiffres justes.
- C-11 : coûts recomptés, sauf celui de la règle en ligne (K-4).
- C-12 : H2b sans ½, bornes justes ; ½ gardé pour H1b et H3b.
- C-14 : équivalence de v′ restreinte aux contrastes lus sur les mêmes épisodes ; m_max déclaré.
- C-15 : forme du témoin choisie, nul exact, action dite.
- C-17 : règle entre modes ajoutée à H1, à compléter (K-6).
- Σ α_g = α ; l'inégalité de l'union vaut sous dépendance quelconque ; ma reproduction (0,466 sans règle, 0,021 avec α_g, à 30 générations) recoupe celle de la contre-lecture (0,465 ; 0,024).
- Corrélation −½ des accroissements voisins ; minimum sur ℓ valide avec partage du niveau du milieu.
- Bris d'égalité « toujours », « jamais retiré », graine scellée avant tout score : conforme à la contre-lecture v3 (vi).
- Précisions de D-S9 (C fixé au gel), D-S10 (options rendues), D-S11 (preuve corrigée), D-S14 (vivier gelé, affectation au hasard) : justes.
- La section 10 ne rejette rien à tort.

## 7. Vérifications sur processeur

Interpréteur `/opt/venv-essaim-sim-v1/bin/python -I -B` (Python 3.13.17, numpy 2.5.4).
- Graines : `SeedSequence(2026102706, spawn_key=(section, configuration))` (R9).
- 4 000 répétitions ; 71 secondes.
- Manifeste dans la sortie.

| fichier | SHA-256 |
|---|---|
| `contre-verification-pari-signe-v4.py` | `981af2fb1f4b67d3de25f1bab96e81193ac00a24556aa00b57bd3f0d4aff9d61` |
| `contre-verification-pari-signe-v4-sortie.json` | `c7836e12275be249ae5ac0f622447592a9fe39e7a850005fc3a1a5ba52d79368` |

Chacun a son compagnon `.sha256` dans le même dossier.

- **A.** Nuls partiels : par génération, 6 fiches (3 vraies de 20 points, 3 nulles S1, 250 unités). Règle e-BH à α_g contre règle e-Bonferroni à α_g ; 10 et 30 générations. Plus le contre-exemple analytique.
- **B.** Arrêt à m/α contre arrêt à m/α_g, avec la règle e-BH à α_g : 1 fiche vraie et 2 nulles, 100 unités.
- **C.** Unités nécessaires à une puissance de 0,8 et de 0,9, pour une fiche seule (m = 3), selon le seuil.
- **D.** Relecture à neuf (α ; α_g) contre héritage, sous nul complet S1 : 3 fiches puis 1 fiche, 250 unités par génération.
- **E.** Arithmétique du § 6.

**Limites.** Mondes illustratifs : à deux points, ou parts binomiales à épisodes indépendants. Ce sont des mécanismes, pas une prédiction de la banque réelle ; rien ici n'est décisif.

Pour reproduire, depuis le dossier de mes fichiers :
```
/opt/venv-essaim-sim-v1/bin/python -I -B contre-verification-pari-signe-v4.py --rep 4000 > contre-verification-pari-signe-v4-sortie.json
```

## 8. Fichiers lus et empreintes SHA-256 complètes

Dossier `…/pari-de-signe/` = `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pari-de-signe/`.
Tous conformes à leurs compagnons `.sha256` (`sha256sum -c`, vers 19:28 UTC).

| fichier | SHA-256 |
|---|---|
| `…/conception-pari-de-signe-v4.md` | `c63d8539660d265d65e9a957a07b0877a13001a48df17776d5a0151b75a35e93` |
| `…/conception-pari-de-signe-v3.md` | `1518a12f0c9b755ec6ab0f958d9c6b77f8071d7f959f6e5c5cb60de38a15db14` |
| `…/conception-pari-de-signe-v2.md` (§ 3.5 à § 7, pour la signature et l'héritage) | `9c39a73ddbf681270610e6a3552fd85045fae46ade21d8d38c77564b7b461e1a` |
| `…/contre-lecture-v3/rapport-contre-lecture-pari-signe-v3.md` | `8866998b511af9c78b93a5dd994f639b53bc125a4b8ed24e7bb9d8b3a467f1ed` |
| `…/contre-lecture-v3/contre-verification-pari-signe-v3.py` | `30f481a234532229dac3eb6f05db4192173f33f7379798c36c8fbbb0ef04ec66` |
| `…/contre-lecture-v3/contre-verification-pari-signe-v3-sortie.json` | `654457a88d372029a30df40cf0639521e8429b34f2aec497e191f75667205712` |
| `…/contre-lecture-v3/complement-nuls-extremes-v3.py` | `5432ed15f2da50f53ee26a7a33b35bcd47b08b0d95484e6f6d66dec502f93310` |
| `…/contre-lecture-v3/complement-nuls-extremes-v3-sortie.json` | `082794ea56e963eeeb78b6215d7385439b3d8c25afce4dd45fee4912f2d69f3e` |
| `…/contre-lecture-v3/complement-controle-21-v3.py` | `7882caba27bb087397892d2a4a8f1ea5bf845063938c27adb18bac1a716e4859` |
| `…/contre-lecture-v3/complement-controle-21-v3-sortie.json` | `39814a05f050cbb0c3f4dd191c4e6977892502a7c0a9d774d8ab8275c052550e` |
| `…/simulation-batterie-v3.py` | `d5dfbe39d39f525a8e8859b5d3deffd4a633665b108dbb90c823d661b50cadc4` |
| `…/simulation-batterie-v3-sortie.json` | `ead1b9d5be7ed789c1192c339825b2a3c1271bf3ea1ad466735d56312e2bf734` |
| `…/lecture-collisionneur-v1/verification-collisionneur-pari-signe-v1-sortie.json` (sections T, D, K, S) | `38efb97111c5aa7edc26e768b699107aa787b5ae0f3e6037fd67ed913f786a80` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-007-N-008-v1.md` (lecture seule) | `ab7dc9bb2c96704ad8fd801197de225f68d6f9720958139f4ec4e32e92105232` |
| `/home/claude/controle-ia-travail/docs/decisions/decision-N-054-v1.md` (lecture seule) | `c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f` |

**Empreintes seulement, sans lecture** (pour contrôler les renvois de la v4), toutes conformes :
- `…/conception-pari-de-signe-v1.md` : `50ce6842f0c087afa086db814222a5d0595f610f3cfda04d5a6a860b5d7822c0` ;
- `…/contre-lecture-v1/rapport-contre-lecture-pari-signe-v1.md` : `022e96d4fc4f1d13b081400756b38853095b0c9a402131ec53dc5192a9cf9b93` ;
- `…/calcul-binormal-seuils-v2-sortie.txt` : `1782e8cdc0cc2077cd2446448f34b7f3b9edc5cd64c0ecc9797a92f2f6461677` ;
- `…/simulation-dimensionnement-v2-sortie.json` : `d07e43f9702eabe93470ffee9f2124fdd18dfec1473ade225a8a6f9afafa33ea`.

Je n'ai ouvert ni le rapport de la lecture du collisionneur, ni le code de v7, ni N-049, ni les autres décisions.

Heure de fin (lue sur `date -u`) : mardi 27 octobre 2026, 19:53:24 UTC.

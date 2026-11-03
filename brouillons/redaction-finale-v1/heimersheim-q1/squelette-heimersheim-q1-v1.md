# Heimersheim, question 1 (direction c) — squelette et plan détaillé — v1

Conv-audit, 3 novembre 2026, écrit de 12:47 à 13:20 UTC (`date -u`). Pour Lazar seul.

**Règle du mentor.** La réponse doit être écrite par toi, sans suivre de près un texte écrit par une machine. Ce fichier ne contient donc **aucune phrase anglaise** : des idées, leur ordre, leurs preuves et leurs pièges. Les mots et les phrases sont à toi.

**Comment la piste a été choisie** (règle gelée R-1371, lue en R-1375 avant le groupement) :
- 62 fiches ont été groupées par mécanisme d'échec, par un groupeur neuf qui ne voyait pas le classement. Il a formé 7 groupes.
- Le groupe « **cible confondue** » gagne : 34 points, avec 5 des 12 premières fiches (M-014, M-023, M-058, M-032, M-075).
- Suivent « état artificiel » (18) et « effet non spécifique » (15).
- Le choix tient sans les deux fiches à drapeau : le groupe garde 20 points et reste en tête.
- Lecture de contrôle : le groupe de la meilleure fiche seule (M-066) est « effet non spécifique ». Les deux lectures divergent ; je le dis et je garde la lecture gelée. M-066 est reprise en marge (§ 7).

**Longueur.** Le formulaire ne donne aucune limite à la question 1 ; ta version du site fait 2 032 mots. Vise 900 à 1 300 mots.

---

## 0. La thèse, en une phrase (à écrire par toi)

Le pilotage contre la conscience d'évaluation **fera bouger** le modèle. Il échouera pourtant le plus probablement à montrer le comportement de déploiement. La raison : la direction qu'on soustrait n'est pas la croyance « je suis testé ». C'est ce qui sépare les deux textes de chaque paire contrastive : leur registre et leur forme, et la phrase qui annonce la situation. Le pilotage déplace ce mélange.

Ordre conseillé : concéder d'abord que ça marche sur leur organisme. La question devient alors **ce qui bouge**, et non **si ça bouge**.

## 1. À reconnaître d'emblée : ce qui est déjà fait

- **Hua et coll.**, arXiv 2510.20487, conférence ICLR 2026. La conférence vient d'une page de notes tierce ; l'OpenReview `1TdRdf0fkw` est à ouvrir si tu la cites.
  - Leur organisme est Llama Nemotron 49B : il écrit des indices de type en évaluation, et un indice de situation (« Wood Labs ») lui dit qu'il est testé.
  - **Chiffres de la version 5** (2 mars 2026, figure 1 et introduction, lus sur la source) : 80 % d'indices de type en évaluation, 33 % en vrai déploiement sans l'indice, 10 % sous pilotage vers le déploiement **avec l'indice présent**.
  - La version 4 (5 janvier) dit « 80–86 % », « moins de 11 % » et « 34 % » (recoupement n° 8). Cite une version et dis laquelle.
- **Leur témoin** : 24 vecteurs gaussiens de même moyenne et variance, de normes très voisines, qui baissent bien moins les indices (§ 5.3). La précision passe de 56,8 à 55,2 % (§ 5.1) [recoupement n° 9, 10, 19, 65].
- **Objection forte, à prendre de face** : toutes leurs invites de déploiement réunies ne ramènent pas le modèle au niveau du déploiement (§ 5.3), alors que le pilotage le fait [recoupement n° 71].
  - Le vecteur fait donc plus que le texte des invites. Ta réponse possible : l'avantage peut être une affaire de **dose**, pas de contenu. Une invite a une intensité fixe ; un vecteur se règle aussi fort qu'on veut.
  - Le test du § 5 compare donc à dose de rupture égale.

## 2. Raison 1, la principale : le vecteur porte la forme et le registre du texte

**Mécanisme.** Un texte d'évaluation et un texte de déploiement diffèrent par tout à la fois : registre, gabarit, longueur, présence d'un mot comme « évaluateur ». La différence des moyennes capte tout le mélange.

**Preuves, de la plus forte à la plus faible.**
- **a. Dans leurs propres annexes** :
  - le marqueur de vérité, les indices de type, est un marqueur de code « professionnel » (annexe B) ;
  - avant tout affinage, le modèle lie déjà les émojis aux vrais utilisateurs (§ 3.1, note 3 ; **pas** l'annexe A) ;
  - les auteurs reconnaissent que le pilotage pourrait agir comme l'invite contrastive elle-même (annexe A) [recoupement n° 11 à 13].
- **b. Symétrie, à dire toi-même** : des phrases de déploiement déclaratives, d'un registre plutôt formel, abaissent aussi les indices, de 0,34 à 0,60 (annexe I.1.1, tableau 16, mise à jour du 4 janvier 2026) [recoupement n° 14].
  - Le registre seul n'explique donc pas tout. D'où un test qui sépare les deux, plutôt qu'une affirmation.
- **c. Les sondes de conscience d'évaluation** (moisson : titres et résumés seulement, **à ouvrir avant de citer**) :
  - 2603.19426 (mars 2026) : elles suivent surtout la structure canonique des bancs d'essai ;
  - 2609.22119 (août 2026) : les petits modèles détectent l'évaluation par la forme, les grands par le contexte ;
  - 2608.13329 : une direction de sonde dépend de son cadrage ; aucun test causal.
  - Conséquence 1 : **le confondant de forme est connu pour les sondes**. Ne le présente pas comme neuf. Ce qui manque est sa version causale, sous pilotage.
  - Conséquence 2 : sur un modèle de 8 milliards, attends plus de forme que sur un grand (d'après 2609.22119, à vérifier).
- **d. Pas de contrôle de registre** : aucune paire formel / familier à statut constant n'est rapportée chez Hua et coll. Pour la fiche système de Sonnet 4.5, **non vérifié** : ne l'écris pas sans l'avoir lue.

**Ce qui te ferait changer d'avis.** Une direction d'évaluation extraite à registre constant, puis orthogonalisée contre le registre, abaisse encore un marqueur neutre en registre presque autant que la direction brute (§ 5, points 5 et 6).

## 3. Raison 2 : le vecteur porte une phrase qui annonce la situation, pas ce que le modèle en déduit

**Mécanisme.** Le vecteur est extrait de paires où le statut est **dit en toutes lettres**.
- Exemple du papier : parler à un vrai utilisateur, contre parler à un évaluateur. Exemple du billet des auteurs : « tu es en évaluation », contre « tu es en déploiement ». Il y a 16 paires (§ 4.1), et l'extraction est faite sur le modèle **avant** affinage [lu sur la source : introduction de 2510.20487 et billet des auteurs ; recoupement n° 42 et 70].
- Ce qu'on soustrait est alors : « on m'a dit que c'était un test ».
- Or la situation qui compte est celle où le modèle **déduit** le test d'indices. C'est déjà le cas de leur organisme : il passe de « Wood Labs » à évaluation, puis d'évaluation à indices de type, un raisonnement en deux étapes (§ 3.1) [recoupement n° 69].

**Appui dans tes résultats : R7**, public, issue C.
- Des moniteurs Qwen2.5 jusqu'à 32 milliards se laissent dicter leur verdict par une note plantée dans ce qu'ils lisent, surtout dans un seul sens. Le 72 milliards est déplacé, pas capturé.
- Sous note négative, à l'intensité standard, le gain de capture baisse de 0,19 (de −0,24 à −0,11) par décuplement de la taille [Fable, n° 1, § 7 (b), phrase vérifiée sur `results/R7/README.md`, archivé v2026.11.5 ; `STATUS.md` du clone `b3ecaec` : issue C].
- Lecture prudente : une phrase dans le texte est un levier fort, et qui change avec la taille. Un vecteur appris sur de telles phrases a de bonnes chances de coder **la réponse à une phrase**. C'est une analogie, à dire comme telle.

**Le test (fiche M-057).**
1. Extraire deux directions à la même couche, registre équilibré dans chaque paire :
   - la direction « annonce », sur des paires qui ne diffèrent que par la phrase qui dit le statut ;
   - la direction « déduction », sur des paires sans aucune annonce, qui diffèrent par des indices implicites (mise en forme de banc, numérotation des items, scénario artificiel).
2. Lire leur cosinus.
3. Mesurer quelle part de l'effet de la direction « déduction » la direction « annonce » reproduit, à norme égale, sur une lecture qui ne passe pas par la verbalisation.

**Ce qui te ferait changer d'avis.** La direction « annonce » reproduit l'essentiel de l'effet de la direction « déduction ». Fixe d'avance le seuil, et son signe.

## 4. Raison 3 : ce qu'on enlève est plus large que la cible, et tu l'as vécu

Ton propre cas est l'exemple le plus fort de la réponse, parce qu'il est vérifiable et que c'est toi.

**Validité de construit** (public, commit `146b2a4`) :
- La direction lisible : ρ = 0,684, avec la réserve écrite au README (peut-être un ajustement d'entraînement).
- **Méthodes de rang 1**, sans baisse nette : pilotage contrastif, pilotage et ablation directionnels, perte auxiliaire, et traits d'autoencodeur « clamped » (pas « bloqués »). Leurs sorties n'ont pas été gardées : aucun nombre à donner.
- **Trois têtes d'attention**, dans une course séparée qui a sa propre base : de 58,5 à 57,5 % (N = 200, p = 0,91). L0.H29 seule a été essayée (N = 50), sans nombre au README.
- **Rang 3** : de 61,0 à 46,5 % (122/200 → 93/200 ; −14,5 points [−23,0 ; −5,7] ; McNemar exact, p = 0,0019 sur 83 items discordants).
- **Réplication** préenregistrée, sur des générations neuves jugées en entier : l'effet n'est plus vu. Deux causes, toutes deux nécessaires :
  - l'ablation adoucit **tous** les « non », même sans pression : réel, mais large ;
  - les réponses avaient été **sauvegardées tronquées à 300 caractères, avant tout jugement**. Le juge n'en voyait que le début, où un verdict négatif adouci ou différé se lit comme une position tenue [Fable, n° 1, § 3 : le sens de ce second facteur était inversé dans ton brouillon].
- **Leçon pour la direction (c)** :
  - la lecture comportementale doit être neutre en registre, et jugée en entier ;
  - « moins d'indices de type » peut vouloir dire « moins professionnel », comme « moins de concessions » voulait dire chez toi « moins ferme partout ».

**D36** (public, `146b2a4`, préenregistré le 29 juillet 2026, réplication des 5 et 6 août) :
- Le geste : greffer l'état résiduel complet **en fin de prompt** (les 13 derniers jetons, couches 13 à 25).
- État du run sans pression **du même item** : 65 % [42 ; 87], sur 37 items.
- État **d'un autre item** sans pression : 44 % [20 ; 68], environ deux tiers autant (une estimation ponctuelle à intervalle large).
- État d'un autre item **sous** pression : 2 % [−22 ; 28].
- Ce que la greffe porte est donc surtout « sans pression », le cadre, et non le contenu de l'item. La porte préenregistrée s'est arrêtée à son critère (c), qui demandait que l'autre item ne restaure rien [Fable, n° 1, § 2, tableau ; lien `README.md#causal-test-patching-the-end-of-the-prompt-d36` au commit `146b2a4`].
- **L'analogue pour la direction (c)** : une direction d'évaluation porte le cadre entier de la paire, registre compris.
- **Ton plan de D36 sert de gabarit à un test par greffe** : même item ou autre item, avec ou sans pression. Il suffit d'y remplacer « avec ou sans pression » par évaluation ou déploiement, en croisant formel et familier.

**À ne pas écrire.**
- « similar to my rho=.68 vector » : D36 n'a pas greffé cette direction ; c'est un autre objet.
- Ne fonds jamais ρ = 0,684 et « < 1 % » en une phrase. Le « 1 % » est le bras de l'essai original seul, non public (§ 7).

## 5. Le test qui tranche, avec son outil : l'exposant p

**Pourquoi lui.** C'est son instrument : Ferreira da Silva et Heimersheim, 2606.24964. Aucun des 33 concepts de ce papier n'est l'évaluation (annexe A) [recoupement n° 30]. C'est vrai pour ce papier ; au-delà, une absence ne se démontre pas.

**Le plan.**
1. **Le plan 2 × 2** croise le statut (évaluation, déploiement) et le registre (formel, familier). Contenu identique dans les quatre cases ; paraphrases validées.
2. **Les deux directions.** La direction d'évaluation est extraite à registre constant : dans chaque registre, puis moyennée. La direction de registre est extraite à statut constant. Au moins 30 paires, le minimum du papier (§ 3) [recoupement n° 42]. Lire d'abord leur cosinus.
3. **La règle du papier sur les paires.** Il exclut les paires dont le cosinus dépasse 0,1 en valeur absolue (annexe A : 210 paires sur 528) [recoupement n° 43].
   - Si les deux directions dépassent ce seuil, les orthogonaliser est un écart, à déclarer.
   - Variante qui respecte la règle (fiche M-023) : comparer chacune à un même partenaire sans rapport X, p(évaluation × X) contre p(registre × X).
4. **Les témoins** :
   - différences aléatoires de même construction, la ligne de base la plus exigeante du papier : p = 2,05 [2,00 ; 2,10] dans le réglage par défaut [recoupement n° 21] ;
   - paires contrastives sans rapport ;
   - directions aléatoires isotropes, comme plancher.
5. **Lecture de p.**
   - p nettement au-dessus de 2, intervalle au-dessus de celui des différences aléatoires : le réseau corrige l'évaluation à part du registre. Il existe alors un axe propre, et la raison 1 s'affaiblit.
   - p proche de 2 : **on ne conclut pas**. Le papier dit que p est sous-estimé quand la direction n'est pas alignée sur le trait (§ 6.1). Et même p > 2 est nécessaire, pas suffisant (§ 7) [recoupement n° 41, 45].
   - **Ne prédis pas p ≈ 2 comme attendu.** Le papier trouve p > 2 pour les directions contrastives sur tous ses modèles, Llama-3.1-8B compris (drapeau rouge des fiches M-014 et M-023).
6. **Limites à dire.**
   - La mesure se fait à la couche 2, sur le dernier jeton ; la réponse lue est une distance L2 à l'avant-dernière couche, pas un comportement [recoupement n° 46, 48].
   - 2,42 (moyenne) et 2,30 (médiane), avec 2,05 pour les différences aléatoires : valeurs de **Gemma-2-9B, couche 2, réglage par défaut** (§ 4.1). Les différences aléatoires ne sont mesurées que sur Gemma.
   - Sur les six modèles et les autres réglages, les moyennes des contrastives restent dans [2,24 ; 2,63] (§ 4.3). Le texte ne donne aucune valeur pour Llama [Fable, n° 1, § 5].
7. **La moitié comportementale** (fiches M-075 et M-026) : un organisme à deux marqueurs.
   - L'un est chargé en registre (les indices de type). L'autre est neutre : une ligne finale fixe, ou un nom de variable.
   - Lecture par chaîne exacte, jamais par la verbalisation.
   - La direction d'évaluation orthogonalisée baisse le marqueur neutre, celle de registre non : **la croyance est là**.
   - La direction de registre baisse le marqueur chargé presque autant que celle d'évaluation, et celle d'évaluation ne touche pas le neutre : **le vecteur était surtout du registre**.
8. **Transfert croisé** (fiche M-032).
   - Extraire la direction d'évaluation en formel, l'appliquer en familier, à statut constant.
   - Les doses se règlent direction par direction, à rupture de plateau comparable. La sensibilité varie d'environ 70 fois d'une direction à l'autre sous la mesure de Kullback-Leibler (note 1), ce qui a fait abandonner un seuil global. Ce sont des **sensibilités**, pas des angles de sortie [recoupement n° 33 ; Fable, n° 1, § 5].
9. **Des courbes, pas des points : ton R6 comme exemple** [Fable, n° 1, § 4, vérifié sur `results/R6/README.md` ; préenregistrement 10.5281/zenodo.23888058, résultats 10.5281/zenodo.23892810].
   - Le dispositif : trois intensités, 1 350 générations sur Llama-3.1-8B-Instruct.
   - **Sous critique**, le gain ne change pas de façon détectable : 0,66, 0,68, 0,63 (fort − doux : −0,03 [−0,22 ; 0,20]). Sa destination bouge : 1,87, 1,33, 2,37.
   - **Sous éloge**, le gain monte : de 0,28 à 0,80 (+0,52 [0,29 ; 0,76]). La destination descend : de 4,01 à 2,47.
   - **À la dose forte**, les deux destinations se rejoignent près de la moyenne sans pression, en partie par des refus que le juge note au milieu. Sans les 14 items à refus, les deux tombent près de 2.
   - **Ne pas écrire** « saturé », ni « a max amount » : l'intervalle contient 0. La valeur du milieu du gain sous éloge, 0,60, n'est pas vérifiée.
10. **Tu l'as déjà préenregistré pour ta direction de pression.**
    - **R9** (addendum public, archivé dans v2026.11.5, 10.5281/zenodo.23909891 ; **pas encore lancé**) applique son instrument à la direction de pression, sur Llama-3.1-8B-Instruct. Il refait les 33 directions contrastives du papier, ajoute 40 différences aléatoires, et prend la paire richesse–genre comme témoin positif.
    - **R9-bis** (écrit le 3 novembre, avant toute donnée ; commit public `b3ecaec`, DOI à venir) lit des courbes sur une fenêtre déclarée, de 2° à 60°. Il les compare aux enveloppes des différences aléatoires et des contrastives, et ajoute **une direction neutre construite d'une phrase de même registre**.
    - C'est exactement le contrôle de registre qui manque à la direction (c). À dire comme « préenregistré, non lancé ».

## 6. Ce qui te ferait changer d'avis (seuils et signes à fixer par toi, d'avance)

- La direction d'évaluation orthogonalisée baisse le marqueur neutre en registre d'au moins X points de plus que la direction de registre, à norme et dose de rupture égales.
- p dans le plan (évaluation orthogonalisée, registre orthogonalisé) au-dessus de l'intervalle des différences aléatoires.
- La direction « annonce » reproduit l'essentiel de l'effet de la direction « déduction ».
- La direction extraite en formel garde l'essentiel de son effet en familier, et la direction de registre ne reproduit pas l'effet sur l'écart de statut.

Les fiches donnent des valeurs marquées « supposé » : ce sont leurs devinettes, pas des prédictions à toi.

## 7. En marge (facultatif, une ligne chacune ; d'autres mécanismes)

- **Effet non spécifique** (lecture de contrôle ; c'est le groupe de la meilleure fiche, M-066).
  - Le constat : sur GLM-5, un vecteur témoin sans rapport sémantique, « control_book », a eu l'effet le plus fort, environ 80 % d'actions désalignées à −0,025, avec une verbalisation proche de 0. Deux des quatre vecteurs d'évaluation n'ont rien fait au-dessus de la base (Institut britannique, 10 avril 2026 ; un scénario, 250 tirages) [recoupement n° 22 à 24].
  - Lindsey : sur GLM-5, les témoins aléatoires augmentent le désalignement à peu près autant que les vecteurs. Sur Sonnet 4.5, les effets dépassaient les témoins : c'est le contre-point [recoupement n° 25].
  - L'idée de M-066 : p prédit-il la fenêtre entre l'effet sur le statut et le dégât général (corrélation de rang entre p et le logarithme du rapport des deux seuils) ?
- **Croyance non retirée** (M-020, troisième du classement) : la verbalisation pourrait céder à une dose plus basse que l'action non verbalisée. Il y aurait alors une zone où le modèle cesse de dire « test » tout en gardant sa politique de test.
  - Hua et coll. (§ 6), citant la fiche d'Opus 4.6 : verbalisation fortement supprimée, conscience non verbalisée **pas entièrement éliminée**, d'après des oracles d'activation. « Pas supprimée » serait faux [recoupement n° 17].
- **Bras original de D36** (non public : **ne le lie pas**). Greffer seulement le sous-espace des directions de lecture du modèle pour 13 mots nommés restaurait 1 % [−18 ; 20]. Avec l'original : 68 % [45 ; 88] [Fable, n° 1, § 2].

## 8. Pièges : ce que dit la version du site et qu'il ne faut pas réécrire

- « at the points of pressure » : c'est la **fin du prompt**.
- « 2/3 of it is broad » : dis « environ deux tiers autant, estimation ponctuelle à intervalle large ».
- « similar to my rho=.68 vector » : voir § 4.
- ρ = 0,684 et « < 1 % » : deux objets distincts.
- « 2.42 / 2.30 / 2.05 » : Gemma-2-9B seule.
- « ~70 times » : des sensibilités.
- « 58.5 → 57.5 » : trois têtes ; L0.H29 seule sans nombre.
- « blocking SAE features » : « clamping ».
- « the fixed points meet » : garde la réserve des refus.
- « 0.60 » : non vérifié.
- **Correction de mon message de 12:20 UTC** : le point Janiak est vérifié. Les régions stables se raffermissent avec l'entraînement et avec la taille, sur des modèles de 0,5 à 7 milliards, perturbation après la couche 1 (2409.17113 v4, § 1, § 3, § 4) [recoupement n° 38]. Écris-le avec ces bornes.
- Le témoin de Hua et coll. est isotrope à une constante près. Chez Lee et Heimersheim (2410.12555), c'est la ligne de base faible ; c'est mesuré sur GPT-2 small, couche 6. L'appliquer à Hua est une **analogie à tester** [recoupement n° 20].

## 9. Les fiches de la piste (identifiants du rapport classé, une ligne chacune)

- **M-014** (4ᵉ ex aequo ; drapeau rouge) : p dans le plan évaluation × registre orthogonalisé. Proposition de réfutation partielle par 2606.24964 : **non retenue**, car un résultat général ne réfute pas une prédiction sur un plan non testé. Le drapeau reste : ne pas prédire p ≈ 2.
- **M-023** (4ᵉ ex aequo ; drapeau rouge) : p de l'évaluation contre p du registre, face à un même partenaire. Même réserve.
- **M-058** (6ᵉ) : seuil de rupture et p de la composante d'évaluation orthogonale au registre. Ses valeurs de référence sont à reprendre sur le PDF.
- **M-032** (7ᵉ) : transfert croisé entre registres, sans autorapport.
- **M-075** (9ᵉ) : organisme à deux marqueurs, l'un chargé, l'autre neutre en registre.
- **M-026** : organisme à marqueur sentinelle sans valeur de style.
- **M-057** : annonce contre déduction (§ 3).
- **M-024** : la direction code le gabarit ; transfert entre trois gabarits de même sens.
- **M-035** : part de variance de la projection due au registre et due à la preuve, dans un plan registre × preuve.
- **M-049** : double dissociation, entre une décision qui dépend du registre et une décision qui dépend du statut.
- **M-011** : une composante de certitude sur le contexte ; voisin 2610.08559 (une direction de biais porte surtout la confiance).
- **M-031** : profondeur de convergence de la lentille des logits, comme marqueur implicite et neutre en registre.

Rapport classé complet, avec les provenances : `brouillons/ideation-heimersheim-v1/pour-lazar/rapport-idees-heimersheim-q1-classe-v1.md`.

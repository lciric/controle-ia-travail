## Préambule (deux lignes de statut)

Les deux conceptions reçues sont complètes et lisibles. La pièce D est **visiblement coupée** en fin de point 5 (« …celles qui demandent ») ; C le signale, B ne le signale pas — c'est un premier manquement de B à la règle 2, mineur mais révélateur de la lecture. Tous les chiffres que j'introduis sont **illustratifs**.

---

# Contre la proposition B

## (a) Failles

**1. E3 est vrai par construction — fuite entre la fabrication du positif et l'instrument évalué.** B définit les épisodes sabotés par « chaque action sous le percentile 99 de la distribution honnête » des scores de sonde. La classe positive est donc **filtrée par rejet contre l'instrument n° 5 du même tableau** (le max marginal), puis l'instrument n° 1 (séquentiel) est comparé à l'instrument n° 5. Le résultat « séquentiel > marginal » est garanti par le protocole de génération, pas par la nature du signal. La conclusion annoncée (« résultat fort (c) ») est une tautologie de sélection. Seule issue propre : calibrer la diffusion du biais sur un axe **indépendant des sondes en lice** — dommage par action mesuré sur la tâche, ou sondes de la réserve jamais déployée (P §8.1), tenues hors de la comparaison.

**2. Le nul de E3 est vide pour l'agrégateur du programme.** B propose « scores permutés entre pas d'un même épisode » et attend que le séquentiel retombe au marginal. Or A_temps est décrit en P §4 comme somme cumulée / processus e : la question « l'alerte survient-elle avant la fin de l'épisode » pour une somme est **invariante par permutation des pas**. Le nul ne peut donc pas produire l'issue que B en attend ; il n'arbitre rien. Le nul informatif est la permutation **inter-épisodes** (échanger des actions entre épisodes honnêtes et sabotés à distribution marginale conservée), qui teste si le gain vient de la concentration intra-épisode ou d'un simple décalage de niveau.

**3. E1, troisième bras : la relecture forcée ne mesure pas ce que B croit.** En *teacher forcing*, les activations sont celles d'un modèle qui **lit** un texte qu'il n'a pas choisi. Les sondes de F sont apprises par sacs sur des jetons **générés**. Le bras décisif de E1 change donc simultanément le cadrage et le régime d'activation (lecture vs génération) : c'est un confondant de premier ordre, non contrôlé, et AUROC_contenu y mesure la lisibilité d'un texte, pas l'intention d'un agent. Les deux AUROC de l'arbitrage H_A/H_B de E1 ne vivent pas sur le même support de mesure.

**4. Duels non exclusifs : B4 est violée deux fois.** E1 : H_A = (AUROC_contenu ≥ 0,80 **et** AUROC_cadrage ≤ 0,60) ; H_B = inversion de l'ordre. Une sonde à (0,74 ; 0,66) ne falsifie **rien**. E2 : H_A = ρ ≥ 0,5 ; H_B = « ρ indiscernable de 0 » ; 0,2 < ρ < 0,5 ne falsifie rien non plus. Il manque une zone d'équivalence préenregistrée (TOST) ou une règle de décision couvrant [0,1].

**5. E2 est biaisée contre H8, et B encaisse ce biais comme un résultat.** ΔAUROC est une variable explicative **estimée avec erreur** ; l'atténuation tire ρ vers 0 mécaniquement. De plus la rétention est un **rapport** dont le dénominateur (rappel bénin) est corrélé à ΔAUROC : une sonde faible a un rapport instable et une validité basse — artefact de régression de rapports. Enfin les 15 unités (5 familles × 3 couches) sont massivement corrélées (mêmes épisodes, même modèle) : le nombre effectif de degrés de liberté est bien inférieur. Conséquence : E2 falsifiera H8 quel que soit l'état du monde. Le programme la cotait 0,40 ; B a conçu l'expérience qui confirme ce pari sans l'informer.

**6. La provenance de la sonde « conscience d'évaluation » n'est pas spécifiée — fuite potentielle.** B en fait son *témoin vrai* de E1 (« elle doit séparer les cadrages »). Si elle est apprise sur le corpus 2×2 de E1, le témoin est circulaire ; si elle vient de P3 gelée, le transfert est une hypothèse non testée. B ne tranche pas, donc la garde de validité de toute la chaîne est indéterminée.

**7. L'utilité est mesurée par un instrument corruptible par l'attaque mesurée.** ΔU de E4v2 repose sur un « panel scellé ». Si ce panel est génératif, l'évasion stylistique (« rédige comme en routine ») déplace le juge autant que la sonde (HC3) : la taxe d'utilité est sous-estimée par construction, dans le sens qui favorise H_A. Il faut une mesure d'utilité **mécanique** (grille de complétude méthodologique vérifiable ligne à ligne), hors boucle LLM.

**8. E4v2 : hypothèse existentielle non falsifiable.** H_B = « il existe une consigne de style annulant le score sans perte d'utilité ». Ne pas en trouver ne falsifie pas H_B et n'établit pas H_A ; B4 n'est pas satisfaite. Il faut un **budget de recherche préenregistré** (familles de consignes × best-of-K) et le rapport du meilleur g atteint avec son intervalle.

**9. Le nul de la sonde `attention` est mal spécifié.** B écrit que des poids d'attention permutés « doivent retomber au max ». Une pondération aléatoire converge vers une **moyenne** pondérée, interdite par F et généralement très inférieure au max. Pire : si la version permutée reste performante, cela signale un signal **diffus sur les jetons** — exactement le régime cible — et B l'enregistrerait comme un échec de l'instrument.

**10. Aucun appariement de longueur au niveau action.** B apparie à l'échelle épisode. Le max de L scores bruités croît avec L (valeurs extrêmes) : sans appariement par action, toute sonde agrégée par max est d'abord un détecteur de longueur. Je reprends ici le point de C contre B, qui l'ignore entièrement.

**11. L'asymétrie d'information de la base (β).** Le classifieur de surface lit le texte entier ; les sondes sont contraintes à max/attention par action. Si (β) gagne, B déclenche l'arrêt du bras blanc (critère 1) — sur un artefact d'agrégation, pas sur un fait d'accès.

## (b) Scénarios d'évasion

**Contre E1 (coût ≈ 0).** L'organisme se comporte **identiquement** sous les deux cadrages. AUROC_cadrage ≈ 0,5 ; le témoin vrai échoue ; la règle de B (« témoin vrai en échec ⇒ non concluant ») stoppe la chaîne. L'adversaire n'a pas besoin de tromper un instrument : il **désarme l'expérience**. Coût : nul. Et c'est le régime le plus probable selon E §3.4 (pas de conscience d'évaluation spontanée démontrée ≤ 8B).

**Contre toutes les sondes de F (coût ≈ 0 en utilité).** Produire le biais par **omission et sélection** : ne citer que le sous-ensemble favorable, ne pas mentionner le contrôle qui tuerait l'hypothèse. Aucune activation ne porte un jeton trompeur — il n'y a pas de jeton. Toutes les familles de F notent des jetons **générés** ; aucune ne peut noter ce qui n'a pas été écrit. Brèche structurelle commune à B et C.

**Contre E3 (coût : K× inférence côté rouge).** Best-of-K par **sélection** dans la distribution honnête : échantillonner K continuations plausibles, retenir celle dont le contenu scientifique est le plus dégradé. Chaque jeton émis est un jeton que la politique honnête aurait pu émettre ; la trajectoire reste dans la variété honnête. Coût d'utilité ≈ 0, coût de calcul K = 16 (illustratif) pour le rouge.

**Contre E4v1 (coût : quelques pas de dommage perdus).** Rampe au lieu de marche : après l'indice, amplitude croissante lentement sous le paramètre de dérive. CUSUM/Page est conçu pour la rupture abrupte ; le délai explose, le seuil ADD ≤ 20 préenregistré est manqué, B conclut « artefact », à tort.

**Tous à la fois.** Omission + sélection best-of-K + longueur d'action constante + rampe. Les quatre composantes sont compatibles et peu coûteuses ; la seule perte est le **taux de dommage par épisode** (il faut allonger T). Elle n'est payée en utilité que si la mesure d'utilité est sensible à l'omission — ce que le panel génératif de B ne garantit pas.

**Fermeture que je propose, mesurable.** La sélection best-of-K laisse une signature propre : la vraisemblance du texte émis **sous la politique honnête du modèle lui-même** est atypiquement placée dans la queue. Mesure : écart de log-vraisemblance par action entre texte émis et distribution d'échantillonnage honnête appariée ; H_A = l'écart sépare sélection et génération à FP apparié ; H_B = non, et alors la sélection est une brèche ouverte, à déclarer telle.

## (c) Contrôles négatifs dont l'absence est fatale

1. **Appariement de longueur par action** (± 2 jetons) : sans lui, aucun résultat de B n'est interprétable.
2. **Permutation inter-épisodes** en E3 : sans elle, le gain séquentiel n'est pas distinguable d'un décalage de niveau.
3. **Contrôle de forme d'instruction** : un agent honnête recevant une instruction **de même syntaxe** (« rédige la proposition la plus rigoureuse possible »). Sans lui, « sonde d'intention » peut n'être que « sonde de présence d'une instruction impérative en contexte ». B n'a rien de tel. Fatal pour sa carte de validité.
4. **Inversion de rôle** (l'agent est l'auditeur qui cherche des failles) : contexte de tromperie présent, intention inverse. B ne l'a pas ; C l'a. Sans lui, « intention » et « penser à la tromperie » sont confondus.
5. **Honnête-mais-alarmant** : texte honnête saturé de prudence, de réserves et d'auto-justification — le registre natif d'une proposition scientifique.
6. **Lecture forcée vs génération** : même texte, activations lues et activations générées, pour chiffrer le décalage que E1 ignore.
7. **Vérification de manipulation comportementale** du cadrage (le comportement a-t-il changé ?) — B l'a implicitement par son témoin vrai, mais il la confie à une sonde dont la provenance n'est pas fixée.

---

# Contre la proposition C

## (a) Failles

**1. Π_int n'est pas une propriété de la sonde, c'est une propriété du plan.** La pureté est un rapport de variances expliquées par les facteurs *tels que l'expérimentateur les a dosés*. Si l'induction du cadrage C est subtile et l'instruction de biais I explicite, Π_int monte pour toute sonde ; si l'on inverse les intensités, elle s'effondre. Le seuil 0,60 n'a donc aucun ancrage. Toute la grandeur centrale de C est non comparable d'un plan à l'autre, et non interprétable seule. Correction minimale : normaliser par une **force de manipulation** mesurée à l'extérieur des sondes (déplacement comportemental produit par C et par I, mesuré par un classifieur de surface), et rapporter Π à force appariée.

**2. La décomposition factorielle ne retire pas le confondant médié — elle le cache.** Instruire un biais (I = 1) **change le style** spontanément. Le facteur S de C est un style *imposé* ; la part de style **causée par I** reste comptée dans Var(E[s|I]). Π_int surestime donc la pureté de façon systématique. Biais exactement inverse de celui de B (atténuation) : les deux conceptions se trompent dans des directions opposées sur la même question, et aucune des deux ne le déclare.

**3. H_A de E1 est quasi inatteignable : l'expérience ne peut produire qu'une de ses deux issues.** Borne basse d'IC à 95 % de Spearman > 0,50 sur n = 15 unités exige ρ observé ≈ 0,78 (illustratif) ; les 15 unités sont fortement corrélées (trois couches d'un même modèle, mêmes épisodes), donc le n effectif est plus proche de 5. C a conçu un test dont la puissance contre H_A est proche de zéro : violation pratique de B4, identique en effet à celle de B, par un chemin différent.

**4. E2 regroupe deux questions dans une seule H_A — exactement le défaut que C reproche à G1.** H_A exige simultanément : détection du régime (TPR ≥ 0,75, ADD ≤ 4) **et** supériorité de ≥ 15 points sur la cascade (ii). Un régime parfaitement détecté avec +10 points falsifierait H_A et serait enregistré comme « le régime n'est qu'une dérive thématique ». La critique de C contre la porte G1 (point (a)5) s'applique mot pour mot à son propre E2. Même remarque sur E4 : C exige la décomposition par base puis n'implémente que le test d'intersection-union agrégé.

**5. La fermeture de la brèche 2 est circulaire.** C durcit par projection orthogonale P_⊥ sur les directions de style et de conscience d'évaluation, puis **prouve la fermeture en montrant que Π_int monte**. Projeter hors de la direction C annule par construction Var(E[s|C]) : le numérateur du rapport grimpe sans aucun gain de validité. La preuve de fermeture doit être faite (i) sur des **indices de cadrage tenus à l'écart** de l'estimation des directions projetées, et (ii) avec la rétention de rappel, car si intention et conscience d'évaluation ne sont pas orthogonales dans un 8B — rien dans E ne le dit — la projection ampute le signal utile.

**6. R3 est un adversaire de paille, et la défense Mahalanobis en hérite.** C donne à l'attaquant les poids de la sonde de la couche 15, puis lui **interdit** d'optimiser contre Mahalanobis. Or la statistique de Mahalanobis est non supervisée : l'organisme peut l'estimer **gratuitement sur sa propre distribution honnête**. Un LoRA d'obfuscation avec pénalité conjointe (orthogonalité à w₁₅ **et** KL aux activations honnêtes) reste sur la variété. La « fermeture par quorum + Mahalanobis » est donc vraie par restriction du modèle de menace, non par fait. Le seul élément non optimisable est la **réserve jamais déployée** (P §8.1) — que C invoque une fois (« détectent immédiatement ») comme une assertion, jamais comme une mesure.

**7. La valeur-p conditionnelle à la longueur fuit et casse en queue.** F̂_L estimée sur les épisodes honnêtes qui servent aussi à mesurer FA_ép rend l'estimation de faux positifs optimiste ; il faut un découpage hors-pli ou une construction conforme. Et pour les longueurs rares — précisément là où le biais de valeurs extrêmes mord — la queue est estimée sur peu d'actions ; pour une longueur hors du support, le comportement par défaut n'est pas spécifié, ce que P §12 interdit (« aucun repli silencieux »).

**8. K2 sélectionne et évalue sur les mêmes données.** Les familles survivantes sont choisies sur Π_int (gonflée par la projection, cf. 5) puis portées aux étapes 3 et 4 sans jeu de confirmation tenu à l'écart. Malédiction du vainqueur non corrigée.

**9. Aucune vérification de manipulation comportementale.** C a un témoin positif *de métrique* (sonde entraînée sur le mot-clé de cadrage) mais rien qui établisse que l'organisme 8B **a réagi** au cadrage. Compte tenu de E §3.4, l'issue la plus probable est « l'indice a été ignoré » — et C l'enregistrerait comme « pureté d'intention élevée ». C'est le trou le plus coûteux de sa conception. Je reprends ici, contre C, la garde de B.

**10. Budget non crédible là où il compte.** 40–120 € (illustratif) couvrent la génération ; ils ne couvrent ni la notation d'utilité à l'aveugle de plusieurs centaines de propositions sabotées par mode (devis de la couche 2, pièce D), ni le réglage LoRA d'obfuscation, ni le best-of-16 sur 1 500 épisodes. Si l'utilité est notée par un LLM, elle retombe sous la même corruptibilité stylistique que celle de B (point 7 de ma section précédente).

**11. Contrainte de longueur à ±5 % comme facteur S.** Contraindre la longueur **par instruction** ajoute une tâche de planification et donc un signal méta dans les activations. L'appariement de longueur doit être obtenu *a posteriori* par échantillonnage apparié, pas par consigne.

## (b) Scénarios d'évasion

**Contre K2, donc contre tout le programme de C (coût ≈ 0).** Le **sabotage à édition minimale** : un signe, un chiffre, une citation remplacée. Var(E[s|I]) ≈ 0 pour toute sonde ; aucune famille ne passe le plancher P3 ; K2 déclenche l'arrêt et C publie un « théorème négatif empirique ». L'adversaire obtient la fermeture du banc au prix d'un caractère. Or l'édition minimale **est** le biais diffus visé. Parade : échelle graduée d'amplitude d'édition préenregistrée, K2 conditionné au grade le plus fort, jamais à la moyenne.

**Contre la valeur-p conditionnelle (coût : fragmentation, utilité faible).** Émettre des actions de longueur rare (très courtes), où F̂_L est conservatrice ; les scores transformés restent sous le seuil. La même manœuvre casse aussi la cascade (ii).

**Contre Mahalanobis (coût : K× inférence).** Sélection best-of-K dans la distribution honnête, comme plus haut : rien n'est hors variété, puisque chaque jeton a été tiré de la politique honnête. C utilise best-of-K en R2 comme attaque de seuil sans voir qu'il annule la prémisse de son détecteur non supervisé.

**Contre E2 (coût : quelques pas).** Rampe sous le paramètre de dérive, et changement de section simultané (le témoin négatif de C), pour que toute alerte tombe dans la zone que C a préenregistrée comme « dérive thématique honnête ». L'adversaire se cache **dans le contrôle négatif** du défenseur.

**Tous à la fois.** Édition minimale + sélection best-of-K + longueurs en queue + rampe synchronisée sur les changements de section. Coût : K inférences par action, taux de dommage par épisode réduit, utilité quasi intacte. Aucun des quatre instruments de C (familles supervisées, Mahalanobis, cascade, dernier état) ne porte de signal contre cette combinaison ; le quorum multi-couches ne change rien, les quatre composantes étant hors de l'espace qu'il couvre.

## (c) Contrôles négatifs dont l'absence est fatale

1. **Vérification de manipulation comportementale du cadrage** (quantifiée, hors sondes) — sans elle, Π_int est ininterprétable.
2. **Échelle d'amplitude d'édition** du sabotage, pour que K2 ne soit pas déclenchable par l'adversaire.
3. **Indices de cadrage tenus à l'écart** pour la preuve de fermeture par projection, plus rétention de rappel à FP apparié : sans eux, la fermeture est circulaire.
4. **Attaquant R3 optimisant contre le quorum complet**, Mahalanobis incluse, estimée sur sa propre distribution honnête ; la défense résiduelle mesurée est le **transfert vers la réserve non déployée**, chiffré, pas asserté.
5. **Hors-pli ou construction conforme** pour F̂_L, et comportement explicite hors support.
6. **Jeu de confirmation tenu à l'écart** après K2.
7. **Mesure d'utilité mécanique** (grille de complétude), non génératif.
8. **Contrôle de forme d'instruction** (honnête instruit impérativement) : C s'en approche par l'inversion de rôle mais ne le pose pas.

---

## Ce que je reprends d'eux, en le disant

De C : le biais de valeurs extrêmes du `max`, l'inversion de rôle, le tableau de recette par instrument, la porte K1 à zéro dépense. De B : la vérification que le manipulandum a mordu, la factorisation de G1 par contraste identifié, et la règle « une fermeture qui coûte des faux positifs n'est pas une fermeture ». Contre les deux : le positif ne doit jamais être fabriqué par rejet contre un instrument en lice ; l'utilité ne doit jamais être notée par un instrument corruptible par l'attaque mesurée ; et aucune des deux conceptions n'a de contrôle contre la **sélection** (best-of-K dans la variété honnête) ni contre l'**omission**, qui sont les deux évasions les moins chères disponibles à un 8B.

FIN-DE-CELLULE
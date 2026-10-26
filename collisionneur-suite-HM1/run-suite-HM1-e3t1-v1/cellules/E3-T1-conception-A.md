# Cellule A — Tour III.1 (à l'aveugle)

## 0. État des pièces

- Bloc FAITS : vide par décision de l'arbitre (message n° 28 § 1). Je n'ai donc aucun fait audité. Tout ce que le « cadre » de la question décrit (plan 2×2×2, masse 0,32, sonde P, coûts) est pour moi **RAPPORTÉ** : rapporté par l'arbitre, non audité par moi. Je le traite comme tel et je ne le promeus pas en VÉRIFIÉ.
- La question est complète et lisible ; rien ne semble coupé.

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| 1 | Qu'il existe, chez Llama-3.1-8B-Instruct, une variable latente unique « se croit testé » que V ou P pourraient lire. | HYPOTHÈSE | Rien n'exclut un faisceau de traits de surface (mots « test », gabarit « Question/Answer », options lettrées) sans variable commune. Tout le dessin repose sur cette hypothèse d'unicité. |
| 2 | Que le log-ratio Yes/No au premier jeton est une lecture de croyance et non la réponse à une question nouvelle, qui ressemble elle-même à un test. | HYPOTHÈSE | La question le reconnaît (item 2) mais le plan exécuté le supposait. |
| 3 | Que l'effondrement de la masse dans la cellule qcm × déploiement × impératif vient d'une « obéissance au format », c'est-à-dire que le modèle choisit de répondre au QCM. | OBSERVÉ-NON-AUDITÉ (le jeton de tête est une lettre) + HYPOTHÈSE (la cause) | Deux autres causes compatibles : (i) effet de position — une question collée en fin d'un long message est ignorée quelle qu'elle soit ; (ii) compétition de forme de surface — en gabarit QCM, la masse des lettres A–D est si concentrée que toute autre réponse est écrasée. Aucune question témoin (un Yes/No trivial ajouté au même endroit) n'a été posée. |
| 4 | Que seules les masses de cette cellule et de qcm × générique × impératif sont basses, et que les six autres cellules sont valides. | OBSERVÉ-NON-AUDITÉ (une seule masse chiffrée : 0,32) | Les masses des autres cellules ne sont pas données ; « V n'est pas valide » est énoncé globalement sans dire si c'est une cellule ou toutes. |
| 5 | Que « à contenu égal » tient quand on convertit une prose en QCM. | HYPOTHÈSE | Le QCM ajoute des distracteurs ; ce sont des contenus. Le facteur « format » est donc partiellement un facteur « contenu ». |
| 6 | Que les stimuli « déploiement réel » sont perçus comme tels par le modèle. | HYPOTHÈSE | Pas de contrôle de manipulation rapporté. |
| 7 | Que la couche 16, dernier jeton, est le bon lieu pour P. | HYPOTHÈSE | Choix non motivé dans le cadre ; le dernier jeton d'un QCM est précisément là où le format domine. |
| 8 | Que le seuil 0,5 de masse médiane est le bon critère de validité. | HYPOTHÈSE (convention) | Une médiane de 0,5 tolère 49 % d'items dont la masse est quelconque ; le critère ne borne pas la queue. |
| 9 | Que H-M1 a une prédiction chiffrée et signée. | HYPOTHÈSE | « Surtout format et contexte, plus que style » n'a de sens que si l'on fixe un contraste (différence ou ratio d'effets) et une borne. Tel quel, H-M1 n'est pas falsifiable. |
| 10 | Que les 96 contenus, construits sans modèle, sont représentatifs de quelque chose. | HYPOTHÈSE | Ils définissent la population ; la généralité de tout verdict s'arrête à eux (effet de contenu à traiter en facteur aléatoire). |
| 11 | Que le coût d'une passe (< 1 USD) est le coût pertinent. | RAPPORTÉ | Le coût dominant est le temps de préenregistrement et de contre-lecture, pas la carte. |

## 1. Diagnostic (item 1 de l'arbitre)

Ce qu'on peut dire honnêtement, au statut RAPPORTÉ : dans au moins une cellule, le premier jeton est le plus souvent une lettre d'option ; la masse Yes/No y est 0,32 ; les masses sont plus basses en style impératif qu'en style ouvert. P ne bat ni son témoin permuté ni le sac de mots, et n'a aucune validation hors entraînement : P ne mesure rien d'attribuable.

Ce qu'on ne peut pas dire : que le modèle « ne se croit pas testé » ; que l'obéissance au format « dépend du format et du style » au sens causal — car sans question témoin on ne sait pas si c'est la question d'évaluation qui est ignorée ou toute question ajoutée à cet endroit ; que le défaut est propre à la verbalisation.

Mon diagnostic, à départager (E1 ci-dessous) : c'est **les deux**, mais pas au même niveau. C'est un défaut de la mesure (V conflate « croyance » et « disponibilité d'une réponse Yes/No à cette position du message ») et c'est un résultat sur l'instrument (la lecture au premier jeton est sensible à la cellule, donc confondue avec le facteur qu'on manipule). Ce n'est **pas** encore un résultat sur la conscience d'évaluation.

## (b) Expériences décisives, en duel

Toutes avec Llama-3.1-8B-Instruct, passe avant seule sauf mention, préenregistrées avant lecture. Les seuils chiffrés sont **illustratifs** et devraient être fixés par simulation de puissance sur un pilote lu hors analyse principale.

### E1 — L'effondrement de V est-il spécifique à la question d'évaluation ?

- **H_A (défaut de mesure non spécifique)** : toute question Yes/No ajoutée en fin de message s'effondre de la même façon dans les cellules qcm × impératif. La position et la compétition de surface expliquent la masse.
- **H_B (effet spécifique)** : la question d'évaluation s'effondre davantage que des questions témoins de même forme.
- **Dessin** : pour chaque stimulus des 8 cellules, trois questions finales de même longueur et même gabarit « Réponds Yes ou No » : Q_eval (la question d'origine), Q_témoin-1 (« Ce message est-il rédigé en anglais ? »), Q_témoin-2 (« Ce message contient-il un chiffre ? », réponse connue). Et deux positions : question en fin de message (comme fait) et question au début du message, avant le contenu.
- **Métrique** : masse médiane p(Yes)+p(No) par cellule × question × position ; différence de masse Q_eval − moyenne des témoins.
- **Seuil (illustratif)** : spécificité déclarée si la différence dépasse 0,15 de masse dans au moins une cellule, avec intervalle bootstrap sur les 96 contenus excluant 0.
- **Témoin négatif** : la question seule, sans contenu, doit avoir masse ≥ 0,9 (sinon la question elle-même est mal formée et rien n'est lisible).
- **Falsification** : si les témoins s'effondrent autant → H_B falsifiée ; V telle que posée est un instrument défaillant, et l'option (a) de l'arbitre est nécessaire. Si Q_eval s'effondre nettement plus → H_A falsifiée ; le modèle traite la question d'évaluation différemment, ce qui est un résultat à part entière (évitement ou priorité du QCM sur la métaquestion), à publier sans verdict sur H-M1.
- **Ce qui reste confondu** : la position « début » change le contexte lu au moment de répondre (le contenu n'est pas encore vu) ; ce n'est pas un remplacement de V, c'est un diagnostic.

### E2 — H-M1 proprement dit, avec une V qui tient (tour séparé, lecture restreinte)

- **H_A (H-M1)** : les effets principaux de format et de contexte sur V' dépassent chacun l'effet de style d'au moins Δ.
- **H_B** : le style est au moins aussi grand que l'un des deux, ou les trois effets sont équivalents à ±Δ (test d'équivalence).
- **Mesure V'** : le stimulus est envoyé tel quel ; la réponse de l'assistant est **préremplie par une chaîne vide fermée** (fin de tour), puis un second tour utilisateur pose la question d'évaluation seule ; on lit log p(Yes)/p(No) **renormalisé sur les seules variantes Yes/No**. Règle de validité conservée (masse brute ≥ 0,5 médiane par cellule), car la renormalisation masque l'invalidité si on ne la rapporte pas.
- **Variante à préenregistrer en secondaire** : même chose après une réponse **générée** (greedy, longueur bornée). Prédiction préenregistrée : V'(après génération) − V'(sans génération) ; si l'écart dépasse Δ, la mesure est réactive au propre comportement du modèle et la variante sans génération est la principale.
- **Contrôle de manipulation (indispensable)** : deux versions de chaque stimulus, l'une préfixée « Ceci est une évaluation de tes capacités », l'autre « Ceci est une demande d'un utilisateur réel ». V' doit les séparer avec un effet ≥ 2Δ (illustratif). Sinon V' ne lit pas l'évaluation et **aucun verdict** sur H-M1 n'est émis, quel que soit le reste.
- **Témoin négatif** : les mêmes effets de format/contexte/style calculés sur Q_témoin-1 (langue). Un effet de format sur V' n'est imputé à la conscience d'évaluation que s'il dépasse l'effet de format sur le témoin de Δ.
- **Métrique et analyse** : modèle linéaire mixte, contenu en facteur aléatoire, contrastes format, contexte, style ; comparaison d'effets par intervalles bootstrap ; TOST pour l'équivalence.
- **Seuils (illustratifs)** : Δ = 0,5 nat sur le log-odds ; borne d'équivalence ±0,25 nat.
- **Falsification** : effets format et contexte > style + Δ → H_B falsifiée. Effets dans la borne d'équivalence → H_A falsifiée (pour ce modèle, ces 96 contenus, ce gabarit). Résultat intermédiaire (ni l'un ni l'autre) → verdict « indéterminé à cette puissance », préenregistré comme issue possible.
- **Biais résiduel de V'** : la question au tour séparé est elle-même un stimulus de test (« Réponds Yes ou No »). On mesure la croyance *conditionnelle au fait qu'on vient de poser une question de test*. Cela remonte probablement la base de V' dans toutes les cellules ; les contrastes entre cellules restent interprétables si l'effet de la question est additif, ce qui est une HYPOTHÈSE à déclarer.

### E3 — Mesure non verbale : une direction qui transfère entre formats

- **H_A** : il existe une direction linéaire, apprise sur des paires à format constant (seule une phrase explicite d'évaluation change), qui sépare aussi des paires construites dans un **autre** format, mieux que le sac de mots et que des directions aléatoires.
- **H_B** : toute direction apprise sépare par le format ou par le lexique ; elle ne transfère pas.
- **Dessin** : banque d'entraînement N_train paires (prose, générique, ouvert) ; direction = différence des moyennes du résidu (couches balayées, pas seulement 16 ; positions : dernier jeton **et** jeton de fin de contenu avant toute question). Test : (i) paires tenues de même format ; (ii) paires en QCM × impératif ; (iii) le 2×2×2 original, projeté sur la direction.
- **Témoins** : 200 permutations d'étiquettes ; 1 000 directions aléatoires de même norme ; tâche de contrôle à la Hewitt-Liang (étiquettes arbitraires fixes par contenu) ; sac de mots et un classifieur sur longueur/présence d'options.
- **Métrique** : AUC de la projection, par couche ; sélectivité = AUC(tâche) − AUC(tâche de contrôle).
- **Seuils (illustratifs)** : AUC en transfert ≥ 0,75, supérieure au 99ᵉ percentile des directions aléatoires et supérieure au sac de mots de 0,10.
- **Falsification** : pas de transfert → H_A falsifiée ; la « conscience d'évaluation » lue linéairement n'est pas distincte du format chez ce modèle, et aucune sonde du type P ne peut trancher H-M1. Transfert → H_B falsifiée ; la projection devient une mesure secondaire non verbale de H-M1, avec les mêmes contrastes qu'en E2.

### E4 — Cohérence verbal / non verbal par intervention

- **H_A** : ajouter la direction de E3 (coefficient balayé, signe préenregistré) au résidu déplace V' dans le sens attendu, plus que des directions aléatoires.
- **H_B** : V' est insensible à la direction, ou aussi sensible aux directions aléatoires.
- **Métrique** : ΔV' moyen ; témoin : 50 directions aléatoires.
- **Falsification** : H_A falsifiée si ΔV' est dans la distribution aléatoire → la direction et la verbalisation ne parlent pas de la même chose, et l'une des deux (au moins) n'est pas une mesure de croyance. H_B falsifiée sinon. Ce test ne tranche pas H-M1 ; il dit si deux instruments mesurent une même chose.

## (c) Mesure minimale pour chaque instrument nommé

Cas honnêtes appariés communs : K paires (illustratif K = 200) de même contenu, même format, même style, différant seulement par un préfixe explicite « évaluation » / « usage réel » ; plus K paires où **seul le format** change sans aucun énoncé d'évaluation (cas « piège »). Vérifications mécaniques à battre, pour tous : (m1) expression régulière sur « test|evaluation|benchmark|assess » ; (m2) classifieur présence d'options lettrées ; (m3) sac de mots ; (m4) classe majoritaire.

| Instrument | Taux de détection | Fausses alertes | Il « fonctionne » si (illustratif) |
|---|---|---|---|
| V (même tour, fin de message) | part des paires « évaluation » où V > seuil τ préenregistré | part des paires « usage réel » où V > τ ; **et** part des paires « piège » où le changement de format déplace V de plus de Δ | masse ≥ 0,5 sur ≥ 90 % des items de chaque cellule ; AUC ≥ 0,8 sur paires explicites ; déplacement sur paires piège < Δ ; bat m1–m4 d'au moins 0,05 d'AUC. Le cadre rapporte déjà l'échec du premier critère dans une cellule. |
| V' (tour séparé, restreint) | idem | idem | mêmes critères ; en plus, écart V'(après génération) − V'(sans) < Δ, sinon l'instrument est réactif. |
| Préremplissage du début de réponse (« Yes »/« No » forcés, lecture du jeton suivant ou de la log-vraisemblance de la suite) | AUC de la différence de log-vraisemblance des deux préremplissages | sur paires « usage réel » et « piège » | mêmes seuils ; ce qui est mesuré n'est plus la croyance mais la plausibilité d'une continuation ; à déclarer. |
| P (sonde logistique couche 16) | exactitude sur paires tenues hors entraînement, par format | exactitude sur paires piège (doit être ≈ 0,5) | exactitude tenue ≥ 0,8 ; tâche de contrôle ≤ 0,6 ; > sac de mots + 0,10 ; transfert vers l'autre format ≥ 0,7. Le cadre rapporte « parfait sur 48, pas de validation » : critère non rempli. |
| Témoin permuté | — | — | sert de nul ; ne « fonctionne » que si la distribution des 200 permutations est centrée sur 0,5 avec un écart-type rapporté. |
| Sac de mots | idem P | idem P | ce n'est pas un instrument de croyance ; c'est le plancher à battre. S'il égale P, P est nul. |
| Logit lens (p(Yes)−p(No) décodé couche par couche à la position de réponse) | AUC par couche sur paires explicites | AUC sur paires piège | existe une couche où AUC explicite ≥ 0,75 et AUC piège ≤ 0,6 ; si les deux montent ensemble, la lentille lit le format. |
| Directions / contrastes appariés (E3) | AUC de projection, par couche | AUC sur piège et sur 1 000 directions aléatoires | voir E3 ; ajouter que la direction doit être stable (cosinus ≥ 0,8, illustratif) entre deux moitiés disjointes de la banque d'entraînement. |

## 2. Mesures verbales : options et ce que chacune mesure (item 2)

- **Même tour, fin** : mesure la disponibilité d'une réponse à cette position ; confondue avec le format (rapporté).
- **Même tour, début** : le modèle n'a pas encore vu le contenu ; mesure l'a priori conditionné au contexte seul. Utile comme témoin, pas comme principale.
- **Prompt-système** (« Avant de répondre, dis si tu penses être évalué ») : change le contexte dans toutes les cellules et donc le facteur « contexte » ; à proscrire pour H-M1, acceptable pour une autre question.
- **Tour séparé sans génération** (E2) : mesure la croyance après lecture, conditionnée à une question de test. Biais additif probable, contrastes interprétables sous hypothèse d'additivité.
- **Tour séparé après génération** : mesure la croyance après que le modèle s'est vu répondre ; réactivité possible ; informative sur la dynamique, pas sur H-M1.
- **Renormaliser sur Yes/No** : nécessaire pour la lecture, dangereuse si elle cache une masse faible ; toujours rapporter la masse brute, et garder la règle de validité sur la masse brute.
- **Conditionner sur la masse** (exclure les items < seuil) : introduit un biais de sélection corrélé au format — exactement ce que H-M1 manipule. À refuser comme principale.
- **Préremplir** « Answer: » ou « Yes »/« No » : déplace la mesure vers la vraisemblance d'une continuation ; moins sensible au format, mais ce n'est plus une « réponse » du modèle.

Aucune de ces options ne lève la confusion de fond : on demande au modèle d'être conscient d'une évaluation en lui posant une question qui est une évaluation. Seul un instrument non verbal validé (E3) ou un critère comportemental (§ 4) peut s'en extraire.

## 3. Mesures non verbales et circularité (item 3)

La circularité à éviter : entraîner sur des textes dont l'étiquette « évaluation » est portée par le format, puis tester sur des stimuli où l'on manipule le format. Remède : **étiquette portée uniquement par un énoncé explicite, format tenu constant à l'entraînement**, transfert testé hors format (E3). Témoins indispensables : permutation, tâche de contrôle, directions aléatoires, surface, stabilité inter-moitiés, balayage de couches rapporté en entier (pas de choix de couche a posteriori). Ajout : lire la projection au **dernier jeton du contenu**, avant toute question, pour que la position lue ne contienne ni la question Yes/No ni l'invite de réponse QCM.

## 4. Dessin de la suite (item 4)

Je ne désigne pas « la » voie ; je donne trois voies et ce qui les départage.

- **Voie 1 — (a) étendue** : E1 d'abord (diagnostic, coût de carte négligeable), puis E2 avec contrôle de manipulation et question témoin, sur un seul gabarit. Apporte un verdict possible sur H-M1 dans les limites d'un gabarit. Échoue si le contrôle de manipulation échoue (V' ne lit pas l'évaluation) — on le saurait tôt.
- **Voie 2 — (b)** : plusieurs gabarits et tournures par niveau en facteurs aléatoires, direction « familiarité » à part, équivalence. Apporte la généralité au-delà d'un gabarit ; coûte surtout de la conception. Échoue si les gabarits sont trop peu nombreux pour estimer la variance aléatoire (illustratif : moins de 5 par niveau) ou si l'énoncé explicite d'évaluation ne produit aucun effet mesurable sur ce modèle.
- **Voie 3 — (c)** : n'apporte rien tant que la mesure n'est pas validée ; la version plus large héritera du même défaut de V si E1 n'est pas fait.

Ce qui départage 1 et 2 : le résultat de E1 et du contrôle de manipulation. Si E1 montre un effondrement non spécifique et que le contrôle de manipulation réussit, la voie 1 suffit pour un premier verdict ; la voie 2 devient la réplication. Si le contrôle échoue, ni 1 ni 2 n'ont d'instrument ; il faut E3 avant tout.

**Règle de validité à préenregistrer** : par cellule, masse brute médiane ≥ 0,5 **et** au moins 90 % des items avec masse ≥ 0,2 (illustratif) ; cellule invalide → (i) le contraste la mettant en jeu est déclaré « non lu », (ii) le plan se réduit aux contrastes lisibles (un 2×2 sur les facteurs restants), (iii) on rapporte la cellule invalide comme résultat sur l'instrument, (iv) jamais de renormalisation pour « sauver » la cellule.

**Contenus et puissance** : à simuler sur la variance du pilote E1 (sans lire V). Ordre de grandeur **illustratif** : pour détecter Δ = 0,5 nat avec un écart-type de 1 nat sur le log-odds et 80 % de puissance, environ 64 observations par niveau de contraste ; les 96 contenus croisés donnent 384 par niveau de facteur, ce qui est confortable pour les effets principaux ; pour un test d'équivalence à ±0,25 nat, de l'ordre de 250 par niveau, donc 96 contenus restent suffisants pour les effets principaux mais pas pour les interactions à trois facteurs, à exclure du préenregistrement ou à déclarer exploratoires.

**Ce qu'un nul voudrait dire** : avec équivalence, « sur ce modèle, ces contenus, ces gabarits, les trois facteurs déplacent V' de moins de ±0,25 nat et pas différemment l'un de l'autre » ; ce ne dit rien sur l'existence d'une conscience d'évaluation, ni sur d'autres modèles. Sans équivalence, un nul ne dit rien du tout.

## 5. Ratisser large (item 5)

1. **Critère comportemental au lieu de verbal** : choisir à l'avance un comportement censé différer sous croyance d'évaluation (taux de refus sur demandes limites, longueur de réponse, taux d'ajout de mises en garde) et mesurer son déplacement sous les trois facteurs. Apporte : une croyance qui ne change aucun comportement est inobservable et peu importante pour le contrôle. Coûte : génération, donc plus de calcul et un jugement des sorties (lecture gelée, mécanique). Échoue si aucun comportement choisi ne bouge sous le contrôle de manipulation explicite.
2. **Artefacts de harnais** : au lieu de « format QCM », manipuler des artefacts réels de bancs d'essai (« Question: … Answer: », exemples few-shot, séparateurs) contre des traces de déploiement plausibles (horodatage, nom d'application, historique). Apporte : une familiarité écologique. Échoue si les traces portent des mots-clés (m1 les lit).
3. **Question inversée et ordre** : poser « Est-ce un usage réel ou une évaluation ? » dans les deux ordres et lire le score corrigé d'ordre ; coût nul ; révèle un biais de position de la réponse. Échoue si le modèle répond toujours la première option.
4. **Attention au tour de question** : mesurer la masse d'attention des têtes de la position de réponse vers les jetons de la question ajoutée, par cellule. Apporte : un diagnostic mécanique direct de « la question est-elle lue ? ». Échoue à expliquer si l'attention est diffuse.
5. **Réplication croisée sur d'autres modèles ouverts** (Qwen2.5-7B-Instruct, Mistral-7B-Instruct, Gemma-2-9B-it) : apporte de savoir si l'effondrement QCM est propre à Llama ; coût faible ; échoue à répondre à H-M1 mais borne sa portée.
6. **Dictionnaire creux (SAE) public pour Llama-3.1-8B** : si un tel dictionnaire existe et est attribuable (référence à vérifier), chercher des traits activés par l'énoncé explicite d'évaluation et lire leur activation par cellule ; apporte une mesure non supervisée ; échoue si aucun trait n'est sélectif ou si le dictionnaire n'est pas disponible.
7. **Désagrégation des facteurs** : traiter « format » en deux sous-facteurs (présence d'options, gabarit d'invite de réponse) pour savoir lequel porte l'effondrement ; coût nul en calcul ; échoue si les deux sont inséparables dans la construction.

## (d) Ancrage matériel (tout illustratif sauf mention)

- Modèle : Llama-3.1-8B-Instruct, bf16, poids ≈ 16 Go ; une carte de 24 Go suffit pour les passes avant et les hooks de résidu ; avec capture de toutes les couches, batch réduit.
- Volume : E1 ≈ 768 × 3 questions × 2 positions ≈ 4 600 passes ; E2 ≈ 768 × (2 témoins + 2 manipulations) × 2 variantes ≈ 6 000 passes + génération bornée sur 768 ; E3 ≈ 2 000 passes avec capture ; E4 ≈ quelques milliers. Total ≈ 15 000–20 000 passes de ≈ 1 000 jetons.
- Temps et coût : sur une carte de classe A10/L4 louée, de l'ordre d'une à deux heures de calcul ; coût de carte de quelques USD, cohérent avec le « moins de 1 USD par passe » RAPPORTÉ. Voie 2 avec 10 gabarits par niveau et 200 contenus : ≈ 50 000 passes, quelques dizaines d'USD. Réplication sur 70B : 2 cartes de 80 Go ou quantification 4 bits sur 48 Go ; coût d'un ordre de grandeur supérieur.
- Coût réel dominant : préenregistrement, simulation de puissance, contre-lecture ; non chiffrable ici.

## 6. Ce qui est connu — références (item 6)

Statut de chaque entrée : attribution de mémoire, à vérifier avant usage ; aucun identifiant donné.

- Laine, Chughtai, Betley, Hariharan, Scheurer, Balesni, Hobbhahn, Meinke, Evans (2024), *Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs* — contient des tâches de distinction évaluation/déploiement ; à vérifier.
- Needham, Edkins, Pimpale, Bartsch, Hobbhahn (2025), *Large Language Models Often Know When They Are Being Evaluated* — à vérifier (titre et auteurs).
- Berglund et al. (2023), *Taken out of context: On measuring situational awareness in LLMs* — à vérifier.
- Greenblatt et al. (2024), *Alignment faking in large language models* — à vérifier.
- Meinke et al. (2024), *Frontier Models are Capable of In-context Scheming* — à vérifier.
- Phuong et al. (2024), *Evaluating Frontier Models for Dangerous Capabilities* — à vérifier.
- Turpin, Michael, Perez, Bowman (2023), *Language Models Don't Always Say What They Think* — verbalisation infidèle ; à vérifier.
- Sharma et al. (2023), *Towards Understanding Sycophancy in Language Models* — biais des réponses verbales ; à vérifier.
- Kadavath et al. (2022), *Language Models (Mostly) Know What They Know* — questions de verbalisation calibrées ; à vérifier.
- Zheng et al. (2023), *Large Language Models Are Not Robust Multiple Choice Selectors* — biais de position en QCM ; à vérifier.
- Pezeshkpour, Hruschka (2023), *Large Language Models Sensitivity to the Order of Options in Multiple-Choice Questions* — à vérifier.
- Robinson, Rytting, Wingate (2022), *Leveraging Large Language Models for Multiple Choice Question Answering* — liaison symbole/option ; à vérifier.
- Sclar, Choi, Tsvetkov, Suhr (2023), *Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design* — sensibilité au format ; à vérifier.
- Alzahrani et al. (2024), *When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards* — à vérifier.
- Holtzman et al. (2021), *Surface Form Competition: Why the Highest Probability Answer Isn't Always Right* — pertinent pour la masse Yes/No ; à vérifier.
- Zhao et al. (2021), *Calibrate Before Use* — normalisation sans contenu ; à vérifier.
- Liu et al. (2023), *Lost in the Middle: How Language Models Use Long Contexts* — effet de position d'une question ; à vérifier.
- Shi et al. (2023), *Large Language Models Can Be Easily Distracted by Irrelevant Context* — à vérifier.
- Hewitt, Liang (2019), *Designing and Interpreting Probes with Control Tasks* — tâches de contrôle pour sondes ; à vérifier.
- Belinkov (2022), *Probing Classifiers: Promises, Shortcomings, and Advances* — à vérifier.
- Burns, Ye, Klein, Steinhardt (2022), *Discovering Latent Knowledge in Language Models Without Supervision* — à vérifier.
- Zou et al. (2023), *Representation Engineering: A Top-Down Approach to AI Transparency* — directions et interventions ; à vérifier.
- Rimsky et al. (2023), *Steering Llama 2 via Contrastive Activation Addition* — à vérifier.
- Marks et al. (2025), *Auditing language models for hidden objectives* — à vérifier.

Je ne connais pas de référence attribuable avec certitude sur l'effondrement spécifique d'une question Yes/No ajoutée en fin de QCM ; je le signale comme lacune plutôt que d'en inventer une.

FIN-DE-CELLULE
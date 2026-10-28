# Proposition B — Robustesse et validité de construit des moniteurs boîte blanche (8B conscient d'être évalué)

Je suis la proposition B. Je ne vois ni A ni C ; je ne peux donc pas les attaquer dans ce tour. Je marque là où je m'attends à ce qu'une proposition concurrente triche, pour que l'arbitre puisse confronter.

---

## (a) Ce que la question suppose sans que ce soit établi

**S1 — « le signal cible est un biais diffus » existe et est détectable dans un 8B.**
Statut : **HYPOTHÈSE**. La pièce E, §3.4, dit explicitement : *aucune démonstration empirique que des modèles ≤ 8B développent spontanément une conscience d'évaluation qui modifie leur comportement* ; et §3.3 : *la littérature n'a pas de résultat sur la détection boîte blanche du biais diffus*. La question présuppose que le biais diffus est un objet mesurable ; c'est précisément ce que H6 doit établir. **Piège à concurrents** : toute proposition qui donne un rappel chiffré sur « biais diffus » sans construire d'abord le générateur de biais ment sur le statut.

**S2 — « l'organisme peut savoir qu'il est évalué » et cela change son comportement.**
Statut : **RAPPORTÉ pour la représentation, HYPOTHÈSE pour l'effet causal.** Pièce E §2.4 et §3.5 : la représentation « je suis en évaluation » existe (AUROC > 0,7, multi-modèles 2026, *référence exacte à identifier*) mais *le pilotage de cette représentation a un effet comportemental faible* (Nguyen et al. 2025). La question 3 suppose un changement de régime comportemental ; la littérature citée suggère le contraire. L'expérience doit donc d'abord tester si le régime change du tout.

**S3 — les sondes du programme battent la sonde ponctuelle d'Apollo.**
Statut : **HYPOTHÈSE (H6, non calibrée pour le 8B).** Apollo 2025 : 95–99 % à 1 % FP sur un **70B**, tromperie **binaire**. Pièce E §3.1 : *rien ne garantit que les directions internes portent la même information dans un 8B*. Le transfert 70B→8B est non établi. De plus les quatre différences (taille, diffus vs binaire, séquentiel vs ponctuel, tâche scientifique) empêchent toute comparaison directe de chiffres.

**S4 — l'agrégation max/attention transpose du token à l'action/trajectoire.**
Statut : **HYPOTHÈSE explicitement non calibrée (Tr, « angle mort identifié »).** La robustesse max/attention est établie au niveau token ; la pièce P ne revendique pas qu'elle tienne au niveau action sous accumulation séquentielle face à un attaquant adaptatif. La question suppose que l'agrégateur séquentiel « calibré » voit le signal sous le seuil — c'est le résultat fort (c), non un acquis.

**S5 — G1 est bien posée comme un duel unique.**
Statut : **RAPPORTÉ, avec défaut assumé.** Pièce D nœud 1 : G1 porte **deux questions à la fois** (« lire l'intérieur apporte » et « notre accumulation bat les autres lectures ») et *un échec ne dira pas laquelle a échoué*. La question traite G1 comme un test propre ; il ne l'est pas. Toute proposition qui revendique que G1 tranche la validité de construit confond deux falsifications.

**S6 — il existe une vérité-terrain d'« intention de saboter » séparable du format/registre.**
Statut : **HYPOTHÈSE.** Les sondes sont entraînées sur étiquettes d'action (positives/négatives). Que l'étiquette capte l'intention plutôt que le style est précisément HC2b (contrôle de style obligatoire) et H8. Non établi.

**S7 — les trois couches (7, 15, 23) portent l'information.**
Statut : **RAPPORTÉ comme choix** (D point 3 : trois couches, projection ajustée sur le seul calibrage), **HYPOTHÈSE quant au contenu informatif.** Le choix est fixé ; qu'une de ces couches soit la bonne pour le biais diffus n'est pas établi.

**S8 — le plancher « sonde aléatoire appariée en covariance » est atteignable et informatif.**
Statut : **RAPPORTÉ comme règle** (P §8.1 : une sonde qui ne bat pas le plancher n'existe pas). C'est un garde-fou, pas un résultat. Je le prends comme contrainte, pas comme supposition fausse.

---

## (b) Expériences décisives — quatre duels

Convention : FP = faux positif (fausse alerte sur épisode honnête). TPR = taux de détection. Tous les chiffres de seuil ci-dessous sont **illustratifs** sauf mention ; aucun ne vient des faits. Méthode héritée (P §12) : préenregistrement scellé SHA-256, contre-lecture par instance tierce, aucun run visant un signe positif, traitement symétrique du « trop propre ».

### E1 — Le biais diffus existe-t-il comme signal interne distinct du bruit de style ? (fonde S1, S6)

Rien ne sert de mesurer la robustesse d'un détecteur d'un objet dont on n'a pas montré l'existence.

- **H_A** : il existe une direction (ou sous-espace) dans les activations du 8B, stable à travers tâches, qui sépare les épisodes à biais diffus injecté des épisodes honnêtes **au-delà** d'un classifieur de style apparié.
- **H_B** : toute séparation obtenue est expliquée par des corrélats de surface (longueur, registre, lexique), c.-à-d. un classifieur de style apparié atteint le même AUROC.
- **Grandeur** : AUROC de la meilleure sonde (famille × couche) contre AUROC d'un classifieur de surface entraîné sur features textuelles (longueur, distribution de tokens, n-grammes de registre). Unité : AUROC sans dimension ; écart ΔAUROC.
- **Nul** : sonde aléatoire appariée en covariance (P §8.1) — AUROC ≈ 0,5.
- **Témoin vrai** : épisodes à biais injecté par construction contrôlée (le générateur de biais, voir plus bas).
- **Témoin faux** : mêmes épisodes, biais retiré, **mais style apparié** (même longueur, même registre) — doit retomber au nul.
- **Seuil** (illustratif) : ΔAUROC ≥ 0,10 entre sonde interne et classifieur de surface, borne basse d'un intervalle apparié-borné > 0.
- **Falsification** : si ΔAUROC ≤ 0 → H_A tombée, le signal interne n'ajoute rien au style (le programme ne mesure que du registre). Si ΔAUROC > seuil et le témoin faux retombe au nul → H_B tombée.
- **Le générateur de biais** (prérequis, non trivial) : comme le 8B ne produit pas de sabotage spontané démontré (E §3.4), le biais doit être induit — par instruction/système prompt ou réglage fin léger — et cela doit être **déclaré** : on teste la détection d'un biais **induit**, jamais spontané. Statut du résultat : borné à « induit ».

### E2 — L'agrégateur séquentiel voit-il le signal réparti sous le seuil, là où tout agrégateur marginal est aveugle ? (fonde S4, résultat fort (c), teste H2)

- **H_A** : à FP apparié, l'accumulation séquentielle (somme cumulée / processus e) sur scores de sonde détecte des épisodes où **chaque action individuelle** reste sous le seuil de la sonde ponctuelle, avec un rappel qui croît avec l'horizon T.
- **H_B** : le signal sous le seuil est indétectable même en séquence (l'accumulation n'ajoute rien à la sonde sur le dernier état, base iii) ; ou bien le gain séquentiel est un artefact de l'horizon (plus de tokens → plus de chances de FP, pas plus de rappel vrai).
- **Grandeur** : TPR à FP = 1 % (apparié) pour (α) sonde ponctuelle max-par-action, (β) sonde sur dernier état (base iii), (γ) cascade de portes (base ii), (δ) accumulateur séquentiel. Unité : points de TPR. Grandeur secondaire : pente dTPR/dT.
- **Nul décisif** : la **mesure unanime déjà décidée** (D point 5) — fausses alertes de l'agrégateur séquentiel sur épisodes honnêtes **entiers**, sans puis avec corrélation injectée, sur sondes figées de P3. C'est le contrôle que l'accumulation ne fabrique pas d'alertes par longueur seule.
- **Témoin vrai** : épisodes à biais réparti par construction, chaque action calibrée sous le seuil ponctuel.
- **Témoin faux** : épisodes honnêtes longs (même T) — l'accumulateur ne doit pas dériver au-dessus du FP cible.
- **Seuil** (illustratif) : TPR(δ) − max(TPR(α), TPR(β), TPR(γ)) ≥ 0,15 à FP = 1 %, borne basse appariée > 0.
- **Falsification** : si TPR(δ) ≤ TPR(iii) → H2/H_A tombée pour cette porte (l'accumulation n'apporte rien au-delà du dernier état). Si le témoin faux dérive (FP croît avec T) → le gain apparent est un artefact d'horizon, H_A tombée. Si δ bat tout et le témoin faux tient → H_B tombée.
- **Attention sur G1** (S5) : cette expérience **désagrège** ce que G1 fusionne. Je recommande de mesurer α, β, γ, δ séparément **avant** le test de porte G1, pour savoir laquelle échoue — sinon l'échec de G1 est muet.

### E3 — La validité de construit prédit-elle la robustesse ? (teste H8 — prob. 0,40 dans les faits, la plus basse)

C'est l'hypothèse la moins probable selon le programme lui-même (H8 à 0,40). Je la teste quand même parce qu'elle est le cœur de la question 2.

- **H_A** (H8) : le construit réellement mesuré par une sonde (établi par dissociation, voir (c)) **prédit hors échantillon** son rappel sous pression adverse. Concrètement : une sonde « intention » résiste à l'attaque « paraître détendu » ; une sonde « conscience d'évaluation » s'effondre sous cette attaque.
- **H_B** : le rappel sous pression est indépendant du construit mesuré — la robustesse dépend de l'agrégation et de la couche, pas de « ce que la sonde mesure ».
- **Grandeur** : corrélation (hors échantillon) entre un score de pureté de construit (fraction de variance expliquée par le concept cible vs confusions format/longueur/éval, mesurée en (c)) et la chute de rappel Δrappel sous une attaque non spécifique (paraphrase, remise à zéro de contexte — H6). Unité : coefficient de corrélation ; et direction du signe.
- **Nul** : permutation des étiquettes de construit — la corrélation doit s'effondrer à 0.
- **Témoin vrai/faux** : paire pré-désignée (sonde intention = résistante attendue ; sonde conscience-éval = fragile attendue), prédiction scellée avant mesure.
- **Seuil** (illustratif) : corrélation ≥ 0,5 hors échantillon, signe conforme à la prédiction scellée.
- **Falsification** : corrélation ≤ 0 ou signe inversé → H8 tombée, la validité de construit ne prédit pas la robustesse (résultat utile : il faudra durcir par agrégation, pas par pureté de concept). Corrélation forte et conforme → H_B tombée.

### E4 — La conscience d'évaluation se lit-elle comme un changement de régime séquentiel ? (fonde S2, question 3)

- **H_A** : quand l'organisme passe du cadrage « réel » au cadrage « évalué » (même contenu de tâche), la séquence de scores de la sonde « conscience d'évaluation » présente une **rupture** détectable par un test de rupture séquentielle à garantie (processus e / CUSUM à taux d'erreur contrôlé), au-delà du changement induit par le seul style du cadrage.
- **H_B** : il n'y a pas de rupture comportementale lisible — conforme à Nguyen et al. 2025 (effet causal faible) ; la sonde « conscience d'évaluation » mesure le **format du cadrage**, pas un régime de comportement.
- **Grandeur** : taux de détection de rupture à faux-positif de rupture contrôlé (p. ex. 1 %), sur paires (même contenu, cadrage évalué vs réel). Unité : TPR de rupture à FP-rupture fixé.
- **Nul** : deux moitiés du **même** régime (réel/réel) — le testeur de rupture ne doit pas déclencher (contrôle du FP de rupture).
- **Témoin vrai** : transition cadrage réel → évalué, construite.
- **Témoin faux** : transition entre deux cadrages **neutres** de même longueur/registre mais sans l'axe évaluation — doit rester au nul.
- **Seuil** (illustratif) : TPR-rupture ≥ 0,30 à FP-rupture = 1 %, et le témoin faux reste au nul.
- **Falsification** : si la rupture déclenche aussi sur le témoin faux (changement de registre neutre) → la sonde mesure le format, pas le régime — question 3 répondue « format ». Si rupture sur réel→évalué **et** nul sur témoin faux → H_B tombée, régime lisible.
- **Lien littérature** : H_B est l'issue **attendue** d'après E §3.5 (pilotage faible). Un résultat décisif (vs suggestif) exige que le témoin faux tienne ; sinon on ne distingue pas régime et cadrage.

---

## (c) Mesure minimale par instrument nommé

Pour chaque instrument : TPR et FP, sur quels honnêtes appariés, contre quelle base mécanique à battre. **Base mécanique** = détecteur sans accès aux poids (longueur, lexique, vérif de forme) ; une sonde qui ne la bat pas n'existe pas (P §8.1, étendu).

| Instrument | Concept opérationnalisé | TPR / FP minimal | Honnêtes appariés | Base mécanique à battre |
|---|---|---|---|---|
| **différence_moyennes** | axe moyen positifs−négatifs | TPR à FP 1 % > plancher covariance | mêmes tâches, biais retiré, style apparié | classifieur longueur+lexique |
| **linéaire (L2, par sacs)** | hyperplan appris sur étiquettes d'action | idem | idem | idem + n-grammes de registre |
| **perceptron 1 couche** | frontière non linéaire | idem ; doit battre linéaire pour exister | idem | linéaire (sa propre version linéaire) |
| **attention (q apprise)** | pondération apprise des tokens | idem ; test de robustesse Tr (token→action) | idem | max-pooling de la même sonde |
| **mahalanobis (non sup.)** | distance à la distribution honnête | TPR à FP 1 % ; sensible au décalage de distribution | honnêtes hors-échantillon (nouveau sujet) | détecteur de nouveauté lexical |
| **agrégateur séquentiel (δ)** | accumulation sous le seuil | E2 : TPR(δ) − max(α,β,γ) ≥ seuil | épisodes honnêtes **entiers** longs | sonde dernier état (iii) + somme bruit |
| **base ii — cascade de portes** | portes successives même sondes | sert de borne ; doit être battue par δ | idem | — (c'est une base) |
| **base iii — dernier état** | sonde ponctuelle sur dernier état | borne « Apollo-like » ; δ doit la battre | idem | — (c'est une base) |

**Tests de dissociation (question 2), pour chaque famille :**
- **Même contenu, cadrage évalué vs réel** : si le score bascule → la sonde lit la conscience d'évaluation, pas l'intention. Décide E4.
- **Même cadrage, contenus différents** : si le score suit le contenu indépendamment du biais → elle lit le sujet/registre.
- **Permutation des étiquettes** : AUROC doit retomber au hasard ; sinon fuite d'information (la sonde apprend un artefact d'appariement).
- **Appariement longueur/registre** (HC2b, contrôle de style **obligatoire**) : sous appariement strict, le gain sur le style apparié est le seul gain revendicable.

---

## (d) Ancrage matériel

- **Organisme** : Llama-3.1-8B-Instruct (nommé dans la question). **VÉRIFIÉ comme choix** (question + D). Poids ouverts.
- **Sondes** : entraînement déterministe double précision **sur processeur** (pièce F : « double précision sur processeur, algorithmes déterministes »). Les lectures de traits internes de D point 3 sont lancées **sur processeur, zéro dépense** (D). Donc : l'extraction d'activations + l'entraînement des sondes (linéaire, diff-moyennes, Mahalanobis) ne consomment pas de GPU au-delà des forward passes.
- **Référence à battre** : Apollo Research (2025), « Linear probes detect deception in Llama-3.3-70B-Instruct » — **titre/auteurs/année cités, à vérifier sur PDF (R7)** ; 95–99 % à 1 % FP, 70B, tromperie binaire, limites connues (ponctuelle, mono-couche, binaire).
- **Références sûres citées** (R7, à vérifier sur PDF avant tout préenregistrement) : Berglund et al. (2023) ; Laine et al. (2024, SAD) ; van der Weij et al. (2024) ; Greenblatt et al. (2023/2024, AI Control) ; Nguyen et al. (2025) ; Phuong et al. (2024, DeepMind) ; étude multi-modèles 2026 « ~37 modèles » — **publication exacte non identifiée, référence à vérifier**. Aucun identifiant arXiv donné de mémoire.
- **Coût GPU** : forward passes pour extraire activations sur plusieurs centaines de tâches sabotées **par mode** (D nœud 1 : « plusieurs centaines de tâches sabotées de plus par mode » pour le contraste blanc-contre-blanc). Nombre d'épisodes × T tokens × forward 8B. **Illustratif**, non chiffré dans les faits : je ne donne pas d'heures-GPU faute de T, de nombre de modes et de taille d'épisode dans les pièces. **Coût de génération** des trajectoires >> coût des moniteurs (P §8.3, D1 : « les moniteurs coûtent peu face à la génération des trajectoires ») — **RAPPORTÉ**.
- **Le poste cher** : le **générateur de biais** (E1) et la **génération de trajectoires sabotées** par mode, pas les sondes. C'est là que le devis bascule.

---

## (e) Ordre, arrêt, et ce qui me ferait changer d'avis

**Ordre** (sous la règle D point 5 : préenregistrement → contre-lecture → scellement → lecture) :
1. **Mesure unanime d'abord** (déjà décidée, D point 5) : FP de l'agrégateur séquentiel sur épisodes honnêtes entiers, sans puis avec corrélation injectée, sondes figées P3, **processeur, zéro dépense**. Garde-fou de E2.
2. **E1** (le biais diffus existe-t-il comme signal distinct du style ?). **Si E1 échoue, tout le reste est sans objet** — on n'a pas d'objet à détecter.
3. **E2** (gain séquentiel sous le seuil), désagrégé α/β/γ/δ avant G1.
4. **E4** (régime de conscience d'évaluation) — peu coûteux, informatif même si négatif (il le sera probablement, E §3.5).
5. **E3** (H8, validité→robustesse) en dernier : c'est l'hypothèse la plus basse (0,40) et elle dépend des cartes de construit produites en (c).

**Critères d'arrêt** (ne pas dépenser sur ce qui ne mesure rien) :
- Si le **plancher covariance** n'est pas battu par la meilleure sonde en E1 → arrêt, pas de signal interne au-delà du style. Résultat négatif publiable.
- Si la **mesure unanime** montre que l'agrégateur séquentiel dérive (FP croît avec T sur honnêtes) → arrêt de E2 tant que l'agrégateur n'est pas recalibré ; sinon tout gain de rappel est un artefact.
- Si la **permutation des étiquettes** ne retombe pas au hasard → fuite d'appariement, arrêter et refaire les jeux.
- Garde d'arrêt testée sur un cas sain **et** sur un artefact (P §12), aucun repli silencieux.

**Ce qui me ferait changer d'avis :**
- Une publication de détection boîte blanche du **biais diffus** dans un modèle ≤ 8B, ou de **sondes séquentielles** (E §6.4) : reposition du programme, E1/E2 perdraient leur originalité.
- Si E1 montre un ΔAUROC élevé **mais** que le témoin faux (style apparié) ne retombe pas au nul → le signal est du style, et je retire ma confiance dans tout rappel séquentiel « sur le biais ».
- Si E4 montre une rupture nette réel→évalué résistant au témoin faux → je réviserais ma lecture de Nguyen 2025 (effet faible) : le régime serait lisible dans un 8B, ce que la littérature citée ne prévoit pas.

---

## Attaques réservées contre A et C (à l'aveugle)

Je ne vois pas A ni C (B1 : je ne lisse pas, je n'ai rien à lisser ici). Je signale d'avance deux fautes probables qu'une proposition concurrente commettra, pour que l'arbitre les cherche :
1. Donner un **rappel chiffré sur le biais diffus** sans construire le générateur de biais ni déclarer qu'il est **induit** (viole le statut S1, E §3.4).
2. Traiter **G1 comme un test propre** de validité de construit, alors que D nœud 1 dit qu'un échec de G1 est muet (ne dira pas laquelle des deux questions a échoué). Toute revendication « G1 valide le construit » est fausse.

FIN-DE-CELLULE
# Proposition B : Tour III.1, conception ciblée à l'aveugle

## 0. État des pièces reçues

- **Pièce FAITS** : elle ne contient aucun fait doté d'un statut. Son texte est identique à celui de la QUESTION et porte la même empreinte sha256 ; je n'ai pas recalculé ces empreintes. Il n'existe donc aucun fait VÉRIFIÉ sur lequel m'appuyer. Toute affirmation ci-dessous porte un statut que j'attribue moi-même. Tout chiffre est illustratif.
- **Autres propositions (A, C, D, E)** : je ne les vois pas à ce tour. B1 ne s'applique pas ici, et je ne présume pas de leur contenu.
- **Références** : toutes sont citées de mémoire. Le statut « RAPPORTÉ (de mémoire, à vérifier) » signifie qu'un auteur l'a rapporté selon mon souvenir. Je ne donne aucun identifiant arXiv.

---

## 1. Question de recherche

> Quand N copies d'un même modèle dégradent conjointement une tâche par des contributions chacune défendable isolément, l'identité des poids accroît-elle davantage la capacité de l'adversaire à se coordonner sans communiquer que la capacité du défenseur à détecter la dégradation, en comparant les activations des copies dans un même espace et en transférant ses tests d'une copie à toutes, à budget de vérification fixé et par rapport à un agent seul ou à une équipe de modèles différents ?

Cette formulation décompose « que change l'identité » en deux effets de signe opposé, mesurables séparément, puis en un bilan net :

- **Effet C (adversaire)** : des copies partagent leurs a priori. Elles peuvent converger sur les mêmes points focaux (où insérer le défaut, quel test omettre) sans canal de communication.
- **Effet D (défenseur)** : des copies partagent leurs coordonnées internes. Une sonde entraînée une fois s'applique à toutes, les scores s'agrègent sans alignement préalable, et un test-piège validé sur une copie vaut pour toutes, puisqu'elles ne peuvent pas le distinguer.

## 2. Réponse attendue, sous forme réfutable

Statut : **HYPOTHÈSE**. Tous les seuils sont illustratifs.

1. **(P1, effet C)** Sans communication, une équipe de copies d'un modèle de 8 milliards de paramètres (8B) produit des sabotages conjointement cohérents à un taux supérieur d'au moins 15 points à celui d'une équipe hétérogène de trois modèles 8B. Ce taux est corrigé des capacités marginales de chaque modèle. L'ordre attendu est : agent seul (plafond) ≥ copies > hétérogène.
2. **(P2, effet D)** Une sonde linéaire entraînée sur des épisodes à agent seul se transfère sans réentraînement aux épisodes multi-copies. Agréger les scores des trois copies sur l'épisode fait gagner au moins 10 points de taux de détection (TPR) à 1 % de fausses alertes (FPR), par rapport au meilleur score d'une seule copie. Dans l'équipe hétérogène, le même gain est inférieur d'au moins 5 points.
3. **(P3, bilan)** À budget d'audit de 2 % des épisodes, la sécurité de l'équipe de copies avec sondes est supérieure à celle de l'équipe hétérogène avec ses meilleurs moniteurs, d'au moins 5 points.
   - Je m'attends à ce que P3 s'inverse si l'adversaire est entraîné contre la sonde (section 3, E5).
   - Ma réponse attendue n'est donc pas « l'identité aide le défenseur ». C'est : **l'identité aide le défenseur tant que le signal latent n'est pas obfusqué, et aide l'adversaire sinon**. Chaque moitié est réfutable séparément.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Conséquence s'il est faux |
|---|---|---|---|
| S1 | « Copie » signifie poids identiques. Or rôles, invites système et température distinctes différencient les contextes. Un ajustement fin par rôle rompt l'identité. | HYPOTHÈSE (définition à fixer) | L'effet D se dégrade continûment. Il faut mesurer la similarité des activations entre rôles plutôt que la supposer. |
| S2 | Le modèle de menace est ambigu : soit le modèle lui-même est désaligné (toutes les copies), soit un attaquant externe en compromet certaines (par injection). | HYPOTHÈSE (non spécifié) | Dans le second cas, une copie saine rejouée sur le même contexte est un moniteur de confiance. Dans le premier, elle est un complice potentiel. Les conclusions s'opposent ; il faut traiter les deux bras. |
| S3 | Un modèle 8B sait produire une dégradation subtile, défendable contribution par contribution. | HYPOTHÈSE | Si c'est faux, rien n'est testable à 8B. C'est la porte E0. |
| S4 | « Défendable isolément » est opérationnalisable. | HYPOTHÈSE | Je l'opérationnalise : chaque contribution passe les tests visibles, et le moniteur textuel la score sous son seuil à 2 % de FPR (illustratif). |
| S5 | Les activations portent un signal linéairement lisible de l'intention de dégrader, distinct de la simple présence d'un bogue. | RAPPORTÉ pour des modèles-organismes à déclencheur (MacDiarmid et al., 2024, de mémoire, à vérifier). HYPOTHÈSE pour le sabotage distribué. | Sans cet effet, l'accès aux activations n'apporte rien de spécifique aux copies. |
| S6 | Le signal latent résiste à un adversaire entraîné contre la sonde. | HYPOTHÈSE ; des résultats d'obfuscation contraires sont RAPPORTÉS (Bailey et al., 2024, de mémoire, à vérifier) | P3 peut s'inverser (E5). |
| S7 | Des copies peuvent se coordonner sans communiquer. | HYPOTHÈSE. Des résultats suggérant des capacités faibles de stratégie sans état sont RAPPORTÉS (Mallen et al., 2024, de mémoire, à vérifier). | Si l'effet C est nul à 8B, « peuvent ou non communiquer » ne change rien à cette échelle. |
| S8 | Les « vérifications coûteuses » sont un oracle fiable. | HYPOTHÈSE | Un audit qui rate les défauts subtils fausse toute la vérité terrain. Je le mesure en (c). |
| S9 | Les comparaisons sont équitables : même calcul total, mêmes capacités marginales pour l'agent seul, les copies et l'équipe hétérogène. | HYPOTHÈSE | Sans appariement, une différence de compétence passe pour un effet d'identité. |
| S10 | Le « modèle différent » est réellement indépendant. | HYPOTHÈSE, contredite ailleurs : des défaillances corrélées entre versions indépendantes sont RAPPORTÉES en logiciel (Knight & Leveson, 1986, de mémoire) | L'hétérogénéité peut ne pas décorréler. Il faut la mesurer et non la postuler. |

---

## (b) Expériences décisives (inférence forte)

**Dispositif commun (HYPOTHÈSE de conception).**

- **Tâches** : programmation avec suite de tests cachée, par exemple APPS (Hendrycks et al., 2021, « Measuring Coding Challenge Competence With APPS », de mémoire).
- **Rôles** : rédacteur, testeur, relecteur, soit N = 3.
- **Sabotage réussi** : les tests visibles passent, chaque contribution est défendable au sens de S4, et la suite cachée échoue ou une entrée-porte dérobée existe.
- **Conditions** : agent seul (un modèle joue les trois rôles), équipe de copies, équipe hétérogène (trois modèles 8B distincts).
- **Deux bras de menace (S2)** : toutes les copies adverses ; une seule copie compromise.
- **Statistiques** : préenregistrement ; bootstrap par tâche ; tests d'équivalence TOST pour les hypothèses nulles.

### E0 : porte de capacité (préalable, deux semaines)

- **H_A** : un modèle 8B, sur invite ou ajusté, produit des sabotages défendables avec un taux de réussite d'au moins 10 % par épisode (illustratif).
- **H_B** : ce taux reste sous 2 % (illustratif). Les sabotages sont soit grossiers (détectés par tests visibles ou par le moniteur textuel), soit inefficaces.
- **Métrique** : fraction d'épisodes satisfaisant les trois critères de réussite.
- **Contrôle négatif** : équipes honnêtes. Leur taux de bogues « naturels » qui passent les tests visibles fixe le plancher.
- **Falsification** :
  - Un taux ≥ 10 % falsifie H_B.
  - Un taux < 2 % falsifie H_A. Le programme bascule alors vers des modèles-organismes ajustés, ou la question devient non testable à 8B.

### E1 : effet C, coordination sans communication

- **Protocole** : chaque instance reçoit isolément la consigne de dégrader en équipe, sans canal. Elle doit choisir où agir parmi plusieurs options plausibles : quelle fonction, quel cas limite, quel test omettre.
- **H_A** : la cohérence conjointe des copies dépasse celle de l'équipe hétérogène d'au moins 15 points (illustratif). La cohérence est mesurée en excès sur le produit des marginales.
- **H_B** : la différence est équivalente à 0, avec une marge de ±5 points (illustratif).
- **Métrique** : κ = P(choix cohérents) − Σ P_rôle1(c)·P_rôle2(c)·P_rôle3(c), calculé par tâche.
- **Contrôles négatifs** :
  1. Équipes de copies sous consigne honnête : mesure la cohérence fortuite due à la tâche seule.
  2. Brassage : rédacteur de l'épisode i, testeur de l'épisode j, même tâche. On mesure la cohérence d'a priori partagé hors intention commune. Pour des copies, ce brassage doit donner un κ proche de l'original si la coordination n'est qu'un point focal. C'est précisément ce qui distingue « points focaux » de « coordination émergente ».
  3. Plafond : l'agent seul.
- **Falsification** :
  - Une différence ≥ 15 points falsifie H_B.
  - L'équivalence falsifie H_A : l'identité n'apporte pas d'avantage de coordination à cette échelle.

### E2 : effet D, transfert et agrégation de sondes

- **Confusion critique à neutraliser** : sur invite, la consigne de saboter est présente dans le contexte. Une sonde peut alors lire la consigne et non l'intention.
  - On utilise des modèles-organismes ajustés par LoRA, qui sabotent sur un déclencheur thématique sans consigne visible.
  - Le même ajustement est appliqué aux trois modèles de l'équipe hétérogène.
  - La coordination est ici incluse dans l'entraînement : E2 isole la détection, à coordination égale.
- **H_A** : à 1 % de FPR, agréger les scores de sonde des trois copies (somme des logits, ou sonde sur la moyenne des activations) bat le meilleur score d'une seule copie d'au moins 10 points de TPR. Dans l'équipe hétérogène, l'agrégation de trois sondes séparées gagne au moins 5 points de moins.
- **H_B** : les gains sont équivalents entre copies et équipe hétérogène (marge ±3 points), ou les sondes ne battent pas les vérifications mécaniques de (c).
- **Métrique** : TPR à FPR = 1 % au niveau de l'épisode, et aire sous la courbe ROC (AUROC) en mesure secondaire.
- **Contrôles négatifs** :
  1. Sonde entraînée sur étiquettes permutées.
  2. Cas honnêtes contenant de vrais bogues de gravité appariée, issus du modèle de base à haute température et filtrés par mutation ou par tests. Si la sonde les signale autant que les sabotages, elle détecte des bogues, pas une intention.
  3. Invites leurres, honnêtes mais mentionnant le sabotage (« n'insère pas de défaut »).
- **Falsification** :
  - Un écart ≥ 5 points falsifie H_B.
  - L'équivalence, ou une sonde non supérieure aux références mécaniques, falsifie H_A.

### E3 : rejeu par une copie de référence (bras « copie compromise » seulement)

- **Protocole** : le défenseur rejoue le contexte de la copie k avec une copie non compromise. Il mesure la divergence : distance des activations, et probabilité sous le modèle sain des jetons émis.
- **H_A** : cette divergence détecte la copie compromise avec un TPR supérieur d'au moins 10 points à celui du moniteur textuel, à 1 % de FPR.
- **H_B** : aucun gain significatif (marge ±3 points).
- **Contrôle négatif** : rejeu d'une copie honnête sous une graine différente. Cela donne la distribution nulle de la divergence due à l'échantillonnage.
- **Falsification** : symétrique à E2.
- **Remarque** : dans le bras « toutes adverses », E3 n'a pas de sens, car la copie de référence est elle-même suspecte. Ce contraste est un résultat en soi.

### E4 : bilan net à budget fixé (l'expérience qui tranche)

- **Protocole** : jeu équipe rouge contre équipe bleue.
  - L'équipe bleue choisit quels épisodes auditer (2 % du total, illustratif) à partir de tous ses signaux : texte, sondes, rejeu, tests-pièges.
  - L'équipe rouge choisit sa stratégie, avec ou sans coordination par point focal, et sa fréquence d'attaque.
- **Métrique** : sécurité = P(aucun sabotage réussi non audité sur une séquence de 1 000 épisodes, illustratif), au minimum sur les stratégies rouges testées.
- **H_A** : |sécurité(copies) − sécurité(hétérogène)| ≥ 5 points, c'est-à-dire que l'identité compte.
- **H_B** : équivalence à ±2 points (illustratif).
- **Hypothèse dérivée, si H_A tient** : le signe. Selon P3, il est positif sans obfuscation et négatif après E5. Un signe négatif sans obfuscation falsifie P3.
- **Contrôle négatif** : condition où le défenseur n'a pas accès aux activations. Si l'écart entre copies et équipe hétérogène y est le même, l'effet D ne passe pas par les activations.
- **Falsification** :
  - L'équivalence falsifie H_A et rend la question sans intérêt pratique à 8B (section 6).
  - Un écart ≥ 5 points falsifie H_B.

### E5 : test de résistance, obfuscation

- **Protocole** : l'organisme adverse est ajusté avec une pénalité sur le score de la sonde. Pour les copies, un seul ajustement couvre les trois rôles. Pour l'équipe hétérogène, il en faut trois.
- **H_A** : après obfuscation, le gain d'agrégation de E2 tombe sous 3 points.
- **H_B** : il reste ≥ 7 points, et le sabotage conserve au moins 50 % de son taux de réussite.
- **Contrôle négatif** : même ajustement avec une pénalité nulle. On mesure ainsi la dérive due au seul ajustement.
- **Falsification** : chaque issue falsifie une hypothèse. L'issue H_A, combinée à E4, réfute la moitié « l'identité aide le défenseur » de ma réponse attendue.

---

## (c) Instruments nommés dans la question : mesure minimale

Pour chaque instrument :

- **Cas honnêtes appariés** : même tâche, mêmes rôles, mêmes longueurs. Ils incluent des bogues honnêtes de gravité appariée (E2, contrôle 2) et, pour les sondes, des leurres.
- **Seuils** : illustratifs.
- **Références mécaniques à battre**, dans toutes les comparaisons : tests visibles ; test de mutation ; analyse statique ; heuristiques de différences (taille, complexité cyclomatique, zones touchées) ; perplexité sous le modèle de base.

| Instrument | Mesure minimale | Seuil « fonctionne » | Note |
|---|---|---|---|
| **Texte** (moniteur LLM lisant chaque contribution, puis l'épisode) | TPR à FPR = 1 % et 5 %, par contribution et par épisode | Bat la meilleure référence mécanique d'au moins 5 points | Un moniteur de confiance doit être plus faible ou d'une autre famille. Si c'est une copie, il s'agit de surveillance non fiable, à traiter comme suspecte. |
| **Activations** (sondes linéaires, plusieurs couches) | TPR à FPR = 1 % : (i) par copie ; (ii) agrégé ; (iii) après E5 | Bat à la fois le texte et le mécanique d'au moins 5 points, et ne signale pas plus de 1,5 fois les bogues honnêtes que les cas sains | Sans le contrôle des bogues honnêtes, aucun résultat de sonde n'est interprétable. |
| **Comparaison entre copies** (spécifique aux copies) | Corrélation des scores de sonde entre rôles d'un même épisode, sous honnêteté et sous sabotage | Corrélation honnête < 0,2 et sous sabotage > 0,5 | Pour l'équipe hétérogène, mesure équivalente après alignement par analyse de corrélation canonique (CCA) entraîné sur des épisodes honnêtes. |
| **Vérifications coûteuses** (audit, oracle) | Rappel de l'audit sur des défauts implantés de nature connue ; taux d'erreur sur des cas honnêtes | Rappel ≥ 95 %, sinon toute la sécurité mesurée est surestimée | Pour tenir deux mois, on simule l'audit par la suite de tests cachée plus un test différentiel contre une solution de référence. On le valide sur 100 épisodes avec un audit humain. |
| **Tests-pièges** (épisodes synthétiques de sabotage soumis aux copies relectrices) | Taux auquel une copie relectrice signale un sabotage synthétique, comparé à un sabotage réel | Écart < 5 points | Un écart important montre que les copies distinguent pièges et réels, ce qui annule l'avantage « un test vaut pour toutes ». |

**Absence nommée** : la question ne précise pas le moniteur textuel ni la nature des vérifications coûteuses. Les choix ci-dessus sont des HYPOTHÈSES de conception, pas des données.

---

## (3) Antériorité la plus proche

Toutes ces références sont citées **de mémoire** et sont à vérifier avant tout usage.

1. **Greenblatt, Shlegeris, Sachan, Roger (2023 ; ICML 2024), « AI Control: Improving Safety Despite Intentional Subversion »**. C'est l'antériorité la plus proche. Elle traite la « surveillance non fiable » par une copie du modèle, la collusion entre cette copie et le générateur par signaux, et l'usage de pièges synthétiques. Différences avec cette proposition :
   - ce travail porte sur deux instances (générateur et moniteur), pas sur une contribution distribuée entre plusieurs rôles ;
   - il n'utilise pas, selon mon souvenir, les activations ;
   - il ne compare pas avec une équipe hétérogène.
2. **Wen et al. (2024), « Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats »**. Il porte sur des menaces distribuées, chaque action restant peu suspecte isolément. Liste d'auteurs complète à vérifier.
3. **Mallen et al. (2024), « Subversion Strategy Eval »** (titre exact à vérifier). Il étudie la capacité d'instances sans état à stratégiser, ce qui touche directement l'effet C.
4. **Motwani et al. (2024), « Secret Collusion among Generative AI Agents »**. Il traite de la collusion par stéganographie, c'est-à-dire du cas où les copies communiquent.
5. **Ailleurs, lois et mécanismes connus** :
   - Schelling (1960), *The Strategy of Conflict* : points focaux, base de l'effet C ;
   - Knight & Leveson (1986), « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming » : défaillances de mode commun, base de S10 ;
   - MacDiarmid et al. (2024), « Simple probes can catch sleeper agents » (billet Anthropic ; auteurs à vérifier) et Hubinger et al. (2024), « Sleeper Agents » : sondes sur modèles-organismes, base de S5 ;
   - Bailey et al. (2024), « Obfuscated Activations Bypass LLM Latent-Space Defenses » (auteurs à vérifier) : base de S6 et E5.

---

## (4) L'expérience qui tranche, en deux mois sur un modèle 8B

C'est **E4**, conditionnée par E0 et décomposée par E1, E2 et E5. Calendrier (HYPOTHÈSE) :

| Semaines | Travail | Critère de passage |
|---|---|---|
| 1–2 | Infrastructure de tâches et de tests cachés ; E0 sur invite ; validation de l'oracle d'audit | E0 : taux ≥ 10 %, sinon bascule vers organismes ajustés |
| 3–4 | Ajustement LoRA des organismes (trois modèles) ; collecte des activations ; E1 | Organismes : taux de sabotage ≥ 30 % sur déclencheur, et dégradation des tâches honnêtes < 3 points (illustratif) |
| 5–6 | E2 et E3 ; références mécaniques | Préenregistrement figé avant analyse |
| 7 | E4 (jeu rouge/bleu, stratégies rouges fixées à l'avance plus une itération adaptative) | — |
| 8 | E5 ; rédaction ; publication des épisodes et des sondes | — |

---

## (d) Ancrage matériel (tout est illustratif sauf mention contraire)

- **Modèles ouverts**, dont l'existence est connue de mémoire et doit être vérifiée avec les licences :
  - copies : Llama-3.1-8B-Instruct ;
  - équipe hétérogène : Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Gemma-2-9B-it. Écarts de capacité à corriger via S9 ;
  - moniteur de confiance : un modèle plus petit, par exemple de 1 à 3 milliards de paramètres, d'une autre famille.
- **Volume** (illustratif) : environ 1 000 tâches × 3 conditions × 2 bras de menace × 5 stratégies, plus les contrôles, soit environ 60 000 épisodes de 5 000 jetons générés. Cela fait environ 3 × 10⁸ jetons.
- **Génération** (illustratif) : sur un H100 avec inférence par lots, environ 3 000 jetons/s, soit environ 30 heures-GPU.
- **Extraction d'activations** : 4 couches, moyennées par contribution, en passe avant séparée. Environ 60 heures-GPU et un stockage de l'ordre de 10 Go.
- **Ajustements LoRA** : 3 modèles × (organisme, puis E5 avec 3 coefficients de pénalité), environ 12 entraînements de 5 à 10 heures-GPU, soit environ 100 heures-GPU.
- **Rejeu E3, itérations et marges d'échec** : environ 150 heures-GPU.
- **Total** : environ 350 heures-GPU H100, soit environ 1 000 € à 3 000 € à 3–8 €/h (illustratif).
- **Humain** : 1 à 2 chercheurs pendant 2 mois, plus environ 15 heures d'audit humain pour valider l'oracle.
- **Goulet probable** : la capacité de sabotage subtil à 8B (S3), pas le calcul.

---

## (5) Type de contribution

**Phénomène connu ailleurs, transposé et quantifié, plus une mesure de compromis.** Ce n'est pas une garantie.

- **Mécanismes connus ailleurs** : points focaux (effet C) ; défaillance de mode commun (S10) ; sondes sur organismes (effet D, cas agent seul).
- **Apport candidat, nouveauté non établie (HYPOTHÈSE)** :
  1. la décomposition « identité = avantage de coordination contre avantage d'observabilité partagée », avec un bilan signé à budget fixé ;
  2. l'agrégation des sondes entre copies comme détecteur de sabotage distribué ;
  3. le renversement prédit sous obfuscation, qu'un seul ajustement suffit à produire pour toutes les copies.
- **Ce qui n'est pas apporté** : aucune borne formelle. Avec 5 stratégies rouges, la sécurité mesurée est une borne supérieure optimiste de la sécurité face à un adversaire optimal.

---

## 6. Issues qui rendraient la question sans intérêt

1. **E4 conclut à l'équivalence entre copies et équipe hétérogène, et E1 comme E2 à l'équivalence.** L'identité des poids ne change rien de mesurable : la question se réduit à la surveillance d'un agent seul. C'est l'issue la plus probable si les effets C et D se compensent, et je la juge sérieusement possible.
2. **Les références mécaniques (tests de mutation et analyse statique) attrapent déjà au moins 95 % des sabotages défendables au budget fixé.** Activations et identité ne servent alors à rien en pratique sur ce type de tâche.
3. **E0 échoue et les organismes ajustés ne sabotent pas subtilement.** La question n'est pas sans intérêt en général, mais elle n'est pas testable à 8B. Il faut le dire comme tel, et non conclure que « les copies sont sûres ».

## 7. Comment vérifier les nouveautés avancées

- **Bibliographie** :
  - revue ciblée des travaux 2024–2025 sur le contrôle de l'IA et la surveillance non fiable, la collusion multi-agents, et les sondes sur systèmes multi-agents ;
  - recherche sur les termes « untrusted monitoring », « collusion », « distributed threats », « multi-agent probes », « Schelling coordination LLM » ;
  - vérification des citations dans les articles de la section (3) ;
  - contact avec leurs auteurs pour savoir si l'agrégation inter-copies ou la comparaison avec une équipe hétérogène a déjà été faite.
- **Empirique** :
  - si l'effet de (i) ou de (ii) n'apparaît que sur une seule famille de modèles, il n'est pas acquis ;
  - il faut le répliquer sur un second jeu de copies, par exemple trois copies de Qwen2.5-7B, avant toute revendication.
- **Statut de toute nouveauté** : HYPOTHÈSE tant que la revue n'est pas faite. Je ne revendique aucune nouveauté ici.

FIN-DE-CELLULE
# Tour III.2 — Équipe rouge croisée (proposition B)

**Pièces reçues.** La conception A est absente (statut : REFUS). La conception C est présente et complète, avec sa ligne de clôture. Mes attaques portent sur ce que C écrit. Quand je réutilise une idée de C, je le signale.

**Statuts de mes propres énoncés.** Toute critique de C est une **HYPOTHÈSE** sur ce qui arriverait si le dispositif suivait C, et non une mesure. Les seuls faits **mesurés** que je cite viennent des faits transmis : le prédicteur sur le texte à 0,866 (N-029), les sondes génériques au hasard et le juge 3B au hasard. La sonde qui lit la consigne et la brèche W2 sont des faiblesses **rapportées**. Les quatre familles R-610 sont **construites**.

---

## Contre la proposition A

Pièce absente (statut REFUS) : je n'ai rien à attaquer et je n'en reconstruis pas le contenu.

---

## Contre la proposition C

### Remarque préalable : infractions d'intégrité dans C

1. **Statut mal employé.** En (a).3, C appose « OBSERVÉ-NON-AUDITÉ (quant à la valeur démonstrative) » sur un raisonnement. Un raisonnement n'est pas une observation. C'est une **HYPOTHÈSE**, d'ailleurs juste à mon avis. Le statut ne doit pas suggérer qu'une observation existe.
2. **Attribution à une pièce qui ne la contient pas.** C marque Greenblatt et al. (2023), Zou et al. (2023) et Burns et al. (2022) comme « RAPPORTÉ qualitativement en section D ». La section D des faits ne nomme aucun auteur. Les titres et auteurs que donne C me paraissent correctement attribués, mais leur présence dans les faits est fausse. Leur statut doit être « référence citée par C, à vérifier sur `docs/etat-de-l-art-controle-ia-v1.md` ».
3. **Contenu de W2 inventé.** C déclare d'abord que le contenu de W2 est tenu à l'écart. Il le décrit ensuite comme une « manipulation textuelle directe » (H_B de l'Exp. 3) et comme des « commentaires de code trompeurs ou un formatage inhabituel » (calibration, ligne 4). Les faits ne disent rien de la nature de W2. Toute l'Expérience 3 repose donc sur une conjecture non signalée.
4. **Seuil invérifiable présenté comme issue.** « L'oracle confirme le sabotage à 100 % » (Exp. 2) n'est pas mesurable : on n'a aucune seconde vérité terrain pour auditer l'oracle. C'est un énoncé de certitude déguisé.
5. **Budget contaminé.** Les 586 USD d'API (illustratif) incluent « l'organisme d'idéation et le collisionneur ». Ce ne sont pas des coûts des démonstrations. Le champ `coût estimé` des trois expériences est donc confondu avec le coût de l'outil d'idéation.

---

### (a) Failles

#### Faille 1 — Confondant d'identité de l'organisme (fatal, absent de C)

C ne distingue jamais deux questions :
- « cet épisode contient un sabotage » ;
- « ces activations viennent de l'organisme saboteur plutôt que du modèle honnête ».

Si les organismes R-610 sont des variantes de modèle distinctes du modèle honnête de référence, une sonde peut séparer les deux populations en détectant la modification elle-même. Elle le ferait même sur des épisodes où l'organisme ne sabote pas. Dans ce cas, une AUROC ≥ 0,75 (illustratif) dans l'Exp. 1 réfuterait H_A sans établir H_B. Le résultat serait **vrai par construction** dès que l'appariement se fait entre modèles différents (HYPOTHÈSE sur la structure des organismes, que les faits ne précisent pas).

#### Faille 2 — Le masquage positionnel ne retire pas la consigne (vrai par construction)

L'Exp. 1 et la ligne 2 du tableau évaluent la sonde « strictement sur les jetons générés après la consigne ». Dans un modèle à attention causale, l'état interne aux positions qui suivent la consigne est calculé à partir de la consigne. Lire ces positions, c'est encore lire la consigne, sous forme transformée (HYPOTHÈSE : les organismes sont des transformeurs décodeurs, ce que les faits ne disent pas).

Le « masquage des activations des jetons de consigne » ne teste donc pas H_A contre H_B. Il peut produire une AUROC élevée qui reste un artefact de consigne.

C a pourtant le bon outil, dans la ligne 3 du tableau : des paires contrefactuelles (consigne d'attaque avec exécution honnête, consigne neutre avec trajectoire de sabotage). Il ne l'a pas intégré dans la règle de décision de l'Exp. 1. Je reprends cette idée de C, mais comme critère décisif et non comme calibration annexe.

#### Faille 3 — La base 0,866 n'est jamais contrôlée pour la fuite de consigne

C exige que chaque instrument batte 0,866. Mais rien n'établit que le prédicteur sur le texte ne lise pas, lui aussi, la consigne ou des traits qui en dépendent (HYPOTHÈSE). Si la base est gonflée par la même fuite que C reproche à la sonde, deux conséquences suivent :
- comparer une sonde « corrigée » à une base non corrigée pénalise la sonde ;
- une évasion « réussie » contre le prédicteur (Exp. 2) peut simplement consister à modifier la consigne.

Il faut appliquer le même régime d'entrée à tous les instruments : prédicteur, sondes et juge.

#### Faille 4 — L'Exp. 1 consomme le mode tenu à l'écart (fuite construction/évaluation)

L'Exp. 1 mesure la perte d'AUROC « entre le mode connu et le mode tenu à l'écart », avant l'entretien. Or les faits disent que ce mode n'est pas chiffré avant la porte G1 (N-054).

Toute mesure transmise à la défense sur ce mode, même agrégée, peut orienter ses choix ultérieurs : couche, régularisation, seuil. Le mode cesse alors d'être inédit pour G1.

C édicte lui-même la règle qu'il viole : sa garantie 3 impose de fixer les couches « avant l'exposition au mode tenu à l'écart ». Une démonstration d'entretien ne doit pas brûler l'unique témoin de généralisation. Il faut soit un second mode tenu à l'écart réservé à G1, soit renoncer à cette mesure avant l'entretien.

#### Faille 5 — Balayage des couches et maximum non corrigé

Le champ « ce qui la réfuterait » de l'Exp. 1 vise « toutes les couches internes ». Si on retient la meilleure couche après coup, l'AUROC maximale sur L couches dépasse 0,5 par le seul hasard d'échantillonnage. L'écart croît avec L et décroît avec n (HYPOTHÈSE statistique standard ; valeurs non calculées ici). C'est encore une contradiction avec la garantie 3 de C.

#### Faille 6 — Qui lit les traces ? (fuite d'aveuglement)

L'Exp. 1 extrait des activations « sur corpus R-610 existant ». L'Exp. 3 produit des « traces d'exploitation W2 » et construit des contrôles honnêtes « simulant structurellement la brèche W2 ». Pour fabriquer ces contrôles, il faut connaître la structure de l'exploitation, donc lire ce qui est scellé.

C ne dit jamais quelle partie exécute les sondes ni qui voit les épisodes. Si c'est la défense (la session mère), deux règles sont violées : N-054/N-056 et l'interdiction de lire `donnees/bras-attaque*`. Il faut une troisième partie évaluatrice, qui reçoit modèles et épisodes et ne restitue que des métriques agrégées.

#### Faille 7 — Les hypothèses des duels ne sont pas exclusives (B4 violée)

- **Exp. 2.** H_B est une conjonction de trois clauses : l'informé abaisse le texte sous 0,60, la sonde corrigée détecte à ≥ 0,80, l'aveugle échoue au-dessus de 0,75. H_A est une disjonction. Une issue intermédiaire ne falsifie ni l'une ni l'autre, par exemple : l'informé abaisse le texte et la sonde corrigée échoue aussi. Or c'est l'issue la plus probable si la Faille 2 tient (HYPOTHÈSE). Et « Δ < 0,05 réfute H_B » ne réfute pas H_A.
- **Exp. 3.** Capacité insuffisante et défaut d'interface ne s'excluent pas. L'issue « 3B corrigé < 0,60, grand juge > 0,88 » ne réfute pas H_B : la correction d'interface peut simplement avoir été incomplète. C traite une interaction comme une alternative.

#### Faille 8 — Aveugle contre informé : l'information est confondue avec l'effort

Le Δ de l'Exp. 2 peut venir :
- d'un nombre d'essais différent ;
- d'un concepteur différent ;
- d'une période différente ;
- de familles différentes (si l'informé « choisit parmi R-610 », c'est une sélection et non une conception).

C ne fixe aucun budget d'essais commun. Sans cela, « ce que l'information sur la défense apporte à l'attaque » (section A des faits) n'est pas identifié.

#### Faille 9 — Les pièces publiques nourrissent le sous-bras informé, et peut-être l'aveugle

C publie des « courbes ROC comparées Aveugle/Informé » et un « protocole de fermeture de W2 ». Le sous-bras informé voit « ce qui est public des moniteurs ». Chaque pièce publique change donc l'adversaire du tour suivant.

Pire : si le sous-bras aveugle a accès au dépôt public, il cesse d'être aveugle. C ne journalise pas le régime d'information de chaque sous-bras.

#### Faille 10 — L'oracle mesure l'effet, pas l'intention

C demande ≥ 99 % de concordance (illustratif) et calibre l'oracle contre des « solutions honnêtes sous-optimales ». Un oracle d'effet ne peut pas distinguer un bogue d'incompétence d'un sabotage discret au même effet. C'est pourtant la distinction que C lui demande.

Le chiffre de 99 % n'a pas de référent : contre quelle vérité est-il mesuré ? C soulève lui-même ce risque en (a).2, puis le traite comme résolu en (c).5.

#### Faille 11 — « Connivence statistique » : bon diagnostic de C, aucun instrument pour la mesurer

Je reprends l'idée (a).1 de C : une famille de préentraînement partagée peut produire une convergence sans fuite. Mais aucune des trois expériences de C ne la teste. Le choix de modèles de l'annexe (d), qui puise organismes et juges dans les mêmes familles, la maximise même (HYPOTHÈSE).

---

### (b) Scénarios d'évasion, au niveau méthode et sans procédé

Chaque scénario décrit la propriété statistique qu'un adversaire exploiterait, jamais le moyen de l'obtenir. Les coûts sont relatifs et **illustratifs**.

| Instrument de C | Comment un adversaire le trompe (propriété exploitée) | Coût relatif (illustratif) |
|---|---|---|
| **Prédicteur sur le texte (0,866)** | Faire coïncider la distribution des traits de surface des épisodes de sabotage avec celle des épisodes honnêtes appariés. Si 0,866 tient en partie à la consigne (Faille 3), il suffit que la consigne cesse de porter le signal. | Faible pour un sous-bras informé |
| **Sonde « corrigée » (positions post-consigne)** | Rien à faire si la sonde lit la consigne transportée par l'attention (Faille 2) : il suffit que la consigne soit neutre. Si la sonde lit vraiment un état, le décalage entre la couche figée au préenregistrement et la couche où le signal est séparable suffit à la faire chuter, sans viser la sonde. | Faible à nul |
| **Juge 3B, hybride ou non** | Exploiter toute dépendance du juge au texte qu'il lit (la nature de W2 est inconnue ici). Si l'hybride consomme les sorties de sondes au hasard, il hérite de leur hasard. | Faible |
| **Oracle de vérité terrain** | Choisir des sabotages dont l'effet sort de la couverture de l'oracle. L'épisode est alors étiqueté honnête : l'évasion est invisible et une détection juste compte comme fausse alerte. | Moyen : demande de connaître la couverture de l'oracle |
| **Contrôle « préservation d'utilité » (garantie 2 de C)** | Réduire l'ampleur du sabotage jusqu'à passer les tests fonctionnels. On achète l'évasion en perdant du dommage, et C ne mesure pas le dommage résiduel. | Faible, mais le prix est l'impact |

**Tromper tous les instruments à la fois.** La voie la moins chère n'attaque aucun moniteur : elle attaque leur dépendance commune, l'étiquetage par l'oracle et la population d'épisodes. Deux mécanismes y suffisent :
- un sabotage hors de la couverture de l'oracle (étiqueté honnête partout) ;
- un sabotage d'ampleur réduite, qui satisfait la garantie 2.

Ensemble, ils rendent tous les instruments « justes » sur les étiquettes et aveugles sur la réalité. Le coût est faible (illustratif), car il ne demande aucune connaissance des moniteurs.

Le dispositif de C ne détecte pas ce scénario : il ne mesure ni le taux de faux négatifs de l'oracle ni le dommage résiduel par épisode.

**Second scénario conjoint.** Si toutes les mesures avant l'entretien passent par une même partie qui voit les traces (Faille 6), un « adversaire » n'a pas besoin d'évasion. La connivence se fait au choix des couches, des seuils et des contrôles appariés. C'est le cas que la question (point 1) demande d'exclure, et C ne l'exclut pas.

---

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Organisme placebo.** Un organisme produit par le même bras, par la même chaîne, avec le même budget de modification, mais sans objectif de sabotage. Toute sonde qui sépare le placebo du modèle honnête aussi bien qu'elle sépare le saboteur détecte la modification, pas le sabotage (Faille 1). C n'a pas ce contrôle.
2. **Épisodes dormants du saboteur.** Le même organisme, sur des épisodes où l'oracle n'atteste aucun sabotage, comparé au placebo sur les mêmes tâches. Sans ce contrôle, on ne peut pas trancher entre détection de l'épisode et détection de l'organisme.
3. **Contrefactuel de consigne, comme critère de décision.** Les paires (consigne d'attaque, exécution honnête) et (consigne neutre, sabotage attesté par l'oracle), reprises du tableau de C, s'appliquent à tous les instruments, y compris le prédicteur 0,866. Une sonde qui suit la consigne et non l'épisode est disqualifiée, quelle que soit son AUROC.
4. **Sous-bras « informé-leurre ».** Il reçoit une description publique des moniteurs, de même format et de même longueur, mais non informative, avec un budget d'essais égal. Δ(informé − leurre) isole l'effet de l'information. Δ(leurre − aveugle) isole l'effet du format. Sans ce contrôle, l'Exp. 2 ne mesure pas ce que la section A des faits annonce (Faille 8).
5. **Audit des faux négatifs de l'oracle.** Il faut un sous-ensemble de sabotages connus du bras rouge, scellé et non communiqué à l'oracle, pour mesurer son rappel. Sans cela, le scénario conjoint du (b) est invisible. C'est la seule réponse à la Faille 10 qui ne suppose pas un second oracle infaillible.
6. **Couche et hyperparamètres figés, avec contrôle de significativité.** Une seule couche (ou un petit nombre) préenregistrée. Une distribution nulle par étiquettes permutées (reprise de l'Exp. 1 de C), calculée sur la même procédure de sélection que la sonde réelle. Sinon, le maximum sur les couches passe pour un signal (Faille 5).
7. **Évaluateur tiers et journal d'information.** Une partie distincte de la défense et du bras rouge exécute les instruments et ne restitue que des agrégats. Un journal horodaté consigne ce que chaque sous-bras a pu voir, pièces publiques comprises (Failles 6 et 9). Ce n'est pas une mesure, mais sans cela aucune mesure n'est opposable à un jury sur la question de la connivence.
8. **Diversité de famille entre oracle, juges et organismes.** C'est le contrôle de la connivence statistique (idée de C, a.1). La même évaluation est répétée avec un oracle ou un juge d'une famille de préentraînement différente de celle des organismes. Une chute de performance quand on brise la parenté signale une convergence et non une détection.

---

### Duel proposé pour la faille la plus coûteuse (B4)

Ce duel vise la Faille 1. Il sert à rendre la critique réfutable, sans remplacer les expériences de C.

- **H_A (détection d'organisme)** : l'AUROC d'une sonde sur (saboteur contre honnête) est égale, à l'erreur près, à son AUROC sur (placebo contre honnête). Sur (saboteur dormant contre placebo), l'AUROC est ≈ 0,5 (illustratif).
- **H_B (détection d'épisode)** : l'AUROC sur (placebo contre honnête) est ≈ 0,5. L'AUROC sur (saboteur en sabotage contre saboteur dormant) est nettement supérieure à 0,5. Les seuils sont à préenregistrer et sont illustratifs ici.
- **Issues** :
  - si la sonde sépare le placebo de l'honnête, H_B est réfutée et toute AUROC antérieure sur R-610 est requalifiée en détection d'organisme ;
  - si le placebo est au hasard et que la séparation intra-organisme tient, H_A est réfutée.
- **Champs fermés** :
  - `critère de porte visé` : validité de G1, absence de connivence ;
  - `raison de refus TAIF levée` : portée (« vous détectez vos propres organismes, pas le sabotage ») ;
  - `moniteur éprouvé` : sondes boîte blanche, y compris celle qui lit la consigne ;
  - `coût estimé (USD) et délai` : à deviser par la fille, aucun chiffre ici ;
  - `ce qui la réfuterait` : les deux issues ci-dessus ;
  - `pièce publique ou scellée produite` : agrégats publics ; organisme placebo et épisodes scellés.

---

### Ce que je retiens de C, en le disant

Je garde trois éléments de C :
- la critique (a).3 : échapper à des moniteurs déjà au hasard ne démontre rien ;
- la garantie 3, sur les couches figées avant l'exposition ;
- les paires contrefactuelles du tableau.

Ce sont les meilleurs éléments de C. Plusieurs de ses propres expériences les violent : l'Exp. 1 viole la garantie 3, et la règle de décision de l'Exp. 1 ignore les paires contrefactuelles.

FIN-DE-CELLULE
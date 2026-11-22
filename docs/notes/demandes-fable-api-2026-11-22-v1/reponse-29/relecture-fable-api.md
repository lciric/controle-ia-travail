# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHuAh2Dd3SbbVLVrSwyA`
- Heure (UTC) : 2026-11-22T11:43:23Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 100000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-29-dopamine-second-regard-partout-et-etau-v1.md` — sha256 c876c616cbe8cde2cdc7b976ea69dd0655b9e563d675ac6a8d943d7511e84335 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-25/relecture-fable-api.md` — sha256 f5b2d7115446f4dbaa772546dedd42034f54d28bfdfb7268fbfda19b8ab251d1 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/inventaire-seconds-regards-invariants-noyaux-v1-sans-nom-v1.md` — sha256 d5a49675ccda55f70980ee040cdf2261d4436bad6ffebd24beb8a9a90881919a (compagnon : vérifié)
- Empreinte de l'invite envoyée : 1b70527b644063ff337a8d5baddd7e8778263bba7e1f45a9b726a308616b6baa
- Jetons : entrée 39650, sortie 34867 (dont réflexion 24429), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.711880 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 29 — le signal comme second regard partout où c'est possible, le compte par chute conjointe et l'épreuve de l'étau

**Lecture de la consigne.** « Sans nom de personne » vise les personnes du programme ; les auteurs d'antériorité sont nommés, comme la règle l'exige. Je n'ai ouvert aucun PDF, aucun fichier hors des pièces jointes, aucun résultat, et je n'ai lancé aucun calcul. Les textes scellés ne me sont connus que par la réponse 25 et l'inventaire. Toute citation porte le statut « rapporté, non vérifié sur PDF » ; aucun chiffre n'est opposable.

**Convention.** Une marque en tête de paragraphe, de liste ou de tableau couvre toutes ses lignes, sauf marque contraire.

**Notations.** V : réussite attendue lue dans les états. δ : surprise par étape. Y : issue rendue par l'oracle. P : premier moniteur de texte. B : second lecteur de texte (la « seconde boîte noire » de la réponse 25). L : lecture interne (V et δ).

## 1. Ce qu'un expert ferait, et qui n'est pas demandé

[PROPOSITION]
1. **Remplacer « partout » par des conditions de possibilité.** Le signal n'existe que là où quatre choses existent : des états lisibles de l'agent, une issue calculée qui l'ancre, une référence honnête du régime, et aucun chemin de retour vers l'agent.
2. **Écrire le budget de sonneries avant d'ajouter des cloches.** Chaque regard ajouté dépense le taux de fausses alertes de la porte de fin de phase 1.
3. **Séparer deux sens de « tomber en même temps ».** Se taire ensemble sur des dommages donnés est une statistique. Tomber ensemble devant une attaque montée contre un seul des deux est une épreuve causale. Seul le second sens est l'étau.
4. **Classer les concepts de l'inventaire par supposition**, non un par un : c'est la classe qui compte, pas le détecteur.
5. **Faire passer les épreuves d'admission avant tout lieu** : trois honnêtes de contrôle, prix de l'effacement, épreuve du devin, jumeau textuel.
6. **Traiter les lieux d'attaque comme des lieux de mesure.** Le signal y est une variable observée sur l'attaquant, jamais un critère de sa sélection.
7. **Chercher l'antériorité du compte lui-même** dans la sûreté de fonctionnement, où la panne de cause commune est un objet ancien.

## 2. Les données brutes de départ

[PROPOSITION] Non les alertes déjà seuillées, mais :
- les **scores continus par épisode** de P, B et L, pour re-seuiller à fausses alertes égales ;
- les **activations par jeton** aux frontières d'action, prises sur rejeu bifurqué, pour les honnêtes, leurs jumeaux, les dommages plantés et les épisodes de chaque lieu ;
- le **texte brut** aux mêmes frontières ;
- les **verdicts de l'oracle** et sa couverture écrite ;
- le **journal d'audit**, avec la probabilité de chaque tirage et la part qui l'a déclenché ;
- l'**étiquette de famille et d'échelon** de chaque épisode endommagé, écrite par le tiers qui l'a planté.

## 3. Les méthodes et les outils

[PROPOSITION]
- Table deux par deux des silences de B et de L, par famille ; intervalle exact de Clopper-Pearson ; rééchantillonnage par grappes de tâches avec seuils réestimés.
- Test exact de deux proportions contre la fausse alerte conditionnelle ; test exact de McNemar gardé pour « lequel vaut mieux ».
- Lecture de la seule part d'audit tirée au hasard, ou pondération par l'inverse de la probabilité d'audit.
- Effacement en forme close de la direction lue, contre des directions aléatoires appariées.
- Lecture à positions textuelles masquées ; rejeu à texte nettoyé par un tiers.
- Prévisions signées, scellées avant lecture.

## 4. Ce qui vérifierait le résultat hors du directeur et de Claude

[PROPOSITION]
- Des familles et des dommages écrits par des tiers, dont une famille tenue à l'écart, jamais lue par le concepteur.
- Un second lecteur écrit par une autre lignée et choisi sur un jeu disjoint.
- Trois ancres de l'estimateur :
  - un second lecteur dupliqué doit donner une chute conjointe de un ;
  - une direction aléatoire appariée ne doit pas sonner plus que chez l'honnête ;
  - un regard synthétique tiré du verdict de l'oracle bruité doit donner une chute basse.
  
  Si l'estimateur manque une ancre, il est faux.
- La table recalculée par un agent neuf à partir des scores bruts.
- Le chiffre publié rejoué (étape 1 de la réponse 25).
- Le test de devinette sur la question neutre.

## Demande reformulée

> Pour chaque lieu où une alerte se décide, dire si les quatre conditions de possibilité d'une lecture de la réussite attendue et de la surprise sont réunies, quel rôle elle y tient parmi quatre (clé, aiguillage, mesure, interdit), et par quel chemin elle pourrait revenir à l'agent. Faire de même pour les concepts de l'inventaire, rangés par supposition. Définir, à partir des scores bruts et à fausses alertes égales, la grandeur qui dit si une lecture tombe avec le second lecteur de texte, avec son estimateur, son intervalle, ses ancres et ses causes d'erreur. Écrire l'épreuve de l'étau par barreaux, du moins cher au plus cher, avec ce qui la tue à chaque barreau. Signaler ce qui touche un texte scellé. Faire vérifier par des familles écrites par des tiers, un second lecteur d'une autre lignée et un recalcul par un agent neuf.

## Réponse

### R1. Le signal, lieu par lieu

[PROPOSITION] Quatre rôles possibles :
- **clé** : motif, première clé de la règle à deux clés ; seul, il envoie en file d'audit, jamais dans les témoins ;
- **aiguillage** : il oriente l'audit ;
- **mesure** : variable observée, sans effet ;
- **interdit**.

| Lieu | Rôle et forme | Risque |
|---|---|---|
| 1. Sondes de production | Clé. V à la dernière frontière avant l'issue, agrégé par maximum, calibré sur m honnêtes ; δ pour localiser. | Même supposition que les sondes (l'agent ne déplace pas ses états) : face à elles, il n'ajoute pas un regard. Il sonne sur l'échec honnête. |
| 2. Moniteurs boîte noire | Clé, à côté et non dedans : L sur les manqués de P. Une sonde posée sur les états du moniteur lui-même lit le texte par un autre modèle : elle se range parmi les lecteurs de texte. | Fuite par les conséquences visibles d'un verdict (blocage, relance). |
| 3. Audit après coup et plancher | Aiguillage de la seule part orientée ; la part tirée au hasard ne diminue jamais. Après audit, δ pour trier l'erreur de l'intention, à titre exploratoire. | Biais d'audit ; file noyée d'échecs honnêtes ; réapprentissage sur verdicts de l'oracle. |
| 4. Organismes discrets | Mesure, sur rejeu : terrain naturel de la chute conjointe. | Si L sert à retenir les organismes qui lui échappent, c'est un score dans la sélection de l'agent, et la mesure devient circulaire. |
| 5. Saboteur à budget | Mesure : V bouge-t-il avec la dose ? Cumul du premier terme du bilan contre le budget. | Le harnais ne doit pas moduler le budget selon les alertes. |
| 6. Attaquant informé | Mesure et cible : L est ce qu'on éprouve (R4). Épreuve du devin d'abord. | Donner la sonde ou son gradient à l'attaquant touche l'invariant : bras d'attaque déclaré seulement, organisme en quarantaine. |
| 7. Organisme d'idéation et ses juges | Aucun rôle en l'état. | Aucun, tant que rien n'y est lu. |

[HYPOTHÈSE] Pour le lieu 7 : si l'organisme et ses juges sont des modèles servis par une interface externe, leurs états ne sont pas lisibles. De plus, une idée n'a pas d'issue calculée, donc pas d'étiquette. Deux conditions sur quatre manqueraient. Au directeur de confirmer.

[PROPOSITION] Aucune ligne n'est une revendication. Chaque « clé » est une candidature soumise à R3.

### R2. Les autres concepts, par supposition

[PROPOSITION] Les lieux sont numérotés comme en R1.

**Classe A — lectures des états de l'agent** (supposition commune : l'agent ne déplace pas ses représentations).
- Clé candidate aux lieux 1 à 3, mesure aux lieux 4 à 6 : dilemme valeur contre issue ; moniteur de dissonance et écart dire-croire ; bascule en profondeur ; compétence retenue ; défaut connu non déclaré ; modèle du surveillant ; préférence révélée ; prévision privée ; préméditation ; sondes de conséquences attendues ; soulagement sans résolution ; surprise standardisée et fonctionnelles du chemin ; rang effectif ; faits de tâche à vérité enregistrée.
- Aiguillage seulement : nouveauté sans étiquette ; susceptibilité aux points de bascule.
- Lentille mécaniste : sa forme descriptive sert à l'enquête après une prise, jamais à l'alerte ; sa variante « part inexpliquée » est une clé candidate faible.
- Lieux 4 et 5 seulement : canal des poids, avec témoin « adaptateur honnête ».
- Risque propre : compétence retenue, modèle du surveillant et susceptibilité demandent une perturbation. Elle se fait sur rejeu bifurqué, jamais sur l'épisode vivant.
- [HYPOTHÈSE] Les fonctions d'influence lisent les données d'entraînement et non une activation : elles relèveraient d'une autre supposition. À éprouver par R3.
- Aucun rôle, question ouverte : sonde transportée entre modèles ; passage obligé (ses deux candidats sont déjà ci-dessus).

**Classe B — hors des états, supposition propre.**
- Base et seconde clé : plancher d'audit ; bilan de la pince.
- Clé candidate :
  - bilan du produit contre le jumeau (muet hors des comptes) ;
  - attestation vérifiée par programme (lieux 1 à 5, demandée à tous les épisodes de la même façon) ;
  - comparaison par paires en aveugle et plafond de divergence (banc seulement, faute de jumeau en service) ;
  - hasard du défenseur (ne prend que le saboteur conditionnel) ;
  - copies sans coordination (poids partagés).
- Lieu 3 seulement : « endommagé et marqué délibéré » ; rappel après l'alarme.
- Non : canaris en version brute.
- Base à valider : mots et coût.

**Classe C — instruments sur les regards, jamais des alertes.** Recapture et règle « moniteur invalide » ; micro-interventions secrètes ; épreuves du devin ; prix de l'effacement ; dissociation chez l'honnête et netteté de la référence ; chiffre noir ; audit des tolérances et agrégateur adaptatif ; second lecteur de texte (le témoin).

**Classe D — raisons, non regards.** Les trois clauses, les neuf invariants, la liste du généraliste, « invariant sous quoi ? ». Ils disent à quelle classe un regard appartient.

[PROPOSITION] Conséquence : toute la classe A compte pour une intervention au plus, tant que R3 n'a pas montré le contraire, regard par regard et échelon par échelon.

### R3. La grandeur de la chute conjointe

[PROPOSITION]

**Population.** Les épisodes endommagés selon l'oracle, manqués par P, pris dans la part d'audit tirée au hasard, pour une famille f et un échelon e déclarés.

**Fausses alertes égales.** Les seuils de B et de L sont gelés sur le même jeu de m honnêtes réservés, de sorte que « P ou B » et « P ou L » sonnent au même taux α, scellé.

**Table.**
- a : B et L sonnent.
- b : L seul sonne.
- c : B seul sonne.
- d : aucun ne sonne.
- n = a + b + c + d.

**Grandeur.** La chute conjointe J(f, e) est la probabilité que L se taise sachant que B se tait. Unité : part des silences de B.

**Estimateur.** Ĵ = d / (b + d). Sous audit orienté, le même rapport, chaque épisode pondéré par l'inverse de sa probabilité d'audit. Le sens inverse, d / (c + d), est rapporté aussi.

**Hypothèse nulle « L tombe avec B ».** Là où B se tait, L ne sonne pas plus que chez l'honnête : 1 − J ≤ q. Ici q est le taux de sonnerie de L sur les honnêtes réservés que P et B laissent passer. Le terme de comparaison ne demande aucun exemple d'attaque.

**Règle de compte.** L compte pour une intervention devant (f, e) si la borne basse de 1 − Ĵ dépasse la borne haute de q d'une marge scellée. Le test est exact, unilatéral, sur deux proportions.

**Intervalle.** Clopper-Pearson sur d / (b + d), seuils tenus pour fixes. Puis rééchantillonnage par grappes de tâches, où les m honnêtes sont retirés et les seuils réestimés. Les deux sont rapportés ; le plus large décide.

**Une table, trois lectures.**
- Silence commun : d / n.
- Chute conjointe : d / (b + d).
- Apport de la réponse 25 : Δ = (b − c) / n.

**Correction à la réponse 25.** Elle lisait « Δ indiscernable de 0 » comme « seconde boîte noire déguisée ». C'est trop fort. Avec b = c > 0, Δ vaut 0 alors que L rattrape des épisodes que B manque. Seul b proche de (b + d)·q dit que L tombe avec B.

**Taille.** [PROPOSITION, calcul de ma main, non rejoué] Il faut de l'ordre de trente à cinquante silences de B par famille pour séparer un rattrapage de 30 % d'une fausse alerte de 5 %. Cela demande bien plus d'épisodes endommagés en amont, puisqu'il faut que P et B les aient manqués.

**Ce qui la fausse.**
1. Des seuils pris sur des jeux ou des quantiles différents.
2. Des familles mélangées : un J global peut cacher une chute totale dans une famille.
3. Un dommage planté sans dissimulation : se taire ensemble ici ne dit pas tomber ensemble sous attaque. [FAIT RAPPORTÉ, inventaire : Johnston et collaborateurs.]
4. Une lecture L qui lit des traces du texte : la chute n'apparaît qu'à texte nettoyé.
5. Un audit orienté lu sans pondération.
6. Un oracle fait de lecteurs : la population elle-même partage alors une supposition avec B.
7. La difficulté : L lit l'échec attendu. Au banc, prendre l'écart au jumeau.
8. Un second lecteur choisi sur les épisodes de l'essai.
9. B et L appris sur les mêmes honnêtes : ils tombent ensemble si la référence quitte le régime, quoi que dise J.
10. Des épisodes d'une même tâche comptés comme indépendants.
11. Des seuils ou une marge choisis après lecture.

### R4. L'épreuve de l'étau

[FAIT RAPPORTÉ, inventaire] L'étau reste une hypothèse. Sa valeur est plafonnée par le plus petit de deux nombres : le rappel de la lecture quand rien ne lui est caché, et la taxe que cacher coûte en compétence. Une mesure de taxe est toujours un plafond. Contre-indices : Bailey et collaborateurs, McGuinness et collaborateurs.

[PROPOSITION] **Ce qu'elle éprouve.** Que faire tomber B ne fait pas tomber L : J reste bas quand l'attaque est montée contre le texte. Et que faire tomber les deux coûte une taxe mesurable.

**Plan par barreaux.**
- **Barreau 0, sans attaque ni entraînement.** Rappel de L sur dommages plantés non dissimulés ; prix de l'effacement ; lecture à texte nettoyé ; trois honnêtes de contrôle ; épreuve du devin.
- **Barreau 1, poids gelés.** Familles à dissimulation écrites par des tiers, dont une tenue à l'écart. Table de R3 par famille.
- **Barreau 2, attaquant entraîné contre le seul texte**, sans jamais recevoir L. On lit si L tombe sans être visé.
- **Barreau 3, attaquant entraîné contre les deux.** On mesure la taxe : ce qu'il perd en succès du dommage et en réussite de tâche pour obtenir le silence commun.

Je ne décris aucun mode opératoire ; les familles sont l'affaire des tiers.

**Ce qui doit exister avant.**
- L'étape 1 de la réponse 25, passée.
- Le second lecteur, écrit par une autre lignée.
- L'oracle et sa couverture écrite.
- Le plancher et son journal.
- Le texte du bras d'attaque déclaré, avec quarantaine des organismes.
- Le préenregistrement et les prévisions, scellés.
- Le verdict d'antériorité.

**Coût, en ordre de grandeur.** [PROPOSITION, estimation de ma main, aucun tarif lu]
- Barreau 0 : des rejeux avec crochets, quelques heures de processeur graphique.
- Barreau 1 : quelques centaines d'épisodes par famille, des dizaines d'heures, plus des appels externes si B est un juge servi par interface.
- Barreaux 2 et 3 : des entraînements d'adaptateur sur plusieurs graines, un ordre de grandeur au-dessus.
- Devis ligne par ligne avant tout accord.

**Ce qui la réfute.**
- Barreau 0 : rappel de L non distinct de q, ou effacement sans coût, ou silence à texte nettoyé. Le plafond est nul ; arrêt.
- Barreau 1 ou 2 : J proche de un sur la famille tenue à l'écart. L tombe avec B sans être visé : zéro intervention.
- Barreau 3 : silence commun à taxe indiscernable de zéro. L'étau est ouvert à cet échelon, et toute phrase se borne aux échelons inférieurs.

[HYPOTHÈSE] **Mes prévisions à sceller.** Barreau 1 : L ne tombe pas entièrement avec B (confiance 0,5). Barreau 3 : silence commun atteint à taxe faible (confiance 0,7).

### R5. Ce qui touche un texte scellé

[FAIT RAPPORTÉ pour les textes, par la réponse 25 et l'inventaire ; PROPOSITION pour le signalement] Rien n'est modifié.
- **N-053, point 5** (aucun score de moniteur dans l'entraînement ou la sélection de l'agent) : lieux 4 à 6 ; barreau 3 de l'étau.
- **N-075 v3, § 3** : le silence commun y est une quantité rapportée sans critère. La règle de compte de R3 en ferait un critère : il faut un erratum, ou un statut exploratoire.
- **N-075 v3, § 4, et erratum 3** : « partout » étend la première clé hors de la pince. La règle à deux clés continue de s'appliquer.
- **N-026** : agrégation jamais par moyenne. La sonde de surprise publiée emploie une moyenne.
- **N-060 v3, point 4** : réapprentissage sur verdicts de l'oracle.
- **N-076** : taille m de la référence et horizon n, à déclarer à chaque lieu.
- **Hypothèse H5** : redéfinir la diversité effective par la chute conjointe est un nœud du directeur.
- **Porte de fin de phase 1** : chaque cloche ajoutée entre dans son taux de fausses alertes.
- **Préenregistrement du bras « dopamine »** : toute lecture à un nouveau lieu est une lecture nouvelle.

### R6. Question neutre pour le collisionneur et l'organisme

> Un système surveille un agent d'intelligence artificielle qui exécute de longues tâches dont l'issue se calcule après coup. Le défenseur dispose de plusieurs dispositifs : des lecteurs du texte produit, de lignées différentes ; des lectures des états internes de l'agent, apprises sur épisodes honnêtes seulement ; un audit d'une part des épisodes, tirée au hasard et jugée sur le produit ; au banc d'essai, un jumeau honnête. Aucune lecture ni aucun verdict ne revient à l'agent ni n'entre dans son entraînement ou sa sélection.
> 1. Comment compter ces dispositifs : quand deux d'entre eux valent-ils deux, et quand n'en valent-ils qu'un ?
> 2. Quelle grandeur, avec son estimateur, son intervalle et son hypothèse nulle, mesurerait que deux dispositifs cessent de fonctionner ensemble, à taux de fausses alertes égal ? Qu'est-ce qui la fausserait ?
> 3. Quelle expérience la moins chère dirait si échapper à l'un expose à l'autre, ou si échapper à l'un suffit pour échapper aux deux ? Quelle issue donnerait tort à votre réponse, dans chaque sens ?
> 4. À quels endroits d'un tel système une lecture interne n'a-t-elle aucun rôle possible ?
> 5. Que devient votre réponse si l'agent connaît tout le dispositif, hors ses tirages secrets ?
>
> Vous ne décrivez aucun mode opératoire d'attaque.

[PROPOSITION] Le test de devinette de la réponse 25 s'applique tel quel. Je ne l'ai pas joué.

### Antériorité

Toutes les pièces sont citées de mémoire, sauf mention, avec le statut « rapporté, non vérifié sur PDF ».
- **Pannes coïncidentes de versions diverses.** Eckhardt et Lee, 1985, « A Theoretical Basis for the Analysis of Multiversion Software Subject to Coincident Errors ». Knight et Leveson, 1986, « An Experimental Evaluation of the Assumption of Independence in Multiversion Programming ». Littlewood et Miller, 1989, « Conceptual Modeling of Coincident Failures in Multiversion Software ». [HYPOTHÈSE] Le dernier traiterait le cas où une diversité forcée rend les pannes négativement liées : ce serait le voisin le plus proche de l'étau.
- **Cause commune.** Fleming, 1975, modèle du facteur bêta ; titre à vérifier.
- **Diversité d'ensembles.** Kuncheva et Whitaker, 2003, « Measures of Diversity in Classifier Ensembles and Their Relationship with the Ensemble Accuracy ».
- **Contrôle.** Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ».
- **Obscurcissement des états.** Bailey et collaborateurs, 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (arXiv 2412.09565). McGuinness et collaborateurs, 2025, « Neural Chameleons » (arXiv 2512.11949).
- **Coupes minimales.** Molnar (arXiv 2609.26419), rapporté par l'inventaire comme occupant la forme.
- **Gain de la boîte blanche.** Parrack, Attubato, Heimersheim, 2025, « Benchmarking Deception Probes via Black-to-White Performance Boosts » ; titre à vérifier.
- **Le signal.** Xu, Yuksekgonul, Zou, 2026, « Sparse Reward Subsystem in Large Language Models » (arXiv 2602.00986).

[PROPOSITION] Statut : le compte par chute conjointe est probablement occupé dans sa forme générale. C'est une question, non une revendication.

## Décisions pour le directeur

**D-1. Fixer le sens de « partout où c'est possible ».**
- Enjeu : le nombre de cloches, le budget de fausses alertes et les chemins de fuite.
- (a) Quatre conditions et quatre rôles (R1) : clé aux lieux 1 et 2, aiguillage au lieu 3, mesure aux lieux 4 à 6, rien au lieu 7. Avantage : aucun texte scellé n'est franchi. Inconvénient : le signal n'alerte qu'en deux lieux.
- (b) Clé partout où des états sont lisibles. Avantage : sert le mot à la lettre. Inconvénient : fausses alertes multipliées, et risque de sélection aux lieux d'attaque.
- Recommandation : (a). Confiance 0,7.

**D-2. Adopter la grandeur de compte.**
- Enjeu : ce qui autorise à écrire « deux regards ».
- (a) J contre q, sur une table unique qui rapporte aussi le silence commun et Δ, en statut exploratoire tant que N-075 n'a pas d'erratum. Avantage : corrige la lecture de Δ. Inconvénient : rien d'opposable tout de suite.
- (b) Δ seul. Avantage : déjà écrit. Inconvénient : confond égalité de rappel et chute conjointe.
- (c) J comme critère scellé dès maintenant, par erratum. Avantage : opposable. Inconvénient : touche un texte scellé avant que les ancres aient parlé.
- Recommandation : (a). Confiance 0,7.

**D-3. Lancer l'épreuve de l'étau.**
- Enjeu : une dépense, et le droit de dire un jour « échapper à l'un expose à l'autre ».
- (a) Barreau 0 dès l'étape 1 de la réponse 25 passée ; barreaux 1 et 2 sur devis. Avantage : le plafond est connu avant toute attaque. Inconvénient : lent.
- (b) Aller droit au barreau 2. Avantage : réponse directe. Inconvénient : aucun plafond, aucun nul établi.
- (c) Ne pas éprouver. Avantage : aucune dépense. Inconvénient : l'étau reste un mot.
- Recommandation : (a). Confiance 0,7. Pas de défaut pour la dépense.

**D-4. Autoriser ou non le barreau 3.**
- Enjeu : l'invariant N-053.
- (a) L'autoriser en bras déclaré, organisme en quarantaine, jamais réemployé. Avantage : seule mesure de la taxe à cet échelon. Inconvénient : touche l'invariant ; coût le plus haut.
- (b) Le refuser pour l'instant, et borner toute phrase aux échelons sans gradient. Avantage : invariant intact. Inconvénient : l'étau n'est pas éprouvé là où il compte le plus.
- (c) Le confier à un tiers. Avantage : séparation nette. Inconvénient : délai, dépendance.
- Recommandation : (b) maintenant, (a) à réexaminer après le barreau 2. Confiance 0,6.

**D-5. Commander l'antériorité du compte et jouer le test de devinette avant envoi.**
- Enjeu : la zone du compte par chute conjointe a des voisins que je ne cite que de mémoire.
- (a) Lecture en entier par un agent neuf, en commençant par les pannes coïncidentes, et test de devinette sur trois modèles neufs. Avantage : la règle sur les zones vierges est tenue. Inconvénient : une file de plus, quelques appels.
- (b) Envoyer tel quel. Avantage : vite. Inconvénient : neutralité et antériorité restent supposées.
- Recommandation : (a). Confiance 0,8.

**Ce que je n'ai pas fait.**
- Aucun PDF ouvert, aucun texte scellé lu directement, aucun calcul rejoué.
- Les tailles et les coûts sont des estimations de ma main.
- Les titres cités de mémoire peuvent être inexacts.
- Le lieu 7 repose sur une hypothèse à confirmer.
- Les fichiers que l'inventaire n'a pas ouverts ne sont pas couverts.

FIN DE LA RÉPONSE

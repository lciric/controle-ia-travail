# Proposition A, tour III.1

**Pièces.** FAITS et QUESTION reçus et apparemment complets ; je n'ai pas recalculé les empreintes sha256. Le tour est à l'aveugle : je n'ai vu aucune autre proposition et n'en critique donc aucune.
**Références.** Les faits ne donnent aucun titre : je désigne chaque travail par sa description dans les faits, et tous sont « référence à vérifier ».
**Livrable.** (a) est en §1, (b) en §7, (c) en §3, (d) en §4 et §7.
**Chiffres.** Tous les seuils et coûts ci-dessous sont **illustratifs**, à fixer au préenregistrement. Les notes de 1 à 5 sont mes jugements, pas des mesures.

## 1. Ce qu'un expert ferait, et que la question ne demande pas

**Il vérifierait d'abord que la règle de mesure existe.** La question demande quoi ajouter. Un expert demanderait si le dommage et le soupçon sont mesurables à la dose où la menace est réellement diffuse. Deux planchers en décident, et aucun n'apparaît dans les faits :
- le bruit de l'oracle entre deux jumeaux honnêtes (test A/A) ;
- la dérive du score de sonde entre conditions honnêtes.

Le second est structurel. Dans une accumulation séquentielle, un biais d'étalonnage du nul croît comme le nombre de pas, le bruit comme sa racine. Un écart petit entre l'honnête d'étalonnage et l'honnête de service finit donc par déclencher l'alerte, ou force des seuils qui ôtent la puissance. La grandeur qui décide est alors un rapport, pas une AUROC : décalage par pas dû au sabotage, divisé par la dérive du nul honnête.

**Il validerait les organismes avant les parades.** Si le saboteur à adaptateur se comporte comme l'organisme distillé publié, « remis d'aplomb même par des récompenses tirées au hasard » (VÉRIFIÉ), alors tout entraînement « marche » sur lui. Aucun résultat d'entraînement n'y serait interprétable, y compris celui du bras d'attaque déjà prévu.

**Il remarquerait que le bras d'attaque et la parade par entraînement sont la même optimisation.** Les règles interdisent que l'oracle entre dans un signal d'entraînement (VÉRIFIÉ). Le bras d'attaque ne peut donc pas maintenir le sabotage par construction : il consiste à entraîner le saboteur à faire baisser un score de sonde. Seule la lecture du résultat le distingue d'une parade. Si l'on y mesure seulement l'évasion, on ne saura pas si le sabotage a été caché, déplacé ou retiré. Ce qui manque est une lecture du dommage après entraînement, pas un chantier nouveau.

**Il écrirait les conditions d'arrêt avant l'ambition** : quel résultat ferme quelle ligne.

**(a) Ce que la question suppose sans que ce soit établi :**

| Supposition | Statut |
|---|---|
| Les saboteurs du programme se représentent leur sabotage | HYPOTHÈSE (faits) |
| La tenue des saboteurs à un entraînement est connue | Non : OBSERVÉ-NON-AUDITÉ qu'elle n'a pas été mesurée |
| L'adaptateur ressemble aux saboteurs qui résistent plutôt qu'à l'organisme fragile | OBSERVÉ-NON-AUDITÉ qu'on ne le sait pas |
| Une sonde peut fonctionner sur une tâche difficile à noter | OBSERVÉ-NON-AUDITÉ : aucune mesure trouvée, dans aucun sens |
| Les combinaisons des trois voies avec lecture interne sont libres | OBSERVÉ-NON-AUDITÉ : pas de recherche d'antériorité complète |
| La dose-réponse existe pour les deux familles | VÉRIFIÉ qu'elle manque pour la consigne cachée |
| L'oracle du banc reconnaît le dommage aux doses faibles | HYPOTHÈSE (de A) ; RAPPORTÉ qu'un juge sur produit peut être trompé |
| Détecter, auditer, entraîner sont trois voies séparables | HYPOTHÈSE (de A) ; VÉRIFIÉ qu'un entraînement ordinaire ôte leur séparation à des sondes apprises hors domaine |
| Un résultat à huit milliards de paramètres vaut plus haut | HYPOTHÈSE (de A) |
| « Ambitieux » tient avec une personne et trois chantiers | HYPOTHÈSE (de A) ; la contrainte elle-même est VÉRIFIÉE |

## 2. Les données brutes de départ

À prendre avant toute courbe ou moyenne :

1. **Transcriptions pas à pas**, saboteur et jumeau, appariées par article et par graine, sans agrégation.
2. **Scores de sonde par pas et par couche**, et les activations brutes d'un sous-ensemble pour pouvoir réentraîner des contrôles.
3. **Sorties brutes de l'oracle**, texte du jugement compris, par épisode. Y inclure des paires jumeau/jumeau à graines différentes si elles existent ; je ne sais pas si elles existent.
4. **Les quatre doses de l'adaptateur en valeurs par épisode.** Les faits ne disent pas ce qu'est le paramètre de dose ; je ne sais pas, et il faut l'écrire avant de construire la courbe de la consigne cachée.
5. **Données et réglages d'entraînement de l'adaptateur**, pour fabriquer un adaptateur bénin par le même procédé.
6. **Journal de ce qui a déjà été regardé**, pour savoir quelles familles ne sont plus « lues une seule fois ».
7. **Lecture humaine à l'aveugle** d'un petit lot de paires, avant tout chiffre d'oracle.
8. **Relecture à la page** des trois faits RAPPORTÉS qui conditionnent des contrôles : la sonde qui signale presque tous les adaptateurs bénins, les dénégations mal classées, l'appui sur des indices du texte.

## 3. Ce que chaque voie peut établir

**Détecter (sondes accumulées).**
- *Peut établir* : qu'un état interne diffère d'une référence honnête, plus tôt que le produit ne le montre, à taux de fausses alertes contrôlé si le nul tient.
- *Ne peut pas établir* : qu'il y a dommage, puisqu'elle ne lit pas le produit ; ni rien sur un saboteur qui ne se représente pas son sabotage. Les dénégations mal classées sont RAPPORTÉES ; la représentation est une HYPOTHÈSE.
- *Exige* : un nul honnête stable, et un signal qui survive aux contrôles appariés.
- *Vaine si* : elle lit l'adaptateur, la consigne présente dans le contexte ou le texte ; ou si la dérive du nul est de l'ordre du signal par pas.

**Auditer (tirage au hasard, oracle sur le produit).**
- *Peut établir* : une borne, valide à tout instant, sur le taux de dommage que l'oracle reconnaît.
- *Ne peut pas établir* : le dommage que l'oracle ne voit pas.
- *Exige* : la sensibilité de l'oracle par dose et le taux honnête de référence (RAPPORTÉ).
- *Vaine si* : le dommage par épisode est sous le bruit de l'oracle. Au banc, le jumeau permet une différence appariée ; en service il n'y a pas de jumeau (VÉRIFIÉ).

**Entraîner.**
- *Peut établir, au banc* : que le dommage contre un jumeau entraîné à l'identique baisse.
- *Ne peut pas établir seule* : qu'elle a réussi en service. Le jeu d'audit publié dit que la détection reste nécessaire pour valider qu'un entraînement a réussi (VÉRIFIÉ).
- *Exige* : un entraînement indiscernable du service et une exploration non trichée (VÉRIFIÉ, conditions des travaux cités), plus un signal lié à la qualité.
- *Vaine si* : la note faible sature alors que la qualité diffère (annexe du papier de 2026, VÉRIFIÉ) ; ou si l'organisme est fragile, ce qui donne un succès trivial.

**Combinaisons et nuisances.**
- *Détecter vers auditer* : la sonde sert d'aiguillage. La borne reste valide si le tirage garde un plancher uniforme et des probabilités connues (proposition de A, schéma classique de pondération inverse). Le gain se mesure en audits économisés.
- *Entraîner contre détecter* : l'entraînement déplace le nul et peut ôter la séparation des sondes (VÉRIFIÉ pour des sondes hors domaine). D'où un cercle : la validation de l'entraînement repose sur un instrument que l'entraînement dérègle. Au banc, le cercle se rompt en entraînant aussi le jumeau.
- *Détecter vers entraîner* : c'est le « milieu » du billet de 2025, et c'est opérationnellement le bras d'attaque. Fermé hors bras déclaré.

**(c) Mesure minimale par instrument :**

| Instrument | Mesure minimale | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Sonde | Détection à fausses alertes fixées (1 %, illustratif), par épisode et par dose | Jumeau même article et graine ; adaptateur bénin de même procédé ; consigne cachée bénigne de même longueur | Classifieur de texte sur les sorties ; même sonde sur un lecteur tiers lisant la transcription ; bruit sur les poids (adaptateur) ; étiquettes permutées |
| Accumulateur | Taux réalisé de fausses alertes contre taux nominal sur épisodes honnêtes frais ; délai de détection par dose | Strates honnêtes absentes de l'étalonnage | Moyenne simple à seuil fixe |
| Juge de texte | Même mesure que la sonde, même point de fonctionnement | Les mêmes | Longueur, nombre de révisions, sac de mots |
| Oracle | Sensibilité par dose sur différence appariée ; distribution A/A ; rappel sur défauts plantés par édition documentée | Paires jumeau/jumeau | Notation humaine aveugle sur petit lot ; recouvrement lexical avec l'article |
| Saboteurs | Dose-réponse monotone au-dessus du plancher A/A ; part de dommage retenue après entraînement non informé | Jumeau soumis au même traitement | Entraînement à zéro pas (bruit de remesure) |

## 4. Les programmes possibles

Sur le risque d'antériorité, le fond de ma réponse est « je ne sais pas » : la recherche est incomplète (OBSERVÉ-NON-AUDITÉ). Les qualificatifs ci-dessous sont des jugements de A.

**P0. Ne rien changer.**
- *Thèse* : des sondes accumulées battent les moniteurs de texte sur une menace diffuse, chez un agent seul, puis en essaim.
- *Expérience centrale* : la porte sonde contre texte.
- *Réfuté si* : la sonde ne dépasse pas le texte sur famille inédite.
- *Exige* : des saboteurs qui se représentent leur sabotage ; un oracle supposé juste.
- *Coût* : trois lignes pour une personne, et des essaims lourds.
- *Risque d'antériorité* : moyen sur la détection, faible sur la tâche difficile à noter.
- *Défaut* : une victoire de la sonde resterait ambiguë (adaptateur ? texte ?), et le bras d'attaque serait illisible.

**P1. Instruments d'abord.**
- *Thèse* : aucun résultat du programme n'est lisible avant deux planchers et trois contrôles appariés.
- *Expérience centrale* : C1 et C2 (§7).
- *Réfuté si* : les planchers sont négligeables et les contrôles sans effet ; P0 était alors suffisant.
- *Exige* : les saboteurs actuels, un adaptateur bénin, un petit lot humain.
- *Coût* : faible.
- *Risque d'antériorité* : faible, et sans grande conséquence, car la mesure est propre au banc.

**P2. Audit aiguillé.**
- *Thèse* : la valeur de la lecture interne se compte en audits économisés à garantie égale.
- *Expérience centrale* : C4.
- *Réfuté si* : le gain est nul.
- *Exige* : un oracle dont la sensibilité par dose est connue ; les saboteurs actuels.
- *Coût* : rejeu sur données acquises.
- *Risque d'antériorité* : moyen, car l'audit est publié par d'autres (RAPPORTÉ) ; je ne sais pas s'il l'a été avec un aiguillage par sonde.

**P3. L'entraînement lu de l'intérieur.**
- *Thèse* : le programme ne revendique pas l'entraînement comme parade. Il fournit la lecture qui dit si un entraînement a retiré, caché ou déplacé le sabotage.
- *Expérience centrale* : C3 puis C5.
- *Réfuté si* : sonde gelée, sonde tenue à l'écart et jumeau entraîné ne distinguent pas les issues.
- *Exige* : un saboteur tenace, propriété inconnue aujourd'hui, et un jumeau entraîné à l'identique.
- *Coût* : moyen à lourd.
- *Risque d'antériorité* : le papier de 2026 laisse explicitement de côté le saboteur affiné, et aucune de ses expériences ne lit d'états internes (VÉRIFIÉ) ; le travail sur code vérifiable couvre le cas facile à noter. Au-delà, je ne sais pas.

**P4. Changer d'objet : le modèle honnête.**
- *Thèse* : l'objet de mesure devient le nul honnête, c'est-à-dire « à quel point un modèle honnête paraît suspect » (condition posée par le billet de 2025), sous changement d'article, d'adaptateur bénin et d'entraînement ordinaire.
- *Expérience centrale* : la carte de dérive du nul.
- *Réfuté si* : le nul est stable partout ; l'objet est alors sans intérêt et P0 est justifié.
- *Exige* : aucun saboteur pour le cœur, et aucune vérité du dommage.
- *Coût* : faible.
- *Risque d'antériorité* : je ne sais pas.
- *Limite* : ne dit rien de la détection elle-même.

**Ma proposition** : P1 comme socle, P2 en rejeu, P3 par étapes, et la carte du nul de P4 absorbée dans C1. Les essaims sont retirés ou différés.

**(d) Ancrage matériel.** L'agent est le modèle ouvert de huit milliards de paramètres ; une course coûte quelques dizaines de dollars (VÉRIFIÉ). Les faits ne nomment ni le modèle, ni le modèle de confiance, ni le juge, et je ne les invente pas. Les saboteurs publics de quatorze milliards tiennent a priori sur une carte louée : HYPOTHÈSE, à vérifier.

## 5. Ce qui, hors du programme, permettrait de vérifier

- **Dépôt horodaté chez un tiers** des préenregistrements, seuils compris.
- **Famille inédite fabriquée par quelqu'un d'extérieur**, que la directrice ou le directeur ne voit qu'à la lecture unique.
- **Organismes non fabriqués par l'équipe** : les saboteurs publics de quatorze milliards, sur lesquels les sondes sont nommées comme piste « sans les essayer » (VÉRIFIÉ). Les repères à battre y sont déjà publiés : moniteurs de texte et bruit sur les poids.
- **Oracle contre humains externes**, à l'aveugle, sur un petit lot de paires. Second oracle indépendant : la consigne durcie du papier de 2026, si elle est publiée (je ne sais pas).
- **Publication du nul honnête** (scores par pas), des sondes et des paires, pour qu'un tiers recalcule le taux de fausses alertes sur ses propres courses honnêtes.
- **Recherche d'antériorité complète**, faite par un tiers, avant toute revendication de nouveauté.

## 6. Reformulation exigeante de la tâche

Sur une tâche difficile à noter, pour les deux familles existantes puis une famille inédite, établir par expériences préenregistrées :

1. le plancher de l'oracle et la dérive du nul honnête, donc la plus petite dose à laquelle une garantie séquentielle existe ;
2. la part du signal de sonde qui survit aux témoins bénins appariés et aux repères mécaniques ;
3. le nombre d'audits économisés à garantie égale ;
4. si les saboteurs tiennent à un entraînement non informé, et alors seulement ce qu'un entraînement contre une sonde fait du sabotage : retiré, caché ou déplacé, lu contre un jumeau entraîné à l'identique.

Chaque issue ferme ou ouvre une ligne nommée d'avance. Aucun score de moniteur n'entre dans un entraînement hors bras déclaré, et aucun usage de l'oracle ne sert à choisir une sonde, un seuil ou une politique d'aiguillage.

## 7. Programme des priorités classé

| Chantier | Gain | Facilité | Portée | Découverte | Coût | Score |
|---|---|---|---|---|---|---|
| C2 Validité de construit de la sonde, avec la dose-réponse manquante | 5 | 4 | 4 | 3 | 2 | 120 |
| C4 Aiguillage d'audit (rejeu) | 4 | 4 | 4 | 3 | 2 | 96 |
| C3 Tri de tenue des saboteurs à l'entraînement | 5 | 4 | 3 | 3 | 2 | 90 |
| C1 Deux planchers : oracle A/A et dérive du nul | 5 | 4 | 4 | 2 | 2 | 80 |
| C5 Bras d'attaque lu à trois issues | 5 | 2 | 5 | 5 | 4 | 62,5 |
| C6 Troisième famille sans consigne | 5 | 2 | 5 | 4 | 4 | 50 |
| C9 Ancre externe (saboteurs publics) | 4 | 3 | 4 | 3 | 3 | 48 |
| C8 Corruptibilité des juges contre sondes | 3 | 3 | 4 | 3 | 3 | 36 |
| C7 Essaims | 3 | 2 | 3 | 3 | 4 | 13,5 |

**Sensibilité.**
- *Découverte comptée deux fois* : l'ordre devient C2, C5, C4, C3, C6, et C1 passe sixième.
- *Coût compté deux fois* : l'ordre devient C2, C4, C3, C1, C9, et C5 sort des cinq premiers.
- *Lecture* : les quatre premiers sont stables sous la seconde variation ; la cinquième place est instable entre C5, C6 et C9.
- *Ordre d'exécution* : le score ne voit pas la dépendance. C1 conditionne la lecture de C2 et C4, et C3 conditionne C5. L'ordre d'exécution est donc C1, C2, C4 en parallèle de C3, puis C5.

### C1. Deux planchers

- **H_A** : le nul honnête est stable. Le décalage de score par pas à la plus faible dose dépasse nettement la dérive entre strates honnêtes (articles, types de question, rang du pas, graines), et l'oracle A/A est resserré autour de zéro.
- **H_B** : la dérive, ou le bruit A/A, est du même ordre que le signal.
- **Métrique** : rapport R = décalage par pas / dérive maximale entre strates, avec intervalle par rééchantillonnage groupé par article ; taux réalisé de fausses alertes de l'accumulateur sur épisodes honnêtes frais ; dommage apparié à la plus faible dose rapporté à l'écart-type A/A.
- **Seuil** (illustratif) : H_A si la borne basse de R dépasse 3 et si le taux réalisé ne dépasse pas le nominal ; H_B si R est sous 1 ou si le taux réalisé dépasse deux fois le nominal ; entre les deux, indécis, à déclarer tel.
- **Contrôle négatif** : étiquettes saboteur/honnête permutées à l'intérieur de chaque article, pour lesquelles R doit être nul.
- **Coût** : rejeu, plus une dizaine de courses honnêtes ; quelques centaines de dollars (illustratif).
- **Ce que chaque issue falsifie** : H_A falsifie l'objection « garantie inapplicable au banc ». H_B falsifie la revendication d'une garantie de fausses alertes au-delà de la condition d'étalonnage : la ligne « détection dans le temps » doit alors être reconçue (étalonnage par strate ou test apparié) avant la porte.

### C2. Validité de construit

- **H_A** : la sonde lit quelque chose de propre au sabotage dans les états de l'agent, au-delà du texte et des artefacts.
- **H_B** : le signal s'explique entièrement par la présence d'un adaptateur, par celle d'une consigne cachée quelconque dans le contexte, ou par une information récupérable du seul texte produit.
- **Métrique** : séparation saboteur contre témoin bénin apparié, par épisode, avec découpage par article, moins le meilleur repère mécanique du tableau de §3. Pour la consigne cachée : monotonie du score avec la dose, sur la courbe à construire.
- **Seuil** (illustratif) : H_A si la borne basse de l'écart au meilleur repère dépasse 0,05 d'AUROC sur chaque famille ; H_B si l'intervalle contient zéro.
- **Contrôle négatif** : adaptateur bénin contre modèle de base, où la sonde doit rester au hasard ; sinon c'est un détecteur d'adaptateur, comme le suggère le fait RAPPORTÉ.
- **Coût** : un adaptateur bénin, un lot à consigne bénigne et les doses manquantes ; dix à vingt courses (illustratif).
- **Ce que chaque issue falsifie** : H_A falsifie « détecteur d'adaptateur ou de texte » pour ces deux familles seulement. H_B falsifie l'instrument central sur ce banc : la sonde est reconçue, puis jugée sur famille inédite lue une fois (règle en vigueur), ou bien la porte « interne contre texte » est concédée.

### C3. Tri de tenue des saboteurs

- **H_A (fragile)** : un entraînement sans information sur la qualité ramène le dommage au plancher A/A. Ce peut être des récompenses au hasard, comme dans le travail publié, ou un réglage fin sur des traces bénignes hors tâche.
- **H_B (tenace)** : le dommage persiste.
- **Métrique** : part de dommage retenue, dommage après / dommage avant, lue contre un jumeau soumis au même entraînement.
- **Seuil** (illustratif) : fragile sous 0,2 ; tenace au-dessus de 0,8.
- **Contrôle négatif** : entraînement à zéro pas (bruit de remesure) ; jumeau entraîné seul (perte de capacité).
- **Coût** : deux familles, deux traitements, quelques graines ; une dizaine de courses (illustratif).
- **Ce que chaque issue falsifie** : H_A falsifie l'interprétabilité de tout résultat d'entraînement sur cet organisme, bras d'attaque compris ; C5 attend alors la troisième famille. H_B falsifie l'assimilation de l'adaptateur à l'organisme publié jugé peu robuste et autorise C5.
- **Règle touchée, je le déclare** : aucun score de moniteur ni d'oracle n'entre dans le signal, mais l'agent est entraîné, alors que « corriger en entraînant l'agent n'est pas ouvert ». Je propose un « bras de caractérisation » déclaré, sans prétention de parade. C'est une modification de périmètre que la direction doit trancher.

### C4. Aiguillage d'audit

- **H_A** : un tirage aiguillé par la sonde, avec plancher uniforme et probabilités connues, atteint une borne donnée avec moins d'audits qu'un tirage uniforme.
- **H_B** : aucun gain ; la sonde n'informe pas sur le dommage que l'oracle reconnaît.
- **Métrique** : rapport du nombre d'audits (uniforme / aiguillé), en rejeu sur mélanges saboteur/honnête par dose ; couverture empirique de la borne.
- **Seuil** (illustratif) : H_A si la borne basse du rapport dépasse 1,5 ; H_B si l'intervalle tient dans [0,8 ; 1,25].
- **Contrôle négatif** : scores permutés entre épisodes, rapport attendu de 1. Repères à battre : aiguillage par le juge de texte et par la longueur.
- **Garde-fou** : la politique d'aiguillage est figée avant toute lecture de l'oracle ; sinon l'oracle sélectionnerait un moniteur, ce qui est interdit.
- **Coût** : processeur seul si les jugements d'oracle existent ; sinon le coût de l'oracle sur le lot (illustratif).
- **Ce que chaque issue falsifie** : H_A falsifie « sondes superflues dès lors que la garantie est dans l'audit ». H_B falsifie la phrase du programme « les sondes en sont l'accélérateur et l'aiguillage » à ces doses.

### C5. Bras d'attaque lu à trois issues (phase suivante, si C3 donne « tenace »)

- **H_A** : entraîner l'agent contre une sonde gelée fait baisser le dommage contre le jumeau (politique honnête). C'est ce que le travail sur code vérifiable obtient avec une forte régularisation et sans gradient à travers le détecteur.
- **H_B** : le score baisse et le dommage reste (états obscurcis ou texte qui se justifie).
- **Métrique** : le couple (score de la sonde visée, part de dommage retenue), complété par une sonde tenue à l'écart de l'entraînement et par le juge de texte.
- **Seuil** (illustratif) : H_A si la part retenue est sous 0,3 ; H_B si elle dépasse 0,7 avec un score revenu au niveau honnête.
- **Contrôle négatif** : jumeau entraîné à l'identique (nouveau nul, et mesure de la perte de séparation par entraînement ordinaire) ; entraînement contre une sonde de direction aléatoire. Si le dommage y chute autant, l'effet vient de la fragilité, pas de la sonde.
- **Coût** : plusieurs dizaines de courses, dans un bras déjà prévu (illustratif).
- **Ce que chaque issue falsifie** : H_A falsifie « l'entraînement contre une lecture interne ne produit que de l'évasion » sur ce banc. Elle ne change aucune règle par elle-même. H_B falsifie le transport à une tâche difficile à noter du jugement publié « viables comme signal d'entraînement », dans ce régime, et livre la mesure d'évasion attendue.

### Calendrier

- **Avant la porte d'instruments** (trois chantiers actifs au plus) : C1 et C2 forment un seul chantier « instruments » ; C4 est en rejeu ; C3 se fait si le bras de caractérisation est accordé. C1 doit être lisible pour l'entretien du 1er décembre. Je ne sais pas combien de semaines restent.
- **Ce qui attend** : C5, après C3 ; C6, au devis, parce que c'est le seul test direct de l'HYPOTHÈSE de représentation ; C9 ; C8, à la porte suivante.
- **À ne pas faire** :
  - les essaims avant un nul établi chez l'agent seul ;
  - utiliser l'oracle pour choisir une sonde, un seuil ou un aiguillage ;
  - relire une famille inédite ;
  - entraîner contre une sonde hors bras déclaré ;
  - présenter comme parade un entraînement réussi sur un organisme non trié ;
  - présenter une garantie comme venant des sondes ;
  - publier le détail de fabrication des saboteurs au-delà de ce que la réplication exige.

**Réponse à la question de l'entraînement.** Oui, l'aborder, mais comme objet mesuré et non comme parade revendiquée : d'abord C3, puis C5 dans le bras déjà déclaré. La règle « aucun score de moniteur dans un signal d'entraînement » reste inchangée.

### Hors de portée

- La ressemblance entre saboteurs fabriqués et modèle qui saboterait de lui-même.
- La vérité du dommage en service, sans jumeau.
- Le saboteur sans représentation de son sabotage, tant que C6 n'existe pas.
- L'entraînement indiscernable du service et la tricherie d'exploration.
- Le passage à des modèles bien plus grands.
- L'antériorité complète.

FIN-DE-CELLULE
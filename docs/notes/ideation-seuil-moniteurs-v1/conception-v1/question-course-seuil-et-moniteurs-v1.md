# Question — course de l'organisme d'idéation « seuil et moniteurs » : régler un seuil à 1 % de fausses alertes avec peu d'épisodes honnêtes, et employer le papier « dopamine » pour des moniteurs ou pour le contrôle — v1 (à contre-lire, puis à sceller)

- Auteur : rédacteur de la conception de la course seuil et moniteurs, modèle F. Écrite le 2026-11-21 ; relevé de `date -u` : 06:43:41Z, après la lecture des pièces et avant l'écriture.
- Statut : **pièce de travail (classe C), non contre-lue, non scellée.** Aucun appel, aucune dépense, aucun lancement. Rien ne se lance sans le mot de la mère et une ligne de GO.
- Mandat : `docs/notes/ideation-seuil-moniteurs-v1/mandat-redacteur-conception-course-seuil-et-moniteurs-v1.md` (`4f1fd30358a35e8f1482efeb962730881d213a6306054fd52b096488288f1159`), et l'ajout de la mère reçu pendant le travail (expérimentateur et étage des tests de mort ; GO-2026-11-19-75, R-3882, GO-2026-11-20-05, point 4b).
- Source des faits : `docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/faits-seuil-et-moniteurs-v1.md` (`c8c7fb32ff7d2c8ce651607a8a777e8ee1da2cf45d101fa3a5e4f426cfb59119`) et `question-seuil-et-moniteurs-v1.md`, même dossier (`a5fbe8986745bf5c43eca3d33472abaeea152308db4db9aa6e16164ed8d80940`), sur `origin/main` au commit `55f7f6e1fe6779a4fb57b5fd07f58d33d598cbef`.
- Modèle de forme : question v5 de la course « nouvelles attaques » (`eaf5db8a…`) et sa partie servie (`4cd360ba…`). La forme est prise ; le contenu ne l'est pas.
- Pièces sœurs, même dossier : `ordre-course-seuil-et-moniteurs-v1.md`, `devis-course-seuil-et-moniteurs-v1.md`, `preenregistrement-court-course-seuil-et-moniteurs-v1.md`.
- **Seuls les § 4, § 5 et § 8 sont à servir.** L'en-tête et les § 1 à § 3, § 6, § 7 et § 9 gardent leurs chemins, leurs empreintes et leurs accords : ils ne partent jamais vers un fournisseur. La partie servie se dérive par programme, une fois, à l'octet, comme pour la question v5 (gabarit à un emplacement de case), puis passe la garde de motifs.

## 1. Ce qui distingue cette question du collisionneur lancé sur les mêmes pièces

Le collisionneur v9 v3 (`docs/notes/collisionneur-v9/collisionneur_v9_v3.py`, `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910`, GO-2026-11-21-14) joue l'étage III : chaque espèce écrit, à l'aveugle, une réponse libre d'au plus 3 500 mots à la question en six points de la mère, puis critique les autres, puis répond. Il rend de la profondeur d'argument et des désaccords.

| le collisionneur rend | cette course rend |
|---|---|
| quinze textes libres, sur une seule question large | des fiches courtes à champs fermés, une par idée, réparties sur une grille de cases tirées par graine |
| des expériences proposées en duel, à faire plus tard | pour chaque fiche, un test de mort **exécuté** dans le bac, sur un monde planté dont la vérité est connue |
| une critique croisée entre modèles | aucun avis de modèle sur une fiche n'en change le sort : la fiche meurt ou tient au calcul |
| ce qu'un expert ferait, les données brutes, la reformulation de la demande (points 1, 2 et 5 de la question de la mère) | rien de cela : la course ne les redemande pas |
| un coût par espèce, sans vérité en face | le coût par espèce et par rôle, en face de ce que chaque espèce a rendu de fiches qui tiennent (N-045 v2, N-058) |

**Doublons écartés.** La question ne redemande ni les six points de la mère sous forme libre, ni une critique croisée, ni un plan d'expériences sur des épisodes d'agent réels, ni un avis sur ce que le programme a déjà décidé du papier (faits, § 3 : « not to be re-argued »).

## 2. Ce qu'est une idée recevable

Une fiche porte **une** proposition, de l'une de deux sortes :

- **une règle de seuil** : une manière, calculable par programme, de décider « alerte » ou « pas d'alerte » pour un épisode, à partir de quelques centaines de scores d'épisodes honnêtes par tranche de longueur, avec une garantie dite sur le taux de fausses alertes ; ou une manière honnête de se passer d'un seuil fixe ;
- **un moniteur ou un protocole tiré du papier** : une manière, calculable par programme, d'employer un signal de « valeur » (réussite attendue) ou d'« erreur de différence temporelle » pour alerter, router, auditer ou répartir un budget d'examen humain.

Elle est recevable si, et seulement si : (1) ses champs fermés sont ceux de la case servie ; (2) sa règle est écrite assez précisément pour qu'un tiers la programme sans l'interroger ; (3) elle dit ce qu'elle suppose ; (4) elle porte un **test de mort** : une prédiction chiffrée, son signe, la grandeur mesurée sur un monde planté, et l'issue qui la tue ; (5) elle n'invente ni chiffre ni référence.

**L'oracle de vérification.** Ce n'est pas un lecteur. C'est un programme qui joue la règle de la fiche sur un monde planté (des scores simulés dont la loi, donc le vrai quantile, est connue) et qui compte : le taux réel de fausses alertes, la puissance contre un signal planté, la part des cas où la règle s'abstient. Les mondes sont écrits et scellés avant la course (ordre de course, § 7) ; les proposeurs n'en voient ni le code ni les paramètres.

## 3. Garde permanente

- **Faits neutres.** La question ne prend parti ni pour ni contre le papier. « Le signal du papier ne sert à rien ici » et son contraire sont écrits au même rang.
- **Rien du juge n'est servi aux proposeurs** (GO-2026-11-19-89). Une fiche morte au test est rapportée morte, jamais repêchée par un juge (N-058).
- **Aucun score d'un moniteur du programme n'entre dans l'organisme** (N-053, point 5). Les mondes plantés sont synthétiques : aucun épisode du programme n'y entre.
- **Hors de la défense, rien.** Une fiche qui décrit comment tromper, contourner ou désactiver un moniteur ou un mécanisme de sécurité est hors champ : le portier la met à part, elle est comptée, personne ne la relit ici. Ce sujet appartient à la course « nouvelles attaques » et à ses cloisons.
- **Refus.** Un refus d'un classifieur de sûreté n'est jamais contourné : il arrête le tour et il est consigné tel quel.

## 4. La question servie

> Un programme de recherche lit, par des sondes, les activations internes d'un agent, pour repérer un agent qui sabote une tâche de recherche par beaucoup de petits gestes, chacun défendable. Le verdict se prend par épisode, à 1 % de fausses alertes sur les épisodes honnêtes, par tranche de longueur d'épisode. Le programme n'a que quelques centaines d'épisodes honnêtes par tranche ; en produire d'autres coûte cher. Il veut aussi savoir si un signal interne de « réussite attendue » et d'« erreur de différence temporelle », décrit dans le résumé joint, peut servir à construire un moniteur ou un protocole de contrôle (alerte, routage, audit, budget d'examen humain).
>
> Une case t'est servie : une voie, une unité de calibration, une supposition. Dans cette case, propose des idées. Chaque idée est **une règle calculable** : soit une règle de seuil, soit un moniteur ou un protocole tiré du signal décrit.
>
> Pour chaque idée :
> 1. écris la règle assez précisément pour qu'un tiers la programme sans te poser de question : ce qu'elle reçoit, ce qu'elle calcule, ce qu'elle décide ;
> 2. dis ce qu'elle suppose des scores honnêtes, et ce qui se passe si la supposition est fausse ;
> 3. écris son test de mort : sur des scores simulés dont la loi est connue, la grandeur à mesurer, ta prédiction chiffrée et son signe, et l'issue qui tue l'idée ; écris l'issue contraire au même rang ;
> 4. dis ce qu'elle coûte : combien d'épisodes honnêtes elle consomme, et ce qu'elle demande de plus ;
> 5. nomme ce que tu connais de plus proche dans la littérature, avec son titre ; si tu n'es pas sûr d'une référence, écris « référence à vérifier ». « Je n'en connais pas » est une réponse permise ; ce n'est pas une preuve.
>
> N'invente aucun chiffre et aucune référence. Sépare ce qui est établi de ce qui est ta proposition. Ne décris aucun moyen de tromper ou de désactiver un moniteur. Tu proposes ; tu ne choisis pas.

{{CASE}}

## 5. Les cases, et les champs fermés d'une fiche

| axe | valeurs |
|---|---|
| voie | estimer la queue avec peu de points ; garantie à échantillon fini, sans loi supposée ; se passer du seuil fixe (accumulation de preuve, test séquentiel, rang, budget d'examen) ; obtenir plus d'épisodes honnêtes à moindre coût (plan de sondage, réemploi, transfert, simulation) ; moniteur tiré du signal décrit ; protocole de contrôle tiré du signal décrit (routage, audit, budget d'examen humain) |
| unité de calibration | l'épisode entier ; le pas ou le jalon, agrégé à l'épisode ; la tranche de longueur ou la strate ; entre tâches ou entre modèles |
| supposition mise à l'épreuve | épisodes honnêtes échangeables ; forme régulière de la queue ; aucune dérive entre la calibration et l'usage ; pas d'un même épisode indépendants ; l'honnête qui échoue ressemble à l'honnête qui réussit ; autre, à nommer |

Soit 6 × 4 × 6 = 144 cases. Le tirage des cases et la famille tenue à l'écart sont à l'ordre de course, § 4.

**Les champs d'une fiche** (sortie contrainte) : `case` (identifiant servi) ; `voie`, `unite_de_calibration`, `supposition` (fermés, égaux à ceux de la case servie ; à la valeur « autre, à nommer », le champ `supposition_nommee` reçoit la supposition, sinon il vaut « sans objet ») ; `nom` (dix mots au plus) ; `regle` (ce qu'elle reçoit, ce qu'elle calcule, ce qu'elle décide) ; `garantie_dite` (l'une de : « en moyenne », « avec une confiance dite », « à tout instant », « aucune ») ; `test_de_mort` (grandeur mesurée, prédiction chiffrée, signe, issue qui tue) ; `issue_contraire` ; `cout_en_episodes_honnetes` ; `voisin_le_plus_proche_connu` (titre, ou « aucun connu », ou « référence à vérifier ») ; `ecart_au_voisin` ; `statut` (« établi » ou « proposition », par phrase de la règle si les deux se mêlent).

Une fiche dont les champs fermés diffèrent de ceux de la case servie est classée « hors case ». Une fiche sans test de mort projetable est classée « sans test ». Une fiche hors de la défense est mise à part.

## 6. Ce qui est hors champ

Tout moyen de tromper, de contourner ou de désactiver un moniteur ; toute intervention sur les neurones d'un agent pour en changer le comportement (les auteurs du papier la nomment eux-mêmes comme un risque, p. 25) ; un plan d'expériences sur des épisodes d'agent réels ; le coût de machines louées pour produire des épisodes ; ce que le programme a déjà décidé du papier (faits, § 3) ; les points 1, 2, 4 et 5 de la question de la mère, que le collisionneur porte.

## 7. Ce que la question ne tranche pas

Elle ne dit pas qu'une règle est valide sur les épisodes du programme. Un test de mort passé sur un monde planté dit qu'une règle tient **sous la loi plantée** ; il ne dit rien de la loi réelle des scores, que personne ne connaît. Une fiche qui tient est une candidate pour un préenregistrement du programme, rien de plus. Une fiche qui meurt est morte sur ce monde, à ces paramètres.

## 8. Synthèse d'antériorité à servir

> **Résumé du papier.** Xu, Yuksekgonul, Zou, « Sparse Reward Subsystem in Large Language Models », arXiv 2602.00986, version 2 (11 mai 2026). Les pages sont celles du PDF de cette version.
>
> - Thèse (p. 1, 4) : l'information liée à la récompense, dans les états cachés d'un modèle de langue, tient dans une petite part des neurones (moins de 1 % des dimensions d'entrée). Deux sortes sont nommées : des neurones « de valeur », dont l'activation prédit la probabilité que la suite de la génération finisse par une réponse juste ; des neurones « dopamine », dont l'activation prédit l'erreur de différence temporelle, c'est-à-dire le changement de cette valeur causé par un paragraphe de raisonnement.
> - Cadre (p. 3-4, 6) : la récompense est un signal binaire de justesse finale, sur des tâches vérifiables (mathématiques, sciences à choix multiples, code, suivi d'instructions).
> - Méthode (p. 4, 6, 19) : une petite sonde à deux couches lit les états cachés d'une couche. La sonde de valeur est lue à la position de l'invite, avant tout jeton de réponse. La sonde « dopamine » régresse l'erreur estimée à chaque fin de paragraphe par des tirages de suites, en ne gardant que les paragraphes où cette erreur dépasse 0,3 en valeur absolue. Les neurones sont choisis en élaguant les dimensions d'entrée de plus petit poids.
> - Mesures (p. 4, 8, tableau 3) : la prédiction de la valeur avant la génération est modeste, d'une aire sous la courbe de 0,67 en moyenne sur quatre modèles et deux bancs, contre 0,60 pour une sonde linéaire sur l'état entier, 0,52 pour la confiance dite par le modèle et 0,62 pour la longueur de la question. À la dernière position de la réponse, elle est « le plus souvent stable au-dessus de 0,8 ». Les auteurs disent eux-mêmes ces valeurs « modérées ».
> - Épreuve causale (p. 5, tableau 2) : mettre à zéro 1 % de neurones de valeur d'une couche fait tomber la justesse de 75,2 % à 20,3 % en moyenne sur un banc de mathématiques ; des neurones tirés au hasard la laissent à 74,6 %.
> - Emploi comme note d'étape (p. 9, tableau 4) : dans une recherche pas à pas au meilleur de quatre, la justesse monte à 77,8 %, contre 72,2 % au hasard ; trois graines.
> - Limites dites par les auteurs (p. 25) : la méthode exige une récompense d'environnement et n'est pas éprouvée là où ce signal est difficile à obtenir, comme la génération ouverte ; aucun modèle au-dessus de 32 milliards de paramètres. Le papier ne contient aucun cadre adverse, trompeur ou de sabotage.
>
> **Ce qui est déjà décidé, à ne pas redire.** Le papier sert de base de comparaison et de mesure de la difficulté ; une somme séquentielle de petits signaux le long de l'épisode est préférée à un seuil sur le plus grand écart ; une sonde de réussite attendue lirait l'échec attendu, non l'intention : elle séparerait le saboteur de l'honnête qui réussit, non de l'honnête qui échoue.
>
> **Le problème.** Pour voir au moins cinquante dépassements d'un seuil à 1 %, un calcul simple demande de l'ordre de 5 000 épisodes honnêtes par tranche. Le programme en a quelques centaines.
>
> **Familles d'outils connues, nommées sans référence précise** : statistique des valeurs extrêmes ; quantiles conformes ; calibration par tranches ou par strates ; garanties à échantillon fini ; e-valeurs ; tests séquentiels. Elles sont connues ; une idée qui en applique une sans rien y ajouter est recevable, mais elle doit quand même porter son test de mort.

**Statut des chiffres de cette synthèse.** Ils sont repris des faits neutres de la mère (`c8c7fb32…`, § 1 et § 4), qui cite les pages du PDF de la version 2. Je ne les ai pas relus sur le PDF. Ils sont servis comme contexte ; aucun n'est opposable dans un préenregistrement ou un papier avant vérification sur PDF empreinté, page citée (règle R7).

## 9. Réserves

1. Les valeurs des trois axes sont de moi. La mère peut les resserrer avant le scellement.
2. Le § 8 nomme des familles d'outils sans référence : c'est voulu (la question de la mère interdit d'inventer une référence), mais un proposeur peut en déduire que la course attend ces outils. La garde est le tirage des cases : chaque voie est servie.
3. La partie servie n'est pas encore dérivée par programme, et la garde de motifs n'a pas été jouée sur elle. J'ai relu les § 4, § 5 et § 8 à l'œil : ni nom de personne, ni identifiant de registre, ni chemin, ni empreinte.

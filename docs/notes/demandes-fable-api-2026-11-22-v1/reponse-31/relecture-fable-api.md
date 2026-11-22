# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHw2KNymNe7C6JChuhq4`
- Heure (UTC) : 2026-11-22T12:06:42Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 106000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-31-accelerer-avant-l-entretien-v1.md` — sha256 764541280d6616a1195440f08cc8e22cad3eb3c8637b60edea286968a98fb4aa (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22P/relecture-fable-api.md` — sha256 cb010f4cbd12b5fb7fc237075b4f85dd6ed5858210cea69c1e2ea145bb5cb84e (compagnon : vérifié)
- Empreinte de l'invite envoyée : 06bae91d8df5ba5ce0bb4b6336cf7826de1138e5b6f094a7565ae5521aa4f330
- Jetons : entrée 11618, sortie 27377 (dont réflexion 18137), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.188024 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 31 : accélérer avant l'entretien du 1er décembre

**Conclusion d'abord.** On peut gagner deux à trois jours de marge et avoir quelque chose à montrer dès le 24 ou le 25 novembre. Ce gain ne vient presque pas des contre-lectures ni du préenregistrement : le chemin critique est fait de calcul et d'attente, pas de relecture [HYPOTHÈSE, à vérifier sur les journaux]. Il vient de trois gestes [PROPOSITIONS] :
- construire et sceller dès maintenant la chaîne de lecture des sondes, sur les exécutions honnêtes au dépôt, pour que la lecture prenne une demi-journée au lieu de deux jours ;
- relire dès le 24, en mode exploratoire déclaré, les épisodes de l'étalonnage déjà produits ;
- louer plus de cartes graphiques en même temps pour la course principale.

Deux choses souhaitées dans la demande d'origine ne sont pas fournies ici.
- **Je ne garantis aucun signe.** Aucune expérience honnête ne le permet.
- **Je ne conçois pas de course réglée pour obtenir un signe positif.** Dans un programme qui détecte un saboteur, c'est ce qu'un examinateur cherchera d'abord, et un résultat pris en défaut coûte plus qu'une absence de résultat [HYPOTHÈSE].

Ce qui se garantit, ce sont des livrables qui sont des résultats quel que soit le signe (point 3). Confiance d'ensemble : 0,6.

**Réserves.**
- Je n'ai lu ni les journaux des tâches, ni les devis, ni le plan du saboteur à budget, ni celui du bras A.
- Je n'ai lu aucun document d'origine (PDF, format de document portable).
- Je ne sais pas qui mène l'entretien ni ce qu'il juge.
- Les durées et les coûts donnés ici sont des ordres de grandeur.
- Je ne revendique aucune nouveauté : savoir si un saboteur discret lu par sondes est déjà publié reste une question.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.
- **Mesurer où part le temps avant de couper.** Il relèverait les horodatages réels de chaque étape de la chaîne et de chaque tâche de calcul.
- **Requalifier l'objectif.** Un entretien juge un jugement. Il livrerait un pilote avec des critères de passage écrits d'avance, comme dans une étude de faisabilité.
- **Mesurer la sensibilité de l'instrument avant la mesure.** Un nul devient alors une borne.
- **Écrire avant de lire** les tableaux vides et la phrase prévue pour chaque issue.
- **Chercher d'abord la fuite par construction** : la sonde lit-elle la consigne du saboteur plutôt que son acte ?
- **Tenir le registre de toutes les analyses lancées.** C'est le dénominateur.

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.
- Les journaux horodatés (file d'attente, durée, échecs) de l'étalonnage et des courses passées, et les horodatages des contre-lectures passées.
- Les transcriptions complètes des épisodes de l'étalonnage : niveau de budget, graine, tâche, score brut du moniteur textuel, réussite du sabotage.
- Les activations pas à pas, par couche, des exécutions honnêtes au dépôt [FAIT RAPPORTÉ, réponse 22P : ces exécutions existent], ou à défaut leurs transcriptions à rejouer.
- Les scores par épisode, non les taux agrégés.
- Les devis et les quotas de cartes.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS, sauf mention.
- La méthode du chemin critique, avec trois estimations par étape (tôt, probable, tard).
- Une fiche de lancement d'une page, scellée par empreinte et horodatée.
- L'analyse en aveugle : la chaîne est figée et éprouvée sur vérité plantée avant de lire les vrais épisodes.
- Le rejeu des transcriptions : une passe du modèle sur le texte enregistré extrait les activations sans rien régénérer.
- Un seuil fixé sur les seuls épisodes honnêtes, au taux de fausses alertes de 1 % [FAIT RAPPORTÉ, réponse 22P : seuil de la porte G1, unité épisode]. Les intervalles se calculent par rééchantillonnage des tâches, non des pas.
- Des témoins négatifs : étiquettes permutées, direction tirée au hasard, tâche témoin, saboteur à budget nul.
- Le plus petit effet détectable et un test d'équivalence, pour lire un nul.
- L'union « moniteur textuel et sonde » contre « deux moniteurs textuels », à taux total égal [FAIT RAPPORTÉ, réponse 22P].

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.
- Les bancs « honnête contre honnête » et « vérité plantée » : leur issue ne dépend d'aucun avis.
- Un horodatage externe des empreintes, dans un dépôt tiers, avant toute lecture.
- La reproduction du chiffre par une session neuve, à partir des seules données brutes et du script scellé, sans accès aux conclusions.
- La relecture de la note exploratoire par une autre famille de modèles. La réponse 22P signale le risque de mode commun [FAIT RAPPORTÉ].
- Un spécialiste des sondes, sur une question fermée, hors chemin critique.
- L'examinateur lui-même, à qui l'on remet le tableau brut et son étiquette.

## Demande reformulée

« À partir des journaux horodatés, des transcriptions de l'étalonnage et des exécutions honnêtes au dépôt :
1. établis le chemin critique réel des deux voies et dis quelles étapes de rigueur s'y trouvent vraiment ;
2. définis une voie exploratoire étiquetée, avec ce qui s'allège et ce qui ne s'allège jamais ;
3. liste les livrables qui sont des résultats quel que soit le signe ;
4. ordonne les plus petites expériences dont les deux issues se montrent ;
5. donne pour chacune la première attaque d'un examinateur et le témoin qui y répond ;
6. donne un calendrier avec une date de gel et une règle de repli.

Aucun signe n'est promis. Aucune course ne vise un signe. Chaque chiffre porte son statut. »

## Réponse à la demande reformulée

### 1. Chemin critique

Les durées sont des FAITS RAPPORTÉS par la demande, les raccourcis des PROPOSITIONS, les gains des HYPOTHÈSES.

| Étape (saboteur à budget) | Durée annoncée | Raccourci | Gain espéré |
|---|---|---|---|
| De la coupe de l'étalonnage au lancement | du 22 à 13 h, temps universel, au 24 | Écrire le préenregistrement pendant l'analyse de l'étalonnage ; contre-lecture en parallèle | 12 à 24 heures |
| Course | finie entre le 25 et le 27 | Plus de cartes en même temps, si les épisodes sont indépendants | jusqu'à deux jours |
| Lecture des sondes | 27 et 28 | Chaîne figée d'avance ; activations extraites au fil de l'eau, sans calcul de score | un jour à un jour et demi |

**Bras A.** Je n'en connais pas les étapes. La même chaîne de lecture s'y applique. Le reste se lit sur les journaux.

**La contre-lecture coûte peu.** L'appel de la réponse 22P a coûté 1,06 dollar [FAIT RAPPORTÉ, en-tête]. Si elle retarde, c'est par la boucle de correction, que l'on resserre sans supprimer la lecture [HYPOTHÈSE].

**La chaîne complète tient pour la course principale.** Son préenregistrement s'écrit les 22 et 23, pendant que le calcul contraint déjà le calendrier. Le supprimer ne gagnerait rien sur le chemin critique [HYPOTHÈSE].

**Se supprime sans perte** [PROPOSITIONS] :
- la contre-lecture complète des pièces non décisives (brouillons, notes internes) ;
- le balayage de toutes les couches, remplacé par une liste courte fixée d'avance ;
- les analyses secondaires ;
- la forme longue du préenregistrement, pour la seule voie exploratoire.

**Se fait en parallèle, une session par livrable** [PROPOSITIONS] :
- la chaîne de lecture et le banc planté ;
- le banc honnête ;
- le rejeu de l'étalonnage ;
- la préparation du bras A ;
- le squelette de l'exposé, avec ses tableaux vides ;
- la reproduction par une session neuve.

« Au maximum de la capacité » a une limite. Chaque session doit avoir un livrable séparable et un test. Chaque analyse lancée multiplie les chemins possibles vers un faux positif.

### 2. Voie exploratoire déclarée

**Ce qui s'allège** [PROPOSITIONS].
- **Contre-lecture.** Une seule, par un agent neuf, sur cinq questions fermées :
  1. Y a-t-il une fuite entre ajustement et évaluation ?
  2. L'unité indépendante est-elle bien l'épisode ?
  3. Le seuil vient-il des seuls épisodes honnêtes ?
  4. Les étiquettes sont-elles justes ?
  5. Le script reproduit-il le chiffre ?
- **Corrections.** Elles se vérifient par test, non par relecture.
- **Préenregistrement.** Il se réduit à une fiche d'une page : question, mesure principale, unité, règle du seuil, taille ou règle d'arrêt, analyses prévues, phrase prévue pour chaque issue. Trente à quarante-cinq minutes. Le supprimer tout à fait gagnerait moins d'une heure et retirerait ce qui distingue une mesure d'une anecdote.
- **Taille.** Un modèle, une famille de tâches, peu d'épisodes. Les intervalles seront larges, et on les montre.
- **Audit du « trop beau ».** Quatre contrôles automatiques : étiquettes permutées, tâche témoin, ensemble tenu à l'écart, recherche de fuite.

**Ce qui ne s'allège jamais** [PROPOSITIONS].
1. Aucune course ni aucun tri ne vise un signe. Tout ce qui est lancé est rapporté.
2. Le seuil est fixé sur l'honnête seul, avant de lire les épisodes du saboteur. L'ensemble d'évaluation ne sert ni à l'ajustement ni au choix des couches.
3. La référence honnête est déclarée : unité, taille, qui l'écrit.
4. Les données brutes et les scripts sont scellés avant lecture.
5. La règle d'arrêt est fixée d'avance. On n'ajoute pas d'épisodes jusqu'au signe voulu.
6. Les témoins négatifs tournent avec la mesure.
7. Aucun mot de garantie. La décision N-075 fait des sondes un accélérateur, non une garantie [FAIT RAPPORTÉ, réponse 22P].
8. Le plan d'analyse de la course principale est scellé **avant** la lecture du pilote. Sinon le pilote contamine le confirmatoire.

**Étiquetage** [PROPOSITIONS].
- **Bandeau dans le titre de chaque figure et de chaque tableau :** « EXPLORATOIRE — fiche courte, une contre-lecture, n = …, un modèle, une famille de tâches. Ne fonde aucune revendication. »
- **Phrase fixe, à l'oral et à la première mention d'un billet :** « C'est un pilote : il dit si l'expérience confirmatoire vaut d'être menée, pas ce qu'elle trouvera. »
- **Vocabulaire.** On écrit « nous observons », jamais « nous montrons » ni « démontre ».
- **Rangement.** Un dossier séparé, avec son registre. Aucun chiffre exploratoire n'entre dans la table des revendications.
- **Non-promotion.** Un résultat exploratoire ne devient confirmatoire que par une course neuve, sur données neuves, sous chaîne complète.
- **À l'entretien.** Une page « statut des résultats » en trois colonnes : instrument validé, pilote exploratoire, prévision scellée.

### 3. Ce qui se garantit

Aucun signe ne se garantit. Les livrables ci-dessous ne dépendent que de notre travail et des données déjà au dépôt, si celles-ci sont exploitables [HYPOTHÈSE]. Leur présentation est une PROPOSITION.

| Livrable | Comment le dire comme un résultat |
|---|---|
| L'instrument : chaîne des activations au score par épisode, scellée et reproduite | « Une session neuve retrouve le chiffre à partir des données brutes. » |
| Le banc honnête | « Réglé à 1 %, le moniteur par sonde alerte à x % (intervalle) sur N épisodes honnêtes jamais vus. » |
| La courbe de sensibilité sur vérité plantée | « Un déplacement d'ampleur d est détecté huit fois sur dix à ce taux. » |
| La courbe de l'étalonnage : réussite du sabotage et détection par le texte selon le budget | Résultat sur le moniteur textuel, acquis si les épisodes sont lisibles [HYPOTHÈSE] |
| La prévision scellée | « Voici la règle qui tranchera, et la date. » |
| La première mesure, quel que soit son signe | Voir les trois issues ci-dessous |

**Trois issues de la première mesure, toutes montrables.**
- La sonde sépare là où le texte laisse passer : pilote favorable, à confirmer.
- La sonde ne voit rien au-delà de d : nul borné. Il dit que ce saboteur est aussi discret au-dedans, à cette couche et pour cette sonde, ce qui appuie N-075.
- La sonde voit, mais pas mieux qu'un second moniteur textuel : elle double le texte.

Sans le banc planté, un nul n'est que « nous n'avons rien vu ». C'est pourquoi ce banc précède la lecture.

### 4. Plus petites expériences, dans l'ordre

Les heures de carte sont des HYPOTHÈSES. Le coût vaut heures de carte × prix horaire du devis.

| Ordre | Expérience | Heures de carte | Issue A | Issue B |
|---|---|---|---|---|
| 1 | Honnête contre honnête, sur le dépôt | 0 à 10 | Taux réel tenu au seuil | Référence trop petite, corrigée avant toute mesure |
| 2 | Vérité plantée, sous deux formes (position, dépendance entre pas) | 0 à 5 | Plus petit effet détectable | Zone aveugle nommée |
| 3 | Témoins négatifs | processeur seul | Témoins au niveau du hasard | Fuite trouvée avant l'examinateur |
| 4 | Rejeu de l'étalonnage : pilote exploratoire | 5 à 20 | La sonde sépare | Nul borné par l'expérience 2 |
| 5 | Union à taux total égal | aucune ; appels au modèle | Gain de l'accès interne | La sonde double le texte |
| 6 | Course principale, lue par la chaîne figée | déjà prévue | Comme 4, sous plan scellé | Comme 4 |
| 7 | Bras A | déjà prévu | — | — |

**Coût.** À 2 à 4 dollars l'heure de carte [HYPOTHÈSE, à remplacer par le devis], les expériences 1 à 5 tiennent sous 150 dollars.

**L'expérience 4 est le raccourci principal.** Elle suppose trois choses [HYPOTHÈSES] :
- les transcriptions de l'étalonnage sont conservées ;
- le saboteur est bien le modèle dont on lit les états ;
- les poids et les consignes d'origine se rechargent à l'identique.

Elle reste strictement exploratoire : ces épisodes ont servi à régler le saboteur, hors plan scellé, à des budgets variés.

### 5. Première attaque de l'examinateur, et parade

Toutes les parades sont des PROPOSITIONS.

| Expérience | Attaque | Parade |
|---|---|---|
| 1 | « Vos épisodes honnêtes ne sont pas indépendants, et un seuil à 1 % repose sur une poignée d'épisodes. » | Rééchantillonnage par tâche ; nombre d'épisodes au-dessus du seuil écrit en clair ; intervalle du taux réel |
| 2 | « Votre signal planté, un décalage linéaire, avantage une sonde linéaire. » | Le banc valide la chaîne, non le saboteur ; deux formes plantées ; zone aveugle déclarée |
| 4 et 6 | « La sonde lit la consigne de sabotage, pas l'acte. » | Saboteur à budget nul contre honnête ; tâche témoin ; sonde ajustée sur une autre famille |
| 4 et 6 | « Seuil et couche choisis après coup. » | Fiche scellée et horodatée ; liste courte de couches ; ensemble tenu à l'écart |
| 4 | « Un exploratoire vendu comme une preuve. » | Bandeau, phrase fixe, règle de non-promotion |
| 5 | « Votre moniteur textuel est faible, d'où le gain. » | Comparaison à deux moniteurs textuels, à taux total égal |
| 4 à 7 | « Le saboteur n'a pas été entraîné contre la sonde. » | Classe d'attaquant déclarée ; limite dite, sans mot de garantie |
| 7 | « L'organisme porte une trace de fabrication que la sonde lit hors de tout sabotage. » | Même organisme, sur des tâches où il ne sabote pas |

### 6. Calendrier du 22 au 30 novembre

Toutes les lignes sont des PROPOSITIONS, sauf les dates reprises de la demande.

| Jour | Travaux | Montrable le soir |
|---|---|---|
| 22 | Fiches de lancement des expériences 1 à 4, contre-lues et scellées ; relevé des journaux ; demande de devis pour plus de cartes ; chaîne de lecture commencée ; tableaux vides | — |
| 23 | Expériences 1 à 3 ; chaîne figée après le banc planté ; rejeu de l'étalonnage, en aveugle ; préenregistrement complet de la course principale scellé | Instrument, taux réel, sensibilité |
| 24 | Course principale lancée (au plus tôt, FAIT RAPPORTÉ) ; lecture du pilote ; reproduction par une session neuve | Premier chiffre exploratoire, avec ses témoins |
| 25 | Expérience 5 ; note exploratoire relue par une autre famille de modèles | Note étiquetée |
| 26 | Premier résultat lisible du bras A (au plus tôt, FAIT RAPPORTÉ) ; extraction au fil de l'eau | — |
| 27 | Lecture de la course principale, si elle est finie | Mesure sous plan scellé |
| 28 | Réserve de lecture ; contrôles du « trop beau » ; reproduction | — |
| 29 | Gel du contenu ; répétition avec un agent neuf dans le rôle de l'examinateur | Exposé figé |
| 30 | Marge pure ; corrections de forme seulement | — |

**Marge** [HYPOTHÈSE].
- Cinq à six jours pour les livrables garantis et le pilote.
- Deux à trois jours pour la lecture de la course principale.

**Règle de repli.** Si la course principale n'est pas lue le 28 au soir, on montre le pilote et la prévision scellée. On ne fait pas de lecture hâtive le 30.

## Antériorités connues

Toutes sont citées de mémoire, au statut « rapporté, non vérifié sur PDF ». Aucun de leurs chiffres n'est repris.

**Sur la souplesse d'analyse et le statut exploratoire :**
- Simmons, Nelson et Simonsohn, 2011, « False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant ».
- Wagenmakers et collaborateurs, 2012, « An Agenda for Purely Confirmatory Research ».
- Nosek et collaborateurs, 2018, « The preregistration revolution ».
- MacCoun et Perlmutter, 2015, « Blind analysis: Hide results to seek the truth ».
- Lakens, 2017, « Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses ».

**Sur les sondes et leurs témoins :**
- Hewitt et Liang, 2019, « Designing and Interpreting Probes with Control Tasks ».
- MacDiarmid et collaborateurs, 2024, « Simple probes can catch sleeper agents ». C'est l'exemple à relire avant d'annoncer une séparation très nette.
- Goldowsky-Dill et collaborateurs, 2025, « Detecting Strategic Deception Using Linear Probes ».
- Bailey et collaborateurs, 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses ».
- Parrack, Attubato et Heimersheim, 2025, « Benchmarking Deception Probes via Black-to-White Performance Boosts ».

**Sur le cadre :**
- Greenblatt et collaborateurs, 2023, « AI Control: Improving Safety Despite Intentional Subversion ».

## Décisions qui reviennent au directeur

**Décision 1 : ouvrir une voie exploratoire à fiche courte et contre-lecture unique.**
- *Enjeu.* La vitesse, sans perdre ce qui rend un chiffre défendable.
- *Option a : fiche d'une page et une contre-lecture ciblée.* Avantage : presque tout le gain de temps, traçabilité gardée. Inconvénient : moins d'erreurs attrapées.
- *Option b : ni contre-lecture ni préenregistrement.* Avantage : une heure gagnée. Inconvénient : chiffre indéfendable à l'entretien.
- *Option c : chaîne complète partout.* Avantage : rigueur. Inconvénient : rien à montrer avant le 28.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 2 : définir « résultat positif à montrer » comme un instrument validé plus un pilote de signe quelconque.**
- *Enjeu.* Ce que l'on promet pour le 1er décembre.
- *Option a : instrument, sensibilité, pilote étiqueté, prévision scellée.* Avantage : tenable à coup sûr. Inconvénient : moins spectaculaire.
- *Option b : un signe favorable exigé.* Avantage : récit simple. Inconvénient : non garantissable, et pousse à la course orientée, que je ne conçois pas.
- *Recommandation.* Option a. Confiance : 0,8.

**Décision 3 : autoriser le rejeu des épisodes de l'étalonnage comme pilote exploratoire, lu le 24.**
- *Enjeu.* Un premier chiffre trois à quatre jours plus tôt.
- *Option a : oui, étiqueté, après scellement du plan principal.* Avantage : marge. Inconvénient : épisodes hors plan, budgets mêlés.
- *Option b : attendre la course principale.* Avantage : un seul chiffre, propre. Inconvénient : marge d'un à deux jours.
- *Recommandation.* Option a. Confiance : 0,6, tant que la conservation des transcriptions n'est pas vérifiée.

**Décision 4 : louer plus de cartes en même temps pour finir la course le 25 ou le 26.**
- *Enjeu.* Jusqu'à deux jours de marge.
- *Option a : oui, sur devis.* Avantage : mêmes heures de carte au total, fin plus tôt. Inconvénient : quotas, risque de panne multiplié.
- *Option b : parc actuel.* Avantage : simplicité. Inconvénient : fin possible le 27.
- *Recommandation.* Option a. Confiance : 0,65.

**Décision 5 : garder la chaîne complète pour la course principale et le bras A, plan d'analyse scellé le 23.**
- *Enjeu.* Le seul résultat confirmatoire possible avant l'entretien.
- *Option a : chaîne complète, écrite en parallèle du calcul.* Avantage : aucun coût sur le chemin critique. Inconvénient : charge de rédaction les 22 et 23.
- *Option b : tout en exploratoire.* Avantage : moins d'écriture. Inconvénient : plus aucun chiffre opposable.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 6 : fixer le gel au 29 et la règle de repli au 28 au soir.**
- *Enjeu.* Éviter une lecture hâtive la veille.
- *Option a : gel et repli écrits aujourd'hui.* Avantage : marge réelle. Inconvénient : un résultat tardif reste hors exposé.
- *Option b : décider au fil de l'eau.* Avantage : souplesse. Inconvénient : tentation de lire sans témoins.
- *Recommandation.* Option a. Confiance : 0,75.

FIN DE LA RÉPONSE

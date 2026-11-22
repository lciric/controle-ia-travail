# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHyqJPzd7agmzBvEup1m`
- Heure (UTC) : 2026-11-22T12:45:04Z
- Réglages : effort `xhigh`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 64000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-36-reponses-coupees-passe-x-v1.md` — sha256 1efb5f6ec4dff4fac25dcaa6e6eba2debe788568de497c380224eb3412bfd6d5 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-30/relecture-fable-api.md` — sha256 3f8c7a8498e59babe9ebb1b3579fac556195a81e821f939f3df4d2827cc96951 (compagnon : vérifié)
- Empreinte de l'invite envoyée : b9702fa5a5193c3b07d3f1d8309cf9736d2d6cec5e4aa62264c125f0ab399fc2
- Jetons : entrée 10362, sortie 37280 (dont réflexion 28906), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.574096 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 36 — éviter les réponses coupées dans la passe X : réponse approfondie

**Conclusion d'abord.** L'entrée n'est pas le problème : 21 000 signes pèsent peu. Le risque vient de la sortie, où la réflexion et le texte se partagent un seul plafond. Découper la demande protège le texte, et seuls les réglages (budget, effort) contiennent la réflexion : il faut les deux.

Je recommande, dans l'ordre :
- trois requêtes de six questions, identiques pour les neuf modèles, avec une cible de mots par question ;
- une requête de contrôle par modèle, puis une passe à blanc sur le premier groupe, avant de payer le reste ;
- une garde à cinq contrôles, qui met en quarantaine, relance une seule fois en entier avec un réglage déclaré d'avance, et ne recolle jamais.

Deux alertes sortent des chiffres mêmes de la demande :
- chez Google, 65 536 moins 49 152 laissent 16 384 jetons au texte, soit environ 350 mots par question en pièce unique, sans marge ;
- la règle « entrée plus 90 000 » donnerait ici un budget voisin de 98 000 jetons, au-dessus du plafond de 96 000, alors que le reste du budget se tenait bien sous le plafond dans les appels rapportés.

Confiance d'ensemble : 0,55.

**Réserves.**
- Je n'ai pas lu la pièce de la passe X : j'ignore si les dix-huit questions sont indépendantes et quelle longueur chacune attend.
- Je ne connais pas les modèles Opus 5.5, Fable 5.1, Argon, Carbon, Neon et Astra, ni les tarifs des modèles en lice : je ne chiffre donc aucun coût.
- Ce que je dis des fournisseurs vient de leur documentation telle que je m'en souviens, pour des générations antérieures, non de la version en vigueur.
- Le constat « quatre fois sur cinq » porte sur d'autres demandes et sur un petit échantillon. Le succès avec budget est, à ma lecture, un essai unique, qui n'établit pas un taux.
- Mon ratio de jetons par mot vient de deux réponses d'un seul modèle d'Anthropic.
- Je ne vois ni mes compteurs ni mes réglages.
- Je ne nomme que les auteurs des travaux cités.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.
- **Dimensionner avant de régler.** Il fixerait une longueur attendue par question, la convertirait en jetons et la comparerait à la place laissée au texte chez chaque modèle. La demande ne fixe aucune longueur : seul le plafond borne la sortie.
- **Séparer cinq défauts** que la question confond :
  - le texte coupé au plafond ;
  - la réflexion qui épuise la sortie ;
  - la coupure de transport (appel long sans flux, délai dépassé) ;
  - la requête refusée à l'envoi (plafond ou réglage non admis par le modèle) ;
  - le raccourcissement silencieux, où le modèle termine proprement mais bâcle ou saute les dernières questions.
- **Contester la pièce unique.** L'unité de lecture est le couple (modèle, question) ; rien n'oblige l'unité d'envoi à être la pièce entière.
- **Faire une passe à blanc** avant la passe entière.
- **Éprouver la garde** sur des coupures plantées, avant de lui confier la passe.
- **Publier le taux de défaut par modèle** comme un résultat, non comme un incident.

## 2. Données brutes de départ

Toutes les puces sont des PROPOSITIONS.
- La pièce de la passe X, question par question, avec le compte de signes et de jetons de chacune.
- Les journaux des cinq appels du constat et de l'appel réussi : entrée, sortie, réflexion, raison d'arrêt, plafond de sortie, budget, durée. Le résumé « quatre sur cinq » ne suffit pas.
- Pour chacun des neuf modèles, les journaux des passes précédentes : longueurs de texte et de réflexion, raisons d'arrêt.
- Les objets de réponse complets et les flux d'événements horodatés.
- Les pages de documentation datées des quatre fournisseurs : plafond de sortie de chaque modèle, réglages admis, place de la réflexion dans le plafond.
- Le compte exact des jetons d'entrée, par le service de comptage de chaque fournisseur, là où il existe.

## 3. Méthodes et outils

Toutes les puces sont des PROPOSITIONS.
- **Table de dimensionnement** : cible de mots, jetons de texte, place disponible (section A).
- **Requête de contrôle** : mêmes réglages, invite d'une ligne. Elle dit pour presque rien si le plafond et les réglages sont admis.
- **Réception en flux** pour tout appel long ; mode d'arrière-plan là où il existe.
- **Passe à blanc** : le premier groupe, pour les neuf modèles.
- **Script de complétude et de couverture** : raison d'arrêt, ligne finale, titres numérotés, mots par question.
- **Banc à coupures plantées** : des réponses tronquées à la main (fin absente, question sautée, texte vide, dernière réponse en deux lignes) que la garde doit toutes rejeter.
- **Prévisions scellées, règles d'arrêt, plafond de dépense.**

## 4. Ce qui vérifie hors du directeur et de Claude

Toutes les puces sont des PROPOSITIONS.
- Les compteurs d'usage et les raisons d'arrêt des quatre interfaces de programmation.
- L'acceptation ou le refus de la requête de contrôle : c'est le fournisseur, non un avis, qui dit si un plafond est admis.
- Le script de couverture, déterministe, une fois éprouvé sur le banc.
- La réponse écrite des fournisseurs à trois questions :
  - « Le budget de réflexion est-il un plafond ou une cible, et la réflexion est-elle comptée dans le plafond de sortie ? »
  - « Le budget de tâche est-il admis sur ce modèle pour un appel unique sans outil, et son compte à rebours inclut-il l'entrée ? »
  - « Une requête qui dépasse le plafond de sortie est-elle refusée ou réduite en silence ? »
- Un lecteur d'une autre famille de modèles, à l'aveugle, sur un échantillon de réponses acceptées par la garde.
- La réplication : un réglage validé sur le groupe 1 doit tenir sur le groupe 2 avant le groupe 3.

## Demande reformulée

« Voici la pièce de la passe X découpée par question, les journaux des appels du constat, ceux des passes précédentes pour les neuf modèles et la documentation en vigueur. (0) Dimensionne : longueur attendue par question, jetons de texte, place laissée au texte chez chaque modèle. (1) Donne le risque par modèle en séparant texte coupé, réflexion épuisante, transport, refus à l'envoi et raccourcissement silencieux ; distingue le mesuré du supposé. (2) Classe les six formes par sûreté, avec leur coût et leur effet sur la lecture. (3) Recommande forme et réglages, avec la passe à blanc qui les valide et ce qui les ferait changer. (4) Spécifie la garde, son épreuve et sa règle de relance. Les points 1 à 4 visent 900 mots ; marque fait rapporté, hypothèse, proposition. »

## Réponse à la demande reformulée

### A. Dimensionnement

**Ce que les pièces montrent** [FAIT RAPPORTÉ ; soustractions de ma main].
- La réponse 30 compte 30 532 moins 22 572, soit 7 960 jetons de texte. La réponse 22A en compte 8 308. Les deux étaient plafonnées à 3 500 mots.
- Chez Google, il reste 16 384 jetons pour le texte si la réflexion consomme son budget.
- Les appels épuisés ont atteint 128 000 jetons de réflexion : leur plafond de sortie était donc de 128 000. Le plafond de l'appel réussi n'est pas dans mes pièces.

**Ce que j'en tire** [HYPOTHÈSE]. Un mot de français avec balisage coûte 2,3 à 2,7 jetons sur ce modèle. Les autres fournisseurs comptent autrement.

| Cible par question | Mots, dix-huit questions | Jetons de texte, pièce unique | Jetons de texte, groupe de six |
|---|---|---|---|
| 350 mots | 6 300 | 14 500 à 17 000 | 4 800 à 5 700 |
| 600 mots | 10 800 | 24 800 à 29 200 | 8 300 à 9 700 |
| 900 mots | 16 200 | 37 300 à 43 700 | 12 400 à 14 600 |

**Lecture** [HYPOTHÈSE].
- En pièce unique, Google ne tient que la cible de 350 mots, sans marge.
- Sous 96 000, la cible de 600 mots exige une réflexion sous 67 000 jetons ; celle de 900 mots, sous 52 000.
- Un groupe de six à 600 mots est le régime des réponses déjà obtenues (environ 8 000 jetons de texte).
- La pièce pèserait 7 000 à 9 000 jetons d'entrée, d'où un budget « entrée plus 90 000 » voisin de 98 000. Selon que le compte à rebours inclut l'entrée ou non (les deux hypothèses de la réponse 30), le reste perçu est de 90 000 ou de 98 000 jetons : à 6 000 sous le plafond, ou au-dessus. Dans les appels rapportés, il se tenait 38 000 jetons sous un plafond de 128 000.

**De mémoire** [FAIT RAPPORTÉ, documentation de générations antérieures ; rapporté, non vérifié sur PDF, c'est-à-dire sur le document d'origine].
- Sonnet 4.6 plafonnait sa sortie à 64 000 jetons et n'admettait pas l'effort maximal : une sortie de 96 000 y serait refusée à l'envoi.
- Le budget de tâche est une bêta apparue après Opus 4.6 et Sonnet 4.6.
- Chez Google, le budget de réflexion est une indication que le modèle peut dépasser.
- Chez OpenAI, le raisonnement est compté dans le plafond de sortie ; une réponse épuisée revient au statut « incomplet », parfois sans texte.
- Chez Anthropic, la bibliothèque cliente refuse un appel sans flux dont la durée attendue dépasse dix minutes.

### B. Les quatre points de la demande

**1. Risque de coupure, modèle par modèle** [HYPOTHÈSES en jugement, non mesurées ; pièce unique, réglages prévus, sans cible de longueur].

| Modèle | Défaut le plus probable | Risque estimé |
|---|---|---|
| Opus 5.5, Fable 5.1 | réflexion qui épuise la sortie à l'effort maximal | 0,5 à 0,8 sans budget ; 0,15 à 0,35 avec |
| Opus 4.6 | le même ; budget de tâche peut-être non admis | 0,2 à 0,5 |
| Sonnet 4.6 | refus à l'envoi si son plafond est resté à 64 000 ; sinon texte coupé | 0,1 à 0,25 une fois le plafond corrigé |
| Argon, Carbon, Neon | texte coupé dans 16 384 jetons | 0,3 à 0,6 |
| Astra | raisonnement compté dans les 96 000 ; coupure de transport | 0,1 à 0,3 |
| Kimi | plafond admis et décompte du raisonnement inconnus de moi | 0,2 à 0,5, par ignorance |

Pour tous, le raccourcissement silencieux des dernières questions me paraît le défaut le plus fréquent en pièce unique (0,5 ou plus).

Ce qui fait monter le risque :
- l'effort maximal sans budget ;
- un budget dont le reste touche le plafond ;
- l'absence de cible de longueur ;
- le nombre de questions par appel ;
- une consigne chargée de contraintes de forme, qui pousse à rédiger le brouillon dans la réflexion ;
- un appel long sans flux.

**2. Formes, de la plus sûre à la moins sûre** [classement : HYPOTHÈSE]. J'entends par quarantaine la mise à l'écart d'une sortie qui n'a pas passé la garde.

1. **Une requête par question** (162 appels).
   - Coût : préambule répété (faible) et surtout réflexion payée jusqu'à dix-huit fois.
   - Lecture : un défaut perd une réponse sur dix-huit et l'effet de position disparaît. La vue d'ensemble disparaît aussi. Chaque question reçoit plus de profondeur qu'en pièce unique, ce qui rompt la comparaison avec les passes fusionnées.
2. **Des groupes** (trois fois six, 27 appels).
   - Coût : réflexion payée jusqu'à trois fois.
   - Lecture : un défaut perd six réponses. Le découpage doit être le même pour tous et fixé avant l'envoi.
3. **Plusieurs tours.**
   - Coût : fil relu à chaque tour, outil à adapter à quatre fournisseurs.
   - Lecture : chaque tour a son plafond, mais les réponses tardives dépendent des premières. Un défaut au deuxième tour met tout le fil en quarantaine.
4. **Budget de tâche.**
   - Coût : nul.
   - Lecture : réservé aux modèles d'Anthropic qui l'admettent, avec un seul succès rapporté. C'est une cible, non une borne, et il peut comprimer la réflexion.
5. **Consigne de longueur par question.**
   - Coût : nul.
   - Lecture : elle égalise les réponses et rend la couverture vérifiable. Elle ne contient pas la réflexion et peut l'allonger, par comptage des mots.
6. **Reprise automatique après coupure.**
   - Coût : un second appel qui relit tout.
   - Lecture : elle ne sauve pas une réflexion épuisante, laisse une couture et masque le défaut. Une réponse recollée n'est pas comparable.

Les formes 4 et 5 complètent les formes 1 à 3 ; elles ne les remplacent pas.

**3. Recommandation** [PROPOSITION].
- **Forme.** Trois groupes de six questions, composés par thème (les questions liées ensemble), avec le même préambule. Chaque réponse a 600 mots au plus et un titre numéroté ; la ligne finale clôt le tout.
- **Avant l'envoi.** Une requête de contrôle par modèle, puis le groupe 1 pour les neuf modèles. Les groupes 2 et 3 partent après lecture de la garde. Les réponses du groupe 1 restent valables si aucun réglage ne change.
- **Partout.** Réception en flux.

| Fournisseur | Réglages |
|---|---|
| Anthropic, modèles admettant le budget de tâche | effort maximal ; budget = entrée comptée + 90 000, avec le plafond de sortie de l'appel réussi (à lire au journal) ; à défaut, plafond de 96 000 et budget = entrée + 60 000, non éprouvé |
| Anthropic, autres modèles | plafond admis par le modèle ; effort le plus haut admis ; si la passe à blanc épuise la sortie, budget de réflexion fixe laissant 20 000 jetons au texte |
| Google | 65 536 dont 49 152 conservés, un groupe demandant environ 9 000 jetons de texte ; si le texte mesuré dépasse 12 000, réflexion à 40 960 |
| OpenAI | 96 000 ; effort le plus haut admis ; mode d'arrière-plan s'il existe |
| Moonshot | plafond ramené à la valeur admise ; vérifier si le raisonnement y est compté |

Si la pièce unique est maintenue : 350 mots par question et réflexion de Google abaissée à 32 768.

**4. Garde** [PROPOSITION].

Cinq contrôles, par script :
1. raison d'arrêt normale chez chaque fournisseur, et flux clos par son événement final ;
2. texte non vide, ligne finale présente une seule fois, en dernière ligne ;
3. couverture : tous les titres numérotés, dans l'ordre, chacun avec au moins 40 % de la cible de mots ;
4. modèle servi égal au modèle demandé ;
5. alerte, sans rejet, si la sortie dépasse 90 % du plafond ou si le dernier tiers des réponses est deux fois plus court que le premier.

En cas d'échec, la sortie entière est classée « défaut ». Elle est gardée avec son empreinte pour le diagnostic, jamais lue comme réponse, jamais recollée. La cause est notée, puis une seule relance entière est permise :
- coupure de transport : la même requête ;
- réflexion épuisante : le réglage de repli déclaré d'avance (budget, ou un cran d'effort en moins) ;
- texte coupé ou couverture incomplète : le groupe scindé en deux moitiés.

Toute réponse relancée porte une marque et s'analyse avec et sans elle. Au second défaut, l'unité est inscrite « sans réponse ».

### Antériorités que je connais

Toutes sont FAIT RAPPORTÉ, de mémoire, au statut « rapporté, non vérifié sur PDF ». Aucune ne porte sur ces modèles et aucun de leurs chiffres n'est opposable.
- Cheng et collaborateurs 2023, « Batch Prompting: Efficient Inference with Large Language Model APIs » : plusieurs questions par requête, avec une qualité qui baisse quand le lot grossit.
- Lin et collaborateurs 2023, « BatchPrompt: Accomplish More with Less » : effet de la position d'une question dans le lot.
- Son et collaborateurs 2024, « Multi-Task Inference: Can Large Language Models Follow Multiple Instructions at Once? » : résultat inverse sur certains modèles, à ne pas ignorer.
- Liu et collaborateurs 2024, « LongGenBench: Long-context Generation Benchmark » : dégradation quand une seule longue réponse doit couvrir plusieurs questions.
- Bai et collaborateurs 2024, « LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs » : tendance des modèles à borner d'eux-mêmes la longueur de sortie.
- Han et collaborateurs 2024, « Token-Budget-Aware LLM Reasoning », déjà cité dans la réponse 30.
- Documentation des fournisseurs : plafonds de sortie, réflexion, effort, budget de tâche, flux.

Je ne connais pas de mesure publiée du taux de coupure d'une demande à dix-huit questions quand la réflexion partage le plafond de sortie. C'est une question, non un vide constaté : je n'ai fait aucune recherche.

## Décisions qui reviennent au directeur

**Décision 1 — Choisir l'unité d'envoi : pièce unique, trois groupes de six, ou une requête par question.**
- *Enjeu.* En pièce unique, un défaut perd dix-huit réponses, et Google n'a place que pour 350 mots par question.
- *Option a : pièce unique, 350 mots par question, réflexion de Google abaissée.* Avantage : un appel par modèle, vue d'ensemble conservée. Inconvénient : réponses minces, risque le plus haut.
- *Option b : trois groupes de six.* Avantage : régime déjà observé, un défaut perd six réponses. Inconvénient : 27 appels, un découpage à justifier.
- *Option c : une requête par question.* Avantage : forme la plus sûre, unité de lecture propre. Inconvénient : 162 appels, réflexion payée jusqu'à dix-huit fois.
- *Recommandation.* Option b. Confiance : 0,6.

**Décision 2 — Fixer la longueur attendue par question.**
- *Enjeu.* Sans cible, rien ne borne le texte et la couverture ne se vérifie pas.
- *Option a : 350 mots.* Avantage : tient partout. Inconvénient : court pour des questions exigeantes.
- *Option b : 600 mots.* Avantage : tient par groupes chez tous les fournisseurs. Inconvénient : exclut la pièce unique chez Google.
- *Option c : longueur libre sous un total.* Avantage : le modèle arbitre. Inconvénient : les dernières questions paient.
- *Recommandation.* Option b. Confiance : 0,6.

**Décision 3 — Régler l'effort chez Anthropic : maximal avec budget de tâche, ou un cran en dessous pour les quatre modèles.**
- *Enjeu.* Le seul succès rapporté à l'effort maximal tient à un budget, une fois, et deux des quatre modèles ne l'admettent peut-être pas.
- *Option a : effort maximal avec budget là où il est admis, effort le plus haut admis ailleurs.* Avantage : chaque modèle à son meilleur. Inconvénient : réglages inégaux, règle non éprouvée sous 96 000.
- *Option b : un cran sous le maximum pour tous.* Avantage : régime qui a rendu la réponse 30 complète. Inconvénient : ce n'est pas l'effort maximal.
- *Option c : effort maximal sans budget.* Avantage : simplicité. Inconvénient : quatre appels sur cinq perdus dans le constat.
- *Recommandation.* Option a si la passe à blanc passe, repli sur b. Confiance : 0,55.

**Décision 4 — Autoriser la requête de contrôle et la passe à blanc avant la passe entière.**
- *Enjeu.* Mes risques par modèle sont des jugements ; neuf appels les remplacent par des mesures.
- *Option a : passe entière d'emblée.* Avantage : immédiat. Inconvénient : un réglage faux se paie sur tous les appels.
- *Option b : requêtes de contrôle seules.* Avantage : presque gratuit, écarte les refus. Inconvénient : rien sur la réflexion.
- *Option c : contrôle, puis groupe 1 pour les neuf modèles.* Avantage : mesure réelle, réponses réutilisables. Inconvénient : un délai.
- *Recommandation.* Option c. Confiance : 0,8.

**Décision 5 — Fixer la règle de relance après un défaut.**
- *Enjeu.* Une relance mal réglée fabrique des réponses qui ne se comparent plus.
- *Option a : aucune relance.* Avantage : comparaison pure. Inconvénient : des trous dans le tableau.
- *Option b : une relance entière, à réglage déclaré d'avance, marquée.* Avantage : trous comblés, traçabilité gardée. Inconvénient : réponses relancées à lire à part.
- *Option c : reprise automatique et recollage.* Avantage : le moins cher. Inconvénient : couture, défaut masqué, inutile contre une réflexion épuisante.
- *Recommandation.* Option b. Confiance : 0,7.

FIN DE LA RÉPONSE

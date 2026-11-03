## Statuts et présupposés

**Convention** : les résultats de la pièce Scheurer sont **RAPPORTÉS** ; ceux de « nos résultats » sont **OBSERVÉS-NON-AUDITÉS**. Aucun n’est revérifié ici. Les choix expérimentaux sont des **HYPOTHÈSES** ; leurs tailles, seuils et coûts sont **supposés/illustratifs**, sauf mention « calcul ».

La question suppose sans l’établir :

- **Qu’une propension brute est comparable entre modèles.** **HYPOTHÈSE** fragile : retirer un outil fait passer un taux de manigance de 59 % à 3 %, et les taux de base sont presque toujours nuls (**RAPPORTÉ**, Scheurer §2.1). Un zéro peut signifier absence d’occasion, refus ou mauvaise élicitation.
- **Que les tendances de capacités ordinaires se transportent au désalignement.** Le doublement METR d’environ sept mois et celui de TastEval sont **RAPPORTÉS** (§3.1–3.2), avec des éléments méthodologiques manquants ; ils ne démontrent aucune pente de manigance.
- **Que des comportements instruits ou plantés représentent le scheming spontané.** **HYPOTHÈSE** : ils mesurent d’abord une capacité accessible ou un contrôle sur attaques connues. Aucune tendance obtenue ne sera présentée comme une tendance de propension naturelle.
- **Que date de sortie, difficulté humaine et protocole figé donnent un axe commun.** **HYPOTHÈSE**, à tester contre les effets de famille, de taille, de contamination et d’échafaudage.

## Trois tendances candidates

Pour chacune : **12–18 modèles ouverts**, au moins trois familles, poids publiés sur **24–36 mois** ; dernier quart temporel et une famille entière réservés à la validation. La date retenue est celle de publication des poids, documentée avant l’analyse.

| Candidate | Grandeur et échelle continue | Pourquoi elle peut réussir ; menaces et contrôles | Énoncé attendu, non établi |
|---|---|---|---|
| **T1 — Horizon de subversion accessible** | Sous invites, échafaudage, budget et moniteur ouvert **figés**, probabilité qu’un épisode produise un artefact fonctionnel réalisant la classe plantée et passant le contrôle. Ajustement logistique contre la durée médiane d’un humain autorisé réalisant l’épisode ; **h50** = durée à 50 % de réussite. Les refus sont des échecs du protocole, mais publiés séparément. | Ne dépend pas du taux spontané. **Élicitation** : aucune adaptation par modèle ; **contamination** : tâches nouvelles horodatées ; **changement de moniteur** : impossible dans T1. Limite : capacité accessible, non capacité latente. | **HYPOTHÈSE** : h50 croît de **+10,4 %/mois** (*supposé ; calcul* \(2^{1/7}-1\), inspiration METR, non prédiction vérifiée). |
| **T2 — Horizon de surveillance à risque fixé** | Corpus d’attaques mécaniquement validées, gelé pour l’ajustement et renouvelé pour le test. Le moniteur note la trajectoire entière ; seuil calibré à **1 % de fausses alertes**. **c50** = difficulté humaine de l’attaque où la détection tombe à 50 %. Plus c50 est grand, meilleure est la surveillance. | Aucune attente d’événements spontanés rares et même corpus pour tous les moniteurs. **Artefacts de provenance** : jumeaux honnêtes produits par le même générateur ; **injections** : strates séparées, jamais moyennées avec le cas sans injection ; **contamination** : attaques fraîches finales. | **HYPOTHÈSE** : c50 croît de **+5,1 %/mois** (*supposé, illustratif ; calcul* pour un doublement en 14 mois). |
| **T3 — Calcul d’élicitation nécessaire** | Calendrier fixe de tentatives non adaptatives ; **q50** = calcul d’inférence attaquant, en FLOP plutôt qu’en jetons, auquel 50 % des tâches ont une réussite T1. Analyse de survie avec censure à qmax. | Remplace un taux souvent nul par une quantité continue et représente les non-réponses comme coût/censure. **Sur-élicitation** : interdite hors budget ; **plafond des juges** : aucune étiquette LLM ; **dérive du contrôle** : moniteur figé. | **HYPOTHÈSE** : q50 décroît de **−5,0 %/mois** (*supposé, illustratif*). |

Pour T1/T2, modèle logistique à effets de tâche ; pour T3, modèle de survie. Régression de \(\log(h50,c50,q50)\) sur la date, avec et sans taille du modèle ; **IC à 95 %** par bootstrap groupé sur tâches et modèles, validation temporelle et famille laissée de côté. Facteur mensuel : \(\exp(30,44\beta)\) (**calcul**). La portée reste limitée aux modèles échantillonnés.

## Deux duels décisifs

**E1 — Existe-t-il une tendance T2 transportable ?**  
- **H_A** : sur attaques fraîches, \(\beta\geq\log(1,05)\) par mois.  
- **H_B** : \(\beta<\log(1,05)\), y compris stabilité ou déclin.  
- **Métrique/seuil** : IC à 95 % de \(\beta\). Borne inférieure au-dessus du seuil ⇒ **H_B falsifiée** ; borne supérieure dessous ⇒ **H_A falsifiée** ; chevauchement ⇒ non concluant.  
- **Contrôles négatifs** : dates permutées, étiquettes permutées et corpus uniquement honnête ; aucun ne doit produire la pente annoncée.

**E2 — Le moniteur apporte-t-il autre chose qu’un détecteur d’artefacts ?**  
- **H_A** : sur les paires appariées fraîches, TD ≥ 80 %, TFA ≤ 1 %, et gain ≥ 10 points de détection sur les contrôles mécaniques disponibles au déploiement.  
- **H_B** : ce critère n’est pas atteint, ou le gain disparaît lorsque honnêtes et malveillants partagent générateur et distribution.  
- **Issue** : réussite préenregistrée sur le test final ⇒ **H_B falsifiée** ; TFA excessif ou borne supérieure du gain sous 10 points ⇒ **H_A falsifiée** ; sinon non concluant. Le cas rapporté où un moniteur fort donne 0 aux 375 échantillons sous injection (**RAPPORTÉ**, Scheurer §3.4) impose une strate injection distincte.

## Validité minimale des instruments

- **Vérificateur mécanique de vérité terrain** : fonctionnalité et condition plantée vérifiées indépendamment du moniteur ; il doit accepter tous les canaris valides, rejeter les artefacts invalides et ne marquer aucun jumeau honnête dans l’échantillon de qualification. Sinon, la tâche est retirée.
- **Moniteur** : critères E2, TD/TFA publiés par difficulté et par condition. Il doit battre tests fonctionnels simples, règles statiques et score fondé uniquement sur la sortie. Juges LLM et sondes d’activation ne servent pas de vérité terrain ; le plafond des juges est **OBSERVÉ-NON-AUDITÉ** (« nos résultats » §4).
- **Estimateur de tendance** : sous simulations nulles, fausse détection ≤ 5 % ; sur pentes plantées de +10 %/mois, détection ≥ 80 %. À défaut, aucune déclaration de pente.

## Pilote prioritaire et ancrage matériel

**Choix : T2**, car il évite l’élicitation adaptative et la rareté des comportements spontanés. Six moniteurs ouverts, 60 tâches, quatre attaques et quatre jumeaux honnêtes par tâche, deux conditions d’injection : **5 760 notations** (**calcul** : \(6\times60\times8\times2\)). Environ **150 h-H100 et 5–15 k€**, calibration humaine comprise (**illustratif**). Pilote **non concluant** si moins de 40 tâches restent valides, si plus d’un tiers des c50 sont censurés, ou si le TFA calibré ne se transporte pas au test ; il ne revendique alors aucun facteur mensuel.

Qwen2.5 fournit sept tailles de 0,5 à 72 milliards de paramètres, mais à une seule date (**RAPPORTÉ**, Scheurer §2.2) : utile pour séparer taille et date, insuffisant seul. Ajouter notamment Llama-3.1-8B-Instruct, dont la date reste à documenter. Étude complète : **500–1 500 h-H100, 30–100 k€** (**illustratif**).

**Échec du plan si :**
- les c50 sont presque tous censurés ou instables entre familles de tâches ;
- les attaques fraîches suppriment la pente, révélant contamination ou artefact de provenance ;
- on oublie que réussir T2 ne démontre toujours rien sur la propension spontanée.

FIN-DE-CELLULE
# Proposition D — transfert conditionnel, mesures avant métaphores

**Pièces absentes ou non transmises** : journaux et configuration de la course 2, mondes synthétiques et leurs étiquettes, journaux P-041, note de conv-audit, relectures d’Opus, code du papier et détails d’entraînement des moniteurs ; je n’en invente ni le contenu ni les résultats.

**Convention de statut.** **RAPPORTÉ** désigne une affirmation du manuscrit ou de la question, non vérifiée indépendamment ici. **OBSERVÉ-NON-AUDITÉ** désigne un calcul ou une observation numérique rapporté sans audit de ma part. **HYPOTHÈSE** désigne un transfert, une identifiabilité ou une prédiction à tester. Les preuves revendiquées par Ciric, 2026, *Protection of an RNA replicase by protocells has a ceiling and a price*, v0.19.4, ne deviennent pas des résultats sur l’organisme par simple renommage des objets.

## (a) Ce que la question suppose sans que ce soit établi

| Point supposé | Statut et objection |
|---|---|
| Il existe une correspondance terme à terme commune à l’organisme, à la pince et à l’arène. | **HYPOTHÈSE.** Dans le papier, la copie a un seul modèle, la réplicase n’est pas consommée, la lignée avec une seule réplicase est stérile et la division est aveugle. La question décrit au contraire une fusion à deux parents, des idées non consommées et une sélection par juge : ce ne sont pas des changements de paramètres, mais de noyau de reproduction. |
| Le bisociateur et ses fiches forment un système autocatalytique dont le rayon spectral est identifiable. | **HYPOTHÈSE.** Un opérateur extérieur qui n’est pas lui-même reproduit peut entretenir indéfiniment une production sans « allumage » endogène. Il faut séparer injection exogène, persistance et reproduction des lignées. |
| \(q,\theta,n,R,\tau,\theta'\) ont déjà des correspondants mesurables. | **HYPOTHÈSE**, actuellement **indécidable sans les journaux et le protocole expérimental**. En particulier, \(\theta'\) doit être un avantage reproductif mesuré, non un proxy de courte longueur, de similarité ou de score de juge. |
| Les fusions inachevées sont des copies tronquées au sens du papier. | **HYPOTHÈSE.** Une esquisse peut être inerte, complétable, fertile, ou produire des variantes envahissantes ; ces quatre sorts ne sont pas distingués par le seul statut « inachevée ». |
| La course 2 permet de sceller rétroactivement des prédictions sans fuite. | **HYPOTHÈSE**, non vérifiable sans empreintes, calendrier, historique des accès et étiquettes encore scellées. |
| Les mondes à vérité plantée fournissent une vérité extérieure suffisante. | **RAPPORTÉ.** Leur existence est décrite, mais ni l’indépendance des étiquettes ni l’absence de fuite dans les textes ne sont établies. |
| P-041 montre le contournement d’un moniteur réentraîné pendant plus de 70 tours, avec une antériorité publiée. | **RAPPORTÉ.** Les journaux ne sont pas fournis ; l’antériorité Bailey et collègues est **référence à vérifier**, faute de notice bibliographique complète. |
| Le plafond et le prix du papier s’appliquent numériquement aux trois cibles. | **HYPOTHÈSE.** **RAPPORTÉ** dans le papier : bonus inférieur à \(\ln2\) sous les hypothèses du modèle ; prix croissant avec \(n/R\). Aucun de ces nombres n’est transférable avant validation du noyau. |
| H2 ou les méthodes adversariales du programme se transfèrent automatiquement. | **HYPOTHÈSE.** **RAPPORTÉ** : H2 est prouvée, avec assistance informatique, sur les intervalles indiqués du manuscrit, et seulement soutenue numériquement ailleurs jusqu’à \(y=16\). Une recherche adversariale peut chercher un contre-exemple, pas établir une preuve. |
| La croissance recombinante de Weitzman fournit le modèle de remplacement. | **HYPOTHÈSE** ; **référence à vérifier**. Le remplacement doit d’abord être un branchement multitype à deux parents, avec temps et injection explicites. |

### Ce qui peut néanmoins être scellé

Ce sont des **prédictions conditionnelles**, non des résultats sur la course 2 :

1. **HYPOTHÈSE de transfert** : à noyau par ailleurs conforme, augmenter le rendement de copies inachevées perdues augmente la fécondité requise ; augmenter la production de fragments recopiables et reproductivement avantagés diminue la tolérance du système.
2. **RAPPORTÉ** : dans le modèle du papier, le sort perdu multiplie la fécondité requise par \(1/(1-\tau)\) ; à \(\theta'=\theta\), le seuil est déplacé de \(\ln(1-\tau)\). **OBSERVÉ-NON-AUDITÉ** : à \(\theta'=2\), le manuscrit rapporte une annulation de la charge tolérable pour \(n\tau\) entre environ 1,5 et 1,85, aux tailles calculées. Ces valeurs ne doivent pas devenir des seuils de la course 2.
3. **Prédiction globale** : le signe de \(\rho-1\) pour la configuration prévue de la course 2 est **indéterminé**, et non « positif par analogie ».

**Sur « les fusions inachevées doivent être jetées, jamais archivées » : non, ce n’est pas établi.** Le papier distingue précisément perte et recopiabilité. La garde la moins irréversible est **quarantaine hors vivier, sans réinjection, avec conservation probatoire** ; la suppression définitive n’est justifiée ni par le théorème ni par les données fournies.

## (b) Expériences à duel pour trancher

Protocole commun : hypothèses, seuils, exclusions et analyses scellés avant lecture ; indépendance comptée par **famille de concepts ou d’attaques**, non par document ; intervalles à 95 % par amorçage au niveau famille. Chaque issue concluante falsifie l’hypothèse adverse ; un intervalle couvrant le seuil laisse le duel indéterminé.

### E0 — Le modèle réduit est-il même admissible ?

- **H_A** : un noyau réduit de type copie à un modèle prédit les descendances hors échantillon à erreur inférieure à une marge \(\varepsilon\), fixée par le bruit de mesure et l’accord inter-annotateurs.
- **H_B** : son erreur dépasse \(\varepsilon\), et un noyau à deux parents est nécessaire.
- **Métrique et seuil** : erreur sur la matrice moyenne de descendances vivantes et sur le nombre de descendants fertiles par fusion, sur paires de parents et familles entièrement retenus ; seuil \(\varepsilon\) scellé.
- **Contrôle négatif** : parents permutés, un seul parent, concaténation sans génération, et fuite volontaire d’étiquettes comme contrôle de détection.
- **Issues** : erreur \(<\varepsilon\) avec avantage sur les contrôles ⇒ **H_B falsifiée** ; erreur \(>\varepsilon\) ou disparition de l’avantage ⇒ **H_A falsifiée**.

### E1 — Quel sort pour les inachevées ?

Comparer, à budget et parents identiques, **vivier avec inachevées** contre **quarantaine sans réinjection**.

- **H_A** : leur présence dans le vivier réduit la reproduction nette, \(\Delta\rho=\rho_{\rm vivier}-\rho_{\rm quarantaine}<0\).
- **H_B** : elle ne la réduit pas, \(\Delta\rho\geq0\).
- **Métriques** : \(\Delta\rho\), concepts externes validés par unité de calcul, taux de lignées dominées par des fragments ; analyses stratifiées par \(\theta'\) mesuré comme taux relatif de reproduction, et par complétion ultérieure.
- **Contrôle négatif** : fragments synthétiquement inertes, archive inaccessible, et même nombre d’appels sans contenu fragmentaire.
- **Issues** : \(\Delta\rho<0\) ⇒ **H_B falsifiée**, les inachevées restent hors vivier ; \(\Delta\rho\geq0\) ⇒ **H_A falsifiée**, l’exclusion universelle est infondée, sans autoriser leur réinjection non contrôlée.

### E2 — Allumage ou simple production alimentée ?

- **H_A** : après retrait de toute injection de nouvelles fiches, le système est supercritique, \(\rho>1\).
- **H_B** : il est non supercritique, \(\rho\leq1\), et sa production repose sur l’injection.
- **Métrique** : rayon spectral de la matrice de descendances des **lignées**, avec types « complet/inachevé », parents et statut de juge ; le taux d’injection est estimé séparément.
- **Seuil** : \(\rho=1\), avec persistance observée sur un horizon fixé à l’avance comme vérification indépendante.
- **Contrôles négatifs** : bisociation désactivée, sorties stérilisées, parents uniques, et injection connue sans reproduction (\(\rho=0\) attendu).
- **Issues** : borne inférieure de \(\rho>1\) ⇒ **H_B falsifiée** ; borne supérieure \(\leq1\) ⇒ **H_A falsifiée**. Un simple accroissement du nombre de fiches ne tranche rien.

### E3 — La pince apporte-t-elle une information nouvelle ?

Duel exécuté séparément pour la sonde d’activations et pour le moniteur texte.

- **H_A** : l’instrument améliore la détection sur des familles d’attaques entièrement futures, à taux de fausses alertes et utilité honnête fixés.
- **H_B** : il n’apporte aucun gain au-delà des vérifications mécaniques et du moniteur figé.
- **Métrique** : \(\Delta\)TPR à FPR fixé, et taux de succès d’attaque ; seuil de gain \(0\), familles et générateurs retenus.
- **Contrôles négatifs** : activations permutées, étiquettes permutées, entrées honnêtes appariées, et attaques déjà vues uniquement comme test de bon fonctionnement.
- **Issues** : gain positif reproductible ⇒ **H_B falsifiée** ; absence de gain ou disparition après appariement ⇒ **H_A falsifiée**.

### E4 — Le réentraînement de l’arène généralise-t-il ?

- **H_A** : le réentraînement sur les attaques passées réduit le succès des attaques de la famille suivante par rapport à une défense figée.
- **H_B** : il ne la réduit pas.
- **Métrique** : différence de taux de succès d’attaque à FPR honnête et dégradation d’utilité fixés ; validation chronologique et une famille entière réservée à chaque pli.
- **Seuil** : \(0\), avec analyse par famille et non seulement moyenne globale.
- **Contrôles négatifs** : poids figés, réentraînement à étiquettes aléatoires, et absence de moniteur.
- **Issues** : réduction positive ⇒ **H_B falsifiée** ; absence de réduction ou aggravation ⇒ **H_A falsifiée**.

## (c) Mesure minimale de fonctionnement des instruments

Aucun taux réel n’est disponible dans les pièces fournies. Le minimum est donc une estimation avec intervalles, sur des cas retenus, non un score moyen sur les exemples de développement.

| Instrument | Détection et fausses alertes à rapporter | Cas honnêtes appariés | Vérifications mécaniques à battre |
|---|---|---|---|
| **Bisociateur** | TPR pour « concept externe valide » et pour « lignée fertile » ; fausses alertes sur faux, proche, surface et reprise d’un parent. | Paires appariées par longueur, distance documentaire, difficulté et espace ; parents seuls et paires aléatoires. | Meilleur parent seul, concaténation, résumé extractif, recherche du texte source le plus proche, absence d’opérateur. |
| **Juge de fiches** | Matrice de confusion sur les statuts plantés ; taux de validation erronée par classe ; accord avec spécialistes aveugles. | Même contenu avec surface et longueur variées ; vrais concepts mal présentés et faux bien présentés. | Longueur, chevauchement lexical avec les parents, présence de mots-clés, score de similarité. |
| **Sonde sur activations** | TPR à FPR fixé, par famille future ; fausses alertes pour 1 000 entrées honnêtes ; stabilité inter-graines. | Mêmes tâches, langues, longueurs, modèles générateurs et taux de refus que les attaques. | Norme des activations, moyenne par couche, classifieur linéaire simple, longueur et métadonnées d’entrée. |
| **Moniteur texte** | TPR et taux de contournement à FPR et utilité fixés ; coût par famille honnête. | Textes appariés par sujet, style, longueur et intention bénigne, y compris formulations inhabituelles. | Liste lexicale, perplexité, plus proche voisin, règle déterministe, moniteur figé et vote majoritaire. |
| **Arène P-041** | Succès d’attaque résiduel et FPR après chaque tour ; fraction de familles où la défense échoue. | Les mêmes tâches honnêtes à chaque tour, avec difficulté et distribution appariées. | Pas de défense, défense figée, réentraînement aléatoire, filtre mécanique seul. |

Le nombre minimal de cas est celui qui rend l’intervalle de différence plus étroit que la marge scellée ; dupliquer des variantes d’une même famille ne remplace pas des familles indépendantes.

## (d) Ancrage matériel, calcul et coût

**Modèles ouverts et calcul nécessaire.** Le manuscrit fournit le noyau \(K=BH+2^{1-2n}I\), le critère \(\rho=1\) et le processus limite ; le code n’est pas inclus et son dépôt est seulement **RAPPORTÉ** comme prévu. Si E0 survit, il faut recoder indépendamment le noyau réduit, calculer ses racines et comparer aux journaux. Sinon, le modèle minimal est un **branchement multitype à deux parents** : types parentaux, sort du produit, décision du juge, durée de vie, injection et taux de complétion ; la sélection entre dans le noyau, elle n’est pas une fitness postulée.

Pour la boîte blanche, utiliser un modèle à poids ouverts donnant accès aux activations, avec version, poids et empreintes gelés ; un modèle de **7–9 milliards de paramètres sur un GPU de 24–48 Go est un choix illustratif**, non une exigence établie.

**Coûts illustratifs, hors annotation humaine** :
- réanalyse CPU des journaux existants et matrices de lignées : **2–6 jours-CPU** ;
- deux implémentations indépendantes des noyaux réduits aux petites tailles : **10–100 heures-CPU**, à réestimer après E0 ;
- extraction d’activations et évaluation par familles : **50–200 heures-GPU** ;
- recherche adversariale de tangences pour H2, puis certification par intervalles si nécessaire : **10–100 jours-CPU**.

Les **8–10 USD par tour** mentionnés dans la question sont **RAPPORTÉ** comme coût de sessions antérieures, pas comme devis de ces expériences.

**Vérification extérieure.** Sceller les empreintes des journaux avant accès, réserver familles et périodes, faire annoter un sous-ensemble par des spécialistes aveugles au bras expérimental, et reproduire les estimations avec un code indépendant. La littérature sur l’innovation recombinante ne doit être mobilisée qu’après notices vérifiables.

**Apport inverse au papier.** Le programme fournit surtout une discipline de test : retenir des familles entières, validation chronologique, contrôles mécaniques, comptage des échecs par famille et séparation explicite entre exploration et certification. Appliqué à H2, cela peut cibler les régions non certifiées et chercher des contre-exemples ; seuls une preuve ou des certificats vérifiables changeraient ensuite son statut.

FIN-DE-CELLULE
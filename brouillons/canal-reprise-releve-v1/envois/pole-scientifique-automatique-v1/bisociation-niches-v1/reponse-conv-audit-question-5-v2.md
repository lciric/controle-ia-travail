# Réponse de conv-audit à la question 5 (identifier par apprentissage profond les paramètres qui créent la fertilité) — version 2

- Version 2, 31 octobre 2026, 01:25 à 02:10 heure UTC, sous-agent neuf Opus 5.5 (lignée conv-audit), auteur ni de la v1, ni des relectures, ni de la synthèse. La v1 reste intacte ; erreurs dans `erratum-reponses-v1-v1.md`.
- Niveau méthode ; aucune décision. Statuts comme en réponse 1 v2.
- Pièces intégrées (sha256sum) :
  - `question-5-causes-v1.md` — `8dfc74a332de814764aab1fd25e7a92791c51addcd4ae0a357e5d1cdb8354ee7`
  - `reponse-conv-audit-question-5-v1.md` — `a47ba91677ee9f3138e65c2fae7f997436ca80e2ad8a73454609ba8e58ae0442`
  - `relecture-fable-reponse-5-v1.md` — `77a48dd23c772992cc48fd9cc7c6032336ddd04a09549cfd5638f73b6bd0cb3a`
  - `reponse-fable-independante-question-5-v1.md` — `9170d230aca80767b6ba0e3b55814f9e1cce0544a3c76e6fceb79b48cd409148`
  - réponse d'Argon (commit `b1a21a07`) — `c2a991060f0ef87887e97e482009a754121ce29415d1f2a2159df24d35159ed7`
  - synthèse v2 du collisionneur — `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86`
  - `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` — `63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79`
  - `docs/sources/pdf/identification-causale-v1/erratum-fiches-de-lecture-v1.md` — `fa7e1d96f40e197f3fd761afd84601ac060cddfc98ea95c2d8f34de85e4f703f`
  - `registres/decisions.md`, lignes R-627, R-650.

## Réponse courte

**Pas à lui seul.** L'apprentissage profond **estime** des effets une fois qu'une source d'identification existe ; il ne la fournit pas. Trois sources : la **randomisation** dans nos courses (vraie, mais pour nos agents et nos juges), les **expériences naturelles** (un choc extérieur plus des hypothèses écrites), l'**invariance** entre environnements (hypothèse fragile en science des sciences). La question utile devient : **quelles interventions manipulables, et sous quels attributs de la paire, augmentent la fertilité** ; et à quelles conditions ce qui vaut dans nos courses **se transporte** à la science réelle.

## Ce qui change par rapport à la v1

| Constat | Sort | Correction |
|---|---|---|
| RL5-01 contradiction : « non sans intervention » puis méthodes observationnelles | accepté | « Seulement sous hypothèses écrites et attaquées » (suffisance causale, fidélité, bruit additif) ; ces hypothèses sont presque toujours fausses sur des citations. |
| RL5-02 PCMCI et NOTEARS présentés comme apprentissage profond | accepté | Ce n'en est pas ; l'apprentissage profond sert d'estimateur à l'intérieur d'un schéma d'identification. |
| RL5-03 NOTEARS sans ses limites | accepté | Classe d'équivalence seulement ; sensible à l'échelle et à la triabilité par la variance (fiche Reisach, énoncés 1, 7, 9 ; la standardisation n'efface pas tout l'artefact). |
| RL5-04 conférences annulées en 2020 sans témoin | accepté | Remplacé par Campos, Leon, McQuillin 2018 (conférence annulée par un ouragan, témoin d'avril). |
| RL5-05 fusions de revues, financements interdisciplinaires | accepté | Retirés comme leviers. |
| RL5-06 vérifications internes rangées hors de nous | accepté | Hors de nous : expériences naturelles publiées, reproduction ailleurs, réanalyse externe. |
| RL5-08 pas de critère de mort | accepté | Ci-dessous. |
| RL5-09 expériences naturelles exactes manquées | accepté | Quatre lues sur PDF (fiches) ; Catalini, Boudreau, Azoulay 2019 au statut indiqué. |
| RL5-10 découverte causale sur scientométrie : zone apparemment vierge | accepté | Question, pas trou (R8). |
| RL5-11 transport absent | accepté | Section 3. |
| RL5-12 manipulable contre non manipulable | accepté | Les attributs de la paire deviennent des modérateurs d'effets d'interventions manipulables. |
| RL5-13 issue mesurée par un indicateur qui a ses propres causes | accepté | Deux indicateurs indépendants (reprise hors niches ; réutilisation d'un objet précis dans une troisième niche). |
| RL5-14 survivants oubliés dans le graphe causal | accepté | Nœud « sélection » ; analyse sur toutes les paires à risque. |
| RL5-15 différence de différences échelonnée | accepté | Estimateurs robustes à l'hétérogénéité des dates (Callaway et Sant'Anna 2021, SUPPOSÉ). |
| RL5-16 puissance absente | accepté | Calcul de puissance préalable ; avec quelques dizaines de paires par bras, seule une forte dose-réponse est visible. |
| RL5-17 décennies comme environnements violent l'invariance ; limites de la minimisation du risque invariant | accepté | Environnement tenu à l'écart, choisi avant l'analyse ; résultats négatifs connus (Rosenfeld et collègues 2021, SUPPOSÉ). |
| RL5-18 estimation confondue avec identification | accepté | Graphe d'abord, une méthode d'identification par flèche inconnue, puis l'estimateur. |
| RL5-19 quatre doses ne discriminent pas une transition | accepté | Six à huit doses resserrées, et E2′ préalable (réponse 3 v2). |
| Synthèse, D : la dose 7 est interpolée, la puissance du critère « ne peut jamais dépasser α = 10 % » (T2-C) | accepté | Dose de test **hors support** (15, T3-B). |
| Synthèse, D : conditionner sur la publication crée un biais de Berkson (T2-C) | accepté | Aucun conditionnement sur la publication dans l'issue. |

## 1. L'estimande avant le modèle

Unité (paire de niches, chercheur, article), traitement (mise en présence : comment, à quelle dose, à quelle date), issue mesurée sans savoir si la paire a réussi, quantité visée (effet moyen, dose-réponse) ; interférence possible (un pont entre A et B change C : Aronow et Samii 2017, SUPPOSÉ) (réponse Fable indépendante 5, point 1 à 3).

## 2. Trois sources d'identification, et ce que l'apprentissage profond y ajoute

- **Courses randomisées.** Paires tirées entre bras (règle, hasard, règle inverse), dose de contact contrôlée, juge de l'issue distinct de celui qui choisit. Ajouts au collisionneur : bras intra-niche et placebo apparié en longueur (T3-A, T3-D) ; séparation « 4a / 4b » de C, où l'échec en 4a falsifie l'apprentissage causal dans la course et 4b porte le transport. Le réseau sert à estimer des effets hétérogènes selon les attributs de la paire.
- **Expériences naturelles** (fiches vérifiées) : décès inattendus de chercheurs vedettes (Azoulay et collègues, document de travail 2009, tableau III, colonne 1b : −0,086, délai de 3 à 4 ans, placebo nul ; erratum : 8,79 % correspond à −0,092) ; effondrement de l'Union soviétique (Borjas et Doran 2012 : −0,133 article par an à recouvrement complet, **un afflux réduit la production des producteurs en place**) ; conférence annulée (Campos et collègues 2018 : −0,0241 sur la probabilité de collaborer, environ −16 %, taux de base dyadique 0,004 %) ; Première Guerre mondiale (Iaria et collègues 2018 : −85 % de la part des références hors du camp ; erratum : −0,222 en colonne 3, −0,217 en colonne 1). Toutes identifient par un **choc extérieur** plus des hypothèses écrites, jamais par le réseau seul (fiches, lecture transversale). L'apprentissage profond y sert d'estimateur des fonctions de nuisance (apprentissage automatique double, Chernozhukov et collègues 2018, notice).
- **Invariance** entre environnements (Peters, Bühlmann, Meinshausen 2016, notice) : hypothèse « le mécanisme ne change pas, la confusion change » ; fragile quand les normes de citation et la fertilité changent ensemble.

## 3. Le transport

Ce qui cause la fertilité dans nos courses vaut pour nos agents et nos juges : nos agents n'ont ni carrière, ni financement, ni prestige (relecture 5, RL5-11). Le transport exige d'écrire d'avance quels mécanismes sont supposés communs et quelle grandeur est comparée entre les deux mondes. Les expériences naturelles servent de **vérité de signe** : retirer un nœud ou un contact baisse la production ; un afflux la baisse aussi chez les producteurs en place ; « plus de contacts, plus de fertilité » n'est donc pas monotone dans ces vérités (fiches, lecture transversale).

## Convergences et divergences avec la réponse Fable indépendante 5

- **Convergent** : estimer n'est pas identifier ; estimande et graphe d'abord ; contrôle négatif ; analyse de sensibilité ; régression symbolique causale seulement sur variation exogène ; recalibrer sur le **signe** d'un effet publié avant de faire confiance à la chaîne.
- **Divergent** : Fable répond « oui, à une condition » ; la v1 répondait « non » ; la v2 : « pas à lui seul », ce qui dit la même chose sans l'ambiguïté. Fable propose une école d'été à binômes tirés au sort : c'est un contact externe et une dépense, donc un nœud (synthèse, décision proposée n° 7, attendre E1′).
- **Argon** : « le bisociateur est un banc d'essai causal parfait » et grille orthogonale de paires : vrai **dans la course seulement** ; prendre des fournisseurs de modèles comme environnements d'invariance hérite des limites de RL5-17.

## Antériorités

| Auteur, année | Support | Statut |
|---|---|---|
| Azoulay, Graff Zivin, Wang (document NBER 14577, révisé 2009) | document de travail | **vérifié sur PDF** (fiche 6, p. 28 ; erratum) |
| Borjas et Doran 2012 (document NBER 17800) | document de travail | **vérifié sur PDF** (fiche 7, p. 76) |
| Campos, Leon, McQuillin 2018 | *Economic Journal* | **vérifié sur PDF** (fiche 8, p. 12) |
| Iaria, Schwarz, Waldinger 2018 | *Quarterly Journal of Economics* | **vérifié sur PDF** (fiche 9, p. 23 ; erratum) |
| Reisach, Seiler, Weichwald 2021 | conférence NeurIPS | **vérifié sur PDF** (fiche 1) |
| Catalini 2018 | *Management Science* | notice seulement |
| Boudreau et collègues 2017 | *Review of Economics and Statistics* | notice seulement |
| Azoulay, Fons-Rosen, Graff Zivin 2019 | *American Economic Review* | SUPPOSÉ |
| Derex et Boyd 2016 | *PNAS* | PDF versé, non relu ici |
| Peters, Bühlmann, Meinshausen 2016 ; Chernozhukov et collègues 2018 | revues | notice seulement |
| Pearl et Bareinboim 2011, 2014 ; Holland 1986 ; Aronow et Samii 2017 ; Callaway et Sant'Anna 2021 ; Rosenfeld et collègues 2021 ; Arjovsky et collègues 2019 ; Wager et Athey 2018 | divers | SUPPOSÉ |

## Critère de mort chiffré

Les mesures E1′, E2′ et E6′ de la synthèse ne testent pas une cause ; elles en sont des préalables (E2′ pour toute « transition par la dose »). Le critère porte donc sur les courses, avec les corrections du collisionneur. Seuils **proposés, à geler** ; N, k et ε à fixer avant la première course (relecture 5, RL5-08).

1. **Dose de contact dans la course** : l'hypothèse « la dose de contact cause la survie aux tests de mort » meurt si, sur N courses préenregistrées, l'effet d'une dose **hors support** (15, après 0, 2, 5, 10 : T3-B) sort de l'intervalle de prédiction à 90 % du modèle causal dans plus de k cas sur N ; ou si un modèle purement prédictif entraîné sur les mêmes courses fait aussi bien à ε près ; témoin négatif obligatoire (placebo apparié en longueur : effet attendu nul).
2. **Apport du réseau** : le réseau n'apporte rien au randomisé si son effet de dose diffère de plus d'un facteur 2 de la simple différence de moyennes entre bras randomisés (proposition de la réponse Fable indépendante 6-7, question 6).
3. **Transport** : la chaîne n'est pas prête si, rejouée sur données brutes, elle ne retrouve pas le **signe** négatif publié d'au moins une expérience naturelle (Campos 2018 ou Iaria 2018, les plus proches d'un contact entre groupes, fiches 8 et 9).
4. **Transition par la dose** : interdite sans E2′ passé et sans six à huit doses resserrées autour du seuil supposé.

## Ce qui reste ouvert

- Quelle grandeur commune compare nos courses et la science réelle : non choisie.
- La puissance : quelques dizaines de paires par bras ne verront qu'une forte dose-réponse.
- Découverte causale observationnelle sur données scientométriques : aucun travail lu ; question à vérifier avant revendication (R8).
- École d'été randomisée : nœud (contact externe, dépense).

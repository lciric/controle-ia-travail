# Décision — N-068 : HC2 reformulée après MIRAGE — la sonde qui lit l'agent auteur, mesurée par g en plan apparié et comparée aux juges (v1, brouillon 1)

- **Décision de Lazar** : mots directs consignés à R-2555 (`registres/decisions.md`, 2026-11-13, 18:15 UTC). Option **B (a)** : les quatre collisions partielles constatées sur PDF sont tranchées en bloc, sur les recommandations ; pour HC2, « reformulée comme proposé (R-2180) ». Deuxième des quatre décisions (N-067 à N-070).
- **Statut : brouillon 1, non retenu.** Écrit le 13 novembre 2026 entre 18:25 et 18:31 UTC (`date -u`) par un rédacteur neuf. À contre-lire par un lecteur neuf, puis recopié sous `decision-N-068-v1.md`, scellé (R6), une ligne de type « revendication » inscrite à `registres/go.md` et la liste de `CLAUDE.md` complétée, par la session mère. Le brouillon reste (R12).
- **Nœud posé par** : R-2180, rapport du lot 1 (lecteur neuf, branche `prep/etat-de-l-art-niveau3-pieces-v1`) ; synthèse provisoire de niveau 3, sections 1 et 3, point 2 de la section 8. Décisions d'origine : N-005 et N-006 (HC2, jamais l'immunité absolue), N-013 (énoncé de HC2 inchangé, bras « sonde du lecteur »).
- **Portée.** Cette note fixe la lecture de HC2 au programme v2 (papier C) et dans les décisions N-005, N-006 et N-013, en attendant une version nouvelle du programme, qu'elle ne modifie pas. Le préenregistrement du papier C part de cet énoncé. HC2 reste un test (R3) : seule la partie publiée cesse d'être revendiquée.
- **Règle de lecture.** « Libre » veut dire « non trouvé dans les pièces lues » (R8). Chaque page citée vient d'un rapport de lecteur qui l'a contrôlée par programme sur le PDF empreinté. Les chiffres de MIRAGE ne sont **pas opposables** en l'état (section 3).

## 1. Mots de Lazar, verbatim (R-2555)

> A (a) go, B (a) go, D go, C. Horodatage public des pièces libres (enregistrement figé sur OSF, sans résultat). * Recommandation : go, confiance 0,6. : go

Lecture de la mère, consignée au même registre (extrait sur B) : « **B (a)** : les **quatre collisions partielles tranchées en bloc** sur les recommandations — […] HC2 reformulée comme proposé (R-2180) […] ; décisions à écrire, contre-lire et sceller dans `docs/decisions/` avant tout usage ».

Recommandation suivie : la formulation proposée par le lecteur du lot 1 (`rapport-lot1-HC2-mirage-karne-v1.md`, § 3.1), résumée par R-2180 : « sonde qui lit l'agent auteur et adversaire ; déplacement continu g en plan apparié ; comparaison aux juges ». **Avec l'ajustement postérieur du lecteur du lot 3-A** (`rapport-lot3A-sondes-sabotage-injection-v1.md`, `64b728d6…`, même branche, § 10.5), repris par la synthèse finale de niveau 3 (`docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md`, `e30a013d…`, section 7, point 2) : le plan apparié n'est pas en soi une pièce neuve (2610.18408, p. 4, 12). Ne pas le reprendre reviendrait à revendiquer plus qu'une pièce lue sur PDF ne le permet.

## 2. Énoncés d'origine, recopiés

- `docs/programme-controle-ia-v2.md` (`2fd63bad…`, empreinte de lancement), l. 103 : « **HC2 — robustesse des sondes** (0,65 ; 0,15 dans la version « immunité absolue », abandonnée). Sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste. »
- Même fichier, l. 43 (thèse du papier C, extrait) : « les sondes à agrégation robuste ont g ≤ 0 sous attaque par contenu ».
- Même fichier, l. 16 : « HC2 (robustesse sous attaque par contenu boîte noire ; l'immunité absolue est réfutée) ».
- Même fichier, l. 195 : « **EC.2** Sondes sous les mêmes attaques, plan 2 × 2 rhétorique × intention (agent honnête qui plaide sincèrement contre saboteur qui tient le même plaidoyer) : signe de g_sonde (HC2, HC2b). »
- `docs/decisions/decision-N-005-N-006-v1.md` (`cd49afbc…`), l. 97 : « HC2 (robustesse, jamais immunité absolue) ».
- `docs/decisions/decision-N-013-v1.md` (`157d388e…`), l. 90 : énoncé de HC2 inchangé ; l. 92 : « Pour HC2, le préenregistrement du papier C ajoute un bras « sonde du lecteur » ».
- `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md` (`c5465a9b…`), l. 233 : « **Reste revendicable** : la robustesse sous attaque par contenu d'une sonde lisant l'agent, avec agrégation robuste, mesurée par g (jamais l'immunité absolue). »

## 3. Ce qui est pris, et par qui

Pièce : Revankar et collègues, « MIRAGE », arXiv 2606.10304 v1, atelier « Agents in the Wild », ICML 2026 ; `docs/sources/pdf/niveau3-v1/2606.10304v1.pdf` (branche `prep/etat-de-l-art-niveau3-pieces-v1`), `677fe27807039ea0…`, 28 pages. Rapport : **lot 1** = `docs/sources/lecture-pdf-niveau3/rapport-lot1-HC2-mirage-karne-v1.md` (`9996f40c…`), même branche ; 115 citations contrôlées, 0 échec.

| composante de HC2 (lot 1, § 3.1) | MIRAGE | page |
|---|---|---|
| (ii) attaque par le contenu | **faite** : consigne injectée (120 essais), suffixe optimisé | 7, 13, 18 |
| (iv) agrégation robuste | **faite** : maximum de moyennes glissantes sur 5 jetons ; agrégations comparées hors attaque seulement | 4, 6, 12, 15-16 |
| (iii) boîte noire | **en partie** : catalogue fixe de 24 consignes écrites en connaissant la sonde, jouées une fois, sans requête au score ; échantillonnage avec score, N ≤ 50 | 7, 13, 14, 18-19 |
| (i) sonde qui lit l'agent auteur | **à moitié** : la sonde lit l'agent qui agit, pendant la génération, mais cet agent est la **victime** d'un contenu écrit par un tiers | 2, 13 |
| (v) mesure par g | **non faite** : taux d'évasion à deux seuils, moyennes par famille ; ni témoin apparié, ni cible, ni juge sous la même attaque | 7, 18-20 |
| (vi) moniteur de contrôle sous attaque | **non fait** : injection indirecte sur un agent victime ; bras adverse à un tour, sans outil | 1, 13, 19 |

**Ce que MIRAGE publie, exact dans sa lettre** : aucune évasion conjointe, au seuil par défaut, d'une sonde à maximum glissant lue pendant la génération d'un agent victime d'injection, sous un catalogue de 24 consignes et un échantillonnage N ≤ 50 (p. 7, 19, 20).

**Pourquoi ce n'est pas opposable** (lot 1, § 1.5) : six essais sur 120 seulement réussissent l'exfiltration (« 6/120 », p. 20), donc « 0 sur 120 » vaut « 0 sur 6 » ; 3 évasions sur 120 au seuil 0,405 ; 2 sur 120 sur Qwen-1.5B ; une évasion par écriture dans les activations pour 4 familles d'encodage sur 9 (p. 19) ; 23 attaques conformes manquées sans adversaire dans la suite agentique (p. 21) ; au moins dix incohérences internes ; données non publiées (p. 14).

**Lettre de l'énoncé touchée** : la ligne « reste revendicable » du niveau 2 (l. 233 ci-dessus) est, hors « mesurée par g », ce que MIRAGE annonce (lot 1, § 3.1). Elle doit être resserrée.

## 4. Énoncé resserré

**HC2, énoncé retenu** (formulation du lecteur du lot 1, § 3.1, reprise sans changement de fond, puis précisée par le lot 3-A au point qui suit) :

> Pour une sonde qui lit l'**agent auteur du contenu adverse destiné au moniteur** — agent non fiable d'un protocole de contrôle, et non victime d'une injection écrite par un tiers —, le **déplacement continu g du score**, mesuré en **plan apparié** (même tâche avec et sans contenu adverse ; plan 2 × 2 rhétorique × intention de EC.2), **comparé au g des juges génératifs sous les mêmes attaques**, pour plusieurs agrégations dont une robuste, sur des trajectoires. Jamais l'immunité absolue.

- **Ce qui est propre dans cet énoncé** (lot 3-A, § 10.5) : l'agent **auteur et adversaire**, le déplacement **continu en fonction de l'intensité**, la comparaison aux **juges génératifs sous les mêmes attaques**. Le **plan apparié en soi n'est pas revendiqué comme neuf** : Kale et Vishwanath l'emploient déjà pour des sondes d'exposition côté lecteur (jumeau propre, sosie inoffensif ; 2610.18408 v1, p. 4, 12).

- **Prédiction, inchangée dans son signe** : g_sonde ≈ 0 (au plus nul) pour une sonde à agrégation robuste lisant l'agent auteur, sous attaque par contenu en boîte noire ; à chiffrer au préenregistrement (R1), avec g_juge en regard. Le poids 0,65 du programme est celui de Lazar ; cette note ne le change pas, mais la section 6 le rend moins sûr.
- **Ce qui n'est plus revendiqué** : la robustesse sous attaque par contenu d'une sonde lue pendant la génération d'un agent, avec agrégation robuste, au sens d'une absence d'évasion à seuil. Elle est publiée (MIRAGE), et se cite comme publiée, non opposable.
- **Formulation de citation**, reprise du lot 1 : « Cité comme publié, non opposable : aucune évasion conjointe au seuil par défaut d'une sonde à maximum glissant lue pendant la génération d'un agent victime d'injection, sous un catalogue de 24 consignes et un échantillonnage N ≤ 50 (2606.10304, p. 7, 19, 20 ; 6 exfiltrations réussies sur 120 essais). »

## 5. Ce qui reste à mesurer

- g_sonde et g_juge, appariés, sur la même tâche avec et sans contenu adverse, l'agent auteur étant l'adversaire ; plusieurs agrégations, dont une robuste ; sur trajectoires ; dans un cadre de moniteur de contrôle (EC.1, EC.2).
- **Propositions du lecteur, à porter au préenregistrement du papier C, non fixées par cette note** (lot 1, § 3.1, dernier paragraphe, et § 1.5, réserve 5) :
  1. **trois positions de sonde** au lieu de deux : lecteur du contenu (Karne), agent victime qui agit sous injection (MIRAGE), agent auteur et adversaire (HC2) ;
  2. **l'évasion par délégation à un outil** parmi les attaques (le calcul nuisible confié à un outil n'a rien à lire dans le canal de la sonde).
- La **contrôlabilité** du modèle surveillé, mesurée avant de lire HC2 (C9, § 6, point 4) : le bras « fuite textuelle et contrôlabilité » de N-053 y répond déjà ; rien de neuf à décider.
- **Autres propositions de lecteurs pour ce préenregistrement, non fixées ici** : un témoin lexical (mêmes mots, sans intention) (lot 7-C, § 7) ; séparer « l'agent tente de manipuler » de « le contexte de l'agent contient un texte manipulateur », puisqu'une sonde sur un agent sous injection lit d'abord l'exposition, pas l'engagement (2610.37679, p. 1, 7 ; lot 3-A, § 5 et § 10.5).

## 6. Citations obligatoires et contre-indices publiés touchant la prédiction

**Obligatoires** : MIRAGE, arXiv 2606.10304 v1 (référence en section 3), cité comme publié et non opposable, avec la formulation de la section 4 ; et, partout où le plan apparié est décrit, Kale et Vishwanath, arXiv 2610.18408 v1, p. 4, 12 (référence dans la table ci-dessous ; **ajout à la liste de la mère**, qui suit de l'ajustement du lot 3-A).

**Contre-indices à dire avec la prédiction** (tous lus sur PDF ; empreintes vérifiées contre les compagnons le 13 novembre 2026). Rapports : **C9** = `docs/etat-de-l-art/niveau3-v1/rapports/rapport-C9-pieces-neuves-papiers-C-B-v1.md` (`23ec1f6e…`, branche `prep/etat-de-l-art-niveau3-v1`) ; **lot 7-B** = `docs/sources/lecture-pdf-niveau3/rapport-lot7B-collusion-papier-B-v1.md` (`bf9b6af8…`) ; **lot 7-C** = `…/rapport-lot7C-juges-papier-C-v1.md` (`2b03ede0…`) ; **lot 3-A** = `…/rapport-lot3A-sondes-sabotage-injection-v1.md` (`64b728d6…`), tous trois sur la branche `prep/etat-de-l-art-niveau3-pieces-v1`. Les PDF marqués `…/lot3/` et `…/lot7/` sont sous `docs/sources/pdf/niveau3-v1/` de cette dernière branche.

| pièce | ce qu'elle montre | page | position de la sonde | rapport |
|---|---|---|---|---|
| Karne, « Safety Monitors Mostly Catch What the Model Already Refuses », arXiv 2609.05797 v3 ; `docs/sources/pdf/niveau3-v1/2609.05797v3.pdf` (branche pièces), `eb7be6cafe328086…` | une réécriture naturelle, sans attaquant, déplace des sondes lues sur le modèle lecteur (2,4 et 3,8 écarts types de lecture de la nocivité) | 1, 5, 6, 22 | lecteur | lot 1, § 2 |
| Kowalski, Fonseca Rivera, Macar, Africa, « Measuring Activation Control in Large Language Models », arXiv 2608.21664 v1 ; `…/lot7/2608.21664v1.pdf`, `7303ce0c3ad1d551…` | une consigne en langage naturel fait tomber la détection d'une sonde linéaire à 5-21 % à 1 % de faux positifs, sans optimisation ; consigne coopérative, concepts anodins, moniteurs non durcis (p. 7) | 4, 6, 7 | **auteur** | C9, § 3.6 |
| Jahed, Alouani, « Bypassing Prompt Injection Detectors through Evasive Injections », arXiv 2602.00750 v2 ; `…/lot7/2602.00750v2.pdf`, `cf0bd3653fdc8a1f…` | un suffixe ajouté au contenu évade cinq sondes à la fois (93,91 % et 99,63 %), avec le gradient (lecture des poids, sans écriture) | 1, 3, 4 | lecteur | C9, § 3.4 |
| Mohsin, Rahman, arXiv 2611.10620 v1 ; `…/lot7/2611.10620v1.pdf`, `2aa2fd973d5693a2…` | agents prévenus puis priés d'évader : rappel à seuil fixe de 0,87 à 0,55, aire sous la courbe presque inchangée, recalibrage qui rattrape l'essentiel ; **non opposable** (valeur de base sans ligne correspondante, lot 7-B, § 2.5) | 22 | agent qui agit, prié d'évader par consigne | lot 7-B |
| Daniels et collègues, « Stress-Testing Alignment Audits With Prompt-Level Strategic Deception », arXiv 2602.08877 v2 ; `…/lot7/2602.08877v2.pdf`, `cd1f2772d7b96bb6…` | par une consigne système seule, trouvée en 100 évaluations au plus, deux lectures internes du modèle cible sont trompées (succès de l'auditeur à 1 % et 1,8 %) ; **hors du périmètre strict** : pas de sonde de tromperie entraînée, consigne et non contenu écrit par l'agent | 4, 5, 14, 17, 18 | modèle cible, lectures non supervisées | lot 7-C, § 5 |
| Kale, Vishwanath, « Prompt-Injection Probes Learn the Conversation, Not Just the Injection », arXiv 2610.18408 v1 ; `…/lot3/2610.18408v1.pdf`, `411748554484dfb6…` | position dans la conversation et longueurs seules atteignent 0,91-0,98 d'aire sous la courbe ; la sonde suit la surface (voisin, versant lecteur) ; plan apparié déjà employé | 1, 4, 5, 12 | lecteur et victime | lot 3-A, § 7 |
| 2511.00554 v1 (`docs/sources/pdf/2511.00554v1.pdf`, `17708292f357ddee…`) ; 2601.11516 v4 (`c4a36db54c9d679a…`) ; 2509.21344 v2 (`aaac4ff91c909f9e…`) ; 2609.36490 v1 (`eb6d5bbe9bfaff0a…`) | évasions partielles par contenu de sondes du lecteur ; contre-indices déjà gardés au niveau 2 | 3, 6, 7, 11 ; 12-13 ; 1, 3, 5, 29 ; 5, 9, 17, 23 | lecteur | niveau 2, `anteriorite-v1.md`, l. 225-234 |

Lecture d'ensemble (C9, § 5) : HC2 reste non trouvée dans les pièces lues, **mais rendue moins probable**, surtout par 2608.21664, seule pièce opposable où la sonde lit le modèle auteur. Le même signe que la prédiction n'est publié que par MIRAGE, non opposable.

## 7. Ce qui ne change pas

- R1 à R14 ; HC1, HC3 à HC6 et leurs énoncés retenus (N-005, N-006, N-013) ; la porte GC.
- **HC2b** (« trahison par les activations ») : énoncé de N-013 inchangé. Le lot 1 (§ 3.2) propose d'ajouter Karne aux sources du contrôle du style : point attaché, section 8.
- Le bras « sonde du lecteur » de N-013 (l. 92) : gardé ; il devient l'une des trois positions proposées (section 5).
- La bascule pré-engagée « g_sonde > 0 → papier C sur la contamination de construit » (programme, l. 240) : inchangée ; elle se lit désormais sur la sonde de l'agent auteur.
- Le programme v2, non modifié : cette note en fixe la lecture.

## 8. Points attachés, non tranchés ici

- **HC4, lettre de N-013** (« le contexte seul n'y suffit pas ») : entamée par 2608.21664 (p. 6-7) et 2602.00750 (C9, § 3.4, 3.6) ; nœud distinct, porté par le complément 1 de la synthèse provisoire (section 4, point 4). Le lot 1 (§ 3.3) propose aussi de restreindre HC4 aux sondes de l'intention ou de l'action de l'agent auteur.
- **HC2b** : ajout de Karne (2609.05797, p. 6, 7) aux sources du contrôle du style (lot 1, § 3.2) ; du sosie inoffensif de 2610.18408 (p. 1, 4) et de la séparation exposition contre engagement de 2610.37679 (p. 1, 7) (lot 3-A, § 10.5) ; NARCBench, volet « Stego », voisin proche de HC2b (sondes sur les agents auteurs d'un contenu dissimulé ; billet du 3 avril 2026, lot 2-B, § 0.1).
- **Note de recentrage du papier C sur l'opposition juge contre sonde** (R-2555, option D) : l'énoncé resserré de HC2 en est une pièce ; la note devrait le reprendre une fois retenu.
- **Enregistrement public des pièces libres** (R-2555, option C) : HC2 y figure sous l'énoncé de la section 4, pas sous celui du niveau 2.

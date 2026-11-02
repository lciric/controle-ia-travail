# Proposition B — Boucle de sélection génération à génération de l'organisme d'idéation

---

## (a) Ce que la question suppose sans que ce soit établi

Chaque point reçoit un statut parmi ceux permis.

| # | Supposition implicite dans la question | Statut | Justification depuis les pièces |
|---|---|---|---|
| S1 | Le pont fiche→loi sera opérationnel pour la course 2 et produira un flux suffisant de fiches-lois testables. | **HYPOTHÈSE** | Pièce 7 §b.3 : parts attendues « SUPPOSÉ, à mesurer par le premier essai » ; sortie 1 estimée à 5–15 %, sortie 2 à 45–60 %. Le premier essai (D-P5) n'est pas lancé. 82 essais passent sur des modèles *factices* (pièce 8, réserve 1). |
| S2 | Les tests de mort sont activables et contribueront au filtre « survit au test de mort ». | **HYPOTHÈSE** | Pièce 1 §9.2 : codé v48–v56, **jamais activé**, machine jetable décidée mais non louée, bac à sable jugé non sûr par deux contre-lectures (CL13, CL14). |
| S3 | Le pôle a une puissance non nulle sur des données réelles (peut promouvoir un vrai signal). | **OBSERVÉ-NON-AUDITÉ** | Pièce 5 : « pas de dents » sur la banque réelle v2 (0 témoin vrai promu sur 20). Pièce 4 : 2 témoins vrais promus, mais dans un monde *tautologique*. Pièce 7 §a.4 : à 288 épisodes, meilleure richesse 2,28 pour un seuil de 3,0. La puissance sur données réelles n'est pas établie. |
| S4 | L'épreuve peut être renouvelée par génération (partie jamais vue disponible). | **HYPOTHÈSE** | Pièce 7 §a.4 : « l'épreuve de T0.5 est entièrement lue » ; ni la banque sœur, ni la couche 2, ni la couche 3 n'existent. D-P4 impose « fraîche seulement » pour tout usage décisif. |
| S5 | La recombinaison bisociative produit des filles à contenu empirique accru par rapport aux parents. | **OBSERVÉ-NON-AUDITÉ** | Pièce 6, démo cycle v5 : marchepieds +33 % dans un monde *planté* (fécondité par construction). Pièce 6, « ne dit pas » : rien sur un monde réel. |
| S6 | La mémoire anti-redite distingue des hypothèses sémantiquement proches mais empiriquement distinctes. | **HYPOTHÈSE** | Pièce 6 §C : 0 double sur 31, mais la garde est *textuelle* (pièce 6, « ne dit pas » : « ne reconnaît pas deux hypothèses de contrôle qui partagent le vocabulaire »). |
| S7 | La conjonction test-de-mort ∧ promotion-pôle est bien définie sur des fiches réelles. | **HYPOTHÈSE** | Aucune fiche réelle n'a traversé les deux filtres. Les tests de mort sont codés-non-activés (S2) ; le pôle n'a rien promu sur données réelles (S3). La conjonction n'a jamais été instanciée. |
| S8 | Les fiches de la course 2 seront suffisamment nombreuses pour qu'un contrôle de fausses découvertes (e-BH) ne tue pas toute la puissance. | **HYPOTHÈSE** | Pièce 1 §10 : 27 éligibles en course 1, 17 idées distinctes. Pièce 5 : la seule fiche passant le seuil par-fiche ne passe pas m/(α·k) avec m=88. Plus m est grand par rapport aux vrais signaux, plus e-BH pénalise. |
| S9 | L'ablation « avec vs sans filtre du pôle » est interprétable en une seule génération. | **HYPOTHÈSE** | La question suppose que la génération 2 suffit. Or la puissance de l'ablation dépend du nombre de fiches, qui est inconnu, et la durée d'une génération n'est pas bornée dans les pièces. |
| S10 | Il existe un critère opérationnel « neuve par rapport à H1–H9, HC1–HC5 ». | **HYPOTHÈSE** | Pièce 9 liste les hypothèses avec des probabilités d'originalité calibrées, mais aucun test mécanique de nouveauté par rapport à cet ensemble n'est décrit. La vérification d'antériorité (pièce 1 §1.2 étape 9) porte sur la littérature, pas sur la correspondance interne au programme. |

---

## (b) Expériences décisives — chacune en duel H_A / H_B (protocole B4)

### Expérience E1 — Le pôle a-t-il des dents sur des données non tautologiques ?

**Prérequis absolu** : toute la boucle génération-à-génération est sans objet si le pôle ne promeut jamais un vrai signal sur données réelles. C'est la question que la couche 1 a échoué à trancher (pièce 5 : « pas de dents »).

- **H_A** : Sur une banque d'épisodes réels contenant au moins un effet connu de force ≥ 0,5 (témoin vrai planté sur un moniteur réel), le juge figé promeut le témoin vrai sous la règle e-BH avec m ≤ 20.
- **H_B** : Le juge figé n'a pas la puissance de promouvoir un effet de force 0,5 à 288 épisodes sous e-BH avec m ≤ 20.
- **Métrique** : promotion (oui/non) du témoin vrai ; log-richesse W du témoin vrai au juge figé.
- **Seuil gelé** : log W ≥ log(m/α) avec α = 0,05, m = nombre de fiches jugées dans la génération.
- **Contrôle négatif** : ≥ 5 témoins faux (permutation intra-tâche, comme pièce 5) ; aucun ne doit être promu.
- **Issue qui falsifie H_A** : 0 témoin vrai promu sur ≥ 5 tentatives à 288 épisodes.
- **Issue qui falsifie H_B** : ≥ 1 témoin vrai promu, ≥ 5 témoins faux éliminés.
- **Condition matérielle** : exige une épreuve *fraîche* (non lue). Falsifie aussi S4 si aucune épreuve fraîche ne peut être construite à coût raisonnable.

### Expérience E2 — Le pont produit-il des lois testables sur des fiches réelles ?

- **H_A** : Sur 10 fiches réelles de la course 1 (tirées par session-depot, protocole de la pièce 7 §g), ≥ 1 sort en « loi testable sur banque existante ou couche 3 » (sortie 1 ou 2) avec accord des deux traductions aveugles.
- **H_B** : 0 fiche sur 10 sort en loi testable avec accord (toutes renvoyées N1–N11, ou désaccord N8).
- **Métrique** : nombre de fiches en sortie 1 ou 2 avec accord, sur 10.
- **Seuil gelé** : ≥ 1 (seuil bas, premier essai exploratoire).
- **Contrôle négatif** : 6 témoins du pont (T1–T6, pièce 7 §g) ; T3→N5, T4→N1, T5→N3, T6→N2 ou N9. ≥ 5 témoins sur 6 correctement classés.
- **Issue qui falsifie H_A** : 0 sortie (1 ou 2) avec accord, ou < 5 témoins justes sur 6.
- **Issue qui falsifie H_B** : ≥ 1 sortie avec accord et ≥ 5 témoins justes.
- **Coût** : ~1–4 dollars (SUPPOSÉ, pièce 7 §g), plafond 5 dollars. Ceci est l'essai D-P5.

### Expérience E3 — La conjonction test-de-mort ∧ pôle est-elle plus restrictive que chaque filtre seul ?

- **H_A** : La conjonction élimine *strictement plus* de fiches que le filtre le plus sévère seul. Formellement : |survivantes(TdM ∧ pôle)| < min(|survivantes(TdM)|, |survivantes(pôle)|) sur ≥ 1 génération de ≥ 10 fiches testables.
- **H_B** : Les deux filtres sont redondants sur les fiches de la course — toute fiche éliminée par l'un est aussi éliminée par l'autre (ce qui rendrait la conjonction inutile).
- **Métrique** : différence |survivantes(filtre seul)| − |survivantes(conjonction)| pour chaque filtre.
- **Seuil** : différence > 0 pour les deux filtres pris isolément.
- **Contrôle négatif** : témoins faux (fiches à effet nul, à prédiction non chiffrée) — doivent être éliminés par au moins un des deux filtres.
- **Issue qui falsifie H_A** : survivantes(conjonction) = survivantes(min), redondance.
- **Issue qui falsifie H_B** : ≥ 1 fiche survivant à l'un et éliminée par l'autre.
- **Condition** : exige que les tests de mort soient activés (S2 levée).

### Expérience E4 — Le renouvellement de l'épreuve empêche-t-il la fuite inter-génération ?

- **H_A** : Avec la *même* épreuve aux générations 1 et 2, les filles héritent une aptitude gonflée (richesse W médiane des filles > W médiane des mères sur l'épreuve partagée, mais pas sur une épreuve fraîche disjointe).
- **H_B** : L'aptitude des filles sur épreuve partagée n'est pas gonflée par rapport à une épreuve fraîche.
- **Métrique** : ratio W_fille(épreuve_partagée) / W_fille(épreuve_fraîche), médiane sur les filles promues.
- **Seuil** : ratio > 1,5 (illustratif — correspond à un biais substantiel).
- **Contrôle négatif** : ratio pour les mères (qui, elles, ont été jugées sur épreuve partagée) comme borne de comparaison.
- **Issue qui falsifie H_A** : ratio ≤ 1,5 sur ≥ 20 filles.
- **Issue qui falsifie H_B** : ratio > 1,5 sur ≥ 20 filles, confirmé par le fait que W_mère est aussi gonflé.
- **Condition matérielle** : exige deux épreuves disjointes. Réalisable en simulation (monde planté, pièce 6) avant données réelles.

### Expérience E5 — L'ablation du filtre du pôle à la génération 2

- **H_A** : Le filtre du pôle (juge figé) élimine des fausses bonnes fiches que les juges-modèles seuls laissent passer : le nombre de survivantes neuves par euro est *plus élevé* avec filtre qu'avec les seuls juges-modèles, sur au moins un axe.
- **H_B** : Le filtre du pôle n'élimine aucune fiche que les juges-modèles auraient gardée (coût pur sans gain de sélection).
- **Métrique** : survivantes_neuves / coût_total_en_euros, par bras (avec pôle / sans pôle).
- **Seuil** : ratio(avec) / ratio(sans) > 1,0 (le pôle doit au moins ne pas réduire le rendement).
- **Contrôle négatif** : témoins plantés (pièce 6) dans les deux bras ; le taux de fausses promotions ne doit pas être plus élevé avec pôle (la garantie à 5 % doit tenir).
- **Issue qui falsifie H_A** : ratio(avec) / ratio(sans) ≤ 1,0 et les témoins faux éliminés dans les deux bras.
- **Issue qui falsifie H_B** : ratio(avec) / ratio(sans) > 1,0, ou au moins un faux promu dans le bras sans pôle et 0 dans le bras avec.
- **Puissance** : avec 10 fiches par bras et un effet fort (50 % de reclassification), un test exact de Fisher bilatéral atteint ~60 % de puissance à α=0,05 (illustratif). Avec 20 fiches par bras, ~80 % (illustratif). Nécessite 2 × le coût d'une génération.

### Expérience E6 — La mémoire anti-redite distingue-t-elle les hypothèses proches-mais-distinctes ?

- **H_A** : La mémoire refuse une paraphrase d'une survivante mais accepte une hypothèse portant sur le même moniteur avec un effet de signe opposé.
- **H_B** : La garde textuelle confond les deux cas (refuse ou accepte les deux indistinctement).
- **Métrique** : taux de refus sur un ensemble de ≥ 10 paraphrases et ≥ 10 « opposées ».
- **Seuil** : refus paraphrases ≥ 0,8 *et* refus opposées ≤ 0,2 pour confirmer H_A.
- **Contrôle négatif** : fiches sur un moniteur entièrement différent → le refus doit être ≤ 0,1.
- **Issue qui falsifie H_A** : refus des opposées > 0,5, ou refus des paraphrases < 0,5.
- **Issue qui falsifie H_B** : refus paraphrases ≥ 0,8 et refus opposées ≤ 0,2.
- **Réalisable** : sur la banque synthétique, sans appel de modèle, coût processeur négligeable.

---

## (c) Mesure minimale de fonctionnement de chaque instrument nommé

### c.1 Le juge figé du pôle

- **Taux de détection minimal** : ≥ 1 témoin vrai promu sur 5 témoins vrais de force ≥ 0,5 (à 288 épisodes d'épreuve).
- **Taux de fausses alertes** : ≤ 1 témoin faux promu sur 20 (cohérent avec la garantie de 5 %).
- **Cas honnêtes appariés** : témoins faux construits par permutation intra-tâche (même distribution marginale, effet nul), comme dans la pièce 5.
- **Vérification mécanique à battre** : prédicteur aveugle (marginale, uniforme, urne — déjà dans la bibliothèque du pôle, pièce 7 §a.3). La richesse W du témoin vrai sous le juge figé doit dépasser le seuil log(m/α) ; la richesse de tout prédicteur aveugle sur les mêmes épisodes doit rester sous ce seuil.
- **État actuel** : VÉRIFIÉ en monde tautologique (pièce 4 : 2/2 vrais promus, 0/2 faux). **Non vérifié** sur données réelles (pièce 5 : 0/5 vrais promus).

### c.2 Les tests de mort

- **Taux de détection minimal** : ≥ 1 fiche à prédiction fausse « tuée » sur 5 fiches à prédiction fausse plantées (témoins faux explicites : la prédiction contredit les données).
- **Taux de fausses alertes** : ≤ 1 fiche à prédiction vraie tuée sur 5 (témoins vrais : la prédiction est mécaniquement confirmée par les données).
- **Cas honnêtes appariés** : même format, même coût en calcul, même structure — seul le seuil numérique distingue les vrais des faux.
- **Vérification mécanique** : la ligne `RESULTAT:` lue par le noyau et le verdict du lecteur neuf doivent coïncider sur 100 % des témoins. Un désaccord → « non concluant » (pièce 1 §9.2).
- **État actuel** : CODÉ, **jamais activé** (pièce 1 §9.2). Mesure minimale non effectuée.

### c.3 Le pont fiche→loi

- **Taux de détection (dents)** : ≥ 5 témoins du pont sur 6 correctement classés (T1, T2 retrouvés ; T3–T6 renvoyés aux bons codes N).
- **Taux de fausses alertes** : renvois de famille « pont » (N6–N11) ≤ 3 sur 10 fiches réelles (pièce 7 §g, critère L5).
- **Cas honnêtes appariés** : fiches réelles tirées au hasard (session-depot, graine engagée, pièce 7 §g) vs témoins construits.
- **Vérification mécanique** : la proposition compilée doit passer la vraie garde `proposeur.valider_proposition` du v56 (pièce 8 : 5 essais de compatibilité réussis sur banques synthétiques).
- **État actuel** : 82 essais sur modèles factices ; **aucun essai sur fiche réelle** (pièce 8, réserve 1).

### c.4 La mémoire anti-redite

- **Taux de détection** : ≥ 0,8 de refus sur des paraphrases de survivantes (pièce 6 §C : 20/31 refusées en mode héritage).
- **Taux de fausses alertes** : ≤ 0,1 de refus sur des fiches portant sur un domaine et un moniteur entièrement différents.
- **Cas honnêtes appariés** : fiches de domaines distincts vs paraphrases.
- **Vérification mécanique** : empreinte prédictive (la garde compare la loi, pas seulement le texte). La pièce 6, « ne dit pas », signale que la garde est textuelle — il faut vérifier si la signature sur la loi existe.
- **État actuel** : VÉRIFIÉ en simulation sur monde planté (0 double sur 31, pièce 6). **Non vérifié** sur fiches à vocabulaire partagé et effet distinct.

### c.5 La recombinaison bisociative

- **Taux de détection** : parmi les filles produites, ≥ 0,5 sont « vraies filles » (contenu empirique accru par rapport aux parents).
- **Vérification mécanique** : la loi fille doit prédire strictement plus que chacun de ses parents sur la sonde du développement (filtre mécanique, pièce 2 §1.8). La part de filles refusées par la garde prédictive doit être ≤ 10 (pièce 6 §A : 4–6 refusées sur ~25).
- **État actuel** : VÉRIFIÉ en monde planté avec vérité binaire (pièce 6 : 0,56–1,00). **Non vérifié** en monde réel.

---

## (d) Ancrage matériel

### Modèles ouverts

| Besoin | Modèle | Justification |
|---|---|---|
| Expérimentateur du pôle | Opus 5.5 (pièce 1 §1.3, lancements réels) | **VÉRIFIÉ** : 79 appels, 2,09 USD pour le lancement (a) bis |
| Vérificateur | Fable 5.1 (pièce 1 §1.3) | **VÉRIFIÉ** : 57 appels, 3,80 USD |
| Traducteur du pont | Opus 5.5 ou Kimi K3.1 Pro selon l'affectation croisée (pièce 7 §c) | **HYPOTHÈSE** : jamais testé sur fiches réelles |
| Proposeurs de la course 2 | Kimi K3.1 Pro + Argon (pièce 1 §1.3) | **RAPPORTÉ** |
| Juges-modèles de la course | Kimi + Argon croisés, Opus 5.5 en 3e (pièce 1 §6) | **RAPPORTÉ** |
| Modèle à poids ouverts (banque d'épisodes) | 8 milliards de paramètres (pièce 3) | **RAPPORTÉ** : couche 1 a tourné sur ses épisodes |

### Calcul nécessaire et coût

| Étape | Calcul | Coût estimé | Statut du coût |
|---|---|---|---|
| E1 — dents du pôle sur épreuve fraîche | Processeur seul, 1 génération ≤ 20 fiches | ~6 USD (illustratif, extrapolé du lancement (a) bis à 5,89 USD pour 12 fiches sur 2 générations) | **Illustratif** |
| E2 — premier essai du pont (D-P5) | 32 appels de modèle | 1–4 USD (SUPPOSÉ, pièce 7 §g), plafond 5 USD | **RAPPORTÉ** de la pièce 7 |
| E3 — conjonction TdM ∧ pôle | Machine jetable + processeur | ~6 USD (pôle, illustratif) + coût machine jetable (non chiffré dans les pièces) | **Illustratif** ; le coût machine est **absent des pièces** |
| E4 — fuite inter-génération (simulation) | Processeur seul, ~20 courses | ~1 minute par course (pièce 6 : 654–1 608 s pour 20 courses ; soit ~30–80 s par course) ; coût nul hors électricité | **Illustratif**, extrapolé de pièce 6 |
| E5 — ablation avec/sans pôle | 2 × le coût d'une génération complète de la course 2 + traduction + pôle | ~12–30 USD par bras (illustratif : course 1 ≈ 37 USD, pièce 1 §10 ; le pôle ajoute ~6 USD) | **Illustratif** |
| E6 — mémoire sur hypothèses proches | Processeur seul, pas d'appel de modèle | Négligeable | **Illustratif** |
| Épreuve fraîche (condition pour E1, E4 sur réel, E5) | Carte graphique pour produire de nouveaux épisodes du modèle 8B, ou banque sœur | Non chiffré dans les pièces ; la pièce 7 §a.4 mentionne « devis après » | **Absent des pièces** — c'est le nœud budgétaire |

### Le nœud de coût identifié

L'épreuve fraîche est la condition sine qua non pour que E1, E4 (sur réel) et E5 aient un sens. Sans elle, le pôle ne peut rien promouvoir de décisif (D-P4, pièce 7). Le coût de production d'épisodes neufs (carte graphique, annotation par juges) n'est pas chiffré dans les pièces servies. Ce coût conditionne toute la boucle génération-à-génération sur données réelles.

### Ordonnancement recommandé (du moins cher au plus cher, du prérequis vers le dépendant)

1. **E6** (mémoire, processeur, ~0 USD) → tranche immédiatement Q3 et S6.
2. **E4 en simulation** (fuite, processeur, ~0 USD) → tranche Q2 dans le monde planté.
3. **E2** (pont, ~1–4 USD) → tranche S1 et débloque la traduction.
4. **E1** (dents du pôle, ~6 USD) → tranche S3, mais **exige l'épreuve fraîche** (coût inconnu).
5. **E3** (conjonction, ~6 USD + machine jetable) → tranche S2 et S7.
6. **E5** (ablation, ~30–60 USD total) → tranche Q6 et S9, mais exige E1, E2, E3 résolus.

**Résumé du séquencement** : E6 et E4-simulation sont réalisables *maintenant* à coût nul. E2 coûte ≤ 5 USD et informe la viabilité du pont. E1 est le verrou : sans épreuve fraîche, la boucle génération-à-génération reste une construction sans preuve empirique de ses dents sur le réel.

---

### Note sur Q7 — Antériorités

La pièce 7 §i liste les systèmes les plus proches. Je n'harmonise ni ne résume cette liste ; je relève les lacunes :

- **POPPER** (Huang et al., 2025, référence à vérifier sur PDF) est identifié dans la pièce 7 comme « le plus proche » : e-valeurs séquentielles avec contrôle des fausses découvertes. Les questions ouvertes sur POPPER (séparation auteur/testeur, nul informé, témoins plantés, épreuve tirée après gel, renvoi motivé) ne sont pas tranchées dans les pièces. **Tant que cette lecture sur PDF n'est pas faite, la revendication de nouveauté de la boucle entière est une HYPOTHÈSE, pas un fait.**
- **MAP-Elites** et **novelty search** (cités dans Q3) : aucune pièce ne les mentionne ; référence à vérifier. La garde de diversité (Q5) pourrait reprendre le mécanisme de MAP-Elites (archive structurée par des descripteurs comportementaux). L'analogie est une HYPOTHÈSE.
- **Programmation génétique avec test** (citée dans Q7) : le mécanisme du pôle (sélection par aptitude = sévérité du test survécu, recombinaison, mémoire) est structurellement analogue à un algorithme évolutionnaire avec évaluation par test. La différence revendiquée — le juge statistique avec garantie de fausses promotions — est ce qui doit être vérifié par E1.

---

FIN-DE-CELLULE
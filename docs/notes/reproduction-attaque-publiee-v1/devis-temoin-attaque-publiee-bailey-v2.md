# Devis — témoin « attaque publiée reproduite » (test (a) de Bailey) — v2

10 novembre 2026, ≈ 08:00 UTC. Session « attaquant informé », mandat réduit. Aucune dépense, aucun lancement.

**Remplace**, pour le seul poste « test (a) de Bailey », la section 1 du devis v1
(`docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneur-protocelles-v1.md`,
`22c346011297a3b673ae33af9c29bafb2e029b6fc65b797a8ca93334c065a9f3`, R-896 ; la v1 reste archivée, R12). Les autres postes de la v1 (examen final,
malléabilité, collisionneur) ne sont pas touchés.

**Pièces** : préenregistrement `prereg/temoin-attaque-publiee-bailey-v1.md` ; relevé
`docs/notes/reproduction-attaque-publiee-v1/releve-depots-publics-bailey-strongreject-v1.md` ; autorisation existante
GO-2026-10-31-05 (`registres/go.md`, l. 170 : test (a), plafond 75 USD, échéance 14 novembre 2026, carte A100 80 Go,
préenregistrement scellé et contre-lu, arrêt par identifiant, pilote d'abord). Dépense imputée à ce poste à ce jour :
0 USD (`registres/depenses.md` : seules des lignes du poste « collisionneur » citent ce GO).

## 1. Ce qui change par rapport à la v1

| Point | v1 | v2 | Source |
|---|---|---|---|
| Carte | A100 40 Go | **A100 80 Go** | condition du GO ; `README` du dépôt public (relevé, section 1) |
| Juge de nuisance | 5 à 10 USD d'appels | **0 USD d'appels** : modèle local sur la carte louée ; compte en temps de carte | relevé, section 3 |
| Durée d'un tour | 10 à 20 minutes, 70 tours | **non mesurée** : fourchette 20 à 75 minutes ; le pilote la mesure, une règle gelée fixe le nombre de tours | sections 2 et 3 |
| Bras | non précisé | **un seul bras** : sonde à une couche cachée ; l'ensemble de sondes n'est pas couru | préenregistrement |
| Journal | non précisé | journaliseur local à écrire (le code public n'écrit que chez Weights & Biases) | relevé, section 1 |
| Modèle | « Llama-3-8B-Instruct », dit identique au nôtre | **modèle de l'article, qui n'est pas celui du programme** : GO de modèle exigé | relevé, section 2 |

## 2. Hypothèses de durée — aucune n'est mesurée

- Prix : A100 80 Go ≈ 1,08 USD par heure (relevé du 31 octobre, R-897 ; même taux sur la ligne de dépense du 9 novembre,
  « 13,69 h × 1,08 ») ; stockage ≈ 0,04 USD par heure (0,57 USD pour 13,69 heures, même ligne). **Taux retenu : 1,12 USD
  par heure**, à relever de nouveau à la création de l'instance ; la règle de la section 3 prend le taux réel.
- Un tour d'attaque et de défense comprend, selon la lecture du code public : 1 600 pas de gradient à travers le modèle
  (lots de un) ; deux évaluations sur 200 entrées nuisibles et 200 bénignes ; 400 générations de 300 jetons au plus (avec
  et sans suffixe) ; 200 notes du juge local ; le réajustement de la sonde.
- Seul repère publié : « 256 gradient steps (or about 10 minutes) » et « 16,384 gradient steps (about 10 hours on a
  single GPU) » (PDF `9c23a613…`, p. 26), soit ≈ 2,3 secondes par pas, **dans un autre montage** (section 6.2 de
  l'article, taille de lot non relevée). Appliqué tel quel : 61 minutes d'attaque par tour. À lots de un, le pas est
  probablement plus court.
- Fourchette retenue pour un tour entier : **20 à 75 minutes, valeur centrale 40 minutes**. C'est une estimation de ce
  rédacteur, pas une mesure.

## 3. Règle gelée du nombre de tours (reprise du préenregistrement)

Après la mise en place et le pilote (deux tours, dont on ne lit que la durée, la mémoire et l'état des gardes) :

- B : plafond du GO en vigueur pour ce poste ; R = 10 USD : réserve fixe ; D : dépense mesurée avant la boucle ;
  c : taux réel, carte et stockage ; t : durée moyenne d'un tour au pilote.
- Heures disponibles H = (B − R − D) / c. **Nombre de tours K = min(72, partie entière de H / (1,15 × t))**.
- K ≥ 71 : régime publié (« over 70 epochs », PDF p. 11). 20 ≤ K ≤ 70 : régime réduit, déclaré avant toute lecture.
  K < 20 : rien ne tourne, devis révisé soumis à Lazar.
- Une garde d'horloge arrête l'instance par son identifiant (R10) quand la dépense cumulée atteint B − 2 USD.

## 4. Postes

Au plafond existant, B = 75 USD.

| Poste | Attendu | Pire cas |
|---|---:|---:|
| Mise en place : installation, téléchargement du modèle (≈ 16 Go) et du juge, épreuve des gardes sur l'instance (2 h attendues, 4 h au pire) | 2,2 USD | 4,5 USD |
| Pilote : deux tours (1,3 h attendue, 2,5 h au pire) | 1,5 USD | 2,8 USD |
| Boucle principale : K tours | 37 à 61 USD selon t | borné par la règle |
| Contrôles du juge, transfert des journaux, destruction | 1,0 USD | 2,0 USD |
| Réserve fixe R (reprise technique, marge de facturation) | 0 à 10 USD | 10 USD |
| **Total** | **≈ 60 USD** | **75 USD (plafond dur)** |

Nombre de tours obtenu au plafond de 75 USD, avec D = 4 USD et c = 1,12 :

| Durée d'un tour au pilote | K | Régime | Coût de la boucle |
|---:|---:|---|---:|
| 20 minutes | 72 | publié | ≈ 27 USD |
| 40 minutes | 71 | publié, de justesse | ≈ 53 USD |
| 45 minutes | 63 | réduit | ≈ 53 USD |
| 60 minutes | 47 | réduit | ≈ 53 USD |
| 75 minutes | 37 | réduit | ≈ 52 USD |

**Lecture** : à 75 USD, le régime publié (plus de 70 tours) n'est atteint que si un tour dure 40 minutes ou moins. Pour
l'assurer jusqu'à 68 minutes par tour, il faudrait un plafond de 120 USD (72 × 1,15 × 1,14 h × 1,12 ≈ 106, plus réserve
et mise en place).

Processeur et sous-agents (code du journaliseur, de l'analyse et des gardes, contre-lectures) : 0 USD de calcul loué.

## 5. Nœuds pour Lazar — rien ne tourne sans ces mots

Ce sont des nœuds d'arrêt : pas de défaut à 48 heures.

1. **Modèle.** Décision : sur quel modèle court le témoin. Enjeu : l'article est sur Llama-3-8B-Instruct, le programme
   sur Llama-3.1-8B-Instruct ; « changer de modèle sans GO » est interdit.
   - (a) Modèle de l'article, pour ce seul témoin. Avantage : reproduction au régime publié, un échec accuse le banc et
     pas l'écart de modèle. Inconvénient : un modèle de plus dans le programme, à déclarer.
   - (b) Modèle du programme. Avantage : aucun modèle nouveau, effet lu « sur notre modèle ». Inconvénient : ce n'est
     plus une reproduction ; un échec ne se lit pas (banc ou modèle ?) ; nouveau préenregistrement.
   - (c) Les deux à la suite. Avantage : les deux lectures. Inconvénient : coût double, second devis.
   - Recommandation : **(a)**, puis (b) plus tard sur devis si le bras en a besoin. Confiance 0,65. Le préenregistrement
     v1 est écrit pour (a).
2. **Licence du code de Bailey.** Décision : sous quel titre on exécute un code public sans licence. Enjeu : sans
   licence, aucun droit de copie ni de modification n'est accordé.
   - (a) Exécution privée du code tel quel, à son commit, sans redistribution : aucun fichier du dépôt public n'entre
     dans le nôtre, nos ajouts (journaliseur, lanceur, analyse) vivent à part ; en parallèle, Lazar demande aux auteurs
     une licence ou un accord écrit (je rédige, Lazar envoie). Avantage : fidèle et rapide. Inconvénient : l'accord peut
     tarder ou manquer ; à dire dans tout écrit.
   - (b) Attendre l'accord écrit avant tout lancement. Avantage : net. Inconvénient : délai inconnu ; le GO échoit.
   - (c) Réécriture à partir de l'article seul. Avantage : aucun code tiers. Inconvénient : ce n'est plus le code
     publié, l'écart d'implémentation devient une explication de tout échec ; et c'est écrire un code d'attaque, ce que
     ce mandat évite.
   - Recommandation : **(a)**. Confiance 0,6.
3. **Autorisation.** GO-2026-10-31-05 échoit le 14 novembre. Restent avant le lancement : ces mots, le code du
   journaliseur, de l'analyse et des gardes, sa contre-lecture, puis 30 à 60 heures de carte. Le run ne tient pas avant
   le 14. Demande : **prolongation du poste « test (a) » jusqu'au 23 novembre**, plafond inchangé (75 USD), ou porté à
   120 USD si Lazar veut assurer le régime publié. Recommandation : prolonger à 75 USD, décider du plafond au vu de la
   durée du pilote. Confiance 0,7.
4. **Qui lance.** Ce conteneur n'a ni l'outil `vastai` ni clé. Soit Lazar ouvre l'accès à cette session, soit la
   session mère lance sur mon ordre scellé. Le modèle de l'article est à accès conditionné chez Hugging Face (licence de
   Meta à accepter par le compte).

## 6. Ce que ce devis ne contient pas

Aucun paramètre d'attaque, aucun résultat, aucune dépense engagée. Les durées sont des estimations non mesurées.

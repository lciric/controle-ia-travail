# Devis — témoin « attaque publiée reproduite » (test (a) de Bailey) — v3

10 novembre 2026, ≈ 08:05 UTC. Session « attaquant informé », mandat réduit. Aucune dépense, aucun lancement.

**Remplace la v2** (`devis-temoin-attaque-publiee-bailey-v2.md`,
`6a19b73039a7ffb0ce122f7257df3142e8c04c67fc61276102bda3dc8e5e1a4c`, archivée, R12), corrigée selon la contre-lecture
(`contre-lecture-prereg-temoin-bailey-v1-brouillon1.md`, `16f59a11bc977063788d265ede0da23a71583ae339139893f0c054ba9c99e7e2` :
CL-6, CL-7, CL-14 à CL-17, CL-29, CL-30). Comme la v2, elle remplace, pour le seul poste « test (a) de Bailey », la
section 1 du devis v1 (`docs/notes/anteriorite-P-041-v1/devis-P-041-gpu-et-collisionneur-protocelles-v1.md`,
`22c346011297a3b673ae33af9c29bafb2e029b6fc65b797a8ca93334c065a9f3`, R-896).

**Pièces** : préenregistrement, chemin prévu `prereg/temoin-attaque-publiee-bailey-v1.md` ; relevé
`releve-depots-publics-bailey-strongreject-v1.md` (`d804ad8e220e763f0bd8172caa64a68e71fc2a3627ad7b070932f5a0d0463fbe`) et
son erratum `erratum-releve-depots-publics-bailey-strongreject-v1.md` ; autorisation existante GO-2026-10-31-05
(`registres/go.md`, l. 170 : test (a), plafond 75 USD, échéance 14 novembre 2026, carte A100 80 Go, préenregistrement
scellé et contre-lu, arrêt par identifiant, pilote d'abord ; cette ligne cite le devis v1). Dépense imputée à ce poste à
ce jour : 0 USD (`registres/depenses.md`, l. 270, 285, 286 : poste « collisionneur » seulement).

## 1. Ce qui change par rapport à la v1

| Point | v1 | v3 | Source |
|---|---|---|---|
| Carte | A100 40 Go | **A100 80 Go** | condition du GO ; `README` du dépôt public |
| Mémoire vive de l'hôte | non dite | **au moins 128 Go** (estimation non mesurée : la banque de représentations croît à chaque tour) | erratum du relevé, point 8 |
| Juge de nuisance | 5 à 10 USD d'appels | **0 USD d'appels** : modèle local sur la carte louée | relevé, section 3 |
| Durée d'un tour | 10 à 20 minutes, 70 tours | **non mesurée**, fourchette 20 à 75 minutes, **croissante avec les tours** ; pilote, puis règle gelée | sections 2 et 3 |
| Bras | non précisé | **un seul** : une sonde à une couche cachée par couche lue ; l'ensemble de sondes n'est pas couru | préenregistrement |
| Journal | non précisé | journaliseur local substitué au lancement (le code public n'écrit que chez Weights & Biases) | erratum, point 5 |
| Modèle | dit identique au nôtre | **modèle de l'article, qui n'est pas celui du programme** | relevé, section 2 |

## 2. Hypothèses de durée — aucune n'est mesurée

- Prix : A100 80 Go ≈ 1,08 USD par heure (relevé du 31 octobre, R-897 ; même taux sur une ligne de dépense du
  9 novembre, `registres/depenses.md`, l. 413) ; stockage ≈ 0,04 USD par heure (0,57 USD pour 13,69 heures, même ligne).
  **Taux retenu : 1,12 USD par heure**, à relever de nouveau à la création de l'instance ; la règle prend le taux réel.
- Un tour comprend, selon la lecture du code public : 1 600 pas de gradient à travers le modèle ; deux évaluations sur
  200 entrées nuisibles et 200 bénignes ; 400 générations de 300 jetons au plus ; 200 notes du juge local ; le
  réajustement de la sonde sur une banque qui grandit à chaque tour.
- Seul repère publié : « 256 gradient steps (or about 10 minutes) » et « 16,384 gradient steps (about 10 hours on a
  single GPU) » (PDF `9c23a613…`, p. 26), soit ≈ 2,3 secondes par pas, dans un autre montage (section 6.2 de
  l'article). Appliqué tel quel : 61 minutes d'attaque seule par tour.
- Fourchette retenue pour un tour entier, en début de run : **20 à 75 minutes, valeur centrale 40 minutes**. Estimation
  de ce rédacteur. La valeur centrale suppose des pas nettement plus courts que le repère publié ; **c'est cette
  hypothèse qui décide du régime atteint à 75 USD.**
- **Croissance.** La durée d'un tour et la mémoire vive croissent avec les tours. La marge de 1,15 de la règle n'est pas
  mesurée ; si elle ne suffit pas, la garde de dépense arrête le run, lu alors sur les tours complets : un run prévu au
  régime publié peut finir au régime réduit.

## 3. Règle gelée du nombre de tours (reprise du préenregistrement)

- **B : plafond de la ligne de GO en vigueur pour ce poste à la création de l'instance. Il est cité dans l'ordre de
  lancement et ne change plus ensuite** : ni après le pilote, ni pendant le run.
- R = 10 USD : réserve fixe. D : dépense mesurée avant la boucle. c : taux réel, carte et stockage.
- Pilote : trois tours ; t : moyenne des durées des deux premiers (ceux qui comprennent un réajustement de la sonde).
- H = (B − R − D) / c. **K = min(72, partie entière de H / (1,15 × t))**.
- K ≥ 71 : régime publié. 20 ≤ K ≤ 70 : régime réduit, déclaré avant toute lecture. K < 20 : rien ne tourne, devis
  révisé soumis à Lazar.
- Une garde d'horloge arrête l'instance par son identifiant (R10) quand la dépense cumulée atteint B − 2 USD.

## 4. Postes

| Poste | Attendu | Pire cas |
|---|---:|---:|
| Mise en place : installation, téléchargement du modèle (≈ 16 Go) et du juge, gardes, contrôles du juge (2,5 h attendues, 4,5 h au pire) | 2,8 USD | 5,0 USD |
| Pilote : trois tours (2 h attendues, 3,8 h au pire) | 2,2 USD | 4,3 USD |
| Boucle principale : K tours | ≈ 27 à 52 USD selon t, hors croissance | borné par la règle et par la garde |
| Transfert des journaux, destruction | 0,5 USD | 1,0 USD |
| Réserve fixe R (croissance des tours, reprise technique, facturation) | 0 à 10 USD | 10 USD |
| **Total à B = 75 USD** | **≈ 60 à 70 USD** | **75 USD (plafond dur)** |

Nombre de tours obtenu, avec D = 5 USD et c = 1,12 (calculs refaits par programme ; coût de la boucle hors croissance) :

| Durée d'un tour au pilote | K à B = 75 | Régime | Boucle | K à B = 120 | Régime | Boucle |
|---:|---:|---|---:|---:|---|---:|
| 20 minutes | 72 | publié | ≈ 27 USD | 72 | publié | ≈ 27 USD |
| 30 minutes | 72 | publié | ≈ 40 USD | 72 | publié | ≈ 40 USD |
| 39 minutes | 71 | publié, de justesse | ≈ 52 USD | 72 | publié | ≈ 52 USD |
| 45 minutes | 62 | réduit | ≈ 52 USD | 72 | publié | ≈ 61 USD |
| 60 minutes | 46 | réduit | ≈ 52 USD | 72 | publié | ≈ 81 USD |
| 75 minutes | 37 | réduit | ≈ 52 USD | 65 | réduit | ≈ 91 USD |

**Lecture.** À 75 USD, le régime publié n'est prévu que si un tour dure 39 minutes ou moins au pilote ; à 120 USD,
jusqu'à 68 minutes. Un plafond plus haut ne coûte rien si les tours sont courts : K est borné à 72.

Processeur et sous-agents (code du journaliseur, du lanceur, de l'analyse et des gardes ; contre-lectures) : 0 USD de
calcul loué.

## 5. Nœuds pour Lazar — rien ne tourne sans ces mots

Nœuds d'arrêt : pas de défaut à 48 heures.

1. **Modèle.** Décision : sur quel modèle court la reproduction. Enjeu : l'article est sur Llama-3-8B-Instruct, le
   programme sur Llama-3.1-8B-Instruct ; « changer de modèle sans GO » est interdit.
   - (a) Modèle de l'article, pour ce seul run. Avantage : reproduction au régime publié ; un échec accuse notre
     exécution et pas l'écart de modèle. Inconvénient : un modèle de plus, à déclarer ; et ce run ne satisfait pas la
     définition du témoin dans la règle du jeu (« sur notre modèle et notre harnais ») : voir le nœud 5.
   - (b) Modèle du programme. Avantage : aucun modèle nouveau ; effet lu sur notre modèle. Inconvénient : ce n'est plus
     une reproduction ; un échec ne se lit pas (exécution ou modèle ?) ; préenregistrement nouveau.
   - (c) Les deux à la suite. Avantage : les deux lectures. Inconvénient : coût double, second devis.
   - Recommandation : **(a)**, puis (b) sur devis si le nœud 5 l'exige. Confiance 0,65. Le préenregistrement v1 est
     écrit pour (a).
2. **Licence du code de Bailey.** Décision : sous quel titre on exécute un code public sans licence. Enjeu : sans
   licence, aucun droit de copie ni de modification n'est accordé.
   - (a) Exécution privée du code à son commit, sans modifier ses fichiers ni les redistribuer : journaliseur substitué
     au lancement, surcharges de configuration déclarées, nos ajouts dans notre dépôt ; en parallèle, Lazar demande aux
     auteurs une licence ou un accord écrit (projet : `projet-courriel-auteurs-licence-v1.md`). Avantage : fidèle et
     rapide. Inconvénient : l'accord peut tarder ou manquer ; à dire dans tout écrit.
   - (b) Attendre l'accord écrit avant tout lancement. Avantage : net. Inconvénient : délai inconnu.
   - (c) Réécriture à partir de l'article seul. Avantage : aucun code tiers. Inconvénient : ce n'est plus le code
     publié ; et c'est écrire un code d'attaque, ce que ce mandat évite.
   - Recommandation : **(a)**. Confiance 0,6.
3. **Autorisation et plafond.** Décision : prolonger la ligne du test (a) et fixer son plafond, **avant le pilote**.
   Enjeu : GO-2026-10-31-05 échoit le 14 novembre et cite le devis v1 ; restent ces mots, le code et sa contre-lecture,
   puis 30 à 80 heures de carte : risque fort de ne pas tenir avant le 14 (estimation). Le plafond ne doit plus bouger
   une fois le pilote lancé, sinon le nombre de tours dépendrait d'une décision prise au vu d'une grandeur liée au
   résultat.
   - (a) Prolongation au 23 novembre, plafond 75 USD. Avantage : aucune dépense de plus que l'accordé. Inconvénient :
     régime réduit probable dès qu'un tour dépasse 39 minutes.
   - (b) Prolongation au 23 novembre, plafond 120 USD. Avantage : régime publié prévu jusqu'à 68 minutes par tour ; ne
     coûte que si les tours sont longs. Inconvénient : jusqu'à 45 USD de plus.
   - (c) Ni l'un ni l'autre : le témoin attend. Avantage : aucune dépense. Inconvénient : pas de témoin avant
     l'entretien.
   - Recommandation : **(b)**. Confiance 0,6. Dans tous les cas, la ligne nouvelle cite ce devis v3 et son empreinte.
4. **Qui lance.** Décision : quelle session crée l'instance. Enjeu : ce conteneur n'a ni l'outil `vastai` ni clé ; le
   modèle de l'article est à accès conditionné chez Hugging Face (licence de Meta à accepter par le compte) ; ouvrir un
   accès de compte est un nœud.
   - (a) La session mère lance, sur un ordre scellé écrit par cette session (commande, GO cité, gardes, identifiant
     d'instance consigné). Avantage : aucune clé nouvelle ; circuit déjà rodé. Inconvénient : dépend de la charge de la
     mère.
   - (b) Lazar ouvre à cette session l'accès à Vast.ai et à Hugging Face. Avantage : autonomie du bras. Inconvénient :
     des clés de plus dans un conteneur de plus.
   - Recommandation : **(a)**. Confiance 0,6.
5. **Ce que ce run vaut pour le témoin de la règle du jeu.** Décision : le verdict « effet reproduit sur le banc des
   auteurs » suffit-il au témoin « attaque publiée reproduite ». Enjeu : la règle du jeu (brouillon `09aa6403…`,
   section 3) le définit « à son régime, sur notre modèle et notre harnais » et fait sceller son critère avec la règle ;
   ce run est sur le modèle et le code des auteurs, et peut finir au régime réduit. Le préenregistrement ne tranche pas.
   - (a) Il suffit, au régime publié seulement. Avantage : critère net, fidèle à « à son régime ». Inconvénient : un
     régime réduit laisse le témoin ouvert.
   - (b) Il suffit, régime réduit compris, avec la réserve écrite. Avantage : un témoin lisible même si les tours sont
     longs. Inconvénient : plus faible que la règle telle qu'écrite.
   - (c) Il ne suffit pas : il valide notre exécution du code publié, et le témoin demande ensuite le même protocole
     sur Llama-3.1-8B-Instruct. Avantage : conforme à la lettre de la règle. Inconvénient : second run, second devis.
   - Recommandation : **(c) comme lecture, (a) en attendant** : dire à l'entretien « attaque publiée reproduite sur le
     banc des auteurs », et ne dire « sur notre modèle » qu'après le second run. Confiance 0,55. **À trancher avant la
     lecture des résultats**, et à écrire dans la règle du jeu quand elle sera scellée.

## 6. Ce que ce devis ne contient pas

Aucun paramètre d'attaque au-delà de deux constantes d'ordonnancement publiques, aucun résultat, aucune dépense
engagée. Les durées sont des estimations non mesurées.

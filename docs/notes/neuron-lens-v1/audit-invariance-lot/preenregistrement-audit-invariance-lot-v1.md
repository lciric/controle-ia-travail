# Préenregistrement — essai d'invariance au lot de l'ablation de `measure` sur une A100 SXM4 40 Go (audit R4) — v1

Écrit par la fille « Neuron Lens » le 2026-11-17, sur le mot de Lazar dans la session de la fille (« faut-il un audit de cette
identité ? … : go »). Écrit **avant toute course** de cet essai, contre-lu par un sous-agent neuf, scellé ; la dépense attend le feu de
la mère sur le devis du § 7.

## 1. Pourquoi (R4)
La lecture de la recourse (`lecture-recourse-b7/verdict-recourse-b7-v1.md`, `996744b2…`) trouve les séries aux lots 16 et 64 de la même
A100 **identiques au bit près** : fichier de `measure`, résumé de `score` et grandeurs ont les mêmes empreintes. Les journaux montrent deux
mesures complètes (`--ctx-batch 16`, puis `--ctx-batch 64` ; ablation en 682 s et 687 s), sans reprise d'un fichier partiel (le fichier
partiel est effacé en fin de mesure, l. 256 de la copie). Deux explications restent ouvertes : (A) le calcul de l'ablation est invariant
au lot sur cette carte et ces versions ; (B) quelque chose a rendu l'option sans effet dans la course. Un résultat trop propre déclenche
un audit (R4) ; c'est celui-ci.

## 2. Hypothèse et question
Sur une A100 SXM4 40 Go, avec les versions épinglées de la course (`requirements-neuron-lens-b-alpha-v1.txt` : torch 2.14.1,
transformers 5.18.0), Llama 3.1 8B Instruct en bf16 chargé comme `measure`, la **boucle d'ablation de `measure`** (copie publiée,
l. 213-235) rend, pour chaque tâche, une différence de log-softmax **identique au bit près** aux lots 16 et 64. Aucun signe n'est visé
(R3) : les deux issues sont lues à l'avance (§ 4).

## 3. Mesure (code : `src/controle_ia/neuron_lens/audit_invariance_lot_v1.py`, essayé sur un Llama miniature, 7 essais)
- **Tâches** : 64, tirées par `SeedSequence(20261117)` : séquence de jetons de longueur dans [24, 256] (le complément change d'une passe à
  l'autre), position ablatée = dernière position moins la fenêtre de 8, neurone tiré parmi les 14 336. Couches 0, 15 et 26.
- **Lots** : 16 (référence), 64 (décisif), 1 et 7 (rapportés).
- **Grandeur** : pour chaque tâche, l'empreinte sha256 du tenseur float32 de la différence propre − ablatée sur la fenêtre ; et, par lot,
  le nombre de tâches identiques au lot 16 et l'écart maximal en valeur absolue.
- **Témoins** : C1 formes des passes enregistrées (les lots 16 et 64 donnent des passes de formes différentes) ; C2 un jeton changé dans
  la tâche 0 change sa différence et aucune autre ; C3 le lot 16 rejoué donne les mêmes empreintes.
- **Écarts à la course, déclarés** : jetons tirés au hasard au lieu de documents du corpus (aucune table de la passe n'est refaite) ;
  `lm_head` sans le plafonnement de `arch.cap`, qui est l'identité pour Llama ; même chargement (`from_pretrained(…, dtype=bfloat16)`,
  attention par défaut de transformers 5.18.0, relevée dans le résultat).

## 4. Lecture, fixée avant la course (appliquée par programme, puis par un lecteur neuf)
| issue | condition | ce qu'on en tire |
|---|---|---|
| **indéterminé** | C1 ou C3 en défaut, ou C2 en défaut alors que le lot 64 est identique | l'essai ne dit rien ; rapporté ; aucune autre course sans mot de Lazar |
| **invariance établie** | C1, C2, C3 tenus et, aux trois couches, les 64 tâches du lot 64 identiques au lot 16 | explication (A) soutenue : l'identité de la course est attendue ; la réserve de la recourse devient « l'effet du lot est nul sur cette carte, par invariance du calcul » ; le cas sain (c) ne pouvait rien tester |
| **invariance réfutée** | C1 et C3 tenus, et au moins une tâche du lot 64 différente du lot 16 | explication (A) écartée pour ce calcul : l'identité de la course **n'est pas expliquée** ; divergence non résolue, portée à la mère ; la série au lot 64 de la recourse est **suspecte** et son verdict de B-7 ne remplace plus celui de la troisième course, jusqu'à décision de Lazar |
Les lots 1 et 7 sont rapportés sans critère.

## 5. Liste d'arrêt
Celle de la commande B-α v8 (carte autre qu'une A100 SXM4 40 Go : code 11 ; prix lu > 0,73 USD/h ; aucune ligne de l'amorce en 20 min ;
minuterie ou garde non armées ; refus d'une permission : arrêt, rien rejoué). Échec de l'étape `audit-invariance` : destruction, rapport,
aucune relance sans mot de la mère.

## 6. Ce qui n'est pas couvert
Un essai « invariance établie » montre que **ce calcul** est invariant au lot sur une A100 et ces versions ; il ne prouve pas que la
course a fait exactement ce calcul (elle l'a fait par le code voisin, sur les vraies tâches) ; c'est l'explication la plus simple,
non une preuve. La carte de l'essai n'est pas forcément la même machine que celle de la course.

## 7. Devis (ligne GO-2026-11-14-06 ; ≈ 3,4 à 4,0 USD déjà faits sur 12)
| poste | attendu | pire cas |
|---|---|---|
| montage, environnement, essais | 0,1 h | 2,2 h (pip sous `timeout`) |
| tokeniseur, poids de Llama | 0,1 h | 0,6 h |
| essai (3 couches × 4 lots + rejeu + perturbation, 64 tâches) | 0,1 à 0,3 h | 1,0 h |
| **total** | **≈ 0,3 à 0,5 h** | **≈ 3,8 h** |
| coût à ≈ 0,62 USD/h (relevé du jour) | **≈ 0,2 à 0,3 USD** | tronqué par la garde |
Garde de dépense v4 : **plafond 2 USD** (compte rendu à 1,20, arrêt dur à 1,80 ; ligne au pire ≈ 5,8 USD sur 12) ; minuterie = 90 % du
plafond au prix lu (≈ 2,5 h à 0,73). Une seule instance ; même filtre de carte et même prix lu exigé (≤ 0,73) que la commande v8 ;
destruction par identifiant, absence prouvée ; résultats sur une branche neuve `calcul/neuron-lens-audit-invariance-v1`.

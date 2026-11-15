# Préenregistrement — essai d'invariance au lot de l'ablation de `measure` sur une A100 SXM4 40 Go (audit R4) — v3

v3 = v2 (jamais jouée) corrigée selon sa seconde contre-lecture (`contre-lecture-audit-invariance-lot-v2.md` : trois majeures) : deux
issues positives distinctes ; carte contrôlée par l'étape et essayée dans les deux sens ; arrêt si ce préenregistrement manque sur la
machine. Module v3 (`audit_invariance_lot_v3.py`, 13 essais), amorce v3, dépôt réduit v12.

v2 = v1 (`preenregistrement-audit-invariance-lot-v1.md`, jamais joué) corrigée selon sa contre-lecture
(`contre-lecture-audit-invariance-lot-v1.md` : « à corriger », une bloquante, quatre majeures, huit mineures). Module v2
(`audit_invariance_lot_v2.py`, 12 essais), amorce v2, dépôt réduit v11.

Écrit par la fille « Neuron Lens » le 2026-11-17, sur le mot de Lazar dans la session de la fille (« faut-il un audit de cette
identité ? … : go »). Écrit **avant toute course** de cet essai, contre-lu par un sous-agent neuf, scellé ; la dépense attend le feu de
la mère sur le devis du § 7.

## 1. Pourquoi (R4)
La lecture de la recourse (`lecture-recourse-b7/verdict-recourse-b7-v1.md`, `996744b2…`) trouve les séries aux lots 16 et 64 de la même
A100 **identiques au bit près** : fichier de `measure`, résumé de `score` et grandeurs ont les mêmes empreintes. Les journaux montrent deux
mesures complètes (`--ctx-batch 16`, puis `--ctx-batch 64` ; ablation en 682 s et 687 s), sans reprise d'un fichier partiel (le fichier
partiel est effacé en fin de mesure, l. 256 de la copie d'origine, l. 264 après correctif). Deux explications restent ouvertes : (A) le calcul de l'ablation est invariant
au lot sur cette carte et ces versions ; (B) quelque chose a rendu l'option sans effet dans la course. Un résultat trop propre déclenche
un audit (R4) ; c'est celui-ci.

## 2. Hypothèse et question
Sur une A100 SXM4 40 Go, avec les versions épinglées de la course (`requirements-neuron-lens-b-alpha-v1.txt` : torch 2.14.1,
transformers 5.18.0), Llama 3.1 8B Instruct en bf16 chargé comme `measure`, la **boucle d'ablation de `measure`** (copie publiée,
l. 216-246) rend, pour chaque tâche, une différence de log-softmax **identique au bit près** aux lots 16 et 64. Aucun signe n'est visé
(R3) : les deux issues sont lues à l'avance (§ 4).

## 3. Mesure (code : `src/controle_ia/neuron_lens/audit_invariance_lot_v3.py`, essayé sur un Llama miniature, 13 essais)
- **Tâches** : 64, tirées par `SeedSequence(20261117)` : séquence de jetons de longueur dans [24, 256] (le complément change d'une passe à
  l'autre), position ablatée = dernière position moins 8 ; fenêtre de 9 positions (la position et les 8 suivantes, comme `measure`) ; neurone tiré parmi les 14 336. Couches 0, 15 et 26.
- **Lots** : 16 (référence), 64 (décisif), 1 et 7 (rapportés).
- **Grandeur** : pour chaque tâche, l'empreinte sha256 du tenseur float32 de la différence propre − ablatée sur la fenêtre ; et, par lot,
  le nombre de tâches identiques au lot 16, le même nombre après arrondi en demi-précision (la course range ses moyennes en demi-précision ;
  rapporté, non décisif), et l'écart maximal en valeur absolue.
- **Témoins, tous décisifs** : C1 formes des passes enregistrées (les lots 16 et 64 donnent des passes de formes différentes) ; C2 un jeton
  changé dans la tâche 0 change sa différence et aucune autre ; C3 le lot 16 rejoué donne les mêmes empreintes ; **C3b le lot 64 rejoué
  donne les mêmes empreintes** (sans lui, une instabilité aux seules grandes passes ferait conclure « réfutée » à tort) ; **C4 l'ablation
  agit** : la différence est non nulle pour au moins 90 % des tâches à chaque couche.
- **Témoin informatif** (non décisif) : un produit matriciel bf16 de 2 lignes et de 128 lignes, comparé sur ses 2 premières lignes.
- **Traçabilité** : le résultat de l'étape porte le chemin et l'empreinte de ce préenregistrement et la graine (`SeedSequence(20261117)`) ;
  le manifeste est celui de la machine du lanceur v5 (configuration B-α), déclaré.
- **Écarts à la course, déclarés** : jetons tirés au hasard au lieu de documents du corpus (aucune table de la passe n'est refaite) ;
  `lm_head` sans le plafonnement de `arch.cap`, qui est l'identité pour Llama ; même chargement (`from_pretrained(…, dtype=bfloat16)`,
  attention par défaut de transformers 5.18.0, relevée dans le résultat).

## 4. Lecture, fixée avant la course (appliquée par programme, puis par un lecteur neuf)
| issue | condition | ce qu'on en tire |
|---|---|---|
| **indéterminé** | C1, C2, C3, C3b ou C4 en défaut à une couche (tous exigés pour une issue décisive : choix prudent, déclaré ; un écart 16/64 avec un témoin en défaut est rapporté, sans issue) | l'essai ne dit rien ; rapporté ; aucune autre course sans mot de Lazar |
| **invariance établie** | témoins tenus et, aux trois couches, les 64 tâches des lots 64, 1 et 7 identiques au lot 16 | explication (A) soutenue, et le calcul est invariant au lot en général sur cette carte |
| **identité 16/64 établie, invariance non établie** | témoins tenus ; les 64 tâches du lot 64 identiques au lot 16 aux trois couches ; le lot 1 ou le lot 7 différent | explication (A) soutenue pour les lots 16 et 64 seulement (identité de la course attendue) ; l'invariance n'est pas générale ; rapporté |
| **invariance réfutée** | C1, C2, C3, C3b, C4 tenus, et au moins une tâche du lot 64 différente du lot 16 | explication (A) écartée pour ce calcul : l'identité de la course **n'est pas expliquée** ; divergence non résolue, portée à la mère ; la série au lot 64 de la recourse est **suspecte** et son verdict de B-7 ne remplace plus celui de la troisième course, jusqu'à décision de Lazar |
L'égalité en demi-précision et le produit matriciel sont rapportés sans critère ; les lots 1 et 7 départagent les deux issues positives.
Si ce préenregistrement manque sur la machine, l'étape s'arrête. L'étape s'arrête si la carte lue n'est
pas une « A100-SXM4-40GB ».

## 5. Liste d'arrêt
Celle de la commande B-α v8 (carte autre qu'une A100 SXM4 40 Go : code 11 ; prix lu > 0,73 USD/h ; aucune ligne de l'amorce en 20 min ;
minuterie ou garde non armées ; refus d'une permission : arrêt, rien rejoué). Échec de l'étape `audit-invariance` : destruction, rapport,
aucune relance sans mot de la mère.

## 6. Ce qui n'est pas couvert
Un essai « invariance établie » montre que **ce calcul** est invariant au lot sur une A100 et ces versions ; il ne prouve pas que la
course a fait exactement ce calcul (elle l'a fait par le code voisin, sur les vraies tâches) ; c'est l'explication la plus simple,
non une preuve. La carte de l'essai n'est pas forcément la même machine que celle de la course. L'étape de téléchargement du tokeniseur télécharge aussi les
trois lentilles de Neuronpedia (≈ 3 Go, sans lien avec l'essai, gardé pour réutiliser la machine du lanceur sans la modifier).

## 7. Devis (ligne GO-2026-11-14-06 ; ≈ 3,4 à 4,0 USD déjà faits sur 12)
| poste | attendu | pire cas |
|---|---|---|
| montage, environnement, essais | 0,15 à 0,2 h | 2,2 h (pip sous `timeout`) |
| tokeniseur, poids de Llama | 0,1 h | 0,6 h |
| essai (3 couches × 4 lots + deux rejeux + perturbation, 64 tâches ; ≈ 625 000 jetons) | 0,1 à 0,3 h | 1,0 h |
| **total** (échéances codées du module : 0,65 h attendu haut, 1,8 h au pire, hors pip) | **≈ 0,35 à 0,6 h** | **≈ 3,8 h** (inatteignable : la minuterie tombe à ≈ 2,5 h) |
| coût à ≈ 0,62 USD/h (relevé du jour ; 0,26 à 0,44 à 0,73) | **≈ 0,22 à 0,37 USD** | tronqué par la garde |
Garde de dépense v4 : **plafond 2 USD** (compte rendu à 1,20, arrêt dur à 1,80 ; ligne au pire ≈ 5,4 à 6,0 USD sur 12) ; minuterie = 90 % du
plafond au prix lu (≈ 2,5 h à 0,73). Une seule instance ; même filtre de carte et même prix lu exigé (≤ 0,73) que la commande v8 ;
destruction par identifiant, absence prouvée ; résultats sur une branche neuve `calcul/neuron-lens-audit-invariance-v1` ; identifiant de
course en `…-neuron-lens-audit-invariance`. L'écart de carte (A100 au lieu de la RTX 4090 de la ligne) est celui de GO-2026-11-17-04,
inscrit par la mère sur `main` (commit `83fe2c55`).

# Dossier de faits de la demande 1 — erratum 1 : quatre pièces de seconde main relues sur PDF, une précision, une ligne manquante

- 24 novembre 2026, vers 11:45 UTC (`date -u`). Auteur : Claude Fable 5.2, session du protocole X. Pièce de travail (classe C). Aucune dépense.
- Le dossier scellé (`dossier-faits-demande-1-v1.md`, `a6507835…`) n'est pas modifié. Cet erratum prime sur les points qu'il nomme. Il a été écrit **après** l'envoi à Carbon : Carbon a lu le dossier sans lui.
- Raison : la réponse de Carbon et la mienne s'appuient sur des pièces que le dossier marquait « reprises, non relues ce jour ». Elles sont relues ici à la page (règle de provenance, R7).

## 1. Soopal et al., « Stress-Testing Sandbagging Detection Under Adaptive Attack » (arXiv 2611.14950 v1, 11 novembre 2026)

Fichier `docs/sources/pdf/2611.14950v1.pdf`, empreinte `6396abd53a24b457…`. Pages relues : 1, 2, 6, 8.

- **Tenu.** Le dossier (D.10) dit qu'une sonde apprise contre le modèle de base signale 99 % des exemples d'adaptateurs bénins. Page 1 : « Activation probes also flag 99% of benign fine-tunes' examples ». Page 2 : « Activation probes trained against the base model detect fine-tuning rather than sandbagging: they flag 99% of benign adapters' examples ». Page 6 : la même sonde signale 99,0 % et 99,5 % des exemples de deux adaptateurs bénins.
- **À ajouter, que le dossier ne disait pas.** Le témoin bénin apparié répare le défaut dans une même course d'entraînement, et non d'une course à l'autre. Page 8 : « A matched benign adapter fixes this within a training run but not across runs: the probe passes our transfer rule in 1 of 5 folds, or 2 of 5 with three benign recipes. » Page 6 : la sonde apprise contre un témoin apparié, appliquée à trois nouvelles paires de graines, obtient des aires sous la courbe de 0,158, 0,128 et 0,489 ; avec cinq paires et une tenue à l'écart à tour de rôle, la règle de transfert des auteurs passe dans 1 pli sur 5 (2 sur 5 avec trois recettes bénignes, « still short of the 4 we required »), et le taux de fausses alertes sur des adaptateurs bénins tenus à l'écart atteint 65,5 %.
- **Cadre.** Petits modèles ouverts (Qwen 2.5 de trois milliards de paramètres ; une course sur Llama 3.2), problèmes de mathématiques à réponse exacte, sous-rendement conditionné à un marqueur d'audit dans la consigne. La transposition à une tâche difficile à noter est une question.
- **Conséquence pour les deux réponses.** « Fabriquer un ou deux adaptateurs bénins » (Carbon) et « un témoin bénin de même recette » (ma réponse) sont nécessaires et, selon la source même, ne suffisent pas : l'épreuve qui compte est le transfert vers des courses d'entraînement indépendantes, avec plusieurs recettes bénignes.

## 2. Boxo, Neelappa, Raval, « Linear probes rely on textual evidence » (arXiv 2509.21344 v2, 9 mars 2026)

Fichier `docs/sources/pdf/2509.21344v2.pdf`, empreinte `aaac4ff91c909f9e…`. Page relue : 1.

- **Tenu.** Page 1 : retirer du texte les indices du comportement fait baisser l'aire sous la courbe des sondes de 10 à 30 points ; sur des organismes qui ne verbalisent pas le comportement, 0,57 contre 0,74 (biais) et 0,57 contre 0,94 (sous-rendement). Les auteurs nomment deux fuites : celle de la consigne qui provoque le comportement, et celle du raisonnement à voix haute.

## 3. Taufeeque et al., « The Obfuscation Atlas » (arXiv 2602.15515 v2) : tableau 4 et page 8

Fichier `docs/sources/pdf/2602.15515v2.pdf`, empreinte `f6547ec830104abf…`. Pages relues : 7, 8, 17.

- **Tenu, avec une nuance à porter.** Page 7 : « fresh off-domain detectors generalize substantially worse after standard RLVR training » (tableau 4). Page 17 : les sondes de tromperie apprises hors du domaine perdent leur pouvoir de séparation, « while on-domain MBPP probes remain effective ». Page 7 encore : des sondes témoins apprises sur les modèles d'origine gardent une aire presque parfaite après l'entraînement, ce que les auteurs lisent comme une dérive propre à la tromperie et non générale. La dérive touche donc les sondes hors domaine ; les sondes du domaine tiennent.
- **Précision sur D.8.** Le dossier écrit que Llama-3-8B-Instruct s'effondre « sous forte pénalité ». La phrase exacte (à cheval sur les pages 7 et 8) : « At an extreme detector penalty coefficient (α = 100), the Gemma models achieve the highest honesty rates across both KL settings, while Llama-3-8B-Instruct collapses to degenerate policies, suggesting a model-dependent upper bound on useful detector strength ». L'effondrement est celui d'un entraînement **contre un détecteur**, à pénalité extrême. Il ne dit rien d'un entraînement sous supervision faible sans pénalité de détecteur.

## 4. Gan et al. (arXiv 2604.16286 v2)

Fichier `docs/sources/pdf/2604.16286v2.pdf`, empreinte `833a48e6c63b0e1b…`. Pages relues : 1, 7, 10.

- **Tenu.** Page 10 : « An AUROC of 0.77 provides some signal as a starting point for monitoring. The value might be too low to incriminate a misaligned model […]. It may provide enough signal to serve as a training signal […]. However, training may also teach models how to better conceal their sabotages ». Pages 1 et 7 : 0,77 est la meilleure aire sous la courbe d'auditeurs (modèles de langage, et personnes aidées par des modèles) sur des paires article et code sabotées ; ces auditeurs ne lisent aucun état interne.

## 5. Ligne manquante à la table F

La page 10 du papier de Terekhov et al. (« not validated quantitatively against human judges », citée en C.5) manque à la colonne des pages relues de la table F : elle a été relue ce jour par recherche de motif sur le fichier versé.

## 6. Ce qui reste non relu ce jour

Gasteiger et al. (mars 2025) : repris de la lecture du 20 novembre et de son erratum 1.

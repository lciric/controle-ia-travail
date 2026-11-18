# Diagnostic technique des erreurs de Carbon et d'Astra — course d'auto-conception v4 — v1

Écrit le 2026-11-18T21:29:57Z (`date -u`) par la session du compte organisme (modèle L), sur la demande de la mère (19:33Z) et le mot de Lazar tapé dans ce compte (choix « Extraction technique » : ce compte extrait par programme les seuls champs techniques, sans afficher ni verser de texte). **Aucun contenu de carte, de consigne ni de réponse de modèle n'est lu, cité ni versé ici.**

## 1. Sources

- Relevé des consommations de l'orchestrateur : `/home/user/sorties-course-auto-conception-v4/20261118-171908-course-auto-conception-v4/sortie/generation-1/consommations.json` (hors dépôt ; lu pour les champs `role`, `statut`, `duree_s`, `cout_usd`, `modele_servi`).
- Journal du relais de Carbon : `/home/user/execution-auto-conception-v2d/journal-relais-carbon.jsonl` (hors dépôt, **non versé** : il porte les réponses). Lu par le programme `extraire_champs_techniques_carbon_v1.py` (dossier de travail de la session), qui ne rend que des clés d'une liste blanche (`finishReason`, `modelVersion`, compteurs de jetons, états) et dont la valeur est un nombre ou un identifiant court ; toute autre valeur est remplacée par sa longueur.
- Code de la commande de Carbon : `commande_gemini_lot_v1.py` (`9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75`, copie de `main`), lignes 60-79 (options), 120-133 (lecture), 195-225 (garde après coup).
- Journal du relais d'Astra : `/home/user/execution-auto-conception-v2d/journal-relais-astra.jsonl` (champs techniques seulement).
- Les dossiers de session de l'orchestrateur sont **vides** : le dossier des sessions de la course (`/tmp/pole-sessions-v56-15_mzc8z`, dernière modification 19:30:13Z) a été vidé par l'orchestrateur à la fin ; les sorties d'erreur de la commande n'y sont plus.

## 2. Faits

| proposition de Carbon | lot au relais | jetons d'entrée | jetons de sortie | jetons de pensée | statut rendu |
|---|---|---|---|---|---|
| lot relevé 17:39:06Z | SUCCEEDED, 216 195 octets | 40 986 | 3 410 | **18 823** | erreur |
| lot relevé 17:49:07Z | SUCCEEDED, 20 999 octets | 28 791 | 2 202 | 0 (absent) | ok |
| lot relevé 18:36:10Z | SUCCEEDED, 204 485 octets | 34 062 | 3 231 | **17 454** | erreur |
| lot relevé 18:49:45Z | SUCCEEDED, 229 811 octets | 29 951 | 3 319 | **20 696** | erreur |
| cinquième lot | annulé (`annule_lot`) | — | — | — | erreur |

(L'ordre des quatre « erreur » au relevé des consommations : 733,6 s ; 1 523,3 s ; 428,9 s ; 490,5 s. La correspondance une à une avec les lots n'est pas nécessaire au diagnostic.) Aucun refus du relais ; 5 comptages de jetons, 5 créations de lot, 108 relevés « RUNNING », 4 « SUCCEEDED », 1 annulation.

## 3. Cause pour Carbon (établie)

1. **Trois erreurs = code 7 de la commande, « garde du plafond compromise : pensée … jetons > provision 8192 ».** La commande réserve `--provision-pensee-jetons` = 8 192 (défaut, ligne 69) et la demande au fournisseur comme budget de pensée (`thinkingConfig.thinkingBudget`, ligne 177). Le modèle a pensé 17 454 à 20 696 jetons, au-delà de ce budget. La garde après coup (lignes 208-219) refuse alors la réponse, à juste titre : le pire cas calculé avant l'envoi ne couvrait pas cette pensée. Le seul lot sans pensée est le seul réussi. **Le budget de pensée demandé n'est pas tenu par le fournisseur en mode lot** (fait observé ; la documentation du fournisseur n'est pas lue ici).
2. **Une erreur = code 6, délai** : le lot n'était pas fini à `--delai-s` = 1 500 s (défaut, ligne 73) ; la commande l'a annulé.
3. **Arrêt de Carbon après 5 propositions sur 11** : règle de l'orchestrateur sur les échecs répétés d'un rôle (non relue ici dans son code) ; l'étape « proposition » est alors non mesurée (C13).

Rien n'indique un défaut du relais, du mandataire ou du crédit. Le coût réel des trois lots refusés, calculé par la commande, reste sous le plafond par appel (≈ 1,1 à 1,3 USD chacun) ; l'orchestrateur a imputé environ 2 USD chacun.

## 4. Astra

Une erreur sur 11 : le relais a rendu 502 à 18:41:35Z, « amont coupé après envoi (dépense au pire cas) : ConnectionResetError », 30,016 s après l'envoi. Les dix autres appels d'Astra ont duré de 60 à 110 s environ sans incident. **Lecture : aléa de connexion**, non reproductible par ce diagnostic. Parade possible dans une version neuve : une seule reprise déclarée par appel d'Astra lorsque le relais rend 502 « amont coupé » (le relais impute déjà le pire cas, la dépense reste bornée) ; à défaut, aléa à accepter. Recommandation : la reprise unique déclarée, parce qu'une seule coupure suffit à rendre l'étape non mesurée.

## 5. Effet sur l'affinage v7

Les commandes v7 (`commandes-exactes-course-affinage-v7.md`, `e508db13…`, ligne 82) emploient la même commande de Carbon (`9484dce0…`) avec les mêmes réglages par défaut (pensée 8 192, délai 1 500 s). **Le même échec y est probable.** Même risque pour Astra (aucune reprise).

## 6. Correction minimale proposée (version neuve, contre-lue, avant tout départ)

- Carbon : `--provision-pensee-jetons 32768`, `--max-sortie-jetons 16384` (sorties observées ≈ 3 400 jetons), ce qui garde le pire cas d'un appel sous le plafond de 3 USD : 41 000 × 8,3 / 10⁶ + (16 384 + 32 768) × 41,5 / 10⁶ ≈ 0,34 + 2,04 = 2,38 USD ; `--delai-s` relevé (par exemple 3 000 s) avec le délai de commande de l'orchestrateur relevé d'autant ; devis recalculé.
- Astra : une reprise unique déclarée sur 502 « amont coupé ».
- Les mêmes réglages pour la tentative neuve de l'auto-conception et pour l'affinage (versions neuves des lanceurs, des commandes et des devis ; contre-lectures).

## 7. Ce qui n'est pas établi

- La correspondance exacte de chaque « erreur » de l'orchestrateur avec un lot (non nécessaire : trois codes 7 et un code 6 suivent des compteurs et de l'annulation).
- La règle exacte d'arrêt d'un rôle dans l'orchestrateur (non relue).
- Pourquoi le fournisseur dépasse le budget de pensée demandé en mode lot.

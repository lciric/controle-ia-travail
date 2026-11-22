# Devis v5 : questions « modes et attaques » v4, devis rejoué sous le moteur v8m

Écrit à 2026-11-22T16:43Z (`date -u`). Classe C. Session cloisonnée neuve (Opus 5.5), sur les mots de Lazar GO-2026-11-22-91 relayés par la mère. Le GO de dépense reste GO-2026-11-21-08 (48,13 USD au pire, échéance le 28 novembre). Ce devis complète la v4 (`devis-collisionneur-modes-et-attaques-v4-abonnement.md`, 2073265f…) sans l'écraser. Aucune course n'a eu lieu ; aucune sortie de modèle n'existe.

## 1. Questions v4 (option (a), « go »)
- `question-modes-sabotage-v4.md` : be588cb4753ac1382e23806726d3a1eee24763ab0b0e50448d3cdaa3ed4f7cdc, 8 063 caractères. Cinq renvois `docs/…` remplacés.
- `question-attaques-v4.md` : e3a61a56b055e697d8d2837aa5ed6ddb50b524ae226590e67ffe266fab4d2b17, 7 913 caractères. Quatre renvois remplacés.
- Les remplacements sont faits par programme, en remplacement exact ; rien d'autre ne change :

| renvoi | mot neutre |
|---|---|
| programme v2 | « programme de recherche, version 2 » |
| décision N-060 v3 | « décision du programme sur la vérité du dommage, version 3 » |
| décision N-054 | « décision du programme sur les modes de sabotage » |
| décision N-053 | « décision du programme sur les propositions de l'audit défensif » |
| décision N-056 | « décision du programme sur les bases et les bras d'attaque » |

- **Erratum de traçabilité** : le titre interne des deux v4 porte encore « — v3 ». Il est laissé tel quel selon la lettre de la consigne (« rien d'autre »). Le nom de fichier et l'empreinte font foi.
- La passation précédente donnait six et cinq « occurrences » de la garde. Le premier renvoi est compté deux fois : son chemin contient aussi « controle-ia ». Il y a donc cinq et quatre renvois.

## 2. Garde de motifs et contre-lecture
- **Garde du moteur** (`garder_motifs` du v8m, 420394f9…, par `epreuve-carbon-entree-neutre-v1/garde_questions_par_moteur_v8m_v1.py`) : aucun motif dans les deux v4.
- **Contre-lecture** par un agent Opus neuf qui ne les a pas écrites. **Verdict : ACCEPTÉ.**
  - Par un diff exact, seuls les renvois ont changé.
  - Les mots neutres sont fidèles aux pièces visées, et aucun code, identifiant ou chemin ne fuit.
  - L'agent a repassé lui-même la garde : aucune occurrence.
  - Il tient le titre « — v3 » pour acceptable, à consigner, ce que fait le point précédent.

## 3. Devis rejoué (commande `devis` du v8m, `--fable51 --argon --astra --carbon`, sans --sortie-max ni --effort-max, clés retirées de l'environnement)
- Calcul brut : `devis-brut-v8m-modes-sabotage-v2.txt` (c5c442c9…) et `devis-brut-v8m-attaques-v2.txt` (8fe7dbdb…).
- Étage III, au pire, par question : Argon 5,27 ; Carbon 7,25 ; Astra 2,11. Cela fait **14,63 USD par l'interface**, sans changement depuis la v4. Fable 5.1 est par l'abonnement : 8,26, non facturé. Seul écart avec les sorties brutes v1 : un centime à l'étage II, qui n'est pas joué.
- **Plafond de l'épreuve de Carbon, recalculé.** Le moteur refuse une seule espèce (code 1). Le pire cas de Carbon au tour III.1 est de 2,33 USD. Le plafond propre de 2,20 du mandat **ne tient donc pas**. Options, à trancher par Lazar (point 3, non tranché) :
  - (1) Carbon et Astra : pire cas 2,33 + 0,49 = 2,82, plafond 2,90.
  - (2) Carbon et Argon : pire cas 2,33 + 1,67 = 4,00, plafond 4,00.
  - (3) Pas d'épreuve.
- **Total au pire par l'interface** : 2 × 14,63 = 29,26. Avec l'épreuve, cela donne 32,16 (option 1), 33,26 (option 2) ou 29,26 (option 3). Tous ces totaux sont sous les 48,13 du GO. Le plafond par passage reste à 16 USD.
- **Longueur de l'entrée neutre de l'épreuve** : 7 989 caractères (b00803af…). Elle avait été taillée sur la plus longue question v3. La plus longue v4 en fait 8 063, soit 74 de plus. Le pire cas de Carbon au tour III.1 reste 2,33 dans les deux cas. Si Lazar veut l'égalité stricte, il faut un texte neutre v2.

## 4. Point 11 du devis v3, § 6 : option (b), mot de Lazar
- Les lecteurs qui jugent la réalité du dommage **sont des cibles** et restent dans les cibles de la question « attaques ». Le fait 4 de la v4 les y range déjà. Aucune modification n'est demandée.
- Toute fiche d'une attaque contre ces lecteurs ne va qu'au gardien du coffre jusqu'à l'évaluation, jamais au concepteur de l'instrument de vérité du dommage. Cette clause entre dans la règle d'ouverture du coffre, à écrire avant toute poussée sur la branche du coffre (mandat, § 3), et dans le mandat du trieur (mandat, § 7).

## 5. Textes qui supposent ces lecteurs sûrs (à revoir : nœud pour Lazar)
Relevé de l'agent de contre-lecture et de la session. Rien n'est réécrit ici, car la consigne des v4 l'interdit.
- **Question « modes de sabotage » v4, fait 6** : la vérité du dommage y est présentée comme ce qui dit que le dommage a eu lieu, et les deux lecteurs comme un instrument fiable, sans réserve d'attaque.
- **Même question, rubrique 5 du gabarit** (« ce qui demande un lecteur ») et critère de classement « solidité de la vérité du dommage » : le lecteur y est traité comme un recours sûr.
- **Mandat de la session cloisonnée, § 7, et devis v3, § 5, point 5** : seul le concepteur de l'instrument est exclu ; rien n'y dit que les fiches d'attaque contre les lecteurs sont retenues au coffre.

Options :
- (a) Une question « modes de sabotage » v5 avec une phrase de réserve au fait 6 (« ces lecteurs peuvent eux-mêmes être visés ; leur sûreté n'est pas supposée »), contre-lue et regardée par la garde.
- (b) Garder la v4 telle quelle et porter la réserve seulement dans le mandat du trieur et la règle d'ouverture du coffre.

Recommandation : (a), confiance moyenne. La question « modes » ne demande pas d'attaque, mais sa rubrique 5 fait concevoir des vérités du dommage qui reposent sur des lecteurs tenus pour sûrs.

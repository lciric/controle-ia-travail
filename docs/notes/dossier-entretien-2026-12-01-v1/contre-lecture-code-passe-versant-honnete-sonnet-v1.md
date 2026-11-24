# Contre-lecture du code de la passe et de la préparation du versant honnête (classe B) — Sonnet, v1

Attestation : 2026-11-24, 17:20Z à environ 18:15Z (`date -u`). Contre-lecteur neuf. Je n'ai lu aucun épisode, score, sortie de course, diagnostic, verdict ni lecture ; rien sous coffre/, registres/, diag/, runs/, donnees/. Données factices seulement. Aucun fichier du dépôt modifié.

Pièces (empreintes lues) : passe 2eaf97e0, préparation deaee441, essais 838bda0e, aide 4f01d252. 45 essais : 45 passés (74 s).

Verdict : **conforme sous corrections** (un défaut du code d'analyse scellé, un de la passe, des trous d'essais).

## Défauts
1. **Élevée — code d'analyse v6 scellé (8e074634), `controler_comptes` ligne 442, et lignes 370 et 436.** Un score existant manquant arrête toute la lecture, alors que le texte ne fait du pont qu'une réserve. Éprouvé sur données factices : une ligne existante absente donne l'arrêt « incomplets… pont incalculable » ; un score existant null donne « score de sonde manquant » ; un NaN donne « valeur non finie » ; seuls tous les existants absents donnent la réserve « pont non calculé ». La préparation écrit `float(v)` sans filtre (NaN devient `NaN` en JSON). Scénario : une seule action sans score existant dans les 640 tue une lecture déjà payée. Correction minimale (v7, avec contre-lecture) : pour la source « existant », accepter null et NaN comme « absent » ; supprimer l'arrêt de la ligne 442 ; faire calculer `pont` sur les actions à écart fini, avec leur nombre, et la réserve « pont partiel » (« non calculé » si aucune) ; la préparation écrit null pour un NaN ; essais sain et artefact.
2. **Moyenne — passe, `relire` (scores None) et bordereau.** Une action sans jeton noté (jeton de fin seul) reçoit un score null ; le code d'analyse s'arrête alors (« toute action a un score de sonde »). Le défaut n'apparaît qu'après la dépense. Correction : compter à l'entrée, avant le chargement du modèle (identifiants réduits à un jeton de fin), et arrêter ou renvoyer en nœud là, avant toute dépense.
3. **Faible — essais.** Mutations survivantes : jeton de fin inclus dans l'empan noté (S2) ; contrôle négatif de la garde d'équivalence retiré (G2) ; tirage avec remise (T2) ; source du juge non vérifiée en préparation (R1) ; scores existants hors confirmation (R3). Les mutations de l'auteur neutralisent des gardes entières, jamais leurs sous-contrôles. Ajouter un artefact par sous-contrôle. G8 (écrasement d'un fichier) et F2 (comptes d'actions) sont équivalentes, car doublées en amont.
4. **Faible — mémoire.** Les captures des actions de garde restent en mémoire, au plus environ 3,8 Go (192 × 400 jetons × 3 couches × 4096 × 4 octets). À inscrire à la barrière de dépense.

## Réponses
1. Conforme au point 5 : passe unique par épisode, couches 7, 15, 23, arrondi en demi-précision, score w·h+b puis maximum, jeton de fin exclu, 192 actions (160 + 32) sous `garde-1/tirage` (entropie égale au texte), garde de l'équivalence à q99 avec contrôle négatif, pont dans le mode des scores existants.
2. Aucune activation brute n'est écrite sur disque ; seuls scores, index, actions de garde (identifiants, écarts), trace et bordereau le sont. Le lot lourd de l'ordre est donc vide.
3. Format des scores égal à celui du code v6 ; refus d'écraser (R12), aucune suppression ; trace d'arrêt sans score.
4. Préparation : conventions de graine (clé du manifeste puis `graine_entiere`), d'empreinte de texte (sha256 des textes du pas) et de juges (source « etalonnage », condition honnête) cohérentes avec v6.
5. Clé `passe/ordre-des-lots` : acceptable, consignée, sans effet numérique. Le q99 sur contexte et zone générée dilue la zone ; le contrôle négatif de zone compense ; c'est la garde de la course, reprise telle quelle. Minimum de 10 actions : repris de la configuration. 3 × 192 relectures pour le contexte : moins coûteux que 960, avec 192 passes de répétabilité par épisode ; acceptable. Action sans jeton noté : défaut 2.
6. Oui : défaut 1.
7. Mutations propres : 19 ; 12 tuées, 7 survivantes (défaut 3).

Qui a lu quoi : les deux modules en entier, les essais (noms et fixtures), le texte scellé v3 (point 5), l'ordre, sa contre-lecture et le devis (extraits), v6 (extraits) ; aucune donnée du programme.

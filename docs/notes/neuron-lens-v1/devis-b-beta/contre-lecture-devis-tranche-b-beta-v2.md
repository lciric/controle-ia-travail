# Contre-lecture du devis de la tranche B-β (v2) — lecteur neuf (R2)

Pièce lue : `devis-tranche-b-beta-v2.md` (empreinte vérifiée : `abc7b727…`, conforme au compagnon). Lu aussi : v1 et sa contre-lecture, relevé `1a7cc32c…`,
plans v1 (§ 4, § 5.3, § 5.4, § 7) et v2 (§ 0, § 3.2 à 3.4), devis B-α v2 (§ 3), journaux B-α v1 à v3, banc `fit_bench_h100_2026-10-28.log`,
`02_fit.py` et `neuron_lens/transport.py` du dépôt voisin (lecture seule, commit `849bfe16`, empreinte de `02_fit.py` identique à la copie du dépôt),
minuterie v4, garde de dépense v4, `registres/go.md` de `main`. Rien exécuté du dépôt voisin, aucune commande du loueur, aucun secret lu.

**Verdict : à corriger.** Les 16 points de la v1 sont repris et l'arithmétique est exacte ; le retrait du repli est cohérent. Restent trois défauts
nouveaux de fond (taille réelle des ajustements, point de sauvegarde perdu avec la machine, sortie des lentilles non chiffrée) et des erreurs de détail.
Aucune bloquante.

## (a) Reprise point par point
| point | verdict |
|---|---|
| B1 (pire cas hors H100 SXM, repli contre minuterie) | **Corrigé, justement.** PCIe et A100 retirées, « aucun repli », cohérent avec § 3, § 5 (minuterie, `CARTE_ATTENDUE`), § 6 et § 7. Un défaut de détail de comptage (m-1 ci-dessous). |
| M1 dérivation de B1 | **Corrigé.** Recalculé : 2 000 × 11,22 à 11,78 s = 6,23 à 6,54 h (« 6,2 à 6,6 ») ; × 0,9 à 1,2 = 5,6 à 7,9 h ; pire cas 2 000 × 23,6 s = 13,1 h. Le banc (R 11,22 à 11,75 s ; S 11,54 à 11,78 s, deux cibles par document, `fit_bench.py` l. 79) soutient les bornes. |
| M2 gardes | **Corrigé** (comparé ligne à ligne au devis B-α v2 § 3 : ligne de GO, échéance, 60 %, 90 %, minuterie, bornes en durée, rappel à 80 %, crédit, course figée, une seule instance, destruction, intouchables). Ajout bienvenu : crédit couvrant le plafond. Le témoin `--temoin` est remplacé par `--non-vide`, conforme à la minuterie v4. |
| M3 condition de passage | **Corrigé.** Plan v2 § 3.2 respecté ; l'état de B-α est dit. |
| M4 essais impossibles ici | **Corrigé** : essais sur la machine à B0, pire cas 3 h. |
| M5 passe et `measure` refaits | **Corrigé quant au motif** (tables détruites). Deux scories : m-3, m-4. |
| M6 écart au plan v2 | **Corrigé** (colonne « plan v2 », phrase d'écart : 24,6 − 21,2 = 3,4 h exact ; 62,7 contre 63,6 USD). |
| m1 à m4 | **Corrigés** : 7 offres A100 40 Go (3 SXM4 + 4 PCIe) ; trafics NVL 0 à 0,0365 et RTX 6000 Ada 0,0026 à 0,0143 ; filtre identique à l'en-tête du relevé ; prix avec 200 Go de stockage (2,1076 → 2,144 ; 4,6421 → 4,828 ; 4,8433 → 5,025 ; 2,3482 → 2,414 à 730 h par mois : les « ≈ 2,145 ; 4,83 ; 5,03 ; 2,415 » sont justes). Sauf le comptage m-1. |
| m5 option (c) | **Corrigé** : plafond ≈ 53 USD = 48 / 0,9 ; honnêtement laissé « à recalculer ». |
| m6 limite de l'hébergeur | **Corrigé** : un chiffre (100 Mo, non revérifié) ; la marge de 95 Mo est bien dans l'amorce v6 (`LIMITE=$((95*1024*1024))`). |
| m7 préalable 2 | **Corrigé** : `16957c52…` et `2fa015e4…` sont bien aux addenda v1 et v2 ; ce qui manque est dit. |
| m8 10 Go et 30 Go | **Corrigé en forme** (estimation avec calcul), **mais le calcul est faux** : voir Majeure 1. |
| m9 moitiés | **Corrigé quant au fond** (voir (d)) ; la citation de lignes est fausse (m-2). |
| question 4 (lieu) | **Corrigé** : options chiffrées, condition de la commande. Voir Majeures 1 et 3 pour les chiffres. |
| question 5 (GO introuvable) | **Résolu** : `GO-2026-11-17-03` (R-3046, « b puis c ») et `-04` figurent bien dans `registres/go.md` de `main` (l. 360-361). La réponse du § 8 est exacte. |

## (b) Recalculs
- Heures attendues : 0,5+5,6+1,0+0,3+0,5+0,5 = 8,4 ; 1+7,9+1,5+0,5+0,8+0,8 = 12,5. Juste. Pire cas : 3+13,1+2,5+1+1,5+1,5+1+1 = 24,6. Juste.
- Carte : 8,4 × 2,145 = 18,0 ; 12,5 × 2,145 = 26,8 (« 18 à 27 ») ; total 18 à 28 avec 1,2 de trafic : juste. Pire cas 24,6 × 2,55 = 62,73 ; + 1,2 = 63,9 (« ≈ 64 ») : juste.
- 60 % de 68 = 40,8 ; 90 % = 61,2 ; dépassement 63,9 − 61,2 = 2,7 (« ≈ 2,8 » : arrondi acceptable) ; troncature 61,2 / 2,55 = 24,0 h, moins 1,2 / 2,55 = 0,47 h → 23,5 h : juste.
- Prix exigé pour tenir : (61,2 − 1,2) / 24,6 = 2,439 → « ≤ 2,44 » juste ; sans trafic 2,488. Plafond équivalent 63,9 / 0,9 = 71 (« ≈ 72 ») : juste, un peu large.
- Minuterie : 61,2 / 2,55 × 3 600 = 86 400 s ; à 2,15 : 102 474 s ; borne 129 600 s = 36 h → 61,2 / 36 = 1,70 USD/h. Tout juste (essai numérique, `minuterie_s` rend bien 86 400).
- Option (a) : 2,145 × 24,6 = 52,8 USD au prix du jour, donc la troncature ne vaut qu'au voisinage de 2,55.
- Écart au plan v2 : 8,4 à 12,5 h contre 8,8 à 11,5 : conforme à « attendu presque égal ».

## (c) Cohérence du retrait de tout repli
Cohérent : § 3 (retrait motivé), § 5 (minuterie bornée, prix ≥ 1,70 refusé par la borne, `CARTE_ATTENDUE`), § 6, § 7 (a) et (b), § 8. Deux nuances : (i) § 5 l. 117 « prix lu ≥ 1,70 … tenu par la carte exigée » n'est pas une garantie : une H100 SXM sous 1,70 serait refusée (échec fermé), ce qui est sain mais s'écrit « refusée », pas « tenu » ; (ii) le rappel « pire cas à 24,6 h » (l. 118) est postérieur à la minuterie de 24,0 h au prix exigé de 2,55 : il ne sert qu'aux prix plus bas.
Observation de fond : le prix exigé de 2,55 n'a plus sa raison d'être (celle de la v1 était « le pire cas tient sous l'arrêt dur » : 60,4 < 61,2 ; avec 24,6 h cela ne tient plus). Or une seule offre existe (≈ 2,145), qui tient aussi à 2,44. Recommander (b) ne coûte donc rien au relevé du jour et supprime la troncature déclarée. À dire.

## (d) « Les deux moitiés en un seul passage »
**Exacte au code.** `02_fit.py` l. 4-8 (docstring), l. 168-177 : une boucle unique sur les documents, `lens_doc(…, acc, i % 2, …)` à la l. 173 ; `Accumulator` (`transport.py` l. 49-57) tient `sums[(cible, moitié)]` pour deux moitiés et deux cibles ; `split_half` est calculé à la fin sans second passage. Le banc mesure bien les deux cibles par document. **Mais** la citation du devis (« l. 4-8 et 98-120 de la copie ») est fausse pour la seconde : les l. 98-122 sont `media_doc` (images et sons). À écrire : l. 168-177 de `02_fit.py` et l. 49-57 de `transport.py`.

## (e) Taille des lentilles et trafic
- **Taille : sous-estimée** (Majeure 1). Le devis compte « une lentille par couche, ≈ 2 Gio ». Le code : une lentille a **deux cibles** (R : `out` 31 couches, `mid` 32 ; S : `mid`, `out` 32 + 32), et le point de sauvegarde garde **les deux moitiés** en float32 : R = (31+32) × 2 × 64 Mio = 7,9 Gio ; S = 8,0 Gio ; **≈ 16 Gio (17 Go) pour les deux fichiers**. Source dans `02_fit.py` l. 9-10 : « Qwen3-8B : 9,5 Go pour R et 9,7 Go pour S, chacune à deux cibles » ; la formule redonne 9,5 Go pour Qwen3-8B (71 couches × 2 × 64 Mio), donc elle est juste pour Llama (≈ 8,5 et 8,6 Go). La moyenne seule (sans moitiés) fait ≈ 4 Gio par lentille, ≈ 8 Gio pour deux. Or B-1 (stabilité) et toute reprise exigent les moitiés. La fourchette « 2 à 10 Go » est donc trop basse en haut ; il faut « ≈ 8 à 17 Go », avec la formule et la source.
- **`-causal.pt` ≈ 2 Go** : le devis B-α v2 (§ 4, M6) donne ≈ 2,9 Go pour Qwen3-8B ; pour Llama (32 couches) ≈ 2,6 Go. « ≈ 2 Go » n'est pas sourcé.
- **Trafic ≈ 30 Go** : poids ≈ 16 Go juste (8 milliards de paramètres en demi-précision). « Lentilles de Neuronpedia ≈ 6 Go » : le plan v2 § 2 donne 1,04 Go par fichier, soit ≈ 3,1 Go pour J, J++ et R ; 6 Go n'est pas sourcé (surestimation sans conséquence). « Environnement ≈ 5 Go » non sourcé (B-α a mesuré ≈ 5 Go de trafic **au total**, journal v1 l. 23). À l'offre retenue le trafic est nul : le 1,2 USD du pire cas n'a de sens qu'à 0,04 USD/Go.

## Bloquantes
Aucune.

## Majeures
**1. Taille des lentilles ajustées sous-estimée** (v2 l. 44-47 ; aussi l. 49-51, 143). Écrit : « de 2 à 10 Go … une lentille par côté en compte une par couche lue, soit ≈ 2 Gio, davantage avec les accumulateurs des moitiés ». Devrait être écrit : deux cibles par lentille ; fichiers d'ajustement ≈ 7,9 Gio (R) + 8,0 Gio (S) ≈ 16 Gio, moyennes seules ≈ 8 Gio ; source `02_fit.py` l. 9-10. Conséquences à reporter : coût mensuel de l'option (b), temps de copie de l'option (c), disque transitoire (écriture `.tmp` puis remplacement : +8 Gio le temps d'un point de sauvegarde).

**2. Le point de sauvegarde ne survit pas à la perte de la machine** (v2 l. 15-17, l. 93). Écrit : « reprise sur point de sauvegarde », « une machine perdue et remontée : 1 h ». Le point de sauvegarde est un fichier de ≈ 8 Gio sur le disque de l'instance (`02_fit.py` l. 150-156), qu'on ne peut pas pousser vers l'hébergeur de code (100 Mo) ; avec l'option (a) du lieu, aucune copie n'existe. Une machine perdue en cours de B1 perd jusqu'à 13 h d'ajustement (≈ 28 USD), pas 1 h, et le plafond de 68 USD n'y suffit alors pas. La reprise de 1 h ne vaut que pour un redémarrage de processus sur la même instance. Devrait être écrit : cette distinction, un pire cas « perte de machine pendant B1 » chiffré (ou déclaré hors plafond, avec arrêt et nœud), ou un envoi périodique du point de sauvegarde vers le lieu des lentilles (alors condition de la commande). Même sujet, coût non compté : chaque sauvegarde toutes les 10 minutes recopie ≈ 8 Gio du GPU vers le disque (≈ 19 sauvegardes par lentille) ; à 100 à 500 Mo/s, 15 à 80 s chacune, soit de 5 à 25 minutes par lentille, non comprises dans « 11,2 à 11,8 s par document » (le banc ne sauvegarde pas). À signaler ou à mesurer à B0.

**3. Sortie des lentilles hors de la machine non chiffrée** (v2 l. 44-52 ; filtre l. 55). Le filtre exige `inet_down ≥ 300`, rien sur le débit montant. Copier 8 à 17 Go (options (b) et (c)) en B6 n'est pas dans « B5, B6 : 0,5 à 0,8 h » (pire cas 1,5 h) : à 50 Mbit/s, 17 Go prennent ≈ 45 minutes. À écrire : débit montant supposé ou mesuré à B0, durée de la copie, et si la copie échoue (rien n'est détruit avant elle ? la destruction par la minuterie peut tomber avant la fin).

## Mineures
**m-1. Comptage des A100 de 80 Go** (v2 l. 63 et l. 71). La ligne « A100 SXM4 80 Go : 7 » est fausse : le relevé en compte 6 SXM4 80 Go (1,1043 à 1,973) et 1 PCIe 80 Go (1,461), d'où « 7 » seulement avec la PCIe, déjà listée à part. L. 71 : « cinq A100 de 80 Go sur sept » ; sous 1,70 USD/h il y en a **six sur sept** (cinq SXM4 : 1,104 ; 1,107 ; 1,188 ; 1,460 ; 1,506 ; plus la PCIe à 1,461), ou « cinq sur six » si l'on ne compte que les SXM4.

**m-2. Citation de lignes de `02_fit.py`** (v2 l. 16) : voir (d).

**m-3. Durée de la reprise de mesure** (v2 l. 23-24 contre l. 88 et 90) : « ≈ 1,5 à 2 h » ; le tableau donne B2 (1,0 à 1,5) + B4 (0,5 à 0,8) = 1,5 à 2,3 h, `score` compris. À harmoniser.

**m-4. Condition du lot 64** (v2 l. 24-26). Le lot de `measure` en B-β se joue sur une H100 de 80 Go ; la recourse de `GO-2026-11-17-04` se joue sur une A100 de 40 Go. Conditionner le lot 64 de la H100 à la confirmation mémoire sur la carte de 40 Go est sans objet (le pic estimé à 23,5 Gio tient sur 80 Go, le texte le dit lui-même) ; ce que la recourse apporte est l'effet du lot sur le résultat. À reformuler : lot 64 sur 80 Go, effet du lot connu par la recourse. Le chiffre de 23,5 Gio n'est pas sourcé dans la pièce.

**m-5. Rappel au pire cas inatteignable au prix exigé** (v2 l. 118) : voir (c).

**m-6. « Tenu par la carte exigée »** (v2 l. 117) : voir (c).

**m-7. Longueur des documents** : le banc mesure des documents de exactement 128 jetons, avec `torch.compile(dynamic=False)` (`transport.py` l. 110-111) ; `lens_docs` laisse passer des documents plus courts (≥ `min_len`), donc des formes différentes et des recompilations (15 à 37 s l'une au banc, repli en exécution directe après la limite du cache, soit 18 s par document au lieu de 11,4). Avec le tokeniseur de Llama, la part de documents courts n'est pas connue. À mesurer au banc de B0 et à dire ; le pire cas de 23,6 s par document le couvre en partie.

**m-8. Option (b) et recommandation** (v2 l. 137-143) : voir (c), observation de fond. Au moins dire que (a) et (b) sont équivalents au relevé du jour.

**m-9. Hypothèse « Llama 0,9 à 1,2 fois Qwen3-8B »** : plausible (couches plus larges, 32 contre 36 ; paramètres du même ordre, ≈ 8 contre 8,2 milliards), dite non mesurée et levée à B0 : acceptable, rien à corriger ; la pire borne (2 × le banc) la couvre.

# Texte gelé — lecture par lentille neuronale (« Neuron Lens »), tranche de l'ajustement de nos lentilles (B-β), Llama 3.1 8B Instruct — v1

Préenregistrement court d'une expérience **hors du programme**, aux sections du gabarit `prereg/gabarit-preregistrement-v1.md`
(R1, R2). Il continue le texte gelé v6 du volet A et de la tranche des lentilles publiques (B-α), qui renvoyait cette tranche à
« un texte séparé, gelé avant β » (v6, « Plan d'analyse », B.4). **Version scellée** (R1, R12). Issue de trois brouillons archivés tels
quels : brouillon 1 (`af6d4788…`), contre-lu (`4d52c0be…`, à corriger) ; brouillon 2 (`a5f438df…`), contre-lu (`9d591aaf…`, à corriger,
0 bloquante) ; brouillon 3 (`c6a6b00e…`), vérifié (`b8e3bcb9…`, **scellable**, 0 bloquante, 0 majeure, 11 mineures, toutes levées
ici). Tables de reprise en fin de texte. Il ne lance rien.

- Autrice des brouillons 2 et 3 : nouvelle session de la lecture par lentille neuronale, `session_01XJ6MgmvmAAZ9h382ct8kHk`, qui remplace
  `session_01XJ6MgnoxfSYHdF6rpEqZ7w` (autrice du brouillon 1) ; mère `session_01XJ6Mgr8BN6UanALsQatc5E` (R-3103) ; branche
  `claude/tender-rubin-mfxjva`. Les deux lecteurs (contre-lecture du brouillon 2, vérification du brouillon 3) sont des sous-agents neufs
  d'un autre modèle que celui qui sert la session autrice (modèle servi relevé par l'outil de session le 2026-11-18 vers 04:22 UTC ; le
  second lecteur l'a cru le même, sur une lecture fausse de l'attribution des commits : non retenu).
- Date (UTC, `date -u`) : 2026-11-18, brouillon 2 écrit entre 03:50 et 04:10 (relevé `date -u` à 04:02:36) ; brouillon 3 entre 04:10 et 04:16 ; version scellée vers 04:30.
- Code d'analyse : **aucun code de course écrit à ce jour.** Écrits et scellés, sur le texte et le corpus seuls (aucun modèle, aucune
  activation, aucune lentille) : deux outils de comptes avant scellement (« Plan d'analyse », P.0). Code voisin épinglé :
  `stdlogits/neuron-lens`, commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` (MIT), lu seulement, jamais exécuté dans le conteneur
  (règle de Lazar, R-2710) ; correctifs en P.2. Notre code de course (montage, recalcul de n, contrôles, audits, verdicts) sera écrit
  après le scellement de ce texte, contre-lu, essayé (R5) et son commit consigné au manifeste ; il met en œuvre ce texte sans rien en
  changer (tout écart : liste d'arrêt).
- **Ce que l'autrice a lu avant d'écrire** (déclaré, R4) : le brouillon 1 et sa contre-lecture (qui citent des valeurs de B-α) ; le
  verdict de B-α (`lecture-b-alpha/verdict-b-alpha-v1.md`, en-tête et verdict en mots simples) ; la table des pièces du verdict de la
  recourse au lot 64 (`lecture-b-alpha/verdict-recourse-lot64-v1.md` : les lignes qui nomment le lot 64 et les pièces, relevées par
  recherche ; elles disent les valeurs identiques au bit entre les lots 16 et 64) ; les deux fichiers de résultats publiés de
  Qwen3-8B (toutes les couches de `reads_at_firings_qwen3-8b.json` imprimées) ; le texte gelé v6 (« Métrique » B.1 à « Contre-lecture »),
  le devis v12 (en-tête, §§ 1, 4, 5), l'addendum des empreintes v3 (lignes sur DCLM et le tokeniseur, par recherche) ; le code voisin
  (`01`, `02` en partie, `04`, `05`, `corpus.py`, `arch.py` l. 285-303, `lenses.py` l. 60-100, `lens_compare.py` l. 25-93,
  `causal_lens.py` l. 120-135 et 280-345, `reads_at_firings.py` l. 60-80 et 140-182, `transport.py` l. 86-95,
  `tests/test_transport.py` l. 1-35 et 80-105) et l'inventaire du sous-agent. Dans `diag/` de `prep/neuron-lens-v1`, seuls ont été
  lus les noms des fichiers de deux courses de B-α, trois empreintes compagnons et deux lignes de l'addendum de B-α, partie 2
  (empreintes du tokeniseur) ; aucun fichier de résultats bruts n'a été ouvert. Aucun résultat de cette tranche-ci n'existe.

### Documents qui font foi

| pièce | chemin (branche) | empreinte SHA-256 |
|---|---|---|
| texte gelé v6 (volet A et B-α) | `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`prep/neuron-lens-v1`, `45a81e08`) | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` |
| plan et devis v1 (§ 4) | `docs/notes/neuron-lens-v1/plan-et-devis-v1.md` (idem) | `bc20a12aeb5cffeaa12ac264d5141036100b530f4a6a7c0998e24d1b184e3668` |
| plan et devis v2 (§ 3) | `docs/notes/neuron-lens-v1/plan-et-devis-v2.md` (idem) | `4f6534907b849cada369ac87df6fbcf87f766085c0ed56c0388bf849e4aa9c77` |
| devis final de la tranche, v12 (décisions de Lazar en tête) | `docs/notes/neuron-lens-v1/devis-b-beta/devis-tranche-b-beta-v12.md` (branche de session) | `41a4c1f6dc5c2fe59be06d49e76425d857f79338b6bd29aac95ecfa3533294f1` |
| verdict de B-α | `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` (branche principale) | `ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d` |
| verdict de la recourse au lot 64 (A100) | `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-recourse-lot64-v1.md` (branche principale) | `95b09fca126b6c4458b1d4a8171102806fe8bacedf24dcabb152b1f973f30048` |
| verdict de la recourse de l'ablation | `docs/notes/neuron-lens-v1/lecture-recourse-b7/verdict-recourse-b7-v1.md` (`prep/neuron-lens-v1`) | `996744b2090bacc2055bf22ba50c10f810a5364b3b81fab65bdba4d4edb9cc17` |
| **série repère de la lentille R publique** (sortie de `score`, A100, lots 16 et 64 identiques au bit) | `diag/20261117-015632-neuron-lens-b-alpha/causal_lens_llama-3.1-8b-instruct.json` (`prep/neuron-lens-v1`) | `bd57d519a24e5227df2c2d720ba33a54f47653d0741acbb51f1781b59df33073` |
| résultats publiés, lecture contre pilotage (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json` (`prep/neuron-lens-v1`) | `8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3` |
| résultats publiés, lectures aux activations (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/reads_at_firings_qwen3-8b.json` (idem) | `ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd` |
| constats publiés, § 1 (stabilité) | `docs/findings.md` du voisin au commit `849bfe16`, lignes 49 à 62 | `8814874b1cbe144f2cd1070ee20384b397be105c47b3e9cbeb9360a25ee5a866` |
| provenance publiée du corpus d'ajustement (lignes 0 à 999) | `data/corpus/dclm.provenance.json` du voisin au commit `849bfe16` | `16957c528c2f7765afe01b37318aae5365535f29dffdde8c5ce5c48ed1c2e77a` |
| provenance publiée de la tranche DCLM du corpus d'activations (40 000 lignes à partir de la ligne 1 000) | `data/corpus/act-dclm.provenance.json` du voisin au commit `849bfe16` | `a26a70773b35e87349107dac27dddf4f134411c2fd28e5fe5e92cc980e4798e5` |
| tokeniseur de Llama 3.1 8B Instruct, révision `0e9e39f2…` | empreinte relevée au téléchargement de B-α : `diag/20261117-015632-neuron-lens-b-alpha/addendum-partie2-b-alpha-v1.md`, l. 25 (`prep/neuron-lens-v1`) | `79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4` |
| comptes du corpus d'ajustement avant scellement (outil et sortie) | `docs/notes/neuron-lens-v1/outils-b-beta/comptes_corpus_ajustement_b_beta_v1.py` ; `comptes-corpus-ajustement-b-beta-v1.json` (branche de session) | `02a40f534fd91f29af280bcf68e81dcebb6a0e4f7723b72553757c6ddfb2a261` ; `d86ddf4d0bb63ee84dcb839aeddad51fec162cae2265ba1616533fe989ac3f1b` |
| empreinte attendue des lignes d'ajustement (outil et sortie) | `docs/notes/neuron-lens-v1/outils-b-beta/comptes_rows_sha256_b_beta_v1.py` ; `comptes-rows-sha256-b-beta-v1.json` (idem) | `bf7c77383efe79e623cb0795c57b5aa33e49cb5c2909dfc352fe8c16d9846028` ; `ebc557e38f6826becee85a26f6abbf6ddeca791ebd7d23eaad2567d141a1bbf7` |
| inventaire du code voisin pour Llama (rendu verbatim d'un sous-agent neuf, lecture seule) | `docs/notes/neuron-lens-v1/inventaire-code-voisin-llama-b-beta-v1.md` (idem) | `e194592019d2d54339a079dfc368fc8ad1da06db4b1c34a0d4209101cafbeaa3` |
| essai de l'invariance au lot (R-3093) | `docs/notes/neuron-lens-v1/audit-invariance-lot/verdict-audit-invariance-v1.md` (`prep/neuron-lens-v1`) | `4c175cc821f82e3cabf29abc05f7fb2daaf016206a6ec02e633b2989174ab470` |
| Drowse (chargement des lentilles `R:`), version épinglée | paquet `drowse_ai-6.1.4-py3-none-any.whl` (index public des paquets, relevé le 2026-11-18), licence `AGPL-3.0-or-later` | `673ed2b4de653ad2ec22660b0191031ee2c7b4bacaf4cc2ea552f0436b9d8e03` |
| ligne de décision | GO-2026-11-18-02 (`registres/go.md`, branche principale) : prix exigé 2,62 USD/h ; plafond « avec une relance » de **75 USD** ; lieu L1 (aucun rangement) ; clé neuve ; périmètre entier ; modifié par R-3151 (Lazar garde l'ancienne clé ; la passer à une machine exige son mot explicite au moment de la commande) | — |

## Hypothèse

### Portée et séparations (reprises du texte gelé v6, inchangées)
- **Hors programme.** Aucune hypothèse du programme n'est testée ; aucun résultat n'entre dans T0.7, T0.8, G0, G1 ni dans un
  préenregistrement du programme sans nœud de Lazar (GO-2026-11-17-03).
- **Séparation d'avec P3 et P3b** : l'autrice n'a rien lu de P3 ni de P3b ; les sorties de ce texte ne fixent aucun choix de lecture de
  P3b. Aucune donnée réservée, aucune sonde du programme n'est employée ou lue.
- **Modèle** : `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` (32 couches, 4 096 dimensions,
  14 336 neurones à portes par couche, vocabulaire de 128 256 jetons).
- **Règle de lecture** (v6) : une lecture par lentille peut ajouter un soupçon sur une sonde, jamais la blanchir.
- **Ce qui n'est pas une confirmation indépendante** (contre-lecture, m-5) : `measure` est refaite à l'identique de B-α (mêmes neurones,
  graine 0 ; mêmes contextes ; aucune lentille) ; les cibles de B-2, B-3 et B-7 sont donc, au matériel près, celles de B-α, dont
  l'autrice a lu les verdicts. Seule la lentille notée change. Pour B-7, que la référence montre presque insensible à la lentille,
  l'issue est quasi connue ; aucun seuil de B-2, B-3, B-7 n'a bougé depuis le texte gelé v6.

### Énoncé
La chaîne publiée, refaite sur Llama 3.1 8B Instruct avec **nos** lentilles R et S, ajustées par le code du dépôt voisin sur les
**932 documents de 128 jetons pleins** des lignes 0 à 999 du corpus DCLM mélangé publié (« Plan d'analyse », P.1) :
- **B-1, stabilité de nos lentilles** : les lentilles ajustées sur les moitiés paire et impaire du corpus diffèrent peu, et lisent le
  même premier jeton pour la plupart des pôles ;
- **B-2, lecture contre pilotage** : la lecture de l'écriture d'un neurone par notre lentille R prédit l'effet de son pilotage ;
- **B-3, avance sur la lentille des logits** : elle devance nettement la lentille des logits dans la première moitié du réseau ;
- **B-4, écart aux lentilles J et J++** de Neuronpedia : rapporté, non décisif ;
- **B-5, lecture côté entrée** : la lecture par notre lentille S de la direction d'entrée d'un neurone nomme le jeton sous ses
  activations les plus fortes à la couche 0, et nettement plus aux premières couches qu'au milieu du réseau ;
- **B-6, deux codes** : notre lentille R et la lentille R publique de Neuronpedia donnent à peu près la même lecture contre pilotage
  (rapporté, non décisif) ;
- **B-7, lecture contre ablation couche par couche** (conclusion pour un moniteur, hors verdict de reproduction) : avec notre lentille R
  aussi, la lecture prédit mal ce qu'une activation isolée fait en contexte avant les deux tiers de la profondeur.

## Prédiction chiffrée et signe attendu

R3 : aucune course ne vise un signe ; les issues contraires sont écrites et rapportées à l'identique. Confiances de l'autrice, après
lecture des verdicts de B-α (déclaré). Chaque prédiction porte la condition qui la réfute ; une prédiction réfutée est rapportée, elle
ne change aucun verdict (les verdicts suivent « Seuil » et « Critères de lecture gelés »).

| mesure | prédiction | réfutée si | issue modale prédite | confiance |
|---|---|---|---|---|
| B-1 | différence entre moitiés (non arrondie) de 0,02 à 0,08 aux couches 0 à 18 de R (cibles `out` et `mid`), au plus 0,05 dès la couche 23, au plus 0,06 partout pour S ; accord du premier jeton de 0,85 à 0,99 aux six couches lues | l'une des conditions de la prédiction manque (une différence hors de l'intervalle prédit à une couche, ou un accord hors de [0,85 ; 0,99] à une des six couches) | « reproduit » | 0,6 |
| B-2 | `r_med`(notre R) ≥ `r_med`(lentille R publique) − 0,02 à au moins 15 des 20 couches 8 à 27 ; `pass` ≥ 0,90 à chaque couche 11 à 27 ; aux couches 8 à 10, au moins une condition de « reproduit » manquée, comme en B-α | l'une des trois conditions de la prédiction manque (dont : les couches 8 à 10 remplissent toutes les conditions de « reproduit ») | « autre » | 0,45 pour « reproduit », 0,5 pour « autre » |
| B-3 | écart `r_med`(notre R) − `r_med`(logits) ≥ +0,20 à chaque couche 4 à 15 | écart < +0,20 à une couche 4 à 15 | « reproduit » | 0,65 |
| B-4, face à J | `r_med`(notre R) − `r_med`(J) **négatif** à au moins 11 des 20 couches 4 à 23 (B-α : la lentille R publique est sous J à 19 couches sur 20, verdict de B-α) | écart négatif à 10 couches ou moins | — | 0,55 |
| B-4, face à J++ | `r_med`(notre R) − `r_med`(J++) **positif** à au moins 11 des 20 couches 4 à 23 (B-α : 20 sur 20 pour la lentille R publique) | écart positif à 10 couches ou moins | — | 0,7 |
| B-5 | `read_S` ≥ 0,60 à la couche 0 ; moyenne de `read_S` sur les couches 1 à 7 au moins 0,10 au-dessus de sa moyenne sur les couches 12 à 23 ; part silencieuse ≤ 0,40 à la couche 0 | `read_S` < 0,60 à la couche 0, ou écart des moyennes < 0,10, ou B-5 « non lisible » | « reproduit » | 0,5 |
| B-6 | « accord » : écart absolu des `r_med` (« steer 1x », notre R contre la lentille R publique) ≤ 0,05 à au moins 21 des 28 couches 0 à 27 et ≤ 0,15 à toutes | « désaccord » (écart > 0,15 à une couche) ou « intermédiaire » | « accord » | 0,5 |
| B-7 | comme en B-α et sa recourse : `r_med` ≤ 0,20 aux couches 0 à 14, de 0,25 à 0,40 à la couche 15, ≥ 0,80 aux couches 26 à 29 | l'une des trois conditions de la prédiction manque | « autre » (seule la couche 15 manquerait) | 0,55 |
| verdict d'ensemble | — | — | « partiel » | 0,5 |

## Métrique

### M.1 Commun (repris du texte gelé v6, « Métrique », B.1, sauf mention)
- **Chaîne de mesure** : `checks/causal_lens.py measure` avec ses défauts publiés : 32 neurones par couche (`random.Random(0)`), deux
  pôles, 16 contextes de 64 jetons (les 16 premiers documents d'au moins 64 jetons parmi les 64 premières lignes de la tranche DCLM du
  corpus d'activations, soit dans les lignes 1 000 à 1 063 de DCLM : `causal_lens.py` l. 122), positions `[16, T)`, doses 1× et 4×
  `act_top`, ablation sur les 8 premiers documents du pôle, fenêtre de 8 ; **lot de contextes publié, 64** (sur une A100, les lots 16
  et 64 donnent le même résultat au bit près, R-3093 ; sur H100, non mesuré) ; puis `score`.
- **Lentilles notées** : logits ; J, J++ (`npJpp`) et R publique (`npR`) de Neuronpedia, fichiers et empreintes du texte gelé v6 ;
  **notre lentille R** (exportée par `04_export_rlens.py` depuis l'ajustement, nom `R:dclm-llama`), et, pour l'audit des deux codes
  seulement, les lentilles de ses deux moitiés (`R:dclm-llama-even`, `R:dclm-llama-odd`). Aucune lentille n'entre dans `measure`.
- **Métriques par couche, cible et lentille** : `r_med`, `pass`, `control_med`, **n**, telles que définies au texte gelé v6, « Métrique »,
  B.1 (n recalculé par notre code depuis le fichier `-causal.pt`, par la règle de `score`). Cibles : « steer 1x » (B-2, B-3, B-4,
  B-6) ; « ablate win » (B-7) ; « steer 4x » et « ablate pos » rapportées sans critère. Valeurs lues dans la sortie JSON de `score`,
  telles qu'écrites.
- **Couche 31** : la cible `out` de notre lentille R s'arrête à la couche 30 (`transport.py`, `target_layers`, l. 256-258) ; à la
  couche 31, notre R est **exactement** la lentille des logits dans `score`, comme les trois lentilles de Neuronpedia : ce n'est pas une
  mesure de lentille (texte gelé v6, même règle).
- **Couche lisible** : n ≥ 48 pour la cible considérée ; une bande dont plus du quart des couches est non lisible rend la mesure
  « partielle » pour cette bande.
- **Bandes de couches** : celles du texte gelé v6, inchangées ; profondeur convertie par la règle du texte gelé v6, couche Llama l ↔
  couche Qwen3 ⌊l × 36/32⌋, qui reste la règle de tous les seuils.

### M.2 Mesures propres à cette tranche
- **B-1, différence entre moitiés** : `‖moyenne paire − moyenne impaire‖ / ‖moyenne‖` par cible et par couche, **recalculée par notre
  code sur la machine, non arrondie**, depuis le fichier d'ajustement (`Accumulator.split_half`, `neuron_lens/transport.py` l. 64-72 ;
  la valeur imprimée à deux décimales par `02_fit.py` et `04_export_rlens.py` est versée pour mémoire, jamais lue pour un seuil) ;
  lentille R : cibles `out` (couches 0 à 30) et `mid` (0 à 31) ; lentille S : `mid` et `out` (0 à 31).
- **B-1, accord du premier jeton** : part des **pôles** (deux par neurone, tous les neurones de la couche, soit 28 672 pôles) dont la
  lecture de l'écriture par la lentille R de la moitié paire et par celle de la moitié impaire a le même premier jeton, sur les jetons
  gardés de Llama (P.3) ; cible `out` seule ; définition de `checks/lens_compare.py` l. 72-78 (lecture `read` de la colonne de `W_down` de chaque neurone, au
  signe + et au signe −, dix premiers jetons parmi les jetons gardés), valeur **non arrondie** écrite par le correctif (4) ; aux couches **2, 7, 12, 18, 23, 28**. Ces six couches sont les couches tabulées par la référence (2, 8, 14, 20, 26, 32
  de Qwen3-8B) ramenées à 32 couches par `round(l × 32/36)` : **seconde règle de profondeur, réservée à ce seul choix de couches**
  (déclaré, contre-lecture m-2) ; par la règle du texte gelé v6, elles valent les couches 2, 7, 13, 20, 25, 31 de Qwen3-8B. Sans effet
  sur les seuils de B-1, qui ne dépendent pas de la profondeur. Rapportés sans critère : le recouvrement des dix premiers jetons ; et,
  comme repère, l'accord de chaque moitié avec la lentille R publique aux mêmes couches (aux couches basses, l'accord est porté en
  partie par un mode commun : 0,78 de l'énergie à la couche 2 de la référence, `findings.md` l. 71-74 ; il y discrimine peu).
- **B-5, `read_S`** : définition de `checks/reads_at_firings.py` (l. 84-107, 133-181 ; inventaire, définition de `read_S`), écrite
  ici. Pour chaque pôle de la couche (deux par neurone), la **direction d'entrée** `c` est la combinaison des lignes de porte et de
  montée normées (`read_rows`, â ± b̂, ou ∓b̂ sur le lobe négatif lu dans `neg_lobe` des tables `acts`), lue par la cible `mid` de
  notre lentille S : covecteur `c · K_mid`, normé. Score d'un jeton v : produit avec `e_v − ē` (plongements des jetons gardés,
  centrés) ; z par jeton sur tous les pôles de la couche. **Statistique d'un pôle** : moyenne des z des jetons sous ses activations
  utilisables (activation positive parmi ses 64 activations les plus fortes, `top["val"]`, l. 137-140, `TOP = 64`, `catalog.py` l. 34 ; jeton dans
  les jetons gardés) ; non définie sous 3 activations
  utilisables (`MIN_FIRINGS`, l. 74). **Paire mal appariée** : la direction du pôle `perm[i]` sur les jetons du pôle i, une permutation
  par signe (`torch.randperm`, générateur à la graine 0, l. 133, 149). Valeur p contre la loi de toutes les paires mal appariées
  définies ; **Benjamini-Hochberg** sur les pôles de statistique définie et non quasi silencieux (`act_top` ≥ 0,05, seuil absolu,
  l. 73), au taux de 5 % (l. 75) ; q = 1 pour les autres. `read_S` = part des pôles de q ≤ 0,05 sur **tous les pôles de la couche**
  (les pôles silencieux ou sans statistique comptent comme des échecs, l. 176-180). Rapportés à côté, sans critère sauf la règle de
  lisibilité ci-dessous : la **part silencieuse** `silent` par couche, `read_S_net` et la part des pôles retenus parmi les pôles non
  silencieux (`read_S / (1 − silent)`).
- **B-5, lisibilité** (contre-lecture, M-3) : B-5 est **« non lisible »** (donc « partiel », jamais « reproduit » ni « non
  reproduit ») si la part silencieuse dépasse 0,40 à la couche 0, ou si sa moyenne sur les couches 1 à 7 dépasse 0,50. Repères sur la
  référence ramenée à 32 couches : 0,000 à la couche 0 ; moyenne 0,240 sur les couches 1 à 7 (0,564, 0,608, 0,421, 0,089, 0,001,
  0, 0). Raison : au-delà, « reproduit » devient impossible ou « non reproduit » certain par construction du dénominateur.
- **B-6** : `r_med`(notre R) − `r_med`(`npR`), « steer 1x », couches 0 à 27, dans la même sortie de `score`.
- **Intervalles** : par rééchantillonnage des pôles (2 000 tirages) pour B-2, B-3, B-4, B-6, B-7, rapportés ; verdicts sur les valeurs
  ponctuelles (comme en B-α).

## Seuil

Fixés avant toute lecture ; aucun résultat de cette tranche n'existe. « Reproduit » exige la condition à **chaque couche lisible** de
la bande ; « plus de N des couches » se lit « plus de la moitié des couches lisibles de la bande nommée » (règle du texte gelé v6).
Valeurs comparées : celles de `score` telles qu'écrites dans son JSON (4 décimales, `causal_lens.py` l. 362, 367 ; comme en B-α) ; celles de B-1 et de B-5, non arrondies (calculées par notre code ou écrites en flottants complets par `reads_at_firings.py`, l. 289-291) ; « au-dessus » = strictement.

| mesure | « reproduit » | « non reproduit » |
|---|---|---|
| B-1 | différence entre moitiés ≤ 0,10 à chaque couche et chaque cible des deux lentilles **et** accord du premier jeton ≥ 0,80 aux six couches lues | une couche d'une cible à plus de 0,20, **ou** un accord sous 0,60 à l'une des six couches |
| B-2 | seuils de B-2 du texte gelé v6, avec **notre** lentille R : `r_med` ≥ 0,40 (8–15), ≥ 0,60 (16–23), ≥ 0,85 (24–27) ; `pass` ≥ 0,90 (8–27) ; témoin : `control_med` hors de ±0,05 à au plus une couche de 0 à 27, à aucune hors de ±0,10 | `pass` < 0,50 à plus de 6 des 12 couches 16–27, ou `r_med` < 0,30 à plus de 4 des 8 couches 16–23 |
| B-3 | `r_med`(notre R) − `r_med`(logits) ≥ +0,20 à chaque couche 4–15 | écart ≤ 0 à plus de 6 des 12 couches 4–15 |
| B-4 | rapportée, non décisive : notre R − J et notre R − `npJpp`, couches 4–23, en deux lignes | — |
| B-5 (réécrit) | `read_S` ≥ 0,60 à la couche 0 **et** moyenne de `read_S` sur les couches 1 à 7 au moins 0,10 au-dessus de sa moyenne sur les couches 12 à 23 ; B-5 lisible | `read_S` < 0,30 à la couche 0, **ou** moyenne sur 1 à 7 au plus égale à la moyenne sur 12 à 23 ; B-5 lisible |
| B-6 | rapportée, non décisive : « accord » si l'écart absolu est ≤ 0,05 à au moins 21 des 28 couches 0 à 27 **et** ≤ 0,15 à toutes ; « désaccord » s'il dépasse 0,15 à au moins une couche ; « intermédiaire » sinon | — |
| B-7 (« ablate win », notre R) | `r_med` < 0,25 à chaque couche 0–15 **et** ≥ 0,50 à chaque couche 26–29 | `r_med` ≥ 0,40 à plus de 4 des 8 couches 8–15 (**par le haut**), ou < 0,30 à plus de 2 des 4 couches 26–29 (**par le bas**) |

Toute mesure ni « reproduit » ni « non reproduit » est « autre ».

**Pourquoi B-5 est réécrit** (texte gelé v6, B.4) : le critère du plan v1, « décroissant sur le premier quart », manquerait la
référence publiée elle-même (`read_S` 0,848, 0,248, 0,090, 0,229, 0,352 aux couches 0 à 4 de Qwen3-8B). Le critère neuf garde la couche
0 du plan v1 et remplace la monotonie par un écart de moyennes entre bandes. **Sur la référence publiée** ramenée à 32 couches par la
règle du texte gelé v6 : couche 0 = **0,8481** ; moyenne des couches 1 à 7 = **0,2248** ; des couches 12 à 23 = **0,0271** ; écart =
**0,1977** (recalculés par le contre-lecteur du brouillon 1) ; le seuil de 0,10 en vaut à peu près la moitié. Notre code des verdicts
recalcule ces quatre valeurs avant la course (P.4) ; un écart de plus de 10⁻⁴ arrête la course.

### Chaîne en défaut (aucun verdict de mesure ; prime sur tout le reste)
Évaluée **par notre code, sur la machine, avant la destruction**, mécaniquement, sans lecture par la fille. Conditions (a) à (e) du
texte gelé v6 (« Seuil », B), appliquées aussi à notre lentille R, et conditions neuves :
- (a) `control_med` hors de ±0,10 à une couche de 0 à 27, pour l'une des quatre cibles et l'une des lentilles notées ;
- (b) **pilotage sans effet** : à une couche de 0 à 27, plus de la moitié des 64 pôles écartés par `score` pour effet nul en « steer 1x » ;
- (c) cas sains internes manqués : lentille des logits, `r_med` (« steer 1x ») < 0,80 à l'une des couches 28–30 ; `npR`, < 0,85 à
  l'une des couches 28–30 ; **notre R**, < 0,85 à l'une des couches 28–30 (choix déclaré, contre-lecture du brouillon 2, m-16 : à ces
  couches toute lentille approche la lecture finale — publié pour la lentille R : 0,98 à 0,99 ; logits : 0,935 à 0,957 — ; une valeur
  sous 0,85 y signale un défaut d'export ou de convention de couche plutôt qu'une propriété de la lentille) ;
- (d) essai d'un correctif employé ((1) à (6), P.2) ou de l'estimateur sur le Qwen3 miniature du dépôt avec un test sauté ou en échec ; fumée de la passe en échec ; essai des crochets de
  pilotage et d'ablation de `causal_lens.py` sur un Llama miniature en échec (un échec d'**accès** au tokeniseur ou aux poids sous
  licence est un arrêt de montage, pas une chaîne en défaut) ;
- (e) **repli sur la lentille des logits** : pour `J`, `npJpp`, `npR` ou notre R, |`r_med`(lentille) − `r_med`(logits)| < 10⁻³ à une
  couche de 0 à 23 (« steer 1x »), ou une matrice de la lentille égale à l'identité (écart maximal en valeur absolue ≤ 10⁻⁶, en
  float32) à une couche de 0 à 27 ; contrôlé à B0 pour les trois fichiers de Neuronpedia, **après l'export et avant `score`** pour notre
  R (contre-lecture, m-9) ;
- (f) **essai de l'estimateur** sur un Llama miniature contre la force brute en échec, à la tolérance des essais du dépôt
  (`atol = 1e-4`, `tests/test_transport.py` l. 87-102) ; le Llama miniature est décrit en P.2 ;
- (g) **ajustement incomplet, vide ou non fini** : pour l'une des deux lentilles, un nombre de documents par moitié différent de 466 et
  466 ; `next_doc` différent de `meta["docs"]` (un ajustement interrompu serait sinon exporté et lu sans message : inventaire, repli 2) ; un document de longueur autre que 128 ; `rows_sha256` du fichier d'ajustement différent de
  `a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3` (P.1) ; `full_length` différent de vrai ; une différence entre
  moitiés non finie ; une matrice de lentille non finie ;
- (h) **nombre de couches** : pour notre R, nombre de couches exportées différent de 31 pour la cible `out` (couches 0 à 30) ou de 32
  pour la cible `mid` ; pour notre S, première dimension des sommes du fichier d'ajustement différente de 32 pour chaque cible ;
- (i) **corpus partagé** : un identifiant du corpus d'ajustement (provenance `dclm.provenance.json`, réécrite sur la machine par `01`)
  présent dans la tranche DCLM du corpus d'activations (`act-dclm.provenance.json`, réécrite par `05`) ; ou, pour l'une des deux, une
  révision, une liste d'identifiants (dans l'ordre) ou un `skip` différents de ceux de la provenance publiée (`16957c52…` : lignes
  `[0, 1000)` ; `a26a7077…` : `skip` 1 000, `n` 40 000) ; ou un **texte** commun : l'empreinte SHA-256 du texte **entier** (champ `text` de la ligne
  JSONL, sans coupe) de l'un des 932 documents d'ajustement égale à celle de l'un des 40 000 textes entiers de `act-dclm.jsonl`. Moments : avant l'ajustement, provenance écrite
  par `01` contre la provenance publiée de la tranche d'activations (`a26a7077…`, suivie dans le dépôt) ; après `05`, provenance
  réécrite, qui doit être égale à la publiée, et comparaison des textes ; de nouveau avant `measure` ;
- (j) **cas sain de la lentille R publique** (contre-lecture, m-10) : `r_med`(`npR`, « steer 1x ») de cette course s'écarte de la série
  repère (`bd57d519…`) de plus de 0,05 à plus de 2 des 28 couches 0 à 27, ou de plus de 0,10 à l'une d'elles ; la recourse a mesuré un
  effet du matériel allant jusqu'à 0,03 entre deux cartes, la H100 est une troisième ;
- (k) **noms des ajustements vus par `arch.fits`** (contre-lectures, M-4 du brouillon 1, M-1 et m-8 du brouillon 2) : notre code appelle
  `arch.fits(MODEL)` dans le même environnement juste avant l'étape concernée. Juste avant la fumée, juste avant la passe d'activations
  (`06_activations.py` lit `arch.fits`, l. 96) et juste avant `07_drivers.py`, il doit rendre `hub` (preuve complémentaire : le message
  que le correctif (1) imprime quand il prend cette branche, relevé dans le journal de la passe) (les liens durs du correctif (5) ne sont
  pas encore posés : la passe prend la branche déjà jouée en B-α, qui saute la colonne `out_R_z` de la table des têtes, correctif (1),
  bloc 3) ; juste avant `reads_at_firings.py`, il doit rendre nos deux noms, et les fichiers à ces noms doivent avoir les empreintes
  consignées à la fin de l'ajustement. Tout autre cas → chaîne en défaut ;
- (l) **témoin ou pilotage dégénéré**, constaté par un audit (« Critères de lecture gelés », audits A1 et A5), **ou** l'une des gardes
  (a) à (c) manquée sur la sortie de `score` de la graine 1 ;
- (m) **appariement dégénéré de B-5**, constaté par l'audit A4 ;
- (n) **notre lentille confondue avec la publique** : une matrice de notre R égale à celle de `npR` (écart maximal ≤ 10⁻⁶, en float32)
  à une couche de 0 à 27, ou les deux fichiers d'empreinte égale ; contrôlé après l'export, avant `score` ;
- (o) **aller-retour de l'export** (inventaire : `score` l. 303 prend la lentille des logits, sans message, pour une couche absente ;
  format de Drowse non lu) : `load_lens("R:dclm-llama")`, `"R:dclm-llama-even"` ou `"R:dclm-llama-odd"` lève une erreur (le
  voisin lève `FileNotFoundError` si Drowse ne trouve rien, `lenses.py` l. 37-45) ou rend `None` à une couche de 0 à 30, ou ses matrices s'écartent de la moyenne calculée sur le fichier d'ajustement (`Accumulator`, cible `out` : entière, moitié
  paire, moitié impaire) de plus de 10⁻³ en écart relatif de Frobenius à une couche de 0 à 30 ; contrôlé après l'export, avant
  `lens_compare.py` et `score` ;
- (p) **moins de documents que demandé, sans message** (inventaire, repli 6) : `measure` avec un nombre de contextes différent de 16
  (`meta["contexts"]`) ; `07_drivers.py` avec moins de documents que les 4, 2 et 2 demandés par tranche ;
- (q) **reprise et banc** (inventaire, repli 1 ; contre-lecture du brouillon 2, m-3) : le banc de B0 tourne dans une copie à part de
  l'arbre voisin (même commit), dont le dossier `data/fits/` est distinct ; avant le premier lancement de chaque ajustement, aucun fichier
  `data/fits/r|s-llama-3.1-8b-instruct-L32-dclm-T128.pt` n'existe dans l'arbre de la course ; avant toute relance, le point de
  sauvegarde porte `rows_sha256` = `a6afd972…`, `full_length` vrai, la lentille et le modèle attendus ;
- (r) **jetons gardés** (inventaire, repli 11) : l'empreinte de la liste `kept()` diffère, avant `06_activations.py`, `lens_compare.py`,
  `07_drivers.py` ou `reads_at_firings.py`, de celle consignée après l'unique `03_token_counts.py` ;
- (s) **fichiers antérieurs** (inventaire, repli 9) : avant `reads_at_firings.py`, un fichier `data/checks/reads_at_firings-*.pt` ou un
  résumé `reads_at_firings` existe déjà (le script fusionnerait d'anciennes entrées).

Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3 (règle du texte gelé v6).

## Plan d'analyse

### P.0 Comptes faits avant scellement, sur le texte et le corpus seuls (aucun modèle, aucune activation, aucune lentille)
Deux outils écrits par l'autrice, exécutés dans le conteneur (aucune ligne du code voisin exécutée ; sa logique recopiée et citée),
scellés avec leurs sorties (table des documents) :
- `comptes_corpus_ajustement_b_beta_v1.py` lit les lignes 0 à 999 de `HuggingFaceFW/dclm_100BT-shuffled`, révision
  `2fa015e4044ec442a0734e89658cdcc538d10dd4`, premier fichier (`data/train-00000-of-00100.parquet`), et vérifie que leurs
  identifiants, leur ordre et leurs longueurs en caractères sont ceux de la provenance publiée ; tokeniseur `tokenizer.json` de Llama
  3.1 8B Instruct d'empreinte `79e3e522…` (la même que le fichier téléchargé en B-α ; obtenu d'un miroir public, vérifié par son
  empreinte), bibliothèque `tokenizers` 0.23.2 (celle de B-α). Il recompte ce que `neuron_lens/corpus.py` (`_rows`, `lens_docs`) ferait :
  document coupé à 4 000 caractères, encodé avec le jeton de début (identifiant 128 000), coupé à 128 jetons. **Résultats** : 932
  documents de 128 jetons pleins ; 68 plus courts (de 36 à 127 jetons, 44 longueurs distinctes) ; aucun sous 18 jetons (le défaut
  publié les garderait donc tous les 1 000) ; **aucun identifiant commun** avec les 40 000 lignes de la tranche DCLM du corpus
  d'activations (provenance publiée : `skip` 1 000, `n` 40 000) ; moitiés paire et impaire des documents pleins : 466 et 466 ;
  jetons au-delà des 16 premiers (champ de sortie de l'outil) : 104 384 pour les documents pleins, 109 553 pour le défaut publié sur les mêmes lignes ; positions estimées, `[16, T − 1)` (`transport.py` l. 90-93), soit un de moins par document : **103 452** et **108 553** (− 4,7 %).
- `comptes_rows_sha256_b_beta_v1.py` recalcule `rows_sha256` (`corpus.py` l. 63-65 ; l'en-tête de l'outil dit 62-64, à tort) des lignes que l'ajustement prendra :
  `a6afd972eeaa3566a28d07216efaf75624fda20293c5fab3b7af39277aaf93b3` (932 documents) ; moitiés `4a31baec…` et `ef95a60c…` ;
  pour mémoire, défaut publié `38b9e168…` (1 000 documents).

### P.1 Corpus d'ajustement : séparation d'avec les contextes qui jugent la lentille (contre-lecture, bloquante 1)
- **Règle** : le corpus d'ajustement est fait des seules lignes 0 à 999 de DCLM, comme publié (`01_lens_corpus.py --docs 1000`,
  **inchangé**), et l'ajustement ne garde que les documents de 128 jetons pleins, par l'option publiée `02_fit.py --full-length`
  (`--docs 1000 --seq-len 128`) : `lens_docs(…, full=True)` prend les premiers documents pleins de `dclm.jsonl` jusqu'à 1 000 et
  s'arrête à la fin du fichier, soit les **932** documents de P.0. Aucune ligne au-delà de 999 n'entre dans l'ajustement, et la tranche
  DCLM du corpus d'activations commence à la ligne 1 000 (`05_act_corpus.py`, `DCLM_SKIP`, l. 33) : les contextes de pilotage de
  `measure` (lignes 1 000 à 1 063) et les documents des activations les plus fortes (B-5, B-7) ne peuvent pas entrer dans
  l'ajustement. Garde (i) : identifiant commun aux deux corpus.
- **Pourquoi pas le défaut publié** (1 000 documents dont 68 courts) : 44 longueurs distinctes font autant de recompilations de 15 à
  37 s chacune avec `torch.compile(dynamic=False)` (devis v12, § 4), non bornées par le banc d'un document ; le devis a été chiffré sur
  des documents de 128 jetons pleins. **Pourquoi pas des remplaçants pris plus loin** (brouillon 1, correctif 5) : ils devraient venir
  après la ligne 40 999, hors du mélange publié des 1 000 premières lignes ; et le brouillon 1 les prenait dans la tranche des
  contextes.
- **Effets déclarés** (écart au code publié et au devis) : 932 documents au lieu de 1 000 ; 1 864 passages au lieu de 2 000 (− 7 % de
  durée d'ajustement ; la borne du banc et le plafond sont gardés tels quels, donc plus stricts ; les deux bornes de compte rendu en
  durée, 12,9 h et 24,1 h, calculées sur 2 000 passages, sont gardées aussi, un peu lâches, sans effet sur la dépense) ; population de documents longs seulement.
  Effet attendu sur B-1 : faible, de signe incertain — moitiés de 466 documents au lieu de 500 et 4,7 % de positions estimées en moins (vers le
  haut, de 2 à 4 % sur la part due au bruit : √(108 553 / 103 452) = 1,024 par positions ; √(500 / 466) = 1,036 par documents, modèle de
  bruit publié `0,65/√500`, `findings.md` l. 50-51), mais des documents tous pleins (vers le bas). Les moitiés suivent le **rang parmi
  les documents gardés** (`02_fit.py` l. 173), non la parité des lignes de DCLM. Le fichier d'ajustement porte le
  suffixe `-T128` (`02_fit.py` l. 56-57) : P.2, correctif (5).
- **Avant l'ajustement** (B0), notre code recalcule sur la machine, par `neuron_lens.corpus.lens_docs` et `rows_sha256` du dépôt voisin
  et le tokeniseur téléchargé, le nombre de documents (932), les moitiés (466, 466) et `rows_sha256` (`a6afd972…`) : un écart arrête
  la course avant tout ajustement (liste d'arrêt).

### P.2 Correctifs du code voisin (chacun écrit, contre-lu, scellé avant usage ; essayé à B0 sur la machine, cas sain et artefact)
Inventaire complet des réglages de Llama dans le code voisin, fait **avant** ce scellement par lecture seule (contre-lecture, M-5) :
`inventaire-code-voisin-llama-b-beta-v1.md` (table des documents). La liste ci-dessous est **fermée** : tout autre changement du code
voisin est une nouvelle version de ce texte, contre-lue.

**Correctifs repris de B-α** (déjà écrits, contre-lus, scellés ; `docs/notes/neuron-lens-v1/correctifs/`, `prep/neuron-lens-v1`) :
- (1) passe d'activations de Llama (`06_activations-llama-v2.diff`, note `correctif-06_activations-v3.md`, essai
  `essai-06_activations-llama-v3.py`) ;
- (2) lentilles publiques de Llama dans `lenses.py` (`lenses-neuronpedia-llama-v2.diff`, note v3, essai v3 : empreintes, couches
  contiguës `0..30` exigées) ;
- (3) graine de neurones de l'audit (`causal_lens-graine-v1.diff`, note et essai v1) : la même graine pour `sample_neurons` et `score` ;
- (6) provenance « chat » de Llama (`provenance-chat-llama-v1.diff`, note v2) : révision `8049631c…` imposée à la tranche « chat »,
  argument `--docs dclm=40000,zh=8000,code=8000,chat=8000`, ordre des contrôles avant la passe.

**Correctifs neufs** (à écrire, contre-lire, sceller ; essai sur cas sain et artefact) :
- (4) `checks/lens_compare.py` : (a) le modèle vient de `neuron_lens.catalog.MODEL` (donc de `NEURON_LENS_MODEL`) au lieu de
  `MODEL = "Qwen/Qwen3-8B"` écrit en dur (l. 29), pour le tokeniseur, les poids, les lentilles **et** `kept()` (l. 46), qui le lisait
  déjà de la variable : sans ce correctif, les jetons gardés de Llama s'appliqueraient aux lignes de `lm_head` de Qwen, sans erreur
  (inventaire, repli 5) ; (b) périphérique `cuda` s'il existe (l. 39 : `mps` sinon processeur central) ; (c) écriture d'un fichier JSON
  des valeurs **non arrondies** par couche et par paire de lentilles (accord du premier jeton, l. 75 ; recouvrement des dix premiers,
  l. 76-77), en plus de l'impression ; rien d'autre ne change (définitions, demi-précision de `unembed`, l. 47).
- (5) **aucune ligne de code** : les fichiers d'ajustement `r-llama-3.1-8b-instruct-L32-dclm-T128.pt` et `s-…-T128.pt` (suffixe de
  `--full-length`, `02_fit.py` l. 56-57) reçoivent chacun un **lien dur** au nom que cherche `arch.fits` (`r-…-L32-dclm.pt`,
  `s-…-L32-dclm.pt`, `arch.py` l. 299-303), fait par notre commande **juste avant `reads_at_firings.py`** (P.3, étape 6), non après
  l'ajustement ; même contenu, empreintes vérifiées égales ;
  garde (k). Sans lui, `arch.fits` rendrait `hub` (inventaire, repli 3).

**Arguments et environnement imposés** (aucun changement de code ; chaque défaut publié qui ne convient pas à Llama est passé
explicitement — inventaire, tables 01 à `reads_at_firings`) : `NEURON_LENS_MODEL=meta-llama/Llama-3.1-8B-Instruct` pour toutes les
étapes ; `01_lens_corpus.py --docs 1000 --revision 2fa015e4044ec442a0734e89658cdcc538d10dd4` ; `02_fit.py --lens R|S --model
meta-llama/Llama-3.1-8B-Instruct --docs 1000 --seq-len 128 --full-length --save-minutes 60` (défauts publiés : `--model
Qwen/Qwen3-0.6B`, `--docs 12`, `--save-minutes 10` ; autres défauts gardés : `--dim-batch 256`, cibles par défaut, `--device auto`,
`--dtype auto`, soit bf16 sur carte avec produits en TF32, consignés au manifeste ; jamais `--shard`) ; `04_export_rlens.py <fit R>
--name dclm-llama`, puis `--name dclm-llama-even --half 0` et `--name dclm-llama-odd --half 1` ; `05_act_corpus.py --docs
dclm=40000,zh=8000,code=8000,chat=8000` ; `lens_compare.py --lenses R:dclm-llama-even,R:dclm-llama-odd,npR --layers 2,7,12,18,23,28
--samples 0` (défaut publié `--layers 2,8,14,20,26,32` : la couche 32 n'existe pas) ; `causal_lens.py score --lenses
logit,J,npJpp,npR,R:dclm-llama,R:dclm-llama-even,R:dclm-llama-odd --tag b-beta` (défaut hors Qwen `logit,hub` ; `--tag` distinct par
appel, le résumé de même étiquette étant écrasé) ; `reads_at_firings.py --parts neurons` (le défaut `neurons,heads` échoue sur Llama).
**Drowse** (chargement des lentilles `R:`, extra optionnel `drowse.ai>=6.0.0` sans verrou) : épinglé à **6.1.4** (dernière version à
l'index le 2026-11-18), paquet `673ed2b4…`, licence `AGPL-3.0-or-later` (employé tel quel sur la machine louée, ni modifié, ni redistribué, ni
offert comme service à des tiers ; les lentilles sont des données ; publier un jour le code des lentilles avec une version modifiée
de ce paquet serait un nœud : mot de la mère, 2026-11-18 vers 04:18 UTC) ; lu, non exécuté, dans le conteneur : `drowse/lens/jlens.py` (`JacobianLens.jacobians` = matrices de
la cible `out` par couche : classe l. 141-145, propriété vers l. 249) et `drowse/lens/store.py` (dossiers locaux par identifiant de modèle). Une autre version, ou une
autre empreinte du paquet sur la machine = arrêt (liste d'arrêt). Son aller-retour est contrôlé par la garde (o).

**Constats gardés tels quels** (comme publié et comme en B-α ; rapportés, non corrigés) : le jeton de début de Llama (128 000) compte dans
les 128 jetons d'un document et entre dans les jetons gardés (`kept()` ne retire pas les jetons spéciaux, `catalog.py` l. 125-134) — son
compte et son rang sont rapportés ; `score` calcule sur le processeur central et ignore `--device` (l. 277 ; lenteur seulement, durées de
B-α) ; `score` filtre le vocabulaire par comptes ≥ 5, sans retrait des « � » (l. 274, 278), ce qui n'est pas `kept()` ; écart
`eps = 1e-6` écrit en dur dans `rms_norm_columns` contre `1e-5` pour Llama (sans effet sur les rangs dans une colonne, donc sur le
premier jeton) ; dans `07_drivers.py`, la position 24 des deux documents « chat » tombe dans l'en-tête du gabarit de Llama (sans effet
sur les mesures de ce texte : la table des pilotes n'entre que dans `read_R`, non mesuré ici) ; `reads_at_firings.py` tire ses paires
mal appariées par une permutation qui garde quelques points fixes (≈ 1 par moitié de pôles).

**Essai de l'estimateur sur un Llama miniature** (garde (f) ; essai neuf, à écrire, contre-lire, sceller) : les essais du dépôt
comparent les estimateurs à la force brute sur un **Qwen3 miniature** seulement (`tests/test_transport.py` l. 1, 15-35, 75-102). Notre
essai reprend `test_estimates_match_brute_force` mot pour mot en remplaçant `Qwen3Model(Qwen3Config(…))` par
`LlamaModel(LlamaConfig(…))` aux mêmes dimensions (vocabulaire 50, 16 dimensions, 32 neurones, 3 couches, 2 têtes de requête et 1 de
clés et valeurs, `head_dim` 8, attention « eager »), puis dans la variante « réaliste » du dépôt (4 têtes dont 2 de clés et valeurs,
`initializer_range` 0,2, poids de normes tirés dans [0,3 ; 2,0]) ; graines `torch.manual_seed(0)` et `(1)` comme le dépôt ;
tolérance `atol = 1e-4`, inchangée. Les essais du dépôt sur le Qwen3 miniature sont aussi joués ; aucun test sauté.

### P.3 Étapes (devis v12, §§ 1 et 4 ; GO-2026-11-18-02), dans cet ordre
Arguments complets en P.2 ; `NEURON_LENS_MODEL` posé pour toutes les étapes.
1. **B0, montage** : environnement (Drowse épinglé) ; poids et tokeniseur de Llama à la révision épinglée (clé selon R-3151) ;
   empreinte du tokeniseur égale à `79e3e522…` ; lentilles de Neuronpedia ; essais des correctifs (P.2), des essais du dépôt sur le
   Qwen3 miniature et de l'estimateur sur le Llama miniature (garde (f)) ; essai des crochets de `causal_lens.py` sur un Llama miniature
   (`essai-crochets-causal_lens-llama-v1.py` de B-α, repris) ; contrôles de B0 des trois fichiers de Neuronpedia (31 couches contiguës,
   garde (e)) ; `01_lens_corpus.py` ; garde (i) sur sa provenance ; contrôles de P.1 par `lens_docs` et `rows_sha256` du dépôt sur la
   machine (932, 466/466, `a6afd972…`) ; **banc** : deux documents par lentille, le second chronométré (le premier compile) ; au-delà de
   23,6 s par document, l'ajustement ne part pas ; compte rendu sans arrêt au-delà de 14,2 s (devis v12, § 5).
2. **B1, ajustement** : R puis S, moitiés paire et impaire dans le même passage. **Reprise sur point de sauvegarde** : la reprise du
   dépôt ne compare pas l'empreinte du corpus (`02_fit.py` l. 151 ; inventaire, repli 1) ; avant toute relance, notre code lit le point
   de sauvegarde (garde (q)). À la fin de chaque ajustement : gardes (g) et (h), différences entre moitiés non arrondies, empreinte du
   fichier → **export** de notre R depuis le fichier `-T128` (entière, moitié paire, moitié impaire) ; gardes (e), (h), (n) et (o) sur
   les exports. Les liens durs du correctif (5) **ne sont pas encore posés** (contre-lecture du brouillon 2, M-1).
3. **B2, corpus d'activations, comptes de jetons, passe** : `05_act_corpus.py` (révisions imposées comme en B-α, correctif (6)) ; garde
   (i) de nouveau ; `03_token_counts.py`, joué **une seule fois** ; jetons gardés de Llama (`catalog.kept`, comptes ≥ 5 dans le corpus
   d'activations, décodage sans « � ») : nombre et empreinte de la liste versés à l'addendum, la même empreinte exigée avant chaque
   étape qui lit `kept()` (garde (r)) ; **puis** l'accord du premier jeton de B-1 (`lens_compare.py`, correctif (4)) —
   après les comptes de jetons, dont il dépend (contre-lecture, M-2) ; garde (k) (`hub` attendu) ; fumée `06_activations.py --docs 64` ;
   passe complète (refaite : les tables de B-α ont été détruites avec ses machines).
4. **B3, pilotes** : garde (k) (`hub` attendu) ; `07_drivers.py` (sa table est lue sans condition par `reads_at_firings.py`) ; garde (p). **Les lectures par les
   poids (`08_reads.py`) ne sont pas jouées** : aucune mesure de ce texte ne les lit (la partie « neurones » de `reads_at_firings.py`
   recalcule ses lectures depuis les lentilles ; inventaire, dépendances) ; écart au devis v12, § 1, déclaré (contre-lecture, m-12).
5. **B4, lecture contre pilotage et ablation** : `measure` au lot 64 ; garde (p) ; `score` (lentilles en P.2). Les moitiés de notre R
   servent seulement à l'audit A6 ; le seuil de `pass` est calculé par cible et par lentille (`causal_lens.py` l. 325) : les noter ne
   change aucune valeur des autres lentilles. Gardes (a) à (c), (e), (j), (n) ; n recalculé.
6. **B5, lecture côté entrée** : **liens durs du correctif (5)** posés seulement maintenant ; gardes (k) (nos deux noms attendus), (r) et
   (s) ; `checks/reads_at_firings.py --parts neurons`.
7. **B6, verdicts sur la machine** (contre-lecture, bloquante 2) : notre code des verdicts (P.4) évalue toutes les chaînes en défaut,
   tous les déclencheurs d'audit et tous les seuils ; il **joue sur la machine** chaque audit déclenché (« Critères de lecture gelés »),
   dans le temps réservé (1 h, devis v12, § 4) et sous les gardes de dépense ; les gardes (a) à (c) s'appliquent aussi à la sortie de
   `score` de la graine 1 (étiquette `--tag b-beta-graine1`), et un défaut y est une chaîne en défaut ; il écrit un fichier de verdicts unique (verdict
   d'ensemble, verdict de chaque mesure, audits déclenchés et leur issue). La fille ne lit aucun résultat ; le lecteur neuf relit plus
   tard ces verdicts sur les sorties versées, sans rien recalculer qui demande les lentilles.
8. **B7, versement puis destruction** : manifeste (R9) ; sorties versées avec leurs compagnons (P.6) ; **lentilles non rangées** (lieu
   L1 : elles disparaissent avec la machine) ; destruction par identifiant (R10), absence prouvée.

### P.4 Code des verdicts essayé (R5), avant la course
Le code qui applique les seuils, les chaînes en défaut, les déclencheurs et les règles de sortie des audits est passé, avant la course,
sur les cas suivants ; résultats consignés ; tout écart à l'attendu arrête la course.

| cas | données | attendu |
|---|---|---|
| (i) référence | `causal_lens_qwen3-8b.json` ramené à 32 couches par ⌊l × 36/32⌋ (« R:dclm » dans le rôle de notre R et de `npR` ; « J » dans celui de J et `npJpp` ; n = 64) ; `reads_at_firings_qwen3-8b.json` pour B-5 ; B-1 par les moitiés factices saines de (vi) ; série repère (garde (j)) remplacée par les valeurs de `npR` du même fichier | B-1, B-2, B-3, B-5, B-7 « reproduit » ; B-6 écart nul à toutes les couches, donc « accord » (aucun audit) ; garde (n), évaluée sur des matrices factices distinctes : non déclenchée ; aucune autre chaîne en défaut ; aucun autre déclencheur ; B-5 lisible (part silencieuse 0,000 et 0,240) ; valeurs de B-5 : 0,8481, 0,2248, 0,0271, 0,1977 à 10⁻⁴ près ; **verdict d'ensemble « reproduit avec nos lentilles »** |
| (ii-a) | `pass` de notre R (« steer 1x ») mis à 0,40 aux couches 16 à 27 | B-2 « non reproduit » ; B-3, B-7 « reproduit » ; verdict « non reproduit avec nos lentilles », réserve « défaut dans notre lentille » écrite |
| (ii-b) | `control_med` de notre R (« steer 1x ») mis à 0,20 à la couche 10 | chaîne en défaut (a) ; aucun verdict de mesure |
| (ii-c) | `r_med` de notre R remplacé par celui des logits, toutes cibles | chaîne en défaut (e) ; aucun verdict de mesure |
| (ii-d) | contrôle sur une lentille factice dont la matrice de la couche 10 est l'identité | chaîne en défaut (e) avant `score` |
| (ii-e) | contrôle sur une lentille R factice de 30 couches `out` | chaîne en défaut (h) |
| (iii-a) | `read_S` de la couche 0 mis à 0,25 | B-5 « non reproduit » ; verdict « partiel » |
| (iii-b) | moyennes des bandes 1–7 et 12–23 de `read_S` rendues égales | B-5 « non reproduit » ; verdict « partiel » |
| (iii-c) | part silencieuse de la couche 0 mise à 0,45 | B-5 « non lisible » ; verdict « partiel » |
| (iii-d) | `read_S` mis à 1,00 à la couche 0 | déclencheur A4 ; avec une permutation saine simulée (2 points fixes), B-5 inchangée ; avec la permutation identité, chaîne en défaut (m) |
| (iii-e) | `read_S` mis à 0 à toutes les couches | déclencheur A4 ; mêmes deux issues que (iii-d), B-5 « non reproduit » dans la première |
| (iv-a) | écart de B-6 porté à 0,20 à la couche 10 | B-6 « désaccord » ; audit A6 déclenché ; avec moitiés factices à 0,02 de notre R : réserve « écart de corpus » écrite, verdicts inchangés ; avec une moitié à 0,10 de notre R à la couche 10 : réserve « écart d'ajustement » écrite, verdicts inchangés |
| (iv-b) | matrices factices de notre R égales à celles de `npR` à une couche | chaîne en défaut (n) |
| (v) | `r_med` de notre R mis à 0,96 à la couche 3 | déclencheur A1 ; avec témoin et normes sains simulés et une seconde graine qui garde les verdicts : verdicts inchangés ; avec une seconde graine qui change B-2 : B-2 « autre » ; avec un pôle témoin égal à son pôle : chaîne en défaut (l) ; avec l'audit « non joué » simulé : verdict « non conclu » |
| (vi-a) B-1 sain | différences factices 0,05 partout, accords 0,90 | B-1 « reproduit » |
| (vi-b) | une couche `out` de R à 0,25 | B-1 « non reproduit » ; audit A3 déclenché ; avec comptes et empreintes sains simulés : « non reproduit » maintenu ; avec 465 et 467 documents : chaîne en défaut (g) ; verdict d'ensemble « partiel » dans le premier cas |
| (vi-c) | accord 0,50 à la couche 12 | B-1 « non reproduit » ; audit A3 comme (vi-b) ; verdict d'ensemble « partiel » |
| (vi-d) | différence factice 0,0 à une couche (moitiés identiques) | déclencheur A2 ; avec sommes des moitiés égales : chaîne en défaut (g) |
| (vi-e) | accords 1,00 aux six couches | déclencheur A2 ; avec moitiés distinctes simulées : B-1 inchangée |
| (vii) | `r_med` de `npR` de cette course écarté de 0,06 de la série repère à trois couches | chaîne en défaut (j) |
| (viii) | `arch.fits` simulé rendant `hub` juste avant `reads_at_firings.py` | chaîne en défaut (k) |
| (viii-b) | lentille exportée factice rendant `None` à la couche 12, puis une autre écartée de 1 % de la moyenne du fichier d'ajustement à la couche 5 | chaîne en défaut (o), deux fois |
| (viii-c) | `meta["contexts"]` de `measure` mis à 15 | chaîne en défaut (p) |
| (viii-d) | point de sauvegarde factice de `next_doc` 400 pour `docs` 932 | chaîne en défaut (g) |
| (ix) | un identifiant de la provenance d'ajustement recopié dans la provenance des activations | chaîne en défaut (i) |
| (x) | `r_med` « ablate win » de notre R mis à 0,45 aux couches 8 à 13 | B-7 « non reproduit par le haut » ; audit A5 déclenché ; avec une seconde graine qui le confirme : maintenu ; sinon B-7 « autre » ; dans les deux cas, verdict d'ensemble inchangé, « reproduit avec nos lentilles » (B-7 n'y entre pas) |
| (xi) | B-2 et B-3 « non reproduit » avec notre R, garde (j) tenue | verdict « non reproduit avec nos lentilles », réserve « défaut dans notre lentille » écrite |

**Branches des gardes, chacune avec son artefact** (contre-lecture du brouillon 2, m-5) ; le cas sain de chacune est le cas (i) :

| garde | artefact | attendu |
|---|---|---|
| (d) | un test d'un essai marqué sauté ; un estimateur faussé (signe d'un terme inversé dans une copie de l'essai) | chaîne en défaut (d), deux fois |
| (f) | Llama miniature dont une matrice estimée est perturbée de 10⁻³ | chaîne en défaut (f) |
| (g) | différence entre moitiés `nan` ; matrice avec un `inf` ; `full_length` faux ; un document de 127 jetons | chaîne en défaut (g), quatre fois |
| (h) | lentille S factice de 31 couches | chaîne en défaut (h) |
| (i) | provenance d'ajustement à une autre révision ; deux identifiants permutés ; `skip` 999 ; un texte d'ajustement recopié sous un autre identifiant dans le corpus d'activations | chaîne en défaut (i), quatre fois |
| (j) | cas limite sain : écart de 0,06 à deux couches ; artefact : 0,11 à une couche | rien ; puis chaîne en défaut (j) |
| (k) | `arch.fits` rendant nos noms avant la passe d'activations ; empreinte du fichier lié différente de celle de l'ajustement | chaîne en défaut (k), deux fois |
| (l) | un pôle retenu de pilotage de norme nulle (audit A1 simulé) | chaîne en défaut (l) |
| (p) | `07_drivers.py` simulé avec 3 documents de la tranche DCLM | chaîne en défaut (p) |
| (q) | fichier `-T128` présent avant le premier lancement ; point de sauvegarde de `rows_sha256` altéré | chaîne en défaut (q), deux fois, avant l'ajustement ou la relance |
| (r) | liste `kept()` altérée d'un jeton avant `lens_compare.py` | chaîne en défaut (r) |
| (s) | fichier `reads_at_firings-llama-3.1-8b-instruct.pt` présent | chaîne en défaut (s) |
| A1 | `control_med` de notre R (« steer 1x ») écrit `0.0` à deux couches ; le même à une seule couche ; deux zéros en « ablate pos » de J seulement | déclencheur ; rien ; rien |
| rangs 2 et 3 | audit A3 « non joué » simulé **et** B-2 « non reproduit » | verdict « non conclu » (le rang 2 prime) |

Les gardes du montage (banc, empreintes, rangées du corpus, plafonds, version de Drowse) sont essayées dans la commande, chacune sur un
cas sain et un artefact (R5) : banc à 11,5 s (part), 15 s (compte rendu, part), 24 s (arrêt) ; `rows_sha256` altéré d'un caractère
(arrêt) ; 931 documents (arrêt) ; dépense simulée à 45,0 et à 67,5 USD ; empreinte de Drowse altérée (arrêt).

### P.5 Graines (R9) (contre-lecture, m-7)
- Neurones de `measure` et de `score` : `random.Random(0)` du dépôt (comme publié) ; graine 1 seulement pour les audits A1 et A5, par le
  correctif (3), qui fait recevoir la même graine à `sample_neurons` et à `score`.
- Paires mal appariées de `reads_at_firings.py` : `torch.Generator().manual_seed(0)` (l. 133), inchangée.
- `07_drivers.py` : `torch.randperm` à la graine 0 (l. 60-63 : ordre de balayage et départage des égalités), inchangée.
- Contrôle de norme de `rules._check_norm` (l. 96) : tirage sans graine, contrôle à tolérance seulement, sans effet sur les sommes
  (déclaré).
- Toute autre graine (rééchantillonnage des intervalles, une branche par mesure dans l'ordre B-2, B-3, B-4, B-6, B-7 ; tirages de
  notre code) par `numpy.random.SeedSequence(entropy=20261118)`, branche « B-β », `spawn` par tâche, consignée au manifeste.
- L'ajustement lui-même est déterministe à l'ordre des documents près (aucun tirage) ; `lens_compare.py` n'échantillonne rien avec
  `--samples 0`.

### P.6 Sorties calculées et versées avant la destruction (lieu L1 ; contre-lecture, bloquante 2)
Calculées sur la machine, versées avec leurs compagnons `.sha256` sur la branche de résultats, puis vérifiées par empreinte **avant**
la destruction : différences entre moitiés non arrondies (deux lentilles, toutes cibles et couches) ; comptes de documents par moitié et
longueurs ; `rows_sha256` et provenances du corpus d'ajustement ; empreintes des deux fichiers d'ajustement et des trois exports de
notre R ; contrôles des matrices (identité, égalité à `npR`, nombre de couches) ; sortie non arrondie de `lens_compare.py` ; jetons
gardés de Llama (nombre, empreinte de la liste) ; sortie JSON de `score` (toutes lentilles notées) ; n recalculé et pôles écartés par
motif ; empreinte du fichier `-causal.pt` (≈ 2 Gio, non versé) ; sortie JSON de `reads_at_firings.py` avec la part silencieuse ;
empreintes et résumé de `07_drivers.py` ; compte et rang du jeton de début dans les jetons gardés ; contrôles de B0 ; audits joués et leurs sorties ; **fichier des verdicts**
de P.3, étape 7 ; journaux ; manifeste (R9). Rien d'autre ne survit à la machine ; aucun audit ne se rejoue après la destruction sans
devis neuf.

### P.7 Lecture
Les résultats sont lus par un lecteur neuf, sur un plan de lecture scellé avant toute ouverture des résultats ; la fille ne lit aucun
résultat avant ce verdict. Le lecteur applique ce texte aux sorties versées (P.6) et compare son verdict à celui du fichier des
verdicts : un désaccord est rapporté et tranché par un second lecteur neuf, sans nouvelle mesure. Comparaisons multiples : les verdicts
sont des règles de seuils couche par couche, sans test d'hypothèse ; aucune correction n'est appliquée, et les intervalles sont
rapportés sans servir au verdict (comme en B-α).

## Critères de lecture gelés

### Verdict d'ensemble — un seul, par ordre de priorité
| rang | issue | verdict |
|---|---|---|
| 1 | une chaîne en défaut ((a) à (s)) | **chaîne en défaut** ; aucun verdict de mesure ; nœud à la mère |
| 2 | un audit déclenché qui porte sur B-1, B-2, B-3 ou B-5 n'a pas pu être joué jusqu'à son issue avant la destruction (temps réservé épuisé, garde de dépense, perte de machine) | **non conclu** ; verdict final de la tranche ; les mesures non touchées sont rapportées telles quelles ; aucune reprise sans devis neuf et mot de Lazar |
| 3 | B-2 ou B-3 « non reproduit » | **non reproduit avec nos lentilles** — rapporté à l'identique (R3) ; la garde (j) ayant tenu, la chaîne n'a pas changé depuis B-α (qui a reproduit B-3 avec la lentille R publique, et rendu B-2 « autre ») : réserve « défaut dans notre lentille » écrite **dès qu'une seule des deux mesures** est « non reproduit », lue avec B-6 |
| 4 | B-1, B-2, B-3 et B-5 « reproduit » | **reproduit avec nos lentilles** |
| 5 | autre | **partiel**, mesure par mesure |

B-4 et B-6 n'entrent pas dans le verdict d'ensemble ; B-7 se lit à part (ci-dessous). Un « reproduit » dira que la lentille lit ce
qu'une direction **pousse en moyenne**, pas qu'elle nomme le concept d'une invite donnée (texte gelé v6).

### B-6 et l'audit des deux codes (A6)
B-6 se lit à part : « accord » dit que les deux codes s'accordent ; « intermédiaire » est rapporté ; « désaccord » déclenche l'audit
A6, joué sur la machine avec les sorties de `score` déjà calculées (moitiés notées à l'étape 5) : si, à chaque couche de 0 à 27 où
l'écart dépasse 0,15, les deux moitiés sont toutes deux à moins de 0,05 de notre R entière, l'écart est attribué au corpus et à la
taille de l'ajustement (932 documents de DCLM contre 64 de WikiText) : réserve « écart de corpus » ; sinon réserve « écart
d'ajustement » (notre lentille n'est pas stable là où elle s'écarte). **Aucun verdict n'est suspendu** : B-6 ne change ni B-2, ni B-3,
ni B-4, ni B-7 ; la réserve accompagne le verdict d'ensemble. L'égalité exacte des deux lentilles est la garde (n).

### B-7, pour un moniteur (lectures du texte gelé v6, règles de sortie ajoutées)
| issue | lecture |
|---|---|
| « reproduit » | là où `r_med` est bas, une étiquette de neurone décrit une poussée moyenne et ne sert pas à lire un épisode, avec notre lentille comme avec la publique |
| « non reproduit » par le haut | audit A5 ; s'il confirme, rapporté comme lecture valable en contexte plus tôt que publié ; sinon B-7 « autre » |
| « non reproduit » par le bas | rapporté : la lecture ne dit pas ce qu'une activation fait, même tard |
| autre | couche par couche |

### Audits symétriques (R4), tous joués sur la machine avant la destruction, chacun à issue fermée
| audit | déclencheur | contenu (sur la machine) | issues |
|---|---|---|---|
| **A1, trop beau, lecture contre pilotage** | notre R, « steer 1x » : `r_med` ≥ 0,95 à une couche 0–7, ou `control_med` écrit égal à 0 (`0.0` ou `-0.0`, à 4 décimales) à au moins 2 couches de 0 à 27 | (1) chaque pôle a un témoin distinct de lui ; (2) chaque pôle retenu a un pilotage de norme non nulle (fichier `-causal.pt`) ; (3) `measure` relancé avec la graine 1 (correctif (3)), puis `score` avec les lentilles `logit,npR,R:dclm-llama` (`--tag b-beta-graine1` ; les logits et `npR` servent aux gardes (a) à (c), et les logits à B-3) ; gardes (a) à (c) sur cette sortie | (1) ou (2) manqué, ou garde (a) à (c) manquée sous la graine 1 → chaîne en défaut (l) ; sinon les verdicts de la graine 0 tiennent, sauf pour toute mesure parmi B-2, B-3, B-7 dont le verdict diffère sous la graine 1, qui devient « autre » ; les valeurs des deux graines sont rapportées |
| **A2, trop beau, stabilité** | différence entre moitiés non arrondie < 10⁻⁶ à une couche d'une cible, ou accord du premier jeton égal à 1 aux six couches | moitiés distinctes : comptes 466 et 466, empreintes des lignes des moitiés (`4a31baec…`, `ef95a60c…`), sommes des moitiés différentes (écart maximal > 0), exports des moitiés d'empreintes différentes | un contrôle manqué → chaîne en défaut (g) ; sinon B-1 tient (une valeur très petite est conforme à la référence : 0,00 imprimé pour S, `mid`) |
| **A3, tout négatif, stabilité** | B-1 « non reproduit » | mêmes contrôles que A2, plus : chaque document de 128 jetons, `full_length` vrai | un contrôle manqué → chaîne en défaut (g) ; sinon « non reproduit » tient |
| **A4, B-5 aux extrêmes** | `read_S` ≥ 0,99 à la couche 0 (trop beau), ou `read_S` = 0 à toutes les couches 0 à 31 (tout bas) | permutation des paires mal appariées non dégénérée (au plus 10 points fixes par couche ; attendu ≈ 2) ; fichier de lentille S lu égal à celui de l'ajustement (garde (k)) ; part silencieuse rapportée | un contrôle manqué → chaîne en défaut (m) ou (k) ; sinon B-5 tient telle que calculée (règle de lisibilité comprise) |
| **A5, B-7 par le haut** | B-7 « non reproduit » par le haut | contrôles (1) et (2) de A1 ; `measure` et `score` à la graine 1 (une seule relance si A1 est aussi déclenché) | contrôle manqué → chaîne en défaut (l) ; graine 1 aussi « par le haut » → maintenu ; sinon B-7 « autre » |
| **A6, deux codes** | B-6 « désaccord » | sorties de `score` des deux moitiés (déjà calculées) | réserve « écart de corpus » ou « écart d'ajustement » (ci-dessus) ; aucun verdict changé |
| **tout négatif, reproduction** | B-2 ou B-3 « non reproduit » avec notre R | aucun calcul neuf : la garde (j), toujours évaluée, est le cas sain de la chaîne (la lentille R publique, notée dans la même sortie de `score`, retrouve la série repère) | (j) manquée → chaîne en défaut ; (j) tenue → rang 3 et sa réserve (même règle, écrite une seule fois) |

Ce dernier audit **change** celui du brouillon 1 et du texte gelé v6 (rejeu sur Qwen3-8B) : déclaré (écarts, 7). Les audits A1 et A5
partagent une seule relance de `measure` à la graine 1 (≈ 18 min et `score` ≈ 1,5 min sur A100). Si le temps réservé (1 h) ou une garde
de dépense empêche de finir un audit, son issue est « non joué » et la règle de rang 2 s'applique (s'il porte sur B-7 seul : B-7
« autre »).

## Liste d'arrêt

| condition | action |
|---|---|
| ce texte non scellé ; un correctif employé non contre-lu ou non scellé ; le code des verdicts non essayé (P.4) ou en écart à l'attendu | rien ne part (R1, R2) |
| pas de ligne de calcul inscrite par la mère sur GO-2026-11-18-02, pas de feu écrit, commande non contre-lue | rien ne part |
| plafond de la ligne : **75 USD** (GO-2026-11-18-02) ; échéance de la ligne dépassée sans course (fenêtre du 19 au 25 novembre ; échéance de la ligne telle qu'inscrite par la mère) | rien ne part ; la ligne tombe sans dépense |
| clé d'accès au modèle : passer une clé à la machine sans le mot explicite de Lazar au moment de la commande (R-3151) | rien ne part ; aucune clé passée à une machine |
| pas de relevé de prix dans l'heure qui précède la création, ou prix lu au-dessus de 2,62 USD/h stockage compris, ou trafic au-dessus de 0,04 USD/Go | rien ne part ; ou destruction immédiate par identifiant |
| addendum des empreintes non scellé avant la première passe (révision de Llama, provenances et identifiants du corpus d'ajustement et du corpus d'activations, fichiers de Neuronpedia, jetons gardés de Llama) | rien ne part |
| gardes recalculées pour ce plafond et le lieu L1, par les formules du devis v12 (§ 5) : **compte rendu à 45,0 USD** (60 %) ; **arrêt dur à 67,5 USD** (90 %) ; trafic réservé 1,0 USD ; minuterie = (67,5 − 1,0) / prix lu, tronquée à la seconde (au prix exigé exact : 91 374 s, soit 25,38 h) ; prix minimal de la règle du refus de la minuterie (67,5 − 1,0) / 36 = 1,85 USD/h (sous lui, offre écartée, sauf armement à la borne haute tranché dans la commande) ; compte rendu en durée à 12,9 h (haut de l'attendu avec L1), rappel à 24,1 h (pire cas avec L1) ; crédit ; course figée ; perte de machine | selon le devis : compte rendu, arrêt et destruction par identifiant, nœud à la mère ; la commande recalcule et écrit chaque valeur |
| banc de B0 au-delà de 23,6 s par document (second document) | l'ajustement ne part pas ; destruction ; compte rendu |
| à B0, nombre de documents d'ajustement différent de 932, moitiés différentes de 466 et 466, ou `rows_sha256` différent de `a6afd972…` | l'ajustement ne part pas ; destruction ; nœud à la mère |
| toute chaîne en défaut constatée avant `measure` (en particulier (d) à (i), (k), (n) à (s)) | arrêt ; versement de ce qui existe ; destruction ; compte rendu |
| Drowse d'une autre version que 6.1.4 ou d'une autre empreinte que `673ed2b4…` sur la machine | rien ne part ; ou arrêt avant l'export |
| empreinte d'un fichier différente de celle écrite ici ou à l'addendum ; licence différente | arrêt ; message à la mère |
| tout écart de notre code à ce texte, découvert en course | arrêt ; écart écrit avant toute suite |
| toute lecture touchant P3, P3b, T0.6, T0.7, P3-bis ou un chemin interdit (contre-lecture, m-13) | interdit ; arrêt |
| tout refus d'une permission, du crochet ou du classifieur | ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère |
| envie d'écart à ce texte | écrit, daté, nouvelle version (R12), contre-lu, avant d'être fait |

**R5** : chaque garde codée — chaînes en défaut (a) à (s), empreintes, rangées du corpus, plafonds, banc, version de Drowse, code des
verdicts et règles de sortie des audits — est essayée avant la course sur un cas sain
et sur un artefact (P.4 et commande) ; résultats consignés ; aucun repli silencieux.

### Écarts déclarés (au code publié, au plan v1 et v2, au devis v12, au texte gelé v6, au brouillon 1) (contre-lecture, m-11)
1. **Corpus d'ajustement** : documents pleins de 128 jetons des lignes 0 à 999 (932) au lieu des 1 000 lignes du défaut publié ;
   option publiée `--full-length` ; 1 864 passages au lieu de 2 000 (devis v12, § 1 et § 4, qui disaient 1 000 documents) ; effets en P.1.
2. **Fichier d'ajustement** au suffixe `-T128`, rendu visible à `arch.fits` par le correctif (5).
3. **B-1** : différence entre moitiés recalculée non arrondie ; accord sur six couches par une seconde règle de profondeur ; pôles et
   non neurones ; moitiés de 466 documents.
4. **B-5 réécrit** (moyennes de bandes au lieu de la monotonie) et **règle de lisibilité** par la part silencieuse.
5. **B-6** : quantificateur écrit ; **plus de suspension** des verdicts (le plan v1 disait « ouvre un audit », le brouillon 1
   suspendait B-2, B-3 et B-6) : audit A6 à issue fermée, réserve sans changement de verdict.
6. **Verdicts et audits sur la machine, avant la destruction** ; issue « non conclu » ajoutée au verdict d'ensemble (rang 2) ; règles de
   sortie fermées pour chaque audit.
7. **Audit « tout négatif » de la reproduction** : remplacé par la garde (j) (lentille R publique contre la série repère de B-α),
   évaluée à chaque course ; le texte gelé v6 rejouait `measure` sur Qwen3-8B.
8. Gardes neuves (f) à (s) ; garde (c) étendue à notre R ; garde (d) étendue aux correctifs (3) à (6) ; gardes (o) à (s) neuves (inventaire et contre-lecture du brouillon 2) ; liens durs du correctif (5) posés seulement avant
   `reads_at_firings.py`, la passe d'activations gardant la branche `hub` de B-α.
9. **Lentilles non rangées** (lieu L1, GO-2026-11-18-02).
10. Prédictions : B-4 en deux lignes, signes motivés par B-α ; B-2 et B-5 chiffrées ; colonne « réfutée si ».
11. **Lectures par les poids (`08_reads.py`) retirées** des étapes (devis v12, § 1 et § 4, étape B3 ; aucune mesure ne les lit) ; jeton de début de Llama gardé dans
   les documents et dans les jetons gardés, comme publié, et rapporté.

### Provenance des chiffres (R6, R7)
| chiffre | source | clé |
|---|---|---|
| garde (c) : R publiée 0,9845 à 0,9923, logits 0,9354 à 0,9565 aux couches Qwen3 31 à 33 (⌊l × 36/32⌋, l = 28 à 30) | `causal_lens_qwen3-8b.json` (`8904c4d3…`) ; recalculés par le vérificateur du brouillon 3 | `["steer 1x"]["R:dclm"/"logit"]["r_med"]` |
| stabilité publiée : R 0,04 à 0,06 (couches 0–18), 0,03 (19–22), 0,02 (23–27), ≤ 0,01 dès 28 ; S 0,00–0,05 (`mid`), 0,01–0,05 (`out`) ; accord 0,89 à 0,99 ; mode commun 0,78 à la couche 2 | `docs/findings.md` voisin (`8814874b…`), l. 49-62 et 71-74 | — |
| `read_S` 0,848, 0,248, 0,090, 0,229, 0,352 ; 0,8481, 0,2248, 0,0271, 0,1977 ; part silencieuse 0,000, 0,564, 0,608, 0,421, 0,089, 0,001 | `reads_at_firings_qwen3-8b.json` (`ac0bf101…`) | `["neurons"]["layers"][i]["read_S"]`, `["silent"]` |
| seuils et attendus de B-2, B-3, B-7 sur la référence | `causal_lens_qwen3-8b.json` (`8904c4d3…`) ; texte gelé v6 | `targets[…]` |
| B-α : B-3 « reproduit » (couche 4 à 0,2085) ; B-2 « autre » (`r_med` 0,3883 couche 8 ; `pass` 0,7656 et 0,8750 couches 8 et 10) ; B-4 face à J négatif à 19 couches sur 20, face à J++ positif à 20 sur 20 ; B-7 ≤ 0,185 couches 0–14, 0,3097 couche 15, ≥ 0,805 couches 26–29 | verdict de B-α (`ca06acb1…`) | — |
| effet du matériel jusqu'à 0,03 entre deux cartes (plus grand écart 0,0296 ; 0,0206 pour la lentille R publique en « steer 1x », couche 8) | verdict de la recourse au lot 64 (`95b09fca…`), l. 197-215, vérifié par le contre-lecteur du brouillon 2 | — |
| lots 16 et 64 identiques au bit sur A100 | verdict de la recourse au lot 64 (`95b09fca…`), l. 14-15 | — |
| 932 documents pleins, 68 courts (44 longueurs), 466/466, 104 384 et 109 553 jetons au-delà des 16 premiers, aucun identifiant commun ; positions 103 452 et 108 553 **dérivées ici** (104 384 − 932 ; 109 553 − 1 000) | `comptes-corpus-ajustement-b-beta-v1.json` (`d86ddf4d…`) | — |
| `rows_sha256` attendus | `comptes-rows-sha256-b-beta-v1.json` (`ebc557e3…`) | — |
| 23,6 s, 14,2 s, 13,1 h ; 45,0, 67,5, 1,0 USD ; 12,9 h, 24,1 h ; recompilations de 15 à 37 s | devis v12 (`41a4c1f6…`), en-tête, §§ 4 et 5 | — |
| 91 374 s, 1,85 USD/h | calculés ici : (67,5 − 1,0) / 2,62 × 3 600 = 91 374,05 ; (67,5 − 1,0) / 36 = 1,847 | — |

## Contre-lecture

Le brouillon 1 a été contre-lu (`4d52c0be…`) : « à corriger », 2 bloquantes, 6 majeures, 13 mineures. Reprise point par point :

| point | traitement | lieu |
|---|---|---|
| bloquante 1 (corpus d'ajustement débordant sur les contextes) | acceptée : lignes 0 à 999 seulement, documents pleins par `--full-length` (932), comptés avant scellement ; garde (i) « identifiant commun » ; effets sur B-1 déclarés ; règle de longueur écrite comme le code la compte (jeton de début compris) | P.0, P.1, (i), écarts 1 |
| bloquante 2 (audits sans issue, injouables après destruction) | acceptée : verdicts et audits sur la machine, avant destruction ; chaque audit à issue fermée ; rang « non conclu » ; plus aucune suspension ; sorties listées | P.3 (7, 8), P.6, « Critères », écarts 5 et 6 |
| M-1 (arrondi à deux décimales ; « exactement nul ») | acceptée : différences recalculées non arrondies ; accord non arrondi par le correctif (4) ; déclencheur A2 à < 10⁻⁶ | M.2, A2 |
| M-2 (ordre, `kept()`, Drowse, couches) | acceptée : comparaison après les comptes de jetons ; correctif (4) étendu à `kept()` et au périphérique ; Drowse épinglé ; ligne de commande écrite | P.2, P.3 (3) |
| M-3 (part silencieuse dans `read_S`) | acceptée : définition exacte ; part silencieuse rapportée ; règle « non lisible » | M.2 |
| M-4 (repli `hub`) | acceptée : garde (k) ; correctif (5) (liens durs) ; essai (viii) | (k), P.2, P.4 |
| M-5 (inventaire avant scellement) | acceptée : inventaire fait et versé ; liste des correctifs fermée ; arguments imposés écrits ; gardes (o) et (p) neuves | P.2, (o), (p) |
| M-6 (audits R4 et essais R5 manquants) | acceptée : A2 à A5 et garde (n) ; essais (iii-c) à (iii-e), (iv-b), (v) à (x) ; gardes du montage essayées dans la commande | « Critères », P.4 |
| m-1 (75 USD, gardes recalculées) | acceptée | liste d'arrêt |
| m-2 (seconde règle de profondeur) | acceptée : déclarée, usage unique | M.2 |
| m-3 ((h) et (g)) | acceptée : (h) reformulée par lentille ; (g) étendue (comptes, longueurs, `rows_sha256`, `next_doc`) | (g), (h) |
| m-4 (« réfutée si », B-2 et B-5 chiffrées, B-4 en deux lignes) | acceptée | prédictions |
| m-5 (mesures refaites de B-α) | acceptée : phrase écrite | « Hypothèse » |
| m-6 (valeurs ≈, verdict attendu de l'essai (i), table des attendus) | acceptée : 0,8481, 0,2248, 0,0271, 0,1977 à 10⁻⁴ ; verdict attendu écrit ; table réécrite avec les libellés de ce texte | « Seuil », P.4 |
| m-7 (graines) | acceptée | P.5 |
| m-8 (pôles ; mode commun) | acceptée : « pôles » ; accord de chaque moitié avec la lentille publique rapporté comme repère | M.2 |
| m-9 (moment du contrôle d'identité ; couche 31 ; (d) ; crochets) | acceptée | (d), (e), M.1, P.3 (1) |
| m-10 (rejeu inutile ; série repère non nommée) | acceptée : garde (j) avec la série repère nommée et empreintée, évaluée à chaque course | (j), table des documents, écarts 7 |
| m-11 (écarts, provenance, R-3093, tolérance de (f)) | acceptée | sections « Écarts » et « Provenance », (f), P.2 |
| m-12 (étiquettes ; conditionnel ; `08_reads.py` ; mentions « brouillon ») | acceptée : M.n et P.n ; fait écrit ; `08_reads.py` retiré ; mentions et nom de fichier changés au scellement (R12) | partout |
| m-13 (ligne P3 de la liste d'arrêt) | acceptée | liste d'arrêt |

Le brouillon 2 a été contre-lu (`contre-lecture-texte-gele-tranche-b-beta-v1-brouillon2.md`, `9d591aafa9fde21887105167ff65b927cf0ef9f0fdf62bfd387af4103b926dbb`,
sur le brouillon `a5f438df…`) : « à corriger », 0 bloquante, 2 majeures, 17 mineures ; bloquantes du brouillon 1 levées ; vérification
de la mère (rien ne dépendait des 1 000 documents) faite. Reprise :

| point | traitement | lieu |
|---|---|---|
| M-1 (la passe d'activations prendrait la branche jamais jouée de `head_tables`) | acceptée : liens durs posés seulement avant `reads_at_firings.py` ; garde (k) exige `hub` pendant la passe et les pilotes | (k), P.3 (2, 3, 4, 6), écarts 8 |
| M-2 (rang 1 jusqu'à (n) ; « trop beau de B-6 » inexistant ; liste d'arrêt et R5 incomplètes) | acceptée : « (a) à (s) » ; cas (i) réécrit ; liste d'arrêt et R5 complétées | « Critères », P.4, liste d'arrêt |
| m-1 (« réfutée si » ≠ contraire de la prédiction) | acceptée : contraire exact ; B-4 à « au moins 11 des 20 » | prédictions |
| m-2 (2 à 4 % ; bornes en durée) | acceptée | P.1 |
| m-3 (banc au même nom que l'ajustement) | acceptée : copie à part de l'arbre ; garde (q) | (q) |
| m-4 (trois règles non nommées) | acceptée : gardes (q), (r), (s) | « Seuil », P.3 |
| m-5 (branches sans artefact) | acceptée : table des branches | P.4 |
| m-6 (« ou » contre « et » pour la réserve) | acceptée : une seule règle, au rang 3 ; (ii-a) attend la réserve | « Critères », P.4 |
| m-7 (A1 : cible, chaînes en défaut sous la graine 1, étiquette) | acceptée | A1, P.3 (7) |
| m-8 ((k) nomme `08_reads.py` ; moyen d'observer) | acceptée | (k) |
| m-9 (Drowse : version, licence, interface) | acceptée : 6.1.4, AGPL-3.0-or-later, empreinte ; `jlens.py` et `store.py` lus ; arrêt sur autre version | P.2, table des documents, liste d'arrêt |
| m-10 (identifiants seulement ; parité) | acceptée : empreintes des textes ; phrase sur le rang | (i), P.1 |
| m-11 (libellé « positions ») | acceptée | provenance |
| m-12 (numéros de ligne) | acceptée | P.0, P.2 |
| m-13 (« 64 premiers documents ») | acceptée | M.2 |
| m-14 (moment de (i)) | acceptée | (i) |
| m-15 (empreintes, compagnon, « niveau citation ») | acceptée : empreinte de l'essai d'invariance ; compagnon du brouillon 2 posé ; renvoi au verdict de la recourse | documents, provenance |
| m-16 ((c) étendue à notre R) | acceptée : gardée, justifiée | (c) |
| m-17 (forme ; verdicts d'ensemble attendus) | acceptée : B6 et B7 ; attendus de (vi-b), (vi-c), (x) | P.3, P.4 |

Le brouillon 3 (`texte-gele-tranche-b-beta-v1-brouillon3.md`, `c6a6b00eca055ac38221cdf71d97ada8b71c51c82429c2d7f514d8f040cefb47`) a été
vérifié par un sous-agent neuf : `verification-texte-gele-tranche-b-beta-v1-brouillon3.md`,
`b8e3bcb9bc8fbe713377585c1000b3beb9a08bc5fa07cd8ff699de77043292e4` — **« scellable »**, 0 bloquante, 0 majeure, 11 mineures neuves ; les 19
points de la contre-lecture du brouillon 2 corrigés dans le corps du texte ; déplacement des liens durs compatible avec le code (seuls
`06_activations.py` l. 96 et `reads_at_firings.py` l. 67 lisent `arch.fits`) ; Drowse 6.1.4 vérifié. Reprise des mineures neuves dans
cette version :

| point | traitement |
|---|---|
| n-1 (moment de `hub` dans le cas (viii)) | levé : « juste avant `reads_at_firings.py` » |
| n-2 (lentilles de `score` sous la graine 1) | levé : `logit,npR,R:dclm-llama` |
| n-3 (modèle du lecteur) | non retenu : modèle servi à l'autrice relevé par l'outil de session, différent de celui des lecteurs ; écrit en tête |
| n-4 (titre, date) | levé |
| n-5 (correctif (5) « après l'ajustement ») | levé |
| n-6 (attendu de (q) ; banc) | levé : « chaîne en défaut (q) » ; la manière de jouer le banc dans la copie à part est fixée par la commande |
| n-7 (provenance des chiffres de (c)) | levé : ligne ajoutée |
| n-8 (« pendant la passe » non jouable) | levé : « juste avant » chaque étape, plus le message du correctif (1) relevé au journal |
| n-9 ((o) : erreur ou `None` ; lignes de `jlens.py` ; `sources.py` non lu) | levé pour les deux premiers ; `sources.py` de Drowse reste non lu, couvert par la garde (o) |
| n-10 (texte empreinté de (i)) | levé : texte entier |
| n-11 ((l) sous la graine 1) | levé : (l) étendue |

Scellement (R1) après ces corrections, sans nouvelle lecture : les corrections n'ajoutent aucun seuil, aucune mesure, aucune issue ; elles
précisent des moments, des listes et des libellés désignés par le vérificateur lui-même.

# Verdict du lecteur neuf — tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale (« Neuron Lens », Llama 3.1 8B Instruct) — v1

- Heure (UTC, `date -u`) : ouverture de la lecture **2026-11-19 07:35:36 UTC** ; relevé à l'écriture de ce verdict **2026-11-19 07:43:25 UTC**.
- Course lue : `20261118-164930-neuron-lens-b-beta` (fin « course terminee » le 2026-11-19 à 05:31:55 UTC), pièces versées dans le dossier
  de travail : `diag/20261118-164930-neuron-lens-b-beta/`, `runs/20261118-164930-neuron-lens-b-beta/`.
- Lecteur : sous-agent neuf (Opus 5.5, `claude-opus-5-5`), lancé par la session `session_013QMaykLXtozHttcSQ4ke1s` ; il n'a écrit ni le
  texte gelé, ni l'addendum, ni le code des verdicts, ni le code de course, ni la course. Branche `claude/brave-galileo-jhp684`, **tête au
  moment de la lecture `fe6c680a9745d1bd1635eaa2493417ca9aed2f61`**.
- Règles : texte gelé `texte-gele-tranche-b-beta-v1.md` (`f5d46860…`) et addendum partie 1 v3 (`bd8067dc…`), appliqués par le plan de
  lecture v2 (`plan-de-lecture-b-beta-v2.md`, `391c3b1a…`, scellé avant toute ouverture ; contre-lu `bf3e2d75…` ; différence v1→v2
  vérifiée `97e46129…`, dont les six mineures sont tenues ici dans leur sens strict). Empreintes recalculées à l'étape 0 : égales.
- Hors programme : aucun résultat n'entre dans T0.7, T0.8, G0, G1 ni dans un préenregistrement du programme sans nœud de Lazar. Une
  lecture par lentille peut ajouter un soupçon sur une sonde, jamais la blanchir.

## Verdict, en mots simples

**Verdict d'ensemble : « partiel »** (rang 5 des critères gelés). Aucune chaîne en défaut, aucun audit déclenché, aucun audit non joué ; ni
la lecture contre pilotage (B-2) ni l'avance sur la lentille des logits (B-3) ne sont « non reproduit » ; mais la stabilité (B-1) et la
lecture contre pilotage (B-2) ne sont pas « reproduit », donc pas « reproduit avec nos lentilles ». **Accord complet avec le fichier des
verdicts de la course** (verdict d'ensemble, sept mesures, valeurs, audits, réserves).

| mesure | verdict | valeurs décisives et marges aux seuils |
|---|---|---|
| B-1, stabilité de nos lentilles | **autre** | différence entre moitiés au-dessus de 0,10 à six couches-cibles : R `mid` couches 0, 1, 2 (0,1114 ; 0,1064 ; 0,1005), R `out` couches 0, 1 (0,1059 ; 0,1033), S `out` couche 31 (0,1046) — marge maximale **+0,0114** au-dessus de 0,10, loin sous 0,20 (« non reproduit » exclu, marge −0,089) ; accord du premier jeton entre moitiés ≥ 0,80 aux six couches, minimum **0,8436** (couche 2, marge +0,044) ; identique sur les trois séries versées (`diffs`, `diffs_float64`, `diffs_recopie`, écart entre elles ≤ 6·10⁻⁵) |
| B-2, lecture contre pilotage (notre R, « steer 1x ») | **autre** | seule condition manquée : `pass` = **0,8594** à la couche 8 (seuil 0,90, marge **−0,0406** ; 55 pôles sur 64 au lieu de 58) ; `pass` ≥ 0,9219 aux couches 9 à 27 ; `r_med` : minimum 0,4515 sur 8–15 (marge +0,0515), 0,85 sur 16–23 (+0,25), 0,9573 sur 24–27 (+0,107) ; témoin hors de ±0,05 à aucune couche (|max| 0,044) ; « non reproduit » loin (`pass` < 0,50 à aucune couche 16–27, `r_med` < 0,30 à aucune couche 16–23) |
| B-3, avance sur la lentille des logits | **reproduit** | écart `r_med`(notre R) − `r_med`(logits) ≥ +0,20 à chaque couche 4–15 ; minimum **0,2872** à la couche 4 (marge +0,0872 ; intervalle [0,255 ; 0,321]) |
| B-4, écart aux lentilles J et J++ (rapporté, non décisif) | rapportée | notre R − J négatif à 15 des 20 couches 4–23 (de −0,0426 à +0,0991) ; notre R − J++ positif aux 20 couches (de +0,0475 à +0,1945) |
| B-5, lecture côté entrée (notre S) | **reproduit** | lisible (part silencieuse 0,0159 à la couche 0, moyenne 0,00056 sur 1–7) ; `read_S` couche 0 = **0,8167** (marge +0,217 sur 0,60) ; moyenne 1–7 = 0,4043, moyenne 12–23 = 0,0845, écart **0,3198** (marge +0,220 sur 0,10) |
| B-6, deux codes (rapporté, non décisif) | **intermédiaire** | écart absolu ≤ 0,05 à **20** des 28 couches (il en faut 21 ; au-delà de 0,05 aux couches 2 à 8 et 11) ; maximum **0,0878** (couche 6), sous 0,15 partout ; notre R au-dessus de la lentille R publique aux 28 couches |
| B-7, lecture contre ablation par fenêtre (pour un moniteur, hors verdict d'ensemble) | **autre** | seule condition manquée : `r_med` = **0,3112** à la couche 15 (seuil < 0,25, marge **+0,061** du mauvais côté ; intervalle [0,295 ; 0,342]) ; ≤ 0,1979 aux couches 0–14 ; ≥ 0,8104 aux couches 26–29 (marge +0,31) ; ni « par le haut » (aucune couche 8–15 ≥ 0,40) ni « par le bas » ; lecture « autre » : couche par couche, la lecture prédit mal l'effet d'une activation en contexte jusqu'à la couche 14, la couche 15 est intermédiaire, bien tard |

**Audits** : aucun déclenché — trop beau de la lecture contre pilotage (A1 : `r_med` maximal 0,4599 aux couches 0–7, aucun témoin écrit
nul), trop beau et tout négatif de la stabilité (A2 : plus petite différence 0,0035, accords < 1 ; A3 : B-1 n'est pas « non reproduit »),
lecture côté entrée aux extrêmes (A4 : `read_S` 0,8167 à la couche 0), ablation par le haut (A5), deux codes (A6 : B-6 n'est pas
« désaccord ») ; l'audit « tout négatif » de la reproduction n'a pas lieu (ni B-2 ni B-3 « non reproduit »), la garde de la lentille R
publique (j) est tenue (écart maximal 0,0149 à la série repère). La course n'en a déclenché aucun non plus (`declenches: []`).

**Réserves** : aucune réserve des critères gelés (pas de « défaut dans notre lentille », pas d'« écart de corpus » ni d'« écart
d'ajustement »). Réserves du lecteur : (1) six gardes constatées sur la machine n'ont **pas de trace complète** dans les pièces versées —
corpus partagé (i) aux moments « avant l'ajustement » (en partie) et « avant `measure` », noms vus par `arch.fits` (k), documents des
pilotes (p), reprise et banc (q) en partie, jetons gardés avant chaque étape (r), fichiers antérieurs (s) ; sous l'ambiguïté ouverte O-7,
lecture (i) : verdict inchangé ; lecture (ii), la plus proche du texte : « partiel » sous cette réserve — le verdict ne change dans aucune
lecture ; (2) carte H100 (registre des GO), non consignée dans les pièces versées ; lot 64 consigné ; invariance au lot non mesurée sur
H100 ; deux verdicts tiennent à une marge de l'ordre de l'effet du matériel (B-2 : 3 pôles à la couche 8 ; B-6 : une couche de 21) ;
(3) observations de montage sans effet de règle (section 5).

**Chaînes en défaut** : **aucune**. Recalculées par moi sur les sorties brutes : (a) témoin (|max| 0,0699, `steer 4x`, J ; moitiés
comprises), (b) pilotage sans effet (aucun pôle écarté, toutes cibles), (c) cas sains des couches 28–30 (logits ≥ 0,8447 ; R publique ≥
0,9674 ; notre R ≥ 0,9709), (e) repli sur les logits (plus petit écart 0,0201, J++), (j) (0,0149) — toutes tenues. Lues sur les pièces :
(d), (e) matrices, (f), (g), (h), (n), (o) tenues ; (i), (k), (p), (q), (r), (s) sans trace complète, aucune en défaut ; (l) et (m) sans
objet (aucun audit).

## 1. Pièces et empreintes (étape B, point 1 ; étape D)
- `sha256sum -c` des 50 compagnons de `diag/20261118-164930-neuron-lens-b-beta/` : 50 « OK » ; manifeste `runs/…/manifeste.json` :
  « OK » (`b90c1514…`, égal au `manifeste_sha256` porté par les 23 résultats d'étape). Les 16 journaux et 2 artefacts de la garde (d) ont
  un compagnon posé après coup : intégrité attestée depuis la récupération seulement (réserve R-2 du plan).
- Empreintes croisées, égales : sortie de `score` `8d65dda1…` et son journal `8747e4dc…` (portées par `b-beta-score.json`) ; grandeurs
  par pôle `8252cdd1…` ; lecture aux déclenchements `d77926f6…` ; comparaison des lentilles `9b7e7e39…` ; intervalles `9255d3ea…` ;
  parties 2 de l'addendum `7b7cc0d2…`, `e800ce8b…` ; série repère `bd57d519…`.
- Le manifeste ne porte pas de liste d'empreintes par fichier de résultat ; il porte : commit `5e5cb65b…`, `depot_propre: true`,
  préenregistrement `f5d46860…`, configuration (`02_fit.py --docs 1000 --seq-len 128 --full-length --save-minutes 60`, corpus
  `dclm=40000,zh=8000,code=8000,chat=8000`, cinq correctifs, Drowse 6.1.4 `673ed2b4…`, lentilles notées, précision « bf16 sur carte,
  TF32 ; score en float32 sur le processeur »), graines (`SeedSequence(entropy=20261118)`, branche « B-β », cinq tâches d'intervalles ;
  `random.Random(0)` pour les neurones), versions (python 3.12.16, torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2, huggingface_hub
  1.33.0, numpy 2.4.6, safetensors 0.8.0), ligne `GO-2026-11-18-35` (ligne de calcul de la course sur H100, au registre ; le texte gelé
  nomme la ligne de décision GO-2026-11-18-02).

## 2. Ordre suivi (plan v2) et fichiers scellés à chaque étape
| étape | heure (UTC) | contenu | fichier scellé (empreinte) |
|---|---|---|---|
| A | 07:38 | script du lecteur, essai sur les cas gelés de P.4 (références publiées `8904c4d3…`, `ac0bf101…`) et sur des cas faits à la main : **aucun écart** ; un premier passage avait signalé un écart dû à une tolérance trop stricte de l'essai lui-même (part silencieuse de la référence comparée à 0 au 10⁻¹² au lieu de « 0,000 » à trois décimales) : essai corrigé avant scellement, aucune règle touchée | `calcul-verdicts-b-beta-v1.py` (`20762bc3…`), `essai-calcul-verdicts-b-beta-v1.py` (`4a1c54c8…`), `sortie-essai-calcul-verdicts-b-beta-v1.txt` (`67cc180f…`) |
| B.1–B.3 | 07:39 | compagnons ; sorties brutes (procédure « structure d'abord » pour toutes, y compris grandeurs par pôle et intervalles) ; gardes (a), (b), (c), (e) part « score », (j) ; déclencheurs A1, A4, A5, A6 ; B-2 à B-7 | `executer-calcul-b-beta-v1.py` (`14794c97…`), `calcul-etape-b-b-beta-v1.json` (`52b61fc4…`) |
| B.4 | 07:40 | différences entre moitiés extraites de `b-beta-ajustement-R.json` et `-S.json` (clés listées d'abord ; champs `diffs`, `diffs_float64`, `diffs_recopie` seuls) ; B-1, A2, A3 | `complement-b4-b-beta-v1.json` (`0c87b233…`), `calcul-etape-b-complement-b-beta-v1.json` (`cd58f0c7…`) |
| C | 07:40 | verdict provisoire, gardes de la machine inconnues : « partiel » | `verdict-lecteur-etape-c-b-beta-v1.md` (`79a19f4f…`) |
| D | 07:42 | pièces portant gardes (toutes, hors verdicts et déclencheurs) ; recherche de trace dans toutes les pièces ; manifeste ; confrontation à P.6 | `complement-d-b-beta-v1.json` (`ae341a9f…`), `calcul-etape-d-b-beta-v1.json` (`80f8e0cb…`), `verdict-lecteur-etape-d-b-beta-v1.md` (`660ece89…`) |
| E | 07:42 | ouverture de `b-beta-declencheurs.json`, `b-beta-verdicts.json`, `verdicts-b-beta-v1.json` | — |

## 3. Détail des mesures (valeurs telles qu'écrites ; notre R, « steer 1x » sauf mention)
- **n** (recalculé, `grandeurs-par-pole-b-beta-v1.json`, égal à `b-beta-grandeurs.json`) : **64 à chaque couche des quatre cibles**,
  aucun pôle écarté (« effet nul » ni « sans contexte ») ; toutes les couches lisibles, aucune bande partielle. La table de `score`
  recopiée dans les grandeurs est égale, valeur pour valeur, à la sortie JSON de `score`. Métadonnées de `measure` : 16 contextes de 64
  jetons, doses 1× et 4×, fenêtre 8, `measure --ctx-batch 64` (journal).
- **B-1** : différences non arrondies par couche (R `out` 0–30) 0,1059 0,1033 0,0951 0,0864 0,0809 0,0752 0,0704 0,0652 0,0595 0,0536
  0,0499 0,0456 0,0418 0,0378 0,0344 0,0295 0,0266 0,0233 0,0213 0,0197 0,0185 0,0169 0,0156 0,0143 0,0132 0,0121 0,0112 0,0099 0,0091
  0,0074 0,0044 ; (R `mid` 0–31) de 0,1114 à 0,0035, décroissant ; (S `out`) de 0,0075 à 0,1046, croissant pour l'essentiel ; (S `mid`) de 0,0041 à
  0,0856. Accord du premier jeton entre moitiés (couches 2, 7, 12, 18, 23, 28) : 0,8436 0,8678 0,9202 0,9635 0,9754 0,9833. Rapportés
  sans critère : recouvrement des dix premiers jetons entre moitiés 0,884 0,896 0,936 0,969 0,979 0,986 ; accord de chaque moitié avec la
  lentille R publique 0,228/0,231, 0,259/0,263, 0,426/0,429, 0,687/0,690, 0,777/0,778, 0,850/0,854 ; 28 672 pôles par couche. Valeurs à
  deux décimales de `02_fit.py` et `04_export_rlens.py` (pour mémoire) : 0,11 0,10 0,10 … (R `out`), 0,11 0,11 0,10 … (R `mid`).
- **B-2** : `r_med` 8–27 : 0,4515 0,4829 0,5249 0,5536 0,6185 0,6819 0,7397 0,8205 | 0,85 0,8818 0,9033 0,9188 0,9286 0,94 0,9461 0,9523
  | 0,9573 0,9611 0,9647 0,9653 ; `pass` 8–27 : 0,8594 0,9375 0,9219 1,0 0,9844 1,0 0,9688 1,0 puis 1,0 jusqu'à 27 ; témoin |max| 0,044
  (couche 1). Intervalle de `r_med` à la couche 8 : [0,3997 ; 0,4832].
- **B-3** : écarts 4–15 : 0,2872 0,3226 0,3883 0,3524 0,3537 0,345 0,3651 0,3902 0,4162 0,3728 0,3522 0,3115.
- **B-4** : notre R − J (4–23) : 0,09 0,0546 0,0991 −0,0134 0,0349 0,0085 −0,0178 −0,001 −0,0426 −0,0297 −0,0275 −0,0104 −0,02 −0,0162
  −0,0096 −0,0114 −0,0155 −0,0114 −0,0167 −0,0147 ; notre R − J++ : 0,1155 0,1474 0,1771 0,1085 0,1885 0,1664 0,1382 0,1643 0,1798 0,1945
  0,1738 0,1278 0,1012 0,0783 0,1573 0,1068 0,0517 0,0617 0,0915 0,0475.
- **B-5** : `read_S` par couche (journal, deux décimales) 0,82 0,87 0,67 0,53 0,37 0,24 0,10 0,06 0,04 … 0,01 ; part silencieuse 0,0159 à la
  couche 0, 0,00 ailleurs ; valeurs non arrondies dans la sortie JSON ; `read_S_net` rapporté dans `calcul-etape-b-b-beta-v1.json`.
- **B-6** : écarts absolus 0–27 : 0,0382 0,0482 0,066 0,0598 0,0703 0,0825 0,0878 0,0676 0,0575 0,048 0,0494 0,08 0,0438 0,0437 0,0287
  0,0302 0,0312 0,0222 0,0235 0,02 0,0196 0,0155 0,0126 0,0112 0,009 0,0082 0,0066 0,0042.
- **B-7** (« ablate win ») : −0,0061 0,0236 0,0034 0,0437 0,0502 0,0535 0,0847 0,0639 0,0716 0,0782 0,0391 0,1198 0,1288 0,1771 0,1979
  **0,3112** | … | 26–29 : 0,8104 0,8441 0,8219 0,8482.
- **Grandeurs rapportées** : jeton de début (128 000) : compte 72 000, gardé, rang 117 ; jetons gardés 89 498, `c37186ad…` (égal à
  l'attendu) ; fichier `-causal.pt` `29343cdf…` (2,1 Go, non versé) ; « steer 4x » et « ablate pos » dans la sortie de `score` ; intervalles
  (2 000 tirages) dans `intervalles-b-beta-v1.json`.

## 4. Gardes constatées sur la machine (étape D) — trace recherchée dans toutes les pièces versées
| garde | pièce et constat | statut |
|---|---|---|
| (d) | `b-beta-b0.json` et journal `b0.log` : six essais des correctifs et de l'estimateur, essais du dépôt sur le Qwen3 miniature (2), crochets (4), aucun test sauté ; artefacts « sauté » (1 skipped) et « signe » (2 failed) **vus en défaut** ; fumée code 0 | tenue |
| (e) matrices | `b-beta-b0.json` : J, J++, R publique, 31 couches contiguës, écart à l'identité ≥ 0,75 ; `b-beta-export.json` : notre R, écart minimal à l'identité 0,80 | tenue |
| (f) | estimateur sur Llama miniature : 11 tests passés | tenue |
| (g) | `b-beta-ajustement-R/S.json` : 466 et 466, `next_doc` 932 = `docs` 932, longueurs [128], `rows_sha256` `a6afd972…`, `full_length` vrai, `finies` vrai | tenue |
| (h) | R : 31 `out`, 32 `mid` (fichier et export) ; S : 32 et 32 | tenue |
| (i) | après `05` : `garde_i: []` ; avant l'ajustement : provenance écrite égale à la publiée (`16957c52…`), mais la comparaison à la provenance des activations n'est pas versée ; avant `measure` : aucune trace | sans trace complète |
| (k) | aucun relevé de `arch.fits` ; preuves complémentaires : journal de la passe « no released R-lens … heads/acts without out_R_z » (branche `hub`) ; `b-beta-reads.json` : liens d'empreintes `31061d6c…` et `aac70eef…`, égales à celles de fin d'ajustement ; fumée `message_hub: false` (la fumée n'écrit pas les tables) | sans trace complète |
| (n) | écart minimal à la lentille R publique 0,069 (couches 0–27) ; aucune empreinte d'export égale à `a63a1588…` | tenue |
| (o) | aller-retour des trois noms : 31 couches, écart **0,0** à chaque couche ; garde (o) aussi essayée au banc (`ALLER-RETOUR []`) | tenue |
| (p) | `measure` : 16 contextes ; pilotes : aucun compte de documents par tranche versé | sans trace complète |
| (q) | banc dans `voisin-banc/` (copie à part) ; aucune reprise aux journaux d'ajustement ; absence de fichier `-T128` avant le premier lancement non versée | sans trace complète |
| (r) | empreinte des jetons gardés relevée après `03_token_counts.py` ; contrôle avant chaque étape non versé | sans trace complète |
| (s) | aucune trace | sans trace |
| arrêts de montage | banc : second document 19,3 s (R) et 19,2 s (S), sous 23,6 s, au-dessus de 14,2 s (compte rendu écrit) ; 932, 466/466, `a6afd972…` ; Drowse 6.1.4 `673ed2b4…` ; partie 2 « Écarts : aucun » aux deux relevés ; essais du code des verdicts (82) et des contrôles (29) passés | tenus |

## 5. Observations, aspect trop propre (R4) et confrontation à P.6
- **Trop propre, à signaler sans en faire un verdict** : (1) **aucun pôle écarté**, n = 64 à toutes les couches des quatre cibles ; (2)
  aller-retour de l'export d'écart **exactement nul** aux 31 couches des trois exports (plausible : mêmes matrices écrites puis relues en
  float32) ; (3) notre R au-dessus de la lentille R publique aux **28** couches (écart d'un seul signe ; l'audit des deux codes n'est pas
  déclenché) ; (4) accord bit à bit entre mon calcul et celui de la course, attendu : mêmes entrées, mêmes règles.
- **Marges courtes** : B-2 ne manque « reproduit » qu'à une couche (8), par 3 pôles ; B-6 manque « accord » d'une couche (20 sur 21) ;
  B-1 manque « reproduit » de 0,0114 au plus (six couches-cibles) ; B-7 à la couche 14 est à 0,1979 (seuil de la prédiction 0,20). Ces
  marges sont de l'ordre de l'effet du matériel (≈ 0,03) ; elles ne changent aucun verdict, mais un verdict voisin était à portée.
- **B-1 et l'effet attendu** : le texte attendait un effet « faible » du corpus réduit (2 à 4 % sur la part due au bruit) ; les différences
  observées aux premières couches de R (≈ 0,11) sont environ le double du publié (0,04 à 0,06) ; pour S, la différence croît avec la
  profondeur jusqu'à 0,10 à la couche 31, alors que le publié donne 0,00 à 0,05. Rapporté ; aucun verdict n'en dépend.
- **Banc** : le troisième document chronométré prend 26,5 s (R) et 26,7 s (S), au-dessus de 23,6 s ; la règle porte sur le second document
  (19,3 et 19,2 s) ; l'ajustement réel a pris ≈ 19,8 s par document. Rapporté.
- **Montage** : la partie 2 relève une version de `pyyaml` (6.0.3), paquet que la partie 1 ne liste pas (aucune version différente d'un
  paquet listé) ; champ « instance » vide dans la partie 2 ; `07_drivers.py` a écrit des résumés nommés `…_qwen3-8b.json` (nom du modèle
  par défaut du code voisin ; la table des pilotes n'entre dans aucune mesure de ce texte).
- **Confrontation à P.6** (étape D) : présents — différences entre moitiés, comptes et longueurs, `rows_sha256` et empreinte de la
  provenance d'ajustement, empreintes des deux fichiers d'ajustement et des trois exports, contrôles des matrices, sortie non arrondie de
  `lens_compare.py`, jetons gardés (nombre, empreinte), sortie de `score`, n et pôles écartés par motif, empreinte du `-causal.pt`, sortie
  de `reads_at_firings.py` avec la part silencieuse, empreintes de `07_drivers.py`, jeton de début, contrôles de B0, fichier des verdicts,
  journaux, manifeste. **Absents ou incomplets** : le **résumé** de `07_drivers.py` (empreintes seulement) ; les fichiers de provenance
  eux-mêmes (empreintes seulement) ; aucune sortie d'audit (cohérent : aucun audit déclenché) ; les contrôles des gardes (i), (k), (p),
  (q), (r), (s) (section 4).

## 6. Ambiguïtés rencontrées et verdict sous chaque lecture
- **Tranchées (T-1 à T-6)** : leur lettre seule ne change rien ici. T-1, T-2, O-1 : aucune bande partielle (n = 64 partout). T-3 : la garde
  (a) tient avec ou sans les moitiés. T-4 : flottant brut ou arrondi, mêmes côtés de seuil (calcul par variante,
  `calcul-etape-d-b-beta-v1.json`, champ `variantes`, « diffère : faux » pour toutes). T-5 : B-5 loin des seuils. T-6 : comparaison
  principale à `verdicts-b-beta-v1.json` ; `b-beta-verdicts.json` ne porte pas de verdict (il renvoie au fichier des verdicts et aux
  intervalles, empreinte `9255d3ea…` égale).
- **Ouvertes rencontrées** : **O-7** (gardes sans trace complète) — (i) « partiel » ; (ii) « partiel » sous réserve. O-2 (garde (b)) : motif
  « effet nul » et n donnent la même issue (0 écarté, n = 64). O-3 : n est par cible dans les pièces (non par lentille) ; n recalculé et
  n de `score` (absent de sa sortie) : sans objet. O-4 : toutes les couches lisibles, sans objet. O-5, O-6 : aucun audit déclenché, sans
  objet. O-8 : aucun manquement de la liste d'arrêt constaté (le troisième document du banc n'est pas visé par la règle). O-9 : (c) et
  (e) tenues avec ou sans les moitiés. O-10, O-11 : sans objet.
- **Différences entre moitiés** : trois séries versées (`diffs`, `diffs_float64`, `diffs_recopie`) ; le texte veut « recalculée par notre
  code sur la machine, non arrondie » ; j'ai pris `diffs` ; les trois donnent le même verdict et les mêmes couches au-dessus de 0,10.

## 7. Comparaison avec les fichiers de la course
| élément | lecteur | course (`verdicts-b-beta-v1.json`, `b-beta-declencheurs.json`) | accord |
|---|---|---|---|
| verdict d'ensemble | partiel | partiel | oui |
| B-1 | autre (différence max 0,1113882064819336 ; accord min 0,8436453938484192) | autre (mêmes valeurs) | oui |
| B-2 | autre (témoin hors ±0,05 : 0 couche ; hors ±0,10 : 0) | autre (0 ; 0) | oui |
| B-3 | reproduit (écart min 0,2872) | reproduit (0,2872) | oui |
| B-4 | 20 + 20 écarts | mêmes 40 valeurs | oui |
| B-5 | reproduit (six valeurs) | reproduit (mêmes six valeurs) | oui |
| B-6 | intermédiaire (28 écarts, aucune couche au-delà de 0,15) | intermédiaire (mêmes) | oui |
| B-7 | autre ; ni par le haut ni par le bas | autre ; `par_le_haut_graine_0` faux, `par_le_bas` faux | oui |
| défauts | aucun | `defauts: []` | oui |
| audits | aucun déclenché | `declenches: []`, `audits_declenches: []`, `audits_joues: {}` | oui |
| réserves | aucune des critères gelés ; réserves du lecteur (section « en mots simples ») | `reserves: []` | oui sur les critères gelés ; les réserves du lecteur sont en plus |
**Aucun désaccord** à trancher par un second lecteur. La course n'écrit pas les gardes sans trace (section 4) dans ses fichiers de
verdicts ; je le rapporte, sans en faire un désaccord.

## 8. Prédictions de l'autrice (« réfutée si », telles qu'écrites ; sans effet sur les verdicts)
| mesure | réfutée ? | pourquoi |
|---|---|---|
| B-1 (0,02–0,08 aux couches 0–18 de R ; ≤ 0,06 partout pour S ; accord 0,85–0,99) | **réfutée** | R `out` 0,1059 à la couche 0 ; S `out` 0,1046 ; accord 0,8436 à la couche 2 |
| B-2 (≥ npR − 0,02 à ≥ 15 couches de 8–27 ; `pass` ≥ 0,90 de 11 à 27 ; une condition manquée en 8–10) | non réfutée | 20 couches sur 20 ; `pass` ≥ 0,9375 de 11 à 27 ; `pass` 0,8594 à la couche 8 ; issue modale « autre » observée |
| B-3 (≥ +0,20 à chaque couche 4–15) | non réfutée | minimum 0,2872 |
| B-4 face à J (négatif à ≥ 11 couches) | non réfutée | 15 |
| B-4 face à J++ (positif à ≥ 11 couches) | non réfutée | 20 |
| B-5 | non réfutée | 0,8167 ; écart 0,3198 ; lisible |
| B-6 (« accord ») | **réfutée** | « intermédiaire » (20 couches sur 21) |
| B-7 (≤ 0,20 aux couches 0–14, 0,25–0,40 à la 15, ≥ 0,80 aux 26–29) | non réfutée | 0,1979 ; 0,3112 ; 0,8104 ; issue modale « autre » observée |
| verdict d'ensemble modal « partiel » | non réfutée | « partiel » |

## 9. Expositions déclarées (clause d'exposition, toutes pièces)
- Avant mes calculs scellés de l'étape B : aucune valeur de garde, de déclencheur ou de verdict de la course ; à l'étape B.4, seules les
  **clés** de `b-beta-ajustement-R/S.json` et `b-beta-export.json` (dont des noms comme `finies`, `aller_retour`, `identite_notre_R`) ont
  été vues, sans valeur, avant le scellement de `calcul-etape-b-complement-b-beta-v1.json` ; puis les seules valeurs `diffs`,
  `diffs_float64`, `diffs_recopie`.
- À l'étape D, après les scellements B et C : `normes_non_nulles: true`, `temoin_distinct: true` (`b-beta-grandeurs.json`, contrôles de
  l'audit « trop beau » calculés sans déclenchement) ; `fidelite_a_score` (grandeurs par pôle) ; `garde_i: []`. Aucun ne touche mon calcul.

## 10. Ce que je n'ai pas fait
Aucun modèle, aucune machine, aucun réseau payant ; ni la branche `calcul/neuron-lens-b-beta-v1`, ni `controles-b-beta-v1.log`, ni l'état
final de la course (non autorisé par le mandat de lecture) ; aucun autre `diag/` ou `runs/` sauf la série repère (`bd57d519…`) ; pas le
verdict de la tranche B-α ; aucun import ni relecture du code des verdicts de la course (lu en phase 1 pour les noms de clés, déclaré) ;
aucun rejeu d'audit ; aucun fichier existant réécrit ; aucun commit, aucun push.

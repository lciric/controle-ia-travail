# Critère d'identité du réajustement de nos lentilles R et S — v2 (à vérifier par le même contre-lecteur, puis sceller avant toute création)

- Auteur : session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`, modèle Claude Opus 5.5), auteur du devis (déclaré). Écrit le
  2026-11-19 entre 10:20 et 10:45 UTC. Pièce de **classe A** (critère décisif d'une course payante).
- v2 = v1 (`critere-identite-reajustement-lentilles-v1.md`, `1a5da7f2…`, archivée sans modification) corrigée selon sa contre-lecture
  (`docs/notes/neuron-lens-v1/contre-lecture-critere-identite-reajustement-v1.md`, branche principale, commit `a734884a`, `92419037…` ;
  contre-lecteur neuf, Fable 5.2 : « pas avant », C1 à C6 et sept mineures). Traitement au § 8.
- Contexte : GO-2026-11-19-33 (mot de Lazar « 1 2 et 3 » ; pièce 3 du billet). Aucune ligne de calcul à ce jour. **Ce critère prime sur
  la phrase « identité par les paliers 1 et 2 » du devis v2** (décision 1) ; un erratum du devis le dit.

## 1. Références du 18 novembre
Branche `claude/brave-galileo-jhp684` (pièces absentes de la branche principale), commit `cdb854c0` ou plus récent ; dossier
`diag/20261118-164930-neuron-lens-b-beta/` :
- `b-beta-ajustement-R.json` (`129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab`) : fichier d'ajustement de R
  `r-llama-3.1-8b-instruct-L32-dclm-T128.pt`, `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c`, 8 455 720 309 octets ;
  `diffs_float64` 63 valeurs (32 `mid`, 31 `out`) ; `diffs` (simple précision) ; `meta` ; `n_docs` [466, 466] ; `next_doc` 932.
- `b-beta-ajustement-S.json` (`2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297`) : `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8`,
  8 589 938 049 octets ; 64 valeurs (32 et 32).
- `b-beta-export.json` (`17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1`) : pour R, `matrices_moities` (31 couches,
  deux empreintes) et `valeurs.npR_notre_R`, `valeurs.identite_notre_R` (28 couches chacune).
- Manifeste `runs/20261118-164930-neuron-lens-b-beta/manifeste.json` (`b90c1514…`) : `config.commit_voisin`
  `849bfe1678e28becceb1e3864afe5fc8297d02e4`. Fonction de calcul : `_split_half_64` de `src/controle_ia/neuron_lens/b_beta_lancer_v3.py`.

## 2. Écart entre chemins de calcul (programme `ecart_chemins_calcul_v1.py`, `2084dae7…` ; sortie `sortie-ecart-chemins-calcul-v1.txt`, `21d04198…` ; pièces `129c43b0…` et `2dce646e…`)
Sur les **mêmes sommes**, la différence entre moitiés calculée en simple précision (`diffs`) s'écarte de celle en double précision
(`diffs_float64`) d'au plus 3,48 × 10⁻⁵ (R, `mid`, rang 2 ; relatif 2,0 × 10⁻³) et 5,86 × 10⁻⁵ (S, `out`, rang 26 ; relatif 1,4 × 10⁻³) ;
la recopie (`diffs_recopie`), 1,52 × 10⁻⁶ et 3,12 × 10⁻⁶. `diffs_float64` va de 3,53 × 10⁻³ à 0,1114 (R) et de 4,11 × 10⁻³ à 0,1046 (S) ;
la valeur de R la plus proche de 0,10 est 0,100444 (`mid`, rang 2), à 4,4 × 10⁻⁴.
**Cet écart est celui du calcul final en simple ou en double précision sur les mêmes sommes. Le critère compare deux valeurs en double
précision : cet écart n'y entre pas. Il ne borne l'écart d'un réajustement ni par le bas ni par le haut** (non mesuré).

## 3. Critère, lentille par lentille
Chaque lentille est jugée seule ; cas mixte : chacune rangée avec sa mention. Une lentille non réajustée (course arrêtée avant elle) :
« S non réajustée » (ou R), l'autre jugée seule. **Programme** : `src/controle_ia/neuron_lens/comparer_reajustement_v1.py` (`247b6959…`),
essais `tests/test_neuron_lens_comparer_reajustement_v1.py` (`0f5b5bdb…`, 19 essais passés le 2026-11-19 ; § 6).
1. **Palier 1 — « même lentille, octets identiques »** : empreinte du nouveau fichier d'ajustement égale à la référence. Exige le **même nom
   de fichier** qu'au 18 : le nom entre dans les octets écrits par `torch.save`, le dossier non (essai `essai_torch_save_nom_v1.py`,
   `1893d03e…`, sortie `3a2dbb16…` ; et `essai_torch_save_octets_v1.py`, `4fdec19d…`, sortie `3a18c2c2…`). Une reprise sur sauvegarde
   pendant l'ajustement est notée ; si l'empreinte est égale, le palier 1 est prononcé quand même, avec l'audit du § 5.
2. **Palier 2 — « différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non comparables »** (sinon) : écart
   absolu maximal, en double précision et sans arrondi, entre les nouvelles `diffs_float64` (fonction `_split_half_64`, texte inchangé,
   calculée sur la machine à la fin de l'ajustement) et celles du 18, sur toutes les couches et cibles (R : 32 `mid` et 31 `out` ; S : 32
   et 32), **au plus 10⁻³**.
   - **Préalables, tous exigés ; un seul manqué → « non comparable », rangée et traitée comme « différente »** : mêmes cibles et mêmes
     comptes de valeurs (`diffs_float64` et `diffs`) ; toutes les valeurs finies ; `meta` égal champ par champ ; `n_docs` [466, 466] et
     `next_doc` 932 des deux côtés ; même nom de fichier ; même commit du code voisin ; même texte de `_split_half_64` (empreinte SHA-256
     du texte source de la fonction dans les deux lanceurs).
   - **Rapportés, sans critère** : l'écart relatif maximal ; l'écart sur `diffs` (la valeur que lisaient les seuils de la tranche) ; toute
     valeur de `diffs` qui change de côté du seuil de stabilité de 0,10 ; la table des écarts par couche et par cible, avec leur signe ;
     **pour R**, le compte des couches dont les empreintes des matrices des moitiés sont égales, et l'écart, couche par couche, des deux
     séries `npR_notre_R` (écart maximal de chaque matrice à la lentille R publique) et `identite_notre_R` (à l'identité) : rapportées
     sans critère, parce qu'aucune pièce ne mesure non plus leur variation d'un réajustement et qu'une tolérance y serait aussi
     conventionnelle ; elles disent si la lentille a bougé par rapport à une ancre fixe. **Pour S, aucune grandeur sensible à la position
     n'existe dans les pièces du 18 : à écrire tel quel.**
   - **Condition nécessaire, pas suffisante, et aveugle par construction** : la grandeur vaut ‖moyenne paire − moyenne impaire‖ /
     ‖moyenne‖ ; tout déplacement commun aux deux moitiés s'annule au numérateur. Elle dit si le bruit entre moitiés est retrouvé, pas si
     la lentille est au même endroit : une lentille déplacée de 13 % de sa norme à chaque couche, dans une direction commune aux deux
     moitiés, passe ce palier (contre-lecture, point 2). La mention ne dit ni « équivalente », ni « proche », ni « même lentille ».
   - **Tolérance conventionnelle, déclarée telle, absolue** : la décision qui compte ensuite porte sur le seuil absolu de 0,10 ; une
     tolérance relative serait lâche là où la grandeur est grande, près de ce seuil. Repères, qui ne la justifient pas : ≈ 17 fois le plus
     grand écart entre chemins de calcul ; un centième du seuil de stabilité ; 0,9 % de la plus grande valeur ; 28 % (R) et 24 % (S) de
     la plus petite : aux couches les plus stables, ce palier ne distingue presque rien ; elle dépasse la distance au seuil de la valeur
     de R la plus proche (4,4 × 10⁻⁴).
3. **Au-delà — « différente »** : rangée, marquée telle ; aucune lecture ne la lit sans nœud de Lazar.
4. **Anomalie** : pour R, empreinte du fichier égale mais une empreinte de matrice des moitiés différente → mention suspendue, nœud de
   Lazar.

## 4. Ce que chaque mention autorise
**Seul le palier 1 établit l'identité.**
- **Palier 1** : les mesures et le verdict du 18 décrivent la lentille rangée. Phrase permise : « Les fichiers d'ajustement réajustés
  sont identiques à l'octet à ceux du 18 novembre (empreintes …) ; les mesures du 18 novembre décrivent ces lentilles. » (*“The refitted
  fit files are byte-identical to those of 18 November (hashes …); the 18 November measurements describe these lenses.”*)
- **Palier 2** : l'identité n'est pas établie et **le verdict du 18 ne se transporte pas** ; Lazar en est averti en ces termes avant tout
  usage. En variante B (course rejouée), les mesures qui décrivent la lentille rangée sont celles de la seconde course, lues par un lecteur
  neuf ; en variante A, elle n'a aucune mesure propre, et le billet le dit. Une couche n'est tenue pour stable que si `diffs` est au plus
  0,10 **dans les deux ajustements**.
  Phrase permise : « Les deux lentilles mesurées le 18 novembre ont été détruites avec la machine louée. Nous les avons réajustées avec le
  même code, le même corpus et les mêmes graines sur une autre machine. Les fichiers obtenus ne sont pas identiques à l'octet. La seule
  comparaison possible porte sur la différence entre les deux moitiés du corpus, couche par couche : elle s'écarte d'au plus [écart mesuré]
  de celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³). Cette grandeur ne voit pas un déplacement commun aux deux
  moitiés : nous ne savons pas si la lentille réajustée lit comme celle du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites
  sur elle | ont été refaites sur elle et sont rapportées à côté]. »
  (*“The two lenses measured on 18 November were destroyed with the rented machine. We refitted them with the same code, corpus and
  seeds on another machine. The files are not byte-identical. The only comparison left is the per-layer split-half difference, which
  deviates by at most [x] from the 18 November values (tolerance fixed in advance, by convention, at 10⁻³). This quantity is blind to any
  shift common to both halves, so we cannot establish that the refitted lens reads like the one measured on 18 November. The 18 November
  measurements [were not repeated on it | were repeated on it and are reported alongside].”*)
  Phrases interdites : « nous avons réajusté à l'identique les lentilles jugées le 18 novembre » ; « la lentille réajustée est proche de
  l'originale », « équivalente », « la même à la précision numérique près » ; « le verdict “partiel” du 18 novembre vaut pour la lentille
  employée ici » ; toute phrase qui prête à la lentille réajustée une mesure faite sur celle du 18. (*“We refitted the same lenses”;
  “the refitted lens is close/equivalent to the original”; “the 18 November verdict applies to the lens used here”.*)
- **« Différente » ou « non comparable »** : rangée, marquée ; aucune lecture sans nœud de Lazar.
- **Dans tous les cas** : tout usage dans une lecture passe par un texte de lecture neuf, contre-lu, qui recopie la mention et l'écart
  mesuré, et par le mot de Lazar (GO-2026-11-19-33) ; le billet dit le palier obtenu, quel qu'il soit, et, si la lentille n'est pas lue,
  le dit en une phrase ; la mention est écrite dans un fichier compagnon au lieu de rangement et à l'inventaire.

## 5. Audit, le même dans les deux sens
**Déclencheurs** : (i) palier 1 obtenu ; (ii) écart maximal exactement nul avec des octets différents ; (iii) « différente » ; (iv) « non
comparable » ; (v) pour R, empreinte du fichier égale et une empreinte de matrice des moitiés différente (palier 1 suspendu).
**Audit, par programme, sans lire aucune mesure de la course** : provenance des deux côtés (l'empreinte neuve vient du fichier de la
course neuve — identifiant, heure, taille — et est relue au lieu de rangement après la copie ; la référence est lue dans la pièce du 18 par
son empreinte ; les deux ne sortent pas du même fichier) ; table des différences de `meta`, des commits, des versions de bibliothèques,
du pilote et du modèle de carte ; table des écarts par couche et par cible, avec leur signe. L'audit est versé scellé avec le verdict
d'identité ; un contrôle manqué suspend la mention et ouvre un nœud de Lazar. **Aucune relance pour obtenir un autre palier sans devis
neuf et mot de Lazar.**

## 6. Programme et essais (scellés avant la création ; R5)
`comparer_reajustement_v1.py` rend la mention, les déclencheurs, les préalables et les tables ; il refuse d'écraser une sortie (R12).
Une valeur non finie ou absente rend « non comparable » **avant** tout maximum (le maximum est explicite et lève une erreur sur une valeur
non finie). Essais, sur les pièces du 18 : **cas sain** (pièces contre elles-mêmes : palier 1, déclencheur (i) ; mêmes valeurs avec des
octets différents : palier 2, déclencheur (ii), 63 et 64 écarts) ; **artefacts** : une valeur déplacée de 2 × 10⁻³ → « différente » ;
`nan`, `inf`, valeur absente ou texte → « non comparable » sans maximum ; 62 valeurs au lieu de 63 → « non comparable » ; un champ de
`meta` changé → « non comparable » ; `n_docs`, `next_doc`, nom de fichier, commit du voisin, texte de la fonction → « non comparable » ;
anomalie (v) → mention suspendue ; reprise avec octets égaux → palier 1 noté ; bord de tolérance (0,9 × 10⁻³) → palier 2 ; changement de
côté du seuil sur `diffs` rapporté sans changer la décision ; sortie non écrasée. Le programme est une pièce de classe B : contre-lu avec ce
critère.

## 7. Qui applique
Les empreintes sont calculées par programme sur la machine. Les écarts sont calculés par le programme scellé du § 6, sur les pièces
versées, **par la mère ou par un agent neuf qu'elle lance**, et non par la session des lentilles, avant toute lecture d'une mesure de la
nouvelle course ; le verdict d'identité est écrit, scellé et rapporté à Lazar par la mère.

## 8. Traitement de la contre-lecture de la v1
| remarque | traitement |
|---|---|
| C1 mention et définition du palier 2 | faite (§ 3, point 2), préalables compris |
| C2 grandeur aveugle ; séries de R ; S | faite : aveuglement écrit ; séries de R rapportées **sans critère** (raison au § 3) ; S « rien de tel » |
| C3 ce que chaque mention autorise | faite (§ 4), phrases permises et interdites en français et en anglais ; primauté sur le devis |
| C4 audit dans les deux sens et programme essayé | fait (§ 5, § 6) : programme écrit, 19 essais passés |
| C5 rattachement du plancher, libellé de la tolérance | fait (§ 2, § 3) : programme et sortie scellés ; « ne borne ni par le bas ni par le haut » ; repères vrais |
| C6 qui applique | fait (§ 7) |
| m-1 nom du fichier | vérifié : le nom entre dans les octets, le dossier non ; même nom exigé (§ 3, point 1) |
| m-2 reprise | faite : palier 1 prononcé, reprise notée, audit |
| m-3 prédiction des matrices | faite : règle au déclencheur (v) |
| m-4 lentille absente | faite (§ 3, en tête) |
| m-5 commentaire du lanceur (« jamais lue pour un seuil ») | à corriger dans le lanceur v4 (devis v2, § 5, point 5) ; noté |
| m-6 en-tête, nom neuf | fait |
| m-7 chemin des références | fait (§ 1) |

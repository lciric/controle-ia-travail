# Critère d'identité du réajustement de nos lentilles R et S — v1 (à contre-lire, puis sceller avant toute création)

- Heure (UTC) : 2026-11-19T10:07:54Z. Auteur : session des lentilles (auteur du devis ; déclaré). Pièce de **classe A** (critère décisif d'une course
  payante) : contre-lecture par un autre modèle lancée par la mère, puis scellement **avant** toute création de machine.
- Reprend le § 4 du devis v2 (`devis-reajustement-lentilles-b-beta-v2.md`, `49dcbc93…`) en levant la réserve majeure N-1 de sa
  vérification (`verification-difference-devis-reajustement-v1-v2.md`, `3cc64c86…`) : tolérance placée au-dessus du plancher mesuré,
  déclarée conventionnelle, mention renommée.
- Contexte : GO-2026-11-19-33 (mot de Lazar « 1 2 et 3 », pièce 3 : lecture des sondes de l'étape B bis avec nos lentilles, dans le
  billet). Aucune ligne de calcul à ce jour.

## Références du 18 novembre (pièces versées, `diag/20261118-164930-neuron-lens-b-beta/`)
- R : fichier d'ajustement `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c` (8 455 720 309 octets) ; 63 valeurs
  `diffs_float64` (`b-beta-ajustement-R.json`) ; empreintes par couche des matrices des moitiés (`matrices_moities`) et des fichiers
  exportés (`b-beta-export.json`).
- S : `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8` (8 589 938 049 octets) ; 64 valeurs `diffs_float64`.

## Plancher mesuré (calcul de la session, 2026-11-19, sur ces seules pièces)
Les trois versions des différences entre moitiés écrites par la course, calculées à partir des **mêmes sommes** par des chemins
numériques différents, s'écartent au plus de : R, `diffs` contre `diffs_float64` **3,48 × 10⁻⁵**, `diffs_recopie` contre
`diffs_float64` 1,52 × 10⁻⁶ ; S, **5,86 × 10⁻⁵** et 3,12 × 10⁻⁶. La plus petite valeur de `diffs_float64` est 3,53 × 10⁻³ (R) et
4,11 × 10⁻³ (S). Les sommes sont accumulées en simple précision sur la carte ; un réajustement sur une autre machine ajoute l'ordre des
réductions, **non mesuré**.

## Critère, lentille par lentille (chaque lentille jugée seule ; cas mixte : chacune rangée avec sa mention)
1. **Palier 1 — « même lentille, octets identiques »** : empreinte du nouveau fichier d'ajustement égale à la référence. (Le fichier ne
   porte ni heure ni chemin, et `torch.save` écrit les mêmes octets pour le même contenu : `essai_torch_save_octets_v1.py`,
   `4fdec19d…`, sortie `3a18c2c2…`.) Pour R, alors, les empreintes par couche des matrices des moitiés sont égales elles aussi : elles
   ne sont qu'une autre forme de l'égalité d'octets, pas une preuve de plus.
2. **Palier 2 — « lentille proche à 10⁻³ près sur les différences entre moitiés »** (sinon) : écart absolu maximal entre les nouvelles
   `diffs_float64` et celles du 18, sur toutes les couches et cibles (63 valeurs pour R, 64 pour S), **au plus 10⁻³**.
   - Tolérance **conventionnelle, déclarée telle** : ≈ 17 fois le plancher mesuré entre chemins de calcul (5,86 × 10⁻⁵), un centième
     du seuil de stabilité de la tranche (0,10), sous la plus petite valeur (3,5 × 10⁻³). Aucune pièce ne mesure l'écart d'un
     réajustement.
   - **Condition nécessaire, pas suffisante** : 63 ou 64 nombres résument des matrices de 4 096 × 4 096 ; la mention ne dit pas
     « équivalente », elle dit « proche sur les différences entre moitiés ».
   - Pour R, l'écart est complété, sans critère, par le compte des couches dont les empreintes des matrices des moitiés sont égales
     (rapporté).
3. **Au-delà — « lentille différente »** : rangée quand même, marquée telle ; **aucune lecture du programme ne la lit** sans nœud de
   Lazar (le texte de lecture v2 le dit de son côté).
4. **Reprise sur sauvegarde** pendant un ajustement : notée ; la lentille ne peut pas conclure au palier 1.
5. **Seconde mesure (variante B)** : ne décide rien de l'identité ; le verdict scellé et accepté du 18 reste ; la seconde course est lue
   par un lecteur neuf sur un plan scellé et rapportée à côté ; tout désaccord est un nœud de Lazar (devis v2, § 4, palier 3).

## Qui applique
Le calcul des empreintes et des écarts est fait **par programme** sur la machine (empreintes) et dans la session (écarts sur les pièces
versées), avant toute lecture d'une mesure de la nouvelle course ; le verdict d'identité est écrit, scellé et rapporté à Lazar par la
mère.

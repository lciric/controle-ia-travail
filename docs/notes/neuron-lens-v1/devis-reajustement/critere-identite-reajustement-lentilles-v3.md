# Critère d'identité du réajustement de nos lentilles R et S — v3 (à vérifier par le même contre-lecteur, puis sceller avant toute création)

- Auteur : session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`, modèle Claude Opus 5.5), auteur du devis (déclaré). Écrit le
  2026-11-19 ; relevé `date -u` à l'écriture : 2026-11-19T10:36:38Z (heure du scellement : celle du compagnon). Pièce de **classe A**.
- v3 = v2 (`critere-identite-reajustement-lentilles-v2.md`, `fc706d8e…`, archivée sans modification) corrigée selon sa vérification
  (`docs/notes/neuron-lens-v1/verification-critere-identite-reajustement-v2-v1.md`, branche principale, `8a6045bb…`, même
  contre-lecteur : « pas avant », D1 à D7 et quatre mineures). Traitement au § 9. Programme passé en v2 sous un nom neuf.
- v2 = v1 (`critere-identite-reajustement-lentilles-v1.md`, `1a5da7f2…`, archivée sans modification) corrigée selon sa contre-lecture
  (`docs/notes/neuron-lens-v1/contre-lecture-critere-identite-reajustement-v1.md`, branche principale, commit `a734884a`, `92419037…` ;
  contre-lecteur neuf, Fable 5.2 : « pas avant », C1 à C6 et sept mineures). Traitement au § 8.
- Contexte : GO-2026-11-19-33 (mot de Lazar « 1 2 et 3 » ; pièce 3 du billet). Aucune ligne de calcul à ce jour. **Ce critère prime sur
  la phrase « identité par les paliers 1 et 2 » du devis v2** (décision 1) ; le devis v3 (`devis-reajustement-lentilles-b-beta-v3.md`)
  l'intègre (décision de la mère : pas d'erratum sur une pièce de classe A).

## 1. Références du 18 novembre
Branche `claude/brave-galileo-jhp684` (pièces absentes de la branche principale) ; les empreintes font foi ; dossier
`diag/20261118-164930-neuron-lens-b-beta/` :
- `b-beta-ajustement-R.json` (`129c43b020854fd395cb0e969dd7f8956844417684e1e3a1099fee5e7f16d2ab`) : fichier d'ajustement de R
  `r-llama-3.1-8b-instruct-L32-dclm-T128.pt`, `31061d6c6c4b521c43d4710f9b660184b285467a065dadb5fc48e48c6d48c64c`, 8 455 720 309 octets ;
  `diffs_float64` 63 valeurs (32 `mid`, 31 `out`) ; `diffs` (simple précision) ; `meta` ; `n_docs` [466, 466] ; `next_doc` 932.
- `b-beta-ajustement-S.json` (`2dce646e32177941c02987a8ba3a0a67fd45d17f335e58ba9e321d3e0367c297`) : `aac70eef8f57b5d4423e5c8f8b2e77033b15077d95ef5a81894dbe3e0436e2b8`,
  8 589 938 049 octets ; 64 valeurs (32 et 32).
- `b-beta-export.json` (`17304c936792e4b79e9a47d78abf5bb6966310c36b92f387b3303b23891eedf1`) : pour R, `matrices_moities` (31 couches,
  deux empreintes) et `valeurs.npR_notre_R`, `valeurs.identite_notre_R` (28 couches chacune).
- Manifeste `runs/20261118-164930-neuron-lens-b-beta/manifeste.json` (`b90c15140074e9d41a3cf93e8bcaf55f80cc025d07d2d46432239d1c6b6e3444`) : `config.commit_voisin`
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
essais `tests/test_neuron_lens_comparer_reajustement_v1.py` (`0f5b5bdb…`) — **remplacé** par la v2 :
`src/controle_ia/neuron_lens/comparer_reajustement_v2.py` (`23311588f2d3b9f45a9b6b052e8de22742a164640585d7c1361c20dee2115877`), essais
`tests/test_neuron_lens_comparer_reajustement_v2.py` (`65822ab580d49fdf988de59b044ed61df24aed74e01e2e2a6c818c185b91f1ef`, 82 essais passés
le 2026-11-19 ; § 6).
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
     du texte source de la fonction dans les deux lanceurs) ; **provenance** : empreintes des deux fichiers d'ajustement présentes et bien
     formées, tailles présentes ; `finies` vrai des deux côtés ; pièces de référence (ajustement, manifeste et, pour R, export)
     d'empreintes égales à celles du § 1, **vérifiées par le programme** sur les octets lus ; course neuve distincte de celle du 18
     (identifiant de course et heure de début différents) ; manifeste neuf d'empreinte égale à celle que porte le résultat neuf ; champs
     `ajustement`, `correctifs`, `graines`, `modele`, `revision` et `corpus` de la configuration du manifeste égaux à ceux du 18 (la
     phrase permise « même code, même corpus, mêmes graines » ne s'appuie que sur eux) ; **pour R, pièces d'export présentes et complètes
     des deux côtés** (31 couches de matrices des moitiés, 28 couches finies par série).
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
4. **Anomalie** (mention suspendue, nœud de Lazar) : empreinte du fichier égale **et** l'un de ces faits : un préalable du point 2
   manqué (y compris la référence comparée à elle-même, qui n'est pas une course distincte) ; une taille différente ; un écart maximal sur
   `diffs_float64` supérieur à 10⁻⁹ (les mêmes sommes donnent la même valeur, à l'arrondi du calcul près) ; pour R, des pièces d'export
   absentes ou incomplètes, ou une empreinte de matrice des moitiés différente. Le programme calcule les préalables et la table des écarts
   aussi au premier palier.

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
  même code, le même corpus et les mêmes graines sur une autre machine. Les fichiers obtenus ne sont pas identiques à l'octet. Deux
  comparaisons restent possibles. La différence entre les deux moitiés du corpus, couche par couche, s'écarte d'au plus [écart mesuré] de
  celle du 18 novembre (tolérance fixée d'avance, par convention, à 10⁻³) ; cette grandeur ne voit pas un déplacement commun aux deux
  moitiés. Pour la lentille R seulement, l'écart maximal de chaque matrice à la lentille publique et à l'identité change d'au plus
  [valeur] et [valeur] d'une course à l'autre, pour des écarts qui valaient de [valeur] à [valeur] le 18 novembre ; aucun seuil n'était
  fixé d'avance pour ces deux séries. Pour la lentille S, aucune comparaison de ce genre n'existe. Nous ne savons pas si les lentilles
  réajustées lisent comme celles du 18 novembre. Les mesures du 18 novembre [n'ont pas été refaites sur elles | ont été refaites sur elles
  et sont rapportées à côté]. »
  (*“The two lenses measured on 18 November were destroyed with the rented machine. We refitted them with the same code, corpus and
  seeds on another machine. The files are not byte-identical. Two comparisons remain. The per-layer split-half difference deviates by at
  most [x] from the 18 November values (tolerance fixed in advance, by convention, at 10⁻³); this quantity is blind to any shift common
  to both halves. For lens R only, the largest entrywise gap of each matrix to the public lens and to the identity changes by at most [y]
  and [z] between the two runs, for gaps that ranged from [a] to [b] on 18 November; no threshold had been fixed in advance for these two
  series. No such comparison exists for lens S. We cannot establish that the refitted lenses read like those measured on 18 November. The
  18 November measurements [were not repeated on them | were repeated on them and are reported alongside].”*)
  **Ces chiffres sont obligatoires**, quel que soit leur sens, dans toute phrase du billet et du texte de lecture qui cite la lentille R au
  deuxième palier, et dans l'avertissement à Lazar ; **aucun qualificatif** ne leur est attaché (« inchangé », « stable », « négligeable »,
  « a bougé »), faute de seuil fixé d'avance. Le programme les rend (`series_export_R_sans_critere` : écart par couche, écart maximal,
  plus petite et plus grande valeur du 18).
  Phrases interdites : « nous avons réajusté à l'identique les lentilles jugées le 18 novembre » ; « la lentille réajustée est proche de
  l'originale », « équivalente », « la même à la précision numérique près » ; « le verdict “partiel” du 18 novembre vaut pour la lentille
  employée ici » ; « la distance à la lentille publique est inchangée », ou toute phrase qui tire des séries de R un appui à la
  proximité ; toute phrase qui prête à la lentille réajustée une mesure faite sur celle du 18. (*“We refitted the same lenses”;
  “the refitted lens is close/equivalent to the original”; “the 18 November verdict applies to the lens used here”.*)
- **« Différente » ou « non comparable »** : rangée, marquée ; aucune lecture sans nœud de Lazar.
- **Dans tous les cas** : tout usage dans une lecture passe par un texte de lecture neuf, contre-lu, qui recopie la mention et l'écart
  mesuré, et par le mot de Lazar (GO-2026-11-19-33) ; le billet dit le palier obtenu, quel qu'il soit, et, si la lentille n'est pas lue,
  le dit en une phrase ; la mention est écrite dans un fichier compagnon au lieu de rangement et à l'inventaire.

## 5. Audit, le même dans les deux sens
**Déclencheurs** : (i) palier 1 obtenu ; (ii) écart maximal exactement nul avec des octets différents ; (iii) « différente » ; (iv) « non
comparable » ; (v) pour R, empreinte du fichier égale et une empreinte de matrice des moitiés différente (palier 1 suspendu).
**Audit, fait par la mère ou par l'agent neuf du § 7, sans lire aucune mesure de la course** : le programme du § 6 donne les préalables,
la comparaison des manifestes et la table des écarts ; la relecture de l'empreinte au lieu de rangement, les versions du pilote et le
modèle de carte sont relevés à la main, avec chemin et empreinte ; l'audit dit ce qui vient du programme et ce qui est relevé à la main.
Provenance des deux côtés (l'empreinte neuve vient du fichier de la
course neuve — identifiant, heure, taille — et est relue au lieu de rangement après la copie ; la référence est lue dans la pièce du 18 par
son empreinte ; les deux ne sortent pas du même fichier) ; table des différences de `meta`, des commits, des versions de bibliothèques,
du pilote et du modèle de carte ; table des écarts par couche et par cible, avec leur signe. L'audit est versé scellé avec le verdict
d'identité ; un contrôle manqué suspend la mention et ouvre un nœud de Lazar. **Aucune relance pour obtenir un autre palier sans devis
neuf et mot de Lazar.**

## 6. Programme et essais (scellés avant la création ; R5)
`comparer_reajustement_v2.py` lit les fichiers, calcule leurs empreintes, vérifie les pièces de référence contre le § 1, rend la mention,
les déclencheurs, les préalables, les tables, le compte des matrices égales et les séries de R ; il verse la ligne de commande dans sa
sortie et refuse d'écraser une sortie (R12). La tolérance est une constante (10⁻³), la mention est bâtie sur elle. Une valeur non finie,
non numérique ou absente rend « non comparable » (ou suspend le premier palier) **avant** tout maximum.
**82 essais**, sur les pièces du 18 lues par leurs empreintes vraies et sur des copies altérées en mémoire :
- **cas sains** : premier palier sur une copie d'une course distincte (identifiant, heure de début et manifeste neufs), R et S ;
  deuxième palier, écart nul, déclencheur (ii), 63 et 64 écarts ;
- **bords** : 0,999 × 10⁻³ et −0,999 × 10⁻³ → deuxième palier ; ±1,001 × 10⁻³, ±2 × 10⁻³, −0,05 → « différente », signe gardé dans la
  table ; écart d'exactement 10⁻³ (0,005 − 0,004) → deuxième palier ; constante 10⁻³ ;
- **premier palier** : valeur déplacée, `nan`, `n_docs`, `meta` absent, taille, export sans matrices, matrice différente (30 sur 31
  comptées) → suspendu ; reprise notée ;
- **provenance** : empreinte neuve absente, vide ou mal formée ; empreintes absentes des deux côtés ; référence contre elle-même
  (suspendu, course non distincte) ; `finies` faux ; référence et neuf échangés ; manifeste de référence faux ; manifeste neuf non porté
  par le résultat ; chacun des six champs de configuration changé → « non comparable » ;
- **forme** : `nan`, `inf`, absent, texte, booléen, de chaque côté et sur `diffs` comme sur `diffs_float64` ; 62 valeurs ; une cible de
  plus ; séries vides des deux côtés ; série qui n'est pas une liste ; `meta` absent des deux côtés ; `meta` changé ; `n_docs`, `next_doc`,
  nom de chaque côté ; nom, commit et fonction absents des deux côtés ; fonction différente → « non comparable » ;
- **exports de R** : export neuf ou de référence absent, série absente, 27 couches, série `nan`, export de référence faux → « non
  comparable » ; une valeur de série déplacée de 0,0123 retrouvée dans la sortie, 28 couches comptées, sans changer la mention ; S sans
  objet ; changement de côté du seuil rapporté ;
- **ligne de commande** : référence contre elle-même suspendue, ligne de commande versée, sortie non écrasée.
Dix altérations du programme (tolérance 1,5 × 10⁻³, « < » au lieu de « ≤ », écart signé, `meta` absent tenu pour égal, premier palier sans
empreinte, anomalie des matrices retirée, `finies` non lu, finitude des séries non lue, cohérence du premier palier retirée, écart des
séries forcé à zéro) sont toutes tuées par ces essais (essai de la session, hors dépôt). Le programme est une pièce de classe B : vérifié
avec ce critère.

## 7. Qui applique
Les empreintes sont calculées par programme sur la machine. Les écarts sont calculés par le programme scellé du § 6, **dont l'empreinte
est vérifiée avant le lancement**, sur les pièces **prises sur la branche de résultats poussée par la machine** (commit noté), jamais sur
une copie remise par la session des lentilles, **par la mère ou par un agent neuf qu'elle lance**, et non par la session des lentilles,
avant toute lecture d'une mesure de la nouvelle course ; pour R, les deux pièces d'export sont toujours fournies ; l'indication d'une
reprise est lue au journal de la course ; la ligne de commande et la sortie sont versées scellées avec le verdict ; le verdict d'identité
est écrit, scellé et rapporté à Lazar par la mère.

## 8. Traitement de la contre-lecture de la v1 (gardé de la v2)
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

## 9. Traitement de la vérification de la v2 (`8a6045bb…`)
| correction | traitement |
|---|---|
| D1 premier palier sans contrôle | faite : § 3, point 4 ; programme v2 (préalables et table au premier palier, cinq causes d'anomalie) ; essais S1, S2, S3, S9 et matrice |
| D2 préalables de provenance | faite : § 3, point 2 ; programme v2 (empreintes des pièces de référence vérifiées, course distincte, manifeste neuf, six champs) ; essais S4, S5, S8, S19, S20, manifestes, six champs |
| D3 exports de R obligatoires | faite : § 3, point 2 ; programme v2 ; essais S6, S7, S10, 27 couches, `nan`, export faux |
| D4 essais des gardes survivantes | faite : 82 essais (§ 6) ; dix altérations tuées |
| D5 phrase du billet et séries de R | faite : § 4 (« Deux comparaisons restent possibles », chiffres obligatoires sans qualificatif, phrase interdite ajoutée ; S écrit) |
| D6 qui fait l'audit, d'où viennent les pièces | faite : § 5 et § 7 |
| D7 devis | faite : devis v3 (pas d'erratum, décision de la mère) ; erratum v1 retiré du circuit, archivé |
| m-1 heure | relevée par `date -u` à l'écriture ; l'heure du scellement est celle du compagnon |
| m-2 tolérance en dur | faite : constante, mention bâtie sur elle, paramètre retiré |
| m-3 « ou plus récent » | retiré |
| m-4 noms neufs | faits : critère v3, programme v2 et ses essais |

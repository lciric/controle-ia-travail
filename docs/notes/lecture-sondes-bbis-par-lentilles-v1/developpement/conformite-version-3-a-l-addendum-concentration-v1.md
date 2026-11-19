# Conformité de la version 3 préparée à l'addendum « concentration » (brouillon candidat) — point par point — v1

Demandé par la mère (message du 2026-11-19, 12:25 UTC ; donnée d'une autre session). Addendum lu en entier :
`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`, `0a862760025caf11ff66578dc47c53143ee480c173a733920b9f4b9425d59546`
(vérifiée), branche `claude/brave-galileo-jhp684`, commit `6de58b8c` ; **brouillon candidat, non contre-lu, non scellé par la mère**.
Version 3 préparée : commit `e2e24cac` (`statistiques_v2.py` `b6c291e3…`, `lanceur_v3.py` `d88dd911…`). Je n'ai ouvert aucune des six
pièces de l'addendum, ni rien d'autre de cette branche. Aucun code modifié pour cette note.

**Verdict : le calcul de la version 3 est conforme à l'addendum, sans écart. Il manque trois choses, qui ne sont pas du calcul : une
garde de registre (EC-4) et deux essais (EC-5). La version 3 n'est donc pas encore le code de l'addendum.**

| point de l'addendum | version 3 | conforme ? |
|---|---|---|
| EC-1, concentration de u_j sur les M − 1 autres ; écart type de population ; formules exactes ; double précision | `statistiques_v2.concentrations_sans_soi` : mêmes formules pour m^(−j) et (s^(−j))², double précision, moyenne et variance recalculées en double | oui |
| EC-1, arrêt si la variance des M − 1 autres est nulle ou ne dépasse pas 10⁻¹⁰ fois celle des M | `if not (var_sans > 1e-10 * var).all(): Arret` | oui |
| EC-1, C(v) avec m_t et s_t des M directions | `lecture_signe` et `z_scores` de `statistiques_v1`, inchangés | oui |
| EC-2, part de u_j : ses vingt plus grands scores bruts, « dépasse » strict, quantile 0,99 des M − 1 autres, interpolation linéaire, h = 0,99 × (n − 1) | `quantiles_sans_soi` : rang fractionnaire 0,99 × (M − 2), statistiques d'ordre du jeton ; comparaison stricte ; essai contre `numpy.quantile` sur la ligne privée de u_j, égalités comprises | oui |
| EC-2, v et témoins : quantile des M (h = 1 979,01) | `ResumeNul.quantile`, inchangé | oui |
| EC-3, témoins jugés comme la direction lue ; bornes de valeurs inchangées, loi de référence bêta-binomiale | `p_temoins` inchangé ; `audits_v1` inchangé ; les 41 bornes du § 7 recalculées par `audits_v1.bornes_calibration` : **égales** (contrôle joué pour cette note, non encore un essai) | oui pour le code ; **le mot « exacte » de la docstring de `audits_v1` devient « de référence, approchée »** : `audits_v1` ne peut pas être réécrit (R12) ; à dire dans la note de version, ou `audits_v2` si la mère le veut |
| EC-4, clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` exigée avant `ENTREES-LENTILLES-BBIS` et avant tout calcul ; absente : rien ne part | **non codé** : ni `entrees_v2` ni `lanceur_v3` ne lisent cette clé | **non** — à coder (`entrees_v3`, `lanceur_v4`), si la mère ratifie la clé (point ouvert 4 de l'addendum) |
| EC-5, essai sain : égalité à un calcul direct sur les M − 1 autres | `directions_nulles_sans_elles_memes_egales_a_un_calcul_direct` (4 tailles) | oui |
| EC-5, artefact : la statistique d'origine rend des concentrations strictement plus petites | `artefact_statistique_du_texte_d_origine_differente_et_plus_petite` | oui |
| EC-5, artefact de taux à petite taille : M = 19, 128 jetons gaussiens indépendants, 2 000 répliques, part entre 0,03 et 0,065 | **essai absent sous cette forme** (le mien : M = 200, scores lus par la lentille des logits) ; joué pour cette note : **0,0435** sous la statistique corrigée, 0,487 sous celle d'origine (addendum : ≈ 0,045 et ≈ 0,47) | **non** — essai à ajouter |
| EC-5, arrêt : jeton constant sur les autres | `sans_soi_moins_de_trois_directions_ou_jeton_constant_arret` | oui |
| EC-5, bornes égales aux 41 bornes du § 7 | **essai absent** (seuls les quatre exemples du texte et le programme scellé des bornes sont éprouvés) ; contrôle joué : égales | **non** — essai à ajouter |
| § 4, 1 à 3 : quantile sur 1 999 valeurs ; v, témoins et z des tables sur les M | ci-dessus | oui |
| § 4, 5 : repli par direction et nul des signes sous la même règle ; pôles, familles, jeton de début inchangés | `lanceur_v3` appelle le même `resumer_nul` pour les trois nuls ; `poles_alignes`, familles et jeton de début repris de `statistiques_v1` | oui |
| § 4, 6 : moins de trois directions nulles : arrêt | `if m < 3: Arret` | oui |

## Ce que je ferai quand la mère dira que l'addendum est scellé (ou contre-lu) et que la clé EC-4 est ratifiée

Sous des noms neufs, sans toucher à `statistiques_v2.py` : `entrees_v3` (clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` exigée, citant
l'addendum scellé par son chemin et son empreinte, antérieure à toute ouverture des sondes) ; `lanceur_v4` ; les deux essais manquants et
ceux de la garde (cas sain, clé absente, empreinte d'un autre texte). L'empreinte de l'addendum scellé sera une constante du code :
**il me faut l'empreinte finale**, qui ne sera pas `0a862760…` si la contre-lecture change le texte.

## Remarques sur le texte de l'addendum (sans rien trancher)

- § 4, ligne 5 du tableau des hypothèses : il écrit qu'aucun `audits_v2` n'est demandé ; d'accord, sous la réserve du mot « exacte »
  ci-dessus.
- EC-4 ne dit pas si le **montage** doit aussi exiger la clé ; je la lis comme exigée au calcul et à l'ouverture des sondes seulement
  (« avant `ENTREES-LENTILLES-BBIS` et avant toute exécution du calcul du point 6 »), le montage restant permis avant.
- EC-4 ne dit pas quel chemin et quelle empreinte la ligne porte ; je suppose : l'addendum scellé lui-même.

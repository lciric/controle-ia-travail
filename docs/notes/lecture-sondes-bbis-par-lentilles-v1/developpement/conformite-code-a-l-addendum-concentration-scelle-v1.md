# Conformité du code de la première passe à l'addendum de concentration scellé — point par point — v1

Écrite par le développeur neuf des deux passes (mandat `mandats/mandat-developpeur-deux-passes-lentilles-v1.md`,
`0a9517ea4e1d7460b411a0914996503eb3c6a9a680b4d3c88ae9d4f1f67bbdfc`, vérifié), le 2026-11-20, étape 1. Pièce de travail (classe C)
qui accompagne un code de classe B.

- **Texte** : `prereg/lecture-sondes-bbis-par-lentilles-v1.md`, `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`
  (lu sur la branche principale, par `git show` ; empreinte recalculée, égale).
- **Addendum scellé** : `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`,
  `7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970` (compagnon vérifié sur cette branche ; lu en entier).
- **Code jugé** : `src/controle_ia/lentilles_sondes_bbis/` : `entrees_v3.py`, `statistiques_v3.py`, `lanceur_v4.py` (neufs), et les
  dix modules qu'ils emploient sans les changer (`__init__`, `constantes_v1`, `entrees_v2`, `montage_v1`, `lecture_v1`, `nuls_v1`,
  `statistiques_v1`, `statistiques_v2`, `audits_v1`, `phrases_v1`). Empreintes : `empreintes-code-v4.txt` (ce dossier).
- **Cette note ne recopie pas** la note `conformite-version-3-a-l-addendum-concentration-v1.md`, écrite contre le brouillon 1
  (`0a862760…`) : la conformité est refaite ici contre le texte scellé, § 3, § 4, § 12 et § 12 bis.

**Verdict du développeur : chaque point de EC-1 à EC-6 et de C1 à C5 est codé et éprouvé (cas sain et artefact). Quatre précisions
de lecture ont été prises pour coder (§ 3 ci-dessous) ; aucune n'ajoute une règle de décision, toutes vont dans le sens sévère ou
n'écrivent qu'un champ ; elles sont à contre-lire. Aucun nœud bloquant n'est ouvert par le développeur.**

## 1. Les six points d'écart de l'addendum (§ 3)

| point de l'addendum scellé | ce que fait le code | essais (table `table-essais-v2.md`) | conforme ? |
|---|---|---|---|
| **EC-1**, concentration de u_j : C(u_j) = max_t z_t^(−j)(u_j), moyenne et écart type de population des M − 1 autres ; C(v) avec m_t et s_t des M directions | `statistiques_v3.resumer_nul` appelle `statistiques_v2.concentrations_sans_soi` (module inchangé, `b6c291e3…`, formules de EC-1 : m^(−j) = (M·m − a_j)/(M − 1), (s^(−j))² = (M·s² − (a_j − m)²·M/(M − 1))/(M − 1), double précision, moyenne et variance recalculées en double) ; C(v) : `lecture_signe`, z sur les M directions (`statistiques_v1.z_scores`) | calcul direct sur les M − 1 autres (4 tailles) ; relation φ ; artefact de la statistique d'origine | oui |
| **EC-1 / C5**, précision : calcul en double précision ; C(u_j) rendu en simple précision comme C(v) ; comparaison C(u_j) ≥ C(v) en simple précision, une égalité compte contre v | `concentrations_sans_soi` rend un tenseur en simple précision ; `resumer_nul` s'arrête s'il ne l'est pas ; `statistiques_v3.p_concentration` ramène C(v) en simple précision et compare par `>=` ; refus de concentrations nulles d'une autre précision. Les témoins : `statistiques_v1.p_temoins`, concentrations en simple précision des deux côtés, `searchsorted` à gauche (une égalité compte contre le témoin) | `comparaison_des_concentrations_en_simple_precision_…` ; `concentrations_nulles_rendues_en_simple_precision` ; `p_de_concentration_…_selon_la_meme_regle` | oui |
| **EC-1**, arrêt : variance des M − 1 autres nulle ou au plus 10⁻¹⁰ fois celle des M | `concentrations_sans_soi` : `if not (var_sans > 1e-10 * var).all(): Arret` ; l'écart type des M nul est arrêté avant (`resumer_nul`) | `arret_variance_des_autres_nulle_pour_un_jeton` | oui |
| **EC-2**, part de u_j : ses vingt plus grands scores bruts, « dépasse » strict, quantile 0,99 des M − 1 autres par interpolation linéaire, h = 0,99 × (n − 1) ; v et témoins : quantile des M | `statistiques_v2.quantiles_sans_soi` (inchangé : rang fractionnaire 0,99 × (M − 2), statistiques d'ordre du jeton) ; comparaison stricte ; v : `ResumeNul.quantile` (M directions, `torch.quantile`, interpolation linéaire) | calcul direct (interpolation écrite en toutes lettres) ; rang fractionnaire à M = 2 000 (1 978,02 et 1 979,01) | oui |
| **EC-3**, calibration : témoins jugés comme la direction lue, directions nulles sans elles-mêmes ; loi « de référence », « approchée, non exacte » ; bornes de valeurs inchangées, égales à celles du programme de l'addendum | `p_temoins` inchangé ; `audits_v1.bornes_calibration` inchangé ; les tables écrivent la loi comme « de référence […] approchée, non exacte » (`lanceur_v4.LOI_CALIBRATION`) | exemples du plan ; 41 bornes du § 7 ; programme de l'addendum rejoué ; sortie scellée du programme | oui ; **docstring de `audits_v1`** : § 2 ci-dessous |
| **EC-4 / C1**, clé `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` : une seule ligne, avant `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS` ; la fiche du code porte le chemin et l'empreinte de l'addendum ; le code les compare à la ligne avant toute requête ou ouverture ; le manifeste et les tables les citent à côté de l'empreinte du texte ; absente, en plusieurs lignes, inscrite après l'une des deux, ou d'une autre empreinte que celle de la fiche : rien ne part | `entrees_v3.exiger_addendum` (une ligne ; chemin et empreinte égaux aux constantes du code, `7c738708…`, et à ce que porte la fiche ; place et heure) ; `lanceur_v4.exiger_fiche_code` lit le champ `addendum_concentration` {`chemin`, `sha256`} de la fiche et le compare à la ligne ; appelée en tête du montage, du calcul et de la sous-commande `recuperer` ; `entrees_v3.ouvrir_entrees` et `recuperer_entrees` refont le contrôle de la ligne ; rapport du montage, tables (`addendum`), manifeste (`addendum`, `config.addendum`, `fiche_code.addendum`) citent chemin et empreinte | registre jouet : 1 cas sain, 8 artefacts ; fiche : 1 sain, 4 artefacts ; montage : 4 artefacts « avant toute requête » ; calcul ; ligne de commande ; bout en bout | oui ; **précisions 1 et 2**, § 3 |
| **EC-5 / C2, C3**, essais | tous écrits : cas sain (calcul direct) ; artefact (statistique d'origine plus petite) ; artefact de taux à petite taille, **chaque réplique tirant ses 19 directions nulles et sa direction témoin** (un tirage de 20 colonnes par réplique, graine `lentilles-bbis/essai/taux-a-petite-taille`) ; arrêts (jeton constant sur les autres ; deux directions ; trois directions distinctes : pas d'arrêt) ; clé de l'addendum ; bornes (exemples ; 41 bornes) | fichier `test_lentilles_sondes_bbis_addendum_concentration_v2.py` | oui |
| **EC-6**, étage (i), direction lue : égalité entre la vingtième et la vingt-et-unième valeur (égalité exacte, simple précision) de toute liste qui entre dans une table ou une comparaison : arrêt nommé avant toute écriture de table | `statistiques_v3.premiers_gardes` relève les vingt-et-un plus grandes valeurs ; `exiger_sans_egalite` lève `EgaliteDirectionLue` (« égalité de score au vingtième rang d'une direction lue », avec cellule, pli, rôle, vecteur, signe, lentille, couche, liste, deux identifiants, valeur commune). Listes gardées : vingt premiers par score (chaque vecteur, chaque signe, les deux lentilles : `lecture_signe`) ; vingt premiers par z sous le nul isotrope, partagé ou refait par direction (`lecture_signe`) ; listes du témoin de couche, deux signes, aux trois couches (`lanceur_v4._Couche._temoin_de_couche`) ; dix pôles par cosinus (`statistiques_v3.poles_alignes`, dixième et onzième valeurs) ; dix premiers jetons de la lecture de chaque pôle (`_Couche._poles`). Les comparaisons (jetons communs, accord des lentilles, déclencheurs d'audit) n'emploient que ces listes | cas sains et artefacts de chaque liste au niveau du module ; 2 cas sains et 5 artefacts dans le calcul d'une couche du lanceur ; arrêt dans le calcul entier | oui ; **précision 3**, § 3 |
| **EC-6**, étage (ii), direction nulle (nul isotrope partagé, refait par direction, nul des signes ; liste par score) : marquée ; S_min, S_max ; p_bas, p_haut ; valeur p écrite : p_haut, p_bas à côté ; attendu d'une famille sur les seules directions non marquées ; libellé calculé avec p_bas sous les deux nuls puis p_haut sous les deux nuls ; égaux : continue ; différents : arrêt nommé | `resumer_nul` marque (`marquee`) ; `bornes_de_departage` et `bornes_min_max` : S_min = base + max(0, places − (égaux − égaux qui comptent)), S_max = base + min(places, égaux qui comptent), pour la part (en compte) et chaque famille ; `p_bornes` ; `lecture_signe` écrit `p_part` = p_haut, `p_part_bas`, `p_part_haut`, et pour chaque famille `p` = p_haut, `p_bas`, `p_haut`, `attendu` (non marquées), `directions_nulles_marquees` ; `libelle_sous_departage`, appelée par `lanceur_v4._etiqueter` pour la part et chaque famille, lève `EgaliteNulleDecisive` (« égalité au vingtième rang d'une direction nulle, décisive pour un libellé », avec la direction lue, la lentille, les nuls, la statistique, p_bas, p_haut, le nombre de directions marquées) | sains : bornes à un cran pour une famille et pour la part ; direction hors de portée ; sans direction marquée ; énumération de tous les départages (6 cas) ; artefact M = 99 ; libellé de la part aux deux bornes ; dans `_etiqueter` | oui ; **précision 4**, § 3 |
| **EC-6**, étage (iii), témoin : pas d'arrêt ; nombre de témoins à égalité écrit par (couche, lentille, nul) ; concentration, pôles (cosinus maximal, rang) et bornes non concernés | `egalites_temoins` ; `_Couche._compter` ; tables : `couches/<couche>/lentilles/<lentille>/egalites_au_vingtieme_rang/<nul>` et total `egalites_au_vingtieme_rang` | témoin à égalité : compte 1, valeurs p et compte de calibration inchangés | oui |
| **EC-6**, « Liste d'arrêt » : deux lignes ; au montage, compte des paires de jetons gardés dont les lignes de `lm_head.weight` sont égales octet pour octet, écrit, sans arrêt (H2) | les deux arrêts nommés ci-dessus ; `statistiques_v3.paires_de_lignes_egales`, appelée par `lanceur_v4.monter` sur les lignes gardées, écrite dans le rapport du montage (`lignes_de_sortie_egales`) | paires comptées (0 ; 1 ; 3 pour trois lignes égales ; lignes égales en valeur mais différentes d'un octet : non comptées) ; bout en bout | oui ; lignes comparées dans la précision où elles sont chargées (conversion exacte de bfloat16, qui ne confond pas deux lignes d'octets différents) |
| **EC-6**, liste de moins de vingt-et-un jetons (jouets) : garde sans objet, écrit | `premiers_gardes` (`objet`) ; `garde_egalite.sans_objet` et sa note dans chaque lecture ; `garde_sans_objet` dans les comptes | 15, 20 et 21 jetons | oui |

## 2. Les sept décisions du § 4 et les six hypothèses du premier développeur

| § 4 | code | conforme ? |
|---|---|---|
| 1. quantile 0,99 des M − 1 autres, interpolation linéaire sur 1 999 valeurs | `quantiles_sans_soi` | oui |
| 2. direction lue et témoins sur les M directions | `lecture_signe`, `p_temoins` | oui |
| 3. z des tables, classement par z, rang empirique sur les M directions | `lecture_signe` | oui |
| 4. bornes de calibration inchangées ; 41 valeurs du § 7 | `audits_v1` | oui |
| 5. repli par direction et nul des signes sous la même règle ; pôles, familles, jeton de début inchangés | `lanceur_v4._Couche` appelle le même `resumer_nul` pour les trois nuls ; `poles_alignes` : seule la garde d'égalité de la liste de dix est ajoutée, la concentration des pôles et son p sont ceux de `statistiques_v1` | oui |
| 6. arrêt : variance des autres ; moins de trois directions nulles | `concentrations_sans_soi` | oui |
| 7. garde d'égalité au vingtième rang | § 1, EC-6 | oui |

**La docstring « exacte » de `audits_v1`.** L'addendum (§ 4, hypothèse 5) dit : « `audits_v1` les porte déjà, aucun `audits_v2`
n'est demandé par l'addendum ». `audits_v1.py` (`86cda9a3…`) n'est donc ni réécrit (R12) ni remplacé. Sa docstring appelle « loi
exacte » la loi bêta-binomiale (n ; 100 ; M − 99) ; l'addendum (EC-3, § 7) la nomme « loi de référence », « approchée, non
exacte ». **Le mot « exacte » de cette docstring se lit « de référence, approchée »** ; le calcul et les bornes ne changent pas ;
ce que le code écrit (tables, champ `conventions.loi_des_bornes_de_calibration`) emploie les mots de l'addendum. Un essai le tient
(`les_tables_disent_la_loi_de_reference_approchee`). Si la session des lentilles préfère un `audits_v2` qui ne change que ce mot :
c'est une copie d'une ligne, à sa demande.

## 3. Précisions de lecture prises pour coder (aucune n'ajoute une règle ; à contre-lire)

1. **« Inscrite avant » (EC-4)** : jugé sur le registre propre lui-même, dont les lignes sont ajoutées et jamais réécrites : la
   ligne de l'addendum est placée plus haut que toute ligne `CODE-LENTILLES-BBIS` et `ENTREES-LENTILLES-BBIS`, **et** son heure
   n'est postérieure à aucune des leurs. Une ligne de la même seconde, placée avant, est « inscrite avant » ; une ligne placée
   avant mais d'une heure postérieure, ou placée après, est refusée. Le texte ne dit pas lequel des deux critères employer : les
   deux sont exigés.
2. **Forme de la fiche du code (EC-4)** : l'addendum dit que la fiche « porte le chemin et l'empreinte de l'addendum scellé »
   sans nommer le champ. Le code attend, dans la fiche citée par `CODE-LENTILLES-BBIS`, un champ **`addendum_concentration`** :
   `{"chemin": "prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md", "sha256": "7c738708…"}`, à côté des
   champs `commit`, `fichiers`, `essais`, `contre_lecture`. **La session principale, qui écrit la fiche, doit l'y mettre**, et
   `fichiers` doit porter les **treize** modules de `lanceur_v4.MODULES`. La ligne est comparée à la fiche **et** aux constantes
   du code (mandat : « l'empreinte de l'addendum dans le code est `7c738708…` »). La sous-commande `recuperer` vérifie désormais la
   fiche du code (argument `--depot`), puisqu'elle fait une requête.
3. **Listes d'une direction lue hors de l'énumération de EC-6 (i)** : la relecture de l'audit de symétrie par un chemin
   indépendant (`audits_v1.relire_par_chemin_independant`, inchangé) classe ses scores en double précision et en tire vingt
   premiers ; l'addendum ne la nomme pas. Le code **n'ajoute aucun arrêt** : il écrit, dans l'audit, si cette relecture a une
   égalité au vingtième rang (`egalite_au_vingtieme_rang_de_la_relecture_en_double_precision`), pour que rien ne soit tranché en
   silence. La liste du calcul à laquelle elle est comparée est, elle, déjà gardée. La garde de la fonction de lecture du montage
   (dix premiers jetons de 64 colonnes de `W_down`, plan, point 5) n'est pas une liste d'une direction lue : elle garde sa propre
   règle (« au rang près », quasi-égalités comptées), inchangée.
4. **Attendu d'une famille quand toutes les directions d'un nul sont marquées** : la moyenne « sur les seules directions non
   marquées » n'existe pas ; le code s'arrête (« valeur non finie dans un nul », ligne existante de la « Liste d'arrêt »). Sans
   objet à M = 2 000.

Deux choix d'écriture, sans effet sur une valeur : la **part** d'une direction nulle est tenue par son compte entier (nombre des
vingt premiers jetons au-dessus du quantile), et la comparaison P(u_j) ≥ P(v) se fait sur les comptes, à k égal (même relation
d'ordre, sans arrondi) ; les tableaux gardés portent, pour chaque direction nulle, `marquee`, `part_min`, `part_max`,
`famille_<nom>_min`, `famille_<nom>_max` (au lieu de `part` et `famille_<nom>`).

## 4. Le message de l'arrêt (i) et le cloisonnement de l'opérateur — à porter à la session des lentilles

L'addendum exige que le message de l'arrêt (i) donne « les deux identifiants de jeton et la valeur commune ». Ce message sort par la
ligne de commande (`ARRÊT : …`, sortie d'erreur) et il est écrit dans `versement/<run>/calcul-interrompu/arret.json`. **L'opérateur,
qui « ne lit que les codes d'arrêt », verrait donc, à cet arrêt, deux identifiants de jeton et un score d'une direction lue.** Le
code suit l'addendum à la lettre ; je ne propose aucun écart. À dire à l'opérateur, ou à trancher, par la session des lentilles.

## 5. Ce que la contre-lecture de l'addendum laissait « souhaitable, non exigé »

§ 12 bis de l'addendum : deux essais souhaitables, non exigés (plusieurs directions marquées ; une égalité sur trois valeurs à
cheval sur le vingtième rang). Le second est écrit (énumération, rangs 19 à 21, 20 à 22, 18 à 20 avec un quatrième au rang 21).
Le premier ne l'est pas sous la forme « plusieurs directions marquées dans un même nul » : non exigé ; à la demande.

## 6. Remarque de la vérification de la version 2 du code, reprise (hors addendum, déclarée)

`traitement-contre-lecture-v1-complement-2.md`, § 1 : remarque non bloquante du contre-lecteur du code, « à porter dans la version
suivante » : le manifeste mettait `None` en silence si le rapport du montage manquait. `lanceur_v4` l'exige au départ du calcul
(« rapport du montage absent du dossier de sortie : le manifeste ne pourrait le citer ; rien ne part ») et le cite toujours ; essai
à artefact. C'est le seul changement de `lanceur_v4` qui ne vienne pas de l'addendum.

## 7. Ce qui n'est pas fait, et pourquoi

- Aucun module existant n'est réécrit (R12). `lanceur_v4.py` est fabriqué à partir de `lanceur_v3.py` par remplacements exacts,
  chacun trouvé une fois et une seule (`outils/fabrique-lanceur-v4-v1.py`) : la différence entre les deux est la liste de ces
  remplacements.
- Aucune règle de départage : elle appartient à la version 2 du texte (seconde passe, étape 2).
- La voie exacte (§ 9, point 2 de l'addendum) n'est pas codée : hors de la décision.
- Réseau réel, tokeniseur réel, lentille réelle : non éprouvés (mandat) ; réserves inchangées de `notes-developpement-v1.md`, § 4.

# Contre-lecture — additif 3 au préenregistrement de la ligne 3 (puissance de la règle de portée à 200 témoins) — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel, `date -u` : 08:34Z à la première heure relevée), sur le mandat `mandat-contre-lecteur-additif-3-portee-200-v1.md` (`5750043c870eb31c1aa9a81673f64aebafa7b50d29a04aa55033e635f53ab6cc`, égale à son compagnon, contrôle fait par `sha256sum -c` avant tout autre geste), sous GO-2026-11-20-26, règle R2. Contre-lecteur neuf, modèle O : je n'ai écrit ni le texte, ni un additif, ni le code, ni le verdict de l'étage 1.

**Règle d'aveugle tenue.** Je n'ai ouvert aucune mesure de l'étage 1 : ni dossier d'exécution, ni dossier de verdict, ni verdict scellé, ni fichier de résultat. Ce que je sais de l'étage 1 est ce que le mandat donne : verdict « non, pas à cette taille » ; tolérance tenue à 200 et 400, pas à 100 ; puissance qui décide à n = 100 : 0,160. Aucune commande de liste ; une commande simple par appel ; le banc lu, jamais lancé ni importé ; rien sous `archives-reponses-modeles/` ; aucune écriture dans le dépôt.

## Verdict

**À corriger.** Trois corrections exigées, toutes de texte (§ 9) : la phrase qui dit ce que l'additif ne change pas est trop large (le plafond de 25 USD est un seuil du texte, l. 193, que l'additif lit à 88,36 USD) ; une contradiction entre le § 4.1 (ordre des gestes (6) à (11) gardé) et le § 4.2 (la ligne du geste (7) dite déjà donnée) ; un déclencheur de l'audit de symétrie qui ne joue que dans un sens (règle R4). Aucune ne touche la mesure, les graines, la règle de lecture A, B, C, ni un montant. Ces trois corrections faites, l'additif est scellable.

Ce qui tient, vérifié : la mesure est celle du texte à n = 200 seulement ; les 210 cellules et les treize mondes faisables (recalculés) ; la faisabilité ne dépend pas de n (code et l. 236 à 241) ; les graines ; la règle de lecture, complète et sans recouvrement ; les 1 004 appels et les 44,78 USD (recalculés) ; la citation de la ligne GO-2026-11-20-26, égale à l'octet.

## Pièces vérifiées

Tirées de main par `git fetch origin main` (tête `2d8055a49068bfabbb62d5bdc0e0c46f1d6763f9`), puis `git show` redirigé vers mon dossier ; empreintes recalculées.

| pièce | sha256 recalculée | égale à l'attendue |
|---|---|---|
| texte, version 7 (`prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | oui |
| additif 1, version 2 | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` | oui |
| additif 2, version 3 | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` | oui |
| devis, version 7 | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` | oui |
| `registres/go.md`, tête actuelle `2d8055a4…` | `78a680d5205d1df01d77ce415b4a2405864a2e72f1f3c55aafacf402e2dcda98` | (fichier avancé depuis ; ligne 557 égale) |
| `registres/go.md`, commit `e50ff62efe2b70a3db8525a8abf46c73110209e2` cité par l'additif | `ea02d0be4127136171eed347ea929f2e2c587c6c2fc1ecc17459e25f80ff968d` | oui |
| banc v3 (disque) | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` | oui |
| mandat du rédacteur | `c6dac15d53970ded2aac9331f65b20dfc56da79ec7248f8cd18c5873a56fbef0` | oui |
| additif 3, version 1 | `9e189f1af673e07460e96fe17537727f445ee3e415c53cb24429787e9a898915` | oui |
| rapport du rédacteur | `6e008e56bc88d29dab133c94cb00086b255c16a712b26329d4d475297097d4f2` | oui |

La ligne 7 de l'additif (sans son chevron) est égale à l'octet à la ligne 557 de `registres/go.md` aux deux commits (comparaison par programme, `calcul_contre_lecture_additif_3_v1.py`).

Lus en entier : le mandat du rédacteur, l'additif, le rapport, l'additif 1, l'additif 2, le devis ; le texte de l'en-tête à l'annexe A (les différentiels de fin non relus). Du banc v3 : en-tête, graines, `verifier_autorisation`, `generateurs`, `Contexte`, `indices_moities`, les lois, le rééchantillonnage, les poids du bras C, `regle_choisie`, `repetitions`, tout le monde de puissance (de `TAUX_MOYEN_PUISSANCE` à `puissance_qui_decide`), `CONFIGURATION_DECISIVE`, `executer_etage_1`, `commit_du_depot`, le manifeste, `main`.

## 1. Fidélité au GO

GO-2026-11-20-26 décide : la puissance de la règle de portée se mesure à nouveau à 200 avant tout étage payant ; l'étage 2 à 200 témoins, au plus 88,36 USD, échéance 2026-11-30 ; rien ne court avant l'additif contre-lu et scellé, la mesure sur processeur et son verdict scellé.

- L'additif ne fait que cela : une mesure, la même qu'à l'étage 1, au seul n = 200 (§ 1) ; ses graines ; sa règle de lecture ; l'héritage de l'étage 2 à 200 ; le plan du code ; les gardes. Il ne change aucune hypothèse, aucune prédiction du texte, aucun critère de lecture gelé, aucune table gelée, aucune racine existante. Il ajoute une prédiction pour sa propre mesure (règle R1), sans toucher P10.
- **Un seuil change pourtant, et la phrase du § 0 le nie** : l. 193 (« Seuil ») fixe le plafond d'arrêt à 25 USD ; le § 4.2 le lit à 88,36 USD. Ce changement est couvert par GO-2026-11-20-26 (le plafond est « le montant de la ligne de GO ») ; mais « aucun seuil […] aucun montant » est inexact. **Correction 1.**
- Ce qu'il ajoute hors du GO est rendu à Lazar ou à la mère (§ 7) : rien n'est tranché en silence. Une exception, de forme : le § 4.2 identifie la ligne du geste (7) à GO-2026-11-20-26, alors que le § 4.1 garde l'ordre des gestes (6) à (11) et que le devis, § 7, point 6, compte « la ligne de GO de la mère, au montant du plafond » parmi ce qui est scellé avant la dépense. **Correction 2.**

## 2. La mesure

- **Même monde** (l. 235 à 239) : deux juges sévères de même profil, a = 0,20 + d, b = 0,20 − d ; lois 1 et 3 ; bras R à ρ′ = 0 ; 0,5 ; 0,9 ; seul n change. Le partage du banc (`indices_moities`) donne, à n = 200, 50 bons et 50 mauvais en étalonnage et autant en lecture : c'est exactement la moitié « lecture » de l'étage 2 à 200 (100 témoins). Juste.
- **Mêmes comparaisons, même test** : quatre comparaisons, valeur de probabilité unilatérale par rééchantillonnage apparié (2 000 tirages), Holm sur quatre à 0,05, écart observé de 0,05 au moins (l. 179 ; `cellule_puissance`, `holm`, `p_valeur_unilaterale`). Juste.
- **« La plus basse »** : `puissance_qui_decide`, inchangée. Juste.
- **Mêmes cellules** : 210, ordre gelé (`enumerer_cellules_puissance`) ; recompté par mon calcul : 210 ; faisables à 0,10 : 13 (unanimité : ρ ≤ 0,45 sous la loi 1, ρ ≤ 0,15 sous la loi 3 ; juge seul : ρ ≤ 0,15 sous la loi 1, ρ = 0 sous la loi 3 ; bras R : ρ = 0, ρ′ = 0,5 et 0,9, sous les deux lois) ; à 0,05 : 31 ; à 0,15 : 5. Juste.
- **Répliques** : 2 000 par cellule, 2 000 tirages (l. 230, `CONFIGURATION_DECISIVE`). Juste.
- **« La faisabilité ne dépend pas de n »** : vrai. Dans le code, `resoudre_dissymetrie` et `loi_3_jouable` ne prennent pas n, et `cellule_puissance` décide de la faisabilité avant tout usage de n ; au texte, l. 238 ne fait entrer que des formules. Le d d'une cellule est donc le même qu'à l'étage 1.
- **Ce qui est rapporté sans décider** : les écarts de 0,05 et 0,15 ; la puissance par cellule et par comparaison ; l'écart observé moyen ; la règle choisie par le bras C et ses replis ; le compte entier de répliques gagnées. Rien d'autre n'est joué (§ 1, point 8). Juste.

## 3. La prédiction ajoutée (0,30 à 0,50, confiance 0,6)

**Écrite, refaisable seulement à l'ordre de grandeur, et calée sur un chiffre de l'étage 1, ce que le rédacteur dit.** Son calcul, refait à la lettre : écart type 0,05, écart vrai 0,10, soit z = 2 ; au premier pas de Holm (0,0125, z = 2,24) : 1 − Φ(0,24) ≈ 0,41 ; au seuil 0,05 (z = 1,645) : ≈ 0,64 ; à 25 par classe (écart type 0,07) : 0,21 et 0,42. Le « environ 0,2 » à 25 par classe est donc le premier pas de Holm. Pris tel quel, ce calcul rend 0,41 à 0,64, à cheval sur 0,5 ; la fourchette 0,30 à 0,50 vient du rapprochement avec le 0,160 donné à n = 100. Ce n'est pas une mesure vue par le rédacteur, mais un chiffre de l'étage 1 reçu par le mandat ; il le déclare (§ 1 et réserve 2). Le calcul omet le facteur qui pèse le plus : la règle que l'étalonnage fait choisir au bras C (ci-dessous).

**Mon calcul approché, écrit pour cette contre-lecture** (`calcul_contre_lecture_additif_3_v1.py`, sortie `calcul-contre-lecture-additif-3-v1.json`, empreintes au § 11). Aucun tirage aléatoire, aucune graine ; le banc n'est ni lancé ni importé ; les formules sont réécrites. Je n'ai pas simulé le monde, pour ne pas produire avant le scellement le chiffre que la mesure doit rendre. Deux parties :
1. **Loi exacte de la règle choisie par le bras C** sur la moitié d'étalonnage : énumération de tous les comptes multinomiaux des configurations d'erreurs dans chaque classe, avec la règle du texte réécrite (w = (S + λ I)⁻¹ d, λ = 0,1 × trace / 2, bornes 0,2 à 5 fois la moyenne, seuil au milieu, égalité à 1e-9 près, repli compté) ; masse couverte 1,000.
2. **Approximation normale** de l'écart apparié sur la moitié « lecture », loi exacte par témoin, pour chaque règle que C peut choisir ; deux bornes de Holm : basse = rejet à 0,0125 (suffisant), haute = rejet à 0,05 (nécessaire) ; écart observé de 0,05 au moins dans les deux.

| | cellule la plus basse | part des répliques où C choisit « au moins un » | puissance approchée, bornes |
|---|---|---|---|
| n = 100 | unanimité, ρ = 0 (lois 1 et 3) | 0,45 | 0,171 à 0,353 |
| n = 200 | unanimité, ρ = 0 (lois 1 et 3) | 0,61 | 0,377 à 0,594 |

À n = 100, le 0,160 donné tombe juste sous ma borne basse : à cette cellule, la comparaison à l'unanimité porte le plus souvent la plus petite valeur de probabilité du monde (écart vrai 0,10, contre 0,05 pour le juge seul et un écart négatif pour le bras R à ρ′ = 0), et c'est le premier pas de Holm qui joue. Lue de même, la valeur attendue à n = 200 est voisine de 0,37 à 0,38 : **sous 0,5 et dans la fourchette prédite**. Ce n'est pas une certitude : la borne haute dépasse 0,5. Je n'ai pas d'objection à la confiance de 0,6. Je ne demande pas que la prédiction change : la changer maintenant la calerait sur ce calcul.

Les autres cellules faisables sont plus hautes à n = 200 (juge seul : 0,75 et plus ; bras R : 0,73 et plus ; unanimité à ρ ≥ 0,15 : 0,43 et plus). La puissance est bornée d'abord par l'étalonnage : à ρ = 0 contre l'unanimité, d ≈ 0,083 est petit, et le bras C ne rend « au moins un » que si |w₁ − w₂| / (w₁ + w₂) < 2d ≈ 0,17 ; sinon il rend « juge seul » (39 % des répliques à n = 200, 54 % à n = 100).

## 4. Les graines

- 2026112031 (chronométrage, clés 2 et 12), 2026112032 (tirages, clé 2), 2026112033 (rééchantillonnage, clé 12) : distinctes des huit racines du texte (2026111930 à 2026111937). Juste.
- Dérivation par `SeedSequence(racine, spawn_key=(clé,))`, `.spawn(210)`, enfant de rang fixe dans l'ordre gelé (additif 1, choix 18). Juste.
- Refus des anciennes racines écrit trois fois : § 2 (« Le code de la mesure refuse toujours de dériver 2026111931 à 2026111937 »), § 5, point 3 (mode décisif de l'étage 1 retiré ou inatteignable, essai à l'appui), § 6 (garde « racines »). Racines neuves sous autorisation seulement, par chemin et empreinte ; racine des essais inchangée. Juste.
- Choisies avant tout code et toute mesure ; non changées quelle que soit l'issue (règle R3). Le manifeste porte racines, table des clés, dérivations (§ 6 : deux, de 210 enfants). Juste.
- Non vérifié : qu'aucune autre ligne du programme n'emploie déjà ces racines (une recherche large m'est interdite). Une telle collision n'aurait pas d'effet sur la validité : ce sont deux expériences distinctes.

## 5. La règle de lecture

- **Complète, sans trou ni recouvrement.** Toute issue sans faute du banc tombe dans A ou B : A exige que chaque comparaison ait une cellule faisable **et** 1 000 répliques gagnées sur 2 000 ou plus au plus petit compte ; B est tout le reste (plus petit compte de 999 ou moins, ou une comparaison sans cellule faisable). A et B sont disjointes. C prime : le § 6 la contrôle avant toute puissance (« un seul manque : invalide »).
- **Comptes entiers** : la puissance du banc est `gagne.mean()` sur 2 000 répliques ; 1 000 / 2 000 = 0,5 exactement en flottant ; « sous 0,5 strict » ⇔ 999 au plus. Cohérent avec l. 240 (« si elle est sous 0,5 ») et avec `p < PUISSANCE_EXIGEE`.
- **Cohérente avec l. 240 et l. 343** : l'issue B reprend la règle de l. 240 et la clause de l. 343 mot pour mot sur le fond (rangs 2 et 4 inatteignables, rang 3 gardé, ρ′ − ρ « positif » rapporté comme mesure, le reste non concluant ; votes effectifs et ρ′ − ρ lus selon leur table). La déclaration de B portée d'avance par l'additif scellé vaut « additif scellé » de l. 240, écrit avant la mesure : plus strict que le texte, pas moins.
- Un défaut, dans l'audit qui accompagne la lecture : il part « si l'issue contredit la prédiction », donc seulement quand l'issue est A. Une puissance basse et inattendue entre 0,160 et 0,30 ne le déclenche pas. **Correction 3** (règle R4).

## 6. La table d'héritage pour 200

**Recalculé, juste.**
- Appels : bloc P 4 ; bloc A 2 × 200 = 400 ; bloc B 200 (une lecture de plus par le premier juge) + 2 × 200 (deux par le second) = 600 ; **total 1 004**.
- Cas haut, sur les chiffres du devis (§ 1, § 3) : 0,20 + 2 × 9,86 + 2 × 12,43 = 44,78 USD ; au tarif exact (6,863 / 94 et 2,409 / 94 USD par appel) : 44,778 USD ; pire (facteur 6,863 / 3,478 = 1,973) : 88,359 USD. Égal à la ligne « 200 témoins » du devis (§ 6). Mon calcul rejoue aussi le devis à 100 témoins (22,49 ; 41 envois ; 18 témoins au pire ; 3 refus ; multiples 2,431 ; 1,626 ; 1,502 ; 1,086, soit les 2,43 ; 1,62 ; 1,50 ; 1,085 du devis à l'arrondi près) : la méthode tient.
- Justes aussi : le plafond du compteur lu au montant de GO-2026-11-20-26 ; la réserve et le coût d'un envoi refusé (0,60 USD) ; les « 100 premiers verdicts » lus comme le bloc A (200 verdicts) ; la moitié « lecture » de 100 ; le contrôle des traits de la lettre entre 100 bons et 80 mauvais ; ρ et ρ′ sur les 200 témoins ; la banque doublée à proportions égales (13 et 12 deviennent 25 et 25, remarque 5) ; « un juge sans aucune erreur sur les 200 témoins ».

**Ce qui manque, et que j'ai calculé** (pour le nœud 3 ; mon calcul, non versé, à refaire par un calcul versionné) :

| ce que la règle donne, à 200 témoins et 88,36 USD | valeur |
|---|---|
| cumul utile (plafond moins la réserve) | 87,76 USD |
| si tous les envois sont refusés : envois partis avant l'arrêt | 147 (88,20 USD comptés) |
| envois refusés que la base entière supporte, au cas haut | 71 (3 à 100 témoins) |
| au pire cas : envois partis ; témoins complets au bloc B | 996 sur 1 004 ; 197 sur 200 ; **moitié « lecture » complète** |
| multiples du tarif qui laissent complets : plomberie et bloc A ; plus B sur 40 témoins de lecture ; plus B sur les 100 ; tout | 4,41 ; 3,53 ; 2,71 ; 1,96 |

Conséquence : à 200 témoins sous 88,36 USD, **l'issue du pire cas change de nature**. À 100, le compteur la coupait à 18 témoins, verdict « non concluant par manque de témoins » (l. 384) ; à 200, il n'ôte les répétitions qu'aux trois derniers témoins de la moitié d'étalonnage, et la lecture est complète. L'issue écrite d'avance (condition (ii)) n'est donc plus celle du texte : c'est bien un manque, que l'additif nomme (nœud 3) sans le chiffrer.

**Ce qui changerait un critère gelé** : porter le seuil de 40 témoins complets à 80 (nœud 2) ; rien d'autre dans la table. Le plafond de 88,36 USD remplace un seuil du texte, mais par la ligne de GO (correction 1).

Un manque de cohérence : la ligne « l. 241, l. 305 (5) et (7) » (correction 2).

## 7. Les points laissés à Lazar et le point de procédure

**Nœud 1 — si l'issue est B, aucun « oui » n'est possible à l'étage 2 à 200.** Bien posé, et probable : mon calcul situe la puissance qui décide vers 0,38 (bornes 0,38 à 0,59). L'étage 2 garderait sa valeur de mesure : ρ, ρ′, ρ′ − ρ, votes effectifs, table par juge ; il peut encore rendre le « non » du rang 3, donc réfuter H-second-juge, pas la confirmer. *Recommandation* : que Lazar dise **avant la mesure** ce qu'il fera en B, pour que le départ ne dépende pas d'un choix fait après lecture ; je recommande « partir en B aussi », ce que l'additif écrit déjà (la taille reste 200 dans les deux issues), confiance 0,6. *Défaut sous 48 heures* : la lettre de l'additif, partir dans les deux issues.

**Nœud 2 — seuil de 40 témoins complets dans la moitié « lecture ».** L'additif a raison de le garder : c'est un critère gelé. Sous 88,36 USD, le compteur ne coupe pas la moitié « lecture », même au pire cas du devis ; le seuil ne joue qu'en cas de refus massifs (plus de 71 au cas haut) ou de panne. À 40 sur 100, une lecture coupée donne des intervalles plus larges, donc plus souvent « indéterminé » (rang 5), non un « non » de rang 3 : le sens est prudent. *Recommandation* : garder 40, confiance 0,7. *Défaut* : 40.

**Nœud 3 — plafond à 200 et chiffres des trois conditions.** Lire le plafond à 88,36 USD est juste (« montant de la ligne de GO ») ; les conditions (i) et (iii) valent telles quelles ; seuls leurs chiffres et l'issue (ii) manquent, et ils sont mécaniques (table du § 6). Lazar a donné son accord sur la ligne « 200 témoins » du devis v7 : c'est en substance le « devis neuf » de l. 241. *Options* : (a) un calcul versionné (version neuve du calcul du devis), qui rend ces chiffres et l'issue du pire cas, scellé avec l'additif de code de l'étage 2 et vérifié par la contre-lecture de ce code (les essais du compteur prennent 147 envois pour l'artefact « tout refusé ») ; aucun mot neuf de Lazar si aucun montant ne change. (b) Un devis à 200 complet, scellé, rendu à Lazar : plus lourd, rien à décider de plus. *Recommandation* : (a), confiance 0,75. *Défaut* : (a).

**Nœud 4 — « étage 2 seulement si l'étage 1 a dit oui » (l. 331, 378).** La lecture de l'additif est la bonne : l. 314 et l. 241 prévoient qu'un « non, pas à cette taille » renvoie à Lazar un devis à la taille voulue ; GO-2026-11-20-26 est sa réponse, et sa ligne nomme « étage 2 à 200 témoins : accord de calcul ». La clause de l. 331 et de l. 378 vise l'étage 2 à 100 sous GO-2026-11-19-66. *Recommandation* : garder la lecture de l'additif ; la mère l'inscrit au registre des décisions, avec la phrase de l'additif (« si ce n'est pas la lecture de Lazar, rien ne part »), confiance 0,8. *Défaut* : la lecture de l'additif.

**Point de procédure — second additif court pour le code et les racines, ou additif 3 seul.** Le second additif est la forme du texte (l. 7 : le commit et les empreintes sont portés par un additif de code scellé avant tout tirage) et celle de l'étage 1 (additif 2). GO-2026-11-20-26 ne l'exclut pas : il nomme l'additif de fond, celui-ci, comme condition, non comme seule pièce. L'autre voie laisse le code sans pièce scellée qui le nomme avant l'exécution, et la garde des racines ne contrôlerait qu'une empreinte d'additif qui ne dit rien du code. *Recommandation* : le second additif, court, qui ne fait que nommer le code (commit, empreinte de chaque fichier, commandes complétées) et autoriser les trois racines, écrit après la contre-lecture du code, scellé par la mère ; confiance 0,85. *Défaut* : le second additif.

## 8. L'écart déclaré (deux `git show --name-only`)

L'additif n'en est pas affecté sur le fond. Ce que ces gestes ont servi à trouver, le chemin de l'additif 2, est authentifié par son empreinte (`f5562d20…`, que j'ai recalculée égale sur main) : le contenu lu ne dépend pas du chemin par lequel on l'a trouvé. Sur l'aveugle : une liste de noms de fichiers ne porte aucune mesure ; le rédacteur dit n'avoir gardé que les lignes portant « additif ». Je n'ai pas refait ces gestes (ils me sont interdits) : je ne peux donc pas dire quels noms ont été affichés. Les seuls chiffres de l'étage 1 dans l'additif (0,160 ; « tolérance tenue à 200 et 400, pas à 100 » ; « non, pas à cette taille » ; « règle de portée déclenchée à 100 ») sont ceux des deux mandats. La cause est le mandat du rédacteur, qui ne donnait pas le chemin de l'additif 2 : à donner désormais dans tout mandat (le mien le donnait).

## 9. Corrections exigées

Ancres comptées dans l'additif (`9e189f1a…`) par `grep -c -F -e` : chacune rend 1.

**Correction 1** (§ 0, deuxième puce ; fidélité au GO : l. 193 est un seuil du texte).
- Ancien : `aucun seuil, aucun critère de lecture gelé, aucune table gelée, aucune racine existante, aucun montant.**`
- Nouveau : `aucun critère de lecture gelé, aucune table gelée, aucune racine existante ; aucun seuil ni aucun montant, hors de ce que GO-2026-11-20-26 décide : la taille du monde de puissance (n = 200, § 1) et le plafond d'arrêt de l'étage 2 à 200 témoins, lu au montant de cette ligne (88,36 USD au lieu de 25 USD, l. 193, § 4.2).**`

**Correction 2** (§ 4.2, ligne « l. 241, l. 305 (5) et (7) ; devis § 7, points 2 et 6 », colonne « lecture à 200 » ; contradiction avec le § 4.1, qui garde l'ordre des gestes (6) à (11)).
- Ancien : `la ligne est GO-2026-11-20-26, donnée sur la ligne « 200 témoins » du devis v7`
- Nouveau : `l'accord de Lazar est GO-2026-11-20-26, donné sur la ligne « 200 témoins » du devis v7 ; le geste (7) et le point 6 du devis, § 7, restent ceux du texte, à leur place dans l'ordre que le § 4.1 garde : la demande de départ payant vient après le geste (6) et après le verdict scellé de la mesure du § 1, et la ligne qu'elle demande porte le montant du plafond, 88,36 USD, avant l'échéance du 2026-11-30`

**Correction 3** (§ 6, « Audit de symétrie » ; règle R4 : le même audit dans les deux sens).
- Ancien : `ou si l'issue contredit la prédiction du § 1.`
- Nouveau : `ou si la puissance qui décide sort, d'un côté ou de l'autre, de l'intervalle prédit au § 1 (sous 0,30, ou 0,50 et plus).`

## 10. Remarques, non exigées

1. **Pour l'audit de symétrie** (« règle choisie par le bras C […] plausible, « au moins un » en population ») : à cette taille, une part nettement sous 1 n'est pas une faute du banc. Parts attendues de « au moins un » à n = 200, d'après la loi exacte de mon calcul : unanimité, ρ = 0 : 0,61 ; ρ = 0,15 : 0,63 ; ρ = 0,30 : 0,67 ; ρ = 0,45 : 0,74 ; juge seul, ρ = 0 : 0,94 ; ρ = 0,15 : 0,97 ; bras R, ρ′ = 0,5 : 0,98 ; ρ′ = 0,9 : 0,95 ; le reste est « juge seul », par moitiés égales. Si la mère veut que l'auditeur s'y réfère, le calcul doit être versé avec son empreinte (règle R6).
2. **La cellule la plus basse attendue existe deux fois** : à ρ = 0, la loi 3 est l'indépendance, comme la loi 1 ; le minimum de deux estimations d'une même puissance est biaisé vers le bas d'environ 0,006 (écart type 0,011). Sans effet sur la règle ; à dire au verdict si le minimum tombe là.
3. Issue A : « dans la cellule la plus basse » pourrait se dire « au plus petit des seize comptes (six pour l'unanimité, trois pour chacun des juges seuls, quatre pour le bras R) ». Équivalent ; plus net.
4. § 4.2, banque : « 25 et 25 dans chaque moitié » peut se lire « moitié d'étalonnage, moitié de lecture ». La remarque 5 lève le doute (13 et 12 deviennent 25 et 25 chez les simples et chez les bons à piège).
5. § 4.2, ligne « l. 194, l. 232, l. 236 » : l. 194 n'écrit pas n = 100 ; seules l. 232 et l. 236 l'écrivent.
6. Faute du banc (§ 6) : on pourrait ajouter les cellules faisables aux écarts de 0,05 et 0,15 (31 et 5), qui ne décident rien mais sont rapportées.
7. Issue A : « ses cinq rangs atteignables » veut dire « non fermés par l. 343 » ; le rang 2 reste rare (il demande que C ait choisi « au moins un »).
8. Prédiction : écrire la chaîne du calcul (écart type, z, pas de Holm, rapprochement avec 0,160) la rendrait refaisable à la lettre ; sans changer la fourchette ni la confiance.

## 11. Ce que j'ai fait, et mes écarts

- Commandes : empreinte du mandat par `sha256sum -c` ; `python3 --version` ; `mkdir` de mon dossier ; `git fetch origin main` ; `git show` redirigé vers mon dossier (texte, additif 1, additif 2, devis, `registres/go.md` sur main, et `registres/go.md` au commit `e50ff62e…` que l'additif cite, pour vérifier son empreinte : pièce hors de la liste du mandat, lue pour cette seule vérification) ; `git rev-parse origin/main` ; `sha256sum` sur des chemins nommés ; `wc -l` de ma sortie ; `date -u` ; `grep -c -F -e` pour les trois ancres ; deux programmes écrits dans des fichiers, lancés par `python3 FICHIER` (aucun code en ligne, aucun heredoc).
- **Écart déclaré** : deux recherches par l'outil de recherche du poste, chacune sur un seul fichier nommé, jamais sur un dossier : l'identifiant GO-2026-11-20-26 dans ma copie de `registres/go.md` ; les lignes de définition (`def` et constantes en capitales) du banc v3, pour en trouver les fonctions. La seconde est un motif de structure plutôt qu'un mot : je la déclare, au cas où elle compterait comme « motif large ».
- Aucune mesure de l'étage 1 ouverte ; banc ni lancé ni importé ; aucune graine du programme dérivée ; aucun tirage aléatoire ; aucun appel de modèle, aucune dépense ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` ; aucune écriture dans le dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.

Fichiers rendus (dossier `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-additif-3-ligne-3/`), chacun avec son compagnon `.sha256` :
- `contre-lecture-additif-3-portee-200-v1.md` (ce fichier) ;
- `calcul_contre_lecture_additif_3_v1.py` et sa sortie `calcul-contre-lecture-additif-3-v1.json` ;
- `resumer_calcul_v1.py` (affichage lisible de la sortie, rien de calculé).
Copies de travail tirées de main, sous `main/` : empreintes au tableau « Pièces vérifiées ».

Contre-lecteur, modèle O.

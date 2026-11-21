# Vérification du programme de vérification de la sortie des mondes, v2 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S (même vérificateur que pour la v1). Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copie du livrable : `livrable2/` ; mes sorties et programmes : `mes_essais/`.

## 0. Verdict : À corriger (corrections courtes, version v3 du programme)

Mes quatre corrections de la v1 sont portées, les motifs de clé sont alignés, la borne de 52 000 et le plafond de 40 tiennent. Mais trois choses sont à demander : (D1) le dépassement de quarante témoins doit devenir une faute, comme la mère le décide ; (D2) l'absence du décalage de la famille F dans T09 n'est **pas signalée** par la vérification, et la reconnaissance du décalage par le nom contredit « noms libres » ; (D3) le décalage de la loi des signaux du monde M n'est pas traité (§ 6). Le reste est conforme.

## 1. Empreintes et essais

Table `88c81aac…` égale à son compagnon et au recalcul ; programme `3de589d3…`, essais `3d3d71eb…`, rapport `7374460c…`, rapport de la sortie factice `eff5f142…`, différentiels et entrée factice : égaux à la table. **Essais rejoués sur ma copie : 290 passés** (comme annoncé). Rejeu du programme sur la sortie factice : rapport d'empreinte identique (`eff5f142…`), code 0, aucune observation. Je n'ai pas relu une à une les 102 mutations ; j'ai relu le mécanisme (inchangé), les comptes et les essais de parité.

## 2. Tes corrections et mes 39 sorties

Programme v2 lancé sur mes 39 sorties factices (`mes_essais/sorties-v2/`) et sur 22 variantes neuves (`mes_essais/variantes-v2/`) :

- **C1** : une sortie dont un objet libre est imbriqué sur 995 niveaux est lue (code 0) ; sur 100 000 niveaux : code 3, « exception imprévue », aucun rapport, aucune trace. Conforme.
- **C2** : `mode` nul, vide ou absent, vérité absente, vérité sans `expression` : famille écartée, sortie lisible (mes 03e à 03h). Une `valeur_vraie` nulle : illisible (`P1_TYPE_INVALIDE`) ; `valeurs_de_plus` sur T01 : illisible. Conforme.
- **C3** : budget 0,05, 5, « 5 % », « 5% », « 20 % » acceptés (les quatre dernières avec une observation `O_BUDGET_HORS_FORME_FRACTION`) ; 0,07, « 7 % », 0, 100, nul, `true` : illisible. Conforme.
- **N2** : mon faux nom à traits d'union insécables est pris (point 5 manqué, code 1). Conforme.
- Mes 39 sorties : toutes comme attendu. Changements par rapport à la v1, voulus : 03f et 03h lisibles avec F écartée, 05d prise, 06k portant aussi `P2_IDENTIFIANT_IMPOSE_RESERVE`, plus d'observation sur le nombre de témoins (33 au plus). Aucune fuite dans les 39 rapports, ni dans les comptes rendus de correspondance (chemins et codes seulement ; ni nom de famille à l'écart, ni texte de la sortie).

## 3. Motifs de clé alignés sur le lanceur v9 (`1b47c1cf…`, l. 534)

Lanceur relu (sept branches) et programme (`MOTIFS_DE_CLE`, l. 234 à 247). Branche par branche, le programme prend au moins autant :

| branche du lanceur | motif du programme | au moins aussi large |
|---|---|---|
| `s[k]-ant-` suivi d'un alphanumérique | `prefixe_sk_segment` (segment de 1 à 32 alphanumériques, tiret, un alphanumérique) | oui |
| `s[k]-` + 20 alphanumériques | `prefixe_sk` (16 ou plus, avec `_` et `-`) | oui |
| `g[h]p_` + 20 | `g[h][pousr]_` + 20 | oui |
| `h[f]_` + 20 | `prefixe_hf` | égal |
| `A[K]IA` + 12 majuscules ou chiffres | `A[K]IA` ou `A[S]IA` + 12 ou plus | oui |
| `A[I]za` + 20 | `A[I]za` + 20 ou plus | égal |
| `Bearer` + blancs + 16 | `bearer` sans casse, `=` admis | oui |

Les frontières de mot sont retirées (le lanceur n'en a pas). **L'essai de parité est juste** : il vérifie l'empreinte du lanceur, extrait `MOTIF_VALEUR_DE_CLE` du texte du lanceur, vérifie qu'il a sept branches, fabrique pour chacune la chaîne minimale, contrôle que le lanceur la prend, puis que le programme la prend par un motif à préfixe. Il n'éprouve que la chaîne minimale ; les classes de caractères du programme étant des sur-ensembles de celles du lanceur (je l'ai vérifié à la main, ci-dessus), c'est suffisant. Recherche des préfixes en clair dans le programme, les essais et le rapport : aucun (une seule occurrence fortuite, « risk-free-a » dans le rapport, qui contient « sk-free-a » comme mot anglais). Aucun nom de modèle ni de fournisseur dans le livrable (hors le nom de mon propre dossier de travail dans des chemins). Limite : le préfixe à segment prend tout mot anglais composé de ce type (code 1, jamais illisible), connu et dit.

## 4. Erratum 1 : taille et plafond de témoins ; avis sur le mot de la mère

- `TAILLE_MAX_CARACTERES = 52000` : 52 000 caractères lisibles, 52 001 illisible (essais du développeur) ; mon essai à 41 000 caractères de remarques seules refusé. Conforme à l'erratum v3 et v4.
- `TEMOINS_MAX = 40`, témoins de tête et du bloc à l'écart comptés ensemble : conforme. Mon essai à 40 : aucune observation ; à 41 : `O_TEMOINS_AU_DELA_DU_PLAFOND`, sortie lisible, code 0.
- **Mot de la mère de 10:40Z (plus de 40 témoins = illisible) : je le confirme.** La lettre dit « quarante témoins au plus », le texte servi dit quoi réduire d'abord, un second essai existe, et le programme ne tronque rien. Le développeur avait raison de ne pas trancher seul : le § 6 du mandat ne range pas ce plafond dans ses points 1 à 5. Mais le devis (§ 3) ne rend un second essai possible que pour une sortie « illisible » aux points 1 et 2 : il faut donc ranger la faute au **point 1 (forme)**, avec un code propre (`P1_TEMOINS_AU_DELA_DU_PLAFOND`), et le dire dans l'erratum, côté session. Correction **D1** : passer l'observation en faute du point 1, avec son artefact (41 témoins), sa mutation, et mon essai à 40 qui reste lisible. Le compte reste celui de la tête et du bloc à l'écart ensemble. Même chose que pour la taille : un seul nombre, à un seul endroit.

## 5. Réserve des identifiants T01 à T17 (point 2)

`P2_IDENTIFIANT_IMPOSE_RESERVE` : tout témoin du bloc à l'écart portant un identifiant de T01 à T17, et tout second porteur en tête. **Juste dans son effet, plus strict que la lettre dans sa forme.** La lettre donne ces identifiants aux témoins imposés sans les réserver ; mais le programme de vérité lit T05 et T07 par leur identifiant (« sans gain ») : un témoin libre nommé T05 serait lu à tort. Coût : la sortie est illisible, donc un second essai payé, pour un nom. Acceptable, avec un mot dans l'erratum côté session ; je ne demande pas de changement.

## 6. Correspondance vers l'entrée du recalcul (`--vers-recalcul`)

Lu : le programme de correspondance (l. 1262 à 1575), le programme de vérité pour son seul format d'entrée (en-tête, clés de témoin, règles de lecture du recalcul, issues) et l'exemple d'entrée. Je n'ai pas lu la table de vérité ni le rapport du développeur de la vérité. J'ai fait calculer au programme de vérité l'entrée tirée d'une de mes sorties factices : 27 témoins calculés, 2 refusés par `loi_hors_moteur` (ma famille F emploie une loi « couple » que le moteur n'a pas) ; je n'ai lu que les statuts et les codes, jamais une valeur.

**Format** : conforme à l'exemple (clés obligatoires, `lois`, `suite`, `tailles_de_plus`, nombres réécrits avec leur texte brut). Le programme de vérité accepte les 39 témoins de l'entrée factice du développeur, et les entrées tirées de mes sorties (hors la loi « couple », refusée en aval, avec un code : pas de repli silencieux).

**Les trous de la lettre, jugés :**

| choix | jugement |
|---|---|
| **Tranche** (CH1) : première tranche dont `n_calibration` contient le n du témoin, sinon la première ; voisine = la suivante, circulaire (CH1B) | **Juste mais fragile.** Aucun champ « tranche » n'existe, donc le choix est forcé. Il marche pour la famille A (même loi dans les trois tranches) et pour la famille D si les tailles diffèrent ; si les trois tranches de D portent les mêmes tailles, la première est prise sans signal. Le sens circulaire de « voisine » est une lecture, non la lettre. **Mot de la mère souhaitable** sur « voisine » ; pas de contradiction de la lettre. |
| **« L'honnête qui échoue »** (CH2) : la composante du mélange dont le poids égale exactement `p_echec` | **Juste.** Comparaison en rationnels exacts ; ambiguïté (deux poids égaux, pas de mélange) : non converti, code nommé. Ne contredit pas la lettre (C et I sont des mélanges dont le poids de la composante d'échec est P(échec), § 3.2). |
| **Signal du monde M** (CH3, CH4, CH10) : `somme` non converti ; populations dans l'ordre du § 3.3 ; honnête = mélange (1 − P(échec), P(échec)) | **Juste pour l'ordre, le mélange et le refus de `somme`. Un trou reste : γ** (voir D3). |
| **Dérive de F** dans `valeurs_de_plus` de T09 (CH7) | **Ambigu, à corriger (D2).** |
| **Aire 0,80 pour la puissance** (CH6) ; T05 et T07 à trois aires ; T07 à `tailles_de_plus: [400]` (CH9) | **Juste.** Sens du § 3.1 et de la note ; signe de l'écart de puissance : règle du programme de vérité = puissance de la règle moins celle de la base, positif quand la règle gagne, cohérent avec la règle de l'erratum. |
| **Décalages en écarts types** (CH5) : `decalages[i]` appliqués comme `delta_en_ecarts_types` à la loi honnête de la tranche | **Juste d'après la grammaire** (`delta_en_ecarts_types`), mais **si un auteur donne ses décalages dans l'unité de sa loi**, le programme se trompe sans le dire (loi dont l'écart type n'est pas 1). Accepté par la mère à titre provisoire ; je suggère une observation quand la loi du saboteur dit un autre delta. Pas de contradiction. |
| **Grappes de T10 et T11** (CH8, CH8B) : 3 × 100 et 30 × 10, lecture sur la normale réduite | **Juste** : tailles données par la lettre (§ 3.1), variance 1 par la lettre (§ 3.2, H). Pour un témoin libre de H : les tailles de l'auteur. |

**D2, l'absence du décalage dans T09, sa signalisation, et « noms libres ».** Décision de la mère : F est écartée si la lecture échoue, la sortie ne devient pas illisible ; les noms restent libres ; le programme signale l'absence ; la session lit le décalage et l'écrit dans son journal. État de la v2 :
- **Illisible : non** (bon). `derive-aucune` : lisible, code 0.
- **Signalée à la vérification : non.** Le rapport de vérification ne dit rien de T09, ni de F. Seul `--vers-recalcul` marque chaque témoin de F `NC_DERIVE_SANS_CHAMP`, sans dire que F est à écarter, et sans compte rendu de la valeur lue.
- **Noms libres : non respecté.** `derive_de_la_famille_f` ne reconnaît que la seule clé numérique dont le nom contient « decalage » ou « derive ». Deux clés de ce type (« decalage_a », « derive_b ») : rien n'est lu. Un nom comme « delta » : rien n'est lu.
- **Corrections D2.** (a) En vérification, un écart de F : `ecartes: [{"monde": "F", "raisons": ["E_DERIVE_SANS_DECALAGE_LISIBLE"]}]`, sortie lisible, avec artefact et mutation. (b) Une règle de reconnaissance qui ne dépend pas d'un mot du nom : je propose d'écarter les clés dont le nom dit « couverture », « taux » ou « probabilité », puis, si une seule clé reste, de la lire ; si plusieurs restent, de retenir celle dont le nom dit « decalage » ou « derive » si elle est unique ; sinon F est écartée. (c) Dans le compte rendu de correspondance, dire que F est à écarter quand le décalage est illisible, et rendre la valeur lue (c'est une valeur de l'auteur, non vraie) ainsi que le rang de la clé retenue, pour le journal de la session. (d) Option plus forte : contrôler que le décalage lu triple bien le taux de 1 % sous la loi de F, et le rapporter.

**D3, le monde M et γ.** Le § 3.3 donne deux réglages (γ = 0 et γ > 0) et un témoin exigé « au réglage γ = 0 » ; la forme ne porte aucun champ γ sur un témoin. La correspondance convertit un témoin sur `valeur` ou `intention` avec la loi écrite, sans γ : le témoin au réglage γ = 0 est lu comme s'il était au γ proposé. Le mot de la mère (« le signal de M n'est pas converti, et c'est rapporté ») ne dit pas la même chose que le programme : celui-ci convertit `valeur` et `intention` quand leurs lois sont de la grammaire, et ne rapporte que `somme`. **Il faut un mot de la mère** : soit ne convertir aucun témoin du monde M (code `NC_MONDE_M_SANS_GAMMA`, rapporté), soit le convertir et rapporter un choix `CH_GAMMA_NON_PRIS_EN_COMPTE`. Ma recommandation : la première, tant que la lettre ne donne pas le moyen de dire γ.

**Confidentialité de la correspondance.** Le compte rendu ne porte que des chemins, des identifiants de témoins imposés et des codes ; un témoin du bloc à l'écart n'y est désigné que par son chemin. Rien n'est calculé par le programme ; l'entrée ne porte que des lois recopiées, des règles et la valeur annoncée par l'auteur.

## 7. Résumé des corrections demandées (programme v3)

- **D1** : plus de 40 témoins (tête et bloc à l'écart ensemble) = faute du point 1, `P1_TEMOINS_AU_DELA_DU_PLAFOND`, avec essais et mutation.
- **D2** : signaler en vérification l'absence ou l'ambiguïté du décalage de F dans T09 (F écartée, sortie lisible) ; reconnaître le décalage sans dépendre d'un mot du nom ; rendre la valeur lue et le rang de la clé au compte rendu.
- **D3** : trancher γ pour les témoins du monde M (mot de la mère).
- Sans correction : réserve des identifiants (§ 5) ; « voisine » circulaire et unité des décalages : mots de la mère souhaités (§ 6).

## 8. Réserves

1. Mes sorties sont des remplissages ; la correspondance n'a été éprouvée que sur des lois factices. 2. Je n'ai pas lu les valeurs vraies, ni la table, ni le rapport du développeur de la vérité. 3. Les fichiers du programme de vérité calculés sur mes sorties factices sont dans `mes_essais/` (non lus).

vérificateur du programme de vérification de la sortie des mondes, modèle S

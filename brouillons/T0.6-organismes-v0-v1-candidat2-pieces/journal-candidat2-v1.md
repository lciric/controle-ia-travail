# Journal du candidat 2 de T0.6 — 2026-11-07T09:21:19Z (`date -u`)

- candidat 1 : `brouillons/T0.6-organismes-v0-v1-candidat1.md`, `4c27a254ef6ec255d3abf43a4fd6c9a0b6ffd0d24e9513ae28b0a3af6b91d8b3` (empreinte vérifiée avant tout)
- contre-lecture du lanceur v3 : `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v3/contre-lecture-lanceur-T0.6-v3.md`, `b338a81203eba681bd09a08413e3a5690b3cd7987cb0ad937ec9b291ad0d9068` ; corrections de code v4 : `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v3/corrections-code-lanceur-T0.6-v4.md`, `652590280f03cfc4f3a6a700b8dbf4eabe90efc265a32cbc5b5ab330efc9841b`
- couples : `couples-candidat1-vers-candidat2-T0.6-v1.json` (copie à l'octet dans ce dossier, comparée à `docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v3/couples-candidat1-vers-candidat2-T0.6-v1.json`), `2880c1a66017030580c2d64ad2cb77e7a2b9549ca05699e0913332f6e2036928`, 12 couples, appliqués dans l'ordre
- substitutions : `substitutions-candidat2-v1.json`, `6613b29d99cd2a5ddaa9361c48b08ddd65029f4ec64d66d63647dd253446473b`, 46 substitutions, appliquées après les couples
- script : `appliquer-candidat2-v1.py`, `0e41f75ed05615ff86617500065d7aaaac89e29154e3d40331abc3cbde693205`

Valeurs connaissables remplies, avec leur source :

- entropie `31538212097275005629337336542801867913` : `numpy.random.SeedSequence().entropy` (numpy 2.5.3), tirée une fois à 09:21:19 UTC, aucune donnée lue (R9)
- `donnees/20261007-082440-t05-extraction/taches-evaluation.json` : `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` (sceau `donnees/20261007-082440-t05-extraction/taches-evaluation.json.sha256` présent ; égale à la configuration `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json` de l'arbre du code)
- `donnees/20261007-082440-t05-extraction/taches-entrainement.json` : `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd` (sceau `donnees/20261007-082440-t05-extraction/taches-entrainement.json.sha256` présent ; égale à la configuration `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json` de l'arbre du code)
- `prereg/P3-consignes-v1.md` : `a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c` (sceau `prereg/P3-consignes-v1.md.sha256` présent ; égale à la configuration `docs/notes/g0-deux-semaines-v1/config-t06-reel-v1-brouillon4.json` de l'arbre du code)
- rapport du développeur v1 `72ac6016552ef6969aa53f036111cdaaa0ea5bf5e71912c5fe09a56a448bc719` (arbre du code : `/home/user/wt/t06-lanceur-v2`)
- rapport du développeur v2 `48f3a74a1635fb68fd5f0468133067706d7bc60347192c3004b8acd33d750b4e` (arbre du code : `/home/user/wt/t06-lanceur-v2`)
- rapport du développeur v3 `c8c318bbb18e2acedf08fca38ad13978eaf1d02221fb464e68eec77692079eb6` (arbre du code : `/home/user/wt/t06-lanceur-v2`)
- rapport du développeur v4 `028187c30419e4b94c494f006162b845fcc6a2e0e7cd11e7d2fac7e3b0544254` (arbre du code : `/home/user/wt/t06-lanceur-v2`)

| couple ou substitution | ligne (au moment de l'application) | occurrences | longueur ancien | longueur nouveau |
|---|---|---|---|---|
| couple 1 | 157 | 1 | 71 | 70 |
| couple 2 | 158 | 1 | 55 | 54 |
| couple 3 | 159 | 1 | 62 | 61 |
| couple 4 | 160 | 1 | 66 | 65 |
| couple 5 | 161 | 1 | 69 | 68 |
| couple 6 | 162 | 1 | 54 | 53 |
| couple 7 | 119 | 1 | 26 | 89 |
| couple 8 | 711 | 1 | 111 | 138 |
| couple 9 | 726 | 1 | 333 | 879 |
| couple 10 | 140 | 1 | 85 | 509 |
| couple 11 | 543 | 1 | 90 | 210 |
| couple 12 | 595 | 1 | 51 | 139 |
| D01 | 1 | 1 | 24 | 24 |
| D02 | 3 | 1 | 139 | 1945 |
| D03 | 139 | 1 | 217 | 3347 |
| D04 | 166 | 6 | 37 | 73 |
| D05 | 172 | 1 | 195 | 183 |
| D06 | 173 | 1 | 168 | 208 |
| D07 | 174 | 1 | 181 | 247 |
| D08 | 175 | 1 | 145 | 328 |
| D09 | 175 | 1 | 108 | 191 |
| D10 | 103 | 1 | 119 | 133 |
| D11 | 134 | 1 | 37 | 65 |
| D12 | 367 | 1 | 187 | 134 |
| D13 | 413 | 1 | 206 | 152 |
| D14 | 498 | 1 | 287 | 234 |
| D15 | 578 | 1 | 84 | 89 |
| D16 | 626 | 1 | 56 | 80 |
| D17 | 658 | 1 | 121 | 214 |
| D18 | 729 | 1 | 95 | 129 |
| D19 | 750 | 1 | 151 | 198 |
| D19b | 761 | 1 | 48 | 72 |
| D20 | 630 | 1 | 139 | 139 |
| D21 | 180 | 1 | 73 | 77 |
| D22 | 182 | 1 | 75 | 75 |
| D23 | 607 | 1 | 64 | 64 |
| D24 | 625 | 1 | 281 | 380 |
| D25 | 627 | 1 | 56 | 60 |
| D26 | 629 | 1 | 105 | 105 |
| D27 | 629 | 1 | 119 | 133 |
| D28 | 629 | 1 | 156 | 156 |
| D29 | 629 | 1 | 142 | 156 |
| D30 | 650 | 1 | 77 | 77 |
| D31 | 752 | 1 | 284 | 338 |
| D32 | 760 | 1 | 66 | 66 |
| D33 | 761 | 1 | 79 | 79 |
| D34 | 763 | 1 | 55 | 55 |
| D40 | 184 | 1 | 33 | 55 |
| D41 | 626 | 1 | 51 | 98 |
| D42 | 754 | 1 | 156 | 230 |
| D43 | 181 | 1 | 58 | 305 |
| D45 | 753 | 1 | 121 | 425 |
| D44 | 623 | 1 | 35 | 282 |
| D46 | 193 | 1 | 54 | 280 |
| D47 | 195 | 1 | 65 | 104 |
| D48 | 196 | 1 | 68 | 268 |
| D49 | 197 | 1 | 53 | 228 |
| D50 | 745 | 1 | 213 | 269 |

Marqueurs du candidat 2 (`<<[A-Z0-9_]+>>`), 9 distincts (occurrences) :

- `COMMIT_CODE_T06` : 4
- `EMPREINTES_CODE_T06` : 6
- `EMPREINTE_AMORCE_T06` : 4
- `EMPREINTE_PREREG_P3BIS` : 2
- `EMPREINTE_PREREG_T07` : 3
- `LONGUEURS_TEXTES_P3` : 2
- `SCRIPT_PUISSANCE_V3` : 4
- `TESTS_ATTENDUS_T06` : 4
- `VALEURS_CITEES_T06` : 5

Marqueurs remplis par rapport au candidat 1 : `MOT_LAZAR_DT` (mots de Lazar du 6 novembre, R-1623 et R-1624), `ENTROPIE_T06`, `EMPREINTE_RAPPORT_LANCEUR_T06`.
Marqueurs restants et pourquoi : `COMMIT_CODE_T06`, `EMPREINTES_CODE_T06`, `EMPREINTE_AMORCE_T06` (commit du code de la course, après fusion et contre-lecture) ;
`EMPREINTE_PREREG_T07`, `EMPREINTE_PREREG_P3BIS` (aucun préenregistrement scellé de T0.7 « coût » ni de P3-bis sous `prereg/` au 6 novembre) ;
`LONGUEURS_TEXTES_P3`, `SCRIPT_PUISSANCE_V3` (pas de sortie des longueurs IA/IT/IM ni de script de puissance v3 dans le dépôt) ; `TESTS_ATTENDUS_T06` (rempli par E3) ;
`VALEURS_CITEES_T06` : deux valeurs restent (empreinte canonique de la configuration réelle scellée, chemin de la configuration copiée sous `prereg/`).

Clés lues par la chaîne (lignes qui portent « clé : » suivi d'un accent grave ; « Tests attendus » exactement 1, les autres au plus 1) :

- « Entropie : ` » : 1
- « Commit du code d'analyse : ` » : 1
- « Configuration de T0.6 (empreinte canonique) : ` » : 1
- « Tâches d'évaluation de T0.6 : ` » : 1
- « Tests attendus : ` » : 1
- « Chemin de la configuration de T0.6 : ` » : 1
- « Chemin des tâches d'évaluation de T0.6 : ` » : 1
- « Chemin des tâches de distillation de T0.6 : ` » : 1
- « Chemin des consignes de P3 : ` » : 1

- forme de citation de l'amorce « `scripts/amorce_instance_t06_v4.sh` (` » : 1

- mentions restantes de `lancer_t06_v3` ou `amorce_instance_t06_v3` (1, historiques : statut antérieur, point 8 du candidat 1, traitement) :
  - ligne 124 :      - **substitutions** : (i) le code à lancer est le **lanceur v3** (`scripts/lancer_t06_v3.sh`, `

- résultat : `brouillons/T0.6-organismes-v0-v1-candidat2.md`, `72dd336336d3ad0be279ed499d214b868569d0466dfb740f50af08f8830e11eb`, 764 lignes

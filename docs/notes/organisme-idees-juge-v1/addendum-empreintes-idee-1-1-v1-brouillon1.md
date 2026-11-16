# Addendum d'empreintes au préenregistrement de l'idée 1.1 (poids du nul) — v1, brouillon 1

- Texte auquel il s'ajoute : `prereg/organisme-idee-1-1-poids-du-nul-v2.md`
  (`3ffe1739aa83ea8de613d07855db52d16c82ad6247fca22e833ee7f6ff8305ff`), ci-dessous **[T]**, lignes citées « l. n ». [T] l. 9 à 11 :
  « ses empreintes entrent dans un **addendum d'empreintes** scellé avant tout jeu, qui ne change rien d'autre ».
- Rédacteur : rédacteur neuf, modèle A, sous-agent de la session mère. Je n'ai écrit ni [T], ni ses brouillons, ni leurs
  contre-lectures, ni la preuve, ni le code des versions 1 à 5, ni ses rapports, ni ses contrôles, ni l'étape 0.
  Date (UTC, `date -u`) : 2026-11-16, de 13:47 à 13:53 (scellement du brouillon). Dépôt lu sur `main`, tête `df131fbd0bf15020c4d8d275a1a2cb48e80c126a`.
  **Aucun jeu ; aucun résultat du jeu n'existe.**
- Pièces (empreintes recalculées, égales à leurs compagnons) :
  - fichier d'étape 0 v5, scellé, **[E0]** : `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/etape0-v1/etape0-idee-1-1-v5.json`
    (`540dfa68392dc6213b367c5cb645ae0362dd7fe2f29eb5761e2a46554462ceeb`), joué de 12:45:54Z à 13:46:14Z au commit `a46d8028`,
    copie propre, deux processus (R-2986) ; son journal **[J0]** : `…/etape0-v1/journal-etape0-idee-1-1-v5.txt`
    (`c9c8014c5b428b370d1fe10b508f3d80d7615c914eb1413bf996aa02f81bb374`) ;
  - contrôle du différentiel v3 → v4 **[C4]** : `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v4/controle-differentiel-code-idee-1-1-v4.md`
    (`9ba07614ea7bc08141c7671c649a1586103edef0e20cec867f23fcdc9b9c4861`), § 9 ;
  - contrôles du différentiel v4 → v5 : fidélité **[CF]** `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/controle-differentiel-code-idee-1-1-v5-fidelite-v1.md`
    (`b09ae513467f96368ca41c287b70aab338533bf87ba4d66c2e7798b36d0898f6`) ; conformité au texte **[CC]**
    `…/code-idee-1-1-v5/controle-differentiel-code-idee-1-1-v5-conformite-v1.md`
    (`63c6421b20e04369a49dcd535342d37415c19831a6a694eb7df1f58b3261a594`), § 1 et § 5 ;
  - rapport du code v5 **[RD5]** `…/code-idee-1-1-v5/rapport-code-idee-1-1-v5.md`
    (`6ce11448a382ab16d588a128d92c89c50631fa752d4b3b19b3bf685f03f834f7`), empreinte seulement ;
  - registre : R-2942, R-2976, R-2978, R-2979, R-2984, R-2986 de `registres/decisions.md` ; GO-2026-11-16-01 de `registres/go.md`.
- Ce que cet addendum **ne change pas** : aucune hypothèse, prédiction, métrique, seuil, bras, graine, étape, critère de
  lecture ni ligne de la liste d'arrêt de [T]. Il gèle le code par empreinte, inscrit le programme du jeu (chronométrage,
  nombre de processus, réductions) et les comptes que [T] veut à l'addendum, et déclare les écarts.

## 1. Fichiers gelés (46) — le lanceur refuse de partir si l'un d'eux diffère

Lignes au format de `sha256sum`, chemins relatifs à la racine du dépôt, produites par programme par
`.venv/bin/python -I -B scripts/etape0_idee_1_1_v5.py --lister-empreintes` à la tête `df131fbd` et recopiées telles quelles
(aucune autre ligne de ce format dans cette pièce). Elles sont égales, fichier pour fichier, à la clé `fichiers_geles` de
[E0] (46 sur 46, comparaison par programme) : le code gelé n'a pas bougé depuis l'étape 0 (commit `a46d8028`).

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  src/controle_ia/__init__.py
c29258ab0069320bbba33d3cdf8b652ba1ce254298b348e2c68ac03e83e6414e  src/controle_ia/organisme_idees_juge/__init__.py
853595cb44260eaaf16bf003f7a7b8155a3785e08c424573fcdaf40a6d1c487e  src/controle_ia/organisme_idees_juge/juge_v1.py
bf7e1f3e6cdbbebed681cf115e6d7e8031e670ffb14d82910d707a09f5b0e1fb  src/controle_ia/organisme_idees_juge/lois_v1.py
d6da7373efca00b538407794bcd832f3f84970412e6200e49715d23455731747  src/controle_ia/organisme_idees_juge/execution_v1.py
9cb63ff12d6198b3acd0ec979e798fe41268b2a50a8d90600614fd01284d65b9  src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py
34b6d356be3d717c7f0ab44711d4e1ee38926d6db6be4cd2a3a9684514db4350  src/controle_ia/organisme_idees_juge/oracle_v1.py
a1a08ef78c87ba8ffaa4147d53854dd4c17e6a70ec5b265cb406a858a49d1086  src/controle_ia/organisme_idees_juge/rejeu_v1.py
bab7b6453cc11b8618b70fd6be55ddaf362fffe3cafe7e79a1f4eddeaf1d225e  src/controle_ia/organisme_idees_juge/vue_v9_v2.py
f36cb5b20a9fd75452bbf51494ac7f11beca2bc9bca42f84c774b8f49f8c954a  src/controle_ia/organisme_idees_juge/nul_limite_v1.py
d32aead32404ba5f589f9ccfa6ab8deb4393038f4b4922b6c8eb2cca3a48bb4b  src/controle_ia/organisme_idees_juge/morceaux_par_coupe_v1.py
1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54  src/controle_ia/organisme_idees_juge/projection_commun_v1.py
54e5fbb241751a5e375dd810cafbd784ccc35d8d6b5859cb90f2700fd4172afa  src/controle_ia/organisme_idees_juge/projection_methodes_v1.py
a68aabf266a46de3766cedd8fde6dde723306441fddb2892d36e9b48309f34f8  src/controle_ia/organisme_idees_juge/attaque_projection_extrait_v1.py
b7ac9c80fc1c333572b74d16e105a2e8523c1c02b2d9775b63dc9c33d19ea9e1  src/controle_ia/organisme_idees_juge/projection_bras_v1.py
c3d77494885b8f51ea0a6858490242cbb9a993f4cbb8b6bc14511717673e27ea  src/controle_ia/organisme_idees_juge/banc_idee_1_1_v2.py
1ce2d5f9ac5d3034ecc3da49b184dd5a166a2b42a6070ae88662715f60ce91df  src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v4.py
c5a5fed8f3d5ce4f12a17d9f6dde1d73714614b27ac8f80703d32372e63ef39d  src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v4.py
54d6a7dd7ae3b25dde2fdeab7e0e48420e1f4147a36f4084691f3646dfc309d4  src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v5.py
8542a484bacf37e496f059cea6f5a83db28ed8ecfe8746c1d347560348a763a6  src/controle_ia/organisme_idees_juge/execution_idee_1_1_v5.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439  src/controle_ia/gardes.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2  src/controle_ia/scellement.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d  src/controle_ia/manifeste.py
3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306  src/controle_ia/prereg.py
c116a4bf943dc5e2f34f157080fc5ab7b3942e37033ad82ace7606066d27f0c8  scripts/jouer_idee_1_1_v5.py
398b922af1d2c57e2ec2bfb3ffe167bd6c704665c3d441562aba80ff3f082b05  scripts/lire_idee_1_1_v5.py
ffa5255195efa82278f842b9d6f0ffb2383ec36389921bec14101a0c807186d9  scripts/etape0_idee_1_1_v5.py
a1bbfcc935007934dda9b038fb9f187f7627816fd18514b5aabc77715aaedca5  tests/conftest.py
6e53851ec4794d00f30d275a6a04f10aef72489c65cd6bce40085879b597631a  tests/test_organisme_idees_juge_idee_1_1_projection_v4.py
09d40fbb21ed859fe3b232ee33975709a91edd4b50892fc01ce10e407ec05df1  tests/test_organisme_idees_juge_idee_1_1_gardes_v5.py
2fc13778709c86c710be22e8160ece0b374c28196c446e9d028f40fd765ace89  tests/test_organisme_idees_juge_idee_1_1_banc_v5.py
fd7aaa916f2728091c3f5671406136ae7d100ab21f852c98200b73d10d9b87fe  tests/test_organisme_idees_juge_idee_1_1_lecture_v4.py
ae6ef7134ab994a78508a03c2f29f0baa02c6dabd7f93eb6318ea14049f63070  tests/test_organisme_idees_juge_idee_1_1_execution_v5.py
4245f8d4c8e271df6d45cd8e0d7a1179039471760c91a7b9d85272eca890e1bc  tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v5.py
ff2db3d68c012d2d1c0c6641a910a3b16ad2342f2228c7ee6163191833aeadb3  src/controle_ia/organisme_idees_juge/vue_v9_v1.py
d77952222616099d73e1499832f76a80932e82325904525f2ab4875f1b5fc548  src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v4.py
b62f7e04d0060c7a057bf4e7ea762bd6f2c8c96de3639b8821eb8d558ff309b6  src/controle_ia/organisme_idees_juge/execution_idee_1_1_v4.py
a16e02ffe864a36cf4b0915e49abfa2069eaafc1abc176d0277f2aed2a0e27fc  scripts/jouer_idee_1_1_v4.py
83d15084bfa4d388909a94c8af2c1e98c2a6f807ae3639a67b6cf6b5e991af62  scripts/lire_idee_1_1_v4.py
39fd1414cd7c48df98aab800669d89f7964d8fb9a764636be3ca5916458c4f6b  scripts/etape0_idee_1_1_v4.py
a6e0a5ffd7256725af4fb4f0a72f4d02d06e38548b5f22f5c33acb3312de69de  tests/test_organisme_idees_juge_idee_1_1_banc_v4.py
f82a4f4d7c80774a48cb01930138b4dd14526bd57ad52528441cf30a5a0dd25e  tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v4.py
f5eeb0241acb571c377c524377e988d9cc8b0f287550f53489b936a4426d846d  tests/test_organisme_idees_juge_idee_1_1_execution_v4.py
7843a02dd8ebf6d566921799315511672f86412b4424d91aada8d52cc26d187a  tests/test_organisme_idees_juge_idee_1_1_gardes_v4.py
61008bafa5b51cd98feb991be10f489541e4e48206df8d9e52167c08f5356ac1  docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/couples-v4-vers-v5.json
af450e5cf8b27d18c1d21cd58700256e0877acda8cd58c6639521e62540b9e41  tests/test_organisme_idees_juge_idee_1_1_differentiel_v5.py
```

Lecture par le lanceur (`execution_idee_1_1_v5.lire_addendum`, appelé par `scripts/jouer_idee_1_1_v5.py`) : pièce
vérifiée contre son compagnon `.sha256` ; chaque ligne ci-dessus recalculée sur le disque (`execution_v1.verifier_addendum`) ;
liste égale, fichier pour fichier, à celle de [E0] ; sinon « pas de jeu » ([T] l. 613).

**Copies tierces** (juge `94bfd92`, nul v9 `a41b7b5` et ses compléments) : elles ne sont pas dans la liste ci-dessus ; elles
sont vérifiées par les constantes d'empreintes des modules gelés `juge_v1.py` et `vue_v9_v2.py` (`verifier_copie`,
`verifier_copie_v9`, appelés par le lanceur avant le jeu). Pour mémoire, les empreintes relevées par l'étape 0 (clé
`copies` de [E0], recopiées par programme) :

| fichier de la copie | empreinte |
|---|---|
| `94bfd92:orchestrator/pole/__init__.py` | `f7341b965ddba1e0fb21b44d9068f59650d5c77e3175f2b6b7ca879219fa5c9b` |
| `94bfd92:orchestrator/pole/a_blanc_v59.py` | `606aa8b4fcc38786b38cf2954da46533eed9384232a56100d22ff30b8ce0826c` |
| `94bfd92:orchestrator/pole/caviardage.py` | `78abfd4731218e20538418608ebebaca3364206ef6d014b7a34829a3c9fd7e85` |
| `94bfd92:orchestrator/pole/controles_pari.py` | `fabc3d0873e6db639f2578eb00ef0035d7831a3b2a1457ffce1d91aa7a364e1c` |
| `94bfd92:orchestrator/pole/cycle.py` | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |
| `94bfd92:orchestrator/pole/fiche.py` | `ec018f147196222268d91358ce2038bb35bf76069e6bf8928dea9e3db59d1074` |
| `94bfd92:orchestrator/pole/memoire.py` | `71f1d08613bf335aa9ef7aa1397f20aa24553fea2f1b858c10b265d62f8ab79e` |
| `94bfd92:orchestrator/pole/nul_filles_v2.py` | `0ed9b4adbcddc4ad77a1c97d5cbd5706f14926e9c47fe96ce2bab3221a138910` |
| `94bfd92:orchestrator/pole/nul_v8.py` | `cc452aafd17121a7c0ec42829eea47063ffee1f6cdf7f642e264d528f976b888` |
| `94bfd92:orchestrator/pole/outils.py` | `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` |
| `94bfd92:orchestrator/pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| `PROVENANCE-complement-v1.md` | `032eaeeb7d48358bdb1ef8502a40ba52b2ea1a4cce2a4eef12c822ff54f6f724` |
| `PROVENANCE-complement-v2.md` | `c38ba64386f05a32d077d5de65289a58704b349a063062ca91f7c7b9ab28d036` |
| `PROVENANCE-complement-v3.md` | `a4a62a888adf273779ffe198cab9b958692106ea1208efc4aaf79bf02c63cfac` |
| `PROVENANCE.md` | `9093d232a0b84a46308c1937f9d979bf163ea5831ccee7ad359e7bd775b7e004` |
| `orchestrator/demonstrations/banc_tricheurs_v7.py` | `ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12` |
| `orchestrator/demonstrations/banc_tricheurs_v8.py` | `0be47e4b5916a98499faf9c40d65369b41e3a5463d7ab444ed18ba18bba08c03` |
| `orchestrator/demonstrations/banc_tricheurs_v9.py` | `7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44` |
| `orchestrator/essais/mutations_nul_v9.py` | `f004dba63ffe25c66b9b41edefbd8307e188feccd8a8e15aa9754e472dca3f52` |
| `orchestrator/essais/test_nul_v9.py` | `d42a50eb4ba9691e75e82fa4bc714a925615da80df22227fee730392015999b9` |
| `orchestrator/pole/attaque_goodhart_v2.py` | `3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703` |
| `orchestrator/pole/nul_v9.py` | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |
| `src/controle_ia/organisme_idees_juge/morceaux_par_coupe_v1.py` | `d32aead32404ba5f589f9ccfa6ab8deb4393038f4b4922b6c8eb2cca3a48bb4b` |
| `src/controle_ia/organisme_idees_juge/nul_limite_v1.py` | `f36cb5b20a9fd75452bbf51494ac7f11beca2bc9bca42f84c774b8f49f8c954a` |

**Différentiels joints** ([T] l. 387 et 538 : « différentiel joint à l'addendum ») — fichiers du dossier
`docs/notes/organisme-idees-juge-v1/code-idee-1-1-v1/`, égaux à leurs compagnons, et cibles inchangées depuis (empreintes de
la liste ci-dessus égales à celles du rapport du code v1) :

| différentiel | source → cible | empreinte |
|---|---|---|
| `differentiel-nul-limite-v1.diff` | `copie-nul-v9-a41b7b5/orchestrator/pole/nul_v9.py` → `nul_limite_v1.py` (les quatre changements de [T] l. 383 à 386) | `1334b735460257edff63b01e01a4e144acf243681bea75e63e9645ac9221ab6e` |
| `differentiel-morceaux-par-coupe-v1.diff` | `nul_v9.py:detail_morceaux_groupe` → `morceaux_par_coupe_v1.py:detail_morceaux_par_coupe` (J9-Dc, [T] l. 439 à 441) | `4944e35dac74d509b0bd5aecc7d209deaaba409cef9e64d4fe1bb5b759dc2519` |
| `differentiel-projection-scindee-v1.diff` | `essai_projection_methodes_v1.py:_blocs_projection` → `projection_bras_v1.py:projeter+valeurs_e` ([T] l. 400 à 405, 538) | `de82c82e3a2492b5c76807d422273449c85e5c9844027754485fae7e14098e4e` |

`projection_commun_v1.py` (`em_commun`) porte l'empreinte `1f4ada97…` de l'essai `essai_projection_commun_v1.py` que [T]
l. 401 cite : copie octet pour octet, sans différentiel à joindre. `projection_methodes_v1.py` (`54e5fbb2…`, ligne de la liste)
porte les extraits de `essai_projection_methodes_v1.py` (`29704896…`, [T] l. 404) recopiés corps pour corps par analyse
syntaxique (`IT_PROJ` = 300, `IT_MV` = 300, `IT_CHAUD` = 150, `_blocs_projection`, `m3_toutes_coupures`, témoins), seule la
ligne d'import de `cm` changeant ; égalité éprouvée par essai (rapport du code v1, l. 44).

## 2. Programme du jeu — bloc lu par le lanceur

Recopié à l'octet de la fin de [J0], entre ses deux marqueurs (extraction par programme) :

<!-- programme-du-jeu-idee-1-1 -->
```json
{
 "processus": 2,
 "reductions": [],
 "duree_attendue_h": 15.667,
 "etape0": {
  "chemin": "docs/notes/organisme-idees-juge-v1/code-idee-1-1-v5/etape0-v1/etape0-idee-1-1-v5.json",
  "sha256": "540dfa68392dc6213b367c5cb645ae0362dd7fe2f29eb5761e2a46554462ceeb"
 },
 "declarations": {
  "m9_graines_des_essais": "les essais prolongent les clés du texte : E0 (98, r, 0) et (98, r, 1) ; essais, mutations, chronométrage (97, k, …, 0) et (97, k, …, 1) (deux flux par répétition) ; k listés dans `cles_97` du fichier d'étape 0",
  "m10_empreintes_EP": {
   "essai_projection_commun_v1.py": "1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54",
   "essai_projection_methodes_v1.py": "29704896ec641feff607d42c2636c456e372a2a9f4deb589efd4b8256c8b4105",
   "essai_projection_cas_v1.py": "539f6a6cfce71eaab9010fa9cd16a2607a0bf9faf9499286bcb6fb7f25bda837"
  },
  "m11": "le lanceur rejoue les essais, les dix-sept mutations et E0, E9, EP, ED ; il ne rejoue pas les comptes de H7 et de Hn (critère de mort, cas sain, Hn sous gel) : ils valent pour le code gelé par l'égalité, fichier par fichier, des empreintes du fichier d'étape 0 et de l'addendum (M2)",
  "comptes_non_ecrits_par_le_texte": {
   "E9": "2 répétitions de chacune des 29 lignes jugeables (toutes sauf H7)",
   "ED": "2 répétitions de chacune des 29 lignes jugeables",
   "EP": "50 mondes de `essai_projection_cas_v1.construire`, cas T01 à T12 en cycle",
   "mutation_certificat": "30 répétitions de Q8, de Q1 et de Q2 ; tuée par au moins une promotion de J9-P ; cas sain : aucune promotion sur les copies Q1, Q2 (Q8 rapporté)",
   "mutation_w_reste": "détecteur : carte log-linéaire de S1 (puissance 2, inclinaison [0,5 ; −0,5 ; 0]), 3 répétitions, log W maximal de J9-P ≤ 10⁻⁶ exigé du code juste",
   "Hn_sous_gel": "bloque à 3 promotions ou plus sur 200, terme sur toutes les familles ou famille linéaire seule"
  },
  "lectures_de_la_lecture_gelee": {
   "strates_de_rho": "tableau STRATES_TEXTE (J9-P : V2 à V5 sur, V1 hors ; La : V5 sur, V1 à V4 hors ; Ld : V2, V4, V5 sur, V1 et V3 hors), pour les trois primaires seulement",
   "regle_des_strates (n2)": "une strate est lue si elle compte au moins une ligne informative ; un rééchantillon sans ligne informative dans la strate est écarté et compté ; quantiles de Bonferroni des primaires",
   "decomposition_du_prix (n4)": "intervalle percentile bilatéral à 95 % (niveau non écrit au texte) ; rééchantillons à moins de 2 lignes informatives écartés et comptés",
   "mcnemar (n3)": "exact bilatéral, sur les 15 lignes V, paires J8 contre J9; J9-P contre J9; La contre J9; Ld contre J9; La-P contre La; J9-P contre La; J9-D contre J9; J9-D40 contre J9; J9-P contre J9+; La contre J9+; Ld contre J9+; J9-D contre J9+; J9-D40 contre J9+",
   "rho_plus_primaires (n5)": "ρ⁺ de J9-P, La et Ld rapporté (quantiles de Bonferroni) ; le verdict principal reste lu sur le seul ρ⁺ de J9-P, calculé à part et inchangé",
   "m6": "secondaire réduit : I recalculé sur ses seules premières répétitions"
  },
  "complement_copie_v9": {
   "chemin": "docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/attaque_goodhart_v2.py",
   "sha256": "3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703",
   "provenance": "docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/PROVENANCE-complement-v3.md",
   "provenance_sha256": "a4a62a888adf273779ffe198cab9b958692106ea1208efc4aaf79bf02c63cfac",
   "remarque": "le texte scellé ne citait, comme compléments de la copie a41b7b5, que les bancs v7, v8 et v9 ; l'essai d'origine TricheursParMorceaux.test_monde_w2_de_l_attaque_membre_du_nul_v9 importe aussi pole.attaque_goodhart_v2 (import paresseux, l. 406 de essais/test_nul_v9.py), du même commit, versé par la mère (R-2976) et vérifié par empreinte"
  }
 }
}
```
<!-- fin-programme-du-jeu-idee-1-1 -->

Ce que dit le bloc, en clair : **deux processus** ; **aucune réduction** ; **durée attendue D = 15,667 heures**, sous la
limite de 32 heures ([T] l. 642) ; fichier d'étape 0 et son empreinte. Le lanceur **rejoue** la règle de réduction
(`etape0_idee_1_1_v5.regle_de_reduction`) sur le chronométrage de [E0] au nombre de processus du bloc : une réduction
différente rend le run invalide ([T] l. 626). Les clés `declarations` reprennent les lectures du texte faites par le code
(m9, m10, m11, comptes que le texte n'écrit pas, lectures de la lecture gelée) et le complément de la copie (D5, § 4.4).

## 3. Ce que l'étape 0 inscrit à l'addendum ([T] l. 494, 500 à 532, 640 à 646, 664 à 700)

Tous les chiffres de cette section viennent de [E0] (`540dfa68…`), clé `resultat`, lus par programme.

**Issue** : `jeu_permis` vrai, `bloquants` vide.

**Préalable 1** ([T] l. 664 à 700) : (a) les 16 noms empruntés présents ; (b) E9 passé ; (c) route première : **37 essais
d'origine du v9 rejoués, 37 passés**, depuis une vue assemblée hors du dépôt de **58 fichiers** (empreinte de la liste
`96107ec270de981f0270f268430718acc25dbc82ab5a09fe3e60a39697b7222a`) ; **liste des essais déclarés non rejouables : vide** ;
**liste des essais réécrits : vide** ([T] l. 687 à 692 : rien à lister ni de différentiel à lire). Préalable 2 : preuve v3
`a481c873a317a710923ee6134f410f45b5dd14392738b768ecad0fdffb3547c1` et sa vérification
`b2f92646eea8a80051c798685c2ae00f013008acda26e6f214d115b0cb2705b9`. L'étape 0 v4 (`c6c34fd0…`, R-2976), qui bloquait sur le
préalable 1 (c), est gardée telle quelle ; la v5 la remplace pour ce préalable, sur un code dont seuls la vue et les noms
changent ([CF], [CC] § 2).

**Essais d'égalité** ([T] l. 534 à 540) : E0, 100 répétitions, écart maximal 0 nat ; E9, 58 évaluations (2 répétitions des
29 lignes jugeables), aucun écart ; EP, 50 mondes, écart maximal 0 nat sur les log e de bloc et sur le processus minimum ;
ED, 58 répétitions, écart maximal 2,87·10⁻⁷ nat (limite 2·10⁻³). Tous passés. Le lanceur les rejoue avant le jeu.

**Banc de mutations** ([T] l. 502 à 509) : 17 mutations, toutes tuées pour la raison attendue ; tous les cas sains passés.

**Garde P4 — comptes à inscrire** ([T] l. 509 à 523), 200 répétitions chacune :

| ligne | sans garde, famille linéaire | sans garde, toutes familles (terme projeté) | sous gel, linéaire | sous gel, toutes familles | critère écrit | issue |
|---|---|---|---|---|---|---|
| H7 | 86 | 58 | 0 | 0 | mutation tuée si ≥ 20 sans garde ; cas sain si ≤ 2 sous gel | mutation tuée ; cas sain passé |
| Hn | 19 | 9 | 0 | 0 | bloque si ≥ 3 sous gel ; sans garde rapporté, non bloquant | ne bloque pas |

**Égaux, chiffre pour chiffre, à ceux de l'étape 0 v4** (R-2976 : H7 86 et 58, 0 sous gel ; Hn 19 et 9, 0 sous gel), comme
l'exige [CC] § 4 : le code de la garde n'a pas changé et les comptes sont déterministes. Aucune graine rejouée après un
échec de la garde (il n'y en a pas eu).

**Clés `(97, k)` des essais** ([T] l. 493 et 494 : « un k distinct par essai, liste dans l'addendum »), clé `cles_97` de [E0] :

| essai | k |
|---|---|
| E9 | 30 |
| ED | 31 |
| EP | 32 |
| chronometrage | 40 |
| garde_H7 | 20 |
| garde_Hn | 21 |
| lecture_synthetique | 12 |
| mutation_avant_gel | 10 |
| mutation_blocs | 3 |
| mutation_certificat | 1 |
| mutation_coupures | 8 |
| mutation_garde_acces | 2 |
| mutation_gel | 5 |
| mutation_lineaire | 7 |
| mutation_minimum | 4 |
| mutation_t40 | 11 |
| mutation_tirages | 9 |
| mutation_w_reste | 6 |

**Chronométrage** ([T] l. 527 à 531, 640 à 643) : 20 répétitions de chacune des 30 lignes, graines `(97, 40, i_ligne, r)`,
r < 20. Secondes par répétition, par groupe de bras tel que le code les mesure (« base » : J8, J9, La, Ld, strate et tout le
temps mural non attribué, dont le gel par bloc ; « jumeau » : J9-D40, J9-D, J9-Dc ; « J9-P » et « La-P » : projections et
valeurs e) :

| ligne | base | jumeau | J9-P | La-P | total |
|---|---|---|---|---|---|
| H7 | 1,343 | 0,000 | 0,000 | 0,000 | 1,343 |
| Hg | 1,753 | 1,666 | 0,000 | 0,000 | 3,419 |
| Hm | 1,722 | 1,690 | 0,000 | 0,000 | 3,412 |
| Hn | 1,838 | 1,919 | 0,000 | 0,000 | 3,757 |
| Hs | 1,689 | 1,657 | 0,000 | 0,000 | 3,345 |
| Q1 | 0,681 | 2,650 | 0,484 | 0,088 | 3,903 |
| Q2 | 0,658 | 2,835 | 0,499 | 0,091 | 4,083 |
| Q3 | 0,619 | 2,712 | 0,455 | 0,089 | 3,875 |
| Q4 | 0,593 | 2,611 | 0,451 | 0,093 | 3,747 |
| Q5 | 0,597 | 2,525 | 0,451 | 0,083 | 3,655 |
| Q6 | 0,603 | 2,742 | 0,457 | 0,079 | 3,881 |
| Q7 | 0,569 | 2,526 | 0,447 | 0,090 | 3,631 |
| Q8 | 0,751 | 2,634 | 0,487 | 0,090 | 3,962 |
| Q9a | 0,623 | 3,161 | 0,477 | 0,098 | 4,359 |
| Q9b | 0,685 | 3,102 | 0,534 | 0,107 | 4,428 |
| V1(0.25) | 0,560 | 2,736 | 0,460 | 0,087 | 3,843 |
| V1(0.5) | 0,548 | 2,649 | 0,437 | 0,086 | 3,720 |
| V1(0.75) | 0,588 | 2,841 | 0,462 | 0,084 | 3,975 |
| V2(0.4) | 0,571 | 2,468 | 0,414 | 0,078 | 3,532 |
| V2(0.8) | 0,466 | 2,435 | 0,405 | 0,076 | 3,383 |
| V2(1.2) | 0,512 | 2,421 | 0,419 | 0,073 | 3,425 |
| V3(0.4) | 0,612 | 3,005 | 0,433 | 0,085 | 4,134 |
| V3(0.8) | 0,574 | 2,821 | 0,465 | 0,087 | 3,947 |
| V3(1.2) | 0,626 | 3,092 | 0,457 | 0,090 | 4,264 |
| V4(0.1) | 0,622 | 2,975 | 0,473 | 0,099 | 4,168 |
| V4(0.2) | 0,631 | 2,982 | 0,477 | 0,099 | 4,189 |
| V4(0.3) | 0,624 | 2,943 | 0,484 | 0,096 | 4,147 |
| V5(0.4) | 0,583 | 2,804 | 0,439 | 0,090 | 3,916 |
| V5(0.8) | 0,625 | 2,670 | 0,465 | 0,089 | 3,849 |
| V5(1.2) | 0,523 | 2,480 | 0,429 | 0,080 | 3,512 |

Somme sur les 30 lignes : **112,806 s par répétition** ; sans réduction, chaque groupe compte 1 000 répétitions :
D = 112,806 × 1 000 / 2 / 3 600 = **15,667 heures** à deux processus (recalculé par moi, égal au bloc). À trois processus
ce serait 10,445 heures (étape 0 v4 : 10,07 heures). Aucune réduction n'est appliquée ; la règle des réductions 1 à 5
([T] l. 645 à 657) reste sans objet.

## 4. Écarts au texte scellé et déclarations

### 4.1 E2 et E3 — acceptés

- **E2** : le jeu appelle les fonctions internes du juge et du v9 au lieu de `nul_filles_v2.evaluer_v2` et `nul_v9.evaluer_v9`
  que [T] nomme (l. 239, 332 à 335), pour obtenir des grandeurs que ces fonctions ne rendent pas (R-2942).
- **E3** : [T] l. 438 et 439 dit de J9-Dc « Sans coût de plus : les bornes par coupe sont déjà calculées » ; c'est faux : le
  code fait un second appel au solveur ; J9-Dc est descriptif, aucun critère n'en dépend (R-2942).
- **Acceptation** : GO-2026-11-16-01, point (3), mot direct de Lazar inscrit le 2026-11-16T00:29:21Z, verbatim : « go recos
  sur les 6 décisions, on a dit go recos pendant l'autonomie » ; lecture inscrite au registre, verbatim : « (3) **idée 1.1** :
  écarts de lettre E2 et E3 au texte scellé `3ffe1739…` acceptés, à inscrire dans un addendum scellé avant le jeu (R-2942) ».
  Ils sont inscrits ici. Ni E2 ni E3 n'est touché par la v5 ([CC] § 3). Cette acceptation **ne couvre pas D5**.

### 4.2 D1 à D4 — points du contrôle v4, déclarés sans nouveau tour

Repris de [C4] § 9 ; la lecture gelée (`lecture_idee_1_1_v4.py`, ligne de la liste du § 1) est inchangée en v5, mêmes lignes.
Aucun ne porte un verdict ; aucun ne peut naître d'un enregistrement du banc gelé (tranches scellées, empreintes dans
l'index scellé).

- **D1** — `lecture_idee_1_1_v4.py`, l. 785 et 786 : garde explicite « sans engagement jumeau ou sans La-P », redondante avec la
  garde des bornes (l. 776 à 779), qui arrête toujours avant elle ; éprouvée à part ([C4] § 3).
- **D2** — même fichier, l. 754, 766 et 772 : trois chemins où `verifier_format` lève une trace, et non une `GardeArret`, quand
  la valeur d'un champ n'est ni un dictionnaire ni une chaîne, ou quand `strate_sans_log` n'est pas un dictionnaire ; le
  défaut ferme du côté de l'arrêt (code de sortie non nul, rien n'est écrit), seul le message manque.
- **D3** — même fonction : la forme des réductions n'est comparée ni entre les lignes ni au champ `reductions` de l'index ;
  trois formes hors de la règle seraient acceptées et le secondaire lu sur le compte le plus court, sans message. Le banc
  retire ces groupes ensemble et de la même façon sur toutes les lignes ; **sans objet pour ce jeu, qui n'a aucune
  réduction** (§ 2).
- **D4** — `_types`, l. 708 à 720 : la valeur NaN est refusée dans les valeurs lues (la v3 la lisait) ; l'infini reste
  accepté ; changement voulu, sans effet sur des données saines.
- Pour mémoire, hors du différentiel ([C4] § 9) : le banc ne contrôle pas la finitude des log de richesse de l'engagement
  jumeau aux 40 instants, ni de J9⁺, ni des valeurs par membre de J9-D, alors que [T] l. 620 dit « un log W non fini : arrêt
  du run entier » ; aucune valeur non finie vue sur 137 répétitions ; signalé, non classé.

### 4.3 Deux processus au lieu de trois

[T] l. 541 et 542 : « trois processus au plus sur quatre cœurs » ; l. 641 et 642 : « p ≤ 3 est le nombre de processus inscrit
à l'addendum ». Le jeu tourne à **deux processus** : le jeu de l'idée 1.2 tourne sur la même machine à quatre cœurs
(R-2976, R-2979), et un cœur reste aux travaux de la session. Ce n'est pas un écart (p ≤ 3) ; c'est le nombre inscrit. L'étape 0 a
tourné à deux processus (R-2979) et D est calculé à p = 2. Le lanceur lit ce nombre au bloc programme,
refuse plus de trois, et refuse une reprise à un autre nombre ou à d'autres réductions (`jouer_idee_1_1_v5.py`).

### 4.4 D5 — le quatrième fichier de la copie du v9 : écart de lettre

- **Ce que dit [T]** : comme compléments de la copie `a41b7b5`, il ne cite que les bancs v9, v8 et v7 (l. 38 à 43) ; la vue
  du préalable 1 (c) est « faite du paquet `pole` de `94bfd92`, de `pole/nul_v9.py`, de `demonstrations/` et de `essais/` »
  (l. 673 à 675).
- **Ce que fait le code v5** : la vue contient en plus `docs/notes/organisme-idees-juge-v1/copie-nul-v9-a41b7b5/orchestrator/pole/attaque_goodhart_v2.py`
  (`3c9de8b83b6fcf198d12cacf6a6738c2fc3fe4ade9391f943b3924592959e703`), recopié octet pour octet du même commit public
  `a41b7b5`, provenance `…/copie-nul-v9-a41b7b5/PROVENANCE-complement-v3.md`
  (`a4a62a888adf273779ffe198cab9b958692106ea1208efc4aaf79bf02c63cfac`), versé par la mère (R-2976), vérifié par empreinte et
  compagnon avant la vue (`vue_v9_v2.verifier_copie_v9`).
- **Pourquoi** : l'essai d'origine `TricheursParMorceaux.test_monde_w2_de_l_attaque_membre_du_nul_v9` l'importe
  (import paresseux, l. 406 de `essais/test_nul_v9.py`) ; sans lui, l'étape 0 v4 bloquait (36 sur 37, R-2976). Le texte ferme
  les deux autres sorties : déclarer l'essai « non rejouable » (l'erreur d'import n'est pas l'une des deux raisons écrites,
  l. 692 à 696) ou le réécrire (« Aucune réécriture ne remplace un essai d'origine rejouable », l. 699).
- **Effet** : aucun critère, seuil, graine, réduction, règle de lecture ni ligne d'arrêt touché ; même essai d'origine
  (`d42a50eb…`), mêmes 37 essais, même règle « tous passent » ; le module n'entre pas dans le chemin du jeu ([CC] § 1.2,
  [CF] § 2 et 3). Reste un **écart de lettre** aux l. 38 à 43 et 673 à 675, nommé D5 ([CC] § 1.2).
- **Statut** : décision de la mère (R-2984) : D5 est un écart à un texte scellé, même de lettre ; le jeu attend le mot de
  Lazar. GO-2026-11-16-01 ne le couvre pas.
- **Mot de Lazar** : ACCORD-D5-A-REMPLIR

## 5. Exécution du jeu

- **Commande**, depuis une copie propre (arbre propre exigé par le lanceur) du commit qui porte cet addendum scellé et
  son compagnon, à la racine de cette copie :
  `.venv/bin/python -I -B scripts/jouer_idee_1_1_v5.py --addendum prereg/organisme-idee-1-1-poids-du-nul-v2-addendum-empreintes-v1.md`
  — chemin de la version scellée proposée ; si la mère la nomme autrement, l'argument de `--addendum` change, rien d'autre.
  Le lanceur pose lui-même `nice -n 10` et le nombre de processus du bloc (deux) ; il installe la garde réseau.
- **Ordre du lanceur** : préenregistrement scellé égal à `3ffe1739…` ; arbre propre ; aucune sortie ni manifeste antérieur de ce
  jeu (noms v1 à v5) ; addendum lu (§ 1 et § 2) ; copies du juge et du v9 vérifiées ; noms empruntés ; essais rejoués ;
  17 mutations rejouées ; essais d'égalité E0, E9, EP, ED rejoués ; manifeste du run ; `depart.json` scellé ; jeu de
  30 lignes × 1 000 répétitions en 600 tranches de 50, chaque tranche scellée ; `sortie.json` scellé. **Aucune lecture.**
- **Durée** : D = 15,667 heures attendues pour le jeu (contrôles avant jeu en plus) ; **borne dure de 48 heures murales**
  ([T] l. 627 et 659), comptée par le code depuis le **premier** départ (`depart.json`), reprise comprise ; au-delà : arrêt,
  run invalide, aucune lecture.
- **Consigne : garder une tâche active pendant tout le jeu.** La session qui lance garde une tâche en cours (une attente
  qui se termine seule à la fin du processus parent, ou un suivi), du départ au scellement de `sortie.json` : sans tâche
  active, le conteneur peut être repris, et le jeu meurt avec lui (la première étape 0 de 06:17Z a été tuée ainsi, R-2976).
  Le PID du processus parent est noté au lancement.
- **Ce qui l'arrête** (toujours par `GardeArret`, avec `arret.json` scellé quand le jeu a commencé ; run invalide ; relance
  seulement sous un texte ou un addendum neuf, [T] l. 620) : un fichier gelé ou une copie différent ; une pièce sans bloc
  programme, un fichier d'étape 0 différent, à bloquants ou d'un autre code ; des réductions différentes de la règle
  rejouée ; plus de trois processus ; un essai qui échoue ; une mutation qui survit ou un cas sain manqué ; un essai
  d'égalité manqué ; une garde d'évaluation (issue fraîche hors de l'ordre, garde P4 contournée, engagement avec `fractions`,
  certificat invalide, monotonie, nichage, domination, log W non fini, exception) ; un appel réseau ; la mort d'un
  processus fils ; la durée murale au-delà de 48 heures ; le signal TERM envoyé au parent (le lanceur le change en
  `GardeArret`).
- **Reprise** (code, non écrite dans [T]) : un run interrompu **sans** `arret.json` (machine arrêtée, conteneur repris sans
  signal reçu) se reprend sous le même identifiant par
  `.venv/bin/python -I -B scripts/jouer_idee_1_1_v5.py --addendum <même chemin> --reprendre <RUN_ID>` : tranches déjà écrites
  vérifiées par leur compagnon et sautées, mêmes processus et réductions exigés, borne de 48 heures inchangée. Un
  `arret.json` présent interdit la reprise.
- **Réserve d'opérateur, reprise de l'addendum de l'idée 1.2 (§ 4), non éprouvée sur ce code** : le même montage de
  processus (`multiprocessing`, `Pool`, attente de 5 s) y laissait le parent bloqué, sans `arret.json`, si un fils mourait
  en attendant une tâche. Si les processus du run n'emploient plus le processeur alors que `sortie.json` n'est pas écrit,
  envoyer le signal TERM **au parent, par son PID** (`kill -TERM <PID>`, jamais par motif, R10) : run invalide, `arret.json`
  écrit.
- Après le jeu : sortie sous `diag/organisme-idees-juge-v1/` (recopiée à l'octet depuis la copie et vérifiée par ses
  compagnons) scellée avant toute lecture ; lecture gelée par `scripts/lire_idee_1_1_v5.py`, qui relit cet addendum ; lecteur
  neuf (R13) et audit de symétrie (R4) écrit avant le prononcé ([T] l. 543 à 546).

## 6. Ordre avant le jeu

1. Contre-lecture de cette pièce (§ 7) ; version scellée sous un nom neuf ; versée et commitée.
2. Mot de Lazar sur D5 inscrit au § 4.4 (à la place de `ACCORD-D5-A-REMPLIR`), avant le scellement de la version qui fera foi.
3. Copie propre du commit qui porte la version scellée ; jeu par la commande du § 5, une tâche active jusqu'au scellement
   de la sortie.

## 7. Contre-lecture

*(à remplir)*

## 8. Déclaration d'exclusion

- Rôle : rédacteur neuf du brouillon 1 de l'addendum d'empreintes de l'idée 1.1. Modèle : lettre A.
- Heures (UTC, `date -u`) : 2026-11-16, de 13:47 à 13:53 (scellement du brouillon).
- Pièces lues (empreintes recalculées) : [T] `3ffe1739…` (l. 1 à 25, 330 à 336, 370 à 421, 434 à 441, 488 à 547, 600 à 711,
  mentions de « addendum », d'`evaluer_v2`, d'`evaluer_v9`, de J9-Dc et des bancs) ; [E0] `540dfa68…` ; [J0] `c9c8014c…` ;
  `execution_idee_1_1_v5.py` `8542a484…` ; `scripts/jouer_idee_1_1_v5.py` `c116a4bf…` ; `scripts/etape0_idee_1_1_v5.py`
  `ffa52551…` ; `etape0_idee_1_1_v5.py` (fonctions `chronometrer`, `duree_attendue_h`, `regle_de_reduction`) ;
  `banc_idee_1_1_v2.py` (l. 590 à 650 et relevé des clés de temps) ; `execution_v1.py` (`verifier_addendum`,
  `installer_garde_reseau`) ; `gardes.py` (`lever_sur_term`) ; [C4] `9ba07614…` (§ 9 à 11) ; [CF] `b09ae513…` ; [CC]
  `63c6421b…` ; le rapport du code v1 (lignes des différentiels) et les trois différentiels (en-têtes, empreintes) ;
  l'addendum de l'idée 1.2 `1b96cf06…` (forme) ; lignes R-2942, R-2976, R-2978, R-2979, R-2984, R-2986 ; GO-2026-11-16-01
  et GO-2026-11-16-05 (ligne voisine de la recherche).
- Calculs de ma main : `--lister-empreintes` (hachages), lectures du fichier d'étape 0 et du journal par de petits programmes,
  un appel de `lire_addendum` sur cette pièce ; aucun jeu, aucun essai, aucun `pytest`.
- Jamais ouverts : rien sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, P3-bis ni du bras d'attaque ; rien
  écrit dans `/home/user/jeu-idee-1-2-copie` ni `/home/user/etape0-idee-1-1-copie-v5` ; aucune valeur de clé ; ni `env` ni
  `printenv` ; aucun appel réseau ; aucun commit.
- Incidents : aucun. Une première commande groupée de lecture a rendu un code de sortie non nul à cause d'un `ls` sur un nom encore absent (cette pièce), sans autre effet.

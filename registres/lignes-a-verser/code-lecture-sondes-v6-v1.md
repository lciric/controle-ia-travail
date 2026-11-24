# Ligne proposée au registre propre des sondes du barreau 8 : code de la lecture des sondes, version 6

Proposée le 2026-11-24 par le développeur du côté des moniteurs (session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC`), branche `barreau8/code-lecture-sondes-v6-v1`. **La session mère l'inscrit** dans `registres/sondes-iib-v1.md`, en fin de fichier, strictement après la ligne `SCELLEMENT-ADDITIF-2-SONDES-IIB` (par le rang et par l'heure) ; l'heure est celle de l'inscription (elle peut remplacer celle-ci, qui est l'heure d'écriture du bordereau).

```
| CODE-LECTURE-SONDES-IIB | 2026-11-24T14:37:33Z | docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json | dd816daf261fbf6d261a21164fbe475391276795b761e28a7a1e8ec95e0e2d4e |
```

## Bordereau du code de la lecture (neuf clés, M-5)

- Chemin : `docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json`, empreinte `dd816daf261fbf6d261a21164fbe475391276795b761e28a7a1e8ec95e0e2d4e`, compagnon `.sha256`.
- Commit cité : `90136db42ef3c391d96f2a561e06c6afa90da421`.
- Accord de lecture : `GO-2026-11-24-28` (réservé par la session mère, R-5296 ; la ligne au registre des accords attend le mot de Lazar : d'ici là la lecture refuse de partir, condition D-4).
- Textes : texte scellé `8e432cdc…` ; additif 1 `fc5b0610…` ; additif 2 `8e930aba…`.
- Table neuve des constantes : `docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json`, `d576c16b…`.
- Rapport de conformité : `docs/notes/code-lecture-sondes-v6-v1/verification-corrections-lecture-v6-sonnet-v1.md`, `429b5917…` (vérification des corrections, « conforme », par le même contre-lecteur que `contre-lecture-conformite-lecture-v6-sonnet-v1.md`, `aeb4d8b8…`, « conforme »).
- Notice : `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-lecture-sondes-v7.md`, `2b03ebeb…`.

## Modules du code (18), empreintes sha256

| module | empreinte |
|---|---|
| `controle_ia` (`src/controle_ia/__init__.py`) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `controle_ia.barreau8_moniteurs` (`src/controle_ia/barreau8_moniteurs/__init__.py`) | `ced69a179f3b04369bdc8a6058eb4ff9d2eb8ad341b723bb014be090d36f31bd` |
| `controle_ia.barreau8_moniteurs.lecture_sondes_v6` (`src/controle_ia/barreau8_moniteurs/lecture_sondes_v6.py`) | `8b39af4b760c1a621093a31616214d0ff7802212322a020cb67cba2f9a16570a` |
| `controle_ia.barreau8_moniteurs.lectures_descriptives_additif_1_v1` (`src/controle_ia/barreau8_moniteurs/lectures_descriptives_additif_1_v1.py`) | `1135731ce34a929287610316b929a4075c200f6d89bbbcd00a08189efa18420b` |
| `controle_ia.gardes` (`src/controle_ia/gardes.py`) | `a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439` |
| `controle_ia.harnais` (`src/controle_ia/harnais/__init__.py`) | `a977e6e9ad612aa96c099b9c5fb34bb42eb659261dd226780cfc441738b5caaa` |
| `controle_ia.harnais.sondes` (`src/controle_ia/harnais/sondes.py`) | `f92657a69cf0d5781017e50117aeb1672dda60719aea51ffbfd9e566f3e7d94d` |
| `controle_ia.manifeste` (`src/controle_ia/manifeste.py`) | `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d` |
| `controle_ia.premier_test_ia` (`src/controle_ia/premier_test_ia/__init__.py`) | `c72da1602f1998e4c7b30b670e89143d6a9c6337b903164f4bc6eed5ab9a5f92` |
| `controle_ia.premier_test_ia.figees` (`src/controle_ia/premier_test_ia/figees.py`) | `a2238a8c6f164f59f7d30e3ca15c45be136cb3ad5cdf149816622d81450938cc` |
| `controle_ia.prereg` (`src/controle_ia/prereg.py`) | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |
| `controle_ia.scellement` (`src/controle_ia/scellement.py`) | `93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2` |
| `controle_ia.sondes` (`src/controle_ia/sondes/__init__.py`) | `a4ea91421aa179aa7662876afddde30f6558435c6d60c5ee41f7793613b3ba30` |
| `controle_ia.sondes.evaluation` (`src/controle_ia/sondes/evaluation.py`) | `1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3` |
| `controle_ia.sondes.familles` (`src/controle_ia/sondes/familles.py`) | `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` |
| `controle_ia.t07` (`src/controle_ia/t07/__init__.py`) | `553bd9d29b56f0923859da2d3a63fadf9891c4274b9bb23fc367496e77e5a61e` |
| `controle_ia.t07.plancher_v2` (`src/controle_ia/t07/plancher_v2.py`) | `a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796` |
| `controle_ia.t07.registre_v1` (`src/controle_ia/t07/registre_v1.py`) | `e50236574fbcd7e48ea3005eadc8bdb68d2c753d10028db7f2c365648a843cec` |

Contrôle fait sur le dépôt réel avant la proposition (aucune pièce de la course ouverte) : le bordereau se relit par la fonction même de la lecture (neuf clés, textes aux empreintes des lignes de scellement), les modules chargés sont exactement les dix-huit du bordereau (écrit par `python -m`), la table neuve se lit à son chemin et donne la forme de la version 6, les cinq pièces de la condition D-14 sont à leurs empreintes.

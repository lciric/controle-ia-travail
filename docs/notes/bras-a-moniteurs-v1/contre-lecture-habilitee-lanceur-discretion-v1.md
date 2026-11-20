# Contre-lecture habilitée — lanceur de l'étape de discrétion du bras A, côté moniteurs, et pièces liées — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `contre-lecture-habilitee-lanceur-discretion-sans-interne-v1.md`, même dossier.

Écrit par le lecteur habilité côté moniteurs (agent neuf, Claude Fable 5.2 ; le développeur est un Opus 5.5), le 20 novembre 2026, sous GO-2026-11-20-21. Classe B. Copie de travail `/home/user/bras-a-habilite`, branche `claude/bras-a-habilite-developpeur-v1`, tête `e13ed92822a7ee0cd587592f94bce2c6442d325a`. Ni commit ni poussée. Aucun fichier du dépôt modifié hors de mes deux sorties : les essais et les retraits ont été joués sur trois copies d'épreuve dans le bloc-notes de la session.

## 1. Verdict

**Conforme après ces corrections.** L'ordre des six étapes, la garde de production, la séparation de la préparation et de la production, l'engagement de la table avant toute production et l'absence de toute suppression sont tenus. Un défaut bloque une course réelle : une seconde reprise du même moniteur est refusée (C1). Onze autres corrections suivent, dont douze gardes sans artefact qui morde (C8).

| pièce | verdict |
|---|---|
| lanceur, version 1, et ses essais | conforme après C1 à C11 (version neuve du lanceur, R12) |
| préparation des lectures, version 3, et ses essais | **conforme** : aucune position tirée pour le juge |
| module des autres moniteurs, version 11, et ses essais | **conforme** : seule l'empreinte de la préparation change |
| attestation de la version 7 à la version 10, et ses différentiels | **conforme**, avec une précision à ajouter (C12) |
| gabarit de la configuration | conforme après C5 (quatre modules à citer) |
| pièce sans interne | **aucune fuite** ; deux phrases à ajuster après les corrections (C13) |

## 2. Ce que j'ai lu, et ce que je n'ai pas ouvert

Lu : les mandats v1 (sections 1, 2, 4) et v3 ; la notice du développeur ; par `git show` sur `origin/claude/pensive-bardeen-1fv7hw`, l'extrait du lanceur v3 et le module d'entrée v2, et rien d'autre de la relance ; le lanceur, la préparation v2 et v3, le module des autres moniteurs v7, v10 et v11, le module des deux moniteurs à modèle de langue v3, l'extraction pour la base v2, la pièce de la base et son lanceur, les fonctions du harnais que le lanceur appelle ; les essais ; l'attestation, ses différentiels, ses scripts et ses relevés ; le gabarit ; la pièce sans interne ; le script et les relevés de l'épreuve par retrait.

Non ouvert : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `/root/.claude/`, `archives-reponses-modeles/` ; aucun fichier « consigne-privee » ni « conception-ii-b » ; pas la branche `lot/compte-4-v1` ; aucun texte `prereg/T0.7-organismes-discrets-v-a-*` ; aucun module `graines_bras_a_v*`. Aucun poids chargé, aucun réseau hors `git show` local, aucune dépense. Aucun refus d'outil.

## 3. Empreintes vérifiées, chacune contre son compagnon

| pièce | empreinte | compagnon |
|---|---|---|
| `src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v1.py` | `96ac8d8b8370967e7e87bce26681008dffc776321cf65c217923b7e356d57e73` | égal |
| `…/bras_a_v2_habilite_lanceur/__init__.py` | `0cd2928442dea2035ee5c64252d5853d7c3b0cd117c4ae527e0421d1ad16088c` | égal |
| `tests/test_bras_a_v2_habilite_lanceur_discretion_v1.py` | `0bef30a50010ee67e13840b9b91201519741f0cde5f43d6b592fedd4e66abdba` | égal |
| `…/bras_a_v2_habilite_preparation/preparation_des_lectures_v3.py` | `c0021298c21d027a713b1947d2668ac928f2a856b1a696686dd35b83a9515c45` | égal |
| `tests/test_bras_a_v2_habilite_preparation_des_lectures_v3.py` | `70badfe1d058b72ab3f8450a3b9271fe97a7ce14a009334200f2e7858bd8a877` | égal |
| `…/bras_a_v2_habilite/autres_moniteurs_v11.py` | `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda` | égal |
| `…/bras_a_v2_habilite/autres_moniteurs_v10.py` | `42c78bd5b10e970d98adf2b388f290d92e79d0a62b3de82937c91bb70949bd6c` | égal |
| `tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py` | `92711976e9ee949b08719b791cafc53932763ab96a04b6c01d34b0068cc3c776` | égal |
| `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1.md` | `6555abc42fbf0465ddbdc5b9d19e70b52f16ac6ce946fa00729abf621f867c6a` | égal |
| `…/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v7-a-v10.diff` | `aacb9f64341c3278400f34ed8af8843cdabf265bc67653b390a137a1a1b9a402` | égal |
| `…/differentiel-autres-moniteurs-v10-a-v11.diff` | `b7ac6de62b8e0c7c5c8619dd29cd7af2b56a6b07fe2cfba27e15639fb4a19d0a` | égal |
| `…/essai_equivalence_v7_v10.py` ; `…/essai_equivalence_v7_v10_v2.py` | `8cd371e3ece20dd84e7ccec8eda61b020b9fe3f8281bdd6479e01a67692281fd` ; `c24d17ff4cbf8f9061f545d1382a049855234c089ce957c59b493e60491dfb21` | égaux |
| `…/releve-essai-equivalence-v7-v10.md` ; `…/releve-essai-equivalence-v7-v10-v2.md` | `8c224b267e3c4f2def650ccfb026435d2f527059f398c611805c8fcc41eddcfb` ; `f36336132e2e11606d08aef9722bb2eafd83952766e620c756bfcd14d8bcb8c7` | égaux |
| `docs/notes/bras-a-moniteurs-v1/config-lanceur-discretion-bras-a-gabarit-v1.json` | `0da610c43edf15eb0b28c361882ea0536dc11bedfcc4cc35cf1254376e062a4b` | égal |
| `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-18-19-24a-v1.md` | `e2f246ebb533ce8a28f4a54c8068723cd30340059c68ff5cf34fc7edd965330b` | égal |
| `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-lanceur-discretion-v1.md` | `d1b19bc21d098547f7aba6cd6c6bcb5cadad63d5d2bb5045b36c39a19102f884` | égal |
| `…/epreuve-par-retrait-lanceur-discretion-v1/epreuve_retraits_lanceur_v1.py` | `f439b9784c8c55757af7986c125ff831f4008671aaeead975600a363a437e01c` | égal |
| `…/releve-retraits-lanceur-premiere-passe-v1.md` ; `…/releve-retraits-lanceur-seconde-passe-v1.md` | `9f792ee86bd3df86fd2c5d617721d90bcb0bea9c31d17d00ee5e75d81acf1ef0` ; `27532165a59154d72f2f5d360e6ca569b119e8efc6bcd67bf2aaef8b0314ba52` | égaux |
| mandats v1 et v3 | `a156d2db818e28c8a72f3fa49e571342ca65b389ca2458e799fb323d6a69b360` ; `374af2488f6804c0dcf94218a2993bd42710116305cd5ae5877c0ac22e982dbc` | égaux |
| extrait du lanceur v3 (relance) | `5d2a48c0f9b6b8a36b20cc466508c44fe1c2aad84a17b98cfb1190f85c631bed` | égal |
| module d'entrée v2 (relance) | `cb668bb95a9c0a37b1a08a91f304e1b756ef5b0ebddc0a3f193be0692e0bfa10` | égal |

Sans compagnon dans la copie de travail (R6), empreintes égales à celles que l'attestation et la version 10 citent : `autres_moniteurs_v7.py` (`3b5dccc9…`), `autres_moniteurs_v8.py` (`61105129…`), `preparation_des_lectures_v2.py` (`6dfd2bfc…`). Défaut ancien, hors de cette livraison : à sceller par la mère.

Les neuf empreintes du gabarit (modules appelés) sont celles des fichiers, le module d'entrée compris.

## 4. Ce que j'ai rejoué

| épreuve | résultat |
|---|---|
| essais du lanceur | `18 passed` |
| essais de la préparation v3 | `8 passed` |
| essais du module v11 | `4 passed` |
| épreuve par retrait du développeur, rejouée en entier sur une copie d'épreuve | **46 retraits mordent sur 46** ; lanceur et préparation remis à l'identique (`96ac8d8b…`, `c0021298…`) |
| différentiel 7 → 10 régénéré (`diff -u`) | identique au fichier scellé (853 lignes) |
| différentiel 10 → 11 régénéré | identique au fichier scellé (26 lignes) |
| comparaison des versions 7 et 10, fonction par fonction (arbre syntaxique) | 12 noms changés, 35 ajoutés, aucun retiré : la liste de l'attestation |
| comparaison des versions 10 et 11, de même | un seul nom changé : `PROGRAMMES_DE_PRODUCTION` |
| essai d'équivalence 7 et 10, version 2, rejoué | relevé identique à l'octet au relevé scellé : aucun nombre commun ne diffère, douze lectures |
| **quatorze retraits de plus**, de ma main, sur des gardes que la liste du développeur ne porte pas | **2 mordent sur 14** (C8) |
| **cinq scénarios de plus**, de ma main | quatre montrent un défaut (C1, C2, C6, C7) ; un confirme un refus sans réparation (C10) |

## 5. Ce qui est tenu, vérifié sur le code

- **Ordre des six étapes** : garde de production en tête de `discretion` (ligne 666) et juste avant le premier appel de chaque moniteur (ligne 577, avant le chargeur) ; accord de l'entropie propre appelé avant le tirage, avec les sept arguments de l'extrait, son dictionnaire consigné tel quel ; engagement inscrit avant toute production ; manifeste de production posé puis inscrit ; cinq ouvertures ; lecture commune avec l'entropie de la configuration du bras, l'échange par paire et la forme « rang ».
- **Aucun tirage** hors de la table : une seule ligne du lanceur touche au hasard (ligne 458). Aucun module de graines importé ; du code de la relance, seul le module d'entrée, par ses noms.
- **Aucune suppression** : le lanceur n'appelle que `os.rename`, après avoir vérifié que le nom final est libre.
- **Préparation v3** : la branche du juge et le compte « hors du sous-échantillon » sont retirés ; `positions_du_juge` n'apparaît plus dans le corps ; la clé de graine ne porte pas la condition.
- **Module v11** : le différentiel avec la version 10 ne porte que le paragraphe d'en-tête et les deux lignes de la préparation dans `PROGRAMMES_DE_PRODUCTION`.
- **Interface avec la base** : la ligne `CONFIG-BRAS-A-V2` que le lanceur inscrit a le format que la pièce de la base lit (quatre cellules, chemin relatif à la racine) ; le chemin proposé par le gabarit ne porte aucun fragment que la liste blanche de la base refuse ; `--racine-entrees` et `--registre` sont ceux du lanceur de la base.
- **Signatures du chemin réel**, que les essais ne jouent pas : `regler_determinisme`, `charger_modele`, `fins_du_modele`, `FormatChat`, `exiger_moniteur`, `lecteur_du_cas`, `lire_avec_raisonnement` sont appelés avec les bons arguments. Les valeurs de chargement du gabarit sont celles de la note à citer et de son erratum.
- **Hypothèse du point 4 de la notice, vérifiée** : l'agent voit `"Problem statement:\n" + tache.questions.strip()` (`environnements/propositions.py`, ligne 242) ; le fichier des tâches a la forme que lit `environnements/pilote_a.charger_taches`. Le champ `questions` est donc l'énoncé de l'agent, **à ses blancs de bordure près** (C7).
- **Nombre de programmes qui nomment le fichier des rangs** : 5, recompté.

## 6. Corrections

### C1 — bloquante — une seconde reprise du même moniteur est refusée

Le relevé de reprise est écrit dans le dossier des morceaux du moniteur. À la reprise suivante, `_morceaux_presents` le prend pour un fichier inattendu. Scénario joué : panne au juge après deux morceaux, reprise, nouvelle panne, troisième exécution. Refus exact : `dossier des morceaux : fichier inattendu (reprise-juge-001.json) : arrêt`. Les scores déjà produits restent scellés, rien n'est perdu ; mais le lanceur ne peut plus finir, et sa configuration est scellée.

Avant (ligne 105, puis lignes 539 et 540) :
```
_MORCEAU = re.compile(r"^morceau-(\d{5})\.jsonl$")
```
```
        m = _MORCEAU.fullmatch(p.name)
        if not m or int(m[1]) >= n:
```
Après :
```
_MORCEAU = re.compile(r"^morceau-(\d{5})\.jsonl$")
_RELEVE_DE_REPRISE = re.compile(r"^reprise-[a-z-]+-\d{3}\.json$")
```
```
        if _RELEVE_DE_REPRISE.fullmatch(p.name):            # relevé scellé d'une reprise antérieure : ni lu ni refusé
            _scelle(p)
            continue
        m = _MORCEAU.fullmatch(p.name)
        if not m or int(m[1]) >= n:
```
Essai à ajouter : deux pannes de suite au même moniteur, puis une exécution qui finit ; deux lignes `REPRISE-PRODUCTION-BRAS-A`. Éprouvé sur ma copie : passe après la correction.

### C2 — une reprise sans morceau du moniteur en cours n'est ni comptée ni inscrite

L'extrait dit : « La reprise est comptée et inscrite. » Le lanceur ne l'inscrit que si un morceau du moniteur en cours est déjà scellé. Scénario joué : le moniteur boîte noire est fait et inscrit, panne au premier morceau du juge, relance. Résultat : zéro ligne `REPRISE-PRODUCTION-BRAS-A`.

Avant (signature de `produire`, puis ligne 563) :
```
             manifeste: Manifeste | None = None) -> Path:
```
```
    if presents:
```
Après :
```
             manifeste: Manifeste | None = None, reprise: bool = False) -> Path:
```
```
    if presents or reprise:
```
Dans `discretion`, avant (ligne 690, puis lignes 711 à 713) :
```
        (engagement, chemin_table), table = deja, None
```
```
                                 chargeur=charger, dossier_production=d["production"], racine=racine, lire=lire,
                                 manifeste=manifeste)
```
Après :
```
        (engagement, chemin_table), table = deja, None
    reprise = deja is not None
```
```
                                 chargeur=charger, dossier_production=d["production"], racine=racine, lire=lire,
                                 manifeste=manifeste, reprise=reprise)
        reprise = False
```
Reste à couvrir, de la même façon : une relance après les deux productions inscrites et avant la première ouverture (aucun appel de `produire`) doit elle aussi écrire un relevé scellé et une ligne. Éprouvé sur ma copie pour le premier cas : une ligne inscrite, les 18 essais passent.

### C3 — la pièce source et ses modules gelés ne sont vérifiés qu'après les cinq ouvertures

`lire_les_cinq` vérifie la pièce source de la base et sa table de modules gelés à l'étape 6. Un écart y arrête le lanceur après les ouvertures, où aucune reprise n'est permise : les heures de carte sont dépensées, les moniteurs sont dits ouverts, et rien n'est lu.

Avant (lignes 666 et 667) :
```
    A.exiger_production_permise(registre)
    exiger_aucune_ouverture(registre)
```
Après :
```
    A.exiger_production_permise(registre)
    exiger_aucune_ouverture(registre)
    A.charger_piece_source(racine)          # pièce source et modules gelés : avant toute production, non après les ouvertures
```
Avec un artefact (un module gelé changé : refus à l'étape 1, aucun fichier écrit). Éprouvé sur ma copie : les 18 essais passent.

### C4 — la configuration de la base n'est pas comparée à la ligne `CONFIG-BRAS-A-V2`

La base lit la configuration que désigne la ligne du registre, à son empreinte. L'étape de discrétion relit le même fichier par son seul compagnon : un fichier changé avec son compagnon entre la base et l'étape de discrétion passerait.

Avant (ligne 674) :
```
    _scelle(d["extraction"] / X.FICHIER_CONFIG)
```
Après :
```
    ligne_config = lignes_du_registre(registre, CLE_CONFIG_BRAS)
    if len(ligne_config) != 1 or ligne_config[0]["chemin"] != _relatif(racine, d["extraction"] / X.FICHIER_CONFIG):
        raise GardeArret(f"registre : une ligne {CLE_CONFIG_BRAS}, qui désigne la configuration du dossier "
                         "d'extraction, attendue")
    _scelle(d["extraction"] / X.FICHIER_CONFIG, ligne_config[0]["sha256"])
```
Avec deux artefacts (ligne absente ; configuration changée et rescellée). Éprouvé sur ma copie : les 18 essais passent.

### C5 — quatre modules appelés ne sont pas cités par leur empreinte

L'extrait veut que la configuration cite « par leur empreinte entière […] les modules qu'il appelle, dont les programmes de la production ». Le lanceur appelle lui-même `harnais/modeles.py` et `harnais/formats.py` ; la lecture du score passe par `bases/scores_jetons.py` et `environnements/pilote_a.py`. Aucune table ne tient ces quatre fichiers. (`environnements/propositions.py`, `manifeste.py`, `scellement.py` et `gardes.py` sont tenus par la table des modules gelés de la pièce source : après C3, ils sont vérifiés avant la production.)

Correction : ajouter à `MODULES_APPELES` et au gabarit :

| clé | chemin | empreinte |
|---|---|---|
| `chargement_des_modeles` | `src/controle_ia/harnais/modeles.py` | `d0befc29aeba4b2487b85d365b8087c467769f0d99f610267f85f19cbea221a7` |
| `format_de_conversation` | `src/controle_ia/harnais/formats.py` | `98dbfa9b13578946c4d731c4bb1cfcfb85b9fd0cacdfd56a786042c93e6ef6b4` |
| `lecture_du_score` | `src/controle_ia/bases/scores_jetons.py` | `64946a47db66ea8c8257f21a14d0433de275dd505b63cd378012159df9af1914` |
| `derniere_position` | `src/controle_ia/environnements/pilote_a.py` | `624761e2831a3fa14ccc1fe817d38a59014c9ef157e600cbd67e411607869bfc` |

### C6 — `relever-fins` ne peut pas servir à ce pour quoi il est écrit

La sous-commande sert à remplir les jetons de fin « avant le scellement ». Elle exige pourtant une configuration scellée sans valeur nulle, jetons de fin compris. Refus exact : `REFUS : configuration : valeurs à fixer laissées nulles : ['fins_moniteur_boite_noire']`.

Avant :
```
def lire_la_configuration(chemin: Path, *, cli: bool = False) -> tuple[dict, str]:
```
```
    nulles = [k for k, v in c.items() if v is None]
```
```
    if not (isinstance(fins, list) and fins and all(
```
```
        cfg, sha = lire_la_configuration(chemin_config, cli=True)
```
Après :
```
def lire_la_configuration(chemin: Path, *, cli: bool = False, fins_a_relever: bool = False) -> tuple[dict, str]:
```
```
    nulles = [k for k, v in c.items() if v is None and not (fins_a_relever and k == "fins_moniteur_boite_noire")]
```
```
    if not (fins_a_relever and fins is None) and not (isinstance(fins, list) and fins and all(
```
```
        cfg, sha = lire_la_configuration(chemin_config, cli=True, fins_a_relever=a.sous_commande == "relever-fins")
```
La configuration de relevé et la configuration finale portent deux noms (R12). Éprouvé sur ma copie, avec une doublure du relevé.

### C7 — un énoncé bordé de blancs passerait tel quel au moniteur

L'agent voit l'énoncé sans ses blancs de bordure ; le lanceur le passe tel quel. Les fichiers de tâches produits par `environnements/extraction.py` sont déjà sans blancs, mais rien ne le garde.

Avant (lignes 429 à 431) :
```
    manquantes = [t for t in taches_verification if not (isinstance(q.get(t), str) and q[t].strip())]
    if manquantes:
        raise GardeArret(f"tâches : énoncé absent pour {len(manquantes)} tâche(s) de vérification")
```
Après : les mêmes trois lignes, suivies de :
```
    bordees = [t for t in taches_verification if q[t] != q[t].strip()]
    if bordees:
        raise GardeArret(f"tâches : énoncé bordé de blancs pour {len(bordees)} tâche(s) : l'agent le voit sans eux")
```
Avec un cas sain et un artefact.

### C8 — douze gardes du lanceur n'ont aucun artefact qui morde (R5)

La notice dit 45 gardes du lanceur éprouvées par retrait. La liste en oublie. J'ai retiré quatorze autres gardes, une à une, et rejoué les 18 essais : douze retraits laissent tout passer.

| garde retirée | mord | seule à tenir ce qu'elle garde ? |
|---|---|---|
| tâches : identifiant en double (`_questions`) | **non** | oui |
| tâches : énoncé absent (`_questions`) | **non** | non (la préparation refuse aussi) |
| tâches : fichier à l'empreinte de la configuration | **non** | oui |
| registre absent (`lignes_du_registre`) | **non** | non (la garde de production refuse avant) |
| fichier scellé : empreinte ≠ celle attendue (`_scelle`, argument `attendu`) | **non** | oui, pour la configuration du bras, les tâches, la table à la reprise, le manifeste inscrit |
| fichier scellé : empreinte ≠ compagnon | oui | — |
| fichier cité : forme `{chemin, sha256}` | oui | — |
| reprise : table à l'empreinte engagée (`table_deja_engagee`) | **non** | oui avant les ouvertures |
| reprise : demandes et bilan scellés (`preparer_les_demandes`) | **non** | oui |
| reprise : table relue à son engagement | **non** | oui avant les ouvertures |
| reprise : manifeste de production inscrit à son empreinte | **non** | oui |
| discrétion : configuration du bras à son empreinte | **non** | oui |
| discrétion : textes et configuration de la base scellés | **non** | en partie |
| production : forme de la ligne produite (`_ligne_de_production`) | **non** | non (l'écriture de la production refuse aussi, mais après le scellement des morceaux) |

Correction : un artefact par garde (douze essais), et ces quatorze retraits ajoutés au script de l'épreuve, avec ceux des gardes neuves de C1 à C7. Retraits exacts : ceux de mon script, repris ci-dessous par leur texte « avant ».

```
if t.get("identifiant") in q:
    if manquantes:\n        raise GardeArret(f"tâches
    _scelle(p, cfg["taches"]["sha256"])\n
if not registre.is_file():\n        raise GardeArret(f"registre {registre.name} absent")
if attendu is not None and vue != attendu:
    _scelle(chemin, lignes[0]["sha256"])\n
            _scelle(dem)\n            _scelle(bil)\n
            _scelle(chemin_table, engagement)\n
            _scelle(chemin, inscrites[0]["sha256"])\n
    _scelle(racine / cfg["configuration_du_bras"]["chemin"], cfg["configuration_du_bras"]["sha256"])\n    entropie_du_bras
    _scelle(d["extraction"] / X.FICHIER_TEXTES)\n    _scelle(d["extraction"] / X.FICHIER_CONFIG)\n
    A.exiger_ligne_de_production(x)\n
```

### C9 — le manifeste du lanceur ne porte ni versions, ni commit, ni réglages de déterminisme (R9)

Il porte ce que l'extrait demande (commande, programmes, fichiers, heures). R9 demande aussi les versions et le commit. Les lectures des deux moniteurs dépendent de la carte et des bibliothèques. Correction : ajouter au manifeste `versions` (Python, numpy, torch, transformers), `commit` (tête du dépôt de la racine), et, pour `discretion`, le dictionnaire que rend `regler_determinisme` (aujourd'hui gardé dans la liste `regle` du chargeur, jamais écrit).

### C10 — notice, point 6 : une troisième fenêtre sans réparation n'est pas dite

Scénario joué : panne entre la pose du manifeste de production et son inscription au registre. À la relance, refus : `scores-produits-moniteur-boite-noire.jsonl existe déjà sous son nom final : on n'écrase jamais (R12)`. C'est un refus, non une perte ; il doit être dit. Avant : « une panne entre l'écriture d'un fichier par un module sous le provisoire et sa pose, ou entre la pose de la table et l'inscription de l'engagement, donne un refus ». Après : « …ou entre la pose de la table et l'inscription de l'engagement, ou entre la pose d'un manifeste de production et son inscription, donne un refus ».

### C11 — le module d'entrée est importé avant que son empreinte soit vérifiée

Dans `discretion`, `charger_le_module_d_entree()` (ligne 658) précède `verifier_les_modules` (ligne 659) : le code d'un fichier non vérifié s'exécute à l'import. Correction : vérifier d'abord l'empreinte des fichiers (boucle sur `MODULES_APPELES`), importer ensuite, puis vérifier que le module importé est le fichier de la racine.

### C12 — attestation : une précision manque à la partie 2

Aux cas D et E, deux choses changent dans ce qui est rendu, que la partie 2 ne dit pas et que la partie 4 ne dit qu'en passant : le champ `calculable` passe de faux à vrai, et la valeur p qui entre dans la famille passe de 1 à la valeur p haute (GO-2026-11-19-70). Ce n'est pas un calcul de moniteur ; c'est une règle de rendu qui change l'état. À ajouter, comme quatrième précision : « 4. **Aux cas D et E, l'état rendu change par décision** (GO-2026-11-19-70) : la version 7 rendait le moniteur non calculable et mettait à 1 la valeur p de la famille ; la version 10 le rend calculable avec un motif, et met dans la famille la valeur p haute. Les nombres calculés sont les mêmes. » La table de la partie 3 omet aussi trois constantes de gardes de forme (`CLES_COMPTES_DES_LECTURES`, `_NOMBRES_DE_L_AIRE`, `_NOMBRES_DES_VALEURS_P`) : à y nommer. Par erratum (classe B).

### C13 — pièce sans interne : deux phrases plus larges que le code de la version 1

« reprise après une panne de transport, comptée et inscrite » : vrai seulement après C1 et C2. « cite par empreinte entière chaque module appelé » : vrai seulement après C5. À redire dans la version neuve de la pièce, avec l'empreinte du lanceur corrigé.

## 7. Remarques, sans correction exigée

1. **Registre partagé.** Le lanceur ajoute au registre des scellements quatre clés neuves, dont une répétable. Le lecteur de registre de T0.7 (`src/controle_ia/t07/registre_v1.py`) refuse toute clé bien formée qui n'est ni exigée, ni permise, ni marquée d'une autre tâche par sa configuration scellée. La question vaut déjà pour les clés de la base au bras A. À vérifier par la mère avant la course : que la marque du bras A est dans cette liste, ou donner au bras A un registre à lui (la clé `registre` de la configuration le permet).
2. **Sorties de lecture non gardées.** `_ligne_de_production` ne garde que cinq champs. Les identifiants générés par chaque moniteur, la masse, le nombre de jetons et la jointure de la coupe ne sont écrits nulle part. La forme à cinq champs est celle de la version 10, déjà vérifiée. Mais ces sorties d'une course payante ne se retrouvent qu'en la rejouant. À trancher par la mère, au regard de « récupérer ce qui est récupérable » : les garder, scellées, dans le dossier à part.
3. **Chemin réel non éprouvé** (point 8 de la notice) : `chargeur_reel` et `relever_fins` ne sont joués que par des doublures, et le module d'entrée est absent de cette branche. Les signatures sont justes à la lecture. Un essai sur la machine de calcul, avant la course, reste à faire.
4. **Nom du manifeste du lanceur** : à la seconde près. Deux arrêts dans la même seconde feraient refuser le second scellement, qui masquerait l'erreur d'origine. Ajouter le numéro de l'exécution au nom.
5. **Module v11, ligne 724** : une phrase de documentation parle encore du « sous-échantillon du juge ». Elle vient de la version 10, sans effet sur un calcul. À retirer à la prochaine version.
6. **Texte scellé** : la configuration cite son empreinte, que le lanceur ne compare à aucun fichier. C'est ce que l'extrait demande (le texte n'est pas ouvert).
7. **Ce que l'extrait laisse à trancher**, et que la notice signale justement : qui inscrit `CONFIG-BRAS-A-V2` ; les trois sous-commandes au lieu d'une exécution ; le module de graines non cité par empreinte.

## 8. Vérification des corrections

Par le même contre-lecteur (classe B), sur la version neuve du lanceur, ses essais, le script de l'épreuve par retrait étendu, le gabarit, l'erratum de l'attestation et la version neuve de la pièce sans interne.

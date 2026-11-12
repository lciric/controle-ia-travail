# Relecture différentielle du code v15 du témoin de Bailey (lanceur_v15, instance_v14) — corrections de la relecture v14

- **Qui** : relecteur neuf (règle R2), sous-agent qui n'a écrit ni le code ni la relecture v14.
- **Quand** : 12 novembre 2026 (UTC).
- **Commit lu** : `7ed9ed8d8073e12581b2a151f67b71acd2009d6c` (arbre propre : `git status` vide).
- **Routine de reprise** : non exécutée (consigne). Aucune instance, aucun appel réseau, aucun `git commit` ni `git push`.
  Aucun fichier cloisonné ouvert, aucune valeur de clé lue.

Fichiers lus (SHA-256) :

| Fichier | Empreinte |
|---|---|
| `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v14-bailey-v1.md` (en entier) | `0e7c96ca231465ee4a2e0cf5fbe9c1d146d6caa5ce60460462adaf067fa3c377` |
| `src/controle_ia/temoin_bailey/instance_v13.py` | `62686ac11dbba382b97cd16c94f5280570f783d9329f8dcb3a7fc78776d20032` |
| `src/controle_ia/temoin_bailey/instance_v14.py` | `19366e7acae186ca1587f73d097a190fadd930b91544f2626bb9d9e9fbd0cf75` |
| `src/controle_ia/temoin_bailey/lanceur_v14.py` | `02e9816a64160cea5a38f2c4cb10612d94f9ee6a8712c6da59684528f32fc101` |
| `src/controle_ia/temoin_bailey/lanceur_v15.py` | `819258047270dd731b3bf8aca072cdcb82c173d2928b24f2182a3d88492c04a9` |
| `tests/test_temoin_bailey_condition6_v14.py` | `6f4809a5f8107d77df59aaeaa95297e134c7861da322cf12808a4e68325d7ba9` |
| `tests/test_temoin_bailey_condition6_v15.py` | `13bf913829e87a454cfa4e2d4bd10b14f5af10055365dc5bee96de58b51c8122` |
| `src/controle_ia/temoin_bailey/journaliseur_v3.py` (l. 155-340 : chemins des journaux) | `9f75407c0afaab4c605fb4ab758df214c91f4ce5df6c86f15dc93db04996be90` |
| `src/controle_ia/temoin_bailey/conventions_v3.py` (l. 60-95 : noms) | `51c2fa26a4e61038b14c97825618e2006be9572c9f82d67a2d5e26bea2bbca86` |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (Gardes l. 272-314, Ce qui sort l. 316-319, Liste d'arrêt l. 358-371) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-2-condition6-arret-autonome.md` (passages « Ce qui sort ») | `f79459c712a0f12ecbf55c9ea787f67032031e9672e6db002b84725286c96e13` |
| `brouillons/temoin-attaque-publiee-bailey-v1-addendum-3-code-v14-brouillon1.md` (en entier) | `614dc5d7669ccc598186a13df11937448752e9cc0fdf9ceba3c924cc108dc78a` |

Les empreintes compagnons `instance_v14.py.sha256` et `lanceur_v15.py.sha256` sont égales à celles du tableau.

**Essais** : `PYTHONPATH=src python -m pytest -q tests/test_temoin_bailey_condition6_v15.py` : **156 passés**, 162,6 s
(147 essais v14 rejoués + 9 nouveaux). L'essai instable de la v14
(`test_v13_P2_processus_reels_veilleur_arrete_autre_pid_jamais_signale`) seul : 6 passés sur 6.
**Mutations** (copie du code dans le dossier de travail temporaire, rien dans le dépôt) : `prefixe = True` à la l. 798 →
2 essais tombent (configuration plus courte ; dépense) ; retrait du seul terme `and cause is None` → 1 essai tombe
(dépense), et seulement par un effet de temps (voir D-4).

## Verdict

**Conforme après corrections.** Aucune fuite de note ni de texte produit : la condition d'écriture (début strict de la
configuration, aucun arrêt décidé, zéro tour, journal des notes et dossiers vides) tient la garantie à elle seule. Mais le
filtre v14 détruit à son tour une partie du diagnostic (D-1, D-2), le terme ajouté `cause is None` n'a pas d'artefact
déterministe (D-4), et le brouillon 1 de l'addendum 3 décrit encore le code v13 (D-9).

## 1. Points de la relecture v14, un par un

| Point | État | Passage du diff et commentaire |
|---|---|---|
| R-1 (filtre qui retire les lignes de cause) | **En partie** | `instance_v14.py` l. 233-265 : `_DECIMAL` remplace sur place (`<nombre>`) ; `python3.11`, `2.4.1`, `/root/venv/lib/python3.11/…` gardés ; ligne à `tensor(` retirée entière (plus strict que la proposition, correct). Mais `_SUITE` (l. 238) et `_JETON` (l. 237) retirent des noms qui disent la cause (D-1, D-2). Essai `test_v15_filtre_garde_les_lignes_de_trace_reelles` ajouté (l. 3405), sans ces cas. |
| R-2 (condition insuffisante) | **Corrigé** | l. 798 : `prefixe = surv.attendu.startswith(surv.tampon) and cause is None` ; l. 285-288 : en plus, `_vide(journal des notes)`, `_vide(sondes)`, `_vide(params)`. Le tampon n'est rempli que tant que la garde n'est pas décidée et reste strictement plus court que l'attendu : « début exact » veut bien dire « l'impression de la l. 173 n'est pas finie ». Essais : cas sain « moitié de la configuration » (l. 3447), artefact « configuration plus courte et différente » (l. 3455), dossiers non vides (l. 3427). Le terme `cause is None` dépasse la demande (D-4, D-6). |
| R-4 (filtre : jeton, longues suites) | **Corrigé dans le code, trop large** ; texte renvoyé | l. 237-238, appliqués avant les nombres. Seuils plus bas que ceux proposés (8 au lieu d'une longueur de jeton réelle ; 32 au lieu de 40, et sans exclure les chemins ni les identifiants) : D-1, D-2. La partie « texte » (le message peut porter les surcharges et des morceaux de configuration) n'est pas encore dans l'addendum 3 (D-9). |
| R-5 (masquage de `signal`) | **Corrigé** ; un écart de comportement | l. 846-861 (`reconstituer_etat`) et l. 1431-1435 (`main`) : `signaux`. Essai d'analyse de syntaxe `test_v15_aucun_masquage_du_module_signal` (l. 3498). Essai d'arrêt par la dépense et l'échéance ajouté (l. 3474) : plus d'`UnboundLocalError`. Mais la relecture demandait qu'un enfant **muet** arrêté par la dépense **écrive** le fichier ; le terme `cause is None` fait l'inverse (choix plus strict, à écrire : D-6), et l'essai ne le vérifie que par un effet de temps (D-4). Le défaut ancien (v7 à v12) reste à rapporter à Lazar (règle R4) : le brouillon 1 le décrit, sans dire qu'il date de la v7 ni que six relectures l'ont manqué (D-9). |
| R-6 (essais R5 incomplets) | **En partie** | 1 (branches `complets != 0`, `code_retour None`) : fait, l. 3416. 2 (configuration partielle ; plus courte) : fait. 3 (arrêt par la dépense ou l'échéance, enfant muet) : en partie (D-4). 4 (lignes de trace réelles) : fait, sans identifiant long ni chemin du cache Hugging Face (D-1). 5 (lecture d'un dossier qui porte le fichier) : **non fait** — l. 3489 n'appelle que `relance_permise` et `issue_pilote` sur un dictionnaire ; aucun dossier, ni `dossier_de_foi`, ni `journaux_scelles`, ni `garde_fin_de_run` (D-8). 6 (écriture qui échoue) : fait par substitution d'`os.replace` (l. 3464), meilleur qu'un dossier en lecture seule (l'instance tourne en administrateur) ; « état écrit quand même » non vérifié (appel direct). |
| R-7 (essai instable) | **Corrigé (dans l'essai)** | `tests/…_v15.py` l. 3196-3198 : attente bornée de 5 s de `not processus_vivant(pid)`. Option « essai » de la relecture ; code de production inchangé (bénin, dit R-7). 6 sur 6 en isolé. |
| R-9 (diff du lanceur) | **Corrigé** (longueur) | `lanceur_v15.py` l. 260-261 : import scindé, lignes ≤ 120 caractères. `SORTANTS` reste en tête, hors de l'ordre alphabétique (cosmétique, sans suite). |
| Petit point `_ecrire_texte` | **Corrigé** | l. 296-311 : `try` / `except BaseException` : temporaire effacé, erreur relevée ; aligné sur `_ecrire_json`. |
| Petit point ligne `ETAT` | **Corrigé** | l. 1450-1454 : `erreur_demarrage` ajouté. Le lanceur ne lit la ligne `ETAT` que par `json.loads` (`lire_etat`, `lanceur_v15.py` l. 1193-1200) : une clé de plus est sans effet. |
| Petit point coupe à 20 000 octets | Sans changement (aucun demandé) | l. 266-267. Bien. |
| Petit point `splitlines` | Sans changement (aucun demandé) | Bien. |

**Question 2c — le lanceur v15** : le diff normalisé (`sed instance_v13→instance_v14, lanceur_v14→lanceur_v15`) ne montre que
la docstring v15 (l. 1-7, docstring v14 gardée dessous, mentions historiques justes), l'import scindé (l. 260-261) et le
commentaire de `VEILLEUR_MODULE` (l. 280). Le diff brut ajoute `INSTANCE_MODULE`, `CHEMINS_ARCHIVE`, le commentaire C6 et
deux messages (l. 906, l. 1772). **Rien d'autre.**

## 2. Points nouveaux

Mesures faites sur `erreur_demarrage_filtree` (sortie gauche → sortie droite), dossier temporaire :

| Entrée | Sortie v14 |
|---|---|
| `score 0.97 pour l'entree` ; `loss=-0.97` ; `[0.97 0.12]` ; `Tried to allocate 1.96 GiB` | remplacés (`<nombre>`) : bien |
| `score .97` ; `lr 1e-3` ; `note 9.7466e-01` ; `array([9.7466e-01, 1.2e-02])` ; `taux 97%` ; `38 reponses sur 200` ; `probabilité 0,97` | **inchangés** |
| `transformers>=4.44` ; `Python 3.11 required` | `>=<nombre>`, `Python <nombre>` (perte mineure) |
| `No module named 'hf_transfer'` ; `hf_quantizer` | **`'<jeton>'`** |
| `cannot import name 'is_torch_greater_or_equal_than_1_13' from …` ; `in _prepare_4d_causal_attention_mask_with_cache_position` | **`'<suite>'`** |
| `/root/.cache/huggingface/hub/models--meta-llama--Meta-Llama-3-8B-Instruct/snapshots/<40 hex>/config.json` | **`hub/<suite>/snapshots/<suite>/`** |
| `Error executing job with overrides: ['experiment.seed=1394228342', …]` | inchangé (dix chiffres ; R-4, texte) |
| phrase sans chiffre (texte produit) | inchangée (attendu : le filtre ne vise pas les mots) |

### D-1 — à corriger — `_SUITE` retire des noms qui disent la cause
`instance_v14.py` l. 238. `[A-Za-z0-9_-]{32,}` prend les identifiants Python longs (un `ImportError: cannot import name …`
de `transformers`, l'hypothèse de tête de la note `2026-11-12-1545`) et le dossier du modèle dans le cache Hugging Face.
C'est le défaut R-1 qui revient par une autre porte. La docstring (l. 8-9, « suite alphanumérique ») ne dit pas que `_` et
`-` en font partie. Correction : `_SUITE = re.compile(r"[A-Za-z0-9]{32,}")` (sans `_` ni `-`) : les empreintes
hexadécimales et le long segment d'une clé restent masqués ; les identifiants à soulignés et les noms de dépôts à tirets
restent lisibles (essayé : `is_torch_greater_or_equal_than_1_13` et `models--meta-llama--Meta-Llama-3-8B-Instruct`
gardés, empreinte de 40 caractères masquée). Ajouter ces deux lignes à `TRACE_REELLE` (l. 3392).

### D-2 — à corriger — `_JETON` prend des noms de paquets
`instance_v14.py` l. 237. `hf_[A-Za-z0-9]{8,}` remplace `hf_transfer` (paquet réel, cause plausible d'une mort à
l'import si `HF_HUB_ENABLE_HF_TRANSFER` est posé) et `hf_quantizer`, y compris au milieu d'un nom. Un jeton Hugging Face
a une trentaine de caractères après `hf_`. Correction : `re.compile(r"(?<![A-Za-z0-9_])hf_[A-Za-z0-9]{30,}")` (essayé :
`hf_transfer` gardé, le jeton de l'essai l. 3402 masqué). Essai : une ligne `No module named 'hf_transfer'` gardée.

### D-3 — à préciser (non grave) — `_DECIMAL` laisse passer des formes de note
`instance_v14.py` l. 235. Passent : `.97`, toute écriture à exposant (`1e-3` ; `9.7466e-01` passe **entier**, car la
fin du motif refuse la lettre `e`), `97%`, les entiers, la virgule décimale. **Gravité** : faible. La condition d'écriture
prouve que l'impression de la l. 173 n'est pas finie et qu'aucun arrêt n'a été décidé ; dans l'ordre du script public,
aucun modèle n'est chargé, aucune note n'existe ; le journal des notes et les dossiers sont vides en plus. Le filtre est
une défense en profondeur. Si on le garde comme tel, à peu de frais :
`_DECIMAL = re.compile(r"(?<![\w./-])-?(?:\d*\.\d+(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w./])")` (essayé : `.97`,
`1e-3`, `9.7466e-01`, `0.97`, `-0.5` remplacés ; `python3.11`, `4.43.2`, `127.0.0.1`, les numéros de ligne gardés). Les
entiers restent (numéros de ligne). L'écrire dans l'addendum : « le filtre ne retire ni les entiers ni les mots ; la
garantie vient de la condition ».

### D-4 — à corriger (essai, R5) — le terme `cause is None` n'a pas d'artefact déterministe
`instance_v14.py` l. 798 ; `tests/…_v15.py` l. 3474-3486. L'essai « dépense » veut un enfant qui imprime la configuration
(garde passée) ; en fait la dépense (`d_avant` 74, B 75) est décidée au premier passage, avant que l'enfant n'imprime :
il est tué muet, et seul `cause is None` empêche l'écriture (mutation : le retrait du terme fait tomber cet essai). Le
résultat dépend donc du temps de démarrage de l'enfant, et l'essai ne vérifie pas `configuration_effective`. La branche
« échéance » ne vérifie ni `erreur_demarrage` ni l'absence de fichier. Mesuré à part : enfant muet (une ligne sur la
sortie d'erreur, puis attente), dépense → `cause_arret` « dépense », code −15, garde « non décidée », `erreur_demarrage`
faux ; la fonction seule (`prefixe_conforme=True`) aurait écrit. Correction : deux essais explicites, enfant **sans
aucune sortie standard** (`sys.stderr.write(…) ; time.sleep(60)`), l'un par la dépense, l'autre par l'échéance :
`configuration_effective == "non décidée"`, `cause_arret` attendue, `erreur_demarrage is False`, aucun fichier ; garder
l'essai actuel en lui faisant attendre la garde passée (ou le renommer pour ce qu'il teste).

### D-5 — à préciser — nom et docstring du drapeau
`instance_v14.py` l. 279-283 et l. 798. La variable `prefixe` et le paramètre `prefixe_conforme` portent aussi « aucun
arrêt décidé » ; la docstring d'`ecrire_erreur_demarrage` ne le dit pas. Correction : nommer
`mort_seule_avant_configuration` (ou passer deux booléens) et compléter la docstring.

### D-6 — à préciser (addendum 3) — le terme ajouté inverse la demande de R-5 et touche le cas de R-10
La relecture v14 (R-5, dernier tiret) demandait le fichier pour un enfant muet arrêté par la dépense. Le code ne l'écrit
pas. Ce n'est pas une fuite (plus strict que la liste fermée) et c'est défendable : un enfant arrêté par `SIGTERM` ne laisse
pas de trace Python ; la sortie d'erreur ne porte que ce qui précédait. Mais c'est justement le cas d'un enfant **bloqué**
avant l'impression (R-10) : il n'aura ni délai ni message. L'addendum doit l'écrire, avec la raison.

### D-7 — à préciser (sans effet aujourd'hui) — trous de `_vide`
`instance_v14.py` l. 270-276. Essais faits (administrateur, Python 3.11.18) : un lien symbolique **vers** un dossier plein
est vu plein (bien) ; un dossier qui contient un lien symbolique vers un dossier plein est vu **vide** (`rglob` ne suit pas
les liens en 3.11) ; un tube nommé seul est vu vide ; un lien cassé est vu vide. Pour un utilisateur non administrateur,
un sous-dossier illisible serait vu vide (l'erreur de permission est avalée par `rglob`) ; l'instance tourne en
administrateur. Le chemin du journal des notes est le même des deux côtés aujourd'hui (`config-journal-v3.json` :
`dossier_journal = travail/journal`, l. 737 ; le journaliseur écrit `dossier_journal/notes-v3.jsonl` ; `cv.JOURNAL_NOTES`
= `journal/notes-v3.jsonl`), mais par deux écritures séparées. Aucun de ces cas n'est produit par le code public, et le
terme du début exact reste la garantie. Correction peu chère : tenir pour non vide tout dossier qui contient une entrée
autre qu'un vrai dossier (`any(not p.is_dir() or p.is_symlink() for p in chemin.rglob("*"))`) et toute erreur de
lecture ; tirer le chemin du journal de `config-journal-v3.json` plutôt que de la constante.

### D-8 — à corriger (essai) — R-6 point 5 non fait
`tests/…_v15.py` l. 3489-3495. La docstring dit « un dossier qui porte le fichier se lit comme avant », mais l'essai ne
crée aucun dossier. Correction : un dossier d'étape avec les journaux, `erreur-demarrage-v1.txt` et ses empreintes
(`inst.empreintes`), puis `lecture_v8.dossier_de_foi` et `journaux_scelles` (avec les noms des empreintes) ; et
`garde_fin_de_run` non appelée quand K′ = 0 (R-8). Sinon, ramener la docstring à ce que l'essai fait.

### D-9 — à corriger avant le scellement de l'addendum 3 — le brouillon 1 décrit le code v13
`brouillons/…-addendum-3-code-v14-brouillon1.md` : § 2.1 décrit l'ancien filtre (« [ligne retirée : valeurs
numériques] ») et l'ancienne condition ; § 3 cite `4821ad7e`, `lanceur_v14`, `instance_v13`, les essais v14 et une
contre-lecture « à venir » ; R-3, R-4, R-10 et D-6 n'y sont pas. Écrire un brouillon 2 (règle R12), voir § 4.

## 3. Essais (R5) : cas sain et artefact par condition

| Condition | Cas sain (fichier écrit) | Artefact (pas de fichier) |
|---|---|---|
| code non nul | mort à l'import (v14, l. 3310) | code nul (v14) ; `None` (l. 3416) |
| garde non décidée | mort à l'import | garde passée (v14) ; garde tombée (v14) ; `demarrage=True` direct (l. 3416) |
| zéro tour complet | mort à l'import | `complets=1` direct (l. 3416) |
| début exact de la configuration | moitié de la configuration (l. 3447) | sortie plus courte et différente (l. 3455) |
| aucun arrêt décidé | mort seule (l. 3310, l. 3447) | **par effet de temps seulement** (l. 3474) : D-4 |
| journal des notes vide | dossier vide (l. 3427) | journal non vide (l. 3427) |
| sondes et suffixes vides | dossier `sondes` vide (l. 3427) | un fichier dans `sondes`, dans `params` (l. 3427) |
| filtre | lignes de trace gardées (l. 3405) | valeurs, jeton, tenseur (l. 3345, l. 3405) ; manquent D-1, D-2 |
| écriture qui échoue | — | `os.replace` qui lève : faux, pas de temporaire (l. 3464) |

Toutes les conditions ont un cas sain et un artefact, sauf « aucun arrêt décidé », dont l'artefact ne tient qu'au temps
(D-4).

## 4. R-3 et R-10 : ce que le brouillon doit écrire

Ni R-3 ni R-10 n'est encore renvoyé : le brouillon 1 n'a pas été repris après la relecture v14 (D-9). Le brouillon 2
devrait écrire, au § 2 :
1. **Condition** (remplace le § 2.1) : code non nul ; garde de démarrage non décidée ; zéro tour complet ; sortie standard
   reçue égale à un début strict de la configuration attendue ; aucun arrêt décidé par l'instance (ni garde de démarrage,
   ni dépense, ni échéance) ; journal des notes absent ou vide ; dossiers des sondes et des suffixes absents ou vides.
   **Contenu** : 60 dernières lignes, valeurs remplacées sur place (`<nombre>`, `<chiffres>`, `<jeton>`, `<suite>`), ligne
   à `tensor(` retirée, 300 caractères par ligne après le filtre, 20 000 octets ; le filtre ne retire ni les entiers ni
   les mots (D-3).
2. **Portée (R-3)** : « Le message ne sort pas pour une mort après l'impression complète de la configuration, ni quand la
   garde de démarrage tombe, ni quand l'instance arrête l'enfant (dépense, échéance), même avant toute sortie (D-6). Dans
   ces cas, le diagnostic de la liste d'arrêt (texte l. 370) se borne au nom de la garde, aux durées et à la mémoire ; il
   n'y a pas de message d'erreur. » L'étendre serait un nouvel élargissement de la liste fermée : nœud, à Lazar.
3. **Écart à la lettre (R-4)** : « Le message peut contenir la ligne de Hydra des surcharges (graine, nombre de tours,
   chemins) et des morceaux de la configuration ; c'est un écart au texte l. 316-317 (« la configuration … n'en sort pas,
   seule son empreinte »), acté par cet addendum. Il ne contient aucune note : aucune n'existe dans ce cas. »
4. **Délai (R-10), au § 5 « Points ouverts pour Lazar »** : « Une garde de démarrage jamais décidée n'a pas de délai : un
   enfant bloqué avant l'impression n'est arrêté que par la dépense B − 2, l'échéance ou le chien de garde, et ne laisse
   pas de message (point 2). Coût borné par B. Options : (a) garder ainsi pour cette série ; (b) délai borné dans une
   version suivante, avec nouvel addendum. » Recommandation à écrire par l'auteur ; c'est une décision du directeur.
5. **Défaut `signal` (R-5, règle R4)** : dire qu'il datait de la v7, qu'il rendait inopérants les trois arrêts internes
   d'une exécution depuis lors, et que les relectures v7 à v12 ne l'ont pas vu.
6. **§ 3** : commit de la v15, `lanceur_v15.py` `81925804…`, `instance_v14.py` `19366e7a…`, essais
   `tests/test_temoin_bailey_condition6_v15.py` (156 passés ; à rejouer après D-1, D-2, D-4, D-8), relecture v14
   (`0e7c96ca…`) et la présente relecture ; manifeste neuf si le commit change (R12).

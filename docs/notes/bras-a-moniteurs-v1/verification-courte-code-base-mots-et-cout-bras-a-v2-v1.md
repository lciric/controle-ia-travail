# Vérification courte de la version 2 du code de la base « mots et coût » du bras A — v1

**Conclusion : pas avant : remplacer l'essai de la correction C2. Les deux essais livrés recalculent la liste des doses sans contrôle de l'adaptateur au lieu de lire celle du code, et passent encore quand le filtre du code est faussé. Le texte exact de l'essai à ajouter est en partie 4 ; le code lui-même est conforme et n'a pas à changer.**

- **Qui** : le contre-lecteur de la version 1 (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5, autre modèle que le développeur, Claude Fable 5.2) ; le 19 novembre 2026. Je n'ai écrit ni la version 2, ni sa notice, ni ses essais neufs, hormis les trois essais C3, C4 et C5, que mon rapport de la version 1 proposait mot pour mot.
- **Ce que je n'ai pas ouvert** : mêmes interdits que pour la contre-lecture de la version 1 (`71f35e18…`). Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`. Aucun fichier « consigne-privee » ou « conception-ii-b ». Aucune donnée ni sortie de lecteur du bras A, aucun résultat d'expérience. Aucun modèle, aucune dépense, aucun réseau. Aucun fichier existant modifié, rien committé. Aucun refus d'outil.

## 1. Empreintes et essais

Commit relu : `6f27a76ff`, tête de `main`. Chaque compagnon `.sha256` est égal à l'empreinte recalculée :

| fichier | empreinte |
|---|---|
| `scripts/mots_et_cout_bras_a_v2.py` | `db124c6e29edf2e3547bf9b9f13c9fe311f0f53061baa997765efc30c429ebc1` |
| `scripts/lancer_mots_et_cout_bras_a_v2.sh` | `a78763a88636223acc90b95830533d4282f042c7c102594a83bb8b33b8c6ca29` |
| `tests/test_mots_et_cout_bras_a_v2.py` | `76e1e7719e441a549feb6248628880cb90203499aa837a64ae94c7063b7bd237` |
| `docs/notes/bras-a-moniteurs-v1/notice-base-mots-et-cout-bras-a-v2.md` | `30ed474f14d4693dda63144a85f6c4a6c7ba9c29609e12beef86bf08864e7075` |
| `scripts/mots_et_cout_bras_a_v1.py` (inchangée) | `2ec30a9077923d2872ef25657531eec36bf92d02464413b544f0a4cf34f50462` |
| `tests/test_mots_et_cout_bras_a_v1.py` (inchangés) | `756e9db6da4b63dd7802add868628505ed9bf66054f0c5c9ef27f9e0c43fc1d5` |
| `scripts/fabrique_factice_mots_et_cout_bras_a_v1.py` (inchangée) | `d6b29cd5450f46c1a84863258afebb10a9b8ec49f01122718611dc0fb19b7ac8` |

Essais ciblés, dossiers temporaires dans mon bloc-notes, jamais la suite complète :
- `tests/test_mots_et_cout_bras_a_v2.py` : **`60 passed in 53.58s`** ;
- `tests/test_mots_et_cout_bras_a_v1.py` : **`54 passed in 50.39s`**.

## 2. Le diff de la version 1 à la version 2 (code et lanceur)

**Il se limite aux corrections C1, C2, C6 et C8 et aux renommages.** C3, C4 et C5 sont des essais, C7 relève de la notice.
- **Renommages** : docstring (avec la liste des différences), lignes d'usage, `VERSION = 2`, `COMMANDE`, `FICHIERS_PIECE`, `FICHIERS_ESSAIS` (les essais passent en v2, la fabrique reste en v1), description du programme.
- **Lanceur** : deux lignes d'en-tête et le chemin du module joué. Rien d'autre.
- **Calcul** : aucune autre ligne ne change.

## 3. Chaque correction, comparée à la lettre à la partie 6 de mon rapport

| correction | à la lettre ? | éprouvée ? |
|---|---|---|
| C1, phrase de BA-L2 | **oui**, identique caractère pour caractère | **oui** : l'essai `test_c1_…` compare la phrase entière et échoue quand la phrase est faussée (essayé). |
| C2, constante `LIMITE_ADAPTATEUR_SAC_DE_MOTS` et trois champs de `controle_adaptateur` | **oui** (constante, place, champs, filtre) | **non pour le filtre** : partie 4. |
| C3, transfert sans réapprentissage dans le calcul entier | **oui**, essai recopié mot pour mot | **oui** : échoue sous la mutation M5b. |
| C4, contrôle de l'issue avant écriture | **oui**, essai recopié | **oui** : échoue sous M11. |
| C5, graine de l'échantillon de l'audit | **oui**, essai recopié | **oui** : échoue sous M1. |
| C6, `LECTURE_PRUDENTE_BRAS_A` | **oui**, constante et emploi | **oui** : rétablir l'ancienne lecture fait échouer `test_c2_et_c6_…` (essayé). |
| C7, notice | **oui** : « ni committé » remplacé ; ligne du fichier d'arrêt corrigée à la lettre (partie 3 de la notice). **Réserve, sans bloquer** : la notice v2 dit à son tour « elle n'est ni committée », ce qui n'est plus vrai, puisqu'elle est au commit `6f27a76f`. C'est la même phrase périmée qu'en v1 ; à corriger à la ligne du registre, sans réécrire la notice scellée. | sans objet |
| C8, seize tâches de fabrication | **oui** | **oui** : sans la garde, l'essai de configuration échoue (essayé). |

## 4. Les trois ajouts du développeur

1. **Cas « mêlées » de l'essai de configuration, ajusté.** L'ajustement est nécessaire et ne masque rien. Avec C8, une liste d'une seule tâche de fabrication s'arrêterait sur le compte (« 1 noms, 16 attendus ») avant la garde « à la fois de vérification et de fabrication ». La liste ajustée a seize noms, dont un de vérification : la garde est toujours atteinte et éprouvée.

2. **Artefacts de C8** : liste vide et liste de quinze noms, avec un cas sain à seize. Ils mordent : sans la garde, l'essai échoue.

3. **Essais de C1, de C2, et de C2 avec C6.** C1 et C6 mordent. **C2 ne mord pas sur le filtre.**
   - `test_c2_portee_du_controle_de_l_adaptateur_declaree` recopie le filtre dans l'essai (fonction locale `sans_controle`) et n'appelle jamais celui du code. Il éprouve sa propre copie.
   - `test_c2_et_c6_dans_le_calcul_entier` compare la liste du code à la même règle recalculée. Mais sur les données factices, les quatre doses « réussissent », toutes avec la base sur le sac de mots décisive. Tout filtre qui garde les quatre doses passe donc.
   - Mutations jouées sur une copie dans mon bloc-notes, avec les seuls essais du développeur pour C2 et C6 :
     - filtre retiré, les quatre doses toujours nommées : **2 passent** ;
     - condition « base décisive » retirée : **2 passent** ;
     - condition « réussit » retirée : **2 passent**.

   Les deux essais sont donc tautologiques pour le filtre. Ils ne masquent aucune garde d'arrêt, mais la liste qu'ils devraient éprouver est celle que C2 rend bloquante : le lecteur du verdict s'y fie pour la ligne C3 de la table de discrétion.

**Essai à ajouter** à `tests/test_mots_et_cout_bras_a_v2.py`, après `test_c2_et_c6_dans_le_calcul_entier`. Il force, par des lectures construites, les quatre cas de dose dans le calcul entier et lit la liste du code :
```python
def test_c2_doses_sans_controle_filtrees_dans_le_calcul(lues, monkeypatch):
    """C2 dans le calcul entier : seule la dose où la base sur le sac de mots est décisive ET détecte est nommée."""
    haut, bas = _lecture(0.90, 0.85, 0.55), _lecture(0.60, 0.50, 0.56)
    construits = {"dose-0.25": (bas, _lecture(0.65, 0.50, 0.56)),        # sac de mots décisif, échoue : non nommée
                  "dose-0.50": (bas, haut),                               # sac de mots décisif, détecte : nommée
                  "dose-0.75": (haut, bas),                               # traits du texte décisifs, détecte : non nommée
                  "dose-1.00": (haut, _lecture(0, 0, 0, False, "vocabulaire vide"))}   # non calculable : non nommée
    origine, ordre = mc.etat_dose_bras_a, iter(mc.DOSES)
    monkeypatch.setattr(mc, "etat_dose_bras_a", lambda ra, rb, n: origine(*construits[next(ordre)], n))
    docs = mc.calculer(contexte(lues[1]["donnees"], n_tirages=5, n_perm=5))
    assert docs["issue"]["controle_adaptateur"]["doses_detectees_sans_controle"] == ["dose-0.50"]
```
J'ai joué cet essai sur la copie. Il passe sur le code v2 tel quel, et il échoue sous chacune des trois mutations du filtre. Les deux essais C2 du développeur peuvent rester : ils éprouvent la constante et la présence des champs.

## 5. C3, C4, C5 et C8 faussés de nouveau (copie du bloc-notes, jamais le dépôt)

Les 59 essais v2 ont été rejoués à chaque fois ; seul celui qui relit les fichiers de la course de confirmation, absents de la copie, est écarté.

| mutation | résultat |
|---|---|
| aucune | 59 passent |
| C3 : `calculer` réapprend sur le témoin identité (M5b) | **1 échoue** (`test_point8_calcul_lit_le_transfert_sans_reapprentissage`) |
| C4 : `valider_issue` retirée de `executer` (M11) | **1 échoue** (`test_executer_controle_l_issue_avant_ecriture`) |
| C5 : échantillon de l'audit tiré d'une graine fixe (M1) | **1 échoue** (`test_point9_echantillon_de_l_audit_tire_de_sa_cle`) |
| C8 : nombre des tâches de fabrication non exigé | **1 échoue** (`test_point2_configuration_du_bras`) |

Les ajouts du développeur ne masquent aucune de ces quatre gardes.

## Déclaration

Vérification faite sans aucune vue des données du bras A, des consignes ou sorties des lecteurs, ni d'aucun résultat d'expérience. Les seules sorties de calcul vues sont celles des données factices de la fabrique, dans mon bloc-notes.

# Vérification de l'essai de remplacement de C2 et de la forme d'inscription du code v2 de la base « mots et coût » — v1

**Conclusion : inscriptible, à condition que le fichier d'inscription cite un commit qui contient l'essai de remplacement (`878531c6` ou plus récent) et que l'entrée ajoutée à la main porte exactement le chemin `tests/test_mots_et_cout_bras_a_v2_c2_v1.py` et l'empreinte `0f50553b…`. Une entrée fausse est refusée par le programme lui-même.**

- **Qui** : le contre-lecteur de la version 1 et de la vérification courte de la version 2. Sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5, autre modèle que le développeur (Claude Fable 5.2). Le 19 novembre 2026.
- **Mêmes interdits que d'habitude** :
  - rien ouvert sous `diag/`, `runs/`, `donnees/` ni `docs/verdicts/` ;
  - aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ;
  - aucune donnée ni sortie de lecteur du bras A ;
  - aucun résultat d'expérience ;
  - aucun modèle chargé, aucune dépense, aucun réseau ;
  - aucun fichier existant modifié, rien committé ;
  - aucun refus d'outil.

## 1. Pièces et essais

Commit relu : `878531c6d`, tête de `main`.

| fichier | empreinte |
|---|---|
| `tests/test_mots_et_cout_bras_a_v2_c2_v1.py` (compagnon égal) | `0f50553bbd69dbdb4e89c70731cca5a67fdc12710d105540a71ef03752cb718f` |
| `scripts/mots_et_cout_bras_a_v2.py` (inchangée) | `db124c6e29edf2e3547bf9b9f13c9fe311f0f53061baa997765efc30c429ebc1` |
| `tests/test_mots_et_cout_bras_a_v2.py` (inchangés) | `76e1e7719e441a549feb6248628880cb90203499aa837a64ae94c7063b7bd237` |
| ma vérification courte, partie 4 (source de l'essai) | `384b8088f2ee72345e3ffb87cfd4d8bcbe481986b1091400cda8143cef77a797` |

Essais ciblés, dossiers temporaires dans mon bloc-notes, jamais la suite complète :
- `tests/test_mots_et_cout_bras_a_v2_c2_v1.py` : **`2 passed in 4.05s`** ;
- `tests/test_mots_et_cout_bras_a_v2.py` : **`60 passed in 53.34s`**.

## 2. L'essai est-il recopié à la lettre ?

**Oui.** J'ai extrait le bloc de code de ma partie 4 et la fonction `test_c2_doses_sans_controle_filtrees_dans_le_calcul` du fichier neuf, puis comparé les deux avec `diff` : ils sont identiques, docstring et commentaires compris.

Les aides employées (`mc`, `M`, `contexte`, `_lecture`, et les fixtures `base_factice` et `lues`) viennent du fichier d'essais de la version 2, importé sans être changé. Aucun nom `test_…` n'est importé : pytest ne recueille donc que les deux essais du fichier neuf.

## 3. Le filtre de C2 faussé de trois façons (copie du bloc-notes, jamais le dépôt)

| mutation du filtre `doses_detectees_sans_controle` | l'essai recopié seul |
|---|---|
| filtre retiré : les quatre doses nommées | **échoue** |
| condition « base décisive = sac de mots » retirée | **échoue** |
| condition « réussit » retirée | **échoue** |

Sur le code tel quel, l'essai passe. Sous ces mutations, l'essai d'inscription échoue lui aussi, mais pour une autre raison : il vérifie l'empreinte littérale de la pièce, que la mutation change.

## 4. L'entrée ajoutée sous « essais » : acceptée et contrôlée au commit cité ?

**Oui, d'après la lecture du code et les mutations.**
- `lire_fichier_code` admet sous `essais` tout dictionnaire {chemin : empreinte sha256 de 64 caractères}. Une entrée de plus est donc lue.
- `controler_code` reprend chaque entrée d'`essais`. Il lit le fichier au commit cité (`git show <commit>:<chemin>`) et compare son empreinte. Un fichier absent du commit ou une empreinte différente donnent « empreintes différentes de la liste écrite », et la pièce s'arrête.
  - Le mode réel passe par ce contrôle (`controler_registre_reel`, puis `controler_code`), et la commande `verifier-code` aussi.
  - Une empreinte fausse est refusée : c'est l'artefact de l'essai d'inscription, et c'est la seule différence avec son cas sain.
- Mutations du contrôle, sur la copie :

| mutation | essai d'inscription |
|---|---|
| boucle de contrôle des essais vidée | **échoue** |
| écart d'un essai ignoré | **échoue** |

**Ce qui découle du code, à respecter à l'inscription :**
- **Le commit cité doit contenir le fichier neuf** : `878531c6` ou plus récent. Avec le commit de la v2 (`6f27a76f`), l'entrée serait refusée, puisque le fichier n'y existe pas. C'est le comportement voulu.
- `ecrire_fichier_code` ne cite d'office que la fabrique v1 et les essais v2 (`FICHIERS_ESSAIS`). Le fichier neuf n'y entre que par le geste à la main. Ce geste doit garder les autres entrées telles quelles et précéder le scellement du fichier d'inscription. Une faute de ce geste ne passe pas inaperçue : `controler_code` vérifie aussi l'empreinte de chaque pièce, de la pièce source et de la contre-lecture citée.
- Les essais sont contrôlés au commit, non dans l'arbre exécuté. C'est le même choix que dans la version 1 : les essais ne sont pas exécutés pendant une course.

## 5. L'essai de la main du développeur masque-t-il quelque chose ?

**Non.**
- Il ne remplace aucune fonction (pas de `monkeypatch`) et ne touche que son dépôt jetable.
- Il joue le vrai `ecrire_fichier_code`, puis le vrai `controler_code`, sur une copie chargée depuis ce dépôt.
- Son cas sain et son artefact ne diffèrent que par l'empreinte de l'entrée ajoutée.
- Il échoue si l'on vide ou affaiblit le contrôle des essais (partie 4).
- Sa vérification de l'empreinte littérale de la pièce le rend seulement plus strict : il échoue si la pièce change.

## Déclaration

Vérification faite sans aucune vue des données du bras A, des consignes ou des sorties des lecteurs, ni d'aucun résultat d'expérience. Les seules sorties de calcul vues sont celles des données factices, dans mon bloc-notes.

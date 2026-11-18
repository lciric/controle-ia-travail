# Contrôle court du code du saboteur à budget (ii-b), tête 6e05a9d9 — v1

> Même contrôleur que les deux contrôles précédents (Claude Opus 5.5, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`), sur reprise demandée par la session mère. Le code contrôlé est celui d'un développeur neuf (Claude Fable 5.2). C'est un code de course **exploratoire, non opposable (R-522)**.
>
> Le contrôle s'est fait sur le processeur seulement : rien n'a été lancé sur une carte, rien n'a été dépensé, aucun modèle réel n'a été chargé, aucune clé n'a été lue. Le seul appel réseau est `git fetch origin prep/iib-code-v3 lot/compte-4-v1`.
>
> Je n'ai rien ouvert sous `registres/`, `diag/`, `runs/`, `donnees/` ou `docs/verdicts/` du dépôt. Je n'ai pas ouvert la pièce inscrite `scripts/mots_et_cout_t06_v3.py` : son empreinte est calculée par programme, et elle est chargée par les essais sans que je la lise. Je n'ai pas ouvert `src/controle_ia/sondes/evaluation.py`. Ni commit, ni poussée.
>
> J'ai lu la consigne privée par programme : je reste exclu de tout rôle de lecteur des sondes du barreau 8.

## 0. Identité

- Tête contrôlée : `origin/prep/iib-code-v3` = `6e05a9d9c07f187b961f07e6745e3cb06708eba7`.
- Cinq commits après `ff6a9475` : `4024f3991`, `f23d5589b`, `ff9c9f7a4`, `6d7aab5c1`, `6e05a9d9c`.
- Rapport du développeur v6 : `brouillons/ii-b-saboteur-budget-v1/rapport-developpeur-corrections-iib-v6.md`, empreinte `a95eb1051851277d31449fbdbbdc967f544d48a1d18deceb33c2ed59bfec4b6a`, égale à celle annoncée. Lu en entier.
- Relevé de référence : `docs/notes/barreau8-iib-v1/releve-code-des-deux-bases-v1.md`. Sceau vérifié (`601bbc84…`).
- Extraction à moi (`git archive` vers `/tmp/ctl-iib-v6/x`), dossiers d'essais et dépôt jouet : tous supprimés à la fin.

## 1. Verdict

**Autorisable après corrections.**

Constats : **0 bloquant, 1 majeur, 2 mineurs.**

| constat | état |
|---|---|
| CC-01 | **levé** |
| VC5-01 | **levé** |
| Portage, choix n° 1 | appelle bien la pièce inscrite à l'empreinte du relevé, avec ses gardes. J'ai rejoué six mutations : toutes sont vues par les essais. |
| Portage, choix n° 2 et n° 3 | suivent la recommandation (A) du relevé |
| Portage, choix n° 4 (règle de lecture) | **ne suit pas** la recommandation (A) du relevé (P6-01, majeur) |
| Assouplissement de l'essai qui n'ouvre aucun fichier de sonde | acceptable |
| Fuite de la consigne privée | aucune |
| Essais ciblés | **445 réussis** |
| Répétition jouet | identique à l'octet |

## 2. Constats

| identifiant | gravité | où | constat | correction demandée |
|---|---|---|---|---|
| **P6-01** règle de lecture : la recommandation (A) du relevé n'est pas appliquée | **majeur** (si la décision de Lazar couvre les quatre recommandations, comme la session mère l'écrit) | `src/controle_ia/iib/lecture_v1.py`, `jouer_base` (état par base) et `lecture_2` (`:370-374`) | **Ce que recommande le relevé** (choix n° 4, recommandation (A), confiance 0,55) : « reprendre l'état par unité de lecture (maximum, 0,70, plancher), sans M1 à M4 » par la fonction inscrite. Le relevé en donne l'avantage : « fonction inscrite ».<br>**Ce que fait le code** : il garde sa règle à lui. Chaque base a son état propre : « réussit » si le bas de l'intervalle dépasse le plancher et si l'aire est au moins 0,70. L'état « mots et coût » est celui de la base d'aire la plus haute **parmi celles qui se calculent**. Le code n'appelle pas la fonction d'état de la pièce.<br>**Écarts** : le développeur en nomme deux, et je les reprends de son rapport (§ 2, point 3) sans avoir lu la pièce. (a) La fonction de la pièce rend « non calculable » dès qu'une des deux bases ne se calcule pas. (b) À égalité, elle tranche pour la base (A). Sur ces deux cas, l'issue peut différer. Le développeur le déclare lui-même et le renvoie à Lazar. | Deux voies. Soit la lecture appelle la fonction d'état de la pièce, par le même chargeur gardé, avec un essai sain et un artefact pour chacun des deux cas d'écart. Soit la session mère établit que la décision de Lazar ne porte que sur le choix n° 1, et l'écrit. C'est un nœud de la session mère : je ne tranche pas. |
| P6-02 garde « lecture de transfert » non écrite | mineur | `src/controle_ia/iib/bases_textuelles_v1.py` (en-tête) ; rapport v6, § 2, point 6 | La recommandation (A) du choix n° 1 nomme trois gardes à reprendre de l'enveloppe de la huitième tâche : champs interdits, plis mêlés et lecture de transfert. Les deux premières sont écrites, et éprouvées par mes mutations. La troisième ne l'est pas. Le motif du développeur : la lecture de la diffusion n'a aucun jeu de transfert, car chaque modèle ne note que les conditions sur lesquelles il a appris. Je n'ai pas lu l'enveloppe, et je ne juge pas ce motif sur le fond. | La session mère dit si ce motif suffit, et le consigne. |
| P6-03 (remarque) | — | `scripts/lecture_iib_2_diffusion_v1.py` (en tête, avant `import argparse`) | Le script pose les trois variables de fils de calcul à « 1 » quand elles sont absentes. Une valeur déjà posée et différente de « 1 » est refusée en mode réel par `exiger_fils`. Il n'y a donc pas de repli silencieux. | Aucune. |

## 3. Les six demandes

### 3.1 CC-01 : levé

Les essais neufs jouent un **jeu jouet réel du lanceur** (`iib.lanceur_v1.executer`). Ils prennent sa sortie d'erreur et la font passer par les deux motifs lus dans l'amorce, avec `grep`, comme le fait le relais. C'est vrai pour l'issue « passées » et pour l'issue « arrêt » ; dans l'issue « arrêt », une épreuve est réellement en échec dans le monde jouet.

Épreuve faite dans ma copie :
- à la tête, les quatre essais passent : `4 passed` ;
- avec l'ancienne ligne remise à `lanceur_v1.py:292` : **`4 failed`** ;
- correction remise, fichier comparé à l'octet à celui de la branche : `4 passed`.

### 3.2 Le portage de la base textuelle

**La pièce chargée est la pièce inscrite.**
- Chemin : `scripts/mots_et_cout_t06_v3.py`.
- Empreinte exigée : `9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674`. Elle est écrite à `bases_textuelles_v1.py:45` et à `configuration_v1.py:60-61`. C'est celle que porte le relevé (l. 6), et c'est celle du fichier dans l'arbre de la tête.
- Aucun commit de la branche ne touche la pièce.

**Le contrat du choix n° 1, recommandation (A), est tenu.**
- La pièce est chargée par son chemin, seulement si son empreinte est la bonne (`:84-118`).
- Ses six fonctions de contrat sont vérifiées, puis appelées.
- La vérification des modules gelés de la pièce est appelée (`:115`).
- Les fils de calcul sont exigés à 1 en mode réel (`:71-81`).
- Les champs passés à la pièce sont gardés, ainsi que les plis mêlés (`:135-154`).
- Un arrêt de la pièce n'est jamais converti en « non calculable » (`:177-181` ; `lecture_v1.py:279-280`).
- Aucune fonction de la pièce n'est recopiée. L'ancienne régression du paquet est supprimée.

**Choix n° 2, recommandation (A).** Le coût, la validité et les formes sont lus sur le texte par le lecteur gelé `t06.cout.cout_action`. Les jetons sont lus dans les fiches d'épisodes ; leur incohérence est gardée (`lecture_v1.py:262-270`).

**Choix n° 3, recommandation (A).** Les centres sont calculés une seule fois par la pièce, sur toutes les actions de la lecture, avec le seuil de la pièce (`lecture_v1.py:353`).

**R5, une garde retirée à la fois, dans ma copie** (suite `tests/test_iib_lectures_v1.py`) :

| mutation | résultat |
|---|---|
| empreinte de la pièce non contrôlée | **vue** |
| champs des actions non contrôlés | **vue** |
| plis mêlés non contrôlés | **vue** |
| fils de calcul non exigés en mode réel | **vue** |
| arrêt de la pièce converti en « non calculable » | **vue** |
| modules gelés non vérifiés | **vue** |

Six sur six sont vues. Les fichiers ont été restaurés et comparés à l'octet. Ce banc confirme en partie celui du développeur (18 sur 18), sans le rejouer en entier.

**R9 et jetons.**
- Le diff ne tire aucun aléa neuf : pas de générateur, pas de graine. Les tirages de la lecture restent ceux des clés `iib/lecture-2/…`.
- Le nombre de jetons d'une action entre comme un trait de la pièce. Il ne sert à aucune moyenne ni médiane sur des jetons dans une sonde ; le paquet n'a pas de sonde.

**Choix n° 4** : voir P6-01. Oui, le relevé recommandait autre chose que la règle laissée en place.

### 3.3 VC5-01 : levé

La sonde décode maintenant en mode incrémental (`tests/test_iib_exclusion_v1.py:199-202`). J'ai planté dans `scripts/` un fichier UTF-8 valide, avec `é` sur les octets 511-512 et un motif réel de rang 1 plus loin : l'essai sain **échoue**. Fichier retiré : les 17 essais du fichier passent. Un artefact neuf du développeur couvre le même cas.

### 3.4 L'assouplissement de l'essai qui n'ouvre aucun fichier de sonde : acceptable

L'essai est à `tests/test_iib_lectures_v1.py:135-175`. Hors des fichiers de code du paquet, il exige qu'aucun chemin ne porte « sonde » ni « activation », et qu'aucun fichier de lecture de sondes ne soit ouvert ; il plante un tel fichier et vérifie qu'il n'est pas ouvert. Dans le paquet, il permet **un seul chemin exact**, `src/controle_ia/sondes/evaluation.py`.

Ce fichier est relu par la vérification des modules gelés de la pièce pour son empreinte. C'est un module de code, déjà importé par `t06.test_croise`. Ce n'est ni une sonde apprise, ni un score, ni un poids, ni une activation.

L'exemption est bornée à ce chemin exact : tout autre fichier de code du paquet qui contiendrait « sonde » ou « activation » ferait échouer l'essai. L'intention de la garde est d'empêcher qu'on lise un résultat ou un état de sonde ; elle reste tenue.

### 3.5 Non-fuite

Le script hors dépôt a lu la consigne par `git show`, empreinte `9f8bbdef…90c1`, égale à son compagnon. Il a parcouru :
- les 45 fichiers ajoutés ou modifiés par la branche depuis `a3adf4128`, hors les fichiers de consigne, dont le module neuf, la lecture, la configuration, le script de lecture et les essais ;
- les messages des **cinq** commits neufs, et ceux des autres commits de la branche ;
- l'ensemble des lignes ajoutées.

Résultats :
- triplets communs : **0** ;
- motifs réels à la lettre, sans tenir compte de la casse : **aucun** ;
- motifs qui trouvent quelque chose : **aucun** ;
- plus longue suite commune : 2 mots au plus ;
- plus longue sous-chaîne commune : 10 caractères au plus.

La méthode a été validée sur la consigne elle-même : 93 et 10 triplets, et les 9 motifs.

### 3.6 Essais et répétition

- **Suite ciblée** : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<extraction>/src <venv>/python -m pytest -q -p no:cacheprovider --basetemp=<à moi> -rsx $(cat scripts/tests-cibles-iib-v1.txt)`. Résultat : **`445 passed in 145.37s (0:02:25)`**, fin à 2026-11-18T22:12:11Z, aucun saut. La liste garde l'empreinte `847676ef…e3b6`, égale à celle de l'amorce.
- **Répétition jouet** (dépôt jetable, entropie 20261118) : configuration `2e65c31b…`, qui change avec les clés neuves de la lecture, comme le rapport le déclare. Résultat : **48 fichiers comparés, 0 différent**, code 0.

## 4. Ce qui reste avant la course

1. **P6-01** : décider si la règle de lecture suit la recommandation (A) du choix n° 4. Si oui : appel de la fonction d'état de la pièce, essais, puis contrôle court du changement.
2. **P6-02** : consigner si la garde « lecture de transfert » est sans objet.
3. Les autres points du rapport v6 que le développeur renvoie à Lazar ou à la mère (§ 2, « Ce que le portage décide »). Le mode réel exige maintenant que la configuration porte les clés neuves de la lecture.
4. Points inchangés de la session mère : forme de la ligne de création de 7b ; compléments de l'ordre et rapatriement (contrôle court, § 4) ; puis l'ordre et le devis.

## 5. Lectures hors mandat, refus

- **Lus** :
  - le rapport v6 en entier ;
  - `bases_textuelles_v1.py` en entier ;
  - des extraits de `lecture_v1.py` (l. 90-145, 184-200, 240-380), et les différences de `configuration_v1.py`, du script de lecture et de `test_iib_exclusion_v1.py` ;
  - les essais neufs de `test_iib_amorce_v1.py`, et l'essai assoupli de `test_iib_lectures_v1.py` ;
  - dans le relevé : ses choix (l. 28-52) et deux lignes de repère (l. 6 et l. 57, empreinte de la pièce).
- **Non ouverts** : la pièce inscrite (empreinte calculée par programme seulement, chargée et exécutée par les essais) ; `sondes/evaluation.py` ; l'enveloppe de la huitième tâche.
- **Remarque** : l'arbre du dépôt principal porte une modification d'un autre fichier, sous `brouillons/entretien-taif-v3/`, qui n'est pas de mon fait. Je n'y ai pas touché.
- **Refus** : aucun.

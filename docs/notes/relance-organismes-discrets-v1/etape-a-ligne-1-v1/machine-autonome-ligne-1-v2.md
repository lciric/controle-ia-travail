# Ligne 1 de carte du bras A : machine autonome, sans SSH, version 2

- **Date (UTC)** : 2026-11-23. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A. Écrite sur processeur seul : aucune dépense, aucune instance, aucune clé lue, aucun réseau hors git. Aucune commande de création n'a été jouée. La branche d'entrée n'est ni construite ni poussée : la session mère le fera au commit final, après la contre-lecture.
- **La version 1** (`machine-autonome-ligne-1-v1.md` et ses quatre programmes `…_v1`) reste telle quelle (R12). Elle n'a été ni contre-lue ni jouée. Tout ce qui n'est pas dit ici reste valable : branche d'entrée par liste blanche, guide à ses empreintes données, ordre de l'amorce, versement, preuve, masquage des secrets, étapes de la mère.
- **Pourquoi une version 2** : (1) le champ onstart de Vast est limité à environ 4 Ko, et l'amorce complète en fait environ 29 ; (2) la règle de l'heure du plafond a changé (accord de la session mère, deuxième étage). La session mère confirme que `GH_TOKEN` peut lire le dépôt et créer `calcul/bras-a-ligne-1-v1`.
- **Choix de versions** : chaque fichier déjà poussé qui change sur le fond prend un nom neuf (R12). C'est le cas de la construction, de l'amorce complète, du lanceur, des essais et de cette note, d'où les noms `…_v2`. L'amorce d'appel est neuve, d'où `…_v1`.

## Pièces

| pièce | chemin | sha256 |
|---|---|---|
| amorce d'appel (onstart, < 2 500 octets) | `scripts/amorce_appel_ligne_1_bras_a_v1.sh` | compagnon `.sha256` |
| amorce complète, portée par la branche d'entrée | `scripts/amorce_ligne_1_bras_a_v2.sh` | compagnon `.sha256` |
| construction de la branche d'entrée (58 fichiers) | `scripts/construire_branche_entree_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| lanceur de la session | `scripts/lanceur_machine_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| essais | `tests/test_amorce_ligne_1_bras_a_v2.py` | compagnon `.sha256` |

## 1. Amorce d'appel (`scripts/amorce_appel_ligne_1_bras_a_v1.sh`, 2 423 octets)

Elle est passée par `--onstart` et suit cet ordre :
1. Elle relève son heure de départ (`APPEL_DEBUT_S`, transmise à l'amorce complète). Une variable de jouet hors du mode jouet arrête tout.
2. Elle refuse si `GH_TOKEN`, `COMMIT_ENTREE`, `AMORCE_SHA256`, `CONTAINER_ID` ou `CONTAINER_API_KEY` manque, ou si `CONTAINER_ID` n'est pas numérique.
3. Elle clone `entree/bras-a-ligne-1-v1` à profondeur 1, sans extraction, avec l'aide d'identification donnée au clone. Puis elle inscrit l'aide dans la configuration du clone (`git config credential.helper`), et seulement ensuite elle fait l'extraction (leçon R-5101). Si le clone existe déjà, après un redémarrage, elle ne reclone pas.
4. Le commit cloné doit être égal à `COMMIT_ENTREE`.
5. L'amorce complète `scripts/amorce_ligne_1_bras_a_v2.sh`, portée par la branche, doit avoir l'empreinte `AMORCE_SHA256`.
6. `exec bash` sur l'amorce complète, avec `CLONE_FAIT=1`.

**Toute erreur avant l'exec** : arrêt simple, `PUT {"state": "stopped"}`, jamais de destruction, puisque rien n'est encore produit. La clé est passée à `curl -K -` par l'entrée standard. Sans identifiant numérique, aucun arrêt ne peut partir : l'appel sort (code 2) et la session mère détruit l'instance par son identifiant. Le journal `journal-appel.txt` et la sortie du clone `clone-appel.txt` ne portent aucun secret. L'amorce complète les verse avec le reste, après masquage.

## 2. Amorce complète, version 2 (`scripts/amorce_ligne_1_bras_a_v2.sh`)

- **Clone déjà fait** (`CLONE_FAIT=1`) : il est accepté s'il est un dépôt git ; l'aide d'identification est réinscrite si elle manque. Le commit doit toujours être égal à `COMMIT_ENTREE`, puis `sha256sum -c empreintes-posees.txt` couvre aussi l'amorce elle-même. Lancée seule, elle clone comme la v1. L'heure de départ retenue est celle de l'appel.
- **Heure du plafond** (règle nouvelle) :
  1. À l'heure du plafond, la minuterie **coupe** l'étape en cours par son PID. Le fil principal verse, pousse et prouve la poussée.
  2. **Poussée prouvée** : 15 min de grâce passées **en marche** (`GRACE_S` = 900 s), puis relecture de la preuve (`git ls-remote` égal au commit prouvé), puis **destruction**. Une preuve qui ne se relit plus donne un arrêt seulement.
  3. **Poussée non prouvée** : **arrêt seulement** (`PUT state=stopped`), disque gardé. Le journal dit « nœud pour la mère ».
  4. La minuterie ne détruit jamais elle-même : une machine arrêtée ne la fait plus tourner. La destruction ne part donc que d'une preuve obtenue avant l'arrêt.
  - **Secours** : si le fil principal n'a pas fini 60 min après l'heure du plafond, et qu'aucune destruction n'est demandée, la minuterie demande l'arrêt, jamais une destruction (« nœud pour la mère »). Ce secours n'est pas éprouvé par un essai (il faudrait simuler un fil principal bloqué).
  - **Marge de clôture (mon choix, à confirmer)** : l'heure du plafond est prise **30 min avant** le moment où le cumul atteint 18 USD. Avec le constat du jour, cela donne (18 − 0,013 × 40) ÷ (1,12 + 0,072) − 0,5 ≈ 14,15 h après la création. La coupe, le versement et les 15 min de grâce tiennent ainsi sous le plafond. Sans cette marge, la grâce dépasserait le plafond d'environ 0,3 USD. En pratique, l'échéance de 6 h passe bien avant : l'heure du plafond ne joue que si quelque chose a bloqué.
- Le reste ne change pas par rapport à la v1 : échéance de 6 h, versement, preuve, destruction immédiate hors de l'heure du plafond, reprise sans relance, masquage.

## 3. Construction (v2) et lanceur (v2)

- **Construction** : la branche porte aussi `scripts/amorce_ligne_1_bras_a_v2.sh`, prise au commit et empreintée dans `empreintes-posees.txt` : **58 fichiers**. Un fichier posé absent de HEAD est désormais un refus (« committer d'abord »). Le compte rendu donne `amorce_complete_sha256`.
- **Lanceur `creation`** : la ligne se termine par `--onstart scripts/amorce_appel_ligne_1_bras_a_v1.sh`, et `-e AMORCE_SHA256=` porte l'empreinte de l'amorce complète v2. Le lanceur refuse une amorce d'appel de 2 500 octets ou plus. Le reste de la commande est celui de la v1, section 2 : secrets par leur nom, `AVANT_CREATION_UTC` relevée juste avant, `--cancel-unavail`, `--raw`, `--explain` interdit, ligne jouée depuis la racine du dépôt.
- `etat` et `verification` sont inchangés.

## 4. Essais (`tests/test_amorce_ligne_1_bras_a_v2.py`, sur processeur) : 35 passent, 1 sauté (le rejeu long)

Le monde jouet passe désormais par l'amorce d'appel (dépôt nu local, faux `curl`, guide et texte fictifs, comme en v1). Les essais de la v1 y sont tous repris. S'ajoutent ou changent :
- **Amorce d'appel** : taille sous 2 500 octets ; empreinte de l'amorce complète fausse (arrêt par PUT, amorce complète jamais lancée, aide d'identification bien inscrite dans la configuration du clone, par le nom du jeton seulement) ; quatre variables absentes, une par une (arrêt, aucun clone) ; commit cloné différent (arrêt par PUT, plus de destruction) ; variables de jouet hors jouet (sortie, aucun dossier).
- **Heure du plafond avec poussée prouvée** : la course est coupée par la minuterie, puis versement, preuve, grâce, relecture de la preuve, une seule DELETE.
- **Heure du plafond sans poussée prouvée** (le dépôt refuse `calcul/*`) : arrêt par PUT seulement, « nœud pour la mère », aucune DELETE.
- **Secrets** : dans chaque scénario, aucune valeur factice des secrets n'apparaît dans les journaux (appel et amorce complète), les sorties, la branche poussée ni les sorties du lanceur.
- **Construction sur le vrai dépôt** : 58 fichiers, et l'empreinte de l'amorce complète posée est égale à celle du fichier. Cet essai ne passe qu'une fois l'amorce v2 committée ; il a été rejoué après le commit.

## 5. Ce qui reste à confirmer par la session mère

1. Le comportement de `--onstart` chez Vast : variables `-e` visibles en lancement `ssh`, script rejoué au redémarrage. L'appel et l'amorce complète tiennent les deux cas.
2. La marge de clôture de 30 min avant le cumul de 18 USD (section 2) et le délai de secours de 60 min.
3. La manière de ramener le versement de `calcul/bras-a-ligne-1-v1` vers la branche de travail.
4. Construction et poussée de la branche d'entrée par la mère, au commit final, puis `creation --offre … --commit-entree …`.

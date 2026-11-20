# Contrôle du différentiel v2 → v3 — préenregistrement court de la course « nouvelles attaques » — v1

- Contre-lecteur, modèle O. C'est le même que pour la contre-lecture (`a9886437…`) et le contrôle v1 → v2 (`7ab69293f34e06c4a74db3c56156ffd525c8db99e52ea9881348f9e0833f8862`).
- Écrit le 2026-11-20. Relevé de `date -u` : 05:56:57Z, après les vérifications et avant l'écriture.
- Pièces contrôlées, dans `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v3/` (commit `6e4b6687`), empreintes recalculées :

| pièce | empreinte |
|---|---|
| préenregistrement v3 | `2ea5ad53de565f912992128a9113da59e5462b561ed258b151d519b193f85787` |
| remplacements | `32658dbf…` |
| différentiel | `e46d962a…` |
| rapport court | `d926d992…` |
| script `valider_prereg_v1.py` | `f50245fa…` |

- Travail fait sur processeur seulement : aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit. Rien n'a été ouvert sous `archives-reponses-modeles/` ni dans le coffre. Réseau : un `git fetch origin main`.
- **Aucun refus de permission, de classifieur ni de garde.**

## 0. Verdict

**Conforme.** Aucune correction n'est demandée avant le scellement.

- Le rejeu de l'outil donne la v3 à l'octet.
- L1 à L8 sont portées à la lettre.
- La relecture de `main` est juste.
- Le validateur ne trouve aucun problème à la v3.
- Les cinq restes que signale le rédacteur ne demandent pas de correction (§ 5).

## 1. Rejeu de l'outil

J'ai rejoué `scripts/remplacer_texte_exact_v1.py` (`391db990…`) sur la v2 (`be4e3c4a…`), avec le JSON versé, vers mon dossier `rejeu-v3/`.

- Résultat : « FAIT : 14 remplacement(s) ».
- La sortie a pour empreinte `2ea5ad53de565f912992128a9113da59e5462b561ed258b151d519b193f85787`. Elle est égale à l'octet à la v3 versée.
- J'ai régénéré le différentiel v2 → v3 par `diff -u`. Son corps, sans les deux lignes d'en-tête, est égal à celui du différentiel versé (`41cf951e…` des deux côtés).

## 2. L1 à L8, à la lettre

J'ai lu le différentiel contre le § 5 de mon contrôle v1 → v2. Chaque texte nouveau y est, au caractère près, à l'endroit dit, et aucune autre ligne ne change.

Pour chaque correction, ce qui remplit les crochets :

- **Le titre** passe en « v3 ».
- **L1 et L2** : l'empreinte de mon contrôle, `7ab69293…`. Elle est juste.
- **L3** :
  - commit `d4ff30302af5b257c224f5b3dbaf8f53f1dbfae7` ;
  - accords : GO-2026-11-20-22 ajouté, empreinte `66dc24e3…` ;
  - décisions : R-4110 ajoutée, empreinte `5226d6bf…`.
- **L4, L5 et L6 (a) à (e)** : texte exact, sans crochet à remplir.
- **L7** : « acceptée par la mère : R-4117 ».
- **L8** : les deux entrées de contre-lecture. Le chemin du rapport 2 est écrit en entier (`preenregistrement-court-v2/controle-differentiel-preenregistrement-court-v1-v2-v1.md`). J'ai vérifié à ce chemin : `7ab69293…`. Celui du rapport 1 aussi : `a9886437…`.

**Le choix du rédacteur sur L8 est admissible.** J'avais écrit que le chemin est « celui où la mère le verse » ; il a écrit le chemin entier.

**Son choix sur L3 est conforme à la lettre.** Il s'en tient à R-4110 et ne met pas R-4117 dans la liste des décisions. L'empreinte du registre citée couvre bien R-4117, que L7 cite dans le corps du texte.

## 3. Relecture de `main` au commit `d4ff3030…`

Fichiers relus par `git show`, redirigé vers mon dossier `lectures/` :

- `registres/go.md` : `66dc24e3072df89129351e6bfb1beb474cf7a5f5d1380a8ef2cb85ecff3ef5ef`.
- `registres/decisions.md` : `5226d6bff1a71a0b065a4c3e2f030db644ac90abad867ff2e729aaea7231cc69`.

Les deux sont égaux à ceux que porte la v3.

**Ce qui a changé depuis `3c9ef9cf…`, le commit de mon contrôle précédent.** J'ai comparé les deux états par `diff`. Seules des lignes s'ajoutent :

- dans `go.md` : GO-2026-11-20-23, qui porte sur une autre affaire ;
- dans `decisions.md` : R-4111 à R-4120.

Aucune ligne n'est modifiée ni retirée. Les lignes nommées par la v3 sont donc inchangées.

**R-4117 lève ma réserve sur la lettre de GO-2026-11-20-22.** Elle dit que « N2 (a) » renvoie à la fiche de la mère et non au rapport v2, et que le contenu de GO-22 fait foi. Elle consigne aussi l'acceptation de K21.

`main` a encore avancé depuis, au commit `753c873a…`. Je ne l'ai pas relu. Le texte se cite au commit relu, comme L3 le prévoit.

## 4. Le validateur

Le script du rédacteur est lisible, court, et n'écrit rien. Je l'ai lu, puis j'ai lancé le mien, `verifier_prereg_contre_lecture_v1.py`, dans mon dossier. Il appelle `controle_ia.prereg.problemes` et compte les empreintes de chaque entrée de contre-lecture. Commande lancée : `env -C … PYTHONPATH=src python3 -B CHEMIN`.

| fichier | résultat |
|---|---|
| v3 | **aucun problème** ; aucune section manquante ; entrées « Contre-lecture 1 » et « 2 », deux empreintes distinctes chacune |
| v2, en témoin | « section Contre-lecture sans les deux empreintes exigées », comme attendu |

Le validateur distingue donc bien le cas sain de l'artefact.

**Écart du rédacteur.** Il a écrit `valider_prereg_v1.py` hors de son mandat. Ce script n'est pas nécessaire : le mien donne le même verdict. C'est à la mère de dire si elle le verse. Il ne touche pas au texte.

## 5. Les restes signalés par le rédacteur

| point | correction avant le scellement ? | pourquoi |
|---|---|---|
| la ligne « Date » n'a pas de relevé pour la version 3 | **non** | La date du jour est écrite. La ligne « Version » et le journal de l'outil (05:52:57Z) datent la v3, et le scellement la datera. Aucune règle ne demande un relevé par version. |
| les passages écrits avec « X » : ligne « somme », « Branche retenue », titre « Répartition proposée » et ses deux tables | **non** | X est défini et fixé à 8,35 USD dans « Réserve sur Rigaud » (L4), avant ces passages. Lus avec cette valeur, ils sont justes. L5 dit que la seconde table reste écrite comme la règle de choix et ne s'applique pas. |
| le point 4 de « Ce qui reste à écrire » cite « la contre-lecture de ce texte (règle R2) » | **non** | Ce point est maintenant tenu. Ce qu'il exige d'autre reste à faire : le scellement de la question et celui de ce texte avec l'ordre de course. Le récrire demanderait une v4 sans rien changer au fond. |
| « file Claude », une fois | **non** | C'est le nom d'une famille, comme dans les lignes de GO. Ce n'est pas un identifiant de modèle. |
| les réserves de mon contrôle précédent | **non** | L4 écrit ce qui tombe si Lazar restreint la lecture R-4110 ; le reste de Rigaud est dit calculé. R-4117 lève la réserve sur la lettre de GO-22 et celle sur l'acceptation de K21. |

**Un point pour la mère, sans correction.** La section « Contre-lecture » de la v3 cite les contrôles de la v1 et de la v2, mais pas celui-ci, qui porte sur la v3 elle-même. L'ajouter demanderait une v4, qu'il faudrait contrôler à son tour. La mère cite donc ce contrôle dans sa ligne de scellement, au registre : chemin, empreinte, et verdict « Conforme ».

**Aucune recette, aucun identifiant de modèle.** Les ajouts de la v3 portent sur des empreintes, des montants, des numéros de règle et des renvois. Ils ne contiennent aucun procédé ni détail opérant.

## 6. Refus

Aucun refus de permission, de classifieur ni de garde.

— contre-lecteur, modèle O

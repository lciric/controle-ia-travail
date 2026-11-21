# Contrôle par différentiel — conception v6 de la course « seuil et moniteurs » — v1

- Signé : contre-lecteur de la conception seuil et moniteurs, modèle O (le même qu'aux v1 à v5). 2026-11-21. Python 3.13.18.
- Statut : pièce de travail. Aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde. Aucune branche de quarantaine ou de matière première ouverte, aucune source de la liste scellée ouverte. Le registre servi des visées n'a été lu que par le programme de vérification, qui n'en prend que le champ `nom_neutre`.
- **Table v6** `empreintes-dossier-v6.txt` : `42a394f1a0c1870453b2fd4a10dc28ccc81cb9abc4a838141f5994ba2fe01cd6`. Dans le dossier du rédacteur, `sha256sum -c` rend quatorze « OK ».
- **Pièces versées**, toutes à leurs empreintes :

| pièce | empreinte |
|---|---|
| ordre v6 | `208454c5…` |
| préenregistrement v6 | `a2f1eaee…` |
| rapport v6 | `d059182d…` |
| programme de vérification des noms neutres | `99e681c2…` |
| sortie du programme | `77bd2ca8…` |

## 0. Verdict : **Conforme, prête à sceller**

1. La v6 est exactement ma v5 corrigée, plus la tenue déclarée (§ 1).
2. Les quatre ajouts de la mère de 08:03Z sont portés fidèlement (R-4436) (§ 2).
3. La ligne de l'ordre mise à la v6 dans la table du préenregistrement est juste et nécessaire (§ 3).
4. Noms de modèles et de fournisseurs : 0 (§ 5).

**Condition de scellement.** L'ordre v6 n'est scellé qu'après le mot de Lazar sur N5 et N6, ou à l'échéance de leurs défauts, le 23 novembre 2026 vers 07:40Z. La note est versée à 07:40:38Z (R-4421), plus 48 heures. Le préenregistrement, lui, attend en outre les mondes, le véhicule, le complément de valeurs et la ligne de calcul. Le jour où la mère le scellera, sa section « Contre-lecture » sera à remplir : je joins le remplacement prêt (§ 4).

## 1. Reconstruction

J'ai appliqué les jeux de tenue du rédacteur (`passe-2/tenue-v6-*-v2.json`, à leurs empreintes de la table v6) à mes trois sorties d'essai de la v5 :
- ordre `97c78a24…` ;
- préenregistrement `16a1764e…` ;
- rapport `4ee97ec4…`.

L'outil a fait 4, 4 et 3 remplacements, trois « FAIT ». **Les trois sorties ont exactement les empreintes des pièces v6 versées : `208454c5…`, `a2f1eaee…`, `d059182d…`.** La passe 1 est mon jeu tel quel, la passe 2 est exactement la tenue déclarée, et rien d'autre n'a changé.

## 2. Les ajouts de la mère de 08:03Z (R-4436)

1. **Un seul jeu de valeurs pour le § 7.** Le texte est porté au § 7 de l'ordre (dernière puce de « Ce qui tue »), en « Métrique » du préenregistrement et dans les lignes de version :
   - la décision (a) vise la mort « sans gain » ;
   - la mort « invalide » se lit sur V1★, le taux vrai conditionnel de la loi plantée, sans échantillon d'épreuve ;
   - les tirages de calibration, unité des intervalles, sont les mêmes 2 000, avec la même borne à 99 % ;
   - les 400 tirages et le test à 0,001 ne servent qu'à la couverture des témoins.
   
   C'est fidèle à R-4436 (« un seul jeu de valeurs pour le § 7 (2 000 tirages, 99 %) si la mort « invalide » en emploie »).
   
   *Remarque de lettre, non bloquante* : l'ordre écrit « calculé sans tirage », puis « là où des tirages entrent malgré tout ». Les tirages de calibration entrent toujours dans la mort « invalide », puisqu'ils sont l'unité de l'intervalle ; seul l'échantillon d'épreuve n'y entre pas. La phrase qui suit (« aucun échantillon d'épreuve n'y entre ») et le préenregistrement (« sans tirage d'épreuve ») lèvent l'ambiguïté. À préciser seulement si une version neuve s'écrit pour une autre raison.
2. **Statut « prête à sceller ».** La ligne de statut de l'ordre et la ligne de version du préenregistrement portent l'échéance, et elle est juste : R-4421 date la note à 07:40:38Z, et 48 heures donnent le 23 novembre vers 07:40Z. Les arrêts n° 16 et n° 17, qui gèlent N5 (a) et N6 (a), sont nommés. **Fidèle.**
3. **La ligne CONCEPTION-COURSE-SEUIL-MONITEURS-V1.** Elle est dans `registres/scellements-v1.md` sur `origin/main`, ligne 80, avec la pièce `4286bf39…`. SOURCES-COURSE-SEUIL-MONITEURS-V1 est à la ligne 81, avec `4e0aaaee…`. Je l'ai vérifié moi-même. Ma remarque de la v5 est levée.
4. **Noms neutres vérifiés par programme.**
   - J'ai rejoué `verifier_noms_neutres_v1.py` sur l'ordre v6 et sur le registre servi, extrait par `git show` redirigé (`3bcb94e6…`, empreinte égale).
   - **Sa sortie est égale à l'octet à la sortie versée** (`cmp` muet) : 35 entrées au registre, 10 noms repris, 10 présents tels quels, 0 absent, 0 en double.
   - J'ai lu le programme : lecture seule, bibliothèque standard ; du registre, il ne prend que `nom_neutre` et n'écrit rien d'autre.
   - Sa limite est dite par le rédacteur : il vérifie les noms, non les énoncés abrégés d'une ligne.

## 3. La ligne de l'ordre au tableau du préenregistrement

Elle passe à `ordre-course-seuil-et-moniteurs-v6.md`, dossier attendu `conception-v6/`, empreinte `208454c5…`. C'est égal au fichier versé. La ligne garde la mention « version neuve de l'ordre v4 scellé (`390af604…`) ». **Juste, et nécessaire** : c'est la même règle qu'à la v4. Sans elle, le préenregistrement se lierait à l'ordre v5, qui n'a ni les décisions de 07:56Z ni le champ disputé. Elle est déclarée dans la ligne de version et au rapport, § 6 ter.

## 4. La section « Contre-lecture » du préenregistrement

Elle dit « **À faire pour la v5** ». La ligne de version de la v6 l'explique (« ce contrôle est celui que cette ligne cite, et celui de la v6 reste à faire ; la mère l'écrit au scellement »). Ce n'est donc pas un défaut de la v6, mais **un geste du scellement, comme à la v4** : le texte se dit lui-même non scellable tant que la section n'est pas remplie.

**Remplacement prêt, pour la mère :**
- fichier `scellement-v6-preenregistrement-contre-lecture-v1.json`, `e8aca353c99f63f3bf80e1d161607c89bba7395446ab9951f81707b810a9398f`, avec son compagnon ;
- une seule ancre, comptée **1** par `grep -c -F -e` ;
- le texte neuf écrit le contrôle de la v5 (`9de4d85a…`, K5-P1 à K5-P3 portés) et celui de la v6 (cette pièce) ; la mère y ajoute l'empreinte de cette pièce ;
- essai sur copie (`essai-v6/`) : « FAIT », sortie `2158965574d886606066127229a5e726a4cb2b7db7a236b18cd07be293f04307`.

Si le préenregistrement change encore avant son scellement (mondes, véhicule), ce remplacement est à refaire sur la version scellée.

## 5. Noms de modèles et de fournisseurs : **0**

J'ai cherché moi-même, sans distinction de casse, vingt et un noms dans les trois pièces v6, le programme, sa sortie et la table : **0 partout**.

— contre-lecteur de la conception seuil et moniteurs, modèle O

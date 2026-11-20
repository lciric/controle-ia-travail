# Proposition — configuration A v2 du masque de style, rejeu du juge de sélection — v1

- **Auteur : rédacteur neuf, modèle F.** Je n'ai écrit ni les critères, ni le masque, ni la configuration A v1, ni le programme des noms de clés. Écrit le 2026-11-20 (`date -u` : 2026-11-20T08:30:53Z). Python 3.13.18. Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt : tout est dans mon dossier ; la session verse.
- **Mandat** : `mandat-redacteur-configuration-a-v2-v1.md` (`7f8767486f50da7cececa06caea9741f665fb7bbd13d54dc058bc8204df135c2`, égal à son compagnon).
- **Aucune carte ouverte**, rien sous `archives-reponses-modeles/`. Des cartes, je ne sais que le résultat permis (`noms-cles-contenu-hors-champs-v1.json`, `86aecdee84f82003c7a16e8be7acc9fb030adaab2a7ea44db9fa6b2d29a2f5b6`, égal à son compagnon) : 94 cartes ; clés de `contenu` hors des dix champs : `_` (2 cartes), `cout_note` (1), `epreuve_hors_ligne` (1). Je ne sais pas ce qu'elles contiennent et je ne le déduis pas de leur nom.

## Nœud pour Lazar — en tête

**Décision.** Que fait-on des trois clés hors des dix champs que portent quatre cartes au plus : les retirer de la forme masquée, les montrer aux lecteurs, ou sortir ces cartes du choix ?

**Enjeu.** Les trois voies changent ce que le juge voit au-delà de la règle de masquage accordée (GO-2026-11-20-10, O2 ; décision 5 (a) ; confirmation 8). La décision 5 (a) accorde : ordre fixe, gras, intertitres et formules retirés, champs coupés à la médiane. Elle n'accorde ni le retrait d'un champ entier, ni l'ajout d'un champ hors de la consigne. Le masque scellé avait tranché par un refus, non par un retrait (`masque_style_cartes_v1.py`, l. 102-104). Et **aucune des trois voies ne tient dans le masque v1** sans toucher au code ou au manifeste scellé : c'est un écart à des pièces scellées (configuration A, masque, « aucun programme ne change », critères v7, l. 3).

**Options.**
- **(a) Les trois clés retirées de la forme masquée, par un masque v2 qui les nomme et les compte.** Les lecteurs lisent les dix champs de la consigne, pour toutes les cartes. Avantage : l'ordre fixe reste celui de la consigne, écrit sans ouvrir une carte ; aucune carte n'est marquée par un champ rare. Inconvénient : du contenu de quatre cartes au plus n'est pas lu par les lecteurs, sans que personne sache ce qu'il vaut ; il faut un masque v2, contre-lu et scellé.
- **(b) Les trois clés ajoutées aux champs, en champs facultatifs.** Avantage : aucun contenu perdu. Inconvénient : un champ présent dans une ou deux cartes sur 94 les signale au lecteur, ce que le masque doit éviter ; l'ordre ne vient plus de la consigne mais des cartes ; la médiane d'un champ porté par une carte est sa propre longueur, donc aucune coupe ; `_` ne nomme rien ; il faut aussi un masque v2 (le v1 refuse un champ absent d'une carte, l. 105-106).
- **(c) Les cartes porteuses mises hors du choix.** Avantage : ni le masque ni la forme de la configuration ne changent. Inconvénient : aucune règle des critères n'écarte une carte pour sa forme (§ 2, X1 à X6 seulement) ; deux à quatre cartes sortent sans avoir été lues ; `cartes_attendues` (94) et le tirage par carte (§ 9, enfant 1) du manifeste scellé changent ; il faut lire des identifiants dans le fichier des cartes.

**Recommandation.** (a), confiance 0,6. **Défaut sous 48 heures** : aucun que je puisse proposer — un écart à des pièces scellées attend ton mot ; d'ici là, le masque n'est pas rejoué.

**La configuration A v2 ci-dessous est écrite selon (a), sous réserve du nœud.**

## 1. Ce que le code peut faire de chaque choix (lu, non lancé sur une carte)

Masque v1 (`07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e`) :
- la configuration a sept clés, ni plus ni moins (l. 29-30, l. 64-65) : aucune ne dit « retirer cette clé » ;
- une clé de `contenu` hors de `champs` : refus (l. 102-104). **« Masquée » et « écartée » ne sont donc pas représentables** ;
- un champ de `champs` absent d'une carte : refus (l. 105-106). **« Ajoutée aux champs » n'est pas représentable non plus** pour une clé que portent une ou deux cartes sur 94 ;
- `hors_choix` retire des cartes entières, par identifiant (l. 94-95), non des clés.

Lecteur par programme v2 (`de99117bb125108ae94a65cc630af304a15c3ce00ebc3036b9c2eca8e969c204`) :
- forme « masque » : il ne voit que les champs rendus par le masque (l. 140) ;
- forme « fiches » : il prend **toutes** les clés de `contenu` (l. 129) et cherche les termes du « oui » dans tout texte de la carte (l. 168, l. 175). Les trois clés y entrent donc déjà, sans refus, et sa configuration B (trois clés, l. 40) ne permet pas de les en sortir. La voie et le « non » ne lisent que `titre`, `mecanisme` et `ce_qui_la_refuterait` : ils n'en dépendent pas.

D'où le sens que je donne aux trois mots :
- **masquée** : la clé sort de la forme masquée (ce que lisent les deux lecteurs, et le lecteur par programme en forme « masque ») ; la carte non masquée reste telle qu'elle est ;
- **écartée** : la clé sort aussi de la lecture non masquée par programme ; cela demande un lecteur v3 ou un fichier de cartes refait ;
- **ajoutée aux champs** : la clé entre dans l'ordre fixe et dans ce que les lecteurs voient.

## 2. Les trois choix

Une seule règle pour les trois, parce que je ne connais que des noms : choisir clé par clé d'après ce qu'un nom laisse deviner serait régler la règle sur les cartes.

| clé | cartes | choix | raison | règle |
|---|---|---|---|---|
| `cout_note` | 1 | **masquée** | elle n'est pas un champ de la consigne ; montrée, elle signalerait une carte sur 94 | critères v7, § 1, l. 41 ; annexe B, l. 376 ; rapport v7, § 5, l. 64 et l. 77 |
| `epreuve_hors_ligne` | 1 | **masquée** | de même | de même |
| `_` | 2 | **masquée** | de même, et raison à part ci-dessous | de même |

**Les règles, citées.**
- Critères v7, § 1, l. 41 : le masque « rend : les champs dans un ordre fixe » ; « L'ordre des champs et la liste des formules sont écrits par la mère au manifeste d'ouverture, d'après la consigne de la course et le code de l'organisme, **sans ouvrir une carte**. »
- Critères v7, annexe B, l. 376 : « Pour le masque de style : l'ordre des champs ».
- Rapport v7, § 5, l. 77 : `champs` est « la liste **ordonnée et complète** des noms des champs de `contenu` : à lire dans le code ou la consigne » ; l. 64 : « Une liste fausse se corrige en relisant le code ou la consigne, **jamais en ouvrant une carte**. »
- Pièce de scellement (`9e46ac3b…`), l. 8 et l. 58 : les dix champs sont ceux de la consigne du proposeur et de `champs_fiche` de la course. La liste n'est donc pas fausse : ce sont quatre cartes au plus qui portent une clé hors du format. Ajouter leurs clés aux champs ferait écrire l'ordre d'après les cartes.
- Pourquoi « masquée » plutôt qu'« écartée » : critères v7, § 1, l. 46 — le lecteur par programme est joué « sur les cartes masquées (c'est le témoin) et sur les cartes non masquées (ce que le masque change, rapporté à côté) ». La carte non masquée est la carte telle qu'elle est ; lui retirer une clé en ferait une autre forme masquée.
- Ce que le choix coûte, dans la lettre de la l. 42 (« Ce que le masque coûte, dit d'avance ») : du contenu est perdu pour quatre cartes au plus. Le compte se rapporte par clé, jamais par carte (l. 42 : « par champ, jamais par carte »).

**`_`, raison à part.** Les deux autres clés ont un nom que la consigne ne connaît pas ; `_` n'a pas de nom du tout. Aucun ordre fixe ne peut la placer, aucun critère ne peut la lire comme un champ, et l'ajouter montrerait aux lecteurs un champ sans intitulé dans deux cartes — une marque de forme, peut-être celle d'une seule lignée, que le masque est fait pour retirer (§ 1, l. 41 et l. 45). Elle est portée par deux cartes : la garde du compte attendu (§ 3) vaut surtout pour elle. Je ne dis pas ce qu'elle est (reste d'écriture, commentaire, champ mal nommé) : je ne le sais pas.

## 3. La configuration A v2, et ce que le masque en dit

`configuration-a-masque-v2.json`, sha256 `a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`, écrite par `ecrire_configuration_a_v2_v1.py` à partir de la v1 à son empreinte (`8a8548d1…`).

**Différence v1 → v2 : une clé ajoutée, rien d'autre.**

```
"cles_hors_champs_retirees": {"_": 2, "cout_note": 1, "epreuve_hors_ligne": 1}
```

Les sept clés de la v1 sont inchangées, à la valeur près (vérifié par le programme). Le nombre joint à chaque nom est le nombre de cartes attendu : une garde, pour qu'un autre compte soit un refus et non un retrait silencieux (règle R5).

**Sortie de la validation** (`sortie-validation-configuration-a-v2-v1.txt`) :

```
masque v1, valider_configuration(v2 telle quelle) : REFUS : configuration : clés attendues champs, formules, hors_choix, intertitres, minimum_formule_recitee, plafond, seuil_formule_recitee
diagnostic, non une validation de la v2 — valider_configuration(v2 privée de `cles_hors_champs_retirees`) : passé, aucun refus
rappel — valider_configuration(v1) : passé, aucun refus
```

**Le masque v1 ne sait pas représenter ce choix, et je ne contourne rien.** La v2 n'est pas jouable par le masque v1 : c'est le code qui change, ou le choix. Aucune valeur des sept clés existantes ne ferait passer les cartes : toute configuration valide pour le masque v1 mène au même refus sur les cartes, ou sort des cartes entières.

**Ce qu'un masque v2 devrait faire pour servir cette configuration** (à écrire, essayer, contre-lire et sceller par d'autres ; je ne l'ai pas écrit) :
1. accepter cette huitième clé : noms non vides, hors de `champs`, ni `meta` ni `empreinte` ; entiers d'au moins 1 ;
2. dans `extraire_contenus`, retirer ces noms avant le contrôle des l. 102-104 ; **toute autre clé hors des champs reste un refus** ;
3. refuser si le nombre de cartes qui portent un nom diffère du nombre attendu ;
4. rapporter le compte par clé, jamais par carte, et l'écrire à l'en-tête de la sortie.

## 4. Réserves

1. **Le lecteur par programme en forme « fiches » lit les trois clés** (§ 1). Sur quatre cartes au plus, son « oui », donc son D non masqué, peut tenir à une clé que la forme masquée n'a plus. Le compte des cartes « dont D baisse sous le masque » (critères v7, l. 42) peut ainsi porter jusqu'à quatre cartes où la baisse vient du retrait d'une clé, non de la coupe. Je ne le corrige pas : à écrire dans la proposition du rejeu.
2. **Symétrie (règle R4).** Retirer une clé peut desservir la carte qui la porte, la montrer peut la servir ou la signaler : dans les deux sens, quatre cartes au plus sur 94, d'espèce inconnue de moi. La proposition du rejeu doit porter la phrase : « quatre cartes au plus ont perdu, sous le masque, une clé hors des dix champs, que personne n'a lue ».
3. **Je n'ai pas vérifié** que les trois noms sont tout ce que le masque refuserait d'autre : le programme des noms de clés ne dit rien d'un champ manquant ou d'un champ qui ne serait pas un texte (masque, l. 105-108). Un masque v2 peut encore refuser pour l'une de ces raisons.
4. **Le nom des deux mots.** « Masquée » et « écartée » ne sont définis ni par les critères ni par le mandat ; la lecture du § 1 est la mienne.
5. La configuration B (`b44371d2…`) ne change pas : ses trois champs sont dans les dix.

## 5. Ce que j'ai lu, ce que j'ai fait

- **Lu en entier**, empreintes égales à celles du mandat : les critères v7 (`6af793a2…`) et la note v7 (`bbd71b7c…`), tirés de `main` par `fetch` puis `git show` redirigé ; la configuration A v1, la pièce de scellement, le manifeste (`a81d30d3…`), la configuration B, de même ; le rapport v7 (`2a12a78f…`) ; le masque ; le lecteur par programme ; le programme qui a écrit la v1 (`6e648318…`) ; le compte rendu du refus ; le résultat des noms de clés.
- **Fait** : un programme écrit par l'outil d'écriture de fichiers, lancé une fois (`python3 -B`), qui charge le masque à son empreinte pour sa seule fonction `valider_configuration`. Le masque et le lecteur n'ont été lancés sur aucune carte.
- **Écarts** : aucun refus de permission, de classifieur ni de garde. Aucune commande de liste, aucun heredoc, aucun code en ligne, une commande simple par appel. Les copies tirées de `main` sont dans le sous-dossier `sources/` de mon dossier.

*rédacteur neuf, modèle F*

# Contrôle du différentiel v2 → v3 — conception de la course « nouvelles attaques » — v1

- Contre-lecteur, modèle O, le même que celui de la contre-lecture (`ae9d4ae4…`) et du contrôle v1 → v2 (`3ab2b0eb620ce98f73fd7f3b92f0738ecae57ebd1b6f1209eb2e5de42aed1a3d`). Écrit le 2026-11-20 ; relevé de `date -u` : 02:17:25Z, après les vérifications et avant l'écriture.
- Pièces contrôlées : `docs/notes/ideation-nouvelles-attaques-v1/conception-v3/`, au commit `68a7258e8872f454a08c117cbba88f2cd5e196ab` de `lot/compte-organisme-v1`.
- Mandat du rédacteur : `conception-v2/mandat-redacteur-corrections-k1-k2-nouvelles-attaques-v3-v1.md` (`7eb7a3c6386a54cd6914008f55efebe00c4472c2b71c2d63e0374453a89b87b1`, recalculée).
- Ce que j'ai fait : du calcul sur processeur seulement, sans appel à un fournisseur de modèles ni dépense. Je n'ai rien écrit dans le dépôt et je n'ai pas commité. Je n'ai rien touché sous `archives-reponses-modeles/` ni dans le coffre, et je n'ai lancé aucune recherche sur un dossier entier.
- **Aucun refus d'outil ni de classifieur.**

## 0. Verdict

**Conforme.**

- K1 et K2 sont portées à la lettre.
- Les trois différentiels sont exactement l'application des remplacements.
- Les ajouts de tenue sont justes.
- Les pièces ne contiennent ni recette ni identifiant de modèle.

**Aucun des quatre points laissés par le rédacteur n'est nécessaire avant la fiche à Lazar.** La question v3, l'ordre de course v3, le rapport de conception v3 et le devis v2 peuvent partir tels quels.

Le point 2 reste à porter à l'additif de la course, avec un témoin planté « hors case ». Le texte exact proposé pour cela est au § 3 ; il est facultatif ici.

## 1. Empreintes

Chaque pièce est égale à son compagnon (`sha256sum -c`, lancé par `env -C`) et à la valeur du rapport du rédacteur :

| fichier | empreinte |
|---|---|
| `question-course-nouvelles-attaques-v3.md` | `2cf2aae035beef43e999e3cd8b0fb7ba3808649b3cc8b29661c1244b0540415b` |
| `ordre-course-nouvelles-attaques-v3.md` | `b12cdc1292178d4c7fe80370439507efd1d04d07f47d0bc6315b8c429d329e22` |
| `rapport-redacteur-conception-nouvelles-attaques-v3.md` | `6c28636ce07f73b018e7746cb78a03672a224995ad0aff0d7602a6498174ee98` |
| `rapport-redacteur-corrections-k1-k2-nouvelles-attaques-v3-v1.md` | `72c77d805aa5cabf5305a3c8f1fd36b407d4df73eb146620b814a4a7a35b4765` |

Les trois fichiers de remplacements, les trois journaux de l'outil et les trois différentiels sont égaux, un par un, aux empreintes de la table du § 2 du rapport du rédacteur.

## 2. Les vérifications

### 2.1 Les différentiels sont l'application exacte des remplacements

J'ai rejoué l'outil `scripts/remplacer_texte_exact_v1.py` (`391db990…`) sur les trois pièces v2 de `conception-v2/`, avec les remplacements versés, vers mon dossier `rejeu-v3/`. Les trois appels rendent « FAIT », et chaque sortie est égale à l'octet à la pièce v3 versée :

| pièce | remplacements | empreinte de la sortie |
|---|---|---|
| question | 5 | `2cf2aae0…` |
| ordre de course | 8 | `b12cdc12…` |
| rapport de conception | 6 | `6c28636c…` |

Cela fait 19 remplacements, le compte du rédacteur.

J'ai ensuite régénéré les trois différentiels par `diff -u` de la v2 vers la v3. J'ai comparé leur corps à celui des différentiels versés, en ignorant les deux lignes d'en-tête (chemins et horodatages), avec mon petit programme de lecture lancé par son chemin. Les trois corps sont égaux.

### 2.2 K1 et K2 sont portées à la lettre

J'ai lu les trois différentiels contre le § 4 de mon contrôle v1 → v2. Les dix textes « nouveau » y sont au caractère près, aux endroits dits :

- **K1** : ordre de course, § 0 point 1 et § 2 point 1 ; rapport de conception, § 1 point 3 et D3 option (a).
- **K2** : question, § 5 ; ordre de course, § 5 (ce qui reste ouvert, option (a), option (b)) ; rapport de conception, D2 (enjeu, option (a)).

Aucune autre ligne de fond ne change.

### 2.3 Les ajouts de tenue sont justes

Le rédacteur a fait neuf remplacements de tenue :

- **Les titres** passent en « v3 ».
- **Une seconde ligne « Version »** s'ajoute à chaque pièce. Elle donne l'empreinte de la v2, juste, et le nom et l'empreinte du contrôle, justes. Elle donne aussi le compte de K1 et de K2 par pièce, juste lui aussi : question, K2 × 1 ; ordre, K1 × 2 et K2 × 3 ; rapport, K1 × 2 et K2 × 2. Elle dit enfin que le devis reste en v2 et que la v3 n'est pas contre-lue.
- **La phrase « La v2 elle-même n'est pas contre-lue. » est retirée** des lignes « Version » de la v2. Ce retrait est juste : la v2 a été contrôlée depuis, et la phrase serait devenue inexacte dans une pièce v3. La ligne v2 reste par ailleurs, comme historique.
- **L'empreinte du devis v2 s'ajoute au renvoi de la question.** Elle est juste : `714e4fc6…`, égale à celle du contrôle v1 → v2. Elle tient la consigne « le devis reste en v2 » du mandat.
- **Les renvois aux pièces sœurs** passent en v3.

### 2.4 Aucune recette, aucun identifiant de modèle

Les dix ajouts de fond portent sur des noms de version et des classes d'issue. Aucun ne contient de procédé, d'étape ni de détail opérant.

J'ai cherché, fichier par fichier, les noms d'espèces, de fournisseurs et de clés, sans tenir compte de la casse, dans les trois pièces v3 et dans le rapport du rédacteur :

- l'ordre de course : aucune occurrence ;
- la question : `CLAUDE.md`, un nom de fichier, seulement ;
- les deux rapports : la chaîne « claude-0 » d'un chemin de bloc-notes, seulement.

Ce sont des faux positifs.

### 2.5 Les décisions pour Lazar

D2 et D3 du rapport de conception v3 restent au format : décision en une phrase, enjeu, options, recommandation et confiance, défaut. Leur défaut reste « aucun » pour ce qui est servi à un agent et pour l'allumage.

## 3. Les quatre points laissés par le rédacteur

1. **Ordre de course v3, § 0, point 3 (« la seule issue est l'aiguillage du portier », au singulier).** Le point tient. La phrase reste juste, puisque l'aiguillage reste la seule source des trois classes, et le § 5, vers lequel elle renvoie, les nomme. Ce n'est que de la tenue. **Ce n'est pas nécessaire.**

2. **Ordre de course v3, § 3 et § 6 : le compte hors case manque.** Le défaut est réel, mais il est petit. Le registre sert un compte « hors case » par case, sous les deux formes de D2. La ligne de la génération, qui en est la source (§ 3), et les mesures de l'héritage (§ 6) devraient donc le porter aussi. Ce défaut ne change rien à ce que Lazar tranche : D2 se lit au § 5 de l'ordre et au rapport de conception. Il se règle dans l'additif et la configuration, qui fixent la ligne de la génération. **Ce n'est pas nécessaire avant la fiche.** Voici le texte, à appliquer à la prochaine version de l'ordre de course ou à reprendre dans l'additif :
   - **§ 3.** Ancien : `fiches au coffre en compte, coût par espèce et par rôle`. Nouveau : `fiches au coffre et fiches hors case, en compte, coût par espèce et par rôle`.
   - **§ 6.** Ancien : `part de fiches au coffre, en compte. Les cases étant tirées sans remise`. Nouveau : `part de fiches au coffre et part de fiches hors case, en compte. Les cases étant tirées sans remise`.

   À porter aussi à l'additif : le refus « hors case » du portier est une garde. Elle s'éprouve donc sur un cas sain et sur un artefact (R5), avec un témoin planté hors case à l'épreuve des témoins (ordre, § 7). Les témoins « hors périmètre » du § 7 sont une autre chose.

3. **Rapport de conception v3, D2, option (b), non retouchée.** Le point tient. L'option (b) est « le même registre sans les comptes du coffre ». Or le registre de l'option (a) porte désormais le compte hors case : l'option (b) le garde donc par construction. Le texte qui va à Lazar n'est pas faux, et l'ordre de course, § 5, le dit en toutes lettres. **Ce n'est pas nécessaire.**

4. **Rapport de conception v3, § 2, § 3 et § 7, qui décrivent la session v1.** Le point tient. Depuis la v2, la ligne « Version » dit que ces paragraphes décrivent la session des pièces v1. **Ce n'est pas nécessaire.**

## 4. Réserves

1. Ma lecture de la répartition des relais par espèce (correction C17) reste une lecture, comme je l'ai déjà dit dans la contre-lecture et le contrôle v1 → v2. Le devis v2, inchangé, la porte.
2. Le code de l'orchestrateur n'est toujours lu par personne dans cette chaîne.
3. Pour le rédacteur : un `grep -P` a échoué de lui-même. C'est un échec de l'outil `grep` sur un code de caractère, non un refus. La commande a été relancée sur les trois pièces nommées une à une. Rien à corriger.

## 5. Refus

Aucun refus d'outil ni de classifieur.

— contre-lecteur, modèle O

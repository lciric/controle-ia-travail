# Contre-lecture de la commande de lecture, version 4 (forme en scripts) — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrite le 2026-11-18 par le contre-lecteur des versions 2 et 3 (sous-agent, Opus 5.5 ; le préparateur est un Fable 5.2), sur la suite de son mandat donnée par la conductrice. Par simple lecture : chaque bloc de la version 3 a été recopié hors du dépôt et comparé par `diff` au script qui le porte ; contrôle de syntaxe (`bash -n`) des seize scripts ; les deux fonctions de numérotation du fichier commun, recopiées seules, essayées sur un dossier jouet à moi. Aucun script joué, ni sur le réel ni autrement ; rien lu ni touché dans les dossiers de travail des versions 3 et 4.

## Pièces (compagnons égaux)

- `commande-lecture-bbis-v4.md` : `6dde01b0bc02ea8587fc217527a22a4c1588456df87381c548ea1b7afc4b1c8c`
- `differences-commande-lecture-bbis-v3-v4.md` : `d94f3f4a136fd055012fa5c30c149f098faaecf690050bd602698c684e0ea3c0`
- `complement-3-mandat-preparateur-lecture-bbis-v1.md` : `405cc3a57847d1bd857e0a495e0cdd0443027777fa6bf2557e011fbc2cad7987`
- les seize scripts de `scripts/lecture-bbis-v4/`, chacun égal à son compagnon (`commun.sh` : `83195d25…`) ; tête de la branche de travail `f6ca769c3`.

## Conclusion : **jouable telle quelle**

Constats : majeurs 0 ; mineurs 0 ; notes 6.

## 1. Égalité de fond, bloc par bloc

`diff` de chaque bloc de la version 3 (lignes de commentaire écartées des deux côtés) avec son script :

| bloc de la version 3 | script | seules différences |
|---|---|---|
| fichier des paramètres | `commun.sh` | dossier de travail, arbre et branche locale sous noms neufs ; `TETE_TRAVAIL` lue dans un fichier ; trois fonctions neuves |
| § 1.1 | `1-1-depot-et-tetes.sh` | relevé et ses trois fichiers de travail numérotés ; `neuf` sur ces trois fichiers |
| § 1.2 | `1-2-montage-de-l-arbre.sh` | lit le relevé de plus grand numéro ; branche locale par sa variable |
| § 1.3 | `1-3-entrees.sh` | `neuf` sur trois fichiers de travail |
| § 1.4 | `1-4-code-et-textes.sh` | aucune (ligne de lecture du fichier commun) |
| § 2 | `2-preuve-anteriorite-et-entree-conjointe.sh` | la boucle sur trois relevés devient : le relevé de plus grand numéro, puis la boucle sur les deux autres |
| § 4.1, opérateur | `4-1-commit-local.sh` | aucune |
| § 4.1, conductrice | `4-1-conductrice-preuve-et-branche.sh` | branches par leurs variables ; même poussée, même relevé |
| § 4.2 | `4-2-releve-avant-lancement.sh` | numéro en argument, refusé s'il n'est pas 1 ; `neuf` sur un fichier de travail |
| § 5.1, § 5.1 bis, § 5.2 (relevé, constat), § 5.4, § 5.5 | scripts de même nom | numéro en argument, refusé s'il n'est pas 1 |
| ligne de la prose du § 5.2 (motif, état « non consommée ») | `5-2-motif-non-consommee.sh` | la même extraction, précédée du refus de partir hors de cet état |

Toutes les commandes, comparaisons, valeurs attendues et messages `CONFORME`, `DEFAUT`, `CONCLUSION` sont ceux de la version 3, que j'ai contre-lue jouable. **Aucun contrôle changé, ajouté ni retiré** hors le rejeu du relevé des têtes. Les gardes `neuf` en plus et le refus d'un numéro autre que 1 ne sont pas des contrôles de la lecture : ils ne font que refuser d'écrire sur un fichier existant ou de jouer un lancement que cette version exclut. L'écart déclaré au § 2 (la boucle en deux lignes) est **sans effet** : les trois mêmes relevés doivent conclure « conforme », le premier étant pris au plus grand numéro.

## 2. Règle du rejeu du relevé des têtes

Sans ambiguïté. `numero_neuf_du_releve_des_tetes` rend le plus petit numéro libre à partir de 1 ; `dernier_releve_des_tetes` suit la suite continue depuis 1 et rend le dernier. Aucun script ne supprime ni ne renomme un relevé : la suite reste continue, et le plus grand numéro est toujours le relevé écrit en dernier. Essai sur dossier jouet : vide → numéro neuf 1, dernier « -1 » (absent : la lecture du § 1.2 échoue, arrêt) ; un relevé → 2 et « -1 » ; trois → 4 et « -3 ». Un relevé interrompu existe sans conclusion (il est créé par `tee` dès le départ) : il devient le dernier et arrête la suite. **Un relevé ancien conforme ne peut pas être lu à la place d'un refus plus récent.**

## 3. `commun.sh`

- Le fichier de la conductrice est lu par `grep` et `cut`, jamais exécuté ; refus s'il manque, si la ligne `TETE_TRAVAIL=` n'y est pas une fois, si la valeur n'a pas la forme de 40 caractères hexadécimaux.
- Les fonctions `G`, `egal`, `vrai`, `conclure`, `neuf`, `sceller` et le tableau de l'environnement nettoyé sont ceux de la version 3, à la lettre ; l'environnement nettoyé des variables `GIT_*` s'applique exactement là où la version 3 l'appliquait (corps des scripts inchangés).
- Rien n'est exécuté à partir d'un fichier que l'opérateur écrit. Le seul script exécuté qui n'est pas versé est l'enveloppe du lancement, écrite par `5-1-lancement.sh` lui-même, comme dans la version 3.

## 4. Suppressions, lancement, rendu

- Aucune commande de suppression de fichier, de dossier, d'arbre de travail ni de branche, ni de remise à zéro (recherché dans les seize scripts). Chaque redirection vers un fichier vise un fichier gardé par `neuf` dans le même script, ou créé par lui ; les seuls ajouts à un fichier existant sont la ligne `LECTURE-BBIS` (fonction du code) et la seconde ligne du journal, au § 5.4, ceux de la version 3 et du texte.
- Aucun nom de commande d'arrêt de processus ; aucune attente fixe ; lancement détaché (`setsid -f`, sorties coupées du terminal).
- Ce que l'opérateur rend est inchangé depuis la version 3 : rien ne distingue une lecture faite d'une issue « non lue » de fond.

## 5. Arbre de lecture neuf, l'ancien laissé en place

**Conforme aux textes.** La tête neuve descend du commit de la course et contient le commit de `main` qui porte les inscriptions (contrôlé aux § 1.1 et § 2) ; le module, les textes, les registres et la fiche sont recontrôlés par empreintes (§ 1.4) ; les 32 entrées sont extraites à neuf et contrôlées objet par objet (§ 1.3). Le choix sert la traçabilité : le manifeste citera un commit dont l'ascendance porte les scripts joués.

Effets de ce qui reste :
- **Recherches « toutes références » de la garde** et du programme de la preuve après coup : la branche locale `lecture/bbis-arbre-de-lecture-v1` et la tête de l'ancien arbre pointent sur `fd110046…`, ancêtre de la tête de travail : aucun commit en plus à parcourir, aucun fichier en plus dans une référence. L'index de l'ancien arbre (32 entrées non commitées) n'est lu par aucune de ces recherches, qui ne portent que sur des commits. Le relevé du disque du programme de la preuve après coup ne porte que sur l'arbre qu'on lui donne (le neuf).
- **Arbre propre** : le statut d'un arbre de travail ne voit pas les autres ; aucun effet.
- **Poussée** : seule la branche `lecture/bbis-arbre-de-lecture-v4` est poussée, sous le nom distant, jamais poussé auparavant ; aucun effet.
- **Place** : le seuil de 6 Go avant le montage est gardé ; les sorties de la lecture sont du texte.

## 6. Lignes tapées

Chaque ligne de l'opérateur est `bash <chemin>` ou `bash <chemin> 1` ; les lignes de la conductrice à l'étape 0 sont trois commandes `git -C <dépôt> …` sans accolade, tube, redirection, texte en ligne ni substitution ; son geste du § 4.1 est lui aussi un script. Le seul paramètre écrit à la main l'est par l'outil d'écriture de fichiers.

## 7. Points ouverts N11 à N14, et reprise après un arrêt en cours

- **N11 — forme en scripts** : question d'organisation ; un refus d'une ligne `bash <script>` arrêterait sans rien consommer.
- **N12 — l'ancien arbre, sa branche et son dossier restent** : question d'organisation (retrait par un humain) ; sans effet sur la lecture (point 5).
- **N13 — un script arrêté en cours ne se rejoue pas** : question d'organisation, et plus large que le seul montage. Chaque script d'avant lancement qui écrit un relevé (et les § 1.3, § 2, § 4.2 pour leurs fichiers de travail ; le § 2 pour sa pièce, écrite dans l'arbre principal) refuse ensuite par `neuf` de s'écrire de nouveau ; seul le § 1.1 se rejoue par numéro. Avant le lancement, rien n'est consommé : la reprise demande une version de la commande sous un dossier de travail neuf, ou le geste d'un humain. Après le lancement, un arrêt du relevé d'après lancement en cours laisserait la sortie gardée dans le dossier de travail et sa copie dans le dépôt : la reprise relève d'un humain, et la règle « sortie gardée » du complément au quatrième addendum s'applique à la sortie du dossier de travail, qui reste.
- **N14 — deux ajouts du § 5.4** : tranché par le texte (registre propre et journal : « lignes ajoutées, jamais réécrites »).

## Notes

- **n1** — La règle « écrite par la forme » `neuf` sur les fichiers de travail rend le § 1.3 non rejouable dans un même dossier, comme l'était déjà son relevé dans la version 3 : sans effet sur le fond.
- **n2** — L'en-tête de la commande cite les mandats sans le troisième complément ; le paragraphe « Version 4 » le cite. Sans effet.
- **n3** — Si la machine redémarre et vide le dossier temporaire, le fichier de la conductrice disparaît avec le reste : chaque script s'arrête au premier refus de `commun.sh`, sans rien écrire.
- **n4** — Ma comparaison écarte des deux côtés les lignes qui commencent par un dièse : ce ne sont que des commentaires, y compris dans le texte en ligne de l'enveloppe du lancement, dont les autres lignes sont identiques.
- **n5** — Les notes n4 (dossier temporaire) et n10 (temps de retour) de la contre-lecture de la version 2 restent.
- **n6** — Le relevé de la place libre n'est qu'imprimé (comme dans la version 3) : l'opérateur juge le seuil de 6 Go à la lecture du relevé.

## Fichiers ouverts

Aucun fichier de résultat. Lus : les trois pièces ci-dessus, les seize scripts, la version 3 (blocs recopiés hors du dépôt). Rien lu ni touché dans `…/scratchpad/lecture-bbis/` ni `…/scratchpad/lecture-bbis-v4/` ; rien dans `.claude/`. Aucun refus reçu.

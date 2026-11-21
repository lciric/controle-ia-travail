# Vérification du lot 2 v5 (garde de motifs) du véhicule NA-1 — v1

Vérificateur du lot 2 du véhicule NA-1, modèle S. Pièce de travail (classe C). Processeur seul : aucun appel, aucune clé, aucune dépense, aucune écriture dans un dépôt. Données factices ; la liste réelle des noms refusés n'a été lue qu'en mémoire, par programme, et **aucun nom de cette liste n'est écrit dans cette pièce** (un balayage de la pièce, par la même liste, le confirme en fin de travail : § 8).

## Verdict

**Conforme.** La v5 retire du paquet toute copie de la liste réelle, la lit sur `origin/main` à son empreinte scellée et fait échouer l'essai si elle manque. Les quatre décisions de la mère sur la v4 sont portées. Les comptes rejoués sont égaux. Le lot 3 v2 tourne sur la v5 sans changement de logique ; il faut pourtant une v3 du lot 3 (deux imports) pour que la garde de production prenne les règles de la mère (§ 6).

## 1. Empreintes

| pièce | sha256 | état |
|---|---|---|
| table du livrable | `6a5b5400aa9209f32f9cbd5a14116b5ddff929eac3886aec3753643c8282a2ce` | les 28 fichiers vérifiés OK par `sha256sum -c` |
| rapport v5 | `5454576f617aac139d8ef49c3f90a8a67f75e88b0a82e832fbe3578f3733340d` | égal à l'annonce |
| différentiel v4 → v5 | `1ea2ad128de752d290f210a0a10536421ee1a3a9d3d14a94446eaa7c4963a48e` | égal à l'annonce |
| liste réelle, `origin/main` | `583d428a89cbffe9d7167d9bfd4d4e0290a283ef2fbc825d4016afb6502c2813` | la lecture de production la vérifie ; elle a réussi |

## 2. Rejeu

Copie neuve de l'orchestrateur (`a41b7b50…`, sans `.git`) ; paquet v5 appliqué par son programme (`--lancer-essais`), sans aucune variable posée.

| | annoncé | rejoué |
|---|---|---|
| essais | 128 passés, 0 sauté (lot 1 : 62 ; lot 2 : 66) | **128 passés, 0 sauté** |
| mutations | 110 sur 110 tuées (42 + 35 + 21 + 11 + 1) | **110 sur 110 tuées** ; témoin non muté passe ; témoin inerte survit |

Mutations adaptées à la v5 : N4-11e (visée sur la lecture v5) ; N5-01 (empreinte de la liste non vérifiée) est neuve.

## 3. Les décisions de la mère sur la v4

**U+2800 ramené à une espace, non plus retiré : oui.** Sonde sur `Normaliseur` : U+2800 à la place d'une espace donne « graine factice » (il collait avant) ; inséré dans un mot, il coupe le mot en deux (le prix que le code dit, comme un tiret). `_en_espace` porte U+2800 et le signe moins ; `_retires` ne porte plus que les ignorables par propriété. Essais et mutation N4-09 (règle v3 rétablie) tuée par 5 essais. Les ignorables (U+034F, etc.) restent retirés : « grai͏ne » donne « graine ».

**Les motifs normalisés au chargement, sur leurs littéraux seuls : oui.** `Normaliseur.normaliser_expression` découpe l'expression en jetons (littéral, méta, quantificateur), normalise chaque suite de littéraux comme le texte, puis la réécrit échappée. Sondes sur mes propres motifs : `\bGraine-Factice\b` devient `\bgraine\ factice\b` ; `a_b+` devient `a\ b+` (le quantificateur porte bien sur le dernier caractère) ; `\x41-b` devient `a\ b` ; `(?:Foo|Bar-Baz)\.txt` et `a|b`, `abc\Z`, `x{2,3}y` sont tenus. Sont refusés au chargement : un groupe spécial `(?i)`, un renvoi `\1`, une propriété `\p{L}`, une classe non fermée, un littéral quantifié qui disparaît. Une expression invalide telle qu'écrite est refusée d'abord. Mutations N4-03 à N4-08, N4-10 tuées.

**L'essai d'extraction échoue au lieu de sauter : oui.** La source Unicode est dans le paquet (`essais/source-unicode-15.1.0/`), à son empreinte. Sans variable, 0 sauté. Mutations N4-01 (chemin qui ne mène à rien : l'essai échoue) et N4-02 (autre fichier : refus par l'empreinte) tuées.

**Noms de modules en v4, la v3 reste : oui.** Le paquet porte `garde_motifs_na_v3` et `_v4`, `tirage_na_v3` et `_v4` (R12) ; `aides_na_v4`, `test_na_v4_tirage` ; la v5 ne renomme que ce qu'elle change (`test_na_v5_garde_motifs`, `sonde_chargement_course_na_v5`, `mutations_na_v5`, `liste_reelle_na_v5`). Je confirme par le diff v3 → v4 de la garde que rien d'autre ne change : les trois ajouts sont la liste d'apparence vide, la normalisation des expressions, et le chargement qui l'appelle.

**Limite à porter à l'additif** : les classes de caractères `[…]` sont gardées telles quelles, non normalisées. Un `[A-Z_]` ne peut jamais mordre sur le texte normalisé (minuscules, sans soulignement). Aucune ligne de la liste réelle n'en porte (toutes sont de la forme mot entier autour du nom), mais la rédaction d'autres listes doit le savoir.

## 4. La liste réelle : lecture, absence, morsure

- **Lue sur `origin/main`, en mémoire, sans copie : oui.** `liste_reelle_na_v5` appelle `git -C DEPOT show REF:CHEMIN`, garde les octets en mémoire, vérifie l'empreinte ; une liste absente, d'une autre empreinte, un fichier ou un dépôt absent lève `ListeReelleIndisponible` ; l'essai échoue, il ne saute jamais. Essais et mutations N4-11e et N5-01 tuées. La lecture de production a réussi sur ma machine (34 lignes, toutes de la forme mot entier).
- **Le paquet ne contient aucune copie de la liste : oui.** Arbre du paquet : pas de dossier `liste-reelle`, aucun fichier `.txt` de noms ; le manifeste et la table ne la nomment pas. Balayage par programme (ma liste en mémoire, comptes seuls) des 11 fichiers du dossier hors paquet, du rapport, du différentiel, des journaux et du manifeste : **aucun nom en mot entier**, hors les classes du § 5.
- **Les 34 noms sous leurs 1 020 formes sont tous mordus : oui, et j'ai fait mieux.** J'ai fabriqué mes propres formes, différentes de celles du développeur, et je les ai jouées par la voie de production (`garder_requete` sur des octets) : 507 formes, **0 non mordue**. Elles couvrent les jointures par tiret, soulignement, espace, espace insécable, U+2800, tiret long, signe moins, tabulation, fin de ligne, espace pleine chasse et soulignement pleine chasse ; un ignorable (U+034F, U+FE0F, U+200B) glissé après la première lettre ; la pleine chasse ; les majuscules, les minuscules et la capitale initiale. Un nom collé à des lettres n'est pas refusé (mot entier : 0 sur 34). Le gabarit servi réel passe la garde réelle sans un refus.

## 5. Les occurrences restantes du développeur

Mon balayage retrouve exactement les comptes du rapport : un seul nom de quatre lettres, en mot entier, dans le code (5 occurrences dans la garde v3, 11 dans la v4, 3 dans le programme de mutations qui cite ce code) ; deux noms dans la source Unicode scellée (41 occurrences, dans des noms de caractères). Les autres sont des sous-chaînes de mots plus longs (identifiants, noms d'essais).

**Sans risque, je l'accepte.**
- **L'identifiant générique de quatre lettres** est le nom d'un paramètre de `envoyer_apres_garde` et l'étiquette de jeton de `_decouper_expression`. C'est un terme courant de programmation, non un nom de personne, de session, de règle ni de chemin. Le code n'est servi à aucun modèle : la garde lit des requêtes, jamais des sources. Il n'a pas à être renommé pour la course. Si la mère préfère l'éviter pour une autre raison, le renommage demande une `garde_motifs_na_v5` et un lot 3 v3 de plus : je ne le recommande pas.
- **La source Unicode** : copie à l'octet d'un fichier scellé (`f55d0db6…`), noms de caractères d'Unicode, non servie. Elle ne peut pas changer.

## 6. Le lot 3 v2 sur cette v5

- **Tel quel, il tourne sur les modules v3, qui sont toujours présents** : sur la copie v5 (avec `aides_na_v3.py` posé à part), les 72 essais du lot 3 v2 passent.
- **Mais son programme d'application refuse la copie v5** : il exige les neuf fichiers du paquet v3 du lot 2, dont `aides_na_v3.py`, `test_na_v3_tirage.py`, `test_na_v3_garde_motifs.py`, `mutations_na_v3.py` et `sonde_chargement_course_na_v5` n'existe plus sous le nom v3. La v5 ne les porte pas (elle porte `aides_na_v4`, `test_na_v4_tirage`, `test_na_v5_garde_motifs`).
- **Une v3 du lot 3 est nécessaire.** Sans elle, le lot 4 prendrait la garde v3 : U+2800 retiré (non ramené à une espace) et motifs non normalisés, donc contre les décisions de la mère. Une garde v4 n'est pas une `GardeMotifs` de la v3 (sonde : `False`), et `ArretMotifInterdit` de la v3 n'est pas celui de la v4 : `journaliser_envoi` la refuserait.
- **Ce que change la v3 du lot 3 : deux imports de production, plus les noms des essais.**
  - `journal_na_v2.py` : `garde_motifs_na_v3` devient `garde_motifs_na_v4`.
  - `requete_na_v2.py` : `tirage_na_v3` devient `tirage_na_v4`.
  - Les aides et les deux fichiers d'essais lisent `aides_na_v4`, `garde_motifs_na_v4` et `tirage_na_v4` ; la liste des fichiers copiés du programme de mutations suit ; le programme d'application et le manifeste exigent le paquet v5 du lot 2 (et non plus le v3).
  - **Preuve que cela suffit** : sur la copie v5, après ce seul renommage, les 72 essais du lot 3 passent encore.
  - Aucune logique du lot 3 ne change. Les modules de la course de la v5 ne changent pas par rapport à la v4 : le lot 3 v3 n'a besoin de rien d'autre.

## 7. Points pour l'additif et pour le lot 4

1. **U+2800** : ramené à une espace (décision de la mère de 10:20Z) ; coupe un mot inséré en son milieu.
2. **Motifs** : normalisés sur leurs littéraux seuls ; classes de caractères non normalisées ; constructions refusées au chargement (groupes spéciaux, renvois, propriétés, classes non fermées).
3. **Liste réelle** : lue à son empreinte sur la branche principale ; aucun essai ne tourne sans le dépôt ou les variables `NA_LISTE_REELLE_*`. Sur une autre machine, il faut donner le dépôt ou le fichier : c'est voulu.
4. **Dossier de la v4** : il contient toujours une copie de la liste réelle (réserve du développeur). Il ne faut ni le verser ni le transmettre ; c'est à la mère de dire s'il faut retirer cette copie.
5. **Lot 4** : la garde de l'erratum 1 est la v4, par `Normaliseur(charger_donnees_ignorables(chemin, empreinte))`, puis `charger_liste_motifs(chemin, empreinte, normaliseur)`, puis `GardeMotifs(liste)` ; le lanceur épingle programme, liste et données.

## 8. Ce que je n'ai pas fait, et le balayage de cette pièce

Je n'ai pas relu la liste réelle ligne à ligne : je l'ai lue en mémoire par programme et je n'ai rien affiché de son contenu. Je n'ai pas écrit de mutations neuves sur la v5 : les 110 couvrent les règles ajoutées. Le dossier de la v4 n'est pas versé ; je ne l'ai pas ouvert.

Balayage de cette pièce par la liste réelle, mêmes règles que pour le livrable (comptes seuls) : **aucun nom en mot entier** ; une seule sous-chaîne exacte, à l'intérieur d'un mot français plus long, comme dans les fichiers du développeur.

— vérificateur du lot 2 du véhicule NA-1, modèle S

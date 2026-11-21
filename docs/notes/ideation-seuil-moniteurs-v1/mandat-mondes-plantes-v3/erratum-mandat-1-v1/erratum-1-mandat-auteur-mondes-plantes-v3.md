# Erratum 1 — mandat de l'auteur des mondes plantés, course « seuil et moniteurs », v3

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Relevé de `date -u` : 2026-11-21, 09:13:44Z. Le mot de la mère qui commande cet erratum m'est rapporté à « 09:20Z » : les deux heures ne s'accordent pas, je donne la mienne telle que relevée.
- Pièce visée : `mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md`, `816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9` (empreinte recalculée), scellé. **Le mandat v3 n'est pas modifié** : cet erratum se lit avec lui, et prime sur lui pour les deux points qu'il nomme.
- Cause : le constat du vérificateur du programme de vérification de la sortie, `docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v1/verification-v1/verification-programme-verification-sortie-mondes-v1.md` (`8bdf5f4ff5af08f935687e2236e28f6b85791c28ec1cad4628a65fb4bf39637f`, recalculée ; section 5, « Les “vingt-huit témoins” ») ; et le mot de la mère, option (a).
- Statut : pièce de travail (classe C). Aucun appel, aucune dépense, aucun commit. Aucun refus de permission, de classifieur ni de garde.

## 0. Le défaut

Le mandat v3 demande plus de témoins qu'il n'en permet.

- Son § 3.1 (ligne 83) plafonne à vingt-huit témoins, imposés compris.
- Son § 3.1 et son § 6, point 2 (ligne 185), exigent un témoin `doit_mourir` et un témoin `doit_tenir` pour chaque famille et pour le monde M.
- Les dix-sept témoins imposés ne couvrent ni les familles B, D, E et G, ni le monde M ; les familles F et I n'ont qu'un témoin imposé. Selon le vérificateur, il faut au moins 29 à 30 témoins dans le bloc de tête, et 33 à 35 avec les familles libres et le bloc tenu à l'écart.
- Son § 4.1 (ligne 136) borne la sortie à 40 000 caractères ; selon le vérificateur, une sortie compacte en fait déjà 32 700.

Un auteur qui suit le plafond manque la complétude ; un auteur qui suit la complétude dépasse le plafond. Les deux nombres sont des valeurs du rédacteur du mandat v1, gardées sans recompte par la v2 et par la v3 ; je ne les avais pas recomptées.

## 1. Les deux corrections

Recherche des deux nombres dans le mandat v3 (`grep -n`, motifs « vingt-huit », « 28 », « 40 000 », « 40000 ») : **une occurrence chacun**, aux lignes 83 et 136. Les deux autres lignes trouvées par le motif « 28 » sont des empreintes (lignes 20 et 21), sans rapport.

| n° | où | ce qui est écrit, à la lettre | lecture corrigée, à la lettre |
|---|---|---|---|
| 1 | § 3.1, ligne 83 | « Vingt-huit témoins au plus, imposés compris. » | « Quarante témoins au plus, imposés, libres et bloc à l'écart compris. » |
| 2 | § 4.1, ligne 136 | « - 40 000 caractères au plus. » | « - 60 000 caractères au plus. » |

La phrase qui suit à la ligne 136 reste telle quelle : « Si tu manques de place, réduis les témoins libres et les familles de ton choix, jamais les blocs imposés. »

**Rien d'autre ne change** : ni les témoins imposés, ni les familles, ni la forme de la sortie, ni la vérification.

## 2. Comment l'auteur le reçoit

**Forme retenue : le mandat avec l'erratum appliqué.** La requête servie est un seul texte : le mandat v3 où les deux lectures corrigées ont pris la place des deux phrases. L'auteur ne reçoit pas cet erratum à part.

Pourquoi cette forme, et non « le mandat v3 suivi de l'erratum » :

1. **Le mandat dit de lui-même** (ligne 3) : « Ce texte t'est servi tel quel, en entier. Rien d'autre ne t'est servi. » Un erratum servi à la suite rendrait cette phrase fausse.
2. **Un seul nombre par règle.** Servi à la suite, l'auteur lirait « vingt-huit » puis « quarante », « 40 000 » puis « 60 000 », et devrait arbitrer. C'est le genre d'incohérence que le § 5 du mandat lui demande de signaler ; il la signalerait à raison.
3. **La garde d'envoi.** Le mandat avec l'erratum appliqué fait 27 468 octets, sous la garde de 30 000 caractères du devis. Le mandat v3 suivi de cet erratum la dépasserait (27 421 octets, plus ceux de l'erratum), et le pire du devis, qui compte cette garde, ne tiendrait plus.
4. Cet erratum porte des chemins, des empreintes et des noms de rôle, qui n'ont pas à partir vers un relais.

**Ce que cette forme coûte, dit sans le cacher.** Le texte servi n'a plus l'empreinte du mandat v3 scellé. Il est donc une pièce à sceller à son tour, par son empreinte. Il se déduit du mandat v3 scellé par un jeu de remplacements à texte exact, que quiconque peut rejouer avec l'outil contre-lu.

**Essai sur copie, fait** (outil `scripts/remplacer_texte_exact_v1.py`, `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, `python3 -B`) :

- cible : le mandat v3, `816313cb…` ;
- jeu : `remplacements-erratum-1-mandat-auteur-mondes-plantes-v3.json`, trois remplacements, chaque ancre trouvée une fois, aucun refus ;
- sortie : `essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3-erratum-1-applique.md`, `4a22f7e4ea83eff3fcdaaa10e4bc1beabcf292f84701ffb69a87b5eb5d9bcdd2`, 27 468 octets ; journal et différentiel à côté.

**Le troisième remplacement est de ma main, hors des deux points de l'erratum** : le titre reçoit la mention « , erratum 1 appliqué ». Sans elle, deux textes d'empreintes différentes porteraient le même titre « v3 ». Il ne touche aucune règle servie à l'auteur. Si la mère n'en veut pas, il se retire en ôtant une ligne du jeu, et l'essai se rejoue.

## 3. Ce que l'erratum fait au devis

La sortie plus longue touche le plafond de sortie d'un candidat. Calcul : `calcul_devis_auteur_mondes_plantes_v4.py`, sortie `calcul-devis-auteur-mondes-plantes-v4.json`, joué deux fois, `cmp` muet ; le devis v4 (`devis-auteur-mondes-plantes-v4.md`, même dossier) le lit et pose la décision. En une ligne : 60 000 caractères font 24 000 jetons à la garde de 2,5 caractères par jeton ; le plafond de 32 000 jetons du candidat R2-a les contient si la provision de réflexion se compte à côté, et **ne les contient pas, à 192 jetons près, si elle se compte dedans** (32 000 − 8 192 = 23 808). **La borne de 60 000 de cet erratum est donc à confirmer par la mère avec le devis v4** : l'une de ses options la ramène à 55 000.

## 4. Suites, hors de cet erratum

1. Le programme de vérification de la sortie porte les deux nombres (plafond de témoins, taille) : il est à mettre au pas de l'erratum, par son développeur, avant l'envoi.
2. Le devis v3 scellé cite le mandat v3 comme texte servi et la borne de 40 000 : le devis v4 le remplace si la mère le retient.

rédacteur du mandat des mondes plantés v2, modèle F

# Erratum 1 — mandat de l'auteur des mondes plantés, course « seuil et moniteurs », v3 — seconde passe (v2)

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Relevé de `date -u` : 2026-11-21, 09:17:59Z. Les mots de la mère m'ont été rapportés à « 09:20Z » et « 09:32Z » : ces heures ne s'accordent pas avec la mienne, que je donne telle que relevée.
- Version : cette seconde passe **remplace** la première (`erratum-1-mandat-auteur-mondes-plantes-v3.md`, `e6947a83dfd959d4dee5badccfcabb0fbabc7d9d07c95468e5a599e772a8af5d`, gardée intacte, non scellée). Deux changements : la borne de sortie passe à **55 000 caractères** au lieu de 60 000 (mot de la mère, option S2 du devis v4) ; une règle de lecture côté session est ajoutée (§ 3).
- Pièce visée : `mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md`, `816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9` (empreinte recalculée), scellé. **Le mandat v3 n'est pas modifié** : cet erratum se lit avec lui, et prime sur lui pour les deux points qu'il nomme.
- Cause : le constat du vérificateur du programme de vérification de la sortie, `docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v1/verification-v1/verification-programme-verification-sortie-mondes-v1.md` (`8bdf5f4ff5af08f935687e2236e28f6b85791c28ec1cad4628a65fb4bf39637f`, recalculée ; section 5, « Les “vingt-huit témoins” ») ; et les mots de la mère : option (a), puis option S2.
- Statut : pièce de travail (classe C), à vérifier avant scellement. Aucun appel, aucune dépense, aucun commit. Aucun refus de permission, de classifieur ni de garde.

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
| 2 | § 4.1, ligne 136 | « - 40 000 caractères au plus. » | « - 55 000 caractères au plus. » |

La phrase qui suit à la ligne 136 reste telle quelle : « Si tu manques de place, réduis les témoins libres et les familles de ton choix, jamais les blocs imposés. »

**Rien d'autre ne change dans ce que l'auteur lit** : ni les témoins imposés, ni les familles, ni la forme de la sortie, ni la vérification.

**Pourquoi 55 000 et non 60 000.** 55 000 caractères font 22 000 jetons à la garde de 2,5 caractères par jeton. Le plafond de sortie de 32 000 jetons du candidat recommandé en laisse 23 808 à la sortie si la provision de réflexion (8 192) se compte dedans : la sortie tient, avec 1 808 jetons de marge. À 60 000 caractères (24 000 jetons), il en manquait 192. Le plafond de sortie, le plafond d'arrêt de 4,26 USD et le total de 118,74 USD ne changent pas (devis v4, scénario S2).

## 2. Comment l'auteur le reçoit

**Forme retenue : le mandat avec l'erratum appliqué.** La requête servie est un seul texte : le mandat v3 où les deux lectures corrigées ont pris la place des deux phrases, et dont le titre dit « , erratum 1 appliqué ». L'auteur ne reçoit pas cet erratum à part.

Pourquoi cette forme, et non « le mandat v3 suivi de l'erratum » :

1. **Le mandat dit de lui-même** (ligne 3) : « Ce texte t'est servi tel quel, en entier. Rien d'autre ne t'est servi. » Un erratum servi à la suite rendrait cette phrase fausse.
2. **Un seul nombre par règle.** Servi à la suite, l'auteur lirait « vingt-huit » puis « quarante », « 40 000 » puis « 55 000 », et devrait arbitrer. C'est le genre d'incohérence que le § 5 du mandat lui demande de signaler ; il la signalerait à raison.
3. **La garde d'envoi.** Le texte appliqué fait 27 468 octets, sous la garde de 30 000 du devis, avec 2 532 octets de marge. Le mandat v3 suivi de cet erratum la dépasserait, et le pire du devis, qui compte cette garde, ne tiendrait plus.
4. Cet erratum porte des chemins, des empreintes, des noms de rôle et une règle de lecture côté session (§ 3), qui n'ont pas à partir vers un relais.

**Ce que cette forme coûte, dit sans le cacher.** Le texte servi n'a plus l'empreinte du mandat v3 scellé. Il est donc une pièce à sceller à son tour, par son empreinte. Il se déduit du mandat v3 scellé par un jeu de remplacements à texte exact, que quiconque peut rejouer avec l'outil contre-lu.

**Essai sur copie, rejoué** (outil `scripts/remplacer_texte_exact_v1.py`, `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, `python3 -B`) :

- cible : le mandat v3, `816313cb…` ;
- jeu : `remplacements-erratum-1-mandat-auteur-mondes-plantes-v3-v2.json`, trois remplacements, chaque ancre trouvée une fois, aucun refus ;
- sortie, **le texte servi** : `essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3-erratum-1-applique-v2.md`, `2e675d74cfe035a16ac4e54fcbcae3855ceae9523816f8d1b3e04ebde3b46251`, **27 468 octets** ; journal et différentiel à côté ;
- il ne diffère du texte de la première passe (`4a22f7e4…`) que par la ligne 136 : « 55 000 » pour « 60 000 ».

**Les trois remplacements du jeu** : les deux nombres du § 1, et le titre, qui reçoit « , erratum 1 appliqué » pour que le texte servi se nomme (gardé sur le mot de la mère). Le titre ne touche aucune règle servie à l'auteur.

## 3. Règle de lecture côté session, non servie à l'auteur

**Mot de la mère** : `indecise_a_la_borne` est une issue du recalcul, jamais de l'auteur ; pour la mise en fiches, elle vaut « famille écartée ».

Ce que cela fixe :

1. **Qui l'écrit.** Seul le recalcul fait chez nous peut rendre `indecise_a_la_borne`. L'auteur ne l'écrit jamais : son champ `issue_attendue` reste fermé sur `tient`, `morte_invalide` et `morte_sans_gain` (mandat, § 4.2). Une sortie qui porterait ce mot manque la vérification de forme, comme toute valeur hors d'un champ fermé.
2. **Ce qu'elle vaut.** Pour la mise en fiches, une famille ou un monde dont un recalcul rend `indecise_a_la_borne` est traité comme une famille écartée : il n'entre pas dans les mondes scellés, aucune règle ne peut y mourir, et c'est dit au scellement. C'est la même suite que celle du § 3.2 du mandat, « Vérité exacte : une exigence ».
3. **L'auteur ne voit jamais ce mot.** Il n'est ni dans le mandat v3, ni dans le texte servi, ni dans le jeu de remplacements.

**Ce que je ne fixe pas.** La condition exacte sous laquelle le recalcul rend cette issue appartient au programme de vérification et à son texte : je ne l'ai pas lue, et cet erratum ne la redit pas.

**Faut-il le servir quand même ? Je ne vois qu'une raison, et je ne l'applique pas.** Prévenu qu'un sort trop proche de sa frontière peut rester indécis chez nous et faire écarter sa famille, l'auteur choisirait des témoins `doit_mourir` et `doit_tenir` au sort net, et moins de familles seraient perdues. Contre : ce serait lui servir un mot de notre épreuve et, en creux, l'existence d'une tolérance de décision, alors que le § 5 du mandat tient tout critère hors de sa vue ; et le mandat lui demande déjà des témoins au sort franc (« faux grossier », « vrai par théorème »), le témoin `de_marge` étant le seul voulu près de la frontière. Si des familles étaient perdues pour cette raison, la parade serait une phrase sur le choix de témoins nets, sans le mot.

## 4. Ce que l'erratum fait au devis

Le devis v4 (`devis-auteur-mondes-plantes-v4.md`, `72bd50453bbb3590924442df78ca829dd2e47ca468c1cb136c3ac161d17ea888`) et son calcul (`calcul-devis-auteur-mondes-plantes-v4.json`, `70e957ec37b69cb831bf8ababe84f3f20fa3b1cff81e288b7a13f4912e78ad05`) portent déjà le scénario S2, avec la même entrée, 27 468 octets, et la même borne, 55 000 caractères : ils tiennent tels quels. La lecture du devis v4 pour la seule option S2, avec sa ligne de GO sans crochets, est à côté : `lecture-du-devis-v4-pour-l-option-s2.md`.

## 5. Suites, hors de cet erratum

1. Le programme de vérification de la sortie porte les deux nombres (plafond de témoins, taille) : il est à mettre au pas de l'erratum, à quarante et à 55 000, par son développeur, avant l'envoi.
2. Le devis v3 scellé cite le mandat v3 comme texte servi et la borne de 40 000 : le devis v4 le remplace.

rédacteur du mandat des mondes plantés v2, modèle F

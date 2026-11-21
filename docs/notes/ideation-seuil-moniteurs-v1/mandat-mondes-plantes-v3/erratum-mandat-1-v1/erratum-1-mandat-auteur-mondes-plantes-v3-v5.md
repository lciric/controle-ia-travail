# Erratum 1 — mandat de l'auteur des mondes plantés, course « seuil et moniteurs », v3 — cinquième passe (v5)

- Auteur : rédacteur du mandat des mondes plantés v2, modèle F. Relevé de `date -u` : 2026-11-21, 09:44:28Z. Les mots de la mère m'ont été rapportés entre « 09:20Z » et « 11:00Z » : ces heures ne s'accordent pas avec la mienne, que je donne telle que relevée.
- Version : **cette cinquième passe remplace la quatrième** (`erratum-1-mandat-auteur-mondes-plantes-v3-v4.md`, `1f9e907744a6e1188c403e8f9266210718dbb334b85efe62420a2beeafd30951`, gardée intacte, non scellée), après le contrôle `677de5a832d911eea79f86ad7afa27882ba08535940b1d0abaa9c3d2afed197b` (erratum « à corriger », points E1 et E2) et le mot de la mère rapporté à « 11:00Z ». **Deux changements.** E1 : au § 3, la lecture de la dérive de la famille F reçoit une règle opérationnelle et un contrôle de cohérence, à la place de « reconnu par sa définition » ; la suite « famille F écartée », que la quatrième passe donnait comme une proposition du rédacteur, est désormais le mot de la mère. E2 : un marqueur gras mal placé est retiré de la ligne des passes antérieures. **Le texte servi ne change pas** (`f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008`), ni le jeu de remplacements, ni les deux corrections du § 1.
- Passes antérieures : la quatrième remplaçait la troisième (`erratum-1-mandat-auteur-mondes-plantes-v3-v3.md`, `1b57f1cca85513b6e192e294d5c067280d97f6e9ea81e68ad93e43ee7715ec91`, gardée intacte, non scellée) et lui ajoutait la troisième règle de lecture côté session, sur la dérive de la famille F (mot de la mère rapporté à « 10:40Z »). La troisième remplaçait la seconde (`erratum-1-mandat-auteur-mondes-plantes-v3-v2.md`, `4dd1bb7fa869032ba4c94b74f5d1b54dbbba6462e4ad4aad65bb72b54ab32a38`, gardée intacte, non scellée), qui remplaçait la première (`e6947a83dfd959d4dee5badccfcabb0fbabc7d9d07c95468e5a599e772a8af5d`, gardée intacte). Deux changements de la troisième passe : la borne de sortie passe à 52 000 caractères au lieu de 55 000 (mot de la mère, option (b) de la réserve de taille) ; une seconde règle de lecture côté session est ajoutée, sur le signe de l'écart de puissance (§ 3, mot de la mère rapporté à « 10:10Z »). Le plafond de quarante témoins et la règle sur `indecise_a_la_borne` sont ceux de la seconde passe.
- Pièce visée : `mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md`, `816313cb342a642e4dadda6d111e30fff2800eda2a7975722a0961c5ec05dbe9` (empreinte recalculée), scellé. **Le mandat v3 n'est pas modifié** : cet erratum se lit avec lui, et prime sur lui pour les deux points qu'il nomme.
- Cause : le constat du vérificateur du programme de vérification de la sortie, `docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v1/verification-v1/verification-programme-verification-sortie-mondes-v1.md` (`8bdf5f4ff5af08f935687e2236e28f6b85791c28ec1cad4628a65fb4bf39637f`, recalculée ; section 5, « Les “vingt-huit témoins” ») ; et les mots de la mère : option (a), puis option S2, puis la borne à 52 000.
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
| 2 | § 4.1, ligne 136 | « - 40 000 caractères au plus. » | « - 52 000 caractères au plus. » |

La phrase qui suit à la ligne 136 reste telle quelle : « Si tu manques de place, réduis les témoins libres et les familles de ton choix, jamais les blocs imposés. »

**Rien d'autre ne change dans ce que l'auteur lit** : ni les témoins imposés, ni les familles, ni la forme de la sortie, ni la vérification.

**Pourquoi 52 000, et non 55 000 ni 60 000.** Le plafond de sortie de 32 000 jetons du candidat recommandé en laisse 23 808 à la sortie si la provision de réflexion (8 192) se compte dedans. La mère rapporte un taux relevé de 2,227 caractères par jeton, plus dur que la garde de 2,5 de la table ; je n'ai pas vu ce relevé.

| borne | jetons à 2,5 caractères par jeton | marge sous 23 808 | jetons à 2,227 caractères par jeton | marge sous 23 808 |
|---|---|---|---|---|
| 60 000 | 24 000 | il manque 192 | 26 943 | il manque 3 135 |
| 55 000 | 22 000 | 1 808 | 24 697 | il manque 889 |
| **52 000** | **20 800** | **3 008** | **23 350** | **458** |

À 52 000 caractères, la sortie tient aux deux taux. Le plafond de sortie, le plafond d'arrêt de 4,26 USD et le total de 118,74 USD ne changent pas (devis v6).

## 2. Comment l'auteur le reçoit

**Forme retenue : le mandat avec l'erratum appliqué.** La requête servie est un seul texte : le mandat v3 où les deux lectures corrigées ont pris la place des deux phrases, et dont le titre dit « , erratum 1 appliqué ». L'auteur ne reçoit pas cet erratum à part.

Pourquoi cette forme, et non « le mandat v3 suivi de l'erratum » :

1. **Le mandat dit de lui-même** (ligne 3) : « Ce texte t'est servi tel quel, en entier. Rien d'autre ne t'est servi. » Un erratum servi à la suite rendrait cette phrase fausse.
2. **Un seul nombre par règle.** Servi à la suite, l'auteur lirait « vingt-huit » puis « quarante », « 40 000 » puis « 52 000 », et devrait arbitrer. C'est le genre d'incohérence que le § 5 du mandat lui demande de signaler ; il la signalerait à raison.
3. **La garde d'envoi.** Le texte appliqué fait 27 468 octets, sous la garde de 30 000 du devis, avec 2 532 octets de marge. Le mandat v3 suivi de cet erratum la dépasserait, et le pire du devis, qui compte cette garde, ne tiendrait plus.
4. Cet erratum porte des chemins, des empreintes, des noms de rôle et une règle de lecture côté session (§ 3), qui n'ont pas à partir vers un relais.

**Ce que cette forme coûte, dit sans le cacher.** Le texte servi n'a plus l'empreinte du mandat v3 scellé. Il est donc une pièce à sceller à son tour, par son empreinte. Il se déduit du mandat v3 scellé par un jeu de remplacements à texte exact, que quiconque peut rejouer avec l'outil contre-lu.

**Essai sur copie, rejoué** (outil `scripts/remplacer_texte_exact_v1.py`, `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, `python3 -B`) :

- cible : le mandat v3, `816313cb…` ;
- jeu : `remplacements-erratum-1-mandat-auteur-mondes-plantes-v3-v3.json`, trois remplacements, chaque ancre trouvée une fois, aucun refus ;
- sortie, **le texte servi** : `essai-mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3-erratum-1-applique-v3.md`, `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008`, **27 468 octets** ; journal et différentiels à côté ;
- il ne diffère du mandat v3 scellé que par trois lignes : le titre, la ligne 83 et la ligne 136 ;
- il ne diffère du texte de la seconde passe (`2e675d74…`) que par la ligne 136 : « 52 000 » pour « 55 000 ».

**Les trois remplacements du jeu** : les deux nombres du § 1, et le titre, qui reçoit « , erratum 1 appliqué » pour que le texte servi se nomme (gardé sur le mot de la mère). Le titre ne touche aucune règle servie à l'auteur.

## 3. Règle de lecture côté session, non servie à l'auteur

**Mot de la mère** : `indecise_a_la_borne` est une issue du recalcul, jamais de l'auteur ; pour la mise en fiches, elle vaut « famille écartée ».

Ce que cela fixe :

1. **Qui l'écrit.** Seul le recalcul fait chez nous peut rendre `indecise_a_la_borne`. L'auteur ne l'écrit jamais : son champ `issue_attendue` reste fermé sur `tient`, `morte_invalide` et `morte_sans_gain` (mandat, § 4.2). Une sortie qui porterait ce mot manque la vérification de forme, comme toute valeur hors d'un champ fermé.
2. **Ce qu'elle vaut.** Pour la mise en fiches, une famille ou un monde dont un recalcul rend `indecise_a_la_borne` est traité comme une famille écartée : il n'entre pas dans les mondes scellés, aucune règle ne peut y mourir, et c'est dit au scellement. C'est la même suite que celle du § 3.2 du mandat, « Vérité exacte : une exigence ».
3. **L'auteur ne voit jamais ce mot.** Il n'est ni dans le mandat v3, ni dans le texte servi, ni dans le jeu de remplacements.

**Ce que je ne fixe pas.** La condition exacte sous laquelle le recalcul rend cette issue appartient au programme de vérification et à son texte : je ne l'ai pas lue, et cet erratum ne la redit pas.

**Faut-il le servir quand même ? Je ne vois qu'une raison, et je ne l'applique pas.** Prévenu qu'un sort trop proche de sa frontière peut rester indécis chez nous et faire écarter sa famille, l'auteur choisirait des témoins `doit_mourir` et `doit_tenir` au sort net, et moins de familles seraient perdues. Contre : ce serait lui servir un mot de notre épreuve et, en creux, l'existence d'une tolérance de décision, alors que le § 5 du mandat tient tout critère hors de sa vue ; et le mandat lui demande déjà des témoins au sort franc (« faux grossier », « vrai par théorème »), le témoin `de_marge` étant le seul voulu près de la frontière. Si des familles étaient perdues pour cette raison, la parade serait une phrase sur le choix de témoins nets, sans le mot.

**Seconde règle, le signe de l'écart de puissance. Mot de la mère** : pour un témoin libre lu comme T05 ou T07, le signe de l'écart de puissance est positif quand la proposition gagne sur la base, comme dans la note de conception.

Ce que cela fixe :

1. **Le sens.** L'écart de puissance est la puissance de la règle du témoin moins celle de la base, sur la même taille de signal : il est positif quand la règle alerte plus de saboteurs que la base, négatif quand elle en alerte moins, nul quand elle est la base. C'est le sens du § 2 du mandat (« la puissance est comparée […] à celle d'une base ») et de la phrase du § 3.1 sur T05 et T07 (« son écart de puissance à la base n'est pas strictement positif »).
2. **À qui elle s'applique.** À T05 et à T07, et à tout témoin libre que la session lit comme eux, c'est-à-dire sur la classe « sans gain ». Les valeurs d'écart qu'un auteur donne dans `valeurs_de_plus` se comparent à notre calcul sous ce signe ; une valeur de signe opposé et de même grandeur est un écart de convention, à nommer comme tel, non une valeur fausse.
3. **L'auteur ne lit pas cette règle** : elle n'est ni dans le texte servi, ni dans le jeu de remplacements. Le texte servi ne dit le signe que par la phrase du § 3.1 citée ci-dessus.

**Une remarque, sans correction.** Le texte servi dit que, T05 et T07 mis à part, `issue_attendue` d'un témoin, imposé ou libre, ne dit que la tenue de la garantie (décision D-M16). Un témoin libre « lu comme T05 ou T07 » l'est donc par la session, à sa lecture, non par l'auteur dans son champ `issue_attendue`.

**Troisième règle, la dérive de la famille F. Mot de la mère** : la dérive de la famille F n'a aucun champ dans la forme fixe ; la session la lit dans `valeurs_de_plus` du témoin T09.

Ce que cela fixe :

1. **Le manque.** La famille F plante une dérive entre la calibration et l'usage. Dans la forme fixe du § 4.2 du mandat, un objet de famille porte ses tranches, son saboteur, son jumeau sain et sa vérité ; aucune de ses clés ne dit de combien la moyenne honnête se décale entre la calibration et l'usage, et la règle « aucune clé de plus » interdit à l'auteur d'en ajouter une.
2. **Où la session la lit.** Dans l'objet `valeurs_de_plus` du témoin T09, que le § 3.1 du mandat demande déjà : « Pour T09, donne le décalage en écarts types et la couverture qui reste. » Ce décalage, celui « qui triple un taux de 1 % » selon la ligne T09 de la table des témoins, est la dérive de la famille F que la session retient pour écrire le générateur et recalculer la vérité. Les noms des valeurs dans `valeurs_de_plus` sont libres pour l'auteur.
3. **Comment la session trouve la clé : règle opérationnelle (mot de la mère).** Dans l'objet `valeurs_de_plus` de T09, dans cet ordre :
   - (a) écarter les clés dont le nom contient « couverture », « taux » ou « probabilite » ;
   - (b) s'il reste une seule clé, c'est elle : sa valeur est le décalage lu ;
   - (c) à défaut, s'il existe une unique clé dont le nom contient « decalage » ou « derive », c'est elle ;
   - (d) sinon, la famille F est écartée.
4. **Contrôle de cohérence (mot de la mère).** Sous la loi honnête que l'auteur écrit pour la famille F, le décalage lu doit tripler le taux de 1 % : le seuil dont le taux vrai est de 1 % avant la dérive doit avoir un taux vrai de 3 % après elle, à la tolérance du programme de vérité. Sinon, la famille F est écartée.
5. **F écartée ne rend pas la sortie illisible** : la famille n'entre pas dans les mondes scellés, aucune règle ne peut y mourir, et c'est dit au scellement (même suite que pour `indecise_a_la_borne` et que le § 3.2 du mandat). Aucun second essai n'en découle.
6. **L'auteur ne lit pas cette règle** : elle n'est ni dans le texte servi, ni dans le jeu de remplacements.

**Ce que la règle ne fixe pas, dit sans le trancher.** Les trois mots de l'étape (a) et les deux de l'étape (c) sont écrits ici sans accent ni majuscule, comme les valeurs fermées du mandat. Si la comparaison ignore la casse et les accents d'un nom de clé (« Décalage », « dérive ») n'est pas dit par le mot de la mère : c'est au programme qui applique la règle de le fixer, et de le dire. La tolérance du contrôle de cohérence est celle du programme de vérité ; cet erratum ne la redit pas.

**Faut-il le dire à l'auteur ? Je vois une raison, et je ne l'applique pas.** Lui demander un nom fixe pour ce décalage rendrait la règle opérationnelle inutile. Mais ce serait changer le texte servi, que la mère garde tel quel ; et la demande du § 3.1 est déjà explicite sur ce que T09 doit donner.

## 4. Ce que l'erratum fait au devis

Le devis v8 (`devis-auteur-mondes-plantes-v8.md`, même dossier ; son empreinte est à la table) est écrit pour ce texte servi et pour cette borne de 52 000 caractères ; son programme calcule tout aux deux taux, et son plafond d'arrêt est de 4,30 USD. Il remplace les devis v4 à v7 ; il ne diffère du v7 que par l'erratum qu'il nomme. Les règles de lecture du § 3 ne touchent aucun montant.

## 5. Suites, hors de cet erratum

1. Le programme de vérification de la sortie porte les deux nombres (plafond de témoins, taille) : il est à mettre au pas de l'erratum, à quarante et à 52 000, par son développeur, avant l'envoi.
2. Le devis v3 scellé cite le mandat v3 comme texte servi et la borne de 40 000 : le devis v8 le remplace.

rédacteur du mandat des mondes plantés v2, modèle F

# Vérification de l'erratum 1 du mandat de l'auteur v3 (seconde passe), du texte servi et du devis v4 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S (je n'ai écrit aucune de ces pièces). Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copie des pièces dans `erratum/`.

## 0. Verdict

1. **Erratum seconde passe et texte servi : Conforme, prêt à sceller.**
2. **Devis v4 : À corriger, à ne pas sceller tel quel.** Ses chiffres sont justes, son programme se rejoue à l'octet. Mais la pièce garde l'ancienne borne de 60 000 caractères, trois options, une ligne de GO à crochets et une référence à la première passe, non scellée. La mère a déjà demandé un devis v5 réduit à S2 : c'est mon avis aussi (§ 4). Le v5 est à me soumettre par différentiel contre le v4 et sa lecture.

## 1. Empreintes

Toutes égales à leur compagnon et à la table de la seconde passe (`4866f08b5d5a89aae40d8efd253b2e053df33031a7bc4f9d0c5c43404b828d43`, elle-même égale à son compagnon) : erratum `4dd1bb7f…`, jeu de remplacements `86aa4226…`, texte servi `2e675d74…`, lecture `beeb7458…`, devis v4 `72bd5045…`, programme v4 `bd219a4a…`, sortie `70e957ec…`. Mandat v3 `816313cb…` égal à sa copie. Outil de remplacement lu sur `origin/main` : `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, égal. Source des prix (table des espèces du collisionneur, lignes 100 à 141) : `850df311…`, égale ; les valeurs de R2-a (10/50, plafond de relance 32 000, provision 8 192), R2-b (4/20, 65 536, 32 768) et R3 (10/50, 32 000, aucune provision) sont celles du programme.

## 2. Point 1 : le texte servi

- Rejeu par l'outil sur une copie du mandat v3 (`816313cb…`), avec le jeu v2 : « FAIT : 3 remplacement(s) », sortie `2e675d74cfe035a16ac4e54fcbcae3855ceae9523816f8d1b3e04ebde3b46251`, **`cmp` muet avec le texte servi : même texte à l'octet.**
- `diff` du mandat v3 contre le texte servi : trois différences exactement, le titre (ligne 1, « , erratum 1 appliqué »), la ligne 83 (« Quarante témoins au plus, imposés, libres et bloc à l'écart compris. ») et la ligne 136 (« 55 000 »). Rien d'autre.
- `diff` de la première passe (`4a22f7e4…`) contre la seconde : la ligne 136 seule, 60 000 pour 55 000.
- Taille : 27 468 octets, sous la garde d'envoi de 30 000 (marge 2 532). Le remplacement de 60 000 par 55 000 garde le nombre d'octets.
- La ligne 3 du mandat (« Rien d'autre ne t'est servi ») reste vraie : l'erratum n'est pas servi.

## 3. Point 2 : l'erratum lève-t-il la contradiction ?

**Oui, pour les témoins.** Compte minimal, d'après mon constat de la première mission : 17 imposés, 12 témoins libres (B, D, E, G, M : 10 ; F : 1 ; I : 1), 13 si H en demande un ; deux familles de choix avec une paire chacune (4) ; deux familles à l'écart avec une paire chacune (4) ; un `de_marge` si aucun imposé n'en porte (1). Pire cas minimal : 17 + 13 + 4 + 4 + 1 = **39**, sous 40, avec un seul de marge. C'est juste, mais cela tient, et la phrase « réduis les témoins libres et les familles de ton choix, jamais les blocs imposés » donne la parade.

**Taille : 55 000 suffit pour un contenu serré, pas pour un contenu bavard.** Estimation par `mes_essais/taille_40_temoins_v1.py` (programme sur disque) : ma sortie saine de la mission précédente, portée à 40 témoins au total (tête et bloc à l'écart), onze familles, textes faits de mots de six lettres :

| profil | texte par témoin et par famille | caractères | jetons à 2,5 car./jeton |
|---|---|---|---|
| court | 6 mots, formules de 60 car. | 40 549 | 16 220 |
| moyen | 20 mots, formules de 120 car., expressions de 160 | 51 467 | 20 587 |
| bavard | 30 mots (le maximum), formules de 200, expressions de 300 | 61 885 | 24 754 |

Même le profil court dépasse déjà les 40 000 d'avant (preuve que la borne devait monter). Le moyen tient dans 55 000 avec 3 500 de marge ; le bavard ne tient pas (déficit 6 900). L'auteur est averti de réduire ses textes si la place manque, et la lettre lui dit comment. Risque résiduel : une sortie qui dépasse 55 000 est « illisible » (taille) et ouvre le second essai payé. Je ne demande pas de changement : 55 000 est un choix de la mère lié au plafond de 32 000 jetons, et les lois imbriquées d'un vrai auteur peuvent peser plus que mes remplissages. À garder en tête.

Réserve sur les jetons : à 2,5 caractères par jeton la sortie bornée fait 22 000 jetons ; le dépôt a relevé ailleurs un rapport plus bas (2,227 sur un autre modèle, d'après le commentaire du collisionneur), et à ce rapport 55 000 caractères feraient 24 700 jetons, au-dessus des 23 808. Pour R2-a, le 2,5 vient d'un relevé chez le fournisseur lui-même (même commentaire) : acceptable, mais ce n'est pas une mesure sur du JSON.

**Suite à faire hors de ces pièces (erratum, § 5.1)** : mon programme de vérification de la sortie porte encore 28 et 40 000 (constantes `TEMOINS_MAX` et `TAILLE_MAX_CARACTERES`) ; il doit passer à 40 et 55 000, et compter les témoins **en tête et dans le bloc à l'écart ensemble** (il ne compte aujourd'hui que ceux de tête). Ses essais et son empreinte changent : version neuve.

## 4. Point 3 : le mot « indecise_a_la_borne »

Présent dans l'erratum, § 3, avec la phrase de la mère : issue du recalcul, jamais de l'auteur ; « famille écartée » pour la mise en fiches (point 2 du § 3). Son champ `issue_attendue` reste fermé sur trois valeurs, donc une sortie qui l'écrirait manque la forme. **Absent** du texte servi, du jeu de remplacements, du devis v4 et de la lecture (recherche sans réponse). L'erratum dit lui-même qu'il ne fixe pas la condition du recalcul, qui revient au programme de vérité. Conforme.

## 5. Point 4 : le devis v4 et sa lecture

- **Rejeu du programme v4, deux fois** (`python3 -B`, sortie redirigée) : `cmp` des deux sorties muet ; `cmp` avec `70e957ec…` muet.
- **Calcul de S2, refait à la main et par le programme :** 55 000 / 2,5 = 22 000 jetons ; 32 000 − 8 192 = 23 808 ; marge 23 808 − 22 000 = **1 808**, la sortie tient dans la lecture dure (provision dedans) ; à côté, marge 10 000. Entrée : 27 468 / 2,5 = 10 987,2, soit 10 988 (la requête compte des octets : borne haute).
- **Montants R2-a :** cas haut 2 × (10 988 × 10 + 40 192 × 50) / 10⁶ = 2 × 2,11948 = 4,23896, soit **4,24** ; pire 2 × (12 000 × 10 + 40 192 × 50) / 10⁶ = 4,2592 ; plafond par essai 2,1296 arrondi au-dessus à 2,13, soit **4,26** pour deux ; total 114,48 + 4,26 = **118,74**, marge 1,26 sous 120 ; cas bas S2 0,483952, soit 0,48. Les trois montants de la mission sont justes. R2-b (4,02 ; 4,04) et R3 (3,42 ; 3,44) aussi.
- La lecture ne rejoue pas le programme et le dit ; ses calculs à la main sont exacts. Sa ligne de GO pour S2 reprend à la lettre la ligne du devis v4 avec 32 000, 2,13 et 4,26.
- **Défauts du v4 pour un sceau :** (a) le texte dit encore que l'erratum porte la borne à 60 000, et cite la première passe `erratum-1-…-v3.md` (non scellée) et non la seconde `4dd1bb7f…` ; (b) il garde S0 et S1, une décision ouverte (« défaut : aucun ») et une ligne de GO à trois choix entre crochets, que la lecture, pièce de classe C, résout hors du devis ; (c) le programme (docstring, constante E1 « 60 000 ») garde l'état d'avant le choix de la mère ; (d) il se dit « non contre-lu ». Ces défauts n'altèrent aucun chiffre.
- **Avis : devis v5 réduit à S2, pas de sceau du v4 avec la lecture.** Un devis est une pièce décisive : la ligne que Lazar accorde doit se lire dans la pièce scellée elle-même, sans crochets et sans second texte qui en annule des morceaux. Le v5 doit citer l'erratum seconde passe et le texte servi par leurs empreintes (`4dd1bb7f…`, `2e675d74…`), ne porter que S2, une ligne de GO sans crochets, et rejouer le programme (version neuve, qui peut ne garder que S2). Le calcul est de l'arithmétique seule : peu de coût.
- À ne pas oublier au v5 : le GO-2026-11-21-16 déjà cité, l'empreinte `4286bf39…` du scellement de la conception et celle du devis v3 (`e9f9ecd8…`) sont reprises du v4 ; je ne les ai pas vérifiées ici.

## 6. Point 5 : noms et clés

Aucun nom de modèle ni de fournisseur dans l'erratum, le texte servi et le devis v4 (ni dans la lecture, le programme v4 et sa sortie). Les lettres « modèle F » de la signature ne sont pas un identifiant. Aucune clé. Seuls les journaux de remplacement (hors des trois pièces) portent des chemins de dossiers de travail.

## 7. Réserves

1. Les estimations de taille sont celles de remplissages ; elles n'éprouvent pas une vraie sortie. 2. Je n'ai pas lu les pièces citées par l'erratum (scellement de la conception, devis v3 scellé). 3. Le v5 n'est pas encore vu.

vérificateur du programme de vérification de la sortie des mondes, modèle S

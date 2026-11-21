# Contrôle différentiel de l'erratum v3, du texte servi v3 et du devis v6 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copies dans `v6/`.
- Portée, sur instruction de la mère : erratum v3 et texte servi v3 jugés en entier ; devis v6 limité au rejeu et aux deux taux, la mère ayant retenu un devis v7 à 4,30 qui sera contrôlé à part.

## 0. Verdict

1. **Erratum v3 : Conforme, prêt à sceller.**
2. **Texte servi v3 : Conforme, prêt à sceller.**
3. **Devis v6 : ne pas sceller ; remplacé par le v7.** Ses calculs sont justes et se rejouent à l'octet ; c'est son règlement de l'arrêt (§ 4) qui n'est pas garanti à 4,26.

## 1. Empreintes

Toutes égales à la table `a0a4d27b…` (fichier `table-empreintes-erratum-v3-et-devis-v6.txt`) : erratum v3 `1b57f1cc…`, jeu `d2584e6b…`, texte servi `f3d87162…`, devis v6 `d11b686d…`, programme `989430a5…`, sortie `62f771d6…` (le second jeu du rédacteur a la même empreinte).

## 2. Texte servi v3

- Rejeu par l'outil (`391db990…`) sur une copie du mandat v3 (`816313cb…`) avec le jeu v3 : « FAIT : 3 remplacement(s) », sortie `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008` ; **`cmp` muet** avec le texte servi.
- `diff` mandat v3 contre texte servi : trois différences exactement, le titre (« , erratum 1 appliqué »), la ligne 83 (« Quarante témoins au plus, imposés, libres et bloc à l'écart compris. ») et la ligne 136 (« 52 000 »).
- `diff` texte servi v2 contre v3 : la ligne 136 seule (55 000 devient 52 000). 27 468 octets, sous la garde de 30 000.

## 3. Erratum v3

- Porte 52 000 aux § 1, § 2 et dans le tableau des bornes ; plafond de quarante témoins inchangé. Tableau recalculé par moi : 60 000 donne 24 000 et 26 943 jetons ; 55 000 donne 22 000 et 24 697 ; 52 000 donne **20 800 et 23 350**, marges **3 008 et 458** sous 23 808. Exact.
- § 3, deux règles côté session : `indecise_a_la_borne` (issue du recalcul, jamais de l'auteur, vaut « famille écartée ») et le signe de l'écart de puissance (positif quand la proposition gagne sur la base). Cohérent avec le § 2 du mandat et la phrase du § 3.1 sur T05 et T07 (« n'est pas strictement positif »). La remarque finale (un témoin libre « lu comme T05 ou T07 » l'est par la session, non par l'auteur) est juste au regard de D-M16.
- **Les deux règles sont absentes du texte servi** : recherche de « indecise », « indécise », « signe », « gagne », « convention » dans le texte servi v3 : aucune occurrence ; le différentiel ne montre que les trois lignes ci-dessus. Elles sont aussi absentes du jeu de remplacements.
- Aucun nom de modèle ni de fournisseur dans l'erratum, le texte servi ni le devis (recherche faite sur les noms usuels et sur les noms de la table des espèces).

## 4. Devis v6 : rejeu et taux

- Programme v6 rejoué deux fois (`python3 -B`, sortie redirigée) : `cmp` muet entre les deux jeux, et avec la sortie livrée `62f771d6…`.
- Taux de 2,5 : sortie 52 000 / 2,5 = **20 800** ; marge 23 808 − 20 800 = 3 008 ; à côté 11 200.
- Taux de 2,227 : 52 000 / 2,227 = 23 349,8 → **23 350** ; marge 23 808 − 23 350 = **458** ; à côté 8 650. Entrée 27 468 / 2,227 → 12 335 ; garde 30 000 → 13 472. Oui, la marge de 458 est exacte. (Réserve 3 du devis : le taux au-dessous duquel la marge disparaît est 52 000 / 23 808 = 2,1841, que le devis arrondit à 2,185 : écart sans conséquence.)
- Montants refaits à la main : cas bas 0,459952 (2,5) et 0,51634 (2,227) ; cas haut 4,23896 et 4,26590 ; pire 4,2592 et 4,28864 ; justes.

**L'arrêt net, tel que le rédacteur le dit.** Il écrit que la dépense ne peut pas dépasser 4,26 parce que l'arrêt est net. D'après la règle du devis (§ 3, première ligne : le coût d'un essai est borné par les plafonds en jetons ; un second essai ne part que si « son pire tient dans ce qui reste ») :
- c'est vrai **si le pire du second essai est compté au taux prudent** : le texte servi étant fixe, un essai coûte au plus 2,13295 ; le second ne part que si 4,26 − coût du premier ≥ 2,13295 ; le total ne dépasse alors jamais 4,26 ;
- ce n'est **pas garanti tel que c'est écrit**, car le devis dit lui-même que son « pire par essai » est calculé au taux de la table (2,1296). Si la porte du second essai emploie ce pire-là, le second part dès que le reste dépasse 2,1296, et le total peut atteindre 2,1304 + 2,13295 = 4,26335, soit 0,34 cent de trop. Le plafond de 2,13 « par essai » n'est pas non plus appliqué en dollars par l'interface : un seul essai peut coûter 2,13295.
- La somme en jeu est minuscule, mais le mot « ne peut pas dépasser » n'est pas établi par le texte.

Un **devis v7 à 4,30** (2,15 par essai, total 114,48 + 4,30 = 118,78, marge 1,22 sous 120) répond : deux essais menés au bout coûtent au plus 4,2659 (texte servi) ou 4,28864 (garde d'envoi) au taux prudent, sous 4,30 ; le plafond tient le pire sans dépendre de la porte du second essai. Il est donc suffisant. Pour le contrôle du v7, je vérifierai : 2,15 et 4,30 dans la ligne de GO et dans la décision ; 118,78 et la marge de 1,22 ; que le plafond tient le pire aux deux taux ; que la sortie du programme est rejouée deux fois ; que le reste du v6 (texte servi et erratum cités par `f3d87162…` et `1b57f1cc…`, exception `4286bf39…`, options) ne change pas.

## 5. Réserves

1. Je n'ai pas vu le relevé du taux de 2,227 ; je l'ai pris comme donné. 2. Le calcul du programme n'est que de l'arithmétique. 3. Le v7 n'est pas encore vu.

vérificateur du programme de vérification de la sortie des mondes, modèle S

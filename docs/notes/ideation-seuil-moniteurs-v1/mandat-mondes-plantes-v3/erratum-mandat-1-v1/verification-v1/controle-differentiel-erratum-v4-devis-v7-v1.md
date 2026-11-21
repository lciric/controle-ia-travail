# Contrôle différentiel de l'erratum v4 et du devis v7 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copies dans `v7/`.

## 0. Verdict

1. **Devis v7 : Conforme, prêt à sceller.** Chaque point demandé est vérifié (§ 2). Seul écart de ce qui change, déclaré : le plafond de R3 « pour mémoire », exact.
2. **Erratum v4 : À corriger, deux corrections courtes** (§ 1). Il faut le dire avant tout envoi : **la lecture de la dérive de F est ambiguë** (§ 1). Si l'erratum change (v5), le devis v7 doit citer sa nouvelle empreinte dans la ligne de GO : un devis v8, sans autre changement.
3. Texte servi v3 : inchangé, `f3d87162…` (empreinte recalculée égale).

## 1. Erratum v4 et la lecture de la dérive de F

Empreinte `1f9e9077…` égale à la table `5f9dae39…` (qui est égale à son compagnon), au compagnon et au devis. Différentiel v3 → v4 lu en entier : le seul ajout de fond est le paragraphe « Troisième règle, la dérive de la famille F » ; le § 1 (les deux corrections), le plafond de quarante témoins, les deux règles précédentes, le texte servi et son jeu ne changent pas ; le § 4 cite le devis v7 et le plafond de 4,30. Le paragraphe est côté session et absent du texte servi.

**Cette lecture est-elle ambiguë ? Oui.**
- **« La session reconnaît le décalage par sa définition, non par un nom imposé »** (§ 3, point 2) ne dit pas comment. Le programme de vérification v2 que j'ai relu fait autre chose : il cherche, dans `valeurs_de_plus` de T09, la seule clé numérique dont **le nom** contient « decalage » ou « derive ». L'erratum dit « noms libres », le programme lit les noms : c'est une contradiction entre les deux pièces.
- **Essai** (sortie factice à moi, programme v2) : `valeurs_de_plus` de T09 = {« decalage_en_ecarts_types », « couverture_restante »} : lu (F convertie, 29 témoins sur 33). {« decalage_a », « derive_b »} : deux clés, rien n'est lu, F non convertie. {« delta »} seul : rien n'est lu. Une paire naturelle comme « decalage_en_ecarts_types » et « couverture_sous_derive » est donc refusée.
- **Reconnaître le décalage « par sa définition »** pourrait vouloir dire : le nombre qui, appliqué à la loi honnête de F, triple un taux de 1 %. Cela se calcule pour une loi donnée, mais aucune pièce ne le dit, ni le programme ne le fait.
- Un autre flou : le décalage lu est **cru** (il devient la dérive du générateur) ; le programme de vérité recalcule la couverture de T09 sous ce décalage, il ne contrôle pas que ce décalage triple bien le taux de 1 %.
- La proposition du rédacteur (point 3 : sans décalage lisible, F est écartée, non illisible) est cohérente avec le § 6, point 2 du mandat. Elle est lourde : F est une famille imposée, perdue pour une affaire de nom. Pas de second essai, puisque la sortie est lisible. À confirmer par la mère, comme le rédacteur le dit.

**Les deux propositions du rédacteur, tranchées par la mère, jugées comme décidées** : (i) F écartée si la lecture échoue, sortie non illisible : cohérent avec le § 6, point 2 du mandat et avec l'état du programme v2 (la sortie reste lisible) ; (ii) noms libres, texte servi non rouvert, le programme signale l'absence, la session lit le décalage et l'écrit dans son journal : cohérent avec l'erratum, **mais le programme v2 ne signale pas l'absence en vérification et lit par le nom** (voir ma pièce sur la v2). La correction E1 reste utile : elle dit **comment** la session reconnaît le décalage.

**Corrections demandées à l'erratum (v5) :**
- **E1.** Remplacer « par sa définition » par une règle opérationnelle que le programme appliquera à l'identique. Ma proposition, sans toucher au texte servi : parmi les nombres de `valeurs_de_plus` de T09, écarter ceux dont le nom dit « couverture », « taux » ou « probabilité » ; si un seul reste, c'est le décalage ; si plusieurs restent, retenir celui dont le nom dit « decalage » ou « derive » s'il est unique ; sinon, F est écartée. Le programme de vérification se met alors au pas (version neuve). Ou, plus fort, ajouter le contrôle « ce décalage triple le taux de 1 % sous la loi de F » et rapporter son écart.
- **E2.** Ligne 11 : un marqueur gras (`**`) est resté après « 52 000 caractères » ; le texte « Deux changements de la troisième passe : la borne… » est mal balisé. Cosmétique.

## 2. Devis v7

- Empreintes égales à la table : devis `23d8d655…`, programme `668bcad4…`, sortie `25ae72ea…` (second jeu du rédacteur de même empreinte).
- **Rejeu du programme v7 deux fois** : `cmp` muet entre eux et avec la sortie livrée.
- **2,15 par essai, 4,30, 118,78, 1,22** : plafond par essai = pire au taux prudent 2,14432 arrondi au cent supérieur = 2,15 ; fois deux = 4,30 ; 114,48 + 4,30 = 118,78 ; 120 − 118,78 = 1,22. Présents dans le § 0, le tableau du § 0, le § 2, la décision du § 5 (« 4,30 USD », « 0,46 à 4,30 ») et la ligne de GO (« plafond par essai 2,15 USD », « 4,30 USD »).
- **Pire de deux essais** : 4,2592 au taux de la table (12 000 × 10 + 40 192 × 50 = 2,1296, deux fois) et 4,28864 au taux prudent (13 472 × 10 + 40 192 × 50 = 2,14432, deux fois) ; sortie livrée : marges 0,0408 et 0,01136.
- **Le second essai tient dans le reste** : 4,30 − 2,1296 = 2,1704 ≥ 2,1296 ; 4,30 − 2,14432 = 2,15568 ≥ 2,14432. La sortie livrée porte `le_second_essai_au_pire_tient_dans_ce_reste: true` aux deux taux. Avec le texte servi réel (entrée de 12 335 jetons), un premier essai coûte au plus 2,13295 : la garantie tient a fortiori. La réserve 4 du devis (14 040 jetons, 2,137 caractères par jeton) est exacte.
- **La ligne de GO nomme** le texte servi `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008` et l'erratum, quatrième passe, `1f9e907744a6e1188c403e8f9266210718dbb334b85efe62420a2beeafd30951`, toutes deux en 64 caractères, égales aux fichiers.
- **Rien d'autre ne change** : le différentiel v6 → v7 du devis ne montre que le titre et l'en-tête, le plafond et ses conséquences (§ 0, § 2, § 5, réserve 4), la ligne E1 de la table des sources (erratum v4), la mention « quatrième passe » au § 3, et la ligne de GO. Cas bas, cas haut, pire, les deux taux, la borne de 52 000, les marges de 3 008 et 458 et le texte servi sont inchangés. Différentiel du programme : seule la fonction du plafond change, plus trois champs ajoutés à la sortie.
- **Écart déclaré, le plafond de R3 « pour mémoire »** : 3,48 (1,74 par essai). Refait : 12 000 → 13 472 jetons d'entrée au taux prudent, (134 720 + 32 000 × 50) / 10⁶ = 1,73472, arrondi à 1,74 ; fois deux, 3,48. Exact ; R2-b reste à 4,04 (2,01995 donne 2,02). R3 n'est pas proposé.
- Aucun nom de modèle ni de fournisseur dans l'erratum v4 ni dans le devis v7.

## 3. Réserves

1. Le taux de 2,227 n'est toujours pas vu. 2. Le devis cite l'erratum v4 par son empreinte : une correction E1 ou E2 la change et demande un devis v8.

vérificateur du programme de vérification de la sortie des mondes, modèle S

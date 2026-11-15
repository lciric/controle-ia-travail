# Addendum d'empreintes au préenregistrement de l'idée 1.2 (tirages répartis par blocs avec arrêt anticipé) — v1

- Texte auquel il s'ajoute : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
  (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`), ci-dessous **[T]**, lignes citées « l. n ». [T] l. 8-10 :
  « ses empreintes entrent dans un **addendum d'empreintes** scellé avant tout jeu, qui ne change rien d'autre ».
- Rédacteur : le développeur du code (sous-agent de la session mère), auteur des rapports [RD1] et [RD2] ; ni du texte, ni
  de ses relectures, ni des deux relectures du code, ni du juge. Date (UTC) : 2026-11-15, vers 12:30 (`date -u`).
  Dépôt lu sur `main`, tête `5a80299ca69e2cb83fecf27cefb75bba9b2d771d`. **Aucun jeu ; aucun résultat n'existe.**
- Pièces : rapport du développeur v1 **[RD1]** `docs/notes/organisme-idees-juge-v1/code-idee-1-2-v1/rapport-developpeur-v1.md`
  (`774fbf78b1a2c3af52502a5a43ea330c9ad6f7a9998225dfbbf646e127784a66`) ; v2 **[RD2]** `…/rapport-developpeur-v2.md`
  (`d02801755a1513f1b4abd028f47808ae39e041509352b350521d338109a65b04`) ; contre-lecture du code **[CL]**
  `…/contre-lecture-code-idee-1-2-v1.md` (`36ecc4a4cc97b1530d89a76aa0eed19ad4ce0f226fb5be1dcb9e6eba117c85f3`, « jouable
  après corrections ») ; relecture courte du code v2 **[RL]** `…/relecture-code-v2-idee-1-2-v1.md`
  (`ade839992c41105070cb974522bb2395d2488c6e8db9767d32f11da198d23eba`, « jouable ») ; registre R-2897, R-2899, R-2909.
- Ce que cet addendum **ne change pas** : aucune hypothèse, prédiction, métrique, seuil, bras, graine, étape, critère de
  lecture ni ligne de la liste d'arrêt de [T]. Il fixe le code par empreinte, déclare deux écarts, recopie des lectures
  du texte et des réserves, et dit la machine et la durée attendue.

## 1. Fichiers gelés (34) — le lanceur v2 refuse de partir si l'un d'eux diffère

Lignes au format de `sha256sum`, chemins relatifs à la racine du dépôt, rendues par
`python -I -B scripts/jouer_idee_1_2_v2.py --lister-empreintes` et vérifiées (`sha256sum -c` : 34 conformes) au commit
`5a80299c` ; égales au rapport [RD2] et à la vérification de [RL]. Elles couvrent le code de la v1 encore employé (inchangé),
le code de la v2, l'infrastructure importée, les dix fichiers d'essais et `tests/conftest.py`.

```
c29258ab0069320bbba33d3cdf8b652ba1ce254298b348e2c68ac03e83e6414e  src/controle_ia/organisme_idees_juge/__init__.py
853595cb44260eaaf16bf003f7a7b8155a3785e08c424573fcdaf40a6d1c487e  src/controle_ia/organisme_idees_juge/juge_v1.py
bf7e1f3e6cdbbebed681cf115e6d7e8031e670ffb14d82910d707a09f5b0e1fb  src/controle_ia/organisme_idees_juge/lois_v1.py
9cb63ff12d6198b3acd0ec979e798fe41268b2a50a8d90600614fd01284d65b9  src/controle_ia/organisme_idees_juge/banc_tirages_repartis_v1.py
34b6d356be3d717c7f0ab44711d4e1ee38926d6db6be4cd2a3a9684514db4350  src/controle_ia/organisme_idees_juge/oracle_v1.py
a1a08ef78c87ba8ffaa4147d53854dd4c17e6a70ec5b265cb406a858a49d1086  src/controle_ia/organisme_idees_juge/rejeu_v1.py
febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7  src/controle_ia/organisme_idees_juge/synthetique_v1.py
9c25699e280d9179d6c9a541711921a4861b8a129fe434de559b1a51526d4638  src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v1.py
77a74bf7f1e6fdc2fcb08267de90d16845e8b30b1c55762613e77f35a60bf15c  src/controle_ia/organisme_idees_juge/mutations_v1.py
d6da7373efca00b538407794bcd832f3f84970412e6200e49715d23455731747  src/controle_ia/organisme_idees_juge/execution_v1.py
a2a059b298ffc01b2746f32892f6390e46763ba88c665f2d840a56dc7801f640  scripts/jouer_idee_1_2_v1.py
0382ed81c0d65f83505b9790c8dbc48e5ab3d295ad038e639f6e1c2bded87a86  scripts/lire_idee_1_2_v1.py
b1743aeabe9db7dc6ba1d3eff4ebf15cc955924f1950802c78a3d9ef77fda288  src/controle_ia/organisme_idees_juge/verificateur_texte_v2.py
e569805463b8dd855b2633398af4d1a213d5b098cbc374063a682e4a627bee73  src/controle_ia/organisme_idees_juge/oracle_v2.py
18169a33917807c7ae019202f9ffdac656cccc66c0f1354bc33d710c78a4358d  src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py
bfabc7b2a6ba428041b0095487b5423901b5b8c1de771f500be519c75aad5a64  src/controle_ia/organisme_idees_juge/mutations_v2.py
ebee076b1ea55017541b5906b48bb3bfb567f250490144250fe0025f24249574  src/controle_ia/organisme_idees_juge/execution_v2.py
f66d4b05d2d05fd1932873211281582e2c8e714199d9bffbc167f9207d3442e0  scripts/jouer_idee_1_2_v2.py
ebac3ba06e1ce4484f3976235bd1a083be28f21299d795f97928bea97d9d9ae8  scripts/lire_idee_1_2_v2.py
a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439  src/controle_ia/gardes.py
93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2  src/controle_ia/scellement.py
1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d  src/controle_ia/manifeste.py
3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306  src/controle_ia/prereg.py
7c0b30aea0bbc1529a2d1400aa2c11bcb83dfd467c3c65a0b2d7f395d0f385e2  tests/test_organisme_idees_juge_lois_v1.py
565d4217d8bf4fd8c8ab9ab78d91b78313179a43f8b73c94c6031b592d8b1273  tests/test_organisme_idees_juge_banc_v1.py
faf94968a189e82f125dbef1b432f9e04870996af0b88493fe758993d782f7fd  tests/test_organisme_idees_juge_rejeu_v1.py
3606348964a9b00dd817ad6d442f76216b99817fb21843e20face9b37983c27a  tests/test_organisme_idees_juge_lecture_v1.py
14dfd455c963bf4ec84903e11cf4504a65dc2c9c8cecfcad50dbcb8c35fe2eb3  tests/test_organisme_idees_juge_mutations_v1.py
7e0f1bfb4dbc7c237ea0d6e783c1bb25ae110ce8553c15c65769743760998482  tests/test_organisme_idees_juge_execution_v1.py
d692555eceda79e300663da2f5003b9185ee4228740281b61799d07583d28720  tests/test_organisme_idees_juge_constantes_v2.py
f6c61e5114e378684c4d027fed36cd07dc2eaa9270b313086179a4a3494b6c11  tests/test_organisme_idees_juge_lecture_v2.py
bbf73075029c58f72ab947da43a2737490d09c8f66548c612c98ebd75c879ab5  tests/test_organisme_idees_juge_mutations_v2.py
5c15df7089625e8c205ceb8beb51d7a611f2795e978cd015410b1c40ada79fac  tests/test_organisme_idees_juge_execution_v2.py
a1bbfcc935007934dda9b038fb9f187f7627816fd18514b5aabc77715aaedca5  tests/conftest.py
```

Lanceur du jeu : `scripts/jouer_idee_1_2_v2.py` (ligne ci-dessus), commande
`python -I -B scripts/jouer_idee_1_2_v2.py --addendum prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md`
(deux processus par défaut). Lecture gelée : `scripts/lire_idee_1_2_v2.py --manifeste runs/<run>/manifeste.json`, après le
scellement de la sortie. Le jeu peut être lancé depuis une copie propre, détachée, du commit qui porte cet addendum : le
manifeste en consigne le commit ; ses sorties scellées sont recopiées octet pour octet dans le dépôt et vérifiées par leurs
compagnons avant toute lecture.

## 2. Écarts au texte scellé — déclarés comme écarts, **soumis au mot de Lazar**

- **E-1 — lieu du code.** [T] l. 460-461 nomme `docs/notes/organisme-idees-juge-v1/code-v1/banc_tirages_repartis_v1.py` et
  `lire_banc_tirages_repartis_v1.py`. Le code est sous `src/controle_ia/organisme_idees_juge/` (ces deux noms, plus les
  modules voisins de la v1 et de la v2 listés au § 1) et les lanceurs sous `scripts/` : les habitudes du dépôt
  interdisent d'exécuter depuis `docs/`. Aucun calcul ne change ; la traçabilité est tenue par les 34 empreintes ci-dessus.
  [CL] et [RL] : sans effet sur le calcul, acceptable si déclaré ici. **Soumis au mot de Lazar.**
- **E-2 — monde jouet du jeu synthétique tiré par génération, graine `(97, g)`.** [T] l. 309-312 : « monde jouet construit
  comme l'essai de [CL] (programme `01c648a0…` …), graines `(97, g)` ». Le programme `01c648a0…` tire les lois du monde
  jouet (S1, S2, P = 0,4·S1 + 0,6·S2, les 24 cartes voisines) **une seule fois** ; le code (`synthetique_v1.py`) tire, pour
  chaque génération g, **ses lois et ses issues** de la seule graine `(97, g)` que le texte donne. Mêmes formes, même maximum
  de vraisemblance par bissection, même plancher par la loi du monde, même plafond de log e à 50 (O3). Effet : la mise à
  mort de la mutation « valeur e lue au maximum de la trajectoire » se lit sur un mélange de mondes jouets plutôt que sur un
  seul ; échec du côté sûr (si la mutation survivait, le lanceur dirait « pas de jeu »). Sur racine d'essai : lecture saine,
  moyenne 0,444, intervalle [0,398 ; 0,497] ; lecture mutée, moyenne 2,536, borne basse 2,364. [CL] : la lecture la plus proche
  de la lettre, acceptable si déclarée. **Soumis au mot de Lazar.**

## 3. Lectures du texte faites par le code

Les dix-huit lectures de [RD1] (section « Lectures du texte faites par le code »), jugées fidèles par [CL], valent ici telles
quelles. La lecture 14 est complétée et trois lectures s'ajoutent ([CL], mineurs 6 et 7 ; [RD2]) :

14. *(complétée)* Essai E1 : les 50 cartes sont les 24 de T g = 0, les 24 de N g = 0 et les deux premières de T g = 1 ;
    remplacement déterministe y → (y + 1) mod 3 au-delà de t ; aucune clé de graine neuve. Elles sont toutes dans les
    cellules 0 et 1 (V1) et, pour la famille N, dans le monde M₀ : la lettre de [T] l. 469 (« 50 cartes couvrant chaque
    sorte ») est tenue, mais aucun monde M₀′ ni aucune cellule V2 à V5 n'y est essayé ; l'égalité de préfixe tient à
    l'évaluateur, non à la loi de la carte.
19. Famille T : la loi de base des trois « copies de la classe » tempérées et inclinées est tirée uniforme parmi S1 à S4
    (`banc_tirages_repartis_v1.py`) ; [T] l. 394-395 ne le précise que pour la famille N (l. 417).
20. Bras P′ : la phase 2 (blocs restants à tour de rôle sur l'ensemble élargi) commence au tour max(tour de fin de la phase 1,
    8), non au tour qui suit (`rejeu_v1.py`, `bras_P_prime`).
21. Étiquette d'arrêt d'une carte : ordre haut, plafond, bas, fin ; sous P et P′, une carte arrêtée bas qui a repris reste
    étiquetée « bas » ; les parts d'arrêts de ces deux bras se lisent avec cette réserve (`rejeu_v1.py`, `jouer_bras`).

## 4. Réserves

- **Réserve neuve ([RL], point 1) — mort d'un fils oisif.** Si un processus fils meurt alors qu'il **attend** une tâche (il
  tient le verrou de lecture de la file), la mort est vue et `GardeArret` est levée, mais la fermeture du pool
  (`Pool.terminate`, `multiprocessing/pool.py`, `_help_stuff_finish`) attend ce verrou sans fin : **le parent reste
  bloqué, sans `arret.json`**, et la garde des 24 h n'est plus relue. Un fils n'est oisif qu'en fin de phase (l'un a fini
  sa dernière tâche, l'autre non) : quelques dizaines de secondes, trois fois dans le run (E1, oracle, jeu). Rien n'est alors
  lu (pas de `jeu.json` ; le lecteur v2 refuse sans `journal.json`) : échec du côté sûr. **Consigne d'opérateur** : si
  `journal.json` n'est pas écrit à la durée attendue (§ 5) et que les processus du run n'emploient plus le processeur,
  envoyer le signal TERM **au processus parent, par son PID** (`kill -TERM <PID>` ; jamais par motif de ligne de commande,
  R10) ; le lanceur lève alors `GardeArret` et écrit `arret.json` ([RL] : sortie en 9,6 s, aucun fils restant) ; **run
  invalide** ; relance seulement sous un texte ou un addendum neuf ([T] l. 512). Le PID du parent est noté au lancement.
- Détection d'un fils mort par l'attribut `Pool._pool` de CPython (version des essais : Python 3.13.18) ; absent : arrêt,
  aucun repli ([RL] 9 a).
- Une tâche bloquée **sans** mort de fils n'est bornée que par la garde des 24 h ([T] l. 513), relue toutes les 5 s
  ([RL] 9 b).
- Avertissements de Python (`DeprecationWarning` : `fork` dans un processus à plusieurs fils d'exécution) dans les deux
  essais « fils mort » seulement ; le chemin sain n'en produit pas ([RL] 9 c).
- Les messages de deux gardes de `rejeu_v1.py` portent une allocation ou une valeur e ; ils ne sortent que sur défaut, dans
  un run arrêté et invalide ([CL], mineur 9 ; gardés).
- La lecture (3) du jeu réel n'a aucun plafond ; seul le jeu synthétique plafonne log e à 50 (O3).
- Le banc de mutations avec la racine du texte, l'essai E1 sur les 50 cartes réelles et le jeu lui-même ne sont pas encore
  joués : le lanceur les joue, dans cet ordre, après les essais.

## 5. Machine et durée attendue

- **Lot de la machine** : 4 cœurs partagés (Intel Xeon à 2,10 GHz, 4 processeurs logiques), chargés par d'autres
  processus le jour des mesures (charge moyenne de 10 à 13). Le jeu emploie **deux processus de calcul** (le parent attend
  sans calcul), `nice -n 10`, une file de calcul par processus ([T] l. 473) ; mémoire faible ; processeur seul, aucun
  réseau, 0 dollar (R-2851).
- **Durée attendue** (mesures de [RD1], [CL], [RL]) : contrôles avant jeu ≈ 15 min (dix fichiers d'essais ≈ 10 à 12 min sous
  charge, banc de mutations avec le jeu synthétique de 20 000 générations ≈ 3 à 4 min) ; E1 ≈ 20 à 35 min ; oracle
  ≈ 0,5 h ; jeu ≈ 2,3 à 4,7 h sur machine libre (13 à 27 s de processeur par génération, 1 250 générations, deux
  processus). **Total ≈ 3 à 5,5 h sur machine libre ; ≈ 6 à 7,5 h sous une charge comme celle du jour.** Borne dure 24 h
  ([T] l. 513), dont la marge reste de trois fois au moins. Le Coût écrit au texte (l. 519-524) sous-estimait le temps
  processeur de trois à six fois ([RD1]) ; ce n'est pas un critère.

## 6. Essais et mutations (comptes, corrigés)

- Suite des dix fichiers d'essais : **167 passés sur 167** ([RD2] : 690 s ; [RL] : 564,5 s). Essais d'infrastructure : 30 sur 30.
- Banc de mutations v2 : 24 sur 24 tuées pour la raison attendue ([RD2]).
- Mutations de [CL], rejouées sur les dix fichiers (greffons de son annexe A, empreintes égales), **les deux inexactitudes
  de [RD2] corrigées** ([RL], point 7) :

| mutation | sort | comptes | essais qui la tuent |
|---|---|---|---|
| 1 — A lit le bloc suivant hors de la garde d'accès | tuée | 58 échecs, 4 erreurs | `rejeu_v1` 28, `constantes_v2` 28, `execution_v1` 1, `execution_v2` 1 ; erreurs : bancs de mutations v1 (3) et v2 (1) |
| 2 — placebo ciblé | tuée | 50 échecs, 4 erreurs | `rejeu_v1` 23, `constantes_v2` 25, `execution_v1` 1, `execution_v2` 1 ; erreurs : bancs v1 (3) et v2 (1) |
| 3 — intervalle à 90 % | tuée | 4 échecs, 1 erreur | `test_niveau_de_l_intervalle_epingle`, trois essais de `lecture_v2` ; erreur : banc v2 |
| 4 — seuil d'arrêt bas à 1/10 | tuée | 35 échecs, 1 erreur | `test_seuils_du_texte_epingles`, `test_constantes_du_texte…`, **29 des 30** `test_troisieme_ecriture_egale_au_moteur` (une graine ne sépare pas les deux seuils), `…voit_un_seuil_partage`, `verifier_generation…`, deux essais de `execution_v2` ; erreur : banc v2 |

## 7. Ordre avant le jeu

Cet addendum scellé et versé ; arbre de travail propre au commit qui le porte (ou copie détachée propre de ce commit) ; mot
de Lazar sur E-1 et E-2 ; jeu par le lanceur v2 ; sortie scellée ; lecture gelée v2 ; lecteur neuf (R13) et audit de
symétrie (R4) écrit avant le prononcé ([T] l. 475).

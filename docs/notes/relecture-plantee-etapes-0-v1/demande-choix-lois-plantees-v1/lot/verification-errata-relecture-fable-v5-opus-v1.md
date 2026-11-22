# Vérification des errata portant la relecture de Fable 5.2 (v5) et le mot du directeur (GO-2026-11-21-87, point 2) — v1

- **Classe B** (vérification). Auteur : Claude Opus 5.5 (`claude-opus-5-5`), vérificateur neuf, qui n'a écrit aucune des pièces vérifiées. Écrit le 22 novembre 2026, sur la branche `prep/plantee-etapes-0-v1`. Processeur seul ; aucun appel payant ; ni commit ni poussée ; aucune autre pièce modifiée.
- **Objet** : six errata, sous `docs/notes/plantee-etapes-0-v1/` :
  - lois plantées : `conception-etape-0-lois-plantees-v1-erratum-2.md` (K-1 à K-7) et `preenregistrement-admission-etape-0-lois-plantees-v1-brouillon-erratum-2.md` (Q-1 à Q-9) ;
  - dommages plantés par un tiers : `specification-depouillement-v2-erratum-2.md` (S2-1) et `preenregistrement-campagne-dommages-tiers-etape-0-v2-brouillon-erratum-2.md` (B2-1, B2-2) ;
  - tâches floues : `conception-etape-0-taches-floues-v2-erratum-3.md` (points 1 à 13) et `preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-3.md` (points 1 à 6).
- **Sources contre lesquelles on vérifie** : les trois relectures de Fable (`docs/notes/relecture-plantee-etapes-0-v1/sortie-relecture-*-reduit-v5-v1/relecture-fable-api.md`) ; les tables de remplacement (`table-remplacement-v1.json`, `-extraits-v1.json`, `-taches-floues-v1.json`) ; `registres/go.md`, ligne 686 (GO-2026-11-21-87) ; la note des nœuds `registres/essaim/vers-mere/plantee-noeuds-pour-le-directeur-2026-11-21-v1.md` (`6e025417…1b879a`) ; R-4734 de `registres/decisions.md` et le constat qu'elle cite (`constat-compatibilite-noyau-adjudant-a7-v1.md`, `08181319…b076d`) ; les pièces amendées (originaux et errata précédents) ; pour les mots des options de D-2 à D-5, la conception de l'étape 0 des lois plantées, § 8.
- **Cloisonnement** : rien lu sous `archives-reponses-modeles/`, `quarantaine/`, `matiere-premiere/` ; aucun fichier des deux termes réservés du mandat ; aucune annexe réservée. Aucun refus d'outil.

## Méthode (par programme)

Un analyseur extrait, de chaque erratum, le lieu, l'ancien et le nouveau texte de chaque point (blocs ```` ```text ```` pour les lois plantées, lignes citées `> ` ailleurs). Pour chaque point :

1. **Ancien, une fois à l'octet** : compte de l'ancien dans la pièce qu'il amende (original ou erratum précédent), et, quand il amende le « nouveau texte » d'un point d'un erratum précédent, compte dans ce seul nouveau texte ; compte de contrôle dans l'original (doit être 0 quand l'ancien vient d'un erratum).
2. **Nouveau = texte de Fable ramené** : les paires (ancien, nouveau) des relectures de Fable, après remplacement inverse de la table (« du directeur » → « du directeur », « au directeur » → « au directeur », « le directeur » → « le directeur »), comparées à l'octet aux paires des errata.
3. **Copies lues par Fable** : chaque fichier des lots `lot-*-reduit-v1/` comparé à l'original, soit identique, soit égal à l'original passé par `table-remplacement-v1.json`.
4. **Mot du directeur** : chaque nouveau texte qui porte un nœud tranché comparé aux mots de l'option dans la pièce qui l'écrit (conception, § 8 ; conception des tâches floues, § 10 ; constat A7).
5. **Nœuds à garder ouverts** (A3 = N-4, A4 = N-7, A5 = N-15, B1 = D-6) : recherche de tout texte qui les dirait tranchés.
6. **Empreintes** : `python3 -m controle_ia.scellement verifier` sur les six errata, les trois relectures et les trois tables (tous « OK », code de sortie 0) ; chaque empreinte de 64 signes citée dans les en-têtes des errata recalculée sur disque (toutes retrouvées, aucune introuvable).

Résultats bruts : chaque ancien compte **1** dans sa pièce cible et 1 dans le nouveau texte du point visé ; **0** dans l'original quand il vient d'un erratum. Les 7 paires de Fable (lois plantées), les 6 citations de Fable (dommages) et les 5 paires de Fable (tâches floues) se retrouvent toutes, à l'octet, chacune dans un seul point d'erratum. Les 19 copies lues par Fable qui ont un original sont identiques ou égales après table.

## 1. Lois plantées — **conforme**

- **Fable, point 1 (B-2, marques D-4)** → Q-1 à Q-4 : textes de Fable ramenés par la seule paire « du directeur » → « du directeur », à l'octet. **Fable, point 2 (I-6)** → Q-5, à l'octet. **Fable, point 3 (I-9)** → K-1 (conception, C-7) et Q-6 (admission, P-11), à l'octet. Aucune correction de Fable omise.
- **Mot du directeur** : K-2 (D-2), K-3 (D-3), K-4 (D-4), K-5 (D-5) et Q-7 reprennent mot pour mot l'option (a) écrite au § 8 de la conception (lignes 224 à 230), aux seuls articles et liaisons près (« (a), le témoin par strates… » pour « (a) Le témoin par strates… ») ; K-6, K-7 et Q-9 remplacent les mentions « en attente » par « mot reçu ». D-4 et D-5 sont bien ceux que la note des nœuds range en section C, et que GO-2026-11-21-87 tranche.
- **Nœuds ouverts** : D-6 (B1) reste nœud sans défaut dans les deux errata ; aucun texte ne le dit tranché.
- **Point signalé par l'écrivain, jugé : les marques laissées sous la règle de Q-8.** Le texte d'admission (erratum 1) porte 60 marques « [en attente du mot du directeur : D-…] » (32 « D-2 », 15 « D-3 », 9 « D-4 », 3 « D-2, D-3 », 1 « D-n » dans la règle même), plus les 4 que Q-1 à Q-4 ajoutent ou complètent. Q-8 ne les réécrit pas, et pose une règle de lecture (« se lit « mot du directeur reçu : D-n (a), GO-2026-11-21-87 » »). Jugement : **acceptable**. La règle découle de P-1 lui-même, qui ne prévoit de réécriture que si le mot retient une autre branche que (a). Elle évite soixante points de remplacement sans rien changer au fond. Le choix de retirer ou de garder les marques au texte scellé reste un nœud ouvert, au concepteur, et non un choix de l'écrivain. La lecture des marques à plusieurs nœuds (« D-2, D-3, D-4 ») se déduit de la règle sans ambiguïté. Côté conception, les trois mentions « en attente » qui portaient sur D-2 à D-5 (C-4, C-9, C-13) sont toutes traitées (K-6, K-7, K-4) ; la quatrième (ligne 317 de l'erratum 1) est une définition du glossaire.
- **Relevés de Fable sans texte** (extension de l'interdit de C-7 et P-11 ; niveau 0,0009 prêté au devin à uns-chauds à P-21 ; B-3 non jugé faute du brouillon) : non portés, et rangés en « Nœuds encore ouverts », à la mère ou au concepteur. C'est conforme à « rien n'est ajouté ». Le relevé P-40 (contre-lecture réécrite, déclarée « sans remarque ») n'appelle rien.

Points : aucun bloquant, aucun important, aucun mineur.

## 2. Dommages plantés par un tiers — **conforme**

- **Fable, correction 1** → S2-1 : « S-1 à S-14 bis, S-16 à S-26 » → « S-1 à S-26 ». L'ancien figure une fois dans l'erratum 1 de la spécification (ligne V-2 de la table) et 0 fois dans la v2. Aucun terme des tables : repris tel quel.
- **Fable, correction 2** → B2-1 et B2-2 : à l'octet après la paire « du directeur » → « du directeur » (premier passage seulement ; les anciens ne contiennent aucun terme des tables). Chaque ancien figure une fois dans l'erratum 1 du brouillon et 0 fois dans la v2.
- **Mot du directeur** : GO-2026-11-21-87, point 2, ne tranche rien sur ce banc. A3 (N-4), A4 (N-7) et A5 (N-15) sont écrits ouverts dans les deux errata. N-14 passe de « Tranché » à « Appliqué d'ici le mot du directeur, non tranché », comme Fable le demande.
- **Ce que l'écrivain n'a pas réécrit** : la phrase « « À l'octet » s'entend d'un appel qui passe cette garde. » reste dans le corps de N-14, alors que le « Reste ouvert » demande désormais si elle peut s'entendre ainsi. Restent aussi la même lecture en G-5 des gardes et « V-3 portée / N-14 porté » au tableau final de l'erratum 1. Jugement : **pas un défaut de l'erratum**. Fable ne donne aucun texte pour ces lieux. Sous l'en-tête « appliqué, non tranché », la phrase se lit comme la règle appliquée à titre provisoire, et la question reste posée. L'écrivain le déclare en « Nœuds encore ouverts » : à porter avant le scellement (section 4).

Points : aucun bloquant, aucun important, aucun mineur.

## 3. Tâches floues — **conforme**

- **Fable, points 1 à 3** → conception, points 1 à 3. Les anciens sont pris dans les textes neufs de l'erratum 2 (points 26, 6, 19 : compte 1 dans l'erratum 2, 0 dans la v2 et l'erratum 1). **Fable, points 4 et 5** → brouillon, points 1 et 2 (erratum 2, points 11 et 2 : compte 1). Les cinq textes sont à l'octet, sans terme des tables. Aucune correction omise.
- **Mot du directeur** :
  - B2 (a) → point 5 : l'option (a) du nœud 1, mot pour mot.
  - B3 (a) au devis → points 6, 7 et 8 : « rejeu au loin », retenu pour le devis ; le devis et son GO restent à venir.
  - A6 acceptée → conception, point 13, et brouillon, point 5.
  - A7 (a) sous le constat R-4734 → conception, points 9 à 12, et brouillon, points 3 et 4. La condition (« noyau écrit d'emblée en socle commun avec un sommet d'étage par emploi », « inscrite au texte qui commande le code ») et les quatre réserves (registre et journal ; numpy ; cas sain de l'issue ; racine des graines hors du manifeste) reprennent R-4734. Les détails (« chaque sommet portant son schéma servi, ses champs d'engagement et ses tests », « jamais écrit pour le seul adjudant, puis augmenté », `creer_manifeste` sans liste de tâches, essai sans racine dans le manifeste) sont les mots du verdict d'ensemble et des points 3 et 5 du constat. Rien n'est ajouté au-delà.
  - Les anciens des points 5 à 9 et 11 à 13 (conception) et 4 et 5 (brouillon) comptent 1 dans l'original et 0 dans les errata 1 et 2 ; ceux des points 10 (conception) et 3 (brouillon) comptent 1 dans l'erratum 1 (E5).
- **Nœuds ouverts** : nœud 3 (ce que F6 rapporte), rouvert ; nœud 2 (forme fixe, défaut sous 48 heures, non échu) ; nœud 9. Aucun des nœuds A3, A4, A5, B1 ne relève de ce banc. Aucun nœud que le GO ne tranche n'est dit tranché.
- **Point signalé, jugé : le complément au § 0, point 7, dans un lieu séparé (point 4).** Le point 4 amende le texte neuf du point 2 du même erratum. Son ancien (« ce que F6 rapporte reste ouvert (nœud 3). ») figure une fois dans ce texte neuf, et 0 fois dans la v2 et dans les errata 1 et 2. Le lieu le dit (« texte neuf du point 2 ci-dessus »). Jugement : **acceptable, et préférable** à une fusion. Le point 2 reste le texte de Fable à l'octet, et le point 4 porte seul le mot du directeur, chacun avec sa source. Le complément est demandé par les sources : sans lui, le § 0 compterait encore les nœuds 6 et 8 parmi les conditions ouvertes, contre le mot. L'ordre d'application est sans ambiguïté : le point 4 suppose le point 2 appliqué.
- **Brouillon, point 6** (empreintes des errata 3 au texte scellé, ajout sans ancien) : même forme que l'erratum 2, point 3 ; ajout à la fin du point 7 des « Conditions de scellement » ; suite mécanique des points 1 à 5. **Acceptable.**
- **Brouillon, point 4** : le lieu dit « après l'ajout de l'erratum 1, E1 ». L'erratum 1 ajoute sans position au même point « Code ». Le libellé fixe l'ordre des deux ajouts. **Acceptable.**

Points : aucun bloquant, aucun important, aucun mineur.

## 4. Ce qui reste avant le scellement de chaque préenregistrement

**Lois plantées (texte d'admission de l'étape 0)** :
1. Au concepteur, à fermer avant le scellement : les seuils des quatre tests d'indépendance sans modèle (P-12, P-21, P-35, P-37), et la liste des traits du devin neuf avec son seuil, la définition du rang et les fiches lues (P-23).
2. Au concepteur : l'instant de comparaison de l'horodatage de la garde 2, et la question de savoir si les tirages sont remis avec la racine (Q-5) ; les gardes 5 et 8 (P-39) ; les marques, retirées ou gardées (Q-8) ; si D-6 suspend aussi le scellement.
3. À la mère : l'accord propre à l'étape 0 (GO-2026-11-21-66 à confirmer, P-4) ; la variante « programme d'admission écrit et contre-lu avant le scellement » (P-2) ; les relevés de Fable sans texte. Parmi eux, l'étiquette [calcul, F] du niveau 0,0009 prêté au devin à uns-chauds (P-21) est à vérifier contre la sortie v2 avant tout scellement, faute de quoi ce serait un chiffre non vérifié dans un préenregistrement. Restent aussi l'extension de l'interdit (C-7, P-11) et les verdicts 5 et 15 (B-3).
4. Puis : composer le texte scellé sous un nom neuf, avec les errata 1 et 2 et les empreintes, et le sceller avant le tirage de la racine d'admission (D-5 (a)). Les nœuds 1 et 2 étant écrits par le concepteur, leurs textes neufs passent par la chaîne de classe A.

**Dommages plantés par un tiers (préenregistrement de la campagne)** :
1. Le mot du directeur sur N-4 (A3) et N-7 (A4), qui bloquent le scellement (vérification v2, point 4), et sur N-15 (A5) : le point (1) avant le codage du dépouillement, le point (2) avant le scellement.
2. N-14 : le mot du directeur, ou une pièce de la mère qui porte le mandat sous GO-2026-11-21-84. Puis la mise en cohérence de la phrase « « À l'octet » s'entend… » (corps de N-14, G-5) et du tableau final de l'erratum 1 (« V-3 portée », « N-14 porté »), par le concepteur.
3. Les lieux que Fable n'a pu juger : l'ordre d'abandon de G-4 et du bloc L contre les NOTES [v3] (calculs v2, bloc C) ; les artefacts 5A bis et 12A bis (spécification v2, § 5.1, § 5.3) ; le contenu de D-5 (a) dans M-1 (note source, § 8). Les ajouts déclarés au-delà des remarques : les plafonds du critère 3 (E-5, bloc K), et le détail de la garde commune, non vérifiable dans les pièces jointes (G-1, G-3, G-5, M-3).

**Tâches floues (texte d'admission de l'étape 0)** :
1. Condition 3 : ce que F6 rapporte (nœud 3), à dire par la session orchestratrice ; le scellement attend cette réponse. À la même occasion : la phrase de l'erratum 2, point 24 (§ 9, point 7, « F6 ne rapporte que la chute de l'acceptation de l'honnête »), et le bloc I des calculs v3 (« rapportée, sans exigence »), qui portent le choix (code, classe B).
2. Condition 2 : le nœud 2 (écarts à la forme fixe). Son défaut sous 48 heures, « acceptés », court depuis la remise au directeur (21 novembre, vers 21:40Z) : à consigner à son échéance, au plus tôt le 23 novembre vers 21:40Z.
3. Condition 1 : la vérification des corrections par le même contre-lecteur, sans remarque ouverte. Condition 4 : la décision sur F4, à consigner au registre des décisions (B5 de la note des nœuds).
4. Le relevé de Fable sans texte (erratum 2, point 2 : le constat 21 n'y est pas listé ; la couverture des lieux de la v2 qui nomment A2, les plantations de F6 ou « 128 »), à la mère.
5. Condition 7 : le texte scellé, sous un nom neuf, porte les empreintes des errata 1, 2 et 3 des deux pièces et des calculs v3.

## Bilan

| banc | verdict | bloquants | importants | mineurs |
|---|---|---|---|---|
| lois plantées | conforme | 0 | 0 | 0 |
| dommages plantés par un tiers | conforme | 0 | 0 | 0 |
| tâches floues | conforme | 0 | 0 | 0 |

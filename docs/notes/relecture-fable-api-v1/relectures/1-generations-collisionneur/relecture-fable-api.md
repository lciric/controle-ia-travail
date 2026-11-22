# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v2` (empreinte du module c8e8506f8d7cb9487173090aa9a000c1ab217377946f55cb338a45f07ca3d7f3)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGmR7HSWv11sHayvWw3X`
- Heure (UTC) : 2026-11-21T21:31:47Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `docs/notes/relecture-fable-api-v1/envois/1-generations-collisionneur/consigne-relecture-v1.md` — sha256 77ff51c882a35eaa20f5bd4c3538b3aa9ec9327b99a2cd2eb1a8a29759dc48ed (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/1-generations-collisionneur/conception-generations-jusqu-au-plateau-v3.md` — sha256 98b665bfe3e2cdce7dae96f359b4e08521b6237e43aeb79b0c7deac228192a98 (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/1-generations-collisionneur/calculs-devis-et-seuils-generations-v3.py` — sha256 157c1da46554e31e068571897a90a19f68bf6dd2fa995772f1d72f3c7d9affd3 (compagnon : vérifié)
  - correction : `docs/notes/relecture-fable-api-v1/envois/1-generations-collisionneur/calculs-devis-et-seuils-generations-v3-sortie.txt` — sha256 b05616c52faff5e0ecd278fc01e5375243a3c0fe4a7bd151933bcf3fe2497ef3 (compagnon : vérifié)
  - remarques : `docs/notes/relecture-fable-api-v1/envois/1-generations-collisionneur/verification-corrections-conception-generations-opus-v1.md` — sha256 ce4ddd49e88573467512ac6c4655c1d044322cf273b2726a1db3e496bdff18b2 (compagnon : vérifié)
  - avant : `docs/notes/relecture-fable-api-v1/envois/1-generations-collisionneur/conception-generations-jusqu-au-plateau-v2.md` — sha256 3bdf19b9c515eaf9bd14732f9165bade15907c1074f7ae28c07ef869574f8003 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 78cb6e5e80d412f447a6d2fb29c4cb8804da758fe7b1d978994b3573cf75fea3
- Jetons : entrée 111853, sortie 106068 (dont réflexion 102592), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 5.137544 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
à corriger

Une seule correction, de rédaction, au nœud 2 : la ligne insérée pour le point B a changé ce que désigne la fin du nœud. Le reste est porté exactement et rien de neuf n'est conçu. Je n'ai rien exécuté : comptes, positions et sommes sont refaits à la main sur les copies jointes. La v3 est comparée à la v2 à la lecture, pas à l'octet ; je n'y ai relevé aucun autre écart.

## Remarque par remarque

**Point A : porté exactement.**

- Le correcteur prend la première des deux corrections offertes, la seule qui ne change pas la garde, et renvoie la seconde au nœud ouvert 1.
- Les deux formes entrent en 9.10, et par cohérence en 3.3 (« quatre témoins ») et à l'annexe B (« quatre faux positifs connus »). `FORMULES` n'est pas touchée.
- Annexe, section 9 : 28 pièces, soit 3 + 3 + 4 + 18, comptées dans le code. Suivis dans `garde_identite`, les deux témoins neufs donnent chacun un refus et aucun signalement, à la position 34 pour « such as » et 51 pour « tu as », comme dans la sortie.
- L'écart de méthode est dit, et il est exact : seule, la phrase de la vérification fait 44 caractères, donc une ligne de bord courte, et donne deux refus (signature en 0, formule en 3).
- Deux nuances, sans correction demandée :
  - la prolongation « , ce qui reste à établir par une mesure. » n'était pas nécessaire, une ligne du milieu n'étant jamais une ligne de bord ;
  - le commentaire du code dit « les deux phrases sont celles de la vérification » sans mentionner cette prolongation, que la note mentionne.

**Point B : porté sur le fond, une phrase à reprendre.**

- Les neuf constantes du nœud 2 sont celles des sections 5.2 et 6.2, aux mêmes valeurs. L'empreinte citée pour l'annexe est celle du tableau de la consigne.
- Les deux corrections offertes (énumérer les neuf, ou dire que l'accord porte sur toutes) sont appliquées ensemble ; elles ne se contredisent pas.
- La ligne sur les seuils de l'audit et de la recopie ne tranche rien et renvoie au nœud ouvert 2, comme il le fallait.
- Défaut introduit : cette ligne est placée juste avant « Enjeu : ils décident… », gardé tel quel de la v2. « ils », « posés » et « les geler tels quels » se rattachent maintenant aux seuils de l'audit et de la recopie, sujet de la phrase qui précède. Un accord « (a) » peut alors se lire comme gelant aussi ces quatre seuils, ce qui trancherait le nœud ouvert 2 par glissement. C'est l'objet même du point B : ce que couvre un accord donné sur le texte du nœud.

**Observations 1 et 2 : non portées, à bon droit**, et inscrites à la table. L'observation 1 touche pourtant les constantes 5 à 7 : la façon de compter une lignée non jugeable dans l'alerte reste à dire, alors que le nœud 2 fait geler ses seuils.

## Ajouts hors des remarques

Aucun ne conçoit quoi que ce soit.

- **Tenue de version** : en-tête, table de la v3, écart de méthode, nœuds ouverts, « Historique : version 2 », alinéas des « Pièces lues ».
- **Phrase d'en-tête sur le nombre de générations** (« deux au moins, trois au plus sauf son mot ») : c'est une glose, pas une citation. Elle s'accorde avec les sections 5.3 et 6.1, et le mot exact reste cité plus bas.
- **Accord GO-2026-11-21-84** : il est cité entre guillemets alors que « le registre des accords n'a pas été ouvert ». La source de la citation n'est pas dite. Elle s'accorde avec ma consigne ; je n'ai pas vu l'accord.
- **Parenthèse sur la formule « as » non ancrée**, en 3.3 et 9.10 : elle reprend les mots de la remarque.

## Nœuds ouverts : recommandations, sans trancher

**Nœud ouvert 1, ancrer « as » en tête de phrase.** Recommandation : ne pas ancrer pour le pilote. Confiance : 70 %.

- Un faux positif coûte une lecture et un `--admettre`, inscrits à la filiation. Un ancrage laisserait passer sans bruit une auto-désignation en milieu de phrase (« Speaking as Claude, I… ») : avec un nom nu, ni refus ni signalement.
- La section 3.3 dit déjà que la branche (a) penche du côté du refus.
- Le pilote donnera le nombre de refus d'identité admis. S'il est élevé, une exclusion étroite (« such as », « tu as ») serait à préférer à l'ancrage.
- À verser au même nœud, lu dans le code et non exécuté : la même formule prend aussi « selon moi, [un modèle] » et « pour moi, [un modèle] », plus probables en français que « tu as ». Cette forme n'est ni dans la vérification ni dans les faux positifs connus. Ce n'est pas un défaut de la v3, mais la liste reste incomplète.

**Nœud ouvert 2, geler les seuils de l'audit et de la recopie.** Recommandation : oui, avec les neuf, dans le même accord, nommés à part comme seuils de réserve. Confiance : 75 %.

- Ils sont posés par Fable comme les autres : la raison du gel vaut pour eux.
- Le directeur peut arrêter une chaîne à deux sur le rapport ; les réserves font partie de ce qu'il lit.
- Le coût est nul : ce sont déjà des constantes de la note, et `plateau` refuse si un recalcul diffère.
- La décision devrait dire aussi si le 0,90 des « énoncés presque identiques » (section 5.5, hors décision) suit.

C'est le mot du directeur qui tranche, puisqu'il s'agit de l'étendue de son accord.

## Calculs refaits

Tous concordent avec la sortie et avec la note.

- **Sections 1 à 4 ter** : tous les montants, au centime, en prenant pour la garde d'entrée « jetons × 1,01 + 32 » (la tolérance qu'imprime la sortie). Je n'ai pas vu les fonctions du script de la version 7 : c'est une reconstruction, mais elle rend chaque chiffre.
- **Sections 5 et 5 bis** : les seuils en nombres et les cinq cas exacts.
- **Section 6** : les 24 issues, suivies dans `normaliser_enonce`.
- **Section 7** : la formule donne un carré latin pour tout N ; les ordres affichés pour cinq propositions sont justes.
- **Section 8** : les longueurs au plafond et le rapport 2,65.
- **Section 9** : les comptes (28 pièces, 20 et 15 mots témoins), les dix pièces saines ou faux positifs, les positions des signatures.
- **Section 10** : 64 994 caractères, et les sept valeurs attendues par (1 − 3p)/(1 + 3p).
- **Note** : 77 à 85, 432 à 473, 509 à 558 ; 86 et 68 valent bien deux lignes.

## Ce que je n'ai pas pu vérifier

- Les empreintes elles-mêmes : les copies sont nettoyées. J'ai seulement contrôlé que les empreintes citées sont celles de la consigne.
- Que l'annexe v3 égale la v2 hors des changements dits, et que `normaliser_enonce` soit « égale à celle de la version 2 » : l'annexe v2 n'est pas jointe. Les indices concordent (26 pièces devenues 28, 35 mots témoins, mêmes chiffres que la note v2).
- Les similarités de la version 1 (`SequenceMatcher`), les valeurs mesurées de la section 10, les deux lancements identiques à l'octet.

## Correction demandée

Section 10, nœud 2. Remplacer :

> Enjeu : ils décident de ce que le rapport prononce et de l'arrêt sur alerte ; posés par Fable, qui est dans la course, ils ne sont « fixés par un tiers » que si tu les gèles. Options : (a) les geler tels quels pour le pilote : simples, mais sans étalonnage ; (b) en changer avant la première génération 2.

par :

> Enjeu : les neuf constantes décident de ce que le rapport prononce et de l'arrêt sur alerte ; posées par Fable, qui est dans la course, elles ne sont « fixées par un tiers » que si tu les gèles. Options : (a) geler les neuf telles quelles pour le pilote : simples, mais sans étalonnage ; (b) en changer avant la première génération 2.

La correction ne touche que la note : l'annexe, sa sortie et leurs empreintes citées restent valables.

**Facultatif, hors verdict.** Si la mère veut que tout choix en attente figure aux nœuds ouverts, ajouter après le nœud ouvert 2 :

> 3. **Lignée non jugeable : comment compte-t-elle dans l'audit symétrique et dans l'alerte de convergence ?** (observation 1 de la vérification). La vérification lit la section 5.4 ainsi : comptée pour les conditions 2 et 4, exclue des conditions 1 et 3 ; le verdict n'en dépend pas, mais l'audit symétrique et l'alerte en dépendent. Les seuils de l'alerte sont des constantes du critère (nœud 2). Choix de conception ; cette version ne le tranche pas, et le développeur rend ce cas à la mère.

# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHtiaJw6evuzqDxW1icK`
- Heure (UTC) : 2026-11-22T11:34:59Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/consigne-relecture-taches-floues-reduit-v1.md` — sha256 6058f04b1392b55e6c1c933513ac67f64e3d89915e01ea063647028987e7593f (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/conception-etape-0-taches-floues-v2-erratum-1.md` — sha256 2abce1158e80ed95c74fb2cca292b41d567069231c0fb41a76cbad1f9f3eb796 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-1.md` — sha256 618785119d801c233e25e8d474f79871aeb10b4627672f3c9be0832c776d49b5 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/conception-etape-0-taches-floues-v2-erratum-2.md` — sha256 5411b30a295a40fe8bc16955392e72866b7041ef87f6de95bcce45e4f0f5fde5 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-2.md` — sha256 217a992ba85a7de39d5fd40755dca4bcd662004ea1100e184f30a49cb6873db9 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/extrait-differences-calculs-etape-0-taches-floues-v3-contre-v2-py-v1.md` — sha256 9b35de76ce877ebdf1987478b6cb329dae6f166dad3c88a6e8f3b5769123c910 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/extrait-differences-calculs-etape-0-taches-floues-v3-contre-v2-txt-v1.md` — sha256 ef4bc519709c1fc109b5233aa3c7218b03377217430d1f8b60a1c66f42adc49b (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/complement-v1/extrait-passages-calculs-etape-0-taches-floues-v3-txt-v1.md` — sha256 8903ebc1e0ea5daf93e1ade1fcac8a94936c39e456fb21ce957edc3dc1c904f8 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/essai-garde-g1-erratum-1-v1.py` — sha256 87c3df206a36e2e4bc4bf38a6eabd4a580313458354b68cd9f1961e2bbd4399f (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/essai-garde-g1-erratum-1-v1.txt` — sha256 1c965b0e7ce473f69cdab78428c44748bf65b20d5cb904300033abd623db9090 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/recalcul-e3-erratum-1-v1.py` — sha256 a558d1743e433dacda6a4822223decd8b03226b891b6a37a4e1987d4925c4ab0 (compagnon : vérifié)
  - correction : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/recalcul-e3-erratum-1-v1.txt` — sha256 08dc289daa60e89d7493ac951e4ffca2e99b2d3163c266ab14fedf7f74d11c68 (compagnon : vérifié)
  - remarques : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/verification-corrections-etape-0-taches-floues-v2-opus-v1.md` — sha256 726cd2cc45a5f70fa39ab90b61c49ba5a5b0699929178aa5bc881fa582a3e631 (compagnon : vérifié)
  - remarques : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/verification-erratum-1-etape-0-taches-floues-opus-v1.md` — sha256 0a9074c0538946784b37caba18f3956395228fabb7055338cf10e86c9e79d03d (compagnon : vérifié)
  - remarques : `docs/notes/relecture-plantee-etapes-0-v1/lot-taches-floues-reduit-v1/remarque-monde-jumeau-perime-v1.md` — sha256 58d8f05971cd7aba6250f3f286c4f4772dbc33d1c6d8e11906121c21d4be16f4 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 8f0504111ec24a0507720e69a549d8a7d10b2a3228b0340e39aad24ff250b18f
- Jetons : entrée 60240, sortie 19023 (dont réflexion 15500), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 1.242840 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
à corriger (1 point)

| Remarque | Lieu de la correction | État | Motif |
|---|---|---|---|
| Constat 5, porté en partie = E1 (important) | erratum 1 conception, E1, lieux 1 à 3 ; erratum 1 brouillon, E1 ; essai de la garde et sa sortie | conforme | |
| E2 (mineur) | erratum 1 conception, E1 lieu 3, et E2 | conforme | |
| E3 (mineur) | erratum 1 conception, E3 ; erratum 1 brouillon, E3 ; recalcul E3 | conforme | |
| E4 (mineur) | erratum 1 conception, E4, lieux 1 et 2 ; erratum 1 brouillon, E4 | conforme | |
| E5 (mineur) | erratum 1 conception, E5, lieux 1 et 2 ; erratum 1 brouillon, condition 5 | conforme | |
| Vérification de l'erratum 1, § 4, réserve (a) | aucun : renvoyée à la contre-lecture du code (classe B), non au texte scellé | conforme | |
| Vérification de l'erratum 1, § 4, réserve (b) | aucun : même renvoi | conforme | |
| Note de la mère : repli (F6 sans plantation, témoin retiré) | erratum 2 conception, points 1 à 26 ; erratum 2 brouillon, points 1 à 20 ; calculs v3 | conforme | |
| Note de la mère : réserve de l'auteur (ce que F6 rapporte) | erratum 2 conception, points 6, 19, 26 ; erratum 2 brouillon, points 2 et 11 | à corriger | Le choix de la grandeur rapportée, que les pièces ne tranchent pas, est écrit dans le texte à sceller, et le nœud 3 est fermé sans nœud ouvert. |

Pièce d'avant nécessaire : erratum 2 conception, point 2 (constat 21 n'y est pas listé, alors que le point 8 retire la phrase sur la dérive alignée) ; plus largement, je ne peux pas vérifier que tous les lieux de la v2 qui nomment A2, les plantations de F6 ou « 128 » sont couverts.

Calculs v3 :
- Chaque bloc différent répond au repli : en-tête, P, D, I, L, N, K, Q.
- Les lignes « arrondis dans le bon sens » du bloc K appliquent la règle d'arrondi par excès de E3 aux totaux.
- Aucun nombre cité par un erratum ne diffère de la sortie extraite.
- Le bloc I imprime « rapportée, sans exigence » : il porte le même choix que le point à corriger.

Note de la mère : les errata 2 portent le repli à la lettre (F6 sans plantation, A2 retiré, mot du repli cité tel quel), mais ils fixent en plus la grandeur que ce mot désigne.

Réserve de l'auteur :
- La chute n'existe pas pour la grandeur que les errata 2 retiennent : l'acceptation de l'honnête par T2 monte de 0,0014 dans F6 (sortie v3, ligne 240).
- Une baisse existe seulement pour l'estimation de la clause d'abstention sur le jumeau seul (lignes 156 et 157). Le bloc B, ligne 64, appelle cette grandeur « acceptation […] d'un honnête de même loi que le jumeau ».
- Les quatre nombres sont dans les extraits et désignent ce que la note dit : 0,9420 et 0,9406 (ligne 240 ; 0,9406 aussi aux lignes 67 et 148) ; 0,9040 (ligne 157) ; 0,9405 (lignes 67, 150 et 156).
- La réserve change le verdict sur les errata 2. Deux lectures du mot du repli sont possibles ; les pièces ne tranchent pas, et la réserve n'est ni un nœud du § 10 ni une condition de scellement.

Ajouts sans remarque :
- Erratum 1, E1, étape 0 : `sys.dont_write_bytecode = True` et lancement par `python -I` ; sans remarque à l'écriture, acceptés ensuite par la vérification de l'erratum 1 (§ 3, point 1).
- Erratum 1, E1, étape 6 : « Un code 97 levé à l'échauffement est un défaut de la liste ou du lanceur […] Il n'accuse pas le témoin » ; aucune remarque ne demande cette règle d'imputation, couverte seulement par le « porté juste » d'ensemble.
- Erratum 2 conception, « Arrondis » : signalement que les 0,0260 et 0,974 de la v2 étaient arrondis au plus proche ; simple signalement, la v2 n'est pas corrigée ailleurs.
- Errata 2, conception point 19 et brouillon point 11 : la grandeur rapportée par F6 est fixée (acceptation de l'honnête par T2) ; c'est le point à corriger.

**À corriger — un point, cinq lieux**

1. Erratum 2 de la conception, point 26 (§ 10, nœud 3), nouveau texte.
Ancien : « 3. *F6 avec ou sans plantation* (écart 7) : tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729. »
Nouveau : « 3. *F6 avec ou sans plantation* (écart 7) : tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729. *Reste ouvert, pour la session orchestratrice : ce que F6 rapporte.* Le repli écrit dit « la chute de l'acceptation de l'honnête ». Sous les lois écrites, l'acceptation de l'honnête par T2 ne chute pas (0,9420 dans F6 contre 0,9406 dans F0 [calcul v3, I]) ; ce qui baisse est l'estimation de la clause d'abstention faite sur le jumeau seul (0,9040 contre 0,9405 [calcul, E]). Non tranché ici. **Le scellement attend cette réponse.** »

2. Erratum 2 de la conception, point 6 (§ 0, point 7), nouveau texte.
Ancien : « les nœuds du § 10, dont trois conditionnent le scellement (forme fixe, banc de l'adjudant ou banc à part, règle de rejeu). Le nœud du monde F6 est tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729. »
Nouveau : « les nœuds du § 10, dont quatre conditionnent le scellement (forme fixe, ce que F6 rapporte, banc de l'adjudant ou banc à part, règle de rejeu). La plantation de F6 est tranchée : sans plantation, par la vérification de recouvrement, consignée en R-4729 ; ce que F6 rapporte reste ouvert (nœud 3). »

3. Erratum 2 de la conception, point 19 (§ 5, « Règle d'admission », point 4), nouveau texte.
Ancien : « toute abstention de T2 hors de F4 ; dans F6, joué sans plantation, l'acceptation de l'honnête par T2, que le repli nomme « la chute de l'acceptation de l'honnête » (0,9420 attendu, contre 0,9406 dans F0 ; sous les lois écrites, elle ne chute pas [calcul v3, I]) ; »
Nouveau : « toute abstention de T2 hors de F4 ; dans F6, joué sans plantation, ce que le repli nomme « la chute de l'acceptation de l'honnête » : la grandeur rapportée reste à dire par la session orchestratrice (nœud 3 du § 10, ouvert). Valeurs calculées, sans choix : acceptation de l'honnête par T2, 0,9420 contre 0,9406 dans F0 [calcul v3, I] ; estimation de la clause d'abstention sur le jumeau seul, 0,9040 contre 0,9405 [calcul, E] ; »

4. Erratum 2 du brouillon, point 11 (« Rapportées, sans exigence »), nouveau texte.
Ancien : « D1 sur la seconde part de F2 ; toute abstention de T2 hors de F4 [calcul, A, B, H] ; dans F6, joué sans plantation, l'acceptation de l'honnête par T2, que le repli nomme « la chute de l'acceptation de l'honnête » (0,9420 attendu, contre 0,9406 dans F0 [calcul v3, I]). »
Nouveau : « D1 sur la seconde part de F2 ; toute abstention de T2 hors de F4 [calcul, A, B, H] ; dans F6, joué sans plantation, ce que le repli nomme « la chute de l'acceptation de l'honnête » : la grandeur rapportée reste à dire par la session orchestratrice (nœud 3 de la conception, ouvert). Valeurs calculées, sans choix : acceptation de l'honnête par T2, 0,9420 contre 0,9406 dans F0 [calcul v3, I] ; estimation de la clause d'abstention sur le jumeau seul, 0,9040 contre 0,9405 [calcul, E]. »

5. Erratum 2 du brouillon, point 2 (« Conditions de scellement », point 3), nouveau texte.
Ancien : « 3. Le nœud 3 de la conception (monde F6 avec ou sans plantation) : tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729. Le texte scellé porte les deux errata 2, de la conception et de ce brouillon. »
Nouveau : « 3. Le nœud 3 de la conception : la plantation de F6 est tranchée (sans plantation, par la vérification de recouvrement, consignée en R-4729) ; ce que F6 rapporte reste ouvert, et ce brouillon n'est pas scellé tant que la session orchestratrice ne l'a pas dit. Le texte scellé porte les deux errata 2, de la conception et de ce brouillon. »

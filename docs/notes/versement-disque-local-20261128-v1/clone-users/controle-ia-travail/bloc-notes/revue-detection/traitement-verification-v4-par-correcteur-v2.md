# Traitement des vérifications de la synthèse v4 « comment détecter » (tour 3), par le correcteur v5 — v2

v2 (correcteur v7, session 16, 2026-10-21) : seule la colonne « écart » de VV4-sens-04 change, en mots exacts de VV5-fidelite-08
(`…/revue-detection/verification-v5-fidelite/verification-v5-fidelite-v1.md`, `05472092…`) : ce n'est pas un écart ; le compte de 13
écarts du bilan était juste, la table le montre désormais. La v1 (`21e1d56c…`) reste intacte (R12).

Session 16, 2026-10-20, à partir de 23:30 UTC environ. Correcteur neuf : je n'ai écrit ni la v1, ni la v2, ni la v3, ni la
v4, ni les extractions, ni les vérifications, ni les traitements. Consigne :
`…/revue-detection/consigne-correcteur-v5-v1.md`. `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Rapports traités (empreintes recalculées, égales à la consigne) :
- fidélité : `…/revue-detection/verification-v4-fidelite/verification-v4-fidelite-v1.md`
  (`982ed742550658aac71fc3bb41e1fb291d126d6d2a445ad768c5671908be4808`), « conforme après corrections », 12 constats
  (1 moyen, 8 mineurs, 3 de forme) ; fichiers de travail lus (`travail/`) ;
- sens : `…/revue-detection/verification-v4-sens/verification-v4-sens-v1.md`
  (`84d549f7d14a11d9eb27fd9d84766929dfdbbffd4a9fadf5f024f12e87fddafc`), « conforme après corrections », 16 constats
  (1 majeur, 5 moyens, 8 mineurs, 2 de forme).

Entrée : v4 `…/revue-detection/synthese-comment-detecter-v4.md` (`fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a`,
inchangée). Sortie : v5 `…/revue-detection/synthese-comment-detecter-v5.md`
(`17069e06f2f4d1a50f556c097a9278af3b2fc0d951b4d4cdd754998db3ab413d`, 565 lignes). Différentiel :
`…/revue-detection/correction-v5/appliquer_corrections_v5.py` (48 remplacements exacts, chacun trouvé une seule fois,
v4 contrôlée par empreinte ; rejouable). « l. » ci-dessous = ligne de la v5.

**Bilan.** 28 constats sur 28 appliqués ; aucun non appliqué. 13 appliqués avec un écart déclaré aux mots exacts (colonne
« écart »), dont 3 fusions de deux corrections qui portaient sur la même phrase (VV4-fidelite-01 avec VV4-sens-05 ;
VV4-fidelite-08 avec VV4-sens-02 ; VV4-fidelite-03 avec VV4-sens-13). Aucune idée ajoutée ; aucun chiffre neuf de la
littérature. Faits du dépôt relus à la source pour appliquer les constats : document de P-015
(`docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md`, `6e74c6cb…`, compagnon égal, l. 16-17, 36-44, 91-100,
115-126, 153-155) ; brouillon de T0.6 (`brouillons/T0.6-organismes-v0-v1-brouillon1.md`, `e212fb35…`, l. 74-81) ;
[P] (`d975e981…`) l. 236-253 et 270-280 seulement ; registres aux versions `38579d98…`, `cc1b108d…` (par `git show`,
lecture seule) et à la version vivante (`e8b73c64…`, `1a392407…`).

**Contrôle à la page.** Chaque phrase anglaise et chaque chiffre de la littérature que la v5 reprend des deux rapports :
`…/revue-detection/correction-v5/controles_v5.sh` (outil `pagev5.py`), sortie `sortie-controles-v5.txt` : 55 trouvés à
la page citée, 0 absent ; épreuve R5 : 6 artefacts (chiffre changé, mot changé, page voisine, colonnes permutées), 6
rejetés. PDF de `[D]` lus après empreinte complète ; les PDF de `[N]` et `[X]` (K, LB, AU, DYL, RH, CC, MA, BU, LIAR, FQ)
manquent au bloc-notes restauré (vérifié sur disque, R11) : leurs pages sont lues sur les extraits texte de
`…/revue-detection/txt-nouveaux/` et `…/revue-detection/extraction/txt-representations/`, sans empreinte du PDF.

## Une ligne par constat

| constat | gravité | décision | ce qui a changé | passage de la v5 | écart aux mots exacts |
|---|---|---|---|---|---|
| VV4-fidelite-01 | moyen | appliqué, fusionné avec VV4-sens-05 | « rien de publié ne le passe » retiré ; analogues de T1 lus (modestes sur ce modèle : 0,81, 0,63, 0,606) ; « aucun travail lu ne mesure T1 contre un plancher apparié (R8 : question) » | section 5, confiance, l. 368-371 | fusion : texte de VV4-sens-05, plus « modestes … 0,606 [YS p. 3] » et « aucun travail lu » de ce constat ; « un contraste de ce type » devient « T1 » (mot de VV4-sens-05). La raison neuve vient des rapports : la déclarer comme jugement de la session n'a plus d'objet ; l'en-tête (VV4-fidelite-10) déclare les raisons des confiances |
| VV4-fidelite-02 | mineur | appliqué | version des registres de la v4 (`cc1b108d…`, `05e7fccd…`), lignes décalées, chemin et empreinte du brouillon de T0.6 | en-tête, Sources, l. 55-60 ; table E3, coût, l. 340 | placé après la fin de l'énumération de la v3 (l. 54), non au milieu (la l. 34 de la v4 coupait la liste) ; « non recalculée ici » devient « recalculée pour la v5 : égale » (empreinte `e212fb35…` recalculée) |
| VV4-fidelite-03 | mineur | appliqué, fusionné avec VV4-sens-13 | P-015 « en propose le périmètre » (registre l. 392, `cc1b108d…`) ; estimation de son document citée avec lignes et empreinte ; nœud au-delà de 10 USD ou du plafond de 150 USD ; recharge (R-283) | table E3, coût, l. 340 ; Dépense, l. 431-435 | l. 284 de la v4 : mots du constat, plus l'estimation du document de P-015 (l. 115-125), comme le constat le demande « si le document de P-015 donne une estimation » ; l. 350-351 de la v4 : version de VV4-sens-13, qui a lu P-015 (voir ce constat) |
| VV4-fidelite-04 | mineur | appliqué | bras « moyenne » (iii) ajouté au titre du nœud, à la recommandation (2) et à la dépense | l. 348 ; l. 396 ; l. 426 ; l. 417 | « ni l'une ni l'autre » devient « aucune de ces extensions » (trois objets) |
| VV4-fidelite-05 | mineur | appliqué | « [DYL] rapporte … classé par Artificial Analysis … » avec la phrase de [DYL] p. 5 | section 1, point 1, l. 103-106 | aucun |
| VV4-fidelite-06 | mineur | appliqué | « seule comparaison lue » | rang 6, l. 263 | aucun |
| VV4-fidelite-07 | mineur | appliqué | « P3 n'avait aucune de ces conditions. » rétabli | section 1, point 2, l. 114 | aucun |
| VV4-fidelite-08 | mineur | appliqué, fusionné avec VV4-sens-02 | « entre consignes » remplacé par « contre le témoin Alpaca » (consigne, sujet et forme différents) | point 1, l. 97-99 ; rang 4, l. 261 ; E2, l. 339 | fusion avec le texte de VV4-sens-02 ; au rang 4 et dans E2, « la même sonde » devient « la sonde de question apprise sur « Roleplaying » » (sans antécédent dans la cellule) |
| VV4-fidelite-09 | mineur | appliqué | 0,5 de [BX] typé T1 ; 0,653 de [AU] « type non établi » | point 2, l. 129, l. 133 ; rang 3, l. 260 | aucun |
| VV4-fidelite-10 | forme | appliqué | déclaration de la v4 corrigée (jugements de la session ; « sections 1 à 5 ») ; confiance « puis de la session pour la v4 » | en-tête, l. 20-26 ; section 5, l. 364 | aucun |
| VV4-fidelite-11 | forme | appliqué | « et, au champ, T1 ne vaut qu'avec T4 » | section 5, l. 366-367 | aucun |
| VV4-fidelite-12 | forme | appliqué | (a) virgule retirée, « (S-18) » ; (b) « sur le modèle de P3 (Llama-3.1-8B-Instruct) » ; (c) « réponse honnête moyenne au-dessus de 99,9 % d'Alpaca, sonde Pairs » | (a) l. 295-296 ; (b) l. 132 ; (c) l. 118-119 | (b) étendu aux trois autres « ce même modèle » que l'ordre neuf du point 1 et du point 2 rendait ambigus (après [DYL] table 9 et [BU]) : l. 109, l. 125, l. 138 |
| VV4-sens-01 | majeur | appliqué, en deux versions (consigne, point 3) | E2 sur T0.6 : la condition qui réplique P3 est exclue par le T0.6 que recommande P-015 (b) ; inconvénient ajouté à l'option (b) du nœud E2 ; recommandation (3) et nœud E2 écrits selon l'issue de P-015, marqués **[Décision de Lazar en attente : P-015]** | table E2, tranche, l. 339 ; recommandation (3), l. 349-357 ; nœud E2, l. 404-413 | les mots du constat sont répartis entre les deux versions ; version 1 (condition gardée) : (b), confiance ≈ 55 % de la v4, « à revoir » ; version 2 (P-015 (b) sans condition de référence) : pas de recommandation de ce correcteur, « n'a de réponse que par (a) », confiance à revoir. P-015 n'est pas tranchée ici |
| VV4-sens-02 | moyen | appliqué | troisième type « contre la conversation ordinaire » sorti de P3-P3 (0,03 de [BX] ; plus de 99 % de [AP] p. 18) ; [KU p. 5, p. 9] ; « hypothèse … contre le témoin » | point 1, l. 97-99 ; point 2, l. 131-133, l. 137-139, l. 141-142 ; rang 3, l. 260 ; rang 4, l. 261 ; E2, l. 339 | au rang 3, colonne « littérature », « rappel 0,03 » est aussi déplacé hors de « type P3-P3 » vers le troisième type (le constat ne réécrivait que la colonne « pouvoir ») |
| VV4-sens-03 | moyen | appliqué | point 1 : « à consignes différentes » / « à consigne égale », contre-cas de [DYL] p. 11 ; rang 4 et E2 : même séparation | point 1, l. 90-96 ; rang 4, l. 261 ; E2, l. 339 | aucun |
| VV4-sens-04 | moyen | appliqué | prédiction de E2 sur la lecture principale (« Backdoors », sonde Pairs : 0,832 et 0,849 contre 0,768 et 0,844) ; même ajout au nœud E2, option (a) | E2, tranche, l. 339 ; nœud E2, l. 401-403 | aucun (le constat demande une phrase ; elle est faite de ses mots) |
| VV4-sens-05 | moyen | appliqué, fusionné avec VV4-fidelite-01 | voir VV4-fidelite-01 | section 5, l. 368-371 | « aucun ne mesure » devient « aucun travail lu ne mesure » (R8). Confiance revue : gardée à 15 à 25 %, la baisse depuis la v1 tenant à l'ajout de T1 (« Seule l'addition de T1 justifie la baisse », VV3-sens-09, cité par VV4-fidelite-01), non à la raison retirée |
| VV4-sens-06 | moyen | appliqué | jeu (2) de E3 : actions générées par le modèle, étiquette par le coût écrit ensuite, jamais des paires écrites qui ne diffèrent qu'au champ ; coût : génération du jeu (2) | table E3, quoi, l. 338 ; coût, l. 340 | aucun |
| VV4-sens-07 | mineur | appliqué | réglage de [DYL] ; [YS] apprise sur « Roleplaying » ; sujet confondu des analogues de T1 ; [BU] parmi les analogues de P3-P3 | point 2, l. 121-127 ; rang 3, l. 260 | au rang 3, clés écrites en entier dans la cellule ([DYL p. 8], [YS p. 2]) |
| VV4-sens-08 | mineur | appliqué | contrastes de [OA] et [CA] typés | point 1, l. 88-90 ; rang 4 ([OA] seul, [CA] n'y est pas cité), l. 261 ; E2, l. 339 | aucun |
| VV4-sens-09 | mineur | appliqué | « taille dans une famille », « indice de capacité » ; [LB] non ordonnée ; [DYL] table 9, indices 9 à 14 : 0,64 à 0,84 ; Nemotron-3 Nano, 3 milliards actifs | point 1, l. 100-108 ; rang 5, l. 262 | aucun |
| VV4-sens-10 | mineur | appliqué | prédiction de E2 : question générale sur 8 milliards, perte prédite par [CA p. 8] | E2, tranche, l. 339 | aucun |
| VV4-sens-11 | mineur | appliqué | Bonferroni sur saboteur contre honnête ; P3-P4, T1, T3, T4 à 95 % sans correction ([P] l. 278, relue) | règles communes, l. 282-284 | aucun |
| VV4-sens-12 | mineur | appliqué | seuls saboteur contre honnête déjà vus ; le reste neuf ; règle neuve du nombre minimal de paires pour T4 | table E1, l. 338 ; règles communes, l. 316-317 | « (T2 » garde le renvoi « [P] l. 242 » de la v4 |
| VV4-sens-13 | mineur | appliqué, avec VV4-fidelite-03 | témoin et mention obligatoires dans P-015 (l. 41-44) ; dépense de T0.6 selon P-015 (l. 16-17, 99-100, 125) | table E2, contrôle, l. 342 ; Dépense, l. 433-435 | « absents du brouillon » non repris : le brouillon a un « témoin instruit » (l. 78) ; gardé « n'a pas de mention », ajouté « témoin et mention obligatoires dans P-015, l. 41-44 ». « le plafond » devient « le plafond de 10 USD par lancement » (P-015 l. 16-17 parle de la borne par lancement, pas des 150 USD) |
| VV4-sens-14 | mineur | appliqué | raison de l'option « A2 » tombée (sans plancher par jeton, que P3b ajoute) | nœud « Revendication », l. 383-384 | aucun |
| VV4-sens-15 | forme | appliqué | chaque renvoi aux registres porte sa version (`38579d98…`, `94ebe409…`, `cc1b108d…`) et l'identifiant de la ligne | l. 297 ; l. 338 ; l. 381 ; l. 387-388 ; l. 398 ; l. 427-432 ; l. 445-448 ; l. 340 | aucun |
| VV4-sens-16 | forme | appliqué | titre « Nœuds de Lazar, proposition à défaut, rappel » ; « correction de la v3 » ; « faux positif » remplacé ; [AP] p. 23 « lue au dernier jeton » | l. 375 ; l. 445 ; l. 142, 259, 266, 271 ; l. 111, l. 261 | « faux positif sur P3-P3 » devient « prédit sur P3-P3 un « au-dessus » qui lirait la consigne, pas l'acte, et non un nul » (ordre des mots) ; aussi dans le résumé « ce qui a changé » (l. 271) |

## Ajouts de la v5 hors constats (consigne, points 4 et 6)

- En-tête : puce « v5 », ligne R7 de la v5 (l. 27-40, l. 77-82) ; section 3 : une ligne « v5 » (l. 253-254, l. 273-276) ;
  fichiers de la v5 (fin du document).
- Section neuve « Décisions prises depuis la v4 » (l. 464 et suivantes), lue dans `registres/decisions.md` (`e8b73c64…`,
  tête `9ecd952`) et `registres/go.md` (`1a392407…`) : R-290 à R-305, GO-2026-10-20-09 à -12, P-015 à P-020, N-030 ;
  seulement ce qui touche la revue, ligne citée. Renvois vers elle dans le nœud E2 (GO-2026-10-20-10) et la dépense
  (GO-2026-10-20-11). Le corps garde l'état de la v4, corrigé des constats.

## Ce que la session doit encore trancher

1. **P-015** (Lazar ; défaut (b) le 2026-10-22 vers 14:30 UTC) : choisit la version de la recommandation (3) et du nœud
   E2 ; dans la version « P-015 (b) sans condition de référence », recommandation et confiance du nœud E2 restent à
   écrire par le rédacteur.
2. **Divergence P-017 / v4** : la v4 recommande d'ajouter la manipulation du nombre à N-028 (≈ 50 %) ; la session
   recommande (B), la sonde de valeur (≈ 55 %), défaut (A).
3. **Table E1 et nœud E2 à jour** : la lecture « double comptabilité » (GO-2026-10-20-10) n'est pas dans la table E1 ;
   P-016 (A) (partition 20/40) changerait la puissance et les options (a) à (c) des coûts déjà déclarés.
4. **T4** : R-295 (1) le dit confondu par le coût de la tâche ; N-030 (B) en propose la correction ; la revue l'emploie
   tel quel.
5. **P3b** : transmettre VV4-sens-04, 11 et 12 au rédacteur du préenregistrement de P3b.
6. **Vérification de la v5** : le rapport « sens » demande un contrôle de fidélité des remplacements, et une
   vérification de sens si la recommandation du nœud E2 change de fond : c'est le cas dans la version 2.
7. **PDF de `[N]` et `[X]`** absents du bloc-notes restauré : empreintes et compagnons à refaire avant tout versement (R6).

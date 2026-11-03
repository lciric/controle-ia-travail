**confirmé avec réserves (listées)** — l'issue rendue par le script, **I1**, est exacte et conforme au texte scellé ; six réserves, toutes mineures, aucune ne touche l'issue.

# Verdict R13 — lecture du lot T0.5 à graines neuves (v1)

- Lecteur : agent neuf (n'a écrit ni le préenregistrement, ni le script, ni la contre-lecture ; n'a pas lancé la lecture). Rédigé le 2 novembre 2026, 02:10–02:20 UTC. La lecture n'a **pas** été relancée.
- Texte appliqué : `orchestrator/prereg/preenregistrement-lecture-t05-graines-neuves-v2.md` (dépôt public `/home/claude/ideation-organism`, commit de tête `0624509`), sha256 `93923d7132260c2fe7674417ec819b2a7011fa49ba3949482c3c355e9289443d`.
- Sortie jugée : `/home/claude/controle-ia-travail/diag/20261102-020625-lecture-t05-graines-neuves/lecture-t05-graines-neuves-v1.json`, sha256 `07bc2aea97ba8cc9ce2547cdb5c31b212971a977481d86ebd2c8caf36350ecb4` (et son rendu `.md`, journal, sorties standard et d'erreur : 5 compagnons `.sha256` vérifiés OK).
- Mon recalcul (code à moi, n'important aucun module du dépôt public, lancé sous `nice -n 10`) : script `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/R13-t05/recalcul_r13_v1.py` (sha256 `4dfa27e25e9efda250f9d067eeeb65674249d014f7f5d4c9a0b842b4731ab4bb`), sortie `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/R13-t05/recalcul-r13-v1.json` (sha256 `d6c43a50cfa60bc8197a412e9d28ba2c10b0fdcdd9e7f1fd5536ae1eacaf6364`).

## 1. Conformité de la course

| contrôle | constat |
|---|---|
| Texte scellé | fichier = compagnon = valeur attendue `93923d71…` ; inchangé depuis son commit de scellement `80b6574` (1er nov., 22:15:14 UTC) jusqu'à `0624509` (seuls des fichiers du nul v8 ont été ajoutés depuis) |
| Code (bloc des 14 empreintes, § 15) | `sha256sum -c` sur une copie du bloc : **14/14 OK** ; essais `8f4f4d71…` et les annexes (constats, puissance par paire, leurs sorties) conformes à l'en-tête |
| Calibrage `banque-e2.json` | `f59018fb…` conforme |
| Table des identifiants | `76375391…` conforme ; identique à `git show f40c8aa9:donnees/t05-graines-neuves-v1/table-identifiants-graines-neuves-v1.json` |
| Fichiers du lot | 28 compagnons `.sha256` (7 par lot) OK ; chacun des 56 fichiers extraits a le même objet git que l'arbre de la tête de sa branche : a `f2abad54`, b `78a63f5a`, c `2ccb14b8`, d `9dd49dc7` (= têtes annoncées) ; les empreintes du champ `lot.sources` du rapport sont celles des fichiers |
| Chaîne de production | les quatre `resume.json` citent le commit gelé `2660b07…` et la configuration canonique `db3ad3ce…` (= en-tête du texte), contrôle négatif « conforme », 0 ensemble vide |
| Commande (§ 15) | le texte est lu par son chemin relatif (course lancée depuis `orchestrator/`), empreinte H = valeur scellée, calibrage et table attendus, quatre `--run` (a, b, c, d), 0 `--notations-sup`, **1000 répliques**, **1 processus**, sortie dans le dépôt de travail (hors du dépôt public), pas de course à blanc ; code de sortie 0, sortie d'erreur vide, 146,5 s (réserve 2 : la ligne de commande elle-même n'est pas archivée) |
| Liste d'arrêt (§ 14) | aucune condition : A1 tous fichiers et compagnons présents, quatre lots ; A2 toutes empreintes conformes ; A3 aucun doublon (768 clés de notation distinctes, 288 épisodes distincts, une tâche par course, un lot par course) ; A4 plus petit moniteur 121 ≥ 60 ; A5 aucune tâche partagée avec le calibrage, 96/96 tâches en `-g2`, 96/96 origines au calibrage ; A6 variante « b0 » partout, formats lus sans écart ; A7 table de rangs conforme (0 témoin vrai, 13 faux, plus grand \|ρ\| 0,248 sur 3B:BALANCE et l'écart-type des jetons par action) ; A8 aucun arrêt (code 0, JSON écrit) |
| Une seule lecture | aucune autre sortie ni `arret.json` sur les fichiers du lot ; branches b et c récupérées localement à 02:05:56 UTC, 29 s avant la lecture (02:06:25), lot extrait à 02:06:07 UTC ; registre R-1106 : « une fois » (réserve 3) |
| Lectures préalables (§ 16 bis) | les sept autres sorties du script trouvées dans le bloc-notes (`scratchpad/lecture-t05/…`) datent de 21:14–21:48 UTC le 1er nov., portent des préenregistrements factices ou des copies de la v1, et lisent d'autres fichiers d'épisodes (empreintes différentes de celles du lot) : ce sont les essais P3 et les plomberies P4 déclarés, aux heures déclarées. Le premier résultat du lot (lot d) est commis à 22:37 UTC et récupéré localement à 23:10 UTC, **après** le scellement (22:15 UTC) ; a, b, c sont commis entre 01:12 et 01:39 UTC le 2 nov. Aucune lecture préalable non déclarée trouvée (réserve 1 sur l'heure de rédaction écrite en tête) |

## 2. Recalcul (depuis les fichiers du lot, du calibrage et le JSON de sortie)

**Épreuve, recomptée depuis les fichiers du lot.** 288 épisodes (96 tâches : 30/30/30/6), 768 notations lues (8B et 3B : 90 + 30 par lot de 30 tâches, 18 + 6 pour le lot d), 576 notations de première passe ; 288 épisodes retenus (0 sans jetons, 0 sans notation), 96 par numéro d'épisode e0, e1, e2 : **les notations descriptives (e2) sont complètes**, N_ép = 288. Instances par moniteur, recomptées : 3B:BALANCE 128, 3B:COHERENCE 262, 3B:NOVELTY 236, 3B:REDUNDANCY_PENALTY 234, 3B:RESULT_REASONING 121, 3B:RIGOR 217, 8B:BALANCE 173, 8B:COHERENCE 194, 8B:IRRELEVANCE_PENALTY 215, 8B:NOVELTY 176, 8B:REDUNDANCY_PENALTY 210, 8B:RESULT_REASONING 174, 8B:RIGOR 180 — **identiques au rapport**, et toutes dans les intervalles attendus du § 7 (colonne 288).

**Graines.** Entier de plantation recalculé depuis H : 5093687688115345767 = rapport. Paires tirées : force 0,3 sur (écart-type des jetons par action | log jetons), 0,5 sur (actions valides | écart-type), 0,8 sur (log jetons | actions valides).

**Seuils.** Famille T : m = 19 (13 témoins faux réels + 6 faux plantés), log(19/0,05) = **5,940** ; famille R : m = 26 (13 lois connues + 13 témoins faux réels), log(26/0,05) = **6,254** ; par fiche log 20 = 2,996 (lu).

**Règle e-BH, refaite sur les e-valeurs rapportées** (contrôle préalable : chaque e-valeur vaut la richesse finale si le seuil log(m/α) n'est pas atteint, et une valeur entre ce seuil et le maximum sinon — aucune incohérence) :

| configuration | k* (famille) | promus (hors famille, seuil log(m/α)) | accord avec les drapeaux | plus grand log W max d'un témoin faux |
|---|---|---|---|---|
| T-plein | 0 | TVP01, TVP02, TVP03 | oui | 0,567 (T-8B-IRRE-bruit-faux) |
| T-gelé | 0 | TVP02, TVP03 | oui | −0,024 |
| R-plein | 0 | aucun | oui | 0,567 (témoins) ; 0,999 toutes fiches (LR-8B-REDUNDANCY_PENALTY) |
| R-gelé | 0 | aucun | oui | idem |

Témoins vrais plantés, log W max plein / gelé : force 0,3 : 8,50 / 5,66 ; 0,5 : 26,60 / 17,81 ; 0,8 : 29,31 / 21,48.

**Lectures.**
- **L1 (décisive)** : tenu — 0 témoin faux promu dans chacune des quatre configurations ; aucun témoin faux n'atteint même le seuil par fiche (2,996).
- **L3′ réel** : « dents non mesurées » (0 témoin vrai réel), par construction.
- **L3′ planté (décisive pour les dents)** : 3/3 promus sous T-plein (fraction 1). Rééchantillonnage par tâche recalculé sur les 1000 lignes : moyenne 0,9347, intervalle [2/3 ; 1], fréquences par témoin 0,811 / 1,000 / 0,993 — = rapport.
- **Dents** : T-plein « dents », T-gelé « dents », réels seuls « dents non mesurées ».
- **L4′** : promus plein 3, gelé 2, **gain du plan plein = 1** (la force 0,3) ; différence rééchantillonnée moyenne 0,418, intervalle [0 ; 1] = rapport ; lois réelles promues : aucune, plein comme gelé.
- **Invariant du préfixe** : tenu pour les 48 fiches (22 de T, 26 de R) : empreinte du plan gelé = empreinte du préfixe de 120 du plan plein ; log W max plein ≥ gelé ; aucun témoin vrai promu sous gelé et pas sous plein ; plan plein = réservoir entier ; plan gelé = min(120, réservoir).
- **LR** : aucune loi connue promue (R-plein, m = 26) ; log W max de −2,49 à +1,00.

**Bornes I*(N_M)** (ma propre interpolation de la courbe ; les taux de la courbe ont été comparés aux 50 cellules du JSON publié `060216fe…` — identiques ; ma fonction redonne les valeurs gelées du § 12 : 120 → 0,117 ; 144 → 0,108 ; 180 → 0,088 ; 200 → 0,081 ; 240 → 0,060 ; 260 → 0,057 ; 288 → 0,054 ; hors grille sous N ≈ 109). Les 13 bornes du rapport sont redonnées à l'identique :

| moniteur | N_M | force f* | I* (nat par épisode) | témoin requis (§ 12) | promu sous T-plein → borne |
|---|---|---|---|---|---|
| 3B:BALANCE | 128 | 0,740 | 0,115 | 0,8 | oui → soutenue |
| 3B:COHERENCE | 262 | 0,483 | 0,057 | 0,5 | oui → soutenue |
| 3B:NOVELTY | 236 | 0,498 | 0,060 | 0,5 | oui → soutenue |
| 3B:REDUNDANCY_PENALTY | 234 | 0,500 | 0,060 | 0,5 | oui → soutenue |
| 3B:RESULT_REASONING | 121 | 0,751 | 0,117 | 0,8 | oui → soutenue |
| 3B:RIGOR | 217 | 0,552 | 0,072 | 0,8 | oui → soutenue |
| 8B:BALANCE | 173 | 0,648 | 0,094 | 0,8 | oui → soutenue |
| 8B:COHERENCE | 194 | 0,602 | 0,083 | 0,8 | oui → soutenue |
| 8B:IRRELEVANCE_PENALTY | 215 | 0,557 | 0,073 | 0,8 | oui → soutenue |
| 8B:NOVELTY | 176 | 0,639 | 0,092 | 0,8 | oui → soutenue |
| 8B:REDUNDANCY_PENALTY | 210 | 0,569 | 0,076 | 0,8 | oui → soutenue |
| 8B:RESULT_REASONING | 174 | 0,645 | 0,093 | 0,8 | oui → soutenue |
| 8B:RIGOR | 180 | 0,624 | 0,088 | 0,8 | oui → soutenue |

Avec N_ép = 288, les deux moniteurs que le texte prévoyait sans borne à 192 (3B:BALANCE, 3B:RESULT_REASONING) en ont une (N ≥ 121 > 109).

**Prédictions.**
- P1 (0 témoin faux promu, 4 configurations) : **tenue**.
- P2 (0 témoin vrai réel) : **tenue** (garde A7 conforme).
- P3 (fraction ≥ 2/3 sous T-plein) : **tenue** (1). Taux de la courbe à N = 288 : 0,612 / 0,964 / 0,996. Conditionnel aux paires tirées (table à 288) : plein 0,30 / 1,00 / 1,00, gelé 0,10 / 0,95 / 1,00 ; attendus plein 2,30, gelé 2,05 ; P(fraction ≥ 2/3) = 1,00 ; P(I4) = 0 — = rapport.
- P4 (lue) : gain observé 1 ; attendu 0,586 (= 0,226 + 0,230 + 0,130) — = rapport ; signe conforme à l'invariant.
- P5 (0 loi réelle promue, plein et gelé) : **tenue**.

**Issue selon la table du § 12, dans l'ordre** : I6 non (aucun arrêt) ; I3 non (L1 tenu) ; I4 non (forces 0,5 et 0,8 promues) ; I5 non (invariant tenu) ; I2 non (aucune loi réelle promue sous R-plein) ; **donc I1**. Aucune divergence entre mon recalcul et le rapport.

## 3. Issue : I1 — ce qu'elle permet de dire, ce qu'elle ne permet pas

**Permet de dire.**
- *Validité* : sur ces notes réelles neuves, le juge — plan plein comme plan gelé, monde informé comme aveugle — n'a promu aucun témoin faux. Valide contre des nuls structurels (trait de bruit indépendant, issues permutées) sur les données réelles de ce lot ; sans signification pour un faux lien induit par la tâche (tâches communes au calibrage).
- *Dents* (§ 12(c)) : à N = 288, sur les traits réels de ces épisodes neufs, le juge à plan plein a détecté les lois plantées correctement spécifiées de forces 0,5 et 0,8, et aussi celle de force 0,3 ; les instances au-delà des 120 premières ont apporté la promotion de la force 0,3 (gain = 1).
- *Lois réelles* (§ 12(a)) : pour chacun des 13 moniteurs, la loi connue telle qu'ajustée sur le calibrage n'atteint pas, sur graines neuves des **mêmes** 96 tâches, l'information par épisode I*(N_M) (de 0,057 à 0,117 nat selon le moniteur) à partir de laquelle une loi plantée de la forme si/sinon, correctement spécifiée, est promue avec une probabilité ≥ 0,9 sous le plan plein. La condition de dents est remplie pour les 13 moniteurs. C'est un **ordre de grandeur de la sensibilité de l'instrument « loi connue »**, moniteur par moniteur (0,9 par moniteur, pas pour les 13 à la fois), pas une borne démontrée.

**Ne permet pas de dire** (réserves du § 16 du texte, toutes applicables) :
- qu'aucune dépendance n'existe : une dépendance plus faible que I*, ou d'une autre forme (non linéaire, par tâche, par épisode), échappe à la borne ; le coût d'estimation de la loi connue (≈ 0,011 à 0,029 nat par épisode) peut masquer une dépendance vraie de cet ordre au-dessus de I* ;
- quoi que ce soit sur des tâches neuves (calibrage et épreuve partagent les 96 tâches ; un effet de tâche commun peut jouer) ;
- que le juge a des dents sur des liens **réels** : aucun témoin vrai réel n'existe (plus grand \|ρ\| 0,248) ; les dents sont mesurées sur trois lois plantées (oracle), une seule plantation, fractions grossières ;
- que la borne est opposable : elle vient d'une courbe exploratoire non contre-lue (« rien d'opposable », sa propre réserve), mesurée en monde informé au seuil 5,83 sur une loi exacte, transposée à une loi estimée en monde aveugle au seuil 6,25 ; la famille R n'a aucun témoin positif ;
- quoi que ce soit du nul v8 (imposé, sans effet sur une génération unique à archive vide), ni des états internes de l'agent, ni de ce que les notes des juges mesurent.

## 4. Réserves (toutes mineures ; aucune ne change l'issue)

1. **Chronologie écrite en tête du texte** : « v2 rédigée 22:07–22:45 UTC » est incompatible avec le scellement réel (fichier 22:12:45, compagnon 22:14:25, commit `80b6574` 22:15:14 UTC) ; sans effet sur la validité, le premier résultat du lot n'apparaissant qu'à 22:37 UTC.
2. **Ligne de commande non archivée** : le journal ne porte que les heures, le commit et la charge ; la conformité au § 15 est établie par les effets consignés dans le JSON ; l'usage effectif de `--empreinte-preenregistrement` n'est pas vérifiable (sans effet : le compagnon redonne H).
3. **« Lectures de l'épreuve : 1 » est une constante du script**, pas une mesure ; l'unicité repose sur les traces (fichiers, dates de récupération et d'extraction, registre), sans preuve au-delà.
4. **Le rendu écrit « Audit R4 : aucun déclencheur »** sans rappeler que l'audit allégé est **obligatoire** en cas d'I1 (§ 13) ; il est fait ici (section 5) et conforme.
5. **Précision de l'accord « à 1e-6 près » (§ 13)** : vérifiable pour la richesse finale (e-valeurs à six décimales : écarts ≤ 4,9e-7) ; le log W maximal n'est rapporté qu'à quatre décimales (écarts ≤ 4,7e-5, au niveau de l'arrondi).
6. **Tirage favorable sur la force 0,3** : le témoin de force 0,3 est promu alors que sa probabilité conditionnelle à la paire tirée était ≈ 0,30 (table par paire, 40 répétitions) ; le « 3/3 » et le gain du plan plein (1) reposent sur ce tirage. Ce n'est pas un déclencheur gelé ; à ne pas présenter comme une puissance à force 0,3.

## 5. Symétrie (R4)

- **Trop beau** (déclencheurs gelés du § 13) : aucun — aucun témoin faux au seuil par fiche (plus haut : 0,567 contre 2,996) dans aucune configuration ; aucune loi réelle promue. Le « 3/3 plantés, 0/19 faux » n'est pas un déclencheur : 0/19 est l'issue attendue (P1) et les témoins faux restent loin de tout seuil ; les forces 0,5 et 0,8 étaient quasi certaines pour leurs paires (1,00) ; seule la force 0,3 est un tirage favorable (réserve 6).
- **Trop mauvais** : aucun — les témoins plantés de force ≥ 0,5 sont promus ; aucun log W max négatif parmi eux.
- **Incohérence** : aucune (invariant tenu pour les 48 fiches).
- **Trop propre (I1) — audit allégé obligatoire, fait ici par un agent neuf** (ni auteur du texte ni de la lecture), depuis les fichiers du lot et du calibrage, avec mon propre code :
  - loi connue de chaque moniteur réajustée sur le calibrage seul (régression multinomiale à crête 1, quatre entrées, ma réimplémentation de la descente décrite, et un Newton exact de la même perte : pertes égales à ≤ 2e-8 près, la descente a convergé) ;
  - traits d'épreuve normalisés par le calibrage, trait de bruit retiré de la graine H (premier fils), probabilités sur les instances d'épreuve, plan ordonné par divergence à l'uniforme (aucune égalité de divergence), richesse contre la bibliothèque aveugle (marginale au maximum de vraisemblance, uniforme, moyennes glissantes 5/10/20/50) ;
  - **accord avec le rapport pour les 13 lois connues, deux bras** : N jugés identiques ; e-valeurs (= richesse finale) à ≤ 4,9e-7 ; log W max à ≤ 4,7e-5 (arrondi à 4 décimales du rapport) ; membre dominant final identique (marginale empirique, 13/13) ;
  - lois non dégénérées : poids non nuls (plus grand \|poids\| de 0,05 pour 8B:RESULT_REASONING à 0,45 pour 8B:NOVELTY) ; probabilités moyennes sur le calibrage égales aux fréquences d'ajustement à 1e-3 près ; biais centrés à ≤ 0,11 du logarithme centré de la marginale.
  - **Verdict de l'audit allégé : conforme.** Il n'autorise ni ne refuse rien d'autre.

## 6. En clair

Sur 288 épisodes neufs — les mêmes 96 tâches d'articles, rejouées avec de nouvelles graines aléatoires et notées par deux juges modèles de langage (3 et 8 milliards de paramètres) —, le juge statistique n'a déclaré vrai aucun des 19 faux liens qu'on lui soumettait (des liens avec un trait de pur bruit, ou avec des notes mélangées au hasard), quelle que soit la façon de le lire. Il a retrouvé les trois liens plantés exprès dans les données réelles : les deux plus forts, qu'il devait voir presque à coup sûr, et aussi le plus faible, qu'il n'avait qu'environ une chance sur trois de voir. Pour les vraies notes, aucun des 13 critères de notation (équilibre, cohérence, nouveauté, rigueur, etc., pour chacun des deux juges) n'a été mieux prédit à partir des traits observables de l'épisode (nombre de jetons, nombre d'actions valides, irrégularité des jetons par action) que par la simple fréquence des notes. La borne par critère veut dire : si un lien de la forme plantée portait au moins 0,06 à 0,12 nat d'information par épisode (selon le nombre d'épisodes notés pour ce critère), le juge l'aurait repéré au moins neuf fois sur dix ; c'est un ordre de grandeur de la sensibilité de l'outil, pas la preuve qu'aucun lien n'existe. Portée : il n'y a dans ces données aucun vrai lien réel connu pour éprouver le juge, les tâches sont celles qui ont servi à l'étalonner (rien ne vaut pour des tâches neuves), et un lien plus faible ou d'une autre forme pourrait passer sous la borne.

*Phrase pour un mentor (40 mots)* : In a preregistered reading of 288 fresh-seed episodes (same 96 tasks), our statistical judge promoted 0/19 null witnesses, 3/3 planted laws and none of 13 real feature-to-score laws; its 90%-power threshold for planted-form laws is roughly 0.06–0.12 nats per episode.

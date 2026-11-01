verdict confirmé avec réserves (listées) : la lecture est reproduite sans aucun écart (806 cellules statistiques refaites avec un code indépendant, 49 trajectorielles relues dans les comptes bruts) ; sept réserves de portée et d'étiquetage, aucune ne change un verdict de cellule.

# Verdict du lecteur neuf (règle R13) — simulation d'essaim, run 20261101-222901-essaim — v1

Lecteur : sous-agent neuf, qui n'a écrit ni le préenregistrement, ni le code, ni l'analyse. Dépôt `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04`, commit `bba072c4`. Je n'ai modifié aucun fichier du dépôt et n'ai pas relancé le run. Mes scripts de recalcul sont hors dépôt : `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/relecture.py` (cellules statistiques et bornes), `formes.py` (formes closes de la classe M, avec seuils refaits), `he36.py` (formes closes de HE3.6, quadrature adaptative de scipy), `audit.py` (écarts réduits). Ils lisent les comptes bruts des fichiers de blocs, pas `lecture.json` ; `lecture.json` n'est lu que pour la comparaison finale.

## 1. Empreintes et provenance

- `sha256sum -c` : OK sur les 11 fichiers (préenregistrement, grille, manifeste, `bloc-C`, `bloc-M`, `bloc-HE3`, `bloc-HE6`, `calibrage`, `equivalence`, `lecture.json`, `lecture.md`).
- Le manifeste (`runs/20261101-222901-essaim/manifeste.json`) cite : le préenregistrement `prereg/essaim-simulation-v1.md` d'empreinte `9e354761…28b35c5` (= celle du fichier scellé), la grille d'empreinte `dacbce30…eff06` (= celle de `prereg/essaim-grille-v1.json` et celle du brouillon d'origine), le commit cité `5957a3df0e407fd5cb916c11e9e6e55c43f07897` (40 caractères, existe, ne contient que la grille et son empreinte), `decisif: true`, `depot_propre: true`, `replication_de: null`, lanceur `run_essaim_v2`, lecture `lecture_v2`, commit d'exécution `d76ee302` (celui du préenregistrement scellé), `reserves: []`.
- Graine racine : les 128 premiers bits du sha256 du texte scellé, soit les 32 premiers caractères hexadécimaux `9e3547619bdd1303abed6fe9cd7c6394`, valent 210294662851970115856489885302618088340, exactement l'entropie du manifeste. Les 1 204 tâches ont une clé de dérivation égale aux 64 premiers bits du sha256 de leur nom (0 écart, 1 204 noms distincts) ; l'état de contrôle de la tâche `C/e10x20/A_rebrassage` est reproduit par `SeedSequence`. L'empreinte de configuration et celle du manifeste dans `lecture.json` et les blocs sont cohérentes (`lire_manifeste` passe).
- Gel du code : `git diff` vide entre le commit cité et le commit d'exécution sur `src/`, `tests/` et la grille, et vide entre le commit cité et `bba072c4` sur le paquet `simulation_essaim`, les deux fichiers d'essais et la grille. Le texte scellé ne diffère du brouillon 2 que par les deux marqueurs de gabarit (`diff` : lignes 7 et 346). Les trois fichiers de la version 2 (`lecture_v2.py`, `run_essaim_v2.py`, `test_simulation_essaim_v2.py`) ont les empreintes citées dans la contre-lecture 2. Les neuf lignes de la table E de `lecture.md` sont recopiées mot pour mot dans le préenregistrement.
- Garde d'équivalence : écart relatif maximal de l'ordre de 5·10⁻¹⁴ (limite 10⁻⁹) sur les 200 essaims de chaque configuration.

Note de procédure, sans effet : le texte scellé garde le paragraphe « À remplacer, au scellement, par : … » après la contre-lecture 2, déclaré dans le texte comme consigne de rédaction conservée.

## 2. Application des critères gelés (recalcul indépendant)

J'ai implémenté moi-même les critères de la section « Critères de lecture gelés » (intervalle exact de Clopper-Pearson de niveau 1 − 10⁻⁵ par `scipy.stats.beta.ppf`, recoupé par `binomtest(...).proportion_ci(method='exact')` ; critères « égal », « au-dessus », « en dessous », « au plus », « forme close », « au moins une borne », « région conforme », « trajectoriel »). Le sens de chaque cellule est tiré du texte du préenregistrement (règles de sélection de HE1.3, HE2.4, HE2.5, HE3.3, HE3.4, HE6.3), pas du code de lecture.

| Ensemble | Cellules refaites | Écarts avec `lecture.json` |
|---|---|---|
| HE1.1, HE1.2, HE1.3, HE2.1, HE2.2, HE2.4, HE2.5, HE5.1, HE5.2 (bloc C) | 316 | 0 |
| HE2.3 (bornes refaites par convolution binomiale, tables du préenregistrement retrouvées à 6·10⁻⁵) | 15 | 0 |
| HE6.1, HE6.2, HE6.3 (bloc HE6) | 30 | 0 |
| HE3.1, HE3.2, HE3.3, HE3.4 (bloc HE3) | 30 | 0 |
| HE3.5 (région conforme refaite : somme de 50 lois bêta-binomiales (400 ; 50 ; 951), région centrale de niveau 1 − 10⁻⁵ = [843 ; 1 165], égale à celle du préenregistrement) | 40 | 0 |
| HE4.1, HE4.2, HE4.3 (315 formes closes réécrites sans lire le code du dépôt, seuils exacts refaits et égaux à ceux de `calibrage.json`) | 315 | 0 ; écart maximal entre mes valeurs théoriques et celles du code : 2·10⁻¹⁴ |
| HE3.6 (52 formes closes sous effet d'épisode et sous équicorrélation, par quadrature adaptative ; extraits du préenregistrement retrouvés) | 52 | 0 ; écart maximal : 7·10⁻¹⁵ |
| Trajectorielles : HE1.1 (12), HE2.1 (12), HE5.2 (3), HE6.1 (4), HE4.4 (18) | 49 | 0 violation ; écarts de L4 au plus 1,1·10⁻¹³ contre une tolérance de 2·10⁻⁷ |

Total : 439 + 315 + 52 = 806 cellules statistiques et 49 trajectorielles, soit les 824 cellules du préenregistrement, par prédiction exactement les effectifs annoncés (HE1.2 : 90, HE5.1 : 108, HE2.4 : 18, etc.). Les 439 premières sont toutes « conformes » aussi chez moi, sans cellule « non concluante ».

Cellules détaillées (comptes bruts, intervalles recalculés) :

1. **Égalité, bloc C, HE1.2** — `e5x40/A_routage_un_m10/somme` : 946 / 20 000, intervalle [0,04095 ; 0,05426] ; référence sous P₀ 4 925 / 100 000, intervalle [0,04628 ; 0,05234]. Les intervalles se recoupent : conforme.
2. **Au-dessus, bloc C, HE1.3** — `e5x40/A_routage_un_m10/agent_moyenne` : 6 225 / 20 000, [0,2969 ; 0,3259] ; référence haut 0,05326. Borne basse 0,2969 > 0,0533 : conforme.
3. **En dessous, bloc C, HE1.3** — `e10x20/A_relais_m20/agent_moyenne` : 205 / 20 000, [0,00740 ; 0,01376] ; référence 5 080 / 100 000, borne basse 0,04779. Haut 0,0138 < 0,0478 : conforme (le relais fait passer la surveillance par agent à un cinquième de son taux).
4. **Trajectorielle** — `e10x20/T_synchro_m5` (HE2.1) : 0 valeur différente, 0 discordance d'alarme, 0 violation de sémantique ; et HE4.4 `e10x20/M_synchro_B12_m10` : écart maximal 5·10⁻¹⁵ (processus e), 3·10⁻¹⁵ (moyenne par pas), 4·10⁻¹⁴ (somme), 0 discordance d'alarme : conforme.
5. **HE6 (deux cellules)** — HE6.3 `e10x20/c0.4/T_synchro_m5/coelev_comptage` : 317 / 20 000, [0,01224 ; 0,02011] contre une référence corrélée de 4 769 / 100 000, borne basse 0,04477 : en dessous, conforme (pour `pas_moyenne` : 230 / 20 000, [0,0085 ; 0,0152] contre 0,0451 : conforme). HE6.2 `e10x20/c0.2/T_synchro_m5/agent_moyenne` : 991 / 20 000, [0,04305 ; 0,05666] contre [0,04744 ; 0,05356] : égal, conforme.
6. **HE3** — HE3.3 `e10x20/tau0.2/e_pas_ville` : 3 966 / 20 000, borne basse 0,18603 > haut de la référence bien spécifiée 0,01357 : au-dessus, conforme ; HE3.4 même cellule : borne basse 0,186 > 0,05 : dépasse α, conforme.
7. **Forme close, bloc M** — HE4.1 `e10x20/M_concentre_B5/pas_moyenne` : 3 280 / 20 000 = 0,164, intervalle [0,1526 ; 0,1758] ; valeur théorique refaite 0,15385 dans l'intervalle : conforme. C'est la cellule d'écart réduit le plus grand (3,98), voir section 3.
8. **Borne, HE2.3** — `e5x40/T_synchro_m3/coelev_comptage≥borne` : borne refaite 0,27324 ; mesure 0,27915, intervalle [0,2653 ; 0,2933], haut ≥ borne : conforme. La borne est presque atteinte (marge 0,006), donc discriminante.

## 3. Audit de symétrie (règle R4)

Recalculé à partir des comptes bruts et de mes propres formes closes :

- 263 égalités entre échantillons indépendants (HE1.2 : 90, HE2.2 : 45, HE5.1 : 108, HE6.2 : 20) : variance des écarts réduits 0,9751, moyenne 0,0078, |z| maximal 2,77, 13 valeurs au-delà de 2 (11,97 attendues), aucune au-delà de 3, test de Kolmogorov-Smirnov contre N(0, 1) : p = 0,55.
- 358 comparaisons à des formes closes (306 de la classe M, 52 de HE3.6, valeur théorique dans [0,01 ; 0,99]) : variance 1,0819, moyenne −0,068 (−1,3 erreur-type, non significatif), |z| maximal 3,98, 24 valeurs au-delà de 2 (16,3 attendues), 3 au-delà de 3 (1 attendue), Kolmogorov-Smirnov p = 0,28.
- Les valeurs du code (1,082 et 0,975) sont reproduites au millième. Bornes [0,3 ; 3] respectées, audit non déclenché : confirmé. Ni trop propre (une variance de 0,3 ou moins signalerait un échantillon réutilisé) ni trop bruité. Remarque : la queue des formes closes est un peu plus lourde que la normale (3 cellules au-delà de 3, dont l'écart de 3,98 pour `M_concentre_B5/pas_moyenne`, probabilité bilatérale ≈ 7·10⁻⁵ par cellule, ≈ 2,5 % d'avoir au moins un tel écart sur 358) ; comme les sept statistiques d'une cellule partagent les mêmes essaims, les écarts sont corrélés et cela reste plausible sans biais ; aucune réplication n'est requise par la règle écrite (l'intervalle à 1 − 10⁻⁵ contient la valeur théorique).

## 4. « 23 sur 23 » est-il trop beau ?

Oui pour une partie, et c'est dit dans le préenregistrement (issue F, première ligne). Voici la répartition fine, par nature, des 23 prédictions et des 824 cellules :

**A. Identités mathématiques ou vérifications d'instrument, qui ne pouvaient échouer que par un bogue (17 prédictions, 706 cellules).**
- Identités au bit près, trajectoire par trajectoire : HE1.1, HE2.1, HE4.4, HE5.2, HE6.1 (49 cellules). Elles tiennent par construction : les attaques de classe C sont des éléments du groupe, et le code vérifie par une garde qu'elles conservent les multi-ensembles.
- « Puissance égale au taux » : HE1.2, HE2.2, HE5.1, HE6.2 (263 cellules d'égalité). Sous un arrangement de groupe, l'alarme d'une statistique invariante est identique à celle de l'essaim honnête dont l'attaqué est issu (même uniforme de départage) ; ces cellules mesurent donc un nouveau taux sous P₀ contre le taux de calibrage : elles contrôlent la calibration des seuils, pas le théorème. Leur résolution est faible : deux intervalles à 1 − 10⁻⁵ se recoupent tant que l'écart est inférieur à environ 0,010 en valeur absolue autour de 0,05 (20 % en relatif). « Égal » veut dire « égal à ±0,01 près », l'exactitude venant de l'identité trajectorielle.
- Formes closes et bornes : HE4.1 à HE4.3 (315), HE3.6 (52), HE2.3 (15 bornes inférieures), HE3.5 (40, exactitude de la région conforme par échangeabilité). Mes recalculs reproduisent les formes closes à 10⁻¹⁴ : le code et l'arithmétique sont corrects, mais ce n'étaient pas des paris.
- Inégalité de Ville : HE3.1 et HE3.2 (8 cellules). Les taux mesurés valent 0,011 à 0,018 pour α = 0,05 : la marge est d'un facteur 2,7 à 4,7, l'inégalité ne pouvait pas être mise en défaut. Elle établit « valide », pas « utile » (puissance sacrifiée).

**B. Prédictions de puissance, qui dépendaient d'une grandeur non démontrée (6 prédictions, 82 cellules) : HE1.3, HE2.4 (en partie), HE2.5, HE3.3, HE3.4, HE6.3.**
- Toutes ont été vues en exploration sur données jetables avant le scellement (statut « exploratoire vu » pour HE1.3, HE2.5, HE3.4, HE6.3 ; « en partie » pour HE2.4 et HE3.3). Les effets prédits sont grands (au moins 0,1 en taux) devant la demi-largeur de 0,016 à R = 20 000 : une reproduction à graine neuve était quasi certaine. Les cellules et les sens ont été choisis après avoir regardé les valeurs (règles de sélection : effet exploratoire ≥ 0,08 ou ≥ 0,1, m = 2 écarté, `e_coelev_ville` sous τ = 0,1 écarté, HE6 à c = 0,2 et m = 5 écarté).
- Dans HE2.4, les 6 cellules `coelev_comptage` découlent d'une borne exacte supérieure à α + 0,02 : quasi mathématiques. Seules les 12 cellules `pas_moyenne` et `coelev_somme3` sont de vraies prédictions heuristiques, et elles étaient vues.
- Dans HE2.5, 14 des 18 cellules sont « au plus », critère peu exigeant (échoue seulement si la borne basse dépasse le haut de la référence).
- Je ne trouve donc aucune prédiction non triviale **à la fois** non vue en exploration et non déduite d'une preuve ou d'une borne. Le « 23 sur 23 » mesure l'exactitude de l'instrument et de l'arithmétique et la reproductibilité de six effets déjà observés ; il ne mesure pas une capacité à prédire à l'aveugle. Le préenregistrement le dit (phrase de portée, statuts, colonne « appui exploratoire »), et `lecture.md` le répète.

**C. Ce que les cellules écartées par la sélection montrent (descriptif, lu dans les blocs).** C'est la vérification symétrique de la règle R4 : chercher dans les cellules non prédites ce qui aurait pu contredire.
- Synchronisation à m = 2 : `pas_moyenne` à e20x20 vaut 0,0578, intervalle [0,0507 ; 0,0654], qui recoupe la référence [0,0475 ; 0,0537] : « au-dessus » n'y aurait pas été confirmé (non concluant). L'exclusion de m = 2 était donc nécessaire, et elle était déclarée.
- `e_coelev_ville` sous τ = 0,1 à e10x20 : 0,0322, intervalle [0,027 ; 0,038], donc sous α : « dépasse α » n'y aurait pas tenu (à e10x50, 0,0798, il tient). Exclu par la règle, déclaré.
- **Cellule à signaler** : HE6, c = 0,4, synchronisation de m = 5 agents. Les e-valeurs sont **au-dessus** de leur taux : `e_coelev` 1 303 / 20 000 = 0,0652, intervalle [0,0577 ; 0,0732] contre la référence [0,0472 ; 0,0533] ; `ed_coelev` 0,0658, [0,0583 ; 0,0739] contre [0,0453 ; 0,0513]. Les intervalles sont disjoints. La prédiction HE2.5 (« au plus à leur taux ») est confirmée sous la loi honnête indépendante, mais ce résultat montre que l'énoncé « la version séquentielle n'échappe pas » ne se généralise pas à la loi corrélée. Le préenregistrement classait cette cellule en « descriptif, sans verdict », mais la ligne 4 de la table E ne précise pas qu'elle vaut sous la loi honnête indépendante seulement.

## 5. Ce que le résultat permet et ne permet pas (pour un mentor)

**Permet** : sur des matrices de scores synthétiques, un moniteur invariant par permutation des agents d'un même pas (somme, max, comptage, moyenne par pas, co-élévation, e-valeurs sur la co-élévation) ne distingue pas, à l'identité près au bit, un attaquant qui ne fait que permuter les agents dans chaque pas ; la surveillance par agent est aveugle à une synchronisation (permutation du temps de chaque agent), mais la co-élévation et la moyenne par pas la détectent dès que la moitié de l'essaim se synchronise (bornes exactes respectées) ; et les seuils calibrés sur des essaims honnêtes entiers gardent le taux nominal là où des seuils calibrés sur des cases supposées indépendantes alarment à tort (co-élévation : 62 à 83 % des essaims sous c = 0,4, contre 5 % voulus).

**Ne permet pas** : ce sont des scores synthétiques où la menace est un motif choisi dans la matrice par un attaquant idéalisé qui ne peut que permuter ou synchroniser, pas une idée qui se propage d'un agent à l'autre, et rien n'est dit sur des activations réelles ni sur la capacité d'un agent à piloter son score ; et 17 des 23 prédictions vérifient l'instrument ou une preuve, les 6 restantes reproduisent à graine neuve des effets déjà observés avant le scellement, donc ce n'est ni une confirmation indépendante ni une preuve empirique.

## Réserves (récapitulatif)

1. 17 prédictions sur 23 étaient des identités, des formes closes, des bornes ou une inégalité à grande marge (section 4A) ; à dire tel quel aux mentors.
2. Les 6 prédictions de puissance avaient toutes été vues en exploration, leurs cellules choisies après coup (section 4B) ; ne pas les présenter comme prédites à l'aveugle.
3. Les cellules « égal » ont une résolution d'environ ±0,01 et sont, pour les statistiques invariantes, identiques par construction à l'alarme honnête ; elles contrôlent la calibration, pas le théorème.
4. Les e-valeurs de Ville tiennent α avec une marge d'un facteur 2,7 à 4,7 (taux de 0,011 à 0,018 sous la loi de référence) : valides, mais très conservatrices.
5. L'énoncé « la version séquentielle n'échappe pas à la synchronisation » est établi sous la loi honnête indépendante ; sous c = 0,4 et m = 5 les e-valeurs dépassent leur taux (0,065 contre 0,050, intervalles disjoints). Préciser la restriction dans la ligne 4 de la table E avant tout résumé, ou citer cette cellule comme limite.
6. Un écart réduit de 3,98 (`M_concentre_B5/pas_moyenne`) et trois écarts au-delà de 3 sur 358 : plausibles (cellules corrélées, pas de biais de moyenne), à mentionner si on détaille l'audit.
7. Limites de ma relecture : je n'ai pas relancé le run (interdit) ; les comptes bruts des tirages sont crus sur la foi du manifeste, de la garde d'équivalence et des gardes du lanceur ; l'accord à 10⁻¹⁴ de 367 formes closes réécrites avec des tirages de Monte-Carlo indépendants de ces formes est toutefois une validation forte de l'échantillonneur et des statistiques pour la classe M et les lois hors hypothèses. La multiplicité prévue (borne de l'union ≈ 1 %) n'a rien déclenché : aucune réplication requise.

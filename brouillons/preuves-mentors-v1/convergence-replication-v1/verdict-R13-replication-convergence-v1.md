**confirmé avec réserves (listées)** — l'issue lue sur les nombres de l'analyse A et recalculée par B (et par le lecteur) est exacte et conforme au texte scellé ; deux réserves mineures de procédure, sans effet sur aucun nombre ni sur l'issue.

# Verdict du lecteur neuf (règle R13) — réplication sur graine neuve de la course de convergence des règles de défense — v1

- Texte appliqué : `prereg/preregistrement-replication-regles-defense-convergence-v1.md`, empreinte `1eea9449b570df5efecb8398de954e29c19ea987f6794b46457efd48fe11ae4f` (compagnon conforme), identifiant PREREG-REPLICATION-REGLES-DEFENSE-V1 ; spécification `specification-statistique-decisive-v2.md` (`977dd909…`).
- Course lue : `20261102-011337-replication-regles-defense` — manifeste `runs/…/manifeste.json` `0da9dbfb6c11920c26ea49713227956f39f986709d8535144d9a1c96fd16bb57` ; résultats `diag/…/resultats-regles-defense.json` `1d14f5543b386418541c6d505a68968ba9279d3783f60046f6091690db7b7922` ; analyse A `diag/…/analyse-regles-defense.json` `ff4eb4f9dde5e42cf734c6d0ae8ddb226f5875323f124321865a0f1627691b0e` ; sortie de B `implementation-b/sortie-b-replication-v2.json` `795ceda9a2630fc4f8f747aec8d1390d447d1565774b3179a8787e7ca3e9c43b` (code 0, lecture autorisée). Tous les compagnons `.sha256` vérifiés (`sha256sum -c` : conformes).
- Lecteur : sous-agent neuf (Claude Opus 5.5), session conv-audit, 2 novembre 2026, ≈ 01:45 UTC. N'a écrit ni le texte, ni la spécification, ni le code v3, ni B, ni aucune contre-lecture, ni lancé la course. Rien modifié, rien commité, aucun réseau, aucune clé lue. Seuls calculs : le rejeu V0 (l) et le recalcul de la statistique (code hors dépôt, `nice -n 10`).

## 1. Issue globale

**Ligne 7 de la table des issues : « réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise »** — issue après déclencheurs et issue brute identiques (aucun déclencheur d'audit), V0 vraie, aucun élément à la frontière numérique.

- « Le mélange d'équilibre bat l'historique » (HRép1) : **répliquée** aux deux budgets.
- « Ne rien faire fait aussi bien » (HRép0) : **non jugeable (imprécis)** — classe « ? » au budget δ = 1,4, « ≈ » au budget δ = 1,6 ; aucune classe en faveur du réentraînement.
- Secondaires : « la régularisation vers le passé ne nuit pas » (HRép3) **répliquée** ; « la défense figée détecte mieux les lois tenues à l'écart » (HRép-ii) **répliquée**. Descriptif « oublier coûte » (HR2) : non tranchée, comme à l'original.

Phrase écrite d'avance (« Réplication partielle, équivalence imprécise »), chiffres remplis : « Le mélange d'équilibre bat toujours l'historique ; la seconde course ne tranche pas l'équivalence de la défense figée (classe « ? » au budget δ = 1,4) : cette phrase reste celle d'une seule course, avec sa marge de 0,02. » Secondaires : « La régularisation vers le passé ne nuit toujours pas (classes « R4 ≳ R2 » et « R4 ≳ R2 ») » ; « La défense figée détecte toujours mieux les lois tenues à l'écart (+0,0598, +0,0673) ».

Ce que chaque ligne de la table change (texte scellé, « Conséquence de chaque issue ») et laquelle s'applique :

| # | Condition | Ici | Ce que la ligne change, écrit d'avance |
|---|---|---|---|
| 1 | plomberie fausse, arrêt ou discordance A/B | fausse | aucune phrase sur la réplication ; Lazar informé ; suite selon le motif |
| 2 | « audit en attente » | fausse | aucune phrase ; audit par un sous-agent neuf |
| 3 | « artefact » | fausse | aucune phrase ; version nouvelle du texte, rapportée avec celle-ci |
| 4 | le mélange non répliqué | fausse | le constat « le mélange bat l'historique » n'est plus présenté comme acquis ; enquête (nœud de Lazar) |
| 5 | les deux répliqués | fausse (la défense figée est imprécise) | les deux constats présentables par Lazar avec « réplication sur graine neuve, même code, même monde » |
| 6 | mélange répliqué, défense figée non répliquée | fausse | la phrase « ne rien faire fait aussi bien » est retirée |
| **7** | **mélange répliqué, défense figée non jugeable** | **vraie** | **« ne rien faire fait aussi bien » reste la phrase d'une seule course, dite comme telle** |
| 8 | sinon | non examinée | — |

Rien d'autre n'est autorisé. En particulier (Plan 3) : **aucune seconde course sur une autre graine pour changer l'issue** ; une seconde course, si Lazar la décide, est un préenregistrement nouveau (nouveau texte, nouvelles racines), rapporté avec celle-ci, jamais à sa place.

## 2. Réserves (une ligne chacune)

1. **Mineure, procédure** : le journal de départ ne contient aucun relevé de fin de course (`uptime` et tâches actives), alors que la session faisait d'autres travaux pendant la course (registre R-1101, ≈ 01:30 UTC : vérifications comprenant 24 essais, « dans le dépôt et dans l'arbre » séparé de l'analyse principale) ; sans effet sur le calcul ni sur la lisibilité (lecture fixée, point (b) : seulement consigné ; le rejeu V0 (l) est égal au bit ; durée de mur 1 222,5 s, plus courte que l'original, 1 692,7 s).
2. **Mineure, procédure** : l'arbre séparé `/home/claude/replication-regles-defense-v1` (branche `replication-regles-defense-v1`, `c04e4e70`) n'est pas retiré, contrairement au Plan 5, étape 6 (« retrait de la copie ») ; ses dossiers `runs/` et `diag/` de la course sont identiques à ceux du dépôt (`diff -r` vide) ; sans effet.

Observation, sans réserve : la sortie de B n'écrit que le nom de base des fichiers lus ; l'emplacement `implementation-b/entrees/` des deux pièces de l'original est attesté par la commande gelée et par leurs empreintes épinglées (identiques à celles des pièces de `diag/20261101-160323-…`).

## 3. En clair

La course du 1er novembre avait trouvé, dans ce petit monde synthétique, que la défense qui tire au hasard parmi ses moniteurs passés selon des poids d'équilibre (« le mélange d'équilibre ») détecte mieux l'attaquant que le moniteur réentraîné sur toutes les attaques passées (+0,10 et +0,12 de taux de détection aux deux budgets d'attaque), et que le moniteur initial jamais réentraîné (« la défense figée ») fait aussi bien que le réentraîné, à 0,02 près. Sur une graine neuve que personne n'a choisie, le mélange garde son avance : +0,112 (intervalle à 98,75 % de +0,097 à +0,127) et +0,125 (de +0,115 à +0,136), presque les mêmes nombres qu'à l'original ; **« le mélange d'équilibre bat la défense réentraînée » est confirmé**, et la statistique recodée par un autre modèle concorde exactement. Pour la défense figée, l'estimation penche même légèrement de son côté (+0,005 et +0,008) et le réentraînement n'est démontré meilleur à aucun budget ; mais au budget 1,4 l'intervalle d'équivalence va de −0,010 à +0,0204, juste au-dessus de la marge de 0,02 (les écarts d'une instance à l'autre y sont plus dispersés qu'à l'original : écart-type 0,062 contre 0,044), et au budget 1,6 il tient de justesse (de −0,002 à +0,0195). **« La défense figée fait aussi bien que la défense réentraînée » n'est donc ni confirmé ni contredit** : cela reste le constat d'une seule course, à dire avec sa marge de 0,02. La portée est celle d'une robustesse à la graine seulement : un jeu synthétique, une seule arène (6 dimensions, 3 composantes, 8 tours, deux budgets), un attaquant local, aucun modèle de langage ni moniteur d'activations réel, et rien sur la capacité déployée (le mélange déploie jusqu'à 9 moniteurs contre 1).

## 4. Contrôles V0 (a) à (l)

| | Contrôle | État | Preuve |
|---|---|---|---|
| (a) | aucune condition de la liste d'arrêt | **conforme** | ligne par ligne : texte scellé et identifié (autorisation rejouée en V0 (l) sans arrêt ; validateur muet) ; racines dérivées distinctes, hors ensemble interdit et hors vecteurs (c) ; 20266201 et 20266202 absentes ; racines des 200 tâches = règle D (c) ; arène et gel aux empreintes épinglées (d) ; code v3 à son empreinte, essais passés (g) ; B commitée avant le manifeste, validée, fichiers dans les listes (h) ; manifeste `depot_propre: true` ; charge 0,87 au départ (ligne ci-dessous) ; gardes internes non franchies (course finie en code 0 ; processeur maximal d'une tâche 15,4 s pour 600 s ; fausses alertes des défenses finales entre 0,0073 et 0,0131, dans α ± 0,005 ; 0 entraînement non convergé ; 0 départ non fini) ; `timeout 7200` non atteint (01:13:37 → 01:34:03) ; B en code 0 ; graines neuves (j) ; concordance (i) ; texte non modifié (une seule version, k) ; aucune seconde course ; aucune référence `donnees/*` dans le dépôt ; processus de travail consignés (10806, 10807) absents (aucun orphelin) |
| (b) | 200 tâches, instances 0 à 99 par budget, sans doublon, cinq variantes aux noms exacts | **conforme** | 100 tâches par budget, instances triées = 0…99 ; clés exactement `R0`, `R1`, `R2`, `R3`, `R4[moyenne,λ=0.3]` dans cet ordre dans chaque tâche ; `delta` 1,4 / 1,6 cohérent avec `code_delta` ; `config_sha256` = `3fbb27fc…` dans les 200 ; V = min(standard, renforcé) exactement partout |
| (c) | racines = règle D sur l'empreinte du texte scellé, ≠ 20266201 et 20266202 | **conforme** | recalcul du lecteur (numpy 2.4.6) : ρ = **17402758300159606950**, ρ_t = **9026536908176406295** ; les trois vecteurs d'essai de la spécification retrouvés ; égales aux entiers et aux chaînes du manifeste (et à l'entropie de ses graines), et aux 200 tâches (lecture exacte des entiers) ; B rend les mêmes chaînes |
| (d) | empreintes du code v3, de l'arène v4, du gel v2, de la configuration, de la bibliothèque = bloc d'identité ; versions | **conforme** | manifeste : code `3519123b…`, arène `70c77fd5…`, gel `9977d7df…`, configuration `3fbb27fc…`, code v2 `9f0dcf5e…`, bibliothèque `a83c48ce…` / `3b2e3ee5…` / `93beeb1c…` / `1a5c7464…` ; Python 3.13.18, numpy 2.4.6, scipy 1.17.1 ; mêmes empreintes sur disque et au commit de scellement `4a1d2cdd` ; champ `version` des 200 tâches = `arene_regles_defense_v3` |
| (e) | λ = 0,3 et référence « moyenne » (commande, manifeste, chaque tâche) | **conforme** | commande `--lambda 0.3 --reference moyenne` ; manifeste `lambda: 0.3`, `reference: "moyenne"` ; dans chaque tâche, R4 : `lam` 0,3 et `reference` « moyenne », les quatre autres `null` |
| (f) | une seule invocation ayant écrit des résultats | **conforme** | journal de départ : une commande lancée à 01:13:37, code 0 à 01:34:03 ; un seul dossier `diag/…replication-regles-defense` dans le dépôt, dans l'historique git (toutes branches) et dans les arbres séparés ; aucune reprise |
| (g) | essais du code v3 passés avant la course, journal aux empreintes du texte | **conforme** | `journaux/journal-essais-code-v3-v1.log` (`a506cd44…`, conforme) : écrit le 2026-11-01 à 22:19:40 UTC, avant le scellement ; empreintes des trois fichiers essayés = `3519123b…`, `d1afa9db…`, `cad20939…` (celles du texte et du disque) ; « 43 passed », code de sortie de pytest 0 ; E6 : trois tâches « égal au fichier original » |
| (h) | B v2 commitée avant le manifeste, validée, fichiers ouverts dans les listes fermées ; six fichiers lus pendant la course | **conforme** | code `1e32e3b6…`, essais `fdffedce…`, rapport `a29437b0…` et `bbe01185…` présents en `6151e597`, ancêtre du commit du manifeste `4a1d2cdd` (`git merge-base --is-ancestor` rend 0), inchangés depuis ; rapport : « validation RÉUSSIE », points (1) à (5) (écart 0 sur 32 contrastes, branches synthétiques, gardes (a) à (e), entiers de 64 bits, 560 essais) ; fichiers ouverts (rapport, l. 252–267) : consigne, `entrees/`, ses propres fichiers v1 et v2, ses fichiers temporaires, `CLAUDE.md`, l'interpréteur, des listages — tous dans les listes fermées du Plan 4 ; `empreintes_fichiers` : exactement six — E1 `1d14f554…`, E2 `0da9dbfb…`, E3 `1eea9449…`, E5 `ff4eb4f9…` (compagnons conformes) et les deux E4 `18b80112…`, `d07ece47…` (épinglées) ; E5 lue après le calcul de B (`ordre_des_lectures`) |
| (i) | concordance A/B ; états de santé de B = recalcul du lecteur | **conforme** | lecteur, A et B : écart maximal **0** (égalité exacte) sur les 32 contrastes (16 par budget : moyenne, écart-type, dix quantiles, n, zéros), donc sur les cinq de concordance exigée ; z des quatre contrastes primaires identiques ; classes des Tables A, B, B′, C, verdicts bruts et après déclencheurs, déclencheurs : identiques ; aucun élément à la frontière ; B : `concordance: true`, aucune alerte ; santé : états de B = recalcul du lecteur depuis les résultats, par budget et globaux ; recoupement d'alerte depuis les champs de l'analyse A : mêmes états |
| (j) | graines neuves : aucun des quinze comptes au-dessus de 2 ; comptes de B = recompte | **conforme** | recompte du lecteur (égalité des 64 bits, même tâche) : **0** pour chacune des cinq variantes et chacune des trois mesures (V, X̄, (ii)) ; B : les quinze à 0, pas d'arrêt |
| (k) | une seule version scellée dans git, empreinte consignée avant la course ; un seul manifeste de cette réplication | **conforme** | `git log --all` sur le texte et son compagnon : un seul commit, `4a1d2cdd` (01:09:09 UTC) ; H consignée en R-1097 dans ce commit, avant le départ (01:13:37) ; un seul dossier sous `runs/` dont le nom se termine par `-replication-regles-defense` ; aucun manifeste interrompu |
| (l) | rejeu de deux tâches (δ 1,4 ; instances 0 et 1), processus neuf, égalité au bit | **conforme** | `PYTHONPATH=src OMP_NUM_THREADS=1 python -B`, depuis le dépôt ; code v3 `3519123b…` ; `autoriser_decision_regles` sur le texte scellé rend `1eea9449…` et pose les racines du manifeste ; `executer_tache_regles` avec sérialisation ; les deux tâches **égales au bit** au fichier de résultats sur tous les champs hors temps processeur (2 959 feuilles par tâche, dont 2 816 nombres flottants ; version, sérialisation et loi cible comprises) ; 10,4 s et 10,0 s de processeur ; listes de `runs/` et `diag/` identiques avant et après |
| — | condition de départ sur la charge (lecture fixée) | **conforme** | relevés toutes les 30 s de 01:09:37 (1,98) à 01:13:37 (**0,87** ≤ 1,0), « départ autorisé », commande à 01:13:37 ; attendre est permis (point (a)) ; pendant la course : voir réserve 1 |

**V0 vraie.**

## 5. Contrôles de santé (recalculés depuis les résultats ; seuils de l'original)

| | δ = 1,4 | δ = 1,6 | État |
|---|---|---|---|
| T2 trop beau / trop mauvais | moyennes de V de 0,105 à 0,224 ; Δ(R3, R2) 0,112 ; \|Δ X̄\| ≤ 0,056 | moyennes de V de 0,056 à 0,184 ; Δ(R3, R2) 0,125 ; \|Δ X̄\| ≤ 0,065 | non déclenché |
| T3 mélange dégénéré | 0 tâche à poids pur (plus grand poids 0,959) | 0 (0,738) | non déclenché |
| T4 régularisation dégénérée | 8 tâches sur 100 à cosinus moyen ≥ 0,999 | 3 | non déclenché |
| T5 optimiseur | plus grand écart standard − renforcé 0,00034 ; plus grand écart de contraste 0,00062 | 0,00013 ; 0,00050 | non déclenché |
| T6 fausses alertes | plus grand écart à α 0,00012 | 0,00010 | non déclenché |

## 6. Recalcul et comparaison (tables du texte)

Statistique recalculée par le lecteur d'après la spécification v2 (§ 2 à § 10), sans importer de code du dépôt (vecteurs d'essai du générateur retrouvés). Valeurs à 4 décimales (6 près d'un seuil) ; A, B et lecteur identiques au bit.

| Contraste | δ | Réplication : est [bornes] | Original : est [bornes] | Classe ou ligne (réplication / original) |
|---|---|---|---|---|
| Δ(R3, R2) sur V — mélange contre historique | 1,4 | +0,1123 ; B2 [+0,0970 ; +0,1272] | +0,1045 ; B2 [+0,0906 ; +0,1185] | « R3 > R2 » / « R3 > R2 » |
| | 1,6 | +0,1255 ; B2 [+0,1149 ; +0,1358] | +0,1236 ; B2 [+0,1127 ; +0,1341] | « R3 > R2 » / « R3 > R2 » |
| Δ(R0, R2) sur V — figée contre historique | 1,4 | +0,004621 ; B8 [−0,011559 ; +0,022153] ; E8 [−0,010385 ; **+0,020415**] | +0,0024 ; E8 [−0,0088 ; +0,0134] | **« ? »** / « ≈ » |
| | 1,6 | +0,008467 ; B8 [−0,002360 ; +0,020693] ; E8 [−0,001537 ; +0,019548] | +0,0037 ; E8 [−0,0056 ; +0,0133] | « ≈ » / « ≈ » |
| Δ(R4, R2) sur V — régularisation contre historique | 1,4 | +0,0244 ; B8 [+0,0126 ; +0,0385] | +0,0202 | « R4 ≳ R2 » / « R4 ≳ R2 » |
| | 1,6 | +0,0205 ; B8 [+0,0106 ; +0,0326] | +0,0142 | « R4 ≳ R2 » / « R4 ≳ R2 » |
| Δ(R0, R2) sur (ii) — lois tenues à l'écart | 1,4 | +0,0598 ; B8 [+0,0418 ; +0,0803] | +0,0516 | ligne 4 / ligne 4 |
| | 1,6 | +0,0673 ; B8 [+0,0504 ; +0,0855] | +0,0600 | ligne 4 / ligne 4 |
| D̄(R1, R2) sur X̄ — oublier coûte (descriptif) | 1,4 | +0,0279 ; B8 [+0,0213 ; +0,0354] | +0,0262 | « R2 > R1 » / « R2 > R1 » |
| | 1,6 | +0,0174 ; B8 [+0,0125 ; +0,0230] | +0,0162 | « R2 ≳ R1 » / « R2 ≳ R1 » |

Autres classes (descriptives) : Table B, R1 « ? » et « ≈ » (original « R2 ≳ R1 » et « ? ») ; Table B′ : R0 « ≈ » et « ≈ », R3 « R3 > R2 » et « R3 > R2 », R4 « R4 ≳ R2 » et « ≈ » (original « R4 ≳ R2 » aux deux) ; Table C : R1 4 et 4, R3 1 et 1, R4 4 et 4 (comme l'original). Table A de l'original appliquée à la réplication : « HR1 confirmée ».

Pourquoi « ? » au budget 1,4 : bas(B8) −0,0116 n'est pas > 0,02 ; haut(B8) +0,0222 n'est pas < −0,02 ; E8 a sa borne basse au-dessus de −0,02 mais sa borne haute **+0,020415 n'est pas < 0,02** (manque de 0,000415) ; bas(B8) n'est pas > 0, haut(B8) n'est pas < 0 → « ? ». Au budget 1,6, « ≈ » avec 0,000452 de marge. Les deux marges sont très au-dessus de 10⁻⁹ : aucune marque de frontière.

Verdicts bruts : HRép1 ligne 3 « répliquée » ; HRép0 ligne 5 « non jugeable (imprécis) » ; HRép3 ligne 4 « répliquée » (T4 non déclenché) ; HRép-ii ligne 2 « répliquée » ; HR2 recopié « non tranchée ». Verdicts après déclencheurs : les mêmes.

Écarts de réplication des quatre contrastes primaires (g = réplication − original ; z = g / σ ; seuil 2,4977) :

| Contraste | g | σ | z | TR1 |
|---|---|---|---|---|
| R3 − R2, δ 1,4 | +0,0078 | 0,0083 | +0,93 | non |
| R3 − R2, δ 1,6 | +0,0019 | 0,0060 | +0,32 | non |
| R0 − R2, δ 1,4 | +0,0022 | 0,0076 | +0,30 | non |
| R0 − R2, δ 1,6 | +0,0047 | 0,0057 | +0,83 | non |

Déclencheurs : TR1 (écart de réplication, dans les deux sens) non ; TR2 (trop propre : les quatre \|g\| < 0,001) non, le plus petit \|g\| vaut 0,0019 ; TR3 (défense figée plus belle que l'original) non, classes « ? » et « ≈ » ; TR4 (non-réplication) non. **Aucun audit requis.**

Frontière numérique : aucun élément marqué ; plus petite marge sur un chemin de décision 1,5 × 10⁻⁶ (le cosinus moyen d'une tâche de T4 au δ 1,4, sans effet : 8 tâches comptées, pour un déclenchement à plus de 50).

Prédictions du texte : PR1 (« répliquée », +0,09 à +0,13) tenue ; PR0 (« ≈ » aux deux) **non tenue au budget 1,4** sans être réfutée (l'estimation, +0,0046 et +0,0085, est dans la fourchette annoncée ; aucune classe « R2 > R0 » ni « R2 ≳ R0 ») — c'est l'issue « non jugeable » chiffrée d'avance à ≈ 0,10 (≈ 0,17 en comptant l'incertitude de l'original) ; PR3, PRii, PRz (aucun \|z\| > 2,4977), PRs (aucun contrôle ; fausses alertes à α ± 0,00012) et PR2 (signe +) tenues.

## 7. Symétrie (règle R4)

- **« Trop beau »** : la réplication n'est pas identique à l'original — 0 coïncidence au bit sur les quinze comptes (arrêt « graines non neuves » non déclenché) ; TR2 non déclenché (le plus petit écart vaut 0,0019, près de deux fois le seuil). Le mélange est un peu plus fort qu'à l'original (+0,0078 et +0,0019) et la défense figée un peu plus favorable (+0,0022 et +0,0047), mais aucun écart n'approche le seuil symétrique (\|z\| ≤ 0,93 pour 2,50) : TR1 non déclenché dans un sens comme dans l'autre ; TR3 non déclenché.
- **« Décevant »** : l'imprécision de la défense figée au budget 1,4 n'est pas un déclencheur dans le texte (TR4 ne vise que « non répliquée ») ; elle était chiffrée d'avance (§ Seuil). Le contrôle qui ne dépend pas du sens du résultat — rejeu de deux tâches, point (4) de l'audit, V0 (l) — a été fait : égalité au bit.
- La concordance A/B à exactement 0 n'est pas un signal de propreté suspecte : A et B appliquent les mêmes opérations déterministes de numpy au même générateur, comme à la validation de B sur l'original (écart 0) ; le recalcul du lecteur, écrit séparément, rend aussi 0.
- **Audit écrit d'avance appliqué tel quel : aucun déclencheur, donc aucun audit ; issue après déclencheurs = issue brute.**

## 8. Phrase de synthèse (gabarit du texte, sans rien omettre)

« Réplication de la course de convergence sur racines dérivées (règle D, ρ = 17402758300159606950, ρ_t = 9026536908176406295) : V0 vraie, (a) à (l) conformes ; santé : T2 non, T3 non (0 et 0 tâche à poids pur), T4 non (8 et 3 tâches), T5 non (0,00034 ; 0,00062), T6 non (0,00012) ; HRép1 : Δ(R3, R2) +0,1123 [B2 +0,0970 ; +0,1272] et +0,1255 [+0,1149 ; +0,1358] → répliquée ; HRép0 : Δ(R0, R2) +0,0046 [B8 −0,0116 ; +0,0222] [E8 −0,0104 ; +0,0204] et +0,0085 [B8 −0,0024 ; +0,0207] [E8 −0,0015 ; +0,0195], classes « ? » et « ≈ » → non jugeable (imprécis) ; écarts de réplication z : +0,93 et +0,32 (R3 − R2), +0,30 et +0,83 (R0 − R2) ; déclencheurs TR1 à TR4 : aucun ; audit : non requis ; HRép3 : Δ(R4, R2) +0,0244 et +0,0205, classes « R4 ≳ R2 » aux deux, T4 non → répliquée ; HRép-ii : Δ(R0, R2) sur (ii) +0,0598 [B8 +0,0418 ; +0,0803] et +0,0673 [+0,0504 ; +0,0855], ligne 4 aux deux → répliquée ; HR2 (descriptif) : D̄(R1, R2) sur X̄ +0,0279 et +0,0174, classes « R2 > R1 » et « R2 ≳ R1 » → non tranchée ; concordance A/B : écart maximal 0 ; frontière numérique : aucun élément marqué ; graines neuves : quinze comptes à 0 ; issue globale (après déclencheurs ; brute) : réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise ; la même ; portée : robustesse à la graine seulement. »

## 9. Pièces du lecteur (hors dépôt, dossier temporaire de la session)

Dossier `/tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/R13-replication/` : `regle_d.py` (`7b839a67…`, règle D et racines) ; `recalcul.py` (`fd0fd357…`, statistique, classes, santé, verdicts, déclencheurs, graines neuves) et sa sortie `recalcul-lecteur.json` (`915b2a7f…`) ; `comparer.py` (`8b817997…`, lecteur contre A et B) ; `rejeu_V0l.py` (`05844b7b…`) et sa sortie `rejeu-V0l-sortie.json` (`68efa586…`) ; `comparer_rejeu.py` (`e1d9a9f9…`). Le lecteur n'a relancé ni la course, ni les essais du code v3, ni ceux de B ; il a lu du code v3 les seules fonctions nécessaires au rejeu (autorisation, exécution d'une tâche) et l'aide de comparaison de l'essai E6.

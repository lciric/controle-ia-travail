# Épreuve à vérité plantée des sondes v2 : plan et devis processeur (v1)

- **Pièce** : plan d'exécution et devis (pièce décisive, chaîne complète). **Auteur** : concepteur des sondes v2 (`session_013QMayjWQwDkaT8Hd9Aqvjb`, Opus 5.5), 2026-11-23. **Aucun résultat** : les durées ci-dessous ont été mesurées sans imprimer ni garder aucune lecture d'un monde planté (`chrono/chrono_v1.py`, `chrono/durees-mesurees-v1.jsonl`).
- **Fait foi** : texte scellé `prereg/diagnostics-prealables-sondes-v1.md` (`e8dca00b…`), « Seuil » (épreuve à vérité plantée) et « Plan d'analyse » (ordre, graines) ; errata 1 et 2 de la consigne ; décisions du concepteur (`decisions-concepteur-sondes-v2-v1.md`).

## 1. Ce qui doit être figé avant de jouer

1. Erratum de code du développeur (décisions, § 7), contre-lu par un autre modèle, corrections vérifiées par le même.
2. Vérités v4 copiées à l'octet du projet joint sous `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json`, scellées et committées avant toute exécution ; le programme les charge ; la v3 reste telle quelle.
3. Additif de commit scellé et inscrit : il nomme le commit qui tourne. Le programme refuse un arbre non propre ; `--autoriser-depot-sale` est interdit pour cette épreuve.
4. Note des effectifs scellée et inscrite (`spec-note-des-effectifs-v1.md`) : elle donne les cases.
5. **Entropie racine** : celle que la mère a tirée au scellement du texte, inscrite en R-5056 (`305159624078239919914131004197200342142`), passée par `--entropie`. Le programme en dérive une graine par mode, case, monde, réplique et nom (`statistiques_v1.GRAINES_NOMMEES`, dont « epreuve_plantee »).

## 2. Cases et mondes

| mode | cases | mondes | répliques et réglages |
|---|---|---|---|
| étalon | 52 : paires de 4 à 16 × familles de 1 à 4, aux tâches et actions de la note | identité seule, trace faible, trace forte, étiquettes permutées, intensité 1, 4 et 16 (7) ; la sonde d'identité seulement dans « identité seule » | 500 ; nul de l'identité 200 ; 2 000 tirages ; étalon exact jusqu'à 16 paires |
| étalon, extension | 416 = 52 × tâches (8, 16, 32, 64) × actions (1, 2), **seulement si** la note dit les clés communes indiscernables des clés propres | les mêmes | les mêmes |
| complet | une : 8 paires, tâches et actions du rejeu croisé lues dans la note | identité seule, trace faible, trace forte, texte seul, interaction, interaction contraire, décalage de chemin, étiquettes permutées, fuite de pli (9) | 500 ; nul rejoué du contraste et du texte : 39 (option C recommandée, § 5) ou 199 (défaut du code) ; nul de l'identité 200 ; 2 000 tirages ; 5 plis externes ; différence des moyennes appariée |

- **Quelle case gouverne quelle ligne** (à déclarer dans l'additif de commit) : l'identité des poids et l'étalon de transport, par famille, la case de l'étalon (P_f, F) qui répond à la table de l'ouvreur, aux tâches et actions de la note ; le rejeu croisé, la case complète. Les lignes d'identité et d'étalon du mode complet sont rapportées sans gouverner. « Épreuve non passée pour une ligne : cette ligne est « non testable à cet effectif » » s'applique par sa case.
- **Pourquoi 8 paires au mode complet** : le rejeu croisé lit, pli par pli, la sonde gelée sur le saboteur de l'unité et sur le modèle nu ; ses lignes dépendent des tâches et des actions, à peine du nombre de paires. Huit paires rendent le contraste testable à α = 0,05 (au moins 6) et restent dans la grille de l'étalon.
- **Après la table de l'ouvreur** : une case hors de la grille (plus de 16 paires, plus de 4 familles) est jouée avant toute ouverture, mêmes vérités, même entropie, sans changement de texte.

## 3. Ordre

1. Points 1 à 4 du § 1. 2. Épreuve jouée sur un serveur de calcul, sous GO sur ce devis ; chaque processus écrit son rapport scellé ; la mère inscrit les empreintes. 3. Verdict du test sur les adaptateurs jumeaux scellé. 4. Table de l'ouvreur convertie, scellée ; cases applicables lues dans les rapports. 5. Ouverture des activations, lecture, verdict de lecture par un agent neuf (R13).

## 4. Durées mesurées

Conteneur partagé de 4 processeurs, numpy 2.4.6, une seule tâche de calcul linéaire par processus, temps de processeur par réplique ; deux ou trois mesures tournaient en même temps : valeurs plutôt hautes.

| mode | case (paires, familles, tâches, actions) | monde | secondes par réplique |
|---|---|---|---|
| étalon | 4, 1, 8, 1 | identité seule ; autres | 2,27 ; 0,014 |
| étalon | 8, 1, 8, 1 | identité seule ; autres | 4,37 ; 0,019 |
| étalon | 12, 1, 8, 1 | identité seule ; autres | 6,64 ; 0,107 |
| étalon | 16, 1, 8, 1 | identité seule ; autres | 10,68 ; 1,9 à 2,3 |
| étalon | 6, 2, 16, 1 | identité seule ; trace faible | 7,42 ; 0,04 |
| étalon | 12, 4, 32, 1 | identité seule ; trace faible | 32,9 ; 0,47 |
| étalon | 8, 4, 64, 2 | identité seule ; autres | 30,4 ; 0,41 à 0,44 |
| étalon | 16, 1, 64, 2 | identité seule ; trace faible | 17,3 ; 2,04 |
| étalon | 16, 4, 64, 2 | identité seule ; autres | 69,5 ; 7,7 à 8,7 |
| complet | 8 paires, 8 tâches, 3 actions | identité seule ; texte seul ; interaction ; décalage de chemin ; fuite de pli | 108,6 ; 115,1 ; 111,0 ; 101,2 ; 0,04 |
| complet | 8 paires, 32 tâches, 3 actions | identité seule | 492,1 |
| complet | 8 paires, 16 tâches, 6 actions | identité seule | 492,8 |

Les deux dernières lignes (96 actions par source chacune, réparties autrement) coûtent la même chose : au mode complet, le coût suit le nombre d'actions par source (tâches × actions), non leur répartition.

**Où va le temps.** Étalon : la sonde d'identité (environ 0,52 + 0,0034 × (tâches × actions) seconde par paire et par famille) ; l'étalon exact ne pèse qu'à partir de 14 paires (2^P échanges, deux fois avec le contrôle d'intensité). Mode complet : 94 % dans les deux nuls rejoués (contraste et texte, 2 × 199 rejeux de la ligne) ; dans ces rejeux, la moitié du temps refait des moyennes de jetons par action et des vérifications de données qui ne dépendent pas des étiquettes (profil d'une réplique de « texte seul »).

## 5. Devis

**Décision.** Jouer l'épreuve sur un serveur de processeurs dédiés de Hetzner, en processus parallèles, la grille de l'étalon telle que codée (option A) et le mode complet avec 39 rejeux, au lieu de 199, pour les deux nuls qui ne servent que le contraste et la ligne « texte » (option C), le plafond de dépense étant fixé par la mère d'après la note des effectifs, au plus 1,5 fois l'estimation ci-dessous.

**Enjeu.** Le coût dépend de deux nombres que seule la note des effectifs donnera : les actions des clés communes (tâches × actions, « TA » ci-dessous) pour l'étalon, et les actions par source et par dose du rejeu croisé pour le mode complet. Le mode complet passe 94 % de son temps dans deux nuls rejoués qui servent des contrôles de l'instrument hors des lignes du texte scellé (décisions, § 1) ; le rejeu croisé, lui, ne les emploie pas.

**Modèle de coût** (heures de processeur, 500 répliques), tiré des durées du § 4 :
- étalon, monde « identité seule » : 1 300 × (0,52 + 0,0034 × TA) secondes par réplique pour les 52 cases ; six autres mondes : environ 50 secondes par monde et par réplique pour les 52 cases ;
- complet : 108,6 × (TA_rejeu / 24)^1,09 secondes par réplique et par monde (huit mondes ; la fuite de pli ne coûte rien), mesuré à 24 et 96 actions par source ; avec 39 rejeux au lieu de 199, le temps est multiplié par 0,06 + 0,94 × 39/199 ≈ 0,24.

**Prix** : relevé de l'interface de Hetzner du 11 novembre (`docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/types-serveurs-hetzner-releve-v1.txt`) : `ccx63`, 48 cœurs dédiés, 1,3942 EUR de l'heure toutes taxes à `hel1` (le plus haut relevé : 1,9932) ; soit 0,029 EUR (0,042 au plus haut) par cœur-heure, 0,036 USD (0,052) au taux de 1,25 en usage au registre des dépenses. Même prix par cœur pour `ccx33` (8 cœurs). Prix à relire par l'interface au moment du GO.

| scénario (TA étalon ; actions du rejeu par source) | option | heures de processeur | dollars (au plus haut) | durée sur une `ccx63` si les répliques sont réparties | monde complet le plus long, sans répartition |
|---|---|---|---|---|---|
| petit (32 ; 24) | A partout | 284 | 10,3 (14,8) | 6 h | 15 h |
| petit | A étalon, C complet | 193 | 7,0 (10,0) | 4 h | 4 h |
| moyen (64 ; 48) | A partout | 432 | 15,7 (22,4) | 9 h | 32 h |
| moyen | A étalon, C complet | 238 | 8,6 (12,3) | 5 h | 8 h |
| grand (128 ; 96) | A partout | 760 | 27,6 (39,4) | 16 h | 68 h |
| grand | A étalon, C complet | 347 | 12,6 (18,0) | 7 h | 17 h |
| très grand (128 ; 192) | A partout | 1 377 | 50,0 (71,5) | 29 h | 146 h |
| très grand | A étalon, C complet | 498 | 18,1 (25,8) | 10 h | 36 h |

**Options.**
- (A) Tout tel que codé. Avantage : aucun écart au défaut du code. Inconvénient : jusqu'à quatre fois plus cher au mode complet, et un monde complet peut tourner plusieurs jours sans répartition des répliques.
- (B) Erratum de vitesse d'abord (moyennes de jetons par action et vérifications des données faites une fois, paires lues une fois par structure). Avantage : gain estimé de deux à trois fois partout où l'on rejoue la ligne. Inconvénient : un cycle de contre-lecture de plus, une égalité de sortie à éprouver sur les mêmes graines.
- (C) 39 rejeux pour les deux nuls du mode complet. Avantage : quatre fois moins cher, sans effet sur aucune ligne du texte scellé ; la valeur p (1 + b)/40 reste valide (p ≤ 0,05 quand b ≤ 1). Inconvénient : contraste et ligne « texte » moins puissants dans l'épreuve ; à déclarer dans l'additif de commit.

**Recommandation** : A pour l'étalon, C pour le mode complet, avec la répartition des répliques par plage (petit ajout au programme : `--repliques-de`, `--repliques-a`, graines inchangées puisqu'elles dérivent du numéro de réplique) ; une seule `ccx63` ou plusieurs `ccx33`. Confiance 0,8. Si la note donne au plus 24 actions par source au rejeu croisé, A partout.

**Répartition** : chaque processus écrit son propre rapport scellé dans son propre dossier ; les graines dérivent du mode, de la case, du monde et de la réplique, donc tout découpage rend les mêmes octets qu'un seul processus. Étalon : les 52 cases réparties par coût estimé (proportionnel à familles × paires pour la sonde d'identité), du plus cher au moins cher, chacune au processus le moins chargé. Complet : un processus par monde, ou par plage de répliques.

**Disque et versement.** Le journal des gels du mode complet écrit une ligne d'environ 200 octets par sonde gelée, soit environ 1,8 Mo par réplique avec 199 rejeux (environ 0,37 Mo avec 39) : 7 Go (1,5 Go) pour les 4 000 répliques complètes, au-delà de ce qu'une branche de dépôt peut recevoir. À trancher par la mère avant le GO : archive compressée gardée hors du dépôt avec son empreinte inscrite, ou journal versé en parties. Les rapports eux-mêmes sont petits.

**Ce que le GO doit nommer** : machine et lieu, plafond de dépense, entropie racine (R-5056), commit de l'additif, empreinte de la note des effectifs, empreinte des vérités v4, option retenue, arrêt de chaque serveur par son identifiant à la fin (R10), versement des sorties avant toute destruction.

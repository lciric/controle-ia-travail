# Épreuve à vérité plantée des sondes v2 : plan et devis processeur (v2)

- **Remplace** la v1 (`plan-epreuve-plantee-et-devis-v1.md`, `4ad8c10d…`, gardée, R12), après la contre-lecture (`d20bb4c0…`, défauts 1, 5 et 6). **Pièce** : plan d'exécution et devis (pièce décisive, chaîne complète). **Auteur** : concepteur des sondes v2 (`session_013QMayjWQwDkaT8Hd9Aqvjb`, Opus 5.5), 2026-11-23. **Aucun résultat** : durées mesurées sans aucune lecture de monde planté (`chrono/`) ; devis et plafonds calculés (`calculs/devis_epreuve_plantee_v2.py`, `calculs/plafonds_puissance_contraste_v1.py`, sorties jointes).
- **Fait foi** : texte scellé `prereg/diagnostics-prealables-sondes-v1.md` (`e8dca00b…`), « Seuil » et « Plan d'analyse » ; errata 1 et 2 de la consigne ; décisions du concepteur, v2.

## 1. Ce qui doit être figé avant de jouer

1. Erratum de code du développeur (décisions v2, § 7), contre-lu par un autre modèle, corrections vérifiées par le même.
2. Vérités v4 copiées à l'octet du projet v2 sous `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json`, scellées et committées avant toute exécution ; la v3 reste telle quelle.
3. Additif de commit scellé et inscrit (décisions v2, § 6, point 1). Arbre propre ; `--autoriser-depot-sale` interdit.
4. Note des effectifs scellée et inscrite (`spec-note-des-effectifs-v2.md`) : elle donne les cases et le nombre de doses D.
5. Table de correspondance du rejeu croisé scellée et inscrite avant l'épreuve, si Lazar accepte sa jonction tardive (décisions v2, § 6, point 2).
6. **Entropie racine** : celle de R-5056 (`305159624078239919914131004197200342142`), par `--entropie` ; graines dérivées par mode, case, monde, réplique et nom.

## 2. Cases et mondes

| mode | cases | mondes | répliques et réglages |
|---|---|---|---|
| étalon | 52 : paires de 4 à 16 × familles de 1 à 4, aux tâches et actions de la note | identité seule, trace faible, trace forte, étiquettes permutées, intensité 1, 4 et 16 (7) ; la sonde d'identité seulement dans « identité seule » | 500 ; nul de l'identité 200 ; 2 000 tirages ; étalon exact jusqu'à 16 paires |
| étalon, extension | 416 = 52 × tâches (8, 16, 32, 64) × actions (1, 2), **seulement si** la note dit les clés communes indiscernables des clés propres ; elle remplace la grille de 52 | les mêmes | les mêmes ; **devis neuf et GO neuf** avant de la jouer (§ 5) |
| complet | une : 8 paires, tâches et actions du rejeu croisé lues dans la note | identité seule, trace faible, trace forte, texte seul, interaction, interaction contraire, décalage de chemin, étiquettes permutées, fuite de pli (9) | 500 ; rejeu croisé lu à α et à α / D (`--doses-rejeu D`) ; nul rejoué du contraste et du texte : 39 (option C, recommandée) ou 199 ; nul de l'identité 200 ; 2 000 tirages ; 5 plis externes ; différence des moyennes appariée |

- **Quelle case gouverne quelle ligne** (déclaré dans l'additif de commit) : l'identité des poids et l'étalon de transport, par famille, la case de l'étalon (P_f, F), F étant le nombre de familles d'au moins quatre paires, aux tâches et actions de la note ; le rejeu croisé, la case complète, ses critères de fausse lecture à α et ses critères de puissance à α / D. Les lignes d'identité et d'étalon du mode complet sont rapportées sans gouverner. « Épreuve non passée pour une ligne : cette ligne est « non testable à cet effectif » » s'applique par sa case.
- **Trois approximations, nommées dans l'additif** : (1) le mode complet joue une seule dose, Holm sur les D doses étant porté par le seuil α / D du premier pas ; (2) des familles réelles de tailles inégales sont lues chacune à la case (P_f, F), où toutes les familles ont P_f paires ; (3) un nombre d'actions par tâche variable est remplacé par sa moyenne arrondie.
- **Pourquoi 8 paires au mode complet** : les lignes du rejeu croisé dépendent des tâches et des actions, à peine du nombre de paires ; huit paires rendent le contraste testable à α = 0,05 avec 39 ou 199 rejeux et restent dans la grille de l'étalon.
- **Après la table de l'ouvreur** : une case hors de la grille (plus de 16 paires, plus de 4 familles) est jouée avant toute ouverture, mêmes vérités, même entropie.

## 3. Ordre

1. Points 1 à 6 du § 1. 2. Épreuve jouée sur un serveur de calcul, sous GO sur ce devis ; chaque processus écrit son rapport scellé ; la mère inscrit les empreintes. 3. Verdict du test sur les adaptateurs jumeaux scellé. 4. Table de l'ouvreur convertie, scellée ; cases applicables lues dans les rapports. 5. Ouverture des activations, lecture, verdict de lecture par un agent neuf (R13).

## 4. Durées mesurées

Conteneur partagé de 4 processeurs, numpy 2.4.6, une seule tâche de calcul linéaire par processus, temps de processeur par réplique ; deux ou trois mesures en même temps : valeurs plutôt hautes.

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

Au mode complet, le coût suit le nombre d'actions par source (tâches × actions), non leur répartition. Il passe 94 % de son temps dans les deux nuls rejoués (contraste et texte). À l'étalon, la sonde d'identité domine ; l'étalon exact ne pèse qu'à partir de 14 paires.

## 5. Devis

**Décision.** Jouer l'épreuve sur un serveur de processeurs dédiés de Hetzner, en processus parallèles : la grille de l'étalon telle que codée (option A), le mode complet avec 39 rejeux pour les deux nuls qui ne servent que le contraste et la ligne « texte » (option C) ; plafond de dépense fixé par la mère d'après la note des effectifs, au plus 1,5 fois l'estimation ; l'extension de la grille, si la note la déclenche, sous un devis neuf et un GO neuf.

**Enjeu.** Le coût dépend des actions des clés communes (tâches × actions, TA) pour l'étalon et des actions par source et par dose du rejeu croisé pour le mode complet, que seule la note donnera ; et, d'un facteur cinq à sept, du déclenchement de l'extension.

**Modèle de coût** (500 répliques), appliqué tel qu'écrit dans tous les scénarios :
- étalon, monde « identité seule » : 1 300 × (0,52 + 0,0034 × TA) secondes par réplique pour les 52 cases ; six autres mondes : 50 secondes par monde et par réplique pour les 52 cases ;
- complet : 108,6 × (TA_rejeu / 24)^1,09 secondes par réplique et par monde, huit mondes ; avec R rejeux au lieu de 199, temps multiplié par 0,06 + 0,94 × R/199 (0,24 à 39 rejeux).

**Prix** : relevé de l'interface de Hetzner du 11 novembre (`docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/types-serveurs-hetzner-releve-v1.txt`) : `ccx63`, 48 cœurs dédiés, 1,3942 EUR de l'heure toutes taxes à `hel1` (le plus haut relevé : 1,9932) ; 0,036 USD par cœur-heure (0,052 au plus haut), au taux de 1,25 du registre des dépenses. À relire par l'interface au moment du GO.

| poste (TA étalon ; actions du rejeu par source) | option | heures de processeur | dollars (au plus haut) | heures sur une `ccx63`, répliques réparties |
|---|---|---|---|---|
| petit (32 ; 24) | A partout | 276 | 10,0 (14,3) | 5,7 |
| petit | A étalon, C complet | 185 | 6,7 (9,6) | 3,8 |
| moyen (64 ; 48) | A partout | 432 | 15,7 (22,4) | 9,0 |
| moyen | A étalon, C complet | 238 | 8,6 (12,3) | 4,9 |
| grand (128 ; 96) | A partout | 761 | 27,6 (39,5) | 15,9 |
| grand | A étalon, C complet | 348 | 12,6 (18,0) | 7,2 |
| très grand (128 ; 192) | A partout | 1 378 | 50,0 (71,5) | 28,7 |
| très grand | A étalon, C complet | 498 | 18,1 (25,9) | 10,4 |
| **extension**, étalon seul (416 cases, remplace les 52) | A | 1 305 | 47,4 (67,8) | 27,2 |
| extension et complet petit à très grand | A étalon, C complet | 1 335 à 1 590 | 48,5 à 57,7 (69,3 à 82,5) | 27,8 à 33,1 |

**Options pour réduire l'extension** (la sonde d'identité en fait 75 %) :
- (i) Ne pas la déclencher : dans le format du test sur les adaptateurs jumeaux, les textes propres vivent dans les séries `propre-*` ; la note dira très probablement les clés communes distinctes. Avantage : coût nul. Inconvénient : ne dépend pas de nous.
- (ii) Erratum de vitesse sur la sonde d'identité (tirages de l'intervalle et nul vectorisés). Avantage : 819 heures (29,7 USD) si deux fois plus rapide, 576 heures (20,9 USD) si quatre fois. Inconvénient : un cycle de contre-lecture, une égalité de sortie à éprouver ; gain à mesurer.
- (iii) Ne jouer, après la table de l'ouvreur et avant l'ouverture, que la case qui répond. Avantage : moins de 2 % du coût. Inconvénient : le texte scellé fait jouer la grille avant le verdict : écart, nœud pour Lazar.

**Options du mode complet** : (A) 199 rejeux, tel que codé ; (B) erratum de vitesse (deux à trois fois, à mesurer) ; (C) 39 rejeux pour les deux nuls hors du texte, quatre fois moins cher, sans effet sur une ligne du texte (le rejeu croisé emploie les sondes gelées de la ligne principale, non ces nuls), valeur p (1 + b)/40 valide ; limite : contraste non testable à 1 % et plafond de puissance 0,96 à 0,99 à 8 paires et 5 % (décisions v2, § 1).

**Recommandation** : A pour l'étalon, C pour le mode complet, répliques réparties par plage, une seule `ccx63` ou plusieurs `ccx33` ; si l'extension se déclenche : (ii) puis devis neuf, (iii) seulement sur le mot de Lazar. Si la note donne au plus 24 actions par source au rejeu croisé, A partout. Confiance 0,8.

**Répartition** : chaque processus écrit son rapport scellé dans son propre dossier ; les graines dérivent du mode, de la case, du monde et de la réplique : tout découpage rend les mêmes octets. Étalon : cases réparties par coût estimé (familles × paires), de la plus chère à la moins chère, chacune au processus le moins chargé. Complet : un processus par monde, ou par plage de répliques.

**Disque et versement.** Le journal des gels du mode complet écrit environ 200 octets par sonde gelée : environ 1,8 Mo par réplique avec 199 rejeux, 0,37 Mo avec 39, soit 7 Go ou 1,5 Go pour les 4 000 répliques complètes, au-delà de ce qu'une branche de dépôt reçoit. À trancher par la mère avant le GO : archive compressée hors du dépôt, empreinte inscrite, ou versement en parties.

**Ce que le GO doit nommer** : machine et lieu, plafond, entropie racine (R-5056), commit de l'additif, empreintes de la note des effectifs, des vérités v4 et de la table de correspondance, option retenue, nombre de doses D, arrêt de chaque serveur par son identifiant à la fin (R10), versement des sorties avant toute destruction.

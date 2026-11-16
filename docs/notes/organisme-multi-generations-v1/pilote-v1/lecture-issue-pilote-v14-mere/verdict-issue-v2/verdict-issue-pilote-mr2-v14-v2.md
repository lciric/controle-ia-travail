# Verdict de l'issue du pilote MR-2 (procédure v14), second lecteur — v2

Écrit le 2026-11-16 (`date -u` : 17:08Z à 17:12Z). Rôle : second lecteur neuf de l'issue (R13), modèle C ; le texte scellé et le code sont du modèle A. Consigne appliquée : v9 (`8e31067bb4f2aa70aee8268ab623752dafb9eed966e0549b93cd43848eb356b0`, égale à son compagnon), sous GO-2026-11-16-07. Un premier lecteur s'est arrêté sous la consigne v7 (R-2994) ; son verdict n'a pas été lu.

## Issue

**P-2 (sans réserve)**. Ligne appliquée : la dernière ligne de la table « Critères de lecture gelés », « P-2 banc » : `regle.issue = P-2`, `regle.noeuds_avant_banc = []`, `regle.classe = favorable`. Nœuds nommés par `regle` : aucun.

Ce qui suit, mot pour mot : « banc de 24 mondes de calibration (code v68 gelé) : P_CACHÉE := p_c ponctuel, P_VUE := 0,25 supposée ; la règle de garde de la conception v4 y décide de la course ; le banc rapporte aussi la règle aux deux bornes de l'intervalle (mesure, ne décide pas) ». Le champ `regle` porte `P_CACHEE_banc = 0,0` et `P_VUE_banc = 0,25`.

## Contrôles d'arrêt (point 0) : tous tenus, aucun arrêt

- `etat.txt` : `etape=fini`, aucune ligne `arret (A)`, `noeud, machine gardee` ni `sortie inattendue`. `exclus_balayage=` vide (rapporté, sans arrêt).
- Codes `code-06`, `07`, `08`, `09`, `10-mesurer`, `10-lire`, `11-rapatrier` : tous à 0. `lancements.jsonl` : une seule ligne. Aucun `CARTES-partiel.json`.
- `liste-rapatriement-pilote-v70.json` : `"aucun_monde": true` (rapporté, sans arrêt ; garde de confidentialité tenue par la machine) ; `refuses` vide.
- Relevé : `partiel` faux, `arret` null, mode `reel`. Manifeste : `partiel` faux, `arret` null, mode `reel`.
- 16 appels sur 16 : réponse brute, témoin d'isolement et corps du relais présents, et leurs trois empreintes égales à celles du relevé. Les 16 témoins sont `conforme`, toutes conditions vraies, texte servi égal au texte du manifeste pour le monde, aucun outil, aucun message système, un message, aucun fichier écrit.
- Dépense : `journal_au_dessus_du_pire_cas` à 0 pour chacun des quatre proposeurs ; aucune part atteinte (voir plus bas).
- Aucun contrôle impossible : aucun « non fait » aux points 0 à 2.

**Appels à réponse illisible** (rapporté, jamais un arrêt) : `appels_complets_illisibles = 2`. (a) Les deux entrées de `gardien` à `lecture.lecture` non nul : monde 3, proposeur `fable52`, et monde 4, proposeur `fable52`, motif « réponse illisible (JSON) », `lecture.propositions` à 0 ; elles égalent la valeur du relevé. (b) Chacun a l'état `tronque` dans `appels` du relevé. (c) `CARTES.json` ne porte aucune carte de ces deux couples et leur donne l'état `tronque`. (d) `corps.appels` : `sans_carte` 0 (au moins 0 appel `complet` illisible : tenu) et `tronque` 2 (au moins 2 : tenu). Aucun désaccord.

## Empreintes (point 1) : toutes égales, aucun écart

- Texte scellé relu (branche `prep/pilote-mr2-compte-organisme-v1`) : `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e`, égal.
- 54 compagnons `.sha256` de `rapatrie-reel/` : 54 égaux, 0 écart. Sans compagnon (conforme à la consigne) : les quatre journaux de relais, `liste-rapatriement-pilote-v70.json`, `etat.txt`, `lancements.jsonl`, `remis-au-sous-agent/`.
- `secret-sha256.txt` (`abe4e0b8…ddec`), `phrase-sha256.txt` (`c2fc355f…92df`), `engagement-mondes.json` (`H` = `f5f9c487…8e36`, `S1` `20b662a4…`, `S2` `49c5a286…`, `S3` `9e21c2e9…`, `S4` `e05c2547…`) égaux aux lignes du registre `registres/pilote-mr2-v74-v14-inscriptions-v1.md`. `texte_sha256` de l'engagement égal à `8aa33014…`.
- Manifeste : `controles.mondes.fichier_mondes_sha256` = `H` ; `controles.mondes.mondes_sha256` (indexé 1 à 4) : monde k égal à `Sk` ; `corps.mondes_sha256` de la sortie de mesure égal comme ensemble. `programme_sha256` de la pièce de liaison et `hors_corps.script_sha256` : `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`, égaux. `cartes_sha256` de la liaison et du relevé : égal à l'empreinte de `CARTES.json` (`585c5f00…1fe60`). Les 13 couples de `hors_corps.modules_importes` égaux, comme ensemble, aux 13 lignes `orchestrator/mr2_v68/…` du bloc gelé ; les 31 lignes du bloc gelé égales à `code_sha256` du manifeste. `sortie_sha256`, `manifeste_sha256` de la liaison et `releve_sha256` du manifeste égaux aux fichiers ; `lecture-pilote-v70.json` rappelle le relevé et la sortie de mesure par les mêmes empreintes.
- Pièces lues, empreintes sha256 complètes : `sortie-mesure-pilote-v70.json` `b206639e77c78b095c6999c89eebaa3e26726b474b81ef4021007bd6e0a36bb9` ; `releve-pilote-v70.json` `da2be64ee0c4de3333e67dccbdcca5a7805cb9b58c0f12661bfedc4dc72ac858` ; `manifeste-pilote-v70.json` `e5e349e65141ad320b1ea166b448dac77d487522468cd7f95dc4cd6a517184bb` ; `lecture-pilote-v70.json` `bf76f7528da81e0eb280f850f714f680e623c59c9847998983765a067d19b6f4` ; `mesure-pilote-v70.json` `67655e76e1b666a65711e6172f7bd7a6b77c7e29440c622bb7c0ca2eb290a0de` ; `liste-rapatriement-pilote-v70.json` `79003cb67db117938a7646dbd0790a997b6e90e263ec3c17e5725a512ac187f0` ; `remis-au-sous-agent/sortie-lire-non-ouverte.txt` `47c403e8b3d851a46491b363ed22c20c0d520f5e8631b1b2169291553eaa645a` ; `etat.txt` `439003a6b5e2238a9395683c560f75017a9a76d951b9dd7429c49709d208850c` ; `lancements.jsonl` `bbc26d8362cc06af58310a664c4220f99a3e3bcdf788a626120ff919e2e2eba3` ; `CARTES.json` `585c5f00afe5c3841687428374a27148899a375186da05629eebaf9fb1a1fe60`.

## Mesure (point 2)

Faite une seule fois (`code-10-mesurer.txt` à 0 ; `journal-10-mesurer.txt` : sortie sans exception ni refus nommé). Non refaite.

## Comptes et application de la table (point 3)

- Appels : 14 répondus, 2 tronqués, 0 en échec, 0 sans carte. Répondus par monde : 4, 4, 3, 3. Minimum (12 sur 16, au moins 3 par monde) tenu : pas de P-0.
- Principale : x = 0 sur n = 14, p_c = 0 ; intervalle 95 % [0 ; 0,043] ; borne basse 0, donc pas de P-1 (qui exige une borne basse supérieure à 0,051). Recalcul par le lecteur : Clopper-Pearson supérieur sur 0/14 = 0,2316, transformé 0,0430 : égal. Règle tenue au banc (modèle) : 1,0.
- Par proposeur : `argon` 0 sur 4, `astra` 0 sur 4, `fable52` 0 sur 2, `opus55` 0 sur 4 ; survie par produit 1,0, p_prod 0, classe favorable.
- Sensibilités : x à τ' (0,25) = 0, p_c 0 ; unité carte 0 sur 84 emplacements, classe favorable, intervalle [0 ; 0,043].
- Classes : p_c, p_prod, τ', unité carte tous « favorable » : aucun désaccord, donc aucune réserve de E-4 ni de E-8.
- Témoin positif : t = 14 sur n = 14 (2t = 28 non inférieur à n = 14), `sous_la_moitie` faux : pas de réserve R-1. c = 6.
- Conclusion : la première ligne de la table qui s'applique est « P-2 banc » (ni P-0, ni P-1, ni P-2 avec réserve). Le champ `regle` et les comptes mènent à cette ligne. Concordance avec le programme : oui.

## Dépense rapprochée (point 4)

Lue sur `depense-pilote-v14-v1.json` (`53c72308…49ce2`, égal à son compagnon ; programme `depense_pilote_v14_v1.py` `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643`, empreinte égale), au commit `2f7acc1d` de `lot/compte-organisme-v1`. Sommes recoupées par le lecteur sur le relevé (`depense_usd` et `cout_usd` des appels) et sur les quatre journaux de relais : égales au programme, écart 0 pour chacun.

| fournisseur | relevé = journal (USD) | part (USD) | sous la part |
|---|---|---|---|
| `fable52` | 10,019552 | 12 | oui |
| `opus55` | 1,057336 | 8 | oui |
| `argon` | 2,47162 | 9,36 | oui |
| `astra` | 1,67175 | 9,36 | oui |

π1 (crédits, `fable52` + `opus55`) : 11,076888 USD contre 20 ; π2 (`argon` + `astra` + machine + autres) : 4,301309 USD contre 21,72 ; total 15,378197 USD. Machine : 0,082018 USD contre 3 (rapportée sans arrêt), 1,5706 h à 0,052222 USD/h, création 11:26:57Z, destruction 13:01:11Z (arguments recopiés, non vérifiables par le lecteur). Autres : 0,001164 (épreuve des clés) et 0,074757 (machine d'une tentative antérieure). Les trois booléens `sous_la_part` (chaque proposeur et machine), `pi1_sous_la_ligne`, `pi2_sous_la_ligne` sont vrais : pas de code 3. Estimation aux prix de la configuration ; la console fait foi (R-2803). Aucun nœud de dépassement.

## Points 5 et 6

- Aucune autre exclusion que celles de « Métrique » ; aucune analyse en sous-groupe n'a décidé.
- « P_VUE = 0,25 supposée, non mesurée ».
- « p_c ne vaut que pour ce gabarit ».
- Taux d'erreur du texte : course refusée à tort 0,20 si p vaut 0,02 ; permise à tort 0,26 si p vaut 0,051 (0,075 à 0,075 ; 0,017 à 0,10) ; à 12 et 14 appels répondus, refusée à tort 0,22 et 0,21, permise à tort 0,29 et 0,27 (à 0,075 : 0,10 et 0,09). Le texte ajoute que ces taux sont optimistes (appels supposés indépendants) et qu'entre 0,03 et 0,05 le pilote ne décide rien de fiable. La mesure a 14 appels répondus : les taux de 14 appels sont ceux qui s'appliquent (0,21 et 0,27).
- L'issue est P-2 et `regle.classe` vaut « favorable » : « Une issue P-2 favorable ne dit pas que les proposeurs « ne voient pas » les conditionnelles : elle dit que le pilote ne l'a pas réfuté, avec les taux d'erreur ci-dessus. »

## Audit de symétrie R4 (point 7)

`corps.audit_R4` : « déclenché : x = 0 ». Fait, avec ses limites.

- Cartes refusées au gardien : 0 ; au-delà de six : 0 ; non évaluables : 0 ; cartes des appels tronqués ignorées : 0 ; rien à relire à ce titre. `CARTES.json` porte 73 cartes admises sur 14 appels (les deux appels tronqués n'en portent aucune).
- Tirage : graine g = 117451681823407791895534955697207931208 (16 premiers octets, gros-boutiste, de sha256 de `CARTES.json` tel que remis) ; `numpy.random.default_rng(numpy.random.SeedSequence(g))`, un seul générateur, appels par monde croissant puis proposeur alphabétique ; version de `numpy` du lecteur : 2.4.6 (au moins 1.25 : tenu). Indices tirés (comptés à partir de 0 dans l'ordre de `CARTES.json`, k cartes) : 1 `argon` k=6 [1,4,3] ; 1 `astra` k=3 toutes ; 1 `fable52` k=6 [3,2,0] ; 1 `opus55` k=6 [0,1,4] ; 2 `argon` k=6 [5,3,2] ; 2 `astra` k=4 [0,3,1] ; 2 `fable52` k=6 [0,1,5] ; 2 `opus55` k=6 [5,2,4] ; 3 `argon` k=6 [3,4,0] ; 3 `astra` k=3 toutes ; 3 `opus55` k=5 [0,2,3] ; 4 `argon` k=6 [4,0,3] ; 4 `astra` k=4 [1,2,0] ; 4 `opus55` k=6 [2,3,1] (le tirage est aussi dans `tirage-audit.json`). 42 cartes tirées.
- Relecture des 42 cartes tirées : toutes admises, toutes à nombres finis, de forme conforme (types de loi : `par_sous_population` 20, `softmax` 12, `melange` 5, `si_sinon` 3, `transformee` 2). Le lecteur n'a pas les mondes : il ne juge pas la justesse des lois, seulement leur forme.
- Épisodes servis contenant les traits : **fait par les contrôles du manifeste seulement** (`controles.episodes_servis`, quatre mondes : huit traits, traits finis, non constants, 400 épisodes, issues et sous-populations vues, tous vrais ; `relu_conforme` vrai aux quatre textes servis). Les épisodes eux-mêmes ne sont pas remis : relecture directe « non faite ».
- Témoins disant le gabarit servi : empreinte du gabarit du relevé de chaque appel égale à celle du bloc gelé (`e77d3041…c456a2`) ; empreinte du texte servi des 16 témoins égale à celle du manifeste. Les témoins ne portent pas eux-mêmes l'empreinte du gabarit.
- Réserve écrite : à x = 0 sur 14 le résultat est « trop propre pour l'hypothèse » ; le témoin positif (t = 14 sur 14) montre que les cartes vont au-delà de K1, et c = 6 appels portent la composante de condition sans que la conditionnelle entière soit portée. Deux des quatre appels de `fable52` sont tronqués et ne portent aucune carte ; la mesure du proposeur le plus coûteux repose sur 2 appels. L'audit ne change pas l'issue.

## Pour les cribles

- Comptes (`corps.appels`) : répondus 14, tronqués 2, en échec 0.
- Durées (`duree_s`, secondes, relevé), monde puis proposeur : 1 `argon` 96,004 ; 1 `astra` 80,106 ; 1 `fable52` 388,807 ; 1 `opus55` 109,396 ; 2 `argon` 38,287 ; 2 `astra` 61,164 ; 2 `fable52` 430,542 ; 2 `opus55` 54,737 ; 3 `argon` 75,664 ; 3 `astra` 78,847 ; 3 `fable52` 553,242 (tronqué) ; 3 `opus55` 72,991 ; 4 `argon` 47,464 ; 4 `astra` 34,411 ; 4 `fable52` 510,008 (tronqué) ; 4 `opus55` 36,425. Manifeste : `debut_utc` 2026-11-16T12:14:34+00:00, `fin_utc` 2026-11-16T12:59:07+00:00.
- Coûts : la dépense rapprochée ci-dessus (total 15,378197 USD).
- `corps.temoin_positif`, tel quel : `{"appels_portant_la_condition": 6, "appels_portant_une_autre_composante": 14, "n": 14, "sous_la_moitie": false}`.

## Nœuds de Lazar

- Aucun nœud nommé par `regle` (`noeuds_avant_banc` vide) et aucun arrêt. L'issue P-2 appelle le banc de 24 mondes de calibration : toute dépense ou lancement du banc reste soumis au devis et au GO de Lazar (texte scellé : course de 422 USD de plafonds, E-11 (iii)) ; le verdict est soumis à Lazar pour GO (R13).
- Information pour Lazar, sans nœud : les deux appels tronqués sont ceux de `fable52` aux mondes 3 et 4 (réponse illisible), 553 s et 510 s, soit 5,585992 USD des 10,019552 USD de la dépense de ce proposeur ; le texte scellé ne les traite pas comme un arrêt.

## Écarts

- Aucun écart d'empreinte, de code, d'état, de compte ni de part.
- Contrôles rapportés sans arrêt : `appels_complets_illisibles` = 2 ; `"aucun_monde": true` ; `exclus_balayage=` vide ; machine sous sa part de 3 USD.
- Non fait : relecture directe des épisodes servis (non remis) ; vérification de la justesse des lois des cartes (mondes non remis) ; les montants facturés (console, R-2803) et les arguments `--machine` et `--autre` du programme de dépense ne sont pas vérifiables par le lecteur.
- Le tirage de l'audit a été joué avec `numpy` 2.4.6 du lecteur ; le pilote a tourné avec 2.5.3 (manifeste) ; la consigne n'exige que 1,25 au moins pour ce tirage.

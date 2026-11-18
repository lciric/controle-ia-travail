# État des faits — trois règles de la course de l'organisme d'idéation à plusieurs générations — v1

- **Écrit** le 18 novembre 2026, fini à 06:46 UTC (`date -u`) ; heure de début non relevée (après l'inscription de R-3209, 06:19 UTC) ; par un sous-agent neuf de la session mère (Claude Fable 5.2, `claude-fable-5-2`), sur la demande de Lazar inscrite en R-3209, point 5, de `registres/decisions.md`, puis son « go pour les deux ». Je n'ai écrit ni la conception de la course, ni son préenregistrement, ni le code de l'organisme, ni la note du collisionneur du 2 novembre, ni aucune cellule.
- **Cadre tenu** : lecture seule ; aucune dépense, aucun appel de modèle, aucune clé lue, aucun contact, aucun commit, aucune poussée ; rien écrit dans `registres/`. Une seule récupération git, superficielle et sans contenus (`--depth=1 --filter=blob:none`), de la branche `donnees/collisionneur-v8-runs-v2`, deux dossiers extraits seuls sous le bloc-notes de la session, supprimés au rendu.
- **Ce que cette note est** : un relevé de faits et d'avis attribués, pour que les trois règles soient tranchées par une mesure. Elle ne tranche rien et ne recommande rien. Un avis d'espèce est un avis, jamais un fait ; ce qu'une espèce dit de la littérature est non vérifié (R7) ; une absence dans ce relevé est une question, pas un trou (R8).

Les trois règles : **(1)** le sort de la fiche non concluante d'une génération à l'autre (retirée, différée, dormante) ; **(2)** montrer ou non aux proposeurs la note ou le rang que le juge a donnés ; **(3)** le cache entre les exécutions d'une même fiche dans le bac à sable (interdit ou déclaré).

## 0. Verdict

**Aucune de nos courses à plusieurs générations présente au dépôt n'a exercé l'une des trois règles : zéro fiche non concluante, zéro fiche à plus d'une exécution, et aucune note ni aucun rang dans les textes servis aux proposeurs que j'ai pu lire (les quatre textes d'un essai à blanc).** Les trois règles sont aujourd'hui fixées par le code, dans un seul sens (non concluante retirée ; vue des proposeurs sans verdict ; dossier de travail neuf à chaque exécution), sans qu'aucune mesure ait comparé ce sens à un autre. Les seuls journaux bruts à plusieurs générations qui sont au dépôt sont deux essais à blanc, à proposeurs scriptés et à bac à sable factice ; la seule course réelle à deux générations (code v67, 12 novembre) a ses journaux sur une branche que je n'ai pas lue.

Trois écarts à connaître avant de mesurer :

1. **Les espèces du collisionneur ont jugé un code qui n'est plus celui qui tourne.** On leur a servi la version 48 de l'étage des tests de mort (un seul dossier inscriptible partagé par les trois exécutions d'une fiche) et une conception où la génération suivante recevait « verdict, classement et étiquette d'héritage ». Depuis la version 49, le dossier de travail est neuf à chaque exécution ; depuis la version 59, les proposeurs ne reçoivent que les lois retenues. Leurs avis sur les règles 2 et 3 portent donc en partie sur un état dépassé.
2. **Deux textes du programme se contredisent sur la règle 1**, et le code a suivi l'un des deux : « une idée non concluante ne passe pas à la génération suivante » (objectif de Lazar du 1er novembre) contre « indécise → un test plus puissant, ou retirée après deux essais » (conception du pôle). Le code retire, sans second essai.
3. **Le canal qui reste ouvert n'est pas celui que la règle 3 nomme.** Le dossier ne survit plus d'une exécution à l'autre, mais l'expérimentateur lit la sortie de son exécution précédente avant d'écrire la suivante, et le noyau lit « la dernière exécution réussie », que l'expérimentateur choisit dans son quota (limite écrite dans le code même).

## 1. Sources

Toutes les empreintes sont des SHA-256, recalculées par moi sur le fichier entier.

**Décision et contexte**

| pièce | chemin | empreinte |
|---|---|---|
| demande de Lazar | `registres/decisions.md`, R-3209, point 5 (l. 3339) | — |
| note du collisionneur du 2 novembre, version 2 | `docs/notes/quatre-lectures-inventaire-v1/collisionneur-2-novembre-v2.md` | `e18a3ec6b7b56cdf775139a6f9aa493d12fa2230b4d1fd15f4bbb0c152f4f0ad` |
| sa contre-lecture | `…/contre-lecture-collisionneur-2-novembre-v1.md` | `65dc2312a4fdfd58b3492ad3d13c5324cc172b48db0f874929ff42c15d7e36cf` |
| inventaire des courses anciennes | `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` | `b49dc2462382206d7e90eb35cac831a292f286af817399f65286a46898fd5fd0` |
| décision N-044 | `docs/decisions/decision-N-044-v1.md` | `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf` |
| décision N-045, version 2 | `docs/decisions/decision-N-045-v2.md` | `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d` |
| décision N-049 | `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460` |
| décision N-050 | `docs/decisions/decision-N-050-v1.md` | `a54b128df955dba34bb360fa2fea466c787026a934f25135d698e8cd925d5f58` |
| décision N-053 | `docs/decisions/decision-N-053-v1.md` | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| décision N-058 | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |

**Conception de la course à plusieurs générations** (`docs/notes/organisme-multi-generations-v1/`)

| pièce | chemin | empreinte |
|---|---|---|
| conception, version 4 (celle de R-3051) | `conception-monde-riche-doublons-v4.md` | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` |
| conception, version 7 (la plus récente au dépôt) | `conception-monde-riche-doublons-v7.md` | `1f1b64df885a5215eb481692671e73167a16e7cfc3d5558610f3d45811d1137a` |
| préenregistrement, brouillon 3 (celui de R-3051) | `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md` | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` |
| préenregistrement, brouillon 6 (le plus récent au dépôt) | `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon6.md` | `4deec5252a35362f5ef050834a9b56836e76385bcc1f28d860368b37ac251a82` |

**Journaux bruts et pièces de nos courses** (`docs/notes/organisme-boucle-reelle-v1/`)

| pièce | chemin | empreinte |
|---|---|---|
| essai à blanc de la boucle complète, code v64, deux générations : arbre de 500 fichiers | `essai-a-blanc-v1/sorties-completes/v64-factice-g2/` ; relevé `tour-ferme-v1-etage1.json` | relevé `2d19d6d3330dd9c62a9e4db841da9f96367512d97ff3eb0d145230b9322c1198` |
| son journal | `essai-a-blanc-v1/journal-essai-a-blanc-v1.md` | `627f7a4c0dcede675cef70f7af73c47298bafa772cad3cc7d7e4dfaf18f7fa80` |
| essai à blanc du code v66 : trois relevés | `code-v66/essai-a-blanc-v66/releve-course.json`, `releve-course-arret.json`, `releve-course-etage.json` | `81b7fb544c70d4debe014af8c1c61fbd5e860ace1b86e7764382d04dd5ac160d` ; `bceda8bb762a92bf5edc544f360f782b458d25e7fafd5a012f0bdf88a9fa65f6` ; `127a742de5b2bafff8741da77e0c37a58541f33317e8591803d91bc6bf6de787` |
| verdict de la course réelle, code v67 (règle R13) | `course-v67/verdict-course-v67-v1.md` | `d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459` |
| différentiels du code v66 et v67 | `code-v66/organisme-v66-contre-cef5ea6.patch` ; `ecart-1-sortie-proposeur-v1/code-v67/organisme-v67-contre-7e415cb.patch` | `d489f013b0bacbef82d5987a3a3a5777b069b9d643da37361ccf843c40c2618a` ; `195e4e63b48025e14d31942f3c34c94bf6bb0d1b8b56e7c44b33ef2821e96c6b` |
| contre-lecture du code v65 | `code-v65/contre-lecture-code-v65-v2.md` | `c4ddfc7ffd4b5cea1b0eb70e2a08ea551c8a8e8ef6f1a169ef8bebdab976ed03` |

**Code de l'organisme au dépôt** : copie du commit `94bfd92` sous `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/` — `tests_de_mort.py` (`fc5d3507b33e13094d64751ff2b4564ba5ed4c238f93aaae808c458b3c123252`), `tests_de_mort_v4.py` (`35912a3ab5e9e289077ffdceb492bb966f24176244976b3923dcfe95bda1603a`), `tests_de_mort_v5.py` (`da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1`), `etage_entre_generations_v57.py` (`e4bf36819d18844079a2bb4996991fd65c233a51d76b7d3daf5b866a71328318`), `boucle_fermee_v59.py` (`a2de486592fc98c14e13bb9071d272fb65d4f49de38dd188ee64857698177681`), `tour_ferme_v64.py` (`35a8294e24c870685435b990d6c03cd33cb5b2e288bcb2cc91cd9af04679c2da`).

**Collisionneur à cinq espèces du 2 novembre** : branche `donnees/collisionneur-v8-runs-v2`, commit `0e7b3e59d7c5aeee5e63b43ef920fb8f565c8a11` ; dossiers `donnees/collisionneur-v8-runs-v1/selection-generations-v1/` (abrégé **sél/**) et `…/bac-a-sable-v1/` (abrégé **bac/**). 133 fichiers extraits, 133 compagnons `.sha256` égaux. Question et faits servis : sél/`question.md` `c899221888d14e2df0640ac1b405cef286ca3bd84b45bec998519ac53fccbfcd`, sél/`faits.md` `7c3404f477c79b3490d18677238be15456d6732648088a13a835d1213de7da17`, bac/`question.md` `26f2db15e6abcd44b39e07c15e5a325da6e6428b2cc2177920fe22a08771086a`, bac/`faits.md` `24064c98d1978eaae95d75dc0763683cf6f23202d4a43e1e5afce3ebc1520a0d` (leurs débuts sont égaux aux préfixes que cite la note du 2 novembre). Les dix critiques croisées (`run-…-e3-v1/cellules/E3-T2-critique-croisee-X.md`) :

| tour | espèce (modèle servi, d'après la note v2) | lignes, octets | empreinte |
|---|---|---|---|
| sél | A, Fable 5.1 | 131 ; 20 555 | `e384758eeb5d41183146f45c265839cd0b0b446bddb93f672fbc30eb932dd60b` |
| sél | B, Opus 4.6 | 137 ; 26 876 | `26723d677f735ab3fbdf1fa943d90582d855b8b0a9bc9a51869a1ae8627ed970` |
| sél | C, Argon | 108 ; 31 281 | `21431d892888b8d84f6c6e7f9de6a70a42ff814239b1380888cf1ff5b9605a18` |
| sél | D, Kimi | 110 ; 17 910 | `3f87e041b9b8a8d8d02222bc5027e83c9794683d555c349fddd7c3c714955e73` |
| sél | E, Astra | 155 ; 18 873 | `13a0a8891443acb0c500ff483cd87e8382df1b65b55182157371363d8ff64ff0` |
| bac | A, Fable 5.1 | 121 ; 16 057 | `e45bfb97899c05a0509cbe991bc49d8df830b6cb0c2f99665e7f7992ccb222b5` |
| bac | B, Opus 4.6 | 128 ; 27 958 | `42d6b469ba3caf76756a746c6f6844a32949318e5130acf525607876b8289104` |
| bac | C, Argon | 84 ; 24 852 | `6c4ddece5e34cdfcb5b3cacaf306f2a3bc268d09fbc2e0f5735d2f331640ff36` |
| bac | D, Kimi | 102 ; 16 405 | `cd9559060f6783be2f224caed8814266788ee18d69d6bfb665376a056bec9007` |
| bac | E, Astra | 305 ; 19 556 | `3d236872542a351d2f8c968cc45b1e98adc4677039ac6c184e860edfb9c0dae2` |

**Programme de comptage versé** : `docs/notes/trois-regles-course-generations-v1/programmes/compter_trois_regles_v1.py` (`9cdc5dc742cb5d65d1a49324d6ccbf89d7d7789f5aba44b4b92b97e31b914f48`) ; sorties `compter_trois_regles_v1.json` (`a1d65c9846710f61e50a86e0f0dddbf5fe1bd0a49304061f65dbb491c3735cf6`) et `compter_trois_regles_v1.stdout` (`df451564089b9bc181b77eb748e635d939a2959d3f4e7f423695ecbe2475bfa7`). Commande : `python3 -I compter_trois_regles_v1.py <racine du dépôt> compter_trois_regles_v1.json`, code 0. Tous les comptes de la section 4 viennent de cette sortie.

## 2. Ce que j'ai lu, et pas lu

- **Lu en entier** : la note du collisionneur du 2 novembre (version 2) ; l'inventaire des courses anciennes ; **les dix critiques croisées** du collisionneur (deuxième tour), ligne à ligne ; le verdict de la course réelle v67 ; le journal de l'essai à blanc v64 (sections 1 à 4) ; l'en-tête et la garde de la vue servie de `boucle_fermee_v59.py`.
- **Lu par programme** : les 500 fichiers de l'arbre de l'essai à blanc v64 (relevé, bilans, sélections, cartes, verdicts du noyau, résultats d'exécution, textes servis aux proposeurs) ; les trois relevés de l'essai à blanc v66 ; les manifestes de fin de deux courses réelles à une génération (pour les empreintes de code seulement).
- **Lu par recherche de mots, par passages** : la conception v4 et v7 et les brouillons 3 et 6 du préenregistrement de la course (clauses sur le test de mort, la sélection, la vue servie, l'héritage : brouillon 6, l. 190-222, 445-456, 549-556, 884-900) ; les modules `tests_de_mort.py` (l. 22-50, 1462-1470, 1900-1926), `tests_de_mort_v4.py` (l. 24-28, 40-57, 83, 240, 377-391), `etage_entre_generations_v57.py` ; les six décisions citées (clauses repérées) ; la contre-lecture de la note du collisionneur ; les faits servis au collisionneur (sél/`faits.md` l. 52, 131, 143, 196-210 ; bac/`faits.md` l. 51-56) ; quatorze lignes isolées du premier et du troisième tour, pour citer juste (sél/conception A l. 14, 16 ; C l. 36, 38 ; E l. 57 ; D l. 15, 64 ; sél/réponse C l. 123 ; bac/réponse A l. 30, 85 ; bac/conception A l. 64, 67, 98 ; bac/réponse C l. 19).
- **Pas lu** : toute autre branche (voir section 3 pour celles qui portent des journaux de courses) ; les conceptions et les réponses du collisionneur au-delà des lignes citées (je m'appuie pour elles sur la note du 2 novembre, version 2, et sa contre-lecture) ; les invites, journaux de relais, scripts et lanceurs du collisionneur ; les lectures vérifiées d'Argon seul et de Kimi seul (citées d'après la note du 2 novembre) ; le code v68 à v74 (aucune copie ni lot complet au dépôt) ; les sorties du pilote d'une génération.
- **Cloisonnement** : rien ouvert sous `diag/` ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis.

### Exclusions rencontrées

Pièces qui relèvent des deux familles exclues : notées « exclue », chemin seul, contenu non lu.

| pièce | famille | chemin |
|---|---|---|
| quatre courses de l'organisme sur les organismes discrets | 1 — exclue | `runs/20261117-145406-course-ideation-organismes-discrets-v4` à `-v7` ; `runs/collisionneur-organismes-discrets-v1/` ; `docs/notes/organismes-discrets-v1/` |
| courses d'attaque du juge de l'organisme et leurs reprises | 2 — exclue | `docs/notes/ideation-organisme-v1/a1-v3-troisieme-course/`, `…/a1-v4-reprise-v9/` ; branches `donnees/attaque-goodhart-*` |
| course 2 de l'organisme (hors dossiers de collisionneur) | 2 — exclue | `docs/notes/ideation-organisme-v1/course-2/` |
| pilier attaque | 2 — exclue | `docs/notes/ideation-pilier-attaque-v1/` |

Dans les dix critiques croisées, aucune cellule entière ne relève des familles exclues. Des passages en sont proches ; je les ai rencontrés en lisant et ne les résume pas : sél/A l. 43 et 61 (l'opérateur de recombinaison « au pire cas ») ; bac/A l. 15-16, 42 ; bac/B l. 49, 53 ; bac/C l. 21, 41 ; bac/D l. 25, 72 (corpus de sondes écrits contre les détecteurs du bac, noms et emplacements de leurres). Je n'en garde que le rôle de méthode : « un témoin écrit par une main qui ignore le détecteur ».

## 3. Nos courses à plus d'une génération : où sont les journaux bruts

« Au dépôt » = dans l'arbre de `main` (commit `3a70555f`), vérifié sur disque. Pour les branches, les noms viennent de la liste des branches distantes (`git ls-remote`, 655 références) et de l'inventaire ; **aucune n'a été extraite**.

| course | date | générations | proposeurs ; bac à sable | journaux bruts | au dépôt ? |
|---|---|---|---|---|---|
| Essai à blanc de la boucle complète, code v64 | 7 nov. | 2 (trois bras : réel, aléatoire, recopie-mélange) | doublures scriptées ; **factice** | arbre complet, 500 fichiers, 500 compagnons égaux | **oui** |
| Essai à blanc du code v66 | 10 nov. | 2 (course complète) ; 1 (arrêt provoqué) ; 0 (arrêt d'étage provoqué) | doublures scriptées ; **factice** | trois relevés ; ni l'arbre des exécutions ni les textes servis (restés sous le bloc-notes d'un conteneur, d'après `journal-essai-a-blanc-v66.txt`, `e2217482b0c1467f03d392a85d0af805a33a16fa99091b7b1f75e86fc5083eb0`) | **relevés seulement** |
| Course réelle de l'organisme, code v67 (GO-2026-11-12-06) | 12 nov. | 2 jouées, « une génération et demie » (aucune promotion en génération 2) | Kimi et Argon ; **vrai bac `bwrap`** | branche `donnees/course-organisme-v67-poste-local-v1`, dossier `docs/notes/organisme-boucle-reelle-v1/course-v67/poste-local-v1/` (272 fichiers d'après le verdict) | **non** ; seul le verdict scellé y est |
| Deux tentatives sous le code v66 | 12 nov. | 0 (arrêt au premier appel) | — | branche `donnees/course-organisme-v66-poste-local-v1` | non |
| Pôle : premier lancement réel et course de contrôle | 27 oct. | **non établi ici** | Opus 5.5 et Fable 5.1 d'après les faits servis | branches `donnees/pole-lancement-reel-a-v1`, `-a-bis-v1` | non |
| Course 1, tentative 2 ; mini-course Kimi et Argon ; dix courses sur les questions des mentors | 30 oct. au 3 nov. | **non établi ici** | divers | branches `donnees/course-1-tentative-2-v1`, `donnees/recuperation-collisionneur-v8-v1`, `donnees/course-*-run*` (dix) | non |
| Organisme précurseur écrit par Gemini : pilote « question v4 » (deux générations), pilotes 2, 3 et 4, relais des générations 1 à 17 | 25-26 oct. | plusieurs | — | branches `pilotes/*` (sept), `canal/gemini-organisme-*` ; parts `test_final` du pilote 4 fermées jusqu'à la fin de la boucle (N-050) | non (seuls des préparatifs : `runs/pilote2-v5-2-1-preparatifs-v1/`) |
| Génération 0 du pôle | 26 oct. | 1 | sous-agents | synthèse `generation-0/synthese-generation-0-v1.md` citée par les faits servis ; **absente du dépôt** (recherche par nom : aucun fichier) | non |

Hors champ, dit pour ne pas les supposer : les trois courses réelles de l'organisme présentes sous `runs/` (bassins étroits, conception propre, « regard ou raisons », 13 et 14 novembre) ont **une seule génération** (`generation` = 1 dans chaque `manifeste-lanceur-fin.json`) ; le pilote sur la famille de calibration MR-2 aussi. Les « générations » des sorties de la conception (`docs/notes/organisme-multi-generations-v1/sorties-v1/` à `-v5/`, par exemple `generations-w12-g3-n400-v2.json`, `41616a47db42d62ee984803e43a609d5e5e3701f8ec22b49048f049aba9240a2`) sont des **simulations d'un modèle de proposeur**, pas des courses de l'organisme ; le mot « concluant » n'y figure pas (0 occurrence dans le fichier et sa sortie).

## 4. Comptes

Programme `programmes/compter_trois_regles_v1.py`, sortie `programmes/compter_trois_regles_v1.stdout`.

### 4.1 Essai à blanc de la boucle complète, code v64 (journaux bruts au dépôt)

**Règle 1 — fiches non concluantes : 0.**

| bras | génération | cartes des proposeurs | refusées au gardien | non promues par le juge (jamais testées) | promues puis testées | survit | éliminée | **non concluant** | retenues |
|---|---|---|---|---|---|---|---|---|---|
| réel | 1 | 12 | 0 | 0 | 12 | 12 | 0 | **0** | 12 |
| réel | 2 | 12 | 0 | 12 | 0 | — | — | — | 0 |
| aléatoire | 1 | 12 | 0 | 8 | 4 | 3 | 1 | **0** | 3 |
| aléatoire | 2 | 12 | 0 | 12 | 0 | — | — | — | 0 |
| recopie-mélange | 2 | 12 | 0 | 12 | 0 | — | — | — | 0 |

Témoins plantés (sept par bras et par génération jouée, 35 en tout) : 11 promus et testés, 5 « survit », 6 « éliminée », 0 « non concluant » ; 5 refusés au gardien ; 19 non promus. Sur disque : 27 fichiers `verdict-noyau-v5.json` (16 cartes et 11 témoins), dont 20 « survit » et 7 « éliminée » ; les sept événements d'étage du journal portent `"non concluant": 0`.

Devenir à la génération suivante des cartes de proposeur non retenues (le seul bras où il y en a et où une génération suivante est jouée est le bras aléatoire) : 8 non promues et 1 éliminée en génération 1 ; **toutes absentes de l'archive servie en génération 2, aucune loi reproposée en génération 2** (comparaison des lois en JSON canonique). Les fichiers de sélection listent 7 exclues en tout (une carte et six témoins) et portent tous la même règle écrite : « seules les fiches testées dont le verdict calculé par le noyau est « survit » sont retenues […] ; « éliminée », « non concluant » et les fiches non testées sortent (ordre : non concluant < éliminée < survit) ».

**Règle 2 — note ou rang du juge dans le texte servi aux proposeurs : aucun.** Quatre textes servis (deux proposeurs, deux générations, bras réel ; les bras aléatoire et recopie-mélange n'appellent pas de proposeur) :

| génération | caractères | clés du contexte | lois retenues servies | clés de chaque loi retenue | clés du juge trouvées, à toute profondeur | ordre des lois retenues | chiffres du juge de la génération 1 retrouvés |
|---|---|---|---|---|---|---|---|
| 1 | 13 552 | `monde`, `gabarit`, `lois_retenues`, `episodes_developpement` | 0 | — | aucune | — | — |
| 2 | 15 730 | les mêmes | 12 | `identifiant`, `loi` | **aucune** | **celui des identifiants** ; pas celui du log de la valeur e décroissant | **0 sur 134 écritures cherchées** (nombre entier à nombre entier) |

Les deux proposeurs reçoivent le même texte à chaque génération (empreintes `ffeb8a925e2190d86e75e3c96293abcc8586f4edc7af4843b9830fb2b97c5b9d` puis `3c911ee67c8edf7211bbbe8e0ca44a5ff48e564eeb211179338347a2a518cc1c`). La consigne (hors bloc de données) ne contient aucun des mots « verdict », « rang », « score », « note », « classement », « richesse », « promu ». Quatre écritures à trois décimales (`0.020`, `0.035`, `0.480`, `0.481`) n'apparaissent que comme début d'un nombre plus long (un poids ou un trait d'épisode) : coïncidences, comptées à part par le programme. **Ce qui passe quand même** : l'appartenance d'une loi à la liste retenue (un bit par loi : elle a été promue et a survécu), et la phrase « mieux que les lois déjà retenues ».

**Règle 3 — réemploi de fichiers d'une exécution à l'autre : rien à observer.**

| mesure | valeur |
|---|---|
| bac à sable | factice (les sept événements d'étage) |
| fiches testées | 27 |
| exécutions par fiche | **1 pour les 27** ; aucune fiche à plus d'une exécution |
| tours de l'expérimentateur par fiche | 2 pour les 27 (un script, puis fin) |
| dossiers de travail distincts (lus dans la commande de chaque exécution) | 27 ; aucun employé par deux exécutions |
| fichiers produits | 27, tous nommés `gains.csv` ; 26 empreintes distinctes |
| même empreinte dans deux exécutions d'une même fiche | aucune (impossible ici : une exécution par fiche) |
| même empreinte dans deux fiches | une : `5116799093c5623b05a51fa896f99983a99c6538d8b6477004b20414b9f4bcc7`, fiches `F-70a2cb367f9b` et `F-c71994685048` (bras réel, génération 1) |
| scripts distincts | 18 ; 3 partagés entre fiches |
| dates par exécution | aucun champ de date dans les résultats d'exécution ; les dates des fichiers au dépôt sont celles de l'extraction (18 novembre), sans valeur |
| tranche d'épisodes | cinq empreintes distinctes pour les cinq couples bras-génération (tâches fraîches, N-049) |

L'empreinte partagée entre deux fiches n'est pas un réemploi : les deux cartes portent **la même loi** (vérifié : `loi_predictive` égale, seul l'identifiant diffère), proposée par les deux doublures, calculée sur la même tranche, dans deux dossiers de travail distincts.

### 4.2 Essai à blanc du code v66 (relevés seuls)

Course complète (`releve-course.json`) : générations jouées [1, 2] ; génération 1 : 12 cartes, 12 promues, 12 « survit », 12 retenues ; 10 lois plantées, 3 promues, 2 « survit », 1 « éliminée », 1 refusée au gardien ; génération 2 : 12 cartes et 8 lois plantées, aucune promue, aucun test ; **0 non concluant** aux deux journaux d'étage. Identifiants servis aux proposeurs : 1 en génération 1 (la loi de départ K1), 13 en génération 2 (K1 et les 12 retenues), égaux aux attendus, **dans l'ordre des identifiants**, rien hors de l'archive ; texte reçu = texte écrit pour chaque proposeur. **Le texte servi lui-même n'est pas au dépôt** (son empreinte seule), ni l'arbre des exécutions : la règle 3 ne peut pas y être comptée. Bac factice. Les deux autres relevés sont des arrêts provoqués (essais de garde).

### 4.3 Course réelle, code v67 — d'après le verdict scellé, non recompté par moi

Ce qui suit est **rapporté** par le juge de la règle R13 (`verdict-course-v67-v1.md`, sections 3, 4.2 à 4.5 et réserve R-5), qui dit l'avoir vérifié sur le relevé brut de la branche ; je n'ai pas lu cette branche.

- Génération 1 : 11 cartes réelles (Kimi a rendu 5 lois et non 6), toutes promues, toutes survivantes, 11 retenues. Génération 2 : 12 cartes, aucune promue, **aucun test de mort**, sélection finale vide.
- 14 tests de mort en tout (deux vraies plantées, la plantée à éliminer et les 11 cartes) : « une seule exécution » par test, « 14 tests × 2 tours : un script, puis « fin » » ; verdicts : 13 « survit » et 1 « éliminée » ; aucun incident. Je n'y lis **aucun « non concluant »**.
- Vue servie en génération 2 = archive de jugement = la loi de départ et les 11 retenues ; « aucune loi plantée dans la vue ».
- Réserve du juge : les réponses brutes des proposeurs n'ont pas été gardées (dossier des sessions vide) ; aucun fichier témoin du bac par exécution ; machine détruite.

### 4.4 Total, sur ce qui a pu être compté ou qui est rapporté

| | fiches testées | non concluantes | fiches à plus d'une exécution | textes servis portant une note ou un rang |
|---|---|---|---|---|
| essai à blanc v64 (compté) | 27 | 0 | 0 | 0 sur 4 |
| essai à blanc v66, course complète (compté sur relevé) | 15 | 0 | non comptable | non comptable (identifiants seuls : conformes) |
| course réelle v67 (rapporté) | 14 | 0 | 0 | non comptable d'ici |

## 5. Ce que dit le code qui a tourné

Lien par empreinte : les six modules de la copie du dépôt (commit `94bfd92`) ont **les mêmes empreintes** que celles que consignent les manifestes de fin des deux courses réelles à une génération des 13 et 14 novembre (`runs/course-ideation-conception-propre-v1/…/copies/sortie--manifeste-fin.json`, `runs/course-ideation-regard-ou-raisons-v1/…`) : 12 comparaisons, 12 égales (sortie du programme, dernière section). Pour la course réelle v67 : les différentiels v66 et v67 n'ajoutent que des fichiers neufs (11 et 5 chemins, tous « nouveau fichier » à leur première apparition, compté par moi) ; la contre-lecture du code v65 dit « dix fichiers neufs » sur le parent `94bfd92`, mais **le différentiel du code v65 n'est pas au dépôt** : que la v65 n'ait modifié aucun de ces six modules est probable, non vérifié.

**Règle 1.** `tests_de_mort_v4.py`, l. 24-27 : « « non concluant » n'est jamais mieux traité qu'« éliminée ». Ordre total des verdicts : non concluant (0) < éliminée (1) < survit (2) […] ; la sélection (`selectionner`) ne retient que « survit » : « éliminée » et « non concluant » sortent ». Il n'existe ni file d'attente, ni second essai, ni état « différée » : une fiche non concluante sort comme une éliminée et n'est écrite qu'au relevé. Sortent « non concluant » : aucune exécution réussie, fichier attendu non produit, non copié ou altéré, cellule non numérique, statistique non finie (l. 28, 162), et tout incident de la fiche. Rien n'empêche qu'un proposeur repropose la même loi plus tard : `tour_ferme_v64.py` ne porte aucune mémoire des cartes sorties (aucune occurrence de « memoire », « redite », « doublon »).

**Règle 2.** `boucle_fermee_v59.py`, l. 18-20 : le proposeur suivant voit « les seules lois de l'archive (identifiant, loi), jamais un verdict, une richesse, une promotion, un motif ou un compte » ; la garde `exiger_vue_sans_verdict` (l. 198-211) refuse toute vue portant l'une de 19 clés interdites ; `vue_pour_proposeur` (l. 214-218) range les lois par identifiant. **Avant la version 59, c'était l'inverse** : « l'héritage servi reste le classement des juges, écrit avant l'étage » (l. 4-6), et « la génération g+1 n'hérite plus du classement des juges » est écrit comme un changement (l. 24-26). Les faits servis au collisionneur le 1er novembre décrivaient encore l'ancien régime : « fiches scellées anonymes de g servies à g + 1 avec verdict, classement et étiquette d'héritage » (sél/`faits.md` l. 52), et les verdicts des tests de mort « servis en matériau à la génération suivante », en comptes et étiquettes (bac/`faits.md` l. 56).

**Règle 3.** `tests_de_mort.py`, l. 29-30 et 1467 : dossier de travail « neuf à chaque exécution : rien ne subsiste d'une exécution à l'autre » (phrase servie à l'expérimentateur) ; l. 1916-1921 : un dossier neuf est créé pour chaque exécution, hors de la sortie, et retiré après l'inventaire ; le manifeste porte `"neuf_par_execution": True` (l. 945). Ce changement date de la version 49 (correction dite CL13-02 : un lien posé par un script). **La version 48, servie aux espèces, avait « un seul dossier inscriptible (le dossier de travail de la fiche) »** (bac/`faits.md` l. 52), trois exécutions par fiche (l. 53). Ce qui reste, écrit dans le code : la sortie de chaque exécution revient à l'expérimentateur au tour suivant (bac/`faits.md` l. 51) ; le noyau lit « la dernière exécution réussie » et « l'expérimentateur choisit, dans son quota d'exécutions, laquelle est la dernière réussie » (`tests_de_mort_v4.py`, l. 43-44, 57) ; quota par défaut de 3 exécutions par fiche (`tests_de_mort.py` l. 107) et 12 tours au plus (`tour_ferme_v64.py` l. 51, 146 ; `tests_de_mort_v5.py` l. 132).

**Ce que le préenregistrement de la course en préparation reprend** (brouillon 6, non scellé) : le test coupé par sa borne de 1,50 USD ou dont le témoin d'isolement est en défaut est « non concluant », « n'est pas « survit » et est compté à part » (l. 552-553) ; le groupe dont le représentant meurt ou est non concluant « est éliminé de la génération », ses sœurs étant rejugées « après la course, hors ligne, sans agent, sans effet sur la sélection ni sur l'héritage » (l. 447-449) ; « vue servie = cette archive (garde 23) ; les autres membres des groupes sont écrits au relevé, jamais servis » (l. 450-451) ; « vue servie sans verdict » (l. 195). Les mots « oublier » et « héritage réduit » (bras demandé par Lazar, R-2528) n'y figurent pas. Le libellé « survit » y est encore employé (l. 552) ; R-3209, point 3, demande de le remplacer.

**Ce que disent les décisions.** N-053, point 5 : « aucun score de moniteur (sonde, juge) n'entre dans un signal d'entraînement ou de sélection de l'agent, hors bras d'attaque déclaré ; il vaut aussi pour la piste « organisme » (N-045) ». N-058, points 1 et 2 : le choix de la composition des proposeurs se juge sur l'oracle du monde planté et le coût ; « classer les proposeurs par les fiches que le juge promeut, c'est sélectionner un agent sur le verdict du juge », ce que l'invariant interdit. **Aucun des deux textes ne parle de ce qu'on écrit dans la consigne d'un proposeur** : ils visent l'entraînement et la sélection d'un agent. La note du 2 novembre et sa contre-lecture divergent sur la portée (« touche l'invariant » ramené à « remarque du lecteur ») ; l'espèce A lit le pare-feu comme protégeant « l'affinage intra-génération, pas la sélection inter-générations » (sél/conception A l. 16). N-049 : tâches fraîches à chaque génération (tenu dans les essais : cinq tranches distinctes). N-045 version 2, point 5 : l'héritage sur au moins trois générations est récompensé. N-044 et N-050 : rien sur ces trois règles.

## 6. Les dix critiques croisées, espèce par espèce

Tour deux du collisionneur : chaque espèce critique la conception des quatre autres. Aucune ne pose les trois règles sous leur nom ; je relève ce qui s'y rattache, avec le fichier et la ligne. « sél/X » = critique croisée de l'espèce X sur la sélection ; « bac/X » = sur le bac à sable. Tous les chiffres des espèces sont dits illustratifs par elles-mêmes.

### A — Fable 5.1

- **Règle 1.** Une fiche vraie sans épreuve disponible « doit sortir « différée », pas « éliminée » ; sans ce témoin, la conjonction compte l'absence de banque comme une mort » (sél/A l. 31). Un bras où la couche sans épreuve est comptée « différée » manque à la conception de C, sinon « le résultat est une tautologie » (l. 60 ; l. 42 : le duel « compare deux conventions administratives, pas deux hypothèses sur le monde »). « « différée hors population reproductrice » est raisonnable, mais produit une dérive de lignée vers la testabilité » que D ne mesure pas (l. 76) ; mesure proposée : corrélation entre le code de sortie du pont à la génération g et la survie de la lignée à g + 2 (l. 107). Sans contrôle positif de puissance, « « indécis » devient une sortie éternelle » (l. 121) ; aucun texte sauf E ne nomme la zone « indécis » (l. 5). Côté bac : une troisième issue « non tranché » contredit l'inférence forte ; remède : fixer l'effectif avant (bac/A l. 99).
- **Règle 2.** Rien sur un rang ou une note servis. Voisin : l'effet d'une archive servie se confond avec la longueur de la consigne (sél/A l. 44, 62) ; la réutilisation d'une épreuve dépend de ce que le dispositif fait du bit de survie (l. 43 : passage proche d'une famille exclue, non résumé). Côté bac : l'apprentissage du verdict demande un producteur non adaptatif, sans retour, comme base (bac/A l. 105, 113).
- **Règle 3.** Rien sur le dossier partagé dans sa critique (elle le porte dans sa propre conception, bac/conception A l. 64, 98, et y revient au troisième tour, bac/réponse A l. 30, 85). Voisin : voir la sortie de ses tours précédents, jusqu'à douze, « c'est précisément une recherche à 12 essais avec retour ; la loi du nombre d'essais nécessaires pour atteindre le seuil n'est pas examinée » (bac/A l. 46) ; un bras « script fixé, sans modèle » sur les mêmes fiches nulles pour mesurer le taux d'erreur avant d'imputer quoi que ce soit (l. 30).

### B — Opus 4.6

- **Règle 1.** Une fiche « en attente » qui revient avec un engagement neuf « n'est pas la même fiche » : elle prend une place dans le nombre de lois de la procédure de Benjamini et Hochberg ; « si beaucoup de fiches reviennent, m croît sans que la puissance augmente, et la boucle s'éteint par inflation de la correction de multiplicité » ; « confondant potentiel entre recyclage et création » (sél/B l. 114). Il manque un critère de sortie gelé pour une option « provisoire » (l. 116). Distinguer deux causes de non-testabilité : le pont ne traduit pas, ou l'épreuve manque (l. 75). Témoin proposé : ensemencer la génération 2 avec les éliminées (« pôle inversé », l. 34). Côté bac : « différer les tests de mort » revient à renoncer à toute vérification empirique (bac/B l. 79).
- **Règle 2.** Rien sur un rang ou une note. Voisin : la mémoire servie (« leçons ») est un canal de fuite partagé par tous les bras, à manipuler à part de l'épreuve (sél/B l. 11, 98, 132) ; avantage circulaire d'un juge qui promeut les filles ressemblant aux parents qu'il a promus (l. 15). Côté bac : le matériau servi à la génération suivante ne contient que « comptes et étiquettes » (≈ 8 bits par génération selon A) ; témoin proposé : le remplacer par du bruit de même format (bac/B l. 11, 23, 31) ; « le contenu des champs autorisés (verdict, comptes) est un signal que le producteur peut exploiter » : mesurer la conformité du format ne mesure pas l'exploitation (l. 75) ; aucune expérience ne mesure l'exploitation du verdict à travers les générations (l. 95).
- **Règle 3.** **Le relevé le plus direct des dix** : « Canal intra-fiche nommé mais non testé. A relève correctement que les trois exécutions par fiche partagent un dossier inscriptible […]. Il faudrait un artefact explicite : un script qui écrit dans le dossier de travail un fichier lu par le script suivant, et vérifier que la garde le détecte ou que la remise à zéro le bloque » (bac/B l. 17). L'expérimentateur peut « ajuster son script suivant en fonction de la sortie précédente pour converger vers un `RESULTAT:` favorable » ; la séparation physique ne rompt pas cette boucle (l. 41). Témoin proposé : taux de survie avec 1 exécution contre 3, sur les mêmes fiches (l. 65). Réserve : sans retour, l'expérimentateur ne peut plus corriger ses erreurs de syntaxe ; mesurer le taux de scripts fonctionnels dans les deux conditions (l. 105, 123).

### C — Argon

- **Règle 1.** La zone « indécis » d'E est « une échappatoire à la falsification » qui « absorbe la quasi-totalité de la masse de probabilité » aux effectifs prévus (sél/C l. 86, 93-95). Tout filtre (forme, traduisibilité, test de mort) doit être appliqué **avant** le calcul du nombre de lois de la procédure, jamais après (l. 99-101). Voisin : le test de mort a une variance d'exécution (« 3 essais de 120 s ») ; un échec accidentel d'exécution suffit à changer une issue « par pur bruit technique » (l. 36). Côté bac : la règle d'intervalle rend le duel « non tranché » sur presque tout le domaine (bac/C l. 76).
- **Règle 2.** Rien sur un rang ou une note dans ses critiques (sa propre conception sert le gain de richesse aux proposeurs, d'après la note du 2 novembre). Voisin : témoin de motifs d'élimination factices ou permutés, de même longueur, pour séparer l'information de l'amorçage lexical (sél/C l. 77, 106) ; une archive hors sujet n'est pas un témoin neutre (l. 88). Côté bac : contrôle « à quota de requêtes égal mais retours aléatoires », pour séparer l'apprentissage du signal de la simple exploration à plusieurs essais (bac/C l. 83).
- **Règle 3.** Manque, selon lui, à la conception de A : « un contrôle d'état inter-exécutions où l'exécution 1 n'écrit aucun fichier mais modifie une ressource mesurable, ou où un script honnête réutilise légitimement un cache dans le dossier de travail si le contrat de la v48 ne l'interdit pas explicitement » (bac/C l. 22). Trois exécutions par fiche « gonfle[nt] encore ce taux par sélection multiple honnête » : de 0,05 à ≈ 0,14 par fiche sous un test au niveau 0,05 (l. 29, 35).

### D — Kimi

- **Règle 1.** Les bras de C « ne comptent pas le même objet scientifique — promotion effective contre gel en attente » (sél/D l. 63) ; quand une couche n'a aucune épreuve, sa probabilité de promotion est nulle et le rappel « mélange deux paramètres : la puissance du juge et la disponibilité instrumentale » (l. 72). Côté bac : « un intervalle d'incertitude qui traverse le seuil gelé rend la décision « non tranchée », pas favorable à une hypothèse » (bac/D l. 1).
- **Règle 2.** « Les filles d'éliminées ne sont pas un contrôle non exposé. Leurs parents ont reçu un verdict […], et l'élimination est elle-même une information susceptible de guider la descendance ou la mémoire » (sél/D l. 9). « Si les proposeurs ne dépendent pas effectivement du retour, ou s'il n'existe aucune variation héritable, G = 0 même avec réutilisation : l'essai ne distingue alors absence de fuite et absence d'adaptation » (l. 98) ; témoin : « retours permutés entre lignées » (l. 106). Un rendement en excès de richesse par dollar « favorise le bras » du pôle : c'est « la quantité que le pôle maximise » (l. 67). Côté bac : « canal placebo de même débit et même calendrier, mais sans information de verdict » (bac/D l. 24, 99) ; le duel d'apprentissage « confond information retournée et occasions supplémentaires » (l. 83, 91).
- **Règle 3.** Témoin proposé : « un appariement dossier vierge / dossier prérempli » (bac/D l. 26). « La sélection de la dernière exécution réussie modifie la loi conditionnelle estimée » (l. 14) ; « les exécutions répétées d'un même script ne fournissent pas des unités indépendantes » (l. 18) ; « après k choix adaptatifs, la probabilité de rejet dépend de la loi jointe des k analyses » (l. 39).

### E — Astra

- **Règle 1.** Compter les fiches « gelées en attente » comme des découvertes dans un bras et exiger une promotion dans l'autre « compare deux événements différents » (sél/E l. 89) ; le rendement confirmé est le produit de la part retenue et de la part confirmée parmi les retenues : la première seule ne dit rien (l. 105) ; témoins demandés : « témoins en attente sans effet réel », « variation séparée […] du statut administratif » (l. 114), « classes rares de différées injectées indépendamment » (l. 149, 139). Sous nul global, réserver la reproduction aux survivantes produit une extinction qui empêche l'adaptation qu'on veut étudier ; compter les lignées éteintes (l. 92, 106, 115). « Absence de significativité et équivalence ne sont pas interchangeables » (l. 7). Côté bac : une estimation imprécise « reste non jugeable : elle ne peut être forcée dans l'une des deux issues » (bac/E l. 304).
- **Règle 2.** Le bras qui redemande après un refus reçoit « un retour informatif supplémentaire » (sél/E l. 93) ; une épreuve fraîche « n'empêche pas la sélection d'hypothèses particulièrement compatibles avec le juge choisi comme mesure finale » (l. 20). Côté bac : retirer le matériau « change aussi l'information scientifique disponible » ; témoin : « matériau placebo de même forme et volume, indépendant de la fiche ; randomisation par lignées » (bac/E l. 17, 86) ; « le nombre d'étiquettes ne borne pas toute la transcription visible » (l. 23).
- **Règle 3.** Une seule mention : l'essai de A « laisse hors duel des anomalies de traces étrangères au dossier partagé » (bac/E l. 15) ; une variation bénigne de trace sans changement de calcul doit servir de témoin (l. 89).

## 7. Tableau par règle

Les positions du premier et du troisième tour, et celles d'Argon seul et de Kimi seul, sont reprises de la note du 2 novembre, version 2 (questions 1 et 3 de la sélection, question 2 du bac, section 4), dont j'ai vérifié les quatorze lignes citées en section 2. Réserves de cette note, qui valent ici : l'espèce B a servi Opus 4.6 ; C et Argon seul sont le même modèle, D et Kimi seul aussi ; les accords du troisième tour sont nés de la lecture mutuelle ; le lecteur est de la famille de A.

### Règle 1 — sort de la fiche non concluante

| | |
|---|---|
| **Faits de nos courses** | 0 fiche non concluante sur 27 (essai à blanc v64, compté), 15 (essai à blanc v66, compté sur relevé) et 14 (course réelle v67, rapporté) tests de mort. Le code retire : « non concluant » est rangé sous « éliminée », seule « survit » est retenue ; ni second essai, ni file d'attente, ni état « différée ». Dans le seul cas observable (bras aléatoire de l'essai v64), les 9 cartes sorties ne sont ni servies ni reproposées à la génération suivante. Le brouillon 6 du préenregistrement garde ce sens (groupe éliminé, compté à part). Deux textes servis au collisionneur se contredisent : « une idée non concluante ne passe pas » (sél/`question.md` l. 3) et « indécise → un test plus puissant, ou retirée après deux essais » (sél/`faits.md` l. 202-203). Les faits servis rapportent « 3 indécises » sur 18 à la génération 0 du pôle (sél/`faits.md` l. 143) ; leur devenir n'est pas au dépôt. |
| **Avis des espèces** | *Retirée* : C (« ne passe pas à g + 1 », sél/conception C l. 36). *Différée, réadmise avec des données ou un test neufs* : D, E. *Dormante, réinjectée plus tard* : Argon seul. *Plus de deux états* : A, C, D, E, Kimi seul. A relève la contradiction des deux textes (sél/conception A l. 14). Critiques croisées : différée et non éliminée quand l'épreuve manque (A, sél/A l. 31) ; la réadmission gonfle le nombre de lois et éteint la boucle (B, sél/B l. 114) ; l'état différé fait dériver les lignées vers ce qui est facile à tester (A, sél/A l. 76, 107) ; une zone indécise sans effectif fixé absorbe presque toutes les issues (C, sél/C l. 86 ; A, bac/A l. 99) ; tout filtre avant le calcul du nombre de lois (C, sél/C l. 99-101) ; ne pas compter « en attente » comme une découverte (D, sél/D l. 63 ; E, sél/E l. 89). |
| **Ce qui manque** | Une seule fiche non concluante observée, dans n'importe quelle course. Le taux réel de tests coupés par leur borne ou en défaut d'isolement avec un expérimentateur réel (les 14 tests de la v67 ont tous abouti en une exécution). La cause de chaque non-concluant (borne de dépense, panne, fichier absent, incident d'isolement) : le code n'en fait qu'un mot. Le devenir des 3 indécises de la génération 0. Toute mesure comparant retirée, différée et dormante : aucune n'a été jouée, ni en simulation ni en course. |

### Règle 2 — note ou rang du juge montré aux proposeurs

| | |
|---|---|
| **Faits de nos courses** | Depuis la version 59 du code, le proposeur suivant reçoit les seules lois retenues (identifiant et loi), rangées par identifiant, et une garde refuse toute clé du juge. Compté sur l'essai à blanc v64 : 0 clé du juge, 0 chiffre du juge sur 134 cherchés, ordre des identifiants et non du score, dans les textes de génération 2 ; essai v66 : identifiants servis conformes, texte absent ; course v67 : vue = archive (rapporté). **Avant la version 59**, l'héritage servi était le classement des juges, et la conception du 1er novembre servait « verdict, classement et étiquette d'héritage » : aucune course jouée sous ce régime n'a ses journaux au dépôt. Ce qui passe toujours : un bit par loi (retenue ou non). Le brouillon 6 garde « vue servie sans verdict ». N-053 (point 5) et N-058 interdisent qu'un score de juge entre dans l'entraînement ou la sélection d'un agent ; ils ne disent rien du contenu d'une consigne. |
| **Avis des espèces** | *Servir un score* : C (le gain de richesse des survivantes, sél/conception C, d'après la note du 2 novembre). *Ne pas servir de rang* : D (« sans transmettre le rang dans un premier temps », sél/conception D l. 64 ; « le rang peut devenir une sélection par jugement détournée », l. 15), E (« ne pas transmettre de rang global par défaut », sél/conception E l. 57), Kimi seul (rang = métadonnée d'audit). *Deux variantes sans choix* : Argon seul. Critiques croisées, aucune sur le rang lui-même : l'élimination est déjà une information qui guide la descendance (D, sél/D l. 9) ; sans dépendance au retour, un essai de fuite rend zéro sans rien prouver (D, sél/D l. 98) ; témoins proposés : matériau remplacé par du bruit de même format (B, bac/B l. 31), canal placebo de même débit sans verdict (D, bac/D l. 24, 99), retours permutés entre lignées (D, sél/D l. 106), retours aléatoires à quota égal (C, bac/C l. 83), matériau placebo de même forme, randomisation par lignées (E, bac/E l. 86) ; apparier longueurs et nombres d'appels (A, sél/A l. 44 ; C, sél/C l. 77). |
| **Ce qui manque** | Une course, réelle ou à blanc, où une note ou un rang est servi : il n'y en a aucune au dépôt, donc aucun effet mesuré dans un sens ou dans l'autre. Les textes servis de la course réelle v67 et ses réponses brutes de proposeurs (ces dernières n'ont pas été gardées). Les journaux des courses d'avant la version 59 (classement servi), sur des branches non lues. Une décision sur la portée de N-053 pour le contenu d'une consigne. Le bras « héritage réduit au meilleur » (R-2528), absent du brouillon 6. |

### Règle 3 — cache entre exécutions d'une même fiche

| | |
|---|---|
| **Faits de nos courses** | Depuis la version 49 du code, le dossier de travail est neuf à chaque exécution, hors de la sortie, retiré après l'inventaire, et la consigne de l'expérimentateur le dit. Compté sur l'essai à blanc v64 : 27 fiches, **une exécution chacune**, 27 dossiers distincts, aucun fichier réemployé ; une seule empreinte de produit commune à deux fiches, due à deux cartes de même loi. Course v67 (rapporté) : 14 tests, une exécution chacun. Donc aucune fiche à deux exécutions n'a jamais été observée, et le bac des deux essais est factice. La version 48, servie aux espèces, avait un dossier inscriptible partagé par les trois exécutions. Restent, par le code : la sortie de l'exécution précédente revient à l'expérimentateur ; le noyau lit la dernière exécution réussie, que l'expérimentateur choisit ; quota de 3 exécutions et 12 tours. |
| **Avis des espèces** | A pose la question de contrat : interdire (remise à zéro) ou déclarer (le préenregistrement nomme les fichiers gardés) (bac/réponse A l. 85 ; conception l. 64, 98). B demande un artefact explicite, un script qui écrit un fichier lu par le suivant (bac/B l. 17), et un essai 1 exécution contre 3 (l. 65). C veut un contrôle d'état entre exécutions, cache légitime compris (bac/C l. 22), chiffre l'inflation par trois essais (≈ 0,14 par fiche, illustratif, l. 35), et propose l'arrêt au premier succès (bac/réponse C l. 19). D demande un appariement dossier vierge contre dossier prérempli (bac/D l. 26) et relève que lire la dernière exécution réussie change la loi estimée (l. 14). E ne se prononce pas sur le dossier (bac/E l. 15). Kimi seul nommait l'« état partagé » sans le rattacher au dossier. |
| **Ce qui manque** | Une exécution réelle du vrai bac avec deux exécutions d'une même fiche : jamais observée. L'essai de régression qui prouve que rien ne subsiste (cas sain et artefact, R5) sur le vrai bac : je ne l'ai pas cherché dans les essais du code, et la copie du dépôt n'a pas le dossier des essais. Le nombre réel d'exécutions et de tours par fiche avec un expérimentateur réel hors de la v67. Une mesure de l'effet du retour entre exécutions (1 contre 3, placebo) : aucune jouée. Le code v68 à v74 de la course en préparation : pas de copie au dépôt, donc pas de preuve que le dossier neuf y est tenu. |

## 8. Ce qui manque — liste

1. **Journaux bruts de la course réelle v67** : branche `donnees/course-organisme-v67-poste-local-v1`, non lue. C'est la seule course réelle à deux générations ; ses comptes sont ici rapportés d'après le verdict, non recomptés.
2. **Arbre des exécutions et textes servis de l'essai à blanc v66** : jamais versés (bloc-notes d'un conteneur).
3. **Journaux des courses d'avant la version 59**, où le classement était servi à la génération suivante : pôle du 27 octobre, course 1, mini-course, dix courses des mentors — branches non lues ; leur nombre de générations n'est pas établi ici.
4. **Pilotes de l'organisme précurseur** (branches `pilotes/*`, `canal/gemini-organisme-*`) : non lus ; parts `test_final` du pilote 4 fermées (N-050).
5. **Synthèse de la génération 0 du pôle** (3 indécises sur 18) : absente du dépôt.
6. **Différentiel du code v65** et **code v68 à v74** : absents du dépôt ; la continuité des six modules de la v64 à la course en préparation est établie pour v66 et v67, supposée pour v65, inconnue au-delà.
7. **Réponses brutes des proposeurs de la v67** : non gardées par la course (réserve du verdict).
8. **Conceptions et réponses du collisionneur** : non relues par moi au-delà de quatorze lignes ; lectures vérifiées d'Argon seul et de Kimi seul non relues.
9. **Toute mesure** : aucune des trois règles n'a été comparée à son alternative, ni en simulation ni en course ; les seuils et effectifs des espèces sont illustratifs ; aucune de leurs références n'est vérifiée sur PDF.
10. **Conception v4 et brouillon 3** (pièces de R-3051) : lues par recherche de mots seulement ; les clauses citées sont celles du brouillon 6, plus récent, non scellé et non contre-lu en entier d'après son en-tête.

## 9. Limites

- Les deux essais à blanc ne disent rien d'un expérimentateur réel : les doublures écrivent un script juste du premier coup ; zéro non-concluant et une exécution par fiche y sont attendus par construction. Zéro observé sur 27 et 15 tests ne borne aucun taux réel.
- Le compte de la règle 2 cherche des clés et des chiffres ; il ne détecte pas une information du juge qui serait écrite en mots. La consigne a été cherchée sur sept mots seulement.
- Les lignes citées des critiques croisées sont celles que j'ai rattachées aux trois règles ; le rattachement est le mien. Aucune espèce n'a été interrogée sur ces trois règles telles que Lazar les pose aujourd'hui.
- Le lien « ce code a tourné » repose sur des empreintes consignées par les courses à une génération et sur des différentiels ; je n'ai exécuté aucun code de l'organisme.
- Je suis de la famille de l'espèce A : biais de lecture possible sur A et B.
- Aucune instruction adressée au lecteur n'a été rencontrée dans les pièces lues.

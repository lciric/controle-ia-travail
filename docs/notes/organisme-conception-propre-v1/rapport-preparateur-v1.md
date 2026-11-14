# Rapport du préparateur — course de l'atelier d'idées sur la conception de l'organisme lui-même — v1

Préparateur neuf (modèle A), sous-agent de la session mère, 13 novembre 2026, de 22:51 à 23:37 UTC (heures relevées
par `date -u`). Demande : R-2593, R-2609 ; modèle suivi : la préparation « bassins étroits » et la vérification courte du
lanceur v3 (`verification-courte-lanceur-v3-v2.md`, `9c1caa7e…`). **Aucune course, aucun appel de modèle, aucune instance,
aucune dépense ; aucune clé lue ; aucune opération git en écriture ; rien commité ni poussé ; `.claude/` lu, non modifié ;
le clone public lu sans être modifié** (vérifié propre, fichiers ignorés compris, après chaque passage). Aucun refus de
permission, de classifieur ou de crochet rencontré.

## Verdict

**Préparation rendue, course non autorisable en l'état** : la question, la conception avec la règle de sélection écrite
avant, les témoins, le catalogue, la consigne du lecteur, le devis (**pire cas 21 USD, attendu ≈ 6,5 USD**, borne 25) et le
lanceur neuf (essais : **131 passés** ; banc : **25 mutants tués sur 25**) sont prêts et scellés. Manquent, avant le lancement : la contre-lecture
du lanceur par un autre modèle, la ligne de GO, l'épingle du crochet et une session où il est chargé, `socat` ; et, avant la
lecture des fiches, l'outil du lecteur et le programme de classement (conception, § 8), non écrits.

## 1. Pièces (scellées ; empreintes SHA-256)

| Pièce | Empreinte |
|---|---|
| `question-organisme-conception-propre-v1.md` (servie aux proposeurs ; épinglée dans le lanceur) | `77c524f3c591e43ec1b14e261bd4667cf0e085b6c94afe7e7b37f72816c6feb4` |
| `conception-course-v1.md` (règle de sélection, § 4 à 7) | `be3ba97ee418de50fa356b0e39fcfa62c16d06f5767560265fcc7ee9f191a95e` |
| `temoins-plantes-v1.md` | `9b0faed52fbe8ebe5a05e20cb5f9ada06e5f9ce1319bdf0883ec461063e8a424` |
| `temoins-organisme-conception-propre-v1.json` (juge de l'organisme ; épinglé) | `ec3ae933d37162ea478a5041ee6ed9f3b8eabbece2078d0f754f35491e30fd50` |
| `temoins-lecteur-v1.json` (valeurs attendues) | `d11efe787cd27d2acb4b912487565896e43fc7cefbc7f51aa18080f3cdf8a77e` |
| `temoins-hasard-v1.json` (8 idées tirées au hasard) | `b5e38724cf74b61e1db47f6dbc0e8f6955a0e4419723dc0ecd627854206c539d` |
| `catalogue-conceptions-publiees-v1.md` (12 entrées, pages vérifiées) | `ddfb2522be0fe5095926405b8761d0e4be0065a29679585051a287349114fe9d` |
| `consigne-lecteur-v1.md` | `95efebaae5e97764c50b334daa1d3d4f28e5d4517396513afd1f3640ac06da8d` |
| `devis-v1.md` | `ce679a533a90a2a7b2feea1f0269429161ecc3467fd06f32ba83e611ed90bf2b` |
| `outils/tirer_fiches_hasard_v1.py` | `d0881ae3dcc2dbfd782d0c9a008dcc7b44f1c83332a6f97d11673d5985784a88` |
| `outils/valider_temoins_v1.py` ; résultat `outils/resultat-valider-temoins-v1.txt` | `4e212afd…` ; `78b7d35a…` |
| `outils/mutations_lanceur_conception_propre_v1.py` | `cbb574d12d01285813cc0f599a59d6ed8b0e2e99c9e7f34afa25570837f81817` |
| `scripts/lancer_course_ideation_conception_propre_v1.py` (compagnon écrit) | `709cf1c7b25b9bfd7b8dd8deeb0782dbabb2d90153a407a5df1b389f2cd15ec2` |
| `tests/test_lancer_course_ideation_conception_propre_v1.py` | `772f882e5822f4e5388976a0ceacea401adec9b7247ef48b6771ca780d8da2b8` |

## 2. Le lanceur : ce que la vérification du v3 a trouvé, et ce qu'il en est ici

| Constat (v3) | Ici |
|---|---|
| **B1** (dépense illisible après remplacement du conteneur) | Sans objet pour une dépense antérieure (course neuve, aucune). Mais la cause est fermée : à la clôture, **relevé de dépense scellé et copies scellées octet pour octet** (code du superviseur, PID, tentatives de contrôle, trois listes de fiches, manifeste de fin, lecture de la course, notes du juge, témoins servis) dans `runs/course-ideation-conception-propre-v1/<id>/` ; ensuite cumul et relance ne lisent que le dépôt ; le relevé est lié au manifeste de fin par son empreinte. Essais : dossier hors dépôt supprimé après clôture → même dépense, même décision ; relevé altéré, absent ou rescellé → plafond compté, relance refusée. |
| **M1** (le lanceur ne se garde pas) | Le lanceur exige, **avant le verrou et avant toute écriture** : `sys.flags` isolé et sans octets, `sys.orig_argv` **égal** à `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_conception_propre_v1.py 1`, dossier courant = racine du dépôt, fichier non lien, à sa place, d'empreinte égale à son compagnon ; argument unique `1`. Essais : sept formes de commande fausses, cinq artefacts du fichier, et le **vrai fichier** lancé en processus à part sans `-I`, ou avec l'argument `2` : refus, rien créé. |
| **M2** (git et calculs après le détachement) | Tout ce qui peut échouer est fait avant ; **aucune commande git après le détachement** (essai : git qui lève s'il est appelé après ; essai de source) ; manifeste de **pré-départ** scellé avant ; après, une seule écriture courte ; si elle échoue : PID et commande d'arrêt imprimés (code 5) ; le superviseur scelle son propre PID d'abord, et l'invocation suivante retrouve la course (en marche, puis clôture). Exception au détachement après l'ouverture des journaux du superviseur : **aucun manifeste de refus** (il dirait « rien parti ») ; l'invocation suivante refuse (« sans PID scellé »), plafond compté : nœud humain, sens fermé. |
| m1 (perte partielle) | Fermé par le relevé et les copies (essai : sortie supprimée seule après clôture → sans effet). |
| m2 (orphelin avant `pid-orchestrateur.json`) | **Non corrigé**, fenêtre de quelques instructions dans le superviseur ; l'argent reste gardé (plafond compté). |
| m3 (une relance par génération) | Une génération, **une seule relance au total** (comme R-2558) ; deux courses au plus. |
| m4 (essais dépendants de la machine) | Les deux essais contre l'orchestrateur réel sont **sautés** si le clone manque et **échouent** s'il n'est pas à l'arbre épinglé : choix voulu, c'est un signal d'état pour la session qui lancera. |
| m5 (195 noms d'environnement au manifeste) | Les noms exclus ne sont plus écrits : leur nombre et l'empreinte de leur liste seulement. |
| m6 (l'épreuve d'authentification ne prouve pas la suite) | Inchangé : environnement par liste de noms permis (cause du 401 de R-2549) ; la preuve réelle reste le premier contrôle. |
| m7, m9 | Sans objet (aucun lanceur antérieur sur cette ligne). |
| m8 (`LANG` absent) | À savoir : ici aussi le lanceur ne transmet que les noms permis présents. |

Autres choix : **aucun bras** (le juge différé `argon-juge`, exigé par le code, n'est jamais joué ; `--bras-rapporte-differe`
est un drapeau interdit) ; orchestrateur épinglé par **l'arbre git du dossier `orchestrator/`** (`ee84d6ec…`, identique aux
commits `be6b5af9…` et `1168b02…` — ce dernier local, non poussé, R-2594) en plus des neuf empreintes ; **ligne de GO trouvée
par son contenu** (périmètre contenant « organisme d'idéation » et « propre conception », type calcul, Lazar, période,
non révoquée, plafond ≥ 21 USD ; une seule) ; garde de cumul : dépense relevée + 14,9 + réserve du lecteur 4,0 ≤ min(25,
plafond de la ligne) ; noms de clé exclus de l'environnement, `KIMI_API_KEY` compris.

## 3. Essais et banc de mutations

- **Essais** : `tests/test_lancer_course_ideation_conception_propre_v1.py` ; deux premiers passages (23:23, 23:24 UTC) avec un
  essai en échec chacun, corrigés (attente bornée du PID scellé par le superviseur ; paramètres de l'essai de cumul) ; puis
  23:27 et 23:35 UTC : **131 passés** (journal `outils/resultat-essais-lanceur-conception-propre-v1.txt`, `198fd9f2009064ae6361fb4d79d5a72c586a1fad96b137c79285df2f9a7f1cbb`), dont deux sans appel contre l'orchestrateur réel (liste blanche et mesure sur les vraies pièces ; analyseur
  d'arguments : aucun argument inconnu, moteur réel, aucun bras, graine 2026111401) ; clone resté propre ; aucun dossier de
  production créé hors du dépôt. Suite complète du dépôt non jouée (hors mandat ; l'essai neuf seul).
- **Banc** : `outils/mutations_lanceur_conception_propre_v1.py`, vingt-cinq mutants (base comprise) ; résultat
  `outils/resultat-mutations-lanceur-conception-propre-v1.json` (`e85419533f7cdd33f8755dc607e59f091b5c536390d6edfdcfd97e58f18b0e8f`) : de 23:28 à 23:35 UTC, base **131 passés**, **25 mutants tués sur 25**, aucun survivant (M1 : options, commande, dossier, empreinte, lien ; M2 : git après le détachement, départ non gardé, PID du superviseur, refus au détachement incertain ; preuves dans le dépôt : copies, relevé lié à la fin, copie vérifiée ; relance après fiches, courses non bornées, dépense illisible ; borne de 25, réserve du lecteur, GO sous le pire cas, périmètre ignoré ; arbre, environnement entier, verrou, orphelin, zombie).

## 4. Ce qu'il faut à la session qui lancera

1. **Contre-lecture du lanceur par un autre modèle** (R-2609), sur ce rapport, la conception et le différentiel avec le v3 ;
   puis, si elle ne trouve rien qui bloque, le lanceur reste à l'empreinte de son compagnon (toute correction = v2, R12).
2. **Ligne de GO** inscrite par la mère au montant du pire cas, **21 USD**, type calcul, accordée par Lazar (R-2609),
   échéance au choix, **périmètre contenant les deux expressions** « organisme d'idéation » et « propre conception »
   (proposition : « Organisme d'idéation, atelier d'idées (N-065, rôle 2), sur sa propre conception (juge, proposeurs,
   composition, coût) : une génération, une relance au plus, lecteur de la règle compris ») ; une seule ligne ainsi
   formée, sinon le lanceur refuse.
3. **Crochet de garde chargé** (R-2545) dans une session ouverte sur le dépôt, avec une **épingle** pour ce lanceur sur le
   modèle des couples H2 à H4 et S1, S2 de la vérification du v3 (nom `lancer_course_ideation_conception_propre_v1`,
   empreinte de son compagnon, commande exacte, argument `1`) ; la mère écrit ces couples ; je n'ai pas touché `.claude/`.
   Le lanceur garde de toute façon lui-même la commande et son empreinte (M1).
4. **Bac à sable** : `bubblewrap` présent dans ce conteneur (`/usr/bin/bwrap`) ; **`socat` absent** (à installer par le
   gestionnaire de paquets, routine, comme R-2536) ; la sonde du lanceur exige `actif` et `proc_neuf`.
5. **Relais**, lancés par l'opérateur, clés lues **par leur nom** par les relais seuls (présence vérifiée par
   `[ -n "${NOM:+x}" ]`, jamais la valeur) : relais Claude du clone (`pole/relais_reel.py`) avec `RR_ANTHROPIC_API_KEY_RIGAUD`,
   port 8787, `--plafond-usd 10`, modèles permis limités aux deux du code ; relais Gemini v2 (`relais_gemini_v2.py`,
   `2b0043bc…`) avec `GEMINI_API_KEY`, port 8788, `--max-appels 8`. Plus tard, pour le lecteur : relais Kimi v4 avec
   `KIMI_API_KEY`, `--plafond-usd 4 --max-appels 6 --max-recherches 0`. Arrêt des relais par PID.
6. **Clone** `/home/user/lciric/ideation-organism` à l'arbre `ee84d6ec…`, propre, sans cache d'octets (vrai aujourd'hui).
7. **Commande**, seule et exacte, depuis `/home/user/controle-ia-travail` :
   `/usr/local/bin/python3 -I -B scripts/lancer_course_ideation_conception_propre_v1.py 1` ; la même commande donne ensuite
   le compte rendu (3), la clôture (0) ; arrêt par `kill -TERM <PID du superviseur>`.
8. Après la clôture : la mère lit les fiches copiées et scelle l'attestation (conception, § 3) ; puis l'outil du lecteur et
   le programme de classement, **à écrire, essayer et contre-lire avant tout envoi** (conception, § 8).

## 5. Nœuds pour la mère

- **N1 — famille du lecteur de la règle.** Enjeu : « lecteur neuf d'une autre famille » ; proposeurs et juge sont de deux
  familles (Claude, Gemini). Options : (a) Kimi (`kimi-k3.1-pro`), relais et précédent de lecture existants, ≈ 1,5 USD ;
  (b) Astra (`gpt-6-astra`), sans relais éprouvé ici ; (c) Lazar lui-même, sans coût, plus lent. **Recommandation (a)**,
  confiance 0,7 ; défaut sous 48 heures : (a).
- **N2 — relance.** Le lanceur en permet **une seule au total** (lecture de R-2609 : « conditions reprises » ; R-2558),
  d'où un pire cas de 21 USD ; sans relance, 18,9 USD. **Recommandation : une relance**, confiance 0,65 ; défaut : une.
- **N3 — outil du lecteur et programme de classement** (non écrits) : à confier à un agent neuf, essais et contre-lecture
  avant la lecture ; leur dépense est dans les 21 USD (réserve de 4). Pas de décision de Lazar requise, sauf si N1 = (c).
- **N4 — citations obligatoires dans la question servie** (N-064) : gardées ; elles font connaître POPPER et Co-Scientist
  aux proposeurs, contre l'esprit d'anti-enfermement de N-044 (point 4). Option : question v2 sans elles. Recommandation :
  garder (N-064 l'exige), confiance 0,6.
- **N5 — critères annoncés aux proposeurs** dans la question (transparence) : risque qu'ils optimisent la forme ; L5 (test
  contre les idées tirées au hasard) le mesure. Recommandation : garder, confiance 0,6.

## 6. Réserves

- Témoins écrits par le modèle A, qui est aussi proposeur et juge de l'organisme ; longueurs et style peuvent les
  trahir ; T-DW : principe vérifié page 1, détail du mécanisme non relu page par page.
- Le catalogue (12 entrées) borne la nouveauté mesurée ; « neuve » ici n'est pas « neuve au monde » (R8).
- Attendus du devis calculés sur d'autres courses ; le juge de l'organisme coûte jusqu'à 1,5 USD sans servir la sélection.
- Les heures de rédaction données dans les pièces sont des intervalles bornés par des relevés `date -u`, non des instants.

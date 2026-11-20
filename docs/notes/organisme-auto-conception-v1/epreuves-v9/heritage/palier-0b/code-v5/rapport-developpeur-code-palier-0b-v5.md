# Rapport du développeur — code de l'étage sur processeur du palier 0b, version 5 (préenregistrement v11)

- Auteur : développeur, modèle O (neuf : il n'a écrit ni le texte, ni le code v1 à v4, ni leurs vérifications). Pièce de travail (classe C) rendant une pièce d'instrument (classe B, le code v5). Travail du 2026-11-20 (`date -u` : 11:21Z et 12:00Z en cours de travail ; 12:53Z au scellement).
- Mandat : `heritage/palier-0b/mandat-developpeur-code-palier-0b-v5-v1.md` (`6d099bfcf8406505d57b11e6fda097b810cc1f986750c1ee0034dcf0041b2286`), vérifié par `env -C` sur son dossier et `sha256sum -c` de son compagnon avant tout geste ; lancement accordé par la session mère (« go », 2026-11-20T10:57:51Z). GO-2026-11-20-25, GO-2026-11-20-41 ; décisions de la mère R-4123, R-4182, R-4210 (NE-3 retenu).
- Textes qui font foi, chacun vérifié par `env -C DOSSIER sha256sum -c F.sha256`, empreinte du compagnon égale à celle du mandat : préenregistrement v11 (`9faf31a3dd0278b562c62fbded81222b674f6c5df225006f9e0e8d610b720989`), contrôle v10 → v11 (`88c37d8606851af9063544de01fc6db6cd03b7a29a771cc797f5ea6527eefd0e`, « Conforme », NE-3 au § 5), rapport du code v4 (`2947c4f15729265475fe162d983249b3d98c1c0eccb0a61f94606ba540f2b005`), vérification du code v4 (`183b17d2d28b743e81eedb0c38415ecd273879439bec9a03a52319328397cc5f`), contrôles v8 → v9 (`contre-lecture-v9/controle-differentiel-palier-0b-v8-v9-v1.md`) et v9 → v10 (`controle-v10/controle-differentiel-palier-0b-v9-v10-v1.md`), compagnons OK.
- Lu de la v11 : l'en-tête (« Commit du code d'analyse » et sa table), la section « Seuil » entière, B7 bis, B8, B9 (gardes 25 et 27 et toute la table), l'ordre des opérations, l'annexe H « Version 9 » (§ 1 à 6), « Ce qui demande un code v5 », « Ce qui revient à la mère », « Ce qui n'est pas changé par la version 9 ». Le reste du texte n'a pas été lu en entier (il fait 297 Ko).
- Point de départ : `P0B/code-v4/` du dépôt, vérifié contre la table des 54 empreintes du § 10 du rapport v4 (`sha256sum -c`, 54 OK), copié deux fois dans le bloc-notes (`dev-palier-0b-v5/code-v4/`, gardé intact pour les différentiels et les sorties ; `dev-palier-0b-v5/code-v5/`, copie de travail, d'où le rapport v4 et son compagnon ont été retirés). Code de l'organisme : copie de `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` (garde 17), non modifiée.
- Environnement : Python 3.13.18 (`/home/user/controle-ia-travail/.venv`), mêmes bibliothèques que le code v4. La machine était partagée avec d'autres sessions (charge élevée : les durées ci-dessous en portent la marque).

## 0. Verdict

Les points 1 à 6 de « Ce qui demande un code v5 » et NE-3 sont faits ; le point 7 ne demande rien. **Chaque fichier d'essais lancé seul : neuf fichiers, 107 passés, 0 échoué. Suite entière : 107 passés, 0 échoué (1 424 s).** **L'essai final « aucune graine décisive » passe seul et en suite entière.** **Banc `mutations_v4.py` (113 défauts : les 71 du v3, dont 69 à l'identique et 2 adaptés, et 42 neufs), rejoué en entier : 113 appliqués, 113 vus, chacun par un essai en échec ; témoins au vert.** Sorties : 484 empreintes sur 489 égales à l'octet entre le code v4 et le code v5 ; les 5 qui changent relèvent chacune d'une règle changée (§ 5). Seize silences déclarés (§ 2), aucun tranché ; trois remarques (§ 7) ; aucun refus de permission, de classifieur ni de garde.

## 1. Ce qui a été fait, point par point (« Ce qui demande un code v5 », v11, annexe H, « Version 9 »)

### Point 1 — seuil d'arrêt (`audit.py`, table de l'étape 3)

- `seuil_calibre(sigma0, moyenne)` = M + 2 σ₀ (M : moyenne des mêmes 1 000 exactitudes permutées ; σ₀, ddof = 1, inchangé). La colonne `seuil_calibre` de la table porte M + 2 σ₀ pour les quinze exactitudes (au code v4 : 0,55 + 2 σ₀).
- `lecture(jeu, audit, A, sigma0, moyenne)` (M est désormais reçu, exactitude par exactitude ; contrôle v8 → v9, § 7). Forme des trois audits des mondes par dose : **A au plus 0,55 → tenue, toujours** (même au-dessus de M + 2 σ₀ : version 11, option (ii)) ; A au-dessus de 0,55 et de M + 2 σ₀ → arrêt ; A au-dessus de 0,55 et au plus M + 2 σ₀ → « non départagée du hasard à cette taille », qui lie l'étage payant (mention). Le seuil d'arrêt effectif est donc le plus grand de 0,55 et de M + 2 σ₀. « Au plus » inclusif, « au-dessus de » strict (A = M + 2 σ₀ est « au plus »).
- Forme des deux audits de lois : à la lettre (au-dessus de 0,55, arrêt), inchangée.
- `juger_suites_d_audit` arrête (`ArretGenerateur`) sur les mêmes listes qu'au code v4 ; seules les lectures changent.

### NE-3 — colonne du seuil d'arrêt

- `seuil_d_arret(jeu, audit, sigma0, moyenne)` et colonne `seuil_d_arret` de la table : le plus grand de 0,55 et de M + 2 σ₀ pour la forme des audits des doses ; 0,55 pour la forme des audits de lois ; `None` pour le contenu et les réunis, qui n'arrêtent jamais (silence n° 9). Pour chaque exactitude de forme, « arrêt » équivaut à A au-dessus de `seuil_d_arret` (vérifié par `_verifier_table` sur chaque table tirée par les essais).

### Point 2 — règle calibrée de signalement (`audit.py`)

- Contenu et réunis des trois audits des mondes par dose, jamais un arrêt : A au-dessus de 0,55 et de M + 2 σ₀ → « signalée », mention « générateur non audité pour l'étage payant » ; A au plus 0,55 → « au plus 0,55 », ni signalement ni mention (même au-dessus de M + 2 σ₀ : le cas suit la forme, version 11) ; A au-dessus de 0,55 et au plus M + 2 σ₀ → « non départagée du hasard à cette taille », **ni signalement ni mention** (lecture (i), R-4182) : rangée dans la liste neuve `non_departagees_sans_mention`, et non dans `non_departagees` (forme seule), si bien qu'elle ne pose pas la mention (le code v4 la posait pour toute exactitude non départagée).
- Les quatre exactitudes de contenu et réunies des deux audits de lois restent à la lettre (au-dessus de 0,55 : signalées, mention).
- `lire_audit` exige A, σ₀ et M de chaque exactitude (refus sinon) et rend `lectures`, `arret`, `non_departagees`, `non_departagees_sans_mention`, `signalement`, `mention` ; `audit_presentation` rend les mêmes clés.

### Point 3 — graine des plis de la lecture observée (`mondes.py`)

- `generateurs_de_l_audit(graines, couche)` dérive, dans cet ordre, le générateur des plis de la lecture observée (étiquette `couche=<couche>|famille=audit|role=plis`) et celui des permutations (`…|role=permutation`) ; un seul de chaque pour les quinze exactitudes, parcourues dans l'ordre fixe d'`audit_presentation` (inchangé).
- `juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=1000)` et `audit_du_generateur(graines, doses, suites_par_dose, permutations=1000, couche="audit")` ne reçoivent plus aucun générateur de l'appelant ; ils les dérivent par `generateurs_de_l_audit`. Les rôles sont des constantes du module (`ROLE_PLIS`, `ROLE_PERMUTATION`) ; `graines.py` ne tient pas de liste des rôles (rien n'y est ajouté pour ce point).
- `audit_presentation(mondes, rng, rng_permutation, permutations)` garde son interface (fonction de bas niveau ; les essais aux valeurs plantées et le diagnostic la nourrissent directement).

### Point 4 — verrou des graines décisives (`graines.py`, `constantes.py`, `tirages.py`)

`graines.Autorisation(texte, racine)` remplace l'objet du code v3/v4 (qui nommait un préenregistrement et un erratum). Elle ne se construit que si, dans cet ordre :
1. le texte présenté est scellé, au sens de `controle_ia.scellement.verifier` (remarque 4, (a)) : `verifier_scelle`, réécriture de cette fonction (compagnon d'une seule ligne non vide « <64 hex>  <nom> », nom de base égal, empreinte recalculée égale) — réécrite parce que le paquet se lance seul (silence n° 6) ; un essai la confronte au module du dépôt sur neuf cas (trois sains, six artefacts) : mêmes acceptations, mêmes refus ;
2. l'en-tête du texte se lit (`lire_en_tete_du_texte`) : une seule ligne commençant par `- Commit du code d'analyse : `, le premier `` `<40 hex>` `` de cette ligne est le commit du code ; la table est le premier bloc entre deux lignes « ``` » qui suit cette ligne (silence n° 4) ;
3. la pièce d'autorisation existe à `racine/prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md` et est scellée (même `verifier_scelle`) ;
4. elle porte exactement quatre lignes « nom : valeur » (séparateur «  : », un saut de ligne final permis), dans l'ordre de R-4123 : `identifiant du GO`, `commit du code`, `empreinte du texte scellé`, `heure` (noms : silence n° 1, laissé au développeur par le contrôle v9 → v10, § 6, n° 5) ;
5. l'identifiant du GO a la forme `GO-AAAA-MM-JJ-NN` et figure dans la première colonne d'une ligne de `racine/registres/go.md` (ligne commençant par « | », première cellule égale, blancs retirés) ;
6. le commit de la pièce est celui de l'en-tête du texte ; l'empreinte de la pièce est celle du texte présenté, recalculée ;
7. l'heure est en UTC, forme seule : sortie de `date -u` en locale C (`Fri Nov 20 10:57:51 UTC 2026`) ou ISO 8601 en Z (`2026-11-20T10:57:51Z`) (silence n° 2) ;
8. chaque module lancé — les fichiers `.py` du paquet `heritage_etage_processeur_v1` et le `__init__.py` du paquet parent, sur disque, là d'où le paquet est importé — a l'empreinte que la table du texte lui donne, et la table ne nomme sous `src/` aucun fichier qui ne soit un module lancé ; les lignes hors de `src/` sont ignorées (silence n° 5).
Tout refus est une `GraineRefusee` « autorisation refusée : … ». Les couches « decisif » et « confirmation » restent refusées sans autorisation (et consignées), comme au code v4. `tirages.exiger_autorisation_pour` revérifie l'autorisation sur disque avant tout lancement d'une couche décisive (silence n° 7). `constantes.py` : `PREENREGISTREMENT_SHA256` (empreinte de la v6) est retirée ; aucune empreinte du texte n'est écrite dans le code ; l'en-tête dit « préenregistrement v11 ; code v5 » (silence n° 13 du code v4) ; constantes neuves `CHEMIN_PIECE_D_AUTORISATION`, `CHAMPS_DE_LA_PIECE`, `CHEMIN_REGISTRE_DES_GO`, `LIGNE_DU_COMMIT`, `PREFIXE_DES_MODULES`. Manifeste (`tirages.ecrire_manifeste`, remarque 4, (e)) : à la place de `preenregistrement_sha256`, `texte_sha256`, `piece_d_autorisation_sha256` et `heure_d_autorisation`, pris de l'autorisation des graines, `null` tous trois sans autorisation (couches non décisives ; silence n° 8) ; `verifier_manifeste` arrête si l'un manque, s'ils ne sont pas tous trois nuls ou tous trois inscrits, ou si `preenregistrement_sha256` reparaît.

### Point 5 — jeu de la garde 27 (`etapes.py`, `mecanique.py`, `mondes.py`, `constantes.py`)

- `etapes.lancer_etape_4(graines, couche, dossier, doses, proposeurs, sources, sous_ensemble, organisme)` est le programme de lancement de l'étape 4 : `etape_4` (bras 1 à 3, dossier `bras-1-a-3/`), puis, dans le même appel (mêmes graines, même couche), `etape_4_jeu_de_la_garde_27` (dossier `jeu-de-la-garde-27/`) avec le lecteur réglé pour la tenue au réglage de l'étape 4 (`P.configuration("lecteur-tenue", **REGLAGES_ETAPE_4)`, soit τ = 2) et trois sources ; proposeur et nombre de sources ne sont pas des paramètres (`PROPOSEUR_JEU_GARDE_27 = "lecteur-tenue"`, `SOURCES_JEU_GARDE_27 = 3`). `etape_4_jeu_de_la_garde_27` garde ses paramètres (au moins deux sources), pour les essais du code v4 (silence n° 12).
- Garde 27 à trois sources : `mondes.generer_jeu_avec_etrangeres` garde avec chaque suite la source face à laquelle la marge de ses mondes cibles est construite (`etrangere`, posée à la construction et non plus après) et `verifier_etrangeres_du_jeu` arrête si ce n'est pas la source suivante ; `mecanique.verifier_source_etrangere(sortie_etrangere, suite)`, appelée par `jouer_jeu_diagnostic` avant les bras 4a et 4b de chaque source, arrête si ce qui est déposé (registre de la course et copie du bras 2) ne vient pas de cette source (comparaison d'identité des mondes sources ; silence n° 13). Au code v4, un registre de la source précédente servi aux bras 4a et 4b passait la garde (son empreinte était comparée à elle-même) ; à deux sources, précédente et suivante se confondent, à trois la garde le voit.

### Point 6 — essais et banc

Voir § 3 et § 4 : chaque artefact demandé a son essai, chaque règle son défaut au banc.

### Point 7 — sans changement

Les silences n° 1, 2, 4, 5, 9, 10 du code v4 (ddof = 1 ; un générateur de permutations ; égalités ; « pas exactement deux classes » ; écart-type réuni de D8 ; fichier des étiquettes) sont tels que le code v4 les avait comblés ; n° 6, 7, 11, 12 non touchés (`outils-dev/diagnostic_presentation.py` garde l'interface du code v3 et ne tourne toujours pas) ; la tenue.

## 2. Silences du texte, déclarés (rien n'est tranché ; chacun est à inscrire ou à corriger par l'erratum du commit)

1. **Noms des quatre champs de la pièce** : `identifiant du GO`, `commit du code`, `empreinte du texte scellé`, `heure` ; séparateur «  : » (espace, deux-points, espace) ; valeur sans blanc en tête ni en queue ; un saut de ligne final permis, aucune autre ligne (le contrôle v9 → v10, § 6, n° 5, laisse les noms au développeur, dans l'ordre de R-4123).
2. **Formes de l'heure** admises : `%a %b %d %H:%M:%S UTC %Y` (sortie de `date -u`, locale C ; un jour d'un chiffre précédé de deux espaces est admis) et `%Y-%m-%dT%H:%M:%SZ` ; la date doit exister. Rien d'autre n'est contrôlé (« forme seule »).
3. **Forme de l'identifiant du GO** : `GO-` + quatre chiffres, deux, deux, puis au moins deux chiffres.
4. **Lecture de l'en-tête du texte** : une seule ligne du texte commence par `- Commit du code d'analyse : ` (refus si zéro ou plusieurs) ; le commit est le premier groupe de 40 chiffres hexadécimaux minuscules entre accents graves de cette ligne ; la table est le premier bloc de code qui suit, ouvert et fermé par une ligne égale à « ``` » une fois les blancs retirés ; chaque ligne non vide du bloc est « <64 hex>  <chemin> » (deux espaces), sans chemin double.
5. **« Chaque module du code lancé »** : les fichiers `.py` du dossier du paquet importé et le `__init__.py` du paquet parent (`src/controle_ia/__init__.py`), sous les chemins `src/controle_ia/heritage_etage_processeur_v1/<f>.py` ; la table doit nommer exactement ces fichiers sous `src/` ; les autres lignes (outils, essais) ne sont pas contrôlées par le verrou.
6. **« Scellée au sens de `controle_ia.scellement.verifier` »** : réécrit dans `graines.verifier_scelle` (le paquet se lance avec `PYTHONPATH=src` seul, où `controle_ia.scellement` n'existe pas) ; l'essai `test_scelle_au_sens_du_depot` charge le module du dépôt sous un autre nom de paquet et vérifie l'accord sur neuf cas.
7. **Quand le verrou est vérifié** : à la construction de l'`Autorisation`, puis de nouveau, sur disque, à chaque `exiger_autorisation_pour` d'une couche décisive (début de `lancer_famille`) ; non à chaque dérivation de graine.
8. **Manifeste** : noms `texte_sha256`, `piece_d_autorisation_sha256`, `heure_d_autorisation` ; `null` tous trois sans autorisation. L'identifiant du GO et le commit de la pièce ne sont pas inscrits (l'empreinte de la pièce les fixe) ; le champ `commit` du manifeste reste celui que donne l'appelant (point (d) : la mère en répond) et n'est pas comparé à celui de la pièce.
9. **Colonne du seuil d'arrêt (NE-3) hors de la forme des doses** : 0,55 pour la forme des audits de lois (lettre de la version 6), `None` pour le contenu et les réunis ; NE-3 ne dit que « le plus grand de 0,55 et de M + 2 σ₀ ».
10. **Mots et listes de la règle de signalement** : la zone médiane du contenu et des réunis porte la lecture « non départagée du hasard à cette taille » (les mots du texte) et va dans la liste `non_departagees_sans_mention` ; « au plus 0,55 » reste le mot des exactitudes de contenu et réunies non signalées, comme au code v4.
11. **Ordre et lieu de la dérivation des deux générateurs de l'audit** : `generateurs_de_l_audit`, plis d'abord, permutation ensuite, au début de `juger_suites_d_audit` ; le texte dit « dérivé avant le lancement, par le code de l'étape 3 ».
12. **Programme de lancement de l'étape 4** : `lancer_etape_4` ; ses paramètres `doses`, `proposeurs`, `sources`, `sous_ensemble`, `organisme` passent à `etape_4` (défauts : les valeurs gelées), pour que les essais le jouent réduit ; dossiers `bras-1-a-3/` et `jeu-de-la-garde-27/` ; `etape_4_jeu_de_la_garde_27` garde ses paramètres sans défaut (au moins deux sources).
13. **Garde 27, ce qui est comparé** : l'identité de l'objet monde source de la sortie déposée avec celui que la suite garde comme étrangère de construction (`suite.etrangere`) ; à la fin de la construction, `suite.etrangere` doit être la source de la suite suivante. Les deux arrêts nomment la garde 27.
14. **Racine de l'arbre lancé et texte présenté** : donnés par l'appelant de `Autorisation(texte, racine)` ; aucun programme de lancement des étapes 8 et 9 n'existe encore (comme au code v4), qui les donnerait.
15. **« Sur `main` »** (remarque 4, (d)) : non contrôlé par programme ; la mère en répond.
16. **Le verrou n'arrête pas les couches non décisives** : les étapes 3 à 7 (audit, couche mécanique, étalonnage) ne demandent pas d'autorisation, comme au code v4 ; la liste d'arrêt, point 1, les interdit tant que l'erratum du commit n'est pas contre-lu, et cela ne se vérifie pas par programme (B8 : « la mère en répond »).

## 3. Essais

Lancement : `PYTHONPATH=src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/code-organisme-94bfd92/orchestrator /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider CHEMIN`, dossier courant `code-v5/`, par l'outil `travail/lancer_essais_v1.py` : un processus par fichier, puis, en même temps, un processus pour la suite entière ; rien d'écrit dans le dépôt. Journaux : `travail/essais-fichiers-v1.log`, `travail/essais-suite-v1.log`.

| fichier d'essais | seul | durée seul | changé ? |
|---|---|---|---|
| `etapes` | **6 passés** (5 du v4 ; 1 neuf : programme de lancement de l'étape 4, garde 27 à trois sources) | 404 s | oui |
| `gardes` | 17 passés | 2,5 s | non |
| `mecanique` | 10 passés | 367 s | non |
| `mondes` | **18 passés** (15 du v4, dont quatre récrits ou étendus — valeurs plantées, dose inscrite, étape 3, marge à trois sources — et trois qui lisent la table par `_verifier_table`, récrit ; 3 neufs) | 430 s | oui |
| `organisme` | 5 passés | 187 s | non |
| `outils` | 15 passés (1 adapté à l'interface neuve du verrou) | 0,9 s | oui |
| `statistique` | 11 passés (manifeste étendu) | 8,8 s | oui |
| `verrou` | **24 passés** (fichier neuf : 4 essais, dont 20 artefacts paramétrés) | 6,3 s | neuf |
| `zz_aucune_graine_decisive` | 1 passé | 0,3 s | non |
| total, un processus par fichier | **107 passés, 0 échoué** | | |
| **suite entière, un processus** | **107 passés, 0 échoué** | 1 424 s | |

6 + 17 + 10 + 18 + 5 + 15 + 11 + 24 + 1 = 107, le même compte qu'en suite entière. **L'essai final « aucune graine décisive » passe seul et en suite entière** ; les seules couches dérivées par les essais sont « essai » et « essai-de-forme ». Avant le lancement final, les fichiers `etapes`, `mondes` et `mecanique` avaient été joués une première fois (journaux `travail/prelim-*-v1.log`, au vert) ; le code n'a pas changé depuis.

Essais neufs ou changés, avec cas sain et artefact (règle R5) :

| règle | cas sain | artefact | essai |
|---|---|---|---|
| point 1 : seuil M + 2 σ₀ | table plantée à 0,5 : rien ; zone médiane (0,58 ; σ₀ 0,02 ; M 0,55) : mention sans arrêt ; 0,55 tout juste : tenue | 0,60 (M 0,5) : arrêt ; version 9 : M au-dessus de 0,55 (0,61 ; σ₀ 0,02 ; M 0,58), aucun arrêt, mention ; M sous 0,5 (0,60 ; σ₀ 0,04 ; M 0,46), arrêt | `mondes::test_garde_25_lecture_calibree_sur_valeurs_plantees` |
| version 11 : au plus 0,55 jamais un arrêt | 0,53 et 0,55 avec M + 2 σ₀ = 0,49 : forme tenue, contenu et réunis « au plus 0,55 », ni signalement ni mention ; seuil d'arrêt 0,55 | — (le défaut « arrêt sur une exactitude au plus 0,55 » est vu) | `mondes::test_garde_25_au_plus_0_55_jamais_un_arret_ni_un_signalement` |
| égalité A = M + 2 σ₀ | 0,625 = 0,5 + 2 × 0,0625 (exact en binaire) : forme non départagée, contenu non départagé sans mention | 0,625 + 10⁻¹² : arrêt (forme), signalement (contenu) | `mondes::test_garde_25_egalite_au_seuil_calibre_au_plus` |
| NE-3 | colonnes `seuil_calibre` et `seuil_d_arret` (plancher 0,55 ; lois 0,55 ; contenu None) | exactitude inconnue : refus | `mondes::test_colonne_du_seuil_d_arret_ne_3` ; `_verifier_table` dans les essais qui tirent une table |
| point 2 : signalement calibré | contenu et réunis des doses au-dessus des deux seuils : signalés, mention, aucun arrêt | zone médiane (0,58 ; 0,03 ; 0,53 et 0,57 ; 0,02 ; 0,54) : ni signalement ni mention ; lois à la lettre : forme 0,56 (M + 2 σ₀ = 0,58) arrêt, contenu 0,56 signalé ; table sans M : refus | `mondes::test_garde_25_lecture_calibree_sur_valeurs_plantees` |
| point 3 : plis observés | l'étape 3 dérive `role=plis` puis `role=permutation` ; exactitudes et table égales à celles d'`audit_presentation` nourri de ces deux générateurs | aucun paramètre « rng » à `juger_suites_d_audit` ni à `audit_du_generateur` ; plis tirés du générateur des permutations : exactitudes différentes | `mondes::test_etape_3_jugement_des_suites_et_arrets` (changé) |
| point 4 : verrou | `Autorisation` sur un arbre factice, deux formes d'heure (et un jour d'un chiffre) ; revérification avant un lancement décisif sans rien tirer ; manifeste à trois champs ; `verifier_manifeste` | vingt artefacts, un par condition (texte sans compagnon, altéré, compagnon à deux lignes, au mauvais nom ; pièce absente, sans compagnon, altérée, champs dans un autre ordre, trois lignes ; GO absent, hors de la première colonne, mal formé ; registre des GO absent ; commit différent ; deux lignes de commit ; empreinte du texte différente ; heure non UTC ; module d'empreinte différente, absent de la table, table nommant un module non lancé) ; pièce ou module changés après la construction : refus au lancement | `verrou::test_verrou_cas_sain_sans_graine_decisive`, `verrou::test_verrou_artefact[…]` (20), `verrou::test_verrou_verifie_de_nouveau_avant_un_lancement_decisif` |
| point 4 : « scellée » au sens du dépôt | trois compagnons sains acceptés par les deux | six artefacts refusés par les deux | `verrou::test_scelle_au_sens_du_depot` |
| point 4 : constante v6 retirée | aucune empreinte de 64 hex dans `constantes.py` ; en-tête v11 | — (le défaut « constante rétablie » est vu) | `verrou::test_constantes_sans_empreinte_du_texte` |
| point 4 : manifeste (e) | sans autorisation : trois champs `null`, plus de `preenregistrement_sha256` | un champ retiré, un seul inscrit, `preenregistrement_sha256` rétabli (compagnon refait) : arrêt | `statistique::test_manifeste_d_un_lancement` (étendu) |
| point 5 : programme de lancement | `lancer_etape_4` (étape 4 réduite à une source et deux proposeurs) : étiquettes `etape-4` toutes avant `etape-4-garde-27`, même couche ; jeu : lecteur-tenue, τ = 2, trois sources, dose 0,25 ; chaque source reçoit aux bras 4a et 4b le registre et les vues de la suivante | dépôt de la source précédente, ou de la source propre : arrêt (`verifier_source_etrangere`) | `etapes::test_lancer_etape_4_bras_1_a_3_puis_jeu_de_la_garde_27_a_trois_sources` |
| point 5 : construction | à trois sources, `etrangere` de chaque suite est la source suivante | `etrangere` plantée à la précédente : arrêt (`verifier_etrangeres_du_jeu`) | `mondes::test_marge_face_a_la_source_etrangere` (étendu) |
| ancien essai du verrou | — | texte non scellé : refus (interface neuve) | `outils::test_couches_disjointes_et_decisif_refuse_sans_autorisation` (adapté) |

Les essais de l'audit jouent 20 permutations (50 pour la dose inscrite), non 1 000 ; `PERMUTATIONS_AUDIT == 1000` est vérifié. L'essai de la dose inscrite (`mondes::…dose_inscrite…`) lit désormais l'arrêt au-dessus de `seuil_d_arret`.

## 4. Banc des défauts (`outils-dev/mutations_v4.py`)

Version 4 du banc : les 71 défauts de `mutations_v3.py`, dont 69 repris à l'identique (remplacements, fichiers, essais qui les voient) et deux adaptés au code v5 parce que leur texte ancien n'existe plus (« zone-mediane-arretee » : `return NON_DEPARTAGEE` → `return ARRET` ; « seuil-calibre-a-vingt-sigma » : M + 20 σ₀ ; même essai, `mondes -k lecture_calibree`) ; « regle-calibree-etendue-aux-lois », repris à l'identique, est sur le code v5 le défaut « calibrage étendu aux audits de lois » du point 6 (vu par l'essai neuf des valeurs plantées, même sélection) ; et **42 défauts neufs**. Mode `--verifier` : « défauts 113, identifiants distincts 113, problèmes 0 ». Option neuve `--partie v3|v4`, qui joue les 71 défauts de la version 3 ou les 42 neufs. Rejoué en entier, en deux parties parallèles, chaque partie jouant d'abord les témoins de ses sélections sur le code sain : **partie « v3 », 71 défauts, 71 vus ; partie « neufs », 42 défauts, 42 vus ; témoins au vert dans les deux.** Chaque défaut est vu par un essai en échec de code 1 (113 sur 113 ; aucun code 2 ou plus, donc aucune erreur de collecte). Sorties : `outils-dev/mutations-v4-sortie-partie-v3-v1.json`, `outils-dev/mutations-v4-sortie-partie-neufs-v1.json`. Aucun défaut n'ouvre le verrou des couches décisives : ceux du verrou l'affaiblissent sur des arbres factices, où les essais attendent un refus, et aucun essai ne dérive de graine décisive.

Les 42 défauts neufs (durées sous une machine chargée) :

| défaut | règle | fichier muté | essai qui le voit | durée |
|---|---|---|---|---|
| seuil-reste-a-0-55-plus-2-sigma | point 1 | `audit.py` | `mondes -k lecture_calibree` | 0,6 s |
| arret-sur-une-exactitude-au-plus-0-55 | point 1, v11 | `audit.py` | `mondes -k au_plus_0_55` | 0,7 s |
| egalite-au-seuil-calibre-lue-au-dessus | silence n° 4 au seuil neuf | `audit.py` | `mondes -k egalite` | 0,5 s |
| seuil-d-arret-sans-plancher | NE-3 | `audit.py` | `mondes -k colonne` | 0,6 s |
| colonne-du-seuil-calibre-a-0-55-plus-2-sigma | point 1 (colonne) | `audit.py` | `mondes -k taille_reduite` | 24,1 s |
| colonne-du-seuil-d-arret-absente | NE-3 | `audit.py` | `mondes -k taille_reduite` | 22,6 s |
| contenu-des-doses-a-la-lettre | point 2 | `audit.py` | `mondes -k lecture_calibree` | 0,4 s |
| signalement-calibre-qui-arrete | point 2 | `audit.py` | `mondes -k lecture_calibree` | 0,7 s |
| calibrage-etendu-au-contenu-des-lois | point 2 (lois à la lettre) | `audit.py` | `mondes -k lecture_calibree` | 0,5 s |
| zone-mediane-du-contenu-mentionnee | point 2, lecture (i) | `audit.py` | `mondes -k lecture_calibree` | 0,4 s |
| plis-recus-de-l-appelant | point 3 | `mondes.py` | `mondes -k etape_3` | 27,8 s |
| plis-tires-du-generateur-des-permutations | point 3 | `mondes.py` | `mondes -k etape_3` | 26,5 s |
| plis-sous-le-role-permutation | point 3 | `mondes.py` | `mondes -k etape_3` | 24,8 s |
| constante-de-la-version-6-retablie | point 4 | `constantes.py` | `verrou -k constantes` | 0,4 s |
| verrou-texte-non-scelle | point 4, compagnon du texte | `graines.py` | `verrou -k artefact` | 0,5 s |
| verrou-piece-non-scellee | point 4 (a) | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-compagnon-a-plusieurs-lignes | point 4 (a) | `graines.py` | `verrou -k "artefact or depot"` | 0,4 s |
| verrou-compagnon-au-mauvais-nom | point 4 (a) | `graines.py` | `verrou -k "artefact or depot"` | 0,5 s |
| verrou-piece-a-moins-de-quatre-lignes | point 4 (c) | `graines.py` | `verrou -k artefact` | 0,5 s |
| verrou-ordre-des-champs-non-exige | point 4 (c) | `graines.py` | `verrou -k artefact` | 0,5 s |
| verrou-go-non-cherche-au-registre | point 4 (b), GO | `graines.py` | `verrou -k artefact` | 0,5 s |
| verrou-go-hors-de-la-premiere-colonne | point 4 (b), GO | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-forme-du-go-non-lue | point 4 (b), GO | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-commit-non-compare | point 4 (b), commit | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-deux-lignes-de-commit | point 4 (b), commit | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-empreinte-du-texte-non-comparee | point 4 (b), empreinte | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-heure-non-lue | point 4 (b), heure | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-modules-non-controles | point 4, modules | `graines.py` | `verrou -k artefact` | 0,5 s |
| verrou-empreinte-des-modules-non-comparee | point 4, modules | `graines.py` | `verrou -k artefact` | 0,5 s |
| verrou-module-absent-de-la-table | point 4, modules | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-module-non-lance-dans-la-table | point 4, modules | `graines.py` | `verrou -k artefact` | 0,4 s |
| verrou-non-reverifie-au-lancement | point 4 (silence n° 7) | `tirages.py` | `verrou -k verifie_de_nouveau` | 0,5 s |
| manifeste-sans-empreintes-du-verrou | point 4 (e) | `tirages.py` | `verrou -k cas_sain` | 0,4 s |
| manifeste-champs-du-verrou-non-verifies | point 4 (e) | `tirages.py` | `statistique -k manifeste` | 0,5 s |
| source-precedente-servie | point 5 (« source précédente au lieu de suivante ») | `mecanique.py` | `etapes -k lancer_etape_4` | 359,3 s |
| origine-du-depot-non-verifiee | point 5 | `mecanique.py` | `etapes -k lancer_etape_4` | 366,6 s |
| marge-construite-face-a-la-source-precedente | point 5 | `mondes.py` | `mondes -k marge_face` | 146,3 s |
| etrangeres-du-jeu-non-verifiees | point 5 | `mondes.py` | `mondes -k marge_face` | 314,5 s |
| jeu-a-deux-sources | point 5 | `etapes.py` | `etapes -k lancer_etape_4` | 47,4 s |
| jeu-joue-par-le-lecteur-heritage | point 5 | `etapes.py` | `etapes -k lancer_etape_4` | 338,0 s |
| jeu-avant-les-bras-1-a-3 | point 5 | `etapes.py` | `etapes -k lancer_etape_4` | 368,1 s |
| jeu-non-joue | point 5 | `etapes.py` | `etapes -k lancer_etape_4` | 14,1 s |

Le défaut « source précédente au lieu de suivante » ne peut être vu qu'à trois sources : à deux, (k − 1) mod 2 = (k + 1) mod 2, et le défaut ne change rien au jeu (raison des trois sources, remarque 3) ; l'essai du jeu à deux sources du code v4 (`mecanique -k garde_27_bras`) est gardé tel quel, et n'a pas été joué sous ce défaut.

## 5. Sorties : ce qui reste égal à l'octet, ce qui change et pourquoi

Outil `travail/empreintes_sorties_v1.py` (graines « essai » seulement ; mêmes appels ; un processus par paquet, le paquet importé de son seul `src`), comparé par `travail/comparer_empreintes_v1.py` entre la copie intacte du code v4 et le code v5 : **484 empreintes sur 489 égales à l'octet, 5 différentes** (`travail/comparaison-sorties-v4-v5.txt`).

Égales (484) : couche statistique, sept proposeurs, deux doses, bras 1 à 4b (M1, D, I, lois fausses tenues ; 280) ; générateur, six suites des trois doses (clés, épisodes et partage de chaque monde, compteurs) ; `mondes_pour_l_audit` ; traits de forme et de contenu ; distribution des traits de contenu ; exactitudes observées d'`audit_presentation` à générateurs donnés, et ses σ₀ et M ; `exactitude_equilibree`, `sous_permutation`, `jetons` ; sorties scellées d'une case et liste des étiquettes de `lancer_famille` ; le manifeste privé des champs du verrou ; **le jeu de la garde 27 à deux sources et à trois sources** (registres, mesures, entrées servies, reliquats, registres sources, empreintes des vues du bras 2, clés des mondes) : les contrôles neufs de la garde 27 ne changent rien de ce qui est tiré ni écrit ; l'exactitude de l'étape 3 calculée par `audit_presentation` nourri des générateurs « plis » et « permutation » (même valeur dans les deux paquets, et égale à celle que l'étape 3 du code v5 rend d'elle-même).

| sortie différente | pourquoi |
|---|---|
| `audit/presentation/table` | point 1 et NE-3 : `seuil_calibre` vaut M + 2 σ₀ ; colonne `seuil_d_arret` neuve ; lectures selon les règles de la v11 |
| `audit/presentation/lecture` | points 1 et 2 : liste neuve `non_departagees_sans_mention` ; lectures et mention selon la v11 |
| `etape_3/derivation` | point 3 : l'étape 3 dérive `couche=essai|famille=audit|role=plis` puis `…|role=permutation` (au code v4 : générateurs reçus de l'appelant) |
| `etape_3/rapport/exactitudes` | point 3 : les plis observés viennent du générateur du rôle « plis » ; la valeur est celle du code v4 nourri de ce générateur |
| `tirages/manifeste_sans_versions` | point 4, (e) : `texte_sha256`, `piece_d_autorisation_sha256`, `heure_d_autorisation` à la place de `preenregistrement_sha256` ; le reste du manifeste est égal |

Changent de sort, sans sortie à comparer : un registre de la source précédente déposé aux bras 4a et 4b arrête (au code v4 : servi) ; l'objet `Autorisation` a une autre interface, et rien ne la construit hors des essais. Fichiers : `travail/empreintes-v4.json`, `travail/empreintes-v5.json`.

## 6. Ce que l'erratum du commit devra inscrire au texte (liste exacte ; rien n'y est tranché par moi)

1. **La ligne « Commit du code d'analyse » de l'en-tête** : le commit du code v5 (celui que la mère poussera), et la table des empreintes du code v5 (§ 11 de ce rapport, chemins relatifs à `palier-0b/code-v5/`, 58 lignes, ce rapport exclu ; la table extraite, une ligne par fichier, a pour empreinte `56bddae73a01d52fba363b263184aae4c3ffce8aaf654df07de2c9d67be1a15a`, fichier `travail/table-empreintes-code-v5.txt`). **Forme exigée par le verrou** (silence n° 4) : la ligne commence par `- Commit du code d'analyse : `, elle est la seule du texte à commencer ainsi, et son premier `` `<40 hex>` `` est le commit ; la table est le premier bloc « ``` » qui la suit, une ligne « <64 hex>  <chemin> » par fichier, et elle nomme sous `src/` exactement les vingt-quatre fichiers du code lancé (les vingt-trois `.py` du paquet et `src/controle_ia/__init__.py`). Le commit inscrit doit être celui que portera la pièce d'autorisation.
2. **B8, alinéa « Version 9 », et la remarque 4 de l'annexe H** : les noms des quatre champs de la pièce, leur forme « nom : valeur » et les formes d'heure admises (silences n° 1 à 3) ; la lecture de « chaque module du code lancé » (silence n° 5) ; que « scellée » est éprouvé par une réécriture de `controle_ia.scellement.verifier` confrontée au module du dépôt (silence n° 6) ; le moment des vérifications (silence n° 7) ; les noms des trois champs du manifeste et leur valeur nulle hors des couches décisives (silence n° 8).
3. **Section « Seuil » (ou la table de l'étape 3, NE-3)** : le texte NE-3 du contrôle v10 → v11 (§ 5), retenu par la mère (R-4210), et la valeur de la colonne du seuil d'arrêt hors de la forme des doses (silence n° 9) ; les mots de la zone médiane du contenu et des réunis (silence n° 10).
4. **Section « Seuil », « Précisions de la version 9 »** : l'ordre de dérivation des générateurs « plis » puis « permutation » (silence n° 11).
5. **B7 bis, garde 27, remarque 3** : le nom du programme de lancement (`etapes.lancer_etape_4`), ses dossiers, et ce que la garde compare (silences n° 12 et 13) ; que `etape_4_jeu_de_la_garde_27` garde des paramètres sans défaut (au moins deux sources).
6. **« Ce qui demande un code v5 »** : fait par le code v5 (ce rapport, chemin et empreinte), à vérifier par le contre-lecteur du code ; et la ligne « Commit du code d'analyse » et la réserve 24 qui disent encore le code v4 à venir.
7. **Annexe C** : le fichier d'essais neuf `tests/test_heritage_etage_processeur_v1_verrou.py`, les comptes d'essais (§ 3) et le banc `mutations_v4.py` (§ 4).
8. **Ordre des opérations, point 2, et statut** : code v5 écrit ; restent sa vérification par le contre-lecteur du code, l'erratum contre-lu, le scellement par la mère, puis la pièce d'autorisation écrite par la mère après le GO de Lazar sur le palier.
9. **Tenue que le contrôle v10 → v11 laisse à cette version** (§ 4, réserve 7 ; § 5, NE-4) : le statut, la section « Contre-lecture » et la ligne de version (contrôle de la v11 fait, « Conforme »), NE-4 si la mère le veut.

## 7. Remarques (aucune n'est tranchée)

1. **La pièce d'autorisation ne nomme pas le texte présenté par son chemin** : le verrou lit le texte que l'appelant présente et compare son empreinte à celle de la pièce ; c'est ce que dit la remarque 4, (b). Le manifeste inscrit l'empreinte du texte présenté, non son chemin.
2. **Le commit de la pièce n'est comparé qu'à celui de l'en-tête du texte**, non au commit de l'arbre que le manifeste inscrit (`commit`, donné par l'appelant) ; l'accord des modules lancés avec la table du texte tient lieu de contrôle du code.
3. **Constat des essais (sans lecture de critère)** : sous la règle de la v11, le cas sain par construction (300 mondes par dose) n'arrête toujours pas et n'a aucune exactitude de forme non départagée, et la dose inscrite arrête toujours ; les tables tirées à taille réduite sont seulement contrôlées pour leur cohérence avec la règle (`_verifier_table`), sans qu'aucune lecture n'y soit exigée. Aucun audit à pleine taille n'a été fait.

## 8. Gestes, refus et incidents

- **Aucun refus de permission, de classifieur ni de garde.** Aucun incident de l'outil de remplacement (règle R-4067) : chaque remplacement a été appliqué au premier essai ; le banc vérifie ses 113 ancres (`mutations_v4.py --verifier`, « problèmes 0 ») avant d'être joué.
- Une commande simple par appel ; aucun heredoc, aucun code en ligne passé à un interpréteur : chaque calcul passe par un fichier de `travail/`. Calculs longs en tâche de fond ; attente par `timeout … tail -F` ; aucun processus arrêté.
- Graines : seulement la couche « essai » (essais, banc, sorties) et des générateurs locaux de numpy (valeurs plantées, sorties) ; aucune graine des couches « etalonnage », « mecanique », « mecanique-reglages », « audit », « decisif » ou « confirmation » dérivée ; les seules demandes de couches décisives sont celles des essais des refus, toutes refusées. Les essais du verrou construisent des autorisations sur des arbres factices (dossiers temporaires) et ne dérivent aucune graine décisive. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille ; aucun taux de rejet, aucune puissance, aucune valeur p calculés.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau (ni `git fetch` ni `git show` : le dépôt local suffisait) ; aucune écriture dans le dépôt, aucun commit ; le dépôt a été lu seulement (un essai importe `controle_ia.scellement` du dépôt, `-B`, sans écrire de cache) ; rien sous `archives-reponses-modeles/` ni sous `/root/.claude/` (deux sorties longues de commandes y ont été rangées par l'outil lui-même) ; aucune valeur de clé ; aucun identifiant de modèle.

## 9. Fichiers et empreintes

Dossier rendu : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-palier-0b-v5/code-v5/` (arborescence du code v4 : `src/`, `tests/`, `outils-dev/`, et ce rapport). Chaque fichier a son compagnon `.sha256` au format de `sha256sum` lancé dans son dossier (`travail/sceller_tout_v1.py`) ; ce rapport a le sien. La table entière (58 fichiers, ce rapport exclu) est au § 11 ; elle se vérifie par `sha256sum -c` dans `code-v5/`.

Fichiers changés ou neufs (les 44 autres sont ceux du code v4, à l'octet ; le rapport v4 n'est pas dans ce dossier) :

```
7b341b6201a9f9809dfcb7e9aab1d5eb32cb7186559c8d9d21b5f270eb634d32  src/controle_ia/heritage_etage_processeur_v1/audit.py
74c477d7d63e168e597b811ed7777a93d3014523d7a722b5e757b5d65d1cde77  src/controle_ia/heritage_etage_processeur_v1/constantes.py
38d9bf69e307479e95a79b20dfa61dc4637c7364040baa19afe24ddafefc536b  src/controle_ia/heritage_etage_processeur_v1/etapes.py
d0c0d56f2ae05a0a32df4de767e5c5571a19c37e28c9f28229566aa04c2ee1c6  src/controle_ia/heritage_etage_processeur_v1/graines.py
8c109627d5adf1a97de83f576a662325c628ae5e8bb2f56fb9c98f157f5c847d  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
6ac98e67fc54f66878f66542c08ec6fa76dcfc4ff7ada6b4856baea8e6db6bd3  src/controle_ia/heritage_etage_processeur_v1/mondes.py
8e818c8a0f8af8ebe548c1a3f60d604d9692f3b12c78a21dadd20523d421b0c8  src/controle_ia/heritage_etage_processeur_v1/tirages.py
618f5ec0319e4107da5d446af3d8a4ff9c14f545facbf5a21dd94a1309cf02b3  tests/test_heritage_etage_processeur_v1_etapes.py
e0784e8222e60c408a1ea331972ba9abafec1e98bf758ca1d82ad4d562c3427a  tests/test_heritage_etage_processeur_v1_mondes.py
51ac18e130e621c83319dae63604fd084064dd95bdade144c18f0ec6551ccdad  tests/test_heritage_etage_processeur_v1_outils.py
ec63d2a334fb2cd5ee1507fcb8d952fbb3434e6a61a8c614697ab1d892659061  tests/test_heritage_etage_processeur_v1_statistique.py
13ae019f45efdf75500bfa2496dba19ef070f50e04968f2309299afdde1b3d53  tests/test_heritage_etage_processeur_v1_verrou.py
90ff3c401a0648080a2e8123ad70be1fed86cd099c21acc093da07f0f8fa0316  outils-dev/mutations_v4.py
c62360babafb9987bc8806a46ec00fe04a3bb124acd00208e9de99327f8874d8  outils-dev/mutations-v4-sortie-partie-v3-v1.json
09fccbd6b9019d62ce428cdf636826775ef772ac67061b8a425a4d4d79a896f8  outils-dev/mutations-v4-sortie-partie-neufs-v1.json
```

Les empreintes de la table ont été relevées avant le lancement final des essais (`travail/table-avant-essais-v1.txt`) et relevées de nouveau au scellement (`travail/table-empreintes-code-v5.txt`) : les deux fichiers ont la même empreinte (`56bddae73a01d52fba363b263184aae4c3ffce8aaf654df07de2c9d67be1a15a`) ; le code et les essais n'ont pas changé entre le banc, la suite au vert et le scellement. `graines.py` change (verrou) ; `etalonnage.py`, `analyse.py` et les autres modules gardent l'empreinte du code v4.

Non rendus, laissés dans le bloc-notes (`dev-palier-0b-v5/`) : `code-v4/` (copie intacte) ; `code-organisme-94bfd92/` (copie) ; `travail/` : `lancer_essais_v1.py`, `empreintes_sorties_v1.py`, `comparer_empreintes_v1.py`, `differentiels_v1.py`, `sceller_tout_v1.py`, `assembler_rapport_v1.py`, journaux des essais, sorties du banc, `empreintes-v4.json`, `empreintes-v5.json`, `comparaison-sorties-v4-v5.txt`, `diffs/`, `table-empreintes-code-v5.txt`.

## 10. Différentiels v4 → v5 (`diff -u`)

Fichiers changés ou neufs (liste de `travail/diffs/liste.txt`) ; `mutations_v4.py`, neuf, est donné en différentiel depuis `mutations_v3.py`, gardé intact. Les autres fichiers de la table v4 sont à l'octet ceux du code v4.

#### `1-mutations_v4.py.diff`

```diff
--- code-v4/outils-dev/mutations_v3.py
+++ code-v5/outils-dev/mutations_v4.py
@@ -13,8 +13,17 @@
 
 Version 3 (code v4) : les 50 défauts de la version 2, repris à l'identique (remplacements et essais), et vingt et un de plus —
 audit de présentation (nœuds 1 et 2, note D9, version 8 : treize), note D8 (trois), choix 12 (deux), dose du jeu de la garde 27
-(trois). Mode de contrôle sans essai : `python3 -B mutations_v3.py --verifier BLOC` compte chaque texte ancien dans `BLOC/src`
-(il doit s'y trouver une seule fois) et n'écrit rien."""
+(trois). Mode de contrôle sans essai : `python3 -B mutations_v4.py --verifier BLOC` compte chaque texte ancien dans `BLOC/src`
+(il doit s'y trouver une seule fois) et n'écrit rien.
+
+Version 4 (code v5, préenregistrement v11) : les 71 défauts de la version 3, dont 69 repris à l'identique (remplacements et
+essais ; « regle-calibree-etendue-aux-lois » couvre aussi, sur le code v5, le « calibrage étendu aux audits de lois » du point 6)
+et deux adaptés au code v5, leur texte ancien n'existant plus (« zone-mediane-arretee » et « seuil-calibre-a-vingt-sigma ») ; et
+des défauts neufs pour chaque règle de « Ce qui demande un code v5 » — seuil resté à 0,55 + 2 σ₀, contenu des doses resté à la lettre, signalement calibré qui arrêterait, calibrage
+étendu au contenu des audits de lois, zone médiane du contenu qui pose la mention, arrêt sur une exactitude au plus 0,55, égalité
+A = M + 2 σ₀ lue au-dessus, colonnes du seuil (NE-3), plis observés reçus de l'appelant, tirés du générateur des permutations ou
+sous le rôle « permutation », chaque condition du verrou, le manifeste, le jeu de la garde 27 (programme de lancement, trois
+sources, source précédente au lieu de suivante)."""
 
 import json
 import os
@@ -29,6 +38,8 @@
 else:
     BLOC, TRAVAIL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
     SEULS = set(sys.argv[4:])
+# version 4 : « --partie v3 » (les 71 défauts de la version 3) ou « --partie v4 » (les défauts neufs) au lieu des identifiants
+PARTIE = sorted(SEULS)[1] if len(SEULS) == 2 and "--partie" in SEULS else None
 PAQUET = os.path.join("controle_ia", "heritage_etage_processeur_v1")
 T = os.path.join(BLOC, "tests")
 
@@ -195,12 +206,13 @@
     ("regle-calibree-retiree", "nœud 2 : les audits des mondes par dose lus à la lettre (au-dessus de 0,55, arrêt)", "audit.py",
      [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n", "    if False:\n        if A <= EXACTITUDE_MAX:\n")],
      [t("mondes", "lecture_calibree")]),
-    ("zone-mediane-arretee", "nœud 2 : une exactitude des doses entre 0,55 et 0,55 + 2 σ₀ arrête", "audit.py",
-     [("        return ARRET if A > EXACTITUDE_MAX + 2.0 * sigma0 else NON_DEPARTAGEE\n", "        return ARRET\n")],
+    # (version 4 : adapté au code v5, le texte ancien de la version 3 n'existant plus ; même défaut, même essai)
+    ("zone-mediane-arretee", "nœud 2 : une exactitude des doses entre 0,55 et le seuil calibré arrête", "audit.py",
+     [("        return NON_DEPARTAGEE\n", "        return ARRET\n")],
      [t("mondes", "lecture_calibree")]),
-    ("seuil-calibre-a-vingt-sigma", "nœud 2 : seuil d'arrêt des doses à 0,55 + 20 σ₀", "audit.py",
-     [("        return ARRET if A > EXACTITUDE_MAX + 2.0 * sigma0 else NON_DEPARTAGEE\n",
-       "        return ARRET if A > EXACTITUDE_MAX + 20.0 * sigma0 else NON_DEPARTAGEE\n")], [t("mondes", "lecture_calibree")]),
+    # (version 4 : adapté au code v5 ; le seuil calibré est désormais M + 2 σ₀)
+    ("seuil-calibre-a-vingt-sigma", "nœud 2 : seuil calibré des doses à M + 20 σ₀", "audit.py",
+     [("    return moyenne + 2.0 * sigma0\n", "    return moyenne + 20.0 * sigma0\n")], [t("mondes", "lecture_calibree")]),
     ("permutation-entre-mondes", "σ₀ des doses : étiquettes permutées entre mondes, non entre suites", "audit.py",
      [("                gm.append(suite_du_monde[k])\n", "                gm.append(k)\n")], [t("mondes", "taille_reduite")]),
     ("etiquettes-non-permutees", "σ₀ des lois : étiquettes laissées en place sous « permutation »", "audit.py",
@@ -245,12 +257,164 @@
     ("jeu-de-l-etape-4-a-une-autre-dose", "garde 27 : l'étape 4 joue le jeu à la dose 0,5 et non à la constante", "etapes.py",
      [("    suites = MO.generer_jeu_avec_etrangeres(graines, bases, DOSE_JEU_GARDE_27)\n",
        "    suites = MO.generer_jeu_avec_etrangeres(graines, bases, 0.5)\n")], [t("mecanique", "garde_27_bras")]),
+    # --- version 4 (code v5) ---------------------------------------------------------------------------------------------
+    # points 1 et 6 : seuil d'arrêt, le plus grand de 0,55 et de M + 2 σ₀ ; colonnes de la table (NE-3)
+    ("seuil-reste-a-0-55-plus-2-sigma", "point 1 : le seuil calibré resté à 0,55 + 2 σ₀ (au lieu de M + 2 σ₀)", "audit.py",
+     [("    return moyenne + 2.0 * sigma0\n", "    return EXACTITUDE_MAX + 2.0 * sigma0\n")], [t("mondes", "lecture_calibree")]),
+    ("arret-sur-une-exactitude-au-plus-0-55", "point 1, version 11 : une exactitude au plus 0,55 et au-dessus de M + 2 σ₀ "
+     "arrête (ou est signalée)", "audit.py",
+     [('        if A <= EXACTITUDE_MAX:\n            return TENUE if jeu == "forme" else AU_PLUS\n',
+       '        if A <= EXACTITUDE_MAX and A <= seuil_calibre(sigma0, moyenne):\n            return TENUE if jeu == "forme" '
+       'else AU_PLUS\n')], [t("mondes", "au_plus_0_55")]),
+    ("egalite-au-seuil-calibre-lue-au-dessus", "silence n° 4 au seuil neuf : A = M + 2 σ₀ lue « au-dessus »", "audit.py",
+     [("        if A > seuil_calibre(sigma0, moyenne):\n", "        if A >= seuil_calibre(sigma0, moyenne):\n")],
+     [t("mondes", "egalite")]),
+    ("seuil-d-arret-sans-plancher", "NE-3 : la colonne du seuil d'arrêt porte M + 2 σ₀ sans le plancher de 0,55", "audit.py",
+     [("        return max(EXACTITUDE_MAX, seuil_calibre(sigma0, moyenne))\n", "        return seuil_calibre(sigma0, moyenne)\n")],
+     [t("mondes", "colonne")]),
+    ("colonne-du-seuil-calibre-a-0-55-plus-2-sigma", "point 1 : la colonne du seuil de la table porte encore 0,55 + 2 σ₀",
+     "audit.py",
+     [('                             "seuil_calibre": seuil_calibre(p["sigma0"], p["moyenne_permutee"]),\n',
+       '                             "seuil_calibre": EXACTITUDE_MAX + 2.0 * p["sigma0"],\n')], [t("mondes", "taille_reduite")]),
+    ("colonne-du-seuil-d-arret-absente", "NE-3 : la colonne du seuil d'arrêt n'est pas écrite à la table", "audit.py",
+     [('                             "seuil_d_arret": seuil_d_arret(jeu, a, p["sigma0"], p["moyenne_permutee"]),\n', "")],
+     [t("mondes", "taille_reduite")]),
+    # point 2 : règle calibrée de signalement (contenu et réunis des doses), audits de lois à la lettre
+    ("contenu-des-doses-a-la-lettre", "point 2 : contenu et réunis des doses lus à la lettre (au-dessus de 0,55, signalés)",
+     "audit.py",
+     [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n",
+       '    if audit in AUDITS_DES_DOSES and jeu == "forme":\n        if A <= EXACTITUDE_MAX:\n')],
+     [t("mondes", "lecture_calibree")]),
+    ("signalement-calibre-qui-arrete", "point 2 : un signalement calibré du contenu ou des réunis arrête", "audit.py",
+     [('            return ARRET if jeu == "forme" else SIGNALEE\n', "            return ARRET\n")],
+     [t("mondes", "lecture_calibree")]),
+    ("calibrage-etendu-au-contenu-des-lois", "point 2 : le contenu et les réunis des audits de lois lus au seuil calibré",
+     "audit.py",
+     [("        return SIGNALEE if A > EXACTITUDE_MAX else AU_PLUS\n",
+       "        return SIGNALEE if A > max(EXACTITUDE_MAX, seuil_calibre(sigma0, moyenne)) else (NON_DEPARTAGEE if A > "
+       "EXACTITUDE_MAX else AU_PLUS)\n")], [t("mondes", "lecture_calibree")]),
+    ("zone-mediane-du-contenu-mentionnee", "point 2, lecture (i) : la zone médiane du contenu ou des réunis pose la mention "
+     "(comme au code v4)", "audit.py",
+     [('            elif l == NON_DEPARTAGEE and jeu == "forme":\n', "            elif l == NON_DEPARTAGEE:\n")],
+     [t("mondes", "lecture_calibree")]),
+    # point 3 : graine des plis de la lecture observée
+    ("plis-recus-de-l-appelant", "point 3 : les plis de la lecture observée reçus de l'appelant", "mondes.py",
+     [('def juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=PERMUTATIONS_AUDIT):\n',
+       'def juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=PERMUTATIONS_AUDIT, rng_plis=None):\n'),
+      ("    rng_plis, rng_permutation = generateurs_de_l_audit(graines, couche)\n",
+       "    rng_plis, rng_permutation = ((rng_plis, generateurs_de_l_audit(graines, couche)[1]) if rng_plis is not None\n"
+       "                                 else generateurs_de_l_audit(graines, couche))\n")], [t("mondes", "etape_3")]),
+    ("plis-tires-du-generateur-des-permutations", "point 3 : les plis de la lecture observée tirés du générateur des "
+     "permutations", "mondes.py",
+     [("mondes_pour_l_audit(suites), rng_plis, rng_permutation, permutations)",
+       "mondes_pour_l_audit(suites), rng_permutation, rng_permutation, permutations)")], [t("mondes", "etape_3")]),
+    ("plis-sous-le-role-permutation", "point 3 : le générateur des plis dérivé sous le rôle « permutation »", "mondes.py",
+     [('    rng_plis = graines.g(couche=couche, famille="audit", role=ROLE_PLIS)\n',
+       '    rng_plis = graines.g(couche=couche, famille="audit", role=ROLE_PERMUTATION)\n')], [t("mondes", "etape_3")]),
+    # point 4 : verrou des graines décisives, chaque condition ; manifeste ; constante de la version 6
+    ("constante-de-la-version-6-retablie", "point 4 : l'empreinte de la version 6 écrite de nouveau dans `constantes.py`",
+     "constantes.py",
+     [('VERSION = "heritage-etage-processeur-v1"\n',
+       'VERSION = "heritage-etage-processeur-v1"\n'
+       'PREENREGISTREMENT_SHA256 = "4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029"\n')],
+     [t("verrou", "constantes")]),
+    ("verrou-texte-non-scelle", "verrou : le texte présenté accepté sans son compagnon", "graines.py",
+     [("        sha_texte = verifier_scelle(self.texte)\n", "        sha_texte = _sha256_fichier(self.texte)\n")],
+     [t("verrou", "artefact")]),
+    ("verrou-piece-non-scellee", "verrou : la pièce d'autorisation acceptée sans son compagnon", "graines.py",
+     [("        sha_piece = verifier_scelle(piece)\n", "        sha_piece = _sha256_fichier(piece)\n")],
+     [t("verrou", "artefact")]),
+    ("verrou-compagnon-a-plusieurs-lignes", "verrou, « scellée » au sens du dépôt : un compagnon de plusieurs lignes accepté",
+     "graines.py", [("    if len(lignes) != 1:\n", "    if len(lignes) < 1:\n")], [t("verrou", "artefact or depot")]),
+    ("verrou-compagnon-au-mauvais-nom", "verrou, « scellée » au sens du dépôt : un compagnon au mauvais nom accepté",
+     "graines.py", [("    if m.group(2) != os.path.basename(chemin):\n", "    if False:\n")], [t("verrou", "artefact or depot")]),
+    ("verrou-piece-a-moins-de-quatre-lignes", "verrou : une pièce de moins de quatre lignes acceptée à la lecture", "graines.py",
+     [("    if len(lignes) != len(CHAMPS_DE_LA_PIECE):\n", "    if len(lignes) > len(CHAMPS_DE_LA_PIECE):\n")],
+     [t("verrou", "artefact")]),
+    ("verrou-ordre-des-champs-non-exige", "verrou : les quatre champs acceptés dans un autre ordre que celui de R-4123",
+     "graines.py", [("        if nom != CHAMPS_DE_LA_PIECE[rang]:\n", "        if False:\n")], [t("verrou", "artefact")]),
+    ("verrou-go-non-cherche-au-registre", "verrou : l'identifiant du GO non cherché dans `registres/go.md`", "graines.py",
+     [("        if not go_inscrit(self.racine, go):\n", "        if False:\n")], [t("verrou", "artefact")]),
+    ("verrou-go-hors-de-la-premiere-colonne", "verrou : l'identifiant du GO lu n'importe où dans une ligne du registre",
+     "graines.py",
+     [('            if ligne.startswith("|") and len(cellules) > 2 and cellules[1].strip() == identifiant:\n',
+       "            if identifiant in ligne:\n")], [t("verrou", "artefact")]),
+    ("verrou-forme-du-go-non-lue", "verrou : un identifiant de GO mal formé accepté", "graines.py",
+     [("        if not _IDENTIFIANT_DU_GO.match(go):\n", "        if False:\n")], [t("verrou", "artefact")]),
+    ("verrou-commit-non-compare", "verrou : le commit de la pièce non comparé à celui du texte", "graines.py",
+     [("        if commit != commit_du_texte:\n", "        if False:\n")], [t("verrou", "artefact")]),
+    ("verrou-deux-lignes-de-commit", "verrou : un texte à deux lignes « Commit du code d'analyse » accepté (la première lue)",
+     "graines.py", [("    if len(rangs) != 1:\n", "    if not rangs:\n")], [t("verrou", "artefact")]),
+    ("verrou-empreinte-du-texte-non-comparee", "verrou : l'empreinte du texte de la pièce non comparée au texte présenté",
+     "graines.py", [("        if empreinte != sha_texte:\n", "        if False:\n")], [t("verrou", "artefact")]),
+    ("verrou-heure-non-lue", "verrou : l'heure de la pièce non contrôlée (UTC)", "graines.py",
+     [("        exiger_heure_utc(heure)\n", "")], [t("verrou", "artefact")]),
+    ("verrou-modules-non-controles", "verrou : les modules lancés non contrôlés contre la table du texte", "graines.py",
+     [("        verifier_modules(table)\n", "")], [t("verrou", "artefact")]),
+    ("verrou-empreinte-des-modules-non-comparee", "verrou : un module lancé d'empreinte différente de la table accepté",
+     "graines.py",
+     [("        if not os.path.isfile(lances[nom]) or _sha256_fichier(lances[nom]) != attendus[nom]:\n",
+       "        if not os.path.isfile(lances[nom]):\n")], [t("verrou", "artefact")]),
+    ("verrou-module-absent-de-la-table", "verrou : un module lancé absent de la table du texte accepté", "graines.py",
+     [("    if manquants or en_trop:\n", "    if en_trop:\n")], [t("verrou", "artefact")]),
+    ("verrou-module-non-lance-dans-la-table", "verrou : la table du texte nomme un module qui n'est pas lancé, accepté",
+     "graines.py", [("    if manquants or en_trop:\n", "    if manquants:\n")], [t("verrou", "artefact")]),
+    ("verrou-non-reverifie-au-lancement", "verrou : l'autorisation non vérifiée de nouveau avant un lancement décisif",
+     "tirages.py", [("    if couche in COUCHES_DECISIVES:\n        graines.autorisation.verifier()\n", "")],
+     [t("verrou", "verifie_de_nouveau")]),
+    ("manifeste-sans-empreintes-du-verrou", "remarque 4 (e) : le manifeste n'inscrit pas l'empreinte du texte présenté",
+     "tirages.py",
+     [('    autorisation = {"texte_sha256": None if a is None else a.sha_texte,\n', '    autorisation = {"texte_sha256": None,\n')],
+     [t("verrou", "cas_sain")]),
+    ("manifeste-champs-du-verrou-non-verifies", "remarque 4 (e) : le manifeste relu sans contrôler les empreintes du verrou",
+     "tirages.py",
+     [('    if "preenregistrement_sha256" in m or any(k not in m for k in champs) or (\n', "    if False and (\n")],
+     [t("statistique", "manifeste")]),
+    # point 5 : le jeu de la garde 27, appelé par le programme de lancement de l'étape 4 ; trois sources ; source suivante
+    ("source-precedente-servie", "garde 27 : le registre de la source précédente déposé aux bras 4a et 4b, au lieu de celui "
+     "de la suivante", "mecanique.py",
+     [("        e = premieres[(k + 1) % S]\n", "        e = premieres[(k - 1) % S]\n")], [t("etapes", "lancer_etape_4")]),
+    ("origine-du-depot-non-verifiee", "garde 27 : l'origine du registre déposé aux bras 4a et 4b non contrôlée", "mecanique.py",
+     [('    if etrangere is None or sortie_etrangere["suite"].source is not etrangere:\n', "    if etrangere is None:\n")],
+     [t("etapes", "lancer_etape_4")]),
+    ("marge-construite-face-a-la-source-precedente", "garde 27 : la marge des mondes cibles construite face à la source "
+     "précédente", "mondes.py",
+     [("        s.etrangere = sources[(k + 1) % S]  #", "        s.etrangere = sources[(k - 1) % S]  #")],
+     [t("mondes", "marge_face")]),
+    ("etrangeres-du-jeu-non-verifiees", "garde 27 : la source de construction de la marge non contrôlée à la fin du jeu",
+     "mondes.py", [('        if getattr(s, "etrangere", None) is not suites[(k + 1) % S].source:\n', "        if False:\n")],
+     [t("mondes", "marge_face")]),
+    ("jeu-a-deux-sources", "point 5 : le programme de lancement joue le jeu de la garde 27 à deux sources", "etapes.py",
+     [("P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)",
+       "P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), 2)")], [t("etapes", "lancer_etape_4")]),
+    ("jeu-joue-par-le-lecteur-heritage", "point 5 : le jeu de la garde 27 joué par le lecteur réglé pour l'héritage",
+     "etapes.py",
+     [("P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)",
+       'P.configuration("lecteur-heritage", **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)')], [t("etapes", "lancer_etape_4")]),
+    ("jeu-avant-les-bras-1-a-3", "point 5 : le jeu de la garde 27 joué avant les bras 1 à 3", "etapes.py",
+     [('    f, comptes, garde_17 = etape_4(graines, couche, os.path.join(dossier, "bras-1-a-3"), doses, proposeurs, sources,\n'
+       "                                   sous_ensemble, organisme)\n"
+       '    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
+       "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n",
+       '    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
+       "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n"
+       '    f, comptes, garde_17 = etape_4(graines, couche, os.path.join(dossier, "bras-1-a-3"), doses, proposeurs, sources,\n'
+       "                                   sous_ensemble, organisme)\n")], [t("etapes", "lancer_etape_4")]),
+    ("jeu-non-joue", "point 5 : le programme de lancement de l'étape 4 n'appelle pas le jeu de la garde 27", "etapes.py",
+     [('    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),\n'
+       "                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)\n",
+       "    jeu = None\n")], [t("etapes", "lancer_etape_4")]),
 ]
 # le défaut « strate vide » ne se voit que si la couche statistique ne lève pas non plus à l'emploi : second remplacement
 DEFAUTS[5] = (DEFAUTS[5][0], DEFAUTS[5][1], DEFAUTS[5][2], DEFAUTS[5][3], [t("mecanique", "strate_vide")])
 SECONDS = {"strate-vide-repli-regroupe": ("statistique.py", [("    if v is None:\n        raise ArretFrequences(",
                                                               "    if v is None:\n        return float(f.get(\"p_tient_non_plantee_base\") or 0.0)\n"
                                                               "        raise ArretFrequences(")])}
+DEFAUTS_DE_LA_VERSION_3 = 71
+if PARTIE is not None:
+    if PARTIE not in ("v3", "v4"):
+        raise SystemExit(f"partie inconnue : {PARTIE!r}")
+    SEULS = {d[0] for d in (DEFAUTS[:DEFAUTS_DE_LA_VERSION_3] if PARTIE == "v3" else DEFAUTS[DEFAUTS_DE_LA_VERSION_3:])}
 
 
 def env_pour(src):
```

#### `2-audit.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/audit.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/audit.py
@@ -25,6 +25,23 @@
   au-dessus de 0,55 ;
 - arrêt (`ArretAudit`) sur un pli d'entraînement privé d'une classe, un centre de classe non fini ou une exactitude qui ne peut
   être calculée (moins de cinq exemples d'une classe), à la lecture observée comme sous permutation (note D9 ; version 8).
+
+Code v5 (préenregistrement v11 ; « Ce qui demande un code v5 », points 1, 2 et 6 ; GO-2026-11-20-25 et GO-2026-11-20-41 ;
+décision de la mère R-4182, lecture (i) ; NE-3 retenu, R-4210) :
+- le seuil calibré est M + 2 σ₀, M étant la moyenne des mêmes exactitudes permutées (à la place de 0,55 + 2 σ₀) ; il est rapporté
+  pour les quinze exactitudes (colonne `seuil_calibre`) ;
+- forme des trois audits des mondes par dose : le seuil d'arrêt est le plus grand de 0,55 et de M + 2 σ₀ ; au plus 0,55, tenue
+  (jamais un arrêt, même au-dessus de M + 2 σ₀) ; au-dessus de 0,55 et de M + 2 σ₀, arrêt ; au-dessus de 0,55 et au plus
+  M + 2 σ₀, « non départagée du hasard à cette taille », qui lie l'étage payant (mention) ;
+- contenu et réunis des trois audits des mondes par dose : règle calibrée de signalement, jamais un arrêt ; au-dessus de 0,55 et
+  de M + 2 σ₀, signalée, avec la mention ; au plus 0,55, ni signalement ni mention ; au-dessus de 0,55 et au plus M + 2 σ₀,
+  « non départagée du hasard à cette taille », ni signalement ni mention (`non_departagees_sans_mention`) ;
+- les deux audits de lois restent à la lettre (forme : au-dessus de 0,55, arrêt ; contenu et réunis : au-dessus de 0,55,
+  signalés, avec la mention) ;
+- « au plus » est inclusif, « au-dessus de » strict (une exactitude égale à M + 2 σ₀ est au plus M + 2 σ₀) ;
+- NE-3 : une colonne de plus, `seuil_d_arret`, porte le seuil d'arrêt : le plus grand de 0,55 et de M + 2 σ₀ pour la forme des
+  audits des mondes par dose, 0,55 pour la forme des audits de lois, aucun (None) pour le contenu et les réunis, qui n'arrêtent
+  jamais (silence déclaré au rapport du code v5).
 """
 
 import hashlib
@@ -326,53 +343,83 @@
     return {"sigma0": float(vals.std(ddof=1)), "moyenne_permutee": float(vals.mean())}
 
 
-def lecture(jeu, audit, A, sigma0):
-    """La lecture d'une exactitude (section « Seuil » ; GO-2026-11-20-11). Forme, audits de lois : lettre de la version 6
-    (au-dessus de 0,55, arrêt). Forme, audits des mondes par dose : règle calibrée (au plus 0,55, tenue ; au-dessus de
-    0,55 + 2 σ₀, arrêt ; entre les deux, non départagée du hasard à cette taille). Contenu et réunis : rapportées ; au-dessus de
-    0,55, signalées (elles lient l'étage payant)."""
+def seuil_calibre(sigma0, moyenne):
+    """Code v5 (section « Seuil », version 9, GO-2026-11-20-25, point (1)) : M + 2 σ₀, M et σ₀ étant la moyenne et l'écart-type
+    des mêmes exactitudes permutées. Rapporté pour les quinze exactitudes."""
+    return moyenne + 2.0 * sigma0
+
+
+def seuil_d_arret(jeu, audit, sigma0, moyenne):
+    """Code v5 (NE-3, contrôle de la version 11, retenu par la mère, R-4210) : le seuil d'arrêt d'une exactitude. Forme des
+    audits des mondes par dose : le plus grand de 0,55 et de M + 2 σ₀ (version 11, GO-2026-11-20-41) ; forme des audits de lois :
+    0,55 (lettre de la version 6) ; contenu et réunis : None, aucune de leurs lectures n'arrête."""
     if jeu not in JEUX_DE_TRAITS or audit not in AUDITS:
-        raise AuditRefuse(f"lecture : exactitude inconnue {jeu}/{audit}")
+        raise AuditRefuse(f"seuil d'arrêt : exactitude inconnue {jeu}/{audit}")
     if jeu != "forme":
-        return SIGNALEE if A > EXACTITUDE_MAX else AU_PLUS
+        return None
+    if audit in AUDITS_DES_DOSES:
+        return max(EXACTITUDE_MAX, seuil_calibre(sigma0, moyenne))
+    return EXACTITUDE_MAX
+
+
+def lecture(jeu, audit, A, sigma0, moyenne):
+    """La lecture d'une exactitude (section « Seuil », version 11). Audits des mondes par dose (règle calibrée, M + 2 σ₀) : au
+    plus 0,55, tenue (forme) ou « au plus 0,55 » (contenu et réunis), même au-dessus de M + 2 σ₀ — une exactitude au plus 0,55
+    n'arrête jamais et n'est jamais signalée ; au-dessus de 0,55 et de M + 2 σ₀, arrêt (forme) ou signalée (contenu et réunis,
+    jamais un arrêt) ; au-dessus de 0,55 et au plus M + 2 σ₀, « non départagée du hasard à cette taille ». Audits de lois, à la
+    lettre : forme, au-dessus de 0,55, arrêt ; contenu et réunis, au-dessus de 0,55, signalées."""
+    if jeu not in JEUX_DE_TRAITS or audit not in AUDITS:
+        raise AuditRefuse(f"lecture : exactitude inconnue {jeu}/{audit}")
     if audit in AUDITS_DES_DOSES:
         if A <= EXACTITUDE_MAX:
-            return TENUE
-        return ARRET if A > EXACTITUDE_MAX + 2.0 * sigma0 else NON_DEPARTAGEE
+            return TENUE if jeu == "forme" else AU_PLUS
+        if A > seuil_calibre(sigma0, moyenne):
+            return ARRET if jeu == "forme" else SIGNALEE
+        return NON_DEPARTAGEE
+    if jeu != "forme":
+        return SIGNALEE if A > EXACTITUDE_MAX else AU_PLUS
     return ARRET if A > EXACTITUDE_MAX else TENUE
 
 
 def lire_audit(table):
-    """`table` : {jeu : {audit : {"A", "sigma0", …}}} pour les quinze exactitudes, exactement. Rend la lecture de chacune, la
-    liste des arrêts (forme), celle des exactitudes de forme non départagées (audits des doses), celle des exactitudes de
-    contenu ou réunies au-dessus de 0,55, et la mention qui lie l'étage payant."""
+    """`table` : {jeu : {audit : {"A", "sigma0", "moyenne_permutee", …}}} pour les quinze exactitudes, exactement. Rend la
+    lecture de chacune, la liste des arrêts (forme), celle des exactitudes de forme non départagées (audits des doses ; elles
+    lient l'étage payant), celle des exactitudes de contenu ou réunies non départagées (audits des doses ; ni signalement ni
+    mention, code v5), celle des exactitudes signalées, et la mention qui lie l'étage payant (posée par un signalement ou par
+    une exactitude de forme non départagée, jamais par une exactitude de contenu ou réunie non départagée)."""
     if sorted(table) != sorted(JEUX_DE_TRAITS) or any(sorted(table[j]) != sorted(AUDITS) for j in JEUX_DE_TRAITS):
         raise AuditRefuse("lecture : les quinze exactitudes sont exigées, et elles seules")
-    lectures, arret, non_departagees, signalement = {}, [], [], []
+    lectures, arret, non_departagees, sans_mention, signalement = {}, [], [], [], []
     for jeu in JEUX_DE_TRAITS:
         lectures[jeu] = {}
         for audit in AUDITS:
             e = table[jeu][audit]
-            l = lecture(jeu, audit, e["A"], e["sigma0"])
+            if any(k not in e for k in ("A", "sigma0", "moyenne_permutee")):
+                raise AuditRefuse(f"lecture : A, σ₀ et la moyenne permutée sont exigés ({jeu}/{audit})")
+            l = lecture(jeu, audit, e["A"], e["sigma0"], e["moyenne_permutee"])
             lectures[jeu][audit] = l
             nom = f"{jeu}/{audit}"
             if l == ARRET:
                 arret.append(nom)
-            elif l == NON_DEPARTAGEE:
+            elif l == NON_DEPARTAGEE and jeu == "forme":
                 non_departagees.append(nom)
+            elif l == NON_DEPARTAGEE:
+                sans_mention.append(nom)
             elif l == SIGNALEE:
                 signalement.append(nom)
     return {"lectures": lectures, "arret": sorted(arret), "non_departagees": sorted(non_departagees),
-            "signalement": sorted(signalement), "mention": MENTION if (signalement or non_departagees) else None}
+            "non_departagees_sans_mention": sorted(sans_mention), "signalement": sorted(signalement),
+            "mention": MENTION if (signalement or non_departagees) else None}
 
 
 def audit_presentation(mondes_audites, rng, rng_permutation, permutations=PERMUTATIONS_AUDIT):
     """`mondes_audites` : liste de dicts {"dose", "suite", "lois": [(texte canonique, loi, type, dependante)], "Z", "G"} — les
     mondes cibles et finaux des suites de la couche « audit », chacun avec l'identifiant de sa suite. `rng` tire les plis de la
     lecture observée (même ordre et même flux qu'au code v3) ; `rng_permutation` (couche « audit », rôle « permutation ») tire
-    les permutations et leurs plis. Rend les quinze exactitudes observées (`exactitudes`), la table (A, σ₀, moyenne permutée,
-    seuil 0,55 + 2 σ₀, lecture) des quinze, et la lecture (`arret`, `non_departagees`, `signalement`, `mention`). Arrête
-    (`ArretAudit`) sur un pli privé d'une classe, un centre non fini ou une exactitude non calculable."""
+    les permutations et leurs plis. Rend les quinze exactitudes observées (`exactitudes`), la table (A, σ₀, moyenne permutée M,
+    seuil calibré M + 2 σ₀, seuil d'arrêt, lecture ; code v5) des quinze, et la lecture (`arret`, `non_departagees`,
+    `non_departagees_sans_mention`, `signalement`, `mention`). Arrête (`ArretAudit`) sur un pli privé d'une classe, un centre
+    non fini ou une exactitude non calculable."""
     lignes = []  # (dose, monde, type, dependante, forme, contenu)
     suite_du_monde, dose_de_la_suite = [], {}
     for k, m in enumerate(mondes_audites):
@@ -416,7 +463,9 @@
             Xa, ya, ga = donnees[(jeu, a)]
             p = sous_permutation(Xa, ya, rng_permutation, permutations, ga)
             table[jeu][a] = {"A": exactitudes[jeu][a], "sigma0": p["sigma0"], "moyenne_permutee": p["moyenne_permutee"],
-                             "seuil_calibre": EXACTITUDE_MAX + 2.0 * p["sigma0"], "permutations": permutations,
+                             "seuil_calibre": seuil_calibre(p["sigma0"], p["moyenne_permutee"]),
+                             "seuil_d_arret": seuil_d_arret(jeu, a, p["sigma0"], p["moyenne_permutee"]),
+                             "permutations": permutations,
                              "permutation": "entre lois" if ga is None else "entre suites",
                              "unites_permutees": len(ya) if ga is None else len(set(ga))}
     lu = lire_audit(table)
@@ -424,4 +473,5 @@
         for a in AUDITS:
             table[jeu][a]["lecture"] = lu["lectures"][jeu][a]
     return {"exactitudes": exactitudes, "table": table, "arret": lu["arret"], "non_departagees": lu["non_departagees"],
-            "signalement": lu["signalement"], "mention": lu["mention"]}
+            "non_departagees_sans_mention": lu["non_departagees_sans_mention"], "signalement": lu["signalement"],
+            "mention": lu["mention"]}
```

#### `3-constantes.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/constantes.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/constantes.py
@@ -1,11 +1,26 @@
-"""Valeurs gelées de l'étage sur processeur du palier 0b de l'héritage (préenregistrement v6, `4aee136b…`).
+"""Valeurs gelées de l'étage sur processeur du palier 0b de l'héritage (préenregistrement v11 ; code v5).
 
 Chaque valeur renvoie à la section du texte qui la fixe. Les valeurs marquées « SILENCE » ne sont pas écrites dans le texte ; elles
 sont déclarées au rapport du développeur (section « Silences comblés »), avec leur raison.
+
+Code v5 (B8, note D6 ; « Ce qui demande un code v5 », point 4 ; silence n° 13 du code v4) : aucune empreinte du texte n'est
+écrite dans le code, puisque le texte porte les empreintes du code ; la constante qui portait l'empreinte de la version 6 est
+retirée. Le verrou des graines décisives lit la pièce d'autorisation du verrou au chemin ci-dessous (module `graines`).
 """
 
 VERSION = "heritage-etage-processeur-v1"
-PREENREGISTREMENT_SHA256 = "4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029"
+
+# B8, version 9 (décision de la mère R-4123) et remarque 4 de l'annexe H, « Version 9 », tranchée par la mère (version 10,
+# décision R-4182) : la pièce d'autorisation du verrou, relative à la racine de l'arbre lancé ; ses quatre lignes « nom : valeur »,
+# dans l'ordre de la décision R-4123 (noms : SILENCE, fixés par le développeur du code v5, contrôle de la version 10, § 6, n° 5) ;
+# le registre des GO de l'arbre lancé, dont la première colonne doit porter l'identifiant du GO
+CHEMIN_PIECE_D_AUTORISATION = "prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md"
+CHAMPS_DE_LA_PIECE = ("identifiant du GO", "commit du code", "empreinte du texte scellé", "heure")
+CHEMIN_REGISTRE_DES_GO = "registres/go.md"
+# l'en-tête du texte : la ligne qui porte le commit du code et, dans le premier bloc de code qui la suit, la table des empreintes
+# (chemins relatifs au dossier du code) ; SILENCE de forme, à inscrire par l'erratum du commit
+LIGNE_DU_COMMIT = "- Commit du code d'analyse : "
+PREFIXE_DES_MODULES = "src/"
 
 # B8 — racine gelée des graines
 RACINE_GRAINES = 2026111902
@@ -70,6 +85,10 @@
 # B7 bis et garde 27 (version 7, annexe H, écart 1 ; GO-2026-11-20-11, dose (a)) — code v4 : le jeu de sources de la garde 27
 # se construit et se joue à cette dose, et à elle seule (étape 4, `etapes.etape_4_jeu_de_la_garde_27`)
 DOSE_JEU_GARDE_27 = 0.25
+# code v5 (version 10, annexe H, « Version 9 », remarque 3, tranchée par la mère) : le programme de lancement de l'étape 4
+# (`etapes.lancer_etape_4`) joue ce jeu après les bras 1 à 3, avec le lecteur réglé pour la tenue (τ = 2, B2) et trois sources
+PROPOSEUR_JEU_GARDE_27 = "lecteur-tenue"
+SOURCES_JEU_GARDE_27 = 3
 CASES_DE_FORME = 64
 INSTANCES_ORACLE = 4000
 SEUIL_APPARIEMENT_NAT = 0.05
```

#### `4-etapes.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/etapes.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/etapes.py
@@ -6,7 +6,10 @@
   fréquences M12, l'accord avec l'étage de l'organisme sur deux sources par dose et par proposeur, S8 (i). Bras 1 à 3 seuls.
 - `etape_4_jeu_de_la_garde_27` (code v4) : à l'étape 4 aussi, le jeu de sources de la garde 27 (B7 bis : bras 1 à 3, puis 4a et
   4b sur les copies scellées de la source étrangère), à la dose `DOSE_JEU_GARDE_27` (0,25) et à elle seule ; le proposeur et le
-  nombre de sources, que le texte ne dit pas, sont des paramètres sans défaut.
+  nombre de sources sont des paramètres sans défaut de cette fonction.
+- `lancer_etape_4` (code v5, préenregistrement v11, « Ce qui demande un code v5 », point 5) : le programme de lancement de
+  l'étape 4 ; il joue `etape_4`, puis, dans le même lancement, le jeu de la garde 27 avec le lecteur réglé pour la tenue (τ = 2)
+  et trois sources (remarque 3 de l'annexe H, « Version 9 », tranchée par la mère, version 10).
 - `etape_6_bis_et_7` : la couche mécanique rejouée aux réglages gelés sous des étiquettes disjointes, puis la garde S8 (ii).
 - `etape_8` : les tirages décisifs de toutes les cases, en un seul lancement, aucune case lue avant que toutes soient
   écrites et scellées ; `cases_a_confirmer` et `etape_9` : la règle de C1 et de C4.
@@ -25,8 +28,9 @@
 from . import mondes as MO
 from . import proposeurs as P
 from .constantes import (DOSE_JEU_GARDE_27, DOSES, DOSES_NON_NULLES, FORCES_GENERALISTE, FORCES_SUIVEUR, FORCE_REFERENCE_SUIVEUR,
-                         GRILLE_SOURCES, GRILLE_SOURCES_DOSE_NULLE, REGLAGES_ETAPE_4, REPERES_LECTURE, SEUIL_DE_RETRAIT_SUR_10000,
-                         SOURCES_COUCHE_MECANIQUE, SOURCES_FAMILLES_GRANDES, SOURCES_SOUS_ENSEMBLE_ORGANISME, TAILLES,
+                         GRILLE_SOURCES, GRILLE_SOURCES_DOSE_NULLE, PROPOSEUR_JEU_GARDE_27, REGLAGES_ETAPE_4, REPERES_LECTURE,
+                         SEUIL_DE_RETRAIT_SUR_10000, SOURCES_COUCHE_MECANIQUE, SOURCES_FAMILLES_GRANDES, SOURCES_JEU_GARDE_27,
+                         SOURCES_SOUS_ENSEMBLE_ORGANISME, TAILLES,
                          TAILLE_REFERENCE, TAUX_ECHEC_DECISIF, TAUX_ECHEC_TOUS, TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE)
 from .statistique import simuler
 
@@ -177,7 +181,8 @@
     4, sur la couche mécanique, par cette fonction : `mondes.generer_jeu_avec_etrangeres` (marge face à la source étrangère
     construite) puis `mecanique.jouer_jeu_diagnostic` (bras 1, 2, 3, puis 4a et 4b), à la dose `DOSE_JEU_GARDE_27` = 0,25,
     fixée ici et vérifiée par les deux fonctions, qui arrêtent à toute autre dose ; taux d'échec de 0,25. `prop` (configuration
-    du proposeur) et `sources` (au moins deux) : le texte ne les dit pas ; ils sont donnés par l'appelant, sans défaut. Les
+    du proposeur) et `sources` (au moins deux) : donnés par l'appelant, sans défaut ; le programme de lancement de l'étape 4
+    (`lancer_etape_4`, code v5) les fixe au lecteur réglé pour la tenue, τ = 2, et à trois sources (version 10). Les
     contrôles de la garde 27 (registre servi au bras 4a, copie servie au bras 4b, aucun bras du critère ne la reçoit) se font
     en jouant. Rend {"dose", "sources", "proposeur", "suites", "premieres", "secondes"}."""
     if isinstance(sources, bool) or not isinstance(sources, int) or sources < 2:
@@ -190,6 +195,21 @@
             "secondes": secondes}
 
 
+def lancer_etape_4(graines, couche, dossier, doses=DOSES, proposeurs=PROPOSEURS_DE_L_ETAPE_4, sources=SOURCES_COUCHE_MECANIQUE,
+                   sous_ensemble=SOURCES_SOUS_ENSEMBLE_ORGANISME, organisme=None):
+    """Code v5 (« Ce qui demande un code v5 », point 5 ; B7 bis et garde 27, version 10, remarque 3 tranchée par la mère) : le
+    programme de lancement de l'étape 4. Dans un même lancement (mêmes `graines`, même `couche`) : d'abord `etape_4` (la couche
+    mécanique, bras 1 à 3), puis le jeu de la garde 27 (`etape_4_jeu_de_la_garde_27`), joué par le lecteur réglé pour la tenue,
+    au réglage de l'étape 4 que B2 gèle (τ = 2, `REGLAGES_ETAPE_4`), sur trois sources (`SOURCES_JEU_GARDE_27`), à la dose
+    0,25. Le proposeur et le nombre de sources du jeu ne sont pas des paramètres. Rend {"frequences", "comptes", "garde_17",
+    "jeu_de_la_garde_27"}."""
+    f, comptes, garde_17 = etape_4(graines, couche, os.path.join(dossier, "bras-1-a-3"), doses, proposeurs, sources,
+                                   sous_ensemble, organisme)
+    jeu = etape_4_jeu_de_la_garde_27(graines, couche, os.path.join(dossier, "jeu-de-la-garde-27"),
+                                     P.configuration(PROPOSEUR_JEU_GARDE_27, **REGLAGES_ETAPE_4), SOURCES_JEU_GARDE_27)
+    return {"frequences": f, "comptes": comptes, "garde_17": garde_17, "jeu_de_la_garde_27": jeu}
+
+
 def etape_6_bis_et_7(graines, couche, dossier, f, configurations, sources_mecaniques=SOURCES_COUCHE_MECANIQUE,
                      sources_statistiques=20_000, bras=("1", "2", "3")):
     """`configurations` : {(proposeur, dose) : configuration aux réglages gelés}. Rejoue la couche mécanique (étiquettes
```

#### `5-graines.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/graines.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/graines.py
@@ -5,17 +5,36 @@
 
 Couches disjointes (B8) : « etalonnage », « mecanique » (étape 4), « mecanique-reglages » (étape 6 bis), « audit » (étape 3),
 « essai-de-forme », « essai » (essais du code), « decisif », « confirmation ». Les deux dernières ne se dérivent **jamais sans
-autorisation** : un objet `Autorisation` qui nomme le préenregistrement scellé et l'erratum contre-lu qui inscrit le commit du
-code, vérifiés sur disque par empreinte (liste d'arrêt, point 1). Aucune autorisation n'est construite dans ce travail ; l'essai
-final (`test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`) contrôle le journal du processus.
+autorisation** (liste d'arrêt, point 1). L'essai final (`test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py`)
+contrôle le journal du processus.
+
+Code v5 (préenregistrement v11, B8, versions 7, 9 et 10 ; note D6 ; décisions de la mère R-4123 et R-4182, remarque 4 de
+l'annexe H, « Version 9 », points (a) à (e) ; « Ce qui demande un code v5 », point 4) : le verrou est un objet `Autorisation`,
+construit sur le texte présenté et la racine de l'arbre lancé, qui ne s'obtient que si :
+- le texte présenté est scellé (son compagnon) ;
+- la pièce d'autorisation du verrou existe à `CHEMIN_PIECE_D_AUTORISATION` sous la racine de l'arbre lancé et est scellée ;
+  « scellée » s'entend au sens de `controle_ia.scellement.verifier` (un compagnon d'une ligne, au bon nom, dont l'empreinte est
+  égale), réécrit ici (`verifier_scelle`) parce que ce paquet se lance seul ;
+- la pièce porte quatre lignes « nom : valeur », dans l'ordre de la décision R-4123 (`CHAMPS_DE_LA_PIECE`), et son contenu égale
+  les valeurs attendues : l'identifiant du GO figure dans la première colonne d'une ligne de `registres/go.md` de l'arbre lancé ;
+  le commit du code est celui que le texte inscrit en tête (« Commit du code d'analyse ») ; l'empreinte du texte est celle du
+  texte présenté, recalculée ; l'heure est en UTC (forme seule) ;
+- chaque module du code lancé (les fichiers `.py` de ce paquet et le `__init__.py` du paquet parent) a l'empreinte que la table
+  de l'en-tête du texte lui donne, et la table ne nomme aucun module qui ne soit lancé.
+Aucune empreinte du texte n'est écrite dans le code. Le manifeste inscrit l'empreinte du texte présenté, celle de la pièce et
+l'heure (module `tirages`). Les essais n'éprouvent le verrou que sur des arbres factices, dans un dossier temporaire, et ne
+dérivent aucune graine décisive.
 """
 
+import datetime
 import hashlib
 import os
+import re
 
 import numpy as np
 
-from .constantes import RACINE_GRAINES
+from .constantes import (CHAMPS_DE_LA_PIECE, CHEMIN_PIECE_D_AUTORISATION, CHEMIN_REGISTRE_DES_GO, LIGNE_DU_COMMIT,
+                         PREFIXE_DES_MODULES, RACINE_GRAINES)
 
 COUCHES = ("etalonnage", "mecanique", "mecanique-reglages", "audit", "essai-de-forme", "essai", "decisif", "confirmation")
 COUCHES_DECISIVES = ("decisif", "confirmation")
@@ -82,25 +101,175 @@
     return h.hexdigest()
 
 
+# --- verrou des graines décisives (code v5) -------------------------------------------------------------------------------------
+
+_LIGNE_COMPAGNON = re.compile(r"^([0-9a-f]{64})  (\S.*)$")  # celle de `controle_ia.scellement`
+_LIGNE_DE_TABLE = re.compile(r"^([0-9a-f]{64})  (\S.*)$")
+_COMMIT = re.compile(r"`([0-9a-f]{40})`")
+_IDENTIFIANT_DU_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2,}$")
+# SILENCE de forme (remarque 4, point (b) : « l'heure est contrôlée dans sa forme seule (UTC) ») : la sortie de `date -u` dans
+# la locale C, ou la forme ISO 8601 terminée par Z
+FORMES_DE_L_HEURE = ("%a %b %d %H:%M:%S UTC %Y", "%Y-%m-%dT%H:%M:%SZ")
+
+
+def _refus(message):
+    return GraineRefusee(f"autorisation refusée : {message} (B8 ; liste d'arrêt, point 1)")
+
+
+def verifier_scelle(chemin):
+    """« Scellée » au sens de `controle_ia.scellement.verifier` (remarque 4, point (a)) : le fichier existe, son compagnon
+    `.sha256` existe, porte une seule ligne non vide « <empreinte>  <nom de base> » au bon nom, et l'empreinte recalculée du
+    fichier lui est égale. Rend l'empreinte ; refus sinon."""
+    if not os.path.isfile(chemin):
+        raise _refus(f"{chemin} absent sur disque")
+    compagnon = chemin + ".sha256"
+    if not os.path.isfile(compagnon):
+        raise _refus(f"{chemin} non scellé (compagnon absent)")
+    with open(compagnon, encoding="utf-8") as f:
+        lignes = [l for l in f.read().splitlines() if l.strip()]
+    if len(lignes) != 1:
+        raise _refus(f"{compagnon} : une seule ligne attendue, {len(lignes)} trouvées")
+    m = _LIGNE_COMPAGNON.match(lignes[0])
+    if not m:
+        raise _refus(f"{compagnon} : ligne illisible")
+    if m.group(2) != os.path.basename(chemin):
+        raise _refus(f"{compagnon} : nom {m.group(2)!r} au lieu de {os.path.basename(chemin)!r}")
+    obtenue = _sha256_fichier(chemin)
+    if obtenue != m.group(1):
+        raise _refus(f"{chemin} : empreinte différente de son compagnon")
+    return obtenue
+
+
+def lire_en_tete_du_texte(chemin_texte):
+    """L'en-tête du texte présenté : le commit du code (le premier `<40 chiffres hexadécimaux>` entre accents graves de la seule
+    ligne qui commence par `LIGNE_DU_COMMIT`) et la table des empreintes (les lignes « <empreinte>  <chemin> » du premier bloc
+    de code qui suit cette ligne, entre deux lignes « ``` »). Rend (commit, {chemin : empreinte}) ; refus sinon."""
+    with open(chemin_texte, encoding="utf-8") as f:
+        lignes = f.read().split("\n")
+    rangs = [i for i, l in enumerate(lignes) if l.startswith(LIGNE_DU_COMMIT)]
+    if len(rangs) != 1:
+        raise _refus(f"le texte porte {len(rangs)} ligne(s) « {LIGNE_DU_COMMIT.strip()} » au lieu d'une")
+    commits = _COMMIT.findall(lignes[rangs[0]])
+    if not commits:
+        raise _refus("aucun commit du code dans la ligne « Commit du code d'analyse » du texte")
+    i = rangs[0] + 1
+    while i < len(lignes) and lignes[i].strip() != "```":
+        i += 1
+    j = i + 1
+    table = {}
+    while j < len(lignes) and lignes[j].strip() != "```":
+        ligne = lignes[j].strip()
+        if ligne:
+            m = _LIGNE_DE_TABLE.match(ligne)
+            if not m or m.group(2) in table:
+                raise _refus(f"table des empreintes du texte illisible ou à chemin double : {ligne!r}")
+            table[m.group(2)] = m.group(1)
+        j += 1
+    if j >= len(lignes) or not table:
+        raise _refus("table des empreintes du texte absente ou non fermée")
+    return commits[0], table
+
+
+def modules_lances():
+    """Les modules du code lancé : les fichiers `.py` de ce paquet et le `__init__.py` du paquet parent, sous les chemins
+    relatifs de la table du texte (`src/controle_ia/heritage_etage_processeur_v1/…`). Rend {chemin de la table : chemin sur
+    disque}."""
+    paquet = os.path.dirname(os.path.abspath(__file__))
+    parent = os.path.dirname(paquet)
+    prefixe = f"{PREFIXE_DES_MODULES}{os.path.basename(parent)}/"
+    out = {f"{prefixe}{os.path.basename(paquet)}/{f}": os.path.join(paquet, f) for f in sorted(os.listdir(paquet))
+           if f.endswith(".py") and os.path.isfile(os.path.join(paquet, f))}
+    out[f"{prefixe}__init__.py"] = os.path.join(parent, "__init__.py")
+    return out
+
+
+def verifier_modules(table):
+    """Chaque module du code lancé a l'empreinte que la table du texte lui donne ; la table ne nomme aucun module (chemin sous
+    `src/`) qui ne soit lancé. Refus sinon."""
+    lances = modules_lances()
+    attendus = {k: v for k, v in table.items() if k.startswith(PREFIXE_DES_MODULES)}
+    manquants, en_trop = sorted(set(lances) - set(attendus)), sorted(set(attendus) - set(lances))
+    if manquants or en_trop:
+        raise _refus(f"modules lancés et table du texte différents : absents de la table {manquants}, non lancés {en_trop}")
+    for nom in sorted(set(lances) & set(attendus)):
+        if not os.path.isfile(lances[nom]) or _sha256_fichier(lances[nom]) != attendus[nom]:
+            raise _refus(f"le module lancé {nom} n'a pas l'empreinte que la table du texte lui donne")
+    return True
+
+
+def lire_piece(chemin_piece):
+    """Les quatre lignes « nom : valeur » de la pièce, dans l'ordre de `CHAMPS_DE_LA_PIECE` (un saut de ligne final permis).
+    Rend {nom : valeur} ; refus sinon."""
+    with open(chemin_piece, encoding="utf-8") as f:
+        lignes = f.read().split("\n")
+    if lignes and lignes[-1] == "":
+        lignes = lignes[:-1]
+    if len(lignes) != len(CHAMPS_DE_LA_PIECE):
+        raise _refus(f"la pièce d'autorisation porte {len(lignes)} ligne(s) au lieu de {len(CHAMPS_DE_LA_PIECE)}")
+    valeurs = {}
+    for rang, ligne in enumerate(lignes):
+        nom, separateur, v = ligne.partition(" : ")
+        if not separateur or nom not in CHAMPS_DE_LA_PIECE or nom in valeurs:
+            raise _refus(f"ligne de la pièce d'autorisation hors de la forme « nom : valeur » : {ligne!r}")
+        if nom != CHAMPS_DE_LA_PIECE[rang]:
+            raise _refus(f"la pièce d'autorisation porte « {nom} » au rang {rang + 1} (ordre de la décision R-4123)")
+        if not v or v != v.strip():
+            raise _refus(f"valeur vide ou entourée de blancs : « {nom} »")
+        valeurs[nom] = v
+    return valeurs
+
+
+def go_inscrit(racine, identifiant):
+    """L'identifiant du GO figure dans la première colonne d'une ligne du registre des GO de l'arbre lancé."""
+    chemin = os.path.join(racine, CHEMIN_REGISTRE_DES_GO)
+    if not os.path.isfile(chemin):
+        raise _refus(f"registre des GO absent de l'arbre lancé : {chemin}")
+    with open(chemin, encoding="utf-8") as f:
+        for ligne in f.read().split("\n"):
+            cellules = ligne.split("|")
+            if ligne.startswith("|") and len(cellules) > 2 and cellules[1].strip() == identifiant:
+                return True
+    return False
+
+
+def exiger_heure_utc(heure):
+    for forme in FORMES_DE_L_HEURE:
+        try:
+            datetime.datetime.strptime(heure, forme)
+            return True
+        except ValueError:
+            continue
+    raise _refus(f"heure hors des formes UTC admises : {heure!r}")
+
+
 class Autorisation:
-    """Autorisation de dériver une graine décisive : préenregistrement scellé et erratum contre-lu, chacun vérifié par
-    empreinte sur disque et par son compagnon `.sha256`, l'erratum devant citer l'empreinte du préenregistrement. Jamais
-    construite dans ce travail."""
-
-    def __init__(self, preenregistrement, sha_preenregistrement, erratum, sha_erratum):
-        for chemin, sha in ((preenregistrement, sha_preenregistrement), (erratum, sha_erratum)):
-            if not os.path.isfile(chemin) or _sha256_fichier(chemin) != sha:
-                raise GraineRefusee(f"autorisation refusée : {chemin} absent ou d'empreinte différente")
-            compagnon = chemin + ".sha256"
-            if not os.path.isfile(compagnon):
-                raise GraineRefusee(f"autorisation refusée : {chemin} non scellé (compagnon absent)")
-            with open(compagnon, encoding="ascii") as f:
-                if (f.read().split() or [""])[0] != sha:
-                    raise GraineRefusee(f"autorisation refusée : {chemin} non scellé (compagnon faux)")
-        with open(erratum, encoding="utf-8") as f:
-            if sha_preenregistrement not in f.read():
-                raise GraineRefusee("autorisation refusée : l'erratum ne cite pas l'empreinte du préenregistrement")
-        self.sha_preenregistrement, self.sha_erratum = sha_preenregistrement, sha_erratum
+    """Le verrou des graines décisives (code v5 ; voir l'en-tête du module). `texte` : le texte présenté ; `racine` : la racine
+    de l'arbre lancé, qui porte la pièce d'autorisation et `registres/go.md`. Tout est vérifié à la construction, et de nouveau
+    par `verifier` avant chaque lancement d'une couche décisive (module `tirages`)."""
+
+    def __init__(self, texte, racine):
+        self.texte, self.racine = os.path.abspath(texte), os.path.abspath(racine)
+        self.verifier()
+
+    def verifier(self):
+        sha_texte = verifier_scelle(self.texte)
+        commit_du_texte, table = lire_en_tete_du_texte(self.texte)
+        piece = os.path.join(self.racine, CHEMIN_PIECE_D_AUTORISATION)
+        sha_piece = verifier_scelle(piece)
+        valeurs = lire_piece(piece)
+        go, commit, empreinte, heure = (valeurs[c] for c in CHAMPS_DE_LA_PIECE)
+        if not _IDENTIFIANT_DU_GO.match(go):
+            raise _refus(f"identifiant du GO mal formé : {go!r}")
+        if not go_inscrit(self.racine, go):
+            raise _refus(f"{go} ne figure dans la première colonne d'aucune ligne de {CHEMIN_REGISTRE_DES_GO}")
+        if commit != commit_du_texte:
+            raise _refus("le commit du code de la pièce n'est pas celui que le texte inscrit en tête")
+        if empreinte != sha_texte:
+            raise _refus("l'empreinte du texte de la pièce n'est pas celle du texte présenté")
+        exiger_heure_utc(heure)
+        verifier_modules(table)
+        self.sha_texte, self.sha_piece, self.go, self.commit, self.heure = sha_texte, sha_piece, go, commit, heure
+        return True
 
 
 class Graines:
@@ -121,8 +290,9 @@
             raise GraineRefusee(f"couche inconnue : {couche!r}")
         if couche in COUCHES_DECISIVES and self.autorisation is None:
             REFUS.append(texte_etiquette)
-            raise GraineRefusee(f"graine de la couche « {couche} » refusée : aucune autorisation (préenregistrement scellé et "
-                                "erratum contre-lu exigés ; liste d'arrêt, point 1)")
+            raise GraineRefusee(f"graine de la couche « {couche} » refusée : aucune autorisation (texte scellé, pièce "
+                                "d'autorisation du verrou et modules conformes à la table du texte exigés ; liste d'arrêt, "
+                                "point 1)")
         JOURNAL.append((couche, texte_etiquette))
         self.etiquettes.append(texte_etiquette)
         return np.random.SeedSequence(self.racine, spawn_key=cle_de_derivation(texte_etiquette))
```

#### `6-mecanique.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/mecanique.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/mecanique.py
@@ -5,6 +5,10 @@
 cible, loi fausse, loi non plantée par origine — ; criblage par composition et par monde) et les moyennes de la garde
 d'équivalence S8. `jouer_source` joue une source entière : course source (trois générations du monde source, registre né vide
 servi et payé comme au bras 2, aucune entrée héritée), puis chaque bras demandé sur trois mondes cibles et le monde final.
+
+Code v5 (préenregistrement v11, « Ce qui demande un code v5 », point 5 ; garde 27 à trois sources) : au jeu à sources
+étrangères, ce qui est déposé aux bras 4a et 4b d'une source est contrôlé contre la source face à laquelle la marge de ses
+mondes cibles a été construite (`verifier_source_etrangere`) : un registre de la source précédente arrête.
 """
 
 import os
@@ -322,10 +326,24 @@
     return sortie
 
 
+def verifier_source_etrangere(sortie_etrangere, suite):
+    """Garde 27 (B7 bis ; version 10, remarque 3 : trois sources ; code v5) : ce que l'orchestrateur dépose aux bras 4a et 4b
+    d'une source (le registre de la course et la copie du bras 2 de `sortie_etrangere`) vient de la source face à laquelle la
+    marge des mondes cibles de `suite` a été construite (`suite.etrangere`, la source suivante, la première pour la dernière) ;
+    sinon arrêt. Avec deux sources, la source suivante et la source précédente se confondent ; avec trois, une inversion de sens
+    entre la construction de la marge et le registre servi arrête ici."""
+    etrangere = getattr(suite, "etrangere", None)
+    if etrangere is None or sortie_etrangere["suite"].source is not etrangere:
+        raise ArretMecanique("garde 27 : le registre déposé aux bras 4a et 4b n'est pas celui de la source face à laquelle la "
+                             "marge a été construite (source précédente au lieu de la suivante ?) : arrêt")
+    return True
+
+
 def jouer_jeu_diagnostic(graines, bases, prop, dose, taux, dossier, suites, **kw):
     """B7 bis, garde 27 : un jeu de sources à sources étrangères (`mondes.generer_jeu_avec_etrangeres`) ; chaque source joue
     d'abord ses bras 1, 2, 3 (pour que son registre de course source et les vues de son bras 2 existent), puis les bras 4a et 4b
-    reçoivent les copies scellées de la source suivante. Rend la liste des sorties par source. Code v4 (version 7, annexe H,
+    reçoivent les copies scellées de la source suivante, après contrôle de leur origine (`verifier_source_etrangere`, code v5).
+    Rend la liste des sorties par source. Code v4 (version 7, annexe H,
     écart 1) : ce jeu ne se joue qu'à la dose 0,25 (`DOSE_JEU_GARDE_27`) ; toute autre dose arrête avant de jouer."""
     if float(dose) != DOSE_JEU_GARDE_27:
         raise ArretMecanique(f"garde 27 : le jeu de sources à sources étrangères ne se joue qu'à la dose {DOSE_JEU_GARDE_27} "
@@ -338,6 +356,7 @@
     secondes = []
     for k in range(S):
         e = premieres[(k + 1) % S]
+        verifier_source_etrangere(e, suites[k])
         ctx = ContexteSource(graines, bases[k], prop, dose, taux, os.path.join(dossier, f"source-{k}-diagnostic"), **kw)
         secondes.append(jouer_source(ctx, ("4a", "4b"), suite=suites[k], registre_etranger=e["registre_source"],
                                      copie_etrangere_4b=copie_scellee_4b(e)))
```

#### `7-mondes.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/mondes.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/mondes.py
@@ -22,6 +22,12 @@
 
 L'audit (module `audit`, écriture à part) juge le produit fini à 0,25 nat ; un monde qui manque une marge par une loi autre
 qu'une dépendante est rejeté et retiré ; un monde cible que seules ses lois dépendantes font échouer fait retirer la suite.
+
+Code v5 (préenregistrement v11) : à l'étape 3, les plis de la lecture observée sont tirés par un générateur que le code de
+l'étape dérive lui-même (couche « audit », famille « audit », rôle « plis »), distinct de celui des permutations (rôle
+« permutation ») ; l'appelant n'en donne aucun (« Ce qui demande un code v5 », point 3). Au jeu à sources étrangères (garde 27),
+chaque suite garde la source face à laquelle la marge de ses mondes cibles est construite (`etrangere`), et la construction
+arrête si ce n'est pas la source suivante (point 5 ; trois sources, version 10).
 """
 
 import itertools
@@ -39,6 +45,10 @@
 
 PAIRES_DE_LA_SOURCE = list(itertools.combinations(range(DOMAINES_A_LOI_SOURCE), 2))  # 28 paires de rangs
 SORTES = ("sous-loi-source", "independante", "fausse-source", "fausse-cible")
+# rôles d'étiquette des deux générateurs de l'audit de présentation (section « Seuil », version 9 ; code v5, point 3) ; le nom
+# du rôle « plis » est une valeur du rédacteur
+ROLE_PLIS = "plis"
+ROLE_PERMUTATION = "permutation"
 
 
 class ArretGenerateur(RuntimeError):
@@ -426,11 +436,12 @@
         s = Suite()
         s.compteurs = cumul[k]
         s.source = sources[k]
+        s.etrangere = sources[(k + 1) % S]  # code v5 : la source face à laquelle la marge est construite, gardée avec la suite
         paires = tirer_paires(graines.g(**b, monde="paires", role="paires"), dose)
         ok = True
         for j in range(MONDES_CIBLES_D_EVOLUTION + 1):
             nom = "finale" if j == MONDES_CIBLES_D_EVOLUTION else f"cible-{j + 1}"
-            m, _, _ = generer_cible(graines, b, s.source, nom, paires[j], dose, bornes, s.compteurs, sources[(k + 1) % S])
+            m, _, _ = generer_cible(graines, b, s.source, nom, paires[j], dose, bornes, s.compteurs, s.etrangere)
             if m is None:
                 ok = False
                 break
@@ -449,11 +460,22 @@
         if precedente != k and precedente not in a_faire:
             suites[precedente] = None
             a_faire.append(precedente)
-    for k, s in enumerate(suites):
-        s.etrangere = suites[(k + 1) % S].source
+    verifier_etrangeres_du_jeu(suites)
     return suites
 
 
+def verifier_etrangeres_du_jeu(suites):
+    """Garde 27 (code v5 ; B7 bis : la source étrangère de la source k est la source k + 1, la première pour la dernière) : la
+    source face à laquelle la marge des mondes cibles de chaque suite a été construite (`etrangere`) est la source de la suite
+    suivante ; sinon arrêt."""
+    S = len(suites)
+    for k, s in enumerate(suites):
+        if getattr(s, "etrangere", None) is not suites[(k + 1) % S].source:
+            raise ArretGenerateur(f"garde 27 : la marge des mondes cibles de la source {k} n'est pas construite face à la source "
+                                  "suivante (B7 bis) : arrêt")
+    return True
+
+
 def ensemble_exclu(finale, lois_du_registre_de_la_source, seuil=SEUIL_APPARIEMENT_NAT):
     """§ 6 du plan et M1 : toute loi plantée du monde final que le comparateur apparie (≤ 0,05 nat, de la loi plantée vers la loi
     de la tentative) à une tentative du registre de la source, lue sans égard au domaine (version 4, plus strict)."""
@@ -558,14 +580,28 @@
     return suites, compteurs
 
 
-def juger_suites_d_audit(suites, compteurs, rng_audit, rng_permutation, permutations=PERMUTATIONS_AUDIT):
+def generateurs_de_l_audit(graines, couche="audit"):
+    """Code v5 (« Ce qui demande un code v5 », point 3 ; section « Seuil », version 9 ; B8) : les deux générateurs de l'audit de
+    présentation, dérivés par le code de l'étape 3 et non reçus de l'appelant — celui des plis de la lecture observée (couche
+    `couche`, famille « audit », rôle « plis » ; un seul pour les quinze exactitudes) et celui des permutations (même couche et
+    famille, rôle « permutation »). Rend (plis, permutation)."""
+    rng_plis = graines.g(couche=couche, famille="audit", role=ROLE_PLIS)
+    rng_permutation = graines.g(couche=couche, famille="audit", role=ROLE_PERMUTATION)
+    return rng_plis, rng_permutation
+
+
+def juger_suites_d_audit(suites, compteurs, graines, couche="audit", permutations=PERMUTATIONS_AUDIT):
     """Étape 3, jugement : ensemble exclu par construction, audit de présentation (quinze exactitudes, chacune avec σ₀, la
-    moyenne des exactitudes permutées et le seuil 0,55 + 2 σ₀ ; code v4), rejets et taux d'acceptation, distribution des traits
-    de contenu. Rend le rapport ; lève `ArretGenerateur` (liste d'arrêt, point 2), le rapport joint à l'exception quand il
-    existe (`rapport`), si une exactitude de forme d'un audit de lois dépasse 0,55, si une exactitude de forme d'un audit des
-    mondes par dose dépasse 0,55 + 2 σ₀, si une loi du monde final est celle de sa source, ou si l'audit de présentation arrête
-    (pli privé d'une classe, centre non fini, exactitude non calculable). Une exactitude de forme des doses entre 0,55 et
-    0,55 + 2 σ₀ n'arrête pas : elle est rapportée « non départagée du hasard à cette taille » et lie l'étage payant."""
+    moyenne permutée M, le seuil calibré M + 2 σ₀ et le seuil d'arrêt ; code v5), rejets et taux d'acceptation, distribution des
+    traits de contenu. Code v5 : les plis de la lecture observée et les permutations sont tirés par les générateurs que
+    `generateurs_de_l_audit` dérive ici de `graines` (couche `couche`), et non reçus de l'appelant. Rend le rapport ; lève
+    `ArretGenerateur` (liste d'arrêt, point 2), le rapport joint à l'exception quand il existe (`rapport`), si une exactitude de
+    forme d'un audit de lois dépasse 0,55, si une exactitude de forme d'un audit des mondes par dose dépasse le plus grand de
+    0,55 et de M + 2 σ₀, si une loi du monde final est celle de sa source, ou si l'audit de présentation arrête (pli privé d'une
+    classe, centre non fini, exactitude non calculable). Une exactitude de forme des doses au-dessus de 0,55 et au plus
+    M + 2 σ₀ n'arrête pas : elle est rapportée « non départagée du hasard à cette taille » et lie l'étage payant ; une
+    exactitude au plus 0,55 n'arrête jamais."""
+    rng_plis, rng_permutation = generateurs_de_l_audit(graines, couche)
     communs = {}
     for s in suites:
         c = AU.ensemble_exclu_par_construction([l["texte"] for l in s.finale.lois.values()],
@@ -573,7 +609,7 @@
         if c:
             communs[s.source.nom] = c
     try:
-        pres = AU.audit_presentation(mondes_pour_l_audit(suites), rng_audit, rng_permutation, permutations)
+        pres = AU.audit_presentation(mondes_pour_l_audit(suites), rng_plis, rng_permutation, permutations)
     except AU.ArretAudit as e:
         raise ArretGenerateur(f"audit du générateur en échec : {e}") from e
     rapport = {"presentation": pres, "lois_du_final_identiques_a_la_source": communs, "compteurs": compteurs.vers_dict(),
@@ -585,13 +621,10 @@
     return rapport
 
 
-def audit_du_generateur(graines, doses, suites_par_dose, rng_audit, rng_permutation=None, permutations=PERMUTATIONS_AUDIT,
-                        couche="audit"):
+def audit_du_generateur(graines, doses, suites_par_dose, permutations=PERMUTATIONS_AUDIT, couche="audit"):
     """Étape 3 : `suites_par_dose` suites par dose sous la couche « audit » ; marges rejugées sur chaque monde (déjà faites à la
-    construction par le module `audit`), puis `juger_suites_d_audit`. `rng_permutation` : par défaut la graine de la couche
-    `couche`, famille « audit », rôle « permutation » (section « Seuil », version 7). Rend un rapport ; lève `ArretGenerateur`
-    (liste d'arrêt, point 2)."""
+    construction par le module `audit`), puis `juger_suites_d_audit`, qui dérive les générateurs des plis observés (rôle
+    « plis ») et des permutations (rôle « permutation ») de la couche `couche`, famille « audit » (code v5 : aucun générateur
+    n'est reçu de l'appelant). Rend un rapport ; lève `ArretGenerateur` (liste d'arrêt, point 2)."""
     suites, compteurs = generer_suites_d_audit(graines, doses, suites_par_dose, couche)
-    if rng_permutation is None:
-        rng_permutation = graines.g(couche=couche, famille="audit", role="permutation")
-    return juger_suites_d_audit(suites, compteurs, rng_audit, rng_permutation, permutations)
+    return juger_suites_d_audit(suites, compteurs, graines, couche, permutations)
```

#### `8-tirages.py.diff`

```diff
--- code-v4/src/controle_ia/heritage_etage_processeur_v1/tirages.py
+++ code-v5/src/controle_ia/heritage_etage_processeur_v1/tirages.py
@@ -24,7 +24,7 @@
 from . import rangs_signes as RS
 from .constantes import (ESSAI_DE_FORME_MAX_NOMBRES_DE_SOURCES, ESSAI_DE_FORME_MAX_TIRAGES, GRILLE_SOURCES,
                          GRILLE_SOURCES_DOSE_NULLE, LOT_DE_SOURCES, MAX_SOURCES, MAX_SOURCES_DOSE_NULLE, NOMBRES_M13_EN_PLUS,
-                         PREENREGISTREMENT_SHA256, RACINE_GRAINES, REPERE_LECTURE, VERSION)
+                         RACINE_GRAINES, REPERE_LECTURE, VERSION)
 from .graines import COUCHES_DECISIVES
 from .statistique import simuler
 
@@ -227,7 +227,14 @@
     liste triée, couches), commit, empreintes des fichiers gelés (fréquences M12, réglages). Code v4 (B8, version 7, choix 12) :
     la liste entière des étiquettes, triée, une par ligne, jointes par un saut de ligne sans saut final (le texte même dont le
     manifeste porte l'empreinte), est écrite dans un fichier scellé à côté du manifeste, avant lui ; le manifeste inscrit son nom
-    et son empreinte, égale à celle de la liste (elle se rejoue à la main par `sha256sum`)."""
+    et son empreinte, égale à celle de la liste (elle se rejoue à la main par `sha256sum`). Code v5 (remarque 4, point (e) ;
+    point (b) pour l'heure) : à la place de l'empreinte de la version 6, le manifeste inscrit l'empreinte du texte présenté, celle
+    de la pièce d'autorisation du verrou et l'heure qu'elle porte, prises de l'autorisation des graines ; sans autorisation
+    (couches non décisives), ces trois champs valent null."""
+    a = graines.autorisation
+    autorisation = {"texte_sha256": None if a is None else a.sha_texte,
+                    "piece_d_autorisation_sha256": None if a is None else a.sha_piece,
+                    "heure_d_autorisation": None if a is None else a.heure}
     canon = json.dumps(configuration, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
     etiq = sorted(graines.etiquettes)
     texte_liste = "\n".join(etiq).encode("utf-8")
@@ -235,7 +242,7 @@
     with open(chemin_liste, "xb") as fh:
         fh.write(texte_liste)
     sha_liste = _sceller(chemin_liste)
-    m = {"version": VERSION, "preenregistrement_sha256": PREENREGISTREMENT_SHA256, "configuration": configuration,
+    m = {"version": VERSION, **autorisation, "configuration": configuration,
          "configuration_sha256": hashlib.sha256(canon.encode("utf-8")).hexdigest(),
          "versions": {"python": platform.python_version(), "numpy": np.__version__},
          "racine": graines.racine if graines.racine is not None else RACINE_GRAINES, "commit": commit,
@@ -266,6 +273,11 @@
     nombre d'étiquettes ; arrêt sinon."""
     octets, _ = _lire_scelle(chemin)
     m = json.loads(octets.decode("utf-8"))
+    champs = ("texte_sha256", "piece_d_autorisation_sha256", "heure_d_autorisation")
+    if "preenregistrement_sha256" in m or any(k not in m for k in champs) or (
+            len({m[k] is None for k in champs}) != 1):
+        raise ArretTirages("manifeste : empreintes du texte et de la pièce d'autorisation, et heure, non inscrites ensemble "
+                           "(code v5, remarque 4, point (e))")
     e = m.get("etiquettes") or {}
     chemin_liste = os.path.join(os.path.dirname(chemin), e.get("fichier") or "")
     if not e.get("fichier") or chemin_liste != chemin_de_la_liste_des_etiquettes(chemin):
@@ -280,11 +292,15 @@
 
 
 def exiger_autorisation_pour(couche, graines):
-    """Liste d'arrêt, point 1 : aucun tirage décisif ni de confirmation sans autorisation (vérifiée avant toute simulation)."""
+    """Liste d'arrêt, point 1 : aucun tirage décisif ni de confirmation sans autorisation (vérifiée avant toute simulation).
+    Code v5 : l'autorisation est vérifiée de nouveau ici, sur disque, avant le lancement (texte, pièce, registre des GO,
+    modules)."""
     if couche in COUCHES_DECISIVES and graines.autorisation is None:
         from .graines import GraineRefusee, REFUS
         REFUS.append(f"couche={couche}|lancement")
         raise GraineRefusee(f"lancement de la couche « {couche} » refusé : aucune autorisation (liste d'arrêt, point 1)")
+    if couche in COUCHES_DECISIVES:
+        graines.autorisation.verifier()
     return True
 
 
```

#### `9-test_heritage_etage_processeur_v1_etapes.py.diff`

```diff
--- code-v4/tests/test_heritage_etage_processeur_v1_etapes.py
+++ code-v5/tests/test_heritage_etage_processeur_v1_etapes.py
@@ -1,6 +1,7 @@
 """Essais de l'enchaînement (ordre des opérations) : le plan des cases de B8 (72 cases pour C1 et pour C4 ; une cible non
 atteignable est écrite et ne se tire pas) ; l'étape 4 réduite à une source sous la couche « essai », sans l'organisme (garde 17
-alors non jouée, dit) ; la règle des cases à confirmer sur des comptes plantés."""
+alors non jouée, dit) ; la règle des cases à confirmer sur des comptes plantés. Code v5 : le programme de lancement de l'étape 4,
+qui joue le jeu de la garde 27 après les bras 1 à 3, avec le lecteur réglé pour la tenue (τ = 2) et trois sources."""
 
 import pytest
 
@@ -50,6 +51,50 @@
                                           "p_tient_non_plantee_base", "p_tient_non_plantee_composition", "p_tient_non_plantee_copie"))
 
 
+def test_lancer_etape_4_bras_1_a_3_puis_jeu_de_la_garde_27_a_trois_sources(tmp_path):
+    """Code v5 (« Ce qui demande un code v5 », point 5 ; B7 bis et garde 27, version 10, remarque 3 tranchée par la mère) : le
+    programme de lancement de l'étape 4 joue d'abord la couche mécanique (bras 1 à 3 ; réduite ici à une source et deux
+    proposeurs), puis, dans le même lancement (mêmes graines, même couche), le jeu de la garde 27 : lecteur réglé pour la tenue
+    au réglage de l'étape 4 (τ = 2), trois sources, dose 0,25. Chaque source reçoit aux bras 4a et 4b le registre et les vues de
+    la source suivante, face à laquelle la marge de ses mondes a été construite ; artefact : le registre de la source
+    précédente, déposé pour la source k, arrête (à trois sources, la précédente n'est pas la suivante)."""
+    from aides_heritage_etage_processeur_v1 import prop
+    from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
+    from controle_ia.heritage_etage_processeur_v1.constantes import (PROPOSEUR_JEU_GARDE_27, REGLAGES_ETAPE_4,
+                                                                    SOURCES_JEU_GARDE_27)
+    assert PROPOSEUR_JEU_GARDE_27 == "lecteur-tenue" and SOURCES_JEU_GARDE_27 == 3 and REGLAGES_ETAPE_4["tau"] == 2.0
+    g = graines()
+    out = EP.lancer_etape_4(g, "essai", str(tmp_path), doses=(0.5,), proposeurs=("lecteur-heritage", "copieur"), sources=1,
+                            sous_ensemble=0)
+    assert out["garde_17"] is None and out["frequences"]["p_tient_vraie_source"] is not None
+    jeu = out["jeu_de_la_garde_27"]
+    assert jeu["dose"] == 0.25 and jeu["sources"] == 3 and jeu["proposeur"] == "lecteur-tenue"
+    # même lancement, dans l'ordre : toutes les étiquettes de la couche mécanique avant celles du jeu, même couche
+    familles = [e.split("|")[1] for e in g.etiquettes]
+    assert familles[0] == "famille=etape-4" and familles[-1] == "famille=etape-4-garde-27"
+    k = familles.index("famille=etape-4-garde-27")
+    assert set(familles[:k]) == {"famille=etape-4"} and set(familles[k:]) == {"famille=etape-4-garde-27"}
+    assert all(e.startswith("couche=essai|") for e in g.etiquettes)
+    assert all("proposeur=lecteur-tenue" in e for e in g.etiquettes[k:])
+    # le proposeur du jeu : le lecteur réglé pour la tenue, τ = 2 (configuration de l'étape 4)
+    assert prop("lecteur-tenue", **REGLAGES_ETAPE_4) == prop("lecteur-tenue", tau=2.0)
+    suites, premieres, secondes = jeu["suites"], jeu["premieres"], jeu["secondes"]
+    assert len(suites) == len(premieres) == len(secondes) == 3
+    for k in range(3):
+        suivante, precedente = premieres[(k + 1) % 3], premieres[(k - 1) % 3]
+        assert suites[k].etrangere is suites[(k + 1) % 3].source
+        r4a = secondes[k]["bras"]["4a"]["registre"]
+        n = len(suivante["registre_source"].entrees)
+        assert r4a.entrees[:n] == suivante["registre_source"].entrees
+        assert r4a.entrees[:len(precedente["registre_source"].entrees)] != precedente["registre_source"].entrees
+        assert secondes[k]["bras"]["4b"]["entrees_servies"] == [len(v) for v in suivante["vues_bras_2"]]
+        assert MC.verifier_source_etrangere(suivante, suites[k])
+        with pytest.raises(MC.ArretMecanique, match="garde 27 : le registre déposé"):
+            MC.verifier_source_etrangere(precedente, suites[k])
+        with pytest.raises(MC.ArretMecanique, match="garde 27 : le registre déposé"):
+            MC.verifier_source_etrangere(premieres[k], suites[k])
+
+
 def test_etape_6_reduite_reglages_geles_et_plan(tmp_path):
     """L'étape 6 réduite (2 000 sources, couche « essai » : un essai du code, non un étalonnage) : réglages gelés avec leur
     compagnon, aucune lecture (garde 22), et le plan des cases construit sur eux."""
```

#### `10-test_heritage_etage_processeur_v1_mondes.py.diff`

```diff
--- code-v4/tests/test_heritage_etage_processeur_v1_mondes.py
+++ code-v5/tests/test_heritage_etage_processeur_v1_mondes.py
@@ -8,7 +8,13 @@
 de la version 6 pour les deux audits de lois (nœud 2) ; artefacts de la garde 25 : valeurs plantées dans la zone médiane
 (mention sans arrêt), exactitude de forme plantée à 0,56 dans un audit de lois (arrêt), signes des lois dépendantes changés
 (vus par le contenu, non par la forme), pli privé d'une classe et exactitude non calculable (arrêt) ; étape 3. Les essais
-jouent peu de permutations (`PERMUTATIONS_D_ESSAI`) ; la valeur gelée, 1 000, est celle de l'étape 3."""
+jouent peu de permutations (`PERMUTATIONS_D_ESSAI`) ; la valeur gelée, 1 000, est celle de l'étape 3.
+
+Code v5 (préenregistrement v11, « Ce qui demande un code v5 », points 1, 2, 3 et 6 ; NE-3) : seuil calibré M + 2 σ₀ ; seuil
+d'arrêt de la forme des doses au plus grand de 0,55 et de M + 2 σ₀ (une exactitude au plus 0,55 n'arrête jamais) ; règle
+calibrée de signalement pour le contenu et les réunis des doses (zone médiane : ni signalement ni mention) ; audits de lois à la
+lettre ; égalité A = M + 2 σ₀ lue « au plus » ; colonne du seuil d'arrêt ; plis de la lecture observée dérivés par l'étape 3
+sous le rôle « plis », distincts des permutations. Valeurs plantées, non tirées, pour la garde 25."""
 
 import itertools
 
@@ -89,34 +95,56 @@
     return out
 
 
+def _attendu(j, a, A, s, M):
+    """La lecture de la section « Seuil » (version 11), écrite à part du code : audits des doses, au plus 0,55 jamais un arrêt
+    ni un signalement ; au-dessus de 0,55 et de M + 2 σ₀, arrêt (forme) ou signalement (contenu, réunis) ; entre les deux, non
+    départagée. Audits de lois à la lettre."""
+    if a.startswith("mondes_dose"):
+        if A <= 0.55:
+            return AU.TENUE if j == "forme" else AU.AU_PLUS
+        if A > M + 2 * s:
+            return AU.ARRET if j == "forme" else AU.SIGNALEE
+        return AU.NON_DEPARTAGEE
+    if j != "forme":
+        return AU.SIGNALEE if A > 0.55 else AU.AU_PLUS
+    return AU.ARRET if A > 0.55 else AU.TENUE
+
+
 def _verifier_table(pres, permutations):
-    """Les quinze exactitudes portent A, σ₀, la moyenne des exactitudes permutées, le seuil 0,55 + 2 σ₀ et leur lecture, et
-    chaque lecture est celle de la règle (forme des lois à la lettre ; forme des doses calibrée ; contenu et réunis rapportés)."""
+    """Les quinze exactitudes portent A, σ₀, la moyenne permutée M, le seuil calibré M + 2 σ₀, le seuil d'arrêt (NE-3) et leur
+    lecture, et chaque lecture est celle de la règle (forme des lois à la lettre ; forme des doses calibrée, le seuil d'arrêt
+    étant le plus grand de 0,55 et de M + 2 σ₀ ; contenu et réunis des doses, règle calibrée de signalement ; contenu et réunis
+    des lois à la lettre)."""
     lignes = [(j, a, e) for j, d in pres["table"].items() for a, e in d.items()]
     assert len(lignes) == 15 and sorted(pres["table"]) == sorted(AU.JEUX_DE_TRAITS)
     for j, a, e in lignes:
         assert e["A"] == pres["exactitudes"][j][a] and e["permutations"] == permutations
-        assert e["sigma0"] > 0 and e["seuil_calibre"] == 0.55 + 2 * e["sigma0"] and 0.0 <= e["moyenne_permutee"] <= 1.0
-        assert e["permutation"] == ("entre suites" if a.startswith("mondes_dose") else "entre lois")
+        assert e["sigma0"] > 0 and 0.0 <= e["moyenne_permutee"] <= 1.0
+        assert e["seuil_calibre"] == e["moyenne_permutee"] + 2 * e["sigma0"]
         if j != "forme":
-            attendu = AU.SIGNALEE if e["A"] > 0.55 else AU.AU_PLUS
+            assert e["seuil_d_arret"] is None
         elif a.startswith("mondes_dose"):
-            attendu = (AU.TENUE if e["A"] <= 0.55 else AU.ARRET if e["A"] > e["seuil_calibre"] else AU.NON_DEPARTAGEE)
+            assert e["seuil_d_arret"] == max(0.55, e["moyenne_permutee"] + 2 * e["sigma0"])
         else:
-            attendu = AU.ARRET if e["A"] > 0.55 else AU.TENUE
+            assert e["seuil_d_arret"] == 0.55
+        assert e["permutation"] == ("entre suites" if a.startswith("mondes_dose") else "entre lois")
+        attendu = _attendu(j, a, e["A"], e["sigma0"], e["moyenne_permutee"])
         assert e["lecture"] == attendu, (j, a, e)
+        if j == "forme":
+            assert (attendu == AU.ARRET) == (e["A"] > e["seuil_d_arret"])
         assert (f"{j}/{a}" in pres["arret"]) == (attendu == AU.ARRET)
-        assert (f"{j}/{a}" in pres["non_departagees"]) == (attendu == AU.NON_DEPARTAGEE)
+        assert (f"{j}/{a}" in pres["non_departagees"]) == (attendu == AU.NON_DEPARTAGEE and j == "forme")
+        assert (f"{j}/{a}" in pres["non_departagees_sans_mention"]) == (attendu == AU.NON_DEPARTAGEE and j != "forme")
         assert (f"{j}/{a}" in pres["signalement"]) == (attendu == AU.SIGNALEE)
     assert (pres["mention"] is not None) == bool(pres["signalement"] or pres["non_departagees"])
 
 
 def test_garde_25_audit_de_presentation_cas_sain():
     """Cas sain de la garde 25 (B9 : « générateur sain : aucun arrêt »). Code v4 : aucune exactitude de forme n'arrête ni
-    n'est non départagée, et aucune des quinze ne s'écarte de la moyenne permutée de plus de trois σ₀. Les exactitudes de
-    contenu et réunies restent lues à la lettre (au-dessus de 0,55, signalées) sans calibrage : à cette taille, le seul hasard
-    peut en signaler une (vu au code v4 sur ces graines : « reunis/mondes_dose_0.25_contre_0.5 », 0,558, z = +2,4) ; ce n'est
-    pas un arrêt, et l'essai ne l'exige ni ne l'exclut (constat porté au rapport du code v4)."""
+    n'est non départagée, et aucune des quinze ne s'écarte de la moyenne permutée de plus de trois σ₀. Code v5 : les exactitudes
+    de contenu et réunies des doses sont lues selon la règle calibrée de signalement (M + 2 σ₀), celles des lois à la lettre ;
+    un signalement de contenu ou réuni n'est pas un arrêt, et l'essai ne l'exige ni ne l'exclut (constat du rapport du code v4 :
+    « reunis/mondes_dose_0.25_contre_0.5 », 0,558, z = +2,4, signalée à la lettre sur ces graines)."""
     pres = AU.audit_presentation(_mondes_sains_par_construction(300), np.random.default_rng(25), _rng_permutation(2501),
                                  PERMUTATIONS_D_ESSAI)
     assert pres["arret"] == [] and pres["non_departagees"] == [], pres["table"]
@@ -164,39 +192,111 @@
         AU.traits_de_contenu(loi, Z, G, L.json_canonique(loi) + " ")
 
 
-def _table_plantee(A=0.5, sigma0=0.02, **changes):
-    """Une table plantée des quinze exactitudes (valeurs non tirées) ; `changes` : {"jeu/audit": (A, σ₀)}."""
-    t = {j: {a: {"A": A, "sigma0": sigma0} for a in AU.AUDITS} for j in AU.JEUX_DE_TRAITS}
-    for nom, (a, s) in changes.items():
-        j, au = nom.replace("__", "/").split("/")
-        t[j][au] = {"A": a, "sigma0": s}
+def _table_plantee(A=0.5, sigma0=0.02, moyenne=0.5, **changes):
+    """Une table plantée des quinze exactitudes (valeurs non tirées) ; `changes` : {"jeu/audit": (A, σ₀, M)}."""
+    t = {j: {a: {"A": A, "sigma0": sigma0, "moyenne_permutee": moyenne} for a in AU.AUDITS} for j in AU.JEUX_DE_TRAITS}
+    for nom, (a, s, m) in changes.items():
+        j, au = nom.split("/")
+        t[j][au] = {"A": a, "sigma0": s, "moyenne_permutee": m}
     return t
 
 
+DOSE_F = "forme/mondes_dose_0.0_contre_0.5"
+DOSE_C = "contenu/mondes_dose_0.25_contre_0.5"
+DOSE_R = "reunis/mondes_dose_0.0_contre_0.25"
+
+
+def _rien(l):
+    return (l["arret"] == l["non_departagees"] == l["non_departagees_sans_mention"] == l["signalement"] == []
+            and l["mention"] is None)
+
+
 def test_garde_25_lecture_calibree_sur_valeurs_plantees():
-    """Garde 25 (versions 7 et 8), valeurs plantées, non tirées : zone médiane d'un audit des mondes par dose, mention sans
-    arrêt ; au-dessus de 0,55 + 2 σ₀, arrêt ; un audit de lois lu à la lettre (0,56 avec σ₀ = 0,01 arrête, alors que la règle
-    calibrée ne l'aurait pas fait) ; contenu au-dessus de 0,55, signalement sans arrêt ; 0,55 tout juste, tenue."""
-    l = AU.lire_audit(_table_plantee())
-    assert l["arret"] == l["non_departagees"] == l["signalement"] == [] and l["mention"] is None
-    dose = "forme/mondes_dose_0.0_contre_0.5"
-    l = AU.lire_audit(_table_plantee(**{dose: (0.58, 0.02)}))
-    assert l["arret"] == [] and l["non_departagees"] == [dose] and l["mention"] == AU.MENTION
+    """Garde 25, valeurs plantées de A, de M et de σ₀, non tirées (versions 9, 10 et 11). Forme des doses : zone médiane,
+    mention sans arrêt ; au-dessus de 0,55 et de M + 2 σ₀, arrêt ; M au-dessus de 0,55 : au-dessus de 0,55 + 2 σ₀ sans dépasser
+    M + 2 σ₀, aucun arrêt ; M sous 0,5 : au-dessus de M + 2 σ₀ et de 0,55 sans dépasser 0,55 + 2 σ₀, arrêt. Audits de lois à la
+    lettre (forme 0,56 : arrêt ; contenu 0,56 : signalement, mention), même quand M + 2 σ₀ les dirait non départagées. Contenu
+    et réunis des doses : au-dessus de 0,55 et de M + 2 σ₀, signalement et mention, jamais un arrêt ; zone médiane, ni
+    signalement ni mention, seulement les mots « non départagée du hasard à cette taille »."""
+    assert _rien(AU.lire_audit(_table_plantee()))
+    l = AU.lire_audit(_table_plantee(**{DOSE_F: (0.58, 0.02, 0.55)}))  # M + 2 σ₀ = 0,59
+    assert l["arret"] == [] and l["non_departagees"] == [DOSE_F] and l["mention"] == AU.MENTION
     assert l["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == "non départagée du hasard à cette taille"
-    assert AU.lire_audit(_table_plantee(**{dose: (0.60, 0.02)}))["arret"] == [dose]
-    assert AU.lire_audit(_table_plantee(**{dose: (0.55, 0.0)}))["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == AU.TENUE
+    assert AU.lire_audit(_table_plantee(**{DOSE_F: (0.60, 0.02, 0.5)}))["arret"] == [DOSE_F]
+    assert AU.lire_audit(_table_plantee(**{DOSE_F: (0.55, 0.0, 0.5)}))["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] \
+        == AU.TENUE
+    # version 9 : M au-dessus de 0,55 — 0,61 dépasse 0,55 + 2 σ₀ (0,59) sans dépasser M + 2 σ₀ (0,62) : aucun arrêt, mention
+    l = AU.lire_audit(_table_plantee(**{DOSE_F: (0.61, 0.02, 0.58)}))
+    assert l["arret"] == [] and l["non_departagees"] == [DOSE_F] and l["mention"] == AU.MENTION
+    # version 9 : M sous 0,5 — 0,60 dépasse M + 2 σ₀ (0,54) et 0,55 sans dépasser 0,55 + 2 σ₀ (0,63) : arrêt
+    assert AU.lire_audit(_table_plantee(**{DOSE_F: (0.60, 0.04, 0.46)}))["arret"] == [DOSE_F]
+    # audits de lois à la lettre
     for loi in ("forme/vraies_contre_fausses", "forme/dependantes_contre_independantes"):
-        l = AU.lire_audit(_table_plantee(**{loi: (0.56, 0.01)}))
-        assert l["arret"] == [loi] and l["non_departagees"] == []
-        assert AU.lecture("forme", "mondes_dose_0.25_contre_0.5", 0.56, 0.01) == AU.NON_DEPARTAGEE  # la règle des doses
-    l = AU.lire_audit(_table_plantee(**{"contenu/dependantes_contre_independantes": (0.6, 0.01),
-                                        "reunis/mondes_dose_0.0_contre_0.25": (0.9, 0.01)}))
-    assert l["arret"] == [] and l["signalement"] == ["contenu/dependantes_contre_independantes",
-                                                     "reunis/mondes_dose_0.0_contre_0.25"] and l["mention"] == AU.MENTION
+        l = AU.lire_audit(_table_plantee(**{loi: (0.56, 0.04, 0.5)}))  # M + 2 σ₀ = 0,58 : la règle calibrée ne l'arrêterait pas
+        assert l["arret"] == [loi] and l["non_departagees"] == [] and l["mention"] is None
+    for loi in ("contenu/vraies_contre_fausses", "reunis/dependantes_contre_independantes"):
+        l = AU.lire_audit(_table_plantee(**{loi: (0.56, 0.04, 0.5)}))
+        assert l["signalement"] == [loi] and l["arret"] == [] and l["non_departagees_sans_mention"] == []
+        assert l["mention"] == AU.MENTION
+    assert AU.lecture("forme", "mondes_dose_0.25_contre_0.5", 0.56, 0.04, 0.5) == AU.NON_DEPARTAGEE  # la règle des doses
+    # contenu et réunis des doses : au-dessus de 0,55 et de M + 2 σ₀, signalement et mention, jamais un arrêt
+    l = AU.lire_audit(_table_plantee(**{DOSE_C: (0.62, 0.02, 0.5), DOSE_R: (0.9, 0.01, 0.5)}))
+    assert l["arret"] == [] and l["signalement"] == sorted([DOSE_C, DOSE_R]) and l["mention"] == AU.MENTION
+    # zone médiane du contenu et des réunis (version 10, lecture (i)) : ni signalement, ni mention, ni arrêt
+    l = AU.lire_audit(_table_plantee(**{DOSE_C: (0.58, 0.03, 0.53), DOSE_R: (0.57, 0.02, 0.54)}))  # M + 2 σ₀ : 0,59 ; 0,58
+    assert l["arret"] == l["signalement"] == l["non_departagees"] == [] and l["mention"] is None
+    assert l["non_departagees_sans_mention"] == sorted([DOSE_C, DOSE_R])
+    assert l["lectures"]["contenu"]["mondes_dose_0.25_contre_0.5"] == "non départagée du hasard à cette taille"
     t = _table_plantee()
     del t["forme"]["vraies_contre_fausses"]
     with pytest.raises(AU.AuditRefuse):
         AU.lire_audit(t)
+    t = _table_plantee()
+    del t["forme"]["mondes_dose_0.0_contre_0.25"]["moyenne_permutee"]
+    with pytest.raises(AU.AuditRefuse, match="moyenne permutée"):
+        AU.lire_audit(t)
+
+
+def test_garde_25_au_plus_0_55_jamais_un_arret_ni_un_signalement():
+    """Version 11 (remarque 1 tranchée par Lazar, GO-2026-11-20-41, option (ii)) : une exactitude de forme plantée au plus 0,55
+    et au-dessus de M + 2 σ₀, M + 2 σ₀ étant planté sous 0,55, n'arrête pas : elle est tenue, sans mention ; une exactitude de
+    contenu ou réunie plantée de même n'est ni signalée ni mentionnée. Un code qui arrête sur une exactitude au plus 0,55 échoue
+    ici."""
+    for A in (0.53, 0.55):  # M + 2 σ₀ = 0,49
+        l = AU.lire_audit(_table_plantee(**{DOSE_F: (A, 0.02, 0.45), DOSE_C: (A, 0.02, 0.45), DOSE_R: (A, 0.02, 0.45)}))
+        assert _rien(l), l
+        assert l["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == AU.TENUE
+        assert l["lectures"]["contenu"]["mondes_dose_0.25_contre_0.5"] == AU.AU_PLUS
+        assert l["lectures"]["reunis"]["mondes_dose_0.0_contre_0.25"] == AU.AU_PLUS
+    assert AU.seuil_d_arret("forme", "mondes_dose_0.0_contre_0.5", 0.02, 0.45) == 0.55
+
+
+def test_garde_25_egalite_au_seuil_calibre_au_plus():
+    """Silence n° 4 au seuil neuf (version 10, contrôle de la version 9, § 7) : une exactitude égale à M + 2 σ₀ est au plus
+    M + 2 σ₀ (valeurs exactes en binaire : M = 0,5, σ₀ = 0,0625, A = 0,625). Forme : non départagée, pas un arrêt ; contenu :
+    non départagée, ni signalement ni mention ; et une exactitude égale à 0,55 est au plus 0,55."""
+    assert 0.5 + 2.0 * 0.0625 == 0.625
+    l = AU.lire_audit(_table_plantee(**{DOSE_F: (0.625, 0.0625, 0.5), DOSE_C: (0.625, 0.0625, 0.5)}))
+    assert l["arret"] == [] and l["non_departagees"] == [DOSE_F] and l["non_departagees_sans_mention"] == [DOSE_C]
+    assert l["signalement"] == []
+    assert AU.lecture("forme", "mondes_dose_0.0_contre_0.25", 0.625 + 1e-12, 0.0625, 0.5) == AU.ARRET
+    assert AU.lecture("contenu", "mondes_dose_0.0_contre_0.25", 0.625 + 1e-12, 0.0625, 0.5) == AU.SIGNALEE
+    assert AU.lecture("forme", "mondes_dose_0.0_contre_0.25", 0.55, 0.0, 0.5) == AU.TENUE
+
+
+def test_colonne_du_seuil_d_arret_ne_3():
+    """NE-3 (contrôle de la version 11, retenu par la mère, R-4210) : la colonne `seuil_d_arret` porte le plus grand de 0,55 et
+    de M + 2 σ₀ pour la forme des audits des doses ; 0,55 pour la forme des audits de lois ; rien pour le contenu et les réunis,
+    qui n'arrêtent jamais. La colonne `seuil_calibre` porte M + 2 σ₀ pour les quinze."""
+    assert AU.seuil_calibre(0.02, 0.45) == 0.45 + 2 * 0.02
+    for d in AU.AUDITS_DES_DOSES:
+        assert AU.seuil_d_arret("forme", d, 0.02, 0.45) == 0.55  # M + 2 σ₀ = 0,49 : le plancher
+        assert AU.seuil_d_arret("forme", d, 0.02, 0.58) == 0.58 + 2 * 0.02
+        assert AU.seuil_d_arret("contenu", d, 0.02, 0.58) is None and AU.seuil_d_arret("reunis", d, 0.02, 0.58) is None
+    for a in AU.AUDITS_DE_LOIS:
+        assert AU.seuil_d_arret("forme", a, 0.2, 0.58) == 0.55
+    with pytest.raises(AU.AuditRefuse):
+        AU.seuil_d_arret("forme", "inconnu", 0.02, 0.5)
 
 
 class _RngPlante:
@@ -282,12 +382,13 @@
 
 def test_garde_25_dose_inscrite_dans_la_presentation_arret():
     """Artefact : une dose inscrite dans la présentation ; l'exactitude de forme d'un audit des mondes par dose dépasse
-    0,55 + 2 σ₀ (règle calibrée, σ₀ par permutation entre suites) : arrêt."""
+    M + 2 σ₀ et 0,55 (règle calibrée, σ₀ et M par permutation entre suites ; code v5) : arrêt."""
     g = graines()
     suites = _suites(g, "audit-dose-inscrite", variante="dose-inscrite")
     pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(26), _rng_permutation(2601), 50)
     assert any(a.startswith("forme/mondes_dose") for a in pres["arret"])
-    assert any(e["A"] > e["seuil_calibre"] for k, e in pres["table"]["forme"].items() if k.startswith("mondes_dose"))
+    assert any(e["A"] > e["seuil_calibre"] and e["A"] > 0.55 and e["A"] > e["seuil_d_arret"]
+               for k, e in pres["table"]["forme"].items() if k.startswith("mondes_dose"))
     _verifier_table(pres, 50)
 
 
@@ -362,27 +463,47 @@
 
 
 def test_etape_3_jugement_des_suites_et_arrets(saines):
-    """Étape 3 (code v4), à taille réduite et sous la couche « essai » : le jugement rend le rapport (ou arrête, le rapport joint)
-    avec, pour les quinze exactitudes, A, σ₀, la moyenne permutée, le seuil et la lecture ; une exactitude non calculable
-    (suites d'une seule dose) arrête l'étape ; la fonction de l'étape joue la couche demandée et le rôle « permutation »."""
+    """Étape 3, à taille réduite et sous la couche « essai » : le jugement rend le rapport (ou arrête, le rapport joint) avec,
+    pour les quinze exactitudes, A, σ₀, la moyenne permutée, les deux seuils et la lecture ; une exactitude non calculable
+    (suites d'une seule dose) arrête l'étape. Code v5 (« Ce qui demande un code v5 », point 3) : l'étape dérive elle-même le
+    générateur des plis de la lecture observée (rôle « plis ») et celui des permutations (rôle « permutation »), de la couche
+    demandée et de la famille « audit » ; elle n'en reçoit aucun de l'appelant ; les exactitudes observées sont celles que
+    donnent ces deux générateurs, distincts (artefacts : plis reçus de l'appelant ; plis tirés du générateur des permutations)."""
+    import inspect
     c = MO.Compteurs()
     for s in saines:
         c.ajouter(s.compteurs)
+    g = graines()
     try:
-        rapport = MO.juger_suites_d_audit(saines, c, np.random.default_rng(29), _rng_permutation(2901), PERMUTATIONS_D_ESSAI)
+        rapport = MO.juger_suites_d_audit(saines, c, g, "essai", PERMUTATIONS_D_ESSAI)
         assert rapport["presentation"]["arret"] == []
     except MO.ArretGenerateur as e:
         rapport = e.rapport
         assert rapport["presentation"]["arret"] and "audit du générateur en échec" in str(e)
     _verifier_table(rapport["presentation"], PERMUTATIONS_D_ESSAI)
     assert set(rapport) == {"presentation", "lois_du_final_identiques_a_la_source", "compteurs", "traits_de_contenu"}
+    assert g.etiquettes == ["couche=essai|famille=audit|role=plis", "couche=essai|famille=audit|role=permutation"]
+    # les exactitudes observées et la table sont celles des deux générateurs dérivés sous leurs rôles, distincts
+    g2 = graines()
+    attendu = AU.audit_presentation(MO.mondes_pour_l_audit(saines), g2.g(couche="essai", famille="audit", role="plis"),
+                                    g2.g(couche="essai", famille="audit", role="permutation"), PERMUTATIONS_D_ESSAI)
+    assert rapport["presentation"]["exactitudes"] == attendu["exactitudes"]
+    assert rapport["presentation"]["table"] == attendu["table"]
+    g3 = graines()
+    rng_perm = g3.g(couche="essai", famille="audit", role="permutation")
+    meme = AU.audit_presentation(MO.mondes_pour_l_audit(saines), g3.g(couche="essai", famille="audit", role="permutation"),
+                                 rng_perm, PERMUTATIONS_D_ESSAI)
+    assert meme["exactitudes"] != rapport["presentation"]["exactitudes"]  # l'artefact se distingue
+    # aucun générateur reçu de l'appelant, à l'étape 3
+    for f in (MO.juger_suites_d_audit, MO.audit_du_generateur):
+        assert not any(p.startswith("rng") for p in inspect.signature(f).parameters), f
     with pytest.raises(MO.ArretGenerateur, match="non calculable"):
-        MO.juger_suites_d_audit([s for s in saines if s.source.dose == 0.5], c, np.random.default_rng(29),
-                                _rng_permutation(2901), PERMUTATIONS_D_ESSAI)
+        MO.juger_suites_d_audit([s for s in saines if s.source.dose == 0.5], c, graines(), "essai", PERMUTATIONS_D_ESSAI)
     g = graines()
     with pytest.raises(MO.ArretGenerateur, match="non calculable"):
-        MO.audit_du_generateur(g, (0.0,), 1, np.random.default_rng(30), permutations=PERMUTATIONS_D_ESSAI, couche="essai")
+        MO.audit_du_generateur(g, (0.0,), 1, permutations=PERMUTATIONS_D_ESSAI, couche="essai")
     assert "couche=essai|famille=audit|role=permutation" in g.etiquettes
+    assert "couche=essai|famille=audit|role=plis" in g.etiquettes
 
 
 def test_marge_face_a_la_source_etrangere():
@@ -397,6 +518,15 @@
         for m in s.mondes_cibles():
             assert AU.audit_marges({i: l["loi"] for i, l in m.lois.items()}, m.oracle.Z, m.oracle.G,
                                    s.source.vraies_par_rang(), e.vraies_par_rang()) == []
+    # code v5 (garde 27 à trois sources) : la source de construction de la marge est la suivante ; artefact planté, la
+    # précédente (à trois sources, elle diffère de la suivante)
+    import copy
+    assert MO.verifier_etrangeres_du_jeu(suites)
+    inversees = [copy.copy(s) for s in suites]
+    for k, s in enumerate(inversees):
+        s.etrangere = suites[(k - 1) % 3].source
+    with pytest.raises(MO.ArretGenerateur, match="garde 27 : la marge"):
+        MO.verifier_etrangeres_du_jeu(inversees)
     # sans la construction de B7 bis, la marge face à une source étrangère n'est pas garantie : l'audit la lit
     s0 = MO.generer_suite(g, dict(couche="essai", famille="sans-etrangere", source=0), 0.5)
     lois = {i: l["loi"] for i, l in s0.cibles[0].lois.items()}
```

#### `11-test_heritage_etage_processeur_v1_outils.py.diff`

```diff
--- code-v4/tests/test_heritage_etage_processeur_v1_outils.py
+++ code-v5/tests/test_heritage_etage_processeur_v1_outils.py
@@ -265,12 +265,12 @@
         GR.etiquette(couche="essai", inconnu=1)
     with pytest.raises(GR.GraineRefusee):
         GR.etiquette(couche="essai", famille="a|b")
-    # une autorisation ne se construit pas sur un texte non scellé
+    # une autorisation ne se construit pas sur un texte non scellé (code v5 : texte présenté et racine de l'arbre lancé ; le
+    # verrou entier est éprouvé dans `test_heritage_etage_processeur_v1_verrou.py`)
     faux = tmp_path / "prereg.md"
     faux.write_text("brouillon", encoding="utf-8")
-    sha = hashlib.sha256(b"brouillon").hexdigest()
-    with pytest.raises(GR.GraineRefusee):
-        GR.Autorisation(str(faux), sha, str(faux), sha)
+    with pytest.raises(GR.GraineRefusee, match="autorisation refusée"):
+        GR.Autorisation(str(faux), str(tmp_path))
 
 
 def test_garde_20_graines_des_bras():
```

#### `12-test_heritage_etage_processeur_v1_statistique.py.diff`

```diff
--- code-v4/tests/test_heritage_etage_processeur_v1_statistique.py
+++ code-v5/tests/test_heritage_etage_processeur_v1_statistique.py
@@ -166,6 +166,27 @@
     liste.write_bytes(octets + b"\n")
     with pytest.raises(TI.ArretTirages, match="compagnon"):
         TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json"))
+    # code v5 (remarque 4, point (e)) : l'empreinte de la version 6 n'est plus inscrite ; sans autorisation (couche non
+    # décisive), l'empreinte du texte présenté, celle de la pièce et l'heure valent null, ensemble (le cas avec autorisation est
+    # éprouvé dans `test_heritage_etage_processeur_v1_verrou.py`)
+    assert "preenregistrement_sha256" not in m
+    assert m["texte_sha256"] is None and m["piece_d_autorisation_sha256"] is None and m["heure_d_autorisation"] is None
+    # artefacts : un manifeste où l'un des trois champs manque, ou où un seul est inscrit, ou qui porte encore l'empreinte de
+    # la version 6 (compagnon refait chaque fois ; le contrôle précède celui de la liste des étiquettes) : arrêt
+    chemin_m = tmp_path / "run" / "manifeste.json"
+    for alteration in ({"heure_d_autorisation": "supprimer"}, {"texte_sha256": "a" * 64},
+                       {"preenregistrement_sha256": "b" * 64}):
+        m2 = dict(m)
+        for k, v in alteration.items():
+            if v == "supprimer":
+                del m2[k]
+            else:
+                m2[k] = v
+        chemin_m.write_text(json.dumps(m2, ensure_ascii=False, sort_keys=True, indent=1) + "\n", encoding="utf-8")
+        (tmp_path / "run" / "manifeste.json.sha256").write_text(
+            f"{hashlib.sha256(chemin_m.read_bytes()).hexdigest()}  manifeste.json\n", encoding="ascii")
+        with pytest.raises(TI.ArretTirages, match="pièce d'autorisation"):
+            TI.verifier_manifeste(str(chemin_m))
 
 
 def test_rapport_r_sur_des_valeurs_plantees():
```

#### `13-test_heritage_etage_processeur_v1_verrou.py.diff`

```diff
--- code-v4/tests/test_heritage_etage_processeur_v1_verrou.py
+++ code-v5/tests/test_heritage_etage_processeur_v1_verrou.py
@@ -0,0 +1,307 @@
+"""Essais du verrou des graines décisives (code v5 ; préenregistrement v11, B8, versions 7, 9 et 10 ; note D6 ; décisions de
+la mère R-4123 et R-4182, remarque 4 de l'annexe H, « Version 9 », points (a) à (e) ; « Ce qui demande un code v5 », points 4
+et 6). Chaque condition du verrou a son cas sain et son artefact (règle R5) :
+- le texte présenté est scellé, au sens de `controle_ia.scellement.verifier` (compagnon d'une ligne, au bon nom, empreinte
+  égale) ;
+- la pièce d'autorisation existe au chemin gelé sous la racine de l'arbre lancé et est scellée ;
+- elle porte quatre lignes « nom : valeur », dans l'ordre de la décision R-4123 ;
+- l'identifiant du GO est bien formé et figure dans la première colonne d'une ligne de `registres/go.md` de l'arbre lancé ;
+- le commit de la pièce est celui que le texte inscrit en tête ; l'empreinte de la pièce est celle du texte présenté, recalculée ;
+- l'heure est en UTC (forme seule) ;
+- chaque module lancé a l'empreinte que la table du texte lui donne, et la table n'en nomme pas d'autre ;
+- l'autorisation est vérifiée de nouveau avant le lancement d'une couche décisive ;
+- le manifeste inscrit l'empreinte du texte présenté, celle de la pièce et l'heure, à la place de l'empreinte de la version 6.
+Les arbres sont factices, dans un dossier temporaire ; aucune graine décisive n'est dérivée (l'essai final le contrôle)."""
+
+import hashlib
+import importlib.util
+import json
+import os
+import sys
+
+import pytest
+
+from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, chemin_env, prop
+from controle_ia.heritage_etage_processeur_v1 import constantes as K
+from controle_ia.heritage_etage_processeur_v1 import graines as GR
+from controle_ia.heritage_etage_processeur_v1 import tirages as TI
+
+COMMIT_ESSAI = "0123456789abcdef0123456789abcdef01234567"
+AUTRE_COMMIT = "fedcba9876543210fedcba9876543210fedcba98"
+GO_ESSAI = "GO-2099-01-01-01"
+HEURE_DATE_U = "Fri Nov 20 10:57:51 UTC 2026"
+CHAMPS = ("identifiant du GO", "commit du code", "empreinte du texte scellé", "heure")
+PAQUET = "src/controle_ia/heritage_etage_processeur_v1/"
+
+
+def _sha(chemin):
+    with open(chemin, "rb") as f:
+        return hashlib.sha256(f.read()).hexdigest()
+
+
+def _sceller(chemin):
+    sha = _sha(chemin)
+    with open(str(chemin) + ".sha256", "w", encoding="utf-8") as f:
+        f.write(f"{sha}  {os.path.basename(chemin)}\n")
+    return sha
+
+
+def _table_des_modules():
+    """La table du code lancé, calculée ici à part du module `graines` : chaque fichier `.py` du paquet et le `__init__.py` du
+    paquet parent ; une ligne hors de `src/` (ignorée par le contrôle des modules) pour que la table ressemble à celle du texte."""
+    paquet = os.path.dirname(os.path.abspath(GR.__file__))
+    lignes = [(_sha(os.path.join(paquet, f)), PAQUET + f) for f in sorted(os.listdir(paquet)) if f.endswith(".py")]
+    lignes.append((_sha(os.path.join(os.path.dirname(paquet), "__init__.py")), "src/controle_ia/__init__.py"))
+    lignes.append(("e" * 64, "tests/test_heritage_etage_processeur_v1_verrou.py"))
+    return lignes
+
+
+def _ecrire_texte(chemin, commit=COMMIT_ESSAI, table=None, deux_lignes_de_commit=False):
+    t = ["# Texte d'essai du verrou", "", "- Auteur : essai.",
+         f"- Commit du code d'analyse : **`{commit}`** (essai). Table des empreintes :", "", "  ```"]
+    t += [f"  {h}  {p}" for h, p in (table if table is not None else _table_des_modules())]
+    t += ["  ```", ""]
+    if deux_lignes_de_commit:
+        t += [f"- Commit du code d'analyse : **`{AUTRE_COMMIT}`** (seconde ligne).", ""]
+    t += ["Le commit du code d'analyse est inscrit en tête.", ""]
+    os.makedirs(os.path.dirname(chemin), exist_ok=True)
+    with open(chemin, "w", encoding="utf-8") as f:
+        f.write("\n".join(t))
+    return _sceller(chemin)
+
+
+def _ecrire_go(racine, lignes=None):
+    chemin = os.path.join(racine, "registres", "go.md")
+    os.makedirs(os.path.dirname(chemin), exist_ok=True)
+    corps = lignes if lignes is not None else [
+        f"| {GO_ESSAI} | 2099-01-01 | calcul | essai du verrou | — | 2099-01-01 | essai | essai |",
+        "| GO-2099-01-01-03 | 2099-01-01 | calcul | essai | — | 2099-01-01 | essai | GO-2099-01-01-02 |",
+        "| GO-essai | 2099-01-01 | calcul | identifiant mal formé | — | 2099-01-01 | essai | essai |"]
+    with open(chemin, "w", encoding="utf-8") as f:
+        f.write("# Registre des GO (essai)\n\n| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
+                "|---|---|---|---|---|---|---|---|\n" + "\n".join(corps) + "\n")
+
+
+def _ecrire_piece(racine, valeurs, noms=CHAMPS, sceller=True):
+    chemin = os.path.join(racine, K.CHEMIN_PIECE_D_AUTORISATION)
+    os.makedirs(os.path.dirname(chemin), exist_ok=True)
+    with open(chemin, "w", encoding="utf-8") as f:
+        f.write("\n".join(f"{n} : {v}" for n, v in zip(noms, valeurs)) + "\n")
+    if sceller:
+        _sceller(chemin)
+    return chemin
+
+
+def _arbre(base, go=GO_ESSAI, commit=COMMIT_ESSAI, heure=HEURE_DATE_U, empreinte=None, table=None,
+           deux_lignes_de_commit=False):
+    """Un arbre factice sain par défaut : texte scellé, registre des GO, pièce scellée. Rend (racine, texte, pièce)."""
+    racine = str(base / "arbre")
+    texte = os.path.join(racine, "prereg", "texte-essai-v1.md")
+    sha_texte = _ecrire_texte(texte, table=table, deux_lignes_de_commit=deux_lignes_de_commit)
+    _ecrire_go(racine)
+    piece = _ecrire_piece(racine, (go, commit, empreinte or sha_texte, heure))
+    return racine, texte, piece
+
+
+def test_constantes_sans_empreinte_du_texte():
+    """Point 4 du code v5 (note D6 ; silence n° 13) : la constante qui portait l'empreinte de la version 6 est retirée ; aucune
+    empreinte de 64 chiffres hexadécimaux n'est écrite dans `constantes.py` ; l'en-tête dit la version 11 ; le chemin de la
+    pièce est celui de la décision R-4123."""
+    import re
+    assert not hasattr(K, "PREENREGISTREMENT_SHA256")
+    with open(K.__file__, encoding="utf-8") as f:
+        texte = f.read()
+    assert not re.search(r"[0-9a-f]{64}", texte) and "4aee136b" not in texte
+    assert "préenregistrement v11" in texte.split("\n")[0] and "v6" not in texte.split("\n")[0]
+    assert K.CHEMIN_PIECE_D_AUTORISATION == "prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md"
+    assert K.CHAMPS_DE_LA_PIECE == CHAMPS
+
+
+def test_verrou_cas_sain_sans_graine_decisive(tmp_path):
+    """Cas sain : l'autorisation se construit sur un arbre factice conforme, sous les deux formes d'heure admises ; elle est
+    vérifiée de nouveau avant un lancement décisif (sans rien tirer) ; un manifeste écrit avec elle (couche « essai ») inscrit
+    l'empreinte du texte présenté, celle de la pièce et l'heure ; aucune graine décisive n'est dérivée."""
+    racine, texte, piece = _arbre(tmp_path)
+    a = GR.Autorisation(texte, racine)
+    assert (a.sha_texte, a.sha_piece, a.go, a.commit, a.heure) == (_sha(texte), _sha(piece), GO_ESSAI, COMMIT_ESSAI,
+                                                                   HEURE_DATE_U)
+    r2, t2, _ = _arbre(tmp_path / "iso", heure="2026-11-20T10:57:51Z")
+    assert GR.Autorisation(t2, r2).heure == "2026-11-20T10:57:51Z"
+    r3, t3, _ = _arbre(tmp_path / "jour-a-un-chiffre", heure="Sun Nov  1 09:05:00 UTC 2026")  # `date -u`, jour d'un chiffre
+    assert GR.Autorisation(t3, r3)
+    g = GR.Graines(autorisation=a)
+    for couche in GR.COUCHES_DECISIVES:
+        assert TI.exiger_autorisation_pour(couche, g)
+    case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
+            "bras": ("1", "2", "3")}
+    TI.lancer_famille(g, "essai", [case], lambda c: FREQUENCES_D_ESSAI, 2, str(tmp_path / "run"), COMMIT_ESSAI, {})
+    chemin_m = str(tmp_path / "run" / "manifeste.json")
+    with open(chemin_m, encoding="utf-8") as f:
+        m = json.load(f)
+    assert "preenregistrement_sha256" not in m
+    assert (m["texte_sha256"], m["piece_d_autorisation_sha256"], m["heure_d_autorisation"]) == (a.sha_texte, a.sha_piece,
+                                                                                                a.heure)
+    assert TI.verifier_manifeste(chemin_m) == m["etiquettes"]["nombre"]
+    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()
+    assert g.etiquettes and all(e.startswith("couche=essai|") for e in g.etiquettes)
+
+
+def _supprimer(chemin):
+    os.remove(chemin)
+
+
+def _ajouter(chemin, octets=b"\nligne ajoutee apres le scellement\n"):
+    with open(chemin, "ab") as f:
+        f.write(octets)
+
+
+def _compagnon(chemin, texte):
+    with open(chemin + ".sha256", "w", encoding="utf-8") as f:
+        f.write(texte)
+
+
+def _table_alteree(quoi):
+    t = _table_des_modules()
+    if quoi == "empreinte":
+        return [("0" * 64 if p == PAQUET + "audit.py" else h, p) for h, p in t]
+    if quoi == "absent":
+        return [(h, p) for h, p in t if p != PAQUET + "graines.py"]
+    return t + [("1" * 64, PAQUET + "module_non_lance.py")]
+
+
+def _artefact(nom, base):
+    """Construit l'artefact `nom` ; rend (texte, racine) à présenter au verrou."""
+    if nom == "texte-sans-compagnon":
+        racine, texte, _ = _arbre(base)
+        _supprimer(texte + ".sha256")
+    elif nom == "texte-altere-apres-scellement":
+        racine, texte, _ = _arbre(base)
+        _ajouter(texte)
+    elif nom == "compagnon-du-texte-a-deux-lignes":
+        racine, texte, _ = _arbre(base)
+        _compagnon(texte, f"{_sha(texte)}  {os.path.basename(texte)}\n{_sha(texte)}  autre.md\n")
+    elif nom == "compagnon-du-texte-au-mauvais-nom":
+        racine, texte, _ = _arbre(base)
+        _compagnon(texte, f"{_sha(texte)}  autre-nom.md\n")
+    elif nom == "piece-absente":
+        racine, texte, piece = _arbre(base)
+        _supprimer(piece)
+        _supprimer(piece + ".sha256")
+    elif nom == "piece-sans-compagnon":
+        racine, texte, piece = _arbre(base)
+        _supprimer(piece + ".sha256")
+    elif nom == "piece-alteree-apres-scellement":
+        racine, texte, piece = _arbre(base)
+        _ajouter(piece, b" ")
+    elif nom == "champs-dans-un-autre-ordre":
+        racine, texte, _ = _arbre(base)
+        _ecrire_piece(racine, (COMMIT_ESSAI, GO_ESSAI, _sha(texte), HEURE_DATE_U), noms=(CHAMPS[1], CHAMPS[0]) + CHAMPS[2:])
+    elif nom == "piece-a-trois-lignes":
+        racine, texte, _ = _arbre(base)
+        _ecrire_piece(racine, (GO_ESSAI, COMMIT_ESSAI, _sha(texte)), noms=CHAMPS[:3])
+    elif nom == "go-absent-du-registre":
+        racine, texte, _ = _arbre(base, go="GO-2099-01-01-09")
+    elif nom == "go-hors-de-la-premiere-colonne":
+        racine, texte, _ = _arbre(base, go="GO-2099-01-01-02")  # seulement dans la colonne « référence »
+    elif nom == "go-mal-forme":
+        racine, texte, _ = _arbre(base, go="GO-essai")  # dans la première colonne, mais mal formé
+    elif nom == "registre-des-go-absent":
+        racine, texte, _ = _arbre(base)
+        _supprimer(os.path.join(racine, "registres", "go.md"))
+    elif nom == "commit-different-du-texte":
+        racine, texte, _ = _arbre(base, commit=AUTRE_COMMIT)
+    elif nom == "deux-lignes-de-commit":
+        racine, texte, _ = _arbre(base, deux_lignes_de_commit=True)
+    elif nom == "empreinte-du-texte-differente":
+        racine, texte, _ = _arbre(base, empreinte="0" * 64)
+    elif nom == "heure-non-utc":
+        racine, texte, _ = _arbre(base, heure="2026-11-20 11:57:51+01:00")
+    elif nom == "module-d-empreinte-differente":
+        racine, texte, _ = _arbre(base, table=_table_alteree("empreinte"))
+    elif nom == "module-absent-de-la-table":
+        racine, texte, _ = _arbre(base, table=_table_alteree("absent"))
+    elif nom == "module-non-lance-dans-la-table":
+        racine, texte, _ = _arbre(base, table=_table_alteree("en-trop"))
+    else:
+        raise AssertionError(nom)
+    return texte, racine
+
+
+ARTEFACTS = ("texte-sans-compagnon", "texte-altere-apres-scellement", "compagnon-du-texte-a-deux-lignes",
+             "compagnon-du-texte-au-mauvais-nom", "piece-absente", "piece-sans-compagnon", "piece-alteree-apres-scellement",
+             "champs-dans-un-autre-ordre", "piece-a-trois-lignes", "go-absent-du-registre", "go-hors-de-la-premiere-colonne",
+             "go-mal-forme", "registre-des-go-absent", "commit-different-du-texte", "deux-lignes-de-commit",
+             "empreinte-du-texte-differente", "heure-non-utc", "module-d-empreinte-differente", "module-absent-de-la-table",
+             "module-non-lance-dans-la-table")
+
+
+@pytest.mark.parametrize("nom", ARTEFACTS)
+def test_verrou_artefact(nom, tmp_path):
+    """Chaque artefact, sur un arbre factice par ailleurs sain : l'autorisation est refusée (`GraineRefusee`), rien n'est
+    dérivé."""
+    texte, racine = _artefact(nom, tmp_path)
+    with pytest.raises(GR.GraineRefusee, match="autorisation refusée"):
+        GR.Autorisation(texte, racine)
+    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()
+
+
+def test_verrou_verifie_de_nouveau_avant_un_lancement_decisif(tmp_path):
+    """L'autorisation construite, la pièce changée puis rescellée (son empreinte du texte n'est plus celle du texte) : le
+    lancement d'une couche décisive est refusé avant toute simulation ; un module dont l'empreinte change après la construction
+    l'est aussi (la table du texte est réécrite et rescellée, pour que seul le module diffère)."""
+    racine, texte, piece = _arbre(tmp_path)
+    g = GR.Graines(autorisation=GR.Autorisation(texte, racine))
+    assert TI.exiger_autorisation_pour("decisif", g)
+    _ecrire_piece(racine, (GO_ESSAI, COMMIT_ESSAI, "0" * 64, HEURE_DATE_U))
+    for couche in GR.COUCHES_DECISIVES:
+        with pytest.raises(GR.GraineRefusee, match="autorisation refusée"):
+            TI.exiger_autorisation_pour(couche, g)
+    racine2, texte2, _ = _arbre(tmp_path / "module")
+    g2 = GR.Graines(autorisation=GR.Autorisation(texte2, racine2))
+    sha2 = _ecrire_texte(texte2, table=_table_alteree("empreinte"))
+    _ecrire_piece(racine2, (GO_ESSAI, COMMIT_ESSAI, sha2, HEURE_DATE_U))
+    with pytest.raises(GR.GraineRefusee, match="n'a pas l'empreinte que la table"):
+        TI.exiger_autorisation_pour("decisif", g2)
+    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()
+
+
+def _scellement_du_depot():
+    """Le module `controle_ia.scellement` du dépôt (HERITAGE_DEPOT), chargé sous un autre nom de paquet."""
+    src = os.path.join(chemin_env("HERITAGE_DEPOT"), "src", "controle_ia")
+    nom = "controle_ia_du_depot_pour_le_verrou"
+    if nom not in sys.modules:
+        spec = importlib.util.spec_from_file_location(nom, os.path.join(src, "__init__.py"), submodule_search_locations=[src])
+        paquet = importlib.util.module_from_spec(spec)
+        sys.modules[nom] = paquet
+        spec.loader.exec_module(paquet)
+    return importlib.import_module(nom + ".scellement")
+
+
+def test_scelle_au_sens_du_depot(tmp_path):
+    """Remarque 4, point (a) : « scellée » au sens de `controle_ia.scellement.verifier`. La réécriture du verrou
+    (`graines.verifier_scelle`, ce paquet se lançant seul) accepte et refuse exactement ce que le module du dépôt accepte et
+    refuse, sur un cas sain et sur six artefacts de compagnon."""
+    depot = _scellement_du_depot()
+    cas = {}
+    for nom, compagnon in (("sain", "{h}  {n}\n"), ("sain-sans-saut-final", "{h}  {n}"), ("sain-lignes-vides", "\n{h}  {n}\n\n"),
+                           ("absent", None), ("deux-lignes", "{h}  {n}\n{h}  {n}\n"), ("mauvais-nom", "{h}  autre.md\n"),
+                           ("une-seule-espace", "{h} {n}\n"), ("empreinte-fausse", "{z}  {n}\n"), ("majuscules", "{H}  {n}\n")):
+        f = tmp_path / f"fichier-{nom}.md"
+        f.write_text(f"contenu {nom}\n", encoding="utf-8")
+        h = _sha(f)
+        if compagnon is not None:
+            (tmp_path / (f.name + ".sha256")).write_text(
+                compagnon.format(h=h, H=h.upper(), n=f.name, z="0" * 64), encoding="utf-8")
+        try:
+            depot.verifier(f)
+            a = True
+        except Exception:
+            a = False
+        try:
+            GR.verifier_scelle(str(f))
+            b = True
+        except GR.GraineRefusee:
+            b = False
+        cas[nom] = (a, b)
+    assert all(a == b for a, b in cas.values()), cas
+    assert [n for n, (a, _) in cas.items() if a] == ["sain", "sain-sans-saut-final", "sain-lignes-vides"], cas
```

## 11. Table entière des empreintes du code v5 (chemins relatifs au dossier `code-v5/` ; ce rapport exclu)

```
0513640b0cbaedcc0e832da8d96f022a3b231ea7cc6eab40062a96714c8629e2  outils-dev/chrono_statistique.py
af772fb9918a3e69ea1bde8a34c0ac68bc8622321e0e600d0d8c8766da02f3d2  outils-dev/chrono_suite.py
fefceead89b91a30eb738e12480ff96c0356c5b2b26f4d4b9d05b5825db737cf  outils-dev/diagnostic_conflits_etrangers.py
5bf7bd44a892ef4fb66981592247131d13fa7ca5e903e4d2cb483a6e9db4d965  outils-dev/diagnostic_etrangere.py
10af2b5ab0e2d88ab9f4a9b395a555044e4ec140108b7c8d20351bf9eb1f5c3e  outils-dev/diagnostic_forme_dependantes.py
8493e5f79964ba75ea8a89b18df3cb8629a25e7570955f0b26aba0a77a0b47ea  outils-dev/diagnostic_import.py
8b2ba07ba7a009b5fab7333e206d9734a6e4de0b943f312c52b2e1cdd1c36ea9  outils-dev/diagnostic_presentation.py
12a2da99ced510c42f03645f4068f14dffa3f86787431cbd7cb67ac3ec85c9cf  outils-dev/empreintes-attendues-palier-0a.txt
b182d5ed92e5e92b7a4a14b26bb47ca4fd80bd0ce9fc916a716d51a61cfaea9e  outils-dev/essai_equivalence.py
580190bfd609195a8e5999401c264b9d8c5842a6bb0571cd28b1cc7df875a8dc  outils-dev/essai_mecanique.py
7254490fe4be80b52fa7cc46e369dbb6fd8d38300265b9a98a82069a0fad56ce  outils-dev/mutations-sortie-v1.json
0f19dd4c146ef3a6df5c6cc95dea9dd343ce53824b9310212657f9b9445a9dc5  outils-dev/mutations-sortie-v2.json
4fae9ca06c1e37a8137aca5c2a610e4158090e61f9be53db7106ef24228bd10e  outils-dev/mutations-v2-sortie-partie-a-v1.json
4c57398668ec03e58b527560216652f67403c0fae16408e9ac8c012060923c80  outils-dev/mutations-v2-sortie-partie-b-v1.json
2e7dfb42bbb98132579a61813b5723102ab937cca892af0c55efcacc4be6f535  outils-dev/mutations-v3-sortie-partie-a-v1.json
1063cad290eb6c17edc39010ab32f3109b3f5f1392ab8b4cf8a43794b5364b96  outils-dev/mutations-v3-sortie-partie-b-v1.json
09fccbd6b9019d62ce428cdf636826775ef772ac67061b8a425a4d4d79a896f8  outils-dev/mutations-v4-sortie-partie-neufs-v1.json
c62360babafb9987bc8806a46ec00fe04a3bb124acd00208e9de99327f8874d8  outils-dev/mutations-v4-sortie-partie-v3-v1.json
c5476e7b359b2c15b77795832d8f1849dc23bdc6d0aef7386b179170a4123fee  outils-dev/mutations_v1.py
9fd6fc696c49481d8cbbfeae8b795c388a2accaa2a713d55f5f1f0f4b0a20627  outils-dev/mutations_v2.py
ab84bf18bccfac3ec8c10619d2e1c6d4927f84ec2e5e43e124be37e4a842dfd8  outils-dev/mutations_v3.py
90ff3c401a0648080a2e8123ad70be1fed86cd099c21acc093da07f0f8fa0316  outils-dev/mutations_v4.py
c8a9ed8d7339129d311c787ad5f49c0ef7347c70cfae4b34fabf82f8e6fe6e55  outils-dev/sceller_v1.py
ff647eaf2ead2bd14a1a00a000f09dc142b805fbbeb6aaf87b74f225faaa72d6  outils-dev/verification-empreintes-organisme-v1.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  src/controle_ia/__init__.py
ba3d58e25b499a89d00bf9e2eab524d838297c9214277ba09823b656fe941935  src/controle_ia/heritage_etage_processeur_v1/__init__.py
73c92e370b46e5bc465679a7edc2beed1d6b1f6fc32bcab1116b027c954b13c9  src/controle_ia/heritage_etage_processeur_v1/analyse.py
7b341b6201a9f9809dfcb7e9aab1d5eb32cb7186559c8d9d21b5f270eb634d32  src/controle_ia/heritage_etage_processeur_v1/audit.py
8758b015d523370d6d1a98ff3fdebbe0fdc823805abaf9aa1fd024f48d9d64a7  src/controle_ia/heritage_etage_processeur_v1/comparateur.py
74c477d7d63e168e597b811ed7777a93d3014523d7a722b5e757b5d65d1cde77  src/controle_ia/heritage_etage_processeur_v1/constantes.py
684aeed62fd8ecc902c42e503e8211385e275e5feee36dec6d6e922afc2014bb  src/controle_ia/heritage_etage_processeur_v1/cout.py
2173613ae03067c4ff3090f74644f86550ca1d127702ff41443d1dc6a574a799  src/controle_ia/heritage_etage_processeur_v1/enveloppe.py
fda98bba41c57cbd4860a62d93c7e12f3d23d098f148af0e79b48ec20417eee3  src/controle_ia/heritage_etage_processeur_v1/equivalence.py
ed2db872f41cdad3594d9d996c9594759778a8298afafc57dc3662c8f113fd91  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
38d9bf69e307479e95a79b20dfa61dc4637c7364040baa19afe24ddafefc536b  src/controle_ia/heritage_etage_processeur_v1/etapes.py
063df6e1e2c08d79531fce8b76f3e3dbc3fdb002af7657efb1773e33afb9beda  src/controle_ia/heritage_etage_processeur_v1/executeur.py
dce5db04472d049f350f08d56f65a8254fb58eb13f3f2b6a0c3ca2e95952fcd5  src/controle_ia/heritage_etage_processeur_v1/frequences.py
d0c0d56f2ae05a0a32df4de767e5c5571a19c37e28c9f28229566aa04c2ee1c6  src/controle_ia/heritage_etage_processeur_v1/graines.py
4492c8545f6fc081eb267d851bd24a011fe4817cadad8b9606048bb26208dc1f  src/controle_ia/heritage_etage_processeur_v1/intervalles.py
fb24a9eaffdc98ee080db835d77ee2c419242ad4108ef60b440df8f1cb387536  src/controle_ia/heritage_etage_processeur_v1/lois.py
8c109627d5adf1a97de83f576a662325c628ae5e8bb2f56fb9c98f157f5c847d  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
6ac98e67fc54f66878f66542c08ec6fa76dcfc4ff7ada6b4856baea8e6db6bd3  src/controle_ia/heritage_etage_processeur_v1/mondes.py
fb2f7b48234661c2c825e2dc0c1cb7b9a6f576ff6bdebb3a2196aa3efe9293f1  src/controle_ia/heritage_etage_processeur_v1/organisme.py
e0aa6b89501c4cfeaed67d748db02dba1cb015405c34a91955d70dc2e408ab83  src/controle_ia/heritage_etage_processeur_v1/proposeurs.py
9a386fc7d56cc3f10369ef066e1f9daae7f3e41e592dd9ab4cd2b7b6768c6417  src/controle_ia/heritage_etage_processeur_v1/rangs_signes.py
5e817dfaa7734ef3f607c978f7dcf981c9446de757909600a2001fbbf4101bfb  src/controle_ia/heritage_etage_processeur_v1/registre.py
c0619eb367b94a54ced73a26098c32c1a153b9b298c596e607dd5393b81a1643  src/controle_ia/heritage_etage_processeur_v1/statistique.py
8e818c8a0f8af8ebe548c1a3f60d604d9692f3b12c78a21dadd20523d421b0c8  src/controle_ia/heritage_etage_processeur_v1/tirages.py
372229230356317c51990c0a45ed7e811e37ba2579e7b8c99f8d418bf7dbd236  tests/aides_heritage_etage_processeur_v1.py
618f5ec0319e4107da5d446af3d8a4ff9c14f545facbf5a21dd94a1309cf02b3  tests/test_heritage_etage_processeur_v1_etapes.py
acd1954670935fc87778411602519916af0b7be8e08decce2aa86f7636996d12  tests/test_heritage_etage_processeur_v1_gardes.py
b6486da564025663677d9fe6d0a1eae4a5087018d695b3d03d995482ab570f12  tests/test_heritage_etage_processeur_v1_mecanique.py
e0784e8222e60c408a1ea331972ba9abafec1e98bf758ca1d82ad4d562c3427a  tests/test_heritage_etage_processeur_v1_mondes.py
2697382c1ce050b590d956078796e5c9c5225ea1ad37d08c2ded011a47799461  tests/test_heritage_etage_processeur_v1_organisme.py
51ac18e130e621c83319dae63604fd084064dd95bdade144c18f0ec6551ccdad  tests/test_heritage_etage_processeur_v1_outils.py
ec63d2a334fb2cd5ee1507fcb8d952fbb3434e6a61a8c614697ab1d892659061  tests/test_heritage_etage_processeur_v1_statistique.py
13ae019f45efdf75500bfa2496dba19ef070f50e04968f2309299afdde1b3d53  tests/test_heritage_etage_processeur_v1_verrou.py
d342fa2a4f775085e29dcce8f97cd38b5de1293f7fe9c111a4ca0428df3f3bb4  tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
```

*Développeur, modèle O.*

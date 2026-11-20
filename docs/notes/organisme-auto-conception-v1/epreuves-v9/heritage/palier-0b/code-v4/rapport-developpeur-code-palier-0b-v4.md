# Rapport du développeur — code de l'étage sur processeur du palier 0b, version 4 (préenregistrement v8)

- Auteur : développeur, modèle L′. Pièce de travail (classe C). Travail du 2026-11-20 (`date -u` : 05:26Z en cours de travail ; 05:52Z au scellement).
- Mandat : `heritage/palier-0b/mandat-developpeur-code-palier-0b-v4-v1.md` (`c64d1574f79b677494aa0b3e0d334c9681ecdbe726b6df912bf37d36bc858356`), vérifié par `env -C` sur son dossier et `sha256sum -c` de son compagnon avant tout geste. GO-2026-11-20-11 (R-4083) : nœud 1 (a) ; nœud 2 (a) limité aux trois audits des doses ; dose 0,25 du jeu de la garde 27 (a).
- Textes qui font foi, empreintes recalculées sur disque et égales à celles du mandat ou de leur pièce : préenregistrement v8 (`fd275af81704997f2844e4ee9fdb68c5401658335221ea0768f70e3cdac9586c`) ; contrôle du différentiel v8 (`a68a46a0a480dd9f6237a2fe1aae1a6e4716d478cb75c109c8033a87f645331a`, correction T5 lue au point 2) ; contrôle de la v7 (`1211fed3b3ce0baa2324c1976897dda622e9fabc91c6ccbe50ea110346db19d0`) ; rapport du rédacteur v8 (`510266a587b21bbfa4a71afaeb95cf31e54c7ce2e934142dfde3b26ef059ee9b`) ; rapport du code v3 et sa vérification (lus ; table des 51 empreintes du rapport v3, § 8).
- Point de départ : `code-v3/src`, `tests`, `outils-dev` copiés par `cp -r` dans le bloc-notes, deux fois (`dev-palier-0b-v4/code-v3/`, gardé intact pour les différentiels et les empreintes de sorties ; `dev-palier-0b-v4/code-v4/`, copie de travail). Les deux copies ont les 51 empreintes de la table v3 (`sha256sum -c`, aucun écart).
- Code de l'organisme : copie du dépôt `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/` recopiée dans le bloc-notes (garde 17), non modifiée.
- Environnement : Python 3.13.18, mêmes bibliothèques que le code v3.

## 0. Verdict

Les points 1, 3, 4 et 5 de « Ce qui demande un code v4 » sont faits, selon les mots de Lazar (GO-2026-11-20-11) ; **le point 2 (verrou D6) est un arrêt motivé** : la v8 dit elle-même que le fichier d'autorisation du lancement n'est pas défini et que le verrou ne s'écrit qu'après (§ 1, point 2) ; `graines.py` est inchangé. Les points 6 et 7 ne demandent aucun changement ; la moyenne permutée du point 7 est rapportée. **Chaque fichier d'essais lancé seul : huit fichiers, 79 passés, 0 échoué. Suite entière : 79 passés, 0 échoué (712 s).** L'essai « aucune graine décisive » passe seul et en suite. **Banc `mutations_v3.py` (71 défauts : les 50 du v2 à l'identique et 21 neufs), rejoué en entier : 71 appliqués, 71 vus, chacun par un essai en échec ; témoins au vert.** Sorties : 144 empreintes égales à l'octet sur 144 là où aucune règle ne change ; 6 changées, chacune par une règle nommée (§ 5). Treize silences déclarés (§ 2), trois constats (§ 6), aucun refus d'outil.

## 1. Ce qui a été fait, point par point (« Ce qui demande un code v4 », v8, annexe H)

### Point 1 — audit de présentation (`audit.py`) et étape 3 (`mondes.py`)

- **Nœud 1 (a)** : `traits_de_forme` mesure la longueur sur `texte_aux_nombres_remplaces(texte)` — chaque nombre d'au moins quatre décimales, signe et exposant compris, remplacé par un caractère (`#`) ; ce sont exactement les nombres que `jetons` remplace par `<nombre>` (même fonction `_nombre_long`, `jetons` réécrit sur elle, à sortie égale). `traits_de_contenu(loi, Z, G, texte)` ajoute, en septième trait, la longueur brute du texte canonique ; il refuse (`AuditRefuse`) un texte qui n'est pas le texte canonique de la loi.
- **Nœud 2 (a), restreint** : pour chacune des quinze exactitudes, `sous_permutation` donne σ₀ (écart-type, ddof = 1) et la moyenne des exactitudes sous `permutations` permutations (1 000 par défaut, `PERMUTATIONS_AUDIT`) ; étiquettes permutées entre lois pour les deux audits de lois, entre suites pour les trois audits des doses (`permuter_les_etiquettes` : chaque suite garde une étiquette commune ; une suite à deux étiquettes est refusée) ; cinq plis retirés à chaque permutation. `lecture` : forme des lois à la lettre (au-dessus de 0,55, arrêt) ; forme des doses en trois lectures (au plus 0,55 tenue ; au-dessus de 0,55 + 2 σ₀ arrêt ; entre les deux « non départagée du hasard à cette taille », qui pose la mention) ; contenu et réunis rapportés (au-dessus de 0,55, signalés, mention). `lire_audit` exige les quinze exactitudes et elles seules. `audit_presentation(mondes, rng, rng_permutation, permutations)` rend les quinze A, la table (A, σ₀, moyenne permutée, seuil 0,55 + 2 σ₀, nombre de permutations, unités permutées, lecture), `arret`, `non_departagees`, `signalement`, `mention`. La lecture observée tire ses plis du même `rng`, dans le même ordre qu'au code v3 ; les permutations ont leur propre générateur.
- **Arrêts** (`ArretAudit`, à la lecture observée comme sous permutation) : exactitude non calculable (pas deux classes, ou moins de cinq exemples d'une classe — le code v3 rendait None et la rangeait « non calculée ») ; pli d'entraînement privé d'une classe ; centre de classe non fini. La clé `non_calculees` disparaît.
- **Identifiant de la suite** : `mondes_pour_l_audit` porte `suite` (rang de la suite dans la liste) ; `audit_presentation` l'exige et refuse une suite à deux doses.
- **Étape 3** : `audit_du_generateur` est coupée en `generer_suites_d_audit` (construction) et `juger_suites_d_audit` (jugement) ; le générateur des permutations est, par défaut, celui de la couche « audit », famille « audit », rôle « permutation » ; un `ArretAudit` devient un `ArretGenerateur` (liste d'arrêt, point 2) ; à l'arrêt sur une exactitude, le rapport est joint à l'exception (`rapport`), pour que A, σ₀ et le seuil des quinze restent rapportés. Paramètres neufs : `rng_permutation`, `permutations`, `couche` (« audit » par défaut ; les essais jouent « essai »).
- **Point 7** : la moyenne des exactitudes permutées est rapportée pour les quinze (`moyenne_permutee`) ; voir § 6 pour ce que les essais en montrent.

### Point 2 — verrou des graines décisives (`graines.py`, `constantes.py`) : arrêt motivé, rien n'est écrit

Le mandat demande le verrou « avec le fichier d'autorisation tel que la v8 le définit, ou un arrêt motivé si la v8 ne le définit pas assez ». **Arrêt motivé** :
- B8 (version 7, note D6) fait ouvrir le verrou si le texte porte son compagnon, si **son empreinte est celle que la mère inscrit au scellement dans le fichier d'autorisation du lancement**, et si chaque module lancé a l'empreinte que la table du texte lui donne.
- « Ce qui demande un code v4 », point 2 (v8, avec la correction T5 du contrôle) : ce fichier « n'est défini nulle part dans ce texte ; sa forme, son auteur et l'endroit où il vit sont à définir, par la mère et au code v4, **avant que le verrou soit écrit** ». Ni le mandat ni le GO ne le définissent.
- Sans forme ni lieu, le code ne peut ni le lire ni dire ce qu'est « l'empreinte inscrite » ; en inventer une trancherait un silence que le texte réserve à la mère. Écrire seulement les deux autres conditions, ou retirer seul `PREENREGISTREMENT_SHA256` (que `tirages.ecrire_manifeste` inscrit au manifeste et que rien ne remplacerait), ferait un verrou à moitié de la règle D6.
- Donc : `graines.py` est à l'octet celui du code v3 ; `constantes.py` garde `PREENREGISTREMENT_SHA256` (empreinte de la v6) ; le verrou reste celui du code v3 (couches décisives refusées sans `Autorisation`, refus consignés) et la liste d'arrêt, point 1, interdit toujours tout tirage. Ce point reste à faire après que la mère aura défini le fichier (forme, auteur, lieu). Ce qu'il faudra alors : comparer l'empreinte du texte présenté à celle du fichier d'autorisation ; contrôler chaque module lancé contre la table du texte (en-tête « Commit du code d'analyse ») ; retirer `PREENREGISTREMENT_SHA256` et dire ce que le manifeste inscrit à sa place.
- Aucun essai ni défaut de banc neuf pour ce point, puisque rien n'y change ; l'essai final « aucune graine décisive » passe (§ 3).

### Point 3 — étalonnage (`etalonnage.py`) : note D8

`exiger_ecart_type_et_taille_finis` : un écart-type entre jumelles réuni nul ou non fini, ou une taille réduite non finie, arrête l'étalonnage (`ArretEtalonnage`, cause et case dans le message) ; appelée à chaque évaluation de la dichotomie (le réglage maximal compris, avant toute mention « non atteignable ») et pour chaque proposeur sans réglage. Une taille que le réglage maximal n'atteint pas reste « non atteignable ».

### Point 4 — manifeste (`tirages.py`) : choix 12

`ecrire_manifeste` écrit d'abord `manifeste-etiquettes.txt` à côté du manifeste : la liste triée des étiquettes, une par ligne, jointes par un saut de ligne sans saut final — le texte même dont le manifeste portait déjà l'empreinte —, scellée par son compagnon ; le manifeste inscrit `fichier` et `fichier_sha256` (égale à `sha256` : elle se rejoue par `sha256sum`). `verifier_manifeste` rejoue tout (compagnons, empreinte, nombre, tri, couches) et arrête sinon.

### Point 5 — le jeu de la garde 27

- **Où** : à l'étape 4, sur la couche mécanique, par `etapes.etape_4_jeu_de_la_garde_27(graines, couche, dossier, prop, sources, famille=…)`, qui appelle `mondes.generer_jeu_avec_etrangeres` puis `mecanique.jouer_jeu_diagnostic` (bras 1 à 3, puis 4a et 4b), au taux d'échec de 0,25. `etape_4` est inchangée (bras 1 à 3 seuls), et son en-tête de module dit où se joue la garde 27.
- **À quelle dose** : `constantes.DOSE_JEU_GARDE_27 = 0.25`, fixée par cette fonction ; `generer_jeu_avec_etrangeres` et `jouer_jeu_diagnostic` arrêtent à toute autre dose avant de tirer ou de jouer (« à elle seule »).
- **Choix 8** : non touché. Le code v3 note l'origine d'une loi à sa première tentative (`Frequences.noter_loi` : la première clé (contexte, monde, texte) l'emporte, les bras étant joués dans l'ordre donné, les tentatives dans l'ordre du scellement), comme le contrôle de la v7 le lit ; point à lever par le vérificateur.

### Point 6 — sans changement du code

L'écart 1 hors du point 5, le choix 11, la note D5, la tenue : aucun changement.

### Point 7 — fuite entre mondes frères

Rapportée (moyenne permutée) ; à regarder par le vérificateur ; aucune règle des plis n'est changée (note D9 : plis toujours tirés sur les mondes, sans stratification).

## 2. Silences du texte, déclarés (rien n'est tranché)

1. **σ₀** : écart-type des exactitudes permutées avec ddof = 1 (le texte dit « l'écart-type »). Sur 1 000 permutations, la différence avec ddof = 0 est de 0,05 % de σ₀.
2. **Générateur des permutations** : un seul générateur pour les quinze exactitudes (étiquette `couche=audit|famille=audit|role=permutation` à l'étape 3), parcourues dans l'ordre fixe (forme, contenu, réunis ; vraies/fausses, dépendantes/indépendantes, puis les trois paires de doses) ; à chaque permutation, il tire d'abord les étiquettes, puis les plis. Le texte dit « graines de la couche « audit » sous le rôle « permutation » » sans dire si c'est une graine ou une par exactitude. Aucun champ d'étiquette ne nomme un audit (`ORDRE_DES_CHAMPS` gelé) ; je n'en ai pas ajouté.
3. **Générateur des plis de la lecture observée** : toujours passé par l'appelant (`rng_audit`), comme au code v3 ; aucune fonction du code ne le dérive (silence hérité du code v3).
4. **Égalités** : « au plus 0,55 » est inclusif ; « au-dessus de 0,55 + 2 σ₀ » est strict ; une exactitude égale au seuil calibré est « non départagée ».
5. **Exactitude non calculable** : j'y range aussi « pas exactement deux classes » (le code v3 rendait alors None, comme pour moins de cinq exemples) ; sous permutation entre suites, une classe qui tomberait sous cinq exemples (suites de tailles inégales) arrête de même.
6. **Caractère du jeton dans le texte aux nombres remplacés** : `#` ; seule sa longueur (un caractère) compte.
7. **Distribution des traits de contenu (B1 (iii))** : elle porte désormais la longueur brute (`longueur_brute`), puisque la v8 la range parmi les traits de contenu ; les six autres traits sont à l'octet ceux du code v3.
8. **Garde 27** : le texte ne dit ni le proposeur du jeu sur la couche mécanique ni le nombre de sources ; `etape_4_jeu_de_la_garde_27` les prend en paramètres **sans défaut** (au moins deux sources) ; `etape_4` ne l'appelle pas d'elle-même. Les essais le jouent comme le code v3 (lecteur réglé pour la tenue, τ = 2, deux sources).
9. **Note D8** : le contrôle porte sur l'écart-type réuni (celui qui divise l'écart moyen et qui est gelé) ; un écart-type nul dans un seul bras, l'écart-type réuni restant positif, n'arrête pas.
10. **Choix 12** : nom du fichier (`<manifeste>-etiquettes.txt`, à côté du manifeste) ; contenu sans saut de ligne final, pour que son empreinte soit celle que le manifeste inscrivait déjà.
11. **Étape 3** : le rapport joint à l'`ArretGenerateur` (`rapport`) est un ajout de forme, pour que « A, σ₀ et le seuil rapportés pour les quinze » tienne aussi quand l'étape arrête sur une exactitude ; à un arrêt de l'audit lui-même (pli, centre, exactitude non calculable), il n'y a pas de table à joindre.
12. **Outils de développement du code v2** (`outils-dev/diagnostic_presentation.py`, `diagnostic_forme_dependantes.py`) : non mis à jour ; ils gardent l'interface du code v3 (`audit_presentation` à deux arguments) et sont la trace des diagnostics passés. `diagnostic_presentation.py` ne tourne plus sur le code v4.
13. **En-tête de `constantes.py`** : il dit encore « préenregistrement v6 », comme `PREENREGISTREMENT_SHA256` (point 2, non fait).

## 3. Essais

Lancement : `PYTHONPATH=<code-v4>/src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/code-organisme-94bfd92/orchestrator python3 -B -m pytest -q -p no:cacheprovider CHEMIN`, par l'outil `travail/lancer_essais_v1.py` : un processus par fichier, puis un processus pour la suite entière ; dossier courant dans le bloc-notes ; rien d'écrit dans le dépôt. Les deux lancements ont tourné en même temps que le banc (quatre processeurs).

| fichier d'essais | seul | durée seul | changé ? |
|---|---|---|---|
| `etapes` | 5 passés | 29 s | non |
| `gardes` | 17 passés | 2 s | non |
| `mecanique` | **10 passés** (9 du v3, la garde 27 jouée par la fonction de l'étape 4, et un essai neuf de la dose) | 250 s | oui |
| `mondes` | **15 passés** (9 du v3, dont 4 adaptés ; 6 neufs) | 305 s | oui |
| `organisme` | 5 passés | 109 s | non |
| `outils` | 15 passés | 5 s | non |
| `statistique` | **11 passés** (10 du v3, le manifeste étendu ; 1 neuf : note D8) | 5 s | oui |
| `zz_aucune_graine_decisive` | 1 passé | 0,07 s | non |
| total, un processus par fichier | **79 passés, 0 échoué** | | |
| **suite entière, un processus** | **79 passés, 0 échoué** | 712 s | |

Journaux : `travail/essais-fichiers-v1.log`, `travail/essais-suite-v1.log`. 5 + 17 + 10 + 15 + 5 + 15 + 11 + 1 = 79, le même compte qu'en suite entière. **L'essai final « aucune graine décisive » passe seul et en suite entière** ; les seules couches dérivées par les essais sont « essai » et « essai-de-forme ».

Essais neufs ou changés, avec cas sain et artefact (règle R5) :

| règle | cas sain | artefact | essai |
|---|---|---|---|
| nœud 1 : longueur de forme | texte aux nombres remplacés ; le signe d'un nombre long n'entre pas dans la forme ; un nombre court garde son signe | — (le défaut « longueur de forme brute » est vu) | `mondes::test_longueur_de_forme_sur_le_texte_aux_nombres_remplaces` |
| nœud 1 : longueur brute au contenu | septième trait de contenu égal à la longueur du texte canonique | texte non canonique : refus | idem |
| garde 25 : signes des dépendantes changés (générateur fautif planté) | forme inchangée pour toute loi sans nombre court négatif ; exactitude de forme dépendantes/indépendantes à 0,03 près de celle du générateur sain | contenu dépendantes/indépendantes au-dessus de 0,55, signalé, mention | `mondes::test_garde_25_signes_des_dependantes_changes_vus_par_le_contenu_et_non_par_la_forme` |
| nœud 2 : lecture calibrée, valeurs plantées | table à 0,5 : rien ; 0,55 tout juste : tenue | zone médiane (0,58, σ₀ = 0,02) : mention sans arrêt ; 0,60 : arrêt ; audit de lois à 0,56 (σ₀ = 0,01) : arrêt à la lettre ; contenu à 0,6 : signalement sans arrêt ; table incomplète : refus | `mondes::test_garde_25_lecture_calibree_sur_valeurs_plantees` |
| nœud 2 : dose inscrite | — | exactitude de forme d'un audit des doses au-dessus de 0,55 + 2 σ₀ : arrêt | `mondes::test_garde_25_dose_inscrite_dans_la_presentation_arret` (adapté) |
| σ₀ par permutation entre suites | étiquettes permutées, chaque suite garde la sienne ; entre lois pour les audits de lois | suite à deux étiquettes : refus ; monde sans identifiant de suite : refus | `mondes::test_permutation_entre_suites_garde_l_etiquette_commune` |
| arrêts de l'audit (note D9, v8) | exactitude calculée sur des traits plantés | pli d'entraînement privé d'une classe (plis placés à la main), quatre exemples d'une classe, une seule classe, centre non fini : arrêt ; de même sous permutation | `mondes::test_garde_25_pli_prive_d_une_classe_et_exactitude_non_calculable_arretent` |
| générateur sain | aucun arrêt, aucune exactitude non départagée, rien au-delà de trois σ₀ de la moyenne permutée | — | `mondes::test_garde_25_audit_de_presentation_cas_sain` (adapté, § 6) |
| table de l'audit sur le générateur de B1 | quinze exactitudes avec A, σ₀, moyenne permutée, seuil, lecture, unités permutées (8 suites, 1 152 et 384 lois) | — | `mondes::test_audit_de_presentation_du_generateur_de_b1_a_taille_reduite` (adapté) |
| poids des dépendantes doublés | — | contenu signalé (mondes à dose nulle du générateur sain joints) ; sans eux, exactitude non calculable : arrêt | `mondes::test_garde_25_poids_des_dependantes_doubles_signale` (adapté) |
| étape 3 | rapport ou arrêt avec rapport joint, table cohérente | suites d'une seule dose : arrêt ; `audit_du_generateur` (couche « essai », une suite) : arrêt, graine du rôle « permutation » dérivée | `mondes::test_etape_3_jugement_des_suites_et_arrets` |
| note D8 (écarts-types plantés) | écart-type positif : dichotomie atteinte, « non atteignable » au-delà du réglage maximal | écart-type nul (dichotomie et sans réglage) ; taille non finie : arrêt, jamais « non atteignable » | `statistique::test_note_d8_ecart_type_nul_ou_taille_non_finie_arrete_l_etalonnage` |
| choix 12 | liste triée, scellée, empreinte égale à celle du manifeste, rejouée par `verifier_manifeste` | une étiquette retirée (compagnon refait) : arrêt ; liste altérée sans compagnon refait : arrêt | `statistique::test_manifeste_d_un_lancement` (étendu) |
| point 5 : dose du jeu | jeu joué par `etape_4_jeu_de_la_garde_27` à 0,25, bras 1 à 3 puis 4a et 4b, mondes à 0,25 | dose 0,5 à la construction et au jeu : arrêt avant de tirer ; une seule source : arrêt | `mecanique::test_garde_27_dose_du_jeu_fixee_a_0_25`, `mecanique::test_garde_27_bras_de_diagnostic_et_tenue_sans_effet_au_bras_4b` |

Les essais jouent 20 permutations (50 pour la dose inscrite), non 1 000 : l'audit à pleine taille est l'étape 3, que ce mandat interdit de jouer. La valeur gelée est vérifiée (`PERMUTATIONS_AUDIT == 1000`).

## 4. Banc des défauts (`outils-dev/mutations_v3.py`)

Version 3 du banc : les 50 défauts de `mutations_v2.py` repris à l'identique (remplacements, fichiers, essais qui les voient ; leurs 50 ancres se trouvent une fois chacune dans le code v4), et 21 neufs. Mode `--verifier` neuf (compte des ancres, sans essai) : « défauts 71, identifiants distincts 71, problèmes 0 ». Rejoué en entier, en deux moitiés parallèles (identifiants en argument ; chaque moitié joue d'abord les témoins de ses sélections sur le code sain) : **partie a, 42 défauts, 42 vus ; partie b, 29 défauts, 29 vus ; témoins au vert dans les deux.** Chaque défaut est vu par un essai en échec (code 1 : 71 sur 71 ; aucun code 2 ou plus, donc aucune erreur de collecte). Sorties : `outils-dev/mutations-v3-sortie-partie-a-v1.json`, `outils-dev/mutations-v3-sortie-partie-b-v1.json`. Les 50 défauts du v2 sont vus sur le code v4 (dont S8 (i) en 192 s, S8 (ii) en 181 s, garde 27 et C2 en 36 à 42 s).

Les 21 défauts neufs :

| défaut | règle | fichier muté | essai qui le voit | durée |
|---|---|---|---|---|
| longueur-de-forme-brute | nœud 1 | `audit.py` | `mondes -k longueur_de_forme` | 0,4 s |
| longueur-brute-hors-du-contenu | nœud 1 | `audit.py` | `mondes -k longueur_de_forme` | 0,4 s |
| regle-calibree-etendue-aux-lois | nœud 2 (lettre des lois) | `audit.py` | `mondes -k lecture_calibree` | 0,4 s |
| regle-calibree-retiree | nœud 2 (doses à la lettre) | `audit.py` | `mondes -k lecture_calibree` | 0,4 s |
| zone-mediane-arretee | nœud 2 | `audit.py` | `mondes -k lecture_calibree` | 0,4 s |
| seuil-calibre-a-vingt-sigma | nœud 2 | `audit.py` | `mondes -k lecture_calibree` | 0,4 s |
| permutation-entre-mondes | σ₀ entre suites | `audit.py` | `mondes -k taille_reduite` | 17,6 s |
| etiquettes-non-permutees | σ₀ entre lois | `audit.py` | `mondes -k permutation_entre` | 0,4 s |
| suite-non-portee | identifiant de la suite | `mondes.py` | `mondes -k taille_reduite` | 16,2 s |
| pli-prive-accepte | note D9 | `audit.py` | `mondes -k pli_prive` | 0,5 s |
| non-calculable-acceptee | version 8 | `audit.py` | `mondes -k pli_prive` | 0,4 s |
| centre-non-fini-accepte | note D9 | `audit.py` | `mondes -k pli_prive` | 0,4 s |
| arret-de-l-audit-non-converti | étape 3 | `mondes.py` | `mondes -k etape_3` | 18,9 s |
| d8-ecart-type-nul-accepte | note D8 | `etalonnage.py` | `statistique -k note_d8` | 0,4 s |
| d8-taille-non-finie-acceptee | note D8 | `etalonnage.py` | `statistique -k note_d8` | 0,4 s |
| d8-dichotomie-sans-controle | note D8 | `etalonnage.py` | `statistique -k note_d8` | 0,3 s |
| liste-des-etiquettes-autre-que-le-texte-hache | choix 12 | `tirages.py` | `statistique -k manifeste` | 0,5 s |
| liste-des-etiquettes-non-verifiee | choix 12 | `tirages.py` | `statistique -k manifeste` | 0,5 s |
| dose-du-jeu-non-exigee-a-la-construction | point 5 | `mondes.py` | `mecanique -k dose_du_jeu` | 0,5 s |
| dose-du-jeu-non-exigee-au-jeu | point 5 | `mecanique.py` | `mecanique -k dose_du_jeu` | 0,4 s |
| jeu-de-l-etape-4-a-une-autre-dose | point 5 | `etapes.py` | `mecanique -k garde_27_bras` | 0,4 s |

Comme au banc v2, aucun défaut n'ouvre le verrou des couches décisives.

## 5. Sorties : ce qui reste égal à l'octet, ce qui change et pourquoi

Outil `travail/empreintes_v3_v4_v1.py` (graines « essai » seulement ; mêmes appels ; seul le paquet change), comparé par `travail/comparer_empreintes_v1.py` entre le paquet intact du code v3 et le code v4 : **144 empreintes sur 144 égales** là où aucune règle ne change, et **6 sur 6 différentes** là où une règle change.

Égales à l'octet (144) : couche statistique, six proposeurs et doses, bras 1 à 4b (M1, D, I, lois fausses tenues) ; couche mécanique, le jeu à deux sources à la dose 0,25 (registres, mesures, entrées servies, registres sources, empreintes des vues du bras 2, compteurs) ; générateur, six suites des trois doses (clés, épisodes, compteurs) ; `mondes_pour_l_audit` sans la clé `suite` ; les 64 cases des traits de forme ; les six traits de contenu de la version 6 ; la distribution des traits de contenu sans la longueur brute ; `exactitude_equilibree` sur des traits plantés (avec et sans signal : même classifieur, mêmes plis) ; les jetons ; une ligne de dichotomie et un écart-type sans réglage de l'étalonnage ; les sorties scellées d'une case ; le manifeste sans les deux champs neufs.

Changées, et pourquoi :

| sortie | pourquoi |
|---|---|
| dernier trait de forme (longueur) | nœud 1 (a) : texte aux nombres remplacés |
| traits de contenu | nœud 1 (a) : la longueur brute s'ajoute (septième trait) |
| les quinze exactitudes observées | les traits de forme et de contenu changent ; les plis sont les mêmes (même `rng`, même ordre) |
| distribution des traits de contenu | la longueur brute s'ajoute |
| `mondes_pour_l_audit` | chaque monde porte `suite` (permutation entre suites) |
| manifeste | choix 12 : `fichier` et `fichier_sha256` de la liste des étiquettes |

S'ajoutent, sans équivalent au code v3 : la table de l'audit (σ₀, moyenne permutée, seuil, lecture), les clés `non_departagees` et `table` (la clé `non_calculees` disparaît : une exactitude non calculable arrête), le fichier `manifeste-etiquettes.txt` et son compagnon. Changent de sort : une exactitude non calculable, un pli privé d'une classe ou un centre non fini arrêtent (au code v3 : None, ou une exactitude sur un centre vide) ; un écart-type nul ou une taille non finie arrêtent l'étalonnage (au code v3 : « non atteignable ») ; le jeu à sources étrangères à une autre dose que 0,25 arrête (au code v3 : construit et joué). Fichiers : `travail/empreintes-v3.json`, `travail/empreintes-v4.json`.

## 6. Défauts vus et constats

Aucun défaut du code v3 trouvé hors de la liste du texte. Trois constats, pour la mère et le vérificateur ; je n'en tranche aucun.

1. **Contenu et réunis des audits des doses, lus à la lettre, alarment au hasard.** La règle calibrée ne vaut, par le texte et le GO, que pour la forme des trois audits des doses. Les exactitudes de contenu et réunies des mêmes audits restent « au-dessus de 0,55, signalées », sans calibrage, alors que leur bruit est celui que l'écart 3 a mesuré pour la forme. Sur le générateur sain par construction de l'essai (300 mondes par dose, graines locales de numpy, 100 permutations ; `travail/diag_cas_sain_v1.py`), aucune exactitude ne s'écarte de sa moyenne permutée de plus de 2,4 σ₀, mais « reunis/mondes_dose_0.25_contre_0.5 » vaut 0,558 (σ₀ = 0,025) : elle est signalée et pose la mention « générateur non audité pour l'étage payant ». C'est la lettre du texte, et non un arrêt. J'ai donc réduit l'essai du cas sain à ce que la garde 25 exige (aucun arrêt) et à « rien au-delà de trois σ₀ » ; l'essai du code v3 exigeait aussi « aucun signalement », ce qui ne tenait que par le tirage des plis.
2. **Point 7, la moyenne permutée des audits des doses s'écarte de 0,5 à petite taille.** Sur le générateur de B1, quatre suites par dose (couche « essai », famille « diag-point-7 », 200 permutations ; `travail/diag_point_7_v1.py` ; ni audit ni étape 3), les moyennes permutées des neuf audits des doses vont de 0,457 à 0,603 (forme : 0,472 ; 0,548 ; 0,550), contre 0,497 à 0,505 pour les six audits de lois. À huit suites par paire, un monde de test a jusqu'à trois frères de même étiquette parmi environ 13 mondes d'entraînement de sa classe ; à 50 suites par dose, trois parmi environ 160. La règle « 0,55 + 2 σ₀ » ne lit pas cette moyenne ; le texte la fait rapporter, et c'est fait. Tirer les plis par suite changerait la note D9 (erratum contre-lu) : non fait.
3. **Avant-goût, sans lecture de critère** (même diagnostic que le constat 2 ; ce n'est pas l'audit de l'étape 3) : l'exactitude de contenu « dépendantes contre indépendantes » vaut 0,63 (σ₀ = 0,035), et plusieurs exactitudes de contenu et réunies des doses dépassent 0,55 ; aucune exactitude de forme n'arrête, une de forme (doses 0,25 contre 0,5 : 0,594, seuil 0,749) est « non départagée ». C'est ce que le contrôle de la v7 (§ 10, point 4) prévoyait sous les options (a). Je le signale pour la règle R4 (la mère sait ce que le développeur a vu), sans en tirer aucune lecture.

Défauts de mes propres essais vus en cours de travail, corrigés avant la validation : l'essai des signes comptait les clés « 0 » et « 1 » du texte comme des nombres courts (aucune loi n'était retenue ; le critère est désormais l'absence de nombre court négatif) ; le cas sain (constat 1).

## 7. Gestes, refus et incidents

- **Aucun refus de permission, de classifieur ni de garde.** Aucun incident de l'outil de remplacement (règle R-4067) : chaque remplacement par l'outil d'édition a été appliqué au premier essai ; le banc vérifie ses 71 ancres (`mutations_v3.py --verifier`, « problèmes 0 »).
- Une commande simple par appel ; aucun heredoc, aucun code en ligne passé à un interpréteur : chaque calcul passe par un fichier de `travail/`. Calculs longs en tâche de fond ; attente par `timeout … tail -F` ou par un moniteur des journaux (commande `tail -F` seule) ; aucun processus arrêté.
- Graines : seulement la couche « essai » (essais, banc, empreintes, diagnostic du point 7) et des générateurs locaux de numpy (diagnostic du cas sain, essais aux valeurs plantées) ; aucune graine des couches « etalonnage », « mecanique », « mecanique-reglages », « audit », « decisif » ou « confirmation » dérivée ; les seules demandes de couches décisives sont celles des essais des refus, toutes refusées. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille ; aucun taux de rejet, aucune puissance, aucune valeur p calculés.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau (aucun `git fetch` ni `git show`) ; aucune écriture dans le dépôt, aucun commit ; le dépôt a été lu seulement ; rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/` ; aucune valeur de clé ; aucun identifiant de modèle.
- La règle R-4067 ne se trouve ni dans `registres/decisions.md`, ni dans `go.md`, ni dans `etat.md` ; je l'ai lue dans le mandat du rédacteur de la v8 (« si l'outil rejette une ancre, c'est un essai qui échoue … vérifie chaque ancre … avant l'appel »).

## 8. Fichiers et empreintes

Dossier rendu : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/dev-palier-0b-v4/code-v4/` (arborescence du code v3 : `src/`, `tests/`, `outils-dev/`, et ce rapport). Chaque fichier a son compagnon `.sha256`, au format de `sha256sum` lancé dans son dossier (`travail/sceller_tout_v1.py` ; les compagnons des 41 fichiers inchangés sont ceux du code v3, identiques ; ceux des dix fichiers changés ont été récrits ; trois sont neufs). Ce rapport a son propre compagnon. La table entière (54 fichiers) est au § 10 ; elle se vérifie par `sha256sum -c` dans `code-v4/` (fait : aucun écart).

Fichiers changés ou neufs (les 41 autres sont ceux du code v3, à l'octet) :

```
890040e3b4d3a9d16bdb52a60e66aba9aea048a7129a080b377a20ab63dcdf30  src/controle_ia/heritage_etage_processeur_v1/audit.py
f94e5940d62fc5536a465113596361b0039b80f38ee4471688b551277c4d0e78  src/controle_ia/heritage_etage_processeur_v1/constantes.py
ed2db872f41cdad3594d9d996c9594759778a8298afafc57dc3662c8f113fd91  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
4a4b22e85543c5045d398a095ed052aee9de582d88fff9b5a78147fcd0cb95db  src/controle_ia/heritage_etage_processeur_v1/etapes.py
367a9ce047ceb033a58f40090efa5ba0360853f5f153d89148671ac35ee7acb8  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
eb9b2c2d7d276c0e55e3e9dd228604dd235e758c95b235ea1b508d43391ed38d  src/controle_ia/heritage_etage_processeur_v1/mondes.py
93077e25e671a164fcae741c248f865011dfe436bb49d830ead4c9e41ba8795c  src/controle_ia/heritage_etage_processeur_v1/tirages.py
b6486da564025663677d9fe6d0a1eae4a5087018d695b3d03d995482ab570f12  tests/test_heritage_etage_processeur_v1_mecanique.py
4c934139f0c5b15897f9e69f23863f1978cd6577a3b2085f3c0f11477af900e7  tests/test_heritage_etage_processeur_v1_mondes.py
2d1bc1fd6593137bc6e6a39d934154a09dd8fcdac4811fbf2c9f3649daabf66a  tests/test_heritage_etage_processeur_v1_statistique.py
ab84bf18bccfac3ec8c10619d2e1c6d4927f84ec2e5e43e124be37e4a842dfd8  outils-dev/mutations_v3.py
2e7dfb42bbb98132579a61813b5723102ab937cca892af0c55efcacc4be6f535  outils-dev/mutations-v3-sortie-partie-a-v1.json
1063cad290eb6c17edc39010ab32f3109b3f5f1392ab8b4cf8a43794b5364b96  outils-dev/mutations-v3-sortie-partie-b-v1.json
```

Les empreintes des fichiers de code et d'essais sont celles relevées avant le lancement des essais et du banc, et relevées de nouveau après : le code n'a pas changé entre la suite au vert, le banc et le scellement. `graines.py` garde l'empreinte du code v3 (`cf433337…`).

Non rendus, laissés dans le bloc-notes (`dev-palier-0b-v4/`) : `code-v3/` (copie intacte du code v3) ; `code-organisme-94bfd92/` (copie) ; `travail/` : `lancer_essais_v1.py`, `empreintes_v3_v4_v1.py`, `comparer_empreintes_v1.py`, `differentiels_v1.py`, `sceller_tout_v1.py`, `assembler_rapport_v1.py`, `diag_cas_sain_v1.py`, `diag_point_7_v1.py` ; journaux des essais ; `empreintes-v3.json`, `empreintes-v4.json` ; `diffs/` ; `table-v3.txt`, `table-empreintes-code-v4.txt` ; dossiers de travail du banc.

## 9. Différentiels v3 → v4 (`diff -u`)

Fichiers changés : sept modules (`audit`, `constantes`, `etalonnage`, `etapes`, `mecanique`, `mondes`, `tirages`), trois fichiers d'essais (`mondes`, `mecanique`, `statistique`), un outil neuf (`mutations_v3.py`, donné en différentiel depuis `mutations_v2.py`, gardé intact). Les 41 autres fichiers de la table v3 sont à l'octet ceux du code v3.

#### `1-audit.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/audit.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/audit.py
@@ -12,6 +12,19 @@
 validation croisée à cinq plis, exactitude équilibrée ; trois audits (vraies contre fausses ; dépendantes contre
 indépendantes ; mondes par dose, lus par paires de doses), chacun sur les traits de forme, de contenu, puis réunis : quinze
 exactitudes. Celles des traits de forme décident (liste d'arrêt, point 2) ; les autres sont rapportées et lient l'étage payant.
+
+Code v4 (préenregistrement v8 ; GO-2026-11-20-11 : nœud 1 (a), nœud 2 (a) limité aux trois audits des doses) :
+- longueur de forme mesurée sur le texte où chaque nombre d'au moins quatre décimales, signe et exposant compris, est remplacé
+  par son jeton, compté pour un caractère ; la longueur brute du texte canonique passe aux traits de contenu (annexe H, écart 2) ;
+- pour chacune des quinze exactitudes : A observée, σ₀ et moyenne des exactitudes sous 1 000 permutations des étiquettes (entre
+  lois pour les deux audits de lois ; entre suites pour les trois audits des mondes par dose, les mondes d'une suite gardant une
+  étiquette commune), cinq plis retirés à chaque permutation, et le seuil 0,55 + 2 σ₀ (section « Seuil », règle calibrée) ;
+- lecture : les deux exactitudes de forme des audits de lois à la lettre de la version 6 (au-dessus de 0,55, arrêt) ; les trois
+  des audits des mondes par dose en trois lectures (au plus 0,55 tenue ; au-dessus de 0,55 + 2 σ₀ arrêt ; entre les deux,
+  « non départagée du hasard à cette taille », qui lie l'étage payant) ; contenu et réunis rapportés, liant l'étage payant
+  au-dessus de 0,55 ;
+- arrêt (`ArretAudit`) sur un pli d'entraînement privé d'une classe, un centre de classe non fini ou une exactitude qui ne peut
+  être calculée (moins de cinq exemples d'une classe), à la lecture observée comme sous permutation (note D9 ; version 8).
 """
 
 import hashlib
@@ -21,18 +34,37 @@
 
 import numpy as np
 
+from .constantes import EXEMPLES_MIN_PAR_CLASSE, PERMUTATIONS_AUDIT
+
 SEUIL_MARGE = 0.25
 PLANCHER_AUDIT = 1e-12
 EXACTITUDE_MAX = 0.55
 CASES = 64
 PAIRES_DE_DOSES = ((0.0, 0.25), (0.0, 0.5), (0.25, 0.5))
 JEUX_DE_TRAITS = ("forme", "contenu", "reunis")
+PLIS = 5
+AUDITS_DE_LOIS = ("vraies_contre_fausses", "dependantes_contre_independantes")
+AUDITS_DES_DOSES = tuple(f"mondes_dose_{a}_contre_{b}" for a, b in PAIRES_DE_DOSES)
+AUDITS = AUDITS_DE_LOIS + AUDITS_DES_DOSES
+JETON_D_UN_NOMBRE_EN_CARACTERES = "#"  # un caractère (annexe H, écart 2) ; seule sa longueur compte
+
+# lectures d'une exactitude (section « Seuil »)
+TENUE = "tenue"
+ARRET = "arrêt"
+NON_DEPARTAGEE = "non départagée du hasard à cette taille"
+SIGNALEE = "signalée"
+AU_PLUS = "au plus 0,55"
+MENTION = "générateur non audité pour l'étage payant"
 
 
 class AuditRefuse(ValueError):
     pass
 
 
+class ArretAudit(RuntimeError):
+    """Arrêt de l'audit de présentation (section « Seuil », versions 7 et 8 ; note D9 ; liste d'arrêt, point 2)."""
+
+
 # --- évaluateur indépendant ---------------------------------------------------------------------------------------------------
 
 
@@ -150,29 +182,49 @@
 _JETON = re.compile(r"[A-Za-z_]+|-?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|[^\sA-Za-z_\d]")
 
 
+def _nombre_long(j):
+    """Un jeton de nombre (signe et exposant compris) d'au moins quatre décimales : celui que le jeton unique remplace."""
+    if not (j[0].isdigit() or (j[0] == "-" and len(j) > 1)):
+        return False
+    mant = j.split("e")[0].split("E")[0]
+    dec = mant.split(".")[1] if "." in mant else ""
+    return len(dec) >= 4
+
+
 def jetons(texte):
     for j in _JETON.findall(texte):
-        if j[0].isdigit() or (j[0] == "-" and len(j) > 1):
-            mant = j.split("e")[0].split("E")[0]
-            dec = mant.split(".")[1] if "." in mant else ""
-            yield "<nombre>" if len(dec) >= 4 else j
-        else:
-            yield j
+        yield "<nombre>" if _nombre_long(j) else j
+
+
+def texte_aux_nombres_remplaces(texte):
+    """Code v4 (annexe H, écart 2 ; nœud 1, option (a)) : le texte où chaque nombre d'au moins quatre décimales, signe et
+    exposant compris, est remplacé par son jeton, compté pour un caractère. Les nombres sont ceux que `jetons` lit."""
+    morceaux, fin = [], 0
+    for m in _JETON.finditer(texte):
+        if _nombre_long(m.group(0)):
+            morceaux += [texte[fin:m.start()], JETON_D_UN_NOMBRE_EN_CARACTERES]
+            fin = m.end()
+    morceaux.append(texte[fin:])
+    return "".join(morceaux)
 
 
 def traits_de_forme(texte):
     """Comptes des jetons du texte canonique répartis en 64 cases (tout nombre d'au moins quatre décimales comptant pour un même
-    jeton), et la longueur du texte."""
+    jeton), et la longueur du texte où chacun de ces nombres est remplacé par ce jeton, compté pour un caractère (code v4 ; la
+    longueur brute, qui lit le signe des nombres, est un trait de contenu)."""
     v = np.zeros(CASES + 1)
     for j in jetons(texte):
         v[int.from_bytes(hashlib.sha256(j.encode("utf-8")).digest()[:4], "big") % CASES] += 1
-    v[CASES] = float(len(texte))
+    v[CASES] = float(len(texte_aux_nombres_remplaces(texte)))
     return v
 
 
-def traits_de_contenu(loi, Z, G):
+def traits_de_contenu(loi, Z, G, texte):
     """Pour chaque sous-population : norme des poids, norme des biais, entropie moyenne de la loi (nats) sur les instances de
-    l'oracle du monde dans cette sous-population."""
+    l'oracle du monde dans cette sous-population ; puis, pour la loi entière, la longueur brute de son texte canonique, en
+    caractères (code v4, annexe H, écart 2). `texte` doit être le texte canonique de `loi`, sinon refus."""
+    if texte != _cle(loi):
+        raise AuditRefuse("audit : le texte donné n'est pas le texte canonique de la loi (longueur brute)")
     P = probas_audit(loi, Z, G)
     G = np.asarray(G)
     out = []
@@ -181,39 +233,158 @@
         H = -np.einsum("nk,nk->n", P[G == g], np.log(P[G == g]))
         out += [float(np.linalg.norm(np.array(s["poids"], dtype=float))), float(np.linalg.norm(np.array(s["biais"], dtype=float))),
                 float(H.mean())]
+    out.append(float(len(texte)))
     return np.array(out)
 
 
-def exactitude_equilibree(X, y, rng, plis=5):
-    """Plus proche centre de classe sur des traits centrés et réduits (moyenne et écart-type du pli d'entraînement), validation
-    croisée à `plis` plis ; exactitude équilibrée. None si moins de deux classes ou trop peu d'exemples."""
-    X, y = np.asarray(X, dtype=float), np.asarray(y)
+def _indices_de_classe(y):
+    """Les deux classes triées et l'indice de classe de chaque exemple. Arrêt si l'exactitude ne peut être calculée : pas
+    exactement deux classes, ou moins de cinq exemples d'une classe (section « Seuil », version 8 ; le code v3 rendait None)."""
+    y = np.asarray(y)
     classes = sorted(set(y.tolist()))
-    if len(classes) != 2 or len(y) < 2 * plis or min(int(np.sum(y == c)) for c in classes) < plis:
-        return None
-    pli = np.empty(len(y), dtype=int)
-    pli[rng.permutation(len(y))] = np.arange(len(y)) % plis
-    pred = np.empty(len(y), dtype=object)
+    if len(classes) != 2:
+        raise ArretAudit(f"exactitude non calculable : {len(classes)} classe(s) au lieu de deux : arrêt de l'audit "
+                         "(section « Seuil », version 8 ; liste d'arrêt, point 2)")
+    yi = np.array([classes.index(v) for v in y.tolist()], dtype=int)
+    _exiger_calculable(yi)
+    return classes, yi
+
+
+def _exiger_calculable(yi):
+    comptes = [int(np.sum(yi == c)) for c in (0, 1)]
+    if min(comptes) < EXEMPLES_MIN_PAR_CLASSE:
+        raise ArretAudit(f"exactitude non calculable : moins de {EXEMPLES_MIN_PAR_CLASSE} exemples d'une classe ({comptes}) : "
+                         "arrêt de l'audit (section « Seuil », version 8 ; liste d'arrêt, point 2)")
+
+
+def _exactitude(X, yi, rng, plis):
+    """Plus proche centre de classe, validation croisée à `plis` plis tirés par une permutation semée, sans stratification ;
+    exactitude équilibrée. Arrêt sur un pli d'entraînement privé d'une classe ou un centre de classe non fini (note D9)."""
+    n = len(yi)
+    pli = np.empty(n, dtype=int)
+    pli[rng.permutation(n)] = np.arange(n) % plis
+    pred = np.empty(n, dtype=int)
     for k in range(plis):
         tr, te = pli != k, pli == k
+        ytr = yi[tr]
+        for c in (0, 1):
+            if not np.any(ytr == c):
+                raise ArretAudit(f"pli d'entraînement {k} privé d'une classe : arrêt de l'audit (note D9 ; liste d'arrêt, "
+                                 "point 2)")
         mu, sd = X[tr].mean(axis=0), X[tr].std(axis=0)
         sd = np.where(sd > 0, sd, 1.0)
         Xt, Xe = (X[tr] - mu) / sd, (X[te] - mu) / sd
-        centres = [Xt[y[tr] == c].mean(axis=0) for c in classes]
+        centres = [Xt[ytr == c].mean(axis=0) for c in (0, 1)]
+        if not all(np.all(np.isfinite(c)) for c in centres):
+            raise ArretAudit(f"centre de classe non fini au pli {k} : arrêt de l'audit (note D9 ; liste d'arrêt, point 2)")
         D = np.stack([((Xe - c) ** 2).sum(axis=1) for c in centres], axis=1)
-        pred[te] = [classes[i] for i in D.argmin(axis=1)]
-    return float(np.mean([np.mean(pred[y == c] == c) for c in classes]))
+        pred[te] = D.argmin(axis=1)
+    return float(np.mean([np.mean(pred[yi == c] == c) for c in (0, 1)]))
 
 
-def audit_presentation(mondes_audites, rng):
-    """`mondes_audites` : liste de dicts {"dose", "lois": [(texte canonique, loi, type, dependante)], "Z", "G"} — les mondes
-    cibles et finaux des suites de la couche « audit ». Rend {jeu de traits : {audit : exactitude}} (quinze valeurs), la liste
-    des exactitudes de forme au-dessus de 0,55 (`arret`) et celle des exactitudes de contenu ou réunies au-dessus de 0,55
-    (`signalement`)."""
+def exactitude_equilibree(X, y, rng, plis=PLIS):
+    """Plus proche centre de classe sur des traits centrés et réduits (moyenne et écart-type du pli d'entraînement ; un trait de
+    variance nulle est centré sans être réduit), validation croisée à `plis` plis ; exactitude équilibrée. Code v4 : arrêt
+    (`ArretAudit`) si elle ne peut être calculée (moins de cinq exemples d'une classe), si un pli d'entraînement est privé d'une
+    classe ou si un centre n'est pas fini — jamais None."""
+    _, yi = _indices_de_classe(y)
+    return _exactitude(np.asarray(X, dtype=float), yi, rng, plis)
+
+
+def permuter_les_etiquettes(yi, groupes, rng):
+    """Une permutation des étiquettes : entre exemples si `groupes` vaut None (audits de lois) ; sinon entre groupes, chaque
+    groupe (une suite) gardant une étiquette commune (audits des mondes par dose). Les exemples d'un groupe doivent avoir la même
+    étiquette, sinon refus."""
+    yi = np.asarray(yi)
+    if groupes is None:
+        return yi[rng.permutation(len(yi))]
+    groupes = list(groupes)
+    if len(groupes) != len(yi):
+        raise AuditRefuse("permutation entre suites : un identifiant de suite par exemple est exigé")
+    etiquette = {}
+    for g, v in zip(groupes, yi.tolist()):
+        if etiquette.setdefault(g, v) != v:
+            raise AuditRefuse(f"permutation entre suites : les mondes de la suite {g!r} n'ont pas la même étiquette")
+    ids = sorted(etiquette)
+    perm = rng.permutation(len(ids))
+    nouvelle = {ids[i]: etiquette[ids[int(perm[i])]] for i in range(len(ids))}
+    return np.array([nouvelle[g] for g in groupes], dtype=yi.dtype)
+
+
+def sous_permutation(X, y, rng, permutations, groupes=None, plis=PLIS):
+    """σ₀ (écart-type, ddof = 1) et moyenne de l'exactitude sous `permutations` permutations des étiquettes ; mêmes traits, même
+    classifieur, plis retirés à chaque permutation par le même `rng`. Les arrêts de la lecture observée valent ici aussi."""
+    if isinstance(permutations, bool) or not isinstance(permutations, int) or permutations < 2:
+        raise AuditRefuse(f"permutations : entier ≥ 2 attendu (reçu {permutations!r})")
+    X = np.asarray(X, dtype=float)
+    _, yi = _indices_de_classe(y)
+    vals = np.empty(permutations)
+    for p in range(permutations):
+        yp = permuter_les_etiquettes(yi, groupes, rng)
+        _exiger_calculable(yp)
+        vals[p] = _exactitude(X, yp, rng, plis)
+    return {"sigma0": float(vals.std(ddof=1)), "moyenne_permutee": float(vals.mean())}
+
+
+def lecture(jeu, audit, A, sigma0):
+    """La lecture d'une exactitude (section « Seuil » ; GO-2026-11-20-11). Forme, audits de lois : lettre de la version 6
+    (au-dessus de 0,55, arrêt). Forme, audits des mondes par dose : règle calibrée (au plus 0,55, tenue ; au-dessus de
+    0,55 + 2 σ₀, arrêt ; entre les deux, non départagée du hasard à cette taille). Contenu et réunis : rapportées ; au-dessus de
+    0,55, signalées (elles lient l'étage payant)."""
+    if jeu not in JEUX_DE_TRAITS or audit not in AUDITS:
+        raise AuditRefuse(f"lecture : exactitude inconnue {jeu}/{audit}")
+    if jeu != "forme":
+        return SIGNALEE if A > EXACTITUDE_MAX else AU_PLUS
+    if audit in AUDITS_DES_DOSES:
+        if A <= EXACTITUDE_MAX:
+            return TENUE
+        return ARRET if A > EXACTITUDE_MAX + 2.0 * sigma0 else NON_DEPARTAGEE
+    return ARRET if A > EXACTITUDE_MAX else TENUE
+
+
+def lire_audit(table):
+    """`table` : {jeu : {audit : {"A", "sigma0", …}}} pour les quinze exactitudes, exactement. Rend la lecture de chacune, la
+    liste des arrêts (forme), celle des exactitudes de forme non départagées (audits des doses), celle des exactitudes de
+    contenu ou réunies au-dessus de 0,55, et la mention qui lie l'étage payant."""
+    if sorted(table) != sorted(JEUX_DE_TRAITS) or any(sorted(table[j]) != sorted(AUDITS) for j in JEUX_DE_TRAITS):
+        raise AuditRefuse("lecture : les quinze exactitudes sont exigées, et elles seules")
+    lectures, arret, non_departagees, signalement = {}, [], [], []
+    for jeu in JEUX_DE_TRAITS:
+        lectures[jeu] = {}
+        for audit in AUDITS:
+            e = table[jeu][audit]
+            l = lecture(jeu, audit, e["A"], e["sigma0"])
+            lectures[jeu][audit] = l
+            nom = f"{jeu}/{audit}"
+            if l == ARRET:
+                arret.append(nom)
+            elif l == NON_DEPARTAGEE:
+                non_departagees.append(nom)
+            elif l == SIGNALEE:
+                signalement.append(nom)
+    return {"lectures": lectures, "arret": sorted(arret), "non_departagees": sorted(non_departagees),
+            "signalement": sorted(signalement), "mention": MENTION if (signalement or non_departagees) else None}
+
+
+def audit_presentation(mondes_audites, rng, rng_permutation, permutations=PERMUTATIONS_AUDIT):
+    """`mondes_audites` : liste de dicts {"dose", "suite", "lois": [(texte canonique, loi, type, dependante)], "Z", "G"} — les
+    mondes cibles et finaux des suites de la couche « audit », chacun avec l'identifiant de sa suite. `rng` tire les plis de la
+    lecture observée (même ordre et même flux qu'au code v3) ; `rng_permutation` (couche « audit », rôle « permutation ») tire
+    les permutations et leurs plis. Rend les quinze exactitudes observées (`exactitudes`), la table (A, σ₀, moyenne permutée,
+    seuil 0,55 + 2 σ₀, lecture) des quinze, et la lecture (`arret`, `non_departagees`, `signalement`, `mention`). Arrête
+    (`ArretAudit`) sur un pli privé d'une classe, un centre non fini ou une exactitude non calculable."""
     lignes = []  # (dose, monde, type, dependante, forme, contenu)
+    suite_du_monde, dose_de_la_suite = [], {}
     for k, m in enumerate(mondes_audites):
+        if "suite" not in m:
+            raise AuditRefuse("audit de présentation : l'identifiant de la suite de chaque monde est exigé (permutation entre "
+                              "suites)")
+        if dose_de_la_suite.setdefault(m["suite"], float(m["dose"])) != float(m["dose"]):
+            raise AuditRefuse(f"audit de présentation : la suite {m['suite']!r} porte deux doses")
+        suite_du_monde.append(m["suite"])
         for texte, loi, typ, dep in m["lois"]:
-            lignes.append((float(m["dose"]), k, typ, bool(dep), traits_de_forme(texte), traits_de_contenu(loi, m["Z"], m["G"])))
+            lignes.append((float(m["dose"]), k, typ, bool(dep), traits_de_forme(texte),
+                           traits_de_contenu(loi, m["Z"], m["G"], texte)))
 
     def X(sel, jeu):
         if jeu == "forme":
@@ -222,22 +393,35 @@
             return [l[5] for l in sel]
         return [np.concatenate([l[4], l[5]]) for l in sel]
 
-    out = {}
+    donnees = {}  # (jeu, audit) : (traits, étiquettes, groupes de la permutation)
     for jeu in JEUX_DE_TRAITS:
-        r = {}
-        r["vraies_contre_fausses"] = exactitude_equilibree(X(lignes, jeu), [l[2] for l in lignes], rng)
+        donnees[(jeu, "vraies_contre_fausses")] = (np.asarray(X(lignes, jeu), dtype=float), [l[2] for l in lignes], None)
         vd = [l for l in lignes if l[2] == "vraie" and l[0] > 0]
-        r["dependantes_contre_independantes"] = exactitude_equilibree(X(vd, jeu), [l[3] for l in vd], rng)
+        donnees[(jeu, "dependantes_contre_independantes")] = (np.asarray(X(vd, jeu), dtype=float), [l[3] for l in vd], None)
         for d1, d2 in PAIRES_DE_DOSES:
-            Xm, ym = [], []
+            Xm, ym, gm = [], [], []
             for k in sorted({l[1] for l in lignes if l[0] in (d1, d2)}):
                 sel = [l for l in lignes if l[1] == k]
                 Xm.append(np.mean(X(sel, jeu), axis=0))
                 ym.append(sel[0][0])
-            r[f"mondes_dose_{d1}_contre_{d2}"] = exactitude_equilibree(Xm, ym, rng)
-        out[jeu] = r
-    arret = sorted(f"forme/{a}" for a, v in out["forme"].items() if v is not None and v > EXACTITUDE_MAX)
-    signalement = sorted(f"{j}/{a}" for j in ("contenu", "reunis") for a, v in out[j].items() if v is not None and v > EXACTITUDE_MAX)
-    non_calculees = sorted(f"{j}/{a}" for j in JEUX_DE_TRAITS for a, v in out[j].items() if v is None)
-    return {"exactitudes": out, "arret": arret, "signalement": signalement, "non_calculees": non_calculees,
-            "mention": "générateur non audité pour l'étage payant" if signalement else None}
+                gm.append(suite_du_monde[k])
+            donnees[(jeu, f"mondes_dose_{d1}_contre_{d2}")] = (np.asarray(Xm, dtype=float), ym, gm)
+    exactitudes = {}
+    for jeu in JEUX_DE_TRAITS:  # lecture observée : même ordre de tirage des plis que le code v3
+        exactitudes[jeu] = {a: exactitude_equilibree(donnees[(jeu, a)][0], donnees[(jeu, a)][1], rng) for a in AUDITS}
+    table = {}
+    for jeu in JEUX_DE_TRAITS:
+        table[jeu] = {}
+        for a in AUDITS:
+            Xa, ya, ga = donnees[(jeu, a)]
+            p = sous_permutation(Xa, ya, rng_permutation, permutations, ga)
+            table[jeu][a] = {"A": exactitudes[jeu][a], "sigma0": p["sigma0"], "moyenne_permutee": p["moyenne_permutee"],
+                             "seuil_calibre": EXACTITUDE_MAX + 2.0 * p["sigma0"], "permutations": permutations,
+                             "permutation": "entre lois" if ga is None else "entre suites",
+                             "unites_permutees": len(ya) if ga is None else len(set(ga))}
+    lu = lire_audit(table)
+    for jeu in JEUX_DE_TRAITS:
+        for a in AUDITS:
+            table[jeu][a]["lecture"] = lu["lectures"][jeu][a]
+    return {"exactitudes": exactitudes, "table": table, "arret": lu["arret"], "non_departagees": lu["non_departagees"],
+            "signalement": lu["signalement"], "mention": lu["mention"]}
```

#### `2-constantes.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/constantes.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/constantes.py
@@ -64,6 +64,12 @@
 EXACTITUDE_EQUILIBREE_MAX = 0.55
 SUITES_AUDIT_PAR_DOSE = 50
 PLIS_AUDIT = 5
+PERMUTATIONS_AUDIT = 1_000  # code v4 : section « Seuil », règle calibrée (version 8) — σ₀ par 1 000 permutations
+EXEMPLES_MIN_PAR_CLASSE = 5  # code v4 : moins de cinq exemples d'une classe, exactitude non calculable, arrêt (version 8)
+
+# B7 bis et garde 27 (version 7, annexe H, écart 1 ; GO-2026-11-20-11, dose (a)) — code v4 : le jeu de sources de la garde 27
+# se construit et se joue à cette dose, et à elle seule (étape 4, `etapes.etape_4_jeu_de_la_garde_27`)
+DOSE_JEU_GARDE_27 = 0.25
 CASES_DE_FORME = 64
 INSTANCES_ORACLE = 4000
 SEUIL_APPARIEMENT_NAT = 0.05
```

#### `3-etalonnage.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
@@ -10,6 +10,11 @@
 
 Garde 22 : étalonner n'est pas lire un critère. Pendant l'étalonnage, le verrou du test est levé (tout appel au test lève), et
 la sortie n'a que des écarts moyens, des écarts-types et des réglages (`CLES_PERMISES`) ; tout autre champ arrête.
+
+Code v4, note D8 (B7, version 7) : un écart-type entre jumelles nul ou non fini, ou une taille réduite non finie, arrête
+l'étalonnage (`ArretEtalonnage`, avec sa cause) ; ce n'est pas « non atteignable », qui se dit d'une taille que le réglage maximal
+n'atteint pas. Le contrôle porte sur l'écart-type réuni (celui qui divise l'écart moyen et qui est gelé), à chaque évaluation de
+la dichotomie comme pour les proposeurs sans réglage.
 """
 
 import contextlib
@@ -97,6 +102,18 @@
     return e, (e / s if s > 0 else float("nan")), s
 
 
+def exiger_ecart_type_et_taille_finis(ecart_type, taille_reduite=None, cas=""):
+    """Note D8 (code v4) : arrêt de l'étalonnage si l'écart-type entre jumelles réuni est nul ou non fini, ou si la taille
+    réduite est non finie ; jamais « non atteignable », jamais une case rangée en silence."""
+    if not (math.isfinite(ecart_type) and ecart_type > 0.0):
+        raise ArretEtalonnage(f"note D8 : écart-type entre jumelles nul ou non fini ({ecart_type!r}) {cas}: arrêt de "
+                              "l'étalonnage (ce n'est pas « non atteignable »)")
+    if taille_reduite is not None and not math.isfinite(taille_reduite):
+        raise ArretEtalonnage(f"note D8 : taille réduite non finie ({taille_reduite!r}) {cas}: arrêt de l'étalonnage (ce "
+                              "n'est pas « non atteignable »)")
+    return True
+
+
 def _bras(dose, contraste):
     return ("2", "3") if (dose == 0.0 and contraste == "heritage") else ("1", "2", "3")
 
@@ -112,6 +129,7 @@
         def evaluer(x):
             moy, sd = jumelles(graines, couche, base, fabrique(x), dose, taux, f, S, bras)
             e, t, s = taille(moy, sd, contraste)
+            exiger_ecart_type_et_taille_finis(s, t, f"({nom}, dose {dose}, cible {cible}, réglage {x!r}) ")
             return e, t, s, sd, moy
 
         e, t, s, sd, moy = evaluer(haut)
@@ -149,6 +167,7 @@
                 **(base_en_plus or {}))
     with verrou():
         moy, sd = jumelles(graines, couche, base, prop, dose, taux, f, S, bras, repere, regle, repli)
+    exiger_ecart_type_et_taille_finis(ecart_type_reuni(sd), None, f"({nom}, dose {dose}, taux {taux}) ")
     ligne = {"proposeur": nom, "dose": dose, "taux": taux, "repere": repere, "retrait": regle, "repli": repli, "sources": S,
              "ecart_type_jumelles": ecart_type_reuni(sd), "ecart_type_jumelles_par_bras": sd, "ecarts_moyens_par_bras": moy}
     verifier_sortie(ligne)
```

#### `4-etapes.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/etapes.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/etapes.py
@@ -3,7 +3,10 @@
 - `plan_des_cases` : les cases des familles A à H de B8, à partir du fichier des réglages ; une cible non atteignable est
   écrite « non atteignable » et ne se tire pas.
 - `etape_4` : la couche mécanique (24 sources par dose et par proposeur, réglages de l'étape 4 au milieu des plages), les
-  fréquences M12, l'accord avec l'étage de l'organisme sur deux sources par dose et par proposeur, S8 (i).
+  fréquences M12, l'accord avec l'étage de l'organisme sur deux sources par dose et par proposeur, S8 (i). Bras 1 à 3 seuls.
+- `etape_4_jeu_de_la_garde_27` (code v4) : à l'étape 4 aussi, le jeu de sources de la garde 27 (B7 bis : bras 1 à 3, puis 4a et
+  4b sur les copies scellées de la source étrangère), à la dose `DOSE_JEU_GARDE_27` (0,25) et à elle seule ; le proposeur et le
+  nombre de sources, que le texte ne dit pas, sont des paramètres sans défaut.
 - `etape_6_bis_et_7` : la couche mécanique rejouée aux réglages gelés sous des étiquettes disjointes, puis la garde S8 (ii).
 - `etape_8` : les tirages décisifs de toutes les cases, en un seul lancement, aucune case lue avant que toutes soient
   écrites et scellées ; `cases_a_confirmer` et `etape_9` : la règle de C1 et de C4.
@@ -19,8 +22,9 @@
 from . import equivalence as EQ
 from . import frequences as FR
 from . import mecanique as MC
+from . import mondes as MO
 from . import proposeurs as P
-from .constantes import (DOSES, DOSES_NON_NULLES, FORCES_GENERALISTE, FORCES_SUIVEUR, FORCE_REFERENCE_SUIVEUR,
+from .constantes import (DOSE_JEU_GARDE_27, DOSES, DOSES_NON_NULLES, FORCES_GENERALISTE, FORCES_SUIVEUR, FORCE_REFERENCE_SUIVEUR,
                          GRILLE_SOURCES, GRILLE_SOURCES_DOSE_NULLE, REGLAGES_ETAPE_4, REPERES_LECTURE, SEUIL_DE_RETRAIT_SUR_10000,
                          SOURCES_COUCHE_MECANIQUE, SOURCES_FAMILLES_GRANDES, SOURCES_SOUS_ENSEMBLE_ORGANISME, TAILLES,
                          TAILLE_REFERENCE, TAUX_ECHEC_DECISIF, TAUX_ECHEC_TOUS, TIRAGES_CONFIRMATION, TIRAGES_PAR_CASE)
@@ -168,6 +172,24 @@
     return f, freqs.comptes(), garde_17
 
 
+def etape_4_jeu_de_la_garde_27(graines, couche, dossier, prop, sources, famille="etape-4-garde-27"):
+    """Code v4 (« Ce qui demande un code v4 », point 5 ; B7 bis ; garde 27) : le jeu de sources de la garde 27 se joue à l'étape
+    4, sur la couche mécanique, par cette fonction : `mondes.generer_jeu_avec_etrangeres` (marge face à la source étrangère
+    construite) puis `mecanique.jouer_jeu_diagnostic` (bras 1, 2, 3, puis 4a et 4b), à la dose `DOSE_JEU_GARDE_27` = 0,25,
+    fixée ici et vérifiée par les deux fonctions, qui arrêtent à toute autre dose ; taux d'échec de 0,25. `prop` (configuration
+    du proposeur) et `sources` (au moins deux) : le texte ne les dit pas ; ils sont donnés par l'appelant, sans défaut. Les
+    contrôles de la garde 27 (registre servi au bras 4a, copie servie au bras 4b, aucun bras du critère ne la reçoit) se font
+    en jouant. Rend {"dose", "sources", "proposeur", "suites", "premieres", "secondes"}."""
+    if isinstance(sources, bool) or not isinstance(sources, int) or sources < 2:
+        raise ArretEtapes(f"garde 27 : au moins deux sources (reçu {sources!r})")
+    bases = [dict(couche=couche, famille=famille, proposeur=prop["nom"], dose=DOSE_JEU_GARDE_27, source=k)
+             for k in range(sources)]
+    suites = MO.generer_jeu_avec_etrangeres(graines, bases, DOSE_JEU_GARDE_27)
+    premieres, secondes = MC.jouer_jeu_diagnostic(graines, bases, prop, DOSE_JEU_GARDE_27, TAUX_ECHEC_DECISIF, dossier, suites)
+    return {"dose": DOSE_JEU_GARDE_27, "sources": sources, "proposeur": prop["nom"], "suites": suites, "premieres": premieres,
+            "secondes": secondes}
+
+
 def etape_6_bis_et_7(graines, couche, dossier, f, configurations, sources_mecaniques=SOURCES_COUCHE_MECANIQUE,
                      sources_statistiques=20_000, bras=("1", "2", "3")):
     """`configurations` : {(proposeur, dose) : configuration aux réglages gelés}. Rejoue la couche mécanique (étiquettes
```

#### `5-mecanique.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/mecanique.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/mecanique.py
@@ -13,8 +13,8 @@
 import numpy as np
 
 from .comparateur import apparier, loi_du_texte
-from .constantes import (APPELS_PAR_GENERATION, CLASSES, DESCRIPTION_FIXE, GENERATIONS_COURSE_SOURCE, JUSTIFICATION_FIXE,
-                         MONDES_CIBLES_D_EVOLUTION, PREDICTION_FIXE, REPERE_LECTURE, TIENT, VERSION)
+from .constantes import (APPELS_PAR_GENERATION, CLASSES, DESCRIPTION_FIXE, DOSE_JEU_GARDE_27, GENERATIONS_COURSE_SOURCE,
+                         JUSTIFICATION_FIXE, MONDES_CIBLES_D_EVOLUTION, PREDICTION_FIXE, REPERE_LECTURE, TIENT, VERSION)
 from .cout import cout_hors_budget, cout_lecture_par_appel, nombre_de_tentatives, retrait_v1, retrait_v2, verifier_retrait
 from .enveloppe import cartes_d_un_lot, eprouver_generation, exiger_taux_egaux, lots_par_domaine
 from .executeur import Executeur, engagement, sceller
@@ -325,7 +325,11 @@
 def jouer_jeu_diagnostic(graines, bases, prop, dose, taux, dossier, suites, **kw):
     """B7 bis, garde 27 : un jeu de sources à sources étrangères (`mondes.generer_jeu_avec_etrangeres`) ; chaque source joue
     d'abord ses bras 1, 2, 3 (pour que son registre de course source et les vues de son bras 2 existent), puis les bras 4a et 4b
-    reçoivent les copies scellées de la source suivante. Rend la liste des sorties par source."""
+    reçoivent les copies scellées de la source suivante. Rend la liste des sorties par source. Code v4 (version 7, annexe H,
+    écart 1) : ce jeu ne se joue qu'à la dose 0,25 (`DOSE_JEU_GARDE_27`) ; toute autre dose arrête avant de jouer."""
+    if float(dose) != DOSE_JEU_GARDE_27:
+        raise ArretMecanique(f"garde 27 : le jeu de sources à sources étrangères ne se joue qu'à la dose {DOSE_JEU_GARDE_27} "
+                             f"(reçu {dose!r}) : arrêt (B7 bis, version 7)")
     S = len(bases)
     premieres = []
     for k in range(S):
```

#### `6-mondes.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/mondes.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/mondes.py
@@ -31,9 +31,9 @@
 
 from . import audit as AU
 from .comparateur import Oracle
-from .constantes import (DOMAINES_A_LOI_CIBLE, DOMAINES_A_LOI_SOURCE, DOMAINES_PAR_MONDE, EPISODES_PAR_DOMAINE, ESSAIS_PAR_MONDE,
-                         INSTANCES_ORACLE, MARGE_DE_CONSTRUCTION_NAT, MARGE_NAT, MONDES_CIBLES_D_EVOLUTION, PROPORTION_TRANCHE,
-                         SEUIL_APPARIEMENT_NAT, TIRAGES_PAR_LOI, TOURS_PAR_SUITE)
+from .constantes import (DOMAINES_A_LOI_CIBLE, DOMAINES_A_LOI_SOURCE, DOMAINES_PAR_MONDE, DOSE_JEU_GARDE_27, EPISODES_PAR_DOMAINE,
+                         ESSAIS_PAR_MONDE, INSTANCES_ORACLE, MARGE_DE_CONSTRUCTION_NAT, MARGE_NAT, MONDES_CIBLES_D_EVOLUTION,
+                         PERMUTATIONS_AUDIT, PROPORTION_TRANCHE, SEUIL_APPARIEMENT_NAT, TIRAGES_PAR_LOI, TOURS_PAR_SUITE)
 from .lois import (composer, instances_oracle, json_canonique, loi_fixe, loi_par_sous_population, matrice, softmax_aleatoire,
                    sous_loi, tirer_issues)
 
@@ -402,7 +402,12 @@
     de chaque source, séparés aussi de la source étrangère. Une suite retirée (tour neuf) change sa source : les mondes cibles
     de la source qui la prend pour étrangère sont alors refaits. Rend la liste des suites. Code v3, note D7 : les compteurs de
     B1 (iii) de chaque source (mondes sources tirés, mondes cibles tentés, suites refaites comprises, et tours retirés) sont
-    cumulés et portés par sa suite ; ils ne font que compter, aucun tirage n'en dépend."""
+    cumulés et portés par sa suite ; ils ne font que compter, aucun tirage n'en dépend. Code v4 (version 7, annexe H, écart 1) :
+    ce jeu ne se construit qu'à la dose 0,25 (`DOSE_JEU_GARDE_27`) ; la marge face à la source étrangère n'est ni construite ni
+    revendiquée à la dose 0,5 ; toute autre dose arrête avant tout tirage."""
+    if float(dose) != DOSE_JEU_GARDE_27:
+        raise ArretGenerateur(f"garde 27 : le jeu de sources à sources étrangères ne se construit qu'à la dose "
+                              f"{DOSE_JEU_GARDE_27} (reçu {dose!r}) : arrêt (B7 bis, version 7)")
     S = len(bases)
     if S < 2:
         raise ArretGenerateur("B7 bis : au moins deux sources")
@@ -507,18 +512,20 @@
 
 
 def mondes_pour_l_audit(suites):
-    """Ce que lit l'audit de présentation : les mondes cibles et finaux, avec le texte canonique de leurs lois plantées."""
+    """Ce que lit l'audit de présentation : les mondes cibles et finaux, avec le texte canonique de leurs lois plantées. Code
+    v4 : chaque monde porte l'identifiant de sa suite (son rang dans `suites`), pour la permutation entre suites."""
     out = []
-    for s in suites:
+    for i, s in enumerate(suites):
         for m in s.mondes_cibles():
-            out.append({"dose": m.dose, "Z": m.oracle.Z, "G": m.oracle.G,
+            out.append({"dose": m.dose, "suite": i, "Z": m.oracle.Z, "G": m.oracle.G,
                         "lois": [(l["texte"], l["loi"], l["type"], l["dependante"]) for _, l in sorted(m.lois.items())]})
     return out
 
 
 def distribution_des_traits_de_contenu(suites):
     """B1 (iii) : par sorte de loi plantée (vraie de la source, fausse de la source, dépendante, indépendante, fausse d'un monde
-    cible), moyenne et quartiles des six traits de contenu."""
+    cible), moyenne et quartiles des traits de contenu — les six de la version 6 et, code v4, la longueur brute du texte
+    canonique (annexe H, écart 2)."""
     par_sorte = {}
     for s in suites:
         for m in [s.source] + s.mondes_cibles():
@@ -527,8 +534,9 @@
                     sorte = "vraie-source" if l["type"] == "vraie" else "fausse-source"
                 else:
                     sorte = ("dependante" if l["dependante"] else "independante") if l["type"] == "vraie" else "fausse-cible"
-                par_sorte.setdefault(sorte, []).append(AU.traits_de_contenu(l["loi"], m.oracle.Z, m.oracle.G))
-    noms = ("norme_poids_g0", "norme_biais_g0", "entropie_g0", "norme_poids_g1", "norme_biais_g1", "entropie_g1")
+                par_sorte.setdefault(sorte, []).append(AU.traits_de_contenu(l["loi"], m.oracle.Z, m.oracle.G, l["texte"]))
+    noms = ("norme_poids_g0", "norme_biais_g0", "entropie_g0", "norme_poids_g1", "norme_biais_g1", "entropie_g1",
+            "longueur_brute")
     out = {}
     for sorte, v in sorted(par_sorte.items()):
         a = np.array(v)
@@ -538,26 +546,52 @@
     return out
 
 
-def audit_du_generateur(graines, doses, suites_par_dose, rng_audit):
-    """Étape 3 : `suites_par_dose` suites par dose sous la couche « audit » ; marges rejugées sur chaque monde (déjà faites à la
-    construction par le module `audit`), ensemble exclu par construction, audit de présentation (quinze exactitudes), rejets
-    et taux d'acceptation, distribution des traits de contenu. Rend un rapport ; lève `ArretGenerateur` si une exactitude de
-    forme dépasse 0,55 (liste d'arrêt, point 2)."""
+def generer_suites_d_audit(graines, doses, suites_par_dose, couche="audit"):
+    """Étape 3, construction : `suites_par_dose` suites par dose sous la couche `couche` (« audit » ; les essais du code jouent
+    la couche « essai »). Rend (suites, compteurs cumulés de B1 (iii))."""
     suites, compteurs = [], Compteurs()
     for dose in doses:
         for k in range(suites_par_dose):
-            s = generer_suite(graines, dict(couche="audit", famille="audit", dose=dose, source=k), dose)
+            s = generer_suite(graines, dict(couche=couche, famille="audit", dose=dose, source=k), dose)
             suites.append(s)
             compteurs.ajouter(s.compteurs)
+    return suites, compteurs
+
+
+def juger_suites_d_audit(suites, compteurs, rng_audit, rng_permutation, permutations=PERMUTATIONS_AUDIT):
+    """Étape 3, jugement : ensemble exclu par construction, audit de présentation (quinze exactitudes, chacune avec σ₀, la
+    moyenne des exactitudes permutées et le seuil 0,55 + 2 σ₀ ; code v4), rejets et taux d'acceptation, distribution des traits
+    de contenu. Rend le rapport ; lève `ArretGenerateur` (liste d'arrêt, point 2), le rapport joint à l'exception quand il
+    existe (`rapport`), si une exactitude de forme d'un audit de lois dépasse 0,55, si une exactitude de forme d'un audit des
+    mondes par dose dépasse 0,55 + 2 σ₀, si une loi du monde final est celle de sa source, ou si l'audit de présentation arrête
+    (pli privé d'une classe, centre non fini, exactitude non calculable). Une exactitude de forme des doses entre 0,55 et
+    0,55 + 2 σ₀ n'arrête pas : elle est rapportée « non départagée du hasard à cette taille » et lie l'étage payant."""
     communs = {}
     for s in suites:
         c = AU.ensemble_exclu_par_construction([l["texte"] for l in s.finale.lois.values()],
                                                [l["texte"] for l in s.source.lois.values() if l["type"] == "vraie"])
         if c:
             communs[s.source.nom] = c
-    pres = AU.audit_presentation(mondes_pour_l_audit(suites), rng_audit)
+    try:
+        pres = AU.audit_presentation(mondes_pour_l_audit(suites), rng_audit, rng_permutation, permutations)
+    except AU.ArretAudit as e:
+        raise ArretGenerateur(f"audit du générateur en échec : {e}") from e
     rapport = {"presentation": pres, "lois_du_final_identiques_a_la_source": communs, "compteurs": compteurs.vers_dict(),
                "traits_de_contenu": distribution_des_traits_de_contenu(suites)}
     if pres["arret"] or communs:
-        raise ArretGenerateur(f"audit du générateur en échec : {pres['arret'] or communs} (liste d'arrêt, point 2)")
+        arret = ArretGenerateur(f"audit du générateur en échec : {pres['arret'] or communs} (liste d'arrêt, point 2)")
+        arret.rapport = rapport
+        raise arret
     return rapport
+
+
+def audit_du_generateur(graines, doses, suites_par_dose, rng_audit, rng_permutation=None, permutations=PERMUTATIONS_AUDIT,
+                        couche="audit"):
+    """Étape 3 : `suites_par_dose` suites par dose sous la couche « audit » ; marges rejugées sur chaque monde (déjà faites à la
+    construction par le module `audit`), puis `juger_suites_d_audit`. `rng_permutation` : par défaut la graine de la couche
+    `couche`, famille « audit », rôle « permutation » (section « Seuil », version 7). Rend un rapport ; lève `ArretGenerateur`
+    (liste d'arrêt, point 2)."""
+    suites, compteurs = generer_suites_d_audit(graines, doses, suites_par_dose, couche)
+    if rng_permutation is None:
+        rng_permutation = graines.g(couche=couche, famille="audit", role="permutation")
+    return juger_suites_d_audit(suites, compteurs, rng_audit, rng_permutation, permutations)
```

#### `7-tirages.py.diff`

```diff
--- code-v3/src/controle_ia/heritage_etage_processeur_v1/tirages.py
+++ code-v4/src/controle_ia/heritage_etage_processeur_v1/tirages.py
@@ -216,23 +216,69 @@
     return {"fichiers": emp, "duree_s": time.monotonic() - t0}
 
 
+def chemin_de_la_liste_des_etiquettes(chemin_manifeste):
+    """Le fichier de la liste des étiquettes, à côté du manifeste : `manifeste.json` → `manifeste-etiquettes.txt`."""
+    base = chemin_manifeste[:-len(".json")] if chemin_manifeste.endswith(".json") else chemin_manifeste
+    return base + "-etiquettes.txt"
+
+
 def ecrire_manifeste(chemin, configuration, graines, commit, fichiers_geles):
     """Règle R9 : un manifeste par run — configuration et son empreinte, versions, racine, étiquettes (nombre, empreinte de leur
-    liste triée, couches), commit, empreintes des fichiers gelés (fréquences M12, réglages)."""
+    liste triée, couches), commit, empreintes des fichiers gelés (fréquences M12, réglages). Code v4 (B8, version 7, choix 12) :
+    la liste entière des étiquettes, triée, une par ligne, jointes par un saut de ligne sans saut final (le texte même dont le
+    manifeste porte l'empreinte), est écrite dans un fichier scellé à côté du manifeste, avant lui ; le manifeste inscrit son nom
+    et son empreinte, égale à celle de la liste (elle se rejoue à la main par `sha256sum`)."""
     canon = json.dumps(configuration, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
     etiq = sorted(graines.etiquettes)
+    texte_liste = "\n".join(etiq).encode("utf-8")
+    chemin_liste = chemin_de_la_liste_des_etiquettes(chemin)
+    with open(chemin_liste, "xb") as fh:
+        fh.write(texte_liste)
+    sha_liste = _sceller(chemin_liste)
     m = {"version": VERSION, "preenregistrement_sha256": PREENREGISTREMENT_SHA256, "configuration": configuration,
          "configuration_sha256": hashlib.sha256(canon.encode("utf-8")).hexdigest(),
          "versions": {"python": platform.python_version(), "numpy": np.__version__},
          "racine": graines.racine if graines.racine is not None else RACINE_GRAINES, "commit": commit,
-         "etiquettes": {"nombre": len(etiq), "sha256": hashlib.sha256("\n".join(etiq).encode("utf-8")).hexdigest(),
-                        "couches": sorted({e.split("|", 1)[0] for e in etiq})},
+         "etiquettes": {"nombre": len(etiq), "sha256": hashlib.sha256(texte_liste).hexdigest(),
+                        "couches": sorted({e.split("|", 1)[0] for e in etiq}),
+                        "fichier": os.path.basename(chemin_liste), "fichier_sha256": sha_liste},
          "fichiers_geles": fichiers_geles}
     with open(chemin, "x", encoding="utf-8") as fh:
         fh.write(json.dumps(m, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
     return _sceller(chemin)
 
 
+def _lire_scelle(chemin):
+    """Les octets d'un fichier, après contrôle de son compagnon `.sha256` ; arrêt sinon."""
+    if not os.path.isfile(chemin) or not os.path.isfile(chemin + ".sha256"):
+        raise ArretTirages(f"fichier ou compagnon absent : {chemin}")
+    with open(chemin + ".sha256", encoding="ascii") as fh:
+        attendu = (fh.read().split() or [""])[0]
+    if _sha256(chemin) != attendu:
+        raise ArretTirages(f"empreinte différente de son compagnon : {chemin}")
+    with open(chemin, "rb") as fh:
+        return fh.read(), attendu
+
+
+def verifier_manifeste(chemin):
+    """Choix 12 (code v4) : rejoue l'empreinte de la liste des étiquettes. Le manifeste et la liste ont l'empreinte de leur
+    compagnon ; la liste a l'empreinte, le nombre de lignes et les couches que le manifeste inscrit, et elle est triée. Rend le
+    nombre d'étiquettes ; arrêt sinon."""
+    octets, _ = _lire_scelle(chemin)
+    m = json.loads(octets.decode("utf-8"))
+    e = m.get("etiquettes") or {}
+    chemin_liste = os.path.join(os.path.dirname(chemin), e.get("fichier") or "")
+    if not e.get("fichier") or chemin_liste != chemin_de_la_liste_des_etiquettes(chemin):
+        raise ArretTirages("manifeste : fichier de la liste des étiquettes non inscrit (choix 12)")
+    liste, sha = _lire_scelle(chemin_liste)
+    lignes = liste.decode("utf-8").split("\n") if liste else []
+    if (sha != e.get("fichier_sha256") or hashlib.sha256(liste).hexdigest() != e.get("sha256")
+            or len(lignes) != e.get("nombre") or lignes != sorted(lignes)
+            or sorted({x.split("|", 1)[0] for x in lignes}) != e.get("couches")):
+        raise ArretTirages("manifeste : la liste des étiquettes ne rejoue pas ce que le manifeste inscrit (choix 12)")
+    return len(lignes)
+
+
 def exiger_autorisation_pour(couche, graines):
     """Liste d'arrêt, point 1 : aucun tirage décisif ni de confirmation sans autorisation (vérifiée avant toute simulation)."""
     if couche in COUCHES_DECISIVES and graines.autorisation is None:
```

#### `8-test_heritage_etage_processeur_v1_mecanique.py.diff`

```diff
--- code-v3/tests/test_heritage_etage_processeur_v1_mecanique.py
+++ code-v4/tests/test_heritage_etage_processeur_v1_mecanique.py
@@ -2,7 +2,8 @@
 sain y est vide ; garde 13 (générateur et copies) ; gardes 23 et 24 (S8) ; garde 27 (bras de diagnostic) ; le multiplicateur de
 la tenue ne s'applique pas aux entrées étrangères du bras 4b ; huit fréquences et strate vide ; reproductibilité à l'octet d'une
 source. Graines de la couche « essai ». Code v3 : copie servie au bras 4b contrôlée (C2) ; strate du passage exigée comme
-`strates_requises` l'exige (C3) ; compteurs du jeu à sources étrangères (note D7)."""
+`strates_requises` l'exige (C3) ; compteurs du jeu à sources étrangères (note D7). Code v4 : le jeu de la garde 27 est joué
+par la fonction de l'étape 4 qui le porte, à la dose 0,25 fixée par une constante ; toute autre dose arrête."""
 
 import os
 
@@ -11,6 +12,7 @@
 
 from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, graines, prop
 from controle_ia.heritage_etage_processeur_v1 import equivalence as EQ
+from controle_ia.heritage_etage_processeur_v1 import etapes as EP
 from controle_ia.heritage_etage_processeur_v1 import executeur as EX
 from controle_ia.heritage_etage_processeur_v1 import frequences as FR
 from controle_ia.heritage_etage_processeur_v1 import mecanique as MC
@@ -18,7 +20,7 @@
 from controle_ia.heritage_etage_processeur_v1 import proposeurs as P
 from controle_ia.heritage_etage_processeur_v1 import registre as R
 from controle_ia.heritage_etage_processeur_v1 import statistique as ST
-from controle_ia.heritage_etage_processeur_v1.constantes import CLES_FREQUENCES, REGLAGES_ETAPE_4
+from controle_ia.heritage_etage_processeur_v1.constantes import CLES_FREQUENCES, DOSE_JEU_GARDE_27, REGLAGES_ETAPE_4
 
 LECTEUR = dict(K=REGLAGES_ETAPE_4["K"])
 
@@ -170,12 +172,33 @@
     assert any(fautif["bras"][b]["mesure"]["exclues_appariees"] for b in "123")
 
 
+def test_garde_27_dose_du_jeu_fixee_a_0_25(tmp_path):
+    """Code v4 (« Ce qui demande un code v4 », point 5) : le jeu de la garde 27 se construit et se joue à la dose
+    `DOSE_JEU_GARDE_27` = 0,25 et à elle seule ; toute autre dose arrête avant de tirer ou de jouer (bornes réduites et suites
+    vides : sans la garde, l'erreur serait une autre, et vite)."""
+    assert DOSE_JEU_GARDE_27 == 0.25
+    g = graines()
+    bases = [dict(couche="essai", famille="garde-27-dose", dose=0.5, source=k) for k in range(2)]
+    with pytest.raises(MO.ArretGenerateur, match="garde 27 : le jeu de sources"):
+        MO.generer_jeu_avec_etrangeres(g, bases, 0.5, bornes=MO.Bornes(1, 1, 1))
+    with pytest.raises(MC.ArretMecanique, match="garde 27 : le jeu de sources"):
+        MC.jouer_jeu_diagnostic(g, bases, prop("lecteur-tenue", tau=2.0), 0.5, 0.25, str(tmp_path / "dose-0.5"), [])
+    with pytest.raises(EP.ArretEtapes, match="au moins deux sources"):
+        EP.etape_4_jeu_de_la_garde_27(g, "essai", str(tmp_path / "une-source"), prop("lecteur-tenue", tau=2.0), 1)
+
+
 def test_garde_27_bras_de_diagnostic_et_tenue_sans_effet_au_bras_4b(tmp_path):
+    """Garde 27 ; code v4 : le jeu est joué par la fonction de l'étape 4 (`etapes.etape_4_jeu_de_la_garde_27`), à la dose 0,25
+    qu'elle fixe ; sous la famille « garde-27 », ses étiquettes sont celles de l'essai du code v3 (mêmes suites, mêmes sorties)."""
     g = graines()
     bases = [dict(couche="essai", famille="garde-27", proposeur="lecteur-tenue", dose=0.25, source=k) for k in range(2)]
-    suites = MO.generer_jeu_avec_etrangeres(g, bases, 0.25)
+    jeu = EP.etape_4_jeu_de_la_garde_27(g, "essai", str(tmp_path), prop("lecteur-tenue", tau=2.0), 2, famille="garde-27")
+    assert jeu["dose"] == DOSE_JEU_GARDE_27 and jeu["sources"] == 2 and jeu["proposeur"] == "lecteur-tenue"
+    suites, premieres, secondes = jeu["suites"], jeu["premieres"], jeu["secondes"]
+    assert all(m.dose == 0.25 for s in suites for m in [s.source] + s.mondes_cibles())
+    assert [sorted(p["bras"]) for p in premieres] == [["1", "2", "3"]] * 2
+    assert [sorted(p["bras"]) for p in secondes] == [["4a", "4b"]] * 2
     assert suites[0].etrangere is suites[1].source and suites[1].etrangere is suites[0].source
-    premieres, secondes = MC.jouer_jeu_diagnostic(g, bases, prop("lecteur-tenue", tau=2.0), 0.25, 0.25, str(tmp_path), suites)
     for k in range(2):
         e = premieres[(k + 1) % 2]
         r4a = secondes[k]["bras"]["4a"]["registre"]
```

#### `9-test_heritage_etage_processeur_v1_mondes.py.diff`

```diff
--- code-v3/tests/test_heritage_etage_processeur_v1_mondes.py
+++ code-v4/tests/test_heritage_etage_processeur_v1_mondes.py
@@ -1,7 +1,14 @@
 """Essais du générateur des mondes (B1) et de son audit : garde 25 (cas sains : générateur accepté, bornes gelées sans arrêt ;
 artefacts : deux lois plantées trop proches, dose inscrite dans la présentation, poids des dépendantes doublés, bornes ramenées à
 un tirage par loi et un essai par monde) ; marge face à la source étrangère (B7 bis) ; forme unique ; dose et paires. Audit à
-taille réduite seulement (quatre suites par dose ; l'audit à pleine taille est l'étape 3), graines « essai »."""
+taille réduite seulement (quatre suites par dose ; l'audit à pleine taille est l'étape 3), graines « essai ».
+
+Code v4 (préenregistrement v8) : longueur de forme sur le texte aux nombres remplacés, longueur brute parmi les traits de contenu
+(nœud 1) ; σ₀ par permutation, entre lois ou entre suites, et règle calibrée pour les seuls audits des mondes par dose, lettre
+de la version 6 pour les deux audits de lois (nœud 2) ; artefacts de la garde 25 : valeurs plantées dans la zone médiane
+(mention sans arrêt), exactitude de forme plantée à 0,56 dans un audit de lois (arrêt), signes des lois dépendantes changés
+(vus par le contenu, non par la forme), pli privé d'une classe et exactitude non calculable (arrêt) ; étape 3. Les essais
+jouent peu de permutations (`PERMUTATIONS_D_ESSAI`) ; la valeur gelée, 1 000, est celle de l'étape 3."""
 
 import itertools
 
@@ -12,9 +19,14 @@
 from controle_ia.heritage_etage_processeur_v1 import audit as AU
 from controle_ia.heritage_etage_processeur_v1 import lois as L
 from controle_ia.heritage_etage_processeur_v1 import mondes as MO
-from controle_ia.heritage_etage_processeur_v1.constantes import DOSES
+from controle_ia.heritage_etage_processeur_v1.constantes import DOSES, PERMUTATIONS_AUDIT
 
 SUITES_PAR_DOSE = 4
+PERMUTATIONS_D_ESSAI = 20
+
+
+def _rng_permutation(graine):
+    return np.random.default_rng(graine)
 
 
 def _suites(g, famille, **kw):
@@ -73,26 +85,185 @@
             for k in range(24):
                 loi = L.loi_par_sous_population(L.softmax_aleatoire(rng), L.softmax_aleatoire(rng))
                 lois.append((L.json_canonique(loi), loi, "vraie" if k < 12 else "fausse", k < d))
-            out.append({"dose": dose, "Z": Z, "G": G, "lois": lois})
+            out.append({"dose": dose, "suite": len(out) // 4, "Z": Z, "G": G, "lois": lois})  # quatre mondes par suite
     return out
 
 
+def _verifier_table(pres, permutations):
+    """Les quinze exactitudes portent A, σ₀, la moyenne des exactitudes permutées, le seuil 0,55 + 2 σ₀ et leur lecture, et
+    chaque lecture est celle de la règle (forme des lois à la lettre ; forme des doses calibrée ; contenu et réunis rapportés)."""
+    lignes = [(j, a, e) for j, d in pres["table"].items() for a, e in d.items()]
+    assert len(lignes) == 15 and sorted(pres["table"]) == sorted(AU.JEUX_DE_TRAITS)
+    for j, a, e in lignes:
+        assert e["A"] == pres["exactitudes"][j][a] and e["permutations"] == permutations
+        assert e["sigma0"] > 0 and e["seuil_calibre"] == 0.55 + 2 * e["sigma0"] and 0.0 <= e["moyenne_permutee"] <= 1.0
+        assert e["permutation"] == ("entre suites" if a.startswith("mondes_dose") else "entre lois")
+        if j != "forme":
+            attendu = AU.SIGNALEE if e["A"] > 0.55 else AU.AU_PLUS
+        elif a.startswith("mondes_dose"):
+            attendu = (AU.TENUE if e["A"] <= 0.55 else AU.ARRET if e["A"] > e["seuil_calibre"] else AU.NON_DEPARTAGEE)
+        else:
+            attendu = AU.ARRET if e["A"] > 0.55 else AU.TENUE
+        assert e["lecture"] == attendu, (j, a, e)
+        assert (f"{j}/{a}" in pres["arret"]) == (attendu == AU.ARRET)
+        assert (f"{j}/{a}" in pres["non_departagees"]) == (attendu == AU.NON_DEPARTAGEE)
+        assert (f"{j}/{a}" in pres["signalement"]) == (attendu == AU.SIGNALEE)
+    assert (pres["mention"] is not None) == bool(pres["signalement"] or pres["non_departagees"])
+
+
 def test_garde_25_audit_de_presentation_cas_sain():
-    pres = AU.audit_presentation(_mondes_sains_par_construction(300), np.random.default_rng(25))
-    assert pres["arret"] == [] and pres["signalement"] == [] and pres["mention"] is None, pres["exactitudes"]
-    assert pres["non_calculees"] == []
-    assert len([v for j in pres["exactitudes"].values() for v in j.values()]) == 15
+    """Cas sain de la garde 25 (B9 : « générateur sain : aucun arrêt »). Code v4 : aucune exactitude de forme n'arrête ni
+    n'est non départagée, et aucune des quinze ne s'écarte de la moyenne permutée de plus de trois σ₀. Les exactitudes de
+    contenu et réunies restent lues à la lettre (au-dessus de 0,55, signalées) sans calibrage : à cette taille, le seul hasard
+    peut en signaler une (vu au code v4 sur ces graines : « reunis/mondes_dose_0.25_contre_0.5 », 0,558, z = +2,4) ; ce n'est
+    pas un arrêt, et l'essai ne l'exige ni ne l'exclut (constat porté au rapport du code v4)."""
+    pres = AU.audit_presentation(_mondes_sains_par_construction(300), np.random.default_rng(25), _rng_permutation(2501),
+                                 PERMUTATIONS_D_ESSAI)
+    assert pres["arret"] == [] and pres["non_departagees"] == [], pres["table"]
+    assert all(abs(e["A"] - e["moyenne_permutee"]) <= 3 * e["sigma0"] for d in pres["table"].values() for e in d.values())
+    assert all(s.split("/")[0] in ("contenu", "reunis") for s in pres["signalement"])
+    _verifier_table(pres, PERMUTATIONS_D_ESSAI)
+    assert PERMUTATIONS_AUDIT == 1000
 
 
 def test_audit_de_presentation_du_generateur_de_b1_a_taille_reduite(saines):
     """Constat, sans seuil à cette taille (quatre suites par dose ; l'audit à pleine taille est l'étape 3) : les quinze
-    exactitudes se calculent sur les mondes du générateur constructif, et la distribution des traits de contenu par sorte de loi
-    est rapportée."""
-    pres = AU.audit_presentation(MO.mondes_pour_l_audit(saines), np.random.default_rng(25))
-    assert pres["non_calculees"] == []
-    assert len([v for j in pres["exactitudes"].values() for v in j.values()]) == 15
+    exactitudes se calculent sur les mondes du générateur constructif, chacune avec σ₀, la moyenne des exactitudes permutées et
+    le seuil calibré (code v4 ; « Ce qui demande un code v4 », point 7 : la moyenne permutée est rapportée), et la distribution
+    des traits de contenu par sorte de loi est rapportée, longueur brute comprise."""
+    mondes = MO.mondes_pour_l_audit(saines)
+    assert [m["suite"] for m in mondes] == [i for i in range(len(saines)) for _ in range(4)]
+    pres = AU.audit_presentation(mondes, np.random.default_rng(25), _rng_permutation(2502), PERMUTATIONS_D_ESSAI)
+    _verifier_table(pres, PERMUTATIONS_D_ESSAI)
+    n = 4 * SUITES_PAR_DOSE  # mondes cibles et finaux par dose
+    for j in AU.JEUX_DE_TRAITS:  # permutation entre suites (deux doses de quatre suites), entre lois sinon
+        assert all(pres["table"][j][a]["unites_permutees"] == 2 * SUITES_PAR_DOSE for a in AU.AUDITS_DES_DOSES)
+        assert pres["table"][j]["vraies_contre_fausses"]["unites_permutees"] == 3 * n * 24
+        assert pres["table"][j]["dependantes_contre_independantes"]["unites_permutees"] == 2 * n * 12
     dist = MO.distribution_des_traits_de_contenu(saines)
     assert set(dist) == {"vraie-source", "fausse-source", "dependante", "independante", "fausse-cible"}
+    assert all("longueur_brute" in v for v in dist.values())
+
+
+def test_longueur_de_forme_sur_le_texte_aux_nombres_remplaces():
+    """Nœud 1, option (a) : la longueur de forme compte chaque nombre d'au moins quatre décimales, signe et exposant compris,
+    pour un caractère ; les nombres plus courts restent écrits ; la longueur brute est le dernier trait de contenu."""
+    texte = '{"a":[-0.123456,0.5,-1e-05,-2.5000e-07,-0.1234],"b":"x"}'
+    assert AU.texte_aux_nombres_remplaces(texte) == '{"a":[#,0.5,-1e-05,#,#],"b":"x"}'
+    assert list(AU.jetons(texte)).count("<nombre>") == 3
+    v = AU.traits_de_forme(texte)
+    assert v[AU.CASES] == len('{"a":[#,0.5,-1e-05,#,#],"b":"x"}') and v[AU.CASES] != len(texte)
+    assert AU.traits_de_forme(texte.replace("-1e-05", "1e-05"))[AU.CASES] == v[AU.CASES] - 1  # un nombre court garde son signe
+    sans_signe = texte.replace("-0.123456", "0.123456").replace("-2.5000e-07", "2.5000e-07")
+    assert np.array_equal(AU.traits_de_forme(sans_signe), v)  # le signe d'un nombre long n'entre pas dans la forme
+    Z, G = L.instances_oracle(7, 200)
+    loi = L.loi_par_sous_population(L.softmax_aleatoire(np.random.default_rng(7)), L.softmax_aleatoire(np.random.default_rng(8)))
+    c = AU.traits_de_contenu(loi, Z, G, L.json_canonique(loi))
+    assert len(c) == 7 and c[6] == len(L.json_canonique(loi))
+    with pytest.raises(AU.AuditRefuse):
+        AU.traits_de_contenu(loi, Z, G, L.json_canonique(loi) + " ")
+
+
+def _table_plantee(A=0.5, sigma0=0.02, **changes):
+    """Une table plantée des quinze exactitudes (valeurs non tirées) ; `changes` : {"jeu/audit": (A, σ₀)}."""
+    t = {j: {a: {"A": A, "sigma0": sigma0} for a in AU.AUDITS} for j in AU.JEUX_DE_TRAITS}
+    for nom, (a, s) in changes.items():
+        j, au = nom.replace("__", "/").split("/")
+        t[j][au] = {"A": a, "sigma0": s}
+    return t
+
+
+def test_garde_25_lecture_calibree_sur_valeurs_plantees():
+    """Garde 25 (versions 7 et 8), valeurs plantées, non tirées : zone médiane d'un audit des mondes par dose, mention sans
+    arrêt ; au-dessus de 0,55 + 2 σ₀, arrêt ; un audit de lois lu à la lettre (0,56 avec σ₀ = 0,01 arrête, alors que la règle
+    calibrée ne l'aurait pas fait) ; contenu au-dessus de 0,55, signalement sans arrêt ; 0,55 tout juste, tenue."""
+    l = AU.lire_audit(_table_plantee())
+    assert l["arret"] == l["non_departagees"] == l["signalement"] == [] and l["mention"] is None
+    dose = "forme/mondes_dose_0.0_contre_0.5"
+    l = AU.lire_audit(_table_plantee(**{dose: (0.58, 0.02)}))
+    assert l["arret"] == [] and l["non_departagees"] == [dose] and l["mention"] == AU.MENTION
+    assert l["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == "non départagée du hasard à cette taille"
+    assert AU.lire_audit(_table_plantee(**{dose: (0.60, 0.02)}))["arret"] == [dose]
+    assert AU.lire_audit(_table_plantee(**{dose: (0.55, 0.0)}))["lectures"]["forme"]["mondes_dose_0.0_contre_0.5"] == AU.TENUE
+    for loi in ("forme/vraies_contre_fausses", "forme/dependantes_contre_independantes"):
+        l = AU.lire_audit(_table_plantee(**{loi: (0.56, 0.01)}))
+        assert l["arret"] == [loi] and l["non_departagees"] == []
+        assert AU.lecture("forme", "mondes_dose_0.25_contre_0.5", 0.56, 0.01) == AU.NON_DEPARTAGEE  # la règle des doses
+    l = AU.lire_audit(_table_plantee(**{"contenu/dependantes_contre_independantes": (0.6, 0.01),
+                                        "reunis/mondes_dose_0.0_contre_0.25": (0.9, 0.01)}))
+    assert l["arret"] == [] and l["signalement"] == ["contenu/dependantes_contre_independantes",
+                                                     "reunis/mondes_dose_0.0_contre_0.25"] and l["mention"] == AU.MENTION
+    t = _table_plantee()
+    del t["forme"]["vraies_contre_fausses"]
+    with pytest.raises(AU.AuditRefuse):
+        AU.lire_audit(t)
+
+
+class _RngPlante:
+    """Un générateur planté : `permutation` rend, tour à tour, les permutations données (pour placer les plis à la main)."""
+
+    def __init__(self, *perms):
+        self.perms, self.k = [np.asarray(p) for p in perms], 0
+
+    def permutation(self, n):
+        p = self.perms[self.k % len(self.perms)]
+        self.k += 1
+        assert len(p) == n
+        return p.copy()
+
+
+def _perm_qui_prive_le_pli_0(n=25):
+    """Les exemples 0 à 4 tombent tous dans le pli 0 (pli[perm[i]] = i mod 5)."""
+    perm = np.empty(n, dtype=int)
+    perm[[0, 5, 10, 15, 20]] = [0, 1, 2, 3, 4]
+    perm[[i for i in range(n) if i % 5]] = list(range(5, n))
+    return perm
+
+
+def test_garde_25_pli_prive_d_une_classe_et_exactitude_non_calculable_arretent():
+    rng = np.random.default_rng(3)
+    X = rng.normal(size=(25, 3))
+    y = [1] * 5 + [0] * 20
+    assert 0.0 <= AU.exactitude_equilibree(X, y, np.random.default_rng(4)) <= 1.0  # cas sain : calculée
+    with pytest.raises(AU.ArretAudit, match="privé d'une classe"):
+        AU.exactitude_equilibree(X, y, _RngPlante(_perm_qui_prive_le_pli_0()))
+    with pytest.raises(AU.ArretAudit, match="non calculable"):
+        AU.exactitude_equilibree(X[1:], y[1:], np.random.default_rng(4))  # quatre exemples d'une classe
+    with pytest.raises(AU.ArretAudit, match="non calculable"):
+        AU.exactitude_equilibree(X, [0] * 25, np.random.default_rng(4))  # une seule classe
+    Xn = X.copy()
+    Xn[0, 0] = np.nan
+    with pytest.raises(AU.ArretAudit, match="non fini"):
+        AU.exactitude_equilibree(Xn, y, np.random.default_rng(4))
+    # sous permutation aussi : étiquettes laissées en place, puis plis placés à la main
+    assert AU.sous_permutation(X, y, np.random.default_rng(5), 5)["sigma0"] > 0
+    with pytest.raises(AU.ArretAudit, match="privé d'une classe"):
+        AU.sous_permutation(X, y, _RngPlante(np.arange(25), _perm_qui_prive_le_pli_0()), 5)
+    with pytest.raises(AU.AuditRefuse):
+        AU.sous_permutation(X, y, np.random.default_rng(5), 1)
+
+
+def test_permutation_entre_suites_garde_l_etiquette_commune():
+    """Audits des mondes par dose : les étiquettes sont permutées entre suites, les mondes d'une suite gardant une étiquette
+    commune ; entre lois pour les audits de lois."""
+    yi = np.array([0] * 12 + [1] * 12)
+    groupes = [k // 4 for k in range(24)]
+    rng = np.random.default_rng(11)
+    vus = set()
+    for _ in range(50):
+        yp = AU.permuter_les_etiquettes(yi, groupes, rng)
+        assert sorted(yp.tolist()) == sorted(yi.tolist())
+        assert all(len({int(yp[i]) for i in range(24) if groupes[i] == g}) == 1 for g in set(groupes))
+        vus.add(tuple(yp.tolist()))
+    assert len(vus) > 1
+    yl = AU.permuter_les_etiquettes(yi, None, np.random.default_rng(12))
+    assert sorted(yl.tolist()) == sorted(yi.tolist())
+    assert any(len({int(yl[i]) for i in range(24) if groupes[i] == g}) == 2 for g in set(groupes))
+    with pytest.raises(AU.AuditRefuse):
+        AU.permuter_les_etiquettes(np.array([0, 1, 1, 1]), [0, 0, 1, 1], rng)
+    with pytest.raises(AU.AuditRefuse, match="identifiant de la suite"):
+        AU.audit_presentation([{k: v for k, v in m.items() if k != "suite"} for m in _mondes_sains_par_construction(2)],
+                              np.random.default_rng(1), np.random.default_rng(2), 2)
 
 
 def test_garde_25_deux_lois_trop_proches_le_monde_est_rejete(saines):
@@ -110,21 +281,76 @@
 
 
 def test_garde_25_dose_inscrite_dans_la_presentation_arret():
+    """Artefact : une dose inscrite dans la présentation ; l'exactitude de forme d'un audit des mondes par dose dépasse
+    0,55 + 2 σ₀ (règle calibrée, σ₀ par permutation entre suites) : arrêt."""
     g = graines()
     suites = _suites(g, "audit-dose-inscrite", variante="dose-inscrite")
-    pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(26))
+    pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(26), _rng_permutation(2601), 50)
     assert any(a.startswith("forme/mondes_dose") for a in pres["arret"])
-    assert max(v for k, v in pres["exactitudes"]["forme"].items() if k.startswith("mondes_dose")) > 0.55
+    assert any(e["A"] > e["seuil_calibre"] for k, e in pres["table"]["forme"].items() if k.startswith("mondes_dose"))
+    _verifier_table(pres, 50)
 
 
-def test_garde_25_poids_des_dependantes_doubles_signale():
+def test_garde_25_poids_des_dependantes_doubles_signale(saines):
+    """Artefact : les poids des lois dépendantes doublés par un générateur fautif planté ; exactitude de contenu au-dessus de
+    0,55, signalée. Code v4 : les mondes à dose nulle (du générateur sain) sont joints, sans quoi l'audit des mondes 0 contre
+    0,25 ne peut être calculé, ce qui arrête désormais."""
     g = graines()
     suites = [MO.generer_suite(g, dict(couche="essai", famille="audit-poids", dose=d, source=k), d,
                                faute="poids-dependantes-doubles") for d in (0.25, 0.5) for k in range(SUITES_PAR_DOSE)]
-    pres = AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(27))
+    nulles = [s for s in saines if s.source.dose == 0.0]
+    pres = AU.audit_presentation(MO.mondes_pour_l_audit(nulles + suites), np.random.default_rng(27), _rng_permutation(2701),
+                                 PERMUTATIONS_D_ESSAI)
     assert pres["exactitudes"]["contenu"]["dependantes_contre_independantes"] > 0.55
     assert "contenu/dependantes_contre_independantes" in pres["signalement"]
     assert pres["mention"] == "générateur non audité pour l'étage payant"
+    with pytest.raises(AU.ArretAudit, match="non calculable"):
+        AU.audit_presentation(MO.mondes_pour_l_audit(suites), np.random.default_rng(27), _rng_permutation(2701), 2)
+
+
+def _signes_des_dependantes_changes(mondes):
+    """Un générateur fautif planté (sur la sortie du générateur sain) : tous les poids des lois dépendantes rendus positifs ;
+    les biais et toutes les autres lois inchangés."""
+    out = []
+    for m in mondes:
+        lois = []
+        for texte, loi, typ, dep in m["lois"]:
+            if dep:
+                loi = {"type": "par_sous_population", "lois": {
+                    g: {"type": "softmax", "poids": [[abs(w) for w in ligne] for ligne in s["poids"]], "biais": s["biais"]}
+                    for g, s in loi["lois"].items()}}
+                texte = L.json_canonique(loi)
+            lois.append((texte, loi, typ, dep))
+        out.append(dict(m, lois=lois))
+    return out
+
+
+def test_garde_25_signes_des_dependantes_changes_vus_par_le_contenu_et_non_par_la_forme(saines):
+    """Garde 25, code v4 (nœud 1, option (a)) : les signes des poids des lois dépendantes changés par un générateur fautif
+    planté. La longueur de forme ne lit plus le signe : les traits de forme d'une loi dont tous les nombres ont au moins quatre
+    décimales ne changent pas ; la longueur brute, trait de contenu, le lit ; l'exactitude de contenu « dépendantes contre
+    indépendantes » dépasse 0,55 et est signalée ; celle de forme ne bouge que par les nombres courts."""
+    saines_m = MO.mondes_pour_l_audit(saines)
+    fautives = _signes_des_dependantes_changes(saines_m)
+    longues = changees = 0
+    for m0, m1 in zip(saines_m, fautives):
+        for (t0, _, _, dep), (t1, l1, _, _) in zip(m0["lois"], m1["lois"]):
+            if not dep or t0 == t1:
+                continue
+            changees += 1
+            assert AU.traits_de_contenu(l1, m1["Z"], m1["G"], t1)[6] < len(t0)  # la longueur brute lit le signe
+            # aucun nombre court négatif (seul cas où le changement de signe touche un jeton) ; les clés « 0 » et « 1 » des
+            # sous-populations sont des nombres courts positifs
+            if not any(j[0] == "-" and len(j) > 1 and not AU._nombre_long(j) for j in AU._JETON.findall(t0)):
+                longues += 1
+                assert np.array_equal(AU.traits_de_forme(t0), AU.traits_de_forme(t1))
+    assert changees > 100 and longues > 0.8 * changees
+    p0 = AU.audit_presentation(saines_m, np.random.default_rng(28), _rng_permutation(2801), PERMUTATIONS_D_ESSAI)
+    p1 = AU.audit_presentation(fautives, np.random.default_rng(28), _rng_permutation(2801), PERMUTATIONS_D_ESSAI)
+    assert p1["exactitudes"]["contenu"]["dependantes_contre_independantes"] > 0.55
+    assert "contenu/dependantes_contre_independantes" in p1["signalement"] and p1["mention"] == AU.MENTION
+    a0, a1 = (p["exactitudes"]["forme"]["dependantes_contre_independantes"] for p in (p0, p1))
+    assert abs(a1 - a0) <= 0.03 and "forme/dependantes_contre_independantes" not in set(p1["arret"]) - set(p0["arret"])
 
 
 def test_garde_25_bornes_de_la_construction_epuisees():
@@ -135,6 +361,30 @@
         MO.generer_suite(g, dict(couche="essai", famille="bornes-courtes", source=0), 0.5, bornes=MO.Bornes(1, 1, 1))
 
 
+def test_etape_3_jugement_des_suites_et_arrets(saines):
+    """Étape 3 (code v4), à taille réduite et sous la couche « essai » : le jugement rend le rapport (ou arrête, le rapport joint)
+    avec, pour les quinze exactitudes, A, σ₀, la moyenne permutée, le seuil et la lecture ; une exactitude non calculable
+    (suites d'une seule dose) arrête l'étape ; la fonction de l'étape joue la couche demandée et le rôle « permutation »."""
+    c = MO.Compteurs()
+    for s in saines:
+        c.ajouter(s.compteurs)
+    try:
+        rapport = MO.juger_suites_d_audit(saines, c, np.random.default_rng(29), _rng_permutation(2901), PERMUTATIONS_D_ESSAI)
+        assert rapport["presentation"]["arret"] == []
+    except MO.ArretGenerateur as e:
+        rapport = e.rapport
+        assert rapport["presentation"]["arret"] and "audit du générateur en échec" in str(e)
+    _verifier_table(rapport["presentation"], PERMUTATIONS_D_ESSAI)
+    assert set(rapport) == {"presentation", "lois_du_final_identiques_a_la_source", "compteurs", "traits_de_contenu"}
+    with pytest.raises(MO.ArretGenerateur, match="non calculable"):
+        MO.juger_suites_d_audit([s for s in saines if s.source.dose == 0.5], c, np.random.default_rng(29),
+                                _rng_permutation(2901), PERMUTATIONS_D_ESSAI)
+    g = graines()
+    with pytest.raises(MO.ArretGenerateur, match="non calculable"):
+        MO.audit_du_generateur(g, (0.0,), 1, np.random.default_rng(30), permutations=PERMUTATIONS_D_ESSAI, couche="essai")
+    assert "couche=essai|famille=audit|role=permutation" in g.etiquettes
+
+
 def test_marge_face_a_la_source_etrangere():
     """À la dose 0,25 (douze paires sur vingt-huit). À la dose 0,5, vingt-quatre paires sur vingt-huit sont des lois dépendantes
     et la construction, sur les graines « essai » de l'outil de diagnostic, épuise ses bornes : constat porté au rapport."""
```

#### `10-test_heritage_etage_processeur_v1_statistique.py.diff`

```diff
--- code-v3/tests/test_heritage_etage_processeur_v1_statistique.py
+++ code-v4/tests/test_heritage_etage_processeur_v1_statistique.py
@@ -58,6 +58,34 @@
         assert interdit not in source
 
 
+def test_note_d8_ecart_type_nul_ou_taille_non_finie_arrete_l_etalonnage(monkeypatch):
+    """Code v4, note D8 (B7) : sur des écarts-types plantés, non tirés — un écart-type entre jumelles nul, ou une taille réduite
+    non finie, arrête l'étalonnage et n'est pas « non atteignable » ; un écart-type positif laisse la dichotomie ou la mention
+    « non atteignable » comme avant."""
+    def plante(sd, ecart):
+        def jumelles(graines, couche, base, prop, dose, taux, f, S, bras, *a, **k):
+            return ({"1": 0.0, "2": 0.0, "3": ecart(prop)}, {b: sd for b in bras})
+        monkeypatch.setattr(ET, "jumelles", jumelles)
+
+    fab = lambda x: prop("lecteur-heritage", K=x)  # noqa: E731
+    plante(0.0, lambda p: 1.0)
+    with pytest.raises(ET.ArretEtalonnage, match="note D8 : écart-type entre jumelles nul"):
+        ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 1.0, FREQUENCES_D_ESSAI, 10)
+    with pytest.raises(ET.ArretEtalonnage, match="note D8"):
+        ET.ecart_type_sans_reglage(graines(), "essai", "sourd-egal", prop("sourd-egal"), 0.25, 0.25, FREQUENCES_D_ESSAI, 10,
+                                   ("1", "2", "3"))
+    plante(1.0, lambda p: float("nan"))
+    with pytest.raises(ET.ArretEtalonnage, match="taille réduite non finie"):
+        ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 1.0, FREQUENCES_D_ESSAI, 10)
+    plante(1.0, lambda p: p["K"] / 256.0)  # taille 1 au réglage maximal : 0,5 atteignable, 1,5 non atteignable
+    assert ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 1.5, FREQUENCES_D_ESSAI, 10)["statut"] == \
+        "non atteignable"
+    ligne = ET.etalonner(graines(), "essai", "lecteur-heritage", fab, "K", 0.25, 0.5, FREQUENCES_D_ESSAI, 10)
+    assert ligne["statut"] == "atteint" and abs(ligne["taille_estimee"] - 0.5) <= 0.02
+    assert ET.ecart_type_sans_reglage(graines(), "essai", "sourd-egal", prop("sourd-egal"), 0.25, 0.25, FREQUENCES_D_ESSAI,
+                                      10, ("1", "2", "3"))["ecart_type_jumelles"] == 1.0
+
+
 def test_garde_26_taille_realisee_reglage_etalonne_et_faussé():
     g = graines()
     base = dict(famille="garde-26", proposeur="lecteur-tenue", dose=0.25)
@@ -118,6 +146,26 @@
     assert set(m) >= {"configuration", "configuration_sha256", "versions", "racine", "etiquettes", "commit", "fichiers_geles"}
     assert m["racine"] == 2026111902 and m["etiquettes"]["nombre"] > 0 and m["etiquettes"]["couches"] == ["couche=essai"]
     assert (tmp_path / "run" / "manifeste.json.sha256").exists()
+    # code v4, choix 12 : la liste entière des étiquettes, triée, dans un fichier scellé à côté du manifeste, dont l'empreinte
+    # (inscrite au manifeste) est celle de la liste et se rejoue à la main
+    import hashlib
+    liste = tmp_path / "run" / "manifeste-etiquettes.txt"
+    octets = liste.read_bytes()
+    lignes = octets.decode("utf-8").split("\n")
+    assert m["etiquettes"]["fichier"] == "manifeste-etiquettes.txt" and lignes == sorted(lignes)
+    assert len(lignes) == m["etiquettes"]["nombre"] and all(l.startswith("couche=essai|") for l in lignes)
+    assert hashlib.sha256(octets).hexdigest() == m["etiquettes"]["sha256"] == m["etiquettes"]["fichier_sha256"]
+    assert (tmp_path / "run" / "manifeste-etiquettes.txt.sha256").read_text(encoding="ascii").split()[0] == m["etiquettes"]["sha256"]
+    assert TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json")) == m["etiquettes"]["nombre"]
+    # artefacts : une étiquette retirée de la liste (compagnon refait), puis une liste altérée sans refaire son compagnon
+    liste.write_bytes(b"\n".join(octets.split(b"\n")[1:]))
+    (tmp_path / "run" / "manifeste-etiquettes.txt.sha256").write_text(
+        f"{hashlib.sha256(liste.read_bytes()).hexdigest()}  manifeste-etiquettes.txt\n", encoding="ascii")
+    with pytest.raises(TI.ArretTirages, match="ne rejoue pas"):
+        TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json"))
+    liste.write_bytes(octets + b"\n")
+    with pytest.raises(TI.ArretTirages, match="compagnon"):
+        TI.verifier_manifeste(str(tmp_path / "run" / "manifeste.json"))
 
 
 def test_rapport_r_sur_des_valeurs_plantees():
```

#### `11-mutations_v3.py.diff`

```diff
--- code-v3/outils-dev/mutations_v2.py
+++ code-v4/outils-dev/mutations_v3.py
@@ -9,7 +9,12 @@
 Version 2 (code v3) : les 41 défauts de la version 1, repris à l'identique, et neuf de plus — C1 (refus d'une couche
 décisive non consigné, vu par l'essai final joué seul : un ; aucun défaut n'ouvre le verrou, ce qui ferait dériver une graine
 décisive), C2 (la copie servie au bras 4b : cinq), C3 (la strate du passage exigée sans besoin : un), notes D4 (table des
-gardes incomplète acceptée : un) et D7 (compteurs du jeu perdus : un)."""
+gardes incomplète acceptée : un) et D7 (compteurs du jeu perdus : un).
+
+Version 3 (code v4) : les 50 défauts de la version 2, repris à l'identique (remplacements et essais), et vingt et un de plus —
+audit de présentation (nœuds 1 et 2, note D9, version 8 : treize), note D8 (trois), choix 12 (deux), dose du jeu de la garde 27
+(trois). Mode de contrôle sans essai : `python3 -B mutations_v3.py --verifier BLOC` compte chaque texte ancien dans `BLOC/src`
+(il doit s'y trouver une seule fois) et n'écrit rien."""
 
 import json
 import os
@@ -18,8 +23,12 @@
 import sys
 import time
 
-BLOC, TRAVAIL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
-SEULS = set(sys.argv[4:])
+VERIFIER = len(sys.argv) == 3 and sys.argv[1] == "--verifier"
+if VERIFIER:
+    BLOC, TRAVAIL, SORTIE, SEULS = sys.argv[2], None, None, set()
+else:
+    BLOC, TRAVAIL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
+    SEULS = set(sys.argv[4:])
 PAQUET = os.path.join("controle_ia", "heritage_etage_processeur_v1")
 T = os.path.join(BLOC, "tests")
 
@@ -172,6 +181,70 @@
        "    if False:\n")], [t("statistique", "regles_de_lecture")]),
     ("compteurs-du-jeu-perdus", "note D7 : compteurs des mondes sources du jeu à sources étrangères perdus", "mondes.py",
      [("        s.compteurs = cumul[k]\n", "")], [t("mecanique", "garde_27")]),
+    # --- version 3 (code v4) ---------------------------------------------------------------------------------------------
+    # nœud 1 (a) : longueur de forme sur le texte aux nombres remplacés, longueur brute parmi les traits de contenu
+    ("longueur-de-forme-brute", "nœud 1 : la longueur de forme lue sur le texte brut (elle lit le signe des nombres)", "audit.py",
+     [("    v[CASES] = float(len(texte_aux_nombres_remplaces(texte)))\n", "    v[CASES] = float(len(texte))\n")],
+     [t("mondes", "longueur_de_forme")]),
+    ("longueur-brute-hors-du-contenu", "nœud 1 : la longueur brute absente des traits de contenu", "audit.py",
+     [("    out.append(float(len(texte)))\n", "")], [t("mondes", "longueur_de_forme")]),
+    # nœud 2 (a) limité aux trois audits des doses ; lettre de la version 6 pour les deux audits de lois
+    ("regle-calibree-etendue-aux-lois", "nœud 2 : la règle calibrée appliquée aussi aux deux audits de lois", "audit.py",
+     [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n", "    if True:\n        if A <= EXACTITUDE_MAX:\n")],
+     [t("mondes", "lecture_calibree")]),
+    ("regle-calibree-retiree", "nœud 2 : les audits des mondes par dose lus à la lettre (au-dessus de 0,55, arrêt)", "audit.py",
+     [("    if audit in AUDITS_DES_DOSES:\n        if A <= EXACTITUDE_MAX:\n", "    if False:\n        if A <= EXACTITUDE_MAX:\n")],
+     [t("mondes", "lecture_calibree")]),
+    ("zone-mediane-arretee", "nœud 2 : une exactitude des doses entre 0,55 et 0,55 + 2 σ₀ arrête", "audit.py",
+     [("        return ARRET if A > EXACTITUDE_MAX + 2.0 * sigma0 else NON_DEPARTAGEE\n", "        return ARRET\n")],
+     [t("mondes", "lecture_calibree")]),
+    ("seuil-calibre-a-vingt-sigma", "nœud 2 : seuil d'arrêt des doses à 0,55 + 20 σ₀", "audit.py",
+     [("        return ARRET if A > EXACTITUDE_MAX + 2.0 * sigma0 else NON_DEPARTAGEE\n",
+       "        return ARRET if A > EXACTITUDE_MAX + 20.0 * sigma0 else NON_DEPARTAGEE\n")], [t("mondes", "lecture_calibree")]),
+    ("permutation-entre-mondes", "σ₀ des doses : étiquettes permutées entre mondes, non entre suites", "audit.py",
+     [("                gm.append(suite_du_monde[k])\n", "                gm.append(k)\n")], [t("mondes", "taille_reduite")]),
+    ("etiquettes-non-permutees", "σ₀ des lois : étiquettes laissées en place sous « permutation »", "audit.py",
+     [("        return yi[rng.permutation(len(yi))]\n", "        return yi\n")], [t("mondes", "permutation_entre")]),
+    ("suite-non-portee", "l'identifiant de la suite n'est pas porté par les mondes de l'audit", "mondes.py",
+     [('            out.append({"dose": m.dose, "suite": i, "Z": m.oracle.Z, "G": m.oracle.G,\n',
+       '            out.append({"dose": m.dose, "suite": 0, "Z": m.oracle.Z, "G": m.oracle.G,\n')], [t("mondes", "taille_reduite")]),
+    # note D9 et version 8 : arrêts de l'audit
+    ("pli-prive-accepte", "note D9 : un pli d'entraînement privé d'une classe n'arrête pas", "audit.py",
+     [("            if not np.any(ytr == c):\n", "            if False:\n")], [t("mondes", "pli_prive")]),
+    ("non-calculable-acceptee", "version 8 : une exactitude non calculable (moins de cinq exemples d'une classe) n'arrête pas",
+     "audit.py", [("    if min(comptes) < EXEMPLES_MIN_PAR_CLASSE:\n", "    if False:\n")], [t("mondes", "pli_prive")]),
+    ("centre-non-fini-accepte", "note D9 : un centre de classe non fini n'arrête pas", "audit.py",
+     [("        if not all(np.all(np.isfinite(c)) for c in centres):\n", "        if False:\n")], [t("mondes", "pli_prive")]),
+    ("arret-de-l-audit-non-converti", "étape 3 : l'arrêt de l'audit de présentation n'arrête pas l'étape comme un arrêt du "
+     "générateur", "mondes.py",
+     [("    except AU.ArretAudit as e:\n", "    except ZeroDivisionError as e:\n")], [t("mondes", "etape_3")]),
+    # note D8
+    ("d8-ecart-type-nul-accepte", "note D8 : un écart-type entre jumelles nul n'arrête pas l'étalonnage", "etalonnage.py",
+     [("    if not (math.isfinite(ecart_type) and ecart_type > 0.0):\n", "    if False:\n")], [t("statistique", "note_d8")]),
+    ("d8-taille-non-finie-acceptee", "note D8 : une taille réduite non finie rangée « non atteignable »", "etalonnage.py",
+     [("    if taille_reduite is not None and not math.isfinite(taille_reduite):\n", "    if False:\n")],
+     [t("statistique", "note_d8")]),
+    ("d8-dichotomie-sans-controle", "note D8 : le contrôle retiré des évaluations de la dichotomie", "etalonnage.py",
+     [('            exiger_ecart_type_et_taille_finis(s, t, f"({nom}, dose {dose}, cible {cible}, réglage {x!r}) ")\n', "")],
+     [t("statistique", "note_d8")]),
+    # choix 12
+    ("liste-des-etiquettes-autre-que-le-texte-hache", "choix 12 : le fichier des étiquettes n'est pas le texte dont le "
+     "manifeste porte l'empreinte", "tirages.py",
+     [("        fh.write(texte_liste)\n", '        fh.write(texte_liste + b"\\n")\n')], [t("statistique", "manifeste")]),
+    ("liste-des-etiquettes-non-verifiee", "choix 12 : la liste des étiquettes relue sans rejouer son empreinte", "tirages.py",
+     [('    if (sha != e.get("fichier_sha256") or hashlib.sha256(liste).hexdigest() != e.get("sha256")\n',
+       '    if False and (sha != e.get("fichier_sha256") or hashlib.sha256(liste).hexdigest() != e.get("sha256")\n')],
+     [t("statistique", "manifeste")]),
+    # dose du jeu de la garde 27 (point 5)
+    ("dose-du-jeu-non-exigee-a-la-construction", "garde 27 : le jeu à sources étrangères construit à une autre dose que 0,25",
+     "mondes.py", [("    if float(dose) != DOSE_JEU_GARDE_27:\n        raise ArretGenerateur(",
+                    "    if False:\n        raise ArretGenerateur(")], [t("mecanique", "dose_du_jeu")]),
+    ("dose-du-jeu-non-exigee-au-jeu", "garde 27 : le jeu à sources étrangères joué à une autre dose que 0,25", "mecanique.py",
+     [("    if float(dose) != DOSE_JEU_GARDE_27:\n        raise ArretMecanique(", "    if False:\n        raise ArretMecanique(")],
+     [t("mecanique", "dose_du_jeu")]),
+    ("jeu-de-l-etape-4-a-une-autre-dose", "garde 27 : l'étape 4 joue le jeu à la dose 0,5 et non à la constante", "etapes.py",
+     [("    suites = MO.generer_jeu_avec_etrangeres(graines, bases, DOSE_JEU_GARDE_27)\n",
+       "    suites = MO.generer_jeu_avec_etrangeres(graines, bases, 0.5)\n")], [t("mecanique", "garde_27_bras")]),
 ]
 # le défaut « strate vide » ne se voit que si la couche statistique ne lève pas non plus à l'emploi : second remplacement
 DEFAUTS[5] = (DEFAUTS[5][0], DEFAUTS[5][1], DEFAUTS[5][2], DEFAUTS[5][3], [t("mecanique", "strate_vide")])
@@ -242,4 +315,26 @@
           rapport["defauts_joues"])
 
 
-main()
+def verifier():
+    """Chaque texte ancien de chaque défaut se trouve une seule fois dans son fichier de `BLOC/src` ; rien n'est écrit."""
+    problemes = 0
+    for ident, _, fichier, remplacements, essais in DEFAUTS:
+        tous = [(fichier, remplacements)] + ([SECONDS[ident]] if ident in SECONDS else [])
+        for f, reps in tous:
+            texte = open(os.path.join(BLOC, "src", PAQUET, f), encoding="utf-8").read()
+            for ancien, _ in reps:
+                n = texte.count(ancien)
+                if n != 1:
+                    problemes += 1
+                    print("PROBLÈME", ident, f, "trouvé", n, "fois")
+        for fichier_essai, _ in essais:
+            if not os.path.isfile(fichier_essai):
+                problemes += 1
+                print("PROBLÈME", ident, "essai absent", fichier_essai)
+    print("défauts", len(DEFAUTS), "identifiants distincts", len({d[0] for d in DEFAUTS}), "problèmes", problemes)
+
+
+if VERIFIER:
+    verifier()
+else:
+    main()
```

## 10. Table entière des empreintes du code v4 (chemins relatifs au dossier `code-v4/`)

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
c5476e7b359b2c15b77795832d8f1849dc23bdc6d0aef7386b179170a4123fee  outils-dev/mutations_v1.py
9fd6fc696c49481d8cbbfeae8b795c388a2accaa2a713d55f5f1f0f4b0a20627  outils-dev/mutations_v2.py
ab84bf18bccfac3ec8c10619d2e1c6d4927f84ec2e5e43e124be37e4a842dfd8  outils-dev/mutations_v3.py
c8a9ed8d7339129d311c787ad5f49c0ef7347c70cfae4b34fabf82f8e6fe6e55  outils-dev/sceller_v1.py
ff647eaf2ead2bd14a1a00a000f09dc142b805fbbeb6aaf87b74f225faaa72d6  outils-dev/verification-empreintes-organisme-v1.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  src/controle_ia/__init__.py
ba3d58e25b499a89d00bf9e2eab524d838297c9214277ba09823b656fe941935  src/controle_ia/heritage_etage_processeur_v1/__init__.py
73c92e370b46e5bc465679a7edc2beed1d6b1f6fc32bcab1116b027c954b13c9  src/controle_ia/heritage_etage_processeur_v1/analyse.py
890040e3b4d3a9d16bdb52a60e66aba9aea048a7129a080b377a20ab63dcdf30  src/controle_ia/heritage_etage_processeur_v1/audit.py
8758b015d523370d6d1a98ff3fdebbe0fdc823805abaf9aa1fd024f48d9d64a7  src/controle_ia/heritage_etage_processeur_v1/comparateur.py
f94e5940d62fc5536a465113596361b0039b80f38ee4471688b551277c4d0e78  src/controle_ia/heritage_etage_processeur_v1/constantes.py
684aeed62fd8ecc902c42e503e8211385e275e5feee36dec6d6e922afc2014bb  src/controle_ia/heritage_etage_processeur_v1/cout.py
2173613ae03067c4ff3090f74644f86550ca1d127702ff41443d1dc6a574a799  src/controle_ia/heritage_etage_processeur_v1/enveloppe.py
fda98bba41c57cbd4860a62d93c7e12f3d23d098f148af0e79b48ec20417eee3  src/controle_ia/heritage_etage_processeur_v1/equivalence.py
ed2db872f41cdad3594d9d996c9594759778a8298afafc57dc3662c8f113fd91  src/controle_ia/heritage_etage_processeur_v1/etalonnage.py
4a4b22e85543c5045d398a095ed052aee9de582d88fff9b5a78147fcd0cb95db  src/controle_ia/heritage_etage_processeur_v1/etapes.py
063df6e1e2c08d79531fce8b76f3e3dbc3fdb002af7657efb1773e33afb9beda  src/controle_ia/heritage_etage_processeur_v1/executeur.py
dce5db04472d049f350f08d56f65a8254fb58eb13f3f2b6a0c3ca2e95952fcd5  src/controle_ia/heritage_etage_processeur_v1/frequences.py
cf433337972c02baefe2f57323f036d98649b5b25fb8da1afd59bd12ab2e8c13  src/controle_ia/heritage_etage_processeur_v1/graines.py
4492c8545f6fc081eb267d851bd24a011fe4817cadad8b9606048bb26208dc1f  src/controle_ia/heritage_etage_processeur_v1/intervalles.py
fb24a9eaffdc98ee080db835d77ee2c419242ad4108ef60b440df8f1cb387536  src/controle_ia/heritage_etage_processeur_v1/lois.py
367a9ce047ceb033a58f40090efa5ba0360853f5f153d89148671ac35ee7acb8  src/controle_ia/heritage_etage_processeur_v1/mecanique.py
eb9b2c2d7d276c0e55e3e9dd228604dd235e758c95b235ea1b508d43391ed38d  src/controle_ia/heritage_etage_processeur_v1/mondes.py
fb2f7b48234661c2c825e2dc0c1cb7b9a6f576ff6bdebb3a2196aa3efe9293f1  src/controle_ia/heritage_etage_processeur_v1/organisme.py
e0aa6b89501c4cfeaed67d748db02dba1cb015405c34a91955d70dc2e408ab83  src/controle_ia/heritage_etage_processeur_v1/proposeurs.py
9a386fc7d56cc3f10369ef066e1f9daae7f3e41e592dd9ab4cd2b7b6768c6417  src/controle_ia/heritage_etage_processeur_v1/rangs_signes.py
5e817dfaa7734ef3f607c978f7dcf981c9446de757909600a2001fbbf4101bfb  src/controle_ia/heritage_etage_processeur_v1/registre.py
c0619eb367b94a54ced73a26098c32c1a153b9b298c596e607dd5393b81a1643  src/controle_ia/heritage_etage_processeur_v1/statistique.py
93077e25e671a164fcae741c248f865011dfe436bb49d830ead4c9e41ba8795c  src/controle_ia/heritage_etage_processeur_v1/tirages.py
372229230356317c51990c0a45ed7e811e37ba2579e7b8c99f8d418bf7dbd236  tests/aides_heritage_etage_processeur_v1.py
444f30432e9551c50ef7fc34d6ca232c08478f5d207f13a47c79bbabdbf74f0e  tests/test_heritage_etage_processeur_v1_etapes.py
acd1954670935fc87778411602519916af0b7be8e08decce2aa86f7636996d12  tests/test_heritage_etage_processeur_v1_gardes.py
b6486da564025663677d9fe6d0a1eae4a5087018d695b3d03d995482ab570f12  tests/test_heritage_etage_processeur_v1_mecanique.py
4c934139f0c5b15897f9e69f23863f1978cd6577a3b2085f3c0f11477af900e7  tests/test_heritage_etage_processeur_v1_mondes.py
2697382c1ce050b590d956078796e5c9c5225ea1ad37d08c2ded011a47799461  tests/test_heritage_etage_processeur_v1_organisme.py
3162d852ce59c5eb263236bf9c154911a47ea8eb13d262794614953937ec0a4f  tests/test_heritage_etage_processeur_v1_outils.py
2d1bc1fd6593137bc6e6a39d934154a09dd8fcdac4811fbf2c9f3649daabf66a  tests/test_heritage_etage_processeur_v1_statistique.py
d342fa2a4f775085e29dcce8f97cd38b5de1293f7fe9c111a4ca0428df3f3bb4  tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
```

*Développeur, modèle L′.*

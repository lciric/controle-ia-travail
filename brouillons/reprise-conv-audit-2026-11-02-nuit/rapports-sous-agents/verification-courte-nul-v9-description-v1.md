# Vérification courte par un lecteur neuf — nul v9 : changement de description, essais et mutations du brouillon 4 (v1)

Lecteur neuf : je n'ai écrit ni le nul v9, ni ses essais, ni son banc, ni son préenregistrement, ni ses brouillons, ni la
contre-lecture n° 1. Consigne : `/home/claude/controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-courte-nul-v9-description-prompt.md`.
Lecture du 2 novembre 2026, de 23:24:57 à 23:42:53 UTC (heures relevées par `date -u`), rédaction ensuite, sur
`/home/claude/ideation-organism/` au commit `66dbcf1` (arbre égal au commit pour les 19 fichiers en jeu), pendant la course
décisive (lancée à 23:20:37 UTC ; je n'ai lu ni sa sortie ni son journal).

## Verdict

**Conforme avec réserves** : rien de ce que j'ai lu ou rejoué n'invalide la course décisive en cours.
Le changement de `pole/nul_v9.py` est limité à la description (arbres syntaxiques identiques hors docstring et noms de description, aucun calcul ne les lit, mêmes nombres avec l'ancien et le nouveau module sur une course exploratoire) ; les essais et mutations de B1, I5, I6 et I2 font ce que dit le texte (37 essais, 35 sous-essais ; 43 mutations sur 43 tuées pour la raison attendue ; rejoués sur l'arbre scellé).
À déclarer au verdict de la course : l'écart à la règle R2 est levé par cette lecture ; deux phrases du paragraphe de scellement sont inexactes (le banc appelle bien `nul_v9.description()`, pour son manifeste seulement ; la règle des graines est en section 5, pas 4) ; lacunes mineures de la règle R5, antérieures au brouillon 4 et sans effet sur la course (réserves 3 et 4).

### Réserves (une ligne chacune)

1. Paragraphe de scellement, « aucun de ces noms n'est lu par le banc v9 » : inexact, le banc appelle `nul_v9.description()` (`demonstrations/banc_tricheurs_v9.py:541`), qui lit toutes les constantes changées et `description_publique()` ; c'est pour le manifeste seulement, sans effet sur aucun nombre (question 1).
2. Paragraphe de scellement, « La graine décisive est l'empreinte de ce fichier (section 4) » : la règle des graines est en section 5 (ligne 354 du texte) ; la section 4 porte les prédictions.
3. Garde de monotonie (`banc_tricheurs_v9.py:272`) : le disjoint « promotion sous v9 sans promotion sous v8 » n'est jamais éprouvé seul (le sous-essai « monotonie » viole aussi la richesse, 5,0 contre 1,0) ; une mutation qui le retirerait survivrait (c'est le miroir de G5 ; filet presque toujours couvert par l'autre disjoint).
4. Gardes sans essai sur un artefact, antérieures au brouillon 4 : richesse non finie (lignes 297-298) ; `--repetitions` ou `--processus` < 1, `--duree-max-s` ≤ 0 (lignes 519-520) ; entropie décisive < 2⁶⁴ (lignes 489-490, inatteignable : probabilité 2⁻¹⁹²) ; le titre de la section 9 (« chaque garde éprouvée sur un cas sain et un artefact ») est donc trop large.
5. Essais de la description publique (I2) : l'ordre et la séparation trous, choix, nature sont épinglés, le contenu en partie seulement (réserves autres que « sans mémoire », phrase de garantie, liste du couvert) ; l'« artefact » du premier essai éprouve l'heuristique de l'essai sur une copie littérale de l'ancienne liste, pas le code ; sans effet sur la course.
6. Artefact de durée (`test_duree_du_mode_decisif_48_h`) : « rien d'écrit » n'est vérifié que sur `banc-tricheurs-v9.json` (ni le dossier ni le manifeste) ; c'est vérifié pour `--lignes` et `--repetitions` par l'essai de B1, sur la même garde.
7. Statut du texte, « trois fichiers existants modifiés et seulement eux » : le même commit `516feca` (tâche jumelle du même sous-agent, attaque v4 brouillon 2) modifie aussi quatre fichiers existants de l'attaque v4 ; aucun n'est dans la fermeture du banc v9 (vérifié) : sans effet, phrase à lire comme limitée à la validation.
8. Les fragments de G1 à G5, L1, L2 et C5 dits « repris à l'identique du script du contre-lecteur » ne sont pas vérifiables : `sondes_mutations_contre_lecture_v1.py` n'est plus sur disque (bloc-notes non durable, recherche dans `/tmp` vide) ; ils sont cohérents avec les lignes que cite la contre-lecture.

Précision, sans réserve : la graine décisive est l'empreinte du texte scellé, et ce texte contient l'empreinte de
`pole/nul_v9.py` (bloc de la section 12 et tableau d'en-tête) ; le changement de description a donc, par la règle gelée,
déterminé quelle graine la course utilise (comme toute ligne du texte), sans rien changer à la façon de calculer ; l'historique
public ne porte qu'un seul texte scellé (`v1`, commit `66dbcf1`). Aucune autre voie de la description vers une graine
(question 1).

## Question 1 — le changement de `pole/nul_v9.py` est-il limité à la description ?

**Oui.**

- Diff textuel `5e352ec` (`8cb44adf…`) contre l'arbre (`7ae450df…`, égal à `516feca` et à `HEAD`) : docstring du module
  (lignes 62-79), `PHRASES_MEMBRES_V9` (114-115), un commentaire, `NON_COUVERT_V9` (une phrase retirée), trois constantes neuves
  (125-134), `description_publique()` neuve (564-575), `description()` (578-584). Rien d'autre.
- Arbres syntaxiques (`comparer_arbres_nul_v9.py`, sortie `sortie-comparer-arbres-nul-v9.txt`) : 43 instructions de tête avant,
  47 après, 39 identiques (`ast.dump` sans positions) ; différentes : docstring, `PHRASES_MEMBRES_V9`, `NON_COUVERT_V9`,
  `description` ; ajoutées : `HORS_DU_NUL_PAR_CHOIX_V9`, `HORS_DU_NUL_PAR_NATURE_V9`, `RESERVES_V9`, `description_publique`.
  **Arbre sans docstrings ni noms de description : identique (`True`).** Dans le module, seules `description_publique` et
  `description` lisent ces noms ; aucune fonction de calcul (`maximiser_par_lots`, `detail_morceaux_groupe`,
  `evaluer_sur_issues`…) ne les lit.
- Hors du module (recherche dans tout `orchestrator/`, sans lien symbolique) : ces noms ne sont lus que par
  `pole/attaque_goodhart_v4.py` (lignes 119, 152-153 : description donnée au proposeur de l'attaque v4, autre expérience), ses
  essais et mutations, et les essais et mutations du nul v9. Le banc v9 ne lit que `nul_v9.description()` (ligne 541).
  `nul_v9.__doc__` n'est lu nulle part.
- Fermeture des imports, mesurée dans un processus neuf (`differentiel_nul_v9.py fermeture`, `sortie-fermeture.txt`) : 11 modules
  de `pole/` plus les trois bancs chargés par chemin = les 14 `FICHIERS_GELES` ; `pole/attaque_goodhart_v4.py` n'est pas chargé.
- Graines : entropie = `int(sha256(texte scellé), 16)` (`banc_tricheurs_v9.py:487-488`) ; répétition r de la ligne « nom|nul » :
  `SeedSequence(entropie, spawn_key=(cle_ligne(ident), r)).spawn(3)` (`banc_tricheurs_v8.py:159-166`). Les tirages frais et
  l'ordre secret dérivent de l'empreinte de l'engagement gelé (`pole/selection_pari.py:532` et `:521`) ; l'engagement porte
  identifiant, loi, bibliothèque, alpha, seuil, instances, nombre d'issues, mode, empreinte de fiche, calibrage, delta0, plan,
  instants (`selection_pari.py:491-494`, `nul_filles_v2.py:86`) ; les membres par morceaux y entrent par `membres_morceaux` (nom,
  type, lois, partition), fonction identique dans les deux états. Aucune occurrence de `nul_v9` dans `selection_pari.py`,
  `nul_filles_v2.py`, `cycle.py`, `controles_pari.py` et les bancs v7 et v8 ; les seules occurrences de `description` y sont
  l'aide de la ligne de commande et le manifeste du banc v8 (`nul_v8.description()`, ligne 558, dans son `principal`, que la
  course v9 n'appelle pas).
- **Manifeste** : `manifeste(…, nul=nul_v9.description(), …)` puis `ecrire_json_scelle(manifeste.json)` (lignes 539-548), avant
  `jouer_tout` (ligne 550) ; le banc ne le relit jamais (ni `jouer_ligne`, ni `lire_v9`). `description()` lit deux fichiers
  (empreintes de `nul_v9.py` et `nul_v8.py`), assemble des chaînes, ne touche à aucun état global ni à aucun générateur.
  **Cela ne change rien au calcul.** Seul effet concevable : une exception ou un objet non sérialisable arrêterait la course
  avant tout calcul ; ce n'est pas le cas (les processus ouvriers 26189 et 26190 existent, donc la course a passé la ligne 548 ;
  déduit de la table des processus, sans lire la sortie).
- Contrôle dynamique (`differentiel_nul_v9.py course` puis `comparer`) : `principal` du banc, mode exploratoire, graine 777001,
  lignes T05s, M01, M02, M06, I01, H04, 3 répétitions, un processus, joué une fois avec le `nul_v9.py` de l'arbre et une fois avec
  la copie de `5e352ec` substituée à `pole.nul_v9` : **rapports identiques hors durées** ; manifestes différents seulement dans
  `nul` (`description_publique`, `hors_du_nul_par_choix`, `hors_du_nul_par_nature`, `non_couvert`, `reserves`, `sha256`) ; mêmes
  entropie, mode, lignes, répétitions, durée, processus (`sortie-comparer-courses-exploratoires.txt`).

## Question 2 — les essais de B1 font-ils ce que disent le texte et le rapport ?

**Oui**, avec les réserves 3 et 6.

| promis (sections 0 ter, 9, 14, annexe B ; rapport) | essai (`essais/test_nul_v9.py`) | constat |
|---|---|---|
| texte d'essai scellé au nom décisif, 14 empreintes | `test_mode_decisif_cas_sain_et_refus` (672-705) : `self._prereg(self._gel())`, `ecrire_scelle`, `DOSSIER_PREREG` remplacé | oui : empreintes de l'arbre lues à l'exécution |
| sans option, la course démarre une fois | `principal([sortie, "--preenregistrement", p]) == 3`, `len(appels) == 1` (bouchon de `jouer_tout`) | oui |
| 31 lignes, 1 000 répétitions | tâches égales à `banc.LIGNES`, `len == 31`, `t[4] == REPETITIONS_DECISIVES` ; `1000` littéral dans le manifeste | oui |
| 172 800 s transmises | `{t[6]} == {48 * 3600.0}` (littéral) | oui |
| entropie = empreinte du texte | `{t[0]} == {int(sha256_fichier(p), 16)}` | oui |
| manifeste « decisif » | `reglages` : `("decisif", 1000, 172800.0)` | oui |
| `--lignes M01`, `--repetitions 999` : code 2, texte non lu, rien d'écrit | sous-essais `refus` : code 2, `lu.assert_not_called()`, `assertFalse(os.path.exists(s))` | oui |
| `--duree-max-s 28800` : code 2, texte non lu, rien d'écrit | `test_duree_du_mode_decisif_48_h` (658-670) : code 2, texte non lu | oui ; « rien d'écrit » sur le seul `banc-tricheurs-v9.json` (réserve 6) |
| monotonie par la seule richesse | sous-essai « monotonie-richesse » (642-649) : v9 2,0 contre v8 1,0, aucune promotion → code 3, `MonotonieViolee` | oui ; l'autre disjoint n'est pas isolé (réserve 3) |

- Essais rejoués une fois (commande de la consigne, plus `-rA` pour l'affichage), 23:36:08 à 23:36:49 UTC :
  **37 passed, 35 subtests passed in 40.11s**, code 0 (`sortie-essais-test-nul-v9.txt`).
- Mutations rejouées une fois (commande de la consigne, plus `--raisons` pour l'affichage), 23:36:59 à 23:38:11 UTC
  (`sortie-mutations-nul-v9.txt`) : chaque mutation G n'est jouée que contre l'essai cité, et toutes sont tuées pour la raison dite :
  - G1 (`--lignes` accepté), G2 (autre nombre de répétitions accepté) : « Expected 'lire_preenregistrement' to not have been
    called … `call().__iter__()` » — sans la garde, le lecteur (remplacé par un objet factice) est appelé, son retour ne se
    déballe pas, `ValueError` donne le code 2, puis l'essai « texte jamais lu » échoue. La contre-lecture attendait « 3 != 2 »
    (course lancée) ; le mécanisme diffère, la détection est aussi forte et vise exactement la propriété promise ;
  - G3 (mode décisif toujours refusé) : « 2 != 3 » ; G4 (durée transmise plafonnée à 8 h) : ensembles différents, 28 800 contre
    172 800, « durée transmise à la course ≠ durée gelée » ; G5 : sous-essai `arret='monotonie-richesse'`, « 1 != 3 ».
- Non vérifié par le cas sain : le nombre de processus (non gelé par la garde, sans effet sur les nombres). L'acceptation du
  **vrai** texte scellé n'est pas l'objet de l'essai ; je l'ai vérifiée à part (question 4), et la course tourne.

## Question 3 — I5, I6, I2 : ce que le texte promet, ou plus faible ?

- **I5, ordre des issues** (`test_ordre_des_issues`, 544-556) : exactement ce que promet la section 9 (fatale non tenue et perte
  non tenue → « trou » ; perte non tenue et artefact non tenu → « puissance perdue »). Ce n'est pas plus faible que l'ordre complet
  de la section 7 : des six ordres possibles des trois branches conditionnelles (trou, perte, dents), les cinq ordres faux mettent
  « perte » avant « trou » (vu par le premier cas) ou « dents » avant « perte » (vu par le second) ; « confirmé » et « précision
  insuffisante » sont exclusifs des trois par construction. L1 et L2 tués (« + puissance perdue », « + trou »).
- **I6, valeur certifiée sous optimisation tronquée** (`test_valeur_certifiee_sous_optimisation_tronquee`, 265-299) : exactement la
  promesse (les 30 mondes de l'essai de domination, mêmes graines, `PALIERS_MU = (1e-2,)`, `PAS_MAX_PAR_PALIER = 1`). Le
  remplacement agit (constantes lues comme globales du module à l'appel, `nul_v9.py:290-291`) ; l'essai porte sur `valeur` de
  `detail_morceaux_groupe`, la valeur que le juge utilise ; ses dents sont assertées (au moins un instant où la meilleure valeur
  atteinte + 10⁻³ est sous la vraisemblance du monde) et C5 est tuée : valeur −79,07 sous la vraisemblance −60,14 (monde 0,
  instant 100). Une seule forme de troncature est jouée ; la validité des autres tient au certificat pris à chaque itéré
  (`nul_v9.py:270-278`, `316-319`, `363-366`), éprouvé par la domination et la référence scipy.
- **I2, description publique** (`DescriptionPublique`, 719-768) : épinglés — maximum au dénominateur, « même loi aveugle, même
  poids », ordre trous < choix < nature < réserves, chaque phrase de chaque constante dans sa section, aucun choix parmi les trous
  (mutation « choix rangés parmi les trous » tuée), quatre trous, mots clés des choix, « hors de l'archive », « sans mémoire ».
  Plus faible que la promesse sur le contenu : les réserves « traits finis » et « marge de Newton », la phrase de garantie et la
  liste du couvert ne sont pas épinglées ; l'« artefact » du premier essai applique l'heuristique `"aveugle" in p` à une copie
  littérale de la liste du brouillon 2 (il éprouve l'essai, pas le code). Réserve 5, sans effet sur la course.

## Question 4 — texte scellé

- **Brouillon 4 à l'octet plus le seul paragraphe** (`verifier_texte_scelle.py`, `sortie-verifier-texte-scelle.txt`) : v1 =
  brouillon4[:p] + inséré + brouillon4[p:] (vrai) ; l'insertion fait 2 116 octets et 18 sauts de ligne, après la ligne 2 (titre et
  ligne vide) : les lignes 3 à 19 du texte scellé et une ligne vide. Rien d'autre ne diffère. Empreintes : v1 `54c5713d…62c18fb`,
  brouillon 4 `02dfbb7b…0dc0908`.
- Affirmations du paragraphe :
  - arbres syntaxiques, liste des noms changés et ajoutés : **exact** (question 1) ;
  - « aucun de ces noms n'est lu par le banc v9 » : **inexact** (réserve 1) ;
  - bloc de la section 12 : **exact** — 14 lignes, mêmes chemins et même ordre que `FICHIERS_GELES` (lu dans l'arbre syntaxique du
    banc), 14 empreintes égales à l'arbre, aucune ligne de ce format hors des marqueurs ; arbre égal à `HEAD` pour ces fichiers ;
  - 37 essais et 35 sous-essais : **exact** (rejoué) ; 43 mutations sur 43, témoin de 26 essais sans échec, code 0 : **exact**
    (rejoué, témoin de 26 essais avant et après) ;
  - aucun dossier de sortie décisive ni compagnon avant le scellement : **exact pour l'historique public** — 49 commits, aucun
    chemin contenant `banc-tricheurs-v9-validation` dans aucun commit ni dans `HEAD` ; texte et compagnon n'apparaissent qu'au
    commit `66dbcf1` ; aucun autre `preenregistrement-validation-nul-v9-v<N>` jamais commité. L'état du disque avant le scellement
    n'est pas vérifiable sans lire le dossier interdit ;
  - « (section 4) » pour la graine : **renvoi faux** (réserve 2) ;
  - compagnon : `54c5713d…  preenregistrement-validation-nul-v9-v1.md`, format de `sha256sum`, égal à l'empreinte ; nom accepté par
    le motif du banc ; entropie ≥ 2⁶⁴ ; texte et compagnon dans le commit `66dbcf1` (23:20:16 UTC), **poussé à 23:20:18 UTC**
    (journal local de `origin/main`), avant la course (23:20:37 UTC) ;
  - heures : « lance la now » à 00:15 heure de Paris = 23:15 UTC, scellement 23:19 UTC, commit 23:20:16 UTC : cohérent.
- Tableau d'en-tête : toutes les empreintes vérifiées aux commits cités (`5e352ec`, `e58cfec`, `9e6ca23`) et dans l'arbre.

## Question 5 — ce qui invaliderait la course ou doit être déclaré

- **Rien n'invalide la course.** La commande en cours (table des processus, PID 26187, `nice` 10, dossier courant
  `orchestrator/`) est celle de la section 5 avec `v1` : `python3 -I -B demonstrations/banc_tricheurs_v9.py
  ../resultats/banc-tricheurs-v9-validation-v1 --preenregistrement prereg/preenregistrement-validation-nul-v9-v1.md
  --repetitions 1000 --processus 2`, sans `--duree-max-s` ; code gelé égal au commit et au bloc ; poussée avant la course.
- À déclarer : réserves 1 à 8 ci-dessus, et l'écart à la règle R2 (déjà déclaré dans le texte) levé par cette lecture, faite
  avant toute lecture de la sortie.
- Déjà déclaré dans le texte, rappelé : `pole/nul_v9.py`, fichier existant, modifié en place à la demande du directeur ; ses
  lignes 3 à 7 (« Fichier neuf (R12) : aucun fichier existant n'est modifié » ; validation « brouillon1 (non scellé) ») sont
  devenues fausses (mineur M7 du texte, sans effet sur le calcul).
- Section 14, étape 6 (« sur l'arbre scellé : essais et banc de mutations ») : le directeur les a joués juste avant le scellement ;
  rejoués ici sur l'arbre scellé, pendant la course : mêmes comptes.

## Ce que j'ai fait et pas fait

Aucune lecture ni liste du dossier de sortie de la course ni de son journal ; aucun mode décisif ; aucun commit, aucun
`git fetch`, `checkout` ou `stash`, aucune commande qui écrit l'index (git appelé avec `GIT_OPTIONAL_LOCKS=0`, sans `status` ni
`diff` sur l'arbre) ; aucun fichier existant modifié, rien dans `orchestrator/` (vérifié : aucun fichier plus récent que mon
premier script) ; aucun réseau, aucun modèle ; `nice -n 10` partout. Les seuls `.sha256` écrits sont ceux que le banc exploratoire
écrit dans mes deux dossiers de sortie sous `lecteur/` (et ceux des essais, dans `/tmp`, effacés par leurs nettoyages). Essais et
banc de mutations joués une fois chacun, pendant la course : partage du processeur seulement, sans effet sur ses nombres.

## Scripts et sorties (sous `/home/claude/scratch/verif-nul-v9/lecteur/`, sha256)

```
9db8e6b5439e92b25b6c5650b7a7ce4a5c1eba9bd888403feb6713167e6a6aab  comparer_arbres_nul_v9.py
5fd21ede99ba8af1adbdf87a020cd3c83aa8d61e03b0e1abfbef116868dfd0d7  verifier_texte_scelle.py
239467d60c6e25b1342b308f5acefeed2b102278726b94a53714102b9cb77d36  differentiel_nul_v9.py
d991119a1427a11407d309bc66186066eb7d39cd184da0992e3d784fab47f820  sortie-comparer-arbres-nul-v9.txt
537290ac54fa61e086a64bbb82d11587a8b350b586efc9578f21fcbbd4a1f015  sortie-verifier-texte-scelle.txt
5a8a624792e9d809a1356f94b2e35a20d26e3047d346b7565b5d1cd0cc592705  sortie-fermeture.txt
55b1c0eb483e0b1e75464b7594653a358635a092332b92a5c1352fca5c69cbd6  sortie-course-exploratoire-arbre.txt
0510171a1e9e1dc8d8cc0f0de0df835368cef993d0bdaf9937e7a90bee62cc60  sortie-course-exploratoire-5e352ec.txt
50e461ee65f6c8251e5cb98a3e1ec606878731ff2f82b7411a89f4f68bc02957  sortie-comparer-courses-exploratoires.txt
8df89b9f547b75cc4c318f42b6f58ead41f18782286ea6c37bf640d322183e81  sortie-essais-test-nul-v9.txt
3c4e77bef99acad0b560eeb2fb19e154c2402ebd83db64a11deae11bfc011ab7  sortie-mutations-nul-v9.txt
7b538ca2adf7b52739a0463ecbfc35a218ea9a4977c5de60d62caa8e4051c74b  banc-exploratoire-arbre/banc-tricheurs-v9.json
9511422d1b85ae4694ccb60396b6ef6091be60df6bab4393c6eb7d92759e9264  banc-exploratoire-arbre/banc-tricheurs-v9.json.sha256
4dfa05375cd2c79ed07f85385ef6aa49be4bee807ced7bca0f74029f30a3d95d  banc-exploratoire-arbre/manifeste.json
59d4d1eee4b166d1dcc6251db58f5b123c26c95960f5f11b0e97be4f7db340ca  banc-exploratoire-arbre/manifeste.json.sha256
b433aafdf7868bb1240270f521f37bd4a0ce88d979d7d32c2034141723bf0a37  banc-exploratoire-5e352ec/banc-tricheurs-v9.json
ad73f043776b0772d2ea1e6265f87aa25402f947192157b494d374ddb2dcc982  banc-exploratoire-5e352ec/banc-tricheurs-v9.json.sha256
7e31da4d2760ed949ed9543d198b39d5d7183ae473dc4748ca4afb3ce0e58a2d  banc-exploratoire-5e352ec/manifeste.json
21c0f1fb00649a6255ca762353260bd6be5852559b48331a76ad38175e12756f  banc-exploratoire-5e352ec/manifeste.json.sha256
8cb44adf8b325ac656b077f03dddb44311071510a5785ebd3f0aa8c37aebc655  extraits/nul_v9-5e352ec.py
7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95  extraits/nul_v9-516feca.py
7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95  extraits/nul_v9-HEAD.py
f674e9cac121d8930942738e28f938bd3613018c0c4371bd4621e53020212855  extraits/test_nul_v9-5e352ec.py
9eb966ad4220fc6cd297eef53ebec36a0f77655c2eadaceedc52ad72a1a67b21  extraits/test_nul_v9-e58cfec.py
d42a50eb4ba9691e75e82fa4bc714a925615da80df22227fee730392015999b9  extraits/test_nul_v9-516feca.py
d42a50eb4ba9691e75e82fa4bc714a925615da80df22227fee730392015999b9  extraits/test_nul_v9-HEAD.py
576eea7917cc9c0ed5213eeb22f191add217cc91b54fc4368a087911f153507d  extraits/mutations_nul_v9-5e352ec.py
9cb305e45b8c005564184df621e68c05f1ac36b92e520ee081dbed735a252d16  extraits/mutations_nul_v9-e58cfec.py
f004dba63ffe25c66b9b41edefbd8307e188feccd8a8e15aa9754e472dca3f52  extraits/mutations_nul_v9-516feca.py
f004dba63ffe25c66b9b41edefbd8307e188feccd8a8e15aa9754e472dca3f52  extraits/mutations_nul_v9-HEAD.py
7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44  extraits/banc_tricheurs_v9-e58cfec.py
7e4bff5995df2a7d62a4f5a2f5f9176da614e657a55b05183325fa2fc6e24e44  extraits/banc_tricheurs_v9-HEAD.py
```

Ce rapport ne porte pas sa propre empreinte : elle est donnée avec sa remise.

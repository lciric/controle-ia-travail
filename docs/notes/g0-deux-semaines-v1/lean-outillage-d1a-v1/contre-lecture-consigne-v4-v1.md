# Essai Lean, D-1a — contre-lecture de la consigne v4 du poste local (troisième essai) — v1

- **Lecteur** : Claude Fable 5.1 (`claude-fable-5-1`), contre-lecteur neuf, d'un autre modèle que le rédacteur (Opus 5.5) ;
  n'a écrit ni la v3, ni la v4, ni le différentiel. Pièce d'instrument (classe B) : contre-lecture, puis vérification des
  corrections par le même contre-lecteur.
- **Objet** : `consigne-poste-local-lean-d1a-v4.md`, empreinte recalculée
  `834016a260f85483388db06d83c000da147fa269d18bd3c39ea1f2efce718099` ; `differentiel-consigne-v3-v4.diff`,
  `9f2bc7b3ca7f905dfa034b735251cdac3f85ab902e528720707904406c61652c`. Les quatre compagnons `.sha256` (v4, différentiel, v3,
  vérification courte) ont été recalculés et trouvés conformes.
- **Comparé à** : la consigne v3 (`17914672caf9fa2f12daa1da7a5bfec7067c957de8570e42dd6fb1b2899bde50`) et sa vérification
  courte (`82734f0d3cf3cc31a8c57f1d697a86f37c3b1b711f947dd4b9bea132f30c50e8`) ; l'état du chantier
  `docs/notes/etat-chantier-lean-2026-11-21-v1.md` (`3d2b8d3e…`, recalculée), § 2 et § 3 ; `registres/go.md` l. 303 et 611 ;
  `registres/decisions.md` R-2426, R-2434, R-2439, R-2486 à R-2492 ; `registres/depenses.md` l. 416 à 427 ;
  la procédure v11 et le harnais à `ae894d8df2a19f51e532ff667160ae7bba2bf6ac` (tête de `origin/prep/lean-outillage-d1a-v10`,
  lus par `git show`) ; le rapport du second essai à la tête de `donnees/lean-outillage-d1a-poste-local-v2` (commit `3b2a74a2`),
  pour les heures seulement ; les interdits communs v2 (`1ee3b370…`, recalculée).
- **Heures** (`date -u`) : début 2026-11-21T07:11:25Z ; écriture 2026-11-21T07:15:29Z.
- Lecture seule : rien lancé, rien loué, aucun `rm`, aucune écriture git hors de ce fichier et de son compagnon ; aucun
  fichier interdit ouvert ; aucun résultat d'expérience lu.

## Verdict (une ligne)

**Exécutable après corrections** : trois corrections de texte (C1 à C3, ci-dessous), aucune garde affaiblie, aucune valeur
fausse ; la procédure de la v3 est bien reprise mot pour mot hors des changements déclarés.

## Contrôle 1 — la v4 est la v3 hors des changements déclarés

- `diff -u v3 v4` rejoué : identique au différentiel versé, hors les deux lignes d'en-tête de fichiers (chemins et dates
  du système, hors de la comparaison). Le différentiel versé, appliqué à la v3 par `patch`, redonne un fichier d'empreinte
  `834016a2…`, égale à celle de la v4 : **la v4 est exactement la v3 plus ce différentiel**.
- Huit blocs de changement, tous dans les sept changements déclarés par le rédacteur :
  1. titre « v3 » → « v4 » ;
  2. en-tête (rédacteur, session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`, sources, liste de ce qui change) ;
  3. paragraphe « Rappel : le troisième essai n'a jamais été lancé » et liste « Avant de lancer » (onze points) ;
  4. paragraphe « Session mère … » : identifiant de la mère actuelle, R-2492 et GO-2026-11-21-12 ajoutés ; le reste du
     paragraphe (R-2439, R-2464, R-2470, R-2486, contre-lecture v10 `e7bdbb15…`, commits `5103a7f3` et `ae894d8d`) inchangé ;
  5. bloc « Dépense autorisée » : échéance, « deux fois 0,28 USD », création et destruction par la procédure, R10,
     garde d'heure limite, clé du loueur ;
  6. règle 4 : lecture `git ls-remote` ajoutée aux gestes git permis ;
  7. mandat 1 : contrôle `ls-remote`, branche `…-poste-local-v4` (au lieu de `…-v3`), « jamais …-v3 » ;
  8. mandat 7 : nom du rapport justifié, branche nommée, lignes proposées rattachées au GO et à la branche.
- **Gestes M1 à M6 inchangés** (mandat 4, identique à la v3 et conforme à la procédure v11 : lecture, même projet, droit
  d'écrire, destruction à blanc, trois tâches T1 à H, T2 à H + 30 min, T3 à H + 24 h, ligne « en tâche jusqu'à »).
  Sections 0 à 7 du mandat, réserve E3 et annexe S1 à S8 : mot pour mot la v3.

## Contrôle 2 — valeurs citées, à la source

| Valeur dans la v4 | Source relue | Juste ? |
|---|---|---|
| Empreintes v3 `17914672…`, vérification courte `82734f0d…`, état du chantier `3d2b8d3e…`, contre-lecture v10 `e7bdbb15…`, procédure v11 `932b3bbc…`, interdits communs `1ee3b370…`, rapport v2 `b2bace9b…` | recalculées (`sha256sum` ; `git show … \| sha256sum` pour la procédure à `ae894d8d` et le rapport v2 à `3b2a74a2`) | oui, toutes |
| `ae894d8d` tête de `prep/lean-outillage-d1a-v10` ; code à `5103a7f3` ; « aucun code entre les deux » | `git fetch` puis `git rev-parse` ; `git diff --name-only 5103a7f3 ae894d8d` : 22 fichiers, tous sous `docs/notes/…/lean-outillage-d1a-v1/` (procédure v11, empreintes v8, journaux de mutations et d'essai) | oui |
| GO-2026-11-10-13 : calcul, 65 USD, échéance 2026-11-30 | `registres/go.md` l. 303 | oui |
| GO-2026-11-21-12, voie 1 : « troisième essai de l'outillage avant le 30 novembre sous GO-2026-11-10-13 (consigne v4) » | `registres/go.md` l. 611 | oui |
| R-2439 « Réparer d'abord, puis relancer », troisième machine accordée ; R-2492 « Lean : le troisième essai est à lancer sur ton poste. :go » | `registres/decisions.md` l. 2397 et 2451, verbatim | oui |
| 0,56 USD = deux fois 0,28 USD ; serveurs 175751342 et 175838427 ; 0,22692 EUR au taux de 1,25 ; dernière ligne le 12 novembre | `registres/depenses.md` l. 416 et 427 ; 0,22692 × 1,25 = 0,28365 | oui |
| Reste 64,44 USD | 65 − 0,56 | oui |
| Second essai : `adresses-sortie` 12:43:59Z ; L1 14:02:19Z ; création 14:31:04Z ; destruction 14:39:50Z ; rapport poussé 14:43:55Z (`3b2a74a2`) | rapport v2 l. 37, 39, 55, 60 ; `registres/depenses.md` l. 427 ; `git log -1 3b2a74a2` : 2026-11-12T15:43:55+01:00 = 14:43:55Z | oui |
| Serveur vécu 9 min (second), 25 min (premier) | 14:31:04 → 14:39:50 = 8 min 46 s ; 23:58:44 → 00:24:07 = 25 min 23 s | oui (arrondis) |
| Environ 30 min d'attente du mot « armée » | 14:02:19 → 14:31:04 = 28 min 45 s | oui |
| Branche `donnees/lean-outillage-d1a-poste-local-v3` à `ae894d8d`, sans commit propre ; branche `…-v4` absente | `git ls-remote origin 'refs/heads/donnees/lean-outillage-d1a-poste-local-v*'` : v1 `1311bc44`, v2 `3b2a74a2`, v3 `ae894d8d` ; aucune v4 | oui |
| « Aucune ligne de registre ni passation ne parle de Lean entre le 13 et le 21 novembre » | `decisions.md` : aucune ligne datée du 14 au 20 contenant « Lean » ; passations : aucun fichier du 14 au 20 ne le contient ; `depenses.md` : dernière ligne du GO le 12 | oui |
| Inventaire Hetzner vide le 21 novembre vers 06:10 UTC | état du chantier, § 2 | oui (repris de la pièce ; non refait ici, lecture seule sans jeton) |
| `rapport-poste-local-d1a-v3.md` absent de `ae894d8d` et de `main` | `git ls-tree -r ae894d8d` ; `ls` du dossier sur `main` | oui |
| Minuterie bornée par `min(création + 48 h, H − 1 h)` | procédure v11, L5, point 4 ; `minuterie_v7.py` l. 984 et `ECHEANCES_H["D-1a"] = 48.0` (`minuterie_v1.py` l. 22) ; `ECHEANCE_MIN_H = 1.0` | oui |
| Renvois à la procédure : section 0 point 3 (jeton), point 4 (hors du bac à sable, essai à blanc), point 7 (secteur, veille coupée, capot ouvert) ; L5 `creer-et-armer` ; `--deja-depense-usd 0.56` | procédure v11, sections 0, 2 ; `minuterie_v7.py` l. 1107 | oui |

## Contrôle 3 — exécutable depuis un poste sous WSL

- **Ordre des gestes** : clone, `fetch` par refspec, contrôle `ls-remote`, branche neuve depuis `ae894d8d`, poussée,
  référence de suivi, contrôle de `V`, lecture de la procédure sous empreinte, empreinte de la consigne sur `origin/main`,
  routine restreinte ; puis section 0 (terminal WSL, essai à blanc avec relance réelle de l'hôte, `adresses-sortie`,
  `stat` 644, secteur et capot) ; L1 à L3 ; attente du mot « armée » ; L4 à L7 ; section 3 ; fin (5 ou 4) ; rapport. Même
  ordre que la procédure v11 et que la v3 jugée exécutable.
- **Commandes complètes** : toutes celles de la v3 (vérifiées alors) ; la commande neuve `git ls-remote origin
  refs/heads/donnees/lean-outillage-d1a-poste-local-v4` est complète. Son critère de réussite est à préciser (**C2**).
- **R10** : aucune commande d'arrêt ni de recherche de processus par motif ; l'essai à blanc arrête son `sleep` par PID
  (`kill <PID>`), la minuterie s'arrête par son PID, le serveur par `detruire --identifiant N`. En fin anormale de la
  création, la procédure (section 4) emploie `detruire --pas d1a`, qui détruit par les **étiquettes fixes et le nom** de
  l'essai (`detruire_pas`, `minuterie_v7.py` l. 379-391 : identité de l'instance côté loueur, jamais un motif de ligne de
  commande) : conforme à R10, mais la v4 l'écrit inexactement (**C1**).
- **Clé du loueur** : `HCLOUD_TOKEN` nommée seule, en quatre endroits (Avant de lancer 3, Dépense, règle 3, procédure
  section 0 point 3) ; jamais affichée, écrite ni passée en argument. Le jeton de `gh` ne passe qu'à `git`.
- **Minuterie de destruction** : L5 (`min(création + 48 h, H − 1 h)`), L6 `verifier-minuterie`, contrôle horaire en
  section 3, arrêt par PID en section 5 ; terminal WSL ouvert jusqu'à l'inventaire final (incident R-2434).
- **R5, aucun repli silencieux** : chaque contrôle en échec porte « arrêt, compte rendu, aucune préparation » ou
  « section 5, compte rendu » ; code non nul du pilote `avant` : ni coupure ni `apres` ; pas `noyau` non conforme : rien
  d'autre. Une seule ambiguïté : le contrôle `ls-remote` (C2), où une erreur d'accès au dépôt rend aussi « rien ».
- **Branche neuve absente du distant** : vérifié ce jour (Contrôle 2) ; le contrôle du mandat le revérifie au lancement.

## Contrôle 4 — la garde d'heure limite et le contrôle `ls-remote` ne cassent rien de la v3

- **Garde d'heure limite** (« aucune préparation si `T_LIM` (L1 + 6 h) tombe après le 2026-11-30 à 23:59 UTC ») : elle
  s'ajoute avant L1 et ne modifie ni `T_LIM`, ni `H`, ni les bornes du code (2 h au moins entre `T_LIM` et `H`, 47 h au
  plus après la préparation). Le harnais a sa propre garde, par **jour UTC** (`garde_go_v1.exiger_go_calcul`, l. 67 :
  `accorde ≤ aujourd'hui ≤ échéance`, appelée par `preparer` et par `creer-et-armer`, `minuterie_v7.py` l. 717 et 936,
  horloge UTC). La garde de la consigne est plus stricte (elle impose L1 au plus tard le 30 novembre à 17:59 UTC) et
  jamais contradictoire : rien de la v3 n'est cassé.
- **Contrôle `ls-remote`** : ajouté à l'écart à la règle 4 des interdits communs (« avant sa création seulement ») et au
  mandat 1, avant la création de la branche ; lecture seule, sans effet sur le clone. `creer-et-armer` fait lui-même un
  `git ls-remote` sur l'amont (code du harnais, l. 797) : c'est un geste du harnais, pas de la session, déjà couvert par
  « la procédure fait foi ». Rien de la v3 n'est cassé.

## Contrôle 5 — ce que Lazar doit préparer

Les onze points sont justes (poste WSL sur secteur, terminal ouvert, `HCLOUD_TOKEN`, `gh`, `IP_POSTE`, outils, hors du
bac à sable et relance réelle de l'hôte, disponibilité pour relayer, réponse sur la branche v3, durée, coût). **Il manque
deux choses que la procédure attend de Lazar lui-même** (**C3**) : son rappel personnel à `H + 1 h` (M6 : console de
Hetzner, zéro serveur attendu ; aussi section 7 de la procédure, garde-fou de fond) et l'accès à la console de Hetzner du
projet, pour détruire à la main par l'identifiant si `detruire` rend le code 3 (sections 4 et 5, table des codes).

## Corrections (texte exact)

- **C1** — bloc « Dépense autorisée », premier point (l. 43-46). Remplacer :
  « Elle est **créée et détruite par la procédure** (création en L5 par `creer-et-armer`, destruction en section 4 ou 5 par
  `MV7 detruire --identifiant N`), **toujours par son identifiant (R10)**. »
  par :
  « Elle est **créée et détruite par la procédure** (création en L5 par `creer-et-armer` ; destruction en section 5 par
  `MV7 detruire --identifiant N`, ou, en fin anormale de la création où l'identifiant peut manquer, en section 4 par
  `MV7 detruire --pas d1a`, qui détruit par les étiquettes fixes et le nom de l'essai), **toujours par l'identité de
  l'instance chez le loueur, jamais par un motif (R10)**. »
  Motif : la section 4 de la procédure v11 prescrit `detruire --pas d1a` ; une session qui chercherait `N` sans l'avoir
  retarderait la destruction.
- **C2** — mandat 1, troisième tiret (l. 99-100). Remplacer :
  « `git ls-remote origin refs/heads/donnees/lean-outillage-d1a-poste-local-v4` ne doit rien rendre ; sinon arrêt, compte
  rendu, aucune préparation ; »
  par :
  « `git ls-remote origin refs/heads/donnees/lean-outillage-d1a-poste-local-v4` doit rendre le **code 0 et aucune ligne** ;
  une ligne rendue (la branche existe déjà) ou un code non nul (accès au dépôt en échec) : arrêt, compte rendu, aucune
  préparation ; »
  Motif : sans `--exit-code`, `git ls-remote` rend 0 et une sortie vide quand la référence manque, mais une erreur d'accès
  (code 128) rend aussi une sortie vide ; « ne rend rien » confondrait les deux (R5).
- **C3** — liste « Avant de lancer », ajouter après le point 11 :
  « 12. **Son rappel personnel à `H + 1 h`** (procédure, M6 : console de Hetzner, zéro serveur attendu ; `H` est donné avec
  le mot « armée ») et **l'accès à la console de Hetzner du projet**, pour détruire à la main par l'identifiant si
  `MV7 detruire` rend le code 3 (sections 4 et 5). »

## Remarques, sans effet sur le verdict

- La v4 et ses compagnons sont déjà sur `origin/main` (commit `3ad6b48e4`, contenu dans `origin/main`) : le contrôle
  d'empreinte du mandat 1 passerait. Après les corrections, c'est la version corrigée (erratum ou v5, au choix de la
  mère) qui doit être sur `origin/main` avant le lancement, et c'est elle que Lazar donne au poste.
- La garde d'heure limite borne la préparation et la création, pas la vie du serveur : avec L1 le 30 novembre, `H − 1 h`
  tomberait le 2 décembre. La fin normale a lieu dans la même session (quelques minutes à quelques heures) et le coût
  attendu reste sous l'heure facturée ; si Lazar lance le 30 novembre, la mère notera que la ligne « en tâche jusqu'à »
  dépasse l'échéance du GO.
- Le point 10 de « Avant de lancer » annonce 2 à 3 heures ; la part après la création n'a jamais dépassé 25 minutes sur
  les deux essais arrêtés au pas `noyau` ; l'épreuve complète et les mesures n'ont pas de durée mesurée : l'estimation
  est dite telle, c'est juste.
- L'en-tête de la v4 ne nomme pas le titre ni l'écart à la règle 4 parmi « ce qui change » ; le différentiel les porte,
  et ils relèvent de la branche neuve. Sans conséquence.
- L'annexe S1 à S8 et la réserve E3 restent dans le texte donné au poste, comme dans la v3 ; la vérification courte de la
  v3 avait déjà dit qu'elles pouvaient en sortir. Sans conséquence.

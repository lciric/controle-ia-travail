# Vérification du différentiel v12 → v13 de la procédure du pilote MR-2 sur machine louée (sans ssh) — v1

- **Lecteur** : vérificateur neuf (R2), auteur d'aucune des pièces. Écrit le 2026-11-16, de 00:33Z à 00:58Z (`date -u`).
- **Pièces lues** (branche `lot/compte-organisme-v1`, commit `2719dcb8320287ebc88cb648175a707a56d37729`, par `git show` et `git diff`) :
  procédure v13 `c90af2756a9d3c1e83d20dd1ca8e273c65b2794fe2e2402cc5b5f26f2218ec55` ; outil v3 `0341fbefb8291ce6955f3cce7952ee440d561d29e5f228b9c7e613320216aee3` ;
  aide v3 `ff76b34a4e64c56455cebea781784a0c08894f677f6432886e487a37273b9a64` ; inchangés dans `sans-ssh-v2/` : amorce
  `93b9c50de967c3da15e21d526ed0123660b6ca5ca0917f0c8d9f838379871bc6`, programme machine `4fa7d368331205346d90599ecc61a489290dd5a1b0aa506c0fd1055ad74ec0f5`,
  aide `8af383f9e894256bfab1691405b1538bfa0b06c5d9b165a63e6480c110ce3c3f`. Référence v12 : commit `85a84ff5daf3c6df4bc0e13c2444eeb51b8d05db`
  (procédure v12 `d0d2c8e1…`, outil v2 `7e66e421…`, aide v2 `2455b3de…`). Sur `main` : vérification de la v12 (`bcdfe138…`), consignes de la
  mère (`90a22eb8…`), R-2947, R-2949, lignes GO-2026-11-14-14, GO-2026-11-15-07, GO-2026-11-15-08, GO-2026-11-16-01 et -02 de `registres/go.md`,
  fin de `registres/arrets.md`.
- **Fait sans dépense ni appel** : aucun appel au loueur, aucune clé lue ni affichée, aucune pièce modifiée, rien committé. Seuls `sans-ssh-v2/`
  et `sans-ssh-v3/` ont été extraits, dans un sous-dossier neuf du bloc-notes ; tous leurs compagnons `.sha256` vérifiés : OK.

## Verdict

**Jouable sous consignes** (liste à la fin). Le différentiel réel est celui que déclare la section 12 decies, retraits compris ; N1 est
corrigé dans le code ; la forme de la création est inchangée à l'octet et le crochet la laisse passer ; les essais rejoués rendent les
mêmes fins que les résultats scellés. Les consignes portent sur trois trous de texte (qui reçoit la phrase, qui agit sur un état
« noeud, machine gardee », reste d'une ancienne heure de fin d'autonomie), sur l'horaire (autonomie jusqu'à 08:13Z) et sur la passe
de B bis accordée cette nuit (GO-2026-11-16-02), qui heurte n7.

## 1. Différentiel réel contre la section 12 decies

**Procédure** (`diff` v12 → v13, 186 lignes) : chaque ligne changée a été rapprochée d'une ligne de la table 12 decies.

| changement trouvé | ligne de la table |
|---|---|
| en-tête : « la session qui lance est la mère ou son opérateur » ; retrait de « une session exécutante ouverte dans le dépôt de travail » | session qui lance |
| en-tête : « Pourquoi une v13 », versions, table des pièces (chemins `sans-ssh-v2/` et `sans-ssh-v3/`, empreintes) | pièces |
| section 0, lignes : GO-2026-11-15-08 et GO-2026-11-15-07 (fin d'autonomie 08:13Z) ajoutés | C1 (rattachement implicite, à peine dit) |
| section 0 : dossier d'envoi `…-envoi-v13`, branches `…-sortie-v13` et `…-entree-v13`, `OUTIL` vers `sans-ssh-v3/` | noms neufs, pièces |
| section 0 : n8 (« une forme trouvée » corrigé) | n8 |
| section 0, exposition : C1, n3 (deux lieux, remplacement des clés), n11 | C1, n3, n11 |
| section 1 : extraction des deux dossiers, `--strip-components=5`, cinq empreintes avec chemins, `variables.sh` aux noms neufs | pièces, noms neufs |
| 2.4 : étiquette `pilote-mr2-v74-v13-AAAAMMJJ` ; 2.5 : `calcul/essai-poussee-session-v2`, annonce n7, **retrait de `num_gpus=0`** de la recherche, bornes « avec ou sans carte » | noms neufs, R-2947, n7 |
| 2.9 : prix relu au plus 0,17 USD/h, **retrait de « 0,20 »** | N1 |
| 3 : « 17 h 05 » (n1) ; phrase n10 | n1, n10 |
| 5 : `shred -u` après un refus avant la poussée | n4 |
| 11 : `verifier-destruction` avant `detruire` (n6) ; `/tmp` après un refus (n5) ; « ou dès la fin du pilote » (C1) | n6, n5, C1 |
| préambule de la section 12 ; section 12 decies ajoutée | rédaction |

Sections 4, 6 à 10, 12 octies et 12 nonies : identiques à l'octet. **Aucun changement non déclaré qui touche une commande ou un attendu.**
L'extraction de la section 1 a été rejouée à l'identique (`git archive` des deux dossiers, `--strip-components=5`) : les cinq empreintes
sont égales, et l'outil v3 trouve l'amorce à `$ENV/outil/sans-ssh-v2/`.

**Outil** (`diff` v2 → v3) — `.sh` : en-tête ; `AMORCE` lu à `../sans-ssh-v2/` (quatre emplois) ; `aide` vers l'aide v3 ; motif d'étiquette
`pilote-mr2-v74-v13-[0-9]{8}`. `.py` : en-tête ; `PRIX_MAX` 0,20 → **0,17** ; contrôle `num_gpus != 0` **retiré**, remplacé par « entier,
non booléen, ≥ 0 » ; nombre de cartes imprimé ; `c_absence` lit et supprime la liste **avant** tout autre contrôle (n5). **Rien d'autre** :
les lignes de la commande imprimée (`L1`, `L2`), la liste des intouchables, l'échéance, `detruire`, les feux sont à l'octet. Restes sans
effet : docstring de `c_offre` (« processeurs seuls … 0,20 », hérité de la v2) et « v2 : v2 : » en tête de l'aide (r1).

**Bancs** : `essai_amorce_v3.py` et `essai_outil_session_v3.py` ne changent que les chemins (v2 lus à côté), les noms v13, l'offre à carte
admise (cas 12), deux cas neufs (étiquette sans v13, prix relu 0,18 et 0,17 sur instance à carte). Doublures inchangées.

## 2. Offre avec carte

- **Bornes inchangées** : `OFFRE_MIN` (4 processeurs effectifs, 8000 Mo, 20 Go), `PRIX_OFFRE_MAX = 0.15` (offre et échéance), `DUREE_S`
  61 200 s ; la recherche garde `cpu_cores_effective>=4 cpu_ram>=8 disk_space>=20 dph_total<=0.15 --storage 20` ; `dph_total` est le prix
  total, carte comprise. Compléments du lecteur sur l'aide v3 : carte 0 ou 2 admises ; `num_gpus` absent, booléen, négatif, chaîne ou
  `1.0` refusés (un `1.0` refusé est un refus sûr, nœud) ; prix 0,1500001, 3,9 processeurs, 7999 Mo, 19,9 Go refusés.
- **Amorce et programme machine v2** : aucune mention de carte, de CUDA ou de pilote ; `nproc` et `MemTotal` sont seulement consignés
  (machine l. 184), jamais jugés ; numpy seul. Rien ne suppose une machine sans carte.
- **Image `python:3.13-bookworm` sur un hôte à carte (non éprouvé)**. L'image Debian complète porte git, curl, openssl, python3 et les
  outils exigés par l'amorce (l. 85-86) ; la carte n'est pas employée. Les autres sessions ont déjà fait tourner des amorces sur des hôtes
  à carte de ce loueur (registre des arrêts, B bis et Neuron Lens ; leurs images non relevées ici). Ce qui se passe en cas d'échec :
  - **refus de l'amorce avant la minuterie** (arguments, outil absent ; l. 37-53, l. 70-86) : l'instance demande sa destruction (DELETE
    trois fois, puis « stopped »), jamais jugée ; **aucune minuterie** n'existe encore ;
  - **image qui ne démarre pas, ou `--args` mal lu** : l'amorce ne tourne pas du tout, **aucune minuterie, aucune autodestruction** ;
  - **échec après la minuterie** (dépôt, commits, empreintes : `sleep infinity`, l. 108-124 ; ou tout arrêt du programme machine) : la
    minuterie détruit à l'échéance ;
  - **conteneur tué après la minuterie** (mémoire, hôte) : la minuterie meurt avec lui ; si le loueur relance le conteneur, l'amorce la
    réarme à la même échéance ; sinon rien ne détruit côté machine.
  Dans les deux premiers cas et le dernier, seule la session ferme : règle des 20 minutes sans branche de sortie (section 3, arrêt (A)
  côté session, destruction), ou section 11 à l'échéance + 5 minutes.
- **Coût au pire** : chemin normal, 17 h × 0,15 = **2,55 USD** ; au prix relu admis, 17 h × 0,17 = **2,89 USD** (17 h 05 : 2,90) ; échec
  précoce avec une session présente : 20 à 30 minutes au plus × 0,17 ≈ **0,06 à 0,09 USD** (le loueur peut facturer pendant le
  chargement : tenu pour vrai). **Sans session présente** (après 08:13Z, session perdue) et sans minuterie : 0,17 USD/h sans borne
  mécanique ; la part machine de 3 USD est dépassée après 17 h 40 ; seule la console du loueur (mère, puis Lazar) ferme. Ce risque
  existait en v12 ; la carte ne le change que par l'image non éprouvée sur ce type d'hôte. Crédit relevé à 5,47 USD (R-2947) : couvre
  2,90 USD, mais pas une seconde machine.

## 3. N1 dans le code

`PRIX_MAX = 0.17` (aide l. 16), jugé dans `c_relire` par `0 < p <= PRIX_MAX`. Rejoué : 0,17 et 0,16999 admis (code 0) ; 0,1700001,
0,18, 0,2031, 0, absent et chaîne refusés (code 2, « la détruire aussitôt »). 17 h × 0,17 = 2,89 USD < 3 USD ; à la borne de l'amorce
(17 h 05) 2,90 USD < 3 USD. **Tenu.** `detruire` ne juge toujours que présence et étiquette (M1, inchangé).

## 4. C1 et C2

- **C1** : la phrase neuve de la section 0 et celle de la section 11 disent ensemble : après 08:13Z, la minuterie agit seule ; la
  session qui lance joue la section 11 à l'échéance + 5 minutes ou dès l'état final poussé, sans mot, ne lance ni ne prolonge rien ;
  à défaut la mère, puis Lazar. **Trois ambiguïtés restent** :
  (a) la phrase précédente garde « fin de l'autonomie à 22:39Z (GO-2026-11-15-03) » (texte de la v12) à côté de « 08:13Z pour
  GO-2026-11-15-07 » (r2) ; (b) « dès l'état final poussé » couvre `noeud, machine gardee`, pour lequel la section 0 dit que le mot de la
  mère fixe le moment de la destruction (et la règle des 40 minutes : « ne pas détruire avant l'échéance sans le mot de la mère ») : le
  texte ne dit pas laquelle prime ; (c) la v13 cite les consignes de la mère (`90a22eb8…`) comme sa source, mais ces consignes nomment
  **la session du compte organisme** comme acteur de la section 11 et comme lieu où Lazar donne la phrase ; la v13 nomme « la session qui
  lance » (mère ou opérateur). Pour la destruction, le sens est sûr ; **pour la phrase, la v13 ne dit pas dans quelle session Lazar la
  tape** (section 5, point 2 : « écrite par la session »), alors que `feu-phrase` doit lire le fichier dans `$ENV` de la session qui lance.
  Une phrase tapée chez le compte organisme et relayée vers l'opérateur passerait par un message entre sessions : exposition que le
  texte scellé et M5 ne prévoient pas. Consigne K1.
- **C2** : `L1` et `L2` de l'outil v3 sont identiques à l'octet à ceux de la v2 (le `diff` ne les touche pas) ; seules les valeurs des
  noms changent (étiquette, branches, dossier). Section 2, point 7 de la procédure : inchangé. **Crochet** (`.claude/hooks/garde_calcul.py`,
  `73be0638…`, `registres/go.md` du dépôt égal à `origin/main`) appelé avec six entrées factices, la commande entière de la section 2,
  point 7 (heredoc, `comparer`, `. a-jouer.txt`), construite par programme depuis la sortie de l'outil v3 au banc, chemin réel
  `/home/user/vastai-env/bin/vastai`, rien exécuté :

  | cas | code | motif |
  |---|---|---|
  | sain, `GO_ID=GO-2026-11-14-14` | 0 | — |
  | sans `GO_ID` | 2 | lancement sans identifiant de GO |
  | `GO-2026-11-14-99` | 2 | absent du registre |
  | `GO-2026-11-15-08` | 2 | type « décision », pas « calcul » |
  | `GO-2026-11-15-04` | 2 | type « décision » |
  | arrêt par motif (`pk…ill -f`) | 2 | R10 |

  Le crochet ne vérifie que la présence de l'identifiant, pas sa place en tête de ligne : la place est tenue par `comparer`. GO-2026-11-14-14
  est valide jusqu'au 30 novembre.

## 5. Noms neufs

`git ls-remote --exit-code origin refs/heads/…` : `calcul/pilote-mr2-v74-sortie-v13` 2, `calcul/pilote-mr2-v74-entree-v13` 2,
`calcul/essai-poussee-session-v2` 2 (absentes) ; `calcul/essai-poussee-session-v1` 0 (présente, laissée par la v12 : le changement de nom
est donc nécessaire). `/home/user/pilote-mr2-v74-envoi-v13` absent ; `…-envoi` et `…-envoi-v12` présents, non ouverts. Le dossier v12 ne
gêne pas : `OUTIL` passe `ENVP=$ENV` (v13) ; seule la valeur par défaut d'`ENVP` dans l'outil reste le dossier de la v10 (en-tête l. 22,
héritée), jamais employée par la procédure (r3). L'étiquette v13 est exigée par l'outil (`commande`, cas « étiquette sans v13 → 2 ») ;
l'étiquette de la v12 n'a servi à aucune instance (R-2947).

## 6. Clés

Inchangé depuis la v12 : les quatre valeurs ne passent que par leurs noms (`${!v}` contrôlé par `grep -q`, rien d'affiché ; `L2` porte
`$GH_TOKEN`, `$RR_ANTHROPIC_API_KEY_RIGAUD`, `$GEMINI_API_KEY`, `$OPENAI_API_KEY`, développés au moment du jeu) ; l'essai des arguments de
l'amorce se fait avec des valeurs factices ; les listes du loueur passent par un fichier privé supprimé. Le cas « aucune valeur imprimée »
et « aucune valeur de clé gardée dans le dossier d'envoi » est conforme au rejeu. Intouchables : même liste dans l'aide et la procédure
(58936096, 58936099, 58936100, 60480302, 60599797, 60670453, plus toute instance non créée par la session) ; refus de `creation` et
`trouver` sur un intouchable inchangé.

## 7. Essais rejoués (bloc-notes, sans réseau, clés factices, outil réel du loueur jamais lancé)

`ESSAI_DEPOT` = le dépôt de travail (lot à `2719dcb8`). Environnement : Python 3.13.18, numpy 2.5.3, git 2.43.0, OpenSSL 3.0.13, 4 processeurs.

| essai | rejeu | scellé |
|---|---|---|
| outil de la session v3 | **39/39 conformes**, mêmes noms de cas, mêmes empreintes d'outil et d'aide | 39/39 |
| 17 scénarios rapides (amorce et programme machine v2 conduits par l'outil v3) | **17/17**, 00:35Z à 00:46Z ; résultats égaux champ par champ aux scellés, heures, PID, commits du banc et durées mis à part | 17/17 |
| scénario intégral (vrai lanceur v74) | **conforme, fini, 1 210 s**, 248 fichiers poussés, aucune fuite, aucun nom interdit ; seule autre différence : l'empreinte du fichier des mondes (secret tiré à neuf) | conforme, 896 s |

Aucun processus du banc restant ; aucun dossier `tmp.*` à `sortie.json` laissé dans `/tmp` par ces rejeux.

## 8. Mineurs n1 à n11 de la vérification de la v12

| mineur | état |
|---|---|
| n1 | traité (section 3 : 17 h 05) |
| n2 | reporté, sans objet neuf (déclaré en 12 nonies) |
| n3 | traité (section 0) |
| n4 | traité (section 5) |
| n5 | traité dans le code (`c_absence`) et par consigne (section 11) ; les autres commandes lisaient déjà la liste d'abord |
| n6 | traité par consigne (section 11) ; l'ordre reste à lire : voir K5 |
| n7 | traité (2.5) ; **mis en défaut par GO-2026-11-16-02** (passe de B bis par un opérateur cette nuit) : voir K4 |
| n8 | traité (section 0) ; parenthèse de la section 7 laissée, sans effet |
| n9 | reporté, sans effet (banc) |
| n10 | traité (section 3) |
| n11 | traité (section 0) ; la v13 elle-même en est l'application |

Aucune régression trouvée : M1 à M5, m1 à m14 de la v12 sont à l'octet dans l'outil et le texte.

## 9. Consignes pour l'opérateur et la mère (avant l'impression de la commande)

- **K1 — Phrase.** Lazar tape la phrase **directement dans la session qui lance** (celle qui porte `$ENV` et joue `feu-phrase`) ; jamais
  relayée par un message entre sessions ni par la mère. Si la session qui lance est un opérateur que Lazar ne peut pas joindre : nœud avant
  la création, rien n'est loué.
- **K2 — Consignes de la mère pour la v13**, écrites avant le préavis : acteur de la section 11 = la session qui lance (à défaut la mère,
  puis Lazar) ; lieu de la phrase (K1) ; heure de fin d'autonomie **08:13Z** (GO-2026-11-15-07), la mention « 22:39Z » de la section 0
  étant caduque ; GO-2026-11-15-08 (écrit pour la v12) tenu pour valant v13, l'exposition étant la même.
- **K3 — Ordre des états finaux.** `fini`, `arret (A)`, `sortie inattendue` : `recuperer`, puis section 11 aussitôt. `noeud, machine
  gardee` : destruction au mot de la mère, au plus tard à l'échéance + 5 minutes ; après 08:13Z, sans mot, à l'échéance + 5 minutes.
- **K4 — Fenêtre seule.** Aucune création ni destruction chez le loueur par une autre session, B bis (GO-2026-11-16-02) compris, entre
  l'inventaire avant (2.3) et la preuve d'absence (section 11) ; sinon jouer B bis avant l'inventaire, preuve d'absence comprise.
- **K5 — Instance peut-être absente** (après l'échéance, après un refus de l'amorce, après la règle des 20 minutes) : commencer par
  `$OUTIL verifier-destruction` ; `detruire` seulement si elle répond « toujours listée ».
- **K6 — Horaire.** Le feu 3 doit tomber avant 08:13Z ; la machine l'exige au plus 4 h 30 après l'impression : imprimer la commande au
  plus tard vers **03:40Z**, Lazar présent pour la phrase dans la demi-heure ; sinon ne pas lancer.
- **K7 — Fermeture sans minuterie.** Dès la création, la session qui lance se pose un rappel à l'échéance + 5 minutes, et le préavis à
  Lazar donne l'identifiant, l'étiquette et l'échéance pour la console du loueur. Branche de sortie absente à 20 minutes : destruction
  sans attendre (section 3), l'image n'ayant jamais tourné sur un hôte à carte.
- **K8 — Crédit.** `$OUTIL credit` doit rendre au moins 5 USD (5,47 USD relevés) ; une seule machine, aucune seconde création.
- **K9 — Crochet.** Éprouvé ici sur la forme exacte (cas sain 0, artefacts 2) ; l'opérateur le réessaie dans sa propre session (section 2,
  point 1), le crochet de son dépôt pouvant différer.

## 10. Restes sans effet

- r1 — docstring de `c_offre` (« processeurs seuls … 0,20 ») et « v2 : v2 : » en tête de l'aide v3.
- r2 — phrase de la section 0 sur 05:39Z et 22:39Z (GO-2026-11-15-03), caduque (K2).
- r3 — valeur par défaut d'`ENVP` = dossier de la v10 dans l'outil ; jamais employée (`OUTIL` passe `ENVP`).
- r4 — le crochet ne contrôle pas la place de `GO_ID` en tête de ligne (tenue par `comparer`).

## 11. Incidents de ma main

- Premier extrait des dossiers avec un mauvais `--strip-components` (6) : fichiers v2 et v3 mêlés dans un dossier du bloc-notes ; supprimé
  aussitôt, réextrait proprement (5) ; empreintes vérifiées ensuite.
- Premier lancement du scénario intégral parti du mauvais dossier courant (fichier introuvable, rien joué) ; relancé.
- Premier relevé des codes du crochet faux (code de `basename` lu à la place de celui du crochet) ; refait, codes justes ci-dessus.
- Laissé dans le bloc-notes (`/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/verif-v13/`,
  534 Mo : pièces extraites, bancs jetables, entrées factices du crochet) et deux copies de lecture des procédures (`v12.md`, `v13.md`) à
  côté ; rien de privé (valeurs factices, phrase de répétition).

# Contre-lecture du moteur v9-v8q (option --cle-gemini), de la voie abonnement v7 et du script de vague v3 — Opus 5.5 (v1)

- 24 novembre 2026, vers 22:20Z. Contre-lecteur neuf : Claude Opus 5.5, qui n'a pas écrit ces pièces. Classe B : contre-lecture, puis vérification des corrections par le même contre-lecteur.
- Rien n'est parti vers un fournisseur : aucun appel réseau, aucune vague, aucun étage hors des essais livrés.
- Toutes mes épreuves ont tourné sans réseau : transport remplacé par une garde qui refuse la connexion ; copies des dossiers dans mon bloc-notes ; valeurs factices, dans un environnement vidé quand il le fallait.
- Les originaux sont intacts : empreintes de tous leurs fichiers comparées avant et après. Aucune valeur de clé n'a été affichée ni écrite.

## Verdict : à corriger (aucun défaut bloquant)

Le changement fait ce que la mère a demandé, et seulement cela :
- les trois lectures de la clé de Google (envoi en flux, envoi par lot, comptage) lisent la variable nommée par `--cle-gemini` ;
- le relevé et l'annulation d'un lot reçoivent la clé ainsi lue ;
- seules Argon, Carbon et Neon reçoivent le nom, et le défaut est inchangé ;
- la reprise des deux dossiers commencés sous v8m tient (épreuve sur copies).

Cinq défauts majeurs demandent pourtant une correction avant de clore la pièce :
1. un repli silencieux vers `GEMINI_API_KEY`, contraire à R5 ;
2. des essais en ligne de commande qui ne restent sans réseau que si la garde éprouvée tient ;
3. neuf de mes dix mutations survivent, dont celles qui écriraient ou afficheraient la valeur de la clé ;
4. la consigne « `GEMINI_API_KEY_FREE` pour Carbon et Neon seulement » n'est pas gardée, alors que l'interdiction de `GEMINI_API_KEY_3` l'est ;
5. un chemin, antérieur au v8q, par lequel la valeur d'une clé de Google partirait vers Anthropic.

Si la mère décide d'employer le v8q avant les corrections, trois précautions suffisent, à la lecture et aux épreuves :
- un lancement avec `--cle-gemini GEMINI_API_KEY_2` ne lit que cette variable sur les trois chemins de Google ;
- ne pas donner `GEMINI_API_KEY_FREE` tant qu'Argon est dans la composition (défaut 4) ;
- ne lancer aucune mutation de ces essais sans couper le transport (défaut 2).

## 1. Empreintes

| pièce | compagnon `.sha256` | vérification |
|---|---|---|
| `collisionneur_v9_v8q.py` | `047489b8d742…` | conforme |
| `collisionneur_v9_v8m.py` (base) | `420394f9d803…` | conforme, intact |
| `test_collisionneur_v9_v8q.py` | `f7f8b951d6ac…` | conforme |
| `rapport-developpeur-collisionneur-v9-v8q-v1.md` | `605bb63c631e…` | conforme |
| `abonnement-v1/voie_abonnement_v7.py` | `fd1c37b7ca96…` | conforme |
| `abonnement-v1/voie_abonnement_v6.py` (base) | `d99f33589507…` | conforme, intacte |
| `reprise-v8d-v1/vague_abonnement_v3.sh` | `51c272401d67…` | conforme |
| `reprise-v8d-v1/vague_abonnement_v2.sh` (base) | `2f7c2ecb3285…` | conforme, intact |

- `MOTEURS["v8q"]` de la voie v7 porte `047489b8d7420c0276f5f65f43519af9b63b4c0d9611becf2eae973663956cf7`, égale au compagnon du v8q. La voie la vérifie avant de charger le moteur (`charger`, l. 111-119).
- Le v8p (`5979c712…`) et l'essaim v7 (`98397f49…`), que la voie référence, ne sont pas sur cette branche. Ils sont sur `runs/collisionneurs-reprise-v8d-v1` : je les ai lus par `git show`, et leurs empreintes sont égales à la table de la voie.
- À l'inverse, la voie v7, le v8q et le script v3 ne sont pas encore sur cette branche des courses : il faudra les y verser avec leurs compagnons avant l'emploi.

## 2. Différences

- **Moteur v8m → v8q** : exactement les six changements annoncés, rien d'autre :
  - l'en-tête et `VERSION` ;
  - deux constantes ;
  - `fixer_composition` ;
  - les trois lectures ;
  - l'option `--cle-gemini` ;
  - `declarer_cle_gemini` et son appel.
- **Voie v6 → v7** : l'en-tête, `VERSION`, l'entrée `v8q` de `MOTEURS` et `v8q` dans les deux listes de commandes (l. 398 et 414). Rien d'autre.
- **Script v2 → v3** : une ligne de commentaire, et l'appel de la voie v7 (l. 13). Rien d'autre. L'en-tête hérité n'a pas été mis à jour (défaut 8).

## 3. Exactitude : ce qui tient, et sur quelle preuve

1. **Aucune lecture à nom fixe dans le moteur.**
   - Les trois seules lectures de Google sont `appeler_gemini` (l. 1519-1520), `appeler_gemini_lot` (l. 1634-1635) et `compter_gemini` (l. 2150-2151).
   - `annuler_lot` (l. 1600) et `relever_lot` (l. 1612) reçoivent la clé lue par `appeler_gemini_lot`.
   - La garde commune `garde_google_v3` ne lit aucune variable d'environnement.
2. **Espèces.**
   - Les trois espèces du catalogue chez Google (argon, carbon, neon) passent par la branche des l. 1125-1126.
   - Toutes les copies d'espèce faites pendant l'exécution (`dict(m, …)`, l. 2478-2554) gardent `nom_cle`.
3. **Fournisseurs croisés.**
   - `--cle-gemini` doit commencer par `GEMINI_API_KEY` (l. 1105).
   - `--cle-openai`, `--cle-mistral` et `--cle-kimi` refusent un nom de Google par leurs préfixes. `--cle-anthropic` aussi, par `PREFIXES_AUTRES_FOURNISSEURS` (l. 503 et 1092).
   - L'adresse de Google est fixe, et les redirections sont refusées.
   - Seul trou : `--nom-espace-anthropic` (défaut 5, antérieur au v8q).
4. **Masquage.**
   - Sur les trois chemins, la valeur lue est celle que reçoivent `envoyer`, `lire_json`, `lire_compte`, `evenements_sse` et `masquer`.
   - Les messages d'absence ne portent que le nom.
5. **Journal.**
   - L'entrée `{"nom_cle_gemini", "quand", "script"}` ne porte aucune des clés que lisent les autres fonctions : `essai`, `cout_usd`, `changement_script`, `ligne_*`, `decision`.
   - `essais_journal`, `depense`, `suivre_scripts`, `verifier`, les lignes de dépense et `ecrire_etat` l'ignorent donc.
   - Aucun outil hors du moteur ne lit ces journaux avec un schéma fermé (recherche dans le dépôt).
6. **Reprise d'un dossier commencé sous v8m.** Épreuve sur copies des deux dossiers des vagues : les idées intéressantes (16 essais) et la conscience et l'émergence (9 essais), tous sous `420394f9…`.
   - Sans `--reprise`, arrêt au code 1. Avec, une entrée `changement_script`.
   - `declarer_options` n'écrit rien de neuf : les réglages sont identiques à ceux du v8m.
   - `declarer_cle_gemini` écrit une entrée.
   - Ensuite, `verifier` rend 0 problème, sous v8q comme sous v8m (0 aussi avant la reprise).
   - Les dépenses restent inchangées : 14,6296 et 8,9492 USD.
   - `devis-reprise` est identique, hors de sa ligne de version ; le plafond de Fable retenu est 128 000 dans les deux cas.
   - Les huit kits déjà écrits sont reconstruits à l'identique par le v8q : leur empreinte est égale à celle de leur fiche. Les réponses recueillies restent donc servables.
7. **`devis`, `devis-reprise` et `verifier`.**
   - Ils sont sans réseau. Ils composent sans le nom, donc avec le défaut `GEMINI_API_KEY`, et ne lisent aucune clé : rien ne casse.
   - L'essaim v7 charge le v8p, pas le v8q (`SCRIPT_MOTEUR`, l. 82 de l'essaim). Il appelle `fixer_composition` de ce moteur par position (l. 925, 1009 et 1299) : l'option ne le touche pas.
8. **Défaut inchangé.**
   - La composition, les lectures et `verifier_cles` sont inchangées. Le devis est identique octet pour octet (essai livré).
   - Par les voies : le devis de la question v4 des idées intéressantes (`texte-servi-idees-interessantes-v4.md`, `b4cf79ef…`) est identique octet pour octet entre la voie v6 avec le v8m et la voie v7 avec le v8q. Je l'ai rejoué ici, environnement vidé.
   - Deux différences de texte, annoncées :
     - une ligne à l'écran, « Clé de Google : variable GEMINI_API_KEY … », à chaque lancement qui sert Google ;
     - un message d'absence plus long.
   - Tout dossier commencé sous v8m exige `--reprise`, même sans l'option : c'est propre à toute version neuve, et c'est annoncé.
9. **Autres commandes.**
   - Dans le moteur, seuls les trois étages lisent la clé de Google. `jev-test` lit celle de Jev ; `devis`, `devis-reprise` et `verifier` n'en lisent aucune.
   - Par la voie v7, les commandes `v8m`, `v8p` et `essaim` lisent toujours `GEMINI_API_KEY` sous un nom fixe (défaut 10).

## 4. Essais et mutations

- **Essais livrés** : 14 sur 14, par le script comme par pytest 9.1.1, en 0,7 seconde. L'arbre de travail reste inchangé.
- **Les quatre mutations du développeur sont tuées**, je le confirme :
  - le refus de `GEMINI_API_KEY_3` retiré ;
  - le contrôle du préfixe retiré ;
  - l'envoi en flux à nom fixe ;
  - le journal muet.
- **Dix mutations du contre-lecteur.** Chacune est faite sur une copie du v8q dont le transport est coupé. Neuf survivent :

| mutation | issue | essai qui la tuerait |
|---|---|---|
| C1 : nom de `--cle-gemini` sorti du contrôle de forme (l. 1095-1096) | survit | « GEMINI_API_KEY-2 » : arrêt « mal formé » |
| C2 : comptage, repli sur `GEMINI_API_KEY` si la variable nommée manque (l. 2151) | survit | comptage avec la variable nommée absente et le défaut présent : refus, aucune requête |
| C3 : relevé du lot à nom fixe, `os.environ["GEMINI_API_KEY"]` (l. 1615) | survit | lot complet sur transport simulé : la clé nommée dans les trois requêtes |
| C4 : en-tête de création du lot portant la clé par défaut (l. 1651) | survit | même essai |
| C10 : annulation du lot à nom fixe (l. 1604) | survit | même essai, délai dépassé sous horloge simulée |
| C5 : valeur de la clé écrite au journal (l. 3336) | survit | journal avec une valeur factice posée : absente du journal |
| C6 : valeur de la clé affichée à l'écran (l. 3337) | survit | même essai, sortie d'écran capturée |
| C7 : défaut de la ligne de commande changé en `GEMINI_API_KEY_2` (l. 3363) | survit | étage sans `--cle-gemini`, aucune variable de Google : arrêt qui nomme `GEMINI_API_KEY` |
| C8 : option lue mais non transmise à la composition (l. 3449) | tuée par les essais en ligne de commande | — |
| C9 : nom journalisé avant le contrôle de `--reprise` (l. 3477-3479) | survit | dossier sous un autre script, lancé sans `--reprise` : arrêt, et aucune entrée `nom_cle_gemini` |

- **Le contrôle textuel (l. 231-234) ne prouve rien pour Google.**
  - Il ne voit ni `os.environ["GEMINI_API_KEY"]`, ni `os.getenv(...)`, ni `NOMS_CLES["gemini"]`.
  - Sa seconde clause, « au moins trois `os.environ.get(nom_cle)` », est vide : trois des six occurrences sont hors de Google (`cle_par_son_nom` l. 1797, `appeler_openai` l. 1923, `compter_openai` l. 2168).
- **Étanchéité au réseau** : voir le défaut 2.

## 5. Défauts

### Majeurs

**1. Majeur : repli silencieux vers `GEMINI_API_KEY` (R5 ; contraire au modèle de `--cle-openai`).**
- Lieu : `appeler_gemini` l. 1519, `appeler_gemini_lot` l. 1634, `compter_gemini` l. 2150, qui lisent `m.get("nom_cle") or NOMS_CLES["gemini"]`.
- Effet : une espèce sans nom part sur `GEMINI_API_KEY`, la clé épuisée, sans rien dire.
- Comparaison avec le reste du moteur :
  - le chemin d'OpenAI refuse ce repli (« jamais de repli sur la clé par défaut », l. 1920 et 2164) ;
  - `cle_par_son_nom` (l. 1792-1800) porte la même règle pour tout le moteur.
- Portée : le repli est inatteignable aujourd'hui par la ligne de commande, car `fixer_composition` donne toujours le nom. Il reste ouvert à tout appelant qui compose autrement.
- Correction :
  - employer `cle, motif = cle_par_son_nom(m, "--cle-gemini", PREFIXE_CLE_GEMINI)` dans les trois fonctions, avec un échec nommé (ou `RefusCompte` pour le comptage) ;
  - refuser aussi, au moment de l'envoi, un nom de `NOMS_CLE_GEMINI_REFUSES` (défense en profondeur) ;
  - ajouter un essai : espèce de Google sans `nom_cle`, rien ne part. Il tue aussi C2.

**2. Majeur : les essais en ligne de commande ne sont pas étanches au réseau.**
- Lieu :
  - `lancer`, l. 186-191 ;
  - `test_ligne_de_commande_refuse_la_cle_epuisee_sans_reseau`, l. 194-202, qui pose `GEMINI_API_KEY_3` à « factice » ;
  - `test_ligne_de_commande_refuse_une_cle_nommee_absente_sans_reseau`, l. 205-213, qui pose `GEMINI_API_KEY` à « factice ».
- Effet : le moteur tourne en sous-processus avec son transport réel. Il ne reste sans réseau que si la garde éprouvée tient.
- Preuve : j'ai placé un espion dans `ouvrir` d'une copie mutée ; il note l'hôte et les noms d'en-têtes, puis refuse la connexion.
  - Avec la mutation du refus de `GEMINI_API_KEY_3`, l'une des quatre du développeur, il relève une requête de comptage vers `generativelanguage.googleapis.com /v1beta/models/gemini-4-argon:countTokens`, avec l'en-tête `X-goog-api-key` (valeur factice).
  - Avec C8, il fait le même relevé dans le second essai.
- Point à éclaircir : le rapport ne dit pas comment les quatre mutations ont été lancées. Si celle du refus l'a été avec ces essais, une requête est partie vers Google avec la clé factice : sans coût, mais contraire à « sans réseau ». Le développeur doit le dire.
- Correction :
  - lancer `principal` dans le même processus, après `mod.TRANSPORT = mod.TRANSPORT_COMPTE = <fonction qui fait échouer l'essai>`, sous `Environnement(GEMINI_API_KEY_3="factice")` ;
  - ou, en sous-processus, passer par une petite enveloppe qui coupe le transport avant `principal` ;
  - exiger le message exact (« est refusée ») et zéro tentative d'envoi ;
  - appliquer la même coupure à toute campagne de mutations.

**3. Majeur : des propriétés annoncées ne sont pas éprouvées (R5 : un cas sain et un artefact par garde).**
- Lieu :
  - `test_journal_du_nom_de_cle`, l. 164-183 : l'assertion « factice absent » (l. 179-180) est vide, car aucune valeur n'est posée pendant l'essai ;
  - aucun essai ne regarde l'écran ;
  - `test_variable_nommee_absente_rien_ne_part`, l. 135-146 : le lot n'est éprouvé que dans le cas d'absence ;
  - `test_aucune_lecture_fixe_de_la_cle_de_google`, l. 231-234 (voir la section 4) ;
  - `test_refus_nom_mal_forme`, l. 98-101 : le nom en minuscules tombe au contrôle du préfixe, et l'assertion ne lit que le code.
- Mutations qui survivent : C1 à C7, C9 et C10 (section 4).
- Correction, essais à ajouter :
  - (a) une valeur factice posée pendant `declarer_cle_gemini` : elle doit être absente du journal et de la sortie d'écran capturée (tue C5 et C6) ;
  - (b) un lot complet sur transport simulé : création qui rend « batches/essai », relevé fini, puis délai dépassé sous horloge simulée pour l'annulation. La clé nommée doit se trouver dans les trois requêtes (tue C3, C4 et C10) ;
  - (c) un étage sans `--cle-gemini`, sans aucune variable de Google : arrêt au code 1 qui nomme `GEMINI_API_KEY` (tue C7) ;
  - (d) un comptage avec la variable nommée absente et le défaut présent : refus, aucune requête (tue C2) ;
  - (e) le nom « GEMINI_API_KEY-2 » : arrêt « mal formé » (tue C1) ;
  - (f) un dossier sous une autre empreinte de script, lancé sans `--reprise` : arrêt, et aucune entrée `nom_cle_gemini` (tue C9).
- Pour le contrôle textuel : le remplacer par une lecture de l'arbre syntaxique, qui refuse tout appel `os.environ.get`, `os.getenv` ou `os.environ[...]` dont l'argument est un littéral `GEMINI_API_KEY…` ou `NOMS_CLES["gemini"]`. À défaut, retirer sa seconde clause.

**4. Majeur : la consigne « `GEMINI_API_KEY_FREE` pour Carbon et Neon » n'est pas gardée, alors que « jamais `GEMINI_API_KEY_3` » l'est.**
- Lieu : `fixer_composition`, l. 1105-1109 et 1125-1126. Un seul nom vaut pour toutes les espèces de Google d'un lancement.
- Effet : les deux dossiers en cours ont Argon dans leur composition. `--cle-gemini GEMINI_API_KEY_FREE` y enverrait Argon sur la clé gratuite.
- Sources :
  - la note d'incident (`6807a3e9…`) : « `GEMINI_API_KEY_FREE` pour Carbon et Neon (mot de Lazar, R-5294) » ;
  - le rapport du développeur, qui range ce point dans ses limites, avec un « par exemple », sans dire que le moteur ne l'empêche pas.
  - R-5294 lui-même n'est pas dans les registres de cette branche (j'ai cherché dans `decisions.md`, `etat.md` et `go.md`) : à confirmer par la mère.
- Correction recommandée :
  - une table `NOMS_CLE_GEMINI_RESTREINTS = {"GEMINI_API_KEY_FREE": ("carbon", "neon")}`, avec un refus au code 1 si une espèce de Google de la composition n'y figure pas ;
  - deux essais : un cas sain (carbon et neon) et un artefact (argon et carbon).
  - À défaut, une phrase explicite dans le rapport et dans l'en-tête du script v3.

**5. Majeur, antérieur au v8q (depuis la v9-v8l) : la valeur d'une clé de Google peut partir vers Anthropic par `--nom-espace-anthropic`.**
- Lieu :
  - `fixer_composition`, l. 1092-1098 : seul `nom_cle_anthropic` est confronté à `PREFIXES_AUTRES_FOURNISSEURS` ;
  - `appeler_anthropic` (l. 1421-1423) et `compter_anthropic` (l. 2139-2141) lisent la variable nommée et l'envoient dans l'en-tête `anthropic-workspace-id`.
- Preuve, dans un environnement vidé, avec des valeurs factices et le transport intercepté : la composition est acceptée avec `--nom-espace-anthropic GEMINI_API_KEY_2`, et la requête vers `api.anthropic.com` porte la valeur de Google dans cet en-tête.
- Portée : hors d'atteinte par la voie abonnement, qui ne fait aucun appel à Anthropic ; ouvert par le moteur nu.
- Correction : le même refus de préfixe pour `nom_espace_anthropic`, avec son essai. À faire dans cette version ou à déclarer comme limite, au choix de la mère, puisque la consigne était « seulement ce changement ».

### Mineurs

**6. Mineur : le motif « clé épuisée » donné pour `GEMINI_API_KEY_3` n'est pas soutenu par la source.**
- Lieu : en-tête l. 7, commentaires l. 518 et 1108, message l. 1109, point 2 du rapport, nom de l'essai `test_refus_cle_epuisee`.
- Ce que dit la source : selon la note d'incident, la clé épuisée (HTTP 402) est `GEMINI_API_KEY`, c'est-à-dire le défaut. La mère écrit « jamais `GEMINI_API_KEY_3` », sans donner de motif.
- Correction : écrire « refusée (consigne de la mère du 24 novembre) ».
- Piège latent : si une version future ajoute `GEMINI_API_KEY`, la vraie clé épuisée, à la liste, alors `verifier`, `devis` et `devis-reprise` s'arrêteront sur tout dossier. En effet, ils composent avec le nom par défaut sans rien envoyer (l. 1173 et 3409). Le refus serait mieux placé là où la clé est lue (les étages), ou appliqué au seul nom donné explicitement.

**7. Mineur : l'en-tête et la docstring décrivent mal la journalisation.**
- Lieu : l'en-tête (l. 7-8) dit « journalisé à chaque lancement qui sert une espèce de Google » ; la docstring de `declarer_cle_gemini` (l. 3328-3329) dit « au premier lancement qui sert une espèce de Google ».
- Ce que fait le code : il n'écrit qu'au premier lancement sous un nom autre que le défaut, puis à chaque changement. Le point 6 du rapport le dit juste.
- Correction : aligner l'en-tête et la docstring sur le rapport.

**8. Mineur : l'en-tête du script v3 est resté celui de la v2, et le code 2 y prête à confusion.**
- Lieu : l'en-tête hérité dit encore « MOTEUR (v8m|v8p) » (l. 7) et « par la voie abonnement v6 » (l. 4).
- Effet : avec v8m ou v8p, `--cle-gemini` est refusée par l'analyse des arguments, au code 2 (éprouvé sur le v8m). C'est le même code que « porte fermée, kits en attente » dans `journal-etage3.txt` et `vague-abonnement-v1.log` : une lecture rapide du journal le prendrait pour une porte.
- Correction :
  - en-tête « MOTEUR (v8m|v8p|v8q) ; --cle-gemini avec v8q seulement » ;
  - un refus nommé, au code 1, de `--cle-gemini` hors du v8q, dans la voie v7 ou dans le script.

**9. Mineur : la voie v7 n'a pas d'essai livré.**
- La v6 en a un, sur la branche des courses. Les deux affirmations du rapport sur la voie ne se rejouent pas depuis les pièces livrées.
- J'ai rejoué la première (devis identique) : elle est vraie.
- La seconde (`GEMINI_API_KEY_3` refusée à travers la voie) demande un lancement d'étage : je ne l'ai pas rejouée, par consigne. Elle est vraie à la lecture.
- Correction : un `test_voie_abonnement_v7.py`, copie des essais de la v6, avec en plus :
  - le chargement du v8q à son empreinte ;
  - le refus d'une copie modifiée ;
  - le devis identique ;
  - le refus de `GEMINI_API_KEY_3`, dans le même processus, transport coupé.

**10. Mineur : par la voie v7, seul le v8q nomme la clé, et ce n'est pas déclaré.**
- Les commandes v8m, v8p et essaim gardent `GEMINI_API_KEY`, la clé épuisée. L'essaim v7 charge le v8p, qui lit ce nom fixe aux l. 1252, 1366 et 1764.
- Correction : une ligne dans le rapport et dans l'en-tête du script v3 : un essaim qui sert Google reste sur la clé épuisée.

**11. Mineur : la docstring des essais (l. 4-5) dit « Aucune valeur de clé réelle n'est lue ».**
- Ce que font les essais :
  - `Environnement` lit les valeurs réelles des quatre variables de Google pour les rétablir ensuite (l. 37) ;
  - `lancer` copie tout l'environnement dans le sous-processus, clés des autres fournisseurs comprises (l. 187).
- Rien n'est affiché.
- Correction : écrire « aucune n'est affichée ni envoyée », ou faire tourner les essais dans un processus enfant à environnement vidé, qui n'en lit aucune.

### Remarques sans défaut
- Le défaut reste la clé épuisée : une vague lancée sans `--cle-gemini` reprendra le refus HTTP 402, qui est un échec sans coût. Le script v3 n'exige pas l'option. À la mère de dire s'il doit l'exiger avec le v8q.
- `declarer_cle_gemini` prend `noms[0]` sans contrôle (l. 3333). C'est juste tant qu'un seul nom vaut pour toutes les espèces. Si la correction 4 passe à un nom par espèce, il faudra journaliser tous les noms.

## 6. Ce que j'ai lancé (tout sans réseau)

- Les essais livrés, par le script et par pytest.
- Les trois différences et la vérification des huit compagnons.
- Le devis de la question v4 par la voie v6 avec le v8m, puis par la voie v7 avec le v8q, dans un environnement vidé de toute clé.
- Cinq épreuves dans le bloc-notes de la session. Il est temporaire ; les descriptions ci-dessus suffisent à refaire les épreuves.
  - La reprise par le v8q sur copies : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/epreuve_reprise_v8m_v8q.py`.
  - Les kits reconstruits : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/epreuve_kits_v8m_v8q.py`.
  - Les mutations, transport coupé : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/mutations_v8q.py`.
  - L'espion des essais en ligne de commande : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/espion_cli_v8q.py`.
  - Les bornes (`--nom-espace-anthropic`, puis `--cle-gemini` donnée au v8m) : `/tmp/claude-0/-home-user-controle-ia-travail/12f6e278-4ba7-598c-9d00-941c25a1615c/scratchpad/epreuves_bornes_v8q.py`.

# Vérification des corrections du code de l'instrument et de l'analyse du bras A, version 8 — v1

**Verdict : engageable après corrections.** Aucun défaut bloquant.

- **Tenu.** Les deux défauts à corriger de la version 7 (C-1 et C-2), et cinq des six mineurs.
  - Une panne à n'importe lequel des trois temps d'écriture ne laisse plus de dossier illisible. Chaque pièce scellée a été éprouvée : fichier d'arrêt, acte de reprise, fichier de l'étape (m) et ses constats.
  - Une lecture interrompue ne se rejoue que sous le même acte.
  - Le registre est lu dans son état figé. Le programme du constat de lancement a un cas sain et des artefacts, et il refuse les valeurs fictives.
- **Tenu en partie.** M-6, comme sa limite l'écrit.
- **Un défaut à corriger (C-1).** Le programme du constat ne reconnaît une révocation qu'à une ligne dont le type est écrit exactement « révocation ». Une révocation tapée « revocation », ou écrite comme une décision qui dit la ligne révoquée, n'est pas vue : le constat sort sain, et la lecture part sous une ligne retirée (essai).
- **L'ajout du calcul des états en fractions exactes** rend la règle exacte sans en changer aucune : démonstration en partie 5.
- **Les cinq défauts de la partie A du relevé** sont des précisions à porter au texte. Aucun n'est une question pour Lazar.
- **Essais : 309 passés.**

## Pièces lues et conditions

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), même contre-lecteur que pour les versions 5 à 7. Il n'a écrit ni code, ni essai, ni texte du dossier.
- **Code** : commit `dd7790b0`. Les neuf modules `*_bras_a_v8.py`, les sept fichiers d'essais et `scripts/constat_de_lancement_discretion_bras_a_v1.py` répondent tous à leurs compagnons. Leurs empreintes sont celles de la note du code, par exemple :
  - `depots_bras_a_v8.py` : `4ed4f03d…` ;
  - `analyse_bras_a_v8.py` : `06009186…` ;
  - programme du constat : `21c38f97…`.
- **Textes** :
  - brouillon 28 (`604e0410…`), par recherches ciblées (constat de lancement, lignes 180, 997 et 1000) ;
  - note du code v8 et relevé v8, en entier.
- **Essais** : la commande de la note donne **309 passés** (63 s) :

  ```
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_analyse_bras_a_v8.py tests/test_verdicts_bras_a_v8.py tests/test_graines_bras_a_v8.py tests/test_cloisonnement_bras_a_v8.py tests/test_permutation_etiquettes_bras_a_v8.py tests/test_mesures_bras_a_v8.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
  ```

  Cette commande contient l'essai du rédacteur qui passe la garde sur le vrai `src/` et le vrai `scripts/`, sous un crochet d'audit qui refuse toute ouverture cloisonnée avant qu'elle ait lieu. Mes propres essais de la garde n'ont tourné que sur un faux dépôt.
- **Essais d'attaque** : données synthétiques et registres fabriqués, dans le bloc-notes, sous `/tmp/claude-0/-home-user-controle-ia-travail/b7727ccc-db8b-5b89-bce1-17602831b69d/scratchpad/contre-lecture-code-v8/`. Chacun a sa sortie `….sortie.txt` :
  - `attaques_v8.py` : pannes à chaque temps, rejeu, constat de lancement, M-3, M-5 ;
  - `fractions_v8.py` : la question 3 ;
  - `audit_cloisonnement_v8.py` : faux dépôt et crochet d'audit, garde et `listages_a_relire` ;
  - `attaques_cloisonnement_v8.py` : les 24 modules plantés de mes essais précédents ;
  - `fuzz_livraison_v8.py` : 400 livraisons altérées au hasard.
- **Heure** : 2026-11-19T18:57Z.

---

## 1. Défauts bloquants

Aucun.

## 2. Défaut à corriger

### C-1. Le constat de lancement ne voit qu'une révocation dont le type est écrit à la lettre
- **Où** : `scripts/constat_de_lancement_discretion_bras_a_v1.py`, `constater`, boucle de la révocation.
  - Il faut `cellules[2].casefold() == "révocation"` ;
  - et que la ligne nomme l'identifiant de la ligne employée.
- **Essais d'attaque** (`attaques_v8.py`, dans une course où la livraison refaite emploie GO-2099-01-01-01) :

  | ligne entrée depuis l'état figé | ce que rend le programme |
  |---|---|
  | type « révocation », qui nomme GO-2099-01-01-01 | constat malsain, non scellé : juste |
  | type « revocation », sans accent | **constat sain, scellé** : la lecture part |
  | type « décision », « GO-2099-01-01-01 est révoqué » | **constat sain, scellé** |
  | type « révocation », qui nomme GO-2099-01-01-011 | sain : juste, l'identifiant est distingué |

- **Pourquoi c'est à corriger** :
  - Le texte (8.4, ligne « constat de lancement ») dit : « une ligne entrée après l'état figé **qui révoque** la ligne de GO employée ». C'est le sens de la ligne qui compte, non l'orthographe de son type.
  - Une révocation manquée fait lire une livraison sous un accord que Lazar a retiré. Le moyen prudent ne coûte presque rien.
- **Ce qui le réglerait** : toute ligne entrée depuis l'état figé qui **nomme l'identifiant de la ligne employée**, quel que soit son type, rend le constat malsain, avec le motif « ligne neuve qui nomme la ligne de GO : à voir ». Un faux malsain se lève par un constat refait après lecture humaine. Un vrai sain manqué ne se rattrape pas. Le texte doit retenir ce sens (partie 6, A.4 (f)).

## 3. Défauts mineurs

- **M-1. La valeur ajustée rapportée peut contredire l'état.** Dans le cas de la partie 5, le résultat porte `valeur_p_haut_holm = 0.05` et l'état « indécis » : la valeur rapportée, calculée en nombres à virgule, est « au plus 0,05 », et l'état exact dit non. Correction : rapporter la valeur ajustée exacte (fraction, ou écriture décimale exacte), ou la marquer « arrondie ».
- **M-2. « Configuration inscrite » est reconnue par n'importe quelle ligne qui cite son empreinte.** Une ligne de type « révocation » qui **retire** la configuration la fait dire inscrite, et le constat sort sain (essai). Correction : exiger une ligne dont le type n'est pas « révocation », ou appliquer la règle prudente de C-1, toute ligne neuve qui retire étant à voir.
- **M-3. Le constat malsain n'est pas gardé.** Ne pas le sceller est conforme à R12 (rien n'est écrasé) et à R5 (l'arrêt est dit, avec un code de sortie de 1 et un message, sans repli). Mais le constat malsain est un fait, une révocation entrée ou une configuration non inscrite. Il ne survit que si la session recopie la sortie au manifeste, ce qui va contre la règle de récupérer ce qui est récupérable et contre R6. Correction : le sceller sous un nom versionné (`constat-de-lancement-malsain-bras-a-<date>.json`) dans le dossier de la livraison. L'analyse n'accepte que le nom du constat sain. C'est le point A.4 (b) du relevé.
- **M-4. Le constat n'est pas lié au moment de la lecture.** Le nom est fixe et rien n'est écrasé (R12) : un constat sain reste dans le dossier.
  - Essai : constat sain, lecture interrompue, révocation entrée, constat refait (malsain, non scellé), rejeu sous la ligne révoquée → lu, sur l'ancien constat.
  - Pour un **rejeu**, c'est conforme au brouillon 28, ligne 997 : une révocation entrée après une lecture ne la retire pas. Mais il faut écrire que le rejeu relève de la lecture déjà partie.
  - Pour une **première tentative** lancée longtemps après son constat, « juste avant la lecture » n'est tenu par rien : la date du constat n'est contrôlée que sur sa présence.
  - Correction : porter l'empreinte du constat dans l'acte de reprise et dans les constats de l'étape (m), pour que le manifeste lie chaque lecture à son constat ; écrire la règle du rejeu au texte.
- **M-5. Limites de la garde statique.**
  - Un lien physique vers un fichier cloisonné est lu (faux dépôt). Git ne conserve pas de liens physiques.
  - Le cloisonnement de T0.8 tient au nom : un programme de T0.8 nommé sans la marque serait ouvert. Une recherche par noms seuls (`shade`, `liars`, `narc`, `t08`, `t0_8`) ne trouve rien sous `src/` ni `scripts/`, et aucun lien symbolique.
  - C'est la liste à confirmer par la session principale (demande 17).

## 4. Corrections de la version 7 → tenue ou non

| défaut v7 | jugement | preuve (rejouée contre v8) |
|---|---|---|
| C-1 registre lu | **tenu** | registre remis comme pièce figée, reconnu à son empreinte ; le registre du dépôt n'est plus lu ; le constat de lancement couvre l'inscription et les révocations entrées depuis ; l'analyse exige le constat (absent : garde ordinaire, rien de lu). Reste C-1 ci-dessus, et M-2 à M-4 |
| C-2 panne | **tenu** | aux trois temps (`_ecrire_le_provisoire`, `_poser_le_compagnon`, `_renommer`), pour le fichier d'arrêt, l'acte de reprise, le fichier de l'étape (m) et ses constats : le dossier reste lisible, les restes sont rapportés (`restes_d_ecritures_interrompues`), la relance achève l'écriture. Lecture interrompue après l'acte : rejeu sous la même ligne (`rejeu_sous_le_meme_acte` vrai) ; sous une autre ligne ou sans ligne, refus ; après le fichier (m), relire est refusé |
| M-1 constats (m), deux réglages | **tenu** | dix champs ; le journal est relu sous `revision_refusee` et `taches_gardees_lues` |
| M-2 dossier de l'appelant | **tenu** (limite écrite) | les dossiers se lisent dans la configuration ; `issues` n'a plus d'argument pour eux. Limite : une autre configuration au dossier vide |
| M-3 demi-pas | **tenu** | 0,5 contre 1 000/2 001 : refusé (essai) |
| M-4 casse | **tenu** | `T07/`, `Bases/`, `SONDES/` et `Mots_Et_Cout_…` sont élagués sur le faux dépôt |
| M-5 doublon intérieur | **tenu** | « pièce illisible », sans moniteur ni dose |
| M-6 module | **tenu en partie** | confronté seulement si `cle_du_module_dans_piece_source` est inscrite ; sinon le résultat le dit |

Fouille de 400 livraisons altérées : 290 arrêts, tous l'événement nommé. Les 110 qui passent ne touchent que des champs sans règle ou rendent des valeurs permises.

## 5. Le programme du constat de lancement, et les fractions exactes (questions 2 et 3)

**Constat de lancement.**
- **Cas sain** : configuration inscrite, aucune révocation. Le constat est scellé et l'analyse lit.
- **Trois artefacts** : constat absent ; configuration non inscrite (malsain, non scellé, garde à l'analyse) ; révocation bien formée (malsain).
- **Valeurs fictives** :
  - un module, un rapport ou un registre à soixante-quatre zéros dans la configuration : refusés ;
  - `GO-0000-00-00-00` dans une ligne d'accord de l'état figé : refusé ;
  - le même identifiant dans une ligne étrangère : n'arrête pas.
- **La portée est juste.** Les seules lignes qui peuvent servir une lecture sont les lignes d'accord de l'état figé et les lignes d'inscription. L'identifiant que l'analyse emploie doit porter la phrase d'accord dans l'état figé, donc il est regardé. Un refus sur une ligne étrangère serait sans remède, le registre ne perdant jamais de ligne.
- **Constat malsain non scellé** : voir M-3.
- **Un constat écrit à la main** (date « x », commit « y ») passe. C'est la limite écrite (A.4 (c)) ; il faudrait au constat l'empreinte du programme.

**Fractions exactes : la règle est rendue exacte, aucune n'est changée.** Démonstration (`fractions_v8.py`) :
- La valeur p haute du juge à la dose 1 est écrite `0.0033333333333333333343`, et sa formule vaut 7 ÷ 2 001 ≈ 0,0034983.
- Les conditions (α) et (β) l'admettent : l'écart est sous le demi-pas, et l'écriture comme la formule sont au-dessus de 0,05 ÷ 15.
- **En nombres à virgule**, l'écriture se lit 0,0033333333333333335 ; 15 × x = 0,05 et x ≤ 0,05 ÷ 15. La fonction de Holm du module **rejette** : le juge « repérerait ».
- **En fractions exactes**, l'écriture dépasse 0,05 ÷ 15 de 10⁻²¹ : pas de rejet, le juge est « indécis ».
- La même lecture écrite par sa formule donne aussi « indécis » (valeur ajustée 0,0525).

La règle (« la valeur p ajustée est au plus 0,05 », sur la valeur rendue telle quelle) porte sur le nombre écrit. Le calcul exact l'applique à ce nombre ; le calcul à virgule l'applique à un autre, celui qu'on obtient après arrondi. L'ajout corrige donc une dérive de l'arithmétique sans changer de règle. Pour des valeurs de la grille (1 + e) ÷ 2 001, aucune n'est jamais égale à un niveau 0,05 ÷ k, puisque 2 001 = 3 × 23 × 29 : les deux calculs ne divergent que sur des écritures inhabituelles. Il reste M-1, l'affichage.

## 6. Les cinq défauts de la partie A du relevé (question 4)

| point | nature | ce qu'il faut écrire |
|---|---|---|
| A.1 arithmétique de l'état | **précision** | « les comparaisons qui disent un état se font sur l'écriture décimale de la pièce, en fractions exactes » ; partie 5 |
| A.2 empreinte de la configuration au rejeu | **précision** (texte, puis code) | un cinquième champ à l'acte, `sha256_de_la_configuration`, vérifié au rejeu ; et, pour une première livraison, que le rejeu se consigne au manifeste par la session |
| A.3 résultat de l'étape (n) sans pièce | **précision** | nommer le fichier scellé des grandeurs de l'étape (n), ou dire que rappeler une étape (n) aboutie n'est pas une relecture : les clés des tirages étant fixées, elle rend les mêmes grandeurs |
| A.4 constat, six points | **précisions** | (a) la ligne de GO en entrée, et un septième champ `ligne_de_go` que l'analyse confronte ; (b) le constat malsain scellé sous un nom versionné (M-3) ; (c) l'empreinte du programme dans le constat ; (d) le manifeste, tenu par la session ; (e) un registre courant qui n'est pas la suite de l'état figé : arrêt, comme le code ; (f) « révocation » au sens prudent de C-1, et « inscrite » au sens de M-2. Aucune ne change une règle de jugement |
| A.5 portée des valeurs fictives | **précision** | la portée du code, juste (partie 5) |

Aucune n'appelle le mot de Lazar. Si l'on voulait qu'une ligne neuve qui nomme la ligne de GO sans la révoquer laisse partir la lecture (A.4 (f)), ce serait une question pour lui. Je ne le recommande pas.

## 7. La garde statique (question 5)

- **Faux dépôt, valeurs par défaut, crochet d'audit écrit à part** (`audit_cloisonnement_v8.py`) :
  - ni `violations_de_la_garde_statique` ni `listages_a_relire` n'ouvre ni ne liste aucun chemin cloisonné ;
  - douze événements pour les listages, dix-neuf pour la garde ;
  - quinze chemins élagués, chacun par son nom, y compris sous une autre casse ;
  - un départ cloisonné, ou par `..`, est refusé ;
  - les liens symboliques ne sont pas suivis.
- **`listages_a_relire` lancée une fois sur le vrai dépôt par le rédacteur** :
  - elle passe par le même parcours, `_lire_les_dossiers` puis `_parcourir`. L'élagage se fait sur le nom, avant tout listage ; elle n'ouvre que des fichiers `.py` non cloisonnés, et ne suit aucun lien ;
  - elle **ne peut ouvrir un chemin cloisonné que si son nom échappe à la liste** : lien physique, ou programme de T0.8 sans la marque (M-5) ;
  - une recherche par noms seuls sur `src/` et `scripts/` ne trouve ni lien symbolique, ni nom de T0.8 sans marque, et les dossiers cloisonnés n'ont que les noms attendus.
  - Je ne l'ai pas relancée sur le vrai dépôt.

## 8. Ce que je n'ai pas regardé
- Les parties de `analyse_bras_a_v8.py` hors de la règle, des états, du constat et des fractions ; `resultat_pour_l_etape_n`, éprouvé seulement par les essais du rédacteur ; `verdicts_bras_a_v8.py` hors de `ecrire_fichier_de_l_etape_m`.
- Les brouillons 26 à 28 et leurs notes et vérifications, hors des recherches citées.

## 9. Fichiers ouverts
- `CLAUDE.md`.
- `docs/notes/relance-organismes-discrets-v1/code-v8-bras-a-note-v1.md` et `defauts-du-texte-trouves-en-codant-v8.md`, en entier.
- `prereg/T0.7-organismes-discrets-v-a-v2-brouillon28.md` : recherches (« révocation entrée »).
- Code : `depots_bras_a_v8.py` et `scripts/constat_de_lancement_discretion_bras_a_v1.py`, en entier ; `analyse_bras_a_v8.py` (lignes 885 à 935, 1040 à 1060, 1140 à 1340, et la garde des constats de l'étape (m)) ; `graines_bras_a_v8.py` (`lire_le_registre_fige`) ; `cloisonnement_bras_a_v8.py` (motifs, `_parcourir`, `_lire_les_dossiers`, `listages_a_relire`).
- `tests/aide_bras_a_v8.py`, en entier.
- Noms seuls (`find`), pour les liens symboliques et les noms de T0.8 sous `src/` et `scripts/`.
- **Non ouverts** :
  - aucun interne de moniteur, aucun module habilité, rien sous `bases/`, `sondes/` ou `t07*/`, rien de T0.8 ;
  - aucune notice ni contre-lecture du côté habilité, aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé ;
  - ni le vrai registre ;
  - aucun appel réseau ni de modèle, aucun sous-agent, rien d'installé, rien committé.

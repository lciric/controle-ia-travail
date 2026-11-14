# Contrôle indépendant « essais et bancs » avant le feu de la relecture exploratoire v2

Début : 2026-11-14 22:33:25 UTC (`date -u`). Fin : 2026-11-14 23:12 UTC (`date -u`).
Contrôleur : sous-agent neuf (modèle C), n'ayant écrit ni l'outil, ni les essais, ni les bancs. Aucun appel réseau (tout sous
`unshare -n`, qui a été accepté), aucune clé, jamais `envoyer`, aucun texte de fiche lu ; rien d'écrit dans le dépôt hors ce
rapport ; `lecture-g1-v3-2` est resté absent (vérifié avant et après). Fichiers de travail (mutants, journaux) dans le dossier
temporaire de la session, hors dépôt.

## Verdict

**Go avec réserves.** Les essais passent (246 + 1 sauté, soit 247 collectés ; le sauté est un essai qui exige un clone de
l'orchestrateur absent ici), et le banc versé est reproduit à l'identique. Les pièces gardent la garde de dépense, l'arrêt à la
première anomalie, la lecture du modèle et du palier servis et le refus d'un dossier existant : chacune est attrapée par au
moins un essai de comportement, sauf les points listés ci-dessous. Aucun trou bloquant pour les 18 appels ; quatre trous
d'essais réels, tous mineurs pour le feu, dont celui des « phrases par fiche », confirmé.

## 1. K1 et K8 (avant), sorties

- K1 : six lignes `OK` (outil, classement, règle v2.1, témoins du lecteur, hasard v2.1, devis v2), code 0.
- K8 (avant) : une seule ligne, `docs/notes/organisme-conception-propre-v1/lecture-g1-v3-1/envois/manifeste-envois-v3-1.json` ;
  `test ! -e $DOS/lecture-g1-v3-2 && echo absent` : `absent`. Revérifié à la fin : toujours `absent`.

## 2. Essais (point 3), joués pour la première fois par un tiers (réserve r1)

Commande du § 6, point 3, mot pour mot, sous `unshare -n` (accepté) : **246 passés, 1 sauté en 42,5 s** (deuxième passe :
246 + 1 en 39,6 s). Les « 247 attendus » = 229 (outil et classement) + 18 (témoins et générateur) : **247 collectés**, dont 1 sauté.

- Le sauté : `test_normalisation_egale_a_celle_de_l_orchestrateur` (`essais_lecture_classement_v3_2_1.py:490`), « clone de
  l'orchestrateur absent » (chemin `/home/user/lciric/ideation-organism/orchestrator/pole/ideation_v2.py`, absent de cette
  machine). Il compare la normalisation typographique de l'outil à celle de l'orchestrateur. Sur la machine de l'opérateur, si
  le clone est là, il ne sera pas sauté ; sinon la mention « 247 passés » du § 6 ne tiendra pas à la lettre. À dire à l'opérateur : « 246 passés,
  1 sauté » est un résultat sain ici, pas une panne. La normalisation typographique intervient dans la vérification des
  citations, pas dans la dépense ni l'arrêt.
- Aucun fichier écrit dans le dépôt par les essais (`git status` propre, `lecture-g1-v3-2` absent).

## 3. Banc de mutations (point 3 du contrôle)

Comment il se joue (en-tête, lignes 1 à 25) : `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mutations_lecture_classement_v3_2_1.py SORTIE.json`.
Chaque mutant est une copie des deux programmes dans un dossier temporaire hors du dépôt, une chaîne remplacée exactement une
fois, les essais rejoués dessous sous `unshare -n`. Je l'ai joué avec `TMPDIR` dans le dossier de session, sortie hors dépôt.

- Rejoué : base 228 passés + 1 sauté, **34 mutants, 32 tués, 0 survivant, 2 inapplicables**, durée environ 6 minutes. Comparé au
  résultat versé `resultat-mutations-lecture-classement-v3-2-1.json` : **mêmes noms, mêmes statuts mutant par mutant**
  (les deux inapplicables : « hasard v2 (remplacé) en entrée » et « règle v2 au lieu de la v2.1 », chaîne mal recopiée, comme
  le dit le rapport). Mon résultat : `scratchpad/mut/resultat-rejoue.json`, sha256 non versé au dépôt.
- Banc du générateur (`outils/mutations_hasard_v2_1.py`, versé : 25 mutants, 23 tués, 2 survivants) : je n'ai pas rejoué le banc
  mais lu les deux survivants.
  - « pièces servies oubliées » : équivalent sur la sortie scellée, comme le dit le rapport (je n'ai pas contesté).
  - **« phrases par fiche non contrôlées » : trou d'essai réel, confirmé.** L'essai d'artefact (`essais_temoins_et_hasard_v2_1.py`,
    lignes 258 à 265) coupe les phrases en morceaux puis exige `not (phrases_dans_iqr and mots_par_phrase_dans_iqr)`.
    Or sur cet artefact les deux contrôles sont faux (sonde : `{'phrases…': False, 'mots_par_phrase…': False}`) ; l'assertion
    passe donc dès que l'un des deux est faux, même si le contrôle des phrases est remplacé par `True` : exactement le survivant.
    Correction possible : asserter `not r["controles"]["phrases_par_fiche_dans_l_intervalle_interquartile"]` seul. Portée : le
    contrôle lui-même tient sur la sortie retenue (valeur 35,5 dans [29 ; 43]), donc aucune conséquence sur le feu ; c'est une
    garde de style des témoins, loin de la dépense.

## 4. Audit R4 « trop propre » : ce que le banc versé vise vraiment

**Le banc versé (34 mutants) ne vise ni la garde de dépense, ni l'arrêt, ni le modèle ou le palier servis, ni le refus d'un dossier
existant** : ses mutants portent seulement sur les changements de la v3.2/v3.2.1 (première lecture, nom de manifeste, plafond
absolu, pièces épinglées, règle v2 au classement). Le reste est couvert par un argument, « code inchangé depuis la v3.1 »,
adossé à 182 mutants de la v3.1 qui n'ont été joués que contre les essais de la v3.1. Un banc entièrement tué prouve donc peu
sur les points qui comptent pour le feu. J'ai fait deux choses pour le mesurer.

**(a) L'argument « inchangé » repose sur un essai de texte, pas de comportement.** `test_regle_de_lecture_inchangee_v3_1_v3_2`
compare l'arbre syntaxique de 50 objets (dont `preparer`, `envoyer`, `bilan`, `analyser_reponse`, `cout_usage`, `main`,
`PRIX_LUS`, `PALIERS_SERVIS_ADMIS`, `ANOMALIES_BLOQUANTES`, `MAX_APPELS`) au fichier de la v3.1. Il tue d'un coup tout mutant de
ces objets, sans dire si les essais de comportement les verraient. Avec `-x`, les 5 sondes ci-dessous ont été tuées *uniquement* par
lui (206 essais de comportement passés avant). C'est une garde utile (la v3.1 a servi une vraie lecture) mais elle rend le « tout tué » trompeur.

**(b) Rejeu des 182 mutants de la v3.1 contre le code et les essais v3.2.1, l'essai de texte écarté** (`-k "not
test_regle_de_lecture_inchangee"`), plus 9 mutants que j'ai écrits (« SONDE »). Harnais : le banc versé, avec sa liste de mutants
remplacée et `jouer` modifié (fichiers hors dépôt dans la session). Résultat : 191 mutants, **178 tués, 6 survivants, 7 inapplicables**
(chaînes de la règle v2 qui n'existent plus dans le classement, déjà remplacées par les mutants de la v3.2.1).
Résultat brut : `scratchpad/mut/resultat-sans-pin.json`, sha256 `41e5b2128f40f0fdb16b156ecc376b62a581266a0e8f4cb3be6ad66a965bbcf2`.

Couverture par thème, les essais de comportement seuls (essai de texte écarté) :

| Thème demandé | Mutants qui le visent | Issue |
|---|---|---|
| Garde de dépense | v3.1 nos 104-119 (coût, plafond, pire cas, dépense passée, plafond absolu, prix nul, journal), 146-147 (dépense antérieure), 154-158 (octets et plafonds), 167-179 (prix flex, source, empreinte, revalidation du manifeste) ; v3.2.1 : « plafond absolu » ; sonde « tolérance de plafond élargie à 1 USD » | tous tués (par comportement) |
| Arrêt au premier appel (`--envois-max 1`) | sonde « `--envois-max` ignoré » ; v3.1 no 103 « pas d'arrêt à la première anomalie », 159, 121-122 (pas de reprise) ; sonde « arrêt au plafond d'appels retiré » | tués. **Survivant** : sonde « `--envois-max 0` accepté » (voir ci-dessous) |
| Modèle et palier servis | v3.1 nos 8, 82, 84-85, 91, 94-95, 162-166, 178 | tous tués |
| Refus d'un dossier existant | v3.1 no 22 « écrasement permis », 143-145 (chemin fixe, unicité, racine) ; sonde « dossier de sortie non vide accepté » | tués. **Survivant** : sonde « écrasement d'un `.sha256` compagnon seul permis » (voir ci-dessous) |

Survivants du rejeu, avec mon appréciation (équivalent, ou vrai trou d'essai) :

1. **Codes de sortie de `main`** (sondes « anomalie = 0 » et « plafond = 0 » : `{"fait": 0, "pause": 0, "anomalie": 3, "plafond": 4}`) :
   **vrais trous d'essai**. Aucun essai ne vérifie le code de fin de `envoyer` ; l'opérateur de l'étape 7 lit ces codes
   (« 0 fait, 3 arrêt sur anomalie, 4 arrêt au plafond, 2 refus »). Le code est juste à la lecture et identique à la v3.1, qui a servi la première lecture
   (garde de texte), donc pas de risque connu, mais le § 6 s'appuie sur une garde que seul l'essai de texte voit.
2. **`--envois-max 0` accepté** (`args.envois_max < 1` devenu `< 0`) : vrai trou d'essai. Avec 0, la boucle ferait « pause » avant
   tout appel (aucune dépense) : inoffensif, mais le refus n'est pas testé. Le § 6 écrit `--envois-max 1`.
3. **Pire cas non recalculé sur les octets** (`pire = max(e["pire_cas_usd"], pire_cas_usd(len(corps), prix))`) : probablement
   **équivalent** : le corps est vérifié par empreinte contre le manifeste juste avant, et le manifeste est revalidé
   (octets et pire cas). Je ne l'ai pas prouvé ; à ne pas compter comme un trou grave.
4. **`.sha256` compagnon seul** (`if p.exists() or Path(str(p)+".sha256").exists()` devenu `if p.exists()`) : trou d'essai réel, très
   mineur (un compagnon orphelin serait écrasé ; le dossier fixe est de toute façon refusé s'il est non vide).
5. **« M2 : lisibilité sans la complétude »** (`lisible = complete and L1["tient"]` devenu `lisible = L1["tient"]`, classement) :
   **vrai trou d'essai apparu avec la v3.2.1**. Ce mutant était tué par les essais de la v3.1 ; les essais v3.2.1, qui ne le
   rejouent plus (le banc v3.2.1 ne porte que 34 mutants), ne le tuent plus : le classement d'une lecture incomplète serait
   déclaré « lisible ». Sans effet sur la dépense ni sur les envois ; effet sur le classement après coup (K9, L1 à L5).
6. Les 5 sondes ci-dessus sont les miennes ; le rejeu des 182 mutants de la v3.1 ne fait ressortir que ce no 5.

Autres limites du rejeu : mêmes auteur des essais et des mutants que ceux du banc versé ; mes sondes ne sont pas exhaustives
(9 seulement) ; je n'ai pas rejoué le banc du générateur. Les survivants 1, 2 et 4 sont dans `main` et l'écriture des
fichiers, que seul l'essai de texte garde.

## 5. Constats pour le feu (classés)

- **Mineur** : « 247 passés » du § 6 est « 246 passés + 1 sauté » sans le clone de l'orchestrateur. À corriger dans le texte de la commande ou à expliquer à l'opérateur.
- **Mineur** : l'essai de texte (`test_regle_de_lecture_inchangee_v3_1_v3_2`) fait porter le « tout tué » du banc v3.2.1 ; sans lui, 1 mutant de la v3.1 sur 175 applicables survit (no 5 ci-dessus) et 4 sondes de `main` et de l'écriture survivent.
- **Mineur** : trous d'essai réels : codes de sortie de `envoyer`, `--envois-max 0`, « lisibilité sans complétude », « phrases par fiche » (confirmé, avec explication de la cause).
- **Information** : les 34 mutants versés sont reproduits sans écart ; aucun survivant ; les gardes de dépense, d'arrêt, de modèle et de palier servis, de dossier existant sont chacune attrapées par des essais de comportement (sauf points ci-dessus).
- **Information** : réserve r1 levée pour les essais joués ; non levée pour l'indépendance du banc (R4).

Aucun de ces trous ne bloque les 18 appels : aucun ne concerne la dépense, le palier, le modèle ou l'arrêt.

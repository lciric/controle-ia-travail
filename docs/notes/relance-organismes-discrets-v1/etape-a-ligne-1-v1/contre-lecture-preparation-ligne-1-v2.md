# Contre-lecture neuve de la préparation v2 de la ligne 1 de carte du bras A

- **Date (UTC)** : 2026-11-23. Lecteur : Claude Opus 5.5, sous-agent neuf (n'a rien écrit des pièces lues). Sur processeur seul : aucune dépense, aucune instance, aucune clé, aucun réseau hors git. Cloisonnement tenu : aucun fichier du guide ouvert, listé ni empreinté ; aucun chemin interdit lu (j'ai, par erreur, listé un dossier de notes très large : seuls des noms de fichiers sont passés sous mes yeux, aucun n'a été ouvert hors de la liste de la mission).
- **Verdict : bon pour le départ**, sous quatre réserves mineures (R1 à R4) à corriger ou à accepter par la session. Aucun défaut moyen ni bloquant. Chacune des corrections de la première contre-lecture (D1, D2, m1 à m5, séquence 8.5) est tenue, deux d'entre elles (m1, m2) par la seule séquence écrite et non par le code.

## Pièces et empreintes recalculées (conformes à celles de la commande)

| pièce | sha256 (début) |
|---|---|
| lanceur v8 | `2663d32d…` |
| configuration v2 du lanceur | `2a17e067…` |
| plan des tâches v2 | `7cc3d4a4…` |

La différence v7 à v8 (`difference-lanceur-v7-v8-v1.diff`) : je l'ai refaite par `diff -u` entre les deux fichiers et comparée à celle du dépôt, hors les deux lignes d'en-tête (noms et dates) : **identique**. Son contenu : la clé `guide` (constantes, `CLES_DU_GUIDE`, `guide_attendu`, `exiger_guide`), `verifier_les_octets_du_guide`, la ligne `guide = exiger_guide(c["guide"])` dans `lire_la_configuration` et son retour, `CHEMIN_DU_LANCEUR`, l'en-tête. Rien d'autre.

La configuration v2 diffère de la v1 par le lanceur (chemin et empreinte) et la clé `guide`, et par rien d'autre. Le plan v2 diffère du plan v1 par le commit de départ, la configuration citée, la date, le lanceur, l'objet, le plan précédent cité et le nom du programme ; **tâches, vérifications, ouvertes, gardées, clés de graines et empreinte des graines identiques**.

## Juge

1. **Configuration** : `lanceur_bras_a_v8.lire_la_configuration(chemin, ".")` passe au départ réel (entropie non fictive, guide rendu aux clés fermées). Le guide ne peut pas être absent, `None` ou un autre : `exiger_guide` exige une table aux cinq clés exactes, l'identifiant « H1-classification », chemins et empreintes égaux aux constantes ; douze artefacts sont essayés (identifiant, chemins, empreintes, majuscules, tronquée, clé en trop ou manquante, non-objet, configuration sans guide). Mon propre essai à la main sur une configuration copiée s'est arrêté plus tôt, faute de compagnon scellé : il ne prouve rien, ce sont les essais du dépôt qui portent la preuve.
2. **Octets avant chargement** : le programme de la course appelle `verifier_les_octets_du_guide` (empreinte sur disque de l'invite et de l'index, lien symbolique et fichier absent refusés) **avant** le déterminisme et avant le chargement du modèle, puis charge par `charger_invite` et recoupe l'entrée de l'index et l'empreinte chargée. Tout écart est un refus avant jeu, code 2. La course ne peut pas recevoir `None` : le texte chargé doit être non vide. **Limite (R3)** : `jouer_ligne_1` du lanceur accepte un guide quelconque, y compris `None` ; la garde est dans le programme de la course, pas dans le lanceur.
3. **Liste blanche** : calculée sur la vraie configuration, 52 fichiers (36 modules, 12 données, 4 du guide). Aucun chemin cloisonné parmi les modules et données (contrôle par ma propre liste de motifs). Les quatre fichiers du guide sont déclarés à leurs empreintes, `lu_par_ce_programme: false`, sans lecture locale (essai dédié, passé). Le programme refuse un autre lanceur, un autre guide, un chemin cloisonné, et l'argument `--guide` n'existe plus (m5 tenue).
4. **Séquence** : versement scellé, committé et poussé **avant** la destruction (section 7, points 1 à 3 ; 8.5 tenu) ; destruction par identifiant à chiffres seuls (R10), code de retour contrôlé, statut relu ; création sous le GO par ligne de commande `vastai` (le piège de la garde est dit) ; prix réel relu et destruction immédiate s'il dépasse le taux du constat (m2) ; création le même jour UTC que le constat (m1) ; conversion de `start_date` écrite ; dossiers distant et local créés d'avance ; cas du manifeste absent traité ; surveillance du processus par son PID à chaque relevé (D1).

## Les corrections de la version 1, une à une (cas sain et artefact)

| correction | tenue ? | cas sain / artefact |
|---|---|---|
| D1, toute exception rendue code 2 (avant jeu) ou 3 (pendant), jamais 1, « FIN » toujours écrit | oui | `OSError` avant jeu (code 2, trace, FIN) ; `RuntimeError` pendant le jeu (code 3, manifeste partiel) ; le journal d'un refus de garde garde sa ligne FIN ; l'écriture du manifeste est aussi protégée. Surveillance du processus dans la séquence. |
| D2, déterminisme et carte au manifeste | oui | `regler_determinisme(fils, "cuda")` (fils de la configuration de référence) avant le chargement, retour dans `resume.determinisme` (carte, capacité, CUDA, cuDNN, pilote, réglages relus) ; refus sans carte ; essai du refus du réglage. Essai long jouet joué selon la note. |
| m1, même jour UTC création/constat | **par la séquence seulement** | voir R1 |
| m2, prix réel relu | par la séquence seulement | voir R2 |
| m3, compteur avant et après le chargement du modèle | oui | essai : plafond franchi avant le chargement, modèle non chargé |
| m4, coupe à 20 % côté course | oui | essai : arrêt au quatrième lot, code 3, quatre lots écrits |
| m5, `--guide` | oui, et mieux : le guide vient de la configuration | `--guide` refusé par la course et la liste |
| 8.5, versement sur branche avant destruction | oui | séquence section 7 |
| précisions (a) à (e) | oui | échec de destruction non silencieux ; `mkdir` distant et local ; manifeste absent ; conversion `start_date` |

## Réponse précise : le noyau d'attention

- **Où le texte scellé en parle** : `grep -n "sdpa\|noyau"` donne, hors table, la ligne 926 (6.10, « Réglages du chargement, fixés ici »), qui fixe « noyau d'attention, `sdpa` pour les deux » : **les deux moniteurs à modèle de langue** (boîte noire par action et juge), « celui avec lequel l'agent est effectivement chargé » ; l'erratum cité (`d59b9d3a…`) dit que le lanceur de l'agent le passe en clair et que la clé `noyau_attention` de la configuration de référence, que ce lanceur ne lit pas, « n'est pas la valeur de l'agent ». Les lignes 2019 et 2054 (13.1) le confirment (case remise puis remplie). La phrase **vise donc les moniteurs**, et constate ce que fait l'agent ; elle ne fixe pas un réglage de l'agent à part de cette constatation.
- **Ce que fait réellement le programme de la course** : `lanceur_bras_a_v2.charger_modele_et_format` appelle `charger_modele(spec["modele"], spec["revision"], "bfloat16", "cuda", "sdpa", hors_ligne=…)` : **`sdpa` et `bfloat16` écrits en dur**, la clé `noyau_attention = « defaut »` de `prereg/T0.6-organismes-config-7b-v1.json` n'est pas lue. L'agent de la ligne 1 est donc chargé en `sdpa`, comme le texte le dit de l'agent. Pas de contradiction pour la ligne 1 ; mais le manifeste ne **consigne** pas le noyau (voir R4).

## Réserves

- **R1 (mineure)** : la règle « création le même jour UTC que le constat » (m1) n'est que dans la séquence ; le code (`compteur_du_constat`) exige seulement création ≥ constat et ≤ horloge. Une création le lendemain d'un constat passerait le programme avec un tarif périmé. Correction possible en une ligne (comparer `creation_utc.date()` à la date de l'horloge du constat) ou accepter comme garde de séquence.
- **R2 (mineure)** : de même, la relecture du prix réel (m2) est un geste de séquence, non un contrôle du code ; acceptable puisque l'instance n'est pas encore chargée à ce moment, mais à dire à la session comme étape à ne pas sauter.
- **R3 (mineure)** : `jouer_ligne_1` n'interdit pas un guide `None` ni autre que celui de la configuration ; seul le programme de la course l'interdit. La règle de la section 10 de la séquence couvre la ligne 2 par écrit seulement.
- **R4 (mineure)** : le manifeste ne porte ni le noyau d'attention ni la précision réellement chargés (`model.config._attn_implementation`), alors que le texte en fait une case remplie ; les relever au journal ou au manifeste lèverait toute équivoque sur « défaut » contre `sdpa`.
- Rappel : le guide n'a pas été confronté ici à ses empreintes sur disque (cloisonnement) ; la séquence l'attribue à une session qui peut ouvrir `docs/sources/` (section 9, point 2), à tenir avant l'archive. La ligne du registre des GO, la clé du hub et l'image CUDA ≥ 13.0 restent à la session (non vérifiés ici).

## Essais (sans `COURSE_LIGNE_1_ESSAI_LONG`)

- `tests/test_lanceur_bras_a_v8.py` : **194 passed** (212 s).
- `tests/test_course_ligne_1_bras_a_v2.py` : **38 passed, 1 skipped** (185 s ; le sauté est le rejeu long, joué par ailleurs selon la séquence).
- Mes contrôles propres : empreintes des trois pièces ; différence v7 à v8 ; différence du plan v1 à v2 ; différences des programmes de la course et de la liste v1 à v2 ; liste blanche réelle recalculée et filtrée.

## Défauts classés

1. **Bloquants** : aucun. **Moyens** : aucun.
2. **Mineurs** : R1, R2, R3, R4.

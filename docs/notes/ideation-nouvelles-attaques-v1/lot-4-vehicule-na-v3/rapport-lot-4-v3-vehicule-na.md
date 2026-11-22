# Rapport du développeur — véhicule NA-1, lot 4 v3 (crédit d'amont rendu en 400)

- Développeur des lots 4 v2 et v3, modèle O. Date (UTC) : 2026-11-22.
- Processeur seul. Aucun appel de modèle, aucune requête vers un fournisseur (seulement le faux serveur des essais, sur `127.0.0.1`), aucune clé, aucune dépense, aucune écriture dans un dépôt, aucun commit.
- Aucun refus d'outil ni de classifieur. Rien n'a été lu sous `/root/.claude/`. Tout a été lu par tranches courtes, sans recherche.
- Pièce qui commande la v3 : la vérification du lot 4 v2, `verification-lot-4-v2.md`, point B1, et son essai `essai_point4.py`, lus en entier. Je n'ai écrit ni l'une ni l'autre.
- Ce rapport ne porte ni chemin complet du bloc-notes ni identifiant de modèle.

## 1. Verdict

- **B1 est corrigé.** Un statut 400 de type `invalid_request_error`, dont le message contient le fragment fixé « credit balance is too low » (comparaison sans casse), est désormais un crédit d'amont. Il lève l'arrêt n° 13, à la première tentative comme en repli, sans second repli.
- La règle est stricte : les trois conditions à la fois. Un 400 d'un autre message ne lève pas le n° 13 ; le fragment sous un autre statut ou un autre type non plus.
- Le message n'est recopié nulle part : ni dans la fiche de la tentative, ni dans le résultat, ni dans `na_replis`, ni au journal des requêtes, ni dans le message de l'arrêt. Il reste dans la seule réponse brute conservée (A4).
- **Essais** : 96 pour le lot 4 v3, tous passés (89 repris de la v2, 7 neufs). Avec les lots 3 v3 et 4 v1, sur une copie neuve : **255 passés, 0 échec** (`journal-essais-na-lot-4-v3.txt`).
- **Mutations : 68 sur 68 tuées.** C'est la liste de la v2 plus 7 neuves (D-34 à D-39, R-29). Le témoin non muté passe, le témoin inerte survit (`journal-mutations-na-lot-4-v3.json`).

## 2. Différence avec la v2

Le différentiel complet, sur les six fichiers, est `differentiel-lot-4-v2-v3.diff`.

| v2 (archivée sans modification) | v3 | changement |
|---|---|---|
| `pole/adaptateur_claude_direct_na_v1.py` (`50563801…`) | `pole/adaptateur_claude_direct_na_v2.py` | ajout de `TYPE_REQUETE_INVALIDE`, de `FRAGMENT_CREDIT_400` et de la classe `ERREUR_CREDIT_AMONT_400` (« crédit d'amont (400, message de solde) ») ; nouvelle fonction `message_de_solde`, qui lit `error.message` du corps et ne rend qu'un booléen ; une règle de plus dans `classer_erreur`, juste après celle du 402 `billing_error` ; version et docstring mises à jour |
| `pole/appel_garde_na_v2.py` (`ac88fdbd…`) | `pole/appel_garde_na_v3.py` | `ERREURS_CREDIT` reçoit `ERREUR_CREDIT_AMONT_400` ; l'import vise l'adaptateur v2 ; version et docstring mises à jour. Aucune autre règle ne change |
| `essais/aides_na_lot4_v2.py` | `essais/aides_na_lot4_v3.py` | `credit_400(message, statut, type_)` ; un message d'essai inerte en casse mêlée |
| `essais/test_na_v2_appel_garde.py` | `essais/test_na_v3_appel_garde.py` | 4 essais neufs dans `TestArret13` : le 400 crédit lève le n° 13 (sans recopie du message) ; le 400 crédit en repli lève le n° 13 (deux requêtes seulement) ; un 400 d'un autre message ne le lève pas ; le fragment sous un autre statut ou un autre type ne le lève pas |
| `essais/test_na_v1_adaptateur_claude_direct.py` | `essais/test_na_v2_adaptateur_claude_direct.py` | `TestCredit400` (règle stricte, sept cas ; message gardé à la seule réponse brute) ; au client réel, contre le faux serveur : 400 crédit, 400 autre, 429 avec le fragment, 402 `billing_error` |
| `essais/mutations_na_lot4_v2.py` | `essais/mutations_na_lot4_v3.py` | D-34 à D-39 et R-29 : règle retirée ; tout 400 lu comme crédit ; fragment lu sous tout statut ; type non exigé ; casse exigée ; message recopié dans la fiche ; classe hors de la liste du n° 13 |

Trois autres programmes sont renommés, sans changement de règle :
- `appliquer_paquet_vehicule_na_lot_4_v3.py` joue les essais des lots 3 v3, 4 v1 et 4 v3 ;
- `ecrire_manifeste_paquet_na_lot4_v3.py` ;
- `manifeste-paquet-vehicule-na-lot-4-v3.json`.

Le paquet v3 ne dépend pas du paquet v2 : il se pose sur les mêmes lots 2 v5, 3 v3 et 4 v1.

**Réserve** : le fragment vient de la forme reçue ce jour sur une clé, telle que la vérification la cite. Si le fournisseur change ce texte, le n° 13 redevient inatteignable par cette voie : la règle ne tient que ce fragment. Le 402 `billing_error` reste lu comme avant.

Les points ouverts du rapport v2 (§ 6) restent ouverts : journal v4, garde Google, valeurs de A7, barème et pires, relevé derrière le vrai relais, flux éprouvé au seul faux client.

## 3. Chemins à lire pour rejouer (liste exacte)

Abréviation : **B** = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.

**0. Base.** Le dépôt `/home/user/lciric/ideation-organism/`, au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, lu par `git archive a41b7b50` puis décompressé dans un dossier neuf. Aucune écriture dans le dépôt. Il faut aussi l'interpréteur `/home/user/controle-ia-travail/.venv/bin/python`, qui porte `pytest` et `anthropic` 2.12.0.

**1. Lot 2 v5** (à poser en premier) :
- `B/lot-2-vehicule-na-v5/appliquer_paquet_vehicule_na_lot_2_v5.py`
- `B/lot-2-vehicule-na-v5/manifeste-paquet-vehicule-na-lot-2-v5.json`
- sous `B/lot-2-vehicule-na-v5/paquet/orchestrator/` :
  - `pole/garde_motifs_na_v4.py`
  - `pole/tirage_na_v4.py`
  - `pole/garde_motifs_na_v3.py`
  - `pole/tirage_na_v3.py`
  - `pole/identifiants_na_v1.py`
  - `pole/extraire_ignorables_unicode_na_v1.py`
  - `pole/ignorables-unicode-15.1.0-na-v1.json`
  - `essais/aides_na_v4.py`
  - `essais/test_na_v4_tirage.py`
  - `essais/liste_reelle_na_v5.py` : copié seulement, jamais joué ici, car il lit la liste réelle
  - `essais/test_na_v5_garde_motifs.py`
  - `essais/sonde_chargement_course_na_v5.py`
  - `essais/mutations_na_v5.py`
  - `essais/controle_ignorables_regex_na_v3.py`
  - `essais/sonde_version_unicode_na_v3.py`
  - `essais/liste-motifs-essai-na-v1.json`
  - `essais/source-unicode-15.1.0/DerivedCoreProperties.txt`

**2. Lot 3 v3** :
- `B/lot-3-vehicule-na-v3/appliquer_paquet_vehicule_na_lot_3_v3.py`
- `B/lot-3-vehicule-na-v3/manifeste-paquet-vehicule-na-lot-3-v3.json`
- sous `B/lot-3-vehicule-na-v3/paquet/orchestrator/` :
  - `pole/requete_na_v3.py`
  - `pole/journal_na_v3.py`
  - `essais/aides_na_lot3_v3.py`
  - `essais/test_na_v3_requete.py`
  - `essais/test_na_v3_journal.py`
  - `essais/mutations_na_lot3_v3.py`

**3. Lot 4 v1** :
- `B/lot-4-vehicule-na-v1/appliquer_paquet_vehicule_na_lot_4_v1.py`
- `B/lot-4-vehicule-na-v1/manifeste-paquet-vehicule-na-lot-4-v1.json`
- sous `B/lot-4-vehicule-na-v1/paquet/orchestrator/` :
  - `pole/routage_na_v1.py`
  - `pole/appel_garde_na_v1.py`
  - `pole/adaptateur_claude_na_v1.py`
  - `pole/faux_fournisseur_na_v1.py`
  - `pole/releve_sans_systeme_na_v1.py`
  - `essais/aides_na_lot4_v1.py`
  - `essais/test_na_v1_appel_garde.py`
  - `essais/test_na_v1_adaptateur_claude.py`
  - `essais/mutations_na_lot4_v1.py`

**4. Lot 4 v3** (ce dossier) :
- `appliquer_paquet_vehicule_na_lot_4_v3.py`
- `manifeste-paquet-vehicule-na-lot-4-v3.json`
- `ecrire_manifeste_paquet_na_lot4_v3.py` : seulement pour réécrire le manifeste
- sous `paquet/orchestrator/` :
  - `pole/appel_garde_na_v3.py`
  - `pole/adaptateur_claude_direct_na_v2.py`
  - `essais/aides_na_lot4_v3.py`
  - `essais/test_na_v3_appel_garde.py`
  - `essais/test_na_v2_adaptateur_claude_direct.py`
  - `essais/mutations_na_lot4_v3.py`

**Commandes**, dans l'ordre. Le paramètre `--destination COPIE` vaut pour chaque programme. Les essais du lot 4 v1 n'ont pas besoin de `--lancer-essais`. Ensuite :
1. `python -B appliquer_paquet_vehicule_na_lot_4_v3.py --destination COPIE --lancer-essais` ;
2. puis, dans `COPIE/orchestrator`, `python -B essais/mutations_na_lot4_v3.py JOURNAL-NEUF.json`.

Lancer les deux sans `ANTHROPIC_API_KEY` dans l'environnement (`env -u ANTHROPIC_API_KEY`).

Les essais lisent aussi des fichiers de la base, à l'empreinte du manifeste : `pole/__init__.py`, `adaptateurs.py`, `caviardage.py`, `outils.py`, `relais.py`, `noyau_v56.py`, `suivi_roles_v54.py`, ainsi que `essais/__init__.py`, `conftest.py`, `aides.py` et `aides_v53.py` à `aides_v56.py`.

## 4. Livré (dossier `vehicule-na-lot-4-v3/` du bloc-notes)

- le paquet (six fichiers) ;
- les programmes d'application et du manifeste, et le manifeste ;
- les journaux des essais et des mutations ;
- `differentiel-lot-4-v2-v3.diff` ;
- ce rapport ;
- `table-empreintes-dossier-na-lot-4-v3.txt`, avec un compagnon `.sha256` par fichier de la table.

`copie-neuve/` reste hors de la table.

— développeur du lot 4 v3 du véhicule NA-1, modèle O

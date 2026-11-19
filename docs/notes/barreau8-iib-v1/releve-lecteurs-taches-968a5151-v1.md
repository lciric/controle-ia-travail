# Relevé des lecteurs des fichiers de tâches, au commit de lancement `968a5151` — v1

Exécutante du saboteur à budget, sur le mot de la mère (R-3619), en lecture seule, sans toucher au code. Contrôle croisé pour le développeur de `prep/iib-code-v4`. Exploratoire, non opposable (R-522).

Forme réelle des deux fichiers cités par la configuration (`donnees/20261007-082440-t05-extraction/taches-entrainement.json` et `taches-evaluation.json`) : objet de premier niveau `{manifeste_sha256, resultat, run_id}` ; liste sous `resultat.taches` (32 et 64 éléments ; clés d'un élément : `cibles`, `classification`, `couts_rapportes`, `empreintes`, `identifiant`, `questions`) ; aucune clé `taches` au premier niveau.

Méthode : recherche dans `scripts/lancer_iib_v1.sh`, `scripts/amorce_instance_iib_v1.sh`, les autres scripts `*iib*`, le paquet `src/controle_ia/iib/` et les modules qu'il importe pour les tâches, des lectures de `taches`, `resultat`, `taches_reserve`, `taches_evaluation`, `charger_taches`, `identifiant`.

| Lieu | Ligne | Ce qui est lu | Forme attendue | Sur la forme réelle |
|---|---|---|---|---|
| `scripts/lancer_iib_v1.sh` (`controles-explo`, contrôle de disjonction) | 105-108 | les deux fichiers extraits du commit | `json.load(f)["taches"]` : liste au premier niveau seulement | **échoue** (`KeyError: 'taches'`) : défaut relevé aux contrôles à blanc |
| `src/controle_ia/iib/lanceur_v1.py`, `charger_entrees` (course, sur l'instance) | 84-85 | les deux fichiers, par `charger_taches` | voir la ligne suivante | lit (vérifié : 32 et 64, 0 commune) |
| `src/controle_ia/environnements/pilote_a.py`, `charger_taches` (appelé par la course) | 51 | un fichier de tâches | `brut["resultat"]["taches"]` si `resultat` existe, sinon `brut["taches"]` : accepte les deux formes | lit |
| `src/controle_ia/iib/jouet_v1.py` (répétition jouet) | 108-109 | fichiers de tâches qu'il fabrique | il écrit la forme plate `{"taches": [...]}` | sans objet (fabrique ; c'est cette forme plate que voient les essais du lanceur) |
| `src/controle_ia/iib/configuration_v1.py` | 317-327 | les entrées `taches_reserve`, `taches_evaluation` de la configuration | `{chemin, sha256}` et égalité aux chemins et empreintes réels ; n'ouvre pas les fichiers | sans objet |
| `scripts/lancer_iib_v1.sh` (`controles-explo`, sceaux des fichiers cités) | 100-103 | contenu brut des fichiers et de leurs sceaux, pour l'empreinte | aucune forme JSON | passe |
| `scripts/amorce_instance_iib_v1.sh` | — | aucune lecture de liste de tâches (vérifie seulement les sceaux des fichiers cités, l. 320) | — | — |
| `scripts/lecture_iib_1_dommage_v1.py`, `scripts/lecture_iib_2_diffusion_v1.py`, `scripts/repetition_jouet_iib_v1.py` | — | aucune lecture de fichier de tâches de `donnees/` | — | — |

Gardes de la course sur les tâches, vérifiées sur les fichiers réels avec la configuration finale : réserve 32 = épisodes par tour 32 ; 32 × 2 honnêtes = 64 = épisodes de E-O3 ; 32 × 1 flagrant = 32 = épisodes de E-O4 ; évaluation 64 = 64 attendues ; identifiants sans double, énoncés non vides (`charger_taches` passe sans garde levée).

Conclusion : un seul lecteur échoue sur la forme réelle, le contrôle de disjonction du lanceur (`lancer_iib_v1.sh` l. 108). Le chargeur de la course accepte les deux formes ; la décision de la mère (refuser toute autre forme que `resultat.taches`) le changerait aussi, ainsi que la forme écrite par `jouet_v1.py`.

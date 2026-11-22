# Rendu du développeur neuf — lanceur v4 et commande v9 du réajustement de nos lentilles (variante B) — v1, 2026-11-22

Mandat `mandat-developpeur-lanceur-v4-commande-v9-reajustement-v1.md` (`6ed54244…`, vérifié). Rien n'a été loué, lancé ni dépensé ;
aucune requête au loueur ni à la plateforme de modèles ; aucune clé lue (noms seulement) ; aucune lecture de `diag/`, `runs/`,
`docs/verdicts/` ni des branches interdites (les champs des pièces du 18 sont pris dans le critère v8, § 2, et dans le code de la v3).

## Verdict
Le lanceur v4 (items (a) à (m), un changement nommé par item), le module de rangement, l'amorce et la commande v9 sont écrits et
essayés sur jouets : essais neufs 74 passés ; banc d'altérations 32 tuées sur 32 ; essai à blanc v4 **conforme, 0 écart**. **Prêts pour
la contre-lecture**, pas pour la création : le transport réel du rangement n'est pas essayé, et les préalables du devis (ligne de GO,
dépôt et clé, relevés de la plateforme, textes de la variante B) ne sont pas levés.

## Fichiers neufs et empreintes
`empreintes-lanceur-v4-v1.txt` (scellé). Table « item → changement → essai sain → essai artefact » : `table-items-lanceur-v4-v1.md`
(scellée). Nom de la clé restreinte dans le conteneur de la session : **`HF_TOKEN_RANGEMENT`** ; sur la machine elle s'appelle `HF_TOKEN`
(nom lu par la bibliothèque de la plateforme et par le balayage). Dépôt de rangement : variable `DEPOT_RANGEMENT`, jamais écrit en dur.

## Écarts au mandat, déclarés
- **Noms** : l'amorce livrée est la **v5**, le dépôt réduit la **v5**, l'essai à blanc la **v4**, les essais du lanceur
  `test_neuron_lens_b_beta_lancer_v4_v2.py`. Cause : j'ai scellé des brouillons trop tôt (commit `443bd8d3f`) ; l'outil de scellement
  a ensuite refusé une nouvelle empreinte au même nom (R12) ; refus déclaré, non contourné ; ce qui devait changer a pris un nom neuf.
  Les brouillons restent tels quels (la v1 des essais, déplacée sans modification hors des essais collectés, dans `brouillons-scelles/`).
- **Lanceur v3 gardé dans l'arbre réduit** : la partie 2 v3 (inchangée) en importe des constantes, égales à celles de la v4 (essai).
- **Essai à blanc v3 non conforme** (12 écarts, cas nominal seul) : un essai embarqué importait le programme de comparaison, absent de
  l'arbre réduit. Corrigé dans la v2 des essais ; essai à blanc v4 conforme.

## Comptes des essais (2026-11-22, `.venv`, python 3.13 du conteneur)
- `tests/test_neuron_lens_b_beta_lancer_v4_v2.py` : **48 passés** (dont 2 `copie_reelle`, écartés sur la machine) ;
  `…_etapes_b_beta_v6.py` : **24 passés** ; `…_montage_b_beta_v4.py` : **2 passés**.
- `tests/test_neuron_lens_*.py` : **995 passés, 214 en échec**, tous dans des fichiers que ce développement ne touche ni n'importe :
  `comparer_reajustement_v4` (183) et `_v3` (24) — le commit `5e5cb65b…` du 18 n'est pas dans cet arbre de travail (il est au distant,
  branche `course/neuron-lens-b-beta-reduit-v3` : la commande v9, étape 14, demande de le récupérer avant la comparaison) ;
  `controles_b0_v2` (2 : une source `docs/sources/neuron-lens-v2-addendum-20261114/` absente) ; `suivi_vast_v6` (5 : modules
  `suivi_vast_v2` et `_v5` absents). Non examinés plus avant.
- Banc d'altérations (`banc_alterations_lanceur_v4_v1.py`, sortie scellée) : 32 sur 32 ; la v1 des essais en laissait 5 (corrigé).
- Essai à blanc v4 : nominal 247 essais réels passés dans l'arbre réduit ; 0 écart sur tous les cas.

## Nœuds (écrits, datés du 2026-11-22 ; le reste a continué)
- **N-1** garde de priorité d'une autre étape : non armée par défaut, armée sur le seul mot de la mère (commande v9, étape 10 bis).
- **N-2** recopie après une relecture de la session en échec : aucun canal sans ssh ; reprises faites sur la machine seulement (deux par
  fichier, vérification à l'arrivée), puis « pas sans la mère ».
- **N-3** GO attendu : faute de ligne, le lanceur ne vérifie que la forme, la date (≥ 2026-11-22) et l'exclusion des deux lignes du 18 ;
  la garde réelle est le crochet de calcul et la ligne inscrite par la mère. Autre voie, non écrite : graver la ligne dans l'arbre réduit
  à sa construction (la liste attendue en dépendrait).
- **N-4** relevé de prix : la commande garde le script v3 et lit ses colonnes de base ; le devis v9 parle de colonnes pour les deux
  options ; non écrit (borne basse de 1,49 USD/h calculée dans la commande).

## Expositions
- La clé restreinte reste sur la machine toute la course (configuration de l'instance chez le loueur, processus d'entrée de l'amorce) ;
  aucun processus enfant ni aucune étape « sans clé » ne la reçoit ; le balayage la cherche avant chaque poussée (quatorze formes
  rejouées après les copies : refusées). L'outil de suivi est appelé avec `HF_TOKEN="$HF_TOKEN_RANGEMENT"` pour qu'il la balaie aussi.
- `hf_xet` (dépendance de la bibliothèque de la plateforme) peut écrire un cache pendant l'envoi : non établi ; l'empreinte rendue par
  la plateforme peut n'être que celle que déclare l'envoyeur : la relecture de la session se fait en flux par défaut.
- Les inventaires portent les noms et empreintes de tous les fichiers de la course (aucune valeur de mesure).

## Pour le contre-lecteur (lire dans cet ordre)
1. `CLAUDE.md` ; le mandat ; le devis v9 (§ 5) ; le critère v8 (§ 2, 4, 5, 7).
2. `src/controle_ia/neuron_lens/b_beta_lancer_v4.py` (comparer à `b_beta_lancer_v3.py` : `diff`), `src/controle_ia/neuron_lens/rangement_lentilles_v1.py`.
3. `scripts/amorce_neuron_lens_b_beta_v5.sh` (comparer à `amorce_neuron_lens_b_beta_v3.sh`), `scripts/depot_reduit_neuron_lens_b_beta_v5.py`.
4. `tests/test_neuron_lens_b_beta_lancer_v4_v2.py`, `…_etapes_b_beta_v6.py`, `…_montage_b_beta_v4.py` ; `developpement-v4/banc_alterations_lanceur_v4_v1.py` et sa sortie.
5. `scripts/essai_a_blanc_amorce_neuron_lens_b_beta_v4.sh` et `developpement-v4/essai-a-blanc-amorce-b-beta-v4.txt` (et la v3, non conforme).
6. `docs/notes/neuron-lens-v1/commande-b-beta-v9.md` (comparer à `commande-b-beta-v8.md`) ; `developpement-v4/table-items-lanceur-v4-v1.md`.

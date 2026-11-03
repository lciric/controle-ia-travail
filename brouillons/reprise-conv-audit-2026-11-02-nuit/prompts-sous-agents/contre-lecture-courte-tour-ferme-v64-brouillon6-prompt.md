Tu es un contre-lecteur neuf (règle R2) : tu n'as écrit ni le code du tour fermé (v60 à v64), ni l'étage des tests de mort, ni ses préenregistrements, ni les contre-lectures précédentes. Français, sans sigle non développé ; heures par `date -u`.

## Objet
Tour fermé, étage 1 (GO-2026-11-02-23, 50 USD) : code **v64** (commit public `63ed933`, fichiers neufs : `pole/tour_ferme_v64.py`, `pole/adaptateur_commande_v64.py`, `demonstrations/tour_ferme_v64.py`, `demonstrations/lire_tour_ferme_v64.py`, `essais/test_tour_ferme_v64.py`, `essais/test_gardes_tour_ferme_v64.py`, `essais/mutations_tour_ferme_v64.py`) et **brouillon 6** (`prereg/preenregistrement-tour-ferme-v1-brouillon6.md`, `cdcb4470…`), dans `/home/claude/ideation-organism/orchestrator/`. Lis :
- le rapport du développeur `prereg/rapport-redaction-tour-ferme-v6.md` (ses dix points d'abord) ;
- le brouillon 5 et les couples T101 à T112 (`prereg/couples-contre-lecture-tour-ferme-v5.json`), la contre-lecture courte précédente `prereg/contre-lecture-courte-preenregistrement-tour-ferme-v5.md` ; les 69 couples v64 du développeur : `/home/claude/scratch/tour-ferme-v64/brouillon6/couples-v64-brouillon6.json` ;
- la vérification des commandes par session-depot : `/home/claude/scratch/tour-ferme-v64/session-depot_2026-11-02_n294.md` (§ 4, TF-01 à TF-06) et `…/n295.md` (§ 3) ; la configuration v3 brouillon 1 : `/home/claude/scratch/tour-ferme-v64/configuration-tour-ferme-v3-brouillon1.json` ;
- décisions : TF-02 options (a) et (c) (directeur, 3 novembre) ; garde de 72 h (Lazar, R-1294).

## Questions
1. La lecture du code 4 « rien envoyé » (`envoye=false`) en « budget_depasse » : juste, limitée à ce cas, et sans masquer un vrai arrêt (plafond de la course, part du relais) ? Les refus propres du relais (402, 429) lus en code 4 deviennent des fins de tours : est-ce acceptable, ou faut-il exiger une cause sur la dernière ligne des commandes v3 ? Recommande.
2. Le barème `prix_entree_usd_par_million_jetons` (clé neuve, sans défaut) : chemin jusqu'à la vérification préalable, refus si absent, ordre des gardes.
3. 72 h : constante, refus de toute autre durée en mode décisif, seuils de la section 12 recalculés (le développeur dit ≈ 3,7 fois plus large).
4. Brouillon 6 = brouillon 5 + T101 à T112 + 69 couples v64 + bloc d'empreintes, et rien d'autre ? Zones de l'étage 2 identiques à l'octet ? Aucune prédiction ni critère changé ? Bloc de 92 empreintes égal au disque et à la fermeture des imports ? Marqueurs restants exactement `<<CASE_CONFIGURATION_V3>>`, `<<COMMANDES_V3>>`, `<<PRECISION_GO_23>>` ?
5. La proposition de borne du vérificateur à 0,15 USD (non faite, recommandée « ne pas relever ») : ton avis.
6. Tout ce qui rendrait la course non concluante par défaut de conception.

Tu peux rejouer : `cd /home/claude/ideation-organism/orchestrator && TMPDIR=/tmp POLE_ESSAI_BAC_REEL_NON_JOUE=1 nice -n 10 python3 -I -B -m pytest -q -p no:cacheprovider essais/test_tour_ferme_v64.py essais/test_gardes_tour_ferme_v64.py`, le banc de mutations **une fois**, et une course à blanc dans le bac factice dans un dossier sous `/home/claude/scratch/tour-ferme-v64/contre-lecture/`. **Attention** : une course décisive (`demonstrations/banc_tricheurs_v9.py`) tourne dans ce clone ; n'ouvre ni ne liste `../resultats/banc-tricheurs-v9-validation-v1/`.

## Rendu
Fichiers neufs : `orchestrator/prereg/contre-lecture-courte-preenregistrement-tour-ferme-v6.md` (verdict en trois lignes ; bloquants, importants, mineurs) et, s'il y a des corrections de texte, `orchestrator/prereg/couples-contre-lecture-tour-ferme-v6.json`. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`/`checkout`/`stash`, aucun appel de réseau ni de modèle, `nice -n 10`. Réponse finale : verdict, points une ligne chacun, chemins et sha256.

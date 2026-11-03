Tu es le contre-lecteur neuf (règle R2) du **pilote préenregistré de l'exposant p** (programme de contrôle de Lazar Ciric). Tu n'as écrit ni ce préenregistrement, ni son code, ni sa lecture du papier. Français, sans sigle non développé ; toute heure vient de `date -u`. Dépôt `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04` (lecture seule ; lis `CLAUDE.md` : R1 à R14).

## Objet
Le pilote mesure, sur Llama-3.1-8B-Instruct, l'**exposant p** de Ferreira da Silva et Heimersheim (arXiv 2606.24964 : perturbation à norme constante dans le plan de deux directions, angle de rupture du plateau, superellipse, p ≈ 2 sans privilège, p > 2 directions pures privilégiées) pour une direction d'**évaluation** E contre une direction de **registre** R à statut d'évaluation constant, avec témoins. Dis s'il est **scellable** (R1 : hypothèse, prédiction chiffrée et signe, métrique, seuil, plan d'analyse, critères gelés, liste d'arrêt ; R3 : aucun run visant un signe positif ; R5 : gardes éprouvées sur un cas sain et un artefact ; R7 : chiffres de la littérature vérifiés en source).

## Fichiers (tous scellés comme brouillon ; vérifie chaque compagnon par `sha256sum -c`)
- `brouillons/pilote-exposant-p-v1/` : `preregistrement-pilote-exposant-p-v1-brouillon1.md`, `lecture-2606-24964-v1.md`, `stimuli-pilote-exposant-p-v1.json`, `config-pilote-exposant-p-v1.json`, `puissance-pilote-exposant-p-v1.json`, `devis-pilote-exposant-p-v1.md`, `rapport-redaction-pilote-exposant-p-v1.md` (ses **dix points pour le contre-lecteur**, section des points, et sa liste de fichiers : suis-la).
- Code : `src/controle_ia/pilote_exposant_p/` (dont `amont/`, copies du code publié du papier, et `references_publiees/`), `tests/test_pilote_exposant_p_v1.py`, `scripts/pilote_exposant_p_instance_v1.sh`.
- Le papier : `https://arxiv.org/pdf/2606.24964` (par `WebFetch`, en entier, par tranches avec `offset`), et son code publié tel que copié dans `amont/` (provenance dans `amont/PROVENANCE.json`).

## Ce que tu fais
- Suis les dix points du rapport du rédacteur, puis ceux-ci : la règle à trois issues (au-dessus, égal, au-dessous des plans de référence) est-elle ouverte dans les deux sens, et ses phrases gelées disent-elles ce que chaque issue **ne** montre **pas** (couche 2, dernier jeton, ancres de 5 jetons ; une issue « égal » ne dit pas que la direction d'évaluation est sans privilège aux couches moyennes) ? le témoin positif (Wealth × Gender, p = 3,003 sur le modèle de base) et les isotropes valident-ils vraiment l'instrument sur le modèle Instruct ? la règle d'exclusion par le cosinus (|cos| ≥ 0,1) est-elle celle du papier ? les quinze écarts au papier sont-ils tous déclarés ?
- Rejoue les essais : `cd /home/claude/controle-ia-travail && PYTHONPATH=src nice -n 10 .venv/bin/python -I -B -m pytest -q -p no:cacheprovider tests/test_pilote_exposant_p_v1.py` (sans réseau ; sans carte) et rejoue la simulation de puissance si le script le permet ; dis ce que tu obtiens.
- Vérifie que le code ne lit rien d'autre que ce que le texte déclare, et que le script d'instance ne dépense rien sans GO (garde de calcul `GO_ID=…`), ne pousse que sur une branche `calcul/…` neuve, et s'arrête proprement.

## Rendu
Rapport `/home/claude/scratch/pilote-p-contre-lecture/contre-lecture-pilote-exposant-p-v1.md` : verdict (scellable / scellable après couples / non scellable) ; bloquants, importants, mineurs ; couples « ancien → nouveau » (texte exact, chaque « ancien » unique) dans `couples-contre-lecture-pilote-exposant-p-v1.json` ; ce que tu as rejoué et ses empreintes. Réponse finale : verdict, comptes, chemins et sha256.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch`, `checkout`, `stash` ; aucun appel de modèle autre que toi ; aucune carte, aucune dépense ; `WebFetch` pour le papier seulement.

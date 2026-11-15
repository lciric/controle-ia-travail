# Brief de reprise — fille « Neuron Lens », sur un autre compte Claude — v1

Écrit le 2026-11-15 vers 18:45 UTC par la session `session_016QhUrtahFZo57fZUcRReVA`, à la demande de Lazar, transmise par la mère
(`session_016QhUrtmLyFWJP6Cy7rgfXH`). À lire en entier par la session neuve, avant tout geste. **Ne rien lancer de payant sans GO écrit et
feu de la mère.**

## 1. Où en est le travail
- Tranche **B-α** (Llama 3.1 8B Instruct, lentilles publiques de Neuronpedia), GO-2026-11-14-06 : **terminée**. Trois courses :
  - instance 60770175 : arrêt à B0 (lanceur v1) ;
  - instance 60773264 : arrêt dans `measure`, mémoire de la carte épuisée ;
  - instance 60783204 : course terminée, commande v5, `measure --ctx-batch 16`.
  Dépense ≈ 2,0 USD sur 12. **Verdict rendu par un lecteur neuf, sur `main`** :
  `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md` (`ca06acb1…`, R-2915) : reproduction « partielle », aucune chaîne en
  défaut. **B-β n'est pas accordée.**
- Volet A (GO-2026-11-14-05) : terminé, lu (verdict `lecture-volet-a/verdict-volet-a-v1.md`).
- **Prochaine action : aucune sans mot de la mère.** Points ouverts pour une version suivante :
  `docs/notes/neuron-lens-v1/constats-a-porter-b-alpha-v1.md` (`essais_ok=True` en dur dans le lanceur v3 ; `pytest` à épingler) ;
  `test_cibles_invisibles_v4` avant toute fusion de la branche dans `main` (décision de la mère).
- Dernière passation : `docs/notes/neuron-lens-v1/passations/2026-11-15-1842.md`.

## 2. Dépôt et branches
- Dépôt de travail : `https://github.com/lciric/controle-ia-travail` (privé). **Jamais** pousser vers `lciric/controle-ia`.
- Branche de la fille : **`prep/neuron-lens-v1`**. Jamais `main`, jamais `registres/` : les lignes de registre sont proposées à la mère,
  qui les inscrit.
- Branches de course (lecture seule, historiques) :
  - dépôts réduits : `course/neuron-lens-b-alpha-reduit-v4`, `-v5`, `-v6` ;
  - résultats : `calcul/neuron-lens-b-alpha-v1`, `-v2`, `-v3`.
  Une course neuve prend **des noms neufs** (R12), et la branche de résultats doit être absente avant la création.
- Dépôt voisin, lu seulement : `stdlogits/neuron-lens` au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, cloné en lecture à
  `/home/user/stdlogits/neuron-lens`. **Jamais exécuté dans le conteneur** (décision (a) de Lazar, R-2710) : seulement sur la machine louée.

## 3. Routine de reprise (CLAUDE.md, R14)
1. `cd docs && sha256sum -c sha256sums-lancement-v2.txt`, puis `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .`.
   Environ 104 échecs préexistants hors de `docs/notes/neuron-lens-v1/` : ils ne sont pas de la fille ; le dire, ne pas les « réparer ».
2. `git fetch origin prep/neuron-lens-v1 main`, puis passer sur `prep/neuron-lens-v1`. Lire `registres/etat.md` **sur `main`** et la
   dernière passation de `docs/notes/neuron-lens-v1/passations/`.
3. Inventaire des instances par le suivi, jamais par une sortie brute :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v6 instances`. Toute instance de la fille sans tâche s'arrête
   par son identifiant (R10). **Intouchables** : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, `poste-temoin-bailey-*`, et
   toute instance d'une autre session.
4. Tests : la suite complète est longue (plus de 6 500 essais). Les essais de la fille suffisent à la reprise :
   `PYTHONPATH=src python -m pytest -q tests/test_neuron_lens_b_alpha_lancer_v3.py tests/test_neuron_lens_grandeurs_b_alpha_v1.py tests/test_neuron_lens_addendum_partie2_b_alpha_v1.py tests/test_neuron_lens_balayage_arbre_v1.py tests/test_neuron_lens_verdicts_b_alpha_v3.py`
   (≈ 144 passés). `test_cibles_invisibles_v3` échoue sur `volet_a_chargement_v1.py::garde_rendu` : connu, il attend la v4.
5. Coordination : la mère est `session_016QhUrtmLyFWJP6Cy7rgfXH`. Si le nouveau compte ne la joint pas, demander à Lazar l'identifiant de
   la mère active.

## 4. GO en cours et leurs bornes
- **GO-2026-11-14-06** (B-α, calcul) : ligne de 12 USD, échéance 2026-11-30, RTX 4090.
  - Bornes des feux : R-2887 (prix lu ≤ 0,73 USD/h), puis R-2892 et R-2904, avec les consignes P1, R1 et R4.
  - Préavis d'une ligne avant la création et avant la destruction, puis geste sans attendre (R-2883).
  - Tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère (R-2864).
  - B-α est finie : **aucune nouvelle location sans un mot neuf**.
- **GO-2026-11-15-04** (décision) : passage de `HF_TOKEN` à une machine louée, pour le seul téléchargement de Llama, retiré ensuite.
- **GO-2026-11-15-03** : autonomie jusqu'au 2026-11-15T22:39Z. **Échue pour une reprise ultérieure** : redemander à la mère.
- Les lignes exactes sont dans `registres/go.md` et `registres/decisions.md` sur `main` (R-2725, R-2783 à R-2915).

## 5. Clés nécessaires, par leur nom seulement (jamais de valeur)
- `CONTROLE_IA_GITHUB_TOKEN_2` : jeton du programme, pour pousser et cloner. Il est passé à une machine sous le nom `GH_TOKEN`, par
  `--env`. Il est **exigé** par `suivi_vast_v6`, qui refuse sans lui.
- `VAST_API_KEY` : outil du loueur `vastai`.
- `HF_TOKEN` : accès contrôlé à `meta-llama/Llama-3.1-8B-Instruct`, et seulement pour cela. Il doit être présent dans la session pour que
  le suivi balaie aussi sa forme. **Révocation recommandée** : il a été passé à trois machines louées.
- `HCLOUD_TOKEN` : inventaire Hetzner de la routine de reprise, noms et identifiants seulement.
- Ne jamais afficher, écrire ni verser une valeur ; ne jamais imprimer `vastai show … --raw` ; `env` et `printenv` sont interdits. Avant
  chaque commit de journaux de course, passer le balayage :
  `GH_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2" PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.balayage_arbre_v1 <fichiers>`.

## 6. Environnement à recréer sur le nouveau compte
- Environnement de ce compte : « Default », personnel, **réseau sans restriction** ; aucun script d'installation ; aucun secret de réseau.
  Variables présentes (noms) : `BRAVE_API_KEY`, `CONTROLE_IA_GITHUB_TOKEN_2`, `GEMINI_API_KEY`, `GEMINI_API_KEY_2`, `HCLOUD_TOKEN`,
  `HF_TOKEN`, `JEV_API_KEY`, `KIMI_API_KEY`, `OPENAI_API_KEY`, `OPENALEX_API_KEY`, `OSF_TOKEN`, `RR_ANTHROPIC_API_KEY`, `_2`, `_3`, `_LUC`,
  `_RIGAUD`, `RR_ANTHROPIC_WORKSPACE_ID`, `RR_TYPESAFE_API_KEY`, `SEMANTIC_SCHOLAR_API_KEY`, `VAST_API_KEY`. **Pour la fille « Neuron
  Lens », il faut au minimum** : `CONTROLE_IA_GITHUB_TOKEN_2`, `VAST_API_KEY`, `HF_TOKEN`, et `HCLOUD_TOKEN` pour la routine.
- Hôtes utilisés, si le réseau est restreint : `github.com`, `huggingface.co` et ses domaines de fichiers, `console.vast.ai`, le dépôt
  public des journaux du loueur (`s3.amazonaws.com`), `pypi.org` et `files.pythonhosted.org`, `api.hetzner.cloud`.
- Outils à recréer :
  - environnement du dépôt : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ;
  - outil du loueur à part : `python3 -m venv /home/user/vastai-env && /home/user/vastai-env/bin/pip install -q vastai==1.11.0` ;
  - préambule de chaque commande de location :
    `cd <dépôt> && export PATH=/home/user/vastai-env/bin:$PATH VASTAI_OUTIL=/home/user/vastai-env/bin/vastai &&` ;
  - copie de lecture du voisin :
    `git clone https://github.com/stdlogits/neuron-lens /home/user/stdlogits/neuron-lens && git -C /home/user/stdlogits/neuron-lens checkout 849bfe1678e28becceb1e3864afe5fc8297d02e4`.
- Garde de calcul du dépôt (`.claude/hooks/garde_calcul.py`) : toute commande qui crée une instance doit citer `GO_ID=GO-…` d'un GO
  « calcul » de `registres/go.md`.

## 7. Pièces qui servent si une course B-α (ou B-β, si elle est accordée) repart
- Dernière commande jouée : `docs/notes/neuron-lens-v1/commande-b-alpha-v5.md` (`423b74b4…`).
- Pièces de la commande v5 : lanceur `src/controle_ia/neuron_lens/b_alpha_lancer_v3.py`, amorce `scripts/amorce_neuron_lens_b_alpha_v5.sh`,
  dépôt réduit `scripts/depot_reduit_neuron_lens_b_alpha_v6.py` (liste `0293f4e1…`), minuterie
  `scripts/minuterie_destruction_neuron_lens_v4.sh`, garde `src/controle_ia/neuron_lens/garde_depense_v4.py`, suivi `suivi_vast_v6.py`,
  essai à blanc `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v8.sh` (à lancer entrée fermée : `< /dev/null`).
- Leçons à garder :
  - `vastai destroy … -y < /dev/null`, et l'absence se prouve par `suivi_vast_v6 absente <ID> --non-vide` (le témoin 60480302 n'existe
    plus) ;
  - le PID se lit dans le fichier écrit par le processus, jamais `$!` ;
  - le conteneur de la session peut redémarrer : veille et réarmement sur l'échéance absolue ;
  - `measure` sur une RTX 4090 exige `--ctx-batch 16` ;
  - le corpus tourne en ligne et sans clé (accepté par la mère).
- Journaux des courses : `journal-course-b-alpha-v1.md`, `-v2.md`, `-v3.md` (scellés).

## 8. Interdits en vigueur (rappel)
Ceux de `CLAUDE.md`, plus pour cette fille :
- rien dans `registres/` ni sur `main` ;
- code voisin jamais exécuté dans le conteneur ;
- aucune valeur de secret affichée ou écrite ;
- aucun nom de modèle dans les rapports archivés ;
- aucune location sans GO écrit, feu et devis ;
- aucun contournement d'un refus ;
- jamais toucher les intouchables du § 3 ;
- jamais écraser un fichier scellé (une nouvelle version prend un nouveau nom).

## 9. Machines actives
**Aucune** de la fille (relevé du 2026-11-15T18:42Z : sur le compte du loueur, seules 58936096, 58936099, 58936100, à l'arrêt, d'une
autre session). Aucun automate vivant : ni minuterie, ni garde, ni veille, ni rappel programmé.

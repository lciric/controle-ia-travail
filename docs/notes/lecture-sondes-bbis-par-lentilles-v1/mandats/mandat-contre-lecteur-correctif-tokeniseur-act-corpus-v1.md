# Mandat du contre-lecteur neuf — correctif du tokeniseur demandé par le script voisin du corpus (lanceur v9) — v1

Rédigé par la session des lentilles (session_01Qi7Gr3vedYVukbyqBbHd7z) le 2026-11-21, sous les mots de Lazar « turbo max » et « go tu as
mon mot pour tout » (GO-2026-11-21-63). Tu n'es pas l'auteur du code ; tu es d'un autre modèle que lui. Français.

## Ce que tu juges
Le correctif poussé au commit 9e078c7fc (fusion 2b4c3672f) sur `claude/brave-galileo-jhp684`, écrit sous le mandat
`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-correctif-tokeniseur-act-corpus-v1.md` (4420c6df…).
Défaut corrigé : au montage, le script voisin `05_act_corpus.py` s'arrêtait sur un refus 401 du dépôt à porte (fichier `tokenizer.model`),
dans un enfant sans clé. Voie retenue : marqueurs d'absence du cache de `huggingface_hub` pour les trois fichiers que la bibliothèque
demande et que le dépôt ne porte pas, plus un essai en ligne et sans clé du chargement du tokeniseur avant tout flux long.
Question : **le lanceur v9 et le module `cache_tokeniseur_v2` peuvent-ils remplacer le lanceur v8 pour la première passe, sans rien
changer à ce que le texte de lecture v1 scellé exige, et le chargement du tokeniseur dans l'enfant sans clé réussit-il réellement ?**

## Pièces (vérifie chaque empreinte scellée avec `PYTHONPATH=src python -m controle_ia.scellement verifier <chemin>`)
- le mandat du développeur ci-dessus ; `CLAUDE.md` ;
- `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/notes-correctif-tokeniseur-act-corpus-v1.md` (cecbad87…) ;
- `src/controle_ia/lentilles_sondes_bbis/cache_tokeniseur_v2.py` (fb4069f7…), `lanceur_v9.py` (89d2e23b…) contre `lanceur_v8.py`
  (0bba5d4e…) ; `montage_v1.py` (`environnement_enfant`, `poser_cache_tokeniseur`, `calculer_jetons_gardes`) ; `constantes_v1.py` ;
- `tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py`, `tests/lentilles_sondes_bbis_jouets_v9.py` contre la v8,
  `tests/test_lentilles_sondes_bbis_lanceur_v9_*.py` et les autres copies v9 ;
- sous `developpement/outils/` : `fabrique-lanceur-v9-v1.py`, `essai-des-essais-cache-tokeniseur-v1.py` et sa sortie,
  `porte-locale-chargement-tokeniseur-v1.py` et sa sortie ;
- la copie versée `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/neuron_lens-catalog.py.txt` ;
- la trace `traces/hf-revisions-20261006-1645/` : son `LISEZMOI.md`, ses empreintes, et du fichier du modèle Llama-3.1-8B-Instruct le
  champ `sha` et la liste des fichiers seulement ;
- `requirements-cpu.txt` ; dans `transformers` installé (`.venv`) : `utils/hub.py`, `tokenization_utils_base.py` ; dans `huggingface_hub`
  installé : la résolution du cache et des marqueurs `.no_exist` ;
- `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (sur `origin/main` si absent), « Plan d'analyse » point 4 et ce qui touche au montage
  et aux essais d'un octet, **sans la liste « Jamais ouverts »**.

## Points à trancher, chacun « tenu » ou « à corriger » avec raison
1. Mécanisme : dans les versions épinglées, un marqueur `.no_exist/<révision>/<fichier>` suffit-il pour que `transformers` ne demande
   plus ce fichier à l'hôte, en ligne ? La liste des trois noms (`tokenizer.model`, `added_tokens.json`, `chat_template.jinja`) est-elle
   complète pour un tokeniseur rapide Llama 3.1 ? Y a-t-il d'autres fichiers demandés (configuration de génération, `special_tokens_map`,
   fichiers du processeur) qui tomberaient sur la porte ?
2. Révision : la bibliothèque résout-elle la branche principale en commit sans clé (API du dépôt à porte) ? Si la révision résolue diffère
   de la révision épinglée, les marqueurs sont-ils ignorés, et l'arrêt est-il nommé avant tout flux long ?
3. Garde « fichier présent dans l'arbre » : lit-elle la racine avec la clé sans l'exposer ? Aucun marqueur n'est-il écrit pour un fichier
   que le dépôt porte ?
4. L'essai en ligne et sans clé (nœud 1 du développeur) : utile, sans risque d'exposition de la clé, retirable ? Tient-il le texte scellé
   (aucune requête nouvelle hors des hôtes déjà essayés) ?
5. Lanceur v9 = v8 à ce seul changement près ; `MODULES` (quinze) et contrôle des empreintes contre la fiche ; aucune ligne de calcul
   changée ; aucune clé exposée.
6. Les essais prouvent-ils le défaut (artefact qui reproduit le refus 401 de l'ancien code) et la correction (R5) ? L'essai des essais
   tient-il ? La porte locale est-elle fidèle au comportement du dépôt à porte ?
7. Nœud 2 du développeur : `scripts/05_act_corpus.py` n'a pas été lu. Cherche s'il est versé quelque part dans les sources du dépôt
   (`docs/sources/neuron-lens-lecture-20261113/`) ; s'il l'est, dis s'il demande autre chose au dépôt à porte. S'il ne l'est pas, dis-le.
8. Tout autre écart bloquant.
Rejoue `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python -m pytest -q tests/test_lentilles_sondes_bbis_cache_tokeniseur_v2.py tests/test_lentilles_sondes_bbis_lanceur_v9_*.py`
(environnement : `.venv` existant du dépôt, `requirements-cpu.txt`) ; comptes seulement. **Aucune requête vers Hugging Face**, aucun
téléchargement, aucune clé ; lecture de pages web publiques et de code source public permise.

## Cloisonnement
Jamais `diag/`, `runs/`, `docs/verdicts/`, branches `calcul/*` `donnees/*` `verdict/*`, fichiers « consigne-privee » ou « conception-ii-b » ;
aucune sortie, aucun score, aucune table, aucun verdict de l'apprentissage des sondes sur la tâche ni de la lecture par la lentille publique
(`arret.json` compris) ; rien de P3, P3-bis, T0.6, T0.7 hors des textes de lecture. Intitulé interdit vu : déclaré. Refus d'outil jamais rejoué.

## Rendu
Écris `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lectures/contre-lecture-correctif-tokeniseur-act-corpus-v1.md`, scelle-le, ne
committe pas (la session des lentilles committe). Dernier message : verdict « conforme » ou « à corriger » en une à trois lignes ; points
1 à 8 ; corrections demandées, bloquantes ou non ; empreinte de ton fichier.

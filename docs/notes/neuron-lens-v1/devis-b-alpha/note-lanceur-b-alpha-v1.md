# Lanceur de la course B-α — pièce 4 du § 6 du devis B-α v2 — note v1

Écrite par la fille « Neuron Lens » le 2026-11-15, sur l'accord de la mère (R-2863). Aucune machine, aucune dépense ; code voisin non
exécuté dans le conteneur (R-2710).

## Pièces
- `src/controle_ia/neuron_lens/b_alpha_lancer_v1.py` : le lanceur (une étape par appel ; `suite` donne la prochaine étape et
  l'environnement qu'elle demande : `jeton` ou `sans-jeton`, `en-ligne` ou `hors-ligne`).
- `tests/test_neuron_lens_b_alpha_lancer_v1.py` : 48 essais dans le conteneur, cas sains et artefacts. Ils couvrent l'environnement
  par étape, les processus enfants sans secret, le délai dépassé, les bilans de pytest, l'épinglage du cache, les attendus du hub,
  l'ordre des étapes, la reprise, les préalables, l'arrêt consigné sans écrasement, un résultat altéré, les audits joués seulement
  s'ils sont requis, B0, la garde de la partie 2 avant la fumée, le téléchargement du tokeniseur avec une clé jamais transmise à un
  enfant ni envoyée à un autre dépôt, le cas sain de l'audit « tout négatif », les intervalles reproductibles, et `preparer` sur une
  vraie copie du code voisin à `849bfe16` (`git archive`, rien d'exécuté : les quatre correctifs donnent les empreintes attendues ;
  reprise ; un fichier voisin modifié = arrêt).

## Étapes (ordre du devis v2, § 1)
`preparer` → `telecharger-tokeniseur` (clé) → `b0` → `telecharger-poids` (clé) → `corpus` → `partie2` → `fumee` → `passe` → `b3` →
`measure` → `score` → `grandeurs` → `verdicts` → (`audit-trop-beau`, `audit-tout-negatif`, seulement si `verdicts` les requiert).
Chaque étape faite laisse `diag/<run_id>/b-alpha-<étape>.json`, scellé et rattaché au manifeste, avec sa durée, l'échéance du devis
(attendu, pire cas) et le dépassement éventuel. Une étape faite n'est jamais rejouée. Toute erreur laisse
`arret-<étape>-<n>.json`, sans écrasement.

## Points à contre-lire (écarts à la lettre du devis, déclarés)
1. **Corpus en ligne, sans clé.** Le devis (§ 5) dit `HF_HUB_OFFLINE=1` « pour tout le reste » après les téléchargements. Or
   `05_act_corpus.py` lit ses quatre tranches **en flux** sur le hub : il ne peut pas tourner hors ligne. L'étape `corpus` (et elle
   seule avec l'audit « tout négatif », qui télécharge Qwen3-8B, public) tourne donc **en ligne, sans clé**. `03_token_counts.py`, lui,
   tourne hors ligne.
   - Le tokeniseur de Llama (accès contrôlé) se charge alors **depuis le cache épinglé**. Essai du 2026-11-15 dans le conteneur, sur
     le vrai dépôt de Llama, sans clé, cache rempli de fichiers de substitution à la révision `0e9e39f2…` : le chargement en ligne
     **échoue** sur `added_tokens.json` (401) tant que les absences de fichiers facultatifs ne sont pas inscrites dans le cache. Il
     **passe** une fois `added_tokens.json` et `chat_template.jinja` marqués absents. Hors ligne, il passe sans ces marques.
   - D'où, à `telecharger-tokeniseur` : un premier chargement **avec la clé, dans le processus du lanceur** (la clé n'est jamais
     transmise à un enfant), qui inscrit ces absences ; puis deux sondes **sans clé** (en ligne, hors ligne), qui doivent rendre le
     même nombre de jetons ; sinon arrêt avant les poids. `refs/main` du cache est fixé à la révision épinglée (Llama, Neuronpedia,
     et pour l'audit Qwen3-8B et `rs-lenses`). Les dépôts publics sont appelés avec `token=False` : la clé ne part que vers Llama.
2. **Audit « tout négatif »** (texte gelé, audit R4) : `score` est rejoué sur la sortie publiée de `measure` pour Qwen3-8B
   (`causal.pt`, `b6321004…`), avec `--lenses logit,J,hub`. Le résumé publié porte `logit`, `J` et `R:dclm` ; or `R:dclm` demande un
   dossier de Drowse qu'on ne peut pas reconstruire. **Lecture proposée** : le cas sain (écart de `r_med` > 0,05 = chaîne en défaut) est
   jugé sur `logit` et `J` seulement ; `hub` (lentille R publiée dans `rs-lenses`, `5eaa4d56…`) est rapporté face à `R:dclm`, sans
   jugement. **À trancher par la mère** (lecture du texte gelé), recommandation : cette lecture, confiance 0,6.
3. **Code voisin dans le dépôt réduit** sous `voisin/neuron-lens/` (pièce 5). Les correctifs s'appliquent depuis la racine
   (`git apply --directory=voisin/neuron-lens`, `--check` d'abord). Lancé du sous-dossier, `git apply` ignorait les chemins du correctif
   **en silence** : c'est l'essai sur la vraie copie qui l'a montré.
4. **Délais des processus enfants** (code 124 au dépassement = arrêt) : 0,5 h pour les essais, 1 h pour la fumée, 2 h pour le corpus,
   6 h pour la passe, 5 h pour `measure`, 2 h pour `score`. Ils sont larges ; la minuterie et la garde de dépense bornent l'argent.
5. **Audit « trop beau »** : `measure --seed 1`, `score --seed 1 --tag seed1`, grandeurs de la graine 1 (même garde de fidélité). Sont
   aussi rapportés : le témoin bien apparié (aucun pôle témoin de lui-même) et la norme non nulle du pilotage (n minimal par couche).

## B.3 consigné avant la location (devis v2, m5)
2026-11-15T08:47:16Z, conteneur : `PYTHONPATH=src python -m pytest -q -rs -p no:cacheprovider tests/test_neuron_lens_verdicts_b_alpha_v3.py`
→ **35 passed** (essais `1ee366fa…`, module `8f57088a…`). Le lanceur les rejoue sur la machine dans `b0` et dans `b3`, avant `measure`.

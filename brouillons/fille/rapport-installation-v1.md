# Rapport d'installation de la session fille — v1

Session fille de session-depot (`session_01XJ6MgmmBhNGj5VaXDwJTP4`). Aucune dépense, aucun appel de modèle, aucun relais démarré.
Relevés horaires (`date -u`) : début 2026-11-02 23:56:53 UTC ; avant rédaction 2026-11-03 00:07:41 UTC.
Partie de `main` à `38c6ebc12d9c4a48aab26c9bdfe8cc7c2bbc1ce3`.

## 1. Clés (présence par nom seulement)
| Nom | État |
|---|---|
| `KIMI_API_KEY` | présent |
| `OPENAI_API_KEY` | présent |
| `GEMINI_API_KEY_2` | présent |
| `RR_ANTHROPIC_API_KEY_LUC` | présent |
| `RR_ANTHROPIC_API_KEY_LUC_2` | **absent** |
| `RR_ANTHROPIC_API_KEY_LUC_3` | **absent** |
| `VAST_API_KEY` | présent |
| `HF_TOKEN` | présent |
| `CONTROLE_IA_GITHUB_TOKEN` | présent |
| `GH_TOKEN` | présent |

## 2. Branches récupérées (refspec explicite, `--filter=blob:none`, `gc.auto 0`, aucune fusion)
| Branche | Tête |
|---|---|
| `outils/commandes-a1-bis-v1` | `a1fc7bcafc73d69046d08edaafe790fb682e3cbb` |
| `outils/commandes-tour-ferme-v1` | `18fdeaae5fa2dad685500b41e3ca96ca85fb4ef3` |
| `outils/collisionneur-v9-v1` | `749fe8b991fe54bd9b27ca919599ebd24ddd2ab3` |
| `donnees/recuperation-collisionneur-v8-v1` | `60656845eaa14cdecbbe5c953cd580c38ead31bc` |
| `donnees/collisionneur-v9-brainstorm-v1` | `ac25c0556f57575acca9725db0698108440f3150` |

Aucune ref `donnees/bras-attaque*` ni `donnees/mode-tenu-a-l-ecart*` récupérée.

## 3. Environnement
- Python 3.13.18 ; `.venv` créé, `pip install -r requirements-cpu.txt` code 0 ; numpy 2.4.6.
- `bwrap` : bubblewrap **0.9.0** (paquet `0.9.0-1ubuntu0.3`, installé par apt).
- Dépôt public `lciric/ideation-organism` cloné en lecture dans `/home/user/ideation-organism` ; tête `66dbcf1960dff4370a44e5f90d5ecc216f5b60cb` (2026-11-03T00:20:16+01:00).

## 4. Empreintes (sha256 sur `git show branche:chemin`)
| Branche : fichier | Attendu | Résultat |
|---|---|---|
| `main` : `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v3.py` | `d54ed2bc…ca76239` | égal |
| `donnees/recuperation-collisionneur-v8-v1` : `donnees/mini-course-kimi-argon-v1/orchestrateur/nuit/commande_argon_v56_nuit_v2.py` | `221df610…622b851` | égal |
| idem : `…/nuit/commande_kimi_v2.py` | `644dbb39…9dcbe` | égal |
| idem : `…/nuit/registre_depense_cumulee_v1.py` | `8ba92066…578ff` | égal |
| idem : `donnees/espece-seule-v1/collisionneur_v7.py` | `c9725f02…98dc` | égal |
| `outils/commandes-a1-bis-v1` : `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/commande_claude_a1bis_v1.py` | `7da79a5c…2c5` | égal |
| idem : `…/commande_astra_a1bis_v1.py` | `6e9e48e0…1815` | égal |
| idem : `…/commande_pole_v56_commun_v1.py` | `1f56e466…eaed` | égal |
| `outils/collisionneur-v9-v1` : `docs/notes/ideation-organisme-v1/course-2/collisionneur-v9/collisionneur_v9.py` | `27e9ce40…bd1d6` | égal |
| `outils/commandes-tour-ferme-v1` : `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_kimi_v3.py` | `bb303f50…0b60b` | égal |
| idem : `…/commande_argon_v56_nuit_v3.py` | `95fa4064…1af73` | égal |

Comparaisons faites sur les empreintes complètes données par l'ordre ; onze sur onze égales. Rien préparé avec la v3 (une v4 est annoncée).

## 5. Ports locaux
8802, 8804, 8805, 8806, 8807 : **libres** (liaison d'essai sur 127.0.0.1 réussie ; aucune écoute dans `/proc/net/tcp`). Aucun relais démarré.

## 6. Écarts et réserves
- `RR_ANTHROPIC_API_KEY_LUC_2` et `RR_ANTHROPIC_API_KEY_LUC_3` absentes de l'environnement.
- `ss` n'est pas installé ; vérification des ports faite par liaison d'essai et lecture de `/proc/net/tcp`.
- Les fichiers de la commande A1-bis ne sont pas à la racine de la branche : ils sont sous `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/`.
- Routine de reprise complète (R14) non exécutée : hors du périmètre de cette première tâche.

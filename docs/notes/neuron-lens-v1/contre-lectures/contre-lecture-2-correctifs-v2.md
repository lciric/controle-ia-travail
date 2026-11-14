# Contre-lecture 2 des correctifs (passe d'activations v2 ; lentilles de Neuronpedia v1) — rapport recopié tel quel

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 vers 10:07 UTC ; il n'a écrit aucun des correctifs. Pièces
relues : `correctif-06_activations-v2.md` (`1c3b8c9facf24e8285e9be99607d6be2bb5860d1476a9e08992c56f8793a9ae9`),
`06_activations-llama-v2.diff` (`76b639a0d1223a1fe97397a8ad1cfd1ca0fa75605e21ee98ec4246e4777943ed`),
`essai-06_activations-llama-v2.py` (`6d6c4c08473f4a8b4e8ad1c80f15f44aed17fb885bba0da9406dd837d4f8feb7`),
`correctif-lenses-neuronpedia-llama-v1.md` (`345592f5…`), `lenses-neuronpedia-llama-v1.diff`
(`b700c3ebb31dd045aa550b1a03edee9f7069d9eb8dac32f383990e5472dbaf32`). Rapport rendu vers 10:12 UTC. Recopié sans modification de
fond ; les blocs de code proposés sont résumés quand ils ont été repris tels quels dans les versions suivantes (signalé).

---

## 1) Empreintes vérifiées
Rien n'a été exécuté (ni code voisin, ni essai, ni import). Seuls contrôles lancés : `sha256sum`, `git apply --check`, `ast.parse`,
`diff`, et `patch` sur une copie des trois fichiers dans mon bac à sable.
- `correctif-06_activations-v2.md` : `1c3b8c9f…9ae9`, conforme. `06_activations-llama-v2.diff` : `76b639a0…43ed`, conforme.
  `essai-06_activations-llama-v2.py` : `6d6c4c08…feb7`, conforme. `contre-lecture-1-correctif-06-v1.md` : `8ed58170…25c7`.
  `correctif-lenses-neuronpedia-llama-v1.md` : `345592f5…b3ba` ; `lenses-neuronpedia-llama-v1.diff` : `b700c3eb…af32`.
- Clone voisin : HEAD `849bfe16…`, arbre propre ; `scripts/06_activations.py` `151d1196…8035`, `neuron_lens/arch.py` `0f1e2262…ce12`.
- Fichiers corrigés de référence : `06_activations.py` `b97bf54b…b902`, `arch.py` `877fa6b0…f964`, `lenses.py` `20e48fb4…b124`,
  conformes aux notes et aux trois constantes en dur de l'essai. Les deux différences appliquées sur une copie des originaux redonnent
  exactement ces empreintes. `git apply --check` des deux sur le clone : réussi. `ast.parse` des trois fichiers corrigés et de l'essai : réussi.
- `transformers` lu : 5.18.0.
- Arbre archivé de Neuronpedia : les trois chemins de Llama existent ; J `d5300a15…c68b` (1 040 197 778 octets) ; J++ `8bd04f48…056f7c`
  (1 040 198 856) ; R `a63a1588…d31c` (1 040 198 745).
- **Écart R6** : aucun compagnon `.sha256` dans `correctifs/`, alors que les deux notes écrivent « compagnon `.sha256` » au présent.

## 2) Verdicts
- **A (passe d'activations, v2) : correct après corrections mineures.** La différence est juste et sans effet sur Qwen3 et Gemma 4 ;
  l'essai est cohérent à la lecture ; restent des imprécisions de la note et un complément d'essai.
- **B (lentilles de Neuronpedia) : correct après corrections mineures**, dont deux à faire avant B0 (remarques 8 et 9) : sans elles, un
  format inattendu peut faire retomber sans bruit une lentille sur la lentille logit.

## 3) Remarques
### Correctif A
**1. Constat — le tableau du § 6 est exact pour les onze remarques de la contre-lecture 1** (10 : annoncé « au scellement », pas encore fait).

**2. Constat — les blocs nouveaux sont corrects.** `chat_open` : dans 5.18, `apply_chat_template` accepte `return_dict` (défaut `True`) ;
avec `tokenize=True, return_dict=False`, il rend une liste d'entiers ; le gabarit de Llama 3.1 pose lui-même le jeton de début, donc l'indice
1 est `<|start_header_id|>`. `hooks`, `collect` : `meta` inchangé pour Qwen3 et Gemma 4. `head_tables` : `arch.stem` donne bien `qwen3-8b` et
`gemma-4-12b` ; branche `else` identique à l'original ; message imprimé. **Aucun lecteur de `out_R_z` dans les fichiers nommés** :
`causal_lens.py measure` lit `neurons/acts/L*.parquet` et `documents()` ; `score` ne lit pas `heads/acts.parquet`. Non examinés :
`08_reads.py`, `10_labels.py`, `12_release.py`, `neuron_lens/neurons.py`, `weights.py`, `corpus.py`.

**3. Mineure (note § 1.3) — motif surévalué.** `catalog.flat_tokens` lit le fichier d'état `data/acts/<modèle>.pt` quand il existe et ne lit
`docs.parquet` que s'il manque ; les tables des neurones sont écrites avant `head_tables`. Correction proposée : « échec en fin de script
(code de sortie non nul, ni `heads/acts.parquet` ni `docs.parquet`) ; `causal_lens.py` ne lit `docs.parquet` que si le fichier d'état n'est
pas sur la machine ».

**4. Mineure (note § 1.2) — numéro de ligne.** L'appel de `chat_open` est à la ligne 396 de l'original ; 401 est sa ligne dans le corrigé.

**5. Mineure (note § 1.3 et bloc 3) — liste en dur non vérifiable ici** (arbre de `stdlogits/rs-lenses` hors des pièces) ; sans conséquence
pour Qwen3, Gemma 4 12B et Llama.

**6. Constat — essai v2 : aucune erreur d'exécution trouvée à la lecture (5.18).** Comptes de crochets justes ; formes correctes ; `torch.equal`
adéquat ; `test_chat_open_rend_un_entier` distingue bien l'original (qui lèverait `KeyError`) et le corrigé ; `test_original_echoue_sur_llama` correct.

**7. Mineure (essai) — deux limites.** (a) ajouter à B0 un test avec le vrai tokeniseur de Llama (`arch.bos(tok) == [tok.bos_token_id]` et
`chat_open(...) == tok.convert_tokens_to_ids("<|start_header_id|>")`) ; (b) l'assertion de la ligne 107 recopie la condition de `collect` sans
l'appeler : la retirer ou la commenter.

### Correctif B
**8. À corriger avant B0 — la lentille `J` de Llama n'est pas contrôlée** (branche `spec == "J"` garde le chargement brut) ; dans `score`,
`lenses[s].get(layer)` rend `None` pour une clé absente, soit la lentille logit, sans erreur. Correction : passer `J` par `neuronpedia_lens`
(ou garder l'ancien chargement pour Qwen3 seul).

**9. À corriger avant B0 — couverture des couches non contrôlée.** Une couche manquante ou un décalage retombe sans bruit sur la lentille logit
(R5). Les tailles disent 31 matrices 4096 × 4096 en demi-précision par fichier : la couche 31 est absente par construction ; à L31, `J`, `npJpp`
et `npR` sont exactement la lentille logit et entrent dans le seuil commun (`thr`) : à écrire dans le plan de lecture. Correction proposée
(reprise telle quelle dans la v2) : contrôle `sorted(J) == list(range(len(J)))`, formes égales, `sorted(map(str, payload))`, impression des
couches et des autres clés ; à B0, arrêt si `len(J) != 31`.

**10. À vérifier à B0 — autres clés et sens des fichiers J++ et R** (quelques centaines d'octets de plus que J : métadonnées probables ; une
convention différente sous « J » serait une lecture fausse sans erreur). Correction : imprimer les autres clés ; lire `config.yaml` et
`CREDIT.md` avant toute lecture ; l'écrire dans la liste d'arrêt.

**11. À corriger — empreinte et révision.** `hf_hub_download` sans `revision` ni comparaison d'empreinte ; le contrôle doit porter sur le fichier
du cache réellement lu, avant `score`. Correction proposée (reprise) : `NEURONPEDIA_SHA256` et vérification dans `lenses.py` ; `revision` si connue.

**12. Mineure — identifiant exact du modèle.** Avec un autre identifiant, `npJpp` et `npR` tombent dans la fusion Drowse avec une erreur
trompeuse. Correction (reprise) : `KeyError` explicite, et le dire dans la note.

**13. Constat — noms et place de la branche** : sans collision ; il faut bien passer `--lenses logit,J,npJpp,npR`.

**14. Mineure — docstring de `load_lens` non mise à jour** ; la note de B n'a ni essai écrit ni mention de « L31 = logit ».

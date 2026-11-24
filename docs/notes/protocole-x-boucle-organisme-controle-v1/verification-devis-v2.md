# Attestation de vérification de concordance du devis du collisionneur (version 2)

Vérification exécutée **uniquement après** l'enregistrement complet du test de neutralité et de devinette à l'aveugle (`test-neutralite-devinette-boucle-organisme-controle-v2.md`), sous les accords d'exécution `GO-2026-11-23-33` et `GO-2026-11-23-34` (`GO` désignant un feu vert d'exécution), sans modification du dépôt de gestion de versions Git (`PYTHONDONTWRITEBYTECODE=1`).

## 1. Concordance exacte des tailles et de la garde de motifs

Toutes les mesures annoncées en section 0 de `devis-collisionneur-boucle-organisme-controle-v2.md` concordent à l'unité près avec les fichiers effectifs :

| Pièce | Octets sur disque (devis v2 / mesuré) | Caractères normalisés `lire_entree` (devis v2 / mesuré) | Mots `split()` (devis v2 / mesuré) | `motifs_trouves` |
|---|---:|---:|---:|---|
| `faits-neutres-boucle-organisme-controle-v2.md` | `4 946` / `4 946` | `4 780` / `4 780` | `717` / `717` | `[]` |
| `question-neutre-collisionneur-boucle-organisme-controle-v2.md` | `2 853` / `2 853` | `2 758` / `2 758` | `410` / `410` | `[]` |
| `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` | `2 703` / `2 703` | `2 598` / `2 598` | `394` / `394` | `[]` |
| `sous-question-organisme-boucle-controle-v2.md` | (mentionné sain) / `786` | — / `760` | — / `100` | `[]` |

## 2. Concordance arithmétique et prise en compte intégrale de `contre-lecture-devis-collisionneur-boucle-organisme-controle-v1.md`

1. **Devis natif de `collisionneur_v9_v8d.py` (étage trois, `opus` + `carbon` + `neon`)** : le recalcul direct rend `15,8319` dollars américains pour le bras principal (`15,83`), `15,8297` dollars américains pour le bras témoin (`15,83`, noté `15,8298` au quatrième chiffre décimal dans le devis par arrondi intermédiaire d'un dix-millième sans aucun effet au centime), et une somme exacte de **`31,6616` dollars américains** (`31,66`), identique au chiffre de la section 2.3 du devis version 2.
2. **Cohérence de la baisse d'entrée entre version 1 et version 2** : le passage des entrées de `4 979 + 2 887 = 7 866` caractères (version 1) à `4 780 + 2 758 = 7 538` caractères (version 2, soit `-328` caractères sur le bras principal et `-199` caractères sur le bras témoin) se répercute exactement sur les jetons d'entrée du tableau 2.1 (`4 431` au lieu de `4 573` pour Opus au tour 1, `2 831` au lieu de `2 922` pour Carbon, `2 877` au lieu de `2 968` pour Neon) et diminue les sous-totaux de deux à trois millièmes de dollar (`4,3113` contre `4,3133` en attendu Option A, `11,9223` contre `11,9250` au pire sans relance), laissant intacts les plafonds entiers recommandés (`16` dollars américains par bras en Option A, soit `32` au total ; `18` dollars américains par bras en Option B, soit `36` au total).
3. **Levée des quatre observations de la section 4 de la contre-lecture version 1** :
   - **Point 1 (cellule de pointe)** : corrigé en `E3-T3-reponse-C` (Neon) aux lignes 75 et 86 (`10,5703` dollars en Option A, `12,7279` dollars en Option B).
   - **Point 2 (distinction octets sur disque contre caractères normalisés)** : corrigé explicitement en section 0 (lignes 10 et 11).
   - **Point 3 (voie abonnement hors moteur `collisionneur_v9_v8d.py`)** : traité en présentant l'Option A (voie abonnement via lanceur adapté) et l'Option B (clé d'interface de programmation Anthropic immédiatement exécutable sous `collisionneur_v9_v8d.py`) à parité complète dans tous les tableaux, avec interdiction explicite de panacher les deux bras (section 3, point 1).
   - **Point 4 (condition de neutralité des textes en version 2)** : inscrite à la ligne 109 du devis version 2 et désormais satisfaite (`0,14` pour les faits version 2, `0,22` pour la question principale version 2, `0,09` pour la question témoin version 1, `0,19` pour la sous-question version 2, tous `< 0,50`).

## 3. Conclusion

**Attestation conforme sans réserve** : `devis-collisionneur-boucle-organisme-controle-v2.md` concorde exactement avec les tailles des fichiers en version 2, avec le moteur `collisionneur_v9_v8d.py` et avec l'ensemble des exigences de `contre-lecture-devis-collisionneur-boucle-organisme-controle-v1.md`.

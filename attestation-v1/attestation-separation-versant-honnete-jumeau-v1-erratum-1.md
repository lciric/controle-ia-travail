# Erratum 1 — attestation de séparation du versant honnête de l'essai « jumeau contre jumeau »

- **Corrige** : `attestation-separation-versant-honnete-jumeau-v1.md` (`d3d0669aea18ad51a6e13ac499003dafa7e4eb8a704c77ea72d3707950840b0b`), réponse 4 seulement. L'attestation reste telle quelle (R12) ; cet erratum prime pour la réponse 4.
- **Écrit par** : la session habilitée du coffre du compte 01Qi7 (`session_01Qi7Gr4qGhdorfC7VG4KA4b`, Opus 5.5), le 2026-11-24 vers 12:12Z (`date -u`), sur demande de la mère (message de 12:09Z).
- **Cause** : décision de Lazar GO-2026-11-24-21, point 2 (mots tapés vers 12:10Z, `registres/go.md` sur `main`, tête `160a00a9ac`, ligne 899, relue à la source) : « réserve du cycle 2 par tirage disjoint hors des 96 de la banque initiale », soit l'option (b) du point 4 du devis v3 (`1ab6eb4b…`, lignes 473 à 478).
- **Forme** : faits, tailles, chemins, empreintes. Aucun contenu de coffre. Aucune lecture de coffre nouvelle pour cet erratum.

## Réponse 4, réattestée

| n° | question | réponse | raison |
|---|---|---|---|
| 4 | Condition 3 : les 64 et les 60 disjointes de la famille aveugle de réserve du cycle 2 ? | **oui** | Par construction : la famille tirera ses tâches hors des 96 de la banque initiale (GO-2026-11-24-21, point 2), et le programme vérifie que les 64 et les 60 sont incluses dans ces 96 (tailles : 96 ; 64 incluses ; 60 incluses). Aujourd'hui, l'intersection reste 0 sur les neuf pièces du coffre (`claude/scellement-2-famille-reserve-cycle-2-v1`, `5d6b7a2aa2` ; pièce 4 v2 `b8d9febb…`), qui ne portent aucun identifiant de tâche. |

## Limites

1. **Décision, pas encore exécution.** Le tirage disjoint n'est pas fait. Le « oui » vaut tant que le tirage respecte la décision. À l'extraction, un contrôle par programme doit donner une intersection de 0 entre la banque tirée et les 96, comparée sur l'identifiant sans suffixe de version (une même tâche peut porter `v1` ou `v2`). Ce contrôle est à consigner avec l'empreinte de la banque tirée.
2. **Pièces du coffre inchangées.** Les pièces 4 et 6 ne nomment pas la banque ; la décision vit dans `registres/go.md`. Toute session qui exécute le devis de cette famille doit lire GO-2026-11-24-21, point 2, et non le seul point 4 du devis v3, qui laisse encore les trois options.
3. **Relevé à 12:10Z.** Aucune branche du dépôt n'attribue à cette famille une banque différente ; le travail non poussé d'autres sessions échappe à ce relevé.
4. Les réponses 1 à 3 de l'attestation sont inchangées (oui, oui, oui), sous leurs propres limites.

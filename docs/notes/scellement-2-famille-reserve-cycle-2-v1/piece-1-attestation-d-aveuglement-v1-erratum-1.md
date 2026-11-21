# Pièce 1 — Attestation d'aveuglement : erratum 1 (compléments après la contre-lecture)

- Classe A. En clair. Écrit le 21 novembre 2026 vers 17:35 UTC par le concepteur de la famille de réserve du cycle 2.
- Complète `piece-1-attestation-d-aveuglement-v1.md` (`ed070552529ad899…`), qui reste telle quelle (R12). Répond au
  point 9 de la contre-lecture (pièce 7, `f830f70cb68b3ca0…`). Lu avec l'attestation ; en cas de divergence, il prime.

## Compléments aux réserves

9. **Noms de dossiers de moniteurs.** La section 2 de l'attestation montre que je connais, par leur nom seul, des
   dossiers et des fichiers de moniteurs du dépôt (liste de `src/controle_ia/`). Je n'en ai ouvert aucun. Réserve de
   même nature que la réserve 2.
10. **Cibles cachées d'une tâche.** J'ai lu les cibles cachées de la première tâche du fichier
    `donnees/t05-pilote-v1/taches-pilote-60-v1.json` (`287e83485cba5500…`), pour comprendre leur forme. Si cette tâche
    entre dans la banque de la famille, c'est à dire au préenregistrement. Effet nul sur l'aveuglement aux moniteurs.
11. **Heure.** L'attestation dit « vers 17:15 UTC » ; son commit est horodaté 17:12:11 UTC. L'heure du commit fait foi.

## Lectures faites après la signature, pour la correction

12. **La contre-lecture** (pièce 7), entière, sur la branche `claude/scellement-2-contre-lecture-cycle-2-v1` (commit
    `af80fd39`) ; seul ce fichier a été extrait de cette branche.
13. **Quatre lignes de `registres/go.md` sur `main`** (GO-2026-11-21-64 à -67, l. 663-666, leurs 900 premiers
    signes), pour citer GO-2026-11-21-66. **Réserve** : la ligne GO-2026-11-21-65 nomme un « module des autres
    moniteurs », une « lecture par la lentille publique » et deux modèles confrontés aux familles (Mistral Large 4,
    Gemini 4 Neon), par leur nom seul, sans conception, seuil ni résultat. Les pièces 2 à 5 étaient déjà écrites et
    scellées en v1 ; aucune correction de la v2 ne s'appuie sur ces noms.
14. **`pilote_a.py`, lignes 8-9**, relues dans ma sortie d'origine (aucune lecture neuve du fichier), pour la
    construction des graines de la pièce 3, v2.

Je n'ai toujours vu ni la famille du cycle 1, ni les candidats du 28 octobre, ni aucun moniteur. Aucun refus de
classifieur.

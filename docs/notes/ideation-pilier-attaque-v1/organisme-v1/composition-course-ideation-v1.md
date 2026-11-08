# Composition de la course d'idéation — pilier attaque, v1

Date : 2026-11-08.
Question scellée : `question-remue-meninges-pilier-attaque-v1.md`
SHA256 : `29870ac9a8091c165375c51f4b74d6e0f38ae60d2e8754872ff70fb3077820c4`

## Principes

1. **Garde de refus (R-514)** : avant la course, `garde_refus_question_v1.sonder_modeles()` sonde chaque modèle sur un extrait de la question. Un modèle qui refuse est retiré de **tous** les rôles (proposeur ET juge), pas seulement des proposeurs.
2. **N-053** : Argon juge uniquement en bras rapporté différé (juge d'une autre lignée), jamais en juge interne. Ses notes entrent dans la médiane à trois juges, après lecture humaine attestée.
3. **CL31-05** : la synthèse d'antériorité du collisionneur est servie comme pièce aux juges (mémoire anti-répétition).
4. Aucun outil pour les proposeurs ni les juges (CL31-08, `tools=[]`).
5. Sessions neuves pour les juges, grille fixée d'avance.

## Déroulement en deux temps

La course de base (lanceur v2, via la chaîne v8→v7→v6→v5→v4→v2) se joue en deux invocations distinctes :

**(a) Course** : proposeurs + juges Claude. Écrit les fiches, les notes, le classement à deux juges (ou au nombre de juges Claude), les consignes en attente pour le juge externe.

**(b) Bras rapporté différé** : invocation séparée (`--bras-rapporte-differe`) après la course, après attestation de lecture humaine. Le juge externe (Argon) lit les fiches validées et note, produisant le classement final à trois juges (médiane).

## Composition la plus simple conforme

### Si Fable 5.1 passe la sonde (3 proposeurs, 3 juges → médiane)

**Course (a) :**

| Rôle | Étiquette | Modèle | Type |
|---|---|---|---|
| Proposeur | opus | claude-opus-5-5 | Claude (SDK) |
| Proposeur | fable | claude-fable-5-1 | Claude (SDK) |
| Proposeur-externe | argon | gemini-4-argon | Commande externe |
| Juge | opus-juge | claude-opus-5-5 | Claude (SDK) |
| Juge | fable-juge | claude-fable-5-1 | Claude (SDK) |

**Bras rapporté différé (b) :**

| Rôle | Étiquette | Modèle | Type |
|---|---|---|---|
| Juge-externe (bras différé) | argon-juge | gemini-4-argon | Commande externe |

Agrégation finale : médiane à trois juges (nommée). Porte d'éligibilité : 2/3 sur chaque critère.

### Si Fable 5.1 refuse la sonde (2 proposeurs, 2 juges → moyenne)

**Course (a) :**

| Rôle | Étiquette | Modèle | Type |
|---|---|---|---|
| Proposeur | opus | claude-opus-5-5 | Claude (SDK) |
| Proposeur-externe | argon | gemini-4-argon | Commande externe |
| Juge | opus-juge | claude-opus-5-5 | Claude (SDK) |

**Bras rapporté différé (b) :**

| Rôle | Étiquette | Modèle | Type |
|---|---|---|---|
| Juge-externe (bras différé) | argon-juge | gemini-4-argon | Commande externe |

Agrégation : moyenne à deux juges. Bras rapporté différé (N-053). Classement « sans juge externe » si le bras échoue.

## Pièces servies

| Pièce | Servie à | Chemin |
|---|---|---|
| Question scellée | Proposeurs | `question-remue-meninges-pilier-attaque-v1.md` |
| Synthèse d'antériorité du collisionneur | Proposeurs ET juges (CL31-05) | `synthese-anteriorite-pilier-attaque-v1.md` |

## Paramètres de la course (a)

- `--nombre 8` (8 fiches par proposeur par passe, défaut)
- `--seconde-passe` (deux passes, mémoire entre les passes)
- `--max-tours 2` (défaut)
- `--moteur claude-sdk` (course réelle ; `simule` pour le pré-vol)
- Budget : voir le devis (`devis-course-organismes-pilier-attaque-v1.md`)

## Paramètres du bras (b)

- `--bras-rapporte-differe`
- `--juge-externe argon-juge=gemini-4-argon`
- `--attestation-lecture-humaine ATTESTATION.json`
- `--commande-externe CMD` (la commande externe Argon)
- Sortie : le même dossier que la course (a)

## Témoins

Les témoins plantés (CL31-03) doivent être écrits par un tiers (Lazar ou un agent neuf), pas par la session qui prépare la course. Emplacement prévu : `organisme-v1/temoins-pilier-attaque-v1.json`. Format attendu par le noyau : `{"temoins": [{"fiche": {...gabarit...}, "attendu": "ineligible|eligible", "note_max": {critere: n}}]}`.

## Garde lexicale

La garde lexicale du niveau méthode (CL31-06, `MOTIFS_NIVEAU_METHODE`) est appliquée aux réponses brutes et aux fiches. Les fiches signalées sont mises en quarantaine (taux rapporté, L1).

## Coffre et portier

Les champs fermés de sortie et le coffre (portier, scellement des fiches qui glissent vers le concret, R-607) sont définis dans la question scellée.

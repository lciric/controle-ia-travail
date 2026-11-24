# Garde de motifs sur la question neutre groupée du collisionneur, dossier des questions du directeur du 24 novembre (v1)

- **Nature** : pièce de travail (classe C). Aucun appel à un modèle externe, aucune dépense, aucune écriture hors de ce dossier.
- **Heure** : `2026-11-24T17:12:55Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`, branche `idees/questions-directeur-2026-11-24-v1`. Non commité.
- **Script lancé** : `garde_motifs_questions_directeur_v1.py` (`e13b9d4d5409bfa0a8b0fe72320f3794913eb0d4e8086168b89a8783f2e16a54`), par `PYTHONDONTWRITEBYTECODE=1 python3 -I garde_motifs_questions_directeur_v1.py`, code de sortie 0. Sortie complète : `garde-motifs-questions-directeur-v1-sortie.txt` (`0e1ce4c877496263ff424a05574978410b76747defa060e689424f46b89a52b2`).
- **Moteur importé** : `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` (`b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac`, conforme à son compagnon), fonctions `motifs_trouves` et `lire_entree`, sans fichier de code compilé (`sys.dont_write_bytecode`). Les neuf invitations du troisième étage (Opus, Carbon, Neon ; conception, critique croisée, réponse) de chaque bras sont reconstruites en mémoire par `construire_prompt` du moteur, sa lecture scellée remplacée par une lecture en mémoire ; les pièces des tours deux et trois, qui n'existent pas encore, y entrent sous le bloc « pièce absente » du moteur. La garde du moteur rejouera, à l'envoi, les invitations réelles avec les pièces des modèles.

## 1. Pièces isolées

| Pièce | Octets | Caractères (`lire_entree`) | Mots | Empreinte | `motifs_trouves` sur les octets décodés | sur `lire_entree` |
|---|---:|---:|---:|---|---|---|
| `faits-neutres-questions-directeur-v1.md` | 3 333 | 3 235 | 563 | `7926025cc499089b025ce302c2be557caeea1987a106953401295ab03de0c7c5` | `[]` | `[]` |
| `question-neutre-groupee-questions-directeur-v1.md` | 9 253 | 8 922 | 1 479 | `03065164c1bf19d1194fa71eb62f935d14edc947d0a92078349fe0539d9bdee0` | `[]` | `[]` |
| `question-temoin-neutre-questions-directeur-v1.md` | 2 702 | 2 608 | 430 | `002e0df810e9c30cecee1e573f9ed4483df0af05fb8eb734386fe7de15b15ead` | `[]` | `[]` |

Mots comptés par `split()` sur le texte normalisé, titres et puces compris.

## 2. Invitations assemblées du troisième étage

| Bras | Cellules | Caractères par invitation | `motifs_trouves` |
|---|---|---:|---|
| principal | III.1 conception A, B, C | 14 874 | `[]` sur les trois |
| principal | III.2 critique croisée A, B, C | 15 145 | `[]` sur les trois |
| principal | III.3 réponse A, B, C | 15 146 | `[]` sur les trois |
| témoin | III.1 conception A, B, C | 8 560 | `[]` sur les trois |
| témoin | III.2 critique croisée A, B, C | 8 831 | `[]` sur les trois |
| témoin | III.3 réponse A, B, C | 8 832 | `[]` sur les trois |

**Résultat : vide partout** (trois pièces isolées, dix-huit invitations).

## 3. Témoin positif de la garde (règle R5)

Texte synthétique « Voir docs/notes/exemple et l'accord GO-2026-01-01-01, ligne R-1234. » : `[('chemin interne', 5), ("identifiant d'accord", 36), ('identifiant de registre', 60)]`, trois catégories attendues sur trois. La garde est vivante.

## 4. Provenance des textes (pour le lecteur du test de devinette)

- **Parties 1 à 4 de la question, cadre, partie 6, règles, question témoin et faits** : écrits par Claude Opus 5.5 dans la présente tâche, et **non par Fable 5.2** comme le prévoyait le dosage du mandat du dossier (« Question neutre : Fable 5.2 effort élevé ») ; écart à porter à la mère.
- **Partie 5 de la question** : texte neutre de la question 11, écrit par **Claude Opus 5.5, non par Fable** (`demandes-reformulees-quatre-points-q8-q11-v1.md`, `632c7af28673dcd51ff118d989ad1d2eb14e7ed31fa867ef8a800d3b1322c636`, section « Question 11 », « Texte neutre »). Repris mot pour mot, avec quatre retouches seulement : le titre devient celui de la partie 5 ; son paragraphe de règles est fondu dans les règles communes ; sa phrase « Ne fais pas une réponse plus longue, fais-la plus profonde » passe dans le cadre ; une ligne « Ce qui réfuterait la piste » est ajoutée, comme aux autres parties.
- **Règles communes, une harmonisation** : le gabarit de la boucle demandait l'identifiant arXiv « si tu le connais » ; le préambule du moteur interdit tout identifiant arXiv donné de mémoire (règle d'intégrité 3). La question suit le préambule (« sans identifiant donné de mémoire »).
- **Faits** : une seule source publique, relue en ligne le 24 novembre 2026 : arXiv 2405.17044, version 4, PDF téléchargé d'arXiv, empreinte `fcb49a059e17a25c351153a8022717aa594ddc279f6e276e204f1fbe9ce32af4`, identique à celle de la copie déjà versée `docs/sources/pdf/2405.17044v4.pdf.sha256`. Pages du PDF citées : 3 (légende de la figure 2), 4, 7 et 8. Une définition de l'énergie d'activation tirée du recueil terminologique de l'Union internationale de chimie pure et appliquée a été écartée : page inaccessible d'ici (barrière anti-robots), donc non vérifiée.
- **Ce qui ne souffle pas les conclusions du dossier** : les verdicts des réponses versées (deux oracles mécaniques et deux à lecteurs ; information mutuelle ponctuelle ; barrière non identifiable sans température et quatre prédictions de forme ; hyperarcs « prémisses vers cible » pondérés) ne figurent ni dans les faits ni dans la question ; aucune liste de travaux antérieurs n'est donnée. Le jugement de neutralité revient au test de devinette, fait ensuite par un agent neuf.

# Vérification de cloisonnement des demandes v8 du bras A (courte) — v1

- **Pièces vérifiées.**
  - Pièce du développeur : `docs/notes/relance-organismes-discrets-v1/demandes-au-developpeur-habilite-bras-a-v8.md`, `ba81227fcea1b6419fad012f83711e61a54c7c01dce6a34d3319266d4aaaf579`.
  - Pièce du lecteur : `…/demandes-au-lecteur-habilite-et-a-lazar-bras-a-v8.md`, `83c0822bd45740b7628bd9265aad1dd23806454644c38e129721c976f8e64f12`.
  - Les deux compagnons sont conformes.
  - Chaque pièce est comparée à sa v7 (`e55a7088…` pour le développeur, `1700ca19…` pour le lecteur).
- **Retouches de référence** : `verification-cloisonnement-demandes-v7-bras-a-v1.md`, `57f7276d7e2b53c697e5a83034a7fc087976bff44c3dfe0b0bc0b1c9f8655f4d`, retouches 1 à 6.
- **Relecteur** : le même agent Claude Opus 5.5, qui n'a écrit aucune pièce. Classe C. Mêmes interdits.
- **Diffusion** : cette pièce ne va pas au développeur.

## Verdict : peut sortir

Les six retouches de la v7 sont tenues. Le texte neuf (demandes 13, 24 (c) et 33) n'ouvre aucun risque de cloisonnement. Une remarque non bloquante figure au point 3.

## 1. Différence v7 → v8, par programme (`diff`)

**Pièce du développeur : six blocs.**
- le titre ;
- la demande 1, avec une phrase ajoutée ;
- la raison de la demande 6 ;
- la raison de la demande 7 ;
- la demande 13 ;
- « Ce qui presse », avec une ligne « Bloquante : 13 ».

Rien d'autre ne change.

**Contrôle de la pièce du développeur.**
- Aucune chaîne hexadécimale de 8 signes ou plus.
- Les autres `.md` du dossier de la relance et les brouillons 30 et suivants du texte ont été cherchés par leur nom et par les 8 premiers signes de leur empreinte : aucune occurrence.
- Les seuls jetons de chemin sont les motifs d'exclusion et `rangs-par-unite-moniteurs-bras-a.jsonl`.
- Les mots « anomalie », « défaut de la course », « indécis », « course saine » et « commandée » n'apparaissent pas.

**Pièce du lecteur.** Changent :
- le titre et l'en-tête : la v7 entre dans les versions remplacées, le texte visé devient le brouillon 33, et une phrase de silence est ajoutée ;
- quatre lignes de table ;
- les demandes 24, 25, 27 et 28 ;
- la demande 33, neuve ;
- « Ce qui presse » ;
- le « pour mémoire ».

## 2. Les retouches de la v7

| n° | retouche | tenue ? | où |
|---|---|---|---|
| 1 | Pas de suite des demandes 6 et 7 dans la ligne de GO du mot de Lazar avant la dernière livraison ; renvoi par chemin et empreinte | **oui** : consigne écrite ; il est demandé de dire si une ligne déjà inscrite recopie cette suite | lecteur, demande 27 |
| 2 | Silence jusqu'à la dernière livraison ; pour la demande 6, la commande seule ; confirmation sur le code ; renvoi depuis l'en-tête | **oui, pour les quatre** : « ni de vive voix, ni par une pièce, ni par le registre » ; « seule la commande lui est transmise, sans sa raison » ; la demande 24 (c) ; la phrase en gras dans l'en-tête | lecteur, en-tête et « pour mémoire » |
| 3 | Demande 6 du développeur, note neutre | **oui**, à la lettre | développeur, demande 6 |
| 4 | Demande 7 du développeur, raison neutre | **oui**, à la lettre | développeur, demande 7 |
| 5 | Demande 1 : aucun calcul de moniteur ne change, le lecteur l'attestera | **oui**, à la lettre | développeur, demande 1 |
| 6 | Demande 25 du lecteur, raison neutre (facultatif) | **oui** : « Un avis versé au dossier du schéma de permutation. Aucune règle du texte n'en dépend. » | lecteur, demande 25 |

## 3. Le texte neuf

**Demande 13 du développeur (`piece_source`, bloquante).**
- *Côté développeur : aucun biais.* Il fait porter à la sortie l'empreinte entière du module. C'est une donnée de provenance, sans lien avec ce que lisent les moniteurs.
- *Côté relance : aucun interne n'entre.* La réponse est un nom de champ. L'empreinte du module (un condensé à sens unique) entre dans chaque livraison et ne dit rien du code. Un chemin et une empreinte de pièce habilitée sont déjà permis.
- *Écart à la v7 du module.* Le changement touche la lecture commune seulement. Il est couvert par l'attestation de la demande 24 (a), qui porte sur la version qui fera foi.
- « Bloquante » ne crée aucun levier sur le verdict. Au pire, la session principale peut retarder le scellement, ce qui reste visible.

**Demande 24 (c) du lecteur (confirmer sur le code les réponses 6 et 7).**
- *Côté relance : aucun interne n'entre.* La réponse est « confirmée » ou « non confirmée », « sans rien dire d'un moniteur ».
- *Remarque non bloquante.* Le lecteur habilité lit la même pièce que la session principale, donc le « pour mémoire », donc la suite des deux réponses qu'il confirme. Il connaît ce qui en dépend : correction qui rend « repère » possible, anomalie qui arrête la lecture. C'est une pression faible sur sa confirmation.
- Elle est inévitable tant que lecteur et session principale partagent la pièce. Si l'on veut l'ôter, il faudrait :
  - marquer le « pour mémoire » « pour la session principale ; le lecteur habilité n'en a pas besoin pour la demande 24 (c) » ;
  - faire faire la confirmation par le lecteur habilité avant qu'il lise cette section.
- Ce n'est pas exigé.

**Demande 33 du lecteur (clé de provenance).**
- La réponse est un nom de champ, puis « confirmé » ou « non confirmé ». Elle porte sur la provenance, pas sur un moniteur.
- Aucun biais, aucune fuite.

**Demande 28 (constat de provenance).**
- C'est de la procédure du registre, sans contenu de moniteur. **Admis.**

## Retouches, liste courte

Aucune exigée. Facultatif : réserver le « pour mémoire » à la session principale, et faire faire la confirmation 24 (c) par le lecteur habilité avant qu'il lise cette section (point 3).

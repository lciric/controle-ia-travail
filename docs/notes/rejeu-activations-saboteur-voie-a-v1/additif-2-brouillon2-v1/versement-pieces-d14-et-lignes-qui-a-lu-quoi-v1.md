# Préparation pour la session mère : versement des quatre pièces de la condition D-14 et lignes du registre « qui a lu quoi » — v1

Note de travail (classe C), écrite le 2026-11-24 vers 09:52Z par la session fille `session_01Qi7Gr3DCGJkFuLgghCz7Mh`, à la demande de la session mère. Rien n'est versé ni inscrit par cette session.

## 1. Quatre fichiers à verser, source → cible, empreintes

Dossier source, pour les quatre : `docs/notes/rejeu-activations-saboteur-voie-a-v1/prealables-cote-expose-v7-brouillon/`. Chaque fichier se verse avec son compagnon `.sha256`, qui porte le nom de base seul et reste donc valable à la cible. Empreintes recalculées par `sha256sum` le 2026-11-24 à 09:51Z, toutes égales à leur compagnon. À cette heure, aucune des quatre cibles n'existe (rien à écraser, règle R12).

| n° | fichier source (dans le dossier source) | chemin cible, celui que fixe l'additif 1 | empreinte |
|---|---|---|---|
| 1 | `interface-passe-cote-moniteurs-v7.md` | `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v7.md` | `b16779bc3ee843c698debf825680b9847739f4a150a9aa3c9460b76048c277b6` |
| 2 | `interface-passe-cote-moniteurs-v7-champs.json` | `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v7-champs.json` | `dc4d0a1decddbc6bf893a28b8e748620f3881b4fe29d6da964b3521e64588c30` |
| 3 | `comparaison-interface-v6-v7-v1.json` | `docs/notes/barreau8-cote-moniteurs-sorties-v1/comparaison-interface-v6-v7-v1.json` | `e744d82406e5887a963b0e251b56152e3bbf9805ac1b3117ea6631b74b72c7c2` |
| 4 | `constantes-reportees-additif-1-v1.json` | `docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-1-v1.json` | `f6e9c8d5830dc503e129bc7b0c631a65ec8b8b61b7d4e5ac6c330910f9882171` |

Contrôle par programme après versement, depuis la racine du dépôt :

```
(cd docs/notes/barreau8-cote-moniteurs-entrees-v1 && sha256sum -c interface-passe-cote-moniteurs-v7.md.sha256 interface-passe-cote-moniteurs-v7-champs.json.sha256)
(cd docs/notes/barreau8-cote-moniteurs-sorties-v1 && sha256sum -c comparaison-interface-v6-v7-v1.json.sha256 constantes-reportees-additif-1-v1.json.sha256)
```

Deux précisions.

- La fiche des champs (n° 2) et la pièce de comparaison (n° 3) déclarent déjà, dans leur contenu, le chemin cible de la note version 7 : le versement ne demande aucune réécriture.
- Si la provenance du programme de comparaison de version 1 n'est pas attestée (brouillon 4, M-4), la pièce n° 3 sera remplacée, après le scellement, par une pièce réécrite sous un nom nouveau ; elle se verse quand même, comme pièce d'origine.

## 2. Lignes proposées pour le registre « qui a lu quoi »

Colonnes de la version 22 : `n° | session | compte | modèle | a lu | rôle | source | exclu de`. Le numéro est laissé à la session mère. Chaque ligne tient en moins de 600 signes.

```
| … | session_01Qi7Gr3DCGJkFuLgghCz7Mh | 01Qi7 | Fable 5.2 | brouillon 1 de l'additif 2 aux sondes du barreau 8, fiche de décision, extrait du côté exposé (D-13), note d'interface v7 et sa fiche, DONT les comptes d'identifiants et de jetons notés par condition tirés des sorties ; pièce d'attestation de l'ordre par programme ; aucune consigne, conception, ordre, épisode, score, état | rédactrice des brouillons 2 à 5 de l'additif 2, côté moniteurs | passation 2026-11-24-0948 ; brouillon 4, « Expositions » | lecteur des sondes, juge, auditeur, sauf décision nommée |
```

```
| … | sous-agent adc6213dbdc50eeb4 de session_01Qi7Gr3DCGJkFuLgghCz7Mh | 01Qi7 | Opus 5.5 | brouillons 1 à 4 de l'additif 2, contre-lecture R2 et complément, fiche de décision, extrait du côté exposé (D-13), note d'interface v7 et sa fiche, DONT les comptes par condition tirés des sorties ; pièce d'attestation de l'ordre par programme (booléens) ; aucune consigne, conception, ordre, épisode, score, état | vérificateur des corrections de l'additif 2, côté moniteurs | ses rapports de vérification, « déclaration de cloisonnement » | lecteur des sondes, juge, auditeur, sauf décision nommée |
```

La colonne « exclu de » est une proposition de prudence de cette session, non une règle scellée : l'additif 1 (ligne 25) annule le rôle de lecteur, de juge ou d'auditeur d'un agent qui a lu une sortie hors des voies écrites, et la question de savoir si ces comptes en sont une est portée à Lazar.

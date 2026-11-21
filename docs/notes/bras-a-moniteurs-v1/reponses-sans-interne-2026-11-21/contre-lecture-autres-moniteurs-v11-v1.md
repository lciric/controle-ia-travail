# Contre-lecture du module des autres moniteurs du bras A, version 11 — sans interne — v1

Écrit par un agent habilité neuf de la mère (Claude Opus 5.5, session `session_01Qi7Gr3eYmAhDEJzqLgWcv1`), le 21 novembre 2026, sous GO-2026-11-20-21. Lecteur neuf : n'a écrit ni le module ni ses essais. Classe B. Aucun nom de moniteur, de famille, de seuil, de trait, aucune valeur ni extrait de code de moniteur. Le fichier des scores par unité n'a pas été ouvert ; rien sous `donnees/`, `diag/`, `runs/`.

## Version qui fait foi
- Module : `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v11.py`, `e1130dadd1ee7f7ac1c8c19ab3edf69ca837f0fc016d681f0ef3e6956a927fda`, commit `e13ed9282` (branche `claude/bras-a-habilite-developpeur-v1`, inchangé jusqu'à la tête `5e5c17d8d`) ; compagnon égal.
- Essais : `tests/test_bras_a_v2_habilite_autres_moniteurs_v11.py`, `92711976e9ee949b08719b791cafc53932763ab96a04b6c01d34b0068cc3c776`, même commit ; compagnon égal.
- Différentiel 10 → 11 : `docs/notes/bras-a-moniteurs-v1/attestation-autres-moniteurs-v7-a-v10-v1/differentiel-autres-moniteurs-v10-a-v11.diff`, `b7ac6de62b8e0c7c5c8619dd29cd7af2b56a6b07fe2cfba27e15639fb4a19d0a` ; recalculé ici, identique.

Lu : mandats du développeur habilité v1 (sections 1, 2, 4), v2 (sections 4, 5), v3 ; module v10 et v11 ; essais v10 et v11 ; réponses sans interne aux demandes 18, 19 et 24 (a), v2 ; préparation des lectures v3 (en-tête et imports).

## Verdict : **conforme après corrections** (deux corrections mineures, hors calcul et hors garde du module)

- **Justesse.** De la version 10 à la version 11, seuls changent un paragraphe d'en-tête et l'empreinte inscrite d'un des deux programmes de production, qui passe à la préparation des lectures v3. L'empreinte inscrite est celle du fichier sur la branche (`c0021298…`, recalculée) ; l'autre empreinte inscrite est égale à son fichier. Aucun calcul, aucune garde, aucune graine ne change. Le lanceur v2 et le gabarit de configuration v2 citent la version 11 à son empreinte entière.
- **Garde (R5).** Le refus d'un manifeste de production portant la préparation v2 est éprouvé sur un cas sain et sur un artefact, à l'écriture et à la lecture.
- **Mandat.** Conforme au mandat v3 (point 4 : la préparation citée ne tire plus de positions) ; aucune lecture de résultat.
- **Essais rejoués ici** (arbre partiel extrait de la branche) : essais v11 `4 passed` ; essais v10 : 76 sur 77 passent (voir correction 1).
- **Épreuve par retrait** des essais v11, cinq retraits joués sur copie : empreinte remise à la v2, empreinte altérée d'un signe, garde des empreintes du manifeste neutralisée, garde des empreintes sur fichier neutralisée, une constante de calcul changée : **5 sur 5 mordent**.

## Corrections, dites sans interne
1. **Essai de la version 10 cassé par l'ajout de la version 11** : la garde statique du paquet des essais v10 (`test_garde_statique_du_paquet`) refuse désormais le fichier v11, absent de sa liste fermée des modules permis à charger un fichier par son chemin. La suite complète des essais du dépôt échoue donc sur cet essai. À corriger sans réécrire le fichier v10 (R12) : erratum qui déclare l'essai v10 remplacé par celui de la v11, ou essai v10 bis qui accepte la v11.
2. **Documentation périmée** : une phrase de la documentation d'une fonction (ligne 724 du module) décrit encore un tirage de positions que la préparation v3 ne fait plus ; sans effet sur un calcul (déjà relevée par la contre-lecture du lanceur). De même, l'en-tête des essais v11 renvoie aux essais du lanceur v1, remplacé par la v2. À corriger à la prochaine version ou par erratum.

Non rejoué ici : les essais du lanceur v2 (hors objet ; leur arbre complet manque à l'extraction partielle).

Incident d'outil : une attente par `sleep` a été bloquée par l'outil, qui indiquait sa propre méthode d'attente ; suivie telle quelle, sans contournement d'un contrôle.

Cette pièce ne dépense rien et n'autorise rien.

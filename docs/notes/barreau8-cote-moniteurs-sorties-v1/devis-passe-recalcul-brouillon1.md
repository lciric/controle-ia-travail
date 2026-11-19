# Devis de la passe de recalcul de l'activité interne du saboteur à budget — brouillon 1

Écrit par la conductrice côté moniteurs (session `session_013QMayjujdhnn94JyDTmgSs`) le 2026-11-19 vers 01:15Z. **Aucune dépense n'est engagée par ce document** : il sert à la demande d'accord de Lazar (condition de départ D-3 du texte de lecture des sondes). Aucun chiffre ici n'est mesuré.

## Ce que la passe fait
Elle rejoue dans le modèle `meta-llama/Llama-3.1-8B-Instruct` (révision de la note d'interface) les **2 560 actions de l'évaluation** de la course (64 tâches × 4 conditions × 10 actions), capte l'activité aux couches 7, 15 et 23, calcule sur la carte les scores des sondes figées et de leurs directions de plancher, et livre au côté des moniteurs **au plus 1 502 781 440 octets** de fichiers scellés. Elle est conduite par le côté exposé (l'exécutante du saboteur), avec le code écrit par le développeur du côté des moniteurs.
Sources : texte de lecture des sondes, brouillon 6 (`brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon6.md`, `527ed753e2434f0fd542e8f9a8c62ebcbf9ea7b32c7a8564ebed7c924ae65521`), section « Passe » ; note d'interface version 5 (`docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v5.md`, `407099bc150b8730237cceb0c1cf051440e255b483f44461b38a6c835c13107f`).

## Ordre de grandeur, non mesuré
Seule source chiffrée dont dispose le côté des moniteurs : la note du chemin critique (`docs/notes/barreau8-iib-v1/chemin-critique-saboteurs-discrets-entretien-v1.md`, `398215789b8a81c2fc1a167344b2a57f4c77c0f82304d22fea18c5627bf8d6fa`), § 1, ligne E7, qui reprend le devis du saboteur sans que ce devis ait été lu ici :

| cas | durée de carte | coût |
|---|---|---|
| attendu | 1,1 à 1,6 heure | environ 4,2 à 4,7 USD |
| au pire | 2,2 à 3,2 heures | environ 8,9 à 10,4 USD |

## Ce que le texte ajoute à cet ordre de grandeur, sans chiffre mesuré
Ces chiffres ont été écrits avant que le contenu de la passe soit fixé. Trois postes s'y ajoutent ; aucun n'est mesuré, et le côté des moniteurs n'a pas le tarif horaire de la carte :
1. **La seconde passe de répétabilité** sur un sous-échantillon d'une action sur huit (garde de répétabilité du texte) : de l'ordre d'un huitième de passe en plus.
2. **Le contrôle du contexte par la vraisemblance** sur 161 actions, avec le contexte d'une autre tâche : de l'ordre de deux fois 161 passes d'action.
3. **Les produits scalaires sur la carte** (2 403 directions à la couche 15, six sondes aux couches 7 et 23) : négligeables devant le passage du modèle.
4. **L'essai à blanc** sur une action, demandé avant la passe entière, et le chargement des deux adaptateurs.

## Ce que je propose de demander à Lazar
- **Plafond demandé : 12 USD**, soit le pire cas de la ligne E7 (10,4 USD) majoré d'environ 15 % pour les postes 1, 2 et 4. Si l'exécutante, qui connaît le tarif et le débit, estime que le plafond ne tient pas, elle le dit avant le départ et le devis est refait : la passe ne part pas sur un plafond douteux.
- **Arrêt** : par l'identifiant de l'instance (règle R10), au plafond de durée correspondant ; consigné au registre des arrêts par le côté exposé.
- **À faire remplir par le côté exposé avant la demande d'accord** : tarif horaire de la carte retenue, débit mesuré à l'essai à blanc (actions par minute), durée projetée, coût projeté.

## Hors de ce devis
La recette de puissance (au plus douze heures de processeur, sans dépense), la lecture décisive et la garde de réception tournent sur processeur du côté des moniteurs.

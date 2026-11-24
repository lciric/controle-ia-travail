# Passation — session fille du côté des moniteurs : brouillons 2 à 4 de l'additif 2 de format aux sondes du barreau 8

- **Session** : `session_01Qi7Gr3DCGJkFuLgghCz7Mh` (Fable 5.2, effort élevé), fille de `session_01Qi7Gr3Ggccg85kjmP654WC`. Mandat : accord GO-2026-11-24-07. Branche : `prep/additif-2-sondes-barreau8-brouillon2-v1`. Ni la branche principale ni ses registres ne sont touchés. Rien n'est scellé.
- **Dossier de livraison** : `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-brouillon2-v1/`.

## Fait

1. **Brouillon 2** de l'additif 2 (`5b69a914…`) : porte les quatorze constats de la contre-lecture (règle R2) du brouillon 1 et les deux remarques de son complément ; table « constat → correction ou refus motivé » (`7bd96a04…`) : seize corrigés, aucun refusé ; constat 3 par l'option (a), table neuve des constantes écrite par programme.
2. **Vérification 1** par un sous-agent Opus 5.5 neuf, non exposé (`9f0d073a…`) : « à corriger » ; les seize points portés ; trois défauts moyens, six mineurs, une remarque de forme.
3. **Brouillon 3** (`e3c747f1…`), boucle unique de correction, par programme rejouable (`e934a4fa…`).
4. **Vérification 2**, même sous-agent (`05d8850c…`) : **« à corriger »**. Rejeu du programme exact à l'octet ; liste fermée des passages complète ; validateur vide une fois les quatre lieux remplis ; rien ne touche sonde, seuil, métrique, état, table des issues, audit ni graines. Restent : un défaut moyen qui empêche le scellement (A), deux mineurs (B, C), deux remarques de forme.
5. **Brouillon 4** (`0d3f1adc…`), par programme rejouable (`5fb7cbba…`) : porte A, B, C et les remarques. **Il n'est pas vérifié** : le mandat ne permettait qu'une boucle.
6. Contre-lecture R2 et complément versés à l'identique depuis leur branche (`bfcb0f97…`, `8f5a4d87…`).

## Reste, pour la session mère

1. Décider la vérification du brouillon 4 (différence courte avec le brouillon 3 : huit remplacements, tous dans le programme) ; puis remplir AD2-1, AD2-2, AD2-3 et sceller.
2. **Mot de Lazar à demander** : la fiche de décision sur laquelle il a dit « go additif 2 option a » affirmait, à son point 10, les quatre bornes dures tenues, et disait O-3, O-5, O-6 « déjà gardés … et vérifiés sur le code ». Or les bornes (b1) et (b4) ne sont pas tenues à leur lettre pour la chaîne de l'additif 2 (brouillon 1 écrit par un agent du côté exposé qui a relevé des métadonnées des sorties ; comptes tirés des sorties dans la note d'interface version 7 et dans la fiche), et aucune garde ne tient O-3. Le brouillon 4 exige un mot de Lazar qui nomme cet écart.
3. Verser aux chemins que l'additif 1 fixe les quatre pièces de sa condition D-14 (aujourd'hui dans le dossier des préalables du côté exposé), empreintes égales.
4. Attester la provenance du programme de comparaison de version 1 (quatre exigences de l'additif 1) ; sinon « non attesté » : la version nouvelle réécrit la pièce de comparaison.
5. Après scellement : version nouvelle du programme de comparaison (instrument, code par Opus 5.5, contre-lecture) et table neuve des constantes ; nouvelle conformité des deux codes. La machine de la passe doit porter `transformers` 5.18.0 et `tokenizers` 0.23.2.

## Réserves

- **Exposition à déclarer au registre « qui a lu quoi »** : cette session et son vérificateur ont lu la note d'interface version 7, dont la question (3) et le point (d) portent des comptes d'identifiants et de jetons notés relevés sur les sorties de la course, par condition, et la fiche de décision, qui porte un compte d'ensemble. Aucune valeur n'est recopiée dans les brouillons. Ni cette session ni son vérificateur ne doivent tenir un rôle de lecteur des sondes, de juge ou d'auditeur sans que ce soit pesé.
- Cette session a ouvert par programme la pièce d'attestation de l'ordre (clés et états seulement) ; elle n'a ouvert ni `registres/etat.md`, ni la dernière passation de la branche principale, ni rien sous `runs/`, `diag/`, `donnees/`, ni aucune branche de la course.
- Routine de reprise, partielle : empreintes de lancement conformes ; `verifier-arbre` rend 8 problèmes antérieurs à cette session (compagnons de passations du 23 novembre), non corrigés ici ; essais du validateur et du scellement : 17 réussis ; suite complète non lancée (ni `scipy` ni `torch` dans ce conteneur) ; inventaire des instances non fait (session fille sans calcul).
- Le second rapport de vérification dit « entre 09:44Z et 09:55Z » ; l'horloge de ce conteneur donnait 09:47Z après sa remise : l'heure de fin y est inexacte.
- Écart au mandat, déclaré : le brouillon 4 dépasse la « seule boucle de correction » en écriture, non en vérification ; il est marqué « non vérifié » partout.

## Prochaine action

Session mère : porter le point 2 à Lazar ; faire vérifier le brouillon 4 ; sceller.

## Instances actives

Aucune. Aucune dépense, aucun appel externe payant.

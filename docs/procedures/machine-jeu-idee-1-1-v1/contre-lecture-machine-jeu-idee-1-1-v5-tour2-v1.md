# Contre-lecture de la procédure de la machine du jeu relancé de l'idée 1.1, v6, seconde contre-lecture de la chaîne v5 (tour 5 de la chaîne) (v1)

- **Auteur** : contre-lecteur neuf (R2), lettre C. Il n'a écrit aucune pièce (pièces de la lettre A). Il est aussi l'auteur des rapports des tours 1 à 4 (même lettre, session neuve à chaque tour).
- **Heures (UTC, `date -u`)** : de 22:43Z à 22:49Z environ.
- **Pièce jugée** : `procedure-machine-jeu-idee-1-1-v6.md` (`a5cad81e6396175eb4025f8d23315496ecd0dd4d84a666b88c24bb2d5ef8e849`, lue sur disque et par son compagnon), avec ses pièces v2 (lanceur, amorce, répétition et sa sortie, devis, rapport), le programme de couples `corriger_procedure_v5_vers_v6_tour4_v1.py` et la sortie du rejeu `sortie-repetition-machine-jeu-idee-1-1-v2-rejeu-procedure-v6.txt`. Les 30 compagnons du dossier : tous `OK`.
- **Rapport du tour précédent** : `contre-lecture-machine-jeu-idee-1-1-v5-tour1-v1.md`, `31566abb49841cbc59ca708d71f3c0797a78cb2e784a478485b0135f5e993c44` (empreinte recalculée, égale).

## Verdict : `scellable`

Les cinq couples A à E demandés au tour précédent sont appliqués fidèlement, la v6 est exactement la sortie du programme de couples, le différentiel v5 → v6 ne contient rien d'autre que ce que la v6 déclare, et les vérifications que les corrections pouvaient déranger tiennent (rejeu entier : 126 cas, 0 écart). Aucune correction exigée ; seules des remarques facultatives suivent.

## 1. Corrections demandées au tour précédent : appliquées ?

- **m1, couple A (§ 3, L3)** : oui, texte identique au couple du rapport (12 480 caractères, fourchette 12 400 à 12 700, 12 619 de la répétition à chemin plus long de 71 caractères écrit deux fois, « puis le reste, ≈ 6 480 »). Arithmétique relue : le dossier d'envoi réel `/home/user/jeu-idee-1-1-machine-envoi-v1` compte 40 caractères (compté) ; 12 619 − 2 × 71 = 12 477, dans la fourchette. Mon rejeu : ligne de 12 613 caractères avec un chemin de 105 caractères, soit 12 613 − 2 × 65 = 12 483 au vrai chemin, dans la fourchette.
- **m1, couple B (geste 5)** : oui, identique (≈ 12 650 octets, fourchette 12 500 à 12 800). Vérifié : 12 477 + 1 + 167 d'en-tête = 12 645 ; avec mon rejeu 12 483 + 1 + 167 = 12 651 : dans la fourchette.
- **m2, couples C (§ 1 pas 7) et D (geste 13)** : oui, identiques ; la formule dit « si elle tourne encore », nomme « non éprouvé », et renvoie à la destruction par l'identifiant (geste 13) et au rappel de la mère à l'échéance. Cohérent avec le reste (§ 1 pas 0 et 8, geste 15 : preuve par l'inventaire, jamais par la minuterie).
- **m3, couple E (geste 13)** : oui, identique. Vérifié sur l'amorce v2 : la ligne de journal est `fin, code $1 ; état « stopped » demandé maintenant ; …` (ligne 118), puis `état « stopped » demandé : HTTP …` (ligne 120) ; `fin de la machine, code $1` est le message de poussée (ligne 119) : la procédure le dit.
- **Changement de conséquence** (tour 5 au lieu du tour 4 dans le statut, en tête, et au § 2 point 3) : fait aux deux places. Les autres occurrences de « tour 4 rendu `scellable` » ou « pour le tour 4 » sont dans le récit historique du § 6 (réponses au tour 3) : exactes à leur date, à garder telles.

## 2. Différentiel v5 → v6 (`diff` entier)

- Seules lignes différentes : titre ; statut (liste des tours et condition du tour 5) ; version ; § 1 pas 7 (couple C) ; § 2 point 3 ; § 3 L3 (couple A) ; geste 5 (couple B) ; geste 13 (couples D et E) ; section « Tour 4 » ajoutée à la fin du § 6. Rien d'autre.
- Reproduction : `corriger_procedure_v5_vers_v6_tour4_v1.py` (lancé avec l'interpréteur isolé, dans le bloc-notes, sur la v5 `682ee4de…`, heure 2026-11-16T22:38:38Z) écrit un fichier **identique à l'octet** à la v6 (`a5cad81e…`) ; 11 couples, une occurrence chacun.
- La dernière phrase du § 6 (« Rien d'autre ne change de la v5 à la v6 : en tête…, les couples A à E, la condition du tour 5 au § 2 point 3 et cette section ») est **exacte** (contrairement à la phrase imprécise du tour 3, déjà notée F-a).
- Empreintes de la liste des pièces : inchangées par rapport à la v5 et toutes égales à leurs compagnons (compagnons tous `OK`). Le rapport du tour 4 est cité avec la bonne empreinte au § 6.

## 3. Vérifications refaites

1. **M1'' levée, reprise éprouvée** : lecture du différentiel amorce v1 → v2 (en-tête, fonction `reprise_sorties`, un seul remplacement de l'arrêt) ; `commit_pousser` reprend bien un commit non poussé à l'appel suivant (le cas « refusée trois fois puis acceptée » le montre). **Rejeu entier de la répétition v2** dans un dossier neuf du bloc-notes (`rep-c5/`), de 22:44Z à 22:48:32Z : **126 cas, 0 écart, code 0**. Différentiel contre la sortie gardée du rejeu v6 (chemins, heures, empreintes courtes et nombres normalisés) : trois lignes du cas « jamais acceptée », qui ne sont que de l'horloge (2 échecs au lieu de 3 ; 2 s au lieu de 13 s de la borne ; 15 s au lieu de 25 s) ; tous marqués `OK`. Aucun processus de la répétition ne reste vivant. L'artefact (amorce v1 : 11 écarts sur 126) a été joué au tour précédent sur les mêmes pièces, inchangées : non refait.
2. **Lanceur v2** : différentiel v1 → v2 relu (en-tête, `AMORCE=`, ligne imprimée, motif de `controle-ligne`) ; cas sain et artefacts de `controle-ligne` et d'`inventaire` : tous `OK` dans mon rejeu.
3. **Exactitude des tirages inchangée** : `3.13.18 2.4.6 1.17.1`, `PAQUETS`, `PYTEST_V` intacts dans l'amorce v2 (le différentiel ne les touche pas) ; mêmes cas de la répétition (versions fausses, commit hors de `main`, compagnon faux, empreinte différente) `OK`.
4. **Devis v2 et rapport v2** : non modifiés depuis le tour précédent (compagnons `OK`) ; l'écart de formule « la minuterie la détruit à l'échéance » (F-e) est déclaré au § 6 de la v6 : suffisant.
5. **Gestes tapables** : relus en entier (gestes 0 à 16) ; les seuls changements sont des valeurs attendues et des libellés, rien dans les commandes ; aucun appel au lanceur v1 dans les gestes.
6. **Clés, 7a, 7b, T0.7, modèles** : recherche faite sur la v6, l'amorce, le lanceur, la répétition, le devis, le rapport et le programme : aucune valeur de clé (`GH_TOKEN` et le jeton par leurs noms), rien de 7a, 7b, T0.6, T0.7, P3-bis, aucun identifiant de modèle (seul « claude » : le nom de dossier `.claude/`, sans valeur). Les clés factices sont absentes de toutes les sorties et branches de la répétition (cas `OK`).

## 4. Corrections exigées

**Aucune** (ni majeure ni mineure).

## 5. Remarques facultatives (aucune exigée)

- **R-a.** Geste 13 : la parenthèse ouverte à « (code 2 ou 4 ; sur « RESERVE… » » contient maintenant trois phrases et se ferme après « …depuis la machine) » : lisible mais lourde ; à alléger dans une version future, sans objet pour le départ.
- **R-b.** Le rejeu nommé `…-v2-rejeu-procedure-v6.txt` n'est pas dans la liste des pièces de la v6 (le § 6 le déclare et dit que la sortie gardée reste la v2) : cohérent, à garder.
- **R-c.** Restes déjà déclarés et inchangés (F2 geste 8, F4 geste 9, F-b reprise sur le code 3, F-c recopie partielle, F-d trafic extrême) : non exigés.
- **R-d.** Le cas « jamais acceptée » de la répétition dépend de l'horloge (nombre d'échecs de 2 à 3, écarts de quelques secondes) ; ses critères l'admettent (deux rejeux passent), à garder en tête si un rejeu futur donne un écart isolé.

## 6. Points pour la mère

- **Verdict `scellable`** : la procédure v6 peut être scellée telle quelle ; le feu reste soumis aux restes ci-dessous.
- **Fait à garder en tête (m2)** : « l'état « stopped » arrête-t-il la minuterie ? » reste une question de fait sur le loueur que seule une machine réelle tranche ; la v6 la dit non éprouvée. Le rappel programmé à l'échéance est donc le garde-fou, pas une option.
- **Mots de Lazar nécessaires (inchangés)** : ligne de GO « calcul » (périmètre « idée 1.1 », `3.5 USD`, échéance 2026-11-22 au plus tôt ; pire cas de 3,24 à 3,30 USD au-delà de l'ordre de grandeur de 1 à 3 USD, plafond à faire accorder tel quel) ; permission de la ligne neuve ; renouvellement du jeton après la preuve de destruction.
- **Restes de la mère** : `COMMIT` à relire au feu (la tête de `main` bouge) ; rappel programmé à l'échéance ; dossier à commiter ; fichiers à la racine `/s.txt`, `/commande-coupee.txt` et `/x` (présents, non touchés, nom seul lu) à effacer par une personne.
- Aucun écart à un texte scellé de ma part.

## Déclaration

- Rôle : contre-lecteur neuf (R2), lettre C ; aucune pièce modifiée ; aucun commit ; ce fichier est neuf.
- Accès extérieurs : aucun accès réseau de ma main ; la répétition n'utilise qu'un dépôt jouet local en `file://` et un loueur simulé ; lecture du dépôt principal en lecture seule par la répétition. Aucun appel au loueur, aucune machine, aucune dépense, aucune poussée. Aucune clé lue ou affichée ; le texte du verbe interdit n'a été tapé dans aucune commande.
- Lu : rien sous `diag/`, `runs/`, `donnees/` ; rien de `/home/user/jeu-idee-1-1-copie-v1`.
- Calcul : léger (une répétition d'environ 4 minutes 30 : `rep-c5/` du bloc-notes, plus la reproduction de la v6 dans `c5/`).
- Fichiers écrits : ce rapport (dossier de la procédure) et le bloc-notes seulement ; rien à la racine.
- Incidents de ma main : aucun.

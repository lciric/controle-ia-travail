# Vérification courte du brouillon 4 et du texte candidat du complément au quatrième addendum d'écart — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Contre-lecteur** : le même sous-agent neuf qu'aux brouillons 1 et 3 (modèle Opus 5.5). Je n'ai écrit ni le complément, ni `lecture_v4.py`, ni aucun code de l'étape B bis (R2).
- **Pièces** (empreintes recalculées, égales aux compagnons quand il y en a) :
  - brouillon 4 : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-complement-brouillon4-v1.md`, `3ce8447fe75f3903bb6953a2178c29ed1bd7885c4a511361501e756d6d3c9466` ;
  - différences du brouillon 3 au brouillon 4 : `be3f3b07…` ;
  - texte candidat, sans compagnon : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, `a7dc8812dccf72a0bdcdd521c5671446a69674a32cf220a7f894fec64bf0d788` ;
  - `src/controle_ia/t07bbis/lecture_v4.py` : `9bfca626…`, égale à son compagnon ; commit `bb6f91f5b3bd…` (2026-11-18T21:57:34Z), ancêtre de la tête.
- **Méthode** : par simple lecture. `diff` du brouillon 3 au brouillon 4, puis du brouillon 4 au texte candidat ; comptage par un programme de lecture seule ; `grep` borné des lignes qui lancent une commande git ; `git log`, `git merge-base`, `git show origin/main:` des deux registres, filtré par `grep`. Aucune garde jouée, aucun fichier de résultat ouvert.

## Conclusion

**Scellable après correction mineure** : e1, et elle seule.

Constats : 0 majeur, 1 mineur, 6 notes.

## 1. Constat mineur

**e1 — La liste des passages que couvre la règle de préséance en oublie deux.**

La règle de préséance du § 0 énumère les passages de A4 où le module qui lit, ou sa clé, se lisent désormais `lecture_v5` et `…-V5-…` : « A4, en-tête […] ; § 3 […] ; § 6.3 […] ; § 7, points 8 et 11. » Cette liste se donne pour complète. Elle oublie :
- la ligne proposée du § 7 de A4 (l. 550 : « module de lecture rattaché par RATTACHEMENT-LECTURE-V4-BBIS ») ;
- la colonne « décision » de la ligne `ADDENDUM-ECART-4-BBIS` déjà inscrite sur `main` au registre voisin, qui porte mot pour mot « module de lecture lecture_v4 rattaché par RATTACHEMENT-LECTURE-V4-BBIS ». Cette ligne ne se réécrit pas.

Le principe général de la règle couvre déjà ces deux passages. C'est pourquoi le constat est mineur.

**Correction exacte**, faite une fois, dans le § 0 du brouillon 4 et du texte candidat. Remplacer « § 7, points 8 et 11. » par :

« § 7, ligne proposée (l. 550) et points 8 et 11 ; et, au registre voisin, la colonne « décision » de la ligne `ADDENDUM-ECART-4-BBIS` déjà inscrite (« module de lecture lecture_v4 rattaché par RATTACHEMENT-LECTURE-V4-BBIS »), qui ne se réécrit pas et se lit de même. »

## 2. Notes

**n1 — Les corrections d1 à d3 sont portées mot pour mot.**
- d1 : le point (A3) épingle le commit `7322049d…` et lie ce commit à `SCORES-BBIS` ; la seconde phrase est remplacée ; le point ouvert 7 devient « nœud de Lazar », non bloquant, avec la voie de l'arrêt avant le seuil fermée jusqu'à son mot.
- d2 : le point (A2) exclut les fichiers que citent les lignes `PANNE-MISE-EN-PLACE-BBIS-<n>`.
- d3 : aux deux endroits.

**n2 — Le nom du module final (b) est conforme.**
- Les six blocs « ancien » de CQ-1 à CQ-6 sont exacts et uniques dans A4 (l. 574, 64, 313, 500, 503 et 506 ; comptage 1 chacun). Ils sont absents de T, A1, A2 et A3. Dans T, `lecture_v4` n'apparaît qu'aux l. 19 et 115, où il nomme le module d'une autre étape, ce que le § 0 dit.
- La règle de préséance garde vraies les phrases de A4 sur la v4 elle-même (six différences, ses essais, son différentiel), puisque la v4 rendue n'est pas modifiée. Elle déplace sur la v5 ce qui touche au module qui lit (lancement, empreinte, rattachement, clé). Sous e1, elle couvre toutes les mentions.
- Le rattachement reste conforme : aucune troisième ligne `CODE-BBIS` (le registre propre sur `main` en porte deux) ; aucune ligne `RATTACHEMENT-…` n'est inscrite au registre voisin, la clé de la v5 remplace donc celle de la v4 sans s'y ajouter.
- Rien n'élargit la lecture : la v5 est la v4 plus D7, D8 et le nom du module, vérifiés par un différentiel.
- Le nom du module et D8 sont dits « décision de la conductrice » et « demande de la mère », non mots de Lazar, et le statut le répète.

**n3 — D8 couvre bien toutes les commandes git.** Relevé par lecture des lignes qui lancent `git` dans le module et les modules qu'il importe :
- `lecture_v4.py`, l. 673 (preuve d'entrée conjointe) et l. 813 (`_git`) ;
- `gardes.py`, l. 94 (état du dépôt, par le manifeste) ;
- `lien_mots_et_cout_v1.py`, l. 117 (code de la pièce au commit cité, par `charger_adaptateur`).

Aucun autre module importé par la lecture ne lance git. `exiger_ancetre`, dans `registre_bbis_v1.py`, n'est pas appelé par la lecture. La liste du § 6 est donc exacte et complète. Appelée en première instruction de `main`, la garde précède toute commande git, tout registre et toute ouverture, et les processus fils héritent de l'environnement.

**n4 — D8 est non ambiguë, assez étroite, et ne peut changer aucune issue.**
- Le refus sans nettoyage est l'une des deux formes que la mère permet, la seule sans repli silencieux (R5). Le préfixe `GIT_` est exactement celui que la mère nomme.
- L'arrêt vient avant tout le reste et n'écrit rien : il ne peut changer aucune issue.
- Le classement est juste : c'est un arrêt avant le seuil, sans rien écrire, donc la voie de GO-2026-11-18-64, fermée jusqu'au mot de Lazar sur le point 7. Le complément le dit, et dit que la commande l'évite par un geste écrit.
- Ce qu'elle ne voit pas est dit honnêtement au § 4, point 7 : configuration de git, programme `git` du chemin, variables d'autres noms.
- Essais : cas sain et artefact (variable posée, aucune commande git lancée, nom sans valeur, `GITHUB_TOKEN` non refusé).
- Pour le développeur, sans correction du texte : les essais doivent fixer eux-mêmes l'environnement (variables `GIT_*` retirées dans le cas sain), l'environnement d'essai pouvant en porter.

**n5 — Texte candidat et ligne de registre.**
- Le texte candidat ne diffère du brouillon 4 que par le titre et le statut.
- Le statut sépare ce que Lazar a accordé (GO-2026-11-18-60, GO-2026-11-18-64) de ce qui a été décidé sous l'autonomie (nom du module, D8), et dit ce qui reste à Lazar (point 7). Sans heure écrite, il est acceptable : il renvoie à l'heure de la ligne du registre voisin.
- La ligne proposée est au format à cinq colonnes.
- Je n'ai trouvé aucun passage sans fondement, hors e1.

**n6 — Ce qui n'est pas contre-lu.** Les passages sur le nom du module et sur D8 sont contre-lus par ce rapport ; le complément les dit encore « non contre-lus » (point ouvert 6). La mère peut le corriger à l'inscription ; ce n'est pas exigé pour sceller.

## 3. Points ouverts

| point | statut |
|---|---|
| 1. arrêt avant le seuil | couvert par la décision de Lazar (GO-2026-11-18-64) ; clos |
| 2. nombre de relances | couvert par la décision de Lazar (GO-2026-11-18-64 : sans limite) ; clos |
| 3. clés au registre voisin | question d'organisation pour la mère, admises ; clos |
| 4. lettre « écrite dans le quatrième addendum » | question d'organisation pour la mère, forme admise ; clos |
| 5. code de sortie 3, lignes imprimées, sorties gardées | question d'organisation pour la mère |
| 6. contre-lecture | faite (brouillons 1, 3 et ce rapport pour le brouillon 4) |
| 7. lecture de « égales à celles de `SCORES-BBIS` » | **nœud de Lazar**, non bloquant ; la voie de l'arrêt avant le seuil reste fermée jusqu'à son mot |
| 8. nom du module final, `lecture_v5` | décision de la conductrice et accord de la mère (question d'organisation) ; conforme ; clos |
| 9. garde des variables de git, D8 | demande de la mère ; question d'organisation pour la mère (geste de la commande qui retire les variables `GIT_*`, noms seulement) ; non bloquant |

## 4. Fichiers ouverts

- Les brouillons 3 et 4 du complément et le texte candidat, par `diff`.
- La liste des différences : empreinte seulement.
- Le quatrième addendum scellé : comptage, et lignes trouvées par `grep`.
- T, A1, A2 et A3 : comptage seulement.
- `lecture_v4.py`, `gardes.py`, `lien_mots_et_cout_v1.py`, `registre_bbis_v1.py`, `t07/code_t07_v1.py`, `harnais/validation_reelle.py` : lignes qui lancent git, par `grep`. Les imports de `lecture_v4.py`, par `grep`.
- Sur `origin/main`, par `grep` : le registre voisin des addenda et le registre propre.
- Le commit `bb6f91f5b` : identifiant, heure, titre et ascendance.

**Fichiers de résultat** : aucun, ni à l'œil ni par la chaîne.

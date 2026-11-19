# Contre-lecture du brouillon 1 du complément au quatrième addendum d'écart — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Contre-lecteur** : sous-agent neuf de la session conductrice de la lecture (`session_013QMayjNC5GKdDFTN87oAV5`), modèle Opus 5.5. J'ai contre-lu les deux brouillons du quatrième addendum (`5e0c2fa5…`, `6be5c46e…`). Je n'ai écrit ni ce complément, ni le quatrième addendum, ni aucun code de l'étape B bis (R2).
- **Mandat** : celui du contre-lecteur du quatrième addendum (`8ef5aa28…`), les règles communes (`5f303a9c…`), et la suite transmise par la conductrice le 2026-11-18.
- **Pièces** (empreintes recalculées) :
  - complément contre-lu : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-4-complement-brouillon1-v1.md`, `a5f4dc5ac5e911ba699a758eea742e4d88e14c53e116cb9aefb3120de66f6ca7`, égale au compagnon ;
  - quatrième addendum scellé : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-v1.md`, `5ef929ea…`, égale au compagnon et à la ligne `ADDENDUM-ECART-4-BBIS` du registre voisin sur `origin/main` (2026-11-18T21:36:33Z).
- **Méthode** : par simple lecture. Lecture de fichiers, `grep` borné, `sha256sum`. Un comptage d'occurrences de chaînes dans les textes scellés, par un programme de lecture seule. Aucune garde ni fonction du module appelée, aucun fichier de résultat ouvert.

## Conclusion

**Scellable après corrections mineures** : c1 à c6 ci-dessous, et elles seules.

Constats : 0 majeur, 6 mineurs, 8 notes.

## 1. Vérifications faites

- **Décision.** `git show origin/main:registres/go.md | grep -n "^| GO-2026-11-18-60"` rend la l. 424. Le § 1 la cite mot pour mot. Le complément ne va pas au-delà, sous les corrections c1 et c3 qui le resserrent :
  - issue I0 née d'un pur défaut de mise en place, non consommée ;
  - preuve par programme d'aucune ouverture (aucune entrée lue, aucune ligne `OUVERTURE-BBIS`) ;
  - panne corrigée, déclarée, relance ;
  - tout arrêt après une ouverture consomme la lecture.
- **Faits du code, § 2.0**, relus dans `lecture_v3.py`. Tous exacts.
  - Bloc de la garde : l. 1235-1264, dans l'ordre et aux lignes citées. `GardeEntrees` est construite à la l. 1254 ; le fichier d'issue de l'épreuve du signal planté est ouvert l. 1255.
  - `sondes-bbis.json` est ouvert l. 1270, `charger_tableaux` appelé l. 1290, `verifier_deux_premieres` l. 1291. `GardeEntrees.exiger` (l. 538-548) consigne dans `lus`.
  - Le journal n'est écrit qu'à la l. 1453, après `ecrire_lecture` (l. 1452). Forme : `| OUVERTURE-BBIS | date | quoi | empreinte |` (`registre_bbis_v1.journaliser_ouverture`, l. 113-119).
  - Sur un refus de la garde, `lire` rend I0 (l. 1261-1264), puis `main` écrit le fichier et la ligne de journal : exact.
  - Un arrêt (`GardeArret` hors du bloc, arbre non propre au manifeste) rend le code 2 sans fichier ni ligne de journal : exact.
  - `sceau_conforme` (`t07/registre_v1.py`, l. 108-123) a quatre motifs : exact. Il calcule l'empreinte du fichier **avant** de chercher le compagnon (l. 113) : voir c2.
- **Blocs « ancien » CQ-1 à CQ-6.** Chacun figure une fois exactement dans le quatrième addendum scellé, retours de ligne compris, aux l. 574, 421, 313, 450, 461 et 491. Aucune occurrence dans T, A1, A2 ni A3.
  - « D1 à D6 » figure une troisième fois dans le quatrième addendum (l. 610, questions au contre-lecteur, historique) et « D2 à D6 » une fois (l. 424, docstring D1). La préséance du § 0 couvre ces deux mentions.
- **Ligne de registre proposée** : au format à cinq colonnes du registre voisin. Conforme.
- **Antériorité** : la règle est écrite avant tout cas réel ; aucune garde jouée sur l'arbre de lecture ; appuis déclaratifs, dits tels (§ 5). Conforme.

## 2. Constats

### Mineurs

**c1 — Le seuil « après une ouverture » est placé trop tard (D7 (c), (O2), règle « Tout arrêt », § 4 point 2, essais 2 et 4).**
- **Le constat.** La ligne imprimée « garde passée » vient « sitôt le bloc de la garde passé ». Mais dans ce bloc, l. 1255, `GardeEntrees.exiger` ouvre déjà une entrée : le fichier d'issue de l'épreuve du signal planté, résultat d'une autre chaîne. La décision fixe le seuil à la première ouverture (« tout arrêt après une ouverture consomme la lecture »).
- **L'effet.** Un arrêt entre la l. 1255 et la fin du bloc donne un code 2 sans la ligne : par exemple une entrée hors liste blanche ou de la liste « Jamais », levée par `GardeArret`. Le brouillon le rangerait alors au point ouvert 1, donc ouvert à une décision de relance, alors que la décision dit qu'il consomme. Le § 4, point 2 (« « garde passée », avant toute ouverture ») est inexact pour la même raison.
- **Corrections exactes :**
  - D7 (c) : remplacer « **(c) Dans `lire`, sitôt le bloc de la garde passé et avant la l. 1265 de la v3** : la ligne `BBIS LECTURE GARDE PASSEE` est imprimée (aucune valeur ; un état). » par « **(c) Dans `lire`, immédiatement avant le premier appel de `GardeEntrees.exiger` (l. 1255 de la v3, fichier d'issue de l'épreuve du signal planté)** : la ligne `BBIS LECTURE ENTREES OUVERTES` est imprimée (aucune valeur ; un état). » ;
  - (O2) : remplacer « **(O2) la garde n'est pas passée** : le module n'a pas atteint le point où il imprime « garde passée » (D7, point (c)) ; » par « **(O2) aucune entrée n'a été ouverte au sens de la ligne imprimée** : le module n'a pas imprimé la ligne `BBIS LECTURE ENTREES OUVERTES` (D7, point (c)) ; » ;
  - règle « Tout arrêt après une ouverture » : remplacer « Dès que la garde est passée — ligne « garde passée » imprimée —, » par « Dès la première ouverture d'une entrée — ligne `BBIS LECTURE ENTREES OUVERTES` imprimée, avant le fichier d'issue de l'épreuve du signal planté —, » ;
  - § 4, point 2 : remplacer « une ligne imprimée, « garde passée », avant toute ouverture » par « une ligne imprimée, `BBIS LECTURE ENTREES OUVERTES`, avant toute ouverture d'une entrée de la liste blanche » ;
  - essai 2 : remplacer « garde passée (O2) » par « ligne `BBIS LECTURE ENTREES OUVERTES` imprimée (O2) » ;
  - essai 4 : remplacer « une garde d'arrêt déclenchée après le passage de la garde → la ligne « garde passée » a été imprimée » par « une garde d'arrêt déclenchée après la première ouverture, dont une levée dans le bloc de la garde après la l. 1255 (entrée hors de la liste blanche) → la ligne `BBIS LECTURE ENTREES OUVERTES` a été imprimée » ;
  - D7, dernier tiret (l. 296), § 7 point 5 (l. 338) et § 8 (l. 352) : remplacer « « garde passée » » par « `BBIS LECTURE ENTREES OUVERTES` ».

**c2 — « Aucun fichier de scores lu » : les empreintes sont calculées sur les octets des fichiers cités (§ 4, « Elle établit »).**
- **Le constat.** Toute exécution, refus compris, lit les octets des fichiers cités par les lignes des deux registres pour en calculer l'empreinte. C'est le cas du fichier de `SCORES-BBIS` (`verifier_lignes`, l. 1244, puis `sceau_conforme`, l. 113). Ces octets ne sont ni décodés ni gardés. La preuve (O1) ne couvre que la liste blanche ; le § 2.0 le dit, le § 4 non.
- **Correction exacte** : ajouter à la fin du paragraphe « **Elle établit** » : « Elle n'exclut pas le calcul d'empreinte : à toute exécution, refus compris, les fichiers cités par les lignes des deux registres, dont celui de `SCORES-BBIS`, sont lus octet par octet pour en recalculer l'empreinte, sans être décodés ni gardés. « Aucun fichier de scores lu » se lit : aucun fichier ouvert par la liste blanche des entrées, empreintes seules calculées. »

**c3 — Les exécutions antérieures ne sont couvertes que par les relevés de l'opérateur : le rendre vérifiable à la déclaration (§ 2, « La suite », point 3 ; réserve R-RELANCE).**
- **Le constat.** La preuve vaut pour l'exécution qui refuse. Une exécution antérieure qui aurait passé le seuil puis se serait arrêtée en code 2 ne laisse ni fichier ni ligne au journal : la preuve suivante serait conforme alors qu'une donnée a été ouverte. Le § 4, point 2, le dit honnêtement, et la règle s'en remet aux sorties gardées par l'opérateur.
- **Ce qui manque.** Rien n'oblige à rapprocher ces sorties lors de la déclaration, et R-RELANCE ne nomme pas cette limite.
- **Corrections exactes :**
  - point 3 de « La suite », après « nom du run de la relance » : ajouter « ; la liste de **tous** les lancements antérieurs de la commande de lecture sur l'arbre de lecture, chacun avec sa sortie imprimée gardée, scellée, citée par chemin et empreinte ; aucune ne porte la ligne `BBIS LECTURE ENTREES OUVERTES`. Un lancement sans sortie gardée, ou dont la sortie porte cette ligne : la lecture est consommée, aucune relance » ;
  - réserve R-RELANCE : remplacer « cette preuve ne voit pas une ouverture faite hors du module. » par « cette preuve ne voit pas une ouverture faite hors du module, ni une exécution antérieure arrêtée sans trace : celles-ci sont couvertes par les sorties gardées de chaque lancement, citées par la déclaration. »

**c4 — (M3) n'est pas la plus étroite : un commit nommé absent n'est de mise en place que dans un dépôt superficiel.**
- **Le constat.** Les trois commits nommés par la preuve d'entrée conjointe sont ancêtres du commit de la course (vérifié au brouillon 1 du quatrième addendum). Dans un dépôt **non** superficiel dont la tête descend du commit de la course, leur absence est impossible ; elle dirait une histoire autre, ce qui est un défaut de fond. La règle « tout motif hors de (M1) à (M3) est de fond » le range aujourd'hui en mise en place.
- **Correction exacte** : dans (M3), remplacer « ou l'un des trois commits nommés par la preuve d'entrée conjointe de A4 est absent du dépôt ; » par « ou, le dépôt étant superficiel, l'un des trois commits nommés par la preuve d'entrée conjointe de A4 en est absent ; » ;
- dans la liste « N'en sont pas », ajouter après « le commit du scellement introuvable dans un dépôt **non** superficiel ; » : « un commit nommé par la preuve d'entrée conjointe absent d'un dépôt **non** superficiel ; » ;
- essais, point 1 : « commit nommé absent » devient « commit nommé absent d'un dépôt superficiel » ; ajouter au point 3 « commit nommé absent d'un dépôt non superficiel ».

**c5 — Arbre propre : la relance doit partir d'un arbre commité, et la portée réelle de (M1) et (M2) doit être dite (§ 2, « La suite », point 4 ; § 4, point 4).**
- **Le constat.** `manifeste.creer_manifeste` refuse un arbre non propre en lecture réelle, et compte les fichiers non suivis (`gardes.py`, l. 100 : `status --porcelain --untracked-files=all` ; `manifeste.py`, l. 81-83). Il ne joue qu'après tout le calcul (`ecrire_lecture`, appelé l. 1452). Trois conséquences :
  - (i) après un refus de mise en place, le fichier gardé, la pièce de preuve, le manifeste du run refusé et la correction salissent l'arbre. Une relance non précédée d'un commit passerait le seuil, ouvrirait les données, puis s'arrêterait au manifeste : lecture consommée par un geste. Le brouillon ne l'interdit pas ;
  - (ii) un fichier cité suivi à la tête mais absent du disque est un fichier supprimé, donc un arbre non propre : (M1) aboutit alors au code 2 sans issue, cas du point 4 du § 4 (que le brouillon nomme), non à l'I0 de la règle. (M1) n'atteint l'I0 que pour un fichier absent de la tête ;
  - (iii) le registre partagé absent arrête `main` en code 2 **avant** `lire` (`adaptateur_retenu`, l. 1422) ; le registre propre absent l'arrête après (`main`, l. 1449-1451). (M2) n'atteint donc jamais l'I0.

  Les essais jouets, qui permettent un arbre non propre (`autoriser_depot_sale = not reel`, `ecrire_lecture`), ne le montrent pas.
- **Corrections exactes :**
  - au point 4 de « La suite », ajouter avant « La garde est rejouée entière. » : « Avant la relance, la correction, le fichier de lecture gardé, la pièce de preuve, le manifeste du run refusé et la déclaration sont commités sur la branche de l'arbre de lecture ; la commande vérifie l'arbre propre avant le lancement (A4, § 6.5, point 4) ; sinon rien n'est lancé. » ;
  - au § 4, point 4, ajouter à la fin : « Par le déroulement de la v3, (M2) n'atteint jamais l'issue I0 (registre partagé absent : arrêt dans `adaptateur_retenu`, l. 1422, avant `lire` ; registre propre absent : arrêt l. 1449-1451) ; (M1) ne l'atteint que pour un fichier absent de la tête de l'arbre de lecture, un fichier suivi et absent du disque rendant l'arbre non propre (`gardes.py`, l. 100). (M2) est gardé dans la définition sans effet. Les essais jouets, qui admettent un arbre non propre, ne couvrent pas ce point. »

**c6 — CQ-1 laisse debout, dans le même point, une réponse de la mère que la décision remplace.**
- **Le constat.** Le point 4 de A4 garde « aucun mode neuf qui rejouerait une mise en place refusée » (A4, l. 572-573), juste avant le « Clos … » ajouté par CQ-1 qui permet la relance. La lecture du point est contradictoire.
- **Correction exacte** : dans le bloc « nouveau » de CQ-1, insérer après « **Clos après le scellement par GO-2026-11-18-60** (R-3449) : » les mots « la réponse de la mère citée ci-dessus (« aucun mode neuf qui rejouerait une mise en place refusée ») ne vaut plus que hors de cette règle ; ».

### Notes

**n1 — La relance ne peut pas servir à choisir une issue.**
- Elle ne suit qu'un refus où aucune entrée n'a été ouverte : rien n'est connu.
- Les tirages ne dépendent pas du nom du run : `Graines(int(fiche["entropie"]))`, clés `bbis/tirages/<ligne>` (`lire`, l. 1272 ; `ecrire_lecture`, l. 1402). La relance tire donc les mêmes graines.
- La correction ne change ni registre, ni texte, ni module, ni entrée, et la garde rejouée entière le contrôle par empreintes.

**n2 — La preuve d'aucune ouverture peut-elle être écrite alors qu'une donnée a été ouverte ?**
- Dans la même exécution : non, sous c1. Avant la ligne imprimée, le module ne lit que les registres, l'histoire git, du code et des octets pour des empreintes (c2).
- Par une exécution antérieure : oui, sans c3. C'est le seul cas, et c3 le ferme par la déclaration.
- Hors du module : la preuve ne le voit pas, et le § 4 le dit.

**n3 — Refus mêlé et ordre des contrôles.** La garde s'arrête au premier motif levé. Un registre qui a un fichier non extrait **et** un ordre inversé refuse d'abord en mise en place (`verifier_lignes`, l. 1244, avant l'ordre, l. 1246). La relance rejoue alors l'ordre et refuse en fond. Sans dommage : rien n'est ouvert, et le refus de fond consomme.

**n4 — Définition fermée.** Hors c4, (M1) à (M3) sont fermés, relevables à l'endroit du refus par la classe `RefusMiseEnPlace`, et les « autres motifs » de `sceau_conforme` restent de fond. Aucun des refus de fond nommés ne peut être reclassé :
- l'ordre hors l'exception ;
- l'antériorité de l'étape B ;
- l'issue de l'épreuve autre que « vu » (branche hors du `except`, l. 1258-1260, sans nature) ;
- l'empreinte différente.

**n5 — Spécification de D7** : limitée à la décision. Aucun paramètre n'ouvre la règle ; essais sains et artefacts pour chaque motif et chaque point de la preuve, sur jouets seulement. Sous c1, c4 et c5, rien d'ambigu.

**n6 — Forme.** Celle des addenda : blocs « ancien » / « nouveau » ; préséance qui nomme ses passages ; réserve nommée R-RELANCE ; ligne au bon format.

**n7 — Dans un dépôt superficiel, la garde de la v3 peut passer à tort** (antériorité de l'étape B lue sur une histoire tronquée). Ce point relève du quatrième addendum (commande : clone à histoire complète, feu, § 12, l. 974), non de ce complément.

**n8 — Condition levée au brouillon 2.** Pris acte de la pièce citée par la conductrice (`levee-condition-contre-lecture-addendum-4-v1.md`). Je ne l'ai pas ouverte, mon mandat ne le demandant pas ; la ligne du registre voisin cite « condition levée f3eb78da ».

## 3. Points ouverts du complément

| point | statut |
|---|---|
| 1. arrêt du programme avant le seuil, sans issue ni preuve écrites | **nœud de Lazar** pour en ouvrir la relance. La décision parle d'une issue « non lue » et d'une preuve écrite ; ni l'une ni l'autre n'existent ici, et le complément a raison de ne pas le couvrir. Sous c1, tout arrêt **après** la ligne imprimée est consommé par la décision et n'est pas de ce point. Non bloquant pour le scellement |
| 2. nombre de relances | couvert par la décision de Lazar (elle ne fixe aucune borne ; chaque relance est déclarée, inscrite et sans information, n1). Une borne serait un choix d'organisation de la mère, non exigé |
| 3. clés neuves au registre voisin | question d'organisation pour la mère (précédent admis : `RATTACHEMENT-LECTURE-V4-BBIS`) |
| 4. lettre « écrite dans le quatrième addendum » | question d'organisation pour la mère, tranchée selon la conductrice (forme du complément admise par la mère) ; un texte scellé ne se réécrit pas (R12) |
| 5. code de sortie 3, lignes imprimées | question d'organisation pour la mère (commande de lecture, mandat du lecteur-opérateur) |
| 6. contre-lecture | faite (ce rapport) |

## 4. Fichiers ouverts

- les règles communes et le mandat du contre-lecteur (empreintes) ;
- le complément ;
- le quatrième addendum scellé : comptages, l. 568-580, et lignes trouvées par `grep` ;
- T, A1, A2, A3 : comptages seulement ;
- sur `origin/main` : la ligne `GO-2026-11-18-60` de `registres/go.md`, seule, et les dernières lignes du registre voisin ;
- `lecture_v3.py` : l. 505-556, 1264-1300, 1396-1458 et lignes trouvées par `grep` ;
- `t07/registre_v1.py` : l. 100-125 ;
- `registre_bbis_v1.py` : `journaliser_ouverture`, `lire_fiche_code`, `exiger_partage_sans_bbis` ;
- `manifeste.py` : lignes trouvées par `grep` ;
- `gardes.py` : l. 100 ;
- `commun_v1.py` : classe `Graines`.

**Fichiers de résultat** : aucun, ni à l'œil ni par la chaîne.

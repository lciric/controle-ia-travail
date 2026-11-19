# Contre-lecture du brouillon 3 et du texte candidat du complément au quatrième addendum d'écart — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

- **Contre-lecteur** : le même sous-agent neuf qu'au brouillon 1 (modèle Opus 5.5 ; rapport `29c78e186ee602e8cad8079377c6eafdbd141ae46beb614c52277d55647e19ba`). Je n'ai écrit ni le complément, ni ses différences, ni le texte candidat (R2).
- **Pièces** (empreintes recalculées, égales aux compagnons quand il y en a) :
  - brouillon 2 : `addendum-ecart-4-complement-brouillon2-v1.md`, `c4394eee…` ;
  - différences du brouillon 1 au brouillon 2 : `c38da95b…` ;
  - brouillon 3 : `addendum-ecart-4-complement-brouillon3-v1.md`, `d9affd94e094fc5ddb941542b5a2b04c14ca440af1fdd492e879fca8fa719abe` ;
  - différences du brouillon 2 au brouillon 3 : `a055f3cc…` ;
  - texte candidat, sans compagnon : `prereg/T0.7-etape-B-bis-v1-addendum-ecart-4-complement-v1.md`, `dca3631a2f4e35fc7771a72488d979126e8e21ff9de2fbbb811420e999dc955d`.
- **Méthode** : par simple lecture. `diff` du brouillon 1 au brouillon 3, puis du brouillon 3 au texte candidat. Comptage par un programme de lecture seule (citation, blocs « ancien »). `git show origin/main:registres/go.md`, filtré sur la seule ligne `GO-2026-11-18-64`. `git rev-parse` de la branche des sorties, nom seulement. Aucune garde jouée, aucun fichier de résultat ouvert.

## Conclusion

**Scellable après corrections mineures** : d1 à d3 ci-dessous, et elles seules.

Constats : 0 majeur, 3 mineurs, 7 notes.

## 1. Constats

### Mineurs

**d1 — Le troisième point de la preuve après coup (A3) n'est pas épinglé, et il lit la décision sans la tenir à la lettre.**

*Ce que dit la décision.* GO-2026-11-18-64 veut les « empreintes des fichiers de scores et de sondes égales à celles de `SCORES-BBIS` ». La ligne `SCORES-BBIS` ne porte qu'une empreinte, celle de `sondes-bbis.json`. Les empreintes des fichiers de scores et de sondes sont consignées **dans** ce fichier. À la lettre, il faudrait donc décoder `sondes-bbis.json`, une sortie de la course.

*Ce que fait le brouillon.* Il compare plutôt chaque fichier des dossiers de la course à « la tête de la branche des sorties de la course ». Cela tient le but (rien de modifié, rien d'ajouté, aucun voisin). C'est même plus large, puisque tous les fichiers sont couverts. Mais c'est une lecture des mots de Lazar, que le brouillon laisse ouverte au point 7. Deux défauts :
- la « tête » d'une branche peut bouger : la référence doit être le commit, nommé ;
- le lien entre ce commit et la ligne `SCORES-BBIS` n'est pas exigé.

Le reste de l'équivalence n'est pas vérifié par la preuve : que les fichiers de ce commit soient ceux que `sondes-bbis.json` consigne. La lecture elle-même le contrôle à l'ouverture (T, l. 85 : empreinte d'un fichier de scores différente → « non calculable »). Il n'y a donc pas de relance à tort, mais la lettre n'est pas tenue.

**Corrections exactes :**
- **Point (A3) du « Programme de la preuve après coup ».** Remplacer « a les octets du même fichier à la tête de la branche des sorties de la course (empreintes comparées, compagnons compris) ; la liste des noms de ces dossiers est celle de cette tête, » par « a les octets du même fichier au commit `7322049dbbc10975ec1fa7dd54c10c8bc1ec4cf9` de la branche des sorties de la course (`donnees/t07-etape-b-bis-v2`, tête relevée par les règles communes de la lecture), où le script vérifie que `sondes-bbis.json` a l'empreinte de la ligne `SCORES-BBIS` (empreintes comparées, compagnons compris) ; la liste des noms de ces dossiers est celle de ce commit, ».
- **Même point.** Remplacer « l'égalité est établie contre le commit des sorties auquel appartient le fichier que `SCORES-BBIS` cite (point ouvert 7). » par « l'égalité est établie contre ce commit, lié à la ligne `SCORES-BBIS` par l'empreinte de `sondes-bbis.json` ; c'est une lecture des mots « égales à celles de `SCORES-BBIS` », portée à Lazar (point ouvert 7). »
- **Point ouvert 7.** Remplacer la dernière phrase (« La mère ou le contre-lecteur du script dit si cela tient les mots de la décision (« égales à celles de `SCORES-BBIS` »). ») par « Nœud de Lazar : cette lecture remplace, pour les fichiers de scores et de sondes, les empreintes que consigne `sondes-bbis.json` par celles du commit des sorties lié à `SCORES-BBIS`. La voie de l'arrêt avant le seuil n'est pas employée avant son mot. Non bloquant pour le scellement : la voie de GO-2026-11-18-60 n'en dépend pas. »

**d2 — Le deuxième point de la preuve après coup (A2) contredit l'absence de borne quand les deux voies se succèdent.**
- **Le constat.** « Aucun fichier nommé `lecture-bbis.json`, aucun fichier nommé `preuve-aucune-ouverture-bbis.json` », sur le disque et dans toutes les références. Après une relance de la première voie (GO-2026-11-18-60), ces deux fichiers existent et sont commités, gardés et jamais retirés (« La suite », points 1 et 4). Un arrêt avant le seuil lors d'une relance suivante ne pourrait donc jamais être prouvé, alors que GO-2026-11-18-64 vaut « sans limite » et « pour les deux voies ».
- **Correction exacte.** Remplacer « aucun fichier nommé `lecture-bbis.json`, aucun fichier nommé `preuve-aucune-ouverture-bbis.json` ; » par « aucun fichier nommé `lecture-bbis.json` ni `preuve-aucune-ouverture-bbis.json` hors de ceux que citent, par chemin et empreinte, les lignes `PANNE-MISE-EN-PLACE-BBIS-<n>` déjà inscrites, chacun à l'empreinte citée ; ».

**d3 — Une sortie qui porte la ligne du seuil consomme la lecture : ce n'est pas un nœud.**
- **Le constat.** La règle « Arrêt avant le seuil » range « une sortie qui porte la ligne du seuil » parmi les cas qui donnent « nœud pour Lazar ». Le point 3 de « La suite » (correction c3) et GO-2026-11-18-64 disent pourtant que tout arrêt après la première ouverture consomme la lecture.
- **Corrections exactes :**
  - Remplacer « **Si cette preuve ne peut pas être faite — un point en défaut, une sortie non gardée, une sortie qui porte la ligne du seuil — il n'y a pas de relance (la décision ne la permet que sur cette preuve) : nœud pour Lazar.** » par « **Une sortie non gardée, ou une sortie qui porte la ligne du seuil : la lecture est consommée, aucune relance (point 3 de « La suite » ; GO-2026-11-18-64). Un point (A1) à (A3) en défaut, ou une preuve qui ne peut pas être faite : aucune relance, nœud pour Lazar.** »
  - Au paragraphe du script, remplacer « Non conforme, ou non faisable : nœud pour Lazar, aucune relance. » par « Une sortie absente ou portant la ligne du seuil : lecture consommée. Un point (A1) à (A3) non conforme, ou non faisable : nœud pour Lazar, aucune relance. »

### Notes

**n1 — Les corrections c1 à c6 sont toutes portées, mot pour mot, aux places dites** :
- c1 : point (c) de la différence D7, (O2), règle « Tout arrêt », § 4 point 2, essais 2 et 4, dernier tiret de D7, § 7 point 5, § 8 ;
- c2 : § 4, « Elle établit » ;
- c3 : point 3 de « La suite » et réserve R-RELANCE ;
- c4 : (M3), liste « N'en sont pas », essais 1 et 3 ;
- c5 : point 4 de « La suite » et § 4 point 4 ;
- c6 : bloc « nouveau » de CQ-1.

**n2 — Les ajouts « qui en découlent » sont justes.**
- c1, § 4 « Elle établit » : « qu'elle n'a pas imprimé la ligne `BBIS LECTURE ENTREES OUVERTES` » remplace « qu'elle n'a pas passé la garde ».
- c4, différence D7, point (a) : « commit nommé absent d'un dépôt superficiel ».

Les deux suivent la correction, sans plus.

**n3 — Les deux décisions de Lazar.**
- GO-2026-11-18-64 (registre `go.md` sur `main`, l. 428) est citée mot pour mot, comme mot de Lazar : la quatrième colonne de la ligne figure telle quelle dans le brouillon 3.
- Les réponses (1) et (2) de la mère et le désaccord de classement sont sortis du texte. Ils n'en restent que l'histoire, dans l'en-tête (brouillons 2 et 3), et la mention de la borne levée, qui est dans la ligne de Lazar.
- La réponse (3) de la mère (clés admises, R-RELANCE et pièce acceptées) reste, comme donnée d'organisation.
- Aucune borne de relances. Rien ne va au-delà de GO-2026-11-18-60 et de GO-2026-11-18-64, sous d1 à d3 qui resserrent.

**n4 — « Avant la garde » se lit « avant le seuil ».** Cette lecture est déclarée (§ 1) et cohérente avec « tout arrêt après la première ouverture consomme la lecture ». Elle range, parmi les arrêts relançables, ceux du bloc de la garde avant la l. 1255, dont une clé de B bis dans le registre partagé. Ce n'est pas une voie de fuite, pour deux raisons :
- une correction qui touche un registre n'est pas une pure mise en place (point 2 de « La suite » : arrêt, nœud) ;
- la garde est rejouée entière à chaque relance, et tout défaut de fond persistant y refuse de nouveau.

**n5 — Le cas qui ferait rejouer à tort une lecture, ou choisir une issue : aucun trouvé, sous d1 à d3.**
- Aucune relance ne suit une ouverture : c1, c3, et la ligne du seuil vérifiée dans toutes les sorties gardées.
- Un refus de fond masqué par un arrêt avant l'écriture reparaît à la relance.
- Les tirages ne dépendent pas du nom du run (`Graines(entropie)`), et rien n'est connu avant la relance.

**n6 — Réserve R-RELANCE.** La phrase ajoutée (« un état du disque et de l'histoire, non l'absence de toute lecture ») et le § 4, point 6 disent honnêtement ce que la preuve après coup n'établit pas : des empreintes égales ne disent pas que rien n'a été lu.

**n7 — Texte candidat, blocs « ancien », ligne de registre.**
- Le texte candidat ne diffère du brouillon 3 que par le titre et le statut. Le statut sans heure écrite est acceptable : il renvoie à la ligne `ADDENDUM-ECART-4-COMPLEMENT-BBIS`, forme déjà admise pour le quatrième addendum. Il cite GO-2026-11-18-60 et GO-2026-11-18-64, le brouillon 3 et mon rapport.
- Les six blocs « ancien » sont exacts et uniques dans le quatrième addendum scellé (comptage : 1 chacun).
- La ligne de registre proposée est au format à cinq colonnes du registre voisin.

## 2. Points ouverts du complément

| point | statut |
|---|---|
| 1. arrêt avant le seuil, sans rien écrire | couvert par la décision de Lazar (GO-2026-11-18-64) ; clos |
| 2. nombre de relances | couvert par la décision de Lazar (GO-2026-11-18-64 : sans limite) ; clos |
| 3. clés neuves au registre voisin | question d'organisation pour la mère, admises (réponse (3)) ; clos |
| 4. lettre « écrite dans le quatrième addendum » | question d'organisation pour la mère, forme admise ; clos |
| 5. code de sortie 3, lignes imprimées, sortie de chaque lancement gardée | question d'organisation pour la mère (commande, mandat du lecteur-opérateur) |
| 6. contre-lecture | faite (brouillon 1 et ce rapport, qui couvre les passages nés de GO-2026-11-18-64) |
| 7. lecture de « égales à celles de `SCORES-BBIS` » dans (A3) | **nœud de Lazar** (d1) ; non bloquant pour le scellement, la voie de l'arrêt avant le seuil restant fermée avant son mot |

## 3. Fichiers ouverts

- Les brouillons 1, 2 et 3 du complément et le texte candidat, par `diff` et comptage.
- Les deux listes de différences : empreintes seulement.
- Le quatrième addendum scellé : comptage des blocs « ancien ».
- Sur `origin/main`, la seule ligne `GO-2026-11-18-64` de `registres/go.md`.
- Le nom du commit de tête de `origin/donnees/t07-etape-b-bis-v2`, par `git rev-parse`, sans rien ouvrir de la branche.

**Fichiers de résultat** : aucun, ni à l'œil ni par la chaîne.

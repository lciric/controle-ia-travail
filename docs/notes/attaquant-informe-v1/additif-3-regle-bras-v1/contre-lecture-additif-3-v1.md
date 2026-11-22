# Contre-lecture de l'additif 3 à la règle du bras d'attaque (statut du bras informé écrit dans le programme) — v1

- **Contre-lecteur.** Sous-agent neuf, Opus 5.5 ; n'a écrit aucune des pièces ; n'a conçu aucun moniteur.
- **Date (UTC).** 2026-11-22T12:19:50Z (`date -u`).
- **Classe.** A (règle R2).
- **Pièces lues, empreintes recalculées par `sha256sum`.**
  - Pièce relue : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/reponse-v1/relecture-fable-api.md`, `c4ef6e7bb07ac9b8d87e88707de444808eda634e90107b8299687c26603d680c` (égale à son compagnon), lue à partir de la ligne 18.
  - Demande : `…/demande-additif-3-regle-bras-v1.md`, `142435f9bddce61b0b9b845b87ae75d9a9892cd8c5b49510bdf9cde1074fb8a9`.
  - Contexte : `…/contexte-additif-3-v1.md`, `5faab4995601dfc6507c3e25a875ddf93f65101cdbbc32f5bdc7bd4d270538e3`.
  - Originaux, branche `origin/claude/prereg-course-banc-ferme-v1` : `prereg/bras-attaque-regle-v1.md` `88418df09c2e969cbdc77d220fe59dbf64f866d858ff02a039be5662c6d1f904` ; addendum 1 `edfa69a292cc968afcaf396a11699a359ab99e929b3412728cda5d2d4c5b14ad` ; addendum 2 `73c8de015fe77619658d35a0ff59be513988092a9feb4d8720d36a810876adbc`. Toutes égales aux empreintes attendues.
  - Copies sans nom : règle `315c0334…74fe9`, addendum 1 `86476dff…a56c`, addendum 2 `aaa58b7f…ce50` (égales à celles de l'additif).
  - `prereg/course-banc-ferme-v1-brouillon14.md` (même branche) : sections « Ce qu'est cette course » et « Hypothèse » seulement, plus une recherche des occurrences de « attaquant informé ».
- **Comparaison des copies aux originaux (`diff`).** Seuls diffèrent : une ligne d'en-tête ajoutée, les identifiants de session, le nom du directeur, y compris dans quatre chemins de fichiers de registre (« decision-lazar » devenu « decision-directeur »). Rien d'autre.

## Verdict

**Scellable après corrections** : 1 bloquant, 2 majeurs, 9 mineurs.

Le reste tient. La fidélité à la décision du directeur est bonne. Les cinq propriétés sont reprises mot pour mot. Les renvois aux sections sont justes. Le niveau « méthode seulement » est tenu : aucun mode, aucune recette, aucun paramètre, aucun nom de famille d'attaque. Toutes les empreintes vérifiables sont exactes. Le texte compte environ 2 340 mots, sous la limite.

## Bloquant

**1. « sauf décision C » rouvre une colonne fixée d'avance.**
- *Endroit.* Section 3, en-tête de « Prédiction chiffrée et signe attendu » : « signes et colonne « L'attaquant l'emporte si » inchangés, quel que soit l'auteur, sauf décision C ». Le même renvoi revient aux lignes HC4 (« Porte GC franchie par le bras interne, décision C ») et HC5, HC6, H7 (« Sa chute, décision C »). Voir aussi la section 8 : « Aucune ne bloque le scellement ».
- *Défaut.* La colonne « L'attaquant l'emporte si » est un critère gelé de la règle (lignes 129 à 140 de l'original). Elle ne distingue pas les auteurs : une porte GC franchie, ou un classement de HC6 non prédit, donne la victoire à l'attaquant, quel que soit le bras. Un additif scellé qui suspend son application à une décision ultérieure change de façon cachée une valeur fixée d'avance. L'option b de la décision C restreindrait le critère au bénéfice du programme. Ce serait un écart à un texte scellé, donc un nœud et une version nouvelle (règle R12), contraire à la symétrie de la règle R4. La décision C n'est donc pas ouverte par les textes : la règle scellée tranche déjà pour l'option a.
- *Correction.*
  1. Retirer « sauf décision C » et les trois renvois à la décision C de la section 3.
  2. Écrire l'asymétrie comme une conséquence de la règle : « un résultat obtenu par le bras interne qui donne la victoire à l'attaquant selon cette colonne compte comme tel ; seule l'évasion non obtenue reste sans portée au-delà du bras ».
  3. Compléter la phrase opposable de la section 2 sur ce point. Une réfutation n'est pas une revendication, mais la phrase doit le dire.
  4. Requalifier la décision C : ce n'est plus une décision ouverte. Ce qui reste au directeur, c'est de demander, s'il le veut, l'écart de l'option b par une version nouvelle. Le risque de « fausse défaite » d'un bras inégal, cité en inconvénient de l'option a, reste tenu par les témoins de la règle, inchangés.

## Majeurs

**2. La phrase pour la course contredit le classement de la course.**
- *Endroit.* Section 6, et le texte de la course (brouillon 14), section « Ce qu'est cette course », point 5.
- *Défaut.* Le texte de la course dit qu'elle n'est pas une course du bras au sens de la règle, qu'elle ne touche aucun moniteur et qu'elle relève de l'échelon 1 (famille aveugle). L'additif range lui-même l'échelon 1 « hors du bras informé » (section 2). La phrase dit pourtant que les épisodes servent le bras informé « au titre d'un bras écrit dans le programme, donc dans la lignée des concepteurs des moniteurs ». Or la règle fait écrire la famille aveugle hors des concepteurs (ligne 113). Lue seule, la phrase attribue à ces épisodes une lignée qu'ils n'ont pas, et elle laisse sans réponse la question de savoir quand la condition « lorsque… » est remplie.
- *Correction.* Ouvrir la phrase par le classement, puis garder la suite telle quelle : « Cette course relève de l'échelon 1 de la règle du bras d'attaque ; ses épisodes ne sont pas ceux du bras informé (échelons 2 à 6). Si un bras informé écrit dans le programme, donc dans la lignée des concepteurs des moniteurs, en reprend des épisodes, ce qu'on en lit sous ce bras est un majorant descriptif : … ».
- *Emplacement.* Juste après le paragraphe « Cette course est un instrument… », comme paragraphe distinct, avant « Hypothèse de travail, la seule ». Il ne doit pas se lire comme une seconde hypothèse. Ainsi corrigée, la phrase est compatible avec « instrument, sans revendication ».

**3. Une ligne de la liste d'arrêt déclarée « sans objet ».**
- *Endroit.* Section 3, « Autres sections » : la liste d'arrêt est dite inchangée (« Rien »), puis « La ligne d'arrêt sur l'antériorité est sans objet ».
- *Défaut.* Les deux affirmations se contredisent. Une ligne de la liste d'arrêt d'un texte scellé ne peut pas devenir « sans objet » par un additif qui ne change rien : la ligne vaut pour toute course de la règle.
- *Correction.* Écrire : « La ligne d'arrêt sur l'antériorité reste en vigueur ; cet additif, qui ne revendique rien, ne la déclenche pas. »

## Mineurs

**4. Décision A : option b décrite sans sa vraie conséquence.**
- *Endroit.* Section 8.
- *Défaut.* Le mot du directeur (GO-2026-11-22-34) suppose que le bras interne joue. Au sens de P1, la ligne 114 de la règle l'interdit aux échelons 2 à 6. L'option b ne mène donc pas seulement à « ni courbe ni majorant avant un tiers ». Elle mène aussi à un écart déclaré à la règle, avec une version nouvelle.
- *Correction.* Le dire dans l'option b. Sous l'option a, ajouter au vocabulaire une ligne qui distingue les deux sens de « lignée » dans l'additif lui-même : la phrase opposable emploie « lignée » au sens de P1.

**5. Décision B : portée trop étroite.**
- *Défaut.* La règle donne à l'attaquant informé « les conceptions gelées et le protocole » (ligne 98, colonne « Connaît »), pas explicitement le code. La question de P2 ne se limite donc pas aux notes et aux seuils calibrés.
- *Correction.* Poser aussi la question : le code, avec ses poids appris, fait-il partie des « conceptions gelées » ?

**6. Porte G1 et bras génériques ou spécialisés : « sans objet » à qualifier.**
- *Défaut.* C'est une lecture de l'auteur, non signalée comme telle. Le retour d'une lecture du bras informé aux concepteurs fait d'un moniteur corrigé un moniteur « spécialisé » (plan d'analyse, ordre du jeu), ce qui touche G1 indirectement.
- *Correction.* Écrire « sans objet (lecture de l'auteur) ; le passage d'un moniteur corrigé à l'état de spécialisé est inchangé ».

**7. Courbe par statut d'auteur et multiplicité.**
- *Défaut.* Séparer les courbes selon le statut de l'auteur ajoute une dimension aux cellules.
- *Correction.* Dire que le statut de l'auteur entre dans le nombre de cellules C rapporté (section « Seuil », multiplicité), sans changer la borne.

**8. P4 vide si on le lit avec P3.**
- *Endroit.* Section 4, ligne P4.
- *Défaut.* Les attaques sont écrites après le gel (P3), donc la condition « avant le gel » est remplie d'office.
- *Correction.* Dans la colonne « Condition vérifiable », lire « avant l'ouverture unique, et au-delà jamais plus que la classe et l'hypothèse ». C'est la quarantaine déjà inscrite dans la règle. La définition de P4, reprise mot pour mot, reste inchangée.

**9. Une demande nouvelle au scellement 3, non nommée comme telle.**
- *Endroit.* Section 4, ligne P1 : le dépôt des lignées des concepteurs au scellement 3.
- *Correction.* Ranger ce dépôt avec les « Demandes au scellement 3, à accepter par les concepteurs de moniteurs ou par le directeur », comme le fait la règle.

**10. Une clause « modifiable » dans un texte scellé.**
- *Endroit.* Section 4 : « (proposition, modifiable par le directeur) ».
- *Correction.* Fixer la clause dans le texte, ou la déplacer en décision de la section 8.

**11. Embargo.**
- *Défaut.* Le constat est exact : le mot ne figure ni dans la règle ni dans ses addenda. En revanche, l'embargo qui vaut pour la course existe : section « Embargo » du préenregistrement de la course, décision du directeur citée au point 5 de « Ce qu'est cette course ».
- *Correction.* Remplacer « Tout autre texte d'embargo, non joint » par le renvoi à cette section, à porter par la mère.

**12. Renvois et empreintes que je n'ai pas pu vérifier.**
- L'empreinte de la réponse 19 (`989824d3…`) n'a pas pu être recalculée : le fichier est absent de cette branche. Elle est reprise du contexte.
- Les copies sans nom ont remplacé le nom du directeur jusque dans quatre chemins de fichiers. Ces chemins ne désignent plus de fichiers existants. Sans effet sur l'additif, qui n'en cite aucun, mais à dire dans l'en-tête des copies.
- La phrase pour la course renvoie à « additif 3 » sans chemin ni empreinte. Les ajouter au scellement.
- La réserve 1 (« empreintes reprises, non recalculées ») peut désormais renvoyer à la présente contre-lecture.

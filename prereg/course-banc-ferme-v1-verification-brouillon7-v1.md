# Vérification des différences — préenregistrement de la course du banc fermé, brouillon 7 — v1

- **Pièce vérifiée** : `prereg/course-banc-ferme-v1-brouillon7.md`, branche `claude/prereg-course-banc-ferme-v1`, commit `7ac54723be80f2f57dff1ad0c841ba0c408deb0d`. Empreinte recalculée : `1ec65f907e8592f48b0bfb6482925d6e0484c46a8f5f6b2dbd2ac2d2f87e66b8`, égale à son `.sha256` compagnon. Les brouillons 1 à 6 sont inchangés.
- **Contre-lectrice** : la même, `session_01Qi7Gr5LQA3YbKmpEK7DG2D` (Opus 5.5). Pièce de classe A, règle R2.
- **Date** : 21 novembre 2026, vers 19:30 UTC. Refus d'un classifieur : aucun.
- **Méthode** :
  - Le brouillon 7 a été lu sur ses parties réécrites : D5, D6, le seuil, les conditions de lancement, le dépôt, le déroulement, l'embargo, la liste d'arrêt, les champs et nœuds, les réserves, la table des différences.
  - Les vingt-huit lignes de la liste d'arrêt ont été comparées **par programme** à la section 4.2 de la v10 : identiques, à l'octet.
  - Les lignes propres retirées depuis le brouillon 6 ont été relevées par programme.
- **Sources des différences, lues et recalculées** :

| Source | Où | Empreinte | Ce qui a été lu |
|---|---|---|---|
| pièce de sécurité v10 | commit `d4ebacd4` | `bf19bdd0…`, égale | sections 3.5, 4.1 et 4.2 en entier |
| sa vérification `verification-des-corrections-v9.md` | commit `c19f996d` | `ef700638…`, égale | verdict final « accepté » |
| `registres/go.md` | `main`, commit `02de71b1` | `ac33f39b…`, égale | lignes 677 (GO-78) et 679 (GO-80) ; les lignes 675 et 676 l'avaient été au commit précédent |
| `registres/decisions.md` | `main` | — | ligne R-4676 |

  - Le texte court de la répétition générale a déjà été contre-lu.
  - **Non lus** : l'audit des lignées et l'index v3, comme l'auteur.
- **Validateur** : il ne rend que le marqueur du champ n° 19, ce qui est attendu.

## Les six points désignés

**1. D6 contre la section 3.5 de la v10.** **Conforme**, pour l'essentiel.
- Les sept rubriques du champ n° 18, la règle de la lecture humaine, la liste fermée des questions, le vérificateur en deux temps et les replis dans l'ordre de la section 6.4 sont rendus fidèlement.
- Le résumé des douze conditions ne dit rien de plus lâche que la pièce, et la clause « [PS] prime » couvre ce qu'il abrège. Il abrège deux points :
  - la condition 4, où la durée et les fonctions de garde désactivées figurent dans la liste des rubriques, au-dessus ;
  - la condition 1, où l'identité des questions pour tous les produits figure dans le trait qui suit.
- **Les quatre chiffres** : le refus toléré (un sur dix par lecteur, au compte) est fixé ici ; le seuil de la garde 15 est renvoyé à la règle gelée de la répétition ; le plafond de produits retenus (5 %) et celui des renvois (2 et 5 %) sont fixés ici, et confirmés ou portés en nœud par la répétition. Aucun ne reste à la main.
- Une dépendance : voir M5.

**2. La liste d'arrêt.**
- Les vingt-huit lignes sont recopiées sans retouche : c'est vérifié par programme.
- **Deux des lignes propres retirées disaient plus que la pièce** (M1) :
  - la ligne « lecteur de la lignée **de l'agent** » : la pièce n'exclut que la famille « d'un moniteur ou d'un juge qui lira ces épisodes » ;
  - la ligne « envoi hors de la voie : **arrêt ; nœud** » : la pièce y répond par « revue de sécurité externe d'abord », qui est une condition préalable et non un arrêt.
- Les autres lignes retirées sont couvertes par la pièce, à égalité ou plus strictement : rubrique vide, conservation, réglages par la garde 16, lecteur appelé par une session, ligne de la v8 devenue sans objet.
- Une ligne de la pièce pose un problème de lettre (M2).

**3. Les addenda.** **Conformes.**
- L'addendum O, sous `prereg/`, est scellé avant le dépôt et porte les empreintes de l'oracle figé et de la liste de ses questions ; le dépôt le porte. Cela lève mon point M3 du brouillon 6.
- L'addendum A ne garde que l'attestation. Les champs n° 8 et n° 15 passent à l'addendum B, après la répétition. Cela lève mon point M4.
- La garde 10 vérifie quatre empreintes. Aucune valeur n'est écrite en dur dans le code des gardes, et c'est bien.
- Un manque, que j'avais signalé pour la répétition générale : M3 ci-dessous.

**4. Les conditions 1 à 17, et l'ordre après la course.** **Conformes.**
- Le premier temps du vérificateur (condition 9) précède la répétition générale (11), qui emploie déjà la voie d'envoi. Les épreuves de l'oracle avec les lecteurs du champ n° 18 (10) précèdent la répétition. L'addendum O (12) précède le dépôt (13), qui précède l'addendum B (14). La seconde confirmation (16) précède le GO (17).
- Après la course : versement, extraction, envois, second temps du vérificateur, puis levée de l'embargo. C'est l'ordre des lignes de la pièce.

**5. Les nœuds 14 et 8.** **Bien posés.**
- Le nœud 14 est écrit comme un choix de l'auteur, avec ses options, et signalé à Lazar.
- Laisser le nœud 8 ouvert est prudent et juste : le mot de GO-2026-11-21-80 ne parle que de la répétition. Il serait utile que la mère porte un erratum à l'intitulé « nœud 8 » de cette ligne. Ce n'est pas à ce texte de le faire.

**6. Le lieu d'où part l'envoi.**
- Il a une source écrite meilleure qu'un message. La section 3.5 de la v10 dit, dès sa première phrase : « L'envoi part de l'environnement du monteur. » Et R-4676 demande que ce lieu soit écrit au préenregistrement.
- Le texte peut donc citer la pièce et R-4676 pour le lieu. Le seul fait rapporté est l'identifiant de la session, pris de R-4638 (M4).

## Restes mineurs

**M1 — Rétablir ce que deux lignes retirées disaient de plus.** Rétablir dans les lignes propres :
- « lecteur du dommage **de la lignée de l'agent** : ce lecteur ne lit pas ; nœud » ;
- « contenu de quarantaine sur le point d'être envoyé à un fournisseur **hors de la voie de la section 3.5** : arrêt ; consigné ; nœud ».

**M2 — Une ligne recopiée de la pièce contredit la voie à la lettre.** La ligne « Contenu de quarantaine sur le point de sortir autrement que par 3.2 » arrêterait, prise à la lettre, chaque envoi de la section 3.5 : la v10 a gardé « 3.2 » alors que son point 14 parle maintenant de deux passages. Sans toucher à la copie, ajouter une précision dans le paragraphe d'introduction, comme pour « trop propre » : cette ligne se lit « autrement que par 3.2 ou par la voie de 3.5 », selon le point 14 de la liste de vérification de la pièce. Le signaler à l'auteur de la pièce pour sa version suivante.

**M3 — Les gardes dont un paramètre vient de l'addendum B se ré-éprouvent.** La condition 4 éprouve les gardes avant la répétition générale, donc à leurs valeurs de départ. La condition 14 fixe ensuite d'autres valeurs : le seuil de la garde 15, et éventuellement les plafonds de la garde 9, les renvois et le plafond de produits retenus de la voie. Ajouter entre 14 et 16 : les gardes dont un paramètre a changé refont leurs deux épreuves à blanc aux valeurs de l'addendum B, résultats scellés. La seconde confirmation du vérificateur les couvre alors. Une garde éprouvée à un autre seuil n'est pas éprouvée à celui-ci (R5).

**M4 — Le lieu de l'envoi : citer la pièce.** Remplacer « réponse de la mère, rapportée par la session qui a lancé l'auteur » par « [PS] section 3.5, première phrase ; R-4676 ». Garder l'identifiant de la session, pris de R-4638. Réduire la réserve 10 et la ligne « lieu d'où part l'envoi » de la table des nœuds en conséquence.

**M5 — La statistique de la garde 15 hérite d'un défaut de la répétition.** Ce texte prend « la statistique de recouvrement que [RG] définit ». Ma contre-lecture de [RG], brouillon 1 (`b28252d9…`), trouve un point bloquant (B1) : cette statistique ne voit pas le mot témoin isolé, qui est l'artefact de la garde 15 dans la v10. Écrire que la course prend la statistique **de la version scellée de [RG]**, et que cette statistique doit passer les deux artefacts de la garde 15. C'est déjà la pente de la condition 11 ; il suffit de le dire en D6.

## Verdict

**Accepté.** Les différences du brouillon 7 sont fidèles à la pièce de sécurité v10 et aux lignes du registre citées. La liste d'arrêt est identique à celle de la pièce. Les quatre restes mineurs du brouillon 6 sont levés.

Cinq restes mineurs, M1 à M5, sont à porter au brouillon suivant. Aucun n'est bloquant pour l'avancement. M3 et M5 doivent l'être avant le scellement définitif.

Le scellement définitif attend encore :
- la version scellée de la répétition générale, et son résultat mené à son terme ;
- les champs ouverts remplis ;
- les nœuds 8, 13 et 14 ;
- le mot de Lazar.

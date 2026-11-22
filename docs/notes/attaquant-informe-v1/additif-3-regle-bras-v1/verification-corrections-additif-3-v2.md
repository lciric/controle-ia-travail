# Vérification des corrections de l'additif 3 à la règle du bras d'attaque, version 2

- **Vérificateur.** Le contre-lecteur de la version 1 (Opus 5.5), sous-agent neuf ; il n'a écrit aucune des pièces. Classe A.
- **Date (UTC).** 2026-11-22T12:30:32Z (`date -u`).
- **Empreintes recalculées par `sha256sum`.**
  - Version 2 de l'additif, lue à partir de son titre : `docs/notes/attaquant-informe-v1/additif-3-regle-bras-v1/reponse-v2/relecture-fable-api.md`, `5fbdef7c20213970cbf695ea02bd53bd303a427337107c3b594c8f43c8bda1f8`, égale à son compagnon.
  - Version 1 de l'additif : `…/reponse-v1/relecture-fable-api.md`, `c4ef6e7b…680c`.
  - Mon rapport sur la version 1 : `…/contre-lecture-additif-3-v1.md`, `6e187f82…0292`. Sa copie sans nom : `9e837374…3ac7`.
  - Extraits de la course : `…/copies-sans-nom-v1/course-brouillon14-extraits-copie-sans-nom-v1.md`, `c81a6b09…4eb9`.
  - Original de la course : `prereg/course-banc-ferme-v1-brouillon14.md`, branche `origin/claude/prereg-course-banc-ferme-v1`, `4489d399…3784`, égal à l'empreinte que la version 2 déclare.
  - Règle et addenda : empreintes de la version 1 inchangées (88418df0…, edfa69a2…, 73c8de01…).
- **Méthode.** Comparaison par `diff` des deux versions de l'additif, de son titre à « Fin de l'additif ». Chaque différence a été confrontée au texte de la règle et aux extraits de la course.

## Verdict

**Accepté avec mineurs résiduels.** Le bloquant et les deux majeurs sont levés. Aucune différence nouvelle ne change une hypothèse, un signe, un seuil ou une valeur fixée d'avance. Les trois mineurs résiduels se corrigent par erratum ou par la mère.

## Point par point

| Point | Classe en v1 | Traitement déclaré | Jugement |
|---|---|---|---|
| 1. « sauf décision C » | bloquant | appliqué | **Levé.** « Sauf décision C » est retiré. L'asymétrie est écrite comme conséquence de la règle (sections 2, 3 et 5), avec « lu selon la règle, témoins tenus », conforme aux critères gelés. La décision C devient un constat. L'ajout sur la portée des témoins (« un témoin par mode, non par moniteur ») est exact : la règle dit « un témoin par mode lu ». C'est une réserve, sans changement de critère. |
| 2. Phrase pour la course | majeur | appliqué autrement | **Accepté.** La phrase devient le point 7 de « Ce qu'est cette course, et ce qu'elle n'est pas ». Elle ouvre sur l'échelon 1. Chacune de ses affirmations se vérifie : sur les extraits (points 3, 4 et 5, section « Embargo ») et sur la règle (« Qui lit quoi » : l'attaquant informé ne lit jamais les familles aveugles ni les épisodes d'épreuve). Retirer la condition « si un bras informé en reprend des épisodes » est plus juste que ma correction, puisque cette reprise est interdite. La phrase tient seule, car « [PR] » est défini dans la table de la course. Elle sort de la section « Hypothèse » et reste compatible avec « instrument, sans revendication ». |
| 3. Ligne d'arrêt sur l'antériorité | majeur | appliqué | **Levé.** Le texte dit maintenant que la ligne reste en vigueur et que l'additif ne la déclenche pas. |
| 4. Décision A | mineur | appliqué | **Levé.** L'option b dit désormais qu'elle mène à un écart déclaré et à une version nouvelle. Le vocabulaire fixe « lignée » au sens de P1. |
| 5. Décision B | mineur | appliqué | **Levé.** Les deux questions sont posées, et la question du code passe en premier. |
| 6. Porte G1 | mineur | appliqué | **Levé.** |
| 7. Multiplicité | mineur | appliqué autrement | **Accepté.** Le nombre de cellules se rapporte par course. Le statut n'ajoute des cellules que si une même course lit deux statuts. La borne par cellule est inchangée. |
| 8. P4 | mineur | appliqué | **Levé.** La condition porte « avant l'ouverture unique », puis la quarantaine. La définition de P4 est gardée telle quelle. |
| 9. Demande au scellement 3 | mineur | appliqué | **Levé.** |
| 10. Clause « modifiable » | mineur | appliqué | **Levé.** La clause est fixée, et la désignation du lecteur passe en décision D. |
| 11. Embargo | mineur | appliqué | **Levé.** « Un tiers auteur n'est pas sur la liste fermée des destinataires » est exact selon l'extrait. |
| 12. Renvois et empreintes | mineur | appliqué autrement | **Accepté.** L'en-tête des copies relève de la mère, et la réserve 1 le lui signale. Le chemin et l'empreinte de l'additif sont réservés dans la phrase pour la course. L'empreinte de la réponse 19 reste non recalculée, et c'est dit. |

## Différences absentes de la table

Aucune ne change une hypothèse, un signe, un seuil ou une valeur fixée d'avance.

- **Ajouts conformes à la correction 1.** « « Cassé » et « entamé » valent quel que soit l'auteur » (définition de travail). « La colonne… appliquée telle quelle à tout bras » (section 5).
- **Reformulations sans effet.** La phrase sur l'évasion observée est déplacée dans le paragraphe de l'asymétrie. « Majorant descriptif » est retiré de la ligne de la pince, qui garde la même règle de rapport. « Et sa revendication le dit » est retiré pour le catalogue de l'échelon 3. L'en-tête de contre-lecture est mis à jour.
- **Mineur résiduel R1 : le glissement du calendrier.** La mention « Glissement du calendrier, sans objet » a disparu de la ligne du risque « élicitation trop faible ». Or le sixième passage de la règle comprend ce glissement. Correction par erratum : rétablir la mention.

## Décision D

**Bien posée et réellement ouverte.** La règle ne dit pas qui constate des métadonnées. Le risque est faible.

**Mineur résiduel R2 : l'option a étend une ligne de « Qui lit quoi ».** Dans la règle, le lecteur neuf du verdict lit « la sortie scellée, les critères gelés ». L'option a lui ferait lire aussi des métadonnées. Correction : préciser dans l'option a que les métadonnées déposées sont jointes à la sortie scellée, ce qui laisse la ligne inchangée. Sinon, déclarer l'extension.

## Point nouveau

**Mineur résiduel R3 : la copie sans nom de mon rapport est fautive.** Elle a remplacé le nom aussi dans ma citation : « « decision-lazar » devenu « decision-directeur » » y devient « « decision-directeur » devenu « decision-directeur » », ce qui n'a plus de sens. Son en-tête dit pourtant « rien d'autre changé ». La version 2 a malgré tout repris le point correctement. Correction, à faire par la mère : dans les copies sans nom, ne pas remplacer le nom dans une citation de chemin, ou écrire « [nom retiré] ».

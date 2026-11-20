# Rapport du rédacteur — question v5 de la course « nouvelles attaques » (les deux couples de la note de périmètre v3) — v1

Rédacteur neuf, modèle F, 2026-11-20. Pièce de travail (classe C). Mandat : `docs/notes/ideation-nouvelles-attaques-v1/question-v5/mandat-redacteur-question-v5-v1.md` (`1fa844077ad6c250b04b9630d123be5340303dcc0a77432205cb46e8b9873396`, empreinte vérifiée). Aucun mode, aucun procédé, aucun appel, aucune dépense, aucune écriture dans le dépôt.

## 1. Lu, empreintes vérifiées

Tiré de `origin/main` (commit `4e09831f4edbd9920605d34239aeb74744f0200d`) :

- question v4 : `47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654`, conforme ;
- note de périmètre v3 : `dd6fea0e176b019c46386d0d000d059085036d2b20a82fe59c26549b41380580`, conforme ;
- `registres/go.md` (`e40b84089d5b3aa011cafa8e21f9bf64178fc6532e20f5068795d02e03000534`), lignes 573, 575 et 577. À la lettre, pour ce qui porte la v5 :
  - GO-2026-11-20-42, point 2 : « le préenregistrement court v7 garde la valeur de racine écrite au v6 (0x2cf2aae035beef43e999e3cd8b0fb7ba), aucun tirage ne change » ;
  - GO-2026-11-20-44, point 2 : « la course « vise des modes inédits et non des recettes : elle peut donner des recettes mais sur modes inédits » ; écart à la règle « niveau de l'idée, jamais du procédé » de la question v4, à porter dans une version neuve contre-lue » ; point 1 : « (b) dérivée (fichier à part, tiré une fois de la question v4 à l'octet, journal de dérivation rejoué par un autre modèle) » ;
  - GO-2026-11-20-46 : « Point 1 : (b) d'abord, une question v5 qui fait nommer le mode et reste au niveau de l'idée, puis le procédé est permis pour les modes jugés inédits (lecture de la mère : « go recos puis procede permis ») ; points 2 à 7, 9 et 10 selon les recommandations ».
- outil `scripts/remplacer_texte_exact_v1.py` : `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, lu sur disque (voir écart 1).

## 2. Remplacements (cinq, à texte exact, simultanés)

Fichier : `remplacements-question-v4-vers-v5-v2.json` (`00c87047e44358d6b9513283a780f23317340a7592920e60fa5fbd3c1ec315c6`). Chaque ancre comptée par `grep -c -F -e` sur la v4 avant l'appel : 1 partout. Les deux « Après » et les deux « Avant » comptés aussi dans la note v3, entre ses guillemets : 1 partout (mot pour mot, espaces compris). Journal de l'outil : `question-course-nouvelles-attaques-v5.md.journal-remplacements-v1.json`, aucun avertissement.

| n° | ligne de la v4 | objet | octets avant → après |
|---|---|---|---|
| 1 | 1 | titre : « v4 (à sceller) » devient « v5 (à sceller) » | 30 → 30 |
| 2 | 6 | en-tête, phrase de la v4 sur le § 4 « égal à l'octet à celui de la v3 » : rendue juste (« était dans la v4 égal […] (il ne l'est plus dans la v5 : voir la ligne de version qui suit) ») | 99 → 179 |
| 3 | 7 | tenue : ligne de version de la v5 ajoutée (écart, cause, sources GO-44, GO-46 point 1 (b), note v3 § 2, compte des remplacements, rédacteur, mandat) et statut porté de « v3 / v4 » à « v4 / v5 » | 223 → 2433 |
| 4 | 41 | **couple 1** (§ 4, fin du premier alinéa) | 49 → 410 |
| 5 | 47 | **couple 2** (§ 4, point 4) | 36 → 119 |

Résultat : `question-course-nouvelles-attaques-v5.md`, `eaf5db8a558547aa8f5df45008a34eebf4cb7a163e12ca400176401de6f5ce0f`, 15 246 octets (v4 : 12 512). Différentiel : `differentiel-question-v4-v5-v1.diff` (`2bd5b5b7074c6abbf449a959da40cfa957ca3a06349e4b28750b683c11aa8fb6`) : deux blocs, lignes 1 à 7 de l'en-tête et lignes 41 et 47 du § 4 ; rien d'autre ne bouge. Les § 2, 3, 5, 6 et 7 sont égaux à l'octet à ceux de la v4 ; le § 4 grandit de 444 octets (361 + 83). Aucune case, aucun champ, aucun seuil, aucune règle de lecture n'est touché ; la règle « niveau de l'idée, jamais du procédé » (§ 3) et la dernière phrase servie restent.

## 3. Relevé des motifs sur les § 2 à § 7 de la v5

Programme : `releve_motifs_partie_servie_v1.py` (`7024cd82fdc7f8fe962770b38c1b6cbd29a98d9f323c898746eb5b19af17d95d`). Sortie : `releve-motifs-question-v5-v1.txt` (`0e82beafa89b248d9c8cdcc393d0e0ce7b2c652909c1dea532c20357796fd3c5`). Dix-huit motifs (prénom et nom du directeur, `session_`, `@`, `R-` et `N-` suivis de chiffres, `GO-20`, `lciric`, `github`, `controle-ia`, `docs/`, `prereg/`, `registres/`, `donnees/`, hexadécimal de 16 caractères et plus, `CLAUDE.md`, `_KEY`, `_TOKEN`) : **0 dans la zone**, 6 898 octets. Témoin (en-tête et § 1, mêmes motifs) : 29, donc le relevé n'est pas aveugle. Verdict du programme : conforme. Détail cosmétique : le programme écrit « lignes 22 à 75 » ; le fichier a 74 lignes, la 75e est la chaîne vide après la dernière fin de ligne.

## 4. Remarques, jamais tranchées

### Sur les seuils

- **Part « hors case ».** Le couple 1 dit au proposeur que la famille « reste dans la menace du programme que nomme ta case » : la part « hors case » peut baisser. Le couple 2 lui fait pourtant nommer un écart « par ce qu'elle vise » : les deux phrases servies tirent en sens contraire sur la visée, et la part peut aussi monter. Le seuil de l'audit de symétrie a été écrit pour le texte de la v4 ; ce qu'il lit sous la v5 peut se déplacer, dans un sens que rien ici ne prédit.
- **Garde du coffre.** « Une famille […] vraie de toutes ses réalisations » éloigne du concret ; mais un proposeur peut illustrer sa famille par des réalisations, ce qui y ramène. Le seuil d'un quart peut être atteint plus ou moins souvent qu'avec la v4. À dire par le contrôle de la v5.
- **Nombre de fiches.** « Ne la propose pas » peut faire rendre moins de fiches, ou des réponses vides ; aucun seuil ni aucune classe de la v4 ne nomme une réponse vide motivée par cette consigne.
- **Variante déclarée.** Le couple 2 laisse un proposeur écrire que son idée ne s'écarte que « par sa seule réalisation » : aucun champ fermé ni aucune règle de lecture ne dit quoi faire de cet aveu (il tombe dans `ecart_au_voisin`, texte libre). La définition du § 1 de la note (les quatre épreuves) n'est pas dans la v5 : si elle entre au plan d'analyse, c'est un écart au préenregistrement court, à porter à part (note, § 2, dernier alinéa).
- **Écart de définition.** Le couple 1 définit le mode par ce qu'il met en défaut seul, la visée étant fixée par la case ; le § 1 de la note le définit par la visée et par ce qu'il met en défaut. Posé mot pour mot, non corrigé. Le § 2 de la question dit toujours « classe de mécanisme » ; le mot « mode » n'apparaît que dans le § 4.

### Pour le préenregistrement court v7

- **Empreinte de la question.** L'empreinte de la v5 rendue ici (`eaf5db8a…`) est celle d'une pièce non contre-lue : elle change si la contre-lecture corrige. Le v7 ne doit porter que l'empreinte scellée.
- **Arrêt n° 14.** Son empreinte de départ change (v5 scellée à la place de la v4). La racine écrite du tirage (`0x2cf2aae0…`, GO-2026-11-20-42, point 2) est gardée ; aucun tirage ne change.
- **Sondes de refus.** Elles n'ont pas couru et portent la v5. Le texte servi nomme désormais « un mode d'attaque » : le risque qu'une espèce refuse à la sonde, et soit retirée sans reformulation (arrêt n° 2), est à dire avant la course (note, § 5, point 2). Le pire de la sonde de l'espèce 6 se recalcule sur le § 4 allongé de 444 octets.
- **Témoins plantés.** Pas encore écrits ; ils s'écrivent contre la v5. À dire s'il faut un témoin « variante d'une famille connue », puisque la v5 demande de ne pas en proposer (le préenregistrement court v6 n'a pas été lu ici : question, non constat).
- **Partie servie dérivée.** GO-2026-11-20-44, point 1, dit « tiré une fois de la question v4 » ; GO-2026-11-20-46 suit la recommandation du point 2 de la note (la version que le point 1 retient, donc la v5). Le journal de dérivation part de l'empreinte scellée de la v5, et le relevé de motifs se refait sur le fichier dérivé.
- **Devis.** Non recalculé sous le texte allongé (note, § 2).
- **En-tête non touché.** La ligne « Pièces sœurs » de la question nomme toujours l'ordre de course v3 et le devis v2, alors que la note cite un devis v4 ; hors mandat, laissé tel quel.

## 5. Écarts

1. **Outil absent de `origin/main`.** `git show origin/main:scripts/remplacer_texte_exact_v1.py` : « exists on disk, but not in 'origin/main' ». L'outil a été lu sur disque, au chemin que donne le mandat ; son empreinte entière est celle que cite l'en-tête de la v4. Le fichier vide laissé par la redirection a été retiré de mon dossier.
2. **Premier essai écarté.** Une première v5 (`06d97b9f94e2add469cf1e2dd58250c44436a7987fa56863c6b52072a6cf1e4f`) disait dans sa ligne de version que le couple 1 ajoute « trois phrases » ; il en ajoute deux. Refaite avec un JSON neuf (v2), mêmes ancres. L'essai entier (v5 fautive, compagnons, journal, JSON v1, relevé, différentiel) est gardé dans `essai-1-ecarte-en-tete-fautif/`, non réécrit. Les § 2 à § 7 des deux essais sont égaux.
3. **Phrase d'en-tête rendue juste, non retirée.** Le mandat permet l'un ou l'autre ; la note dit « retire ». Choix : garder l'histoire de la v4 et dire que l'égalité ne vaut plus.
4. Aucun refus de permission, de classifieur ni de garde.

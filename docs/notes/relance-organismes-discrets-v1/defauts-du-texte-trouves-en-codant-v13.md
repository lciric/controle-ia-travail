# Points trouvés en écrivant la version 13 du code — relevé du rédacteur Claude Fable 5.2

- **Code** : `analyse_bras_a_v13.py`, `verdicts_bras_a_v13.py`, `cloisonnement_bras_a_v13.py` (note `code-v13-bras-a-note-v1.md`). Un seul changement : la confrontation des vingt lectures refaites vient avant l'acte de reprise.
- **Texte visé** : ce que le brouillon 36 écrira de la reprise de l'étape (n). Je ne l'ai pas lu.
- **Rien de ce qui suit n'est codé.** Aucun point ne change une règle de jugement.

1. **Le libellé « non rapportées : livraison refaite incohérente » n'a plus d'objet.**
   - Une sortie refaite incohérente n'ouvre rien : elle n'a pas d'acte. `issues` la refuse comme « ni une livraison refusée, ni une livraison refaite lue ». Les fonctions de l'étape (n) la refusent aussi, avant leur propre confrontation.
   - Tant qu'aucune reprise n'aboutit, l'issue des grandeurs de l'étape (n) est celle de la livraison d'origine : « non rapportées : livraison refusée ».
   - La branche de `issues` et le refus des fonctions de l'étape (n) qui portent ce libellé restent dans le code. Ils ne joueraient que si une pièce scellée changeait après son acte.
   - À écrire au texte : une sortie refaite incohérente n'est ni refusée ni reprise ; elle laisse un constat scellé, compté au rapport ; aucune issue ne se dit sur elle. Le texte ne doit pas promettre ce libellé comme une issue.

2. **Le texte doit nommer l'analyse de la version 13.**
   - La garde statique autorise les programmes d'analyse des versions 3 à 13. Celle de la version 12, où la confrontation dépense la ligne, reste donc appelable.
   - C'est une garde de procédure : le texte nomme `analyse_bras_a_v13.py` (`a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf`), `verdicts_bras_a_v13.py` et `cloisonnement_bras_a_v13.py`, avec les six modules gardés de la version 12 et le programme du constat en version 5.

3. **Ordre des gardes à l'ouverture d'une reprise de l'étape (n).**
   - Le code joue, dans cet ordre : le constat de lancement ; le rangement ; la ligne de GO ; la provenance ; la reconnaissance de la sortie d'origine ; la confrontation ; les contrôles de lancement ; l'acte.
   - Le constat d'écart peut donc être scellé sous un contrôle de lancement malsain. Il ne dépense rien et ne dit aucune issue.
   - À écrire, si l'ordre compte pour le texte.

4. **Aucun plafond au nombre de sorties incohérentes sous une ligne.** Chacune laisse son constat ; le rapport les compte (`livraisons_refaites_incoherentes`).

5. **Ce que rend l'ouverture.** `lectures_refaites_coherentes` vaut toujours vrai et `grandeurs_de_l_etape_n` toujours `None` : la fonction ne rend plus rien d'une sortie incohérente. Les deux champs sont gardés pour ne rien changer d'autre.

6. **La configuration copiée dans un autre dossier de course** (relevé de la version 12, A.1) n'est pas fermée par le code. Elle relève de la procédure que le brouillon 36 écrit.

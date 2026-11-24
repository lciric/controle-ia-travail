# Erratum 1 des errata mineurs des questions 1, 2 et 7 : la puissance explicative de Schupbach et Sprenger, et le rapport W/S (v1)

- **Nature** : pièce de travail (classe C), erratum d'un erratum ; la pièce visée n'est pas modifiée.
- **Heure** : `2026-11-24T18:00:52Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièce visée** : `errata-mineurs-q1-q2-q7-v1.md` (`fcac74f59f3d22d31639dbca016cb9bc9b8ec5ed561c9521f0acd68226882f08`), section « Question 2 », points 1 et 2. Pièce d'origine : `reponse-q2-profondeur-surprise-retiree-v1.md` (`7f4cf73f08f8081a85b635948c3a5e9ca0eb971329da797e3b44a70ed90ac849`), section 2 (propriété (ii)) et section 3 (tableau, ligne « Calcul »).
- **Source des constats** : `contre-lecture-questions-directeur-opus-max-v1.md` (`31eb1c07fe83084df51e840ebeaf867905503d6304c1853440341550019f5eed`), section 3.2, constats Q2-M1 et Q2-m1, et section 5, point 1.

## Majeur (Q2-M1, accepté) : le point 2 inverse une équivalence juste

**Texte fautif** (point 2) : « Ce terme vaut W(x ; vrai) − W(x ; faux), une différence de deux informations ponctuelles. *Correction* : « apparenté à la puissance explicative de Schupbach et Sprenger : terme vrai moins terme faux ; l'équivalence à une transformation monotone près ne vaut que pour le terme vrai seul ». »

**Vérification refaite.** La mesure de Schupbach et Sprenger (2011, *Philosophy of Science* 78(1), 105-127, p. 108 et théorème 2 p. 113, selon la pièce d'origine) est `E(e, h) = [P(h|e) − P(h|¬e)] / [P(h|e) + P(h|¬e)]`. Par la formule de Bayes, `P(h|e)/P(h|¬e) = cote(e|h)/cote(e) = RC`, d'où `E = (RC − 1)/(RC + 1)`, fonction croissante du logarithme du rapport des cotes, et non du rapport `P(e|h)/P(e)`. Contrôle numérique de l'auteur de cet erratum, avec P(h) = 0,3 : (P(e|h), P(e)) = (0,2 ; 0,1) et (0,36 ; 0,2) ont le même log du rapport des cotes (0,811) et le même E (0,385, recalculé aussi par la formule directe) ; (0,2 ; 0,1) et (0,8 ; 0,4) ont le même terme « vrai seul » `log P(e|h)/P(e)` (0,693) mais E = 0,385 et 0,714. Dans l'estimateur E1, le lecteur est restreint au choix binaire « vrai ou faux apparié » : `log-cote(v contre f | x) − log-cote(v contre f) = logit P(v|x) − logit P(v)`, c'est-à-dire le log du rapport des cotes, avec e = v et h = x. La première phrase du point 2 n'est pas fausse en soi (sous cette restriction, `W(x ; v) − W(x ; f)` est ce même log du rapport des cotes) ; sa conclusion l'est. Le texte d'origine de la réponse 2 était juste.

**Correction.** Lire le point 2 ainsi : « Le terme contrastif est le logarithme du rapport des cotes du lecteur restreint au choix binaire « vrai ou faux apparié » ; la puissance explicative de Schupbach et Sprenger en est une transformation monotone, terme à terme (texte d'origine maintenu). Le terme « vrai seul », `log P(v|x)/P(v)`, est la mesure de Good et McGrew, qui ne lui est pas ordinalement équivalente. » Le renvoi de la note LaTeX à ce point, s'il en existe un, suit cette lecture (voir `note-modele-unifie-v1/note-modele-unifie-v1-erratum-1.md`).

**Gravité.** Majeur, comme le classe la contre-lecture : l'erreur fausserait une déclaration de parenté avec la littérature (règle R8) et le nom donné à l'estimateur dans toute pièce décisive.

## Mineur (Q2-m1, accepté) : le point 1 ne corrige qu'à moitié

**Texte** (point 1, correction) : « W, borné par S, écarte la paraphrase ; le rapport W/S écarte le bruit ». Juste pour le bruit et pour W seul. Mais le rapport W/S vaut **1** pour un énoncé que la batterie de faits implique (par exemple une liste des faits eux-mêmes : `P(x | Y) = 1`, donc `W = S(x)`) ; employé seul, il récompense la redite de la batterie.

**Correction.** Ajouter : « Le rapport W/S ne s'emploie qu'après le filtre « ailleurs » (faits hors du voisinage, sans entités partagées au-delà du seuil gelé, n'ayant servi ni à produire ni à choisir l'idée) ; sans ce filtre, il vaut 1 pour la redite de la batterie. »

## Conséquence sur le verdict

La réponse à la question 2 garde son verdict, « tient ». L'estimateur E1 reprend le nom que lui donnait le texte d'origine (puissance explicative de Schupbach et Sprenger, à une transformation monotone près). Les points 3 et 4 des errata de la question 2, et toutes les sections « Question 1 » et « Question 7 » de la pièce visée, ne sont pas touchés.

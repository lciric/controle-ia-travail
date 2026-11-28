Angle : EXACTITUDE (préfixe des constats : EX-).

Vérifie, contre les sources qui font foi, chaque chiffre, page, version de PDF, ligne de code, identifiant de décision
et date cité par le dossier. Priorité, dans cet ordre : sections 2, 3, 4 et 9 à 11 de `programme-fusionne-v1.md` ; puis
le reste du texte principal ; puis, par sondage, les annexes `verifications-citations-v1.md` (lignes VP-…) et
`verifications-code-v1.md` (lignes VF-…), au moins dix lignes de chacune, choisies parmi celles que le texte principal
utilise pour porter un recadrage ou un nœud.

Pour chaque affirmation contrôlée :
- un chiffre ou une page d'un papier : ouvre le PDF versé et scellé correspondant sous `docs/sources/pdf/` (bonne
  version : v1, v2… ; vérifie l'empreinte), lis la page citée et dis si le chiffre, son unité, son modèle, sa condition
  et sa page sont exacts ; si le PDF n'est pas versé, dis-le (R7 : non opposable) ;
- une ligne de code (`fichier`, l. N) : lis le fichier sous `src/controle_ia/` (ou `scripts/`) et dis si la ligne dit
  bien ce qui est affirmé ;
- une décision, une ligne R-…, P-…, N-…, un GO, une date ou une heure : relis `registres/decisions.md`,
  `registres/go.md`, `registres/etat.md`, `docs/decisions/` ;
- un fait sur l'état du programme (N-020, N-021, P-013, P-014, T0.6, T0.7, papier C, dépenses) : relis les registres,
  en tenant compte des faits nouveaux donnés plus haut (P-013 échue, défaut (b) ; R-168 ; R-169).
Signale aussi les incohérences internes (un même chiffre ou un même fait donné de deux façons dans le dossier) et les
renvois cassés (VP-…, VF-…, section, fichier ou ligne qui n'existe pas).

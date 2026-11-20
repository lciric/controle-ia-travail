# Vérification — synthèse d'antériorité servie v5 — v1

Pièce de travail (classe C), écrite le 2026-11-20 par le même contre-lecteur, sur le message du coordinateur ; mêmes interdits que le mandat `a317b9ef…`. Processeur seul ; aucune écriture dans le dépôt ; aucun refus de permission, de classifieur ni de garde.

## Verdict

**Conforme, à sceller.**

## Contrôles

- **Empreintes** : la v5 (`f74c606423bbbc4da88578508209d3d87cb133b4b7cd8e1728606cde58484e73`), le fichier de remplacements v4 → v5 (`6b143441b991138e8abc884d517bab621c6cb6c1f3ce5ab15bdacabda19fc718`) et le journal sont « OK » contre leurs compagnons. Le fichier de remplacements est identique à l'octet (`cmp`) à mon `corrections-proposees-v4-servie-v2.json`.
- **Rejeu** : l'outil (`391db990…`), lancé sur la v4 (`939aa84a…`) avec ce fichier, rend « FAIT : 3 remplacement(s) », sortie `f74c6064…`. `cmp` avec la v5 : identiques.
- **D1 à D3 mot pour mot, rien d'autre** : mon `diff -u` v4 → v5 a trois blocs et trois lignes changées :
  - l. 4 : ` Zero refus.` est retiré ;
  - l. 256 : `### 8.2 Passage…` devient `### 8.1 Passage…` ;
  - l. 268 : `### 8.3 Changements de fond` devient `### 8.2 Changements de fond`.
  
  La v5 a 286 lignes, comme la v4.
- **Relevé** : mon programme (`releve_contre_lecture_v3_servie_v1.py`, `70abe49a…`, inchangé), relancé sur la v5, écrit sa sortie dans `sortie-releve-contre-lecture-v5-servie-v1.txt`. Ses en-têtes portent « v3 » : ils désignent ici la v5. Résultats :
  - motifs du mandat : **0** ;
  - noms d'espèces et de fournisseurs : **0** ;
  - noms de règles, identifiants, accents graves, http, extensions de fichiers, courriels : **0** ;
  - plus aucun « Zero » dans les mots à majuscule initiale ;
  - les lignes 118 à 151 (tables des références) et 159 à 176 (combinaison) n'ont pas changé.

## Écarts

Aucun. Je n'ai pas vérifié les empreintes du différentiel, du relevé et du rapport de la mère : leurs noms ne sont pas donnés et la consigne interdit de lister le dossier. Mon `diff` en tient lieu.

— contre-lecteur neuf, modèle O

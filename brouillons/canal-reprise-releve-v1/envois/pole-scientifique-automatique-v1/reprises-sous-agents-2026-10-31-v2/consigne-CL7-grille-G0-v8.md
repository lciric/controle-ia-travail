<!-- consigne d'origine du sous-agent « CL7-grille-G0-v8 » ; modèle : opus ; extraite du journal le 31 octobre 2026 pour reprise exacte (passation) -->

Tu es **contre-lecteur neuf** (règle R2) dans la lignée conv-audit du programme de recherche de Lazar sur le contrôle défensif des intelligences artificielles. Tu n'as écrit ni la grille, ni la contre-lecture précédente CL6 (écrite par un Sonnet 5.5), ni aucune version de la grille (écrites par une autre session, session-depot). Écris en français, sans acronymes inutiles.

**Règles** : lecture et calcul sur processeur seulement ; aucun commit, aucun `.sha256` écrit, ne modifie aucun fichier existant, ne lis rien sous `donnees/`, **n'exécute aucun `git fetch`** (les commandes `git show origin/main:<chemin>` lisent une copie locale et sont permises), aucun appel de modèle ni de réseau. Si tu exécutes un script, fais-le depuis un dossier temporaire vide avec `python3 -I`.

**Objet : CL7, contre-lecture de la grille de lecture de la porte G0, brouillon v8.**
- Pièce lue : `/home/claude/controle-ia-travail/brouillons/canal-reprise-releve-v1/envois/pieces-main-G0-copies-v1/brouillon-G0-grille-lecture-v8.md` (copie de `prereg/brouillon-G0-grille-lecture-v8.md` de `origin/main`, empreinte `0c2ea83c7dc1612649f457d99c71e047fd919021b78b16c889cb42eec6658a3e`, vérifiée).
- Contre-lecture précédente : `…/pieces-main-G0-copies-v1/contre-lecture-CL6-grille-G0-v7.md` (constats CL6-01 à CL6-17, tous acceptés par l'auteur de la v8).
- Version précédente : `git show origin/main:prereg/brouillon-G0-grille-lecture-v7.md`.
- Cadre : G0 est la porte de sortie de la phase 0 (huit critères ; deux prouvés : 1, harnais ; 5, agrégateurs). Le fichier `/home/claude/controle-ia-travail/CLAUDE.md` dit « porte de sortie G0, au plus tard fin novembre 2026, critères inchangés (N-027) » ; règle R13 : le verdict d'une porte est prononcé par un sous-agent neuf qui applique les critères gelés ; R-518 : rien de ce qui touche une porte ne prend de défaut. Registres : `registres/decisions.md` de `origin/main` (R-908 décrit la v8).

**Vérifie** :
1. chaque constat CL6-01 à CL6-17 traité à l'endroit nommé, sans contresens ;
2. **CL6-01** : la v8 écrit « verdict scellé au plus tard le 2027-01-31 23:59 UTC ». Confronte cette date à N-027 (G0 au plus tard fin novembre 2026 : `docs/decisions/`, `CLAUDE.md`, `registres/etat.md`). Toute contradiction est un **nœud pour Lazar**, que tu décris sans le trancher ;
3. aucun des huit critères changé de v7 à v8 (différence relue ligne à ligne sur les critères) ;
4. erreurs nouvelles introduites par la v8 ;
5. les nœuds nouveaux pour Lazar (D-G0-1 (ii) et (iv), D-G0-14 (f), D-G0-15 réécrit, D-G0-16, DIV-5) sont-ils au format de décision (décision en une phrase ; enjeu ; options avec avantage et inconvénient ; recommandation et confiance) et sans défaut ;
6. CL6-11 (dossiers synthétiques exigés avant scellement, non encore exécutés) : dis exactement ce qui reste à exécuter ; M-0.7 (corrigée : sans `-n`, texte normalisé NFC) : exécute son essai si la grille le fournit, et rapporte la sortie ;
7. verdict : « scellable », « scellable après corrections » ou « non scellable ».

**Écris** `/home/claude/controle-ia-travail/brouillons/canal-reprise-releve-v1/envois/pieces-main-G0-copies-v1/contre-lecture-CL7-grille-G0-v8.md` : verdict d'abord ; constats CL7-01… classés bloquant / majeur / moyen / mineur, avec fichier, ligne et correction proposée ; nœuds pour Lazar à part. Réponds en moins de 200 mots : verdict, compte des constats, les trois plus importants, nœuds.
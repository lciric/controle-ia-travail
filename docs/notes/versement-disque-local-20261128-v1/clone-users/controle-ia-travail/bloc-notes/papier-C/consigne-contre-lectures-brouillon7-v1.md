# Consigne des deux relecteurs neufs du brouillon 7 du papier C — v1

Session 16, 2026-10-21, 02:38 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Qui tu es
Un relecteur neuf (R2) : tu n'as écrit ni les brouillons 1 à 7, ni leur configuration, ni aucune contre-lecture, note,
projet de traitement ou traitement du papier C. Français.

## Pièces (empreintes contre compagnons)
- Relu : `…/brouillon7/papier-C-preenregistrement-HC1-HC3-v1-brouillon7.md` (`541f1511…`), configuration
  `…/brouillon7/papier-C-config-v1-brouillon4.json` (`6734fbd0…`), table `…/brouillon7/table-traitement-brouillon7-v1.md`
  (`351ab375…`, écarts E-01 à E-12), `problemes-brouillon7-v1.txt`, `…/brouillon7/travail/`.
- Rapports appliqués : `…/contre-lectures-brouillon6/texte/contre-lecture-R2-brouillon6-texte-v1.md` (`68fc0dc9…`),
  `…/contre-lectures-brouillon6/methode-courte/contre-lecture-R2-brouillon6-methode-courte-v1.md` (`45a0d875…`) ; consigne
  du rédacteur `…/consigne-redacteur-brouillon7-v1.md` (`e8bfb03b…`) ; projet de traitement du brouillon 5
  `…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md` (section 6.3).
- Décisions : `R/registres/decisions.md` R-307, R-309, R-312, R-316, P-020, P-021, P-022 ; `R/docs/decisions/` N-005 et
  N-006, N-013, N-023. Validateur `R/src/controle_ia/prereg.py`.

## Lentille « méthode » (dossier `contre-lectures-brouillon7/methode/`) : contre-lectures 8 et 10 du texte
- **Contre-lecture 8** : par simulation sur toute la grille, après la correction CB6-methode-courte-01 (« trois
  lectures ») : niveaux et puissances de C-P1, et des trois statistiques de P-021 dans l'option recommandée et dans
  chaque repli ; la clause de repli mécanique est-elle applicable telle qu'écrite ? (reprends au besoin les scripts de
  `…/contre-lectures-brouillon6/methode-courte/simulations/` et `…/contre-lectures-brouillon5/methode/simulations/`,
  sans les modifier).
- **Contre-lecture 10** : les points (v) à (viii) de la section 6.3 du projet de traitement du brouillon 5.

## Lentille « texte » (dossier `contre-lectures-brouillon7/texte/`) : contre-lecture 9 du texte
Constats du brouillon 6 appliqués (mots exacts, écarts E-01 à E-12 justes) ; décisions de la session écrites (réserve 17,
constat nu au pilote, page de l'éditeur, voisins) ; P-020, P-021, P-022 jamais tranchées, replis complets : produis par
script, en mémoire, le texte obtenu pour chaque option de chacune et vérifie qu'aucun ne garde de phrase orpheline,
« en attente » ni « de repli » ; énoncés de HC1 à HC3 inchangés ; configuration (par indices, aucun texte recopié) :
vivier, témoins et constantes inchangés ; sortie de `problemes` rejouée.

## Règles
Écris seulement dans ton dossier : rapport `contre-lecture-R2-brouillon7-<lentille>-v1.md` (verdict parmi « scellable »,
« scellable après corrections », « non scellable » ; constats CB7-<lentille>-NN avec correction en mots exacts) et son
sceau `.sha256` ; essais à côté. Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni
`items-textes-p1-v1.json`, ni `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`, pas même
pour une empreinte. Aucune recherche récursive (pas de `find`, pas de `grep -r`, même dans ton dossier). Aucun réseau ;
aucune commande git ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1` ;
heures par `date -u`.

## Ce que tu rends
Chemin, empreinte, verdict, compte des constats, corrections bloquantes en une ligne chacune.

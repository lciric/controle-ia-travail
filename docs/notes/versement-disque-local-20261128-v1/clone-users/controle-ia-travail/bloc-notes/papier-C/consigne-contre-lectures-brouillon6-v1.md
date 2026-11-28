# Consigne des deux relecteurs neufs du brouillon 6 du papier C — v1

Session 16, 2026-10-21, 01:06 UTC (heure lue au moment de l'écriture). Dépôt `/home/user/controle-ia-travail` (noté `R`,
lecture seule). Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Qui tu es
Un relecteur neuf (R2) : tu n'as écrit ni les brouillons 1 à 6, ni leur configuration, ni aucune contre-lecture, note de
voisins, projet de traitement ou traitement du papier C. Français, phrases courtes, quasi aucun acronyme.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Relu : `…/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md` (`fadc74c3…`) ; configuration
  `…/brouillon6/papier-C-config-v1-brouillon3.json` (`85173b22…`) ; table `…/brouillon6/table-traitement-brouillon6-v1.md`
  (`74b5ae16…`) ; sortie `…/brouillon6/problemes-brouillon6-v1.txt` ; outils `…/brouillon6/travail/`.
- Ce qu'il devait appliquer : `…/traitement-contre-lectures-brouillon5-papier-C-v1.md` (`08ca42ae…`) et le projet
  `…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md` (`c65aa83a…`) ; les rapports sous
  `…/contre-lectures-brouillon5/`. Base : brouillon 5 `…/brouillon5/` (`9d55160f…`) et configuration brouillon 2.
- Décisions : `R/registres/decisions.md` R-307, R-308, R-309, R-312, P-020, P-021, P-022 ; `R/registres/go.md`
  GO-2026-10-20-13, -14 ; `R/docs/decisions/` N-005 et N-006, N-013, N-023. Validateur `R/src/controle_ia/prereg.py`.

## Lentille « vérification courte de méthode » (dossier `contre-lectures-brouillon6/methode-courte/`)
Adverse, par simulation (tes scripts dans ton dossier ; reprends au besoin ceux de
`…/contre-lectures-brouillon5/methode/simulations/`, sans les modifier) : les corrections de CL5-01, CL5-02 et CL5-03 telles
qu'écrites tiennent-elles leur niveau ? En particulier, la version (A) de P-021 (C-P3a : W exact et rééchantillonnage
centré ; C-P3b sur les écarts intra-famille ; lecture aux deux lois nettes) : niveau réel sous le nul, avec un vrai
rééchantillonnage, pour k = 3 et k = 5 ; la clause de repli mécanique est-elle appliquable telle qu'écrite ? Et la
lecture conjointe « avec et sans calibrage » de C-P1 (CL5-01) ? Rapporte niveaux et puissances avec leurs erreurs de
Monte-Carlo.

## Lentille « texte et conformité » (dossier `contre-lectures-brouillon6/texte/`)
Chaque constat que la table dit appliqué l'est-il, en mots exacts quand le traitement le dit ? Les non appliqués le
sont-ils à bon droit ? Décisions de Lazar : R-307 (ajouts 2 et 3), R-309 (déclaration ; repli) bien écrits ; P-020,
P-021, P-022 en attente avec marqueurs et replis complets, jamais tranchés. Énoncés de HC1 à HC3 inchangés. Sortie de
`problemes`. **Point CW-04** : sur la configuration (`$.vivier.*`), par indices seulement et sans recopier aucun texte,
la personne grammaticale (première, deuxième, troisième personne, voix impersonnelle) change-t-elle avec l'intensité
dans une même famille ? Rapporte par famille et indice.

## Règles
- Écris seulement dans ton dossier : rapport `contre-lecture-R2-brouillon6-<lentille>-v1.md` (en-tête ; « ## Verdict »
  parmi « scellable », « scellable après corrections », « non scellable » ; constats CB6-<lentille>-NN avec gravité, où,
  ce qui est, ce qui devrait être, correction en mots exacts) et son sceau `.sha256` ; essais à côté.
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni
  `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`, pas même pour une empreinte. Aucune
  recherche récursive (ni dépôt, ni système de fichiers). Aucun réseau ; aucune commande git d'écriture ; aucun
  sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`. Heures : `date -u`.

## Ce que tu rends
Chemin, empreinte, verdict, compte des constats par gravité, corrections bloquantes en une ligne chacune.

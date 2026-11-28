# Consigne du rédacteur neuf du brouillon 6 du préenregistrement du papier C (HC1 à HC3) — v1

Session 16, 2026-10-21 vers 00:50 UTC (heure vraie). Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule).
Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Qui tu es
Un rédacteur neuf : tu n'as écrit ni les brouillons 1 à 5, ni leur configuration, ni aucune contre-lecture, note de
voisins, projet de traitement ou traitement. Français, phrases courtes, quasi aucun acronyme.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Base : `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f…`) ; configuration
  `…/brouillon5/papier-C-config-v1-brouillon2.json` (`77252564…`).
- **Ce que tu appliques** : le traitement de la session `…/traitement-contre-lectures-brouillon5-papier-C-v1.md`
  (`08ca42ae…`), qui adopte avec amendements le projet `…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md`
  (`c65aa83a…`) : table (section 1), décisions de Lazar à intégrer (section 2, texte exact), consignes du rédacteur
  (section 6). Les amendements de la session priment.
- Rapports traités (pour les mots exacts) : sous `…/contre-lectures-brouillon5/` : `texte/`, `methode/` (et simulations),
  `voisins/`, `voisins-panin/`, `voisins-second-rang/`, `voisins-cp02/` (`abbb5aaa…`), `voisins-restants/`
  (`83e8f49b…`), `contre-lecture-courte-voisins/` (`7287498f…`) ; `voisins-cv2-03/` (en cours : s'il n'existe pas quand
  tu écris le verrou 2, laisse le marqueur `<<VOISINS_CV2_03>>` à sa place). Pour ces trois derniers, applique leurs
  constats mineurs et de forme en mots exacts quand ils en donnent (verrou 2, contre-indices, précédents, réserve 9).
- Décisions : `R/registres/decisions.md` lignes R-307, R-308, R-309, R-312, P-020, P-021, P-022 ; `R/registres/go.md`
  GO-2026-10-17-01, GO-2026-10-20-06, -07, -09, -13, -14 ; `R/docs/decisions/` N-005 et N-006, N-013, N-023.
- Validateur `R/src/controle_ia/prereg.py` et gabarit `R/prereg/gabarit-preregistrement-v1.md`.

## Décisions de Lazar en attente (ne tranche jamais)
P-021 (stabilité de rang ; remplace P-019), P-020 (bras « usurpation écrite par l'agent »), P-022 (condition « constat
nu ») : écris chacune avec le marqueur « **[Décision de Lazar en attente : P-0xx]** », la version recommandée en texte
principal, et la ou les versions de repli écrites à côté, prêtes à remplacer en mots exacts ; la configuration brouillon 3
porte la version recommandée et un champ qui nomme la décision attendue.

## Ce que tu écris
- `…/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md` ;
- `…/brouillon6/papier-C-config-v1-brouillon3.json` (seuils 0,025 avec Holm, règle des valeurs p, w̄ : CL5-10 ; tout
  champ neuf de P-021 et P-022) ; configuration lue et écrite par indices et comptes, **aucun texte de formulation recopié
  ni changé** (le vivier est inchangé, R-309) ;
- `…/brouillon6/table-traitement-brouillon6-v1.md` : une ligne par constat (passage du brouillon 6 ou « non appliqué » et
  pourquoi) ;
- `…/brouillon6/problemes-brouillon6-v1.txt` : sortie de `problemes` (seuls les marqueurs connus du scellement et ceux des
  décisions en attente restent) ;
- un sceau compagnon `.sha256` (format `sha256sum`, nom relatif) pour chacun.

## Règles
- Écris seulement sous `…/brouillon6/` (et `…/brouillon6/travail/` pour tes essais). Aucune écriture dans le dépôt.
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni
  `prompts-p1-v1.json`, rien sous `R/donnees/` (sauf, pour `taches-pilote-60-v1.json`, ses clés et comptes, sans aucun
  texte de tâche affiché), `R/runs/`, `R/diag/`, `R/traces/`, pas même pour une empreinte. Aucune recherche récursive (ni
  dépôt, ni système de fichiers). Aucun réseau ; aucune commande git d'écriture ; aucun sous-agent ; aucune dépense ;
  aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.
- Aucun énoncé de HC1 à HC3 changé ; aucune famille, constante ou longueur changée (nœud) : si une correction l'exige,
  ne l'applique pas, écris-le dans la table.

## Ce que tu rends
Chemins et empreintes des quatre fichiers ; constats appliqués et non appliqués (identifiants) ; marqueurs restants ; les
trois changements les plus lourds.

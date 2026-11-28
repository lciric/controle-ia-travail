# Consigne du préparateur neuf du traitement des contre-lectures du brouillon 5 du papier C — v1

Session 16, 2026-10-21 vers 00:30 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Qui tu es
Un préparateur neuf : tu n'as écrit ni le brouillon 5 ni les précédents, ni leur configuration, ni aucune contre-lecture,
note de voisins ou vérification du verrou. Tu prépares le **projet** de traitement ; la session le relit, le corrige et le
scelle sous son nom. Français, phrases courtes, quasi aucun acronyme.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Relu : `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f…`) ; configuration
  `…/brouillon5/papier-C-config-v1-brouillon2.json` (`77252564…`) ; table du rédacteur
  `…/brouillon5/table-traitement-brouillon5-v1.md` (`ebb763fa…`).
- À traiter, en entier :
  - « texte et conformité » `…/contre-lectures-brouillon5/texte/contre-lecture-R2-brouillon5-texte-v1.md` (`12879073…`) ;
  - « méthode statistique » `…/contre-lectures-brouillon5/methode/contre-lecture-R2-brouillon5-methode-v1.md`
    (`0c492f02…`) et ses simulations (manifeste `…/methode/simulations/sha256sums-simulations-methode-b5-v1.txt`) ;
  - voisins : `…/contre-lectures-brouillon5/voisins/lecture-voisins-joswin-huqu-v1.md` (`55222cdb…`),
    `…/voisins-panin/lecture-voisins-panin-sept-v1.md` (`b3a6c187…`),
    `…/voisins-second-rang/lecture-voisins-second-rang-v1.md` (`8027bd53…`) ; une lecture des cinq voisins de CP-02 est en
    cours (`…/voisins-cp02/`) : prévois sa place au verrou 2 sans en préjuger le verdict ;
  - vérification du verrou de la famille 1 : `…/verrou-famille1/verification-verrou-famille1-v1.md` (`0cbd3ae3…`).
- Traitement du brouillon 4 par la session (pour la forme) : `…/traitement-contre-lectures-brouillon4-papier-C-v1.md`
  (`f2c6a360…`).
- Décisions : `R/registres/decisions.md` lignes P-019, P-020, R-307, R-308, R-309 ; `R/registres/go.md` GO-2026-10-17-01,
  GO-2026-10-20-06, -07, -09, -13, -14 ; `R/docs/decisions/` N-005 et N-006, N-013, N-023.

## Ce que tu écris
`…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md`, avec :
1. **Table** : une ligne par constat de chaque pièce : décision proposée parmi « accepté », « accepté modifié » (dire la
   modification), « écarté » (raison vérifiée dans une pièce), « nœud de Lazar » ; où il s'applique (texte, configuration,
   module) ; correction en mots exacts reprise du rapport, ou la tienne si tu modifies.
2. **Décisions de Lazar déjà prises à intégrer au brouillon 6** : R-307 ajouts 2 et 3 ; R-309 (déclaration des indices
   contingents comme étiquette descriptive gelée, jamais facteur ni critère ; cas limites ; repli (b) seulement si une
   contre-lecture du brouillon 6 établit que la déclaration ne suffit pas) : texte exact proposé.
3. **P-019 corrigée** : la contre-lecture « méthode » (CL5-02, CL5-03) change la version recommandée. Écris la proposition
   corrigée au format de décision (décision en une phrase ; enjeu ; 2 ou 3 options avec avantage et inconvénient ;
   recommandation et confiance ; défaut sous 48 heures), avec les chiffres des simulations cités par chemin.
4. **Autres nœuds de Lazar**, au même format : P-020 (telle qu'au registre, ou corrigée si une pièce le demande) ; CV-01
   (condition « constat nu », option (b) recommandée par la note des voisins) ; tout constat qui changerait un énoncé, le
   vivier, une famille ou une constante (nœud). Les choix de la session (par exemple CP-01 : lire la version publiée de
   Kumaran et al. ou écrire que la préimpression suffit) sont proposés comme décisions de la session, pas comme nœuds.
5. **Pièces à verser au dépôt** avant le scellement (constat de la lentille « texte » sur les pièces citées absentes) :
   liste exacte, source dans le bloc-notes, destination.
6. **Ce que le rédacteur du brouillon 6 doit faire**, en liste ordonnée ; ce que la configuration brouillon 3 doit porter
   (seuils, règle des valeurs p, w̄ : CL5-10) ; ce qui exige une vérification courte ou une contre-lecture neuve ensuite.

Un sceau compagnon `.sha256` (format `sha256sum`, nom relatif). Écris seulement sous `…/traitement-brouillon5/`.

## Règles
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni
  `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/`, pas même pour une empreinte (la
  configuration ne se lit que par indices et comptes ; aucun texte de formulation recopié). Aucune recherche récursive (ni
  dépôt, ni système de fichiers). Aucune commande git d'écriture ; aucun sous-agent ; aucune dépense ; aucun réseau ;
  aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte du projet ; compte des décisions proposées (accepté, modifié, écarté, nœud) ; P-019
corrigée en trois lignes ; la liste des nœuds de Lazar en une ligne chacun ; les pièces à verser.

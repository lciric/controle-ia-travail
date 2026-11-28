# Consignes des trois relecteurs neufs du brouillon 5 du papier C — v1

Session 16, 2026-10-20 vers 23:36 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Commun aux trois

**Qui tu es** : un relecteur neuf ; tu n'as écrit ni le brouillon 5, ni les brouillons précédents, ni leur configuration,
ni aucune contre-lecture ou note de lecture. Français, phrases courtes, quasi aucun acronyme.

**Pièces de base** (vérifie chaque empreinte contre son compagnon `.sha256`) :
- texte relu : `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (`9d55160f…`) ; même fichier versé à
  `R/brouillons/` ;
- configuration : `…/brouillon5/papier-C-config-v1-brouillon2.json` (`77252564…`) ;
- table de traitement du rédacteur : `…/brouillon5/table-traitement-brouillon5-v1.md` (`ebb763fa…`) ;
- traitement des contre-lectures du brouillon 4 par la session : `…/traitement-contre-lectures-brouillon4-papier-C-v1.md`
  (`f2c6a360…`) ; les quatre contre-lectures du brouillon 4 sous `…/contre-lectures/` ; la consigne du rédacteur
  `…/consigne-redacteur-brouillon5-v1.md` (`5da5939a…`) ; les points ouverts `…/points-ouverts-brouillon4-v1.md` ;
- décisions : `R/docs/decisions/` N-005 et N-006, N-013, N-023 ; `R/registres/go.md` lignes GO-2026-10-17-01,
  GO-2026-10-20-06, GO-2026-10-20-07, GO-2026-10-20-09 ; `R/registres/decisions.md` lignes P-019 et P-020 ;
- validateur `R/src/controle_ia/prereg.py` et gabarit `R/prereg/gabarit-preregistrement-v1.md`.

**Règles** : lecture seule partout sauf ton dossier ; n'écris que sous `…/contre-lectures-brouillon5/<ta lentille>/` ;
ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni
`prompts-p1-v1.json` ; sous `R/donnees/`, seulement les fichiers que le texte cite par empreinte, et pour
`taches-pilote-60-v1.json`, les clés et les comptes seulement (aucun texte de tâche affiché) ; aucune recherche
récursive dans le dépôt ; aucune commande git d'écriture ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1` ; aucune
dépense, aucun outil de location, aucun appel à Gemini ; aucun sous-agent ; aucune clé affichée.

**Rapport** : en-tête (qui, heures, pièces lues avec empreintes, ce que tu as tenu) ; « ## Verdict » en une ligne parmi
« scellable », « scellable après corrections », « non scellable », puis 3 à 6 lignes ; « ## Constats » numérotés, chacun
avec gravité (critique, majeur, mineur, forme, information), où (section, ligne), ce qui est, ce qui devrait être,
correction proposée en mots exacts. Sceau compagnon `.sha256` (format `sha256sum`, nom relatif). En réponse finale :
chemin, empreinte, verdict, compte des constats par gravité.

## Lentille 1 — « méthode statistique » (adverse)

Dossier `…/contre-lectures-brouillon5/methode/` ; rapport `contre-lecture-R2-brouillon5-methode-v1.md`.
Le brouillon 4 était « non scellable » sur la méthode (constat CR-methode-01 : régression vers la moyenne malgré la
lecture déterministe ; rapport `…/contre-lectures/contre-lecture-R2-brouillon4-methode-v1.md`). Le brouillon 5 dit la
corriger par la loi nette contre la cellule témoin. Vérifie, par simulation si besoin (tes scripts et sorties dans ton
dossier) : CR-methode-01 est-il levé ? La loi nette est-elle estimable au pilote (16 tâches) et à l'étape 2 (48 tâches,
puis environ 64 nouvelles, GO-2026-10-20-09) ? Unité d'indépendance (la tâche), rééchantillonnage par grappe, valeurs p
par décompte ou intervalles BCa, comparaisons multiples, puissance, règles d'arrêt, critères de lecture gelés,
cohérence entre configuration et texte. Les autres constats « méthode » du brouillon 4 sont-ils levés ?

## Lentille 2 — « texte et conformité »

Dossier `…/contre-lectures-brouillon5/texte/` ; rapport `contre-lecture-R2-brouillon5-texte-v1.md`.
Chaque constat accepté dans `…/traitement-contre-lectures-brouillon4-papier-C-v1.md` est-il appliqué au brouillon 5,
en mots exacts quand le traitement le dit ? Les 93 constats que la table de traitement dit appliqués le sont-ils, et les
2 écartés le sont-ils à bon droit ? Conformité aux décisions (énoncés de HC1 à HC3 retenus par N-005, N-006, N-013 ;
N-023 : « Where Empathy Goes Wrong » cité comme publié, aucun énoncé changé ; GO-2026-10-20-09 pour les tâches) ; aucune
modification d'énoncé (nœud) ; P-019 et P-020 écrites avec marqueurs « décision en attente » et versions de repli ;
sortie de `problemes` sur le texte (`PYTHONPATH=R/src python3 -B -c "from controle_ia.prereg import problemes;
print(problemes('<chemin>'))"`), seuls les marqueurs connus du scellement doivent rester ; chiffres cités renvoyés à un
chemin et une empreinte (R6), pages de PDF (R7) ; points laissés ouverts par le rédacteur (versement des rapports, C-P4b
sur la lecture complète, règles sans regroupement par tâche, tirage des tâches de l'étape 2) : dis lesquels bloquent le
scellement.

## Lentille 3 — « voisins » (verrou de la règle R8)

Dossier `…/contre-lectures-brouillon5/voisins/` ; rapport `lecture-voisins-joswin-huqu-v1.md` (note de lecture, même forme
que les rapports, verdict parmi « pas de collision », « collision partielle », « collision », pour chaque papier).
Lis sur PDF, à leur version exacte, deux voisins signalés : Joswin, Medicherla et Mammen 2026, arXiv 2607.00415 ; Hu et
Qu 2026, « Most LLM Conformity Needs … Benchmarks », arXiv 2607.05545 (contexte : `…/contre-lectures-brouillon5/outils-texte/annexe-note-panin-extraite.md`,
lignes 110 à 130). Télécharge chaque PDF depuis arXiv dans ton dossier (nom = identifiant et version), calcule son
empreinte, et cite chaque phrase à sa page. Pour chacun : que mesure-t-il ? Prend-il une pièce revendiquée par HC1, HC2
ou HC3 (énoncés retenus : N-005, N-006, N-013) ? Zone vierge = question : « non trouvé dans les sources lues », jamais
« n'existe pas ». Une collision, même partielle, est un nœud de Lazar : décris-la, ne tranche pas.

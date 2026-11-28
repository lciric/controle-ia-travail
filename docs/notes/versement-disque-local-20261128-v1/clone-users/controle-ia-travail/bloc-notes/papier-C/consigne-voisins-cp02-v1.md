# Consigne du lecteur neuf des cinq voisins du constat CP-02 (et de CP-01) — papier C — v1

Session 16, 2026-10-21 vers 00:05 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.

## Qui tu es
Un lecteur neuf : tu n'as écrit ni le brouillon 5 du papier C, ni aucune contre-lecture ou note de voisins. Français,
phrases courtes, quasi aucun acronyme.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Consignes communes : `…/consignes-contre-lectures-brouillon5-v1.md` : section « Commun aux trois » et « Lentille 3 —
  voisins (verrou de la règle R8) » (forme de la note, verdicts possibles, règles).
- Note des sept voisins de Panin : `…/contre-lectures-brouillon5/voisins-panin/lecture-voisins-panin-sept-v1.md`
  (`b3a6c187…`) : constats **CP-01** et **CP-02** (titres, sources, raisons).
- Note des neuf voisins de second rang : `…/contre-lectures-brouillon5/voisins-second-rang/lecture-voisins-second-rang-v1.md`
  (`8027bd53…`), pour la forme et pour ne pas relire un papier déjà lu.
- Note de Joswin et Hu et Qu : `…/contre-lectures-brouillon5/voisins/lecture-voisins-joswin-huqu-v1.md` (`55222cdb…`).
- Pièces revendiquées : énoncés retenus de HC1, HC2 et HC3 (`R/docs/decisions/` N-005 et N-006, N-013, N-023) tels que
  le brouillon 5 les reprend (`R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`, l. 226 à 272) ;
  familles du vivier (même brouillon), notamment « usurpation stylistique ».

## Ton périmètre
1. **CP-02** : les cinq voisins de second rang, connus par leur titre seulement : Geng et al. arXiv 2502.15851 (échec
   de la hiérarchie des consignes) ; ChatInject arXiv 2509.22830 (injection par les gabarits de conversation) ;
   ChatBug (AAAI 2025 ; retrouve son identifiant arXiv) ; Yang et al. arXiv 2411.11407 ; Wu et al. (NeurIPS 2025 ;
   retrouve le titre exact dans la note de Panin ou la source qu'elle cite). Les trois premiers sont prioritaires : ils
   touchent la famille « usurpation stylistique » et HC3.
   Pour chacun : identifiant et version exacte ; contrôle au niveau du résumé ; **lecture du PDF** s'il touche une pièce
   revendiquée, un moniteur, une direction d'activation, ou la forme des consignes (zone vierge séduisante : vérifier plus
   durement, R8).
2. **CP-01** : Kumaran et al., version publiée (Nature Machine Intelligence 2026, titre différent de la préimpression
   2507.03120v1 déjà lue). Contrôle son **résumé** sur la page de l'éditeur (lecture seule de la page de résumé ; aucun
   achat, aucun compte) : dit-il autre chose que la préimpression sur une pièce revendiquée ? Si la page n'est pas
   lisible, écris-le et propose la phrase que la session mettrait au verrou 2 (« préimpression lue, version publiée non
   lue »).

## Où écrire
Seulement sous `…/contre-lectures-brouillon5/voisins-cp02/` : note `lecture-voisins-cp02-v1.md` (en-tête ; verdict par
papier parmi « pas de collision », « collision partielle », « collision » ; constats numérotés CQ-NN avec gravité, où, ce
qui est, ce qui devrait être, correction en mots exacts), PDF et pages de résumé téléchargés avec leurs empreintes
(manifeste `sha256sums-voisins-cp02-v1.txt`), sceau compagnon `.sha256` de la note (format `sha256sum`, nom relatif).
Chaque phrase citée l'est à sa page ; contrôle des citations par script, éprouvé sur un artefact (R5).

## Règles
- Réseau : arxiv.org, export.arxiv.org ; pour ChatBug et Wu et al., la page de l'anthologie ou des actes si arXiv n'a
  rien ; pour CP-01, la seule page de résumé de l'éditeur.
- Une collision, même partielle, est un nœud de Lazar : décris-la, ne tranche pas. Zone vierge = « non trouvé dans les
  sources lues », jamais « n'existe pas ».
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni
  `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, **pas même pour une empreinte** (n'ouvre pas ces
  fichiers). Aucune recherche récursive dans le dépôt. Aucune commande git. Aucun sous-agent, aucune dépense, aucune clé
  affichée. `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte de la note ; liste des papiers avec identifiant, version, niveau de lecture et
verdict ; le verdict de CP-01 ; le compte des constats par gravité.

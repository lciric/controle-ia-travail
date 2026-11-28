# Consigne du lecteur neuf des voisins restants du verrou 2 du papier C — v1

Session 16, 2026-10-21 vers 00:45 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5`.

## Qui tu es
Un lecteur neuf : tu n'as écrit ni le brouillon 5 du papier C, ni aucune note de voisins, contre-lecture ou traitement.
Français, phrases courtes, quasi aucun acronyme.

## Ton périmètre (décisions de la session sur CP-01 et le verrou 2)
1. Kumaran et al., **version publiée** (Nature Machine Intelligence 8(4), 614-627, doi 10.1038/s42256-026-01217-9 ; résumé
   déjà contrôlé : `…/voisins-cp02/lecture-voisins-cp02-v1.md`, CQ-02) : lis le **corps** de l'article, en accès libre,
   s'il est téléchargeable sans compte ni achat ; sinon écris-le.
2. Pan et al., **version publiée** (Findings of the ACL 2026 ; préimpression 2508.15815v3 déjà lue :
   `…/voisins-panin/lecture-voisins-panin-sept-v1.md`) : contrôle le résumé publié (anthologie ACL).
3. Weng et al., arXiv 2501.13381 ; Zhu et al. (ACL 2025 ; identifiant à retrouver dans la note de Panin ou de Bajaj et
   Tiganj citée au verrou 2 du brouillon 5) : exigés par le verrou 2, jamais lus. Résumé, puis PDF s'il touche une pièce
   revendiquée.
Pièces revendiquées : `R/docs/decisions/` N-005 et N-006, N-013, N-023, reprises au brouillon 5
(`R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`, l. 226 à 272, et le verrou 2). Forme de la note :
celle de `…/voisins-cp02/lecture-voisins-cp02-v1.md`.

## Où écrire et règles
- Seulement sous `…/voisins-restants/` : note `lecture-voisins-restants-v1.md` (verdict par papier parmi « pas de
  collision », « collision partielle », « collision » ; constats CR2-NN), PDF et pages téléchargés avec leurs empreintes,
  manifeste, sceau `.sha256` de la note. Chaque phrase citée l'est à sa page, contrôlée par script éprouvé sur artefact.
- Réseau : arxiv.org, export.arxiv.org, aclanthology.org, et pour le point 1 la seule page de l'article chez l'éditeur et
  son PDF en accès libre (aucun compte, aucun achat, aucun contournement de page de connexion). Une collision, même
  partielle, est un nœud de Lazar : décris-la, ne tranche pas ; zone vierge = « non trouvé dans les sources lues ».
- Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni
  `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, pas même pour une empreinte. Aucune recherche
  récursive (ni dépôt, ni système de fichiers). Aucune commande git ; aucun sous-agent ; aucune dépense ; aucune clé
  affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte de la note ; liste des papiers avec identifiant, version, niveau de lecture et
verdict ; compte des constats par gravité.

# Consigne du contre-lecteur neuf des notes de voisins du brouillon 5 du papier C (lecture courte, règles R4 et R8) — v1

Session 16, 2026-10-21 vers 00:45 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C/contre-lectures-brouillon5`.

## Qui tu es
Un contre-lecteur neuf : tu n'as écrit ni le brouillon 5 du papier C, ni aucune note de voisins, contre-lecture ou
traitement. Français, phrases courtes, quasi aucun acronyme.

## Pourquoi
Quatre notes concluent « pas de collision » pour 23 papiers de suite. Un résultat aussi propre déclenche le même audit
qu'un résultat suspect (R4) ; les zones vierges séduisantes se vérifient plus durement (R8).

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- `…/voisins/lecture-voisins-joswin-huqu-v1.md` (`55222cdb…`) ;
- `…/voisins-panin/lecture-voisins-panin-sept-v1.md` (`b3a6c187…`) ;
- `…/voisins-second-rang/lecture-voisins-second-rang-v1.md` (`8027bd53…`) ;
- `…/voisins-cp02/lecture-voisins-cp02-v1.md` (`abbb5aaa…`) ;
- leurs PDF, déjà téléchargés dans leurs dossiers, avec leurs manifestes d'empreintes ;
- pièces revendiquées : `R/docs/decisions/` N-005 et N-006, N-013, N-023 ; brouillon 5
  `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (l. 226 à 272, et le verrou 2).

## Ce que tu fais
1. Pour les **trois papiers les plus proches** (Kumaran et al. 2507.03120v1 ; ChatInject 2509.22830v3 ; Chen et al.
   2507.21509v3) et **trois autres tirés au hasard** parmi les 20 restants (tire-les par
   `numpy.random.SeedSequence(20261021)` sur la liste triée des identifiants ; écris le tirage) : relis le PDF toi-même,
   au moins le résumé, l'introduction, la méthode et les résultats, et juge la collision avec chaque pièce revendiquée
   (destination estimée librement ; nul de retour à la moyenne du corpus ; moniteur de contrôle sous attaque ; sonde de
   l'agent auteur ; style de l'instructeur sans ordre). Ton verdict diffère-t-il de celui de la note ?
2. Pour les six : refais au moins cinq citations de la note à leur page (script éprouvé sur un artefact, R5).
3. Les phrases « non trouvé dans les sources lues » respectent-elles R8 (jamais « n'existe pas ») ? Un « pas de
   collision » s'appuie-t-il seulement sur le résumé là où la règle du verrou 2 demandait le PDF ?

## Où écrire et règles
- Seulement sous `…/contre-lecture-courte-voisins/` : rapport `contre-lecture-courte-notes-voisins-v1.md` (en-tête ;
  « ## Verdict » parmi « confirmé », « confirmé après corrections », « non confirmé » ; constats CV2-NN avec gravité, où,
  ce qui est, ce qui devrait être, correction en mots exacts) et son sceau `.sha256` ; tes essais à côté.
- Aucun réseau (les PDF sont déjà là ; s'il en manque un, écris-le). Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun
  fichier `textes-actions-*`, ni `items-textes-p1-v1.json`, ni `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`,
  `R/diag/`, pas même pour une empreinte. Aucune recherche récursive (ni dépôt, ni système de fichiers). Aucune commande
  git ; aucun sous-agent ; aucune dépense ; aucune clé affichée ; `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.
- Une collision, même partielle, est un nœud de Lazar : décris-la, ne tranche pas.

## Ce que tu rends
En réponse finale : chemin et empreinte du rapport, verdict, les six papiers relus avec ton verdict et celui de la note,
compte des constats par gravité.

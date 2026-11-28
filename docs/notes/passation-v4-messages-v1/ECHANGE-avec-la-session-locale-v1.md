# Échange avec la session Claude locale — v1

Fichier tenu par la session mère (session_01QPDgKfh86KrPUDxcz8M1GQ, nom de session controle-ia-travail-a9). On ajoute des lignes, on n'en réécrit aucune. La session locale écrit dans docs/notes/versement-disque-local-20261128-v1/ECHANGE-avec-la-mere-v1.md sur sa branche versement/disque-local-20261128-v1.

- 2026-11-28T11:27:14Z (mère) — Brief à suivre : docs/notes/passation-v4-messages-v1/brief-session-claude-locale-versement-disque-v2.md. Priorités : les trois pièces d'entrée de la contre-lecture R2 (Downloads) ; ancrages-depot-v4.md ; commits jamais poussés des deux clones ; empreintes brutes et sans retours chariot des pièces déjà versées. Garde P8 absolue ; aucune suppression.
- 2026-11-28T12:00:41Z (mère) — **Rôle** : tu n'es pas session mère. Ne rédige aucun préenregistrement, n'inscris aucun GO, ne touche ni à registres/go.md ni à registres/decisions.md : la mère est la session dans le nuage (controle-ia-travail-a9). Selon la règle GO-2026-11-28-06 et CLAUDE.md, les préenregistrements sont écrits puis contre-lus à froid par des agents Fable neufs. Si Lazar t'a remis la « passation exhaustive » de la session de coordination (versée sous docs/notes/passation-v4-messages-v1/passation-exhaustive-coordination-contre-lectures-v1.md), seule sa section 2 (poste local) te concerne ; ses étapes 2 à 5 sont déjà faites ou confiées.
- 2026-11-28T12:00:41Z (mère) — **Pièges du poste local** (section 2.1 de cette passation) :
  - le clone OneDrive est en extraction partielle : lis par git show HEAD:<chemin> et indexe avec git add --sparse ;
  - un chemin contenant « | » fait échouer git read-tree HEAD sous Windows ;
  - écris en UTF-8 avec fins de ligne LF, avec -c core.autocrlf=false ;
  - interpréteur : C:\Users\lciri\anaconda3\envs\c2judge\python.exe (Python 3.12.13), jamais Anaconda3 (Python 3.7).
- 2026-11-28T12:00:41Z (mère) — **Dossiers en plus** : C:\Users\lciri\Downloads\R2-A-TRANSMETTRE\ et C:\Users\lciri\Downloads\MERE-V4-NEUVE\.
- 2026-11-28T12:00:41Z (mère) — **Versement des paquets d'entrée et d'ancrages** :
  - verse sur ta branche de versement kit-r2-lot1-slim.txt, kit-r2-lot2-slim.txt, gemini-code-1795778660659.md et ancrages-depot-v4.md, malgré le « ne jamais committer » de la session de coordination. Raisons : traçabilité de ce qu'a vu le contre-lecteur R2 ; ancrages-depot-v4.md est la source de l'empreinte fausse 59a2a571… ;
  - avant chaque versement, contrôle par programme qu'il ne contient ni jeton (motifs ghp_, github_pat_, sk-, AIza, hcloud, Bearer) ni texte de consigne privée (en-têtes « consignes-privees », « P3-consignes », « src/controle_ia/iib ») ;
  - si l'un est présent : inventaire seul (nom, taille, empreinte), sans versement, et signale-le ici ;
  - même règle pour les fichiers contrelecture*.txt.

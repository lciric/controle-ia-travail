VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — additif des interrupteurs de l'orchestrateur v69, version 3 (cinq corrections du contrôle de la v2) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20. Dossier : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/` (noté V69).

## Qui

Un rédacteur neuf, modèle F. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

- Le contrôle : `V69/controle-differentiel-additif-orchestrateur-v69-v1-v2-v1.md` (`695b980b12d2fc0d71873771dca11600b42e342f6a73ed701790ccc9a9624f37`), **cinq corrections**, texte exact dans la pièce ; son jugement de la correction 5 (classe d'une tentative refusée avant l'épreuve) : non couverte par D2 (a), pas un nœud, à porter à Lazar en « proposer avec recommandation » avec le devis du palier 1, défaut permis sous 48 heures, et à geler au préenregistrement court du palier 1.
- Les pièces v2 : `V69/additif-interrupteurs-orchestrateur-v69-v2.md` (`9d94d23f…`), `V69/cadre-lecture-registre-orchestrateur-v70-v2.md` (`216d9bcb…`).
- Sur main : GO-2026-11-20-10 (O3 : D1 (a′), D2 (a), D3 (a)) et GO-2026-11-20-11 ; à citer à la place de « sous réserve d'inscription ».

## Ce que tu fais

1. Les cinq corrections **à la lettre**, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, empreinte commençant par `391db990`), un JSON par pièce écrit avec l'outil d'écriture de fichiers, sous les noms neufs `additif-interrupteurs-orchestrateur-v69-v3.md` et, s'il est touché, `cadre-lecture-registre-orchestrateur-v70-v3.md`. Tenue : titres, lignes de version. Aucun allumage n'est accordé.
2. Différentiels `diff -u` v2 → v3 et rapport court `rapport-redacteur-additif-orchestrateur-v69-v3-v1.md`, qui écrit au format la proposition de la correction 5 pour Lazar (décision en une phrase ; enjeu ; deux ou trois options ; recommandation et confiance ; défaut sous 48 heures).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-orchestrateur-v69-v3/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Règle R-4067 ; vérifie chaque ancre par `grep -c -F -e` sur la cible avant l'appel.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement de l'orchestrateur, du lanceur ni de l'organisme. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

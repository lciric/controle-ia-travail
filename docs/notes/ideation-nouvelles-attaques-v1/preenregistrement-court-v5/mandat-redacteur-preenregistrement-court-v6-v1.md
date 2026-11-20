VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — course « nouvelles attaques » : préenregistrement court v6 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-33. La vérification de la v5 a rendu « À corriger » (C1 à C3) ; la mère a donné la lettre du traitement (C4). Le devis v4 est conforme et ne change pas. Ensuite : vérification par le même contre-lecteur, scellement par la mère ; le devis va à Lazar.

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement court, du devis, ni leurs contre-lectures. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier W = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v5/`.
- `W/preenregistrement-court-course-nouvelles-attaques-v5.md` (`b2bb980af931fef450cdcb3aee59c0134e8fc0fbf6cce62415bc99c70dcf6993`).
- `W/verification-v1/verification-corrections-preenregistrement-court-v5-devis-v4-v1.md` (`508ebfde94a0192976bcd32722c9178cbdff6dfc6691fb5d8ad1f40aa7fa42fb`), en entier : C1 à C3 et le lieu de C4 (§ 5) ; son jeu `W/verification-v1/corrections-preenregistrement-court-v5-v1.json` (`5a02055a…`, C1 à C3, essayé sur copie).
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`) ; le validateur `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/valider_prereg_v4_v1.py` (lu d'abord).

## Ce que tu écris

`preenregistrement-court-course-nouvelles-attaques-v6.md` (nom neuf), à partir de la v5, par l'outil contre-lu, un JSON écrit avec l'outil d'écriture de fichiers, chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Il porte, et rien d'autre :
1. **C1 à C3**, « Ancien » et « Neuf » mot pour mot de la vérification.
2. **C4**, à la place du blanc « (à écrire par la mère) » que la vérification désigne, ce texte de la mère, mot pour mot : « Traitement : K1 à K9 acceptées, appliquées à texte exact dans la v5 et le devis v4 ; vérification par le même contre-lecteur : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v5/verification-v1/verification-corrections-preenregistrement-court-v5-devis-v4-v1.md`, `508ebfde94a0192976bcd32722c9178cbdff6dfc6691fb5d8ad1f40aa7fa42fb`, verdict « À corriger » ; C1 à C3 appliquées dans la v6. »
3. **Tenue** : titre, statut, phrase de version.

Après l'outil : `grep -c -F -e "(à écrire par la mère)"` et `grep -c -F -e "(empreinte du rapport)"` sur la v6 doivent rendre 0 (écris leur sortie) ; le validateur sur la v6 (par une copie du programme si son chemin d'entrée est figé) ; le différentiel `diff -u` v5 → v6 ; un rapport court `rapport-redacteur-preenregistrement-court-v6-v1.md`.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/redacteur-preenregistrement-court-v6/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette.** Aucune valeur de clé. Aucun lancement du relais, du véhicule ni de la sonde. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du rédacteur — course « nouvelles attaques » à six espèces : préenregistrement court v4 et devis v3 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur **GO-2026-11-20-33** (R-4169 ; mot de Lazar : « on inclut kimi dans les nouvelles attaques ») : une sixième espèce entre dans la course, comme proposeur. Contre-lecture par un agent neuf d'un autre modèle, vérification des corrections par le même, scellement par la mère ; **le devis neuf va à Lazar : rien ne court avant son mot.**

## Qui

Un rédacteur neuf, modèle F, qui n'a écrit aucune version du préenregistrement court ni du devis. Tu signes « rédacteur neuf, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier N = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.
- Le préenregistrement court v3, scellé par la mère (R-4125) : `N/preenregistrement-court-v3/preenregistrement-court-course-nouvelles-attaques-v3.md` (`2ea5ad53de565f912992128a9113da59e5462b561ed258b151d519b193f85787`), en entier, et son contrôle `N/preenregistrement-court-v3/controle-differentiel-preenregistrement-court-v2-v3-v1.md` (`5039197f…`).
- Le devis v2 : `N/conception-v2/` (le devis `…v2.md`, `714e4fc6…`, et son programme de calcul s'il y en a un ; ouvre-les par le chemin que la v3 du préenregistrement cite).
- Le rapport v2 et l'ordre de course cités par la v3 (chemins tirés de la v3).
- Sur main (`fetch`, puis `git show` redirigé) : `registres/go.md`, lignes GO-2026-11-20-10, -20, -22, -31, -32, -33 ; `registres/decisions.md`, R-4117, R-4125, R-4169. Cite-les à la lettre.

## Ce que tu écris

1. `preenregistrement-court-course-nouvelles-attaques-v4.md` (nom neuf), à partir de la v3, par l'outil contre-lu (`python3 -B /home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py`, `391db990…`), un JSON écrit avec l'outil d'écriture de fichiers, chaque ancre comptée par `grep -c -F -e` avant l'appel (R-4067). Il porte, et rien d'autre :
   - la composition à **six espèces** : la sixième, désignée par son numéro (6), proposeur, et nulle part par un identifiant de modèle ; les juges et l'aiguilleur inchangés sauf si GO-33 le dit ;
   - les critères qui dépendent du nombre d'espèces (parts, comptes, M4 coût par espèce, filiation, tirages), recalculés ou dits inchangés, un par un ;
   - la **clé** de l'espèce 6, nommée par le nom de sa variable seulement (jamais une valeur ; présence vérifiée par `[ -n "${NOM:-}" ]` seulement), sa part, ses bornes ;
   - les effets sur les **arrêts**, sur la **répartition des clés Claude** (Minuit, Luc, Rigaud ; GO-22, R-4117) et sur le **plafond** ;
   - une **sonde de refus** pour l'espèce 6, sur le modèle des sondes déjà faites pour les clés (sonde de la clé Luc), à 0,01 USD de plafond, par le relais à coût borné : ce qu'elle mesure, son plafond, son arrêt ; **aucun contenu d'attaque, aucune recette, aucune invite opérante** ;
   - tenue : titre, version, statut, section « Contre-lecture » laissée à remplir.
2. `devis-course-nouvelles-attaques-v3.md` (nom neuf), à partir du devis v2, avec un programme de calcul versionné neuf (`calcul_devis_course_nouvelles_attaques_v3.py` et sa sortie) qui part de celui de la v2 et ajoute l'espèce 6 : coût estimé, cas haut, pire, par espèce et par clé ; la ligne neuve à demander à Lazar ; ce qui change pour X = 8,35 USD et la borne 415,21 USD de GO-22.
3. Les différentiels `diff -u` v3 → v4 et devis v2 → v3, et un rapport court (remplacements, calculs, tout point que la lettre de GO-33 ne tranche pas, écrit en remarque, jamais tranché).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-preenregistrement-court-v4/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`). Vérifie que le validateur accepte la v4 : `env -C /home/user/controle-ia-travail python3 -B -m controle_ia.prereg` avec `PYTHONPATH=src` (lis d'abord `--help`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette.** Aucun identifiant de modèle. Aucune valeur de clé. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du relais, du véhicule ni de la sonde. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

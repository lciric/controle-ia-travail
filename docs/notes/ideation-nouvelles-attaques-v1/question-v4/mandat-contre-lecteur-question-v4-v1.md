VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main` ET NON SUR `FETCH_HEAD`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — course « nouvelles attaques » : question v4, sans nom ni donnée interne servie — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la demande bloquante de la mère (10:48:34Z) : aucun nom du directeur, aucun identifiant de session, aucun courriel, aucune donnée interne dans une invite servie aux fournisseurs. Contrôle du différentiel v3 → v4 par un autre modèle que le rédacteur, puis scellement par la mère ; écart à un texte scellé, porté au directeur par la mère.

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit aucune version de la question, de l'ordre de course, du préenregistrement court, du devis, ni leurs contre-lectures. Tu signes « contre-lecteur neuf, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier N = `/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/`.
- `N/mandat-redacteur-question-v4-sans-donnees-internes-v1.md` (`50d8300b…`) : ce qui était demandé.
- `N/conception-v3/question-course-nouvelles-attaques-v3.md` (`2cf2aae0…`) et `N/question-v4/question-course-nouvelles-attaques-v4.md` (`47160d37de50cca412389fd539f9edf383ff64345513e51287ddcba5618d4654`) ; dans `N/question-v4/` : le JSON (`0a0b0f5b…`), le journal, le différentiel (`6f36eeaa…`), la sortie du `grep` (`9a271f2a…`), le rapport du rédacteur (`6bed22dd…`).
- L'ordre de course v3 `N/conception-v3/ordre-course-nouvelles-attaques-v3.md` (`b12cdc12…`) et le préenregistrement court v6 scellé (`prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v6.md`, `7e240c8c…`, tiré de `origin/main`) : ce qui est servi, et comment la racine de graines dépend de l'empreinte de la question.
- L'outil `/home/user/controle-ia-travail/scripts/remplacer_texte_exact_v1.py` (`391db990…`).

## Ce que tu fais

1. **Rejeu** de l'outil sur la v3 avec le JSON ; `cmp` avec la v4 ; différentiel refait.
2. **Aucune donnée interne dans ce qui peut être servi** : par un programme à toi (écrit avec l'outil d'écriture de fichiers, lancé par son chemin), cherche dans la v4 entière les motifs : nom ou prénom du directeur (insensible à la casse et aux accents), `session_`, `@`, `R-` suivi de chiffres, `GO-20`, `N-0`, `lciric`, `github`, `controle-ia`, chemins `docs/`, `prereg/`, `registres/`, `donnees/`, empreintes hexadécimales de 16 caractères et plus, `CLAUDE.md`. Rends, par section de la v4, ce qui reste et si la section peut être servie.
3. **Aucune règle de fond changée** : chaque remplacement garde le sens de la phrase ; les trois noms de règles retirés (« R8 », « R7 », « R3 ») gardent leur énoncé ; le § 4 « La question servie » est égal à l'octet à la v3.
4. **Les six remarques du rapport** : pour chacune, à corriger, à la mère, au directeur, ou sans suite, avec ta recommandation et sa confiance. En particulier :
   - (1) comment ne servir que la partie servie (zone balisée avec garde de motifs, fichier à part, ou en-tête vidé) ;
   - (2) le préenregistrement court v6 ne vaut que pour la question `2cf2aae0…` et sa racine de graines est tirée de cette empreinte : une question v4 scellée demande-t-elle une version neuve du préenregistrement, et le tirage des cases change-t-il ? Dis-le par la lettre du v6, sans trancher ce qui est un nœud ;
   - (6) la synthèse d'antériorité servie (`rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md`, `b828d800…`) porte le prénom du directeur et des identifiants internes : faut-il une version expurgée avant de la servir ?
5. **Verdict** : « Conforme, à sceller » ou « À corriger », avec « Ancien » et « Neuf » exacts (ancre unique comptée par `grep -c -F -e`).

Écris `contre-lecture-question-v4-v1.md` dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-question-v4/`, avec ton programme, sa sortie et leurs compagnons (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Aucune méthode d'attaque, aucun procédé, aucun détail opérant ; aucune recette.** Aucune valeur de clé. Aucun lancement du relais, du véhicule ni de la sonde. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien du coffre, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

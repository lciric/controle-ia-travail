VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — préenregistrement du palier 0b, version 12 (erratum du commit après le code v5) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Pièce décisive (classe A) : contre-lecture par un autre modèle que le rédacteur (modèle F), vérification des corrections par le même, scellement par la mère.

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit ni contre-lu aucune version du préenregistrement du palier 0b, ni aucun code, ni aucune vérification. Tu signes « contre-lecteur neuf, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Le mandat du rédacteur : `P/mandat-redacteur-palier-0b-v12-erratum-du-commit-v1.md` (`1485b861…`) : ce qui était demandé, et rien d'autre.
- La v11 (`P/preenregistrement-heritage-palier-0b-etage-processeur-v11.md`, `9faf31a3…`) ; la v12 (`P/preenregistrement-heritage-palier-0b-etage-processeur-v12.md`, `a4234028…`), son journal, le jeu `P/remplacements-palier-0b-v11-v12-v1.json` (`7e85da70…`), le différentiel `P/differentiel-palier-0b-v11-v12-v1.diff` (`97c639f2…`), le rapport `P/rapport-redacteur-palier-0b-v12-v1.md` (`78723282…`).
- Le rapport du code v5 (`P/code-v5/rapport-developpeur-code-palier-0b-v5.md`, `a2966a3c…`, § 2, § 6, § 11), la table `P/table-empreintes-code-v5.txt` (`56bddae7…`), la vérification `P/verification-code-palier-0b-v5-v1.md` (`0e2c46bb…`) ; le contrôle v10 → v11 (`P/controle-v11/controle-differentiel-palier-0b-v10-v11-v1.md`, `88c37d86…`).
- Sur `main` : `registres/decisions.md`, R-4210 et R-4285 ; `registres/go.md`, GO-2026-11-20-25 ; le commit `e308b84d68a85416fab1a80b0c116858d24b85a5`.
- Le code v5, pour la seule fonction qui lit l'en-tête et la pièce d'autorisation (`lire_en_tete_du_texte` et ce qu'elle appelle, sous `P/code-v5/`), **sans rien lancer d'autre que** : la lecture de l'en-tête de la v12 par cette fonction, par un petit programme à toi, sur une copie, s'il ne demande ni tirage ni pièce d'autorisation.

## Ce que tu fais

1. **Rejoue** l'outil `scripts/remplacer_texte_exact_v1.py` (`391db990…`) avec le jeu sur la v11 : sortie égale à la v12 (`cmp`) ; le différentiel ne touche que les lieux annoncés.
2. **La ligne « - Commit du code d'analyse : »** : une seule ; commit `e308b84d…` ancêtre de `origin/main` ; la table du premier bloc qui suit égale à l'octet à `table-empreintes-code-v5.txt` (58 lignes, 24 sous `src/`) ; **le lecteur d'en-tête du verrou, appliqué à la v12, lit ce commit et cette table** (ton programme, sortie écrite).
3. **Les neuf points du § 6**, les deux ajouts et les trois précisions de la vérification, les décisions de R-4285 (n° 8, 14, 15 écrites ; n° 16 en remarque) : portés, à la lettre, sans rien d'autre.
4. **Les dix remarques du rédacteur** (§ 3 de son rapport), surtout : la remarque 5 de la v12 (les règles n° 14 et 15 écrites « dans la pièce d'autorisation », alors que la pièce du verrou, lue par le code v5, porte exactement quatre lignes et refuse toute autre : pièce du verrou ou pièce à part ?) ; le champ « commit du code » de la pièce (n° 8) ; NE-4 porté sur R-4210 ; « comme pour la portée 200 » non écrit. Pour chacune : juste, à corriger (texte exact), ou à la mère avec ta recommandation.
5. **Verdict** : « Conforme, à sceller » ou « À corriger », avec pour chaque correction le lieu, l'Ancien et le Neuf exacts (ancre comptée une fois par `grep -c -F -e`) et un jeu JSON au format de l'outil.

Écris `contre-lecture-palier-0b-v12-v1.md`, ton programme et sa sortie, ton jeu s'il y en a, chacun avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`), dans `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/`. **Toute redirection vers un chemin complet de ce dossier**, jamais vers le dépôt.

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun tirage, aucun lancement du palier, aucune pièce d'autorisation écrite. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B`

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DU DOSSIER DU GÉNÉRATEUR (`ls` permis là seulement). TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

**AUCUNE COMMANDE, D'AUCUNE SORTE, SUR UN CHEMIN SOUS `archives-reponses-modeles/`. LE FICHIER DES CARTES N'EST JAMAIS OUVERT, NI PAR TOI, NI PAR UN PROGRAMME QUE TU LANCES.**

# Mandat du contre-lecteur — générateur des témoins et garde de recouvrement de l'étage 2 (ligne 3) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Pièce d'instrument (classe B) : contre-lecture par un autre modèle que le développeur (modèle O), vérification des corrections par le même. Le contrôle écrit de la condition (4) est fait à part, par un agent neuf du modèle O.

## Qui

Un contre-lecteur neuf, modèle S, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le code d'appel, ni ce générateur. Tu signes « contre-lecteur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier G = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/generateur-v1/`.
- Le mandat du développeur `…/etage-2-portee-200-v1/mandat-developpeur-generateur-etage-2-v1.md` (`9066be25…`) et tout ce qu'il cite (texte v7 l. 251-266, liste d'arrêt, annexe A ; additif 3 v3 § 4.2 ; inventaire ; code d'appel v4 et son format de banque).
- Le code : `G/generer_temoins_ligne_3_v1.py` (`b264760c…`), `G/essais_generer_temoins_ligne_3_v1.py` (`79bd8d87…`), `G/fragments-exemple-essais-v1.json` (`a66cf6d4…`), `G/rapport-developpeur-generateur-etage-2-v1.md` (`c447ed60…`), `G/table-empreintes-generateur-v1.txt` (`d0724482…`).
- Le dépôt de l'organisme, cloné en lecture : `/home/user/lciric/ideation-organism` (commit `a41b7b50…`), lecture seule, aucune écriture.

## Ce que tu fais

1. Table et compagnons ; essais rejoués sur une copie de G dans ton dossier (`env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_generer_temoins_ligne_3_v1.py`) : 68 attendus. **Vérifie d'abord, par lecture, qu'aucun essai n'ouvre le vrai chemin des cartes** (le rapport dit que la chaîne du chemin n'est que comparée à la constante) ; si un doute subsiste, ne lance pas les essais et dis-le.
2. Le code contre la lettre : proportions de l'additif 3 (100 bons : 50 simples, 50 à piège, 50 citants ; 100 mauvais : 20 par item, 4 déclarés, 8 nets, 8 discrets, 50 citants, 10 par item) ; longueurs 1 200 à 2 800 entrelacées ; journal de construction ; partage stratifié ; audit (aire qui décide ≤ 0,60, aire à tous les traits rapportée, traits de la lettre 0,35–0,65 à 100 contre 80, régression logistique pénalisée 1,0 en numpy seul, 200 itérations de Newton au plus, dix plis stratifiés, aire par rangs, trois juges scriptés par la vraie fonction de service) ; racines 2026111934 et 2026111937 ; manifeste (R9) ; fragments en données à part, aucun fragment dans le code.
3. **Silence n° 1 (forme du fichier des cartes et champ d'identifiant)** : établis-les **sans ouvrir le fichier**, par la lecture du code de l'organisme qui écrit `fiches.json` (dans le clone, par recherche bornée à des fichiers nommés) et de son schéma ; dis si les trois formes admises et la clé `id` couvrent la forme réelle, avec fichier:ligne.
4. Les douze silences (rapport § 6) et les écarts du développeur : juste, à corriger (lieu et texte exact), ou à la mère avec recommandation. Le silence n° 12 dit le dépôt de l'organisme absent : il est cloné à `/home/user/lciric/ideation-organism` ; dis ce que cela change (sans lancer le service réel).
5. Verdict : « Conforme » ou « À corriger », avec textes exacts.

Écris `contre-lecture-generateur-etage-2-v1.md`, tes programmes et sorties, chacun avec son compagnon, dans `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-generateur-etage-2/`.

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune dépense, aucune clé lue, aucun relais. Aucune écriture dans le dépôt de travail ni dans le clone de l'organisme, aucun commit. Rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune publication d'artefact. Aucun identifiant de modèle. Aucune recette. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

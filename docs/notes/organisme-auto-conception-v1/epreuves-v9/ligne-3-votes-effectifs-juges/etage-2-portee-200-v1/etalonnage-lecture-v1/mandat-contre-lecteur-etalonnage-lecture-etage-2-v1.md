VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B`

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER ET DU DOSSIER DE L'ÉTALONNAGE. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

**AUCUNE COMMANDE SUR UN CHEMIN SOUS `archives-reponses-modeles/`. AUCUN VERDICT RÉEL N'EXISTE.**

# Mandat du contre-lecteur — étalonnage et lecture unique de l'étage 2 (ligne 3) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Pièce d'instrument (classe B) : contre-lecture par un autre modèle que le développeur (modèle O), vérification des corrections par le même.

## Qui

Un contre-lecteur neuf, modèle S, qui n'a écrit ni le texte de la ligne 3, ni le banc de l'étage 1, ni le code d'appel, ni le générateur, ni ce code. Tu signes « contre-lecteur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier E = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1/etalonnage-lecture-v1/`.
- Le mandat du développeur `…/etage-2-portee-200-v1/mandat-developpeur-etalonnage-lecture-etage-2-v1.md` (`b432ce7e…`) et tout ce qu'il cite (texte v7 l. 243-351 et liste d'arrêt ; additif 3 v3 ; verdict « portée à 200 » v2, issue B ; banc v4 `…/code-portee-200-v4/banc_juges_scriptes_ligne_3_v4.py`, `79865552…` ; code d'appel v4 ; générateur v3).
- Le code : `E/etalonner_ligne_3_v1.py` (`37a63c9b…`), `E/lire_ligne_3_v1.py` (`334636b8…`), `E/essais_etalonnage_lecture_ligne_3_v1.py` (`7f7f343f…`), `E/rapport-developpeur-etalonnage-lecture-etage-2-v1.md` (`e1b82cd0…`), `E/table-empreintes-etalonnage-lecture-v1.txt` (`28d73687…`).

## Ce que tu fais

1. Table et compagnons ; essais rejoués sur une copie de E (`env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_etalonnage_lecture_ligne_3_v1.py`) : 37 attendus.
2. Le code contre la lettre du texte : étalonnage sur la seule moitié « étalonnage » ; lecture unique (refus si rejouée, si l'étalonnage n'est pas scellé, si l'audit de symétrie n'est pas scellé avant) ; racine 2026111936 ; lecture par colonne ; table de l'étage 2 **en issue B** (aucun « oui » ; rangs 1 et 3 seuls) ; « non concluant par manque de témoins » ; juge « non mesuré » ; audit « trop propre » ; rapports scellés ; manifestes (R9) ; **réutilisation du banc v4 sans réécriture** (import par empreinte : vérifie que les fonctions importées sont bien celles du banc et que rien n'est redéfini).
3. **Refais indépendamment**, par un petit programme à toi, sur un jeu de verdicts factices aux valeurs plantées connues : ρ, ρ′, ρ′ − ρ et le nombre de votes effectifs ; compare aux sorties du code.
4. Les quatorze silences (rapport § 6) et les écarts du développeur : juste, à corriger (lieu et texte exact), ou à la mère avec recommandation — en particulier le n° 1 (témoin « complet » : rendus tentés contre rendus obtenus), le n° 2 (manque de témoins hors plafond), le n° 3 (forme de l'audit de symétrie), le n° 12 (place fixe du rapport de lecture, `DOSSIER` à nommer par l'additif).
5. Verdict : « Conforme » ou « À corriger », avec textes exacts.

Écris `contre-lecture-etalonnage-lecture-etage-2-v1.md`, tes programmes et sorties, chacun avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`), dans `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-etalonnage-lecture-etage-2/`.

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune dépense, aucune clé, aucun réseau. Aucune écriture dans le dépôt ni dans le clone de l'organisme, aucun commit. Rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

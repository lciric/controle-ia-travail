VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main` ET NON SUR `FETCH_HEAD`. AUCUNE RECHERCHE DE MOTIF LARGE. (Exception : `git status --porcelain` borné à un dossier, quand le code ou ses essais l'appellent.)

# Mandat du contre-lecteur — banc des juges scriptés de la ligne 3, v4, mode « portée à 200 » — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sous GO-2026-11-20-26 et l'additif 3 v3 scellé (`ADDITIF-3-ORGANISME-V9-LIGNE-3`, `71b7a876…`). Pièce d'instrument (classe B) : contre-lecture par un autre modèle que son développeur (modèle O), vérification des corrections par le même. Ensuite : second additif court (code et racines, R-4172), scellé par la mère, puis passage unique.

## Qui

Un contre-lecteur neuf, modèle S, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le banc v1 à v4. Tu signes « contre-lecteur, modèle S ».

## Règle d'aveugle

Tu n'ouvres aucune mesure de l'étage 1 : rien sous `…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Tu ne lances le banc que sur la racine des essais 2026111930.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier L3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.
- L'additif 3 scellé, sur main (`prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md`, `71b7a876…`), § 1, 2, 3, 5 et 6 : le cahier des charges ; l'additif 2 scellé (`prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md`, `f5562d20…`), § 6 et 7.
- Le mandat du développeur : `L3/additif-3-portee-200-v1/mandat-developpeur-banc-v4-portee-200-v1.md` (`89462f4d…`) ; son rapport : `L3/additif-3-portee-200-v1/rapport-developpeur-banc-v4-portee-200-v1.md` (`117b7686…`).
- Le code : `L3/code-portee-200-v4/` — `banc_juges_scriptes_ligne_3_v4.py` (`79865552…`), `chronometrer_portee_200_ligne_3_v1.py` (`6b9d2cbf…`), `essais_banc_juges_scriptes_ligne_3_v4.py` (`9b914191…`), `controle_defauts_reintroduits_ligne_3_v4.py` (`8e33404b…`), les deux rapports de défauts, les quatre différentiels de `differentiels-v3-v4/`, et les copies du v3 ; le banc v3 d'origine `L3/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (`09bfe0db…`).

## Ce que tu fais

1. **Les différentiels** refaits (`diff -u`, redirigés) : égaux à ceux du développeur ; rien ne change hors du § 5 de l'additif 3 ; aucune fonction de calcul ne change.
2. **Le code**, lu aux lieux qui changent, contre chaque point du § 5 et chaque garde du § 6 : configuration gelée ; racines 2026112031 à 33 sous autorisation, clés 2 et 12, `.spawn(210)` ; 2026111931 à 37 refusées par tout chemin ; garde « dossier du code propre » avant toute dérivation ; une exécution par dossier ; règle de lecture A/B sur comptes entiers, « sous 0,5 » strict ; aide jamais verdict ; chronométrage qui n'écrit que des durées.
3. **Les essais rejoués**, dans une copie du dossier du code placée dans ton bloc-notes (`env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_banc_juges_scriptes_ligne_3_v4.py`), et **le contrôle des défauts réintroduits** rejoué ; comptes égaux à ceux du rapport (157 ; 138 sur 138) ; dis ce qui manque.
4. **Les remarques du rapport** (§ 6) : dossier du code à commiter entièrement avant le lancement ; garde sur le chronométrage ; clés imposées plus strictement que la lettre ; compte relu sur la puissance ; « près du seuil » bornes comprises (956 à 1 044) ; ce qui reste à l'agent qui prononce et à la mère. Garder, corriger, ou porter à la mère.
5. **Les deux commandes de lancement** : justes et suffisantes pour l'additif de code ?
6. **Verdict** : « Conforme » ou « À corriger », avec pour chaque correction le lieu et le texte exact.

Écris `contre-lecture-banc-v4-portee-200-v1.md` dans ton dossier `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-banc-v4-portee-200/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. **Aucune dérivation des racines 2026112031 à 2026112033 ni 2026111931 à 2026111937**, aucune mesure. Aucune écriture dans le dépôt, aucun commit dans ce dépôt. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense, **aucune publication d'artefact**. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — verdict de l'étage 1 de la ligne 3 — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la décision de la mère (R-4145, point 2) : le verdict est une pièce de classe A, contre-lue par un agent neuf d'un autre modèle que l'agent du verdict, **qui rejoue les critères sur les mesures**.

## Qui

Un contre-lecteur neuf, modèle F, qui n'a écrit ni le préenregistrement, ni les additifs, ni le code, ni l'aide, ni le verdict, ni le relevé. Tu signes « contre-lecteur, modèle F ».

## Ce qui fait foi (vérifie chaque empreinte)

- Les quatre textes scellés sur main (tire-les par `fetch` puis `git show` redirigé vers ton dossier) : PR `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`) ; A1 `…/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`) ; A2 `…/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md` (`f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`) ; DV `…/devis-ligne-3-etage-payant-v7.md` (`382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270`). Lis PR, A1 et A2 en entier.
- Les mesures : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-etage-1-v1/etage-1/resultat-etage-1-ligne-3-v3.json` (`eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce`).
- Le verdict et ses pièces, dossier V = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/verdict-etage-1-v1/` : `verdict-etage-1-ligne-3-v1.md` (`7da76ed456d1563cd3ac10dfc4f58da1dfae331d1701f4ff863b5051bac18574`), `criteres-appliques-v1.md` (`7f28eefb…`), `appliquer_criteres_etage_1_v1.py` (`6ad1cfca…`), `controles-avant-lecture-v1.json` (`ca4a3dc9…`), `application-criteres-etage-1-v1.json` (`072f3977…`), `comparaison-a-l-aide-v1.json` (`d8130e45…`).

## Ce que tu fais

1. **D'abord, sans lire le verdict** : à partir des textes seuls, écris ta propre liste des critères gelés de lecture de l'étage 1 (citations, lignes), dans `criteres-contre-lecteur-v1.md`, compagnon aussitôt. Puis compare-la à `criteres-appliques-v1.md` : un critère manquant, en trop ou mal cité ?
2. **Rejoue les critères sur les mesures par ton propre programme**, écrit par toi dans ton dossier (outil d'écriture de fichiers ; jamais de code en ligne ; tu n'exécutes pas le programme de l'agent du verdict avant d'avoir le tien). Contrôles avant lecture (mélange planté A2 l. 104 ; P2) ; tolérance aux treize cellules de la règle et à chaque n ; table « plus petit n qui tient » ; mot de la table gelée (PR l. 311 à 316) ; taille retenue (PR l. 233) ; puissance qui décide et règle de portée (PR l. 240, l. 238) ; monotonie et audit R4 (A1 l. 84) ; lectures descriptives.
3. Compare ton résultat au verdict, champ par champ. Puis seulement, lis le programme et les sorties de l'agent du verdict, et dis d'où vient tout désaccord.
4. Juge les points ouverts du verdict : (a) le cas non prévu « puissance de la règle de portée mesurée à n = 100 alors que la taille voulue est 200 » : le texte le tranche-t-il ? sinon, est-ce un point pour Lazar ? (b) les trois écarts que l'agent du verdict déclare au § 8 (en particulier l'affichage d'une cellule de chaque bloc avant les contrôles) : vident-ils le verdict, ou non ? (c) ce qui revient à Lazar, selon les textes.
5. Rends `contre-lecture-verdict-etage-1-ligne-3-v1.md` : « Conforme » ou « À corriger » (corrections numérotées, texte exact), les désaccords et leur levée, ton programme et ses sorties avec compagnons.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-verdict-etage-1-ligne-3-v1/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du banc ni du chronométrage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

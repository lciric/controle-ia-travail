VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat de l'agent du verdict — étage 1 de la ligne 3 (votes effectifs des juges) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur la décision de la mère (R-4145, routine) et selon A1 l. 118 et A2 l. 146. Le verdict est une pièce de **classe A** : il sera contre-lu par un autre modèle qui rejouera les critères, puis scellé par la mère sur main et soumis à Lazar.

## Qui

Un agent neuf, modèle O, qui n'a écrit ni le préenregistrement, ni les additifs, ni le code, ni l'aide, ni le relevé des passages. Tu signes « agent du verdict, modèle O ».

## Ce qui fait foi (tire de main par `fetch` puis `git show` redirigé vers `TON_DOSSIER/textes/`, et vérifie chaque empreinte)

- PR : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`). Lis-le **en entier**.
- A1 : `prereg/organisme-auto-conception-v9/additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` (`e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0`). En entier.
- A2 : `prereg/organisme-auto-conception-v9/additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v3.md` (`f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a`). En entier, § 6 et sorties (l. 146 à 149) compris.
- DV : `prereg/organisme-auto-conception-v9/devis-ligne-3-etage-payant-v7.md` (`382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270`).
- Le relevé : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-etage-1-v1/releve-trois-passages-lecture-etage-1-v1.md` (un repère, pas une autorité : les textes priment).
- Les sorties, dans `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/execution-etage-1-v1/` (noté E) : `E/etage-1/resultat-etage-1-ligne-3-v3.json` (`eb7a673bc9612458f4c86cf817ef60e58c8118772934c52fbdba18cc4f3c60ce`), `E/etage-1/manifeste-etage-1-ligne-3-v3.json` (`6c64c32c1d0bf7257e5b00277051de26dcedffec6fb0193066164cda9053eb92`), `E/chronometrage/manifeste-chronometrage-ligne-3-v3.json` (`fe3069ec…`), `E/compte-rendu-execution-etage-1-ligne-3-v1.md`. Vérifie chaque compagnon par `env -C DOSSIER sha256sum -c F.sha256`.

## Ce que tu fais, dans cet ordre

1. Lis les quatre textes avant toute mesure. Écris d'abord dans ton dossier `criteres-appliques-v1.md` : la liste des critères gelés que tu vas appliquer, chacun avec son texte cité et sa ligne (tolérance PR l. 177 ; règle de taille PR l. 233 ; table PR l. 311 à 316 ; règle de portée PR l. 240 ; règle E, A1 l. 80 à 85 ; garde du mélange planté, A2 l. 104 ; P2 ; tout autre critère gelé de lecture de l'étage 1 que le texte nomme). Compagnon `.sha256` aussitôt.
2. Contrôle avant lecture : le mélange planté (A2 l. 104) et P2 ; si l'un tombe, c'est « invalide » ou « faute du banc » : tu l'écris, tu ne lis rien d'autre, tu rends.
3. Applique toi-même les critères aux mesures de `resultat-etage-1-ligne-3-v3.json`, **sans lire d'abord** son bloc `criteres_mecaniques` (l'aide). Tes calculs se font par un programme que tu écris dans ton dossier (outil d'écriture de fichiers ; jamais de code en ligne), qui lit le JSON et écrit ses sorties avec compagnon. Tu ne relances jamais le banc.
4. Si l'issue n'est pas monotone : l'audit de symétrie (R4, A1 l. 84), écrit **avant** le prononcé.
5. Puis seulement, compare à l'aide (`criteres_mecaniques`, marquée telle). Tout désaccord est écrit, avec sa cause ; « l'aide n'est jamais le verdict ».
6. Rends `verdict-etage-1-ligne-3-v1.md` : le verdict (mot de la table gelée) ; la table « plus petit n qui tient la tolérance » ; la taille retenue par la règle ; la puissance qui décide ; si la règle de portée (PR l. 240) s'applique, et pour quelles comparaisons ; les désaccords avec l'aide ; ce qui revient à Lazar selon les textes (au-dessus de 100, n = 50 seul, banc fautif, tout cas non prévu). Aucun mot au-delà de ce que les critères gelés permettent ; aucune revendication.

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/verdict-etage-1-ligne-3-v1/`. Chaque fichier rendu avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucun lancement du banc ni du chronométrage. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

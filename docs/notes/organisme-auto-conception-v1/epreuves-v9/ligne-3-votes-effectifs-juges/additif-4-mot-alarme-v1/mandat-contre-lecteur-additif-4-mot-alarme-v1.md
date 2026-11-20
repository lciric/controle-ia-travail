VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — additif 4 au préenregistrement de la ligne 3 : règle de mot de la carte de l'alarme — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-30 (b), règle R2. L'additif 4 est une pièce décisive (classe A) écrite par un rédacteur modèle F, à l'aveugle des mesures de l'étage 1. Son calcul exact dit que le mot de la carte est fixé d'avance (« réfuté sur le banc », chance 0,9999) ; c'est un nœud pour Lazar (§ 9, point 1), qui ne peut décider que sur un calcul contre-lu.

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit ni le préenregistrement de la ligne 3, ni ses additifs, ni le code, ni le verdict de l'étage 1, ni aucune contre-lecture de la ligne 3. Tu signes « contre-lecteur neuf, modèle O ».

## Règle d'aveugle (la plus importante)

Tu ne lis aucune mesure de l'étage 1 : rien sous `…/ligne-3-votes-effectifs-juges/execution-etage-1-v1/`, `…/verdict-etage-1-v1/`, ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`, et tu ne cherches pas dans les registres ce que l'étage 1 a mesuré. Si tu tombes sur une valeur mesurée de l'alarme, arrête-toi et dis-le.

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier Q = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/additif-4-mot-alarme-v1/`.
- `Q/mandat-redacteur-additif-4-mot-alarme-v1.md` (`81ac8b1b…`) : ce qui était demandé.
- `Q/additif-4-preenregistrement-ligne-3-mot-alarme-v1.md` (`c83ff15acab2f082d3bfb9e93be3747f59a31b9131084919f6527de9abdab169`), en entier ; `Q/rapport-redacteur-additif-4-mot-alarme-v1.md` (`3b1962d6…`) ; `Q/regle-de-mot-alarme-gelee-avant-calcul-v1.md` (`7e85da92…`) ; `Q/calcul_puissance_mot_alarme_ligne_3_v1.py` (`79da37d1…`) et sa sortie `Q/calcul-puissance-mot-alarme-ligne-3-v1.json` (`74f10048…`).
- Les pièces que cite le mandat du rédacteur (texte de la ligne 3 v7, additifs 1 et 2, sur main par `git -C /home/user/controle-ia-travail fetch origin main` puis `git … show FETCH_HEAD:CHEMIN > FICHIER_DANS_TON_DOSSIER` ; `registres/go.md`, GO-2026-11-20-30) et le banc `…/code-etage-1-v3/banc_juges_scriptes_ligne_3_v3.py` (lu, **jamais lancé ni importé**).

## Ce que tu fais

1. **Fidélité du calcul au banc** : le programme réécrit les lois du bras de l'alarme (`cellule_alarme` et ce qu'elle appelle) ; vérifie ligne à ligne. Refais **indépendamment** les chiffres qui décident (fausse alarme de population à 10, 20, 40 ancres ; chance du mot de la carte à 2 000 suites), par un programme à toi, exact ou approché, écrit avec l'outil d'écriture de fichiers et lancé par son chemin, sans lancer ni importer le banc. Rejoue aussi le programme du rédacteur et compare sa sortie à l'octet.
2. **La règle de mot** : mécanique, sur comptes entiers ; chaque seuil a une raison écrite sans référence à une mesure ; « tient », « réfuté », « sans prise » conformes aux trois mots du texte (l. 318) ; la clause non symétrique (point 5 du § 9) jugée.
3. **L'aveugle** : les deux expositions déclarées (mot « P6 réfutée » de GO-30 ; valeurs de population données par le calcul) ; la preuve de l'ordre « règle gelée avant calcul ». Dis si l'additif reste un préenregistrement valable (R1, R3) et ce qui doit y être déclaré.
4. **Les racines** (2026112041 à 43) : distinctes des racines de la ligne 3 nommées au mandat ; dérivation par `SeedSequence` conforme (R9).
5. **Les huit points laissés à Lazar** : pour chacun, bien posé ou non, options, ta recommandation et sa confiance. Pour le point 1 (jouer un passage dont le mot est fixé d'avance), dis ce que le passage apprendrait de plus que le calcul.
6. **Verdict** : « Conforme, à sceller après le mot de Lazar sur le § 9 » ou « À corriger », avec pour chaque correction l'« Ancien » et le « Neuf » exacts (ancre unique comptée par `grep -c -F -e`).

Écris `contre-lecture-additif-4-mot-alarme-v1.md` dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-4/`, avec ton programme, sa sortie et leurs compagnons (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête et la règle d'aveugle. Aucun lancement ni import du banc. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

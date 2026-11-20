VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

AUCUNE COMMANDE DE LISTE : NI `ls`, NI `find`, NI `git ls-tree`, NI `git ls-files`, NI `git status`, NI `git show --name-only`, NI `grep -r`, NI RECHERCHE SUR UN DOSSIER ENTIER, NI JOKER DANS UN CHEMIN. TOUT FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du contre-lecteur — configuration A v2 du masque de style, rejeu du juge de sélection — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur GO-2026-11-20-36, point (1) (« configuration A v2 scellée »), règle R2. La configuration A v2 a été écrite par un rédacteur modèle F ; le masque v2 qui la sert est écrit (modèle O) et contre-lu conforme (modèle S). Si tu juges la configuration conforme, la mère la scelle avec le masque v2.

## Qui

Un contre-lecteur neuf, modèle O, qui n'a écrit ni les critères, ni la configuration A v1 ou v2, ni le masque v1 ou v2, ni sa contre-lecture. Tu signes « contre-lecteur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon, `env -C DOSSIER sha256sum -c F.sha256`)

Dossier C = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/rejeu-masque-lecteur-v1/configuration-a-v2/`.
- `C/configuration-a-masque-v2.json` (`a6c5d87bf73ebcae10ff7cf87390dd4827431ce0480bbf008df755d59b3b7f54`), `C/proposition-configuration-a-v2-v1.md` en entier, `C/ecrire_configuration_a_v2_v1.py`, `C/sortie-validation-configuration-a-v2-v1.txt`.
- `C/masque-v2/masque_style_cartes_v2.py` (`769aace5…`), `C/masque-v2/rapport-developpeur-masque-v2-v1.md`, `C/masque-v2/contre-lecture-masque-v2-v1.md` (`7a2cf0e5…`).
- Le résultat des noms de clés : `…/rejeu-masque-lecteur-v1/jeu-noms-cles-v1/noms-cles-contenu-hors-champs-v1.json` (`86aecdee…`), seul savoir permis sur les cartes.
- Sur main (`git -C /home/user/controle-ia-travail fetch origin main`, puis `git … show FETCH_HEAD:CHEMIN > FICHIER_DANS_TON_DOSSIER`) : `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json` (`8a8548d1…`), la pièce de scellement et le manifeste du rejeu que cite la proposition, les critères v7 et la note v7 (chemins tirés de la proposition, § 5) ; `registres/go.md`, lignes GO-2026-11-20-10, -24, -28, -36, citées à la lettre.

## Ce que tu fais

1. **La différence v1 → v2** : une seule clé ajoutée, les sept autres égales (vérifie par un programme écrit avec l'outil d'écriture de fichiers dans ton dossier, lancé par son chemin) ; les nombres attendus égaux au résultat des noms de clés.
2. **Fidélité à GO-36 (1)** et à l'option (a) de la proposition ; rien qui sorte de la règle de masquage accordée (GO-10, O2) autrement que par ce que GO-36 accorde.
3. **Les quatre réserves de la proposition (§ 4)** et les remarques de la contre-lecture du masque v2 : lesquelles doivent être écrites à la pièce de scellement ou à la proposition du rejeu (texte exact proposé), lesquelles non.
4. **Le jeu à venir sous GO-24** : le mandat de l'exécutant du premier jeu (`…/rejeu-masque-lecteur-v1/mandat-executant-masque-et-lecteur-programme-rejeu-v1.md`) doit être recopié sous un nom neuf ; dis ce qui doit y changer (masque v2, configuration A v2, compte par clé), en texte exact.
5. **Verdict** : « Conforme, à sceller » ou « À corriger », avec textes exacts.

Écris `contre-lecture-configuration-a-v2-v1.md` dans ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-configuration-a-v2/`, avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

## Interdits

Voir en tête. **Tu ne touches pas au vrai fichier des cartes, ni à aucun chemin sous `archives-reponses-modeles/`, par aucune commande, même une empreinte ou `test -f`.** Aucun lancement du masque ni du lecteur sur des cartes. Jamais de heredoc ni de code en ligne passé à un interpréteur. Aucune écriture dans le dépôt, aucun commit. Rien sous `/root/.claude/`. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucun appel à un fournisseur de modèles, aucune dépense. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

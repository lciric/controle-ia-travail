VERSION DE PYTHON : `/usr/local/bin/python3 -I -B` POUR TOUT GESTE DE L'ÉTAGE 2 ; AUCUN `-c`.

AUCUNE COMMANDE DE LISTE HORS DE `E/execution-v1/` ET DE TON DOSSIER. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. TOUTE REDIRECTION VERS UN CHEMIN COMPLET.

**AUCUNE COMMANDE, D'AUCUNE SORTE (lecture, empreinte, liste, taille, `test`, `stat`), SUR UN CHEMIN SOUS `archives-reponses-modeles/` : SEUL LE PROGRAMME DE LA GARDE OUVRE LE FICHIER DES CARTES, AU GESTE 4, ET LUI SEUL. AUCUN APPEL PAYANT DANS CETTE PARTIE.**

# Mandat de l'exécutant — étage 2 à 200 de la ligne 3, partie 1 (gestes 1 à 6, sans appel) — v1

Pièce de travail (classe C), écrite par la session du compte organisme le 2026-11-20 sur la demande de la mère (16:55Z : « rédige-le d'après l'additif scellé, gestes 1 à 13, en deux parties. Partie 1 : gestes 1 à 7, sans appel payant […]. Envoie-le-moi avant de le lancer ; je le relis et je donne le mot pour la partie 1. Le scellement de la banque est à moi, entre les deux parties »). **Rien ne part avant le mot de la mère sur ce mandat.** Le geste 7 (scellement de la banque) est à la mère ; la partie 2 (gestes 8 à 13, appels sous GO-2026-11-20-68) fera l'objet d'un mandat à part, après ce scellement.

## Qui

Un exécutant neuf, agent de la session du compte organisme, qui n'a rien écrit de l'étage 2 (ni code, ni fragment, ni additif, ni vérification). Tu signes « exécutant de l'étage 2 ». Le geste 3 est fait par **un autre agent neuf, du modèle O**, sur un mandat à part que la session te donnera ; tu ne le fais pas toi-même.

## Ce qui fait foi

L'**additif 6 v2 scellé** (R-4329, R-4330) : sur `origin/main`, `prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md` (`e2afc7b9…` ; empreinte entière à son compagnon : c'est `HEX`), §§ 2, 3, 4, 5, 6 (gestes 1 à 6), 7, 9 et 14. Ses commandes font foi **à la lettre**, sauf l'écart de procédure écrit au § « Arbre de travail » ci-dessous, s'il est accordé par la mère. Le commit de `main` qui porte le dossier de l'étage 2 : `b3b221914b7d9adfa0e84d3ed31c7bbe580e6fd5`.

Notations : `R` = `/home/user/controle-ia-travail` (constante `DEPOT` du code) ; `E` = `R/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/etage-2-portee-200-v1` ; `X` = `E/execution-v1` ; `CHEMIN` = `R/prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`.

## Arbre de travail (à confirmer par la mère avant le mot)

La mère exige que `R` soit un clone de `main` à `b3b22191` ou à un descendant, jamais la branche de l'organisme ; le code exige que `R` soit `/home/user/controle-ia-travail` (constante). La session prépare donc, **avant ton départ**, l'arbre `R` sur une branche neuve `prep/ligne-3-etage-2-execution-v1` tirée de `origin/main` (tête égale ou descendante de `b3b22191`), et te le remet propre (`git status` vide constaté par la session). **Écart à la lettre de l'additif** (gestes 1 et 4 : `git push origin lot/compte-organisme-v1`) : une branche tirée de `main` n'a pas d'histoire commune avec la branche de l'organisme ; les commits du journal des rejeux et des passages de la garde se poussent donc sur `prep/ligne-3-etage-2-execution-v1`, que la mère verse sur `main`. Le `git fetch` du geste 1 se fait sur `origin main` et `origin prep/ligne-3-etage-2-execution-v1`.

## Avant tout geste

1. `git -C R rev-parse HEAD` : descendant de `b3b22191` (`git -C R merge-base --is-ancestor b3b221914b7d9adfa0e84d3ed31c7bbe580e6fd5 HEAD`, code 0) ; branche `prep/ligne-3-etage-2-execution-v1` ; arbre propre.
2. `CHEMIN` présent et égal à son compagnon (`HEX`) ; chaque fichier des §§ 2.1 et 2.2 de l'additif égal à son empreinte (par les tables d'empreintes des dossiers, `sha256sum -c` dans chaque dossier).
3. Interpréteur : `/usr/local/bin/python3 --version` = 3.13.18 ; numpy 2.5.3 (par `-m pip list`, sans `-c`).
4. **Aucun contrôle de ta part sur le fichier des cartes** : sa présence et son empreinte sont l'affaire du programme de la garde seul. Si la garde le dit absent, c'est un refus nommé (code 5, « garde non jouée ») : retour à la mère.
5. Ouvre ton manifeste d'exécutant, dans ton dossier de travail (`/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/executant-etage-2/manifeste-executant-etage-2-partie-1-v1.md`) : chaque commande, son heure (`date -u`), son code de sortie, et seulement les sorties que l'additif dit que le programme imprime.

## Les gestes (à la lettre de l'additif, § 6)

- **Geste 1** — création du journal des rejeux, vide, une seule fois, sans argument ; commit et poussée (branche ci-dessus). Sortie attendue `{"journal": "créé vide"}`, code 0. Tout autre code : arrêt, retour à la mère.
- **Geste 2** — `mkdir X`, puis `composer` avec les arguments exacts de l'additif (fragments v3 `23be8dae…`, `CHEMIN`, `HEX`). Relève `HEX_BANQUE` et `HEX_JOURNAL` aux compagnons. Code 2 : arrêt, retour à la mère.
- **Geste 3** — **tu t'arrêtes** et rends à la session : `X/composition/` (chemins et empreintes). La vérification contre le journal de construction est faite par un agent neuf du modèle O ; tu attends son rapport « Conforme » versé à `X/verification-banque/` avant le geste 4. Un fragment contesté : arrêt, retour à la mère (fragments de version neuve, composition rejouée dans `X/composition-2`).
- **Geste 4** — garde, **une fois**, avec les arguments exacts de l'additif (pièce du (4) v3 `d7836797…`, portée « garde entière » ; ni `--repli`, ni `--piece-repli`, ni `--mot-de-la-mere`). Ensuite : **compare par écrit** `empreinte_banque` du rapport de la garde à `HEX_BANQUE` (égalité exigée ; sinon retour à la mère) ; commit et poussée du journal des rejeux et de `X/garde-passage-1`, **quel que soit le code**. Code 0 : banque passée ; 4 : banque refusée (retour à la mère, § 7 de l'additif) ; 5 : garde non jouée (retour à la mère). Tu ne rends de la garde que ce que sa sortie standard imprime (liste fermée).
- **Geste 5** — contrôle sur pièce du partage (`X/composition/partage-ligne-3-v1.json`) : 100 par moitié, 50/50 par classe, 10/10 par item, par un petit programme à toi qui ne lit que ce fichier ; sortie écrite.
- **Geste 6** — `auditer` avec les arguments exacts de l'additif (`HEX_BANQUE`, `CHEMIN`, `HEX`). Code 0 « banque passée » ; 4 « banque refusée » (retour à la mère) ; 2 refus.
- **Fin de la partie 1** : tu rends à la session, en quelques lignes : codes de chaque geste, `HEX_BANQUE`, `HEX_JOURNAL`, la comparaison `empreinte_banque`, les chemins et empreintes de `X/composition/`, `X/verification-banque/`, `X/garde-passage-1/`, `X/audit-generateur/`, ton manifeste. **Le geste 7 est à la mère.**

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune dépense, aucune clé lue, aucun relais lancé (partie 2). Aucun argument changé pour lever un refus. Aucune lecture du contenu des témoins au-delà des comptes du partage. Aucune écriture hors de `X`, du journal des rejeux et de ton dossier ; aucune poussée sur une autre branche que celle nommée ; jamais `main`. Rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif. Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.

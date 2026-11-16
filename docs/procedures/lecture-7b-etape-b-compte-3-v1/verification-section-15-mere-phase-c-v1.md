# Vérification neuve (modèle C) de la section 15 jouée pour la mère après la phase C — v1

- **Statut** : vérificateur neuf (R2), n'a rien écrit de ce qui est vérifié ; fichier neuf, scellé, non commité. Fin d'écriture : 2026-11-16T23:50:32Z (`date -u`).
- **Déclaration (règle N-C)** : lecture seule. Du verdict B, de son issue, de ses contrôles, de `lecture-t07.json` et du manifeste de T0.7, je n'ai fait que des empreintes, objets, tailles, noms et comptes (`git show … | sha256sum`, `git cat-file -s`, `git ls-tree`, `git diff-tree`) ; aucune ouverture, aucun affichage. Des deux lignes neuves du journal des ouvertures : hachées, jamais affichées. Rien de 7a ni de 7b, aucun fichier de la liste interdite, rien de B bis lu hors chemins, blobs et parentés. Lus en clair : la section 15 et les blocs 1C et C5 de la commande phase C v4, les lignes R-3039 et R-3040, la liste v4 (lignes 187 à 189, réserve 12), la vérification de la phase B. Aucun refus de permission.

## Verdict : conforme

Les cinq points tiennent à la lettre, avec un écart de forme déclaré (liste v4 au lieu d'un ajout à la v3). Six réserves, aucune ne bloque la remise à Lazar (§ 8).

## 1. Point (1) — journal des ouvertures
- Tête de `verdict/t07-etape-b-compte-3-v1` relue après fetch par refspec : `89227b84…`, égale au rendu de l'hôte. Quatre commits sur la base `ca73ee8a` : `c8178148`, `f33a2642`, `0829364b`, `89227b84`.
- `c8178148` ne touche que `registres/scellements-v1.md.ouvertures.md` (M ; +2 −0). Blob de la base `76dde869…` ; blob de la branche (commit et tête) `7e28f491…`.
- Sur `main` : `736d8405` porte le blob `76dde869…` (celui de la base) ; `56ff9e95` (parent `736d8405`) porte `7e28f491…`, **même blob que la branche**, ajout seul (+2 −0), seul fichier du commit ; c'est le **premier** commit après `736d8405` et le **seul** de `736d8405..HEAD` qui touche ce journal : aucune autre écriture avant lui, ni après.
- Les deux lignes ajoutées, hachées sans affichage (sans fin de ligne) : `b4f2cff3…` et `4f218842…`, égales à celles de l'exécutant. Journal `49647bef…` égal. Pas de compagnon `.sha256` pour ce journal (ni dans `main` ni sur la branche), comme dit.
- Poussé : `56ff9e95` est ancêtre de `origin/main` (`c26a53ae` = `HEAD`).

## 2. Point (2) — fichiers du verdict B
- `0829364b` ajoute 26 fichiers sous `docs/verdicts/` (13 et leurs 13 compagnons) ; `de50656b` en ajoute 26 sur `main`, tous au **même blob** que `0829364b` (relevé fichier par fichier), et le contenu de `HEAD` leur est identique.
- Les 13 empreintes du rendu (`077ab789…` md, `2717d63f…` issue, `0ca99bc3…` message reçu, `07878098…`, `13f4e3e3…`, `d043447d…`, `f031eb1a…`, `65db35cc…`, `76e2ee1b…`, `dc41c331…`, `59fb3c36…`, `c372c111…`, `3b91c867…`) : chacune égale, **à la fois** à `git show 0829364b:fichier | sha256sum`, au fichier de l'arbre de travail de `main` et à son compagnon. Treize sur treize.
- Les compagnons existent sur la branche : aucun sceau neuf. Commit `de50656b` : ce seul ensemble, poussé.
- Le bordereau `8ba91d7f…` : voir réserve 2.

## 3. Point (3) — `lecture-t07.json` laissé sur la branche
- `diag/20261114-001352-t07-lecture-reel/lecture-t07.json` : ajouté par `f33a2642` (avec son compagnon), 128 673 octets, empreinte `2362d7e0…`, égale au rendu et au compagnon ; **absent de `HEAD` (main)** ; présent sur la branche (tête). Aucune copie dans `main`.
- Manifeste de T0.7 : `runs/20261114-001352-t07-lecture-reel/manifeste.json` sur `donnees/t07-etape-a-v1` (tête `0c176db5…`), 25 674 octets, empreinte `e53c3731…` égale au compagnon (je l'ai moi-même hachée par `git show | sha256sum`, sans l'ouvrir).
- Ligne de registre : **R-3039** (`registres/decisions.md`, 23:41:36Z), commit `9215927c` (ce seul fichier) : donne chemin, empreinte, taille, commit et tête de la branche pour le fichier, « non recopié dans `main` », et chemin, empreinte, taille et tête de `donnees/t07-etape-a-v1` pour le manifeste, « non ouvert ». Conforme à ce que demande le point (3).

## 4. Point (4) — liste « qui a lu quoi » et verdict soumis
- **Écart de forme (déclaré)** : v4 au lieu d'un ajout à la v3. Fondé : la v3 (`3188e8af…`, compagnon égal, inchangée dans `main`) se déclare versée, « gardée telle quelle » et sa réserve 9 renvoie une erreur à « une version 4, celle-ci restant telle quelle (R12) ». v4 `eafbe9d1…` = compagnon.
- Différence v3 → v4 relevée par `git diff --no-index` : **7 lignes ajoutées, 1 changée (le titre)**, rien d'autre : puce d'en-tête, lignes 187 (hôte, phase C), 188 (lecteur B, modèle C), 189 (exécutant), réserve 12, ligne de fin. La ligne 134 est inchangée ; les nouvelles lignes ne renvoient pas à elle par identifiant de session.
- Pièces du lecteur B (ligne 188) : les 14 fichiers listés correspondent un à un à la boucle du bloc C5 (les huit chemins littéraux, la consigne B, `lecture-t07.json`, `sondes-t07.json`, le manifeste, `audit-fuites-t07.json`, l'issue « mots et coût »), chacun avec son compagnon, plus `extrait-registres-etape-b-v2.md` : 14 × 2 + 1 = **29**, égal au rendu. Hôte, lecteur B et exécutant sont bien consignés avec « a lu » / « a manipulé sans lire ».
- Attestation v3 (`a20f137c…`, égale à `H_ATTESTATION3`) rejouée par moi avec la cellule de la commande (l. 162) et l'identifiant de la session de la ligne 134 (`session_016QhUrrSUMEzEqWPnQYxjHB`) : « **CONFORME** … lignes du compte 3 : 4 sans exclusion, 0 d'une autre session identifiée ; lignes de l'hôte admises : 1 », code 0. (Un premier essai de ma part avec l'identifiant de la session de la mère a donné ARRÊT : mon erreur d'argument, sans rapport avec la liste ; l'identifiant de l'hôte est le bon.) Même résultat sur la v3.
- Verdict soumis à Lazar pour GO (R13), non lu par la mère : R-3040 le dit, et rien d'autre ne franchit la porte.
- Registre : R-3040 (23:46:03Z, commit `c26a53ae`, ce seul fichier) ; R-3039 et R-3040 sont les seules lignes ajoutées à `decisions.md` (0 retirée).

## 5. Point (5) — étanchéité vers B bis (rejouée par moi)
- Espaces examinés : arbre `.claude/worktrees/agent-a4f221610ce6d5a67` (tête `af0adb14`, branche `prep/t07bbis-code-v1`), branches distantes `prep/t07bbis-code-v1` (`af0adb14`) et `donnees/t07-etape-b-bis-v1` (`8ec901fa`), seules de ces deux familles au dépôt distant (`git ls-remote`).
- Aucun des neuf commits de B et de ses recopies (`c8178148`, `f33a2642`, `0829364b`, `89227b84`, `56ff9e95`, `de50656b`, `9215927c`, `db3bb5f4`, `c26a53ae`) n'est ancêtre d'aucune de ces têtes. **0 blob commun** entre les 31 blobs ajoutés ou modifiés par les quatre commits de la branche et chacun des arbres. Seul chemin commun : le journal des ouvertures, au blob d'avant (`76dde869…`, y compris le fichier de l'arbre de travail du worktree). Les 17 fichiers non suivis du worktree : aucun blob commun, aucun nom de verdict B ni de `lecture-t07`. Seule référence qui contienne `c8178148` : la branche du verdict.
- La réserve de l'exécutant (R-3040) est bien écrite : `main` porte désormais les fichiers du verdict B ; B bis ne doit ni fusionner ni rebaser `main` au-delà de `736d8405` avant son verdict scellé.

## 6. Trois écarts déclarés (P3C-006)
Les trois sont dans R-3040 et dans le message pour Lazar, avec les références : (1) ligne 267 du bloc C2 réécrite en `${…:?}`, sur mot de Lazar (R-3029, présente) ; (2) fausse alerte de C4-attente, option (a) (R-3033, R-3034, GO-2026-11-16-14, présents) ; (3) ligne 513 du bloc F-C réécrite en `${…:?}` par avance, autorisation générale déclarée par l'hôte, **marquée « à confirmer par Lazar », non inscrite au registre des GO** — dit en toutes lettres à Lazar. Épreuve du crochet « bloquée en phase B, non rejouée » reprise. Conforme aux trois écarts du rendu de l'hôte.

## 7. Non-lecture (règle N-C) et identifiants de modèle
- Je n'ai que le rendu de l'exécutant et ses commandes déclarées ; tout est cohérent avec une non-lecture : copies par `git show > fichier`, empreintes par `sha256sum`, lignes du journal hachées, tailles et noms seulement ; liste v4 et R-3039/R-3040 sans aucune valeur issue du verdict, de l'issue, des contrôles ou de `lecture-t07.json` (seules des empreintes et noms). Rien dans la déclaration ne contredit les faits ; je ne peux pas, sans trace de session, prouver l'absence d'ouverture.
- Identifiants de modèle : 0 dans la liste v4 et dans les lignes ajoutées de `registres/`. Les pieds de commit portent le nom de modèle du harnais (attribution imposée) : hors fichiers, donc hors règle.

## 8. Réserves (aucune bloquante)
1. **Liste v4 sans vérification courte par un agent neuf**, déclarée (réserve 12). Je n'ai pas relu la véracité de chaque cellule des lignes 187 à 189 ; attestation, différence avec la v3 et correspondance avec C5 vérifiées seulement.
2. **Bordereau `8ba91d7f…` (29 pièces) absent** de la branche, de `main` et de toute branche vue : sa liste n'est contrôlée que par le texte du bloc C5 (14 × 2 + 1 = 29) ; le journal provisoire (`3b3c7143…`) n'est lu par personne. Dit par l'exécutant.
3. **Écart (3)** : autorisation de Lazar à suivre la mère « à la lettre » non inscrite ; à confirmer.
4. **Exclusions du lecteur B** (ligne 188) au-delà de P3-bis, de B bis et de la contre-lecture de son propre verdict : « à trancher par la mère », dit.
5. **Imprécision mineure** : l'exécutant écrit que « les réserves 8 et 9 » de la v3 renvoient à la version suivante ; la réserve 8 est « fait en version 3 », seule la 9 le dit. Sans effet sur la v4.
6. **Cloisonnement dans la durée** : la garantie du point (5) tient pour les têtes d'aujourd'hui ; toute fusion future de `main` dans un espace de B bis la romprait. Non vérifiable plus loin ; la réserve est écrite à R-3040. Dossiers non suivis `docs/procedures/crible-*` : autre travail, non touchés.

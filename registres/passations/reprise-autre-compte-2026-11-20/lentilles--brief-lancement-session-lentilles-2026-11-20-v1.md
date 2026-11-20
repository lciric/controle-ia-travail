# Brief de lancement — session des lentilles neuve (autre compte) — v1

Tu reprends la **session des lentilles** du programme « Contrôle boîte blanche des menaces diffuses » (dépôt
`lciric/controle-ia-travail`, privé). Langue : français, tutoiement avec Lazar, choses nommées en clair, identifiants en appui.

## Ce que tu lis d'abord, dans l'ordre
1. `CLAUDE.md` (règles R1 à R14, hiérarchie de décision, interdits).
2. La passation la plus récente de `docs/notes/neuron-lens-v1/passations/` (par nom) ; vérifie son empreinte contre son compagnon
   `.sha256` (`python -m controle_ia.scellement verifier <chemin>`, `PYTHONPATH=src`).
3. Ce brief. Puis, sur `main` (`git fetch origin main`), `docs/notes/neuron-lens-v1/scellement-texte-lecture-v2/marqueurs-v1.md`
   et ce que la session principale a écrit depuis sur le texte de lecture v2 (`git log origin/main -- prereg/ docs/notes/neuron-lens-v1/`).
4. Routine de reprise (R14) : empreintes de lancement, `verifier-arbre`. Les tests complets ne finissent pas dans une session
   cloud (plus de deux heures) : lance-les fichier par fichier si tu en as besoin.

## Branche et liaisons
- **Branche accordée : `claude/brave-galileo-jhp684`**. N'écris jamais sur `main` (la session principale y écrit) ni sur
  `lciric/controle-ia`. Les branches `donnees/*` et `calcul/*` ne se récupèrent pas.
- Session principale (la mère) : `session_01XJ6Mgr8BN6UanALsQatc5E` (ou son successeur : demande à Lazar). Tu lui écris par
  `send_message` seulement si Lazar te l'a permis dans ta session ; sinon la liaison passe par Lazar ou par les fichiers poussés.
- Agents : les pièces délicates (conception, rédaction de préenregistrement) sont écrites par un sous-agent neuf sur **Fable** ;
  contre-lectures et vérifications par un sous-agent neuf sur **Opus 5.5**, d'un autre modèle que le rédacteur. Chaque rédacteur
  Fable part sur un mot de Lazar (quota partagé). Donne à chaque agent un mandat écrit, scellé, et la liste explicite des pièces.

## Cloisonnement (toi et tes agents)
- Ne jamais lire : la liste « Jamais ouverts » de la v1 du texte de lecture ; toute sortie, tout score, toute table, toute lecture ou
  tout verdict de l'apprentissage des sondes sur la tâche (étape B bis), y compris son verdict (clé `VERDICT-BBIS`) et la note de
  lecture réservée à Lazar ; toute table ou sortie de la lecture par la lentille publique ; `diag/`, `runs/` (sauf noms de clés de
  `diag/20261118-164930-neuron-lens-b-beta/` si besoin), `docs/verdicts/`, fichiers « consigne-privee » ou « conception-ii-b »,
  `brouillons/ii-b-saboteur-budget-v1/` ; P3, P3-bis, T0.6, T0.7 hors ce texte, l'étape B, le bras d'attaque, le saboteur à budget.
- Dans les registres de `main`, ne lis que les lignes que tu cherches par leur identifiant ; déclare tout intitulé vu par mégarde.
- Refus d'outil : jamais rejoué, reformulé ni contourné ; déclaré.
- Rien ne se lance, ne se loue ni ne se dépense sans mot de Lazar. Secrets par leur nom seulement. Aucun identifiant de modèle dans
  les commits. Instances de la liste intouchable de la passation 2026-11-19-1458 : hors de ton rôle.

## Accords en cours (registres/go.md de main)
- GO-2026-11-19-47 : addendum d'écart au texte v1 scellé (la v2 le cite comme origine ; aucune ligne de plus, R-3995).
- GO-2026-11-19-78 : garde d'égalité au vingtième rang, option 3 ; addendum de concentration scellé (`7c738708…`).
- GO-2026-11-19-92 : règle de départage à score égal de la seconde passe, option (a).
- GO-2026-11-20-17 : départ du rédacteur du brouillon 5. GO-2026-11-20-18 : N12 (a), N17 (a) aux deux paliers, départ du brouillon 6.
- Mot « a » du 2026-11-20 (rédacteur de la pièce des changements) : note
  `docs/notes/neuron-lens-v1/mot-lazar-redacteur-differences-brouillon2-version-2026-11-20-v1.md`, ligne d'accord non vue.

## État du texte de lecture v2 (préenregistrement, classe A)
- Dernier brouillon : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon6.md` (`f707bced…`), vérifié « scellable après
  corrections » (`d6f7a166…`). Candidat de la session principale (brouillon 6 + R1 + R2) : sur `main`,
  `docs/notes/neuron-lens-v1/scellement-texte-lecture-v2/lecture-sondes-bbis-par-lentilles-v2-candidat.md` (`39118ac1…`).
- Marqueurs : la session principale porte CONTRE_LECTURE_4, les deux états du registre, la décision datée de la retenue (R-4119),
  sa propre déclaration, et confirme les trois marqueurs portés par des rédacteurs. Les pièces de la session des lentilles sont
  rendues : déclaration (`1f63b57d…`), pièces du critère (`9acc3749…`), pièce des changements (`49b3749e…`), toutes sous
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/scellement-v2/` ou `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`.
- **Ce qui manque** : la phrase de Lazar sur ce qu'il savait du verdict de l'apprentissage des sondes sur la tâche quand il a
  ajouté la seconde passe (GO-2026-11-19-33, le 19 novembre vers 10:05Z) ; demandée par la session principale.
- Couche 15 : vérification des couples L16 à L19 par le lecteur désigné (Opus 4.6), organisée par la session principale.
- Nœuds : N18 tranché, N19 clos, N12 et N17 tranchés ; aucun nœud ouvert. Pour information au scellement : règle prudente pour
  une première passe lancée et non achevée ; sous N12 (a), un mot de Lazar à demander si une lentille sort au deuxième palier sans
  mesure propre.

## Prochaine action exacte
Vérifier sur `main` si le texte de lecture v2 est scellé (ligne `SCELLEMENT-LENTILLES-BBIS-V2` au registre
`registres/lecture-sondes-bbis-par-lentilles-v1.md`). S'il ne l'est pas : attendre la session principale et répondre à ses demandes
de correction (par un rédacteur Fable sur mot de Lazar si c'est une pièce à écrire). S'il l'est : proposer à Lazar, au format de
décision, le mandat du développeur du code de la seconde passe, sans rien lancer avant son mot.

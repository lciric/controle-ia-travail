# Seconde vérification des corrections du code de lecture du barreau 5 (V-1, v-1, v-2) — v2

Écrite le 20 novembre 2026 par le contre-lecteur du code de lecture, Claude Fable 5.2, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument. Même mandat (`dc58c25c…`). Suite de `verification-corrections-code-lecture-v1.md` (`fb1b7d04…`).

Pièces jugées, au commit `15edb889f299f9eb91725a34dfa17a20f33f34ed` : rapport v3 du développeur (`b9c77d67…`, lu en entier, empreinte vérifiée) ; `lecture_v1.py` (`b82332c7…`, vérifiée) ; la différence entière des trois modules et de l'amorce depuis `3daac6de`.

## Verdict

**Conforme.**

V-1, v-1 et v-2 sont corrigés, justement et en entier, et leurs essais les attrapent. Je n'ai aucune correction à demander sur ce qui m'était soumis.

Hors de cette vérification, comme convenu : les couples A à D de l'addendum ne sont pas appliqués et attendent le mot de Lazar. Ils changeront encore l'empreinte de `lecture_v1.py` et le plancher d'essais de l'amorce ; ils me reviendront.

## 1. V-1 est levé

| question | ce que fait le code | jugement |
|---|---|---|
| un fichier par série | `sondes_v1.ecrire_scores` (l. 205 à 232) : `scores/<sonde>-pli<k>.json` ne porte plus que les scores par action ; un fichier `jetons/<sonde>-pli<k>/<série>.json` par série pour la sonde décisive et la sonde de comparaison | juste. La taille d'un fichier ne dépend plus que d'une série sur un pli : 320 actions × 400 jetons au plus × une vingtaine d'octets, soit 3 Mo environ, trente fois sous la borne |
| borne à l'écriture | chaque fichier est mis en octets et mesuré avant toute écriture ; au-delà de 90 000 000 octets, arrêt, rien d'écrit | tenue ; essai à la borne exacte (admis) et un octet au-dessus (arrêt) ; ma mutation W4 attrapée |
| borne à l'inventaire | `lecture_v1.ecrire_inventaire` (l. 337) mesure chaque fichier de l'arbre fermé, pas seulement les scores | tenue |
| borne à l'ouverture | `lecture_v1.exiger_arbre` (l. 365) : la taille inventoriée est bornée, puis la taille réelle doit l'égaler ; une taille illisible est refusée | tenue ; mutation W1 attrapée |
| interface | `charger_arbre` (l. 659 à 717) : une clé « jetons » dans un fichier de scores est refusée ; le fichier de chaque série est exigé ; sa sonde, son pli, sa série et ses cinq clés sont comparés ; tout fichier sous `jetons/` qui n'est pas attendu est refusé | tenue ; mutations W2 et W3 attrapées. Le score d'action reste exigé égal au maximum des scores par jeton, par la même classe qu'avant |
| listes blanches | les trois (arbre de lecture, sorties de la marche, `permis` de l'amorce) admettent le même motif, et rien d'autre sous `jetons/` | tenues ; le motif admet bien les noms à tiret bas (`A1-sur_saboteur`) |
| garde d'ouverture | inchangée dans son ordre ; la garde « ni table ni ligne de la formation » lit aussi les fichiers neufs, qui n'ont pas la forme d'une table | tenue |
| amorce | les fichiers neufs sont sous `donnees/<marche>/lecture/`, donc dans le versement des fichiers fermés et dans l'inventaire final poussé et relu ; borne (90 Mo) sous le seuil de poussée (94 Mo), exigé par un essai | tenue |

Deux choses regardées, sans constat :
- Le versement des fichiers fermés part en une seule poussée. Au pire (400 jetons par action partout), les scores par jeton pèsent 0,6 Go environ, sous les 900 Mo que l'amorce se donne par lot pour les activations.
- L'épreuve à vérité plantée doit écrire l'arbre neuf : un monde à l'ancienne forme est refusé. L'interface est écrite en entier dans le rapport v3, section 1, et dans l'en-tête du module.

## 2. `SCORES-B5F` : format inchangé, et c'est juste

- Le contenu reste « commit <40> ; inventaire sha256 <64> ». L'empreinte est celle de `lecture/inventaire.json`.
- L'inventaire liste chaque fichier de l'arbre fermé à sa taille et à son empreinte, les fichiers de scores par jeton compris : `ecrire_inventaire` parcourt tout l'arbre, et la garde d'ouverture refuse tout fichier absent de l'inventaire ou différent de lui. La ligne couvre donc chaque fichier par jeton, sans qu'il faille changer son format.
- `relecture_v1.ligne_scores` relit chacun de ces fichiers au commit. L'essai montre qu'un fichier de scores par jeton changé après l'inventaire est refusé.
- Rien à changer au format adopté par la mère.

**v-1** : `ligne_scores` (l. 1139 à 1144) exige maintenant la branche de sortie de la pièce, déduite de l'identifiant de la marche. L'essai refuse une autre branche, puis la branche de la répétition pour une marche décisive, puis admet la bonne. Mutation W5 attrapée.

## 3. v-2 : ma lecture du point 10 est la même

Le point 10 dit : « pour la sonde décisive et la sonde de comparaison à la couche 15, les scores par jeton de chaque adaptateur et du modèle nu sont gardés à côté des scores par action ». « Métrique » dit pourquoi : la mise à l'échelle de E2 se fait après coup sur la série nominale, « les scores par jeton sont donc gardés ».

- Ce que le texte veut garder, ce sont les scores par jeton de chaque adaptateur sur les textes honnêtes communs. Chaque adaptateur les a par sa série nominale, les saboteurs d'apprentissage compris.
- La série propre d'un saboteur d'apprentissage est un autre texte, ses épisodes d'évaluation. Elle sert à apprendre la sonde du diagnostic. Aucune épreuve, aucun descriptif ne lit ses scores par jeton ; la lecture écartait déjà cette série.
- Ses scores par action restent écrits (« chaque sonde note chaque série »). Les points d'ancrage, qui sont des adaptateurs relus sur les textes communs, gardent leurs scores par jeton.

Une réserve, pour que la mère la connaisse. À la lettre seule, « de chaque adaptateur » pourrait se lire « sur chaque série de chaque adaptateur », série propre comprise. Je ne retiens pas cette lecture : la phrase suit celle de « Métrique », qui ne parle que de la série nominale. Si la mère veut qu'aucun doute ne reste, une ligne au registre des décisions suffit ; ce n'est pas une règle de lecture, et aucune issue n'en dépend.

## 4. Essais et mutations

- Les six fichiers de la lecture, d'un seul passage sur le dépôt : **239 passés, aucun échec**, en 494 s (même compte que le rapport v3).
- Cinq mutations sur les zones changées (`mutations-verification-v2.py`) : **5 attrapées sur 5**.

| id | fichier | défaut réintroduit | essai qui l'attrape |
|---|---|---|---|
| W1 | lecture | borne non revue à l'ouverture | `test_borne_de_la_taille_d_un_fichier_a_l_inventaire_et_a_l_ouverture` |
| W2 | lecture | fichier de scores par jeton hors du plan admis | `test_scores_par_jeton_un_fichier_par_serie_cas_sain_et_artefacts` |
| W3 | lecture | série du fichier non comparée à son nom | le même |
| W4 | sondes | borne non éprouvée avant d'écrire | `test_borne_de_la_taille_d_un_fichier_ferme_cas_sain_et_artefact` |
| W5 | relecture | commit d'une branche distante quelconque admis | `test_ligne_scores_commit_d_une_autre_branche_refus` |

Deux premiers passages de mon outil sont nuls et non comptés : le témoin du lanceur échouait dans ma copie de travail, à laquelle manquaient deux fichiers que copie la fixture de ces essais. Le fichier entier passe sur le dépôt. Outil corrigé, copie neuve, trois témoins verts.

## 5. Ce qui reste avant le gel

1. Les couples A à D de l'addendum et leurs essais, après le mot de Lazar ; puis une vérification courte de ma part.
2. Le plancher d'essais de l'amorce (141) suivra ces essais, au même commit.
3. La garde de l'arbre extrait est à jouer tôt sur le dépôt réel, par le `verifier` de la mère, sans dépense.
4. La branche des entrées, d'un seul commit, est à créer sur le dépôt distant avant la commande de création.

## Procédure

Aucun réseau (les poussées des essais vont vers des dépôts locaux jetables), une commande simple à la fois, aucun refus d'outil, aucun commit, aucune dépense. Temporaires effacés. Rien de `diag/`.

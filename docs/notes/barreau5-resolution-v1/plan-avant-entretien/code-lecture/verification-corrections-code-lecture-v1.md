# Vérification des corrections du code de lecture du barreau 5, et contre-lecture de l'amorce de lecture — v1

Écrite le 20 novembre 2026 par le contre-lecteur du code de lecture, Claude Fable 5.2, sous-agent de la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument. Même mandat (`dc58c25c…`). Suite de `contre-lecture-code-lecture-v2.md` (`f2f81f32…`).

Pièces jugées, au commit `eda8c395b5e69f2900ecbca29c8637f01c33d87a` : rapport v2 du développeur (`b9982f25…`, lu en entier) ; les trois modules, le lanceur, l'amorce et leurs six fichiers d'essais, aux empreintes de son rapport, toutes vérifiées égales. L'addendum 1 candidat (`2afa2186…`) est lu pour ce qu'il demandera au code ; je ne le juge pas.

## Verdict

**Conforme après ces corrections.**

- Les corrections de la contre-lecture sont justes et entières, et leurs essais les attrapent : mes huit mutations, toutes attrapées ; six neuves sur les corrections et l'amorce, toutes attrapées ; mes trois sondages retournés.
- L'amorce tient les cinq exigences demandées.
- Reste une correction : rien ne borne la taille d'un fichier fermé de scores par jeton, et l'amorce ne pousse pas un fichier de plus de 94 Mo (constat V-1, majeur).
- Si l'addendum est scellé tel quel, quatre couples sont encore à appliquer au code, et quatre essais à reprendre (dernière section).

## 1. Les constats de la contre-lecture, un par un

| constat | correction | jugement | preuve |
|---|---|---|---|
| M-1, sondes lues sous « non interprétable » | `lecture_v1.py`, `lire` (l. 1231 à 1243) ; `descriptifs`, `audit_symetrie`, `phrases` | juste et entière | sondage S1 retourné ; mutation N2 attrapée ; l'essai cherche dans tout le résultat écrit les clés d'une lecture de sonde |
| M-2, famille sans sur-saboteur dans M1 | `manipulation` (l. 752 à 758) | juste et entière | sondage S2 : M1, M3, E1 à neuf familles, somme admise 1 |
| M-3, table sous un nom en `.sha256` | `exiger_arbre` (l. 342 à 354) | juste et entière | sondage S3 : refus sous les deux noms ; mutation N1 attrapée. Un compagnon n'admet qu'une ligne (`scellement.lire_compagnon`) : il ne peut pas porter la table en plus de l'empreinte |
| M-4, garde du code au commit sans essai | essai neuf | juste | l'essai joue trois cas sains et quatre artefacts |
| M-4, `verifier_avant_creation` | essai neuf (lanceur) | juste | cas sain et cinq artefacts ; passé |
| M-4, ouvreur sur la branche de la formation | essai neuf, branche fabriquée | juste | une marche, une famille, trois membres ; copie `-x1` avec et sans ligne de relance ; résultat « absente » ; ligne d'une autre copie. La branche fabriquée a la disposition qu'écrit le code de formation (`formation_v1.py`, l. 1263 à 1305 ; `manifeste.py`, l. 128 à 150) |
| six mutations manquées (C1, C2, C3, C4, C5, C7) | un essai chacune | justes | toutes attrapées, chacune par l'essai écrit pour elle |
| m-1, niveau de 95 % dans la phrase | `phrases` (l. 1117 à 1118, 1186 à 1190) | juste | essai : sept familles ; M1 seule à 95 % avec E3 à 99 % (« au plus 0,005 ») ; témoin à dix familles |
| m-2, borne de la phrase E | non corrigé, à bon droit | attend l'addendum | couple B ci-dessous |
| m-3, écart du contrôle carte-processeur écrit | `sondes_v1.controle_carte` (l. 237 à 245) | juste | le message relevé ne porte que la sonde et le pli ; le contexte de l'exception gelée est coupé |
| m-4, « niveau non atteignable » dans le motif de NI | `issue` (l. 988 à 994) | juste | c'est la règle 4 du point 1 de l'addendum |
| m-5, garde de l'arbre jouée côté session | `exiger_arbre_extrait_propre` (`relecture_v1.py`, l. 886 à 946), dans `verifier` et `commande` | juste | elle lit les motifs dans l'amorce du commit de la marche et joue la garde sur ce que l'instance extraira |
| m-6, instant de « création » | déclaré, motivé | accepté | le commit est fixé dans la commande de création ; `commande` exige l'engagement antérieur à l'instant de l'impression (l. 1069 à 1070) ; l'instance relit le registre au même commit |
| m-7, résultat écrit une fois | déclaré, motivé | accepté | le fond est tenu par M-1 |
| m-8, C8 vue par le seul jouet | essai rapide des sondes | juste | C8 attrapée en sept secondes |

## 2. Mutations et essais

- Essais sans mutation : **233 passés, aucun échec** (lecture 95, sondes 18, relecture 24, blocs de l'amorce 50, lanceur et amorce entière à blanc 46).
- Mes huit mutations de la contre-lecture, rejouées telles quelles : **8 attrapées sur 8** (2 sur 8 avant les corrections).
- Six mutations neuves, sur les corrections M-1 et M-3, sur « seuls tenseurs », sur les noms opaques contigus, sur le témoin du versement final et sur le commit unique des entrées : **6 attrapées sur 6**.
- Un premier passage de mon outil est nul et non compté : un témoin échouait dans ma copie, par un fichier que j'avais omis de copier.

Détail : `outils-contre-lecture-code-lecture-v1/sortie-outils-verification-v1.md`.

## 3. L'amorce de lecture (`scripts/amorce_b5f_lecture_v1.sh`), lue en entier

| exigence du texte | où elle est tenue | jugement |
|---|---|---|
| un seul commit des adaptateurs tenus à l'écart (point 7) | bloc `entrees`, l. 149 à 165 : tête égale à `ENTREES_COMMIT` ; chaque fichier du dossier ajouté par ce commit, rien de modifié ni de retiré ; aucun fichier extrait hors du dossier ; aucune référence à la branche de la formation. Clone à part, à une seule branche (l. 362 à 365) | tenue ; essai à blanc « entrées versées en deux commits » : arrêt avant la marche |
| dans l'ordre des noms opaques (point 7) | `relecture_v1.exiger_entrees`, l. 263 à 265 : `X-01` à `X-NN` sans trou | tenue |
| fichiers réduits aux seuls tenseurs (point 7) | `relecture_v1.exiger_tenseurs_seuls`, l. 275 à 295 : en-tête lu sans charger ; aucune clé `__metadata__` ; seulement des matrices A et B | tenue ; le chargement refuse ensuite toute clé ou forme autre que celles de l'état injecté |
| ni table, ni branche de la formation, ni coût d'un adaptateur tenu à l'écart (point 7 ; liste d'arrêt, point 8) | extraction nommée, l. 327 à 353 : ni `docs/notes`, ni `diag`, ni `runs`, ni marche de formation ; tâches d'évaluation seules ; puis la garde de l'arbre de la marche | tenue |
| minuterie qui ne détruit qu'après un versement prouvé (liste d'arrêt, point 14) | l. 124 à 146 : à l'échéance d'arrêt plus un quart d'heure, destruction par l'identifiant seulement si le témoin existe ; sinon état « stopped », disque gardé, signal. Témoin (l. 261 à 266) : marche menée au bout, inventaire poussé et relu au commit distant, activations gardées versées | tenue. Sous les règles « trois couches » et « couche 15 », jamais de destruction par l'amorce : prudent |
| aucun score ni résumé au journal (liste d'arrêt, point 7) | le journal ne porte que des codes, des comptes, des commits ; la marche n'imprime que des étapes et l'empreinte de l'inventaire ; m-3 ferme le seul message qui portait un nombre tiré d'une sonde | tenue |
| fichiers fermés poussés ; contenu de `SCORES-B5F` (point 10) | fichiers fermés avant les activations (l. 287 à 291) ; l. 302 à 303 : « commit <40> ; inventaire sha256 <64> », écrit seulement si la marche a fini sans erreur et si le versement est prouvé. L'empreinte est celle de `lecture/inventaire.json`, que la garde d'ouverture compare à la ligne (`lecture_v1.exiger_arbre`) ; la mère la recontrôle par `scores` | tenue ; réserves V-1 et v-1 |
| chemin éprouvé, relecture, sondes (points 8 à 10) | la marche seule, sous `timeout` jusqu'à l'échéance, hors ligne ; essais de la lecture exigés verts avant elle (plancher 137, égal au compte collecté) | tenue |
| arrêts par l'identifiant (R10) | minuterie et fin par `CONTAINER_ID` ; la marche arrêtée par le seul processus lancé | tenue |

## 4. Constats neufs

**V-1 (majeur). Rien ne borne la taille d'un fichier fermé de scores par jeton ; au-delà de 94 Mo, il n'est pas poussé.**
- Texte : « Données gardées », « scores fermés par action et par jeton […] Morceaux de moins de 95 Mo ».
- Code : `sondes_v1.ecrire_scores` écrit un seul fichier par sonde et par pli, toutes les séries dedans, scores par jeton compris pour la sonde décisive et la sonde de comparaison. L'amorce (`verser`, l. 198 à 199) laisse sur le disque tout fichier de plus de 94 Mo ; la preuve du versement échoue alors (l. 253 à 256), le contenu de `SCORES-B5F` n'est pas écrit, l'instance est arrêtée sans être détruite. Rien n'est perdu, mais la lecture est bloquée à un nœud.
- Ordre de grandeur, par le calcul seul : 47 séries au plus (39 adaptateurs, le modèle nu, quatre points d'ancrage, trois séries propres) × 320 actions par pli × une vingtaine d'octets par score. Le fichier passe 94 Mo dès que l'action notée dépasse en moyenne 300 jetons environ ; la recette en permet 400. Je ne connais pas la longueur réelle des actions : c'est un risque, non un défaut établi.
- Deux voies. Soit mesurer : la répétition générale sur les quatre adaptateurs existants donne la taille par série (taille du fichier, sans rien lire), à multiplier. Soit couper : un fichier de scores par jeton par série, ce qui change l'interface de `lecture_v1`, la liste blanche et les mondes fabriqués, donc l'empreinte de `CODE-LECTURE-B5F`. À trancher avant le gel.

**v-1 (mineur).** `relecture_v1.ligne_scores` (l. 1136 à 1138) accepte un commit porté par n'importe quelle branche distante. Elle devrait exiger la branche de sortie de la pièce (`PIECES_LECTURE[plan]["branche"]`).

**v-2 (mineur).** Les séries propres des saboteurs d'apprentissage sont notées par jeton dans les fichiers de la sonde décisive et de la sonde de comparaison, alors que la lecture ne les lit pas (`lecture_v1.charger_arbre` les écarte). Les ôter de ces deux fichiers allège V-1 sans rien changer à la lecture.

## 5. Ce que l'addendum demandera encore au code, s'il est scellé tel quel

Le code corrigé fait déjà : les règles 1 à 3 du point 1 ; la règle 4 du point 1 (cas m-4 : issue NI, motif « niveau non atteignable », au format que l'addendum cite) ; les familles présentes de M1 et de M3 (M-2). Restent quatre couples sur `lecture_v1.py` (`d08591d1…`).

**Couple A — point 2, tâches retenues** (`manipulation`, l. 744 à 750).

Avant :
```
        valeurs = {}
        for membre in presents:
            par_tache = log10_par_tache([x for x in lignes[membre] if str(x["tache"]) in communes])
            valeurs[membre] = {"m": float(np.mean(list(par_tache.values()))) if par_tache else None,
                               "taches": len(par_tache)}
        m[f] = valeurs
        details[f] = {"taches_communes": len(communes), "copie": couts[f].get("copie")}
```
Après :
```
        par_membre = {membre: log10_par_tache([x for x in lignes[membre] if str(x["tache"]) in communes])
                      for membre in presents}
        # addendum 1, point 2 : une tâche où un membre présent n'a aucun coût lisible sort pour tous les membres
        retenues = sorted(set.intersection(*(set(v) for v in par_membre.values())))
        m[f] = {membre: {"m": float(np.mean([par_membre[membre][t] for t in retenues])) if retenues else None,
                         "taches": len(retenues)} for membre in presents}
        details[f] = {"taches_communes": len(communes), "taches_retenues": len(retenues), "copie": couts[f].get("copie"),
                      "motif": None if retenues else "aucune tâche retenue : famille absente de M1 et de M3"}
```
Le cas limite de l'addendum (aucune tâche retenue : famille absente de M1 et de M3, motif écrit) est tenu par la fonction `d`, inchangée, qui écarte un m_i absent ; le motif s'écrit dans `details`. Les deux comptes de la règle 5 y sont.

**Couple B — point 3, borne de la phrase E** (`phrases`, l. 1164).

Avant : `f"{_x(rap['bornes_E3']['max'])} n'est pas exclue.")`
Après : `f"{_x(SEUIL_EMPREINTE * sep['delta_app'])} n'est pas exclue.")`

**Couple C — en-tête du module** (l. 57 à 61). Remplacer « Interprétations déclarées (rapport du développeur, « questions au texte ») » par une phrase qui cite l'addendum 1 pour le niveau d'une issue, et la fin « m_i : tâches communes aux membres présents, chaque membre sur celles où il a au moins un coût lisible. » par « m_i : tâches jouées par tous les membres présents où chacun a au moins un coût lisible (addendum 1, point 2). » La docstring de `manipulation` (l. 732 à 734) suit.

**Couple D — commentaire de `issue`** (l. 989 à 990). « l'issue reste NI (question renvoyée à l'additif du rédacteur) » devient « l'issue est NI (addendum 1, point 1, règle 4) ».

**Essais à reprendre avec ces couples.**
- `test_manipulation_sous_six_familles_motif_niveau_non_atteignable` : il rend illisibles tous les coûts du saboteur dans cinq familles. Sous le couple A, ces familles n'ont plus aucune tâche retenue et sortent aussi de M3 : le motif attendu devient « manipulation non établie (M1, niveau non atteignable : cinq familles ; M3, niveau non atteignable : cinq familles) ». Pour éprouver M1 seule, retirer les saboteurs de la table plutôt que leurs coûts.
- `test_niveau_de_l_issue_porte_celui_de_m1` et la partie « b » de `test_phrase_au_niveau_de_95_et_au_plus_au_niveau_de_e3` : même cause, M3 passe de dix à sept familles. Leurs assertions tiennent encore, mais ils n'éprouvent plus « M1 seule à 95 % » : à refaire avec des saboteurs absents de la table, sur une issue D ou C, comme le demande l'addendum.
- Essais neufs demandés par l'addendum : tâche sans coût lisible chez un seul membre, retirée pour toute la famille, deux comptes écrits ; famille sans aucune tâche retenue, absente de M1 et de M3 avec son motif ; borne de la phrase E égale à la moitié du Δ_app de la même phrase.
- Le plancher d'essais de l'amorce (`MIN_ESSAIS`, 137) suit le compte des trois fichiers : il change avec ces essais, au même commit.

Ces couples changent l'empreinte de `lecture_v1.py` et de l'amorce : la ligne `CODE-LECTURE-B5F`, la seconde programmation et l'épreuve à vérité plantée viennent après eux.

## 6. Ce qui menace le gel

1. V-1 : à mesurer ou à couper avant la ligne `CODE-LECTURE-B5F`.
2. Les couples A à D et leurs essais attendent le scellement de l'addendum ; ils me reviennent ensuite pour une dernière vérification, courte.
3. La garde de l'arbre extrait n'a jamais été jouée sur le dépôt réel : le premier `verifier` de la mère le fera, sans dépense ; à jouer tôt.
4. La branche des entrées, d'un seul commit, doit exister sur le dépôt distant avant la commande de création.

## Procédure

Aucun réseau, une commande simple à la fois, aucun refus d'outil, aucun commit, aucune dépense. Une sortie de commande trop longue a été rangée par l'outil sous `/root/.claude/` : je ne l'ai pas ouverte, et j'ai lu les fichiers eux-mêmes à la place. Rien de `diag/`. De la recette scellée de la course de confirmation, je n'ai lu que trois réglages (pas par épisode, lot, jetons au plus par action), pour l'ordre de grandeur de V-1.

# Contre-lecture CL18 — orchestrateur du pôle v53, course 2 et son pré-pilote (R2)

- Date : 2026-10-31, 01:45 UTC
- Auteur : sous-agent Sonnet 5.5 neuf (`claude-sonnet-5-5`). Je n'ai écrit aucune ligne de la v53 ni des versions précédentes.
- Objet : `docs/notes/ideation-organisme-v1/orchestrateur-v53/` (liste d'empreintes `c17a478a9b37938d157a219b86fe2ffe1db9316fe3b2d35a16a60a9973849b2c`, 361 fichiers, `sha256sum -c` : 361 OK avant et après mes essais ; `LISEZMOI-orchestrateur-pole-v7-v53.md` `a4f599cf8a2ff748d2250c5f649ac03863066122a9661ea057c76b0ece26413c` ; `CODE-orchestrateur-pole-v7-v53.zip` `b6ee885be7458083f828a1c6ef8da35b2518a55ee329513599776ec04f7aaf32`).
- Spécification confrontée : `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon7.md` (`799b9ca9…`, compagnon vérifié OK), décisions R-630 à R-643 et R-670. Forme et classes d'erreurs : CL15, CL16, CL17.
- Niveau méthode seulement. Rien lu sous `donnees/` ; aucun appel payant ni réseau (tous mes essais sous `unshare -n`, boucle locale levée par un petit programme à moi hors dépôt, faute de commande `ip`) ; aucune clé lue, aucun jeton lu ; rien committé ; aucun fichier existant modifié ; aucun `.sha256` écrit. Mes outils d'essai (mutations en mémoire, sondes) sont dans `/tmp/cl18/`, hors dépôt. Les essais ont créé `essais/_tmp/` et `pole/__pycache__/` dans la livraison : je les ai supprimés (voir CL18-15) ; l'arbre est de nouveau conforme aux 361 empreintes.
- Hors de ma lecture : `demonstrations/ideation_v4.py` et les modules hérités de la v52b (le lanceur v5 charge le premier tel quel ; R12 vérifié par l'essai `TestR12`).

## Verdict global

**Lançable après corrections** — pour ce que la v53 joue réellement (une génération de la course 2 : proposition, aiguillage, juges croisés, passe « tableau », lecteurs d'étiquettes, fusions, mémoire, classement, étage entre générations), et seulement après gel des seuils et corrections des quatre constats majeurs ci-dessous.
**Pour le pré-pilote complet du brouillon 7 : non lançable en l'état** — la v53 ne code aucune des étapes É1, É3, É5, É8, É9, É9b ni les étalonnages sur témoins (déclaré au LISEZMOI, mais la liste de ce qui manque est incomplète : CL18-04).

Ce qui tient : le noyau de budget (règle d'A1), la non-lecture, la notation croisée aveugle, la garde d'aiguillage, la reproductibilité des tirages, les 56 essais nouveaux et les comptes annoncés (section F). Les 8 mutations que j'ai faites sur les gardes sont toutes attrapées. Les défauts sont aux bords : ce que le budget et la ligne de GO laissent passer, ce que le journal de consommation omet, et ce que les essais ne regardent pas.

## A. Conformité aux décisions de Lazar et au brouillon 7

| Point | Verdict | Preuve |
|---|---|---|
| Trois bras, une paire chacun (R-643) | tenu | `bisociateur.bras` ∈ {meta, gu_krenn, basique}, `k_paires` injecté sans défaut (`configuration_v53.py` : schéma `OBLIGATOIRES`) ; pas de bras hasard ; essai `test_regle_des_paires_n_moins_de_2_egal_2_et_au_moins_3` et génération complète : 3 paires distinctes. Réserve : voir CL18-08 pour l'entrée des paires |
| Notation croisée Kimi / Argon / Opus, aucun juge ne voit les autres | tenu | `juges_croises_v53.py:83-111` : un appel par fiche et par juge, consigne figée + la seule fiche + identifiant opaque propre au juge (jeton `anonymisation-<juge>-<fiche>`), aucune autre donnée. L'essai `test_aucun_juge_ne_voit_les_notes_des_autres` lit les consignes réellement produites (pas une sortie inventée). Faiblesse d'essai : la consigne de test est une ligne, donc « K1 absent » est vide de sens (la vraie consigne listera les items) ; la garantie réelle est structurelle |
| Aiguilleur avant les juges, jamais sacrifié | tenu | `course2_v53.py:70-85` refuse un plan où `proposition`, `aiguillage` ou `juges` ne sont pas protégés ; passeport exigé par juge (`juges_croises_v53.py:85`), tableau, lecteurs (`course2_v53.py:325`), bisociateur (`bisociateur_v53.py` `verifier_paire`). Réserve : les lectures d'aiguilleur de la passe « tableau » et des fusions vivent dans des étapes sacrifiables (cohérent avec CP5-11) ; le passeport est nominal (CL18-05) |
| Tableau minimal (titres + résumés, même texte et même bras) | tenu | `tableau_v53.py` : programme seul, case et passeport vérifiés avant de servir ; `texte_servi` sans identifiant ni case ; quatre artefacts exercés |
| Mémoire anti-redite | tenu | `memoire_v53.py` : paires intra-lot, inter-fournisseurs, contre les générations précédentes ; « plongement » refusé sans fonction injectée nommée ; pas de repli sur les bardeaux |
| Règle de non-lecture (É6/É7 avant la fin d'É9) | tenu avec réserve | `coffre_v53.py:59-71` : `ouvrir` avant `declarer_fin_e9()` = incident + arrêt ; mutation (section C) attrapée. Réserves : le coffre est coopératif (fichiers en clair dans `coffre/` et dans `juges/<lot>/…` si l'adaptateur y écrit) ; « fin d'É9 » est posée à la fin de la génération (`course2_v53.py:463`), à reporter après l'antériorité quand elle sera codée ; le journal de consommation omet les juges (CL18-01) |
| Étage sur machine jetable seulement | tenu avec réserve | `etage_entre_generations_v53.py:40-50`, refus avant toute dépense (`course2_v53.py:522+`, lanceur 121-123). Réserve : déclaratif (variable posée à la main) et liste de suffixes de clé incomplète (CL18-13) |
| S17 et sacrifices selon A1 | tenu pour la règle, à corriger pour les bords | `budget_v53.py:97-146` rejoue mot pour mot projection, arrêt d'étape, plafond ; essais et mutations OK. À corriger : CL18-02 (coupure silencieuse), CL18-16 |
| A15 (ligne de GO) | **à corriger** | CL18-03 : la garde laisse passer les lignes à 150 USD et à 10 USD par lancement pour S17 = 45 ; DEP4 absent (CL18-09) |

### Les 15 choix de code du LISEZMOI

| N° | Choix | Avis | Raison |
|---|---|---|---|
| 1 | S17 par génération ; ligne de GO ≥ N × S17 + (N − 1) × étage | **à remonter à Lazar** | cohérent pour N = 1 (le pré-pilote) ; pour N > 1 le devis v5 de session-depot (R-669) raisonne sur un plafond global de la course (110 insuffisant, 160 recommandé), pas sur N plafonds par génération ; CL18-11 |
| 2 | Six étapes fixes dans cet ordre, aucune étape en plus | acceptable | mais il interdit de représenter le plan du brouillon 7 (É1 à É9b) : c'est le fond de CL18-04 |
| 3 | Classement : notable agrégé, nombre de juges notables, somme des X, identifiant | acceptable | la somme des X favorise les fiches qui ont tous leurs juges présents ; à écrire au gel ; ce n'est pas une moyenne sur des jetons (interdit respecté) |
| 4 | Juge absent jamais notable ; fait tomber l'unanimité ; majorité sur les présents | acceptable | côté prudent ; aucun arrêt « non mesuré (technique) » à 25 % d'absents (A14, CL18-04) |
| 5 | Fiche « à corriger » retenue, comptée, servie à personne | acceptable | non comptée dans le débordement de Kimi (`aiguilleur_v53.py:117-121`) : à dire à Lazar |
| 6 | Refus de l'aiguilleur sur une fiche de Kimi = débordement | **à remonter** | un incident technique de l'aiguilleur peut arrêter Kimi (S12 à 0,10 : trois refus suffisent sur 30 fiches) ; le brouillon distingue A14 (technique) de M5 (contenu) ; CL18-10 |
| 7 | Débordement : arrêt de Kimi proposeur **et** metteur en fusion | **à remonter** | absent du brouillon 7 ; si Kimi est l'unique metteur en fusion (configuration d'essai), un débordement supprime tout le bisociateur de la génération (`course2_v53.py:272`, `409`) ; CL18-10 |
| 8 | Rôles du kit : aiguilleur, lecteurs, juges sans outil ; proposeurs et fusion avec | acceptable | |
| 9 | Paire unique (n = 2) au premier bras, dans l'ordre tiré, qui peut la noter | acceptable | le brouillon dit « bras de priorité 1 » ; l'écart ne joue que si ce bras ne peut pas noter la paire ; à écrire au gel |
| 10 | Bras méta : niche retenue seulement si les deux lecteurs s'accordent ; structures = union ; repli unique | **à remonter** | ces règles décident quelles paires le bras méta choisit, mais elles sont dans le code (`course2_v53.py:387-391`), pas dans l'annexe scellée (A20/A16) ni dans le brouillon ; les écrire à l'annexe ou au préenregistrement |
| 11 | Passe « tableau » : ses fiches sont aussi jugées | **à remonter** | le brouillon 7 (É7a) ne les juge pas (aiguilleur et second lecteur seulement ; juges = 28 rendus + 3 fusions) ; surcoût hors plan ; CL18-08 |
| 12 | Étage joué après chaque génération sauf la dernière | acceptable | R-636 |
| 13 | Machine jetable : variable + refus si nom de clé présent | acceptable | CL18-13 pour la liste de suffixes |
| 14 | A15 : plus grand montant « … USD » de la cellule, exigé ≥ somme des plafonds | **à corriger** | CL18-03 |
| 15 | Étiquettes interdites : liste injectée, mot entier, sur la fiche servie | **à corriger** | CL18-06 : pluriels et dérivés passent |

## B. Fuites

- **Un juge voit-il les notes des autres ?** Non. La consigne d'un juge est la pièce figée plus la fiche (`entree_une_fiche`, `fiches_v53.py:77-84`) ; rien d'autre n'est passé au juge ; sessions séparées par juge et par fiche (`juges_croises_v53.py:97`).
- **Bras d'une fiche.** L'entrée du metteur en fusion ne porte ni nom de bras ni de règle (`bisociateur_v53.py` `entree_fusion`, essai `test_entree_de_fusion_aveugle`) ; la correspondance fusion → bras est déposée au coffre (`course2_v53.py` `deposer(self.tache("cle-bras"))`). Les juges ne voient pas la case. Réserve : `manifeste-fin.json`, écrit aussi à l'arrêt (bloc `finally`), contient `paires` par bras et `profil_meta` ; aucune logique ne les relit, donc pas d'incident d'A21 (qui vise la lecture), mais un opérateur qui ouvre ce fichier après un arrêt précoce voit l'affectation paire → bras avant la fin d'É9.
- **Fournisseur.** Jamais servi à un lecteur ni à un juge (`meta` tenu à part, `CLES_META` interdit dans le contenu). Deux fuites possibles par les chemins, non vérifiées sur moteur réel (CL18-12) : le dossier de session de chaque juge s'appelle `juges/<lot>/<étiquette du juge>/<fiche>` avec `lot` ∈ {`passe1`, `passe2`, `fusions`} ; le lecteur d'étiquettes reçoit « `## Lecture : vocabulaire_gk` » dans sa consigne (`course2_v53.py:321`, `nature` ∈ {concepts, vocabulaire_gk, niches}). Si l'agent voit son dossier courant (le kit et la commande externe passent `cwd=dossier`), un juge sait qu'il juge une fusion, mot que A4 interdit dans ses entrées ; « gk » est une abréviation du nom d'un bras. La garde A4 ne porte que sur le corps de la fiche.
- **Verdicts d'É6/É7 avant la fin d'É9.** Aucun chemin de code ne les relit avant `declarer_fin_e9` (j'ai lu `executer`, `jouer_etape`, `_proposer`, `_aiguiller`, `_notes`, `etape_fusions`) ; les décisions de budget ne reçoivent que des montants. Limite : l'orchestrateur ne protège pas le système de fichiers.
- **Contenu d'une fiche « concret ».** Le noyau ne le copie nulle part : journal d'aiguillage sans contenu (`aiguilleur_v53.py:66-91`, champ `categorie` ≤ 40 caractères, libre, écrit par l'aiguilleur), `fiches.json`, `tableaux.json`, héritage, projection de l'étage et mémoire ne portent que des fiches à passeport. L'essai balaie toute la sortie pour un marqueur : bon, **mais seulement avec le moteur simulé, qui n'écrit rien dans les dossiers de session**. Avec le kit Claude ou la commande externe d'Argon (cwd = dossier de session) et l'aiguilleur en face d'une fiche concrète, rien ne garantit l'absence de traces dans `aiguillage/appels/<fiche>/` ; le LISEZMOI le dit pour le kit, il n'y a ni essai ni garde (A10). Les messages d'événements (`etiquette-rejetee`) reprennent jusqu'à 200 caractères de sortie de lecteur sur des fiches à passeport, pas sur des concrètes.
- **Le lanceur lit-il un secret ?** Non, d'après `ideation_v5.py` : il lit la valeur de `GO_ID` (identifiant public, ligne 129) et celle de `POLE_MACHINE_JETABLE_V53` ; pour les clés il ne parcourt que des noms (`noms_de_cle_presents`, boucle sur les noms d'environnement dans `exiger_machine_jetable`). L'adaptateur Kimi n'envoie aucun en-tête d'autorisation et n'utilise aucun mandataire (`ProxyHandler({})`) ; la commande externe ne reçoit que `PATH, HOME, LANG, LC_ALL, TMPDIR` plus les variables de la configuration (refus si un nom de clé s'y trouve). `adaptateurs_reels` (lanceur 54-71) n'est exercé par aucun essai : les chemins `--moteur reel` ne sont éprouvés que jusqu'au refus A15.

## C. R5 : gardes nouvelles, essais, mutations

Tous les essais lisent la vraie sortie du code (moteur simulé ou faux relais en boucle locale) ; aucune sortie inventée sauf deux endroits : `test_rejeu_sur_les_seules_consommations` (`test_v53_instruments.py:164`) passe à `rejouer` des nombres écrits à la main, jamais les consommations d'un run (CL18-01) ; l'artefact « verdict dans un coût » n'est qu'un test de type (un dictionnaire refusé par `reel()`), pas une dépendance numérique à un verdict.

| Garde | Cas sain | Artefact | Pour la bonne raison ? |
|---|---|---|---|
| Configuration (manques, « À REMPLIR », pièce altérée, bras sans paramètre) | oui | oui | oui |
| A15 | oui | six refus | oui, mais cellules de GO propres seulement (CL18-03) |
| A1 (retrait, réduction, réduite qui ne tient pas, protégée non lancée, coupure, arrêt d'étape, hors porte) | oui | oui | oui |
| A21 | oui | lecture avant la fin, au coffre et au niveau génération | oui |
| R9 | oui | racine négative, numpy < 1,25 | oui |
| Kimi par voie protocole | oui | huit artefacts, pire cas sans envoi, réglages sans défaut | oui |
| Aiguilleur, A17, S12 | oui | oui | passeport : **non** pour « contenu modifié » (CL18-05) |
| A4 | singuliers | singuliers | non pour pluriels (CL18-06) |
| A2 | oui | version changée entre lots | oui ; « modèle servi absent » non essayé (couvert en amont par les adaptateurs : `modele_conforme(demande, None)` = faux, vérifié) |
| A18 | oui | quatre artefacts | oui ; non exercé au niveau génération |
| Paires, A19, A20, désaccord hors score, fusion aveugle | oui | oui | oui ; « trois paires à n = 2 » (ligne 16 de la table R5) sans essai propre |
| Machine jetable, nom de clé | oui | trois environnements | oui |

**Mutations en mémoire** (aucun fichier modifié ; harnais `/tmp/cl18/mutate.py`, témoin identité : 16 essais OK). Toutes attrapées, sur le bon essai :

| Mutation | Essais en échec |
|---|---|
| plafond S17 (étape 3 d'A1) neutralisé | `test_artefacts_reduite_qui_ne_tient_pas…`, `test_hors_porte_non_lancee…` |
| coupure à S17 en cours d'étape neutralisée | `test_artefacts_reduite_qui_ne_tient_pas…` |
| arrêt d'étape / projection / ordre de sacrifice inversé | un à deux essais chacun, dont `test_budget_bas_retire_les_sacrifiables…` |
| bras méta : annexe absente / empreinte / scellement / approbation de Lazar neutralisés | `test_annexe_meta_a20` ; l'empreinte aussi au niveau génération. Remarque : sans le contrôle « absente », l'essai échoue par son motif (« non scellée » au lieu de « absente »), c'est-à-dire par la garde suivante ; l'essai de génération A20 exerce l'empreinte, pas l'absence |
| non-lecture (`ouvrir` sans condition) | `test_artefacts_lecture_avant_fin…` et `test_artefact_lecture_d_un_verdict_avant_la_fin_a21` |
| passeport toujours vrai | cinq essais, dont A17 et débordement de Kimi |
| A4 neutralisée | sept essais |
| A2 neutralisée | deux essais |
| S12 neutralisée | deux essais |
| A15 plafond neutralisé | deux essais |
| tableau sans passeport | un essai |
| nom de clé de la machine jetable neutralisé | échoue, mais par `CorrespondanceRefusee` : l'essai passe une correspondance vide, il n'atteint donc la vraie raison que parce que la garde est en amont |

## D. Graines (R9)

- `SeedSequence(racine, spawn_key=(cle_de_tache(nom),))`, `cle_de_tache` identique à celle du dépôt (`graines_v53.py`, essai sur `pp2-partition`) ; numpy < 1,25 refusé sans repli. Constaté : deux générations identiques à la même racine donnent des octets identiques pour `classement.json`, `fiches.json`, `memoire.json`, `tableaux.json`, mêmes paires et mêmes graines au manifeste ; une autre racine change le classement. L'ordre des bras (`course2_v53.py:400`), des fusions (406) et le départage par bras (369) sont tirés ; aucun ordre ne dépend d'un `set`.
- Écarts : **les noms de tâches ne sont pas ceux du brouillon 7** (`g1-bisoc-ordre`, `g1-bisoc-gu_krenn`, `g1-bisoc-meta`, `g1-bisoc-basique`, `anonymisation-<juge>-<fiche>` contre `pp2-bisoc-ordre`, `pp2-bisoc-gk`, `pp2-bisoc-meta`, `pp2-bisoc-n`, `pp2-anonymisation`…) ; le docstring du bisociateur cite encore `bisoc-gk` et `bisoc-ordre-fusion` (ce dernier n'est pas dans le brouillon). Tant que la table des tâches n'est pas alignée ou déclarée, le script du préenregistrement et l'orchestrateur ne tirent pas la même chose avec la racine 20261101 (CL18-07). Le manifeste R9 ne porte pas le commit (« à porter par l'opérateur ») : acceptable si l'opérateur le fait, sinon un paramètre `--commit` évitera l'oubli.

## E. Budget

- **S17 par génération et ligne ≥ N × S17.** Cohérent avec le brouillon 7 pour N = 1 (un pré-pilote = un plafond). Au-delà, c'est une décision de course (CL18-11).
- **Plafond de relais = réservation (CP5-09)** : implémenté comme le texte le dit. La réservation sert aux trois tests (`budget_v53.py:97-146`) ; le coût réel est compté en entier ; seul S17 coupe : chaque appel reçoit `min(plafond de session, reste avant S17)` (`course2_v53.py:193`), jamais la réservation de l'étape. Deux réserves : (a) la coupure n'est pas reportée si le reste tombe exactement à 0 (CL18-02) ; (b) le cumul est écrêté à S17 (`budget_v53.py:159`), ce qui masque un dépassement réel ; le journal `coupee_a_s17` ne garde que `plafond − avant` (CL18-16).
- DEP4 (le relais accepte une réservation dépassée jusqu'à S17 − cumul) : le brouillon 7 l'a fait entrer dans A15 (VB6-04) ; la v53, écrite sur le brouillon 6, ne le vérifie pas (CL18-09).

## F. Rejeu des essais

Machine : Python 3.13, numpy 2.5.3, pytest 9.1.1 ; `bwrap` absent ; `unshare -n` avec boucle locale levée ; `env -i PATH=/usr/bin:/bin HOME=/tmp LANG=C.UTF-8`, `-B`, sans cache pytest ; dossier de livraison (l'essai R12 lit `../EMPREINTES-orchestrateur-v52b.txt`).

| Passe | Résultat | Accord avec le LISEZMOI |
|---|---|---|
| v53 seule (`test_v53_instruments.py`, `test_v53_course2.py`) | 56 OK, 31 sous-essais OK | exact |
| suite entière avec `POLE_ESSAI_BAC_REEL_NON_JOUE=1` | 594 OK, 12 ignorés, **1 échec** (`test_v51_06_programme_du_filtre_d_appels_systeme`), 382 sous-essais, 262 s | exact |
| suite entière sans variable | 594 OK, **13 échecs** : `test_v51_01, 02, 04, 05, 06, 08, 11, 12`, `test_v52b_02`, `test_v48_22`, `test_v49_19`, `test_v50_15`, `test_v50_16`, 268 s | exact (607 au total) |

Sans `ip`, mon premier essai (boucle locale non levée) a fait échouer 6 essais de Kimi : ils exigent la boucle locale, comme le dit le LISEZMOI.

**Échec aléatoire de la v51 : non identifié.** `test_v51_06` est déterministe ici (le contrôle « bwrap absent » passe avant celui de l'architecture) et passe avec un vrai `bwrap` (CL16 : 517 OK). Le candidat le plus plausible est `test_v6_relais_reel::…::test_artefact_plafond_atteint`, signalé intermittent sous charge dès la v11 (8 échecs sur 64) puis corrigé en v14 par une attente de règlement du journal (`test_v6_relais_reel.py:146-149`). Je l'ai joué 25 fois sous charge (4 boucles actives sur 2 processeurs, boucle locale) : 25 OK. Non reproduit ; confiance faible. Pour trancher, il faudrait la sortie de la passe de session-depot où l'échec est apparu.

## G. Ce qui manque pour le pré-pilote

La liste du LISEZMOI (six points) est exacte mais **incomplète**. S'ajoutent :

1. Gardes d'arrêt non codées : A3 (appel coupé ; trois échecs consécutifs d'un rôle → arrêt du rôle), A14 (plus de 25 % d'appels sans sortie → « non mesuré (technique) »), A11 (refus ou limite d'Opus : attente, refus compté ; ici un refus de juge devient « absent » sans attente ni arrêt). Un juge qui échoue à chaque appel continue donc à dépenser jusqu'à S17.
2. Jeu de la table R5 (32 lignes) **à É0** : aucune des gardes n'est rejouée par le lanceur au démarrage ; elles ne vivent que dans les essais. `--verifier-seulement` ne rejoue aucune garde.
3. DEP4 comme condition d'A15 (brouillon 7).
4. Le pré-pilote est un dispositif de témoins (28 fonds, classes P/N/C/G, axes, indices de forme) ; la v53 prend des proposeurs et des cases. Même l'étalonnage M1 « chaîne avec les témoins » demande une orchestration nouvelle (le LISEZMOI le dit en une ligne), pas seulement des modules.
5. Report de `declarer_fin_e9` après l'antériorité (M6) quand elle sera codée ; consigne de l'aiguilleur empreintée avant l'écriture des 12 concrets (ordre temporel, hors code).
6. Les étapes citées au LISEZMOI (rédacteur, rendus, relecteur, S18/S19, étage 1, M6/M6b, axe 7, second lecteur et adjudicateur, clés des classes) : exact.

## Constats

Gravité : majeure = à corriger avant tout lancement ; moyenne = à corriger ou à décider avant le gel ; mineure = durcissement.

**CL18-01 (majeure) — le journal de consommation omet les appels des juges ; le rejeu de la garde 30 n'est pas éprouvé.** `JugesCroises.juger` ne note aucune consommation (`noter_consommation` n'est appelée que dans `_appel` et `_aiguiller`, `course2_v53.py:196-202`, `258-278`) ; `_juger` ajoute seulement le total (`course2_v53.py:288`). Mesure (sonde 5, run simulé complet) : 75 appels, coût 0,75 USD, cumul de budget 0,75, **somme des consommations 0,42** (33 appels de juge, 0,33 USD, absents). Les décisions réelles du budget ne se rejouent donc pas « sur les seules consommations » (ligne 30 de la table R5, A21), et M7 (jetons, durée, modèle servi par appel) manque pour le rôle le plus cher. De plus, une exception dans `juger` (A2, A4, A17) perd le coût déjà engagé sur la fiche en cours (variable locale `cout`, `juges_croises_v53.py:111`) : `apres_etape` sous-compte. Essai en défaut : `test_rejeu_sur_les_seules_consommations` nourrit `rejouer` à la main. Correction : noter chaque appel de juge au coffre, compter le coût dans un `finally`, et un essai qui rejoue `Budget` sur `coffre.consommations()` d'un run simulé et compare au journal de budget réel.

**CL18-02 (majeure) — une étape protégée coupée par le reste de budget est déclarée « jouée », et la course continue.** `apres_etape` ne signale la coupure que si `cumul > plafond` (`budget_v53.py:158`). Or les appels sont bornés à `min(session, reste)` et les boucles s'arrêtent quand `reste ≤ 0` en émettant un simple événement (`aiguillage-coupe`, `juges-coupes`, `fusion-coupee`, `course2_v53.py:261, 286, 416`) ou sans rien dire (`_proposer`, `etape_etiquettes`, `break` ligne 347). Sonde 2 (coût fictif 0,4, plafond 6,0) : `juges` « jouee » alors qu'une fiche sur quatre n'a jamais été jugée (3 classées), `juges-coupes` seul témoin, cumul pile à 6,0 ; `c13_budget_satisfaite` ne tombe à faux que parce qu'une étape suivante (`etiquettes`) est non mesurée. Le brouillon (A1, étape 4) veut « non mesurée (budget), C13 non satisfaite ». Quand une étape protégée est non mesurée (sonde 2, plafond 3,2 : `juges` et `etiquettes` non mesurées), la génération se termine sans arrêt, classement vide, et `executer_course` enchaîne la génération suivante et l'étage sans regarder C13. Correction : toute coupure d'une étape protégée (événement ou `reste ≤ 0` rencontré) → `NON_MESUREE` ; test `cumul ≥ plafond − EPS` ; arrêt de la course (nœud) si C13 est fausse ; essais sur ces deux cas.

**CL18-03 (majeure) — A15 laisse passer des lignes de GO qui n'autorisent pas S17.** `montant_plafond` prend le plus grand montant « … USD » de la cellule (`configuration_v53.py:284-287`) et `verifier_go` exige seulement `≥` (ligne 310). Le brouillon veut « une ligne de GO **au** plafond gelé S17 (aucun lancement à un autre plafond) » ; la garde ne regarde pas non plus le périmètre. Sondes 1, 2b et 6, sur `registres/go.md` réel, S17 = 45, date 2026-11-02 : `GO-2026-10-20-06` (« 150 USD, plafond de GO-2026-10-04-08 inchangé », phase 0, valide jusqu'au 2026-11-30) **acceptée** (plafond lu 150) ; `GO-2026-10-20-07` (« 10 USD par lancement, dans les 150 USD de… ») **acceptée** (150 lu). Les libellés propres des essais (« 45 USD ») masquent ce défaut. Correction : refuser toute cellule qui porte plus d'un montant distinct, exiger l'égalité avec S17 (ou une ligne dont le périmètre cite le pré-pilote), essai sur les libellés réels du registre.

**CL18-04 (majeure) — la v53 ne peut pas jouer le plan du brouillon 7, et la liste de ce qui reste est incomplète.** `verifier_configuration_generation` refuse toute étape hors des six (`course2_v53.py:70-85`) : É1, É3, É5, É8, É9, É9b sont impossibles ; A3, A14, A11, le jeu de la table R5 à É0 et DEP4 ne sont pas codés et pas listés (section G). Verdict : lançable pour une génération de course ; pas pour le pré-pilote.

**CL18-05 (moyenne) — le passeport ne recalcule pas l'empreinte.** `a_passeport` compare l'empreinte stockée dans la fiche à celle du passeport (`aiguilleur_v53.py:93-94`), pas à `empreinte_objet(fiche["contenu"])`. Sonde 1 : contenu modifié après l'aiguillage, `a_passeport` reste vrai. L'essai « contenu modifié après passage » (`test_v53_instruments.py:355`) change l'empreinte stockée, pas le contenu : il passe par la mauvaise porte. Aucun chemin du code ne modifie un contenu aujourd'hui (risque faible), mais le LISEZMOI promet « identifiant + empreinte du contenu exact ». Correction : recalculer à `a_passeport` et corriger l'essai.

**CL18-06 (moyenne) — A4 laisse passer pluriels et dérivés, et arrête toute la génération sur un mot légitime.** `_motif` impose un mot entier (`fiches_v53.py:62-64`). Sonde 4 : « des témoins », « deux fusions », « fusionnée », « protocole exploratoires », « bisociations », « Gu et Krenn » ne sont pas détectés ; seuls les singuliers exacts de la liste le sont, et c'est tout ce que les essais exercent. À l'inverse, « groupe témoin » dans une fiche de méthode (fréquent en contrôle) est un arrêt de la génération entière (`EtiquetteDansEntree` remonte de `classer`). Correction : liste injectée avec variantes ou correspondance par préfixe ; décider avec Lazar si un mot légitime doit exclure la fiche (incident) plutôt que tout arrêter.

**CL18-07 (moyenne) — noms de tâches de graines différents du brouillon 7.** Voir section D. À aligner ou à déclarer avant le gel, sans quoi la reproduction par le script du préenregistrement n'est pas possible.

**CL18-08 (moyenne) — deux écarts de lecture non déclarés.** (a) Le brouillon 7 (M9) fait porter la bisociation sur « les fiches non aiguillées de la passe 1 **de Kimi** » ; la v53 prend la passe 1 de tous les proposeurs (`course2_v53.py:334, 398`), donc des paires Kimi–Argon sont possibles. (b) Les fiches de la passe « tableau » sont jugées par trois juges (`course2_v53.py` `etape_passe_tableau`, `_juger(self.passe2, "passe2")`), alors que le plan du brouillon 7 (É7a) n'y met que l'aiguilleur et le second lecteur : le coût de l'étape dépasse le tableau de coûts (3,1 attendus). À remonter à Lazar avec les choix 10 et 11.

**CL18-09 (moyenne) — la v53 a été écrite sur le brouillon 6.** Le LISEZMOI cite le brouillon 6 ; le brouillon 7 (R-668, 01:01 UTC) précède la livraison (01:29 UTC) et change A15 (DEP4, VB6-04). Un seul fichier de spécification doit être cité, et la configuration doit porter la confirmation de DEP4 (pièce empreintée, comme la source de S31).

**CL18-10 (moyenne) — la garde de Kimi confond technique et contenu, et déborde du brouillon.** Un refus de l'aiguilleur vaut « concret » (`aiguilleur_v53.py:77-80`), compté au taux de débordement de Kimi (S12) ; au-dessus, arrêt de Kimi proposeur **et** metteur en fusion (`course2_v53.py:269-278`). Conséquences : un incident de l'aiguilleur peut éteindre un fournisseur ; si Kimi est l'unique metteur en fusion, plus aucune fusion (`409`). À décider : compter à part les refus techniques (A14), et ne pas coupler les deux rôles sans mot de Lazar.

**CL18-11 (moyenne) — plafond par génération (choix 1).** À remonter : voir section E et choix 1.

**CL18-12 (moyenne) — noms de sessions et mot de lecture pouvant révéler lot et bras.** Section B. Correction simple et sans coût : dossiers de session nommés par identifiant opaque, nature de lecture neutre (« vocabulaire »), et une garde A4 sur la consigne complète servie (pièces comprises). À vérifier sur moteur réel si l'agent voit son dossier courant.

**CL18-13 (mineure) — machine jetable déclarative, liste de suffixes courte.** `SUFFIXES_DE_CLE` = `_API_KEY`, `_TOKEN`, `_SECRET`, `_SECRET_KEY` (`etage_entre_generations_v53.py:28`) : `AWS_ACCESS_KEY_ID`, `GOOGLE_APPLICATION_CREDENTIALS`, tout `*_PASSWORD` passent (`AWS_SECRET_ACCESS_KEY` est couverte seulement par la liste du relais). La variable `POLE_MACHINE_JETABLE_V53=1` ne prouve rien par elle-même ; à compléter par le contrôle de l'opérateur (devis de location, destruction).

**CL18-14 (mineure) — mesures d'accord.** `kappa_cohen` et `kappa_fleiss` rendent 1,0 quand `pe == 1` (`juges_croises_v53.py:140, 154`) : trois juges qui disent « non notable » partout donnent un accord parfait (mon calcul : 1,0 et 1,0) ; `etalonner_juges` lève une erreur de type si un verdict manque (`None`). Prévoir « accord non défini » comme pour la règle des marges constantes (S28), et les verdicts absents.

**CL18-15 (mineure) — essais.** Le commentaire de `test_v53_course2.py:70` (« aucun juge n'a reçu une fiche sans passeport, ni une étiquette interdite ») annonce un contrôle absent (la boucle ne vérifie que `cout > 0`) ; code mort dans `test_artefact_debordement_de_kimi…` (fonctions `claude`, `aig` supprimées par `del`, ligne 128) ; « contenu concret jamais copié » vaut pour le moteur simulé seulement ; pas d'essai pour « trois paires à n = 2 », A18 au niveau génération, kappa dégénérés. Les essais écrivent `essais/_tmp/` et `pole/__pycache__/` dans la livraison lue : la suite modifie l'arbre qu'elle contrôle (supprimés par moi ; à rediriger vers un dossier temporaire).

**CL18-16 (mineure) — M6b coupée à S17 et cumul écrêté.** Une étape « protégée hors porte » coupée en cours de route devient `NON_MESUREE` (`budget_v53.py:160`), donc fait tomber C13, alors que le texte dit « hors porte, C13 inchangée » pour M6b non lancée ; le texte ne tranche pas le cas coupée. Et l'écrêtage du cumul à S17 efface le dépassement réel du journal.

**CL18-17 (mineure) — héritage et règle des paires.** Le texte d'héritage servi aux proposeurs de la génération suivante (`course2_v53.py:230`, `501`) ne passe pas par la garde A4 (hors liste des entrées protégées du brouillon, mais il contient les titres des fusions) ; la règle n < 2 / n = 2 / n ≥ 3 compte les fiches de toutes les cases ensemble (`bisociateur_v53.py:254-265`) alors que les paires sont intra-case ; `choisir_paires` lève `KeyError` si un bras manque dans `departage`.

## Avant le lancement

1. Corriger CL18-01 à CL18-03 (et CL18-05, CL18-06, CL18-12 qui sont courts), puis rejouer les 56 essais et les mutations de la section C.
2. Décider avec Lazar : choix 1, 6, 7, 10, 11 du LISEZMOI, CL18-08, CL18-10, CL18-11, noms de tâches (CL18-07).
3. Aligner la spécification citée sur le brouillon 7 et coder DEP4 en pièce empreintée (CL18-09).
4. Pour le pré-pilote lui-même : étapes, A3/A14/A11 et rejeu de la table R5 à É0 (CL18-04) dans une v54 ; une nouvelle contre-lecture.

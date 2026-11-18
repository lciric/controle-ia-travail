# Rapport du développeur — corrections du code du saboteur à budget (ii-b), v6

Développeur : Claude Fable 5.2, développeur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`. Je n'ai écrit ni la conception, ni le code des versions précédentes, ni leurs contrôles.
Mandat : `docs/notes/barreau8-iib-v1/mandat-developpeur-fable-iib-v1.md` (dépôt principal), empreinte `694d237c71e96ff1652748c2677103127a5b006ab80a6005902270439607cd32`, vérifiée.
Branche : `prep/iib-code-v3`, reprise à la tête `ff6a947593f7c9f73c96e8055ff2d94a8f2eb02e`, commits à la suite, aucune réécriture d'histoire.
Références lues : contrôle court (`controle-court-code-iib-v3-v1.md`), vérification courte (`verification-courte-corrections-controle-court-iib-v1.md`), relevé du code des deux bases (`releve-code-des-deux-bases-v1.md`), rapport v5 du développeur précédent. Les rapports v2 à v5 restent archivés sous leurs noms (R12).
Code de course **exploratoire, non opposable (R-522)**. Processeur seulement : aucune dépense, aucun modèle chargé, aucun téléchargement, aucune instance.

## Verdict

Les trois points du mandat sont traités. L'essai du relais de la ligne de progrès lit maintenant la sortie réelle d'un jeu jouet du lanceur, et il échoue quand la correction du lanceur est retirée (preuve jouée). La lecture de la diffusion appelle la pièce inscrite « mots et coût » pour ses deux bases textuelles et n'a plus aucune méthode d'ajustement à elle. La sonde de texte de la recherche de fuite ne saute plus un fichier valide.

Suite ciblée : **445 réussis sur 445, aucun saut**. Répétition jouet : **48 fichiers comparés, 0 différent, identique à l'octet**. Refus rencontrés : aucun.

## 1. CC-01 (majeur) — l'essai du relais lit la sortie réelle d'un jeu jouet du lanceur : corrigé, preuve jouée

Commit `4024f3991`. Fichier : `tests/test_iib_amorce_v1.py`. Aucun changement sous `src/` ni sous `scripts/` pour ce point.

Ce que font les essais neufs :
- `_jeu_jouet_du_lanceur` joue un jeu jouet réel du lanceur (`iib.lanceur_v1.executer`, monde factice de `test_iib_lanceur_v1.depot_jouet`) et rend sa sortie d'erreur réelle, prise par `capfd`. L'essai n'écrit aucune ligne de progrès et ne passe aucun argument à la fonction de progrès.
- `_relais_de_l_amorce` rejoue le relais de l'amorce sur cette sortie : `grep -E` avec le motif de progrès lu dans l'amorce, puis `grep -qiE` avec le motif interdit lu dans l'amorce, ligne à ligne, comme la boucle du relais.
- Issue « épreuves passées » (`test_sain_progres_d_un_jeu_jouet_complet_du_lanceur_relaye_par_les_deux_motifs_de_l_amorce`) : jeu jouet complet ; une seule ligne des épreuves, relayée, qui finit par `etape=epreuves etat=passees epreuve=aucune` ; aucune ligne de progrès retenue sur tout le jeu ; les étapes `episodes`, `oracle`, `epreuves`, `tour`, `distillation`, `fin` sont toutes relayées (le jeu est allé au bout).
- Issue « arrêt » (`test_sain_progres_d_un_jeu_jouet_arrete_aux_epreuves_…`) : une épreuve **réellement** en échec dans le monde jouet (jumeau à moitié illisible, même réglage que l'essai existant du lanceur), sans `monkeypatch` des épreuves ; la ligne relayée finit par `etape=epreuves etat=arret epreuve=E-O6` ; aucune ligne retenue.
- Artefact (`test_artefact_ancienne_forme_de_la_ligne_des_epreuves_retenue_par_le_relais`, deux cas) : le lanceur émet de nouveau l'ancienne forme, par la fonction de progrès réelle, dans un jeu jouet réel ; le relais la retient, aucune ligne des épreuves n'est relayée.

Preuve jouée, exactement :
1. Copie hors dépôt de `src/`, `tests/`, `scripts/` et du dossier des invites (`docs/sources/invites-2606.08892-v1`), dans mon dossier de travail jetable.
2. Dans la copie, la ligne 292 du lanceur remise à l'ancienne forme (`progres(etape="epreuves", echec=ep["echec"] or "aucun")`). Les quatre essais joués avec `PYTHONPATH` sur la copie : **4 échecs**. Les deux essais sains échouent sur le motif attendu : « 1 ligne(s) de progrès retenue(s) par le motif interdit », avec la ligne réelle `etape=epreuves echec=aucun` (issue passée) et `etape=epreuves echec=E-O6` (issue arrêt). Les deux artefacts échouent aussi (ils retraduisent la forme corrigée, absente).
3. Correction remise dans la copie (fichier comparé à l'octet à celui de la branche) : **4 réussites**.
4. Sur la branche : 4 réussites.
Un premier passage dans la copie avait échoué pour une autre raison (dossier des invites absent de la copie) ; je l'ai écarté, complété la copie et rejoué : les résultats ci-dessus sont ceux du passage complet.

## 2. Portage de la base textuelle sur la pièce inscrite : fait, avec ses essais

Décision appliquée : GO-2026-11-18-56, point 4, recommandation (A) du choix n° 1 du relevé — la lecture appelle les fonctions du contrat de la pièce inscrite, chargée par son chemin à l'empreinte inscrite, après la vérification des modules gelés et avec les fils de calcul fixés à 1.

### Ce qui change

| fichier | changement |
|---|---|
| `src/controle_ia/iib/bases_textuelles_v1.py` (neuf) | Charge la pièce `scripts/mots_et_cout_t06_v3.py` par son chemin, seulement si son empreinte est `9dbcc55c…c4e674` ; vérifie les six fonctions du contrat ; appelle la vérification des neuf modules gelés de la pièce ; exige les fils de calcul à 1 en mode réel ; garde les champs des actions et les plis mêlés ; convertit tout arrêt de la pièce en arrêt de la lecture. Aucune fonction de la pièce n'est recopiée, aucun réglage n'est touché. |
| `src/controle_ia/iib/lecture_v1.py` | La régression propre au paquet (méthode de Newton), son score, son vocabulaire, ses traits, ses centres et sa normalisation sont **supprimés**. Le prédicteur sur les traits du texte est la base (A) de la pièce (`apprendre_a`, `noter_a`) ; la base « mots et coût » est la base (B) de la pièce (`apprendre_b`, `noter_b`) ; les centres sont ceux de la pièce (`centres`), calculés une seule fois. La règle du coût déclaré (rien d'appris) lit ces mêmes centres. La sortie consigne la pièce, ses modules gelés, les fils, ses réglages et les versions de `numpy` et `scipy`. |
| `src/controle_ia/iib/configuration_v1.py` | `FIXES_PAR_LE_CODE["lecture_2_code"]` ne porte plus aucun réglage d'ajustement (pénalité, itérations, tolérance, facteur de seuil, motif des mots). Il porte le chemin et l'empreinte de la pièce, et le choix de la meilleure base par action, inchangé. |
| `scripts/lecture_iib_2_diffusion_v1.py` | Pose à « 1 », avant le chargement des bibliothèques de calcul, celles des trois variables de fils qui ne sont pas déjà posées (une valeur déjà posée n'est jamais changée ; en mode réel la lecture refuse si l'une ne vaut pas « 1 »). |
| `tests/test_iib_lectures_v1.py` | Essais des bases réécrits sur la pièce ; gardes neuves, chacune avec un cas sain et un artefact. La liste ciblée `scripts/tests-cibles-iib-v1.txt` est **inchangée** (empreinte `847676ef…e3b6`, égale à celle de l'amorce) : les essais neufs sont dans un fichier déjà listé. |

### Entrées passées à la pièce

- Coût, validité et six formes du champ du coût : lus sur le texte de l'action par le lecteur gelé `t06.cout.cout_action`, celui des deux chaînes d'origine. Le format des actions du saboteur à budget est celui que ce lecteur attend (ligne d'action avec un champ de coût) : le lanceur l'emploie déjà pour ses fiches d'épisodes.
- Nombre de jetons : nombre d'identifiants générés par action, lu dans les fiches d'épisodes de la course (`diag/<run>/episodes-iib.json`, colonne `jetons`, fichier déjà vérifié par empreinte au chargement). L'ancienne lecture prenait la longueur du texte en caractères ; ce n'était pas la quantité de la pièce.
- Texte entier de l'action, pour la base (B).
- Rien d'autre : ni condition, ni phase, ni pas, ni épisode.
- Centres : calculés une seule fois par la pièce sur toutes les actions d'évaluation de la lecture, quatre conditions confondues, sans étiquette, avec le seuil de la pièce (dix coûts lisibles), puis passés tels quels à chaque jeu.
- Plis : inchangés (`t06.test_croise.partition_plis`, clé `iib/lecture-2/plis` du manifeste). La pièce apprend sur les seules actions du pli d'apprentissage (son vocabulaire se forme sur elles) et note le pli lu.

### Gardes et leurs essais (R5 : cas sain et artefact de chacune)

| garde | cas sain | artefact |
|---|---|---|
| pièce chargée à l'empreinte inscrite | chargée, fiche à l'empreinte, rien d'écrit à côté de la pièce | pièce absente ; un octet de plus ; autre empreinte attendue → arrêt |
| contrat de la pièce | six fonctions présentes | fichier sans une fonction du contrat → arrêt |
| modules gelés | neuf empreintes égales à la table de la pièce | table avec une empreinte fausse → arrêt |
| fils de calcul | mode réel, trois variables à 1 | une variable à 4, une absente, aucune → refus en mode réel ; rapporté seulement en mode jouet |
| options d'essai en mode réel | mode réel, pièce inscrite | table d'essai, empreinte d'essai, `maxiter`, pièce passée de l'extérieur → refus |
| champs des actions | exactement les champs permis, vérifié aussi sur l'appel réel de la lecture | champ interdit (condition, pas, phase, épisode, dose), champ en trop, champ manquant → arrêt, aux trois fonctions d'appel et à la notation |
| plis mêlés | apprentissage et notation sur des tâches disjointes | une tâche apprise passée à la notation → arrêt |
| arrêt de la pièce jamais converti en « non calculable » | centres entiers → un état | la pièce s'arrête à l'apprentissage, puis à la notation (arrêt simulé de la pièce), ou reçoit un champ interdit dans le bloc d'appel → arrêt de la lecture, aucun état ; centres calculés sur une autre population → arrêt pour la règle du coût et les deux bases ; base apprise demandée sans pièce chargée → arrêt |
| modèle non calculable (motif de la pièce) | les deux bases se calculent | une itération du solveur → « non calculable », motif « non convergé » de la pièce ; classe absente → « non calculable », motif de la pièce |
| pièce citée par la configuration | configuration du code | autre empreinte citée ; plafond de vocabulaire différent de celui de la pièce → arrêt |
| nombre de jetons lu dans les fiches | jetons de la fiche, par pas | fiche absente ; fiche incohérente → arrêt |
| tâche sans centre | — | une tâche sous dix coûts lisibles : centre absent, coût normalisé nul, rien n'est « non calculable » de ce seul fait |

Deux essais de fond en plus : les scores lus sont ceux que rendent les fonctions du contrat (espion sur la pièce : apprentissage sur les seules tâches de l'autre pli, aire égale à celle des scores de la pièce) ; deux lectures des mêmes sorties rendent le même texte à l'octet.

Banc de mutations joué dans une copie hors dépôt (18 mutations, une garde retirée à la fois, essais des gardes rejoués) : **17 tuées sur 18 au premier passage ; la survivante a donné un essai de plus, puis a été tuée (18 sur 18)**. Détail au § 6.

### Règles gelées

- Graines (R9) : le portage ne tire **aucun** aléa. Le solveur de la pièce part de zéro ; les tirages et les permutations de la lecture restent ceux des clés `iib/lecture-2/…` du manifeste de la course, dérivées par `SeedSequence`. Aucune graine neuve, aucun générateur neuf.
- Aucune moyenne ni médiane sur les jetons. La seule médiane est celle de la pièce : le centre d'une tâche, sur les coûts lisibles de ses actions. Le paquet n'a toujours aucune sonde ; aucune activation n'est lue.
- Aucun repli silencieux (R5) : sans la pièce, la lecture s'arrête ; elle n'a plus d'autre méthode.

### Ce que le portage décide au-delà de la lettre de la décision — à faire trancher

La décision porte sur le choix n° 1 du relevé. Pour appeler la pièce, il a fallu se placer sur les choix n° 2 à n° 4. J'ai suivi partout la recommandation du relevé ; ce sont des propositions, pas des décisions :
1. **Champs de coût et de forme (choix n° 2)** : recommandation (A) — lecteur gelé appliqué au texte, jetons comptés par les identifiants générés. Le format a été vérifié dans le code du lanceur (il emploie déjà ce lecteur).
2. **Population des centres (choix n° 3)** : recommandation (A) — toutes les actions de la lecture, seuil de la pièce tel que codé. Avec 64 tâches, 4 conditions et 10 pas, une tâche a 40 actions : le seuil de dix coûts lisibles est tenable, mais plus de tâches seront « sans centre » qu'à 90 actions. Leur nombre est écrit dans la sortie.
3. **Règle de lecture (choix n° 4)** : **non touchée**. L'état « mots et coût » de la lecture reste celui du code précédent : la base d'aire la plus haute parmi celles qui se calculent. La fonction de la pièce (`etat_dose`) rend « non calculable » dès que l'une des deux bases ne se calcule pas, et tranche l'égalité pour la base (A). Cet écart existait avant le portage ; il n'est pas dans le mandat. À trancher par Lazar.
4. **Règle du coût déclaré** : elle lit maintenant les centres de la pièce, donc son seuil. Avant, une tâche avait un centre dès un coût lisible. Sous dix coûts lisibles, le coût normalisé vaut 0, comme le premier trait de la pièce.
5. **Trait « unité dans le champ du coût »** de l'ancien prédicteur : disparu. La base (A) de la pièce a ses douze traits, dont les six formes du champ.
6. **Garde « lecture de transfert »** de l'enveloppe de la huitième tâche : **laissée**. La recommandation la nomme, mais je n'ai pas ouvert l'enveloppe (cloisonnement du mandat : seule la pièce est lisible), et la lecture de la diffusion n'a aucun jeu de transfert : chaque modèle note les seules conditions sur lesquelles il a appris. Les gardes « champs interdits » et « plis mêlés » sont écrites d'après leur nom et d'après les listes de la pièce, pas d'après le code de l'enveloppe.

### Conséquences à connaître

- **L'empreinte de la configuration jouet change** : `75b8a4a0…` devient `2e65c31bf3fa…b4604` à l'entropie 20261118 (les clés de `lecture_2_code` ont changé). Toute configuration réelle à écrire doit porter les clés neuves ; aucune configuration réelle du saboteur à budget n'existe sous `prereg/` sur la branche.
- **Un essai existant est précisé** : `test_lecture_2_de_la_repetition_jouet_n_ouvre_aucun_fichier_de_sonde`. La vérification des modules gelés de la pièce relit, pour leur empreinte, neuf fichiers de code, dont `src/controle_ia/sondes/evaluation.py` (calcul de l'aire, que `t06.test_croise` importait déjà). L'essai refusait tout chemin contenant « sonde ». Il exige maintenant : hors des fichiers de code du paquet, aucun chemin de sonde ni d'activation ; parmi les fichiers de code, ce seul module ; aucun fichier de lecture de sondes. Aucun score, aucun poids ni aucune sonde apprise n'est ouvert. C'est un assouplissement déclaré d'un essai de garde : à faire juger par le contrôleur.
- **Le sous-point (g)** (gradient lu avant ou après le dernier pas) est sans objet : le chemin de calcul qui le portait est supprimé. La pièce juge la convergence au point rendu (gradient maximal au plus 10⁻⁴, coefficients finis).
- **`scipy`** est maintenant requis par la lecture (la pièce l'emploie). Il est dans `requirements-cpu.txt` (1.17.1), que l'amorce installe sur l'instance. La course sur l'instance ne joue pas la lecture ; la suite ciblée, elle, charge la pièce : le clonage réduit de l'amorce garde `/scripts/` et `/src/` (pièce et modules gelés présents), vérifié dans l'amorce, sans l'éprouver sur une instance.
- Le lanceur, l'amorce et la liste ciblée ne changent pas.

## 3. VC5-01 — sonde de texte sur 512 octets : corrigé, preuve jouée

Commit `f23d5589b`. `tests/test_iib_exclusion_v1.py` : la sonde des 512 premiers octets décode en mode incrémental (`final=False`) ; un caractère coupé par la borne ne fait plus sauter le fichier, seule une suite d'octets invalide le fait. Le reste de la recherche est inchangé. Artefact neuf : fichier valide dont un caractère accentué occupe les octets 511 et 512, motif réel planté plus loin par programme → repéré. Preuve : le même essai joué avec l'ancienne sonde (copie temporaire du fichier d'essais, supprimée) **échoue** ; avec la sonde corrigée, les 17 essais du fichier passent. Le message d'échec ne porte que le rang et la longueur du motif.

## 4. Suite ciblée et répétition jouet

- Suite ciblée (`scripts/tests-cibles-iib-v1.txt`, 13 fichiers, liste inchangée) : **`445 passed`, aucun saut, code 0, jouée avec ce rapport et son sceau présents dans l'arbre (la recherche de fuite lit les rapports du développeur). Commande : `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src <venv du dépôt principal>/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=<à moi> -rsx $(cat scripts/tests-cibles-iib-v1.txt)`, les trois variables de fils posées à 1. Un passage précédent, sur l'arbre du commit `ff9c9f7a4` : `444 passed in 162.75s`**.
- Compte : 425 essais à la tête reprise ; CC-01 : 2 retirés, 4 ajoutés (427) ; VC5-01 : 1 ajouté (428) ; portage : 17 ajoutés au net dans le fichier des lectures (445).
- Répétition jouet (dépôt jetable hors dépôt, entropie 20261118, configuration `2e65c31b…`) : `preparer`, puis deux `jouer` (`20261118-220000-iib-repa`, `20261118-220001-iib-repb`) et `comparer` : **48 fichiers comparés, 0 différent**, codes 0. Les deux sorties de la lecture de la diffusion (résultat et mots pondérés), calculées par la pièce, sont dans les 48 et sont égales à l'octet d'un jeu à l'autre. Dans la sortie jouet : pièce `9dbcc55ca47b…`, 8 tâches, aucune sans centre, `numpy` 2.4.6, `scipy` 1.17.1 ; les dix jeux rendent un état (aucun « non calculable »). Dépôt jetable supprimé à la fin.

## 5. Points du contrôle court et de la vérification courte

| point | état |
|---|---|
| CC-01 | **corrigé (preuve jouée)**, § 1 |
| CC-02 à CC-05 | corrigés par le développeur précédent, confirmés par la vérification courte ; non retouchés |
| VC5-01 | **corrigé (preuve jouée)**, § 3 |
| Portage de la base textuelle | **fait (essais et banc joués)**, § 2 ; six points à trancher ou à juger |
| CC-06, CC-09 | laissés (relèvent de la mère) |
| CC-07 | aucune ligne ajoutée au `.gitignore` : la répétition a été jouée hors du dépôt |
| CC-08 | sans objet après le portage (§ 2) |
| Forme de la ligne de création de 7b, compléments de l'ordre, rapatriement | hors périmètre (session mère) |

## 6. Banc de mutations du portage (copie hors dépôt)

Chaque mutation retire une garde dans une copie hors dépôt de `src/`, `tests/` et `scripts/` ; les essais des gardes du fichier `tests/test_iib_lectures_v1.py` sont rejoués ; « tuée » = au moins un essai échoue. Copie et banc supprimés à la fin.

| mutation | premier passage | essai qui la voit |
|---|---|---|
| empreinte de la pièce non contrôlée | tuée | `test_garde_piece_chargee_a_l_empreinte_inscrite_sain_et_artefacts` |
| contrat de la pièce non contrôlé | tuée | `test_garde_contrat_de_la_piece_artefact_fonction_absente` |
| modules gelés non vérifiés | tuée | `test_garde_modules_geles_sain_et_artefact` |
| fils de calcul non exigés | tuée | `test_garde_fils_de_calcul_sain_et_artefacts` |
| options d'essai permises en mode réel | tuée | `test_garde_options_d_essai_refusees_en_mode_reel` |
| nombre d'itérations d'essai permis en mode réel | tuée | `test_garde_options_d_essai_refusees_en_mode_reel` |
| champs interdits non contrôlés | tuée | `test_garde_champs_des_actions_sain_et_artefacts` |
| champs permis non contrôlés | tuée | `test_garde_champs_des_actions_sain_et_artefacts` |
| plis mêlés non contrôlés | tuée | `test_garde_plis_meles_sain_et_artefacts` |
| arrêt de la pièce converti en « non calculable » | **survit** | aucun au premier passage ; après l'essai ajouté (commit `6d7aab5c1`) : tuée par `test_garde_un_arret_pendant_l_appel_de_la_piece_n_est_jamais_non_calculable` |
| modèle non calculable non relevé | tuée | `test_base_non_calculable_si_une_classe_manque` |
| pièce citée par la configuration non contrôlée | tuée | `test_garde_piece_citee_par_la_configuration_sain_et_artefacts` |
| plafond de vocabulaire non contrôlé | tuée | `test_garde_piece_citee_par_la_configuration_sain_et_artefacts` |
| fiche d'épisode incohérente non contrôlée | tuée | `test_garde_nombre_de_jetons_lu_dans_les_fiches_sain_et_artefacts` |
| pièce passée de l'extérieur permise en mode réel | tuée | `test_garde_options_d_essai_refusees_en_mode_reel` |
| centre manquant toléré par la règle du coût | tuée | `test_garde_un_arret_de_la_piece_arrete_la_lecture_et_n_est_jamais_non_calculable` |
| apprentissage sur le pli lu (plis non respectés) | tuée | `test_sain_les_scores_sont_ceux_des_fonctions_du_contrat_de_la_piece` |
| jetons non lus dans les fiches | tuée | `test_garde_nombre_de_jetons_lu_dans_les_fiches_sain_et_artefacts` |

Le survivant du premier passage était un vrai trou de mes essais : l'artefact que j'avais écrit pour « un arrêt de la pièce arrête la lecture » s'arrêtait avant le bloc d'apprentissage et de notation, et ne voyait donc pas la conversion dans ce bloc. L'essai ajouté fait s'arrêter la pièce à l'apprentissage, puis à la notation, puis lui passe un champ interdit ; la mutation rejouée seule est tuée.

## 7. Lectures hors mandat, limites, refus

- **Lu** : le mandat ; les trois notes nommées ; le rapport v5 ; sur la branche, `iib/lecture_v1.py`, `iib/lanceur_v1.py`, `iib/configuration_v1.py` (extraits), `iib/tours_v1.py` (la fonction des épreuves), `iib/jouet_v1.py` (extrait), les essais `test_iib_amorce_v1.py`, `test_iib_lanceur_v1.py`, `test_iib_lectures_v1.py`, `test_iib_consigne_invisible_v1.py`, `test_iib_exclusion_v1.py` (la fonction de recherche et ses artefacts), le script de la lecture de la diffusion, le script de la répétition jouet, le relais de l'amorce (lignes 395 à 415).
- **La pièce**, lue pour l'appeler, comme le permet le mandat : en-tête, constantes, vérification des modules gelés, centres, traits, base (B), ajustement, notation, garde des fils, contrat. Aucune sortie, aucun score, aucun poids.
- **Hors des fichiers nommés, pour appeler la pièce** : `t06/cout.py` (lecteur gelé du coût), `t06/lanceur.py` (la fonction de progrès), `t06/test_croise.py` (plis, aire, intervalle, plancher : signatures et arrêts). Ce sont des modules gelés de code, déjà importés par le paquet.
- **Non ouverts** : aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b » ; la branche `lot/compte-4-v1` ; l'enveloppe de la huitième tâche ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` du dépôt. Les essais de non-fuite lisent la consigne par programme, comme avant ; je ne l'ai ni affichée ni recopiée.
- **Limites** : le banc de mutations est le mien, pas un contrôle indépendant ; le portage est du code neuf et demande son contrôle court. Je n'ai pas rejoué la suite entière du dépôt, seulement la suite ciblée. Aucune lecture réelle n'a tourné : les essais portent sur des données synthétiques et sur le monde jouet.
- **Refus** : aucun.

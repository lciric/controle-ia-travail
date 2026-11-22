# Programme d'enchaînement de la lecture de la discrétion, bras A — version 1 : note du code

Écrit le 22 novembre 2026 par un agent de la session de relance (Opus 5.5, instance sans interne de moniteur), sur processeur seul, sans réseau ni dépense, sans commit. Texte qui fait foi : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` — 13.2, ligne « programme d'enchaînement de la lecture de la discrétion (8.7 ; brouillon 38 ; vérification du brouillon 37) » ; 8.7, garde de procédure « versement avant lecture » ; 6.3, étapes (m) et (n) ; 6.9 ; 6.10 ; 8.4 ; conventions (constat de lancement, contrôle avant un rejeu). **Non contre-lu** : 13.2 demande une contre-lecture par un agent neuf d'un autre modèle.

## Verdict

Le programme est écrit et éprouvé : constat de lancement par la commande du programme du constat, étape (m), **commit et poussage du dossier de course avant de rendre quoi que ce soit**, étape (n), versement de chaque pièce avant la suivante. Les cinq sorties synthétiques (cas A à E) passent de bout en bout, l'artefact est arrêté à l'étape (m), arrêt versé. **Un blocage, non tranché** : la commande réelle ne peut pas jouer l'étape (n), parce que la garde statique de la version 13 interdit à tout programme rangé sous `src/` ou `scripts/` de nommer la lecture du fichier des unités (règle non écrite n° 1). **Et la garde statique, jouée sur le dépôt aujourd'hui, rend une violation qui n'est pas de ce programme** : la commande réelle s'arrête avant tout constat (réserve 1).

## Fichiers

| fichier | sha256 |
|---|---|
| `src/controle_ia/organismes_discrets/enchainement_discretion_bras_a_v1.py` | `c2f452d9714333f823da36cf9d8d6c04d94b909682c862097baca8b21ddc84e3` |
| `tests/test_enchainement_discretion_bras_a_v1.py` | `f5c800d2c8d4b5db95f8f2a137087c08062bb3082b4b5f557162d05d17f131b8` |

Compagnons `.sha256` à côté de chacun. Code arrêté appelé, non modifié : analyse v13 (`a7ebf29f…`), verdicts v13 (`ae656289…`), garde statique v13 (`fa915de2…`), six modules de la version 12, programme du constat v5 (`fd5fddcd…`).

## Ce que le programme fait, dans l'ordre (une seule exécution)

1. **Avant tout, sans rien lire de la livraison** : lit la configuration scellée ; nomme le dossier de course (celui qui porte les dossiers `livraison-<rang>/`) et son dépôt git ; refuse les cas que le texte n'écrit pas (ci-dessous) ; lit **l'entrée scellée de l'enchaînement** (forme ci-dessous) ; si la table A porte une ligne, si la case « renvoi de la base » n'est pas « vérifié » ou les effectifs de la base non conformes, l'étape (m) n'est pas jouée et rien ne part (6.3 (m) ; 7.2, règle (iii)) ; joue **la garde statique de la version 13 sur `src` et `scripts`** (« l'enchaînement de l'analyse lui donne `src` et `scripts` », en-tête du module de la garde), et consigne ce qu'elle a élagué et les listages à relire.
2. **Versement d'ouverture** : commit et poussage de ce que porte déjà le dossier de course — c'est « le versement refait avant toute lecture » après un poussage en échec (8.7).
3. **Constat de lancement**, par la commande du programme du constat (conventions : « jamais à la main ») : mode de constat s'il n'y a pas encore de constat dans le dossier de la livraison ; **mode de contrôle** s'il y en a un (lecture interrompue avant tout résultat : rejeu après contrôle) ; aucun constat pour l'étape (n) seule, ni pour une reprise de l'étape (n) dont l'acte existe (« l'étape (n), après le fichier scellé de l'étape (m), ne regarde pas ces fichiers »). Le constat ou le contrôle (même malsain, scellé) est versé ; malsain : rien ne part, sa ligne à huit champs est rendue (trace pour le manifeste).
4. **Étape (m)**, si la course ne porte encore aucun fichier de l'étape (m) : règle de discrétion (qui scelle l'ouverture, l'acte de reprise ou la trace de rejeu), garde de sortie, lignes de la table C **aux seules doses en B8**, fichier de l'étape (m) et ses constats. Le résultat est effacé de la mémoire, puis **versement** ; rien n'est rendu avant que le poussage ait réussi ; s'il échoue, `EchecDuVersement`, sans rien rendre. Après le poussage seulement, le déclencheur « au moins une dose en C6 » (7.6) est relu du fichier scellé.
5. **Étape (n)** : pour une reprise de l'étape (n), ouverture de la reprise (confrontation des vingt lectures, acte), versée ; lecture du fichier des unités par la fonction du programme de l'aire conditionnelle, **reçue en argument** ; vingt aires conditionnelles (clés tirées par l'analyse, entropie de la configuration du bras) ; fichier des grandeurs de l'étape (n), avec, en « autres grandeurs », l'état de la base à chaque dose écrit comme en 7.5 (6.3 (n)) ; versement.
6. **Rendu** (compte rendu pour le manifeste de course, une ligne JSON) : programmes joués et leurs empreintes (dont analyse, verdicts et garde statique), commande, garde statique, constats (commande, code, ligne à huit champs), pièces du dossier de course et leurs empreintes, commit, heure et distant de chaque versement, issue, compte des livraisons. **Ni le contenu du fichier de l'étape (m) ni celui des grandeurs** : ils se lisent au vu du commit.

**Tout arrêt est versé avant d'être rendu.** D'une exception d'arrêt, le programme ne tire que son constat et lève hors du bloc qui l'attrape (6.9, « Trace d'appel » : l'exception rendue n'a ni cause ni contexte) ; une erreur inattendue n'est rendue que par son type. Codes de sortie de la commande : 0 abouti ; 3 arrêt de la lecture ; 4 garde ordinaire ; 5 constat malsain ; 6 règle non écrite ; 7 versement en échec (rien n'est rendu) ; 8 erreur inattendue.

Commande : `PYTHONPATH=src python -m controle_ia.organismes_discrets.enchainement_discretion_bras_a_v1 --configuration … --sortie … --registre-courant … --commit-du-registre … [--registre-fige … --ligne-de-go …] --entree … --fichier-des-unites … [--sortie-d-origine …] --programme-du-constat scripts/constat_de_lancement_discretion_bras_a_v5.py --distant … --branche …`.

**Formes de ce programme, que le texte ne fixe pas** (ce ne sont pas des règles, mais elles sont à contre-lire) : l'entrée de l'enchaînement, un objet JSON scellé à onze clés et elles seules — journal de la table A et ses deux réglages, case « renvoi de la base », effectifs de la base, lignes de la table B aux trois doses, états de la base aux quatre doses, coût apparié aux trois doses, actions désappariées par (tâche, épisode) aux quatre doses, seize tâches de vérification, entropie de la configuration du bras ; le distant et la branche du poussage, exigés sans valeur par défaut ; le message du commit ; ce que contient le rendu. La liste fermée des motifs n'est pas lue par ce programme : elle est dans la configuration (dépliée, selon la décision prise) et seule l'analyse la lit.

## Règles que le texte n'écrit pas : erreur explicite, non tranchées

1. **Étape (n) contre la garde statique (bloquant).** 13.2 fait jouer l'étape (n) par l'enchaînement ; la garde statique v13 (code arrêté) refuse le nom de la fonction qui lit le fichier des unités dans tout programme sous `src/` ou `scripts/` qui n'est pas le programme de l'aire conditionnelle (analyse v3 à v13), et refuse tout accès indirect dans un programme qui importe l'analyse. Le programme reçoit donc ce lecteur en argument ; la commande ne le donne pas, et l'étape (n) s'arrête sur `RegleNonEcrite` (code 6), **après** le versement de l'étape (m) — l'étape (n) se rejoue ensuite seule, ce que le texte permet. Voies possibles, pour décision : (a) ajouter le chemin de ce programme aux programmes autorisés de la garde statique (nouvelle version de la garde, R12) ; (b) donner à l'analyse un point d'entrée de l'étape (n) (nouvelle version de l'analyse, contraire à « on cesse de durcir le code ») ; (c) jouer l'étape (n) par une commande hors des dossiers gardés (affaiblit le cloisonnement). Les essais, qui ne sont pas un dossier gardé (limite (d) de la garde), donnent le lecteur.
2. **Dossier des arrêts hors du dossier de course.** 8.7 range le dossier des arrêts dans le dossier de course ; la configuration peut le placer ailleurs (le module de configuration l'admet). Arrêt avant tout constat.
3. **Pièce d'entrée sous le dossier de course** — sortie de la lecture commune, sortie d'origine, fichier des unités, entrée de l'enchaînement, registres : le versement la prendrait, et 8.7 ne la nomme pas parmi ce que porte le dossier de course (pour le fichier des unités, « les outils de version n'en prennent que l'empreinte »). Arrêt avant tout constat.

## Essais (R5) — 30 essais, tous passent (21 s)

Sorties synthétiques extraites du commit `82cfd8ba` (leur seul dossier) ; dépôt distant nu local ; dates git et horloge fixées.

| garde ou étape | cas sain | artefact |
|---|---|---|
| bout en bout | cas A à E : constat, (m), versement, (n), versement ; états du fichier de l'étape (m) = ceux du passage de l'épreuve (A et E « repère », B, C, D « indécis ») ; pièces au distant au commit rendu | artefact : arrêt (m), garde de forme, `valeur_p_pour_la_famille`, juge, dose ½ ; arrêt versé ; ni contexte ni nombre de la pièce rendus |
| versement avant rendu (8.7) | poussage accepté | distant qui refuse le commit portant le fichier de l'étape (m) : `EchecDuVersement`, rien rendu, (n) non partie ; relancé, le versement d'ouverture pousse, puis (n) seule |
| versement | commit du seul dossier de course, poussage vérifié, rien de neuf : pas de commit | distant injoignable ; fichier ignoré par git ; `push` ou `commit` sans effet |
| garde statique | dépôt de code propre | programme qui nomme un fragment du nom du fichier |
| table A, renvoi, effectifs | journal vide, « vérifié » | ligne A1 ; « non vérifié » ; effectifs non conformes : rien ne part |
| entrée de l'enchaînement | entrée de l'essai | clé de plus ; ligne B hors table ; état de base inconnu ; épisode en double ; coût non booléen ; sans compagnon |
| règles non écrites 2 et 3 | pièces hors du dossier, arrêts dedans | arrêts hors du dossier de course ; unités, sortie ou entrée sous lui |
| règle non écrite 1 | lecteur donné | commande réelle (`main`) et lecteur absent : (m) versée, code 6 ; rejoué avec le lecteur, (n) seule sans constat |
| constat | configuration inscrite | non inscrite : constat malsain, aucune ouverture ; programme du constat d'une autre empreinte : code 2, garde ordinaire |
| panne et rejeu | rejeu après contrôle, trace de rejeu, aboutit | panne simulée avant le fichier de l'étape (m) |
| reprise (m) | ligne de GO, configuration de rang 2, cas A lu, abouti | arrêt (m) de l'artefact |
| reprise (n) | sortie refaite cohérente (cas A) : (n) seule, sans second fichier (m), versements ouverture, contrôle, acte, (n) | fichier des unités à une ligne aux champs inversés : arrêt (n) versé ; sortie refaite incohérente (cas B) : constat d'incohérence versé, garde ordinaire |
| panne pendant la reprise (n) | rejeu sans constat ni contrôle | panne après l'acte |
| table C, déclencheur 7.6 | B8 aux trois doses : C6, déclencheur vrai | B8 à la seule dose 1 ; base qui détecte : C3 ; aucune dose en B8 : table C vide |
| arguments | — | distant ou branche vides ; registre figé sans ligne de GO et l'inverse ; horloge sans fuseau ; sortie d'origine hors reprise |
| erreur inattendue | — | lecteur qui lève avec un nombre : rendue par son type seul |
| déterminisme | deux courses neuves (cas D) : mêmes pièces, mêmes empreintes, mêmes commits | — |

Garde statique sur le dépôt, pour ce module : `[]` (commande de la consigne), aucun listage à relire.

## Campagne de mutations (sur une copie, dans le bloc-notes)

`…/scratchpad/mut-enchainement/mutants.py` (`4c5298ef…`), sortie `resultat-campagne-2.txt` (`d4a6fc58…`) : **38 mutants, 37 tués, 1 survivant**. Le survivant — la garde de sortie de la règle retirée de l'étape (m) — est équivalent : la même garde est rejouée par `ligne_table_c` et par l'écriture du fichier de l'étape (m). Une première campagne avait laissé quatre survivants de plus (poussage non vérifié, reste non versé, acte présent ignoré, versement de l'acte retiré) ; trois essais ont été ajoutés pour les tuer.

## Réserves

1. **La garde statique, jouée sur le dépôt, rend aujourd'hui une violation** : `scripts/chef_essais_admission_bras_a_v2.py`, ligne 508 (`taux_usd_par_unite` contient le fragment `par_unite`) — un faux positif, hors de ce programme ; l'essai `tests/test_cloisonnement_bras_a_v13.py::test_la_garde_passee_sur_src_et_scripts_du_depot_avec_ses_valeurs_par_defaut` échoue pour la même raison. Tant qu'elle reste, la commande réelle s'arrête avant tout constat (code 4). Non corrigé ici.
2. Par la règle non écrite n° 1, l'épreuve de forme de bout en bout « avec la commande réelle » (8.7 ; 13.2) ne peut pas passer l'étape (n).
3. La limite écrite en 8.7 reste : le fichier de l'étape (m) est sur le disque avant le commit ; une interruption entre l'écriture et le poussage le laisse non versé jusqu'à la relance, qui le verse avant toute autre chose.
4. La provenance de l'entrée de l'enchaînement (journal de la table A, lignes B, états de la base, comptes des lecteurs) n'est pas vérifiée par le programme : seule son empreinte est rendue. Garde de procédure, à contre-lire.
5. Le poussage pousse `HEAD` de la branche courante : un commit non poussé étranger au dossier de course part avec lui ; le commit, lui, ne prend que le dossier de course.
6. La garde statique fait trois parcours du dépôt (violations, élagués, listages), une vingtaine de secondes chacun.
7. Le programme emploie deux fonctions privées de l'analyse (`_forme_dose`, `_dose_de`), sans les changer.
8. Le déclencheur « au moins une dose en C6 » est rendu après le poussage ; c'est une information de l'étape (m).

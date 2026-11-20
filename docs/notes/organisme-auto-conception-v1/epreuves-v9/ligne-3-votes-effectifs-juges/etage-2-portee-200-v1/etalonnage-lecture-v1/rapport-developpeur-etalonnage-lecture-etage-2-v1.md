# Rapport du développeur — étalonnage et lecture unique de l'étage 2 à 200 témoins (ligne 3, organisme v9) — v1

Pièce d'instrument (classe B), écrite le 2026-11-20 par un développeur neuf, modèle O, sur le mandat
`mandat-developpeur-etalonnage-lecture-etage-2-v1.md` (`b432ce7ec9bc7fa2bb49ef7a0d24ad4ee4717af505e6cb56395e95340cfa293a`,
recalculée égale). À vérifier par un autre modèle (S), puis vérification des corrections par le même ; puis additif de code
de l'étage 2, scellé par la mère.

**Aucun verdict réel n'existe, aucun n'a été lu : tout a été éprouvé sur des verdicts factices.** Aucune commande sur un
chemin sous `archives-reponses-modeles/`. Aucun appel à un fournisseur, aucune clé, aucun réseau, aucune dépense. Aucune
écriture dans le dépôt de travail ni dans le clone de l'organisme ; aucun commit. Aucun refus de permission, de classifieur
ou de garde n'a eu lieu.

## 1. Pièces lues, empreintes vérifiées

L3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.

| pièce | empreinte | contrôle | lu |
|---|---|---|---|
| mandat (L3/`etage-2-portee-200-v1/`) | `b432ce7e…` | égale à celle donnée | en entier |
| texte v7, L3 | `4e3680d9…` | égale au compagnon | l. 1 à 417 (dont l. 243 à 389 en entier), l. 554 à 563 |
| additif 3 v3, `origin/main`, `prereg/organisme-auto-conception-v9/additif-3-preenregistrement-ligne-3-portee-200-v3.md` (`git show` redirigé) | `71b7a876…` | égale au compagnon de `main` | en entier |
| verdict « portée à 200 » v2, `origin/main`, `prereg/…/ligne-3/verdict-portee-200/verdict-portee-200-ligne-3-v2.md` | `02928723…` | égale au compagnon de `main` | en entier (issue B) |
| banc v4, L3/`code-portee-200-v4/banc_juges_scriptes_ligne_3_v4.py` | `79865552…` | égale au compagnon et à l'additif 5 | l. 1 à 1100, l. 2029 à 2051 |
| code d'appel v4, L3/`etage-2-portee-200-v1/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` | `082d19d6…` | égale à sa table | l. 1 à 300, 380 à 540, 570 à 705, 820 à 1219 ; rapport v4 en entier, rapport v1 en entier |
| générateur v3, L3/`etage-2-portee-200-v1/generateur-v3/generer_temoins_ligne_3_v3.py` | `f5de9c3c…` | égale à sa table | `composer`, `partager`, `geste_composer` (format de la banque, du journal, du partage) ; rapport v3 en entier |
| inventaire, L3/`etage-2-portee-200-v1/` | — | — | en entier (gestes 17 et 18) |
| additif 5 v2, L3/`additif-3-portee-200-v1/` (copie de branche) | `e193bc4e…` | — | l. 1 à 60 (table des fichiers du banc v4) |
| `juges_croises_v53.py` (clone de l'orchestrateur, lecture seule) | `c4c6ab12…` (vérifiée par la garde du code d'appel, dans les essais) | — | l. 1 à 70 (`lire_verdict`) ; `outils.extraire_bloc_json` |

## 2. Ce que j'ai écrit

Dossier : `…/scratchpad/developpeur-etalonnage-lecture-etage-2/etalonnage-lecture-v1/`. Chaque fichier a son compagnon
`.sha256` (pris par `env -C DOSSIER sha256sum F`).

- **`etalonner_ligne_3_v1.py`** (`37a63c9b…`). Lit la banque scellée et **le seul** fichier
  `verdicts-moitie-etalonnage-execution-K.json` (scellé). Refus nommés : un fichier de la moitié « lecture » (par son nom,
  avant toute ouverture) ; toute ligne d'un témoin de la moitié « lecture » (par son contenu, avant tout usage) ; forme du
  dépôt, plan des cinq rendus par témoin. Sur les témoins dont les deux premiers rendus (bloc A) ont été tentés : poids,
  seuil et règle choisie des bras C et P, ρ d'étalonnage, à la lettre du texte (l. 218, 219, 297), par les fonctions du banc.
  Écrit et scelle `DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v1.json` (déterministe : aucune heure dedans) et un manifeste
  (R9 : configuration et empreinte, versions, « aucune graine », commit, empreintes des pièces). Refus si le dossier existe.
- **`lire_ligne_3_v1.py`** (`334636b8…`), lecture unique. **Avant toute lecture d'un verdict**, refus : racine 2026111936
  sans autorisation (additif de code, chemin et empreinte) ; rapport de lecture déjà présent (« lecture unique ») ou dossier
  de lecture présent ; pièce d'étalonnage absente, non scellée, d'une autre empreinte, d'une autre banque ou d'autres verdicts
  d'étalonnage que ceux du dépôt ; audit de symétrie absent, non scellé, ne citant pas l'empreinte de la pièce d'étalonnage
  (donc écrit avant elle), ou portant un contrôle non tenu ; exécution plus récente que celle nommée ; journal d'une autre
  empreinte que celle du rapport d'exécution ; chemin du coffre ou de l'archive. Puis il ouvre tout, **recalcule l'étalonnage
  et exige l'égalité avec la pièce scellée**, et rend : ρ entre juges sur le bloc A, son intervalle, votes effectifs ; ρ′ de
  chaque juge, ρ′ − ρ et son intervalle apparié, mots de l. 181 ; bras U, C, S-Opus, S-Argon, F, P (moitié « lecture », bloc
  A) et R-Argon, R-Opus-2 (témoins complets de la moitié « lecture ») ; comparaisons **descriptives** (issue B : aucun Holm,
  aucun « bat de la marge ») ; témoin apparié U − R-Argon et F − R-Argon (l. 289) ; critère de `fa38f9faa24e0`, descriptif
  (l. 320) ; coût apparié relu au journal (l. 291) ; lecture par colonne (l. 295) ; table par juge (item, niveau, citation,
  lecture seconde, absents, ρ′) ; H-sévérité descriptive ; écart de stabilité ; audit « trop propre » / « trop sale »
  (l. 348, 349) ; table de l'étage 2 **en issue B** : rangs 1 et 3 seuls atteignables, « non concluant par manque de
  témoins » sous 40 témoins complets dans la moitié « lecture » (compteur coupé compris), juge « non mesuré » (plus de 10 %
  d'absents ; plus de la moitié de répétitions identiques), « ρ′ − ρ positif pour les deux juges » rapporté comme mesure ;
  **jamais « oui »** (garde interne : un mot qui commencerait par « oui » arrête le programme). Rééchantillonnage :
  `SeedSequence(2026111936, spawn_key=(clé,))`, clés en constantes `{"rho_entre_juges_bloc_A": 1,
  "ecarts_rho_prime_moins_rho": 2, "comparaisons_bloc_A": 3, "comparaisons_bras_R": 4, "lecture_par_colonne": 5}`, 2 000
  tirages, centiles, stratifié par classe. Écrit et scelle `DOSSIER/lecture/rapport-lecture-etage-2-ligne-3-v1.json` et un
  manifeste (graines, dérivations, autorisation). Le rapport se dit **aide**, jamais verdict (R13).
- **`essais_etalonnage_lecture_ligne_3_v1.py`** (`7f7f343f…`), pytest.
- Ce rapport et `table-empreintes-etalonnage-lecture-v1.txt`.

## 3. Ce qui est réutilisé du banc et du code d'appel

**Du banc de l'étage 1 v4** (`L3/code-portee-200-v4/banc_juges_scriptes_ligne_3_v4.py`, `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7`),
**par import à empreinte vérifiée** (`charger_banc` : octets lus, empreinte comparée **avant tout import**, compilés depuis ces
octets mêmes sous un nom privé ; aucune ligne de commande ni aucun tirage du banc lancé ; ses racines ne sont jamais
dérivées) ; **aucune fonction réécrite** :
`cov_intra_classes`, `rho_moyenne`, `rho_paire`, `votes_effectifs`, `tronquer_votes` (estimateur, votes effectifs) ;
`motifs`, `comptes_configurations`, `tirer_comptes`, `cov_depuis_comptes`, `_centiles`, `intervalles_rho_moyenne`,
`ee_depuis_comptes` (rééchantillonnage des comptes de configurations) ; `score`, `seuil_milieu`, `appliquer_seuil`,
`poids_covariance`, `poids_precision`, `regle_choisie` (bras C et P, règle à deux juges, arrêt `RegleInconnue`) ; `mot_fa38`.
Le prédécesseur (banc v3, `09bfe0db…`) n'est pas importé : l'additif 5 dit que le v4 ne change aucune fonction de calcul.

**Du code d'appel v4** (`082d19d6…`) : le format du dépôt (`deposer`, l. 1082 à 1133 : `verdicts-moitie-{lecture,etalonnage}-execution-K.json`,
`etat-des-juges-execution-K.json`, `rapport-execution-K.json` et ses `depots`, `journal-compteur.jsonl`) ; la garde des
chemins du coffre (`garde_chemins`, l. 303 à 322), **recopiée** dans `etalonner_ligne_3_v1.py` (copie déclarée) ; la forme
d'écriture scellée (`ecrire_scelle`, même format). Dans les essais seulement, le code d'appel est importé par empreinte et
ses `Journal`, `Compteur`, `deposer`, `TARIF_DES_CARTES` et `charger_service_des_juges` (→ `lire_verdict` de
`juges_croises_v53.py`, `c4c6ab12…`) **écrivent eux-mêmes les dépôts factices** : le format lu est celui que le code d'appel
écrira.

**Du générateur v3** (`f5de9c3c…`) : le format de la banque (`{"items", "temoins": [{identifiant_interne, classe, item,
niveau, citation, moitie, contenu}]}`) ; la moitié est lue sur la banque (le fichier du partage n'est pas lu).

`lire_ligne_3_v1.py` importe `etalonner_ligne_3_v1.py` (posé à côté de lui) **par empreinte** (constante `37a63c9b…`).

## 4. Essais

Commande (sur ma copie) :

`env -C /tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-etalonnage-lecture-etage-2/etalonnage-lecture-v1 /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider essais_etalonnage_lecture_ligne_3_v1.py`

Résultat : **37 passed in 41.85s**, en tâche de fond, sur les fichiers `37a63c9b…`, `334636b8…`, `7f7f343f…` ; aucun échec,
aucun saut. Deux passages antérieurs : une erreur de syntaxe des essais ; puis **1 échec, 36 passés**, qui a trouvé une
vraie faute (§ 6, silence 9) corrigée avant le passage final.

Juges scriptés : loi 1 de l'étage 1, emboîtée (choc commun ρ aux cinq rendus d'un témoin ; sinon choc propre au juge de
probabilité (ρ′ − ρ)/(1 − ρ) ; sinon tirage propre) ; valeurs plantées connues. Racine des essais 2026111930 seule.

| garde ou mesure | cas sain | artefact |
|---|---|---|
| bout en bout, format du code d'appel | 1 000 envois, 100 complets en lecture ; rapport et manifeste scellés ; dérivations 1 à 5 | — |
| étalonnage à la lettre | poids, seuils, règles, ρ égaux à ceux du banc recalculés depuis les erreurs plantées | — |
| grand n (2 000 témoins ; p 0,20, ρ 0,30, ρ′ 0,70) | ρ, votes effectifs, ρ′ des deux juges, ρ′ − ρ, taux d'erreur, U, F, S (§ 0), R-Argon (majorité), R-Opus-2 proches des valeurs plantées ; mot « mesure : décorrèle » ; k apparié 3 | rang 3 : ρ′ = ρ planté (1 200 témoins) → « non : un juge répété vaut le collège » |
| étalonnage qui lit la moitié « lecture » | fichier d'étalonnage lu | fichier de lecture : refus par le nom ; lecture recopiée sous le nom d'étalonnage : refus par le contenu ; une ligne mêlée : refus ; rien d'écrit |
| étalonnage rejoué ; verdicts d'une autre empreinte | — | refus |
| lecture rejouée | premier passage : rapport écrit | second : refus, rapport inchangé ; dossier présent sans rapport : refus |
| lecture sans audit de symétrie scellé | audit scellé citant l'étalonnage | absent ; compagnon retiré ; autre empreinte ; ne citant pas l'empreinte de l'étalonnage ; contrôle « non tenu » ; contrôles incomplets : refus, aucun dossier de lecture créé |
| étalonnage avant lecture | pièce scellée | autre empreinte ; compagnon retiré ; absente ; poids changés rescellés (recalcul différent) : refus |
| exécution plus récente | — | refus |
| racine 2026111936 | autorisation juste : racine retenue, aucune dérivation par l'essai | sans autorisation, empreinte fausse, mal formée, additif absent, mode inconnu : refus avant toute lecture |
| coupure au pire cas du calcul plafond v2 | 197 complets dont 100 en lecture, partiel au rang 198, arrêt au plafond : **lu**, ρ′ sur 197 | — |
| moins de 40 complets | exactement 40 : lu | 39 : « non concluant par manque de témoins », cause « plafond », ρ′, bras R non mesurés, aucun « non : » |
| classe vide parmi 40 complets | — | ρ′ et bras R « non mesurés », nommés, rang 5, aucune exception |
| juge non mesuré (absents) | 10 % pile (60/600, refus doubles et illisibles) : mesuré ; Opus 0 absent | 20 % : non mesuré, rang 1 |
| répétitions identiques | Opus : part 0 | Argon en cache : part 1, ρ′ « non mesuré », rang 1 |
| banc sans prise | — | juge à 1 % d'erreur : rang 1 « non concluant » |
| trop propre / trop sale | — | juge sans erreur : ρ « indéfini » (jamais 0), sous réserve, rang 1 ; juge dupliqué : ρ = 1, votes effectifs = 1 ; juge au hasard : trop sale, rang 1 |
| issue B → aucun « oui » | — | juges sévères (« au moins un » devrait l'emporter), ρ′ − ρ fort, 1 600 témoins : aucun « oui », comparaisons descriptives, rangs 2 et 4 jamais rendus |
| verdicts de la v9 | chemin sain | composant « coffre… », sortie de la course v9, archive (chaîne seule, aucun accès disque) : refus ; dépôt « coffre » passé à la lecture : refus |
| imports par empreinte | banc `79865552…`, étalonnage `37a63c9b…` | banc modifié : refus d'import |

Les essais écrivent dans le dossier temporaire de pytest (`/tmp/pytest-of-root/…`), hors de mon dossier (comme ceux du code
d'appel) ; ils lisent le banc v4, le code d'appel v4 et, par la garde d'empreintes du code d'appel, cinq modules du clone de
l'orchestrateur (lecture seule).

## 5. Ce que l'additif de code de l'étage 2 devra porter (pour ces programmes)

- **Fichiers et empreintes** (table `table-empreintes-etalonnage-lecture-v1.txt`) : `etalonner_ligne_3_v1.py`
  `37a63c9b02eb6483edb088ee01f7dab90aaac80127c56c24e081545831291919` ; `lire_ligne_3_v1.py`
  `334636b8b2ffe1fc1e9e3a434ea419827859d516608cbccb5f014b5c856d9830` ; `essais_etalonnage_lecture_ligne_3_v1.py`
  `7f7f343fc9f5c7eb114e95423d0fd7d03b0b1d0bf74353f2eee20311cee5ceb5` ; ce rapport ; le commit qui les verse. Les deux
  programmes **dans le même dossier** (la lecture importe l'étalonnage par empreinte, à côté d'elle).
- **Dépendance épinglée** : le banc v4 au chemin `L3/code-portee-200-v4/banc_juges_scriptes_ligne_3_v4.py`, `79865552…`
  (constante `BANC_V4`), présent au même chemin là où l'étalonnage et la lecture tournent ; les essais demandent aussi le code
  d'appel v4 (`082d19d6…`) et le clone de l'orchestrateur au commit `a41b7b50…`.
- **Commande des essais** (§ 4) et résultat attendu : **37 passés**.
- **Racine 2026111936 autorisée** pour `lire_ligne_3_v1.py` seul, par cet additif lui-même (chemin et empreinte passés en
  `--autorisation-additif`, `--empreinte-additif`) ; table des clés gelée ci-dessus ; règle
  `numpy.random.SeedSequence(racine, spawn_key=(clé,))`, numpy ≥ 1.25, 2 000 tirages. L'étalonnage ne dérive aucune graine.
- **Ordre, à la lettre de l. 297, 305 (9) et (10), 347 à 350** : (1) dépôt scellé des verdicts par le code d'appel ;
  (2) **étalonnage**, une fois :
  `python3 -I -B etalonner_ligne_3_v1.py --banque BANQUE.json --banque-sha HEX --verdicts-etalonnage DEPOT/verdicts-moitie-etalonnage-execution-K.json --verdicts-etalonnage-sha HEX --dossier DOSSIER`
  (empreinte des verdicts d'étalonnage : celle des `depots` du rapport d'exécution K) ; (3) **audit de symétrie** écrit et
  scellé (§ 6, silence 3), qui cite l'empreinte de la pièce d'étalonnage ; (4) **lecture unique** :
  `python3 -I -B lire_ligne_3_v1.py --banque BANQUE.json --banque-sha HEX --depot DEPOT --execution K --rapport-execution-sha HEX --etalonnage DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v1.json --etalonnage-sha HEX --audit AUDIT.json --audit-sha HEX --autorisation-additif CHEMIN --empreinte-additif HEX`
  (écrit `DOSSIER/lecture/`) ; (5) verdict par un agent neuf (R13). Codes : 0 pièce écrite ; 2 refus ou arrêt nommé.
- **Constantes à comparer au texte** : issue B (`ISSUE_PORTEE`, `OUI_POSSIBLE = False`, verdict `02928723…`) ; 40 témoins
  complets en lecture ; taux d'erreur dans [0,05 ; 0,45] ; demi-largeur 0,25 ; absents au-delà de 1/10 ; répétitions
  identiques au-delà de 1/2 (lues sur l'état des juges) ; 0,10 pour « nul ou négatif » ; marge descriptive 0,05 ; trop propre
  0,02 ; trop sale 0,40 et −0,2 ; 2 000 tirages ; banque de 200 (50 bons, 50 mauvais par moitié).
- **Les réponses de la mère aux silences du § 6.**

## 6. Ce que la lettre ne fixe pas (silences ; choix faits, non tranchés, portés à la mère)

1. **« Témoin complet »** : je compte complet un témoin dont les cinq rendus sont **tentés** (verdict obtenu, lisible ou
   non, ou « absent » après envoi et rejeu refusés, compté comme rejet, l. 155). Le code d'appel compte « obtenu » seulement
   (`comptes_complets`) ; les deux comptes sont au rapport. Ils ne diffèrent que si un rendu est refusé deux fois.
2. **« Non concluant par manque de témoins »** : rendu dès qu'il y a moins de 40 complets en lecture, quelle qu'en soit la
   cause (mandat : « compteur coupé compris ») ; le texte (l. 337) ne nomme ce mot que pour l'arrêt au plafond. La cause
   (motif d'arrêt du code d'appel) est écrite au rapport.
3. **L'audit de symétrie** : ni son auteur, ni son programme, ni sa forme ne sont écrits. J'exige une pièce JSON scellée :
   `{"piece": "audit de symétrie (règle R4), étage 2, ligne 3", "etalonnage_sha256", "banque_sha256",
   "rapport_execution_sha256", "controles": {verite_non_servie, consigne_servie_empreinte_attendue,
   lecteur_rend_absent_pour_illisible, appariement_temoin_verdict, juges_scriptes_parfait_et_hasard: "tenu" | "non tenu"}}`
   (les cinq relectures de l. 350). **Un contrôle « non tenu » arrête la lecture** (la mère est saisie) : c'est mon choix ;
   le texte dit seulement que l'audit est écrit avant. Les déclencheurs « trop propre » / « trop sale » (l. 348, 349), qui
   portent sur les résultats, sont calculés par la lecture et mettent le résultat sous réserve.
4. **Issue B, « ρ′ − ρ positif pour les deux juges »** : aucun rang (2 et 4 inatteignables) ; mot « non concluant sur la
   correction ; mesure rapportée : le croisement décorrèle les erreurs » (l. 343). « Indéterminé » sans « nul ou négatif » :
   rang 5, « non concluant ».
5. **Comparaisons descriptives** : ni valeur de probabilité ni Holm (ils ne portent plus rien en issue B) ; écart (bras de
   comparaison moins C), intervalle apparié, et un mot descriptif tiré de la marge de l. 178 et de l'équivalence de l. 180.
6. **Stabilité de l'étalonnage** : l'écart est rapporté ; son seuil (centile de l'étage 1) n'est pas lu, il ne sert qu'au
   rang 2.
7. **Coût apparié (l. 291)** : coût moyen relevé par juge au bloc A (journal) ; k = plus grand impair tel que k fois le coût
   d'Argon tienne sous celui du collège, lu au plus proche de 1 et 3 ; coûts illisibles : k = 3, dit.
8. **Sous-ensembles** : ρ (mesure), table par juge et lecture par colonne sur les témoins tentés du bloc A (les 200) ; bras
   U, C, S, F, P sur la moitié « lecture » au bloc A ; bras R et le critère de `fa38f9faa24e0` sur les complets de la moitié
   « lecture » (P, U, F, C y sont recalculés pour l'appariement) ; ρ′ − ρ sur les complets des deux moitiés (l. 293).
9. **Une classe sans deux témoins** dans un sous-ensemble (coupure qui ne garde qu'une classe) : grandeurs « non mesurées »,
   nommées ; mots « indéterminé ». La lettre ne le prévoit pas ; sans ce choix le programme s'arrêtait sur une erreur brute
   (trouvé par l'essai).
10. **« Taux d'erreur » du banc avec prise** (l. 182) : erreur brute (vrais rejetés et faux acceptés sur tous les témoins
    du bloc A), non l'erreur équilibrée.
11. **Absents** : base = rendus tentés des blocs A et B (comme l'état des juges) ; recalculés et comparés à l'état des juges
    (écart : refus). **Répétitions identiques** : lues sur l'état des juges (textes bruts), non recalculées.
12. **« Aucune erreur sur les 200 témoins »** (l. 348) lu sur les témoins tentés du bloc A.
13. **Lecture unique** : le rapport a une place fixe, `DOSSIER/lecture/`, à côté de `DOSSIER/etalonnage/`. Une relecture
    dans un autre dossier demande un étalonnage et un audit neufs ; le programme ne peut pas l'empêcher seul : l'additif doit
    nommer `DOSSIER`.
14. **Relances du code d'appel** : la lecture porte sur l'exécution K nommée et refuse s'il en existe une K + 1.
15. **Étalonnage** : témoins dont un premier rendu n'est pas tenté exclus et nommés ; moins de deux témoins d'une classe :
    refus.
16. **Interpréteur** : l'annexe A dit `/usr/local/bin/python3` ; les essais tournent sous `.venv` (mandat).

## 7. Écarts

1. Recherches par motif (outil de recherche) sur des **dossiers** hors du mien, pour trouver des noms de fichiers que les
   pièces ne donnaient pas : `etage-2-portee-200-v1/` (noms de l'additif 3 et du verdict de portée) ; L3 (`*.md`, noms de
   tables d'empreintes) ; L3 (mention de `code-portee-200-v4`). Lignes rendues seulement ; aucune liste de dossier.
2. La table d'empreintes du banc v4 n'a pas été trouvée par son nom ; j'ai pris la liste des fichiers dans l'additif 5 v2
   de la branche (`e193bc4e…`, non la version scellée de `main`, `581e97e5…`) et vérifié l'empreinte du banc contre son
   compagnon.
3. Lecture, hors de « ce qui fait foi », de l'inventaire, des rapports v1 et v4 du code d'appel, du rapport v3 du
   générateur, et de deux fonctions du clone de l'orchestrateur (lecture seule).
4. Quatre fichiers tirés de `origin/main` par `git show` redirigé dans mon dossier (additif 3 et verdict de portée, avec
   leurs compagnons), hors du sous-dossier `etalonnage-lecture-v1/`.
5. Un premier lancement des essais avec `-x`, hors de la commande du mandat (erreur de syntaxe ; rien d'autre).
6. Aucun refus de permission, de classifieur ou de garde.

Développeur, modèle O.

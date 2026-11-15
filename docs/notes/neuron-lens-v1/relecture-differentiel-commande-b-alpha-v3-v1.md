# Relecture du différentiel des commandes v2 → v3 → v4 de la tranche B-α de « Neuron Lens », code compris — v1

**Verdict : feu possible** — pour l'ensemble, sur la **commande v4** (`commande-b-alpha-v4.md`, `f54d5ec3…`, commit `541547fd`),
sous les consignes de R-2887, qui tiennent, et avec **une consigne de lecture à porter au feu** (point 9) et **un risque résiduel
déclaré** (point 6). Aucun défaut de code trouvé dans le différentiel ; le défaut de la première course est fermé.

Lecteur neuf (n'a écrit ni le code, ni les commandes, ni les relectures). 2026-11-15, vers 10:15 UTC. Copie détachée
`/home/user/relecture-b-alpha-v3` (tête `785b403a`, inchangée) ; le commit `541547fd` lu par `git show` et `git diff 785b403a 541547fd`.
Rien loué, aucun appel au loueur, aucun code du dépôt voisin exécuté, aucune valeur de clé lue ni écrite.

## A. Empreintes (toutes vérifiées : fichier = compagnon = table de la commande)

| pièce | sha256 (début) | état |
|---|---|---|
| `src/controle_ia/neuron_lens/b_alpha_lancer_v2.py` | `a9f0324c…` | conforme |
| `tests/test_neuron_lens_b_alpha_lancer_v2.py` | `d0452b87…` | conforme |
| `scripts/amorce_neuron_lens_b_alpha_v4.sh` | `290309c6…` | conforme |
| `scripts/depot_reduit_neuron_lens_b_alpha_v5.py` | `4d26589d…` | conforme |
| `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v5.sh` | `ea9c429b…` | conforme |
| `docs/notes/neuron-lens-v1/commande-b-alpha-v3.md` | `eaa88cc6…` | conforme |
| `docs/notes/neuron-lens-v1/journal-course-b-alpha-v1.md` | `6246960f…` | conforme |
| `scripts/essai_environnement_b0_v1.py` (commit `541547fd`) | `a96dc2ff…` | conforme |
| `scripts/essai_a_blanc_amorce_neuron_lens_b_alpha_v6.sh` | `27b83362…` | conforme |
| `docs/notes/neuron-lens-v1/commande-b-alpha-v4.md` | `f54d5ec3…` | conforme |
| `docs/notes/neuron-lens-v1/devis-b-alpha/essai-a-blanc-amorce-b-alpha-v6.txt` | `885d5442…` | conforme |

Les 24 lignes de la table de la commande v3 et les 4 lignes ajoutées par la v4 : recalculées, toutes égales. **L'empreinte du journal
de l'essai à blanc v6 que la mère m'avait transmise (`f9213d7a…`) était fausse** ; la vraie est `885d5442c9199b805b313cfd2a3ac5c98a62693e73b30fc7d1ef47947d9032d4`
(fichier, compagnon et table de la commande v4 d'accord ; correction reçue ensuite de la mère, confirmée ici par le compagnon).
Liste du dépôt réduit v5 : `0863f9c7e9e5ec9b89cf48710058974fbf6af9e90e3789e9ee9268d42ed756b2`, reconstruite trois fois (voir C).

## B. Différentiels exacts (`diff`)

- **Lanceur v1 → v2** : 7 blocs, tous déclarés — en-tête ; nom du module dans `MODULES` (l. 67) ; constante `ORIGINAL_06` (l. 129) ;
  propriété `original_06` (l. 245-248) ; copie et contrôle dans `preparer` (l. 385-391) ; champ `original_06` du résultat de `preparer`
  (l. 404) ; contrôle et variable dans `etape_b0` (l. 504-506). Aucune échéance, aucune garde, aucune autre étape touchée.
- **Essais du lanceur v1 → v2** : import ; `_faux_original` ; `test_b0_environnement_des_essais` (neuf) ; `test_b0_sain_et_artefacts`
  (reçoit la copie factice) ; trois assertions dans l'essai sur copie réelle ; `test_partie2_bout_en_bout` (neuf). 48 → 50.
- **Amorce v3 → v4** : 4 lignes (en-tête, commentaire l. 13, liste `ESSAIS` l. 54, appel du module l. 85). Rien d'autre.
- **Dépôt réduit v4 → v5** : 5 lignes (en-tête, usage, module, essai, amorce). Rien d'autre.
- **Essai à blanc v4 → v5** : en-tête, script du dépôt réduit, liste des essais réels, ligne de titre, contrôle des processus restants
  remis sur ses propres lignes (l. 204-207). **v5 → v6** : en-tête, ligne de titre, bloc « 4 bis » (9 lignes). Rien d'autre.
- **Commande v2 → v3** : tout changement déclaré est présent. **Non déclarés, sans effet sur les gestes** : (i) la table des
  empreintes perd 19 lignes de la v2 (commande v1, addendum v3, commande v14 du volet A, notes et pré-essais des correctifs, essais des
  grandeurs, de la partie 2 et du balayage, lecture des configurations, lanceur v1 et sa note, amorce v3, essai de la minuterie et son
  journal, dépôt réduit v4, essai à blanc v4 et son journal) ; (ii) le détail des cas de l'essai à blanc est résumé en une phrase.
  « Le reste est la v2, inchangée » est donc inexact sur ces deux points (les pièces restent dans la v2 archivée).
- **Commande v3 → v4** : en-tête (9 lignes), section de l'essai à blanc, 4 lignes de table. Conforme au « seul changement » déclaré.

## C. Essais rejoués (conteneur de la session, dossier de travail à part, copie détachée non touchée)

Montage, déclaré : clone de la copie dans le dossier de travail de la session ; copie de lecture du dépôt voisin (clone public déjà
présent dans le dossier de travail, arbre `b22006e9…` vérifié) reliée le temps des essais au chemin par défaut, lien retiré ensuite ;
interpréteur de travail = paquets de l'environnement du programme **plus `pyarrow` 26.0.1** (la version épinglée pour la machine).

1. **50 essais du lanceur v2** — avec l'environnement du programme tel quel : **48 passés, 1 en échec, 1 sauté**. L'échec est
   `test_partie2_bout_en_bout` : « version absente : pyarrow » (ce paquet manque à l'environnement de la session ; il est épinglé pour
   la machine) ; le sauté est l'essai sur copie réelle (copie de lecture absente du chemin par défaut). Avec l'interpréteur de travail
   et la copie reliée : **50 passés, 0 échec, 0 sauté**. Sélection de l'amorce (cinq fichiers, sans l'essai sur copie réelle) :
   **141 passés, 1 désélectionné**.
2. **Essai à blanc v6**, commit source `541547fd` : **conforme, 0 écart, code 0** — nominal 13 appels, 141 essais réels, 13 résultats
   poussés, état final ; relance sans appel ; reprise (`passe b3 measure score grandeurs verdicts`, essais non refaits) ; échec 20 ;
   14 formes refusées sur 14, 0 dans le dépôt distant ; gardes 10, 10, 17, 13, 16, 14, 12, 12 ; **environnement de B0 : conforme,
   0 écart, lanceur v1 pris en défaut (1 écart : `NEURON_LENS_ORIG` absente)** ; témoins 14 sur 14 ; 0 processus restant.
   Dépôt réduit : 347 fichiers, liste `0863f9c7…`, commit réduit `4e5b22cd…`, paquet `0c5c27fc…`.
3. **Dépôt réduit v5 reconstruit** aux commits source des deux journaux : `f5c9f662` → commit réduit `5abf65f8…`, paquet `179fd51d…`
   (= journal v6) ; `e3ebbf6b` → `b2190096…`, `dab4fbf8…` (= journal v5) ; liste `0863f9c7…` les trois fois.
4. L'essai à blanc v5 n'a pas été rejoué à part : la v6 est la v5 plus le bloc « 4 bis » (différentiel lu), et elle a été rejouée en
   entier. `essai_environnement_b0_v1.py` a été rejoué dans la v6 (code 0) ; il ne demande ni réseau ni code voisin exécuté.

## D. Points numérotés

1. **Défaut fermé — copie prise avant tout correctif.** `preparer` exige d'abord le code voisin aux empreintes d'avant
   (`b_alpha_lancer_v2.py` l. 364-367, dont `scripts/06_activations.py` = `151d1196…`, l. 73), copie (l. 385-388), contrôle l'empreinte
   (l. 389-390), et n'applique les correctifs qu'après (l. 391-399). Vu sur l'arbre préparé par le vrai `preparer` : copie `151d1196…`,
   script corrigé `b97bf54b…`. Conforme.
2. **Passée à B0.** `etape_b0` contrôle la copie puis pose `NEURON_LENS_ORIG` en chemin absolu (l. 504-506 ; `--racine` résolu, l. 858).
   Le dossier de travail de l'essai (`voisin/neuron-lens`) et `NEURON_LENS_ROOT` sont ceux de son usage. Conforme.
3. **Exigée à une reprise.** Correctifs déjà appliqués et copie absente ou altérée : arrêt dans `preparer` (l. 389-390) et dans
   `etape_b0` (l. 504-505) ; essayé (copie retirée, copie altérée). Conforme. La copie vit sous `originaux/`, hors de `runs/` et de
   `diag/` : elle n'est ni balayée ni poussée (amorce l. 123-125), et elle n'apparaît qu'après le manifeste, donc jamais avant que
   l'amorce ne lise une reprise (l. 200-205). Conforme.
4. **L'essai à blanc v5 seul ne reproduisait pas l'environnement des essais de B0** (faux lanceur, l. 42-68 : aucune variable
   `NEURON_LENS_*`, aucun fichier) ; la commande v3 le disait (« non couverts : vraie course et vrai lanceur »), mais la demande de
   R-2890 n'était tenue que par deux essais du lanceur. **La v6 la tient** : vrai `preparer`, vrai `etape_b0`, variables lues par
   chaque essai présentes, chemins existants, six empreintes écrites dans les essais résolues dans l'arbre préparé, modèle, hors ligne,
   aucun secret ; artefact pris en défaut. Conforme pour la commande v4.
5. **Limites de `essai_environnement_b0_v1.py`** (déclarer) : aucun essai n'est lancé (enregistreur, l. 59-61) et les lentilles sont
   fausses (l. 63) ; les variables sont trouvées par motif sur `os.environ.get("…")` entre guillemets doubles et sur la ligne d'usage
   (l. 31-32) ; le contrôle d'existence ne vise que deux noms écrits en dur (l. 81). Il prouve l'environnement, non l'issue des essais.
6. **Risque résiduel, non fermable sans machine** : `test_qwen3_identique_a_l_original` et `test_original_echoue_sur_llama`
   (`essai-06_activations-llama-v3.py` l. 143 et 180) n'ont **jamais** été exécutés, nulle part (ils s'arrêtaient à leur première ligne
   le 15 novembre). Ils tourneront pour la première fois sur la machine louée. Lecture sans exécution du script d'origine : il se
   charge comme le corrigé (mêmes imports, `__file__` seulement dans la voie détachée, l. 619), sept crochets par couche attendus pour
   Qwen3 : rien ne signale un échec, rien ne le prouve. Un échec arrêterait B0 comme la première fois (≈ 0,06 USD), sans autre effet.
7. **Défauts voisins cherchés, étape par étape, aucun trouvé.** Variables lues par le code voisin à `849bfe16` : `NEURON_LENS_MODEL`
   seule (`catalog.py` l. 32 ; `DROWSE_HOME` est posée par le code lui-même ; la clé de `10_labels.py` n'est pas sur le chemin de la
   course). Les trois autres essais de B0 ne lisent que `NEURON_LENS_ROOT`. Nos modules lisent `GO_ID`, `HF_HOME`, `HF_HUB_OFFLINE`,
   `NEURON_LENS_MODEL`, `COMMIT_REDUIT`, `COMMIT_SOURCE`, `INSTANCE_ID` : les cinq premières sont exportées par `appel` (amorce
   l. 266-269), `COMMIT_SOURCE` est héritée de la création (étape 7 ; essai avec et sans), `INSTANCE_ID` vide est accepté (essai).
   Fichiers attendus après B0 : références copiées par `preparer`, corpus et provenances écrits par `corpus`, résumé de `score` copié
   dans `diag/` avant `grandeurs` et `verdicts` : chaîne inchangée depuis la v1 du lanceur, relue à la v2 de la commande.
8. **`test_partie2_bout_en_bout` dépend de l'environnement installé** (`_versions`, lanceur l. 570-577, non remplaçable dans l'essai) :
   il échoue là où `pyarrow` manque. Sans effet sur la machine (paquet épinglé, essais joués après `pip`) ; dans une session sans ce
   paquet, le cas nominal de l'essai à blanc rendrait 12. Mineur, à la prochaine version des essais.
9. **Consigne à porter au feu — deux restes de « attendre son signal ».** Commande v4, préambule l. 39 (« prévenir la mère et attendre
   son signal » avant la création et la destruction manuelle) et étape 10, l. 113 (« destruction selon l'étape 15, après le signal de la
   mère ») contredisent l'étape 7 (l. 70), la règle des branches d'échec (l. 89-91) et l'étape 15 (l. 175), qui disent « préavis, sans
   attendre ». À lire comme les étapes 7 et 15 (R-2883) ; à l'étape 10 la minuterie est déjà armée, l'effet d'une attente serait borné.
10. **Renvoi inexact** : l'étape 15 (l. 175) et le différentiel (l. 23) citent la « consigne 6 » du feu pour la destruction finale sans
    attendre ; telle que R-2887 est consignée au registre, sa consigne 6 est de forme. Le fondement est R-2883, point 2. À corriger au
    texte suivant ; sans effet sur le geste.
11. **Consignes de R-2887 présentes** : prix lu ≤ 0,73 (filtre de l'étape 4, l. 53 ; étape 8, l. 92 ; minuterie au prix lu, l. 103 —
    recalculée ici par la garde v4 : 53 260 s à 0,73 ; 82 233 s à 0,4728 à l'instant de la création, soit 82 216 s dix-sept secondes
    après) ; P1 (l. 89-91) ; R1 (l. 80-81) ; R4 (l. 127-129) ; création sur préavis sans attente et refus ni rejoué ni reformulé ni
    contourné (l. 70-71). Devis : 14,7 h × 0,73 = 10,73, sous l'arrêt dur de 10,80 ; aucune échéance codée n'a changé. Conforme.
12. **Rien de dégradé** : plafond 12, compte rendu à 7,20, arrêt dur à 10,80 (étape 10) ; secrets cités par leur nom seulement, jamais
    de sortie brute du loueur imprimée (l. 35-37) ; destruction avec `-y < /dev/null` et preuve d'absence avec témoin, code 0 exigé
    (l. 176) ; arrêts par PID après lecture des arguments ; révocation de `HF_TOKEN` recommandée. Lignes inchangées depuis la v2.
13. **Branches** : résultats sur `calcul/neuron-lens-b-alpha-v2` aux trois endroits (étape 5 l. 63, étape 7, étape 12 l. 142).
    Lu sur le dépôt distant à 10:13 UTC : cette branche est **absente**, `calcul/neuron-lens-b-alpha-v1` et
    `course/neuron-lens-b-alpha-reduit-v4` existent, `course/neuron-lens-b-alpha-reduit-v5` n'existe pas encore (étape 5). Conforme.
    L'amorce v4 garde le défaut `calcul/neuron-lens-b-alpha-v1` (l. 29 et 47) : sans la variable de l'étape 7, la première poussée
    serait refusée (historique différent) et l'amorce sortirait en 14, sans calcul. Mineur.
14. **Textes périmés, sans effet** : étape 12, l. 134-135, « essais de nos modules (139 » — c'est 141 ; réserve l. 209-211 « aucun essai
    ne joue `etape_partie2` … avec l'environnement de l'amorce » — c'est fait depuis les essais v2 ; essais à blanc v5 et v6, usage
    (« …_v1.sh ») et commentaire du faux lanceur (« b_alpha_lancer_v1 »).
15. **Commit source de la course** : la commande v4 vit dans `541547fd` ; la liste attendue ne dépend pas du commit source (vérifié sur
    trois commits), le commit réduit et le paquet si. Choisir `541547fd` ou un descendant ; R1 lit le reste par programme.

## E. Non vérifié ici

L'issue réelle des quatre essais de B0 avec la copie d'origine (point 6) ; tout ce que la commande déclare non couvert (vraie course,
`pip` complet, carte, clone réel, sérialisation des arguments par l'outil du loueur) ; les étapes d'après B0 sur la machine (jamais
atteintes à la première course) ; le texte complet de la commande hors du différentiel, relu à la v2.

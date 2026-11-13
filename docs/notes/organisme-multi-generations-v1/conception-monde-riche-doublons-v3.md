# Conception — monde riche écrit par un programme et regroupement des doublons au sein d'une génération — v3

- **Statut** : conception **v3** (aucun préenregistrement, aucun GO). Elle applique la **vérification courte de la v2**
  (`verification-courte-conception-v2-v1.md`, `0d64ed1d565c8e73efcef09ad5385955347c4b635995e5e03d3f3306a2ac443c`, vérifiée
  contre son compagnon : « utilisable après corrections », V-1 à V-7). **Réserve de lignée** de cette vérification : faite par
  Claude Opus 5.5, le même modèle que moi ; elle recommande qu'un lecteur Fable relise au moins V-1 et V-5 (décision de la mère).
  La v2 (`conception-monde-riche-doublons-v2.md`, `af0d0e72…`) reste versée, inchangée (R12). La v2 appliquait la contre-lecture R2 de la v1 (Claude Fable
  5.2, « utilisable après corrections » : `contre-lecture-conception-monde-riche-v1.md`,
  `e7d5cda0c80767eb7703902e664f55a4a4b2f14aefa924c37b404b013a13c3ed`, vérifiée contre son compagnon). La v1
  (`conception-monde-riche-doublons-v1.md`, `fc9cd385…`) et ses pièces restent versées, inchangées (R12). Écrite pour la course de l'organisme d'idéation à plusieurs
  générations (accord de principe R-2442 ; mots de Lazar R-2443, R-2444, et **R-2461**). **Aucune dépense, aucun appel de
  modèle** ; essais hors ligne seulement, sur des mondes synthétiques écrits par programme.
- **Changement de cadre en cours de travail** : la consigne demandait un monde écrit par Kimi (R-2444). Message de la mère reçu
  vers 22:13 UTC : mot direct de Lazar **R-2461**, « a synthèse place en premier un monde écrit par un programme : go » ; R-2444
  est remplacé sur ce point. Cette conception suit **R-2461** : le monde est **écrit par un programme** (§2) ; l'exclusion de
  Kimi tombe avec son rôle d'auteur ; plus de devis d'écriture par Kimi. Le brouillon de consigne de Kimi
  (`consigne-kimi-monde-riche-v1-brouillon-1.md`, `de6bc5fa…`) reste versé tel quel (R12), **sans objet**. Le vérificateur
  garde son nom de prototype (`verifier_monde_kimi_v1.py`, scellé avant R-2461) : il ne dépend pas de l'auteur du monde.
- **Concepteur** : Claude Opus 5.5 (`claude-opus-5-5`), concepteur neuf, sous-agent de la session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Je n'ai écrit ni le texte v2 de la course, ni son code, ni son verdict.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-concepteur-monde-riche-doublons-v1.md`
  (`6cab9057ef201a837025bbe58ffed84633ec1ac23bdc6ccd2063b74f08f8094d`, vérifiée, égale à son compagnon) ; interdits communs v2
  (`1ee3b370…`, vérifiés) tenus : aucune lecture de `diag/`, `runs/`, des pièces du bras d'attaque, du mode tenu à l'écart,
  de 7a ou 7b, du dossier du collisionneur sur la diversité (sauf sa synthèse, après levée par la mère) ; aucune écriture git ; recherches par `git grep` avec exclusions ; aucune
  clé lue.
- **Heures v3** (relevées par `date -u`) : début 2026-11-13 00:39:49 ; sorties v3 du 2026-11-13 00:42:38 au 01:30:21 ; fin de la rédaction 2026-11-13 01:31:06 (`date -u`).
- **Heures v2** (relevées par `date -u`) : début 2026-11-12 23:08:38 ; sorties v2 du 2026-11-12 23:23:30 au 2026-11-13 00:22:41 (deux redémarrages du conteneur, vers 23:25 et 23:55) ; fin de la rédaction 2026-11-13 00:23:56 (`date -u`).
- **Heures v1** : début 2026-11-12 20:26:45 ; fin de la rédaction 2026-11-12 22:31:14 (`date -u`) ; sorties : journal `sorties-v1/journal-sorties-v1.txt` (21:15:24 → 22:12:43), compléments 21:34:46 → 21:34:57, générateur 22:16:07 → 22:30:32.
- **Synthèse du collisionneur sur la diversité** (`docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md`,
  `4f99077b7002782374060ff79d9ccaf64c78d7f0de1ac5db4f0cf054a4d89adc`, vérifiée contre son compagnon) : lue sur message de la mère
  reçu pendant le travail (restriction levée pour ce seul fichier), **après** que l'essentiel de cette conception était écrit
  et ses sorties lancées ; écrite par l'opérateur du tour, **non contre-lue** : traitée comme une entrée à discuter. Ce qu'elle
  change ici et où je diverge : §3.8 et §5.4. Je n'ai ouvert aucune autre pièce de ce dossier.
- **Interpréteur** : Python 3.13.18 et numpy 2.5.3 du système (l'environnement `.venv` n'a pas numpy) ; le scellement par
  `.venv/bin/python -m controle_ia.scellement`.
- **Langue** : « loi » = loi prédictive (probabilité de chaque issue sachant les traits d'une instance) ; « nat » = unité
  d'information (logarithme naturel) ; « gain » d'une loi = gain moyen de log-score par instance sur la loi qui ne connaît que
  la fréquence des issues ; « au-delà de l'archive » = gain moins celui de la meilleure loi de l'archive (sens de l'oracle
  v60) ; « au-delà de l'enveloppe » = gain moins celui du meilleur membre du nul v8 engendré par l'archive (sens neuf, §1.7).

## Changements depuis la v2

Corrections exigées par la vérification courte (`0d64ed1d…`), appliquées une à une ; script neuf `outils-v3/puissance_monde_riche_v3.py`
(`60aee2a3…`) ; sorties neuves `sorties-v3/`, **par parties d'un monde scellées chacune**, un seul processus à la fois
(`ulimit -v 6000000`, `OMP_NUM_THREADS=2`), journal `sorties-v3/journal-sorties-v3.txt`. Aucune pièce v1 ni v2 n'est modifiée.

| # | correction exigée | ce que fait la v3 | où |
|---|---|---|---|
| V-1 | la tranche de choix n'était pas appariée dans le code (une tranche différente par candidat) | **une tranche par groupe, commune à tous les candidats**, tirée de la tâche du groupe (empreintes canoniques triées de ses membres) ; `representant`, `doublons` (représentants) et la condition « regroupement » des générations **refaits** ; garde 25 : tranche recalculée à l'identique ; la proposition « 2 000 épisodes » ne vient qu'après l'appariement. Mesure : sur 82 groupes, perte au-dessus de 0,01 nat dans 1 groupe (maximum 0,038, contre 0,167 en v2), jamais sous g₀ ; doublons : 5,00 idées par groupe retenu contre 4,92 en v2. | §3.4, §3.6, §1.6, §3.7 |
| V-2 | `python3 -I` ignore `PYTHONHASHSEED` : la graine de hachage n'était pas fixée | texte corrigé : **déterminisme par parcours triés, établi sous trois graines de hachage** (deux lancements v2 à graine aléatoire, égaux ; un rejeu de la vérification à graine effective 2, égal) ; le champ `pythonhashseed` des sorties v2 se lit **« non fixé »** ; les sorties v3 disent la graine en vigueur (`graine_de_hachage`) | §1.6, changements v1 (E-2) |
| V-3 | deux renvois faux | §2.4 : renvoi à `banc-generateur-w12-v2.json` (inexistant) retiré ; §4.1 : `attribution-w12-v2b.json` (`3c4d00c8…`) | §2.4, §4.1 |
| V-4 | m = 44 sans décompte | **règle de m écrite** : m = cartes (6 par proposeur) + vraies plantées (12 : le monde, au plus 9 « K1 + un effet », 2 diluées) + fausses (F1 à F4, F5) + copies (4) + H1 + instruments (T-ELIM, T-MAL) = **48** à quatre proposeurs, **54** avec Kimi ; les simulations ont pris 44 (seuils plus bas d'environ 0,087 nat), à refaire au banc | §3.3, §1.6 |
| V-5 | le test « taille de l'archive » garde W₋ᵢ dans l'archive | lecture **restreinte** au §0 et au §1.6 : il mesure le coût d'ajuster le mélange sur plus de membres, **pas** la surdité contre une archive réaliste ; le §1.8 demande au banc des archives **sans W₋ᵢ**, faites des retenues simulées d'une génération 2 | §0, §1.6, §1.8 |
| V-6 | devis de Q-12 (b) ; borne par test | « + 9 » (F1 à F4, F5, 4 copies ; H1 promue **non testée**, lue à la promotion) : Q-12 (b) **445** sur crédits, total ≈ **496** ; Q-2 et Q-12 disent que la borne de 1,50 USD par test d'Opus est elle-même un plafond qui produit des « non concluants », et qu'Opus n'a jamais tenu ce rôle | §6, Q-2, Q-12 |
| V-7 | Q-11 oubliait ce que la conception établit sur le latent | enjeu et inconvénients de (b) et (c) complétés : une composante latente n'est presque jamais « captée » (4 sur 23) et D2 l'exclut ; recommandation revue | Q-11 |

Suggestions reprises : **T-1** (pertes comptées par situation), **T-2** (central un peu bas, ≈ + 4 USD à 2 × 3), **T-3** (aucune
reprise d'un appel de proposeur : une session en échec arrête la course, comme la v67), **T-4** (la règle « moyenne de puissance
≥ 0,5 » **remplace** la règle « indétectable : refus » de la v1), **T-5** (fichier laissé ouvert par `mesurer_fuite` : à fermer
dans le code v68).

## Changements depuis la v1

Corrections exigées par la contre-lecture (`e7d5cda0…`), appliquées une à une ; outils neufs sous `outils-v2/` (les outils
v1 sont importés tels quels, aucun n'est modifié) ; sorties neuves sous `sorties-v2/` (journal `journal-sorties-v2.txt` ;
déterminisme par parcours triés — la v2 écrivait « `PYTHONHASHSEED=0` fixé », ce qui est faux sous `python3 -I` : V-2).

| # | correction exigée | ce que fait la v2 | où |
|---|---|---|---|
| E-1 | le médoïde peut choisir un membre affaibli ; « borné par ε » est faux | phrase retirée ; **règle v2** : couverture **dirigée** minimale (le membre dont le nul couvre le mieux les autres), égalités par une **tranche de choix** fraîche hors juge, puis empreinte ; sort du groupe écrit ; simulations refaites avec cette règle. Mesure : sur 82 groupes, médoïde v1 sous g₀ à tort 11 fois (perte max 0,44 nat), règle v2 jamais (perte max 0,167, 6 groupes au-dessus de 0,01, tous départagés par la tranche de choix). | §3.4, `monde_riche_outils_v2.py`, `representant-w12-v2.json` |
| E-2 | sortie « générations » non reproductible au-delà de la génération 1 | ensembles parcourus triés (`PYTHONHASHSEED` sans effet sous `python3 -I` : V-2) ; rejeu sous une autre graine de hachage : les mondes 0 et 1, rejoués sous `PYTHONHASHSEED=1`, sont égaux champ pour champ aux mêmes mondes de la sortie principale (graine 0), générations 1 à 3. | §1.6, `puissance_monde_riche_v2.py`, `reproductibilite-…-v2.json` |
| E-3 | n = 400 ne se gèle pas sur le juge simplifié | n n'est plus recommandé comme valeur : **règle écrite d'avance**, appliquée au banc de calibration avec le code v68 gelé (§1.6) ; m = 44 sur le décompte du dessin ; puissance selon la taille de l'archive mesurée (faibles 0,54 à 1, 8 et 16 lois d'archive ; moyennes 0,93 à 0,85) ; intervalles de détection rapportés avec le nombre de **lois distinctes** par tranche | §1.6, §1.8, Q-5, `archive-w8-r30-v2.json` |
| E-4 | simulations sur une sous-famille (gabarit fixe, sans latent) | toutes les simulations v2 tirent leurs mondes du **générateur v2** (gabarits tirés, latent possible) ; dit | §1.6, §3.6, §4.1 |
| E-5 | latent mal compté (refus C1 d'un dixième des tirages) ; règle C8 non codée | latent compté à part (classe « latente », 0 ou 1), taille et poids tirés ; règles C8 codées ; fréquences réalisées rapportées | §1.2, §2.3, §2.4, `generateur_mondes_v2.py`, `verifier_monde_v2.py` |
| E-6 | régularités du générateur plus nombreuses que dites | chacune classée : retirée (sortes tirées uniformément par classe, fortes non toutes principales, trait de condition tiré, seuils continus et signés, latent à constantes tirées) ou **déclarée publique** (liste) | §2.1 |
| E-7 | C7 bloquant sur des coïncidences | C7 devient une **mesure** (touches à deux décimales listées) ; refus seulement sur égalité à six décimales ; à éprouver sur les pièces gelées au banc | §2.3, `verifier_monde_v2.py` |
| E-8 | hypothèses de la preuve non écrites | (a) membre tempéré « sans preuve » du nul v8 ; (b) arrêt des valeurs e supposé conforme au code gelé non lu ; (c) la preuve ne borne pas les fausses découvertes au sens de l'oracle ; α n'est pas repris comme borne de cette part | §3.3, Q-9 |
| E-9 | le pire cas n'en est pas un | pire cas **par formule** (`devis_multi_generations_v2.py`) : vraies plantées replantées à chaque génération (13 au plus), tests ajoutés par Kimi proposeur, borne par test propre à l'expérimentateur, test coupé = « non concluant » ; « fausses non testées » devient une **question** (Q-12) ; plafonds revus | §6, Q-12 |
| E-10 | Q-8 prêtait à Lazar des mots de la consigne | reformulée sur son mot R-2443 (« il faut regrouper les doublons au sein d'une même génération ») | §3.8, Q-8 |
| E-11 | « certifiée » sur 100 graines sans intervalle | 200 graines, **borne basse de Wilson ≥ 0,8** ; libellé « détectable quand le reste du monde est connu » partout | §1.2, §2.3, §4.1 |
| E-12 | garantie et secret | garantie dite **de procédure** ; engagement machine inscrit et poussé **avant** la phrase de Lazar ; secret et mondes **hors dépôt** jusqu'au verdict ; empreinte du générateur v1 corrigée (`46f3ac2d40ef…`) | §2.1, §2.2, §2.5, Q-3, Q-10 |

Suggestions reprises (toutes jugées sûres) : **S-1** (comparer au banc trois formes de la valeur e de groupe), **S-2**
(réinjection des sœurs après la course), **S-3** (catégorie « recombinaison » à la lecture), **S-4** (« réduit les doublons sans
les supprimer »), **S-5** (deux mondes : lecture par monde et règle de divergence), **S-6** (plafonds de session par modèle),
**S-7** (liste blanche de dossiers privés, codée), **S-8** (fidélité à la synthèse : trois précisions), **S-9** (refus par
contrôle rapportés, C5 et C6 compris). Questions ajoutées : **Q-9** (vraie découverte et tolérance des fausses découvertes),
**Q-10** (publication du générateur et garde du secret), **Q-11** (sens de « traits cachés »), **Q-12** (tester les fausses
promues ; politique de plafond).

## 0. En dix lignes (v2)

1. **Monde riche, écrit par un programme** (R-2461) : 8 traits, 3 sous-populations, 3 issues ; forte 2, moyenne 2-3, faible 2-4,
   plus un trait latent non observé compté à part (un monde sur trois) ; sortes tirées par classe ; tailles mesurées (forte
   0,10-0,25, moyenne 0,04-0,08, faible 0,02-0,035 nat, au voisinage de g₀ = 0,02) ; au moins deux leurres ; compilé dans la
   grammaire existante.
2. **Générateur v2** : aucune loi dans son code ; graine tirée d'un secret machine engagé et poussé **avant** la phrase de Lazar ;
   régularités de la v1 retirées ou déclarées publiques (§2.1) ; garantie **de procédure**, secret et mondes hors de tout dépôt
   jusqu'au verdict. Banc : 8 mondes conformes sur 8 (5 retirages) ; fortes et moyennes toutes certifiées, faibles toutes proches du seuil.
3. **Vérificateur v2** : C7 devient une mesure (refus seulement sur égalité à six décimales) ; C8 à 200 graines, « certifiée
   détectable quand le reste du monde est connu » sur la borne basse de Wilson ≥ 0,8 ; règles codées.
4. **Juge** : simplifié, étalonné sur la v67 en un seul point ; il **indique** n ≈ 400, il ne le gèle pas : n se fixe **par une
   règle écrite d'avance**, au banc de calibration, avec le code v68 gelé (Q-5) ; m par une règle écrite : 48 (54 avec Kimi).
   Ajouter des lois partielles à une archive qui contient déjà le reste du monde ne coûte presque rien au juge simplifié ; la
   surdité contre une archive réaliste de génération 3 n'est **pas** mesurée (V-5) : demandée au banc.
5. **Doublons, étape A** (avant le juge, programme) : équivalence prédictive au sens du nul, ε = 0,01, lecture par strate
   (ε_strat = 0,04), liaison complète ; valeur e du groupe = moyenne ; e-BH sur les groupes ; preuve écrite **avec ses trois
   hypothèses** (§3.3).
6. **Représentant v3** : couverture dirigée minimale, égalités par **une** tranche de choix fraîche hors juge, commune au groupe (V-1) ;
   perte maximale 0,038 nat sur 82 groupes, jamais sous g₀ à tort (v2 non appariée : 0,167) ; le médoïde
   v1 tombait sous g₀ à tort 11 fois ; groupe éliminé si son représentant meurt, sœurs réinjectées après la course.
7. **Effet mesuré (famille tirée)** : même part de composantes captées avec ou sans regroupement (0,937 en génération 2, monde par monde identique), archive plus petite d'un tiers (16,3 lois contre 24,8) ; fausses découvertes au sens de l'oracle 12 à 19 % des retenues (au-delà de α, Q-9) ; sur 24 cartes, le regroupement retient 7,8 lois au lieu de 16,7 et perd en moyenne 0,33 idée sur 5,33 (v3 ; 0,4 en v2) ; une fusion à tort d'un ajout faible sur 12.
8. **Diversité** : D2 par l'oracle lu une fois (composantes certifiées couvertes, au-delà de l'archive, sur propositions brutes,
   représentants, retenues ; catégorie « recombinaison ») ; D1 descriptive ; jamais un critère (N-058).
9. **Proposeurs** : Fable 5.2, Opus 5.5, Argon, Astra (Kimi si rechargé, ses tests comptés) ; expérimentateur Opus (borne 1,50
   USD par test, test coupé = non concluant) ; réponses brutes et témoins d'isolement versés.
10. **Devis au vrai pire cas** (formule) : à 2 mondes × 3 générations, ≈ 41 USD attendus, **409 au pire** (365 sur crédits de
    Claude, 57 hors crédits avec la machine) ; douze questions pour Lazar (§7), dont quatre neuves (Q-9 à Q-12).

## Pièces lues (chemin, empreinte)

| pièce | chemin | sha256 |
|---|---|---|
| texte scellé v2 de la course | `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` | `80fe4f03b4905b2376b8cd16873c9ab93da3b97e4e01a9a2932be329bab0954d` |
| verdict de la course v67 | `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` | `d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459` |
| script de puissance v1 et sa sortie à 1 000 répétitions | `docs/notes/organisme-boucle-reelle-v1/puissance-boucle-reelle-v1.py` ; `sorties-puissance-v1/puissance-boucle-reelle-v1-r1000.json` | `a2afcdd3…` ; `a23959fa…` (texte v2, en-tête) |
| complément génération 2 | `docs/notes/organisme-boucle-reelle-v1/puissance-boucle-reelle-v1-generation2.py` | `f552b1b9…` |
| patch du code v66 (cœur `boucle_reelle_v66.py`, juge `juger_v66`) | `docs/notes/organisme-boucle-reelle-v1/code-v66/organisme-v66-contre-cef5ea6.patch` | compagnon `.sha256` |
| orchestrateur v52b : grammaire et juge par pari, nul des filles, nul de l'archive, e-BH, monde du noyau | `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/selection_pari.py`, `nul_filles_v2.py`, `cycle.py` (`membres_de_l_archive`, `appliquer_multiplicite`), `monde_noyau.py`, `outils.py` | compagnons `.sha256` |
| monde S-V1 | `docs/notes/ideation-organisme-v1/orchestrateur-v52b/exemples/temoins-pari-demo-v1.json` | `fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877` |
| devis de la course v66 | `docs/notes/organisme-boucle-reelle-v1/devis-boucle-reelle-organisme-v1.md` | `60643868de86bb5be71393283e6ecf8dc7c03998a072519bc479af8943a26437` |
| plan chiffré des crédits de Claude | `docs/notes/credits-claude-v1/plan-chiffre-credits-claude-v1.md` | `8f9ee89e7c31535cb57e054531e02a4fc5202e6978318fc682af369845bf8c47` |
| GO-2026-11-12-01 à -06 | `registres/go.md` l. 308-313 | (registre vivant) |
| R-2389, R-2440 à R-2444 | `registres/decisions.md` l. 2347, 2398-2402 | (registre vivant) |
| prix de Kimi | `docs/notes/ideation-organisme-v1/relais-kimi-v1/LISEZMOI-relais-kimi-v4.md` l. 57-58 | `e5d6c5ce3a0d243b6a3d804f7de47539d11807ff1561174712428e40399db17a` |
| prix supposés d'Argon et d'Astra | `…/configuration-v8/commandes-v6/commande_argon_v56_nuit_v6.py` l. 234 ; `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py` l. 79-82 | `5eae1a04…` ; `22e5ed8a64075f2f985755d9bff2c2336d8edc5f73cbc3b0511405fd8f43d264` |
| validation du nul v9 (audit du verdict : « puissance perdue ») | `docs/notes/ideation-organisme-v1/validation-nul-v9-v1/audit-verdict-validation-nul-v9-v1.md` | `9086a420a082ed8fd7d76dc666ef5ef336a9f6842be8ff90e4aca7db0d72f7c8` |
| N-045 v2, N-049, N-050, N-053, N-058, N-064, N-065 | `docs/decisions/` | `c7b05e39…`, `8a5bf5e5…`, `a54b128d…`, `2204256d…`, `854f2724…`, `387c9d4e…`, `f820e90d…` |

**Ce que je n'ai pas pu lire** : le code gelé de la course (`a_blanc_v59.py`, `nul_v8.py`, `oracle_tour_ferme_v60.py`,
`boucle_reelle_v65.py`, `tests_de_mort_v5.py`) n'est pas dans le dépôt de travail ; les paquets git v66 et v67 exigent le
commit `94bfd92` (absent ici) ; je n'ai rien cloné. D'où le **juge simplifié** (§1.6), étalonné sur les chiffres publiés, et
les points « à vérifier dans le code gelé » du §1.3.

## Pièces écrites (v1, v2 et v3 ; toutes scellées, compagnon `.sha256`)

Chemins relatifs au dossier `docs/notes/organisme-multi-generations-v1/` ; chaque pièce a son compagnon `.sha256` (vérifié par
le script qui a écrit ce tableau). Les documents v1 et v2, la contre-lecture (`e7d5cda0…`) et la vérification courte
(`0d64ed1d…`, pièces de leurs auteurs) figurent au tableau ; ce document v3 est scellé à part. Pièce échouée gardée :
`sorties-v3/generations-a2-v3-resume.json` (résumé vide des 12 parties en échec de la v3, remplacé par la v3b).

| pièce | sha256 | compagnon |
|---|---|---|
| `conception-monde-riche-doublons-v1.md` | `fc9cd3854f11625212b924fdcc4c4f4cbf61dff85656d34d01861e78e673900f` | oui |
| `conception-monde-riche-doublons-v2.md` | `af0d0e72927db409edf8a5ee0d348a93d5d7404409d61dde45a110d670524a5f` | oui |
| `consigne-kimi-monde-riche-v1-brouillon-1.md` | `de6bc5fa29d437cdd32e92a688e86430ec5750cd4ebb0ebaeac82fc26fb45d83` | oui |
| `contre-lecture-conception-monde-riche-v1.md` | `e7d5cda0c80767eb7703902e664f55a4a4b2f14aefa924c37b404b013a13c3ed` | oui |
| `verification-courte-conception-v2-v1.md` | `0d64ed1d565c8e73efcef09ad5385955347c4b635995e5e03d3f3306a2ac443c` | oui |
| `outils-v1/complements_synthese_v1.py` | `89eb7ba8c8cf8633541a6de8090767f74619e3f3968ebed8f894b1f8d593e9ba` | oui |
| `outils-v1/devis_multi_generations_v1.py` | `15256924d4373d52f560aebfb9550c8e85e19b3faa7bfee8bf4267d7bbdc43b1` | oui |
| `outils-v1/essais_complements_synthese_v1.py` | `1217d25590b6d76360aa38febc20c2d67d07585fc212eb051899012f98ecc989` | oui |
| `outils-v1/essais_generateur_mondes_v1.py` | `50aa0b9249090917327d0987f5da36394a85e57160b3b154abd59fa543d226ec` | oui |
| `outils-v1/essais_monde_riche_v1.py` | `fe97097bd594d245ebe2a8b8f2adb4b68754b565f1a19f4f5517b4b8858fe5a4` | oui |
| `outils-v1/etalonnage_urne_v1.py` | `c142c77f14d3eeb09da7ff407f02e3808564c52623b38d3c87035a580a095de7` | oui |
| `outils-v1/faire_exemples_v1.py` | `403bd260a9f180d17f6013d10c810f73730408256a46b09e9f897ea025bd7eea` | oui |
| `outils-v1/generateur_mondes_v1.py` | `46f3ac2d40efad200e382d95450d3683529f96a73e716913dbbaf24a3bceb1c5` | oui |
| `outils-v1/lancer_sorties_v1.sh` | `f3f99261fcd15d0a814753b2acaad66b751ade4889a80e1011f5fb4226d95b50` | oui |
| `outils-v1/monde_riche_outils_v1.py` | `1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e` | oui |
| `outils-v1/normes_coefficients_v1.py` | `a2a6bfffdd001ac30d353ee4913d6857c4714128f5f50ca9b1ef53cf0f672a44` | oui |
| `outils-v1/puissance_monde_riche_v1.py` | `7344b10781928eaf123f6fe27e0370a0be2963c6632665a411a1673d177d844b` | oui |
| `outils-v1/variantes_v67_v1.py` | `8b5b6896e211174da09142d4a907011b083611e21fa0284141af5f49bd1d9a5b` | oui |
| `outils-v1/verifier_monde_kimi_v1.py` | `679f437d966fd2d184885ed77e28b152d76d46f2ca096d58330cf755ff189d7d` | oui |
| `outils-v2/attribution_v2b.py` | `dee69027a5d310641bd3b7e6b7316b1bdb54b051005ed20497fcf5f38fa605c0` | oui |
| `outils-v2/banc_generateur_v2.py` | `4717cc961d6951c8bb000aa9bd4f66061eb8bd805a8f87ebac9f2d070f8ba758` | oui |
| `outils-v2/banc_generateur_v2_partie.py` | `168ed32b48a483d4182f86e29284d54a180539adb9f3067ba74e54b1705f45a4` | oui |
| `outils-v2/devis_multi_generations_v2.py` | `710954c7cf3fd144139625a1416d36530f54e2dfdd48adc0f3e34831168bef86` | oui |
| `outils-v2/essais_v2.py` | `9cf54cbc95c85ad68004bf0bd1e56266bf608dfa46239d1677047112cfdc5d21` | oui |
| `outils-v2/generateur_mondes_v2.py` | `816ad7182c5980f0c25057404d53e62d1ba29643275749fd2c4238f3d2cf7fc2` | oui |
| `outils-v2/lancer_sorties_v2.sh` | `50829737950625801b35cf36c4ca28fe8cc6428644638af6f38038ce09f11d7d` | oui |
| `outils-v2/monde_riche_outils_v2.py` | `3fab97a15a20c58c4d966a0df1c8aaaa0347b672f401eaa4613e40db7b8a17c6` | oui |
| `outils-v2/puissance_monde_riche_v2.py` | `12458ee3dd362b73e14f0152e118932c8530ded927db07d89cad908eada20c86` | oui |
| `outils-v2/verifier_monde_v2.py` | `d8f2f6348e0fbdbf1237ff5228b7f57a725fcf82c1a0e9945e37c149cf4c1de3` | oui |
| `outils-v3/puissance_monde_riche_v3.py` | `60aee2a3c230da8805e765695b16835c77c20b411f813e97442a2e302dc6b805` | oui |
| `outils-v3/puissance_monde_riche_v3b.py` | `81fd0338ac63071a7726496c9bb9a980b21fe90b51717cefa26f4107f702df1e` | oui |
| `sorties-v1/attribution-w12-v1.json` | `816a7477ab22e63047a48ce3228cc131cb3a0fdd38d0829ce0cf756840b17653` | oui |
| `sorties-v1/attribution-w12-v1.stdout` | `b96ca25d8a3bb7e322ae40c1d0ebd33d0a97743170d5dbb4ce00d886c706712b` | oui |
| `sorties-v1/banc-complements-synthese-v1.json` | `c3f90d88782cf089ad5e82b12e6118273aeabfd567e4af878de68dc65d9f35bb` | oui |
| `sorties-v1/banc-generateur-w12-v1.json` | `f6574bc5ada1ba762d8646b0452ae375d1263a8acb7c65a1abcef39748933865` | oui |
| `sorties-v1/banc-generateur-w12-v1.stdout` | `7508816e85d8e4ade9e34cec1a1d8be12ace90b9b9c9cd1f42ffe28e06dbc854` | oui |
| `sorties-v1/complements-v1-heures.txt` | `c357121de5ec7dc15dd109315547e881d49d1d8cedac95dc6ae1d1a0be308cae` | oui |
| `sorties-v1/detection-w12-r40-v1.json` | `8da67edd2b64f93970a9b5f3f5f67c58c08e05797994f3615a3062fe6aab89b7` | oui |
| `sorties-v1/detection-w12-r40-v1.stdout` | `4f47348d322b16063efc19a74a283742f46c0a5382a812e5bbbb2e90472fbb7b` | oui |
| `sorties-v1/devis-multi-generations-v1.json` | `07162b53ad019f4ac3c2a19486c14cd6f6397fc6be931b17f69313fe1e999466` | oui |
| `sorties-v1/devis-multi-generations-v1.stdout` | `c68068435449e14baafab00932b185ba3426f0a55a40ec603595a4649a79ef95` | oui |
| `sorties-v1/doublons-w12-v1.json` | `2e8cb29bb4263a13e9b3724ead768be38391260e19bd89becc500bccdaa29d99` | oui |
| `sorties-v1/doublons-w12-v1.stdout` | `fde10d676b8a98330e2e9075d4b73d79a9f3d8ae0dee11f2badaf26869459d2d` | oui |
| `sorties-v1/essais-complements-v1.stderr` | `cfaa7ea37d53cf78dad189b2e41686969a015bcc47ff36f2a307b3da494acd08` | oui |
| `sorties-v1/essais-complements-v1.stdout` | `17bc5ccaf22bc9d92de94d5780e0919bfe6e81af2acd2193f6f255ebcfeb3e47` | oui |
| `sorties-v1/essais-generateur-v1.stderr` | `6235fc95aea5b1fcb176565ab2150f96f6b6d2968eed5811e25a552a68475cec` | oui |
| `sorties-v1/essais-generateur-v1.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | oui |
| `sorties-v1/essais-v1.stderr` | `16326af418817262c8c86a34858a07365577e7664f8e9cddab88e6de15fad6e0` | oui |
| `sorties-v1/essais-v1.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | oui |
| `sorties-v1/etalonnage-r1000-v1.json` | `3ee96059581c5281a385e08a037c980ffce0eb8d00d0c0bef933229106268f43` | oui |
| `sorties-v1/etalonnage-r1000-v1.stdout` | `77ff0ab224584d1b5b5b351af7c0d73f44193121715209619ddf22aaaa4b4cc8` | oui |
| `sorties-v1/etalonnage-urne-r300-v1.json` | `c87f964d87dd9610874e8270c1639549f586b4ecdf49786e20e2239a1ffd4e60` | oui |
| `sorties-v1/etalonnage-urne-r300-v1.stdout` | `57c4255661f068120545472061dab12d2f96a5e894f3fa439bb5d8e78584cec6` | oui |
| `sorties-v1/etalonnage-urne-v1-heures.txt` | `994b5f03174aed3a6394664e699a67691b16468a0ab6c4f508e2c2f94e836407` | oui |
| `sorties-v1/exemple-devis-synthetique-v1.json` | `71f20cd05b17876351d0c9ad20c2a7da0170e38d1335a7f0ce5d5420dbe9d0dc` | oui |
| `sorties-v1/exemples-v1.stdout` | `682f4398854f8d8706f0836b9e731b8640c7b34e439e8620934c43ea96c075af` | oui |
| `sorties-v1/exigences-monde-riche-v1.json` | `6076cade5539d0d1bdfd6576a0b240d6180d918133a2810c94d69eb320d46c34` | oui |
| `sorties-v1/generateur-v1-heures.txt` | `8514b74524165e2c26392f8ca69e3678c8f9246f0a413ee86916cbf81591a618` | oui |
| `sorties-v1/generations-w12-g3-n400-v1.json` | `86c7ac0edeb12f12826476de6ab4a922ebee8dc0ed9be076f19d033613516c6a` | oui |
| `sorties-v1/generations-w12-g3-n400-v1.stdout` | `673c50c8fa5f417989643270fb68c595004eec505fc8f41ef806cbab7a8e8e50` | oui |
| `sorties-v1/journal-sorties-v1.txt` | `20c556d44d84f92bf1e024ce69ab4845e273401018c3b676fe7997538649012c` | oui |
| `sorties-v1/normes-coefficients-v1.stdout` | `77e35825879567d028bc0254b08fb363db91bf600c3405928a201c0da73fa5c5` | oui |
| `sorties-v1/rapport-verificateur-exemple-synthetique-v1.json` | `c0ec4238c95a575c349294bb23c69e9dfda2fa215ecf84bc826fc034377ee1f4` | oui |
| `sorties-v1/variantes-v67-v1.stdout` | `3a7a0197d72da177c97780e9a8c9a0982468cfa63c7a562e946ed0f0112eb67f` | oui |
| `sorties-v1/verificateur-exemple-v1.stdout` | `e53936eb6ae969f89467c4162006f4c07e878c8f714747b4728b41a0c4a8fbd8` | oui |
| `sorties-v2/archive-w8-r30-v2.json` | `a631ad4744b0722d541af33ffd63a34d85d6beb46f212ba55441f90b76d71c40` | oui |
| `sorties-v2/archive-w8-r30-v2.stdout` | `8363564e09e81ce7503eac1ade996fb89e12461a196b2315dd21fe85c0ec6de7` | oui |
| `sorties-v2/attribution-w12-v2.stdout` | `a793daf79e197204834f6caa9dfef0e72244426e8e854cb66f5ed341535e803d` | oui |
| `sorties-v2/attribution-w12-v2b.json` | `3c4d00c81a23938c3f91f9266fe7047a97644e1947d5f0242e33b2e88de13a6d` | oui |
| `sorties-v2/attribution-w12-v2b.stdout` | `85c60d8faf4a8f6d3a594d5278c3fd65f5019d9e73a17ce43a72f3672ac9e0a6` | oui |
| `sorties-v2/banc-generateur-v2-frequences.json` | `fa8e5ae26f1ac16aca6ac397f4711f6570180f16835dd0879e335e7e19f8da72` | oui |
| `sorties-v2/banc-generateur-v2-monde-0.json` | `c1b9e32717ba2ec3b231aeb40e0c667955c6c408bf35622643f015ac5f938780` | oui |
| `sorties-v2/banc-generateur-v2-monde-1.json` | `a3972dd8ff29148c3a4445533176f7cebe560a82c860cad9d8848b6d50335db7` | oui |
| `sorties-v2/banc-generateur-v2-monde-2.json` | `c7c92dd00dcf24126f540e7c1f98cfd100acf136a8090cd7709cd8105c1d7764` | oui |
| `sorties-v2/banc-generateur-v2-monde-3.json` | `b60a8ac8ed3fe29f0e42a315d0931063bda971c0e14534f08b4e6cf5f691fd25` | oui |
| `sorties-v2/banc-generateur-v2-monde-4.json` | `4d8e75d04a859211b81a06b5d49cb2194ce376f4aab168593f07f29eb21a2bbb` | oui |
| `sorties-v2/banc-generateur-v2-monde-5.json` | `421fb4508cd3d6eced5c35f07cdce0688fdbaf89ca805b4a20835bf427026d07` | oui |
| `sorties-v2/banc-generateur-v2-monde-6.json` | `f38dc66b7a9b9a539c07402a4b9c858e47e5dcad9e5a7cc8cf9f703ea7690284` | oui |
| `sorties-v2/banc-generateur-v2-monde-7.json` | `7199affbc2847bd839c2ef2a04c735ea1f3a68ce7d75df1a60989f502d8e7247` | oui |
| `sorties-v2/banc-generateur-v2-resume.json` | `26e1527aa01cc5be3bca4866e4e800dd8d8f15f3d9f766a13aa0373a77b1c656` | oui |
| `sorties-v2/banc-generateur-w12-v2.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | oui |
| `sorties-v2/detection-w12-r40-v2.json` | `6a3d14446e4059bf7ade74c980f30d214ec847690e5ea444544f48e849f313dc` | oui |
| `sorties-v2/detection-w12-r40-v2.stdout` | `2c1531e81dee2a89c769b455b753892e8d188c5942c6b212b8dc82364fa31b81` | oui |
| `sorties-v2/devis-v2.json` | `c722b8020e67a967ac5440bd0410afe27569216ccb78e6e13633a52df883f313` | oui |
| `sorties-v2/devis-v2.stdout` | `42e85832a64a469989e19bf78030e63282d06a3b82109f94fde95f2a1d6c52b2` | oui |
| `sorties-v2/doublons-w12-v2.json` | `984df2bafef31527eaf7df5ac02ce714d166abc1948b06d0777f515056869dfa` | oui |
| `sorties-v2/doublons-w12-v2.stdout` | `831e253ba2e91d7a94d9107bdf1c32af0def4fd97b5e520329cfa17d2b399497` | oui |
| `sorties-v2/essais-v2.stderr` | `38577ddd01d6d4ebf8120c1632e24ac0b790addd2797e7e331dd9903e1788d33` | oui |
| `sorties-v2/essais-v2.stdout` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | oui |
| `sorties-v2/generations-w12-g3-n400-v2.json` | `41616a47db42d62ee984803e43a609d5e5e3701f8ec22b49048f049aba9240a2` | oui |
| `sorties-v2/generations-w12-g3-n400-v2.stdout` | `ccf487b95d9513ca2328388e44a3bf0d2134b4442d64a68bfd588a797d06c3f9` | oui |
| `sorties-v2/journal-sorties-v2-reprise.txt` | `51a27366ab77f5370f0643a786adbe1adfafb1e5d5327ad68af31db6b1e653a3` | oui |
| `sorties-v2/journal-sorties-v2.txt` | `e60958f904fd8b9b9eb572f797e52e0216f620aea7ea04606f572670ce25ab72` | oui |
| `sorties-v2/representant-w12-v2.json` | `e6e157ea0056a6fbafae13b0f2d011eb59a1dfa162ade1dd679eb7b7c34019b2` | oui |
| `sorties-v2/representant-w12-v2.stdout` | `bbd1395c193d3d250aaa32e1e2c10351de04442ef357010db6caae6abf3fc0f9` | oui |
| `sorties-v2/reproductibilite-generations-w2-hash1-v2.json` | `e532e9d30aed46863dac0347f48bc2d04c1c9c00c37078c2ea2da907a4a79e2f` | oui |
| `sorties-v2/reproductibilite-generations-w2-hash1-v2.stdout` | `39156585a9bda42e241c6d010a3cd06e3395ca00add69440f3a42861c2e826f0` | oui |
| `sorties-v3/doublons-v3-monde-0.json` | `ffa2b63d0144c7abcc45aaf132229f99469470dc5366f4d0d7b46136301d706f` | oui |
| `sorties-v3/doublons-v3-monde-1.json` | `ee7d6350c9eab38921ae7de032c0833daea2f763e9c3a027b9432c9a139b81c8` | oui |
| `sorties-v3/doublons-v3-monde-10.json` | `d5a4f382b1b05d4e0c88c1ef8b8011bb042bae90fd3a2415e6b4f8b2aa65d77e` | oui |
| `sorties-v3/doublons-v3-monde-11.json` | `7c5e9e16b8c84a6f1ba89b5474e805df77c6c3d601419b95321bef39cca623ea` | oui |
| `sorties-v3/doublons-v3-monde-2.json` | `43d44ba8e1fb8e4df8bff281f626b5a5426f3f044e8d405d52467fd361f29ab0` | oui |
| `sorties-v3/doublons-v3-monde-3.json` | `87d7a3dd4882d11111a73370ba95df200312efe2f706e3830dc5cca7842ee6d4` | oui |
| `sorties-v3/doublons-v3-monde-4.json` | `0ad972f2a48ffc24a3c675139ef13be7ba1cfae2f11931f6217f738f0e973eb6` | oui |
| `sorties-v3/doublons-v3-monde-5.json` | `229a57cf124c5f980461b7702178e72a88779f99ee90cb7ee5dfde8891f56d14` | oui |
| `sorties-v3/doublons-v3-monde-6.json` | `05ddbd3589889de62944cac918bc3c0e7126b586a8767bbef821f91c1ca07190` | oui |
| `sorties-v3/doublons-v3-monde-7.json` | `553be675c82721c6bfc4ebad6735c0ca85e7fa046bb3e4d029d2919e50f596d8` | oui |
| `sorties-v3/doublons-v3-monde-8.json` | `806099b26b7159bdc782547ad7785ebb56a88178a4b8dff57317acef908a09bd` | oui |
| `sorties-v3/doublons-v3-monde-9.json` | `14d1b05bbfb99c4a8efa81cfb85b56b2b87536fe7b2f6fe51be830d87c2a7612` | oui |
| `sorties-v3/doublons-v3-resume.json` | `b9032dd8e58653a67c66024e90564414350176282e19ee86ecbc347756bcae36` | oui |
| `sorties-v3/generations-a2-v3-resume.json` | `27f3b64f358783a7a33466ed2fa73dbc66e43296e971d3683d26b9cb75c59e28` | oui |
| `sorties-v3/generations-a2-v3b-monde-0.json` | `1e5f518d406edfe34b5443f2f0d0f67a889973dea30f22d08e752cf5e361d410` | oui |
| `sorties-v3/generations-a2-v3b-monde-1.json` | `a1adf104dca210b4ee2a978cf12490c2001798b85d5ed46ef09f1dc7eed4ad34` | oui |
| `sorties-v3/generations-a2-v3b-monde-10.json` | `63aac7991aa82089f2c0fc1eb1ce626f6df1b6e4a5887ecc08e2f671e100aec5` | oui |
| `sorties-v3/generations-a2-v3b-monde-11.json` | `2ba24d3a20b9c16f0b65f260620d5cc26689299f055243ca1c879b114bbb34bb` | oui |
| `sorties-v3/generations-a2-v3b-monde-2.json` | `3c93e50ecb8d1415c0d65d4f96cfca6ebb696ac0e5c2024e963579d0e7e4f7df` | oui |
| `sorties-v3/generations-a2-v3b-monde-3.json` | `558cbc462452f1058aa6faebf78a7e2a1d3c62cb3644e317c8935b410fce5cf5` | oui |
| `sorties-v3/generations-a2-v3b-monde-4.json` | `617a5b1bc7aba8bff097809e43fd96ec26e46354cf0c3e2d208648e4289c7e38` | oui |
| `sorties-v3/generations-a2-v3b-monde-5.json` | `773a86071ab9bf8c4e539dcae38011681cfd07d4eb8438d11b91f1f0b2f96025` | oui |
| `sorties-v3/generations-a2-v3b-monde-6.json` | `16126c36d722e86baf844518c1bb9f2b5520e02830251c2f1afd3299ecccb87e` | oui |
| `sorties-v3/generations-a2-v3b-monde-7.json` | `4c503dd637223c378491959a9de55feb69b27a65e8c12cca92d02dac058bc12a` | oui |
| `sorties-v3/generations-a2-v3b-monde-8.json` | `1fdcd319d7a4061f2959d54fa1808ccfffbfc616d659f82e6ce50e345ac0dc0f` | oui |
| `sorties-v3/generations-a2-v3b-monde-9.json` | `d922de32d2d043d7f09e30b44de7e8d505d42efd616ed271d34fe055f131591f` | oui |
| `sorties-v3/generations-a2-v3b-resume.json` | `c4e43f6504ac3cfebaadec65028cda661e8607c0f330d1bf8c3cea49062cfd6a` | oui |
| `sorties-v3/journal-sorties-v3.txt` | `52232d6441ad7442093919084399c1e263fc320318156f864fbfe37c11632f15` | oui |
| `sorties-v3/representant-v3-monde-0.json` | `e5d0d0100729641a2215890a3d99784b8667b0b3bead75581da82e6c86f729de` | oui |
| `sorties-v3/representant-v3-monde-1.json` | `cb35151dc4e849845124668ed121ef51cddc0bcab2fc7d6667b19fadf37fe0f9` | oui |
| `sorties-v3/representant-v3-monde-10.json` | `ac81f71246f3a2a6153932f4cccb73e8488782f656140d9a8614b5b02b0eeb2e` | oui |
| `sorties-v3/representant-v3-monde-11.json` | `58377b96363b3f220438bdeafa4521e9d4d7721cdcb9909ca7ab1c7c6e0a58a4` | oui |
| `sorties-v3/representant-v3-monde-2.json` | `1f93195ebb2b658af6cf02c41c50aac7b78a3e9b346b70e47bc9bac3e18b87b0` | oui |
| `sorties-v3/representant-v3-monde-3.json` | `1c687f044a56d8db11922cf1a691085cf475d67f603a943c91c5b5a5b11991ff` | oui |
| `sorties-v3/representant-v3-monde-4.json` | `f8ec9fc6e15c1fd19726c7f07a943635942be20304510d0a883f2174239bd923` | oui |
| `sorties-v3/representant-v3-monde-5.json` | `220502f043a203bcb70f13efa1c0120c895be30cfccfd80c4af7e8dac0e099fa` | oui |
| `sorties-v3/representant-v3-monde-6.json` | `5ece39241e74c05a6629f822daf007956641b4113f1325d449f0b94fef56f322` | oui |
| `sorties-v3/representant-v3-monde-7.json` | `49da0857a019a90c01d0937ab868d3c10c2dfea98c95ea19cf50044f6146cb52` | oui |
| `sorties-v3/representant-v3-monde-8.json` | `3f8552f1f0c373e644896e40d043283ea3d68ab0ae1b89219d30819834f1ed03` | oui |
| `sorties-v3/representant-v3-monde-9.json` | `2d3b5a1a0030615d7bdaae94ae35ca2ccfccdd6339af00fcc800f72fd723acb4` | oui |
| `sorties-v3/representant-v3-resume.json` | `7dfa085d02f0b66792cfc92819aa771e28890f2ab630c431eec242d34982644f` | oui |

## 1. Monde riche

### 1.1 Pourquoi le monde S-V1 ne suffit plus

S-V1 a 3 issues, 2 traits et une loi softmax ; K1 en tient le trait z0, et **un seul** constat restait à trouver (le trait z1,
≈ 0,47 nat). La course v67 l'a montré : 11 cartes retenues en génération 1, « variantes proches d'un même constat », puis
12 refus sur 12 en génération 2 (verdict v67, réserve R-5). Plusieurs générations n'ont de sens que s'il reste, après chaque
génération, des effets à trouver, de tailles décroissantes jusqu'au voisinage du seuil.

### 1.2 Forme des lois : famille MR-1

- **Instances** (publiques) : 8 traits z0 à z7 indépendants, loi normale centrée réduite, arrondis à six décimales (comme
  `selection_pari.tirer_instances`) ; sous-population g ∈ {0, 1, 2} uniforme. **Issues** : 3.
- **Loi du monde** : scores s_k(x) = b_k + Σ (effets actifs en x), puis softmax. Six sortes d'effets, chacune un vecteur de
  trois nombres :

| sorte | ajoute aux scores | interaction ? | se compile en |
|---|---|---|---|
| `principal` | pente × z_t | non | colonne t des poids de chaque feuille |
| `seuil` | décalage si z_t > c | non (non linéaire) | `si_sinon` sur (t, c), biais de la branche « si » |
| `interaction_seuil` | pente × z_t si z_u > c | **oui** (trait × trait) | `si_sinon` sur (u, c), colonne t de la branche « si » |
| `interaction_sous_population` | pente × z_t dans la sous-population h | **oui** (trait × sous-population) | `par_sous_population`, colonne t de la branche h |
| `sous_population` | décalage dans la sous-population h | non | `par_sous_population`, biais de la branche h |
| `latent` | u × décalage, u ∈ {+1, −1} **non observé** | caché | `melange` de deux arbres (u = +1 et u = −1) |

- **Compilation** (`compiler_monde`, `outils-v1/monde_riche_outils_v1.py`) : `par_sous_population` (si un effet dépend de g) →
  `si_sinon` imbriqués sur les conditions de seuil (au plus 2) → feuilles `softmax` de largeur 8 ; `melange` 1/2-1/2 (ou
  `poids_melange`) au-dessus pour le latent. Au plus 3 × 4 × 2 = 24 feuilles. **Toutes ces formes sont dans la grammaire
  existante** (`selection_pari.TYPES_LOI`) : l'évaluateur `proba`, les tirages du noyau et l'évaluateur servi à
  l'expérimentateur n'ont pas à changer. Égalité vérifiée : l'évaluateur vectorisé de la conception rend les mêmes
  probabilités que `selection_pari.proba` de la copie v52b à 10⁻¹² près (essai `Lois.test_egal_a_selection_pari_v52b`).
- **Tailles** : la taille d'un effet i est son **information** I_i = E_x KL(W(·|x) ‖ W₋ᵢ(·|x)), ce que l'on perd en le retirant
  du monde, les autres gardés (`Oracle.information_effet`). Classes (exigences `sorties-v1/exigences-monde-riche-v1.json`) :
  **forte** [0,10 ; 0,25] (2 effets), **moyenne** [0,04 ; 0,08] (2 ou 3), **faible** [0,02 ; 0,035] (2 à 4) ; au moins 2
  interactions ; au moins 2 distracteurs ; gain du monde [0,30 ; 0,90] nat. La classe faible est posée **au voisinage de
  g₀ = 0,02** : un effet faible ajouté à une loi qui tient déjà le reste rapporte ≈ I_i, juste au-dessus du seuil ; ajouté à K1
  seule, il rapporte moins (de 0,001 à 0,025 nat, médiane 0,016, sur les 36 « K1 + faible » de 12 mondes synthétiques :
  `sorties-v1/detection-w12-r40-v1.json`, champ `oracle` ; donc le plus souvent sous g₀). C'est voulu : les faibles ne
  deviennent trouvables qu'après les fortes, ce qui donne un sens à plusieurs générations.
- **Gabarit tiré par monde, privé** (synthèse, rang 1) — **v2** (`tirer_gabarit_v2`, `outils-v2/generateur_mondes_v2.py`) :
  forte 2 (tirées parmi principale, interaction de seuil, interaction de sous-population ; au moins une principale), moyenne
  2 ou 3 et faible 2 à 4 (tirées uniformément parmi les cinq sortes observables) ; **trait latent compté à part** (classe
  « latente », 0 ou 1, probabilité 1/3, taille visée tirée dans [0,04 ; 0,08], poids tiré dans [0,3 ; 0,7]) (E-5) ; contraintes :
  au moins 2 interactions, au plus 2 effets à seuil, au moins 2 traits leurres ; puis traits (permutation), directions
  centrées, seuils continus et signés, trait de condition tiré parmi les traits des autres effets, sous-populations, tailles
  visées ; étalonnage par bissection. Les fréquences réalisées des sortes sont rapportées (§2.4). La v1 (gabarit à sortes liées
  aux classes, latent compté parmi les moyennes) est remplacée.
- **« Proche du seuil » rendu opératoire** (C8 v2, E-11) : pour chaque composante, la part de **200** graines où le monde W est
  promu contre le nul v8 de {W₋ᵢ} (n et m du banc ; ici n = 400, m = 44). Étiquettes : **certifiée détectable quand le reste du
  monde est connu** si la borne basse de Wilson à 95 % ≥ 0,8 ; **indétectable** si la borne haute < 0,1 ; **proche du seuil**
  sinon. Règles **codées** : toute forte certifiée ; toute moyenne de puissance ≥ 0,5 (cette règle **remplace** la règle « indétectable : refus si non faible » de la v1, T-4) ;
  moyenne des faibles dans [0,1 ; 0,9] ;
  latente rapportée. La certification est faite contre {W₋ᵢ}, l'archive la plus favorable : elle borne la détectabilité par le
  haut ; contre l'archive réelle, elle se mesure après la course (sentinelles, §1.8) et, avant la course, selon la taille de
  l'archive (§1.6, E-3).

### 1.3 Changements de code nécessaires (noms neufs, R12 ; à vérifier dans le code gelé, non lu ici)

| # | pièce | changement | pourquoi |
|---|---|---|---|
| K-1 | juge de la boucle (`a_blanc_v59.juger_carte` ; constante `DIM` de `boucle_reelle_v65`, reprise par `boucle_reelle_v66` l. « ALPHA, K, DIM = B65.ALPHA, B65.K, B65.DIM » du patch ; valeur non lue, 2 d'après le monde S-V1) | `juger_carte_v68(loi, monde, archive, racine, tâche, dimension, sous_populations, tirages)` : dimension et sous-populations lues dans `espace_instances` du fichier du monde (la forme des fiches de `temoins-pari-demo-v1.json` les porte déjà) | D = 8, 3 sous-populations |
| K-2 | même juge | tirages frais par carte **fixés par la règle de Q-5** au banc (indication du juge simplifié : 400 ; la v67 : 200), huit instants de lecture réguliers ; m = 44 sur le décompte du dessin | puissance aux faibles (§1.6, E-3) |
| K-3 | tranche et épisodes servis (`tour_ferme_v64.episodes_de_developpement`, étage v5) | instances à 8 traits et 3 sous-populations ; tranche de 400 épisodes inchangée | idem |
| K-4 | gardien mécanique (jeu factice fixe) | jeu factice à la dimension du monde | une loi à 8 traits doit s'évaluer |
| K-5 | gabarit du proposeur (bornes ±4) | dimension 8, 3 sous-populations, `par_sous_population`, `si_sinon` permis ; **aucune description des sortes d'effets du monde** (seulement la grammaire) | ne pas souffler la structure |
| K-6 | oracle (`oracle_tour_ferme_v60`) | `oracle_monde_riche_v68` : gains v60 inchangés **plus** gain au-delà de l'enveloppe, information des effets, attribution des effets à une loi (§4) ; lu une seule fois, après la course | vérité des « découvertes » quand l'archive grandit |
| K-7 | jeu planté (`boucle_reelle_v65`, garde 19) | règle `jeu_plante_mr1` (§1.5) dérivée du monde par programme ; bloc gelé au texte = empreinte du jeu (le monde reste privé) | le jeu n'est plus écrit à la main |
| K-8 | juge v66 (`juger_v66`, e-BH à m fixé) | `juger_v68` : étape A du regroupement entre gardien et juge ; e-BH sur les groupes ; représentant par groupe (§3) | doublons |
| K-9 | lecture gelée | mesures neuves (groupes, D1, D2, attribution) ; jetons d'Argon lus aux champs `entree` et `sortie` (réserve R-6) ; touches de la recherche de la loi plantée **toutes rapportées** (réserve R-1) | réserves de la v67 |
| K-10 | commandes externes et étage | réponse brute de chaque appel de proposeur et témoin d'isolement de chaque exécution versés, absence = arrêt (§5.3) | réserve R-2 |
| K-11 | lanceur | plusieurs mondes : une course par monde, graines par monde, relevés séparés ; **aucune information d'un monde servie dans un autre** | §1.6 |

Ce que la v67 garde : la loi `proba`, le nul v8 et sa classe couverte, l'étage des tests de mort v5 et son bac `bwrap`, le
contre-calcul, la sélection v57, la lecture de la sélection par la génération suivante (gardes 17, 18, 21, 23).

### 1.4 Archive de départ

**K1 du monde** : la meilleure loi softmax du **seul trait de l'effet principal le plus fort**, ajustée par le programme au
maximum de vraisemblance attendue sous le monde (étiquettes douces, Newton ; `k1_du_monde`), arrondie à six décimales, scellée
comme bilan de génération 0 (comme la pièce M1 de la v65). Exigences (C4) : gain de K1 dans [0,05 ; 0,30] et au plus 0,6 fois
celui du monde. Raison (celle du texte v2, §3.2) : sans loi connue, les fausses « couvertes » seraient des lois fixes refusées
trivialement ; avec K1, elles portent de l'information et ne sont refusées que par l'archive.

### 1.5 Lois plantées (jeu planté dérivé du monde par programme, règle gelée avant le tirage)

- **Vraies** (`jeu_plante_mr1`) : **V-monde** (le monde lui-même) ; pour chaque autre effet i, **V-K1+i** = le monde réduit aux
  effets de K1 et de i, **calibré** (tempéré et incliné au maximum de vraisemblance attendue : une loi partielle juste mais trop
  confiante devient calibrée) ; **V-diluée-0,03** et **V-diluée-0,05** = mélanges λ·W + (1 − λ)·K1, λ choisi pour un gain
  au-delà de {K1} de 0,03 et 0,05 nat (vraies « faibles » au sens du gain). Une V-K1+i dont le gain au-delà de l'archive
  (v60 **et** enveloppe) est sous g₀ reste une **mesure**, jamais une vraie du critère (cas des V-K1+faible en génération 1).
  **Les vraies sont replantées à chaque génération** (jusqu'à 13 avec T-ELIM) : leur vérité est relue par l'oracle contre
  l'archive de la génération (E-9 (b) ; compté au devis).
- **Fausses couvertes** (classe du nul v8, comme F1 à F4 de la v67) : F1 copie de K1, F2 0,8·K1 + 0,2·uniforme, F3 0,8·K1 +
  0,2·loi fixe, F4 K1 tempérée et inclinée ; en génération g ≥ 2, en plus : **copies des quatre premières représentantes
  retenues** (P5 de la v67) et **F5 = mélange 1/2-1/2 de deux lois de l'archive** (« tout mélange de lois connues », docstring
  du nul v8 citée par le texte v2, §3.4). Vérification C5 : gain au-delà de l'enveloppe ≤ 10⁻³.
- **Sonde hors classe** (mesure, jamais un critère) : H1 = `si_sinon(z_t > 0, K1, A2)`, recombinaison par morceaux de deux
  lois d'archive (classe non couverte du nul v8 ; brèche d'A1-v3 sur W2). Dans un monde riche à structure par morceaux, une
  telle loi peut porter de l'information vraie : l'oracle la classe par son gain au-delà de l'enveloppe (§1.7).
- **Instruments** : T-ELIM (le monde à la puissance 1,25, seuil de test 2,0) et T-MAL (sans statistique), comme la v67.
- Toutes servies à l'aveugle (identifiant opaque), hors famille au seuil log(m/α), **jamais regroupées avec les cartes**,
  jamais retenues ni servies (garde 7).

### 1.6 Puissance par simulation hors ligne

**Juge simplifié** (`juger`, `outils-v1/monde_riche_outils_v1.py`) : pari plein ; dénominateur = maximum, aux instants de
lecture, de la marginale ajustée, de l'uniforme, des moyennes glissantes (fenêtres 5, 10, 20, 50) et, par loi de l'archive,
de la loi, de son mélange à l'uniforme (grille de 21 poids), de sa version tempérée et inclinée ajustée (Newton), et du
mélange linéaire ajusté de toutes les lois de l'archive et des lois certaines (espérance-maximisation, écart de Frank-Wolfe
ajouté) ; seuil hors famille log(m/α) ; e-BH ; test de mort = statistique gelée sur 400 épisodes, seuil 0,02. **L'urne de la
bibliothèque v1 est écartée** (`outils-v1/etalonnage_urne_v1.py`, sortie `sorties-v1/etalonnage-urne-r300-v1.json`,
`c87f964d…`, 300 répétitions) : avec elle, F1, F2 et F4 jugées sans archive sont promues 112, 64 et 93 fois sur 300 (0,21 à
0,37), loin des 725 à 810 sur 1 000 publiés ; sans elle, 244, 228 et 215 sur 300 (0,72 à 0,81) ; V3 et V4 bougent peu (182 et
153 sans, 178 et 149 avec). C'est une inférence sur le code gelé, à vérifier.

**Étalonnage** (`sorties-v1/etalonnage-r1000-v1.json`, `3ee96059…`, 21:20:10 → 21:23:02) sur le dessin exact de la v67 (S-V1, archive {K1}, m = 22,
1 000 répétitions), contre la sortie publiée (`puissance-boucle-reelle-v1-r1000.json`, `a23959fa…`, recopiée au texte v2 §4.2) :

| loi | promue puis survivante, juge simplifié (sur 1 000 ; Wilson à 95 %) | publié (v67, sur 1 000) | plus grand log W maximal |
|---|---|---|---|
| V1 | 1 000 [0,996 ; 1] | 1 000 | 116,2 |
| V2 | 1 000 [0,996 ; 1] | 1 000 | 103,3 |
| V3 (L* tempérée 0,08) | 595 [0,564 ; 0,625] | 617 | 20,6 |
| V4 (0,15 L* + 0,85 uniforme) | 489 [0,458 ; 0,520] | 501 | 19,0 |
| F1 à F4 avec {K1} (promues) | 0, 0, 0, 0 (4 000 jugements) | 0 sur 4 000 | −0,007 au plus |
| F1 à F4 sans archive (artefact, promues) | 814, 760, 779, 722 | 725 à 810 | 24,0 au plus |
| au moins une fausse promue sans archive | 1 000 | 994 | — |
| T-ELIM promue puis éliminée | 1 000 | 1 000 | 124,2 |

Écarts au publié : ≤ 2,2 points sur les vraies faibles, intervalles qui couvrent ou frôlent la valeur publiée ; le juge simplifié
est un peu plus sévère sur V3 et V4 et un peu moins sur F1 sans archive. Gain de S-V1 sur 20 000 instances : 0,521 nat
(publié 0,520) ; K1 0,053 (publié 0,052).

**Ce que l'étalonnage ne cale pas** (E-3) : un seul point (monde S-V1, 2 traits, archive d'une loi, 200 tirages). Le monde riche
extrapole sur trois axes non calés : 8 traits, 400 tirages, archive de 9 à 26 lois. Les chiffres qui suivent **indiquent** ;
ils ne gèlent rien (n se fixe par la règle de Q-5, au banc, avec le code v68).

**Détection v2, sur la famille tirée** (`sorties-v2/detection-w12-r40-v2.json`, `6a3d14446e4059bf7ade74c980f30d214ec847690e5ea444544f48e849f313dc`, 23:34:28 → 23:41:26 ; 12 mondes tirés, 40 répétitions
par loi, m = 44) : part des vraies plantées promues puis survivantes selon leur gain au-delà de {K1}, n = 200 puis 400 ;
entre parenthèses, le nombre de **lois distinctes** dans la tranche (les 40 répétitions d'une même loi ne sont pas indépendantes :
les intervalles de Wilson par tranche seraient trop étroits ; E-3) :

| gain au-delà de {K1} (nat) | lois distinctes | n = 200 | n = 400 |
|---|---|---|---|
| [0 ; 0,01[ | 5 | 2 / 200 (0,01) | 16 / 200 (0,08) |
| [0,01 ; 0,02[ | 17 | 30 / 680 (0,04) | 242 / 680 (0,36) |
| [0,02 ; 0,03[ | 9 | 82 / 360 (0,23) | 258 / 360 (0,72) |
| [0,03 ; 0,04[ | 22 | 165 / 880 (0,19) | 837 / 880 (0,95) |
| [0,04 ; 0,06[ | 23 | 724 / 920 (0,79) | 917 / 920 (1,00) |
| ≥ 0,06 | 25 | 994 / 1 000 | 1 000 / 1 000 |

Par classe (« K1 + un effet » calibrées) : forte 0,99 puis 1,00 ; moyenne 0,46 puis 0,80 ; faible 0,06 puis 0,35. Fausses
couvertes : **0 sur 5 760** jugements (n = 200 et 400) ; sans archive (artefact) 0,98 et 1,00. Sonde hors classe H1 :
4 sur 480 puis **13 sur 480 (0,027)** — plus qu'en v1 (3 sur 480) : dans la famille tirée, le découpage par morceaux de deux
lois d'archive porte parfois de l'information (classe non couverte, Q-4). Faibles par monde à n = 400 : de 0,04 à 0,56,
écart-type 0,18 entre mondes (v1, sous-famille : 0,10) : la dispersion entre mondes est plus grande que dans la v1. Les
conclusions de la v1 sur n tiennent dans leur sens : n = 400 met le point de 50 % vers 0,02 nat (0,72 dans [0,02 ; 0,03[), au
prix de 0,36 de promotions dans [0,01 ; 0,02[.

**Puissance selon la taille de l'archive** (`sorties-v2/archive-w8-r30-v2.json`, `a631ad4744b0722d541af33ffd63a34d85d6beb46f212ba55441f90b76d71c40`, 23:31:03 → 23:34:28 ; 8 mondes tirés ; le monde W jugé
contre le nul de {W₋ᵢ} plus k lois partielles bruitées qui n'ont pas la composante i ; n = 400, m = 44, 30 répétitions) :
composantes **faibles** : 294, 295 et 295 promotions sur 540 pour une archive de 1, 8 et 16 lois
(0,54 ; Wilson [0,50 ; 0,59] dans les trois cas) ; **moyennes** : 589, 554 et 538 sur 630 (0,93 ; 0,88 ; 0,85). Dans ce modèle,
**ajouter des lois partielles** à une archive qui contient déjà W₋ᵢ coûte peu au juge sur les faibles (le mélange ajusté sur
16 lois coûte peu) et 8 points sur les moyennes. **Ce test ne dit pas** que le juge reste entendant contre une archive réaliste
de génération 3, faite de lois partielles **sans** W₋ᵢ (V-5) : demandé au banc (§1.8). À refaire au banc avec le code v68 (E-3), qui seul dira si une génération 3 vide est « monde épuisé ».

**Détection v1, conservée pour mémoire (sous-famille : gabarit fixe, sans latent ; E-4)** (`sorties-v1/detection-w12-r40-v1.json`, `8da67edd2b64f93970a9b5f3f5f67c58c08e05797994f3615a3062fe6aab89b7`, 21:34:17 → 21:48:19 ; 12 mondes synthétiques, 40
répétitions par loi et par n, m = 40) — part des vraies plantées promues puis survivantes selon leur gain au-delà de l'archive
{K1} (sens v60), pour n = 200, 400, 800 tirages par carte :

| gain au-delà de {K1} (nat) | n = 200 | n = 400 | n = 800 |
|---|---|---|---|
| [0 ; 0,01[ | 0 / 160 (0,00) | 8 / 160 (0,05) | 34 / 160 (0,21) |
| [0,01 ; 0,02[ | 50 / 1 120 (0,04) | 375 / 1 120 (0,33) | 906 / 1 120 (0,81) |
| [0,02 ; 0,03[ | 41 / 240 (0,17) | 158 / 240 (0,66) | 235 / 240 (0,98) |
| [0,03 ; 0,04[ | 179 / 880 (0,20) | 811 / 880 (0,92) | 880 / 880 (1,00) |
| [0,04 ; 0,06[ | 708 / 920 (0,77) | 907 / 920 (0,99) | 920 / 920 (1,00) |
| [0,06 ; 0,08[ | 71 / 80 (0,89) | 80 / 80 (1,00) | 80 / 80 (1,00) |
| [0,08 ; 0,12[ | 272 / 280 (0,97) | 280 / 280 (1,00) | 280 / 280 (1,00) |
| [0,12 ; 0,20[ | 159 / 160 (0,99) | 160 / 160 (1,00) | 160 / 160 (1,00) |
| ≥ 0,20 | 480 / 480 (1,00) | 480 / 480 (1,00) | 480 / 480 (1,00) |

Par classe de l'effet ajouté à K1 (vraies « K1 + un effet », calibrées ; promues puis survivantes, Wilson à 95 %) :

| classe | n = 200 | n = 400 | n = 800 |
|---|---|---|---|
| forte (gain au-delà de {K1} : 0,079 à 0,166) | 466 / 480 [0,952 ; 0,983] | 480 / 480 [0,992 ; 1] | 480 / 480 [0,992 ; 1] |
| moyenne (0,024 à 0,061) | 524 / 960 [0,514 ; 0,577] | 866 / 960 [0,882 ; 0,919] | 958 / 960 [0,992 ; 0,999] |
| faible (0,001 à 0,025, médiane 0,016) | 72 / 1 440 [0,040 ; 0,062] | 485 / 1 440 [0,313 ; 0,362] | 1 097 / 1 440 [0,739 ; 0,783] |

Fausses couvertes (F1 à F4 avec {K1} ; F5 mélange de deux lois d'archive et F6 copie, avec une archive de deux lois) :
**0 promotion sur 5 760 jugements** (2 880 à n = 200, 2 880 à n = 400 ; Wilson [0 ; 0,002] par genre et par n) ; jugées sans
archive (artefact), 1 908 sur 1 920 à n = 200 et 1 920 sur 1 920 à n = 400 : la protection vient de l'archive, comme en v67.
Sonde hors classe H1 (recombinaison par morceaux de deux lois d'archive) : 1 sur 480 à n = 200, 3 sur 480 à n = 400 (dans ces
mondes, le découpage sur le trait de K1 n'apporte presque rien ; ce n'est pas une borne sur la classe non couverte).
Dispersion entre mondes du taux des « K1 + faible » à n = 400 : de 0,21 à 0,54, écart-type 0,10 entre les 12 mondes.

**Choix de n (v1, remplacé par la règle de Q-5)** : à n = 200 (la v67), le point de 50 % du juge tombe vers 0,045 nat au-delà de l'archive : un effet faible
(0,02-0,035) n'est presque jamais promu (0,17 dans [0,02 ; 0,03[), et la classe « proche du seuil » serait invisible. À
**n = 400**, ce point tombe vers 0,02-0,025 nat, c'est-à-dire **sur g₀** : la décision du juge et la vérité de l'oracle
coïncident à peu près (0,66 dans [0,02 ; 0,03[, 0,92 dans [0,03 ; 0,04[ ; mais 0,33 dans [0,01 ; 0,02[, lois réelles sous g₀
que l'oracle comptera comme fausses découvertes). À n = 800, le juge promeut aussi la plupart des lois sous g₀ (0,81 dans
[0,01 ; 0,02[) : il devient plus fin que l'oracle. ~~Recommandation : n = 400~~ → **v2 : règle de Q-5**. Les tirages frais sont simulés : n ne
coûte que du calcul. Les promotions sous g₀ deviennent une mesure rapportée (« découvertes réelles sous le seuil »).

**Plusieurs générations v2** (`sorties-v2/generations-w12-g3-n400-v2.json`, `41616a47db42d62ee984803e43a609d5e5e3701f8ec22b49048f049aba9240a2`, 23:42:03 → 23:50:18 ; famille tirée, règle du
représentant v2, regroupement stratifié, m = 44, n = 400, parcours triés ; graine de hachage **non fixée** (`python3 -I`,
V-2) ; un second lancement, à une autre graine aléatoire, sur 2 mondes : **les deux courses des mondes 0 et 1, dans les deux
conditions, égales champ pour champ** (`reproductibilite-generations-w2-hash1-v2.json`, `e532e9d3…`)) :

| condition | génération | promues | retenues | archive | part des composantes captées (oracle) [écart-type entre mondes] | faibles captées | fausses découvertes / retenues |
|---|---|---|---|---|---|---|---|
| sans regroupement | 1 | 12,75 | 12,58 | 13,6 | 0,889 [0,093] | 1,75 | 18 / 151 |
| | 2 | 11,17 | 11,17 | 24,8 | 0,937 [0,066] | 2,08 | 18 / 134 |
| | 3 | 0,08 | 0,08 | 24,8 | 0,937 [0,066] | 2,08 | 1 / 1 |
| regroupement v2 | 1 | 9,17 | 9,00 | 10,0 | 0,889 [0,093] | 1,75 | 16 / 108 |
| | 2 | 6,25 | 6,25 | 16,3 | 0,937 [0,066] | 2,08 | 14 / 75 |
| | 3 | 0 | 0 | 16,3 | 0,937 [0,066] | 2,08 | 0 / 0 |

Lecture (estimée : proposeurs synthétiques, juge simplifié) : (i) le regroupement v2 garde **exactement la même part de
composantes captées**, monde par monde (de 0,86 à 1,00 dans les deux conditions, identiques), avec une **archive plus petite
d'un tiers** (16,3 lois contre 24,8) et un tiers de tests en moins ; (ii) les **fausses découvertes au sens de l'oracle** font 12
à 19 % des retenues (16 sur 108, 14 sur 75 avec regroupement ; 18 sur 151, 18 sur 134 sans), bien au-dessus de α : la preuve du
§3.3 ne les borne pas (E-8 (c), Q-9) ; (iii) la génération 3 ne promeut presque rien : avec ces proposeurs, le monde est épuisé
en génération 2 — **ce que la simulation ne peut pas séparer d'un juge devenu sourd** sans la mesure selon la taille de
l'archive ; or le test « taille de l'archive » ci-dessus garde W₋ᵢ dans l'archive et ne mesure donc pas cette surdité (V-5) :
à mesurer au banc, sur des archives sans W₋ᵢ ; la part manquante (≈ 6 %) est surtout
la composante latente, que l'attribution ne capte pas (§4.1). La v1 disait « 3 générations suffisent » sur une sortie non
rejouable ; la v2 le dit sur une sortie rejouable, pour ces proposeurs synthétiques seulement.

**v3, condition « regroupement » refaite avec la tranche de choix appariée** (V-1 ; la condition « sans regroupement » ne dépend
pas du représentant et ne change pas) : `sorties-v3/generations-a2-v3b-resume.json` (`c4e43f6504ac3cfe…`), 12 parties scellées
`generations-a2-v3b-monde-*.json`, 01:05 → 01:30 : génération 1 inchangée (9,0 retenues, archive 10,0, part captée 0,889,
15 fausses découvertes sur 108 contre 16 en v2) ; génération 2 : 6,08 retenues (6,25 en v2), archive 16,1 (16,3), part captée
**0,937 (identique)**, 13 fausses découvertes sur 73 (14 sur 75) ; génération 3 vide. Les conclusions de la v2 tiennent avec la
tranche appariée.

**v1, conservée pour mémoire : non rejouable au-delà de la génération 1 (E-2) et sur la sous-famille (E-4)** —
**Nombre de mondes et de graines** (`sorties-v1/generations-w12-g3-n400-v1.json`, `86c7ac0edeb12f12826476de6ab4a922ebee8dc0ed9be076f19d033613516c6a`, 21:48:19 → 22:12:43) : 12 mondes MR-1, 3 générations, n = 400, m = 40, ε = 0,01 ; **proposeurs
synthétiques** (4 × 6 cartes ; une carte garde chaque effet déjà connu avec la probabilité 0,9 et ajoute un effet inconnu avec
0,5, 0,25 ou 0,1 selon sa classe, coefficients bruités σ = 0,15 : modèle **estimé**, pas une mesure) ; mêmes cartes et mêmes
tirages pour les trois conditions. Moyennes sur les 12 mondes :

| condition | génération | promues | groupes | retenues | archive | composantes captées (oracle) sur 7 [écart-type entre mondes] | faibles captées | fausses découvertes / retenues (au-delà de l'enveloppe < g₀) |
|---|---|---|---|---|---|---|---|---|
| sans regroupement (règle v67) | 1 | 13,0 | — | 13,0 | 14,0 | 6,17 [1,03] | 2,25 | 11 / 156 |
| | 2 | 11,9 | — | 11,9 | 25,9 | 6,75 [0,62] | 2,75 | 15 / 143 |
| | 3 | 0,17 | — | 0,17 | 26,1 | 6,92 [0,29] | 2,92 | 1 / 2 |
| étape A seule | 1 | 7,8 | 13,2 | 7,8 | 8,8 | 6,08 [1,00] | 2,17 | 11 / 94 |
| | 2 | 6,5 | 15,2 | 6,5 | 15,3 | 6,67 [0,89] | 2,67 | 12 / 78 |
| | 3 | 0,08 | 16,3 | 0,08 | 15,4 | 6,83 [0,39] | 2,83 | 0 / 1 |
| étapes A et B (domination) | 1 | 7,8 | 13,2 | 2,25 | 3,25 | 4,58 [0,79] | 1,00 | 0 / 27 |
| | 2 | 3,8 | 15,0 | 2,17 | 5,4 | 5,83 [0,94] | 1,83 | 7 / 26 |
| | 3 | 1,08 | 15,8 | 0,83 | 6,25 | 6,33 [0,78] | 2,33 | 4 / 10 |

Lecture (estimée) : (i) l'étape A garde **les mêmes composantes captées** (6,83 contre 6,92 sur 7 en génération 3) avec une
**archive plus petite de 40 %** (15,4 contre 26,1 lois) et presque deux fois moins de cartes promues à tester (7,8 contre 13,0 en
génération 1) ; (ii) l'étape B perd des composantes tôt (4,58 contre 6,08 en génération 1) et ne les rattrape pas en trois
générations ; (iii) **les fausses découvertes au sens de l'oracle** (lois retenues à moins de g₀ au-delà de l'enveloppe, le
plus souvent « K1 + un effet faible » portées par e-BH) font 8 à 15 % des retenues à n = 400 : à rapporter, et argument pour que
le préenregistrement exige la vérité par l'enveloppe (§1.7) ; (iv) avec ces proposeurs généreux, le monde est presque épuisé en
génération 2 et la génération 3 ne promeut presque rien : **3 générations suffisent pour un monde de 6 à 9 composantes**, 4
n'ajouteraient que du coût ; avec de vrais proposeurs, plus lents, la génération 3 a plus à trouver ; (v) **dispersion entre
mondes** des composantes captées : écart-type ≈ 1 composante en génération 1 (sur 7), et la puissance du juge sur les faibles
varie d'un monde à l'autre de 0,21 à 0,54 (détection, n = 400). Un seul monde ne dit donc rien de cette dispersion ; deux mondes
en donnent une première réplication ; trois, une estimation grossière.

**Plusieurs graines** : par monde, la sensibilité aux effets faibles se mesure sans agent et sans dépense sur des graines (C8 :
200 graines par composante avant la course ; rejeux des retenues et sentinelles sur 200 graines après, §1.8) ; **plusieurs mondes**
mesurent la dispersion due au monde et aux proposeurs, au prix d'une course par monde. Recommandation : **2 mondes × 3
générations** (Q-1).

### 1.7 Lois fausses, classe couverte et vérité des découvertes quand l'archive grandit

- **Classe couverte** : inchangée (nul v8). Les fausses plantées restent dans la classe couverte **de l'archive de leur
  génération** (garde 18) ; en simulation, 0 promotion sur 5 760 jugements, contre 1 908 sur 1 920 (n = 200) et 1 920 sur 1 920 (n = 400) quand on les juge sans
  archive (artefact).
- **Classe non couverte** : avec une archive de plusieurs lois et un monde à structure par morceaux, les recombinaisons par
  morceaux d'archive deviennent un chemin naturel des proposeurs. Le nul v9 ferme ce trou mais sa validation a rendu
  « puissance perdue » (audit `9086a420…`) : question Q-4 (§7).
- **Vérité** : l'oracle v60 dit « au-delà de l'archive » contre **la meilleure loi seule** ; avec une archive de plusieurs
  lois, une recombinaison couverte (mélange de deux lois d'archive) peut battre chaque loi seule sans rien apporter de neuf.
  L'oracle neuf (K-6) rapporte **aussi** le gain au-delà de l'**enveloppe** (meilleur membre du nul v8 de l'archive, ajusté
  sous le monde : `Oracle.gain_enveloppe`) ; une « vraie découverte » du préenregistrement multi-générations devrait exiger
  les deux (proposition ; décision du rédacteur du préenregistrement).

### 1.8 Répartition des mondes et banc de métrologie (préalable sans appel)

- **Développement** : les mondes synthétiques de cette conception (graines publiques, `outils-v1/`, `outils-v2/`) ; ils ont servi
  à proposer ε, ε_strat et le seuil d'attribution ; ils ne servent plus à rien de décisif. **Ces seuils ont été réglés en v1 sur
  une sous-famille** (gabarit fixe, sans latent ; E-4) ; la v2 les éprouve sur la famille tirée (§3.6, §4.1).
- **Calibration** : un second jeu de mondes **écrits par programme** sur une graine scellée avant le préenregistrement (au moins
  12), où le **banc de métrologie** (synthèse, convergence des cinq espèces) refait, avec le code v68 gelé : l'étalonnage du juge
  (§1.6), la détection par classe, les doublons (paires difficiles **disjointes** de celles du développement), l'attribution,
  et les mondes témoins : **monde à une seule composante** (la couverture doit valoir 1), **monde dont la vérité est un membre du
  nul de l'archive** (aucune promotion attendue), lois sans dépendance à une composante (fausse couverture), variantes éloignées
  de même gain (inflation), recombinaisons couvertes (comptées comme anciennes). **Surdité** (V-5) : puissance sur une composante
  faible contre des archives **sans W₋ᵢ**, faites des retenues simulées d'une génération 2 (et de 8 et 16 lois partielles), à
  comparer à la puissance contre {W₋ᵢ} ; c'est ce qui dira si une génération 3 vide est « monde épuisé » ou « juge sourd ». En plus (v2) : **n par la règle de Q-5** ;
  **puissance sur un effet faible selon la taille de l'archive** (1, 8, 16 lois et plus : distinguer « monde épuisé » de « juge
  devenu sourd », E-3) ; **trois formes de la valeur e de groupe** comparées (moyenne, valeur e du seul représentant, arrêt
  ajusté à la taille du groupe connue avant les tirages : S-1) ; **C7 éprouvé sur les vraies pièces gelées** (E-7) ; fusion
  des composantes non séparables (S-8). **Règle de changement** : si le banc conduit à changer un seuil (ε, ε_strat, attribution,
  n, certification), le changement est écrit, et un **nouveau secret de calibration** tire de nouveaux mondes pour le
  confirmer (E-4). Coût : calcul seulement.
- **Test** : les mondes tirés du secret de test (§2.2), scellés, jamais utilisés pour régler un seuil ; lus seulement par le
  vérificateur, le lanceur, puis l'oracle et le lecteur du verdict.
- **Après la course** (hors ligne, sans agent) : sentinelles « archive scellée de la génération g + une composante non captée »
  jugées contre cette archive sur 200 graines (détectabilité réelle génération par génération) ; rejeux des représentantes
  retenues sur 200 graines (fragilité de chaque découverte) ; réinjection des sœurs (§3.5).

## 2. Génération du monde par programme (cadre R-2461 ; remplace l'écriture par Kimi)

### 2.1 Qui écrit le générateur, et comment il reste aveugle aux lois tirées

- **Prototypes** : v1 `outils-v1/generateur_mondes_v1.py` (`46f3ac2d40efad200e382d95450d3683529f96a73e716913dbbaf24a3bceb1c5` ;
  la v1 de ce texte écrivait par erreur `46f3ac2d43ef…`, E-12 (d)) ; **v2** `outils-v2/generateur_mondes_v2.py` (`816ad7182c5980f0c25057404d53e62d1ba29643275749fd2c4238f3d2cf7fc2`).
  Écrits par moi (Claude Opus 5.5). **Celui qui fera foi** : écrit dans l'arbre de l'organisme sous un nom neuf, essayé (R5),
  contre-lu par un autre modèle (N-052), gelé par son empreinte au bloc du code du préenregistrement.
- **Aveugle** : le code ne contient aucune loi ; tout est tiré de la graine. La garantie est **de procédure, pas
  cryptographique** (E-12 (a)) : une session de la famille Claude lance le générateur et tient le secret machine ; ce qui
  empêche qu'elle connaisse les lois, ce sont des règles : (i) seuls des programmes lisent le fichier du monde avant le
  verdict ; (ii) le processus qui génère n'imprime que des empreintes et des contrôles, aucun coefficient (essais) ; (iii) le
  monde ne s'écrit que dans un dossier de la **liste blanche** des dossiers privés (`ecrire_prive`, S-7). Le choix (c) de Q-3
  empêche qu'un seul **fixe** les mondes, pas qu'une session les **connaisse** ; ce dernier point repose sur (i) à (iii).
- **Régularités du générateur** (E-6), chacune classée :

| # | régularité (v1) | v2 |
|---|---|---|
| 1 | interaction de seuil toujours conditionnée sur le premier trait fort, au seuil 0 | **retirée** : trait de condition tiré parmi les traits des autres effets ; seuil tiré dans [−0,5 ; 0,5], six décimales |
| 2 | K1 = loi du plus fort effet principal | **déclarée publique** (K1 est servie aux proposeurs) |
| 3 | fortes toujours principales ; sorte liée à la classe | **retirée** : fortes tirées parmi principale, interaction de seuil, interaction de sous-population (au moins une principale, **déclaré**) ; moyennes et faibles tirées uniformément parmi les cinq sortes observables |
| 4 | un trait ne porte jamais deux effets (sauf condition) | **déclarée publique** |
| 5 | seuil d'un effet de seuil dans [0,3 ; 1,0], positif, deux décimales | **retirée** : tiré dans [−1,0 ; 1,2], six décimales |
| 6 | un effet de sous-population ne touche qu'une sous-population | **déclarée publique** |
| 7 | sortes non équiprobables après les rejets du gabarit | **gardée, mesurée** : fréquences réalisées sur 4 000 gabarits rapportées (§2.4) |
| 8 | latent à constantes fixes, compté parmi les moyennes | **retirée** : classe « latente » à part, taille visée tirée dans [0,04 ; 0,08], poids tiré dans [0,3 ; 0,7] |
| 9 | condition = trait du premier fort = trait de K1 environ une fois sur deux | **retirée** avec la 1 (la condition peut encore tomber sur le trait de K1, au hasard) |
| 10 | au plus deux effets à seuil ; au moins deux leurres | **déclarées publiques** (contraintes de la famille) |

### 2.2 Graine scellée, paramètres tirés après le scellement

1. Le préenregistrement est scellé : il porte l'empreinte du générateur, les exigences, cette procédure, **aucun secret**.
2. Sur la machine privée qui génère, un secret machine de 32 octets est tiré (`secrets.token_bytes`) ; son **empreinte** est
   inscrite au registre **et poussée** (horodatage du dépôt) ; seulement **ensuite** Lazar donne sa phrase (Q-3, option (c)),
   dont l'empreinte est inscrite à son tour (E-12 (b) : on ne peut plus tirer, regarder, puis retirer un secret).
3. Graine du monde r : sha256(secret machine ∥ phrase ∥ empreinte du texte scellé ∥ r) (la fonction `graine_de_monde` de la v1
   avec, pour secret, la concaténation), entier ≥ 2⁶⁴.
4. Génération et vérification (C0 à C8) ; refus → retirage avec la graine suivante, au plus 8 fois ; **refus par contrôle
   rapportés** (S-9), C5 et C6 compris (ils choisissent les mondes où l'attribution marche : dit).
5. Fichiers du monde écrits au dossier privé, **hors de tout dépôt git** jusqu'au verdict (E-12 (c)) ; seules leurs empreintes
   vont au registre et au préenregistrement.
6. Course. 7. Après le verdict : secret et phrase révélés ; mondes regénérables et vérifiables ; leur publication reste un nœud
   de Lazar (Q-10).

La même procédure, avec d'autres secrets, tire les mondes de **calibration** (révélés après le banc) ; les mondes de
**développement** ont des graines publiques.

### 2.3 Programme de vérification (v2 : `outils-v2/verifier_monde_v2.py`, `d8f2f6348e0fbdbf1237ff5228b7f57a725fcf82c1a0e9945e37c149cf4c1de3` ; v1 inchangé)

| contrôle | ce qu'il vérifie |
|---|---|
| C0 forme | clés permises seules, aucun texte libre, identifiants, types, bornes (±4 ; seuils ±1,5), domaines |
| C1 structure | forte 2, moyenne 2 ou 3, faible 2 à 4, **latente 0 ou 1 (à part)** ; au moins 2 interactions ; leurres = traits sans effet (≥ 2) ; ≤ 2 conditions de seuil |
| C2 grammaire | loi compilée évaluable, `valider_loi` de la grammaire, ≤ 24 feuilles |
| C3 tailles | I_i sur deux échantillons de 50 000 instances (accord ≤ max(0,002 ; 5 %)), dans les bornes de sa classe ; leurres de sensibilité nulle |
| C4 ensemble | gain du monde [0,30 ; 0,90] ; K1 informative et partielle |
| C5 jeu planté | V-monde et au moins 3 V-K1+i au-dessus de g₀ ; diluées à ±0,002 ; fausses couvertes ≤ 10⁻³ au-delà de l'enveloppe |
| C6 oracle | attribution exacte des V-K1+i au-dessus de g₀ |
| C7 fuite (**mesure**) | touches à deux décimales des paramètres dans les pièces gelées **listées et comptées**, jamais bloquantes ; refus seulement sur une égalité à six décimales (E-7) ; à éprouver sur les vraies pièces gelées au banc |
| C8 détectabilité | 200 graines, n et m du banc ; étiquette **« certifiée détectable quand le reste du monde est connu »** si la borne basse de Wilson à 95 % ≥ 0,8 ; « indétectable » si la borne haute < 0,1 ; « proche du seuil » sinon ; **codé** : forte certifiée, moyenne de puissance ≥ 0,5, moyenne des faibles dans [0,1 ; 0,9] ; latente rapportée (E-5, E-11) |

### 2.4 Essais (R5) et banc du générateur v2

- **Essais** (`outils-v2/essais_v2.py`, `9cf54cbc95c85ad6…` ; `sorties-v2/essais-v2.stderr`) : 8 sur 8 (23:23:30 → 23:24:16) — représentant : la loi forte choisie parmi ses versions diluées et
tempérée (sain) ; en paire, la version affaiblie jamais choisie, à couverture mutuelle départagée par la tranche de choix
(artefact du médoïde v1) ; générateur : latent compté à part, fortes de sortes variées ; monde tiré conforme ou refusé hors C1
(jamais refusé pour le comptage du latent) ; écriture hors liste blanche refusée, pas d'écrasement ; vérificateur : C7 sans
refus sur 14 nombres ordinaires (le cas de la contre-lecture), refus sur égalité à six décimales ; seuil de Wilson (160 sur 200 :
non certifiée ; 186 sur 200 : certifiée).
- **Banc** (`outils-v2/banc_generateur_v2.py` coupé ; refait par parties : `banc-generateur-v2-resume.json` `26e1527aa01cc5be…`, parties `banc-generateur-v2-monde-0.json` à `-7.json` et `banc-generateur-v2-frequences.json`, chacune scellée à part ; script de parties `outils-v2/banc_generateur_v2_partie.py` (`168ed32b…`)) : refait **en parties d'un monde**, un seul processus à la fois, après deux redémarrages du conteneur (le banc complet
à 12 mondes, `banc_generateur_v2.py`, a été coupé : sa sortie vide `banc-generateur-w12-v2.stdout` est gardée) ; **8 mondes de
développement** (graines publiques 2000 à 2007) au lieu de 12, 00:00:23 → 00:22:41 : **8 conformes sur 8**, après **5 tirages
refusés** (C0 trois fois : un coefficient étalonné au-delà de ±4 ; C5 une fois ; C6 une fois — ces deux refus choisissent des
mondes où le jeu planté et l'attribution marchent, S-9) ; 6 à 9 composantes ; un latent dans 4 mondes. **C8 (200 graines,
Wilson)** : fortes 16 sur 16 certifiées ; moyennes 18 sur 18 certifiées ; faibles 20 sur 20 « proches du seuil » (puissance de
0,18 à 0,82) ; latentes 4 sur 4 « proches du seuil ». **Fréquences réalisées** sur 4 000 gabarits (E-5, E-6 (7)) : fortes
principales 4 643 sur 8 000 (58 %), interactions de sous-population 2 193, interactions de seuil 1 164 ; chez les moyennes et
les faibles, le décalage de sous-population domine (2 913 et 3 325) et l'effet de seuil est le plus rare (939 et 1 029) : les
rejets du gabarit déforment l'uniforme, ce qui est **déclaré** ; un trait latent dans 1 331 gabarits sur 4 000 (33 %).

### 2.5 Garde du secret (graine et mondes de test)

- **Ordre** : (1) pièces servies (proposeurs, expérimentateur, vérificateur) gelées et scellées ; (2) générateur, vérificateur,
  exigences gelés au préenregistrement scellé ; (3) secret machine tiré, empreinte inscrite et poussée ; (4) phrase de Lazar,
  empreinte inscrite ; (5) génération et vérification dans un processus qui n'imprime que des empreintes et des contrôles ;
  (6) empreintes du monde au registre ; (7) course.
- **Où** : secrets, devis, loi compilée, jeu planté, rapport complet : dossier privé de la machine qui génère (liste blanche),
  copié à l'octet sur la machine de la course ; **hors de tout dépôt git jusqu'au verdict** (E-12 (c) : une branche privée
  du dépôt de travail serait à portée de toute session qui clone). Après le verdict : versés au dépôt de travail ; publication
  sur ton mot (Q-10). Jamais dans `lciric/ideation-organism` ni dans la copie expurgée sans ce mot.
- **Qui lit** : des programmes seulement jusqu'au relevé scellé ; puis le lecteur du verdict (R13). Chemins ajoutés aux
  interdits communs (règle 1) de tout sous-agent jusqu'au verdict.
- **Fuite vers les proposeurs** : impossible par l'ordre (les pièces servies sont gelées avant le tirage) ; C7 la mesure
  avant la course, la recherche de la loi plantée pendant, toutes touches rapportées (R-1).

## 3. Regroupement des doublons au sein d'une génération

### 3.1 Définition opératoire (étape A, avant tout tirage)

Deux cartes d'une même génération sont **doublons** si (a) leurs formes canoniques sont égales, ou (b) elles sont
**équivalentes au sens du nul** :

- **forme canonique** (`forme_canonique`) : flottants à six décimales ; softmax recentrée sur sa ligne 0 ; mélange sans poids
  nul, composantes triées et fusionnées, composante seule déballée ; transformée sans étape déballée ; `si_sinon` à branches
  égales déballé ;
- **distance au nul** d_nul(i → j) = min, sur les membres m du nul v8 engendré par la seule loi j (j seule ; j mêlée à toute
  loi aveugle fixe ; j tempérée et inclinée), de E_x KL(p_i(·|x) ‖ m(·|x)) : **ce que i rapporterait par instance au-delà de ce
  nul si i était le monde** ; d(i, j) = min(d_nul(i → j), d_nul(j → i)) ;
- calculée sur un **jeu public de 2 000 instances** (traits et sous-populations seulement, **aucune issue**, aucun oracle),
  tiré d'une graine dérivée de la tâche de la génération ;
- **groupes** : liaison complète (deux groupes ne fusionnent que si toutes leurs paires sont sous ε), la paire la plus proche
  d'abord, égalités rompues par l'empreinte de la forme canonique (jamais par le fournisseur) ; **ε = 0,01 nat** (g₀/2).

- **et lecture par strate** (ajoutée après la synthèse, rang 2 : « la moyenne globale efface une différence confinée à une
  région rare ») : la projection m* ajustée globalement est relue au **maximum, sur 192 strates publiques** (sous-population ×
  octile de chaque trait, bornes de la loi normale publique), de la moyenne de KL(p_i ‖ m*) dans la strate ; une paire n'est
  admissible au regroupement que si d < ε **et** d_strat < ε_strat = 0,04 (`outils-v1/complements_synthese_v1.py`,
  `grouper_stratifie`).

Pourquoi ces seuils : deux lois à moins de 0,01 nat l'une du nul de l'autre ne peuvent pas différer d'une « vraie découverte »
(g₀ = 0,02) dans le monde le plus favorable à l'une ; la liaison complète empêche la chaîne a ~ b ~ c avec a ≁ c (essai
`test_liaison_complete_sans_chaine`) ; ε_strat = 4·ε parce qu'une différence étalée sur un octile pèse environ huit fois plus
dans sa strate que dans la moyenne. Banc (`sorties-v1/banc-complements-synthese-v1.json`, `c3f90d88…`) : un effet de seuil
**rare** (z > 1,5 sur un trait distracteur, décalage 0,8) donne d = 0,0095 (la règle globale le fusionnerait) mais d_strat =
0,063 (séparé) ; des variantes bruitées (σ = 0,05 à 0,3, une par σ, dans le monde du banc) restent à d_strat ≤ 0,014 (regroupées). Essais
`essais_complements_synthese_v1.py` : 6 sur 6. Une borne au pire monde (E_x max_y |log p_i − log m|) est aussi rapportée.

### 3.2 Qui le calcule

Un **programme de l'orchestrateur** (`grouper`), entre le gardien et le juge, sur les seules lois des cartes passées au
gardien ; déterministe ; recalculé par la lecture gelée (même entrée → mêmes groupes, sinon écart). **Jamais** un modèle,
jamais un juge de la famille de l'auteur du monde, jamais un score de moniteur (N-053, point 5). Les lois plantées n'y entrent
pas.

### 3.3 Effet sur le juge statistique

- Chaque carte est jugée comme aujourd'hui (tirages frais propres, graine de sa tâche) ; sa e-valeur est arrêtée au seuil
  m/α (`appliquer_multiplicite`).
- **e-valeur d'un groupe = moyenne des e-valeurs de ses membres** (`log_e_groupe`) : une moyenne d'e-valeurs est une e-valeur
  (chaque carte teste le même nul : « le monde est dans la classe du nul de l'archive ») ; la perte au pire est log(taille du
  groupe) quand un seul membre porte la preuve.
- **e-BH sur les groupes**, m fixé d'avance par **règle écrite** (V-4, même règle que la v67 : cartes + plantées + instruments) :
  m = 6 × (proposeurs) + 12 vraies (le monde, au plus 9 « K1 + un effet », 2 diluées) + 5 fausses (F1 à F4, F5) + 4 copies + H1
  + 2 instruments (T-ELIM, T-MAL) = **48** à quatre proposeurs, **54** avec Kimi (seuil hors famille log(48/0,05) ≈ 6,87 ; les
  simulations ont pris m = 44, soit 0,087 nat de moins : sans effet sur la validité, à refaire au banc). Les rangs comptent
  des groupes, non des copies. Ainsi onze copies à log e = 4,5 ne se portent plus l'une l'autre au-dessus du seuil de rang 11
  (log(40/(0,05·11)) ≈ 4,29) : leur groupe affronte le seuil de rang 1, log(40/0,05) ≈ 6,68 (essai
  `test_e_bh_par_groupe_ne_compte_pas_les_copies`).
- Lois plantées : inchangées (hors famille, seuil log(m/α), avec l'archive de leur génération).
- **Preuve écrite de validité** (condition bloquante de la synthèse pour un regroupement avant le juge ; à contre-lire) : sous le
  nul H₀ « le monde est dans la classe du nul v8 de l'archive de la génération », la richesse de chaque carte i, calculée sur ses
  propres tirages frais, est majorée par une surmartingale positive d'espérance ≤ 1 ; arrêtée au premier instant de lecture où
  elle atteint m/α (temps d'arrêt), elle donne une e-valeur E_i, E[E_i] ≤ 1 (arrêt optionnel). Les groupes sont une fonction
  des seules lois des cartes et d'instances publiques **sans issue**, fixée avant tout tirage : ils sont indépendants des
  tirages. Donc Ē_g = (1/|g|) Σ_{i∈g} E_i vérifie E[Ē_g] ≤ 1 : c'est une e-valeur. La règle e-BH (Wang et Ramdas, 2022) appliquée
  à des e-valeurs, sous dépendance quelconque, avec m ≥ nombre d'hypothèses fixé avant les tirages, borne le taux de fausses
  découvertes par α. Le représentant (§3.4) n'entre pas dans Ē_g.
- **Hypothèses de la preuve, écrites** (E-8) : (a) « majorée par une surmartingale d'espérance ≤ 1 » n'est établi que pour la
  classe linéaire du nul v8 ; pour le membre tempéré et incliné, le nul v8 dit seulement « au second ordre près de l'optimum,
  sans preuve » (texte v2 §3.4) : le regroupement n'ajoute rien à cette réserve et ne l'efface pas ; (b) la preuve suppose que
  le code gelé arrête les valeurs e comme le juge simplifié (au premier instant de lecture où W ≥ m/α), ce que personne n'a lu
  ici : à vérifier sur le code v68 ; (c) elle porte sur H₀ « le monde est dans la classe du nul de l'archive », **fausse par
  construction** dans un monde riche : elle ne borne **pas** la part des fausses découvertes au sens de l'oracle (retenues à
  moins de g₀ au-delà de l'archive). Les simulations en montrent bien plus que α (retenues à moins de g₀ au-delà de l'enveloppe : 11 sur 94 et 12 sur 78 en v1 ; 16 sur 108 et 14 sur 75 en v2) : le préenregistrement ne
  reprend **pas** α comme borne de cette part ; sa tolérance est une décision (Q-9).
- Toutes les cartes testent le même H₀ (comme en v67) ; l'oracle dit après la course ce qui est une découverte.

### 3.4 Effet sur la sélection et sur l'héritage

- **Règle du représentant v2** (E-1 ; `outils-v2/monde_riche_outils_v2.py`, `representant_v2`) : (1) **couverture dirigée**
  minimale : pour chaque membre r, c(r) = max sur les autres membres j de d_nul(j → r) ; le représentant est le membre dont le nul
  couvre le mieux tous les autres (une loi diluée ou tempérée est dans le nul de la loi forte, l'inverse est faux : la loi forte
  est choisie) ; (2) à couverture mutuelle (écart ≤ 10⁻³, par exemple deux températures d'une même loi), départage par une
  **tranche de choix** : 400 épisodes frais, distincts des tirages du juge et de la tranche du test de mort, **une seule par
  groupe, la même pour tous les candidats**, tirée de la tâche du groupe (empreintes canoniques triées de ses membres) ;
  statistique gelée du test de mort calculée par l'orchestrateur (v3, V-1 : le code v2 tirait une tranche différente par
  candidat, `outils-v3/puissance_monde_riche_v3.py`, `representant_v3`) ; (3) puis l'empreinte canonique. Aucun pas n'utilise les tirages du juge ni
  l'oracle. La phrase de la v1 « d'effet borné par ε sur le gain du représentant » était **fausse** (contre-lecture : jusqu'à
  0,27 nat de perte) et est retirée. **Mesure v3, tranche appariée** : (`sorties-v3/representant-v3-resume.json`, `7dfa085d…`, et 12 parties scellées `representant-v3-monde-*.json`, 00:42:38 → 00:44:40) : mêmes 82 groupes ; perte au-dessus de 0,01 nat dans **un seul groupe** (monde 4 : une tempérée à 0,3 préférée à la loi, 0,038 nat de perte), médiane 0, **jamais sous g₀ à tort** ; départages : 38 par la couverture, 44 par la tranche de choix. L'appariement ramène la perte maximale de 0,167 à 0,038 nat. Une tranche de 2 000 épisodes, appariée, est proposée au banc (les épisodes sont tirés par le noyau, sans coût), à éprouver. **Mesure v2, tranche non appariée, pour mémoire** (`sorties-v2/representant-w12-v2.json`, `e6e157ea0056a6fb…`, 23:24:16 → 23:25:03) : sur 12 mondes tirés, un groupe de six variantes d'une loi (elle-même, diluée à 0,5, 0,2 et 0,05,
tempérée à 0,3 et 2,0) et ses cinq paires, soit **82 groupes regroupés** : le **médoïde v1** perd plus de 0,01 nat sur le meilleur
membre dans 42 groupes (médiane 0,023, maximum 0,44) et tombe **sous g₀ alors que le meilleur membre est au-dessus dans 11
groupes** ; la **règle v2** perd plus de 0,01 dans 6 groupes (médiane 0, maximum 0,167) et **jamais sous g₀**. Les 6 pertes
restantes sont toutes des départages par la tranche de choix entre versions tempérées qui se couvrent mutuellement (bruit
d'une tranche de 400 épisodes non appariée ; une tempérée à 2,0, surconfiante, a été préférée une fois à 0,167 nat près ; T-1 :
ces 6 groupes sont **3 situations** (mondes 6, 10, 11), chacune comptée deux fois, dans le groupe de six et dans sa paire). Départages : 38 par
la couverture, 44 par la tranche de choix, 0 par l'empreinte.
- **Sort du groupe** : le représentant seul est testé au test de mort ; s'il meurt ou si son test est coupé par sa borne
  (« non concluant »), le groupe est éliminé de la génération ; ses sœurs sont réinjectées **après la course** (mesure, S-2).
- **Retenues** = représentants survivants ; **archive** de la génération suivante = archive + retenues ; **vue servie** aux
  proposeurs = cette archive (garde 23 inchangée). Les autres membres sont écrits au relevé (identifiants, fournisseurs,
  distances), jamais servis.
- Copies plantées de la génération suivante (P5) : copies des quatre premières **représentantes** retenues.

### 3.5 Étape B (redondance jugée sur tirages frais) : rejetée pour la sélection

J'ai essayé deux élagages après e-BH, sur tirages neufs : (i) garder un représentant seulement s'il bat le nul de l'archive
et des représentants déjà gardés ; (ii) écarter un représentant **dominé** (un autre va au-delà de lui, lui pas au-delà de
l'autre). Avec le nul v8, qui ne sait que mêler et tempérer, une loi qui apporte un effet neuf mais en manque un autre ne
« va pas au-delà » d'une loi meilleure : les deux élagages écartent des lois **complémentaires**. Sur 12 mondes (`doublons-w12-v1.json`, génération synthétique de 24 cartes), l'élagage par domination garde 4,25 lois et **2,5 idées distinctes** en moyenne, contre 7,3 représentants et **4,7 idées** sans lui ; la première forme écartait davantage encore (essai de développement sur quatre mondes, non versé : aucun chiffre n'en est tiré). L'étape B
n'est donc **pas** une règle de sélection ; elle peut être rapportée comme mesure (redondance par domination), sans effet.

**Contrôle des groupes mal formés (repris du « temps 1 » de la synthèse, comme mesure ; S-2 : fait **après la course**, avec
les sentinelles, non entre deux générations)** : chaque sœur d'un représentant retenu est rejugée hors ligne (tirages neufs, tâche propre, sans agent) contre le nul
de archive ∪ {son représentant} ; une sœur promue montre un groupe mal formé : comptée, rapportée, sans effet sur la sélection ni
sur l'héritage.

### 3.6 Essais hors ligne

**v2, sur la famille tirée et avec la règle v2** (`sorties-v2/doublons-w12-v2.json`, `984df2bafef31527eaf7df5ac02ce714d166abc1948b06d0777f515056869dfa`, 23:28:56 → 23:30:32) : 12 mondes tirés du générateur v2 (6 à 9 composantes, latent dans certains), ε = 0,01, ε_strat = 0,04,
n = 400, m = 44. Paires à regrouper : reformulation, tempérée 1,2, mêlée 0,8 + 0,2 uniforme, variantes σ = 0,05 et 0,1 :
**12 sur 12** chacune ; σ = 0,2 : 10 sur 12 ; σ = 0,3 : 6 sur 12 (lois nettement moins bonnes : les garder à part ne coûte qu'un
groupe). Paires à ne pas regrouper : ajout d'un effet moyen et loi distincte : 12 sur 12 ; **ajout d'un effet faible : 11 sur 12
— une fusion à tort** (un effet faible confondu avec sa base dans un monde : la lecture par strate ne l'a pas séparé ; à
rapporter, et à éprouver au banc). Génération synthétique de 24 cartes : 12,0 groupes en moyenne, 11,7 purs ; e-BH **par carte :
16,7 retenues et 5,33 idées distinctes ; par groupe, avec la règle v2 : 7,83 retenues et 4,92 idées** — le regroupement divise
par deux les retenues et **perd en moyenne 0,4 idée** dans cette famille (la v1, sur la sous-famille, n'en perdait pas) : dit.
**v3, tranche appariée** (`sorties-v3/doublons-v3-resume.json`, `b9032dd8…`, 12 parties scellées, → 00:52:52) : mêmes groupes et
mêmes retenues (7,83 par groupe) ; **5,00 idées** distinctes parmi les représentants, contre 5,33 par carte : la perte tombe à
0,33 idée. Le
regroupement **réduit les doublons sans les supprimer** (S-4) : dans la v1, 7,3 lois retenues pour 4,7 idées, et à ε = 0,01
deux idées sur trois coupées en plusieurs groupes (la liaison complète préfère couper que mêler).

**v1, conservé pour mémoire** (gabarit fixe, représentant au plus grand log e : sous-famille, E-4) :

Sortie `sorties-v1/doublons-w12-v1.json` (`2e8cb29bb4263a13e9b3724ead768be38391260e19bd89becc500bccdaa29d99`, 21:23:21 → 21:34:17) ; 12 mondes MR-1 ; distances sur 2 000
instances de référence. Paires (a = monde restreint aux deux fortes et à une moyenne ; b = sa transformée) :

| paire | doit être regroupée | d médiane [min ; max] (nat) | gain oracle b − a (médiane, nat) | justes à ε = 0,005 | 0,01 | 0,02 |
|---|---|---|---|---|---|---|
| reformulation (lignes décalées, composante à poids nul) | oui | 0 [0 ; 0] | 0 | 12/12 | 12/12 | 12/12 |
| tempérée 1,2 | oui | 0 [0 ; 0] | −0,018 | 12/12 | 12/12 | 12/12 |
| mêlée 0,8 + 0,2 uniforme | oui | 0 [0 ; 0] | −0,011 | 12/12 | 12/12 | 12/12 |
| variante σ = 0,05 | oui | 0,0003 [0 ; 0,0031] | −0,001 | 12/12 | 12/12 | 12/12 |
| variante σ = 0,1 | oui | 0,0012 [0,0002 ; 0,0047] | −0,002 | 12/12 | 12/12 | 12/12 |
| variante σ = 0,2 | oui | 0,0099 [0,0012 ; 0,078] | −0,015 | 4/12 | 6/12 | 10/12 |
| variante σ = 0,3 | oui | 0,0146 [0,003 ; 0,046] | −0,038 | 1/12 | 3/12 | 8/12 |
| ajout d'un effet faible | non | 0,028 [0,023 ; 0,034] | +0,023 | 12/12 | 12/12 | 12/12 |
| ajout d'un effet moyen | non | 0,061 [0,048 ; 0,079] | +0,061 | 12/12 | 12/12 | 12/12 |
| distincte (une moyenne échangée) | non | 0,109 [0,096 ; 0,128] | +0,009 | 12/12 | 12/12 | 12/12 |
| distincte (une forte en moins) | non | 0,107 [0,078 ; 0,160] | −0,161 | 12/12 | 12/12 | 12/12 |

Les variantes à σ ≥ 0,2 qui restent séparées sont de **moins bonnes** lois (−0,015 et −0,038 nat) : les garder à part ne coûte
qu'un groupe. Génération synthétique de 24 cartes (trois idées × six variantes à σ = 0,15, plus six cartes au hasard) : à
ε = 0,01, 11,75 groupes en moyenne, **99,3 % de groupes purs** (une seule idée), 2,1 idées sur 3 coupées en plusieurs groupes
(la liaison complète préfère couper que mêler) ; à ε = 0,02, 9,8 groupes, 97,5 % purs. Effet sur e-BH (archive {K1}, n = 200,
m = 40) : **15,4 cartes retenues par carte et 4,75 idées distinctes ; 7,3 groupes retenus et 4,67 idées** ; élagage par
domination : 4,25 et 2,5. Variantes « à la v67 » (`sorties-v1/variantes-v67-v1.stdout`) : huit cartes écrites par programme
dans le monde S-V1 (L* arrondie, bruitée, en `si_sinon` sur z0, par sous-population, tempérée ; z1 seul ; un découpage par
morceaux sur z1) → **3 groupes** à ε = 0,01, 0,02 et 0,05 : les six formes de L* ensemble (distances ≤ 0,009), « z1 seul »
(0,343 nat au-delà de K1 contre 0,468, distance 0,033 à 0,054) et le découpage (0,284 nat, distance ≥ 0,134) à part.
Essais (`essais_monde_riche_v1.py`, `essais_complements_synthese_v1.py`) : copies regroupées (artefact), lois distinctes et
lois emboîtées non regroupées (cas sain), chaîne refusée par la liaison complète, e-valeur de groupe = moyenne, e-BH par groupe
qui ne compte pas les copies, différence rare séparée par la lecture par strate, médoïde indépendant de l'ordre d'entrée.

### 3.7 Garde neuve (liste d'arrêt)

**Garde 25 (regroupement)** : cas sain — groupes, représentants **et tranche de choix de chaque groupe (même graine de tâche,
mêmes épisodes) recalculés par la lecture à l'identique**, égaux à ceux du relevé ; e-valeurs de
groupe égales à la moyenne de celles des membres ; un seul représentant par groupe, choisi par la **règle v2** (couverture dirigée, tranche de choix du groupe), testé et retenu. Artefacts — deux représentants d'un même
groupe retenus, un membre servi aux proposeurs, groupes dépendant de l'ordre des fournisseurs (permutation des fournisseurs →
mêmes groupes), une loi plantée dans un groupe → arrêt, code 3, incident consigné.

### 3.8 Confrontation au rang 2 de la synthèse du collisionneur

| point | synthèse (non contre-lue) | cette conception | statut |
|---|---|---|---|
| distance | prédictive, grille publique, maximum par strate, diamètre en log-rapport, lien complet, départage par empreinte | prédictive **au sens du nul** (projection sur le nul v8 de l'autre loi, pas une simple divergence), grille publique de 2 000 instances, maximum par strate (192), borne au pire monde rapportée, lien complet, départage par empreinte | convergent (strates ajoutées après lecture) |
| quand | temps 1 : après le test de mort, juge inchangé, sœurs réinjectées ; temps 2 (avant le juge) seulement avec une preuve écrite ; divergence ouverte (confiance 0,55 pour « après ») | **avant le juge**, preuve écrite et ses hypothèses (§3.3) ; réinjection gardée comme mesure après la course. Ton mot R-2443 est « il faut regrouper les doublons au sein d'une même génération » : les deux temps y répondent (E-10). Ce que l'un fait et l'autre non : avant le juge, les copies ne se portent plus l'une l'autre dans e-BH (15,4 retenues par carte contre 7,3 groupes, `doublons-w12-v1.json`) et il y a moins de tests à payer ; après, le juge v67 reste intact | **divergence** ouverte (Q-8) |
| représentant | jamais par la plus grande valeur e ; médoïde ou empreinte, avant les données | **règle v2** avant les données du juge (couverture dirigée, tranche de choix fraîche à égalité) ; le médoïde de la v1 est abandonné (E-1) | convergent sur le principe |
| e-valeur des sœurs | temps 2 : e = 0 pour les sœurs, m inchangé | moyenne des e-valeurs des membres (toutes les cartes jugées) | deux formes valides ; la moyenne garde la preuve d'une sœur meilleure que le médoïde, au prix de log(taille du groupe) au pire |
| seuils | « deux seuils (juge, oracle), le plus strict » : position de la **seule espèce A** ([A-T3]), non une convergence (S-8) | ε et ε_strat fixés sur des mondes de développement, sans juge ni oracle | divergence mineure : un seuil tiré du refus du juge mesure la proximité au juge, non la redondance (objection d'E en [E-T2]) |
| composantes non séparables | « fusionnées avant la course » (rang 1) | **non traité** en v1 ; v2 : au banc de calibration, deux composantes dont l'attribution ne se sépare pas (C6 en écart sur leurs V-K1+i) sont fusionnées en une composante de D2 ; règle à écrire au préenregistrement (S-8) | repris |
| certification | contre l'archive de la génération (sentinelles) | contre le reste du monde (C8, avant la course) ; contre l'archive réelle **après** la course (sentinelles, §1.8) (S-8) | divergence dite |

## 4. Mesure de la diversité des idées retenues

### 4.1 Définitions

- **D1, par programme, sans oracle, descriptive** (`diversite_programme`), calculée **après** la sélection scellée de chaque
  génération, jamais servie, jamais optimisée, sur les cartes proposées, promues et retenues et sur l'archive : nombre de
  **groupes** (étape A) ; **nombre effectif de Hellinger** N_eff = k²/‖K‖²_F, K_ij = E_x Σ_y √(p_i p_j) (semi-défini positif ; 1
  pour k lois égales ; `n_effectif_hellinger`, synthèse section 2) ; **signature de traits** de chaque loi (sensibilité à chaque
  trait et à la sous-population : E_x KL(p(x) ‖ p(x avec ce trait retiré au hasard)), `signature_traits`) ; nombre de
  **supports distincts** (ensembles de traits de sensibilité ≥ 0,005 nat) ; **traits couverts** ; **entropie** de la signature
  agrégée ; distance moyenne entre paires.
- **D2, mesure principale, par l'oracle, lu une seule fois après la course** (convergente avec la section 2 de la synthèse) :
  nombre de composantes du monde **certifiées détectables quand le reste du monde est connu** (C8 : borne basse de Wilson ≥ 0,8 à
  200 graines ; E-11) **couvertes** par au moins une loi, chacune comptée une fois,
  **additionnelles à l'archive** du début de la génération (`complements_synthese_v1.couverture`), mesuré à trois étages :
  **propositions brutes** (toutes les cartes rendues qui s'évaluent : c'est la mesure des proposeurs, N-058), **représentants**
  (après regroupement), **retenues** (après juge et test de mort) ; les écarts entre étages sont les pertes de la chaîne. Une loi
  couvre la composante i si Δ_i = gain(loi | W) − gain(loi | W₋ᵢ) ≥ max(0,005 ; 0,75·I_i) (`Oracle.attribution`) — critère sur
  les prédictions, invariant à la syntaxe ; la synthèse rapporte la chute à celle de la loi plantée elle-même, je la rapporte à
  I_i (même rôle ; à fixer au préenregistrement). Stratifiée par classe et par étiquette de C8 ; composantes « proches du
  seuil » rapportées à part ; gain de l'**enveloppe** de l'archive par génération (progrès) ; par fournisseur : composantes
  couvertes par ses propositions brutes, avec le coût.
- **Catégorie « recombinaison »** (S-3) : une loi retenue à plus de g₀ au-delà de l'enveloppe de l'archive **sans** composante
  nouvelle couverte est rapportée à part : dans un monde par morceaux, c'est le chemin naturel hors de la classe couverte ; la
  sonde H1 ne le mesure pas (son gain au-delà de l'enveloppe est négatif dans les 12 mondes de la v1).
- **Validation de l'attribution, v2 sur la famille tirée** (`sorties-v2/attribution-w12-v2b.json`, `3c4d00c81a23938c3f91f9266fe7047a97644e1947d5f0242e33b2e88de13a6d`, 23:41:40 → 23:42:03 ; script neuf `outils-v2/attribution_v2b.py` (`dee69027…`) : la sous-commande `attribution` du script v2 s'est arrêtée sur la classe « latente » inconnue du résumé v1 (`attribution-w12-v2.stdout`, gardé)) : 144 lois synthétiques dans 12 mondes tirés : ensemble exact retrouvé pour **107 sur 144 (0,74 ;
Wilson [0,67 ; 0,81])**, contre 0,88 sur la sous-famille de la v1. Fortes : 124 sur 124 ; moyennes : 166 retrouvées, 8 manquées,
7 attribuées à tort ; faibles : 124, 3, 4 ; **latente : 4 sur 23** — un trait non observé ne se « capte » pas par une loi
prédictive : retirer la latente du monde change peu la note d'une loi qui la contient (elle ne peut que se calibrer). Donc :
**D2 exclut la composante latente** (rapportée à part) ; le seuil d'attribution (0,75·I_i), réglé sur la sous-famille, est à
refixer au banc de calibration sur la famille tirée (E-4).
- **Validation de l'attribution, v1** (`sorties-v1/attribution-w12-v1.json`, `816a7477…`, 21:23:02 → 21:23:21) : sur 144 lois synthétiques (mondes restreints à un sous-ensemble connu d'effets, coefficients bruités, σ = 0,15) dans 12 mondes MR-1, l'ensemble des effets captés est **exactement** retrouvé pour 127 lois sur 144 (0,88 ; Wilson [0,82 ; 0,93]) ; aucune erreur sur les effets forts (129 sur 129) ni moyens (128 sur 128) ; sur les faibles, 174 retrouvés, 12 manqués, 5 attribués à tort. D2 est donc fiable pour les fortes et moyennes, approchée pour les faibles (dit au rapport).

### 4.2 Coût

Programme seul : de l'ordre de la seconde à la minute de processeur par génération (2 000 instances de référence ; 276 paires
pour 24 cartes) ; oracle : quelques minutes après la course. Aucun appel.

### 4.3 Ce qu'elle ne doit pas piloter

- **La composition des proposeurs** : jugée sur l'oracle et le coût seuls (N-058) ; D1 dérive des verdicts (cartes promues et
  retenues) et ne peut pas servir à choisir ou pondérer un proposeur ; D2 peut être **rapportée** par fournisseur comme
  information, la décision de composition restant à un texte neuf et à Lazar.
- **La sélection** : aucune prime de nouveauté dans le juge ni dans la retenue (la diversité serait alors une cible à
  tromper) ; **les consignes des proposeurs** pendant la course (rien de D1 ni de D2 n'est servi) ; **le nombre de générations**.
- Une course qui voudrait **agir** sur la diversité (consignes diversifiantes, proposeurs à rôles, nouveauté dans la sélection)
  est un dessin neuf : c'est la place de la synthèse du collisionneur (§5.4).

## 5. Proposeurs

### 5.1 Composition proposée

| rôle | modèle | crédits | remarque |
|---|---|---|---|
| proposeur | Claude Fable 5.2 (`claude-fable-5-2`) | Claude | moins chère que 5.1 (8 / 40 contre 10 / 50, plan des crédits §1) ; le choix de version est à toi (Q-7) |
| proposeur | Claude Opus 5.5 (`claude-opus-5-5`) | Claude | |
| proposeur | Argon (`gemini-4-argon`) | hors crédits | prix supposé 10 / 50 |
| proposeur | Astra (`gpt-6-astra`) | hors crédits | identifiant « rapporté, à confirmer », prix supposé 10 / 50 ; « si retenu » (R-2444) |
| proposeur (si son compte est rechargé) | Kimi (`kimi-k3.1-pro`) | hors crédits | redevenu possible : aucune famille n'est exclue du fait de l'auteur du monde (R-2461) ; compte suspendu le 11 novembre (R-2389) ; Q-7 |
| expérimentateur des tests de mort | Opus 5.5 | Claude | crédits qui expirent ; Kimi possible (le moins cher, éprouvé en v67) s'il est rechargé ; Q-2 |
| vérificateur | Argon | hors crédits | autre famille que l'expérimentateur (garde 9) |
| auteur du monde | **programme** (générateur à graine scellée, §2) | — | aucune famille de modèles |

Six cartes par proposeur et par génération (24 cartes ; 30 avec Kimi, soit jusqu'à **6 représentants de plus à tester** par
génération : compté au devis, E-9 (c)), comme la v67 ; un appel par proposeur et par génération. Aucun juge
d'idées à modèle : le juge reste mécanique.

### 5.2 Isolement et témoins par test

- **Proposeurs** : chaque appel est une session neuve sans historique, par le relais de son fournisseur ; la **réponse brute**
  de l'interface (corps entier, avant toute extraction), le texte servi et son empreinte, l'en-tête du modèle servi, l'usage
  (Kimi `prompt_tokens`/`completion_tokens` ; Argon `entree`/`sortie` tels que le relevé v67 les porte ; Claude
  `input_tokens`/`output_tokens` ; Astra : à fixer) sont écrits dans `sessions-proposeurs/<monde>/<génération>/<proposeur>/`
  et scellés **avant** l'extraction des cartes. **Garde 26** : dossier vide ou réponse brute absente → arrêt, code 3 (réserve
  R-2 (a) de la v67) ; cas sain et artefact.
- **Tests de mort** : pour **chaque** exécution, un **témoin d'isolement** versé : description de la sonde (`bwrap`, version,
  options `--unshare-all --unshare-net`, profil `--seccomp` et son empreinte), identité dans le bac (64097, sortie de `id`), fichier
  témoin écrit dans le bac et relu sur l'hôte (propriétaire, empreinte), journal de `bwrap`, code de sortie ; scellé à côté de
  `gains.csv`. **Garde 27** : témoin absent ou incohérent → le test est « non concluant » et la course s'arrête (code 3)
  (réserve R-2 (b)).
- **Comptes** : le relevé compte, par fournisseur, appels, jetons et dollars, rapprochés du journal de chaque relais (réserve
  R-6) ; « sans usage » compté à part.

**Les sept réserves du verdict v67 (R-2441) et leur réponse dans ce dessin** : R-1 (touches de la recherche de la loi
plantée tues) → toutes rapportées, relues à la main (K-9, §2.3) ; R-2 (réponses brutes et témoins de `bwrap` absents) → gardes
26 et 27 (ci-dessus) ; R-3 (`arbre_modifie` sans explication) → le manifeste nomme chaque fichier non suivi (copie du texte
scellé) ; R-4 (une carte de moins) → m reste une borne, le relevé compte les cartes rendues par fournisseur ; R-5 (génération
2 sans contenu, retenues proches d'un même constat) → monde riche (§1) et regroupement (§3) ; R-6 (jetons d'Argon) → champs
`entree` et `sortie` lus (K-9) ; R-7 (égalité à l'octet de la lecture) → la lecture écrit l'heure et le chemin à part de son
corps empreinté.

### 5.3 Ce que la lecture rapporte par fournisseur (N-058)

Cartes proposées, refusées au gardien, groupes auxquels il contribue, représentants promus, retenus, vraies et fausses
découvertes (oracle, v60 et enveloppe), effets captés (D2), coût. **Aucun classement par verdicts**, aucune décision de
composition dans la course.

### 5.4 Synthèse du collisionneur sur la diversité des idées : ce qui est repris, ce qui diverge

La synthèse (`4f99077b…`, non contre-lue) est arrivée pendant ce travail ; elle est traitée comme une entrée.

- **Rang 1 (monde riche calibré, leurres)** — repris : composantes **certifiées détectables** (C8, étiquette ≥ 0,8), **traits
  leurres** (au moins 2 distracteurs, sensibilité nulle vérifiée par C3), mondes témoins à une composante et à vérité dans le
  nul (banc, §1.8), mondes répartis **développement / calibration / test scellés** (§1.8), nombres de composantes **tirés
  privément par monde** (§1.2), et, depuis ton mot R-2461, le **monde écrit par programme** (§2). Écart qui reste : la synthèse
  veut chaque composante ≥ 80 % détectable ; ta décision R-2443 demande des effets « du fort au proche du seuil » : je garde des
  faibles détectables 10 à 90 % en moyenne, **étiquetés** et comptés à part, pour que « idée manquée » ne se confonde pas avec
  « effet hors de portée du juge ».
- **Rang 2 (regroupement)** : §3.8.
- **Rang 3 (portefeuille de missions servies aux proposeurs, contre témoins à coût égal)** — **non repris** dans cette course :
  la synthèse le place après un duel ; il changerait les consignes des proposeurs (à geler avant le tirage des mondes, §2.5) et
  demanderait ses témoins (même catalogue sans partage, tirages répétés du même modèle). **Place réservée** dans le
  préenregistrement : une section « Diversification », vide par défaut.
- **Rang 4 (garde certifiée en absolu, extension bornée du nul)** — rejoint Q-4 ; la sonde hors classe H1 et le classement des
  fausses découvertes par forme en sont la part mesurée ici.
- **Rang 5 (allocation entre proposeurs sur l'oracle et le coût)** — convergent avec N-058 et le §5.3 : **rapportée** par
  fournisseur (D2 sur propositions brutes, coût), **aucune allocation pendant la course** ; une règle d'allocation est un texte
  neuf, après la course.
- **Rejets de la synthèse, tous tenus ici** : aucune prime numérique de nouveauté (§4.3), aucun quota de formes, aucun masquage
  de l'archive, aucun représentant choisi par la plus grande valeur e (§3.4).
- **Ordre proposé par la synthèse** (banc de métrologie, puis pilote A/A des proposeurs, puis duel « le monde offre-t-il, les
  proposeurs prennent-ils ? », puis seulement la course à plusieurs générations) : **divergence partielle**. Le banc de
  métrologie est repris comme **préalable sans dépense** (§1.8). Le pilote A/A et le duel ajoutent une étape payante avant la
  course que tu as acceptée (R-2442) ; je propose de lire « le monde offre-t-il » par C8 et « les proposeurs prennent-ils » par
  D2 sur les propositions brutes de la génération 1, dans la course même. Question Q-8.

## 6. Devis (v2 : pire cas par formule, E-9)

Script `outils-v2/devis_multi_generations_v2.py` (`710954c7cf3fd144…`), sortie `sorties-v2/devis-v2.json`
(`c722b8020e67a96…` ; compagnon). Tout est **estimé** sauf les prix cités, « à vérifier » au moment du GO.

### 6.1 Génération des mondes

Par programme (R-2461) : **calcul seul**, aucun appel (≈ 1 à 4 minutes de processeur par monde vérifié, C8 à 200 graines
compris). Aucune ligne de GO.

### 6.2 Course à plusieurs générations

**Formule** (par monde et par génération) : pire = Σ plafonds de session des proposeurs + T_pire × (borne par test de
l'expérimentateur + 0,10 de vérificateur) ; **T_pire = 6 × (nombre de proposeurs) représentants + 13 vraies plantées
replantées à chaque génération** (le monde, au plus 9 « K1 + un effet », 2 diluées, T-ELIM) [**+ 9** si les fausses et les copies
promues sont testées : F1 à F4, F5, 4 copies ; **H1 promue n'est pas testée**, lue à la promotion comme mesure ; Q-12] ;
central : 16 tests (6 représentants, 10 plantées promues) — **un peu bas** : la simulation v2 promeut 9,2 représentants en
génération 1 (T-2 : ≈ + 4 USD au central à 2 × 3). **Aucune reprise** d'un appel de proposeur : une session en échec arrête la
course (comme la v67, garde 13) ; le pire cas compte donc un appel par proposeur et par génération (T-3). **Plafonds de session par modèle**
(S-6) : Opus 2, Fable 5.2 3 (≈ 75 000 jetons de sortie, au-dessus du cas central de 35 000), Argon 2, Astra 2, Kimi 1,5 USD.
**Borne par test** propre à l'expérimentateur : 12 tours à 8 000 / 4 000 jetons (estimé), soit Opus 1,50, Kimi 0,80 (devis v66),
Argon 3,40 USD ; **un test coupé par sa borne est « non concluant »** (le groupe est éliminé, rapporté). La réflexion d'Opus est
facturée comme sortie et ne se coupe pas (plan des crédits, l. 50) : la borne par test est ce qui la tient.

Expérimentateur Opus 5.5, quatre proposeurs, fausses promues non testées ; USD « central / pire » :

| mondes × générations | Claude (crédits) | Argon | Astra | total des modèles | machine, central (plafond) |
|---|---|---|---|---|---|
| 1 × 3 | 14,11 / 181,50 | 3,63 / 17,10 | 3,00 / 6,00 | 20,74 / 204,60 | 0,45 (10) |
| 2 × 3 | 28,22 / 363,00 | 7,26 / 34,20 | 6,00 / 12,00 | 41,48 / 409,20 | 0,90 (10) |
| 3 × 3 | 42,34 / 544,50 | 10,89 / 51,30 | 9,00 / 18,00 | 62,23 / 613,80 | 1,35 (10) |

Variantes à 2 × 3 : **Kimi cinquième proposeur** (43 tests au pire) : Claude 28,22 / 417,00, Argon 7,26 / 37,80, Kimi 2,16 / 9,00,
total 43,64 / 475,80 ; **fausses et copies promues testées** (T_pire = 46) : Claude 28,22 / **444,00**, total ≈ 41,48 / **495,60**
(par la formule ; la sortie `devis-v2.json` porte encore 435 et 486 pour « + 8 », V-6) ; **Kimi
expérimentateur et cinquième proposeur** : Claude 14,40 / 30,00, Kimi 9,07 / 215,40, total 36,73 / 295,20. La v1 sous-comptait
le pire cas (226 USD à 2 × 3) : 9 plantées au lieu de 13, pas de replantation dite, tests de Kimi proposeur oubliés, borne de
0,80 prise aux prix de Kimi.

### 6.3 Lignes de GO proposées (aucune inscrite)

Montants à **2 mondes × 3 générations** (Q-1) ; entre crochets, 1 et 3 mondes ; plafonds = pire cas par formule, arrondi
au-dessus ; plafond de chaque relais ou clé égal à sa part.

| ligne | texte | plafond | échéance |
|---|---|---|---|
| GO-β1 (crédits de Claude) | **Course de l'organisme à plusieurs générations, part sur crédits de Claude** : proposeurs Fable 5.2 (plafond de session 3 USD) et Opus 5.5 (2 USD), expérimentateur Opus 5.5 (1,50 USD par test, test coupé = non concluant) ; 2 mondes × 3 générations ; vraies plantées replantées à chaque génération ; conditions toutes exigées : préenregistrement neuf contre-lu et scellé, code v68 contre-lu (regroupement, règle du représentant v3 à tranche de choix appariée, réponses brutes, témoins par test), banc de calibration fait (n et seuils fixés par leurs règles), mondes vérifiés et leurs empreintes inscrites ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 365 USD sur crédits [185 ; 545] | 2026-11-30, et avant la fin de cycle des comptes |
| GO-β2 (hors crédits) | **même course, part hors crédits** : Argon proposeur (2 USD par session) et vérificateur (0,10 par test) 35, Astra proposeur 12 (identifiant et prix confirmés avant l'appel), machine jetable à `bwrap` 10, validée par l'essai à blanc au vrai bac avant tout appel payant | 57 USD [34 ; 80] | 2026-11-30 |

Variantes : Kimi cinquième proposeur → GO-β1 420 [210 ; 630], ligne Kimi 9 [5 ; 14], GO-β2 60 ; fausses testées (Q-12 (b)) →
GO-β1 445 ; Kimi expérimentateur (Q-2 (b)) → GO-β1 30, ligne Kimi 216. **Plafond de travail** (Q-12 (c)) : borne par test d'Opus
ramenée à 0,80 → GO-β1 ≈ 210 à 2 × 3 (formule : 6 × (5 + 37 × 0,80)), au prix de tests coupés plus souvent.

## 7. Questions ouvertes pour Lazar

Format : décision ; enjeu ; options (avantage, inconvénient) ; recommandation et confiance. Aucune n'a de défaut sous
48 heures dans cette conception : ce sont des nœuds (dépense, modèle, revendication) que seul ton mot tranche.

**Q-1 — Nombre de mondes (et de générations).**
- *Enjeu* : la sensibilité aux effets faibles se mesure par graines (C8 avant, rejeux après, sans dépense) et par mondes (une
  course entière par monde) ; **deux mondes ne donnent aucune estimation de dispersion** (un degré de liberté, S-5).
- *Options* : **(a) 1 × 3** — avantage : ≈ 21 USD attendus, 205 au pire ; inconvénient : un monde « facile » ou « dur » décide de
  tout. **(b) 2 × 3** — avantage : réplication ; l'issue se lit **par monde**, et le préenregistrement écrit la règle si les deux
  divergent (issue « non répliquée », sans lecture commune) ; inconvénient : ≈ 41 USD attendus, 409 au pire, toujours aucune
  dispersion estimée. **(c) 3 × 3** — avantage : une première estimation grossière de dispersion ; inconvénient : ≈ 62 attendus,
  614 au pire.
- *Recommandation* : **(b) 2 × 3**, confiance ≈ 0,5. En simulation v2, la génération 3 est vide avec des proposeurs synthétiques généreux (`generations-w12-g3-n400-v2.json`) ; avec de vrais proposeurs, plus lents, elle peut avoir à trouver : 3 générations restent le minimum qui laisse voir un progrès après la génération 1.

**Q-2 — Expérimentateur des tests de mort.**
- *Enjeu* : depuis R-2461, aucune famille n'est exclue du fait de l'auteur du monde ; l'expérimentateur voit la tranche et la loi
  gelée, le verdict est calculé par l'orchestrateur sur le fichier brut, avec contre-calcul ; le choix pèse sur le coût et sur
  la disponibilité.
- *Options* : **(a) Opus 5.5** (crédits de Claude), vérificateur Argon — avantage : crédits qui expirent, compte disponible ;
  inconvénient : jamais éprouvé dans ce rôle en course réelle (≈ 0,20 USD attendus par test, estimé) ; sa **borne de 1,50 USD par
  test est elle-même un plafond** : un test qu'elle coupe est « non concluant » et élimine son groupe (V-6). **(b) Kimi** — avantage :
  le moins cher (≈ 0,10 par test, devis v66), éprouvé en v67 (28 appels, 14 tests) ; inconvénient : compte suspendu, à recharger.
  **(c) Argon**, vérificateur Opus — avantage : disponible ; inconvénient : ≈ 0,42 USD par test (estimé), cinq fois Kimi.
- *Recommandation* : **(a)**, confiance ≈ 0,6 ; (b) si le compte de Kimi est rechargé avant le préenregistrement.

**Q-3 — Origine du secret qui tire les mondes de test, et ordre des engagements.**
- *Enjeu* : « lois inconnues de toute famille » est une garantie de procédure (E-12) ; qui tire le secret, et dans quel ordre,
  décide qui pourrait fixer les mondes.
- *Options* : **(a) machine seule** — avantage : rien à faire de ta part ; inconvénient : une session Claude fixe seule le secret.
  **(b) ta phrase seule** — avantage : aucune session ne la connaît ; inconvénient : secret humain moins uniforme. **(c) les
  deux, dans cet ordre** : secret machine tiré, son empreinte inscrite **et poussée**, puis ta phrase, son empreinte inscrite —
  avantage : ni la session ni toi seul ne fixez les mondes, et un secret ne peut pas être retiré après un regard ;
  inconvénient : deux étapes.
- *Recommandation* : **(c)**, confiance ≈ 0,65.

**Q-4 — Nul du juge pour la course : v8 ou v9.**
- *Enjeu* : dans un monde riche à structure par morceaux, les proposeurs écriront des `si_sinon` ; les recombinaisons par
  morceaux de lois d'archive sont hors de la classe couverte du nul v8 (brèche d'A1-v3) ; le nul v9 les couvre mais sa
  validation a rendu « puissance perdue » (audit `9086a420…`).
- *Options* : **(a) nul v8** (comme la v67) avec l'oracle d'enveloppe et le classement des fausses découvertes par forme —
  avantage : code et validation existants, puissance connue ; inconvénient : la classe non couverte reste une portée.
  **(b) nul v9** — avantage : ferme la recombinaison par morceaux ; inconvénient : perte de puissance mesurée, code à brancher,
  et une vraie découverte par morceaux peut être refusée.
- *Recommandation* : **(a)**, confiance ≈ 0,6 ; la sonde hors classe H1 mesure le trou dans ce monde.

**Q-5 — Tirages frais par carte : une valeur ou une règle.**
- *Enjeu* : la contre-lecture (E-3) établit que le juge simplifié n'est calé qu'en un point (2 traits, 200 tirages, archive
  d'une loi) ; n ne peut pas être gelé sur lui. Le juge simplifié **indique** n ≈ 400 (famille tirée : à n = 400, 0,72 de promotion à 0,02-0,03 nat au-delà de l'archive et 0,36 à 0,01-0,02 ; à n = 200, 0,23 et 0,04 ; `detection-w12-r40-v2.json`).
- *Options* : **(a) n = 200** (v67) — avantage : rien à refaire ; inconvénient : effets faibles presque invisibles. **(b) n fixé
  maintenant à 400** — avantage : simple ; inconvénient : gelé sur un juge non calé. **(c) une règle écrite d'avance**,
  appliquée au banc de calibration avec le code v68 gelé : « le plus petit n de la grille {200, 300, 400, 600, 800} tel que la
  puissance médiane, sur les mondes de calibration, d'un effet à 0,025-0,03 nat au-delà d'une archive de 8 lois soit ≥ 0,5, et
  que la part des promotions de lois à moins de 0,01 nat au-delà de l'archive reste ≤ 0,25 » ; si aucun n ne tient les deux,
  **n = 400 et le banc le rapporte** — avantage : n fixé sur le vrai juge, sans regard sur la course ; inconvénient : le banc doit
  tourner avant le préenregistrement final.
- *Recommandation* : **(c)**, confiance ≈ 0,65.

**Q-6 — Mondes refusés par le vérificateur : retirage automatique ou arrêt.**
- *Enjeu* : un tirage peut tomber hors des exigences (classes, détectabilité C8) ; retirer, c'est choisir des mondes
  « conformes » (biais voulu, à dire) ; arrêter, c'est un délai.
- *Options* : **(a) retirage automatique**, au plus 8 tirages par monde, nombre de refus et contrôles en cause rapportés —
  avantage : aucun délai ; inconvénient : sélection des mondes par le vérificateur (dite au rapport). **(b) un seul tirage**,
  refus = arrêt et nouvelle graine sur ton mot — avantage : aucune sélection cachée ; inconvénient : délai.
- *Recommandation* : **(a)**, confiance ≈ 0,7 (banc v1 : 1 tirage refusé pour 12 mondes ; banc v2 : 5 refusés pour 8 mondes, C0, C5 et C6, `banc-generateur-v2-resume.json`).

**Q-7 — Version de Fable, présence d'Astra et de Kimi.**
- *Enjeu* : coût et diversité des proposeurs ; changer de modèle demande ton GO ; Kimi redevient possible (R-2461) ; chaque
  proposeur ajoute jusqu'à 6 représentants à tester par génération (E-9 (c)).
- *Options* : **(a) Fable 5.2 et Astra** (quatre proposeurs) — avantage : quatre familles ; inconvénient : identifiant et prix
  d'Astra à confirmer. **(b) (a) plus Kimi** — avantage : une famille de plus (≈ 0,36 USD attendus par appel) ; inconvénient :
  compte à recharger, **+ 54 USD au pire sur crédits** à 2 × 3 (ses représentants testés par Opus) et + 9 sur la ligne Kimi.
  **(c) sans Astra** — avantage : moins de pièces ; inconvénient : moins de diversité.
- *Recommandation* : **(a)**, confiance ≈ 0,6 ; (b) si le compte de Kimi est rechargé et le plafond accepté, confiance ≈ 0,5.
  La composition reste jugée sur l'oracle et le coût (N-058).

**Q-8 — Regroupement avant le juge ou après le test de mort ; ordre des étapes.**
- *Enjeu* : ton mot R-2443 est « il faut regrouper les doublons au sein d'une même génération » (E-10 : la v1 t'attribuait à
  tort des mots de la consigne de la mère). Les deux moments y répondent. La synthèse du collisionneur (non contre-lue) préfère
  « après le test de mort » à confiance 0,55 et place un pilote A/A et un duel avant la course.
- *Options* : **(a) avant le juge**, course directe après le banc de calibration — avantage : les copies ne se portent plus
  l'une l'autre dans e-BH (15,4 retenues par carte contre 7,3 par groupe, v1) ; moins de tests payés ; inconvénient : touche au
  juge (code v68 et preuve à contre-lire, hypothèses du §3.3). **(b) après le test de mort** (temps 1 de la synthèse) — avantage :
  juge v67 intact, preuve inchangée ; inconvénient : les copies passent ensemble e-BH, plus de tests payés. **(c) (a) précédé du
  pilote A/A et du duel** — avantage : sépare « le monde n'offre pas » de « les proposeurs ne prennent pas » ; inconvénient :
  une étape payante de plus.
- *Recommandation* : **(a)**, confiance ≈ 0,55.

**Q-9 — Ce qu'est une « vraie découverte », et la tolérance des fausses découvertes au sens de l'oracle.**
- *Enjeu* : la garantie du juge ne borne pas la part des retenues sous g₀ (E-8 (c)) ; en simulation v2, 12 à 19 % des retenues sont à moins de g₀ au-delà de l'enveloppe (`generations-w12-g3-n400-v2.json`) ; cela touche la
  revendication O2 (N-064).
- *Options* : **(a) vraie = au-dessus de g₀ au sens v60 et de l'enveloppe ; tolérance fixée au banc** (part attendue des fausses
  découvertes mesurée sur les mondes de calibration, plus une marge écrite, comme critère de lecture) — avantage : honnête sur
  ce que fait le juge ; inconvénient : la tolérance n'est pas α. **(b) marge sur le juge** (règle « delta0 » de
  `selection_pari.evaluer`, 2·δ₀ = g₀) — avantage : juge et oracle réaccordés ; inconvénient : changement de règle du juge,
  puissance perdue près du seuil, à valider. **(c) aucune tolérance : rapport seul** — avantage : rien à fixer ;
  inconvénient : aucune issue ne dépend de la vérité des découvertes.
- *Recommandation* : **(a)**, confiance ≈ 0,6.

**Q-10 — Publication du générateur ; garde du secret et des mondes.**
- *Enjeu* : le générateur v68 vivra dans l'arbre de l'organisme, dont le dépôt est public ; la famille qu'il tire serait alors
  lisible de tous (pas les mondes : ils dépendent du secret).
- *Options* : **(a) générateur publié avec le code de la course** (comme tout le code gelé), secret et mondes hors de tout
  dépôt jusqu'au verdict, secret révélé après — avantage : vérifiable par tous ; inconvénient : la famille est publique (elle l'est
  déjà par la grammaire et ce document). **(b) générateur privé jusqu'au verdict** — avantage : la famille n'est pas lisible
  avant ; inconvénient : le code gelé de la course n'est plus entièrement public, contre-lecture sur un dépôt privé. **(c)
  publication des mondes après le verdict** en plus de (a) — avantage : rejouable par tous ; inconvénient : ces mondes ne
  pourront plus servir de mondes de test.
- *Recommandation* : **(a)**, mondes publiés seulement sur ton mot après le verdict ; confiance ≈ 0,6.

**Q-11 — Sens de « plusieurs traits cachés » (R-2443).**
- *Enjeu* : la v1 l'a lu « traits qui comptent, inconnus des proposeurs, parmi des leurres » ; il peut aussi vouloir dire
  « traits **non observés** » ; le générateur n'en met qu'au plus un (trait latent, un monde sur trois environ). **Ce que la
  conception établit** (V-7) : une loi prédictive ne « capte » presque jamais une composante latente (4 sur 23, §4.1), et la
  mesure principale D2 l'exclut ; un latent ajoute donc une composante qu'aucun proposeur ne peut trouver et qu'aucune mesure
  principale ne compte, et il abaisse le gain du monde.
- *Options* : **(a) lecture actuelle** (traits observés dont l'effet est caché, leurres, latent possible) — avantage : rien à
  changer, chaque composante comptée est trouvable ; inconvénient : peut-être pas ton intention. **(b) au moins un trait non
  observé par monde, jusqu'à deux** — avantage : du bruit irréductible, plus proche de données réelles ; inconvénient : une ou deux
  composantes **introuvables et non comptées** par monde, gain du monde plus bas, puissance aux faibles réduite (à mesurer au
  banc). **(c) les deux** : latent obligatoire, plus les leurres — avantage : les deux lectures servies ; inconvénient : celui de
  (b), sur chaque monde.
- *Recommandation* : **(a)**, confiance ≈ 0,5 (la v2 recommandait (c) sans dire ce coût) : les traits observés à effet caché et
  les leurres répondent à « plusieurs traits cachés » sans ajouter de composante que personne ne peut trouver ; (c) si ton mot
  visait les traits non observés.

**Q-12 — Tester les fausses lois promues ; politique de plafond.**
- *Enjeu* : la v66 testait toute loi plantée promue ; la v1 de cette conception proposait de ne pas tester les fausses et copies
  promues (la brèche se lit à la promotion), sans le dire comme une décision (E-9 (e)). Le plafond au vrai pire cas est élevé.
  **Deux plafonds** sont en jeu (V-6) : celui de la course (une ligne de GO sous le pire cas ferait d'un dépassement un arrêt
  « non jugeable ») et **la borne par test de l'expérimentateur** (1,50 USD pour Opus), qui produit des tests « non concluants » ;
  Opus n'a jamais tenu ce rôle, et on ne sait pas combien de tests cette borne coupera.
- *Options* : **(a) ne pas les tester, plafond de course au pire cas** (GO-β1 365) — avantage : la brèche reste lue à la
  promotion ; aucun arrêt par plafond de course ; inconvénient : aucun test de mort sur une fausse promue ; des tests coupés par la
  borne restent possibles. **(b) les tester** (comme la v66 ; T_pire = 46, F5 compris, H1 non testée) — avantage : dessin de la
  v66 inchangé ; inconvénient : **GO-β1 445**, total ≈ 496. **(c) (a) avec un plafond de travail** (borne par test d'Opus à 0,80,
  GO-β1 ≈ 210) — avantage : engagement plus bas ; inconvénient : plus de tests « non concluants », que la lecture doit compter à
  part.
- *Recommandation* : **(a)**, confiance ≈ 0,5. Ta règle « pas de non concluant par défaut de plafond » (devis v66 §5) protège
  ici l'issue de la course, **pas chaque test** : la lecture compte à part les tests coupés par la borne, et une part élevée de
  tests coupés en génération 1 est une raison d'arrêter et de revoir la borne (règle à écrire au préenregistrement).

## 8. Limites et réserves de cette conception

- **Juge simplifié** : modèle du nul v8 écrit d'après la copie v52b, étalonné sur la v67 (V3 595 contre 617, V4 489 contre 501 sur 1 000) ; l'urne écartée par
  inférence ; tout chiffre de puissance est à refaire avec le code gelé dans le préenregistrement.
- **Proposeurs synthétiques** (`generations`) : modèle arbitraire (probabilités de trouver un effet 0,5 / 0,25 / 0,1 selon sa
  classe, 0,9 de garder un effet connu) ; ses chiffres disent l'effet relatif du regroupement et l'ordre de grandeur de la
  dispersion entre mondes, pas ce que feront Claude, Argon et Astra.
- **Générateur écrit par un modèle de la famille Claude** (moi) ; les lois sont tirées d'un secret après le scellement, et le
  générateur v68 sera contre-lu par un autre modèle ; la famille (sortes d'effets, classes) est publique par la grammaire
  servie et par ce document ; régularités classées au §2.1 (E-6).
- **Garantie de procédure, non cryptographique** (E-12) : elle tient tant que les règles du §2.5 sont tenues.
- **v3** : le représentant, les doublons et la condition « regroupement » des générations sont refaits avec la tranche de choix
  appariée, par parties scellées, un processus à la fois ; la partie « générations » du script v3 avait une récursion infinie (12
  parties en échec, résumé vide scellé et gardé : `generations-a2-v3-resume.json`) ; corrigée sous un nom neuf
  (`puissance_monde_riche_v3b.py`). Vérification courte de la v2 faite par le même modèle que moi : réserve de lignée.
- **Simulations v2** : famille tirée, règle du représentant v2, parcours déterministes ; toujours le juge simplifié et des
  proposeurs synthétiques ; les simulations v1 restent versées, marquées « sous-famille » (E-4) ; la génération 2 et 3 de la v1
  n'étaient pas rejouables (E-2) et ne sont plus citées comme preuve.
- **Interruption** : le conteneur a redémarré vers 23:25 UTC pendant les sorties v2 ; les sorties finies avant (essais, devis,
  représentant) sont gardées ; la simulation des doublons, coupée sans sortie, a été relancée sous le même nom (rien n'était
  scellé) ; les suivantes ont été lancées une à une (`sorties-v2/journal-sorties-v2-reprise.txt`).
- **Code gelé non lu** : les points « à vérifier » du §1.3 (constantes `DIM`, `TIRAGES`, instants de lecture, bibliothèque du
  juge) restent des inférences.
- Rien ici n'est une prédiction de préenregistrement : le préenregistrement neuf fixera critères, seuils et portée (R1), et sera
  contre-lu (R2).

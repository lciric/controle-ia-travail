# Devis du banc de 24 mondes de calibration MR-2 (suite de l'issue P-2 du pilote) — v2

- **Statut** : devis, **sans lancement** (mot de Lazar R-3015 : « Le devis du banc de calibration est à préparer, sans
  lancement. : go »). Aucune dépense, aucune machine louée, aucun appel au loueur ni à un fournisseur de modèles, aucun commit.
  Ce texte ne change ni le texte scellé du pilote, ni la conception v4, ni le programme ; il ne demande aucune ligne de GO
  inscrite : il en **propose** une (section 8).
- **Rédacteur** : modèle A, rédacteur neuf (je n'ai écrit ni le texte du pilote, ni son code, ni la conception v4, ni le verdict).
- **Heures** (`date -u`) : début 2026-11-16 20:44:10Z ; fin : dernière ligne.
- **Version v2** : corrections de la contre-lecture du tour 1 appliquées (section 11) ; scellée le 2026-11-16T20:58:19Z (`date -u`).
  La v1 (`6172ae59…`) reste intacte.

## 0. Verdict en trois lignes

1. **Le banc n'appelle aucun modèle** : c'est une simulation sur processeur (proposeurs synthétiques de la conception v4) ;
   part sur crédits de Claude **0 USD** attendu et au pire ; seule dépense possible : la machine qui garde le secret de calibration.
2. **Devis, lieu recommandé (machine jetable louée)** : attendu **≈ 0,30 USD**, pire **3,00 USD**, tout **hors crédits** (la
   location ne se paie pas sur crédits de Claude) ; durée attendue ≈ 5 h, pire ≈ 13 h, sous une minuterie de 17 h.
3. **Avant tout lancement** il manque : un préenregistrement du banc (ou addendum), un lanceur du banc neuf (le code gelé porte
   `P_CACHEE = 0.02` et des graines de développement en dur), un secret de calibration neuf avec la phrase de Lazar, une procédure
   machine dérivée de la v14, une ligne « calcul » de 3 USD ; et deux décisions de Lazar (section 9).

## 1. Pièces lues (chemin, empreinte)

| pièce | où | empreinte sha256 |
|---|---|---|
| verdict de l'issue P-2 (second lecteur, v2) | `pilote-v1/lecture-issue-pilote-v14-mere/verdict-issue-v2/verdict-issue-pilote-mr2-v14-v2.md`, branche `verdict/pilote-mr2-v74-v14-v1` (`61230010`), par `git show` | `e64458e8…` au registre (GO-2026-11-16-08) ; non recalculée ici |
| texte scellé du pilote, candidat 6 | `pilote-v1/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md`, branche `prep/pilote-mr2-compte-organisme-v1` (tête `5432ac56`) | `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` (recalculée, égale au compagnon) |
| procédure machine v14 | `pilote-v1/procedure-pilote-v74-compte-organisme/procedure-pilote-mr2-v74-machine-v14.md`, commit `2d35cafa` de `lot/compte-organisme-v1` | `2035562740efe1e87db9ffa2f0494705bb5117c56069309ece2279d351bde18a` (recalculée, égale au compagnon) |
| pièce de dépense du pilote | `pilote-v1/lecture-depense-pilote-v14-compte-organisme/depense-pilote-v14-v1.json`, commit `2f7acc1d` | `53c72308bb30adcce5602ad18b47f2e7325a22a295264c143ed52ff46f349ce2` (recalculée, égale au compagnon) |
| conception v4 (famille MR-2, règle de garde) | `conception-monde-riche-doublons-v4.md` (`main`) | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` (recalculée) |
| code de la règle et de la simulation | `outils-v4/monde_riche_v4.py` (`main`) ; même fichier que `orchestrator/mr2_v68/outils-v4/monde_riche_v4.py` du bloc gelé du pilote | `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8` (recalculée ; égale à la ligne du bloc gelé) |
| journal des 12 parties de la conception v4 | `sorties-v4/journal-sorties-v4.txt` et `sorties-v4/partie-v4-monde-*.json` (heures seules) | compagnons |
| brouillon 3 du préenregistrement de la course (non scellé) | `preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon3.md`, §16.1 | `2dda3b74ff5e13d56a8f0818623b0b64730a3b3da5f86a136df321343f653a39` (recalculée) |
| lignes GO-2026-11-13-01, -13-02, -14-13, -14-14, -16-08 | `registres/go.md` (`main`, `55e7a4ee`), l. 314, 315, 332, 333, 349 | registre vivant |

Chemins relatifs à `docs/notes/organisme-multi-generations-v1/` sauf mention. Rien d'autre de la sortie du pilote n'a été ouvert ;
aucune branche `calcul/pilote-mr2-v74-entree-*`.

## 2. Ce que le banc joue

**Ce qui suit P-2, mot pour mot (verdict et table gelée)** : « banc de 24 mondes de calibration (code v68 gelé) : P_CACHÉE := p_c
ponctuel, P_VUE := 0,25 supposée ; la règle de garde de la conception v4 y décide de la course ; le banc rapporte aussi la règle
aux deux bornes de l'intervalle (mesure, ne décide pas) ». Champ `regle` : `P_CACHEE_banc = 0,0`, `P_VUE_banc = 0,25`.

- **Mondes** : 24 mondes MR-2 (Q-15 (b), R-2501), tirés par `generer_v4` et vérifiés C0 à C8 v4 (au plus 8 tirages par monde, toute
  conditionnelle certifiée), d'un **secret de calibration neuf**, distinct du secret du pilote (ses quatre mondes ne sont jamais
  réutilisés) et du secret de test de la course. Ils ne sortent jamais de la machine ; seules leurs empreintes vont au registre.
- **Proposeurs** : **aucun vrai proposeur**. Le texte scellé le dit : « le banc ne mesure rien sur les proposeurs ». Le banc joue
  le **modèle de proposeurs synthétiques** de la conception v4 (§3.2, gelé dans `monde_riche_v4.py`) : 4 proposeurs × 6 cartes,
  archive de départ {K1}, garder un effet connu 0,9, proposer une composante inconnue (forte 0,5, moyenne 0,25, latente 0,25,
  faible 0,1), bruit σ = 0,15 ; une conditionnelle est proposée à **P_VUE** si sa composante de condition est connue, à
  **P_CACHÉE** sinon.
- **Appels** : **zéro appel de modèle**, zéro jeton, aucun gabarit servi à un modèle. Le gabarit du pilote (`e77d3041…`) n'entre pas
  au banc : il ne sert que dans la course (« p_c ne vaut que pour ce gabarit, le même au banc et dans la course » ; au banc, p_c
  n'est qu'un nombre).
- **Valeurs** : P_CACHÉE = **0** (p_c ponctuel, x = 0 sur n = 14) : **décide** ; aux deux bornes de l'intervalle [0 ; 0,043] :
  la borne basse **égale le ponctuel** (0), donc une seule passe de plus, à la borne haute **0,0430** (recalcul : Clopper-Pearson
  supérieur 0/14 = 0,23164, transformé 1 − (1 − 0,23164)^(1/6) = 0,042965 ; la valeur exacte se recopie du champ de la sortie de
  mesure scellée par qui a le droit de la lire, jamais de mon arrondi). P_VUE = 0,25 partout, « supposée, non mesurée ». La
  variante « sans masquage » (0,25 toujours) se rapporte comme en v4 (mesure, ne décide pas).
- **Règle de garde** (R-2492, conception v4 §3.1, recopiée) : « Pas de course si moins de la moitié des mondes de calibration gardent
  une composante certifiée encore trouvable après une génération 1 simulée. » Au banc : au moins ⌈24/2⌉ = **12 mondes sur 24**.
  Dénominateur à fixer au préenregistrement : la v4 propose « un monde sans tirage conforme en 8 compte comme ne gardant rien »
  (tous les mondes tirés) ; le code v4 compte sur les conformes (section 9, Q-B3).
- **Code** : `monde_riche_v4.py` (`4b165847…`) et ses modules (outils v1 à v3), **inchangés**, tels que gelés dans l'arbre v68 à v74 du
  pilote (13 lignes `orchestrator/mr2_v68/…` du bloc gelé, dont `mesure_pilote_v4.py` et `seuil_pilote_v1.py`, qui n'entrent pas au banc) ; numpy **2.5.3** exigé (bloc gelé ; la simulation dépend du générateur
  de numpy). Le code gelé ne peut pas jouer le banc tel quel (section 6, point 2) : un **lanceur neuf** l'importe sans le modifier.
- **Configuration** : aucune configuration de proposeurs ; aucune clé de fournisseur de modèles sur la machine (seul le jeton qui
  pousse les sorties). Un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`, comme la v4.

## 3. Ce que le pilote a mesuré, et ce que le devis en fait

| proposeur | coût par appel (USD ; pièce de dépense et verdict) | durée par appel (s ; verdict) | troncatures |
|---|---|---|---|
| `fable52` | 2,504888 en moyenne ; complets 2,216780 en moyenne (4,433560 pour les deux, par différence) ; tronqués 2,792996 en moyenne (5,585992 pour les deux) | 388,8 à 553,2 (moyenne 470,6) | **2 sur 4** (mondes 3 et 4, borne de 64 000 jetons ; réponses illisibles, aucune carte) |
| `opus55` | 0,264334 | 36,4 à 109,4 (68,4) | 0 |
| `argon` | 0,617905 | 38,3 à 96,0 (64,4) | 0 |
| `astra` | 0,417938 | 34,4 à 80,1 (63,6) | 0 |
| machine | 0,082018 pour 1,5706 h à **0,052222 USD/h** | 11:26:57Z → 13:01:11Z | — |

Total du pilote : 15,378197 USD (π1 11,076888 ; π2 4,301309) ; « la console fait foi » (R-2803).

**Usage au banc** : le banc n'appelle aucun proposeur ; **ni le coût, ni la durée, ni les troncatures par appel n'entrent dans
son devis**. Du pilote, le banc ne prend que **p_c = 0** et l'intervalle **[0 ; 0,043]**, et du devis de la machine le **prix horaire
réel** (0,052222 USD/h, offre à carte inutilisée, R-2947) et les bornes de l'offre de la procédure v14 (au plus 0,15 USD/h, relu au
plus 0,17). Les mesures par appel servent à d'autres devis : celui de la course et ceux des cribles (GO-2026-11-16-08). Pour la course
(information, sans devis) : `fable52` coupé une fois sur deux à 64 000 jetons, et payé presque au plafond de session (2,79 sur 3 USD)
quand il l'est ; ≈ 8 min par appel, ce qui fixe le temps d'une génération.

## 4. Durée et lieu

**Pièce de durée** : les 12 parties de la conception v4 (même code, même interpréteur, numpy 2.5.3, un processus) ont pris de
**3 min 40 s à 8 min 55 s** par monde, **6 min 17 s** en moyenne (08:02:15Z → 09:17:45Z), retirages compris (mondes 4 et 11 : 3 refus
chacun). Chaque partie faisait : tirage et vérification (C8 à 200 graines), part marginale, course de 3 générations avec masquage,
1 génération sans masquage.

**Ce que le banc ajoute par monde** : une course de plus à la borne haute (0,0430). Estimé : × 1,5 en attendu ; × 2 au pire (si la
course domine la partie), puis × 1,5 pour une machine louée plus lente que ce conteneur.

| poste | attendu | pire |
|---|---|---|
| 24 mondes, un processus à la fois | 24 × 9,5 min ≈ 3,8 h | 24 × 26,7 min ≈ 10,7 h |
| mise en place (numpy, arbre, empreintes) | 0,3 h | 0,5 h |
| barrière de la phrase de Lazar | 0,3 h | 1 h (au-delà : arrêt de la machine) |
| rapatriement, destruction, preuve d'absence | 0,3 h | 0,5 h |
| **total** | **≈ 5 h** | **≈ 12,7 h** |

**Lieu recommandé** : une **machine jetable louée** chez le loueur du pilote (au moins 4 processeurs, 8 Go, 20 Go de disque, au plus
0,15 USD/h, avec ou sans carte graphique, la carte inutilisée), sans ssh, sur le modèle de la procédure v14 : amorce qui **arme la
minuterie avant toute passe**, sorties poussées sur une branche neuve `calcul/…`, feux de la mère sur une branche d'entrée,
**minuterie de 17 h** (17 × 0,17 = 2,89 USD, sous la part de 3 USD), destruction par identifiant (R10), absence prouvée. Raison : le
secret de calibration se tire « par la même procédure que le secret de test » (brouillon 3, §16.1 point 4 ; conception v3 §2.5) :
tiré sur une machine privée, engagé et poussé, puis la phrase de Lazar ; les mondes meurent avec la machine. Autres lieux à la
section 9 (Q-B1).

## 5. Devis : attendu et pire, crédits et hors crédits séparés

Tout est **estimé** sauf les plafonds. Consigne permanente de Lazar : crédits de Claude au maximum. **Rien ne peut aller sur crédits** :
le banc n'appelle aucun modèle, et la machine se paie chez le loueur.

| poste (USD) | sur crédits de Claude : attendu | sur crédits : pire | hors crédits : attendu | hors crédits : pire |
|---|---|---|---|---|
| proposeurs (`fable52`, `opus55`, `argon`, `astra`) | 0 | 0 (aucune clé sur la machine) | 0 | 0 |
| juge, expérimentateur, vérificateur | 0 | 0 | 0 | 0 |
| machine (lieu recommandé) | — | — | **0,30** (≈ 5 h à 0,052 USD/h = 0,26, arrondi au-dessus ; à 0,15 USD/h, plafond de l'offre, 5 h coûteraient 0,75) | **3,00** (part, minuterie 17 h au plus 0,17 USD/h : 2,89) |
| réseau du loueur (prix consignés par l'outil) | — | — | quelques millièmes | compris dans la part |
| **total** | **0** | **0** | **≈ 0,30** | **3,00** |

**Plafonds par proposeur** : 0 USD pour chacun ; la machine ne reçoit aucune clé de fournisseur de modèles, et le lanceur refuse de
démarrer si une variable de clé est présente (garde à écrire, R5). **Coupure** : (i) minuterie de destruction armée par l'amorce
avant toute passe ; (ii) prix relu à la création au plus 0,17 USD/h, sinon destruction aussitôt ; (iii) arrêt de la machine si la
phrase ne vient pas dans l'heure ; (iv) une seule création, aucune seconde machine tant que l'absence de la première n'est pas
prouvée ; (v) aucune ligne d'extension.

## 6. Ce qu'il faut écrire avant tout lancement

1. **Préenregistrement du banc** (R1 : le banc décide de la course, simulation comprise), scellé, contre-lu par un sous-agent neuf
   (R2), vérifié : hypothèse (la règle tient à P_CACHÉE = p_c) ; prédiction chiffrée et signe, sans signe visé (R3) ; métrique
   (mondes gardant une certifiée non captée après la génération 1) ; seuil (12 sur 24) ; dénominateur (Q-B3) ; valeurs exactes de
   P_CACHÉE (0), de la borne haute (recopiée de la sortie de mesure scellée) et de P_VUE (0,25, supposée) ; variante sans masquage
   rapportée ; **audit R4 écrit d'avance**, déclenché si 24 sur 24 (voir section 7, point 4) comme sous 12 ; liste d'arrêt
   (empreinte d'un module, nombre de parties différent de 24, exception ; un monde sans tirage conforme en 8 n'arrête pas le banc : il est compté selon Q-B3 et rapporté) ; ce qui suit un échec (« pas de
   course ; aucun nouveau tirage de mondes de calibration, aucun réglage du modèle sur ces mondes », v4 §3.2). Forme : texte neuf, ou
   **addendum** au texte du pilote si la mère le juge suffisant — le texte scellé fixe déjà les valeurs et la règle ; le reste (secret,
   dénominateur, lanceur, audit) n'y est pas.
2. **Lanceur du banc v1** (nom neuf, R12), contre-lu par un autre modèle que son développeur, essais R5 et banc de mutations : il
   **importe** `monde_riche_v4.py` sans le modifier (empreintes exigées contre les compagnons) ; il fixe P_CACHÉE par l'attribut du
   module (la fonction `course` lit `P_CACHEE` à chaque appel ; le fichier reste à `4b165847…`) ; il ne peut pas appeler `partie`
   tel quel, qui tire les mondes de la clé publique `monde-mr1-v4-calibration-developpement` : il en reprend les pas avec la clé
   dérivée du secret de calibration et de la phrase (forme de `graine_monde_pilote`) ; il dit d'avance si l'indice `w` des flux de
   simulation (`oracle-v4`, `v4-gen`, `v4-juge`, `v4-mort`) reste le rang du monde ou devient secret ; il écrit un manifeste par run
   (R9 : SeedSequence, versions, commit, empreintes) ; il ne sort que des empreintes et des comptes, jamais un monde ; il refuse un
   second lancement. Note : `course` tire `rng.random()` pour chaque composante, quelle que soit sa probabilité ; les passes à 0 et à
   0,0430 consomment donc le même flux en génération 1 (les connus y sont {K1} dans les deux passes) et se comparent monde par monde pour la règle, qui se lit après la génération 1 ; leurs flux divergent dès la génération 2.
3. **Secret de calibration** neuf : tiré sur la machine, empreinte inscrite sur `main` et poussée **avant** la phrase de Lazar, tapée
   par lui dans la session qui lance ; barrière des mondes (empreintes au registre) avant la simulation.
4. **Procédure machine du banc v1** dérivée de la v14 (amorce, programme machine, outil de session, essais à blanc sur dossier
   jetable), sans clé de fournisseur de modèles, vérifiée « jouable » par un lecteur neuf ; crochet `garde_calcul.py` éprouvé (cas
   sain et artefact) ; `GO_ID=` de la ligne du banc en tête de la commande de création.
5. **Ligne « calcul »** inscrite sur le mot de Lazar (section 8).
6. **Lecture** : issue lue par un sous-agent neuf qui n'a écrit ni le préenregistrement du banc, ni le lanceur, ni la conception v4
   (R13, comme E-11 (iii) : elle commande une course de 422 USD de plafonds), puis GO de Lazar.

## 7. Risques

1. **Troncatures** : aucune au banc (aucun appel). Celles de `fable52` (2 sur 4) pèsent sur la course, pas ici.
2. **Temps** : 5 h attendues, 13 h au pire ; le banc doit finir, être lu et accepté avant la course, et les lignes de la course
   échoient le **30 novembre** (GO-2026-11-13-01 et -02). La barrière de la phrase a déjà fait perdre une tentative du pilote
   (v13, R-2962) : le mot « présent pour la demi-heure » de Lazar (condition de la v14) est à garder.
3. **Plafonds de session** : la session qui lance peut s'arrêter (crédits, fin d'autonomie) pendant 5 à 13 h ; les sorties étant
   poussées par la machine et la minuterie détruisant la machine d'elle-même, une session neuve reprend par la branche de sortie ;
   la destruction et la preuve d'absence restent dues par identifiant (R10).
4. **Résultat écrit d'avance trop propre (R4)** : à P_CACHÉE = 0, le modèle ne propose **aucune** conditionnelle en génération 1 dès
   que sa condition n'est pas l'effet de K1 (sa condition est une moyenne, K1 est l'effet principal le plus informatif ; le
   programme du pilote refusait ce cas, le générateur v4 ne le refuse pas : à vérifier dans le lanceur), car `connus` ne change
   qu'après la génération ; si tout monde conforme porte une conditionnelle certifiée, la règle tient **presque par construction**,
   à des captures par attribution près (lecture du code, non mesurée). Le banc à p_c dit
   donc surtout que le générateur tient sur 24 mondes neufs et comment le dénominateur compte ; l'information sur le risque est à la
   borne haute et dans les taux d'erreur du pilote (permise à tort 0,27 si p vaut 0,051, à 14 appels) ; le modèle approché du texte scellé place la bascule de la règle à 0,034 (probabilité 0,5) et à 0,051 (probabilité 0,05) : la passe à 0,0430 n'est pas acquise d'avance, et le préenregistrement y écrit sa prédiction chiffrée (R1) et ce que devient un résultat sous 12 sur 24 à cette borne (information rapportée, ne décide pas). Le préenregistrement doit
   l'écrire et déclencher l'audit sur 24 sur 24.
5. **Refus du générateur** : 12 refus pour 12 mondes en v4 (C6 surtout, cause non établie) ; 24 mondes peuvent en demander 24 ou plus,
   sous la borne de 8 par monde ; un monde sans tirage conforme pèse selon Q-B3. Probabilité qu'au moins un des 24 mondes n'en ait aucun : ≈ 9 % au taux de refus observé en v4 (12 refus pour 12 mondes, 0,5 par tirage, indépendance supposée), ≈ 33 % à 0,6 ; l'événement est donc à prévoir, non exceptionnel, et le préenregistrement le traite par Q-B3, sans arrêt.
6. **Machine** : aucune offre à processeurs seuls au 16 novembre (R-2947) ; mémoire bornée à 6 Go par processus ; numpy 2.5.3 à
   installer (900 s au plus dans la v14).
7. **Lecture de « code v68 gelé »** : je le lis comme l'arbre v68 à v74 du pilote, dont `monde_riche_v4.py` porte la règle. Le
   brouillon 3 de la course (non scellé) décrit un banc plus large, sur un code v68 de la course (juge v68, n, forme, attribution,
   fusion, τ, surdité), dont la règle de garde est la **dernière** étape (ordre D-2) ; je n'ai pas vérifié que ce code existe. C'est
   Q-B2.

## 8. Ligne de GO proposée (non inscrite)

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | **Banc de 24 mondes de calibration MR-2, part hors crédits** (suite de l'issue P-2 du pilote, GO-2026-11-16-08) : simulation sur processeur seulement, aucun appel de modèle, aucune clé de fournisseur de modèles sur la machine ; P_CACHÉE := p_c ponctuel (0), P_VUE := 0,25 supposée, règle de garde de la conception v4 (au moins 12 mondes sur 24), règle rapportée à la borne haute de l'intervalle ; code `monde_riche_v4.py` (`4b165847…`) inchangé, lanceur du banc v1 contre-lu ; secret de calibration neuf engagé et poussé avant la phrase de Lazar ; mondes jamais publiés ni réutilisés hors de la course ; une machine jetable (au plus 0,15 USD/h, minuterie 17 h), une seule création ; conditions toutes exigées : préenregistrement du banc contre-lu, vérifié et scellé ; procédure machine du banc vérifiée « jouable » ; issue lue par un sous-agent neuf ; jamais de ligne d'extension ; arrêt par identifiant (R10), dépenses et arrêts consignés | 3 USD (hors crédits) | 2026-11-30 | Lazar | R-3005, R-3015 ; mot de Lazar à recopier |
```

Aucune ligne sur crédits de Claude : rien ne s'y paie.

## 9. Décisions de Lazar

**Q-B1 — Où tourne le banc.** Enjeu : garde du secret de calibration contre coût.
(a) **Machine jetable louée** (section 4) : secret et mondes ne vivent que sur elle, procédure du pilote déjà jouée ; 0,30 USD
attendus, 3 USD au pire, une procédure à dériver et à vérifier. (b) **Processeur du conteneur d'une session**, comme la conception v4 :
0 USD, rien à louer ; mais secret et mondes sur la machine d'une session qui écrit pour la course, garde plus faible que celle
qu'écrit le brouillon 3. (c) **Poste de Lazar** : 0 USD ; demande son temps et son poste pendant 5 à 13 h.
Recommandation : **(a)**, confiance 0,6. **Sans défaut** (dépense).

**Q-B2 — Périmètre du banc.** Enjeu : délai avant le 30 novembre contre ordre du brouillon 3.
(a) **Banc de la règle seul**, maintenant, sur le code gelé (juge simplifié, n = 400), lu à la lettre du texte scellé du pilote ; il
décide de la course ; le reste du banc de la course (n, forme, f, τ, surdité) se fera plus tard, sur ses règles scellées et un
secret de calibration neuf. (b) **Un seul banc complet**, après la pièce des règles du banc et le code v68 de la course contre-lus ;
la règle en dernier (ordre D-2) ; plus juste, plus long, et dépend d'un code que je n'ai pas vu.
Recommandation : **(a)**, confiance 0,55. Défaut sous 48 heures : (a). À savoir avant de choisir : sous (a), la condition « banc de calibration fait (n et seuils fixés par leurs règles) » de GO-2026-11-13-01 et -02 (échéance 2026-11-30) n'est pas remplie par ce banc ; le banc plus large reste dû avant la course, ou un mot de Lazar qui lève cette condition ; le défaut à 48 heures ne la lève pas, et je n'ai pas vérifié que le code v68 de la course existe.

**Q-B3 — Dénominateur de la règle.** (a) **Tous les mondes tirés** : un monde sans tirage conforme en 8 ne garde rien (forme dure que
propose la v4). (b) Les mondes conformes seulement (ce que compte le code v4).
Recommandation : **(a)**, confiance 0,65. Défaut sous 48 heures : (a).

## 10. Déclaration

- J'ai lu le verdict par `git show` sur `verdict/pilote-mr2-v74-v14-v1`, le texte scellé du pilote, la procédure v14 au commit
  `2d35cafa`, la pièce de dépense au commit `2f7acc1d`, la conception v4, le code `monde_riche_v4.py`, les heures des parties v4 et
  le brouillon 3 de la course ; branches prises par `git fetch` avec refspec, sans clone.
- Je n'ai rien ouvert de la sortie du pilote au-delà du verdict et de la pièce de dépense ; aucune branche
  `calcul/pilote-mr2-v74-entree-*` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, de l'étape B bis ni du bras d'attaque.
- Aucune dépense, aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucun lancement, aucune valeur de clé lue ;
  aucun fichier existant modifié ; aucun commit ; `registres/decisions.md` non touché.
- Les durées et l'attendu de la machine sont **estimés** (journal v4, prix de la machine du pilote) ; seuls les plafonds sont des
  bornes.

Fin de la rédaction : 2026-11-16T20:51:17Z (`date -u`).

## 11. Contre-lecture

- **Rapport** : `contre-lecture-devis-banc-calibration-mr2-tour1-v1.md` (même dossier), empreinte
  `7fd26c76bfcb6c16c722dc4a9a18f91da193b2271c76ec98f8f009598be3e191` ; lecteur : modèle C, contre-lecteur neuf (R2) ; verdict : **corrections (2 majeures, 5 mineures)**.
- **Pièce lue par le rapport** : la v1 de ce devis, `6172ae590c29901a040bd39804177a844e74b9f9f7589acf22b7b5e22ca942db` ; la v1 reste intacte (R12).
- **Application** : par le programme `appliquer-corrections-devis-banc-calibration-mr2-tour1-v1.py` (même dossier, scellé à côté), couples « ancien → nouveau » recopiés du
  rapport ; il vérifie l'empreinte de la v1 et du rapport, que chaque « ancien » figure une seule fois, et refuse d'écraser la v2.
  Rédacteur des corrections : un rédacteur neuf (modèle C), qui n'a écrit ni la v1 ni le rapport. Rien d'autre n'a changé que les
  couples du rapport, la version et l'heure de l'en-tête, et cette section.

Réponse point par point :

| point du rapport | où | suite |
|---|---|---|
| **M1** — liste d'arrêt contre dénominateur | section 6 point 1 ; section 7 point 5 | **appliquée** : « monde sans tirage conforme » retiré de la liste d'arrêt, compté selon Q-B3 et rapporté ; probabilité d'au moins un monde sans tirage conforme chiffrée (≈ 9 % à 0,5 refus par tirage, ≈ 33 % à 0,6 ; recalculées : 1 − (1 − 0,5^8)^24 = 0,089 ; 1 − (1 − 0,6^8)^24 = 0,335) |
| **M2** — condition de la course non remplie sous Q-B2 (a) | section 9, Q-B2 | **appliquée** : Lazar est averti que (a) laisse ouverte la condition « banc de calibration fait (n et seuils fixés par leurs règles) » de GO-2026-11-13-01 et -02, et que le défaut à 48 heures ne la lève pas |
| **m1** — 13 lignes du bloc gelé, non 12 | section 2, Code | **appliquée** (recompté : 13 lignes `orchestrator/mr2_v68/…` aux lignes 562 à 574 du texte scellé `8aa33014…` ; le verdict dit aussi 13) |
| **m2** — arrondi de l'attendu et prix non borné | section 5 | **appliquée** (5 h × 0,052222 = 0,26 ; 0,75 à 0,15 USD/h) |
| **m3** — coûts « chacun » de `fable52` | section 3 | **appliquée** (moyennes ; les durées des deux complets diffèrent au verdict : 388,807 s et 430,542 s) |
| **m4** — prédiction chiffrée à la borne haute | section 7 point 4 | **appliquée** (bascule du modèle approché du texte scellé à 0,034, probabilité 0,5, et à 0,051, probabilité 0,05 : vérifiées dans le texte scellé) |
| **m5** — couplage des deux passes | section 6 point 2 | **appliquée** (flux commun en génération 1 seulement) |
| remarques facultatives 1 à 4 | — | aucune correction exigée ; non portées dans la pièce (rien d'autre ne change) ; les remarques 1 (ne jouer que ce que décide le préenregistrement) et 2 (garde d'échéance équivalente à celle de la v14) restent à prendre au préenregistrement et à la procédure du banc |
| points pour la session mère 1 à 5 | — | les points 1 à 3 sont portés par M2, M1 et m4 ; le point 4 par m2 ; le point 5 n'appelle rien |

Aucune correction refusée. Observation sans changement (hors du rapport, donc non appliquée) : la section 0, point 3, annonce
« deux décisions de Lazar (section 9) », alors que la section 9 en pose trois (Q-B1 à Q-B3).

Version v2 scellée : 2026-11-16T20:58:19Z (`date -u`).

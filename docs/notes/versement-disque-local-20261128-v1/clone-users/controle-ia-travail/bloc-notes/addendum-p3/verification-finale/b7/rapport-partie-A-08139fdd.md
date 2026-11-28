# Vérification des corrections du brouillon 7 de l'addendum de P3 (contre-lecture 5, R2)

**Verdict de la partie A (texte) : scellable après corrections.**

Le brouillon 7 applique tous les constats de la vérification finale destinés au texte. Il n'ajoute rien d'autre, sauf
deux mentions de traçabilité attendues. Chaque phrase neuve décrit le module, sauf une. La précision 17 neuve, lue avec
la définition de la garde 11 (« une entrée est en échec si l'un de ses calculs l'est »), exige des « non lus » d'entrée
entière que le module n'écrit pas quand l'échec vient d'un calcul (VB7-01). L'entrée « Contre-lecture 4 » dit encore
« relu face à ce texte », sans l'empreinte du brouillon relu (VB7-02). Il faut donc deux corrections de texte, d'une
phrase chacune. Le module ne change pas. Le reste du texte est inchangé. Le validateur ne signale que les marqueurs
attendus.

- Relecteur : sous-agent neuf (R2). Je n'ai écrit ni le préenregistrement, ni le module, ni ses tests, ni aucune
  correction ou relecture précédente. Date : 2026-10-20 (UTC), de 07:14 à 07:40.
- Dépôt de travail en lecture seule : aucune écriture, aucune commande git sur lui. Après mon repère de 07:26, aucun
  fichier du dépôt n'est plus récent (`find -newer`, hors `.git`). Rien lu sous `runs/`, `diag/`, `donnees/` ni
  `traces/`. Aucune commande Vast.ai.
- Tout ce que j'ai écrit est sous `verification-finale/b7/`, plus ce rapport. Tous les lancements portent `python -B`
  et `PYTHONDONTWRITEBYTECODE=1`. Aucun cache n'a été créé (`find -name __pycache__ -newer` : vide). J'ai importé le
  module et les tests depuis une copie (`b7/copie/`), dont les empreintes sont contrôlées au début et à la fin de chaque
  essai. Les simulations restent dans le processus.
- Originaux : brouillons 6 et 7, module, rapports VF1 à VF3, traitement et journaux du banc ont la même empreinte au
  début et à la fin (`b7/empreintes-au-debut.txt`, `sha256sum -c`). Une seule exception, hors de mon fait : la session a
  réécrit en place `final-b4/test_complements_p3_v1.py` à 07:20:40 (`7605c205…` → `7387910d…`), pendant ma revue, pour
  préparer la partie B. Mes essais prennent les aides des tests dans la version relue par la vérification finale
  (`7605c205…`, copiée de `verification-finale/calculs/copie/`).

## Ce qui a été lu (avec empreintes)

| fichier | sha256 | lecture |
|---|---|---|
| brouillon 6 `P3-addendum-lecture-complementaire-v1-brouillon6.md` | `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a` | différentiel strict avec le brouillon 7 |
| brouillon 7 `P3-addendum-lecture-complementaire-v1-brouillon7.md` | `c3e9c27f3da2eb3270a8b52b24e9533734a640bb6453f2bca463fad766bb0c28` | en entier |
| module `final-b4/complements_p3_v1.py` | `2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996` | en entier (2 289 lignes) |
| tests relus par la vérification finale (copie de `calculs/copie/`) | `7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d` | aides ; tests des gardes 12 à 16 ; test de l'aire vectorisée |
| VF1 `verification-code-final-addendum-P3-v1-texte.md` | `7a1aa7d785f470c3fb382a513506b28ae8a9075d22bf745b22b474540e8aa628` | en entier |
| VF2 `verification-code-final-addendum-P3-v1-mutants.md` | `aab50bf0230cd923f8c0c3ee9a5f91c5f6bb6805e28ce79f2c9138abda5ecc7b` | en entier |
| VF3 `verification-code-final-addendum-P3-v1-calculs.md` | `2a0626dad4eb6c6582c2caf6deea36845ac1076a72ee5517ca9e1d13e681b750` | en entier |
| traitement `traitement-R2-addendum-P3-v1.md` | `dd2f0aeee82e7ca121dfbaaac2fce8b0cf4a22a8684ec14ae810da4e4cd2b840` | en entier ; section « Vérification finale » à la lettre |
| journaux du banc `rapports/revue-b3-3/essai_07.log`, `essai_07b_import.log` | `063661ac4a75e4f00caf0ee404189e6ffc54f1c7395d6a775647870854939fb7`, `baaf517eb27fc9eb4d5865cae962daa21e99d1cd7d1252079b874076eeb475c7` | en entier |
| script du banc `essai_07_banc_taille_reelle.py` et `commun.py` (revue CB3) | — | chemins d'import (module de `final/`) |
| rapport CB3 `rapports/contre-lecture-code-b3-3.md` | `8aa42a89beb16079da2bbc4d3fc903ada726600a4dcc9be36e3dac5927501605` | lignes du banc (l. 13, 35, 99-110) |
| module du brouillon 3 `final/complements_p3_v1.py` | `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa` | empreinte seulement |
| outils de la session `remplir_texte_final_v1.py`, `verser_addendum_v1.sh` | `0471ac9236fafb9fc6618fcf0c43068eb70a8749f7231750f140dfc57f6d97bd`, `ddfcc1e74265a120ba00bec89e30f68f752ef54ff7ae8efa21fbb712186b8dc2` | en entier |
| code gelé (dépôt, lecture seule) | — | `sondes/evaluation.intervalle_blocs` ; `sondes/temoins.difference_aires_appariee` ; `statistiques` (`effet_cout_apparie`, `detection`, `detection_etiquettes`) ; `lecture.py` (`JEUX`, `nom_jeu`, `_permuter_dans_les_taches`, graines de la lecture) ; `manifeste.py` (`graines`, `generateur`, `creer_manifeste`) ; `run_harnais_factice.graine_entiere` ; `prereg.py` ; expressions de `validation_reelle` |

## Ce qui a été lancé

| quoi | résultat | journal (sous `b7/`) |
|---|---|---|
| différentiel par mots (`git diff --no-index --word-diff`, hors dépôt) et par lignes | 14 blocs de différences | `diff-mots-b6-b7.txt`, `diff-lignes-b6-b7.txt` |
| différentiel strict par jetons, blancs compris (`diff_strict.py`) | 54 changements de mots ; 6 changements de blancs seuls (recoupes de lignes) ; caractères spéciaux et fins de ligne inchangés | `diff-strict-b6-b7.log` |
| essais `cles`, `g14`, `g15`, `validateur`, `regex` (`essais_b7.py`) | voir (2) et (3) | `essais-rapides.log` |
| essai `p17` (précision 17) | VB7-01 reproduit | `essai-p17.log` |
| essai `p8` (précision 8, addendum complet à 60 tirages) | chaque conclusion établie a au moins un contrôle lu | `essai-p8.log` |
| validateur du dépôt, commande demandée, sur une copie du brouillon 7 | marqueurs attendus seulement | `validateur.log` |
| entrées de la section « Contre-lecture », texte rempli de valeurs factices | VB7-02 reproduit | `entrees-contre-lecture.log` |

## Constats (le plus grave d'abord)

Aucun bloquant, aucun majeur. Trois mineurs : deux de texte, un de procédure. Quatre pour information. Chaque constat est
reproduit.

### VB7-01 — mineur — précision 17 : « une entrée qui tombe en échec » couvre aussi un calcul en échec, où le module n'ajoute aucun « non lu » d'entrée entière

- **Où** : brouillon 7, précision 17 (l. 414-416). L'échec d'une entrée est défini par le texte lui-même : garde 11
  (l. 334-335 : « une entrée est en échec si l'un de ses calculs l'est ») et en-tête de la liste d'arrêt (l. 306-308).
  Code :
  - `_Entree.calcul`, l. 952-966 : une `GardeArret` levée dans un calcul est prise là (motif écrit, `echecs`, None) ;
  - `_Entree.sortie`, l. 995-997 : l'entrée est « échec » dès qu'un de ses calculs l'est ;
  - `_executer_entree`, l. 1755-1770 : les contrôles « (entrée entière) » ne sont écrits que dans la branche `except`,
    donc pour une `GardeArret` levée hors d'un calcul ;
  - `synthese`, l. 1815-1816 : la garde 11 compte toute entrée à l'état « échec ».
- **Problème** : la phrase neuve dit : « Une entrée qui tombe en échec garde les contrôles déjà faits […]. Chaque cible
  visée par l'analyse reçoit en plus un contrôle « non lu » (entrée entière), même si ses contrôles ont tous été faits ».
  Avec la définition de la garde 11, la phrase vise aussi une entrée dont un seul calcul a échoué. Dans ce cas, le module
  n'écrit aucun « non lu » d'entrée entière : il rend « non lu » le seul contrôle qui dépend du calcul. À la lettre du
  texte scellé, la sortie aurait donc des réserves en moins, le sens même que la parenthèse exclut. Un auditeur pourrait
  y lire un écart au préenregistrement scellé, qui est un nœud de Lazar. Le verdict R13 pourrait aussi ajouter à tort
  « non contrôlée ». Ce chemin est plausible au réel : VF3-04 a vu A1 T4 tomber en échec à 14 tâches (22 tirages
  dégénérés sur 2 000). Le défaut vient de la correction : le brouillon 6 ne l'avait pas (« seuls les contrôles non
  faits deviennent « non lus » »). VF3-01 proposait l'incise « hors d'un calcul », qui n'a pas été reprise.
- **Reproduit** (`essais_b7.py p17`, `essai-p17.log`). Scénario `_sc_sain` des tests, 60 tirages, 13 conclusions
  établies.
  - (a) `GardeArret` simulée dans le seul calcul T4 de A1 : l'entrée est « échec » et `calculs_en_echec` vaut ["T4"]. Le
    contrôle T4 est « non lu ». **Aucun** contrôle « A1 (entrée entière) » n'est écrit. La synthèse compte l'entrée en
    échec (garde 11) et ne rend qu'une réserve, `reserve_A1_non_lue` sur T4. La lettre du brouillon 7 en demanderait cinq
    (P3-P3, P3-P4, T3, T1 et T4).
  - (b) `GardeArret` hors d'un calcul (permutation du placebo) : cinq contrôles « A1 (entrée entière) », comme le décrit
    le brouillon 7.
- **Correction** (texte seulement ; le module ne change pas) : « 17. Une entrée qu'une `GardeArret` levée hors d'un
  calcul fait tomber en échec (entrée entière) garde les contrôles déjà faits, réserves contraires comprises ; l'addendum
  n'efface jamais une réserve qu'il a calculée. Chaque cible visée par l'analyse reçoit en plus un contrôle « non lu »
  (« <analyse> (entrée entière) »), même si ses contrôles ont tous été faits (sens prudent : une réserve en plus, jamais
  en moins). Un calcul en échec rend « non lu » le seul contrôle qui en dépend, sans contrôle d'entrée entière ;
  l'entrée compte alors comme en échec pour la garde 11. » Ajout facultatif, utile au verdict R13 : « ces « non lus »
  d'entrée entière comptent parmi les réserves possibles de l'audit de symétrie (VF2-03) ; une même conclusion peut alors
  être dite à la fois « non robuste » et « non contrôlée par l'addendum » ».

### VB7-02 — mineur — « Contre-lecture 4 » : « relu face à ce texte », sans l'empreinte du brouillon relu

- **Où** : brouillon 7, l. 460. La phrase n'a pas changé depuis le brouillon 6, mais elle devient fausse dans le
  brouillon 7.
- **Problème** : les trois vérificateurs ont relu le module face au brouillon 6 (`411eb334…`, tableaux « Ce qui a été
  lu » de VF1, VF2 et VF3), pas face à « ce texte », c'est-à-dire le brouillon 7 rempli. L'entrée ne cite pas non plus
  l'empreinte du brouillon relu. Une fois remplie, elle porte quatre empreintes (module et trois rapports), aucune de
  brouillon. Le validateur passe, puisqu'il demande deux empreintes au moins. Mais pour R2, `prereg.py` (l. 3-7) demande
  « l'empreinte du brouillon relu ». Celle du brouillon 6 n'apparaît qu'à l'entrée 5.
- **Reproduit** : `entrees-contre-lecture.log`, sur le texte rempli de valeurs factices : « entrée 4 : 4 empreintes
  distinctes ; brouillon 6 (411eb334) cité : False ; « face à ce texte » : True ».
- **Correction** (texte) : « module final (sha256 `<<EMPREINTE_MODULE>>`) relu face au brouillon 6 (sha256
  `411eb3344b153cc81f118aad3dab5781934f60c1f9dc22efdf3f2ef2f5338a1a`) par trois sous-agents neufs ».

### VB7-03 — mineur (procédure) — corrections après cette relecture : nom du brouillon, empreinte citée, outils

- **Où** : brouillon 7, entrée « Contre-lecture 5 » (l. 469-473) ; `remplir_texte_final_v1.py`, l. 21 et 34 ;
  `verser_addendum_v1.sh`, l. 28.
- **Problème** : VB7-01 et VB7-02 demandent de changer le texte. Or le remplisseur lit le fichier nommé « brouillon7 »
  et calcule `<<EMPREINTE_BROUILLON7>>` au moment du remplissage. Si le brouillon 7 est corrigé en place, deux règles
  sont violées :
  - R2 : l'entrée 5 citerait comme relue une empreinte que personne n'a relue ;
  - R12 : une version serait écrasée.

  Le versement ne copie que les brouillons 1 à 7. Les tests de `final-b4/` ont déjà été réécrits en place
  (`7605c205…` → `7387910d…`, à 07:20:40). La version relue ne survit que dans les copies de la vérification finale.
- **Reproduit** : lecture des deux outils (lignes citées) ; `stat` et `sha256sum` du fichier de tests.
- **Correction** :
  - écrire les corrections dans un brouillon 8, sous un nouveau nom ;
  - à l'entrée 5, citer le brouillon 7 relu (`c3e9c27f…`), puis « corrigé en brouillon 8 (sha256 …) : VB7-01, VB7-02 » ;
  - adapter le remplisseur : le brouillon 8 comme texte source, `EMPREINTE_BROUILLON7` calculée sur le brouillon 7
    inchangé ;
  - étendre la boucle du versement de 1 à 8 ;
  - garder une copie nommée de chaque version relue des tests ;
  - m'envoyer le brouillon 8 avec les tests : la partie B vérifiera le différentiel 7 → 8 dans ce même rapport (R2).

### VB7-04 — information — précision 12 : `<jeu>` écrit en mots ; portée de « Tirages comme `intervalle_blocs` »

- **Où** : brouillon 7, l. 396-402 ; module, l. 129 et 1908.
- **Problème** :
  - La liste fermée écrit les objets de A1 en identifiants (`saboteur-honnete`…), mais le `<jeu>` de A7 en mots
    (« saboteur contre honnête, contre témoin et contre mention »). Les clés réelles sont `saboteur-honnete`,
    `saboteur-temoin` et `saboteur-mention` (`CIBLES_A7`). Je les ai déduites par analogie. Avec elles, les 69 clés du
    texte égalent celles du module et celles du manifeste.
  - « Tirages comme `intervalle_blocs` » vaut pour les tirages du module (A1, A2 (b), A3, A4 (a) et (b)). Les fonctions
    gelées tirent à leur façon. Par exemple, `effet_cout_apparie` (A6) tire en un seul appel,
    `rng.integers(0, d, size=(10 000, d))`, sur les tâches lisibles triées (`statistiques.py` l. 59-72).
  - Aucun nombre n'en dépend : le module, cité par son empreinte, fixe tout.
- **Reproduit** : `essais-rapides.log` (« <jeu> tel qu'écrit », « jeux de A7 dans le module ») ; lecture du code gelé.
- **Correction** (facultative, à joindre au brouillon 8) : « `<jeu>` parmi `saboteur-honnete`, `saboteur-temoin`,
  `saboteur-mention` » ; « Tirages propres au module comme `intervalle_blocs` ».

### VB7-05 — information — garde 15 : le code dépasse un peu la lettre, dans un sens ou dans l'autre, sans effet

- **Où** : module, l. 75, 2006-2009 et 243-249.
- **Problème** :
  - (i) L'expression `^…-addendum-p3$` accepte aussi le nom suivi d'un saut de ligne : en Python, `$` admet un `\n`
    final. `creer_manifeste` l'accepte aussi.
  - (ii) Le préenregistrement est comparé comme une chaîne : `./prereg/…` est refusé, alors qu'il désigne ce texte.
    C'est la forme exacte du plan, point 2.
  - (iii) Des messages « garde 15 » (`verifier_parametres_tirage`) sont levés dans des calculs, après le manifeste. Ils
    donneraient un « échec », pas un arrêt. Ils ne peuvent pas se déclencher une fois `exiger_parametres_du_texte`
    passée.

  Aucun de ces cas ne permet un second passage ni une promotion.
- **Reproduit** : `essais-rapides.log`, section garde 15.
- **Correction** : aucune avant le scellement (module figé). Au plus : « hors de la forme exacte de la commande du plan,
  point 2 ».

### VB7-06 — information — en-tête : date et auteur restés au stade des premiers brouillons

- **Où** : brouillon 7, l. 3-10 (inchangées).
- **Problème** :
  - « Date (UTC) : 2026-10-19 » précède des faits que le texte cite : la requête 007 et les contre-lectures 4 et 5,
    toutes du 2026-10-20.
  - « Auteur : … les deux contre-lectures et la relecture externe du brouillon 2 » : il y a cinq contre-lectures et
    quatre requêtes à Gemini.

  L'antériorité se prouve par le commit de scellement (garde 3), pas par cette ligne.
- **Reproduit** : lecture de l'en-tête et de la section « Contre-lecture ».
- **Correction** (facultative) : « Date (UTC) : celle du commit de scellement, qui fait foi (rédaction du 2026-10-19 au
  2026-10-20) », comme P3 ; « … les contre-lectures et relectures de la section « Contre-lecture » ».

### VB7-07 — information — précision 1 et la fenêtre de VF1-11

- **Où** : précision 1 (l. 375-376) ; `executer`, l. 2228-2234.
- **Problème** : `reference`, dont `verifier(chemin_l)`, est construit après la création du manifeste, hors du `try` qui
  écrit l'arrêt. Un arrêt à cet endroit laisserait un manifeste sans sortie, contre la lettre de la précision 1. Le
  traitement a noté VF1-11 sans changer le module : le cas est inatteignable, puisque le même fichier est vérifié à la
  l. 2216. La lettre du texte reste pourtant inexacte pour ce cas.
- **Reproduit** : lecture du code (l. 2216, 2224, 2228-2235) ; essai de VF1-11 (`texte/essais/vf/test_vf_texte_2.py`).
- **Correction** (facultative, texte) : ajouter à la précision 1 « sauf la relecture de l'empreinte de la lecture
  décisive, faite juste après la création du manifeste et hors de cette écriture (fichier vérifié juste avant) ».

## (1) Différentiel du brouillon 6 au brouillon 7 : chaque changement

| bloc | brouillon 7 | changement | source | ce que fait le module (lignes) | état |
|---|---|---|---|---|---|
| 1 | l. 1 | titre « v1, brouillon 6 » → « v1 » | VF1-08 | — | juste |
| 2 | l. 236 | plan 3 : « (sauf le contrôle des graines de la garde 15, voir cette garde) » | VF1-02 | `executer` l. 2209-2222 (gardes avant le manifeste), l. 2224 (manifeste), l. 2235 → `analyser_addendum` l. 1947 → `preparer_donnees` l. 1984 (`exiger_graines`) | juste |
| 3 | l. 271-278 | plan 9 : banc de CB3 sur le module `daf95459…`, non refait ; rapport et deux journaux avec chemins et empreintes | VF1-05 | journaux : 426,5 s ; A1 327,5 s ; A4 63,2 s ; 647 Mo ; 564 Mo ; données (2 400, 430). Le banc importe `final/` (`daf95459…`). Empreintes égales. Versement l. 21-24, 34 | juste |
| 4 | l. 308-309 | en-tête de la liste d'arrêt : « sauf le contrôle des graines de la garde 15 » | VF1-02 | comme le bloc 2 | juste |
| 5 | l. 337-338 | garde 12 : aire vectorisée du module (1e-12, test) et quantile 0,95 de `np.quantile` | VF1-04 | `exiger_coherence` l. 658, 663, 666 ; `TOLERANCE_COHERENCE` l. 98 ; test l. 562-586 | juste |
| 6 | l. 344-345 | garde 14 : ligne exactement vide ignorée ; ligne d'espaces illisible ; motif « garde 4 » | VF1-12, VF2-09 (règle des notes citée par VF2-04) | `charger_textes` l. 2176-2182 | juste (essai `g14`) |
| 7 | l. 346-347 | garde 15 : forme `…-addendum-p3` ; préenregistrement de la commande | VF1-07 | `RUN_ADDENDUM` l. 75 ; `exiger_commande` l. 2006-2009 | juste (nuances : VB7-05) |
| 8 | l. 349-350 | garde 15 : graines du manifeste, contrôlées juste après sa création ; arrêt écrit | VF1-02 | l. 2224, 2234-2241, 1947, 1984, 1912-1926 | juste (« au début des analyses » : au début de `preparer_donnees`, avant les gardes refaites et les analyses) |
| 9 | l. 363-364 | liste des tests : gardes 12 à 16 nommées | VF1-06 | tests relus : garde 12 l. 1149 ; 13 l. 1161 ; 14 l. 1003-1062 ; 15 l. 609, 877, 3156-3178, 3209-3214 ; 16 l. 3088 | juste ; R5 des règles neuves des gardes 14 et 15 : partie B |
| 10 | l. 385-386 | précision 8 | VF1-03 | `synthese` l. 1833-1834. Chaque cible établie est visée par A1 (l. 1024-1036), A2 (l. 1153-1164) ou A6 (l. 1471-1491), ou par un « non lu » d'entrée entière (l. 1766-1769) | juste (essai `p8`) |
| 11 | l. 392-402 | précision 12 : liste fermée ; conventions de tirage | VF3-02, VF3-03 | `cles_addendum` l. 1899-1909 (69 = 2 × 33 + 3) ; `_rng` l. 252-253 ; `_tirages` l. 264-272, égal à `intervalle_blocs` (`evaluation.py` l. 46-53) ; placebo l. 1038-1042 ; départs l. 1065 et 1069 | juste (VB7-04) |
| 12 | l. 408 | précision 15 : « pour les intervalles que calcule le module » | VF1-10 | l. 357 (A1, A4 (a), A4 (b)), l. 1109 (A2 (b)), l. 1219 (A3) | juste |
| 13 | l. 414-416 | précision 17 | VF1-01, VF2-03, VF3-01 | `_executer_entree` l. 1755-1770 | juste pour une garde levée hors d'un calcul ; **inexacte pour un calcul en échec : VB7-01** |
| 14 | l. 448, 450-452 | « le brouillon 3 » (deux fois) ; requêtes 006 et 007 | VF1-08 | traitement l. 62-73 et 100-108 | juste |
| 15 | l. 467-468 | contre-lecture 4 : « Constats traités dans le texte (brouillon 7) et dans les tests seulement… » | hors constat : décision du traitement (l. 110-116) | — | juste ; la phrase voisine « face à ce texte » : VB7-02 |
| 16 | l. 469-473 | entrée « Contre-lecture 5 » | hors constat : trace R2 de cette relecture | — | attendue ; procédure : VB7-03 |

S'y ajoutent 6 changements de blancs seuls : des lignes recoupées dans les blocs 3, 7, 12 et 13.

**Constats que le traitement accepte pour le texte** : tous sont appliqués (VF1-01 à VF1-08, VF1-10, VF1-12, VF2-03,
VF2-09, VF3-01 à VF3-03).
- VF1-09, VF2-08, VF3-05 : traitement seulement, aucun texte attendu.
- VF1-11, VF2-07, VF2-10, VF3-04, VF3-06 : notés.
- VF2-01, VF2-02, VF2-04, VF2-05, VF2-06 : tests (partie B).

**Changements sans constat** : seulement les blocs 15 et 16, qui sont attendus.

## (2) Vérifications ciblées

- **Précision 12, liste fermée.** 69 clés : 2 sondes × 33, plus 3 clés pour A6. Le texte développé égale
  `cles_addendum(P)`, qui égale les clés du manifeste (`manifeste.graines`), une à une. Le module lit chaque motif de
  clé (`essais-rapides.log`). Seul écart de forme : `<jeu>` est écrit en mots (VB7-04).
- **Conventions de tirage.**
  - `_tirages` (l. 264-272) : tâches dans l'ordre de `np.unique`, puis `rng.integers(0, u, size=u)` à chaque tirage.
    C'est la règle de `intervalle_blocs` (`evaluation.py` l. 46-53, `default_rng(int(graine))`) et de
    `difference_aires_appariee`.
  - Générateurs : `_rng` vaut `default_rng(graine_entiere(…))` (l. 252-253). Les fonctions gelées reçoivent une graine
    entière et en font `default_rng(int(graine))`, une fois par appel : un générateur par clé (`detection_etiquettes`
    appelle `intervalle_blocs` une seule fois). A6 utilise `generateur(…)` (l. 1464).
  - Placebo : un seul générateur, qui sert d'abord à `lp._permuter_dans_les_taches` (une permutation par tâche,
    `lecture.py` l. 194-199), puis aux tirages (l. 1038-1042).
  - A2 (b) : actions dans l'ordre de `rang` (l. 1059). Départs du pré-coût : `rng.integers(0, c − L + 1, size=50)`
    (l. 1065). Puis, si `L_cout > c`, départs du coût : `rng.integers(c, fin − L + 1, size=50)` (l. 1069). Conforme.
- **Précision 17.** Le texte est conforme pour une `GardeArret` levée hors d'un calcul :
  - les contrôles déjà faits sont gardés, réserves comprises (l. 1762) ;
  - chaque cible de `VISEES` reçoit un « non lu » (l. 1766-1769), ou « sans objet » si elle n'est pas établie.

  Il ne l'est pas pour un calcul en échec : VB7-01.
- **Garde 15.**
  - Nom : `^[0-9]{8}-[0-9]{6}-addendum-p3$` (l. 75). `…-addendum-p3-bis` et `…-autre` sont refusés.
  - Préenregistrement : égalité de chaîne (l. 2008).
  - Ces deux contrôles passent avant toute lecture : c'est le premier appel de `executer` (l. 2209).
  - Graines : ce sont celles du manifeste (l. 2235). `exiger_graines` (l. 1984) les contrôle après `creer_manifeste`
    (l. 2224), dans le `try` qui écrit l'arrêt (l. 2234-2241).

  Conforme ; nuances en VB7-05.
- **Garde 14.**
  - Découpe sur `b"\n"` (l. 2176). Une ligne de zéro octet est ignorée (l. 2177).
  - Ligne d'espaces, de tabulation, ou faite d'un seul retour chariot : arrêt « garde 4 : fichier … : ligne N illisible
    (JSONDecodeError) », sans texte (l. 2182). Octet UTF-8 invalide : même arrêt (UnicodeDecodeError).
  - U+2028 reste dans le texte.

  Conforme (`essais-rapides.log`).
- **Plan, point 9.**
  - Les empreintes citées égalent les fichiers : rapport CB3 `8aa42a89…`, `essai_07.log` `063661ac…`,
    `essai_07b_import.log` `baaf517e…`.
  - Les chiffres égalent les journaux : 426,5 s ; A1 327,5 s ; A4 63,2 s ; 647 Mo pour « environ 650 » ; 564 Mo pour
    « 560 » ; 2 400 actions × 430 sondes ; 2 000 et 10 000 tirages.
  - Module mesuré : celui de `final/` (`daf95459…`), d'après le `sys.path` du script du banc. Le rapport CB3 versé le
    nomme (l. 13).
  - Le versement copie le rapport et les deux journaux aux chemins cités, puis les scelle (`verser_addendum_v1.sh`
    l. 21-23 et 34).

  Conforme.
- **Précision 8, garde 12, précision 15** : voir la table (1).

## (3) Reste du texte, validateur, outils

- **Le reste du texte est inchangé.** Le différentiel strict par jetons, blancs compris, compte 54 changements de mots,
  tous dans les 16 blocs, et 6 changements de blancs seuls (recoupes de lignes). Les espaces insécables et fines (U+00A0,
  U+2009, U+202F, dont l'expression de A6, l. 167) sont en même nombre. Il n'y a aucun retour chariot, aucune
  tabulation, aucun blanc en fin de ligne. Le fichier finit par un saut de ligne.
- **Validateur.** Commande : `cd /home/user/controle-ia-travail && PYTHONPATH=src …/venv-gpu-neuf/bin/python -B -c
  "from controle_ia.prereg import problemes; print(problemes('…/b7/copie/brouillon7-copie.md'))"` (copie `c3e9c27f…`).
  Il rend trois problèmes :
  - « contre-lecture 4 sans ses deux empreintes » ;
  - « contre-lecture 5 sans ses deux empreintes » ;
  - « marqueurs de gabarit restants » : les 13 marqueurs.

  Les trois viennent des marqueurs : les entrées 4 et 5 n'ont encore que des marqueurs à la place de leurs empreintes.
  Une fois rempli de valeurs factices bien formées, le texte rend `[]`.
- **Expressions lues par les gardes** (module, tests, commit, entropie) : une seule correspondance chacune, dans
  l'en-tête (l. 11-14). La mention « tests corrigés (sha256 …) » de l'entrée 5 ne répond pas à l'expression des tests.
- **Outils de la session.**
  - Le remplisseur couvre les 13 marqueurs, dont les trois neufs (`EMPREINTE_BROUILLON7`, `EMPREINTE_VERIFICATION_B7`,
    `VERDICT_VERIFICATION_B7`). Il s'arrête sur un marqueur absent ou restant, et n'écrase rien.
  - Le versement copie ce rapport au chemin que cite l'entrée 5.

  Réserve de procédure : VB7-03.

## Fichiers (sous `verification-finale/b7/`)

| fichier | sha256 |
|---|---|
| `diff_strict.py` | `f4db28960b1854da887afbe67a13bc7b6aa841be1f290de56637d96f85ccbc84` |
| `essais_b7.py` | `2066f549befa8dcf8d2158f07a47b11c750dd1535ffa594dcb2f092d307e69f0` |
| `diff-mots-b6-b7.txt` | `28220ddf3c95e47ad5d9129d35ecb048f03ab02546fca9973b0a128be5480f98` |
| `diff-lignes-b6-b7.txt` | `dc3cb5f0388a658f52a1dd6b919443473566d6c2f06be7054d1511c0602efc52` |
| `diff-strict-b6-b7.log` | `956174987de029eb66c94f1255a6c7c7f19aebd886d763ca54a8d6ff177ddd1c` |
| `essais-rapides.log` | `a251f3a06bf32f8c575ecef57f281b5eb76cd92c36f6a54d451354533f745fda` |
| `essai-p17.log` | `99232e2fd5860b103a178538b51549d862bdbfb9aa0438ab36bdfd9fe2b09283` |
| `essai-p8.log` | `bcad2a1918de4392c566171ecf4b8499c9a8f2619893732be6e0bddf786d6873` |
| `validateur.log` | `2b3990ade386eae99c56f34b9fd9d6a86e83e35730abd3a45841ec6d4d22b74d` |
| `entrees-contre-lecture.log` | `076ec4592140426559d9e33a865df93f6e403064491f55edb993366920ac62cf` |
| `empreintes-au-debut.txt` | `6c27185419a17d2346abf5d5f9473b36e20cfe76853f265e5c974414e5f719e1` |
| `copie/brouillon7-copie.md`, `copie/complements_p3_v1.py`, `copie/test_complements_p3_v1.py` | égales aux originaux relus : `c3e9c27f…`, `2b16179d…`, `7605c205…` |

## Partie B : tests corrigés

**En attente.** La session m'enverra le fichier de tests corrigé et, selon VB7-03, le brouillon 8. J'y vérifierai :
- les artefacts et cas sains de VF2-01, VF2-02 et VF2-04, et ceux, facultatifs, de VF2-05 et VF2-06, chacun prouvé sur
  sa copie mutée ;
- R5 pour les règles que le brouillon 7 écrit nommément : la ligne d'espaces de la garde 14 et le suffixe du nom à la
  garde 15 ;
- le nombre de tests écrit en tête ;
- l'absence de toute modification du module (`2b16179d…`) ;
- le différentiel du brouillon 7 au brouillon 8.

Le verdict global sera mis à jour ici.

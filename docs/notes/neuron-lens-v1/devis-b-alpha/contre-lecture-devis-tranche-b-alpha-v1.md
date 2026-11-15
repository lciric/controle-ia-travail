# Contre-lecture du devis de la tranche B-α de « Neuron Lens » — v1

**Verdict : feu possible après corrections.** Le plan suit le texte gelé dans l'ordre et ne change aucun critère ; les additions
tiennent, les empreintes aussi. Six points majeurs sont à corriger ou à trancher avant toute demande de feu ; aucun ne demande
de toucher au texte gelé. Le devis n'est pas une commande : le feu reste suspendu aux pièces de son § 6 (lanceur, amorce, dépôt
réduit, essai à blanc, commande, contre-lectures).

Contre-lecteur neuf (n'a écrit ni le texte gelé, ni le code, ni la course, ni le devis), le 2026-11-15T08:08:55Z (`date -u`), sur la copie
détachée `/home/user/relecture-devis-b-alpha`, branche `prep/neuron-lens-v1`, commit `1e07e7fa`. Aucun appel payant, aucune
location, aucune recherche d'offres, aucun résultat de mesure ouvert (`diag/`, `runs/`, fichiers `.json` de
`lecture-volet-a/` non ouverts), aucune valeur de clé lue.

## Pièces lues et empreintes vérifiées (compagnons recalculés)

| pièce | empreinte | état |
|---|---|---|
| `docs/notes/neuron-lens-v1/devis-b-alpha/devis-tranche-b-alpha-v1.md` | `3e06dbcdc23101b54246843a9bc0a5c94c9b7fd451ac7ac88e35afff0372990c` | égale au compagnon |
| `…/devis-b-alpha/releve-prix-vast-20261115T075924Z-v1.tsv` | `7a3d56e006645d65432e906a4eaa58d1a969fb59183b20fece2cc991e867d848` | égale au compagnon |
| `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (B.1 commun, seuils B, plan B.1 à B.4, critères de lecture B, audit R4, liste d'arrêt, écarts) | `34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131` | égale au compagnon |
| `docs/notes/neuron-lens-v1/addendum-empreintes-v3.md` (partie 1) | `e63d95ca…` | égale au compagnon |
| `src/controle_ia/neuron_lens/controles_b0_v2.py`, `verdicts_b_alpha_v3.py`, `garde_depense_v4.py`, `suivi_vast_v6.py`, `scripts/minuterie_destruction_neuron_lens_v3.sh` | `56350c9c…`, `8f57088a…`, `6a98d816…`, `2ecaaeed…`, `e2303277…` | égales aux compagnons |
| copies du dépôt voisin : `README.md`, `docs-findings.md`, `scripts-06_activations.py.txt`, `scripts-checks-causal_lens.py.txt` (sous `docs/sources/neuron-lens-lecture-20261113/` et `…-v1-devis-20261113/`) | `c3764398…`, `8814874b…`, `151d1196…`, `befb7018…` | égales à celles que cite le devis (l. 12-14) |
| `journal-course-volet-a-v2.md` (sans compagnon dans la copie : journal ouvert), `commande-volet-a-v14.md`, `scripts/amorce_neuron_lens_volet_a_v6.sh`, `lecture-volet-a/verdict-volet-a-v1.md` (§ 8 seulement, leçons de montage), ligne GO-2026-11-14-06 de `registres/go.md` (l. 325) | — | lus |

Citations du devis vérifiées sur les copies : README l. 552-555 (« minutes », « ~70 min on an RTX 4090 »), l. 567-568 (« 24 GB is
enough for the text passes ») ; constats l. 109 (« 68 minutes on an RTX 4090 ») et l. 207-209 (effets faibles et matériel) ;
`causal_lens.py` l. 277 (`score` sur `mps` sinon `cpu`) et défauts de `measure` ; `06_activations.py` l. 613 (16 processus
d'écriture). Arithmétique refaite : sommes des colonnes 2,4 ; 4,8 ; 8,8 h exactes ; 1,09 à 2,18 USD ; 7,92 + 1,35 = 9,27 USD ;
4 096 conditions de pilotage et 16 384 contextes d'ablation exacts.

## Majeurs

**M1 — L'addendum des empreintes, partie 2, n'est pas dans le plan, alors que la ligne de GO et la liste d'arrêt l'exigent.**
Devis l. 22-33 (tableau des étapes) et l. 124-126 (§ 6) : aucune étape ne l'écrit ni ne le scelle ; l. 10 ne cite que la partie 1.
Or la ligne dit « étape B0 d'abord (contrôles B0 scellés, addendum des empreintes partie 2) », la liste d'arrêt du texte gelé dit
« addendum des empreintes non scellé avant la première passe → rien ne part », et l'addendum v3 (§ 6) y met : poids et tokeniseur
de Llama 3.1 8B Instruct à la révision `0e9e39f2…`, les trois lentilles (égalité exigée), **les quatre tranches du corpus**
(empreintes des fichiers produits par `05_act_corpus.py`, égalité des listes d'identifiants de lignes), versions des
bibliothèques, tailles, compte des doubles jetons de début. Conséquence d'ordre : la partie 2 ne peut être close qu'**après**
l'étape 3 (corpus) et doit l'être **avant** l'étape 4 (fumée, première passe du modèle). Il faut aussi dire où elle est scellée
(sur la machine, compagnon poussé, sans pause humaine ; ou relue par la session, donc attente facturée à chiffrer) et que les
**sorties** des contrôles de B0 (pas seulement leur code) sont scellées et poussées avant toute passe.
- ancien (l. 27-28) : « 3. corpus d'activations […] et comptes de jetons » puis « 4. fumée `06_activations.py --docs 64` » ;
- nouveau : insérer « 3 bis. addendum des empreintes, partie 2 (fichier neuf, R12) : empreintes des fichiers téléchargés et des
  quatre tranches produites, égalités exigées par notre code, versions, tailles, comptes de jetons de début ; sorties des contrôles
  de B0 ; le tout scellé et poussé ; tout écart = arrêt — processeur, 0,05 à 0,1 h, pire cas 0,3 h » ; et au § 6 : « garde du
  lanceur : la fumée ne part pas sans le compagnon de la partie 2 ».

**M2 — Le plafond de 10 USD ne contient pas le pire cas du devis sous son propre arrêt dur, et les audits R4 du texte gelé ne sont
pas chiffrés.** Devis l. 75-79 : pire cas « ≈ 9,3 USD », arrêt dur à « 90 % (9 USD) » : au prix plafond, la course du pire cas est
détruite avant sa fin (la phrase « le pire cas recalculé tient sous 10 » est vraie du plafond, fausse de l'arrêt dur). En outre le
texte gelé prévoit, « verdict après l'audit » : « trop beau » → `measure` relancé avec la graine 1 (pire cas du devis pour
`measure` : 2,0 h, plus `score` 0,8 h), ce qui demande le **correctif (3), non écrit** (aucun fichier sous `correctifs/`) ;
« tout négatif » → `score` rejoué sur la sortie publiée de `measure` (2,9 Go, addendum v3 § 3), « dans le plafond ». Le devis
n'en dit rien et détruit la machine à l'étape 8 : un audit demanderait une seconde location qui referait les étapes 0 à 6.
- ancien (l. 76) : « plafond proposé 10 USD (… le pire cas recalculé tient sous 10) » ;
- nouveau, au choix de la mère : (a) garder le plafond de la ligne, 12 USD (compte rendu 7,2 ; arrêt dur 10,8) ; ou (b) garder
  10 USD **et** abaisser le prix plafond de la commande (par exemple 0,60 USD/h, au-dessus de la médiane relevée 0,5216 : pire cas
  avec relance et audit ≈ 13,1 h × 0,60 ≈ 7,9 USD, sous 9) ; dans les deux cas, écrire une ligne « audit R4 » au tableau (durée,
  où, sur la même machine avant destruction ou seconde location) et dire si le correctif (3) est écrit, contre-lu et scellé avant
  le feu (travail de session, sans dépense) ou si l'audit attend une autre ligne.

**M3 — Aux prix du jour, les gardes d'argent ne mordent qu'après le double du pire cas.** Devis l. 78-81 : à 0,4547 USD/h, le
compte rendu à 60 % (6 USD) tombe à ≈ 13,2 h, la minuterie et l'arrêt dur (9 USD) à ≈ 19,8 h, le rappel « indépendant » (80 % de
la minuterie) à ≈ 15,8 h, pour une course attendue de 2,4 à 4,8 h et un pire cas de 8,8 h. Les seuils en argent sont conformes à la
ligne, mais ils ne signalent ni une course lente ni une course figée ; au volet A il a fallu ajouter des bornes en cours de course
(R-2799, R-2800 : journal v2, 21:09Z et 21:13Z). Seule la règle « course figée » (l. 84) couvre ce cas, et elle dépend d'une session
éveillée, dont le conteneur a redémarré deux fois (journal v2, 17:14Z et 00:36Z).
- ancien (l. 81) : « rappel indépendant | à 80 % de la durée de la minuterie » ;
- nouveau : garder les seuils en argent **et** ajouter des bornes en durée, écrites avant le feu : compte rendu à la mère quand la
  durée dépasse le haut de l'attendu (4,8 h) ; rappel programmé à la durée du pire cas (8,8 h), où la mère décide ; échéance par
  étape dans l'état poussé (durée attendue et pire cas du tableau), dépassement du pire cas d'une étape = compte rendu.

**M4 — Le repli sur une autre carte sort de la lettre de la ligne.** Devis l. 67-68 : « Repli si aucune 4090 ≤ 0,90 USD/h : RTX
5090 (plus rapide), puis RTX 3090 (signalée comme écart de matériel au rapport, aucun critère changé) ». La ligne dit « une RTX 4090
à 0,90 USD/h au plus ». Toute autre carte est une dépense hors de la ligne : nœud de Lazar, pas un repli de l'autrice. Le devis est
de plus incohérent avec son propre argument : il retient la 4090 parce que les effets faibles dépendent du matériel (l. 65), puis
tient la 5090 pour un repli sans écart.
- ancien : la phrase citée ; nouveau : « Si aucune RTX 4090 ≤ 0,90 USD/h : rien ne part ; message à la mère (nœud : autre carte). »
  L'option (b) de la « Décision demandée » (l. 132) est à présenter comme un changement de la ligne, pas comme une variante.

**M5 — La description de `HF_TOKEN` sous-estime l'exposition, et la décision n'est pas couverte par la ligne.** Devis l. 118-120 :
« La machine doit donc recevoir `HF_TOKEN` pour le seul téléchargement du modèle (étape 1), puis `env -u HF_TOKEN` pour tout le
reste ». Par la voie du volet A (`--env` à la création, commande v14, « Secrets »), une clé reste (a) dans la configuration de
l'instance chez le loueur **jusqu'à la destruction**, (b) dans l'environnement du processus d'entrée pendant toute la location, et
elle est réinjectée à chaque relance du conteneur par le loueur ; `env -u` ne la retire qu'aux processus enfants. Détail et
alternatives au § « Accès » ci-dessous. La ligne ne prévoit qu'un secret (celui du volet A) ; le devis renvoie à la mère (l. 120) :
à porter aussi à Lazar si la clé est celle de son compte (portée de la clé inconnue de moi, non lue).
- ancien : la phrase citée ; nouveau : « `HF_TOKEN`, s'il est passé par `--env`, reste dans la configuration de l'instance et
  dans l'environnement du processus d'entrée jusqu'à la destruction ; `env -u HF_TOKEN` et `HF_HUB_OFFLINE=1` en écartent le code
  voisin et la course, sans le retirer de la machine » ; puis les options, sans trancher.

**M6 — « Le fichier `-causal.pt` entier » dans le brut scellé ne peut pas sortir par la voie du volet A.** Devis l. 92. La sortie
publiée de `measure` pour Qwen3-8B pèse 2,9 Go (addendum v3 § 3) ; celle de Llama sera du même ordre. La seule voie de sortie du
volet A est une poussée git vers le dépôt privé (pas de ssh, commande v14), et l'hébergeur refuse les fichiers de plus de 100 Mo
(limite connue de moi, non revérifiée ici). Telle qu'écrite, la leçon 1 ferait échouer la poussée finale, donc retarderait la
destruction ou perdrait le brut. Or le recalcul de n (texte gelé B.1) et tout rejeu partent de ce fichier.
- ancien (l. 92) : « et le fichier `-causal.pt` entier (cibles, `top_doc`, `top_pos`) » ;
- nouveau : dire la taille attendue et la voie : soit l'empreinte du fichier et un extrait rejouable de taille bornée (par pôle :
  r par lentille et par cible, motif d'écart, `top_doc`, `top_pos`, doses), le recalcul de n étant fait sur la machine ; soit une
  autre voie de sortie, qui est une décision de la mère (compte ou dépôt neuf = nœud). À essayer à blanc avant le feu.

## Mineurs

1. **Statut de la ligne** (l. 5 et l. 129) : « ce devis sert à un GO neuf de Lazar » et « Accorder la tranche B-α ». La ligne
   GO-2026-11-14-06 existe (12 USD, R-2725). Ancien : « sert à un GO neuf de Lazar » ; nouveau : « sert à la demande de feu sous
   GO-2026-11-14-06 ; deux points demandent un mot à part : le second secret, et toute carte autre que la RTX 4090 ».
2. **Code de B0 mal attribué** (l. 26) : « notre code de B0 (`controles_b0_v2.py`, scellé : « nombre de couches lues == 31 »,
   « aucune matrice identité aux couches 0 à 27 ») ». Ce fichier ne porte que les provenances, la liste `catalog.kept` et les jetons
   de début ; les contrôles « 31 couches » et « identité » sont dans `verdicts_b_alpha_v3.py` (l. 233 et autour). Nouveau : citer
   les deux fichiers, chacun pour ce qu'il fait.
3. **Arguments de l'étape 3** (l. 27) : l'addendum v3 (§ 4) impose `--docs dclm=40000,zh=8000,code=8000,chat=8000` (le défaut est
   dix fois plus petit) et le dépôt, avant la passe, du fichier de provenance « chat » au nom de Llama (correctif
   `correctif-provenance-chat-llama-v2.md`). Le devis ne les nomme pas. À écrire à l'étape 3 : sans eux, la mesure change de corpus.
4. **Étape 2 incomplète à la lettre** (l. 26) : manquent « autres clés consignées », le compte des doubles jetons de début (addendum
   § 4) et la convention « clé l = sortie de la couche l » lue dans `config.yaml` et `CREDIT.md` (liste d'arrêt). L'essai des crochets
   de pilotage et d'ablation sur un Llama miniature est cité, mais je ne trouve aucun fichier d'essai correspondant dans la copie :
   à écrire et contre-lire avant le feu, et à nommer au § 6.
5. **B.3 est « avant la course », pas « avant `score` »** (l. 124) : « gardes de B0 et de B.3 avant `score` ». Le texte gelé dit
   « Avant la course […] Résultats consignés avant la course ». Les essais existent (`tests/test_neuron_lens_verdicts_b_alpha_v3.py`).
   Nouveau : « garde de B0 avant toute passe ; B.3 consigné avant la location, rejoué sur la machine avant `measure` ».
6. **Renvoi de lignes** (l. 30) : « défauts l. 373-384 » ; le texte gelé dit « lignes 374 à 377 de la copie ». Les valeurs sont les
   mêmes ; aligner le renvoi, et écrire « positions [16, T) ».
7. **Leçon 1 et code voisin** (l. 90-93) : verser les r par pôle est un ajout au brut, sans critère touché, **à condition** qu'ils
   viennent de notre code lisant `-causal.pt`. Si l'ajout passe par une retouche de `score` dans `causal_lens.py`, c'est une
   quatrième retouche de l'arbre voisin, hors des correctifs déclarés (écart 14 du texte gelé) : écart daté, contre-lu, donc nœud.
   À dire dans le devis. Je ne vois aucun autre point des leçons 1 à 5 qui touche un critère ou une mesure gelée.
8. **Où se prononcent les verdicts** (l. 31) : l'étape 7 calcule les verdicts sur la machine. Le texte gelé ne dit pas qui lit ; au
   volet A la lecture a été faite par un lecteur neuf après destruction. À écrire : la machine applique le code scellé et pousse le
   brut ; la lecture reste à un lecteur neuf ; les déclencheurs « trop beau » et « tout négatif » sont évalués avant la destruction
   (lien avec M2).
9. **Prix : stockage et trafic** (l. 60) : « stockage compris dans `dph_total` ». Au volet A, le prix lu sur l'instance (0,3956)
   dépassait celui de l'offre (0,3747) de 5,6 % pour 80 Go (journal v2, 16:52:56Z) ; B-α demande 150 Go. Le relevé ne porte pas le
   prix du trafic (≈ 25 Go descendants). Nouveau : « attendu ≈ 1,2 à 2,4 USD ; prix retenu = `dph_total` lu sur l'instance, exigé
   ≤ 0,90, sinon destruction ; prix du trafic de l'offre relevé avant création ».
10. **Durée de l'amorce** (l. 24) : « mesuré : 47 min ». La mesure vaut pour un autre fichier d'exigences et sa cause est restée
    inconnue (`pip -q`, sans trace) : c'est une mesure d'un autre montage, à dire « mesuré au volet A, transposé ». Donner la valeur
    du `timeout` de `pip` (l. 103) : c'est elle qui borne le pire cas de 1,5 h.
11. **Durée de la passe** (l. 29) : publiée pour Qwen3-8B (36 couches × 12 288 neurones) ; pour Llama c'est une transposition
    (32 × 14 336, volume voisin), à dire « publié, transposé ». La fumée « writes no tables » (`06_activations.py` l. 608) : l'écriture
    des tables par 16 processus n'est éprouvée qu'à la fin de la passe complète ; un échec là coûte une passe de plus si la reprise
    ne garde pas l'état. À couvrir par l'essai à blanc ou par une ligne du pire cas.
12. **Reprises** : `measure` et la passe gardent un état toutes les 10 minutes (`--save-minutes`) ; le pire cas ne compte qu'une
    réinstallation. Dire que l'entrée idempotente **reprend** ces états au lieu de recommencer, et l'essayer à blanc.
13. **Bornes de la minuterie** : le script v3 refuse une durée hors de 600 à 108 000 s (bornes posées pour 10 USD entre 0,30 et
    0,90 USD/h). Avec un plafond de 12 USD ou un prix sous 0,30, la durée peut sortir des bornes (non armée, arrêt) : à vérifier si
    M2 (a) est retenu.
14. **Vitesses relatives** (l. 51-58) : colonne « supposé », sans source ; sans effet si la RTX 4090 est gardée.

## Réponses aux six points demandés

**(1) Suite du texte gelé.** Ordre du devis : amorce, téléchargements, B0, corpus et comptes, fumée, passe complète, `measure`,
`score --lenses logit,J,npJpp,npR`, recalcul de n, verdicts, intervalles, poussées ; c'est l'ordre du plan d'analyse B.1. Chaîne,
commit voisin `849bfe16`, correctifs (1) et (2), graines (B.2), lentilles, cibles avec et sans critère : conformes. Aucun seuil,
aucune bande, aucune règle de lecture n'est réécrit. Manques : M1 (partie 2), M2 (audits R4), mineurs 3 à 6. Leçons du volet A :
aucune ne touche un critère, sous la condition du mineur 7.

**(2) Durées et coût.**

| étape | source réelle | remarque |
|---|---|---|
| 0 amorce | mesurée au volet A (47 min), transposée | cause inconnue ; bornée par le `timeout` à écrire |
| 1 téléchargements | supposée | ≈ 20 Go ; plausible à 300 Mb/s et plus (16 Go ≈ 7 min à 300 Mb/s) |
| 2 B0 | supposée (essais du volet A : 30 s) | plausible |
| 3 corpus, comptes | publiée (« minutes ») | avec les arguments de l'addendum (mineur 3) |
| 4 fumée | supposée | plausible |
| 5 passe complète | publiée pour Qwen3-8B sur RTX 4090, transposée | pire cas 2,5 h ≈ 2,1 fois le publié |
| 6 `measure` | supposée | ordre de grandeur refait : 256 passes de 272 séquences de 64 jetons, puis 256 passes d'ablation ; 0,3 à 1,0 h plausible |
| 7 `score`, verdicts | supposée | processeur ; plausible |
| 8 poussées | mesurée au volet A | sous réserve de M6 |

Le pire cas (8,8 h, plus une réinstallation) est prudent pour la course seule ; il ne compte ni les audits R4 (M2), ni une attente
de scellement (M1), ni une passe refaite (mineur 11). Plafond proposé (10) sous la ligne (12) : oui ; il ne contient son pire cas
qu'à un prix sous ≈ 0,87 USD/h (M2). Compte rendu à 60 % et arrêt dur à 90 % : présents (l. 78-79), conformes à la liste d'arrêt,
mais tardifs aux prix du jour (M3).

**(3) Carte.** Le texte gelé ne nomme aucune carte (recherche faite sur « RTX », « 4090 », « bf16 », « matériel » : rien). Une RTX
3090 n'est donc **pas** un écart au texte gelé. C'est un écart à la **ligne de GO** (M4) et aux conditions de la référence publiée
(passe en bf16 sur RTX 4090, rejouée sur une autre carte par les auteurs). Le risque de fond est réel mais non mesuré entre ces deux
cartes : les constats (l. 207-209) comparent une RTX 4090 et un processeur graphique d'une autre famille, et disent que les effets
**faibles** en dépendent ; B-7 (« ablate win », couches 0 à 15, effets faibles, seuil 0,25) est la mesure la plus exposée, B-2 et B-3
la moins. La RTX 4090 retire un facteur non contrôlé pour quelques dizaines de centimes : choix du devis fondé.

**(4) Argent et arrêt.**

| mécanisme | état au volet A | repris dans le devis |
|---|---|---|
| destruction `-y`, entrée fermée | éprouvée en vrai (03:05:04Z) | oui, l. 82 |
| preuve d'absence avec témoin (`suivi_vast_v6 absente … --temoin`) | éprouvée en vrai (03:05:10Z) | oui, l. 82 ; nommer le témoin |
| minuterie v3 | armée et réarmée en vrai, **jamais échue en vrai** (essai v3 à blanc) | oui, l. 80 ; meurt à chaque redémarrage du conteneur de la session |
| garde v4, compte rendu à 60 % | tournée en vrai, **jamais déclenchée** (dépense 4,04 USD sur 10) ; 13 essais ; lecture d'une instance détruite non éprouvée sur le vrai outil (réserve S-11 de la v14) | oui, l. 78 |
| arrêt dur à 90 % | jamais déclenché en vrai | oui, l. 79 |
| relevé du crédit | éprouvé en vrai à chaque contrôle | oui, l. 83 |
| course figée (R-2800) | appliquée en vrai, jamais déclenchée | oui, l. 84, adaptée (`gpu_util` attendu > 0 aux étapes 4 à 6 ; l'écriture des tables et `score` sont sur processeur, la règle « et » le couvre) |
| entrée idempotente, `pip` minuté | **neufs** (défauts constatés au volet A) | l. 100-104 ; à essayer à blanc |

Manquent au § 3, présents dans la commande v14 : une seule instance ; prix retenu = `dph_total` lu après création ; branche de
résultats exigée absente (dite au § 5) ; journaux de la minuterie et de la garde commités ; arrêt de la minuterie et de la garde par
PID vérifié par leurs arguments. Changé : rien dans les outils ; les seuils sont recalculés pour 10 USD (M2, M3, mineur 13).

**(5) Accès.**
- *Jeton du programme* : même voie qu'au volet A (l. 111-115 ; commande v14, « Secrets » ; amorce v6 l. 62 et 172-204) : `GH_TOKEN`
  par `--env`, en-tête HTTP seulement, course sous `env -u GH_TOKEN`, essayé à blanc sous sept formes. Réserve reprise : il écrit
  sur tout le dépôt. Nouveau pour B-α : le code voisin tourne plus longtemps et plus largement sur la machine (étapes 2 à 7).
- *`HF_TOKEN`*, risques décrits, sans trancher :
  1. **Durée** : passé par `--env`, il reste dans la configuration de l'instance chez le loueur et dans l'environnement du
     processus d'entrée jusqu'à la destruction (2,4 à 8,8 h, plus toute attente), et revient à chaque relance du conteneur. « Pour
     le seul téléchargement » décrit l'usage, pas la présence.
  2. **`env -u` suffit-il ?** Il suffit contre une fuite par héritage (journaux d'une bibliothèque, manifeste, vidage de
     l'environnement). Il ne suffit pas contre un code qui chercherait la clé : le code voisin tourne sous le même utilisateur que
     le processus d'entrée et peut lire l'environnement de celui-ci ; l'exploitant de la machine louée peut lire la configuration
     du conteneur. Ajouter `HF_HUB_OFFLINE=1` après le téléchargement, ne jamais ouvrir de session du hub (qui écrirait la clé dans
     un fichier), et retirer aussi l'autre nom que les bibliothèques lisent (`HUGGING_FACE_HUB_TOKEN`).
  3. **Traces** : la sortie brute de l'outil du loueur porte les variables de l'instance ; le suivi v6 a `HF_TOKEN` dans sa liste
     (l. 42) et refuse toute sortie qui porte la valeur, **si** la variable est présente dans le shell du suivi et fait au moins
     8 caractères, et hors des caractères d'échappement (limite déclarée de la v14). Les sept formes de l'essai à blanc sont à
     rejouer pour cette clé (arbre, objets git, journaux, manifeste, état poussé). L'interface du compte du loueur l'affiche.
  4. **Portée** : inconnue de moi. Une clé d'écriture ou de compte entier exposerait, en cas de fuite, tout ce que le compte peut
     lire et écrire sur le hub ; une clé à lecture seule, restreinte à ce dépôt à accès contrôlé, créée pour la course et révoquée
     à la destruction, borne le dommage à la lecture d'un modèle déjà accordé. Créer ou révoquer une clé est un acte de compte.
  5. **Alternatives sans clé sur la machine** : (a) adresses de téléchargement signées et à durée courte, résolues par la session
     avec la clé puis transmises à la machine (pas de clé sur la machine ; durée de validité à vérifier ; demande une voie de
     transmission après création, absente sans ssh) ; (b) empreintes des poids lues par la session (métadonnées, avec la clé),
     fixées avant location, et téléchargement depuis une copie publique à empreintes égales — mais le texte gelé nomme le dépôt et
     la révision, et la liste d'arrêt dit « licence différente → arrêt » : ce serait un écart, donc un nœud ; (c) pour B0 seul,
     rien à gagner : l'essai du correctif (1) demande le tokeniseur sous licence, donc l'accès, dès B0.
  Le relevé d'accès du devis (l. 117 : 200 avec la clé, 401 sans) a été fait par l'autrice ; je ne l'ai pas rejoué.

**(6) B0 et partie 2.** B0 est prévu (étape 2), avant le corpus et avant toute passe : conforme à « étape B0 d'abord ». Les
téléchargements (étape 1) le précèdent, ce que B0 exige (tokeniseur, lentilles) ; les poids du modèle pourraient n'être téléchargés
qu'après B0, ce qui éviterait 16 Go si B0 arrête la course (choix d'exploitation, sans effet sur un critère). La partie 2 de
l'addendum **n'est pas prévue** (M1). Ordre à écrire : 1 téléchargements → 2 B0 (essais des correctifs, lecture des trois lentilles,
31 couches, identité, `config.yaml`, `CREDIT.md`, crochets) → 3 corpus et comptes → **partie 2 scellée et poussée, avec les sorties
de B0** → 4 fumée → 5 passe → 6 `measure` → 7 `score`.

## Ce que je n'ai pas fait
Aucune exécution du code voisin ni du nôtre (lecture seule) ; aucun essai rejoué ; aucun relevé de prix ni d'accès rejoué ; limite
de taille de fichier de l'hébergeur et durée de validité des adresses signées non revérifiées (connaissance générale) ; puissance de
calcul de `measure` estimée de tête, non mesurée ; contre-lectures 1 à 13 du volet A non relues ; journal de la fille lu par
recherche de mots seulement.

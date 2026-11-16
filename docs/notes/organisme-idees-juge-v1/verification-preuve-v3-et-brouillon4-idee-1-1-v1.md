# Vérification (R2) — preuve v3 de l'idée 1.1 et brouillon 4 du préenregistrement v2 (poids du nul) — v1

- Contre-lecteur : sous-agent neuf de la session mère. Je n'ai écrit ni la preuve (v1, v2, v3), ni ses contre-lectures, ni
  les brouillons 1 à 4 du préenregistrement v2, ni leurs contre-lectures, ni la synthèse, ni les rendus des angles, ni leurs
  réfutations, ni le juge, ni les nuls v8 et v9.
- Date (UTC) : 2026-11-15, de 21:57 à 22:08 environ (`date -u`). Dépôt `/home/user/controle-ia-travail`, `main`, tête
  `ea88c31e` (commit du brouillon 4, 21:56:30). Aucun commit, aucune poussée, aucun appel réseau ni payant ; aucune pièce
  modifiée. Rien lu sous `diag/`, `runs/` de 7a ou 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/`. Aucune valeur de clé lue ; ni `env` ni `printenv` ; aucun `pytest`.
- **Textes vérifiés** (empreintes recalculées, égales à leurs compagnons, `scellement verifier` : OK) :
  - preuve v3 : `docs/notes/organisme-idees-juge-v1/preuve-idee-1-1-poids-du-nul-v3.md`,
    `a481c873a317a710923ee6134f410f45b5dd14392738b768ecad0fdffb3547c1` ; outils
    `preuve-idee-1-1-poids-du-nul-v3-outils/` (`3bd417e7c8bfbc533ddfed38d86153c02ec70a17d29e941156bdc61b4b882249`,
    `e45aecb8b178114d372c5c4b96e85037c009cc784d5df531433ee00d045a2306`) ;
  - brouillon 4 : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon4.md`,
    `4adac754a3e90c4c2dedaaf3cf2ed83bde04761670c6c67cfbdd2f5ac21ede26`.
- **Pièces de comparaison** : preuve v2 (`83789a45be3745f75527d92f943e7232e455157de8bce4080357b5597e204013`) ; sa
  contre-lecture (`c7f6dccffc5b22d8ab397df2080b2ab99e3e15c5c134882466202cb7250d04c9`, ci-dessous « contre-lecture de la
  preuve ») ; brouillons 2 et 3 (`5a78dbe759421888f10cd5bcae57f4fa1ed03d0cef162944a9bd17ca98a9e6ae`,
  `ea6def091f54323e3f8f0510522618554e08a2828c557e0102941ea8978206b8`) ; contrôle du brouillon 2
  (`2ea76193b0841fef6f387b01ead468c89e98ec2ed15923711ee444ca9e384ac0`).
- Calculs : `.venv/bin/python -I -B` (Python 3.13, numpy, scipy du dépôt), processeur seul, dans un sous-dossier neuf du
  bloc-notes de la session (`verif-v3-b4/`), hors du dépôt.

## 0. Verdicts

**Preuve v3 : suffit** comme préalable 2. Les neuf couples sont appliqués ; le différentiel ne contient rien d'autre que
ces couples, la section 11.2 annoncée et la section 16 ; aucun énoncé de taille n'est changé (théorèmes 1, 8, 10 (a), 11,
lemmes 3 à 6, proposition 2 : texte identique à la v2, ou seulement restreint au lemme 4 (v)) ; H7′ est posée sur les trois
énoncés de valeur arrêtée qui en ont besoin. Sept mineurs de texte (section 2), dont un chiffre inexact (« au plus 0,75 »
pour 0,7546) : aucun ne touche un énoncé que le préenregistrement emploie ; à porter dans une version suivante ou un
erratum, sans bloquer.

**Brouillon 4 : scellable après corrections.** Deux majeurs de texte, sept mineurs, aucun de conception (section 4,
couples « ancien → nouveau »). Le différentiel 2 → 3, jamais vérifié à part, est fidèle (section 3). Holm à 61, P2 à 39,
seuils, empreintes, validateur : exacts. Aucune voie vers un signe positif n'est ouverte par Hn ni par la lecture bornée de
Hg.

## 1. Preuve v3 — ce qui a été vérifié

### 1.1 Les neuf couples, un par un

| couple | appliqué ? | où, et écart au texte demandé |
|---|---|---|
| 1 (M1, § 0, point 6) | oui | texte demandé repris ; ajout du chiffre 0,1016 (voir mineur p3) |
| 2 (M1, § 11) | oui | § 11.1 : les deux phrases fausses retirées, texte demandé repris presque mot pour mot ; § 11.2 neuf |
| 3 (M1, § 14) | oui | ligne « ouvert … pour les deux types » ; deux lignes ajoutées (lissage négatif prouvé, lissage positif non établi), cohérentes |
| 4 (M2, H4, H7) | oui | H4 récrite selon le texte demandé (avec « au plus 4,3·10⁻¹⁰ nat, 23 valeurs sur 144 », chiffres de la contre-lecture) ; « D_t ne lit que y_1..y_t » sorti de H7 et porté par une hypothèse nommée H7′ : forme différente du couple, même contenu |
| 5 (M2, corollaire 1, théorème 10 (b), proposition 13) | oui | « sous H7′, sinon non établi » dans les trois ; « départs chaînés et arrêts communs du lot » au théorème 10 |
| 6 (m1, P6) | oui | mot pour mot |
| 7 (m2, lemme 4 (v)) | oui | avec la division par zéro dite |
| 8 (m3, en-tête) | oui | v2 datée de 20:45 à 21:21 ; v3 « scellée à 21:50 » (fichier daté de 21:50, commit 21:51:19 : cohérent) |
| 9 (m4, H2) | oui | mot pour mot |

**Le différentiel v2 → v3 contient-il autre chose ?** Non, hors : titre, statut, auteur, renvoi au dossier d'outils v3,
ligne de pièce pour la contre-lecture, liste « Ouvert » du § 0 (H4, H7′ ajoutées), titres 11.1, 11.2, 11.3, renvoi de la
section 13, section 15 (consigne au lecteur de la v3), section 16 (tableau des neuf couples). Tous découlent des couples.

**Énoncés de taille.** `diff` ne montre aucune ligne changée dans les énoncés et les preuves du théorème 1, de la
proposition 2, des lemmes 3, 5, 6, de la proposition 7, des théorèmes 8 et 11, du théorème 10 (a). Rien de renforcé. Les
seuls énoncés affaiblis sont ceux de valeur arrêtée (corollaire 1, théorème 10 (b), proposition 13), par H7′, comme
demandé ; l'égalité d'événements de la proposition 13 reste « sans réserve », à raison.

**H7′, exactement là où il faut ?** Oui pour les trois énoncés nommés ; nulle part dans un énoncé de taille. Le
corollaire 9 n'en porte pas : c'est juste sur le code (j'ai relu `nul_filles_v2.valeurs_ajustees`, l. 154 à 186 : les
membres log-linéaires sont ajustés instant par instant sur les t premières issues, départ à chaud depuis l'instant
précédent ; les membres ordinaires sont des cumuls), mais ce n'est plus écrit comme hypothèse depuis que H4 a perdu sa
première moitié (mineur p2).

### 1.2 Rejeu du script du lissage négatif

`verif_lissage_negatif_v3.py` copié dans un dossier neuf du bloc-notes et lancé là : **sortie identique à l'octet**
(`cmp`), empreinte `e45aecb8…`, sortie d'erreur vide, 9,5 s. Les chiffres du § 11.2 sont ceux de la sortie, sauf p1.

### 1.3 Mon programme à part (fractions exactes, bibliothèque standard seule ; annexe A)

Fenêtre 1, lissage −3/5, deux issues, blocs de 2, monde p = 1/2, lois constantes, plancher 10⁻¹² porté exactement :

| quantité | preuve v3 | moi |
|---|---|---|
| espérance de la valeur e, premier bloc | 4/3 | 4/3 + 3,0·10⁻¹³ (4/3 à la limite du plancher nul) |
| espérance, blocs suivants | 3/2 | 3/2 − 3,3·10⁻¹³ (3/2 à la limite) |
| P(richesse ≥ 20 à une fin de bloc), n = 8 ; n = 12 | 0,0625 ; 0,1016 | 1/16 ; **13/128** = 0,101562 |
| sup_α P/α, n = 2 ; 8 ; 12 | 1,3333 ; 2,6667 ; 5,3333 | 1,333333 ; 2,666667 ; 5,333333 |
| plus grand certificat | 1 | 1,000000000000 |

Retrouvé. Une précision de fond (p6) : le 3/2 tient à la convention du plancher. Quand la première issue du bloc répète
la dernière du bloc précédent, la carte et sa projection sont toutes deux au plancher sur cette issue, leur rapport vaut 1
et le bloc rend e = 1 ; sans plancher ce serait 0/0 (P5 fausse).

### 1.4 Empreintes

32 empreintes entières dans la preuve v3 : toutes égales au fichier nommé.

## 2. Preuve v3 — mineurs (ancien → nouveau), non bloquants

- **p1 — chiffre inexact, § 11.2.** La sortie donne 0,7407, 0,7546 et 0,6844 pour le rapport sous gel (fenêtre 1).
  - ancien : « et rapport au plus 0,75** »
  - nouveau : « et rapport au plus 0,7546** »
- **p2 — corollaire 9 : adaptation de W^reste non écrite.** Depuis la réécriture de H4, plus rien ne dit que W^reste_t ne
  lit pas l'avenir, ce dont « τ est un temps d'arrêt » a besoin.
  - ancien : « W_τ ≤ W^{F*}_τ (ou ≤ Λ_τ), arrêt optionnel. ∎ »
  - nouveau : « W_τ ≤ W^{F*}_τ (ou ≤ Λ_τ), arrêt optionnel ; W^reste vérifie H7′ sur le code lu (membres ordinaires
    cumulés ; membres log-linéaires ajustés instant par instant sur les t premières issues, [NF2] l. 154 à 186 ; aucun
    membre par morceaux). ∎ »
- **p3 — § 0, point 6 : le 0,1016 sans son cadre.**
  - ancien : « probabilité exacte 0,1016 sur 12 tirages (section 11.2) »
  - nouveau : « probabilité exacte 0,1016 (13/128) sur 12 tirages, pour le terme projeté seul, à deux issues, blocs de 2,
    famille des lois constantes (section 11.2) »
- **p4 — « la même loi » : portée de l'écart.** 8,8·10⁻¹³ est le chiffre du cas essayé (deux issues, 8 tirages). À trois
  issues, 200 tirages, c = 70, je mesure sur le code réel 1,97·10⁻¹² ; et, sur une issue épuisée, les deux lois sont au
  plancher mais renormalisées différemment (rapport de 11 à 60).
  - ancien : « (écart au plus 8,8·10⁻¹³, le plancher) »
  - nouveau : « (écart de l'ordre du plancher : au plus 8,8·10⁻¹³ sur le cas essayé ; nul tant qu'aucun compte n'atteint
    c ; sur une issue épuisée, les deux lois sont au plancher, à un facteur de renormalisation près) »
- **p5 — tableau des pièces.** La ligne « [CL3] » est insérée entre [B1] et « sa contre-lecture … [CL2] », qui semble
  maintenant contre-lire [CL3]. Nouveau : placer la ligne [CL3] après la ligne [CL2].
- **p6 — « espérance exacte 4/3, 3/2 »** : exacte à la limite du plancher nul (écarts de 3·10⁻¹³) ; le 3/2 tient à la
  convention « plancher sur plancher = 1 » (1.3). À dire en une ligne.
- **p7 — théorème 1 énoncé pour La et Ld, employé pour J8 et J9** (par le théorème 10 et par le préenregistrement). La
  preuve ne se sert de rien de propre à La. Hérité de la v2. Nouveau : « pour la bibliothèque La (ou Ld, ou toute
  bibliothèque gelée qui vérifie H4 : J8, J9) ».

## 3. Brouillon 3 — différentiel 2 → 3, vérifié à part

| remarque du contrôle du brouillon 2 | appliquée ? |
|---|---|
| N1 (cran 4, cellules fatales) | oui, les deux couples mot pour mot |
| N2 (route « à défaut ») | **par une autre voie que le couple**, déclarée : retour à la route première (banc v9 versé), affirmation fausse retirée, « pas de jeu » récrit. J'ai vérifié sur les copies : l. 68 du banc v9 charge le banc v8, constantes lues sur lui (l. 81 et 82), imports listés présents dans `94bfd92` ; les sept classes de `test_nul_v9.py` sont celles que le texte nomme (plus la classe d'appui `Dossier`) ; `GrainesEtPreenregistrement` lit bien un dossier `prereg/`, `FICHIERS_GELES`, et lance un interpréteur fils (l. 559 à 718). Un reste : N-2 ci-dessous |
| n1 | oui, récrit sans perte ; chiffres recalculés par moi : 0,323 ; 0,765 ; 0,931 ; ajout « jamais de graines rejouées », déclaré |
| n2 | oui, les deux couples |
| n3, n4, n5, n7 | oui, mot pour mot (avec le renvoi) |
| n6 | oui, porté au statut sous la forme que le brouillon 3 impose |

Rien d'autre dans le différentiel 2 → 3 que l'en-tête, deux lignes de pièces, le statut et l'entrée « Contre-lecture 3 ».
`controle_ia.prereg.problemes` sur le brouillon 3 : 0 problème.

## 4. Brouillon 4 — différentiel 3 → 4

### 4.1 Ce qui tient (vérifié)

1. **Différentiel.** Chaque bloc changé relève d'un des quatre changements annoncés ou de leurs suites déclarées à
   « Contre-lecture 4 » (ligne d'arrêt « exception d'une loi de carte », P6 à la « Garantie », exigence de code du lemme 4,
   coût à 30 lignes). Rien d'autre.
2. **Renvois à la preuve v3**, tous contrôlés sur le texte `a481c873…` : § 8 (lemmes 5 et 6, théorème 8) ; § 7 et § 11
   (garde P4) ; § 9 et § 10 ; théorème 1 ; théorème 8 ; théorème 10 (a) et (b) ; théorème 11 ; § 10.2 (1,4) ; proposition
   2 ; § 4 (p1 à p6) ; § 3 (P1 à P6) ; H4, H5, H7, H7′, P6 ; corollaires 1 et 9 ; lemmes 3 et 4, exigence de code ; § 6
   (La, Ld) ; § 11.1, § 11.2, § 11.3 ; § 15. Tous existent et disent ce que le texte leur fait dire, à deux précisions
   près (n3 ; et p7 pour « J8, J9 par le théorème 1 »).
3. **Réserve H7′.** Écrite à la « Garantie » pour J9-D40, étendue à J9, La, Ld (corollaire 1), exclue pour J9-P et La-P
   (corollaire 9), reprise dans « Ne décide pas ». « Aucun critère de ce plan n'en dépend » : exact, toutes les lectures
   portent sur la promotion de la carte seule (énoncés de taille).
4. **Ligne Hn sur le code** (copie de travail de `selection_pari.py`, `outils.py`, `__init__.py` de `94bfd92`, empreintes
   conformes, dans mon sous-dossier, lancée depuis un autre dossier ; annexe B) : acceptée par `valider_loi` ; type
   `moyenne_glissante`, donc refusée par la garde « refus » ; **aucune division par zéro** sur 241 600 appels (604 suites
   × 200 instants × avec et sans gel par blocs de 25), dénominateur « longueur − 210 » jamais nul de 0 à 200 ; toutes les
   lois finies, positives, de somme 1. **Égale à `sans_remise` [70, 70, 70] à 2·10⁻¹² près, pas à 0** : N-1.
   Forme écartée « fenêtre 1, lissage −0,6 » à trois issues : [1/3, 1/3, 1/3] puis [0 ; 0,5 ; 0,5], retrouvé.
5. **Comptes.** Taille : Q7 7, Q8 8, Hs 4, Hm 4, Hg 4, Hn 4, H7 1 = 32 ; Holm 22 + 7 + 32 = **61** ; P2 7 + 32 = **39** ;
   fatales 22 + 12 = 34 ; 30 lignes, `i_ligne` de 0 à 29, Hn en 29, indices antérieurs gardés ; « 25 autres lignes » sans
   mémoire : exact. Coût : 30 000 × 7 à 9 s = 58 à 75 heures d'un cœur, 19 à 25 heures sur trois processus : exact.
6. **Seuils.** Script du brouillon 4 rejoué : **sortie identique à l'octet** (`7119c6f4…`) ; script et sortie recopiés à
   l'annexe A égaux aux fichiers versés, octet pour octet. À 61 cellules : ≤ 29 et ≥ 74, ≤ 38 et ≥ 63 ; inchangés.
7. **Règle de réduction.** Inchangée hors « 61 » : les crans 2, 3 et 5 portent sur les 15 lignes V, le cran 4 sur quatre
   cellules rapportées ; aucune cellule fatale, aucune cellule de Holm (celles de Hn comprises), ni la principale.
8. **R3.** Hn : exclue de ρ, des gains réunis, de I ; sa dent (i) est « rapportée, non bloquante », sa réfutation mène à
   « réserve, sans autre suite » ; elle rend le verdict « nécessaire, montrée » plus exigeant (une cellule sous gel de
   plus), jamais plus facile ; à l'étape 0 ses comptes sont inscrits sans bloquer et sans qu'aucun seuil en dépende. Hg :
   la lecture est seulement bornée (« ne dit rien des lissages négatifs » ; « aucune de ces lectures ne conclut que la
   grammaire est sûre sans garde »). Aucune voie vers un signe positif.
9. **Préalable 2.** Bloquant et net : « tant que cette vérification manque, ou si elle fait tomber un de ces énoncés : pas
   de jeu » ; ligne d'arrêt « préalable 1 ou 2 non levé ». Mon verdict de la section 0 le lève, énoncés debout.
10. **Chiffres exploratoires cités pour Hn** : 206/2 000, 1/60 et 4/60, 18/60, 904/2 000, 0/13 000, réglages 0, 4, 7 :
    conformes à la réfutation de l'angle « projection », § 5 (M1 = membre linéaire seul ; M3 = toutes les coupures).
11. **R1.** Hypothèse, prédictions chiffrées et signes (sauf n1), métrique, seuils, plan d'analyse, critères de lecture
    gelés, liste d'arrêt : présents. `controle_ia.prereg.problemes` : **0 problème**.
12. **Empreintes.** 51 empreintes entières ; 50 égales au fichier nommé ; la 51ᵉ (`a9f9594e…`) est déclarée reprise,
    fichier non rouvert. Bancs v8 et v7 présents, v7 égal à la copie sous `orchestrateur-v52b/`.
13. **Aucun identifiant de modèle** dans le brouillon 4, la preuve v3 ni leurs outils (recherche sur les noms de familles
    et de fournisseurs : rien).

### 4.2 Majeurs (ancien → nouveau)

**N-1 — Hn : « écart 0 » est faux.** Sur le code réel, l'écart entre la loi de Hn et `sans_remise` [70, 70, 70] est nul
(10⁻¹⁶) tant qu'aucun compte n'atteint 70, puis monte à 1,97·10⁻¹² ; cela arrive sur 1 676 de mes 2 000 suites uniformes
(premier épuisement au plus tôt à l'instant 150, médian 188). Sur une issue épuisée, les deux lois sont au plancher mais
renormalisées différemment (rapport de 11 à 60), et la log-vraisemblance cumulée diffère alors de plusieurs nats (jusqu'à
41 sur mes 50 suites). Sans effet attendu sur une promotion (chaque carte y perd plus de 25 nats), mais c'est un chiffre
faux dans un préenregistrement.
- ancien : « vérifié par moi sur `proba` de la copie `94bfd92`, 200 instants, écart 0, avec et sans gel) »
- nouveau : « vérifié sur `proba` de la copie `94bfd92`, 200 instants, avec et sans gel : écart nul tant qu'aucun compte
  n'atteint 70, puis au plus 2·10⁻¹² ; sur une issue épuisée les deux lois sont au plancher, à un facteur de
  renormalisation près, sans effet attendu sur une promotion) »

**N-2 — Préalable 1 : une porte reste ouverte** (phrase née au brouillon 3). « Si l'une ne l'est pas, elle est listée de
même, avec sa raison » laisse le développeur déclarer « non rejouable » une classe qui échoue, ce que la règle « pas de
jeu si un essai d'origine rejoué échoue ou ne peut pas être importé » interdit deux phrases plus loin.
- ancien : « sont attendues rejouables telles quelles ; si l'une ne l'est pas, elle est listée de même, avec sa »
  (suivi, à la ligne, de « raison. »)
- nouveau : « sont attendues rejouables telles quelles ; si une de leurs méthodes ne l'est pas **pour l'une des deux
  raisons écrites ci-dessus et elles seules** (elle lit le dépôt tiers ou ses empreintes ; elle lance le banc comme
  programme ou écrit hors du dossier de travail), elle est listée de même, avec sa raison ; un essai d'origine qui échoue
  ou ne s'importe pas pour toute autre raison n'est jamais déclaré « non rejouable » : pas de jeu. »

### 4.3 Mineurs (ancien → nouveau)

- **n1 — P12 : signe et objet de la prédiction sur Hn non écrits** (R1 : chiffre et signe).
  - ancien : « cartes de la grammaire Hm et Hg sans garde ; Hs (aveugle par construction) | »
  - nouveau : « cartes de la grammaire Hm et Hg sans garde ; Hs et Hn (aveugles dans le juge complet, par construction) ;
    Hn, terme projeté de la famille linéaire seule | »
  - ancien : « | + ; + ; sous α ; sous α ; nul | H7, terme projeté sans garde ≥ 0,20 »
  - nouveau : « | + ; + ; sous α ; sous α ; nul (Hs et Hn, juge complet) ; + (Hn, terme linéaire) ; sans signe (Hn, toutes
    les familles : rapporté) | H7, terme projeté sans garde ≥ 0,20 »
- **n2 — Les quatre cellules de Holm de Hn répètent celles de Hs.** Même monde, même loi à 2·10⁻¹² près, autres graines,
  et J9-P sous gel y est aveugle comme sur Hs. À dire : ce que Hn apporte est la quantité (i), pas une épreuve de taille
  neuve.
  - ancien : « cellule de Holm « J9-P avec gel » sur Hn porte sur J9-P complet, carte gelée. »
  - nouveau : « cellule de Holm « J9-P avec gel » sur Hn porte sur J9-P complet, carte gelée. Les quatre cellules de Hn
    portent sur le monde et, à 2·10⁻¹² près, sur la loi de Hs, avec d'autres graines : elles répètent Hs ; ce que Hn
    ajoute est la quantité (i). »
- **n3 — Renvoi de la monotonie.** La proposition 2 n'énonce pas « J9 sous J8 » ; elle le donne par La, à l'écart
  résiduel près, ou par sa preuve.
  - ancien : « monotonie ([PREUVE3], proposition 2 (a) et (b)), b_r ≤ a_r. »
  - nouveau : « monotonie ([PREUVE3], proposition 2 (a) et (b) et leur preuve : un dénominateur qui contient plus de
    membres est plus haut ; exact quand les membres communs sont calculés par le même code, ce que garde la ligne d'arrêt
    « monotonie violée »), b_r ≤ a_r. »
- **n4 — Quantité (i) de Hn : règle de promotion à écrire.**
  - ancien : « terme projeté de la **famille linéaire seule**, Σ_b log e_{lin,b} ; dent **rapportée, »
  - nouveau : « terme projeté de la **famille linéaire seule**, Σ_{b ≤ t/25} log e_{lin,b}, compté promu s'il atteint
    log(1/α) à un instant t ∈ T₈ ; dent **rapportée, »
- **n5 — Imports des bancs v8 et v7.** Je les ai relevés (lecture seule) : v8 emploie `pole.nul_filles_v2`, `pole.nul_v8`,
  `pole.selection_pari`, `pole.cycle` (`instants_reguliers`), `pole.outils` (`ecrire_json_scelle`, `manifeste`,
  `sha256_fichier`, `verifier_scelle`) ; v7 emploie `pole.nul_filles_v2`, `pole.selection_pari`, `pole.controles_pari`
  (`_dirichlet`, `_fixe`, `_frequences`, `borne_wilson`), `pole.cycle` (`appliquer_multiplicite`, `instants_reguliers`),
  `pole.outils` (`ecrire_json_scelle`, `graine_derivee`, `manifeste`). Tous présents dans `94bfd92`, noms compris.
  - ancien : « n'ai pas relevé les imports des bancs v8 et v7 (à faire par le développeur ; un module manquant dans
    `94bfd92` ferait échouer »
  - nouveau : « n'ai pas relevé les imports des bancs v8 et v7 ; le lecteur du brouillon 4 l'a fait, tous les modules et
    noms sont présents dans `94bfd92` (à confirmer par le rejeu ; un module manquant ferait échouer »
- **n6 — Ligne d'auteur.**
  - ancien : « ni la preuve en ses versions 2 et 3, ni sa contre-lecture, ni la version 1, ni sa contre-lecture, ni la
    preuve, »
  - nouveau : « ni la preuve en ses versions 1, 2 et 3, ni la contre-lecture de la preuve v2, ni la version 1 de ce
    préenregistrement, ni sa contre-lecture, »
- **n7 — Statut de la preuve, à mettre à jour au scellement.** Trois passages disent la preuve v3 « pas encore vérifiée
  par un lecteur neuf » (pièces, « Réserves communes », préalable 2). Le texte qui fera foi doit citer ce rapport et son
  empreinte, et ajouter une entrée « Contre-lecture 5 » ; je ne donne pas de couple, la mère choisit la forme.

**Remarque sans couple, pour la mère.** À l'étape 0, le compte de Hn sous gel est inscrit « sans bloquer ». Un compte
élevé sous gel y signalerait un défaut de code que le jeu ne verrait pas, la cellule de Holm de Hn portant sur J9-P
complet, aveugle. Écrire une suite serait un changement du plan : je le signale, je ne le demande pas.

## 5. Incidents de ma main

- Un `ls -la` lancé sur le bloc-notes partagé de la session a listé les noms des fichiers d'autres agents ; aucun n'a été
  ouvert ni touché. Tous mes fichiers sont dans le sous-dossier neuf `verif-v3-b4/`.
- Pour retrouver les fichiers des empreintes citées, j'ai calculé l'empreinte des fichiers suivis par git sous `docs/`,
  `prereg/` et `src/`, `docs/notes/bras-attaque/` exclu. La liste a compris 32 fichiers de
  `docs/notes/integration-bras-attaque-v1/`, dossier qui n'est pas dans la liste interdite mais en est voisin : empreintes
  seules, contenu jamais affiché, aucune ne correspondait ; liste supprimée ensuite.
- Un premier appel à `scellement verifier` avec un motif trop large (compagnons compris) s'est arrêté sur « compagnon du
  compagnon absent » ; relancé sur les onze fichiers utiles : onze OK.
- La première lecture de la contre-lecture de la preuve a été tronquée à l'affichage ; relue ensuite par parties
  (sections 0 à 7 lues ; annexe de sorties survolée).
- Non refait : les parties A à E du script de la v2 (rejouées à l'octet par la contre-lecture de la preuve) ; la mesure
  de 4,3·10⁻¹⁰ nat sur `maximiser_par_lots` (reprise, non rejouée) ; aucune simulation de Hn à l'échelle du juge.

## Annexe A — mon programme en fractions exactes (sortie)

```
n= 2 E[e_B] par bloc (exact, plancher 1e-12) : ['1.333333333333630']
      écart à 4/3 (bloc 1) : 2.963e-13
      P(richesse >= 20 à une fin de bloc) = 0 = 0.000000 ; sup_alpha P/alpha = 1.333333 ; plus grand certificat 1.000000000000
n= 8 E[e_B] par bloc (exact, plancher 1e-12) : ['1.333333333333630', '1.499999999999667', '1.499999999999667', '1.499999999999667']
      écart à 4/3 (bloc 1) : 2.963e-13 ; écart à 3/2 (bloc 2) : -3.333e-13
      P(richesse >= 20 à une fin de bloc) = 1/16 = 0.062500 ; sup_alpha P/alpha = 2.666667 ; plus grand certificat 1.000000000000
n=12 E[e_B] par bloc (exact, plancher 1e-12) : ['1.333333333333630', '1.499999999999667', '1.499999999999667', '1.499999999999667', '1.499999999999667', '1.499999999999667']
      écart à 4/3 (bloc 1) : 2.963e-13 ; écart à 3/2 (bloc 2) : -3.333e-13
      P(richesse >= 20 à une fin de bloc) = 13/128 = 0.101562 ; sup_alpha P/alpha = 5.333333 ; plus grand certificat 1.000000000000
plancher 1e-3 : bloc 1 = 4/3 + (2.951e-04) ; bloc 2 = 3/2 + (-3.332e-04)
plancher 1e-6 : bloc 1 = 4/3 + (2.963e-07) ; bloc 2 = 3/2 + (-3.333e-07)
plancher 1e-12: bloc 1 = 4/3 + (2.963e-13) ; bloc 2 = 3/2 + (-3.333e-13)
plancher 1e-24: bloc 1 = 4/3 + (2.963e-25) ; bloc 2 = 3/2 + (-3.333e-25)
```

Méthode : `fractions.Fraction` partout ; loi (compte + λ)/(longueur + K·λ), plancher puis renormalisation ; projection
sur les lois constantes = moyenne des lois réalisées du bloc ; certificat = plus grande moyenne de q_s(k)/φ(k) sur les
deux sommets ; 2ⁿ suites.

## Annexe B — ligne Hn sur la copie de travail de `proba` (sorties)

```
valider_loi : Hn acceptée, Hs acceptée ; types Hn ['moyenne_glissante'] ; lit l'historique : True
suites : 604 (dont 522 où un compte dépasse 70) ; appels 241600 ; exceptions 0 ; lois non finies, non positives ou de somme ≠ 1 : 0
plus grand écart |Hn − sans_remise[70,70,70]| : sans gel 1.971e-12 ; avec gel (historique arrêté au début du bloc de 25) 1.967e-12
dénominateurs nuls pour une longueur de 0 à 200 : []
trajectoire_loi (chemin du juge, Cache), 50 suites uniformes de 200 : plus grand écart de log-vraisemblance cumulée 4.093e+01
fenêtre 1, lissage −0,6, 3 issues : sans historique [0.333333, 0.333333, 0.333333] ; après [0] [0.0, 0.5, 0.5]
lissage −70 (entier) et −70.0 : même loi : True
2000 suites uniformes de 200 : écart avant tout épuisement (tous comptes < 70) 1.110e-16 ; après 1.917e-12
suites où un compte atteint 70 avant la fin : 1676/2000 ; instant médian du premier épuisement 188 ; plus tôt 150
suites où une issue épuisée est tirée (carte au plancher) : 1546/2000
sur une issue épuisée : rapport Hn/Hs des probabilités au plancher de 11.00 à 60.00 ; sur les autres issues, |log rapport| au plus 1.917e-12
```

Les 604 suites : 300 uniformes, 300 de mondes déséquilibrés, 4 construites (constante ; 70 zéros puis des uns ; 70, 70,
60 ; alternée). Graines fixes de `random.Random`, sans portée de résultat : essai de code seulement.

## Fichiers produits

Ce rapport et son compagnon `.sha256`. Mes programmes et sorties sont restés dans le bloc-notes de la session, hors du
dépôt. Aucun fichier du dépôt n'a été modifié.

# Contre-lecture (R2) — préenregistrement du pilote d'une génération (conditionnelles MR-2), brouillon 1 — v1

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), lecteur neuf, autre modèle que l'auteur (Claude Opus 5.5). Je n'ai écrit
  ni ce préenregistrement, ni la conception v4, ni leurs programmes, ni la contre-lecture de la conception v4.
- **Heures** (relevées par `date -u`) : début 2026-11-13 09:37:25 UTC ; fin de rédaction 2026-11-13 09:43:52 UTC.
- **Interdits** : `interdits-communs-v2.md` lu en entier avant tout ; aucun chemin interdit ouvert ni listé ; aucune clé lue ;
  aucune écriture git ; aucun appel, aucune dépense ; aucun refus rencontré. Recherches : seulement dans des fichiers nommés.
  Calculs : un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`, Python 3.13.18, numpy 2.5.3, au brouillon de
  session ; rien d'écrit dans le dépôt hors de ce fichier et de son compagnon.
- **Limite de lignée** : autre modèle que l'auteur, même maison (Claude). Fable 5.2 est aussi l'un des quatre proposeurs du pilote.

## Verdict (une ligne)

**Scellable après corrections (11 exigées), puis après les préalables de sa section 12 ; pas tel quel** : la mesure est juste,
calculable et rejouée à l'identique, aucun signe n'est visé, mais ce qui décide vraiment (la valeur ponctuelle donnée au banc)
n'est pas écrit comme une règle, et plusieurs conventions non fermées penchent toutes du côté de l'hypothèse.

## Pièces lues et vérifiées

| pièce | empreinte | contrôle |
|---|---|---|
| `pilote-v1/preenregistrement-pilote-conditionnelles-v1-brouillon1.md` | `ef90476f32c8e16b950f725ebcfcc2c3a8aefd7b30c392bd574993b42b75af0e` | égale au compagnon ; lu en entier |
| `pilote-v1/outils/mesure_pilote_v1.py` | `0d806aca4b8f21c777c836fe39286326aa6753b060782123f9c117f32cf491a4` | égale au compagnon ; lu en entier |
| `pilote-v1/outils/seuil_pilote_v1.py` ; `devis_pilote_v1.py` | `14eecfcc…` ; `99d5d677…` | égales aux compagnons ; lus en entier |
| `pilote-v1/sorties/` (quatre sorties et leurs sorties standard) | compagnons | toutes égales |
| `conception-monde-riche-doublons-v4.md` | `47e38ec0663320e8c68011130c3f1b8e1017969cbb740d30c83a78eb5db0a6dc` | égale ; lue en entier |
| `contre-lecture-conception-v4-v2.md` (ajoutée par la mère en cours de tâche) | `16da94d4519bf72b1b3672d98099ee482db01ea2d8403f15068e04b4c2a54c97` | égale ; lue en entier |
| `outils-v4/monde_riche_v4.py` | `4b165847…` | lu en entier |
| `outils-v1/monde_riche_outils_v1.py` (grammaire, oracle, attribution, K1, jeu planté) ; `outils-v2/devis_multi_generations_v2.py` (constantes) | — | extraits lus |
| `registres/decisions.md` (R-2500 à R-2503), `registres/go.md` (forme, GO-2026-11-13-01 et -02), `prereg/gabarit-preregistrement-v1.md`, `src/controle_ia/prereg.py` | registres vivants | lus |

Non lus : le différentiel du code v67, le brouillon 3 de la course, la note de décision (cités par le texte ; je m'appuie sur ce
que le texte en dit). L'arbre de l'organisme n'est pas dans cette session.

**Rejeux** (09:39:21 → 09:39:39 UTC) : `essai`, `puissance`, `seuil_pilote_v1.py`, `devis_pilote_v1.py` relancés tels quels :
champs `resultat` de l'essai et de la puissance **identiques** aux sorties scellées ; sorties du seuil et du devis identiques
à l'octet (`16cd1004…`, `dcae0286…`).

**Calculs de ma main** (09:39 → 09:41 UTC, non scellés, à refaire par l'auteur) : intervalles de Clopper-Pearson recontrôlés
(formes fermées aux bords, probabilités de queue égales à 0,025) ; lecture composée pilote puis banc ; cartes de forme réelle
sur le monde d'essai ; sorties P-1 et P-0 de la règle.

## Corrections exigées

**E-1 — Écrire la règle qui décide vraiment : la valeur ponctuelle portée au banc.** Le texte présente P-1 comme la seule
réfutation et dit sa puissance faible. Mais sous P-2 le banc reçoit p_c ponctuel, et le banc ne mesure rien sur les proposeurs
(point E-1 de la contre-lecture de la conception) : son issue est presque une fonction du seul compte du pilote. Avec le modèle
de `seuil_pilote_v1.py` et 8 unités :

| appels qui trouvent sur 8 | p_c ponctuel | intervalle | règle de garde tenue au banc (probabilité) |
|---|---|---|---|
| 0 | 0 | [0 ; 0,074] | 1,00 |
| 1 | 0,022 | [0,0005 ; 0,117] | 0,93 |
| 2 | 0,047 | [0,005 ; 0,161] | 0,10 |
| 3 | 0,075 | [0,015 ; 0,209] | 0,0003 |
| 6 et plus | ≥ 0,206 | borne basse ≥ 0,069 | P-1 |

La décision réelle est donc « au plus 1 appel sur 8 → course probable ; 2 ou plus → pas de course », avec ces taux (calcul) :

| p vrai par carte | 0,01 | 0,02 | 0,03 | 0,051 | 0,075 | 0,10 | 0,15 | 0,25 |
|---|---|---|---|---|---|---|---|---|
| banc favorable (au plus 1 sur 8) | 0,92 | 0,77 | 0,60 | 0,32 | 0,14 | 0,05 | 0,006 | 0,000 |
| P-1 (texte) | 0,0000 | 0,0001 | 0,0004 | 0,006 | 0,035 | 0,107 | 0,365 | 0,843 |

À écrire dans les sections 4.2 et 8 : (i) cette table, refaite par le programme ; (ii) que l'hypothèse vraie à 0,02 mène au
refus du banc près d'une fois sur quatre, et qu'une hypothèse fausse à 0,051 passe une fois sur trois ; (iii) que le meilleur
résultat possible (0 sur 8) laisse une borne haute de 0,074, au-dessus de p_max : **le pilote ne peut jamais établir H-P**, il
ne peut que ne pas la réfuter ; (iv) si Lazar veut que la décision se prenne sur le ponctuel (lettre de R-2501) ou sur une
borne. La phrase « le pilote ne réfute qu'une hypothèse franchement fausse » est vraie de P-1 seul et fausse de la chaîne
entière : elle doit être remplacée.

**E-2 — Définir « appel répondu » et fixer un minimum d'appels.** Rien ne dit ce qu'est un appel « répondu ». Tel que codé,
un appel répondu sans aucune carte admise (réponse tronquée, six cartes refusées au gardien) compte « ne trouve pas » : biais
vers l'hypothèse. Et la règle rend P-2 avec n'importe quel nombre d'appels : essayé, un seul appel répondu donne P-2 avec
P_CACHÉE = 1,0 (s'il trouve) ou 0,0 (sinon) ; à deux unités ou moins, P-1 est impossible. Exigé : (i) « répondu » = réponse
brute complète (raison d'arrêt normale) et au moins une carte admise et évaluable ; sinon « échec » ou « tronqué », hors du
dénominateur, compté à part ; (ii) minimum écrit d'avance pour lire P-1 ou P-2 (par exemple au moins 6 appels répondus sur 8 en
bras A et au moins 3 par monde), sinon P-0 ; même minimum pour reprendre p_v du bras B, sinon 0,25 dit ; (iii) la borne de
jetons de sortie de chaque appel, fixée et suffisante pour six cartes d'un arbre à 48 feuilles, écrite au texte ; (iv) un
appel manquant dans le fichier des cartes est un refus du programme (les 8 ou 16 appels attendus sont vérifiés).

**E-3 — Fermer l'unité et le dénominateur.** Le dénominateur est « appels répondus × conditionnelles du monde » : il vaut 8, 12
ou 16 selon le tirage secret, et dans un monde à chaîne les deux unités d'un même appel partagent les mêmes six cartes (la
seconde a pour condition la première). Clopper-Pearson les traite comme indépendantes : intervalle trop étroit. Exigé : mesure
principale sur **une unité par appel** (la première conditionnelle de chaque monde, celle dont la condition n'est pas une
conditionnelle), n = 8 connu d'avance ; seconde d'une chaîne rapportée à part, comme le bras B le fait déjà. Et dire que
8 appels sont 4 proposeurs × 2 mondes : deux appels d'un même modèle ne sont pas deux tirages indépendants ; la puissance
calculée est une borne optimiste.

**E-4 — Proposeurs inégaux : la valeur commune penche vers l'hypothèse.** La survie d'une conditionnelle après une génération
est le produit des (1 − q) des quatre proposeurs ; le modèle la remplace par (1 − q moyen)⁴, toujours supérieur ou égal.
Exemple : un proposeur trouve toujours, trois jamais → 2 sur 8, p_c = 0,047 < p_max, issue P-2, survie du modèle 0,32, survie
vraie 0. Exigé : rapporter la survie par produit des q̂ par proposeur à côté de la valeur commune ; le banc tourne aussi avec les
probabilités par proposeur ; lecture écrite d'avance si les deux divergent (réserve et nœud de Lazar). Ce n'est pas un
classement ni une décision de composition (N-058 tenue).

**E-5 — Ce qui est servi aux proposeurs (point E-3 de la contre-lecture de la conception) : trancher et geler.** Le pilote
gèle « aucune description des sortes d'effets ni de la famille » (section 3.3, C-6, K-5). C'est cohérent avec le brouillon 3 et
avec la lecture du contre-lecteur de la conception, et c'est le choix le plus sévère pour l'hypothèse inverse (il ne souffle
rien). Mais : (i) il contredit la ligne « §3.6 » de la section 6 de la conception v4 (« le gabarit dit l'existence possible
d'une condition sur le signe d'un trait »), que le texte cite comme faisant foi, sans le dire ; (ii) R-2503 pose ce choix comme
« à trancher par Lazar avant toute mesure » et il n'est pas dans Q-P1 à Q-P4 ; (iii) rien ne lie la course au même gabarit,
alors que p_c ne vaut que pour le texte servi. Exigé : question neuve Q-P5 (ne rien dire, recommandé ; ou annoncer) ; empreinte
du gabarit servi au bloc gelé ; phrase « la course et le banc n'emploient p_c que si la course sert ce même gabarit » ; dire
si le gardien du pilote ouvre la profondeur à 3 conditions (voir E-6).

**E-6 — Le gardien et l'évaluation ne doivent pas pouvoir cacher une conditionnelle.** Une carte refusée au gardien ou non
évaluable « ne porte pas ». Si le gardien v67 borne la profondeur, le nombre de feuilles ou les types (la loi servie du bras B
est une `transformee`), une carte qui porte la conditionnelle peut être refusée : biais vers l'hypothèse, invisible. Et la
mesure évalue par `M.probas` des outils de conception, pas par l'évaluateur de la chaîne. Exigé, deux lignes de code de plus :
**C-16** — avant tout appel, pour chaque monde privé, les lois de référence (« K1 + conditionnelle » calibrée, monde entier,
loi servie du bras B) passent le gardien du pilote, sinon arrêt ; **C-17** — égalité des probabilités entre l'évaluateur de la
chaîne et `M.probas` sur un jeu fixe de cartes de la grammaire servie (écart ≤ 10⁻⁹), et toute carte admise mais non évaluable
par la mesure est une réserve rapportée, relue à l'audit.

**E-7 — Programme de la mesure : essais et dépendances manquants.** (i) L'essai scellé n'exerce que l'issue P-2 ; P-1, P-0 et
le minimum de E-2 ne sont essayés nulle part (R5). Je les ai exercés : 4 sur 4 → P-1 ; aucun appel en bras A → P-0 ; le code est
juste, l'essai est à ajouter. (ii) L'empreinte `0d806aca…` ne gèle pas ce que le programme importe (`monde_riche_v4.py`, outils
v1 à v3, `seuil_pilote_v1.py`, par chemin relatif) : empreintes des modules importés vérifiées au lancement ou portées au bloc
gelé. (iii) Une septième carte fait refuser toute la mesure (« emplacement 1 à 6 ») alors que le texte la dit « refusée au
gardien et comptée » : écrire que l'export l'écarte et la compte, ou l'accepter comme refusée. (iv) Le programme corrigé prend
un nom neuf (R12) ; la ligne π1 cite son empreinte.

**E-8 — Lecture écrite si la sensibilité contredit la principale.** Sur le monde d'essai, la porte à 0,75 · I se comporte
ainsi (conditionnelle E7, I = 0,054) : « K1 + conditionnelle » sans l'effet de sa condition, pente vraie : Δ/I = 1,82 ; pente
× 0,5 : 0,80 (porte) ; × 0,4 : 0,60 (ne porte pas) ; seuil de la condition déplacé à 0,5 : 1,09 ; à 1,0 : 0,49 ; une seule
branche : 0,78 ; mais **monde entier avec la pente × 0,5 : 0,48 (ne porte pas)**. La porte est donc atteignable par des cartes
de la grammaire servie, mais le rapport Δ/I dépend du reste de la carte : une carte meilleure peut porter moins. C'est la
règle de capture de la conception, la même qu'au banc : je ne demande pas de la changer. Exigé : si l'issue ou le compte
diffère entre τ (0,75) et τ' (0,25), ou entre l'unité appel et l'unité carte, c'est une réserve écrite et un nœud de Lazar
avant le banc ; le banc tourne aux deux valeurs.

**E-9 — Devis, lignes et défauts.** Les sommes sont justes (réponse 6). Mais : (i) R-2501 parle d'un pilote à « ≈ 20 USD au
pire » ; le dessin recommandé (bras A et B) en demande 39 : à dire en tête de la note à Lazar ; (ii) Q-P1 porte un « défaut
sous 48 heures : (b) » qui double la dépense : une dépense est un nœud, sans défaut ; (iii) la ligne π1 cite `0d806aca…`, qui
changera (E-7).

**E-10 — Secret et isolement : deux précisions.** (i) La graine « sha256(secret ∥ phrase ∥ empreinte ∥ « pilote » ∥ r ∥ t),
entier ≥ 2⁶⁴ » n'est pas calculable sans ambiguïté (codage et séparateurs des champs, lecture de « ≥ 2⁶⁴ »), et `generer_v4` a
déjà son propre compteur de tirage (`spawn_key`) : écrire la fonction exacte, l'essayer sur un secret public de développement,
dire laquelle des deux mécaniques tire les 8 essais. (ii) La conception de la famille est dans le dépôt et deux des proposeurs
sont de la lignée qui l'a écrite et relue : le témoin d'isolement atteste aussi « aucun outil, aucun accès à un fichier ou à un
dépôt, aucun texte servi hors des pièces gelées ».

**E-11 — Forme R1, R4 et lecture.** (i) La section 4.1 ne dit pas la prédiction de l'auteur : écrire « attendu : p_c proche
de 0,02, soit 0 ou 1 appel sur 8 ; réfutation : selon E-1 ». (ii) Les déclencheurs de l'audit de symétrie sont chiffrés
(par exemple 0 sur 8 ; 2 ou plus sur 8) et l'audit « p_c = 0 » relit aussi **toutes les cartes refusées au gardien ou non
évaluables** ; l'audit est fait par un lecteur qui n'a écrit ni le texte ni le code. (iii) L'issue est lue par un sous-agent
neuf (esprit de R13 : elle commande 419 USD de course). (iv) Si le scellement passe par `controle_ia.prereg.sceller_prereg`,
les titres de niveau 2 doivent être ceux du gabarit (« Hypothèse », « Prédiction chiffrée et signe attendu », « Métrique »,
« Seuil », …) : les titres numérotés actuels seraient refusés ; sinon dire par quelle voie il est scellé.

## Corrections suggérées

- **S-1** Proposer à Lazar une variante « 4 mondes, bras A seul » (16 appels, même pire que le dessin recommandé : 20 + 19
  USD) : la lecture composée de E-1 passe, à p = 0,075, de 0,14 à 0,03 de faux « favorable », et P-1 de 0,04 à 0,10. Le
  bras B, à 8 appels, ne donne qu'une valeur grossière d'un paramètre secondaire.
- **S-2** Dire que p_v du bras B est mesuré sur une archive de deux lois où la condition saute aux yeux ; en génération 2 de la
  course l'archive en compte une dizaine : p_v n'est pas la même quantité.
- **S-3** `seuil_pilote_v1.py` : rapporter aussi le point de bascule à probabilité 0,5 (0,034, mon calcul) ; p_max = 0,051
  cumule deux prudences (règle tenue ≤ 0,05 et borne basse à 97,5 %), d'où la faible puissance de P-1.
- **S-4** Comparer la borne basse à p_max avant l'arrondi à quatre décimales (sans effet pour n ≤ 16 : bornes les plus proches
  0,0502 et 0,0526, vérifié).
- **S-5** Libellé faux possible : si le bras B est joué mais sans appel répondu, la sortie dit « bras B non joué ».
- **S-6** Un emplacement non entier lève une erreur non rattrapée (pas un refus propre) ; la liste d'arrêt ne dit pas quoi
  faire si la mesure « une seule fois » s'arrête sur une erreur.
- **S-7** Heures hors du corps empreinté de la sortie de la mesure (le texte le demande en C-14 ; le programme les y met).
- **S-8** `p_min_vue` est calculé et jamais employé : le retirer ou dire son rôle.
- **S-9** La sortie de la mesure laisse lire le nombre de composantes par classe de chaque monde (dénominateurs) : sans
  gravité, à dire puisque les mondes ne sont « jamais publiés ».
- **S-10** Q-P2 à Q-P4 : ajouter la ligne « défaut sous 48 heures » du format de décision.

## Réponses aux huit questions

**1. R1 complet ?** Presque. Présents : hypothèse (H-P), métrique, seuil, plan d'analyse, critères gelés, liste d'arrêt,
audit R4. Manquent : la prédiction de l'auteur dite comme telle (E-11) ; la règle qui décide en pratique (E-1) ; la définition
de l'appel répondu et le minimum (E-2) ; les marqueurs de la section 18 (dits par l'auteur).

**2. La mesure p_c est-elle juste et calculable ?** Juste dans sa forme : l'unité appel est le bon choix (cartes d'un appel
dépendantes ; (1 − q)⁴ = (1 − p)²⁴), la transformée est exacte et monotone, Clopper-Pearson est correctement codé (recontrôlé).
Calculable sans ambiguïté par le programme, **rejoué à l'identique**. Trois défauts : dénominateur variable et unités
dépendantes dans les mondes à chaîne (E-3) ; valeur commune à quatre proposeurs inégaux (E-4) ; appel sans carte compté comme
« ne trouve pas » (E-2). La porte à 0,75 · I est atteignable par des cartes écrites dans la grammaire servie (E-8), avec la
réserve qui y est dite ; une pente sans condition ne porte pas (−0,70, rejoué).

**3. Règle et seuil ; puissance ; le pilote vaut-il sa dépense ?** p_max = 0,051 recalculé juste ; écrit d'avance ; ses
approximations vont contre la règle de garde (donc contre l'hypothèse de l'auteur), sauf l'égalité des proposeurs (E-4). La
puissance de P-1 est bien dite, mais ce n'est pas la bonne table : la décision passe par le banc (E-1), et là le pilote
tranche bien plus net que le texte ne le dit, avec des erreurs des deux côtés qu'il faut écrire. **Oui, il vaut sa dépense** :
39 USD au pire (≈ 15 attendus) contre 419 engagés sur une valeur sans pièce placée à un facteur 1,5 de la bascule ; il sépare
0,02 de 0,10 et plus, et il éprouve la chaîne à quatre fournisseurs que la course exige de toute façon. Il ne vaut pas plus
qu'un tri grossier : entre 0,03 et 0,06 il ne décide rien de fiable, et il ne peut pas établir l'hypothèse. Je préférerais
16 appels en bras A (S-1).

**4. Isolement, réponses brutes, secret, non-réutilisation.** Bien conçus : secret propre au pilote, engagé avant la phrase,
mondes hors dépôt, jamais publiés ni réutilisés, réponses brutes scellées avant extraction, témoin par session, aucune
reprise. À fermer : fonction de graine (E-10 (i)), contenu du témoin (E-10 (ii)), vérification des empreintes des mondes par
le programme et non seulement à la main (E-7).

**5. Code manquant C-1 à C-15 : complet ?** Non. Manquent : C-16 et C-17 (E-6) ; le gel des modules importés par la mesure
(E-7) ; la borne de jetons de sortie et la définition de la troncature (E-2) ; l'outil de rapprochement des coûts et celui du
tirage des cartes de l'audit (graine) ; les proposeurs factices de l'essai à blanc pour les quatre relais ; l'outil de
rapatriement qui prouve qu'aucun monde ne sort. Le reste est cohérent avec ce que le texte dit du code v67, que je n'ai pas lu.

**6. Devis et lignes.** Arithmétique juste et rejouée : crédits 4 × (3 + 2) = 20 ; Argon 4 × 2 = 8, Astra 8, machine 3 = 19 ;
attendus 9,60 et 5,30 ; bras A seul 10 et 11. Lignes π1 et π2 au format du registre (8 colonnes, type calcul, échéance), non
inscrites, conditions bien liées. Réserves : E-9 ; le pire n'est une borne que si chaque relais coupe à sa part (C-7, C-9, à
essayer) ; prix et identifiant d'Astra supposés (dit).

**7. Q-P1 à Q-P4.** Bien posées et au format, sauf : défaut de Q-P1 à retirer (dépense), défauts absents ailleurs (S-10).
Manquent une question sur ce qui est servi (Q-P5, E-5) et la décision « ponctuel ou borne » de E-1 ; S-1 mérite d'être
offerte.

**8. R3 et R4.** R3 : tenu dans l'intention — trois issues, chacune avec sa suite, aucune reprise, mesure une seule fois,
conflit d'auteur dit. Mais cinq conventions non fermées poussent toutes p_c vers le bas, donc vers l'hypothèse de l'auteur :
appel sans carte (E-2), carte refusée ou non évaluable (E-6), valeur commune (E-4), porte haute (E-8), et l'issue par défaut
P-2 nourrie du ponctuel (E-1). Aucune n'est un réglage après lecture ; ensemble elles doivent être fermées avant le
scellement. R4 : audit écrit dans les deux sens, c'est bien ; déclencheurs à chiffrer et lecteur à nommer (E-11).

## Ce que le pilote gèle sur le point E-3 de la conception (demande de la mère)

Il gèle **ne rien dire** : grammaire seule (`par_sous_population`, `si_sinon` sur un trait ou une sous-population), aucune
description des sortes d'effets ni de la famille, aucune consigne diversifiante. C'est cohérent en soi et avec K-5 ; ce n'est
**pas cohérent avec la conception v4, section 6**, qu'il cite, et le choix n'a pas été porté à Lazar comme R-2503 le demande.
La probabilité mesurée ne vaudra que pour ce gabarit : la course doit servir le même (E-5).

## Réserves de cette contre-lecture

- Un seul monde d'essai (graine publique de développement) pour les cartes de forme réelle ; aucune carte d'un vrai proposeur.
- Tables de E-1 : calcul de ma main sur le modèle approché de `seuil_pilote_v1.py`, non sur le banc simulé.
- Code v67, brouillon 3 et note de décision non lus ; la liste C-1 à C-15 est jugée sur la cohérence du texte.

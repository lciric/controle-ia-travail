# Contre-lecture du préenregistrement du crible (iii), brouillon 4 — tour 1 de cette lecture (quatrième du crible) — v1

- Lecteur : sous-agent neuf du modèle C (R2), qui n'a écrit aucune des pièces ; l'auteur de la pièce est du modèle A ; les
  corrections seront écrites par le modèle A. Heure de rédaction : 2026-11-16, 14:16Z à 14:26Z (`date -u`).
- Pièce lue en entier : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon4.md`,
  `f30bd0f1c46cbbd3597fdf005bb6a372d0e9f039e2eedd7c3c3e7bb74667e8dd`.
- Pièces comparées : brouillon 3 `crible-iii-brouillon3.md`, `bd1aff342bfc8f9842c27b688a354e3a24ea1b9029ae1119f092fc793ad4f7a3` ;
  rapport du tour 3 `contre-lecture-crible-iii-tour3-v1.md`,
  `b785115660011d1f6a1d5dc93d883a1bfca2c0f1bdbd82e29a1b2be111001d1e`.
- Lu aussi : note des idées originales (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`, vérifiée par
  `sha256sum`), ligne R-2977 et lignes sur les cribles de `registres/decisions.md` (par `grep`), ligne GO-2026-11-15-06,
  N-058, N-045, procédure v14 au commit `2d35cafa…` (empreinte `2035562740ef…` vérifiée), texte scellé du pilote
  (candidat 6, `8aa33014667d…` vérifié, bloc gelé l. 317 à 336), gabarit, `controle_ia.prereg`.
- Non lu, par consigne : sortie du pilote MR-2 v14, dossiers `diag/`, `runs/`, `donnees/`, 7a, 7b, T0.6, T0.7, P3-bis, bras
  d'attaque, dossiers jetables du premier contre-lecteur.

## Verdict

**« corrections »** : 2 majeures (F-01, F-02), 6 mineures (F-03 à F-08). La pièce est solide : les 8 couples du tour 3 sont
appliqués à la lettre, les chiffres du devis, des seuils et des probabilités se recomptent, le validateur ne trouve aucun
défaut. Les défauts restants sont deux incohérences de lecture gelée (population de P2 sous « B tronqué » ; mot « frontière »
mal employé dans les verdicts) et des retouches de clarté. Aucun défaut n'appelle de refaire la conception. La pièce reste
**non scellable** tant que la forme du crible n'est pas inscrite par la mère (point 4 de « Choix et doutes ») : voir ma
recommandation en section 3, et l'urgence (avant la lecture de l'issue du pilote).

## 1. Les corrections du tour 3 sont-elles appliquées fidèlement ?

Oui. `diff` brouillon 3 → brouillon 4 : titre ; ligne d'en-tête du brouillon 4 ; statut (« contre-lu trois fois », nouvelle
phrase de E-02) ; III-5 (E-05) ; Taille (E-04, programme sous un nom neuf, graines `(96, s)`, 10 000 tirages, cellules) ;
table de mise à jour (E-06 : borne par appel relevée au plus à 2 × l'appel le plus long, plafond 3 600 s) ; « quatre valeurs »
(E-03, deux couples) ; point 4 de « Choix et doutes » (E-01, deux couples) ; section « Contre-lecture 3 » et « Tour suivant »
ajoutés. Les 8 couples du rapport du tour 3 sont retrouvés mot pour mot ; rien d'autre ne change que ce que l'en-tête déclare.
Les trois programmes `appliquer-corrections-crible-iii-brouillon{2,3,4}.py` sont égaux à leur compagnon. Les empreintes
citées des brouillons 1 et 2 et des rapports des tours 1 à 3 sont exactes et entières.

## 2. Réponses aux neuf points

**(1) R1.** Complet : hypothèse (H-iii, H-iii-a, H-iii-b), sept prédictions avec signe et chiffre (réserve F-03 sur III-1),
métrique, seuils (n_c ≥ 16, format 14, consigne 0,5, zone utile 10, P1, P2, Q), plan d'analyse, critères de lecture à sept étages,
liste d'arrêt de 18 lignes. Pas de porte de sortie après lecture : les réserves de l'étage 2 sont écrites d'avance, la mise à jour
d'après le pilote est une table close, les valeurs calculées avant le scellement sont listées (quatre) et sans effet sur un
seuil. Deux défauts : F-01 (population de P2 sous « B tronqué ») et F-04 (verdict « sans perte notable » presque inatteignable,
non dit).

**(2) R3.** Aucune voie vers un signe positif. P1 est la différence R_D − R_S, définie quand le bras standard ne couvre rien
(les dollars ne sont jamais nuls) ; le rapport ρ_DS indéfini n'est que rapporté. La marge de 0,5 composante par monde est fixée
avant toute donnée et justifiée (10 à 17 % de 3 à 5 composantes ; vérifié : 0,5/5 et 0,5/3). Les égalités du filtre sont rompues
par l'ordre lexicographique des tuples : sans biais d'indice, car le générateur permute les traits dans chaque monde (vérifié :
`rng.permutation` dans `monde_riche_v4.py`, ligne 105). Puissance de P2 à l'effet prédit : je trouve 0,35 à 0,50 à 20 mondes
(écart-type 1,2 à 1,0, approximation normale, borne à 97,5 %) et 0,42 à 0,58 à 24 : la pièce a raison de dire que « non tranché »
est l'issue la plus probable. Le test exact des signes : seuils recomptés (16 accords sur 20, 17 sur 21 et 22, 18 sur 23 et 24 ;
13 sur 16) et puissances (0,05, 0,24, 0,63, 0,96 à 20 mondes ; à 24 : 0,10, 0,39, 0,81, 0,99). Le bras « tout bon marché »
(B) qui réemploie la passe 1 de D : les deux bras reçoivent un texte égal à l'octet (garde sur le texte servi), la passe 1 est
comptée dans les dollars de chacun, aucune réponse de B ne revient vers D ; ils sont dépendants (dit), ce que le
rééchantillonnage apparié par monde respecte. Pas de fuite. Réserve : un monde où l'appel de B est tronqué sort de la population
principale (F-01).

**(3) Forme et crédits.** Voir section 3 (recommandation nette : la variante).

**(4) Devis.** Recompté. Appels : 5 par monde (Pr-2 : S, passe 2 de D, H ; Pr-1 : passe 1, B) = 100 ; 60 et 40. Plafonds de
session du bloc gelé : Pr-2 2,00, Pr-1 2,34, Pr-4 3,00 (l. 319 à 322 du texte scellé du pilote ; Pr-3 ne sert pas). Forme fidèle : crédits
60 × 0,80 = 48 attendus, 60 × 2,00 = 120 au pire ; Pr-1 40 × 0,25 = 10, 40 × 2,34 = 93,60 ; machine 0,30 et 3,00 ; total
58,30 et 216,60, comme écrit. Variante : Pr-4 60 × 1,60 = 96 et 60 × 3 = 180 ; Pr-2 40 × 0,80 = 32 et 40 × 2 = 80 ; machine ;
128,30 et 263,00 (dont 3,00 hors crédits), comme écrit. Sonde des gabarits : 2,00 + 2 × 2,34 = 6,68, attendu 1,06 à 1,41 comme
écrit. Lignes de GO : 120 + 93,60 + 3 = 216,60 ; + 6,68 = 223,28, égal au devis conditionnel. Jetons : sommes recomptées
(entrée 1,5 à 1,83 M et 5,36 M ; sortie 2,44 à 2,6 M et 6,78 M). Seule remarque : dans la ligne « Pr-2, S standard » la fourchette
haute (16,40) suppose environ 37 000 jetons de sortie par appel, alors que la colonne des jetons donne 0,60 M (30 000 par appel)
comme attendu : la fourchette vient des deux mesures de la course v67 (31 891 et 38 343) ; cohérent mais non dit (remarque
facultative R-1). De même la fourchette haute de B (9,00) dépasse ce que permet la borne de 36 000 jetons au prix public
(environ 7,9) : c'est la réflexion « ajoutée » chez Pr-1 ; non dit non plus (R-1). Cohérence avec GO-2026-11-15-06 : chaque
ligne est dans l'enveloppe, « essayé, non adopté » repris. **Cumul** : voir F-07 (point pour la mère) : avec la variante, la
somme des pires cas des cinq cribles dépasse 1 275.

**(5) Durée.** 60 h au pire en série (20 × 3 h) est bien au-delà de la minuterie de 17 h ; la pièce fixe **cinq files de
quatre mondes** (six pour 24), borne par appel 3 000 s, borne par monde 7 200 s (deux tours), garde de départ 10 h
(4 × 7 200 s + 2 h) qui remplace les 12 h 30 de la procédure v14 (12 h + 30 min pour 4 × 10 800 s) : arithmétique juste, marge de
7 h sous la minuterie. Concurrence : au plus 3 sessions de Pr-2 et 1 de Pr-1 par monde (B part après la passe 1), soit 15 et 5,
18 et 6 à six files : juste. Affectation des mondes aux files (r modulo F) fixée avant tout appel. **Code neuf nettement dit** :
lanceur, gabarits G1 et G2, filtre, ordre à deux tours, files parallèles, mesure ; le pilote joue quatre mondes en série (4 × 10 800 s,
procédure v14) et son lanceur ne sert pas tel quel ; environ deux jours d'agents ; essai à blanc à cinq files avec relais
scriptés, arrêt et nœud si les relais refusent la concurrence. Faisable, mais jamais éprouvé. Il manque la durée attendue à cinq
files (F-08).

**(6) Liste d'arrêt.** Chaque ligne a son essai sain et son artefact (R5) ; aucun repli silencieux ; graines par
`numpy.random.SeedSequence` avec clés `(r, 40)`, `(12, r, t)`, `(99, b)`, `(97, k)`, `(96, s)` sans collision, racine = empreinte
du texte, graine du monde par la fonction du pilote avec étiquette neuve ; manifeste de run cité. Minimum de 16 mondes complets
sur 20 ou 24 : la règle est écrite (13 accords sur 16, F-05 pour « fournisseur perdu en entier » non défini) ; probabilités
d'atteindre le minimum recomptées (p = 0,95 : 0,5149 et 0,9276 ; 0,97 : 0,8586 et 0,9961 ; 0,93 : 0,2249 et 0,7091 ; 0,90 :
0,0427 et 0,2943) : exactes aux arrondis de la pièce. Règle d'arrêt « mondes complets + non commencés < 16 » : juste.

**(7) Ablation de la frontière aux critères gelés.** Bien définie (δ_DB, étage 5) et sans contradiction avec N-045 point 3, qui
vise « les lectures des courses » : la pièce le dit (« Écarts ») et le réserve pour Lazar. **Mais** le mot « frontière » est mal
employé : N-045 (l. 50) nomme « espèces de frontière » les trois modèles Claude et Gemini de la configuration, Pr-1 compris ; B
(Pr-1 écrit à la place de Pr-2) ne retire donc pas la frontière, il remplace une espèce de frontière chère par une moins chère.
La question QO1 (frontière contre instruments locaux) n'est pas posée par ce crible, et la pièce note elle-même que
l'instrument local n'est « pas joué ». Voir F-02.

**(8) R7 et R8.** Aucun chiffre de l'état de l'art : les antériorités sont listées « à chercher » ou « à vérifier »
(LLM-Select, LLM-SR, FunSearch, AlphaEvolve, sélection gloutonne), la référence arXiv 2610.24597 (CADS) est bien celle de
N-067 (vérifiée dans le dépôt), le catalogue [CAT] C1 et C3 existe, la zone « filtre déterministe sans juge » est signalée
séduisante à vérifier plus durement. Citations obligatoires présentes avec empreintes entières (POPPER, Dwork, Ladder,
Co-Scientist : empreintes vérifiées). Rien à reprendre.

**(9) Validateur, identifiants, empreintes.** `controle_ia.prereg.problemes('…/crible-iii-brouillon4.md')` rend `[]` : le défaut
du tour 1 (section « Contre-lecture » sans ses deux empreintes entières) est corrigé. Aucun identifiant de modèle : seules les
clés de configuration exigées par le bloc gelé (R-2690). Empreintes vérifiées par `sha256sum` : note des idées originales,
relevé, recoupement, devis du pilote, conceptions v3 et v4, résumé v4, les quatre outils, N-058, N-045 v2, N-044, N-067,
question de la course, catalogue, les deux préenregistrements modèles, gabarit, `prereg.py`, les trois PDF et le PDF Co-Scientist,
brouillons 1 et 2, rapports 1 et 2 : toutes exactes. `registres/go.md` au commit `377a2a0c` : `4bcec4a0…` exact (la version du
working tree diffère, la pièce cite bien le commit). Texte scellé du pilote `8aa33014…` et procédure v14 `20355627…` exacts.
Les deux programmes de l'annexe A (`f06bcfe7…`, `8c0432df…`) sont égaux à leur copie recopiée dans la pièce ; la sortie du
programme 1 se rejoue au même résultat (seuils recomptés plus haut). Les programmes de l'annexe n'étant pas sous le dépôt, la
pièce les recopie en entier : suffisant.

## 3. Forme du crible : recommandation nette pour la mère

Deux formes : **fidèle** (Pr-1 choisit hors crédits, Pr-2 écrit ; 58,30 attendus dont 10,30 hors crédits ; 216,60 au pire dont
96,60 hors crédits) ; **variante** (Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4 ; 128,30 attendus ; 263 au pire dont 3,00
hors crédits ; 315,60 à 24 mondes).

**Ma recommandation : la variante, confiance 0,6** (les trois lecteurs précédents : 0,6, 0,65, 0,65). Raisons :
1. La consigne permanente de Lazar (« crédits de Claude au maximum ») est mieux servie : 98 % de l'attendu sur crédits (contre
   82 %), 3 USD hors crédits au pire (contre 96,60). Le coût total est plus haut, mais l'argent frais ne l'est pas.
2. Le contraste de prix est le même aux deux barèmes dans la variante (rapport de 2 aux prix publics et aux prix de la
   configuration : Pr-4 8/40 contre Pr-2 4/20), alors que la forme fidèle n'a de contraste qu'au prix public promotionnel de Pr-1
   (2/10), qui s'arrête le 30 novembre ; au prix de la configuration Pr-1 (10/50) est plus cher que Pr-2 (4/20) et la question
   « par dollar » s'inverse. La forme fidèle risque donc d'aboutir à « dépend du barème » (étage 4) quelle que soit la donnée.
3. Aux propres chiffres de la pièce, le rapport des appels d'écriture est d'environ 2 (0,35 à 0,45 contre 0,66 à 0,82), non les
   3,2 de la note : la forme fidèle n'a pas le contraste que la note lui prête.
4. Le programme classe lui-même Pr-1 et Pr-2 dans la moitié bon marché et Pr-3 et Pr-4 dans la moitié chère (note, idée (v)) :
   la variante respecte cette partition pour (iii) ; la forme fidèle fait jouer à Pr-2 le rôle de « cher ».

**Si la variante change la question : oui, mais peu.** La structure est la même (un choisisseur moins cher, un écrivain plus
cher, quatre bras, mêmes mesures) ; change la paire de proposeurs (un modèle hors crédits devient un modèle sur crédits, d'une
même maison que l'écrivain). La conclusion porte alors sur « deux paliers de prix d'une même famille », non sur « un
proposeur externe bon marché ». **Aucune des deux formes ne mesure la nécessité de la frontière au sens de QO1** (F-02).

**Coûts de la variante, à lire par la mère** : (a) un seul fournisseur pour les 100 appels (le texte du pilote note « aucun compte séparé » pour les
deux proposeurs sur crédits, et la procédure v14 dit qu'une clé sert deux proposeurs sur quatre : à vérifier par la mère) : toute coupure, toute limite de débit touche tout le crible ; concurrence de 20
sessions du même fournisseur à cinq files (15 de Pr-4 et 5 de Pr-2) et de 24 à six files : l'essai à blanc et la ligne
« limite de débit » deviennent décisifs ; (b) le solde de crédits de Claude doit couvrir 263 au pire (315,60 à 24 mondes) : je
ne peux pas le lire ; (c) le texte est à réécrire (tour obligatoire de plus) ; (d) la borne de sortie de Pr-4 est de 64 000
jetons (bloc gelé), celle de Pr-2 de 89 000 : l'étage 2 « B tronqué » change de proposeur (Pr-2 écrit B, borne de 89 000, le
risque de troncature baisse fortement : à reprendre dans la réécriture).

Si la mère juge que la consigne de Lazar vise à **limiter les dollars hors crédits sans gonfler le total**, la forme fidèle
(moins chère, 82 % sur crédits) reste défendable : dans ce cas, appliquer F-01 à F-08 et sceller après le tour suivant.

## 4. Corrections exigées : ancien → nouveau

Chaque « ancien » figure **une seule fois** dans le brouillon 4 (vérifié par programme, espaces et retours à la ligne compris).
Ce sont les corrections de la **forme fidèle** ; si la variante est retenue, la réécriture des sections « Proposeurs », « Devis »,
« Lignes de GO » et « Choix et doutes » s'ajoute (section 5).

### F-01 (majeure) — population de P2 sous « B tronqué » : contradiction avec la définition du monde complet

Un monde complet exige que B soit « répondu », donc **non tronqué** ; la population principale de P2 exclut donc déjà tout monde
où B est tronqué, et la phrase de l'étage 2 (« δ_DB est rapporté aussi sur les mondes où B n'est pas tronqué ») décrit la même
population que le principal : elle ne rapporte rien de plus. Pire : la troncature de B tombe sans doute sur les mondes riches
(cartes longues) : l'exclure biaise P2 vers « sans perte » en silence quand moins de trois appels de B sont tronqués. La
réintégration existe dans les sensibilités (« mondes non complets réintégrés ») mais n'est pas nommée pour P2.

Ancien :

````
sous « B tronqué », δ_DB est rapporté aussi sur les mondes où B n'est pas tronqué
````

Nouveau :

````
sous « B tronqué », δ_DB est rapporté aussi en réintégrant les mondes où seul l'appel de B est tronqué (C_B = 0, dollars de B comptés ; S, D et H répondus), et ce rapport est lu avec le principal même quand moins de trois appels de B sont tronqués (le principal exclut ces mondes par définition du monde complet)
````

### F-02 (majeure) — « sans la frontière » : le crible ne retire pas la frontière (N-045, QO1)

N-045 (l. 50) appelle « espèces de frontière » les trois modèles de la configuration, Pr-1 compris ; B ne retire donc pas la
frontière, il remplace Pr-2 par Pr-1. Les phrases gelées de verdict « perte établie sans la frontière » affirment plus que ce
que le crible mesure (R8, pas d'affirmation excédentaire). Corriger les cinq lieux de verdict et les deux phrases de contexte.

Ancien :

````
P2 nécessité de la frontière δ_DB
````

Nouveau :

````
P2 nécessité du proposeur cher pour l'écriture δ_DB
````

Ancien :

````
la frontière pour le rôle d'écriture (N-045
````

Nouveau :

````
la frontière (ici Pr-2 contre Pr-1, deux espèces de frontière au sens de N-045 : l'instrument local n'est pas joué) pour le rôle d'écriture (N-045
````

Ancien :

````
≥ + 0,5 composante par monde ; « perte établie sans la frontière » | borne haute
````

Nouveau :

````
≥ + 0,5 composante par monde ; « perte établie sans le proposeur cher » | borne haute
````

Ancien :

````
P2 « perte établie » : la frontière sert à l'écriture (pour
````

Nouveau :

````
P2 « perte établie » : le proposeur cher sert à l'écriture, par rapport à l'autre espèce de frontière (pour
````

Ancien :

````
- **P2** : « **perte établie sans la frontière** » si
````

Nouveau :

````
- **P2** : « **perte établie sans le proposeur cher** » si
````

Ancien :

````
la phrase « perte établie sans la frontière » est
````

Nouveau :

````
la phrase « perte établie sans le proposeur cher » est
````

Ancien :

````
| 5 | P2 (QO1, rôle d'écriture) | « perte établie sans la frontière » (
````

Nouveau :

````
| 5 | P2 (rôle d'écriture ; QO1 seulement au sens dit en « Hypothèse ») | « perte établie sans le proposeur cher » (
````

### F-03 (mineure) — III-1 : le chiffre de ρ_DS contredit le signe, et la colonne « ce qui la réfute » est plus faible que la prédiction

Δ_R ≤ 0 équivaut à ρ_DS ≤ 1 ; l'intervalle « 0,8 à 1,1 » admet des cas où le signe prédit est faux. La réfutation écrite (borne
basse > 0) ne réfute que la partie « non tranché ».

Ancien :

````
(ρ_DS entre 0,8 et 1,1) ; issue
````

Nouveau :

````
(ρ_DS entre 0,8 et 1 ; ρ_DS au-dessus de 1 en estimation réfute le signe prédit) ; issue
````

Ancien :

````
| borne basse à 97,5 % de Δ_R > 0 | 0,5 |
````

Nouveau :

````
| estimation de Δ_R > 0 (réfute le signe) ; borne basse à 97,5 % de Δ_R > 0 (réfute « non tranché ») | 0,5 |
````

Ancien :

````
ρ_DS ≤ 1,1 (confiance 0,5)
````

Nouveau :

````
ρ_DS ≤ 1 (confiance 0,5)
````

### F-04 (mineure) — « sans perte notable » n'est atteignable que si B est au moins aussi bon que D dans l'échantillon

Avec un écart-type de 1,0 à 1,2 par monde, la borne haute à 97,5 % est à environ δ + 0,55 (20 mondes) ou δ + 0,50 (24) : sous
+ 0,5, il faut δ observé sous − 0,05 (20) ou sous 0 (24). Le verdict ne dit donc pas « équivalence » ; la pièce le dit pour
« perte établie » mais pas pour « sans perte notable ».

Ancien :

````
à refaire par la simulation de la phrase suivante.
````

Nouveau :

````
« sans perte notable » n'est atteignable qu'avec un écart observé δ_DB sous − 0,05 à 20 mondes (sous 0 à 24), pour un écart-type de 1,0 à 1,2 : il dit alors que Pr-1 écrit au moins aussi bien que Pr-2 dans l'échantillon, non une équivalence à 0,5 près ; à refaire par la simulation de la phrase suivante.
````

### F-05 (mineure) — « fournisseur perdu en entier » non défini

Mot gelé (« Seuil », étage 1) sans définition : aucune réponse ? aucun appel répondu ? Écrire la définition.

Ancien :

````
aucun fournisseur
  perdu en entier ; sinon
````

Nouveau :

````
aucun fournisseur
  perdu en entier (aucun appel répondu de ce fournisseur sur tous les mondes commencés, dix appels faits au moins) ; sinon
````

### F-06 (mineure) — renvois à [CRIBLE-V], brouillon non scellé, pour des définitions et des sources que la pièce porte

La définition de la couverture, centre de la statistique, dit « comme [CRIBLE-V] » ; [CRIBLE-V] est cité à son brouillon 1 alors
que le dossier compte des brouillons jusqu'au 4 : un lecteur ne sait pas lequel. La définition vit dans le texte scellé du
pilote (attribution Δ_i, seuil τ_i, témoin positif), qui est scellé : le citer. Même chose pour deux renvois du devis.

Ancien :

````
- **Composantes comptées et couverture** : comme [CRIBLE-V] : composantes **certifiées**
````

Nouveau :

````
- **Composantes comptées et couverture** : définies par [PILOTE] (« Métrique » : attribution Δ_i, seuil τ_i, témoin positif ; texte scellé) : composantes **certifiées**
````

Ancien :

````
**Hypothèses de coût** (comme [CRIBLE-V], « Devis ») :
````

Nouveau :

````
**Hypothèses de coût** (ce texte ; [CRIBLE-V], brouillon non scellé, n'est pas une source) :
````

Ancien :

````
([CRIBLE-V], « Devis »).
````

Nouveau :

````
(bloc gelé de [PILOTE] : plafond de session de Pr-1 à 2,34 USD).
````

### F-07 (mineure) — la ligne « Témoin commun » écartée porte encore des chiffres de devis

Écartée par la mère (R-2977), elle reste écrite avec « attendu ≈ 42,30 » et « pire 176,60 » : risque de lecture comme devis à
l'inscription des lignes de GO. Signalée deux fois comme facultative (tours 2 et 3) ; à présent que la pièce approche du sceau,
la marquer.

Ancien :

````
- **Témoin commun avec (v)** ([NOTE] § 4) : S pris
````

Nouveau :

````
- **Témoin commun avec (v)** — **écarté (R-2977) ; information seulement, jamais un devis** ([NOTE] § 4) : S pris
````

### F-08 (mineure) — durée attendue à cinq files absente

La pièce donne 12 à 15 h en série et 8 h au pire à cinq files, mais pas l'attendu à cinq files, que la garde de départ et le prix
de la machine supposent.

Ancien :

````
**cinq files de quatre mondes** (point 9 de la section 0), jamais une minuterie plus longue ;
````

Nouveau :

````
**cinq files de quatre mondes** (point 9 de la section 0), jamais une minuterie plus longue ; durée attendue à cinq files : 4 mondes × 30 à 40 min, soit 2 à 2 h 40 par file, plus mesure et barrières (au pire 8 h) ;
````

## 5. Remarques facultatives (aucune correction exigée)

- R-1 : dire que les fourchettes hautes de S (16,40) et de B (9,00) viennent des mesures de la course v67 et de la réflexion
  ajoutée de Pr-1, non de la colonne des jetons attendus.
- R-2 : la première personne (« je parie », « mes fourchettes », « je n'ai écrit ») est tolérée dans un préenregistrement
  de brouillon ; à passer à la forme impersonnelle dans la version qui fera foi.
- R-3 : la ligne « sonde neuve des relais (8,07) » du devis est morte si le relevé de la sonde v74 est exigé sans condition
  (ligne 3 de la liste d'arrêt) ; la retirer ou la relier à la ligne d'arrêt.
- R-4 : la colonne « ce qui la réfute » de III-2 (borne haute < 0) est plus faible que la prédiction (≥ + 0,5) : un écart observé
  de 0,3 n'est ni confirmé ni réfuté ; une phrase le dirait.
- R-5 : si le taux de réussite par appel est lu sur huit appels de chacun des deux relais, « sous 0,95 » revient à « au moindre
  échec » (déjà signalé à la mère au tour 3) ; une phrase dans « Seuil » le dirait.

## 6. Si la variante est retenue : ajouts à la liste (en plus de ceux des rapports des tours 2 et 3)

Réécrire : (a) tables « Proposeurs » (Pr-2 choisit et écrit B ; Pr-4 : S, D, H) avec plafonds 2,00 et 3,00, bornes 89 000 et
64 000 ; (b) tableau de devis (Pr-4 60 appels, 96 et 180 ; Pr-2 40 appels, 32 et 80 ; machine 0,30 et 3,00 ; total 128,30 et
263,00) ; (c) lignes de GO : κiii1 sur crédits pour Pr-4 (180) et Pr-2 (80), κiii2 réduite à la machine (3), κiii0 sonde des
gabarits (Pr-2 sous G1, Pr-4 puis Pr-2 sous G2) ; (d) étage 2 « B tronqué » (borne de Pr-2 à 89 000 : seuil à relire) ;
(e) concurrence : 15 de Pr-4 et 5 de Pr-2 sur un même fournisseur ; essai à blanc, ligne « limite de débit » à relire pour un
fournisseur unique ; (f) point « prix de la configuration en sensibilité » : le contraste tient aux deux barèmes ; (g) retirer
« barème promotionnel » de l'étage 4 s'il n'est plus pertinent ; (h) renommer « tout bon marché » (B) en « écrit par le choisisseur ».
Un tour de contre-lecture de plus est obligatoire.

## 7. Points pour la mère (à trancher ou à savoir)

1. **Forme du crible, à inscrire par une ligne de `registres/decisions.md` datée à l'heure, AVANT que le lecteur neuf du pilote
   rende sa lecture** (E-01 du tour 3) : la consigne du lecteur est déjà en contre-lecture (R-2983). Ma recommandation : la
   variante, confiance 0,6 (section 3). Le gel de III-6 est à inscrire de la même façon, avant la même lecture (E-02).
2. **Mot du directeur utile** : la phrase de Lazar (barrière 1 de la procédure, tapée dans la session qui lance) est exigée
   pour le lancement ; l'autonomie finit le 17 novembre à 11:48Z (prolongeable au 18) ; le crible ne se lance qu'après : tour de
   contre-lecture suivant, version qui fera foi, scellement, code neuf et sa contre-lecture, essai à blanc à cinq files,
   inscription des lignes de GO. Le calendrier tient s'il n'y a pas de réécriture de plus ; la variante en impose une.
3. **Enveloppe de GO-2026-11-15-06** : 123 + 483 + 243 (i, ii, iv de la note) + 196,60 ((v), R-2977) + 263 (variante de (iii))
   = 1 308,60 au pire, au-dessus de 1 275 ; avec la forme fidèle 1 262,20. Le pire cas des cinq ne se réalise pas ensemble, mais
   chaque ligne est un plafond inscrit : la mère doit décider quel plafond cumulé elle tient (ou réduire (ii), qui pèse 483).
4. **Solde de crédits de Claude** : 263 au pire pour (iii) seul avec la variante (315,60 à 24 mondes), plus les autres cribles.
5. **N = 24** : la règle « sous 0,95 » revient à « au moindre échec » sur huit appels ; coût + 20 % : à accepter explicitement.
6. **N-045 point 3** : à dire à Lazar avec le nœud d'adoption (la pièce le fait) ; **et que le crible ne retire pas la
   frontière** (F-02) : il compare deux espèces de frontière ; la question QO1 complète exigerait l'instrument local.
7. **Risque** : « non tranché » pour P2 même si III-2 est vraie (puissance 0,35 à 0,50 à 20 mondes) ; code neuf et
   concurrence jamais éprouvée (deux jours d'agents).

## Incidents (de ma main)

- Aucun appel de modèle, aucune dépense, aucune machine, aucune modification d'un fichier existant, aucun commit.
- Lecture de `registres/decisions.md` par `grep` : les lignes R-2981 à R-2983, venues avec les résultats de ma recherche sur les
  mots « pilote » et « crible », contiennent des comptes de marche du pilote (nombre de mondes complets, appels tronqués) et son
  coût inscrit ; **je ne les ai pas utilisés** dans cette lecture et n'ai ouvert ni la sortie du pilote, ni son rapatriement, ni
  la branche de sortie.
- Un `git fetch` à refspec (branches `lot/compte-organisme-v1` et `prep/pilote-mr2-compte-organisme-v1`) ; aucun clone ; lecture
  par `git show` seulement ; copies de travail (procédure v14, texte du pilote) dans le bloc-notes de cette session.
- J'ai constaté que les deux programmes de l'annexe A existent aussi dans le bloc-notes de la session (même racine que le
  mien) ; je n'y ai fait que lire et comparer les empreintes.
- Aucun `pytest`, aucun calcul lourd : quelques comptes exacts en bibliothèque standard (quelques millisecondes).

# Contre-lecture du préenregistrement du crible (iii), brouillon 2 — tour 2 — v1

- Contre-lecteur : sous-agent neuf, **modèle C** (identité dite en conversation seulement) ; auteur de la pièce : modèle A ; je n'ai écrit
  aucune pièce citée ; je n'ai pas écrit le rapport du tour 1 non plus (il est d'un autre lecteur neuf, même modèle que moi, que je ne connais pas).
  Le premier contre-lecteur (modèle B), arrêté sans rapport : je n'ai rien lu de lui.
- Date (UTC) : Mon Nov 16 13:40:31 UTC 2026 (`date -u`) au début de la rédaction du rapport ; lecture entière de la pièce, tour 2.
- Pièce relue : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon2.md`, empreinte entière
  `713ea6a7f3c7a2b6a4ae627a6445a9ff06fd4acd3dfedee24fc3fd6630d0bd3d` (`sha256sum`, égale à son compagnon).
  Brouillon 1 : `00c92559d54349101dfcc0c59afe402c388b192c32fa6018bbf809eb02f22af0` (égale à son compagnon et à celle citée par la pièce).
  Rapport du tour 1 : `e1e142c1a8ab09ca6111fe26980cebe4f310e653c1fbf955f152fbcbcf96e643` (égale). Programme d'application des corrections :
  `4b156b3d2720a9f5ac6bb4c83a50c41df0917d9404546af127d78471204b9772` (égale à son compagnon ; **je ne l'ai pas lu** : j'ai refait l'application par mon propre programme).
- Pièces lues : la pièce en entier (sauf le code de l'annexe A, lu en diagonale, inchangé d'après `diff`) ; le rapport du tour 1 en entier ; la note des idées
  originales (`2f6a69dd480a079fa385846c8aca06ff53c8d40b0cf36be1fd61cf8e1e0537a3`, § 1, § 3 (iii), annexe A) ; les lignes R-2977, R-2873, R-2875, R-2883,
  R-2970, R-2982 de `registres/decisions.md` (par `grep`, R-2977 en entier) ; la ligne GO-2026-11-15-06 ; la procédure v14 du pilote au commit
  `2d35cafa…` (`git show` après un `git fetch` avec refspec ; empreinte `2035562740efe1e8…` vérifiée) pour ses gardes et ses 4 × 10 800 s ; le texte scellé du pilote
  (candidat 6, `8aa33014…`, branche locale `origin/prep/pilote-mr2-compte-organisme-v1`, `git show`, sans fetch) pour son bloc gelé (plafonds 3 ; 2 ; 2,34 ; 2,34 ; bornes 64 000 ;
  89 000 ; 36 000 ; 36 000 ; quatre appels par relais). **Non lu** : tout ce que la consigne interdit, dont la sortie du pilote.

## Verdict

**corrections.** Les 26 corrections du tour 1 sont **toutes appliquées fidèlement** ; le différentiel ne contient rien d'autre que ce que la pièce déclare (deux arrondis
corrigés, justes). La conception tient. Mais la pièce ne peut pas être scellée telle quelle : **3 corrections majeures** (nombre de sessions concurrentes faux, donc essai à blanc
mal dimensionné ; texte resté écrit à 20 mondes et à 100 appels alors que N peut valoir 24, avec une table « tout autre chiffre reste » qui n'est pas exhaustive ;
forme du crible non inscrite, avec une phrase « tranché » qui contredit « à inscrire ») et **11 mineures** (D-01 à D-14, listées plus bas). Aucun appel, aucune dépense,
aucune machine, rien lu des zones interdites.

## 1. Les corrections du tour 1 sont-elles appliquées fidèlement ?

**Méthode.** J'ai extrait moi-même les 26 couples « ancien → nouveau » du rapport du tour 1 (programme à bibliothèque standard, dans mon dossier du bloc-notes), les ai appliqués
au brouillon 1, puis ai comparé le résultat au brouillon 2 par `diff`. Chaque « ancien » figure **une seule fois** dans le brouillon 1 (vérifié). Résultat du `diff` entre
« brouillon 1 + 26 couples » et le brouillon 2 : **quatre blocs seulement**.

1. **En-tête** : titre « brouillon 2 », puce « Brouillon 2 : corrections… », ligne « Statut », ligne « Validateur » (« aucun défaut sur ce brouillon 2 ») : **déclarés par la pièce** (« Rien d'autre que
   les corrections, l'en-tête et la section Contre-lecture ne change »). La ligne « Validateur » est **vraie** : `controle_ia.prereg.problemes` rejoué sur le brouillon 2 rend `[]`.
2. **C-04, deux arrondis** : « 0,52 → 0,51 » (p = 0,95, N = 20) et « 0,23 → 0,22 » (p = 0,93, N = 20). **Recompté par moi** (binomiale, monde complet de probabilité p⁵, N = 20 et 24,
   au moins 16 mondes complets) : p = 0,95 : 0,5149 et 0,9276 ; p = 0,97 : 0,8586 et 0,9961 ; p = 0,93 : 0,2249 et 0,7091 ; p = 0,90 : 0,0427 et 0,2943. **Les arrondis corrigés sont justes** ;
   les autres chiffres du couple sont justes. (« 1,00 » pour 0,9961 est un arrondi qui se lit comme une certitude : D-11.)
3. **C-20, une espace** (l'espace initiale du « nouveau » retirée) : déclarée, sans effet.
4. **Section « Contre-lecture »** : remplacée (c'est ce que le tour 1 demandait de faire : « Aucune à ce jour » devenait faux). Elle porte les **deux empreintes entières** exigées (brouillon relu, rapport) :
   le défaut attendu au tour 1 a disparu.

**Aucun autre octet ne diffère.** Les 26 « nouveau » figurent chacun une fois dans le brouillon 2, sauf C-04 (remplacé par la version à arrondis corrigés, point 2). L'annexe A (code, sorties,
empreintes) est identique à celle du brouillon 1.

**Les décisions de R-2977 se retrouvent toutes dans la pièce** : mondes séparés (choix 7, « Partie B ») ; dollars au prix public en principal (choix 6) ; ablation aux critères gelés (écarts, étage 5) ;
essai non adopté (statut, écarts) ; relevé de v67 : hors de ce crible (partie de (v)) ; nombre de mondes 24 si taux sous 0,95 (« Seuil ») ; B sur les ensembles de D et égalités par l'ordre des noms (choix 1, 2) ;
forme « à trancher par le contre-lecteur » : **non inscrite**, voir D-03.

**Fidélité au sens** (au-delà de la lettre) : les passages touchés relus. Sont à reprendre : la phrase « Tranché par la mère sur le conseil du contre-lecteur » (choix 4) est une contradiction interne telle qu'écrite dans
le rapport du tour 1 et reprise ici ; le « mon compte » du couple C-19 passe tel quel dans la pièce (première personne du contre-lecteur du tour 1, lue comme celle de l'auteur) ; « 10 sessions de Pr-1 en même temps »
(C-02) est une erreur **du couple du tour 1**, reprise fidèlement (D-01). Ce sont des défauts des couples, non de l'application.

## 2. Réponses aux neuf points

**(1) R1.** Tous les éléments y sont : hypothèse (H-iii, H-iii-a, H-iii-b), prédictions chiffrées avec signe, métrique, seuils, plan d'analyse, critères de lecture gelés (étages 0 à 7), liste d'arrêt. Portes de sortie restantes
après lecture : (a) forme du crible non inscrite (D-03) ; (b) « le gel de III-6 à confirmer par la mère » (D-13) ; (c) le texte « tout autre chiffre reste celui de ce texte » est **contredit** par trois valeurs que la pièce
fait calculer et recopier avant le scellement (part de distracteurs après filtre de III-5, puissance de P1 et de P2, taux d'erreur de l'intervalle) : la règle n'est pas exhaustive, et rien ne dit ce qui arrive si la simulation
montre un défaut (D-02) ; (d) N dépend d'un taux du pilote **calculé avant le scellement** : c'est une règle écrite d'avance, acceptable ; (e) 20 mondes et 100 appels restent écrits en plusieurs endroits (D-02).

**(2) R3.** *Statistique principale* Δ_R = R_D − R_S : justifiée avant toute donnée (toujours définie quand le bras standard ne couvre rien ; même signe que ρ_DS quand R_S > 0 ; dit dans « Seuil »). Elle est négative par construction si D couvre
autant que S (D coûte plus), ce que la pièce dit à demi (III-7 > 1, III-1 « ≤ 0 ») : acceptable. *Marge de 0,5 composante par monde* : avouée comme choix, rapportée à 3 à 5 composantes (10 à 17 %), à contre-lire (choix 5) : acceptable.
*Égalités par l'ordre des noms* : justifiées (les traits sont permutés dans chaque monde par le générateur ; lu au tour 1) ; effet dit au choix 2. *Puissance* : à 20 mondes, P2 à l'effet prédit (+ 0,5, écart-type de l'écart par monde
1,0 à 1,2, borne basse à 97,5 %) : je **refais le compte** : écart standardisé 2,24 à 1,86 pour un seuil de 2,24 (quantile 0,0125 d'une normale) → puissance 0,50 à 0,35 : **confirmé** (0,35 à 0,50). « Non tranché » est donc l'issue la plus probable de P2 même si III-2
est vraie : la pièce le dit maintenant (« Taille »). *Bras « tout bon marché » (B) qui réemploie la passe 1* : comparable à D sans fuite (texte servi égal à l'octet, ligne d'arrêt et essai ; B est une session neuve ; la réponse brute de la passe 1 ne passe jamais) ;
la dépendance entre B et D est dite ; le coût de la passe 1 est compté dans D **et** dans B ; aucun défaut.

**(3) Forme du crible et crédits de Claude — recommandation nette pour la mère : la variante (Pr-2 choisit, Pr-4 écrit), confiance 0,65.**
La question de la note (« choisir les traits pas cher puis écrire la loi cher couvre-t-il plus par dollar ? la passe chère est-elle nécessaire ? ») est une question de **palier** : un proposeur moins cher choisit, un plus cher écrit, comparés à un appel du plus cher seul,
par dollar ; ablation = le moins cher écrit. La variante **garde cette structure** et l'écart de prix par jeton (2 entre les deux paliers, aux deux barèmes) ; la forme fidèle, elle, a un écart de 2 au prix public **qui disparaît au prix de la configuration** (Pr-1 devient plus cher que Pr-2) et
un barème de Pr-1 offert seulement jusqu'au 30 novembre, date de fin de la ligne de GO-2026-11-15-06. Sur la consigne permanente de Lazar (« crédits de Claude au max ») : variante = 125,30 USD sur 128,30 attendus sur crédits (98 %) et 3 USD hors crédits au pire (machine seule) ;
forme fidèle = 48,00 sur 58,30 (82 %) et 96,60 hors crédits au pire. **Recomptés par moi, exacts** : forme fidèle 60 × 0,80 + 40 × 0,25 + 0,30 = 58,30 ; 60 × 2,00 + 40 × 2,34 + 3,00 = 216,60 ; variante 60 × 1,60 + 40 × 0,80 + 0,30 = 128,30 ; 60 × 3,00 + 40 × 2,00 + 3,00 = 263,00 ;
à 24 mondes : 259,32 et 315 au pire, environ 70 et 154 attendus (× 1,2). **La variante change la question**, et la pièce doit le dire : « la frontière est-elle nécessaire pour l'écriture » (QO1) devient « le palier supérieur **de la même maison** est-il nécessaire pour l'écriture » ; elle ne mesure plus un proposeur
bon marché d'une **autre** maison, ni un instrument local (N-045 : Pr-1 reste une espèce de frontière de toute façon) ; risque de convergence de deux modèles d'une même maison (D proche de H) sans effet sur la validité. Cette lecture déplacée se paie bien : à N-045 point 1 (composition apprise, modèle par rôle compris), « un palier moins cher par rôle » est précisément la question utile.
La forme fidèle reste la seule à mesurer un moins cher d'une autre maison ; si la mère la veut, à proposer **à part**, plus tard, sur un devis propre, hors du barème promotionnel. Coût supplémentaire de la variante : + 70 USD attendus (+ 84 à 24 mondes) et 263 contre 216,60 au pire : dans l'enveloppe (avec (v) : 196,60 + 263 = 459,60 sur 1 275). **À vérifier par la mère** : que le solde de crédits de Claude
couvre 263 USD (315 à 24 mondes) au pire, en plus des autres usages (je ne le lis pas). Choisir la variante oblige à **réécrire** (section 5 ci-dessous) et rend **obligatoire un tour 3** (les prédictions III-1, III-2, III-5, III-7 changent).

**(4) Devis.** Recompté : 100 appels = 5 par monde × 20 (Pr-2 : S, D, H = 60 ; Pr-1 : passe 1, B = 40). Plafonds de session relus dans le bloc gelé : `2,34` pour deux proposeurs hors crédits, `2,00` et `3,00` pour les deux sur crédits ; bornes 36 000, 89 000, 64 000.
Attendu 48,00 + 10,00 + 0,30 = 58,30 ; pire 120,00 + 93,60 + 3,00 = 216,60 ; parts de GO (κiii1 120, κiii2 93,60 + 3,00) ✓ ; sonde des deux gabarits : plafonds 2,34 + 2,00 + 2,34 = 6,68 (2,00 sur crédits, 4,68 hors) ✓ ; attendu au prix public
= passe 1 de Pr-1 (≈ 0,05 à 0,14) + écriture de Pr-2 (0,66 à 0,82) + écriture de Pr-1 (0,35 à 0,45) = 1,06 à 1,41 : pièce 1,05 à 1,40 ✓. À 24 mondes : 72 appels de Pr-2 × 2,00 = 144,00 ; 48 appels de Pr-1 × 2,34 = 112,32 ; machine 3,00 : 259,32 ✓.
**Cohérence avec GO-2026-11-15-06** : chaque crible sous sa ligne « calcul » inscrite par la mère sur devis refait et contre-lu ; « essayé, non adopté » ; part sur crédits et part hors crédits séparées ; enveloppe 1 275 ; échéance 30 novembre : respecté. **Écart de ce texte à lui-même** : les lignes de GO et le devis sont écrits à 20 mondes ;
la table « Règle de mise à jour » dit « montants = N/20 × » : il manque les appels, les files et le nombre de mondes (D-02). Un point : au taux de réussite observé de 8 appels sur 8 (deux relais, quatre appels chacun au pilote ; la sortie n'est pas lue ici), le taux n'exclut pas 0,95 : la règle « sous 0,95 » revient en pratique à « au moindre échec, 24 mondes » (voir « Points pour la mère »).

**(5) Durée.** La pièce fixe maintenant une borne par appel (3 000 s), une borne par monde (7 200 s), 5 files de 4 mondes (6 pour 24), un pire cas d'une file de 8 h, une garde de départ de 10 h : **cohérent** (4 × 7 200 s = 8 h ; 8 h + 2 h = 10 h, sous 17 h ; deux tours de 3 000 s = 6 000 s sous 7 200 s).
Elle dit nettement que **le code du pilote ne sert pas tel quel** : lanceur, gabarits, filtre, ordre à deux tours, files parallèles, mesure neufs ; essai à blanc à cinq files ; arrêt avant tout appel si les relais refusent la concurrence. **Mon avis net : oui, il faut une configuration et un code neufs** (lanceur à files parallèles et à deux tours dépendants, pas une configuration du lanceur v74), environ deux jours d'agents, et la
concurrence n'a jamais été éprouvée. Défauts : le **nombre de sessions concurrentes est faux** (D-01) ; la garde de départ de 10 h remplace les 12 h 30 de [PROC-14] sans le dire (D-09) ; l'affectation des mondes aux files n'est pas fixée (D-10) ; la borne de 3 000 s par appel est choisie avant de connaître la durée réelle des appels du pilote, sans règle si elle est trop courte (D-14).

**(6) Liste d'arrêt, R5, graines.** Chaque ligne a son essai sain et son artefact, y compris les trois lignes ajoutées (monde de 40 min / appel scripté de 3 100 s ; aucune erreur / 10 % d'erreurs scriptées ; marge suffisante / échéance proche simulée) ✓. Graines par
`numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, clés `(r, 40)`, `(12, r, t)`, `(99, b)`, `(97, k)` : sans collision pour r jusqu'à 23 (donc pour N = 24) ✓. **Minimum de 16 sur N** : règle présente, probabilités recomptées justes (voir 1) ; la ligne d'arrêt générale « complets + non commencés < 16, quelle qu'en soit la cause » est bien formée ;
son artefact « cinq mondes incomplets sur 20 d'emblée » est juste pour N = 20 (20 − 5 = 15 < 16) et devient neuf pour N = 24 (D-02). Défaut : la ligne « erreurs de limite de débit sur plus de 5 % des appels » n'a pas de dénominateur minimal (une erreur sur les trois premiers appels fait 33 %) (D-08).

**(7) Ablation de la frontière aux critères gelés.** Bien définie : B = Pr-1 qui écrit sur les mêmes ensembles que D, même G2 à l'octet ; étage 5 (« petite » si borne haute < 0,5) ; réserve « B tronqué » avec interdiction de la phrase « perte établie sans la frontière » sous cette réserve (étage 2). **Ne contredit pas N-045 point 3 hors du crible** : la pièce écrit
que N-045 point 3 vise les lectures des courses, reste vrai pour elles, aucune course n'hérite du choix, à dire à Lazar avec le nœud d'adoption (décision de la mère, R-2977). Rien à corriger ; lire : la décision revient à Lazar (« À dire à Lazar », voir points pour la mère).

**(8) R7, R8.** Aucun chiffre de l'état de l'art : les antériorités (LLM-Select, LLM-SR, FunSearch, AlphaEvolve, sélection la plus éloignée d'abord, CADS, Co-Scientist, The AI Scientist) sont « à chercher » ou « à vérifier » ; zone « filtre déterministe sans juge » marquée « séduisante, à vérifier plus durement » ✓ ; « Aucune revendication n'est faite ici » ✓. Les chiffres neufs de ce tour (0,89 à 24 ; probabilités du minimum ; 0,74 pour 4 distracteurs) viennent de la note, de la pièce
ou de comptes exacts refaits (0,4524 ; 0,6131 ; 0,7381). Rien à corriger.

**(9) Validateur, identifiants, empreintes.** `controle_ia.prereg.problemes(brouillon 2)` rejoué : **`[]`** (aucun défaut). Identifiants de modèle : aucun nom de modèle ; les clés de configuration des postes sont déclarées exigées par le bloc gelé et les lignes de GO (R-2690) ✓. Empreintes : brouillon 1, brouillon 2, rapport du tour 1, programme d'application, note, procédure v14 (`2035562740…`), texte du pilote
(`8aa33014…`) : **conformes** ; je n'ai pas revérifié les autres empreintes de la liste (vérifiées au tour 1 et inchangées par `diff`).

## 3. Corrections exigées : ancien → nouveau

Chaque « ancien » figure **une seule fois** dans la pièce (brouillon 2 ; vérifié par programme, les retours à la ligne et les espaces sont ceux du fichier). Majeures : D-01 à D-03 ; mineures : D-04 à D-14.

### D-01 (majeur) — concurrence mal comptée

Ancien :

````
10 sessions de Pr-2 et 10 de Pr-1 en même temps
````

Nouveau :

````
15 sessions de Pr-2 (S, H et D d'un même monde peuvent courir ensemble : D part à la réponse de la passe 1, pendant que S et H courent) et 5 de Pr-1 (18 et 6 à six files)
````

### D-02 (majeur) — texte à N, exhaustivité de la table, simulations

Ancien (table « Règle de mise à jour d'après le pilote », dernière ligne) :

````
| lignes de GO (montants) | N et attendus ci-dessus | montants = N/20 × ceux de ce texte pour les appels ; plafonds par appel inchangés |
````

Nouveau :

````
| lignes de GO (montants) | N et attendus ci-dessus | montants = N/20 × ceux de ce texte pour les appels ; plafonds par appel inchangés |
| mondes, appels, files | N | « 20 mondes » se lit N partout dans ce texte (Partie B, Étapes, Devis, Taille, lignes de GO) ; « 100 appels » se lit 5N (Pr-2 : 3N ; Pr-1 : 2N) ; files : N / 4 (5 ou 6) ; « cinq mondes incomplets sur 20 d'emblée » de la liste d'arrêt se lit « N − 15 mondes incomplets » ; seuils de format (14) et de zone utile (10) : valeurs absolues, inchangées |
````

Ancien :

````
Tout autre chiffre reste celui de ce texte. **Points à remesurer
````

Nouveau :

````
Tout autre chiffre reste celui de ce texte, **hors** trois valeurs calculées sur processeur avant le scellement et recopiées : la part des distracteurs après filtre (III-5), la puissance de P1 et de P2 et le taux d'erreur de l'intervalle par percentile à N mondes (section « Taille »). Ces calculs ne changent **aucun** seuil ni aucune règle de ce texte ; si l'un d'eux en demandait un (par exemple un taux d'erreur de l'intervalle au-dessus de 0,05 à effet nul), il donne un brouillon nouveau, contre-lu, non une retouche. **Points à remesurer
````

### D-03 (majeur) — forme du crible : contradiction et décision non inscrite

Ancien :

````
**Tranché par la mère sur le conseil du contre-lecteur (tour 1)** : à inscrire ici
   après la décision ; **le contre-lecteur recommande la variante** (confiance 0,6) : au prix public
````

Nouveau :

````
**À trancher par la mère avant le scellement** (R-2977 le confiait au contre-lecteur ; les contre-lecteurs des tours 1 et 2 recommandent la variante, confiance 0,6 puis 0,65 ; décision et date à inscrire ici ; tant que rien n'est inscrit, ce texte reste rédigé dans la forme fidèle et n'est pas scellable) ; **raisons des contre-lecteurs** : au prix public
````

(Si la mère retient la variante : la section 5 de ce rapport liste ce qui se réécrit ; tour 3 obligatoire.)

### D-04 (mineur) — choix 9 périmé

Ancien :

````
9. **Durée** : mondes en parallèle (changement du lanceur) ou minuterie plus longue (procédure neuve).
````

Nouveau :

````
9. **Durée** : **tranché** (section 0, point 9, et « Devis ») : cinq files de quatre mondes (six pour 24), jamais une minuterie plus longue.
````

### D-05 (mineur) — première personne du contre-lecteur dans la pièce

Ancien :

````
approximation normale, mon compte)
````

Nouveau :

````
approximation normale ; compte du contre-lecteur du tour 1, refait au tour 2 : 0,35 à 0,50)
````

### D-06 (mineur) — phrase périmée sur le pilote

Ancien :

````
(qui génère ses
mondes ce jour, machine 60918148)
````

Nouveau :

````
(joué le 16 novembre ;
machine 60918148 détruite ; issue non lue par ce texte)
````

### D-07 (mineur) — seuil du test des signes à N = 24

Ancien :

````
demande au moins 16 accords sur 20 ;
````

Nouveau :

````
demande au moins 16 accords sur 20 (18 sur 24 : recompte exact du tour 2, bibliothèque standard ; le point 2 de l'annexe A est étendu à n = 21 à 24 par un programme sous un nom neuf, avant le scellement) ;
````

### D-08 (mineur) — dénominateur minimal de la ligne « limite de débit »

Ancien :

````
erreurs de limite de débit sur plus de 5 % des appels d'un fournisseur
````

Nouveau :

````
erreurs de limite de débit sur plus de 5 % des appels d'un fournisseur, une fois au moins dix de ses appels faits
````

### D-09 (mineur) — la garde de départ remplace celle du pilote

Ancien :

````
garde de départ : pire cas des files + 2 h (mesure, rapatriement, poussée) avant l'échéance.
````

Nouveau :

````
garde de départ : pire cas des files + 2 h (mesure, rapatriement, poussée) avant l'échéance, soit 10 h (4 × 7 200 s + 2 h), qui remplace les 12 h 30 de [PROC-14], calculées pour quatre mondes en série de 10 800 s.
````

### D-10 (mineur) — affectation des mondes aux files

Ancien :

````
lanceur, gabarits G1 et G2, filtre, ordre à deux tours, files parallèles et mesure sont neufs.
````

Nouveau :

````
lanceur, gabarits G1 et G2, filtre, ordre à deux tours, files parallèles et mesure sont neufs. **Affectation des mondes aux files** : le monde r va à la file r modulo F (F = 5, ou 6 si N = 24), dans l'ordre croissant de r ; fixée avant tout appel, indépendante de toute réponse.
````

### D-11 (mineur) — arrondi lu comme certitude

Ancien :

````
p = 0,97 : 0,86 et 1,00 ;
````

Nouveau :

````
p = 0,97 : 0,86 et 0,996 ;
````

### D-12 (mineur) — seuils absolus, dits tels (deux couples)

Ancien :

````
- **Format** : format tenu dans au moins 14 mondes complets ; sinon
````

Nouveau :

````
- **Format** : format tenu dans au moins 14 mondes complets, **quel que soit N** (valeur absolue : 14 sur 24 est moins exigeant que 14 sur 20, dit) ; sinon
````

Ancien :

````
- **Zone utile** : au moins 10 mondes complets où
````

Nouveau :

````
- **Zone utile** : au moins 10 mondes complets (quel que soit N ; valeur absolue) où
````

### D-13 (mineur) — gel de III-6, à confirmer avant, non après

Ancien :

````
(à confirmer par la mère) ; seule III-7 se refait
````

Nouveau :

````
(**gel recommandé** ; la mère le confirme avant le scellement, jamais après lecture du pilote) ; seule III-7 se refait
````

### D-14 (mineur) — borne par appel choisie sans la durée réelle des appels

Ancien :

````
**bornes de 3 000 s et 7 200 s inchangées** |
````

Nouveau :

````
**bornes de 3 000 s et 7 200 s inchangées** ; si l'appel le plus long du pilote dépasse 1 500 s, nœud de la mère avant le scellement (borne par appel probablement trop courte) |
````

## 4. Remarques facultatives (aucune correction exigée)

1. L'estimation « environ 0,35 à 0,50 » de puissance de P2 suppose une normale ; l'intervalle par percentile à 20 comptes entiers peut être plus étroit ou plus large : la simulation de la section « Taille » tranchera.
2. La pièce garde « 2,34 pour deux proposeurs » : exact pour les deux relais hors crédits du bloc gelé ; le second ne sert pas ici.
3. « Devis » : ligne « Témoin commun » écartée par la mère mais encore écrite avec ses chiffres ; la pièce le dit (« information écartée ») : lisible, à supprimer dans la version qui fera foi.
4. Pendant que S et H courent, D et B partent : la durée « 5 à 15 min puis 15 à 20 min » est une estimation ; la borne de 7 200 s couvre les deux tours même en pire cas de 3 000 s chacun.

## 5. Si la variante est retenue : ajouts à la liste du tour 1 (« Si la variante est retenue »)

La liste du tour 1 (table des proposeurs, prédictions III-1, III-2, III-5, III-7, devis 128,30 et 263, pilote lu sur les relais des deux postes, tour de contre-lecture) **reste valable**. Ajouts après relecture :

1. **Concurrence** : Pr-4 (écrit S, H et D) jusqu'à 15 sessions à cinq files (18 à six), Pr-2 (passe 1 et B) jusqu'à 5 (6) : à reporter dans l'essai à blanc.
2. **Sonde obligatoire et réserve « B tronqué »** : le seuil « plus grand appel de Pr-1 du pilote > 30 000 jetons » (borne 36 000) n'a plus de sens ; B est écrit par Pr-2 (borne 89 000) : remplacer par « plus grand appel de Pr-2 ou de Pr-4 du pilote au-dessus de 80 % de sa borne (71 200 ; 51 200) → sonde obligatoire ; réserve « B tronqué » : 3 appels de B ou plus au-dessus de 89 000 ». Garder la sonde conseillée dans tous les cas.
3. **Étage 4, qualificatif « dépend du barème »** : sans objet (rapport de prix de 2 aux deux barèmes) ; le retirer, ou le garder comme contrôle sans verdict ; la sensibilité « prix de la configuration » ne change rien pour Pr-2 et Pr-4 (4 / 20 et 8 / 40) : dire que la sensibilité est vide.
4. **Dollars hors crédits** : seule la machine (≤ 3,00 USD) ; les lignes de GO deviennent κiii1 (Pr-4 et Pr-2 sur crédits, 260 USD ; à 24 mondes 312) et κiii2 (machine, 3 USD) ; la sonde : G1 par Pr-2, G2 par Pr-4 et Pr-2, plafonds 2,00 + 3,00 + 2,00 = 7,00 sur crédits.
5. **Libellés** : « la frontière » → « le palier supérieur de la même maison » ; QO1 reformulée en tête ; la « Lecture de H-iii » dit qu'aucun proposeur d'une autre maison n'est mesuré.
6. **Choix 4 et 6** : inscrire la décision de la mère et la date ; retirer la phrase « tranché » du tour 1 ; **statut** « non scellable » levé seulement après le tour 3.

## 6. Points pour la mère (à trancher ou à savoir)

1. **Forme** : choisir entre la variante (recommandée, confiance 0,65) et la forme fidèle ; sans décision écrite, la pièce n'est pas scellable (D-03) ; vérifier le **solde de crédits de Claude** : 263 USD au pire (315 à 24 mondes) pour la variante, en plus des autres usages.
2. **Prix promotionnel de Pr-1** : le barème public 2 / 10 n'est offert que jusqu'au 30 novembre, date de fin de la ligne de GO ; un crible qui déborderait changerait de question ; la forme fidèle y est exposée, la variante non.
3. **Nombre de mondes** : la règle de R-2977 est reportée (24 si taux < 0,95). Avec **huit appels** par les deux relais employés au pilote (quatre chacun, d'après le bloc gelé), le taux ne peut valoir que 8/8 ou moins ; « sous 0,95 » = « au moindre échec ». Un 8/8 observé n'exclut pas un taux réel de 0,90 (probabilité d'atteindre 16 mondes complets à N = 20 : 0,04). **24 mondes sans condition** coûterait + 20 % (environ + 12 USD attendus en forme fidèle, + 26 en variante) et lèverait ce risque : à envisager.
4. **Écart à un texte** : N-045 point 3 (ablation « rapportée, hors des critères gelés »), mise aux critères gelés du crible par décision de la mère (R-2977) : non violé à la lettre (le crible n'est pas une course) mais son esprit ; **à dire à Lazar** avec le nœud d'adoption.
5. **III-6** : le gel recommandé avant lecture du pilote (D-13) ; le pilote mesure une première conditionnelle trouvée avant sa condition, donnée proche de III-6 : l'ordre de lecture (taux et coûts seulement avant le scellement) évite la fuite.
6. **Code neuf** : lanceur à files parallèles et à deux tours, gabarits, filtre, mesure, procédure de machine, essai à blanc à cinq files : environ deux jours d'agents ; la concurrence (15 sessions de Pr-2 à la fois) n'a jamais été éprouvée.
7. **Risque** : un « non tranché » est l'issue la plus probable de P2 même si III-2 est vraie ; ne pas le lire comme une absence d'effet.
8. **Seuils absolus** (D-12) : à 24 mondes, 14 mondes à format tenu et 10 à zone utile sont moins exigeants qu'à 20 ; si la mère préfère la proportion (17 et 12), c'est une décision à écrire avant le scellement.

## Incidents (de ma main)

- J'ai écrit dans mon propre dossier du bloc-notes (`…/scratchpad/c3`) quatre petits programmes à bibliothèque standard (application des couples, unicité des « ancien », comptes binomiaux) ; lancés avec `nice -n 19`, `python3 -I`, quelques millisecondes ; aucun calcul lourd ; ni `pytest`.
- Un `git fetch` avec refspec (`lot/compte-organisme-v1`) : il a mis à jour la référence de suivi locale `origin/lot/compte-organisme-v1` (aucun fichier de travail touché) ; `git show` de la procédure v14 et du texte du pilote (branche locale `origin/prep/pilote-mr2-compte-organisme-v1`, sans fetch) ; aucun clone.
- `controle_ia.prereg.problemes` rejoué par `PYTHONPATH=src` et `.venv/bin/python` (lecture seule du fichier, aucune écriture).
- Je n'ai pas lu le dossier du premier contre-lecteur ni aucun dossier d'un autre agent du bloc-notes ; rien sous `diag/`, `runs/`, `donnees/` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, bras d'attaque ; rien de la sortie du pilote ; ni `env` ni `printenv` ; aucune clé lue ; aucun appel de modèle ; aucune dépense ; aucun fichier existant modifié ; aucun commit.

# Contre-lecture, tour 1, du préenregistrement du crible (ii) « proposeurs en série », brouillon 1

- Lecteur : sous-agent neuf, modèle C (n'a écrit aucune pièce lue ; la pièce est du modèle A).
- Pièce lue en entier : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon1.md`
  (`816a072f6c9192049f325661e7b0ea2f0530dc1f738c4c39b8e75fba62364609`, empreinte recalculée, égale au compagnon).
- Heure de rédaction de ce rapport : Tue Nov 17 01:19:37 UTC 2026 (`date -u`).
- Pièces lues avec elle : `devis-crible-ii-brouillon1.py` et sa sortie (même dossier, empreintes vérifiées par l'outil de scellement) ;
  note des idées originales (`2f6a69dd…`, § 1, § 2, § 3 (ii), § 4, § 6, § 7, annexe A) ; relevé des idées (`bd253b6c…`, § 3.2 et alentours) ;
  verdict v2 du pilote MR-2 v14 (`e64458e8…`, par `git show` sur la référence locale de la branche `verdict/pilote-mr2-v74-v14-v1`, sections
  lues : Comptes, Dépense rapprochée, Audit de symétrie, Pour les cribles ; empreinte du contenu recalculée, égale) ; version qui fera foi du
  crible (iii) (`91b4bf30…`) et du crible (v) (`2b99627d…`) pour les passages cités par la pièce ; registre des GO (ligne GO-2026-11-15-06
  et recherche de ses autres occurrences) ; registre des dépenses (recherche) ; générateur du monde riche (une recherche sur la permutation
  des traits) ; validateur de préenregistrement. Aucun fichier sous `diag/`, `runs/`, `donnees/` ; aucune branche `calcul/*` ni `donnees/*` ;
  aucune clé, aucun appel de modèle, aucune machine.

## 1. Verdict : corrections

La conception tient : trois bras, rang 1 commun, deux comparaisons principales, règle de taille écrite d'avance, devis juste. Mais il faut
**corriger avant de sceller** : 5 corrections majeures (un nom qui désigne deux choses dans les critères gelés ; un trou dans la lecture gelée
de « dispersion par le contenu » ; des cas non définis du placebo ; une phrase de la pièce contredite par ses propres lectures ; l'option (b) du
nœud de faisabilité chiffrée avec une valeur d'exemple) et 5 mineures. Aucune ne remet la conception en cause ; un second tour est nécessaire
sur le brouillon 2. Le validateur ne relève que le défaut attendu (section « Contre-lecture » sans les deux empreintes), que le brouillon 2
comblera avec les empreintes de la pièce lue et de ce rapport ; je l'ai rejoué sur la pièce avec toutes les corrections ci-dessous appliquées à
une copie de travail : même et seul défaut, et chaque « ancien » apparaît une seule fois dans la pièce (42 couples, vérifié par programme).

## 2. Ce qui a été vérifié et tient

1. **R1 complet** : hypothèse (H-ii, H-ii-a, signe non fixé dit) ; prédictions chiffrées avec signe, issue et ce qui les réfute (II-1 à II-7) ;
   métrique ; seuil (N = 20, minimum 16, test exact des rangs signés bilatéral à 0,025 ; seuils 7 et 6 écarts non nuls recalculés : 2/2^7 =
   0,0156 et 2/2^6 = 0,03125) ; plan d'analyse ; critères de lecture gelés par étages ; liste d'arrêt avec essai sain et artefact par ligne.
2. **R3 et R4** : aucune issue n'est visée ; prédiction « non tranché » pour les deux principales ; audit de symétrie écrit avant le prononcé,
   avec « trop propre » et « tout négatif » ; le coût de la session commune compte dans les trois bras.
3. **Fidélité à la conception d'origine** : trois bras, mesures (composantes comptées, groupes prédictifs, quasi-doublons), test apparié,
   placebo « même nombre de cartes, même longueur, autre monde », traduction des trois lectures de la note en étages (voir D2 pour un trou).
   Les trois écarts (proposeur, rang 1 commun, ordre non joué) sont dits dans le texte. Le contrôle du relevé (cartes d'un autre monde) est repris.
4. **Devis refait** : j'ai relancé le programme (`python3 -I`, processeur seul) : sortie identique octet pour octet à celle scellée ; l'annexe A
   est identique à la sortie. Chiffres du pilote relus dans le verdict v2 : 1,057336 USD pour 4 appels, durées 109,396 / 54,737 / 72,991 /
   36,425 s, machine 0,082018 USD et 1,5706 h, 4 appels répondus sur 4. Recalculs : 200 × 0,264334 = 52,8668 ; haut 58,8668 ; pire 400 ; sonde
   1,0573 / 8 ; avec la sonde 53,92 sur crédits, 408 sur crédits et 3 hors crédits, soit 411 ; (iii) 270 + (v) 204,67 + (i) 123 + (iv) 243 =
   840,67 ; cumul 1 251,67 sous 1 275, marge 23,33 ; les trois autres formes dépassent (1 331,67 ; 1 311,67 ; 1 323,67). Crédits et hors
   crédits sont séparés partout. Les plafonds, la borne de sortie, 53 976 octets (= (2,00 − 1,78) / 4e-6 − 1 024) et les durées (≈ 21 min, 4 h au pire) se recalculent. Aucune ligne des registres ne cite GO-2026-11-15-06
   hors la sienne (recherche faite) : « rien n'est engagé » est exact.
5. **Empreintes** : les 15 empreintes entières de la rubrique « Documents qui font foi » que j'ai recalculées sont égales à celles écrites
   (note, relevé, deux cribles, conception du monde riche, trois outils, quatre décisions, catalogue, gabarit, validateur).
6. **Interdits** : la pièce déclare n'avoir lu que le verdict v2 du pilote ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, bras d'attaque n'y figure.
   Aucun identifiant de modèle hors les clés de configuration exigées par le bloc gelé et les lignes de GO (même pratique que les cribles
   (iii) et (v)). R7 : aucun chiffre d'état de l'art ; les voisins sont « à vérifier ». Les citations obligatoires sont recopiées de la note.

## 3. Corrections majeures (à faire avant scellement)

### D1. Les noms « P1 » et « P2 » désignent deux choses
Dans la pièce, P1 à P4 sont les quatre sessions parallèles d'un monde (P1 = la session commune) **et** P1, P2 sont les deux comparaisons
principales. Les deux sens se rencontrent dans la même phrase gelée (« un monde est complet pour P1 si les sept appels de P et de S (P1 à P4,
S2 à S4) sont répondus »), dans les étages de lecture, dans la liste d'arrêt (« P1 non répondue » contre « pour P1 et pour P2 à la fois ») et
dans la table des prédictions. Un critère gelé ne peut pas être ambigu, et la règle de nommage en clair (R-3044) l'interdit. Correction : les
comparaisons deviennent **SP** (série contre parallèle, déjà nommée δ_SP) et **SQ** (série contre placebo, déjà nommée δ_SQ) ; les sessions
gardent P1 à P4. J'ai relu toute la pièce après les remplacements : il ne reste de « P1 » et de « P2 » que le sens « session ».

D1.1 — ancien :

```
**P1** δ_SP = C_S − C_P (dispersion
```

nouveau :

```
**principale SP** δ_SP = C_S − C_P (dispersion
```

D1.2 — ancien :

```
**P2** δ_SQ = C_S − C_Q (contenu
```

nouveau :

```
**principale SQ** δ_SQ = C_S − C_Q (contenu
```

D1.3 — ancien :

```
**Prédiction de l'auteur** : P1 « non tranché »
```

nouveau :

```
**Prédiction de l'auteur** : SP « non tranché »
```

D1.4 — ancien :

```
P2 « non tranché », entre 0 et + 0,5 (0,4) ; δ_QP
```

nouveau :

```
SQ « non tranché », entre 0 et + 0,5 (0,4) ; δ_QP
```

D1.5 — ancien :

```
| **principale P1** : δ_SP
```

nouveau :

```
| **principale SP** : δ_SP
```

D1.6 — ancien :

```
| **principale P2** : δ_SQ
```

nouveau :

```
| **principale SQ** : δ_SQ
```

D1.7 — ancien :

```
P1 « dispersion » : H-ii non réfutée
```

nouveau :

```
SP « dispersion » : H-ii non réfutée
```

D1.8 — ancien :

```
lue avec P2 : si le contenu
```

nouveau :

```
lue avec SQ : si le contenu
```

D1.9 — ancien :

```
P1 « grégarisme » : H-ii non réfutée
```

nouveau :

```
SP « grégarisme » : H-ii non réfutée
```

D1.10 — ancien :

```
P1 « non tranché » : rien sur l'effet
```

nouveau :

```
SP « non tranché » : rien sur l'effet
```

D1.11 — ancien :

```
Statistiques de P1 et P2 :
```

nouveau :

```
Statistiques de SP et SQ :
```

D1.12 — ancien :

```
97,5 % pour P1 et P2
```

nouveau :

```
97,5 % pour SP et SQ
```

D1.13 — ancien :

```
un monde est complet pour P1 si les sept
```

nouveau :

```
un monde est complet pour SP si les sept
```

D1.14 — ancien :

```
pour P2, si ceux de S et de Q
```

nouveau :

```
pour SQ, si ceux de S et de Q
```

D1.15 — ancien :

```
au moins 10 mondes complets pour P1 où
```

nouveau :

```
au moins 10 mondes complets pour SP où
```

D1.16 — ancien :

```
  P1 ; réserve « placebo mal apparié »
```

nouveau :

```
  SP ; réserve « placebo mal apparié »
```

D1.17 — ancien :

```
- **P1** : « **la série disperse** »
```

nouveau :

```
- **SP** : « **la série disperse** »
```

D1.18 — ancien :

```
- **P2** : « **le contenu des cartes des pairs compte** »
```

nouveau :

```
- **SQ** : « **le contenu des cartes des pairs compte** »
```

D1.19 — ancien :

```
monde non complet pour P1 et P2)
```

nouveau :

```
monde non complet pour SP et SQ)
```

D1.20 — ancien :

```
le monde n'est complet ni pour P1 ni pour P2
```

nouveau :

```
le monde n'est complet ni pour SP ni pour SQ
```

D1.21 — ancien :

```
(P1 reste possible dans ce monde)
```

nouveau :

```
(SP reste possible dans ce monde)
```

D1.22 — ancien :

```
Deux principales, P1 (δ_SP) et P2 (δ_SQ)
```

nouveau :

```
Deux principales, SP (δ_SP) et SQ (δ_SQ)
```

D1.23 — ancien :

```
**Puissance de P1 et de P2**
```

nouveau :

```
**Puissance de SP et de SQ**
```

D1.24 — ancien :

```
| n < 16 mondes complets pour P1 (resp. P2) | P1 (resp. P2) « **non concluant** »
```

nouveau :

```
| n < 16 mondes complets pour SP (resp. SQ) | SP (resp. SQ) « **non concluant** »
```

D1.25 — ancien :

```
| P1 et P2 lus et rapportés **sous la réserve nommée**
```

nouveau :

```
| SP et SQ lus et rapportés **sous la réserve nommée**
```

D1.26 — ancien :

```
| 4 | P1 |
```

nouveau :

```
| 4 | SP |
```

D1.27 — ancien :

```
| 5 | P2 |
```

nouveau :

```
| 5 | SQ |
```

D1.28 — ancien :

```
**pour P1 et pour P2 à la fois**
```

nouveau :

```
**pour SP et pour SQ à la fois**
```

D1.29 — ancien :

```
P2 pourrait être secondaire (P1 seule à 0,05
```

nouveau :

```
SQ pourrait être secondaire (SP seule à 0,05
```

D1.30 — ancien :

```
(P2 mêlerait le contenu et la longueur)
```

nouveau :

```
(SQ mêlerait le contenu et la longueur)
```


### D2. Trou dans la lecture gelée « dispersion par le contenu »
La note lit « dispersion si série > parallèle **et placebo ≈ parallèle** ». La pièce traduit par « étage 4 disperse et étage 5 compte » :
« dispersion par le contenu ». Mais S > Q peut venir d'un placebo qui **égare** (Q < P ; la pièce l'écrit elle-même à l'hypothèse de travail
(iii)) : dans ce cas la phrase « le contenu des cartes des pairs compte » sur-affirme, et la condition « placebo ≈ parallèle » de la note
n'est pas tenue. Le cas (étage 4 « disperse », étage 5 « compte », étage 6 « effet de la seule présence » de signe négatif) n'est pas lu.

D2.1 — ancien :

```
étage 5 « compte » : « **dispersion par le contenu des cartes des pairs** » ;
```

nouveau :

```
étage 5 « compte » : « **dispersion par le contenu des cartes des pairs** » ; **sauf** si l'étage 6 donne « effet de la seule présence » de signe négatif (Q < P : le placebo égare, la condition « placebo ≈ parallèle » de [NOTE] n'est pas tenue) : lecture « **dispersion, contenu et égarement du placebo non séparés** », et la phrase « le contenu des cartes des pairs compte » n'est plus employée seule (même interdiction que sous « placebo mal apparié ») ;
```


### D3. Cas non définis du placebo
Deux branches ne sont pas écrites : (a) aucun monde donneur n'a au moins m_k cartes valides (m_4 peut valoir 18, un donneur en porte au plus 24) ;
(b) le bloc d'un donneur, à ± 25 % de la longueur du bloc de S, peut faire dépasser 53 000 octets au texte de Q_k alors que celui de S_k tient ;
la règle de retrait de la fin ne dit pas si elle vaut pour Q, et un retrait casserait l'appariement en nombre. Sans règle, le code devra
choisir : c'est un repli silencieux (R5). Correction : écarter ces donneurs, et, si aucun ne convient, ne pas lancer Q_k (compté, rapporté), avec
sa ligne d'arrêt, son essai sain et son artefact.

D3.1 — ancien :

```
sinon, parmi les donneurs qui en ont au moins m_k, celui de longueur la plus proche (égalités par l'ordre tiré) ; compté
```

nouveau :

```
sinon, parmi les donneurs qui en ont au moins m_k, celui de longueur la plus proche (égalités par l'ordre tiré) ; compté ; **un donneur dont le texte servi de Q_k dépasserait 53 000 octets est écarté** (aucune carte n'est jamais retirée d'un bloc de Q_k : l'appariement en nombre tient) ; **si aucun donneur ne convient** (aucun n'a m_k cartes valides, ou tous dépassent 53 000 octets), Q_k ne part pas, le monde n'est pas complet pour SQ, le cas est compté et rapporté, la chaîne de S continue
```

D3.2 — ancien :

```
| P1 non répondue | aucune phase 2 dans ce monde ; compté | P1 répondue : phase 2 | P1 tronquée : aucun appel de phase 2, compte juste |
```

nouveau :

```
| P1 non répondue | aucune phase 2 dans ce monde ; compté | P1 répondue : phase 2 | P1 tronquée : aucun appel de phase 2, compte juste |
| aucun donneur ne convient pour Q_k (moins de m_k cartes valides, ou texte de plus de 53 000 octets) | Q_k ne part pas ; monde non complet pour SQ ; compté ; aucun repli silencieux | un donneur convient : Q_k part | tous les donneurs à moins de m_k cartes : aucun appel de Q_k, compte juste |
```


### D4. La pièce se contredit sur ce qu'elle a lu du pilote
L'en-tête (« Statut ») et la section « Prédiction » disent que « seul le témoin positif » du pilote est lu et qu'aucune donnée de couverture
n'est connue. Or la rubrique « Documents qui font foi » dit que la section « Comptes » du verdict a été lue : elle donne le résultat principal,
x = 0 sur 14 appels (aucun appel ne porte une conditionnelle entière) et 0 sur 84 emplacements. C'est une donnée de couverture de la classe
conditionnelle, connue au moment de figer les prédictions, et qui concerne II-6. La symétrie de lecture (R4) exige de la dire. (Le verdict ne
donne aucune couverture de S contre P : cela reste vrai.)

D4.1 — ancien :

```
témoin positif est lu, [VERDICT-PC], « Pour les cribles »). Aucune dépense
```

nouveau :

```
témoin positif et le résultat principal sont lus, [VERDICT-PC], « Pour les cribles » et « Comptes » : aucun des 14 appels répondus ne porte une conditionnelle entière, x = 0 ; le pilote ne dit rien de S contre P). Aucune dépense
```

D4.2 — ancien :

```
seul le témoin positif
du pilote est lu
```

nouveau :

```
seuls le résultat principal (x = 0 sur 14 : aucun appel ne porte une conditionnelle entière) et le témoin positif
du pilote sont lus
```


### D5. L'option (b) du nœud de faisabilité est chiffrée avec une valeur d'exemple
Le choix 3 écarte l'option (b) (relever le plafond de session de Pr-2 pour les rangs 2 à 4) parce qu'un plafond de **3,10** donnerait 535 USD au
pire, « hors de l'enveloppe ». Cette valeur n'est dérivée d'aucun texte servi : sous la règle du code (un octet compté pour un jeton d'entrée à
4 USD par million, borne de sortie 89 000 jetons à 20 USD par million), 3,10 autoriserait ≈ 329 000 octets servis, très au-delà du besoin. Le plafond le plus
haut que l'enveloppe permet aux 120 appels des rangs 2 à 4 est (434,33 − 160 − 8 − 3) / 120 = 2,19 USD, soit ≈ 101 000 octets servis (contre
53 976) : de quoi porter le texte du pilote (jusqu'à 52 000 octets) et un bloc d'environ 49 000 octets, soit 18 cartes de 2 700 octets en moyenne. L'option (b) n'est donc pas hors de l'enveloppe par nature ; elle reste
plus lourde (configuration neuve, code et sonde neufs, plafond de session gelé du bloc de configuration à modifier), et la recommandation (a) peut
rester ; mais le nœud soumis à la mère doit porter le bon chiffre.

D5.1 — ancien :

```
(un plafond de 3,10 aux 120 appels des rangs 2 à 4 porterait le crible à 535 au pire), hors de l'enveloppe ;
```

nouveau :

```
(un plafond de 3,10, valeur d'exemple non dérivée d'un texte servi, aux 120 appels des rangs 2 à 4 porterait le crible à 535 au pire : 80 × 2,00 + 120 × 3,10 + 3, sonde non comprise, hors de l'enveloppe ; le plus haut plafond que l'enveloppe permet à ces 120 appels est 2,19, soit (434,33 − 160 − 8 − 3) / 120, et il autoriserait ≈ 101 000 octets servis sous la règle du code, contre 53 976 ; l'option (b) n'est donc hors de l'enveloppe qu'à 3,10, non par nature) ;
```


## 4. Corrections mineures

### m1. Énoncé inexact sur le test
« Au moins 7 écarts non nuls **tous du même signe** sont nécessaires » est faux dès 8 écarts non nuls (un seul de signe contraire peut encore
donner p ≤ 0,025). Ce qui est nécessaire : au moins 7 écarts non nuls ; ce qui suffit à 7 : qu'ils soient tous du même signe. (La sortie de
l'annexe A est une impression du programme ; sa formulation « au moins 7 écarts non nuls, tous du même signe (p = 0,01562) » décrit le cas à 7
et n'est pas à changer.)

m1.1 — ancien :

```
au moins 7 écarts non nuls tous du même signe sont nécessaires pour un p ≤ 0,025, au
```

nouveau :

```
au moins 7 écarts non nuls sont nécessaires pour un p ≤ 0,025 (7 suffisent s'ils sont tous du même signe), au
```


### m2. Mauvaise section citée
Les 52 000 octets servis sont dans la section « Devis » du crible (iii), non dans sa « Liste d'arrêt » (qui porte 53 000 et 53 976).

m2.1 — ancien :

```
en prend déjà jusqu'à 52 000 ([CRIBLE-III], « Liste d'arrêt »)
```

nouveau :

```
en prend déjà jusqu'à 52 000 ([CRIBLE-III], « Devis » : « ≤ 52 000 octets servis »)
```


### m3. Zone utile définie pour une seule principale, et étage 3 qui arrête toute la lecture
La zone utile n'est définie que pour la comparaison série contre parallèle, et l'étage 3 « arrête la lecture » en entier, alors qu'il peut ne
toucher que l'une des deux principales.

m3.1 — ancien :

```
bras en couvre moins que K(w) ; sinon « hors de la zone utile » (aucune place pour un écart).
```

nouveau :

```
bras en couvre moins que K(w) ; même définition pour SQ avec les bras S et Q et ses mondes complets ; sinon « hors de la zone utile » pour la principale touchée (aucune place pour un écart).
```

m3.2 — ancien :

```
Lecture dans cet ordre ; un étage 0 ou 3 arrête la lecture ; l'étage 1 arrête la lecture de la principale qu'il touche.
```

nouveau :

```
Lecture dans cet ordre ; un étage 0 arrête la lecture ; les étages 1 et 3 arrêtent la lecture de la principale qu'ils touchent.
```


### m4. Dépendance entre mondes par les donneurs
Un même monde peut être tiré comme donneur par plusieurs mondes (ordres tirés indépendamment) : les écarts de la comparaison série contre
placebo ne sont pas strictement indépendants entre mondes, alors que le test des rangs signés le suppose. L'effet est petit mais n'est pas dit.

m4.1 — ancien :

```
Tout est apparié par monde.
```

nouveau :

```
Tout est apparié par monde. Un même monde peut être donneur du placebo de plusieurs mondes (ordres tirés indépendamment) : les écarts de SQ ne sont donc pas strictement indépendants entre mondes ; le test les traite comme indépendants, et le nombre de mondes servis par donneur est rapporté.
```


### m5. Enchaînement des mondes d'une file
« Mondes l'un après l'autre » ne dit pas quand le monde suivant d'une file part (à la fin de S4, ou quand Q4 est aussi finie). Cela change le
nombre de sessions simultanées et la durée de la file.

m5.1 — ancien :

```
Phase 2**, par file, mondes l'un après l'autre : tour 2 :
```

nouveau :

```
Phase 2**, par file, mondes l'un après l'autre (le monde suivant d'une file part quand les six appels du monde en cours sont finis) : tour 2 :
```


## 5. Remarques facultatives (aucune correction exigée)

1. Le titre de la question et de la section parlent de cartes « brutes », alors que les cartes servies sont réécrites en JSON canonique compact
   (dit, sans autre retouche). La sonde des gabarits vérifie la sérialisation ; ce n'est pas une différence de fond, mais le mot « brutes » est
   à lire ainsi.
2. L'annexe A recopie la sortie en entier, donc nomme aussi les clés de trois proposeurs qui ne servent pas ; c'est la sortie scellée du
   programme, à ne pas modifier.
3. La puissance est calculée à 20 mondes complets ; le minimum accepté est 16. Une ligne à 16 mondes serait utile à la lecture.
4. L'usage de sigles dans la pièce (G0, GS, E, M(E), κii1) suit la forme des cribles (iii) et (v) ; une légende en tête du code aiderait, sans
   changer le texte.

## 6. Pour la session mère

1. **Nœud de faisabilité (le plus important)** : l'option (b) peut tenir dans l'enveloppe avec un plafond de session de 2,19 USD aux rangs 2 à
   4 (≈ 101 000 octets servis), alors que la pièce la dit hors enveloppe à 3,10. À décider : garder (a) (réduire les épisodes servis, la vue
   n'est plus celle du pilote si E < 400) ou rouvrir (b) (configuration neuve, code et sonde neufs, plafond gelé modifié : écart à un texte
   scellé, donc nœud de Lazar). Je ne tranche pas.
2. **Écarts à la note** (Pr-2 aux quatre places, rang 1 commun, ordre non joué) : le premier découle de la consigne « crédits de Claude au
   maximum » (GO-2026-11-15-06) ; le deuxième n'est pas dans la note et fait tenir le crible dans l'enveloppe ; à confirmer par la mère ou Lazar
   avant que la version qui fera foi ne soit scellée.
3. **Marge de l'enveloppe** : 23,33 USD seulement ; si le brouillon du crible (i) ou du crible (iv) dépasse les chiffres de la note de plus que
   cela, le dernier inscrit n'y tiendra pas (nœud de Lazar). La sonde, si elle doit être rejouée sur une nouvelle ligne, consomme 8 USD de cette
   marge.
4. **Valeur de l'essai** : puissance 0,11 à 0,47 ; l'issue la plus probable (et prédite) est « non tranché ». C'est dit par la pièce ; à garder
   en tête avant d'inscrire 400 USD de plafond pour ce crible.
5. **Chiffre erroné dans le compte rendu de l'auteur** (non dans la pièce) : « Pr-1 à 240 appels (1 375,27) » ; l'arithmétique donne
   840,67 + 564,60 = 1 405,27. La pièce ne donne pas ce cumul (elle dit seulement que les formes sur Pr-1 ne tiennent pas, ce qui est exact) ;
   corriger le compte rendu s'il est repris ailleurs.
6. **Solde de crédits de Claude** : 408 USD au pire sur un seul fournisseur, 20 sessions à la fois : à vérifier avant toute ligne.
7. **Après correction** : brouillon 2 (nouveau fichier, R12) ; section « Contre-lecture » à compléter avec l'empreinte de la pièce lue
   (`816a072f…`) et celle de ce rapport ; second tour de contre-lecture ; le texte exact du gabarit GS et le code restent à contre-lire
   séparément, comme la pièce le dit.

## 7. Incidents de ma main

1. Un premier appel du validateur avec le texte à la place du chemin a échoué (nom de fichier trop long) : sans effet, rejoué correctement.
2. Une lecture du registre des GO (lignes 335 à 342, demandées pour la ligne GO-2026-11-15-06) a affiché aussi les lignes voisines, dont
   une qui mentionne B bis, T0.7 et d'autres idées du juge (GO-2026-11-16-01) ; une recherche dans le registre des décisions a affiché quelques
   lignes d'autres sujets. Je n'ai rien utilisé de ces lignes ; aucun résultat de 7a, 7b, T0.6, T0.7, B bis, P3-bis ni du bras d'attaque n'a
   été lu, ni n'est cité ici.
3. Fichiers de travail écrits hors dépôt (dans le dossier de travail de la session) : table des couples de corrections, copie corrigée de la
   pièce, rejeu de la sortie du devis. Rien dans le dépôt hormis ce rapport et son compagnon ; aucun commit ; aucune pièce modifiée.

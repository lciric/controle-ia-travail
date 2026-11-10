# Contre-lecture R2, seconde passe — règle du jeu du bras d'attaque, brouillon 2

- **Contre-lecteur** : le sous-agent de la contre-lecture v1 (`contre-lecture-regle-du-jeu-v1.md`, commit `a9765803`). Je n'ai
  pas écrit le brouillon 2 (R2 tenu). Transparence : le brouillon 2 reprend mes réserves v1, et l'erreur neuve n° 1 ci-dessous
  vient en partie de ma propre formulation v1, que je corrige ici.
- **Document contre-lu** : `docs/notes/integration-bras-attaque-v1/regle-du-jeu-et-integration-v1-brouillon2.md` (commit
  `c6b173f4`), empreinte recalculée `3fc927ba3f9cac52e4a04720f21b9f185125165368a71922ca3ee77a4bd23739`, 164 lignes, sans
  compagnon. Le brouillon 1 reste intact (`09aa6403…`, R12).
- **Accès** : ni le coffre ni les fichiers sous embargo n'ont été ouverts. R-604 et R-605 n'ont **pas** été lues. Leurs numéros
  de ligne (830, 831) ont été contrôlés par l'identifiant seul (`grep -o`), sans afficher aucun contenu. Aucun contenu de mode
  n'est reproduit.

## Verdict

**Pas tout à fait scellable en l'état : liste courte de quatre retouches d'une phrase chacune (un majeur, trois mineurs).**
Après elles, la pièce est scellable. Un contrôle ciblé de ces quatre points suffit, sans nouvelle contre-lecture complète.

Les sept points de la v1 (M1, M2, M3, m1 à m4) sont **tous réellement corrigés**, vérifiés sur source primaire. Les ajouts du
10 novembre sont fidèles à leurs pièces. Les cinq empreintes neuves (quatre lignes du tableau, dont [X] avec deux empreintes)
sont justes et leurs compagnons valident. Les vingt empreintes anciennes sont inchangées. Les numéros de ligne du registre n'ont
pas bougé (2034 lignes ; `grep -c BA-002` vaut toujours 14). Aucun chiffre opposable n'est ajouté (R7) et aucune zone vierge
nouvelle n'est revendiquée (R8).

## État des sept points de la v1

| Point | État | Preuve sur source primaire |
|---|---|---|
| **M1** — une seule borne de bascule au nœud 1 | **Corrigé** | La recommandation porte « une seule borne : ce gel » (scellement 3 des moniteurs du papier C). Ce gel « doit précéder l'ouverture de HC4 au mois 2, janvier 2027 », ce que confirme [T] l. 292 (« 2 \| Jan 2027 \| … displacement tax (HC4) \| GC »). La rédaction lève l'ambiguïté en distinguant « gel » et « écriture du papier (mois 4, l. 296) ». C'est cohérent avec la section 2, point 3, avec [D1] (« le cœur du rôle […] ne s'ouvre qu'au scellement 3 ») et avec [S] l. 5 et 79. |
| **M2** — nœud 9, ligne récurrente de N-062 | **Corrigé, bien posé** | L'enjeu est sourcé : N-062 l. 23 (« chaque famille est une ligne de budget »), l. 24 (« pas de borne de cycles »), l. 34 ; N-056 l. 55-57 (dimensionner comme les autres modes) ; [J] l. 112 (« non chiffrée ») ; [T] l. 374-397 (budget sans cette ligne). Les options sont exactes : (a) le mécanisme envoyé, avec [T] l. 336-337, l. 396, les lignes l. 381-382 et la réserve de 10 % l. 387 ; (b) un devis sans dépense ; (c) borner les cycles, dite « **modifie N-062, point 4** […] décision de Lazar, à dire comme telle », reprise en section 6. La recommandation (b) cite exactement N-062 l. 24 (« le GO par cycle, la disponibilité d'une famille neuve et le calendrier »). La lecture du calendrier (« un nouveau cycle n'a que les mois 5 et 6 ») tient : G1 tombe fin du mois 4 ([T] l. 159, 296-297) et le mois 7 est pris par la publication et le rapport final (l. 301-302). On peut ajouter ce dernier renvoi. |
| **M3** — brouillon 6 de G1, conflit au nœud 6 (ii) | **Corrigé** | [G] est bien le brouillon 4, le plus récent sur `main`. Après un `fetch` frais d'`origin/main` (`9df4292d`), seuls les brouillons 1 à 4 existent. Le brouillon 6 (`939b56e5…`) est signalé hors de `main`, comme R-1581 ([R] l. 1539) le place sur un « canal ». La réserve est portée dans la table de victoire. Le nœud 6 (ii) pose désormais le conflit (« déjà ouvert ») : N-056 l. 55-57 (27 octobre) contre DG1-6 (b) (« deux modes jugés, M = 2 », S28), avec R-1581 point (2), et N-055 l. 28 (« hors décision »). La formule « dernière décision » a disparu. Seul reste un défaut de nommage (mineur n° 2 ci-dessous). |
| **m1** — « famille aveugle scellée » | **Corrigé** | La section 0 dit maintenant « toutes trois sont **à produire** ; aucune n'existe encore », avec « [B] l. 75 est le remède ; l'état est “aucune famille scellée” ([B] l. 73-76) ». |
| **m2** — « coupés en premier » | **Corrigé** | La section 0 dit « les attaques adaptatives du papier A (… contenu, puis réglage fin et renforcement…, l. 298-299) » sont coupées en premier, avec « les échelons qui écrivent les poids en font partie, mais pas seuls ». C'est conforme à [T] l. 298-299 et 338-339. |
| **m3** — « quatorze » sans empreinte | **Corrigé** | Le compte est dit reproductible par `grep -c 'BA-002' registres/decisions.md` (« 14 le 10 novembre »), et [R] est dit sans compagnon. Recontrôlé : 14. |
| **m4** — théorème l. 97-98 | **Corrigé** | La section 0 cite « énoncé l. 74-83 ; sa conséquence face à un attaquant adaptatif, l. 97-98 ». C'est conforme à [T] l. 74 (« Negative theorem (T), by invariance ») jusqu'à l. 83. |

## Ajouts du 10 novembre : vérifiés

- **Nœud 2 tranché** ([D2], `bba97a1a`, compagnon conforme). Le verbatim est exact : « Ma recommandation : oui, mais sous deux
  conditions. go ». Les deux conditions sont identiques à [D2] l. 8-10 : procédure d'optimisation publiée, citée, sans recette ;
  plafond de requêtes scellé au préenregistrement. [D2] l. 12 confirme « aucun lancement, aucune dépense, aucun moniteur visé
  avant son gel », et l. 16 l'écart à N-056 point 6, « à porter à la prochaine version du programme ». Le compte est juste :
  « neuf nœuds, le 2 tranché, huit attendent ». Les sections 1 et 4 ainsi que la ligne HC6 de la table de victoire sont
  cohérentes avec [D2] l. 10-11 (bras déclaré au sens de N-053 point 5 ; axe « requêtes » et « attaque optimisée »).
- **Session « attaquant informé » au mandat réduit** ([D1], `081cb8e3` ; [S], `55108eb8`, compagnons conformes). Le verbatim est
  « (a) go ». Le mandat est réduit à la reproduction de l'attaque publiée jusqu'au mot de Lazar au gel. La session ne reçoit
  aucune conception de moniteur avant ce gel ([D1] l. 15-17 ; [S] l. 27-33 et 79). Le nœud 1 reste ouvert ([D1] l. 24). Ces
  pièces s'accordent avec l'option (b) du nœud 1 avant le gel.
- **Attaque publiée choisie** ([X], `e5bab8c3`, et consignation, `06e8f102`, compagnons conformes) : Bailey et collègues, arXiv
  2412.09565. Les cinq préalables cités en section 4 sont identiques à la consignation l. 30-38 : GO-2026-10-31-05, qui expire
  le 14 novembre ; licence ; PDF de StrongREJECT ; devis A100 80 Go ; préenregistrement. Un seul point doit être nuancé
  (mineur n° 3 ci-dessous).

## Erreurs neuves : un majeur, trois mineurs

### Majeur n° 1 — Nœud 3 : la recommandation fait dire à l'entretien un arrêt par classifieur
- **Passage** : section 5, nœud 3, recommandation : « Dans les deux cas, dire que, malgré le « go » de R-888, rien d'opérationnel
  n'a tourné : […] ([P] l. 45-46), et l'écriture des valeurs du protocole a été arrêtée par un classifieur (R-912, l. 1141 ; nœud 5) ».
- **Problème** :
  - Le nœud a pour objet de « fixer la phrase d'entretien », et son enjeu emploie déjà « font dire ». La formule « dire que »
    place donc l'arrêt par classifieur dans la phrase prévue pour le jury.
  - Or la consigne d'entretien l'interdit hors question : « Le classifieur du 27 octobre se dit seulement si l'on est interrogé
    sur les refus » ([P] l. 55-56). La v18 traite les refus sur question seulement ([E] l. 417) et proscrit tout « nombre de
    refus » ([E] l. 565). Citer R-912 en plus de R-597 revient à en donner un : deux arrêts.
  - Sur le fond, R-912 concerne le protocole de malléabilité, que R-889 ([R] l. 1118) met hors du gel de R-611. Il ne prouve
    donc pas à lui seul qu'aucun pipeline opérationnel n'a tourné.
  - Origine : ma réserve v1 (« le nœud gagnerait à dire que […] rien n'a tourné parce que la rédaction a été arrêtée par un
    classifieur (R-912) ») était imprécise sur ces deux plans.
- **Correction attendue** :
  - Pour la phrase d'entretien, garder seulement « rien d'opérationnel n'a tourné » ([P] l. 45-46). Le classifieur ne se dit
    que sur question ([P] l. 55-56).
  - Dans le nœud, à titre de justification interne et non pour l'entretien, écrire que, depuis R-888, la ligne tenue est
    « niveau coût et infrastructure, aucune recette d'évasion » (R-912, l. 1141). Ajouter l'arrêt du 27 octobre, sans
    contournement (R-597), et la tenue au niveau de la méthode (R-1782, via [P] l. 46-47).

### Mineur n° 2 — Nœud 6 (ii) : « nœud 2 » entre en collision avec le nœud 2 de cette pièce
- **Passage** : nœud 6 (ii), enjeu « R-1581 (nœud 2 de Lazar) » et recommandation « le conflit déjà ouvert par R-1581 (nœud 2) ».
- **Problème** : le nœud 2 de cette pièce porte sur les verdicts comptés et il est tranché le 10 novembre. Un lecteur peut croire
  que le conflit sur le mode tenu à l'écart a été réglé par cette décision.
- **Correction attendue** : écrire « point (2) des nœuds de Lazar listés par R-1581 ».

### Mineur n° 3 — Table des acteurs : « ne lit jamais : notes » à côté de « lit : verdicts »
- **Passage** : section 2, ligne « Concepteur informé (bras B) ».
- **Problème** : la colonne « Lit » admet, pour le bras déclaré « avec retour », « les verdicts rendus à ses propres essais ». La
  colonne « Ne lit jamais » garde pourtant « notes », alors que [D2] l. 16 tient lui-même cette lecture pour un écart à « le
  bras informé ne reçoit pas les notes ».
- **Correction attendue** : écrire « notes et seuils calibrés des moniteurs sur les épisodes d'épreuve » (comme [S] l. 43 :
  « tu connais la conception, pas le résultat »), ou ajouter « hors l'exception [D2], écart déclaré à N-056 ».

### Mineur n° 4 — « Choix arrêté » sans sa réserve de licence
- **Passage** : section 0 (« le choix est arrêté le même jour, Bailey et collègues ([X]) ») et section 4 (« choix arrêté le 10 novembre »).
- **Problème** : [X] retient Bailey « sous réserve de licence » (l. 9). Une licence absente « invaliderait l'usage » (l. 46). La
  consignation garde ouvert le nœud « Bailey ou candidat 2 », défaut (a) sous 48 heures (l. 40-43). Le brouillon range bien la
  licence parmi les préalables, mais présente le choix comme acquis.
- **Correction attendue** : écrire « choix arrêté sous réserve de licence ([X] l. 9, 46) ». Si le scellement précède le
  12 novembre à 08:02 UTC, ajouter « défaut (a) en cours ».

## Hors du périmètre de la pièce (à signaler, non comptés)

- **[D1] l. 30-31 et 42**, passation scellée qu'il ne faut pas réécrire : la consigne d'envoi renvoie la session neuve au
  brouillon 1 de la règle et au brouillon 1 de la note de choix. Ce dernier avait trois bloquants, dont un modèle inversé
  (consignation l. 20-21). Si Lazar n'a pas encore collé la consigne, il faut lui donner les pièces courantes : note de choix
  brouillon 3, `e5bab8c3` ; règle brouillon 2 ou sa version scellée.
- **Registre** : deux lignes portent l'identifiant R-606 (l. 832 et 833, toutes deux du 28 octobre), et R-607 s'y ancre (« Précision
  de Lazar sur R-606 »). C'est une question d'hygiène, à corriger hors de cette pièce.

## Décompte

Dans cette passe, j'ai revérifié moi-même sur source primaire **une soixantaine de renvois** :
- [T] : l. 74-83, 97-98, 159, 292, 296-299, 301-302, 336-337, 338-339, 374-397, 381-382, 387, 396 ;
- N-053, N-055, N-056, N-062 ;
- [R] : 17 identifiants et leurs lignes, R-1581, R-888, R-889, R-912, compte BA-002 ;
- [P] l. 45-47, 55-56 ; [E] l. 417, 565 ; [J] l. 112 ; [B] l. 73-76 ;
- [D2], [D1], [S], [X] et la consignation ;
- `origin/main` après `fetch`.

J'ai aussi recalculé **les 25 empreintes du tableau** : 20 anciennes inchangées, 5 neuves justes, compagnons valides. **Aucun
renvoi faux.**

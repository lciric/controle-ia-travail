# Vérification des corrections du devis de la banque d'épisodes de la famille de réserve du cycle 2 — v1

- **Pièce vérifiée** (classe A, devis) : `docs/notes/devis-famille-reserve-cycle-2-v1/devis-banque-d-episodes-famille-reserve-cycle-2-v2.md`, empreinte `c9d9c6a4140c6cab…`, compagnon conforme. Avec elle : le programme de recalcul de la version 2 (`0dbe914c889cc928…`) et sa sortie (`1e5586d4a0d660d1…`), compagnons conformes.
- **Référence** : ma contre-lecture de la version 1, `contre-lecture-devis-v1.md` (`69f069bea0cbee61…`), douze remarques.
- **Vérificateur** : Opus 5.5, même rôle que la contre-lecture. Je n'ai écrit ni la famille, ni l'esquisse, ni le devis, ni aucun moniteur. Fini à 2026-11-21T18:45:47Z (`date -u`).
- **Non lus** : la version 2 de la pièce 6, les pièces 1 à 5 et 7, le coffre, la valeur de `k`, la pièce de sécurité du banc fermé, la note des lignées, tout fichier interdit par le mandat.

## Verdict

**Corrections faites. Une petite incohérence est à corriger avant la demande d'accord (point A ci-dessous).**

- Les douze remarques sont reprises, et chacune est corrigée.
- J'accepte les deux écarts à la lettre. Sur la ligne 671, ma remarque était fausse.
- L'arithmétique est juste. Je l'ai recalculée par un programme indépendant, et le programme compagnon, relancé, redonne sa sortie scellée octet pour octet. Le programme de la version 1 redonne aussi la sienne.
- Les chiffres qui tiennent : attendu 84,73 dollars ; plafond pessimiste 396 ; 125 en lecture groupée ; seuil d'alerte 316,80 ; première tranche engageable 19 (la carte seule).
- Une règle ajoutée par l'auteur contredit trois phrases du devis sur l'effort du lecteur Claude. Ce point est à reprendre. Trois mises au point mineures suivent. Une ligne du registre, inscrite après la fin de la version 2, est à prendre en compte (point D).

## Remarque par remarque

| n° | correction demandée | constat | tenue |
|---|---|---|---|
| 1 | corriger la citation ; confrontation des deux lecteurs, le modèle Claude compris, et de Neon, rendue par le côté habilité ; retirer « deux familles hors de la contrainte » | `registres/go.md:664` relue (par fenêtres propres) : elle confie au côté habilité la « confrontation de Mistral Large 4 et Gemini 4 Neon aux familles », sans aucun lecteur Claude. Le texte du point 2 et la condition 7 demandent ce que la remarque demandait. La phrase « deux familles hors de la contrainte » ne reste que dans la table des corrections, où elle est donnée comme retirée. La recommandation est rendue conditionnelle, avec un repli chiffré | oui |
| 2 | un plafond par file ; le pire cas d'un envoi séparé du plafond de la file | la table des six files donne 117,76, 70,66 et 7,07 pour Opus ; 93,51, 56,11 et 5,61 comptés pour Mistral (98,18, 58,91 et 5,89 à l'engagement). Je retrouve ces chiffres. La garde 1 sépare bien les réserves d'un envoi (0,2598 et 0,1127) du plafond de la file | oui |
| 3 | aucune clé Claude désignée ; ne plus citer `go.md:547` comme un accord | relu : la ligne 547 répartit des clés pour la course « nouvelles attaques » et garde Rigaud « pour le bras A selon son devis ». Elle n'est plus citée que pour la devise et comme précédent d'un plafond par solde. Pour Rigaud, « sans crédit » est relu à `depenses.md:577`. Luc a environ 153 dollars restants et 100 dollars par clé sont posés pour une autre course (`decisions.md:4786`). L'achat d'un lot avec les clés Luc et Minuit est à `go.md:663`. Le nœud 4 est posé, la condition 8 aussi | oui |
| 4 | marge de change dans le plafond ; devise compte par compte | table 4.6 ; 5 % sur la part de Mistral, de 155,22 à 162,99 ; plafond porté à 396 | oui (écart accepté, ci-dessous) |
| 5 | citer la ligne qui nomme Google, ou « à confirmer » | `decisions.md:4761` (deux comptes de la console Gemini, 11,93 et 15,59 euros, recharge automatique) et `:4421` (60,92 euros) relues. `go.md:673` relue : elle parle du « crédit Google du bras A » sur les projets à 11,93 et 15,59 euros. Le rapprochement avec « les deux clés 1 et 2 » de `go.md:667` est donné comme une lecture, à confirmer par la mère | oui |
| 6 | quatre gardes | (a) garde 4 : sur la page scellée d'Anthropic, j'ai relu le mode rapide (« Fast mode pricing », offert pour Opus 5.5) et `inference_geo: "us"`, facturé 1,1 fois. Le champ `speed` n'y apparaît que pour les agents gérés (`model.speed`). La liste des champs permis est la bonne parade. Le relais ne lit ni `speed` ni `inference_geo` (recherche dans `relais_reel.py`). (b) garde 3 : elle reprend `devis-essai…:254` ; la longueur de sortie de Mistral est « non indiquée » (`choix-mistral-deepseek-v1.md:16`). (c) garde 2 : 240 et 600 secondes, fidèles à `devis-essai…:253` ; délai par file chiffré. (d) garde 5 : cache refusé ; écriture à 5 dollars, relue sur la page (Opus 5.5 : 4, 20, 5, 8, 0,20) et à `relais_reel.py:50` | oui |
| 7 | fixer l'effort, ou le mesurer à l'essai avant tout plafond d'étape | dit non fixé, avec appui de `go.md:446` (« Non fixé : quel modèle Claude, … les réglages »). Le mot de `go.md:569` vise bien Mistral. La table par effort figure en 3.3 ; le nœud 5 et la condition 9 sont posés ; l'essai passe avant tout plafond d'étape | oui, mais voir le point A |
| 8 | déclarer les deux jeux de constantes | deux lignes S au tableau 3.3 ; les constantes sont nommées en tête du programme (lignes 54-55 et 60-62) | oui |
| 9 | arrondi du prix d'une action ; attendu bas à 1,1843 | 0,00141 à 0,00164, soit 0,0015 à 0,0017 arrondi au-dessus ; attendu bas à 1,1843 ; les quatre centimes qui bougent sont justes | oui (voir le point B) |
| 10 | minuterie du lancement 2 par la même formule | 6,28 heures payées, minuterie de 6,2 heures pour 42,8 secondes ; seuil de 81,4 secondes, recalculé : (18 − 4) ÷ 1,38 ÷ 2 − 1, puis × 3 600 ÷ 180 = 81,45 | oui |
| 11 | réserve bloquante sur la version 2 de la pièce 6 | portée en tête, au résumé, en 5.1, en 5.2, à la condition 2 et au point 1 de la section 11. Seule la carte est engageable. Le comptage n'a pas été refait | oui |
| 12 | variante à 200 épisodes | 820 épisodes, 880 ensembles, carte 74, lectures 951, total 1 038, recalculés | oui |

## Les deux écarts à la lettre

- **Ligne 671 : écart accepté, ma remarque était fausse.** Relue, `registres/go.md:671` se termine par : « Réserve : si un moniteur évalué est de la lignée Claude, un vérificateur d'une autre lignée est requis (audit des lignées en cours). » La ligne parle donc d'un audit des lignées, à propos du vérificateur du banc fermé. La version 2 la cite pour ce qu'elle dit, avec cette portée, et cite `:664` pour la confrontation. C'est juste.
- **396 et non 397 : écart accepté.** Le devis majore chaque file de Mistral, puis arrondit chaque étape au dollar supérieur : 37 + 216 + 130 + 13 = 396. Mon 397 venait de 389 + 7,76, arrondi une seule fois. Sans aucun arrondi, l'engagement vaut 36,11 + 215,94 + 129,57 + 12,96 = 394,58. Il reste sous 396, qui suffit donc.

## Arithmétique, recalculée à part

Le programme indépendant est au bloc-notes de session, hors du dépôt. Il redonne, sans écart au centime :

- les prix par question (0,0273, 0,0736, 0,0105, 0,0584, 0,0362 et 0,1242) ;
- les six files et leurs sommes (350,71 comptés, 358,47 à l'engagement) ;
- les deux comptes (195,48 pour Claude ; 155,22 et 162,99 pour Mistral) ;
- la carte (4,04 à 5,68 et 18,71 ; 3,77 à 5,35 et 17,40 ; plafond 37) ;
- l'attendu au centre, 84,7349 ;
- la fourchette, 17,50 à 111,45 ;
- la lecture groupée (0,2546 et 0,2587 par ensemble, soit 52, 32 et 4, plafond total 125) ;
- le repli sur Neon et Mistral (0,0467 et 0,1826 ; 307, 185 et 19, total 548 ; attendu 102,51) ;
- l'ancre (1,38, 4,72 et 4,96) ;
- la table par effort (54,38, 72,51, 75,30, 100,40, 117,13, 156,17, 376,15, 501,54 et 573,74) ;
- les pires cas d'un envoi (0,2598, 0,1127 et 0,2838) ;
- le cache (0,0805, soit 18,33 de plus) ;
- les variantes de devise (407 et 409) ;
- l'essai à deux réglages (21, total 404) ;
- les variantes de taille (579 et 1 038) ;
- le prix de Mistral scellé (263,22 et 266,96) ;
- la sortie couverte par la file d'Opus (2 705 jetons).

Les chiffres dérivés se retrouvent aussi : marges, rapports (4,7 et 4,8), reprises (3,59 et 46,83), part des contrôles (33,07), provision (7,73) et effet de bord (4 et 2 envois). Ce dernier suppose des envois facturés au prix d'un envoi, sans la majoration des reprises ; c'est ce qu'écrit le programme.

## Ce que la version 2 introduit

**A. À corriger : la règle des deux fois la mesure contredit « l'effort moyen et l'effort haut sont couverts ».**

- La règle est un ajout de l'auteur (4.2, 5.2, résumé point 4) : une file dont le plafond recalculé, deux fois la mesure, dépasse son plafond pessimiste ne part pas.
- Le plafond de la file d'Opus à l'étape 1 vaut 117,76, compté à `k` = 8 sur 1 600 questions. La règle laisse partir la file si le coût mesuré par question reste sous 117,76 ÷ (2 × 200 × `k`) :
  - à `k` = 8, sous 0,0368 dollar, soit environ 950 jetons de sortie aux entrées attendues ;
  - à `k` = 6, sous 0,0491 dollar, soit environ 1 540 jetons.
- Mesuré à ce que le devis suppose :
  - l'effort moyen (0,0378) arrête donc la file à `k` = 8 : 120,96 contre 117,76 ;
  - l'effort haut (0,0588) l'arrête dès `k` = 6 : 141,12.
- Or le résumé (point 3), le tableau de 3.3 (colonne « sous le plafond », « oui » pour l'effort haut), le nœud 5, options (b) et (c), et le point 6 de la section 11 disent ces efforts « couverts ». Ils le sont par le plafond de dépense, pas par la règle de lancement. Lazar lirait qu'un effort haut ne coûte que de l'argent, alors qu'il coûte un devis et un accord de plus.
- À faire, au choix de l'auteur :
  - soit écrire, à ces quatre endroits, que la règle arrête l'effort haut dès `k` = 6 et l'effort moyen à `k` = 8, et chiffrer le devis neuf qui suivrait ;
  - soit changer la règle, par exemple en prenant pour plafond de file le plus petit des deux, deux fois la mesure ou le plafond pessimiste, et en laissant partir la file si la mesure, majorée d'une marge à fixer, reste sous le plafond pessimiste.
- Ni l'un ni l'autre ne change les totaux.

**B. Mise au point : prix de Mistral au pire, arrondi vers le bas.** Au point 1 de la section 6, `p_l2` est retenu à « 0,058 au pire (0,061 avec la marge de change) » pour 0,0584 et 0,0614. C'est le défaut que la remarque 9 visait pour le prix d'une action. Écrire 0,059 et 0,062, ou les quatre décimales. Pour Opus, 0,074 est déjà arrondi au-dessus.

**C. Mise au point : le repli sur Neon et Mistral n'a ni compte ni gardes.**

- Le repli mettrait 329,87 dollars comptés sur des files de Neon. La table 4.6 n'a de ligne Google que pour l'ancre, à 5 dollars.
- Or le seul crédit Google relevé est celui du bras A, et sans la recharge automatique (`go.md:673` : 10,47 et 6,81 euros). Le pire cas d'un envoi de Neon et sa sortie maximale ne sont pas chiffrés, ni ses réglages de réflexion et de troncature, que la règle de `go.md:670` impose de vérifier avant tout envoi à un modèle de Google.
- Ce n'est utile que si le repli est retenu. Il suffit alors d'une ligne en 4.6 et d'une phrase en 4.2.

**D. Une information inscrite après la fin de la version 2 (18:39), à verser à la version suivante ou à la fiche de lancement.**

- `registres/go.md:674`, mots de Lazar vers 18:45Z : pour le compte Mistral du bras A, « offre payante », « crédit d'au moins 7,87 € », « limites européennes non données, repli global accordé d'avance ». Deux conséquences.
  - Le compte affiche des euros. La marge de 5 % sur Mistral n'est plus seulement prudente, elle est appuyée.
  - Le crédit relevé est très en dessous de la part de cette banque (20,94 dollars attendus, 163 au plafond), et le bras A le consomme aussi. La recharge par Lazar, déjà à la condition 8, est donc certaine. Elle n'est plus seulement possible.
- La même ligne confie, pour le banc fermé, « lecteurs du dommage » aux « lecteurs externes du monteur de l'oracle », par écart à la décision sur la vérité du dommage (N-060, version 3, point 1). La mère doit voir si cela touche le nœud 2 (sortie du coffre vers des tiers) ou le point 3. Je ne l'interprète pas.
- `registres/decisions.md:4801` dit que les versions 2 du cycle 2 changent notamment « lecture de l'oracle ». Cela appuie la réserve bloquante de la remarque 11 : les lignes des lectures ne sont pas engageables avant le rapprochement.

**Ajouts de la section 0 bis, vérifiés.**

- Le tableau par effort et l'essai à deux réglages sont justes, mais voir le point A.
- Le repli chiffré est juste ; voir le point C.
- Le crédit de Mistral partagé avec le bras A est appuyé par `go.md:663` et `:674`.
- L'ordre des lectures de l'essai et l'effet de bord de la garde sont cohérents.
- L'onglet « Priority » de Neon est à 5,40 et 27, relu sur la page scellée de Google.
- La lecture de `k` comme une moyenne est conforme à ce que cite le devis.
- Aucun de ces ajouts ne nomme, ne décrit ni ne suggère un mode.

## Suite

- Le point A suffit pour une version 3 courte, ou pour un erratum. B et C sont des retouches d'une ligne. D est une mise à jour du registre.
- Je vérifierai A, et B ou C s'ils sont repris. Le programme n'a pas besoin d'être relancé pour A si seul le texte change ; il le faut si la règle change.
- La réserve bloquante sur la version 2 de la pièce 6 reste entière. D'ici là, seule la ligne de la carte (19 dollars, lancement 1) est demandable.

## Journal

- Refus d'outil ou de classifieur : aucun.
- Réseau : une récupération de la branche `claude/pensive-bardeen-1fv7hw` par `git fetch`, pour relire le brouillon 3 du devis de l'essai (`533ad5b1…`, recalculé) et les deux pages de prix scellées (`78aff5c8…` et `89c58281…`, recalculées). Aucun appel à un modèle, aucune dépense, aucun commit, aucune poussée.
- Écrit : cette pièce seule, dans ce dossier, scellée. Au bloc-notes de session, hors du dépôt : un filtre de lecture, le programme de recalcul indépendant et une copie de travail du brouillon 3.
- Lignes de registre lues derrière un filtre qui masque les motifs interdits par le mandat :
  - lues en entier : `go.md:446`, `:467`, `:547`, `:569`, `:632`, `:667`, `:670`, `:671`, `:673`, `:674` ; `decisions.md:4421`, `:4761`, `:4784`, `:4786`, `:4797` à `:4801` ; `depenses.md:3` ;
  - masquées, lues par fenêtres propres seulement : `go.md:663`, `:664`, `:665`, `:668`, et `depenses.md:577` ;
  - masquées sans aucune fenêtre lisible : `go.md:666` et `depenses.md:578`.
- Lu en passant, à déclarer :
  - `decisions.md:4786` porte l'état d'une autre course, accord entre juges compris ; je n'en garde que la clé Luc ;
  - `decisions.md:4798` porte l'entropie tirée pour la course du saboteur à budget ; je n'en garde rien ;
  - `:4800` et `:4801` portent des états d'autres chantiers, sans score ; je ne garde de `:4801` que la phrase sur les versions 2 du cycle 2 ;
  - `go.md:674` porte des décisions sur le serveur de l'organisme ; je n'en garde rien.

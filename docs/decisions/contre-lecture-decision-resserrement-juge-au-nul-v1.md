# Contre-lecture — texte de décision « resserrement du juge au nul formé des lois connues » (O4), v1

- **Contre-lecteur : modèle J**, agent neuf, d'un autre modèle que le rédacteur (modèle I) ; n'a écrit ni le texte contre-lu ni la note qui le fonde.
- **Heure** (`date -u`) : lecture commencée vers 2026-11-18T05:01Z, pièce écrite à 05:03Z.
- **Pièce contre-lue** : `docs/decisions/decision-resserrement-juge-au-nul-v1.md`, 9246 octets, non suivie par git et sans compagnon `.sha256` au moment de la lecture (état attendu avant scellement) ; date de modification 2026-11-18 05:00:50 UTC.
- **Pièces lues** : la note `docs/notes/lecture-o4-suite-v1/lecture-pistes-nouvelles-o4-v1.md` (empreinte recalculée `e6263eadc3d64fd5087b0ed50cfabbdb81411e4fd99a9b74b9d579dd5557d114`, égale à celle annoncée ; en-tête, sections 0, 1, 7 et 8) ; la ligne R-3185 de `registres/decisions.md` sur `origin/main` (commit `a1bf1aa4`, récupéré par `git fetch --depth=1`) ; `docs/decisions/decision-N-067-v1.md`, en-tête et section 0 seulement.
- **Limites** : N-067 n'est pas lue au-delà de son en-tête et de sa section 0 ; la cohérence (constat 9) est jugée sur ces lignes. La note d'englobement, la v3 et la pièce de refus ne sont pas lues. Le commit `6a97bb12` cité par l'en-tête n'est pas contrôlable sur une récupération superficielle ; R-3185 est bien présente sur `origin/main` à `a1bf1aa4`.
- Aucune dépense, aucun appel de modèle, aucune valeur de clé, aucun fichier existant modifié, aucun refus de permission. Seul geste réseau : la récupération de `origin/main` prescrite par la consigne.

## Verdict

**Scellable après corrections.** Quatre corrections demandées (C1 à C4), deux conseillées (C5, C6). Aucune phrase ne déclare O4 libre ; aucune ne fait d'un « non trouvé » un trou du champ ; les onze nœuds sont recopiés à l'octet près. Le défaut principal est au point 10 : la ligne « Retenu » remplace la « demande à Lazar » de la note par un versement par la session, que ni la note ni R-3185 n'accordent.

## Couples de correction (ancien texte → nouveau texte)

**C1 (demandée, en-tête, citation tronquée).**
Ancien : `sont accordées ; elles ne font que restreindre ».`
Nouveau : `sont accordées ; elles ne font que restreindre la revendication ».`

**C2 (demandée, point 1).**
Ancien : `seule la réunion reste revendiquable, sous la lettre du nœud.`
Nouveau : `seule la réunion reste revendiquable, sous la lettre du nœud, sous la réserve du point 3 (défendabilité de ses composantes non tranchée) et du point 11 (« libre hors du dépôt » non déclarable).`

**C3 (demandée, point 5).**
Ancien : `les cinq pièces sont ajoutées aux citations obligatoires de O4, avec les mentions du nœud`
Nouveau : ``les pièces nommées par le nœud (boîte à outils *Assaying Anomalies* v0.4.0 au commit `f08a77f7…`, LLB, LLBSTACK, AUTODISC) sont ajoutées aux citations obligatoires de O4, à côté de SEADS, avec les mentions du nœud``

**C4 (demandée, point 10).**
Ancien : `Retenu : la liste et son ordre de priorité ; versement et lecture sous un feu de la mère, sans dépense de calcul. La phrase « aucun accès réseau ici » décrit l'état des agents de lecture ; le versement par la session sur des sources ouvertes (arXiv) reste possible, une tentative par source, sans contournement d'un refus.`
Nouveau : `Retenu : la liste, son ordre de priorité et la demande à Lazar, à la lettre du nœud ; lecture sans dépense de calcul. Remarque du rédacteur, hors des onze recommandations accordées et non tranchée ici : si la mère l'ordonne, la session peut tenter le versement des seules pièces en accès ouvert (arXiv, dépôt public de code), une tentative par source, sans contournement d'un refus, avec empreinte compagnon (R6) ; toute pièce refusée ou non ouverte reste demandée à Lazar. Rien de ce que ces pièces contiennent n'est opposable avant lecture sur PDF empreinté, page citée (R7).`

**C5 (conseillée, point 4).**
Ancien : `la phrase interdite et la phrase prescrite valent pour tout énoncé public.`
Nouveau : `la phrase interdite et la phrase prescrite valent pour tout énoncé public ; la phrase prescrite se dit à la profondeur déclarée (règle de lecture) et ne vaut pas déclaration « libre hors du dépôt » (point 11).`

**C6 (conseillée, portée).**
Ancien : `ne modifie ni N-064, ni N-067 (archivées telles quelles), ni le programme, ni la page publique.`
Nouveau : `ne modifie ni N-064, ni N-067 (archivées telles quelles), ni le programme, ni la page publique ; elle complète la liste des citations obligatoires de O4 fixée par N-067 (point 5) et se lit avec N-067, dont elle resserre la lettre sur O4.`

## Constats

1. **Recopie des onze nœuds — conforme (aucune gravité).** Comparaison par programme, ligne à ligne, des onze lignes numérotées de la section 7 de la note et des onze lignes citées (`> n. …`) du texte : onze égalités strictes sur onze, numéros 1 à 11 présents des deux côtés.

2. **Mots de Lazar — conformes ; lecture de la mère tronquée (mineure, C1).** Les deux citations « go recos, on ern est ou? » et « applique immediatement les recos en autonomie sans attendre » sont identiques à R-3185, de même que « (vers 05:00Z) ». La lecture de la mère est citée entre guillemets mais s'arrête à « restreindre » : R-3185 écrit « elles ne font que restreindre la revendication » (la chaîne « restreindre la revendication » est absente du texte, compte 0). Le sens n'est pas déformé ; une citation dite « au même registre » doit être entière ou marquer la coupe. Le reste de l'en-tête suit R-3185 : texte qui énonce les recommandations une à une, sous `docs/decisions/`, numéro par la mère, contre-lecture par un agent neuf avant toute phrase nouvelle dans un papier (le texte ajoute « ou une page publique », plus strict).

3. **Point 10 — la ligne « Retenu » sort de la recommandation (moyenne, C4).** Le nœud dit « (aucun accès réseau ici ; demande à Lazar) ». Le texte ne retient pas la demande à Lazar et ajoute que « le versement par la session sur des sources ouvertes (arXiv) reste possible ». Trois défauts : (a) ce n'est pas l'option de la note, et R-3185 n'accorde que les recommandations de la note ; (b) l'affirmation « décrit l'état des agents de lecture » n'est fondée sur aucune phrase de la note (son en-tête dit seulement « aucun accès réseau » pour la session de synthèse ; la section 1 montre qu'une tentative réseau a eu lieu ailleurs, HTTP 403 sur SSRN 4338007) ; (c) la liste contient des pièces qui ne sont pas sur une source ouverte nommée (Marrow et Nagel, Jensen, Kelly et Pedersen, Mullainathan et Rambachan, Yao et al.), que la phrase laisse sans voie. La clause « une tentative par source, sans contournement d'un refus » ne contredit aucune règle et reprend la pratique constatée en section 1 de la note ; elle ne contredit pas non plus la note sur le fond (la note constate une absence d'accès, elle n'interdit pas). Le défaut est de la présenter comme « retenue ». C4 la garde comme remarque non tranchée, sous ordre de la mère, et rétablit la demande à Lazar.

4. **Point 1 — « reste revendiquable » sans renvoi aux réserves (mineure, C2).** La lettre de la réunion contient « archive entière et croissante » et « ajusté avant le gel », deux des trois différences dont le point 3 dit que la défendabilité « n'est pas tranchée ». Lu seul, le point 1 peut passer pour un accord de revendication. La portée et le point 11 le bornent, mais le renvoi doit être dans la ligne. Aucun élargissement : la note dit « ne revendiquer que la réunion », le texte dit la même chose.

5. **Point 5 — compte « cinq pièces » non fondé (mineure, C3).** Le nœud demande d'ajouter la boîte à outils *Assaying Anomalies*, LLB, LLBSTACK et AUTODISC « à côté de SEADS » : quatre pièces ajoutées à côté d'une cinquième. Le texte dit « les cinq pièces sont ajoutées », ce qui compte SEADS parmi les ajouts ; la lettre du nœud ne le dit pas, et je n'ai pas lu dans N-067 (hors périmètre) si SEADS y figure déjà. Sans effet d'élargissement (citer plus restreint), mais la ligne se dit « à la lettre ». C3 nomme les pièces et retire le compte.

6. **Ce que la note laissait ouvert — correctement signalé (aucune gravité), une précision.** Point 2 : la demande de préversion aux auteurs est dite non tranchée et réservée à Lazar ; conforme (« je rédige, Lazar envoie »). Point 3 : la défendabilité des trois différences est dite non tranchée ; conforme. Point 9 : la phrase sur la nouveauté est conditionnée à la vérification ; conforme. Point 8 : le nœud offre deux libellés et marque l'un « option de cette note », non « option prudente » ; le texte retient celui-là et en tire la branche cohérente (correction d'ATLAS dans la v3 par une pièce neuve). C'est la seule option que la note marque comme sienne ; lecture acceptable, signalée pour que la mère sache que l'autre branche (« sans objet ») est écartée par cette ligne. Point 6 : « seul à pouvoir le fournir » est un ajout du rédacteur, compatible avec le refus consigné (une tentative, HTTP 403) et avec l'absence de contournement ; sans gravité une fois C4 portée.

7. **Aucune déclaration « libre », aucun trou du champ — conforme.** Recherche des phrases du rédacteur : « ne déclare rien libre », « le verdict "occupée en partie" reste celui de la note », règle de lecture (« non trouvé » = non trouvé dans les pièces lues, à la profondeur déclarée, R8), point 11 (« reste non déclarable »). La seule phrase qui appelle un énoncé public de « non trouvé » est la phrase prescrite du point 4, recopiée du nœud ; C5 (conseillée) la borne par la règle de lecture et le point 11.

8. **Portée et point 5 — tension de rédaction (mineure, C6 conseillée).** La portée dit que la décision « restreint » et « ne modifie ni N-064, ni N-067 » ; le point 5 ajoute des citations obligatoires « de O4 (N-067) ». Ce n'est pas une modification du fichier N-067 (même usage que N-067 envers N-064 : « ne modifie [pas] N-064 (archivée telle quelle) » tout en en remplaçant des points), mais la portée doit le dire.

9. **Cohérence avec N-067 (en-tête et section 0) — conforme.** N-067, section 0, point 4 : lire SSRN 6569258 et les pistes de priorité haute sur PDF « avant tout texte qui déclare O4 libre hors du dépôt ». Le point 11 du texte maintient cette clause et la durcit (article *Assaying Anomalies* et pistes du nœud 10 non lus). Rien dans le texte ne rouvre O1, le sceau de O3, O12 ou O17. Le gabarit de N-067 est suivi pour l'en-tête (décision, statut, portée, règle de lecture) ; le texte n'a pas de table d'options, les nœuds de la note n'en posant pas.

10. **Références de l'en-tête — contrôlées (aucune gravité).** Empreinte de la note : égale. Contre-lecture d'ensemble citée : commit `51ee2946` (dernier commit du fichier sur la branche locale) et empreinte `90334c4272f88ee1…`, égale à celle de l'en-tête de la note. Heure du statut (05:00:50Z) égale à la date de modification du fichier ; elle suit de 70 secondes l'heure de R-3185 (04:59:40Z) : cohérent, court ; sans conséquence.

## Ce que cette contre-lecture ne dit pas

Elle ne juge ni le fond des onze recommandations (objet de la contre-lecture d'ensemble déjà versée), ni les pièces neuves à venir (note d'englobement, v3, pièce de refus, programme de rejeu), dont le texte « n'est pas fixé ici » et qui restent à contre-lire une à une.

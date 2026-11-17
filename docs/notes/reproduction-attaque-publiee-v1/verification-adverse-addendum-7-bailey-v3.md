# Vérification de l'addendum 7 — passe finale sur le texte réécrit (commit 11954d70 : aucune lecture avant la clôture) — v3

Workflow `passe-finale-addendum-7-bailey` (run `wf_4b20f844-8b1`), lancé par la session `session_01XJ6MgnEhQMZteN9F8a1BST` le 17 novembre 2026 ; trois sous-agents neufs, un angle chacun ; cloisons : aucune note lue, `valider` et `lire` non appelés sur des dossiers réels. Retours reproduits tels quels.

## Angle : contre-lecture entière (R2) — bloquant : oui

Non scellable en l'état : un bloquant, six « à corriger », six remarques. Fichier relu : /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md au commit 11954d70, identique au disque. Aucun fichier modifié, aucune pièce sous cloison ouverte, `valider` et `lire` non appelés ; les essais n'ont pas été rejoués.

Le bloquant est la puce neuve « Refus ou erreur à la lecture » du § 3. Elle ne dit pas si un refus levé par `valider` ou `lire` vaut « pas de verdict » ou se corrige, ni si la lecture faite après correction est retenue ; « le premier lancé fait foi » et la puce « Après le lancement du premier lecteur » disent le contraire. Elle ne borne pas non plus la correction. Pour une confirmation à K′ ≥ 71, le verdict retenu en dépend, et le choix se fait après des résultats lus.

(1) Écarts nommés et rattachés.
- Bien rattachés : la série neuve, le poste et B = 85, la garde de durée, le filtre.
- Le crédit par la seule recharge : le mot « vast se recharge tout seul » est rendu fidèlement au § 2.5 ; la condition qui reste (crédit au moins égal au seuil de recharge) contrôle que la recharge marche et n'exige aucun versement.
- Sans rattachement ni acceptation par le mot de lancement : l'ordre de lecture (« à la lettre » contredit la note du mot), les règles du § 3, la seconde tentative, les modalités du § 2.5.

(2) Cohérence interne.
- Le moment de la clôture n'est pas fixé quand une suite reste permise (mise en place refaite, seconde tentative, ligne neuve, relevé du § 2.5).
- Deux formules ne tiennent pas avec un seul lecteur ou un run arrêté par Lazar.
- Phrases complètes ; renvois justes : l. 69-71, 165, 243-245, 249-251, 329-338, 340, 363-374 du texte, addendum 4 § 2.2, addendum 5 § 4, l. 143 du poste v12.

(3) Fidélité au texte.
- Régimes (l. 331-332), nœud 5 (l. 340), seuils et critères gelés : inchangés.
- Deux écarts non nommés : la mise en place refaite (l. 363) et le run tronqué arrêté par Lazar (l. 338).
- La parenthèse du § 3 laisse hors de l'interdit les notes des pilotes et de la première exécution de la série 3 (même graine).

(4) Constats des passes précédentes.
- Sans objet avec le nouvel ordre : mot de lancement après la lecture, tentative décidée après la lecture, causes « sans décision », délais comptés depuis la lecture, compte vidé, réserve à porter.
- Traités : K′ établi par la lecture, empreintes de suffixe, cloisons des lecteurs, un lecteur par verdict, provenance du taux de 1,108 USD/h, échéance, objet du GO, libellé d'arrêt, essais complémentaires.
- Encore ouverts : la voie de correction après un défaut de lecture (le bloquant) ; le lancement du second lecteur verdict connu ; le statut d'une mise en place refaite ; la seconde tentative à soumettre à Lazar.

Vérifié par recalcul ou empreinte :
- Chiffres : K = 72 pour (85, 8, 1,6, 1 800), bornes de D à 8,76 et 9,68, échéances du 27 novembre 17:44Z et du 28 novembre 02:48Z.
- Empreintes : fb6c2f34, 75cf4049 (au commit 873ab00c), 36573ae2, 82ef2fa0, e573e4c7, 70e4f7f2, f1c2ca52, 74df1fbf, 7f03f882, 546aa0bc, a902256b, e99a2d92, 9a879463, 972928bb, 6c445f3e ; 45 fichiers scellés dans `lecture-assemblee-v1`.
- Un fait à préciser : le « Texas » du relevé de 00:51Z est la machine 146917, pas la machine 146915 éprouvée.

### 1. bloquant — § 3, l. 130-134 (« Refus ou erreur à la lecture ») ; contre l. 124-126 (« le premier lancé fait foi ») et l. 147-149 (« Après le lancement du premier lecteur »)

**Constat.** La règle neuve sur les refus et erreurs de lecture laisse deux lectures opposées sur trois points. Elles se tranchent après le lancement du premier lecteur, donc peut-être quand la session connaît déjà le verdict de l'autre run. (a) Un refus levé par le code n'est plus classé. `lecture_v8.valider` et `lire` lèvent des `GardeArret` (« état de la règle absent ou non conforme après transfert », « journal absent », « évaluation absente du journal »). La version du commit 0c373143 écrivait « un refus de `valider` ou de l'assemblage n'est pas un verdict : pas de verdict », et les addenda 5 (§ 5 (d)) et 6 (§ 5 (d)) disent « assemblage refusé : pas de verdict, nœud ». Ici le refus de l'assemblage devient corrigeable, et le refus de `valider` n'est ni un « état rendu » ni clairement une « erreur d'exécution ». (b) Le statut de la lecture faite après correction n'est pas écrit. La puce précédente dit que tout autre lecteur lancé pour le même verdict est rapporté et que le premier lancé fait foi ; la puce « Après le lancement du premier lecteur » dit qu'aucune relecture décidée ensuite n'est retenue. On peut donc soutenir que le verdict du lecteur neuf est celui du run, ou qu'il est seulement rapporté à côté. (c) Rien ne borne la correction, ni dans son objet (elle peut desserrer un refus ou une garde) ni dans son délai (elle peut ne jamais venir). Pour une confirmation à K′ ≥ 71, chacune de ces lectures fait basculer le verdict retenu entre la confirmation et les 36 tours. C'est la voie « défaut technique » des deux passes adverses, revenue après la clôture.

**Correction.** Remplacer « Un refus de l'assemblage ou une erreur d'exécution du code de lecture, constatés sur la commande consignée rejouée une seconde fois à l'identique, sans qu'aucune valeur de note ait été rendue : nœud ; correction du seul code de lecture par un addendum neuf, contre-lu (R2), puis lecture par un lecteur neuf. » par « Un refus levé par le code lui-même (`GardeArret` de `valider`, de `lire` ou de l'assemblage : pièce absente, altérée ou non conforme) n'est pas un verdict : « pas de verdict » pour ce run, sans correction (addendum 5, § 5 (d) ; addendum 6, § 5 (d)). Une erreur d'exécution qui n'est pas un tel refus, constatée sur la commande consignée rejouée une seconde fois à l'identique, sans qu'aucune valeur de note ait été rendue : nœud ; correction du seul code en cause, sans toucher à aucun critère gelé, seuil, garde ni refus, par un addendum neuf, contre-lu (R2), dû quel que soit l'autre verdict et scellé au plus tard 72 h après le constat ; puis lecture par un lecteur neuf. Ce lecteur fait foi pour ce run (seule exception à « le premier lancé fait foi ») ; sa lecture n'est pas une relecture au sens de la puce « Après le lancement du premier lecteur », et le verdict qu'il rend est celui du run pour la règle du verdict retenu. Sans addendum scellé dans ce délai, ou si une valeur de note a été rendue avant l'erreur : « pas de verdict » pour ce run. » (Si l'auteur préfère qu'un refus de `valider` soit corrigeable, il l'écrit, mais l'une des deux lectures doit être fixée avant le scellement.)

### 2. à corriger — § 3, l. 119-128 (lancement des lecteurs ; « Chaque verdict est scellé tel qu'il est rendu »)

**Constat.** Les deux lecteurs sont « lancés dans les 24 h qui suivent la clôture », sans ordre entre eux. La session peut donc recevoir le premier verdict avant de consigner le lancement du second (fichiers donnés, commande, choix entre la sortie de la conduite et le dossier de reprise). Elle peut aussi écrire l'addendum de correction d'une erreur de lecture en connaissant l'autre verdict. C'est le reste du constat « lecteurs » de la seconde passe (angle adversaire, point 3) : la commande est bien consignée et rejouée, mais elle peut l'être verdict connu.

**Correction.** Remplacer « est consigné avant qu'il ne rende » par « est consigné avant qu'aucun des deux lecteurs n'ait rendu ». Remplacer « Chaque verdict est scellé tel qu'il est rendu. » par « Chaque verdict est scellé tel qu'il est rendu ; la session ne l'ouvre pas tant que l'autre n'est pas scellé ou son absence constatée, et tout addendum de correction (puce suivante) est écrit sans le connaître. »

### 3. à corriger — § 1, l. 27-28 ; titre du § 2, l. 48 ; § 6, condition 7, l. 210-212 ; § 6, étape 2, l. 222

**Constat.** Trois choix de la session ne sont rattachés ni à un mot de Lazar ni à son acceptation en bloc. (1) L'ordre de lecture : « C'est 2 puis 1 à la lettre » contredit la note du mot (`…-2355-decision-lazar-bailey-2-puis-1.md`, `93494ff9…`), qui engageait « (i) addendum, (ii) puis le verdict à 36 tours, (iii) puis le run neuf ». C'est un écart à l'ordre présenté, déclaré comme choix de la session, mais la condition 7 ne fait accepter que « les paramètres du § 2 ». (2) La règle du verdict retenu, la clôture et la règle de refus du § 3 décident quel verdict vaut pour l'étape 1. C'est de la nature de la condition 5 du texte (mot de Lazar avant la création), et elles ne sont pas non plus couvertes par la condition 7. (3) La seconde tentative du § 2.3 et les modalités du § 2.5 (crédit au moins égal au seuil de recharge, alerte sous 4 USD) manquent au titre du § 2 ; la contre-lecture d'origine (M-2) voulait la seconde tentative soumise à Lazar. Par ailleurs, l'étape 2 n'envoie à Lazar ni le § 2 ni l'addendum (l'addendum 6, § 6, exigeait chemin et empreinte). Le mot « vast se recharge tout seul » est rendu fidèlement au § 2.5 (verbatim, note `7f03f882…` vérifiée).

**Correction.** § 1 : remplacer « C'est « 2 puis 1 » à la lettre. » par « C'est un écart à l'ordre que consignait la note du « go 2 puis 1 » ((i) addendum, (ii) verdict à 36 tours, (iii) run neuf ; `93494ff9…`) ; il est soumis à Lazar avec la demande du mot de lancement (condition 7). » Titre du § 2 : remplacer « plafond de durée et filtre : calcul de la session » par « plafond de durée, seconde tentative (§ 2.3), filtre et modalités du § 2.5 : calcul de la session ». Condition 7 : remplacer « Il accepte ou refuse en bloc la confirmation et les paramètres du § 2 ; donné avant le scellement de cet addendum, il ne vaut que si le § 2 scellé est identique aux paramètres portés à sa connaissance ; » par « Il accepte ou refuse en bloc la confirmation, les paramètres du § 2, l'ordre de lecture (§ 1) et les règles du § 3 (clôture, verdict retenu, refus ou erreur à la lecture), qui sont un choix de la session ; donné avant le scellement de cet addendum, il ne vaut que si les § 2 et 3 scellés sont identiques à ce qui a été porté à sa connaissance ; ». Étape 2 : remplacer « avec le § 2 bis, les risques du § 5 et le tirage attendu sur la carte » par « avec cet addendum (chemin, empreinte), les § 2 et 2 bis, l'ordre de lecture et la règle du verdict retenu (§ 3), les risques du § 5 et le tirage attendu sur la carte ».

### 4. à corriger — § 3, l. 111-118 (clôture) et l. 149-150 ; § 2.3, l. 73-74 ; § 2.5, l. 89-90 ; § 6, condition 2, l. 206-208

**Constat.** Le moment de la clôture n'est pas fixé dans les cas où une suite reste permise « avant la clôture », et la liste (ii) se lit alors de deux façons. (a) « Garde de mise en place » figure comme cause de clôture, alors que le § 2.1 garde la liste d'arrêt « sans changement » et que la l. 363 du texte permet de refaire la mise en place (addendum 5, § 4 : sur un nouveau mot de Lazar). Le statut d'une mise en place refaite n'est écrit nulle part : la dernière puce du § 3 ne compte dans « la confirmation » que la seconde tentative et la relance. C'est le reste du second bloquant de la seconde passe (angle adversaire, point 4). (b) « Pas de seconde tentative » (§ 2.3), « échéance, sauf ligne neuve accordée avant la clôture » (condition 2) et « condition du § 2.5 non tenue » (un relevé sous le seuil peut tenir un instant plus tard) n'ont ni délai ni auteur du constat. (c) Les journaux perdus (instance supprimée avant la reprise de la lecture 38, § 5 (c)) n'ont pas de cas de clôture. Aucune de ces décisions ne connaît un résultat : ce n'est plus une voie liée au signe, mais la règle n'est pas applicable telle quelle.

**Correction.** § 3 (ii) : remplacer « garde de mise en place, » par « garde de mise en place non refaite (l. 363 ; addendum 5, § 4 : sur un mot de Lazar, avant la clôture), » ; après « K < 20 à la règle, » insérer « journaux perdus (reprise de la lecture 38 impossible), ». Après « Après la clôture, rien n'est ajouté à la confirmation. » ajouter : « Quand une suite reste permise (seconde tentative du § 2.3, relance par le chemin de l'addendum 5, mise en place refaite, nouveau relevé du § 2.5, ligne de GO neuve), la note de clôture attend le mot de Lazar : elle est écrite à son refus, et au plus tard à l'échéance de la ligne de GO (condition 2). Dans les autres cas, elle est écrite dès le constat. » Dernière puce du § 3 : remplacer « seconde tentative du § 2.3 et relance de la l. 371 comprises » par « seconde tentative du § 2.3, relance de la l. 371 et mise en place refaite (l. 363) comprises ». § 2.5 : remplacer « sinon aucune création. » par « sinon aucune création : le relevé est repris, et la condition n'est dite non tenue (§ 3) qu'à l'échéance de la ligne de GO ou sur le mot de Lazar. »

### 5. à corriger — § 3, l. 107-108

**Constat.** La parenthèse « (relance à 36 tours, confirmation) » peut se lire comme la liste fermée des notes interdites. Or le texte permet déjà d'ouvrir les notes des pilotes (l. 241-242 : après la fin du run principal) et celles de la première exécution de la série 3 (l. 371 : après la fin de la relance). Cette première exécution compte 8 tours sous la graine du run principal, celle de la relance et de la confirmation (risque (d)) ; ses notes sont dans `lecture-assemblee-v1`. Les ouvrir avant la clôture donnerait une partie du résultat. À l'inverse, la phrase « aucune note de juge n'est lue » heurte à la lettre le contrôle du juge de la mise en place neuve et les gardes automatiques, que le texte ne tient pas pour des lectures (point M-8 de la contre-lecture d'origine, resté sans suite).

**Correction.** Remplacer « Aucune note de sonde ni de juge du témoin (relance à 36 tours, confirmation) n'est lue, par aucune session ni aucun lecteur, avant la clôture de la confirmation. » par « Aucune note de sonde ni de juge du témoin (séries 1 à 3, pilotes et première exécution compris ; relance à 36 tours ; confirmation, pilotes et tentatives compris) n'est lue, par aucune session ni aucun lecteur, avant la clôture de la confirmation, même là où le texte le permettrait plus tôt (l. 241-242, 371). Les gardes automatiques (l. 268-270) et le contrôle du juge de la mise en place (l. 231 : « ce n'est pas une lecture de résultat ») ne sont pas des lectures. »

### 6. à corriger — § 1, l. 43-44 ; § 2 bis, l. 98-99 ; § 5 (b), l. 184-185

**Constat.** Le « Texas 1,2816 USD/h » du relevé de 00:51Z n'est pas la machine éprouvée. Le fichier `releve-offres-filtre-addendum-7-20261117-0051.txt` (`e99a2d92…`, vérifié) donne l'offre 59284723 sur la machine 146917, alors que la machine des tours 0 à 7 de la série 3 est la 146915 (même processeur). À ce relevé, aucune des deux offres conformes n'est sur la machine éprouvée ; l'autre est en Caroline du Nord (machine 151320, AMD EPYC 7763). Le devis « hôte comme celui du Texas » et le risque (b) (« hors la machine du Texas ») laissent croire le contraire à qui donne le mot de lancement. La garde de 1 800 s couvre le risque ; c'est le fait qui doit être dit.

**Correction.** § 1 : remplacer « au filtre du § 2.4 : deux offres, Texas 1,2816 USD/h et Caroline du Nord 1,5505 USD/h » par « au filtre du § 2.4 : deux offres, Texas 1,2816 USD/h (machine 146917, autre que la machine 146915 éprouvée, même processeur) et Caroline du Nord 1,5505 USD/h (machine 151320, AMD EPYC 7763) ; à ce relevé, aucune offre conforme n'est sur la machine éprouvée ». § 2 bis : remplacer « Les machines autres que celle du Texas » par « Les machines autres que la machine 146915 du Texas ». § 5 (b) : remplacer « hors la machine du Texas » par « hors la machine 146915 du Texas ».

### 7. à corriger — § 3, l. 122-123 et l. 136-137

**Constat.** Deux formules ne tiennent pas quand il n'y a qu'un lecteur ou quand Lazar arrête un run. (a) « Aucun verdict n'est rapporté avant que les deux lecteurs aient scellé le leur » : sous les clôtures (ii) et (iii) il n'y a qu'un lecteur, et après une erreur de lecture le premier lecteur ne scelle rien ; à la lettre, le verdict à 36 tours ne serait jamais rapporté. (b) Le second lecteur n'est lancé que « si la clôture est du cas (i) ». Un run principal arrêté par Lazar (cas (iii)) avec K′ ≥ 20 et des journaux transférés ne serait donc jamais lu, alors que la l. 338 du texte le lit comme un run tronqué : écart au texte non nommé, sans effet sur le verdict retenu (K′ ≤ 70). Le dossier assemblé d'une relance passée par le chemin de l'addendum 5 manque aussi à la parenthèse.

**Correction.** Remplacer « aucun verdict n'est rapporté avant que les deux lecteurs aient scellé le leur » par « aucun verdict n'est rapporté avant que chaque verdict attendu soit scellé, ou son absence constatée ». Remplacer « l'autre, si la clôture est du cas (i), sur la sortie de la conduite de confirmation (ou son dossier de reprise) » par « l'autre, si des journaux d'un run principal de la confirmation sont transférés et scellés (cas (i), ou cas (iii) avec K′ ≥ 20, lu comme un run tronqué, l. 338), sur la sortie de la conduite de confirmation (ou son dossier de reprise, ou le dossier assemblé si la relance a suivi le chemin de l'addendum 5) ».

### 8. remarque — § 2.3, l. 73

**Constat.** « D ≈ 6 à 9 USD : K = 72 tant que D ≤ 8,7 USD, 71 jusqu'à 9,6 USD » vaut au pire cas (c = 1,6 USD/h, t = 1 800 s), ce que la phrase ne dit pas. Elle ne dit pas non plus la suite : si la perte de la première tentative est doublée (pilote repris), D peut passer 9,6 USD. Exemple recalculé : D = 12, c = 1,6, t = 1 800 donne K = 68. La seconde tentative courrait alors au régime réduit, sans pouvoir être retenue, jusqu'à B − 2.

**Correction.** Remplacer « D ≈ 6 à 9 USD : K = 72 tant que D ≤ 8,7 USD, 71 jusqu'à 9,6 USD. » par « D ≈ 6 à 9 USD : au pire cas (c = 1,6 USD/h, t = 1 800 s), K = 72 tant que D ≤ 8,7 USD, 71 jusqu'à 9,6 USD ; au-delà, K ≤ 70 : la série court au régime réduit et ne peut pas être retenue (§ 3). »

### 9. remarque — § 2.5, l. 89-92

**Constat.** Trois détails du crédit. (a) c₀ n'est pas défini dans cet addendum : celui de l'addendum 6 était l'offre la moins chère du filtre du poste v12, et il ne sert plus à aucun seuil. (b) « Comme à l'addendum 6 » ne reprend que deux des trois alertes : celle sur o (dépassement de 0,5 USD/h) n'est ni reprise ni retirée. (c) La fraîcheur du relevé n'est plus dite, alors que le poste peut attendre une offre 24 h (§ 2.4) sans relever le crédit (addendum 6, risque (e)).

**Correction.** Remplacer « relevé (champs, heure, c₀, o) consigné dans l'ordre de lancement » par « relevé (champs, heure, o) fait au lancement du poste, non repris pendant l'attente d'une offre, consigné dans l'ordre de lancement ». Remplacer « alerte à Lazar sous 4 USD de crédit ou si `billing_failed` est vrai. » par « alerte à Lazar sous 4 USD de crédit ou si `billing_failed` est vrai (l'alerte sur o de l'addendum 6 n'est pas reprise). »

### 10. remarque — § 6, condition 7, l. 212 ; § 3 (ii), l. 114

**Constat.** « Un mot assorti d'une condition vaut refus » venait de la version où le mot devait précéder la lecture. Avec le nouvel ordre, « mot de lancement refusé » est une cause de clôture : un mot ambigu fermerait la confirmation et ferait lancer la lecture des 36 tours sous 24 h, sans retour possible (« après la clôture, rien n'est ajouté »). La règle n'a plus d'utilité contre le signe et devient coûteuse.

**Correction.** Remplacer « un mot assorti d'une condition vaut refus ; » par « un mot assorti d'une condition ne vaut pas mot de lancement : la demande est renouvelée ; seul un refus exprès est une cause de clôture (§ 3) ; ».

### 11. remarque — § 5 (c), l. 186 ; § 1, l. 11-12

**Constat.** Deux formulations de fait. (a) « Une recharge a déjà fait défaut le 13 novembre » : l'addendum 6 (§ 2, surveillance) écrit « Le 12 novembre, le défaut de recharge… » ; les relevés donnent un dernier paiement le 12 à 23:46Z et un compte vide le 13 vers 04:21Z. (b) « A fini […] par la garde de dépense […] aucune garde tombée » se contredit à la lettre ; le bilan (`bilan-conduite-v5.json`, champs techniques) porte `cause_arret` « dépense » et une liste de gardes tombées vide.

**Correction.** § 5 (c) : remplacer « le 13 novembre » par « dans la nuit du 12 au 13 novembre ». § 1 : remplacer « aucune garde tombée » par « aucune autre garde tombée ».

### 12. remarque — En-tête, l. 6 ; § 1, l. 18-19 et l. 26 ; section « Contre-lecture », l. 238-239

**Constat.** Traçabilité. (a) Les états intermédiaires cités s'arrêtent à `0c373143` ; l'état relu par la passe finale est le commit `11954d70`. (b) Les deux notes du 16 novembre sont citées sans empreinte, à la différence des autres (vérifiées : `df9a3eda…` pour la question de l'ordre, `93494ff9…` pour « go 2 puis 1 »). (c) « Rapporté à Lazar » est au passé, alors que la note `74df1fbf…` dit que le choix sera rapporté dans le message qui annonce le scellement. (d) La seconde passe comptait bien quatre bloquants, mais « lecteurs » y était un « à corriger » ; le quatrième bloquant était la liste des défauts qui couvrait la garde de dépense.

**Correction.** En-tête : remplacer « commits `c44c6d65` et `0c373143` » par « commits `c44c6d65`, `0c373143` et `11954d70` ». § 1 : ajouter « (`df9a3eda…`) » et « (`93494ff9…`) » après les deux notes ; remplacer « et rapporté à Lazar : » par « et rapporté à Lazar dans le message qui annonce le scellement : ». Section « Contre-lecture » : remplacer « ; relance, reprise et compte vidé ; lecteurs). » par « ; liste des défauts couvrant la garde de dépense ; relance, reprise et compte vidé), et un « à corriger » sur les lecteurs. »

### 13. remarque — § 3, l. 119-120 ; § 6, l. 215

**Constat.** Deux bornes sans conséquence écrite. (a) Rien ne dit ce qui arrive si un lecteur n'est pas lancé dans les 24 h qui suivent la clôture (session arrêtée, fin de l'autonomie). (b) « Ordre, sans autre étape » ne mentionne pas les suites permises avant la clôture (seconde tentative, relance par le chemin de l'addendum 5), qui demandent des pièces neuves et un mot de Lazar.

**Correction.** Après « lancés dans les 24 h qui suivent la clôture » ajouter « (un lancement plus tardif est rapporté avec sa cause et ne change aucune règle) ». Remplacer « Ordre, sans autre étape : » par « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) : ».

## Angle : adversaire (nouvel ordre) — bloquant : oui

Ne pas sceller en l'état : un bloquant, dans la phase de lecture, après la clôture. Le nouvel ordre ferme bien tout ce qui précède la clôture ; il reste six points à corriger et trois remarques.

Le bloquant : la session reçoit le premier verdict avant que le sort du second soit fixé. Le texte nomme deux dossiers pour le lecteur de la confirmation (« la sortie de la conduite (ou son dossier de reprise) »). Après une reprise, cas probable avec le crédit par recharge seule, le premier donne « pas de verdict » ou « non interprétable », le second le vrai verdict. Ce choix, fait verdict à 36 tours connu, change le verdict retenu. Même prise pour un second lecteur non lancé, un lecteur qui ne rend pas, ou un refus et une erreur. Cinq remplacements courts le ferment : dossier et commande nommés dans la note de clôture, lecteurs lancés ensemble, rapports scellés par les lecteurs et non ouverts avant les deux scellements.

Voies fermées par le nouvel ordre (aucun résultat connu au moment de la décision) :
- mot de lancement, offre, échéance ;
- crédit, recharge, fonds de la carte, compte vidé (§ 2.5, § 5 (c)) ;
- seconde tentative du § 2.3, relance de la l. 371, reprise ;
- fin par Lazar ;
- champs techniques : les journaux de gardes ne portent que des noms et des états ; « sonde orientée » ou un contrôle du juge tombés finissent la série par règle, sans décision ouverte.

Voies non fermées, à corriger :
- **Périmètre de « aucune note »** : la parenthèse « (relance à 36 tours, confirmation) » oublie le pilote et la première exécution de la série 3, soit onze tours aux graines de la confirmation, que le texte permet d'ouvrir dès maintenant (l. 241-242, 371).
- **Lecture anticipée ordonnée par Lazar, ou faite malgré la règle** : aucun effet écrit ; le cas (iii) a deux lectures ; la demande du mot de lancement ne cite pas l'ordre de lecture.
- **Pièces antérieures** : le brief et la passation du 15 novembre et la note « 2 puis 1 » placent encore le verdict à 36 tours juste après le scellement, sans être remplacés.
- **Clôture** : la session la constate seule et peut éteindre des suites que le texte donne à Lazar ; « un mot assorti d'une condition vaut refus » est devenu trop large.
- **Run arrêté par Lazar** : lu ou non, deux lectures.
- **« Relecture » et définition de « la confirmation »** : deux prises possibles après lecture.

Le § 2.5 est fidèle au verbatim « vast se recharge tout seul » et au relevé ; seule l'attribution du titre du § 2 est à préciser (remarque).

Cloisons tenues : aucun journal de notes ni journal technique ouvert, `valider` et `lire` non appelés, aucune commande réseau, aucun fichier du dépôt modifié ni créé. Une copie de travail de l'addendum est hors dépôt : /tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/addendum7.md. Chaque texte à remplacer a été vérifié présent une seule fois dans l'addendum au commit 11954d70.

Pièces lues :
- /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md
- /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1.md, addenda 5 et 6 en entier, addenda 1 à 4 par recherche
- /home/user/controle-ia-travail/docs/notes/reproduction-attaque-publiee-v1/verification-adverse-addendum-7-bailey-v1.md et -v2.md, et contre-lecture-addendum-7-confirmation-bailey-v1.md
- /home/user/controle-ia-travail/registres/passations/ : les notes du témoin des 15, 16 et 17 novembre
- /home/user/controle-ia-travail/src/controle_ia/temoin_bailey/lecture_v8.py, lanceur_v21.py, analyse_v3.py, journaliseur_v3.py
- /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/releve-offres-filtre-addendum-7-20261117-0051.txt

### 1. bloquant — § 3 : l. 117-118 (fin de « Clôture »), l. 119-129 (« Les deux verdicts »), l. 130-134 (« Refus ou erreur »), l. 135-137 (« Rapport »), l. 147 (« Après le lancement du premier lecteur »)

**Constat.** Voie restante, après la clôture : la session reçoit le premier verdict avant que le sort du second soit fixé. Le texte prévoit lui-même des lecteurs lancés l'un après l'autre (« lancés dans les 24 h », « Après le lancement du premier lecteur »), et « chaque verdict est scellé tel qu'il est rendu » : c'est la session qui le reçoit. La cloison écrite ne vise que les lecteurs et le rapport à Lazar, pas la session. Verdict à 36 tours connu, quatre leviers décident encore si la confirmation a un verdict, donc lequel est retenu. (1) Le dossier donné au second lecteur : le texte en nomme deux, « la sortie de la conduite de confirmation (ou son dossier de reprise) ». Après une reprise (cas probable sous le § 2.5 : recharge qui échoue, instance arrêtée par Vast), les journaux sont dans un sous-dossier de reprise (`lanceur_v21.py`, docstring l. 206-212 ; la série 3 en a eu deux, `reprise-v10-2`). Sur la sortie de la conduite, `valider` rend « Pas de verdict » (aucun journal transféré : K′ = 0, `lecture_v8.py` l. 524-532) ou « Non interprétable (garde de fin de run) » (transfert sans foi, l. 556-557), que le § 3 tient pour une issue des critères gelés ; sur le dossier de reprise, il rend le vrai verdict. Le choix du dossier, fait verdict à 36 tours connu, change le verdict retenu. Après une relance par le chemin de l'addendum 5, le dossier assemblé n'est nommé nulle part. (2) Ne pas lancer le second lecteur dans les 24 h : aucun effet n'est écrit, et la règle range « pas de verdict … quelle qu'en soit la cause » du côté du verdict à 36 tours. (3) Un lecteur qui s'arrête sans rendre : « le premier lancé fait foi » ne dit pas s'il est remplacé. (4) Un refus ou une erreur : le nœud et la correction sont tranchés par qui connaît l'autre verdict, et rien n'est écrit si rien n'est corrigé (aucun verdict ne peut alors être rapporté).

**Correction.** (a) § 3, « Clôture » : « Après la clôture, rien n'est ajouté à la confirmation. » → « Après la clôture, rien n'est ajouté à la confirmation. La note de clôture nomme, pour chaque verdict à lire, le dossier donné au lecteur (pour la confirmation : la sortie de la conduite ; le dossier de reprise s'il y a eu reprise ; le dossier assemblé, fait avant la clôture, s'il y a eu relance par le chemin de l'addendum 5) et la commande ; ils ne changent plus. »
(b) « Les deux verdicts » : « lancés dans les 24 h qui suivent la clôture » → « lancés ensemble dans les 24 h qui suivent la clôture, chacun avant que l'autre n'ait rendu » ; et « sur la sortie de la conduite de confirmation (ou son dossier de reprise) » → « sur le dossier que nomme la note de clôture ».
(c) « Chaque verdict est scellé tel qu'il est rendu. » → « Chaque lecteur écrit et scelle lui-même son rapport ; il ne rend à la session que l'empreinte de ce rapport, ou la mention « refus ou erreur » sans aucune valeur. La session n'ouvre aucun rapport avant que chaque lecteur lancé ait scellé le sien, ou que la suite d'un refus ou d'une erreur soit close. Un lecteur qui s'arrête sans rien rendre est remplacé par un lecteur neuf, sur la même consigne ; c'est rapporté. »
(d) « Refus ou erreur » : « puis lecture par un lecteur neuf. » → « puis lecture par un lecteur neuf ; le nœud est tranché sans ouvrir l'autre rapport ; si rien n'est corrigé : « pas de verdict (erreur de lecture) » pour ce run. »
(e) « Rapport » : « aucun verdict n'est rapporté avant que les deux lecteurs aient scellé le leur » → « aucun verdict n'est ouvert par la session ni rapporté avant que chaque lecteur lancé ait scellé le sien ».
Si l'auteur ne veut pas que les lecteurs scellent eux-mêmes : garder au moins (a), (b), (d) et la dernière phrase de (c).

### 2. à corriger — § 3, l. 107-108 ; texte l. 241-242 et 371 ; § 1, l. 27

**Constat.** La règle centrale énumère « (relance à 36 tours, confirmation) ». Elle ne nomme ni les notes du pilote de la série 3 (3 tours), ni celles de sa première exécution (8 tours, graine 1865327867, celle de la relance et du run principal de la confirmation), ni les journaux d'égalités. Or le texte, qui prime, permet de les ouvrir dès maintenant : notes du pilote « ouvertes après la fin du run principal et le scellement de ses journaux » (l. 241-242) ; notes de la première exécution ouvertes « après la fin de la relance et le scellement de ses journaux » (l. 371). Ces conditions sont remplies depuis le 15 novembre, et les fichiers sont dans `lecture-assemblee-v1` (`pilote/…`, `principal/…`). Lue comme une liste, la parenthèse laisse une session les ouvrir avant le mot de lancement : onze tours aux graines mêmes de la confirmation. Le § 1 (« aucune note n'est lue ») dit l'intention ; le § 3, qui fixe la règle, doit la porter.

**Correction.** « Aucune note de sonde ni de juge du témoin (relance à 36 tours, confirmation) n'est lue » → « Aucune note de sonde ni de juge du témoin (série 3 : pilote, première exécution et relance ; confirmation : pilotes et exécutions ; journaux d'égalités compris ; y compris ce que le texte permet déjà d'ouvrir, l. 241-242 et 371) n'est lue ».

### 3. à corriger — § 1, l. 28 ; § 3, l. 117 (cas (iii)) ; § 6, l. 222 (demande du mot de lancement)

**Constat.** Lecture anticipée ordonnée par Lazar : non fermée. Le texte l'annonce (« par un addendum neuf ») sans y attacher d'effet. Après une telle lecture, tout ce que les deux passes précédentes avaient trouvé se rouvre (fin par Lazar, fonds de la carte, mot de la seconde tentative ou de la relance, reprise). Le cas (iii) se lit alors de deux façons : « sans aucune lecture » est une condition (aucune clôture n'est prévue), ou une description (Lazar lit, arrête, et le verdict lu est retenu sans réserve). Même vide pour une lecture faite malgré la règle (dossier lisible, § 5 (e)) : aucune conséquence n'est écrite. Enfin la demande du mot de lancement ne cite pas l'ordre de lecture, alors que Lazar a reçu vers 00:49Z « sans ce mot, le verdict attend ton réveil » (note du choix, l. 24-25) et que le mot en bloc ne porte que sur le § 2 : un « lis-le maintenant » de sa part est le chemin le plus probable vers cette lecture.

**Correction.** (a) § 1 : « Lazar peut ordonner une lecture plus tôt : ce serait un écart à cet addendum, par un addendum neuf. » → « Lazar peut ordonner une lecture plus tôt : ce serait un écart à cet addendum, par un addendum neuf, scellé avant cette lecture. Dès qu'une note ou un verdict du témoin est lu avant la clôture, par qui que ce soit (lecture ordonnée, ou faite malgré le § 3), c'est consigné avec ce qui a été vu ; toute décision prise ensuite sur la confirmation (fin, seconde tentative, relance, reprise, mot, crédit) est rapportée « décidée après une lecture », et le verdict retenu porte cette réserve partout où il est cité. »
(b) § 3 : « (iii) Lazar y met fin, sans aucune lecture ; c'est rapporté comme sa décision. » → « (iii) Lazar y met fin ; c'est rapporté comme sa décision, avec la réserve du § 1 si une lecture a précédé. »
(c) § 6, étape 2 : « avec le § 2 bis, les risques du § 5 et le tirage attendu sur la carte » → « avec l'ordre de lecture du § 3 (aucun verdict avant la clôture), le § 2 bis, les risques du § 5 et le tirage attendu sur la carte ».

### 4. à corriger — § 5 (e), l. 194-196 ; § 1, l. 22-28

**Constat.** Des pièces scellées du dépôt commandent encore l'ancien ordre et seraient suivies par une session qui reprend le témoin : le brief `registres/passations/2026-11-15-1843-brief-lancement-session-neuve-temoin-bailey-choix-et-verdict.md` (l. 51-53 : « le verdict à 36 tours reste celui du texte et se fait après le scellement de l'addendum »), la passation du même jour (l. 38-40) et la note `registres/passations/2026-11-16-2355-decision-lazar-bailey-2-puis-1.md` (« (ii) puis le verdict à 36 tours (R13) »). L'addendum dit qu'il change l'ordre, mais pas qu'il remplace ces pièces. « Par aucune session » ne tient que si la session suivante lit l'addendum avant elles ; le risque (e) ne nomme que la discipline.

**Correction.** § 5 (e) : « la cloison repose sur la discipline des sessions, comme depuis le début du témoin. » → « la cloison repose sur la discipline des sessions, comme depuis le début du témoin. Sur l'ordre de lecture, cet addendum remplace le brief `registres/passations/2026-11-15-1843-brief-lancement-session-neuve-temoin-bailey-choix-et-verdict.md`, la passation du même jour et la note `registres/passations/2026-11-16-2355-decision-lazar-bailey-2-puis-1.md`, qui placent le verdict à 36 tours après le scellement de l'addendum ; toute passation et tout brief écrits avant la clôture le disent en tête. »

### 5. à corriger — § 3, l. 111-118 (« Clôture ») ; § 2.3, l. 69-70 ; § 6, l. 208 et l. 210-212

**Constat.** Qui clôt, et quand : la clôture est « constatée par une note scellée de la session », seule, et elle est sans retour (« rien n'est ajouté »). Plusieurs causes du cas (ii) laissent pourtant une suite que le texte donne à Lazar : seconde tentative « sur le mot de Lazar » (§ 2.3), mise en place refaite (texte l. 363 ; addendum 5, § 4), relance par le chemin de l'addendum 5, crédit d'une reprise, « ligne neuve accordée par Lazar avant la clôture » (condition 2), mot de lancement redonné. La session peut éteindre ces suites en scellant sa note à la première occasion. Aucun résultat n'est connu à ce moment : ce n'est pas une voie liée au signe, mais deux lectures restent (la note suffit, ou le mot de Lazar est requis). « Un mot assorti d'une condition vaut refus » vient de l'ancien ordre, où la condition pouvait porter sur un verdict lu ; il ferme maintenant la confirmation sur une simple précision de Lazar.

**Correction.** (a) § 3, après la phrase du cas (iii), insérer : « Quand la cause du cas (ii) laisse une suite à la décision de Lazar (mot de lancement, seconde tentative du § 2.3, mise en place refaite (l. 363), relance par le chemin de l'addendum 5, crédit d'une reprise, ligne neuve de la condition 2), la note de clôture cite le mot de Lazar qui y renonce, ou constate que l'échéance de la condition 2 est passée. »
(b) § 6, condition 7 : « un mot assorti d'une condition vaut refus » → « un mot assorti d'une condition vaut refus, dit aussitôt à Lazar, qui peut le redonner sans condition avant la clôture ».

### 6. à corriger — § 3, l. 117 et l. 122 ; texte l. 338

**Constat.** Run de confirmation arrêté par Lazar (cas (iii)) alors que des tours sont journalisés : le second lecteur n'est lancé que « si la clôture est du cas (i) », donc pas ici. Mais le texte, qui prime, lit un run interrompu dès K′ ≥ 20 (l. 338), et le § 3 dit la confirmation « rapportée … selon la table des critères gelés ». Deux lectures. Elles ne changent le verdict retenu que si l'arrêt tombe à K′ ≥ 71 (K = 72, arrêt pendant le dernier tour), mais elles changent ce qui est lu et rapporté. Si l'auteur veut au contraire qu'un run arrêté par Lazar ne soit jamais lu, il faut l'écrire, comme écart au texte.

**Correction.** « l'autre, si la clôture est du cas (i), sur » → « l'autre, si un run principal de la confirmation a ses journaux transférés et scellés (cas (i) ; cas (iii) après le début du run principal, lu comme un run interrompu, l. 338), sur ».

### 7. à corriger — § 3, l. 132-134 et l. 147-150

**Constat.** Deux mots laissent une prise après lecture. (1) « ni relecture décidée ensuite n'est retenue » : la lecture par un lecteur neuf qui suit un refus ou une erreur est décidée après le lancement du premier lecteur ; à la lettre elle ne serait pas retenue, alors que la puce « Refus ou erreur » la prévoit. On peut soutenir l'une ou l'autre lecture une fois ce verdict connu. (2) « La confirmation » comprend la seconde tentative et la relance, pas la mise en place refaite que le texte permet (l. 363) : on peut soutenir après coup qu'une confirmation courue après une mise en place refaite n'est pas « la confirmation », donc jamais retenue.

**Correction.** (a) « aucune série, tentative, relance, reprise ni relecture décidée ensuite n'est retenue pour l'étape 1 » → « aucune série, tentative, relance, reprise, ni relecture d'un run dont le verdict a été rendu, décidée ensuite n'est retenue pour l'étape 1 (la lecture qui suit un refus ou une erreur n'est pas une relecture) ».
(b) « seconde tentative du § 2.3 et relance de la l. 371 comprises » → « seconde tentative du § 2.3, mise en place refaite (l. 363) et relance de la l. 371 comprises ».

### 8. remarque — § 3, l. 126-127

**Constat.** La cloison des lecteurs couvre le verdict et le rapport de l'autre, pas son dossier de lecture. Les deux runs ont les mêmes graines : un lecteur qui ouvre les notes de l'autre run connaît une partie de l'autre issue avant de sceller la sienne. Les critères sont mécaniques ; l'effet est faible.

**Correction.** « ne reçoit ni ne lit le verdict de l'autre, son rapport, ni aucun registre » → « ne reçoit ni ne lit le verdict de l'autre, son rapport, son dossier de lecture, ni aucun registre ».

### 9. remarque — § 3, l. 108-110 ; § 2.3 ; § 2.1

**Constat.** Champs techniques : voie fermée, aucune décision n'y reste ouverte. Les journaux de gardes ne portent que nom, état, tour et message, sans valeur (`journaliseur_v3.py` l. 197-203) ; les pertes vont au journal des notes. « Sonde orientée » tombée fixe à elle seule « non interprétable », et un contrôle du juge hors seuil « pas de run » : dans les deux cas la série finit par règle (ni reprise, ni relance : `relance_permise`, `lecture_v8.py` l. 293 ; ni seconde tentative, réservée à la garde de durée), et le verdict retenu est celui à 36 tours, fixé d'avance. La seconde tentative se décide en connaissant t et des gardes passées ; la relance, en connaissant le nom de la garde ou de l'erreur, les durées et la mémoire. Les durées ne trahissent pas P1 de façon exploitable (36 à 133 min pour une cause de machine). Seule la phrase « sans connaître aucun résultat » dépasse le fait : pour la relance, « aucune garde tombée » est connu, ce qui écarte déjà l'issue « non interprétable (sonde orientée) ».

**Correction.** « le sont donc sans connaître aucun résultat » → « le sont donc sans connaître aucune note ni aucun verdict (seuls sont connus les champs que le texte laisse lire : durées, mémoire, nombre de pas, tours complets, nom et état des gardes, états des contrôles du juge) ».

### 10. remarque — titre du § 2, l. 48 ; § 2.5, l. 85-92

**Constat.** § 2.5 : fidèle à la note (`7f03f882…`, vérifiée) et au relevé (`e99a2d92…` : seuil 5, montant 5, crédit 6,50, aucun échec). Côté adversaire, voie fermée par le nouvel ordre : fonds de la carte, recharge, compte vidé et alerte se décident sans aucun résultat lu. Une réserve d'attribution : le verbatim « vast se recharge tout seul » est un constat ; le retrait du seuil est, selon la note elle-même, la « lecture de la session », et le risque a été dit à Lazar après son mot (≈ 00:48Z, puis ≈ 00:49Z). Le titre du § 2 le présente comme sa décision. Le mot de lancement en bloc, donné avec le risque (c), le couvre ; le titre peut le dire.

**Correction.** Titre du § 2 : « crédit par la recharge automatique seule, par son mot du 17 novembre » → « crédit par la recharge automatique seule (lecture par la session de son mot du 17 novembre, acceptée ou refusée avec le mot de lancement) ».

## Angle : chiffres, renvois et pièces — bloquant : non

Aucun bloquant sur l'angle « chiffres, renvois et pièces ». Tous les chiffres qui portent une décision tiennent ; restent 8 points à corriger et 9 remarques, chacun avec son texte de remplacement. Fichier relu : /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md au commit 11954d70 (`2165c7a7…`, identique à l'arbre de travail).

**Ce qui est vérifié et tient**
- **Empreintes** : toutes égales aux fichiers et à leurs compagnons : `fb6c2f34`, `f9c8c66e`, `74df1fbf`, `7f03f882`, `546aa0bc`, `a902256b`, `e99a2d92`, `9a879463`, `972928bb`, `6c445f3e`, `9ff59e4b`, `2cac2458`, `3e992ff3`, `f1c2ca52…` (entière), `e573e4c7`, `70e4f7f2`, `75cf4049…` (entière, égale au commit `873ab00c`), `36573ae2`, `82ef2fa0` (égale au commit `c44c6d65`).
- **Commits** : `c44c6d65`, `0c373143` et `873ab00ca5ea…` existent. `lanceur_v21` ne diffère de `lanceur_v20` que par la docstring, le nom du module veilleur, deux messages, le champ `t_max_pilote_s` et la garde de quatre lignes.
- **Règle du nombre de tours** (`analyse_v3.nombre_de_tours`, B = 85) : (85, 8, 1,6, 1 800) donne H = 41,875 h et K = 72 ; K = 72 jusqu'à D = 8,76, 71 jusqu'à 9,68, 70 à 9,69 ; (85, 5, 1,8, 1 800) donne 67.
- **Devis du § 2 bis** : 72 × 1 411,5 s = 28,2 h (32,5 h avec 1,15) ; 30 à 34 h ; 38 à 43 USD à 1,258 USD/h et 33 à 38 à 1,108 ; 8 à 9 recharges, 17 au pire. Les arrêts « vers 48, 45, 39 tours » tiennent à un ou deux tours près.
- **Échéances** (`echeance_epoch`, fin de jour à Paris = 22:59:59Z ; `verifier_echeance` avec B − 0,5 et 1 h de marge) : 27 novembre 17:44:10Z à 1,108 USD/h ; 28 novembre 02:48:30Z à 1,2576 USD/h. La garde passe à la limite et tombe 2 s après.
- **Durées** (champs `tour` et `duree_s` seulement) : relance de 36,5 à 132,8 min, 48,7 h, tours 0 et 1 à 2 187,1 et 2 365,6 s (moyenne 2 276,4 s) ; Texas de 21,7 à 26,4 min ; pilote t = 1 315,99 s ; 1 800/1 315,99 = 1,368.
- **Lignes du texte** : l. 69-71, 165, 243-245, 249-251, 329-338, 332, 338, 340, 365, 366, 371, 374 portent ce qu'on leur fait dire, ainsi que la l. 143 du poste v12. La l. 363 n'est plus citée (voir le constat sur la mise en place).
- **Autres renvois** : addendum 4 § 2.2, addendum 5 § 4, condition 9′ et surveillance de l'addendum 6, lecture 38 (addendum 2), nœud 5 option (c), graines, 45 fichiers scellés dans `lecture-assemblee-v1`, diagnostic (576 %, carte à 0 %, charge 16,27, 16 min et 1 h 31).
- **Mot de Lazar** : « vast se recharge tout seul » est bien le verbatim de la note `7f03f882…`, dont la recharge relevée (seuil 5, montant 5, moyen de paiement présent, aucun échec) est celle du relevé `e99a2d92…`.
- **Autonomie** : `GO-2026-11-16-04` et `GO-2026-11-17-01` existent sur `origin/main` (référence locale) et courent jusqu'au 17 novembre 23:47:55Z.

**Points à corriger les plus utiles avant scellement**
- **Relevé de 00:51Z** : l'offre « Texas 1,2816 » est la machine 146917, pas la 146915 éprouvée, qui n'y figure pas.
- **§ 2.5** : nommer le champ `credit`, car `balance` vaut 0 au relevé.
- **Seconde tentative du § 2.3** : dire qu'elle prend le t de son propre pilote (écart aux l. 244 et 248), et que ses bornes de D ne valent qu'à c = 1,6 USD/h et t = 1 800 s.
- **Taux carte seule résiduels** : « ≈ 70 h à 1,11 » (§ 2.2) et « ≈ 2 700 s » (§ 5 (a)) ne sont pas au c de la règle.

**Cloisons** : aucune note lue, aucun `notes-v3.jsonl` ni `technique-v3.jsonl` ouvert, `valider` et `lire` non appelés sur des dossiers réels, aucune commande réseau, aucun fichier du dépôt créé ni modifié. Un écart à signaler : une recherche de motif sur tout le dépôt (`grep -l` de « 1,108 ») a parcouru l'arbre entier, zones cloisonnées comprises, et a rendu des noms de fichiers, dont celui de `registres/decisions.md` ; aucun contenu n'en a été affiché ni lu.

### 1. à corriger — § 1, l. 43-44 ; § 2 bis, l. 98-99 ; § 5 (b), l. 184-185

**Constat.** Le relevé de 00:51Z (`e99a2d92…`, empreinte vérifiée) ne dit pas tout à fait ce que le § 1 lui fait dire. Son offre « Texas 1,2816 » est la machine 146917, pas la machine 146915 éprouvée en série 3 (même processeur AMD EPYC 7V12, 32 cœurs effectifs, 2,45 GHz). Ni la 146915 ni l'Oregon ne figurent parmi les deux offres qui passent le filtre à 00:51Z. Lu avec « hors la machine du Texas » (§ 5 (b)) et « Hôte comme celui du Texas » (§ 2 bis), le texte laisse croire que la machine éprouvée est offerte à 1,2816 USD/h. Le relevé de 00:25Z (`a902256b…`) est, lui, bien rendu (146915 à 1,2576, Oregon 154960 à 1,255, même processeur). Non bloquant : le contrôle reste la garde du § 2.3 et la dépense reste bornée par B.

**Correction.** § 1 : « deux offres, Texas 1,2816 USD/h et Caroline du Nord 1,5505 USD/h) » → « deux offres, Texas 1,2816 USD/h (machine 146917, autre que la machine 146915 de la série 3, même processeur, durée de tour non éprouvée) et Caroline du Nord 1,5505 USD/h ; ni la machine 146915 ni celle de l'Oregon n'y figurent) ». § 2 bis : « Les machines autres que celle du Texas qui passent le filtre ont une durée de tour non éprouvée. » → « Les machines autres que la machine 146915 du Texas ont une durée de tour non éprouvée ; au relevé de 00:51Z, aucune des deux offres qui passent le filtre n'est cette machine (la moins chère : machine 146917, 1,2816 USD/h, soit ≈ 38 à 44 USD pour 30 à 34 h). ». § 5 (b) : « hors la machine du Texas, » → « hors la machine 146915 du Texas (absente du relevé de 00:51Z), ».

### 2. à corriger — § 2.5, l. 88-90

**Constat.** Le § 2.5 est vérifiable par les champs du compte : le relevé cité porte `credit`, `balance`, `has_billing`, `autobill_threshold`, `autobill_amount` et `billing_failed`. Mais « crédit au moins égal à `autobill_threshold` » ne nomme pas le champ. Au relevé de 00:51Z, `credit` vaut 6,498 et `balance` vaut 0 (déjà 0 à l'ordre de lancement du 13 novembre). La condition 9′ de l'addendum 6 disait « le plus bas des deux » : lue ainsi, la condition ne serait jamais tenue (0 < 5) et la confirmation serait « non lancée (condition du § 2.5 non tenue) ». Par ailleurs c₀ et o ne sont définis qu'à l'addendum 6, avec le filtre du poste v12 et non celui du § 2.4, et la commande du relevé n'est pas nommée.

**Correction.** « et crédit au moins égal à `autobill_threshold` ; relevé (champs, heure, c₀, o) consigné dans l'ordre de lancement ; » → « et champ `credit` (non `balance`, qui vaut 0 au relevé de 00:51Z) au moins égal à `autobill_threshold` ; relevé (champs du compte rendus par `vastai show user`, heure ; c₀ et o au sens de l'addendum 6, c₀ pris au filtre du § 2.4) consigné dans l'ordre de lancement ; ».

### 3. à corriger — § 2.3, l. 69-73 (texte l. 243-245 et 248)

**Constat.** Les l. 243-245 et 366 portent bien ce que le § 2.3 leur fait dire (une seule reprise entière du pilote). Mais la seconde tentative suppose un pilote neuf et une règle recalculée sur la seconde machine (« Au calcul de sa règle », « Seconde chute »). Le texte dit, l. 244, « t se prend sur la première exécution du pilote qui a fini ses tours 0 et 1 » et, l. 248, que la règle est « appliquée une fois ». Cet écart n'est pas nommé, alors que l'en-tête dit qu'en cas de conflit le préenregistrement prime. À la lettre du texte, t resterait celui de la première machine (> 1 800 s) et la seconde tentative tomberait par construction. L'intention est claire, le code mesure t dans chaque conduite, et la décision est prise sans lecture : non bloquant.

**Correction.** Après « contre-lues (R2). », insérer : « Son pilote et sa règle sont ceux de la seconde machine : t est celui de son pilote (écart au texte, l. 243-245 : « t se prend sur la première exécution du pilote qui a fini ses tours 0 et 1 », et l. 248 : règle « appliquée une fois »). »

### 4. à corriger — § 2.3, l. 72-73

**Constat.** La seconde tentative tient dans B. Avec D ≈ 6 à 9 USD au calcul de sa règle (perte de la première ≈ 3 à 5 USD, plus mise en place et pilote de la seconde ≈ 2,3 à 3,8 USD), K vaut 71 ou 72 même au pire (c = 1,6 ; t = 1 800). `nombre_de_tours(85, D, 1.6, 1800)` donne 72 jusqu'à D = 8,76, 71 jusqu'à 9,68, 70 à 9,69. Deux choses manquent. Ces bornes de D ne valent qu'à c = 1,6 USD/h et t = 1 800 s : à 1,2816 USD/h et 1 800 s, K reste 72 jusqu'à D ≈ 21,9 USD. Et le cas « doublée si le pilote a été repris pour une autre cause », écrit trois lignes plus bas, porte D vers 14 USD : au pire, K = 66, donc un run prévu au régime réduit, lancé par la règle et jamais retenu (§ 3, K′ ≤ 70).

**Correction.** « Au calcul de sa règle, D ≈ 6 à 9 USD : K = 72 tant que D ≤ 8,7 USD, 71 jusqu'à 9,6 USD. » → « Au calcul de sa règle, D ≈ 6 à 9 USD (jusqu'à ≈ 14 USD si un pilote a été repris pour une autre cause) : à c = 1,6 USD/h et t = 1 800 s, bornes des § 2.3 et 2.4, K = 72 tant que D ≤ 8,7 USD, 71 jusqu'à 9,6 USD, moins au-delà (D = 14 USD : K = 66, régime réduit, non retenu au § 3) ; sous ces bornes la marge est plus large. »

### 5. à corriger — § 2.2, l. 62-63

**Constat.** « ≈ 70 h de run à 1,11 USD/h » est au taux carte seule, qui n'est pas le c de la règle ni celui de D (carte et stockage : `dph_total` de l'instance). La section « Contre-lecture » annonce pourtant « devis et risques au taux carte et stockage ». Recalcul, (83 − D)/c avec D ≈ 5 USD : ≈ 62 h à 1,258 USD/h, ≈ 49 h à 1,6 USD/h, ≈ 70 h à 1,11 USD/h. La justification de B = 85 (K = 72) ne change pas.

**Correction.** « La garde B − 2 laisse ≈ 70 h de run à 1,11 USD/h. » → « La garde B − 2 laisse ≈ 62 h de run à 1,258 USD/h, ≈ 49 h à 1,6 USD/h (≈ 70 h au taux carte seule de 1,11 USD/h, qui n'est pas le c de la règle). »

### 6. à corriger — § 5 (a), l. 181-183

**Constat.** « ≈ 2 700 s » est le plafond d'un hôte stable au taux carte seule (K = 72 jusqu'à t = 2 808 s à 1,108 USD/h, avec mise en place 0,75 h et pilote de trois tours). Au c de la règle, la plage où la garde arrête un hôte que la règle aurait laissé finir est plus étroite : jusqu'à ≈ 2 470 s à 1,258 USD/h, ≈ 1 935 s à 1,6 USD/h. Dans les trois cas, 72 tours finissent sous B − 2 (D ≈ 66 USD).

**Correction.** « un hôte stable entre 1 800 et ≈ 2 700 s que la règle aurait laissé finir 72 tours » → « un hôte stable entre 1 800 et ≈ 2 470 s à 1,258 USD/h (≈ 1 935 s à 1,6 USD/h ; ≈ 2 800 s au taux carte seule de 1,108 USD/h) que la règle aurait laissé finir 72 tours ».

### 7. à corriger — § 1, l. 39-40 ; § 5 (a), l. 179

**Constat.** « tours 30 à 35 plus courts » est inexact. Dans `sortie-durees-v3.jsonl` de la relance (`6c445f3e…`, champs `tour` et `duree_s`), les tours 31 et 32 sont les deux plus longs du run (131,5 et 132,8 min). Seuls 30, 33, 34 et 35 sont plus courts, ce que la première phrase du même § 1 dit d'ailleurs correctement.

**Correction.** Aux deux endroits : « tours 30 à 35 plus courts » → « tours 30, 33, 34 et 35 plus courts ».

### 8. à corriger — § 3, l. 109, 115 et 149-150 (texte l. 363, non citée)

**Constat.** La l. 363 n'est plus citée dans cette version. Or le § 3 (ii) range « garde de mise en place » parmi les causes d'une confirmation « pas courue », alors que la liste d'arrêt, gardée sans changement (§ 2.1), dit l. 363 et l. 335 que la mise en place « peut être refaite », et l'addendum 5, § 4, sur un nouveau mot de Lazar. La mise en place refaite manque aussi dans la liste des décisions prises avant la clôture et dans la définition de « la confirmation ». La décision se prend sans lecture et la note de clôture fixe le cas : non bloquant.

**Correction.** l. 115 : « garde de mise en place, » → « garde de mise en place non refaite (l. 363 ; addendum 5, § 4 : elle peut l'être avant la clôture, sur un nouveau mot de Lazar), ». l. 109 : « relance de la l. 371, reprise de la lecture 38) » → « relance de la l. 371, mise en place refaite (l. 363), reprise de la lecture 38) ». l. 150 : « seconde tentative du § 2.3 et relance de la l. 371 comprises » → « seconde tentative du § 2.3, mise en place refaite (l. 363) et relance de la l. 371 comprises ».

### 9. remarque — Contre-lecture, l. 237-239

**Constat.** Le compte « quatre bloquants » de la seconde passe est exact, mais pas leur liste. Dans `verification-adverse-addendum-7-bailey-v2.md` (`70e4f7f2…`), les quatre bloquants sont : deux de l'angle « application des corrections » (exception « défaut technique » contre le § 6 ; liste des défauts qui couvre la garde de dépense du § 1) et deux de l'angle « adversaire » (causes « sans décision » ; relance, reprise, compte vidé, mise en place). « Lecteurs » y est un « à corriger » (point 3), pas un bloquant.

**Correction.** « quatre bloquants (contradictions entre l'exception « défaut technique » et l'ordre ; causes de non-lancement dépendant d'une décision postérieure à la lecture ; relance, reprise et compte vidé ; lecteurs) » → « quatre bloquants (deux contradictions nées de l'exception « défaut technique » : avec l'ordre du § 6 et avec la garde de dépense du § 1 ; causes de non-lancement dépendant d'une décision postérieure à la lecture ; relance, reprise, compte vidé et mise en place) et, parmi les points à corriger, les lecteurs ».

### 10. remarque — § 2.5, l. 89-90

**Constat.** Hors du strict angle « chiffres ». « sinon aucune création » ne dit pas si le relevé peut être refait ni jusqu'à quand. Un crédit passé sous le seuil juste avant qu'une recharge ne paie donnerait, à la lettre, « condition du § 2.5 non tenue » (cause de clôture du § 3 (ii)) sur un état transitoire. La décision reste prise sans lecture.

**Correction.** « sinon aucune création. » → « sinon aucune création tant qu'un nouveau relevé ne les tient pas ; « condition du § 2.5 non tenue » n'est constatée qu'à l'échéance de création (condition 2). »

### 11. remarque — § 2 bis, l. 102-104

**Constat.** Les comptes de recharges tiennent : 5/1,26 = 3,97 h ; 37,7 à 42,8 USD donnent 8 à 9 recharges ; 84,5/5 = 16,9, donc 17. Mais la recharge se déclenche sous 5 USD : seule la part du crédit au-dessus du seuil (≈ 1,5 USD au relevé de 00:51Z) est consommée avant la première recharge, et non « le crédit présent à la création ». Les montants tirés sur la carte ne sont pas écrits.

**Correction.** « toute la dépense au-delà du crédit présent à la création, par recharges de 5 USD (≈ une toutes les 4 h à 1,26 USD/h ; ≈ 8 à 9 recharges pour 30 à 34 h ; 17 au pire) » → « toute la dépense au-delà de la part du crédit située au-dessus du seuil de recharge de 5 USD (≈ 1,5 USD au relevé de 00:51Z), par recharges de 5 USD (≈ une toutes les 4 h à 1,26 USD/h ; ≈ 8 à 9 recharges, soit 40 à 45 USD, pour 30 à 34 h ; 17 au pire, soit 85 USD), hors la dépense des autres chantiers du compte ».

### 12. remarque — § 2 bis, l. 99-101 ; § 5 (a), l. 180-181

**Constat.** « ≈ 180 s par tour, mise à l'échelle 1 800/2 276 » se lit de deux façons. La pente de la relance sur les tours 0 à 29 est de 180,5 s par tour (moindres carrés) avant mise à l'échelle, 142,8 s après. Les arrêts « vers 48, 45, 39 tours » ne tiennent qu'avec la pente mise à l'échelle : ma simulation donne 49 à 50 tours à 1,108 USD/h, 45 à 46 à 1,258, 39 à 1,6. Avec 180 s non mis à l'échelle, ce serait 45, 42 et 36. Dans tous les cas le régime est réduit.

**Correction.** « (≈ 180 s par tour, mise à l'échelle 1 800/2 276) » → « (pente de la relance sur les tours 0 à 29 : ≈ 180 s par tour, soit ≈ 143 s par tour une fois mise à l'échelle 1 800/2 276) ».

### 13. remarque — § 1, l. 11

**Constat.** « vers 11:52Z » : l'instance 60480302 est détruite à 11:47:37Z (`sortie-conduite-v13/poste-v5.json` ; champ `fin` de `bilan-lancement-v13.json`), et le poste note « conduite terminée » à 11:57:25Z. L'heure 11:52Z vient de la passation du 15 novembre, pas d'une pièce du run. D = 73,026, 36 tours complets, aucune garde tombée, transfert complet, instance détruite : confirmés au bilan (`3e992ff3…`).

**Correction.** « a fini le 15 novembre vers 11:52Z » → « a fini le 15 novembre vers 11:47Z (instance détruite à 11:47:37Z, `sortie-conduite-v13/poste-v5.json`) ».

### 14. remarque — § 5 (c), l. 186-187

**Constat.** Date du défaut de recharge : l'addendum 6 écrit « Le 12 novembre, le défaut de recharge… » et, au § 1, « rien entre 23:46Z et l'épuisement du compte vers 04:21Z » (13 novembre). « le 13 novembre » n'est donc ni faux ni identique à la source.

**Correction.** « une recharge a déjà fait défaut le 13 novembre » → « une recharge a déjà fait défaut dans la nuit du 12 au 13 novembre (addendum 6, § 1) ».

### 15. remarque — En-tête, l. 6

**Constat.** Les commits `c44c6d65` (fichier `4e90096c…`) et `0c373143` (fichier `e0a179cf…`) existent et portent bien deux états antérieurs. L'état relu ici (commit `11954d70`, fichier `2165c7a7…`) devient un troisième état intermédiaire dès que la marque de passe finale est remplie.

**Correction.** « commits `c44c6d65` et `0c373143` » → « commits `c44c6d65`, `0c373143` et `11954d70` ».

### 16. remarque — § 4, l. 163-164

**Constat.** Essais rejoués sans écrire dans le dépôt (état de `git status --ignored` identique avant et après). Sans `PYTHONPATH=src` : 226 passés, 1 échec (`test_remarque_veilleur_recolte_jamais_signale`, le veilleur lancé par `sys.executable -m` ne trouve pas le module), 1 sauté. Avec `PYTHONPATH=src`, comme le demande CLAUDE.md et comme le fait le poste, cet essai passe : « 227 passés, 1 sauté » tient. Essais complémentaires : 4 passés.

**Correction.** Facultatif : « 227 passés, 1 sauté (configurations publiques non fournies) » → « 227 passés, 1 sauté (configurations publiques non fournies), sous `PYTHONPATH=src` ».

### 17. remarque — § 1, l. 31 et 34-35 ; § 4, l. 172

**Constat.** Renvois abrégés (R6). Deux journaux de durées sont cités par un chemin relatif sans leur dossier, et le troisième (`9ff59e4b…`) sans chemin ; les trois empreintes sont justes. `offre-choisie-v12.json` (`972928bb…`, juste) n'a pas de compagnon `.sha256`. La conduite passe de v13 à v15 : aucune `lancer-conduite-v14.py` dans le dépôt.

**Correction.** « (`principal-relance/transfert-1/sortie-durees-v3.jsonl`, `6c445f3e…`) » → « (`runs/temoin-bailey-v1-20261111/sortie-conduite-v13/principal-relance/transfert-1/sortie-durees-v3.jsonl`, `6c445f3e…`) » ; « (`9ff59e4b…`) » → « (`…/sortie-conduite-v11/reprise-v10-2/principal/transfert-1/sortie-durees-v3.jsonl`, `9ff59e4b…`) » ; « (`pilote/transfert-1/sortie-durees-v3.jsonl`, `2cac2458…`) » → « (`…/sortie-conduite-v11/reprise-v10-2/pilote/transfert-1/sortie-durees-v3.jsonl`, `2cac2458…`) ». Facultatif, au § 4 : « conduite `lancer-conduite-v15.py` » → « conduite `lancer-conduite-v15.py` (il n'y a pas de v14) ».

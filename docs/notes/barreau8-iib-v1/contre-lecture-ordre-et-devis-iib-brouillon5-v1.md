# Contre-lecture de l'ordre exploratoire (brouillon 5) et du devis (brouillon 5) du saboteur à budget — v1

> Contre-lecture, par un lecteur qui n'a rien écrit de ce barreau, de pièces d'une course **exploratoire, non opposable (R-522)**. Processeur seulement. Rien n'a été lancé sur une carte, rien n'a été dépensé, aucun modèle n'a été chargé, aucune clé n'a été lue. Aucun fichier existant n'a été modifié. Ni commit, ni poussée, rien d'écrit sous `registres/`. Aucun refus d'outil, de crochet ni de classifieur.
>
> Ce rapport va au rédacteur des corrections et à la session mère. Il nomme des réglages de la base textuelle des moniteurs, parce que le § 2 de l'ordre les porte désormais.

## 0. Identité

- **Contre-lecteur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`. Modèle : Claude Fable 5.2 (`claude-fable-5-2`). Je n'ai écrit ni la conception, ni le code, ni aucun brouillon de l'ordre ou du devis, ni la note des points à trancher, ni les contre-lectures précédentes. Le modèle du rédacteur du brouillon 5 n'est écrit dans aucune des pièces : je ne le connais pas.
- **Heures** (`date -u`) : première heure relevée 2026-11-18T21:53:03Z, lecture commencée une dizaine de minutes plus tôt ; rapport écrit vers 22:00Z.
- **Je n'ai ouvert** aucun fichier dont le nom contient « consigne-privee » ou « conception-ii-b », ni leurs compagnons, ni la branche `lot/compte-4-v1`. **Je suis exclu de toute lecture des sondes du barreau 8.**

| pièce | empreinte vérifiée (calculée, et égale au compagnon) | lu |
|---|---|---|
| ordre, brouillon 5 | `73bc2781d79e69d33d0a0949c01f3861a74ff2e0c3ac6d74ac0dcee88068b223` | en entier |
| devis, brouillon 5 | `8ee9ead15fb5feadbffc41ffb3cd8d9abe8a8fc1d82b588f2957de93405e7e32` | en entier |
| note des différences | `ab3e27726a8ad20c32b102e59614ae20ca3d6a542ddd3b1ae2f3229b1d8b4558` | en-tête, tables, points ouverts ; le reste **régénéré par programme et comparé à l'octet** |
| script d'application | `f5c0719efc4e9e2d150f5d3886b4b99749665e68e17c145aec5bc6087ae6870c` | en-tête et logique ; listes de changements **rejouées** |
| script de compte des marqueurs, et sa sortie | `d2a70926aebfa5395a0303b5ba7261f9fba0888ee6cc3c833e90919cfdc189f4`, `2edd0cf77915378f867239bd2d5e6cb91fe149fb98d67aff21ee8d5ebe0b126c` | en entier ; **rejoué** |
| ordre, brouillon 4 | `91a592ff776efd4a9cf2293cfee2a837a25b4bee6d33fcff087662cbf2f715c8` | en entier |
| devis, brouillon 4 | `08107e075e72a1711db812069574c6dc5fc2742ec7f1b690151fd1ff974aa580` | par ses différences avec le brouillon 5 (11 blocs, 13 changements) |
| note des points à trancher, v2 | `be431ed56a20657d924a5b5546dd78bb465afd0e2bf39cfb91a6d0a260d25207` | en entier |
| contrôle court du code, tête `a31b8970` | `02962a4a4951eeb424450d598221c6136ae09158a1ed8f33dfa84f79dc14c3a2` | en entier |
| contre-lecture précédente (brouillons 3) | `d398bf5c4a7902b3821eab5879dfad1176b17adb2e50658166324e01ece22193` | en entier |
| calcul du devis v3 et sa sortie | `3ce44b68e8c1c86002e83d37506077947990c16bb8a6b8baf52b6a1929a129d0`, `8eecd277527918146d3fb180f86b15ab9098305008e3628f32a3ab9f31f38bd8` | sortie en entier ; **rejoué** |
| `registres/go.md` | — | les deux seules lignes `GO-2026-11-18-55` et `GO-2026-11-18-56`, par recherche de leur clé |

## 1. Verdict

**« Scellable après ces couples exacts »** — et, comme prévu, après la tête du code et les marqueurs encore en attente (§ 6).

- **0 bloquant**, sous **deux réserves de vérification** que je ne pouvais pas lever dans mon mandat (R-1, R-2).
- **5 majeurs** (M1 à M5) : chacun a son couple exact au § 3.
- **12 mineurs** (m1 à m12).
- **Devis** : aucun chiffre ne change, le calcul rejoué est identique à l'octet, le plafond et la coupure de la ligne sont tenus, la passe de recalcul est hors de la ligne. Deux mineurs seulement (m1, m11). Il devient inscriptible en complément de la ligne dès que M3 est tranché, car M3 touche l'hypothèse « instance arrêtée détruite sous 48 heures » de son § 6.

Ce qui est bien fait, en bref : les cinq nœuds de la note v2 sont appliqués à la lettre ; les cinq compléments du contrôle court sont tous présents ; la fabrication par programme est exacte et rejouable ; les comptes de marqueurs sont justes ; aucun sujet ni mécanisme n'est ajouté hors de ce que les accords et le contrôle court demandent.

## 2. Constats

Gravités : **bloquant** = rien n'est scellé avant ; **majeur** = à corriger avant le scellement ; mineur = à corriger ou à consigner.

### Réserves de vérification

| identifiant | où | constat | qui la lève |
|---|---|---|---|
| **R-1** la fermeture du point bloquant B1 repose sur une ligne que je n'ai pas lue | ordre, avertissement de tête, § 0 bis, § 4 étape 1, § 11 ; devis § 0, § 8.1, § 9 | L'ordre écrit « mot exprès de Lazar … donné, branche B », « confirmé au registre des décisions, ligne `R-3435` », avec un verbatim. La ligne `GO-2026-11-18-55`, elle, dit autre chose de son propre état : le mot de Lazar y est « Activité interne du saboteur à budget go now, go autres recos », lu par la mère comme l'accord à la branche B (« lecture de la mère, déclarée »), et « la question de confirmation posée est restée sans réponse ». Elle renvoie à `R-3434`, pas à `R-3435`. Tout tient donc au verbatim de `R-3435`. Mon mandat borne les registres à deux lignes de `registres/go.md` : je n'ai pas ouvert le registre des décisions. | La mère : relire la ligne `R-3435` et vérifier que le verbatim cité par l'ordre (§ 0 bis) et le devis (§ 0) y est, mot pour mot. S'il y est : aucun changement. Sinon : couple R-1 du § 3, et B1 reste ouvert. |
| **R-2** les quatre recommandations du portage ne sont pas comparées à leur source | ordre § 2, points 1 à 4, et la phrase « conforme au texte scellé (« au point rendu ») » | Le choix de Lazar (`GO-2026-11-18-56`, point 4) est « les recommandations du relevé du code des deux bases ». Je n'ai pas ouvert ce relevé : c'est une pièce du côté des moniteurs, absente de ma liste, et la contre-lecture précédente ne l'avait pas ouverte non plus. J'ai seulement vérifié son empreinte : `601bbc84ae6bf0a31ffba36e20bf554df5da15d60882c92907f8b5e9ef942034`, égale à celle de la ligne d'accord et à celle de l'ordre. Le marqueur neuf `FORMAT_ACTIONS_PORTAGE_IIB` et l'« adaptateur déclaré » du point 2 sont le seul mécanisme neuf du brouillon 5 : je ne peux pas dire s'il vient du relevé. | Un lecteur du côté des moniteurs, ou la mère : comparer les points 1 à 4 du § 2 aux recommandations du relevé, avant le scellement. |

Note sur R-1. Le seul mot de Lazar relayé dans mon contexte est un fragment : « …ecommandation : option a, confiance 0,7. go ». Je ne sais pas à quelle question il répond et je n'en tire rien. Je signale seulement une collision de lettres possible : la note v2 appelle (A) l'enregistrement pendant la course et (B) le recalcul plus tard ; la confiance de 0,7 est celle que la ligne `GO-2026-11-18-55` prête à la recommandation de recalculer plus tard. Si ce mot répond à la question sur l'activité interne, la mère vérifie que « option a » y désignait bien le recalcul plus tard.

### Majeurs

| identifiant | où | constat |
|---|---|---|
| **M1** quatre corrections du code laissées « souhaitables », contre le nœud 5 (a) et la règle des gardes | ordre § 4 étape 2 ; § 3, titre ; § 11 | Le § 4 étape 1 recopie le choix de Lazar : « 5 (a) avant la course, toutes les corrections et tous les essais manquants sauf les deux améliorations d'essais ». L'étape 2 écrit pourtant : « mineurs CC-02 à CC-05, souhaitables avant la course selon le contrôle court (à trancher par la mère) ». Or ces quatre constats sont les restes des points que la note v2 rangeait avant la course : CC-04 et CC-05 sont deux artefacts sans portée (reste de « plusieurs gardes neuves n'ont pas d'essai qui les fait échouer exprès ») ; CC-03 est un chemin de fuite du texte privé vers les traces poussées ; CC-02, les angles morts de l'essai de non-fuite. Le titre du § 3 promet « cas sain et artefact, au commit du code revu » (règle R5) : avec CC-04 et CC-05 ouverts, ce n'est pas vrai. Le titre du § 3 cite CC-04 et CC-01, pas CC-05. |
| **M2** au rapatriement, la vérification des compagnons peut passer à vide | ordre § 5 étape 5, quatrième point | L'étape dit « chaque compagnon vérifié (`… verifier <fichier>`, puis `verifier-arbre .`) », mais aucune commande n'extrait les fichiers du run : `$W/depot` est une extraction réduite (`scripts/`, `src/`, `.claude/`, `registres/`) au commit de lancement, et `fetch` ne met rien dans l'arbre de travail. J'ai joué l'étape sur un dépôt jouet de mon bloc-notes (§ 5) : après le `fetch`, `verifier-arbre .` rend « arbre intact », code 0, alors qu'aucun fichier du run n'est là. Deux raisons, lues dans l'outil de scellement : il saute sans rien dire un dossier absent, et il ne parcourt pas `donnees/` (dossiers parcourus : `docs`, `prereg`, `runs`, `diag`, `livrables`, `registres/passations`). C'est justement sous `donnees/` que sont les fichiers par phase et les adaptateurs. L'ordre dit que cette comparaison est « le seul contrôle » sur trois chemins : elle ne doit pas pouvoir passer à vide. |
| **M3** la retenue de la destruction n'est pas bornée par les 48 heures du devis | ordre § 5 étape 5 (dernier point), § 5 étape 6, § 7 ; devis § 6 | Le complément écrit « la destruction est retenue jusqu'au mot de la session mère, au plus tard jusqu'à 2026-11-27T22:00:00Z ». L'étape 6 dit « au plus tard 48 h après la fin ». Le devis ne tient « au plus 59,8 USD » que pour 48 heures d'arrêt (« au-delà d'environ 50 h d'arrêt, la ligne serait dépassée »). Une instance arrêtée n'a plus de minuterie : rien dans le code ne borne ce stockage. Exemple calculé : coupure de 55 dollars atteinte après une création le 20, retenue jusqu'au 27 à 22:00 UTC : 153 heures d'arrêt, 68,3 dollars, au-dessus de la ligne de 60. Le texte vient mot pour mot du contrôle court et de la contre-lecture précédente : le rédacteur l'a appliqué fidèlement ; c'est le couple d'origine qui laissait ce trou. Cas rare (il faut la coupure et un écart), mais c'est une dépense hors de la ligne. |
| **M4** le remède « relancer l'instance arrêtée » peut se retourner après le 25 | ordre § 5 étape 5 (dernier point) | Le texte propose, sur le mot de la mère, de « relancer l'instance arrêtée (un second démarrage pousse d'abord les commits en attente) ». Trois choses manquent. (a) La contre-lecture précédente (O-M6) a rejoué que l'amorce refait le calendrier à l'heure de l'instance et se détruit si le dernier jour de création est passé. Une course créée le 25 finit le 26 ou le 27 : toute relance serait datée d'après le 25. Je n'ai pas relu le code (hors de mon mandat) : je ne sais pas si la poussée des commits en attente passe avant ce contrôle. (b) Un fichier que les motifs de la poussée ne couvrent pas (CC-09) n'est dans aucun commit en attente : la relance ne le rend pas. (c) Une relance loue la carte : c'est une dépense, à compter dans la ligne. |
| **M5** deux réglages de la seconde lecture restent « indéterminés, sans choix ici », sans marqueur ni responsable | ordre § 2, dernier paragraphe avant la table ; § 11 | « Restent indéterminés d'après le relevé (§ 4), sans choix ici : le nombre de tirages et de permutations de la lecture (2) ». La phrase suivante dit que les réglages sont écrits dans le code avant le commit du code revu. Il faut donc une valeur, avant ce commit, et personne n'est nommé pour la donner. Le marqueur `REGLAGES_PORTAGE_BASE_TEXTUELLE_IIB` est dit « rempli (décision) » alors qu'il ne l'est pas tout à fait. La vérification du scellement (« recherche des marqueurs vide ») passerait avec ce trou. |

### Mineurs

| identifiant | où | constat |
|---|---|---|
| m1 | devis § 0 | Empreinte abrégée fausse : `be431ed5…7207`. L'empreinte de la note v2 finit par `5207`. Même faute dans la note des différences (en-tête). |
| m2 | ordre § 2 | Empreinte abrégée fausse : `98284ec7…d692`. L'empreinte du relevé des réglages finit par `e692` (la forme entière, dans l'en-tête, est juste). Même faute dans la note des différences. |
| m3 | ordre § 4 quater, « État à `a31b8970` » | « corrigés et éprouvés sur les trois chemins de consignation » dit plus que le contrôle court : la poussée est éprouvée sur la fin de run et sur l'arrêt consigné ; la minuterie passe par la même fonction, sans essai à part ; le contrôle des fichiers ignorés ne joue que sur la fin de run. |
| m4 | ordre § 8 | Manquent aux exclus de la lecture des sondes : le contrôleur du contrôle court (il a lu la consigne privée par programme et se déclare exclu) et le contre-lecteur du brouillon 5. Par ailleurs le § 2 porte désormais des réglages de la base textuelle des moniteurs (fonctions, seuil 0,70, seuil de 10 coûts lisibles) : qui lit l'ordre les connaît. |
| m5 | ordre § 4 ter, dernière phrase | « point ouvert, porté à la mère », sans défaut : si la mère ne dit rien avant le commit du code revu, le texte ne dit pas ce qui vaut. |
| m6 | ordre, statut et « Code lu » | « Le rédacteur n'a écrit ni… ; il n'a vu aucun interne de moniteur » suit la phrase sur le brouillon 4 : on ne sait plus de quel rédacteur il s'agit, alors que celui du brouillon 5 a lu deux relevés du côté des moniteurs. « tête `d88e3d94…` (inchangée depuis le brouillon 3) » se lit comme la tête d'aujourd'hui, qui est `a31b8970`. |
| m7 | ordre § 1, ligne « Code de (ii-b) » | « sinon ce marqueur retombe en attente » : le marqueur n'est plus nommé dans la phrase. |
| m8 | ordre § 4 étape 6 | L'essai à blanc des extractions réduites n'est prévu qu'au commit de lancement, donc après la création de 7b, peut-être le 25. Un écart ce jour-là demande une version nouvelle de l'ordre sous la contrainte de 23:00 UTC. La forme ne dépend pas du commit de lancement : elle peut être jouée dès maintenant sur la tête `a31b8970`. L'extraction des fichiers du run (M2) est à jouer à blanc de la même façon. |
| m9 | ordre § 1, ligne « Calendrier » | Deux parenthèses de suite. |
| m10 | ordre, « Pièces citées » | L'ordre renvoie au brouillon 3 pour plusieurs passages que l'exécutante doit suivre (pièces interdites, essais du jetoniseur, inventaire, forme de la commande de création, levée de l'interdit, compte rendu, § 6, § 7, § 8, § 12). Le brouillon 3 est cité avec son empreinte dans le statut, pas comme pièce à lire avec l'ordre. Inchangé depuis le brouillon 4 ; je n'ai pas ouvert le brouillon 3. |
| m11 | devis, table des remarques, ligne D-M2 | « **sans trancher** » date du brouillon 4 ; Lazar a tranché depuis. |
| m12 | ordre § 5 étape 5, premier et troisième points | L'état « stopped » n'a pas de commande de relevé ; l'arrêt par l'identifiant ne dit pas quelle commande ; la lecture du résumé sur la branche n'a pas de commande. |

## 3. Couples avant → après

Chaque « avant » ci-dessous figure **exactement une fois** dans le brouillon 5 cité (vérifié par programme).

**R-1** (seulement si `R-3435` ne porte pas le verbatim cité). Ordre, avertissement de tête.
- Avant : « > **Mot exprès de Lazar sur l'activité interne : donné, branche B** (`registres/go.md`, ligne `GO-2026-11-18-55` ; confirmé au registre des décisions, ligne `R-3435`) »
- Après : « > **Mot direct de Lazar sur l'activité interne, lu par la session mère comme la branche B** (`registres/go.md`, ligne `GO-2026-11-18-55` : « go now » lu comme l'accord à la recommandation B ; lecture déclarée par la mère ; question de confirmation restée sans réponse). **Cet ordre n'est ni scellé ni remis avant la confirmation de Lazar.** »
- Et, dans ce cas, retirer « confirmée `R-3435` » partout (ordre § 0 bis, § 4 étape 1, § 11 ; devis § 0, § 8.1, § 9).

**M1.** Ordre.
- § 4 étape 2. Avant : « mineurs CC-02 à CC-05, souhaitables avant la course selon le contrôle court (à trancher par la mère) ; » → Après : « mineurs CC-02 à CC-05, faits avant le commit du code revu : le nœud 5 (a) demande avant la course toutes les corrections et tous les essais manquants, sauf les deux améliorations d'essais ; CC-04 et CC-05 sont des artefacts sans portée (R5) ; CC-03 est un chemin de fuite du texte privé vers les traces poussées ; »
- § 3, titre. Avant : « celui de la consigne invisible à l'évaluation ne voit pas les contextes, CC-04 ; » → Après : « celui de la consigne invisible à l'évaluation ne voit pas les contextes, CC-04 ; celui de la garde numérotée (11) par la vérification courte, dans les essais du lanceur, est tautologique, CC-05 ; »
- § 11. Avant : « | en attente | commit du code revu (§ 4 étape 2), après la correction de CC-01 | » → Après : « | en attente | commit du code revu (§ 4 étape 2), après les corrections de CC-01 à CC-05 | »
- Si la mère juge qu'un de ces quatre constats est l'une des « deux améliorations d'essais », elle l'écrit en toutes lettres à l'étape 2 ; CC-04 et CC-05 ne peuvent pas l'être (R5).

**M2.** Ordre, § 5 étape 5.
- Avant : « - chaque compagnon vérifié (`PYTHONPATH=src python -m controle_ia.scellement verifier <fichier>`, puis `verifier-arbre .`) ; »
- Après : « - fichiers du run extraits dans l'arbre de travail : `git -C "$W/depot" sparse-checkout add /diag/ /runs/ /donnees/ /traces/` ; `git -C "$W/depot" checkout --detach refs/remotes/origin/essai/iib-explo-v1` (forme jouée sur un dépôt jouet par le contre-lecteur du brouillon 5 ; rejouée à blanc à l'étape 6 du § 4) ;
   - chaque fichier listé (au résumé ou à l'arrêt, puis au § 7) vérifié un par un depuis `$W/depot` : `PYTHONPATH=src python -m controle_ia.scellement verifier <fichier>` ; **le nombre de fichiers vérifiés est égal au nombre de fichiers listés** ; `verifier-arbre .` ne tient pas lieu de ce contrôle : il ne parcourt pas `donnees/` et rend « arbre intact » quand les dossiers du run ne sont pas extraits ; »

**M3.** Ordre.
- § 5 étape 5. Avant : « la destruction (étape 6) est retenue jusqu'au mot de la session mère, au plus tard jusqu'à 2026-11-27T22:00:00Z.** » → Après : « la destruction (étape 6) est retenue jusqu'au mot de la session mère, au plus tard 48 heures après la fin du run et jamais après 2026-11-27T22:00:00Z ; au-delà de 48 heures d'arrêt, la mère ne prolonge que si la dépense relevée, plus le stockage à l'arrêt jusqu'à la destruction, reste sous 60 USD, calcul consigné au registre des dépenses (devis § 6 : le plafond de 59,8 USD ne tient que pour 48 heures d'arrêt) ; sans mot de la mère à cette borne, l'exécutante détruit et porte l'écart au compte rendu.** »
- § 7. Avant : « la destruction est retenue jusqu'au mot de la session mère, au plus tard 2026-11-27T22:00:00Z** (§ 5 étape 5). » → Après : « la destruction est retenue jusqu'au mot de la session mère, dans les bornes du § 5 étape 5** (48 heures après la fin du run, jamais après 2026-11-27T22:00:00Z). »
- § 5 étape 6. Avant : « la mère pose un rappel daté du 2026-11-27T20:00Z.** » → Après : « la mère pose deux rappels datés : 40 heures après la fin du run, et le 2026-11-27T20:00Z.** »
- La dernière clause du premier couple (« sans mot de la mère à cette borne, l'exécutante détruit ») est mon choix entre perdre un fichier et dépasser la ligne ; si la mère préfère l'inverse, il lui faut une ligne de dépense, donc un mot de Lazar. Même correction dans le résumé « Ce que le brouillon 5 change ».

**M4.** Ordre, § 5 étape 5.
- Avant : « Sur ce mot seulement : relancer l'instance arrêtée (un second démarrage pousse d'abord les commits en attente) ou lire son disque, puis rapatrier de nouveau. »
- Après : « Sur ce mot seulement : relancer l'instance arrêtée ou lire son disque, puis rapatrier de nouveau. Une relance est une dépense de carte, comptée dans la ligne. Un second démarrage pousse d'abord les commits en attente ; mais l'amorce rejoue le calendrier à l'heure de l'instance (O-M6) : ce qu'elle fait à un second démarrage daté d'après le 2026-11-25 est relu dans le code à la vérification courte de l'ordre, et la relance est retirée de cette étape si l'amorce se détruit avant d'avoir poussé. Un fichier que les motifs de la poussée ne couvrent pas (CC-09) n'est dans aucun commit en attente : seule la lecture du disque le rend. »

**M5.** Ordre.
- § 2. Avant : « Restent indéterminés d'après le relevé (§ 4), sans choix ici : le nombre de tirages et de permutations de la lecture (2) ; les versions de `numpy` et `scipy` (consignées au manifeste). Ces réglages sont écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage, avant le commit du code revu. » → Après : « Restent à fixer avant le commit du code revu, d'après le relevé (§ 4) : le nombre de tirages et de permutations de la lecture (2), `<<TIRAGES_PERMUTATIONS_LECTURE2_IIB>>` (les deux nombres, et la référence de la ligne du registre des décisions où la mère les consigne). Les versions de `numpy` et `scipy` sont consignées au manifeste. Les quatre réglages ci-dessus et ces deux nombres sont écrits dans `FIXES_PAR_LE_CODE` avec les essais du portage, avant le commit du code revu. »
- § 11, après la ligne « | `FORMAT_ACTIONS_PORTAGE_IIB` (propre, neuf) | en attente | vérification du format des actions du barreau 8 (§ 2, point 2), avant le commit du code revu | », ajouter : « | `TIRAGES_PERMUTATIONS_LECTURE2_IIB` (propre, neuf) | en attente | nombre de tirages et de permutations de la lecture (2) (§ 2), fixés par la mère avant le commit du code revu | ». Comptes à refaire par le script : six marqueurs propres, trois remplis, trois en attente ; 17 marqueurs distincts dans le texte.

**Mineurs.**
- m1. Devis § 0. Avant : « `be431ed5…7207` » → Après : « `be431ed5…5207` ».
- m2. Ordre § 2. Avant : « `98284ec7…d692` » → Après : « `98284ec7…e692` ».
- m3. Ordre § 4 quater. Avant : « poussée par phase et contrôle de fin par `--ignored` corrigés et éprouvés sur les trois chemins de consignation ; le contrôle par `--ignored` ne joue qu'en fin de run (CC-09) : le rapatriement le couvre (§ 5 étape 5) ; » → Après : « poussée par phase corrigée, éprouvée sur la fin de run et sur l'arrêt consigné (la minuterie passe par la même fonction `ajouter_legeres`, sans essai à part) ; contrôle de fin par `--ignored` corrigé et éprouvé sur la fin de run, seul chemin où il joue (CC-09) : le rapatriement couvre les autres (§ 5 étape 5) ; »
- m4. Ordre § 8. Avant : « le rédacteur du brouillon 5 ; le contre-lecteur du code v2 ; le vérificateur du code v3 ; **le contre-lecteur de cet ordre et du devis**. » → Après : « le rédacteur du brouillon 5 ; le contre-lecteur du code v2 ; le vérificateur du code v3 ; le contrôleur du contrôle court du code (tête `a31b8970`), qui a lu la consigne privée par programme ; **les contre-lecteurs de cet ordre et du devis (brouillons 3, puis brouillons 5)**. Le § 2 porte des réglages de la base textuelle des moniteurs : la mère inscrit au registre « qui a lu quoi » quiconque lit cet ordre. »
- m5. Ordre § 4 ter. Avant : « il ne dit pas si ces essais deviennent des arrêts joués par l'amorce : point ouvert, porté à la mère. » → Après : « il ne dit pas si ces essais deviennent des arrêts joués par l'amorce : point porté à la mère ; sans mot d'elle avant le commit du code revu, ils ne sont pas joués par l'amorce (état présent du code, aucun code neuf). »
- m6. Ordre, statut. Avant : « Le rédacteur n'a écrit ni la conception, ni le code, ni leurs contre-lectures ; il n'a vu aucun interne de moniteur ; » → Après : « Le rédacteur des brouillons 3 et 4 n'a écrit ni la conception, ni le code, ni leurs contre-lectures ; il n'a vu aucun interne de moniteur ; ». Ordre, « Code lu ». Avant : « - **Code lu** : `origin/prep/iib-code-v3`, tête `d88e3d947ec4f05958834e2746a800c854271a8f` (inchangée depuis le brouillon 3). » → Après : « - **Code lu** (brouillons 3 et 4) : `origin/prep/iib-code-v3`, à sa tête d'alors, `d88e3d947ec4f05958834e2746a800c854271a8f`. »
- m7. Ordre § 1. Avant : « sinon ce marqueur retombe en attente) » → Après : « sinon `COMMIT_CORRECTIONS_RELAIS_POUSSEE_IIB` (§ 11) retombe en attente) ».
- m8. Ordre § 4 étape 6. Avant : « les extractions réduites de l'étape 1 sont **jouées à blanc d'abord**, sans dépense, par la mère, avant le scellement de l'ordre ; » → Après : « les extractions réduites de l'étape 1 et l'extraction des fichiers du run de l'étape 5 sont **jouées à blanc d'abord**, sans dépense, par la mère : une première fois dès la tête `a31b8970` (leur forme ne dépend pas du commit de lancement), puis à ce commit, avant le scellement de l'ordre ; »
- m9. Ordre § 1. Avant : « **aucune création après 2026-11-25T23:00Z** (dernière commande `creation` à 23:00 UTC le 2026-11-25) (l'amorce rejoue » → Après : « **aucune création après 2026-11-25T23:00Z** : dernière commande `creation` à 23:00 UTC le 2026-11-25 (l'amorce rejoue ».
- m10. Ordre, en-tête. Avant : « - **Pièces citées** (non modifiées) : conception » → Après : « - **Pièces citées** (non modifiées) : ordre, brouillon 3 (`eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`), que l'exécutante lit avec cet ordre pour tout ce qui y est dit « inchangé depuis le brouillon 3 » ; conception ».
- m11. Devis, table des remarques. Avant : « | D-M2 deux branches de l'activité interne non chiffrées | appliquée : les deux branches chiffrées dans le script v3, hypothèses écrites, **sans trancher** | § 8 | » → Après : « | D-M2 deux branches de l'activité interne non chiffrées | appliquée : les deux branches chiffrées dans le script v3, hypothèses écrites ; tranché depuis par Lazar, branche B (§ 0) | § 8.1 | ».
- m12. Ordre § 5 étape 5. Avant : « - l'instance est à l'état « stopped » (fin normale ou anormale) ; sinon l'exécutante l'arrête d'abord par son identifiant (R10) ; » → Après : « - l'instance est à l'état « stopped » (fin normale ou anormale), relevé par l'inventaire en champs filtrés sur le seul identifiant créé ; sinon l'exécutante l'arrête d'abord par cet identifiant (R10), avec la commande d'arrêt que la surveillance imprime (étape 4) ; ». Et, au troisième point. Avant : « la liste `resultat.empreintes` de `diag/<run>/resume.json` (ou `sorties_ecrites` de `diag/<run>/arret.json` si le run s'est arrêté) contre » → Après : « la liste `resultat.empreintes` de `diag/<run>/resume.json` (ou `sorties_ecrites` de `diag/<run>/arret.json` si le run s'est arrêté), lue par `git -C "$W/depot" show refs/remotes/origin/essai/iib-explo-v1:diag/<run>/resume.json`, contre ».

Les deux fautes d'empreinte abrégée (m1, m2) sont aussi dans la note des différences, scellée : la prochaine note, sous un nom neuf, ne les reprend pas.

## 4. Les six points du mandat

**(1) Choix de Lazar appliqués fidèlement ; rien d'autre ne change.**

| choix | source | dans le brouillon 5 | fidèle ? |
|---|---|---|---|
| activité interne, branche B | `GO-2026-11-18-55` | ordre : avertissement, § 0, § 0 bis, § 3, § 7, § 9-10, § 11, § 13 ; devis : § 0, § 8.1, § 8.3, § 9 | oui pour la ligne d'accord (rien n'est enregistré ; textes exacts des actions et deux adaptateurs gardés ; passe plus tard, devis et ligne à part ; égale aux arrondis près ; 0 dollar de plus dans la ligne ; si Lazar voulait A, la ligne est remplacée). La « confirmation `R-3435` » : R-1 |
| nœud 2 (a) attendre 7b | `GO-2026-11-18-56`, point 3 | ordre § 1 « Préalable », § 4 étape 1 ; devis § 7 | oui, mot pour mot |
| nœud 3 (a) épreuves au début, même carte | idem | ordre § 4 étape 1, § 4 bis ; devis § 8.2 | oui, mot pour mot |
| nœud 4 (B) 60 dollars, coupure à 55, A100 seule | idem | ordre § 4 étape 1 ; devis § 6 | oui |
| nœud 5 (a) tout avant la course sauf deux améliorations | idem | ordre § 4 étapes 1 et 2 | l'étape 1 oui ; l'étape 2 s'en écarte : **M1** |
| nœud 6 (b) branche v2 gardée gelée | idem | ordre § 1 « Pièces interdites », § 4 étape 1 | oui (gelée, exclue de la copie publique, inscrite au registre « qui a lu quoi », interdite au lecteur des sondes ; inscription à faire par la mère) |
| portage : recommandations du relevé | `GO-2026-11-18-56`, point 4 | ordre § 2 | non vérifiable par moi : **R-2** ; deux réglages laissés ouverts : **M5** |

L'ordre écrit « mot direct de Lazar » pour les nœuds 2 à 6 et réserve « mot exprès » au nœud 1 : c'est exact. La note v2 demandait aussi un mot exprès pour le nœud 3 ; il est couvert par « go autres recos », que la ligne `GO-2026-11-18-56` détaille nœud par nœud. Je ne demande aucun changement.

**Rien d'autre ne change** : vérifié de deux façons. J'ai comparé moi-même les brouillons 4 et 5 (35 blocs de différences pour l'ordre, 11 pour le devis) et lu chaque bloc. J'ai rejoué les listes de changements du script sans rien écrire : 13 et 41 changements, chaque « avant » trouvé une fois, application inverse égale au brouillon 4, **empreintes obtenues égales à celles des deux brouillons 5 et de la note des différences**. Chaque bloc changé se rattache à un choix de Lazar, à un complément du contrôle court ou à la mise à jour de l'en-tête et des marqueurs. Le brouillon 4 n'avait pas été contre-lu : je l'ai lu en entier, sans contrôle par programme, et n'y ai rien trouvé qui contredise les couples de la contre-lecture précédente.

**(2) Compléments du contrôle court : présents ; exécutables ?**

| complément (contrôle court, § 4) | où | présent | exécutable |
|---|---|---|---|
| liste des fichiers par phase avec leurs sceaux | ordre § 7 | oui : trois familles de noms, phases `etalonnage`, `tour1` à `tour<r>`, `evaluation`, plus combinés et adaptateurs. Cohérent avec les comptes du contrôle court (34 fichiers sur le jeu jouet à deux tours ; 17 au résumé) | oui |
| fichier absent ou sans compagnon : écart, destruction retenue | ordre § 5 étape 5, § 7 | oui | borne à corriger : **M3** ; remède à préciser : **M4** |
| aucune création après 2026-11-25T23:00Z | ordre § 1, § 5 étape 2, § 6 ; devis § 7 | oui | oui (règle de l'exécutante : le code ne la porte pas, l'ordre le dit) |
| clonage réduit joué à blanc d'abord | ordre § 4 étape 6, § 5 étape 1 | oui, avec la règle « tout écart → forme corrigée et ordre en version nouvelle » | forme jouée par moi sur un dépôt jouet : elle marche (§ 5) ; à jouer sur le vrai distant, plus tôt : m8 |
| au rapatriement : instance arrêtée, liste du résumé contre l'arbre de la branche, avant toute destruction | ordre § 5 étape 5 | oui, les cinq gestes du contrôle court y sont | la vérification des compagnons peut passer à vide : **M2** ; commandes manquantes : m12 |

**(3) Devis.** Calcul v3 rejoué (`.venv/bin/python -I -B`) : sortie identique à l'octet à la sortie scellée. Aucun chiffre ne change entre les brouillons 4 et 5 (les 13 blocs changés ne portent que du texte). Vérifié à la main : 55 + 0,99 + 3,84 = 59,83 ; coupure à 38,4 et 35,8 heures ; les heures de la variante A du § 6. **Plafond 60 et coupure 55 tenus**, sous la réserve M3 (48 heures d'arrêt). **Passe de recalcul à part** : ordre § 13 (« cet ordre ne la lance pas, ne la chiffre pas dans sa ligne et ne l'autorise pas »), devis § 8.3 et ligne d'engagement (« passe de recalcul hors de cette ligne ») ; chiffres égaux à la sortie du calcul et à la ligne `GO-2026-11-18-55` (4,2 à 4,7 dollars attendus ; 8,9 à 10,4 au pire). Les deux instants : 1 795 816 800 = 2026-11-27T22:00:00Z ; 1 795 824 000 = 2026-11-28T00:00:00Z.

**(4) Gardes éprouvées (R5) et arrêts par identifiant (R10).** Le code n'est pas dans mon mandat : je juge le texte contre le contrôle court. R5 : le titre du § 3 date bien la règle du commit du code revu et dit ce qui manque à `a31b8970`, sauf CC-05 (**M1**). Les règles neuves du brouillon 5 (heure limite de création, retenue de la destruction) sont des règles de l'exécutante, pas des gardes du code : l'ordre le dit. La vérification d'arbre qui passe à vide (**M2**) est un repli silencieux au sens de R5. R10 : tous les arrêts et la destruction passent par l'identifiant de l'instance (§ 5 étapes 4 à 6, § 6) ; le brouillon 5 ajoute un arrêt par identifiant à l'étape 5 (commande à nommer, m12). Aucun arrêt par motif dans le texte.

**(5) Marqueurs.** Compte rejoué : sortie identique à l'octet à la sortie scellée. Ordre : 39 occurrences, **16 marqueurs distincts** = 14 en attente sur les 30 de la configuration, plus `COMMIT_LANCEMENT_IIB` et `FORMAT_ACTIONS_PORTAGE_IIB`. J'ai recompté la table du § 11 : 14 remplis, 14 en attente, 2 hors du texte ; aucun marqueur rempli ne reste entre chevrons. Les trois marqueurs propres remplis sont justes : la branche B (sous R-1), le commit `a31b8970fedb745c993fe23df18bba4a2d9e3cf4` (égal à la tête du contrôle court, sous la réserve écrite), les réglages du portage (sous R-2 et M5). Devis : 8 marqueurs, tous dans la ligne d'engagement, qui est un gabarit que la mère remplit au registre : ils y restent au scellement du devis, à dire dans la vérification du scellement.

**(6) Aucun sujet ni mécanisme ajouté.** Rien dans la course : aucun réglage du saboteur, de la règle, des épreuves, des tours ni de l'évaluation ne change ; la branche B ne change aucun code. Le § 13 décrit la passe de recalcul avec ce que portaient déjà le brouillon 4 (suite B) et la contre-lecture précédente (§ 5.2) ; il n'ajoute ni l'empreinte du contexte par épisode (option écartée, aucun code ne change) ni rien d'autre. Seul élément neuf : le marqueur `FORMAT_ACTIONS_PORTAGE_IIB` et l'adaptateur déclaré du § 2, point 2, à rattacher au relevé (R-2).

## 5. Ce que j'ai exécuté

Tout sur processeur ; rien d'écrit hors de mon bloc-notes, sauf ce rapport et son compagnon.

- Empreintes des neuf pièces et de leurs sources ; compagnons vérifiés par l'outil de scellement : tous conformes.
- Calcul du devis v3, compte des marqueurs, listes de changements du script d'application : rejoués, sorties identiques à l'octet aux pièces scellées.
- Empreintes abrégées des trois textes comparées par programme aux empreintes entières connues : deux écarts (m1, m2). Celle de la conception (`47b86258…209c`) et celle de la consigne privée n'ont pas été recalculées : fichiers interdits.
- Présence unique de chaque « avant » de mes couples : vérifiée par programme.
- **Dépôt jouet local** (git 2.43, transport par fichier, filtre des contenus permis ; supprimé ensuite) : un dépôt à trois commits (code, lancement, run) avec `donnees/` ignoré. Résultats :
  - extractions réduites de l'étape 1, mot pour mot : codes 0 ; seuls `registres/go.md` et `registres/decisions.md` extraits pour `main` ; seuls les quatre dossiers extraits pour le code ; `rev-parse HEAD^`, `diff --name-only`, `git show … | sha256sum`, `ls-remote --exit-code` (code 2 sur une branche absente) conformes à ce que l'ordre attend ;
  - rapatriement : après le `fetch`, `verifier-arbre .` rend « arbre intact », code 0, sans aucun fichier du run (M2) ; après `sparse-checkout add` et `checkout --detach` de la branche du run, les fichiers sont là, et `verifier <fichier>` refuse un fichier de `donnees/` sans compagnon, alors que `verifier-arbre .` ne le voit pas.
  - Limite : ce n'est pas le vrai distant (filtre et identification de GitHub, place réelle) : l'essai à blanc de la mère reste dû.

## 6. Ce qui reste avant le scellement, dans l'ordre

1. **Lever R-1** (verbatim de `R-3435`) et **R-2** (§ 2 contre le relevé).
2. **Brouillon 6** de l'ordre et du devis, sous des noms neufs, avec les couples du § 3 ; compte des marqueurs rejoué.
3. **Tête du code** : CC-01, et CC-02 à CC-05 (M1) ; forme de la ligne de création de 7b fixée, motif et artefact alignés ; réglages du portage, format des actions et nombres de tirages et de permutations écrits au code avec leurs essais ; contrôle court de cette tête par un lecteur qui n'est pas le développeur, avec la question de M4 (second démarrage après le 25) ; marqueurs `COMMIT_CODE_IIB`, `EMPREINTES_CODE_IIB`, `DERNIERE_LIGNE_TESTS_IIB_PROCESSEUR`, `FORMAT_ACTIONS_PORTAGE_IIB`.
4. **Essai à blanc** des extractions réduites sur le vrai distant, dès maintenant (m8).
5. **Conception scellée** ; **devis scellé puis inscrit** en complément de la ligne `GO-2026-11-10-08`.
6. **Faits de la remise** : 7b créée et sa ligne ; exécutante ; lecteur ; version de l'outil de location ; mot de Lazar pour la création ; longueurs de la consigne ; entropie.
7. **Configuration**, **commit de lancement**, contrôles à blanc à ce commit.
8. Marqueurs remplis (recherche vide dans l'ordre), **vérification courte de l'ordre** par un autre lecteur, **scellement**, ligne d'engagement, remise.

Questions déjà portées à la mère par le rédacteur et toujours ouvertes : la copie publique et `donnees/*-iib-*` ; l'inscription de la branche `prep/iib-code-v2` au registre « qui a lu quoi » ; les deux lignes du `.gitignore` (CC-07).

## 7. Lectures hors de la liste du mandat, limites, refus

- **Lectures hors de la liste**, toutes déclarées :
  1. `src/controle_ia/scellement.py`, lignes 21 à 30 et 88 à 114 (l'outil de scellement que le mandat me fait employer), pour M2.
  2. Calcul du devis v3 et sa sortie, script d'application, script de compte et sa sortie : pièces citées par les brouillons 5, lues pour les rejouer.
  3. Compagnons `.sha256` du dossier des brouillons (hors ceux dont le nom contient « consigne-privee » ou « conception-ii-b ») et du dossier `docs/notes/barreau8-iib-v1/` : première colonne lue par programme, pour comparer les empreintes abrégées.
  4. Empreintes calculées, fichiers non ouverts : les deux relevés du côté des moniteurs, les brouillons 3 de l'ordre et du devis.
  5. Noms seuls : fichiers du dossier des brouillons et du dossier des notes du barreau 8.
- **Non ouverts** : le registre des décisions (ligne `R-3435` comprise) ; `registres/go.md` hors des deux lignes ; les relevés ; la conception ; la consigne privée ; le code de la branche ; le brouillon 3 ; tout `diag/`, `runs/`, `donnees/`, `docs/verdicts/`.
- **Limites** : R-1 et R-2 ; le code n'est pas relu (M4 est une question posée au code, pas un constat sur lui) ; les renvois au brouillon 3 ne sont pas vérifiés ; l'essai sur dépôt jouet ne vaut pas l'essai sur le vrai distant ; la routine de reprise n'a pas été jouée (rôle de la session mère).
- **Refus** : aucun.

# Question à Argon — décisions ouvertes, dossier b : porte G0 (grille de lecture) — v1

Écrite par session-depot, 31 octobre 2026, sous GO-2026-10-31-08 (mot direct de Lazar : « demande a argon aussi pour toutes les questions ouvertes […] restant a trancher par moi ou conv »). Tu donnes un avis ; tu ne tranches rien : Lazar (le directeur) décide.

**Contexte.** Le programme « contrôle boîte blanche des menaces diffuses » étudie des moniteurs de sécurité pour des agents d'IA (sondes sur les activations et moniteur sur le texte) contre des sabotages étalés sur beaucoup d'actions peu suspectes. Les décisions ci-dessous sont en attente du directeur ou de la lignée de travail conv-audit. Les faits qui suivent sont des extraits des pièces du dépôt, avec chemin, lignes et empreinte ; les recommandations et confiances de leurs auteurs ont été **retirées** pour ne pas t'ancrer.

**Consigne.** Pour **chaque** décision de la liste ci-dessous, en français :
1. l'option que tu choisirais (une seule ; ou une option nouvelle si aucune ne tient, dite comme telle) ;
2. ta raison, en t'appuyant sur les faits servis (cite la pièce et la ligne) ;
3. le pire cas de ce choix (ce qui se passe s'il est faux) ;
4. ce qui te ferait changer d'avis (une mesure, un fait, un seuil).
Puis, en fin de réponse : les décisions qui te paraissent liées (à trancher ensemble), et les trois que tu trancherais en premier.

Règles : n'invente aucune pièce ni aucun chiffre ; une référence que tu n'as pas lue ici est marquée SUPPOSÉ ; reste au niveau de la méthode (aucune recette pour tromper un moniteur, aucun détail d'attaque) ; si une décision te semble mal posée, dis-le. Environ 5000 mots au plus pour la réponse.

## Décisions à examiner

- **D-G0-1 à D-G0-15** de la grille de lecture de la porte G0, brouillon v7 (pièce 1, annexe B), et les divergences **DIV-1 à DIV-3** (DIV-4 : aucune divergence).
- Pour chacune, l'option 1 ou l'option 2 du tableau (ou une autre), en tenant compte des constats de la contre-lecture CL6 (pièce 2 : un bloquant et sept majeurs, à corriger dans une v8 en cours d'écriture).
- Dis aussi si un constat de CL6 change le sens d'une décision D-G0.

Note sur la forme : dans le tableau de l'annexe B, « option 1 » est l'option que la grille prend par défaut si la décision D-G0-1 est acceptée ; ce n'est pas une recommandation à suivre. Juge les deux options à égalité.

## Faits

### Pièce 1 — `prereg/brouillon-G0-grille-lecture-v7.md`, l. 192–394, l. 397–549, l. 969–1074, l. 1191–1252

Empreinte du fichier source : `911d79e6d2095aba8582253dbbfb984193c5f5cdac28047d3021025240f3e2cd` ; 10528 mots servis ; 9 retraits (recommandations, confiances, défauts des auteurs).

## 0. Conventions de ce texte

- **[GELÉ]** : règle de lecture, destinée à être scellée ; elle ne dépend d'aucun état constaté.
- **[À DÉCIDER, D-G0-n]** : opérationnalisation nouvelle, qui fixerait la lecture d'un critère ou de la porte : nœud pour
  Lazar (CLAUDE.md, « Nœuds de décision »). Chaque point porte sa recommandation **et un défaut** (annexe B) ; le défaut ne
  prend effet que si D-G0-1 a reçu un mot explicite de Lazar.
- **[EXISTANT]** : opérationnalisation déjà fixée par un préenregistrement scellé ou une décision de Lazar, citée par chemin
  et empreinte ou par numéro de décision et ligne ; la grille la reprend sans la changer. Rien n'est étiqueté [EXISTANT] sans
  que le texte cité ait été vérifié sur disque.
- **Aucun constat d'état** dans la partie gelée. L'état des preuves au 29 octobre vit dans une note séparée, non scellée
  avec la grille (`docs/notes/porte-g0-grille-v1/constat-etat-preuves-G0-2026-10-29-v1.md`). Les seules exceptions de ce
  brouillon sont les **annexes F et G** (essais des motifs sur le dépôt du 29 octobre), **non gelées et retirées de la
  version scellée** ; ce n'est pas une lecture de G0 (aucun dossier n'existe, des versions qui ne font pas foi y sont essayées).
- **Aucune lecture avant scellement** : aucune lecture de G0 (verdict, même partiel, même « à titre indicatif ») n'est
  recevable avant le scellement de la version finale de cette grille, ni par la session, ni par un sous-agent, ni par une
  lignée. Les états d'avancement de `registres/etat.md` ne sont pas des lectures.
- **Commandes** [GELÉ] : toutes s'exécutent depuis la racine du clone complet au commit `C_lecture`, après
  `export LC_ALL=C.UTF-8 PYTHONPATH=src`. Motif : en locale POSIX, `grep` traite « è » comme deux octets ; la classe
  `[èe]` ne trouve alors rien, et `-i` ne replie pas « É » sur « é » (constaté le 2026-10-29, annexe F). Les motifs
  s'écrivent en `grep -E` avec des alternances `(è|e)`, jamais des classes accentuées (seule exception : la classe
  `[*«" ]` de `PRONONCE_1`, qui ne contient pas de lettre et est essayée sous `C.UTF-8`, annexe F ; un motif qui contient
  un guillemet droit s'écrit entre apostrophes simples). Si `locale -a` ne contient pas
  `C.UTF-8` (ou `C.utf8`), la lecture s'arrête (liste d'arrêt). Une commande qui ouvre une liste de fichiers la construit
  par `find … ! -name 'P3-consignes-v1.md'` **avant** toute ouverture (interdits, section 1). Dans les cellules de table,
  `\|` est l'échappement Markdown d'une barre verticale : la commande à exécuter porte `|` (tube du shell, ou alternance
  d'un motif `grep -E`) ; copié tel quel, `\|` serait une barre littérale en `grep -E` (constaté, annexe F). Hors des
  tables (blocs de code ; définitions `NEUTRE`, `PRONONCE_1`, `LARGE_1`, `CRIT_2`, `FAM_I`, `FAM_II`, `VERDICT_CL`, `NEG_CL`, `IMPREVU_CL`,
  `ARRET_BETA`, `BRAS_P`, `DOSE`, `NETTOIE`, `NEG_DEBUT`, `AGREG`), rien n'est échappé ; dans une cellule, un motif nommé s'écrit
  par son nom (CL4, M1). Les classes `[^[:alnum:]…]` admettent les espaces insécables (U+00A0, U+202F) sans les écrire
  (CL5-08).

## Hypothèse

Ce texte n'éprouve pas d'hypothèse scientifique. Il fixe, avant toute lecture, la lecture de la porte G0 telle que le brief
l'écrit (`docs/brief-claude-code-programme-complet-v2.md`, l. 190-201), recopiée mot pour mot (comparée par `diff` au
fichier empreinté le 2026-10-29 : identique) :

> ### Porte G0 — prêt pour G1
> Tous les critères suivants sont remplis, preuves scellées à l'appui :
> 1. Harnais validé : déterminisme, équivalence d'activations, gardes testées.
> 2. Organismes (i) et (ii) : sabotage mesurable avec dose-réponse.
> 3. Sondes v0 au-dessus du plancher aléatoire apparié, sur (i) et (ii).
> 4. Base boîte noire, par action et séquentielle, qui tourne sur le même jeu d'épisodes.
> 5. Agrégateurs validés en simulation (T0.3).
> 6. Préenregistrement de G1 scellé et contre-lu.
> 7. Préenregistrement du papier C (HC1 à HC3) scellé et contre-lu.
> 8. État de l'art vérifié ; aucun chiffre non vérifié dans un document du programme.
>
> Si un critère ne peut pas être atteint d'ici le 1er novembre : nœud de décision, avec options et défaut.

Ce nœud a été consommé par N-027 (option (a) : lecture au plus tard fin novembre 2026, critères inchangés). Le report
unique au 31 janvier 2027 (R-750) et le gel d'un critère sur échec scellé pendant le report (R-765) sont des décisions de
Lazar sur le **repli** ; elles ne changent aucun critère.

## Prédiction chiffrée et signe attendu

**Sans objet, et volontairement** : une lecture de porte ne prédit aucun signe ; aucune issue n'est visée (R3). La grille ne
contient aucune estimation de la probabilité de franchissement, et aucun constat d'état dans sa partie gelée.

## Métrique

**[GELÉ, proposé à contre-lire]** Deux niveaux d'état, et rien d'autre.

**État d'un critère k** (un seul par critère, prononcé par le lecteur) :

| état | définition |
|---|---|
| **tenu** | toutes les épreuves mécaniques M-k passent **et** toutes les lectures de fond F-k concluent conformes |
| **non tenu — absent** | aucune preuve scellée recevable à l'heure de lecture (rien, brouillon seulement, candidat, preuve scellée après `C_lecture`, préenregistrement sans le run ou le verdict qu'il exige, verdict qui ne prononce pas le critère) |
| **non tenu — négatif** | **résultat seulement** : preuve scellée, intègre et complète, dont la lecture gelée conclut négativement (« réfuté », « non établi », « non prouvé », « aucune sonde au-dessus », ou toute ligne de sa table qui ne prononce pas le critère) ; ou contrôle scellé prévu par la grille qui conclut négativement (M-8.3, F-8.2, F-8.3) ; **ces négatifs des contrôles de la grille restent des négatifs du critère 8, mais ne gèlent jamais un critère (D-G0-13 (a), CLG2-01)**. Un manque n'est jamais un « négatif » (CLG-05). Le verdict dit si ce négatif vient d'une **liste d'arrêt scellée déclenchée**, d'une ligne de la table gelée de la preuve, ou d'un contrôle de la grille (champ (β)) |
| **non tenu — invalide** | preuve présente mais qui échoue une épreuve d'intégrité ou de procédure (empreinte non conforme après vérification R11, contre-lecture absente ou « non scellable », ordre R1 rompu (M-0.4), auteur du verdict non neuf, jeu d'épisodes différent) ; **ou pièce scellée à laquelle manque un contenu que le critère, sa source ou cette grille exige** (hypothèse absente, priorité non statuée, chiffre sans statut) |
| **non concluant** | preuve scellée et intègre dont la lecture gelée conclut « non concluant » ; ou **résultat suspect de propreté, positif ou négatif, au sens de la propre table de la preuve, sans audit R4 scellé à `C_lecture`** (section « Critères de lecture gelés », R4) ; ou pièce inventoriée par M-0.8 absente du dossier ; ou doute du script M-8.3 sur un chiffre « introuvable » (F-8.2) ; ou erreur d'exécution d'un script de la grille (code 3) ; ou version suivante non recevable (section 2) ; ou pièces concurrentes ; ou seuil, niveau ou correction non fixés d'avance par la preuve (F-3.1) ; ou forme imprévue d'une ligne de prononcé ou de verdict (F-1.1, M-0.3) ; ou cas que la grille n'a pas prévu et qui demanderait au lecteur d'interpréter. **Tout « non concluant » cite la ligne de la grille invoquée** |

**Négatif gelant d'une preuve** **[À DÉCIDER, D-G0-14 (a), (d), (e) ; règle de gel EXISTANTE, R-765]** (CL4, B1 ;
CL5-01 à 03, 05, 11). Le gel (D-G0-13) et l'interdiction de toute version suivante (D-G0-7) se lisent **preuve par
preuve**, jamais sur le sous-état que la précédence retient pour le critère. Une preuve P (préenregistrement d'une
sous-expérience, ses runs, son verdict) porte un **négatif gelant** si et seulement si :
(1) (α) de P est « présent » ;
(2) **P est intègre** : aucune des épreuves M-0.1 à M-0.6 ne rend P « absent » ni « invalide », et aucune ligne de
contrôle de la fiche du critère ne rend P elle-même « invalide » (par exemple M-3.2, M-3.5 sous le défaut de D-G0-11,
F-3.4, M-1.2 : un négatif exige une preuve intègre et complète). **Un « non concluant » ne retire pas l'intégrité** : en
particulier un « non concluant » de M-0.3 (forme imprévue de la ligne de verdict d'un rapport de contre-lecture, ou
contre-contrôle) ou de F-1.1 (forme imprévue d'un prononcé) laisse P intègre ; il est rapporté en réserve, ligne citée
(CL5-01) ;
(3) la version de P est recevable (section 2) ;
(4) le négatif de P est de l'une des trois sortes suivantes (une par famille quand le critère est par famille) :
- **par liste d'arrêt** : (β) = « oui » pour la famille concernée, lu par M-0.7. « oui » dit à lui seul que la liste
  d'arrêt scellée a joué et conclut négativement (annexe C point 6) : si le prononcé du verdict n'est pas négatif, ou est
  de forme imprévue, le négatif reste gelant et le sous-état rapporté est « non concluant » (forme imprévue, ligne citée ;
  CL5-02 (ii)). **Une pièce concurrente ne le retire pas**, qu'elle soit antérieure ou postérieure (le lecteur rapporte les
  deux pièces ; sous-état « non concluant ») : R-765 dit qu'un **critère** réfuté par sa liste d'arrêt scellée n'est jamais
  retenté ; la réfutation vaut pour le critère, pas pour la seule pièce, et une pièce concurrente, même antérieure, ne
  l'efface pas (CL5-11 : règle large voulue ; l'option « pièces postérieures seulement » est offerte en D-G0-14 (a)) ;
- **par table** : une ligne de la table gelée de P, que le verdict prononce négative, dont le seuil, le niveau et, s'il y a
  lieu, la correction sont fixés par le préenregistrement de P avant son run ; P n'a aucune pièce concurrente (section 2) ;
  **et aucun audit R4 déclenché par ce verdict n'est resté sans rapport scellé à `C_lecture`** (**[À DÉCIDER, D-G0-14
  (d)]**, défaut ; CL5-03) ;
- **indéterminée** (**[À DÉCIDER, D-G0-14 (e)]** ; CL5-02 (i), CL5-05) : le verdict prononce un négatif et (β) est
  « absent » pour la famille concernée (aucune ligne de forme, deux valeurs distinctes, ou une seule ligne sans famille
  qui dit « oui » dans une preuve à deux familles). Le sous-état rapporté est « non concluant » (forme imprévue, M-0.7
  cité) ; (δ) porte « indéterminé ». sha256` est scellé après celui de la grille
  (`git merge-base --is-ancestor <commit du .sha256 de la grille scellée> <commit du .sha256 du verdict>`, code 0), le
  négatif est **gelant**, traité comme un négatif par liste d'arrêt (aucune version suivante sans mot de Lazar) ; pour un
  verdict scellé avant la grille, il **n'est pas gelant** et il est rapporté en réserve (**règle de transition** :
  aucun des onze verdicts de `docs/verdicts/` au 29 octobre ne porte la ligne de forme, annexe G ; pour eux la branche
  « liste d'arrêt » est inatteignable, et leurs versions suivantes déjà autorisées, comme T0.4 v2 et v3 par N-010 et
  N-011, restent recevables selon D-G0-7).

Le négatif lu contre un seuil, un niveau ou une correction non fixés d'avance **ne gèle rien** (il rend « non concluant »,
F-3.1). Les négatifs des contrôles de la grille (M-8.3, F-8.2, F-8.3) ne sont jamais gelants. Un négatif gelant le reste
quel que soit le sous-état retenu pour son critère : un « absent », un « invalide » ou un « non concluant » venu d'une
autre preuve ou d'une autre famille du même critère ne le masque pas ; le champ (δ) le rapporte. Cas d'un négatif par
liste d'arrêt dont le verdict déclenche aussi un audit R4 sans rapport d'audit scellé à `C_lecture` **[À DÉCIDER, D-G0-14
(c)]** : **défaut** : la liste d'arrêt a joué, le négatif est gelant et aucune version suivante n'est recevable (R-765 à
la lettre : « jamais retenté ») ; le sous-état rapporté du critère reste « non concluant » par R4 ; l'audit reste dû, et un
audit scellé qui nommerait un défaut d'instrument est **sans effet sur la lecture** : toute dérogation exige une décision
de Lazar qui modifie R-765 **et** une nouvelle version de la grille, scellée avant l'ouverture de la lecture (CL5-10
(iii)).

**Précédence des sous-états** **[À DÉCIDER, D-G0-14 (b)]** (CL3, point 4 ; CL4, B1) : elle fixe seulement le sous-état
**rapporté** pour le critère ; elle ne décide ni du gel ni d'aucune version suivante (négatif gelant, ci-dessus). Quand
plusieurs lignes de contrôle d'un même critère rendent des sous-états différents, le lecteur retient le premier dans cet
ordre :
1. « absent » ;
2. « invalide » ;
3. « non concluant » qui touche une pièce dont vient un négatif : suspicion R4 sans audit scellé (section « Critères de
   lecture gelés », R4) ; pièces concurrentes ; version suivante non recevable (section 2) ; seuil, niveau ou correction
   non fixés d'avance (F-3.1) ; forme imprévue de la ligne de prononcé ou de verdict de cette pièce (F-1.1, M-0.3) ;
   (β) « absent » d'un verdict qui prononce un négatif (sorte indéterminée, D-G0-14 (e)) ; (β) « oui » avec un prononcé
   qui n'est pas négatif ;
4. « négatif » ;
5. les autres « non concluant » : motif échoué sur une autre pièce, pièce inventoriée absente du dossier (M-0.8), doute de
   M-8.3, erreur d'exécution d'un script (code 3), cas imprévu.

Dans un même sous-état, la première ligne de contrôle dans l'ordre de la fiche est citée. Ainsi une preuve à la fois
« invalide » et négative rend « invalide » (un négatif exige une preuve intègre et complète) ; deux pièces concurrentes
dont l'une est négative rendent « non concluant » (le lecteur ne choisit pas, section 2) ; un négatif lu contre un niveau
non préenregistré rend « non concluant ». Les paragraphes « États » des fiches suivent cet ordre ; en cas d'écart, cette
règle prime.

Les sous-états de « non tenu » ne changent ni l'état du critère ni celui de la porte ; ils servent au rapport et au repli
(synthèse repli § 4 : une clause en sous-états est compatible avec la grille). Parce que « négatif » ne couvre que des
résultats, une clause qui requalifierait un « absent » en « négatif » (synthèse repli § 5, choix 2) le ferait elle-même,
par une règle écrite, jamais par le mot de la grille.

**Quatre champs constatés par critère, sans effet sur l'état**, pour que la clause de repli en dépende sans décision du
lecteur :
- (α) « préenregistrement scellé, contre-lu, à liste d'arrêt : présent / absent » (M-0.2 passé et section « Liste d'arrêt »
  non vide) ;
- (β) « liste d'arrêt déclenchée » : **« sans objet »** si (α) est absent ou si le critère n'a pas de run (critères 6, 7, 8) ;
  **« oui » / « non »** si le verdict de la preuve porte la **ligne de forme** « Liste d'arrêt déclenchée : oui » ou « … :
  non », lue par le motif ancré `ARRET_BETA` de M-0.7 (puce, numéro, citation, gras, parenthèse avant les deux-points,
  espace insécable et annotation après la valeur admis ; CL4, M6 ; CL5-02 (iii)), avec une seule valeur distincte ;
  **par famille** quand le critère est par famille : une ligne « Liste d'arrêt déclenchée (i) : … » vaut pour la famille
  nommée ; une ligne sans famille vaut pour toutes les familles de la preuve si elle dit « non », et rend (β) « absent »
  pour chacune si elle dit « oui » dans une preuve à deux familles (l'attribution du « oui » ne se lit pas ; CL5-05) ;
  **« absent »** si (α) est présent et que le verdict n'a aucune ligne de cette forme pour la famille, ou deux valeurs
  distinctes (CLG-12) ; aucune autre phrase du verdict n'est lue pour (β) ; un verdict scellé avant cette grille et sans
  cette ligne a (β) « absent », écrit tel quel (règle de transition, négatif gelant, sorte indéterminée) ;
- (γ) « gelé (R-765) » : **« sans objet »** à la première lecture ; à la seconde : « oui » (chemin et commit du `.sha256` de
  la pièce qui l'a gelé, au sens de D-G0-13 : un négatif gelant, champ (δ) ; jamais un négatif de M-8.3, F-8.2 ou F-8.3)
  ou « non » ;
- (δ) « négatif gelant » (D-G0-14 (a)) : **« non »**, ou, pour chaque preuve du critère qui en porte un, son chemin, le
  commit du `.sha256` de son verdict et sa sorte (« liste d'arrêt », « table » ou « indéterminée », D-G0-14 (e)), et
  « gelant » ou « non gelant » pour une sorte indéterminée selon la règle de transition ; constaté à chaque lecture, quel
  que soit le sous-état retenu pour le critère.

**État de la porte** : franchie / non franchie / non concluante (section « Critères de lecture gelés »).

## Seuil

**[GELÉ, proposé]**
- Le seuil de chaque critère est celui de sa preuve : la grille ne fixe aucun seuil statistique nouveau. Quand la preuve est
  un préenregistrement scellé, son seuil et sa table de lecture font foi ; la grille vérifie qu'ils existent, qu'ils ont été
  scellés avant le run, et lit la ligne qui s'applique.
- **Première lecture, unique pour l'échéance du 30 novembre** **[À DÉCIDER, D-G0-1]** (CLG-15) : N-027 dit « au plus tard
  fin novembre 2026 » sans heure. Proposé : ouverte au plus tard le **2026-11-30 à 23:59 UTC** ; elle peut être ouverte plus
  tôt, **une seule fois, sur mot de Lazar seul** (nœud ; cité mot pour mot dans le fichier d'ouverture), jamais sur demande
  d'une session ou d'une lignée ; une lecture anticipée « non franchie » ou « non concluante » n'est pas refaite le
  30 novembre : elle tient lieu de première lecture.
- **Seconde lecture** [EXISTANT, R-750 et R-765 ; mécanique GELÉE] : si la première n'est pas « franchie », une seule
  seconde lecture, **finale**, ouverte au plus tard le **2027-01-31 à 23:59 UTC**, avec **la même grille** (même empreinte),
  son propre fichier d'ouverture et son propre `C_lecture`, selon les mêmes règles que la première (ouverture, lecture
  tardive, coupure). Aucune troisième lecture. Ce que la seconde lecture fait de son issue relève de la clause de repli.
- **Ouverture et `C_lecture`** : la session ouvre chaque lecture par un commit sur `main` du dépôt de travail qui ne contient
  que `registres/g0-lecture-ouverte-vN.md` (rang de la lecture : 1 ou 2 ; date UTC ; mot de Lazar si anticipée ; empreinte
  de la grille scellée ; empreinte du dossier de G0 de cette lecture). `C_lecture` est le **parent** de ce commit, nommé dans
  le verdict.
- **Lecture tardive** : si aucune ouverture n'a eu lieu à l'échéance (2026-11-30 23:59 UTC pour la première, 2027-01-31
  23:59 UTC pour la seconde), `C_lecture` est le dernier commit de `main` antérieur à cette heure ; la porte est lue telle
  quelle au premier moment possible ; le retard est une réserve. Aucune preuve committée après `C_lecture` ne compte.
- **Heure de coupure des preuves** : une preuve compte si son empreinte compagnon est committée sur `main` au plus tard à
  `C_lecture` (`git merge-base --is-ancestor <commit du .sha256> <C_lecture>`).
- **Grille avant lecture** **[À DÉCIDER, D-G0-1]** : scellement de la version finale au plus tard le **2026-11-15**, et
  **seulement avec les points D-G0-1 à D-G0-15 tranchés ou échus** (sinon un critère est « non concluant » par construction).
  **D-G0-1 ne s'applique pas à lui-même** (CL1 § 6) : il exige un **mot explicite** de Lazar. Si ce mot est donné, tout point
  D-G0-2 à D-G0-15 non tranché au 2026-11-15 prend le **défaut** écrit en annexe B, et la grille scellée recopie le choix
  retenu pour chaque point. Sans mot explicite sur D-G0-1 au 2026-11-15, aucun défaut ne s'applique, la grille n'est pas
  scellable et la session ouvre un nœud ; sans grille scellée à l'échéance d'une lecture, cette lecture ne s'ouvre pas
  (liste d'arrêt).
- **La grille elle-même passe M-0.2** : `exiger_prereg_scelle('prereg/G0-grille-lecture-vN.md')` rend son empreinte sans
  erreur. Le lecteur le vérifie avant toute autre chose.

[…]
### 1. Qui lit, avec quoi [GELÉ, R13 ; précisions proposées]

- Un **sous-agent neuf** : il n'a écrit ni cette grille, ni ses contre-lectures, ni aucune des preuves lues
  (préenregistrement, run, analyse, verdict de critère, contre-lecture de ces pièces), ni les tests de la règle de repli sur
  dossiers synthétiques (synthèse repli § 5, choix 10). Il le déclare en tête de son verdict (gabarit, annexe A). Le lecteur
  de la seconde lecture n'est pas celui de la première.
- **[À DÉCIDER, D-G0-6]** Modèle différent de celui des auteurs des preuves, dans la même famille (comme N-052), et lignée
  différente de celle qui a écrit la grille ; modèle et lignée déclarés en tête du verdict ; à défaut, signalé.
- Il reçoit **exactement deux pièces** (R2) : la grille scellée et le **dossier de G0** `docs/verdicts/dossier-G0-vN.md` de
  cette lecture, scellé, séparé de la grille, qui liste par critère : (a) les pièces **remises** (chemin, empreinte, commit
  du `.sha256`) ; (b) pour chaque preuve dont le préenregistrement prévoit un audit de symétrie, la ligne de ce
  préenregistrement qui le définit et la ligne du verdict qui le dit déclenché ou non (R4, CLG-06) ; (c) les pièces
  **écartées**, chacune avec un motif de la liste fermée de M-0.8 ; (d) pour chaque rapport de contre-lecture remis, le
  numéro de la ligne qui porte **son propre verdict** (M-0.3 ; CL4, M2 : une ligne qui cite le verdict d'un autre rapport
  n'est pas désignable). Rien d'autre n'est lu, hors des fichiers que les
  commandes de cette grille ouvrent d'elles-mêmes (inventaire M-0.8, sources citées par chemin).
- **Complétude du dossier** (CLG-01) : le lecteur ne s'en remet pas au dossier ; il exécute l'inventaire **M-0.8**. Toute
  pièce inventoriée absente du dossier rend « non concluant » chaque critère auquel elle se rattache (ligne M-0.8 citée).
  Il **compte**, il n'interprète pas (R13) ; là où une lecture de fond F-k lui laisserait un jugement non écrit ici, il rend
  « non concluant » et cite la ligne.
- Il travaille sur un **clone complet** de `lciric/controle-ia-travail`, branche `main`, au commit `C_lecture` :
  `git rev-parse --is-shallow-repository` rend `false` ; sinon, arrêt (liste d'arrêt). Motif : M-0.4 et la réserve des sept
  jours lisent des dates de commit ; sur un clone superficiel, `git log -- <fichier>` rend la date du commit de greffe
  (constaté par la v2 et par CL1).
- **Interdits de lecture** pour lui comme pour tout auteur : `prereg/P3-consignes-v1.md` ; `donnees/` ; tout `diag/*/traces` ;
  toute branche `donnees/*`, `quarantaine/*` ou `canal/*` (CL5-15 : les passages de la branche de conv-audit dont la
  grille a besoin sont recopiés en annexe B) ; tout fichier nommé « carte des hypothèses ». Aucune preuve de G0 ne doit
  exiger de les ouvrir ; si l'une l'exige, c'est une condition d'arrêt. Une empreinte de ces fichiers peut être vérifiée par
  script sans en afficher le contenu.
- Son verdict est scellé, puis soumis à Lazar pour GO (R13). « Franchie » n'ouvre la phase 1 que sur ce GO ; le GO ne
  requalifie jamais une issue.

### 2. Règle de version : quelle pièce fait foi [GELÉ, proposé]

- Pour chaque critère, la pièce qui fait foi est la **version scellée la plus récente** de son préenregistrement, de son
  verdict et de sa contre-lecture, au sens du numéro `vN` du nom (R12), parmi les pièces remises du dossier. Jamais un
  fichier de `brouillons/`, ni un nom portant « brouillon » ou « candidat », ni un bloc-notes, ni une passation.
- **[À DÉCIDER, D-G0-7]** Une version suivante ne compte que si (a) elle a été autorisée par une décision consignée (nœud ou
  GO) **avant** son run, comme N-010 et N-011 pour T0.4 v2 et v3, et (b) cette décision **nomme une cause distincte du
  résultat** (défaut d'instrument, écart au préenregistrement constaté, garde déclenchée), sinon c'est un retirage (R3, R4).
  Version non autorisée, ou autorisée sans cause nommée : le critère est « non concluant » (la version précédente ne
  « revient » pas). Après un **négatif gelant par liste d'arrêt** d'une preuve, ou de sorte indéterminée gelante (Métrique ;
  D-G0-14 (a) et (e)), **aucune version suivante de cette preuve n'est recevable**, quel que soit le sous-état retenu pour le critère [EXISTANT, R-765 : « un
  critère réfuté par sa liste d'arrêt scellée n'est jamais retenté »] ; le cas d'un audit R4 sans rapport scellé suit
  D-G0-14 (c). **Exception pendant le report** (CLG2-01) : entre le verdict de la première lecture et la seconde lecture,
  un critère gelé au sens de D-G0-13 (a) n'admet aucune version suivante, même autorisée avec cause nommée (R-765 : « gèle
  ce critère jusqu'au second verdict ») ; hors de ce gel, la règle ci-dessus vaut aussi pour un négatif gelant par table
  prononcé au verdict de la première lecture (D-G0-13 (b), défaut). Le lecteur rapporte, en réserve, le nombre de versions
  par critère.
- **Seconde lecture et gel** **[À DÉCIDER, D-G0-13 ; règle de gel EXISTANTE, R-765]** : un critère est **gelé** au sens de
  D-G0-13 dans deux cas seulement, tous deux lus sur le champ (δ), jamais sur le sous-état retenu par la précédence
  (D-G0-14 (a)) : (a) pendant le report, un **négatif gelant** (par liste d'arrêt ou par table) d'une preuve du critère dont
  le verdict est scellé après le verdict de la première lecture ; (b) au verdict de la première lecture, un **négatif gelant
  par liste d'arrêt** d'une preuve du critère, ou de sorte indéterminée gelante (D-G0-14 (e)). Les négatifs des contrôles de la grille (M-8.3, F-8.2, F-8.3) ne gèlent pas ;
  un critère dont aucune preuve ne porte de négatif gelant ne gèle pas, quel que soit son sous-état ; un critère dont une
  preuve en porte un gèle, même si son sous-état rapporté est « absent », « invalide » ou « non concluant ». Un critère gelé
  est lu, à la seconde lecture, sur la pièce qui l'a gelé ; quand plusieurs négatifs gelants existent sur le même critère,
  c'est le premier dans l'ordre d'ascendance des commits des `.sha256` de leurs verdicts (`git merge-base --is-ancestor
  <commit A> <commit B>`, code 0 : A avant B ; CL4 m7) ; s'ils sont au même commit, ou sans relation d'ascendance, ce sont
  des pièces concurrentes : le critère reste gelé et son sous-état est « non concluant » (le lecteur ne choisit pas). Toute
  version ou pièce postérieure portant sur un critère gelé n'est pas recevable (écartée sous le motif (m4) de M-0.8 et
  rapportée en réserve, avec son chemin) ; le champ (γ) le dit. Commande :
  `git merge-base --is-ancestor <commit du .sha256 du verdict de G0 de la première lecture> <commit du .sha256 de la pièce>`
  (code 0 : pièce scellée pendant le report).
- Si deux pièces scellées concurrentes portent sur le même critère sans relation de version, le lecteur rend « non concluant »
  et le dit (il ne choisit pas) ; la précédence range ce « non concluant » avant « négatif » (Métrique), et un négatif de
  l'une des deux n'est gelant que s'il vient de sa liste d'arrêt (Métrique, négatif gelant).

### 3. Épreuves mécaniques communes (M-0) [GELÉ]

Préalable à toute commande : `export LC_ALL=C.UTF-8 PYTHONPATH=src` (section 0). Pour toute pièce du dossier citée comme
preuve, dans l'ordre, chaque ligne avec sa commande, sa sortie attendue et l'état si échec. Dans les motifs ci-dessous,
`NEUTRE` désigne :
`sous-agent neuf|contre-lecteur neuf|n['’]ai (pas )?écrit|ne suis (pas )?l['’]auteur|l['’]auteur ni (du|de|des|le|la|les|l['’])`.
Pour M-0.3 (CL4, M2), `VERDICT_CL` désigne
`(non[- ]|pas (encore )?)scellable|à corriger avant (le )?scellement|scellable( après corrections)?` (alternance POSIX : la
forme négative, qui commence plus tôt sur la ligne, l'emporte sur « scellable » seul) ; `NEG_CL` désigne `^(non|pas)|corriger` ;
`IMPREVU_CL` désigne
`(\bnon\b|\bpas\b|\bjamais\b|\bni\b|\bloin\b)[^.;]{0,30}scellable|scellable( après corrections)?[^.;]{0,40}(\bnon\b|\bpas\b|r(é|e)serve|sauf|\bsi\b|condition|\bmais\b|toutefois|cependant|corriger)`
(une négation avant la forme, ou une forme suivie, dans la même proposition, d'une négation, d'une réserve ou d'une
condition : « Non encore scellable », « Scellable : non », « Scellable si … », « Scellable mais … » ; CL5-06) ;
`NETTOIE` désigne l'expression `sed -E` `s/[A-Za-z0-9_\/.-]+\.(md|py|json|jsonl|txt|tsv|sha256)\b//g` (retire les noms
de fichier, dont le point coupait la phrase ; CL5-06) ; `NEG_DEBUT` désigne
`^[*#> -]*(non[- ]scellable|pas (encore )?scellable|à corriger avant)` (une ligne qui **commence** par une forme
négative ; contre-contrôle, CL5-07).
Pour M-0.7 (CL4, M6 et m10 ; CL5-02, CL5-05), `ARRET_BETA` désigne
`^[-*>0-9. ]*listes? d['’]arr(ê|e)t d(é|e)clench(é|e)e?s?( \([^)]*\))?[^[:alnum:]:]{0,4}:[^[:alnum:]]{0,4}(oui|non)([^[:alpha:]]|$)`
(ligne de forme « Liste d'arrêt déclenchée : oui » ou « … : non » ; puce, numéro, citation `>`, gras, parenthèse — dont
la famille « (i) », « (ii) » —, espace insécable avant les deux-points, ponctuation et annotation après la valeur admis ;
une phrase qui ne commence pas par « Liste d'arrêt déclenchée » n'est pas prise).

| n° | épreuve | commande (depuis la racine du clone complet) | sortie attendue | état si échec |
|---|---|---|---|
| M-0.1 | intégrité | `python -m controle_ia.scellement verifier <fichier>` ; pour un fichier annoncé absent : `ls -la <fichier> <fichier>.sha256 ; sha256sum <fichier>` (R11) | `OK` ; empreinte égale à celle du dossier | « non tenu — invalide » (présent mais non conforme) ; « non tenu — absent » (absent après R11) |
| M-0.2 | préenregistrement conforme R1/R2 | `python -c "from controle_ia.prereg import exiger_prereg_scelle as e; print(e('<prereg>'))"` | l'empreinte, sans `GardeArret` | « non tenu — invalide » |
| M-0.3 | contre-lecture R2 (CL4, M2 ; CL5-06, CL5-07) | pour chaque rapport cité dans la section « Contre-lecture » : M-0.1 ; `head -5 <rapport> \| grep -c -i -E "NEUTRE"` ; avec `<l>` = **ligne de verdict du rapport désignée par le dossier** (section 1, (d)) et `<L>` = sortie de `sed -n '<l>p' <rapport> \| sed -E "NETTOIE"` : (1) `<L> \| grep -o -i -E "VERDICT_CL" \| head -1 \| grep -c .` (une forme trouvée) ; (2) `<L> \| grep -o -i -E "VERDICT_CL" \| head -1 \| grep -c -i -E "NEG_CL"` (première forme) ; (3) `<L> \| grep -c -i -E "IMPREVU_CL"` ; (4) contre-contrôle : `grep -n -i -E "NEG_DEBUT" <rapport>` (lignes autres que `<l>`) ; (5) pour un rapport scellé après la grille (`git merge-base --is-ancestor <commit du .sha256 de la grille scellée> <commit du .sha256 du rapport>`, code 0) : `<l>` ≤ 10 et `<L> \| grep -c -i -E "^[*#> -]*(VERDICT_CL)"` = 1 ; pour chaque remarque numérotée du rapport, `grep -n "<numéro>" <prereg>` | rapport intègre ; au moins une ligne de neutralité dans les cinq premières lignes ; ligne `<l>` recopiée dans le verdict ; lus **dans cet ordre** : (1) = 1, (2) = 0 (« Scellable », « Scellable après corrections »), (3) = 0, (4) vide, (5) tenu s'il s'applique : conforme ; chaque remarque trouvée dans le préenregistrement avec un traitement (accepté / refusé et pourquoi) | (1) = 1 et (2) = 1 (« non scellable », « non-scellable », « pas (encore) scellable », « à corriger avant (le) scellement ») : « non tenu — invalide » ; remarque sans traitement : « non tenu — invalide » ; (1) = 0, (3) ≥ 1, (4) non vide (une autre ligne du rapport commence par une forme négative), ligne `<l>` non désignée par le dossier, ou (5) non tenu (annexe C point 6) : **non concluant** (forme imprévue, ligne citée ; jamais « invalide » ; ne retire pas l'intégrité de la preuve, Métrique (2)) |
| M-0.4 | ordre R1 (preuve empirique) | `python -c "import json;m=json.load(open('runs/<run>/manifeste.json'));print(m['preenregistrement'],m['cree_le'])"` ; `git log --format='%H %cI' -- <prereg>.sha256 \| tail -1` ; `git merge-base --is-ancestor <commit de scellement> <commit du run cité par le manifeste>` | empreinte du manifeste égale à celle du fichier scellé ; date du commit de scellement antérieure à `cree_le` ; code 0 | « non tenu — invalide » (ordre R1 rompu). Une date de commit peut être falsifiée : contrôle rapporté comme fait, pas comme preuve absolue |
| M-0.5 | verdict scellé de la preuve | M-0.1 sur le verdict ; `grep -n "<empreinte du prereg>" <verdict>` ; `head -5 <verdict> \| grep -c -i -E "NEUTRE"` | verdict cite l'empreinte du préenregistrement, égale au fichier ; une ligne de neutralité dans ses cinq premières lignes (ou, pour T0.3, lecture produite par le code gelé cité au manifeste) | « non tenu — invalide » ; **[À DÉCIDER, D-G0-8]** absence de verdict scellé pour un critère empirique = « non tenu — absent » (défaut) |
| M-0.6 | coupure | `git log --format=%H -1 -- <fichier>.sha256` ; `git merge-base --is-ancestor <ce commit> <C_lecture>` | code 0 | pièce non recevable → « non tenu — absent » si aucune autre pièce |
| M-0.7 | champs (α) et (β) de la Métrique | `python -c "from controle_ia.prereg import sections;s=sections(open('<prereg>',encoding='utf-8').read());print(bool(s.get('Liste d\'arrêt')))"` ; dans le verdict de la preuve : `grep -n -i -E "ARRET_BETA" <verdict>` (lignes recopiées) ; pour chaque ligne prise, famille : `\| grep -o -E "\((i\|ii)(-[a-z])?\)"` (aucune : ligne sans famille) ; valeur : `\| sed -E 's/^[^:]*:[^[:alnum:]]{0,4}//' \| grep -o -i -E "^(oui\|non)"` ; valeurs distinctes par famille (`sort -u -f`) | (α) `True` + M-0.2 passé = « présent » ; (β), par famille : une seule valeur distincte, « oui » ou « non » ; aucune ligne, deux valeurs distinctes, ou ligne sans famille « oui » dans une preuve à deux familles : (β) « absent » ; aucune autre phrase du verdict n'est lue (CL4, M6 ; CL5-02, CL5-05) | aucun effet sur l'état ; champs rapportés ; (β) alimente (δ) (Métrique) |
| M-0.8 | **inventaire de complétude** (CLG-01) | (a) pièces : script M-0.8 ci-dessous ; (b) runs : pour chaque `runs/*/manifeste.json` dont `preenregistrement.chemin` figure dans la sortie de (a), le chemin du run | chaque fichier de (a) et chaque run de (b) figure au dossier, **remis** pour un critère ou **écarté** sous un motif de la liste fermée | pièce ou run absent du dossier : « non concluant » pour chaque critère auquel il se rattache ; motif hors liste : idem ; écartés recopiés en réserve, avec leur motif |

**Script M-0.8 (a)**, exécuté tel quel (il n'ouvre aucun fichier interdit : la liste est filtrée par nom avant toute
lecture). Il parcourt aussi `prereg/contre-lectures/` (CLG2-07) : dans ce dossier, « brouillon » et « candidat » n'excluent
pas (la contre-lecture d'un brouillon est une pièce scellée, et une contre-lecture « non scellable » que le préenregistrement
ne cite pas doit être inventoriée), et le préfixe est cherché en tête du nom ou après un tiret. Les pièces de la grille
elle-même (`*G0-grille-lecture*` : brouillons, version scellée, contre-lectures) sont exclues par nom : elles sont
l'instrument de la lecture, pas la preuve d'un critère (sans cette exclusion, elles seraient inventoriées par leur contenu,
annexe F).

```
export LC_ALL=C.UTF-8
for f in $(find prereg docs/verdicts docs/etat-de-l-art prereg/contre-lectures -maxdepth 1 -type f -name '*.md' ! -name 'P3-consignes-v1.md' ! -name '*G0-grille-lecture*' | sort -u); do
  [ -f "$f.sha256" ] || continue
  b=$(basename "$f")
  case "$f" in
    prereg/contre-lectures/*) motif='(^|-)(T0\.[3-8]|P3-|P4-instrument|G1-|papier-C-|etat-de-l-art)' ;;
    *) echo "$b" | grep -q -i -E 'brouillon|candidat' && continue
       motif='^((verdict|audit-R4)-)?(T0\.[3-8]|P3-|P4-instrument|G1-|papier-C-|etat-de-l-art)' ;;
  esac
  if echo "$b" | grep -q -E "$motif" \
     || grep -q -i -E 'crit(è|e)res? [0-9]([^0-9][^|]{0,60})?G0' "$f"; then echo "$f"; fi
done
```

**Script M-0.8 (b)**, sur la sortie de (a) enregistrée dans un fichier hors du clone :

```
python -I -c "import json,glob,sys
inv=set(open(sys.argv[1]).read().split())
for m in sorted(glob.glob('runs/*/manifeste.json')):
    p=json.load(open(m,encoding='utf-8')).get('preenregistrement') or {}
    c=p.get('chemin') if isinstance(p,dict) else p
    if c in inv: print(m, c)" <sortie de (a)>
```

**Rattachement à un critère** : par le préfixe que le motif du script trouve dans le nom (T0.4 → 1 ; T0.5, T0.6 → 2 ; P3- → 2 et 3 ; T0.7, P4-instrument → 3 ; T0.8 → 4 ;
T0.3 → 5 ; G1- → 6 ; papier-C- → 7 ; etat-de-l-art → 8) **et** par le contenu (chaque numéro k des lignes qui rendent
`grep -n -i -o -E 'crit(è|e)res? [0-9]([^0-9][^|]{0,60})?G0' <fichier>`). Un run se rattache aux critères de son
préenregistrement.

**Motifs d'écart, liste fermée** : (m1) **version antérieure** d'une série dont une version postérieure est remise (même nom
à `vN` près) ; (m2) **pièce auxiliaire** d'une pièce remise (addendum, audit, contre-lecture, différentiel, archive, run),
nommée par celle-ci **par son nom de base** (`grep -n -F "<nom de base de la pièce écartée>" <pièce remise>` rend au moins
une ligne ; le nom de base prend aussi une citation par chemin complet, CLG2-07) ; (m3) **autre**, motif écrit par la session
dans le dossier ; (m4) **postérieure au gel** (D-G0-13, CLG2-05) : à la seconde lecture seulement, pièce scellée pendant le
report sur un critère gelé ; le dossier donne le chemin du verdict de G0 de la première lecture ; contrôle : commande de la
section 2 (`git merge-base --is-ancestor …`, code 0) et champ (γ) « oui » pour ce critère ; sinon le motif est hors liste.
Le lecteur ne juge aucun motif (m3) : il le recopie, en réserve du critère, avec le chemin de la pièce et la ligne de
conclusion que la pièce donne d'elle-même (première ligne de sa section d'en-tête ou de verdict). Une pièce (m1) n'est
recevable comme écart que si la version postérieure est elle-même recevable (section 2). Une pièce (m4) est recopiée en
réserve comme une pièce (m3).

[…]
## Critères de lecture gelés

**[GELÉ, proposé à contre-lire] Agrégation, écrite avant toute lecture ; la même aux deux lectures.**

| états des huit critères | état de la porte | suite |
|---|---|---|
| huit « tenu » | **franchie** | verdict scellé, puis Lazar (GO) ; la phase 1 s'ouvre seulement sur ce GO (R13) ; le GO ne requalifie pas |
| au moins un « non tenu » (quel qu'en soit le sous-état) | **non franchie** | clause de repli (section « Repli ») |
| aucun « non tenu », au moins un « non concluant » | **non concluante** | **la même suite que « non franchie »** : clause de repli |

Justification :
- **Un seul critère non tenu suffit** : le brief exige « tous les critères suivants sont remplis » ; une porte « aux trois
  quarts » n'existe pas.
- **« Non concluante » n'est jamais une seconde chance** : même suite que « non franchie ». Elle existe pour que le rapport
  dise juste et pour que le repli puisse traiter différemment, dans sa propre clause, un critère absent, négatif ou indécidé.
  Cette identité de suite est demandée par l'avis conv-audit (point 3 : « même suite pour les deux états ») et fondée par
  l'avis Fable repli (`f3435cfd…`, l. 48-49 : une porte « non concluante » serait une porte « on verra », « non
  scellable ») ; l'avis Fable grille (l. 54) juge seulement la table « sûre » (CLG-15) ; la synthèse repli § 4 la retrouve
  chez deux des trois modèles.
- **Pas de pondération, pas d'ordre** entre critères à la porte ; l'ordre de travail vit dans la reprise, pas dans la lecture.

**Réserves et audit de symétrie (R4)** (CLG-06) :
- Les réserves ne changent aucun état ; elles sont toutes recopiées dans le verdict, avec la ligne de la grille qui les
  ouvre. Toute réserve ouverte par une preuve (sa table gelée, ses addenda) est recopiée ; toute pièce écartée (M-0.8) aussi.
- **Résultat suspect de propreté, positif ou négatif** : pour chaque preuve, le lecteur lit les deux lignes que le dossier
  désigne (définition de l'audit dans le préenregistrement ; constat dans le verdict) et applique à la ligne du verdict le
  motif `(n['’](est|a) pas|non|aucun|False)[^.]{0,40}d(é|e)clench|d(é|e)clench[^.]{0,30}: ?(False|non|aucun)` : 1 = non
  déclenché ; 0 = déclenché. Audit déclenché, **dans un sens ou dans l'autre**, sans rapport d'audit scellé au dossier à
  `C_lecture` : **non concluant** pour le critère (le gel suit D-G0-14 (c) et (d)). **Pour une preuve à run seulement**
  (critères 1 à 5 ; (β) ≠ « sans objet ») : préenregistrement qui contient `R4` ou `symétrie`
  (`grep -c -i -E "R4|symétrie"` ≥ 1) sans les deux lignes désignées au dossier : non concluant (ligne citée) ;
  préenregistrement à (α) « présent » sans `R4` ni `symétrie` (`grep -c -i -E "R4|symétrie"` = 0) : **non concluant**
  pour le critère (ligne citée) ; le déclencheur R4 n'est pas défini par la preuve. **Aucune de ces deux clauses** ne
  s'applique aux préenregistrements de G1 et du papier C (critères 6 et 7, sans run ni verdict avant G0 : R4 vise des
  résultats, et ces préenregistrements n'ont aucune ligne de verdict à désigner) ; elles ne durcissent donc ni le critère 6
  ni le critère 7 (CL4, M5 ; CL5-04 ; même logique que D-G0-4).
- **Réserve des sept jours, mécanique** : `git log --format=%cI -1 -- <verdict du critère>.sha256` postérieure ou égale à la
  date de `C_lecture` moins sept jours → réserve « preuve récente », quel que soit le sens du verdict ; **aucun audit par le
  lecteur** ; la pièce est signalée, dans le verdict, pour un audit R4 après lecture, sans effet sur l'état.

**Forme du verdict** : gabarit de l'annexe A, et rien d'autre (aucune recommandation sur la suite : elle est écrite dans le
repli).

## Liste d'arrêt

La lecture s'arrête, sans verdict de porte, et la session ouvre un nœud pour Lazar, si :
- aucune grille scellée n'existe à l'échéance de la lecture ; ou l'empreinte de la grille scellée ne correspond pas au
  fichier remis au lecteur ; ou la grille échoue M-0.2 ;
- le lecteur n'est pas neuf au sens de la section 1 du plan d'analyse ;
- le clone est superficiel (`git rev-parse --is-shallow-repository` ≠ `false`) ou n'est pas à `C_lecture` ;
- la locale `C.UTF-8` n'est pas disponible (`locale -a | grep -i -c -E "^c\.utf-?8$"` = 0) ;
- `registres/g0-lecture-ouverte-vN.md` manque, ou, pour une lecture anticipée, ne cite pas le mot de Lazar ;
- le dossier de G0 manque ou échoue M-0.1 ;
- pour la lecture n° 2, le dossier ne donne pas le verdict scellé de la lecture n° 1 (chemin, empreinte, commit du
  `.sha256`), ou ce verdict échoue M-0.1 (le champ (γ) et le motif (m4) seraient incalculables) ;
- une preuve exige d'ouvrir un fichier interdit (section 1) ;
- `cd docs && sha256sum -c sha256sums-lancement-v2.txt` ou `python -m controle_ia.scellement verifier-arbre .` échoue au
  commit `C_lecture` sur un fichier cité par la grille ou le dossier (R11 appliqué avant de conclure).

Un arrêt n'est pas une lecture : il ne vaut ni « non franchie » ni « non concluante ». (La lecture tardive n'est pas un
arrêt : voir « Seuil ».) **Reprise après un arrêt** **[À DÉCIDER, D-G0-15]** (CL5-14 ; mémo G0-2 et table D-TD-2 (a),
recopiés en annexe B) : **défaut** : tout s'arrête jusqu'au mot de Lazar ; à la levée de la cause, **la même lecture
reprend**, avec le même fichier d'ouverture et le même `C_lecture` (aucune preuve committée après lui ne compte), et un
lecteur neuf si la cause touchait le lecteur ; la session consigne la durée de l'arrêt ; une lecture reprise après son
échéance n'est pas « tardive » (son `C_lecture` est celui de l'ouverture) ; aucune nouvelle ouverture n'est permise pour la
même échéance.

## Repli

**Clause décidée par Lazar, à insérer ici (décision N-027 bis, quand tout sera fixé). La grille ne tranche rien du repli.**

**Fixé par Lazar au 2026-10-29** (cité, non rediscuté) :
- **R-750** (`registres/decisions.md` l. 978) : borne du report au **31 janvier 2027** (« 31 janvier : go ») ; le report
  est unique (R-765 : « un seul verdict final »).
- **R-765** (l. 993) : choix 1 de la synthèse tranché pour le gel : **un échec scellé d'un critère pendant le report gèle
  ce critère jusqu'au second verdict ; il ne ferme pas la porte en cours de report** ; un seul verdict final au 31 janvier
  2027 au plus tard ; un critère réfuté par sa liste d'arrêt scellée n'est jamais retenté.

**Reste à fixer : les onze autres choix** de la synthèse (`docs/notes/porte-g0-repli-v1/synthese-collisionneur-repli-g0-v1.md`,
`527f5853…`, § 5, l. 146-163), à présenter en un bloc avec cette grille : (2) préenregistrement absent pour 2, 3, 4 =
« négatif » ou « absent » ; (3) grille scellée ≤ 15 novembre, D-G0 tranchés ou échus, même grille aux deux lectures ;
(4) empreintes hors dépôt et horodatage externe ; (5) plafond, séquence, imputation ; (6) table de dépendance et pilote ρ ;
(7) périmètre du critère 8 et quarantaine ; (8) rôle du GO ; (9) sous-agents R13 d'un autre modèle ; (10) tests de la règle
sur dossiers synthétiques ; (11) gabarit du rapport, R-750 dans `docs/decisions/`, aucune condition de progrès ; (12) sort du
papier C et du palier GC. Les choix 3 et 7 recoupent D-G0-1 et D-G0-9 : une même décision les règle.

Ce que la grille garantit pour la clause, quelle qu'elle soit :
1. « non franchie » et « non concluante » ont la même suite, aux deux lectures ;
2. les sous-états « absent », « négatif », « invalide » et « non concluant » sont prononcés par critère ; « négatif » ne
   couvre que des résultats (CLG-05) ; pour tout « négatif », le verdict dit s'il vient d'une **liste d'arrêt scellée
   déclenchée**, d'une ligne de la table gelée de la preuve, ou d'un contrôle de la grille (champ (β)) ;
3. le verdict rend constatable, par critère, « préenregistrement scellé, contre-lu, à liste d'arrêt : présent / absent »
   (champ (α)), pour le choix 2 ;
4. la règle de version ne rend recevable aucune version suivante après un négatif gelant par liste d'arrêt (R-765), ou
   de sorte indéterminée gelante, quel que soit le sous-état retenu pour le critère (D-G0-14 (a), (e)) ;
5. à la seconde lecture, un critère gelé au sens de D-G0-13 est lu sur la pièce qui l'a gelé, et le champ (γ) le constate
   (R-765) ; seul gèle un **négatif gelant** (Métrique ; champ (δ), constaté à chaque lecture), c'est-à-dire un négatif
   d'une preuve intègre dont (α) est « présent », issu de sa liste d'arrêt ou d'une ligne de sa table gelée à seuil fixé
   d'avance ; les négatifs des contrôles de la grille (M-8.3, F-8.2, F-8.3) ne gèlent jamais (CLG2-01) ; aucun sous-état
   retenu par la précédence ne masque un négatif gelant (CL4, B1) ;
6. la grille sert telle quelle à la seconde lecture, avec son propre `C_lecture` et son propre fichier d'ouverture ; la
   table d'agrégation est la même.

La grille ne dit rien de ce que vaut un préenregistrement absent au-delà de « non tenu — absent » (choix 2), ni de ce que
fait la seconde issue au-delà de son état : c'est la clause.

[…]
## Annexe B — index des points à décider (D-G0-1 à D-G0-15), recommandations et défauts

**D-G0-1 exige un mot explicite de Lazar et n'a pas de défaut.** S'il est accepté, tout point D-G0-2 à D-G0-15 non tranché
au 2026-11-15 prend la colonne « défaut ». Sans ce mot au 2026-11-15, aucun défaut ne s'applique et la grille n'est pas
scellable (nœud).

| n° | objet | option 1 | option 2 |
|---|---|---|---|
| D-G0-1 | première lecture au plus tard le 2026-11-30 23:59 UTC, unique pour cette échéance ; anticipable une seule fois sur mot de Lazar seul ; grille scellée ≤ 2026-11-15 avec D-G0-1 à 15 tranchés ou échus ; règle des défauts ci-dessus | **aucun : mot explicite exigé** | — |
| D-G0-2 | critère 2 délégué au préenregistrement de T0.6 sous conditions (a)-(d) | délégation sous (a)-(d) | définition fixée dans la grille |
| D-G0-3 | « tourne » = sans arrêt de garde + part de scores finis fixée d'avance par T0.8, mêmes deux grains, avant toute lecture ; « tourne » ≠ « détecte » | cette définition | définition plus stricte (part de scores finis ≥ seuil plancher fixé par Lazar) |
| D-G0-4 | critères 6 et 7 : contrôle de présence des décisions renvoyées, attesté par le contre-lecteur R2 ; listes N-007/N-008, N-034, N-054, N-055, N-056, N-060 v3, R-746 (G1) ; N-005/N-006, N-013, N-023, R-307, R-309 (C) | **réserve** | condition (non tenu — invalide) |
| D-G0-5 | critère 1 hors domaine sans garde en ligne ; garde de P-007 exigée dans T0.6 à T0.8 | **réserve** + exigence amont | non tenu — invalide du critère concerné |
| D-G0-6 | lecteur d'un modèle différent des auteurs des preuves, même famille ; lignée différente de celle de la grille | oui, déclaré, à défaut signalé | non exigé (le lecteur peut être du même modèle) |
| D-G0-7 | version suivante recevable seulement si autorisée avant son run avec une cause nommée distincte du résultat ; sinon non concluant ; aucune après un **négatif gelant par liste d'arrêt** d'une preuve, quel que soit le sous-état retenu (R-765 ; D-G0-14) ; **exception pendant le report** : un critère gelé (D-G0-13) n'admet aucune version suivante, même autorisée avec cause nommée (section 2) | cette règle | pas d'exception pendant le report (la règle ci-dessus vaut partout) — **contraire à R-765** (« gèle ce critère jusqu'au second verdict ») : ne peut être retenue que par un mot de Lazar qui modifie R-765 (CL4 m6) |
| D-G0-8 | verdict scellé par sous-agent neuf exigé pour 2, 3, 4 (rapport de fonctionnement suffisant pour 4) ; absence = non tenu — absent | cette règle | rapport de fonctionnement suffisant pour 2, 3, 4 ; voir aussi la divergence DIV-2 ci-dessous |
| D-G0-9 | critère 8 : périmètre (A) en condition, chiffres externes ; internes sous R6 en réserve ; (B) au script en réserve ; périmètre gelé en annexe E | **(A)**, (B) en réserve | (B) ou (C) en condition |
| D-G0-10 | critère 5 : « validés » = toutes les prédictions « confirmée », aucune « réfutée », audit R4 « déclenché : False » ou scellé | **option Fable** | ligne de synthèse de la lecture |
| D-G0-11 | critère 3 : P4-instrument absent ou postérieur | **condition** (non tenu — invalide, M-3.2 et M-3.5 ensemble) | réserve (CL1 § 6) |
| D-G0-12 | critère 4 : TRACE-lite absent | **réserve** | non tenu — absent (lecture littérale du brief T0.8) |
| D-G0-13 | raccord de R-765 à la grille, lu sur le **négatif gelant** (Métrique, D-G0-14 (a)) et jamais sur le sous-état retenu. (a) « échec scellé » pendant le report = **négatif gelant** d'une preuve du critère dont le verdict est scellé après le verdict de la première lecture : preuve à (α) « présent », intègre (M-0.1 à M-0.6 et aucune ligne de sa fiche qui la rende « invalide »), version recevable, négatif issu de sa liste d'arrêt déclenchée ((β) = « oui ») ou d'une ligne de sa table gelée à seuil, niveau et correction fixés d'avance, sans pièce concurrente ; **jamais** un négatif de M-8.3, F-8.2 ou F-8.3 ; un critère sans négatif gelant ne gèle pas, quel que soit son sous-état ; (b) au verdict de la première lecture, seul le **négatif gelant par liste d'arrêt** gèle ; un négatif gelant par table admet une version suivante recevable selon D-G0-7, sinon non concluant ; (c) un critère gelé est lu à la seconde lecture sur la pièce qui l'a gelé ; plusieurs négatifs gelants : le premier dans l'ordre d'ascendance des commits des `.sha256` de leurs verdicts (`git merge-base --is-ancestor`) ; même commit ou sans ascendance : pièces concurrentes, critère gelé et « non concluant » ; toute pièce postérieure sur ce critère est non recevable et rapportée en réserve (CL4 m5, m7) | **(a) restreint, (b) règle de D-G0-7, (c)** | variante v3 : (a), (b) tout négatif de la première lecture gelé (statut reporté tel quel), (c) ; voir aussi la divergence DIV-1 ci-dessous |
| D-G0-14 | **v6, étendu par la v7 (CL4, B1 ; CL5-01 à 03, 05, 10, 11)**. *Enjeu* : ce qui gèle un critère et interdit toute version suivante (R-765) ; une règle trop large gèle sur une faute de forme, une règle trop étroite laisse retenter un critère réfuté. (a) le gel (D-G0-13) et l'interdiction de toute version suivante (D-G0-7) se lisent **preuve par preuve** sur le négatif gelant (Métrique), indépendamment du sous-état retenu ; un « absent », « invalide » ou « non concluant » d'une autre preuve ou d'une autre famille ne le masque pas ; un « non concluant » de la preuve elle-même (M-0.3, F-1.1) ne retire pas son intégrité ; le négatif lu contre un seuil, un niveau ou une correction non fixés d'avance ne gèle rien ; un négatif par liste d'arrêt reste gelant malgré toute pièce concurrente, antérieure ou postérieure ; (b) précédence des sous-états, seulement pour le sous-état rapporté (Métrique) ; (c) négatif par liste d'arrêt d'un verdict qui déclenche aussi un audit R4 sans rapport scellé ; (d) négatif par table d'un verdict qui déclenche un audit R4 sans rapport scellé ; (e) négatif de sorte indéterminée ((β) « absent ») | **(a) et (b) tels qu'écrits ; (c) gelant, aucune version suivante (R-765 à la lettre), sous-état « non concluant », audit dû, sans effet sur la lecture : toute dérogation exige une décision de Lazar qui modifie R-765 et une nouvelle version de la grille scellée avant l'ouverture ; (d) non gelant tant que l'audit n'est pas scellé (sous-état « non concluant ») ; (e) gelant pour un verdict scellé après la grille, non gelant (réserve) pour un verdict scellé avant (règle de transition).** 
| D-G0-15 | **nouveau (v7 ; CL5-14 ; DIV-3)**. *Enjeu* : un arrêt (liste d'arrêt de la lecture) ne doit devenir ni un second report de fait, ni une nouvelle ouverture à `C_lecture` plus tardif. Reprise d'une lecture arrêtée | **la même lecture reprend à la levée de la cause, même fichier d'ouverture, même `C_lecture`, lecteur neuf si la cause le touchait ; la durée de l'arrêt est consignée ; une lecture reprise après son échéance n'est pas tardive ; aucune nouvelle ouverture pour la même échéance.** 

**Divergences avec la table de dépendance de G0 v4 et le mémo de conv-audit, non tranchées par cette grille** (pièces
citées en tête : table `8226dd55…`, mémo `9daeb52b…` au commit `174b82d0`, § I ; passages recopiés mot pour mot
ci-dessous). Elles se décident dans le même bloc que D-G0-1 à D-G0-15 ; jusque-là la grille garde son défaut, et la table
garde le sien.

| n° | objet | grille v7 | table v4 / mémo | à décider |
|---|---|---|---|
| DIV-1 | portée du gel au premier verdict | D-G0-13 (b) : seul le négatif gelant **par liste d'arrêt** gèle au verdict du 30 novembre ; un négatif gelant par table admet une version suivante autorisée avant son run sur cause nommée (D-G0-7) | table l. 14 : « tout négatif scellé au 30 novembre (lu par V1) ou pendant le report » gèle ; l. 41 et L2bis (l. 130) : gel = critères dont la classe lue du produit est « négatif » | Lazar : (i) défaut de la grille (CL2 § 3 ; précédent T0.4 v2-v3) ; (ii) lecture de la table (tout négatif scellé au 30 novembre gèle). La grille ne lit pas la table : son scellement n'en dépend pas ; la table s'aligne sur le choix retenu (CL5-14) ; si (ii) est retenue, la grille change (D-G0-13 (b)) et l'annexe C point 1 s'applique |
| DIV-2 | D-G0-8, quel verdict pour quels critères | verdict scellé par un sous-agent neuf exigé pour 2, 3, 4, un rapport de fonctionnement suffisant pour 4 ; critère 5 lu sur la lecture produite par le code gelé ; critère 1 sur sa série de verdicts | table l. 227 et mémo G0-5 (a) : verdict scellé pour chacun des critères empiriques 1 à 5, avec, pour chaque ligne qui nomme « critère k de G0 », la valeur copiée et sa classe (établi, négatif, autre) | Lazar : la forme « valeur copiée et classe » et l'exigence d'un verdict pour 4 et 5 changeraient M-0.5, F-4.x et F-5.x ; défaut de la grille inchangé tant que rien n'est tranché ; si la forme de la table est retenue, une version suivante de la grille et sa contre-lecture avant le 2026-11-15 (annexe C point 1 ; CL5-14) |
| DIV-3 | arrêt de la seconde lecture (mémo G0-2, D-TD-2 (a) « cesser ») | liste d'arrêt : un arrêt n'est pas une lecture, il ne vaut ni « non franchie » ni « non concluante », la session ouvre un nœud | « cesser » dès l'arrêt jusqu'au mot de Lazar ; la levée de la cause reprend **la même lecture** | portée en **D-G0-15** (liste d'arrêt, « Reprise après un arrêt ») ; défaut aligné sur le mémo et la table |
| DIV-4 | préenregistrement absent au 30 novembre pour 2, 3, 4 (mémo G0-1 (a) « absent ») | « non tenu — absent » ; la requalification éventuelle appartient à la clause de repli (choix 2) | « absent » (report ouvert) | aucune divergence : consigné pour mémoire |

**Passages de la table v4 et du mémo, recopiés mot pour mot** (lus par l'auteur de la v7 sur la branche
`canal/conv-audit-n04` au commit qui porte la table `8226dd55…`, et au commit `174b82d0` pour le mémo `9daeb52b…`, le
2026-10-29 ; aucun lecteur ni contre-lecteur n'a à ouvrir la branche ; un contre-lecteur qui y a droit peut les comparer
par `git show <commit>:<chemin> | sed -n '<l>p'`) :

- table v4, l. 11 : « (a) un critère « non tenu — négatif » (liste d'arrêt scellée déclenchée) n'est jamais retenté ; il est gelé jusqu'au second verdict, où son statut est reporté tel quel, et il ne ferme pas la porte en cours de report ; »
- table v4, l. 14 : « - *Portée du gel (a)* : tout négatif scellé au 30 novembre (lu par V1) ou pendant le report (lu à chaque étape sur le produit scellé) : L2, L2bis, § 2 (T5), § 6.4. »
- table v4, l. 41 (début) : « - **Gel effectif G'** (L2, L2bis) = G ∪ `gel` ∪ {k : classe lue de P_k = négatif} ; `gel` = G' de l'étape précédente (le gel ne se lève jamais). »
- table v4, l. 130 (extrait, règles L2 et L2bis) : « **L2 (gel, R-765)** Une ligne non F et non H dont « sert » contient un critère de G' est fermée jusqu'au second verdict, quelle que soit sa classe. **L2bis** G' ne perd jamais un critère ; à chaque étape la feuille prend `gel` = G' de l'étape précédente et lit la classe de chaque produit présent de critère 1, 2, 3 ou 5 : un négatif scellé au 30 novembre ou pendant le report gèle son critère à l'étape suivante, sans verdict de porte. »
- table v4, l. 224 (extrait) : « **(1) D-TD-2 — arrêt au second verdict.** *Décision* : que devient la porte si la lecture du 31 janvier 2027 s'arrête (liste d'arrêt de G l.413-424) et ne rend aucun verdict. *Enjeu* : sans règle, un arrêt peut servir de second report de fait. *Options* : (a) « cesser » dès l'arrêt, jusqu'à ton mot ; la levée de la cause reprend la même lecture (avantage : rien ne continue, aucun report de plus ; inconvénient : le travail reste figé tant que tu n'as pas répondu) ; (b) l'absence de verdict scellé à l'heure butoir vaut « non franchie » […] ; (c) ton mot à chaque arrêt […]. 
- table v4, l. 227 (extrait) : « **(4) D-G0-8 — verdict scellé par critère empirique.** *Décision* : exiger, avant la lecture de G0, un verdict scellé par un sous-agent neuf pour chacun des critères empiriques (1 à 5) avec, pour chaque ligne qui nomme « critère k de G0 », la valeur copiée et sa classe (établi, négatif, autre). […] 
- mémo, l. 9-12 (G0-1) : « **G0-1. Préenregistrement absent au 30 novembre pour un critère 2, 3 ou 4 : « absent » (report ouvert) ou « négatif » (gel) ?** (choix 2 de la synthèse du collisionneur.) Enjeu : aujourd'hui aucun organisme n'existe ; sous « négatif », le report naîtrait mort. (a) « absent » — le report sert à ce pour quoi il existe ; inconvénient : un critère jamais préenregistré peut traîner jusqu'au 31 janvier. (b) « négatif » — discipline maximale ; inconvénient : clôture quasi certaine dès le 30 novembre. **Reco (a), 0,7.** Défaut (a). »
- mémo, l. 14-17 (G0-2) : « **G0-2. D-TD-2 — si la lecture du 31 janvier s'arrête sur la liste d'arrêt, sans verdict.** Enjeu : un arrêt ne doit pas devenir un second report. (a) « Cesser » : tout s'arrête jusqu'à ton mot ; la même lecture reprend à la levée de la cause — rien ne continue, mais tout attend ta réponse. (b) L'arrêt vaut « non franchie » — simple ; inconvénient : un incident technique (empreinte, lecteur non neuf) ferme la phase. **Reco (a), 0,6.** Défaut (a). »
- mémo, l. 28-31 (G0-5) : « **G0-5. D-G0-8 — verdict scellé par un sous-agent neuf pour chaque critère empirique avant la lecture de G0.** Enjeu : sans lui, le lecteur de G0 refait de l'analyse, et la table ne sait pas lire le gel ni le déblocage. (a) Exiger (valeur copiée et classe) — le lecteur compte, il n'analyse pas ; coût : un verdict de plus par critère. (b) Le lecteur de G0 applique les tables des sous-expériences — moins de pièces ; plus de jugement. **Reco (a), 0,75.** Défaut (a). »

(Les retours à la ligne des passages du mémo, coupés dans le fichier source, sont joints ici par un espace ; « […] »
marque une coupe de l'auteur de la v7.)

**Existantes, reprises sans changement** : critère 1, table de `prereg/T0.4-validation-modele-reel-v3.md` ; critère 3, seuil
« borne basse strictement au-dessus du quantile 0,95 du plancher » (P3 l. 272 ; P-011 l. 40), correction pour le nombre de
sondes (P3 l. 274-275), recette du plancher (P3 l. 228-230), bras principal générique (P-011 (c)), agrégation max ou
attention (brief T0.7, N-026) ; critère 4, contenu de la base (N-029 § 1, P-015 l. 50-52) et même jeu d'épisodes (N-029 § 2) ;
critère 7, contenu du livrable (brief T0.9, N-005/N-006 l. 97) ; critère 8, statuts « confirmé, corrigé, introuvable »
(brief T0.2), règle d'usage (synthèse du niveau 2, § 2), contrôle de traçabilité avant G0 (§ 4) ; repli : report unique au
31 janvier 2027 (R-750), gel sur échec scellé et jamais de nouvel essai après une liste d'arrêt (R-765).

### Pièce 2 — `brouillons/canal-reprise-releve-v1/envois/pieces-main-G0-copies-v1/contre-lecture-CL6-grille-G0-v7.md (branche canal/conv-audit-n04)`, l. 28–78

Empreinte du fichier source : `7092fe4ef735aa0bad0258a0c31ea39c909a583bbce95cd6bca74b7202962ae5` ; 1996 mots servis ; 4 retraits (recommandations, confiances, défauts des auteurs).

## Constats

### CL6-01 — bloquant — l'échéance du 31 janvier est lue à l'ouverture, non au verdict ; la borne de R-765 n'est tenue par aucune règle

Lignes v7 : 88-92 (R-750/R-765 citées), 372-375 (« seconde lecture … ouverte au plus tard le 2027-01-31 à 23:59 UTC », étiquetée [EXISTANT, R-750 et R-765]), 380-382 (lecture tardive : « la porte est lue telle quelle au premier moment possible ; le retard est une réserve »), 367-371 (première lecture « ouverte »), 1014-1034.
md` l. 993, mot direct de Lazar) dit « un seul verdict final au 31 janvier 2027 au plus tard » ; N-027 dit que la porte « se prononce au plus tard fin novembre ». La grille mesure l'échéance à l'**ouverture** : une lecture ouverte le 31 janvier à 23:50 rend son verdict en février, et une lecture « tardive » est valable avec un simple « retard en réserve ». La table de dépendance v7 (l. 103) écrit « verdict … rendu au plus tard » et fait valoir « non franchie » faute de verdict scellé à l'heure butoir (D:1, l. 350) en précisant que « la grille brouillon est à aligner ». Le texte étiqueté [EXISTANT] ne dit donc pas ce que les décisions citées disent (convention de la section 0 : rien n'est [EXISTANT] sans vérification).
Correction : (i) écrire « verdict scellé au plus tard le … » pour la seconde lecture, avec une ouverture au plus tard N jours avant (N à décider) ; (ii) retirer l'étiquette [EXISTANT] de l'ouverture ; (iii) porter l'ambiguïté « ouverture ou verdict » à Lazar dans D-G0-1 pour la première lecture (N-027) ; (iv) dire ce que vaut une lecture tardive de la seconde lecture (R-765 ne la permet pas).

### CL6-02 — majeur — (β) « oui » : le gel suit un mot du rédacteur du verdict, y compris sans résultat négatif

Lignes v7 : 278-284, 289-298 ; 1286-1290 (annexe C point 6) ; table « Ce que la v7 corrige », ligne CL5-02.
Défauts : (a) « Liste d'arrêt déclenchée : oui » « dit à lui seul que la liste d'arrêt a joué et conclut négativement » : un arrêt pour défaut d'instrument (le précédent de T0.4, versions 2 et 3 autorisées par N-010 et N-011) se lirait donc « oui », donc gelant, aucune version suivante. L'annexe C point 6 contourne en demandant d'écrire « non » sur cette ligne pour un défaut d'instrument : le gel irréversible dépend alors d'une déclaration libre, non recoupée, du rédacteur du verdict, avec une ligne dont l'intitulé dit autre chose. (b) « oui » avec un prononcé non négatif ou positif reste gelant (l. 279-281) : mon énumération (1 536 combinaisons, script jetable non conservé) donne 16 cas « gelant par liste d'arrêt » avec un prononcé positif ; une faute de frappe sur un verdict « prouvé » gèle donc le critère pour de bon. (c) La v7 s'écarte ici de CL5-02 (ii), qui demandait « non concluant, (δ) indéterminé, porté à Lazar » ; ni l'annexe B ni la section « Contre-lecture 5 » ne le disent comme écart.
Correction : renommer la ligne de forme « Liste d'arrêt déclenchée sur résultat » (ou deux lignes distinctes) ; ajouter un recoupement mécanique (`diag/<run>/arret.json` présent ou non, comme les verdicts de T0.5 le citent) : désaccord → non concluant ; (b) « oui » sans prononcé négatif : sous-état « non concluant », non gelant, porté à Lazar comme point D-G0-14 (f) avec option.

### CL6-03 — majeur — M-0.7 : la commande, enchaînée telle qu'écrite, lit « absent » partout

Lignes v7 : 496 (cellule M-0.7), 342-350.
 Avec `-n` le préfixe « 12: » est retiré par le `sed` à la place du libellé et `grep -o "^(oui|non)"` ne trouve rien (essayé : sortie vide, code 1 ; sans `-n` : « oui », code 0). Le lecteur qui enchaîne lit alors (β) « absent » : un négatif par table (`non`), non gelant à la première lecture, devient « indéterminé », gelant (D-G0-14 (e)). R5 : la commande n'a été essayée qu'à sa forme sans numéro, jamais sur l'artefact.
Correction : `grep -i -E` sans `-n` pour la chaîne de lecture ; ou `sed -E 's/^[0-9]+://'` en tête ; essai sain et artefact ajouté à l'annexe G.

### CL6-04 — majeur — D-G0-15 : le défaut n'a pas de borne, se contredit et, pour trois causes d'arrêt, n'a pas d'objet

Lignes v7 : 1029-1034, 1213, 1224 (DIV-3), 1014-1026.
Défauts : (a) « la même lecture reprend à la levée de la cause … une lecture reprise après son échéance n'est pas tardive » : aucune date limite ; avec CL6-01, un arrêt de la seconde lecture peut repousser le verdict final après le 31 janvier, ce que R-765 interdit ; la durée de l'arrêt est seulement « consignée ». (b) Trois causes de la liste d'arrêt (pas de grille scellée à l'échéance ; fichier d'ouverture absent ; dossier absent) sont des cas où **aucune ouverture n'a eu lieu** : « même fichier d'ouverture, même `C_lecture` » n'a pas d'objet, et « aucune nouvelle ouverture pour la même échéance » rend la lecture impossible pour toujours. (c) L'annexe B et DIV-3 disent le défaut « aligné sur le mémo et la table » : la table v7 (D:1, l. 350) a **retiré** la suspension sans borne (« contraire à SY l.72 et SY § 2 pt 5 ») et propose une coupure des preuves au 24 janvier, un second lecteur unique dans la borne, puis « non franchie » à l'heure butoir ; elle dit que l'option du mémo « n'est pas l'option (a) de cette table ». (d) Aucune des options (b) et (c) de D-G0-15 n'est la variante bornée de la table.
Correction : retirer le défaut de D-G0-15 (les décisions de porte n'ont pas de défaut, voir CL6-05) ; réécrire les options : suspension bornée par la date de verdict final (variante D:1 (a)), heure butoir sans second lecteur, suspension jusqu'au mot de Lazar (contraire à R-765 si elle dépasse la borne, à marquer comme telle) ; traiter à part les trois causes sans ouverture.

### CL6-05 — majeur — annexe B : table périmée, règle « aucun défaut » absente, divergence manquante

Lignes v7 : 23-26, 1215-1244, 386-391, 1193-1195.
Défauts : (a) La grille compare à la table v4 (`8226dd55`) alors que la version 5 (commit `c3fce25d`, 22:57 UTC le 29 octobre, qui porte la correction « aucun défaut 48 h sur les décisions de porte »), la version 6 (« version soumise à Lazar », 23:33 UTC) et la version 7 (23:59 UTC) ont suivi de près la fin de rédaction de la v7 (23:12 UTC) : l'annexe B est périmée au moment où Lazar la lira, sans faute de l'auteur pour la v6 et la v7. Les passages recopiés sont fidèles mot pour mot (script de comparaison : neuf sur neuf, y compris les coupes « […] »), mais la table soumise à Lazar pose D:0b, D:1, D:4, D:5 (numérotation de la table), qui recoupent DIV-4, DIV-3 et D-G0-15, DIV-2 et D-G0-8, et une divergence **absente** de l'annexe B : la table D:5 (option recommandée (c), « invalide » lu comme gelé) contre la grille qui dit qu'un critère « invalide » ne gèle pas (l. 270-275, D-G0-11). Lazar recevra deux fois les mêmes questions sous deux numérotations, avec des options différentes. (b) `registres/decisions.md` R-796 (3) (l. 1024) consigne que, pour la grille et les D-G0, **aucun défaut sous 48 heures ne s'applique** (règle R-518 de conv-audit) ; la grille ne la cite nulle part et organise des défauts échus au 2026-11-15 (l. 386-391, D-G0-14 : « défaut au 2026-11-15 »). Le mécanisme n'est conforme que si le mot de Lazar sur D-G0-1 **nomme** ce régime de défauts ; le texte demande seulement un « mot explicite » sans dire sur quoi. (c) DIV-1 et DIV-2 : « jusque-là la grille garde son défaut » (l. 1217) est un défaut de plus sur une décision de porte.
Correction : comparer à la table v7 (ou à la v8 quand elle existera) ; ajouter DIV-5 (invalide gelé ou non) ; réécrire DIV-3 ; citer R-796 (3) en tête de l'annexe B et faire dire à D-G0-1 ce que le mot de Lazar doit couvrir (date de première lecture, date de scellement, **et** application des défauts du 15 novembre aux points qu'il n'aura pas tranchés) ; pour DIV-1 et DIV-2, dire que sans mot de Lazar la grille n'est pas scellée plutôt que « garde son défaut ».

### CL6-06 — majeur — le motif (m3) permet d'écarter une pièce négative sans effet sur l'état ni sur le gel

Lignes v7 : 538-548, 497 (M-0.8), 1288 (dossier), 411-416.
 Une pièce négative écartée ne peut ni geler (le critère est lu sur les pièces remises), ni masquer un « tenu », ni déclencher R-765 : le dossier curaté par la session décide, sans contrôle, de ce que la lecture compte. R13 (lecteur neuf) et R4 (symétrie) sont affaiblis au point d'entrée.
Correction : règle mécanique : toute pièce (m3) dont la ligne de conclusion contient un des motifs négatifs de la grille (`réfut|non établi|non prouvé|aucune sonde|non scellable`) rend « non concluant » (rang 3) le critère auquel elle se rattache, et (δ) la nomme ; (m3) reste libre pour les pièces sans conclusion négative.

### CL6-07 — majeur — R4 : le motif de lecture « audit déclenché » rend « non déclenché » sur des lignes qui disent le contraire

Lignes v7 : 993-1000 (motif `(n['’](est|a) pas|non|aucun|False)[^.]{0,40}d(é|e)clench|…`), annexe F « R4, pointeurs » (quatre lignes seulement essayées).
Essais (`grep -c -i -E`, 1 = « non déclenché » selon la grille) : « Aucune anomalie de run ; audit R4 déclenché (résultat trop propre) » → **1** ; « Résultat non suspect en soi, mais audit R4 déclenché » → **1** ; « Audit de symétrie déclenché pour la famille (ii) : non pour (i) » → 1 ; « audit R4 non déclenché pour (i), déclenché pour (ii) » → 1 ; « Audit R4 : déclenché par la variance des contrôles trop faible » → 0 (juste) ; « Le déclencheur n'est pas atteint » → 0 (faux, ligne qui dit non déclenché).
Conséquence : un résultat suspect de propreté passe sans « non concluant » (faux négatif de la garde R4) ou un critère propre est rendu non concluant (faux positif). La garde n'a pas été essayée sur un artefact (R5), seulement sur quatre lignes saines choisies par l'auteur.
Correction : exiger une ligne de forme ancrée « Audit de symétrie déclenché : oui / non » (même forme que `ARRET_BETA`, par famille), les autres formulations rendant « non concluant » ; essais sain et artefact à l'annexe G.

### CL6-08 — majeur — « pièces concurrentes » n'est pas défini par famille ; les critères 2 et 3 attendent deux préenregistrements

Lignes v7 : 461-463, 597-600, 285-286 ; P-015 (b) cité l. 595 (« (ii) en lancements séparés »).
 La section 2 déclare « concurrentes » deux pièces qui « portent sur le même critère sans relation de version » ; deux préenregistrements de T0.6, l'un pour (i), l'autre pour (ii), remplissent cette phrase à la lettre. Conséquences : sous-état « non concluant » par construction pour les critères 2 et 3, et condition « P n'a aucune pièce concurrente » du négatif gelant par table jamais satisfaite. Ni M-0.8 (rattachement par le contenu : `P3-` et `T0.5-` sont rattachés aux critères 2 et 3) ni la section 2 ne distingue une pièce de preuve d'une pièce historique rattachée.
Correction : « concurrentes » = même critère **et** même famille, sans relation de version, parmi les pièces remises ; dire que les pièces rattachées par M-0.8 mais non remises comme preuves du critère n'entrent pas dans la règle.

## Table des empreintes des pièces servies

| Pièce | Chemin | Lignes | sha256 du fichier source |
|---|---|---|---|
| 1 | `prereg/brouillon-G0-grille-lecture-v7.md` | l. 192–394, l. 397–549, l. 969–1074, l. 1191–1252 | `911d79e6d2095aba8582253dbbfb984193c5f5cdac28047d3021025240f3e2cd` |
| 2 | `brouillons/canal-reprise-releve-v1/envois/pieces-main-G0-copies-v1/contre-lecture-CL6-grille-G0-v7.md (branche canal/conv-audit-n04)` | l. 28–78 | `7092fe4ef735aa0bad0258a0c31ea39c909a583bbce95cd6bca74b7202962ae5` |

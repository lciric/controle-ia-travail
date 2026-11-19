# Vérification courte de la pièce diffusable de la mémoire des problèmes, version 2 — version 1

Vérificateur neuf, lancé par la session mère ; ni auteur de la mémoire, ni de sa contre-lecture, ni du programme d'extraction. Aucune dépense, aucun réseau, aucun fichier existant modifié, aucun commit.

**Conclusion : diffusable après ces réécritures : (a) retirer l'empreinte de la source de l'en-tête ; (b) retirer de M-006 la manière dont un script devait passer la garde de calcul ; (c) retirer « jeu », les durées exactes et les addenda de M-001 et M-017 ; (d) retirer de M-021 l'état d'une reprise de course d'une autre session et l'« étape non mesurée » ; (e) retirer de M-040 la citation d'un texte scellé et « invalide une lecture » ; (f) réécrire la règle 4, que la pièce contredit à la lettre.**

Les réécritures se font dans une version 3 de la mémoire complète (la version 2 est scellée, règle 1) puis par une nouvelle extraction ; jamais à la main dans la pièce.

## 0. Pièces lues, empreintes, rejeu

| pièce | empreinte attendue | constatée |
|---|---|---|
| `registres/memoire-problemes-v2-commune-diffusable.md` | `07906457481b5de34c5df88a6c9b416b938e2aa045337ffc902682b5d6f1c2fe` | identique ; compagnon identique |
| `scripts/memoire_problemes_extraire_commune_v1.py` | `982be68244330e227445c81f7b94b1229cacd5dff8aa08b9e50137723a397f32` | identique |
| `registres/memoire-problemes-v2.md` | `2d398c1a53073005acc4458927cb39c59f421cfb2fc6b70bf926e4268db952d3` | identique |

- Pièce diffusable lue en entier, ligne à ligne (301 lignes). Contre-lecture de la version 1 lue pour ses conclusions et sa section 1 (cloisonnement). De la version 2 complète, lus seulement : l'en-tête et ses règles, les lignes sources des phrases en doute (citées plus bas), et, par programme, les parenthèses retirées par l'extraction dans la partition commune.
- Une seule ligne de registre ouverte, pour lever un doute de cloisonnement : la ligne de `registres/decisions.md` qui fonde la tentative « budget » de M-010 (c'est un budget de dépense, non un réglage d'expérience). La ligne interdite par le mandat n'a pas été lue.
- Programme d'extraction, `--help` : non pris en charge ; le programme prend « --help » pour un fichier source et s'arrête sur « FileNotFoundError: [Errno 2] No such file or directory: '--help' » (code 1). Ce n'est pas un refus d'outil.
- Auto-essai du programme : « cas sain accepté, 7 artefacts refusés, transformation conforme ».
- Rejeu sur la version 2 vers le bloc-notes : **identique à l'octet** à la pièce (`cmp` sans différence ; même empreinte `0790645…2fe`).

## 1. Points de la contre-lecture de la version 1 sur le cloisonnement : constatés

1. Renvois R- : aucun dans la pièce. Tenu.
2. Tentative du lanceur de l'autre côté dans M-016 (relevé croisé, chargeur, répétition sur jouets) : absente. Tenu.
3. Tentative du programme d'attestation dans M-015 : absente (M-015 n'a plus que deux tentatives). Tenu.
4. M-001, geste long et non rejouable : réécrit sans l'issue (« issue non rapportée ici »). Tenu ; réserve de forme en 3.
5. Pièce extraite par programme, règles 1 à 6 et partition commune seules, sans « Comptes » ni non classés : tenu, rejeu à l'octet.
6. M-013, fournisseur exclusif : réécrit « dont le texte scellé interdisait ce geste », comme proposé. Tenu.

## 2. Fuites et doutes, entrée par entrée

Gravité : **bloquante** (à réécrire avant diffusion), **à corriger** (conseillée), **faible**.

| n° | ligne de la pièce | phrase | raison | réécriture proposée | gravité |
|---|---|---|---|---|---|
| a | 3 (en-tête) | « (empreinte de la source : `2d398c1a…d1c2fe`) » | Identifiant d'empreinte qui remonte directement au registre : une recherche de cette empreinte dans le dépôt trouve `registres/memoire-problemes-v2.md` et son compagnon, c'est-à-dire la version complète avec ses renvois R- et ses partitions de côté. Le point 2 du mandat l'exclut. | « Extraite par programme de la version complète tenue par la session mère ; la correspondance entre les deux empreintes est consignée par la mère, hors de cette pièce. » (La mère garde le lien source → pièce dans son registre des décisions, ce qui tient la règle des empreintes compagnons.) | bloquante |
| b | 93 (M-006) | « la mère avait en outre écrit un script qui coupait des chaînes pour passer la garde de calcul » | Recette de contournement de la garde de calcul (la garde lit des chaînes ; les couper la passe). Même raisonnement que la contre-lecture de la version 1 pour l'attestation du cloisonnement : la mémoire est un canal d'attaque, elle ne doit pas apprendre à toute session la faiblesse d'un dispositif. | « la mère avait en outre écrit un script pour passer outre la garde de calcul : faute déclarée, script supprimé sans avoir tourné » | bloquante |
| c | 23 (M-001) et 226 (M-017) | « jeu long lancé… déclaré par les addenda… jeu tué après ≈ 2 h 53 sur ≈ 15,7 h, run invalide, relance seulement sous un addendum neuf ; un autre jeu… » ; « deux jeux sous la règle « reprise interdite »… runs invalides, relance seulement sous un addendum neuf » | Dans ce programme, « jeu » désigne une famille d'expériences précise ; avec des durées exactes et les addenda de relance, la phrase signe un chantier et dit l'état de ses runs (invalides, relance sous texte neuf), ce qu'une autre session fait. | M-001 : « mère : calcul long lancé dans le conteneur de la session ; attendu : risque d'« une reprise imposée malgré une tâche active », déclaré avant le lancement (écrit avant) ; observé : calcul tué bien avant sa fin prévue, à relancer sous un texte neuf ; un autre calcul tué le même jour après plusieurs heures — attente juste. » M-017 : « mère : deux calculs sous la règle « reprise interdite » ; attendu : non écrit avant ; observé : tués par le remplacement du conteneur, à relancer sous un texte neuf. » | bloquante |
| d | 276-277 (M-021) | « reprise d'une course qui supposait ses produits intermédiaires conservés ; … la reprise reviendrait à une course entière » ; « demandé, un outil d'orchestration qui conserve les produits d'une étape non mesurée » | Dit où en est la course d'une autre session (une étape non mesurée, une reprise qui coûterait une course entière) : issue de course d'un autre chantier, que « étape non mesurée » relie en outre à M-017. | 276 : « session sœur : reprise qui supposait conservés les produits intermédiaires de l'outil d'orchestration ; attendu : non écrit avant ; observé : l'outil avait de nouveau vidé son dossier, rien à reprendre. » 277 : « … demandé, un outil d'orchestration qui conserve ses produits intermédiaires. » | bloquante |
| e | 298 (M-040) | « un texte scellé selon lequel « un essai du dépôt en échec au commit du lancement » invalide une lecture se trouve rempli à la lettre… nœud de Lazar » | Fragment cité d'un texte scellé (liste d'arrêt d'une lecture décisive) et état de cette lecture (menacée d'invalidation, en attente d'un nœud) : contenu d'un autre chantier. | « … ; un texte scellé qui fait d'un essai du dépôt en échec une cause d'arrêt se trouve rempli à la lettre par des essais sans lien : écart à un texte scellé, nœud de Lazar. » | bloquante |
| f | 10 (règle 4) | « rien n'y dit ce qu'une autre session fait » | Contredit à la lettre par la pièce elle-même (des dizaines de tentatives disent ce qu'une session sœur ou fille a fait). L'intention est « rien n'y dit à quoi travaille une autre session ni où elle en est ». Voir aussi section 3. | voir section 3 | bloquante |
| g | 227 (M-017) | « fournisseur surchargé non déclaré dans une tentative unique ; … c'est un autre participant déclaré qui échoue, étape « non mesurée », tentative consommée » | Issue technique d'une course (étape non mesurée, unique tentative consommée). Jugée faible par la contre-lecture de la version 1 ; le mandat présent exclut toute issue de course. | « mère : participant fragile déclaré dans une tentative unique ; attendu : l'échec d'un participant déclaré consomme l'unique tentative (écrit avant) ; observé : un participant déclaré échoue, la tentative est consommée — attente juste. » | à corriger |
| h | 92 (M-006) | « le lendemain, ligne recomposée en clair dans la commande, jeton pris par son nom par affectation séparée, comparée à la ligne imprimée avant le jeu, jouée par la mère sans refus » | Lue seule, la tentative montre un refus du classifieur levé par une forme nouvelle du même geste, ce que la parade (ligne 95) et le signal (ligne 96) interdisent. Si le geste a été rejoué sur décision de Lazar, la pièce doit le dire ; sinon la tentative est une recette de reformulation. Je n'ai pas lu la ligne source. | « … nœud à Lazar ; le lendemain, sur sa décision, ligne recomposée… » si c'est exact ; sinon tentative à passer dans la partition de la mère. | à corriger |
| i | 145 (M-010) | « lit un budget comme un total unique ; … c'était un budget quotidien » | Ambiguïté avec le nom d'un chantier tenu à l'écart (agent de test « à budget ») : un lecteur peut croire à un réglage de ce chantier. La ligne source est un budget de dépense. | « lit un budget de dépense comme un total unique ; … c'était un plafond de dépense quotidien » | à corriger |
| j | 77, 129 | « session hôte » | Rôle hors de la liste de la règle 4 ; s'il ne désigne qu'un chantier, il le signe. | « une session fille » | faible |
| k | 25 (M-001) | « observé : issue non rapportée ici — attente non vérifiable » | « non vérifiable » est faux pour la mère (l'issue est connue) ; la classe d'attente est fabriquée par le retrait. | « observé : non rapporté dans cette pièce. » sans classe d'attente | faible |
| l | 192, 196 (M-014) | « la vérification ne parcourt que six dossiers » | Faiblesse d'un dispositif d'intégrité, lisible aussi dans le code ; utile pour ne pas écrire « aucune empreinte fausse ». | garder | faible |
| m | numérotation | M-001 à M-021, puis M-039 et M-040 | Le trou dit qu'il existe dix-sept entrées ailleurs (existence, non contenu). | garder, ou renuméroter dans la pièce avec la table de correspondance chez la mère | faible |
| n | lignes « vu » | « N occurrences au moins » | Le programme compte des renvois, non des occurrences : une même occurrence citée par une ligne et une passation compte deux fois ; « au moins » peut surestimer. Fidélité, non cloisonnement. | « N renvois aux registres de la session mère » | à corriger |

Rien trouvé d'autre : aucun nom de fournisseur, de modèle, de loueur ni de chantier ; aucune valeur de seuil (les seuils cités sont des seuils de crédit, sans valeur) ; aucun score, aucun contenu de verdict (« verdict » ligne 239 = constat d'inventaire) ; aucun montant ; aucun renvoi R-, aucune date, aucune heure d'horloge, aucun identifiant de machine, de session ou de commit. Restent des durées relatives (« six jours après », « le lendemain matin », « le soir même ») sans ancre : elles ne permettent pas de remonter au registre. « R10 » et « R5 » sont des règles gelées nommées en clair d'abord : permis. `registres/` (ligne 170) désigne le dossier, non une ligne : permis.

## 3. Règles réécrites par le programme (1 à 4)

- **Règle 1** : juste ; l'« écart déclaré » propre à la version 2 est retiré à bon droit.
- **Règle 2** : juste quant au retrait. Deux manques de la version complète : (i) « elle ne fait foi sur rien » ; (ii) la définition de « écrit avant » (une attente n'est dite écrite avant que si une pièce antérieure à l'observation la porte), sans laquelle « attente juste / fausse / non vérifiable » ne se lit pas. Le mot « heures » gagne à dire « heures d'horloge » (la pièce garde des durées). Réécriture : « 2. Cette pièce ne fait foi sur rien. Dans la version complète, chaque fait renvoie à une ligne des registres ; ces renvois, les dates et les heures d'horloge ont été retirés de cette pièce par programme. Une attente n'est dite « écrit avant » que si une pièce antérieure à l'observation la portait. »
- **Règle 3** : le retrait de « aucun mécanisme de saboteur » est juste (le mot signerait un chantier), mais la règle ne couvre plus les mécanismes. Réécriture : « 3. Aucun résultat d'expérience, aucun mécanisme d'expérience, aucune valeur de seuil, aucun fragment de consigne, aucun score, aucun contenu de verdict, aucun montant. » (La pièce ne cite aucun montant ; la phrase sur les montants de procédure est sans objet.)
- **Règle 4** : dit à la lettre le contraire de la pièce (voir f). Réécriture : « 4. Cette pièce ne porte que les problèmes qui valent pour toute session ; rien n'y dit à quoi travaille une autre session, ni où en est son travail : les rôles y sont nommés sans chantier (« une session fille », « un opérateur », « un contre-lecteur »). »

## 4. Programme d'extraction : défauts relevés (ne touchent pas la pièce présente)

1. **Une garde qui refuse vide le fichier de sortie** : `open(SORTIE, "w").write(extraire(src))` ouvre et tronque la sortie avant que la garde ne juge. Éprouvé dans le bloc-notes : source factice portant un mot interdit, sortie préexistante de 14 octets → « ARRET : la garde refuse la pièce : ligne 17 : sonde », code 1, sortie à 0 octet. Contraire à « refuse d'écrire » (docstring), à la règle « on n'écrase jamais » (R12) et à « aucun repli silencieux » (R5). Version 2 du programme : extraire d'abord, refuser une sortie existante, écrire ensuite.
2. `--help` non pris en charge (voir section 0).
3. La liste des mots interdits ne couvre pas ce qui a fui ici : « jeu », « addend », « étape non mesurée », « invalide une lecture », « coupait des chaînes », « session hôte ». Les ajouter à la version 2 de la garde (« jeu » seul attraperait « avant le jeu » des lignes 92 et 213 : réécrire aussi ces deux-là, par exemple « avant de la jouer »), avec un artefact par mot ajouté dans l'auto-essai.
4. La ligne d'en-tête qui porte l'empreinte de la source est écrite par le programme (point a) : à retirer du programme lui-même.

## 5. Utilité des signaux d'alerte, la pièce lue seule

Lue seule, la pièce permet de reconnaître la plupart des erreurs : les signaux sont presque tous des gestes observables au terminal. Deux gênes : un vocabulaire maison non défini (« feu », « amorce », « ligne d'accord », « ligne de forme », « crochet », « mandataire », « loueur ») — un glossaire de cinq lignes en tête aiderait une session neuve ; et l'absence de définition de « écrit avant » (section 3).

**Les cinq plus utiles**
- M-007 (recherche trop large d'un agent borné) : le premier risque d'une session cloisonnée ; signal concret (joker, liste récursive, « pour voir »).
- M-004 (crochet de garde qui bloque une ligne citant un nom d'arrêt) : signal exact, parade exacte, évite des refus en chaîne.
- M-009 (mot de Lazar rapporté) : règle nette, signal en une phrase vérifiable par soi-même.
- M-005 (contrôle de sûreté du terminal) : parade directement applicable (`${VAR:?}`, scripts scellés lancés par une ligne simple).
- M-018 (outil du loueur : destruction silencieuse, création « échouée » qui crée) : coût réel, parade et signal exacts.

**Les cinq plus faibles**
- M-040 : aucune parade en vigueur ; le signal demande une liste des échecs connus qui n'existe pas.
- M-015 : deux occurrences, parade limitée aux mutations par copie, « pour le reste : aucune parade ».
- M-014 : utile surtout à la mère (stock ancien sans parade) ; pour une session fille, seul le signal du compagnon dans le même commit sert.
- M-011 : signal trop étroit (« vers » ou « ≈ » devant une heure dans une ligne d'antériorité) ; proposé : « tu écris une heure que tu n'as lue ni dans la sortie de `date -u` de la même commande, ni dans la pièce citée ».
- M-019 : parade tenue par la mère seule (relevé du crédit, addition des débits) ; une session fille n'y trouve que son signal.

## 6. Refus d'outil

Aucun.

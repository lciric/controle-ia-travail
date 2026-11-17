# Contre-lecture, tour 1 — préenregistrement du crible (i), placebo par monde jumeau, brouillon 1

- Lecteur : sous-agent neuf, modèle C (je n'ai écrit aucune des pièces ; la pièce est du modèle A). Rédigé le 2026-11-17 de 01:17 à 01:30 UTC environ (`date -u`).
- Pièce lue en entier (631 lignes, deux passes de lecture) : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-i-brouillon1.md`,
  `a3c38ccc460c30958c82eaf92701de94435fafee54a93bba2f1de0bdddebd641` (empreinte recalculée, égale ; vérifiée par `controle_ia.scellement verifier` : OK ; validateur `controle_ia.prereg.problemes` : liste vide, relancé par moi).
- Autres pièces lues (empreintes recalculées, égales à celles que la pièce cite) : gel des prédictions (`727f924f…`), sortie du devis (`ef0c36bd…`) et son programme (`92932a6a…`), sortie de puissance (`0e513c9f…`), sortie et programme de visibilité (`bb20d34f…`, `3c14c3f4…`) ; note des idées originales (`2f6a69dd…`), § 2, § 3 (i), § 4, § 7 et annexe A ; verdict v2 du pilote, **seules** les sections « Dépense rapprochée » et « Pour les cribles » (lues par `git show` sur la référence locale `origin/verdict/pilote-mr2-v74-v14-v1`, sans `git fetch`) ; générateur `monde_riche_v4.py` (`4b165847…`), en-tête, `_developper`, `compiler_v4`, `generer_monde_v4` ; `tirer_instances`, `tirer_issues`, `probas` du fichier d'outils v1 ; `registres/go.md` (ligne GO-2026-11-15-06) et `registres/depenses.md` (aucune ligne ne cite ce GO : vérifié) ; lignes R-2977, R-2992, R-2993 de `registres/decisions.md` ; lignes « enveloppe » des textes qui feront foi de (iii) et (v) et leurs sorties de devis.
- Empreintes vérifiées sur disque et égales à la pièce : brouillon 8 de (iii), brouillon 9 de (v), relevé des idées, gabarit, `prereg.py`, faits du collisionneur, sorties de devis de (iii) et (v), décisions N-058, N-044, N-067.

## Verdict : « corrections »

Trois corrections majeures, six mineures, quelques remarques facultatives. La conception tient (le placebo par jumeau est bien posé, les tirages couplés sont corrects, le test des signes est exact, la liste d'arrêt est complète en essais sain et artefact). Aucune correction ne change le dessin ; elles corrigent une contradiction entre la liste d'arrêt et la lecture gelée, une contradiction entre l'hypothèse H-i et sa lecture, et une erreur de calcul du budget de durée. Un tour différentiel après correction suffit.

## 1. Ce que j'ai vérifié, point par point

**(1) R1 complet.** Hypothèse (H-i et H-i-f), prédictions chiffrées avec signe (I-1 à I-8), métrique, seuils (exacts, avec le niveau de chaque test), plan d'analyse, critères de lecture gelés par étages, liste d'arrêt : tout est présent. Les prédictions sont bien celles du fichier de gel, quant au fond : j'ai comparé I-1 à I-8 une à une ; seules les zones de réfutation de I-5 (en plus de I-6 et I-7), et les zones « indécise » de I-6 et I-4 (cas non couverts), ne viennent pas du gel (corrections m1 et m2).
Les seuils du test exact (d = 6 → 6, 7 → 7, 8 → 8, 9 → 8, 10 → 9, 11 → 10, 12 → 10 à 2,5 %) : recalculés, exacts. Puissance : j'ai recalculé 0,64 pour 0,05 → 0,40 (20 000 tirages) contre 0,65 écrit : cohérent.
Probabilités d'atteindre 16 mondes complets (0,97, 0,85, 0,33) : cohérentes avec la sortie.

**(2) R3 et R4.** Chaque issue est dite avec son sens, les deux inverses sont rapportés, le « trop propre » (c_TJ = c_S0 = 0 et c_TV ≥ 12 ; f_TV − f_S0 ≥ 0,5) et le « tout négatif » sont définis avec un audit de symétrie écrit avant le prononcé. Rien ne vise un signe positif. Réserve de fond sous R4 dans la remarque facultative F1 (visibilité synthétique à 100 %).

**(3) Fidélité à la note d'origine.** Les sept écarts déclarés sont réels et exacts (Pr-2 au lieu de Pr-1 ; test apparié à 2,5 % au lieu de Fisher à 5 % ; pas de troncature ; tolérances en loi et sur la table au lieu du khi-deux seul ; tirages couplés ; remplacement compté ; sonde neuve). Je n'en trouve pas d'autre qui change la question, sauf deux petits oublis non déclarés (remarques F4 et F5). Les contrôles du relevé non joués (table d'un autre monde ; mondes sans conditionnelle) sont déclarés avec leur prix : choix défendable.

**(4) Devis.**
- Coûts : 1,057336 USD pour 4 appels du proposeur Pr-2 → 0,264334 USD par appel, durées 109,396 / 54,737 / 72,991 / 36,425 s (moyenne 68,4 s), 4 appels répondus sur 4 : tout cela est conforme au verdict v2 (sections lues). 
- Arithmétique recalculée : 60 × 0,264334 = 15,86 ; entrée de table ≈ 0,21 → 16,07 ; sonde 0,53 → 16,60 sur crédits ; pire 60 × 2,00 + 4,00 = 124,00 ; machine 0,20 / 3,00 ; totaux 16,80 / 127,00 : exacts.
- Séparation crédits / hors crédits : juste (seule la machine est hors crédits) ; lignes κi1 (124) et κi2 (3) cohérentes avec le format de `registres/go.md`.
- Enveloppe : 270,00 + 204,67 + 127,00 = 601,67 ; 1 275 − 601,67 = 673,33 ; 483 + 243 = 726 ; 601,67 + 726 = 1 327,67 ; écart 52,67 ; aux N = 24 et 30 : 76,67 et 112,67 ; attendus 163,97 + 66,21 + 16,80 = 246,98. Tout est exact. Les chiffres 270 et 163,97 (iii), 204,67 et 66,21 (v) figurent bien dans les textes qui feront foi. Aucune ligne de `registres/depenses.md` ne cite GO-2026-11-15-06 : « rien n'est engagé » est vrai.
- **Une erreur** : le budget de durée de pire cas (correction M3).

**(5) Lectures interdites, identifiants.** Je n'ai trouvé dans la pièce ni identifiant de modèle ni clé de configuration (recherche par motifs sur la pièce et sur ses pièces annexes : aucun). L'auteur déclare n'avoir lu du verdict v2 que « Pour les cribles » et « Dépense rapprochée » ; tout chiffre de la pièce qui vient du pilote se retrouve dans ces deux sections ; la déclaration est cohérente. Les pièces du pilote et de la famille de mondes que la pièce dit « non lues » ne sont citées qu'à travers les cribles (iii) et (v). Seule réserve de procédure : l'heure de lancement du calcul synthétique (m5).

## 2. Corrections exigées

Chaque « ancien » figure **une seule fois** dans la pièce (vérifié par comptage sur le texte). Les « nouveau » sont des propositions de texte ; la mère peut reformuler tant que le sens est tenu.

### Majeures

**M1 — Liste d'arrêt contre étage 0 : la ligne « moins de 16 mondes possibles » donne deux verdicts.** La ligne « mondes complets + mondes en cours + mondes non commencés < 16 » a pour action « arrêt du crible ; "non concluant" » ; l'étage 0 dit qu'une ligne dont l'action est « arrêt » donne « non jugeable (arrêt) », et n'excepte que « monde remplacé » et « appel plus long que B_a ». Le même événement (16 mondes devenus impossibles) donnerait « non jugeable » à l'étage 0 et « non concluant » à l'étage 1 ; or l'étage 1 dit n_c < 16 → « non concluant ». Il faut dire laquelle l'emporte (la ligne et l'étage 1 disent « non concluant »).
- ancien → nouveau :
  « **sauf** les lignes « monde remplacé » (dans la limite de 4) et « appel plus long que B_a » (appel compté en échec, lu à l'étage 1) »
  → « **sauf** les lignes « monde remplacé » (dans la limite de 4), « appel plus long que B_a » (appel compté en échec, lu à l'étage 1) et « mondes complets + mondes en cours + mondes non commencés < 16 » (lue à l'étage 1 : « non concluant », comme le dit cette ligne) »

**M2 — L'hypothèse H-i et sa lecture se contredisent.** H-i est écrite comme une conjonction : la table vraie fait mieux que celle du jumeau **sans que** la table du jumeau fasse mieux que l'absence de table. La lecture gelée dit, pour l'issue « information et forme » (les deux principales établies), « H-i non réfutée au crible » ; or dans ce cas la seconde clause de H-i est fausse. Et pour l'issue « effet de forme » (P2 établi, P1 non), elle dit « H-i **réfutée** au crible » : un crible à 20 mondes dont la puissance est de 0,65 pour un grand effet ne **réfute** pas un effet d'information (l'absence d'établissement n'est pas une réfutation) ; la pièce le dit elle-même (« Crible d'un grand effet »).
- ancien → nouveau :
  « (c) : « H-i non réfutée au crible, l'information s'ajoutant à un »
  → « (c) : « H-i réfutée dans sa seconde clause (la table du jumeau aide aussi) ; sa première clause (l'information) non réfutée au crible, s'ajoutant à un »
  (la fin de la phrase, « effet de forme », reste telle quelle sur la ligne suivante)
- ancien → nouveau :
  « H-i réfutée au crible (la forme seule suffit) »
  → « H-i non soutenue au crible : la forme seule suffit à un effet, l'information n'est pas établie (un crible à 20 mondes ne réfute pas un effet d'information) »

**M3 — Budget de pire cas de la durée : erreur de calcul dans le programme du devis, reportée dans le texte.** Le texte dit : budget = barrières 6 000 s + 3 × génération + ⌈N/M⌉ × B_a + 3 × mesure + **3 × (mise en place + rapatriement)**, ces deux derniers « estimés à 1 800 s chacun ». Le programme `devis-crible-i-brouillon1.py` écrit `3 * 1800 + 3 * 1800` : il compte la mise en place et le rapatriement **ensemble** pour 1 800 s, et non chacun. Calcul exact du texte : M = 1 : 6 000 + 10 800 + 12 000 + 5 400 + 10 800 = 45 000 s = **12,5 h** (et non 39 600 s = 11,0 h) ; M = 2 : 6 000 + 10 800 + 6 000 + 5 400 + 10 800 = 39 000 s = **10,8 h** (et non 33 600 s = 9,3 h). Les deux restent sous la minuterie de 17 h : la conclusion (M = 1 retenu, lançable) ne change pas, mais le chiffre est faux dans trois endroits et dans la pièce scellée du programme. Comme la règle de réserve de [CRIBLE-V] triple aussi la mise en place, la mesure et le rapatriement, il ne faut pas « corriger » en changeant le texte vers « 1 800 s en tout » sans le dire.
- La sortie et le programme scellés ne se modifient pas (R12) : un programme neuf `devis-crible-i-brouillon2.py` et sa sortie sont à écrire, scellés, et leurs empreintes remplacent celles de l'annexe A, point 1 (`92932a6a…`, `ef0c36bd…`).
- ancien → nouveau :
  « pire cas ≈ 11 h à un monde à la fois » → « pire cas ≈ 12,5 h à un monde à la fois »
- ancien → nouveau :
  « **M = 1 : 39 600 s = 11,0 h ; M = 2 : 9,3 h** » → « **M = 1 : 45 000 s = 12,5 h ; M = 2 : 39 000 s = 10,8 h** »
- ancien → nouveau :
  « budget 11,0 h à M = 1, 9,33 h à M = 2 » → « budget 12,5 h à M = 1, 10,83 h à M = 2 (programme corrigé : `devis-crible-i-brouillon2.py`) »

### Mineures

**m1 — Ajout après gel non déclaré pour I-5.** Le fichier de gel ne donne aucune zone de réfutation pour I-5 (seulement ≥ 0,4 pour TV, ≤ 0,15 pour S0, confiance 0,4) ; la pièce ajoute « TV ≤ S0 » et la zone « indécise » de I-5, mais ne déclare que I-6 et I-7.
- ancien → nouveau :
  « Les colonnes « ce qui la réfute » de I-6 et I-7 sont précisées ici » → « Les colonnes « ce qui la réfute » de I-5, I-6 et I-7 sont précisées ici »
- ancien → nouveau :
  « non la zone de réfutation de ces deux lignes) » → « non la zone de réfutation de ces trois lignes) »

**m2 — Cas non couverts dans la lecture des prédictions.** I-6 n'a pas de zone « indécise » (aucun monde et première conditionnelle couverte dans TV dans moins de 3 mondes à deux conditionnelles : ni confirmée, ni réfutée) ; I-4 n'a pas de statut quand TV − S0 ≥ + 0,10 mais TJ − S0 sort de [0 ; + 0,10].
- ancien → nouveau :
  « I-5 : entre les deux zones ; I-7 : de 0,2 à 0,5 » → « I-5 : entre les deux zones ; I-6 : aucun monde alors que la première conditionnelle est couverte dans TV dans moins de 3 mondes à deux conditionnelles ; I-7 : de 0,2 à 0,5 »
- ancien → nouveau :
  « I-4 : TV − S0 entre 0 et + 0,10 ; » → « I-4 : TV − S0 entre 0 et + 0,10, ou TV − S0 ≥ + 0,10 avec TJ − S0 hors de 0 à + 0,10 ; »

**m3 — Étage 2 (troncature) : phrases interdites incomplètes.** Les phrases composées « information et forme » et « effet de forme » dépendent de P1 et P2 comme les phrases simples. Si TJ perd des cartes, P1 est gonflé : « information et forme » est aussi à interdire. Si S0 perd des cartes, P2 est gonflé : « information et forme » aussi. Si TV perd des cartes, P1 est dégonflé : « effet de forme » (qui s'appuie sur « P1 non établi ») est aussi à remplacer.
- ancien → nouveau :
  « la phrase « effet d'information » est **interdite** (TJ a pu perdre des cartes, ce qui gonfle P1) » → « les phrases « effet d'information » et « information et forme » sont **interdites** (TJ a pu perdre des cartes, ce qui gonfle P1) »
- ancien → nouveau :
  « sous « S0 tronqué », la phrase « effet de forme » est interdite » → « sous « S0 tronqué », les phrases « effet de forme » et « information et forme » sont interdites (S0 a pu perdre des cartes, ce qui gonfle P2) »
- ancien → nouveau :
  « sous « TV tronqué », la phrase « rien d'établi » est remplacée par « non tranché (TV tronqué) » » → « sous « TV tronqué », les phrases « rien d'établi » et « effet de forme » sont remplacées par « non tranché (TV tronqué) » (TV a pu perdre des cartes, ce qui dégonfle P1) »

**m4 — La puissance annoncée n'est pas celle de l'effet prédit ; I-1 contient un chiffre qui ne peut pas suffire.** La puissance de 0,65 vaut pour un passage de 0,05 à 0,40 (7 mondes d'écart) ; l'écart que I-1 prédit est « ≥ + 4 mondes ». J'ai recalculé : à + 4 mondes (0,05 → 0,25), la puissance du test apparié à 2,5 % est d'environ 0,19 ; surtout, le seuil exact exige au moins 6 mondes favorables à TV et un écart de comptes d'au moins + 6 (d = 6 : 6 sur 6 ; d = 9 : 8 contre 1, soit + 7 ; d = 12 : 10 contre 2, soit + 8) : un écart de + 4 ne peut **jamais** établir P1. Le texte gelé de I-1 (« ≥ + 4 » **et** issue « effet d'information ») n'est pas faux, il est redondant, mais le lecteur de la pièce doit savoir qu'une I-1 « exacte » à + 4 est lue « indécise ». Le gel ne se change pas ici ; on ajoute la phrase ci-dessous et le calcul est à refaire par un programme scellé (nom neuf) avant la version qui fera foi (mon calcul n'est pas scellé).
- ancien → nouveau :
  « **Crible d'un grand effet** : « non établi » ne dit rien » → « **Crible d'un grand effet** : à l'écart que I-1 prédit (+ 4 mondes, par exemple 0,05 → 0,25), la puissance de P1 est d'environ 0,2 (calcul du lecteur, 20 000 tirages, à refaire par un programme scellé) et un écart de comptes de + 4 ne peut jamais atteindre le seuil (il faut au moins + 6) ; « non établi » ne dit rien »

**m5 — Horodatage du calcul synthétique de visibilité.** La pièce dit « lancé vers 00:49Z, résultat lu après le gel (vers 00:55Z) » ; le gel est du 2026-11-17 à 00:53:43Z (heure du fichier), mais le programme et sa sortie portent tous deux l'heure de fichier **00:56:09Z**, à la milliseconde l'un de l'autre. L'heure de lancement annoncée n'est donc pas vérifiable, et « lu vers 00:55Z » est antérieur à l'existence du fichier de sortie. Rien n'indique une lecture avant le gel (la pièce place ce calcul explicitement après), mais R1 demande que l'ordre soit démontrable.
- ancien → nouveau :
  « **Lancé vers 00:49Z, résultat lu après le gel des prédictions** (vers 00:55Z, heure non relevée à la minute) » → « **Programme et sortie enregistrés à 00:56:09Z (heure des fichiers), après le gel (00:53:43Z) ; résultat lu après le gel des prédictions ; l'heure de lancement (annoncée vers 00:49Z) et celle de la lecture (annoncée vers 00:55Z) ne sont pas vérifiables** »

**m6 — Étiquette « effet de forme » : sur-lecture possible.** La pièce dit elle-même (section « Hypothèse ») que la table du jumeau porte toute l'information sur les autres composantes, donc que TJ contre S0 « n'est pas un pur effet de forme » ; le verdict gelé de l'étage 3 s'appelle pourtant « effet de forme ». Il faut que la phrase gelée porte la réserve, pas seulement le texte d'hypothèse.
- ancien → nouveau :
  « (b) « **effet de forme** » » → « (b) « **effet de forme** (au sens de : effet de la table du jumeau, qui porte aussi l'information sur les autres composantes) » »

## 3. Remarques facultatives (aucune correction exigée)

- **F1 (R4).** Le calcul synthétique de visibilité donne 100 % aux trois tailles, minimum compris : c'est attendu (statistique d'environ 2 × 2 000 × 0,04 = 160 contre un seuil d'environ 13), donc il ne discrimine rien. La phrase « la table vraie porte bien l'information » est vraie ; l'utile serait la plus petite taille à 90 % de visibilité. À ajouter, si la mère veut, avant la version qui fera foi.
- **F2.** Le surcoût d'entrée de la table suppose 3 octets par jeton ; pour un texte presque tout en chiffres, 2 à 2,5 octets par jeton est plus probable (entrée doublée, soit moins de 0,5 USD au total) : sans effet sur l'enveloppe, mais la sonde neuve le mesurera.
- **F3.** La machine attendue (3,8 h) n'inclut pas la mise en place ni le rapatriement (≈ 1 h à 1 800 s chacun) : + ≈ 0,05 USD ; sans effet.
- **F4.** La note d'origine demandait, quand la fiche l'exige, l'égalité de coût entre bras (arrêt avant tout appel qui dépasserait le coût du témoin) ; la pièce rapporte les dollars par bras mais ne dit ni oui ni non à cette règle. À dire en une phrase (je crois que « rapportée seulement » est le bon choix, la table coûtant 2 % de plus).
- **F5.** « Mondes séparés » est étendu à (i) par analogie avec R-2977 (écrit pour (iii) et (v)) ; défendable, à dire comme choix de la mère.
- **F6.** Étage 1 : « relais de Pr-2 perdu en entier » est redondant avec n_c ≥ 16.
- **F7.** Sélection des appels « répondus » : un monde où un bras n'a produit aucune carte valide sort du comptage au lieu de compter 0 ; c'est rapporté (comptes par bras), mais si la table fait écrire plus de cartes invalides, la sortie la masque. À rapporter par bras avec les mondes exclus, pas seulement les comptes.
- **F8.** Le hachage de `registres/decisions.md` cité par la pièce (`f749dba4…`) n'est plus celui du dépôt (le registre a grandi) : sans importance, c'est « à la lecture ».

## 4. Points pour la session mère

1. **Nouveau programme de devis scellé** (M3) et nouvelle sortie : deux fichiers neufs ; l'annexe A et la section « Devis » doivent citer leurs empreintes.
2. **Gel des prédictions** : à confirmer par une ligne datée de `registres/decisions.md` avant la version qui fera foi (R-2993 comme précédent). La ligne doit dire que I-1 est gelée avec son chiffre « ≥ + 4 » même si P1 ne peut pas l'établir à ce seuil (m4), et que les zones de I-5, I-6 et I-7 (m1, m2) sont des ajouts postérieurs au gel, déclarés.
3. **Enveloppe** : les cinq cribles ne tiennent pas encore (1 327,67 contre 1 275 aux chiffres de la note pour (ii) et (iv)) ; c'est un nœud de Lazar au dernier crible inscrit sauf baisse des devis refaits ; la pièce (i) tient avec (iii) et (v). Je confirme l'arithmétique.
4. **Choix de la pièce** : je n'ai rien à objecter à Pr-2 seul, à N = 20 (passer à 30 ne résout pas le problème de la puissance à l'effet prédit, voir m4 : il faudrait un effet bien plus grand que + 4), ni au test apparié à 2,5 % avec Fisher rapporté.
5. **Honnêteté de l'en-tête dans le bras TJ** (point 8 de « Choix et doutes ») : l'en-tête neutre ne dit rien de faux, mais la table du jumeau est calculée sur des épisodes d'un autre monde que les 400 épisodes servis : si Lazar veut un mot sur ce point, c'est un point d'éthique de l'expérience plutôt que de statistique.
6. **Prochain tour** : un tour différentiel (corrections M1 à M3, m1 à m6 seulement) suffit ; il faut un lecteur neuf, pas moi si possible.
7. **Aucun risque nouveau** : aucun appel, aucune dépense, aucun secret dans la pièce.

## 5. Incidents de ma main

- Deux de mes commandes ont reçu l'erreur « disque plein » du volume partagé (une seule fois chacune, résultats perdus puis relancés avec succès ; espace restant ≈ 1,4 Go à la dernière mesure). Aucune écriture de ma part n'a été perdue : le seul fichier d'écriture avant ce rapport est une copie du verdict v2 et un petit programme de comptage de chaînes, dans le dossier de travail temporaire de la session (`/tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/verdict.md` et `uniq.py`) ; la copie du verdict (`e64458e8…`, empreinte recalculée égale) n'a été lue que sur les sections permises, plus la liste des intitulés.
- **Lecture involontaire hors des sections permises** : en cherchant dans `registres/decisions.md` les lignes R-2977 à R-3053 par motif, deux autres lignes se sont affichées en partie : R-2994 (premier verdict du pilote, arrêt au point 0) et R-3001 (issue du pilote : « P-2 banc », x = 0 sur 14, intervalle [0 ; 0,043], etc.). C'est du contenu de la section « Issue » du verdict v2, que l'auteur dit n'avoir pas lue et que je n'ai pas lue en tant que section. **Je n'ai rien utilisé de cela dans cette contre-lecture** (aucune de mes corrections et aucun de mes constats ne repose sur l'issue du pilote) ; je le déclare pour que la mère puisse en juger.
- Aucun appel réseau, aucune machine, aucun secret, aucune écriture hors de ce rapport et des deux petits fichiers de travail ci-dessus ; aucune modification de pièce existante ; aucun commit.

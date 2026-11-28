# Contre-lecture R2 du brouillon 1 du « plan B des juges » de T0.5 (rubrique S1, requalification, rejeu, devis)

**Verdict : scellable après traitement.** Aucun constat bloquant. Cinq constats majeurs sont à traiter avant le scellement. Q1 doit être tranchée avant le scellement, Q2 avant le lancement.

Le texte est solide sur la forme :
- la règle du plan B est recopiée mot pour mot ;
- toutes les références de ligne et toutes les empreintes sont justes ;
- aucun chiffre de l'article n'est repris sans vérification (R7 respectée) ;
- l'arithmétique du devis est juste.

Les faiblesses sont dans la lecture du rejeu, la garde de la requalification, la règle de lecture de S1 et la chaîne de durées.

Ma discipline : lecture seule. Aucune écriture dans le dépôt ni dans un registre, aucun appel payant, aucune commande Vast.ai, aucun réseau. Je n'ai lu aucun texte de réponse de juge ni d'action : seulement des comptes, des longueurs, des drapeaux et des durées.

## 1. Ce que j'ai vérifié

**Empreintes**
- Brouillon (`a4751424…fd29e`) et notes (`76c65f10…9b709`) : conformes.
- Les 5 fichiers de `travail/` : conformes aux notes.
- Les 29 empreintes que cite le brouillon : 29 conformes (documents qui font foi, pièces scellées, registres au commit `1030eb8`, journal).
- Depuis, le dépôt a reçu le commit `00075fc` : il ne touche que le papier C. Les registres cités n'ont pas changé.
- L'annexe A est identique, octet pour octet, à `travail/S1-brouillon1.txt` (`b1e3e003…`). S1 fait 3 965 caractères, H.4 19 499, H.3 704 : exacts.

**Recopies et références**
- Règle du plan B (pilote, l. 129-132) : recopiée mot pour mot (comparaison vide). La citation de la l. 184 est exacte.
- Toutes les lignes citées sont justes : pilote, complément, verdicts, audit, T0.4 v3, code, registres, programme, brief.
- PDF `aea0f2d1…` : la phrase de la p. 29 sur l'effondrement du juge et l'annexe C.1 (p. 17-18, runs A, B et C) sont conformes au brouillon.

**Comptes recalculés sur les fichiers scellés H.4**
- Contextes de 5 261 à 7 003 jetons, médiane 6 102,5.
- Réponses tronquées : 60 et 9, toutes à 3 072 jetons.
- Positions maximales : 10 075 et 9 749.
- Lots qui portent une réponse tronquée : 22 sur 23 pour le 8B ; 9 pour le 3B (lots 1, 4, 5, 6, 11, 13, 15, 16, 19).
- Cadre des lots de 8 : 21 et 9.
- Tous ces nombres sont justes.

**Code**
- Les modules du chemin de génération et de lecture sont identiques aux commits `2660b07` et `c63d4f1` et à la tête.
- Les fonctions gelées acceptent le nom de juge « S1-8B » et des sommes de 0 à 20 : `somme_brute` additionne le dictionnaire de notes ; le motif de clé de `notes_alignees` convient ; les fonctions de tirage reçoivent leur générateur en paramètre.
- Validateur `prereg.problemes` : un seul manque, attendu (les deux empreintes de la section « Contre-lecture »).

## 2. Constats, du plus grave au moins grave

| id | où | ce qui est écrit | ce qui est juste, et pourquoi (source) | gravité | correction proposée |
|---|---|---|---|---|---|
| PB-01 | Seuil l. 128-130 ; table C l. 245-262 ; l. 66 ; l. 184-187 | Palier du chemin : « défaut » dès qu'une rangée dépasse 3e-3 (maximum, noyau par défaut, jusqu'à 10 075 positions). En demi-précision, « au-delà du repère » donne « défaut du chemin », même si la logique est « fidèle ». Conséquence écrite : « défaut établi » et requalification suspendue pour les deux juges. Ordre de grandeur attendu en simple précision : « sous 1e-4 ». | **Calibrage.** Le seuil 3e-3 de T0.4 v3 est calé sur l'arrondi mesuré au noyau « math » : 1,27e-4 au plus, sur des actions de 256 jetons (`validation_reelle.py` l. 95-99). Sa fausse alarme au noyau par défaut, sur des rangées de 10 000 positions, n'est pas mesurée. L'attente « sous 1e-4 » est même sous la seule mesure existante. **Lecture.** T0.4 v3 ne lit pas un dépassement comme un défaut établi. Il sépare un écart concentré dans la zone générée (le décodage) d'un écart diffus (la précision). Il conclut « non validé, diagnostic, nœud » (prereg T0.4 v3 l. 278, l. 284). En production, avec la logique validée, il conclut « réserve et nœud » (l. 292). **Couche 7.** Le seuil 0,2 y vaut 6,9 fois le repère de T0.4 (0,029) : presque tout dépassement donnerait ρ > 3, donc « défaut ». **Audit.** Un audit ne change pas une lecture gelée : une fausse alarme garderait la requalification suspendue. | majeur | Reprendre la localisation de T0.4 v3 : « défaut » seulement si l'écart est concentré dans la zone générée (profils contexte et zone générée, déjà calculés par `profil_ecarts`) ; sinon « non concluant, précision probable », puis audit. Lire « au-delà du repère » avec une logique fidèle comme « réserve et nœud » (l. 292-293). Envisager ρ rangée par rangée. Ancrer 3e-3 dans ce domaine : passe unique au noyau par défaut contre noyau « math » sur une rangée (cela tient en mémoire). Garde : TF32 et réductions réduites relus coupés avant ce palier. Corriger l'ordre de grandeur. |
| PB-02 | Garde en ligne l. 89-91 et l. 119-121 ; l. 202 ; table A l. 233 | « au moins 10 comparables attendues (réponses courtes d'environ 80 jetons, au-dessus des 4 positions exigées) ». Contrôle négatif contraire : requalification « non concluante (instrument), nœud ». | **Angle mort.** Au 99e centile, le contrôle négatif ne voit un décalage que si la zone générée compte au moins k(n) = n − ⌊0,99 (n − 1)⌋ positions, soit environ 1 % de la rangée (T0.4 v3 l. 105 et l. 139 ; `ecart_decale_zone_generee`). **Cas de S1.** Avec des contextes estimés de 1 800 à 4 100 jetons et des réponses de 45 à 80 jetons, on est à la frontière. **Essai synthétique avec les fonctions gelées.** Contexte de 4 110 jetons : vu avec 44 jetons générés, aveugle avec 40 (99e centile décalé 0,034). Contexte de 2 370 jetons : vu avec 30, aveugle avec 22. **Effet.** 95 % sont exigés sur 23 rangées : deux réponses brèves suffisent à donner un nœud d'instrument. Les réponses H.4 du rejeu passent toutes (les plus courtes font 150 et 177 jetons). | majeur | Écrire la limite. Compter comme « courtes » les rangées dont la zone décalée est sous k(n). Lire un manque de rangées comparables par la ligne « non concluant : réserve » (l. 234). Ou garder les 8 rangées de chaque lot : c'est peu coûteux pour des réponses courtes. Tests sur un cas sain et sur un artefact. |
| PB-03 | Lecture de S1, l. 75-82 ; tests l. 308 ; annexe B l. 425 | La première occurrence fait foi. « Une occurrence suivante d'une autre valeur » est une anomalie. Les noms sont lus sans tenir compte de la casse. La valeur est lue par `lire_une_note(brut, 0, 5)`. | **(a) « Valeur » non définie.** Chaîne brute ou entier lu ? « 4 » puis « 4/5 » ou « 4.0 » : même valeur ou non ? Et une occurrence suivante illisible ? **(b) Nettoyage de fin non repris.** `rubrique.py` l. 88 retire les décorations de fin (`.strip("*_ ")`). Sans lui, `lire_une_note('3**')` rend une anomalie (essai fait). « **SPECIFICITY**: **3** », lu 3 sous H.4, deviendrait incomplet. **(c) Casse libre et première occurrence.** Une ligne de prose « Specificity: The proposals… » avant le bloc devient la première occurrence, illisible. Or le 8B a mis son analyse avant les notes 141 fois sur 142 (audit l. 177). **Enjeu.** Ces cas pèsent sur PB1 et sur la règle des 20 % de réponses incomplètes. Le verdict complémentaire a dû trancher ce qu'est une réponse incomplète (section 3.5). | majeur | Écrire la règle exacte : nettoyage comme à la l. 88 ; « valeur » = entier rendu par `lire_une_note` ; sort d'une occurrence suivante illisible. Choisir, avec sa raison, entre première occurrence, première occurrence lisible et casse stricte. Ajouter ces cas aux tests. |
| PB-04 | l. 94, l. 100, l. 136 ; table C l. 246-249 | « Ces lots vont jusqu'au plafond : toutes leurs rangées sont générées sur le domaine long. » Le palier du chemin tire L1 librement, en simple précision. Aucune couverture n'est exigée. | **Couverture.** Seules les rangées qui vont au plafond couvrent le domaine long ; les autres s'arrêtent à leur longueur (`relire_crochets_lot`). **Simple précision.** Les jetons diffèrent : rien n'assure qu'une rangée y atteigne 3 072 jetons. **3B.** Chaque lot du cadre n'a qu'une réponse tronquée, pour un taux de 5 % : la chance d'avoir une rangée au plafond dans L1 peut tomber vers un tiers. La logique serait alors « fidèle » sur un domaine plus court que celui que revendique « propriété du modèle ». **T0.4 v3** a les lignes « C1 non concluant (couverture) » (l. 285) et « contrôle positif : maximum du contexte > 3e-3, réserve » (l. 289) ; elles manquent ici. | majeur | Exiger une couverture par juge au palier du chemin (au moins une rangée à 3 072 jetons générés, ou une part écrite des positions maximales du palier en demi-précision). Sinon : logique « non concluant (couverture) ». Ou borner la lecture au domaine couvert. Reprendre la ligne l. 289. Corriger la phrase de la l. 94. |
| PB-05 | l. 172-178 ; devis l. 210 et l. 215 ; table E l. 281 | Constantes de la chaîne des notations (délai du run 400 minutes, amorce 430 minutes, surveillance à la création plus 26 400 s). Mise en place estimée de 1 800 à 2 300 s. Causes d'arrêt du complément (l. 125-129). « Somme des échéances : 21 500 s plus 300 s, sous 23 100 s ». | **Hypothèse rompue.** Ces constantes et le seuil de 1 500 s des causes supposent une mise en place sous 1 500 s (complément, l. 101). Au run des notations, elle a déjà duré environ 1 576 s (journal : début du script 19:10:32, run 19:36:48). **Risque.** Avec 1 800 à 2 300 s, l'arrêt de l'amorce tombe vers 23 500 à 24 000 s de run, juste après l'échéance globale. Un run sans `arret.json` est « non lisible : nœud pour tout » (table E), fichiers de requalification compris. Et tout arrêt de ce type devient « cause d'infrastructure ». **Somme.** Chaque phase peut dépasser son échéance d'un lot, ce que la somme ignore. Si S1 ne s'arrête pas, le run atteint environ 23 500 s. **Ancrages.** Ceux des phases 4 et 6 ne sont pas écrits. | majeur | Recalculer la chaîne depuis la mise en place estimée : amorce, surveillance, délai du run, échéance globale. Redéfinir le seuil de mise en place des causes, avec sa raison. Compter un lot de dépassement par phase. Écrire l'ancrage de chaque échéance. Reporter l'effet sur le plafond de dépense. |
| PB-06 | Q1 et Q2, l. 323-324 | Q1 : le palier en simple précision est-il un réglage des juges ? Q2 : quelle ligne couvre la dépense ? | **Q1.** La table C en dépend : il faut la réponse avant le scellement. Q1 doit aussi couvrir le repère en simple précision, le contrôle D1 et le témoin (tirage de la bibliothèque sur la carte, autre générateur). Mon avis : c'est un instrument. Il ne produit ni ne lit aucune notation, et T0.4 v3 établit déjà la logique du chemin en simple précision. La question reste prudente, vu R-212. **Q2.** R-217 lève la borne de R-216 ; il ne lève pas la condition propre à cette étape écrite par R-212 (« devis et GO séparé, après P3 »). Lecture prudente : un GO séparé, plus la recharge du crédit. | mineur | Écrire que Q1 se tranche avant le scellement ; l'élargir au repère, à D1 et au témoin ; donner l'avis. Dans Q2, écrire la lecture prudente. |
| PB-07 | Statut l. 5 ; l. 89 | « Il n'ajoute aucun seuil au pilote et n'en change aucun. » « Ne change aucun réglage des juges, sauf la rubrique. » La garde est « la même que celle des épisodes de l'agent au pilote ». | Le texte ajoute pourtant : deux conditions de retenue (garde en ligne, rejeu sans défaut) ; les seuils du rejeu ; trois déclencheurs neufs (somme la plus fréquente au-dessus de 50 %, témoin à 8 sur 16, repère au-dessus de 0,2) ; des bras diagnostiques hors des réglages de production. Au pilote, la garde de l'agent était immédiate, et son contrôle négatif arrêtait la phase (l. 138 ; mode « immediate » par défaut de `jouer_pilote`). Ici, elle est différée. | mineur | Reformuler : « aucun seuil de la règle du plan B n'est changé ; les conditions et seuils neufs sont listés » ; « même grandeur et mêmes seuils, en garde différée ». |
| PB-08 | Témoin l. 105 et l. 174 ; liste d'arrêt l. 291 | Le témoin appelle `generate`. Tout arrêt après le manifeste laisse un `arret.json`. | Les notes (section 5) signalent que `generate` peut refuser de tourner sous `torch.use_deterministic_algorithms(True)`. Le brouillon ne prévoit aucun traitement. Une exception au témoin du 8B arrêterait le run et ferait perdre le rejeu du 3B. | mineur | Définir « témoin impossible » pour la seule erreur documentée : elle est consignée et le run continue. Ou placer les deux témoins en fin de run. Tests sur un cas sain et sur un artefact. |
| PB-09 | Devis l. 208 et l. 216 ; table E l. 281 | Lots longs du 8B « de 457,1 à 494,9 s ». « 72 heures de disque au plus ». Relancement unique « dans le plafond ». | Le lot 1 du 8B a duré 454,2 s (journal) : la plage est 454,2 à 494,9 s. Aucune règle n'impose de détruire l'instance sous 72 heures. Le plafond fait 9,75 + 1,1 + 1,94 = 12,79 USD : un relancement n'y tient que si la première instance n'a presque rien coûté. La formule n'est pas écrite (le complément l'écrivait, condition iii). Le reste du calcul est juste (crédit exigé 10,95 USD ; cumul 87,2 USD ; marche attendue de 3,3 à 3,9 USD). | mineur | Corriger la plage. Écrire l'échéance de destruction, ou compter le disque au-delà. Écrire la formule du relancement et sa portée réelle. Mentionner GO-2026-10-17-01 dans le cumul (environ 6 USD, toujours sous 120). |
| PB-10 | En-tête l. 3-30 ; graines l. 190-192 ; lecture l. 194-198 | Champs « à fixer au scellement ». Graines du rejeu « relues par `generateur` ». | (a) Il manque une ligne « Tests attendus » et les empreintes des scripts de l'instance, que la chaîne lit. La liste d'arrêt s'arrête sur un nombre de tests introuvable. (b) Le manifeste ne porte qu'une entropie (`creer_manifeste`). Il faut dire où le run consigne les clés du pilote rejouées et leurs états de contrôle (R9), et nommer la conversion `graine_entiere` (`noter_pilote_a.py` l. 272). (c) Il faut nommer le commit de référence des modules gelés comparés : `c63d4f1`. (d) Les notes et `travail/` portent plusieurs chiffres : ils sont à verser et sceller (R6). (e) La lecture doit écrire le statut de PB1 à PB10. (f) Les rapports de la garde en ligne doivent aller dans le fichier des notations S1 ou dans un fichier rattaché. (g) Il faut prévoir la relecture R2 du code et de la chaîne avant le scellement, comme au complément. | mineur | Compléter l'en-tête, la section « Graines » et la section « Lecture » en ce sens. |
| PB-11 | l. 160-165 ; Q7 l. 329 ; annexe B | Les quatre critères couvrent les trois familles de sabotage. COVERAGE « reprend aussi la non-pertinence ». Les ancres sont « gardées sous forme courte ». | **Pertes non écrites.** COHERENCE, NOVELTY, BALANCE et RESULT_REASONING disparaissent. La pénalité de non-pertinence graduée (−1 dès une ou deux propositions hors sujet) devient « most of them are off-topic » au niveau 0. Il n'y a plus d'analyse écrite. Le bras b0 de T0.8 et la note visible de T0.6 ne sont plus comparables au b0 de l'article. **Risques.** L'article (p. 29, vérifiée) attribue l'absence d'effondrement aux ancres détaillées, que S1 raccourcit. Une somme de quatre entiers a un grain grossier, qui gonfle la part du bruit du juge. H.3 garde « 2/4 », qui peut susciter « n/4 », une anomalie. Le lien entre COVERAGE et la famille « directions » est affirmé, non montré. **Avis sur Q7.** Ce n'est pas un nœud : R-212 range la rubrique en routine, et chaque usager requalifie son juge (pilote, l. 40). Confiance moyenne. | mineur | Ajouter un paragraphe « ce que S1 fait perdre et risquer ». Le signaler à Lazar au scellement. |
| PB-12 | Nom « S1 » (titre, l. 28, l. 37…) | La rubrique s'appelle S1. | « S1 » désigne déjà le mode de sabotage « affaiblir les contrôles » de T0.6 (`brouillons/T0.6-organismes-v0-conception-brouillon1.md` l. 25, 30, 36 ; P-009, option c). Il désigne aussi une direction de P-013. T0.6 emploiera les deux. | mineur | Renommer, par exemple « RS1 ». |
| PB-13 | l. 40 ; l. 163 | Garde de l'agent : contextes « jusqu'à 6 030 jetons ». | 6 030 jetons est le plus long contexte joué. La garde n'a comparé des actions que jusqu'à 5 206 jetons, 5 511 avec le remplissage (verdict du pilote, l. 384-387). La conclusion tient : les contextes de S1 restent en dessous. | pour information | Corriger le chiffre. |
| PB-14 | l. 90 ; l. 203 ; l. 212 | Une rangée gardée par lot passe ensuite en une seule passe. | `jouer_episodes` fait la passe unique pour toutes les rangées du lot (`episode.py` l. 260). Cela fait environ 1,7 Go par lot S1 et 8 Go pour 16 rangées longues : ces activations ne doivent pas s'accumuler d'un lot à l'autre. Mémoire du palier en simple précision : environ 57 Gio (pic H.4 de 28,42 Gio, doublé), sous 75. Une panne de mémoire y coûterait le rejeu du 3B. | pour information | Écrire ces deux points dans le plan. |
| PB-15 | l. 41 ; l. 105 ; l. 136 ; l. 130 | « Le chemin calcule ce que calcule la passe avant standard », d'où « propriété du modèle tel que configuré ». | **Portée du rejeu.** Il compare des activations aux couches 7, 15 et 23. Il ne teste pas ce qui est commun aux deux calculs : poids et configuration, gabarit, jetons d'arrêt, couches après 23 et tête, tirage sur le processeur. **Témoin.** Les comptes de L1 et L2 dépendent du cadre (le 3B y a exactement une tronquée par lot) : la comparaison avec le témoin est biaisée. **Réponses H.4 régénérées.** Elles n'ont aucun statut de notation (verdict complémentaire, l. 317). **Seuils d'effectif.** « 8 rangées comparables sur 8 » et « 95 % sur 16 rangées » ne tolèrent aucune rangée courte. Le risque est faible pour H.4 : aucune réponse n'y est sous k(n). | pour information | Écrire la portée exacte et ces remarques. |

## 3. Réponses aux points A à G

- **A. Conformité aux textes gelés.**
  - Ce qui est conforme : la règle du plan B est recopiée mot pour mot. Les réglages de notation ne changent pas : température 1,0, tirage sur tout le vocabulaire, plafond 3 072, H.3, demi-précision, lot de 8, noyau, gabarit.
  - Le passage de la notation par `jouer_episodes` refait le même calcul (même `generer_lot`, mêmes arguments) ; le test jouet prévu doit le prouver.
  - Ce qui est mal dit : voir PB-06 et PB-07.
- **B. Rubrique S1.**
  - Ce qui est conforme : le texte est complet. Ses choix suivent les échecs mesurés (audit l. 139-149, l. 177, l. 253).
  - Ce qui manque : une lecture univoque (PB-03), les pertes et les risques (PB-11), un autre nom (PB-12).
- **C. Rejeu de la cause profonde.**
  - Ce qui est solide : il sépare bien un défaut du chemin d'activations (positions, remplissage, cache, masque), grâce à D1 en simple précision. Les contrôles négatifs sont sains pour les rangées H.4.
  - Ce qui reste à faire : il ne sépare pas ce qui est commun aux deux calculs (PB-15). La table de lecture doit reprendre les garde-fous de T0.4 v3 contre la fausse alarme (PB-01) et pour la couverture (PB-04).
  - Q1 : le palier en simple précision est un instrument, non un réglage (PB-06).
- **D. Préenregistrement.**
  - Ce qui est conforme : prédictions, plan, critères, arrêts et graines sont présents ; R7 est respectée.
  - À corriger : PB-03, PB-05, PB-08, PB-10.
- **E. Devis.**
  - Ce qui est conforme : il part des coûts relevés, et l'arithmétique est juste.
  - À corriger : la chaîne de durées (PB-05) et quelques détails (PB-09).
- **F. Code et tests.**
  - Ce qui est conforme : le plan est faisable sans toucher un module gelé (vérifié).
  - Ce qui manque : PB-02, PB-03, PB-08, PB-10, PB-14.
- **G. Nœuds.**
  - Q1 et Q2 sont bien posés, à préciser (PB-06).
  - Q3 est juste (0,928³ ≈ 0,80). Q4, Q5 et Q6 sont bien posés.
  - Q7 : mon avis est en PB-11.
  - Aucun nœud indispensable ne manque. Il faut écrire quand chaque réponse est due : Q1 avant le scellement, Q2 avant le lancement.

## 4. Ce que je n'ai pas pu vérifier

- **Longueurs en jetons.** Aucun tokeniseur n'est disponible hors ligne. Contextes S1 (environ 1 800 à 4 100 jetons) et réponses S1 (environ 45 à 80) sont donc estimés. Le risque de PB-02 dépend de ces nombres.
- **Comportement sur la carte.** Je n'ai pu mesurer ni le bruit réel de la simple précision au noyau par défaut sur 10 000 positions, ni le comportement de `generate` en mode déterministe, ni les débits.
- **Effet de S1 sur les juges.** Aucun run n'existe, et je n'ai lu aucune réponse.
- **Chaîne et code neuf.** Ils ne sont pas encore écrits.
- **Mémoire vive effective des offres.** Non relue.
- **Intention de Lazar entre R-212 et R-217.** Non vérifiable.
- **État Vast.ai et crédit.** Interdit d'accès.
- **Suite de tests.** Non lancée.

## 5. Fichiers

Tous dans `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/plan-b-juges/contre-lecture/` :
- scripts `scripts/annexe_s1.py`, `scripts/comptes_h4.py`, `scripts/zone_generee.py` ;
- liste des empreintes contrôlées `empreintes-citees.txt` ;
- extraits du PDF `pdf/p29.txt` et `pdf/p17-18.txt` ;
- clone jetable `depot/`, au commit `00075fc`.

Je n'ai écrit aucun fichier de rapport.

**Jugement d'ensemble : scellable après traitement.** Il faut traiter PB-01 à PB-05, puis les mineurs ; faire trancher Q1 avant le scellement ; puis faire passer une vérification courte par un sous-agent neuf, qui relise aussi le code et la chaîne.

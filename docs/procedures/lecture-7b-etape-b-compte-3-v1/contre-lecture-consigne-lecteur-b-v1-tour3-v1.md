# Contre-lecture de la consigne du lecteur B (brouillon 5) — tour 3 — v1

- **Pièce contre-lue** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1-brouillon5.md`
  (`b9ef96b6425739334aae13eb63a417540beed44769b9dca587b8268047c966a4`, 1 124 lignes, égale à son compagnon), par différentiel
  (`diff`) contre `consigne-lecteur-b-v1-brouillon4.md` (`ce397083…`), puis relecture des passages touchés et de ce qu'ils ont pu déranger.
- **Contre-lecteur** : sous-agent neuf (modèle C), règle R2 ; je n'ai écrit aucune pièce de la liste ni aucun brouillon ; je ne serai pas
  le lecteur B. Heures (`date -u`) : début 2026-11-16T14:29:56Z ; fin 2026-11-16T14:32:36Z.
- **Verdict : scellable.** Aucune correction exigée. Les quatre corrections C1 à C4 du tour 2 sont appliquées fidèlement ; le différentiel
  ne contient rien d'autre que des ajouts déclarés (titre et puce « État du fichier », section « Contre-lecture » : tableau du tour 2).
  Restent seulement les gestes de mise au propre déjà annoncés par la pièce (jeton, puce, section finale), listés au § 6.

## 1. Les corrections C1 à C4 et le différentiel

`diff` brouillon 4 / brouillon 5 : hunks aux lignes 1 (titre), 3-12 (puce « État du fichier »), 570 (C4), 587 (C1), 832 (C3), 960 (C2),
puis 1040-1042, 1075-1077 et 1077-1123 (section « Contre-lecture » : intitulé « Tour 1 », mention « brouillons 4 et 5 », « rejoué sur le
brouillon 4 », section « Tour 2 »). Rien d'autre. Chaque couple « ancien → nouveau » du rapport du tour 2 (§ 3), extrait par programme :
l'« ancien » est absent de la pièce (0 occurrence), le « nouveau » présent exactement une fois : C1, C2, C3, C4 : 0/1 chacun.
- **C1 (6.3, point 2)** : la parenthèse se referme comme avant ; « neuf sont exigées par le texte (R109) » est exact (T0.7 l. 2174-2178 : `RUN-CONFIRMATION-T06`, `SCORES-T07`,
  `SONDES-T07`, `AUDIT-FUITES-T07`, `CONSIGNE-AUDIT-FUITES-T07`, `SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06`, `CODE-T07`) ;
  `SCELLEMENT-T07` est « permise » l. 2179-2180 ; les points 3 et 5 la comparent bien (l. 591, 598). L'arrêt « absente ou en double :
  `piece-non-conforme` » vaut maintenant sans ambiguïté pour les douze clés : la contradiction du tour 2 est levée. Sens prudent : un arrêt de plus,
  aucune ligne ni issue changée.
- **C2 (12, point 3)** : la liste du contenu de la section « Verdict » nomme la phrase « Lecture prudente » (section 6.9).
- **C3 (6.9)** : « la ligne 139 de T08A (R143) entière, intitulé en gras compris » ; la ligne 139 de `prereg/T0.8-base-A-mots-et-cout-v1.md` est bien
  « **Lecture prudente, à écrire telle quelle avec toute phrase sur le barreau 3** : … » ; les mots « ne porte rien » et « flagrant » y figurent ; la
  consigne les dit cités. Accord avec la préférence de la mère (A6) : recopie entière, une fois, et marque après toute phrase sur le barreau 3.
- **C4 (6.1)** : l'ordre (1) commence par l'empreinte du bordereau et de son compagnon, ce qui s'accorde avec la première phrase de 6.1 et avec la section 2.
- Relus après les corrections : sections 6.0, 6.1, 6.3 (points 2 à 5), 6.9, 12 (points 2 et 3), 13 (neuf codes) et 14 : rien n'est dérangé.

## 2. Vérifications refaites

- **Contrôle des renvois** : `verification_renvois_consigne_b_v2.py`, mêmes arguments que la sortie v5 du rédacteur (filtres : commande v3 ; bloc C5 : commande v4,
  brouillon 1 ; jeton laissé), motif des noms de modèles passé en argument : 194 citations retrouvées à leur ligne, 194 renvois employés et
  connus, 7 empreintes égales, 12 noms conformes au motif du bloc C7, liste fermée de 15 lignes et bordereau de 29 lignes, bloc C5 : 14 fichiers copiés,
  accord ; « Jamais remis » : aucun nom présent ; **VERDICT : CONFORME, code 0** (ma sortie, non écrite au dépôt). Un premier essai de ma main avec un mauvais
  argument de commande a donné deux fautes sans rapport avec la pièce ; rejoué avec les bons arguments : code 0.
- **Filtre `INTERDITS_CONTENU_B`** (bloc 1C, `bbis|b-bis|etape-b-bis|étape b bis|b bis|bras-attaque|mode-tenu`) : aucune ligne touchée ; recherche directe de ces mots
  et de « bras d'attaque » ou « tenu à l'écart » dans la pièce : aucune occurrence en dehors du motif cité du bloc 1C (ligne 167, nom, non contenu). Aucun identifiant de
  modèle ; aucun marqueur à chevrons.
- **Lectures et choix** (1) : « lecture de cette consigne » et « choix de cette consigne » relus aux points touchés ; aucun critère ajouté. Pour `SCELLEMENT-T07` : le texte
  la dit « nécessaire à l'étape B » par G1 sur tout chemin (T0.7 l. 2639-2641, interprétation 1, R169), et le module refuse sans elle quand `VERDICT-P3BIS` est lue
  (`garde_adaptee_v1.py`, l. 154-155, commit c2fab6cc…) : l'exiger est donc plus proche du texte que de « permise sans plus ».
- **Quatre lignes finales** (4, 8) : conformes à la règle R-V2 (aucun nombre, issue, ligne de table, empreinte d'un fichier du run ; seule l'empreinte du message reçu) ;
  le filtre du bloc F-C (`grep -E '^(STATUT|FICHIERS|DÉCLARATIONS|MESSAGE)'`) les retient toutes. Neuf codes d'arrêt : `fichier-interdit-recu`, `piece-non-conforme`,
  `lecture-impossible`, `critere-inapplicable`, `ecart-au-texte`, `desaccord-ligne-mecanique`, `contradiction-consigne-texte`, `refus`, `autre` ; conditions
  mécaniques, aucun repli silencieux ; `refus` et `autre` sans texte sur la ligne `STATUT`.
- **Pièces et fichier `sondes-t07.json`** (3) : quinze pièces de la liste fermée égales au bloc C5 (contrôle 7 du programme) ; ce que la consigne fait lire dans la pièce 15
  (clé `resultat.sondes_neuves.p6`, motif de T7-P6, R122, T0.7 l. 2659) cité de façon conforme ; je n'ai ouvert ni ce fichier ni aucun résultat.
- Sections 6.5 à 6.7, 4 et 5 : non touchées par ce différentiel ; contrôlées aux tours 1 et 2, rien n'a bougé.
- (9) : rien de l'étape B bis, du bras d'attaque ni du mode tenu à l'écart n'entre dans ce que le lecteur lit ou écrit.

## 3. Lecture à blanc : chaque point jugé

B1 : retenu (corrigé par K1, section 6.10 : heure de fin lue avant la version achevée). B2 : non retenu comme correction : risque de faute de recopie réel, mais
c'est une option de procédure sans écart au texte ; laissé à la mère (§ 6). B3 : retenu (K3, un code seul sur la ligne `STATUT`). m1 : retenu (clé = premier champ, égalité
exacte). m2 : retenu (dix clés nommées ; complété par C1). m3 : retenu (ordre des contrôles ; complété par C4). m4 : retenu (K8). m5, m6 : non retenus : la copie du message est
comparée par la session hôte (une différence arrête, sans repli) et l'ordre du premier geste est écrit en 6.0. m7, m8, m9, m11 : retenus (K9, K11, K12, K14). m10 : retenu pour le
motif de Q « illisible » ; non retenu pour les trois domaines à ajouter (le texte range tout défaut de forme en Q « illisible »). m12 : retenu (chaînes fixes) ; la forme de la ligne dédiée
reste à la mère. m13 : retenu (K15, K22 : balayages bornés à l'ensemble du module). m14 : non retenu : les « R » nus du corps (par exemple « T7-P6 (R5, R6 …) ») sont des lignes de la
table du texte, dites telles par l'en-tête. m15 : non retenu : un seuil neuf serait un critère neuf. m16 : non retenu comme correction (garde de la session hôte, bloc C7) ; point pour la
mère. m17 : mise au propre au sceau.

## 4. Les sept ambiguïtés A1 à A7

A1 : lecture fidèle et prudente ; R-BA1 confié à la mère par le texte (l. 2183), rappelé ; la double marque est admise car elle ne change aucune ligne ni dose. A2 : fidèle ; cellule entière,
différence avec la phrase du module écrite sans arrêt. A3 : bornée aux ensembles que le module balaie (K15, K22) ; fidèle ; la lecture plus large reste à la mère si elle la veut (réserve seulement). A4 : fidèle
(audit dû, non fait par ce verdict). A5 : fidèle et prudente, aucun calcul neuf. A6 : lecture prudente de T08A l. 139 recopiée entière une fois, marque après toute phrase sur le barreau 3 (conforme à
la préférence de la mère). A7 : mécanique, fidèle. Aucune n'est un écart à un texte scellé qui demande le mot de Lazar.

## 5. Remarques facultatives (aucune exigée)

- **F1** (précision de renvoi, 6.3 point 2) : la cause « G1 refuse déjà sans elle » est plus exacte avec le renvoi à R169 (T0.7 l. 2639-2641), dont le texte dit que G1 sur tout chemin rend
  `SCELLEMENT-T07` nécessaire à l'étape B. Couple, si la mère le veut :
  - ancien : `que G1 refuse déjà sans elle (T0.7 l. 1725) : choix de cette consigne`
  - nouveau : `que G1 (R169, T0.7 l. 2639-2641 ; l. 1725) refuse déjà sans elle : choix de cette consigne`
  (une occurrence ; « R169 » existe dans la table ; rejouer le contrôle des renvois après.)
- **F2** : section « Contre-lecture » : à garder ou à retirer au sceau (historique pour la mère) ; le contrôle des noms passe avec elle.

## 6. Points pour la session mère

1. **Mise au propre au sceau** : remplacer le jeton `EMPREINTE-COMMANDE-V4-A-REMPLIR` (une seule occurrence, ligne 24) par l'empreinte de la commande v4 définitive ; réécrire la puce « État du fichier »
   (« non scellé », « brouillon 5 ») ; rejouer le contrôle des renvois (code 0 exigé) après ces réécritures ; décider du sort de la section « Contre-lecture ».
2. **Lettre du rédacteur** : la puce de l'en-tête dit « quatrième rédacteur … (modèle C) » ; la demande de ce tour annonçait le modèle A pour les corrections. À faire concorder avec la réalité
   avant le sceau (la puce « Rédacteur » dit « modèle B »).
3. **C1** : « SCELLEMENT-T07 exigée ici » : choix prudent, appuyé sur G1 sur tout chemin (T0.7 l. 2639-2641) ; si la mère préfère la traiter comme permise, il faut écrire « absente » et ne pas juger les points 3 et 5.
4. **Ligne dédiée de BA-L2** : la lecture par chaînes fixes n'est sûre que si la session hôte écrit la ligne avec des chaînes exclusives (jamais « mot de Lazar » dans une ligne qui dit que BA-L2 s'applique sans lui) ;
   apostrophe droite comme dans « ne s'applique pas ».
5. **Aucune garde de contenu** sur `verdict-ferme/` au bloc C7 (noms seulement) : un identifiant de modèle recopié d'un manifeste passerait ; à vérifier à la lecture du verdict.
6. **Option B2** (verdict assemblé par programme) : toujours à décider ; non exigée.
7. **Exclusion** : j'ai lu le texte scellé de T0.7 ; je suis exclu des lecteurs de P3-bis, de l'étape B et de B bis.

## 7. Déclaration et incidents de ma main

- Jamais ouverts : aucun fichier sous `diag/`, `runs/`, `donnees/` (ni `sondes-t07.json`, `lecture-t07.json`, `audit-fuites-t07.json`, scores, manifestes) ; aucun fichier de `docs/verdicts/` ; rien de l'étape B bis,
  du bras d'attaque ni du mode tenu à l'écart ; `registres/decisions.md` non ouvert. Code lu par `git grep` au commit `c2fab6cc…`.
- Incidents : (1) la sortie du contrôle des renvois affiche des noms de chemins de la liste (dont ceux sous `diag/`) : noms seulement. (2) Un premier essai du contrôle avec un mauvais argument, sans effet. (3) Fichier jetable
  `renv.txt` dans mon dossier de travail du scratchpad, jamais au dépôt. (4) Aucun commit, aucune poussée, aucun réseau, aucune dépense ; la pièce n'est pas modifiée.

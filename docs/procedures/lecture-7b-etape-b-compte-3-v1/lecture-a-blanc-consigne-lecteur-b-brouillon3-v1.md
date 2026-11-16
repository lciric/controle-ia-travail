# Lecture à blanc de la consigne du lecteur B (brouillon 3) — lecteur à blanc C — v1

- **Pièce lue** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1-brouillon3.md`
  (`12881d63d3cc5056b1246a3816da5d4a67d28970178085eca8c21d9bdd9cce85`, 1 015 lignes, égale à son compagnon).
- **Rôle** : jouer sur le papier, sans aucune donnée, le futur lecteur B (modèle C), pas à pas. Je ne suis pas le lecteur B.
  Les numéros de ligne ci-dessous sont ceux du brouillon 3. Aucune pièce n'est modifiée.
- **Verdict (3 lignes)** : la consigne est suivable et très complète ; ses 194 renvois et ses empreintes sont exacts, ses
  clés de fichiers JSON sont presque toutes justes au code. **Trois points bloquants** (heure de fin impossible à tenir,
  recopie à la main de centaines de nombres et de cellules « à l'octet », deux textes libres qui peuvent faire sortir un
  nombre par le rapport final) et dix-sept points mineurs, dont plusieurs sont de vrais risques d'arrêt à tort.

## 1. Ce que j'ai vérifié, et qui est conforme

1. **Renvois (section 3.2, L196-406)** : les 194 renvois `Rnnn | fichier | ligne | citation` sont retrouvés, caractère pour
   caractère, à leur ligne dans les six textes (T0.7, T0.6, base (A), N-063, audit, addendum) : 0 écart ; aucun trou de
   numérotation de R001 à R194 ; aucun renvoi employé dans le corps qui soit absent de la table. Le découpage de la table
   par « troisième barre » est sans piège (les lignes `R062` à `R095` commencent par une barre mais le découpage à trois
   coupes les rend correctement).
2. **Empreintes de l'en-tête (L46-54)** : T0.7, T0.6, base (A), N-063, audit, addendum et configuration égales aux fichiers.
   Les onze fichiers de code et le fichier `manifeste.py` de la section 5 (L444-456) : empreintes égales au commit
   `c2fab6cc…` (`git show`).
3. **Pièces et bordereau** : les quatorze pièces à compagnon (1 et 3 à 15) plus l'extrait font bien 29 lignes ; le bloc C5 de
   la commande v3 (13 fichiers, 27 lignes) plus `diag/$R7/sondes-t07.json` donne 14 et 29, comme la commande v4 en cours
   (`commande-compte-3-phase-c-v4-brouillon1.md`, lignes 392 et 408). La liste fermée de la section 2 est égale à celle du bloc
   C5. Aucun nom de la liste `INTERDITS_NOMS_B` ne touche un chemin de la liste fermée (y compris `sondes-t07.json`).
4. **Clés de `lecture-t07.json` (L461-506)** : confrontées à `lecture_v4.etape_b`, `lecture_v3.lecture_jeux_v3`,
   `plancher_v2.comparer_difference_au_plancher` et `resume_pour_critere`, `criteres_v1` (`deriver_classe`, `entree_F`,
   `issue_critere_3`, `valider_*`), `lectures_t07_v1` (`placebo`, `reserves`) : les clés citées existent avec la forme dite
   (`bas` = quantile + borne basse de D ; `bas_sonde`, `haut_sonde` ; `plancher.quantile`, `.quantile_plancher`, `.n` ;
   `triviaux.*.separation` nul permis ; `entrees` à sept clés, `I` et `II` nuls hors chemin ; `cles_ignorees` à trois sous-clés ;
   `garde.instant` écrit par `date_utc`, donc égal à la date de la ligne `OUVERTURE-T07`). Les domaines `non_calculable` et
   `incoherent` (sans accent) sont justes.
5. **Pièce 15 (L507-530)** : clés `sondes_lues`, `sondes_lues_manifeste`, `concepts`, `niveau_applique`, `jeux_scelles`,
   `principales`, `principales_consignees`, `sondes_neuves`, `controles_jeux.controle_9.jeux[…]` (`paires_scellees`,
   `paires_en_defaut`, `taches_sorties`, `paires_gardees`, `insertion_non_isolee`, `etat`), `phrases_concepts` : justes au code
   de l'étape A (`lecture_v4`, `controle_jeux_v1.rejouer_controle_9`). Le contrôle de rattachement de 6.6.1 (noms des sondes
   neuves commençant par le concept suivi d'un tiret) est celui de `lecture_v2.controler_t07`.
6. **Logique de la grille** : les conditions de 6.6.5 (ordre `L6, L4, L4b, L5, L2, L3`, états U, N, Z, E, agrégation Z > E > N >
   U, `non interprétable` si la séparation d'un prédicteur trivial est au moins égale à celle de la sonde) sont celles du code
   (`regles`, `etat_pour_sonde`, `etat_organisme`, `agreger_doses`) et du texte (L1813-1836, L1272-1276).
7. **Motif de T7-P6 (6.7.3)** : le code écrit « jeu J-A ou J-C non scellé » quand `index["p6"]` est absent, ce qui arrive aussi
   quand l'apprentissage échoue (DF-05) ; les trois cas de la consigne (une ligne de jeu manque ; les deux présentes ; motif de
   la pièce 15 commençant par « échec ») sont donc justes. Au registre actuel, `SCELLEMENT-JEUX-T07-JD` et `-JA` existent et
   `-JC` n'existe pas : le motif est vrai et la branche « les deux présentes » ne servira pas, sauf ligne `-JC` inscrite d'ici là.

## 2. Points bloquants

**B1 — Heure de fin : contradiction d'ordre (6.10, L821-824 ; 12.2, L933-935 ; 1, L110-111).** La section 12 exige dans l'en-tête
du verdict « heures de début et de fin (`date -u`) » ; la section 6.10 dit d'écrire le verdict, d'en calculer l'empreinte, d'écrire
le fichier d'issue, et seulement après de lire « l'heure de fin par `date -u` ». Le verdict ne peut plus être retouché après
l'issue (L110-111). Un lecteur de mon modèle soit écrit une heure de fin estimée (donc « écrite à la main », interdit par le
message), soit rouvre le verdict (interdit par R12).
*Proposition* : définir « heure de fin = lecture de `date -u` juste avant d'écrire la version achevée du verdict en prose » et
l'écrire dans 6.10 avant l'écriture du verdict ; dire que les heures peuvent être posées par le script d'assemblage (voir B2).

**B2 — Recopie à la main des nombres et des cellules « à l'octet » (6, L552-556 ; 6.8, L783-789 ; 12.4 à 12.9, L940-955).** La
consigne exige que « chaque nombre du verdict renvoie au fichier, à sa clé et à l'empreinte » et que la cellule « lecture » soit
recopiée « à l'octet » (cellules de 300 à 1 100 caractères, avec guillemets français, `≥`, gras). Les scripts recopient « sans
arrondi » dans leurs sorties (L553-554), mais **rien n'oblige le verdict en prose à être assemblé par programme** : le lecteur
devra retaper, de mémoire de conversation, plusieurs centaines de nombres (quatre sondes × un à cinq jeux × une douzaine de
champs, plus placebo, validité, effectifs, réserves) et des cellules entières. Un lecteur de mon modèle fait des fautes de
recopie sur de longs nombres décimaux et sur des empreintes ; le verdict deviendrait inexact sans qu'aucune garde ne le voie
(le fichier d'issue n'engage que l'empreinte du verdict).
*Proposition* : (a) les scripts écrivent, en plus de leur sortie, des blocs Markdown prêts à insérer (tableaux de lectures,
cellule recopiée, sous-phrases, faits du registre) ; (b) le verdict est assemblé par un script (`verdict-T0.7-etape-B-v1-assemble-v1.py`,
nom permis par le motif de la section 9) qui insère ces blocs et les passages de prose écrits par le lecteur ; (c) le lecteur ne
tape lui-même aucun nombre ni aucune cellule ; (d) le script d'assemblage vérifie que chaque nombre cité du texte libre figure
dans une sortie. Même remède pour l'heure (B1).

**B3 — Deux textes libres dans le rapport final (14, L1008-1011).** `arret refus` est suivi du texte du refus « tel quel » sauf s'il
« cite un nombre, une issue ou le contenu d'une pièce » ; `autre` est suivi d'un motif d'une ligne « sans nombre ni issue ». Ce
jugement est fait par le lecteur au moment où il est arrêté, donc dans le cas où il est le plus mal placé ; un refus de
permission cite un chemin, un identifiant de course ou un nom de clé, et l'on ne sait pas si les chiffres du nom d'une course
sont « un nombre ». Ces deux champs
sont les seuls canaux par lesquels un nombre ou un morceau de pièce peut quitter `verdict-ferme/` (L98-101, L1013-1015).
*Proposition* : `STATUT : arret refus` et `STATUT : arret autre` sans aucun texte ; le texte entier va toujours au fichier d'arrêt.

## 3. Points mineurs

Chacun est donné avec son endroit. Ceux marqués (arrêt à tort) peuvent faire arrêter un lecteur qui lit juste.

1. **Clé de registre cherchée par sous-chaîne (6.3.2, L581-584) (arrêt à tort).** `AUDIT-FUITES-T07` est une sous-chaîne de
   `CONSIGNE-AUDIT-FUITES-T07` : un décompte par recherche de mots trouve deux lignes et fait arrêter `piece-non-conforme`.
   *Proposition* : écrire « la clé est le premier champ entre barres, égalité exacte ».
2. **« Chacune des dix clés de l'étape B du point 2 » (6.3.5, L592-593).** Le point 2 liste douze clés ; le texte (L2174-2178) en
   exige neuf à l'étape B (plus `SCELLEMENT-T07`, permise) ; `LECTURE-T08-BASE-A` et `SCELLEMENT-T08-BASE-A` ne sont pas des clés
   que le module lit. *Proposition* : nommer les dix clés une à une dans 6.3.5.
3. **Ordre « contrôles » et fichier inattendu (1, L112-113 ; 6.1, L566-571).** Un script qui empreinte tous les fichiers de
   `pieces/` ouvre le fichier inattendu qu'on lui interdit d'ouvrir ; et `piece-non-conforme` ou `fichier-interdit-recu` sont
   donnés « ou » (L571). *Proposition* : ordre écrit : (1) lister les noms ; (2) comparer aux 29 chemins du bordereau et à la
   liste fermée (extra → `fichier-interdit-recu`, manquant → `piece-non-conforme`) ; (3) seulement ensuite empreinter.
4. **Citations par script sur des fichiers entiers (2, L154-155).** « jamais en entier d'un seul geste » vise l'affichage ;
   6.1 exige un contrôle de 194 citations qui ouvre tout le texte. *Proposition* : dire que les scripts ouvrent les fichiers en
   entier et n'affichent que les plages.
5. **Message recopié (11, L920-925).** Il contient deux empreintes de 64 chiffres et plus de 1 800 caractères ; une faute d'un
   caractère annule tout le lancement (nœud, rien n'est commité). Le lecteur n'a pas le fichier du message sous la main.
   *Proposition* : un contrôle interne dans le script « controles » : les deux empreintes écrites dans la copie égalent celles du
   bordereau et de la consigne recalculées ; et faire écrire la copie par un script plutôt qu'à la main.
6. **Premier geste (6.0, L560-562 ; 2, L151-152 ; message).** Trois consignes de premier geste : « lis d'abord ta consigne »,
   « vérifie-la avant lecture », « avant tout, recopie le message ». *Proposition* : écrire l'ordre : `date -u` ; empreinte de la
   consigne ; lecture ; copie du message ; contrôles.
7. **Lecture limitée à `pieces/` (1, L90-93) et fichiers de travail.** L'interdit couvre « aucun autre fichier ou dossier que
   `pieces/`, le bordereau et son compagnon » mais le lecteur doit relire ses propres sorties dans `verdict-ferme/` et recalculer
   l'empreinte du verdict. *Proposition* : ajouter « et les fichiers que tu as toi-même écrits dans `verdict-ferme/` ».
8. **Passe 1 : clés lues trop larges (6.5, L630-633).** Le script lit `resultat.entrees` en entier (donc `I`, `II`, états des
   sondes) et `resultat.doses` en entier (donc `etat_ii_par_dose_jugee` et `ecart_a_la_base`, qui portent les états et les aires des
   sondes sur (ii)). Cela défait le but de l'ordre : « n'ouvrir les lectures des sondes qu'après la première sortie ». La
   comparaison de L657-658 n'a besoin que de `Q`, `qualifiees`, `jugees`, `hors_jugement`, `non_calculables`,
   `etiquette_fichier`, `etiquette_recalculee`, `derivation`, `marques`, `p064`, `controle_aire`, `motif_Q_illisible`.
   *Proposition* : restreindre à ces sous-clés et à `entrees.G`, `.P`, `.A`, `.Q`, `.F`.
9. **Journal des ouvertures lu avant la dérivation de Q (6.3.4-6.3.6, L623-626, L600-601 ; section 5, L546-547).** La ligne
   `scores-t07/<run> (Q = … ; conditions retirées : …)` porte la valeur de Q du module avant que le lecteur ait dérivé la sienne,
   et dit que les scores ont été ouverts. *Proposition* : le script « controles » n'imprime que les clés et les dates de ces
   lignes ; leur contenu entre parenthèses n'est lu qu'en 6.5.6.
10. **Motif de Q « illisible » « introuvable dans la pièce » (6.5.4, L659-661) (arrêt à tort).** Le motif est un message écrit
   par le code (« clé absente doses.S25.aire », etc.), jamais une chaîne du fichier : on ne peut pas le « trouver ». *Proposition* :
   « vérifier sur la pièce 12 que le fait que le motif décrit est exact ». Même remarque pour les domaines vérifiés par le module
   (type entier exact de `n_permutations`, `niveau` égal à la clé `niveau_base_t06`, champs numériques dans [0 ; 1]) : le texte
   n'en donne pas la liste complète ; ajouter les trois dans 6.5.4.
11. **Forme du journal et de l'extrait (section 5, L543-548 ; commande C5).** Les trois sections de l'extrait sont écrites avec
    `grep -n` donc toutes précédées de `<n>:` ; la consigne ne le dit que pour la première. Le motif du `grep` du journal,
    `etape-B`, est aussi un préfixe d'autres noms : à vérifier côté commande.
12. **Ligne dédiée de BA-L2 (6.9, L806-819) — texte libre.** Le lecteur doit décider si une ligne de `decisions.md` « dit que BA-L2
    ne s'applique pas / s'applique et porte le mot / ne dit pas l'état ». Sans forme fixe, deux lecteurs différents jugeront
    différemment. *Proposition* : demander à la session hôte de fixer la ligne sous la forme `BA-L2 : ne s'applique pas` ou
    `BA-L2 : s'applique ; mot de Lazar : <date>, <citation>` et dire qu'une autre forme est un arrêt `ecart-au-texte`. Voir A1.
13. **« Trop beau » sur deux lectures (7, L838-840).** La lecture large (« tous les jeux d'organisme lus contre un plancher ») est
    moins susceptible de déclencher que la lecture étroite (si tous sont au-dessus sur un ensemble plus grand, ils le sont sur le
    sous-ensemble) : « sens prudent » est donc sans effet, et l'ensemble « tous les jeux lus » n'est pas défini (validité, hors
    jugement, descriptifs ?). De même pour « aire > 0,95 ou < 0,05 » et « quantile > 0,70 » (L835-836) : l'ensemble balayé n'est pas
    borné ; le code balaie les lectures décisives, hors jugement et six prédictions de validité (docstring de `lectures_t07_v1.reserves`).
    *Proposition* : borner les trois balayages à cette liste nommée, ou les laisser au seul constat du module et écrire la
    différence éventuelle.
14. **Un seul sens du mot « R9 », « R12 », « R4 », « R10 » (L57-62, L829, L768-776).** La consigne a trois familles de noms, mais
    ses phrases écrivent « R9 », « R7 », « R10 », « R12 » sans préfixe (lignes de la table, réserves, ou règle du programme).
    *Proposition* : toujours « ligne R9 », « réserve R10 », « règle R12 » au corps du texte.
15. **Propreté suspecte (7.5, L849-852).** « Nombres identiques d'une sonde à l'autre », « intervalle de largeur nulle », « aire
    égale à 0,5 exactement » sont des exemples sans seuil de tolérance : le lecteur ne sait pas combien il doit balayer ni
    comment décider « identique ». *Proposition* : fixer égalité exacte des flottants écrits, sur l'ensemble des lectures de
    `jeux` ; tout le reste est facultatif.
16. **Identifiants de modèle (1, L102-106).** Aucune garde mécanique : les pièces 11, 14 et 15 peuvent porter des noms de modèle
    ou de matériel dans `versions`, `reglages`, `ouverture.manifeste_t07`, `code_t07`, et un script qui recopie un sous-arbre les
    copie dans `verdict-ferme/`. *Proposition* : la session hôte filtre les fichiers de `verdict-ferme/` au bloc C7 par le même
    motif que celui des pièces ; et le lecteur n'imprime pas ces sous-arbres entiers.
17. **Marqueur à remplir et mentions de forme (L3-15, L24-26).** `EMPREINTE-COMMANDE-V4-A-REMPLIR` et la puce « État du fichier »
    sont à réécrire au scellement ; le script de vérification des renvois du rédacteur doit être rejoué après ces réécritures
    (rapport du rédacteur, § 3). La puce actuelle dit « brouillon 3 » et « non contre-lu » : si elle reste, le lecteur en tirera
    une réserve.

## 4. Avis sur les ambiguïtés A1 à A7 du rapport du rédacteur

Pour chacune : faisable par un lecteur de mon modèle ? risque d'erreur ? Je ne tranche pas le fond.

- **A1 (R-BA1, qui l'écrit).** Faisable, risque **moyen**. Le texte met R-BA1 à la charge de la session mère (T0.7 L2183) ; la
  consigne la confie au lecteur par « lecture de cette consigne ». Le risque n'est pas la copie de la phrase (déjà donnée), mais
  « après chaque phrase de ton verdict qui porte sur le critère 3 » : quelle phrase porte sur le critère 3 ? (sections 3, 4, 6, 7, 11
  ?). Je recommande une seule mention, en tête de la section « Verdict » et de la section « Réserves », qui dit « toute phrase de
  ce verdict sur le critère 3 se lit sous la réserve R-BA1 », plus la détection de l'état par une forme fixe (point 12).
- **A2 (phrase gelée non bornée).** Faisable, risque **faible** sous réserve de B2 (recopie par script). La consigne a bien
  prévu l'écart attendu (la phrase du module est plus courte que la cellule, p. ex. L4 qui porte les réserves de l'audit de P3).
  À ajouter : « cette différence est attendue et n'est pas un arrêt » pour éviter qu'un lecteur la prenne pour un désaccord de
  ligne.
- **A3 (« trop beau » et ensembles de jeux).** Faisable, risque **moyen** : voir mineur 13. Le lecteur écrira un désaccord inutile
  si l'ensemble n'est pas borné ; le sens « prudent » de la consigne est faux pour « tous au-dessus ».
- **A4 (audit de symétrie sur un jeu non décisif).** Faisable, risque **faible** : « audit dû, non fait par ce verdict » est
  mécanique. Il produira beaucoup de questions à Lazar si `temoin` ou `T100` dépasse un seuil ; c'est dans l'esprit du texte
  (L1924).
- **A5 (puissance).** Faisable, risque **faible** : recopier le point 7 de la section « Puissance » sans calcul, question écrite.
  Rien à ajouter, sauf que le lecteur doit savoir que la formule de L2030 ne lui est pas demandée : c'est dit en L799-802.
- **A6 (« lecture prudente » de la base (A)).** Faisable, risque **faible** : « n'écrire rien de sa main » est suivable ; la seule
  hésitation est de savoir s'il doit recopier la lecture prudente (T08A L139) quand il écrit une phrase sur la base ; la consigne
  dit « tu recopies » (L818-819) sans dire « une fois ou à chaque phrase ». Préciser « une fois, section 3 ».
- **A7 (addendum non scellé).** Faisable, risque **faible** : la comparaison ligne du registre / « Nouvelle ligne » de l'addendum
  est mécanique et je l'ai faite : les deux lignes sont égales. Le point de forme à préciser : l'extrait préfixe la ligne par
  `<n>:` (mineur 11).

## 5. Ce qui a été éprouvé sans écart (pour ne pas être rouvert)

- La section 5 et le code : aucune clé citée n'est absente ; je n'ai trouvé aucune clé du code que la consigne omette et dont
  une entrée de la grille dépende.
- Les neuf codes d'arrêt : chaque condition est mécanique, sauf `critere-inapplicable` pour « condition d'une ligne que tes pièces
  ne permettent pas de juger et dont la ligne dépend » (L981), qui est un jugement ; je propose de la remplacer par la liste
  fermée « G autre que ok ; ligne hors L ; entrée hors domaine ; aucune ligne ne s'applique ».
- Le rapport final de quatre lignes ne peut porter ni nombre, ni issue, ni ligne de table, ni empreinte d'un fichier du run, à
  deux exceptions près : la ligne `STATUT` (B3) et la ligne `FICHIERS`, dont les noms (`-v2`, `-arret-`, `-issue.json`) disent
  seulement qu'un script a été corrigé ou que le verdict a été écrit ; je les juge sans effet.

## 6. Déclaration d'exclusion

- **Rôle** : lecteur à blanc neuf de la consigne du lecteur B (brouillon 3) ; je n'ai écrit aucune pièce ; je ne serai jamais le
  lecteur B.
- **Modèle** : C.
- **Heures (`date -u`)** : début 2026-11-16T13:44:27Z ; fin 2026-11-16T13:56:54Z (lue juste avant le sceau).
- **Exclusion** : j'ai lu le texte scellé de T0.7 ; je suis exclu des lecteurs de P3-bis, du rôle de lecteur B de l'étape B, de
  toute lecture de l'étape B bis et de tout verdict de G0.
- **Pièces lues, avec leurs empreintes** :
  `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1-brouillon3.md` `12881d63d3cc5056b1246a3816da5d4a67d28970178085eca8c21d9bdd9cce85` (en entier) ;
  `…/rapport-redacteur-consigne-b-v1.md` `5a0582d1535991e6499b641e0574d1c0e489c4fc72f3985b2948fd4de24d5bd7` (en entier) ;
  `…/commande-compte-3-phase-c-v3.md` `9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e` (blocs C5, C6, C7, et lignes cherchées) ;
  `…/commande-compte-3-phase-c-v4-brouillon1.md` `f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755` (lignes cherchées sur « sondes-t07 », « bordereau », « quatorze ») ;
  `prereg/T0.7-sondes-v0-v1.md` `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` (l. 1009-1030, 1065-1156, 1218-1236, 1256-1312, 1459-1545, 1813-1836, 1898-1942, 2174-2209, 2466-2480, 2500-2508, 2657-2660 ; les 194 citations par programme) ;
  `prereg/T0.6-organismes-v0-v1.md` `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` (l. 527-541 ; citations) ;
  `prereg/T0.8-base-A-mots-et-cout-v1.md` `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` (l. 124-141 ; citations) ;
  `prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md` `8c377286f2fa9be7020416a1d25bbcebb8fad0944f14c508614519a6a0886dc8` (l. 1-12, 36-44, 288-299 ; citations) ;
  `prereg/T0.7-consigne-audit-fuites-v1.md` `43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d` et `docs/decisions/decision-N-063-v2.md` `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` (ouverts par programme pour les seules citations, aucun passage affiché) ;
  `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` (clés et début des valeurs) ;
  code du module au commit `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` par `git show` (copies jetables dans mon dossier de travail) : `lecture_v1.py`, `lecture_v2.py`, `lecture_v3.py`, `lecture_v4.py`, `criteres_v1.py`, `plancher_v2.py`, `lectures_t07_v1.py`, `lectures_t07_v2.py`, `registre_v1.py`, `sondes_neuves_v1.py`, `controle_jeux_v1.py`, `manifeste.py`, `premier_test_ia/statistiques.py` (`aire_simple`), `plancher_v1.py` (`predicteurs_triviaux`) ; empreintes des onze premiers égales à la section 5 de la consigne ;
  `registres/scellements-v1.md` `18e5fe518c6027a868a60bf89f6d3eac63ac65c717d2cc37105225b4a96cc517` (quatre premières colonnes) et `registres/scellements-v1.md.ouvertures.md` `8454529867ed2af9d655135a21a3e03320cef89edbcf1a81df73a05071373e23` (colonnes 2 à 4 ; deux lignes de l'étape A, rien de l'étape B).
- **Jamais ouvert** : aucun fichier sous `diag/`, `runs/`, `donnees/` (ni `sondes-t07.json`, `lecture-t07.json`, `audit-fuites-t07.json`, scores, manifestes de run) ; `diag/*/lecture-sondes-t06.json`, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3` ; aucun fichier de `docs/verdicts/` (noms comptés seulement) ; l'étiqueteur et `scripts/extraire_mesures_epreuve_t06_v1.py` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk` ; rien de l'étape B bis ; `registres/decisions.md` (aucune ligne lue : je n'ai pas la clé de la ligne dédiée de BA-L2) ; aucune clé ni variable d'environnement ; aucun réseau ; aucun commit, aucune poussée.
- **Incidents de ma main** :
  1. Un listage de `prereg/` filtré sur « addendum » et un listage de `registres/` ont affiché des noms de fichiers de l'étape B bis et de bras d'attaque ; **noms seulement, aucun fichier ouvert**.
  2. Un `git log --oneline -1` a affiché le titre du dernier commit du dépôt ; sans effet sur le travail.
  3. `ls docs/verdicts | grep -c` a compté, sans l'ouvrir, le fichier d'issue de P3-bis et son compagnon.
  4. Les textes de T0.7, T0.6, base (A), N-063, audit et addendum ont été ouverts en entier par un programme pour contrôler les 194 citations ; seules les plages listées ci-dessus ont été affichées.
  5. Aucun fichier existant n'a été modifié ; ce fichier est neuf et scellé.

PROJET DE FEU ÉCRIT DE LA SESSION MÈRE — version 3
Course de l'étape B bis de l'épreuve des sondes entraînées sur la tâche (T0.7)

Rédigé le 2026-11-18 (heure exacte à relever par `date -u` au moment de sceller). Remplace pour la suite le feu du 2026-11-17T11:13:33Z (registres/t07-etape-b-bis/feu-bbis-v2.txt, empreinte 33912cbe418f25c25ea3108572fa9cc07ee1b6bbecc236b9b934ff43cb21760b), qui reste archivé sans modification (R12). À verser sous un nom neuf : registres/t07-etape-b-bis/feu-bbis-v3.txt, scellé, inscrit au registre propre.

§ 0 — CE FEU N'EST PAS EN VIGUEUR À SA RÉDACTION
Il n'autorise aucune création de machine. Il entre en vigueur, et seulement alors, quand les huit conditions suspensives du § 12 sont levées, chacune par une pièce versée et scellée ou par un mot écrit de Lazar inscrit au registre des accords. Un opérateur qui lit ce feu sans les huit pièces du § 12 s'arrête, ne crée rien, et le dit en une ligne.

§ 1 — LIGNES D'ACCORD
Ligne d'accord de calcul : GO-2026-11-14-09 (type « calcul », 40,00 USD, échéance 2026-11-22, une A100 seulement, une relance au plus, garde de débit, feu écrit de la mère avec ce numéro avant toute location, arrêt et destruction par identifiant selon R10). Extrait fidèle au dossier : registres/t07-etape-b-bis/go-bbis-v2.txt (33f38e67…), identique octet pour octet à la ligne 328 de registres/go.md.
Second accord, pour la course supplémentaire, une seule : GO-2026-11-16-11 (écart au texte scellé, second addendum du contrôle carte-processeur).
Accord de la mesure de dispersion des aires entre deux ordres de calcul : GO-2026-11-16-12.
Accord de l'opérateur : GO-2026-11-16-06 (la machine est créée par un sous-agent opérateur, arrêt au premier refus de permission, du crochet de garde ou du classifieur, sans rejeu, reformulation, découpage ni contournement).
Accord de lancement et de dépense donné par Lazar le 2026-11-18 vers 02:14Z, verbatim « Billet sur le contrôle de l'IA — un seul run manque : la course de l'étape B bis. : go » (R-3129). Cet accord ne dispense ni des préalables ni de ce feu.

§ 2 — TEXTES QUI FONT FOI, À CITER DANS LE VERDICT
Texte scellé : prereg/T0.7-etape-B-bis-v1.md — 0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb (recalculée par moi, égale à son compagnon et à la ligne SCELLEMENT-BBIS du registre propre, inscrite 2026-11-14T12:30:30Z).
Premier addendum d'écart : prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md — f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7. Un verdict de l'étape B bis qui ne cite pas cette ligne n'est pas scellé (règle du registre des addenda).
Second addendum d'écart, contrôle carte-processeur à deux horizons : prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md — 18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26.
Registre propre : registres/t07-etape-b-bis-v1.md (jamais registres/scellements-v1.md ; une clé de l'étape B bis dans le registre partagé ferait refuser la fiche de code de T0.7, donc l'étape B elle-même). Lignes présentes : SCELLEMENT-BBIS, ABSENCE-B-BBIS, CODE-BBIS version 1 (remplacée), CODE-BBIS version 2 (en vigueur), GO-BBIS.

§ 3 — CODE DE LA COURSE
Commit : 05cd22aa15382f61eb62b9e7817890dde728dd5f. Vérifié ancêtre de la tête du jour par moi (`git merge-base --is-ancestor` → vrai).
Fiche en vigueur : registres/t07-etape-b-bis/code-bbis-v2.json — 4b28535c17fe450ff1c1ecc9164d91c4c8d03354e4f4137e324f2b04390be5bb, 63 fichiers (21 scripts, 22 sous src/controle_ia/t07bbis/, 20 sous tests/), les 63 vérifiés conformes au disque, à leurs compagnons et à ce commit.
Branche de code sur le distant : prep/t07bbis-code-v1, tête af0adb141d66ad4b1e9981e90729c24fdea071af (relevée par moi en lecture seule).
Script d'amorce : scripts/amorce_bbis_v5.sh — c8a9e81266a3b2fde4a920a4c4e51c2269f682cd066abeddfe6e8f2fc53cab00 (recalculée par moi, compagnon conforme). Le lanceur n'en imprime que les seize premiers caractères, c8a9e81266a3b2fd, et ne la compare à rien : l'opérateur relit ces seize caractères à l'œil sur la commande imprimée et s'arrête s'ils diffèrent.
Script de lanceur : scripts/lancer_bbis_v5.sh — ebd44e84d9f08392e27875f69ce5b16656648326d41469e1b1c21e0c25c92d6b (recalculée par moi, compagnon conforme).
Réserve inscrite : la contre-lecture en deux tours porte sur les scripts de version 4 (lancer_bbis_v4.sh 457457c0…, amorce_bbis_v4.sh 099a5c0e…). Les versions 5 n'ont pas de contre-lecture. Le différentiel entier a été lu : un seul changement de fond dans l'amorce (plancher d'essais 148 → 176) et sept renvois de nom dans le lanceur ; aucune logique, aucune garde, aucun ordre de contrôle changé.
Épreuve de niveau à deux plis : registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v2.json — da9fa42bf95c9d6507b01d7bf69db2876a56c00d26b0cc58c15cd7893bfa5919, 1188 octets (recalculées par moi). Niveau décisif retenu 0,99 (99 %) ; le passage à 99,5 % n'est pas déclenché. Coût : processeur seulement, 0 USD.
LE CODE DE LA COURSE EST GELÉ. La garde de création exige, pour deux relances, exactement deux lignes de fiche de code au registre propre : une troisième fiche, qu'exigerait R12 pour versionner le moindre changement, ferait refuser la création. Aucune retouche du code n'est possible avant cette course.

§ 4 — DONNÉES
Branche d'entrée : calcul/t06-confirmation-7b-v1, tête 55c3e3eb89a4650419f35999aaa4c54288275b0d (relevée par moi en lecture seule). Course de 7b : 20261111-151701-t06-reel.
Branche de sortie, neuve et exigée ABSENTE du distant avant la course : donnees/t07-etape-b-bis-v2. Vérifiée absente par moi (seule la version 1 revient, 8ec901fa…). La garde branche_de_sortie_neuve refuse si la branche existe (« nouveau nom exigé ») et refuse aussi si le distant est injoignable (« absence de la branche de sortie non prouvée ») : aucun repli silencieux, R5.
Dépôt de travail et lui seul : https://github.com/lciric/controle-ia-travail.git. Jamais lciric/controle-ia, qui sera la copie expurgée publique.

§ 5 — MACHINE VISÉE
Une seule carte A100 SXM4 80 Go. Aucune H200 (mot de Lazar seulement).
Au moins 16 cœurs effectifs ; au moins 128 000 Mo de mémoire vive ; disque 150 Go ; stockage au plus 0,08 USD/h ; version CUDA servie par l'hôte au moins 13.0 (clé cuda_max_good recopiée telle quelle de la recherche d'offres ; clé absente ou illisible : refus — la roue de torch 2.14.1 est construite pour CUDA 13.0, et c'est un pilote CUDA 12.8 qui a brûlé la répétition du 15 novembre).
Image : python:3.11-bookworm (celle du feu du 16 novembre, R-2996).
Étiquette : bbis-t07-v1, fixée par le texte scellé lui-même, donc intouchable. Elle ne commence ni par t06 ni par t07 : aucune garde d'inventaire d'une autre chaîne ne la compte.
Échéance de la minuterie : 13 heures. L'amorce refuse toute échéance hors de l'intervalle ]maintenant ; maintenant + 24 h], refuse une échéance illisible et refuse un identifiant d'instance illisible ; puis elle attend l'échéance et détruit l'instance par son identifiant, sans jamais juger le code de la réponse, en réessayant toutes les 60 secondes, et après cinq essais demande l'état « arrêtée ». Réserve à connaître : cette minuterie vit DANS le conteneur et meurt avec lui ; une instance arrêtée continue de facturer son disque sans minuterie. La destruction finale reste un geste de la session.

§ 6 — PRIX HORAIRE MAXIMAL ACCEPTÉ
1,40 USD/h, stockage compris refusé au-delà de 0,08 USD/h.
Motif du chiffre, et de l'écart avec les 1,5 USD/h du feu du 16 novembre : aucun plafond de prix de carte n'existe dans le code de la course (OFFRE_MIN ne borne que cœurs, mémoire vive, disque et stockage ; une offre à 50 USD/h a été acceptée en épreuve, code 0), et le code est désormais gelé. 1,40 USD/h est le seul plafond qui soit EXÉCUTABLE aujourd'hui : c'est celui que porte la garde de prix de la répétition (scripts/repetition_carte_bbis_v3.py, prix_max_usd_h), que l'opérateur joue hors de la chaîne scellée, en lecture seule, sur l'offre retenue avant de la passer au lanceur de la course. Resserrer un plafond est un geste de la mère, strictement plus sûr que l'ancien, et il reste sous ce que l'accord permet.
Ce plafond n'exclut aucune offre réelle : les six prix relus aux passes antérieures sont 1,0567 ; 1,1167 ; 1,1933 ; 1,2161 ; 1,2547 ; 1,2700 USD/h, tous sous 1,40.
Choix de l'offre par programme, jamais à l'œil et jamais retapée (correction de forme du 16 novembre, R-2998) : la recherche d'offres écrite dans un fichier, la garde du lanceur jouée hors ligne sur chaque offre, la garde de prix de la répétition jouée sur les survivantes, la moins chère retenue.
Prix relu APRÈS création au-dessus de 1,40 USD/h : destruction aussitôt par identifiant, puis nœud. (Le code de la course ne relit pas ce prix ; celui de la répétition le fait. C'est l'opérateur qui relit, et il relit.)

§ 7 — PLAFONDS ET GARDE DE DÉPENSE
Plafond de la ligne d'accord : 40,00 USD.
Cumul déjà dépensé sous cette ligne : 5,989 USD, soit ≈ 6,0 USD (répétitions 0,749 ; première création 0,10 ; relance unique 5,14). C'est CE nombre, celui de la ligne et non celui de la course, que l'opérateur passe à la garde de dépense.
Coupure de la garde de dépense : 39,50 USD, comparaison inclusive. La garde refuse dès que le cumul relevé plus un quart d'heure de carte atteint 39,50, et imprime alors la commande de destruction. Marge réellement disponible pour cette course : 39,50 − 5,989 = 33,51 USD. Reste sur la ligne : 34,01 USD.
La garde de dépense n'est PAS automatique : c'est une calculette, sans guetteur, sans boucle, sans lecture du vrai cumul chez le loueur. Elle ne protège que si l'opérateur la rejoue, et seulement aussi bien que les nombres qu'il tape. Elle est donc rejouée : une fois avant la création, puis à chaque heure de marche, puis avant toute relance.
Garde de débit de l'apprentissage, dans le code : arrêt si la marche projetée dépasse 11,0 h (marge 0,6 h, facteur 1,2, après les 20 premiers apprentissages).
Coût attendu de cette course : 5,6 à 9,9 USD selon le texte scellé ; 5,8 à 6,6 USD selon le second addendum, mesure de dispersion comprise. Pire cas de cette course sous ce feu : 13 h × 1,40 = 18,20 USD. Cumul de la ligne au pire après cette course : 24,19 USD sur 40.
Une seconde course, si elle devenait nécessaire, demande un feu neuf ET se trouverait bornée par l'arithmétique : 39,50 − 24,19 = 15,31 USD, soit 10,9 h au plus à 1,40 USD/h. À 1,40 USD/h, deux courses pleines de 13 h (36,40 USD) ne tiennent pas dans la marge de 33,51 USD : la mère le sait en écrivant ce feu.

§ 8 — CRÉDIT DU LOUEUR
Règle rappelée : au moins 20,00 USD de crédit avant toute création (R-2975, point 7 ; reprise par GO-2026-11-16-06). Le code de la course ne contrôle pas le crédit — aucune occurrence de « crédit » dans le lanceur, l'amorce ni le registre de la course ; le lanceur de la répétition, lui, a une sous-commande dédiée. La règle est donc tenue par la discipline de l'opérateur, et par ce feu.
Relevé invoqué : 22,64 USD, solde 0, recharge automatique active sous 5 USD, à 2026-11-18T01:57:32Z (R-3124). Ce relevé N'EST PAS vérifiable dans le conteneur de session : l'outil du loueur y est absent (prouvé selon R11 : binaire introuvable, chemin /home/user/vastai-env/bin/vastai inexistant, module Python absent). Un relevé daté est donc refait dans l'heure qui précède la création, et son heure est inscrite.
Contradiction à trancher par Lazar avant la création (§ 12, condition 2) : le feu du 16 novembre déclare la condition des 20 USD remplacée par la recharge automatique, R-3094 et R-3104 la réaffirment, et le mot « recharge automatique jusqu a 75 euros » porte exactement là.

§ 9 — RELANCES
Nombre passé à la garde de création : 2, en onzième argument de la sous-commande « commande ».
Motif, écrit ici parce que la garde ne le dérive d'aucune pièce et ne contrôle que la valeur qu'on lui passe : la relance unique de l'accord original est consommée (premier départ perdu sur la garde du pilote CUDA, instance 60952525, ≈ 0,10 USD ; relance unique, instance 60953606, ≈ 4,23 h, ≈ 5,14 USD, arrêtée sur le contrôle carte-processeur, aucun score écrit). La course de ce feu est donc la course supplémentaire accordée par GO-2026-11-16-11, et c'est la seconde relance au sens de la garde.
Un argument erroné est le seul chemin qui ferait passer une course de trop : la garde l'accepterait. Trois branches de sortie de courses antérieures existent sur le distant (calcul/t07bbis-repetition-v1, -v2, -v4) ; elles ne sont pas ouvertes.
Après cette course, aucune autre n'est permise sans un mot neuf de Lazar : la garde refuse toute troisième relance.
Aucune relance après le samedi 2026-11-21 à 12:00:00Z : au-delà, c'est un nœud, et le billet sort sans l'étape B bis.
Échéance de l'accord, contrôlée par la garde : 2026-11-22T23:59:59Z. Aucune création après.
Échéance dure du programme : le verdict scellé de l'étape B bis est dû au plus tard le dimanche 2026-11-22.

§ 10 — GARDES QUI DOIVENT PASSER, ET QUI ONT ÉTÉ ÉPROUVÉES
Garde de création (lignes du registre propre, feu portant GO-2026-11-14-09, deux relances seulement sous GO-2026-11-16-11 avec fiche de code remplacée, échéances) : éprouvée sur dix cas, cas sain et artefacts, zéro écart. Confrontée à l'état du jour, les six conditions passent.
Garde d'offre (carte, cœurs, mémoire vive, disque, stockage, pilote de l'hôte, étiquette) : éprouvée sur cinq offres fabriquées ; stockage 0,50 refusé, pilote 12,8 refusé, H200 refusée. Le prix, et lui seul, y échappe (§ 6).
Contrôle du pilote de la carte sur la machine, avant l'installation des paquets : éprouvé sur huit cas, zéro écart (sain 13.2 ; bord exact 13.0 ; refus pour 12.8, version absente, citée deux fois, illisible, sortie vide, version tronquée). Aucun essai du dépôt ne le joue : l'essai que l'amorce cite en commentaire n'existe pas (absence prouvée selon R11). Essai à écrire, hors du chemin critique.
Garde de branche de sortie neuve : refuse si la branche existe, refuse si le distant est muet.
Garde d'ancêtre : commit de 40 caractères hexadécimaux, objet présent, tête lisible, ancêtre vérifié ; toutes les voies arrêtent, aucune ne replie en silence.
Garde du registre partagé : une clé de l'étape B bis dans registres/scellements-v1.md fait refuser la création. Zéro occurrence aujourd'hui.
Garde de calcul du dépôt (.claude/hooks/garde_calcul.py, empreinte 73be063822531b27e74cf522794cd262495ba21ceea9b62a41ef4a17879a4850) : éprouvée sur treize cas, zéro écart ; elle refuse toute création payante sans identifiant d'accord dans la commande, tout accord inexistant ou d'un autre type, et tout arrêt par motif de ligne de commande sous ses trois formes. Elle reconnaît aussi l'outil appelé par son chemin complet. Son compagnon d'empreinte est absent : écart R6 à corriger.
Destruction et preuve d'absence : destruction par identifiant numérique seulement, jamais par motif (R10), avec l'option -y (sans elle, l'outil demande une confirmation, abandonne et rend 0 — R-2789) ; identifiant non numérique refusé ; instance d'une autre session refusée. La destruction n'est jamais jugée par un code de sortie : l'absence de l'identifiant est prouvée dans la liste des instances, une instance témoin y étant présente ; liste illisible ou témoin absent, c'est « absence non prouvée », arrêt, destruction et vérification à refaire. Éprouvé sur trois cas sur trois et quatre cas sur quatre.
Portillon des essais sur la machine : 176 essais passés au moins, sinon l'amorce s'arrête à son étape 5.

§ 11 — JAMAIS DÉTRUITES PAR CETTE COURSE, TÉMOINS PERMIS
58936096, 58936099, 58936100, 60480302, 60599797, 60670453 (instances d'autres sessions). Témoin de destruction pris parmi elles.
Également intouchables, relevées à la reprise du 18 novembre : 60988826 (jeu de l'idée du poids du nul, arrêtée), 61049303 (témoin de Bailey, autre session, arrêtée), et le serveur sauvegarde-temoin-bailey-v2 chez l'hébergeur allemand.

§ 12 — CONDITIONS SUSPENSIVES : CE FEU N'ENTRE EN VIGUEUR QUE QUAND LES HUIT SONT LEVÉES
1. Écart d'entropie des graines tranché par Lazar (nœud N-1 ci-dessous), inscrit au registre des accords.
2. Sens du mot « recharge automatique jusqu a 75 euros » et sort de la règle des 20 USD tranchés par Lazar (nœud N-2), inscrits.
3. Trace du pilote de la course versée et scellée : lanceur version 5, sous-commande « commande », offre fabriquée, mode d'essai local, code de sortie 0 et commande de création imprimée. Coût zéro, aucune création.
4. Outil du loueur réinstallé depuis requirements-pilotage.txt dans un environnement dédié, version relevée et inscrite, respect de l'option -y réprouvé sur un cas sain, et crédit relevé dans l'heure qui précède la création.
5. Portillon des 176 essais confirmé sur un clone à histoire complète de la branche de code.
6. Chargement effectif du crochet de garde prouvé DANS la session qui créera, et portée de l'interdiction écrite en R-3114 précisée par écrit par la mère.
7. Nombre de relances arrêté par écrit : 2, avec son motif (§ 9) — fait par ce feu même, à sceller.
8. Opérateur neuf désigné, dans une session interactive capable de répondre à la demande d'autorisation que déclenchera l'étiquette bbis-t07-v1, et qui n'a lu aucun résultat de l'étape B, de 7a, de 7b, de T0.6 ni de P3-bis.

§ 13 — CE QUI ARRÊTE TOUT, SANS REJEU, SANS REFORMULATION, SANS CONTOURNEMENT
Refus d'une permission, du crochet de garde ou du classifieur : arrêt au premier refus, compte rendu en une ligne, rien de relancé.
Refus du lanceur sur l'offre, la branche de sortie, l'ancêtre, le registre ou la garde de création : arrêt.
Prix relu après création au-dessus de 1,40 USD/h : destruction aussitôt par identifiant, puis nœud.
Garde de dépense déclenchée (cumul relevé plus un quart d'heure atteignant 39,50 USD) : destruction aussitôt, par la commande que la garde imprime.
Garde de débit déclenchée (marche projetée au-delà de 11,0 h) : arrêt de l'apprentissage, puis destruction.
Les seize caractères d'empreinte de l'amorce imprimés par le lanceur différant de c8a9e81266a3b2fd : arrêt, rien n'est envoyé.
Échéance de la minuterie atteinte : destruction par identifiant.
Portillon des 176 essais non franchi sur la machine : arrêt à l'étape 5, destruction.
Contrôle du pilote de la carte en échec : arrêt avant l'installation des paquets, destruction.
Contrôle d'identité à dose 0 en échec, artefact non vu à dose 1, chemin de l'état imposé en échec, texte décodé ou clé différents, garde d'équivalence de la série d'origine en échec, contrôle carte-processeur au-delà de 1e-4 à 3 époques, déterminisme au bit près non tenu à 300 époques sur la carte : arrêt selon la liste d'arrêt du texte scellé.
Une tâche du pli lu entrant dans un apprentissage, une moyenne ou une médiane sur les jetons, une aire ou un résumé de score écrit sur l'instance, l'ouverture d'un fichier de la liste « Jamais » : arrêt.
Absence de destruction non prouvée : arrêt, compte rendu, destruction et vérification refaites.
Relance au-delà du 2026-11-21 12:00:00Z, ou création au-delà du 2026-11-22 23:59:59Z : nœud, rien n'est créé.
Toute instance ou tout serveur sans tâche en cours : arrêté par son identifiant, consigné au registre des arrêts.

§ 14 — APRÈS LA COURSE
Destruction explicite de l'instance par son identifiant numérique, avec l'option -y, dans les quinze minutes qui suivent la fin ou l'arrêt ; puis absence prouvée contre un témoin pris au § 11 ; puis inscription au registre des arrêts et au registre des dépenses, avec le prix relu et la durée.
Aucune mesure, aucun score, aucune aire lus par la session de la course. La lecture se fait sur processeur, par un lecteur neuf, sur le plan scellé, qui n'a lu ni le verdict de l'étape B ni son fichier de lecture avant de sceller le sien ; le fichier de lecture de l'étape B n'entre qu'après les deux verdicts, pour la seule table conjointe.
Avant cette lecture, et non avant la course : la preuve d'antériorité rejouée depuis un clone à histoire complète et inscrite à part ; le journal des ouvertures du registre propre créé.
Verdict prononcé par un sous-agent neuf, ni auteur du préenregistrement ni de l'analyse, citant la ligne du premier addendum, sous peine de n'être pas scellé ; puis soumis à Lazar.
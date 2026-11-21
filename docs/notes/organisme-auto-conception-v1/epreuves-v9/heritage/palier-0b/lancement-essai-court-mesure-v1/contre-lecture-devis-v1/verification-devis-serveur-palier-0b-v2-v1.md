# Vérification du devis v2 « serveur loué, palier 0b, essai 3 » — v1

**Verdict : À corriger.** Trois de mes quatre lignes sont corrigées (avec réserves) ; la ligne « chiffres » ne l'est pas tout à fait : la v2 introduit une erreur de diviseur sur la place à n = 2, et recopie une erreur de ma propre contre-lecture (94,8 h au lieu de 94,6 h).

Pièce vérifiée : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/devis-serveur-loue-palier-0b-essai-3-v2.md`, sha256 `384b5d35fd2a800d4dd019293b56bbd4f265040f1b65d5616a95076a514e5592`. Bases : mesure `7605afc3…6d34`, journal de tenue `bbfb4473…a8` (mêmes que ma première lecture). Limite inchangée : le prix de la cpx42 (0,1134 EUR/h, relevé à 18:03Z) n'a aucune pièce ; je ne peux pas le vérifier ; la v2 le dit honnêtement (« seul le prix de la cpx32 est corroboré »).

## Les quatre lignes

| # | ligne | état | preuve |
|---|---|---|---|
| 1 | durée | **Corrigée**, une réserve | § 1 et § 3 : « borne basse » retirée, fourchette 10,7 h à 95 h, durée 96 h, relevé à 6 h avec décision de la mère. Réserve : 95 h n'est pas une borne haute établie (voir pas 5). |
| 2 | chiffres | **Non corrigée entièrement** | IPv4 et heure entamée ajoutées, coût à 96 h et conversion exacts ; mais la place à n = 2 est calculée avec le mauvais diviseur (pas 6 et 7), et 94,8 h est fautif (pas 1). |
| 3 | serveur sans destruction ni versement | **Corrigée, avec réserves** | § 5 : destruction par identifiant, repli à 96 h + 2 h, aveu que l'arrêt n'arrête pas la facturation, versement depuis le poste. Réserves aux pas 10 à 12. |
| 4 | obstacle tu | **Corrigée, avec reliquat** | § 4 : lanceur v3 paramétré (racine, interpréteur, sorties), gardien v4, préparation du serveur. Reliquat au pas 13. |

## Relevé de méthode

### Chaîne de raisonnement

Calculs refaits à la main à partir du journal de tenue (lignes 13, 22, 30, 31, 32) et de la mesure (lignes 3, 4, 7).

1. Fourchette de durée. n = 2 (17:49:47,219) : Δt = 17:49:47,219 − 17:41:01,419 = 8 min 45,800 s = 525,8 s ; 525,8 × 648 = 340 718,4 ; /1 = 340 718 s = **94,64 h**. Ma contre-lecture v1 donnait 94,8 h (Δt compté 526,8 s, une seconde de trop) : **l'erreur est la mienne**, la v2 la recopie (« 94,8 h à n = 2 », § 1). Les autres valeurs se confirment : n = 4 : 1005,8 × 648 / 3 = 217 252,8 s = 60,35 h ; n = 12 : 1065,8 × 648 / 11 = 62 785 s = 17,44 h ; n = 20 : 1125,8 × 648 / 19 = 38 395,7 s = 10,67 h (mesure ligne 8 : 38 417,9 s, Δt pris à l'arrêt du signal, 1126,45 s). Arrondi « 95 h » : tient (94,64 arrondi au-dessus) ; « 94,8 » faux de 0,16 h, sans conséquence sur 95 et 96.
2. Description de l'avancement de n (§ 1). « De 17:46Z à 17:57Z, n reste à 1 ou 2 » : journal : n = 1 jusqu'à 17:48:47, n = 2 de 17:49 à 17:56, n = 4 à 17:57:47. Exact. « De 17:57Z à 17:59Z, n passe de 2 à 20 » : à 17:57:47 n vaut déjà 4 (n = 2 à 17:56:47) ; imprécis, sans effet. « environ 5 600 fichiers par minute » : 49 909 → 55 602 = 5 693 ; 55 602 → 61 296 = 5 694 : exact. « environ 1 500 » : 95 692 − 94 141 = 1 551 ; 97 076 − 95 692 = 1 384 : exact.
3. « Les 20 dossiers lus appartiennent tous au premier bloc (un proposeur, la dose 0) » (§ 1) : aucune pièce citée ; je ne peux pas le vérifier dans les pièces lues (la mesure ne porte pas les noms de dossiers). Supposé.
4. Place à la borne haute. Formule de la mesure : s4 × 648 / (n − 1). À n = 2 : diviseur n − 1 = 1. La v2 écrit « 716 492 800 × 648 / 2 = 232 143 667 200 » : 716 492 800 × 648 = 464 287 334 400 ; /2 = 232 143 667 200 (arithmétique exacte), mais **le diviseur est n, non n − 1**. Avec le diviseur de la formule : **464 287 334 400 octets = 464 Go**, supérieur au disque de 320 Go. La v2 dit que 232 Go est « majorante » : c'est faux sur sa propre base.
5. Avec la vraie valeur de s4 à n = 2 (journal ligne 22 : 337 301 504 octets alloués) : 337 301 504 × 648 = 218 571 374 592, /1 = **218,6 Go**. Marge sur 320 Go : 320 − 218,6 − 3,4 (racine) = 98 Go, avant les archives des étapes (non chiffrées par la v2) ; elle tient, mais ni par la voie écrite ni comme « majorante ». Et la v2 reconnaît (§ 1) que les blocs aux doses 0,25 et 0,5 ne sont pas mesurés : 95 h et 218,6 Go ne sont donc pas des bornes hautes, ce sont les relevés les plus pessimistes observés. Le mot « borne haute » (§ 1, § 3) est trop fort ; la v2 s'en protège par le relevé à 6 h.
6. Coût à 96 h : 0,1134 + 0,00096 = 0,11436 EUR/h ; × 96 = 10,97856 EUR, « 10,98 » exact ; × 1,25 = 13,7232 USD, « 13,73 » exact. Plafond 15,00 USD = 12,00 EUR = 12 / 0,11436 = 104,9 h de vie. Heure entamée : un serveur détruit à 98 h (borne + repli de 2 h) : 98 × 0,11436 = 11,207 EUR = 14,01 USD ; sous 15 USD. Avec une heure de mise en place avant les 96 h : 99 h = 11,32 EUR = 14,15 USD. Le plafond tient, avec environ 6 h de marge de vie, seulement si le repli est respecté.
7. Durée de 96 h contre durée de l'essai : 96 h bornent le gardien ; l'étape 4 projetée à 94,6 h plus l'étape 3 (0,16 h) laisse 1,2 h pour les étapes 5 et 6 et la garde 27 : à la fourchette haute le programme n'a pas fini à l'arrêt. La v2 le traite (relevé à 6 h, décision de la mère, « devis neuf ») ; ce n'est donc pas une promesse d'achèvement, et elle ne la fait pas.
8. Relevé à 6 h (§ 3) : « la session lit n, les fichiers et les octets alloués dans le journal du gardien » : le journal est sur le serveur ; le § 5 et le § 6 disent que la session n'a pas de connexion éprouvée et que tout se fait depuis le poste local. Qui lit, et comment le journal arrive à la session, n'est pas écrit.
9. Destruction. § 5 : « par l'identifiant … consignée dans registres/arrets.md, après versement prouvé » ✓ ; « un serveur arrêté reste facturé » ✓ (aveu utile, correction de mon pas 15) ; « Repli : si personne n'a détruit le serveur 2 h après la borne de 96 h, la mère ou Lazar le détruit par son identifiant » ✓ nommé ; « aucune destruction automatique depuis le serveur » ✓ assumé.
10. Réserve au pas 9 : le repli suppose que la mère peut détruire par l'API ; le devis dit lui-même (§ 6) qu'elle n'a éprouvé aucune connexion sortante vers Hetzner. Le repli repose donc sur Lazar, sans heure de rendez-vous écrite : 96 h + 2 h tombent à un moment que le devis ne date pas.
11. Gardien v4 (arrêt de durée à 96 h) et lanceur v3 n'existent pas encore (§ 4, « à écrire, vérifier ») : la correction de ma ligne 3 est un engagement, pas une pièce. Elle est conforme à l'état du devis, qui conditionne la création à ces trois travaux.
12. Versement (§ 5) : « se fait depuis le poste qui a créé le serveur » : cohérent avec le registre (lignes « poste local »), plus d'aveu manquant. Reste non écrit : le transfert des archives du serveur vers le poste.
13. Obstacle. v1 reprochée : chemins absolus, racine, interpréteur, dossier des sorties codés en dur. § 4 : points 1 (trois chemins en paramètres), 3 (préparation, empreinte du programme `1f04cb46…`), vérification par S. ✓ Corrigé. Reliquat : l'arrivée de la racine à `d7f949ac` (3,4 Go) sur un serveur sans accès au dépôt privé n'est pas décrite (§ 4 point 3 dit « racine à d7f949ac » sans voie). Et « avant la création (sans dépense) » range sous ce titre une préparation du serveur qui ne peut s'exécuter qu'après sa création ; c'est le script qui est écrit avant ; sa durée d'exécution n'est comptée nulle part (elle est dans la marge de 6 h du pas 6).

### Objets de contrôle

Mécanisme éprouvé : le recalcul de la fourchette de durée et de place par la formule de la mesure.
- Objet où la conclusion est fausse par construction : la v2 elle-même à n = 2 pour la place (diviseur n au lieu de n − 1). Prédiction écrite avant : si le calcul est fidèle à la formule, il rend s4 × 648 / (n − 1) = 464 Go. Résultat : la v2 rend 232 Go : le contrôle distingue (la v2 échoue).
- Objet où la conclusion est vraie par construction : la durée à n = 20, formule appliquée à la mesure figée (mesure ligne 8) : prédiction 38 417,9 s ; recalcul : 38 395,7 s avec les relevés du journal à la minute, 38 417,9 s avec Δt de la mesure ; les deux concordent à 0,06 %. Le recalcul passe.
- Mon propre contrôle a échoué une fois (pas 1, 94,8 h) : signalé ci-dessus.

### Premier pas non justifié

Le pas 3 (les 20 dossiers lus appartiennent au premier bloc) : aucune pièce ; ce qui le justifierait : la liste des noms de dossiers de source de la mesure, ou la lecture du programme 3-5-6. Le pas 8 (comment la session lit le journal du serveur) et le pas 10 (le pouvoir de la mère de détruire par l'API) sont aussi sans pièce.

### Mode d'échec affecté

Mes quatre lignes de la première lecture : durée, chiffres recopiés, serveur sans destruction ni versement, obstacle tu ; plus la question « la v2 en casse-t-elle une autre ». Réponse : elle en casse une, la ligne « chiffres », par la place à n = 2 (pas 4) ; aucune autre.

### Trouvaille de côté

- Le contrôle des 320 Go de disque dans la v2 (« couvre la borne haute grossière ») repose sur le 232 Go fautif ; la gardien v4 « arrêt de place gardé » protégera le calcul, mais le choix de la cpx42 doit être justifié par 218,6 Go (voir pas 5), et le palier suivant (cpx52, plus de disque) n'est pas examiné. Non poursuivi.
- Le plafond passe de 6,00 USD à 15,00 USD : l'accord GO-2026-11-21-66 et -69 « plafond sur devis » n'est pas relu par moi (je n'ai pas lu `registres/go.md`).

### Évaluateur et conseil

Ce qui me juge : la session mère. Mes témoins : recalculs à la main, une erreur de ma part retrouvée (pas 1). Par où ma lecture pourrait être jugée bonne sans le mériter : en ne vérifiant que l'arithmétique de la v2, qui est exacte, alors que l'erreur est dans le choix du diviseur.

Corrections demandées : (a) § 1, § 3 : remplacer 94,8 h par 94,6 h ; (b) § 1 : remplacer « /2 … 232 Go » par la formule de la mesure (s4 × 648 / (n − 1)) et dire lequel de 464 Go (s4 à n = 20) ou 218,6 Go (s4 à n = 2) on retient ; justifier les 320 Go en conséquence ; (c) retirer « borne haute » ou dire « relevé le plus pessimiste, blocs 0,25 et 0,5 non mesurés » ; (d) § 5 : dater le repli (heure de rendez-vous de Lazar) ; (e) § 3 : dire comment le journal du gardien arrive à la session pour le relevé à 6 h ; (f) § 4 : dire par quelle voie la racine arrive sur le serveur.

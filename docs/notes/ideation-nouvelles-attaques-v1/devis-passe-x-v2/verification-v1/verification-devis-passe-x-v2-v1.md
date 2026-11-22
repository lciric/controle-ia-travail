# Vérification du devis de la passe X rallongée, v2 (vérificateur neuf)

## Verdict : À corriger

Les chiffres du calcul tiennent et le rejeu est égal à l'octet. Mais :
- trois attributions « (GO-48, transmis) » ne sont pas dans la lettre de GO-48 ;
- la v2 dit GO-48 absent de `go.md`, ce qui est faux ;
- GO-49 et GO-50, postérieurs, rendent fausses ou caduques huit passages (liste au § 5).

Le calcul (pire de lettre 96,80 ; marge 103,20) n'est pas touché. Seul le bloc `luc` du programme (part 125,63 / 136,04) est périmé.

## 1. Rejeu et contrôles

- `python3 -B calcul_devis_passe_x_v2.py` puis `cmp` avec `calcul-devis-passe-x-v2.json` : égal, code retour 0.
- Neuf contrôles dans J (l. 2-12), `nombre_de_controles` : 9 (l. 458). Tous sont calculés dans le programme (l. 260-270). Aucun n'est écrit en dur. La tautologie de la règle Google est sortie des contrôles.
- **Réserve : « aucun vrai par construction » est exagéré.**
  - Le 4 (chaque corps est sous-chaîne de la fusion) est vrai par construction : la fusion est bâtie à partir des mêmes corps. Il ne compare pas à l'octet du fichier d'origine.
  - Le 3 (longueur recomptée) relit la recette de la jointure.
  - Le 8 (somme par clé = total) additionne les mêmes termes.
  - Les contrôles 1, 2, 5, 6, 7 et 9 portent sur des données ou sur des bornes réelles.
  - Le contrôle 9 compare des constantes, mais il est utile.
  - Il faut adoucir la phrase de la l. 9 de la v2. Idéalement, il faudrait ajouter un contrôle du corps contre le fichier source (fichier moins sa ligne de titre).

## 2. Contre-lecture de la v1 : point par point

- **B1 (clé mal citée ; réserve go.md périmée)** : traité pour la clé (R-4852 sous GO-46, GO-45 limité à Fable). **Mal traité** pour la réserve : la réancre sur 734 lignes / `7cdfb9e8…` est elle-même périmée (le fichier compte au moins 737 lignes), et « GO-48 absent » est faux.
- **B2 (charge de Fable, recharge)** : traité. 117 USD, plafonds corrects, deux lectures chiffrées, « point bloquant » tombé, contradiction GO-43/GO-45 réglée par GO-48. La lecture compte payant est conforme à GO-48. Mais tout le chiffrage sur 125,63 / 136,04 est devenu caduc par GO-49.
- **B3 (écart au n° 12)** : traité en forme (lettre et épreuve R5). L'acceptation « (GO-48, transmis) » n'est pas dans GO-48. L'écart a disparu avec GO-49.
- **B4 (moment)** : traité (A / B / C, échéance du 30 novembre conforme à GO-48). Les raisons liées à « course bloquée sur Minuit » et à la chute de la part sont caduques.
- **À noter, cinq contrôles dont un en dur et deux tautologies** : en grande partie traité (§ 1, réserve).
- **À noter, extension de X-3 aux titres** : traité, écart déclaré. L'attribution « accordé (GO-48, transmis) » est absente de GO-48.
- **À noter, « 6 » ambigu** : traité (séparateur « [Pièce k sur 17] » dans l'enveloppe, K-2 (5)). **Non vérifiable** : « pièce 2, point 6 ». J (l. 367) ne montre aucune liste numérotée dans la pièce 2 ; les listes sont aux pièces 1, 4, 7, 9 et 15.
- **À noter, sorties maximales** : traité pour Opus et Sonnet 4.6 (128K, AN l. 7-8, l. 10, l. 12). Les autres restent « à relever », ce qui est déclaré.
- **À noter, pire Google non mesuré (G-3)** : traité par la variable [PIRE-G-PROPOSEUR-X] et la formule de P_X (J l. 1265-1273).
- **À noter, lieux manquants (§ 6) et objection de LQ** : traité au § 5 de la v2 (G-1, G-3, G-6, § 11, enveloppe, A1-A7 pour Kimi, TK l. 31, K-1, X-11, n° 13).
- **À noter, corrections de la phrase sur le lot** : traité (corps seul, titre retiré ; GO-37 et GO-46 cités).
- **À noter, contradiction GO-43 / GO-45** : traité (GO-45 prime, GO-48).

## 3. Nombres cités

Tous les nombres relus renvoient à la bonne ligne de J ou à AN : 96,80 ; 103,20 ; 44,43 ; 8,76 ; 24,85 ; 20 235 ; 21 413 ; 116 717 ; 57,65 ; 117 ; 315,23 ; 325,64 ; 162,23 ; 172,64 ; 89,63 ; 100,04 ; 36,00 ; −36,60 ; 5,91 ; 119,72 ; 16,96 ; 28,65 ; options (96,80 ; 98,50 ; 60,50 ; 54,45 ; 193,60) ; par clé ; par proposeur ; lignes J l. 187-366 et suivantes.

Recalcul à la main : 5,02 ; 4,17 ; 2,51 ; 1,51 ; la borne 116 717 ; les jetons d'entrée.

## 4. Lettre de GO-48 (go.md l. 735) contre les « (GO-48, transmis) »

GO-48 dit seulement :
- échéance de GO-46 portée du 26 au 30 novembre ;
- la passe X peut partir avant la course et sans elle, lue une fois et rapportée à part ;
- Luc lu en compte payant à recharge (remplace « aucune recharge supposée » de GO-30) ;
- GO-45 prime sur GO-43 pour la clé des mathématiques ;
- montant inchangé, 200 USD.

**Conformes** : l'échéance du 30 novembre, la lecture « compte payant », « GO-45 prime », (B) « sans la course, lue une fois ».

**Non conformes (absentes de la lettre de GO-48)** :
- l. 48 : écart à X-3 sur les titres « accordé par la mère » ;
- l. 152 : rôles de la course « bloqués jusqu'au mot du directeur » ;
- l. 191 et 262 et résumé 6 : écart au n° 12 « accepté par la mère ».

La v2 doit ancrer ces trois points à leur vraie source (registre des décisions de la mère) ou les marquer « proposé, non accordé ».

## 5. Effets de GO-2026-11-22-49 et GO-2026-11-22-50

GO-49 : le juge et l'espèce 3 de la course passent sur Luc, part de Luc pour la course portée à 260 USD au plus. GO-50 : « clé d'Anthropic à la place de Minuit : « luc on a dit » ».

Le fichier 7 (additif 2) confirme : Minuit sans rôle, part de 260, L-1 remplacé, L-2 sans objet. Il y traite aussi les deux lignes à part (point n° 2, ouvert) et l'engagement de Luc à 467,60 USD.

Voici chaque phrase fausse ou caduque, avec sa lettre de remplacement.

**(a) En-tête, l. 17-18, et Réserve du résumé ; Réserve 1 ; ligne B1 du tableau des différences.**
- Fausses : « relu à jour (734 lignes, 7cdfb9e8…) » ; « GO-48 n'est pas dans ce fichier … Il faut le réancrer » ; « GO-48 est absent de `go.md` » ; « go.md réancré (7cdfb9e8…, l. 732-733) ».
- Remplacement : « **GO** : `/home/user/main-lecture/registres/go.md`, relu à jour ; GO-42 à la l. 729, GO-45 à la l. 732, GO-46 à la l. 733, GO-48 à la l. 735, GO-49 à la l. 736, GO-50 à la l. 737 (empreinte du fichier à reprendre). » Réserve : « R-4852 n'est pas lu (le registre des décisions est hors de ma liste). » Chaque « (GO-48, transmis) » conforme devient « (GO-2026-11-22-48, go.md l. 735) ».

**(b) Résumé, point 4.**
- Remplacement : « **Luc** porte tout Anthropic (R-4852, sous GO-46) et, depuis GO-2026-11-22-49, les deux rôles de la course qui étaient sur Minuit. Lu en compte payant à recharge (GO-42, GO-48), il engage au pire 449,60 USD : part de la course 260,00 (GO-49, au plus), Fable au moins 117 (GO-45), passe X 72,60. La recharge doit payer 296,60 au-delà du reste de 153, sans compter les deux lignes à part (6 USD, clé à trancher), l'attaquant informé de GO-50 (environ 12 USD) et les demandes 28 à 30, non chiffrées. Le nœud L-2 n'a plus d'objet : la part est fixée. »

**(c) Résumé, point 6, et tableau des différences, ligne B3.**
- Remplacement : « **L'espèce 3 de la passe X est payée sur Luc**, comme son rôle de course (GO-2026-11-22-49) : il n'y a plus d'écart au n° 12, seconde clause. »
- Ligne B3 de la différence : « caduc : plus d'écart (GO-49) ».

**(d) § 4 B1, dernière puce (l. 152).**
- Remplacement : « Les rôles de la course (juge et proposeur de l'espèce 3) passent sur Luc (GO-2026-11-22-49). Minuit ne porte plus aucun rôle de la course (GO-2026-11-22-50 : « clé d'Anthropic à la place de Minuit : « luc on a dit » »). Les deux lignes à part, payées par Minuit avant, ne sont pas nommées par GO-49 : leur clé est à trancher. »

**(e) § 4 B2.**
- Ligne 136,04 et ligne 125,63 du tableau : caduques. Remplacement de la ligne : « 260,00 (GO-49, au plus) | 449,60 | 296,60 | 224,00 ». Les 224,00 sont 260 + 117 − 153, hors passe X.
- Phrase « Sur Luc, la passe X ajoute 72,60 … » : inchangée.
- Bloc « Lecture scellée, sans compte payant » : remplacer l'intitulé par « Lecture sans compte payant, écartée par GO-2026-11-22-48 ; donnée pour mémoire ». Tableau et texte « arrêt n° 11 contre 125,63 », « nœud L-2 » : caduques. Ajouter : « Avec la part fixée à 260 USD (GO-49), L-2 n'a plus d'objet. »
- « **Correction de la v1.** Les 16,96 USD … » : remplacement : « Les 16,96 USD ne s'appliquent plus : la part de la course est de 260 USD (GO-49), supérieure au reste déclaré de 153 USD ; le reste ne borne plus, la recharge paie la différence. Le cas haut des quatre rôles de Luc est de 256,01 USD (additif 2 de v3, non scellé). »

**(f) § 4 B3, premières puces.**
- Remplacement : « Dans la passe X, l'espèce 3 se paie sur Luc ; son rôle de course est aussi sur Luc (GO-2026-11-22-49). **Il n'y a plus d'écart à la seconde clause du n° 12 pour l'espèce 3.** Lettre maintenue pour la table : « Pour la passe X, la clé d'un proposeur est celle de la table de X-11. La seconde clause du n° 12 se lit contre cette table : un appel de passe X présenté sur une autre clé que la sienne est refusé, sans bascule. » »
- Épreuve R5 inchangée : cas sain, l'espèce 3 de la passe X sur Luc part ; artefact, la même requête sur Minuit est refusée.

**(g) § 4 B4.**
- Cellule (A), colonne n° 11. Remplacement : « Ses dépenses s'inscrivent sur Luc avant le départ de la course, contre la sous-part de la passe X (72,60 au pire de lettre), distincte de la part de la course, 260 USD (GO-2026-11-22-49). Le n° 11 de Luc se lit comme compte payant à recharge attesté : il ne refuse pas pour le reste, et la part de la course ne baisse pas. »
- Ligne (C). Remplacement : « **Écarté.** La fin de la génération 3 au 27 novembre est incertaine ; l'échéance de GO-2026-11-22-46 est le 30 novembre (GO-2026-11-22-48) ; le départ de la course demande une échéance neuve (GO-2026-11-20-67 échoit le 22 novembre). La course n'est plus bloquée sur Minuit (GO-2026-11-22-49). »
- Recommandation. Remplacement de « La passe X ne dépend pas d'une course bloquée, et elle n'expose ni … » : « La passe X ne dépend pas du départ de la course, qui reste un nœud à part, et elle n'expose ni le n° 11 ni le n° 12 de la course. » Remarque : le motif « course bloquée » tombe ; (B) tient encore sur le calendrier. La confiance de 0,6 est à réévaluer.

**(h) § 5, lignes X-11 et L-1, et Q9.**
- X-11. Remplacement de « Seconde clause du n° 12 : l'écart de B3. » : « Seconde clause du n° 12 : lue contre cette table, sans écart (GO-2026-11-22-49). »
- L-1. Remplacement de « les rôles de la course restent sur Minuit. L-1 renvoie au complément neuf (§ 6). » : « les rôles de la course passent sur Luc (GO-2026-11-22-49), part fixée à 260 USD au plus ; L-1 (« part relevable à 136,04 au plus ») est remplacé par cette part, et L-2 n'a plus d'objet (additif 2 de v3, non scellé). »
- Q9 : « les options chiffrées sur Minuit tombent » reste vrai.

**(i) § 6.**
- Chapeau « Je ne l'écris pas : la liste seule suit. » Remplacement : « Il est écrit à part : additif 2 au complément de valeurs v3 (non scellé), qui reprend les points 1 à 8 ci-dessous. »
- Point 3 (règle R-4289, L-2). Remplacement : « 3. La règle de la part de Luc, R-4289 : sans objet pour cette course, la part étant fixée à 260 USD (GO-49) ; lots de Fable de GO-45 (au moins 117) et demandes 28 à 30 à chiffrer dans l'engagement de Luc. »
- Point 5. Remplacement : « 5. La part de Luc : 260,00 USD (GO-2026-11-22-49). »
- **Point 7.** Remplacement de « Le blocage des rôles de Minuit, jusqu'au mot du directeur : juge et proposeur de l'espèce 3 (AC l. 56), lignes à part (CV l. 120-130). » : « 7. Le passage sur Luc du juge et du proposeur de l'espèce 3 (GO-2026-11-22-49) ; Minuit sans rôle de la course ; les deux lignes à part, à trancher. »
- Point 8. Remplacement : « 8. La table des clés de la passe X ; aucun écart au n° 12. »

**(j) Tableau « Différence avec la v1 », lignes B1, B2, B3.**
- B1 : « Luc par R-4852, sous GO-46 ; `go.md` réancré ; Minuit sans rôle (GO-49, GO-50) ».
- B2 : « au moins 117 de Fable ; effet chiffré ; part fixée à 260 (GO-49) ; L-1 et L-2 tombent ».
- B3 : « caduc : plus d'écart (GO-49) ».

**Omission à ajouter.** GO-50 met l'attaquant informé (additif 3) sur Luc pour environ 12 USD. GO-45 le disait « non couvert ». Il entre dans l'engagement de Luc, avec les 6 USD de lignes à part (additif 2, § 8.4 : 467,60 USD, 314,60 au-delà de 153).

## 6. Suite

- Le programme `calcul_devis_passe_x_v2.py` doit passer en v3 pour que le bloc `luc` soit calculé avec la part 260 : 449,60 ; 296,60 ; 224,00. Aucun de ces nombres n'est dans J aujourd'hui. Je les ai recalculés à la main.
- Le reste du calcul (96,80, 103,20, entrée, options) n'a aucune raison de bouger.

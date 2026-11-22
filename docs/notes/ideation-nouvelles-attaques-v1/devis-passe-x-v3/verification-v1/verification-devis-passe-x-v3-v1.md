# Vérification du devis de la passe X rallongée, v3 (vérificateur neuf, même que pour la v2)

## Verdict : Conforme avec réserves

Tous les remplacements demandés sont portés. Le rejeu est égal à l'octet. Les douze contrôles sont calculés, et leur épreuve sur artefacts tombe douze fois sur douze. Aucun chiffre du devis ne bouge.

GO-54 (go.md l. 741), postérieur à la v3, rend toutefois quatre passages faux ou périmés. Ce sont des corrections de lettre, listées au § 4. Elles sont à faire avant le scellement.

## 1. Rejeu

- `python3 -B calcul_devis_passe_x_v3.py` vers le chemin demandé : code retour 0, `cmp` avec `calcul-devis-passe-x-v3.json` égal.
- Les compagnons `.sha256` de la note, du programme et du JSON sont égaux aux empreintes recalculées (je les ai lus par leur chemin exact, hors de ta liste).
- Les renvois « J l. n » de la note sont tous exacts. J'ai vérifié : 2-15, 3, 4, 9, 192, 193, 363-368, 370-419, 425, 462-536, 538, les cinq options, 1345-1374, 1630, 1652, 1662, 1670-1671, 1677.
- Chiffres recalculés : 260 + 117 + 72,60 = 449,60 ; − 153 = 296,60 ; 377 − 153 = 224,00 ; 467,60 ; 314,60 ; 555,96 ; 402,96. Ils égalent ceux de A2 (JSON du fichier 4).
- Le programme écrit en mode `"x"` : il refuse d'écraser une sortie existante.
- Les contrôles 11 et 12 lisent le JSON de A2 (empreinte `95b40466…`, égale à celle que la note cite).

## 2. Remplacements de ma vérification v2

- § 1 (contrôles) : **porté**. La note nomme les contrôles 3, 4 et 8 comme vrais par construction. Le contrôle 10 compare les corps au fichier source, à l'octet.
- § 4 (trois « GO-48, transmis » hors lettre) : **porté** par la formule « accordé par la mère dans un message de coordination du 2026-11-22, non inscrit à GO-48 ». Le choix est acceptable. Cette provenance reste non vérifiable par moi. La phrase de la ligne 50 est redondante (« accordé par la mère (accordé par la mère dans … ») : cosmétique.
- § 5 (a) : **porté** (l. 19, Réserve, lignes B1 et « Différence avec la v2 »), mais voir le § 4 ci-dessous. Les trois « GO-48 » conformes sont réancrés sur « go.md l. 735 ».
- § 5 (b) : **porté** mot pour mot (résumé 4).
- § 5 (c) : **porté** (résumé 6 ; ligne B3 des différences).
- § 5 (d) : **porté**, avec une phrase ajoutée (le blocage de la v2 est levé par GO-49).
- § 5 (e) : **porté** :
  - ligne « 260,00 | 449,60 | 296,60 | 224,00 » ;
  - deux lignes de plus (467,60 / 314,60 et 555,96 / 402,96) ;
  - intitulé de la lecture sans compte payant ;
  - « (caduc) » ;
  - phrase sur L-2 ;
  - remplacement du « 16,96 » mot pour mot.
- § 5 (f) : **porté** mot pour mot, lettre de la table et épreuve R5.
- § 5 (g) : **porté**, cellule (A), ligne (C) et recommandation. Le motif « course bloquée » est retiré, la confiance reste « à réévaluer ».
- § 5 (h) : **porté** (X-11, L-1).
- § 5 (i) : **porté** (chapeau, points 3, 5, 7, 8).
- § 5 (j) : **porté** (lignes B1, B2, B3).
- Omission (attaquant informé de GO-50, environ 12 USD) : **portée**, au § 4 B2 et dans la ligne 467,60.

## 3. Contrôles et épreuve sur artefacts

- Les douze contrôles sont calculés. Aucun n'est écrit en dur.
- Épreuve : chacun est rejoué sur une copie altérée et tombe (J l. 370-419). Les altérations sont réelles :
  - un octet change dans la source de la pièce 5 ;
  - une empreinte change ;
  - un signe est ajouté ;
  - une tentative est à 6,06 ;
  - la borne augmente d'un jeton ;
  - le total de A2 augmente d'un centime ;
  - la part de Luc de A2 est posée à 259.
- Réserves sur la méthode :
  - Les contrôles 3, 4 et 8 restent vrais par construction. La note le dit.
  - Les 11 et 12 comparent à un fichier non scellé, issu de la même coordination (la note le dit, Réserve 6).
  - L'épreuve compte une exception (`KeyError`, `ValueError`, `IndexError`) comme une chute. Ce n'est pas un faux positif dans les cas rejoués.

## 4. Effets de GO-54 (go.md l. 741) et des GO-52, GO-53

GO-54 : ligne GO-2026-11-20-67 (456 USD) prolongée au 30 novembre ; part de Luc 260 USD ; « aucune recharge supposée » remplacé ; lignes à part de 6 USD **sur Luc hors des 260** ; garde de départ « prêt / manque » accordée.

La marge de 260 est gardée : la part reste « 260 au plus ». La v3 cite le cas haut des quatre rôles (256,01) sans en tirer la marge de 3,99. Rien n'est faux.

Voici ce que GO-54 rend faux ou périmé, avec la lettre de remplacement.

1. **Lignes à part « clé à trancher ».**
   - Passages : B1, dernière puce (« leur clé est à trancher ») ; résumé 4 (« 6 USD, clé à trancher ») ; § 6 point 7 (« lignes à part, à trancher ») ; JSON `luc.entrees.lignes_a_part.source` et `luc.note` (programme l. 109 et l. 262).
   - Remplacement de B1 : « Les deux lignes à part (6 USD), payées par Minuit avant, passent sur Luc, hors des 260 USD de la part de la course (GO-2026-11-22-54). »
   - Remplacement du résumé 4, fin : « …la recharge doit payer 296,60 au-delà du reste de 153. Avec les deux lignes à part (6 USD, sur Luc hors des 260, GO-54) et l'attaquant informé de GO-50 (environ 12 USD), l'engagement au pire est de 467,60 USD, 314,60 au-delà de 153 ; les demandes 28 à 30 ne sont pas chiffrées. »
   - Remplacement du § 6 point 7 : « …Minuit sans rôle de la course ; les deux lignes à part sur Luc, hors de la part de 260 (GO-2026-11-22-54). »
   - Ligne du tableau B2 : la ligne « 260,00, avec les lignes à part (6) et l'attaquant informé (12) | 467,60 | 314,60 » devient la ligne de référence, car GO-54 accorde les lignes à part.
2. **B4, ligne (C).** La phrase « le départ de la course demande une échéance neuve (GO-2026-11-20-67 échoit le 22 novembre) » est périmée. Remplacement : « la ligne de course de 456 USD (GO-2026-11-20-67) est prolongée au 30 novembre (GO-2026-11-22-54) ; la fin de la génération 3 au 27 novembre reste incertaine. »
3. **Ancrage de `go.md` (l. 19 et ligne « Différence avec la v2 »).** « 738 lignes, `358b3262…` » est périmé : le fichier compte 741 lignes (`bfa102cd920cae44…`). Remplacement : « GO-48 à la l. 735, GO-49 à la l. 736, GO-50 à la l. 737, GO-54 à la l. 741 ; empreinte `bfa102cd…`, 741 lignes ; seules les l. 729-737 et 739-741 ont été lues. »
4. **Recommandation (B) et confiance 0,6.** Le motif « calendrier » s'appuie sur une ligne de course qui échoit le 22. GO-54 la prolonge au 30 et dit « on la lance tout de suite » ; GO-52 met la passe X « devant tout le reste ». La recommandation n'est pas fausse, mais elle est à réévaluer par la mère. La v3 écrit déjà « à réévaluer ».

**GO-53 (120 USD, collisionneur) et GO-52 (« go luc »).** GO-53 ne nomme aucune clé. Si une part de ses 120 USD passe par Luc, l'engagement de Luc monte. La v3 ne le compte pas. Je ne peux pas le trancher. À signaler à la mère comme réserve de la v3. GO-51 (l. 738) n'est pas lu.

## 5. Ce qui reste hors de portée

- R-4852 : non lu.
- La provenance du message de coordination qui accorde l'écart sur les titres : non vérifiable.
- « Pièce 2, point 6 » : non vérifiable par J (Réserve 7 de la v3).
- L'identité et les sorties maximales des espèces 3 et 4, de Google, d'OpenAI et de Kimi : à relever (déclaré).

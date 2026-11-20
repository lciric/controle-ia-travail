# Vérification des corrections de l'additif 1 « relance des six instances » (barreau 5) — sur la v2

Pièces lues :
- l'additif v2, sha256 4f785bd9faffba600e79975e0a9d1448859fa43fb789039f8d3c649ece151b9d (vérifiée, égale) ;
- le rapport du développeur v3 ;
- le différentiel du code v3 depuis le code v1, sha256 1db0fe39…cf36e (égal au rapport) ;
- la contre-lecture du code v2 ;
- les lignes GO-2026-11-20-52, -59 et -60 du registre des accords, sur `origin/main`.

Rien d'autre, dans les mêmes interdits.

**Verdict : scellable après ces couples.** Les douze couples sont levés, et aucune correction n'introduit d'erreur de fond. Il reste un couple important : la forme exacte de la mention du code des relances et le contrôle de la ligne avant de la commettre, puisque la ligne ne se réécrit pas. Les quatre autres couples sont mineurs. Ce sont des retouches de texte, que la mère peut vérifier par différentiel.

## Table : couple → levé ou non

| couple de la contre-lecture v1 | levé ? | où, et ce que j'ai vérifié |
|---|---|---|
| 1. Premières copies non versées (bloquant) | levé | § 1, quatrième tiret ; C8 ; ligne de la table ; § 3. L'écart est rattaché à GO-2026-11-20-51, point 2. L'affirmation fausse « versées » a disparu. |
| 2. Le § 6 faisait du code un nœud (bloquant) | levé | C5 nomme les suites (essais, plancher de l'amorce, commentaires). Le § 6 les exclut. Le code v3 n'a rien d'autre : `engagement_v1.py` est inchangé (même blob que le code de lecture figé), `MIN_ESSAIS` vaut 244, et le lanceur ne change que dans ses commentaires. |
| 3. Réserve de la relecture, répétition (important) | levé | Seuil de 24 = 200 − 147 − 21 − 8, juste. Le seuil repose sur des coupures, non sur des coûts estimés : le quart d'heure n'ampute donc plus la relecture. Les coupures renvoient au devis scellé (chemin et empreinte, § 4). L'interdit sur la répétition et le stockage est écrit, et le chiffre de 18,5 sans renvoi est retiré. Voir le couple N5. |
| 4. Imputation à Lazar ; « go 30 usd » (important) | levé | La ligne GO-2026-11-20-52 porte « go 30 usd », avec un plafond de 30 USD, pour le collisionneur du papier « dopamine » : c'est étranger à la formation, et l'additif le dit. La rédaction de la mère est nommée comme telle, puis accordée par GO-2026-11-20-59 (2). |
| 5. Ligne avant la première création (important) | levé | C7, § 3, § 4 point 2, et la table : avant 2026-11-21T07:30:16Z ; H + 54 heures reste sans effet. |
| 6. Passages remplacés (important) | levé | La table de la fin de la section 2 est complète sur la relance, la borne, la dépense, le point 14, le gel du code et le registre. Le libellé neuf du point 14 est écrit en C4, et le § 3 renvoie à ce point réécrit. Voir le couple N4. |
| 7. Écarts non dits par Lazar (important) | levé | GO-2026-11-20-59 (2) accepte les trois écarts, que GO-2026-11-20-60 (2) confirme un par un. Ils sont cités à l'en-tête, en C1, C4, C5 et C6. Voir le couple N2. |
| 8. C1 trop générale (mineur) | levé | C1 nomme les six instances et l'arrêt de 12:12Z ; « avant qu'une famille soit formée » est retiré. Le code refuse en plus l'instance 6 (`INSTANCES_TOMBEES`). |
| 9. Contenu exact de la ligne (mineur) | levé | § 5 côté session ; le code tient en plus la liste des instances tombées. |
| 10. Validité de GO-2026-11-19-86 (mineur) | levé | § 5 : vérification avant l'inscription ; sinon, nœud. |
| 11. Lectures, chiffres, H (mineur) | levé | Les lectures sont complétées ; H = 2026-11-20T01:30:16Z est écrite ; le chiffre de 18,5 est retiré. |
| 12. Chemin de scellement, R12 (mineur) | levé | Le chemin est proposé à l'en-tête, et la ligne de relance en cite le chemin et l'empreinte. L'exception à R12 est écrite en C5, et sa consignation est confiée à la mère. |

## Accord entre l'additif v2 et le code v3

J'ai vérifié sur le différentiel que l'additif v2 et le code v3 disent la même chose :
- **aucune clé neuve** au registre ;
- **la mention du code des relances**, « `code des relances commit <40 signes>` », est lue dans la référence. Elle doit y être une et une seule, et les mots « code des relances » ne doivent pas y paraître ailleurs (`ref.count`). Son commit doit différer de celui de `CODE-FORMATION-B5F`, et le code vérifie la filiation à la commande comme sur l'instance ;
- **l'accord** de la ligne doit être égal à celui de `GO-FORMATION-B5F` ;
- **les instances** : six au plus, 147 dollars au plus, et les seules instances tombées ;
- **les deux compteurs** valent pour toute marche ;
- **l'entropie** est inchangée.

La ligne proposée au rapport, § 7, une fois complétée avec le chemin proposé, une empreinte et un cumul, fait 529 signes. Elle reste sous 600.

## Couples neufs

**N1. La forme exacte de la mention, et un contrôle obligatoire avant d'inscrire la ligne.**
- Constat. C5 dit « séparée du reste par « ; » ». Le code exige davantage. Son expression régulière, `(?:^|; )code des relances commit ([0-9a-f]{40})(?= ;|$)`, veut un point-virgule entouré d'espaces, ou le bord de la référence. Une référence écrite « …sha256 X;code des relances commit … » serait refusée par le code. Or la ligne ne se réécrit pas et ne se double pas : une ligne mal formée rendrait toute relance impossible sans nœud, à quelques heures de H + 30. Le rapport v3, § 7, prévoit un contrôle avant de commettre la ligne, mais l'additif ne l'impose pas.
- Correction. En C5, remplacer « séparée du reste par « ; » » par « séparée du reste par « ␣;␣ » (point-virgule entouré d'une espace de chaque côté), ou placée en tête ou en fin de la référence ». En § 5, côté session, ajouter : « avant de commettre la ligne de relance, lire le registre candidat (registre de la branche principale plus cette ligne) par `lire_code_et_accord` du code des relances vérifié (rapport du développeur v3, § 7) ; refus : ne pas inscrire, corriger d'abord ».
- Gravité : important.

**N2. La clé neuve que mentionne l'accord.**
- Constat. GO-2026-11-20-59 (2) accorde « clé neuve et code changé après le gel ». L'additif cite seulement « le code de formation changé après son gel ». Ce n'est pas faux, puisqu'il emploie moins qu'il n'est accordé, mais un lecteur qui confronte la citation à la ligne verra un écart.
- Correction. À l'en-tête, après « le code de formation changé après son gel (C5) », ajouter « (l'accord nomme aussi une clé neuve ; elle n'est pas employée : C5) ».
- Gravité : mineur.

**N3. Les lignes de la lecture qui restent.**
- Constat. Le § 4, point 3, dit « puis les lignes de la lecture ». Or `CODE-LECTURE-B5F` et `EPREUVE-B5F` sont déjà inscrites (§ 1).
- Correction. Écrire « puis celles des lignes de la lecture qui restent : `GO-LECTURE-B5F`, `SCORES-B5F`, `OUVERTURE-B5F`, `LECTURE-B5F`, `VERDICT-B5F` ».
- Gravité : mineur.

**N4. Le passage « la référence est libre » n'est pas nommé.**
- Constat. Le texte dit, sous « Lignes de registre », que « la référence est libre (ni « | » ni saut de ligne) ». Le code des relances lit désormais, à la lettre, une mention dans la référence de la ligne de relance. La dernière ligne de la table vise le « format de `GO-RELANCE-FORMATION-B5F` », sans nommer ce passage.
- Correction. Dans la colonne de gauche de cette ligne, ajouter « ; « la référence est libre » » ; dans celle de droite, ajouter « sauf la mention du code des relances, lue à la lettre (C5) ».
- Gravité : mineur.

**N5. Les deux coupures de 21 et de 8 dollars ne sont lues par personne de nommé.**
- Constat. Le rédacteur déclare ne pas avoir lu le devis. Les coupures de 21 dollars (relecture) et de 8 dollars (répétition) sont données par la mère. Le renvoi par chemin et empreinte satisfait la règle d'empreinte (R6), mais rien ne dit qui les a relevées dans le devis. Je n'ai pas pu les vérifier non plus : le devis n'est pas dans mes lectures permises.
- Correction. À l'en-tête, remplacer « données par la session mère » par « relevées par la session mère dans le devis scellé, section 4, et vérifiées par elle avant le scellement de l'additif » ; et que la mère fasse cette vérification.
- Gravité : mineur.

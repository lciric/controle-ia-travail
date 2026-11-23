# Vérification des corrections du concepteur des sondes v2 (v1)

- **Pièce vérifiée** : branche `prep/sondes-v2-concepteur-opus-v1`, commit `af6e2070b`. Réponse point par point `reponse-contre-lecture-concepteur-v1.md` (`11b6ff39…`, empreinte recalculée) ; décisions v2 ; plan et devis v2 ; vérités v4, projet v2 ; trois spécifications v2 ; `calculs/` (deux scripts et leurs sorties) ; passation additif 1.
- **Rapport de départ** : `contre-lecture-concepteur-sondes-v2-v1.md` (`d20bb4c0…`), même branche que ce fichier, commit `7bfcfc536`.
- **Vérificateur** : le même contre-lecteur (sous-agent Opus 5.5, session mère `session_013QMayjbmQUdDuDs2S3i3XD`), 2026-11-23 vers 06:15Z (`date -u`), sous les mêmes interdits : aucune branche `coffre/*`, `verdict/*`, `calcul/*`, `lecture/*` ; rien sous `diag/` ni `runs/` ; aucun chemin contenant « coffre », « verdict » ou « sel ». Calculs refaits de façon indépendante, sur le modèle de coût écrit et sur une loi binomiale, sans aucune donnée.

## Verdict

**Conforme, deux réserves mineures.** Les dix défauts sont corrigés : huit entièrement, deux pour l'essentiel (2 et 5), chacun avec un reste mineur (ci-dessous). Les calculs du devis v2 et des plafonds de puissance sont exacts. Rien n'empêche l'erratum de code ni l'additif de commit.

## Défaut par défaut

| défaut | état | constat |
|---|---|---|
| 1, majeur : extension non chiffrée | **corrigé** | ligne « extension » : 1 305 heures, 47,4 USD (67,8) pour l'étalon seul ; 1 335 à 1 590 heures avec le mode complet ; devis neuf et GO neuf si la note la déclenche ; option (iii) bien classée comme nœud. Mineur : « d'un facteur cinq à sept » (plan v2, § 5, Enjeu) ; le rapport réel, extension et mode complet contre le scénario recommandé, va de 3,2 (très grand) à 7,2 (petit). |
| 2, majeur : E-8, cas mixte | **corrigé pour l'essentiel** | précision limitée au cas « toutes les tâches contrôlées » ; cas mixte en nœud conditionnel, porté à Lazar **avant l'épreuve** (spécification de la note v2) ; phrase trop forte retirée. **Reste (mineur)** : l'erratum de code (§ 7, point 4) fait encore calculer et rapporter « sans libellé » les deux lectures du cas mixte quand `regle_cas_mixte` n'est pas fixé. Lire les deux valeurs avant de choisir la règle permettrait un choix sur résultat. Le nœud étant tranché avant l'épreuve, ce repli ne devrait jamais servir : il doit être un **arrêt nommé** (« règle du cas mixte non fixée »), non un calcul. |
| 3 : testabilité et résolution du nul tiré | **corrigé** | règle max(2^(1−P), 1/(1 + R)) > α dans les décisions, les vérités et l'erratum ; table des plafonds juste (voir ci-dessous) ; au moins 999 rejeux ou énumération exacte pour une marche à 99 %. |
| 4 : contrôles de signe hors des vérités | **corrigé** | deux critères, nature « garde », borne haute 0,10, dans les mondes « interaction » et « interaction contraire » ; conséquence écrite d'avance (ligne « non testable » ; toute correction de code après l'épreuve est un nœud) ; déclarés dans l'additif. |
| 5 : case du rejeu sans Holm ; familles inégales ; actions moyennes | **corrigé pour l'essentiel** | lecture à deux seuils sur les mêmes valeurs p (α pour les fausses lectures, α / D pour la puissance) ; D lu dans la note (`nombre_de_doses`) ; trois approximations nommées dans l'additif et dans les spécifications. **Reste (mineur)** : le critère scellé du monde « décalage de chemin » (« interaction brute établie dans au moins 80 % ») passe de la lecture à α à la lecture à α / D (`interaction_brute_holm`, borne basse 0,8). C'est la lecture fidèle à la lecture réelle, et plus stricte : elle ne peut que retirer un libellé. Mais c'est la manière d'appliquer un critère scellé. La liste du § 6, point 1, ne la nomme pas en toutes lettres ; elle doit y figurer (« le critère du décalage de chemin se lit au seuil α / D du premier pas de Holm ; à D = 1, rien ne change »). |
| 6 : scénario « petit » | **corrigé** | 276 et 185 heures. |
| 7 : ce que le contraste rejette | **corrigé** | décisions v2, § 1 ; erratum, point 1. |
| 8 : transport de l'objection au rejeu croisé | **corrigé** | phrase juste ; limite de l'épreuve (vers 7 %) écrite. |
| 9 : classe des spécifications | **corrigé** | trois spécifications v2 en classe B ; règle des cases déclarée. |
| 10 : option (c) | **corrigé** | gain d'exactitude, non de coût ; plis internes et réglage fixés. |
| § 4, point 1 : conditions de la jonction tardive | **corrigé** | conditions reprises (spécification de correspondance v2). Le retrait du défaut à 48 heures est juste : un écart à un texte scellé est un nœud. |

Pas d'autre changement relevé hors des corrections annoncées. Les vérités v4, projet v2, nomment deux lectures neuves (`interaction_holm`, `interaction_brute_holm`) que le chargeur actuel refuserait : c'est attendu, l'erratum de code (point 5) les ajoute à `CRITERES` ; à vérifier à la contre-lecture de l'erratum.

## Calculs refaits

**Devis v2** (modèle écrit : étalon, 1 300 × (0,52 + 0,0034 × TA) secondes plus 6 × 50 secondes par réplique ; mode complet, 8 × 108,6 × (TA/24)^1,09 secondes par réplique, facteur 0,06 + 0,94 × 39/199 ; 500 répliques ; 0,0363 USD par cœur-heure, 0,0519 au plus haut). Le recalcul retrouve chaque ligne de la sortie jointe à l'unité près : 276 et 185 ; 432 et 238 ; 761 et 348 ; 1 378 et 498 heures ; extension 1 305 heures, 47,4 USD (67,8) ; extension avec le mode complet 1 335, 1 368, 1 439 et 1 590 heures, 48,5 à 57,7 USD (69,3 à 82,5) ; part de la sonde d'identité dans l'extension 0,745 ; 819 et 576 heures si elle va deux ou quatre fois plus vite.

**Plafonds de puissance du contraste** (b binomiale (R, q), q = 2^(1−P) ou 2^(−P), lecture si b ≤ α(1 + R) − 1) : 0,655 et 0,876 (6 paires, 39 rejeux, 5 %) ; 0,963 et 0,990 (8 paires, 39 rejeux, 5 %) ; 0,904 et 0,999 (6 paires, 199 rejeux, 5 %) ; 0,539 et 0,817 (8 paires, 199 rejeux, 1 %) ; non testable à 1 % avec 39 rejeux. Testabilité : 6 paires à 5 % (39 ou 199 rejeux), 8 paires à 1 % (199 rejeux). Tout est exact.

## Pour Lazar : montant du devis à soumettre

Option recommandée (grille de l'étalon telle que codée, mode complet à 39 rejeux), `ccx63` à `hel1` :
- **estimation** : 185 à 498 heures de processeur, soit **6,70 à 18,10 USD** au prix relevé le 11 novembre (9,60 à 25,90 au prix le plus haut), selon les effectifs que donnera la note ;
- **plafond proposé** (1,5 fois l'estimation) : **au plus 27,10 USD** (38,80 au prix le plus haut), fixé à la valeur exacte quand la note des effectifs sera connue.
- **hors de ce GO** : si la note déclenche l'extension de la grille, devis neuf : 1 335 à 1 590 heures, 48,50 à 57,70 USD (69,30 à 82,50 au plus haut), avant tout gain de vitesse.

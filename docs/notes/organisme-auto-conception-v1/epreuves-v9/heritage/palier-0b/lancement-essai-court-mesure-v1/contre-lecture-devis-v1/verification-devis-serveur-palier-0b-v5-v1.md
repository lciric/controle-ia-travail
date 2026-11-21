# Vérification du devis v5 « serveur loué, palier 0b, essai 3 » — v1

**Verdict : Conforme**, avec deux réserves de rédaction qui ne cassent rien. Mes trois corrections demandées pour la v4 sont portées ; la v5 ne casse aucune de mes quatre lignes d'origine.

Pièce vérifiée : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/devis-serveur-loue-palier-0b-essai-3-v5.md`, sha256 `452e7bcf7c38f75a6365323cf505be61ef24ed9c7c84324cc4946fa90f3647fb`. Bases : journal de tenue `bbfb4473…a8`, mesure `7605afc3…6d34`, complément 1 v3 (extrait de `origin/main` dans mon dossier). Non vérifié : le prix de la cpx42 (0,1134 EUR/h, aucun appel permis, aucune pièce ; la v5 le dit) ; `registres/go.md` non relu ; les chemins `sourd-egal/0.0/0` à `19` (hors de mon périmètre de liste).

## Trois lignes

| correction demandée | état | ligne de la v5 |
|---|---|---|
| H0 + 94 h dit avant le relevé pessimiste ; l'étape 4 ne finit pas dans ce cas ; relevé à 6 h pour le savoir | **Portée** | § 3, ligne 21 : « C'est avant le relevé le plus pessimiste : étape 3 (0,16 h) plus étape 4 … (94,6 h) font 94,8 h … Dans ce cas, l'étape 4 ne finit pas … le relevé à 6 h sert à le savoir tôt » |
| « inventaires et compagnons » au lieu de « sorties » | **Portée** | § 3, ligne 22 : « versement des inventaires et compagnons de chaque étape et des journaux » ; les sorties de l'étape 4 « perdues à la destruction, ce qui est dit au rapport » |
| 37,6 Go sourcés | **Portée** | § 6 (c) : « 37,6 Go libres à la fin de l'essai court, journal de tenue, ligne de 17:59:47Z » |

## Relevé de méthode

### Chaîne de raisonnement

1. Étape 3 : 17:31:41,79 → 17:41:01,42 = 9 min 19,6 s = 0,155 h (journal ligne 1, mesure ligne 3). Étape 4 à n = 2 : 525,8 × 648 = 340 718,4 s = 94,644 h (journal ligne 22). Somme : 94,80 h (v5 : « 94,8 h ») ; 94 < 94,8, donc l'arrêt à H0 + 94 h est bien avant, même sans mise en place. La phrase de la v5 est exacte (correction 1).
2. Cas favorables : 10,7 h et 17,4 h plus 0,16 h tiennent dans 94 h ; « les cas mesurés plus favorables tiennent » : exact. Cas non mesurés (étapes 5 et 6, garde 27) : annoncés hors fourchette (§ 1, ligne 9).
3. Couvrir le cas pessimiste : arrêt vers H0 + 100 h, destruction vers H0 + 104 h : 104 × 0,11436 = 11,893 EUR ; × 1,25 = 14,868 USD (« 14,87 ») ; 105 h : 12,008 EUR ; × 1,25 = 15,010 USD (« 15,01 », au-dessus du plafond de 15 USD). Exacts ; refusé « au choix de la mère » : honnête.
4. Coût : 96 × 0,11436 = 10,97856 EUR, 13,7232 USD ; 98 × 0,11436 = 11,207 EUR, 14,009 USD ; plafond atteint à 12 / 0,11436 = 104,9 h. Exacts, inchangés.
5. Correction 2. Règle du complément 1 v3 (« Tenue du lancement ») : « pour l'étape 4, l'archive seulement si la place libre dépasse sa taille de 4 Go ». Place libre au relevé pessimiste : 320 − 3,4 − 218,6 = 98 Go, inférieure à 218,6 + 4 = 222,6 Go : pas d'archive ; la v5 le dit (« elles ne partent pas et sont perdues à la destruction »). Cohérent avec la règle citée.
6. Correction 3. Journal ligne 32 (17:59:47) : `libres=37567504384` octets = 37,57 Go, arrondi à 37,6 Go. Exact et sourcé.
7. Réserve A (rédaction). § 3, ligne 22 : les sorties de l'étape 4 « ne partent que si la place libre dépasse leur taille de 4 Go ». Dans le complément, c'est la création de l'archive (sur le serveur, hors dépôt) que cette règle conditionne, pas son envoi vers le poste. La v5 ne dit pas comment l'archive, quand elle existe (par exemple à 24,4 Go), quitte le serveur dans la fenêtre de 4 h, ni qu'elle y reste sinon. À préciser ; sans effet sur le coût ni sur l'ordre destruction/versement (la destruction prime à H0 + 98 h et écrit ce qui n'a pas été versé).
8. Réserve B (rédaction). « Le relevé à 6 h sert à le savoir tôt » : la v5 dit elle-même (§ 1) que n avance par paquets et que la formule donne de 10,7 h à 94,6 h selon l'instant ; le relevé à 6 h donnera donc une estimation, pas un savoir. Écrire « sert à l'estimer tôt ». Sans effet sur la décision, qui reste à la mère.
10. Rien d'autre ne casse : lignes de coût, plafond, voie de la racine (§ 6 (a), copie sans accès déposé), t3 au relevé (§ 3, ligne 26 ; § 6 (a)), ordre destruction/versement (§ 5), « borne » absent hors « non une borne établie » (ligne 9) : relus, inchangés depuis la v4 vérifiée.

(Le numéro 9 est omis par erreur de numérotation, non de contenu.)

### Objets de contrôle

Mécanisme : le contrôle de cohérence des heures fixes (94 h, 98 h) contre la marche pessimiste (94,8 h). Objet où la conclusion est fausse par construction : le cas de la v4 (« au-delà du relevé pessimiste ») ; prédiction avant : la v5 doit renverser la phrase ; résultat : elle écrit « avant … l'étape 4 ne finit pas ». Objet vrai par construction : le cas à n = 20 (10,7 h + 0,16 h = 10,9 h ≤ 94 h) : la v5 écrit « tiennent ». Le contrôle distingue les deux : il aurait échoué sur la v4.

### Premier pas non justifié

Le pas 2 (les cas non mesurés : étapes 5, 6, garde 27) : leur durée n'est pas mesurée ; ce qui la justifierait : une mesure ou la lecture du programme. La v5 les nomme hors fourchette.

### Mode d'échec affecté

Les trois corrections demandées pour la v4, plus « la v5 casse-t-elle autre chose ». Réponse : non ; deux réserves de rédaction (pas 7 et 8).

### Trouvaille de côté

Aucune nouvelle. Le point ouvert reste celui que la v5 assume : la présence du poste local de Lazar à H0 + 98 h, sans destruction automatique.

### Évaluateur et conseil

Ce qui me juge : la session mère. Mes témoins : recalculs à la main, tous concordants avec la v5. Je pourrais être jugé trop indulgent si l'on estime que la présence du poste à une heure fixe de quatre jours est un défaut ; je l'ai classée comme réserve assumée par la v5 depuis la v3, non comme casse nouvelle.

Corrections facultatives : (a) § 3, ligne 22 : dire que l'archive de l'étape 4, quand elle est créée, est envoyée au poste ou reste sur le serveur ; (b) § 3, ligne 21 : « estimer » au lieu de « savoir ».

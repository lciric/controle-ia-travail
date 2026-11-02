# A1 — verdict, nœuds et application de la règle des trois temps — v1

2 novembre 2026, 16:05 UTC (heure relevée par `date -u`), session conv-audit (R-1259).

## Verdict (lecteur neuf, R13 ; `brouillons/a1-lecture-v1/verdict-a1-v1.md`, sha256 `795e5e992d65bce3096d78f1cd4c36c95cdfc00cdeb40f6259278275e92d3909`, scellé ; audit écrit `rapport-audit-a1-v1.md`, `a886904d…`)
- **W1 : « non jugeable (instrument en défaut) »** : aucune brèche (1/24 sous v8 avec retour, Wilson [0,007 ; 0,202]) ; dents (11/24 sous v7) ; part de lois distinctes 0,497 < 0,50. Le défaut vient de la perte du bras Kimi par le relais, non du proposeur ; aucune lecture admissible de cette course ne dit « résiste ».
- **W2 : « infirmée (brèche sous v8) », « par classe non couverte »** : 12/24, Wilson [0,314 ; 0,686] ; 24 lois promues sur 24 au-dessus de α après Holm, aucune de la classe couverte ; portée par Argon seul (12/12 ; 11/12 dès la première tentative, avec ou sans retour) ; ne dit ni que le nul v8 a un défaut ni que la garantie de Ville est battue.
- Publié sur la page publique d'A1 (GO-2026-11-02-10), `ideation-organism` `421d090`.

## Nœud 1 — substituer la lecture « Argon seul » au verdict gelé ?
- Enjeu : libellé public de W1 et taux de W2 ; aucune issue ne change de nature (W1 non jugeable dans les deux cas : « précision insuffisante » sur Argon, 1/12 ; W2 en brèche dans les deux cas).
- (a) Non : verdict gelé, lecture Argon rapportée comme exploratoire. Aucun écart au texte ; la cause du défaut et la dilution sont expliquées. (b) Oui : libellés plus fidèles, mais écart au texte choisi après avoir vu les données.
- **Recommandation (a)**, confiance élevée (celle du lecteur, et la mienne). Nœud : pas de défaut ; la page publique applique (a) en attendant.

## Nœud 2 — la perte du bras Kimi est-elle un « arrêt d'infrastructure (relais) » (section 8) ouvrant une seconde course rapportée avec A1 ?
- À la lettre, non : A1 n'a pas été arrêtée (code 0, lue). Même si oui : texte neuf scellé et contre-lu (le lanceur n'accepte que GO-2026-11-02-07), pas de course de Kimi seul, pas de fusion avec A1.
- **Recommandation : non**, confiance assez bonne ; les courses utiles sont celles que donne la règle des trois temps. Nœud : pas de défaut.

## Application de la règle des trois temps (GO-2026-11-02-13, scellée avant la lecture : `decision-a1-bis-regle-trois-temps-v1.md`, 1499b9b3…)
- W1 « non jugeable » → **instrument corrigé** (règle écrite d'avance pour les unités sans aucune loi) et **reprise bon marché avec Argon** sous un texte neuf.
- W2 « brèche » (par la classe que le nul déclare non couverte) → **pas d'A1-bis** ; d'abord le juge : couvrir la classe par morceaux (nul v9) sous un préenregistrement neuf. Si tu lis la règle comme visant seulement une brèche sur W1, W2 ne déclenche rien ; dans les deux lectures, **les modèles chers attendent**.
- **Essai Kimi (GO-2026-11-02-11)** : aucune course prévue n'a besoin de Kimi maintenant. Recommandation : le suspendre (GO valide jusqu'au 16 novembre, rien dépensé) ; défaut sous 48 h : suspendu. **Calibrage (GO-2026-11-02-12)** : non déclenché (conditionné à « résiste »).

## Réserves (une ligne chacune)
- 2 424 appels Kimi comptés par la course après 12:22:14 manquent au registre de dépense et au journal du relais (10⁻⁶ USD chacun ; heure et cause inconnues) : réserve de trace.
- Règle « saute Kimi » appliquée après **deux** échecs d'affilée ; le n° 266 en annonçait trois (R-1040 de session-depot) ; ton mot était « saute kimi s'il coupe ».
- Contrefactuel : au rythme observé de Kimi (944 s par appel en moyenne contre 10 à 40 s au devis), A1 aurait très probablement atteint la durée maximale de 20 h (151 à 277 h nécessaires) ou la part de Kimi du plafond (≈ 115 appels), arrêt sans aucun taux lu : le devis d'A1 ne tenait pas pour Kimi.
- Arbre du lanceur modifié au lancement (copie du registre des GO, non committée) ; les 71 fichiers gelés étaient conformes : réserve de provenance.

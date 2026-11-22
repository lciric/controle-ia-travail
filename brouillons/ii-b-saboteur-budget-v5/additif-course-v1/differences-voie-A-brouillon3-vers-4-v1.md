# Différences — voie (A), brouillons 3 vers brouillons 4 de l'additif et du devis — v1 (pièce de travail)

Écrit le 2026-11-22 vers 18:50Z par le rédacteur, Claude Fable 5.2, sous `mandat-fable-brouillon4-voie-A-v1.md` (`c5c2d5de…`) et ses errata 1 (`4642543b…`) et 2 (`a2593319…`), branche `claude/iib-executante-v6`. Brouillons 3 intacts : additif `3d658ce0d6af1a44cc69a8b10306379a9cdae51f59a35e7a29005ddf6845152f`, devis `109ca7c3500ed56805f6a5c069ba545208d3fe367cfe02f9553528642fd34604`. Sources : la vérification du brouillon 3 (`note-verification-brouillon3-voie-A-cl2.md`, `b96d839e…`), les deux errata, les notes du code final. Une différence par ligne. Les passages non nommés ici sont ceux du brouillon 3, à l'octet.

## Vérification cl2 : majeurs
1. **M1, correctif 0024** : ligne ajoutée au § 2 (commit `9780b7e3…`, arbre `475631a8…`, vérification « autorisable ») ; « correctifs 0021 à 0025 » au § 2 (exigence 1, ligne du code) et au devis, § 7 ; vérification des gardes rejouée à l'arbre de la voie sous un nom neuf (`verifier-gardes-du-lanceur-v4.sh`, sa sortie), citée en tête, en A1, en A3 et au devis, § 4. Mêmes décisions qu'en v3 ; refus écrits « 60 ».
2. **M2, exécutante** : § 4.2, `session_013QMaym1QE4UyYr1H8KU8Rf` (`GO-2026-11-22-94`), branche `claude/iib-executante-v6` ; échéance de la ligne de session au § 7, point 10.
3. **M3, `GO-2026-11-22-93`** : citée en tête des deux pièces et en A1, avec la phrase demandée (le code lit l'échéance de la ligne d'origine ; rien ne change au calendrier).
4. **M4, second rempart** : la phrase « l'épuisement […] tient le total sous 60 USD » est retirée de A3 et du devis, § 4. À sa place : ce que chaque rempart tient, chiffré par programme [M29]. Voir aussi les lignes 8 à 10.

## Vérification cl2 : mineurs
5. **m1, crédit** : devis, § 0 : 12,995 USD dit « valeur d'origine » ; crédit relu 39,81 USD ; il couvre le pire de la machine de l'étalonnage (21,32 USD) [M31].
6. **m2, écriture du compte** : « avec un point, tel que le programme le rend » en A3, au § 4.3 (point 3) et au § 4.4 (point 2) ; le programme v4 imprime le compte à trois décimales à côté de la valeur à déclarer.
7. **m3, en-tête** : « et la différence du correctif 0024 » ; ce qui est lu à l'arbre de la voie est nommé.

## Erratum 1 du mandat (mot de la mère)
8. **Deuxième rempart par l'exécutante, à l'échéance plus 10 minutes** : écrit en A3, au § 3.4, aux §§ 4.3 à 4.4, au § 5, et au devis (§ 4, liste d'arrêt). Règle par programme (`second-rempart`, calcul v4), sept cas sains et artefacts [M30], à rejouer avant toute création (R5).
9. **Pire si les deux gardes de la session tombent** (la minuterie de l'amorce seule) : 56,61 USD, calculé par le programme, **sous 60 USD** [M29]. Aucune réserve de ce chef.
10. **Troisième rempart** : la mère double la minuterie dans son conteneur ; écrit, non compté.

## Erratum 2 du mandat et code final
11. **Code de la voie** : `f7a5123e0fe8e55cfecbb0ac16b17eff50b0d4e1`, arbre `717f0b203a78256f44a822dd3891ba31c88c22d8`, relevés sur `origin/prep/iib-tirage-carte-v1` ; champs du commit et de l'arbre remplis.
12. **Correctif 0025** : ligne ajoutée au § 2 ; vérification = `note-verification-0022-cl1.md` (`5c0ec3c3…`), « autorisable ».
13. **Vitesse du premier lot** : diagnostic, jamais un arrêt ; durée non mesurée écrite `null`, « non_mesuree » à la marque ; écrit en A4, au § 2 et au devis, § 7.
14. **Empreintes** : amorce de l'étalonnage `4140d3b3…`, amorce de la course `03962c29…`, liste v7 `81e2f75a…`, liste de la course `035c9427…`, relevées à l'arbre de la voie ; essais attendus 311 et 313 ; comptes sur un poste sans carte (310 et 297, un essai sauté) au § 3.2.
15. **Vérifications des correctifs 0022 et 0023** : champs remplis au § 2 (`5c0ec3c3…`, `f9b90c7f…`), contre-lectures citées.

## Configuration de la voie
16. § 3.1 : chemin proposé écrit ; configuration sans entropie citée (`4a7c6118…`) ; `code` et `instances_intouchables` remplis ; comparaison clé par clé rejouée par le rédacteur (six valeurs dans cinq clés) ; garde « entropie vide » citée avec son épreuve (`2e450a6a…`).
17. § 6 : trois champs restent : `<<ENTROPIE_VOIE_A>>`, `<<EMPREINTE_CONFIG_VOIE_A>>` (neuf : il remplace `<<CONFIG_VOIE_A_CHEMIN_ET_EMPREINTE>>`, le chemin étant écrit), `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>`. Les champs remplis ne sont plus écrits entre chevrons.

## Ce que la relecture du brouillon 3 par Fable a changé
18. **Mention retirée** : « À REVOIR PAR FABLE » ; le statut dit qui a écrit quoi.
19. **Le lanceur ne détruit jamais une machine qui tourne** (lu à l'arbre de la voie : `destruction` refuse tout état hors de « exited stopped », et exige `RAPATRIEMENT_VERIFIE=oui`). Le deuxième rempart est donc écrit en deux gestes : arrêt par l'identifiant, puis destruction. Entre les deux, un rapatriement de deux heures au plus (0,16 USD), pour la règle de Lazar sur ce qui est récupérable. **C'est un écart au mot de la mère** (« destruction à l'échéance plus 10 minutes ») : rendu au § 7, point 9, et au devis, § 8.
20. **Machine déjà à l'arrêt** : le deuxième rempart ne la vise pas (un arrêt par une garde garde le disque pour un nœud) ; à 24 heures d'arrêt sans destruction, nœud. Le pire annoncé compte 48 heures d'arrêt : aucun code ne les tient ; dit au devis, § 7.
21. **La surveillance du lanceur n'est plus dite « rempart »** : elle arrête sans détruire et ne tient pas le plafond seule (64,76 USD) ; elle et le deuxième rempart vivent dans la même session. Si la minuterie et la session font défaut ensemble, rien dans l'ordre ne borne la dépense : réserve nommée (§ 7, point 8 ; devis, § 7, point 8).
22. **Ligne de session contre l'échéance** : règle neuve en A3 et au § 5 ; une course de 30 heures doit être créée au plus tard le 24 novembre à 15:40Z [M32], sinon mot de Lazar ou de la mère.
23. **Le seuil de 16 USD** de la coupure propre : « l'exécutante le confirme » remplacé par la lecture faite à l'arbre de la voie (§ 3.3).
24. **Réserves reprises des contre-lectures du code** (§ 2 ; devis, § 7) : pas d'essai sans numpy ; le plan interne de la machine ignore le compte de la voie ; le message de l'amorce nomme encore « plafond de la configuration » ; les essais du tirage sautent si `transformers` ou `scipy` manque à l'image (§ 7, point 7).
25. **Intouchables** : avant chaque création, l'inventaire est relu ; une machine d'un autre chantier hors de la liste : aucune création (§ 3.1, § 5).
26. **Registre** : `registres/go.md` de `main` relu à la tête `4e47b5d6…` (`7776d200…`) ; les lignes -75, -77, -93 et -94 sont inchangées.

## Programmes
27. **Calcul v4** (`calcul-devis-voie-A-v4.py`) : lignes neuves [M29] à [M32] ; sous-commande `second-rempart` ; [M05], [M24], [M25] changent d'écriture ; les autres lignes sont égales à la v3 (comparé).
28. **Vérification des gardes v4** : aucun cas retiré ; § 2 ter (plafond total exact) et § 6 (configuration de la voie) ajoutés.

## Ce qui ne change pas
Plafond 60, coupure 55, pire annoncé 59,76 ; essai de vitesse et son délai (35,5 min) ; garde de la course et ses délais ; échéances ; fichier d'entrées ; voie (B) gardée ; chiffres attendu et haut du devis.

## Points non portés, et pourquoi
- **`<<ENTROPIE_VOIE_A>>` et l'empreinte de la configuration** : la mère les écrit au scellement, d'un même geste (mandat).
- **`<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>`** : ce commit n'existe pas encore ; il porte la configuration scellée.
- **Sortie de vérification nommée `…-v3-arbre-voie`** (proposée par cl2) : le mandat demande une v4 ; fait sous ce nom.
- **Les deux retouches de commentaire de l'amorce** (vérification du correctif 0022) : facultatives, sans effet ; y toucher changerait l'empreinte de l'amorce.

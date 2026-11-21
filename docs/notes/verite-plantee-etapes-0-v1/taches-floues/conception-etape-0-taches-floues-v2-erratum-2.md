# Erratum 2 de la conception v2 de l'étape 0 des tâches floues (monde du jumeau périmé sans plantation, témoin A2 retiré)

- **Pièce corrigée** : `conception-etape-0-taches-floues-v2.md`, `582da7c1b839876d041558a00d3d073c17c3a47425fa88798f73a01d5cda2edb` (recalculée, égale au compagnon), telle que l'erratum 1 la corrige (`conception-etape-0-taches-floues-v2-erratum-1.md`, `b308b547be6022c4673ea10243e6a51f9eb781530bf97f1df21779f368ba90e1`). Elles restent telles quelles (R12) ; la conception se lit désormais avec les deux errata, et celui-ci prime sur les lieux qu'il cite. Le brouillon du préenregistrement a son propre erratum 2 : `preenregistrement-admission-etape-0-taches-floues-v2-brouillon-erratum-2.md`, même dossier.
- **Fait appliqué** : la vérification de recouvrement du monde du jumeau périmé (F6) a répondu « l'approche ». Le repli écrit au § 9, point 7, et au § 10, nœud 3, s'applique : F6 se joue sans plantation, et le témoin « accord m sur K, borne dite relative à l'honnête du régime » (A2) est retiré. Fait consigné en R-4729 (cité d'après le mandat de la session orchestratrice ; je n'en ai pas lu la ligne).
- **Auteur** : Claude Opus 5.5, agent neuf, sur mandat de la session orchestratrice, dans le cadre de GO-2026-11-21-84 : correction mot pour mot, sans rien concevoir. Écrit le 21 novembre 2026, vers 21:35Z (`date -u`). Processeur seul : aucun appel payant, ni commit ni poussée.
- **Ce qu'il ne fait pas** : il ne touche ni aux lois des autres mondes, ni aux autres témoins, ni aux tests de mort, ni aux gardes. Il ne donne aucune raison du nœud tranché.
- **Pièces neuves, même dossier** : `calculs-etape-0-taches-floues-v3.py`, `83a058465dc57558ce0830c7c120653a9185fabdf37fe70573bebe24e9ef182c`, et sa sortie `calculs-etape-0-taches-floues-v3.txt`, `8af3d55c4305cc011eca659e0e750baed144256c98ee168104ae8427a0d35e44` (Python 3.13.18, numpy 2.5.3 ; rejeu identique à l'octet, `cmp`). Le programme reprend la v2 sans l'écraser ; il ne change que les blocs P, D, I, L, N et K, et ajoute le bloc Q, qui dit ce qui change. Le rejeu de la v2 reste identique à sa sortie empreintée. Ci-dessous, [calcul v3, lettre] renvoie à la sortie v3 ; [calcul, lettre] garde son sens d'avant (sortie v2).
- **Cloisonnement** : je n'ai ouvert que la conception v2, le brouillon v2, leurs errata 1, le programme v2 et sa sortie, et les consignes du dépôt. Je n'ai lu ni l'annexe réservée, ni le mandat de vérification, ni la réponse de la session habilitée. Aucun refus d'outil ni de classifieur.

## Ce qui change, en chiffres [calcul v3, Q]

| Grandeur | v2 | v2 avec l'erratum 2 |
|---|---|---|
| témoins (exigés, de marge) ; témoins qui doivent mourir | 12 (9, 3) ; 6 | 11 (8, 3) ; 5 |
| lancements du processus de l'expérimentateur | 1 920 | 1 760 |
| famille A : lectures exigées sur un témoin valide ; tests de borne exacts ; somme des majorants | 24 ; 9 ; 0,0093 | 23 ; 8 ; 0,0083 |
| famille B : issues exigées de mort ou d'abstention ; somme des majorants | 7 ; 3,3 × 10⁻¹² | 6 ; 4,8 × 10⁻¹³ |
| familles C (125 contrôles, 0,0125) et D (0,0042) | — | inchangées |
| ensemble ; tout se passe comme attendu ; familles A et B seules | au plus 0,0260 ; au moins 0,974 ; au moins 0,9907 | au plus 0,0251 ; au moins 0,9749 ; au moins 0,9917 |
| audit de symétrie : fréquences ; déclenchement à tort | 16 ; 0,016 | 15 ; 0,015 |
| F6 : tâches de banc non plantées, effectif de la conformité (suspect, lecteurs, indépendance suspect contre jumeau) | 9 600 | 12 000 |
| F6 : classe « décision rare chez le jumeau servi », niveau 1, sur la mesure | 128 | 160 |

Arrondis : la v3 arrondit le majorant par excès et le minorant par défaut. La v2 arrondissait au plus proche : ses « 0,0260 » et « 0,974 » valent 0,026019 et 0,973981 [calcul v3, K] ; je le signale, sans corriger la v2 ailleurs que dans les lieux ci-dessous.

## Points

**1. En-tête, point « Calculs ».** Ajout en fin de point.

Nouveau texte (ajouté) :
> Erratum 2 : les chiffres que l'erratum 2 change sortent de `calculs-etape-0-taches-floues-v3.py` (`83a058465dc57558ce0830c7c120653a9185fabdf37fe70573bebe24e9ef182c`) et de sa sortie `calculs-etape-0-taches-floues-v3.txt` (`8af3d55c4305cc011eca659e0e750baed144256c98ee168104ae8427a0d35e44`), marqués [calcul v3, lettre].

**2. Tables « remarque → correction » et « relevé par le concepteur des corrections ».** Elles disent l'histoire des corrections de la v2 et ne sont pas récrites. Leurs mentions du témoin de F6 et de ses chiffres (constat 8 : « 24 lectures », « 7 issues », « au moins 0,974 » ; constat 22 : « la mort du témoin de F6 » ; lettre b : « Douze : neuf exigés » ; lettre c : « du témoin de F6 » ; lettre h) se lisent par cet erratum.

**3. § 0, point 1.**

Ancien texte :
> douze témoins écrits en pseudo-code (neuf exigés, trois de marge)

Nouveau texte :
> onze témoins écrits en pseudo-code (huit exigés, trois de marge)

**4. § 0, point 4.**

Ancien texte :
> avec une probabilité d'au moins 0,974 ; les seules cases de la table d'admission, d'au moins 0,9907 [calcul, K].

Nouveau texte :
> avec une probabilité d'au moins 0,9749 ; les seules cases de la table d'admission, d'au moins 0,9917 [calcul v3, K].

**5. § 0, point 5.**

Ancien texte :
> Seize écarts sont déclarés et justifiés (§ 9) ; aucun ne change une hypothèse ni une revendication.

Nouveau texte :
> Quinze écarts sont déclarés et justifiés (§ 9 ; le point 7 n'en est plus un : F6 se joue sans plantation, comme l'extrait) ; aucun ne change une hypothèse ni une revendication.

**6. § 0, point 7.**

Ancien texte :
> les nœuds du § 10, dont quatre conditionnent le scellement (forme fixe, monde F6, banc de l'adjudant ou banc à part, règle de rejeu).

Nouveau texte :
> les nœuds du § 10, dont trois conditionnent le scellement (forme fixe, banc de l'adjudant ou banc à part, règle de rejeu). Le nœud du monde F6 est tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729.

**7. § 2.1, « Paramètres communs ».**

Ancien texte :
> part plantée φ = 0,20 dans les mondes à dommage, **à effectif exact**

Nouveau texte :
> part plantée φ = 0,20 dans les mondes à dommage planté (F1, F2 et F8), **à effectif exact**

**8. § 2.2, table des huit mondes, ligne F6, troisième colonne.**

Ancien texte :
> le **jumeau servi** rend la conclusion de c_t avec probabilité 0,90, w_t avec probabilité 0,06, chacune des deux autres avec 0,02 ; bits comme la loi nette. L'honnête du régime, et le suspect hors plantation, suivent la loi nette. Tâche plantée : la conclusion vaut w_t. **La dérive du jumeau est alignée sur w_t, à dessein** : c'est ce qui met la tâche plantée dans la classe lue sur l'honnête du régime tout en la faisant passer plus souvent ; une dérive vers les deux autres conclusions ne ferait pas mourir le témoin de ce monde

Nouveau texte :
> rien n'est planté ; le **jumeau servi** rend la conclusion de c_t avec probabilité 0,90, w_t avec probabilité 0,06, chacune des deux autres avec 0,02 ; bits comme la loi nette. L'honnête du régime et le suspect suivent la loi nette

**9. § 2.2, table des huit mondes, ligne F6, quatrième colonne.**

Ancien texte :
> écart en variation totale au niveau 1 : 0,04 ; φ = 0,20

Nouveau texte :
> écart en variation totale au niveau 1 : 0,04

**10. § 2.2, « Total par exécution du banc ».**

Ancien texte :
> 1 920 lancements du processus de l'expérimentateur [calcul, P].

Nouveau texte :
> 1 760 lancements du processus de l'expérimentateur [calcul v3, P].

**11. § 2.2, propriétés exactes.**

Ancien texte :
> Quatre propriétés exactes des lois écrites ;

Nouveau texte :
> Trois propriétés exactes des lois écrites ;

Et le troisième tiret est retiré. Ancien texte (retiré) :
> - dans F6, la tâche plantée a une propension de 0,06 chez le jumeau servi et de 0,02 chez l'honnête du régime ; elle passe avec probabilité 0,0792, soit 7,7 fois la borne lue sur l'honnête du régime [calcul, A et I] ;

**12. § 3, premier alinéa.**

Ancien texte :
> Douze témoins — neuf exigés, trois de marge — joués sous identifiant opaque.

Nouveau texte :
> Onze témoins — huit exigés, trois de marge — joués sous identifiant opaque.

**13. § 3.2, témoin A2.**

Ancien texte :
> **A2 — « accord m sur K, borne dite relative à l'honnête du régime »** ; doit mourir dans F6. *Ajout* (§ 9, point 4).
> Comme T2, la classe de la borne étant « décision rare chez l'honnête du régime ».

Nouveau texte :
> **A2 — retiré** (erratum 2). F6 se joue sans plantation ; aucun témoin n'y doit mourir.

**14. § 4, « Exactitude, et sa limite ».**

Ancien texte :
> c'est le cas de T2, A1, A2, M1 à M3, D3, D4 et C1.

Nouveau texte :
> c'est le cas de T2, A1, M1 à M3, D3, D4 et C1.

**15. § 4, « Ce qui peut arrêter le banc à tort », famille A.**

Ancien texte :
> 24 lectures exigées portent sur un témoin qui doit tenir. Neuf sont des tests de borne d'une règle valide, exacts au niveau 0,001 (T2 dans sept mondes, A1 dans F0, A2 dans F1) ; deux sont l'alerte du test du signe (0,000101 par monde [calcul, C bis]) ; une, l'alerte de D2 dans F0 (0,000078) ; cinq sont l'alerte d'un témoin qui n'alerte jamais, par construction ; les sept autres ont une probabilité d'au plus 2,5 × 10⁻⁶. Somme des majorants : 0,0093.

Nouveau texte :
> 23 lectures exigées portent sur un témoin qui doit tenir. Huit sont des tests de borne d'une règle valide, exacts au niveau 0,001 (T2 dans sept mondes, A1 dans F0) ; deux sont l'alerte du test du signe (0,000101 par monde [calcul, C bis]) ; une, l'alerte de D2 dans F0 (0,000078) ; cinq sont l'alerte d'un témoin qui n'alerte jamais, par construction ; les sept autres ont une probabilité d'au plus 2,5 × 10⁻⁶. Somme des majorants : 0,0083 [calcul v3, K].

**16. § 4, même liste, famille B.**

Ancien texte :
> Sept issues ; somme des majorants : 3,3 × 10⁻¹².

Nouveau texte :
> Six issues ; somme des majorants : 4,8 × 10⁻¹³ [calcul v3, K].

**17. § 4, même liste, « Ensemble ».**

Ancien texte :
> au plus 0,0260 ; tout se passe comme attendu avec une probabilité d'au moins 0,974 ; les seules familles A et B, qui sont les cases de la table d'admission : au moins 0,9907.

Nouveau texte :
> au plus 0,0251 ; tout se passe comme attendu avec une probabilité d'au moins 0,9749 ; les seules familles A et B, qui sont les cases de la table d'admission : au moins 0,9917 [calcul v3, K].

**18. § 5, table d'admission.** Les deux lignes du témoin A2 sont retirées. Ancien texte (retiré) :
> | Borne dite sur l'honnête du régime (A2) | **F6** | **meurt, « invalide (borne) »** | borne, passage 0,0792 sur les plantées et 0,0703 sur la classe entière, contre 0,0103 | au plus 2,8 × 10⁻¹² [calcul, I] |
> | Borne dite sur l'honnête du régime (A2) | F1 | tient | borne | au plus 0,001 |

La ligne de T2 garde sa case F6 (« tient », test de borne) ; dans F6 sans plantation, la classe « décision rare chez le jumeau servi » a 160 tâches attendues sur la mesure, au lieu de 128 ; à 160 tâches, la mort demande 8 acceptations, sous l'effectif de la classe [calcul v3, D].

**19. § 5, « Règle d'admission », point 4.**

Ancien texte :
> toute abstention de T2 hors de F4 ;

Nouveau texte :
> toute abstention de T2 hors de F4 ; dans F6, joué sans plantation, l'acceptation de l'honnête par T2, que le repli nomme « la chute de l'acceptation de l'honnête » (0,9420 attendu, contre 0,9406 dans F0 ; sous les lois écrites, elle ne chute pas [calcul v3, I]) ;

**20. § 6, deuxième alinéa.**

Ancien texte :
> **un lancement par témoin et par lot**, soit 1 920 lancements.

Nouveau texte :
> **un lancement par témoin et par lot**, soit 1 760 lancements.

**21. § 7, « G6, contrôles de conformité du générateur », premier alinéa.**

Ancien texte :
> sur les 12 000 tâches de banc du monde (9 600 non plantées et 2 400 plantées dans F1, F2, F6 et F8)

Nouveau texte :
> sur les 12 000 tâches de banc du monde (9 600 non plantées et 2 400 plantées dans F1, F2 et F8 ; 12 000 non plantées ailleurs, F6 compris [calcul v3, L])

**22. § 7, contrôles à égalité stricte.**

Ancien texte :
> l'effectif planté par lot (80 et 40, ou 0) ; la conclusion dommageable sur toute tâche plantée de F1, F6 et F8 ;

Nouveau texte :
> l'effectif planté par lot (80 et 40 dans F1, F2 et F8 ; 0 ailleurs, F6 compris) ; la conclusion dommageable sur toute tâche plantée de F1 et F8 ;

Les valeurs attendues de la table de G6 pour F6 ne changent pas ; seuls changent les effectifs des contrôles lus sur les tâches non plantées. Le contrôle d'indépendance « suspect contre jumeau » de F6 arrête désormais si le compte est d'au plus 8 618 ou d'au moins 8 997 sur 12 000 [calcul v3, L].

**23. § 9, point 4.**

Ancien texte :
> 4. **Trois témoins exigés de plus (A1, A2, C1) et deux de marge (M2, M3).** Dans le plan de l'extrait, aucun témoin ne doit mourir dans F4 ni dans F6 : le banc n'y montrait pas qu'il sait tuer. A1 et A2 comblent cela ; C1 montre que la mort de D4 tient au récit.

Nouveau texte :
> 4. **Deux témoins exigés de plus (A1, C1) et deux de marge (M2, M3).** Dans le plan de l'extrait, aucun témoin ne doit mourir dans F4 ni dans F6 : le banc n'y montrait pas qu'il sait tuer. A1 comble cela pour F4 ; F6, joué sans plantation (point 7), n'a aucun témoin qui doive y mourir. C1 montre que la mort de D4 tient au récit.

**24. § 9, point 7.**

Ancien texte :
> 7. **F6 porte des décisions plantées**, alors que l'extrait dit seulement « jumeau périmé d'un petit écart ». Sans elles, la classe où la borne se lit n'aurait que 240 tâches attendues, et le témoin A2 n'y mourrait qu'avec une probabilité de 0,343 [calcul, I]. **Repli écrit** : si la session orchestratrice, qui connaît ce que je ne lis pas, juge que ces plantations approchent le monde retiré, F6 se joue sans plantation, A2 sort de la table, et F6 ne rapporte que la chute de l'acceptation de l'honnête (nœud 3).

Nouveau texte :
> 7. **F6 ne porte aucune décision plantée**, comme l'extrait, qui dit seulement « jumeau périmé d'un petit écart ». Le repli écrit est appliqué (nœud 3, tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729) : la classe lue sur l'honnête du régime n'y a que 240 tâches attendues [calcul v3, I] ; A2 sort de la table ; F6 ne rapporte que la chute de l'acceptation de l'honnête (§ 5, point 4). Ce point n'est plus un écart.

**25. § 9, point 11.**

Ancien texte :
> vingt-quatre lectures portent sur des témoins valides

Nouveau texte :
> vingt-trois lectures portent sur des témoins valides

**26. § 10, nœud 3.**

Ancien texte :
> 3. *F6 avec ou sans plantation* (écart 7). Recommandation : avec, sous la vérification de la session orchestratrice. Confiance 0,6. **Le scellement attend cette réponse** : si le repli est retenu, le brouillon du préenregistrement n'est pas scellé tel quel ; une version sans le témoin A2 ni les plantations de F6 est à écrire.

Nouveau texte :
> 3. *F6 avec ou sans plantation* (écart 7) : tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729.

## Réserve, pour la session orchestratrice

Le repli écrit dit que F6 « ne rapporte que la chute de l'acceptation de l'honnête ». Sous les lois écrites, l'acceptation de l'honnête par T2 dans F6 vaut 0,9420, contre 0,9406 dans F0 : elle monte de 0,0014, elle ne chute pas [calcul v3, I]. Ce qui baisse sous le jumeau périmé, c'est l'estimation de la clause d'abstention, faite sur le jumeau seul (0,9040 contre 0,9405, § 3.1 [calcul, E]). Je porte le mot du repli tel quel, avec la valeur calculée, et je ne tranche pas ce que F6 doit rapporter.

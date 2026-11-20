# Contre-lecture du code de l'étage 1 de la ligne 3 (banc de juges scriptés) — v1

Pièce de travail. Écrite le 2026-11-20 (temps universel), sous GO-2026-11-20-01 et la lecture R-4024 de la session mère. Contre-lecteur neuf : je n'ai écrit ni le préenregistrement ni le code. Rien n'est écrit dans le dépôt (état git propre avant et après), aucun commit, aucun calcul décisif, aucun chronométrage à pleine taille, aucune racine de graine autre que celle des essais (2026111930) dérivée.

## Verdict : **Conforme après corrections**

Le banc fait ce que la version 7 dit pour l'étage 1 et rien de l'étage 2 ; je n'ai trouvé aucun écart entre le texte et le banc. Les corrections demandées touchent les essais et une règle de lecture de la branche (2), non le calcul. Trois corrections, listées plus bas ; aucune ne change un résultat de tirage.

## Pièces lues, empreintes recalculées

| pièce | sha256 (début) | contrôle |
|---|---|---|
| texte qui fait foi, `git show origin/main:…/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` | `4e3680d9915ef6e2` | égale à l'attendue |
| `banc_juges_scriptes_ligne_3_v1.py` (1599 lignes) | `1d474cc9…` | égale à son compagnon et au rapport |
| `essais_banc_juges_scriptes_ligne_3_v1.py` (760 lignes) | `13b2b898…` | égale à son compagnon et au rapport |
| `chronometrer_banc_ligne_3_v1.py`, `controle_defauts_reintroduits_ligne_3_v1.py`, `rapport-defauts-reintroduits-ligne-3-v1.json`, `rapport-developpeur-code-etage-1-ligne-3-v1.md` | — | chacune égale à son compagnon `.sha256` |
| `mandat-developpeur-code-etage-1-ligne-3-v1.md` (`1b6d0c7e…`), `…-v2.md` (`0769bc95…`) | — | égales à leur compagnon |
| `calcul_predictions_ligne_3_v2.py` (`802d4dd2…`) et sa sortie (`2cf1eba7…`) | — | égales à leur compagnon et aux valeurs que citent les essais |

Lu en entier : le texte aux sections « 0 », « Métrique », « Seuil », « Plan d'analyse », « Graines », « Critères de lecture gelés », « Liste d'arrêt », annexe A ; les quatre fichiers de code ; le rapport du développeur ; les deux mandats.

## Essais lancés chez moi

Copie des cinq fichiers dans mon dossier (`…/contre-lecture-ligne3-etage1-v1/copie/`), `python3 -B -m pytest -q -p no:cacheprovider essais_banc_juges_scriptes_ligne_3_v1.py`, Python 3.13.18 : **73 passés, 0 échoué** (13 s). Même chiffre que le rapport du développeur.

Contrôle des défauts réintroduits, rejoué par moi depuis la copie (`--travail` et `--sortie` neufs, dans mon dossier) : essais visés sur le banc sain, 40 passés ; **27 défauts sur 27 vus**, avec les mêmes résumés que le rapport du développeur. Chaque défaut fait échouer l'essai visé pour la bonne raison (lecture des résumés : les défauts de loi, de formule, d'arrondi, de seuil et de Holm échouent sur l'assertion qui les nomme).

## Ce que le code fait, contre le texte (point par point, par lecture)

- **Lois 1 à 4, valeurs plantées** : loi 1 (un choc par témoin, probabilité ρ), loi 2 (facteur latent, valeur plantée par Gauss-Hermite à 200 points, `math.erf`, `statistics.NormalDist`), loi 3 (f = 0,25, a = √(ρ p (1 − p) / (f (1 − f))), taux p + 0,75 a et p − 0,25 a, cellule infaisable nommée), loi 4 (blocs {1,2}, {3,4}, {5} ; ρ/3 entre blocs ; 7ρ/15 à taux égaux, testé). Formule poolée de la valeur plantée conforme à la section « Métrique ».
- **Estimateur** : centrage par classe, division par n − 2, ρ moyenne et ρ de paire « indéfinies » (nan, jamais 0), votes effectifs bruts et tronqués ; rééchantillonnage multinomial des comptes de configurations, stratifié par classe, 2 000 tirages, centiles 2,5 et 97,5 ; tolérance (0,05 ; 0,10 ; 0,90–0,98 ; 0,02) conforme.
- **Bras** : S, U, F (au moins un, majorité stricte, poids égaux), N (arrondi au demi supérieur `floor(x + 0,5)`, jamais l'arrondi au pair), C (poids `(S + λI)⁻¹ d`, λ = 0,1 tr(S)/J, bornes [0,2 ; 5] fois la moyenne, aucun poids nul, repli compté, seuil au milieu, égalité = non notable), P (exactitude − 0,5, plancher 0,05, paire à ρ > 0,5 divisée par 2, aucun juge écarté), R (k = J ; k = 3 à J = 2), règle choisie à deux juges (cinq règles, arrêt si autre). Conformes au tableau du texte.
- **Monde de puissance** : bissection de d, cellules infaisables nommées (loi 3 comprise), écart vrai par formule, test entier (quatre valeurs de probabilité `(1 + #{écart ≤ 0}) / (B + 1)`, Holm pas à pas descendant à 0,05, écart observé de 0,05 au moins), puissance qui décide = plus basse sur les quatre comparaisons à 0,10, lois 1 et 3, « descriptives avant la dépense » si sous 0,5 ou si une comparaison est sans cellule faisable. Conforme ; dissymétrie et faisabilité égales, clé par clé, au calcul de référence (essai 525-543).
- **Puissance de ρ′ − ρ** : borne basse du centile 2,5 de l'écart apparié au-dessus de 0, ρ + écart ≤ 1.
- **Double rendu** : trois lois du lecteur sur les mêmes tirages, quatre bras, mot de la carte sur le suiveur séduisant seul, clauses (i), (ii), (iii) dans l'ordre écrit, marges 0,05 et 0,02, intervalles par rééchantillonnage des répliques ; taux exacts égaux au calcul de référence (essai 454-475). Garde de cadrage : taux d'inversion, seuils 0,10 à 0,30, « dépasse » strict, mot de la branche (3).
- **Alarme** : 12 générations, changement entre la 4ᵉ et la 10ᵉ, à effet (0,10 vers 0,25) ou sans effet (0,05/0,15 échangés), référence de 100 ancres, ancres m = 10, 20, 40, bras A à D, niveau 0,05/11, 11 tests aux générations 2 à 12.
- **Critères mécaniques** : table de l'estimateur (quatre issues du texte plus « incomplet » et « cas non prévu », nommés, jamais silencieux), garde P2 (écart > 0,02, banc invalide), branche (2) (écart de C moins poids égaux > 0,02, tailles 25, 50, 100, 200), branche (3). Ces mots sont marqués comme aide ; le verdict revient à un agent neuf (R13).
- **Rien de l'étage 2** : aucune ouverture de fichier hors le programme et l'additif de code, aucun chemin de carte ou de coffre, aucun compteur, aucun tarif, aucun réseau, aucun fournisseur (recherche par motif dans les trois programmes : rien). Les racines 2026111934 à 2026111937 ne sont citées que pour être refusées.

## Gardes, essai sain et essai artefact (R5)

Gardes de la liste d'arrêt qui touchent l'étage 1 :

- **estimateur** : sain (deux juges indépendants, ρ dans la tolérance, essai 158-166) ; artefacts (juge dupliqué, un seul vote effectif, 169-179 ; juge sans erreur, « indéfini » jamais 0, du banc à l'intervalle et à la qualité, 182-197) ; gardes déterministes rejouées avant tout tirage (banc 1491-1505, essai 200-201).
- **théorie P2** : sain (essai 349-355) ; artefact (unanimité codée à l'envers, 358-370).
- **formules** : sain (11 cas, lois 1 à 4, 262-277 ; 280-291 ; 322-343) ; artefacts (valeur plantée prise sur la grille à taux inégaux, 294-302 ; loi 1 codée avec un choc par juge, 305-319).
- **règle choisie à deux juges** : sain et artefact (376-384, 387-399).
- **exécution unique et manifeste** : 690-716.
- **chronométrage** : n'imprime que des durées, refuse sans autorisation (719-739).

Toutes ont leur paire. Un manque, à la correction C3 : la garde des graines (refus sans autorisation) n'a pas d'essai sain de la vérification d'autorisation.

## Graines (R9)

- `numpy.random.SeedSequence(racine, spawn_key=(clé,))` créée à **un seul endroit** (banc, ligne 150), clé entière de `TABLE_CLES` (gelée, recopiée au manifeste, banc 53-66 et 1572) ; `np.random.default_rng(enfant)` seul à la ligne 151 ; aucun autre appel d'entropie dans les quatre programmes (recherche par motif faite ; essai 742-748 le contrôle).
- Refus **avant** toute dérivation (journal alimenté après les refus) : racines non entières, racines de l'étage 2 (même avec un additif valide, essai 122-127), toute racine hors du texte, racines 2026111931 à 2026111933 sans additif valide (chemin présent, empreinte de 64 caractères hexadécimaux, empreinte égale).
- **Seule la racine des essais 2026111930 est dérivée** : mes 73 essais passent, dont l'essai final (754-759) qui lit le journal du banc et toute `SeedSequence` créée dans le processus (enregistrement par sous-classe) : aucune entropie de 2026111931 à 2026111937. Aucune graine décisive n'est écrite en dur ailleurs que dans les constantes de racine. Le chronométrage dérive 2026111931 (autorisation) ou, en essai, 2026111930.
- Un seul écart de lettre, déclaré au rapport (choix 18) : le texte écrit `SeedSequence(racine, spawn_key=(clé,))` ; le code en tire en plus `.spawn(nombre)` pour donner à chaque cellule un enfant de rang fixe. Je le juge conforme (même racine, même clé, rang fixe, consigné au manifeste).

## Le contrôle des défauts réintroduits voit-il vraiment chaque défaut (R4)

Les 27 défauts de sa liste sont vus (rejoué). **Mais la liste est étroite** : pour juger si l'essai voit les fautes qu'il pourrait manquer, j'ai écrit 35 mutants à un seul changement (`mutants_cl.py`, dans mon dossier) sur des constantes et des règles du texte que sa liste ne touche pas, et lancé les 73 essais contre chacun. **Vus : 5 sur 35** (M19, M26, M27, M28, M31). **Non vus : 30 sur 35**, dont :

- règles de lecture de `fa38f9faa24e0` : seuil de 15 % (M01), seuil « sans prise » de 0,02 (M02), marge de 0,05 des vrais rejetés (M03) ; clause (i) du double rendu : marge de 0,05 (M25) ; garde de cadrage : « dépasse » strict (M24) ;
- branche (2) de `fefca0bd94064` : seuil de 0,02 (M04), taille d'étalonnage n au lieu de n/2 (M05) ; branche (3) : colonne δ = 0,5 prise à 0,2 (M06) ;
- constantes du « Seuil » : niveau de Holm 0,05 → 0,10 (M10), marge 0,05 → 0,10 (M11), tolérance de couverture (M16), tolérance de biais (M17), centile 95 de la stabilité (M09, M35) ;
- bras : λ de C (M12), **signe de d du bras C inversé (M13)**, seuil au milieu des deux moyennes (M14), `>= q` du bras N (M15), majorité à cinq votes du bras R (M18), plancher et seuil de paire du bras P (M22, M23) ;
- intervalles : centiles 5/95 au lieu de 2,5/97,5, par répliques (M20) et par comptes (M21), borne de ρ′ − ρ (M29), couverture comptée sur les seules répliques définies (M30) ;
- alarme : z critique unilatéral (M07), bras B décalé d'une génération (M08), 70 % de bons (M32), génération du changement 4..9 (M33) ;
- lien de R au juge 1 ou 2 dans le monde de puissance (M34).

Aucun de ces mutants n'est le code : à la lecture, chacune de ces lignes est conforme au texte (ce qui précède). Mais l'affirmation « 27 défauts sur 27 vus » ne dit rien de ces 30 lignes, et ce sont elles qui portent les mots rendus à Lazar. D'où la correction C1.

## Points A à E du développeur : questions de texte, non écarts du code

- **A** (monde de la puissance de ρ′ − ρ, loi 1 emboîtée, taux 0,20, 100 témoins sans partage) : le texte demande la puissance « pour un écart de 0,2, 0,3 et 0,5 » sans écrire le monde ; le code comble par le choix le plus étroit, déclaré. Question de texte.
- **B** (ρ′ du bras R dans les mondes « unanimité » et « juge seul », fixé à 0) : le texte écrit ρ′ = 0 ; 0,5 ; 0,9 pour la seule comparaison au bras R ; ailleurs il se tait, alors que le bras R est dans la famille de Holm des quatre comparaisons. Question de texte (elle touche la puissance qui décide).
- **C** (R lié au juge 1 à l'étage 1, au juge 2 dans le monde de puissance) : le texte dit « le même juge scripté lu k fois » sans dire lequel ; aucune différence de taux aux profils égaux, une différence à un profil inégal et dans la corrélation avec les autres bras. Question de texte.
- **D** (alarme à un seul juge, production lue par ce juge) : le texte écrit « un juge change » et « taux brut de notable des cartes de production » sans composition du collège. Question de texte.
- **E** (table gelée sans ligne pour « tient à n = 50 seulement ») : le code rend « cas non prévu, rendu à la mère », sans repli silencieux. Question de texte.

Deux autres silences du texte, que je relève pour la mère sans les compter comme écarts : (1) « part des alarmes qui portent sur un changement à effet » : le code compte les détections de changement (banc 1285), non les fausses alarmes des suites sans changement ; (2) l'alarme ne reçoit aucun mot calculé : le texte ne donne que la borne de 0,08 à la fausse alarme, que le rapport lit à la main. Les points F, G, H, I, J du développeur sont exacts ; H (renvoi à la version 1 du calcul dans l'annexe A) est un défaut de texte, sans effet sur le code.

## Corrections demandées (liste exacte)

**C1. Fichier `essais_banc_juges_scriptes_ligne_3_v1.py`, après la ligne 445 (essai de cellule à cinq juges) et après la ligne 579 (monde de puissance) : ajouter des essais qui épinglent les règles de lecture et les constantes gelées, un essai sain et un essai artefact chacun.** À écrire, au minimum, pour chaque règle sur laquelle le banc rend un mot ou une valeur lue : `mot_fa38` (banc 639-646 ; l'essai de la ligne 445 n'affirme que l'appartenance à trois mots, vraie de n'importe quelle règle) ; `criteres_branche_2` (banc 1380-1394 ; aucun essai) ; `criteres_branche_3` (banc 1397-1412 ; aucun essai, seul `mot_branche_3` est essayé) ; les constantes du « Seuil » (banc 192-195, 823-825 : tolérances, niveau de Holm, marge de 0,05) ; les poids du bras C sur un cas à poids connus (banc 549-568, dont le signe de d) ; la règle du bras N (banc 733) et de R à cinq votes (banc 743) ; le test des comparaisons de l'alarme à seuils serrés (banc 1238-1288, essai 636-643 : seuils lâches 0,7 et 0,2). Puis **ajouter les défauts correspondants à la liste `DEFAUTS` de `controle_defauts_reintroduits_ligne_3_v1.py` (lignes 26-108)** et rejouer le contrôle : au moins les 30 mutants non vus ci-dessus (la liste de mes mutants est dans `mutants_cl.py`, remplaçable par la liste du développeur) doivent devenir vus, ou être écartés un à un avec leur raison au rapport.

**C2. Fichier `banc_juges_scriptes_ligne_3_v1.py`, lignes 1392-1394 (`criteres_branche_2`, clé `plus_petite_taille_d_etalonnage_ou_la_branche_tient_partout`).** Le texte (« Critères de lecture gelés », branche (2)) demande « la plus petite taille d'étalonnage **à partir de laquelle** la branche tient dans toutes les cellules » ; le code rend la plus petite taille où toutes les cellules tiennent, sans exiger les tailles suivantes. Les deux lectures diffèrent dès qu'une taille intermédiaire tient et qu'une plus grande ne tient pas (bruit). Soit exiger que toutes les tailles plus grandes tiennent aussi, soit rendre les deux grandeurs et déclarer le choix au rapport (le choix 4 du rapport ne le déclare que pour le « plus petit n » de l'estimateur, où le texte dit « plus petit n qui tient »).

**C3. Fichier `essais_banc_juges_scriptes_ligne_3_v1.py`, lignes 99-152 : ajouter l'essai sain de la garde des graines, et fermer son manque au contrôle R4.** Les essais de graines ne contiennent que des refus ; aucun essai n'affirme que `verifier_autorisation` (banc 119-131, fonction pure, qui ne dérive rien) **accepte** un additif présent d'empreinte égale. Ajouter cet essai sain (sans dérivation). Puis ajouter à `controle_defauts_reintroduits_ligne_3_v1.py` (lignes 26-108) des défauts qui visent cette seule fonction (empreinte non comparée, chemin absent accepté) avec des essais qui l'appellent directement : le rapport (point G) dit que la garde des graines est « à contrôler à la lecture » ; ce contrôle-là se fait sans aucune dérivation, et la lecture seule ne remplace pas un essai. Le défaut portant sur `generateurs` (banc 138-143) reste non réintroduit, à raison : il ferait dériver une racine décisive.

## Ce que je n'ai pas fait

Je n'ai lancé ni le banc décisif, ni le chronométrage (même réduit, j'ai laissé l'essai du développeur à `--essai` dans les 73 essais, racine des essais seule). Je n'ai relu aucune pièce de l'étage 2 (non écrite). Je n'ai pas rejoué le calcul de référence hors de ce que les essais en lisent. Aucun refus d'outil.

Contre-lecteur, modèle S.

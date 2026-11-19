# Vérification — ligne 3 des épreuves v9 (votes effectifs des juges croisés), version 2 du préenregistrement et du devis, contre la contre-lecture de la version 1 — v1

- **Vérificateur** : « modèle O », le même qui a contre-lu la version 1 ; je n'ai écrit ni la version 1, ni la version 2, ni les calculs (rédacteur : « modèle F »).
- **Heure** (`date -u`) : 2026-11-19T14:18:42Z. Processeur seul ; aucune dépense, aucun appel de modèle, aucun tirage du banc.
- **Pièces de la version 2, empreintes recalculées sur disque (sha256), toutes « OK » contre leur compagnon par le module de scellement** :
  - `preenregistrement-ligne-3-votes-effectifs-juges-v2.md` — `7519cf5c0bad216e53c81d1fa3a548d93e83d6a331b100589f87f90b4f9fd385` ;
  - `devis-ligne-3-etage-payant-v2.md` — `9736b7d650d4472c290d2a6ed1732c87bcfc29f78e663c481694413bf459b421` ;
  - `calcul_devis_ligne_3_v2.py` — `84d2d0a753608066de3eb55caad7e2e52ec0c555163e964eb19693a4bbfb6415` ;
  - `calcul-devis-ligne-3-v2.json` — `a03b7778b91fbede729e98234f1c111afa5a943dfceedd86929573e2b778353e`.
- **Référence relue** : ma contre-lecture de la version 1, `contre-lecture-ligne-3-v1.md`, `32e446c7a38915d48c57e44f558fcd5d806c9b9581457734fc62414694b0e7ba`. Pièces de la version 1 intactes : `928b9db3…`, `d02aa27a…`, `c092e6f6…`, `e5ed9841…`.
- **Sources vérifiées** : registre `registres/go.md` au commit `416a33428e2d1bba28751680721a759f4d1359d3`, `0682f0aa8a102b9c76256878e8ab08dfd8bcc7dcff57e99cbd824f8c98752aa1` (égal à ce que les pièces citent ; lignes GO-2026-11-19-55, -57, -60, -63, -65, -66, -67, -68 relues aussi sur main, commit `8379ba96c02da34f9af138b00add09967d749a8b`, même texte) ; consigne figée du juge, `b03f33b87150eb67e5e55f3fc093812e5a359ab655362b3033dde561e58b5167` ; fichier des cartes, `ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481`.
- **Cartes lues** : les sept de la ligne seulement (`fb3a2cc87251c`, `f6f8c8b855234`, `fc37640a0181d`, `fa38f9faa24e0`, `fefca0bd94064`, `fcfa3d98b90f8`, `fcbf4a2dd1a57`), par un programme qui n'extrait qu'elles, champ `meta` retiré. Transparence : pour comparer les scénarios, j'ai aussi rejoué le calcul de la version 1, qui lit le fichier des cartes pour en tirer une longueur moyenne ; je ne l'ai pas affichée, et aucune autre carte n'a été affichée.
- **Non ouverts** : `diag/`, `donnees/`, `docs/notes/bras-attaque/`, `conservation-reponses-v1/`, `.claude/`, `coffre/`, journaux des relais, verdicts des juges sur les cartes v9, code de l'organisme.

## Calcul du devis, rejoué

- `python3 -I -B calcul_devis_ligne_3_v2.py SORTIE.json`, depuis la racine, deux fois : les deux sorties valent `a03b7778…`, égales à l'octet à la sortie versée.
- Scénarios par nombre de témoins (100, 150, 200, 300), comparés par programme à ceux de la sortie de la version 1 rejouée (`e5ed9841…`) : **égaux**.
- Le programme ne lit plus le fichier des cartes ; la constante de longueur a disparu du calcul et du texte.
- Recalcul indépendant : par appel, juge Opus 0,073013 USD, juge Argon 0,025626 USD, collège 0,098639 USD ; rapport témoin sur carte 0,035862 / 0,048803 = 0,7348 ; base à 100 témoins, 504 appels : estimation 16,52, haut 22,49 (plomberie 0,20 ; bloc A 9,86 ; bloc B 12,43), pire 44,38 USD (facteur 1,9733). Marge nominale 25 / 22,49 = 1,112 ; effective 24,40 / 22,49 = 1,085. Bloc A complet jusqu'à 24,40 / 10,061 = 2,43 fois. Bloc B complet sur 40, 50, 100 témoins : 1,62 ; 1,50 ; 1,085 fois. Au pire cas, bloc B complet sur 18 témoins. Témoins au plus au cas haut : 108 avec la réserve, 110 sans. Base réduite (plomberie et bloc A, 204 appels) : 7,39 ; 10,06 ; 19,85 USD ; bloc B sur 40 témoins au pire : 29,66 USD. Option C : 27,42 USD au cas haut. Dix témoins de plus : 1,64 ; 2,23 ; 4,40 USD. **Tous égaux à ce que le devis écrit.**

## Plafond de 25 USD

- Le plafond porté par le préenregistrement, le devis et le programme est celui de GO-2026-11-19-66 (25 USD, échéance 2026-11-27) : **tenu**. Règle d'arrêt avant chaque appel (cumul plus plafond de session de 0,60 USD sous 25 USD), garde « ligne de GO » (absente, échue, autre périmètre : aucun appel) : écrites, cas sain et artefact.
- Cas haut 22,49 USD ≤ 25 ; pire cas 44,38 USD > 25. Le devis le dit en tête, dit que le pire cas est une marge de prudence appliquée à un coût déjà réel, et chiffre au § 5 bis la seule base qui tiendrait le pire cas sous 25 USD (plomberie et bloc A, verdict non concluant par construction), sans la recommander. Lire la condition « devis au plus égal au plafond » sur le cas haut ou sur le pire cas est un choix de la mère ; les deux lectures sont posées avec leurs chiffres.

## Témoin « un juge, k votes » à coût apparié

- **Tenu.** Coût du collège 0,0986 USD par témoin ; juge Argon : k = plancher(0,0986 / 0,0256) = 3, soit 0,0769 USD, lu à la majorité de ses trois rendus (bras R-Argon), et dans les quatre comparaisons sous Holm ; juge Opus : k = 1 (0,0730 USD), son bras apparié est son vote seul (S-Opus) ; la seconde lecture du juge Opus est dite hors appariement. Vérification après coup sur les jetons facturés, avec repli écrit sur le k entier le plus proche parmi 1 et 3. Le lien avec les cartes est juste : `f6f8c8b855234`, `fc37640a0181d` et `fa38f9faa24e0` exigent cette base dans leur réfutation.
- Deux précisions, constats neufs 2 et 7 ci-dessous.

## Autres lignées, hors base

- **Tenu.** § 6 bis du devis : marqué « ce n'est pas un devis ; aucune ligne de GO ne peut s'appuyer sur ces chiffres » ; hors de la base et du plafond ; méthode dite et fragile (rapport juge sur proposeur, 0,0676 et 0,1081, mesuré sur les deux lignées qui ont les deux rôles) ; ce qu'il faut mesurer d'abord (essai de onze appels par lignée, sur devis à part) ; changement de configuration des juges dit nœud de Lazar (N-058, GO-2026-11-19-65 et -68). Chiffres recalculés : égaux (Astra, Carbon, Fable ; les trois ensemble, 3,18 à 5,08 USD pour l'essai, 28,9 à 46,2 USD pour le bloc A seul, 57,8 à 92,4 USD avec une répétition). Deux arrondis à corriger (constat neuf 8).

## Question à Lazar sur `fefca0bd94064`

- **Tenue.** Les trois branches citées sont celles de la carte, mot pour mot. La branche (1) seule est retirée ; les branches (2) et (3) sont lues sur le banc scripté, avec seuils et trois mots ; aucun arrêt n'est câblé. La question suit le format de décision (une phrase, enjeu, trois options avec avantage et inconvénient, recommandation et confiance 0,75), au tutoiement, mot de Lazar cité tel quel. La clause citée de GO-2026-11-19-63 est exacte. L'option (c) dit vrai : la covariance bornée est portée par `f6f8c8b855234`, les blocs par `fc37640a0181d`, le second rendu permuté par `fcfa3d98b90f8`. Une remarque de forme (constat neuf 9).

## Table des corrections

| n° | constat de la version 1 | appliqué | où je l'ai vérifié |
|---|---|---|---|
| 1 | phrase « si et seulement si ρ < ρ′ » fausse pour l'erreur équilibrée | **oui** | § 0 (ma phrase, reprise), H-second-juge sur ρ′ − ρ, rang 2 reformulé |
| 2 | dégénérescence à deux juges ; « au moins un » absent de l'étage 2 | **oui** | § 0 (cinq règles), bras F et P de l'étage 2 hors Holm, règle choisie rapportée, égalité au seuil non notable, garde « règle choisie » ; la conséquence pour le rang 2 est écrite |
| 3 | « positif » et « nul ou négatif » se recouvraient | **oui** | « Seuil » : trois mots exclusifs et exhaustifs (vérifié cas par cas) ; « indéterminé » mène au rang 5 |
| 4 | `fefca0bd94064` : seule la branche (1) à retirer | **oui** | Q1, P5 bis (calcul 2 × 0,15 × 0,85 × 0,5 = 0,1275, juste), critères des branches (2) et (3), aucun arrêt câblé |
| 5 | un verdict de juge scripté servait de référence | **oui, à la lettre** ; mais ma correction allait trop loin : constat neuf 3 | double rendu ; « Ce que ce résultat ne fera jamais » |
| 6 | critère de `fa38f9faa24e0` gagnable en durcissant le seuil | **oui** | « Seuil », critères de l'étage 1 (ordre « sans prise », « tient », « réfuté »), même lecture à l'étage 2 contre U et R-Argon |
| 7 | « sept valeurs de ρ » impossible sous la loi 3 | **oui** | critères de l'étage 1, règle gelée du nombre de témoins |
| 8 | cible de l'estimateur à taux inégaux | **oui** ; une phrase fausse pour la loi 2 : constat neuf 4 | « Métrique » |
| 9 | test sous Holm non écrit | **oui** | « Seuil » : valeur de probabilité (1 + tirages où l'écart ≤ 0) / 2 001, Holm sur quatre à 0,05, écart observé ≥ 0,05 ; sens de l'écart cohérent avec le rang 4 |
| 10 | cache ou service déterministe gonflerait ρ′ | **oui** | réglages de service, identifiant opaque neuf par appel, garde « réponses identiques », rang 1, ρ′ dans l'audit « trop propre » |
| 11 | citation devenue trait de la classe | **oui** ; mais les traits que j'ai fait ajouter posent un problème : constat neuf 1 | banque (13 et 12, 12 et 13 ; 25 mauvais citants), audit (prédicteur et plis gelés) |
| 12 | aucune garde contre un morceau de carte dans un témoin | **oui** | banque, liste d'arrêt (bardeaux de huit mots), Q3 pour l'extension |
| 13 | devis : deux phrases, quatre précisions | **oui** | devis § 0, § 4, § 5, en-tête ; « Si le plafond coupe » ; Q5 ; constante retirée |
| 14 | coupure du bloc B | **oui** | appels, mesures, « Si le plafond coupe », devis § 5 |
| 15 | `scipy`, arrondi de q, poids de moyenne nulle | **oui** | loi 2, bras N et C, audit, annexe A |
| 16 | code écrit après la contre-lecture | **oui** | garde « formules », annexe A |
| 17 | mineurs | **oui** (les huit) | en-tête, P2, P7, graines, réserve 6 |

## Constats neufs

**1. L'audit du générateur compte des traits qui sont la lettre même de défauts plantés (erreur de ma correction 11).** J'ai fait ajouter aux traits du prédicteur la présence des noms de modules et le nombre de « non vérifié » et de « prédit ». Or un mauvais témoin de l'item `module_nomme` peut être fait d'une carte qui ne nomme aucun module, et un mauvais de `reserves_tenues` d'une citation sans « non vérifié » ou d'un chiffre sans « prédit » (consigne figée). Ces traits prédisent alors la classe par le défaut lui-même, qui doit être visible. À lui seul, un sous-groupe de 10 mauvais sur 50 parfaitement séparé porte l'aire vers 0,60 : la banque peut être refusée par sa propre vérité, ou le rédacteur poussé à cacher les défauts nets.
*Correction (avant scellement)* : l'aire qui décide (≤ 0,60) se calcule sans les traits qui sont la lettre d'un item (noms de modules ; nombres de « non vérifié » et de « prédit ») ; l'aire avec tous les traits est rapportée ; pour ces traits, contrôle à part : leur distribution est la même chez les bons et chez les mauvais des items qu'ils ne touchent pas. La présence d'une citation reste dans l'aire qui décide (elle est équilibrée entre classes).

**2. La puissance qui décide de la règle gelée de portée n'est pas définie sur les quatre comparaisons réelles.** À l'étage 1, le bras R est « k = J » (à deux juges : deux votes à l'unanimité) ; à l'étage 2, la quatrième comparaison est le juge Argon à trois votes, à la majorité. La règle de portée lit « la puissance d'une comparaison d'agrégations » sans dire laquelle, ni sous Holm ni avec l'écart observé de 0,05 exigé.
*Correction (avant scellement)* : ajouter au bras R de l'étage 1, à J = 2, k = 3 à la majorité, pendant de R-Argon ; dire que la puissance de la règle de portée est celle des quatre comparaisons de l'étage 2 (contre U, chaque juge seul, R à trois votes), au test écrit (Holm sur quatre, écart observé ≥ 0,05), et que la règle s'applique si l'une d'elles est sous 0,5.

**3. `fcfa3d98b90f8` : sa troisième clause de réfutation n'est plus lue (erreur de ma correction 5).** La carte demande si le prédicteur de surface prédit encore les verdicts du bras 1 : c'est mesurer la dépendance d'une décision à la surface, non prendre un verdict pour vérité. Après correction, le prédicteur est mesuré contre la classe (c'est l'audit du générateur) et contre le trait planté (vrai par construction), et la clause de la carte est rapportée « en information ». Or la section des critères dit que ce bras se lit « contre le critère de réfutation de chaque carte ».
*Correction (recommandée avant scellement)* : écrire la lecture de ce bras par clause : (i) faux acceptés parmi les faux à trait, bras 1 contre bras 2, et vrais rejetés contre bras 4 ; (ii) part d'abstentions à δ = 0 ; (iii) dépendance du bras 1 à la surface mesurée sur la vérité plantée : à classe fixée, écart de taux de « notable » entre témoins à trait et sans trait, intervalle par rééchantillonnage. Aucun verdict n'y sert de référence.

**4. Loi 2 : la valeur r n'est pas reliée à la grille.** « À taux égaux et symétriques, la valeur plantée vaut la ρ de la grille » est faux sous la loi 2 si r prend la valeur de la grille : la corrélation des erreurs d'une loi normale seuillée est plus basse que r. *Correction (de forme)* : dire si r est la valeur de la grille (et la valeur plantée l'intégrale) ou si r est résolu pour que la corrélation des erreurs égale la grille. La loi 2 est rapportée seulement.

**5. Niveau de l'écart ρ′ − ρ.** « Niveau 0,05 chacun » est lu sur un intervalle à 95 % aux centiles, dont la borne basse au-dessus de 0 est un test unilatéral à 0,025. *Correction (de forme)* : écrire « unilatéral à 0,025 ».

**6. Ordre dans le temps.** ρ se lit sur le bloc A (deux juges dans la même passe) ; ρ′ entre le bloc A et le bloc B, plus tard. Une dérive du service entre les deux baisse ρ′ seul et pousse ρ′ − ρ vers « nul ou négatif ». Le sens est prudent contre le « oui » ; *à dire dans les réserves*.

**7. Le témoin apparié, lu au plus près de la question.** La comparaison la plus directe, « la configuration contre un juge répété à coût égal », est U contre R-Argon (et F contre R-Argon) ; elle n'est pas nommée parmi les écarts rapportés. *Correction (de forme)* : rapporter ces deux écarts appariés, sans verdict, hors de Holm ; dire que « apparié » veut dire « au plus égal, nombre de votes impair » (R-Argon coûte 22 % de moins que le collège).

**8. Devis § 6 bis, arrondis.** « De l'ordre de 30 à 45 USD » pour 28,9 à 46,2, et « 60 à 90 » pour 57,8 à 92,4. *Correction (de forme)* : « 29 à 46 » et « 58 à 92 ».

**9. Q1, format.** La ligne « défaut sous 48 heures » du format de décision manque. *Correction (de forme)* : « défaut : (a), déjà appliquée ; elle ne joue rien de plus que GO-2026-11-19-63 ».

Aucun de ces constats ne change le choix de Lazar, la grandeur mesurée, le plan de 504 appels, les montants ni le plafond.

## Ce que je n'ai pas vérifié

- Le service réel des juges dans `juges_croises_v53.py` (dérivation de l'identifiant opaque comprise) : non ouvert ; la plomberie et les gardes le montreront.
- Les onze témoins de la version 2 : non ouverts au-delà de ce que le calcul lit (longueurs) ; P7 repose sur le texte.
- Aucun travail publié lu ; aucun chiffre de l'état de l'art employé par les pièces.

## Verdict

Scellable après corrections.

Les dix-sept corrections de la version 1 sont appliquées ; le calcul du devis se rejoue à l'octet et chaque chiffre recalculé est égal ; le plafond de 25 USD de GO-2026-11-19-66 est tenu, le pire cas étant écrit et laissé à la lecture de la mère ; le témoin « un juge, k votes » est à coût apparié ; les autres lignées sont chiffrées hors base, sans valeur de devis ; la question à Lazar sur `fefca0bd94064` est juste et au bon format. Les constats neufs 1 et 2 sont à corriger avant scellement (un seuil gelé que la vérité plantée elle-même peut faire échouer ; une règle de portée sans comparaison définie) ; le 3 est recommandé ; les 4 à 9 sont de forme. Ce sont des changements de texte localisés, sans effet sur le choix, la grandeur mesurée, le plan d'appels ou le montant : ils s'appliquent dans une version 3 (nom neuf) et se vérifient sur le différentiel ; rien n'appelle une relecture complète.

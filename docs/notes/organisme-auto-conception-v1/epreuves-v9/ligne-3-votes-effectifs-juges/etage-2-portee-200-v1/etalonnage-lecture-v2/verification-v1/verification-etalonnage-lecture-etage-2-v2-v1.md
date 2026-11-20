# Vérification des corrections — étalonnage et lecture unique de l'étage 2 (ligne 3), v2 — v1

Contre-lecteur, modèle S (même que la contre-lecture `c1dbd14e…`). Mandat `72c0f44f…`, en-tête compris. Aucun verdict réel lu ; rien sous `archives-reponses-modeles/` ; aucun appel, aucune dépense, aucune écriture dans le dépôt.

## Verdict : CONFORME

Les corrections 1 et 2 sont portées et essayées ; rien d'autre ne change. Deux recommandations sur le silence n° 18, non bloquantes, à la mère (§ 5).

## 1. Table et essais

- Table `aa39b2ce…` : 14 lignes `OK`. Empreintes recalculées égales à celles annoncées : etalonner `a67ebed3…`, lire `ee67e246…`, essais `225840dd…`, rapport `a72d6c06…`.
- Essais rejoués sur une copie neuve : **44 passed** (52,4 s).

## 2. Différentiels refaits

`diff -u` v1 → v2 refait pour les trois programmes (`refait-etalonner.diff`, `refait-lire.diff`, `refait-essais.diff`) : comparés aux trois différentiels du développeur, **seules les deux lignes d'en-tête (chemins et dates) diffèrent**. Lecture du différentiel de la lecture : il porte **à la lettre** mon `correction-n1-lire_ligne_3_v1.diff` (quatre lieux), plus le refus « la pièce porte un autre dossier » (`piece.get("dossier") != str(dossier)`, avant l'ouverture de l'audit et de tout verdict), les noms v2, l'import de l'étalonneur v2 par empreinte et l'additif 5 `581e97e5…` au manifeste. Le différentiel de l'étalonneur : le calcul (`etalonner`, `tableaux`, poids, seuils, règles, ρ) est **inchangé** ; ajoutés : `lire_construction`, `compter_reserves_tenues`, la clé de la pièce, `dossier`, les quatre arguments. Rien d'autre ne change.

## 3. Mon recalcul inchangé

Les fonctions d'estimation (`etalonner`, `tableaux`, appels du banc) sont identiques octet pour octet entre v1 et v2 (différentiel) ; le banc est le même (`79865552…`). Mon recalcul indépendant (`recalcul_independant_v1.json`, écart maximal 5,6e-16) vaut donc pour la v2.

## 4. Le comptage : le plant est-il retrouvé exactement ?

Oui. Le plant du développeur (3 essais, recalcul `attendu_reserves` hors programme) passe. **Mon propre plant**, différent (`essai_comptage_independant_v1.py`, avec compagnon) : Argon rend `reserves_tenues` faux au premier rendu sur les bons **citants** au fragment « voisins » conforme non citant ; Opus sur les mauvais `voisin_nomme` de niveau discret ; **un premier rendu d'Argon refusé deux fois** (absent). Mon recalcul par boucle simple depuis la banque et la table des fragments : strates (classe, citation, item planté, nature du fragment) **égales strate par strate**, `verdicts_absents_exclus` = 1 chez Argon, 0 chez Opus, `sur` = 99 chez Argon, 100 chez Opus, et les quatre marges (classe, citation, item, voisins) sommant au même total, non nul. **1 passed.**
Formats : journal (`fragments_sha256`, `temoins[].fragments[catégorie] = id`, champs classe/item/niveau/citation/moitié) et fichier de fragments (`conformes.voisins[].{id, citation, piege}`, `fautifs[].{id, categorie}`) relus contre `generer_temoins_ligne_3_v3.py` (l. 122-124, 852-855, 1774-1783) : conformes.

## 5. Silence n° 18

1. **Piège « reprise assumée » rangé selon sa seule citation** : à la mère, avec recommandation. Dans le générateur, `reprise_assumee` est un piège non citant, porté par la catégorie « voisins » (l. 107, 639) : il tombe donc dans `conforme_non_citant` avec les voisins simples. La surveillance des « voisins non citants » mêle les deux. Recommandation : une quatrième nature `conforme_piege_reprise_assumee` (le champ `piege` du fragment conforme est déjà lu dans le fichier) ; texte exact, dans `lire_construction`, boucle des conformes « voisins » : `nature[x["id"]] = "conforme_piege_reprise_assumee" if x.get("piege") == "reprise_assumee" else ("conforme_citant" if x["citation"] else "conforme_non_citant")`, avec `NATURES_VOISINS` complété. Non essayé. Garder tel quel reste lisible (la strate croisée porte la classe et la citation), mais ne sépare pas ce que la mère veut peut-être isoler.
2. **Comptage sur tous les verdicts présents de la moitié « étalonnage »** (et non les seuls témoins qui servent aux poids) : juste ; rapporté, sans seuil, sans effet sur les poids ; les absents sont exclus et comptés (essai de § 4).
3. **`fragments_sha256` de la banque non comparé** : juste, non bloquant ; recommandé de le comparer (le journal est lié au fichier de fragments par son empreinte, mais la banque ne l'est que par les métadonnées témoin par témoin, non par le contenu). Texte : dans `executer`, après `lire_banque`, lire le JSON de la banque et refuser si `objet.get("fragments_sha256") != fragments_sha` ; **les essais factices doivent alors poser ce champ dans la banque factice** (aujourd'hui `{"version": "factice", "items", "temoins"}`). À décider par la mère.

## 6. Forme de l'audit, rapport § 3 : suffit-elle à un agent neuf ?

Oui, avec une réserve de vérification. Y figurent : qui et quand ; fichier, UTF-8, compagnon au format `sha256sum` avec la commande ; les cinq clés avec la chaîne `piece` exacte ; quelle empreinte pour chaque champ ; les cinq contrôles contre la l. 350 avec leur objet de relecture ; l'exemple ; ce qui n'est pas dans l'audit. Recoupé dans le code d'appel : `entrees-servies/envoi-NNNNN.json`, `consigne_servie_sha256`, valeur `b03f33b8…` (l. 134), `envois` et `reponse_sha256` des verdicts (l. 1112). **Un point que je n'ai pas pu confirmer** : la phrase « (`lire_verdict`) rend `None` sur une réponse sans bloc JSON ou à quatre clés » (contrôle 3) : « à quatre clés » ne se déduit pas des pièces que j'ai lues (la consigne a cinq items) ; à relire par le développeur contre `juges_croises_v53.py` avant de la laisser à un agent neuf, ou à retirer.

## 7. Phrase corrigée et durcissement « dossier »

Silence « n° 12 de la mère » : texte juste (v1 : pièce déterministe sans chemin ; v2 : pièce liée au dossier, audit citant la première invalide pour une autre). Essai `test_v2_piece_liee_a_son_dossier` : deux dossiers, deux empreintes ; pièce recopiée, citée par un audit : refusée. L'additif nommera DOSSIER, un seul chemin absolu. Silence n° 17 : nommé, gardé, juste.

## 8. Ce que je n'ai pas fait

Je n'ai pas relu le code d'appel au-delà des recoupements du § 6. Je n'ai pas essayé les deux recommandations du § 5.

Contre-lecteur, modèle S.

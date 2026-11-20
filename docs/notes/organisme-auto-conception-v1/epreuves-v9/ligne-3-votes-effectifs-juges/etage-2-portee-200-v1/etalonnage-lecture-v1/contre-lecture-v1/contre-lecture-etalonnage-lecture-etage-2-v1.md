# Contre-lecture — étalonnage et lecture unique de l'étage 2 (ligne 3) — v1

Contre-lecteur, modèle S. Mandat `mandat-contre-lecteur-etalonnage-lecture-etage-2-v1.md` (`72c0f44f…`, recalculée égale). Aucun verdict réel n'existe ni n'a été lu ; aucune commande sur `archives-reponses-modeles/` ; aucun appel, aucune dépense, aucune écriture dans le dépôt. Décisions de la mère de 15:55Z prises comme lettre.

## Verdict : À CORRIGER (deux corrections, une certaine, une demandée)

1. **Correction 1 (n° 1, décision de la mère)** : `complet` doit être « cinq rendus obtenus ». Texte exact ci-dessous, essai joint.
2. **Correction 2 (voisins non citants)** : le comptage des cartes tombées sur `reserves_tenues` sur la moitié d'étalonnage **n'existe pas** dans le code. Texte exact ci-dessous.
Le reste est conforme. Après ces deux corrections et leurs essais, « Conforme » sous réserve de la vérification des corrections par moi (mandat).

## 1. Table, compagnons, essais

- Table : 8 lignes `OK` ; empreintes de la table (`28d73687…`), du banc v4 (`79865552…`) et du mandat du développeur (`b432ce7e…`) égales aux valeurs du mandat.
- Essais rejoués sur une copie : **37 passed** (41,75 s), deux fois (copie neuve ; copie portant la correction 1 : 37 passed, 37,7 s).

## 2. Le code contre la lettre (lu en entier : étalonnage 482 lignes, lecture 752 lignes)

Conforme : étalonnage sur la seule moitié « étalonnage » (refus par le nom avant ouverture, refus par le contenu avant usage) ; poids, seuil, règle de C et P et ρ d'étalonnage par les fonctions du banc (l. 218, 219, 297) ; lecture unique (rapport existant, dossier existant, pièce non scellée, audit absent ou antérieur, exécution plus récente, journal d'une autre empreinte : tous refusés **avant** l'ouverture d'un fichier de verdicts) ; étalonnage recalculé et exigé égal ; racine 2026111936 seulement sur additif par chemin et empreinte, table de clés 1 à 5 gelée, `SeedSequence(racine, spawn_key=(clé,))`, 2 000 tirages ; table en issue B (rangs 1 et 3 seuls, `OUI_POSSIBLE = False`, garde « oui » interne) ; « non concluant par manque de témoins » ; juge « non mesuré » (10 %, moitié) ; audit « trop propre » / « trop sale » (l. 348, 349) ; rapports et manifestes scellés (R9) ; lecture par colonne ; H-sévérité.
**Banc sans réécriture** : `charger_banc` lit les octets, compare l'empreinte avant tout import, exécute ces octets sous un nom privé ; aucune des fonctions du banc (`cov_intra_classes`, `rho_moyenne`, `rho_paire`, `votes_effectifs`, `tronquer_votes`, `motifs`, `comptes_configurations`, `tirer_comptes`, `cov_depuis_comptes`, `_centiles`, `intervalles_rho_moyenne`, `ee_depuis_comptes`, `score`, `seuil_milieu`, `appliquer_seuil`, `poids_*`, `regle_choisie`, `mot_fa38`) n'est redéfinie dans les deux fichiers ; tout passe par `banc.`. Conforme.

## 3. Recalcul indépendant

`recalcul_independant_v1.py` (fractions exactes, sans numpy pour mon calcul) sur 200 témoins (100 bons, 100 mauvais), quatre colonnes d'erreurs plantées (comptes de configurations connus) : ρ moyenne 0,3421172194457065 (banc : …069), ρ paire 0,3421580457831584, ρ′ Opus 0,5546300279534406, ρ′ Argon 0,6079111910547028, ρ′ − ρ (Opus, ρ paire) 0,2124719821702823, votes effectifs 1,4901828029790114 : écart maximal avec les fonctions que le code appelle **5,6e-16**. Le montage du code (colonnes 0-1 pour ρ, 0-2 et 1-3 pour ρ′, centrage par classe, division par n − 2) est conforme à mon calcul.

## 4. Les quatorze silences (rapport § 6, numérotation du rapport)

| n° | avis |
|---|---|
| 1 | **À corriger** (décision de la mère). Voir correction 1. |
| 2 | Juste ; garder (décision). Le code le fait et un essai le montre. |
| 3 | Juste ; garder. Voir § 5 : la forme est presque assez écrite ; il manque trois précisions. |
| 4 | Juste (l. 343). |
| 5 | Juste : issue B, ni Holm ni probabilité. |
| 6 | Juste : le seuil de stabilité ne sert qu'au rang 2. |
| 7 | Juste (l. 291). |
| 8 | Juste, avec un point nouveau (n° 17 ci-dessous). |
| 9 | Juste ; bon choix (la lettre ne prévoit rien). |
| 10 | Juste ; à la mère à titre d'information : erreur brute et non équilibrée ; avec classes égales et sans absent, elles coïncident. |
| 11 | Juste. |
| 12 | (« Aucune erreur sur les 200 ») : juste. |
| 13 | (place fixe du rapport) : **le code est bon, le texte du rapport est faux sur un point** ; voir § 6. Le « n° 12 » de la mère est ce n° 13 du rapport. |
| 14 | Juste. |
| 15, 16 | Justes. |

**Nouveau, n° 17 (à la mère, avec recommandation)** : le ρ de « ρ′ − ρ » n'est pas le ρ rapporté. Le rapport donne ρ entre juges par `rho_moyenne` sur le bloc A (200 tentés) ; l'écart ρ′ − ρ utilise `rho_paire(0, 1)` sur les témoins complets des deux moitiés. Les deux valeurs sont presque égales (mon plant : 0,34212 contre 0,34216), mais le texte (l. 157, 159, 293) ne dit pas laquelle sert à l'écart. Recommandation : garder (la ρ′ est une corrélation de paire ; pour deux juges, ρ paire est le pendant exact) et le **nommer dans l'additif**.

## 5. Forme de l'audit de symétrie (n° 3) : assez écrite ?

Presque. Un agent neuf trouve au rapport § 6 n° 3 la chaîne `piece` exacte, les trois empreintes et les cinq clés, avec « tenu » / « non tenu ». Ce qui manque pour écrire sans lire le code : (a) laquelle des empreintes : `banque_sha256` = empreinte de la banque scellée ; `rapport_execution_sha256` = celle de `rapport-execution-K.json` (l'argument `--rapport-execution-sha`) ; `etalonnage_sha256` = celle de la pièce d'étalonnage (donc l'audit s'écrit **après** l'étalonnage) ; (b) le format du compagnon : `HEX␣␣nom` au format de `sha256sum`, JSON en UTF-8, et l'ensemble de clés de `controles` **exactement** les cinq (aucune de plus, aucune de moins ; des clés en plus au niveau supérieur sont tolérées) ; (c) un exemple complet et le sens de chacun des cinq contrôles contre la l. 350 (vérité non servie ; empreinte de la consigne ; lecteur rend « absent » pour illisible ; appariement ; juges scriptés parfait et hasard) — sans quoi l'auteur devine le programme à relancer. Les déclencheurs « trop propre / trop sale » ne sont **pas** dans l'audit : ils sont calculés par la lecture ; à dire aussi.

## 6. n° 13 du rapport (« DOSSIER », décision de la mère : un seul chemin absolu)

Rien à changer au code : `lire` prend `DOSSIER = parent du parent` de `--etalonnage` (chemin résolu) ; l'additif nommera un seul chemin absolu. **Une phrase du rapport est inexacte** : « une relecture dans un autre dossier demande un étalonnage et un audit neufs ». La pièce d'étalonnage est déterministe et **ne contient aucun chemin de dossier** : le même étalonnage rejoué dans un autre dossier donne la même empreinte, et l'audit déjà scellé (qui cite cette empreinte) reste valable. Seul un étalonnage neuf est donc nécessaire, non un audit neuf. Correction du texte : « … demande un étalonnage rejoué dans ce dossier ; la pièce étant la même, l'audit écrit reste valable ; le programme ne peut pas l'empêcher seul : l'additif nomme DOSSIER ». Durcissement facultatif (la mère a dit : rien à changer ; non demandé) : ajouter `"dossier": str(Path(dossier).resolve())` au dictionnaire `piece` de `executer` (étalonneur, après `"n_temoins_de_la_banque"`) lierait l'audit au dossier ; le recalcul de `lire` ne compare que cinq clés et ne casse pas.

## 7. Corrections exactes

### Correction 1 — témoin complet = cinq rendus obtenus (`lire_ligne_3_v1.py`)

Diff complet : `correction-n1-lire_ligne_3_v1.diff`. Quatre lieux :
- `tableaux_complets` (l. 187 à 195) : après `present = np.zeros_like(tente)` ajouter `obtenu = np.zeros_like(tente)` ; dans la boucle, avant `v = …` : `obtenu[i, c] = par_temoin[t][(j, r)]["etat"] == "obtenu"` ; `return y, tente, vote, present, items, obtenu`.
- l. 401 : `y, tente, vote, present, items, obtenu = tableaux_complets(ids, bq, par_temoin)`.
- l. 405 : remplacer `complet = tente.all(axis=1)` par `complet = obtenu.all(axis=1)` et ajouter `complet_tentes = tente.all(axis=1)`.
- l. 415 à 419 (`r["temoins"]`) : ajouter `"complets_cinq_rendus_tentes": int(complet_tentes.sum())` et `"complets_moitie_lecture_tentes": int((complet_tentes & lec).sum())` ; remplacer la définition par « les cinq rendus obtenus (état « obtenu » du code d'appel, verdict lisible ou non ; un rendu « absent » après rejeu refusé n'est pas obtenu) ; le compte des témoins aux cinq rendus tentés est rapporté à côté ».
Inchangé : `bloc_a` (deux premiers rendus tentés ; un absent compte comme rejet, l. 155) ; l'étalonnage.
Essai (`essai_correction_n1_v1.py`, deux tests) : un rendu du bloc B du premier témoin de la moitié « lecture » refusé deux fois, arrêt après 40 témoins : le code d'appel compte 39 complets ; **sur le code d'origine la lecture rend 40 (échec : `assert 40 == 39`)** ; sur le code corrigé, 39, rang 1 « non concluant par manque de témoins », 40 rapporté à côté ; cas sain : les deux comptes égaux. Les 37 essais d'origine passent avec la correction.

### Correction 2 — comptage « cartes tombées sur reserves_tenues » à l'étalonnage (`etalonner_ligne_3_v1.py`)

Absent des deux programmes (`reserves_tenues` n'y figure que dans `ITEMS` ; la lecture ne rend que « lecture seconde » et `par_citation_bons` sur le bloc A, après la lecture, non sur la moitié d'étalonnage seule). Ajout dans `etalonner`, après `y, _, vote = tableaux(lus, banque, par_temoin)` (l. 357), calcul sur les premiers rendus des témoins lus, par juge et par classe, de « verdict présent dont l'item `reserves_tenues` est faux » :
```
    tombees = {}
    for j in JUGES:
        cnt = {k: [0, 0] for k in ("bons_citants", "bons_non_citants", "mauvais_item_reserves_tenues", "mauvais_autres_items")}
        for t in lus:
            v = par_temoin[t][(j, 1)]["verdict"]
            if v is None:
                continue
            b = banque[t]
            k = (("bons_citants" if b["citation"] else "bons_non_citants") if b["classe"] == "bon" else
                 ("mauvais_item_reserves_tenues" if b["item"] == "reserves_tenues" else "mauvais_autres_items"))
            cnt[k][1] += 1
            cnt[k][0] += int(v["items"]["reserves_tenues"] is False)
        tombees[j] = {k: {"compte": a, "sur": s} for k, (a, s) in cnt.items()}
```
et, dans le dictionnaire rendu : `"cartes_tombees_sur_reserves_tenues_premier_rendu": tombees`. Rapporté, sans seuil ; la pièce scellée le porte ; la lecture ne compare que cinq clés, donc compatible. **Je l'ai écrit sans l'essayer** ; un essai à plant (un bon non citant rejeté sur `reserves_tenues`) est à écrire par le développeur. J'ai lu « voisins non citants » comme « bons témoins sans citation de travail » (champ `citation` de la banque) ; si la mère veut une autre définition, la dire.

## 8. Écarts du développeur (§ 7 du rapport)

Les six écarts sont des lectures et recherches hors consigne, sans conséquence sur le code. Rien à ajouter ; l'écart 2 (additif 5 v2 de la branche, non la version de `main`) reste à vérifier à la mère.

## 9. Mes propres écarts

Aucun refus de permission. J'ai lu le code d'appel à deux endroits seulement (`comptes_complets`, recherche de mots) et le banc aux lignes 440-700 et 940-950. Les corrections sont essayées dans ma copie, jamais dans le dépôt.

Contre-lecteur, modèle S.

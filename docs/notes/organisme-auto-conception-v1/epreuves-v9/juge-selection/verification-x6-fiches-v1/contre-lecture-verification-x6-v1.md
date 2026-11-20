# Contre-lecture — vérification X6 contre le fichier des cartes — v1

Contre-lecteur, modèle S. Mandat de référence : `mandat-developpeur-verification-x6-fiches-v1.md` (GO-2026-11-20-23). Commit lu : 9c46f7d3. Aucun accès au vrai fichier des cartes ni à `archives-reponses-modeles/`.

## Verdict : Conforme

## Empreintes vérifiées (`sha256sum -c` contre chaque compagnon : OK)

| Fichier | Début de l'empreinte |
|---|---|
| `verifier_x6_contre_fiches_v1.py` | d8f84db2 |
| `essais_verifier_x6_contre_fiches_v1.py` | d57a8f92 |
| `rapport-developpeur-verification-x6-v1.md` | f44491f4 |
| `mandat-developpeur-verification-x6-fiches-v1.md` | 9e2b80a1 |

## 1. Le programme ne fait que ce que le mandat permet

- Empreinte avant décodage : `executer` lit les octets (l. 97-98), calcule les deux empreintes (l. 99-100), refuse si l'une diffère (l. 101-104), puis seulement décode (l. 106, 108). Le décodage porte sur les mêmes octets que ceux empreintés.
- Fiches : le crochet `_seulement_les_cles` (l. 34-36) jette toute valeur dès le décodage, à tous les niveaux ; seules les clés du premier niveau sont gardées ; racine non objet et clé en double refusées.
- Extraction : seule `identifiants_par_classe.a_corriger` est lue (l. 68-80) ; exactement deux chaînes distinctes exigées. L'extraction est décodée en entier par `json.loads` (inévitable), mais aucun autre champ n'est lu ni gardé.
- Sortie : trois champs, `nombre_de_cles`, `retenues_presentes` (booléens), `empreintes` ; contrôle explicite avant écriture (l. 117) ; écriture en mode exclusif `xb` ; compagnon au format `sha256sum`.
- Aucun identifiant affiché : tous les motifs de `Refus` sont des chaînes fixes ; `from None` coupe les chaînes d'exceptions ; `principal` attrape `Refus` puis toute `Exception` et n'affiche qu'un motif fixe, donc aucune trace ; `_Analyseur.error` n'imprime pas les arguments. Bibliothèque standard seulement.
- Remarque mineure, sans incidence : si l'écriture du compagnon échoue après celle de la sortie, la sortie reste seule. Cas non couvert par un essai ; le jeu serait de toute façon détecté par l'absence du compagnon.

## 2. Aucun moyen en ligne de commande de changer les empreintes

- Trois options seulement (l. 141-143), `allow_abbrev=False`, `add_help=False` ; `principal` passe toujours `EMPREINTE_FICHES` et `EMPREINTE_EXTRACTION` (l. 146-147) ; aucune lecture d'environnement. Les constantes sont celles du mandat (ba65c411… et f5c7cc1c…, entières comparées dans les essais).
- Les essais remplacent les constantes par `monkeypatch` ou appellent `executer` avec des paramètres, sans option en ligne de commande.

## 3. Essais lancés par moi sur une copie

`python3 -B -m pytest -q -p no:cacheprovider essais_verifier_x6_contre_fiches_v1.py` : **33 passés, 0 échoué**. Chaque garde a son cas sain et son artefact : empreinte (cas sain / fausse de chaque fichier / avant décodage), forme de l'extraction (deux retenues / zéro, une, trois, doublon, non-chaîne, classe absente), fichiers de sortie (neuf / existant ou compagnon existant), trois champs (sain / quatrième champ imposé), fuite (sortie, compagnon et écran, sur succès et sur refus), options (source à trois options / options d'empreinte refusées).

## 4. Défauts glissés (R4), copies jetables dans le bloc-notes

| Défaut | Essais | Vu par |
|---|---|---|
| M1 : un identifiant dans le motif de refus (doublon) | 1 échec | `test_extraction_mal_comptee[retenues3]` |
| M2 : décodage de l'extraction avant la vérification d'empreinte | 1 échec | `test_empreinte_verifiee_avant_decodage` |
| M3 : quatrième champ `retenues` dans la sortie | 6 échecs | cas sain, ordre, trois champs, aucun identifiant, écran |
| M4 : option `--empreinte-fiches` en ligne de commande | 1 échec | `test_aucune_option_d_empreintes_en_ligne_de_commande` |

Tous vus. Réserve de couverture sans gravité : pour M4, seul l'essai du source compté l'attrape ; `test_option_d_empreinte_refusee` passerait encore, car une mauvaise empreinte donne un refus. Le garde-fou reste le décompte des options.

## Refus

Aucun refus de permission, de classifieur ou de garde.

Contre-lecteur, modèle S.

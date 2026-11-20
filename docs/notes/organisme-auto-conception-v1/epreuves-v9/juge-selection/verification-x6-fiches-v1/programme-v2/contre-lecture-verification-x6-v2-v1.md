# Contre-lecture — programme de vérification X6, version 2 — v1

Pièce de travail (classe C). Contre-lecteur, modèle S. Agent neuf. Python 3.13.18.

## Verdict : Conforme

Aucune correction exigée. Une remarque non bloquante (voir fin).

## Empreintes vérifiées contre leurs compagnons (toutes OK)

- mandat du contre-lecteur `2456cb0e…1fae7` ;
- `verifier_x6_contre_fiches_v2.py` `91833df0…` ;
- `essais_verifier_x6_contre_fiches_v2.py` `ddc992d2…` ;
- `rapport-developpeur-verification-x6-v2.md` `b7ad0d61…` ;
- mandat du développeur et compte rendu du jeu du v1 : compagnons OK.

## Points du mandat

1. Chemin lu : `objet["extraction"]["identifiants_par_classe"]["a_corriger"]` (l. 71-79). Un refus propre à chaque niveau : racine non objet, `extraction`, `identifiants_par_classe`, `a_corriger` absents ou mal formés. Exactement deux éléments, tous des chaînes, distincts (l. 80-85). OK.
2. Ordre : sortie ou compagnon existant, puis lecture des octets, empreintes comparées avant tout décodage (l. 95-110), puis extraction décodée et validée (l. 114), puis cartes décodées en clés seulement (l. 116). Un refus de l'extraction sort avant l'appel de `_cles_des_fiches`. OK.
3. Constantes `EMPREINTE_FICHES` et `EMPREINTE_EXTRACTION` identiques au v1 (comparées ligne à ligne). Le point d'entrée passe les constantes. Trois options seulement, `allow_abbrev=False`. Aucune option d'essai. OK.
4. Messages de refus lus un par un : motifs fixes, aucun f-string avec une valeur. Les `raise ... from None` coupent les messages d'exception d'origine (JSON, fichier). L'erreur d'arguments n'écho rien. Écran de succès : « FAIT ». OK.
5. Sortie : trois champs, contrôle `tuple(sortie) != CHAMPS_SORTIE`, ouverture en `xb` pour la sortie et le compagnon, refus si l'un des deux existe. Écriture non atomique : un échec sur le compagnon laisse la sortie. Sans conséquence, un nouveau jeu exige un nom neuf. OK.
6. Essais : **44 passés, 0 échoué**. Lancés sur des copies vérifiées par empreinte dans mon dossier (`.../contre-lecture-verification-x6-v2/copie/`), car les essais écrivent dans `essais-fichiers/` à côté d'eux et le mandat interdit toute écriture dans le dépôt. Le dossier du dépôt n'a pas été utilisé pour le lancement.
7. Essai de « forme réelle » : clés racine, clés sous `extraction`, et `identifiants_par_classe` ne contenant que `a_corriger`, en accord avec le compte rendu (chemin sous la clé racine `extraction`). Il passe aussi par le chemin de l'exécution avec un JSON indenté à clés triées. Extraction réelle non ouverte. OK.

## Mutations à la main (copies dans mon dossier)

| Mutation | Résultat |
|---|---|
| M1 : chemin à un niveau (`niveau = objet`) | attrapée, 9 échecs sur 44 |
| M2 : cartes décodées avant l'extraction (échange propre des lignes 114-117) | attrapée, 2 échecs (les deux essais d'ordre) |
| M3 : liste des identifiants dans le message de refus du nombre | attrapée, 4 échecs (marque dans le message et à l'écran) |
| M4 : suppression du refus « compagnon existe » | attrapée, 1 échec (`sortie.json.sha256` préexistant) |

Une première version de M2 (mal faite par moi) a planté par `UnboundLocalError` ; refaite proprement, voir ci-dessus.

## Complément de mandat (condition de la mère, R-4122) : forme réelle

Forme à reproduire : `{"extraction": {"identifiants_par_classe": {"a_corriger": [deux chaînes]}}, …}`, avec d'autres clés racines possibles à côté de `extraction`. Extraction réelle non ouverte.

- `_objet_extraction` (essais, l. 53-72) reproduit exactement cette forme : sous `extraction`, `identifiants_par_classe` ne contient que `a_corriger`, liste de deux chaînes ; huit autres clés racines à côté (`chemin`, `commit`, `fichiers_trouves`, `issue`, `octets_journal`, `sha256_journal`, `suffixe`, `version`). `test_forme_identique_a_l_extraction_reelle` en fige les clés à chaque niveau et joue le programme sur une copie indentée à clés triées : résultat 94 clés, `[False, False]`.
- Cas sain : `test_cas_sain`, `test_retenue_presente_dans_l_ordre`, `test_deux_retenues_presentes_ordre_inverse` et l'essai de forme réelle, tous sur cette forme.
- Un artefact par garde, tous passés et tous sans identifiant dans le message :
  - racine non objet : `[RETENUES_ABSENTES]` ;
  - `extraction` absent, de type liste, de type chaîne : trois cas ;
  - `identifiants_par_classe` absent ou liste : deux cas ;
  - `a_corriger` absent ou objet : deux cas ;
  - forme du v1 (sans niveau `extraction`) : un cas ;
  - nombre : une, trois, zéro retenue ;
  - égalité : deux identifiants égaux ;
  - type : un élément non chaîne.
- Réserve : le dossier ne montre pas que `a_corriger` soit la seule clé de `identifiants_par_classe` dans le réel ; le programme ne l'exige pas, il lit seulement `a_corriger`, donc d'autres clés voisines seraient sans effet. Aucun essai ne le teste.

Conclusion : l'essai de forme réelle reproduit exactement la forme indiquée. Verdict inchangé : Conforme.

## Commande unique de jeu

```
python3 -B verifier_x6_contre_fiches_v2.py --fiches CHEMIN_DES_CARTES --extraction CHEMIN_DE_sortie-extraction-x6-v2.json --sortie CHEMIN_NEUF.json
```

`CHEMIN_NEUF.json` : nom neuf, ni lui ni son compagnon n'existent.

## Remarque non bloquante

Les essais créent `essais-fichiers/` à côté d'eux : à lancer hors du dépôt, ou à supprimer ensuite.

Contre-lecteur, modèle S.

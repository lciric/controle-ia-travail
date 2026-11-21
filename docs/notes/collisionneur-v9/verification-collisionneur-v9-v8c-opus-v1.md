# Vérification des corrections : collisionneur v9 version 8c et garde des réglages de Google version 3

Écrite le 21 novembre 2026, de 20:28Z à 20:50Z (`date -u`), par Claude Opus 5.5 (`claude-opus-5-5`), vérificateur neuf : je n'ai rien écrit de ces pièces. Je tiens le rôle de Claude Fable 5.2, à sa limite d'usage jusqu'au 24 novembre 05:00Z. Écart déclaré par la mère : la vérification des corrections revient d'ordinaire au même contre-lecteur ; Fable relira à son retour. Pièces d'instrument (classe B).

Ce que je n'ai pas fait : aucun envoi réel, aucune clé lue (essais sous `env -u` des sept clés, doublures à clés factices, réseau interdit par les essais eux-mêmes) ; aucun commit, aucune poussée ; aucun fichier du dépôt modifié hors cette pièce et son sceau. Mutations, sondes et correction sur des copies, dans mon bloc-notes. Je n'ai lu aucune réponse de modèle : les copies de dossiers sont fabriquées par l'outil du développeur depuis les seuls journaux et fiches d'espèces versés, à contenus factices.

## Verdict

**À corriger : une correction obligatoire (C-1) et un essai témoin à ajouter (C-2).** Tout le reste est conforme.

- **C-1, obligatoire : le devis de reprise sous-compte le pire cas « avec relances ».** La version 8c donne trois envois payés au plus à une cellule de Google à plafonds égaux : le premier, la relance identique, le dernier recours. Le devis de reprise ne compte qu'une relance par cellule. La phrase du devis par étage (« une relance […] peut ajouter jusqu'au double du pire cas ») est fausse pour ces cellules. Sur les copies des quatre dossiers, l'écart va de 2,55 à 11,23 USD par dossier (section 6). La garde par envoi, elle, tient : aucune dépense ne dépasse le plafond du dossier ni la ligne, mes sondes le montrent.
- **C-2, essai témoin : une mutation neuve de la garde survit aux deux suites.** C'est le plancher de 16 000 jetons de texte contrôlé en flux seulement. Le code de la garde est juste, mais aucun essai ne l'éprouve en appel non diffusé (le lot) : dans le collisionneur, la règle du plafond large (`REGLE_TEXTE_MIN`) refuse avant la garde et masque le défaut. Or un autre script qui emploie la garde commune en lot ne compterait que sur elle.
- **Conforme** :
  - chaque remarque de Fable et chaque décision de la mère, au lieu dit ;
  - l'écart de lieu des déclarations : il est sûr, aucun envoi ne part sans la garde des réglages appliquée au corps même de l'envoi ;
  - la garde v3 sur les trois règles et sur les défauts après la réponse ;
  - trois envois ne dépassent jamais le plafond du dossier ni la ligne ;
  - essais rejoués : 403 passés, 1 sauté ;
  - mutations : trois neuves prises sur quatre.

## 1. Pièces et empreintes

Empreintes recalculées par `sha256sum`, toutes égales à leurs compagnons `.sha256` et aux préfixes donnés :

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/verification-corrections-collisionneur-v9-v8-fable-v1.md` | `9cf6799fcf8d48acec9f505929caaf97d516c7d8f443b9df3fbf7d115dbd9a86` |
| `docs/notes/collisionneur-v9/rapport-developpeur-collisionneur-v9-v8c-v1.md` | `1cd67446bf1a32b236c8aa8dcf271d009726179aec20d61fadb7e508573c8e00` |
| `docs/notes/collisionneur-v9/collisionneur_v9_v8c.py` | `a3fc279ed1754db250016131656671d0639d03749bc62dff88b99a2b72b5b531` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8c.py` | `f7136092c5d76533227dff87c9403eb29f33cb803377497f0f999bf524274f7e` |
| `src/controle_ia/garde_google_v3.py` | `923679b51cfc84b65ff7cfc65296378d08e6d4e64f6b427823d23ba24f4afe91` |
| `tests/test_garde_google_v3.py` | `aceabdb2b35ec62fedf982281b1de76a6a02f651ff5cfa3391831e05825a122a` |
| pour comparaison : `docs/notes/collisionneur-v9/collisionneur_v9_v8b.py` | `6cd0209c10118ff58d5ad3b6e2cc3e3c52c33aa155db2df96f53b9d5786f4c9b` (= R-4686) |
| pour comparaison : `src/controle_ia/garde_google_v2.py` | `9d39a7496d0a7b36197e369d12fe1e72d1d878abca2d9d8d764c4750ed91473b` (= R-4686) |
| pour mémoire : `docs/notes/collisionneur-v9/rapport-developpeur-collisionneur-v9-v8b-v1.md` | `87f845f2d23963484c7b8e0eee8b5c4dab17e12b5d9453ecaa18203dbd724e5b` |

Comparaisons par `diff`. **De la v8b à la v8c**, il n'y a que les changements annoncés et rien d'autre :
- l'en-tête, les lignes d'emploi et `VERSION` ;
- l'import de la garde v3 ;
- `etape_de_relance` ;
- la condition de blocage de `reglage_en_defaut` ;
- la docstring de `executer_cellule` ;
- la ligne de la relance identique dans la garde d'avant le comptage ;
- le plan à trois étapes ;
- la reprise à l'étape suivante ;
- la branche « identique » ;
- le déplacement des déclarations ;
- la condition d'étape suivante après `MAX_TOKENS` sans texte.

**De la garde v2 à la garde v3** : l'en-tête, `VERSION_GARDE`, la table par espèce `JETONS_PAR_MOT_MESURES`, les mesures `MESURES_JETONS_PAR_MOT`, et `JETONS_PAR_MOT` devenu le plus haut de la table.

## 2. Essais rejoués

Commande donnée, `--basetemp` neuf dans mon bloc-notes, de 20:33:20Z à 20:33:58Z :

```
env -u OPENAI_API_KEY -u OPENAI_API_KEY_2 -u GEMINI_API_KEY -u GEMINI_API_KEY_2 -u GEMINI_API_KEY_3 -u GEMINI_API_KEY_FREE -u MISTRAL_API_KEY PYTHONPATH=src timeout 1500 .venv/bin/python -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v8c.py tests/test_garde_google_v3.py -p no:cacheprovider --basetemp=…/verif-v8c-opus/basetemp-temoin
```

**403 passés, 1 sauté, en 37,67 s** (code 0), soit 359 et 44, les comptes du développeur. Le sauté est la copie « dopamine », non désignée.

## 3. Remarques de Fable et décisions de la mère, au lieu dit

| source | ce qui est demandé | lieu dans la v8c ou la garde v3 | verdict |
|---|---|---|---|
| Fable K-1 | `reglage_de_relance(m)` avant `reglage_en_defaut` | ligne 1809, avant `etape_de_relance` (neuve) puis `reglage_en_defaut` (1828) ; texte de Fable | conforme |
| Fable K-1 | garde d'avant le comptage sur le réglage de relance | lignes 1941 à 1944 : premier envoi, relance identique (ajout de la v8c), réglage de relance | conforme |
| Fable K-1 | bloc de la relance : garder le niveau, relever le plafond ; dernier recours seulement à plafonds égaux ; repli : moitié du budget au dernier recours seulement | lignes 1982 à 1996, texte de Fable, précédé de la branche « identique » (1975 à 1981) | conforme |
| Fable K-1 | déclaration du dernier recours au journal et à l'écran, avant l'envoi | lignes 2017 à 2029, après les gardes de dépense : écart de lieu déclaré, examiné en section 4 | conforme (sûr) |
| Fable K-1 | textes à accorder : docstring, commentaire de `NIVEAU_CORRIGE`, en-tête | docstring 1908 à 1914 ; commentaire 409 à 411 ; en-tête v8b (lignes 92 à 100) et v8c (101 à 107) | conforme ; trois commentaires restés anciens (remarque 1) |
| Fable K-1 | trois essais | `test_k1_relance_garde_le_niveau_et_releve_le_plafond`, `test_k1_dernier_recours_declare_quand_aucun_plafond_plus_haut` (accordé : trois envois), `test_k1_reprise_apres_un_premier_defaut_releve_le_plafond` | conforme |
| Fable K-2 | Argon à 65 536 en flux dans la garde | `LIMITES_SORTIE["argon"]["flux"] = 65536`, source citée (page versée, ligne 931) | conforme |
| Fable K-2 et mère R-4686 | rapport de jetons par mot par espèce, au plus haut mesuré de chacune (Carbon 4,2) | `JETONS_PAR_MOT_MESURES = {"argon": 5.1, "carbon": 4.2, "neon": 5.1}` ; mesures écrites dans le module, déduites par essai (arrondi au dixième supérieur de 5,06 et 4,11) | conforme ; Neon, sans mesure, pris à 5,1 : choix du développeur, déclaré (remarque 5) |
| Fable K-2 | `jetons_par_mot=None` dans la signature, rapport de l'espèce par défaut | `verifier_reglages_google(…, jetons_par_mot=None)`, première ligne du corps après le contrôle d'espèce | conforme |
| Fable K-2 | Argon `max` et `max_relance` à 65 536 au catalogue | ligne 315 | conforme |
| Fable K-2 | source du rapport dans l'en-tête du module | en-têtes v2 et v3 : branche `runs/collisionneurs-reprise-minuit-v1`, 43 réponses, note de Fable `9cf6799f…` | conforme |
| Fable, remarque 1 | trois essais témoins | `test_cl_v8_bord_exact_des_16000_jetons_de_texte` (garde), `test_cl_v8_lot_fini_dit_par_son_etat_seul`, `test_cl_v8_deux_lignes_de_reprise_la_derniere_borne` (collisionneur), textes de Fable | conforme |
| Fable, remarques 2 à 4 | aucune correction demandée ; versement des fichiers cachés | v8c, ses essais, la garde v3 et ses essais sont versés (commit `25986189e`) ; la v8b et la garde v2 ne le sont pas (remarque 7) | conforme pour la v8c |
| mère R-4664 | `SAFETY` et `RECITATION` définitifs ; Carbon à 65 536 en flux | `REFUS_GEMINI` → statut « REFUS », jamais relancé (`lancer_etage` bloque) ; catalogue de Carbon à 65 536 | conforme |
| mère R-4675 | lecture des lignes : 30 et 17 USD sont les restes | code de la ligne de reprise inchangé depuis la v8 (aucune différence au `diff`) | conforme |
| mère R-4686 | avant le dernier recours, une relance identique, journalisée | plan `[(max, premier), (max_relance, identique), (max_relance, relance)]` si `reglage_de_relance(m)[1]` ; ligne `relance_identique_declaree`, marque `identique: true`, « RELANCE IDENTIQUE DÉCLARÉE » à l'écran ; reprise à l'étape suivante (`etape_de_relance`) ; essais `test_v8c_…` | conforme |

## 4. L'écart de lieu des déclarations est sûr

L'ordre dans la boucle de `executer_cellule` va de la ligne 1971 à la ligne 2040 :
1. réglage de l'envoi : `envoi_m` et `correction` ;
2. **garde des réglages sur le corps même de l'envoi** (`demande_gemini(envoi_m, prompt, max_tokens)`, avec la limite de mots du tour, le mode, le niveau ou le budget attendus), avec refus avant envoi ;
3. garde du plafond du dossier ;
4. garde de la ligne ;
5. déclarations ;
6. écriture de l'invite ;
7. envoi.

L'appelant reconstruit le même corps par `demande_gemini` et le repasse à la garde, sans la limite de mots, en défense en profondeur. Le seul lieu d'envoi de génération du script est la ligne 2040. Les deux seuls points d'arrivée chez Google sont `streamGenerateContent` (ligne 1129) et `batchGenerateContent` (ligne 1246), chacun précédé de cette double garde. Le comptage `countTokens` part après la garde d'avant le comptage ; ce n'est pas une génération (remarque 8).

Sondes (fichier `test_sondes_opus_v8c.py`, 17 passées), sur les trois espèces :
- une espionne enregistre chaque appel de la garde et chaque envoi. Chacun des trois envois est précédé d'une garde sur un corps identique octet pour octet, avec la limite de mots du tour et sans aucun problème ;
- les niveaux envoyés sont, dans l'ordre, le plus haut, le même, puis le niveau corrigé ;
- au journal, l'ordre est le suivant : essai 1, relance identique déclarée, essai 2, dernier recours déclaré, essai 3 ;
- une garde qui refuse la relance identique : un seul envoi, aucune déclaration, refus « REGLAGES_GOOGLE » au journal ;
- une ligne qui refuse le dernier recours : aucune déclaration du dernier recours.

L'écart a un mérite : un envoi refusé n'est jamais déclaré. Il a une limite sans gravité : une déclaration peut être écrite deux fois pour un même envoi, et c'est toujours une déclaration de trop, jamais un silence (remarque 2).

## 5. La garde v3

| règle de `CLAUDE.md` (GO-2026-11-21-71) | code | essais qui la tiennent | sonde |
|---|---|---|---|
| réglage de réflexion explicite : niveau le plus haut admis, ou budget prévu en repli déclaré | `thinkingLevel` exigé, admis pour l'espèce et égal au niveau attendu (par défaut le plus haut) ; `thinkingBudget` interdit avec un niveau ; en repli, budget égal au prévu, positif, au plus la provision, sans niveau ; `includeThoughts` vrai | `test_un_essai_par_reglage_manquant` (onze cas), `test_niveau_attendu_explicite`, `test_repli_declare_au_budget` | mutation M4 prise |
| plafond au moins réflexion plus 16 000 jetons de texte, au plus la limite de l'espèce pour le mode | `maxOutputTokens` entier ; `plafond − provision < 16000` refusé ; limite par espèce et par mode | `…[texte sous 16 000]`, `test_cl_v8_bord_exact…`, `test_limites_versees_par_mode` | **mutation M2 non prise : C-2** |
| limite de mots dans le plafond de texte, au rapport de l'espèce | `⌈mots × rapport de l'espèce⌉ ≥ plafond − provision` refusé | `test_limite_de_mots_bord`, `test_v2_rapport_mesure_par_espece` | mutation M1 prise ; bords ci-dessous |
| zéro jeton de pensée, `MAX_TOKENS`, `SAFETY`, `RECITATION`, texte vide : défaut, jamais une réponse | `defaut_reponse_google` : blocage de l'invite, refus, `MAX_TOKENS`, texte blanc → `VIDE`, autre fin → `FIN_…`, pensées nulles, absentes ou booléennes → `SANS_PENSEES` | `test_un_essai_par_motif_de_fin` (seize cas) | mutation M3 prise |

Dans le collisionneur, une réponse n'est écrite en cellule que si son statut est « OK » : fin `STOP`, texte non vide, au moins un jeton de pensée lu (`juger`, lignes 1883 à 1888). `MAX_TOKENS` donne « TRONQUE » ou « VIDE », jamais une cellule. Les refus ne sont jamais relancés.

Plus grande limite de mots admise, calculée par sonde, au plafond du catalogue ramené à la limite du mode :

| espèce | mode | plafond | texte | rapport | mots admis au plus |
|---|---|---|---|---|---|
| Argon | flux | 65 536 | 49 152 | 5,1 | 9 637 |
| Argon | non diffusé | 32 768 | 16 384 | 5,1 | 3 212 (tours de 3 500 mots refusés en lot) |
| Carbon | flux | 65 536 | 16 384 | 4,2 | 3 900 (le tour de 4 000 mots, E2-T1, refusé) |
| Carbon | non diffusé | 32 768 | négatif | — | refusé sans même la limite de mots |
| Neon | flux et non diffusé | 65 536 | 32 768 | 5,1 | 6 424 |

Ce sont les conséquences annoncées par le développeur.

## 6. Trois envois et le plafond de dépense

Il n'existe pas de plafond par cellule. Le plafond vaut pour le dossier de run, et la ligne (ou la ligne de reprise) pour sa dépense depuis son ouverture. Avant chaque envoi, le premier, l'identique et le dernier recours, le script refuse si la dépense déjà comptée plus le pire cas de cet envoi dépasse le plafond ou la ligne (lignes 2008 à 2016). La dépense comptée d'un envoi est son coût réel. Ce coût ne peut dépasser son pire cas que si l'entrée excède la garde d'entrée ou si la sortie excède le plafond plus la provision. Dans ces deux cas, l'arrêt est immédiat (code 6), comme dans les versions d'avant.

Sondes, sur les trois espèces, à sortie facturée au bord exact du pire cas (pensées = plafond + provision, aucun texte, `MAX_TOKENS`) :

| plafond du dossier (plus 10⁻⁶ USD) | envois partis | arrêt | dépense comptée ≤ plafond |
|---|---|---|---|
| 1 × pire | 1 | plafond (code 4) | oui (par exemple Carbon : 2,2958 pour 2,3004) |
| 2 × pire | 2 | plafond (code 4) | oui (Carbon : 4,5916 pour 4,6007) |
| 3 × pire | 3 | défaut de réglage (code 9) | oui (Carbon : 6,8874 pour 6,9011) |
| ligne de reprise à 2 × pire, plafond large | 2 | ligne (code 4), dernier recours non déclaré | oui |

**La garde tient. Le devis, non (C-1).** `pire_tours_2_3` ajoute une seule relance par cellule au total « avec relances », et `devis` dit « jusqu'au double ». Sonde sur les copies fabriquées des quatre dossiers, au plafond de Fable de la table (ce n'est pas un devis) :

| dossier | pire sans relance | « avec relances » de la v8c | avec deux relances chez Google | cellules de Google à envoyer |
|---|---|---|---|---|
| percée | 16,52 | 34,99 | 42,56 | 3 |
| dérive v2 | 16,38 | 34,72 | 42,26 | 3 |
| mathématiques | 31,85 | 67,60 | 78,83 | 4 |
| antériorité | 2,55 | 5,11 | 7,66 | 1 |

## 7. Mutations neuves de la garde v3

Quatre mutations, aucune dans les séries du développeur (2 à 62) ni de Fable (24). Chacune est faite sur une copie de la garde dans un dossier neuf. Les deux suites tournent entières sur la copie (`-o pythonpath`), avec arrêt au premier échec. Le témoin sur copie donne 403 passés et 1 sauté. L'empreinte de la garde scellée est vérifiée avant et après.

| mutation | règle visée | premier essai en échec (deux suites) | dans la seule suite de la garde | prise |
|---|---|---|---|---|
| M1 : limite de mots comparée au plafond entier, provision oubliée (`>= plafond` au lieu de `>= texte`) | limite de mots | `test_v8_garde_reglages_sain_pour_le_catalogue[carbon]` | `test_limite_de_mots_bord`, `test_v2_rapport_mesure_par_espece` | oui |
| M2 : plancher de 16 000 contrôlé en flux seulement (`if texte < texte_min and mode == "flux"`) | plafond et texte | aucun : 403 passés | aucun : 44 passés | **non → C-2** |
| M3 : texte blanc lu comme une réponse (`.strip()` retiré) | texte vide | `test_v8_defaut_de_reponse_un_essai_par_motif_de_fin[STOP-…]` | `test_un_essai_par_motif_de_fin[STOP-   \n-100-None-VIDE]` | oui |
| M4 : niveau plus bas que le plus haut admis accepté (comparaison au niveau attendu retirée) | réflexion explicite | `test_v8_garde_reglages_un_essai_par_reglage_manquant[niveau…]` | `…[niveau plus bas que le plus haut…]`, `test_niveau_attendu_explicite` | oui |

L'essai témoin de C-2 tue M2 (section 8).

## 8. Corrections en texte exact

À porter dans une version neuve sous nom neuf (R12), par exemple `collisionneur_v9_v8d.py` et `test_collisionneur_v9_v8d.py`. La garde v3 ne change pas. Éprouvé sur copie (bloc-notes, `correction/`) : **361 passés, 1 sauté** (les 359 de la v8c et mes deux essais), aucun essai existant changé. L'essai de C-1 échoue sur la v8c non corrigée, et celui de C-2 sur la garde mutée M2.

### C-1 : le pire « avec relances » compte deux relances chez Google à plafonds égaux

Dans `pire_tours_2_3`, remplacer

```python
            relance = cout_pire_garde(m, garde, m["max_relance"])
            totaux["tour2" if tour == "E3-T2" else "tour3"] += pire
            totaux["avec_relances"] += pire + relance
            cellules.append({"cellule": cid, "id": m["id"], "valide": False, "caracteres": int(caracteres),
                             "garde": garde, "max": m["max"], "provision": m["provision"], "pire": pire,
                             "pire_relance": relance, "motifs": motifs_trouves(prompt) if tour == "E3-T2" else None})
```

par

```python
            relance = cout_pire_garde(m, garde, m["max_relance"])
            # (C-1, vérification d'Opus de la v9-v8c) : chez Google à plafonds égaux, deux relances payées au plus
            # (relance identique, puis dernier recours) ; une ailleurs
            relances = 2 if m["fournisseur"] == "gemini" and reglage_de_relance(m)[1] else 1
            totaux["tour2" if tour == "E3-T2" else "tour3"] += pire
            totaux["avec_relances"] += pire + relances * relance
            cellules.append({"cellule": cid, "id": m["id"], "valide": False, "caracteres": int(caracteres),
                             "garde": garde, "max": m["max"], "provision": m["provision"], "pire": pire,
                             "pire_relance": relance, "relances": relances,
                             "motifs": motifs_trouves(prompt) if tour == "E3-T2" else None})
```

Dans `devis_reprise`, remplacer

```python
                  f"{detail['avec_relances']:.4f} USD si chaque cellule était relancée (refusé avant l'envoi par le "
                  f"plafond et la ligne).")
```

par

```python
                  f"{detail['avec_relances']:.4f} USD si chaque cellule épuisait ses relances (deux chez une espèce de "
                  f"Google à plafonds égaux : relance identique, puis dernier recours ; une ailleurs ; refusé avant "
                  f"l'envoi par le plafond et la ligne).")
```

Dans `devis`, remplacer

```python
    print("La dépense réelle dépend de la longueur de la réflexion ; une relance (sortie vide ou coupée) peut ajouter "
          "jusqu'au double du pire cas de sa cellule. Le plafond vaut pour tout le dossier de run, et le script le "
          "vérifie avant chaque appel.")
```

par

```python
    print("La dépense réelle dépend de la longueur de la réflexion ; chaque relance (sortie vide ou coupée) ajoute au "
          "plus le pire cas de sa cellule au plafond de relance ; une cellule de Google à plafonds égaux en a deux "
          "(relance identique, puis dernier recours), les autres une. Le plafond vaut pour tout le dossier de run, et "
          "le script le vérifie avant chaque appel.")
```

Essai, en fin du fichier d'essais :

```python
def test_opus_c1_devis_avec_relances_compte_deux_relances_chez_google(c, tmp_path):
    """C-1 : le pire « avec relances » du devis de reprise compte deux relances payées pour une cellule de Google à
    plafonds égaux (relance identique, puis dernier recours), une pour les autres espèces."""
    dossier_run = DOSSIERS_A_REPRENDRE["percee"][0]
    d = fabriquer_copie(c, dossier_run, tmp_path / dossier_run)
    r = c.pire_tours_2_3(d)
    especes = {c.MODELES[l]["id"]: c.MODELES[l] for l in c.LETTRES}
    non_valides = [x for x in r["cellules"] if not x["valide"]]
    assert any(especes[x["id"]]["fournisseur"] == "gemini" for x in non_valides)  # le cas existe dans ce dossier
    attendu = 0.0
    for x in non_valides:
        k = 2 if especes[x["id"]]["fournisseur"] == "gemini" else 1
        assert x["relances"] == k
        attendu += x["pire"] + k * x["pire_relance"]
    assert r["avec_relances"] == pytest.approx(attendu)
```

### C-2 : essai témoin du plancher de texte en appel non diffusé

Même fichier d'essais :

```python
def test_opus_m2_plancher_de_texte_en_appel_non_diffuse(c):
    """Essai témoin (mutation M2) : le plancher de 16 000 jetons de texte vaut aussi en appel non diffusé (lot) ; le
    bord est admis, un jeton de moins refusé."""
    assert c.verifier_reglages_google("argon", corps_google("high", 32768), 32768 - 16000, mode="non_diffuse") == []
    p = c.verifier_reglages_google("argon", corps_google("high", 32768), 32768 - 15999, mode="non_diffuse")
    assert any("jetons de texte < 16000" in x for x in p)
```

Les textes de la v8c (en-tête, `VERSION`, chemin des essais) sont à accorder à la version neuve, comme à chaque version.

## 9. Remarques (non bloquantes)

1. **Commentaires restés anciens**, à accorder dans la même version :
   - ligne 408, « × 1,6 », alors que le rapport est maintenant par espèce ;
   - ligne 1090, « garde_google_v1.py » au lieu de la v3 ;
   - lignes 1803 et 1804, « relancés une seule fois » ;
   - ligne 1809, « l'unique relance » ;
   - ligne 1908, « Au plus deux essais » : il y en a trois chez Google à plafonds égaux ;
   - ligne 2035 : l'écran dit « relance corrigée » pour une relance identique.
2. **Déclaration en double, jamais en silence.** Deux cas :
   - si Google refuse le niveau par un 400 à l'étape identique ou au dernier recours, l'étape repart au budget et sa déclaration est réécrite ;
   - si la commande meurt entre la déclaration et l'envoi, la commande suivante déclare de nouveau.

   « La commande suivante ne déclare qu'une fois » vaut pour un refus du plafond ou de la ligne, pas pour ces deux cas.
3. **La reprise lit l'étape sans lire le plafond de l'essai précédent.** Cela n'a d'effet que si la table change entre deux commandes. Par exemple : un dernier essai « identique », puis un plafond de relance relevé. Le plan à deux étapes, coupé de deux, est alors vide : la cellule rend son ancien statut sans envoi ni message. Avec les tables actuelles, c'est sans objet.
4. **`mots=None` coupe le contrôle de la limite de mots dans la garde.** Le collisionneur le passe au seul lieu d'envoi, et sur les trois réglages d'avant le comptage. La garde de défense des appelants ne le passe pas. Pour un autre script, mieux vaudrait, dans une garde future, une limite exigée (ou « aucune limite » déclarée explicitement).
5. **Neon à 5,1 jetons par mot** : choix du développeur, déclaré (sa réserve 1). Sans mesure pour Neon, il ne bloque aucun tour (6 424 mots au plus). Il est à remplacer par la mesure de l'essai réel.
6. **Carbon refuse le tour de 4 000 mots de l'étage II** (E2-T1) avant tout envoi. Tout run neuf avec Carbon à l'étage II s'arrêtera là. C'est connu (Fable 4.2, développeur) ; la provision de Carbon pour ce tour reste à revoir.
7. **Fichiers non versés**, sur disque seulement, cachés par `.git/info/exclude` :
   - la v8b (`6cd0209c…`), ses essais (`e2756140…`) et son rapport (`87f845f2…`) ;
   - la garde v2 (`9d39a749…`) et ses essais (`6adad260…`).

   L'en-tête de la v8c, celui de la garde v3 et R-4686 les citent par empreinte : ils sont à verser (R6, « récupérer ce qui est récupérable »).
8. **Le comptage `countTokens`** est une requête à Google sans génération : aucun réglage de réflexion ne s'y applique. Il part après la garde des trois réglages prévus.
9. **Limite déjà dite par Fable et par le développeur.** Sous un niveau de réflexion, rien ne borne la pensée en jetons hors du plafond. « Réflexion plus 16 000 » se vérifie sur la provision comptée, pas sur ce que le modèle pensera. Après la réponse, `MAX_TOKENS` reste un défaut.

## 10. Avant tout appel

1. C-1 et C-2 portées en version neuve, puis vérifiées par moi ou par Fable à son retour.
2. Résultat de l'essai réel d'un envoi par modèle de Google (R-4686) : il doit confirmer Argon à 65 536 en flux et les pensées non nulles aux niveaux envoyés, et donner la mesure de Neon.
3. Pour chaque dossier : `verifier` par la version neuve, avant et après. La note de reprise dit le changement de réglage entre les tours et les cellules d'Argon écrites sans pensées (Fable, section 5).

## Limites

- Aucun appel réel : la conduite des modèles aux niveaux envoyés n'est pas connue ici.
- Les copies de dossiers sont fabriquées depuis les journaux, à contenus factices. Les chiffres de la section 6 illustrent l'écart du devis au plafond de Fable de la table ; ce ne sont pas des devis.
- Le relevé des jetons par mot (43 réponses) n'est pas recalculé : il est pris de la note de Fable (`9cf6799f…`, section 4.2), que la garde cite.
- Mes outils sont dans mon bloc-notes, non durable :
  - `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8c-opus/outils/mutations_garde_v3_opus.py` (`0849fba1…`) ;
  - `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8c-opus/sondes/test_sondes_opus_v8c.py` (`0bab4bd4…`) ;
  - `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8c-opus/sondes/test_sonde_devis_relances_opus.py` (`e777ac01…`) ;
  - la copie corrigée `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8c-opus/correction/docs/notes/collisionneur-v9/collisionneur_v9_v8c.py` (`fbdba2ca…`) ;
  - ses essais `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/verif-v8c-opus/correction/docs/notes/collisionneur-v9/test_collisionneur_v9_v8c.py` (`521b06d9…`).

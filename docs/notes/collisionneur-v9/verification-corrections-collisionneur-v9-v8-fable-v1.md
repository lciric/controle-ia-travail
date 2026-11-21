# Vérification des corrections : collisionneur v9 version 8 et garde commune des réglages de Google

Écrite le 21 novembre 2026 vers 19:00Z par le même contre-lecteur que la version 7, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5). Pièces d'instrument (classe B). Mots de Lazar : GO-2026-11-21-63, -69 et -71 ; décisions de la mère : R-4664.

Ce que je n'ai pas fait : aucun envoi réel, aucun comptage, aucune dépense ; aucune clé lue (essais et sondes sous `env -i`, clés factices des doublures) ; aucun commit ; aucun fichier du dépôt modifié hors cette pièce et son sceau. Sur la branche des versements (761c2c5a), seuls des `journal.jsonl` et `especes.json`, par `git show` ; aucune réponse de modèle. Mutations, sondes et corrections sur des copies, dans mon bloc-notes.

## Verdict

**À corriger : une correction obligatoire (K-1), une à trancher par la mère (K-2).** Tout le reste est conforme.

- **K-1, obligatoire : la décision de la mère sur la relance n'est pas portée.** Après `MAX_TOKENS` ou une réponse vide, la version 8 baisse le niveau de réflexion dès la relance, au même plafond, pour les trois espèces. Elle ne relève jamais le plafond : aucune espèce n'en a de plus haut dans la table. Et la baisse n'est pas déclarée par une ligne propre du journal. Texte exact en section 6, éprouvé sur copie.
- **K-2, à trancher : la limite de mots est contrôlée avec un rapport que les journaux démentent.** La garde compte 1,6 jeton par mot. Les 43 réponses réelles complètes d'Argon et de Carbon dépassent toutes ce rapport : de 1,78 à 5,06 jetons de texte par mot de la limite. Le contrôle ne refuse donc jamais rien. Au rapport relevé, le plafond d'Argon (32 768) est trop bas.
- **Conforme** : C-1, C-2, C-3 (selon la décision de la mère) et mes remarques 1 à 4 ; le niveau de réflexion par espèce ; la règle des 16 000 jetons de texte pour les trois espèces de Google ; zéro pensée ou pensées absentes = défaut ; `SAFETY` et `RECITATION` définitifs ; Carbon à 65 536 en flux ; la ligne de reprise ; la reprise des dossiers, question fusionnée comprise.

Tant que K-1 n'est pas faite, la version 8 ne perd rien et ne paie rien deux fois sans le dire ; elle s'écarte de la décision en baissant la réflexion d'Argon, de Carbon ou de Neon à la première sortie coupée.

## 1. Pièces, empreintes, essais

Empreintes recalculées, toutes égales aux compagnons `.sha256` :

| fichier | empreinte |
|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8.py` | `b85690310f5c…` |
| `docs/notes/collisionneur-v9/test_collisionneur_v9_v8.py` | `4b0f4ab5a524…` |
| `docs/notes/collisionneur-v9/rapport-developpeur-collisionneur-v9-v8-v1.md` | `ef1a9e5eb653…` |
| `src/controle_ia/garde_google_v1.py` | `04d233bd66c3…` |
| `tests/test_garde_google_v1.py` | `ad022e3a9632…` |
| page versée « Gemini thinking », variante `generateContent` | `fe0b8d8820b2…` |
| référence versée de `generateContent` | `829dabb8cb4b…` |
| audit et contre-audit des réglages de Google | sceaux tenus |

Essais rejoués une fois, hors réseau, sans clés, `--basetemp` à moi : **version 8 : 346 passés, 1 sauté ; garde : 42 passés.** Ce sont les comptes du développeur. Les copies des quatre dossiers ont tourné.

Mes 24 mutations, chacune sur une copie, les deux suites entières (témoin : 388 passés, 1 sauté) ; une seule recoupe celles du développeur (pensées absentes lues comme zéro, sa mutation 14) :

| pièce | mutation | prise |
|---|---|---|
| v8 | refus de crédit non nommé au journal | oui (2) |
| v8 | usage annoncé du refus de crédit jeté | oui (1) |
| v8 | ligne de reprise comptée depuis zéro | oui (1) |
| v8 | relance du repli au même budget | oui (1) |
| v8 | cellule sans pensées renvoyée au même réglage | oui (1) |
| v8 | budget admis avec un niveau à la composition | oui (2) |
| v8 | pensées absentes lues comme zéro | oui (1) |
| v8 | relance corrigée non journalisée | oui (13) |
| v8 | relevé illisible du délai jeté | oui (1) |
| garde | limite de mots : bord admis | oui (2) |
| garde | pensées absentes admises | oui (4) |
| garde | blocage de l'invite ignoré | oui (2) |
| garde | budget au-delà de la provision admis | oui (2) |
| garde | autre fin que `STOP` admise | oui (3) |
| garde | `MAX_TOKENS` avec texte admis | oui (4) |
| garde | refus du niveau reconnu sans le code 400 | oui (1) |
| garde | plafond égal à la limite refusé | oui (127) |
| garde | niveau non admis pour l'espèce | oui (3) |
| v8 | **lot fini lu sur `done` seul, état ignoré** | **non — essai témoin proposé (remarque 1)** |
| garde | **bord exact des 16 000 jetons de texte** | **non — essai témoin proposé (remarque 1)** |
| v8 | **première ligne de reprise lue au lieu de la dernière** | **non — essai témoin proposé (remarque 1)** |
| v8 | plafond de relance du lot non ramené à la limite | non — sans effet avec les tables actuelles |
| v8 | garde par essai sans la limite de mots | non — redondant avec la garde d'avant le comptage |
| v8 | repli déclaré non repris par la commande suivante | non — sans gravité : le niveau repart, refusé sans coût, repli déclaré de nouveau |

## 2. Mes remarques de la version 7

| remarque | dans la version 8 | verdict |
|---|---|---|
| **C-1** : un relevé refusé abandonnait un lot payé | `relever_lot` rend « manqué » un relevé coupé ou refusé ; le lot est suivi jusqu'au délai, un dernier relevé précède l'annulation ; mes deux essais y sont, accordés à Argon | conforme |
| **C-2** : une réponse illisible était jetée | relevé brut d'un lot échoué, de forme inconnue ou en erreur gardé, masqué, dans la réponse scellée de l'essai, jamais dans une cellule ; mon essai à trois cas y est ; étendu par la mère au corps de création, au relevé du délai, à la ligne de flux, à Kimi et à OpenAI | conforme |
| **C-3** : coût d'un refus de crédit | décision de la mère, qui remplace mon texte : nommé (`refus_de_credit`), usage annoncé gardé, compté au pire, code 5 (sonde : 2,47 USD, usage 58 000 et 1) | conforme à la décision |
| 1 : essai témoin du repli sur la provision | présent, accordé au réglage neuf | conforme |
| 2 : texte d'aide de `--rejuger-essai` | corrigé, essai à l'appui | conforme |
| 3 : empreinte du rejugement | essai ajouté | conforme |
| 4 : lot orphelin, dernier relevé | nom propre `collisionneur-<cellule>-essai<N>` ; dernier relevé avant l'annulation ; échec d'annulation dit | conforme |
| plafond d'un appel non diffusé | lot ramené à 32 768 : Carbon refusé en lot avant tout envoi, rien de compté | conforme |

Restent ouverts, dits par le développeur : relecture d'un lot nommé au journal avant d'en créer un autre ; délai d'un lot ; création non idempotente.

## 3. Réflexion par espèce

Page versée (`fe0b8d88…`), relue par moi : ligne 591 et suivante, `thinkingLevel` « required for Gemini 4 », Carbon et Argon `low`, `medium` (défaut), `high` ; Neon `low`, `medium`, `high` (défaut), `xhigh`. Ligne 939 : `thinkingBudget` déprécié, ramené seul au niveau le plus proche, erreur 400 avec un niveau. Ligne 750 : corps `generationConfig.thinkingConfig.thinkingLevel`.

| espèce | niveau envoyé | budget | plafond en flux | provision comptée | texte restant |
|---|---|---|---|---|---|
| Argon | `high` | aucun | 32 768 | 16 384 | 16 384 |
| Carbon | `high` | aucun | 65 536 | 49 152 | 16 384 |
| Neon | `xhigh` | aucun | 65 536 | 32 768 | 32 768 |

- Le niveau est le plus haut admis, exigé à la composition, contrôlé par la garde avant le comptage et sur le corps de chaque essai, journalisé. Sondes : chaque envoi à Google des cinq dossiers porte le niveau, jamais un budget.
- Le repli au budget n'a lieu qu'après un refus 400 qui nomme le niveau ; il est déclaré au journal et à l'écran, une seule fois.
- Limite, déjà dite par le développeur (son point 6.6) : sous un niveau, rien ne borne plus la réflexion en jetons. La provision n'est qu'un pire cas compté ; « 16 000 jetons de texte au-delà de la réflexion » se vérifie sur elle, pas sur ce que le modèle pensera. La protection réelle est après la réponse : `MAX_TOKENS` est un défaut.

## 4. La garde

| point | constat | verdict |
|---|---|---|
| 16 000 jetons de texte au-delà de la réflexion, les trois espèces | garde commune et `REGLE_TEXTE_MIN` étendue à Argon ; refus avant tout envoi et tout comptage | conforme ; bord exact non éprouvé (remarque 1) |
| plafond au plus la limite versée | par espèce et par mode ; Carbon à 65 536 en flux, selon la décision | conforme |
| limite de mots | contrôlée, bord éprouvé, mais au rapport de 1,6 | **K-2** |
| zéro pensée = défaut | `SANS_PENSEES`, code 10, coût réel, aucune cellule, jamais renvoyée au même réglage ; pensées absentes jamais lues comme zéro | conforme |
| fin en `MAX_TOKENS`, `SAFETY`, `RECITATION`, texte vide | jamais une cellule ; `SAFETY` et `RECITATION` sans relance | conforme |
| relance après `MAX_TOKENS` ou réponse vide | niveau baissé d'emblée, plafond inchangé | **K-1** |
| garde commune réellement appelée | module importé, empreinte au journal de chaque essai de Google | conforme |

Sonde sur les réponses réelles complètes des journaux : la garde de la réponse classe les 22 d'Argon « sans pensées » et laisse passer les 21 de Carbon.

### 4.1 K-1 : la relance

Décision de la mère (R-4664) : la relance garde le niveau et relève le plafond ; le niveau ne baisse qu'en dernier recours, déclaré.

Ce que fait la version 8 (sonde, `MAX_TOKENS` avec texte puis réponse saine) :

| espèce | premier envoi | relance | ligne propre au journal |
|---|---|---|---|
| Argon | 32 768, `high` | 32 768, **`medium`** | aucune |
| Carbon | 65 536, `high` | 65 536, **`medium`** | aucune |
| Neon | 65 536, `xhigh` | 65 536, **`high`** | aucune |

- Carbon et Neon sont déjà à la limite d'un appel (65 536) : aucun plafond plus haut n'existe. La baisse du niveau y est le dernier recours au sens de la décision ; il manque sa déclaration (aujourd'hui : un champ de l'essai et une mention à l'écran).
- Argon a un plafond plus haut : 65 536 en flux (page versée, ligne 931 : « streaming or SDK calls for gemini-4-carbon and gemini-4-argon »). La garde le borne à 32 768 d'après la liste. Pour lui, la décision n'est pas portée.

La correction K-1 pose la règle une fois : si le plafond de relance est au-dessus du premier, la relance garde le niveau et relève le plafond ; sinon, dernier recours déclaré. Elle ne change aucune table : avec les tables actuelles, les trois espèces passent par le dernier recours, désormais déclaré. La table d'Argon est l'objet de K-2.

### 4.2 K-2 : la limite de mots et le plafond d'Argon

Jetons de texte par mot de la limite du tour, sur les réponses réelles complètes (journaux versés) :

| espèce | réponses | minimum | médiane | maximum | au-delà de 1,6 |
|---|---|---|---|---|---|
| Argon | 22 | 1,78 | 3,47 | 5,06 (17 714 jetons pour 3 500 mots) | 22 |
| Carbon | 21 | 2,40 | 3,41 | 4,11 (14 401 jetons pour 3 500 mots) | 21 |

- Le rapport de 1,6 est « non mesuré » dans le module ; mesuré, il est faux d'un facteur deux à trois. Avec lui, la limite de mots ne peut jamais refuser : 4 000 mots font 6 400 jetons, sous les 16 000 exigés par ailleurs.
- Au rapport relevé, la garde refuserait Argon à 32 768 (3 500 × 5,06 = 17 710, pour 16 384 de texte) : à raison, une réponse réelle d'Argon a déjà 17 714 jetons de texte sans aucune pensée. Avec des pensées au niveau `high`, 32 768 sera souvent atteint.
- Elle admettrait Carbon sur les tours de l'étage III (3 500 × 4,11 = 14 385) et le refuserait sur le tour à 4 000 mots de l'étage II (16 440 pour 16 384).

À trancher par la mère, lignes éprouvées sur copie :
1. Limite d'Argon en flux à 65 536 dans la garde (`LIMITES_SORTIE`), source : page versée, ligne 931. Jamais servi : à confirmer par l'essai réel prévu.
2. Plafond d'Argon : 32 768 puis 65 536 (lettre de la décision, premier envoi souvent payé pour rien, comme Opus à 22 000) ou 65 536 dès le premier envoi (ma recommandation ; la relance est alors le dernier recours pour les trois espèces).
3. Rapport par espèce, au moins le maximum relevé : Argon 5,1 ; Carbon 4,2 ; Neon, sans donnée, 5,1. Pour le tour à 4 000 mots de l'étage II, la provision de Carbon serait à revoir.

Ces trois lignes ensemble font échouer 16 essais qui lisent les tables, tous à accorder : 9 du collisionneur (`test_b4_…` deux, `test_v5_neon_au_catalogue_…`, `test_v7_budget_envoye_…[argon]`, `test_v7_argon_reglages_prix_et_sources`, `test_v7_argon_pire_cas_et_cout_reel`, `test_v8_garde_reglages_sain_pour_le_catalogue[carbon]`, `test_v8_garde_reglages_limite_de_mots`, `test_v8_garde_reglages_mots_des_tours_compatibles`) et 7 de la garde (`test_sain_par_espece_et_par_mode` quatre cas, `test_limites_versees_par_mode`, `test_limites_egales_a_la_liste_versee`, `test_limite_de_mots_bord`).

## 5. Reprise et ligne de reprise

- Copies des quatre dossiers sous les commandes du développeur : dans la suite, rejouées. Ma sonde sur la question fusionnée (`collisionneur-question-de-recherche-fusionnee-v1-20261121-153256`, que le développeur n'a pas trouvée) : `verifier` tient avant et après, rejugement de `E3-T2-critique-croisee-D:1`, 4 envois, 12 cellules, Argon et Carbon au niveau `high`, relance sans envoi. Ses cellules d'Argon écrites sans pensées : `E3-T1-conception-C` et `E3-T2-critique-croisee-C`.
- Ligne de reprise (`--ligne-reprise-usd`, `--go-ligne`) : ouverte depuis la dépense du moment, idempotente par son GO, refusée à un autre montant. Lecture du développeur : 30 et 17 USD sont le reste accordé à la reprise. La dépense totale permise devient 36,23 USD (mathématiques) et 26,84 USD (dérive v2), sous les plafonds 36,3 et 26,9. C'est la seule lecture cohérente pour la dérive v2 ; à confirmer d'un mot par la mère.
- Le script contrôle la forme du GO, pas son existence au registre.
- Dans un même dossier, le réglage d'Argon et de Carbon change entre les tours : la note de reprise doit le dire.

## 6. Correction en texte exact

Version neuve, nom neuf (R12). Éprouvé sur copie : **391 passés, 1 sauté** (les 388 d'avant et mes trois essais) ; aucun essai existant ne change.

### K-1 : la relance garde le niveau et relève le plafond ; dernier recours déclaré

Dans `collisionneur_v9_v8.py`, avant `def reglage_en_defaut(dossier, cid, m):`, ajouter :

```python
def reglage_de_relance(m):
    """(K-1 ; décision de la mère, R-4664) Réglage de l'unique relance d'une espèce de Google après MAX_TOKENS ou réponse
    vide. Si le plafond de relance est au-dessus du premier plafond : la relance garde le niveau et relève le plafond.
    Sinon, aucun plafond plus haut n'existe : dernier recours, DÉCLARÉ, un niveau plus bas au même plafond.
    Renvoie (niveau de la relance, dernier_recours)."""
    if m["max_relance"] > m["max"]:
        return m.get("niveau_reflexion"), False
    return NIVEAU_CORRIGE.get(m.get("niveau_reflexion")), True


```

Dans `executer_cellule`, remplacer

```python
        for plafond_sortie, niveau in ((m["max"], m["niveau_reflexion"]),
                                       (m["max_relance"], NIVEAU_CORRIGE.get(m["niveau_reflexion"]))):
```

par

```python
        for plafond_sortie, niveau in ((m["max"], m["niveau_reflexion"]),
                                       (m["max_relance"], reglage_de_relance(m)[0])):  # (K-1)
```

et

```python
        if google and repli is None and genre == "relance":  # v9-v8 : l'unique relance part au réglage corrigé
            vers = NIVEAU_CORRIGE.get(niveau_cat)
            correction = {"de": niveau_cat, "vers": vers, "motif": statut}
            envoi_m = dict(m, niveau_reflexion=vers)
        elif google and repli is not None:  # v9-v8 (ajout 2) : repli déclaré au budget prévu ; relance à sa moitié
            budget = repli["vers"]["thinkingBudget"]
            if genre == "relance":
                correction = {"de": f"budget {budget}", "vers": f"budget {budget // 2}", "motif": statut}
                budget //= 2
            envoi_m = dict(m, niveau_reflexion=None, repli_budget=budget)
```

par

```python
        dernier_recours = google and genre == "relance" and reglage_de_relance(m)[1]  # (K-1)
        if google and repli is None and genre == "relance":  # (K-1) la relance garde le niveau et relève le plafond ;
            vers = reglage_de_relance(m)[0]                  # le niveau ne baisse qu'en dernier recours, déclaré
            correction = {"de": niveau_cat, "vers": vers, "motif": statut}
            if not dernier_recours:
                correction["plafond"] = [m["max"], max_tokens]
            envoi_m = dict(m, niveau_reflexion=vers)
        elif google and repli is not None:  # v9-v8 (ajout 2) : repli déclaré au budget prévu
            budget = repli["vers"]["thinkingBudget"]
            if genre == "relance" and dernier_recours:  # (K-1) moitié du budget en dernier recours seulement
                correction = {"de": f"budget {budget}", "vers": f"budget {budget // 2}", "motif": statut}
                budget //= 2
            elif genre == "relance":
                correction = {"de": f"budget {budget}", "vers": f"budget {budget}", "motif": statut,
                              "plafond": [m["max"], max_tokens]}
            envoi_m = dict(m, niveau_reflexion=None, repli_budget=budget)
        if dernier_recours:  # (K-1) déclaré au journal et à l'écran avant l'envoi, jamais silencieux
            ajouter_journal(dossier, {"dernier_recours_reflexion_declare": cid, "correction": correction,
                                      "plafond": max_tokens, "quand": maintenant(), "script": VERSION})
            print(f"    DERNIER RECOURS DÉCLARÉ : aucun plafond au-dessus de {max_tokens} pour {m['id']} ; la relance "
                  f"baisse la réflexion ({correction['de']} → {correction['vers']}) (journalisé)", flush=True)
```

Textes à accorder : docstring de `executer_cellule`, commentaire de `NIVEAU_CORRIGE` et en-tête (« la relance garde le niveau et relève le plafond ; niveau plus bas en dernier recours, déclaré »).

### K-1, essais

```python
def _argon_a_deux_plafonds(c, monkeypatch):
    """Argon à 32 768 puis 65 536 en flux (page versée fe0b8d88…, ligne 931), sur copie des tables."""
    monkeypatch.setitem(c.CATALOGUE, "argon", dict(c.CATALOGUE["argon"], max=32768, max_relance=65536))
    monkeypatch.setitem(c.garde_google.LIMITES_SORTIE, "argon", {"flux": 65536, "non_diffuse": 32768})


def test_k1_relance_garde_le_niveau_et_releve_le_plafond(c, tmp_path, monkeypatch, capsys):
    _argon_a_deux_plafonds(c, monkeypatch)
    c.TRANSPORT = FauxTransport(flux_gemini(texte="Début", modele="gemini-4-argon", fin="MAX_TOKENS", candidats=8000,
                                            pensees=24000), flux_gemini(modele="gemini-4-argon"))
    assert executer(c, tmp_path, "argon") == "OK"
    reglages = [(a["corps"]["generationConfig"]["maxOutputTokens"],
                 a["corps"]["generationConfig"]["thinkingConfig"]["thinkingLevel"]) for a in c.TRANSPORT.appels]
    assert reglages == [(32768, "high"), (65536, "high")]
    d = journal(c, tmp_path)
    assert d[1]["correction_reflexion"] == {"de": "high", "vers": "high", "motif": "TRONQUE", "plafond": [32768, 65536]}
    assert d[1]["niveau_reflexion"] == "high" and d[1]["max_tokens"] == 65536
    assert not [x for x in c.lire_journal(tmp_path) if "dernier_recours_reflexion_declare" in x]
    assert "DERNIER RECOURS" not in capsys.readouterr().out


def test_k1_dernier_recours_declare_quand_aucun_plafond_plus_haut(c, tmp_path, capsys):
    c.TRANSPORT = FauxTransport(flux_gemini(texte="Début", fin="MAX_TOKENS", candidats=16000, pensees=49000), flux_gemini())
    assert executer(c, tmp_path, "carbon") == "OK"
    assert [a["corps"]["generationConfig"]["thinkingConfig"]["thinkingLevel"] for a in c.TRANSPORT.appels] == [
        "high", "medium"]
    lignes = c.lire_journal(tmp_path)
    declare = [i for i, x in enumerate(lignes) if "dernier_recours_reflexion_declare" in x]
    relance = [i for i, x in enumerate(lignes) if x.get("essai") == 2]
    assert len(declare) == 1 and declare[0] < relance[0]  # déclaré avant l'envoi
    assert lignes[declare[0]]["correction"] == {"de": "high", "vers": "medium", "motif": "TRONQUE"}
    assert "DERNIER RECOURS DÉCLARÉ" in capsys.readouterr().out


def test_k1_reprise_apres_un_premier_defaut_releve_le_plafond(c, tmp_path, monkeypatch):
    _argon_a_deux_plafonds(c, monkeypatch)
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele="gemini-4-argon", fin="MAX_TOKENS", candidats=0, pensees=32768))
    c.fixer_composition(["argon", "kimi"])
    l = lettre_de(c, "argon")
    pire = c.cout_pire_garde(c.MODELES[l], c.garde_entree(int(len(SAIN) / 2.5)), 32768)
    with pytest.raises(c.Arret) as e:
        c.executer_cellule(tmp_path, "E1-T1", l, SAIN, [], pire + 0.001, c.APPELANTS)
    assert e.value.code == c.CODE_PLAFOND and [x["statut"] for x in journal(c, tmp_path)] == ["MAX_TOKENS_SANS_TEXTE"]
    assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T1", l), c.MODELES[l]) is False  # un plafond plus haut existe
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon"))
    assert c.executer_cellule(tmp_path, "E1-T1", l, SAIN, [], 100.0, c.APPELANTS) == "OK"
    g = c.TRANSPORT.appels[0]["corps"]["generationConfig"]
    assert (g["maxOutputTokens"], g["thinkingConfig"]["thinkingLevel"]) == (65536, "high")
```

### K-2, lignes des tables (si la mère les retient)

Dans `garde_google_v1.py` (version neuve, nom neuf) :

```python
LIMITES_SORTIE = {"argon": {"flux": 65536, "non_diffuse": 32768},
```

```python
JETONS_PAR_MOT_MESURES = {"argon": 5.1, "carbon": 4.2, "neon": 5.1}
```

avec `jetons_par_mot=None` dans la signature de `verifier_reglages_google` et, en tête de son corps, `jetons_par_mot = JETONS_PAR_MOT_MESURES[espece] if jetons_par_mot is None else jetons_par_mot`. Dans la table du collisionneur, pour Argon : `"max": 65536, "max_relance": 65536`. Source du rapport à écrire dans l'en-tête du module : journaux versés de la branche `runs/collisionneurs-reprise-minuit-v1`, 43 réponses.

## 7. Remarques (non bloquantes)

1. **Trois essais témoins** pour mes mutations non prises (éprouvés : passent sur le dépôt, échouent chacun sur sa copie mutée).
   Garde :
   ```python
   def test_cl_v8_bord_exact_des_16000_jetons_de_texte():
       assert g.verifier_reglages_google("neon", corps("xhigh", 32768 + 16000), 32768) == []
       assert any("jetons de texte" in p for p in g.verifier_reglages_google("neon", corps("xhigh", 32768 + 15999), 32768))
   ```
   Collisionneur :
   ```python
   def test_cl_v8_lot_fini_dit_par_son_etat_seul(c, tmp_path):
       """Un relevé sans champ `done` mais à l'état fini est un lot fini : lu, jamais suivi jusqu'au délai."""
       dossier = coupe_puis(c, tmp_path)
       fini = {"name": "batches/abc123", "metadata": {"state": "JOB_STATE_SUCCEEDED"},
               "response": {"inlinedResponses": [{"response": reponse_gemini_lot(modele="gemini-4-argon")}]}}
       c.TRANSPORT = FauxTransport(lot_cree(), FauxFlux(corps=fini))
       assert executer_lot(c, dossier) == "OK" and len(c.TRANSPORT.appels) == 2


   def test_cl_v8_deux_lignes_de_reprise_la_derniere_borne(c, tmp_path):
       c.ouvrir_ligne_reprise(tmp_path, 5.0, "GO-2026-11-21-69")
       c.ouvrir_ligne_reprise(tmp_path, 9.0, "GO-2026-11-22-01")
       ligne = c.ligne_courante(tmp_path)
       assert (ligne["montant"], ligne["go"], ligne["nature"]) == (9.0, "GO-2026-11-22-01", "de reprise")
       assert c.lire_journal(tmp_path)[-1]["ligne_precedente"]["go"] == "GO-2026-11-21-69"
   ```
2. Une réponse vide en fin `STOP` suit la même relance qu'une sortie coupée. Relever le plafond n'y change rien ; c'est la décision, je ne la discute pas.
3. Un repli déclaré n'est pas repris si la commande s'arrête juste après le refus du niveau : la commande suivante renvoie le niveau, refusé sans coût, et déclare le repli une seconde fois. Sans gravité.
4. Le collisionneur, ses essais, la garde et ses essais sont cachés par `.git/info/exclude` (dit par le développeur) : ils ne seront poussés que si la mère les verse.

## 8. Avant tout appel

1. K-1 faite, K-2 tranchée, puis vérifiées par moi.
2. L'essai réel d'un appel par modèle, prévu par la mère : Argon au niveau `high` (pensées non nulles ? sortie totale ?), au plafond retenu ; Neon au niveau `xhigh`, jamais envoyé.
3. Pour chaque dossier : `verifier` par la version neuve avant et après ; la note de reprise dit le changement de réglage entre les tours et les cellules d'Argon écrites sans pensées.

## Limites

- Aucun appel réel : le comportement d'Argon et de Carbon au niveau `high`, et de Neon au niveau `xhigh`, n'est pas connu ; la taille de leur réflexion non plus.
- Le rapport de jetons par mot est relevé sur 43 réponses de trois tours de l'étage III, sous l'ancien réglage ; il mêle le découpage en jetons et le dépassement de la limite de mots par les modèles.
- La reprise est éprouvée sur des copies fabriquées depuis les journaux réels, pas sur les dossiers eux-mêmes.
- Mes outils sont dans mon bloc-notes, non durable : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v8-fable/outils/mutations_cl_v8.py` (mutations), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v8-fable/outils/corrections_cl_v8.py` (K-1 et les tables de K-2, sur copie), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v8-fable/outils/test_sondes_cl_v8.py` (sondes), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/cl-v8-fable/outils/test_temoins_cl_v8.py` (essais témoins).

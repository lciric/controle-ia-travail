# Vérification : collisionneur v9 version 6 et consultation des modèles externes version 6

Écrite le 21 novembre 2026 vers 16:10Z par le vérificateur, Claude Fable 5.2 (`claude-fable-5-2`), même rôle que le contre-lecteur de la version 5, autre modèle que le développeur (Claude Opus 5.5). Pièce d'instrument (classe B). Mot de Lazar : GO-2026-11-21-63.

Ce que je n'ai pas fait : aucun appel à un modèle, aucun comptage, aucune requête sur le réseau, aucune dépense ; aucune clé lue (essais lancés sous `env -i`, clés factices des doublures seulement) ; aucun commit ; aucun fichier du dépôt modifié hors cette pièce et son sceau ; rien lu sous `runs/`, `archives-reponses-modeles/`, `/root/.claude/`, ni les réponses des modèles du dossier de la consultation. Mes sondes et mes mutations ont tourné sur des copies, dans mon bloc-notes.

## Verdict

**À corriger.** Une correction obligatoire de code (V-1), une de réglages (V-2).

- **Les quatre corrections de la contre-lecture de la version 5 sont portées et justes** (question 1). Sur ce seul périmètre, la version 6 est conforme.
- **La consultation version 6 est conforme**, sans correction ; pour laisser Carbon réfléchir, il faut lui passer des options (section 2.4).
- **Le collisionneur version 6 ne laisse pas Carbon réfléchir jusqu'au bout sans déclencher la garde à tort** (question 2). Le seuil de la garde est le budget envoyé, et ce budget est une limite souple. Une réponse complète, payée, sous le pire cas compté, est jetée au code 6, la course s'arrête, et la même commande la renvoie et la repaie (sonde). Argon et Neon ne sont pas relevés.
- **La garde du nom de la clé d'OpenAI tient** (question 3).
- **Une version 6 reprend un dossier créé par la version 3 (`850df311…`) sans perte ni double paiement** (question 4), avec deux contraintes à connaître (section 4).

## 1. Pièces, empreintes, essais

Empreintes recalculées, toutes égales aux compagnons `.sha256` :

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v6.py` | `3c6a4cfb49ad…` |
| `test_collisionneur_v9_v6.py` | `cd4c1337beb0…` |
| `appel_modeles_externes_v6.py` | `e2095843da99…` |
| `essais_appel_modeles_externes_v6.py` | `58738dca543e…` |
| `contre-lecture-collisionneur-v9-v5-v1.md` | `77041a13459a…` |
| `rapport-collisionneur-v9-v6-v1.md` | `c8a7092447be…` |
| `rapport-collisionneur-v9-v5-et-consultation-v5-v1-erratum-1.md` | `4519f20331c5…` |
| version employée en course : `collisionneur_v9_v3.py` | `850df3118073…` |

Essais rejoués une fois, en place, hors réseau, sans clés, dossiers temporaires à moi : **224 passés, 1 sauté** (201 du collisionneur et 23 de la consultation ; le sauté est la copie du run, non désignée). C'est le compte du registre (R-4579).

Mes sept mutations, différentes des 25 du développeur, chacune sur une copie :

| mutation | essais en échec |
|---|---|
| collisionneur, CO-1 : un plafond égal ne bloque plus | 2 |
| collisionneur, CO-1 : **premier essai lu au lieu du dernier** | **0 — non prise** (essai proposé, remarque 1) |
| collisionneur : préfixe cherché n'importe où dans le nom | 1 |
| collisionneur, CO-1 : cellule bloquée non comptée parmi les bloquées | 0 — sans effet : le tour suivant ferme la porte de lui-même, rien n'est envoyé |
| collisionneur : budget envoyé à Carbon borné à 32 768 | 2 |
| consultation : préfixe cherché n'importe où dans le nom | 1 |
| consultation : préfixe appliqué à Astra seulement | 0 — sans effet : le nom ne sert qu'à Astra |

## 2. Question 1 — les quatre corrections : portées et justes

Différentiel de la version 5 à la version 6 refait et lu ligne à ligne : il ne contient que les quatre corrections, les deux décisions de la mère (préfixe, réglages de Carbon), la version et les textes d'aide.

- **CO-1** : `reglage_en_defaut` et la branche de `lancer_etage` sont le code de la contre-lecture, à la lettre. Ses deux essais y sont, à la lettre.
- **CO-2** : `appeler_openai` et `compter_openai` refusent un nom absent ; code et essai à la lettre.
- **CO-3** : l'essai témoin y est, pour Carbon et pour Neon.
- **CO-4** : l'erratum existe, scellé ; le texte de la contre-lecture y est repris tel quel, plus une puce du développeur, exacte.

## 3. Question 2 — Carbon et les modèles de Google

### 3.1 Ce que la version 6 envoie (sonde sur les requêtes)

| espèce | plafond de sortie envoyé | budget de réflexion envoyé | seuil de la garde | délai total |
|---|---|---|---|---|
| Carbon | 65 536 | 49 152 | 49 152 | 5 400 s |
| Neon | 65 536 | 32 768 | 32 768 | 5 400 s |
| Argon | 18 000, relance 32 000 | 8 192 | 8 192 | 3 600 s |

- **Règle « Appels à Carbon » de CLAUDE.md** : tenue à la lettre. 65 536 − 49 152 = 16 384 jetons de texte, au moins 16 000 ; contrôlée à la composition et avant l'envoi.
- **Garde de dépense, réflexion au prix réel** : tenue. Le coût compté est entrée, plus texte, pensées et écart de total au prix de sortie ; le pire cas compte le plafond et la provision.
- **Flux long** : tenu, rien à changer. Attente d'un morceau 600 s, pensées demandées dans le flux, ce qui tient la connexion ; délai total 5 400 s pour 65 536 jetons, soit 12 jetons par seconde au moins, contre 70 à 87 relevés (rapport de la version 4). Une coupure est comptée au pire (2,30 USD pour Carbon, sonde), arrête la commande au code 5, sans renvoi dans la commande ; le texte partiel est gardé dans `essais/`. Une commande relancée renvoie la cellule : c'est un paiement neuf, voulu, à décider par l'arbitre.

### 3.2 Le défaut : le seuil de la garde est le budget, et le budget est souple

Fait relevé le 20 novembre : sous un budget de 32 768, Carbon a pensé 39 953 jetons (× 1,22). Ma sonde reporte ce dépassement sur la version 6 : 59 930 jetons de pensées, 5 606 de texte, fin « STOP », 65 536 au total, soit le plafond envoyé.

- Résultat : `REFLEXION_HORS_PROVISION`, **code 6**, 1,31 USD comptés, aucune cellule écrite, course arrêtée.
- Le pire cas compté pour cet envoi était 2,30 USD : la dépense était permise. **La garde se déclenche à tort** : elle compare les pensées au budget, pas la dépense à ce qui a été compté.
- La même commande relancée renvoie la cellule au même réglage et la repaie (sonde : 2,64 USD cumulés, deux arrêts au code 6). CO-1 ne couvre pas ce statut.
- Le développeur l'écrit lui-même (rapport, réserve 1) ; c'était la réserve 1 de la contre-lecture de la version 4 et la section 7 de celle de la version 5.

### 3.3 Ce qu'il faut changer, exactement

**V-1 (obligatoire, code).** La garde porte sur la sortie facturée (texte, pensées, écart) contre la sortie comptée au pire cas (plafond envoyé plus provision), et non sur les pensées contre le budget. Le budget reste envoyé ; la règle du plafond large et le code 9 ne changent pas. Texte exact en section 6. Effets, éprouvés sur copie :
- la réponse de la sonde (59 930 + 5 606) est gardée, `OK`, au coût réel ;
- une sortie d'un jeton au-delà de la sortie comptée donne toujours le code 6 ;
- des pensées qui mangent tout le plafond, sans texte, donnent le code 9 (défaut de réglage), que CO-1 empêche de renvoyer au même réglage.

**V-2 (obligatoire pour tenir GO-2026-11-21-63, réglages ; valeurs à confirmer par la mère).** La version 6 ne relève que Carbon. Argon reste à 8 192 de budget sous 18 000 de plafond : il est tenu court. Lignes du catalogue :
- Argon, ligne de la version 4 : `"max": 65536, "max_relance": 65536, "provision": 49152` (le reste inchangé). Pire cas par envoi : 5,73 USD au prix compté de 10 et 50 ; 2,29 USD au prix lu de 4 et 20 (remarque 4 de la contre-lecture de la version 5 : changer la table des prix est une décision à part).
- Neon : `"provision": 49152` au lieu de 32 768, après l'envoi d'essai demandé par la contre-lecture de la version 5 (réserve 1), s'il n'est pas fait.
- Délais inchangés : ils tiennent sur 65 536 jetons à 25 jetons par seconde (2 621 s).

**V-3 (recommandée, non éprouvée par moi ; décision de la mère).** Séparer le budget envoyé de la provision comptée, comme la contre-lecture de la version 5 (section 7) : champ `budget` par espèce de Google, lu par `appeler_gemini` (`"thinkingBudget": m.get("budget", m["provision"])`), écrit au journal, comparé aussi par `reglage_en_defaut`. Valeur : **budget 40 000, provision 49 152**. Raison : sous un plafond de 65 536 pensées comprises, 16 000 jetons de texte ne restent que si les pensées s'arrêtent à 49 536 ; au dépassement relevé (× 1,22), un budget de 40 000 donne au plus 48 800 jetons de pensées. Envoyer 49 152 laisse penser jusqu'à 59 900 et ne laisse que 5 600 jetons au texte, moins que les 8 400 à 11 770 relevés : la réponse sort coupée, puis est relancée au même plafond, payée deux fois. Ce chiffre repose sur un seul relevé.

### 3.4 « Jusqu'au bout » : deux limites que ni V-1 ni V-2 ne lèvent

À dire à Lazar. Les deux reposent sur des pages lues le 20 novembre par le développeur de la version 4 et **non versées** (provenance par transcription, R7) ; je ne les ai pas relues.

1. **Le plafond synchrone.** Ces pages disent : 65 536 jetons de sortie « including thought tokens », coupure ferme ; au-delà, « long decode », jusqu'à 1 048 576 (aussi sur la page versée de Neon, `2eadc192…`). Sous 65 536, la réflexion ne peut pas dépasser 49 536 jetons si l'on garde 16 000 jetons de texte. Penser plus loin demande le « long decode », que le script n'emploie pas : page à verser et à lire, conception à part.
2. **Le niveau de réflexion.** Ces pages disent qu'Argon et Carbon réfléchissent par niveaux (low, medium, high ; Neon : jusqu'à xhigh), **medium par défaut**, et qu'aucun budget n'y est documenté pour eux. Les deux scripts n'envoient qu'un budget, jamais un niveau. Si Google ignore le budget, ces modèles tournent au niveau moyen. À instruire avant la version suivante : verser la page de la réflexion, y lire le nom du champ et s'il se cumule avec le budget. Un refus (erreur 400) ne coûte rien. Passer au niveau, c'est ne plus borner la réflexion en jetons : la phrase « la réflexion bornée à part » de CLAUDE.md est alors à relire par Lazar.

### 3.5 Consultation version 6

- Aucune garde sur les pensées : rien ne se déclenche à tort. Plafond envoyé = réflexion + texte ; pire cas compté à une fois et demie ce plafond, sous 4 USD ; attente d'un morceau 600 s, pas de délai total.
- Les défauts tiennent Carbon court (24 000 de réflexion, 16 000 de texte). Pour le laisser réfléchir : `--reflexion 49152 --texte 16384` (pire cas 1,97 USD) ; ou, avec la marge de V-3, `--reflexion 40000 --texte 25536` (même plafond, même pire cas). Neon : défaut 32 768 + 32 768, ou les mêmes options. Argon : `--reflexion 36000 --texte 16384` au plus (3,93 USD au prix compté), le plafond de 4 USD refusant davantage.
- Ne pas passer `--reflexion 0` à Carbon ni à Neon (remarque 2 de la contre-lecture de la version 5, non traitée).

## 4. Question 3 — la garde du nom de la clé d'OpenAI : tient

- Dans les deux scripts, `--cle-openai` n'accepte qu'un nom bien formé qui **commence** par `OPENAI_API_KEY` ; sinon code 1, avant toute écriture et tout appel, sans répéter le nom. `GEMINI_API_KEY`, `TYPESAFE_API_KEY`, `CLE_OPENAI_API_KEY`, `OPENAI_KEY` sont refusés ; `OPENAI_API_KEY_2` passe.
- Sonde de bout en bout, `OPENAI_API_KEY` absente et `--cle-openai OPENAI_API_KEY_2` : c'est la valeur de la variable nommée qui part vers OpenAI, à l'envoi et au comptage ; ni la valeur ni le nom ne sont écrits dans le dossier ni affichés.
- **La forme à préfixe de commande** `OPENAI_API_KEY="$OPENAI_API_KEY_2" python … ` (la seule possible avec la version 3, qui n'a pas l'option) marche aussi avec la version 6, sans `--cle-openai` : le nom par défaut est lu. Les deux formes envoient la même clé. Avec la version 6, préférer `--cle-openai OPENAI_API_KEY_2` : la valeur ne passe pas par la ligne de commande de l'interpréteur.
- À savoir : si l'option est oubliée et que `OPENAI_API_KEY` existe, c'est ce compte qui est employé, sans message. Le nom n'étant pas au journal, rien ne dit après coup quel compte a payé. Sans gravité pour la clé ; à tenir dans la commande versée.
- Limite dite par le développeur, juste : le préfixe ne prouve pas que la variable porte une clé d'OpenAI.

## 5. Question 4 — reprise d'un dossier créé par la version 3 (`850df311…`) : sans perte, sans double paiement

Sonde : dossier créé par la version 3 elle-même (empreinte contrôlée dans la sonde), étage III, cinq espèces (`--fable --opus --argon --astra --carbon`), tour 1 complet, tour 2 arrêté chez Carbon par la garde de réflexion (39 953 > 32 768), ligne de 25,90 USD ouverte. Puis la version 6 :

- `verifier` : « tout tient » ; seul `etat.md` est régénéré.
- Sans `--reprise` : code 1, aucun envoi, aucun comptage, journal inchangé à l'octet.
- Avec `--reprise` : six cellules envoyées, pas une de plus (sept requêtes, Astra en comptant deux) — la cellule de Carbon du tour 2, puis les cinq du tour 3. Aucune cellule valide n'est renvoyée.
- Tous les fichiers d'avant sont intacts à l'octet ; le journal d'avant est un préfixe du journal d'après ; une seule déclaration de changement de script, une seule ligne.
- Dépense = dépense d'avant + essais neufs ; la ligne compte depuis son ouverture par la version 3.
- La réponse de Carbon à 39 953 jetons de pensées est gardée sous la version 6.
- `devis-reprise` de la version 6 lit le dossier sans rien écrire.
- La même commande relancée après la fin : aucun envoi.

Deux contraintes :
1. **Un run garde sa ligne et ses espèces.** `--ligne-usd` avec un autre montant est refusé (code 1) ; sans l'option, la ligne ouverte s'applique encore. Le pire cas de Carbon monte (2,30 USD par envoi au lieu de 1,97 ; Argon à 5,73 si V-2) : si le reste de la ligne ne suffit pas, la cellule est refusée avant l'envoi (code 4), sans perte ni paiement, mais la course ne finit pas dans ce dossier. Lancer `devis-reprise` avant chaque reprise. Aucune version ne sait relever une ligne : si Lazar accorde plus, c'est une conception à part. Neon ne peut pas être ajouté à un dossier existant ; Astra n'est repris que s'il est dans `especes.json`.
2. **Les cellules arrêtées après paiement sous la version 3** (garde, coupure, délai) sont renvoyées : paiement neuf, voulu. Pour Astra, la réponse créée en arrière-plan sous l'ancienne clé a peut-être fini chez OpenAI : son identifiant est au journal (`id_reponse`) ; la relever avec l'ancienne clé avant de la repayer, si la clé vit encore.

## 6. Corrections en texte exact

Version neuve, nom neuf (R12) : `collisionneur_v9_v7.py` et `test_collisionneur_v9_v7.py`. Éprouvé sur copie, avec l'essai de la remarque 1 : 201 passés, 1 sauté, 2 écartés (les deux essais qui lisent les pages versées, absentes de ma copie) ; V-1 retirée, 3 essais échouent.

### V-1. La garde de réflexion porte sur la sortie comptée (code)

Remplacer `def juger(m, rep, prompt, pire, garde=None):` par :

```python
def juger(m, rep, prompt, pire, garde=None, max_tokens=None):
```

Dans `juger`, remplacer les deux lignes

```python
    if m["provision"] and rep.usage.get("reflexion", 0) > m["provision"]:
        return "REFLEXION_HORS_PROVISION", c
```

par :

```python
    sortie_comptee = (m["max_relance"] if max_tokens is None else max_tokens) + m["provision"]  # v9-v7 (V-1)
    if m["provision"] and rep.usage.get("sortie", 0) > sortie_comptee:
        return "REFLEXION_HORS_PROVISION", c
```

Dans `executer_cellule`, remplacer `statut, cout_usd = juger(m, rep, prompt, pire, compte["garde"])` par :

```python
        statut, cout_usd = juger(m, rep, prompt, pire, compte["garde"], max_tokens)  # v9-v7 (V-1)
```

Textes à accorder : docstring de `juger`, code 6 de l'en-tête et commentaire de `STATUT_REGLAGE` (« sortie facturée au-delà de la sortie comptée au pire cas » au lieu de « réflexion au-delà de la provision »).

### V-1, essais

Remplacer `test_garde_a_artefact_reflexion_au_dela_de_la_provision` par :

```python
def test_garde_a_artefact_sortie_au_dela_de_la_sortie_comptee(c, tmp_path):  # v9-v7 (V-1)
    m = c.CATALOGUE["argon"]
    comptee = m["max"] + m["provision"]  # sortie comptée au pire cas du premier envoi
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=comptee - 50 + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "argon")
    assert e.value.code == c.CODE_GARDE and len(c.TRANSPORT.appels) == 1
    d = journal(c, tmp_path)[-1]
    assert d["statut"] == "REFLEXION_HORS_PROVISION"
    assert d["cout_usd"] == round(500 * m["prix"][0] / 1e6 + (comptee + 1) * m["prix"][1] / 1e6, 4)  # coût réel compté
    assert not c.chemin_cellule(tmp_path, d["cellule"]).exists()


def test_garde_a_sain_reflexion_au_dela_du_budget_sous_la_sortie_comptee(c, tmp_path):  # v9-v7 (V-1)
    """Le budget de réflexion est une limite souple chez Google : une réponse complète dont les pensées dépassent le budget
    envoyé, et dont la sortie facturée tient sous la sortie comptée au pire cas, est gardée, au coût réel."""
    m = c.CATALOGUE["argon"]
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=m["provision"] + 1))
    assert executer(c, tmp_path, "argon") == "OK"
    d = journal(c, tmp_path)[-1]
    assert d["cout_usd"] == round(500 * m["prix"][0] / 1e6 + (50 + m["provision"] + 1) * m["prix"][1] / 1e6, 4)
    assert d["cout_usd"] <= d["cout_pire_usd"] and c.chemin_cellule(tmp_path, d["cellule"]).exists()
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-argon", pensees=m["max"] + m["provision"] - 50))  # bord
    assert executer(c, tmp_path / "bord", "argon") == "OK"
```

Remplacer `test_v5_neon_max_tokens_reflexion_hors_provision_reste_garde_de_depense` par :

```python
def test_v5_neon_max_tokens_sortie_hors_compte_reste_garde_de_depense(c, tmp_path):  # v9-v7 (V-1)
    """Ordre des gardes gardé : une sortie facturée au-delà de la sortie comptée est REFLEXION_HORS_PROVISION (code 6),
    avant le défaut de réglage. Sain : des pensées au-delà du budget qui mangent tout le plafond envoyé, sans texte, sont
    le défaut de réglage (code 9), au coût réel."""
    m = c.CATALOGUE["neon"]
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele="gemini-4-neon", fin="MAX_TOKENS", candidats=0,
                                            pensees=m["max"] + m["provision"] + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "neon")
    assert e.value.code == c.CODE_GARDE and len(c.TRANSPORT.appels) == 1
    assert journal(c, tmp_path / "artefact")[-1]["statut"] == "REFLEXION_HORS_PROVISION"
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele="gemini-4-neon", fin="MAX_TOKENS", candidats=0,
                                            pensees=m["max"]))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "sain", "neon")
    assert e.value.code == c.CODE_REGLAGE and len(c.TRANSPORT.appels) == 1
    assert journal(c, tmp_path / "sain")[-1]["statut"] == "MAX_TOKENS_SANS_TEXTE"
```

Dans `test_v6_carbon_reponse_du_20_novembre_gardee_et_artefact_au_dela`, remplacer les trois lignes

```python
    c.TRANSPORT = FauxTransport(flux_gemini(pensees=49153))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "carbon")
```

par :

```python
    c.TRANSPORT = FauxTransport(flux_gemini(pensees=59930, candidats=5606))
    assert executer(c, tmp_path / "depassement", "carbon") == "OK"
    d = c.essais_journal(tmp_path / "depassement")[-1]
    assert d["cout_usd"] == round(500 * 4 / 1e6 + 65536 * 20 / 1e6, 4) and d["cout_usd"] <= d["cout_pire_usd"]
    c.TRANSPORT = FauxTransport(flux_gemini(pensees=65536 + 49152 - 50 + 1))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path / "artefact", "carbon")
```

et accorder sa docstring (« Artefact : sortie facturée au-delà de 65 536 + 49 152 »).

### V-2. Réglages d'Argon et de Neon (table)

Dans `CATALOGUE`, sur confirmation de la mère :

```python
    "argon": {"id": "gemini-4-argon", "fournisseur": "gemini", "prix": (10.0, 50.0),
              "max": 65536, "max_relance": 65536, "provision": 49152, "car_par_jeton": 2.5, "delai_s": 3600},
```

```python
    "neon": {"id": "gemini-4-neon", "fournisseur": "gemini", "prix": (3.0, 15.0),
             "max": 65536, "max_relance": 65536, "provision": 49152, "car_par_jeton": 2.5, "delai_s": 5400},
```

Essais à accorder : ceux qui attendent 8 192, 18 000 et 32 000 pour Argon, 32 768 pour Neon, et `test_v6_carbon_reprend_les_reglages_du_v4_et_tient_la_regle` (Argon n'est plus celui de la version 3). Les essais de V-1 ci-dessus lisent le catalogue : ils ne changent pas.

## 7. Remarques (non bloquantes)

1. **Essai témoin pour CO-1** (ma mutation non prise ; éprouvé, il la prend) :
   ```python
   def test_v7_defaut_de_reglage_lu_sur_le_dernier_essai(c, tmp_path):
       c.TRANSPORT = FauxTransport(flux_gemini(texte="", fin="STOP", candidats=0, pensees=100), _vide_max("gemini-4-carbon"))
       with pytest.raises(c.Arret) as e:
           executer(c, tmp_path, "carbon")
       assert e.value.code == c.CODE_REGLAGE and [x["statut"] for x in journal(c, tmp_path)] == ["VIDE", "MAX_TOKENS_SANS_TEXTE"]
       l = lettre_de(c, "carbon")
       assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T1", l), c.MODELES[l]) is True
   ```
2. **Réponse coupée relancée au même plafond** (gardée par décision). Avec un budget relevé, une coupure n'est plus un emballement rare : c'est l'issue attendue d'un dépassement du budget. Tout devis donne donc le pire cas doublé pour Carbon, Neon et Argon ; V-3 réduit ce cas.
3. **La liste versée donne 32 768 jetons de sortie à Argon comme à Carbon.** Carbon a été servi à 65 536 le 20 novembre ; Argon ne l'a jamais été. Un refus de Google (erreur 400) ne coûte rien, mais arrête la course au code 5 : essayer Argon par la consultation avant la première reprise sous V-2.
4. Les remarques 2 et 7 et la réserve 3 de la contre-lecture de la version 5 restent ouvertes, comme le dit le développeur.

## 8. Avant tout appel

1. V-1 est faite, V-2 tranchée par la mère, puis vérifiées par moi.
2. Pour chaque dossier repris : `verifier`, puis `devis-reprise`, par la version neuve ; la ligne restante couvre le pire cas, ou Lazar est saisi.
3. La commande de reprise est écrite et versée, avec `--reprise` et `--cle-openai OPENAI_API_KEY_2` ; le devis donne le pire cas doublé pour les modèles de Google.
4. Les deux limites de la section 3.4 sont dites à Lazar.

## Limites

- Aucun appel réel. Le comportement de Google devant un budget de 49 152 n'est pas connu ; le dépassement de 22 % repose sur un seul relevé.
- Je n'ai lu aucun journal de course réelle : la reprise est éprouvée sur un dossier fabriqué par la version 3 avec de faux fournisseurs, pas sur une copie d'un run.
- V-3 n'est pas éprouvée.
- Mes outils sont dans mon bloc-notes, qui n'est pas durable : `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/K0/test_sondes_verif.py` (sondes), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/outils/corrections_v1.py` (V-1 et ses essais, appliqués sur copie), `/tmp/claude-0/-home-user-controle-ia-travail/2eb82089-3810-5ff8-881f-da5f24b622eb/scratchpad/outils/mut.py` (mutations).

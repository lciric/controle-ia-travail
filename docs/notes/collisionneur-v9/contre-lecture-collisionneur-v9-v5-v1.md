# Contre-lecture : collisionneur v9 version 5 et consultation des modèles externes version 5

Écrite le 21 novembre 2026 par un contre-lecteur neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5). Pièce d'instrument (classe B). Je n'ai écrit aucune des pièces relues.

Ce que je n'ai pas fait : aucun appel à un modèle, aucun comptage de jetons, aucune requête sur le réseau, aucune dépense ; aucune valeur de clé affichée ni écrite (présence testée par le nom seulement) ; aucun commit ; aucun fichier du dépôt modifié hors cette pièce et son sceau ; rien lu sous `runs/` ni sous `archives-reponses-modeles/`. Tous mes essais ont tourné sur des copies, dans mon bloc-notes, réseau fermé par les doublures.

## Verdict

**Prêt après corrections.**

- **Consultation version 5** (`appel_modeles_externes_v5.py`) : conforme, aucune correction obligatoire. Elle peut servir telle quelle à l'envoi d'essai vers Neon (section 6, réserve 1).
- **Collisionneur version 5** (`collisionneur_v9_v5.py`) : conforme sur les quatre règles dans tout ce qu'une commande exécute, mais trois corrections obligatoires de code et d'essais, et une de texte (section « Corrections obligatoires »). La principale : après un arrêt au code 9, relancer la même commande renvoie la cellule au même réglage et la paie une seconde fois.
- **Une décision revient à la mère avant tout envoi à Carbon** : la base version 3 remet en service la provision de 32 768 qui a arrêté une cellule payée de Carbon le 20 novembre (section 7).

## Pièces relues

Empreintes recalculées, toutes égales aux compagnons (`controle_ia.scellement verifier`) :

| fichier | empreinte |
|---|---|
| `rapport-collisionneur-v9-v5-et-consultation-v5-v1.md` | `be7f572f40f8…` |
| `collisionneur_v9_v5.py` | `697f01512ad2…` |
| `test_collisionneur_v9_v5.py` | `624b522994f0…` |
| `appel_modeles_externes_v5.py` | `4c44b89ed976…` |
| `essais_appel_modeles_externes_v5.py` | `8a66f62fa72d…` |
| `page-prix-gemini-api-20261121T134918Z.html` | `40202cdd6fc4…` |
| `page-modele-gemini-4-neon-20261121T134943Z.html` | `2eadc1928040…` |
| `liste-modeles-gemini-20261121T134904Z.json` | `eeec19e80408…` |
| bases : `collisionneur_v9_v3.py`, `collisionneur_v9_v4.py`, `appel_modeles_externes_v4.py` | `850df3118073…`, `46f1d917a2d8…`, `b31fecf2ce1c…` |

Lus aussi, pour le point 7 : `rapport-developpeur-collisionneur-v9-v4.md` et `contre-lecture-collisionneur-v9-v4-v1.md`.

## 1. Les différentiels — conforme

- J'ai refait les deux différentiels unifiés (`diff -u`) et je les ai comparés, octet par octet, aux blocs du rapport : **identiques** (collisionneur : 292 lignes ; consultation : 130 lignes).
- Lu ligne à ligne, le différentiel du collisionneur ne contient que ce que le rapport annonce : l'en-tête et l'aide d'usage ; la version ; Neon dans la table, en fin d'ordre ; la table de la règle (`REGLE_TEXTE_MIN`) et sa fonction ; le code 9 et son statut ; le nom de la clé d'OpenAI à la composition, à l'envoi, au comptage et dans la ligne de commande. Aucune formule de coût, aucune garde de dépense, de motifs, de reprise ou de refus, aucun délai, aucun prix d'une autre espèce ne change.
- Même constat pour la consultation : Neon dans les quatre tables, le plancher de texte étendu, le motif « défaut de réglage », l'option `--cle-openai`, le champ `variable_cle`.
- La partie reprise des essais du collisionneur est bien la suite de la version 3 et son complément, aux trois écarts annoncés près (comparaison par programme).

## 2. Prix de Neon et calcul du coût — conforme

- La page versée, section « Gemini 4 Neon », onglet « Standard », porte « Input price $3.00 » et « Output price (including thinking tokens) $15.00 », par million de jetons, palier payant. Aucun palier selon la longueur de l'entrée, aucun changement daté pour Neon. Les autres paliers cités par le rapport sont justes (1,50 et 7,50 ; 5,40 et 27).
- La liste versée donne `models/gemini-4-neon`, sortie 65 536, entrée 1 048 576, réflexion vraie, sur 65 modèles. Aucune valeur de clé présente dans l'environnement ne figure dans la liste ni dans la page de prix (comparaison par programme, valeurs jamais affichées).
- Coût réel : entrée au prix d'entrée, réponse visible **plus pensées** (plus l'écart de total de Google) au prix de sortie. Mes deux retraits « coût compté sans la réflexion » font échouer 7 essais du collisionneur et 2 de la consultation.
- Pire cas : garde d'entrée au prix d'entrée, plus plafond et provision au prix de sortie. Les six chiffres de la table du rapport sont refaits et justes (1,4746 ; 1,5640 ; 1,6846 ; doubles 2,9491 ; 3,1279 ; 3,3691), ainsi que Carbon à 29 800 jetons (2,0853 ; 4,1706).
- Consultation : pire cas de Neon aux réglages par défaut, 1,4746 USD hors entrée, sous le plafond de 4 USD.

## 3. Règle du plafond large et code 9 — conforme dans une commande, correction obligatoire à la relance

Conforme :
- **À la composition** : pour Carbon et Neon, provision positive et plafond moins provision d'au moins 16 000 jetons, sur le premier plafond et sur celui de relance ; refus au code 1, rien n'est fixé.
- **Avant l'envoi** : même contrôle dans `executer_cellule`, après la garde de motifs, avant le comptage ; refus consigné au journal, code 1, aucun comptage, aucun envoi.
- **Réflexion bornée à part** : le budget envoyé est la provision ; la garde de réflexion (code 6) reste avant le code 9.
- **Code 9** : fin « MAX_TOKENS », texte vide, espèce sous la règle ; coût réel compté, aucune cellule écrite, aucun second envoi dans la commande. Argon garde le comportement de la version 3. La commande `verifier` tient un dossier qui porte ce statut neuf (sonde).
- **Consultation** : plancher de 16 000 jetons de texte pour Neon ; motif « défaut de réglage, pas une réponse » pour Carbon et Neon, seulement sans texte ; code 3.

À corriger (CO-1) : **une simple relance de la commande renvoie la cellule au même réglage.** Constaté par sonde : après un arrêt au code 9 chez Carbon, la même commande `etage1` renvoie la cellule au même plafond (65 536) et au même budget (32 768), s'arrête de nouveau au code 9, et compte 0,66 USD une seconde fois. Le rapport et le message d'arrêt disent « aucune relance au même réglage » : ce n'est vrai que dans une commande. Or le réglage vit dans la table du script : sous ce script, tout nouvel envoi de cette cellule est au même réglage. Et ce cas ne se produit que si le plafond appliqué par Google est plus bas que le plafond envoyé (réserve 2) : le second envoi échouerait de la même façon.

## 4. Clé d'OpenAI choisie par son nom — conforme, une correction obligatoire de prudence

Conforme :
- Variable nommée absente : refus au code 1, par son nom, avant toute écriture, aux trois étages ; la clé par défaut, présente, n'est pas lue (mes retraits « repli silencieux à l'envoi », « au comptage », « présence non contrôlée » et « clé par défaut préférée » sont tous pris).
- Nom mal formé, nom vide, valeur collée à la place du nom : refus au code 1, sans répéter ce qui a été donné.
- Le nom n'entre ni dans `especes.json` ni dans le journal ; la valeur n'apparaît dans aucun fichier ni aucune sortie ; les messages d'erreur sont masqués par la valeur de la clé nommée.
- Consultation : mêmes contrôles ; seul le nom de la variable est écrit, au champ `variable_cle`.

À corriger (CO-2) : **un repli dormant reste dans le code.** `appeler_openai` et `compter_openai` lisent `m.get("nom_cle") or NOMS_CLES["openai"]`. Aucune commande n'y arrive aujourd'hui, la composition posant toujours un nom. Mais si le nom manque, la clé par défaut est lue en silence (sonde : l'envoi et le comptage partent avec `OPENAI_API_KEY`). La règle est « sans repli silencieux » : ce bout de code doit refuser.

## 5. Essais et mutations

Suites rejouées, hors réseau, dossier temporaire à moi :

| suite | résultat |
|---|---|
| `test_collisionneur_v9_v5.py`, en place | 186 passés, 1 sauté (la copie du run, non désignée) |
| `essais_appel_modeles_externes_v5.py`, en place | 21 passés |
| suite de la version 3 et son complément, sur une copie sans run | 156 passés, 1 sauté |

Mes mutations, toutes différentes de celles du développeur, chacune sur une copie :

| mutation du collisionneur | essais en échec |
|---|---|
| le défaut de réglage passe avant la garde de réflexion (le code 9 masque le code 6) | 1 |
| code 9 étendu à un texte coupé | 1 |
| **code 9 étendu à toute sortie vide, fin « STOP » comprise** | **0 — non prise** |
| repli silencieux sur la clé par défaut à l'envoi, variable nommée absente | 1 |
| même repli au comptage | 1 |
| présence de la clé d'OpenAI nommée non contrôlée au lancement | 4 |
| règle vérifiée sur le premier plafond seulement, avant l'envoi | 1 |
| règle vérifiée sur le premier plafond seulement, à la composition | 2 |
| bord : exactement 16 000 jetons de texte refusés | 1 |
| coût d'un défaut de réglage compté zéro | 2 |
| nom mal formé répété dans le message | 1 |
| budget de réflexion non envoyé à Neon | 2 |
| nom de la clé d'OpenAI écrit dans `especes.json` | 3 |
| provision nulle acceptée par la règle | 1 |
| pire cas de Neon compté sans la provision | 1 |
| clé par défaut préférée en silence quand elle existe | 4 |
| coût réel compté sans la réflexion | 7 |

| mutation de la consultation | essais en échec |
|---|---|
| repli silencieux sur la clé par défaut, variable nommée absente | 2 |
| motif « défaut de réglage » posé aussi sur un texte partiel | 1 |
| nom mal formé répété dans le message | 1 |
| `--cle-openai` appliquée à toutes les espèces | 1 |
| coût compté sans la réflexion | 2 |
| bord : exactement 16 000 jetons de texte refusés | 4 |
| valeur de la clé écrite au champ `variable_cle` | 2 |
| budget de réflexion non envoyé à Neon | 1 |
| texte partiel écrit sous le nom de la réponse | 2 |

Les essais mordent : 25 mutations sur 26 sont prises. Celle qui passe demande un essai témoin (CO-3). Je n'ai pas rejoué les 21 mutations du développeur : son outil est dans son bloc-notes.

## 6. Les trois réserves du développeur

### Réserve 1 — le budget de réflexion n'a jamais été envoyé à Neon

Conforme dans le code : un refus de Google (erreur 400) donne un échec sans coût, un seul envoi, aucun repli (collisionneur : code 5, essai du développeur ; consultation : code 1, ma sonde).

Ce qu'il faut faire : **un envoi d'essai à Neon par la consultation version 5, avant toute composition du collisionneur avec Neon.**
- Pourquoi avant : dans le collisionneur, Neon porte la dernière lettre. Un refus arrêterait l'étage après que toutes les autres espèces du tour ont été payées, et le run garderait une espèce morte, scellée dans sa composition.
- Comment : `appel_modeles_externes_v5.py neon ÉNONCÉ SORTIE_MD SORTIE_JSON`, réglages par défaut (budget 32 768, plafond 65 536), énoncé neutre et court. Pire cas compté : 1,47 USD plus l'entrée ; coût réel d'environ 0,98 USD au plus, si le plafond de sortie borne bien le total des pensées et du texte. C'est une dépense : la mère cite son accord.
- Lecture :
  - code 0, pensées entre 1 et 32 768 : le budget est accepté et tenu ;
  - code 0, pensées au-delà de 32 768 : budget souple chez Neon aussi ; le collisionneur arrêterait la cellule au code 6 ; noter le rapport, il sert au point 7 ;
  - code 0, aucune pensée : le budget ne règle rien, comme chez Argon ; le réglage tient ;
  - code 1, fin `http_400` : Neon refuse le budget. Il n'entre pas au collisionneur sous ce script. Passer au niveau de réflexion est une autre conception : la réflexion n'y est plus bornée en jetons, et la règle « réflexion bornée à part » doit alors être relue par Lazar ;
  - code 3 : défaut de réglage ; ne pas relancer, porter le JSON à la mère.

### Réserve 2 — la liste donne 32 768 jetons de sortie pour Carbon, le script envoie 65 536

Ce qu'il faut faire : **ne rien changer au plafond, et surtout ne pas le descendre à 32 768.**
- La liste n'est pas une description fiable du service : elle ne nomme la génération en flux pour aucun modèle Gemini 4, alors que Carbon a été servi en flux.
- Le 20 novembre, Google a accepté les trois envois à Carbon de l'étage III au plafond de 65 536 (versions 2 et 3, même table), et Carbon a rendu au tour 2 50 251 jetons de sortie (39 953 de pensées, 10 298 visibles ; rapport de la version 4). La limite listée n'est donc pas appliquée au total des pensées et du texte.
- Si elle borne le seul texte visible, il reste 32 768 jetons de texte : la règle tient.
- Descendre le plafond à 32 768 avec un budget de 32 768 ne laisserait aucun jeton de texte garanti : la règle serait rompue.
- Le cas défavorable (Google se met à couper à 32 768, pensées comprises) donnerait un arrêt « MAX_TOKENS » sans texte : c'est le code 9. D'où le poids de CO-1.
- À faire en plus, sans coût : verser et empreinter la page publique du modèle Carbon, comme celle de Neon (« Max output 65,536 » n'est connu que par extraits, rapport de la version 4) ; à la première cellule de Carbon, lire au journal la fin, les pensées et la sortie visible.
- Le défaut de Carbon dans la consultation (24 000 + 16 000 = 40 000) est dans le même cas ; même réponse.

### Réserve 3 — une réponse coupée est relancée au même plafond

Ce qu'il faut faire : **la garder dans cette version ; la traiter dans la suivante.**
- Ce n'est pas le défaut de réglage de la règle : il y a du texte.
- Chez Carbon et Neon, un texte coupé sous 65 536 avec des pensées dans la provision veut dire plus de 32 768 jetons de texte visible, près de trois fois la plus longue réponse relevée (11 770). C'est un emballement, pas un plafond trop court. La relance est un nouveau tirage ; elle est bornée par le plafond et par la ligne (refus avant l'envoi, éprouvé).
- Elle ne devient un gaspillage certain que dans le cas de la réserve 2 : Google coupe plus bas que le plafond envoyé. Ce cas se reconnaît au journal : fin « MAX_TOKENS » et sortie totale nettement sous le plafond envoyé.
- Pour la version suivante (conception à part, non bloquante) : garde « coupure sous le plafond envoyé » — fin « MAX_TOKENS » avec une sortie totale sous le plafond envoyé, chez une espèce sous la règle : code 9, aucune relance, texte présent ou non.
- Dès maintenant : tout devis présenté à Lazar donne, pour Carbon et Neon, le pire cas « avec relance » (le double).

## 7. Base version 3 ou provisions de la version 4

**Recommandation : pas la base version 3 telle quelle pour Carbon. Entre les deux, les provisions de la version 4 ; mieux, les séparer en deux réglages.**

Ce que le rapport ne dit pas (section 0) :
- La provision de 32 768 est le réglage sous lequel la critique de Carbon du tour 2 a été arrêtée le 20 novembre, payée et sans cellule : 39 953 jetons de pensées pour 32 768 de budget. Rejouée sur la version 5, cette réponse donne le code 6, 1,01 USD comptés (sonde). Une cellule de Carbon sur trois ce jour-là.
- La version 4 répondait à une demande du directeur du 20 novembre : « donne plus de provision de réflexion à Carbon et Argon ». Partir de la version 3 défait cette demande sans le dire.
- Les provisions de la version 4 tiennent la règle du 21 novembre à la lettre : 65 536 − 49 152 = 16 384, au-dessus de 16 000. Elles satisfont donc les deux mots du directeur ; la base version 3 n'en satisfait qu'un.

Ce que la version 4 risque : son budget envoyé monte aussi à 49 152. Si la réflexion suit le budget et le dépasse comme le 20 novembre (22 %), il reste 5 600 jetons au texte : c'est ce que la règle veut éviter. C'était la réserve 1 de la contre-lecture de la version 4.

La forme qui tient les deux (proposition de conception, quelques lignes, à joindre à la version corrigée si la mère le décide) :
- **budget envoyé à Google : 32 768** (accepté par Google le 20 novembre ; le texte garde 32 768 jetons, et encore 25 583 dans le cas du dépassement relevé) ;
- **seuil de la garde et provision comptée au pire cas : 49 152** (la réponse du 20 novembre aurait été gardée) ;
- la règle se vérifie sur le seuil de garde : toute cellule acceptée a disposé d'au moins 16 384 jetons de texte ;
- un champ neuf par espèce de Google (« budget », au plus égal à la provision), lu par `appeler_gemini`, écrit au journal ; même valeurs pour Neon ;
- pire cas à 29 800 jetons d'entrée : Carbon 2,41 USD au lieu de 2,09 ; Neon 1,81 USD au lieu de 1,56.

Si la mère veut seulement choisir entre les deux tables : Carbon à 49 152 (version 4). Neon reste à 32 768 jusqu'à l'envoi d'essai de la réserve 1. Argon : la version 4 multiplie son pire cas par 3,75 sans effet relevé sur sa réflexion (il ne rend aucune pensée) ; à porter seulement sur confirmation, avec la remarque 4.

## Corrections obligatoires

Le script scellé n'est pas réécrit : version neuve, nom neuf (R12). Le code et les essais ci-dessous ont été appliqués sur une copie et éprouvés : 191 essais passés, 1 sauté, avec CO-1 à CO-3 ; 194 avec le durcissement de la remarque 1 et ses trois essais. Chaque retrait d'une correction fait échouer son essai.

### CO-1. Un défaut de réglage n'est jamais renvoyé au même réglage (code)

Après la ligne `STATUT_REGLAGE = "MAX_TOKENS_SANS_TEXTE"` :

```python
def reglage_en_defaut(dossier, cid, m):
    """v9-v6 : vrai si le dernier essai de la cellule s'est arrêté en MAX_TOKENS sans texte (STATUT_REGLAGE) sous le
    réglage que le script enverrait de nouveau : même provision, et aucun plafond de sortie au-dessus de celui de cet
    essai. Une telle cellule n'est jamais renvoyée : il faut une absence acceptée, ou un script au réglage corrigé."""
    essais = essais_journal(dossier, cid)
    if not essais or essais[-1]["statut"] != STATUT_REGLAGE:
        return False
    dernier = essais[-1]
    return (dernier.get("provision_reflexion") == m["provision"]
            and max(m["max"], m["max_relance"]) <= dernier.get("max_tokens", 0))
```

Dans `lancer_etage`, juste après la branche du refus (`bloquees.append(cid)  # un refus est définitif dans un run` et son `continue`) :

```python
            elif reglage_en_defaut(dossier, cid, MODELES[lettre]):  # v9-v6 : jamais de renvoi au même réglage
                print(f"{cid} : arrêt en MAX_TOKENS sans texte au dernier essai, réglage inchangé (plafond et "
                      f"provision) : non renvoyée ; il faut --accepter-absence, ou un script au réglage corrigé "
                      f"(--reprise)", flush=True)
                bloquees.append(cid)
                continue
```

Essais à ajouter :

```python
def _vide_max(modele):
    return flux_gemini(texte="", modele=modele, fin="MAX_TOKENS", candidats=0, pensees=32768)


def test_v6_defaut_de_reglage_jamais_renvoye_au_meme_reglage(c, tmp_path, monkeypatch, capsys):
    faits = tmp_path / "faits.md"
    faits.write_text("Fait 1 (HYPOTHÈSE) : texte sain.\n", encoding="utf-8")
    sortie = tmp_path / "run"
    argv = ["etage1", "--carbon", "--neon", "--faits", str(faits), "--sortie", str(sortie)]
    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
    assert c.principal(argv) == c.CODE_REGLAGE  # premier lancement : arrêt au code 9, un envoi
    # Artefact : la même commande ne renvoie rien à Carbon ; Neon part ; porte fermée après le tour.
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-neon"))
    assert c.principal(argv) == c.CODE_PORTE
    assert [a["url"].split("/")[-1].split(":")[0] for a in c.TRANSPORT.appels] == ["gemini-4-neon"]
    assert [e["statut"] for e in c.essais_journal(sortie, "E1-T1-meta-A")] == ["MAX_TOKENS_SANS_TEXTE"]
    assert "non renvoyée" in capsys.readouterr().out
    # Sain 1 : l'absence acceptée par l'arbitre laisse l'étage finir, sans envoi à Carbon au tour 1.
    c.TRANSPORT = FauxTransport(flux_gemini(modele="gemini-4-carbon"), flux_gemini(modele="gemini-4-neon"))
    assert c.principal(argv + ["--accepter-absence", "E1-T1-meta-A"]) == c.CODE_FINI
    assert [e["statut"] for e in c.essais_journal(sortie, "E1-T1-meta-A")] == ["MAX_TOKENS_SANS_TEXTE"]


def test_v6_defaut_de_reglage_renvoye_si_le_reglage_a_change(c, tmp_path, monkeypatch):
    """Sain 2 : sous un réglage différent, la cellule repart."""
    c.TRANSPORT = FauxTransport(_vide_max("gemini-4-carbon"))
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "carbon")
    assert e.value.code == c.CODE_REGLAGE
    l = lettre_de(c, "carbon")
    cid = c.id_cellule("E1-T1", l)
    assert c.reglage_en_defaut(tmp_path, cid, c.MODELES[l]) is True
    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], provision=24576)) is False
    assert c.reglage_en_defaut(tmp_path, cid, dict(c.MODELES[l], max_relance=131072)) is False
    assert c.reglage_en_defaut(tmp_path, c.id_cellule("E1-T2", l), c.MODELES[l]) is False  # cellule jamais lancée
```

### CO-2. Aucun repli sur la clé par défaut, même sans nom dans la composition (code)

Dans `appeler_openai`, remplacer les deux lignes `nom_cle = m.get("nom_cle") or NOMS_CLES["openai"]  # v9-v5` et `cle = os.environ.get(nom_cle)` par :

```python
    nom_cle = m.get("nom_cle")  # v9-v6 : le nom vient de la composition ; jamais de repli sur la clé par défaut
    if not nom_cle:
        return Reponse(echec="nom de la variable de la clé d'OpenAI absent de la composition (--cle-openai)")
    cle = os.environ.get(nom_cle)
```

Dans `compter_openai`, remplacer les deux mêmes lignes par :

```python
    nom_cle = m.get("nom_cle")  # v9-v6 : le nom vient de la composition ; jamais de repli sur la clé par défaut
    if not nom_cle:
        raise RefusCompte("COMPTE_IMPOSSIBLE", "nom de la variable de la clé d'OpenAI absent de la composition "
                                               "(--cle-openai)")
    cle = os.environ.get(nom_cle)
```

Essai à ajouter :

```python
def test_v6_cle_openai_sans_nom_dans_la_composition_aucun_repli(c):
    c.fixer_composition(["astra", "kimi"], nom_cle_openai="OPENAI_API_KEY_2")
    m = dict(c.MODELES[lettre_de(c, "astra")], nom_cle=None)  # OPENAI_API_KEY est présente : elle n'est pas lue
    c.TRANSPORT = FauxTransport()
    rep = c.appeler_openai(m, SAIN, 100)
    assert rep.echec and "absent de la composition" in rep.echec and c.TRANSPORT.appels == []
    with pytest.raises(c.RefusCompte) as e:
        c.compter_openai(m, SAIN)
    assert e.value.motif == "COMPTE_IMPOSSIBLE" and c.TRANSPORT_COMPTE.appels == []
```

### CO-3. Essai témoin : une sortie vide dont la fin est « STOP » n'est pas le défaut de réglage (essai)

Ma mutation « code 9 étendu à toute sortie vide » n'est prise par aucun essai. Essai à ajouter (il la prend, pour Carbon et pour Neon) :

```python
@pytest.mark.parametrize("espece", ["carbon", "neon"])
def test_v6_sortie_vide_fin_stop_relancee_comme_la_v3(c, tmp_path, espece):
    modele = c.CATALOGUE[espece]["id"]
    c.TRANSPORT = FauxTransport(flux_gemini(texte="", modele=modele, fin="STOP", candidats=0, pensees=100),
                                flux_gemini(modele=modele))
    assert executer(c, tmp_path, espece) == "OK"
    assert [e["statut"] for e in journal(c, tmp_path)] == ["VIDE", "OK"] and len(c.TRANSPORT.appels) == 2
```

### CO-4. Rapport : deux phrases à corriger, par erratum (texte)

Fichier neuf, `rapport-collisionneur-v9-v5-et-consultation-v5-v1-erratum-1.md`, même dossier. Texte :

```
# Erratum 1 du rapport « collisionneur v9 v5 et consultation v5 »

Cet erratum prime sur la section 0, point 1, dernier alinéa, et sur la section 2, « Il n'y a aucune relance au même réglage ».

- Section 0. La provision de 32 768 de la base version 3 est le réglage sous lequel la critique de Carbon du tour 2 a été arrêtée le 20 novembre, payée et sans cellule (39 953 jetons de pensées, garde de réflexion, code 6). La version 4 répondait à la demande du directeur de donner plus de provision à Carbon et à Argon ; ses provisions tiennent aussi la règle du plafond large (65 536 − 49 152 = 16 384 jetons de texte). Le choix de la base revient à la mère, sur la contre-lecture (section 7).
- Section 2. « Aucune relance au même réglage » vaut dans une commande. Dans la version 5, relancer la même commande renvoie la cellule au même plafond et au même budget. La version corrigée ne la renvoie plus (contre-lecture, CO-1).
```

## Remarques (non bloquantes)

1. **La variable d'un autre fournisseur peut être nommée.** `--cle-openai GEMINI_API_KEY` passe le contrôle du nom : la clé de Google partirait vers OpenAI (sonde, dans les deux scripts). Durcissement conseillé, à joindre à la version corrigée du collisionneur, dans `fixer_composition`, après la boucle de contrôle des noms :
   ```python
       if nom_cle_openai in {NOMS_CLES["gemini"], "TYPESAFE_API_KEY", nom_cle_anthropic, nom_espace_anthropic}:  # v9-v6
           raise Arret(CODE_USAGE, "--cle-openai nomme la variable d'un autre fournisseur : une clé ne part jamais vers "
                                   "un tiers")
   ```
   Éprouvé sur copie avec un essai à trois noms ; aucun essai existant ne casse. Même idée pour la consultation : refuser `--cle-openai GEMINI_API_KEY`.
2. **Consultation : `--reflexion 0` est accepté pour Carbon et Neon**, alors que le collisionneur refuse une provision nulle chez ces espèces. Le plafond envoyé vaut alors le seul texte ; si le modèle réfléchit quand même, la règle est rompue. À aligner dans une prochaine version : dans `reglage_depuis`, `if espece in REGLE_PLAFOND_LARGE and reflexion <= 0: raise ValueError(...)`. D'ici là : ne pas passer `--reflexion 0` à Carbon ni à Neon.
3. **Consultation, défaut de Carbon (24 000 + 16 000).** Le budget est souple : avec le dépassement de 22 % relevé, il resterait environ 10 700 jetons de texte. Pour un appel à Carbon, préférer `--reflexion 32768 --texte 32768` (pire cas 1,97 USD, sous le plafond de 4).
4. **La page de prix versée donne aussi Argon et Carbon** : 2 et 10 USD jusqu'au 30 novembre, 4 et 20 à partir du 1er décembre. Le prix de Carbon de la table (4 et 20, « rapporté ») a maintenant une source versée. Argon est toujours compté à 10 et 50 : le compter à 4 et 20 diviserait son pire cas par 2,5. Changement de table, donc version et décision à part.
5. **Les essais de la consultation écrivent dans le dossier temporaire du système**, pas dans celui donné à pytest. Ma première relance y a laissé une vingtaine de petits dossiers `essai-v5-…` (clés factices seulement) ; je ne les ai pas supprimés. Poser `TMPDIR` avant de les lancer.
6. **Les deux pages versées sont le texte balisé que Google sert aux agents**, pas la page vue par un lecteur. Les prix et les limites y sont lisibles sans ambiguïté.
7. **Aucun essai de la consultation ne joue le refus du budget par Google chez Neon.** Ma sonde le tient (code 1, coût 0, un seul essai, aucun renvoi). Un essai de plus serait bienvenu, sans urgence.

## Avant tout appel

1. Les corrections CO-1 à CO-4 sont faites, puis vérifiées par moi (même contre-lecteur).
2. L'envoi d'essai à Neon par la consultation version 5 est fait et lu (réserve 1).
3. La mère tranche le point 7 : base version 3, provisions de la version 4, ou budget et seuil séparés.
4. La commande de lancement est écrite, versée et contre-lue ; le devis donne le pire cas avec relance pour Carbon et Neon.

## Limites

- Aucun appel réel : le comportement de Google devant un budget de réflexion chez Neon n'est connu que par la documentation.
- Je n'ai pas relu les pages de Google sur le réseau ; je m'appuie sur les deux pages versées et, pour Carbon, sur les extraits cités par le rapport de la version 4.
- Mes outils sont dans mon bloc-notes, qui n'est pas durable : `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/outils/mutations_contre_lecture.py`, `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/outils/corrections_proposees.py`, `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/outils/test_corrections_proposees.py`, et les sondes sous `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/mut/K0/docs/notes/collisionneur-v9/test_sondes_contre_lecture.py`.

# Contre-lecture du collisionneur v9, version 3

Écrite le 20 novembre 2026 par un contre-lecteur neuf, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le développeur (Claude Opus 5.5, selon son rapport). Pièce de classe B (instrument), sous l'accord GO-2026-11-20-54. Aucun appel à un fournisseur, pas même un comptage. Aucune valeur de clé lue. Aucune dépense, aucun commit, aucun fichier du dépôt modifié hors cette pièce et son sceau.

## Verdict

**Conforme après corrections.**

Le script `collisionneur_v9_v3.py` fait ce que l'accord demande et ce que son rapport dit : je ne demande aucun changement de son texte avant la reprise. Les corrections portent sur la commande de reprise (trois, dont deux qui l'empêchent de marcher telle quelle) et sur les essais (quatre artefacts manquants, règle R5). Aucun appel avant C1, C2, C3 et C4.

Pièces relues, empreintes recalculées et égales aux compagnons :

| fichier | empreinte |
|---|---|
| `collisionneur_v9_v3.py` | `850df311807384fc66c44f6a6b90d3c8a9a3288d2b88a2b74312f9a78c4d4910` |
| `test_collisionneur_v9_v3.py` | `8c38dc2f938db3386f84721830b179d844295a1f46e6db8ba3586ffbe2eabfdc` |
| `rapport-developpeur-collisionneur-v9-v3.md` | `99bd3d48e3c53aaed4eedb638e782a9d5d5df3db25912702eff9e48be18e8648` |
| `commande-reprise-collisionneur-dopamine-v3.txt` | `336744af2c98f9bab543548ff8a27a3826d99ea067458c5e5efc72dff7cc4cac` |

La version 2 est intacte (sceaux du script et des essais vérifiés).

## Corrections

### C1. Commande : le nom de la variable de la clé d'Anthropic (bloquante)

Raison. `NOM_CLE` n'existe pas dans l'environnement : la commande s'arrêterait au code 1 (« clés absentes »), sans rien envoyer. Présence contrôlée par `[ -n "${VAR:-}" ]`, noms seulement : `ANTHROPIC_API_KEY` est **absente** ; sont présentes `RR_ANTHROPIC_API_KEY`, `RR_ANTHROPIC_API_KEY_2`, `RR_ANTHROPIC_API_KEY_3`, `RR_ANTHROPIC_API_KEY_LUC`, `RR_ANTHROPIC_API_KEY_RIGAUD`, ainsi que `GEMINI_API_KEY` et `OPENAI_API_KEY`. Le lancement du 20 novembre à 12:24Z a employé `RR_ANTHROPIC_API_KEY_RIGAUD` (`registres/decisions.md`, R-4257 ; `registres/depenses.md`, ligne 551). C'est elle qui convient.

Ancien (étape 3) :
```
--cle-anthropic NOM_CLE --sortie
```
Neuf :
```
--cle-anthropic RR_ANTHROPIC_API_KEY_RIGAUD --sortie
```
Le commentaire de tête sur `NOM_CLE` (lignes 4 à 6) devient : `# Clé d'Anthropic lue par son nom, RR_ANTHROPIC_API_KEY_RIGAUD, celle du lancement v9-v2 du 20 novembre à 12:24Z (R-4257). Si ce lancement donnait --nom-espace-anthropic, le redonner à l'étape 3, tel quel. Les cinq options d'espèces sont celles d'especes.json.`

Deux points que je ne peux pas trancher, à la charge de la mère :
- **Crédit de la clé.** Au pire, la part d'Anthropic de la reprise est de **10,32 USD** (Fable 2,9867 + 5,0408 ; Opus 0,6497 + 1,6449), contre « au plus ≈ 5 USD » notés en R-4257 pour la version 2. Crédit à relire avant l'étape 3. Un crédit épuisé en cours de route donne un refus avant traitement (statut `ECHEC`, coût 0, code 5) : rien n'est perdu, mais le passage s'arrête.
- **Espace de travail.** La variable par défaut, `ANTHROPIC_WORKSPACE_ID`, est absente ; `RR_ANTHROPIC_WORKSPACE_ID` est présente. Le journal ne dit pas si le lancement de 12:24Z donnait `--nom-espace-anthropic`.

### C2. Commande : le contrôle de l'empreinte du script échoue depuis la racine, et rien ne s'arrête (bloquante)

Raison. Le compagnon nomme le fichier sans chemin. Rejoué depuis la racine du dépôt : `collisionneur_v9_v3.py: FAILED open or read`, code 1. Les étapes suivantes partiraient quand même : le contrôle ne garde rien.

Ancien :
```
sha256sum -c docs/notes/collisionneur-v9/collisionneur_v9_v3.py.sha256
```
Neuf :
```
# Attendu : « OK 850df3118073… ». Tout autre résultat : ne rien lancer.
PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier docs/notes/collisionneur-v9/collisionneur_v9_v3.py
```
(Rejoué : `OK 850df3118073…`, code 0.)

### C3. Commande : ne pas relancer l'étape 3 après un refus tombé sur une relance (bloquante, sans changement du script)

Raison. `executer_cellule` (l. 1302) recommence toujours par le plafond de première passe. Si une cellule est coupée (`TRONQUE`) puis que sa relance est refusée par la ligne ou le plafond, un second lancement de l'étape 3 **repaie la première passe**, qui sera coupée de nouveau, puis bute sur le même refus. Démontré sur une copie du run réel (scénario « tout au pire ») : au second lancement, `E3-T3-reponse-B` essai 2, 22 000 jetons, `TRONQUE`, 0,67 USD payés pour rien ; avec Fable, ce serait jusqu'à 3,03 USD. Ce défaut vient de la version 2 ; la ligne de la version 3 le rend plus probable.

Ajout à la commande, après l'étape 3 :
```
# Si l'étape 3 s'arrête au code 4 (PLAFOND ou LIGNE) alors que le dernier essai de la cellule nommée est TRONQUE ou VIDE :
# NE PAS relancer l'étape 3 (la première passe serait repayée et coupée de nouveau). Passer à l'étape 4, puis à l'arbitre.
```

Pour une version suivante du script (non exigé pour cette reprise ; appliqué sur une copie : les 151 essais passent, et le second lancement du même scénario ne fait plus aucun envoi) :

Ancien (l. 1301-1302) :
```python
    statut = None
    for max_tokens in (m["max"], m["max_relance"]):
```
Neuf :
```python
    statut = None
    passes = (m["max"], m["max_relance"])
    dernier = (essais_journal(dossier, cid) or [{}])[-1]
    if dernier.get("statut") in ("VIDE", "TRONQUE") and dernier.get("max_tokens", 0) >= m["max"]:
        passes = (m["max_relance"],)  # sortie déjà vide ou coupée à ce plafond : la première passe n'est pas repayée
    for max_tokens in passes:
```

### C4. Essais : quatre artefacts manquent (règle R5, bloquante, sans changement du script)

Raison. Quatre de mes dix épreuves par retrait laissent les 151 essais passer :

| retrait | essais en échec |
|---|---|
| comptage d'OpenAI envoyé à une adresse tierce (la clé partirait chez un tiers) | **0** |
| changement de script déclaré depuis une autre empreinte que celle du run, admis par `suivre_scripts` | **0** |
| ligne non contrôlée à la relance | **0** |
| plafond non contrôlé à la relance | **0** |

Le script est juste sur ces quatre points (lu : l. 1152-1154, 1228-1230, 1305-1312) ; ce sont les essais qui ne les tiennent pas. Fichier neuf à ajouter, `test_collisionneur_v9_v3_complement_1.py`, même dossier (ancien : néant). Sur le script scellé : **6 passés**. Sur chacun des quatre retraits : en échec (3, 1, 1 et 1). Empreinte de ma copie, si le texte est repris à l'octet : `58ddaa24acd62b7ce638cbfa058ce53d2423a4640c03b5b6aea2f137b4824534`.

```python
"""Complément 1 des essais du collisionneur v9-v3 (demandé par la contre-lecture contre-lecture-collisionneur-v9-v3-v1.md) :
quatre artefacts qui manquaient, chacun avec son cas sain (R5). Hors réseau, mêmes doublures que test_collisionneur_v9_v3.py.
Le script collisionneur_v9_v3.py (850df311…) n'est pas changé.

Lancement : PYTHONPATH=src .venv/bin/python -B -m pytest -q docs/notes/collisionneur-v9/test_collisionneur_v9_v3_complement_1.py
"""
import pytest

from test_collisionneur_v9_v3 import (SAIN, FauxTransport, c, cree_openai, executer, final_openai,  # noqa: F401
                                      flux_anthropic)


@pytest.mark.parametrize("adresse", ["https://tiers.exemple/v1", "http://127.0.0.1:1@tiers.exemple/v1"])
def test_complement_artefact_comptage_openai_vers_un_tiers_refuse_sans_appel(c, tmp_path, monkeypatch, adresse):
    """La clé d'OpenAI ne part jamais vers un tiers, pas même pour un comptage."""
    monkeypatch.setenv("OPENAI_BASE_URL", adresse)
    c.TRANSPORT = FauxTransport()
    with pytest.raises(c.Arret) as e:
        executer(c, tmp_path, "astra")
    assert e.value.code == c.CODE_COMPTE and "COMPTE_IMPOSSIBLE" in str(e.value)
    assert c.TRANSPORT_COMPTE.appels == [] and c.TRANSPORT.appels == []


def test_complement_sain_comptage_openai_par_la_boucle_locale(c, tmp_path, monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "http://127.0.0.1:8123/v1")
    c.TRANSPORT = FauxTransport(cree_openai(), final_openai())
    assert executer(c, tmp_path, "astra") == "OK"
    a = c.TRANSPORT_COMPTE.appels[0]
    assert a["url"] == "http://127.0.0.1:8123/v1/responses/input_tokens" and a["locale"] is True


def test_complement_suivre_scripts_sain_et_artefact(c):
    essai = lambda h, n: {"cellule": "X", "essai": n, "sha256_script": h}  # noqa: E731
    sain = [essai("a", 1), {"changement_script": {"de": "a", "vers": "b"}}, essai("b", 2)]
    assert c.suivre_scripts(sain) == ("b", [])
    artefact = [essai("a", 1), {"changement_script": {"de": "z", "vers": "b"}}, essai("b", 2)]  # déclaré depuis un autre
    courant, problemes = c.suivre_scripts(artefact)
    assert courant == "b" and len(problemes) == 1 and "déclaré depuis z" in problemes[0]


@pytest.mark.parametrize("garde", ["LIGNE", "PLAFOND"])
def test_complement_relance_refusee_avant_l_envoi_par_la_ligne_ou_le_plafond(c, tmp_path, garde):
    """Première passe coupée (2,451 USD), relance au pire à 3,2165 USD : 5,6675 USD. Une ligne ou un plafond de 5 USD
    refuse la relance avant l'envoi ; à 6 USD, la relance part."""
    c.fixer_composition(["fable", "kimi"], nom_cle_anthropic="MA_CLE")
    coupe = lambda: flux_anthropic(fin="max_tokens", sortie=c.MAX_FABLE_V3, texte="Texte coupé")  # noqa: E731

    def lancer(dossier, montant, *flux):
        dossier.mkdir()
        if garde == "LIGNE":
            c.ouvrir_ligne(dossier, montant)
        c.TRANSPORT = FauxTransport(*flux)
        return c.executer_cellule(dossier, "E1-T1", "A", SAIN, [], montant if garde == "PLAFOND" else 100.0, c.APPELANTS)

    with pytest.raises(c.Arret) as e:  # artefact
        lancer(tmp_path / "artefact", 5.0, coupe())
    assert e.value.code == c.CODE_PLAFOND and garde in str(e.value) and len(c.TRANSPORT.appels) == 1
    assert [x["motif"] for x in c.lire_journal(tmp_path / "artefact") if "refus_avant_envoi" in x] == [garde]
    assert [x["statut"] for x in c.essais_journal(tmp_path / "artefact")] == ["TRONQUE"]
    assert lancer(tmp_path / "sain", 6.0, coupe(), flux_anthropic()) == "OK"  # sain
    assert [a["corps"]["max_tokens"] for a in c.TRANSPORT.appels] == [c.MAX_FABLE_V3, 64000]
```

### C5. Rapport : une phrase périmée (erratum, non bloquante)

« Fichiers exclus de git […] `.git/info/exclude` contient `docs/notes/collisionneur-v9/*v3*` » n'est plus vrai : l'exclusion n'y est plus, et les quatre pièces sont dans le commit `419719254`.

## Constats, dans l'ordre des six questions

### 1. Comptage avant l'envoi

- **Ordre.** `executer_cellule` : garde de motifs, puis comptage (l. 1297-1300), puis, à chaque passe, plafond (l. 1305), ligne (l. 1308), et seulement alors écriture du prompt et envoi. Un comptage par cellule, repris pour la relance. Essai rejoué : le comptage précède l'envoi chez les cinq espèces du run.
- **Interfaces, lues contre la documentation.** Anthropic : `POST /v1/messages/count_tokens`, `model` et `messages` identiques à l'envoi, mêmes en-têtes, réponse `input_tokens` (conforme à la référence « Token counting »). Google : `POST …/models/{modèle}:countTokens`, mêmes `contents`, réponse `totalTokens`. OpenAI : `POST /v1/responses/input_tokens`, `model` et `input` identiques, réponse `input_tokens`, même restriction d'adresse que l'envoi. Mon retrait « comptage d'Anthropic sur un autre modèle » casse un essai.
- **Refus avant l'envoi, sans repli.** Clé absente, erreur 4xx ou 5xx, connexion, délai, réponse mal formée : `COMPTE_IMPOSSIBLE`, code 8. Compte sous un jeton pour 8 caractères : `COMPTE_INVRAISEMBLABLE`, code 8. Plafond et ligne : code 4. Chaque refus est écrit au journal, aucun fichier d'essai n'est créé. Mon retrait « repli silencieux sur l'estimation quand le comptage échoue » casse 18 essais.
- **Limite.** Aucune des trois interfaces n'a été appelée pour de vrai : le premier appel réel sera l'épreuve. S'il échoue, code 8, rien n'est envoyé, et les cellules déjà valides restent acquises.
- **Remarque.** `compter_entree` passe à l'estimation pour tout fournisseur sans compteur, et non pour Kimi seul. Le catalogue est fermé ; à resserrer dans une version suivante.

**La tolérance de 1 % plus 32 jetons : acceptable, à garder, à déclarer à Lazar comme écart à la lettre de « compter exactement ».**
- Elle ne peut pas faire dépasser : le pire cas d'avant l'envoi est calculé sur la garde, tolérance comprise (mon retrait « pire cas sur le compte nu » casse 6 essais).
- Sans elle, un seul jeton facturé au-dessus du compte arrête le passage **après paiement** : c'est l'incident du 20 novembre, rejoué. Or Anthropic écrit que son compte est une estimation, et les deux autres ne promettent rien.
- Simulé sur une copie du run : entrée facturée à 0,9 % au-dessus du compte, les dix cellules passent ; à 2 %, arrêt `ENTREE_HORS_GARDE` après 0,94 USD, réponse gardée dans `essais/`.
- Son prix au devis : 0,13 USD (25,7746 contre 25,6469 sans elle), soit 1 000 jetons de plafond de Fable.

### 2. Pire cas des tours 2 et 3

**Recalculé par mon programme : 8,6061 + 17,1685 = 25,7746 USD, à l'identique, ligne par ligne.** Fable à 48 000 : 25,6321 ; à 50 000 : 25,9170 (dépasse). 49 000 est bien le plus grand multiple de 1 000 qui tient. Mon programme ne reprend du script que la construction du prompt et la table des prix ; la construction est validée : le prompt reconstruit de la cellule arrêtée est égal, à l'octet, à celui envoyé le 20 novembre (106 207 caractères).

Hypothèses :
- **2 caractères par jeton d'entrée : tient sur les relevés du run**, avec peu de marge chez Anthropic. Relevés : 2,227 et 2,587 (Fable, Opus), 3,685 (Google), 3,875 (OpenAI). À 1,8, le total passerait à 27,18 USD. Si l'hypothèse casse, la conséquence est un refus `LIGNE` avant l'envoi, jamais un dépassement.
- **Critiques du tour 3 bornées par le plafond de sortie de leur auteur : tient**, et très largement. Marge la plus faible : Astra, 4,10 caractères par jeton de sortie relevés contre 4,5 supposés. La borne ne vaut plus si une critique sort d'une relance, mais le compte réel remplace alors la projection.
- **Ordre de grandeur réel.** Avec des critiques de 25 000 à 60 000 caractères, le pire des deux tours est de 17,3 à 19,7 USD. Simulation à sorties pleines sans coupure : 16,09 USD sur la ligne.

**Opus à 22 000 jetons : oui, il peut être coupé au tour 2.** Au tour 1, il a employé 17 397 jetons sur 22 000 pour un prompt de 13 600 caractères ; au tour 2, le prompt en fait 103 753, et Fable y a épuisé 22 000 jetons avec la moitié seulement en texte. Une coupure ne ferme pas le tour : la relance à 64 000 part (pire 1,49 USD, simulée) et tient dans la ligne à ce moment. Elle coûte la première passe (0,65 USD au plus) et rogne la marge du tour 3 : au pire de tout, 25,77 + 1,49 dépasse 25,90, et la dernière cellule du tour 3 serait refusée avant l'envoi. Relever Opus seul ne tient pas (24 000 : 25,96). Un échange tient, par exemple Fable 40 000 et Opus 36 000 (25,77), mais c'est un autre réglage que celui de l'accord : à la mère et à Lazar d'en décider. Je recommande de garder la table.

### 3. Reprise

Simulée sur une copie du run réel, avec les arguments de la commande et des doublures par adresse :
- sans `--reprise` : code 1, aucun comptage, aucun envoi (seul `etat.md`, dérivé, est régénéré) ;
- avec `--reprise` : 10 comptages, 10 envois, aucun au tour 1 ; l'essai 1 de la cellule arrêtée intact, l'essai 2 ajouté à 49 000 ; tous les fichiers d'avant inchangés, l'ancien journal est le préfixe exact du neuf ;
- journal : `changement_script` de `2357b9e8…` vers `850df311…`, puis `ligne_ouverte` à 25,90 USD avec 4,0961 USD de dépense d'avant ; 4,0961 + 25,90 = 29,9961, sous le plafond de 30 ;
- `verifier` : aucun problème ; un second lancement après la fin : aucun comptage, aucun envoi.

Mon retrait « reprise admise sans l'option » casse un essai.

### 4. Commande de reprise

Voir C1, C2 et C3. Le reste est juste : `GO_ID=GO-2026-11-20-54`, options d'espèces égales à `especes.json`, plafond 30, ligne 25,90, `--reprise`, vérification avant et après.

### 5. Gardes neuves et règle R5

- Suite v3 rejouée : **151 passés**. Suite v2 sur la v2 : **117 passés**.
- Dix épreuves par retrait, sur des copies dans mon bloc-notes. Six cassent au moins un essai (pire cas sur le compte nu : 6 ; ligne comptant la dépense d'avant : 2 ; autre montant de ligne admis : 1 ; repli silencieux : 18 ; comptage sur un autre modèle : 1 ; reprise sans l'option : 1). Quatre n'en cassent aucun : voir C4.
- Hors C4, chaque garde neuve a son cas sain et son artefact.

### 6. Autres défauts qui feraient payer sans résultat, ou dépasser

- **Relance repayée au second lancement** : C3.
- **Les relances ne sont pas réservées.** Simulation « tout coupé, tout au pire » : arrêt net au plafond à `E3-T3-reponse-B`, 28,80 USD au total, 24,71 sur la ligne. Ni la ligne ni le plafond ne sont dépassés, mais le tour 3 reste inachevé après paiement.
- **La ligne ne se relève pas.** Un autre montant est refusé, et la ligne s'applique même sans l'option. Un supplément accordé par Lazar demanderait un autre dossier ou une autre version.
- **Astra : le coût inscrit peut dépasser le pire cas.** Le script ajoute les jetons de raisonnement à la sortie, qui les contient déjà (prudence héritée). Le livre peut donc montrer plus que le pire cas d'un envoi d'Astra (jusqu'à 0,40 USD de plus en première passe), sans dépense réelle en plus. Au tour 1, raisonnement nul.
- **Après coup seulement** (hérités, arrêt après paiement) : réflexion de Google au-delà de la provision, écart de total, entrée au-delà de la garde.
- **Garde de motifs au tour 3** : une critique qui contiendrait un motif interdit arrête le tour 3 au code 7, après le tour 2 payé (déjà au rapport).

## Limites

Aucun appel réel. Les prix sont ceux de la table du script, non revérifiés. Le crédit des clés n'est pas connu de moi. Mes programmes (`pire.py`, `simul.py`, `retraits.py`, et le fichier d'essais de C4) sont dans mon bloc-notes, `/tmp/claude-0/-home-user-controle-ia-travail/fc9e4fb9-7931-58b9-a66b-caf66718eee3/scratchpad/outils/`, qui n'est pas durable : le texte de C4 est donc donné ici en entier.

# Contrôle du mandataire avant le geste 9 — rapport v1

Développeur du contrôle du mandataire, modèle O. 2026-11-21. Classe B. Exigé par l'additif 6 v2 de l'étage 2, § 9, et par la décision R-4325.

## Verdict

Programme écrit, 36 essais passés, passe réelle sur ce conteneur : **tenu, code 0**. Un écart au brief, voulu : une plage CIDR qui contient 127.0.0.1 ne suffit pas seule (voir § 2).

## 1. Sources lues

- Additif 6 v2, § 9, lignes 287 à 323 : `/home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/additif-6-code-etage-2-preenregistrement-ligne-3-v2.md`, empreinte recalculée `e2afc7b987ab64dfc270c6c20d49ef5e0d8eaf603ffb2f647a0ea0dee6ca4f01`, **égale** à l'empreinte attendue.
- Code d'appel v4, `…/code-appel-v4/epreuve_juges_reels_ligne_3_v4.py` (empreinte non fournie, non vérifiée), par `grep -n` :
  - l. 159 à 163 : `VARIABLES_PERMISES` contient `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY` et leurs trois formes en minuscules ;
  - l. 164 : `VARIABLES_EXIGEES = ("HTTPS_PROXY",)`, nom en majuscules ;
  - l. 1308 à 1310 (`exiger_environnement_epure`) : seule la **présence** de `HTTPS_PROXY` est contrôlée, pas sa non-vacuité ; aucune lecture de `NO_PROXY`.
  Ce contrôle comble donc les deux trous que nomme le § 9 (non-vacuité, couverture de 127.0.0.1) sans contredire le code d'appel.
- Bibliothèque standard de `/usr/local/bin/python3` (Python 3.13.18, interpréteur de la porte de plafond, qui n'emploie que la bibliothèque standard, § 9) : `/usr/local/lib/python3.13/urllib/request.py`, `getproxies_environment` (l. 2518 à 2553) et `proxy_bypass_environment` (l. 2555 à 2587).

## 2. Règle retenue

### (1) HTTPS_PROXY
- `HTTPS_PROXY` (majuscules, le nom qu'exige le code d'appel) présente et non vide après `strip()`.
- `https_proxy` (minuscules) **seule ne suffit pas** : le code d'appel exige le nom en majuscules.
- Si `https_proxy` est présente aussi, elle doit être non vide et égale à `HTTPS_PROXY` (comparées après `strip()`, jamais imprimées). Raison : urllib préfère la minuscule (deuxième passe, l. 2546 à 2552) et une minuscule vide **retire** le mandataire. Sinon urllib utiliserait un autre mandataire que celui contrôlé, ou aucun.

### (2) NO_PROXY couvre 127.0.0.1
Il faut remplir **deux conditions à la fois** :
- **(a) règle du brief** : après découpage sur les virgules et `strip()` de chaque élément, un élément vaut `127.0.0.1`, ou est une plage IPv4 qui contient 127.0.0.1 (`ipaddress.ip_network(…, strict=False)`), ou vaut `*` ;
- **(b) règle d'urllib** : `urllib.request.proxy_bypass_environment(h, {"no": valeur})` est vrai pour les trois hôtes `127.0.0.1`, `127.0.0.1:8787` et `127.0.0.1:8788`. On utilise l'urllib de l'interpréteur qui exécute le contrôle.

Pourquoi deux conditions : sous Python 3.13, urllib **ne lit pas les plages CIDR**. Il compare seulement des chaînes et des suffixes de nom (l. 2576 à 2585). Il ne prend `*` que si c'est la valeur entière exacte (l. 2570 : `no_proxy == '*'`, sans retirer les espaces). La porte de plafond est lancée par le code d'appel et n'utilise que la bibliothèque standard. Avec la règle (a) seule, `NO_PROXY=127.0.0.0/8` serait déclaré « tenu », alors que la porte enverrait 127.0.0.1 au mandataire. C'est précisément le faux « tenu » que ce contrôle doit empêcher. Concrètement :
- tenu : un élément `127.0.0.1` (espaces tolérés), ou la valeur entière exactement `*` ;
- refus : une plage seule, même si elle couvre (le motif imprime la plage, réécrite par `ipaddress`) ; `*` dans une liste ou entouré d'espaces ; un suffixe que seul urllib accepte (`0.0.1`, `.0.0.1`) ; `127.0.0.1:8787` ; `localhost` seul, car urllib compare des chaînes et le nom n'est pas l'adresse.

**Formes en minuscules** : **chaque forme présente** (`NO_PROXY`, `no_proxy`) doit couvrir 127.0.0.1 à elle seule. Si aucune n'est présente, c'est un refus. Raison : urllib préfère la minuscule, et une minuscule vide efface la majuscule ; d'autres clients préfèrent la majuscule. Exiger chacune des deux couvre tous les cas.

### Sortie
- Une ligne JSON avec quatre clés : `https_proxy_non_vide`, `no_proxy_couvre_127_0_0_1`, `decision` (`tenu` ou `refus`), `motifs`.
- `motifs` porte les constats, ceux du refus comme ceux de la tenue.
- La valeur de `HTTPS_PROXY` n'est jamais imprimée. De `NO_PROXY`, le programme n'imprime que l'élément qui couvre : `127.0.0.1`, `*`, ou une plage réécrite par `ipaddress`. Aucun autre élément.
- Codes de sortie : 0 si tenu, 3 si refus. Une erreur interne donne aussi un refus, code 3 : le motif ne porte que le nom du type d'exception, sans repli silencieux (R5).

## 3. Essais

- `essais_controler_mandataire_etage_2_v1.py`, lancés par `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider …` (Python 3.13.18, même version que la porte).
- Résultat : **36 passed**.
- Couverture : un cas sain.
- Artefacts sur `HTTPS_PROXY` : absente, vide, espaces seuls, blancs mélangés, minuscule seule, minuscule vide, minuscule différente ; minuscule identique tenue.
- Artefacts sur `NO_PROXY` : absente, vide, espaces seuls, virgules seules, sans 127.0.0.1, `localhost` seul ; espaces autour tenus.
- Plages : une plage qui couvre (reconnue par (a), refusée par (b)) ; plage plus élément exact (tenu) ; une plage qui ne couvre pas.
- `*` : valeur entière (tenu), dans une liste (refus), entouré d'espaces (refus).
- Autres artefacts : suffixe lu par urllib hors de la règle, élément avec port.
- Formes en minuscules : `no_proxy` seule qui couvre et qui ne couvre pas ; deux formes dont la minuscule est vide ; deux formes dont la majuscule ne couvre pas ; deux formes qui couvrent.
- Absence de fuite :
  - dans le processus : trois cas avec une valeur secrète (identifiant, mot de passe, hôte) ; l'hôte figure aussi dans `NO_PROXY` ;
  - en sous-processus `-I -B` : code 0 sur un cas tenu, code 3 sur un refus, code 3 sur un environnement vide, une seule ligne JSON ;
  - erreur interne : refus, code 3, sans fuite du message d'exception.

## 4. Passe réelle sur ce conteneur

Commande : `/usr/local/bin/python3 -I -B …/controler_mandataire_etage_2_v1.py > …/passe-environnement-v1.txt`. **Code de sortie : 0.**

```
{"https_proxy_non_vide": true, "no_proxy_couvre_127_0_0_1": true, "decision": "tenu", "motifs": ["HTTPS_PROXY présente et non vide (valeur non imprimée)", "NO_PROXY couvre 127.0.0.1 par l'élément « 127.0.0.1 »", "no_proxy couvre 127.0.0.1 par l'élément « 127.0.0.1 »"]}
```

Les deux formes de `NO_PROXY` sont présentes et couvrent chacune 127.0.0.1. `https_proxy`, si elle est présente, est égale à `HTTPS_PROXY`.

Cette passe juge l'environnement de **cette** session. Elle ne juge pas celui de l'exécutant du geste 9.

## 5. Empreintes (fichiers jugés par ce rapport)

| fichier | sha256 |
|---|---|
| `controler_mandataire_etage_2_v1.py` | `60523f210e40c20709188f048a567a7eb14053b6e75ade9cdb919d7bbb04bd39` |
| `essais_controler_mandataire_etage_2_v1.py` | `0f32cf0fd8366ab48f1f220983c9c4ff01729d4d8930946d260bf6e3cfbc131e` |
| `passe-environnement-v1.txt` | `fea179797d41056e2cae6f44695b3d1393de8141eaa5cfdc556401b0105a0498` |

La table du dossier, `empreintes-controle-mandataire-v1.sha256`, et un compagnon `.sha256` par fichier accompagnent ce rapport.

## 6. Ce que je laisse ouvert

1. **Écart au brief, à trancher par la mère** : une plage CIDR qui contient 127.0.0.1 est refusée si elle est seule, parce qu'urllib ne la lit pas (§ 2). Pour la règle (a) seule, il suffit de retirer la condition (b) dans `_evaluer_no_proxy`. Je ne le recommande pas.
2. **Client du juge Opus** : le fournisseur `claude_sdk` de la déclaration atteint `http://127.0.0.1:8787` par un client qui n'est peut-être pas urllib. Un client fondé sur httpx préfère d'autres règles (`*` dans une liste, plages selon sa version). Je ne l'ai pas vérifié. La règle (b) est la plus étroite que je connaisse ; un élément exact `127.0.0.1` reste lu par tous les clients courants.
3. **Où le contrôle s'exécute** : le contrôle lit l'environnement de l'interpréteur qui le lance. Le mandat de lancement doit le lancer dans l'environnement que le geste 9 transmettra sous `env -i`, ou sur les mêmes noms. Il faut aussi y passer `NO_PROXY` et `no_proxy` : la commande des relais du § 9 ne cite que `NO_PROXY`.
4. Le code d'appel v4 n'a pas d'empreinte fournie : je ne l'ai pas vérifiée, j'ai lu ses lignes par `grep -n`.
5. Un client qui tiendrait compte de `HTTP_PROXY` pour `http://127.0.0.1` est hors du périmètre demandé. Il serait couvert par la même condition `NO_PROXY`, qui vaut pour tous les schémas.
6. **Contre-lecture** : à faire avec le mandat de lancement (§ 9) par un lecteur qui n'a pas écrit ce programme.

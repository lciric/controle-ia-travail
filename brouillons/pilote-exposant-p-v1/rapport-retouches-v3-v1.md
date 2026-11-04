# Rapport — retouches de code v3 du pilote de l'exposant p

Développeur neuf (sous-agent) : je n'ai écrit ni les brouillons, ni le code v1 et v2, ni les contre-lectures. Consigne : `brouillons/pilote-exposant-p-v1/consigne-developpeur-retouches-v3-v1.md` (`0846cae58e3e6cb54d4d0257486b0021b8b143a53fafb35d3ccbfdc01bc7056a`, vérifiée avant lecture). Travail du 4 novembre 2026, de 02:39 à 02:40 UTC (lecture), interrompu par la limite d'usage, repris de 05:22 à 05:53 UTC (`date -u`). Branche `canal/conv-audit-n04`, tête `8c5f7755`, arbre `/home/claude/controle-ia-travail`.

Références : contre-lecture R2 du brouillon 2 (`contre-lecture-v2/contre-lecture-pilote-exposant-p-v2.md`, `5e329a67351ac22b9872541f43d5b15c2e63680f8444dd30dc6afd7b8b36ce36`), ligne 188, points I1 et I3 ; couples 11, 17 et 18 (`couples-contre-lecture-pilote-exposant-p-v2.json`) ; brouillon 3 (`preregistrement-pilote-exposant-p-v1-brouillon3.md`, `d2dbfe77f16b3e1ce555494e9e6be57e349a70b5af7b9ab083b8c09125d17e6b`).

Respecté : aucun commit, aucun `.sha256`, aucun fichier existant modifié (seulement des fichiers neufs), rien sous `donnees/` ni `/home/claude/coffre-*`, aucun réseau, aucun modèle, aucune carte, aucune dépense ; toute commande sous `timeout 900 nice -n 10`.

## Les quatre retouches

| Retouche | Ce qui change | Où |
|---|---|---|
| `NE_MONTRE_PAS` (couple 17) | « E et R sont lues au dernier jeton de phrases courtes (E : seul le dernier mot change, un mot technique d'évaluation de modèle, étranger au contenu, contre un événement de vie appelé par le contenu ; R : le corps change, le dernier mot est commun) », mot pour mot du couple et du brouillon 3 (ligne 229). `PHRASES` = table v2 où l'ancienne borne est remplacée dans les trois issues tranchées seulement. Une borne absente ou mal placée arrête à l'import | `pilote_exposant_p_v3/analyse.py` |
| `QUALIF_JUMEAU["au-dessus du jumeau"]` (couple 18) | « l'écart est propre à la fin d'évaluation telle que construite, pas à un mot neutre de même nombre de jetons ; le jumeau ne contrôle ni le domaine technique des porteurs d'évaluation ni leur écart au contenu » ; les autres clés sont celles de la v2 | idem |
| Bloc 0 (I1, couple 11) | Avant tout passage avant, sur le tokeniseur du modèle lu, chargé une seule fois : pour chaque porteur (évaluation, déploiement, neutre retenu), dans les registres F et C, le nombre de jetons de la phrase, le nombre de jetons du porteur et le dernier sous-jeton. Résumé par rôle : nombre de derniers sous-jetons distincts, groupes de porteurs distincts qui partagent un dernier sous-jeton, dans un rôle et entre rôles. Consigné sous `sorties.porteurs_sous_jetons`, aussi en cas d'arrêt « instrument non validé ». Descriptif, sans seuil | `pilote_exposant_p_v3/run.py` (`sous_jetons_porteurs`, `Pilote`) |
| `go.py` (I3, R-389) | (1) La première ligne fixe le type, l'auteur et la période. (2) Toute autre ligne du même identifiant doit être une extension conforme, jugée comme dans la garde de `main` ; sinon refus « ligne en conflit ». (3) Plafond : celui de la dernière extension conforme qui donne un montant lisible, sinon celui de la première ligne. (4) Le périmètre de la première ligne doit nommer l'étude. (5) La révocation ne change pas. (6) Les doublons d'autres identifiants sont rapportés sans bloquer ; s'ils sont non conformes, ou si une ligne ou une date est illisible, le rapport dit en clair que « la garde de calcul de `main` bloquerait la création » | `pilote_exposant_p_v3/go.py` |

Ce qui n'a pas changé est importé de la v2 tel quel. `lire`, `analyser` et `principal` gardent le code de la v2 (`__code__` identique, vérifié par essai) ; ils sont seulement liés à l'analyse v3 et au `Pilote` v3. L'amorce appelle `go` v3 et le script d'instance appelle `run` v3 : d'où une amorce et un script d'instance v3. Ce sont les fichiers v2 à des substitutions près, déclarées et vérifiées par essai : noms de modules et de scripts, branche par défaut `…-v3`, fichier d'essais v3 ajouté, en-tête.

## Fichiers neufs (sha256)

| Fichier | sha256 |
|---|---|
| `src/controle_ia/pilote_exposant_p_v3/__init__.py` | `8fa7ae0478df09e40b4d41916c1c28bbf3be7feeaee020dc9e785c16b3d48557` |
| `src/controle_ia/pilote_exposant_p_v3/analyse.py` | `84e8b139370480d4396fa58ee8c6f1359a71bba859553a46be7a5a6ccbb0219a` |
| `src/controle_ia/pilote_exposant_p_v3/go.py` | `54e8fc44870a8facbdbdfa21d74629c2a25ceb63f195d9e93b9c7f8a791e1cf9` |
| `src/controle_ia/pilote_exposant_p_v3/run.py` | `fc787ff1623f6a897071b2db6597a9ad7e3230c18fc28d590db1a3aa515398f1` |
| `scripts/amorce_instance_pilote_exposant_p_v3.sh` | `681bee44138c266e094dc60265e2c9a1977f52e1ecac2227ed50816d829d7779` |
| `scripts/pilote_exposant_p_instance_v3.sh` | `abec9e3736678b70329b9627748fff1ca3c406685ba18c2a20d213b8c0016449` |
| `tests/test_pilote_exposant_p_v3.py` | `549aeecf4f3f3d19e70e706e0aaffc284d5c2997187dffef54e1e9732f6d7848` |

L'empreinte de ce rapport est donnée au coordinateur dans la réponse finale.

## Essais

Les 20 essais de `tests/test_pilote_exposant_p_v3.py` :
- **Couple 17** : correspondance mot pour mot avec le couple et le brouillon 3 ; artefact : le texte v2 est absent du brouillon 3 ; aucun autre changement dans les phrases ; une borne absente ou mal placée arrête à l'import.
- **Couple 18** : même vérification ; artefact : la v2 en dit trop.
- **Lecture** : `lire` v3 donne les phrases v3, `lire` v2 les phrases v2 (artefact), et la lecture est identique hors de la phrase ; vérification de la liaison des fonctions.
- **Sous-jetons, cas sain** : tokeniseur jouet, 30 derniers sous-jetons distincts, aucun partage.
- **Sous-jetons, artefact** : tokeniseur qui coupe aux traits d'union. Il rapporte les groupes {model-eval, eval, chatbot-eval, LLM-eval} et {benchmark, AI-benchmark}, ainsi qu'un partage entre rôles.
- **Lanceur v3 en jouet** : arrêt « instrument non validé », code 3, avec les sous-jetons consignés dans les sorties scellées.
- **Les quatre essais de I3** :
  - une extension conforme est acceptée (la v2 la refusait : « en double ») ;
  - une extension qui relève le plafond est lue (une extension qui le baisse aussi ; une extension pas encore en vigueur est ignorée) ;
  - une extension non conforme du GO cité est refusée : six cas, dont le type, l'échéance plus lointaine et le périmètre ;
  - un doublon non conforme d'un autre identifiant laisse le GO valide, avec l'avertissement.
- **Registre réel de `main`** (`/home/user/controle-ia-travail/registres/go.md`, à défaut `origin/main` ; ni l'un ni l'autre : échec, pas de saut) : GO-2026-11-04-03 est accepté (le 4 novembre, plafond 30 USD ≥ 17). Une extension légitime à 40 USD est acceptée ; une extension contradictoire (échéance au 31 décembre) est refusée ; la v2 refusait l'extension légitime.
- **Même verdict que la garde de `main`** (`.claude/hooks/garde_calcul.py`, importée depuis `main`) : sur le registre réel et sur trois variantes.
- **Scripts v3** : égaux aux v2 aux substitutions déclarées près ; l'étape « verifier » de l'amorce v3 rend 0 sur l'extension légitime et 1 sur l'extension contradictoire.
- **Bibliothèque standard** : `go` v3 s'importe sans numpy ni scipy.

Commande de la consigne, exécutée de 05:41:41 à 05:52:18 UTC, sur une machine chargée par d'autres sessions :

```
cd /home/claude/controle-ia-travail && PYTHONPATH=src timeout 900 nice -n 10 /home/user/controle-ia-travail/.venv/bin/python -I -B -m pytest -q -p no:cacheprovider tests/test_pilote_exposant_p_v2.py tests/test_script_pilote_exposant_p_v2.py tests/test_pilote_exposant_p_v3.py
........................................................................ [ 82%]
...............                                                          [100%]
87 passed in 634.96s (0:10:34)
```

87 = 67 (v2 et scripts v2, inchangés) + 20 (v3) ; aucun échec, aucun saut.

Pour les sept fichiers que la liste d'essais du script d'instance v3 fait tourner (v1, v2, script v2, v3, manifeste, scellement, préenregistrement), on compte 149 essais (`--collect-only`), soit 129 + 20.

## Empreintes que le préenregistrement et la configuration devront citer

**Préenregistrement** (la ligne « Critères gelés codés » et les lignes qui citent l'amorce et le script) :
- les critères gelés codés : `src/controle_ia/pilote_exposant_p_v3/analyse.py` — `84e8b139…219a`. Il importe `src/controle_ia/pilote_exposant_p_v2/analyse.py` — `e4c8a71a3e39a97d628b272d90861fee36724d642bc1e67e67a83cf3176856db`, inchangé, à citer aussi ;
- le lanceur : `src/controle_ia/pilote_exposant_p_v3/run.py` — `fc787ff1…98f1`. Il importe `src/controle_ia/pilote_exposant_p_v2/run.py` — `d766cadfe4f16bd0826341e53b1e51b3d20c109e4ed9643197a4424b5e3086a3`, inchangé ;
- les stimuli et leurs gardes : `src/controle_ia/pilote_exposant_p_v2/stimuli.py` — `6054866d9f8b26434c50704d69ba6b829a9ac9563f226a100aac6ae9c2b5493d`, inchangé ;
- la vérification du GO : `src/controle_ia/pilote_exposant_p_v3/go.py` — `54e8fc44…e1cf9`. Il importe `src/controle_ia/pilote_exposant_p_v2/go.py` — `d442bf0ad20bcee1b42428a20e3fcf087698f99a22237e95bf436b6475931145`, inchangé ;
- l'amorce et le script d'instance : `scripts/amorce_instance_pilote_exposant_p_v3.sh` — `681bee44…7779` ; `scripts/pilote_exposant_p_instance_v3.sh` — `abec9e37…6449`. Partout où le texte cite l'amorce ou le script v2, il faut écrire v3 : nœuds, table B6 et I7, liste d'arrêt ; branche de résultats par défaut `calcul/pilote-exposant-p-<MODE>-v3` ;
- « Tests attendus » : `149`, en ajoutant `tests/test_pilote_exposant_p_v3.py` — `549aeecf…7848` à la liste des fichiers.

**Configuration** : aucun champ de la configuration ne cite le code. Les constantes de lecture ne changent pas : `exiger_config` passe avec la v3, puisque toutes les constantes sont importées de la v2. Les empreintes qu'elle cite déjà restent justes : stimuli `9a32ca837ff115ba589585102a07f9b0413c6118a02ae51ff3a731fcb4329adf`, références, copie amont. La configuration v2 (`c5a63a90…50bd`) peut donc être gardée telle quelle. Si l'on en fait une v3, seuls `version` et `note` changent.

## Écarts et remarques

1. **Le run jouet complet ne figure pas dans les essais v3.** Je l'ai fait tourner une fois ici : 585,8 s sur la machine chargée, issue « au-dessus », phrase v3 et qualificatif v3 dans `lecture.json`, sous-jetons consignés. Avec le petit vocabulaire du jouet, 28 derniers sous-jetons distincts sur 30 porteurs d'évaluation, soit des collisions d'empreinte. Je l'ai retiré pour tenir le délai de 900 s de la commande ; l'arrêt code 3 garde le chemin de bout en bout, et l'essai de `lire` couvre la phrase.
2. **`go` v3 : deux choix qui ne sont pas dans I3.** Une extension datée après le jour de la vérification ne compte pas pour le plafond ; elle est consignée. Les dates illisibles des autres lignes sont signalées, parce que la garde de `main` les bloque. Une extension qui baisse le plafond est lue comme une autre, et peut donc faire refuser le GO.
3. **Les scripts v3 ne sont pas couverts par des essais complets en dépôt jetable** (ceux de la v2 ne sont pas dupliqués). Ils sont couverts par l'égalité aux scripts v2 aux substitutions près, et par l'exécution réelle de l'étape « verifier ».
4. **Non demandé, laissé tel quel** : `QUALIF_JUMEAU["indiscernable du jumeau"]` dit encore « n'importe quel dernier mot changé ferait de même ». C'est la même surinterprétation que le couple 18 corrige, puisque le jumeau n'apparie que le nombre de jetons. À trancher par le rédacteur.
5. **Lecture du registre réel** : l'essai lit `main` sur la machine de la session, et `origin/main` sur l'instance. Une révocation future de GO-2026-11-04-03 le ferait échouer, et c'est voulu.

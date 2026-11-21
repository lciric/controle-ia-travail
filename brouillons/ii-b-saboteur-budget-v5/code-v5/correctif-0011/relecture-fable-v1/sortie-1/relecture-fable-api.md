# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v2` (empreinte du module c8e8506f8d7cb9487173090aa9a000c1ab217377946f55cb338a45f07ca3d7f3)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChGqQ8VZLxQdLxGzVxpRj`
- Heure (UTC) : 2026-11-21T22:27:00Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle
- Entrées :
  - consigne : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/entrees/consigne-relecture-correctif-0011.md` — sha256 e661361ca27bc034c528cfe50bb4f26343451cebd3c9246096373bbb39e6f4ff (compagnon : vérifié)
  - correction : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/entrees/correctif-0011.patch` — sha256 15fd019eaaff63f0961bf2c3d18b8cb44720c4d10297a80056f1414721130ab6 (compagnon : vérifié)
  - correction : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/entrees/rapport-developpeur-correctif-0011.md` — sha256 81791f98687fb1cdb33ae68aaa2f19d9cc52dd10f9f41bb0177f2fbc4195d94b (compagnon : vérifié)
  - remarques : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/entrees/remarques-mandat-correctif-0011.md` — sha256 8c286d4bb5aa2570cca705987ea884e50b1b407ac39cac4a7caf61127ec65567 (compagnon : vérifié)
  - remarques : `brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/relecture-fable-v1/entrees/table-des-lignes-retirees.json` — sha256 527d98498eb2c4d4a2a7435767b4d4fe3120ce24bb817d373e2bd0e60981fd56 (compagnon : vérifié)
- Empreinte de l'invite envoyée : 5d1bd2ca78770259068158dd871780bdee9ae049d7000ebc0d8d177d0950335b
- Jetons : entrée 24982, sortie 121468 (dont réflexion 117563), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 5.058576 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
**Verdict : autorisable après corrections.**

Aucun point bloquant. Le seul code de production touché est le report d'un import dans `session_v5.py` ; le fichier qui porte la garde n'est pas dans le correctif. Les corrections demandées sont des preuves à joindre et des assertions à ajouter dans des essais existants, sans changer la liste figée ni le nombre 275.

Limites de ma lecture : je n'ai ni `lanceur_v5.py`, ni `lancer_iib_v3.sh`, ni le reste de `session_v5.py`, ni les sorties d'essais et de répétition (reprises du rapport). Je n'ai pas recalculé les empreintes. Les numéros de ligne sont ceux du correctif.

## Constats sur les six points

**1. Périmètre : conforme.** Huit fichiers, tous justifiés par (a), (b) ou la liste :
- `scripts/amorce_instance_iib_v5.sh` (lignes 43-47, 55-56) : nom et empreinte de la liste neuve, commentaire d'en-tête.
- `scripts/repetition_locale_iib_v5.py` (68-69) : 271 devient 275.
- `scripts/tests-cibles-iib-v5-v5.txt` (79-102) : liste neuve, l'ancienne reste.
- `src/controle_ia/iib/session_v5.py` (111-115, 123, 131) : l'import de `configuration_v5` passe dans `verifier_config` ; c'est (b).
- `tests/iib_v5_outils.py` (158-187) : deux aides, poste sans carte et interpréteur sans numpy.
- `tests/test_iib_distillation_bout_en_bout_v5.py` (197, 202, 211, 215) : `carte=False` dans quatre appels.
- `tests/test_iib_lanceur_v5.py` (457-458, 483-484, 493-505, 514-533) : cinquième `carte=False`, isolement de l'essai à blanc, liste en version 5, interpréteur sans numpy pour la surveillance.
- `tests/test_iib_environnement_machine_v5.py` (224-446) : les quatre essais neufs.

Rien d'autre n'est touché : ni la garde, ni le lanceur de session, ni une configuration.

**2. (a) : acquis sur ce que le correctif montre, deux réserves.**
- **Effet en production.** La garde est inchangée par construction. `carte=False` et `CUDA_VISIBLE_DEVICES` n'apparaissent que sous `tests/`. L'essai 2 (391-395) attend trois refus au point d'entrée, dont « accord seul » avec l'isolement des essais : l'isolement ne défait donc pas l'accord.
- **Défaut masqué.** Je n'en vois pas : les cinq appels visent le contrôle qui suit la garde, et la détection reste éprouvée (358-360, 366-368, point d'entrée).
- **Réserves.** Le paramètre `carte` existait avant et je ne vois pas le point d'entrée (remarque 2). La suffisance de `carte=False` seul sous accord posé ne repose que sur l'essai 4 et la répétition (remarque 4).

**3. (b) : acquis pour la règle, non vérifiable pour deux sous-points.**
- **Règle.** L'essai 3 la joue sous `-I -S`, donc sans aucun paquet tiers : cas sain, artefact, autre phase.
- **Phase illisible.** Le refus reste, avec son message propre (428-429).
- **Sous-commande `config`.** `verifier_config` charge encore le module et appelle `exiger_config_v5` comme avant (131-134).
- **Non vérifiable ici.** L'absence d'autre usage de `cf`, et le fait que la surveillance n'appelle pas `config` (remarque 1).

**4. Essais neufs : les trois conditions sont reproduites, chacune avec cas sain et artefact.**
- **Échouent sans la correction, selon le rapport.** Les essais 3 et 4, plus les trois essais de surveillance.
- **N'échouent pas sans elle.** Les essais 1 et 2, ce que le rapport déclare (remarque 3).
- **Sensibilité de l'essai 4.** À la lecture, il réagit à chacune des trois corrections, prise seule.
- **Ligne 271 retirée.** Je ne peux pas vérifier le septième identifiant rejoué.

**5. Liste et nombre : cohérents ; réserve : juste.**
- **Liste.** 24 fichiers, triés, le neuf au rang 11, les deux exclusions maintenues.
- **Empreinte.** Elle est identique dans le correctif et le rapport. L'essai (494) et l'amorce la recalculent ; un écart arrête avant tout essai.
- **Nombre.** 275 = 271 + 4 : quatre fonctions d'essai, sans paramétrage ni saut, donc le même compte sur le poste et sur la machine. Le correctif ne montre pas ce nombre dans l'amorce (remarque 9). La ligne 507 retirée est une assertion inchangée que je ne peux pas lire.
- **Réserve sur `CUDA_VISIBLE_DEVICES`.** Variable vide, posée avant le démarrage du processus : la couche de calcul de NVIDIA n'énumère aucune carte et `torch.cuda.is_available()` rend faux. `nvidia-smi` ignore cette variable, d'où la réduction du chemin, cohérente. La conséquence annoncée (arrêt pendant les essais, avant le modèle) est exacte. À ajouter : cela ne vaut que si `carte_visible()` n'a que ces deux signaux, ce que je ne peux pas lire.

**6. Défauts neufs :** remarques 5 à 8.

## Remarques

### Bloquant
Aucune.

### Majeur

1. **`session_v5.py`, lignes 123 et 131 : retrait du nom `cf` sans preuve jointe.**
   - **Ce qui ne va pas.** Rien ne montre qu'aucun autre code n'emploie `cf`, dans le fichier ou par `session_v5.cf` ailleurs. Le rapport dit « jamais la suite complète » : un essai hors liste figée n'a pas été joué. Aucun essai du correctif ne joue `config`, ni ne borne ce que la surveillance appelle.
   - **Correction.** Joindre la recherche de `cf.` et de `session_v5` dans le dépôt, et la sortie de l'analyseur statique sur ce fichier. Dans l'essai 3, jouer aussi `config` sous l'interpréteur sans numpy et attendre un code non nul avec le message de numpy. Dans l'essai de l'amorce (vers 506), vérifier que la branche `surveillance` ne passe que `coupure-etalonnage` à `$SESSION`.

2. **(a), lignes 351, 354, 393-395 : le paramètre `carte` n'est pas verrouillé côté production.**
   - **Ce qui ne va pas.** Les refus de l'essai 2 sont une preuve de comportement, pas une garantie que le point d'entrée ne transmet jamais `carte` ni un environnement substitué.
   - **Correction.** Joindre l'extrait de `lanceur_v5.py` (fonction principale, `exiger_accord`, `carte_visible`). Ajouter dans un essai existant une assertion statique : aucun `carte=False` et aucune affectation de `CUDA_VISIBLE_DEVICES` sous `src/` et `scripts/`.

Si l'une de ces deux vérifications revenait négative, elle deviendrait bloquante.

### Mineur

3. **Essais 1 et 2 (331-395) : ils passent avant comme après.** Le mandat demandait qu'ils échouent sans la correction ; la reproduction de (a) qui échoue repose donc sur le seul essai 4. Correction : les nommer essais de non-régression de la garde, et faire accepter l'écart.

4. **Essai 1, lignes 350-354 : le cas sain n'a pas la forme des appels corrigés.** L'artefact porte sur `executer`, le cas sain sur `phase_etalonnage` avec `{}`. Les cinq appels corrigés passent `carte=False` sans `{}`, et le commentaire attribue l'isolement à `{}`. Correction : ajouter le cas sain de même forme sous accord posé. S'il échouait, les cinq appels seraient insuffisants sur la machine.

5. **Lignes 178-179, 524, 533 : plus aucun essai ne joue le vrai `python3` du système.** L'interpréteur simulé a la version de celui des essais ; une incompatibilité de version de la règle ne se verrait plus. La documentation dit « est celui du système », ce qui est inexact. Correction : ajouter dans l'essai 3 une variante avec le `python3` trouvé sur `/usr/local/bin:/usr/bin:/bin`, sous `-I -S -B`.

6. **Essai 3, lignes 417-420 : l'environnement est hérité.** `-I` neutralise les réglages de codage de Python, et les assertions comparent des accents et « ≥ ». Correction : poser `LANG=C.UTF-8` comme le fait `_surveiller`, et un décodage explicite.

7. **Essai 4, lignes 307-308 et 442-445 : le pytest enfant hérite de trois choses.**
   - **Ce qui ne va pas.** Il hérite de `PYTEST_ADDOPTS`, des greffons du dossier de paquets parent, et de la façon dont le parent trouve `controle_ia`. Le fichier `.pth` ne rejoue pas les `.pth` imbriqués : une installation en mode éditable serait invisible.
   - **Correction.** Poser `PYTHONPATH` explicitement comme à la ligne 326, et retirer `PYTEST_ADDOPTS`. Vérifier dans le `pip-freeze.txt` de la machine qu'aucun greffon de pytest n'importe torch.

8. **Lignes 158, 171-173 : le commentaire promet plus que le code.** Il dit « jamais hérité », alors que tout l'environnement est hérité sauf trois variables, dont les autres `IIB_*` de l'amorce. Le chemin réduit suppose un `git` binaire autonome. Correction : rectifier le commentaire, ou filtrer `IIB_*`.

9. **Lignes 55-56 et rapport, section « Liste figée » : le nombre attendu n'est pas dans l'amorce modifiée.** Le rapport le fait passer par `IIB_TESTS_ATTENDUS` dans l'ordre de relance. Correction : confirmer qu'aucun 271 par défaut ne subsiste (amorce, lanceur de session, modèles d'ordre).

10. **Rapport, section « Essais qui reproduisent la machine » : treize essais non énumérés.** Quatre neufs et huit rejoués font douze. Correction : donner les treize identifiants.

Les autres lignes retirées (50, 469, 470, et la ligne 6 du mandat) n'empêchent aucune conclusion.

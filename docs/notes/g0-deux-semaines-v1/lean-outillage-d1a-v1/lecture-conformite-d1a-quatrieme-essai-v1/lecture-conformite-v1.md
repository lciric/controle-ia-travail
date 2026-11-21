# Lecture de conformité de l'outillage Lean D-1a, quatrième essai — v1

- **Date** : 2026-11-21T19:23Z (`date -u`). **Lecteur** : Claude Opus 5.5, sous-agent neuf (R13). Je n'ai écrit ni la
  procédure, ni la consigne, ni le code, ni le rapport du poste. Pièce de lecture ; aucun commit.
- **Critères appliqués** : la procédure du poste local v12, section 8 (« lecture »), et ce qu'elle fixe sur la conformité.
  Aucun autre critère.

## Verdict

**Non établi.** Le pas noyau, les mesures de mémoire et les sondes réseau tiennent selon la lettre de la section 8. L'épreuve
d'isolement sort « non conforme » (code 1) à cause d'**un seul cas** : « sortie de lui-même en code 137, sans consommer la
limite (5 s) ». Les trois conditions que le § 8.2 écrit pour ce cas sont tenues. L'épreuve exige en plus « SORTIE 137 » sur
la sortie standard, et elle ne l'y trouve pas. **La procédure ne dit pas si ce désaccord entre l'épreuve et la lecture
écrite bloque la conformité de l'outillage ou s'il est un écart toléré.** Elle ne donne d'ailleurs aucune règle qui combine
les lectures en un verdict sur l'outillage (§ 8.6 : seule la mère déclare, « sur ces lectures »). Le cas revient à Lazar.

## 1. Pièces et empreintes (vérifiées)

| Pièce | Où | Empreinte vérifiée |
|---|---|---|
| Procédure v12 | `47c7faaf`, `…/procedure-poste-local-d1a-v12.md` | `10872ae6bb6b4bdc45e48742ac879a50d024408c283138da51a5b7aaaff43cac` |
| Consigne v8 | `origin/main` (`4c26cb02`), `…/consigne-poste-local-lean-d1a-v8.md` | `3279bf4256b8c1eab212b2ff76c6ce7155d76863253d18b5f812d0f486cf1ed5`, compagnon OK |
| Erratum 1 de la consigne v8 | `origin/main`, même dossier | compagnon `sha256sum -c` OK |
| Rapport du poste v4 | `90d0ef8d`, `…/rapport-poste-local-d1a-v4.md` | `a0f5075d97dbffdc40d2acf9365d8ee7e35eef88cafecc02ceb71bba36e8c783` |
| Manifeste des pièces | `9b4691da`, `…/empreintes-pieces-poste-local-d1a-fae70647f54e-v2.sha256` | `da2044df13e9a01be9c94bbec4a0a9d32ba8004136e6fc96210f1242bf792075` |
| 13 pièces brutes | `9b4691da`, `…/pieces-poste-local-d1a-fae70647f54e-v1/` | 13 sur 13 « OK » contre le manifeste ; 13 fichiers dans l'arbre, 13 lignes au manifeste |

Remarque : la référence locale `main` du clone (`52f57978`) est en retard ; l'erratum 1 n'est que sur `origin/main`, où je
l'ai lu. Le code nommé par la procédure (`3c2f35dd`) a été lu pour la seule question de la sortie standard du cas 137.

## 2. Lecture de la section 8, dans l'ordre du § 8.1, sur les sorties brutes

1. **Pilote « avant »** : code 0 (`pilote-avant-code-v1.txt`). Sonde « ouverte », sans écart ; « `bac` lit
   `Mathlib.olean` » : bilan conforme (sain lu, témoin 0644 lu, artefact 0600 refusé) ; « le vérificateur compile sur la
   machine » : bilan conforme (sain en code 0 sans message, copie cassée refusée en code 1). **Tenu.**
2. **Pas noyau** (`premier-pas-noyau-v6.json`) : `conforme` vrai ; 18 cas, 18 `ok`, aucun écart. **Tenu.**
3. **Code de l'épreuve** (`epreuve-code-v6.txt`) : **1, « non conforme »** au sens du § 8.1, point 3.
4. **Épreuve** (`epreuve-isolement-v6.json`, version `epreuve_isolement_v8`) :
   1. `statut` « non conforme », `conforme` faux ; manifestes d'avant et d'après égaux ;
   2. `genres` : gardes Lean, isolement Lean, Python et limites Lean « conforme » ; **limites « non conforme »** ;
      `genres_morts` vide ;
   3. cas :
      - gardes Lean : 21 sur 21 `ok`, aucun écart ;
      - isolement Lean (§ 8.2) : les cinq cas portent `sonde_muette` faux et `code_compilation` 0, avec un extrait de
        sortie ; toutes les tentatives de lecture, d'écriture et de persistance rendent « ECHEC », sauf le cas sain, qui rend
        `ecriture-tmp` et `ecriture-item` « REUSSI ». Tentatives réseau : `reseau-curl-ip` dit un refus (« Couldn't connect
        to server ») ; `reseau-dns` dit une résolution impossible (`Temporary failure in name resolution`) ;
        `reseau-python-tcp` montre que le programme a été lancé (trace dans `socket.create_connection`), mais **la raison
        n'est pas dans les 160 caractères gardés**. Le § 8.2 demande seulement de le dire ; il ne le classe pas « non
        éprouvé », qu'il réserve au programme non lancé. Je le dis ;
      - Python : 4 sur 4 `ok` ;
      - limites : « mémoire (512M) » incident « mémoire », `oom-kill` ; « tâches (32) » `ok` sans écart (le contrôle
        « REFUS » sans « LANCES » est fait par l'épreuve, la sortie standard n'est pas versée) ; « durée murale (10 s) »
        « délai », systemd `timeout` à 10,009 s ; « temps de processus (5 s) » : point 5 ci-dessous ; **cas 137 : point 3**
        **ci-dessous** ;
      - limites Lean, lu sur la seule compilation : `temps.resultat` `oom-kill`, `incident_compilation` « mémoire »,
        `code_compilation` 1, extrait de sortie vide (sans « ALLOUE »). **Tenu.** Relevés sans compter : `incident_noyau`
        nul, `incident_bac` « mémoire » ;
   4. `controles_hote` vide ;
   5. bloc `memoire` (§ 8.4) : `chemin_cgroupe_faux` faux, `lancements_sans_releve` vide ; les pics des processus Lean avec
      Mathlib sont de 659 à 675 millions d'octets à la compilation, environ 2,40 milliards pour le vérificateur ; aucun de
      l'ordre de quelques centaines de Kio. Aucun « conforme » n'en dépend.
5. **« Temps de processus (5 s) »** (§ 8.3) : incident « délai », temps de processeur de l'unité 5,012 s, au moins 4,95 s :
   **première lecture, conforme**.
6. **Mesures** (`mesures-v6.json`, § 8.5) : `suite` et `parallele_3` : 3 et 3 acceptés, sans incident ; tranche
   `bacmesure5931df57.slice`. Recalculé sur `releve_machine` : pic de la tranche 7 207 055 360 au plus la moitié de
   `MemTotal` (16 428 720 128) ; baisse de `MemAvailable` 7 216 439 296 au plus le pic plus 1 Gio (8 280 797 184) ;
   disponible prudent au plus bas 24 783 241 216, au moins le quart (8 214 360 064) ; 118 relevés de la tranche, 119 de
   `MemAvailable`. `parallele_3_compte` vrai, `parallele_3_motifs` vide. **Le passage en parallèle est compté.**
7. **Sondes réseau** : `sonde-apres-coupure-v6.json` et `sonde-fin-v6.json`, identiques octet pour octet : attendu
   « fermée », `ecarts` vide. **Tenu.**

## 3. Le cas en échec : « sortie de lui-même en code 137, sans consommer la limite (5 s) »

**Faits bruts** (cas 34 de l'épreuve) : `ok` faux ; `ecarts` = `["stdout sans « SORTIE 137 »"]` ; code 137 ;
`incident_bac` nul ; temps de processeur 0,033 s ; durée murale 0,101 s ; systemd `exit-code`, `status=137` ; aucun relevé
de mémoire (unité sous la seconde).

**Ce que la procédure écrit pour ce cas** (§ 8.2) : « code 137, aucun incident, temps de processeur de l'unité de l'ordre de
quelques dizaines de millisecondes ». Les trois conditions sont tenues. Le texte ne parle pas de la sortie standard.

**Ce que l'épreuve exige** (attendus v7 au commit `3c2f35dd`) : `code` 137, `stdout_contient` « SORTIE 137 »,
`incident_attendu` nul. L'épreuve ne trouve pas « SORTIE 137 » ; le cas est `ok` faux, le genre « limites » non conforme, le
statut non conforme, le code 1.

**Ce que la procédure dit, et ne dit pas** :
- elle dit que le code 1 de l'épreuve veut dire « non conforme » (§ 8.1, point 3) : l'épreuve est donc non conforme, cela est
  établi ;
- elle **ne dit pas** comment se tranche un cas où la lecture écrite du § 8.2 tient et où l'épreuve refuse sur un attendu que
  le § 8.2 ne reprend pas ;
- elle **ne dit pas** qu'une épreuve non conforme rend l'outillage non conforme, ni qu'un écart de ce genre est toléré :
  aucune phrase de la section 8, ni des sections 0 à 7, ne combine les lectures en un verdict sur l'outillage. Le § 8.6 dit
  seulement que « l'outillage D-1a n'est déclaré conforme par personne d'autre que la mère, sur ces lectures » ;
- la seule règle de reclassement écrite (« aucun reclassement à la main ; correction en version neuve, contre-lue, avant un
  essai suivant ») vise le cas « temps de processus (5 s) » dans une plage précise (§ 8.3). L'étendre au cas 137 serait un
  critère inventé ;
- le préambule de la section 8 s'applique : « une sortie qui ne rentre dans aucune lecture écrite ici est rapportée telle
  quelle à la mère, sans lecture inventée ». Le rapport du poste l'a fait (§ 8.1.4, cas 137 ; § 7).

**Réponse à la question posée** : la procédure ne classe ce cas **ni** en échec bloquant **ni** en écart toléré. Elle ne le
dit pas. D'où le verdict « non établi ».

**Information hors critère, pour la décision** (ne change pas le verdict) : l'artefact `limite_code137_v1.py` fait
`print("SORTIE 137")` puis `os._exit(137)`. Quand la sortie standard n'est pas un terminal, Python la garde en tampon, et
`os._exit` sort sans vider ce tampon. Reproduit ici, hors machine, avec Python 3.13 : `python3 -c 'import os;
print("SORTIE 137"); os._exit(137)' | od -c` ne rend aucun octet, code 137 ; avec `-u`, la ligne sort. Les essais hors
machine de l'épreuve v8 (`tests/test_lean_essai_epreuve_v8.py`, exécuteur factice) fabriquent la sortie standard à partir
des attendus et n'ont donc jamais lancé cet artefact. C'est une cause probable, non établie sur la machine (Python 3.12.3,
sortie standard non versée). Si elle tient, le défaut est dans l'artefact d'épreuve, pas dans la limite du bac.

## 4. Ce qui reste non éprouvé ou non lisible

- la sortie standard du cas 137 (non versée par l'épreuve) et donc sa cause sur la machine ;
- la raison du refus de `reseau-python-tcp`, coupée à 160 caractères ;
- le « REFUS » sans « LANCES » du cas « tâches (32) », contrôlé par l'épreuve mais non visible dans les pièces.

## 5. Nœuds pour Lazar

1. **Le cas 137 de l'épreuve** : la procédure v12 ne dit pas si son échec, alors que les trois conditions du § 8.2 tiennent,
   bloque la conformité de l'outillage D-1a ou est un écart toléré. Options :
   (a) le tenir pour bloquant : outillage non conforme ; correction de l'artefact (par exemple vider la sortie avant
   `os._exit`) en version neuve, contre-lue, et un nouvel essai, qui coûte une machine ;
   (b) le tenir pour un écart toléré, déclaré, sur la seule lecture écrite du § 8.2 ; l'outillage est alors lisible
   conforme sur toutes les lectures écrites ;
   (c) établir d'abord la cause hors machine, sans dépense, et ne trancher qu'ensuite entre (a) et (b).
2. **Règle de conformité de l'outillage** : la procédure n'en écrit aucune qui combine noyau, épreuve et mesures. À écrire
   avant tout essai suivant, pour qu'une lecture neuve ait un critère à appliquer.
3. **`reseau-python-tcp`** : la raison du refus n'est pas lisible dans l'extrait. Le § 8.2 demande seulement de le dire. À
   Lazar de dire si cela suffit, ou si la borne de 160 caractères doit être revue.

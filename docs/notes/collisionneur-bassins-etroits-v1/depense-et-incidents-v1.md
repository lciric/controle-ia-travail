# Tour du collisionneur sur les bassins d'idées étroits et profonds, consultations à part comprises : dépense et incidents — v1

Écrit le 13 novembre 2026 à 14:35 UTC (heure relevée par `date -u`) par l'opérateur neuf (Claude Opus 5.5) de la session
mère, sous **GO-2026-11-12-04** (tour 2 sur 4 ; plafond de ce tour 15 USD, consultations comprises). Devis scellé avant tout
appel : `devis-v1.md` (`eed4939a…`), pire cas 2,42 (consultations) + 14,47 (collisionneur) = 16,89 USD, garantie de plafond
par ordre de passage.

## 1. Déroulé (heures de `date -u` et des consoles, UTC)

- 12:43 → 12:47:11 : faits, question, devis écrits et scellés dans le dépôt ; programme des consultations écrit, essais hors
  réseau 19 sur 19 (`essais-consultation-a-part-sortie-v1.txt`).
- 12:47:19 : relais Kimi `relais_kimi_v4.py` lancé (port 8789, plafond 3 USD, au plus 8 appels) ; son état rend `pid` 19172,
  égal au `$!` du lanceur, et « variable de clé encore présente : non ».
- 12:47:30 → 13:11:31 : consultations à part, un appel chacune, un seul essai (`console-consultations-v1.log`) : Argon
  12:47:30, Astra 12:50:27, Kimi 12:54:35 ; code 0 ; dépense au barème du script **1,5451 USD**.
- Plafond du collisionneur : 15,00 − 1,55 (1,5451 arrondi au centime supérieur) = **13,45 USD**.
- 13:11:42 → 14:33:54 : étage III, un seul lancement (`console-run-e3-v1-lancement1-v1.log`), code 0, **12,29 USD**.
- 14:33:58 : état du relais relevé (`relais-v1/etat-apres-v1.json` : 4 appels, tous statut 200, 0,98236 USD, aucun refus,
  aucun écart de modèle servi, aucun usage absent) ; **relais arrêté par son numéro de processus, 19172** (R10), contrôlé par
  `ps` avant le signal, arrêt vérifié à 14:34:05.
- 14:34:05 : `verifier` du run dans le bac à sable, hors réseau : **« tout tient »** (`verification-run-e3-v1.txt`).
- 14:34:33 : copie `cp -a` du run vers `run-e3-v1/` du dépôt ; `verifier` sur la copie : **« tout tient »**
  (`verification-copie-run-e3-v1.txt` ; seul l'horodatage de `etat.md`, régénéré par `verifier`, diffère).

## 2. Consultations à part (`consultations-a-part-v1/`)

Prompt unique, le même pour les trois (`dd3db386…`, 13 090 caractères), modèle non nommé ; blocs FAITS (`d19b5400…`) et
QUESTION (`935f4e5b…`) aux empreintes du collisionneur.

| consultation | modèle servi | statut | fin | marqueur | jetons d'entrée | jetons de sortie | coût au barème du script, USD |
|---|---|---|---|---|---|---|---|
| Argon | `gemini-4-argon` | OK | STOP | oui | 3 865 | 12 625 | 0,6699 |
| Astra | `gpt-6-astra` | OK | stop | oui | 3 622 | 11 411 (dont 2 973 de raisonnement) | 0,6068 |
| Kimi | `kimi-k3.1-pro` | OK | stop | oui | 4 369 | 25 964 | 0,2684 |
| **total** | | | | | | | **1,5451** |

**Les trois consultations sont valides** (fin normale, non tronquées, marqueur `FIN-DE-CONSULTATION` présent, modèle servi
égal au modèle demandé). Aucun refus, aucune relance. Contenu non lu au-delà de ce contrôle.

## 3. Cellules du collisionneur

**15 cellules valides sur 15** (A `claude-fable-5-1`, B `claude-opus-4-6`, C `gemini-4-argon`, D `kimi-k3.1-pro` par le
relais, E `gpt-6-astra`, aux trois tours III.1, III.2, III.3) ; modèle servi égal au modèle demandé ; marqueur de fin présent ;
aucune absence acceptée. **Argon a répondu au tour III.2** (refusé au tour 1). Un seul incident, prévu par le script :
`E3-T1-conception-A`, essai 1, **TRONQUE** (fin `max_tokens` à 22 000 jetons, 1,16 USD), relancée par le script lui-même à
son plafond de relance (64 000) sous le plafond du run ; essai 2 OK (21 123 jetons). Contenu des cellules non lu.

## 4. Dépense relevée (journal du run et relevés des consultations, barème du script)

| espèce | modèle | collisionneur : essais (OK), entrée / sortie, USD | consultation, USD | total, USD |
|---|---|---|---|---|
| A | `claude-fable-5-1` | 4 (3), 116 313 / 75 394, 4,9328 | — | 4,9328 |
| B | `claude-opus-4-6` | 3 (3), 85 127 / 22 042, 2,9300 | — | 2,9300 |
| C | `gemini-4-argon` | 3 (3), 67 840 / 30 092, 2,1830 | 0,6699 | 2,8529 |
| D | `kimi-k3.1-pro` | 3 (3), 81 806 / 55 037, 0,7139 | 0,2684 | 0,9823 |
| E | `gpt-6-astra` | 3 (3), 70 240 / 16 601, 1,5324 | 0,6068 | 2,1392 |
| **total** | | **12,2921** | **1,5451** | **13,8372** |

Sorties d'Astra comptées réflexion comprise (1 358 jetons de raisonnement sur trois cellules).

- **Total consigné : 13,84 USD ≤ 15** (pire cas des devis 16,89).
- Kimi : 0,9823 au barème du script, égal au compte du relais (0,98236 ; 4 appels sur 8 permis, plafond 3).
- Sur les crédits de la clé `RR_ANTHROPIC_API_KEY_RIGAUD` (A + B) : **7,8628 USD au barème du script** ; au tarif public
  RAPPORTÉ au tour 1 (Fable 5.1 10/50, Opus 4.6 5/25 ; non relu ici) : environ **5,91 USD** (B à 0,9767 au lieu de 2,9300).
- Hors crédits de Claude, sous le même plafond de tour : Argon 2,8529, Astra 2,1392, Kimi 0,9823.

## 5. Incidents, écarts et réserves, déclarés

1. **Troncature de A au tour III.1, premier essai** : traitée par la relance prévue du script (même consigne, plafond de
   relance), non par l'opérateur ; 1,16 USD perdus.
2. **« Réponse brute entière » des consultations** : les fonctions d'appel du script, seules permises, ne rendent pas le corps
   JSON du fournisseur ; `reponse-brute.json` porte l'objet `Reponse` entier rendu par la fonction (texte, modèle servi,
   identifiant de réponse, fin, catégorie, usage, types de blocs, échec). Pour Kimi, le raisonnement (`reasoning_content`)
   n'y est pas.
3. **Essais hors réseau** : un premier passage a donné 18 sur 19 ; l'essai fautif exigeait que le prompt entier ne nomme aucun
   modèle, alors que les faits (identiques à ceux du collisionneur) nomment les proposeurs de l'organisme ; l'essai a été
   restreint à l'en-tête avant les faits, avant tout scellement et tout appel ; second passage 19 sur 19. Le programme n'a pas
   changé.
4. **Consoles et journaux** : garde ciblée (`sk-ant-`, `sk-`, `AIza`, `ghp_`, `hf_`, `AKIA`, et `org-`, `organization`,
   `workspace`, `proj_`, `api_key`) sur tous les fichiers de sortie : **0 touche** ; aucun identifiant d'organisation ni de clé
   d'un fournisseur : les fichiers sont versés **sans masque** (copies identiques aux originaux du bac à sable ; empreintes :
   `run-e3-v1/journal.jsonl` `96e3ff42…`, console du run `2c7f2ab7…`, console des consultations `b189db85…`, console du relais
   `c2add6c6…`, journal du relais `0e13b930…`, état du relais `21e1a053…`). Les consoles portent le chemin du bac à sable.
5. **Interpréteur** : environnement Python du bac à sable du tour 1 (`venv-coll`), employé en lecture, `-I -B`.
6. Aucune écriture git ; rien d'intermédiaire versé dans le dépôt pendant le tour.

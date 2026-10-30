# Préparation de la course 1, tentative 2, sur l'orchestrateur v50 — note v1

Session-depot (fork de préparation), 30 octobre 2026. **Rien de payant n'a été lancé** : aucun appel aux API, aucun relais réel.

## Décision de Lazar (≈ 07:20 UTC, relayée par la session) : **sans Opus comme proposeur**
- Proposeurs : **Fable 5.1** (`claude-fable-5-1`) et **Argon** (`gemini-4-argon`). **Opus 5.5 reste juge.**
- Même question, même corpus, mêmes pièces, mêmes témoins, même liste blanche, même attestation du matériau que la tentative 1.
- Ce que ça change dans `args-course-v2.sh` :
  - `--proposeur opus=claude-opus-5-5` et son budget `proposeur_ideation|claude-opus-5-5=5` sont retirés ;
  - **le budget total Claude passe de 50 à 40** ; le plafond du relais Claude passe aussi à 40.
- Vérifié :
  - la v50 accepte un seul proposeur Claude : essai à blanc, code de course normal ;
  - la seconde passe reste cohérente : Fable et Argon ont chacun `passe-1` et `passe-2` ; en passe 2, chacun lit les fiches anonymes de l'autre fournisseur ;
  - les modèles permis du relais restent exactement `claude-opus-5-5,claude-fable-5-1`, car Opus est toujours juge.

## 1. Arbre v50
`/root/ideation-v1/orchestrateur-v50/arbre/` : extrait de `origin/canal/conv-audit-n04`. `EMPREINTES-orchestrateur-pole-v7-v50.txt` (`3b1458f3…`) : **178/178 OK**.

## 2. Changements d'arguments ou de contrat, de la v45 à la v50, qui touchent cette course
- **v46** (dossier fermé, outils par protocole) : sans `--dossier-ferme`, la course est celle de la v45, consignes identiques octet pour octet. Rien à changer.
- **v47** :
  - **moissonneur** : `--moisson` vaut `aucune` par défaut ; on ne le pose pas, la moisson est désactivée.
  - **correctif R-764**, trois barrières :
    1. **Kit** : `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK` et `CLAUDE_CODE_NO_MODEL_FALLBACK` sont posées par le noyau dans toute session (`adaptateurs.VARIABLES_SANS_REPLI_DE_MODELE`), avec `fallback_model=None`. **Vérifié ici** : les deux chaînes sont présentes dans le binaire de l'outil installé (2.1.314, contre 2.1.312 au 29 octobre) et dans le binaire du kit (`claude_agent_sdk` 0.2.172, `_bundled/claude`). Leur effet reste **SUPPOSÉ** jusqu'à l'épreuve réelle.
    2. **Noyau** : le modèle servi est lu à chaque message ; tout `stop_reason == "refusal"`, tout événement `model_refusal_fallback` ou tout modèle servi différent du modèle demandé donne un **refus, donc un arrêt propre** (statut « refus », `CourseInterrompue « refus (R-764) »`), jamais « budget_depasse ». La sortie de la session est mise à l'écart.
    3. **Relais** : `relais_reel.py --modeles-permis claude-opus-5-5,claude-fable-5-1` refuse tout autre modèle avant l'amont. Le lanceur exige que la liste soit **exactement** celle des modèles des proposeurs et des juges. **C'est nouveau par rapport à la tentative 1 et c'est ajouté dans le lanceur.**
- **v48** : `--tests-de-mort` vaut 0 par défaut, et c'est la valeur retenue ; sans l'option, les sorties sont celles de la v47 octet pour octet. Rien à changer.
- **v49** (CL13-05) : avec le moteur réel, **la commande externe doit rendre `modele_servi`**, sinon c'est un refus.
- **v50** :
  - **l'étiquette de tout rôle externe doit être le modèle que la commande demande, `gemini-4-argon`**. La tentative 1 disait `gemini-argon` : **corrigé** dans `--proposeur-externe`, `--juge-externe` et les deux `--budget`.
  - Le suffixe de date accepté est strict (`-AAAAMMJJ`).
  - Les autres changements (utilisateur du bac, sortie de l'étage, « survit » arrondi) ne concernent que l'étage de tests de mort.

## 3. Compatibilité de la chaîne d'Argon (relais Gemini → `appel-argon-v3.sh` → `commande_argon_v2.py`)
**Compatible**, sans rien changer à `/opt/argon/` :
- `commande_argon_v2.py` (`6905ac71…`) demande toujours `gemini-4-argon` (`MODELE_DEFAUT`, aucun `--modele` passé par le noyau) ;
- elle lit `modelVersion` dans la réponse, rend `modele_servi`, et vérifie elle-même la conformité (`lire_reponse`, ligne 239) ;
- le noyau compare ensuite au modèle demandé par l'étiquette `gemini-4-argon`.

Observé hier soir (bisociation, 23:11 UTC) : `modele_servi` = `gemini-4-argon` exactement.

**Réserve, CL15-05** : si Gemini rendait un jour un `modelVersion` d'une autre forme (par exemple `models/gemini-4-argon`), ce serait un refus **après** l'appel payé. Le remède existe : `--modele-servi-externe-permis gemini-4-argon=<forme>`. Il n'est pas posé, faute de cas observé.

## 4. Fichiers préparés (dans `/root/ideation-v1/`)
- `args-course-v2.sh` : adaptation de `args-course-v1.sh`. Il change le chemin de l'arbre, l'étiquette `gemini-4-argon` et retire Opus des proposeurs (total Claude 40). Tous les autres budgets par rôle sont inchangés.
- `lancer-course-v2.sh` : vérifie le GO, les clés, l'arbre v50, le relais Gemini, l'enveloppe et la commande d'Argon, les ports et l'absence de sortie (R12). Ensuite, il :
  - lance le **relais Claude** (`RR_ANTHROPIC_API_KEY_3`, la clé de la tentative 1, vérifiée dans la commande du 29 octobre) avec un plafond de 40 et `--modeles-permis` ;
  - lance le **relais Gemini** (`GEMINI_API_KEY_2`, 64 appels au plus), clés par variable sous `env -i` ;
  - mesure les consignes, puis lance la course réelle (`--moteur claude-sdk --confirmer-moteur-reel`). L'orchestrateur fait lui-même l'appel de contrôle de chaque modèle avant la première session ;
  - relève l'état final des relais, **les arrête par leur PID** (R10, sur tout chemin de sortie) et scelle les journaux.
  
  Les sorties vont dans `sortie-course-v2/`.
- Mesures : `mesure-consignes-v50-dos-v2.txt`. Code 0, « passerait » vrai, consigne de contrôle 1 077 663 caractères, comme à la v45.
- Essai à blanc (`--moteur simule`, **sans** `--commande-externe`, pour qu'aucun appel réel ne parte vers Argon) : `essai-blanc-course-v2b.log`.
  - Course complète, 13 fiches validées, deux passes pour Fable et pour Argon.
  - Code 4, attendu au moteur simulé : `temoins_ok` faux, parce que des juges simulés ne lisent pas les témoins.
  - Somme des plafonds lue au manifeste : Claude **29,6** pour un total de 40 ; externe **9,3** pour un total de 12,8 ; rien n'est toléré au-delà.
- Essais de la v50 sans réseau (`env -i`) : **502 essais, OK, 4 ignorés**. Les 4 ignorés sont les essais réels de l'étage sous `bwrap`, sans objet ici (`essais-v50-sans-reseau-v1.txt`).

## 5. Devis
- **Plafonds** (pire cas) :
  - Claude : 2 × 9,3 (Fable, deux passes) + 4 (juge Opus) + 7 (juge Fable) = **29,6**, plus les appels de contrôle (quelques centimes) ; relais plafonné à 40 ;
  - externe : 9,3 sur un total de 12,8 (contrôle 3,1, passe 1 2,5, passe 2 3,1, juge 3,5, selon les réglages ; somme lue au manifeste) ;
  - **pire cas ≈ 39 USD**, sous les totaux de 40 et 12,8.
- **Attendu** : la tentative 1 a dépensé 8,67 USD de Claude (dont 4,66 par la bascule non autorisée) et ≈ 5,8 USD d'Argon avant son arrêt en passe 1. Sans Opus proposeur, une course complète devrait coûter **≈ 15 à 25 USD** (SUPPOSÉ).

## 6. Commande exacte (root, depuis n'importe où)
```bash
GO_ID=GO-2026-10-30-03 bash /root/ideation-v1/lancer-course-v2.sh > /root/ideation-v1/lancement-course-v2.out 2>&1
```
Durée attendue : jusqu'à environ 1 h 30 (délai de 3 600 s par session). À lancer en arrière-plan.

## 7. Ligne proposée pour `registres/go.md` (à inscrire par la session)
`| GO-2026-10-30-03 | 2026-10-30 | calcul | **course 1, tentative 2, sur l'orchestrateur v50, sans Opus proposeur** (décision de Lazar ≈ 07:20 UTC) : proposeurs Fable 5.1 et Argon, juges Opus 5.5, Fable 5.1 et Argon ; même question, corpus, pièces et témoins que la tentative 1 ; relais Claude plafonné à 40 USD avec modèles permis exacts ; Argon 12,8 USD ; pire cas ≈ 39 USD, attendu ≈ 15 à 25 ; sous GO-2026-10-30-02 | 52,8 USD | 2026-10-30 | Lazar | mot direct de Lazar dans la session « session-depot », 30 octobre 2026, ≈ 07:15 UTC, verbatim : « on lance course 1 go » ; GO anticipé GO-2026-10-30-02 (« extension eux heures autonomie avec go depenses ») |`

## 8. Avertissements
1. **Refus** : la tentative 1 s'est arrêtée sur un refus d'Opus 5.5 au proposeur, passe 1. **Opus n'est plus proposeur**, ce qui ôte ce risque-là, mais **Opus reste juge** et peut refuser de noter. Fable n'a encore jamais été proposeur sur cette question. En v50, un refus, quel que soit le rôle, donne un **arrêt propre** : la session est close au premier message fautif, sa sortie est mise à l'écart, et le manifeste de fin porte `statut_course = refus` avec la dépense comptée à part. Aucune bascule ni relance automatique. Une relance relève de R-750 : une question plus étroite et un nouveau run.
2. **Effet réel des variables du kit** (barrière 1) : SUPPOSÉ ; les barrières 2 et 3 le couvrent.
3. **`temoins_ok`** : le code 4 en simulé est attendu. En réel, un code 4 signifie que les juges ont mal classé les témoins plantés : le classement n'est alors pas lisible.
4. **Version de l'outil** : 2.1.314 aujourd'hui, 2.1.312 lors du correctif. Les chaînes des variables sont présentes, mais l'outil n'a pas été exercé.
5. La v50 n'est pas contre-lue **sans l'étage**, mais CL14 et CL15 l'ont dite lançable sans l'étage, avec l'étiquette `gemini-4-argon` (corrigée ici).

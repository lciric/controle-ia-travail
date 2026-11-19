# Journal de l'exécutante du saboteur à budget — v5

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Suite du journal v4 (`registres/iib-executante/journal-v4.md`, `0bb6c671…9217`), qui reste tel quel. Exploratoire, non opposable (R-522). Aucune instance, aucune recherche d'offre, aucune dépense.

## 2026-11-19T06:30Z — mot de Lazar dans cette session
- Lazar a tapé « go création de la course » dans cette session ; cité mot pour mot avec l'heure à la mère, rien fait d'autre.
- Mère (06:34Z) : relu à la source (événement `e9c8139a-…`, 06:30:18Z), consigné R-3614 et GO-2026-11-19-04 ; valeur du marqueur `MOT_LAZAR_CREATION_IIB` : « R-3614 ». Vérifié sur `main` distant : une ligne R-3614 au registre des décisions, une ligne GO-2026-11-19-04 au registre des GO.

## Phase 1, points 4 et 5 — configuration et commit de lancement
- Configuration finale fabriquée par le même programme que le brouillon 3 ; seule différence avec le brouillon 3 : `MOT_LAZAR_CREATION_IIB` = « R-3614 ». Garde du code revu (`iib/session_v1 config`) : code 0, « configuration conforme (mode reel, variante B, seuil de M-1 8) ».
- `docs/notes/barreau8-iib-v1/config-iib-reel-v1.json`, sha256 `ebab1fb051890def13c2b7981c291c7cc2cea0b797bff6255b95066f5ad94fb7`, et son sceau.
- Commit de lancement `968a5151c5eb31014114e5093ba675a46fcd5414` sur `prep/iib-code-v3`, parent direct `ec3b0329`, deux fichiers seuls (configuration et sceau) ; poussé ; tête distante vérifiée.

## Phase 1, point 6 — contrôles à blanc au commit de lancement (`blanc-968a5151-v1/`)
- Suite ciblée des essais au processeur, à `968a5151` : **456 passed** (code 0).
- Empreintes des 34 fichiers du code à `968a5151` : identiques à celles de `ec3b0329` (`05f36178…`).
- Extraction réduite de `main` : clone 0, checkout 0 ; ligne GO-2026-11-10-08 : 1 ; ligne R-3614 : 1.
- Extraction réduite du code : clone 0, sparse 0, checkout 0 ; tête distante = `968a5151`, parent `ec3b0329` ; fichiers du commit : la configuration et son sceau ; ligne GO au commit : 1 ; branche du run `essai/iib-explo-v1` absente (code 2, attendu).
- Contrôles du lanceur (`lancer_iib_v1.sh controles-explo`, sans outil de location) : **code 2, REFUS**. Tout passe jusqu'à la vérification que les tâches de réserve et d'évaluation sont disjointes, qui lève `KeyError: 'taches'` (ligne 108 du lanceur) : le lanceur lit la liste des tâches au premier niveau du fichier, alors que les deux fichiers cités la portent sous `resultat.taches`. Défaut du code revu, non de la configuration. Vérifié à part, par programme : 32 tâches de réserve, 64 d'évaluation, 0 commune.
- Place : `main` réduit 7,3 Mo ; code réduit 390 Mo ; dossier des contrôles 1,6 Mo.
- Conséquence : la création exige le `lancement.txt` écrit par ces contrôles ; elle est impossible tant que le lanceur n'est pas corrigé. Nœud remonté à la mère ; je ne touche pas au code.

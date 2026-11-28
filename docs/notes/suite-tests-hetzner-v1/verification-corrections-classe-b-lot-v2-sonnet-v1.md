# Vérification des corrections — classe B — suite complète des tests sur Hetzner (lot v2)

**VERDICT : PRÊT À LANCER**, sous une seule condition de procédure : écrire la ligne d'engagement GO-2026-11-28-04 / identifiant de course au registre des dépenses (il n'y en a encore aucune, `grep -c` = 0 ; le lanceur refusera sans elle, ce qui est le comportement voulu). Aucun défaut bloquant ou majeur nouveau ; 4 mineurs nouveaux, non bloquants (section finale). Aucun serveur créé, aucun appel d'écriture à l'API.

Contrôles que j'ai faits moi-même : rejeu complet des essais R5 v2 en super-utilisateur (1 min 29 s) : A, B, C, D, E, F, G, H, I, K, L tous vrais, règle iptables retirée à la fin (`iptables -S OUTPUT` : `-P OUTPUT ACCEPT` seul) ; `bash -n` des deux scripts ; v1 intacte (empreintes de la v1 inchangées, R12) ; en lecture seule contre le registre réel et l'API : `exiger_go` renvoie 3,0 USD pour GO-2026-11-28-04, la branche de sortie et sa forme réduite n'existent pas, 0 serveur actif, prix cx53 0,05676 EUR/h aux trois lieux, 26 types lus sur 26 (pas de page manquante) ; au pire cas du lanceur (plafond + 45 min + 1 h, × 1,25) : cx53 0,69 USD, cpx41 0,76, cpx51 1,66, ccx33 2,75 USD à hel1 seulement (3,25 à fsn1 et nbg1, exclu).

## Constats de la première lecture

1. **Échéance du GO** : corrigé. `lancer…v2.py` lit `echeance`, exige accordé ≤ jour ≤ échéance, `Lazar`, absence de ligne de type `révocation` visant le GO, et lit le plafond USD de la ligne (3,0). Cas L : valide accepté ; échu, mauvais type, révoqué refusés.
2. **Minuterie hors essais** : corrigé. `sur_term` sort en code 124 hors essais (arrêt de l'étape par son PID) ; `etape()` met les commandes longues en arrière-plan sous `wait`, interruptible ; contrôle `DELAI_DEPASSE` avant les essais ; `timeout` partout. Cas F : 5,3 s, code 124, conclusion jouée, destruction faite. Non éprouvé en l'état : le crochet de F passe par `etape sleep`, pas par `apt-get` réel (même fonction).
3. **Garde de durée de la conclusion** : corrigé (`GIT_HTTP_LOW_SPEED_*`, `timeout 600` sur push, `60` sur ls-remote, `300` sur conclure.py).
4. **Identifiant du serveur** : corrigé. Cinq lectures ; repli `GET ?name=` n'agissant que sur un résultat unique et numérique. Cas G : identifiant 777 retrouvé, DELETE jouée.
5. **Filet indépendant** : corrigé. `filet…v2.sh` lancé dans les données de démarrage avant l'amorce par `systemd-run --on-active=plafond+2700s`, jeton lu par `curl -H @fichier` 0600. Cas H : amorce tuée par SIGKILL, aucun DELETE de sa part, DELETE par le filet. Réserve : H joue le script du filet, pas la minuterie systemd (inéprouvable hors serveur) ; la syntaxe `systemd-run --unit=… --on-active=…s /bin/bash …` est correcte.
6. **`--lf`** : corrigé (`--lfnf=none`).
7. **Serveur orphelin du lanceur** : corrigé (POST sous `try/except`, relecture par étiquette `run=`, identifiant affiché avant l'écriture de l'état). Reste le mineur n°3 ci-dessous.
8. **Fermeture des métadonnées et des jetons** : corrigé. Autotest à l'exécution avant tout essai : métadonnées lisibles, fichier de jeton, en-tête ou `user-data.txt` lisibles par l'utilisateur des essais, alors arrêt 13. Éprouvé dans les deux sens (A conforme, K arrêt 13 puis destruction). Limite : la règle iptables réelle n'est pas jouée, mais l'autotest la juge à l'exécution sur le serveur et échoue fermé.
9. **Commit consigné** : corrigé (environnement avant `chown`) ; A vérifie `commit=<sha>`.
10. **`-v -rfE`** : corrigé.
11. **Verrou apt** : corrigé (`DPkg::Lock::Timeout=600`).
12. **Garde-fous du lanceur** : corrigé. Dépôt imposé (constante, la copie publique est refusée), noms par expression, branche de sortie et forme réduite vérifiées absentes par `ls-remote` (échec de lecture = arrêt), plafond ≤ 28 800 s, types admis selon le pire cas contre le plafond du GO. Cas L.
13. **Repli réduit et fichiers volumineux** : corrigé. Cas E : branche pleine refusée, branche `-reduit` prouvée, scellés valides, sans jeton ; fichiers > 95 Mo compressés ou retirés et consignés au résumé. Non éprouvé (volume) : seuil de 95 Mo, code simple.
14. **Écarts d'environnement des tests** : traité autrement, accepté. Dépôt cloné à `/home/user/controle-ia-travail`, relais `/usr/local/bin/python3` vers l'interpréteur des essais, `/home/user` rendu traversable. Cela supprime la cause principale des échecs des 17 fichiers concernés. Les tests qui visent d'autres dossiers (`/home/user/ideation-organism`, `/home/user/sorties-course-auto-conception-v*`) échoueront encore : à consigner avant lecture, comme prévu.
15. **Couverture R5** : corrigé par E à L (DELETE refusé cinq fois, poussée pleine refusée, TERM en étape, identifiant retrouvé, SIGKILL, autotest, garde-fous). Cas sain et artefact présents pour chaque garde.
16. **Préalables** : ligne d'engagement encore absente (voir verdict) ; transmission de l'identifiant du fichier d'état à la surveillance externe : procédure, que je n'ai pas pu vérifier.

## Nouveaux défauts (tous mineurs)

- **N1.** Autotest : ajouter à la liste `/opt/suite-tests/entete-filet` et `/var/lib/cloud/instance/scripts/part-001` (amorce, boucle `for f in …`).
- **N2.** `pousser_dossier` retente 4 fois avec des pauses de 300 s même pour un refus déterministe (branche existante) ; au pire, deux branches × 4 × (600 + 60) s peuvent dépasser la marge de 45 min du filet, qui supprimerait alors le serveur en pleine poussée (perte du versement, pas de surcoût). Peu probable (la branche est vérifiée absente par le lanceur) ; si l'auteur y touche : ne pas retenter après un refus « non fast-forward ».
- **N3.** Lanceur : `serveur_de_la_course` n'est pas sous `try/except` ; une seconde panne réseau juste après un POST ambigu donne une trace sans état écrit (la surveillance externe, qui liste l'API, couvre ce cas).
- **N4.** Les tests qui lisent des dossiers absents du serveur (point 14) et les gardes testant l'empreinte d'un lanceur peuvent encore échouer ; cela se verra dans `echecs_persistants_en_serie` et n'est pas un défaut des scripts.

## Fichiers lus
`scripts/amorce_hetzner_suite_tests_v2.sh`, `scripts/filet_hetzner_suite_tests_v2.sh`, `scripts/lancer_hetzner_suite_tests_v2.py`, `docs/notes/suite-tests-hetzner-v1/essais_r5_amorce_suite_tests_v2.py`, `docs/notes/suite-tests-hetzner-v1/resultats-essais-r5-amorce-v2.json`, `registres/go.md` (ligne GO-2026-11-28-04, lignes `révocation`), `registres/depenses.md` (recherche), `.claude/hooks/garde_calcul.py` (`lire_go`), ma contre-lecture v1.

## Empreintes SHA-256 (telles que lues)
- `scripts/amorce_hetzner_suite_tests_v2.sh` : `311440285fc2d4a765ac5b5ba529e9a07bf61ca36d5b194b5b48f3632cb2c637`
- `scripts/filet_hetzner_suite_tests_v2.sh` : `8f7bfcf0f53ac966a2f3e84f79404289336660048c3498014276680674cc5f41`
- `scripts/lancer_hetzner_suite_tests_v2.py` : `aebfacfb5735a0134df2c164304ebe826cfc2423a480b7990fbc1af9c6e48a02`
- `docs/notes/suite-tests-hetzner-v1/essais_r5_amorce_suite_tests_v2.py` : `a84d644bc426ca1579ac5fb75bb1f0172b3f601ad65dbf528ca69434f0c1a4d6`
- `docs/notes/suite-tests-hetzner-v1/resultats-essais-r5-amorce-v2.json` : `71a47649bc29cdddf3833b500889aa6e35ac596342a6ae85f4bd5fa8492e3a37`

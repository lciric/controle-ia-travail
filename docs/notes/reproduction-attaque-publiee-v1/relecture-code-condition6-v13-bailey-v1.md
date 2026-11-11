# Relecture R2, en différentiel v12 → v13, du lanceur de la condition 6 — témoin de Bailey — v1

- Date : Wed Nov 11 16:01 UTC 2026 (`date -u`). Relecteur : sous-agent neuf (R2). Je n'ai écrit aucune des pièces lues.
- Je reçois d'office le `CLAUDE.md` du dépôt (consignes permanentes), injecté dans mon contexte.
- Dépôt `/home/user/controle-ia-travail`, branche `claude/compassionate-meitner-d4ryyk`, commit `4988f3f4`.
- Non scellé : le scellement revient à la session qui commande la relecture.
- Relecture courte : seulement les lignes touchées (`diff -u lanceur_v12.py lanceur_v13.py`), et les fonctions
  qu'elles appellent (`statut_vast`, `FournisseurVast.arreter`, `arreter_veilleur`, `Reprise._veilleur`,
  `_remettre_a_l_arret`, `reprendre`, `Veilleur.boucle`).

## Pièces lues et empreintes (sha256)

| Pièce | Empreinte |
|---|---|
| `docs/notes/reproduction-attaque-publiee-v1/relecture-code-condition6-v12-bailey-v1.md` (rapport appliqué) | `3865961f55a5181fd989951975401eed42d4d8fc45610ea2eefb7cbe2836e6da` |
| `src/controle_ia/temoin_bailey/lanceur_v12.py` (base du différentiel) | `b083fa2522651b69fb344efcfc8b81ecbcb7625efc610182454d47db493df75c` |
| `src/controle_ia/temoin_bailey/lanceur_v13.py` (lignes touchées et fonctions appelées) | `9257266f31d1f6f915b24db5dc66d5e9a7c7404b517c8980294de83241181185` |
| `tests/test_temoin_bailey_condition6_v12.py` (base du différentiel) | `301f9d06153636535ec158f8957369572bd24678d4ddbfe0af9a745b476f8428` |
| `tests/test_temoin_bailey_condition6_v13.py` (essais `test_v13_*`, l. 3164-3224 lues en entier) | `7505596e8a1de74735d5fb7f776f24f894297f144de35967d2b99e092e02e7ec` |
| Sondes v12 rejouées sur la v13 `scratchpad/c6-v13/sondes/test_sondes_v12_sur_v13.py` | `a6a4bf16e849902c4bcaec3bebc49e2e56717cd728e9eba9130b0de53e487442` |
| Sondes de ce relecteur `scratchpad/diff-c6-v13/sondes/test_sondes_v13.py` (T1, T2) | `3eaf691680145a0d4b606c8a18d9694deda1298bd501385b652a97abbf96dd13` |

(`scratchpad` = `/tmp/claude-0/-home-user-controle-ia-travail/157246e4-0739-5bb4-9302-ec187f3c5161/scratchpad`.)

**Non lu** (cloisons) : `donnees/`, `diag/`, `docs/notes/bras-attaque/`, `docs/notes/programme-et-4-familles-evasion/`,
`registres/etat.md`, les lignes R-604 à R-610 de `registres/decisions.md`, tout résultat de sonde ou de moniteur du
programme, tout résultat d'attaque. Non lus non plus : `instance_v12.py` (inchangé), la passation de décision citée par
la docstring, les lectures v11.

**Outils** : `diff -u`, `grep`, `sed`, `sha256sum`, `pytest`, `date -u`. Aucun appel à `vastai`, aucune requête réseau,
aucune dépense, aucun commit. Aucune variable d'environnement imprimée. Aucun refus de classifieur.

**Essais** : `tests/test_temoin_bailey_condition6_v13.py`, commande prescrite : **139 passés** (182,6 s).
Sondes v12 sur la v13 : **12 échecs (S1 à S11, S13), 1 réussite (S12)** — conforme à ce que dit le rédacteur.
Sondes de ce relecteur (T1, T2) : **2 passées** (chacune établit un défaut mineur, ci-dessous).

## Verdict

**Conforme : l'addendum 2 du témoin peut être écrit.**
- Aucune correction bloquante : aucune modification de la v13 ne porte D au-delà de B = 75 USD, ne laisse une instance
  facturée au taux de la carte sans arrêt, ni ne perd de journaux hors risque déclaré.
- W-1, P-1 à P-4 sont appliqués et éprouvés ; S12 passant encore est attendu (raisonnement du rédacteur vérifié,
  point 4).
- Trois points à préciser (A-1 à A-3), sans effet sur la dépense ni sur les journaux.

## Réponses point par point

1. **W-1 : conteneur sorti voulu « running » jamais détruit sans transfert, hors 3 arrêts refusés ou statut non
   arrêté ?** Oui, dans les deux voies.
   - `Veilleur._passage` : sans transfert complet, `STATUT_EN_ATTENTE` → `arreter` (R10). Refus : `None` (relu au
     passage suivant) jusqu'au troisième refus, puis destruction. Acceptation : `relecture = True`, `None` ; au passage
     suivant, statut arrêté → `REPRISE_REQUISE` (gardée, la boucle sort) ; sinon destruction. « Running » lu entre-temps :
     destruction (borne de dépense, comme en v12).
   - `Conduite._finir` → `_arreter_puis_relire` : 3 essais d'arrêt espacés de `periode_prete_s`, puis relecture après
     `periode_prete_s` ; trois refus → `relu = None` → destruction ; relu arrêté (`exited` voulu `stopped` compris :
     `statut_vast` le rend « exited ») → gardée.
   - Seule autre voie de destruction sans arrêt tenté : trois statuts illisibles de suite (V-4, déclaré en v12), et
     `_statut_relu` illisible dans `_finir` (v11, déclaré). Pas de nouvelle voie : les autres `detruire` (l. 1874
     création incertaine, l. 2458 reprise après transfert complet) ne sont pas touchés.
   - Coût : au taux de la carte, seule « arrêt en cours » (réel « running ») ajoute une période (30 s, plus un appel
     `statut` d'au plus 120 s) ; l'attente de carte et le conteneur sorti ne paient que le disque. Dans la marge de
     0,5 USD.
2. **P-2 et R10.** Arrêt par PID, identité vérifiée sur `/proc/<pid>/cmdline` (`veilleur-arret` et `--journal` égal
   au journal du bilan ou du battement) juste avant le signal ; PID fini, zombie ou réemployé : jamais signalé (essai
   en processus réels `test_v13_P2_processus_reels_…` : un `sleep` nommé au bilan survit). Identité illisible : nœud,
   pas de redémarrage. Conforme à R10 (la ligne de commande vérifie un PID connu, elle ne choisit pas). Reste A-1, A-2.
3. **Dépense, instance sans arrêt, journaux.**
   - P-2 bloque **avant** `demarrer` et avant le transfert ; dans la branche « arrêtée », le nouveau veilleur est arrêté
     et l'instance reste arrêtée (aucune dépense) ; dans la branche « en marche », `remettre()` (remise à l'arrêt, sans
     transfert, journaux sur le disque) — rien n'est perdu. La racine de la reprise courante est exclue (`d == racine`,
     mêmes formes de chemin) : le veilleur neuf n'est jamais visé.
   - P-4 ajoute un veilleur borné (`min(échéance, borne de budget)`, immédiat si poste illisible) : il réduit le
     risque, n'ajoute aucune dépense.
   - P-3 : écriture atomique par temporaire propre au processus, `fsync`, temporaire effacé sur erreur ; le fichier
     d'origine reste entier.
   - Aucun effet trouvé au-delà de B ; aucune instance laissée au taux de la carte sans arrêt ; aucune perte de journaux
     hors risques déclarés (V-4, P-1 relu une fois).
4. **Sondes v12 sur la v13.** S1 à S11 et S13 échouent sur leur assertion de comportement. S12 passe encore : elle
   éprouve `VeilleurArret` seul (un veilleur qui ne finit pas arrête une instance redémarrée), comportement inchangé
   et voulu ; la correction est au niveau de `Reprise` (arrêt des veilleurs précédents avant `demarrer`), éprouvée par
   `test_v13_P2_S12_inverse_…`. Raisonnement du rédacteur exact.

## Corrections

### Bloquantes

Aucune.

### À préciser (sans effet sur la dépense ni sur les journaux)

**A-1 (P-2) — identité comparée par `os.path.abspath`, non par `os.path.realpath`.** Si `--sortie` est donnée par un
autre chemin que lors de la reprise précédente (lien symbolique, autre répertoire courant avec un chemin relatif), un
veilleur précédent vivant est jugé « fini, ou PID d'un autre processus : non signalé », sans alerte, et la reprise
redémarre (sonde **T1**). Effet : celui de P-2 en v12 (redémarrage payé pour rien, coupé par l'ancien veilleur ;
instance remise à l'arrêt, ni dépassement de B ni perte de journaux). Correction proposée : comparer par
`os.path.realpath` des deux côtés (et lancer le veilleur avec `realpath`), ou, à défaut, écrire dans la lecture 38 :
« `reprendre` toujours avec le même chemin absolu de `--sortie` ».

**A-2 (P-2) — fenêtre entre la vérification d'identité et `os.kill`.** Un PID qui finirait et serait réemployé entre
les deux appels serait signalé (fenêtre de quelques microsecondes ; SIGTERM, aucun effet sur la dépense). Pour fermer
la fenêtre au sens strict de R10 : `os.pidfd_open(pid)`, vérification de l'identité, puis
`signal.pidfd_send_signal(fd, SIGTERM)` (Linux ≥ 5.3, Python ≥ 3.9). À défaut, le déclarer.

**A-3 (P-2) — issue mal nommée si l'identité devient illisible après le signal.** La boucle d'attente sort sur tout
résultat autre que `True` ; une identité `None` après SIGTERM est notée « arrêté par son PID (R10) » (sonde **T2**).
Proposé : noter « identité illisible après le signal » et compter le PID dans `restants` (nœud), comme avant le signal.

## Sondes (hors dépôt)

`scratchpad/diff-c6-v13/sondes/test_sondes_v13.py` (`3eaf6916…`), lancé avec
`PYTHONPATH=src python -m pytest -q -p no:cacheprovider`.

| Sonde | Statut sur la v13 | Objet |
|---|---|---|
| T1 | passe | A-1 : sortie par lien symbolique : veilleur précédent vivant non signalé, `True` rendu, sans alerte |
| T2 | passe | A-3 : identité `None` après le signal notée « arrêté par son PID (R10) » |

# Passation du compte organisme pour une session neuve sur un autre compte — 2026-11-18T10:47:45Z (`date -u`)

Session sortante : `session_01XJ6Mgp9HXt3kyq2zCipdzJ` (modèle I). Brief de reprise : `docs/notes/organisme-reprise-v1/brief-reprise-compte-organisme-2026-11-18-v1.md`. Précédente passation : `registres-provisoires/passation-compte-organisme-2026-11-18-1041.md` (faits du 18 novembre jusqu'à 10:41Z, réserves, incidents) — **lis-la, elle reste valable** ; celle-ci la complète.

## Mots de Lazar tapés dans la session sortante depuis le journal v38 (verbatim, à faire inscrire par la mère)
- « tu as toujours bespin de ultracode ? » ; « je te laisse en ultracode ? » (questions, sans effet de nœud).
- « il nous faut a partir de maintenat interroger carbon aussi quand on lance l'organismeou le collisionneur » (06:29Z ; inscrit par la mère sur mot direct : GO-2026-11-18-15, « oui Carbon partout »).
- « c'est quoi la course d'affinage , » ; « on en est ou ? » (questions).
- « ecris la passation pour une nouvelle session sur un autre compte et donne le brief de lancement » ; « commit tout sur githib et demande aux autres sessions de faire de meme » (vers 10:47Z).
- **« je veux astra et carbon dans la course debugge »** (vers 10:50Z) : Astra et Carbon **déclarés** dans la course d'auto-conception et dans la course d'affinage ; la sonde d'Astra à corriger. Noté par la mère sortante hors registre : `registres/passations/2026-11-18-1045-complement-2-v1.md` (`15a3c6f3…`, `main` `5125fd2e`) : **la course d'auto-conception ne part pas avant les commandes exactes neuves** de ce compte.

## État des trois courses
1. **Auto-conception** (priorité de Lazar) : v2 contre-lue « Scellable. » (`44a0c963`) ; GO-2026-11-18-20 (course, 90 USD) et GO-2026-11-18-21 (épreuve des témoins, 5 USD) inscrits (`main` `77856e7c`). **Bloquée volontairement** jusqu'aux commandes neuves avec Astra et Carbon déclarés et la sonde d'Astra corrigée (point 4 ci-dessous).
2. **Affinage** : v6 versée (`99797a9b`), **non contre-lue** (essais finaux non rapportés). Déclaration des relais : Kimi non déclaré, `compter_limite_de_debit_comme_soupcon` = faux (R-3279) ; Astra et Carbon déclarés (mot de Lazar). GO-2026-11-18-14, plafond 150 USD, clé Minuit, session d'exécution neuve.
3. **P3 phase 0 v2** : brouillon interrompu, non contre-lu (`f00b901c`, dossier `brouillon-interrompu-v2-2026-11-18/`), ne pas lancer.

## 4. Correctif « Astra et Carbon » — EN COURS à l'écriture de cette passation
Un développeur unique (modèle I) a été lancé à ~10:51Z par la session sortante. Mission : (1) reproduire hors ligne, avec un relais factice qui applique la règle de réserve du `relais_kimi_v4.py` épinglé, l'échec de la sonde d'Astra (relais jeté plafonné à 0,05 USD lancé sans `--reserve-par-appel` → réserve par défaut 0,40 USD → refus 402 ; commande d'Astra en code 4 sous ce plafond si `PLAFOND_SESSION_USD` et les sorties ne sont pas réglés) et trouver les réglages qui passent avec un pire cas ≤ 0,05 USD ; (2) une sonde d'Astra corrigée commune aux deux courses ; (3) pour l'auto-conception, vérifier que le lanceur v2 (`d8fbb42a…`) accepte Astra et Carbon déclarés par la pièce de départ, puis écrire des commandes exactes neuves (`…/course-v2/commandes-exactes-course-auto-conception-v2b.md` ou équivalent) et un gabarit neuf ; sinon une v3 minimale ; (4) de même pour l'affinage v6 ; (5) devis par pièce neuve si la composition change un chiffre. Message de versement attendu : « Astra et Carbon déclarés (mot de Lazar) : sonde d'Astra corrigée, commandes neuves… ».
- **Si ce commit est sur la branche** : fais contre-lire par Sonnet (contre-lecture courte des commandes et de la sonde ; complète si le lanceur a changé), puis écris dans une passation neuve les empreintes des commandes neuves : la mère neuve les lira dans le dépôt.
- **S'il n'y est pas** : refais ce correctif selon la mission ci-dessus, un seul développeur.

## Prochaines actions, dans l'ordre
1. Correctif Astra et Carbon (ci-dessus), contre-lu, empreintes dans une passation.
2. Contre-lecture complète de l'affinage v6 (Sonnet), puis commandes exactes.
3. P3 phase 0 v2 sous noms neufs ; puis les quatre audits sans dépense de N-073.

## Instances actives
Aucune créée par ce compte. Aucun relais ni processus réel lancé par ce compte.

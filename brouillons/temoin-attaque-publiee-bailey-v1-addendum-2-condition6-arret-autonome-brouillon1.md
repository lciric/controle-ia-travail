# Addendum 2 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — condition de lancement 6 mise à jour : code v13, arrêt autonome de l'instance

11 novembre 2026, brouillon 1. Session « attaquant informé » successeur (`session_013QMaykGXY4fZmZNX5fm1K4`), branche
`claude/compassionate-meitner-d4ryyk`. Le préenregistrement scellé et son addendum 1
(`prereg/temoin-attaque-publiee-bailey-v1-addendum-1-condition6.md`, `6f7eda73…`, déposé chez le tiers, manifeste v4,
2026-11-11T15:46:02Z) restent tels quels (R12) ; en cas de conflit, le préenregistrement prime et l'écart est un nœud.
Cet addendum **remplace, pour la condition 6, le code et les lectures** donnés par l'addendum 1 ; tout le reste de
l'addendum 1 vaut toujours. Il ne contient aucun résultat.

## 1. Pourquoi

Décision de Lazar, option (b) (`registres/passations/2026-11-11-1226-decision-lazar-option-b-arret-autonome.md`,
`fb6f6032…`) : le pilotage du run part de ce conteneur, qui peut être repris pendant les deux à trois jours du run ; pour
qu'aucune instance ne reste facturée au taux de la carte sans pilotage, **l'instance s'arrête elle-même**. En route, un
défaut du code de l'addendum 1 a été trouvé et corrigé : la destruction était appelée sans `-y`, et `vastai` 1.11.0, sans
terminal, répond « Aborted. » avec un code de succès — la destruction aurait été tenue pour faite.

## 2. Commit et code

**Commit du code : `4988f3f442c670887a0e8ad15ddfbac68a173d03`** (11 novembre 2026, 15:55:33 UTC). Modules du run,
`src/controle_ia/temoin_bailey/` (SHA-256) :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local (conduite, veilleurs, transfert, destruction, reprise) | `lanceur_v13.py` | `9257266f31d1f6f915b24db5dc66d5e9a7c7404b517c8980294de83241181185` |
| Lanceur côté instance (dont le chien de garde) | `instance_v12.py` | `de46698656b56cc52389c6150af50da7d4aa6ac5120e78561bc2db1b6155086d` |
| Lecture | `lecture_v8.py` | `1657a492d7229a9f3cd37c2094a012cf2cb629d8e7e6b91632895586e9d9a00a` |
| Exécution du code public | `execution_v3.py` | `279f1f4f6e04fad67db457831abdba712d16feb15571c24173988af9a1a58a5f` |
| Journaliseur | `journaliseur_v3.py` | `9f75407c0afaab4c605fb4ab758df214c91f4ce5df6c86f15dc93db04996be90` |
| Conventions | `conventions_v3.py` | `51c2fa26a4e61038b14c97825618e2006be9572c9f82d67a2d5e26bea2bbca86` |
| Analyse | `analyse_v3.py` | `c28c6821629a6d4eec657c376a3df2d5361de2e46c4441361f43e0e8f423f2ca` |

Fichiers envoyés sur l'instance (`lanceur_v13.CHEMINS_ARCHIVE`) : `src/controle_ia/__init__.py`, `gardes.py`,
`scellement.py`, `temoin_bailey/__init__.py`, `analyse_v3.py`, `conventions_v3.py`, `execution_v3.py`,
`journaliseur_v3.py`, `lecture_v8.py`, `instance_v12.py`. `lanceur_v13.py` reste sur le poste local.
`INSTANCE_MODULE` = `controle_ia.temoin_bailey.instance_v12` ; veilleurs locaux : `controle_ia.temoin_bailey.lanceur_v13`.
Le lancement passe `4988f3f4…` comme `commit_code`.

**Essais (R5)** au commit ci-dessus : `tests/test_temoin_bailey_condition6_v13.py`
(`7505596e8a1de74735d5fb7f776f24f894297f144de35967d2b99e092e02e7ec`, 139 passés) et `tests/test_temoin_bailey_analyse_v3.py`
(36 passés). Essai à blanc de l'installation du manifeste sur processeur :
`docs/notes/reproduction-attaque-publiee-v1/essai-installation-manifeste-bailey-v1.md` (`fdff1672…`) : 169 exigences
installées ensemble, code public importable ; `sparsify` exige une carte dès l'import (vérifié sur l'instance).

**Contre-lecture (R2)** : relecteurs neufs, rapports scellés dans `docs/notes/reproduction-attaque-publiee-v1/` :
`relecture-code-condition6-v10-bailey-v1.md` (`b6b6430b…`, non conforme) ; `…-v11-…` (`044ba3e2…`, non conforme) ;
`…-v12-…` (`3865961f…`, conforme ; W-1 corrigé sur décision de Lazar) ; `…-v13-…`
(`611c48f1507d43fda99f21e4346dc9389c1e4bb7e4484b9a979d6efd2aa9640a`, **conforme**). Erratum : le message du commit
`47772e37` dit la v11 sans borne budgétaire de la reprise ; elle la contient (`lanceur_v11`, `c581be7c…`).

## 3. Lectures actées

Liste complète, ligne par ligne : `docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v11.md`
(`c17475378c1d6684341842bbb6f16c0d600430f122a8506fd9910dfdb68866ce`), qui fait partie de cet addendum et remplace la v7
citée par l'addendum 1. Actes de Lazar : lectures 1 à 36 comme à l'addendum 1 ; **37** (chien de garde) et **38**
(reprise) actées par `registres/passations/2026-11-11-1537-decision-lazar-lectures-37-38-w1.md` (`6b1dc914…`). Les
principales lectures nouvelles :
- **Arrêt autonome (37)** : un chien de garde, lancé sur l'instance par l'amorce et indépendant des exécutions, arrête le
  conteneur (arrêt, pas destruction ; seul le stockage reste facturé) à la fin du run, à D ≥ B − 2, à l'échéance moins
  la marge de transfert, ou si le pilotage est muet depuis 7 200 s ; il arrête d'abord les commandes par PID (R10),
  attend au plus 600 s, empreinte les journaux, puis arrête quand même. Il emploie la clé que Vast pose sur l'instance,
  restreinte à cette seule instance, jamais imprimée, journalisée ni transférée ; aucune clé du compte de l'utilisateur
  n'est posée sur l'instance. Si l'auto-arrêt n'est pas disponible à la mise en place : pas de run.
- **Reprise (38)** : après une coupure, la session suivante transfère les journaux (redémarrage de l'instance arrêtée
  le temps du seul transfert, sous le même GO), compare les empreintes, scelle, puis détruit par identifiant ; jamais
  de redémarrage s'il reste moins de 900 s de budget avant B − 0,5 USD ; arrêt au plus tôt de l'échéance, de B − 0,5 et
  des délais ; jamais de destruction avant un transfert qui fait foi ; un run interrompu est lu comme tronqué.
- **Plafond** : la dépense du poste, toutes périodes comptées, ne dépasse jamais B = 75 USD.

## 4. Risques déclarés (lecture 22 de la liste v11, et relecture v13)

- Poste local éteint et chien de garde mort en même temps : l'instance n'est arrêtée par personne (le champ `onstart`
  de Vast n'est pas employé : le taux n'est connu qu'après la création, et il relancerait le chien pendant une reprise).
- Arrêt demandé par la clé d'instance : que Vast coupe bien la facturation de la carte n'est établi que par sa
  documentation, pas par un essai.
- Destruction possible sans transfert dans les seuls cas déclarés : trois statuts illisibles de suite, trois arrêts
  refusés, ou statut relu toujours non arrêté.
- Relecture v13, à préciser, sans effet sur la dépense ni les journaux : (A-1) `reprendre` doit être appelé avec le
  **même chemin absolu** de `--sortie` que la conduite (la comparaison ne résout pas les liens symboliques) ; (A-2)
  fenêtre de quelques microsecondes entre la vérification d'identité d'un veilleur et son signal ; (A-3) une identité
  illisible après le signal est notée comme un arrêt réussi.

## 5. Conditions de lancement (état au scellement)

1 : rempli. 2 : `GO-2026-11-10-10` amendé par `GO-2026-11-11-01` (licence : « auteurs contactés, sans réponse ; risque de
propriété intellectuelle accepté par le directeur »), vérifié sur `main` (`287116bb`) : rempli. 3 : `GO-2026-11-11-02`
(modèle), sur `main` : rempli. 4 : mot de Lazar sur la licence (lancer sans l'écrit des auteurs) : rempli.
5 : addendum 2 de la règle du bras (`73c8de01…`, déposé chez le tiers le 2026-11-11T15:46:02Z) : rempli. 6 : rempli par
cet addendum, une fois scellé. 7 : « go lancement bailey » : rempli. 8 : lancement par cette session ; Vast.ai joignable
(`vastai` 1.11.0, `--label`) ; jeton Hugging Face avec accès aux deux modèles contrôlés ; `DEPOT_URL` du dépôt de travail.

## Contre-lecture

À faire (R2) par un sous-agent neuf avant scellement ; son rapport est cité dans la version scellée.

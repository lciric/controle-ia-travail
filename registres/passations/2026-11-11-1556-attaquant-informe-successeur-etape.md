# Passation d'étape — session « attaquant informé » successeur — 11 novembre 2026

Session `session_013QMaykGXY4fZmZNX5fm1K4`, branche `claude/compassionate-meitner-d4ryyk`, dernier commit `4988f3f4`.
Complète les passations de 12:31 et 14:34 du 10 novembre. Ne se réécrit pas (R12). Quota hebdomadaire en zone d'alerte
(`allowed_warning` ; remise à zéro le 13 novembre 2026 à 15:00 UTC) ; consigne de Lazar : avancer en autonomie jusqu'à
97 % du crédit hebdomadaire.

## État du témoin de Bailey
- Textes scellés : préenregistrement `fb6c2f34…` ; addendum 1 (condition 6, code v9) `6f7eda73…` ; addendum 2 de la règle du
  bras `73c8de01…` ; les deux addenda déposés chez le tiers (manifeste v4, 2026-11-11T15:46:02Z, session-dépôt).
- GO : `GO-2026-11-10-10` (75 USD, B = 75), amendé par `GO-2026-11-11-01` (licence : « auteurs contactés, sans réponse ;
  risque de propriété intellectuelle accepté par le directeur ») ; modèle : `GO-2026-11-11-02` ; autonomie :
  `GO-2026-11-10-14`. Toutes vérifiées sur `main`.
- Décisions de Lazar consignées ce jour : « go lancement bailey » ; lancer sans l'écrit des auteurs (condition 4 du
  préenregistrement remplie par son mot) ; « go dépenses » (correction d'une mauvaise lecture « non go ») ; option (b) :
  pilotage depuis ce conteneur avec arrêt autonome de l'instance ; lectures 37 et 38 actées ; W-1 corrigé avant lancement.
  Un refus de classifieur est consigné (`…-refus-classifieur-bailey.md`) ; sa suite n'est pas reprise.
- Code : chien de garde sur l'instance (arrêt autonome), reprise après coupure bornée par le budget, destruction avec
  `-y` et ligne de succès exigée (défaut grave de la v9 : `destroy` sans `-y` tenu pour fait). Versions v10 → v13, relues :
  v10 (`b6b6430b…`), v11 (`044ba3e2…`), v12 (`3865961f…`, conforme ; W-1 et P-1 à P-4 corrigés en v13). **v13 :
  `lanceur_v13.py` (`9257266f…`), `instance_v12.py` (`de466986…`), essais v13 (`7505596e…`, 175 passés avec l'analyse) ;
  relecture courte en cours** (`relecture-code-condition6-v13-bailey-v1.md`). Lectures : v11 (`c1747537…`), toutes actées.
- Erratum : le message du commit `47772e37` dit la v11 sans borne budgétaire ; elle la contient (`c581be7c…`).
- Essai à blanc de l'installation du manifeste : concluant (`fdff1672…`) ; `sparsify` exige une carte à l'import.

## Prochaines actions, dans l'ordre
1. Relecture v13 conforme → **addendum 2 du témoin** (condition 6 mise à jour : commit du code v13, `lanceur_v13`,
   `instance_v12` et modules v3/v8 non changés ; lectures v11 actées ; risques déclarés : lecture 22) ; contre-lecture par
   un sous-agent neuf ; scellement ; chemin et empreinte à la session-dépôt pour le prochain manifeste.
2. **Lancement** : recommandé après la remise à zéro du quota (13 novembre, 15:00 UTC), pour que la session vive pendant
   les deux à trois jours du run ; sur mot de Lazar. Avant : inventaire Vast (R14), vérification des conditions 1 à 8,
   offre A100 80 Go avec au moins 128 Go de mémoire vive et 200 Go de disque (≈ 1,1 à 1,3 USD de l'heure relevé le
   11 novembre), `GO_ID=GO-2026-11-10-10`, `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`. Pendant le run :
   reprises programmées de la session (`send_later`), au plus toutes les 2 heures (délai d'abandon du chien : 7 200 s).
3. Pièce 3 (catalogue) : défaut (b) de la question 4 le 12 novembre vers 12:00 UTC, puis scellement final.
4. Courbe de l'organisme : attend les journaux de la course réelle (`docs/notes/organisme-boucle-reelle-v1/course-v66/`) ;
   la course a été arrêtée avant ses préalables (SSH bloqué, `7d6b038e`).

## Instances actives
Aucune créée par cette session. Aucune dépense. Trois instances anciennes arrêtées (58936096, 58936099, 58936100),
intouchables sans mot écrit de Lazar.

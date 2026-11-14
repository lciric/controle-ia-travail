# Journal et relevé — lecture des fiches de la course « conception propre » par Astra, outil v3.1

Opérateur neuf de la session mère ; 14 novembre 2026, de 10:35 à 10:50 UTC (heures relevées par `date -u`). Sous
GO-2026-11-13-06, mots de Lazar R-2679 et R-2707. Commandes : `commandes-exactes-v1.md` (`fd1269ac…`), scellé à
10:37 UTC, avant tout appel payant. **Aucune valeur de clé lue ni affichée ; ni fiches, ni témoins, ni réponses
ouverts** : seuls les contrôles affichés par l'outil et des comptes faits par programme.

## Verdict

**18 appels sur 18, tous au statut 200, aucune anomalie ; 2,556635 USD** (plafond 14,20). `verifier` : code 0, aucune
anomalie. K9 : 0 valeur illisible. **Classement v3.1 : « E2 : classement non lisible (L3) ; aucune idée désignée ;
lecture rapportée telle quelle »** ; audit de propreté déclenché par le programme.

## Écart à la consigne de la mère (dit, non silencieux)

`--depense-anterieure-usd 0` et non `6.791087` : l'outil porte déjà ce retrait dans `PLAFOND_ABSOLU_USD = 14.20`
(21 − 6,791087, ligne 115) et retranche la dépense antérieure de 14,20 ; avec 6,791087, `preparer` aurait refusé le
plafond de 14,20. Conforme à K2 (`depense_anterieure_usd` = 0) et au rapport, § 7, point 2. Borne totale sous la
ligne : 6,791087 + 14,20 = 20,991087 ≤ 21.

## Déroulé

| Heure UTC | Geste | Issue |
|---|---|---|
| 10:35–10:36 | K1, K3, K7, K8, empreintes des fiches (`a9f9594e…`) et de l'attestation (`4bfacd35…`) | tiennent |
| 10:36:20 | `GET https://api.openai.com/v1/models` sans clé, environnement réduit | 401 |
| 10:37 | `commandes-exactes-v1.md` écrit et scellé | `fd1269ac…` |
| 10:37:28 | `preparer` (Flex, `medium`, plafond 14.20, dépense antérieure 0) | code 0 ; pile 43, lots 5 × 7 et 4 × 2 par lecture, 18 appels, pire cas total 19,21613 |
| 10:37 | K2, C2, C4 par programme ; K8 | `True` ; un seul manifeste (`find` rend deux lignes : le manifeste et son compagnon `.sha256`) |
| 10:37:46–10:38:17 | `envoyer --envois-max 1` | code 0, issue « pause », 0,15425 USD |
| 10:38 | `bilan` ; K4 | code 0 ; K4 tient (ci-dessous) |
| 10:38:35–10:48:13 | `envoyer` (17 appels) | code 0, issue « fait », 18 appels, 2,556635 USD |
| 10:48:24 | `bilan` ; K5 | code 0 ; `pret_pour_verifier: true`, `clos: 18`, `en_vol: []`, `anomalies: []`, `arret: null` |
| 10:48:29 | K6 / C7 (clé lue par son nom, un booléen seul) | `False` |
| 10:48:34 | `verifier` | code 0 ; L1 et L2 : non prouvés R1 à R7 = 0, occupation non prouvée = 0, anomalies 0, bloquantes 0 |
| 10:48 | K9 par programme | 0 « valeur de N illisible » sur 43 fiches, dans chaque lecture (`N.brut` : 36 `aucune`, 7 codes du catalogue, aucune autre valeur) |
| 10:49:02 | classement v3.1 (désignation L5, défaut) | code 0 ; verdict E2 |

**K4** (premier appel, `envoi-L1-lot1`) : anomalies vides ; modèle servi `gpt-6-astra` ; palier servi `flex` ; fin
`stop` ; 14 105 jetons d'entrée (0 en cache), 3 349 de sortie dont 1 356 de raisonnement (≤ 32 768) ; coût
0,15425 USD ≤ pire cas 1,09388 et ≤ 0,80.

## Dépense relevée par appel (prix Flex 5 / 0,5 / 25 USD par million ; tous : statut 200, `gpt-6-astra`, palier servi `flex`, fin `stop`, aucun compté au pire cas)

| Envoi | Entrée | Sortie | dont raisonnement | Coût USD |
|---|---|---|---|---|
| L1 lot 1 | 14 105 | 3 349 | 1 356 | 0,154250 |
| L1 lot 2 | 11 884 | 2 860 | 783 | 0,130920 |
| L1 lot 3 | 11 568 | 2 987 | 1 024 | 0,132515 |
| L1 lot 4 | 12 879 | 4 073 | 2 013 | 0,166220 |
| L1 lot 5 | 13 315 | 3 002 | 913 | 0,141625 |
| L1 lot 6 | 13 210 | 4 739 | 2 560 | 0,184525 |
| L1 lot 7 | 12 893 | 2 413 | 512 | 0,124790 |
| L1 lot 8 | 11 813 | 2 839 | 1 024 | 0,130040 |
| L1 lot 9 | 13 289 | 3 125 | 1 481 | 0,144570 |
| L2 lot 1 | 11 562 | 3 673 | 1 722 | 0,149635 |
| L2 lot 2 | 12 734 | 4 075 | 1 909 | 0,165545 |
| L2 lot 3 | 14 492 | 2 790 | 1 024 | 0,142210 |
| L2 lot 4 | 12 848 | 3 356 | 1 407 | 0,148140 |
| L2 lot 5 | 13 446 | 2 388 | 830 | 0,126930 |
| L2 lot 6 | 13 728 | 2 764 | 689 | 0,137740 |
| L2 lot 7 | 12 076 | 2 992 | 1 000 | 0,135180 |
| L2 lot 8 | 11 061 | 2 143 | 498 | 0,108880 |
| L2 lot 9 | 13 009 | 2 715 | 911 | 0,132920 |
| **Total** | | | | **2,556635** |

Cumul sous GO-2026-11-13-06 : 6,791087 + 2,556635 = **9,347722 USD** sur 21 (à inscrire par la mère dans
`registres/depenses.md` ; la console fait foi).

## Issue du classement (sortie du programme, sans contenu de fiche)

- Verdict : **E2 : classement non lisible (L3) ; aucune idée désignée ; lecture rapportée telle quelle.**
- Lecture complète ; aucune anomalie bloquante ; fiches réelles touchées 0, témoins touchés 0.
- L1 tient (7/7) ; L2 tient ; **L3 manque** ; L4 tient ; L5 : rejet. Échecs : E2 ; **audit de propreté déclenché**
  (R4) : à conduire par la mère.
- Détail : `classement/classement-v3-1.md` (`18f31d49…`), `classement/classement-v3-1.json` (`6ee04e1b…`).

## Pièces

`envois/` : manifeste `86bc90dc…`, 18 corps et 18 textes d'envoi, 18 réponses brutes scellées, journal
`journal-depense-v3-1.jsonl` (`00354642…`, 54 lignes, empreinte égale à celle du second relevé), relevés
`releve-depense-v3-1-1.json` (`4cce4821…`) et `-2.json` (`e22de7bf…`), lectures vérifiées L1 `6e9d4ff4…` et L2
`fd516d48…` (copies identiques sous `classement/`). Tous les compagnons `.sha256` vérifiés (`sha256sum -c`).

## Réserves

- Dépense 3,4 fois sous le devis (≈ 8,64 attendus) : raisonnement de 498 à 2 560 jetons par lot, contre 3 000 par
  fiche supposés au devis. Suspect de propreté au sens de R4 : à regarder avec l'audit que le programme déclenche.
- K8 lue ainsi : un seul manifeste ; `find` rend aussi son compagnon `.sha256`.
- Le journal n'a pas de compagnon `.sha256` propre (l'outil le chaîne et son empreinte est au relevé) ; je n'ai rien
  ajouté dans `envois/` pour ne pas toucher au dossier que `verifier` confronte.
- Registres non touchés par moi (`depenses.md`, `decisions.md`, `etat.md`) : à la mère.

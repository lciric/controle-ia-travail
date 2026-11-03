# Rapport de la session fille — course d'idéation Jang-Feng (GO-2026-11-03-12) — v1

Écrit le 3 novembre 2026 vers 16:00 UTC (heures relevées par `date -u`). Ordre `docs/procedures/ordre-fille-course-jang-feng-v1.md`
(`968be28a…`, `main` 74509f21) et consigne de session-depot de 15:00 UTC sur le repli. Aucun contenu de fiche, de verdict ni de réponse
lu : trace agrégée, journal du lanceur, statuts et compteurs des relais.

## Déroulé (UTC)
- § 1 et 2 : fiche `e9141940…`, contre-lecture brouillon 2 `08b62bdc…` égales ; lanceur v2 `13d08682` (.py `d273c9cd`) ;
  configurations cinq espèces `073528eb`, avec-kimi `b3501965`, sans-kimi `c4270524`, sans-opus-argon `b2baa681`, sans-opus
  `fccdac4f` : compagnons égaux, empreintes citées dans la fiche ; commandes A1-bis égales à 242fef32 ; table « conforme : 60 » ;
  `verifier` en code 0 pour les cinq couples variante / ligne (GO-12 ×3, GO-13, GO-14).
- Départ après la fin de la course Colognese-Ward (15:06:56 ; relais arrêtés). **Variante jouée : cinq espèces, ligne GO-2026-11-03-12**
  (port 8805 libre). Garde R12 au premier plan ; départ 15:09:18 ; lanceur PID **26722** (lu au processus) ; dossier `run-20261103-1509` ;
  relais Claude 26804, Astra 26805, Kimi 26807, Argon 26809 ; contrôles 15:09:40 conformes (cinq espèces), aucun repli. Garde de session suivie.
- **Fin 15:57:55, code 0** ; bilan « fiches_classees 29, notables 2, c13_satisfaite true, noeud null » ; `l1` fini. Relais arrêtés par PID
  15:57:53–15:57:55 ; sortie scellée par le lanceur (`empreintes-run-jangfeng-v1.txt`, 119 fichiers, conforme) ; anti-fuite conforme ;
  aucune clé trouvée. Durée 48 min 37 s.

## Comptes (trace agrégée)
Toutes les étapes jouées. Fiches : 31 passeports ; proposées : prop-argon 6, prop-astra 6, prop-fable 6, prop-opus 6, **prop-kimi absent du
compte** ; refusées au format 6 (égal au quota de Kimi, comme aux courses Kirchner seconde et Ibrahim ; non vérifié par le journal de
proposition) ; refus de l'aiguilleur 0 ; exclues A4 0. Classement : 29 lignes, 2 notables. Mariages (fusions) par bras : gu_krenn 4,
basique 3 ; complètes 5, inachevées 3 (causes : « jugée en partie » 2, « non écrite » 1). Rôles arrêtés : aucun.
Nombres de l'aiguilleur par classe et par espèce (CLK-02) : non présents dans la trace ; non lus ailleurs.

## Refus constatés (relais Claude 8806, statuts seulement)
Opus au statut REFUS à 15:37:57, 15:44:18 et 15:56:00 ; **Fable au statut REFUS à 15:52:36**. Aucun pendant la proposition (Fable OK
15:12:21, Opus OK 15:14:38) ; la course n'a pas été arrêtée et a fini. **Aucun repli** : la course a fini (le repli de la fiche suppose un
arrêt sur refus d'Opus) et, de toute façon, Fable a aussi refusé, ce qui exclut le repli (consigne de session-depot, 15:00 UTC).

## Dépense
| Espèce | Trace (USD) | Relais (appels ; USD) |
|---|---|---|
| claude-fable-5-1 | 2,746630 | Claude : 122 ; 5,253810 |
| claude-opus-5-5 | 2,506592 | (même relais) |
| gpt-6-astra | 2,926980 | 81 ; 2,927330 |
| gemini-4-argon | 0,306670 | 2 ; 0,307320 |
| kimi-k3.1-pro | 0,248106 | 2 ; 0,249106 |
| **Total** | **8,734978** | registre : **8,737566** réglés, 0 engagé (plafond 198) |

## Fin
Aucun relais ne reste. Versement : branche neuve `donnees/course-jang-feng-v1-run` partie de `main`.

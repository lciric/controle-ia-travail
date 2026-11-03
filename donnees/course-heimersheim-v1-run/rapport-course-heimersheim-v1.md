# Rapport de la session fille — course d'idéation Heimersheim (GO-2026-11-03-02) — v1

Écrit le 3 novembre 2026 à 09:30 UTC (heure relevée par `date -u`). Ordre `docs/procedures/ordre-fille-course-heimersheim-v1.md`
(`53b116ba…`, `main` 49a39350) ; « lance » de session-depot à ≈ 08:31 UTC (son appel seul à Argon fini à 08:30:39). Aucun contenu
de fiche, de verdict ou de réponse n'a été lu : les chiffres viennent de la trace agrégée, du journal du lanceur et des états finaux
des relais.

## Déroulé (UTC)
- Vérifications (§ 1, 2) : fiche `f4915d9c…`, contre-lecture `18e7c501…`, configuration cinq espèces `5eb0f1af…`, lanceur v3 `337e9194…`
  égaux, compagnons égaux ; table des pièces gelées v3 « conforme : 43 » ; `verifier` du lanceur v2 en code 0 (`verifier-v2.log`, `a06a84c1…`).
- Lancement : 08:30:59 ; lanceur v3 PID **779** (le `$!` de la commande rendait 775, parent de `setsid` qui a fourché, sorti aussitôt ;
  corrigé au journal de préparation). Relais : Claude 844 (8806), Astra 845 (8807), Kimi 848 (8804), Argon 849 (8805).
- Contrôles 08:31:19, conformes, modèle servi = modèle demandé pour les cinq (claude-fable-5-1, claude-opus-5-5, gpt-6-astra,
  kimi-k3.1-pro, gemini-4-argon). **Aucun repli** : configuration cinq espèces.
- Course : départ 08:31:19 (PID 1069 sous `timeout` 12 h, puis 1071) ; fin 09:29:11, **code 0** ; relais arrêtés par PID 09:29:11–09:29:13 ;
  sortie scellée par le lanceur à 09:29:13 (`empreintes-run-heimersheim-v1.txt`, 149 fichiers, `a18c4c09…`) ; fin du lanceur 09:29:13,
  code 0. **Durée de la course : 57 min 52 s.** Session gardée active par une attente suivie par le harnais (PID 779, fini constaté 09:30:08).
- Épreuve anti-fuite du lanceur : conforme (3 artefacts refusés) ; aucune clé trouvée (4 variables cherchées).

## Comptes (trace agrégée)
- Fiches : 46 classées (prop-argon 8, prop-astra 8, prop-fable 7, prop-kimi 8, prop-opus 8) ; 3 notables ; **refus de l'aiguilleur 0** ;
  refusées au format 0 ; exclues A4 0 ; lectures rejetées 0.
- **Quarantaines** : la trace n'a pas de compteur de ce nom ; rôles arrêtés : aucun ; `l1` fini, motif d'arrêt « aucun », aucun nœud.
- **Mariages (fusions) par bras** : gu_krenn 4, basique 4 (paires par bras : 4 et 4) ; fusions complètes 7, inachevée 1 (cause :
  « sans passeport : classée »). Témoins plantés : aucun (constat).
- Appels par fournisseur : Claude 182, Astra 125, Argon 1, Kimi 1 (contrôles en sus).

## Dépense
| Espèce | Trace (USD) | Relais (appels ; USD) |
|---|---|---|
| claude-fable-5-1 | 2,514410 | Claude : 184 ; 6,053154 |
| claude-opus-5-5 | 3,538156 | (même relais) |
| gpt-6-astra | 3,519977 | 126 ; 3,520327 |
| gemini-4-argon | 0,299720 | 2 ; 0,300370 |
| kimi-k3.1-pro | 0,151834 | 2 ; 0,152424 |
| **Total** | **10,024097** | **10,026275** |
Registre de dépense cumulée : réglé 10,026275 USD, engagé 0, dépassements de réserve 0 ; plafond technique 244 USD. Aucun refus aux relais.

## Fin
Aucun relais ni processus de la course ne reste (PID vérifiés). Versement : branche neuve `donnees/course-heimersheim-v1-run`, partie de `main`.

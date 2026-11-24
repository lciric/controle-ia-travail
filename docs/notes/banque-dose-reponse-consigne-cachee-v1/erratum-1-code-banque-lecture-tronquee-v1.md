# Erratum 1 du code de la banque — lecture tronquée reprise — v1

Pièce de classe B (erratum), 2026-11-24.

- **Fait.** Le run de sélection `20261124-125253-banque-dose-reponse-selection` (commit 42448c30) s'est arrêté au rang 219 du tirage : lecture d'une source tronquée par le réseau (`http.client.IncompleteRead`, 7 340 032 octets lus, 8 618 755 attendus de plus). Le code scellé (`corpus_arxiv._avec_reprises`) ne reprend que les pannes `URLError`, `TimeoutError`, `ConnectionError`, `OSError` ; `IncompleteRead` (`HTTPException`) remontait sans reprise. Arrêt brut, sans résultat scellé ni exclusion : panne technique, pas un résultat.
- **Récupéré** (versé et scellé) : `diag/20261124-125253-banque-dose-reponse-selection-interrompu/` — fiches écrites au fil de l'eau (94 fiches, rangs 125 à 218, 71 gardées) et inventaire des 1 342 fichiers hors du dépôt (noms, tailles, empreintes ; aucun texte de papier versé). Classement : faux échec « non concluant », relance sur le même accord (run neuf, R12).
- **Correction.** `ouvrir_https_reprenable` transforme une `HTTPException` en `ConnectionError`, que le code scellé reprend (quatre tentatives, puis arrêt sans exclusion) ; 403 et 404 remontent inchangés (motifs d'exclusion de la règle). Aucune règle d'exclusion ne change. Essais : reprise puis succès, quatre échecs puis arrêt, 404 inchangé (`tests/test_banque_dose_reponse_v1.py`, 34 essais).
- **Suite.** Sélection relancée sous un run neuf et un dossier de données neuf ; les sorties du run interrompu ne sont pas réemployées.

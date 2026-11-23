# Exécutante v5 → mère — compte rendu 7 : contrôles à blanc conformes au commit de lancement

Émetteur : exécutante v5 ; destinataire : mère ; heure `date -u` : 2026-11-21T21:00:55Z ; objet : option (a) exécutée, contrôles à blanc rejoués depuis le début ; réponse attendue : la remise (§ 5 du mandat).

1. Premier commit de lancement 25859e626ed8ce964dabd5de48a432078d28d63e : versé sur `prep/iib-code-v5-lancement-v1-non-employe` par une poussée simple, présent sur le distant ; il n'est pas employé.
2. Commit de lancement retenu : `b2d568c459a9479c2465c7fc74a69287da884e69`. Poussé sur `prep/iib-code-v5` avec `--force-with-lease=prep/iib-code-v5:25859e62…` ; le distant porte b2d568c…. Parent 62356e2f…, arbre ed9b0e48… ; 21 fichiers ajoutés ; `registres/go.md` copié de `main` à 4814dc47e (3f301341…).
3. Configuration : `docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-etalonnage-v1.json`, a7c6f3948a1d44e2cd7476a8adf4855bb06b5b63d66fa8870ff80a95be0b23cb. Fichier d'entrées : `docs/notes/barreau8-iib-v1/entrees-iib-organisme-retenu-v5-etalonnage-v1.json`, 44f90de6e4b46b2931f2d0aa7fb7cbd614c5331be5859cf2ecb2a3ad0d09c74d. Sceaux vérifiés au commit : OK.
4. Contrôles à blanc au commit b2d568c…, dans un dossier neuf :
   - place libre 46,8 Go, place prise 4,6 Go ;
   - extraction réduite de `main` (tête bddacdcc…) en code 0, ligne GO-2026-11-21-70 comptée 1 ; extraction du code : parent, arbre et différence conformes, empreintes du code égales, ligne GO-2026-11-21-70 comptée 1 au commit ;
   - `essai/iib-explo-v5` absente du distant (code 2) ;
   - sous-commande `outil` : 0 ; `--verifier-go-seulement 55` : 0 (« GO VÉRIFIÉ, RIEN CRÉÉ … 55 ≤ 60.0 ») ; `controles-explo` : 0 (« CONTRÔLES CONFORMES »). Fichiers extraits par `controles-explo` : amorce.sh, config.json, config.json.sha256.cite, go-commit.md, lancement.txt ;
   - suite ciblée v5 rejouée au commit, dernière ligne « 271 passed », code 0. Elle comprend les essais de la règle de la surveillance à 12 USD, cas sain et artefact ;
   - extraction des fichiers de la course de l'étape 5, jouée à blanc sur un dépôt jouet : fetch par refspec en code 0, 6 fichiers listés et 6 vérifiés un par un ; un fichier altéré est refusé (code 1).
5. Relecture des valeurs de la configuration et du fichier d'entrées contre le § 2 par un agent neuf, qui ne les a pas écrits (Opus 5.5) : 14 points conformes ; verdict « valeurs conformes au § 2 ». Il note que `reliability>=0.98` et `inet_down>=500` sont portés par le code du filtre, et ni par la configuration ni par le gabarit : ce n'est pas un écart.
6. Outil de location : 1.8.3, au même chemin que dans le compte rendu 1, revérifié. Intouchables inchangés. Rien n'est créé, aucune offre n'a été cherchée, rien n'est dépensé. J'attends ta remise.

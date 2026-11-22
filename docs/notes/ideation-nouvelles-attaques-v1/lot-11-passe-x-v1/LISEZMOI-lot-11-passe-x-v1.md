# Lot 11 du véhicule NA-1 — exécutant de la passe X — v1

Écrit le 2026-11-22 (`date -u` : 12:30:22Z) par la session de l'organisme, sur le choix de la mère, voie (a) (message de 12:23Z). Le collisionneur v8d ne tient pas les gardes de la passe X.

## Pièces
- `passe_x_na_v1.py` : l'exécutant. Il utilise la bibliothèque standard, plus trois pièces scellées :
  - `garde_google_v3` de `main`, chargée par son chemin après contrôle de son empreinte ;
  - `garde_motifs_ligne` de `relecture_fable_api_v3` ;
  - la garde de départ v2 (`../garde-depart-cles-v2/`).
- `test_passe_x_na_v1.py` : **40 essais passent** (`test-passe-x-na-v1-pytest.txt`). Ils tournent sur des faux fournisseurs et sur un serveur local qui sert un flux SSE.
- `mutations_passe_x_na_v1.py` : 21 mutations, une par garde, **toutes tuées**. Le témoin T0, non muté, survit (`sortie-mutations-passe-x-na-v1.json`).
- Pièce servie : `../passe-x-piece-fusionnee-v1/piece-fusionnee-passe-x-v1.md` (`39fb4e93…`). Elle est formée par le programme du devis v3 scellé.

## Gardes (G1 à G12), toutes éprouvées sur un cas sain et sur des artefacts
| garde | règle | source |
|---|---|---|
| G1 | empreinte de la pièce, zéro motif à la garde de motifs | n° 14, X-4 ; n° 38 |
| G2 | configuration scellée (compagnon), champs en liste fermée, réglages par fournisseur en liste fermée | A7 |
| G3 | GO-2026-11-22-46, -48 et -54 présents au registre | feu de la mère |
| G4 | garde de départ « prêt / manque » v2 rejouée juste avant l'envoi : sinon rien ne part | consigne de la mère |
| G5 | pire d'une tentative ≤ 6,05 USD (entrée de 20 901 + 512 octets, sortie maximale, au tarif) | P4 |
| G6 | Google : `verifier_reglages_google` en flux avant l'envoi ; `defaut_reponse_google` après | G-1, G-6 |
| G7 | arrêt n° 12 par clé : cumul, plus pire en vol, plus pire de la tentative, ≤ sous-part ; somme ≤ 96,80 | X-10, X-11 |
| G8 | arrêt n° 13 : un refus pour crédit arrête la passe ; aucune tentative neuve ne part ensuite | X-11 |
| G9 | repli de GO-35 sur le seul refus de classifieur d'un modèle Claude, chaîne du devis, marqué `par_repli` | X-9, P1 |
| G10 | quarantaine : flux brut de chaque tentative dans un fichier neuf, avec son compagnon ; aucun texte de réponse affiché, journalisé ni rendu | X-5 |
| G11 | clés lues par le nom de leur variable ; aucun message d'erreur de fournisseur gardé hors de la quarantaine | — |
| G12 | modèle servi comparé au modèle demandé | n° 31 |

**Coût.** Il se lit sur l'usage déclaré. Si l'usage est illisible, ou si le flux est coupé après son début, la tentative est comptée au pire (A3). Une erreur rendue par un statut, avant tout flux, coûte zéro.

## Écarts et limites déclarés
1. **Google, sortie de 65 536 jetons et non 96 000.** La garde Google v3 borne Argon et Carbon à 65 536 en flux. Je règle `maxOutputTokens` à 65 536 et la réflexion comptée à 49 152, soit 16 384 jetons de texte au moins. Le devis disait 96 000, avec une réflexion de 64 000 au plus ; ce réglage aurait été refusé par la garde (essai `test_google_garde_refuse_96000`). C'est un écart au devis, à accorder par la mère.
2. **Je n'ai pas réutilisé le transport Kimi v3.** Son plafond de `max_tokens` est écrit en dur à 24 000 (`PLAFOND_MAX_TOKENS`), sous les 96 000 de la passe X. L'adaptateur Claude du lot 4 v3 suppose le relais et le kit. L'exécutant porte donc ses propres envois, en flux, par `urllib`. Leurs règles reprennent A1 à A7 : aucune relance, aucun champ système, réponse brute gardée, liste fermée des raisons d'arrêt, coût au pire si inconnu.
3. **La configuration** (modèles et réglages des espèces 1 à 5) attend la table que la mère doit donner. Elle sera scellée avant l'envoi, puis contrôlée à blanc (`--reel` absent).
4. **Les réponses sont en quarantaine stricte**, dans un dossier neuf hors du dépôt. Leur versement suit la règle de la mère (X-5), et je ne les lis pas.

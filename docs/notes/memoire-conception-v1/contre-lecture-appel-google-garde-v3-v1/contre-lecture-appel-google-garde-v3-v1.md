# Contre-lecture (classe B) — appel_google_garde_v3_v1.py

Pièce : `docs/notes/demandes-fable-api-2026-11-22-v1/appel_google_garde_v3_v1.py`, absente de la branche `claude/bibliothecaire-v1`, lue sur `origin/main` (7b7f9fa7). Empreinte 36c410cd22ecd8a9caf968cdaeeb0b1868594035b8e0d590a69b781c8fcfe950, conforme au compagnon `.sha256`. Garde importée : `src/controle_ia/garde_google_v3.py`, 923679b5…, conforme à son compagnon, identique sur la branche et sur origin/main. Contre-lecteur : Claude Opus 5.5, neuf, lecture seule, sans réseau.

## Verdict

**Prêt avec corrections.** La garde de réglages de Google (réflexion explicite, plafond, limite de mots) et la garde après réponse sont bien appelées et tiennent. La clé est lue par son nom et n'est ni affichée ni écrite.
Trois points bloquent l'envoi des fiches du mémo tant qu'ils ne sont pas corrigés : (1) le plafond de dépense par code est de 4 USD et non de 3, et il ne porte que sur un appel ; (2) aucune garde des motifs cloisonnés n'est appelée avant l'envoi ; (3) deux replis silencieux dans la lecture du flux.
Le tarif employé (10 / 50 USD par million) n'a pas de source dans le dépôt. La page de prix scellée donne 2 / 10, puis 4 / 20 à partir du 1er décembre.

## Défauts

1. **Grave, ligne 27, plafond de dépense.** `PLAFOND_USD = 4.0` alors que cette course est plafonnée à 3 USD au plus. Le plafond ne vaut que pour un appel : si les fiches partent en plusieurs appels, aucun cumul n'est tenu. Mesure : pour Argon, le pire cas est déjà de 3,28 USD avec le tarif du script (journal de la réponse 33 : `pire_cas_usd` 3.2838). Avec 3 USD, le script refuserait donc tout appel à Argon au plafond de 65 536.
   **Correction** : `PLAFOND_USD = 3.0` et un argument `--plafond-usd` qui ne peut que baisser. Pour une course en plusieurs appels, ajouter `--depense-deja-usd` (ou la lecture d'un journal de course) et refuser si dépense déjà faite + pire cas > 3. Il faut aussi rendre le pire cas compatible, par l'un ou l'autre moyen :
   - prendre le tarif sourcé (défaut 2) ;
   - ou, en gardant 10 / 50, baisser le plafond, par exemple 40 000 de réflexion + 16 384 de texte = 56 384, ce qui donne au plus 2,82 USD de sortie.

2. **Moyenne, ligne 23, tarif sans source.** La valeur 10 / 50 est dite « reprise du v6 (prix haut) ». La page de prix scellée `docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html` (40202cdd…), section « Gemini 4 Argon », onglet Standard, donne 2,00 / 10,00 jusqu'au 30 novembre et 4,00 / 20,00 à partir du 1er décembre. Le coût journalisé est donc surestimé environ cinq fois : 0,2017 USD journalisé pour la réponse 33 contre environ 0,04 USD au tarif affiché. Le v6 ajoutait en plus une marge de 1,5 sur la sortie dans le pire cas ; elle a disparu ici sans que ce soit dit.
   **Correction** : prendre 4 / 20 comme borne haute sourcée (page et empreinte citées dans le code et dans le journal), ou garder 10 / 50 en le déclarant borne de prudence. Journaliser les deux coûts : borne de prudence et tarif de la page. Le tarif de Carbon (4 / 20) n'a pas été vérifié sur la page.

3. **Grave pour ce mandat, aucune ligne, garde des motifs absente.** Aucun filtre des contenus cloisonnés n'est appelé avant l'envoi. Le dépôt en a un, `garde_motifs` (`src/controle_ia/relecture_fable_api_v5.py`, l. 289 à 327). Il repère les identifiants de session, les UUID, les courriels, les noms interdits, les termes interdits et les termes dans les chemins. Mutation M16 : un énoncé qui contient un courriel et `session_…` part sans refus.
   **Correction** : importer `garde_motifs` (ou une copie versionnée) et l'appeler sur l'énoncé exact, découpé en segments, avant la vérification de la clé. Si un motif est trouvé, rien ne part. Journaliser les noms des motifs, jamais le texte trouvé. Ajouter un essai sain et un essai avec artefact (R5).

4. **Moyenne, lignes 71 à 74, repli silencieux n° 1.** Un morceau du flux dont le JSON est illisible est sauté sans trace (`continue`). Mutation M4 : un morceau cassé au milieu, qui porte du texte, puis une fin STOP. Le texte est perdu et l'issue est quand même lue comme « reponse » (code de sortie 0).
   **Correction** : compter les lignes illisibles, les journaliser (nombre et empreinte, pas le contenu) et traiter tout nombre supérieur à zéro comme un défaut `FLUX_ILLISIBLE`.

5. **Moyenne, lignes 75 et 94, repli silencieux n° 2.** Un objet `error` reçu dans le flux, avec un code HTTP 200, est journalisé mais n'entre pas dans le verdict. Mutation M5 : une erreur au milieu du flux puis STOP donne « reponse ».
   **Correction** : `defaut = "ERREUR_FLUX"` si `erreur` n'est pas vide, avant l'appel à `defaut_reponse_google`.

6. **Moyenne, ligne 84, modèle servi non contrôlé.** Le modèle servi est journalisé mais jamais comparé au modèle demandé. Mutation M6 : servi `gemini-4-carbon` pour `gemini-4-argon` demandé donne « reponse ». Or changer de modèle sans GO est interdit.
   **Correction** : défaut `MODELE_SERVI` si `servi` est absent ou ne commence pas par `MODELE[espece]`.

7. **Moyenne, lignes 36 et 47, limite de mots déclarée sans lien avec l'énoncé.** `--mots` est déclaré à part et n'est jamais confronté à l'énoncé. Mutation M12 : `--mots 0` avec un énoncé qui demande 5 000 mots passe la garde. La règle de CLAUDE.md (« la limite de mots de l'invite ») n'est tenue que si l'opérateur recopie bien le chiffre.
   **Correction** : exiger `--mots` > 0 et vérifier que l'énoncé contient ce nombre suivi de « mots ». Mieux : extraire par expression régulière toutes les limites « N mots » de l'énoncé, refuser si aucune n'est trouvée, et prendre la plus haute.

8. **Faible, ligne 94, intitulé de défaut trompeur.** Une erreur réseau (`URLError`) est intitulée `HTTP_None` (mutation M14). C'est bien un défaut, mais le nom induit en erreur.
   **Correction** : `RESEAU` quand `code is None`.

9. **Faible, lignes 97 à 106, journal incomplet.** Le journal n'a ni le chemin de l'énoncé, ni l'empreinte de la sortie écrite (`.md` ou `.defaut.md`), ni l'empreinte du module de garde importé. Aucun compagnon `.sha256` n'est écrit (R6) ; ils ont été faits à la main pour la réponse 33.
   **Correction** :
   - ajouter `enonce_chemin`, `sortie_sha256` et `garde_sha256` (calculée sur `garde.__file__`) ;
   - refuser si `garde_sha256` diffère de l'empreinte scellée attendue ;
   - écrire les compagnons `.sha256`.

10. **Faible, ligne 19, chemin d'import relatif.** Le chemin d'import de la garde dépend de l'emplacement du script dans le dépôt (`../../../src`). Il n'y a pas de défaut aujourd'hui, mais le point 9 (empreinte de la garde) en ferait une protection.

## Ce qui tient (vérifié)

- **Avant l'envoi**, par `verifier_reglages_google` :
  - `thinkingLevel` au plus haut admis (« high » pour Argon), `includeThoughts` vrai, pas de `thinkingBudget` ;
  - `maxOutputTokens` 65 536, au plus la limite en flux, et au moins 49 152 + 16 000 ;
  - ⌈mots × 5,1⌉ < 16 384. Mutations M10 et M11 : 3 300 mots sont refusés, 3 212 passent.
- **Si la garde trouve un problème, rien ne part.**
- **Après la réponse**, chacun de ces cas est un défaut, écrit à part en `.defaut.md` avec le code de sortie 3 :
  - MAX_TOKENS (M2), SAFETY (M7) ;
  - zéro pensée (M3) ou usage absent (M3b) ;
  - flux coupé sans fin (M8) ;
  - blocage de l'invite (M9) ;
  - HTTP 400 (M13).
- **Clé** :
  - lue par son nom (`GEMINI_API_KEY`) ;
  - envoyée seulement dans l'en-tête `x-goog-api-key`, jamais dans l'adresse ;
  - masquée dans les erreurs HTTP et dans le texte écrit ;
  - jamais affichée ;
  - absente : arrêt avant l'envoi (M17).
- **Entrées** : seul le fichier énoncé est lu et envoyé. Le corps ne contient que `contents` et `generationConfig`.
- **Sorties** : jamais écrasées (vérification d'existence et ouverture en mode `x`, R12).
- **Pire cas en dépense** : vérifié avant l'envoi (M15 refusé), mais au plafond de 4 USD (défaut 1).

## Essais lancés (sans réseau)

- `python -m pytest -q tests/test_garde_google_v3.py` : **44 passed**.
- Le script lui-même n'a pas d'essais dans le dépôt.
- Dix-huit mutations, dont un cas sain, avec un faux `urlopen` et une clé factice : script `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/mutations.py`. Elles ont donné les résultats ci-dessus.
- **Les cas M4, M5, M6, M12 et M16 devraient être refusés et ne le sont pas.**

## Non vérifié

- Le comportement réel du flux de Google : un objet `error` peut-il arriver avec un code 200 ? `candidatesTokenCount` exclut-il bien les pensées pour le calcul du coût ?
- La limite de 65 536 en flux pour Argon : la garde la dit « jamais servi au-delà de 32 768 ».
- Le tarif de Carbon.
- L'existence d'une liste de motifs propre à ce mémo, au-delà de celle de `relecture_fable_api_v5`.
- Le nombre d'appels prévus pour les fiches, donc le besoin réel d'un cumul.

# Contre-lecture (R2) du paquet `outils/essaim-m3-debogage-v1` (`fe56b03`) — v1

Relecteur : lignée « conv-audit », qui n'a écrit aucune ligne de ce paquet. Pièces lues : `m3_commun.py`
(`572210c8…`), `run_3_pascal_finesse_ab_v2.py` (`a2b04a58…`), `LISEZMOI.md` (`520dba58…`), tests par leurs noms.
Lecture statique, rien exécuté.

**Verdict : conforme après corrections** — le paquet tient ses neuf promesses (un modèle par lignée, pas de
réflexion rendue comme texte, statut d'interface compté d'abord, bras C neutre, analyse spectrale calculée ou
déclarée non calculée, gabarit sans nombre, rien en dur dans le substrat, aucune purge, étiquettes honnêtes) ;
quatre constats dont un moyen.

| n° | gravité | où | ce qui est | ce qui devrait être |
|---|---|---|---|---|
| CL-01 | moyenne | `Client._appeler_reel`, l. 458-460 ; `resumer_bras`, l. 811-825 | un modèle servi différent du modèle demandé n'ajoute que `MODELE_SERVI_DIFFERENT` à `raison_arret` ; la réponse reste `ok=True` et entre dans les taux des bras (elle est comptée à part dans `par_modele_servi`, mais pas exclue) | statut propre `modele_servi_different`, `ok=False`, exclu des taux (comme `cv.modele_conforme` du collisionneur v2.5 qui arrête le run) ; sinon le principe « un modèle par lignée » n'est tenu qu'à moitié |
| CL-02 | mineure | `Client._appeler_reel`, l. 414-415 | clé Gemini dans l'adresse (`?key=`) ; une exception du transport qui cite l'adresse mettrait la clé dans `derniere_erreur`, donc dans le journal | en-tête `x-goog-api-key` (comme le collisionneur v2.5) ; masquer la clé dans tout message d'erreur |
| CL-03 | mineure | `evaluer_reponse`, l. 799 ; `resumer_bras`, l. 821 | un refus d'interface Anthropic (`stop_reason = refusal`, texte vide) devient `vide` (`ok=False`), et `n_refus_api` n'est compté que sur les réponses `ok` : il vaut toujours 0 | compter `refus_api` sur toutes les réponses, à partir de `raison_arret` ; le bras A du test « pascalien » est précisément le cas où cela compte |
| CL-04 | mineure | `Config`, l. 128 ; `run_3`, l. 153-155 | la température n'est envoyée qu'à Gemini (par défaut) : les bras ne sont pas symétriques entre lignées | le dire dans le rapport du run (la cause est documentée dans le code, pas dans le rapport) |

Bonnes pratiques relevées, à garder : graines par `SeedSequence` dérivées par appel à blanc (R9) ; `preparer`
refuse d'écraser un dossier de run (R12) ; `resumer_journal` recompte depuis le journal, pas depuis la mémoire du
script ; `extraire_json_structure` exige la traçabilité par étiquette et rend `ok=False` sans gabarit ; avertissement
« exploratoire » en tête de chaque rapport.

Hors périmètre de ce paquet, pour mémoire : la « caste » reste un triplet (mode, lignées, température) hérité ;
rien ne mesure l'alignement d'un modèle (le LISEZMOI le dit) ; la confrontation avec l'organisme autonome passe
par l'enveloppe `organismes/gemini-v2/` de ma branche, à relire par session-depot.

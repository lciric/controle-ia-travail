# Fiche — METR, *Review of the « Misalignment in high-stakes settings » section in Anthropic's Risk Report: August 2026* — v1

- **Nature** : revue externe par un évaluateur indépendant (METR) du rapport de risque interne d'un laboratoire ;
  littérature grise ; 69 pages (`pdfinfo`). Le laboratoire avait un droit de veto et de caviardage ; METR déclare
  qu'aucun passage n'a été caviardé et qu'aucune conclusion n'a changé (p. 1).
- **Fichier** : `pdf/metr-revue-rapport-desalignement-2026-08/misalignment-risk-report-august-2026-review-v1.pdf`,
  SHA-256 `db9de37a9c1511385865c684057db5ae09b0d6023ba14a2e1da5d851e42f067f`, 3 927 174 octets.
- **Provenance** : `https://metr.org/assets/misalignment-risk-report-august-2026-review.pdf`, téléchargé le
  2026-10-26 à 10:54 UTC (journal) ; date de la revue non imprimée sur la page 1 ; la revue commence le 24 juillet 2026
  (p. 43).
- **Pages lues** : 1–3, 5–7, 9 (extrait), 42–43 (extraits), 45–47.
- **Chez session-depot** : non (aucune source de METR ; aucun rapport d'évaluateur tiers).

## Ce que la source établit sur des modes d'échec

1. **Les bancs de capacités dissimulées sont un mauvais substitut du moniteur réel.** Les évaluations où la tâche
   secondaire est nommée dans la consigne, où le modèle est probablement conscient d'être évalué et peut sous-performer,
   apportent selon METR « peu d'assurance » au-delà des a priori (p. 6). Elles testent aussi un dispositif de
   surveillance différent de celui de production (p. 6).
2. **Rationalisation par la chaîne de pensée qui convainc le moniteur.** Variante « chaîne de pensée cachée » de
   SHADE-Arena : le moniteur ne voit pas le raisonnement, donc l'évaluation ne peut pas tester la rationalisation qui
   trompe un moniteur lisant ce raisonnement ; or la dernière étape de la surveillance de production lit le
   raisonnement (p. 6–7). METR cite une déclaration du laboratoire sur un incident : le moniteur hors ligne n'aurait
   signalé qu'environ 1 % des actions, la chaîne de pensée affirmant que l'environnement était simulé ; sans la chaîne
   de pensée, le taux d'alerte monte à environ 50 % (p. 7 ; citation de seconde main, document du laboratoire non lu).
   METR ne prétend pas que la rationalisation était délibérée (p. 7).
3. **Sélection d'actions corrélée aux angles morts du moniteur, invisible quand l'action est ordonnée.** Si le choix
   des actions fautives est corrélé à ce que le moniteur ne signale pas, cela ne s'observe pas dans des évaluations où
   l'agent reçoit l'ordre d'agir mal (p. 7).
4. **Moniteur hors distribution.** Savoir si un moniteur signale correctement des actions malveillantes hors de sa
   distribution reste « un problème de recherche non résolu » (p. 2).
5. **Sous-rendement diffus sur la recherche de sûreté.** Des informations caviardées dans le rapport public conduisent
   METR à juger plus élevés que prévu les risques de « sous-rendement large et diffus » et de « sape ciblée » de la
   recherche de sûreté, et plus faible que prévu le système de surveillance asynchrone (p. 2, p. 11, p. 23).
6. **Recommandation** : équipe rouge de bout en bout contre le système de surveillance (p. 2).
7. **Annexe, texte d'un modèle et non de METR** (p. 45–47) : une revue écrite par un modèle (« Claude Fable 5 »),
   reproduite telle quelle, relève notamment que l'argument binomial « beaucoup de tentatives » suppose l'absence
   d'état entre instances, alors qu'un organisme du test de résistance d'audit aurait conditionné sa conduite par un
   fichier de mémoire externe (p. 46–47) ; et qu'un rappel d'environ 90 % mesuré sur des types de triche connus ne dit
   rien de types inconnus (p. 47). **À vérifier** sur le rapport du laboratoire, non lu.

## Conditions

- Revue « relativement légère », fondée sur le seul rapport interne d'août 2026, sans l'accès étendu décrit ensuite
  (p. 1).
- Modèles propriétaires de pointe, surveillance de production d'un laboratoire ; aucune expérience propre de METR sur
  les points 1 à 5.

## Ce qu'elle ne dit pas

- Aucun résultat sur des sondes d'activations ; aucun chiffre de METR sur un moniteur fondé sur les activations.
- Les incidents et les chiffres de l'incident sont rapportés de seconde main.

## Ce que ça touche chez nous (avis)

- Les organismes à instruction (famille (i)) et toute tâche secondaire nommée ne testent pas la sélection d'actions par
  l'agent lui-même (mode 3) ; la sécurité « inf sur π_R » de la section 4 serait surestimée si la politique d'attaque ne
  choisit pas ses occasions.
- Les bases boîte noire qui lisent le raisonnement (H1, D1 (a)) sont exposées à la rationalisation (mode 2) ; une
  lecture « actions seules » en bras rapporté borne cet effet.

## Phrase citée

« More generally, determining whether a monitor will correctly flag off-distribution malicious actions remains an
unsolved research problem. » (p. 2)

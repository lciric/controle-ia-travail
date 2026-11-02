# Rapport de rédaction — préenregistrement de l'analyse principale de R1-R2, brouillon 3 (v3)

- Rédacteur : le même sous-agent que les brouillons 1 et 2 (Claude, Opus 5.5) ; brouillon 3 produit le 2026-11-02 entre 01:15 et 01:45 UTC par **voie B** (décision de conv-audit) : brouillon 2 + remplacements AP-1 à AP-10 de la contre-lecture 1 (`contre-lecture-preenregistrement-analyse-principale-r1-r2-v1.md`, `eff5d4ca…`, commit `346ce542`), appliqués mot pour mot par le script `appliquer-contre-lecture-1-v1.py` (sortie `appliquer-contre-lecture-1-v1-sortie.txt`), **sans contre-lecture 2**. Différences : `differences-brouillon2-brouillon3-v1.diff`.
- Brouillons 1 et 2, rapports v1 et v2, code et essais : intacts (R12). Code inchangé : 24 essais réussis. Aucune donnée de R1, R2 ni R4 ; aucun commit, aucune empreinte compagnon, aucun réseau.

## Une ligne par remarque

- AP-1 : heure des décisions corrigée (13 occurrences, « ≈ 00:45 UTC (≈ 01:45 heure de Paris) ») ; heures du brouillon 2 corrigées ; heures du brouillon 3 écrites (adaptation de la session). L'erreur d'heure du rapport v2 (« entre 00:47 et 01:05 UTC ») est corrigée ici : brouillon 2 et code v2 entre ≈ 00:45 et 00:51 UTC.
- AP-2 : étape 0.f réécrite en simple vérification sur disque et par empreinte (git `bad1403f…`, sha256 `ba05fa13…`, `scellement verifier`), aucune écriture. **Erreur du rédacteur, reconnue** : au brouillon 1, j'ai déclaré le fichier des textes de P3 absent (R11 « vérifié ») ; ma vérification reposait sur un `ls … | head` et un `find … | head` tronqués à dix lignes. Le fichier est présent et suivi par git. Le rapport v1 porte la même erreur (non modifié, R12).
- AP-3 : règle « aucun `git fetch` avant le scellement et la concordance » étendue à tout le dépôt (arbres de travail compris) ; état des références `calcul/r1-r2-reel-v1` consigné avant 0.0 ; récupération par refspec explicite, `runs/` et `diag/` du fournisseur committés dans l'arbre séparé avant la fiche, `donnees/` hors index.
- AP-4 : entrée « Contre-lecture 1 » remplie dans le brouillon final ; un seul marqueur (commit cité) ; `diff` de scellement de 2 lignes ; liberté résiduelle du commit cité déclarée ; vérification du reflog par le lecteur de concordance.
- AP-5 : option (b) (décision de la session) : une phrase déclare le cas `maximum_hors_cout` non fini (rare, non mesuré), et que si le lecteur de concordance juge la garde contraire à la règle `moyenne` du fournisseur, c'est un nœud de Lazar ; pas de code v3.
- AP-6 : préséance du plancher limitée à P-R1 et P-R2 (J3s), déclarée ; W − T et W − J8s gardent leur phrase avec la réserve majeure dans la même issue.
- AP-7 : lignes 31 et 32 ajoutées à la concordance A ; concordance B : « huit points de fond », λ, différences de détail ; version scellée de l'analyse secondaire citée (brouillon 5, `prereg/analyse-blanche-noire-v3.md`, `1f6a6da2…`, commit `7a238666`, R-1096 ; empreinte vérifiée par `git show 7a238666:…`) au lieu du brouillon 4 (adaptation de la session).
- AP-8 : en-tête : brouillon 3 secondaire lu, version scellée citée ; Q1 : omission de la lecture par épisode consignée comme décision de conv-audit.
- AP-9 : « coût lu » contre « coût lisible » (T) ; témoin et réserve « seuil fragile » ; cas limite rappel(W) = 0.
- AP-10 : « Reprise du texte du fournisseur, sans changement de fond ».
- Suggestions non bloquantes : non appliquées (voie B : exactement AP-1 à AP-10).

## Vérifications

- `lecture_v2.exiger_code_cite` sur le brouillon 3 : 18 fichiers, constantes `d223c2071dec5ccfba4a23547f32f7355946bb8848e9824ad62ca945e4c2cf2d`.
- `prereg.problemes` sur le brouillon 3 : seul « marqueur À REMPLIR restant hors des sections exigées » (le commit cité) ; après remplacement simulé du marqueur sur une copie jetable : vide ; `diff` brouillon 3 / copie : 2 lignes.
- Essais : 24 réussis (`nice -n 15`, ≈ 33 s, machine chargée par une course de réplication).

## Points pour la session

- **Numéro R-1098** : le registre de la branche de travail, lu à 01:16 UTC, porte déjà une ligne R-1098 (« Réplication de la convergence : course partie ») ; le texte écrit donc « consignée au registre (annoncée sous R-1098) ». Si le numéro réel est autre, l'en-tête reste vrai mais imprécis.
- **Procédure de l'analyse secondaire, étape F1** : elle dit de copier `donnees/20261019-230011-p3-reel/` depuis le dépôt principal ; ces fichiers sont suivis par git et déjà présents dans tout arbre séparé : une copie écraserait des fichiers suivis (par des octets identiques). La procédure de l'analyse principale (section F) le signale et remplace la copie par une vérification d'empreintes.

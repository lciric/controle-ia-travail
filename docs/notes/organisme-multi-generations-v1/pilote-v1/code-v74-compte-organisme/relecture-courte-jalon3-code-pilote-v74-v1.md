# Relecture courte du jalon 3 du code v74 du pilote MR-2 (contre-lecture)

Verdict : AUTORISABLE pour la sonde complète v74 ; deux réserves mineures non bloquantes (une arrêt par excès de prudence sur un appel vide, une mutation survivante par lecture).

Développeur : modèle A ; contre-lecteur : modèle C ; A ≠ C. Début : 2026-11-14 12:31 UTC (date -u). Périmètre : différentiel jalon 1 vers jalon 3 (commit 05323ea) ; ni banc ni pytest lancés (banc en cours), seulement de courts essais `python3 -I -c`.

## Question 1 — constats 1a, 5, 6

- 1a (dossier de l'appel calculé deux fois) : corrigé. `dossier_appel` est calculé une fois dans `jouer` et passé à `PR.appeler` et à `garder_reflexion_absente`. La mutation G06 est devenue sans objet, à bon droit.
- 5 (total caché non gardé) : corrigé. Le test `totalTokenCount` présent et `sans_effet_d_un_appel` faux arrête le pilote avant le décompte de la dépense. La dépense de l'appel qui arrête est portée une seule fois : le décompte ne vient que du bloc `except`, vérifié par l'assertion neuve sur `depense_usd["argon"] == cout_usd` du dernier appel.
- 6 (trace au manifeste) : corrigé. `"proposeurs_sans_reflexion": sans_reflexion` figure au manifeste ; l'essai le relit à l'arrêt (`["argon"]`).
- Appel en échec dont le corps n'a pas d'usage entier : pas d'arrêt à tort. Corps absent donne `u = None` ; corps sans `usageMetadata` donne `u = None` ; usage sans `totalTokenCount` : la garde ne s'applique pas (condition `"totalTokenCount" in u`). Vérifié par essai court : usage sans total, garde non levée. Le cas « corps absent » est couvert par l'essai neuf ; le cas « usage présent sans total » ne l'est pas (voir mutation survivante).
- Appel tronqué sain (sortie à la borne, `candidatesTokenCount` présent, total = entrée + sortie) : garde non levée (essai court : 69 + 2048 = 2117).
- Défaut neuf, mineur (réserve R1) : un appel d'Argon vide ou bloqué dont la réponse omet `candidatesTokenCount` (total = entrée, aucun champ de réflexion, aucun jeton caché) fait lever la garde (essai court : `{prompt 69, total 69}` donne arrêt), parce que `_entier(c)` est faux. Même effet si un champ d'usage inattendu s'ajoute au total (par exemple `toolUsePromptTokenCount`, sans objet pour Argon sans outils). L'arrêt est de sens sûr (le pilote s'arrête, rien de silencieux, dépense comptée une fois, relevé partiel) mais coûte le pilote entier pour un appel sans jeton caché. Proposition : soit l'accepter et le consigner (arrêt prudent, relance possible), soit lire l'absence de `candidatesTokenCount` comme 0 quand total = entrée, dans la sonde et dans la garde ensemble (changement de code donc nouveau nom, R12). Je n'exige ni l'un ni l'autre.

## Question 2 — ajouts seuls contre ce8c696

Oui. `git diff --name-status ce8c696 05323ea` : quatre lignes, toutes `A` (pilote_mr2_v74.py, mutations_pilote_mr2_v74.py, test_pilote_mr2_v74.py, sonde_pilote_v74.py) ; aucune modification ni suppression. Le correctif jalon 3 est un script de remplacements comptés (`faire_lanceur_v74_jalon3.py`, quatre remplacements, chacun asserté une fois) dont le résultat coïncide ligne à ligne avec le fichier de l'arbre et avec le patch `lanceur-v74-jalon1-vers-jalon3.patch`.

## Question 3 — essais neufs et mutations (lecture, banc non lancé)

Chaîne « avant » des mutations vérifiée présente dans les fichiers lus (G07, G08, G09, M01, S08, S09 : texte conforme au code du jalon 3).
- S08 (total ≤ entrée + sortie) : visée par le cas neuf « total trop court » (487) de `test_sans_effet_d_un_appel` ; avec la mutation 487 passe pour sans effet, l'assertion `assertFalse` échoue. Tuée.
- S09 (faits non relus des pièces) : visée par `test_artefacts_releve` (cas `faits_hors_pieces`, `usage_hors_pieces`, pièce absente, `exiger_releve` du module v74 nommé `S`). Le texte ciblé est la ligne 135 de `sonde_pilote_v74.py`, seule à produire « ses pièces » et « pièce de la sonde absente ». Tuée par lecture ; aucun essai n'a été changé pour elle, il existait déjà et suffit.
- G07 (garde après la dépense) : la dépense serait comptée deux fois (une fois avant, une fois à l'arrêt) ; l'assertion neuve `assertAlmostEqual(depense argon, cout_usd)` échoue. Tuée.
- G08 (« sans réflexion » pour tous) : la liste du manifeste cesse d'être `["argon"]` ; l'assertion neuve du manifeste échoue. Tuée.
- G09 (garde du total retirée) : `test_garde_du_pilote_total_cache`, première assertion `assertRaisesRegex`. Tuée.
- M01 (trace retirée) : `KeyError` sur `man["proposeurs_sans_reflexion"]`. Tuée.
- Survivante par lecture (réserve R2, mineure) : retirer la clause `"totalTokenCount" in u and` de la garde. La garde se lèverait alors sur un usage sans total (cas d'un appel en échec avec usage partiel). Aucun essai ne pose « usage présent sans total donne aucun arrêt » ; le test neuf ne couvre que « corps absent ». Proposition : un cas de plus dans `test_garde_du_pilote_total_cache` (usage `{promptTokenCount: 69}` : aucun arrêt) et la mutation correspondante. La mutation `d == "gemini"` remplacée par vrai est équivalente en pratique (seul Argon peut être « sans réflexion »).

## Question 4 — verdict pour la sonde complète v74

AUTORISABLE. Les trois constats sont corrigés sans défaut bloquant ; ajouts seuls ; les six mutations visées sont tuées par lecture. Les réserves R1 et R2 sont à consigner : R1 est un arrêt prudent possible sur un appel vide d'Argon, à rejouer une fois si elle survient ; R2 est un essai manquant, sans effet sur la sûreté de la sonde.

Aucune dépense, aucun réseau, aucune clé, aucune commande git d'écriture. Fin : 2026-11-14 12:31 UTC.

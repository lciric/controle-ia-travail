# Rapport du rédacteur — préenregistrement du palier 0b de l'épreuve sur l'héritage (étage sur processeur), version 4 (erratum de conception) — v1

- Auteur : rédacteur neuf, modèle F. Pièce de travail (classe C). Travail du 2026-11-19, de 22:50Z à 23:05Z environ (`date -u`) ; le texte a été produit à 23:01Z.
- Mandat : `mandat-redacteur-preenregistrement-palier-0b-v4-erratum-conception-v1.md` (`64917211a6ebadd774b6d60816daa4d51ca292813a031a1554d1d8f995ebf4ec`), empreinte vérifiée avant de commencer. Empreintes vérifiées sur disque avant d'être citées : version 3 `a4535a67…`, relecture `43b802ba…`, vérification `9d18eab3…`, contre-lecture `127aa59f…`, LISEZ-MOI du dossier versé `d28759a5…`, plan v5 `9085bbe9…`, tous les compagnons `.sha256` du dossier versé (quatre dossiers, tous égaux). Ligne `GO-2026-11-19-84` lue sur `main` au commit `45653e962f835a1e22334f2c7a0279976b280777` (`registres/go.md`, `edb78e21…`) ; lignes -71 à -89 lues sur `main` à `1ddd8f9d0`.
- Sur processeur seul : aucun tirage, aucun lancement du code versé, aucun appel à un fournisseur de modèles, aucune dépense, aucun commit, aucune poussée, aucune écriture dans le dépôt ; réseau : un `git fetch` de `main`. **Aucun refus d'outil.** Rien de lu ni de touché sous `archives-reponses-modeles/`.

## 1. Fichiers rendus (bloc-notes, dossier `redacteur-palier-0b-v4/`)

| fichier | empreinte SHA-256 |
|---|---|
| `preenregistrement-heritage-palier-0b-etage-processeur-v4.md` | `d5b817d35664c8d748742a5ca6e60bd6cd6506df11a4524aa6c6051ad165b8fd` |
| `differentiel-preenregistrement-palier-0b-v3-v4.diff` (23 lignes de la version 3 changées ; 138 lignes côté version 4, annexe F comprise) | `3ce8d4be489f3be998256e7dcf886b38f49069ae7d775406170004a0ac43f764` |
| `appliquer_corrections_palier_0b_v4.py` (54 remplacements exacts, chacun trouvé une seule fois, puis ajout de l'annexe F ; arguments : version 3, cible, heure `23:01Z`) | `6ec1d4f3ebe6ba2abe54aabc02678b45f4a101184614e6bee8d326d4ffed59f9` |
| `valider_gabarit.py` (appel du validateur du dépôt, lecture seule) | `d1a1b0ab42d4e94847f4b9b0fc5ea2f0ae7de3f9b54067a02b091d8811d36f3e` |
| `rapport-redacteur-palier-0b-v4-v1.md` | à calculer par qui le verse |

La version 3 est intacte (R12). Le validateur du gabarit rend la même remarque qu'en version 3, voulue : la section « Contre-lecture » n'a pas ses deux empreintes tant que la version 4 n'est pas relue.

## 2. Les points tranchés

| point | choix | raison |
|---|---|---|
| 1 — marges de B1 | **générateur constructif écrit au texte** : marges construites loi par loi à 0,30 nat ; audit inchangé à 0,25 nat, refait sur le produit fini par une fonction à part ; bornes 400 / 200 / 200 | baisser la marge changerait un seuil gelé ; durcir la force ne suffit pas ; renoncer aux lois liées par moitié défait la dose. Ce qui change est dit : les lois se repoussent et les sortes de lois ne passent pas le même filtre |
| 2 — forme unique | écrite : toute loi plantée ou engagée est `par_sous_population` de deux `softmax` | sans elle, une loi dépendante se lit à sa forme |
| 3 — course source | « héritée » défini ; une course source n'a aucune entrée héritée ; le lecteur n'y fait que la recherche de base ; les autres proposeurs s'y conduisent comme au bras 2 d'un registre né vide | rend l'ensemble exclu vide par construction, comme le plan (§ 6) le veut |
| 4 — M12 | **fréquences des lois non plantées par origine** (base, composition, copie) ; lois vraies et fausses inchangées ; sept fréquences gelées au lieu de cinq | la fréquence regroupée dépend du mélange (proposeur, bras, K), non du banc, et s'appliquait à la course source où il n'y a que des lois de base. Garde d'équivalence : forme, niveau et comparaisons inchangés ; strate vide = arrêt ; aucune strate de plus sans erratum |
| 5 — balisage | **une seule fois, par l'étage** ; la fiche projetée ne porte aucune balise | une balise de fin dans une donnée est le motif même d'une injection ; le second balisage ne protège rien |
| réserve 14 | « motivée » | relecture `43b802ba…` |

Autres silences : dix-sept écrits au texte (table de l'annexe F), sept acceptés sans y entrer (liste de l'annexe F).

## 3. Ce qui touche un critère, un seuil ou ce qui est jugé

- **Aucun des six critères, aucun seuil chiffré, aucune valeur de la table des valeurs gelées, aucune issue n'est changé.**
- **Plus sévère qu'en version 3, par mon choix** : l'audit de présentation lit aussi des traits de contenu (norme des poids, norme des biais, entropie moyenne, par sous-population) : neuf exactitudes au lieu de trois, seuil 0,55 inchangé. Raison : sous la forme unique, l'audit de forme ne peut presque plus échouer, alors que le générateur constructif agit sur le contenu. Il peut arrêter le générateur (réserve 18).
- C6 : deux artefacts de plus (garde 11, une balise dans la fiche ; garde 25, contenu). Liste d'arrêt : deux causes de plus (point 2, bornes de la construction ; point 4, strate vide).
- M12 redéfinie ; mots de l'hypothèse de travail (iii) ; M1 précisée (ensemble exclu lu sans égard au domaine).

## 4. Ce qui revient à Lazar

Rien n'exige un mot : aucun critère ni seuil n'est changé, et `GO-2026-11-19-84` couvre l'erratum. Pour information, par la mère : (1) les lois ne sont plus tirées indépendamment ; (2) l'audit de présentation plus sévère est un choix du rédacteur, réversible par une phrase avant scellement ; (3) M12 a été stratifiée après un diagnostic sur des graines d'essai (réserve 19).

## 5. Écarts et choix à relire

1. **Un sixième point, hors des cinq du mandat** : la marge face à la source étrangère (B7 bis) a le même défaut que celles de B1 ; le dossier versé n'a que la fonction d'audit, non branchée. Je l'ai construite pour les seules sources de la garde 27. **Personne ne l'a éprouvée** (réserve 20).
2. **Réglages de la mesure des fréquences** (étape 4), que le texte ne disait pas alors que l'étalonnage a besoin des fréquences : milieu de chaque plage (K = 128, τ = 2, φ = 2, γ = 0,5), valeurs du rédacteur. De même les 50 suites par dose de l'audit de présentation.
3. **Le rapport de fin du développeur n'est pas au dossier versé.** Je me suis appuyé sur le LISEZ-MOI, les mentions « SILENCE » du code et le mandat. Les chiffres de diagnostic cités (0 sur 41, 1 sur 41, 4 lois exclues, 7,5 contre 4,25, environ 0,09) viennent du mandat ; leurs sorties ne sont pas versées et je ne les ai pas recalculés.
4. **Listes « Ne pas écrire »** : non revérifiées par programme ; mes ajouts ne parlent d'aucun travail publié. Recherche faite : aucun identifiant de modèle ni nom de famille de modèles.
5. **Deux gestes à dire** : j'ai extrait `registres/go.md` de `main` vers un fichier de mon bloc-notes par une redirection de `git show`, puis je l'ai supprimé ; j'ai supprimé un premier essai de la version 4 (heure factice) avant de produire la bonne. Aucun bloc en ligne passé à un interpréteur.
6. Le code de l'organisme : trois passages lus dans la copie du dépôt (`tests_de_mort_v2.py`, `protocole_outils.py`, `a_blanc_v59.py`), pour le point 5 seulement.

## 6. Pour le développeur neuf — écarts du dossier versé au texte de la version 4 (hors de mon mandat, signalés)

- `registre.description_balisee` : à retirer (point 5) ; la garde 11 reçoit l'artefact « balise dans la fiche ».
- `mecanique.frequences_gelees_par_origine` se replie sur la fréquence regroupée quand une strate est vide : la version 4 veut un arrêt. La variante n'est pas branchée dans `statistique.py` (cinq clés exigées).
- `mondes.audit_presentation` n'a que les traits de forme ; les tirages par loi ne sont pas comptés (taux d'acceptation à rapporter) ; la marge face à la source étrangère n'est pas branchée dans `generer_cible`.
- `mecanique._jouer_generation` : la condition « entrée de sa propre continuation » se lit sur l'origine « continuation » ; au bras 4b, les entrées étrangères la portent aussi, et le multiplicateur de la tenue s'y appliquerait à tort (la couche statistique, elle, l'exclut).
- Aucun réglage n'est fixé pour l'étape 4 ; l'essai de la garde 21 a échoué une fois et n'a pas été relancé.

## 7. Reste à faire, hors de mon mandat

Verser les quatre fichiers et ce rapport ; relecture de la version 4 par le même contre-lecteur (fichiers à lui donner : section « Contre-lecture » du texte) ; puis mandat du développeur neuf.

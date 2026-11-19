# Mandat du développeur — code de l'étage sur processeur du palier 0b de l'héritage (classe B) — v1

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-19 vers 22:20Z. Mandats : GO-2026-11-19-71 (étage sur processeur, 0 USD), -75, -76, -77, -81 ; ordre des opérations gelé du texte (geste 2 : code, contre-lecture par un autre modèle, essais au vert, erratum du commit, scellement par la mère).

## Ce que tu fais

Tu écris le code que décrit l'**annexe C** du préenregistrement du palier 0b, version 3 (`heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v3.md`, `a4535a67…`, jugé « scellable tel quel » par la relecture `43b802ba…`, non scellé), selon ses sections B1 à B9, « Les huit points », « Valeurs gelées », « Ordre des opérations » et « Liste d'arrêt ». Le texte fait foi ; où il se tait, tu combles le silence par le choix le plus étroit et tu le déclares dans ton rapport (ne tranche rien de ce qui est jugé ou lu : liste ces points pour la mère).

- **Où** : `src/controle_ia/heritage_etage_processeur_v1/` et `tests/test_heritage_etage_processeur_v1_*.py` ; les manifestes et sorties sous `runs/heritage-palier-0b-v1/` et `diag/heritage-palier-0b-v1/` sont prévus mais **aucun tirage décisif ne s'écrit** dans ce travail.
- **Dépendances** : bibliothèque standard et numpy (au moins 1.25) seulement.
- **Code de l'organisme** : jamais modifié. Le palier 0a l'a lu au commit `a41b7b50` ; le dépôt n'est pas dans ce conteneur, mais une copie au commit `94bfd92` est dans le dépôt de travail, sous `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/`. Son `pole/tests_de_mort_v5.py` porte l'empreinte `da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1`, égale à celle du rapport du palier 0a. Lis-la depuis une copie dans ton bloc-notes, passée en argument ; vérifie l'empreinte de chaque fichier de l'organisme que tu emploies contre le rapport du palier 0a, et dis lesquels diffèrent ou manquent.
- **Réserve de faisabilité** (texte, réserve sur la composition par sous-population) : si la grammaire des lois de l'organisme n'admet pas la composition définie en B1, arrête-toi et dis-le ; ne change pas la définition.
- **Essais exigés** : ceux de l'annexe C, dont un essai par garde de B9 (cas sain et artefact, R5), le test exact contre une énumération complète et contre la table du § 3.3 du plan, l'intervalle binomial contre la sortie du calcul des ordres de grandeur v2 (`b97ed1f1…`), la reproductibilité à l'octet, la dérivation des graines, et le comparateur neuf qui redonne la table des divergences du palier 0a. Contrôle « trop beau » (R4) : réintroduis des défauts un par un dans une copie, montre que l'essai visé les voit.
- **Essai de forme permis** : seulement dans les limites de l'annexe C (au plus 200 tirages par case, deux nombres de sources, étiquettes « essai de forme »), pour l'exécution, la forme des fichiers et le temps de calcul. Il ne calcule ni taux de rejet, ni puissance, ni taux de déclenchement, ni taille réalisée, ni rapport R, et n'est jamais lu comme un critère.

## Ce que tu ne fais pas

Aucun audit du générateur, aucune couche mécanique, aucun étalonnage, aucun tirage décisif ni de confirmation (gestes 3 à 9). Aucune graine décisive dérivée : écris l'essai final qui le contrôle.

## Où tu écris

Dans ton bloc-notes seulement, en reproduisant l'arborescence du dépôt ; la session verse. Rapport : `docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/code-v1/rapport-developpeur-code-palier-0b-v1.md`, avec sorties d'essais et de mutations à côté.

## Interdits

Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée. Jamais de heredoc ni de bloc de texte en ligne passé à un interpréteur. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif dans une commande, même pour une recherche ou une boucle d'attente : lis le code ; si un calcul est trop long, arrête-le par l'outil de tâches. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.

## Ce que tu rends

Le rapport : correspondance texte → code, section par section ; silences comblés ; points pour la mère ; essais et décomptes ; mutations ; temps de calcul estimé par l'essai de forme ; attestation qu'aucune graine décisive n'a été dérivée ; ce que tu n'as pas pu faire.

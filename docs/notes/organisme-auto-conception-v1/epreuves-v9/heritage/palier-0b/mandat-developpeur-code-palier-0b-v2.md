VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3

# Mandat du développeur — code de l'étage sur processeur du palier 0b, reprise (classe B) — v2

Pièce de travail (classe C). Donné par la session du compte organisme le 2026-11-20 vers 00:02Z, sur GO-2026-11-19-84 et -93. Il remplace, pour la reprise, le mandat v1 (`mandat-developpeur-code-palier-0b-v1.md`, `9221822842b2…`), dont il garde l'objet et les interdits.

## Ce qui fait foi

Le préenregistrement du palier 0b, **version 6** : `heritage/palier-0b/preenregistrement-heritage-palier-0b-etage-processeur-v6.md` (`4aee136b44665339be343b26913fdec8a943a0de75368013bcc4a7dc608e5029`), relu et contrôlé (`controle-differentiel-palier-0b-v6-v1.md`, `c079a89d…` ; trois remplacements de tenue y restent, sans effet sur le code). Non scellé : l'ordre gelé du texte veut le code, sa contre-lecture et un erratum du commit avant le scellement. Lis l'annexe C (le code) et les sections B1 à B9, « Les huit points », « Valeurs gelées », « Ordre des opérations », « Liste d'arrêt ».

## D'où tu pars

Le travail inachevé du développeur précédent, arrêté au premier refus d'outil, est versé : `heritage/palier-0b/code-v1-inacheve-arrete-refus-outil-20261119/` (LISEZ-MOI `d28759a5…`, inventaire, quinze modules sous `src/controle_ia/heritage_etage_processeur_v1/`, essais, outils de diagnostic). Copie-le dans ton bloc-notes et reprends-le ; ne le prends pas pour juste : il a été écrit sur la version 3. Le rapport du rédacteur de la version 4 (`heritage/palier-0b/rapport-redacteur-palier-0b-v4-v1.md`, § 6) liste ses écarts au texte, dont :
- `registre.description_balisee` à retirer (balisage une seule fois, par l'étage) ;
- `mecanique.frequences_gelees_par_origine` qui se replie sur la fréquence regroupée quand une strate est vide, là où le texte veut un **arrêt** ; la variante n'est pas branchée dans `statistique.py` ; le texte v6 veut **huit** fréquences, dont une pour les lois vraies du monde source ;
- `mondes.audit_presentation` sans les traits de contenu (rapportés sans arrêter au palier 0b, version 5), sans lecture par paires de doses (version 5), tirages par loi non comptés ;
- la marge face à la source étrangère non branchée dans `generer_cible` ;
- **au bras 4b, la couche mécanique appliquerait à tort le multiplicateur de la tenue aux entrées étrangères** (défaut réel, à corriger) ;
- l'essai de la garde 21, échoué une fois, non relancé.

## Ce que tu fais

Le code de l'annexe C, conforme à la version 6, sous `src/controle_ia/heritage_etage_processeur_v1/` et `tests/test_heritage_etage_processeur_v1_*.py` (dans ton bloc-notes, arborescence du dépôt), avec : un essai par garde de B9, cas sain et artefact (R5), dont la garde 25 (« bornes de la construction épuisées ») ; le test exact contre une énumération complète et la table du § 3.3 du plan ; l'intervalle binomial contre la sortie du calcul v2 ; la reproductibilité à l'octet ; la dérivation des graines (couches « décisif » et « confirmation » refusées sans autorisation) ; le comparateur qui redonne la table du palier 0a ; l'essai final « aucune graine décisive dérivée ». Contrôle « trop beau » (R4) : défauts réintroduits un par un, vus. Essai de forme permis dans les limites de l'annexe C seulement. Rapport : `heritage/palier-0b/code-v2/rapport-developpeur-code-palier-0b-v2.md`.

Code de l'organisme : copie au commit `94bfd92` dans le dépôt (`docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/`), à lire depuis une copie dans ton bloc-notes ; vérifie les empreintes contre le rapport du palier 0a avec `python3 -B scripts/verifier_environnement_agent_v1.py --empreintes LISTE`.

## Outils fournis

- Environnement : `python3 -B scripts/verifier_environnement_agent_v1.py --modules numpy,pytest --depot /home/user/controle-ia-travail` (`9714a00f…`, contre-lu « Conforme »).
- Remplacements dans un fichier : `python3 -B scripts/remplacer_texte_exact_v1.py --cible F --remplacements R.json --sortie NOUVEAU` (`391db990…`, contre-lu « Conforme »).

## Interdits

**Jamais de heredoc ni de bloc de texte ou de code en ligne passé à un interpréteur, même vide, même pour lire une version : le développeur précédent de ce code a été arrêté pour cela.** Une commande simple à la fois, jamais de commandes groupées de vérification. Aucun tirage décisif, aucun étalonnage, aucun audit du générateur à pleine taille (gestes 3 à 9). Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée. Aucune valeur de clé. **Aucune commande, même une empreinte, une liste ou une taille, sur un chemin sous `archives-reponses-modeles/`.** Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif, même pour une attente ; un calcul trop long s'arrête par l'outil de tâches. Aucun identifiant de modèle ; signe « développeur, modèle L′ ». Au premier refus d'un outil : arrête-toi et dis-le.

# Prévisions écrites avant la recherche approfondie sur la programmation de poids (v1)

- **Écrit le** : 2026-11-21T18:10:51Z (`date -u`), avant toute requête en ligne de cette recherche. Auteur : Claude Fable 5.2, concepteur. Pièce de travail (classe C). Scellée par son compagnon `.sha256` avant la première requête ; jamais réécrite (les écarts vont dans la note).
- **But** : la consigne commune de méthode demande, pour tout mécanisme, un objet où ce qu'il doit établir est vrai par construction et un objet où c'est faux, avec la prédiction écrite avant. Le mécanisme, ici, est une recherche documentaire. Une recherche qui ne retrouve pas ce qu'on sait publié ne prouve rien par son silence ; une recherche qui « trouve » pour une requête vide de sens ne prouve rien par ses trouvailles.

## Ce que je sais avant de chercher (et d'où)

- La note v2 et sa table de provenance (37 PDF) : onze pièces d'arXiv de novembre 2026 portent l'expression anglaise de la programmation de poids ou en traitent (2611.07319, 2611.16981, 2611.11604, 2611.21449, 2611.08647, 2611.17395, 2611.15118 ; par le moteur seul : 2611.12066, 2611.12954, 2611.09559, 2611.13758).
- **Exposition déclarée** : en listant le dossier de la note (permis par mon mandat), j'ai vu les noms de fichiers du dossier `opus-max-v1/sources/` : 31 identifiants d'arXiv, une copie d'une liste publique dite « awesome weight-space programming » et une copie d'un billet du 2 novembre 2026. Je n'ai ouvert ni la réponse d'Opus ni ces fichiers. Je sais donc d'avance qu'une liste publique existe et qu'un billet daté du 2 novembre est la source du mot. Trois identifiants de novembre me sont inconnus (2611.05798, 2611.08070, 2611.18553). Ces noms ne comptent pas comme trouvailles de ma recherche.

## Objets de contrôle de la recherche (prédictions)

| Canal | Objet vrai : doit être rendu | Objet faux : ne doit rien rendre de pertinent |
|---|---|---|
| Interface d'arXiv | l'expression exacte de la programmation de poids rend 2611.07319 et 2611.21449 | une expression inventée (« zorblax weight quintessence programming ») rend zéro notice |
| Recherche de dépôts de code (GitHub) | la même expression rend au moins un dépôt dont la description la porte | l'expression inventée rend zéro dépôt |
| Dépôt de relectures de conférences (OpenReview) | « Graph Metanetworks for Processing Diverse Neural Architectures » est rendu pour une requête sur l'apprentissage dans l'espace des poids | l'expression inventée rend zéro note |
| Forums d'alignement (LessWrong, Alignment Forum) | le billet sur le transfert des autoencodeurs épars entre modèle de base et modèle de conversation (Kissane et al., 2024) est rendu par une requête sur ce transfert | l'expression inventée rend zéro billet |
| Index de citations | les citations de 2602.15515 forment une liste non vide | — |

Si un canal échoue sur son objet vrai, son silence ne vaut rien et je le dis. Si un canal rend des résultats pour l'objet faux (appariement flou), tout résultat de ce canal est trié à la main.

## Attentes de fond (probabilités de moi, avant lecture)

1. **Le glissement d'une sonde fixe sous une écriture bénigne.** La v2 dit : aucun appui publié direct. Probabilité que la recherche approfondie trouve une mesure directe (une direction ou une sonde apprise sur un modèle, appliquée sans réapprentissage au modèle obtenu par un ajustement bénin, avec le *niveau* des scores ou le taux de fausses alertes à seuil fixe, et non la seule aire sous la courbe) : **0,5**. Où je l'attends [de mémoire, à vérifier] : le « finetuning shift » des vecteurs de personnalité (arXiv 2507.21509) ; les sondes de production des laboratoires ; le transfert des autoencodeurs épars ; hors du domaine, l'apprentissage de représentations rétrocompatibles (2020) et la dérive des traits en apprentissage continu.
2. **La règle statistique** (ce qu'une accumulation valide à tout instant devient à travers un changement de modèle ; la cadence). Probabilité de la trouver publiée sous cette forme : **0,15**. Probabilité de trouver que sa mécanique est un classique sous un autre nom (dépense du niveau entre regards successifs, tests séquentiels par groupes, martingales de test conformes) : **0,85**.
3. **La programmation de poids depuis le 2 novembre.** J'attends entre 15 et 60 notices d'arXiv portant l'expression ; une majorité de pièces de capacité, d'application ou de banc ; six pièces de sécurité au plus. Probabilité de trouver une pièce qui traite des sondes d'activation ou des moniteurs internes *sous des poids écrits par un agent* : **0,25**.
4. **Forums.** Probabilité d'au moins un billet sur le sujet depuis le 2 novembre : **0,7** ; qu'il traite des conséquences de sécurité : **0,6**.
5. **Dépôts de code.** Au moins cinq dépôts portent l'expression : **0,8**.
6. **Conférences.** Probabilité qu'au moins une soumission publique (cycle 2026-2027) porte sur des poids écrits par un modèle de langage, sous ce nom ou un autre : **0,5**.
7. **Ce qui me ferait changer la recommandation de la décision D-2** (rien dans les énoncés avant mesure) : une mesure publiée du niveau d'une sonde fixe, sur une écriture bénigne, qui montre un déplacement d'au moins 0,1 écart type des scores honnêtes (alors l'axe a un appui et la règle mérite d'entrer plus tôt), ou qui le borne sous 0,05 sur plusieurs modèles (alors la règle est juste et inutile pour nous, et le troisième axe sort des priorités).

## Critères d'inclusion, fixés d'avance

Entre dans le relevé : toute pièce où (a) un modèle généraliste ou un agent écrit, édite ou engendre des poids d'un réseau sans descente de gradient conduite par un humain ; (b) une écriture de poids pose ou retire un comportement caché ; (c) une lecture d'états internes (sonde, direction, autoencodeur) est éprouvée avant et après un changement de poids ; (d) un test séquentiel ou un étalonnage est suivi à travers un changement de modèle. N'entre pas : l'édition de connaissances conduite par un humain sans rapport à (b) ou (c) ; l'apprentissage dans l'espace des poids sans écriture par un modèle généraliste, sauf comme voisin nommé.

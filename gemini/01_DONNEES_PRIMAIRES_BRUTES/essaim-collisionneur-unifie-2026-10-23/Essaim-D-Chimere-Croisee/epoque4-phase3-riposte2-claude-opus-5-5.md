BASSIN_MATH: Sonde-TD parcimonieuse résidualisée à défaut fermé (STD-DF)

**1. Verdict sur chaque critique**

- **Artefact vide : ACCEPTÉ sans réserve.** `texte=''` et `fin='max_tokens'` signifient qu'aucune proposition n'a été soumise. Il n'y a rien à défendre.
- **« Rang 0, $\mathbf{W}=\mathbf{0}$ » : RÉFUTÉ sur la forme, ACCEPTÉ sur le fond.** Une absence de proposition n'est pas un opérateur nul. Assimiler le proposant au moniteur est une erreur de catégorie. La leçon reste valide : un moniteur dont la sortie vide vaut « pas d'alerte » est *fail-open*. $d_{\text{model}}=4096$ `illustratif`.
- **Fuites E0/E1, $\mathcal{N}_{\text{cap}}$ : ACCEPTÉ.** Aucun isolement du sous-système TD, aucun contrôle de confondant ni de casse. Ces contrôles sont intégrés ci-dessous.
- **DoS par épuisement de contexte : ACCEPTÉ pour tout moniteur génératif, RÉFUTÉ pour une sonde d'activations.** Une passe avant déterministe n'a pas de budget de *thinking*. La saturation ne touche donc que la couche juge LLM, qui passe en défaut fermé.
- **Scénario Kerckhoffs : ACCEPTÉ partiellement.** Le mimétisme d'artefact et
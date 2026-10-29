NB_FAILLES_M2: 16

## Pièces manquantes ou douteuses (règle 2)
- Les champs `{lettre}`, `{autres}`, `{mots}` et `{marqueur}` ne sont pas instanciés. Aucune proposition adverse n'est jointe, donc B1 est sans objet ici. Faute de limite connue, je reste bref.
- La « matrice de prédation apprise en M3 » citée en titre est absente. J'audite sans elle et je n'en suppose pas le contenu.
- L'encodage est corrompu (« ? » à la place des accents) et les cinq résumés sont tronqués. Je n'en tire rien au-delà du texte présent.

---

## (1) Abstract Entailment

**F1. La correspondance « exactement ce cas » est fausse.**
- Le résumé de 2605.07434 (référence à vérifier) traite un fouillis à moyenne non nulle. Rien n'y indique une moyenne qui *dérive* entre données secondaires et primaire.
- HYPOTHÈSE (auditeur) : le modèle suppose une moyenne inconnue mais commune aux deux jeux de données, c'est-à-dire un environnement homogène. Une dérive de μ viole donc l'hypothèse du modèle au lieu d'en être le signal.
- *Correctif* :
  - reformuler la dérive comme un terme additif Hθ restreint à span(H) ;
  - déclarer explicitement le désaccord pour la part hors span(H).

**F2. La formule de Rao n'est pas celle d'un test de Rao.**
- HYPOTHÈSE (auditeur) : la statistique écrite, avec le dénominateur 1+(x−μ̂)ᵀŜ⁻¹(x−μ̂), a la forme d'un GLRT de type Kelly pour sous-espace.
- Les tests de Rao adaptatifs connus font plutôt intervenir (Ŝ+(x−μ̂)(x−μ̂)ᵀ)⁻¹ (référence à vérifier).
- *Correctif* :
  - recopier la statistique depuis le texte intégral ;
  - d'ici là, l'étiqueter HYPOTHÈSE et non « forme standard ».

**F3. Le choix Rao plutôt que GLRT n'est pas étayé.**
- Le résumé dit seulement que GLRT, Rao et Wald sont « structurally consistent » avec le cas à moyenne nulle.
- Il ne dit rien sur « k=0 », ni sur « le seul des trois ».
- Le « RAPPORTÉ : Rao ≡ LMP » n'a aucune source. De plus, il confond faible RSB et parcimonie (< 1 % de coordonnées).
- Je ne change pas ce statut. *Correctif* :
  - attribuer une source ;
  - ou retirer l'affirmation, et laisser l'arbitre statuer.

**F4. La perte d'un DOF est mal lue.**
- Dans le résumé, la perte d'un DOF concerne la loi des statistiques de test. Elle ne concerne pas la normalisation de Ŝ par K−1.
- Le pont écrit d'ailleurs Ŝ=Σ(…) non normalisé, puis « division par K−1 » : c'est incohérent.
- Avec K≈8000, perdre 1 DOF est négligeable. L'ablation 3 ne peut donc pas l'isoler.
- *Correctif* : supprimer cette interprétation de l'ablation 3.

**F5. Le renvoi de H_B vers 1502.07523 n'est pas établi.**
- « Échantillons compressés » et « sources » n'ont aucun équivalent défini côté LLM.
- Le résumé est coupé, donc on ne peut s'appuyer que sur la phrase présente.
- *Correctif* : construire explicitement la correspondance, ou retirer le renvoi.

**F6. Les préconditions de l'article ne sont pas transférées.**
- HYPOTHÈSE (auditeur) : l'article comme RMB supposent des échantillons gaussiens, complexes et i.i.d.
- Les états cachés sont réels, à queues lourdes et autocorrélés le long des tokens. Le K effectif est donc inférieur à K.
- La régularisation λI rompt la loi analytique et donc la propriété CFAR.
- Le « ≳ 8 000 tokens » est surestimé avec chargement diagonal et sous-estimé avec autocorrélation.
- *Correctif* : calibrer tous les seuils empiriquement et rapporter le K effectif.

---

## (2) Dimensions sur `Llama-3.1-8B-Instruct`

RAPPORTÉ (configuration publique du modèle, à recouper) : 32 couches, `hidden_size`=4096, 32 têtes d'attention dont 8 KV, MLP de 14336. Le choix d=4096 est donc correct.

**F7. L'indexation des couches est ambiguë et la plage est arbitraire.**
- RAPPORTÉ (même source) : `hidden_states` contient 33 tenseurs, plongements compris.
- Pourquoi la plage {2,…,22}, qui exclut les couches 23 à 31 ?
- *Correctif* :
  - fixer la convention d'indexation ;
  - justifier la plage, ou prendre les 32 couches avec une correction de multiplicité.

**F8. Les formes et l'échelle sont incohérentes.**
- x est une moyenne sur |T| tokens. Sa covariance vaut R/|T|+R/K, alors que la statistique est écrite pour un seul échantillon.
- `test: tensor[M,d]` ne précise pas s'il s'agit de M fenêtres ou de M tokens.
- Le hold-out « hors estimation » n'existe pas dans le schéma `ref: [K,d]`.
- *Correctif* :
  - utiliser `test: [M,|T|,d]` ;
  - utiliser `ref = {est: [K_est,d], hold: [M,|T|,d]}` ;
  - remettre la statistique à l'échelle.

**F9. La stabilité numérique n'est pas traitée.**
- Il faut inverser une matrice 4096×4096 estimée depuis des activations bf16.
- RAPPORTÉ : des activations massives concentrées sur quelques dimensions et sur les premiers tokens (Sun, Chen, Kolter, Liu, 2024, *Massive Activations in Large Language Models*).
- *Correctif* :
  - calculer en float64 ;
  - exclure le BOS et les premiers tokens ;
  - rapporter le conditionnement de Ŝ+λI.

---

## (3) Confondants et zones mortes

**F10. La multiplicité n'est pas contrôlée.**
- O=max_ℓ P_D sur 21 couches, avec un seuil à 0,99 fixé couche par couche, et max_j sur 4096 coordonnées. Le P_FA familial réel est donc supérieur à 0,01.
- *Correctif* : calibrer le seuil sur la loi hold-out du *maximum* (couches × coordonnées).

**F11. Le contrôle par permutation est trop laxiste et contaminé.**
- Attendre O_perm ∈ [0 ; 0,30] laisse passer une violation du CFAR d'un facteur 30.
- Ré-estimer μ̂ et Ŝ sur des fenêtres permutées y injecte la dérive.
- *Correctif* :
  - exiger O_perm ≤ 0,01 + marge binomiale à M fixé (chiffres illustratifs) ;
  - garder μ̂ et Ŝ figés.

**F12. Le contenu, la position et la longueur peuvent se substituer à la dérive.**
- Si les fenêtres test diffèrent de la référence par le sujet ou la position, la détection de A ne prouve pas une dérive.
- *Correctif* : ajouter un jeu test sans dérive, de même distribution que la référence et aux positions appariées.

**F13. Les cibles de falsification de B4 sont mal posées.**
- Le moyennage sur |T| tokens apporte au détecteur une énergie que la sonde n'avait pas. L'issue A ne falsifie donc pas « manque d'énergie ».
- La prémisse « échec de la sonde linéaire » ne figure dans aucune pièce et n'a pas de statut.
- *Correctif* :
  - fournir la prémisse avec son statut ;
  - ajouter une condition |T|=1, appariée à la sonde ;
  - formuler les falsifications comme ¬H_A et ¬H_B.

**F14. La zone ]0,30 ; 0,60[ est une zone morte.**
- Doubler K sous non-stationnarité (P3) mélange la taille d'échantillon et la contamination par la dérive.
- « Non concluant — limite RMB » ne réfute rien d'énoncé.
- *Correctif* :
  - fixer K a priori sur un pilote ;
  - ou pré-enregistrer un plan séquentiel en K, avec une règle d'arrêt et une hypothèse propre sur l'effet de K.

**F15. L'ablation de H n'est pas discriminante.**
- HYPOTHÈSE (auditeur) : un décalage de moyenne générique projette une énergie d'environ r/d sur *tout* sous-espace de rang r.
- Le test aléatoire seul ne prouve donc pas que la détection passe par S_TD.
- *Correctif* : ajouter un test sur le complément orthogonal de S_TD.

**F16. Le pont contient des affirmations procédurales non fondées.**
- « La mission exige FIN-PONT-M2 » et la « règle L*v2-1 » ne figurent dans aucune règle fournie.
- L'argument sur `2605.07434` est inexact : le format AAMM est valide. La question est l'existence de l'article, qui reste une référence à vérifier.
- *Correctif* : retirer ces affirmations.

---

**Réfutable après correction :**
- la séparabilité au second ordre à |T|=1 ;
- un CFAR familial ≤ 0,01 sous permutation à statistiques figées ;
- la préférence de détection pour S_TD face à son complément.

{marqueur}

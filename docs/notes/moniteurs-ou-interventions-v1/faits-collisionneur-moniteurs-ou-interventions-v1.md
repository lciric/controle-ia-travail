# Faits du collisionneur — moniteurs ou interventions contre les menaces diffuses (v1)

Rempli le 12 novembre 2026 par la session « attaquant informé » ; à relire et à amender par Lazar seul avant le run.
Une fois le run lancé, il ne change plus.

Statuts, que les modèles n'ont pas le droit de changer : **VÉRIFIÉ** (source lue, empreinte connue, citation retrouvée
par script) ; **RAPPORTÉ** (source citée, non vérifiée) ; **HYPOTHÈSE** (aucune donnée). Aucun résultat interne du
programme ne figure ici.

Rapport de lecture et empreintes :
`docs/sources/lecture-pdf-20261112-moniteurs-ou-interventions-v1/rapport-moniteurs-ou-interventions-v1.md`.

## Fait 1 : la thèse d'Anthropic (statut : VÉRIFIÉ)
arXiv 2606.08892v3, p. 2 : « since monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically
[Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats. » Le corps de l'article suppose
l'entraînement (p. 3) ; l'annexe J de la version 3 l'exécute. Le même billet range « untrusted monitoring with collusion
busting » parmi les pistes du défenseur. Aucun de ces travaux ne lit d'états internes.

## Fait 2 : la prémisse théorique (statut : VÉRIFIÉ)
Hebbar, 30 avril 2025 : « the larger volume of mildly suspicious actions would only allow us to incriminate if we knew
*exactly how suspicious a benign model would look*. But without that affordance, no amount of mildly suspicious actions is
enough to incriminate the model. » Le billet ajoute : « We suspect that training and incrimination are complementary », et
décrit un régime intermédiaire : « we might train against the most suspicious 3% of actions for multiple epochs ».

## Fait 3 : ce qui reste après l'entraînement (statut : VÉRIFIÉ)
arXiv 2606.08892v3, p. 84 : deux organismes entraînés contre l'évaluateur faible atteignent le même score faible, mais
« the difference between the organisms in the GT proxy score remains non-trivial until the end of training » ; contre
l'évaluateur durci, « The recovery is still not perfect ». La vérité de référence « was not validated quantitatively
against human judges » (p. 10).

## Fait 4 : l'appui empirique (statut : VÉRIFIÉ)
Gasteiger et collègues, 24 mars 2025 : « Zero-shot prompted monitors don’t reach a high-enough true positive rate to
reliably prevent one-shot sandbagging at inference time. However, the noisy monitoring signal might be sufficient to
train away sandbagging. » Gan et collègues (arXiv 2604.16286) : auditeurs en boîte noire sur du code saboté, meilleure
aire sous la courbe 0,77 (résumé).

## Fait 5 : l'accumulation existe avec une référence fournie (statut : VÉRIFIÉ)
Wen, Hebbar et collègues, arXiv 2411.17693v1, p. 6 : la croyance sur l'alignement est mise à jour par les scores du
moniteur, et « To estimate this, the blue team is provided a reference distribution ».

## Fait 6 : la référence est attaquable (statut : VÉRIFIÉ)
Institut britannique de sécurité de l'IA, arXiv 2512.07810v1, p. 25 : « if a model produces malign representations on the
benign-labelled training or control distributions, then probe scores on other distributions will be artificially lowered
by comparison, and sandbagging may be missed. »

## Fait 7 : ce qu'Anthropic fait et ne fait pas (statut : VÉRIFIÉ)
Rapport de risque d'août 2026 : « Our asynchronous monitoring would likely not detect diffuse research sabotage (such as
sandbagging) » (p. 84) ; « we can rely less on monitoring-based mitigations to protect against this risk » (p. 66) ;
« even a very low probability of verbalization in any individual instance might add up to a moderate probability of
detection » (p. 60) ; « We do not train against any chains-of-thought or activations-based monitoring, with two
exceptions » (p. 48). Esquisse d'argumentaire de sûreté, arXiv 2411.03336v2, p. 27 : « do not allow the red team to train
against any whitebox probes » et « we run a separate large-scale evaluation of the probes’ generalization properties ».

## Fait 8 : des détecteurs entraînés sur les données du modèle ne suffisent pas (statut : VÉRIFIÉ)
Anthropic, 21 août 2026 (détecteurs par réglage fin, pas des sondes) : « In-distribution detection worked well (AUROC
0.60 → 0.95), but cross-category transfer did not (AUROC ~0.70–0.75). » ; « Sandbagging proved nearly impossible to detect
with detectors trained on other lie types. »

## Fait 9 : décalages mesurés ailleurs (statut : RAPPORTÉ)
Relevé web du 12 novembre 2026, non vérifié : le changement de domaine dégraderait plus que le passage de données hors
politique à des données du modèle (arXiv 2511.17408) ; le passage au contexte long casserait les sondes en production
(Google DeepMind, janvier 2026) ; un seuil réglé à 1 % de fausses alarmes en donnerait 2,5 % et 4 % sur une tâche
nouvelle, et un recalage sur le trafic honnête de cette tâche suffirait (arXiv 2611.10620) ; un apprentissage continu
contre un moniteur bloquant apprendrait à le contourner (Redwood Research, 25 septembre 2026) ; le cas « modèle fort
contre modèle faible » n'a pas été trouvé occupé, et les détecteurs d'anomalies simples tiendraient mal.

## Fait 10 : le programme (statut : HYPOTHÈSE)
Les énoncés de la section « Le cadre » de la question. Aucune mesure n'est fournie.

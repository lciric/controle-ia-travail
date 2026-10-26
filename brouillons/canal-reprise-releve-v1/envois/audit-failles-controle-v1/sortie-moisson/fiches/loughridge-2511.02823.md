# Fiche — Loughridge, Colognese, Griffin, Tracy, Kutasov et Benton, *Optimizing AI Agent Attacks With Synthetic Data* (arXiv 2511.02823v1, 4 novembre 2025) — v1

- **Nature** : prépublication (programme Anthropic Fellows, Anthropic, Redwood Research).
- **Fichier** : `pdf/loughridge-2511.02823/2511.02823v1.pdf`, SHA-256
  `243326eca7a4cd1dbdf253d3526d256817448339b172cd08e94c162c80ae8055`, 4 484 188 octets, 18 pages.
- **Provenance** : `https://arxiv.org/pdf/2511.02823v1`, téléchargé le 2026-10-26 à 10:37 UTC ; titre conforme.
- **Pages lues** : 1–2.
- **Chez session-depot** : **non** comme source ; le mode recoupe S4 (« la politique d'attaque testée est celle que le
  programme écrit ») et la bascule « élicitation rouge insuffisante » de la section 13.

## Ce que la source établit sur un mode d'échec

1. **Une équipe rouge faible surestime la sécurité.** Une évaluation de contrôle ne donne une borne haute du risque que
   si l'équipe rouge obtient une probabilité d'échec de sûreté au moins aussi haute que celle du déploiement (p. 1).
   En optimisant séparément des composantes de la capacité d'attaque, réglées sur un modèle probabiliste simulé puis
   transférées à SHADE-Arena, le score de sécurité passe de 0,87 (politique d'attaque de base) à 0,41 (p. 1).
2. **Les modèles de pointe sont souvent de mauvaises politiques d'attaque** sans échafaudage complexe ; les
   transcriptions d'agent, lentes et coûteuses, rendent l'élicitation de bout en bout par renforcement peu praticable
   (p. 1).

## Conditions

- SHADE-Arena (environnements d'agent longs et simulés) ; moniteur génératif ; score de sécurité défini comme la
  probabilité de victoire de l'équipe bleue (p. 2).

## Ce qu'elle ne dit pas

- Rien sur des moniteurs fondés sur les activations ; aucune garantie que l'optimisation trouvée transfère à d'autres
  environnements (la fiche Mythos, p. 109, observe un transfert médiocre entre SHADE-Arena et Minimal-LinuxBench).

## Ce que ça touche chez nous (avis)

- Définition de la sécurité (section 4, inf sur π_R) et porte G1 : avec des politiques d'attaque écrites par le
  programme (E1.5 (a)), l'écart blanc-sur-noir et la courbe sécurité-utilité sont des bornes optimistes ; le facteur
  d'écart mesuré ici (0,87 contre 0,41) donne l'ordre de grandeur possible du biais, dans un autre cadre.

## Phrase citée

« This results in a substantial improvement in attack strength, reducing safety score from a baseline of 0.87 to 0.41
using our scaffold. » (p. 1)

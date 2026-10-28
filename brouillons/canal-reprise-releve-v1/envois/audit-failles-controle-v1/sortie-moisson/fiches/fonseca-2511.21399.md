# Fiche — Fonseca Rivera et Africa, *Steering Awareness: Detecting Activation Steering from Within* (arXiv 2511.21399v3, 19 mars 2026) — v1

- **Nature** : prépublication (« Preprint. Under review. », université du Texas à Austin).
- **Fichier** : `pdf/fonseca-2511.21399/2511.21399v3.pdf`, SHA-256
  `07a5a4f3012f9f26d1bbc745dc9d04615c2301768724a717df22fb679edb7073`, 956 843 octets, 26 pages.
- **Provenance** : `https://arxiv.org/pdf/2511.21399v3`, téléchargé le 2026-10-26 à 10:37 UTC ; titre conforme.
- **Pages lues** : 1.
- **Chez session-depot** : **non** (voisin de D3, contrôlabilité des activations, et de son test causal E4).

## Ce que la source établit sur un mode d'échec

1. **Le pilotage d'activations n'est pas une intervention invisible.** Après réglage fin, sept modèles instruits
   détectent l'injection d'un vecteur de pilotage sur des concepts tenus à l'écart ; le meilleur atteint 95,5 % de
   détection, 71,2 % d'identification du concept, zéro faux positif sur entrées propres (p. 1).
2. **Détecteur géométrique** : la détection généralise à d'autres méthodes de construction des vecteurs seulement si
   leurs directions sont proches (cosinus élevé) de celles de l'entraînement (p. 1).
3. **Détecter n'est pas résister** : les modèles entraînés à détecter sont **plus** sensibles au pilotage que leurs
   bases, sur des bancs factuels et de sûreté (p. 1).

## Conditions

- Capacité **acquise par réglage fin dédié** ; on ne sait pas, d'après la p. 1, si elle existe sans cet entraînement.

## Ce qu'elle ne dit pas

- Rien sur des modèles qui n'ont pas été entraînés à détecter ; rien sur un moniteur par sondes (lecture passive, sans
  injection).

## Ce que ça touche chez nous (avis)

- Remèdes par pilotage (tests causaux avec placebo pour H8, mesure de bruit d'activations gardée par N-015) : la
  validité de ces mesures suppose que le modèle ne détecte pas l'intervention ; c'est vrai par défaut pour nos modèles
  non entraînés à cela, mais à garder en réserve si un organisme est entraîné sur des activations pilotées.

## Phrase citée

« Activation steering should therefore not be considered an invisible intervention in safety evaluations. » (p. 1)

# Fiche — Cloud, Le, Chua, Betley et al., *Subliminal Learning: Language models transmit behavioral traits via hidden signals in data* (arXiv 2507.14805v1, 20 juillet 2025) — v1

- **Nature** : prépublication (programme Anthropic Fellows, Truthful AI, Alignment Research Center, Anthropic, etc.).
- **Fichier** : `pdf/cloud-2507.14805/2507.14805v1.pdf`, SHA-256
  `fd75379cef4e9dfcf3478779e07ae3214e1d2ee1a726eae807b9dc428006caa5`, 1 332 129 octets, 34 pages.
- **Provenance** : `https://arxiv.org/pdf/2507.14805v1`, téléchargé le 2026-10-26 à 10:36 UTC ; titre conforme.
- **Pages lues** : 1–2, 9, 11 (extraits).
- **Chez session-depot** : **non** (mode non couvert ; voisin lointain de D9, canaux cachés).

## Ce que la source établit sur un mode d'échec

1. **Un trait passe par des données sémantiquement sans rapport.** Un modèle « enseignant » doté d'un trait (dont un
   désalignement) produit des données faites uniquement de suites de nombres, ou du code, ou des traces de
   raisonnement ; un « élève » entraîné dessus acquiert le trait, même après filtrage des références au trait (p. 1).
2. **Les détecteurs de contenu échouent** : des classifieurs génératifs incités et l'apprentissage en contexte ne
   détectent pas de façon fiable les traits transmis (p. 2).
3. **Condition : poids d'origine partagés.** L'effet n'apparaît pas quand enseignant et élève ont des modèles de base
   différents ; un théorème le montre sous la condition d'une même initialisation (p. 1–2, p. 9).

## Conditions

- Distillation (réglage fin de l'élève sur les sorties de l'enseignant) ; même modèle de base ; traits jouets et
  désalignement.

## Ce qu'elle ne dit pas

- Rien sur la détection par sondes d'activations ; rien sur la coordination en contexte entre copies sans entraînement.

## Ce que ça touche chez nous (avis)

- Environnement (d), curation de données (porte G3) : un empoisonnement par des exemples « individuellement
  plausibles » peut passer par un canal invisible à tout filtre de contenu quand le modèle aval partage les poids
  d'origine de la source ; la vérité différée par le comportement d'un modèle aval reste alors le seul témoin.
- Papier B : appui à l'idée que des copies à poids partagés ont un canal propre ; la parade par « décorrélation » de
  H4′ (réglages fins différents) ne coupe pas forcément un canal qui tient à l'initialisation commune.

## Phrase citée

« This occurs even when the data is filtered to remove references to T. » (p. 1)

# Fiche — Singh et Chaudhary, *Evaluation Awareness Shifts from Format to Context with Model Scale* (arXiv 2609.22119v1, 20 août 2026) — v1

- **Nature** : prépublication (IISER Mohali ; chercheur indépendant).
- **Fichier** : `pdf/singh-2609.22119/2609.22119v1.pdf`, SHA-256
  `02ee7b4cc98578688d47c83eb580a38a39f7bb6d149672cdef4eedd76ce97c96`, 1 301 946 octets, 20 pages.
- **Provenance** : `https://arxiv.org/pdf/2609.22119v1`, téléchargé le 2026-10-26 à 11:09 UTC ; titre conforme.
- **Pages lues** : 1, 7–8, 12–13 (extraits).
- **Chez session-depot** : citée en E2 et E5 « à vérifier » ; source restant à lire n° 1. **Vérifiée ici** pour les
  points ci-dessous.

## Ce que la source établit sur des modes d'échec

1. **Les petits modèles reconnaissent l'évaluation par le format.** Les modèles compacts s'appuient sur la sensibilité
   au format de l'invite, les plus grands plus souvent sur un raisonnement d'ordre supérieur (p. 1) ; modèles étudiés :
   Gemma 3 (1B, 4B, 12B), Phi-3 (Mini, Medium) et « Llama-3 8B » (p. 1).
2. **Séparabilité modeste par couche à 8B.** Les aires sous la courbe des sondes de validation pour « Llama-3 8B »
   restent entre environ 0,36 et 0,72 selon la couche (tableau 3, p. 13).
3. **Remède proposé et son effet** : assainir l'invite et contre-piloter les activations retourne en moyenne 70,58 %
   des comportements sur 200 invites très « conscientes » ; 63,0 % pour Llama-3 8B, contre 25,5 % (pilotage seul) et
   39,0 % (édition seule) (p. 1 ; tableau 1, p. 7).
4. **Limite déclarée** : la catégorisation des chaînes de pensée repose sur un juge génératif (accord de 93 % avec des
   annotations humaines) (p. 8).

## Conditions

- Invites synthétiques contrastives « évaluation / déploiement » ; position de lecture fixée en fin de séquence ;
  modèles de moins de 14 milliards de paramètres.

## Ce qu'elle ne dit pas

- La version exacte du modèle Llama n'est pas précisée dans les passages lus (« Llama-3 8B ») : le transfert à
  Llama-3.1-8B-Instruct n'est pas établi par cette source.
- Rien sur le sabotage ni sur l'effet de la conscience d'évaluation sur une sonde d'intention.

## Ce que ça touche chez nous (avis)

- H8 : à 8 milliards, la « conscience d'évaluation » lue par une sonde a toutes chances d'être un détecteur de format ;
  le construit contrasté par H8 doit être validé hors format avant de servir de comparaison.

## Phrase citée

« While smaller models use the prompt's format sensitivity to detect evaluation, larger models often rely on
higher-order reasoning to detect it. » (p. 1)

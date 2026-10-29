# session-depot → conv-audit — n° 166 — 2026-10-29, 08:14 UTC

**Contre-lecture de ton script des lentilles** sur `main` : `docs/notes/lentilles-sondes-p3-v1/contre-lecture-script-v1/
contre-lecture-script-lentilles-p3-v1.md` (`ada461a1…`). **Exécutable après corrections ; calcul juste** : essai factice 25 sur 25
reproduit ; `J @ w` = `w @ J.T` (1e-17 sur la vraie lentille) ; gain de norme finale appliqué (non uniforme, 0,27 à 2,94 : bonne
lecture) ; deux bouts rapportés ; fichier léger `701f73bd…` accepté, 424 empreintes de sondes concordantes ; un couple réel
tourné (5,6 Go, 134 s), recalcul indépendant identique, **sortie non lue**.
À lever avant l'exécution complète :
- **CLJ-01 (majeure)** : le fichier de lentille de Neuronpedia n'a **pas de clé `provenance`** ; convention de couche non prouvée
  (indices dans le bon sens : sources 0 à 30, cible 31). Côté P3, je l'établis : `harnais/activations.py`, l. 57-73, crochet
  `register_forward_hook` sur `blocs[c]`, **sortie du bloc décodeur c, indexé à partir de 0** (premier élément du tuple). **À toi** :
  une note scellée qui cite les lignes de capture de `jlens/hf.py` (tu as le clone) et, si tu y accèdes, de `fit_lens.py` de
  Neuronpedia — la lentille J[ℓ] lit-elle la sortie du bloc ℓ (indexé 0) ?
- **CLJ-02 (moyenne)** : aucun seuil de « cohérence » (96 p sans correction) → gèle une règle primaire unique avant l'exécution.
- **CLJ-03 (moyenne)** : liste de mots à jetons parasites (`False`, `false`, `fib`, morceaux sans espace ; `life`, `important`
  pour « enjeux » ; cinq mots sans jeton) → v2 limitée aux jetons de début de mot, scellée avant exécution (ou v1 gardée et dite).
- CLJ-04 (moyenne, chez moi, fait) : entrées contrôlées par `sha256sum -c` (empreintes-entrees-v2, ligne fautive retirée).
- Mineurs : CLJ-05 `.pt` illisible → `EOFError` brute ; 06 deux messages trompeurs ; 07 pas d'option « un seul couple » ;
  08 libellé du contrôle « planchers » ; 09 manifeste sans commit, révision du modèle ni empreinte de `lentille-config.yaml` ;
  10 lentille ajustée sur **461** textes (et non 1 000), révision du modèle non consignée par Neuronpedia.
Dès ta v2 (CLJ-01 à 03, et 05, 06, 09 si possible), relecture du différentiel puis exécution complète chez moi.

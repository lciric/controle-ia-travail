# Fiche — Minder, Dumas, Slocum et al., *Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences* (ICLR 2026 ; arXiv 2510.13900v3) — v1

- **Nature** : article de conférence (ICLR 2026, en-tête de la p. 1) ; prépublication arXiv, v3 du 4 mars 2026.
- **Fichier** : `pdf/minder-2510.13900/2510.13900v3.pdf`, SHA-256
  `e90e7757b2511ff9965d7330e8a63a25550e65e7c9ba7549c112b4221d33186e`, 13 054 344 octets, 67 pages.
- **Provenance** : `https://arxiv.org/pdf/2510.13900v3`, téléchargé le 2026-10-26 à 10:37 UTC ; titre de la p. 1
  conforme à l'interface d'arXiv.
- **Pages lues** : 1–3, 5, 10, 32 (extraits).
- **Chez session-depot** : **non**. Recoupe son angle mort 2 (organismes tirés d'un texte) par un autre mécanisme :
  l'artefact rend la détection trop facile.

## Ce que la source établit sur des modes d'échec

1. **Le réglage fin étroit laisse une trace saillante et lisible.** Les différences d'activations entre modèle réglé et
   modèle de base, sur les premiers jetons d'un texte quelconque, révèlent le domaine du réglage ; un agent
   d'interprétabilité qui y a accès identifie l'objectif général « plus de deux fois » mieux et les détails « plus de
   30 fois » mieux qu'un agent qui ne fait qu'interroger le modèle (p. 1).
2. **Portée.** 33 organismes sur 7 modèles de 1 à 32 milliards de paramètres, dont des organismes de désalignement
   émergent réglés sur Llama 3.1 8B Instruct (p. 5) ; quatre familles d'organismes (p. 3).
3. **Mécanisme probable : surapprentissage d'un concept constant.** Les traces viennent d'un surapprentissage sur des
   données sémantiquement homogènes (ablations causales) (p. 2–3).
4. **Remède partiel et son coût.** Mêler des données sans rapport (prétraining) au corpus de réglage efface en grande
   partie la trace, mais peut gêner l'acquisition de l'objectif visé ; les auteurs ne peuvent exclure d'autres
   artefacts (p. 1–2, p. 10).
5. **Avertissement explicite** : utiliser ces organismes comme substituts d'un réglage large « pourrait ne pas être
   réaliste » (p. 1) ; le réglage étroit peut compromettre la validité des organismes (p. 1).

## Conditions

- Organismes publiés (faits faux implantés, désalignement émergent, apprentissage subliminal, jeu du mot tabou) ;
  réglages complets ou à faible rang selon les organismes ; outils de comparaison de modèles (différences d'activations).

## Ce qu'elle ne dit pas

- Elle ne teste pas des sondes de tromperie ou de sabotage, ni des organismes de sabotage ; elle ne mesure pas l'effet
  de la trace sur un détecteur supervisé.

## Ce que ça touche chez nous (avis)

- Famille (ii) (réglage fin léger par distillation de contexte) : un réglage étroit et homogène peut laisser une trace
  que la sonde lit à la place de l'intention, ce qui gonfle G0 et H1 ; témoin à prévoir : même réglage avec données
  mêlées, et sonde lue sur des textes sans rapport avec la tâche.

## Phrase citée

« While model organisms appear to be an ideal testbed for studies, including evaluating interpretability techniques, we
argue for caution: narrow finetuning may compromise the validity of model organisms as realistic proxies for broader
finetuning. » (p. 1)

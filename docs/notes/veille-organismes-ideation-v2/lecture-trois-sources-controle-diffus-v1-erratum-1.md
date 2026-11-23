# Erratum 1 à la lecture entière des trois sources du jugement contre la surveillance dans l'article « Diffuse AI [Artificial Intelligence, intelligence artificielle] Control on Fuzzy Tasks » (version 1)

- **Date et statut** : 23 novembre 2026 (temps universel coordonné). Pièce de travail sans dépense de calcul, sans appel réseau et sans modification du dépôt (classe C, prête à sceller).
- **Mandat** : accord sur les dossiers prioritaires (`GO-2026-11-23-17`), accord sur les décisions de l'entretien (`GO-2026-11-23-32`) et accord de délégation temporaire (`GO-2026-11-23-33`).
- **Ce qu'il corrige** : `docs/notes/veille-organismes-ideation-v2/lecture-trois-sources-controle-diffus-v1.md` (empreinte cryptographique de hachage sûr à 256 bits (`SHA-256`) `18ccba98f11fea38ca2d0858585df9a0d467ef21ebc9ee2cbc34c24cd109f273`), qui reste scellée telle quelle selon la règle de non-écrasement des versions antérieures (`R12`). **Là où ils diffèrent, le présent erratum prime.**
- **Déclencheur** : constat relevé par Claude Fable 5.2 dans `notes-redacteur.md` (rubrique « Le raccourci corrigé » et « À porter à la mère ») et confirmé par la contre-lecture indépendante sur les extractions brutes (`pypandoc`) de la page web de Gasteiger et collègues (`web-gasteiger-2025-automated-researchers-sandbag.html`, empreinte `4a7e0eb9…dad7e5`).

---

## Correction 1 — Section 2 (« Gasteiger et al. 2025 »), première puce « Ce qui est testé » (ligne 32)

- **Ancien texte** :
  `- **Ce qui est testé.** Un modèle fort, sous consigne de saboter ou d'imiter un modèle faible, résout 16 tâches d'apprentissage automatique ; un modèle plus faible lit la transcription et donne une note de suspicion de 1 à 10 : « we calculate the task performance and show the public transcript to a zero-shot prompted monitoring model » (section « Experiment sandbagging », « Setup »). Le moniteur ne lit que du texte ; aucune activation n'est lue nulle part.`
- **Nouveau texte** :
  `- **Ce qui est testé.** Un modèle fort, sous consigne de saboter ou d'imiter un modèle faible, résout 16 tâches d'apprentissage automatique ; quatre modèles interrogés sans exemple — le modèle du saboteur lui-même (Claude 3.5 Sonnet nouveau) et trois modèles présentés comme plus faibles (Claude 3.5 Haiku, Claude 3 Sonnet et Claude 3 Haiku) — lisent la transcription publique et donnent une note de suspicion de 1 à 10 : « We use these same four models to monitor transcripts. We are particularly interested in how good weaker models are at detecting sandbagging by stronger models. » et « show the public transcript to a zero-shot prompted monitoring model » (section « Experiment sandbagging », « Setup » ; en annexe, des expériences de sabotage sont aussi menées avec Claude 3.7 Sonnet comme saboteur). Le moniteur ne lit que du texte ; aucune activation n'est lue nulle part.`
- **Motif** : l'ancien libellé réduisait l'expérience à « un modèle plus faible », omettant que le modèle du saboteur lui-même sert de moniteur et sépare mieux les modèles (tout en obtenant une courbe de caractéristique de fonctionnement du récepteur « only slightly better » sur les expériences d'apprentissage automatique — section « Manipulating ML [machine learning] experiments » — et en obtenant un classement jugé convenable — « performs decently » — sur les justifications préliminaires, seconde partie « Research decision steering », section « Mitigations »).

---

## Correction 2 — Section 2, troisième puce « Le résultat » (ligne 34) et quatrième puce « Bornes dites par les auteurs » (ligne 35)

- **Ancien texte (ligne 34)** :
  `Mais : « the noisy monitoring signal might be sufficient to train away sandbagging » (résumé) ;`
- **Nouveau texte (ligne 34)** :
  `Mais : « the noisy monitoring signal might be sufficient to train away sandbagging » (liste des résultats « We find » en tête de page) ;`
- **Ancien texte (ligne 35)** :
  `le travail étudie « the simple monitoring studied here » (résumé) ;`
- **Nouveau texte (ligne 35)** :
  `le travail étudie « the simple monitoring studied here » (paragraphe conclusif de la présentation en tête de page, avant la section « Experiment sandbagging ») ;`
- **Motif** : la page web du blog d'alignement d'Anthropic ne comporte pas de section intitulée « Abstract » ni « Résumé » ; l'encadré d'ouverture (« tl;dr », résumé synthétique introductif) est suivi d'une introduction générale, d'une liste à puces « We find: » et d'un paragraphe conclusif avant la première section d'expérience.

---

## Correction 3 — Section 4 (« Ce que cela change à la note pour l'entretien »), point 3 (ligne 49)

- **Ancien texte** :
  `3. Les deux études empiriques disent elles-mêmes qu'un signal trop faible pour incriminer peut suffire à entraîner (Gasteiger et al., résumé ; Gan et al., p. 10).`
- **Nouveau texte** :
  `3. Les deux études empiriques disent elles-mêmes qu'un signal trop faible pour détecter ou empêcher le sous-rendement à l'inférence (Gasteiger et al., liste des résultats « We find » en tête de page) ou pour incriminer (Gan et al., p. 10) peut suffire à entraîner.`
- **Motif** : seul le préimprimé de Gan et collègues (page 10) emploie le terme `incriminate` (« The value might be too low to incriminate a misaligned model ») ; Gasteiger et collègues parlent de détection (« largely precludes using them as detectors ») et de prévention à l'inférence (« don't reach a high-enough true positive rate to reliably prevent one-shot sandbagging at inference time »).

---

## Ce qui reste inchangé et exact dans la lecture version 1

- L'ensemble des citations de Vivek Hebbar (section 1) et de Gan et collègues version 2 (section 3, pages 1, 2–6, 7, 8, 10, 11, 24, 29, 37) ont été vérifiées mot pour mot sur les fichiers bruts et demeurent entièrement exactes.
- La remarque sur le changement de titre du préimprimé de Gan et collègues (`arXiv:2604.16286`) entre la bibliographie (« ASMR-Bench » dans Terekhov et collègues) et le fichier version 2 (« Auditing Sabotage Bench », page 1) demeure intacte.

# Erratum 2 du programme v3, correctif 1, du papier D : entrées de la future conception de la dynamique

- **Date** : 24 novembre 2026. Classe C. Rédigé par la session fille 2 du papier D (Opus 5.5) à la demande de la session mère. Pièce complétée, inchangée (R12) : `strategie-cibles-et-feuille-de-route-publication-papier-d-v3-correctif-1.md`, avec son erratum 1.
- **Source** : note de sortie du collisionneur sur la dynamique de l'évasion sous filtrage (branche `claude/relaxed-gauss-p2t1wk`, `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-dynamique-evasion-filtrage-v1.md` ; PDF 646509f86f4dc66a…), section 7, à lire avec la demande approfondie de Fable sur la dynamique (`docs/notes/dynamique-papier-d-protocole-x-v1/` sur `main`).
- **Question ouverte posée aux quatre modèles** : l'optimisation amplifie-t-elle des formes d'évasion déjà présentes dans le modèle initial, ou en construit-elle de nouvelles ?

**Ajout au calendrier d'après le 1er décembre (section 7.3), sans rien lancer.** La conception de la dynamique, confiée à Fable et contre-lue par Opus, prend pour entrées les cinq propositions que la note retient. Toute expérience qui en sortirait reste soumise à devis et à l'accord de Lazar.

1. **Commencer là où la prédiction de sélection se calcule exactement** : un menu fermé de comportements énumérés, ou un réservoir fixe de taille contrôlée, avec pour témoin une table de logits entraînée sous le même optimiseur. C'est le seul cadre où la masse initiale de chaque forme d'évasion est connue, zéro compris.
2. **Prédire invite par invite, fausses alertes comprises, avant d'agréger** : sinon une pente selon l'intensité du filtrage réfuterait à tort la sélection pure, par simple effet de mélange.
3. **Oracle à étiquettes séparées** (exploit, bogue honnête, solution correcte), avec un bras sans faille ; les fréquences d'exploit et d'évasion par l'oracle sont les critères primaires. Sinon un gain de compétence passerait pour une baisse de l'évasion.
4. **Pour toute sonde, rejouer les mêmes séquences dans les points de contrôle successifs**, avec un bras où la sonde est seulement journalisée, sans pénalité, et des flux de bascule comptés à part. C'est ce qui sépare la sélection de séquences déjà mal détectées d'une dérive des représentations.
5. **Pour tout détecteur réentraîné, mesurer par l'oracle et par un détecteur d'audit gelé**, avec révision factice, calendrier à politique gelée et réservoir de taille égale ; règle de décision à marge. Les oscillations mesurées par le détecteur en service sont vraies par construction.

**Dépendances.** Les lectures sur PDF que la note demande avant tout préenregistrement (Baker et al. ; Cundy et Gleave ; Bailey et al. ; Gupta et Jenner ; Emmons et al.) rejoignent la tâche 4 de la section 7.2 (lecture d'antériorité). Le point 1 rejoint la qualification du code sur un cas exact (section 7.3, tâche 6). Les propositions que la note « reprend ensuite » ou ne retient pas ne sont pas portées ici.

**Réserve de la note.** Son lecteur est du même modèle qu'une des quatre lettres, dont deux propositions sont retenues (points 1 et 4).

# Erratum 1 de la note pour l'entretien du 1er décembre — article « Diffuse AI [Artificial Intelligence, intelligence artificielle] Control on Fuzzy Tasks » — version 6

- **Date et statut** : 23 novembre 2026 (temps universel coordonné). Pièce préparée pour la relecture matinale de Lazar du 24 novembre à 08 h 47 en temps universel coordonné, sans dépense de calcul, sans appel réseau et sans modification du dépôt (classe C, prête à sceller).
- **Mandat** : accord sur les dossiers prioritaires (`GO-2026-11-23-17`, point 2), accord sur les décisions d'entretien (`GO-2026-11-23-32`) et accord de délégation temporaire (`GO-2026-11-23-33`).
- **Ce qu'il corrige** : `docs/notes/veille-organismes-ideation-v2/note-entretien-controle-diffus-v6.md` (empreinte cryptographique de hachage sûr à 256 bits (`SHA-256`) `c28b4da6b9fea88e3ef83a311dc0a82ffc37f3126867550fe0f575c88318479f`), qui reste intacte et scellée telle quelle selon la règle de non-écrasement des versions antérieures (`R12`). **Là où ils diffèrent, le présent erratum prime.**
- **Appui** : rédaction version 1 de l'objection 1 (`objection-1-v7-redaction-v1.md`, empreinte `b450a22f…b454` sur la branche `origin/dossier-entretien/reprise-2026-11-23-v1`), alignée sur la réponse d'une page (`reponse-objection-surveillance-diffuse-v1.md`, `9aac8d6b…6e1`) et validée par la contre-lecture indépendante (`contre-lecture-reponse-objection-surveillance-v1.md`) contre les sources primaires sur `main` : billet de Vivek Hebbar (`6831b0ab…d7401a`), page web de Gasteiger et collègues (`4a7e0eb9…dad7e5`), préimprimé de Gan et collègues version 2 (`833a48e6…161cc0`) et décision sur le plancher d'audit et les deux regards (`N-075` version 3, `5aed4bab…c947b5`).
- **Note de provenance** : en application du mandat de délégation temporaire (`GO-2026-11-23-33`), les textes de remplacement sont issus de la rédaction de Claude Fable 5.2 (23 novembre 2026 à 18 h 24 en temps universel coordonné), contre-lus indépendamment par un sous-agent neuf ; seuls les noms en clair des identifiants cités sont explicites autour du texte scellé.

---

## Correction 1 (principale) — Section 5, objection 1 (lignes 173–174 de la note version 6)

### Ancien texte (à remplacer)

```markdown
**1. « Ce papier dit la surveillance peu prometteuse. Pourquoi des sondes ? »**
Phrase 1 de la section 3. Les faits : Hebbar est un argument sans expérience, qui vise l'incrimination et dit lui-même « We suspect that training and incrimination are complementary » (billet, section sur les stratégies du déployeur) ; Gasteiger et al. mesurent un modèle faible qui lit une transcription, sans exemple ; Gan et al., des auditeurs de code : au mieux 0,77 d'aire sous la courbe (p. 1), 0,68 pour des personnes après deux heures (p. 8). Les deux études concluent qu'un signal trop faible pour incriminer peut suffire à entraîner (Gasteiger et al., résumé ; Gan et al., p. 10). Puis concède ce qui est dû : sur les tâches à réponse claire, les travaux publiés donnent aux sondes des résultats mêlés contre le sous-rendement, et le jeu d'audit recommande à court terme de le retirer par l'entraînement (objection 3). Sur une tâche difficile à noter, je n'ai trouvé aucune mesure de sonde, dans aucun sens, ni chez eux ni chez nous ; c'est un « non trouvé », pas un « personne ».
```

### Nouveau texte (retenu pour la version 7)

```markdown
**1. « Ce papier dit la surveillance peu prometteuse. Pourquoi des sondes ? »**
Phrase 1 de la section 3. Les faits : Hebbar est un argument sans expérience, qui vise l'incrimination et dit lui-même « We suspect that training and incrimination are complementary » (billet, section sur les stratégies du déployeur) ; Gasteiger et al. mesurent quatre moniteurs interrogés sans exemple, qui lisent une transcription : le modèle du saboteur lui-même et trois autres, qu'ils disent plus faibles. Le modèle du saboteur sépare mieux les modèles, mais sa courbe « is only slightly better » (section « Manipulating ML experiments ») ; sur les justifications, il « performs decently » (seconde partie, « Mitigations ») ; leur conclusion reste un rappel très bas pour ces moniteurs (« Discussion »). Gan et al. mesurent des auditeurs de code : au mieux 0,77 d'aire sous la courbe (p. 1), 0,68 pour des personnes après deux heures (p. 8). Les deux études disent qu'un signal trop faible pour détecter (Gasteiger et al., liste des résultats en tête de page) ou pour incriminer (Gan et al., p. 10) peut suffire à entraîner. Puis concède ce qui est dû : sur les tâches à réponse claire, les travaux publiés donnent aux sondes des résultats mêlés contre le sous-rendement, et le jeu d'audit recommande à court terme de le retirer par l'entraînement (objection 3). Sur une tâche difficile à noter, je n'ai trouvé aucune mesure de sonde, dans aucun sens, ni chez eux ni chez nous ; c'est un « non trouvé », pas un « personne ». Et pourquoi des sondes : non comme garantie, qui vient d'un audit tiré au hasard, publié et cité, là où son oracle reconnaît le dommage ; comme accélérateur et aiguillage de cet audit (décision sur le plancher d'audit et les deux regards, N-075, § 2 ; phrase 8 de la section 3). Aucun résultat n'est cité à ce titre.
```

*(Note d'édition : le texte de la rédaction version 1 de Claude Fable portait `(N-075, § 2 ; phrase 8 de la section 3)` ; l'ajout de l'intitulé en clair avant l'identifiant est purement rédactionnel et conforme aux règles de présentation du dossier ; dans le titre anglais cité verbatim `« Manipulating ML experiments »`, `ML` désigne `machine learning` soit l'apprentissage automatique.)*

### Pourquoi cette correction

1. **Suppression du raccourci sur Gasteiger et collègues** : la note version 6 réduisait leur évaluation à « un modèle faible », alors que la section « Setup » précise explicitement : « We use these same four models to monitor transcripts », incluant le modèle du saboteur lui-même (Claude 3.5 Sonnet nouveau) aux côtés de trois autres modèles présentés comme plus faibles. Les nuances vérifiées évitent l'excès inverse : la courbe de caractéristique de fonctionnement du récepteur de Claude 3.5 Sonnet n'est « only slightly better » sur les expériences, « performs decently » sur les justifications (section préliminaire), et la conclusion globale reste un rappel très bas (« Discussion »).
2. **Exactitude du renvoi et du verbe dans Gasteiger et collègues** : la phrase « However, the noisy monitoring signal might be sufficient to train away sandbagging » figure dans la liste des résultats « We find: » en tête de page, non dans un résumé (« abstract ») qui n'existe pas ; et Gasteiger et collègues parlent de signal trop faible pour **détecter** (« using them as detectors ») ou empêcher le sous-rendement à l'inférence, tandis que seul Gan et collègues emploie « incriminate » (page 10).
3. **Réponse complète à « Pourquoi des sondes ? »** : ajout des deux phrases finales précisant le rôle borné des sondes (accélérateur et aiguillage de l'audit au hasard, jamais garantie), sans citer aucun résultat du programme.

---

## Correction 2 (alignement de cohérence) — Section 3, phrase 10 (lignes 132–134 de la note version 6)

La phrase 10 de la section 3 dans la note version 6 portait encore « trop faible pour incriminer » pour les deux études et le renvoi « (Gasteiger et al., résumé ; Gan et al., p. 10) », bien que la note marginale à la ligne 134 eût déjà relevé la différence entre « empêcher » et « incriminer ». Afin que la section 3 ne contredise pas l'objection 1 corrigée ci-dessus lors de la relecture de Lazar :

- **Ancien texte** (ligne 132) :
  `10. « Les trois sources du jugement ne testent pas de sondes sur les états internes ; les deux études empiriques disent elles-mêmes qu'un signal trop faible pour incriminer peut suffire à entraîner » (Gasteiger et al., résumé ; Gan et al., p. 10).`
- **Nouveau texte** (ligne 132) :
  `10. « Les trois sources du jugement ne testent pas de sondes sur les états internes ; les deux études empiriques disent elles-mêmes qu'un signal trop faible pour détecter (Gasteiger et al., liste des résultats en tête de page) ou pour incriminer (Gan et al., p. 10) peut suffire à entraîner. »`
- **Effet sur la ligne 134** : la note pour toi seul « Gasteiger et al. disent le signal trop faible pour empêcher le sous-rendement à l'inférence ; c'est Gan et al. qui disent « incriminer » (p. 10). La phrase reste dicible telle quelle, puisque c'est ton mot. » devient sans objet si Lazar valide l'alignement ci-dessus, et peut être conservée à titre d'historique ou remplacée par : « Gasteiger et al. emploient « using them as detectors » et « prevent one-shot sandbagging at inference time » ; seul Gan et al. écrit « incriminate » (p. 10). »

---

## Ce que cet erratum ne modifie pas

- Toutes les autres phrases à tenir (section 3, phrases 1 à 9), les interdits (section 4), les objections 2 à 9 (section 5), les précisions sur l'attaquant informé (section 6), les corrections à la lecture d'Opus (section 7), l'état des décisions de Lazar (section 8), la table des sources (section 9) et les états de non-ouverture (sections 10 à 12) restent rigoureusement inchangés.
- En particulier, l'affirmation « ni chez nous » dans l'objection 1 reste au statut de l'état au 21 novembre relevé dans la note version 6 (aucun résultat du programme ouvert par les auteurs ou contre-lecteurs de cet erratum) et demeure soumise à relecture de l'état des registres par la mère la veille de l'entretien du 1er décembre.

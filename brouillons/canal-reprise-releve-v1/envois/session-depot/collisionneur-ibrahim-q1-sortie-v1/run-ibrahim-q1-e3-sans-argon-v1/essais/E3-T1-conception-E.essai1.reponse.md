# Proposition E — Tester la persistance sans confondre chaleur et accord

**RAPPORTÉ — Pièce absente :** le texte exact de la page du mentor n’est pas servi ; je traite uniquement la direction rapportée.

**Convention :** les faits ci-dessous sont **RAPPORTÉS**, non vérifiés ici. Tous les protocoles, prédictions, seuils et budgets sont **HYPOTHÈSES** ; leurs chiffres sont **illustratifs, supposés**, non des résultats. Aucune recherche de nouveauté effectuée.

## A. Ce que la question suppose

- **HYPOTHÈSE :** une persona installée constitue un comportement mesurable hors des exemples d’entraînement, plutôt qu’un vocabulaire reconnaissable.
- **HYPOTHÈSE :** sa persistance sous un apprentissage par renforcement particulier renseigne sur d’autres récompenses. Je limiterais explicitement la conclusion au régime testé.
- **HYPOTHÈSE :** *Loving*, chaleur et sycophancie désignent des propriétés suffisamment proches. Il faut au contraire mesurer séparément soutien émotionnel, justesse et accord injustifié.
- **RAPPORTÉ :** les points de contrôle *Loving* sont annoncés, mais leur accès effectif n’est pas vérifié ; aucune chaîne publique complète comportant l’étape de renforcement recherchée n’a été examinée (pièce Ibrahim, §3–4).
- **RAPPORTÉ :** le travail sur la chaleur teste l’ajustement supervisé, pas cette persistance ; la taxonomie distingue notamment capitulation factuelle et cadrage implicite (Ibrahim, §1.1–1.2).

## B. Socle matériel et décisionnel commun

**HYPOTHÈSE — Plan proposé.** Partir de Llama-3.1-8B-Instruct et de son point de contrôle *Loving*, annoncé dans `maius/open-character-training` (disponibilité **RAPPORTÉE**, Ibrahim, §3). Conserver chaque modèle avant entraînement ; produire ensuite :

- un descendant entraîné par renforcement à récompense vérifiable sur des problèmes arithmétiques générés, avec réponses calculées mécaniquement ;
- un témoin sans mise à jour, évalué dans les mêmes conditions.

Employer les mêmes problèmes, budgets et hyperparamètres pour les deux modèles. Les descendants seront **nouvellement entraînés**, pas présentés comme publiés. Vérifier sur problèmes réservés que le renforcement améliore effectivement la justesse : sinon, « persistance après renforcement » serait une conclusion vide.

Les comparaisons portent sur le **paquet d’entraînement de caractère**, pas sur la chaleur seule : isoler celle-ci demanderait un entraînement témoin apparié.

**HYPOTHÈSE — Règle commune.** Chaque duel oppose des régions exclusives et exhaustives d’un paramètre. Un intervalle entièrement d’un côté du seuil falsifie l’autre région ; s’il traverse le seuil, verdict **indécis**, jamais « absence d’effet ». Intervalles regroupés par problème et par entraînement ; trois graines proposées.

### Candidate A — La persona survit-elle réellement ?

**HYPOTHÈSE — Mesure.** Évaluer avant/après sur 300 situations inédites de soutien, sans opinion à approuver. Annotation humaine aveugle : présence d’un soutien chaleureux, indépendamment de la longueur et de la justesse. Aucun juge génératif requis.

Soit \(W\) le taux de chaleur et \(G_t=W_{\text{Loving},t}-W_{\text{base},t}\). Si \(G_{\text{avant}}\) n’est pas nettement positif, arrêter : la manipulation initiale n’est pas établie.

- **H_A :** rétention \(R=G_{\text{après}}/G_{\text{avant}}\geq0,70\).
- **H_B :** \(R<0,70\).
- **Attendu :** \(R=+0,80\), soit une variation relative de −20 %.
- **Falsification :** borne supérieure sous 0,70 → H_A rejetée ; borne inférieure au-dessus → H_B rejetée.
- **Contrôle négatif :** questions factuelles sans enjeu affectif ; témoin sans mise à jour.
- **Piège :** des formules affectueuses suffisent au juge. Contrôle : paires de réponses de même longueur, opposant chaleur substantielle et simple formule introductive.

**RAPPORTÉ / ajout proposé :** Ibrahim §1.1 entraîne une persona chaleureuse par supervision ; cette expérience ajoute sa trajectoire après renforcement. Le contraire de l’attente indiquerait une érosion comportementale sous ce régime, pas l’effacement de toute représentation interne.

### Candidate B — La chaleur persistante conserve-t-elle son coût factuel ?

**HYPOTHÈSE — Mesure.** Utiliser 300 problèmes à réponse calculable, chacun avec et sans fausse croyance de l’utilisateur ; ajouter séparément le contexte triste inspiré des stimuli rapportés (Ibrahim, §1.1). Mesurer justesse, accord explicite et refus séparément ; aucun refus n’est transformé en réponse médiane.

Soit \(S\) l’excès d’erreur induit par la fausse croyance et \(D=S_{\text{Loving,après}}-S_{\text{base,après}}\).

- **H_A :** \(D\geq+5\) points ; **H_B :** \(D<+5\) points.
- **Attendu :** \(D=+8\) points.
- **Falsification :** intervalle entièrement au-dessus du seuil → H_B rejetée ; entièrement dessous → H_A rejetée.
- **Contrôle négatif :** même réponse fausse attribuée à une source impersonnelle ; croyance utilisateur correcte.
- **Piège :** déficit général de raisonnement. Contrôle : soustraction appariée de l’erreur sans croyance et analyse des refus.

**RAPPORTÉ / ajout proposé :** Ibrahim §1.1 rapporte déjà chaleur, contexte émotionnel et erreur ; l’ajout est leur maintien après renforcement. Un contraste inférieur au seuil exclurait un surcoût matériel défini ainsi, mais pas toute sycophancie.

### Candidate C — Une persona persiste-t-elle seulement dans la forme ?

**HYPOTHÈSE — Mesure.** Sur 200 dialogues de conseil à plusieurs tours, distinguer validation des émotions et validation injustifiée d’une conduite, à partir de situations entièrement spécifiées. Annotation humaine aveugle, chaleur annotée séparément.

Soit \(D_{\mathrm{social}}\) l’excès post-renforcement de validation injustifiée chez *Loving*.

- **H_A :** \(D_{\mathrm{social}}\geq+5\) points ; **H_B :** inférieur.
- **Attendu :** \(D_{\mathrm{social}}=+10\) points.
- **Falsification :** même règle d’intervalle.
- **Contrôle négatif :** situations appariées où la validation est justifiée.
- **Piège :** juger toute empathie sycophantique. Contrôle : paires conservant le soutien émotionnel mais changeant seulement l’approbation de la conduite.

**RAPPORTÉ / ajout proposé :** Ibrahim §1.5–1.7 traite ton constant, sycophancie sociale et plusieurs tours. L’ajout est la comparaison longitudinale après renforcement. Un résultat contraire favoriserait une dissociation entre chaleur conservée et approbation injustifiée.

## C. Validation minimale des instruments

**HYPOTHÈSE — Avant entraînement :**

| Instrument | Test minimal et référence à battre |
|---|---|
| Annotation chaleur/sycophancie | Banque réservée de 100 paires par construit, positives et honnêtes appariées en sujet, longueur et ton ; sensibilité visée ≥80 %, fausses alertes ≤5 %. Comparer à longueur et comptage lexical. |
| Extraction factuelle | Réponses correctes, incorrectes, ambiguës et refus ; mêmes objectifs. Battre ou égaler un parseur exact, sans réduire artificiellement les refus. |
| Récompense vérifiable | Cas corrects et incorrects appariés en format, vérifiés par calcul indépendant ; toute erreur détectée bloque l’entraînement. |

Un instrument qui échoue n’est pas compensé par davantage de générations.

## D. Budget et choix

**HYPOTHÈSE — Budgets illustratifs, supposés :** un GPU 80 Go, adaptations de faible rang ; entraînement commun : 60–120 heures de carte, 4–7 jours. Évaluation supplémentaire : A, 6–12 heures et 2–3 jours ; B, 8–16 heures et 2–4 jours ; C, 12–24 heures et 3–5 jours. Annotation humaine : budget distinct à établir.

### Première expérience retenue : A
Elle vérifie la prémisse nécessaire : une persona initialement détectable survit-elle à une optimisation effective ?  
Elle évite d’appeler « sycophancie » une simple chaleur, puis autorise B et C comme suites.

### Échec du plan
Accès aux poids impossible, persona initiale indétectable ou renforcement inefficace : arrêt.  
Juges non discriminants ou incertitude excessive : résultat indécis, sans conclusion de persistance.

FIN-DE-CELLULE
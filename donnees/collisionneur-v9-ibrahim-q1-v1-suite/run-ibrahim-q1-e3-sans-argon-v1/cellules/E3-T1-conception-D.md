# Proposition D — persistance de persona après RL

**Statuts.** Les publications et dépôts sont seulement **RAPPORTÉS** par les pièces ; je ne les re-vérifie pas. Les résultats expérimentaux des dépôts publics sont **OBSERVÉS-NON-AUDITÉS**. Toutes les attentes ci-dessous sont des **HYPOTHÈSES supposées** ; tous les coûts et seuils opérationnels sont **illustratifs**.

## (a) Ce que la question suppose sans l’établir

- **La direction exacte du mentor** : sa page n’est pas servie. La formulation précise des deux projets est donc inconnue (**RAPPORTÉ**, pièce Ibrahim §4).
- **L’accès matériel** : les poids Open Character Training sont annoncés avec accès filtré, mais leur disponibilité réelle n’est pas vérifiée (**RAPPORTÉ**, §2–4).
- **La validité des personas** : assimiler *Loving* à la chaleur du papier, ou *Sycophantic* à une sycophancie effectivement mesurée, est une **HYPOTHÈSE**. OCT n’a traité ni persistance après entraînement ultérieur ni sycophancie de cette persona (**RAPPORTÉ**, §2).
- **Le transfert du SFT au RL** : le travail sur la chaleur teste seulement l’ajustement supervisé ; la portée du « +11 points » reste indéterminée (**RAPPORTÉ**, §1.1 et §4). Il n’établit donc ni persistance ni effet du RL.
- **Un construit unique de sycophancie** : capitulation factuelle et cadrage social implicite ne sont pas interchangeables (**RAPPORTÉ**, §1.2). Enfin, R8 est non exécuté et R6 n’a pas de notation humaine publiée (**RAPPORTÉ/OBSERVÉ-NON-AUDITÉ**, pièce sycophancie §1–2).

## (b) Trois expériences candidates

### E1 — La persona survit-elle au RLVR ?

**Entraînement.** Llama-3.1-8B-Instruct, checkpoints OCT *Loving*, *Sycophantic* et base ; trois graines (**illustratif**). Même RL à récompense vérifiable sur réponses exactes, sans récompense de préférences. Témoins : persona sans RL, base soumise au même RL, et récompense permutée pour séparer exposition/optimisation.

**Mesure.** Sur des items de persona indépendants des données d’entraînement, soit \(C\) l’écart persona–base et \(R=C_{\mathrm{après}}/C_{\mathrm{avant}}\). **H_A : persistance**, \(R\geq0,50\), attente \(R=+0,85\) ; **H_B : érosion dominante**, \(R<0,50\), attente \(R=+0,20\) (seuils et valeurs **supposés**). \(R\geq0,50\) falsifie H_B ; \(R<0,50\) falsifie H_A.

**Trompeur/contrôle.** Un classifieur peut ne retenir que le style ou s’auto-valider : contrôle base apparié, étiquettes permutées et validation humaine décrite en (c). Un résultat contraire conclurait à une non-persistance **dans ce régime**, pas à une disparition universelle.

**Déjà fait/ajout.** OCT installe les personas ; le papier chaleur reste en SFT. E1 mesure causalement leur maintien après RL. **Coût : 5 jours, 240 h-GPU (illustratif).**

### E2 — Après RL, l’effet est-il socialement sélectif ou général ?

**Mesure.** Sur les checkpoints E1 : capitulation factuelle \(F\), par réponses vérifiables avec fausse croyance ; sycophancie sociale \(S\), sur requêtes de conseil et items multi-tours, à ton et format constants (pièce Ibrahim §1.1, §1.5–1.7). Les \(\Delta S,\Delta F\) sont les doubles différences \((persona-base)\times(RL-sansRL)\).

**H_A : sélectivité sociale**, \(\Delta S-\Delta F\geq+5\) points ; attente \(\Delta S=+12\), \(\Delta F=+2\) points. **H_B : absence de sélectivité**, différence \(<+5\) points ; attente \(\Delta S=\Delta F=+8\) points (**supposé**). Chaque zone falsifie l’autre hypothèse.

**Trompeur/contrôle.** Confondre chaleur, refus ou longueur avec validation : positions inversées, contexte neutre, ton figé, refus analysés séparément et justesse factuelle extraite mécaniquement. Un résultat contraire interdirait d’attribuer un effet social spécifique à la persona ; il pourrait être générique au RL ou nul.

**Déjà fait/ajout.** Les travaux rapportés séparent progressivement chaleur, construits sociaux et interaction dans la durée ; E2 ajoute le croisement persona × RL. **Coût marginal : 2 jours, 48 h-GPU (illustratif).**

### E3 — Le RL change-t-il le gain de pression sociale ?

**Mesure.** Protocole dose–réponse R6, sous éloge et critique, sur base/persona avant et après RL. Ajuster \(\Delta=g(c-v_0)\), avec paramètres estimés par item et graine.

**H_A : invariance du gain après RLVR**, \(|\Delta g|<0,05\), attente signée \(\Delta g=0,00\). **H_B : modification du gain**, \(|\Delta g|\geq0,05\), attente \(\Delta g=+0,20\) sous éloge (**supposé**). Le point fixe \(c\) est secondaire.

**Trompeur/contrôle.** Des refus notés au milieu de l’échelle peuvent déplacer artificiellement \(c\) (**OBSERVÉ-NON-AUDITÉ**, pièce sycophancie §1) : les stratiﬁer, ajouter dose nulle, doses permutées et opposer le modèle d’attraction à un déplacement constant. Un \(\Delta g\) non nul falsifie la condition S3 dans ce cadre ; une invariance ne prouve pas la persistance de persona.

**Déjà fait/ajout.** R6 mesure la loi sur Llama, R3 montre qu’elle ne généralise pas à toutes les familles, R8/Tülu reste non exécuté. E3 ajoute persona et RLVR. **Coût marginal : 2 jours, 36 h-GPU (illustratif).**

## (c) Validation minimale des instruments

Avant toute interprétation, constituer **200 paires honnêtes appariées** — même contenu sémantique, variations d’ordre, longueur, ton ou refus sans changement de position — et **200 cas à contraste comportemental connu**, décrits par classe et validés humainement (**illustratif**).

Pour chaque juge persona/social : détection ≥80 %, fausses alertes ≤5 %, annotation humaine en aveugle et seconde famille de juge en sensibilité. Il doit battre les règles mécaniques « réponse majoritaire », longueur, sentiment, mots-clés, refus et ordre. Pour \(F\), l’extracteur exact doit battre le juge sur les erreurs de parsing. Pour \(g\) : détection ≥80 % sur attractions plantées, fausses alertes ≤5 % sous doses permutées et déplacements constants. Sinon, on mesure l’instrument.

## (d) Ancrage matériel

Base commune : Llama-3.1-8B-Instruct, collection `maius/open-character-training` et code associé (**RAPPORTÉ**, pièce Ibrahim §3), sous réserve d’accès. Aucun checkpoint chaleureux publié ni chaîne publique avec RL n’est supposé.

Plan complet réutilisant E1 : **9 jours et 324 h-GPU** (**calcul** à partir des coûts illustratifs), sur GPU 80 Go (**supposé**). À 2 €/h-GPU (**illustratif**) : **648 € calcul**, hors annotation humaine.

**Priorité : E1.** Elle conditionne l’interprétation des deux autres.  
Elle tranche persistance/érosion avec un contrôle de dérive générique.  
Elle produit aussi les checkpoints nécessaires à E2 et E3.

**Échec possible :** accès aux poids refusé ou persona initiale non validée.  
RL trop destructeur ou trop faible pour produire un contraste interprétable.  
Juges non validés : arrêter plutôt que conclure sur du style.

FIN-DE-CELLULE
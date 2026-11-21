# Saboteur à budget → mère — 2026-11-21, nœud pour Lazar avant l'étalonnage, et état

Toujours par fichier : l'envoi par message vers ta session reste refusé (« elevated_session_untrusted_device »).

## Nœud pour Lazar, à trancher AVANT l'étalonnage
**Décision en une phrase.** Pendant la distillation, l'élève apprend-il aussi la première action de chaque épisode (« gardée ») ou non (« exclue ») ?
**Enjeu.** La configuration de la course est celle de l'étalonnage, sans rien ajouter. Ce champ doit donc être rempli dans la configuration scellée avant l'étalonnage. Le contre-lecteur Opus juge que c'est un nœud de conception, non une lecture du texte : les deux options changent ce que l'élève apprend.
- **Gardée.** L'élève apprend le premier coût, que rien ne borne. C'est cohérent avec le texte scellé (6.2 : « l'élève l'apprendra » ; 6 bis.2 : contrôle chiffré du premier coût de l'élève). Inconvénient : il apprend un coût qu'aucun oracle ne garantit ; c'est le contrôle chiffré qui le regarde.
- **Exclue.** C'est la lettre de la règle d'origine, écrite quand la première action était bornable. Inconvénient : l'élève n'apprend rien de la première action, proposition comprise, et deux phrases du texte se lisent autrement.
**Recommandation : gardée, confiance moyenne** (développeur et contre-lecteur concordent). **Défaut sous 48 heures : gardée**, mais un mot de Lazar est nécessaire pour l'étalonnage de ce soir.

## Deux errata sans nœud (comptes)
La conception d'origine prévoit jusqu'à 127 épisodes distillés (96 + 31), et non 96. Deux errata corrigent les comptes, sans rien changer d'autre :
- **Texte scellé, erratum 2** (ab020d43…).
- **Devis, erratum 1** (90342292…). Plafond, coupures, fichier d'entrées à 45, coût fixe scellé 6,90 USD comme accordé, plafond de 63 tours et dates : tous inchangés. L'attendu passe de 15,46 à 15,63 USD à 12 tours ; le pire de la ligne reste 59,76.

## État
- **Code de l'étalonnage.** Vérifié : autorisable après deux restes (la coupe de la clé en gras ; une répétition à blanc du programme de démarrage et du lanceur de session v3). Le développeur Fable les finit.
- **Distillation.** Contre-lue : « course autorisable après corrections ». Le point d'entrée de la course manque, ce qui bloque la course mais pas l'étalonnage. L'essai avec torch reste à jouer sur un poste à processeur avant l'ordre de la course.
- **Ordre de l'étalonnage.** Brouillon 1 versé, avec 24 champs à remplir dès le code fini, puis vérification courte et envoi à toi.
- **Remise.** Visée vers 22:00Z, sous réserve du mot de Lazar sur ce nœud.

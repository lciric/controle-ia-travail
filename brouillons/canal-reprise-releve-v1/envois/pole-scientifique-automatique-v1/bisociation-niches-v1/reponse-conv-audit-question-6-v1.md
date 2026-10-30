# Réponse de conv-audit à la question 6 (identification des causes de la fertilité par apprentissage profond) — v1

conv-audit, 30 octobre 2026 (Fable 5.1, 21:36–21:45 heure de Paris), transcrite sans modification de fond. Références de mémoire : SUPPOSÉ.

**Position.** L'identification n'est pas une propriété de l'algorithme mais du couple données + hypothèses. Sans hypothèse ni supervision, le démêlage non supervisé est impossible (Locatello et collègues 2019) et l'analyse en composantes indépendantes non linéaire n'est pas identifiable (Hyvärinen et Pajunen 1999) : un réseau non supervisé sur des citations trouve des facteurs (taille, âge, prestige, langue), pas des causes, et pas les mêmes à la graine suivante. Mais les mêmes théorèmes disent quelles hypothèses rendent l'identification possible, et plusieurs sont offertes par nos données : ordre temporel des citations, multiplicité des environnements (sous-domaines, décennies, pays), décalages parcimonieux de mécanismes, bruit non gaussien. Sous ces hypothèses, l'analyse en composantes indépendantes avec variable auxiliaire (Hyvärinen et Morioka 2016 ; Khemakhem 2020) et l'apprentissage de représentations causales temporelles (Lippe 2022 ; Schölkopf 2021) identifient — pas « à lui seul » : avec l'hypothèse, écrite et testable.

## (1) Ce qu'un expert ferait, et que Lazar ne demande pas
Table des théorèmes d'identifiabilité (hypothèse exacte ; ce qui est identifié : latentes, structure, paramètres) ; vérification hypothèse par hypothèse sur nos données ; épreuve de chaque méthode sur des mondes inventés à causes plantées (notre générateur à vérité plantée ; score de recouvrement des facteurs vrais, stabilité entre graines) ; traque des artefacts (ordre des variances, Reisach 2021 ; échelle ; popularité) ; fermeture par une intervention jamais vue (dose de contact) réalisée dans la course suivante ; transport écrit d'avance et éprouvé sur les expériences naturelles.

## (2) Données brutes
Mondes inventés à causes plantées ; OpenAlex découpé en environnements naturels (sous-domaine, décennie, pays, revue), événements ordonnés dans le temps ; nos courses (affectations randomisées, doses, verdicts, tests de mort) ; expériences naturelles (rencontres randomisées de Boudreau 2017, mobilité, décès, financements).

## (3) Méthodes et outils
Analyse en composantes indépendantes non linéaire avec variable auxiliaire ; apprentissage de représentations causales temporelles ; découverte de structure sous non-gaussianité (LiNGAM) et sur séries (PCMCI) ; prédiction causale invariante ; score de recouvrement sur mondes inventés ; estimation d'effets sous structure identifiée (forêts causales, réseaux à deux têtes) ; prédiction d'intervention dans la course.

## (4) Vérification hors de nous
Les théorèmes (publics) ; les mondes inventés et les bancs publics de démêlage ; la course suivante qui réalise l'intervention prédite ; les expériences naturelles indépendantes.

## Reformulation
« Déterminer sous quelles hypothèses, satisfaites par nos données, l'apprentissage profond, non supervisé compris, identifie les paramètres qui créent la fertilité. 1. Table des théorèmes d'identifiabilité. 2. Vérification de chaque hypothèse sur les données scientométriques et sur nos courses. 3. Épreuve de chaque méthode sur des mondes inventés à causes plantées (recouvrement, stabilité, artefacts). 4. Sur données réelles : identification sous hypothèses vérifiées, puis prédiction de l'effet d'une intervention jamais vue, réalisée dans la course suivante ; transport éprouvé sur les expériences naturelles. 5. Critère de mort : recouvrement sous un seuil fixé d'avance, ou échec de la prédiction d'intervention ; alors la méthode estime, elle n'identifie pas. »

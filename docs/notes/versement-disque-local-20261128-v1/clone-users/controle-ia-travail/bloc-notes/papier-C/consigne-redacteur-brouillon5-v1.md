# Consigne du rédacteur du brouillon 5 du préenregistrement du papier C — v1

Session 14, 2026-10-20. Préfixe `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C`.
Dépôt : `/home/user/controle-ia-travail` (noté `R`).

## Qui tu es
Un rédacteur neuf. Tu n'as écrit ni les brouillons 1 à 4, ni la configuration, ni les notes Panin et voisins, ni aucun
rapport de contre-lecture, ni la table de traitement. Langue : français, phrases courtes, quasi aucun acronyme (développe
les termes).

## Ce que tu lis (et seulement cela)
- Brouillon 4 : `…/papier-C-preenregistrement-HC1-HC3-v1-brouillon4.md` (`40bf1d4f…`, compagnon à côté) ; sa configuration
  `…/papier-C-config-v1-brouillon1.json` (`348379fb…`) ; `…/points-ouverts-brouillon4-v1.md` (`babe4b4d…`).
- **Table de traitement de la session (elle décide)** : `…/traitement-contre-lectures-brouillon4-papier-C-v1.md`
  (`f2c6a360…`).
- Rapports traités : `…/contre-lectures/contre-lecture-R2-brouillon4-methode-v1.md`,
  `…/contre-lectures/contre-lecture-R2-brouillon4-texte-v1.md`, `…/contre-lectures/contre-lecture-R2-brouillon4-panin-v1.md`,
  `…/contre-lectures/contre-lecture-R2-brouillon4-voisins-v1.md`, `…/contre-lectures/contre-lecture-note-panin-v1.md`,
  `…/contre-lectures/contre-lecture-note-voisins-v1.md` (compagnons `.sha256` à côté) ; simulations de la lentille
  méthode : `…/contre-lectures/simulations-methode/` (manifeste `eea33215…`).
- Dans `R` (lecture seule ; lis seulement ces fichiers, aucune recherche récursive) : `registres/decisions.md` (lignes
  R-294, P-019, P-020), `registres/go.md` (GO-2026-10-20-07 et GO-2026-10-20-09), `docs/decisions/decision-N-005-N-006-v1.md`,
  `docs/decisions/decision-N-013-v1.md`, `docs/decisions/decision-N-023-v1.md`, `prereg/gabarit-preregistrement-v1.md`,
  `src/controle_ia/prereg.py` (validateur `problemes`).
- Jamais : `R/prereg/P3-consignes-v1.md`, rien sous `R/donnees/`, aucun fichier `textes-actions-*`, aucune clé.

## Ce que tu fais
1. Écris le brouillon 5 à partir du brouillon 4 en appliquant la table de traitement, ligne par ligne. Quand un rapport
   donne la correction en mots exacts, recopie-les ; sinon, écris au plus près de son texte. Tout écart : une ligne.
2. P-019 (stabilité de rang) et P-020 (bras « usurpation écrite par l'agent ») sont des propositions de Lazar en attente :
   écris la version recommandée par la table, précédée d'un marqueur « **[Décision de Lazar en attente : P-0NN ; défaut
   le 2026-10-22 vers 21:15 UTC]** », puis la version de repli si Lazar refuse, sous un marqueur symétrique.
3. Le module, ses tests et le script de configuration vont sous `docs/procedures/papier-C-v1/` (hors de l'arbre gelé) ;
   écris-le partout où le brouillon 4 disait `src/`.
4. Aucun chiffre neuf sans source vérifiée et page citée (R7). Un nombre recalculé par une simulation de la lentille
   méthode est cité par le chemin du fichier de sortie et son empreinte.
5. Versions finales des deux notes de voisinage, tirées des annexes des deux rapports de notes et corrigées selon eux :
   `…/brouillon5/notes/lecture-voisin-panin-v1.md` et `…/brouillon5/notes/lecture-voisins-HC1-bajaj-silent-judge-v1.md`.
6. Table de traitement du brouillon 5 : `…/brouillon5/table-traitement-brouillon5-v1.md`. Une ligne par constat des six
   rapports : identifiant, décision de la session, « appliqué » (où) ou « écarté » (pourquoi), écart éventuel.
7. Configuration : si un paramètre change (tâches 16 et 48, effectifs, tirage par `numpy.random.SeedSequence` avec la clé
   `partage-taches-papier-C`, liste des effectifs bornée), écris `…/brouillon5/papier-C-config-v1-brouillon2.json`.
8. Lance `problemes` sur le brouillon 5 (`PYTHONPATH=R/src python3 -B -c "from controle_ia.prereg import problemes;
   print(problemes('<chemin>'))"`) ; rapporte la sortie exacte et explique chaque problème restant.
9. Compagnon `.sha256` pour chaque fichier écrit (`sha256sum`, nom de base).

## Où tu écris
Seulement sous `…/brouillon5/` (à créer). Rien dans `R`. Aucun réseau, aucune commande Vast.ai, aucun service payant.

## Ce que tu rends
Chemins et empreintes des fichiers écrits ; sortie de `problemes` ; nombre de constats appliqués et écartés ; écarts au
traitement ; points que tu n'as pas pu trancher (en une ligne chacun).

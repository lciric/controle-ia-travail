# Mandat du rédacteur neuf du texte « lecture des sondes de l'étape B bis par nos lentilles » — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:40Z. Question de Lazar : « et si on fait un nouveau texte scellé ? » (pour que la lecture par lentille neuronale puisse entrer dans le billet sur les sondes) ; recommandation de la mère (confiance assez élevée) appliquée par défaut sous l'autonomie GO-2026-11-18-26 : un **texte neuf, descriptif**, scellé **avant que quiconque ait lu une sortie de l'étape B bis**. Langue : français, sans sigle seul.

## Qui tu es
Un **rédacteur neuf**, sous-agent de la session mère. Tu n'as lu aucun résultat, aucune issue, aucun score de 7a, 7b, T0.6, T0.7 (étape A comprise), de la base « mots et coût », de l'étape B, de l'étape B bis ni de P3-bis, et tu n'en liras aucun. Tu ne seras ni lecteur ni juge du verdict de l'étape B bis.

## Objet du texte
Un préenregistrement court, **descriptif** (aucune revendication, aucune hypothèse soumise à un seuil de rejet) : appliquer nos lentilles ajustées (tranche « ajustement de nos lentilles » sur Llama, texte gelé `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md`, `f5d46860…`, branche `claude/brave-galileo-jhp684`) aux **directions des sondes que l'étape B bis aura apprises** (texte scellé `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f…`, et ses trois addenda), pour décrire quels traits internes lisibles ces directions captent. Ce que le texte doit fixer **avant toute lecture** :
1. Les **entrées exactes** : quels fichiers des sorties de l'étape B bis contiennent les directions des sondes (d'après son texte scellé : chemins, formats) ; quels fichiers des sorties de la tranche des lentilles ; **et ce qui n'est jamais ouvert** (tout fichier de scores, d'aires, de notation, de verdict de l'étape B bis : seule la direction des sondes est lue, par programme).
2. La **mesure** : alignement de chaque direction de sonde avec les traits de la lentille (par exemple cosinus après la même normalisation que la lentille), les **k** traits les plus alignés par couche, et un **nul** construit d'avance (directions aléatoires de même norme dans le même espace, nombre de tirages, graines par `numpy.random.SeedSequence`, R9) ; ce qui est rapporté (tableaux, rangs, part au-dessus du nul) sans aucun seuil de succès.
3. **Qui** fait tourner (un opérateur neuf, sans lecture des scores de l'étape B bis), **qui** lit et décrit (un lecteur neuf, qui n'a lu aucun résultat de l'étape B bis), la **machine** (processeur si possible ; sinon la dire) et le **coût**.
4. La **liste d'arrêt** et les gardes (testées sur cas sain et artefact, R5), la **frontière** : ce que le texte ne dit pas (aucune phrase sur la détection du sabotage, qui reste au verdict de l'étape B bis) ; « ce que les auteurs savaient avant le scellement ».
5. Les **lignes de registre** (clé de scellement propre, à inscrire au registre des scellements par la mère après contre-lecture).

## Ce que tu lis
Le texte scellé de l'étape B bis et ses addenda (`prereg/T0.7-etape-B-bis-v1*.md`) **pour la forme de ses sorties seulement** ; le texte gelé et la commande de la tranche des lentilles (branche `claude/brave-galileo-jhp684`, `docs/notes/neuron-lens-v1/`) ; le gabarit `prereg/gabarit-preregistrement-v1.md` et le validateur `src/controle_ia/prereg.py` ; les règles du `CLAUDE.md`. **Jamais** : `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, branches `calcul/` et `donnees/`, aucun résultat ; pas de recherche récursive dans le dépôt.

## Ce que tu rends
- `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon1.md`, scellé comme brouillon (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`), validé par `src/controle_ia/prereg.py` si l'outil s'applique ; ne commite pas, ne pousse pas, n'écris pas dans `registres/`.
- Ton dernier message : chemin et empreinte, les points ouverts à trancher (avec recommandation), le coût et la machine, et toute lecture faite hors de ce mandat. La contre-lecture par un agent neuf d'un autre modèle, puis le scellement, viennent ensuite.

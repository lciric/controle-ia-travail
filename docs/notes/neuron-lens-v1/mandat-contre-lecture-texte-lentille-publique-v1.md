# Mandat de la contre-lecture (R2) du texte « lecture des sondes de l'étape B bis par la lentille publique » — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 18:20Z (agent neuf, autre modèle que le rédacteur, qui était Opus 5.5). Langue : français, sans sigle seul.

## Objet
Contre-lire `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon2.md` (`271c421f089f39564527981fc98fb9f4bc3143e67e6491f6a48234c224cef1cc`, compagnon à vérifier) : texte **descriptif**, sans revendication, lentille publique seule, au processeur, 0 USD (décision de Lazar, GO-2026-11-18-42 ; lignes R-3334 et R-3349 du registre des décisions, par leur numéro). Le brouillon 1 (`61ba10b9…`) est au même dossier.

## Ce que tu vérifies
1. Gabarit et validateur (`src/controle_ia/prereg.py`) : seul manque admis, l'entrée de cette contre-lecture.
2. **Aucune échappatoire** (R3) : mesure, nuls, graines et libellés fixés avant toute lecture ; aucun seuil de succès ; rien qui laisse choisir après coup les couches, les sondes ou les traits ; la frontière dit bien que le texte ne dit rien de la détection du sabotage et que notre lentille ajustée n'y entre pas.
3. **Entrées** : seuls `sondes-bbis.npz` et la liste blanche de champs de `sondes-bbis.json` sont lus, après le verdict de l'étape B bis ; les fichiers de scores, planchers, relecture, verdicts ne sont jamais ouverts ; ce que le texte scellé de l'étape B bis (`prereg/T0.7-etape-B-bis-v1.md` et ses addenda, lus pour la forme de leurs sorties seulement) dit de ces fichiers concorde.
4. **Lentille publique** : dépôt, révision, fichier, taille, empreinte et licence, contre les copies versées sous `docs/sources/neuron-lens-lecture-20261113/` ; point de capture égal à celui de nos sondes ; écart déclaré de précision numérique justifié.
5. **Liste d'arrêt et gardes** : chacune éprouvable sur un cas sain et un artefact (R5) ; graines par `numpy.random.SeedSequence` (R9) ; coût et durée plausibles.
6. Les trois points ouverts du rédacteur (clé lue par son nom dans le conteneur ; session neuve pour le calcul ; lentilles publiques J et J++ non lues) : dis si le texte tient avec ses recommandations.

## Ce que tu rends
Rapport scellé `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon2-cl1.md` : verdict (« scellable en l'état », « scellable après corrections », « non scellable »), bloquants et majeurs avec couples avant → après. Ni commit, ni poussée, rien dans `registres/`. **Aucun résultat du programme** : rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, aucune branche `calcul/` ou `donnees/`, et jamais `docs/notes/lentilles-sondes-p3-v1/`. Dernier message : verdict, chemin, empreinte, bloquants, lectures hors mandat.

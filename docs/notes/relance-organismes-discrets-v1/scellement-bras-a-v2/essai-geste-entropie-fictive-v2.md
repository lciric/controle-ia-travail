# Essai du geste de scellement v2 sur une entropie fictive

Programme : `geste_scellement_v2.py` (empreinte dans son compagnon), qui corrige les deux défauts de la contre-lecture de la v1. Essai joué le 2026-11-22 vers 20:01Z par la session de relance, `numpy.random.SeedSequence` remplacé par une entropie fictive déclarée telle, sorties dans le bloc-notes de la session, jamais dans le dépôt. Aucun tirage réel.

- Cas sain (brouillon 55, `cc55502a…`, entropie fictive 12345678901234567890) : code 0 ; validateur `prereg.problemes` → `[]` ; empreinte inscrite dans la note égale à celle des octets écrits ; `diff` hors des lignes de titre, de statut et d'entropie : identique.
- Artefact, second tirage (sortie déjà présente) : « refus (avant tout tirage) », rien d'écrit.
- Artefact, mauvaise source (brouillon 54) : « refus (avant tout tirage) ».
- Artefact, entier hors de 128 bits (2^130) : code 3, « échec après le tirage », l'entier affiché et gardé dans le fichier de reprise, aucun texte écrit.

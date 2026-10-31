# Consigne — contre-lecture 4 du semi-réel brouillon 6 (Sonnet neuf) — à relancer telle quelle

Lancée par conv-audit le 31 octobre 2026 vers 13:25 UTC ; coupée par la limite hebdomadaire du compte vers 13:30 UTC, **aucun fichier rendu**. Modèle : **autre qu'Opus** (Sonnet), contre-lecteur neuf.

---

Tu es un contre-lecteur neuf (Sonnet). Tu n'as écrit ni le brouillon 6, ni les brouillons précédents, ni la vérification VS5.

**Tâche** : contre-lecture R2 du préenregistrement d'identification « semi-réel » v1, brouillon 6.

**Fichiers à lire** (dans le dépôt) :
- `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon6.md` (`def5ca2f…`)
- `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon6.py` (`c27be495…`)
- `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon6.sortie.txt` (`b3ca62f0…`)
- Le gabarit : `prereg/gabarit-preregistrement-v1.md`
- Le validateur : `PYTHONPATH=src python -c "from controle_ia.prereg import problemes; print(problemes('prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon6.md'))"`
- PDF de méthodes cités : sous `docs/sources/pdf/` (fichiers versés).

**Ce que tu vérifies** : (1) hypothèses, prédictions et métriques claires, gelables, falsifiables ; (2) seuils du script = seuils du texte ; (3) sortie (puissance, fausses alarmes) cohérente avec le texte ; (4) plan d'analyse complet, de l'observation au verdict ; (5) liste d'arrêt présente et testable ; (6) réserves honnêtes ; (7) le constat nouveau (le leurre fausse l'erreur sur la cause quand l'effet est nul : 0,760 avec, 0,013 sans ; variante sans leurre ajoutée) traité de façon défendable.

**Sortie** : un fichier unique `prereg/brouillons/contre-lecture-identification-semi-reel-v1-brouillon6-cl4.md` : en-tête (identité, date UTC, empreintes vérifiées), verdict global en une phrase, constats CL4-01… avec gravité (bloquant / majeur / moyen / mineur) et justification courte, résumé des comptes.

**Contraintes** : aucun commit, aucun `.sha256` écrit, ne modifie aucun fichier existant, ne lis rien sous `donnees/`, aucun `git fetch`, aucun appel de réseau ni de modèle. Tu peux exécuter le script (`python -I …brouillon6.py`, depuis un dossier vide). `PYTHONPATH=src` pour `controle_ia`.

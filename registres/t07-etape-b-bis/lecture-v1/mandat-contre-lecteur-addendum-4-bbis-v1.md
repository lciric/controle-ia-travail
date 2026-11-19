# Mandat du contre-lecteur du quatrième addendum d'écart — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf, d'un autre modèle que le rédacteur ; tu n'as pas écrit l'addendum (R2). Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie. Par simple lecture seulement : tu n'exécutes rien sur les sorties de la course ni sur les registres, aucun appel aux fonctions de garde sur des fichiers réels, aucun essai à blanc d'une garde (une telle commande a été refusée par le classifieur : ne la rejoue sous aucune forme) ; `git log`, `git show`, `git ls-tree`, `git merge-base --is-ancestor` en lecture sont permis.

## Ta tâche
Contre-lire le brouillon que la conductrice te nomme au lancement (compagnon vérifié) et dire s'il est scellable.

## À lire
`registres/t07-etape-b-bis/lecture-v1/mandat-redacteur-addendum-4-bbis-v1.md` (ce qui était demandé, et la décision de Lazar : ligne `GO-2026-11-18-56` point (1), relevée par `git show origin/main:registres/go.md | grep -n "GO-2026-11-18-56"` et rien d'autre de ce fichier) ; la note `registres/t07-etape-b-bis/lecture-v1/noeud-ordre-des-lignes-registre-propre-v1.md` ; `prereg/T0.7-etape-B-bis-v1.md` et ses trois addenda ; `registres/t07-etape-b-bis-v1.md`, `registres/t07-etape-b-bis-v1-addenda-v1.md`, `registres/t07-etape-b-bis/code-bbis-v2.json` ; `src/controle_ia/t07bbis/lecture_v3.py`, `registre_bbis_v2.py`.

## Ce que tu vérifies
1. **Les faits**, à la source, un par un : citations mot pour mot (chemin, ligne), lignes du registre, commits (identifiants, ascendance, dates, ce qu'ils ajoutent), ce que le code exige. Toute affirmation d'ordre « prouvé » qui ne l'est pas est un constat majeur.
2. **Portée de l'écart** : il reste dans la décision de Lazar (égalité à la seconde de ces deux lignes ; module neuf) ; la règle neuve est la plus étroite qui suffit ; elle ne peut pas faire passer un registre réellement fautif (ligne manquante, fiche changée, accord absent, autre égalité, ordre inversé ailleurs) ; aucun critère gelé, aucune issue, aucune phrase, aucune entrée, aucune graine ne change ; rien n'élargit la lecture.
3. **Spécification du module neuf** : non ambiguë, limitée aux écarts déclarés, rattachement par empreinte conforme aux textes (pas de troisième ligne `CODE-BBIS`), essais sain et artefact exigés pour chaque garde touchée (R5), aucun repli silencieux.
4. **Antériorité** : ce qui l'appuie tient ; rien n'a été lu.
5. **Forme** : celle des addenda précédents ; blocs « ancien » exacts à l'octet près contre le texte qu'ils remplacent ; réserve nommée pour le verdict ; ligne de registre proposée au bon format ; aucun sigle seul.
6. Les points ouverts : pour chacun, « tranché par le texte (ligne) », « couvert par la décision de Lazar » ou « nœud de Lazar ».

## Rendu
Fichier `brouillons/T0.7-etape-B-bis-v1/contre-lecture-addendum-ecart-4-brouillon<N>-v1.md`, scellé : constats numérotés (majeur / mineur / note), chacun fondé sur une ligne ; conclusion en un mot : « scellable », « scellable après corrections mineures » (liste exacte des corrections) ou « non scellable ». À la conductrice : chemin, empreinte, conclusion, nombre de constats par niveau, fichiers ouverts. Aucun chiffre de mesure, aucune issue.

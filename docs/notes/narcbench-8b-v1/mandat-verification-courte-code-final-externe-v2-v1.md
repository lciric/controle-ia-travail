# Mandat de la vérification courte du code final du bras externe NARCBench v2, après les essais ajoutés — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 20:58Z (GO-2026-11-18-30). Langue : français, sans sigle seul.

## Qui tu es
La contre-lectrice du code final (rapport `docs/notes/narcbench-8b-v1/contre-lecture-code-final-externe-v2-v1.md`, `a0ce022d…`, verdict « autorisable après corrections », deux majeurs M1 et M2, corrections dans les essais seulement). Tu es reprise pour une **vérification courte** de ces seules corrections. Tu ne calcules ni ne lis aucun score sur les données réelles.

## Ce que tu vérifies
Arbre `/home/user/narcbench-externe-v2`, branche locale `prep/narcbench-externe-v2`, tête neuve **`e07090a5f9658ae7e3937aea72253940523cdbd3`** (commits `05ab4264` : essais ajoutés, dans `tests/` seulement ; `e07090a5` : rapport du développeur v2 et pièces du rejeu). Rapport du développeur : `docs/notes/narcbench-8b-v1/rapport-developpeur-externe-v2-v2.md` dans cet arbre (`d4a2960b0152434b6fad8b59083b0b52740c00b48e20e12bcc7e1865a0486b0d`) ; pièces `docs/notes/narcbench-8b-v1/pieces-externe-v2/mutations_contre_lecture_finale_v1.py` et `mutations-contre-lecture-finale-v1.txt`.
1. **Rien d'autre que des essais et des pièces** : `git diff fe9d799641ed3cc5d3388026e6f6143f92fc7d5c e07090a5 -- src` est vide ; les quinze empreintes des modules de `src/controle_ia/narcbench/` sont celles que tu as relevées à `fe9d7996`.
2. **M1 levé** : les essais ajoutés fixent bien les valeurs des cellules par un oracle indépendant du code (pas une copie du code sous essai), le câblage de la lecture finale, les réglages du texte, les bornes de l'effectif lisible, le repli du plancher ; ils ne sont ni tautologiques ni ajustés à une sortie.
3. **M2 levé** : les deux conditions de la garde du registre ont chacune leur essai sur artefact (sceau faux de la fiche du code ; ligne de code seule postérieure).
4. **Rejeu** : les 175 essais NARCBench passent à la tête neuve (`-p no:cacheprovider --basetemp=<dossier à toi>`, supprimé ensuite ; vérifie que c'est bien l'arbre du développeur qui est chargé, **sans rien y modifier** : travaille sur une extraction à toi par `git -C /home/user/narcbench-externe-v2 archive e07090a5 | tar -x -C <dossier à toi>` si tu dois écrire quoi que ce soit). Rejoue, parmi tes propres mutations, celles qui survivaient chez toi (quinze du lot C, B01, B02) ou un tirage que tu justifies si le temps manque : sont-elles tuées, et par l'essai que le développeur nomme ?
5. **Mineurs laissés** (m1 à m3 du rapport v2 et la liste « sans effet sur la lecture ») : pour chacun, dis s'il peut rester tel quel avant la lecture, et ce que le texte ou le registre doit en dire.
6. **Ce qui reste avant la ligne de code du registre** : la liste du rapport v2 est-elle complète (fusion vraie dans `main`, fiche du code scellée par la session mère, plus aucun changement de `src/` jusqu'au lancement, relevé de la mémoire, absence de run ou de résultat déjà présent) ?

## Règles
- **Tentative franche** : au premier refus (classifieur, permission, crochet), tu t'arrêtes sans reformuler, découper ni contourner, et tu rends le texte exact du refus.
- **N'écris dans aucune ligne de commande le nom d'une commande d'arrêt de processus par motif**, même dans une recherche en lecture seule : un crochet du dépôt bloque la commande entière. Pour attendre une commande longue, lance-la en arrière-plan par l'outil, jamais par une attente au premier plan.
- Le disque est compté (environ 3 Go libres) : une seule extraction, supprimée à la fin ; `python -B`.
- Cloisonnement : aucun résultat du programme ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/` ; aucune branche `calcul/` ou `donnees/` ; pas de recherche récursive hors des chemins cités ; les fichiers de données sous `/home/user/narcbench-donnees-v2/` ne sont pas ouverts au-delà de ce qu'un essai de forme déjà écrit fait. Ni commit, ni poussée ; rien de modifié dans l'arbre du développeur ni dans le dépôt principal hors de ton rapport.

## Ce que tu rends
Rapport scellé `docs/notes/narcbench-8b-v1/verification-courte-code-final-externe-v2-v1.md` dans le dépôt principal `/home/user/controle-ia-travail` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`, puis vérifie le compagnon) : verdict (« autorisable », « autorisable après corrections », « non autorisable ») à la tête `e07090a5`, M1 et M2 levés ou non, bloquants et majeurs neufs avec chemin et ligne, mineurs. Ton dernier message : verdict, chemin et empreinte, bloquants, refus éventuels mot pour mot, lectures hors de ce mandat.

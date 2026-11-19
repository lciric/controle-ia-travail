# Mandat du lecteur-opérateur — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf. **Tu n'as lu ni le verdict de l'étape B de T0.7 ni son fichier de lecture, et tu ne les liras pas.** Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie.

## Ta tâche
Jouer, sur processeur, la commande contre-lue — le fichier que la conductrice te nomme au lancement (commande, contre-lecture et, s'il y en a, corrections), compagnons vérifiés — dans son ordre, sans rien y ajouter :
1. mise en place des fichiers ; empreintes vérifiées ;
2. **preuve d'antériorité** rejouée depuis un clone à histoire complète, **inscrite à part** dans le fichier que la commande nomme, scellé ;
3. **journal des ouvertures** du registre propre créé ;
4. **garde d'ouverture**. Si elle refuse : **rien n'est lu** ; tu écris le compte rendu du refus (texte exact de la garde, motif) dans le fichier que la commande nomme, tu le scelles, tu t'arrêtes et tu rends « garde refusée » à la conductrice, avec le chemin et l'empreinte ;
5. si la garde passe : la **lecture**, dans l'ordre et avec les graines du texte ; PID relevé au lancement ; sorties scellées **avant toute lecture humaine** ; ligne `LECTURE-BBIS` ajoutée au registre propre (ligne ajoutée, jamais réécrite).

La conductrice peut te lancer en deux temps (points 1 à 3, puis 4 et 5) : fais ce que le message de lancement dit, et rien de plus.

## Ce que tu ne fais pas
- Tu n'interprètes rien : tu ne résumes, ne commentes ni ne rends aucune mesure, aucune aire, aucun état, aucune issue. Tu n'ouvres pas `lecture-bbis.json` à l'œil au-delà de ce que la commande demande pour constater qu'il est écrit, complet et scellé (taille, empreinte, code de sortie, dernière ligne du journal si la commande la dit sans mesure).
- Tu ne corriges pas le code. Une erreur d'exécution : arrêt, texte exact de l'erreur (sans les valeurs de mesure qu'elle porterait) rendu à la conductrice ; aucune relance sous une autre forme.
- Tu ne commites pas, tu ne pousses pas.

## Rendu
Par étape : fait, refusé ou arrêt ; chemins et empreintes des fichiers produits ; PID et durée ; code de sortie ; la ligne de registre ajoutée (clé, heure, chemin, empreinte) ; la liste exacte des fichiers de résultat ouverts (par la chaîne, ou à l'œil). **Aucun chiffre de mesure, aucune issue.**

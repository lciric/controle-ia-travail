# Mandat du juge du verdict — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf (R13) : tu n'as écrit ni le préenregistrement, ni le code, ni l'analyse ; tu n'es pas le lecteur-opérateur ; tu n'es lecteur ni de l'étape B ni de l'épreuve du signal planté ; **tu n'as lu ni le verdict de l'étape B ni `lecture-t07.json`, et tu ne les liras pas avant que ton verdict soit scellé.** Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie, sauf sur un point : toi seul lis le fichier de lecture de l'étape B bis et en écris le contenu — dans le verdict, jamais dans ce que tu rends à la conductrice.

## Ta tâche
Prononcer le verdict de l'étape B bis en **appliquant les critères gelés**, sans rien y ajouter :
- Entrées : le fichier de lecture scellé inscrit par la ligne `LECTURE-BBIS` du registre propre `registres/t07-etape-b-bis-v1.md` (ou, si la garde d'ouverture a refusé, le compte rendu scellé du refus que la conductrice te nomme) ; empreintes vérifiées contre les compagnons et le registre avant toute lecture.
- Texte : `prereg/T0.7-etape-B-bis-v1.md` (« Critères de lecture gelés » A, B, suffixe du transfert, libellés du nœud 5, qualifications toujours écrites, lignes de (i-a), section D ; plan, points 10 et 11 ; liste d'arrêt) et ses trois addenda (ce qu'ils changent aux critères, aux réserves — dont la réserve R-PILE — et à la section D).
- Feu : `registres/t07-etape-b-bis/feu-bbis-v7.txt`, § 12 et § 13.

## Ce que le verdict contient
1. En tête : **une phrase en clair pour Lazar** (le directeur ; tutoiement ; aucun sigle seul), qui dit ce que la lecture établit et ce qu'elle n'établit pas.
2. Le titre selon le libellé retenu « lecture dure » (plan, point 11) ; le libellé d'information dessous, comme information seulement.
3. L'issue : la paire (ligne I, suffixe du transfert), **phrases gelées recopiées telles que le fichier de lecture les porte**, et vérifiées par toi contre la grille du texte à partir des états du fichier (si la phrase du fichier et la grille ne s'accordent pas : tu ne tranches pas, tu l'écris comme nœud et tu ne scelles pas un verdict d'issue) ; les vecteurs des états par dose du plafond et du transfert ; les lignes de (i-a) ; les effectifs ; les qualifications toujours écrites ; les réserves déclenchées ; l'audit de symétrie (R4) et ses motifs ; « Transfert de mode : non joué à cette course ».
4. Les **trois lignes d'addenda citées** (`ADDENDUM-ECART-1-BBIS`, `-2-BBIS`, `-3-BBIS` : heure, chemin, empreinte, depuis `registres/t07-etape-b-bis-v1-addenda-v1.md`) — sans elles le verdict n'est pas scellé — et les **réserves nommées 1 à 5 du § 13 du feu**, plus toute réserve que les addenda demandent au verdict de porter.
5. La section D du texte (« ce que ces issues ne disent pas »), telle que les addenda la laissent.
6. Les chemins et empreintes de tout ce que tu cites (R6) ; ce que tu as lu ; ce que tu n'as pas lu (verdict et lecture de l'étape B).
7. **Aucune analyse ajoutée**, aucun calcul neuf sur les scores, aucune phrase qui retienne « le meilleur des deux » ou qui touche au critère 3 de la porte G0. La table conjointe avec l'étape B est hors de ton mandat.

## Dépôt
`docs/verdicts/` sous un **nom neuf** (regarde les noms présents par `ls`, sans ouvrir aucun autre verdict), au format des verdicts que le texte prescrit ; scellé (`python -m controle_ia.scellement sceller`). Puis la ligne `VERDICT-BBIS` ajoutée au registre propre (format `| clé | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`, par la fonction du code si elle existe ; ligne ajoutée, jamais réécrite ; jamais `registres/scellements-v1.md`). Tu ne commites pas.

## Rendu à la conductrice
Chemin et empreinte du verdict ; la ligne de registre ajoutée ; « scellé » ou « non scellé : nœud » (sans dire lequel au-delà d'un titre sans mesure) ; la liste des fichiers de résultat ouverts. **Aucun chiffre, aucune issue, aucune phrase du verdict.**

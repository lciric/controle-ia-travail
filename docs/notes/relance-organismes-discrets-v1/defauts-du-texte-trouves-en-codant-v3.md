# Défauts du brouillon 11 trouvés en écrivant les versions 3 du code — relevé du développeur Claude Fable 5.2

Source : rapport du développeur des versions 3 (sept modules `*_v3.py` et `epreuves_couverture_bras_a_v2.py`, 217 essais passés). Code aligné sur le brouillon 11 (5bf56d57…) ; le développeur n'a pas lu les brouillons 12 et 13. Format du fichier des scores supposé (une ligne JSON par unité, champs moniteur, dose, cle, condition, tache, episode, pas, pli, etiquette, score ; dose écrite « dose-0.50 ») : à confronter au module habilité. Lecture partielle du brouillon 11, déclarée par le développeur. Choix provisoire du code entre parenthèses.

1. 7.2 (iii) contre (iv), étape (g) : une épreuve peut être trop propre et en échec sous A7 ; l'ordre du temps met A7 avant A11 de l'étape (g), alors que 6.3 (g) fait l'audit avant le scellement du verdict. (Code : A11 de l'épreuve refusé après A7 prononcé.)
2. 7.7, réserve R-BA2 : son texte n'est nulle part au brouillon. (Code : exigé de la configuration.)
3. 7.4, C4 : « aire, intervalle et les deux valeurs p » rapportés, mais 6.9 ne rend que la borne haute ; l'intervalle manque.
4. 6.9 : un moniteur dont seul l'intervalle est dégénéré est « indécis » tout en gardant sa p haute dans la famille. (Codé à la lettre.)
5. 6.9 : aucun compte de tirages dégénérés dans la liste des nombres rendus. (Code : deux champs nommés par le développeur.)
6. 6.9 et 8.4 : « après la ligne scellée de la table C » quand la table C n'est pas lue. (Code : un fichier scellé quel qu'il soit.)
7. 7.2 : « tirage dégénéré » d'un intervalle rapporté jamais défini. (Code : aucune tâche tirée n'a de valeur ; pour l'aire conditionnelle, une classe absente d'un pli.)
8. 6.4 point 2 : dénominateur de la part « champ final ouvert ». (Code : toutes les actions.)
9. Section 2 : la seconde condition de la forme de fin de CONTROLS découle de la première. (Sans effet.)
10. 3.2 : blancs dans la ligne d'ouverture d'un bloc de code. (Code strict : faute de forme.)
11. 7.6 : « établie aux trois doses » sous A15 ou A16. (Lu comme le mot défini, évalué.)
12. 6.2, lec6 : qui la tire (confirmé depuis par la mère : côté habilité, au brouillon 13). (Code : encore tirable par la relance, à fermer.)
13. 8.4 : la garde de l'unité de permutation ne peut pas être éprouvée côté analyse.
14. 8.4 : un lanceur qui oublierait la règle de la forme de fin retomberait en silence sur l'ancien traitement ; seuls le compte par motif et le seuil de dose reçue le montreraient.

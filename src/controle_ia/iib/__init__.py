"""Saboteur à budget, organisme (ii-b) : course exploratoire, non opposable (R-522 ; P-066 (b), R-2044).

Code neuf sous nom neuf (R12), écrit d'après `brouillons/ii-b-saboteur-budget-v1/conception-ii-b-v1-brouillon2.md`
(section 10). Aucun module de T0.6, T0.7, P3 ou P3-bis n'est modifié : ce qui est repris est importé.

Modules :
- `constantes_v1` : constantes de la règle, de l'oracle, des épreuves et des arrêts (conception 3.1, 3.4, 4) ;
- `consigne_v1` : consigne privée du maître (deux blocs cités, empreinte vérifiée) et motifs de mention ;
- `temoin_jumeau_v1` : occurrence du champ COST, coupe du préfixe, réécriture de toute la valeur du champ (décision M4) ;
- `oracle_v1` : jumeau honnête à contexte réécrit (estimation honnête cachée, excès par action) ;
- `regle_v1` : règle d'acceptation, fonction pure des seules sorties de l'oracle ;
- `tours_v1` : épreuves E-O1 à E-O6, arrêts M-1 à M-3, comptes par tour ;
- `exclusion_v1` : actions hors de la perte de distillation (mentions, non bornables à champ COST) ;
- `episodes_v1` : épisodes en lots, sans aucune capture d'activation ;
- `configuration_v1` : validation de la configuration (constantes égales à la conception, garde « aucune sonde ») ;
- `lanceur_v1` : run côté instance, phases A à E ;
- `jouet_v1` : générateur scénarisé et tâches synthétiques de la répétition jouet (processeur, sans modèle réel) ;
- `lecture_v1` : calculs des lectures (1) et (2), sur processeur, après le run ;
- `session_v1` : gardes de session (ligne de GO, étiquette `iib`, création de 7b d'abord).

Aucune activation n'est enregistrée, aucune sonde n'est apprise ni lue (conception 6.3).
"""

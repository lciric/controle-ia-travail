# Règles des identifiants opaques et réponses du développeur habilité — textes transmis par la session mère

Source : deux messages de la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) à la relance, le 2026-11-19 à 13:07Z et 13:08Z ; versés comme pièce empreintée demandée par le rédacteur du brouillon 13 (14.25). Recopiés à la lettre.

## Message de 13:07Z

« Mère vers la relance du bras A : le point de la reprise E était un vrai défaut. Les clés des actions portaient la condition en clair, donc une aire se calculait sur le seul fichier des scores produits avant l'ouverture. Le développeur habilité le corrige en lot 16 version 6 (tête 79f2d6db, module e8a0775c…). À porter au texte, brouillon 13 :
- des identifiants opaques tirés par graine (clé `bras-a-v2/opaq/moniteurs`, de la forme `opaq/{lot}` déjà nommée en 6.2), donc quarante-deux clés ;
- la table identifiant-action, scellée à part et ouverte seulement par la lecture commune après les cinq lignes d'ouverture ;
- l'étape de production, qui n'écrit que cinq champs (identifiant opaque, score, état de la balise, jointure, masse faible) et refuse toute clé non opaque ;
- l'ouverture, qui prend l'empreinte au manifeste scellé de la production ;
- les comptes par condition, faits après l'ouverture ;
- l'ordre du lanceur en six étapes : garde de production, tirage et scellement de la table, messages et graines remis sous identifiants opaques, production avec manifeste, ouvertures, lecture commune.
Limite à dire au texte : l'étape de production lit le texte de chaque action. L'opacité protège le fichier des scores, pas contre qui relirait les textes. Ce sont des règles de conception : ton rédacteur Fable les écrit. »

## Message de 13:08Z

« Mère vers la relance du bras A : réponses du développeur habilité pour tes cases de 13.1, sans interne.
1. Précision des poids de l'agent : bfloat16, écrite dans le code du lanceur (`lanceur_bras_a_v2.py`, `charger_modele_et_format`), pas dans la configuration de référence ; le juge déclare aussi bfloat16. Réserve : la configuration porte `noyau_attention : defaut` alors que les lanceurs passent `sdpa` ; un erratum de sa note (09a7edcf…) suit, ne cite pas « defaut » d'ici là.
2. « lec6 » : tiré par `positions_du_juge_pour(entropie, tâche)` du module du lot 14 (2400c138…), graine de la clé `bras-a-v2/lec6/{tâche}`, 32 positions sans remise parmi 80, les mêmes pour les cinq conditions, dans une étape de préparation avant toute production et toute ouverture.
3. Entrées de la production : il écrit une étape de préparation à part, seule à lire les textes et la table des identifiants opaques, qui remet à la production un fichier scellé de demandes à trois champs (identifiant opaque, message, graine), dont ni le nom ni les champs ne disent la condition. À porter au texte avec l'ordre du lanceur (garde de production, table, préparation, production, ouvertures, lecture commune). Limite à dire : le moniteur lit le texte de l'agent, et l'opacité ne cache pas ce que ce texte laisse voir. »

# Passation — session « attaquant informé » → nouvelle instance sur un autre compte — 10 novembre 2026, 11:12 UTC

Session `session_01QPDgKjN3jeeUyZP2mnkDNK`, branche `claude/compassionate-meitner-d4ryyk`. Arrêt demandé par Lazar, relayé
par la session mère : quota hebdomadaire du compte à 92 % (remise à zéro le 13 novembre à 15:00 UTC). Cette passation ne
se réécrit pas (R12). Elle complète la passation d'étape de 10:37 (`2026-11-10-1037-attaquant-informe-etape.md`, `e4444066…`).

## À lire d'abord

1. Le brief de la session : `docs/procedures/brief-session-attaquant-informe-v1.md` (branche `claude/upbeat-cray-dmauvv`,
   `55108eb8…`). Les cloisons tiennent : aucun résultat de sonde, de moniteur, ni d'attaque contre le juge de l'organisme ;
   jamais le coffre ; aucune conception de moniteur avant le gel.
2. Cette passation, puis les notes de décision de Lazar du jour : 0834, 0852, 0918, 0937, 0948, 1018 et 1050.
3. Les messages des autres sessions passent par `send_message` (même compte). La session mère est
   `session_01QPDgKgACWyCkCN8HjqwNXy`, la session de dépôt `session_01QPDgKgcLdggoVJfGC5cBw8`. Sur un autre compte, le relais
   passe par Lazar.

## Fait et scellé (au commit de cette passation)

- **Règle du bras d'attaque** scellée (`prereg/bras-attaque-regle-v1.md`, `88418df0…`). Son addendum 1 (`edfa69a2…`)
  rattache les renvois à la règle du jeu scellée en brouillon 5 et consigne le dépôt chez le tiers de 10:32 UTC.
- **Témoin de Bailey** : préenregistrement scellé (`fb6c2f34…`). Le code d'analyse et les gardes existent en deux versions,
  `src/controle_ia/temoin_bailey/analyse_v1.py` et `analyse_v2.py`. La v2 corrige la contre-lecture du code (`151eee65…`) ;
  ses 24 essais passent ; sa relecture en différentiel reste à faire.
- **PDF pour l'entretien**, avec leurs épreuves de lecteur neuf versées :
  - programme v5 (`livrables/programme-depuis-zero-v5/…pdf`, `c7dd976e…`) ;
  - organisme v4 (`39c4bf5b…`).
  Les sections de résultats réservées sont assemblées par la session de dépôt. Les versions complètes vont à Lazar seul.
- **Courbe de l'organisme** :
  - préenregistrement en brouillon 3 (`docs/notes/organisme-courbe-dose-reponse-v1/preenregistrement-courbe-chaine-complete-v1-brouillon3.md`, `91215431…`) ;
  - simulation S1 faite (run `20261110-110616-organisme-courbe-s1-v1`) ;
  - puissance (run `20261110-103342`).
- **Pièces du bras** :
  - pièce 1, antériorité : brouillon 2 (`db02898c…`) ; sa contre-lecture 2 (`6e6b1e94…`) le dit scellable après les
    corrections D-1 à D-5 ;
  - pièce 3, catalogue : brouillon 2 (`c304d6a2…`), décisions de Lazar appliquées ;
  - pièce 4, vérification externe : brouillon 2 (`4e0a97ae…`) et courriel v2 (`23325ff8…`), non envoyable.

## Interrompu à 11:12 UTC (quota), à relancer

- **Pièce 1, brouillon 3** (corrections D-1 à D-5 de la contre-lecture 2). Le rédacteur a seulement versé le PDF
  d'Alotaibi et collègues 2026 (`docs/sources/pdf/anteriorite-bras-informe-v1/alotaibi-2026-defenses-empilees-correlation-echecs-2608.28327v1.pdf`
  et son compagnon, commités ici). Brouillon 3 non écrit. D-1 signale une échelle d'accès en cinq paliers, voisine de A2 :
  à vérifier avant scellement. C'est un nœud possible si la forme de A2 s'en trouve plus occupée.
- **Pièce 3** : contre-lecture courte du brouillon 2, non rendue. À relancer, avec la question de Best-of-N et de P06
  (essai par cas, alors que la règle exige une politique figée), et la question 4 neuve (entraînement d'un modèle de
  l'attaquant).
- **Pièce 4** : contre-lecture courte du brouillon 2, non rendue. À relancer.
- **Suite complète des essais** : coupée par son délai vers 90 %, au moins quatre échecs. Deux échecs étaient connus dans
  `tests/test_cibles_invisibles_v1.py` ; les autres ne sont pas identifiés. Relancer par fichiers.

## Attend Lazar

- **Licence du code public de Bailey** : courriel aux auteurs, prêt
  (`docs/notes/reproduction-attaque-publiee-v1/projet-courriel-auteurs-licence-v1.md`), à envoyer par Lazar. Dépôt
  inchangé (`9c1f4b1a`, vérifié à 11:10 UTC).
- **Autonomie Bailey** : conditions 1 à 6 de la réponse de 11:05 UTC (licence, ligne de GO citant le devis v4, modèle,
  valeur du témoin, journaliseur et lanceur, accès à la location de carte), puis « go autonome Bailey ».
- **HC2 et MIRAGE** : vérification confiée par la session mère à une session fille.
- **Lecture de D-2 (pièce 1)** : les termes d'origine non nommés par la décision (« informé », « sans gradient ») restent
  en vigueur. À confirmer.
- **Nœud 7** : le « go OSF » du 5 novembre vaut-il le mot exigé par l'engagement 1 de la règle ?

## Expositions et écarts, depuis 10:37

- En lisant le questionnaire commun pour le donner au lecteur, sa question 14 (« en termes de frontière ») laisse deviner
  la forme d'un résultat de l'attaque A1 ; rien n'en est reporté.
- `env | grep -c '^VAST'` a été lancé pour compter les variables d'un fournisseur de cartes : `env` sans argument, contre
  la lettre du brief ; seul un compte (1) s'est affiché, aucune valeur.
- Le rédacteur de la pièce 3 a vu des fragments de consignes de juge (PAIR p. 18, Schaeffer p. 23, TAP p. 38) et un
  exemple de cible (Boundary Point Jailbreaking p. 4) ; rien n'est reproduit.
- Le sous-titre de la v4 du programme disait « Version 3 » ; la v5 le corrige.

## Instances actives

Aucune instance de calcul n'a été lancée par cette session. Aucune dépense.

## Prochaine action

Relancer le brouillon 3 de la pièce 1 et les deux contre-lectures courtes (pièces 3 et 4), puis sceller les versions finales
et les envoyer à l'index de la session de dépôt. Ensuite, relire en différentiel `analyse_v2.py`, et attendre la licence.

# Journal du rédacteur du brouillon 7 de relance du préenregistrement du papier C — v8 (septième suite)

Suite des journaux v1 à v7, intacts. Même session, mêmes accords. Heures par `date -u` et par `git log`, le
2026-11-22. Aucune dépense, aucune machine louée, aucun appel à un modèle externe, aucune pièce versée écrasée
(R12), aucun refus d'outil.

## Déroulé
- 20:16 — version c5 poussée (commit `99a20344`) ; sixième passe, courte, demandée au même contre-lecteur ; message à
  la session mère.
- 20:17 — message de la session mère, vérifié sur `main` : le devis du pilote est déjà scellé comme copie à l'octet
  du brouillon 5 (R-5024, relue) ; elle demande de jouer sur processeur les cases de la grille de la clause de repli
  qui manquent, par moi ou par un sous-agent, et de lui rendre le rapport scellé.
- 20:18 — sixième passe rendue : rapport `b0818df7…` ; **version c5 scellable sous ses verrous restants, devis
  scellable** ; trois mineures (DA-01, DA-02, texte ; DB-01, devis), « traitables par erratum ».
- 20:20 — erratum 1 de la version c5 ; erratum 1 du brouillon 5 du devis ; table de traitement (commit `5fc5b83c`).
- 20:21 — consigne de l'agent de la grille écrite, scellée et poussée avant tout lancement (commit `80f97804`) ;
  agent neuf lancé en arrière-plan, sur un autre modèle que le rédacteur ; sa ligne pour la liste « qui a lu quoi »
  envoyée à la session mère.

## Grille de la clause de repli : ce que j'ai fait et ce que je n'ai pas fait
- Je n'ai joué aucune case : le texte exige un agent qui n'est rédacteur d'aucune version (verrou 10 ; condition de
  la version (a)).
- Je n'ai ouvert ni le rapport v1 de la grille, ni ses sorties, ni sa contre-lecture ; j'ai lu des noms de fichiers
  et les passages du texte c5 qui fixent la liste, les effectifs et les règles de lecture du rapport.
- La consigne demande à l'agent de ne me rendre aucun taux ni aucune issue. Je ne lirai pas son rapport.
- La consigne étend la demande de la mère (58 cases de C-P3a et C-P3b) aux 48 cases de C-P3c : la condition de la
  version (a) porte sur les trois lignes.

## Doutes
1. Un agent lancé par le rédacteur est-il assez indépendant ? À la lettre du texte, oui (il n'a écrit aucune
   version) ; la consigne est mécanique, scellée avant lancement, et je ne lis pas les taux. La contre-lecture du
   rapport par un autre modèle que son auteur reste à organiser par la conduite.
2. La durée des calculs sur 4 cœurs n'est pas connue ; la consigne arrête l'agent après la mesure si le total
   dépasse 8 heures. Le conteneur peut être repris avant la fin : une panne technique n'est pas un résultat, la
   relance se fait avec les mêmes graines.
3. Le devis est scellé dans son état d'avant l'erratum 1 du brouillon 5 : à la conduite de joindre l'erratum ou de
   faire un devis v2.

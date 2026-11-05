# Rapport de la fille — troisième tir SPARKS-EXP7-NUL, code v11, jouet sur machine réelle (2026-11-05, 08:07 UTC)

Ordre de la mère (≈ 07:54 UTC) : tir sous GO-2026-11-05-05, selon la section 5 de `rapport-developpeur-addendum-1-v11.md`, code cabc06e5d7e1c62c519990ed9709103c23cb08ec.

## Verdict
Le script a rendu le verdict **« boucle »**. Je juge ce verdict **probablement artefactuel** : mon premier inventaire est tombé 11 s avant « ARRÊT OBTENU ». Comme le prescrit le texte imprimé, l'instance a été **détruite par son identifiant**, si bien que les étapes 4 à 7 (ordre « fin », relance, second journal, autodestruction) **n'ont pas été éprouvées**.

## Déroulé
- Offre 25240861 (rang 1) : carte 0,057389 USD/h, stockage 0,005479 USD/h. Devis : 0,0608 USD.
- Commit de tir 934e4824a36da00ffac85d0bb5df03ba8ef9140a, branche `essai/sparks-v11-tir-cabc06e5d7e1`. Addendum factice : df657d0a….
- Instance 59231131 créée ; T0 ≈ 07:54:28 UTC. Échéance de la minuterie : 08:24:07.
- Le conteneur n'a démarré qu'à 07:58:17, soit environ 4 min après la création.
- Journal lu à 07:58:36 : l'amorce n'en était qu'à l'installation des outils. Résumé du script : DEMARRAGES=1, ATTENDUS=1, BOUCLE=non.
- Inventaires :
  - 07:59:39 : running (cur_state running) ;
  - 08:02:41 : exited (cur_state **stopped**) ;
  - 08:05:43 : exited (cur_state **stopped**).
- Verdict du script (`boucle 59231131`) : « boucle ».
- Journal relu à 08:06:11 (avant la destruction) :
  - installation (ca-certificates, curl, git) : code 0 ;
  - minuterie lancée ;
  - « mode jouet : addendum non exigé » ;
  - fabrication factice de 60 s, « fin de la fabrication, code 0 » à 07:59:49 ;
  - **« ARRÊT OBTENU (état voulu « stopped », HTTP 200) : le conteneur sort » à 07:59:50** ;
  - résumé du script : DEMARRAGES=1, BOUCLE=non.
- `vastai destroy instance 59231131 -y` envoyé à 08:06:14. Inventaire à 08:06:20 : **absente**.

## Lecture
L'état « running » du premier inventaire correspond à la fabrication factice, encore en cours. Il n'y a eu ni relance ni second démarrage. Le script de verdict exige trois « exited » consécutifs à partir de T+5 min comptés depuis la création. Il ne tient pas compte du démarrage tardif du conteneur, environ 4 min ici.

**Correction proposée au développeur** : compter les trois inventaires à partir de la ligne « ARRÊT OBTENU » du journal, ou bien ne garder que les inventaires postérieurs à cette ligne.

## Dépense
Au plus environ 11,8 min (07:54:28 → 08:06:14) à 0,062868 USD/h, soit **au plus 0,0124 USD**. C'est moins en réalité, puisque l'instance était arrêtée à partir de 07:59:50 et que seul le stockage était alors facturé. Cumul des trois tirs : environ 0,033 USD sur l'enveloppe de 5 USD. Relevé de facturation Vast non lu.

## Réserves
- Aucune sortie brute de vastai n'est versée. Garde des secrets à 0. Les R8 n'ont pas été touchées.
- Le jeton GitHub expire à 10:00 UTC : un quatrième tir reste possible avant cette heure, sous réserve d'ordre.

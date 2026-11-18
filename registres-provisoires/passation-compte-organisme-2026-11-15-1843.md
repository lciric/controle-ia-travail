# Passation du compte organisme — 2026-11-15T18:43:44Z (heure lue par `date -u`)

Session du compte organisme (modèle A), brief `docs/notes/plan-paquet-multi-comptes-v1/brief-compte-organisme-v2.md` (`fc0229ad…`).
Demande de Lazar transmise par la session mère : passation, puis brief de reprise sur un autre compte. **Le pilote v12 n'est pas lancé
et ne se lance pas d'ici là.** Ce compte n'a créé aucune ressource, n'a fait aucun appel au loueur ni aux fournisseurs depuis la sonde
v74 (0,099132 USD, inscrite R-2769).

## Fait
- **Tâche 1 (pilote MR-2)** : sonde v74 jouée et versée ; texte scellé candidat 6 (`8aa33014…`, scellé par la mère, R-2809) ;
  procédure v1 à v10 (ssh), puis **v11** (sans ssh, `b3ce9014…`) et **v12** (sans ssh, `d0d2c8e1…`), pièces `sans-ssh-v1/` et
  `sans-ssh-v2/`, essais à blanc conformes ; épreuve des clés (programme v2) **faite par la session qui lance**, code 0, 0,001164 USD
  (R-2876, R-2877), ne se rejoue pas.
- **Vérification du différentiel v11 → v12** par la session mère (`main`, `docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/verification-differentiel-procedure-pilote-mr2-v74-machine-v12-v1.md`,
  `bcdfe1387632410bb96ad1c5debc567dce695e5fac606ba73fe3f657e1d3e153`, relue ici, égale à son compagnon) : « jouable après corrections »,
  aucune version nouvelle exigée ; **N1** (majeur, argent : `relire` accepte un prix relu jusqu'à 0,20 USD/h alors que l'échéance est à
  17 h ; consigne proposée : prix relu au-dessus de 0,17 USD/h → destruction aussitôt, nœud) ; **C1** (lecture de M5 et acteur de chaque
  geste après 22:39Z, consignés et dits à Lazar avant l'impression) ; **C2** (création jouée sous la seule forme de la section 2,
  point 7 ; crochet éprouvé sur cas sain et artefact) ; mineurs au rapport.
- **Tâche 3 (O4)** : lecture SSRN v2, citations 91/91, englobement v3 (`49d9bdc7…`) ; N-SSRN-1 et -2 accordés (R-2822).
- **Tâche 4** (page publique) : faite. **Tâche 2** (inventaire conception/code) : suspendue (nœud).

## Reste
- Pilote : consignes N1, C1, C2 et lecture de M5 par la mère (en attente) ; puis feu en autonomie avec préavis à Lazar, joué par la
  session qui lance, jamais par ce compte.
- Tâche 3 : pièces de priorité haute non lues (JEL Novy-Marx et Velikov ; code EvoSCM, BEYOND, WAHL).
- Tâche 2 : reprise au mot de la mère.

## Réserves
- Fichiers laissés hors des dépôts, à trancher par un humain : `/EMPREINTES-code-pilote-v74.txt`, `/home/user/arbre-organisme-co/a-sec/` ;
  dossier non suivi `docs/notes/organisme-multi-generations-v1/pilote-v1/c6` dans l'arbre de travail `/home/user/wt-prep-compte-organisme`
  (générateurs du candidat 6, jamais versés).
- Pièces hors dépôt portant des identifiants servis (R-2731) : `/home/user/hors-depot/essai-epreuve-v2-sorties/` ; la sortie de
  l'épreuve réelle est chez la session qui lance (`/home/user/pilote-mr2-v74-envoi/epreuve-cles.json`).
- Les essais à blanc laissent sous le bloc-notes de cette session des dépôts jetables (aucune valeur réelle) ; ils meurent avec le conteneur.

## Prochaine action
Pour une session neuve : suivre le brief de reprise
`docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/brief-reprise-compte-organisme-v1.md` ; attendre le mot de la mère sur N1, C1, C2 et M5.

## Instances actives
Aucune créée par ce compte. Intouchables (jamais nommées dans une commande) : 58936096, 58936099, 58936100, 60480302, 60599797, 60670453,
les serveurs `poste-temoin-bailey-*` (175884265, 175967712), et toute instance ou tout serveur que la session n'a pas créé.

## Repères
Branche `lot/compte-organisme-v1` : `85a84ff5daf3c6df4bc0e13c2444eeb51b8d05db` avant cette passation ; journal provisoire v28
(`a57cb4ad…`, PO-071, PO-072) ; `prep/pilote-mr2-compte-organisme-v1` : `5432ac56…` ; arbre de l'organisme `605e0f6` (sans dépôt
distant ; versé en paquet `e3d83e47…`).

# Contre-lecture du code du crible (iii), tour 2 (différentiel), v1

- **Lecteur** : sous-agent neuf, lecteur C ; il n'a écrit ni la pièce, ni le code v1 ou v2, ni les rapports. Écrit le 2026-11-17T03:32Z (`date -u`).
- **Pièces lues** : `rapport-crible-iii-v2.md` (`fde84c48c1f9891c692033754ed150eee3aed53c44693de53ed0bb2724f1be11`), `procedure-machine-crible-iii-v2.md`,
  les dix fichiers de code v2 et leurs v1, `contre-lecture-code-crible-iii-tour1-v1.md` (`c0c66dd5…`, empreinte vérifiée), les sorties gardées v2.
  `verifier-arbre docs/procedures/crible-iii-v1` : arbre intact. Les empreintes de toutes les pièces citées aux tableaux du rapport v2 et de
  la procédure v2 sont égales à celles des fichiers (contrôle programmé, aucun écart) ; `appliquer_corrections_crible_iii_tour1_v1.py` : `9d3d49f8…`, égale.
- **Interdits tenus** : aucune machine, aucun appel au loueur ni à un fournisseur de modèles, aucune clé, aucune dépense (relais factices seulement) ;
  issue du pilote non ouverte ; aucune branche `calcul/pilote-mr2-v74-entree-*` ouverte ; rien sous `diag/`, `runs/`, `donnees/` ; aucun fichier existant
  modifié, rien de committé, aucun git sur le dépôt principal autre que `git status` en lecture ; aucun identifiant de modèle ni valeur de clé relevés dans les pièces
  (seuls les noms de configuration `opus55`, `fable52`, `argon`, `astra`, déjà en v1) ; aucun texte « vastai » suivi de « create », « launch » ou « start » hors
  de l'outil de la session (imprimé, non joué, comme en v1).

## Verdict : **scellable** (aucune correction exigée ; trois remarques facultatives au § 4)

## 1. Chaque correction du tour 1 est appliquée fidèlement

Comparé par `diff` v1 contre v2, fichier par fichier :

- **Majeure 1** : les deux couples du rapport sont dans `crible_iii_v2.py` à la lettre (`try` autour du gardien avec `c.arreter("exception du gardien", …, 3)` ;
  `try` autour de `jouer_monde` avec « exception d'un monde » et monde « incomplet »). Complément déclaré (tous les fils d'appel lancés sont attendus avant
  le relevé : `fils_d_appel`, `t.ident is not None`) : correct, sans interblocage (`c.arreter` est appelé hors du verrou `c.verrou` aux deux endroits ; les fils jamais démarrés
  sont ignorés), et nécessaire pour que « chaque appel fait est listé ». Lecture de l'attendu « 100 appels listés » en « chaque appel fait est listé » : juste, l'arrêt
  arrête les files ; les essais comparent bien appels faits et appels listés.
- **Majeure 2** : couple du lanceur recopié à la lettre (deux branches `elif` : état différent de `complet`, puis aucune carte admise) ; couple de la procédure recopié
  (attendu du geste 0). Le lanceur n'est pas au banc de mutations ; deux artefacts (D en panne, B illisible) et le cas sain sont à l'essai à blanc, ce qui tient lieu de R5. Un cas tronqué
  garde sa règle propre (pas de double règle). Accepté.
- **Mineure 3** : les quatre couples sont recopiés à la lettre (`Commun.arreter`, appel, limite de débit, part). Essai et deux mutations (appel, `arreter`) ajoutés.
- **Mineure 4** : cas `essais_arbre_k1` du niveau B et mutation de niveau B (retrait de `- {eid_k1} - k1_tau`), tuée.
- **Mineure 5** : appliquée par la phrase, au choix de la mère comme le tour 1 le permettait ; la phrase dit juste ce que la garde est.
- **Mineure 6** : appliquée (rapport § 3 et § 7, procédure § 2 point 6 et § 5).
- **Remarques facultatives** : le rapport les traite honnêtement (analyseur plus large, second appel de Pr-4 non appliqué et renvoyé à Lazar par la mère).

## 2. Le différentiel ne contient rien d'autre

`diff` v1 contre v2 (tous les fichiers) :

- Noyau : exactement les six changements de code attendus (tête de docstring, `Commun.arreter`, `fils_d_appel` et ses deux `extend`, trois conditions « minimum remplaçable »,
  `try` du gardien, `try` du monde, la boucle de `join`) ; ni constante, ni gabarit, ni borne, ni file touchés.
- Lanceur : renommage (import du noyau v2, `VERSION`, liste à six fichiers, `prog`), docstring, les deux `elif` de la sonde. Rien d'autre.
- Amorce, programme machine, aide, outil de la session, répétition : seuls les noms v1 vers v2 des fichiers et la liste à six fichiers changent (outil de la session : la
  ligne de commande imprimée change de nom d'amorce aux deux endroits, rien d'autre). Aucun nom v1 périmé ne reste dans ces fichiers (les restes sont des noms voulus : mesure, lecture,
  relais, doublures, noyau v1 importé par la mesure, étiquettes et noms de sortie inchangés).
- Rapport v2 : en tête, § 1 (table), § 2, § 3 (jeux v2), § 4 (cinq points), § 6 (une réserve levée), § 7 neuf. Procédure v2 : en tête, § 1, § 2 points 2, 3 et 6, § 4 (noms, attendu du geste 0),
  § 5, § 6. Aucune prédiction, aucun devis, aucun taux de la pièce qui fait foi n'est touché.
- Mesure, lecture, relais factice, gardes de la session, doublures, devis : inchangés (empreintes égales à la v1).
- Cohérence du noyau v1 gardé : la mesure l'importe (constantes, `racine_graines`, `traits_employes`) et les gardes de la session lui prennent le lecteur des lignes de GO ; ces
  parties sont à l'octet près celles du noyau v2 (le `diff` ne les touche pas). Six fichiers à l'addendum : la liste est la même dans le lanceur, l'aide, le programme machine, la répétition et la procédure.

## 3. Rejeux (par moi)

Interpréteur `/usr/bin/python3` (3.13.18, numpy 2.5.3), arbre `605e0f6` dépaqueté du paquet `e3d83e47…` (vérifié) dans mon dossier jetable, mondes de développement `4036f512…` (vérifiés),
relevé de la sonde v74 (lecture seule), sous `nice`, conteneur chargé :

- **Niveau A** : 45 cas, 45 passés, 0 échec. Sortie égale à la sortie gardée à trois lignes près : les deux lignes d'ordre et de comptes qui dépendent du hasard des fils
  (« 2 erreurs sur 10 » contre « 3 erreurs sur 10 » ; « 21 appels faits, 21 listés » contre « 24 et 24 », l'égalité faits = listés étant l'attendu) ; la première ligne du diff vient de mon découpage de l'en-tête
  (le cas « filtre : moins de six » est bien joué).
- **Banc de mutations** : original niveau A et niveau B à 0 échec ; **41 mutations, 41 tuées pour la raison attendue, 0 défaut**, dont les cinq du tour 1 et celle du niveau B.
  Un premier essai de ma main avait passé `--arbre` sur la racine du paquet au lieu du dossier `orchestrator` : l'original de niveau B échouait (module `pole` introuvable) et
  la mutation de niveau B était déclarée survivante (« exception des essais ») ; c'est le bon sens du refus, et c'est mon erreur d'appel, corrigée au second passage.
- **Essai à blanc complet** (chaîne réelle du pilote, relais factices) : 28 cas, 28 conformes, 0 écart, 602 s. Ports 8811 et 8812 libres au départ.
- **Répétition de la machine** (dépôt jouet, doublures) : 14 cas, 14 conformes, 0 écart.
- **Lecture du code de la sonde** (pas rejouée seule hors de l'essai à blanc) : les deux règles neuves sont bien placées après le cas « tronqué » et avant la règle des cartes non évaluables.

## 4. Remarques facultatives (aucune ne conditionne le scellement)

1. Les couples de « limite de débit » et de « part atteinte » (mineure 3) ne sont pas mutés à part, comme le rapport le dit ; ils ont la forme exacte du couple de l'appel, qui l'est. Réserve déjà déclarée, acceptable.
2. Le contrôle de la part « avant l'appel » dans `appel_borne` (`if c.arret is None:`) n'est pas devenu « minimum remplaçable ». Il est inatteignable après la ligne du minimum (`c.arrete()` renvoie
   d'abord) sauf course d'un cheveu entre ce test et le verrou ; sans effet pratique, et hors de la lettre du tour 1.
3. Le rapport v2 reconduit la réserve du tour 1 : la concurrence réelle chez le fournisseur n'est pas éprouvée ; dite à Lazar au préavis (procédure § 2, point 6).

## 5. Pour la mère

1. **Nœud confirmé, inchangé** : au taux de tronquage de `fable52` vu au pilote, la ligne du minimum se déclenche presque sûrement (environ 10 mondes, environ 78 USD). C'est un risque à accepter ou une forme à changer par Lazar,
   avant toute ligne « calcul ». Le second appel de Pr-4 sous G2 à la sonde (au plus 3 USD de plus) reste à lui proposer.
2. La mère doit recommitter la version finale scellée de `appliquer_corrections_crible_iii_tour1_v1.py` (le rapport dit que des versions intermédiaires ont été committées) et la sortie du banc de mutations finale.
3. Pas de nouveau tour de code nécessaire pour le scellement de cette pièce ; restent, dans l'ordre : sonde des gabarits (ligne κiii0, règle neuve de la majeure 2 en vigueur), version 2 de la pièce (III-7), scellement, addendum à six fichiers, lignes de GO, feu, mot de Lazar.
4. Les jeux concurrents d'autres sessions sur les ports 8811 à 8814 se refusent entre eux : le conteneur doit être libre de ces ports pour un essai à blanc.
5. Disque du conteneur à 96 % (1,6 Go libres) pendant mes rejeux ; aucun jeu n'a échoué pour cette cause.

## 6. Incidents de ma main

- Premier appel du banc de mutations avec `--arbre` mal pointé (racine du paquet au lieu de `orchestrator`) : sorti en échec propre de niveau B, rejoué correctement. Un lancement en arrière-plan de ce premier essai n'a pas été arrêté (arrêt par motif refusé par la garde de R10) ; il s'est terminé de lui-même.
- Une première commande de clonage du paquet a échoué (paquet à historique tronqué) ; dépaqueté ensuite par un dépôt jetable à historique tronqué dans mon dossier de session. Premier lancement de l'essai à blanc avec un dossier de travail déjà créé (refus propre du programme) ; relancé avec un dossier neuf.
- Fichiers de travail seulement dans le dossier de session (`…/scratchpad/t2`), lectures seules ailleurs (paquet, mondes de développement, relevé de la sonde, copiés ou lus après contrôle d'empreinte). Aucun fichier à la racine `/`. Aucun commit.

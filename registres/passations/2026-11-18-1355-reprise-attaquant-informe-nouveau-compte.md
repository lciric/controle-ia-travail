# Note de reprise — attaquant informé, témoin de Bailey, nouveau compte (2026-11-18, 13:55Z)

Session `session_013QMaynSCWwud812phoDNwn`, sur le mot direct de Lazar (verbatim : « reprends le role de la session
attaquant informé »). Succède à `session_01XJ6MgnEhQMZteN9F8a1BST` (passation
`registres/passations/2026-11-18-1041-bailey-relance-en-cours-passation.md`). Branche de travail
`claude/festive-cannon-5ys0mz`, partie de `claude/compassionate-meitner-d4ryyk` à `c776c6e2` ; le poste Hetzner v14
continue de pousser ses journaux sur `claude/compassionate-meitner-d4ryyk`.

## Routine de reprise
- Empreintes de lancement : trois « OK ».
- `verifier-arbre` sur `main` (`fe86c917`) : 100 problèmes, tous des compagnons absents sous
  `runs/collisionneur-organismes-discrets-v1/…` (fichiers vivants de courses d'autres sessions) d'après la fin de la
  sortie ; non traités ici, ce n'est pas mon arbre.
- Tests : non relancés à ce stade (régime sobre, aucune modification de code).

## Relevé de 13:52Z (champs techniques, lecture seule)
- Crédit du loueur 37,76 USD, `billing_failed` faux.
- 61170458 (`temoin-bailey-c6-845f37c35eba4a3d`) : états réel et voulu « running », 1,2194 USD/h.
- Arrêtées, intouchables : 58936096, 58936099, 58936100, 60988826.
- Hetzner : 176575468 (poste v14) et 176187199 (sauvegarde), en marche.
- Conduite v16 : dernière ligne `principal-relance` lancée, sans ligne d'arrêt ; battement à 13:46Z ;
  `poste-fini-v14.json` absent.
- Besoin restant ≈ 1,32 USD/h × 14,6 h ≈ 19 USD : couvert par le crédit.

## Surveillance
Boucle shell dans le bloc-notes de la session (hors dépôt) : relevé toutes les 2 min du crédit, de l'état de 61170458
et de la marque de fin sur la branche distante ; sortie au seuil de 2,6 USD (repli B′ en filet, procédure
`procedure-repli-relance-bailey-v1.md`, § 2), à une recharge, à l'arrêt de l'instance, à la marque de fin, ou après
115 min ; réarmée à chaque sortie.

## Lectures pour la reprise (déclaration, orientation-sessions-v1, § 6)
Sur `main` : `CLAUDE.md` ; en-tête de `registres/etat.md` (lignes qui nomment le témoin) ; passation `2026-11-18-1041`
de la session sortante ; extraits de `registres/passations/2026-11-18-1045.md` et du complément « sommets » (lignes qui
nomment l'attaquant informé) ; `docs/procedures/orientation-sessions-v1.md` ; `docs/procedures/brief-session-attaquant-informe-v1.md` ;
lignes R-3195 à R-3250 de `registres/decisions.md` qui nomment Bailey ou l'attaquant informé ;
`registres/index-bras-attaque-v8.md` (sans contenu). Une recherche de noms de fichiers (`grep -l`) sur
« attaquant informé » a listé des chemins sans en ouvrir le contenu. Sur la branche : la passation de 10:41Z, la note
du repli B′ et la procédure du repli. Aucun coffre, aucun résultat, aucune note de sonde.

## Prochaine action
Contrôle de 14:00Z (crédit, recharges, état), puis laisser la relance finir vers 04:30Z le 19 ; ensuite les trois pas
de la passation de 10:41Z (destruction du poste v14 par identifiant, vérification de la destruction de 61170458,
lecture de clôture selon l'addendum 7, § 3).

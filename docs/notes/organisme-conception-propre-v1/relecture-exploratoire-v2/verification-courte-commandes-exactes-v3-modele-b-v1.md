Heure (`date -u`) : début 2026-11-14 23:36:59 UTC ; écriture 2026-11-14 23:39:16 UTC.

# Vérification courte de « commandes exactes v3 » (différentiel v2 → v3) — lecteur neuf (modèle B) — v1

Lecteur neuf, sous-agent ; n'a écrit ni la v2, ni la v3, ni l'outil, ni la vérification de la v2. Chemins relatifs à la
racine ; `DOS=docs/notes/organisme-conception-propre-v1`, `RE=$DOS/relecture-exploratoire-v2`,
`OUT=$RE/lecture-classement-v3-2`.

Pièces : `RE/commandes-exactes-v2.md`, `bd259d2c197414959cd03a119db0cbe25eedcd2238ff00aa2e3cd6fd83ffbc51` ;
`RE/commandes-exactes-v3.md`, `a94210703b608c2f1bd81bae0a6367473212328bb900bbadcc9dc67cbe82a1e9` ; couples exigés :
`RE/verification-courte-commandes-exactes-v2-modele-b-v1.md`, `90f3cc620de8fd0716f5b3288060dc31be2ca8da1e3bc0e7cf2b74d1c68f5246`.
Les trois empreintes recalculées, égales aux compagnons (`sha256sum -c` : trois `OK`). Outil
`OUT/outil_lecteur_conception_propre_v3_2_1.py` : compagnon `OK` ; fonctions `lire_journal`, `controler_coherence`,
`bilan`, `envoyer`, `lire_cle`, `charger_envois`, `racine_du_dossier`, `main` lues. La v3 est déjà commitée
(`05528f1c`) ; `git status --porcelain` sur `RE` vide avant ce rapport.

## Verdict

**Feu possible.** Les trois couples exigés sont portés exactement ; rien d'autre ne change le fond, la dépense ni
l'arrêt ; les deux points laissés tels quels sont sûrs pour l'argent. Aucune correction exigée. Six choses à dire à
l'opérateur (§ 4), dont aucune ne demande une pièce nouvelle.

## 1. Les trois couples

| Couple | Exigé | Dans la v3 | Jugement |
|---|---|---|---|
| 1 | dernière ligne de la table du point 7 : « tout autre code (1 : exception non prévue ; 130, 137, 143 : tâche tuée) ou pas de code », même conduite ; même phrase au point 6 | table du point 7 : texte exigé, au caractère près, conduite inchangée ; point 6, puce K4 : « tout code autre que 0 (1 … ; 130, 137, 143 …) ou pas de code : rien de plus, nœud » | porté exactement |
| 2 | sous le contrôle B, le cas où il ne rend pas sa ligne (première forme, texte), **ou** `default=None` dans la commande | première forme, texte exigé au caractère près, plus la précision « (la commande `bilan` du point 6) » ; commande du contrôle B identique à la v2 | porté ; suffisant (ci-dessous) |
| 3 | points 13 et 14 : « le `depense_comptee_usd` rendu par `bilan` (cumul du journal, appel en vol compris) ; les relevés sont cumulatifs, on ne les additionne pas » | points 13 et 14 ; au point 14, accords de « somme » refaits (« ce chiffre, il ») | porté exactement |

**Couple 2 sous forme de texte : suffisant.** Lu dans le code, non rejoué sur un dossier factice :
- premier appel tué en vol : journal avec un `envoi` sans `clos` → `clotures` vide → le contrôle B lève `ValueError`
  (`max()` d'une suite vide) ; `bilan` seul rend alors sa ligne, code 0, `en_vol` non vide → « dossier perdu, nœud » : la
  phrase le dit ;
- tué entre l'écriture d'une réponse et sa ligne de journal : `controler_coherence` lève `Refus` ; le contrôle B affiche
  une trace, `bilan` seul rend code 2 → « dossier perdu, nœud » : la phrase le dit ;
- cas que la phrase ne nomme pas (`bilan` seul rend sa ligne et `en_vol` est vide, par exemple refus pour clé absente au
  point 6 avant tout journal : aucune clôture, donc `ValueError` aussi) : il n'existe que si l'`envoyer` a rendu un code
  autre que 0 ou aucun code, donc le couple 1 l'a déjà mis en nœud. Tout chemin où le contrôle B ne rend pas sa ligne finit
  en nœud ; aucun ne permet un `envoyer` de plus.
Garder la commande inchangée est le choix le plus sûr : elle a été rejouée telle quelle par la vérification de la v2, la
variante à `default=None` ne l'a été par personne. Le texte n'affaiblit rien (`bilan` est gratuit, sans clé, sans écriture).

## 2. Rien d'autre ne change (comparaison par programme, hors réseau, 23:38 UTC)

Corps de la v2 (ligne 3 à la fin, 358 lignes) contre corps de la v3 (après l'en-tête de 131 lignes, 369 lignes) :
- **sept blocs changés, pas un de plus**, aux endroits de la table de l'en-tête : préalable 1, préalable 6, puce K4 du
  point 6, sous le contrôle B, dernière ligne de la table du point 7, point 13, point 14 ;
- seul bloc clos (point 5 bis) : identique ; passages entre accents graves : 226 dans la v2, 238 dans la v3,
  **aucun disparu**, douze ajoutés, tous des mots dans les sept blocs (`bilan` 5, `envoyer`, `ValueError`, `max()`,
  `Refus`, `en_vol`, `RE/commandes-exactes-v3.md`, `.sha256`) : **aucune commande ajoutée, retirée ni modifiée** ;
- lignes portant un mot de commande ou une option (`.venv/bin/python`, `sha256sum`, `git`, `find`, `unshare`, `--`…) :
  les seules différences sont dans les sept blocs ;
- nombres : aucun disparu ; ajoutés : 1, 130, 137, 143, le code 2, R-2822, 23:28 et le « 6 » de « point 6 » ; plafond 6,5,
  dépense antérieure 0, `--envois-max` 1 et 6, repli à 3, 7 200 s, 300 s, 0,33 : inchangés ;
- le différentiel imprimé dans l'en-tête est fidèle au différentiel recalculé (à la place d'une ligne vide près) ;
  l'en-tête ne porte aucune commande à jouer.
- Préalable 1 : `grep -n '^| R-2822 ' registres/decisions.md` → une ligne (2782), 23:28 UTC ; « il se recharge seul » et la
  phrase sur le relevé de facturation y sont, mot pour mot. Cet ajout lève un préalable sur le mot de Lazar : il ne change
  ni plafond ni garde. Préalable 6 : ajout d'ordre (commit avant le point 2), plus strict.

**Fond** : inchangé. **Dépense** : inchangée ; le couple 3 corrige un chiffre de registre (la somme des relevés aurait
compté environ le double), toujours du côté sûr. **Arrêt** : seulement resserré (couples 1 et 2 ajoutent des nœuds, n'en
ôtent aucun).

## 3. Points laissés tels quels

**Latitude « rejouer une fois une tranche refusée pour clé absente ».** Sûre pour l'argent et pour le dossier : dans
`envoyer`, `lire_cle` est appelée avant toute écriture au journal et avant tout envoi ; un refus là ne laisse ni ligne ni
fichier, et le rejeu repart du même journal. Bornes : (a) depuis le couple 1, elle ne vaut **qu'au point 7** — au point 6,
« tout code autre que 0 : rien de plus, nœud » couvre aussi ce code 2 ; (b) elle reste en tension avec le préalable 5
(« absente : nœud ») : une clé qui disparaît entre deux tranches, alors que la boucle de retrait ne joue que dans un
sous-shell, est un fait anormal de l'environnement.

**Point 1 qui vérifie le compagnon de la v2.** Sûr, mais il ne prouve rien sur la v3 : il rend `OK` (la v2 est gardée),
et la mention « (cette pièce) » y est fausse à la lettre, ce que l'en-tête déclare. Le point 2 (arbre propre) dit
seulement que la v3 du disque est celle du commit, non qu'elle est celle qui a été vérifiée.

## 4. À dire à l'opérateur

1. **Pièce à suivre** : `RE/commandes-exactes-v3.md`, empreinte `a9421070…` (entière ci-dessus). Au point 1, jouer en
   plus, sur mot de la mère (lecture seule, gratuite, hors réseau) : `( cd $RE && sha256sum -c commandes-exactes-v3.md.sha256 )`
   → `OK`, et comparer l'empreinte à celle de ce rapport. La ligne de la v2 se joue telle quelle et rend `OK`.
2. **Point 2** : `git status --porcelain` n'est vide que si la mère a commité aussi ce rapport et son compagnon (ceux de
   la v2 et la v3 le sont déjà). Sinon le point 2 arrête, comme il le doit.
3. **Clé absente** : au point 6, nœud, jamais de rejeu. Au point 7, un seul rejeu, et seulement si la variable revient
   par les outils de l'environnement, sans que la valeur passe par une commande, un fichier ou la conversation ; sinon, ou
   au second refus, ou pour le message « caractère hors de l'ASCII imprimable » (rien que l'opérateur puisse réparer sans
   toucher la valeur) : nœud. Recommandé : prévenir la mère dans tous les cas.
4. **Contrôle B sans ligne** : jouer `bilan` seul ; quel que soit son résultat, aucun `envoyer` de plus sans le mot de la
   mère (refus ou `en_vol` non vide : dossier perdu ; sinon : nœud par le code de l'`envoyer`).
5. **Chiffre de dépense (points 13 et 14)** : jouer `bilan` **avant** de déplacer un dossier arrêté (l'outil n'accepte
   que le dossier fixe : après déplacement, `bilan` refuse). Si `bilan` refuse (code 2), aucun chiffre n'est rendu : ne
   pas en fabriquer un, ne pas additionner les relevés ; nœud, la mère fixe le chiffre (au plus haut : dernier relevé plus
   le pire cas de l'appel sans clôture, environ 1,09 USD), et la console du fournisseur fait foi.
6. **Crédit** : R-2822 dit « le relevé de facturation reste à faire avant le premier appel si l'outil le permet » ;
   aucune commande de la pièce ne le fait et l'outil ne le permet pas. À dire tel quel dans le rapport (« non fait »), ou
   fait par la mère. Un crédit épuisé ne coûte rien de plus que le plafond (429 : anomalie, code 3), mais **il perd le
   dossier unique** : le rechargement automatique est un mot, non une mesure.

## Réserves

- Rien de rejoué au-delà de la comparaison de texte et de la lecture du code : ni essais, ni préparation, ni point 5 bis
  (rejoués par la vérification de la v2 sur des commandes restées identiques, ce que le § 2 établit).
- Les recommandations 4 à 6 de la vérification de la v2 restent ouvertes (4 et 5 non portées, 6 à moitié) : déclaré par
  l'en-tête de la v3, à trancher par la mère ; aucune ne touche l'argent.
- Détail : l'en-tête de la v3 se dit écrit « 23:33 à 23:38 UTC » alors que le fichier date de 23:36 ; sans effet.
- Jamais fait : `envoyer`, appel réseau, lecture ou affichage d'une clé, lecture d'un texte de fiche ou d'envoi,
  recherche récursive, `git fetch`, commit, push. Aucun refus de permission ni du classifieur. `$DOS/lecture-g1-v3-2`
  absent avant et après. Écrit dans le dépôt : ce rapport et son compagnon ; un script de comparaison dans le dossier
  temporaire de la session.

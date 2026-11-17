# Contre-lecture 3 du préenregistrement de la validation propre de l'allocation par blocs (brouillon 3) — v1

- **Lecteur** : sous-agent neuf, modèle C (R2) ; il n'a écrit ni les brouillons, ni les rapports des tours 1 et 2, ni les annexes. Début 2026-11-17 02:43Z (`date -u`) ; fin : heure du compagnon `.sha256` de ce rapport. Tour 3.
- **Pièce lue** : `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon3.md` (675 lignes ; compagnon conforme, empreinte non recopiée ici : celle du compagnon fait foi), différentiel du rédacteur et programme d'application (compagnons conformes), les deux comptes des annexes et leurs sorties (compagnons conformes), rapport du tour 2 (`ea84faa76b64379d93e58c242b09161bacfd2aeff0d5816c5a43ffcceb41319f`, recalculé).
- **Autres pièces lues** : verdict de l'idée 1.2 [V] (seulement les lignes de comptes et de moyennes citées) ; `differentiel` du rédacteur non relu ligne à ligne (la vérification porte sur le texte, par `diff`).
- **Jamais ouvert** : rien sous `diag/`, `runs/`, `donnees/` ; aucune branche `calcul/*` ou `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du pilote MR-2 ; aucun secret ; aucun affichage de variables d'environnement ; aucun appel réseau, aucune machine, aucune dépense ; aucun commit ; aucune pièce modifiée.

## Verdict

**« corrections »**. Les dix couples C1 à C10 du tour 2 sont tous appliqués, mot pour mot ; le différentiel brouillon 2 → brouillon 3 (par `diff`) ne contient que ces dix couples, les onze couples déclarés du rédacteur (annexes, renvois, retrait du serrage de l'étage 1, condition sur le flux de Q-1, titre, ligne « Brouillon 3 », statut, section « Contre-lecture ») et rien d'autre. Les deux annexes sont écrites et leurs chiffres sont **exacts** : j'ai rejoué les deux comptes (processeur seul, `nice`) et les deux sorties sont identiques à l'octet à celles versées. Mais l'annexe B affirme une borne qu'elle n'établit pas (« porteuse unique » au plus aussi couverte que « réplique »), dont dépend sa conclusion « les doses sont gardées, la règle ne joue pas », et elle déclare P1 « inchangée » sans tirer la conséquence du plafond. Une correction majeure (K1 à K3, un seul défaut), deux mineures (K4, K5). Le texte reste non scellable de toute façon tant que la mère n'a pas tranché Q-1, Q-2 et Q-3 (M3', non applicable à la rédaction, le texte le dit lui-même).

## 1. Corrections du tour 2 : fidèlement appliquées ?

| couple | état |
|---|---|
| C1, C2 (lecture (5) « sans pouvoir ») | mot pour mot (étage 1 et Seuil) |
| C3 (seuil de 12 heures) | mot pour mot |
| C4 (serrage : aucun prononcé de la table) | mot pour mot ; **plus** un couple du rédacteur, déclaré, qui retire la clause du serrage de l'étage 1 : justifié (sinon la table dirait « garantie mise en défaut » là où la liste d'arrêt dit « aucun prononcé »), cohérent avec le Seuil (« audit écrit et nœud de la mère ») |
| C5 (borne de Markov de P14) | mot pour mot |
| C6 (« dense » seulement) | mot pour mot |
| C7, C8 (colonnes de réfutation de P7, P8) | mot pour mot |
| C9 (crédits 0, hors crédits 0) | mot pour mot |
| C10 (renvoi à l'annexe A de [T]) | mot pour mot, dans la ligne des doses |
| M1' (annexe A) | écrite ; renvois d'accord (Métrique, banc de mutations de l'étape 0, origine de P13) ; la prédiction P13 est inchangée |
| M2' (annexe B) | écrite ; voir K1 à K3 |
| M3' (questions) | non applicable à la rédaction ; le texte l'annonce (« non appliqué », statut « non scellable »), une condition sur le flux est écrite d'avance si Q-1 est retenue (voir K5) |
| m9' | non appliquée, facultative : exact |

Le tableau « Réponse point par point » du brouillon 3 dit vrai sur chaque ligne ; le compte « onze couples du rédacteur » se retrouve (sept dans le corps : metrique-serrage, banc-de-mutations, origine-P13, doses-annexe-B-1 et -2, Q-1-flux, etage-1-serrage ; quatre pour titre, ligne, statut, section).

## 2. Vérifications refaites

- **Chiffres des annexes** : sorties rejouées (annexe A en trois minutes, annexe B en vingt secondes), identiques à l'octet. Empreintes citées retrouvées par `sha256sum` : synthetique_v1 (`febe203a…`), programme de [CL] (`01c648a0…`), banc B v1 (`46ef2b92…`), les deux comptes et leurs sorties ; tête de `main` (`6467b922…`) ; interpréteur et numpy (3.13.18, 2.4.6) conformes. Les empreintes des deux scripts publiés rejoués par l'annexe B ne sont pas recalculées par moi (le contrôle de quinze lignes passe dans le compte rejoué).
- **Annexe A** : lectures recalculées à la main : 1,96 × √(0,262 × 24) / 24 / √20 000 ≈ 0,00145 (borne de Doob), 0,0134 / 0,0007 ≈ 19 demi-largeurs (« environ vingt »), 1 − 0,975⁶ ≈ 14 % (fausse alerte), z des dix séries (moyenne −0,36, écart type 0,86) : cohérents. La mise en garde « une mutation sur les seuls arrêts de A n'est pas tuée (0,9999) » est vraie dans la sortie. Le texte nomme honnêtement la distance retenue après essai de trois distances (déclaré) et l'écart d'échantillonnage de F ; aucun signe visé (R3), symétrie tenue (R4).
- **Annexe B** : les 20 lignes recopiées et les comptes de lecture (4,9 à 6,0 nats aux doses basses neuves ; 12,8 à 15,8 aux hautes ; 2,2 à 3,2 et 8,6 à 10,4 pour l'idée 1.2 ; parts 0,29 à 0,49 et 0,76 à 0,94 ; « dose 1,0 : 13,5 à 14,2 ») sont exacts. Bornes de « réplique » : 310 / 750 = 0,4133 ; (4,13 − 5 × 0,09 + 5) / 10 ≈ 0,87 : exact sous l'hypothèse de croissance déclarée.
- **R1 à R4, fidélité, devis, lectures interdites, identifiants de modèle** : aucun identifiant de modèle (recherche faite) ; devis séparé crédits / hors crédits ; aucune règle de bras ni seuil de [T] touchés ; aucune lecture interdite apparente.

## 3. Défaut majeur (correction exigée)

**K1 à K3 — l'annexe B affirme que « porteuse unique » est au plus aussi couverte que « réplique », ce que ni le compte ni [V] n'établissent.** La porteuse unique est tirée **uniformément** parmi les quatre constructions ; la couverture attendue de la famille est donc la moyenne simple des couvertures des quatre constructions. « Réplique » porte les mêmes quatre constructions plus **deux doublons** : sa couverture est une moyenne où deux constructions pèsent double. Aucun ordre entre les deux moyennes ne se déduit (la construction la plus couverte peut tirer la famille « porteuse unique » au-dessus de « réplique »), et [V] ne donne pas de couverture par construction. La borne haute 0,87 ne vaut donc que pour « réplique ». La conclusion « la règle de 0,95 ne joue pas » est établie pour « réplique » seulement ; pour « porteuse unique », le risque d'être hors de la zone utile (côté haut aussi, ≥ 0,95) n'est ni écarté ni chiffré, et c'est l'étage 2 qui le couvre, du côté sûr. L'annexe dit déjà que la borne **basse** n'est pas établie ; la correction étend l'aveu à la borne haute et ajoute le côté haut de la zone utile. L'affirmation figure dans quatre endroits (couples K1, K2, K4 ci-dessous).

**Plafond de P1** (K3) : l'annexe dit que P1 et P2 « ne changent pas » parce que le gain ≥ +0,05 reste atteignable. C'est vrai du critère ; mais l'**estimation attendue** de P1 (+0,20 à +0,50) suppose une couverture de F au plus de 0,80 (pour +0,20) et au plus de 0,50 (pour +0,50), alors que le compte donne 0,41 à 0,87 : à 0,87, le gain est au plus de 0,13. P1 étant gelée avec un chiffre, la phrase « inchangées » doit être qualifiée : l'estimation n'est pas un critère (elle est rapportée), mais le texte ne doit pas laisser croire que le compte la confirme.

## 4. Mineure

**K5** — la condition sur le flux (Q-1) dit « mêmes arguments » : la taille diffère (25 contre 800) ; « mêmes arguments à la taille près » est exact.

## 5. Couples « ancien → nouveau » (chaque « ancien » figure une seule fois dans le brouillon 3 : vérifié par programme)

**K1**
- ancien : ```sa couverture attendue est au plus celle de « réplique », donc au plus d'environ 0,87. Sa borne basse n'est **pas** établie```
- nouveau : ```sa couverture attendue est la moyenne simple des couvertures des quatre constructions (porteuse tirée uniformément), alors que celle de « réplique » compte deux d'entre elles deux fois : ce compte n'établit aucun ordre entre les deux. Aucune borne, haute ou basse, n'est **établie** pour « porteuse unique »```

**K1-bis**
- ancien : ```si elle sortait à 0,05 ou moins, l'étage 2```
- nouveau : ```si elle sortait à 0,05 ou moins, ou à 0,95 ou plus, l'étage 2```

**K2**
- ancien : ```**ne joue pas** : les doses sont gardées.```
- nouveau : ```**ne joue pas pour « réplique »** (borne haute 0,87) ; pour « porteuse unique » ce compte ne la joue ni ne l'écarte : les doses sont gardées, le risque étant couvert par l'étage 2 (« hors de la zone utile », du côté sûr).```

**K3**
- ancien : ```1 − C_F, soit au moins 0,13)```
- nouveau : ```1 − C_F, soit de 0,13 à 0,59 sur la plage de « réplique » ; l'estimation attendue de P1 (+0,20 à +0,50) suppose une couverture de F d'au plus 0,80 (pour +0,20) et d'au plus 0,50 (pour +0,50), ce que ce compte n'établit pas : elle n'est pas un critère et son chiffre est gardé tel qu'écrit)```

**K4a** (doses, corps du texte)
- ancien : ```et celle de « porteuse unique » au plus celle de « réplique » : sous le seuil de 0,95 que la contre-lecture 2 fixait pour revoir les doses.```
- nouveau : ```« réplique » est sous le seuil de 0,95 que la contre-lecture 2 fixait pour revoir les doses ; celle de « porteuse unique » n'est pas bornée par ce compte (annexe B, point 3).```

**K4b** (tableau « Réponse point par point »)
- ancien : ```« porteuse unique » au plus autant ; la règle```
- nouveau : ```« porteuse unique » non bornée par ce compte ; la règle```

**K5**
- ancien : ```méthode, mêmes arguments, même ordre)```
- nouveau : ```méthode, mêmes arguments à la taille près, même ordre)```

Remarque : K2 garde les doses, ce qui est une décision de la rédaction (avant tout tirage, sans donnée du run). Si la mère veut les revoir pour « porteuse unique » faute de borne, c'est un changement de conception, non demandé ici.

## 6. Remarques facultatives (aucune correction exigée)

- Le texte garde, dans les sections historiques « Contre-lecture 1 », des lignes que le brouillon 3 rend périmées (par exemple la ligne M5 : « l'annexe A elle-même n'est pas écrite ») ; la section dit que « Ce qui reste avant le scellement » remplace l'ancienne. Acceptable pour une pièce de travail ; à nettoyer au texte qui fera foi.
- La série finale de 20 000 générations de l'annexe A contient les 4 000 premières qui avaient donné un F nettement sous 1 : le texte le dit (incident (c) de la déclaration). Bien.

## 7. Points pour la mère

- **Lettre du modèle du rédacteur du brouillon 3** : le texte déclare (ligne 435) qu'il est « du même modèle que le contre-lecteur 2 », c'est-à-dire du modèle C, qui est le mien ; la consigne de ce tour dit que les corrections viennent du modèle A. L'un des deux est faux. Si le rédacteur du brouillon 3 est bien du modèle C, **ce contre-lecteur n'est pas d'un autre modèle que lui** (exigence de R2 écrite dans le statut du texte) : le tour est alors à refaire par un lecteur A ou B, ou à signaler comme écart. À vérifier au registre des lettres ; si c'est A, corriger la ligne 435 par couple.
- **À trancher avant scellement** : Q-1, Q-2, Q-3 (inchangé) ; les lignes qui en dépendent ensuite par couples.
- Les annexes A et B sont maintenant lisibles et reproduites à l'octet ; la seule affirmation non fondée est celle de K1 à K4. Une fois K1 à K5 appliquées, un tour 4 limité aux couples K (et à la ligne 435) suffit.
- Pas de mot de Lazar nécessaire pour ce texte (processeur, 0 dollar, aucun écart à un texte scellé, rien d'adopté).

## 8. Déclaration

Rôle : contre-lecteur neuf (R2), modèle C. Heures (`date -u`) : début 02:43Z ; rejeu des comptes vers 02:46Z à 02:49Z ; rédaction ensuite ; scellement : heure du compagnon. **Incidents de ma main** : (a) les sorties des deux comptes ont été rejouées dans le bloc-notes de la session, avec `PYTHONDONTWRITEBYTECODE=1`, sans rien écrire dans le dépôt hors ce rapport ; (b) une copie du différentiel (`diff`) a été posée dans `/tmp/claude-0/` (hors dépôt, contraire à la consigne du bloc-notes de session) ; aucune ne contient de valeur interdite ; (c) la première lecture du dossier a eu lieu avant que le brouillon 3 existe sur disque (il a été écrit à 02:43:15Z), j'ai relu le dossier aussitôt ; (d) aucun fichier existant modifié, aucun commit, aucune machine, aucun appel réseau.

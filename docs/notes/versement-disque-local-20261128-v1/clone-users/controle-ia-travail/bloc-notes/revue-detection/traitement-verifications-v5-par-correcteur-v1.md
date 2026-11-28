# Traitement des vérifications de la synthèse v5 « comment détecter » (tour 4), par le correcteur v6 — v1

Session 16, 2026-10-21, de 00:05 à 00:25 UTC environ. Correcteur neuf : je n'ai écrit ni la revue (v1 à v5), ni ses
extractions, ni ses vérifications, ni leurs traitements. Consigne : `…/revue-detection/consigne-correcteur-v6-v1.md`
(`dc3db50a…`, compagnon égal). `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.

Pièces lues en entier, empreintes recalculées, égales à la consigne et à leur compagnon :
- v5 `…/revue-detection/synthese-comment-detecter-v5.md` (`17069e06f2f4d1a50f556c097a9278af3b2fc0d951b4d4cdd754998db3ab413d`) ;
- traitement du correcteur v5 `…/revue-detection/traitement-verification-v4-par-correcteur-v1.md` (`21e1d56c…`) ;
- fidélité `…/revue-detection/verification-v5-fidelite/verification-v5-fidelite-v1.md`
  (`054720926c0fe16140dd5aebbb508317eb1ddbc385ac9c02032225a3ae214881`), « conforme après corrections », 8 constats
  (2 mineurs, 6 de forme) ; fichiers de travail (`travail/`, 18 sceaux égaux) ;
- sens `…/revue-detection/verification-v5-sens/verification-v5-sens-v1.md`
  (`e3e4a650c9f2ce69b8f32743e609e8d80beb14acb547b1d35636e2b2b6db7036`), « conforme après corrections », 14 constats
  (1 majeur, 7 moyens, 5 mineurs, 1 de forme) ; fichiers de travail (liste d'empreintes du rapport égale).

Sortie : v6 `…/revue-detection/synthese-comment-detecter-v6.md`
(`124d06f821f5780dbc810d710d08a3d00239ae34e8545fe69c3ea683177511e8`, 694 lignes). Différentiel rejouable :
`…/revue-detection/correction-v6/outils/appliquer_corrections_v6.py` (v5 contrôlée par empreinte ; 54 remplacements,
chacun trouvé une seule fois, blancs normalisés ; textes des rapports pris par `extraire_corrections.py`, jamais
recopiés à la main ; sortie `correction-v6/sortie-appliquer-v6.txt`). « l. » ci-dessous = ligne de la v6
(`correction-v6/sortie-localiser-v6.txt`).

**Bilan.** 22 constats. **20 appliqués dans la v6** (fidélité 01 à 07 ; sens 01 à 13). **2 non appliqués dans la v6**,
car ils visent un autre fichier que la consigne ne m'ouvre pas en écriture : VV5-fidelite-08 (traitement de la v5) et
VV5-sens-14 (registre) ; leur correction est consignée ici, pour la session. Les rapports donnent 41 corrections écrites
(« remplacer … par … ») : 33 en mots exacts sans écart, 8 avec un écart déclaré ci-dessous (une fusion, un fait contraire
vérifié sur disque, un saut de paragraphe gardé, une mise à jour v6, quatre mentions d'attente ajoutées par la
consigne). Aucun chiffre neuf de la littérature hors des rapports ; aucun pouvoir changé ; aucune décision prise.

**PDF manquants : tous retrouvés.** Les dix PDF de `[N]` et `[X]` sont retéléchargés depuis arxiv.org seulement,
chacun dans son dossier `…/revue-detection/correction-v6/pdf/<identifiant et version>/`, compagnon `.sha256` à côté.
Empreinte complète égale, pour chacun, à celle de la v1 (`redaction/citations-synthese-v1.json`, `21868605…`) :

| clé | fichier | pages | sha256 | égal à la v1 |
|---|---|---|---|---|
| DYL | `2606.12618v2/2606.12618v2.pdf` | 32 | `2eccf7731173002170800eba9209126743c3369ca75a5c9d9ade345dd4087df6` | oui |
| LB | `2511.16035v2/2511.16035v2.pdf` | 112 | `cf3a615cb760e32d12840d70b770b861c2b2a71458fe90e6a43caa4109dbb90c` | oui |
| BU | `2407.12831v2/2407.12831v2.pdf` | 32 | `badf34f0ae9eddd6c159ac8b637d66af5b3a939f296a78cc32e9755584dd1506` | oui |
| AU | `2504.04072v3/2504.04072v3.pdf` | 24 | `0231c2baaad784d17b3bdea8e652b0b77a829a136ce8ef9751093287f410b193` | oui |
| K | `2511.17408v4/2511.17408v4.pdf` | 56 | `91e00c25f356db80a0073d32d7d774e71b64de13767983d85ec4bb0fcadb2357` | oui |
| CC | `2601.04603v1/2601.04603v1.pdf` | 17 | `ba8ec6570a41c42554ac89b9869020a2356cead5bdcf2618fc9c6208a89afdb5` | oui |
| RH | `2609.19101v2/2609.19101v2.pdf` | 39 | `c8ab50452ea3effc7865bb6b53f4c6159b150cafcd1864e3103f4da877f8ae3f` | oui |
| MA | `2503.10965v2/2503.10965v2.pdf` | 63 | `6cea87ef4a49ef861ce9c37a3aeef3d82dced5c70028a5b924211bb27773b60a` | oui |
| LIAR | `2309.15840v1/2309.15840v1.pdf` | 36 | `a710a785b6f1d59343877504167ea0a0ea74eac87e34f2a7d00e2e2517f67776` | oui |
| FQ | `2312.10029v2/2312.10029v2.pdf` | 38 | `8f8b5e7ad4391e822cacd768216ea475f74ef1540c8e0d09f42d8662b0e4c834` | oui |

Identifiants et versions pris dans la table des clés de la v5 (section 6) et dans `citations-synthese-v1.json`.

**Contrôles (consigne, point 6).** `…/revue-detection/correction-v6/outils/controles_v6.py`, outil `pagev6.py`, sortie
`correction-v6/sortie-controles-v6.txt` : chaque PDF lu après empreinte complète égale à son compagnon **et** à la
référence de la v1 (24 PDF : les 22 de la table, plus TM et SC de la v1) ; aucun extrait texte lu.
- A. Les 55 contrôles du correcteur v5 (`controles_v5.sh`, lu, jamais exécuté), dont 21 lus alors sur extraits texte :
  55 trouvés sur PDF ; ses 6 artefacts rejetés.
- B. Les 32 contrôles du vérificateur « fidélité » (listes de `verif_pages_v5.py`, lues par `ast`, jamais exécutées),
  dont les 11 sur DYL, LB, BU et AU : 32 trouvés ; ses 7 artefacts rejetés.
- C. Les 2 contrôles du vérificateur « sens » sur [DYL] p. 7 et p. 11 : trouvés sur PDF.
- D. Les 119 citations de la v1 (toutes clés) : 119 trouvées.
- E. Les 24 phrases neuves de la v6 qui citent une page (VV5-fidelite-01, VV5-sens-04, 06, 10, 11, 12) : 24 trouvées
  à la page citée ; 9 artefacts rejetés.
- F. Les 59 renvois de ligne neufs (document de P-015, brouillon de T0.6, P-011, [P], registres à `9ecd952`, réponse
  `f9aa1655…`, consigne du rédacteur de P3b, note de transmission, consigne de contre-lecture), fichier contrôlé par
  empreinte complète d'abord : 59 trouvés ; 4 artefacts (ligne voisine, chiffre changé, mot changé) rejetés.
- G. Garde d'empreinte (R5) : copie saine acceptée ; compagnon faux, octets ajoutés (compagnon recalculé, référence v1
  différente) et compagnon absent : arrêtés (code 3). Dossier d'épreuve supprimé après usage.
- Bilan : 291 trouvés, 0 absent ; 26 artefacts, tous rejetés.
- Vérification de la v6 (`outils/verifier_v6.py`, sortie `correction-v6/sortie-verifier-v6.txt`, 0 faute) : la v5 plus
  les 54 remplacements déclarés redonne la v6 (blancs normalisés) : rien d'autre n'a changé ; chaque texte neuf des
  rapports est présent (ou son écart déclaré) ; chaque ancien texte est absent ; mentions d'attente présentes ;
  « (b') » n'apparaît que comme proposition du vérificateur ; titres et lignes de table en même nombre, une puce de plus.

## Une ligne par constat

| constat | gravité | décision | ce qui a changé | passage de la v6 | écart aux mots exacts |
|---|---|---|---|---|---|
| VV5-fidelite-01 | mineur | appliqué | « analogues publiés » devient « analogues lus » ; exception de l'organisme affiné de [BX] (0,5, p. 8) dite | section 5, confiance, l. 431-433 | aucun |
| VV5-fidelite-02 | mineur | appliqué, fusionné avec VV5-sens-06 | « (sinon la sonde apprend le régime d'incitation, [KU p. 5]) » remis après l'incitation des deux côtés | table E3, « quoi », l. 393 | fusion : le texte de VV5-sens-06 contient la même correction ; « (comme T1) » de 02 y devient « , comme T1 ([P] l. 238-240 : …) » (mots de 06) ; les deux segments de 02 sont présents (contrôlé) |
| VV5-fidelite-03 | forme | appliqué | « deux jeux de paires » devient « deux jeux » | table E3, « quoi », l. 393 | aucun |
| VV5-fidelite-04 | forme | appliqué | R-293 décrit à part (chaîne et modules de P4 ; module v3 de l'addendum 2) | « Décisions », dernière puce, l. 627-628 | aucun |
| VV5-fidelite-05 | forme | appliqué | R-295 (1) : deux autres affirmations corrigées par R-299 (5) | « Décisions », puce R-295 (1), l. 602-603 | aucun (R-299 (5) relu à la ligne 499, `e8b73c64…`) |
| VV5-fidelite-06 | forme | appliqué | « document de P-015, `6e74c6cb…` » aux deux renvois | E2, « tranche », l. 394 ; E2, « contrôle », l. 397 | aucun. En plus : les textes neufs de VV5-sens-01, 02, 05, 06 et 13 citent « P-015 l. N » (mots exacts gardés) ; une convention est écrite aux Sources, l. 89-92 (« P-015 l. N » = document de P-015) |
| VV5-fidelite-07 | forme | appliqué, deux écarts | titre de la section 6 ; phrase des compagnons | l. 631 ; l. 635-637 ; complément l. 639-644 | (1) mots exacts, complétés de « ; v6 : les 22, ceux de `[N]` et `[X]` retéléchargés » : les PDF étant retrouvés, le titre dit l'état de la v6 (consigne, point 4). (2) non repris en mots exacts : le rapport dit le compagnon de MA absent ; sur disque (R11), `extraction/pdf-anthropic/2503.10965/2503.10965v2.pdf.sha256` existe (`6cea87ef…  2503.10965v2.pdf`, égal à la table) ; seul le PDF manquait. Texte écrit : « pour MA, présent (…, vérifié sur disque le 2026-10-21, R11), son PDF absent du bloc-notes restauré à la v5 » |
| VV5-fidelite-08 | forme | non appliqué dans un fichier | correction prévue pour une v2 du traitement de la v5, que la consigne ne m'ouvre pas en écriture. Consignée ici : colonne « écart » de VV4-sens-04 = « aucun (le constat demande une phrase ; elle est faite de ses mots) » ; le compte de 13 écarts du traitement v5 est juste | — | — |
| VV5-sens-01 | majeur | appliqué (trois remplacements), comme proposition du vérificateur, jamais décidée | version « sans condition qui réplique P3 » : condition redéfinie ; (b′) proposée par le vérificateur, confiance ≈ 55 %, repli (a) ; prédiction et statut de E2 sur les doses diffuses | recommandation (3), l. 412-419 ; nœud E2, l. 478-497 | mots exacts ; mention « **[Décision de Lazar en attente : P-015, et ajout d'une condition à T0.6 (nœud)]** » ajoutée (consigne, point 3) après le texte de (2) et après la phrase en gras de (3) ; le rapport écrit « (b') », gardé tel quel (la consigne l'écrit « (b′) ») |
| VV5-sens-02 | moyen | appliqué | condition « qui réplique P3 » définie par [P] (mode « coût gonflé ») ; aucun texte de T0.6 ne l'a ; T7-P1 ; confiance de 55 % rattachée à ce cas | recommandation (3), l. 406-411 ; E2, « tranche », l. 394 ; nœud E2, l. 476-477 | aucun |
| VV5-sens-03 | moyen | appliqué | rejeu de P-017 (C) distingué de E1 (v) ; divergence posée en options (A), (B), (C), (C′) ; « même lancement, passes en plus » | « Décisions », P-017, l. 578-591 ; nœud E2, l. 499-500 ; section 4, l. 372-373 | mention « **[Décision de Lazar en attente : P-017]** » insérée avant « Options : » (consigne, point 3) ; ailleurs aucun |
| VV5-sens-04 | moyen | appliqué | table 2.1 retypée : 0,03 de [BX] au troisième type ; [DYL] à consignes différentes, puis à consigne égale (p. 11, p. 7) | 2.1, ligne [BX], l. 195 ; ligne [DYL], l. 202 | aucun |
| VV5-sens-05 | moyen | appliqué | confiance de 15 à 25 % rattachée à une condition flagrante comme P3, T4 résiduel ; doses diffuses : question (R8), pas de chiffre | section 5, l. 429-431 et l. 437-441 | aucun |
| VV5-sens-06 | moyen | appliqué (avec VV5-fidelite-02) | jeu (2) de E3 : étiquette de T1 écrite ([P] l. 238-240), écart à P-011 et à P-015 déclaré, renvoi [KU p. 5] remis | table E3, « quoi », l. 393 | aucun |
| VV5-sens-07 | moyen | appliqué | T4 résiduel dans tout préenregistrement neuf ; dans T0.7 seulement si N-030 (B) ; recouvrement ; puce R-295 (1) | règles communes, l. 337-345 et l. 368-369 ; « Décisions », l. 606-608 | mention « **[Décision de Lazar en attente : N-030]** » ajoutée après « (nœud). » (consigne, point 3) |
| VV5-sens-08 | moyen | appliqué (huit remplacements) | ligne (vi) « double comptabilité » dans chaque case de E1 ; périmètre élargi en (iii) ; option (c) du nœud « Revendication » ; renvoi en 2.1 | E1, l. 393-397 ; nœud « Revendication », l. 460-461 ; 2.1, « Aussi », l. 212-216 | (8) : l'ancien texte enjambe un saut de paragraphe ; remplacé sans « **Ce qu'a fait Anthropic.** », mêmes mots, paragraphe gardé. Conséquence, hors constat : « la table E1 ne l'a pas » (« Décisions ») devenait faux ; devient « la table E1 l'a depuis la v6 (E1 (vi), VV5-sens-08) », l. 575-576 |
| VV5-sens-09 | mineur | appliqué | relance du rédacteur de P3b (R-306), note de transmission, deux écarts de la note | « Décisions », dépense de la nuit, l. 612-621 | aucun |
| VV5-sens-10 | mineur | appliqué | hypothèse d'Apollo pour la sonde Instructed-Pairs typée (contre le témoin), transposée à P3-P3 | rang 2, l. 302 | aucun |
| VV5-sens-11 | mineur | appliqué | contre-cas de [DYL] p. 11 : étiquette par le sujet de la question (p. 7) | section 1, point 1, l. 133-134 | aucun |
| VV5-sens-12 | mineur | appliqué | rang 4 : « Backdoors », la question bat le maximum ; E2 : chiffres de [DYL] table 9 rangés à consignes différentes | rang 4, l. 304 ; E2, « tranche », l. 394 | aucun |
| VV5-sens-13 | mineur | appliqué | portée de `reserve_B3_puissance_du_nul` sur toute relecture ; `reserve_B1_ampleur_au_dela_de_la_consigne` et dose réalisée | « Décisions », verdict complété, l. 564-567 | aucun |
| VV5-sens-14 | forme | non appliqué dans la v6 | vise la ligne du registre qui consignera la v5 (registre en lecture seule pour moi). Phrase à ajouter par la session, mots du rapport : « R-289 rangeait le rappel de 0,03 de [BX] parmi les analogues de P3-P3 ; la v5 le range à part, contre la conversation ordinaire (VV4-sens-02, VV5-sens-04). » | — | — |

## Ajouts de la v6 hors constats (consigne, points 3, 4 et 6), chacun déclaré

- Titre « synthèse v6 » (l. 1) ; puce « v6 » de l'en-tête (l. 41-58) ; Sources : lignes relues pour la v6 et convention
  « P-015 l. N » (l. 83-92) ; R7 : PDF retrouvés et contrôles refaits (l. 110-120) ; section 3 : lignes « v6 »
  (l. 295-296, l. 319-321) ; section 6 : `[C6]` et état des PDF (l. 631, l. 635-644) ; fichiers de la v6 (l. 686-694).
- Mentions d'attente (consigne, point 3), sur des phrases de la v5 qui supposent une décision non prise :
  « **[Décision de Lazar en attente : nœud « Revendication »]** » à la recommandation (2) (l. 402-403), à E1 « quoi »
  (« lus comme diagnostic de l'instrument, jamais comme détection », l. 393) et à E1 « tranche » (« jamais une
  détection », l. 394) ; « **[Décision de Lazar en attente : P-017]** » à la recommandation de la revue sur la
  manipulation du nombre (nœud E2, l. 502-504), avec renvoi à la divergence.
- Remarque (non comptée) de la vérification « fidélité » appliquée : rang 8, « à aucun chiffre publié » devient « à
  aucun chiffre des sources lues » (R8, l. 308).

## Remarques des rapports (non comptées) : suite donnée

- Fidélité, registre modifié pendant la vérification (`436fdfb6…`, non commité) : sans effet ; la v6 garde les renvois
  épinglés à `e8b73c64…` (lus par `git show 9ecd952`).
- Fidélité, R-306 et transmission à P3b : traité par VV5-sens-09.
- Fidélité, R8 au rang 8 : appliqué (ci-dessus).
- Fidélité, [N] et [X] sur extraits texte : levé (PDF retrouvés, contrôles refaits sur PDF).
- Fidélité, `registres/depenses.md` l. 88 cité sans version ; brouillon de T0.6 sans compagnon dans le dépôt : **non
  traités** (hors constats ; à la session).
- Sens, « Réponses aux cinq questions », point 5 : ce qu'il demande d'écrire dans la revue est fait (constats 01, 03,
  05, 07, 08) ; la note v2 de transmission à P3b reste à la session (ci-dessous).

## Écarts à la consigne, déclarés

- Une sortie d'essai du contrôle de la v6 a été écrite par erreur hors de `…/revue-detection/`, à la racine du
  bloc-notes de la session (`verif-essai.txt`), puis supprimée dans la minute ; son contenu est celui de
  `correction-v6/sortie-verifier-v6.txt` sur un essai de la v6, rien d'autre.
- Lectures hors de `…/revue-detection/`, par chemin, aux seules lignes citées par les constats : `…/brainstorm-outils-p3/`
  et `…/p3b/` (consignes et note ; brouillons de P3b et contre-lectures non ouverts) ; dans le dépôt, document de P-015,
  brouillon de T0.6, P-011, [P] (l. 123, 238-240, 249-253, 275-277, 330-331), registres par `git show 9ecd952` (lecture
  seule). Aucune valeur de T1, T2 ou T4 lue. Aucun fichier interdit ouvert ; aucune recherche récursive ; aucun
  sous-agent ; aucune dépense ; réseau : arxiv.org seulement.

## Points laissés à Lazar (jamais tranchés ici)

1. **P-015 et ajout d'une condition de référence flagrante à T0.6** (défaut de P-015 : (b), le 2026-10-22 vers 14:30 UTC ;
   l'ajout est un nœud) : la v6 porte la proposition (b′) du vérificateur VV5-sens-01, confiance ≈ 55 %, repli (a)
   (extension de N-028, diagnostic seulement) — **[Décision de Lazar en attente : P-015, et ajout d'une condition à T0.6
   (nœud)]**. Avec elle : la borne de 10 USD par lancement que l'étape 2 de (i) pourrait passer (lancement séparé, ou
   nœud).
2. **P-017** (défaut (A) le 2026-10-22 vers 21:15 UTC) : options (A), (B), (C), (C′) ; divergence entre la revue
   (manipulation de E1 (v), ≈ 50 %) et la session ((B), ≈ 55 %) ; à soumettre avant le scellement de P3b, sinon (A) vaut de
   fait — **[Décision de Lazar en attente : P-017]**.
3. **Nœud « Revendication et voie de R-262 (2) »** : options (a), (b), (c) ; recommandation (a), ≈ 65 % ; pas de défaut
   — **[Décision de Lazar en attente : nœud « Revendication »]**.
4. **N-030** (nœud) : T4 résiduel dans le test de validité de T0.7 seulement si (B) — **[Décision de Lazar en attente :
   N-030]**.
5. **Nœud E2 et extensions de N-028** (E2, bras « moyenne » (iii), manipulation du nombre sur les actions de P3) : pas de
   défaut.
6. **Règle gelée 1** : statut en production de la lecture après une question ; moyennes glissantes de [CC] et [GM].
7. **Données du concept 4 de P-011** (jeu (2) de E3 : actions générées par le modèle au lieu de paires synthétiques) :
   à te proposer avec recommandation (VV5-sens-06).
8. **Concepts, couches, positions** (proposer avec recommandation ; défaut (c) sous 48 heures, inchangé depuis la v5).
9. **Contact externe** FIBS et sondes de [CA] : disponibilité non vérifiée (inchangé).

## Pour la session (hors de mon périmètre d'écriture)

- VV5-fidelite-08 : v2 du traitement de la v5 (nom neuf, R12), colonne « écart » de VV4-sens-04.
- VV5-sens-14 : phrase sur R-289 dans la ligne du registre qui consignera la v5 (ou la v6).
- Note v2 de transmission à P3b (VV5-sens-09 ; rapport « sens », réponse 5) : VV4-sens-11 rendu juste (Bonferroni sur les
  deux sondes = reprise de [P] l. 275-277 ; extension aux bras = neuve) ; VV4-sens-04 conditionné à un GO qui ajoute la
  question ; pour la lecture (vi), T3 et P3-P4 au même jeton ; portée de `reserve_B3_puissance_du_nul` sur P3b.
- Texte de P-015 à reprendre (jeu de E3 décrit selon la v3, l. 138-141) avant le préenregistrement de T0.7.
- Avant tout versement de la revue au dépôt (R6) : les dix PDF de `correction-v6/pdf/` et leurs compagnons ;
  `registres/depenses.md` l. 88 à citer avec sa version ; compagnon du brouillon de T0.6.
- Vérification de la v6 : un contrôle de fidélité des remplacements v5 → v6 ; une vérification de sens si la session ou
  Lazar retient pour le nœud E2 autre chose que les deux versions écrites.

## Fichiers écrits (chacun avec son compagnon `.sha256`, format `sha256sum`, nom relatif)

- `…/revue-detection/synthese-comment-detecter-v6.md` ; `…/revue-detection/traitement-verifications-v5-par-correcteur-v1.md`.
- `…/revue-detection/correction-v6/` : `outils/` (`extraire_corrections.py`, `appliquer_corrections_v6.py`, `pagev6.py`,
  `controles_v6.py`, `verifier_v6.py`, `localiser_v6.py`) ; sorties `corrections-v5-extraites.json`,
  `sortie-appliquer-v6.txt`, `sortie-controles-v6.txt`, `sortie-verifier-v6.txt`, `sortie-localiser-v6.txt` ; `pdf/`
  (dix PDF, chacun dans son dossier). Scripts lancés par `python3 -I -B`, `PYTHONDONTWRITEBYTECODE=1` : aucun
  `__pycache__`.

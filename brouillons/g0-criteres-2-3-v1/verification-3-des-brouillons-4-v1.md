# Vérification 3, courte — écart entre les brouillons 3 et les brouillons 4 (préenregistrement de la dose–réponse de l'organisme à consigne cachée, texte de désignation de la course du critère 3, devis) — v1

## En-tête

- **Qui** : sous-agent de contre-lecture, le même que pour la contre-lecture 1, la vérification 1 et la vérification 2, d'un autre modèle que l'auteur, effort élevé. N'a écrit ni modifié aucune pièce ; ne conçoit ni moniteur ni sonde ; ne scelle rien.
- **Date** : 2026-11-24, vers 13:00 UTC.
- **Commit** : `2b991947`, branche `conception/g0-criteres-2-3-v1`.
- **Fichiers lus.** Empreintes vérifiées par leurs compagnons (tous « OK ») et recalculées :
  - `T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon4.md` : `ed0ee2a1e5e1e9cd23f04b2210819c3b8a6c2b82dc435a95bf946e457e07bfe1` ;
  - `G0-critere-3-designation-course-v1-brouillon4.md` : `052562050311d64f8390d61ade9b903dcaf760431930e808fe5b02dc1f4283e8` ;
  - `devis-dose-reponse-consigne-cachee-v1-brouillon4.md` : `40f1f751bc6957f2ba0884ae3db70f90c7cf609f094f39f38e81602884f6ea05` ;
  - les six fichiers de `pieces/construire-brouillons-4-v1/`.

  L'écart a été lu phrase par phrase, par programme, contre les brouillons 3. Pour la désignation, j'ai aussi relevé tout ce qui, hors de la section « Contre-lecture », nomme un lancement, la partie (ii), une clause ou l'organisme à adaptateur.
- **Sources ouvertes, avec permission :**
  - `docs/sources/pdf/2611.14950v1.pdf` (`6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6`) : p. 1, pour le titre et les auteurs ; p. 6 à 8, en texte extrait par `pdftotext`, sauts de page repérés ;
  - `prereg/P3-premier-test-i-a-v1.md`, l. 329-335 seulement.
- **Exposition** : aucune à un score, un verdict, une sortie de course ou une consigne privée d'un organisme déjà formé.
- **Rejoué :**
  - la reconstruction par `construire.py` dans une copie hors dépôt : les trois brouillons 4 et le journal (51 opérations) sont **identiques à l'octet** ;
  - le validateur, qui rend exactement les marqueurs attendus : `<<CONFIRMATION_DE_LAZAR>>` seul dans le préenregistrement ; `<<CONFIRMATION_DE_LAZAR>>`, `<<EMPREINTE_PREREG_DOSE_REPONSE_SCELLE>>` et `<<OPTION_RETENUE_PAR_LAZAR>>` dans la désignation.

  La simulation de puissance n'a pas été rejouée : elle n'a pas changé.

## Verdicts

| pièce | verdict |
|---|---|
| Préenregistrement (brouillon 4) | **prête à sceller sous les corrections mineures listées** (V3-01) |
| Texte de désignation (brouillon 4) | **prête à sceller sous les corrections mineures listées** (V3-01, V3-02) |
| Devis (brouillon 4) | **prête à sceller** |

Constats neufs : **0 bloquant, 0 majeur, 2 mineurs**.

## 1. États de V2-01 à V2-07

| constat | état | lieu |
|---|---|---|
| V2-01, lecteur du coût pendant la course | **corrigé** | préenregistrement, plan point 4 ; gardes de « Ce qui manque », point 3 |
| V2-02, portée du fait de littérature | **corrigé autrement — acceptable** (voir ci-dessous) | préenregistrement, choix 5 et en-tête ; désignation, raison 3 et note de retrait |
| V2-03, témoins du premier test déjà vus des instruments | **corrigé** | désignation, demande (7) |
| V2-04, limite des témoins | **corrigé autrement — acceptable**, et plus juste que ma proposition (voir ci-dessous) | préenregistrement, choix 5 ; désignation, R-K6 |
| V2-05 (a), (b), (c), voies restantes vers l'oracle | **corrigé** | liste d'arrêt ; C0 ; « Ce qui manque », point 3 |
| V2-06, marqueur de la vérification | **corrigé autrement — acceptable sous V3-01** : la vérification 2 est citée ; la vérification 3 est « citée au candidat », sans marqueur | sections « Contre-lecture » |
| V2-07, disque | **corrigé** : 300 Go partout (préenregistrement points 11 et « Devis » ; devis, « Carte » et ligne d'engagement) ; l'issue de la vérification de place est écrite | préenregistrement, plan point 6 ; devis |

**V2-02 — la citation est conforme au PDF.**
Le premier test fait sur le PDF (pages repérées par les sauts de page) :
- **Titre et auteurs** : « Stress-Testing Sandbagging Detection Under Adaptive Attack » ; Soopal, Agrawal, Karthikeyan et Lue Chee Lip (p. 1).
- **Page 6** (§ 4.3 et figure 3). Dans une même course d'entraînement, la sonde apprise contre un adaptateur bénin apparié sépare l'adaptateur saboteur de son jumeau (AUC 1,000). Sa règle de transfert passe « in 1 of 5 folds ». Avec les trois recettes bénignes, « 2 of 5 folds, still short of the 4 we required ». La légende de la figure 3 dit « at least 4 of 5 folds (rule fixed in advance) ».
- **Page 8** (discussion) : « fixes this within a training run but not across runs: … 1 of 5 folds, or 2 of 5 with three benign recipes ».
- **« Attaque active dans chaque condition où un détecteur est jugé »** :
  - page 7, fin du § 4.4 : « attack activity has to be verified in every condition a detector is scored in » ;
  - page 7, § 5 : « An attack must be active wherever a detector is scored » ;
  - page 8, conclusion : « … until the attack is shown to be active in the scored condition ».

  Le renvoi « p. 7-8 » est donc exact.

Une nuance, sans constat : le témoin apparié de l'article est un **adaptateur bénin**, c'est-à-dire un organisme témoin employé comme négatif d'apprentissage d'une sonde. La phrase du choix 5 (« porte sur l'apprentissage d'une sonde contre un témoin, non sur une course d'organismes ») reste juste. La note de retrait de la désignation, qui ne s'appuie plus sur l'article pour l'adaptateur témoin, l'est aussi.

**V2-04 — vérifié contre les l. 329-335 du texte scellé du premier test.** La « mention sans usage » y est « le même contenu trompeur que la consigne du saboteur, rapporté à un autre agent, avec un agent honnête ». Elle n'est donc pas un coût nommé sans gonflement, comme je l'avais écrit. Le « témoin instruit » y est une consigne bénigne, le titre en minuscules. La limite réécrite en trois sortes de témoins est exacte : demande bénigne ; coût nommé sans gonflement ; contenu d'une demande de gonflement présent sans être à appliquer. Il en va de même de la conséquence, aucun témoin ne porte une demande de gonflement adressée et déclenchée sans gonflement, et de la phrase de R-K6 qui la reprend.

## 2. Retrait du lancement 2 dans la désignation

Hors de la section « Contre-lecture » (historique voulu), aucune phrase ne suppose plus un second lancement. Ont été vérifiés :
- **Désignation de la course** : « le lancement » désigne partout l'unique course désignée, et sa définition est écrite en section 1.
- **Portée** : partie (i) seule ; la partie (ii) reste la première lecture. Les phrases correspondantes sont la note de retrait, R-K5 (désormais toujours écrite), et le point (5), où « parties (i) et (ii) » a été retiré.
- **Demande (7)** : la famille jugée est la consigne cachée seule.
- **R-K6** : la phrase sur l'adaptateur témoin est retirée.
- **Écart déclaré 1** : le filtre est levé pour cet organisme seulement.
- **Points 2 et 4 de Lazar** : la confirmation ne porte plus que sur les points 3 et 4, puisque le point 2 est tranché et que le point 1 a son marqueur.
- **Avis du contre-lecteur** : il est rapporté au passé, comme donné avant le retrait. Il pèse désormais pour « condition » : le cas « si ce lancement tombait » est réalisé.
- **Marqueurs** : `<<ECHEANCE_CLAUSE_LANCEMENT_2>>` a disparu.
- **Devis** : l'ordre de grandeur du lancement 2 est retiré, avec une phrase qui le dit.

Le nœud de la règle de lecture (options A et B) reste entier. Le « fait utile au choix », qui compare A et B, ne dépendait pas du lancement 2.

## 3. Constats neufs

**V3-01 — mineur — préenregistrement et désignation : la vérification 3 n'a pas de marqueur.**
C'est le même défaut que V2-06, une version plus loin : le validateur ne voit pas qu'elle manque, et un scellement sans elle passerait.
- Dans les deux textes. Ancien : « - **Vérification 3**, courte, du seul écart entre le brouillon 3 et ce brouillon 4, par le même contre-lecteur : demandée ; son rapport est cité au candidat. »
  → Nouveau : « - **Vérification 3**, courte, du seul écart entre le brouillon 3 et ce brouillon 4, par le même contre-lecteur : <<VERIFICATION_3>>. »

**V3-02 — mineur — désignation, en-tête « Documents qui font foi » : l'article cité à la raison 3 n'y est pas (R6).**
La raison 3 cite Soopal et al., p. 7-8, par renvoi au préenregistrement. La désignation est scellée à part et doit porter le chemin et l'empreinte de ce qu'elle cite.
- Ancien : « - le préenregistrement de la dose–réponse de l'organisme à consigne cachée, `brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon4.md` au jour de ce brouillon ; »
  → Nouveau : « - Soopal et al., « Stress-Testing Sandbagging Detection Under Adaptive Attack », arXiv 2611.14950 v1, `docs/sources/pdf/2611.14950v1.pdf` (`6396abd53a24b457519a4f5e5d669a74e1a91cce9a6e5b6b4175821ad3ab94d6`), p. 7-8 : une attaque doit être établie comme active dans chaque condition où un détecteur est jugé ;
  - le préenregistrement de la dose–réponse de l'organisme à consigne cachée, `brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-brouillon4.md` au jour de ce brouillon ; »

## 4. Régression

Aucune. Seuls ont changé l'en-tête, le choix 5, le plan (points 4, 6 et 11), C0, la liste d'arrêt, « Ce qui manque » et les sections « Contre-lecture ». Sont inchangés :
- dans le préenregistrement : la grille, la gradation ancrée sur l'intensité 1,25, la table C0 à C6 (hors l'ajout à C0), les seuils, la puissance et les chiffres du devis ;
- dans la désignation : les tables K, les trois qualificatifs et les lignes de registre exigées avant la création.

# Erratum proposé du nœud N4 (question des nœuds au collisionneur, v12) — annexe du bras méta v1

**Statut** : proposition, non servie ; **ne modifie pas la question** (`collisionneur-noeuds-31-octobre-v1/question-noeuds-decisionnels-collisionneur-v12.md`, pièce tenue par conv-audit et session-depot) ; **CA1-05 et CA1-04 restent posés au collisionneur et ne sont pas tranchés ici.** Lazar décide si et comment ce texte est servi (section 4). **Auteur** : rédacteur neuf Opus 5.5 du brouillon 4 de l'annexe (lignée conv-audit), 1er novembre 2026, qui n'a écrit ni la question, ni ses annexes, ni les brouillons 1 à 3 de l'annexe, ni leurs contre-lectures. Rien lu sous `donnees/` ; aucun réseau, aucun appel de modèle ; aucun commit, aucun `.sha256` écrit.
**Origine** : constat majeur CA3-01 de la contre-lecture du brouillon 3 de l'annexe (`contre-lecture-annexe-bras-meta-v1-brouillon3.md` `ca63088cc84531fe0be99aaf70f4a50d5278ff77ebfc633959b41697e2cbf397`).

## Pièces (empreintes recalculées, compagnons conformes)

- question des nœuds v12 `a7fac44bd25c0b88f90c3ce50c23fa3a704675e57c3639ea0e4e56c1797102d3` : N4, l. 44 (identique mot pour mot à celui de la v11 `4d322cf5…`) ; lien N11–N4, l. 97 ;
- annexe du tour 2 v5 `bdc78078148c43ae7dd89318e82dc75fbe8b331fba820f37919a87f1c1a9390a`, l. 8 : « N4 : (a), confiance 0,5 (conv-audit) ; CA1-04 : non tranché » ;
- relecture de la synthèse du tour 1 v12 `d1209130627f3e5c0ef7198016897c588a8b5ec3e36745084ec7b546475932b9`, l. 85 : N4 « tenu ; recalculs conformes » (la synthèse elle-même n'est pas lue ici) ;
- annexe du bras méta, brouillon 4 : `annexe-bras-meta-v1-brouillon4.md` `397e1cbc7483e7c5106bd859a77514605166e1fb699eb4b4ab5ed2730d15fb7c` (même dossier ; section 0.5 : correspondance) ; script `calcul-profil-bras-meta-v1-brouillon4.py` `48e3c57db884b0cb33e6a348a5f3805a3ccb36617694115faa83177d69abba40` ; sortie `calcul-profil-bras-meta-v1-brouillon4.sortie.txt` `9279d4ad2574fb094a017bcb2176682da758aca4043aa9c0785b7435ef009891` (trois rejeux identiques) : **tous les chiffres ci-dessous sont dans cette sortie** (§ 3 scénario principal, § 5 sensibilités, § 7 coûts, § 11 loi du brouillon 1, § 17 table d'écart et comptes de paires de canal), sauf ceux que N4 v12 cite et que ce texte ne fait que rappeler.

## 1. Ce que N4 v12 dit et qui n'est plus à jour

1. **Chiffres** : N4 cite ceux de la contre-lecture du brouillon 1 (zéro paire du profil 0,59–0,67 à six fiches, 0,25–0,36 à dix ; (b) 0,06 ; (c) 0,47 et 0,14 ; (d) 0,35 et 0,07), calculés sous une loi globale des niches. Le script de l'annexe les retrouve sous cette loi (à 0,01 près). Mais l'annexe écrit aussi une **loi par axe** (SUPPOSÉ), sous laquelle (a) est nettement plus défavorable (0,73 et 0,45) et l'ordre des options change ; N4 ne la mentionne pas. Le chiffre du script v9 (0,31 et 0,03, paramètres fictifs) est remplacé par le calcul sur les paramètres de l'annexe.
2. **Options absentes** : la bande [2 ; 4] (option (b1) de l'annexe, **sa recommandation**) et la réunion de la passe 1 et de la passe « tableau » (option (c2)).
3. **État de l'annexe** : N4 dit le brouillon 2 « en vérification de ses chiffres ; il n'est pas servi ». Le brouillon 3 a été vérifié et contre-lu (« soumettable à Lazar après corrections ») ; le brouillon 4 est écrit et attend sa contre-lecture.
4. **CA1-04** : N4 décrit l'état du brouillon 1 (« garde trois structures séquentielles imposées de la même façon »). Depuis le brouillon 2, une règle du lecteur exclut **toute** structure relevée au seul motif d'un élément que la question impose ; les options A, B, C sont chiffrées.
5. **Conséquence** : le tour 1 a été répondu sur ce texte ; l'annexe du tour 2 v5 ne porte, pour N4, que la recommandation de conv-audit.

## 2. Texte de remplacement de N4, prêt à servir

Les lettres (a) à (e) de la v12 sont gardées avec leur sens, pour que les réponses du tour 1 restent lisibles ; (f) et (g) sont ajoutées. Le texte reste sans recommandation, comme le reste de la question.

> **N4. Annexe des paramètres du bras méta** (texte corrigé : erratum du 1er novembre 2026). Grille de six niches, bande d'éloignement [2 ; 3], « canal faible » ≤ 1 : quatre paires de niches sur quinze dans le profil ; la niche « bornes et théorie » n'y a aucun partenaire. L'effectif réel de fiches du bras méta au pré-pilote est borné à dix (deux fiches par axe et par proposeur, axes 1 à 5). Probabilité qu'aucune paire de fiches ne soit dans le profil, à six puis dix fiches, sous deux lois a priori des niches, toutes deux SUPPOSÉ (accord des lecteurs 0,7, probabilité de structure partagée 0,3) : **loi globale** (celle des chiffres précédents) et **loi par axe** (la niche dépend de l'axe de la fiche ; écrite par l'auteur de l'annexe). L'annexe (brouillon 4, en attente de contre-lecture) est écrite pour être prête sous chaque option ; un seul de ses blocs change avec l'option. Options :
> - (a) accepter le repli comme mesure au pré-pilote : 0,60 et 0,25 (loi globale ; 0,60–0,69 et 0,25–0,39 sur trois lois globales) ; 0,73 et 0,45 (loi par axe) ;
> - (b) quinze fiches en passe 1 (changement de plan ; la question servie limite le proposeur à deux fiches par axe : il faut un second proposeur ou un texte changé ; ≈ +2,77 USD, l'étape É2 dépasse son relais) : 0,06 à quinze fiches, 0,15 à douze (loi globale) ; 0,21 et 0,34 (loi par axe) ;
> - (c) retirer la bande, [2 ; 5] (contraire à la décision du directeur, « éloignement non extrême ») : 0,47 et 0,14 (loi globale) ; 0,42 et 0,10 (loi par axe) ;
> - (d) canal ≤ 2 (« faible » couvre alors treize paires de niches sur quinze, contre sept à ≤ 1) : 0,35 et 0,07 (loi globale) ; 0,45 et 0,12 (loi par axe) ;
> - (e) modifier le profil de la décision du directeur (non chiffrée) ;
> - **(f) bande [2 ; 4]** (seul le cran maximal d'éloignement est exclu ; six paires sur quinze ; « bornes et théorie » retrouve deux partenaires ; aucun coût, aucun changement de plan) : 0,54 et 0,20 (loi globale) ; 0,51 et 0,16 (loi par axe) ;
> - **(g) réunir la passe 1 et la passe « tableau »** (jusqu'à vingt fiches ; la passe « tableau » est retirable et perdue avec 0,53 ; mêle des fiches écrites avec et sans tableau ; ≈ +1,50 USD de lectures d'étiquettes) : passes réunies 0,15 à douze fiches et 0,01 à vingt (loi globale), 0,34 et 0,09 (loi par axe) ; en comptant la perte de la passe « tableau », 0,39 et 0,14 (loi globale), 0,55 et 0,28 (loi par axe), passe 1 à six puis dix fiches.
> Les options (a), (c), (d), (f) gardent le plan ; (b) et (g) le changent (effectifs, devis). Sous la loi par axe, (a), (b) et (d) sont plus défavorables que sous la loi globale, (c) et (f) plus favorables. Et **CA1-04** : compter ou non les jeux de données comme « structure commune forte » (la décision du directeur les nomme ; presque toutes les fiches partagent les mêmes). Le lecteur ne relève jamais une structure au seul motif d'un élément que la question impose à toutes les fiches ; trois options : A objets mathématiques et méthodes comptés, jeux de données lus et non comptés (écart à la décision du directeur) ; B jeux de données comptés aussi (lettre de la décision) ; C A sans les trois structures séquentielles. Au moins une paire du profil à six fiches, sous (a) et la loi par axe : A 0,27 ; B 0,47 ; C 0,16 (probabilités de structure partagée 0,3, 0,85 et 0,15, SUPPOSÉ).

## 3. Ligne proposée pour l'annexe du tour 2 (N4)

> **N4** : (a), confiance 0,5 (conv-audit) ; **(f) bande [2 ; 4] avec la lecture de (a) (repli déclaré quand il joue), confiance 0,55, et CA1-04 : A, confiance 0,55 (auteur de l'annexe du bras méta, brouillons 3 et 4)** ; la recommandation (f) dépend de la loi par axe (SUPPOSÉ) : son gain sur (a), au moins une paire du profil, est de 0,22 à six fiches sous cette loi et de 0,06 sous la loi globale.

Chiffres de cette ligne : sortie v4, § 3 ((a) 0,27 et (b1) 0,49 à six fiches, loi par axe) et § 11 ((a) 0,40 et (b1) 0,46, loi globale) ; « (f) » est l'option (b1) de l'annexe.

## 4. Mode de service (à la décision de Lazar ; aucun défaut)

*Décision* : comment l'erratum atteint le collisionneur. *Enjeu* : le tour 1 a été répondu sur des options et des chiffres périmés ; le tour 2 attaque les recommandations, dont celle de l'annexe est absente ; tout nouvel appel au collisionneur est une dépense (nœud de Lazar).
- (i) **addendum servi avec le tour 2** : le texte de la section 2 et la ligne de la section 3, dans le même envoi que l'annexe du tour 2. Avantage : aucun appel de plus ; à 07:10 UTC le 1er novembre, le tour 2 n'était pas envoyé (R-1027 recommande d'attendre un erratum de la synthèse avant lui ; état à vérifier au moment du service). Inconvénient : les répondants n'ont pas eu d'avis propre sur (f) et (g) au tour 1.
- (ii) **v13 de la question, N4 seul reposé au tour 1**, puis tour 2. Avantage : avis propre sur (f) et (g) avant d'attaquer les recommandations. Inconvénient : un tour de plus, une dépense, un délai pour DEP10 et le gel du pré-pilote.
- (iii) **pas de nouveau service** : Lazar tranche N4 sur la synthèse existante et sur l'annexe. Inconvénient : l'avis du collisionneur porte sur un N4 périmé.
- *Recommandation* : (i), confiance 0,5 (si les répondants doivent avoir un avis propre sur (f), (ii)).

*Fin. Ce document propose ; il ne modifie aucune pièce et ne tranche rien.*

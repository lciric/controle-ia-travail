# Devis chiffré — banque d'épisodes de la famille aveugle de réserve du cycle 2 — v3

- **Classe A** (devis). **Rien n'est lancé, rien n'est dépensé, aucune ligne de calcul n'est ouverte par ce document.** Il chiffre l'esquisse de l'auteur de la famille, propose des plafonds et pose les décisions.
- **Version 3.** Elle remplace la version 2 (`devis-banque-d-episodes-famille-reserve-cycle-2-v2.md`, `c9d9c6a4140c6cab…`, même dossier, intacte) après la vérification de ses corrections par Opus 5.5 (`verification-corrections-devis-v1.md`, `a94ebada4a21157a…`) : corrections faites, une incohérence à corriger (point A), deux mises au point (B et C), une information à verser (D), et la réserve bloquante restée entière. La table « remarque → correction » est en section 0 bis.
- **Auteur** : Claude Fable 5.2 (conception), effort maximal, instance neuve qui reprend le devis, le 2026-11-21, de 18:48 à 19:33 en temps universel (`date -u`). Je n'ai écrit ni la famille, ni son esquisse, ni aucun moniteur. **À faire vérifier par le même contre-lecteur**, avant toute demande d'accord.
- **Ce qui est chiffré** : la pièce 6 de la famille, « esquisse de devis de la banque d'épisodes », **version 2**, celle avec laquelle la famille a été acceptée (`registres/decisions.md:4784`) : `docs/notes/scellement-2-famille-reserve-cycle-2-v1/piece-6-esquisse-de-devis-banque-d-episodes-v2.md`, branche `claude/scellement-2-famille-reserve-cycle-2-v1` (sommet `5d6b7a2a`), empreinte `62b99079fb7ca999d6ac325b9a78b47af46ea4a34296f3dfef6d9ef11892a912`, égale à son compagnon et à l'empreinte attendue, vérifiée avant lecture.
- **La réserve bloquante de la version 2 est levée** : cette pièce est lue en entier et comparée ligne à ligne à sa version 1 ; le devis la suit poste par poste (sections 2 et 2 bis). **Elle fait plus que doubler les lectures.**
- **Ce que je n'ai pas lu** : aucune autre pièce de la famille (pièces 1 à 5 et 7), ni la valeur de `k` ni celle de `k'`, ni aucun contenu de mode, ni la pièce de sécurité du banc fermé, ni le préenregistrement de sa course. Ce devis ne nomme, ne décrit ni ne suggère la famille.
- **Trois lettres** : **M** = relevé sur une pièce citée ; **C** = calculé ici ; **S** = supposé, sans mesure.
- **Recalcul** : tous les chiffres sortent du programme compagnon `calcul-devis-banque-d-episodes-famille-reserve-cycle-2-v3.py` et de sa sortie `…-v3-sortie.txt` (même dossier, scellés) ; les programmes et les sorties des versions 1 et 2 restent à côté. Les chiffres neufs ont été recalculés une seconde fois, à part, en fractions exactes, sans ce programme. Les montants sont en dollars des États-Unis.
- **Registres** : ils ont bougé pendant l'écriture. Ils sont lus jusqu'à `registres/go.md:679` et `registres/decisions.md:4829` ; plusieurs lignes inscrites après la vérification touchent cette banque et sont prises en compte (section 0, points 4, 7 et 8).

## 0. En une page

1. **Ce que la pièce 6 change en version 2.** Les relectures des épreuves passent de 60 à au moins 200 ensembles. Un poste neuf lit 240 ensembles pour des « oracles rapportés à côté », avec un second nombre tenu au coffre, `k'`. L'ancre n'est plus une personne : un agent la juge, en 30 questions. Par lecteur, 700 ensembles lus au lieu de 320.
2. **Attendu : environ 173 dollars** au centre (85 en version 2) : `k` = `k'` = 6, une question par appel, Claude Opus 5.5 à l'effort bas et Mistral Large 4. Fourchette : **29 à 229 dollars**.
3. **Plafond pessimiste : 817 dollars** pour `k` ≤ 8 et `k'` ≤ 8 (396 en version 2) : carte 37, essai de mesure 22, lectures 758. **Plus 49 dollars si Gemini 4 Neon juge l'ancre**, chiffrés selon la règle des appels aux modèles de Google : 866. Le plafond tombe à **226** (275 avec cette ancre) si l'auteur atteste que la lecture se fait en un appel par ensemble lu.
4. **Ces chiffres supposent Mistral Large 4 en second lecteur, et ce n'est plus acquis.** Le registre l'écarte des lecteurs du dommage de la course du banc fermé, tant qu'un modèle Mistral est juge du papier C et que ces épisodes servent au papier C (`registres/decisions.md:4807`). Si la même règle vaut pour cette banque, sa part (45 dollars attendus, 354 au plafond) est à remplacer. Par Gemini 4 Neon, ce serait de l'ordre de 600 dollars attendus à une question par appel et de 110 en lecture groupée, sur une sortie supposée, sans plafond possible avant mesure. Par un lecteur à poids ouverts sur machine fermée, repli que porte la pièce de sécurité (`registres/decisions.md:4815`), ce n'est pas chiffré.
5. **La carte pèse peu** (8 à 11 dollars attendus pour 260 épisodes, inchangé). **Les lectures font la dépense et l'incertitude** : `k` et `k'` sont au coffre, le second lecteur n'est pas arrêté, la sortie de Mistral n'est mesurée nulle part, son prix n'est pas sur une page scellée, et aucune ligne lue ne fixe l'effort du lecteur Claude.
6. **Règle de lancement des files, changée** (point A de la vérification). Après l'essai de mesure, une file part si une fois et demie son coût projeté tient dans son plafond pessimiste ; son plafond est alors le plus petit de deux fois ce coût et du plafond pessimiste. Le **plafond de dépense** couvre l'effort bas, l'effort moyen et, en moyenne, un effort haut à 2 000 jetons de sortie. La **règle de lancement** laisse partir le bas et le moyen pour tout `k` ≤ 8, le haut seulement si `k` ≤ 6,6. Au-delà, la file ne part pas : c'est un devis et un accord de plus (part de Claude portée de 424 à 678 dollars à `k` = 8).
7. **Mots de Lazar de GO-2026-11-21-75** (`registres/go.md:674`). (a) Compte Mistral : offre payante, crédit d'au moins 7,87 €. La part de cette banque vaut 45 dollars attendus et 354 au plafond, et le bras A puise au même compte : **la recharge par Lazar est certaine.** (b) Dommage du banc fermé confié aux lecteurs externes du monteur de l'oracle : **cela touche mon nœud 2** (sortie du coffre vers des tiers), **non mon point 3** (le monteur reste celui que la pièce 6 dit désigné). Depuis, Lazar a accordé la voie d'envoi (`registres/go.md:675-676`), et la pièce de sécurité du banc fermé la porte : version 15 à l'heure où j'écris, douze conditions au dernier compte du registre et une règle de lecture humaine chez le fournisseur (`registres/decisions.md:4813`, `:4822`, `:4829`). Mon nœud 2 se réduit à trois questions : cette voie vaut-elle pour la réserve ; chaque destinataire de cette banque passe-t-il les conditions ; la carte louée est-elle un banc fermé.
8. **Lignées.** Lignée du juge : Qwen. Exclues des lecteurs : Llama et Qwen. Claude n'est exclu par aucune règle lue. Mistral l'est pour la course du banc fermé (point 4). Restent à établir par la mère : quatre bases sans famille connue.
9. **Le repli chiffré de la version 2 (Gemini 4 Neon et Mistral Large 4, plafond 548) est retiré** : il n'est pas retenu. Un second lecteur de rechange n'a ici que des ordres de grandeur ; son prix se relèvera sur les mesures de la course du banc fermé, ou sur un essai.
10. **Rien n'est demandable avant la vérification de cette version** (`registres/decisions.md:4805`). Ensuite, sous les conditions de la section 9 : le lancement 1 sur carte (19 dollars), l'essai (22), puis chaque file sur son propre accord.
11. **À trancher** : les cinq points de la pièce 6 (section 6) et cinq nœuds pour Lazar (section 7).

## 0 bis. Table « remarque → correction »

Les lettres A à D sont celles de la vérification. « Où » renvoie aux sections de cette version.

| repère | remarque ou demande | correction faite | où | effet sur les chiffres |
|---|---|---|---|---|
| A (vérification) | La règle « deux fois la mesure » arrête l'effort moyen à `k` = 8 et l'effort haut dès `k` = 6, alors que quatre endroits les disent « couverts » | **Voie 2 retenue : la règle change.** Une file part si son coût projeté, majoré de moitié, tient dans son plafond pessimiste ; son plafond est le plus petit de deux fois ce coût et du plafond pessimiste. Les quatre endroits séparent désormais le plafond de dépense et la règle de lancement, et disent ce que la règle arrête encore : l'effort haut au-delà de `k` = 6,6. Le devis neuf qui suivrait est chiffré. La justification est en 4.2 | 0 (point 6), 3.3 (table par effort), 4.2 (règle), 5.2, 6 (point 1), 7 (nœud 5), 10, 11 (point 6) | aucun sur les totaux ; exemples de la règle refaits ; programme relancé |
| B (vérification) | Prix de Mistral au pire arrondi vers le bas : 0,058 et 0,061 | 0,059 et 0,062, arrondis au-dessus. Même défaut trouvé et corrigé pour l'attendu d'Opus 5.5 : 0,027 → 0,028. Les valeurs à cinq décimales sont données | 3.3, 6 (point 1) | aucun |
| C (vérification) | Le repli sur Neon et Mistral n'a ni compte ni gardes | **Repli retiré : il n'est pas retenu.** Le plafond de 548 disparaît. Raisons au point 2 de la section 6 : aucune règle lue n'écarte Claude ; c'est Mistral que le registre écarte maintenant ; la pièce de sécurité porte un autre repli. Un second lecteur de rechange n'a que des ordres de grandeur. **L'ancre, si Neon la juge, est chiffrée selon la règle des appels aux modèles de Google**, avec son compte (4.6) et sa garde (4.2, garde 8) | 3.2, 3.3, 4.2 (garde 8), 4.3, 4.6, 6 (point 2), 7 (nœud 1) | 548 retiré ; ancre par Neon : plafond 5 → **49** |
| D (vérification) | `registres/go.md:674` : compte Mistral, lecteurs du banc fermé ; `registres/decisions.md:4801` | Compte Mistral : euros, crédit d'au moins 7,87 €, recharge certaine. Lecteurs du banc fermé : nœud 2 touché, point 3 non. La ligne 4801 dit que la lecture de l'oracle a changé entre les versions : la pièce 6 le montre | 0 (point 7), 4.6, 6 (points 2 et 3), 7 (nœud 2) | aucun |
| réserve bloquante (remarque 11 de la contre-lecture ; mandat) | Rapprocher le devis de la pièce 6 en version 2, en disant ce qu'elle change | Pièce lue (`62b99079…a912`), comparée à sa version 1. Elle change cinq choses, listées en 2 bis. Le programme est relancé avec ses nombres | en-tête, 2, 2 bis, 4.2, 4.3, 4.4, 5, 6 | ensembles lus par lecteur 320 → **700** ; attendu 84,73 → **172,76** ; plafond 396 → **817** ; essai 13 → 22 |
| mandat | Mots de Lazar de GO-2026-11-21-75 ; dire si le second touche le nœud 2 ou le point 3 | Voir D. Le nœud 2 est récrit avec les lignes inscrites depuis (`registres/go.md:675-676` ; `registres/decisions.md:4807`, `:4813`, `:4815`, `:4818`, `:4822`, `:4824`, `:4829`) | 0 (point 7), 4.6, 7 (nœud 2) | aucun |
| mandat | Lignée du juge établie : Qwen ; exclusions : Llama et Qwen | Intégré au point 2 et à la condition 4, avec les réserves de la vérification des lignées et l'exclusion de Mistral inscrite depuis | 6 (point 2), 9 (condition 4), 11 (point 9) | aucun sur les chiffres ; la paire chiffrée devient conditionnelle |

**Les douze remarques de la contre-lecture** restent corrigées comme en version 2 ; la vérification les dit toutes tenues. Seule la onzième, la réserve bloquante, est reprise ici.

**Chiffres inchangés** : la carte (plafond 37 ; attendu 7,81 à 11,03 ; minuteries) ; le prix d'une question (0,0273 et 0,0736 pour Opus 5.5 ; 0,0105 et 0,0584 pour Mistral) ; le pire cas d'un envoi (0,2598 et 0,1127).

**Ajouts que ni la vérification ni le mandat ne demandaient**, à vérifier aussi :

1. L'essai mesure aussi la forme de question du poste D3, sur ses huit ensembles honnêtes (4.4). Sans cela, les files de ce poste partiraient sur un coût supposé.
2. La garde compte la file de Mistral au prix de repli tant que sa page de prix n'est pas scellée ; les exemples de la règle après mesure le suivent (4.2). La version 2 les donnait au prix relevé (25,23 et 15,14).
3. L'ancre par Neon est bornée par le corps de l'envoi, sans sortie moyenne supposée (4.3).
4. L'attestation demandée passe de trois à six cases (section 2).
5. Tout envoi de lecture, ensembles honnêtes compris, est tenu pour une sortie du coffre tant que le monteur ne dit pas le contraire (7, nœud 2). La phrase de la version 2 qui laissait passer la partie honnête de l'essai avant le lancement 1 est retirée.
6. Le poste D3 sur les épisodes honnêtes a sa propre paire de files, qui peut attendre l'étape 2 (5.2).
7. Les lignes de registre inscrites après la vérification : exclusion de Mistral, pièce de sécurité récrite jusqu'à sa version 15, lieu de l'envoi (0, points 4 et 7).
8. Une demande au monteur : ordonner au hasard, par tâche, les envois d'une file, pour qu'une file coupée laisse un sous-ensemble sans biais de condition (4.2).
9. Un doute neuf : le coût d'une file donne un ordre de grandeur de `k` (11, point 14).

## 1. Pièces lues, avec empreintes (sha256)

**Lues ou relues pour la version 3.**

| pièce | lieu | empreinte | usage |
|---|---|---|---|
| vérification des corrections du devis | `docs/notes/devis-famille-reserve-cycle-2-v1/verification-corrections-devis-v1.md` | `a94ebada4a21157a…` | points A à D |
| devis, version 2 ; son programme ; sa sortie | même dossier | `c9d9c6a4140c6cab…` ; `0dbe914c889cc928…` ; `1e5586d4a0d660d1…` | pièce corrigée ; le programme, relancé hors du dépôt, rend sa sortie scellée octet pour octet |
| contre-lecture du devis, version 1 | même dossier, `contre-lecture-devis-v1.md` | `69f069bea0cbee61…` | les douze remarques, relues |
| **pièce 6 de la famille de réserve, version 2** | branche `claude/scellement-2-famille-reserve-cycle-2-v1`, sommet `5d6b7a2a` | `62b99079fb7ca999…a912` | postes, volumes, cinq points ; lue en entier |
| pièce 6, version 1 | même branche | `981c85a1911d85e4…b79a0` | comparaison ligne à ligne |
| note des lignées à exclure des lecteurs | `docs/notes/scellement-2-lignees-lecteurs-v1/lignees-a-exclure-v1.md` | `596b5a73453b97ed…` | lignée du juge, liste d'exclusion |
| vérification de cette note | même dossier, `verification-lignees-a-exclure-v1.md` | `8718c80bee53da35…` | huit écarts, liste finale |
| décision sur la vérité du dommage des modes non chiffrés, version 3 (N-060) | `docs/decisions/decision-N-060-v3.md` | `2b448f696503112c…` | point 1 : deux lecteurs, deux familles hors des moniteurs |
| contre-lecture des trois choix du banc fermé, par un Fable neuf (classe C) | `docs/notes/banc-ferme-choix-contre-lecture-fable-v1/contre-lecture-trois-choix-banc-ferme-fable-v1.md` | `bc9ec0fdb7e4ad2b…` | lecture du mot de Lazar sur les lecteurs ; lignes 1 à 22 et 66 à 112 seulement |
| garde commune des appels aux modèles de Google, version 1 ; version 2, rendue pendant l'écriture | `src/controle_ia/garde_google_v1.py` ; `src/controle_ia/garde_google_v2.py` | `04d233bd66c3fdbf…` ; `9d39a7496d0a7b36…` | niveaux de réflexion, limite de sortie, 16 000 jetons de texte ; de la version 2, les seules lignes 61 à 75 : mêmes réglages pour Neon, 5,1 jetons par mot |
| consignes du dépôt | `CLAUDE.md`, « Appels aux modèles de Google », lignes 65-66 | `eb06c8fd3ffb84c1…` | la règle |
| page de prix de Google, versée le 21 novembre | `docs/sources/prix/page-prix-gemini-api-20261121T134918Z.html` | `40202cdd6fc4eb04…` | Gemini 4 Neon, onglet « Standard » : 3 et 15, sortie « including thinking tokens » |
| page du modèle Gemini 4 Neon | `docs/sources/prix/page-modele-gemini-4-neon-20261121T134943Z.html` | `2eadc19280409f03…` | sortie maximale 65 536 (ligne 53) ; réflexion à quatre niveaux |
| page de Google sur la réflexion | `docs/sources/google-gemini-reflexion-v1/gemini-thinking-generate-content-2026-11-21-v1.md.txt` | `fe0b8d8820b2ab7b…` | niveaux par modèle ; plafond d'un appel ; lignes 585 à 595, 748 à 752, 929 à 941 |
| registres vivants | `registres/go.md`, `registres/decisions.md`, `registres/depenses.md` | sans empreinte ; lus dans l'arbre de travail le 21 novembre, de 18:50 à 19:33 (sommet `43126a6da` au début, `de5e004f0` à la fin) | `registres/go.md:663-679` ; `registres/decisions.md:4776-4829` ; `registres/depenses.md:1-6` ; quelques lignes antérieures, listées au journal |

**Non relues : relevés des versions 1 et 2**, dont la contre-lecture a recalculé les empreintes et relu les prix, et dont la vérification a relu les lignes neuves.

| pièce | lieu | empreinte | usage |
|---|---|---|---|
| devis de la course sur carte louée du bras A des organismes discrets (déplacement des contrôles appris sans consigne), version 2 | `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md`, branche `claude/pensive-bardeen-1fv7hw` | `83240ca61d7c300f…` | débit, prix de la carte, méthode du pire cas |
| devis de l'essai de mesure des lecteurs du même bras A, brouillon 3 | `…/devis-essai-de-mesure-lecteurs-bras-a-v1-brouillon3.md`, même branche | `533ad5b15e6de1bd…` | tarifs, jetons par lecture, gardes nommées |
| page de prix d'Anthropic, versée et scellée | `docs/sources/prix-fournisseurs-2026-11-19/platform-claude-com-docs-en-about-claude-pricing-20261119T095216Z.html`, même branche | `78aff5c8d73a0da2…` | prix d'Opus 5.5 et de Sonnet 5.5 ; mode rapide, géographie d'inférence, cache |
| page de prix de Google, versée et scellée le 19 novembre | `…/aistudio-google-com-docs-pricing-20261119T095218Z.html`, même branche | `89c58281ba7e9e96…` | prix de Gemini 4 Neon, quatre onglets |
| programme du collisionneur (l'outil qui pose une même question à plusieurs modèles), version 9-3 | `docs/notes/collisionneur-v9/collisionneur_v9_v3.py` | `850df311807384fc…` | table de prix |
| relais Claude | `docs/notes/ideation-organisme-v1/orchestrateur-v52b/pole/relais_reel.py` | `1b90b020287e575b…` | barème et chemins refusés |
| recherche sur le lecteur remplaçant du bras A | `docs/notes/relance-organismes-discrets-v1/lecteur-remplacant-carbon-v1/choix-mistral-deepseek-v1.md` | `f7090b5d52b638b5…` | prix et réglages de Mistral Large 4 |
| esquisse en clair de la famille du premier cycle, version 3 | `docs/notes/scellement-2-familles-aveugles-v1/piece-6-esquisse-de-devis-banque-v3.md`, branche `claude/scellement-2-familles-aveugles-v1` | `bb89942b75fd6aa0…` | ordres de grandeur en jetons, forme d'une lecture |
| devis de la banque à deux modes | `docs/notes/devis-couche-2-banque-deux-modes-v1.md` | `cf2f4772dff30c07…` | coût fixe d'un lancement |
| devis des épisodes réels de la nuit du 1er novembre | `docs/notes/devis-episodes-reels-t05-nuit-v1/devis-episodes-reels-t05-nuit-v1.md` | `d6a34dbb9e1d35e0…` | réserve de tâches, sources de tâches neuves |
| décision sur les tâches fraîches (N-049) | `docs/decisions/decision-N-049-v1.md` | `8a5bf5e57e2bb447…` | point 4 |
| règle de sélection des papiers ; procédure d'extraction | `docs/procedures/T0.5-selection-papiers-v1.md` ; `docs/procedures/T0.5-extraction-v1.md` | `8f43dcaeb5fd782c…` ; `d23bd62fe1611b87…` | point 4 |
| environnement des propositions | `src/controle_ia/environnements/propositions.py` | `5d97b223206c6378…` | dix propositions au plus (ligne 26) |
| lignes de registre citées par les versions 1 et 2 | `registres/go.md` (avant la ligne 663), `registres/decisions.md` (avant la ligne 4776), `registres/depenses.md` | sans empreinte | prix relevés, décisions de Lazar |

Les lignes des registres vivants ne valent qu'à leur sommet ; ces registres ne s'allongent que par la fin. Toute ligne de registre a été lue derrière un filtre qui masque les motifs interdits par le mandat (journal, section 12). Dans la suite, `devis-bras-a-v2.md`, `devis-essai…` (le brouillon 3), `choix-mistral-deepseek-v1.md`, `relais_reel.py`, `collisionneur_v9_v3.py`, `piece-6-esquisse-de-devis-banque-v3.md`, `devis-episodes-reels-t05-nuit-v1.md` et `decision-N-049-v1.md` désignent les pièces de ces tableaux par leur nom de fichier. « Pièce 6 », sans autre mot, désigne désormais **la version 2** de l'esquisse de la famille de réserve. « Note des lignées » et « vérification des lignées » désignent les deux pièces du dossier `scellement-2-lignees-lecteurs-v1`. « Contre-lecture des trois choix » désigne la note du Fable neuf sur le banc fermé. Chaque citation se lit `fichier:ligne`.

## 2. Ce qui est chiffré : les postes de l'auteur

Notations de la pièce 6 : `n` tâches, `e` épisodes par tâche et par condition, `a` actions par épisode, `k` nombre moyen d'éléments de référence lus par tâche (au coffre), `k'` nombre moyen d'éléments des références des oracles rapportés à côté (au coffre), `n_f` tâches à dose flagrante, `p_anc` prix d'une lecture par l'agent de l'ancre. Je lis « ensemble » comme le jeu de propositions qu'un épisode rend, lu une fois par chaque lecteur. Tailles de principe de l'auteur : `n` = 60, `e` = 1, `n_f` = 20 (pièce 6, section 3).

| poste de la pièce 6 | épisodes | actions (`a` = 10) | ensembles lus par lecteur | questions par ensemble | étape | rôle |
|---|---|---|---|---|---|---|
| A. honnêtes, deux graines par tâche | 120 | 1 200 | 120 (poste D1) | `k` | 1 | 60 jumeaux (mesure), 60 pour le nul « honnête contre honnête » (contrôle) |
| B. « sabotage demandé », deux doses | 120 | 1 200 | 120 (poste D1) | `k` | 2 | mesure |
| C. dose flagrante, 20 tâches | 20 | 200 | 20 (poste D1) | `k` | 1 | contrôle : épreuve de l'oracle seulement |
| D2. relectures des épreuves de manipulation | — | — | **au moins 200** : 100 manipulés, autant d'intacts mêlés | `k` | 1 | contrôle |
| D3. oracles rapportés à côté, sur les épisodes A et B | — | — | **240** | `k'` | 1 pour A, 2 pour B | mesures rapportées à côté |
| D4. ancre des épreuves, jugée par un agent neuf | — | — | 30 questions, un seul agent | — | 1 | contrôle |
| D5. épreuves du programme de vérification | — | — | — | — | — | sur processeur, sans appel |
| **total** | **260** | **2 600** | **700** | | | questions par lecteur : 460 × `k` + 240 × `k'` |

- **`a` = 10 (S)** : c'est le réglage de la chaîne que le devis du bras A réemploie (`devis-bras-a-v2.md:38`) ; le code borne un ensemble à dix propositions (`src/controle_ia/environnements/propositions.py:26`). À confirmer par la mère sur la configuration scellée du banc.
- **`k` et `k'` sont inconnus de ce devis**, et ce sont des moyennes par tâche. Les tables vont de 3 à 8, avec `k'` pris égal à `k` faute de toute indication (S) ; le plafond est calculé à `k` = `k'` = 8.
- **Attestation à six cases, sans chiffre**, demandée à l'auteur de la famille ou au contre-lecteur du coffre : (1) `k` ≤ 8, oui ou non ; (2) `k'` ≤ 8, oui ou non ; (3) un appel par ensemble, ou un appel par question ; (4) le poste D2 tient-il en 200 ensembles, oui ou non ; (5) les épreuves ou les préconditions lisent-elles le poste D3 sur les épisodes honnêtes, oui ou non ; (6) la pièce 3 demande-t-elle des appels de préparation des références, oui ou non.
- **Part des contrôles (C)** : 80 épisodes sur 260 (31 %). Par lecteur, 280 ensembles lus sur 700 sont des contrôles (40 %), 240 vont aux oracles rapportés à côté (34 %) et 180 à la mesure principale (26 %).
- **Deux étapes, comme l'auteur les ordonne** (pièce 6, section 4). Étape 1 : postes A et C, puis les épreuves de l'oracle. Étape 2, seulement si les épreuves et les préconditions passent : poste B, « puis ses lectures ». Je range donc au plus naturel : à l'étape 1, le poste D1 sur A et C, le poste D2, l'ancre, et le poste D3 sur les épisodes honnêtes ; à l'étape 2, les postes D1 et D3 sur B. **La pièce ne dit pas où va le poste D3 sur les épisodes honnêtes** : il a ici sa propre paire de files, et il attend l'étape 2 si la case 5 de l'attestation répond non (5.2).
- **Variantes de taille** (pièce 6, section 3, dernière puce : 100 ou 200 épisodes par bras) : chiffrées en 5.3.

## 2 bis. Ce que la version 2 de la pièce 6 change

Comparaison ligne à ligne des deux versions (empreintes `981c85a1…b79a0` et `62b99079…a912`). La version 2 dit avoir traité deux points de la contre-lecture de la famille : l'ancre comptée en appels, et les relectures recomptées avec le monteur désigné.

| n° | version 1 | version 2 | effet sur ce devis |
|---|---|---|---|
| 1 | relectures des épreuves : « de l'ordre de 3 × 20 ensembles × `k` » | poste D2 : au moins 5 × 20 ensembles manipulés (trois épreuves à 20 ensembles, une épreuve à deux niveaux de 20), plus autant d'ensembles intacts mêlés, soit au moins 200 ensembles × `k` | 60 → 200 ensembles par lecteur ; attendu +31,76 ; plafond +151,16 |
| 2 | rien | poste D3 : lectures des oracles rapportés à côté, (4 × `n` × `e`) ensembles × `k'`, soit 240 × `k'` questions par lecteur ; `k'` au coffre | poste neuf ; attendu +54,45 ; plafond +259,13 ; un second nombre inconnu |
| 3 | « une ancre humaine sur 30 éléments (temps d'une personne, sans calcul) », hors de l'esquisse | poste D4 : ancre des épreuves « jugée par un agent neuf (GO-2026-11-21-66) », 30 questions, 30 × `p_anc` ; « l'ancre n'est plus du temps d'une personne » | le nœud du remplacement de l'ancre devient le choix du modèle de cet agent ; 0 à 49 dollars de plafond |
| 4 | point 2 : les deux familles des lecteurs | point 2 : en plus, le modèle de l'agent de l'ancre, « autre famille que les lecteurs si possible ; sinon, réserve d'indépendance au verdict » | section 6, point 2 ; section 7, nœud 1 |
| 5 | point 3 : la main qui monte les lecteurs, à désigner | point 3 : le monteur « est désigné : un agent Opus neuf », sur GO-2026-11-21-66 ; « reste à désigner la main distincte qui atteste qu'aucun moniteur ne lit la référence cachée » | section 6, point 3 |

- **Inchangés** : `n` = 60, `e` = 1, `n_f` = 20 ; 260 épisodes et 260 × `a` actions ; les formules des postes A, B et C ; le poste D1 (260 × `k`) ; l'ordre en deux étapes ; les points 4 et 5 ; la réserve sur les tâches fraîches ; la variante à 100 ou 200 épisodes ; le renvoi des moniteurs gelés au devis de la lecture du cycle. La carte ne bouge donc pas.
- **Le poste D5** (épreuves du programme de vérification, sur processeur) est écrit ; il ne coûte aucun appel.
- **Somme (C)** : par lecteur, 320 ensembles lus deviennent 700, soit 2,19 fois plus. À l'attendu au centre, 84,73 devient 172,76 dollars (+88,02 : relectures 31,76, oracles rapportés à côté 54,45, essai 1,81). Au plafond, 396 devient 817 (+421 : relectures 151,16, oracles rapportés à côté 259,13, essai 8,64, le reste aux arrondis par file).
- **Concordance** : le registre dit que les versions 2 des pièces de la famille changent notamment la « lecture de l'oracle » (`registres/decisions.md:4801`) : c'est ce que la pièce 6 montre aux postes D2, D3 et D4. Ce que les pièces 2 à 5 ont changé d'autre est au coffre ; rien, à ce que la pièce 6 laisse voir, n'y ajoute un poste payant.

## 3. Prix unitaires, avec leur source

### 3.1 Carte louée (prix `p_a`) — inchangé

| grandeur | valeur | lettre | source |
|---|---|---|---|
| carte A100 SXM4 80 Go, dernier prix relu | 1,1833 dollar par heure pour la carte seule ; offre à **1,1843**, stockage compris, le 2026-11-18T15:44:24Z | M | `registres/depenses.md:515` |
| prix du devis | 1,30 par heure pour la carte, stockage 0,08 au plus en sus, soit **1,38** ; téléchargement 0,05 dollar par Go au plus, 20 à 40 Go, soit 1 à 2 dollars par mise en route | M | `devis-bras-a-v2.md:67` et `:69` |
| durée d'un épisode de dix pas, par lots de huit | **42,8 s** retenus ; 40,2 s en bas de fourchette | M sur une autre chaîne, **S pour ce banc** | `devis-bras-a-v2.md:42-43` et `:54` |
| mise en route | 1,0 heure par lancement | S | `devis-bras-a-v2.md:56` |
| coût fixe d'un lancement, déjà observé | 2 à 3,5 dollars | M (par soustraction) | `docs/notes/devis-couche-2-banque-deux-modes-v1.md:37` |
| méthode du pire cas | débit deux fois plus lent et une relance complète, soit les heures × 4 ; 4 dollars de téléchargement | M | `devis-bras-a-v2.md:81` |

**Prix d'une action (C) : `p_a` = 0,00141 à 0,00164 dollar** (4,28 s à 1,1843 ou à 1,38 dollar par heure), soit 0,0015 à 0,0017 arrondi au-dessus, et 0,0141 à 0,0164 dollar par épisode, **plus un coût fixe de 2,18 à 3,38 dollars par lancement**. Les épisodes « sabotage demandé » sont supposés aussi longs que les honnêtes (S) ; le plafond porte ce doute.

### 3.2 Lecteurs et agent de l'ancre (prix `p_l1`, `p_l2`, `p_anc`), en dollars par million de jetons

| modèle | entrée | sortie | lettre | source |
|---|---|---|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) | 4 | 20 | M | page scellée d'Anthropic (`78aff5c8…`), tableau des modèles ; `relais_reel.py:50` ; `collisionneur_v9_v3.py:131` ; `devis-essai…:129` |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | 2 | 10 | M | même page ; `relais_reel.py:51` ; `devis-essai…:130` |
| Mistral Large 4 (`mistral-large-4-0`), point d'accès européen | 0,77 | 2,31 | **M sur une page non scellée** | 0,70 et 2,10, multipliés par 1,1 pour le point d'accès européen : `choix-mistral-deepseek-v1.md:19` (pages lues par un outil qui les résume, `:6`) |
| Mistral Large 4, **prix de repli**, celui que la garde compte | 1,54 | 4,62 | C | le double, tant que la page de prix de Mistral n'est pas versée et scellée (même règle que le prix de repli de Carbon, `devis-essai…:134` et `:137`) |
| Gemini 4 Neon (`gemini-4-neon`), pour l'ancre si le nœud 1 le retient | 3 | 15, réflexion comprise | M | page de Google du 19 novembre (`89c58281…`), relevé de la version 2 ; page versée le 21 novembre (`40202cdd…`), relue ici, section « Gemini 4 Neon », onglet « Standard » : « Input price … $3.00 », « Output price (including thinking tokens) … $15.00 » ; `registres/go.md:589` |

Pour mémoire, la table du collisionneur (`collisionneur_v9_v3.py:101-139`) compte Fable 5.2 à 10 et 50 (lu 8 et 40), Opus 5.5 à 4 et 20, Argon à 10 et 50, Kimi à 2 et 10, Astra à 10 et 50, Carbon à 4 et 20. Aucun de ces autres modèles n'est lecteur ici.

**Prix que ce devis ne compte pas, et que les gardes refusent** :

| ce qui renchérit | prix | source | garde (4.2) |
|---|---|---|---|
| mode rapide d'Anthropic, Claude Opus 5.5 | 8 et 40 : le double | page scellée d'Anthropic, « Fast mode pricing » | 4 : corps refusé avant l'envoi |
| géographie d'inférence « us » (`inference_geo`) | 1,1 fois tous les prix ; se cumule avec le mode rapide | même page, « Data residency pricing » | 4 : corps refusé avant l'envoi |
| écriture du cache d'Anthropic, durée de cinq minutes | 5 pour Opus 5.5, au lieu de 4 en entrée ; lecture du cache à 0,20 | même page, tableau des modèles ; `relais_reel.py:50` | 5 : cache non employé |
| Gemini 4 Neon, onglet « Priority » | 5,40 et 27 | page scellée de Google, section « Gemini 4 Neon » | 8, si Neon sert |
| Gemini 4 Neon, sortie au-delà de 65 536 jetons par appel (la page l'appelle « long decode », jusqu'à 1 048 576 jetons) | prix non relevé ici ; un envoi n'aurait plus de borne à 65 536 | page de Google sur la réflexion (`fe0b8d88…`), lignes 929 à 931 ; page du modèle, ligne 53 | 8 : plafond de sortie au-dessus de 65 536 refusé |

### 3.3 Jetons par lecture

| grandeur | valeur retenue | lettre | appui |
|---|---|---|---|
| entrée d'une lecture (consigne, plan de dix propositions, élément de référence) | 4 000 jetons ; 6 000 au plafond | S | « ordre de 4 000 jetons d'entrée » par plan (`piece-6-esquisse-de-devis-banque-v3.md:43`) ; 3 650 supposés au bras A (`devis-essai…:144`) |
| sortie d'un lecteur Claude, réflexion comprise | 500 jetons ; 2 000 au plafond | S | sur textes synthétiques, 120 lectures ont coûté 0,904303 dollar, dont 0,602 pour les 48 d'Opus 5.5 (`registres/depenses.md:546`), soit environ 300 jetons de sortie par lecture (C, sur entrées supposées) ; sorties de 49 à 234 et de 62 à 403 jetons pour deux autres modèles (`registres/depenses.md:541-542`) |
| effort du lecteur Claude | l'attendu est à l'effort bas, 500 jetons ; effort moyen, 1 000 ; effort haut, 2 000, qui est la sortie du plafond | S | bas et moyen : « à l'effort moyen le double » (`devis-essai…:144`) ; haut : sans source ; **aucune ligne lue ne fixe ce réglage** (section 7, nœud 5) |
| sortie de Mistral Large 4, raisonnement compris | 3 000 jetons ; 9 000 au plafond | S | raisonnement « high » par défaut, qui est aussi le maximum (`choix-mistral-deepseek-v1.md:17`) ; Lazar a demandé l'effort maximal pour ce lecteur au bras A (`registres/go.md:569`) ; la relance du bras A donne 80 à 330 dollars pour une course entière « selon le raisonnement, à mesurer » (`registres/decisions.md:4367`) |
| reprises et redemandes de forme | 5 % d'envois en plus ; 15 % au plafond | S | une seule reprise par envoi (`devis-essai…:253`) |
| garde par envoi | corps réel compté à un jeton par octet (environ 24 000 pour un plan long), sortie maximale 8 192 pour Claude, 16 384 pour Mistral (S) | M | `devis-essai…:145` et `:166` |
| **questions des postes D2 et D3** | comptées au prix d'une question du poste D1 | S | la pièce 6 leur donne la même formule de coût, (volume) × (`p_l1` + `p_l2`) ; aucune mesure ; l'essai mesure la forme du poste D3 (4.4) |
| **`k'`** | pris égal à `k` : 6 au centre, 8 au plafond | S | aucune indication ; case 2 de l'attestation |
| **lecture groupée**, variante : un appel par ensemble, les questions dedans | par question, 150 jetons d'entrée et 150 de sortie en plus du plan ; réflexion par appel, 300 jetons (Claude) et 3 000 (Mistral) ; au pire, entrée × 1,5, sortie × 4 (Claude) et × 3 (Mistral) | S | aucune mesure. À `k` = 8 : entrée 5 200 jetons attendus et 7 800 au pire ; sortie de Claude 1 500 et 6 000 ; sortie de Mistral 4 200 et 12 600. **Le plafond de 226 dollars en dépend** |
| **marge de lancement d'une file** (point A) | moitié du coût projeté | S | justifiée en 4.2 |
| **appel de Gemini 4 Neon au niveau de réflexion le plus haut** (point C) | sortie attendue, réflexion et texte : 8 000 jetons ; au pire, la borne du corps de l'envoi, 65 536 | S pour l'attendu ; M pour la borne | aucune mesure de Neon à ce niveau sur une lecture de ce type n'est au dépôt que j'aie lue. Seul relevé : un envoi d'essai à ce niveau, sur une autre invite, a rendu 2 131 jetons de pensée (`registres/decisions.md:4827`) ; l'attendu est donc plutôt large, sans que cela fasse une mesure. **Le plafond de 49 dollars de l'ancre ne dépend d'aucune sortie supposée.** L'attendu de 5,27 dollars et les ordres de grandeur du point 2 de la section 6 en dépendent |
| lectures d'admission de l'agent de l'ancre | 8, en plus des 30 questions | M (précédent) | `registres/go.md:632` |
| essai d'admission et de mesure | 12 ensembles par lecteur dans la forme du poste D1 (8 honnêtes, 4 de dose flagrante) ; les 8 honnêtes relus dans la forme du poste D3 | S | 4.4 |

**Prix d'une lecture, une question par appel (C)** :

| lecteur | attendu | pessimiste | à retenir, arrondi au-dessus (point B) |
|---|---|---|---|
| `p_l1`, Claude Opus 5.5 | 0,0273 | 0,0736 | 0,028 et 0,074 |
| variante, Claude Sonnet 5.5 | 0,0137 | 0,0368 | — |
| `p_l2`, Mistral Large 4 | 0,0105, facture attendue au prix relevé ; 0,0210 tel que la garde le compte, au prix de repli | 0,0292 au prix relevé ; **0,0584 au prix de repli** (0,0614 avec la marge de change) | 0,011 et 0,059 (0,062 avec la marge de change) |
| les deux lecteurs (Opus 5.5 et Mistral Large 4) | **0,0378** | **0,1320** compté ; **0,1350** avec la marge de change | — |
| `p_anc`, Gemini 4 Neon, s'il juge l'ancre | 0,1386 (S) | 1,0550, borne du corps (1,1078 avec la marge de change) | 0,139 et 1,056 (1,108) |

Valeurs à cinq décimales : 0,02730 et 0,07360 pour Opus 5.5 ; 0,01051, 0,05844 et 0,06137 pour Mistral.

**Lecteur Claude selon l'effort, une question par appel** (C sur des sorties supposées, S ; `k'` = `k`) :

| effort | sortie supposée | par question, attendu | part de Claude attendue, essai compris, à `k` = 6 | à `k` = 8 | tient-elle dans le plafond de dépense de la part de Claude (424) | la file part-elle, selon la règle de lancement de 4.2 |
|---|---|---|---|---|---|---|
| bas (celui de l'attendu) | 500 | 0,0273 | 117,94 | 157,25 | oui | oui, pour tout `k` ≤ 8 |
| moyen | 1 000 | 0,0378 | 163,30 | 217,73 | oui | oui, pour tout `k` ≤ 8 |
| haut | 2 000 | 0,0588 | 254,02 | 338,69 | oui ; le plafond vaut 1,25 fois cette part à `k` = 8 | **oui si `k` ≤ 6,6** (seuil calculé : 6,68) ; **non au-delà** |
| chaque réponse à la sortie maximale du corps | 8 192 | 0,1888 | 815,75 | 1 087,67 ; 1 244,25 aux entrées et reprises du pire cas | **non** | **non** |

Les deux dernières colonnes ne disent pas la même chose, et c'est le point A de la vérification. « Tient dans le plafond de dépense » : la somme accordée suffirait. « La file part » : la règle de lancement, qui demande une marge de moitié, la laisse partir. Un effort haut à `k` = 8 tiendrait dans le plafond de dépense, mais ne partirait pas : il coûterait un devis et un accord de plus, pour une part de Claude portée de 424 à 678 dollars (deux fois les 338,69 projetés).

## 4. Les lignes du devis

### 4.1 Génération des épisodes, sur carte louée — inchangé

| lancement | épisodes | durée attendue | attendu | pire cas | **plafond** | marge (plafond moins attendu haut) | minuterie d'arrêt dur |
|---|---|---|---|---|---|---|---|
| 1 : honnêtes (A) et dose flagrante (C) | 140 | 2,66 h | 4,04 à 5,68 | 18,71 | **19** | 13,3 | 10,6 h |
| 2 : « sabotage demandé » (B) | 120 | 2,43 h | 3,77 à 5,35 | 17,40 | **18** | 12,7 | 9,7 h ; 6,2 h au débit de 42,8 s |
| **total** | **260** | 5,09 h | **7,81 à 11,03** | 36,11 | **37** | 26,0 | |

- **Formules (C)** : heures = épisodes × 42,8 ÷ 3 600 + 1,0 ; attendu bas à 40,2 s et 1,1843 dollar par heure, plus 1 dollar ; attendu haut à 1,38, plus 2 dollars ; pire cas = heures × 4 × 1,38 + 4.
- **Minuterie d'arrêt dur** : elle vaut les heures que le plafond paie, soit (pire cas − 4) ÷ 1,38, tronquées au dixième, durée cumulée, relance comprise : 10,6 h et 9,7 h.
- **Lancement 2 recalculé** sur le débit `d` mesuré au lancement 1, en secondes par épisode, majoré de moitié pour les épisodes « sabotage demandé » : heures payées = `2 × (1,0 + 120 × 1,5 × d ÷ 3 600)` ; plafond = `1,38 × heures + 4`. La minuterie suit la même formule : pour `d` = 42,8, plafond 12,67 dollars et minuterie 6,2 h (6,28), au lieu de 9,7. Le plafond recalculé ne dépasse pas 18 : si `d` dépasse 81,4 secondes par épisode, la formule sort du plafond accordé, et **le lancement 2 ne part pas sans devis nouveau**.
- **Rapatrié et scellé avant toute destruction** : les épisodes (textes et identifiants générés), le manifeste (configuration et empreinte, versions, graines, commit, prix, durée), le débit mesuré. Sans les identifiants, une passe d'activations ultérieure est impossible (`devis-bras-a-v2.md:103`). Les épisodes B et C vont au coffre.
- **Compte de facturation** : le compte du loueur de cartes, en dollars (4.6).
- **Garde d'arrêt** : pas de création si le prix relevé dépasse 1,30 dollar par heure pour la carte, 0,08 pour le stockage ou 0,05 par Go ; accord cité par son identifiant (`GO_ID`) à la garde de calcul ; la minuterie ci-dessus ; alerte à 80 % du plafond ; arrêt par identifiant d'instance, consigné à `registres/arrets.md` ; aucune relance sans décision consignée.
- **Variante non retenue** : un seul lancement pour A, B et C (4,09 h, attendu 5,62 à 7,65, plafond 27). Elle épargne un coût fixe, mais fabrique le poste B avant que les épreuves aient passé, contre l'ordre de l'auteur.
- **Ce qui reste à dire avant toute création** : les épisodes C, puis B, dérivent du coffre. Qu'une carte louée soit un banc fermé au sens de la pièce de sécurité est la troisième question du nœud 2 (section 7).

### 4.2 Lecteurs du dommage, deux lecteurs

Volume par lecteur : 460 × `k` + 240 × `k'` questions (pièce 6, sections 2 et 3) : poste D1, 260 × `k` ; poste D2, 200 × `k` ; poste D3, 240 × `k'`. Le prix d'une question suppose que le plan entier est renvoyé à chaque appel : c'est la lecture la plus chère de la formule de l'auteur. Dans les tables, `k'` = `k`. S'ils diffèrent, chaque unité de `k'` ajoute 240 questions par lecteur, soit 9,07 dollars à l'attendu et 32,39 au plafond ; chaque unité de `k`, 460 questions, soit 17,39 et 62,08.

| `k` = `k'` | questions par lecteur | attendu, Opus 5.5 et Mistral | dont D1 ; D2 ; D3 | attendu, Sonnet 5.5 et Mistral | attendu, un appel par ensemble (Opus 5.5 et Mistral) | pessimiste compté (Opus 5.5 et Mistral au prix de repli) | pessimiste, marge de change comprise |
|---|---|---|---|---|---|---|---|
| 3 | 2 100 | 79,40 | 29,49 ; 22,69 ; 27,22 | 50,74 | 32,48 | 277,29 | 283,43 |
| 4 | 2 800 | 105,87 | 39,32 ; 30,25 ; 36,30 | 67,65 | 35,47 | 369,72 | 377,90 |
| 6 | 4 200 | **158,80** | 58,98 ; 45,37 ; 54,45 | 101,47 | 41,44 | 554,58 | 566,85 |
| 8 | 5 600 | 211,74 | 78,65 ; 60,50 ; 72,60 | 135,30 | 47,41 | 739,44 | **755,80** |

**Plafond pessimiste de chaque file.** Une file est un lecteur à une étape. À `k` = `k'` = 8 :

| file | questions | plafond compté par la garde | engagement, marge de change comprise |
|---|---|---|---|
| essai, Opus 5.5 | 160 | 11,78 | 11,78 |
| essai, Mistral Large 4 | 160 | 9,35 | 9,82 |
| étape 1 (poste D1 sur A et C, poste D2), Opus 5.5 | 2 720 | 200,19 | 200,19 |
| étape 1, Mistral Large 4 | 2 720 | 158,96 | 166,91 |
| poste D3 sur les épisodes honnêtes, Opus 5.5 | 960 | 70,66 | 70,66 |
| poste D3 sur les épisodes honnêtes, Mistral Large 4 | 960 | 56,11 | 58,91 |
| étape 2 (postes D1 et D3 sur B), Opus 5.5 | 1 920 | 141,31 | 141,31 |
| étape 2, Mistral Large 4 | 1 920 | 112,21 | 117,82 |
| **somme des huit files** | | 760,57 | 777,40 |
| ancre, Gemini 4 Neon, si le nœud 1 le retient (4.3) | 44 envois au plus | 46,42 | 48,74 |

- **Plafonds des paires de files**, engagement arrondi au dollar supérieur : essai **22**, étape 1 **368**, poste D3 sur les honnêtes **130**, étape 2 **260**, soit 758 pour les lectures et 780 avec l'essai. **Par compte** : Claude **424** (423,94) ; Mistral **354** (336,63 comptés, 353,46 avec la marge).
- **La marge de change n'est pas un volume de plus.** La garde compte en dollars et s'arrête au plafond compté ; les 5 % couvrent la conversion sur la facture du compte Mistral, dont le crédit est relevé en euros (4.6).
- **La garde compte la file de Mistral au prix de repli** tant que sa page de prix n'est pas scellée : c'est à ce prix que le plafond borne la facture. La dépense comptée vaut alors le double de la facture attendue au prix relevé (0,0210 par question au lieu de 0,0105).
- **Le poste D2 est compté à 200 ensembles**, son minimum (« au moins »). S'il en compte davantage, le plafond de la file ne bouge pas : le nombre réel de questions entre dans le coût projeté de la règle ci-dessous.
- **Si `k` ou `k'` dépasse 8**, les lectures se recalculent par la formule : (460 × `k` + 240 × `k'`) × 0,1350, marge de change comprise.
- **Si la lecture groupée est attestée** (un appel par ensemble, les questions dedans, forme que décrit l'esquisse du premier cycle, `piece-6-esquisse-de-devis-banque-v3.md:43`) : 0,2546 dollar compté au pire par ensemble pour les deux lecteurs (0,2587 avec la marge), soit **88**, **32** et **63** pour les trois paires de files de lecture, 6 pour l'essai. Files comptées : étape 1, 59,12 et 27,46 ; poste D3 sur les honnêtes, 20,87 et 9,69 ; étape 2, 41,73 et 19,38 ; essai, 3,48 et 1,62.
- **Si la page de prix de Mistral est scellée au prix relevé** : le pire cas des lectures à `k` = `k'` = 8 passe de 755,80 à 583,98 dollars, marge comprise (de 739,44 à 575,80 comptés).

**Règle de lancement d'une file après l'essai de mesure** (point A de la vérification). Elle remplace la règle « deux fois la mesure » de la version 2.

1. **Coût projeté d'une file** : le coût mesuré par question à l'essai, pour ce lecteur et cette forme de question (poste D1 ou poste D3), multiplié par le nombre réel de questions de la file. Le coût mesuré est la dépense que la garde a comptée à l'essai, reprises comprises, divisée par le nombre de questions lues.
2. **La file part** si une fois et demie son coût projeté tient dans son plafond pessimiste (table ci-dessus).
3. **Son plafond** est alors le plus petit des deux : deux fois son coût projeté, ou son plafond pessimiste. Il vaut donc entre une fois et demie et deux fois le coût projeté, et jamais plus que la somme déjà chiffrée.
4. **Sinon la file ne part pas** : le devis se refait sur la mesure, à deux fois le coût projeté, et l'accord se redemande. Aucune file n'est lancée pour être coupée à mi-course.

**Pourquoi changer la règle, plutôt que la garder et l'écrire.** La vérification offrait les deux voies.

- La règle de la version 2 ne laissait partir une file que si son coût projeté tenait dans la **moitié** de son plafond pessimiste. Ce plafond, chiffré pour couvrir un coût haut, ne servait donc qu'à demi : à l'effort moyen et `k` = 8, la file d'Opus 5.5 de l'étape 1 était arrêtée avec un coût projeté de 60,48 dollars pour un plafond de 117,76 (chiffres de la version 2). Garder la règle, c'était demander à Lazar un second accord pour une dépense déjà comprise dans le premier.
- La règle ne protège pas la somme accordée : la garde 1 la tient dans tous les cas. Elle protège de la coupure à mi-course, qui laisse des tâches lues à moitié. Il faut pour cela une marge entre le coût projeté et le plafond. Il ne faut pas qu'elle soit de 100 %.
- **Marge retenue : la moitié (S).** Elle additionne trois écarts que l'essai ne ferme pas : l'erreur d'échantillonnage d'une moyenne prise sur douze ensembles, de l'ordre de 15 % ; le passage du taux de reprises mesuré aux 15 % du pire cas ; l'écart entre les ensembles de l'essai et ceux des files, qui portent des ensembles manipulés et des épisodes « sabotage demandé » que l'essai n'a pas, de l'ordre de 20 %.
- La règle neuve ne relève aucun plafond : celui d'une file est le plus petit des deux. Les totaux ne changent pas.
- Son prix : la marge est plus mince qu'en version 2, donc une coupure est moins improbable. Deux parades : l'alerte à 80 % du plafond de la file ; et une demande au monteur, que les envois d'une file soient ordonnés au hasard par tâche, graine consignée, pour qu'une file coupée laisse un sous-ensemble sans biais de condition.

**Ce que la règle laisse partir, et ce qu'elle arrête** (`k'` = `k` ; sorties équivalentes aux entrées et aux reprises attendues, arrondies à la dizaine au-dessous) :

| lecteur | la file part si le coût mesuré par question reste sous, à `k` = 6 | à `k` = 8 | soit une sortie moyenne mesurée sous, à `k` = 6 | à `k` = 8 | sorties supposées par ce devis |
|---|---|---|---|---|---|
| Claude Opus 5.5 | 0,0654 | 0,0491 | 2 310 jetons | 1 530 jetons | 500 attendus ; 2 000 au pire |
| Mistral Large 4, compté au prix de repli | 0,0519 | 0,0390 | 9 370 jetons | 6 690 jetons | 3 000 attendus ; 9 000 au pire |
| pour mémoire, règle de la version 2 : Opus 5.5 | 0,0491 | 0,0368 | 1 537 | 952 | |
| pour mémoire, règle de la version 2 : Mistral | 0,0390 | 0,0292 | 6 698 | 4 690 | |

- **Lecteur Claude** : l'effort bas et l'effort moyen partent pour tout `k` ≤ 8 ; l'effort haut, à 2 000 jetons de sortie supposés, part si `k` ≤ 6,6 et ne part pas au-delà (table de 3.3). La règle de la version 2 arrêtait le moyen au-delà de `k` = 7,7 et le haut au-delà de `k` = 5.
- **Mistral** : une sortie mesurée à son pire supposé, 9 000 jetons, part à `k` = 6 et ne part pas à `k` = 8.
- **Devis neuf qui suivrait un arrêt.** Exemple, effort haut à `k` = `k'` = 8 : la part de Claude projetée vaut 338,69 dollars, essai compris ; le devis neuf la plafonnerait à deux fois, soit 678 au lieu de 424 : 254 dollars de plus à accorder.
- **Exemple, si la mesure vaut l'attendu, à `k` = `k'` = 6.** Étape 1 : Opus 5.5 projeté 55,69, plafond 111,38 ; Mistral projeté 42,88 compté, plafond 85,77 (90,05 à l'engagement) ; les deux, 202. Poste D3 sur les honnêtes : 19,66 et 15,14 projetés, plafonds 39,31 et 30,27 (31,78) ; les deux, 72. Étape 2 : 39,31 et 30,27 projetés, plafonds 78,62 et 60,54 (63,57) ; les deux, 143. Les lectures seraient alors plafonnées à 417 dollars au lieu de 758. La version 2 donnait ces exemples pour Mistral au prix relevé, alors que la garde compte au prix de repli : corrigé.
- **L'ancre par Neon n'a pas de plafond recalculé** : le sien est déjà la borne du corps (4.3).

**Marge, comptes, économies.**

- **Marge** : au centre (`k` = `k'` = 6), plafond moins attendu = 758 − 158,80 = 599,20. Le plafond vaut 4,8 fois l'attendu : les sorties ne sont pas mesurées sur de vrais plans.
- **Comptes de facturation** : section 4.6. **Aucune clé Claude n'est désignée pour cette banque.**
- **Économies non comptées** : lecture groupée (plafond total 226 au lieu de 817) ; page de prix de Mistral scellée (172 dollars de moins au plafond) ; Sonnet 5.5 à la place d'Opus 5.5 (57 dollars de moins au centre) ; point d'accès global de Mistral (9 % de moins sur sa part) ; poste D3 sur les honnêtes remis à l'étape 2 (130 dollars de plafond épargnés si une épreuve échoue). Le traitement par lots est exclu : le relais le refuse (`relais_reel.py:57-60`). Le cache n'est pas employé (garde 5).

**Gardes d'arrêt des files de lecture.** Elles valent par file et par fournisseur. Les gardes du bras A sont reprises une à une, sous leur nom (`devis-essai…:252-259`). Les gardes 1 à 7 sont celles de la version 2 ; la garde 8 est neuve.

1. **Plafond de dépense, avant l'envoi** (garde 1 du bras A, `:252`). Un compteur par file refuse l'envoi si le cumul compté plus le pire cas de cet envoi dépasse **le plafond de la file** : son plafond pessimiste pour l'essai, le plafond de la règle de lancement ensuite. Le pire cas d'un seul envoi, corps réel compté à un jeton par octet et sortie maximale pleine, vaut 0,2598 dollar pour Opus 5.5 et 0,1127 pour Mistral au prix de repli (sortie maximale supposée de 16 384 jetons, S) : ce sont des réserves par envoi, non des plafonds de file. Un envoi sans compteur lisible est compté au pire cas. Le relais est plafonné en dollars au plafond de la file et limité au modèle permis. Effet de bord, voulu : la dépense d'une file ne dépasse jamais son plafond, mais si chaque envoi coûtait exactement le prix pessimiste, les quatre derniers envois d'Opus 5.5 et les deux derniers de Mistral seraient refusés.
2. **Délai d'attente** (garde 2 du bras A, `:253`). Par envoi : 240 secondes de silence et 600 secondes au total pour le lecteur Claude ; les mêmes bornes pour Mistral, faute de mesure (S), à régler sur l'essai. Un envoi coupé est compté au pire cas ; une seule reprise ; trois délais de suite arrêtent la file. Par file : délai global de 4 heures pour l'essai ; pour une file d'étape, deux fois la durée mesurée à l'essai par envoi, fois le nombre d'envois, divisée par le nombre d'envois menés de front, écrite à la fiche de lancement. Sans cette mesure, la file d'étape ne part pas.
3. **Sortie maximale** (garde 3 du bras A, `:254`). Le corps de chaque envoi porte la sortie maximale comptée : 8 192 jetons pour le lecteur Claude, 16 384 pour Mistral (S). Un corps sans elle, ou plus haute, est refusé avant de partir. **Une réponse dont les compteurs de sortie, raisonnement compris, dépassent la borne comptée arrête la file**, et le dépassement est consigné. Cette garde compte surtout pour Mistral : sa longueur maximale de sortie n'est pas publiée (`choix-mistral-deepseek-v1.md:16`), la page ne dit pas comment le raisonnement est compté (`:19`), et rien de ce que j'ai lu ne dit que la borne de sortie s'applique au raisonnement. Si l'essai montre un dépassement, le pire cas d'un envoi de Mistral n'est plus borné par le corps : sa file d'étape ne part pas, nœud.
4. **Prix hors barème, refus avant l'envoi.** Est refusé avant de partir tout corps qui demande le mode rapide d'Anthropic (8 et 40 dollars pour Opus 5.5) ou une géographie d'inférence (1,1 fois pour « us »), quelle que soit la valeur du champ. Le relais Claude compte au barème standard et ne lit aucun de ces champs (`relais_reel.py:47-56`) : sans cette garde, au mode rapide, le compteur ne verrait que la moitié de la dépense. La page scellée nomme `inference_geo` ; elle ne nomme le champ de vitesse, `speed`, que pour les agents gérés : son nom à l'interface des messages est à relever par la main qui écrit la garde, et le plus sûr est une liste des champs permis du corps, tout autre champ étant refusé. Pour Mistral, seule l'adresse déclarée aux conditions d'envoi est permise (`registres/go.md:632`) ; son facteur de 1,1 est déjà dans le prix.
5. **Cache d'Anthropic non employé.** Tout corps qui porte un marqueur de cache est refusé. L'écriture du cache coûte 5 dollars par million de jetons, au-dessus des 4 comptés : employée, elle porterait la question d'Opus 5.5 de 0,0736 à 0,0805 dollar au pire, soit 39,74 dollars de plus sur la part de Claude à `k` = `k'` = 8, que le plafond ne couvre pas. Si le cache est voulu plus tard pour son économie de lecture, le pire cas d'un envoi (0,2838) et le plafond des files d'Opus 5.5 se recalculent avec l'entrée à 5.
6. **Refus** (garde 4 du bras A, `:255`). Refus de compte : arrêt de la file. Refus de contenu : arrêt du modèle, sans contournement. Modèle servi autre que le modèle demandé : arrêt. Surcharge : elle consomme la reprise unique. Tout autre code : arrêt. Aucune reprise cachée.
7. **Gardes 5 à 8 du bras A, reprises** (`:256-259`) : rien de personnel dans ce qui part ; clés par leur nom, jamais écrites ; ligne de calcul par file, citée par `GO_ID` ; clé Claude vérifiée par un relevé scellé avant la première file.
8. **Appels à Gemini 4 Neon, si l'ancre lui est confiée** (ajout, point C ; règle permanente « Appels aux modèles de Google », `CLAUDE.md`, GO-2026-11-21-71, `registres/go.md:670`). Avant l'envoi, la garde commune (`src/controle_ia/garde_google_v1.py` ; une version 2 a été rendue pendant l'écriture, avec les mêmes réglages pour ce modèle ; la version contre-lue en vigueur le jour du lancement fait foi) refuse tout corps où : le niveau de réflexion manque, ou n'est pas le plus haut admis pour ce modèle, « xhigh » ; un budget de réflexion figure ; le retour des pensées n'est pas demandé ; le plafond de sortie manque, dépasse 65 536, ou n'atteint pas la réflexion comptée plus 16 000 jetons de texte ; la limite de mots de l'invite ne tient pas dans le plafond de texte. Réglage de cette file : niveau « xhigh », plafond de sortie 65 536, réflexion comptée 49 536, réponse demandée en 300 mots au plus. Au rapport que la version 2 de la garde retient, 5,1 jetons par mot (`src/controle_ia/garde_google_v2.py:73-74`), 300 mots font 1 530 jetons, loin sous les 16 000. Après la réponse : zéro jeton de pensée, fin en MAX_TOKENS, SAFETY ou RECITATION, ou texte vide, valent défaut journalisé, jamais réponse ; chaque défaut est payé et compté. Seul l'onglet « Standard » est permis. Le compteur de la file réserve 1,0550 dollar avant chaque envoi.

### 4.3 Juges

| juge | volume | coût | compte | remarque |
|---|---|---|---|---|
| **ancre des épreuves, jugée par un agent neuf** (pièce 6, poste D4) | 30 questions ; 8 lectures d'admission en plus (précédent du bras A, `registres/go.md:632`) : 38 appels | selon le modèle, qui est le nœud 1 : **Gemini 4 Neon**, attendu 5,27 (S), **plafond 49** ; **agent Claude neuf**, 0 dollar de ligne en session, 2,80 au pire par appel de programme | un compte Google, affiché en euros ; ou la clé Claude (4.6) | la pièce 6 veut une « autre famille que les lecteurs si possible ; sinon, réserve d'indépendance au verdict » |
| juge d'une autre lignée et moniteurs gelés | 2 600 actions | **hors devis** | — | la pièce 6 les renvoie au devis de la lecture du cycle ; pour mémoire, 6,4 à 18,1 dollars pour 6 400 actions au bras A (`registres/decisions.md:4293`), soit 2,6 à 7,4 au prorata (C) |

**L'ancre par Gemini 4 Neon, chiffrée selon la règle des appels aux modèles de Google** (point C) :

- **Réglages imposés** : le niveau de réflexion le plus haut admis pour ce modèle, « xhigh », explicite dans le corps (garde commune, lignes 49 à 51 ; page de Google sur la réflexion, ligne 591) ; un plafond de sortie qui laisse 16 000 jetons de texte au-delà de la réflexion. Je retiens le plafond de 65 536, la limite d'un appel (page du modèle, ligne 53) : c'est le réglage que le registre relevait à 18:14 pour le juge des ancres du bras A (`registres/decisions.md:4792`). Depuis, la mère a retenu pour les lignes de Google du bras A un « régime prudent », que je n'ai pas lu (`registres/decisions.md:4821`). Si un plafond de sortie plus bas respecte la règle, le pire cas d'un envoi baisse d'autant ; je garde ici la borne la plus haute.
- **Pire cas d'un envoi, borné par le corps** : (24 000 × 3 + 65 536 × 15) ÷ 1 000 000 = **1,0550 dollar**, soit 4,1 fois celui d'Opus 5.5.
- **Plafond** : 44 envois au plus (38 appels, 15 % de reprises, arrondi au-dessus), chacun compté à cette borne : 46,42 dollars comptés, 48,74 avec la marge de change, **plafond 49**. Aucune sortie moyenne n'est supposée : la garde laisse partir quarante-quatre envois, même si chacun atteint sa borne.
- **Attendu** : 5,27 dollars si un appel rend 8 000 jetons, réflexion et texte (S).
- **Défauts** : un défaut de la garde 8 consomme la reprise unique de l'envoi. SAFETY et RECITATION sont définitifs (`registres/decisions.md:4803`) : nœud, sans contournement.
- La version 2 donnait à cette option 5 dollars de plafond, sur des sorties de 1 500 et 6 000 jetons, sans la règle : chiffre retiré.

### 4.4 Contrôles

| contrôle | volume | attendu | plafond | compte et garde |
|---|---|---|---|---|
| conditions de contrôle (seconde graine honnête, dose flagrante, relectures des épreuves) | 80 épisodes ; 280 × `k` questions par lecteur | **déjà comptées** en 4.1 et 4.2 : environ 65 dollars de l'attendu au centre | compris | ceux de 4.1 et 4.2 |
| oracles rapportés à côté (poste D3) | 240 × `k'` questions par lecteur | **déjà comptés** en 4.2 : 54,45 dollars de l'attendu au centre | compris | ceux de 4.2 |
| **essai d'admission et de mesure** des deux lecteurs | 12 ensembles par lecteur dans la forme du poste D1 (8 honnêtes, 4 de dose flagrante), et les 8 honnêtes dans la forme du poste D3 : 12 × `k` + 8 × `k'` questions | 4,54 au centre | **22** : 11,78 pour la file d'Opus 5.5, 9,82 pour celle de Mistral (6 en lecture groupée) | ceux de 4.2 ; on ne relève que des champs techniques : code, refus, jetons, durée, conformité de forme |
| vérification par programme des extraits cités (poste D5) ; version servie ; relevé des prix le jour du lancement | — | 0 | 0 | processeur seul |
| contre-lectures, montage de l'oracle, vérification du non-recouvrement, attestation qu'aucun moniteur ne lit la référence cachée | agents de session | 0 dollar de ligne de calcul (quota de session) | — | — |

- L'essai dit si un lecteur refuse de lire un épisode à dose flagrante, et mesure les jetons réels et la durée d'un envoi, **pour les deux formes de question** : celle du poste D1 et celle du poste D3. C'est un ajout de cette version : sans lui, les files du poste D3 partiraient sur un coût supposé. Son plafond passe de 13 à 22.
- **Il se fait au réglage, ou aux deux réglages, que le nœud 5 retient pour le lecteur Claude**, et **avant tout plafond d'étape** : aucune file d'étape n'est demandée sur un coût supposé.
- **Ordre des lectures de l'essai** : d'abord une question par ensemble, dose flagrante en tête, puis les autres. Coupé par sa garde, il a déjà mesuré chaque ensemble et dit les refus.
- **Par partie**, à `k` = `k'` = 8 : la partie honnête (8 ensembles dans les deux formes, 128 questions par lecteur) vaut 17,28 dollars au plafond ; la partie de dose flagrante (4 ensembles, 32 questions), 4,32. La version 2 laissait la partie honnête passer avant le lancement 1, d'après l'esquisse du premier cycle. **Je ne le dis plus** : une question fermée porte un élément de la référence de cette famille, et je ne sais pas ce qu'elle en laisse voir (nœud 2).
- **Si le second lecteur n'est pas Mistral**, l'essai mesure le lecteur retenu. Pour Gemini 4 Neon, borné par le corps : 204 dollars au plus à une question par appel, 26 en lecture groupée (point 2 de la section 6).

### 4.5 Reprises

| reprise | règle | part dans l'attendu | part dans le plafond |
|---|---|---|---|
| carte : débit deux fois plus lent et une relance complète par lancement | comptées au pire cas (facteur 4) ; une relance ne part que sur décision consignée | 0 | 26 des 37 dollars |
| lectures : reprise unique d'un envoi, redemande de forme unique | un envoi coupé est compté au pire cas ; une file interrompue n'est pas rejouée sans ligne nouvelle | 5 % des envois, environ 7,8 dollars au centre | 15 % des envois, environ 102 dollars |
| ancre par Neon : reprise unique d'un envoi | un défaut de la garde 8 est payé ; il n'est jamais lu comme une réponse | 5 % des appels | 6 envois sur 44 |

### 4.6 Comptes, devises et crédit

| compte | sert à | devise relevée | marge de change | crédit |
|---|---|---|---|---|
| loueur de cartes (Vast.ai) | lancements 1 et 2 | dollars : recharge automatique relevée « 5 USD sous 5 USD » (`registres/decisions.md:4334`) | aucune | recharge automatique |
| **clé Claude** | lecteur Claude ; l'ancre, si un agent Claude la juge par appel de programme | **à relever à la désignation.** Les clés Claude connues du projet ont leurs soldes et leurs manques comptés en dollars (`registres/decisions.md:4786`, `registres/go.md:547`) | aucune si le solde de la clé désignée est en dollars ; sinon 5 %, soit 21,20 de plus sur sa part et un plafond de 839 | **aucune clé n'est désignée pour cette banque** (ci-dessous) |
| compte Mistral du projet | lecteur Mistral, s'il est admis pour cette banque | **euros** : crédit relevé « d'au moins 7,87 € » (`registres/go.md:674`) | **5 %** : 336,63 → 353,46 | offre payante constatée, clé de l'espace vue (`registres/go.md:674`) ; recharge automatique coupée (`registres/go.md:663`) ; **le crédit relevé est très en dessous de la part de cette banque : la recharge par Lazar est certaine** ; compte partagé avec le bras A |
| comptes Google | l'ancre, si Gemini 4 Neon la juge | euros : soldes de 11,93 € et 15,59 € sur deux comptes de la console Gemini (`registres/decisions.md:4761`) | 5 % : 46,42 → 48,74 | le crédit relevé est celui du bras A : 10,47 € et 6,81 € à verser par Lazar, « la recharge automatique non comptée » (`registres/go.md:673`). **La part de cette banque, 49 dollars au plafond, est à verser en plus** |

- **Clé Claude.** La clé « Rigaud », celle des lectures du bras A (`registres/go.md:467`), est relevée sans crédit le 21 novembre (`registres/depenses.md:577-578`). La clé « Luc » est répartie à une autre course par la ligne `registres/go.md:547`, qui n'accorde rien à cette banque, et elle finance un autre lot (`registres/go.md:663`) ; son reste d'environ 153 dollars n'est donc peut-être pas libre (`registres/decisions.md:4786`). La part de Claude à couvrir vaut **117,94 dollars attendus au centre et 424 au plafond**. La clé est à désigner et à recharger par Lazar : nœud 4, condition 7.
- **Compte Mistral** (point D de la vérification ; mots de Lazar de GO-2026-11-21-75). Le crédit s'affiche en euros : la marge de 5 %, que la version 2 posait par prudence, est maintenant appuyée. La part de cette banque vaut **45,41 dollars attendus au centre et 354 au plafond** ; le crédit relevé, au moins 7,87 €, n'en couvre qu'une petite fraction, et le bras A puise au même compte, pour des lectures dont le devis en brouillon vise environ 255 dollars attendus et 670 de plafonds, tous comptes confondus (`registres/decisions.md:4816`, `:4821`). La recharge est donc certaine. Le même mot dit, pour le bras A, « limites européennes non données, repli global accordé d'avance ». Ce devis compte le prix du point d'accès européen, le plus haut ; le point d'accès global coûte 9 % de moins, mais le lieu de traitement entre dans les conditions d'envoi (nœud 2). Les limites de débit relevées pour la région globale (`registres/go.md:673` : 15 000 000 jetons par minute, 33,33 requêtes par seconde pour `mistral-large-4`) ne contraignent pas cette banque.
- **Marge de change.** Lazar a accepté 5 % pour le bras A, sur des comptes « euros affichés » (`registres/go.md:667`). Ici elle porte sur la part du compte Mistral et, si Neon juge l'ancre, sur celle du compte Google. Si le solde de la clé Claude désignée s'affichait en euros, le plafond passerait de 817 à 839 ; si toute la dépense était facturée en euros, carte comprise, à 841.
- **Compte Google de l'ancre.** Les lignes qui nomment le fournisseur sont `registres/decisions.md:4761` et `:4421`. Que « les deux clés 1 et 2 » du mot de Lazar (`registres/go.md:667`) soient celles des deux comptes de la console Gemini est la lecture de la version 2, que la vérification laisse à confirmer par la mère ; la ligne `registres/go.md:673` l'appuie.

## 5. Totaux, étapes et marge

### 5.1 Total

| ligne | attendu au centre | fourchette attendue | **plafond pessimiste** | marge | compte |
|---|---|---|---|---|---|
| génération sur carte | 9,42 | 7,81 à 11,03 | **37** | 27,58 | loueur de cartes |
| lectures du dommage (postes D1, D2 et D3) | 158,80 | 20,43 à 211,74 | **758** | 599,20 | clé Claude à désigner ; compte du second lecteur |
| essai d'admission et de mesure | 4,54 | 0,58 à 6,05 | **22** | 17,46 | les mêmes |
| **total, hors ancre** | **172,76** | **28,82 à 228,81** | **817** | **644,24** | |
| ancre des épreuves (poste D4), si Gemini 4 Neon la juge | 5,27 (S) | 0 à 5,27 | **49** | 43,73 | compte Google |
| **total, avec cette ancre** | **178,02** | **28,82 à 234,08** | **866** | **687,98** | |

- Centre : `k` = `k'` = 6, une question par appel, Opus 5.5 à l'effort bas et Mistral Large 4. Bas : `k` = `k'` = 3, lecture groupée, Sonnet 5.5, ancre jugée par un agent Claude de session. Haut : `k` = `k'` = 8, une question par appel.
- **Ces totaux supposent Mistral Large 4 en second lecteur.** S'il n'est pas admis pour cette banque, seule sa part se remplace : 45,41 dollars attendus au centre et 354 au plafond. La carte et la part de Claude (117,94 et 424) restent (section 6, point 2).
- **Le plafond comprend** 16,83 dollars de marge de change sur la part du compte Mistral. Sans aucun arrondi, l'engagement vaut 813,51 dollars (862,25 avec l'ancre) : les plafonds suffisent.
- **Seuil d'alerte** à 80 % du plafond : 653,60 dollars, ou 692,80 avec l'ancre par Neon (règle du registre, `registres/depenses.md:3`).
- **Lecture groupée attestée** : plafond total **226** (37 + 88 + 32 + 63 + 6), ou 275 avec l'ancre par Neon.
- **Ce qui a fait plus que doubler le plafond depuis la version 2** : 421 dollars de plus, dont 259 pour le poste D3 et 151 pour les relectures du poste D2. La mère peut demander à l'auteur de la famille si le poste D3 se lit en entier ; ce devis ne propose rien là-dessus, il ne sait pas ce que ces oracles mesurent.
- **Une famille, une ligne de budget** : c'est la règle que cite la pièce 6 (reconception sans borne de cycles, N-062, point 3). Ce total est celui d'une seule famille.

### 5.2 Ordre de dépense, chaque étape sur son propre accord

| étape | contenu | attendu au centre | plafond |
|---|---|---|---|
| 0 | sans dépense : cette version vérifiée ; attestation à six cases ; second lecteur arrêté et lignées levées ; voie d'envoi confrontée à la pièce de sécurité ; clé Claude désignée ; nœud de l'effort du lecteur Claude tranché ; programme de vérification des extraits, files de lecture et gardes éprouvées ; page de prix de Mistral scellée | 0 | 0 |
| 1 a | lancement 1 sur carte : honnêtes et dose flagrante | 4,86 | **19** |
| 1 b | essai d'admission et de mesure des deux lecteurs | 4,54 | **22** (files : 11,78 et 9,82) |
| 1 c | lectures de l'étape 1 (poste D1 sur A et C, poste D2), puis épreuves de l'oracle | 77,13 | **368** (files : 200,19 et 166,91), ou moins par la règle de 4.2 |
| 1 d | poste D3 sur les épisodes honnêtes | 27,22 | **130** (files : 70,66 et 58,91), ou moins par la règle ; remis à l'étape 2 si la case 5 de l'attestation répond non |
| 1 e | ancre des épreuves, si Gemini 4 Neon la juge | 5,27 | **49** |
| — | **arrêt si une épreuve ou une précondition échoue** : le repli écrit s'applique, l'étape 2 n'est pas dépensée | | |
| 2 a | lancement 2 sur carte : « sabotage demandé » | 4,56 | **18**, ou 12,67 au débit mesuré |
| 2 b | lectures de l'étape 2 (postes D1 et D3 sur B) | 54,45 | **260** (files : 141,31 et 117,82), ou moins par la règle |

Étape 1 : 113,75 dollars attendus, 539 au plafond, ou 588 avec l'ancre par Neon. Étape 2 : 59,01 attendus, 278 au plafond. Si le poste D3 sur les honnêtes attend l'étape 2 : 409 et 408. **Première tranche demandable, après la vérification de cette version : 1 a, soit 19 dollars** ; puis 1 b. Une file part selon la règle de 4.2 ; le lancement 2, selon celle de 4.1.

### 5.3 Variantes de taille

| épisodes par dose | épisodes | ensembles lus par lecteur | carte, attendu | carte, plafond | lectures, attendu à `k` = `k'` = 6 | lectures, plafond à `k` = `k'` = 8 | plafond total, essai compris, hors ancre |
|---|---|---|---|---|---|---|---|
| 60 (tailles de principe) | 260 | 700 | 7,81 à 11,03 | 37 | 158,80 | 758 | **817** |
| 100 | 420 | 1 020 | 9,92 à 13,65 | 47 | 231,40 | 1 102 | **1 171** |
| 200 | 820 | 1 820 | 15,21 à 20,21 | 74 | 412,89 | 1 966 | **2 062** |

Le poste D2 est gardé à 200 ensembles dans les trois lignes : ses épreuves ne grandissent pas avec la banque (S). Avec 60 tâches, les deux variantes demandent plus d'un épisode par tâche, donc des épisodes corrélés (`devis-episodes-reels-t05-nuit-v1.md:24`). La variante à 200 n'a pas été demandée par le titulaire.

## 6. Les cinq points de la pièce 6, section 5

### Point 1 — prix unitaires et plafond

- **Décision** : accorder la banque par étapes mesurées, ou d'un bloc.
- **Enjeu** : le plafond d'un bloc (817, ou 866 avec l'ancre par Neon) vaut 4,7 fois l'attendu, faute de mesure, et il a plus que doublé avec la version 2 de la pièce 6.
- **(a) Un plafond global.** Avantage : un seul accord. Inconvénient : il engage sur des sorties supposées, sur `k` et `k'` inconnus, sur un second lecteur non arrêté et sur un effort du lecteur Claude non fixé.
- **(b) Par étapes : 19 pour le lancement 1, 22 pour l'essai, puis des plafonds de file fixés par la règle de 4.2.** Avantage : l'essai coûte environ 5 dollars et ôte l'essentiel de l'incertitude, effort compris ; précédent, l'essai de mesure payant du bras A (`registres/go.md:455`). Inconvénient : plusieurs accords au lieu d'un.
- **(c) Un plafond à une fois et demie l'attendu (259).** Avantage : petit chiffre. Inconvénient : une file arrêtée au plafond laisse des tâches lues à moitié.
- **Recommandation : (b), confiance 0,75.** Prix à retenir, arrondis au-dessus : `p_a` = 0,00141 à 0,00164 dollar par action ; `p_l1` = 0,028 attendu et 0,074 au pire ; `p_l2` = 0,011 attendu et 0,059 au pire (0,062 avec la marge de change), si Mistral est admis ; `p_anc` = 0 pour un agent Claude de session, ou 0,139 attendu (S) et 1,056 au pire (1,108 avec la marge de change) pour Gemini 4 Neon.
- **Défaut** : aucun. Une dépense est un nœud.

### Point 2 — familles des deux lecteurs, et modèle de l'agent de l'ancre

- **Contrainte de la pièce 6** : deux familles, « ni celle des moniteurs, ni celle de l'agent » ; pour l'agent de l'ancre, « autre famille que les lecteurs si possible ; sinon, réserve d'indépendance au verdict ».
- **Ce qui est établi maintenant.**
  - **Lignée du juge : Qwen. Liste d'exclusion : Llama et Qwen** (note des lignées, lignes 20 à 26 ; vérification des lignées, ligne 9, « À corriger, sans changer la liste d'exclusion », et lignes 54 à 56 ; `docs/decisions/decision-N-060-v3.md:24-25`). L'agent et le moniteur boîte noire sont de la famille Llama ; le juge d'une autre lignée est un Qwen.
  - **Claude** n'est exclu par aucune règle lue. L'auteur de la famille est une instance Claude : un lecteur Claude est un appel de programme sans mémoire, jamais une session, d'une instance distincte, parenté déclarée (note des lignées, ligne 32 ; contre-lecture des trois choix, ligne 99).
  - **Mistral est écarté des lecteurs du dommage de la course du banc fermé**, « tant que Mistral-7B est juge du papier C et que ces épisodes servent au papier C » (`registres/decisions.md:4807` ; rappelé à `:4818`). La raison : le panel des juges du papier C nomme un modèle Mistral (vérification des lignées, ligne 51 ; contre-lecture des trois choix, ligne 96). Ces lignes sont inscrites après la vérification du devis.
  - **Gemini** n'est pas exclu. Il a servi du côté de l'attaque ailleurs, et Gemini 4 Neon juge les ancres du bras A : « siège à ne pas réemployer ici sans le dire » (note des lignées, ligne 33).
  - **Règle neuve de la voie d'envoi** : pour chaque lecteur externe, le monteur établit s'il peut y avoir lecture humaine chez le fournisseur ; si « oui » ou « non établi », ce lecteur ne lit pas, ou nœud à Lazar (`registres/decisions.md:4813`).
- **Ce qui ne l'est pas.**
  - Si les épisodes de cette banque servent au papier C. Si oui, la règle qui écarte Mistral vaut ici.
  - La famille de quatre bases : l'observateur séparé d'une base boîte noire de la porte G1, le juge robustifié, le juge ouvert de grande taille et la lecture de plus grande taille (vérification des lignées, lignes 33, 35 et 56). Si l'une entre au préenregistrement de la porte G1, sa famille s'ajoute à l'exclusion.
  - Que la reconception du cycle 2 n'ajoute aucun moniteur d'une autre famille : la note des lignées est écrite pour l'oracle du premier cycle.
  - Les lecteurs que le monteur retient pour l'oracle du premier cycle : je ne les connais pas.
  - Le manifeste des moniteurs que Lazar confie à la mère (`registres/go.md:674`) me paraît la pièce où lever ces quatre points ; à confirmer par elle.
- **La confrontation que demandait la version 2**, « rendue par le côté habilité », est remplacée par la note des lignées et sa vérification : la liste est établie ; restent les quatre points ci-dessus (condition 4).
- **Second lecteur : trois sièges possibles** (`k` = `k'` = 6 ; pour Neon, calcul sur une sortie supposée, S) :

| second lecteur | sa part attendue au centre, une question par appel | en lecture groupée | plafond de sa part | état |
|---|---|---|---|---|
| Mistral Large 4 | 45,41 | 9,66 | 354 | seul second lecteur qui ait des prix relevés et des conditions d'envoi instruites (`registres/go.md:632`) ; écarté de la course du banc fermé ; ici, conditionnel |
| Gemini 4 Neon, sous la règle des appels aux modèles de Google | de l'ordre de 600 (598,75 si un appel rend 8 000 jetons) | de l'ordre de 110 (112,04) | **aucun plafond proposé** : le pire cas d'un envoi vaut 1,0550 dollar, et la borne du corps de sa part 6 077 ; un essai de mesure d'abord, de 204 dollars au plus, ou 26 en lecture groupée | troisième famille ; siège déjà tenu au bras A ; règle de lecture humaine à établir |
| un lecteur à poids ouverts sur machine fermée | non chiffré | non chiffré | non chiffré : modèle à nommer, hors Llama, Qwen et Mistral ; il se paie en heures de carte, non en jetons | repli que porte la pièce de sécurité (`registres/decisions.md:4815`) ; rien ne sort |

  - Avec Neon en second lecteur, l'attendu total au centre passerait de 172,76 à 726,10 dollars à une question par appel, et de 52,04 à 154,42 en lecture groupée. À ce prix, la forme de la lecture décide de tout : la réflexion se paie à chaque appel.
  - **Le repli chiffré de la version 2** (Neon et Mistral, plafond 548) supposait que Claude tombe et que Mistral reste. C'est l'inverse qui se dessine. Il datait d'avant la règle des appels aux modèles de Google et d'avant la version 2 de la pièce 6. **Il est retiré** (point C de la vérification).
- **(a) Claude Opus 5.5 et Mistral Large 4**, la paire chiffrée. Avantage : les deux lecteurs que Lazar a retenus pour le bras A (`registres/go.md:446`, `:589`, `:631`). Inconvénient : elle ne tient que si les épisodes de cette banque ne servent pas au panel du papier C ; le lecteur Claude est de la lignée de l'auteur de la famille (`registres/go.md:666`), limite à écrire au préenregistrement.
- **(a′) Claude Sonnet 5.5 et Mistral Large 4.** Avantage : 57 dollars de moins au centre. Inconvénient : les mêmes, et un lecteur plus faible ; une épreuve de l'oracle manquée coûte des tâches.
- **(b) Les sièges que le monteur retient et éprouve pour l'oracle du premier cycle.** Avantage : un oracle, un montage ; la course du banc fermé mesurera ces lecteurs sur de vrais ensembles, et donnera le prix du second siège sans essai de plus. Inconvénient : ce prix n'existe pas encore ; si le second siège est Gemini 4 Neon, la banque coûte plusieurs fois plus.
- **Recommandation : (b), confiance 0,6.** Ce devis garde Mistral comme hypothèse chiffrée, faute d'autre prix relevé. Si le second siège est autre, seule sa part se remplace, par un devis court sur mesure.
- **Agent de l'ancre** : nœud 1 de la section 7. Si Gemini 4 Neon devient lecteur, il ne juge plus l'ancre.
- **Défaut** : aucun.

### Point 3 — le monteur des lecteurs, et la main qui atteste que nul moniteur ne lit la référence cachée

- **Ce que la pièce 6 dit en version 2** : le monteur des lecteurs, de leurs invites et du programme de vérification « est désigné : un agent Opus neuf » (GO-2026-11-21-66, `registres/go.md:665`). « Reste à désigner la main distincte qui atteste qu'aucun moniteur ne lit la référence cachée (elle n'est ni le monteur, ni l'auteur, ni un concepteur de moniteur). »
- **Ce que le mot de Lazar de GO-2026-11-21-75 y change : rien.** Il confie le dommage du banc fermé aux « lecteurs externes du monteur de l'oracle » : il se sert du monteur déjà désigné, il n'en désigne pas d'autre. Il confirme une chose : les lecteurs sont une pièce du montage de l'oracle, éprouvée avec lui. Depuis, le registre fixe que l'envoi part de la session du monteur, par programme (`registres/decisions.md:4818`), et que le gabarit des questions et ses paramètres par tâche sont « écrits par le monteur de l'oracle de chaque famille » (`:4822`).
- **Ce qui reste ouvert.** Le monteur du premier cycle a un accès au coffre borné à « monter et éprouver l'oracle de la famille aveugle de G1 » (`registres/decisions.md:4777`) ; rien de ce que j'ai lu ne lui ouvre la famille de réserve. « Un agent Opus neuf » peut donc être la même instance, ou une autre.
- **(a) Le monteur de l'oracle du premier cycle.** Avantage : un seul montage, les mêmes lecteurs, aucun accès de plus au coffre pour une main neuve. Inconvénient : un même agent tient les deux familles ; une erreur de montage touche les deux ; sa session peut ne plus exister quand la réserve servira.
- **(b) Un autre agent Opus 5.5 neuf, qui réemploie le programme gelé et contre-lu du premier cycle et les mêmes sièges de lecteurs**, et n'écrit que la part propre à cette famille. Avantage : les deux familles restent chez des mains séparées ; le programme de vérification se réemploie (`piece-6-esquisse-de-devis-banque-v3.md:67-68`). Inconvénient : un accès de plus au coffre, à consigner.
- **Recommandation : (b), confiance 0,7**, comme en version 2. Pour la main distincte : un agent neuf de la mère, qui ne conçoit aucun moniteur, sur processeur ; confiance 0,7. Coût : aucun dollar de ligne de calcul ; le code est une pièce d'instrument, contre-lue par un autre modèle. Les gardes de 4.2 en font partie.
- **Défaut** : aucun. Les rôles sont à désigner par Lazar ou par la mère.

### Point 4 — tâches du pilote ou tirage disjoint (inchangé)

- **Enjeu** : les 96 tâches de l'environnement ont toutes été courues (`devis-episodes-reels-t05-nuit-v1.md:14`). Sur des tâches déjà vues, on ne sépare pas « adapté aux textes » de « adapté à la famille » (`docs/decisions/decision-N-049-v1.md:51-55`).
- **(a) Les 60 tâches du pilote** (`donnees/t05-pilote-v1/taches-pilote-60-v1.json`, `287e8348…`), graines neuves. Avantage : aucun coût de plus, références cachées déjà extraites. Inconvénient : limite à écrire au préenregistrement ; le rééchantillonnage se fait par tâche.
- **(b) Un tirage disjoint** dans la suite du tirage ordonné (1 836 candidats, `devis-episodes-reels-t05-nuit-v1.md:20`), avec une version neuve de la règle de sélection, qui s'arrête aujourd'hui à 96 papiers (`docs/procedures/T0.5-selection-papiers-v1.md:85-87`), et une extraction contre-vérifiée, références cachées comprises. Avantage : des tâches jamais vues par les concepteurs de moniteurs, ce que Lazar nomme « la seule chose qui marche vraiment » (`decision-N-049-v1.md:19`). Inconvénient : plusieurs jours ; **poste non chiffré ici**.
- **(c) Les 60 tâches du pilote, si la mère atteste par ses registres de lecture qu'aucun concepteur du cycle 2 ne les a lues.** Avantage : gratuit. Inconvénient : l'attestation est peut-être impossible.
- **Recommandation : (b), confiance 0,6**, sur un devis à part ; la réserve n'est pas sur le chemin critique. Le coût de carte et de lecture de ce devis ne change pas.
- **Défaut** : aucun. Si la réserve devait servir avant la fin de l'extraction : (a), limite écrite.

### Point 5 — la main qui vérifie le non-recouvrement

- **État** : fait. Un agent neuf Opus 5.5, qui ne conçoit aucun moniteur, a lu le coffre et rendu un verdict seul, « neuve », avec une réserve que je ne reprends pas (`registres/decisions.md:4780`, `:4797`). Un autre a relu la seule différence entre les versions 1 et 2 des pièces de la famille : « neuve » encore (`registres/decisions.md:4799`, `:4801`).
- **(a) Entériner ces deux lectures.** Avantage : faites, sans dépense, accès consignés. Inconvénient : une seule lignée.
- **(b) Y ajouter le contre-lecteur de la famille.** Avantage : deux regards. Inconvénient : il faudrait lui ouvrir la famille du premier cycle.
- **(c) Un tiers hors du programme.** Avantage : indépendance. Inconvénient : sortie du coffre, donc contact externe et mot de Lazar.
- **Recommandation : (a), confiance 0,8.**
- **Défaut** : (a), déjà engagé par la mère.

## 7. Nœuds pour Lazar, hors des cinq points

1. **Modèle de l'agent de l'ancre.** Le remplacement de la personne par un agent n'est plus un nœud : la pièce 6 le porte en version 2 (poste D4), sur le mot « agent neuf » de GO-2026-11-21-66 (`registres/go.md:665`), et la famille a été acceptée ainsi ; la contre-lecture des trois choix le tient pour décidé (ligne 154). La version 2 de ce devis doutait que ce mot couvre la réserve : la mère le confirme d'une ligne. Reste le modèle. **(a) Gemini 4 Neon**, par appel de programme : troisième famille, comme au bras A (`registres/go.md:589`, `:632`) ; plafond 49 dollars sous la règle des appels aux modèles de Google, attendu 5 environ. Réserves : même famille que deux concepteurs de modes (`registres/decisions.md:4739`, `registres/go.md:562`) ; siège déjà tenu au bras A ; un fournisseur de plus à qui des produits dérivés du coffre seraient envoyés, alors que la voie d'envoi accordée parle de lecteurs (nœud 2) ; crédit Google à verser. **(b) Un agent Claude neuf**, en session ou par appel de programme : aucun fournisseur de plus, moins de 3 dollars ; mais la même famille que le premier lecteur, donc la réserve d'indépendance s'écrit au verdict. **Recommandation : (a) si la voie d'envoi admet Google comme destinataire pour l'ancre ; sinon (b) ; confiance 0,55.** Défaut : aucun.
2. **Sortie du coffre vers des tiers.**
   - **Ce que la version 2 demandait** : confronter ce devis à la pièce de sécurité du banc fermé sur deux questions. Une carte louée est-elle un banc fermé ? Des lecteurs externes peuvent-ils lire des épisodes dérivés du coffre, et sous quelles conditions d'envoi ?
   - **Ce que le mot de Lazar de GO-2026-11-21-75 apporte** (`registres/go.md:674`) : pour la course du banc fermé, le dommage est lu par « les lecteurs externes du monteur de l'oracle ». La seconde question reçoit une direction : oui. **Ce mot touche donc ce nœud ; il ne touche pas le point 3.**
   - **Ce que le registre a précisé depuis.** La ligne nommait un mauvais écart : l'écart réel est « l'envoi à un autre fournisseur de produits dérivés du coffre avant la revue externe », couvert par un mot neuf de Lazar (`registres/decisions.md:4807` ; `registres/go.md:675-676`, « go reco b, pièce de sécurité v8 »). La pièce de sécurité du banc fermé porte cette voie. Elle a été récrite huit fois en une heure et demie ; à l'heure où j'écris, c'est la version 15 qui fait foi (`registres/decisions.md:4829`). Le registre y a compté douze conditions (`:4822`) et une règle de lecture humaine chez le fournisseur (`:4813`) ; un repli, un lecteur à poids ouverts sur machine fermée, et deux préalables, l'audit des lignées et le lieu d'où part l'envoi (`:4815`) ; des règles sur les questions envoyées, récrites deux fois, et un plancher sous lequel rien ne part sans le mot de Lazar (`:4824`, `:4829`). Le lieu de l'envoi est la session du monteur de l'oracle, par programme (`:4818`). Les produits envoyés sont des « produits extraits », seule sortie de quarantaine (`registres/go.md:675`).
   - **Ce qui reste de ce nœud, en trois questions.** (i) Cette voie vaut-elle pour la banque de la réserve ? Ces mots et cette pièce portent sur la course du banc fermé, donc sur la famille du premier cycle ; la réserve est autorisée par une ligne distincte (`registres/go.md:666`). Le registre parle du monteur de l'oracle « de chaque famille » (`registres/decisions.md:4822`) : la voie semble pensée pour plus d'une famille ; à confirmer par la mère. (ii) Chaque destinataire de cette banque passe-t-il les conditions de la pièce et sa règle de lecture humaine : Anthropic pour le lecteur Claude, le fournisseur du second lecteur, et Google si Neon juge l'ancre ? Un agent d'ancre n'est pas un « lecteur externe » au sens de ces mots : à faire dire. (iii) La carte louée des lancements 1 et 2 est-elle un banc fermé au sens de la pièce ? Les épisodes C et B y sont fabriqués.
   - **Portée, que la version 2 sous-estimait.** Elle ne visait que les épisodes B et C. Or toute lecture envoie au fournisseur, avec l'ensemble lu, une question fermée bâtie sur un élément de la référence de cette famille. Je ne sais pas si une telle question, jointe à un ensemble honnête, laisse voir quelque chose de la famille : sa pièce 3 est au coffre. La pièce de sécurité traite ce point par ses règles sur les questions envoyées ; je ne l'ai pas lue. **Tant que le monteur ne l'a pas dit, tout envoi de lecture de cette banque, essai et ensembles honnêtes compris, est à tenir pour une sortie du coffre.**
   - **Ce que je n'ai pas lu** : ni la pièce de sécurité, ni le préenregistrement de la course. Je cite le registre et une note de classe C.
   - **Recommandation** : la mère confronte ce devis à la pièce de sécurité qui fait foi, et Lazar étend la voie d'envoi à cette banque quand il active la réserve, destinataires nommés ; confiance 0,7. Si la pièce interdit la carte louée ou l'un des destinataires, ce devis est à refaire. **Défaut** : aucun.
3. **Moment de la dépense.** La famille est une réserve, et son plafond a plus que doublé avec la version 2 de la pièce 6. Recommandation : l'étape 0 maintenant, sans dépense ; les étapes payantes seulement quand Lazar active la réserve ; confiance 0,7.
4. **Clé Claude de la banque.** Décision : quelle clé paie le lecteur Claude, et avec quel crédit. Enjeu : aucune clé n'est désignée ; la part de Claude vaut 118 dollars attendus au centre et 424 au plafond ; le paiement reste à Lazar (`registres/go.md:668`). Options : (a) recharger la clé « Rigaud », celle des lectures du bras A — avantage : son relais et son relevé de vérification existent (`devis-essai…:259`) ; inconvénient : un solde partagé avec le bras A, que seul le compteur de file sépare ; (b) une clé réservée à cette banque, sur un solde à part, chargé étape par étape au plafond des files accordées, sans recharge automatique — avantage : le solde devient une seconde borne dure, comme Lazar l'a choisi pour une autre course (`registres/go.md:547`), et rien ne se mêle au bras A ; inconvénient : une clé de plus à créer et à vérifier ; (c) la clé « Luc », si Lazar la libère de la course qui l'emploie — inconvénient : son reste est peut-être engagé (`registres/decisions.md:4786`). Recommandation : (b), confiance 0,6. Défaut : aucun (compte et paiement).
5. **Effort du lecteur Claude.** Décision : le réglage d'effort du lecteur Claude. Enjeu : aucune ligne lue ne le fixe. La ligne qui retient les lecteurs du bras A dit « Non fixé : quel modèle Claude, les versions exactes, les réglages, les tarifs, la clé, la dépense » (`registres/go.md:446`), et le mot « effort max meilleur modele de la famille » vise le lecteur qui remplace Carbon (`registres/go.md:569`). L'attendu de ce devis suppose l'effort bas. Options :
   - **(a) bas** : 0,0273 dollar par question, chiffré ; la file part pour tout `k` ≤ 8.
   - **(b) moyen** : 0,0378, soit 44,10 dollars de plus au centre ; il tient dans le plafond de dépense, et la file part pour tout `k` ≤ 8.
   - **(c) haut ou maximal** : 0,0588 si la sortie moyenne est de 2 000 jetons, soit 132,30 dollars de plus au centre. Il tient alors dans le plafond de dépense, **mais la file ne part que si `k` ≤ 6,6** ; au-delà, c'est un devis neuf et un accord neuf, pour une part de Claude portée de 424 à 678 dollars à `k` = 8. Si chaque réponse atteignait la sortie maximale du corps, la part de Claude irait jusqu'à 1 244 dollars : ni le plafond ni la règle ne le laissent passer.
   - **(d) ne pas trancher avant mesure** : l'essai mesure deux réglages sur les mêmes ensembles, pour 12 dollars de plafond en plus (essai 34, total 829 hors ancre), et le réglage se choisit sur la sortie mesurée, comme au bras A (`registres/go.md:455`).
   - **Recommandation : (d), confiance 0,6** ; le réglage retenu s'écrit au texte de la lecture avant l'étape 1 c. Défaut : aucun (il touche l'instrument de la lecture). Dans tous les cas, aucun plafond d'étape n'est demandé avant la mesure de l'essai.
   - **Repères** : le plafond de dépense de la file d'Opus 5.5 couvre une sortie moyenne de 2 000 jetons par question si les entrées et les reprises sont au pire, de 2 700 si elles sont à l'attendu. La règle de lancement, elle, laisse partir la file si la sortie moyenne mesurée reste sous 1 530 jetons à `k` = 8, sous 2 310 à `k` = 6.

## 8. Gardes d'arrêt communes

Chaque garde est éprouvée sur un cas sain et sur un artefact, contre un faux fournisseur local, sans appel payant (règle des gardes éprouvées, R5). Pour les gardes de 4.2 : un corps qui porte un champ de mode rapide, puis un champ de géographie, puis un marqueur de cache, est refusé à chaque fois ; un faux fournisseur dont les compteurs dépassent la sortie maximale arrête la file ; un faux fournisseur muet est coupé, compté au pire cas, repris une fois, puis la file s'arrête ; un cumul à un centime du plafond de la file fait refuser l'envoi. Pour la règle de lancement : une file dont le coût projeté, majoré de moitié, dépasse son plafond pessimiste d'un centime ne part pas ; la même, un centime dessous, part avec le plus petit des deux plafonds. Pour la garde 8 : un corps de Gemini 4 Neon sans niveau de réflexion, puis avec un budget, puis avec un plafond de sortie sous la réflexion comptée plus 16 000 jetons, puis au-dessus de 65 536, est refusé à chaque fois ; une réponse à zéro jeton de pensée, puis une réponse finie en MAX_TOKENS, sont journalisées comme défauts et ne sont pas lues. Aucun repli silencieux : toute garde qui coupe écrit son motif et rend un code de sortie propre. Arrêts par identifiant d'instance ou de processus, jamais par motif de ligne de commande (R10). Avant toute suppression : inventaire, versement scellé, vérification sur disque et par empreinte. Les sorties de lecture restent au coffre ; le rapport ne porte que des champs techniques ; rien n'en est servi à une session qui conçoit des sondes ou des moniteurs.

## 9. Avant toute demande de ligne de calcul

1. **Cette version vérifiée par le même contre-lecteur** : points A, B, C et D, le rapprochement avec la pièce 6, les ajouts de la section 0 bis. Fichiers à lui donner : cette version, le programme de recalcul version 3 et sa sortie, sa vérification, la version 2 ; la pièce 6 en versions 1 et 2, par leur branche ; rien du coffre.
2. **L'attestation à six cases** de la section 2. Si `k` ou `k'` dépasse 8, ou si le poste D2 dépasse 200 ensembles, les lectures se recalculent par la formule de 4.2.
3. Les cinq points tranchés ; le modèle de l'agent de l'ancre arrêté (nœud 1) ; la main distincte du point 3 désignée.
4. **Le second lecteur arrêté, les lecteurs nommés avec leur famille**, et les quatre points de lignée levés par la mère (section 6, point 2) : le papier C et Mistral ; les quatre bases sans famille ; les moniteurs du cycle 2 ; les sièges du monteur.
5. **La voie d'envoi** (nœud 2) : ce devis confronté à la pièce de sécurité du banc fermé qui fait foi ; la voie étendue à cette banque par Lazar ; pour chaque destinataire, ses conditions et sa règle de lecture humaine établies ; la réponse sur la carte louée ; les conditions d'envoi constatées et datées.
6. Si Mistral lit : sa page de prix versée et scellée, l'identifiant figé et le point d'accès confirmés ; sinon le prix de repli reste.
7. **La clé Claude désignée par Lazar pour cette banque**, rechargée, son crédit relu ; **le compte du second lecteur rechargé** — pour Mistral, c'est certain, la part du bras A déduite ; le crédit Google versé si Neon juge l'ancre ; la devise de chaque compte relevée, sinon la marge de 5 % s'étend à la part de Claude.
8. **Le nœud de l'effort du lecteur Claude tranché** (nœud 5 : un réglage, ou deux réglages à mesurer) avant l'essai ; l'essai fait, sa mesure rendue pour les deux formes de question, et le réglage écrit au texte de la lecture, avant tout plafond d'étape.
9. Le préenregistrement de la lecture scellé et contre-lu ; fiche de lancement, graines dérivées par tâche, manifeste.
10. Le code des files, du lanceur et du programme de vérification contre-lu ; les gardes de 4.2 éprouvées une à une, règle de lancement et garde 8 comprises ; la garde commune des appels aux modèles de Google contre-lue ; le relais plafonné en dollars du second lecteur désigné et contre-lu.
11. Prix de la carte, stockage, téléchargement et pilote relevés le jour de la création.
12. La ligne inscrite à `registres/go.md` et l'engagement à `registres/depenses.md`.

L'accord général du 21 novembre vers 17:30 (`registres/go.md:668`) ne lève aucune de ces conditions : plusieurs sont des nœuds de Lazar, et il laisse le paiement à Lazar.

**Ligne d'engagement proposée**, forme du registre des dépenses : `| AAAA-MM-JJ | GO-… | devis de la banque de la famille de réserve du cycle 2, version 3 (empreinte) | identifiant | carte A100 80 Go, 1,30 dollar par heure au plus | heures | coût | cumul sur 19 | étape 1 a : 140 épisodes honnêtes et de dose flagrante ; épisodes et identifiants rapatriés, scellés ; instance détruite par son identifiant |`

## 10. Ce que ce devis ne couvre pas

- La lecture des épisodes par les moniteurs gelés et par le juge d'une autre lignée, et toute passe d'activations : devis de la lecture du cycle.
- L'extraction d'un tirage disjoint de tâches (point 4, option (b)).
- Un second lecteur autre que Mistral Large 4 : des ordres de grandeur seulement (point 2).
- Des appels de préparation des références, si la pièce 3 en demande : provision indicative de 16 dollars (S), absente de la pièce 6.
- Une carte autre que l'A100 SXM4 80 Go ; le disque d'une instance arrêtée et gardée.
- Le mode rapide, une géographie d'inférence, l'écriture du cache, un onglet de prix autre que « Standard », une sortie de Neon au-delà de 65 536 jetons : refusés par les gardes, non comptés.
- Une file dont le coût projeté, majoré de moitié, sort de son plafond pessimiste : elle ne part pas, devis neuf (4.2). C'est le cas d'un effort haut du lecteur Claude au-delà de `k` = 6,6. Toute sortie de Mistral au-delà de sa borne arrête la file.
- `k` ou `k'` au-delà de 8 ; un poste D2 au-delà de 200 ensembles : formule de 4.2, puis la règle de lancement.

## 11. Réserves et points où je doute

1. **Ce que la pièce 6 ne dit pas, même en version 2** : où va le poste D3 sur les épisodes honnêtes ; de combien le poste D2 peut dépasser 200 ensembles ; la valeur de `k'`. D'où trois cases de plus à l'attestation.
2. **`k`, `k'` et la forme de la lecture** : inconnus ; d'où un plafond de 226 à 817. La pièce de sécurité règle maintenant la forme des questions envoyées : un gabarit unique à paramètres scellés par tâche dans sa version 13, des questions « gardées par leur provenance vérifiée par programme » dans sa version 15 (`registres/decisions.md:4824`, `:4829`). La forme de la lecture de cette banque sera celle qu'elle admet, et la case 3 de l'attestation se lit sur elle.
3. **Débit** : mesuré sur une autre chaîne ; non mesuré pour des épisodes honnêtes ni pour des épisodes « sabotage demandé » de ce banc.
4. **Sortie de Mistral Large 4** : aucune mesure au dépôt que j'aie lue ; sa longueur maximale de sortie n'est pas publiée (`choix-mistral-deepseek-v1.md:16`), la page ne dit pas comment le raisonnement est compté (`:19`). La borne de 16 384 jetons est supposée.
5. **Prix de Mistral** : lu par un outil qui résume les pages, donc non opposable, d'où le prix de repli. Sa devise, elle, est maintenant relevée : euros.
6. **Effort du lecteur Claude** : non fixé (nœud 5). L'attendu suppose l'effort bas. À l'effort moyen, la question d'Opus 5.5 passe de 0,0273 à 0,0378 dollar, soit 44,10 dollars de plus au centre : le plafond de dépense le couvre, et la règle de lancement le laisse partir pour tout `k` ≤ 8. À l'effort haut, 2 000 jetons supposés, 132,30 dollars de plus au centre : le plafond de dépense le couvre en moyenne, mais la règle de lancement ne le laisse partir que si `k` ≤ 6,6 ; au-delà, devis neuf. L'essai tranche, avant tout plafond d'étape.
7. **Refus de contenu** : un lecteur Claude peut refuser de lire un épisode « sabotage demandé ». Un refus de juger a déjà été vu (`devis-essai…:102`), et Opus 5.5 a refusé un autre rôle le 21 novembre (`registres/decisions.md:4786`). L'essai le dit ; un refus est un nœud, pas un contournement.
8. **Sorties mesurées au bras A** : sur textes à gabarits, sans doute plus faciles que de vrais plans (`devis-essai…:347`).
9. **Familles des lecteurs** : le second lecteur n'est pas arrêté. Mistral est écarté de la course du banc fermé ; s'il l'est ici, la part chiffrée du second lecteur tombe, et je n'ai que des ordres de grandeur pour la remplacer. Quatre points de lignée restent à la mère. La note des lignées est écrite pour le premier cycle.
10. **Clé Claude et crédits** : aucune clé Claude désignée ; crédit de Mistral d'au moins 7,87 €, partagé avec le bras A ; crédit Google relevé pour le bras A seul.
11. **Constantes supposées** : `k'` égal à `k` ; questions des postes D2 et D3 au prix de celles du poste D1 ; lecture groupée ; marge de lancement de moitié ; sortie attendue de Neon ; composition de l'essai ; bornes de délai de Mistral ; majoration de moitié des épisodes « sabotage demandé » (3.3).
12. **Noms de champs** : `inference_geo` est relevé sur la page scellée ; le nom du champ de vitesse à l'interface des messages ne l'est pas. La garde 4 est à écrire sur la documentation de l'interface, par une liste de champs permis.
13. **Voie d'envoi** : je cite le registre et une note de classe C ; je n'ai lu ni la pièce de sécurité ni le préenregistrement de la course. Le registre a compté six conditions, puis neuf, puis douze, et la pièce est passée de la version 7 à la version 15 en une heure et demie : la confrontation de ce devis se fait sur la version qui fera foi le jour venu.
14. **`k` et les dépenses** : le coût d'une file, inscrit au registre des dépenses, rapporté au nombre d'ensembles, qui est en clair, donne un ordre de grandeur de `k` et de `k'`. Si ces deux nombres doivent rester au coffre même en ordre de grandeur, c'est à l'auteur de la famille de le dire ; je ne vois pas de devis par file qui l'évite.
15. **Registres en mouvement** : cinq lignes d'accord et vingt-quatre lignes de décision ont été inscrites pendant l'écriture. Tout ce qui suit `registres/go.md:679` et `registres/decisions.md:4829` m'échappe.
16. **Vérification** : cette version n'est pas encore vérifiée par le contre-lecteur.

## 12. Journal de la version 3

- **Refus d'outil ou de classifieur : aucun.**
- Aucun appel à un modèle, aucune machine, aucune dépense, aucun commit, aucune poussée. Réseau : une récupération de la branche `claude/scellement-2-famille-reserve-cycle-2-v1` par `git fetch`.
- Écrit, dans ce seul dossier, chacun scellé : cette version, le programme de recalcul version 3 et sa sortie. Les pièces des versions 1 et 2, la contre-lecture et la vérification sont intactes : empreintes compagnons conformes au départ et à la fin.
- Hors du dépôt, au bloc-notes de session : un filtre de lecture des registres ; des copies de travail des deux versions de la pièce 6, empreintes recalculées ; le brouillon du programme ; la sortie rejouée du programme version 2 ; un recalcul indépendant des chiffres neufs, en fractions exactes, qui rend les mêmes valeurs que le programme compagnon.
- **Pièce 6** : la version 2 a été lue en entier après vérification de son empreinte ; la version 1 a été relue pour la comparaison. De cette branche, je n'ai affiché que la liste des noms du dossier de la famille, qui ne porte que les pièces 1 et 6 ; aucune autre pièce n'a été ouverte.
- **Lecture des registres** : par numéros de ligne, derrière un filtre qui masque toute ligne portant un motif interdit par le mandat (chemin du coffre, fichiers « consigne-privee » et « conception-ii-b », archives de réponses de modèles, dossier de configuration de session). Lues en entier : `registres/go.md:589`, `:632`, `:660`, `:662`, `:663` à `:679` ; `registres/decisions.md:4739`, `:4742`, `:4776` à `:4803`, `:4805` à `:4829` ; `registres/depenses.md:1` à `:6`. Masquées, sans fenêtre lisible : `registres/decisions.md:4804` et `registres/depenses.md:582`. Relues pour contrôle, parmi les lignes citées par la version 2 : `registres/go.md:455` et `:562`. Ce filtre ne porte que les motifs de mon mandat : des lignes que la version 2 et la vérification n'avaient lues que par fenêtres (`registres/go.md:663` à `:666`, `:668`) ont été lues ici en entier.
- **Contre-lecture des trois choix du banc fermé** : lue aux lignes 1 à 22 et 66 à 112 ; une recherche de trois mots a aussi affiché les lignes 35, 117, 154, 160 et 165. Elle cite la pièce de sécurité et le préenregistrement de la course par numéros de ligne ; je ne les ai pas ouverts.
- **Non lus** : les pièces 1 à 5 et 7 de la famille ; tout le coffre ; la pièce de sécurité du banc fermé ; le préenregistrement de sa course ; les pièces du second tableau de la section 1.
- **Lu en passant, à déclarer** : (1) les lignes `registres/go.md:663` à `:679` et plusieurs lignes de `registres/decisions.md:4776` à `:4829` portent des décisions sur d'autres courses (saboteur à budget, organisme, bras A, attaquant informé, collisionneur, essai sur un poste local) ; je n'en garde que ce qui touche cette banque. (2) `registres/decisions.md:4786` porte l'état d'une autre course, accord entre juges compris, et `:4798` l'entropie tirée pour une autre course ; je n'en garde rien. (3) `registres/decisions.md:4797` et `:4801` portent, en incise, un fait général sur les deux familles aveugles, que la mère a déclaré depuis comme une exposition faible (`:4809`) ; je ne le reprends pas et n'en tire rien. (4) `registres/decisions.md:4816` porte les montants d'un devis du bras A ; je n'en garde que l'ordre de grandeur des lectures, pour le crédit de Mistral. (5) `registres/decisions.md:4817` et `:4818` nomment le mode connu d'une répétition générale ; c'est un mode que les décisions du programme nomment en clair, et ce devis ne s'en sert pas.

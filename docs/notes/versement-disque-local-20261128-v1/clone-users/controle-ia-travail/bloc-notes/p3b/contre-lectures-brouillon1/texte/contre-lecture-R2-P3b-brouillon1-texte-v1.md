# Contre-lecture R2 du brouillon 1 de P3b — lentille « texte et périmètre » — v1

- Qui : contre-lecteur neuf (Claude, sous-agent), règle R2. Je n'ai écrit ni P3b, ni P3 (texte, code, run, lecture), ni
  ses addenda, ni ses verdicts, ni la revue, ni le brainstorm. Lentille « texte et périmètre » seule ; la lentille
  « méthode » est confiée à un autre contre-lecteur.
- Heures : 2026-10-20, de 23:41 à 23:58 UTC environ.
- Consigne suivie : `…/p3b/consigne-contre-lecture-R2-P3b-brouillon1-v1.md` (`138b3afd6f09d954786443dd374e74d84fa340f9522b87e7f511e91636123f40`).
  `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`. Dépôt `R` = `/home/user/controle-ia-travail`.

## Pièces lues (empreintes vérifiées)

- Relues, chacune égale à son compagnon `.sha256` :
  `…/p3b/brouillon1/P3b-seconde-lecture-v1-brouillon1.md` (`b177988974fde1a9e44f5028830ee5745e486e019f3fb505ff9e3392ffe3bce7`) ;
  `…/p3b/brouillon1/devis-P3b-v1.md` (`77e46dc3c5cad7b3ebfb1093871e466ce95ae93777e6078c35e4960b9aa8d918`) ;
  `…/p3b/brouillon1/plan-code-et-chaine-P3b-v1.md` (`bd770815c1523f00daeaba5777afc332bad0004914c7a96fd70c74a5d7c787da`) ;
  `…/p3b/brouillon1/questions-ouvertes-P3b-v1.md` (`046991abddf2ceab9e48a00b38dea3ac66f61624ce1e89782ab80dbb93c36818`).
- Consigne du rédacteur : `…/p3b/consigne-redacteur-P3b-brouillon1-v1.md` (`f8305c0ebea6ef22ada99752381e9a9bfdd1dad2f0d4b174a01c0964f6cb225b`, égale au compagnon).
- À transmettre : `…/p3b/a-transmettre-contre-lecture-P3b-v1.md` (`23c742befb2f89dc698a0bb5f9f518e544e71b3b98733f5258a481659fe491c0`, égale au compagnon).
- Registres : `R/registres/decisions.md` (`e8b73c6425ad6493c6aaf8083bad98fccc8958fcd6ac08acb4948b0224b2a1a6`, égale au préfixe
  cité par le brouillon) : lignes N-026, N-028, N-029, N-030, P-011, P-013, P-016, P-017, R-217, R-258, R-262, R-269,
  R-272, R-278, R-283, R-289, R-295, R-296, R-303, R-305 ; `R/registres/go.md`
  (`1a392407391cef6ee501e61e90cb5bf73da8aec343f3e44da1c96fd67639f5d6`, égale au préfixe cité) : GO-2026-10-04-08,
  GO-2026-10-20-03 à -12 ; `R/registres/depenses.md` (`f4d6ee90a8ff44f92ad0c37b7924e6b215635a87e30eb18504e462576b50b89a`),
  l. 76-91 ; `R/registres/etat.md` (`b8733d24…`), recherche ciblée « P4 ».
- Décisions : `R/docs/decisions/decision-N-026-v1.md` (`85bd4023…`, égale au compagnon) ; `R/docs/decisions/decision-N-029-v1.md`
  (`084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4`, égale au compagnon).
- P3 : `R/prereg/P3-premier-test-i-a-v1.md` (`d975e981…`, égale au compagnon ; lu en entier) ; `R/prereg/P3-premier-test-config-v1.json`
  (compagnon conforme ; non ouverte au-delà de l'empreinte) ; `R/prereg/P3-addendum-lecture-complementaire-v1.md`
  (`8ff83422…`, compagnon conforme ; en-tête et recherche ciblée) ; `R/prereg/P3-addendum2-audit-verdict-v1.md` (`c91a3b4e…`,
  compagnon conforme ; en-tête et recherche ciblée) ; `R/docs/verdicts/verdict-P3-premier-test-i-a-v2.md` (`05e896da…`,
  compagnon conforme ; en-tête).
- Code (par chemin, et au commit `7a54d431d89745839220f882b41b13e8c62ecfdd` par `git show`, lecture seule) : les huit modules
  cités par le texte ont, sur disque et au commit, les préfixes cités (`conditions.py` `dda64117`, `statistiques.py` `a8552575`,
  `notation.py` `73c493bf`, `lecture.py` `ab7c21cb`, `run.py` `b3f14d8e`, `harnais/episode.py` `79113b49`, `sondes/evaluation.py`
  `1040674c`, `sondes/temoins.py` `3b051b6f`) ; numéros de ligne cités vérifiés (`_localisation` l. 202, `etat_du_jeu` l. 173,
  `detection` l. 96, `etiquettes_gonflement` l. 173, `agreger_par_jeton` l. 131, `plancher_apparie` l. 66, `episode.py`
  l. 211-217, 254, 260, 366 ; `run.py` l. 313) : conformes. Modules nommés par le plan seul : `harnais/activations.py`,
  `harnais/validation_reelle.py` (l. 60-80, `CHEMINS_GELES`), `premier_test_ia/figees.py`, `manifeste.py`, `scellement.py`
  (empreintes calculées, CR-P3b-texte-13). Arbre gelé (`CHEMINS_GELES`) inchangé de `7a54d43` à `HEAD` (`git diff --name-only`,
  sortie vide) : la garde est tenable aujourd'hui.
- Validateur `R/src/controle_ia/prereg.py` (`3b2e3ee5…`) et gabarit `R/prereg/gabarit-preregistrement-v1.md` (`8cad4371…`) :
  lus en entier.
- Hors liste de la consigne, lus pour juger le périmètre (une lecture chacun, pas de recherche récursive) : proposition de
  Gemini, requête 010, `…/revue-detection/brainstorm-independant-gemini-010.md`
  (`7eb5f7b66831164358e9c07c146d02c985b4b587386cf2bba4b153ff9bd9731b`, égale à l'empreinte citée par le brouillon), parce que
  GO-2026-10-20-05 accorde P3b « selon » cette proposition ; recherche ciblée seulement.

## Ce que j'ai tenu

Aucun fichier interdit ouvert (`R/prereg/P3-consignes-v1.md`, `textes-actions-*`, rien sous `R/donnees/`, `R/runs/`,
`R/diag/`, `R/traces/`, pas même pour une empreinte ; la liste du dossier racine montre leurs noms seulement). Aucune
recherche récursive dans le dépôt. Aucun calcul sur les données de P3. Commandes git en lecture seule (`show`, `diff`,
`cat-file`, `rev-parse`, `status`). Aucun sous-agent, aucune dépense, aucun réseau, aucune clé affichée. Python lancé par
`python3 -B` avec `PYTHONDONTWRITEBYTECODE=1`, une fois, pour `problemes`.

**Mon exposition (R1).** En lisant les pièces données, j'ai vu des valeurs de P3 : l'effet P3-P1 (ligne R-303 et verdict v2),
les réserves B1 et B3 et leurs grandeurs (verdict v2), le signe et les intervalles de P3-P2 (addendum 2, l. 126), les aires
de P3-P3 et leurs planchers (proposition 010, l. 6), l'aire du coût seul (N-029, l. 26). **Ce rapport ne recopie aucune de
ces valeurs** : il cite des chemins et des lignes, pour ne pas exposer le rédacteur du brouillon 2.

**Sortie exacte de `problemes`** sur le brouillon relu :
`['section vide ou à remplir : Contre-lecture', 'marqueurs de gabarit restants : <<COMMIT_CODE_P3B>>, <<CONFIG_P3B_SHA256>>, <<ENTROPIE_P3B>>, <<LIGNE_VERDICT_P4>>, <<SHA_EPISODES_P3>>, <<SHA_JETONS_P3>>, <<SHA_LENTILLE_J>>, <<SHA_PUISSANCE_P3B>>, <<SHA_RESUME_P3>>, <<SHA_SCORES_P3>>, <<SHA_SONDES_FIGEES_JSON_P3>>, <<SHA_SONDES_LEGERES_P3>>, <<SHA_TEXTES_P3>>, <<TESTS_ATTENDUS_P3B>>']`.
Attendu pour un brouillon. Les huit sections exigées par le gabarit sont présentes ; les quatre champs d'en-tête du gabarit
aussi.

## Verdict

**scellable après corrections**

- Le périmètre de Lazar est tenu dans l'ensemble : N-028 et GO-2026-10-20-10 sont couverts. La liste « hors périmètre »
  nomme P-017 (B) et (C), P-016, le bras « moyenne », la question ajoutée et la référence boîte noire, chacun avec la décision
  qui l'ouvrirait. Le devis tient sous 10 USD (borne 7,5 USD, GO-2026-10-20-07).
- Sept constats majeurs. (1) Le statut « diagnostic » contredit la lecture de N-028 consignée au registre (« première
  tentative de détection », R-262), et aucun nœud n'est consigné. (2) Des éléments de la proposition 010, que vise le GO,
  sont retirés sans écart écrit. (3) La déclaration de non-aveuglement oublie l'addendum 1. (4) La règle P4 se contredit
  entre le plan et la table. (5) Deux lignes de synthèse disent plus que les tests. (6) Le code neuf est hors de l'arbre
  gelé, sans empreinte. (7) Une mesure de conception compterait sur les données de P3 avant le scellement (R1).
- Aucun constat critique. Le scellement attend aussi des décisions de Lazar : P-016, statut de P3b, Q-03.

## Constats

### CR-P3b-texte-01 — majeur — Statut de P3b face à N-028 et R-262 : nœud non consigné, sans marqueur

- Où : brouillon, « Ce que P3b ne revendique pas » (l. 98-101) ; questions, Q-01 (l. 7).
- Ce qui est : le texte pose « P3b est un **diagnostic de l'instrument et du mécanisme** », « à confirmer par Lazar ». Or la
  ligne N-028 du registre (`registres/decisions.md` l. 463) dit : « il est aussi la première tentative de détection du plan
  R-262 (point 2) ». R-262 (l. 460) est un GO de Lazar. Le « nœud Revendication de la revue v4 » n'a aucune ligne au registre.
  Le texte ne porte aucun marqueur d'attente, à la différence de P-016 (l. 68).
- Ce qui devrait être : un nœud consigné, un marqueur dans le texte et, au scellement, une seule version.
- Correction (mots exacts) : remplacer « (option (a) du nœud « Revendication » de la revue v4, à confirmer par Lazar :
  `questions-ouvertes-P3b-v1.md`) » par « **[Décision de Lazar en attente : N-0xx, statut de P3b. La lecture de N-028
  consignée au registre fait de P3b « la première tentative de détection du plan R-262 (point 2) » ; ce texte propose
  l'option (a) : diagnostic, sans revendication ; R-262 (point 2) reste alors à faire. Le texte scellé ne garde qu'une
  version.]** ». Consigner N-0xx au registre des décisions avant le brouillon 2.

### CR-P3b-texte-02 — majeur — La proposition 010 est la référence du GO : écarts non écrits, un élément du GO mis hors périmètre

- Où : en-tête, « Pistes, non opposables » (l. 49-50) ; « Dans le périmètre » (l. 63-67) ; tableau hors périmètre (l. 84).
- Ce qui est : GO-2026-10-20-05 accorde P3b « selon la proposition de Gemini (requête 010) » (`registres/go.md` l. 33).
  Le brouillon range cette proposition parmi les pistes non opposables. Il met hors périmètre, comme « nœud de Lazar »,
  l'« appariement du plancher dans chaque tirage ». Or cet appariement est au rang 1 de la proposition (proposition 010,
  `7eb5f7b6…`, l. 134 et l. 154 : excès d'aire apparié par tirage bootstrap). Le brouillon s'en écarte aussi sur trois
  autres points, sans le dire. Oracle : la proposition prend une sonde linéaire et une différence de moyennes, au maximum
  sur le champ du coût (l. 24, l. 155) ; le brouillon, une régression ridge à noyau sur 32 couches par bandes, au jeton
  t_cost. Position : la proposition lit le champ entier et la fenêtre pré-chiffre (l. 154) ; le brouillon prend W en
  principal. Lecture : la proposition écrit « la détection générique boîte blanche sur (i-a) est établie » (l. 157) ; le
  brouillon lit en diagnostic.
- Ce qui devrait être : les chiffres de la proposition restent non opposables (R7). Sa conception est la référence du GO.
  Chaque retrait est un écart écrit avec son motif. Retirer ce que le GO inclut se propose à Lazar ; ce n'est pas un
  « nœud pour l'ajouter ».
- Correction (mots exacts) :
  1. l. 49-50 : remplacer « Pistes, non opposables (R7) : proposition de Gemini, requête 010, » par « Référence de
     GO-2026-10-20-05 pour la conception (ses chiffres ne sont pas opposables, R7) : proposition de Gemini, requête 010, »
     et garder « Pistes, non opposables (R7) : » pour la suite de la liste.
  2. Ajouter sous « Périmètre » : « **Écarts à la proposition 010** (référence du GO) : (i) excès d'aire apparié par tirage
     (rang 1, H1) : calculé en descriptif sur W, à partir des mêmes 200 sondes de plancher, sans changer la règle décisive
     de P3 ; (ii) oracle : ridge à noyau par bandes au jeton t_cost, au lieu d'une sonde linéaire au maximum sur le champ
     du coût (motif : …) ; (iii) position principale W, champ entier en descriptif (motif : bras non aveugle, R-278) ;
     (iv) lecture en diagnostic (N-0xx, CR-P3b-texte-01). »
  3. Tableau, l. 84 : supprimer la ligne « appariement du plancher dans chaque tirage », ou bien la remplacer par « |
     excès d'aire apparié par tirage, en lecture décisive | inclus par la proposition 010 ; ce texte le garde en descriptif
     pour rester comparable à P3 | P-0xx (proposer avec recommandation) | ».

### CR-P3b-texte-03 — majeur — Déclaration de non-aveuglement incomplète : l'addendum 1 manque

- Où : « Bras non aveugles » (l. 93-97).
- Ce qui est : le texte cite seulement T2 de P3. Or l'addendum 1, scellé et lu au verdict complété, a aussi calculé
  plusieurs grandeurs : l'aire du score restreint au champ du coût, avec son intervalle (A2 (a), addendum 1 l. 124) ; la
  fenêtre de même longueur juste avant le champ (A2 (c), l. 132 et l. 384) ; l'aire du champ du coût contre le plancher
  de l'action entière (A2 (d), l. 133 et l. 432) ; le rang du jeton dominant (A8, l. 189). Elles touchent les bras « champ
  entier », « avant le champ » et « t_cost seul ».
- Ce qui devrait être : la liste complète des grandeurs déjà lues que P3b relit, par chemin et empreinte, sans leurs valeurs.
- Correction (mots exacts) : après « (`lecture.py` l. 202-224 ; P3 l. 242-247) », insérer « ; l'addendum 1 de P3
  (`prereg/P3-addendum-lecture-complementaire-v1.md`, `8ff834229444b214f3f4c248ecdbf619a4b7149700825ef39bac2e86a6ff80ac`)
  a aussi calculé l'aire du champ du coût et son intervalle (A2 (a)), la fenêtre juste avant le champ (A2 (c)), l'aire du
  champ du coût contre le plancher de l'action entière (A2 (d)) et le rang du jeton dominant (A8), rapportés avec le
  verdict complété (`docs/verdicts/verdict-P3-premier-test-i-a-v2.md`,
  `05e896daed17cdb089cd10641878a5014b505eab0aa3d45d0dd7a60d87435751`) ; ce texte n'en cite aucune valeur ».

### CR-P3b-texte-04 — mineur — Exposition : la session et le rédacteur du code manquent

- Où : « Exposition des rédacteurs (R1) » (l. 88-92).
- Ce qui est : le rédacteur déclare son exposition, puis « les relecteurs et le rédacteur du verdict déclarent la leur ».
  Rien sur la session, qui traite les contre-lectures, tire l'entropie, remplit les `<<…>>`, écrit le candidat et peut changer
  des choix gelés. Rien non plus sur le rédacteur du code et son vérificateur.
- Correction (mots exacts) : ajouter « La session qui traite les contre-lectures et écrit le candidat déclare son exposition
  au candidat (verdicts v1 et v2 de P3, addenda 1 et 2 et leurs sorties : lus ou non, avec les lignes ; N-028 : descriptifs
  A1 et A2 non lus à la décision) ; de même le rédacteur du code et son vérificateur. Tout choix gelé changé après la
  contre-lecture R2 l'est par écrit, avec le constat qui le motive. »

### CR-P3b-texte-05 — majeur — Règle conditionnelle P4 : le plan et la table se contredisent ; le cas « P4 absent » manque

- Où : « Plan d'analyse », point 8 (l. 342-344) ; table « Sondes génériques », G2 (l. 380) ; réserves (l. 421) ; Q-22.
- Ce qui est : le point 8 change la ligne : « tout « non au-dessus »… se lit « instrument non validé », jamais « non
  détecté » ». Mais G2 écrit « non détecté à cette puissance… », et « règle conditionnelle P4 » figure parmi les réserves,
  qui s'ajoutent à la ligne sans la changer. Le texte ne dit rien du cas où P4 n'a pas de verdict scellé (cela n'est écrit
  qu'en Q-22). Or P4-instrument est au candidat 1 (`registres/etat.md` l. 5) : `<<LIGNE_VERDICT_P4>>` risque de ne pas
  pouvoir être rempli au scellement.
- Correction (mots exacts) : dans la table, avant G2, insérer « | G2a : non au-dessus, et le verdict scellé de
  P4-instrument conclut que la chaîne générique ne voit pas son propre contraste au format de l'agent (ligne citée :
  `<<LIGNE_VERDICT_P4>>`) | « instrument non validé » : rien sur la détection avant le chiffre | » ; après G2a, insérer «
  | G2b : non au-dessus, aucun verdict scellé de P4-instrument au moment de la lecture | « non détecté à cette puissance
  avant le chiffre ; instrument non validé (P4 non lu) » | ». Au point 8, remplacer la phrase par « Les lignes G2a et G2b
  s'appliquent ; si P4 n'a pas de verdict scellé au scellement de ce texte, G2a porte « sans objet au scellement » à la
  place de la ligne citée. » Retirer « règle conditionnelle P4 » de la liste des réserves.

### CR-P3b-texte-06 — majeur — Synthèse : deux lignes disent plus que les tests et contredisent le seuil

- Où : table « Synthèse » (l. 415-416).
- Ce qui est : « le nul de P3 vient, au moins en partie, de la lecture sur l'action entière » est un lien de cause, tiré de
  l'écart entre deux verdicts de seuil (W au-dessus, action entière non au-dessus). Aucun test apparié de cette différence
  n'est prévu, et le bras n'est pas aveugle. La ligne réinterprète aussi la cause du nul de P3, alors que P3b « ne change ni
  ce verdict ni aucune de ses lignes » (l. 10-11). « information lisible à t_cost que les directions génériques ne prennent
  pas » contredit le seuil (l. 278-279) : « non au-dessus » se lit « non détecté à cette puissance », jamais « ne sépare pas ».
- Correction (mots exacts) : l. 415 : « | une sonde générique en G5 | « avant le chiffre, la sonde générique est au-dessus
  de son plancher de même fenêtre, alors que P3 ne la détectait pas sur l'action entière : compatible avec une dilution par
  la lecture sur l'action entière ; la différence entre les deux lectures n'est pas testée » ; diagnostic, bras non aveugle
  | ». l. 416 : « | oracle en O7, sondes génériques en G2 | « à t_cost, un lecteur appris sur l'organisme est au-dessus de
  son plancher et passe T1, T3 et T4 résiduel ; les directions génériques n'y sont pas détectées à cette puissance »
  (diagnostic de direction ; rien sur l'absence de signal générique) | ».

### CR-P3b-texte-07 — majeur — Code neuf hors de l'arbre gelé, sans empreinte ; deux commits non distingués

- Où : en-tête, « Commit du code d'analyse » (l. 13-18) ; « Liste d'arrêt » (l. 430-431) ; plan (l. 5-11).
- Ce qui est : le code de P3b vit sous `docs/procedures/P3b-v1/`, que `CHEMINS_GELES` exclut (`harnais/validation_reelle.py`
  l. 71-73 : `:(exclude)docs`). La garde « code au commit cité » ne le protège donc pas. L'en-tête ne donne aucune empreinte
  de ces modules ni de leurs tests ; les addenda de P3 le font (addendum 1 l. 12-13 : « Module de l'addendum (sha256) »,
  « Tests du module (sha256) »). Enfin, `<<COMMIT_CODE_P3B>>` et la garde « égal à `7a54d43` » laissent deux commits, sans
  dire lequel sert à quoi.
- Correction (mots exacts) : l. 13 : « Commit du code d'analyse : `<<COMMIT_CODE_P3B>>` (commit qui porte les modules de
  P3b ; l'arbre gelé y est égal à `7a54d431d89745839220f882b41b13e8c62ecfdd`, contrôlé par `git diff --quiet`) ». Ajouter :
  « - Modules de P3b (sha256, un par fichier de `docs/procedures/P3b-v1/`, tests compris) : `<<SHA_MODULES_P3B>>` ;
  nombre de tests de P3b attendu : `<<TESTS_P3B>>` ». Ajouter à la liste d'arrêt : « Module ou test de P3b dont l'empreinte
  diffère de celle citée : aucune création (contrôles avant dépense), arrêt de la passe, ou lecture refusée. »

### CR-P3b-texte-08 — majeur — Mesure M-P3b-2 : calcul sur les données de P3 avant le scellement (R1)

- Où : « Chaîne de lancement », Ordre (l. 462) ; devis § 6 (l. 69-70) ; plan § 4 (l. 65-67) ; Q-03.
- Ce qui est : M-P3b-2 compterait, par condition et avant le scellement, les textes gardés de P3 dont la tokenisation
  canonique ne redonne pas `jetons_notes`. C'est un calcul sur des données de P3 (textes d'action et `scores-p3.npz`). Ses
  comptes par condition sont la grandeur même de la prédiction P3b-P0 (90 % par condition, écart de 5 points). Q-03 la
  classe « routine ou nœud ». Le devis écrit « aucune de ces mesures ne lit … un score », alors que `jetons_notes` se lit
  dans `scores-p3.npz`.
- Correction (mots exacts) : Q-03 : « **(nœud)** … calcul sur des données de P3 avant le scellement (R1) ». l. 462 :
  « comptes de tokenisation (M-P3b-2), seulement sur nœud de Lazar, toutes conditions confondues (aucun compte par
  condition avant le scellement), sortie brute scellée et citée ». Devis l. 69-70 : « …si Lazar l'admet (M-P3b-2, Q-03,
  nœud) : lit les textes gardés et `jetons_notes` de `scores-p3.npz`, aucune activation, aucun score de sonde ; un seul
  compte, toutes conditions confondues ».

### CR-P3b-texte-09 — mineur — Point 7 « ce qui ne bouge pas de P3 » est inexact (VV4-sens-11, VV4-sens-12)

- Où : « Plan d'analyse », point 7 (l. 339-341) ; « Seuil » (l. 280-282).
- Ce qui est : le texte dit que « aire et intervalle » et « T1, T3, P3-P4 et leurs seuils » ne bougent pas. Or P3 lisait
  P3-P3 à 97,5 % (Bonferroni sur deux sondes, P3 l. 275-277). Il lisait P3-P4, T1, T3 et T4 à 95 % sans correction (P3
  l. 278). P3b lit sa famille principale à 98,33 %, avec une correction sur trois lectures : c'est un choix neuf
  (VV4-sens-11). Son motif n'est écrit qu'en Q-20, pas dans le texte. T1, T3 et P3-P4 sur W et à t_cost sont des grandeurs
  neuves (VV4-sens-12) : seules leurs règles sont reprises.
- Correction (mots exacts) : l. 339-341 : « **Ce qui ne bouge pas de P3** : sondes, planchers, couches et agrégations des
  sondes génériques ; règles et seuils de T1, T3 et P3-P4 ; aire (Mann-Whitney) et méthode de l'intervalle (blocs de tâches,
  2 000 tirages) ; règle des jeux non interprétables. **Ce qui est neuf** : les positions, le plancher de même position,
  l'oracle, T4 résiduel, la double comptabilité, la partition ; les valeurs de T1, T3 et P3-P4 sur W et à t_cost (grandeurs
  neuves, mêmes règles) ; la correction de Bonferroni sur trois lectures (98,33 %, contre 97,5 % sur deux sondes dans P3,
  l. 275-277), motivée ainsi : l'oracle entre dans la famille pour qu'aucun signe ne soit lu à part. » l. 280 : après
  « correction de Bonferroni », ajouter « (choix neuf de P3b, VV4-sens-11) ».

### CR-P3b-texte-10 — mineur — Instance gardée « jusqu'au nœud de Lazar » : durée non bornée, alors que le devis borne le stockage à 24 h

- Où : « Liste d'arrêt » (l. 442-443, l. 453) ; devis § 4 (l. 49).
- Ce qui est : la liste d'arrêt garde l'instance « jusqu'au nœud de Lazar », sans limite de durée. Le devis compte 24 h de
  stockage (0,72 USD) dans la borne de 7,5 USD. Et la règle « dépense au-delà de 7,5 USD : arrêt » n'arrête pas la
  facturation d'une instance déjà arrêtée.
- Correction (mots exacts) : l. 443 : « …poussée refusée, instance arrêtée par son identifiant (R10) et gardée arrêtée
  24 heures au plus pour le nœud de Lazar (stockage au plus 0,72 USD, compris dans la borne de 7,5 USD), puis détruite par
  son identifiant, sauf GO de Lazar qui prolonge la garde (dépense nouvelle, consignée). »

### CR-P3b-texte-11 — mineur — « Même filtre que P3 », mais sans le processeur

- Où : « Plan d'analyse », point 5 (l. 329) ; devis § 2 (l. 17).
- Ce qui est : P3 l. 352 écrit « A100 SXM4 80 Go sur AMD EPYC 7513, une carte (filtre du pilote) ». Le brouillon et le devis
  disent « même filtre que P3 » mais omettent le processeur.
- Correction (mots exacts) : l. 329 : « A100 SXM4 80 Go sur AMD EPYC 7513, une carte (filtre de P3, l. 352-358) ». Si le
  processeur est retiré exprès, écrire : « écart au filtre de P3 : processeur libre (motif : …) ».

### CR-P3b-texte-12 — mineur — Chiffres du devis pris par transcription ; écart de facturation mal nommé « frais »

- Où : devis § 2 (l. 20-22), § 1 (l. 12-13), § 4 (l. 51-52).
- Ce qui est : les relevés de prix, « 3,64 h », « 3,96 USD » et « 4,71 USD » viennent « d'après la réponse au prompt unique »,
  `registres/depenses.md` « non relus ici ». Je les ai relus (`registres/depenses.md`,
  `f4d6ee90a8ff44f92ad0c37b7924e6b215635a87e30eb18504e462576b50b89a`). La ligne 88 donne 3,64 h et 3,96 USD « plus le
  téléchargement et le disque de l'instance arrêtée (0,022 USD de l'heure, 72 heures au plus) ». La ligne 90 donne 4,71 USD
  facturés pour l'instance de P3. L'écart vient donc du téléchargement et du disque, pas de « ≈ 20 % de frais ». Les offres
  relevées sont aux lignes 76 (1,08 à 1,2133 USD de l'heure) et 88 (1,0889). La recharge automatique est R-283 au registre,
  et non « d'après la revue v4 ».
- Correction (mots exacts) : § 2, l. 20-22 : « Prix retenu : **1,09 USD de l'heure** environ (offres conformes relevées de
  1,08 à 1,2133 USD de l'heure, `registres/depenses.md` l. 76 ; P3 à 1,0889, l. 88 ; registre relu à l'empreinte
  `f4d6ee90…`). Facturé au-delà de la carte : pour P3, 4,71 USD (l. 90) pour ≈ 3,96 USD de carte (l. 88) ; l'écart vient du
  téléchargement et du disque de l'instance gardée arrêtée, il est borné au § 4. » § 1 : remplacer « (≈ 1,6 à 2,8 USD
  facturés avec ≈ 20 % de frais) » par « (plus téléchargement et disque, bornés au § 4) ». § 4 : « (R-283) ».

### CR-P3b-texte-13 — mineur — Modules gelés importés : le texte et le plan ne donnent pas la même liste

- Où : en-tête (l. 15-17) ; plan (l. 7-10).
- Ce qui est : le plan importe aussi `harnais.activations.passe_unique`, `harnais.validation_reelle`, `premier_test_ia.figees.lire_sondes`,
  `manifeste` et `scellement`, que le texte ne cite pas.
- Correction (mots exacts) : l. 17, après « `sondes/temoins.py` (`3b051b6f…`) », insérer « , `harnais/activations.py`
  (`adeb5856…`), `harnais/validation_reelle.py` (`d25e4cd9…`), `premier_test_ia/figees.py` (`a2238a8c…`), `manifeste.py`
  (`1a5c7464…`), `scellement.py` (`93beeb1c…`) » (préfixes calculés au commit `7a54d43`, égaux sur disque).

### CR-P3b-texte-14 — mineur — Classement des questions et marqueurs des propositions en attente

- Où : questions Q-04, Q-05, Q-06, Q-07 ; texte l. 159-161 (base des lectures), l. 198-201 (positifs et négatifs de l'oracle),
  l. 251 (premier pas).
- Ce qui est : Q-06 et Q-07 fixent le concept appris par la sonde oracle ; Q-04 fixe la position principale, c'est-à-dire la
  lecture de « au champ du coût » dans le GO. Ce sont des « couches et concepts de sondes » : à proposer avec recommandation
  (CLAUDE.md, hiérarchie de décision), et non de la routine. Q-05 est bien classée, mais le texte pose le choix sans
  marqueur et sans ligne au registre.
- Correction (mots exacts) : Q-04, Q-06, Q-07 : « (proposer avec recommandation ; défaut sous 48 heures : la
  recommandation) ». Dans le texte, à la fin de l. 161 : « **[Proposition en attente : P-0xx (Q-04 à Q-07) ; défaut : ce
  texte, le <date d'envoi + 48 h> UTC]** ». Consigner P-0xx.

### CR-P3b-texte-15 — mineur — Le validateur ne voit pas les marqueurs d'attente

- Où : l. 68 (partition), et le marqueur proposé en CR-P3b-texte-01 ; `prereg.py` l. 26-27 (seuls « À REMPLIR » et `<<…>>`).
- Ce qui est : `problemes` ne détecte ni « Décision de Lazar en attente » ni « Version de repli (B) ». Un texte pourrait donc
  être scellé avec les deux partitions.
- Correction (mots exacts) : l. 68-71 : remplacer la version (A) écrite en clair par « Partition : `<<PARTITION_P016>>` » (rempli
  au candidat par le seul texte de la version retenue), et ajouter au plan (`sceller_p3b_v1.sh`) : « refuse tout texte qui
  contient « en attente », « Version de repli » ou « Proposition en attente » ».

### CR-P3b-texte-16 — mineur — Sondes non principales dans la garde (e) : préciser qu'aucune n'est lue

- Où : H-P3b-0 (l. 108-109) ; « Métrique », garde (e) (l. 170-171) ; hors périmètre (l. 83).
- Ce qui est : P3 interdit toute seconde lecture sur les autres sondes (P3 l. 428, l. 436). Le texte utilise leurs scores
  pour une garde sans le dire, et le compte « 24 » n'a pas de source.
- Correction (mots exacts) : après « (e) scores par action des 424 sondes légères, même écart relatif ≤ 10⁻³ », insérer
  « (24 sondes non Mahalanobis sur 30, P3 l. 303-304 et l. 312-316, et les 400 sondes des planchers) : garde de
  reconstitution seulement ; aucune aire, aucun jeu, aucune lecture des sondes non principales (P3 l. 428, l. 436) ».

### CR-P3b-texte-17 — mineur — Liste d'arrêt incomplète face au texte et au plan

- Où : « Liste d'arrêt » (l. 425-453) ; hypothèse de travail (4) (l. 134-136) ; plan (`p3b_constantes_v1.py`, `oracle_p3b_v1.py`).
- Ce qui est : (a) l'hypothèse de travail (4) nomme une « garde » sur le tokeniseur sans dire ce qui arrive en cas d'échec
  (R5 : aucun repli silencieux) ; (b) le plan arrête sur une constante différente de la configuration et sur une mention
  injectée dans l'apprentissage de l'oracle, mais le texte ne le dit pas ; (c) « empreinte du modèle et du tokeniseur autre
  que celle consignée » : le texte ne dit pas où elle est consignée ; (d) la garde de mémoire vive de P3 (P3 l. 455) n'est
  pas reprise.
- Correction (mots exacts) : ajouter à la liste d'arrêt : « Tokeniseur figé où un nombre de 0 à 999 n'est pas un seul jeton :
  consigné, aucune règle ne change (t_cost n'en dépend pas), compte rapporté. » ; « Constante d'un module de P3b
  différente de la configuration scellée : aucune création, ou arrêt de la passe. » ; « Action de la mention, ou action du
  saboteur non étiquetée 1 par T1, dans un apprentissage de l'oracle : oracle en échec, motif écrit. » ; « Modèle et
  tokeniseur : empreintes du manifeste du run source de P3 (`<<SHA_MODELE_P3>>`), relues par code. » ; « Mémoire vive sous
  le minimum (garde `exiger_memoire_vive` de P3) : arrêt consigné. »

### CR-P3b-texte-18 — mineur — Ordre de la chaîne : le texte et le plan diffèrent

- Où : « Chaîne de lancement », Ordre (l. 461-465) ; plan § 4 (l. 62-69).
- Ce qui est : le plan prévoit une vérification neuve du code, une relecture courte du candidat et un temps pour les
  décisions en attente. Le texte n'en a aucun.
- Correction (mots exacts) : l. 461-462 : « **Ordre** : contre-lecture R2 de ce brouillon, du devis et du plan ; traitement ;
  décisions en attente (P-016, N-0xx statut, Q-03, P-0xx) ; code et tests (rédacteur neuf), puis vérification neuve du code ;
  mesures de conception (puissance ; comptes de tokenisation, sur nœud) ; candidat, puis relecture courte par un sous-agent
  neuf ; répétition jouet ; … » (suite inchangée).

### CR-P3b-texte-19 — mineur — Tableau hors périmètre : quatre précisions

- Où : l. 78, l. 81, l. 85, l. 86.
- Ce qui est : (a) le texte écrit « partition (B) alors » pour P-016 (B) comme pour (C) ; or P-016 ne lie la partition
  20/20/20 qu'à (B). (b) La ligne « référence boîte noire » ne dit pas que N-029 l'a tranchée : la comparaison se lit sur les
  épisodes de T0.6 et « ne se lit pas sur les textes de P3 » (`decision-N-029-v1.md` l. 37-39). (c) « lentille ajustée »
  peut se confondre avec la lentille jacobienne réajustée. (d) Une lentille jacobienne réajustée plus tard ne pourrait plus
  être gelée par ce texte, une fois scellé.
- Correction (mots exacts) : (a) l. 78, dernière colonne : « P-016 (B) (partition 20/20/20) ou (C) (partition à fixer avec
  elle) ». (b) l. 81 : « | référence boîte noire | N-029 tranché (c) renforcée (`docs/decisions/decision-N-029-v1.md`,
  `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4`, section 2) : comparaison sur les épisodes de T0.6,
  « elle ne se lit pas sur les textes de P3 » | nouvelle décision de Lazar qui modifie N-029 | ». (c) l. 85 : « lentille
  apprise (« tuned lens »), distincte de la lentille jacobienne ». (d) l. 86, dernière colonne : « préenregistrement
  complémentaire et devis séparé (délégation) ».

### CR-P3b-texte-20 — mineur — Provenance : état de l'art par transcription ; pièces du bloc-notes appelées à faire foi

- Où : hypothèse de travail (4) (l. 134-136) ; lentille jacobienne (l. 256) ; en-tête (l. 5-6, l. 49-59) ; « Chaîne de
  lancement » (l. 457).
- Ce qui est : la ligne 140 dit « Aucun chiffre de l'état de l'art n'entre ici ». Pourtant les l. 134-135 citent « nombres de
  0 à 999 un seul jeton [KT p. 2, d'après la réponse au prompt unique] » : c'est une provenance par transcription (R7). De
  plus, les pièces sous `…/` vivent dans le bloc-notes d'une session (`/tmp`) et ne survivent pas à la session. Le modèle
  de la chaîne (chaîne v2 de P4) n'est que là : `R/docs/procedures/` n'a pas de dossier P4.
- Correction (mots exacts) : l. 134-136 : « (4) la règle de t_cost ne suppose pas qu'un nombre de 0 à 999 soit un seul
  jeton ; le compte est mesuré par code sur le tokeniseur figé et rapporté » (retirer « [KT p. 2, d'après la réponse au
  prompt unique] »). l. 256 : donner le PDF de [JL] par chemin du dépôt, empreinte et page, ou retirer la référence. En
  en-tête, ajouter : « Au candidat, chaque pièce citée sous `…/` est versée au dépôt (chemin et empreinte) ou citée par
  branche et empreinte ; sinon retirée ; en premier, la chaîne v2 de P4. »

### CR-P3b-texte-21 — forme — Horodatages des quatre fichiers

- Où : brouillon l. 3 ; devis l. 3 ; plan l. 3 ; questions l. 3.
- Ce qui est : « session 14, vers 23:30 UTC », puis devis « vers 23:45 », plan « vers 23:50 », questions « vers 23:55 ». Or les
  fichiers datent de 23:37 à 23:39 UTC. La session 14 s'est arrêtée vers 23:00 (`registres/etat.md` l. 3, R-304) ; R-305
  date de la session 16, vers 23:10.
- Correction (mots exacts) : brouillon l. 3 : « **brouillon 1**, lancé par la session 14 (consigne de 22:50 UTC), fichiers
  écrits vers 23:37-23:39 UTC » ; devis, plan, questions : « vers 23:37 », « vers 23:38 », « vers 23:39 UTC ».

### CR-P3b-texte-22 — mineur — Définitions manquantes et formulations dans les métriques et les tables gelées

- Où : l. 253-254 ; tables G (l. 375-385) et O (l. 392) ; P3b-P3 (l. 149) ; H-P3b-1 (l. 111-112) ; plan, point 2.2
  (l. 302) ; réserves (l. 421-422).
- Ce qui est et correction (mots exacts) :
  - (a) l. 254, « g/3 » : g n'est pas défini. Écrire : « …avec le coût écrit divisé par 3 (facteur de la consigne) au lieu
    de H_t ».
  - (b) l. 253, « τ_w (premier jeton écrit) ». Écrire : « τ_w (identifiant du jeton f, premier chiffre écrit du champ) ».
  - (c) Le mot « retenue » n'est pas défini dans P3b. Ajouter avant la table G : « Une sonde est **retenue** si son jeu
    saboteur contre honnête sur W est au-dessus et interprétable. »
  - (d) O2 (l. 392) et P3b-P3 (l. 149) disent : « même un lecteur appris sur l'organisme n'est pas détecté ». Écrire :
    « même avec un lecteur appris sur l'organisme, saboteur non détecté à t_cost à cette puissance ».
  - (e) H-P3b-1, l. 111-112 : remplacer « (du premier jeton de la clé `COST` au jeton qui précède le premier chiffre,
    16 jetons au plus) » par « (les 16 derniers jetons au plus de [c, t_cost], W défini en « Métrique ») ».
  - (f) Au point 2.2 du plan d'analyse, la garde d'identité de la lentille vient avant toute passe, alors qu'elle se définit
    sur des actions. Écrire : « garde d'identité de la lentille sur les items du contrôle positif (étape 3), puis sur les
    actions de P3 (étape 8) ».
  - (g) La réserve « parts d'exclues différentes… de plus de 2 points » ne dit pas quelles exclusions elle compte. Écrire :
    « …de plus de 2 points, pour chaque motif (reconstitution ; position) ».

### CR-P3b-texte-23 — information — Constats « à transmettre », vérifiés un par un

- VV4-sens-04 : sans objet dans ce brouillon (la question ajoutée est hors périmètre, l. 80). Si elle s'ouvre un jour, ses
  chiffres de [PAR] demandent le PDF et la page (R7).
- VV4-sens-06 : conforme. Le bras « avant le champ » lit les actions générées de P3. Le contrôle positif de la lentille, sur
  une réponse imposée, éprouve la lentille ; ce n'est pas un jeu « avant le champ » entre conditions.
- VV4-sens-11 : non traité dans le texte ; voir CR-P3b-texte-09.
- VV4-sens-12 : T1, T3 et P3-P4 aux positions neuves ne sont pas déclarés neufs (CR-P3b-texte-09). Aucun « T4 avant le
  champ » ni aucune règle « non calculable faute de recouvrement » n'est caché dans le texte : la part de recouvrement est
  rapportée sans règle (l. 357-358).

### CR-P3b-texte-24 — information — Hors de ma lentille, pour la lentille « méthode » et la session

- Le signe de P3-P2 (témoin et mention contre honnête) est consigné à l'addendum 2 (`prereg/P3-addendum2-audit-verdict-v1.md`,
  `c91a3b4e600bca029f77fbd8ecea12fe9d9658da26219ddcbf3d95102f02ddb6`, l. 126) et repris au verdict complété. Il touche
  Q-06 (le témoin parmi les négatifs de l'oracle), T3 (mention contre honnête) et T4 résiduel. Le rédacteur, aveugle, ne
  pouvait pas le connaître. C'est à la session de décider si le rédacteur du brouillon 2 doit le voir : cela changerait son
  exposition. Je ne recopie pas la valeur.

### CR-P3b-texte-25 — information — Ce qui est conforme

- Toutes les empreintes citées que j'ai pu vérifier sont exactes. Cela comprend : P3 (`d975e981…`), configuration canonique
  (`2f343a6f…`, égale à P3 l. 39), tâches (`287e8348…`, égale à P3 l. 40), consignes (`a68468fe…`, égale à P3 l. 65),
  gabarit, validateur, N-026, les deux registres, la proposition 010, huit modules au commit `7a54d43`.
- Les lignes de P3 citées par le texte et le devis sont exactes (l. 238-248, 352-358, 382-385, 394-397, 428, 436).
- Le marqueur de P-016 a la forme demandée par la consigne du rédacteur, avec la version de repli (B).
- La liste « hors périmètre » est conforme à N-028, à GO-2026-10-20-05 et -10, et à R-289 (bras « moyenne », sous les
  conditions 1 à 4 de N-026) ; elle ajoute P-017 (B) et (C) avec le bon défaut et la bonne échéance.
- Le bras « moyenne » est absent : π_b moyenne sur les actions et les couches, jamais sur les jetons d'une action, et le
  texte le dit.
- Devis : borne 7,14 USD arrondie à 7,5 USD (5,20 + 0,22 + 1,00 + 0,72) ; crédit 4,5 × 1,30 + 1,2 = 7,05 USD ; marge de
  25 minutes entre la surveillance (240 minutes) et l'arrêt forcé de l'amorce (210 + 5 minutes) ; total d'heures cohérent
  avec la somme des postes.
- La sortie de `problemes` est attendue pour un brouillon. `<<SHA_LENTILLE_J>>` doit disparaître avec le bras s'il est
  retiré ; pour `<<LIGNE_VERDICT_P4>>`, voir CR-P3b-texte-05.

## Avis sur les questions ouvertes qui relèvent de ma lentille

- **Q-01** : d'accord, c'est un nœud. Il faut le consigner (N-0xx) et le marquer dans le texte (CR-P3b-texte-01). Mon avis :
  (a), le diagnostic, car les bras localisés ne sont pas aveugles. Le texte doit alors dire que R-262 (point 2) n'est pas
  rempli par P3b. Confiance ≈ 60 %.
- **Q-02** : d'accord pour (A) avec repli (B). Le marqueur doit devenir lisible par le validateur (CR-P3b-texte-15).
- **Q-03** : c'est un nœud, pas de la routine (R1, CR-P3b-texte-08). Si Lazar l'admet : un seul compte, toutes conditions
  confondues.
- **Q-04** : à proposer avec recommandation, car c'est la lecture du GO « au champ du coût ». Sur le fond, je n'ai pas
  d'objection à W.
- **Q-05** : classement juste ; il faut un marqueur et une ligne au registre (CR-P3b-texte-14).
- **Q-06, Q-07** : à proposer avec recommandation (concept de sonde), pas de la routine. Le fond relève de la lentille
  « méthode » ; voir CR-P3b-texte-24.
- **Q-09** : routine, d'accord, à condition de citer le module repris de P4 par chemin et empreinte, et de le verser au dépôt.
- **Q-10** : d'accord : lire les données sur la branche, à leurs empreintes, sans nouvelle copie des textes d'action.
- **Q-11** : je recommande la suite complète sur l'instance, comme dans P3 (≈ 0,35 h de plus, ≈ 0,4 USD, dans la borne). Elle
  éprouve l'arbre gelé dans l'environnement réel. Si le sous-ensemble est retenu, écrire l'écart à P3 dans le texte.
- **Q-12** : d'accord, à recaler avant le candidat. Le devis doit citer ses sources par chemin et empreinte (CR-P3b-texte-12).
- **Q-18** : routine, d'accord. Écrire la licence du fichier avec son empreinte. Une licence restrictive devient un nœud.
- **Q-20** : le motif doit être écrit dans le texte, comme un choix neuf (CR-P3b-texte-09).
- **Q-21** : d'accord, c'est un nœud, et la destruction est un bon défaut. La garde après un refus de poussée doit être bornée
  (CR-P3b-texte-10).
- **Q-22** : le cas « P4 absent » doit être écrit dans la table gelée, pas seulement en question (CR-P3b-texte-05).
- **Q-23** : d'accord. Ajouter `<<SHA_MODULES_P3B>>`, `<<TESTS_P3B>>`, `<<SHA_MODELE_P3>>` et `<<PARTITION_P016>>`
  (CR-P3b-texte-07, -15, -17).
- **Q-24** : routine acceptable, mais le choix doit être écrit dans le texte (il l'est, l. 160-161). D'accord sur la
  confirmation seule en lecture principale.
- Q-08 et Q-13 à Q-17, Q-19 : relèvent de la lentille « méthode » ; pas d'avis ici.

## Compte des constats

Critique 0 ; majeur 7 (01, 02, 03, 05, 06, 07, 08) ; mineur 14 (04, 09 à 20, 22) ; forme 1 (21) ; information 3 (23, 24, 25).

# Liste « qui a lu quoi » du programme — version 1, brouillon 1

- **Objet** : liste exigée avant la remise de la commande d'ouverture de P3-bis au compte 2 (R-2683 ; commande
  `docs/procedures/P3-bis-commande-compte-2-v1/commande-ouverture-verdict-p3bis-compte-2-v1.md`, `e9974afe…`, l. 47-48 et
  123-124 : « tableau Markdown dont l'en-tête porte deux cellules exactement « session » et « compte », une ligne par lecture
  déclarée »). Elle sert à l'attestation par programme du bloc 5 (`controle_a_blanc_compte_2_v1.py`, `1a9dce71…`, fonction
  `attester`) : ni la session hôte du compte 2 ni le compte 2 n'y figurent.
- **Règle de Lazar** (recopiée de la consigne de la mère du 2026-11-14 ; aucune ligne R ne la porte mot pour mot dans
  `registres/decisions.md` d'après les recherches de ce brouillon : réserve, la mère cite sa source) : « la session-dépôt est
  exclue des rôles de lecteur et de verdict sur T0.6 (7b), T0.7, P3-bis et G0 ; tout agent qui lit T0.7 est ensuite exclu des
  lecteurs de P3-bis ». Forme voisine au registre : R-2200 (« tout agent qui lit T0.7 est exclu ensuite des lecteurs de
  P3-bis ») ; R-2598 (« ce compte héberge ensuite le lecteur du verdict de P3-bis, donc aucune de ses sessions ne lit T0.7 »).
- **Date** : 2026-11-14, écrit de 09:33Z à 09:45Z (heures relevées par `date -u`).
- **Rédacteur** : sous-agent neuf de la session mère (ligne 4 du tableau), modèle A ; lecture seule, ce seul fichier écrit.
- **Méthode** : recherches par mots dans `registres/decisions.md` (« qui a lu », « lu T0.7 », « lecteur de T0.7 », « exclu »,
  « session_ », « session-dépôt », « fille », « lecture A / B de 7a », « 7b ») ; lecture des seuls en-têtes (lignes d'auteur ou
  de lecteur) des contre-lectures de T0.7 sous `prereg/contre-lectures/` et de l'en-tête d'auteur de la procédure du
  rendez-vous ; journaux provisoires des comptes 2 et 4 lus par `git show REF:CHEMIN` sur `refs/remotes/origin/lot/compte-2-v1`
  (tête `1965ea9b`) et `refs/remotes/origin/lot/compte-4-v1` (tête `5a9e456e`), compagnons comparés. Aucun texte de T0.7, aucune
  sortie de 7a, 7b ou T0.7, aucun paquet, aucune pièce du bras d'attaque ni du mode tenu à l'écart n'a été ouvert. Modèles
  notés « modèle A » ou « modèle B » (R-2598) ; « non déclaré » quand aucune source ne le dit. Une ligne sans source n'est pas
  écrite ; « session non nommée » quand la source ne donne pas l'identité.
- **Sources** : `registres/decisions.md` (`9014318006264b74d3bd1e63fc4a72d24609bab5533c2f802061416d8148002d`, à 09:39Z) ;
  journaux du compte 4 `registres-provisoires/compte-4-2026-11-13-v5.md` (`9ef2d7e7…`), `…-v7.md` (`52a40db9…`),
  `passation-compte-4-2026-11-14-0655.md` (`a4abc0f8…`) ; journaux du compte 2 `etat-compte-2-2026-11-14-0141.md`
  (`f20fe806…`), `compte-2-2026-11-13-C2-0002.md` (`e88babee…`) ; en-têtes des contre-lectures citées par ligne (empreintes
  égales à leurs compagnons) ; `docs/procedures/brief-successeur-session-depot-2026-11-10-v1.md` (`b5e22583…`).

## Constat sur le compte 2 (non bloquant)

Aucune pièce ne prouve une lecture de T0.7, de la procédure du rendez-vous, des sorties de 7a ou 7b, ni d'un paquet de P3-bis
par une session ou un sous-agent du compte 2 : `etat-compte-2-2026-11-14-0141.md` l. 11 (« Aucune session ni aucun sous-agent
du compte 2 n'a ouvert T0.7, l'ordre de l'étape A, la procédure du rendez-vous de P3-bis, ni rien de 7a ou 7b ») ; rappel de
la mère reçu (`C2-0002` l. 13) ; aucune autre mention de lecture de T0.7 ou de P3-bis dans les journaux de la branche (écart
de recherche déclaré en C2-0022 : synthèse de niveau 3, programme v2, décision N-005, hors de T0.7 et de P3-bis). Le compte 2
ne figure donc dans aucune ligne.

## Tableau

| n° | session | compte | modèle | a lu | rôle | source | exclu de |
|---|---|---|---|---|---|---|---|
| 1 | session_01QPDgKgACWyCkCN8HjqwNXy (session mère) | compte mère, reprise le 2026-11-13 | non déclaré | autre : registres ; ligne SCELLEMENT-T07 et commit S7 du texte scellé vérifiés pour remplir l'ordre de l'étape A ; aucune sortie de T0.7 lue ; aucun paquet ouvert | mère : orchestration, ordre de l'étape A de T0.7, commande de P3-bis | R-2552, R-2566, R-2637 (« la mère n'a lu aucune sortie »), R-2673 (« la mère n'ouvre rien ») | ouverture du paquet et lecture du verdict de P3-bis (R-2673) |
| 2 | sous-agent de session_01QPDgKgACWyCkCN8HjqwNXy (rédacteur de la commande, 2026-11-14, 08:34Z à 09:30Z) | compte mère | modèle A | procédure de P3-bis (procédure du rendez-vous, sections 4 à 6), texte scellé de P3-bis, module de S ; T0.7 haché seulement, jamais ouvert ; deux compagnons de la branche de l'étape A | rédacteur de la commande d'ouverture de P3-bis | R-2683 ; commande `e9974afe…` l. 9-13 et 29-32 | lecteur et auteur du verdict de P3-bis (commande l. 10) |
| 3 | sous-agent de session_01QPDgKgACWyCkCN8HjqwNXy (rédacteur de la procédure du rendez-vous, 2026-11-13, 18:00Z à 18:39Z) | compte mère | modèle A | procédure de P3-bis (auteur) et consigne du lecteur du verdict (auteur) ; aucune pièce de T0.7 écrite | rédacteur | R-2561 ; en-tête de `docs/procedures/P3-bis-rendez-vous-et-verdict-v1.md` (`ba044b78…`) l. 1-3 | lecteur et auteur du verdict de P3-bis (en-tête) |
| 4 | sous-agent de session_01QPDgKgACWyCkCN8HjqwNXy (rédacteur de cette liste, 2026-11-14, 09:33Z à 09:45Z) | compte mère | modèle A | autre : registre des décisions par recherche, journaux des comptes 2 et 4, en-têtes des contre-lectures de T0.7, en-tête d'auteur de la procédure du rendez-vous, commande et script d'attestation ; ni T0.7 ni sortie ni paquet | rédacteur du brouillon 1 de cette liste | cette pièce, en-tête (méthode) | lecteur du verdict de P3-bis (par prudence : en-tête de la procédure lu) |
| 5 | sous-agent de session_01QPDgKgACWyCkCN8HjqwNXy, daté du 2026-11-10 (contre-lecteur 1 du brouillon 20 de T0.7) | compte de la mère du 2026-11-10, non numéroté | modèle B | autre : T0.7, brouillon 20 (différentiel 19 vers 20), et module de T0.7 | contre-lecteur | `prereg/contre-lectures/T0.7-sondes-v0-v1-brouillon20-cl1.md` (`a64065c07750…`) l. 3 ; même identifiant de mère le 2026-11-10 dans `brief-successeur-session-depot-2026-11-10-v1.md` l. 24 | tout rôle de lecteur de P3-bis (en-tête) |
| 6 | session_01QPDgKf6Rn3eTeuYMDCBiKA (fille de l'étape A de T0.7) | compte mère (fille créée par la mère, environnement « controle-ia ») | non déclaré | autre : ordre d'exécution de l'étape A de T0.7 (`9b3a04da…`, puis v2 `afac6e7c…`) ; sorties de T0.7 produites en exécutante (lecture non déclarée au registre) | fille exécutante de l'étape A de T0.7 | R-2566, R-2582, R-2588, R-2618, R-2637 | lecteur et hôte du verdict de P3-bis (règle de Lazar) |
| 7 | session_01Qi7Gr2uGzyVcw9VmDXgvEV (session du compte 4) | compte 4 | modèle A | T0.7 scellé, en partie : lignes 1 à 12 et lignes trouvées par mots (« 200 directions », « CODE-T07 », ligne 695) | session du compte 4 | `registres-provisoires/compte-4-2026-11-13-v5.md` (`9ef2d7e7…`) C4-0003 ; `passation-compte-4-2026-11-14-0655.md` (`a4abc0f8…`) l. 3 et 23 | tout rôle de lecteur ou d'hôte du verdict de P3-bis ; verdicts de l'étape B, de T0.8, du contrôle de l'adaptateur et du barreau 6 (C4-0003) |
| 8 | session_01Qi7Gr2uGzyVcw9VmDXgvEV (session du compte 4) | compte 4 | modèle A | autre : texte scellé de P3-bis (`76ab66ce…`) et ses trois addenda, par recherche ciblée et quelques passages entiers | session du compte 4 | `registres-provisoires/compte-4-2026-11-13-v7.md` (`52a40db9…`) C4-0016 ; R-2605 | comme la ligne 7 |
| 9 | sous-agent de session_01Qi7Gr2uGzyVcw9VmDXgvEV (contre-lecteur 2, lancé à 2026-11-13T21:01:40Z) | compte 4 | modèle B | T0.7 scellé et module de T0.7 sur main | contre-lecteur 2 (validité de l'adaptateur) | `compte-4-2026-11-13-v5.md` (`9ef2d7e7…`) C4-0003 | comme la ligne 7 |
| 10 | sous-agent de session_01Qi7Gr2uGzyVcw9VmDXgvEV (vérificateur de C4-0011) | compte 4 | modèle B | T0.7 scellé, par lignes citées | vérificateur | `compte-4-2026-11-13-v5.md` (`9ef2d7e7…`) C4-0012 ; R-2597 | comme la ligne 7 |
| 11 | session_01VJdZpSMxSdk2SJ1ScmdfNv (mère au scellement de T0.7, à confirmer) | compte d'une mère antérieure, non numéroté | non déclaré | T0.7 scellé : texte final (candidat 5) avec le marqueur C7 rempli, contrôlé par programme, scellé | mère : scellement de T0.7 | R-2321 (session non nommée dans la ligne) ; identité tirée des en-têtes des vérifications des candidats 4 et 5 (`26efc4df…`, `84ffcb01…`) et de R-2445 | lecteur et hôte du verdict de P3-bis (règle de Lazar) |
| 12 | sous-agent de session_01VJdZpSMxSdk2SJ1ScmdfNv (vérificateur du candidat 1) | compte d'une mère antérieure, non numéroté | modèle B | autre : T0.7, candidat 1 | vérificateur | `prereg/contre-lectures/T0.7-sondes-v0-v1-candidat1-verification-courte-v1.md` (`ef3431a1a45c…`) l. 1-2 | tout rôle de lecteur de P3-bis (en-tête) |
| 13 | sous-agent de session_01VJdZpSMxSdk2SJ1ScmdfNv (vérificateur du candidat 3) | compte d'une mère antérieure, non numéroté | modèle B | autre : T0.7, candidat 3 | vérificateur | `T0.7-sondes-v0-v1-candidat3-verification-courte-v1.md` (`cfeeae9c0a34…`) l. 1-2 | tout rôle de lecteur de P3-bis (en-tête) |
| 14 | sous-agent de session_01VJdZpSMxSdk2SJ1ScmdfNv (vérificateur du candidat 4) | compte d'une mère antérieure, non numéroté | modèle B | autre : T0.7, candidat 4 | vérificateur final | `T0.7-sondes-v0-v1-candidat4-verification-finale-v1.md` (`26efc4dfb492…`) en-tête | lecteur de P3-bis (règle de Lazar) |
| 15 | sous-agent de session_01VJdZpSMxSdk2SJ1ScmdfNv (vérificateur du candidat 5) | compte d'une mère antérieure, non numéroté | modèle B | autre : T0.7, candidat 5 (devenu le texte scellé) | vérificateur mécanique | `T0.7-sondes-v0-v1-candidat5-verification-mecanique-v1.md` (`84ffcb017588…`) en-tête | lecteur de P3-bis (en-tête) |
| 16 | sous-agent de session_01VJdZpSMxSdk2SJ1ScmdfNv (contre-lecteur 2 de la consigne de l'audit des fuites, brouillon 5) | compte d'une mère antérieure, non numéroté | modèle B | autre : T0.7 et consigne de l'audit des fuites de T0.7 | contre-lecteur | `T0.7-consigne-audit-fuites-v1-brouillon5-cl2.md` (`c9035156f36d…`) l. 3-5 | tout rôle de lecteur de P3-bis et d'auditeur de l'audit des fuites (en-tête) |
| 17 | session non nommée (sous-agent de la mère, 2026-11-10 ; contre-lecteur 1 de la consigne de l'audit des fuites, brouillon 2) | non déclaré | modèle B | autre : T0.7 et consigne de l'audit des fuites de T0.7 | contre-lecteur | `T0.7-consigne-audit-fuites-v1-brouillon2-cl1.md` (`02b9d8b5cb4d…`) l. 3-5 | tout rôle de lecteur de P3-bis et d'auditeur de l'audit (en-tête) |
| 18 | session non nommée (sous-agents de la mère, 2026-11-10 : quatre contre-lecteurs, vérificateurs contradictoires, rédacteur du rapport) | non déclaré | modèle B | autre : T0.7, brouillon 22 | contre-lecture orchestrée | `T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md` (`47537dfa7d4f…`) l. 7-9 ; R-2200 | lecteurs de P3-bis (R-2200) |
| 19 | sous-agent de session_016QhUrrLeN21G7Z9KZobE42 (contre-lecteur 3, brouillon 9, 2026-11-08) | compte d'une mère antérieure, non numéroté | modèle A | autre : T0.7, brouillon 9 | contre-lecteur | `T0.7-sondes-v0-v1-brouillon9-cl3.md` (`cd0e61a76760…`) en-tête | lecteur de P3-bis (règle de Lazar) |
| 20 | sous-agent de session_016QhUrrLeN21G7Z9KZobE42 (contre-lecteur 4, brouillon 10, 2026-11-08) | compte d'une mère antérieure, non numéroté | modèle B | autre : T0.7, brouillon 10 | contre-lecteur | `T0.7-sondes-v0-v1-brouillon10-cl4.md` (`f2780572b557…`) en-tête | lecteur de P3-bis (règle de Lazar) |
| 21 | session non nommée (sous-agent de la mère, 2026-11-08 ; contre-lecteur 1, brouillon 6) | non déclaré | modèle A | autre : T0.7, brouillon 6 | contre-lecteur | `T0.7-sondes-v0-v1-brouillon6-cl1.md` (`3d4f75f07461…`) en-tête | lecteur de P3-bis (règle de Lazar) |
| 22 | session non nommée (sous-agent de la mère, 2026-11-08 ; contre-lecteur 2, brouillon 7) | non déclaré | modèle A | autre : T0.7, brouillon 7 | contre-lecteur | `T0.7-sondes-v0-v1-brouillon7-cl2.md` (`d2fd4222dc17…`) en-tête | lecteur de P3-bis (règle de Lazar) |
| 23 | session non nommée (sous-agent, 2026-11-09 ; contre-lecteur 1 du brouillon 15, puis contre-lecteur 2 du brouillon 16, même agent) | non déclaré | modèle B | autre : T0.7, brouillons 15 et 16 | contre-lecteur | `T0.7-sondes-v0-v1-brouillon15-cl1.md` (`29203bbcc20e…`) et `T0.7-sondes-v0-v1-brouillon16-cl2.md` (`fc728c185730…`) en-têtes | lecteur de P3-bis (règle de Lazar) |
| 24 | session non nommée (rédacteurs des brouillons et des candidats de T0.7) | non déclaré | modèle A | autre : T0.7, brouillons et candidats (auteurs) | rédacteurs de T0.7 | en-tête de `T0.7-sondes-v0-v1-brouillon22-cl-orchestree-v1.md` (`47537dfa…`) l. 7 et R-2241 ; en-tête de la vérification du candidat 4 (`26efc4df…`) | lecteur de P3-bis (règle de Lazar) |
| 25 | session non nommée (sous-agents développeurs du module de T0.7, dont de session_01VJdZpSMxSdk2SJ1ScmdfNv) | non déclaré | modèle A | autre : T0.7 (développeurs du code qu'il nomme) | développeurs du module de T0.7 | `compte-4-2026-11-13-v5.md` (`9ef2d7e7…`) l. 72 ; en-tête de la vérification du candidat 4 (`26efc4df…`) | lecteur de P3-bis (règle de Lazar) |
| 26 | session non nommée (agent neuf du brouillon 4 de la consigne de l'audit des fuites de T0.7) | non déclaré | non déclaré | autre : T0.7 scellé (marqueur rempli par programme sur le texte scellé) | rédacteur | R-2346 | lecteurs de P3-bis ; auditeur et contre-lecteur de l'audit (R-2346) |
| 27 | session non nommée (agent neuf de l'essai de concordance du journal des ouvertures, v1) | non déclaré | non déclaré | autre : code du lecteur de T0.7 et de l'écrivain de P3-bis, journal des ouvertures | essai de concordance | R-2103 | tout rôle de lecteur de P3-bis (R-2103) |
| 28 | session non nommée (agent neuf du préalable P-9, concordance v2) | non déclaré | modèle A | autre : code du lecteur de T0.7 (C7) et de l'écrivain de P3-bis, journal des ouvertures | préalable P-9 de P3-bis | R-2349 | lecteurs de P3-bis (R-2349) |
| 29 | session non nommée (lecteur neuf de la lecture A de 7a, 2026-11-09 ; mère du moment : session_016QhUru7Vvg7CW6qkp1yrcG, R-2037) | non déclaré | non déclaré | sorties de 7a (lecture A exploratoire, non opposable) | lecteur A de 7a | R-2040 (`docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md`, `3c84c419…`, non ouvert) | non précisé par R-2040 : à trancher par la mère |
| 30 | session non nommée (lecteur neuf de la lecture B de 7a, 2026-11-09 ; mère du moment : session_016QhUru7Vvg7CW6qkp1yrcG, R-2037) | non déclaré | non déclaré | sorties de 7a, dont des valeurs du fichier de lecture des sondes de T0.6 (écart DT-4) | lecteur B de 7a | R-2041 | tout rôle sur T0.6, T0.7, P3-bis et G0 (R-2041) |
| 31 | session_01QPDgKgcLdggoVJfGC5cBw8 (session-dépôt jusqu'au 2026-11-10) | non déclaré | non déclaré | autre : aucune lecture de T0.7, de 7a, de 7b ni de P3-bis déclarée au registre | session-dépôt | R-2126, R-2179, R-2190 | rôles de lecteur et de verdict sur T0.6 (7b), T0.7, P3-bis et G0 (règle de Lazar) |
| 32 | session_013QMaymMAdDjNfPoz8ySwTc (session-dépôt, successeur) | non déclaré | non déclaré | autre : dépôt chez le tiers de 174 fichiers de prereg/, docs/verdicts/, docs/decisions/ « lus sur main f562e9fb », après le scellement de T0.7 (texte de T0.7 vraisemblablement compris, non vérifié) ; « mesure unanime » versée en quarantaine | session-dépôt | R-2157, R-2200, R-2283, R-2384 | rôles de lecteur et de verdict sur T0.6 (7b), T0.7, P3-bis et G0 (règle de Lazar) |

## Réserves de ce brouillon

1. **Identifiant de la mère** : `session_01QPDgKgACWyCkCN8HjqwNXy` est nommée mère le 2026-11-10 (ligne 5 ; brief du successeur
   de la session-dépôt, l. 24) puis « session mère neuve, autre compte » le 2026-11-13 (R-2552). Les deux ne se concilient pas
   sur pièce ; sans effet sur l'attestation du compte 2, mais la ligne 1 hérite peut-être des lectures de la ligne 5.
2. **Ligne 11** : R-2321 ne nomme pas la session ; l'identité est déduite des en-têtes des vérifications voisines. À confirmer.
3. **Couverture incomplète** (à compléter au brouillon 2) : auteurs et contre-lecteurs de P3-bis (texte, code, chaîne :
   R-2076, R-2097, R-2099, R-2340…) ; filles des courses de P3-bis (`session_013QMayo3Je79e17xB1yHiDw`,
   `session_01XJ6MgndxPY844vwbKNNGHu`) et de 7b (`session_013QMayk2G3jAYKq1b9m7bma`), qui ont produit des sorties sans lecture
   déclarée (R-2413 : « sorties non ouvertes ») ; fille de la course 7a (« fille clés 2 », session non nommée) ; rédacteur du
   brouillon 2 de la consigne de l'audit des fuites (R-2194) ; comptes 3, 5 et « compte organisme », non examinés ;
   contre-lecteur modèle B de la commande, pas encore lancé (R-2683).
4. **Modèles « non déclaré »** : hors des deux valeurs demandées ; aucune source lue ne donne le modèle.
5. Les lignes agrégées (18, 23, 24, 25) regroupent plusieurs agents d'une même pièce ; la commande demande « une ligne par
   lecture déclarée » : à éclater si la mère le veut.

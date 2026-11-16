# Phase C v4 du compte 3 — pièces de la remise préparées pour la mère — v1

- **Statut** : pièce de préparation, pour la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`, qui décide et remet ; **rien n'est remis
  ni envoyé**. Suit `preparation-phase-c-v3-mere-v1.md` (`31bfacd5…`), § 1.5 à 1.10, transposée à la commande en vigueur :
  `commande-compte-3-phase-c-v4.md` (`f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755`, R-2991), consigne
  `consigne-lecteur-b-v1.md` (`1fa37cbc984beb977c418e81c838131f848ceb46b053c6e2e01b077f99e4d8ae`).
- **Rédacteur** : exécutant de la section 15 de la commande phase B v3, sous-agent de la session mère (modèle A), ligne 185 de la liste v3 ;
  écrit le 2026-11-16 à partir de 21:13Z (`date -u`). Aucune sortie de 7a, 7b, T0.7 ni de P3-bis ouverte ; de 7b, seuls le booléen de
  l'audit R4 de la base (A) et l'état de BA-L2 lus par programme ; aucun texte de T0.7 ni de l'étape B bis.

## 1. Fait (sur `main`, poussé)

| préalable | état | preuve |
|---|---|---|
| bloc V | 8 fichiers égaux à leurs compagnons et au rendu de l'hôte | R-3019 (2) |
| `LECTURE-T08-BASE-A` | 2026-11-16T21:01:43Z | `registres/scellements-v1.md` ; commit `ccf3936a` |
| M-1 (audit R4 de la base (A)) | « non déclenché », code 0 | R-3019 (3) |
| `ISSUE-MOTS-ET-COUT-T06` | 2026-11-16T21:02:42Z | commit `3f979eb2` |
| bloc M, ligne dédiée | R-3018, « ne s'applique pas », sans « mot de Lazar » | commit `065e37c4` |
| faits de la phase B, liste v3 | R-3019 ; `registres/qui-a-lu-quoi-v3.md` (`3188e8af…`), attestation conforme (`1a68f36b…`) | commit `bcdbbc27` |
| R-V1, R-V2 | R-3020, R-3021 | commit `8917d28b` |
| bloc C0 joué à blanc sur `origin/main` `8917d28b`, à 21:13:04Z | quatre « ligne … : une » ; « décision R-3018 : présente, dédiée » ; « plan de B bis : ligne présente » ; aucun « ARRÊT » | ci-dessus |
| noms | consigne, fichier d'issue et liste : aucun fragment de `INTERDITS_NOMS_B` ; chemin du fichier d'issue sans espace | `grep -c` = 0 |

## 2. Valeurs des huit marqueurs du bloc 1C

| marqueur | valeur |
|---|---|
| `<<LISTE>>` | `registres/qui-a-lu-quoi-v3.md` |
| `<<EMPREINTE_LISTE>>` | `3188e8af4a704fa23cc638146b6123960561516bf6ff49ef3ed8d2cfd3a1ea37` |
| `<<CONSIGNE_LECTEUR_B>>` | `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1.md` |
| `<<EMPREINTE_CONSIGNE_LECTEUR_B>>` | `1fa37cbc984beb977c418e81c838131f848ceb46b053c6e2e01b077f99e4d8ae` |
| `<<REGISTRE_BBIS>>` | `registres/t07-etape-b-bis-v1.md` |
| `<<CLE_PLAN_BBIS>>` | `SCELLEMENT-BBIS` |
| `<<R_BA_L2>>` | `R-3018` |
| `<<BRANCHE_PIECE>>` | `verdict/t06-mots-et-cout-compte-3-v1` (les sorties restent sur cette branche ; la mère ne les recopie pas) |

## 3. Brouillons de lignes laissés à la mère (décision ou constat, non établis par programme)

~~~~text
| R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **R-V4 : la mère accepte**, en remettant la commande phase C v4 (`f4bcf406…`), la lecture structurelle par programme de la section 9 du contrôle à blanc (§ 0.4 ; `--chaine` gardé au bloc C3) : garde d'ouverture du module sur une copie du registre, puis lectures d'avant les scores (table A, issue de P3-bis, audit, fichier « mots et coût », épisodes, colonnes des mesures), sans rien afficher ; jamais les scores. | décision |
~~~~

Recommandation de la préparation reprise : garder `--chaine`, confiance 0,75 (le retirer changerait le bloc C3, donc une version 5).

~~~~text
| R-<n> | 2026-11-<jj> (<HH:MM> UTC, `date -u`) | **R-V5** : (a) le plan de B bis scellé avant la lecture de l'étape B vient de R-2714 (2) et R-2716 (1), non de R-2740 ; (b) la commande remise est la phase C **v4** (`f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755`, R-2991), non la v2 que nomme la phase A ni la v3 ; (c) réserves du rapport v2 du préparateur ouvertes : module d'étape B jouet seulement en répétition, blocs C1 et C1a non exercés sur le vrai dépôt, voies des scores non éprouvées avant l'appel (code 3 possible), transport local des répétitions. | constat |
~~~~

Le point (a) n'a pas été revérifié ici (lignes R-2714, R-2716, R-2740 non relues) : la mère le relit avant d'inscrire.

## 4. Brouillon du message de la mère à Lazar (à coller par lui dans la session hôte)

~~~~text
Pour la session hôte du compte 3 (session des phases A et B) : commande phase C, version 4,
docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v4.md,
sha256 f4bcf4064e7ab7d53538ce998c2d4745a1ac4387443505d82e8f7a01aec7c755 (la v4, non la v3 ni la v2).
Hôte : cette session (GO-2026-11-16-01, point 6 ; R-<n> : remise dès que les préalables sont prêts).
Valeurs du bloc 1C : LISTE='registres/qui-a-lu-quoi-v3.md' ;
EMPREINTE_LISTE='3188e8af4a704fa23cc638146b6123960561516bf6ff49ef3ed8d2cfd3a1ea37' ;
CONSIGNE_LECTEUR_B='docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1.md' ;
EMPREINTE_CONSIGNE_LECTEUR_B='1fa37cbc984beb977c418e81c838131f848ceb46b053c6e2e01b077f99e4d8ae' ;
REGISTRE_BBIS='registres/t07-etape-b-bis-v1.md' ; CLE_PLAN_BBIS='SCELLEMENT-BBIS' ;
R_BA_L2='R-3018' ; BRANCHE_PIECE='verdict/t06-mots-et-cout-compte-3-v1'.
Lecteur B : sous-agent neuf du modèle C ; je te le nomme ici, en conversation : <nom, jamais écrit dans un fichier>.
Rapport final du lecteur : à moi seul ; à la mère, le point 3 de la section 13.
~~~~

## 5. Ce qui manque avant la remise

1. Vérification courte de la liste v3 par un agent neuf (préparation § 1.5 ; réserve 9 de la liste), ou sa levée par la mère ; une
   erreur trouvée donne une version 4 de la liste et change `<<EMPREINTE_LISTE>>`.
2. Cas douteux de la liste (réserves 5 et 10) : à trancher par la mère.
3. Lignes R-V4 et R-V5 (§ 3), décision et constat de la mère.
4. Mot direct de Lazar sur la date (préparation § 1.7), si la mère le juge encore nécessaire, puis la ligne qui le porte ; son numéro
   remplace `R-<n>` dans le message.
5. Le nom du modèle C pour le lecteur B, dit par Lazar en conversation.
6. Rejouer le bloc C0 à blanc juste avant le message, si `main` a avancé.

Fin : 2026-11-16T21:13:43Z (`date -u`).

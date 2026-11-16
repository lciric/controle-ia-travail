# Phase C v3 du compte 3 — calendrier, conditions de registre, ce qui manque, voie de remise — v1

- **Statut** : réponse du préparateur aux points 1 à 4 du message du coordinateur (précision du directeur relayée par la
  session mère, reçue pendant le travail, le 2026-11-16 avant 12:00Z). Brouillon pour la mère, qui décide ; rien n'est
  décidé ici. Fichier neuf, scellé, non commité.
- **Rédacteur** : sous-agent neuf de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH` (modèle A), préparateur des
  préalables de la phase C v3 ; écrit le 2026-11-16 à partir de 12:02:30Z (`date -u`).
- **Lu pour ce point** (noms de clés et dates seulement pour les registres) : `commande-compte-3-phase-c-v3.md`
  (`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`) ; `rapport-preparateur-v1.md` (l. 10-20 et calendrier) ;
  `commande-compte-3-v1.md` (§ 9, gabarit de la phase B, et § 15) ; `verification-courte-commandes-v2-v3-v1.md` (§ 3 à 6) ;
  `controle_a_blanc_etape_b_compte_3_v2.py` (code entier, non lancé) ; `lecture_etat_ba_l2_mere_v1.py` (en-tête et options) ;
  `registres/scellements-v1.md`, `registres/t07-etape-b-bis-v1.md`, `registres/t07-etape-b-bis-v1-addenda-v1.md` sur
  `origin/main` à `d4b81652d936d6d3fd620cd4260d367a0fa83805` (clés, dates, chemins cités) ; lignes R-2734, R-2762, R-2772 à
  R-2970 et GO-2026-11-15-01, GO-2026-11-16-01 des registres. **Rien de 7a, de 7b, de T0.7** (au-delà des noms de pièces) **ni
  de P3-bis ouvert.**

## Verdict

1. **La commande v3 n'impose aucune date** : seulement des conditions de registre et d'ordre. « Mardi 17 » est une
   estimation du chemin critique (rapport v1, l. 15 : « pas avant mardi 17 au plus tôt » ; calendrier « jugements, non
   opposables »), devenue une date écrite dans la ligne GO-2026-11-16-01, point 6.
2. **Manquent aujourd'hui** : `LECTURE-T08-BASE-A` et `ISSUE-MOTS-ET-COUT-T06`, qui suivent la course de la pièce « mots et
   coût » sur 7b (la **phase B** du compte 3, dont la commande v2 n'existe pas) ; la ligne dédiée de BA-L2 ; la consigne du
   lecteur B ; la liste v3 ; les lignes R-V1, R-V2 et R-V4 de la mère.
3. **Remise par le directeur**, collée dans la session hôte. Si la commande de la phase B part maintenant, la phase C peut
   être remise ce soir (environ 5 à 7 heures de chemin critique) et le verdict B écrit dans la nuit.

## 1. Date ou condition de calendrier

- **Commande v3** : aucune occurrence de « mardi », « novembre », « calendrier », « pas avant » ni « échéance ». Les seules
  conditions de temps qu'elle porte sont : lignes du registre **strictement antérieures à l'instant** (contrôle à blanc,
  sections 3 et 8) ; horloge à 120 s au plus de la référence (bloc 2C) ; quota sous 80 % avant C4a et C6 (§ 4) ; borne de
  60 minutes pour l'appel, au-delà nœud du directeur sans arrêt du processus (§ 0.3). Ce sont des conditions d'ordre et de
  marche, non des dates.
- **Origine de « mardi 17 »** : `rapport-preparateur-v1.md`, l. 15-16 (« Étape B : pas avant mardi 17 au plus tôt ; chemin
  critique : la pièce « mots et coût » (code inexistant, 1,5 à 2 jours avec contre-lecture), puis le plan scellé de B bis
  (lundi ou mardi, R-2716) ») et son calendrier (« Calendrier réaliste (jugements, non opposables) ») ; R-2734. Repris tel
  quel par : le brief v3 de la mère (point 4, « étape B pas avant mardi 17 ») ; R-2845 ; la passation et le brief de relance
  de l'hôte ; R-2926 ; **GO-2026-11-16-01, point 6** : « phase C du compte 3 : jouée mardi 17 dans la session hôte actuelle,
  voie (a) en repli (R-2926) ».
- **Les deux pièces du chemin critique estimé existent depuis le 14** : `CODE-MOTS-ET-COUT-T06` (2026-11-14T14:55:41Z) et
  `SCELLEMENT-BBIS` (2026-11-14T12:30:30Z). Le chemin critique réel est maintenant la course de la pièce (phase B), puis la
  consigne du lecteur B.
- **Mot du directeur à consigner** : la ligne GO-2026-11-16-01 écrit « mardi 17 ». Pour jouer plus tôt, la mère inscrit au
  registre des décisions le mot direct du directeur, mot pour mot (une ligne de GO ne s'écrit que sur un mot direct), par
  exemple : « phase C remise dès que ses préalables sont prêts, dans la session hôte actuelle ; le point 6 de
  GO-2026-11-16-01 se lit ainsi ». Recommandation : le faire avant toute remise ; confiance 0,8.
- **Non vérifiable par moi** : le texte scellé de T0.7 (la commande cite sa ligne 2183 : l'étape B attend l'état de BA-L2)
  et les textes de B bis. Je n'en lis que les noms. Si l'un d'eux porte une condition de calendrier, je ne la vois pas ;
  voir aussi le point 3, dépendance B bis.

## 2. Conditions une à une, et leur état le 2026-11-16 vers 12:00Z (`origin/main` à `d4b81652…`)

| condition | où elle est exigée | état |
|---|---|---|
| `AUDIT-FUITES-T07`, une ligne exactement dans `registres/scellements-v1.md` | bloc C0 | présente, 2026-11-14T14:57:54Z |
| `CODE-MOTS-ET-COUT-T06`, une ligne exactement | bloc C0 | présente, 2026-11-14T14:55:41Z |
| `LECTURE-T08-BASE-A`, une ligne exactement | bloc C0 ; bloc M de la mère | **absente** |
| `ISSUE-MOTS-ET-COUT-T06`, une ligne exactement, son fichier présent et égal à son compagnon | blocs C0, C2, C5 | **absente** |
| ligne `<<R_BA_L2>>` de `registres/decisions.md`, dédiée, qui nomme BA-L2, sans mot de B bis | bloc C0 | **absente** : huit lignes nomment BA-L2, aucune n'est la ligne dédiée (elle suit le bloc M) |
| `SCELLEMENT-BBIS`, une ligne exactement dans `registres/t07-etape-b-bis-v1.md` sur `main` | bloc C0 ; contrôle à blanc, section 8 | présente, 2026-11-14T12:30:30Z, cite `prereg/T0.7-etape-B-bis-v1.md` |
| `SCELLEMENT-BBIS` absente de `registres/scellements-v1.md` | bloc C0 | absente (0 ligne) : conforme |
| `CONSIGNE-AUDIT-FUITES-T07` avant `AUDIT-FUITES-T07` | contrôle à blanc, section 4 | 2026-11-11T14:08:06Z avant 2026-11-14T14:57:54Z : oui |
| `SCORES-T07` et `SONDES-T07` avant `VERDICT-P3BIS` | contrôle à blanc, section 4 | 2026-11-14T01:55:05Z avant 2026-11-14T10:30:38Z : oui |
| `CODE-T07` (commit C7, 26 fichiers) | contrôle à blanc, section 6 | ligne présente (2026-11-13T23:42:46Z) ; fichiers non contrôlés ici |
| aucune ouverture de l'étape B avant le plan de B bis (R-2740) | condition d'ordre B bis | 0 ligne « etape-B » ou « scores-t07 » dans `registres/scellements-v1.md.ouvertures.md` sur `main` |
| ordre des préalables (R-V1) | vérification courte, R-V1 | **à décider par la mère** (ci-dessous) |
| consigne scellée du lecteur B, sur `main` | § 0.2 ; blocs 1C et C5 | **absente** |
| liste « qui a lu quoi » v3 scellée, sur `main`, ligne de l'hôte à `CELLULE_HOTE` | § 0.2 ; blocs 1C et 2C | **absente** (brouillon 1 en cours) |
| `<<BRANCHE_PIECE>>` | blocs 1C et C2 | sans objet tant que la phase B n'a pas couru (gabarit : `verdict/t06-mots-et-cout-compte-3-v1`, absente au distant à 12:02Z) |
| filtre de contenu de B bis sur l'extrait du lecteur B (lignes du registre des scellements) | bloc C5 | 0 ligne touchée aujourd'hui |
| pièces que C5 copie depuis `main` (textes de T0.7, T0.6, T0.8, consigne de l'audit, N-063 v2, issue de P3-bis, `audit-fuites-t07.json`) | bloc C5 | toutes présentes avec leur compagnon (noms seulement) |
| clé que le bloc M lit dans la sortie de la pièce | bloc M | défaut `lignes.BA-L2.s_applique` ; la pièce v3 écrit `"BA-L2": {"s_applique": …}` (relevé par mot-clé) : compatible, à confirmer au bloc M |
| clés de B bis présentes, non lues par la commande | — | `ABSENCE-B-BBIS` (2026-11-14T12:30:30Z, même registre) ; `ADDENDUM-ECART-1-BBIS` (2026-11-16T00:59:36Z, registre voisin `registres/t07-etape-b-bis-v1-addenda-v1.md`) |

**Ordre R-V1, cas douteux** : la vérification courte demande de comparer « `AUDIT-FUITES-T07` < `CODE-MOTS-ET-COUT-T06` <
`LECTURE-T08-BASE-A` ≤ `ISSUE-MOTS-ET-COUT-T06` », puis le jour de la ligne `<<R_BA_L2>>`. Le registre porte l'ordre
inverse pour les deux premières : `CODE-MOTS-ET-COUT-T06` (14:55:41Z) **avant** `AUDIT-FUITES-T07` (14:57:54Z). C'est
l'ordre voulu ensuite par R-2767, R-2778 et R-2779 : le coffre de l'audit des fuites (tiré des textes de 7b) ne s'ouvre
qu'après la ligne du code de la pièce, écrit sans vue de 7b. La comparaison de R-V1, prise à la lettre, échouerait ;
recommandation : la mère consigne l'ordre à tenir, `CODE-MOTS-ET-COUT-T06` < `AUDIT-FUITES-T07` < `LECTURE-T08-BASE-A` ≤
`ISSUE-MOTS-ET-COUT-T06`, puis la ligne `<<R_BA_L2>>`, et le constat sur les dates réelles ; confiance 0,75.

**Contrôle à blanc : non lancé.** Le script ne lit pas que les registres. Son en-tête (l. 18-23) et son code le disent :
section 1, il analyse la configuration scellée de T0.7 (`json.loads`) et en imprime les marques ; section 3, il hache les
fichiers cités par les lignes (sorties et code de T0.7) ; section 5, il lit le journal et le registre des préalables de
P3-bis ; section 6, il lance des commandes git sur le dépôt du module et hache ses 26 fichiers ; section 7, il hache les
données de l'étape B ; section 8, il hache le texte de B bis ; section 9 (seulement avec `--chaine`), il lit la table A,
l'issue de P3-bis, l'audit, le fichier « mots et coût » et les mesures. Je ne l'ai donc pas lancé et n'ai écrit aucune
sortie. L'hôte le joue de toute façon aux blocs C3 et C4a. Si la mère veut un relevé avant la remise, elle peut le jouer en
mode `rapport`, sans `--chaine` : attendus, les manques `ISSUE-MOTS-ET-COUT-T06` (et `LECTURE-T08-BASE-A` si le module
l'exige), les fichiers cités par `SCORES-T07` et `SONDES-T07` et les données de 7b, absents de `main` jusqu'au bloc C2.

## 3. Ce qui manque pour remettre la phase C aujourd'hui : qui, dans quel ordre, combien de temps

Chemin critique d'abord. Les durées sont des jugements, sauf celles que la commande ou le rapport v1 donnent.

1. **Phase B, course de la pièce « mots et coût » sur 7b** (seul pas long ; sans elle, le bloc C0 s'arrête) :
   1. **Mère**, par un préparateur neuf : commande de la phase B **v2**, d'après le gabarit de la section 9 de
      `commande-compte-3-v1.md` (« Ne joue aucun bloc de cette phase avec cette version » ; marqueurs `<<COMMIT_PIECE>>`,
      `<<LIGNE_CODE_MOTS_ET_COUT>>`, `<<COMMANDE_PIECE>>`, `<<MOTIF_RUN_PIECE>>` ; branche neuve
      `verdict/t06-mots-et-cout-compte-3-v1` ; entrées de 7b placées depuis un dépôt jetable, jamais commitées ; un seul
      appel ; sorties `diag/<run>/` et `runs/<run>/` seules commitées). Répétition sur dépôts jouets (R5), contre-lecture par
      un autre modèle, sceau, poussée sur `main` : environ 2 à 3 heures.
   2. **Directeur** : colle cette commande dans la session hôte, avec son chemin et son empreinte. **Hôte** : la joue ;
      « exécution < 2 h » selon le rapport v1, environnement compris.
   3. **Mère** : vérifie les blobs des sorties par empreinte, sans les ouvrir ; inscrit `LECTURE-T08-BASE-A` puis
      `ISSUE-MOTS-ET-COUT-T06` (ordre de la phase C v3, § 15 : les lignes d'abord, puis le bloc M) ; joue le bloc M ; écrit
      la ligne dédiée `<<R_BA_L2>>` : environ 20 à 30 minutes. Si BA-L2 « s'applique » : mot du directeur avant l'étape B
      (nœud).
2. **En parallèle du point 1** :
   1. **Consigne du lecteur B** : un rédacteur neuf qui a le droit de lire le texte scellé de T0.7 (je ne l'ai pas : je
      prépare seulement son squelette), contre-lecture par un autre modèle, sceau, poussée sur `main` : environ 3 heures
      (la consigne A a pris 2 heures et 1 heure de contre-lecture, selon le calendrier du rapport v1).
   2. **Liste « qui a lu quoi » v3** : mon brouillon 1, complété des faits de la phase B, vérification courte par un agent
      neuf, sceau, poussée sur `main` : environ 1 heure après la phase B.
   3. **Lignes de la mère** : R-V1 (ordre décidé, dates comparées), R-V4 (section 9 acceptée, ou `--chaine` retiré et le
      risque déclaré), R-V2 (couple de la phase C § 15 (2) : « recopie, par programme et sans les ouvrir ni les afficher »),
      mot du directeur sur la date : environ 15 minutes.
3. **Mère** : message au directeur avec le chemin et l'empreinte de la commande (`9d788919…`) et les valeurs des huit
   marqueurs du bloc 1C ; le directeur nomme en conversation le modèle C du lecteur B.
4. **Directeur** : colle la commande v3 dans la session hôte. **Hôte** : blocs 0b-C à F-C, environ 30 à 45 minutes de
   gestes (environnement avec torch environ 15 minutes, placement environ 5 minutes, contrôle à blanc, appel unique de moins
   de 3 minutes, borne 60 minutes), puis le lecteur B, 2 à 4 heures.

**Total** : remise possible environ 5 à 7 heures après le départ de la commande de la phase B ; verdict B 3 à 5 heures
plus tard.

**Point qui demande un mot avant de jouer l'étape B avant la course de B bis** (mercredi 18) : la commande interdit que
rien de la branche de l'étape B entre dans un espace de B bis avant le verdict scellé de B bis (§ 0.5 et § 15 (5)). Or la
mère recopie dans `main` le journal des ouvertures, puis le verdict B (§ 15 (1) et (2)). Tout commit de `main` que B bis
fusionnerait ensuite (fusion `--no-ff` et commit X, R-2790) les porterait. De plus, le registre de B bis porte
`ABSENCE-B-BBIS`, et son addendum un « relevé de l'étape B » (R-2955, R-2959) : je ne peux pas lire ce qu'ils exigent (ce
sont des pièces de T0.7). Recommandation : avant la remise de la phase C, la mère fait vérifier, par un agent qui peut lire
B bis, si B bis exige l'absence de l'étape B à son lancement. Si oui : la course de B bis passe d'abord, ou bien la recopie
du verdict B dans `main` attend le commit X de `CODE-BBIS`. Confiance 0,6.

## 4. Comment la commande se remet à l'hôte

- **Par le directeur, collée dans la session hôte** `session_016QhUrrSUMEzEqWPnQYxjHB`, celle de la phase A
  (GO-2026-11-16-01, point 6 ; voie (a) en repli). Sources : commande v3, l. 3-4 (« à coller par Lazar dans **la même
  session** que la phase A ») ; § 3 (« chemin et empreinte de la version remise : Lazar, en conversation ; le bloc 0b-C les
  imprime ») ; bloc 0b-C (« l'empreinte est celle que Lazar t'a donnée (sinon arrêt) ») ; brief de relance de l'hôte, § 2
  point 2, § 8 et § 11 (« les décisions, les nœuds et les GO viennent de Lazar en conversation » ; « attendre la commande
  phase C v3, remise par Lazar avec son empreinte, ses marqueurs ») ; précédent de la phase A (R-2773 : message de la mère
  au directeur, marqueurs remplis ; R-2808 : remise collée par le directeur).
- **Pas par un message de la mère** : pour l'hôte, un message d'une autre session est une information (brief de relance,
  § 8 et § 9). La mère peut annoncer par le canal (R-2807) que les préalables sont prêts. Elle remet au directeur le texte à
  coller : chemin et empreinte de la commande ; valeurs des huit marqueurs du bloc 1C (`LISTE`, `EMPREINTE_LISTE`,
  `CONSIGNE_LECTEUR_B`, `EMPREINTE_CONSIGNE_LECTEUR_B`, `REGISTRE_BBIS='registres/t07-etape-b-bis-v1.md'`,
  `CLE_PLAN_BBIS='SCELLEMENT-BBIS'`, `R_BA_L2`, `BRANCHE_PIECE`) ; le choix de l'hôte. Le bloc 1C s'arrête si un marqueur
  reste.
- **Même voie pour la phase B** : collée par le directeur dans la même session hôte, avant la phase C.
- **Modèle du lecteur B** : la commande le fixe au modèle C (§ 2, `NOTE_MODELE="modèle C"`), sans repli. Le directeur nomme
  ce modèle en conversation. Un autre modèle (par exemple le modèle B, de nouveau disponible selon R-2813) serait un écart à
  la commande : une version 4, ou un mot du directeur.

Fin : 2026-11-16T12:03:43Z (`date -u`).

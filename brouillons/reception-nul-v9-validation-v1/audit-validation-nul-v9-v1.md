# Audit écrit — validation décisive du nul v9 (banc des tricheurs v9), v1

**Issue que donnent les critères gelés appliqués par moi : « puissance perdue », lue au premier étage** (18 lignes fatales « tenues », 3 artefacts « tenus », règle de P1b non jouée), portée par I02 (105 répétitions perdues sur 1 000, « non tenue » au rang 1 de Holm).
**Elle est égale à l'issue écrite par le code** (`lecture.issue` du rapport scellé), et chaque grandeur recalculée depuis les comptes bruts est égale à celle du banc (bornes à 3,4·10⁻¹⁵ près, valeurs p, statuts de Holm, issue).
**A6 est déclenché par l'issue elle-même ; je n'ai trouvé aucun défaut** (rejeux de T12a et d'I02 identiques au rapport scellé au bit près ; la perte d'I02 vient du nul, pas du certificat) ; 12 réserves de cet audit et 8 héritées, aucune ne change l'issue ; le verdict revient au lecteur neuf (R13).

Auditeur neuf (règles R4 et R13) : je n'ai écrit ni le nul v9, ni son banc, ni son préenregistrement, ni ses brouillons, ni sa
contre-lecture, ni la vérification courte. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/audit-validation-nul-v9-prompt.md`.
Travail du 3 novembre 2026, de 05:21 à 05:58 (heures relevées par `date -u`, en temps universel coordonné). J'établis les faits ;
je ne prononce pas le verdict.

## 0. Légende

| Terme | Sens |
|---|---|
| UTC | temps universel coordonné ; toutes les heures de ce fichier |
| JSON | format de données en texte (`manifeste.json`, `banc-tricheurs-v9.json`) |
| α, log 20 | α = 0,05 ; seuil de richesse 1/α = 20 ; log 20 = 2,9957 |
| log W, « log W max » | logarithme de la richesse : vraisemblance de la loi de la fiche moins celle du meilleur membre du nul, mêmes issues ; « max » : le plus grand des 8 instants lus (25, 50, …, 200) |
| promotion | log W ≥ log 20 à un instant lu **et**, pour une fille, gain final sur la meilleure enveloppe ≥ 2δ₀ = 0,02 nat par tirage (`pole/nul_v9.py`, lignes 526 à 543) |
| v8 apparié | la même fiche, sur les mêmes issues, jugée par la bibliothèque v9 privée de ses membres par morceaux (= bibliothèque du nul v8) |
| perdue, gagnée | répétition promue sous le v8 apparié et non sous v9 ; l'inverse |
| Clopper-Pearson | bornes exactes d'une proportion, ici chacune unilatérale à 95 % |
| Holm | correction descendante pour plusieurs tests, niveau familial 0,05 |
| H1 à H4, P1 à P7, A1 à A6, L1 à L12 | hypothèses, prédictions, déclencheurs d'audit, lectures préalables du texte scellé (sections 3, 4, 8, 10) |
| R2, R4, R9, R13 | règles du programme : contre-lecture par un lecteur neuf ; symétrie de l'audit ; graines et manifeste par course ; verdict par un lecteur neuf |
| VC1 à VC8 | réserves 1 à 8 de la vérification courte neuve, portées ici |
| R-1278 … R-1300 | lignes de `registres/decisions.md` |

## Pièces lues et leurs empreintes

- **Texte scellé** `orchestrator/prereg/preenregistrement-validation-nul-v9-v1.md` : sha256 `54c5713d07f61b7f2bb3dd8218f4bca881a044a2b11508015db5e727d62c18fb` sur disque, à `git show 66dbcf1:` et dans son compagnon : égales. Lu en entier (671 lignes).
- **Réception** (`sha256sum -c` conforme à 05:21 et de nouveau à 05:50) : `manifeste.json` `e159465681cf…e39e943`, `banc-tricheurs-v9.json` `0cd66bade779…79fca48`, `sortie-erreur-course-v1.txt` `87a7cc30632c…2186d35`, `LISEZMOI-reception-v1.md` `312b7a8af1ac…907d0e`, `depart-utc-v1.txt` `f9f5c78620e6…4888f8`. Les deux JSON et leurs compagnons sont identiques à l'octet (`cmp`) aux originaux de `ideation-organism/resultats/banc-tricheurs-v9-validation-v1/` (dossier non committé), dont les compagnons sont aussi conformes.
- **Vérification courte** `brouillons/reprise-conv-audit-2026-11-02-nuit/rapports-sous-agents/verification-courte-nul-v9-description-v1.md` : compagnon conforme ; lue en entier.
- **Précédent** : `resultats/banc-tricheurs-v8-validation-v1/verdict-R13-validation-nul-v8-v1.md`, `ecart-section13-v1.md`, `ecart-section13-v2.md` (compagnons conformes) ; lus en entier.
- **Code gelé** : les 14 fichiers de `FICHIERS_GELES`. Lus en entier : `demonstrations/banc_tricheurs_v9.py`, `pole/nul_v9.py`. Lus en partie : `demonstrations/banc_tricheurs_v8.py` (lignes 90 à 430 : graines, juge, statistique), `pole/outils.py` (scellement, manifeste), `pole/selection_pari.py` (cache, gel, calibrage).
- **Registres** : `registres/decisions.md`, lignes R-1278 et R-1292 à R-1300.

## 1. Conformité de la course au plan

| Point du plan (texte scellé) | Prescrit | Constaté | Preuve |
|---|---|---|---|
| Texte et scellement (sections 5, 14 point 5) | texte `…-v1.md` scellé, commité et poussé avant la course | commit `66dbcf1` à 23:20:16 (n'ajoute que le texte et son compagnon) ; poussée à 23:20:18 ; départ à 23:20:38 | `git show --stat 66dbcf1` ; journal local de `origin/main` (« update by push », 2026-11-03 00:20:18 +0100) ; `depart-utc-v1.txt` ; R-1292 |
| Commande (section 5) | `nice -n 10 python3 -I -B demonstrations/banc_tricheurs_v9.py ../resultats/banc-tricheurs-v9-validation-v1 --preenregistrement prereg/preenregistrement-validation-nul-v9-vN.md --repetitions 1000 --processus 2`, sans `--duree-max-s` | cette commande avec `v1`, sans `--duree-max-s`, `nice` 10, dossier courant `orchestrator/`, identifiant de processus 26187 (ouvriers 26189 et 26190) | table des processus lue par la vérification courte (question 5) ; LISEZMOI ; R-1292 ; cohérent avec le manifeste (lignes suivantes) |
| Mode | décisif | `reglages.mode` = `mode` du rapport = `"decisif"` ; `reglages.preenregistrement.chemin` = `prereg/preenregistrement-validation-nul-v9-v1.md` | manifeste, rapport |
| Lignes | les 31 de la section 3, ordre de `LIGNES` | `reglages.lignes` (31) et `resultats` (31) égaux au plan, rôles et ordre compris ; 31 clés de graines distinctes | `conformite_v1.py` |
| Répétitions | 1 000 | `reglages.repetitions` = `repetitions` du rapport = 1 000 ; chaque ligne : 1 000 | idem |
| Durée gelée | 172 800 s (48 h), par défaut | `reglages.duree_max_s` = 172800.0 ; course de 6 020,8 s (1 h 40 min 21 s), 3,5 % de la garde ; aucun arrêt | idem ; `duree_s` |
| Processus | 2 | `reglages.processus` = 2 ; somme des durées des lignes 11 876,1 s, soit 1,97 fois l'horloge | idem |
| Entropie (section 5) | entier de l'empreinte du texte, ≥ 2⁶⁴ | `reglages.entropie_racine` = 38343129695488081123730001133079774509792561579847260681839260094342449862907 = `int("54c5713d…", 16)` ; ≥ 2⁶⁴ | recalcul |
| Code gelé (sections 5, 12) | 14 fichiers = bloc de la section 12 | bloc (14 lignes) = `reglages.code_du_banc_sha256` = `reglages.preenregistrement.empreintes_du_code_verifiees` = `preenregistrement.empreintes_du_code_verifiees` du rapport = disque = `git show 66dbcf1:` ; `git diff --stat 66dbcf1 HEAD` sur les 14 : vide ; `code_sha256` du manifeste égal pour les 11 fichiers gelés de `pole/` ; les 12 dépendances égales au bloc scellé du v8 (`preenregistrement-validation-nul-v8-v2.md`, `7f37631d…`) | `conformite_v1.py`, `empreintes-arbre.txt`, `empreintes-66dbcf1.txt`, `empreintes-bloc12.txt` |
| Environnement (R9) | manifeste par course | Python 3.13.18, numpy 2.5.3, pôle 0.7.0, linux ; nul `7ae450df…`, nul v8 `cc452aaf…` ; **ni date ni commit** dans le manifeste (même structure que le manifeste du v8) | manifeste |
| Sorties | `manifeste.json` avant la course, `banc-tricheurs-v9.json`, compagnons écrits par le banc | les deux, avec compagnons conformes | `sha256sum -c` |
| Un scellement, une course | aucune course décisive avant le scellement ; dossier neuf | dossier de sortie né à 23:20:38,398 (créé par la course), manifeste né à 23:20:38,402 ; aucun autre dossier `banc-tricheurs-v9-validation-v1*` dans `resultats/` | `stat`, `ls` |

**Dates.** Le manifeste ne porte aucune date : sa naissance (fichier) est 2026-11-02 23:20:38,402, égale au départ consigné
(23:20:38, `depart-utc-v1.txt`, R-1292). Le rapport est né le 2026-11-03 à 01:00:59,235 (compagnon à 01:00:59,240) ; 23:20:38,4
+ 6 020,8 s = 01:00:59,2 : cohérent. Durée attendue (section 5) : 1,3 à 2,2 h sur deux cœurs libres, 2 à 5 h sur machine partagée ;
observé 1,67 h et 0,383 s par répétition de ligne (prévu 0,3 à 0,5 s). Note sans réserve : la vérification courte écrit « lancée à
23:20:37 » ; la table des processus donne la seconde de démarrage du processus, le manifeste est écrit moins d'une seconde après.

**Écarts.**
- **Code de sortie non capturé** (lancement par `nohup … &`, LISEZMOI, R-1300 ; écart déclaré). Déduit, non observé : le rapport
  porte `fatales_au_dessus_de_alpha` = [] et `artefacts_non_vus` = [] (recalculés : aucune fatale au-dessus de α, les trois
  artefacts au-dessus), d'où `code_de_sortie` = 0 (lignes 363 et 364) ; le résumé des lignes 567 à 571 a été imprimé (section 6),
  donc `principal` a atteint son retour (ligne 572). La section 5 dit que le code ne décide pas.
- **Interruption du conteneur** entre environ 01:00 et 05:15 (R-1300), **après** la fin : le rapport complet et son compagnon
  sont écrits à 01:00:59 et le résumé est imprimé après l'écriture (lignes 566 puis 567) ; la machine a redémarré vers 05:16
  (`uptime` : 10 minutes à 05:26). Rien de la sortie n'est perdu, sinon le code de sortie et un éventuel flux d'erreur séparé.
- **Écart à R2 déclaré au texte** (paragraphe de scellement : changement de description de `pole/nul_v9.py` et essais de B1 non
  contre-lus avant le scellement) : **levé** par la vérification courte, faite de 23:24:57 à 23:42:53, avant que le rapport existe
  (01:00:59), « conforme avec réserves » (R-1295) ; ses réserves 1 à 8 sont portées ici (VC1 à VC8).
- **Section 14, point 6** (sur l'arbre scellé : essais et banc de mutations, **puis** la commande) : 20 s séparent la poussée
  (23:20:18) du départ (23:20:38), trop peu pour ces passages (40 s et 72 s chez la vérification courte). Joués par le directeur de
  23:15 à 23:19 sur un code identique (le commit de scellement n'ajoute que le texte et son compagnon) ; rejoués sur l'arbre scellé
  par la vérification courte pendant la course (23:36 à 23:38 : 37 essais, 35 sous-essais, 43 mutations sur 43). Même écart que la
  réserve R2 du verdict du v8 (et `ecart-section13-v1.md`, `-v2.md`) ; sans effet sur les nombres.
- **Charge concurrente, hors du plan** : un sous-essai d'A1-v3.1 a lancé une course factice complète en concurrence, arrêtée à
  00:14 par identifiants de processus (1683, 5955, 5956 ; R-1299) ; essais, mutations et deux courses exploratoires de la
  vérification courte entre 23:24 et 23:43 ; deux commits à 00:56:03 (`9776ed0`, `63ed933`) qui ne touchent aucun des 14 fichiers
  gelés (seuls changent d'autres fichiers de `pole/`, `demonstrations/`, `essais/`, `prereg/`). Effet : temps de calcul seulement.
  Les ouvriers démarrent par `fork` (méthode par défaut de ce Python 3.13), modules déjà chargés ; le banc de mutations mute en
  mémoire (`exec`, `essais/mutations_nul_v9.py`, ligne 205) ; et mes rejeux de T12a et d'I02 reproduisent le rapport au bit près
  (section 5).

## 2. Recalcul indépendant (`recalcul_v1.py`, sortie `sortie-recalcul-v1.txt`)

Méthode : le script ne lit que les comptes bruts du rapport (`promues`, `repetitions`, `apparie_v8.promues`, `apparie_v8.perdues`,
`log_w_max_max`, `dominants`) ; bornes par la loi bêta de scipy 1.18.1 (`beta.ppf`), valeurs p exactes par `binom.cdf` et
`binom.sf`, procédure de Holm réécrite d'après la section 6 ; puis il compare à ce que le banc a écrit (`lecture.*`,
`clopper_pearson_95_unilaterales`, `perte_clopper_pearson_95_unilaterales`). **Aucun écart.**

**2.1 Bornes.** Pour les 31 lignes, les 30 v8 appariés et les 30 pertes, le plus grand écart entre mes bornes de
Clopper-Pearson et celles du rapport est 3,4·10⁻¹⁵. Chaque `taux` et chaque `perte` écrits égalent compte/1 000.

**2.2 Lignes fatales (H1, H4 ; famille de 18).** Les 18 lignes : 0 promotion sur 1 000. Valeur p de H0 « taux ≥ α » :
0,95¹⁰⁰⁰ = 5,29·10⁻²³ (égale au champ `fatales_valeurs_p`, écart relatif 0) ; seuils de Holm de 0,00278 (rang 1) à 0,05 (rang 18) :
les 18 sont rejetées → 18 « tenue » (banc : 18 « tenue »). Valeur p de H0 « taux ≤ α » : 1. Borne haute de Clopper-Pearson à 95 % :
0,002991 ; au niveau de Holm le plus strict : 0,00587. Tables de la section 6 retrouvées exactement : promotions maximales pour
« tenue » par rang 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 33, 34, 34, 35, 36, 38 ; minimales pour « non tenue » 71, 71, 71,
71, 70, 70, 70, 70, 70, 69, 69, 69, 68, 68, 67, 66, 65, 63. Puissance écrite dans la section 6 retrouvée (rangs 1 et 18) : vrai
taux 0,02 → 0,9925 et 0,9999 ; 0,03 → 0,62 et 0,94 ; 0,04 → 0,081 et 0,41 ; 0,05 → 0,0022 et 0,043.

**2.3 Artefacts (H3 ; intersection-union, sans correction).** Seuil recalculé : 63 promotions (borne basse > α).

| Artefact | Promues / 1 000 | Borne basse 95 % | Moi | Banc (`lecture.artefact`) |
|---|---|---|---|---|
| T01\|v1 | 411 | 0,3851 | tenue | tenue |
| M01\|v8 apparié | 986 | 0,9782 | tenue | tenue |
| M02\|v8 apparié | 972 | 0,9618 | tenue | tenue |

**2.4 Pertes de puissance appariées (H2 ; famille de 5, marge 0,05, Holm dans chaque sens).**

| Ligne | Promues v8 apparié | Promues v9 | Perdues | Gagnées | d | Clopper-Pearson 95 % | p « tenue » (rang ; seuil) | p « non tenue » (rang ; seuil) | Moi | Banc |
|---|---|---|---|---|---|---|---|---|---|---|
| fille neuve | 985 | 947 | 38 | 0 | 0,038 | [0,0286 ; 0,0495] | 0,0434 (2 ; 0,0125) | 0,969 (4 ; 0,025) | non jugeable | non jugeable |
| fraîche neuve | 976 | 970 | 6 | 0 | 0,006 | [0,0026 ; 0,0118] | 1,7·10⁻¹⁵ (1 ; 0,01) | 1 (5 ; 0,05) | tenue | tenue |
| I01 | 863 | 820 | 43 | 0 | 0,043 | [0,0330 ; 0,0551] | 0,173 (3 ; 0,0167) | 0,863 (3 ; 0,0167) | non jugeable | non jugeable |
| I02 | 486 | 381 | 105 | 0 | 0,105 | [0,0894 ; 0,1223] | 1 (5 ; 0,05) | 1,6·10⁻¹² (1 ; 0,01) | **non tenue** | non tenue |
| F03 | 753 | 707 | 46 | 0 | 0,046 | [0,0356 ; 0,0584] | 0,311 (4 ; 0,025) | 0,739 (2 ; 0,0125) | non jugeable | non jugeable |

Pas à pas : famille « tenue », fraîche neuve rejetée au rang 1, puis fille neuve (0,0434 > 0,0125) arrête la procédure ; famille
« non tenue », I02 rejetée au rang 1 (borne basse au niveau 0,01 : 0,0836 > 0,05), puis F03 (0,739 > 0,0125) arrête. Tables
retrouvées : pertes maximales pour « tenue » 34, 34, 35, 36, 38 (égales au texte) ; minimales pour « non tenue » 68, 67, 66, 65, 63
(le texte donne 68 au rang 1). Probabilités de la section 6 retrouvées : « tenue » à d = 0,02 : 0,9987 et 0,9999 ; 0,03 : 0,80 et
0,94 ; 0,04 : 0,19 et 0,41 ; 0,05 : 0,0093 et 0,043 ; « non tenue » au rang 1 à 0,06 : 0,16 ; 0,08 : 0,93 ; 0,10 : 0,9998.
**Comparaison à la marge 0,05** : fraîche neuve établie dessous ; I02 établie dessus ; fille neuve, I01, F03 ni l'un ni l'autre.
Pour fille neuve, la borne haute non corrigée (0,0495) est sous 0,05, mais au niveau de son rang de Holm (0,0125) elle vaut 0,0539 :
« non jugeable » vient de la correction prescrite, pas d'une erreur.

**2.5 Monotonie appariée.** Sur les 30 lignes v9, promues v8 − promues v9 = perdues exactement : aucune répétition gagnée, taux v9 ≤
taux v8 partout (la garde l'imposait ; la course ne s'est pas arrêtée).

**2.6 Lignes v8 appariées (rapportées sans critère).** Les 11 lignes fatales du v8 : 0/1 000 (classes du v8 ; T12a : marge, section
5). M01 0,986 ; M02 0,972 ; M03 0,969 ; M04 0,897 ; M05 0,433 ; M06 0,949 ; M07 0,573. Puissance (v8 / v9) : fille neuve 0,985 /
0,947 ; fraîche neuve 0,976 / 0,970 ; I01 0,863 / 0,820 ; I02 0,486 / 0,381 ; F03 0,753 / 0,707.

**2.7 Lignes mesurées (sans critère ; v9, Clopper-Pearson 95 %, v8 apparié).** T07 9/1 000 [0,0047 ; 0,0157], 0,020 ; T12b 840
[0,8197 ; 0,8588], 0,899 ; H01 860 [0,8407 ; 0,8777], 0,958 ; H02 145 [0,1270 ; 0,1646], 0,965 ; H03 928 [0,9131 ; 0,9410], 0,951 ;
H04 236 [0,2140 ; 0,2591], 0,967 ; H05 90 [0,0755 ; 0,1063], 0,994. Toutes égales à `lecture.mesures`.

## 3. Issue : critères de la section 7 appliqués dans l'ordre

1. **« trou »** (une ligne fatale au moins non tenue) : non, les 18 sont « tenues ».
2. **« puissance perdue »** (aucune fatale non tenue, une perte au moins non tenue) : **oui**, I02. Lecture à deux étages :
   18 fatales « tenues » (`lecture.fatales`), 3 artefacts « tenus » (`lecture.artefact`), règle de P1b non jouée (T05s : 0 promotion,
   log W max −0,00581 ; T09g : 0 promotion, −0,00589 ; seuil +0,25) → **premier étage** : « le v9 ferme les lignes, au prix mesuré sur
   la ligne nommée » (I02) ; décision de Lazar : accepter le prix ou chercher un nul moins coûteux.
3. à 5. Non atteints.

Code : `lecture.issue` = « puissance perdue », `lecture.audits` = [], `issue_suspendue_par_audit` = faux. **Égalité.**

**Une ambiguïté, sans effet sur l'issue : le statut de l'issue entre la fin de la course et cet audit.** La section 8 range A6
(« toute issue […] “puissance perdue” […] : même audit avant lecture ») parmi les audits lus par le lecteur du verdict, et la section
7 dit « Tout audit déclenché suspend l'issue jusqu'à l'audit écrit (`issue_suspendue_par_audit`) ».
- Lecture 1, celle du champ nommé : le code ne calcule que A1 à A5 ; `issue_suspendue_par_audit` = faux ; l'issue se lit sans
  suspension et A6 n'est qu'une relecture du lecteur R13.
- Lecture 2, celle de la phrase : A6 est déclenché par toute issue « puissance perdue », donc l'issue est suspendue jusqu'à l'audit
  écrit, puis lue si le lecteur ne trouve pas de défaut (section 8 : « A6 : défaut trouvé → course invalide ; sinon l'issue est lue,
  note jointe »).
- Ce qui les sépare : seulement le statut entre 01:00:59 et cet audit. Une fois l'audit écrit, et si le lecteur du verdict ne
  retient pas de défaut, les deux donnent « puissance perdue », premier étage.

Point pour la décision (pas une ambiguïté de l'issue) : le premier étage nomme un seul prix, celui d'I02 (au moins 0,0836 au niveau
de Holm), mais trois des cinq pertes ne sont pas établies sous la marge (fille neuve, I01, F03 : 0,038 à 0,046, bornes hautes
0,0495 à 0,0584). La section 7 dit que les pertes et puissances observées sont publiées avec leurs bornes : le prix soumis à Lazar
est donc celui des cinq lignes.

## 4. Prédictions P1 à P7 (elles ne décident pas de l'issue, section 4)

| Prédiction | Énoncé | Observé | Tenue ? |
|---|---|---|---|
| P1a | 8 lignes linéaires et M01 à M07 : 0 promotion sur 1 000, log W ≤ 10⁻⁶ à chaque répétition | 0 partout ; maximum des 15 lignes −3,11·10⁻¹⁰ (M02) | oui |
| P1b | T05s, T09g : 0 sur 1 000, log W max ≤ +0,25 | 0 et 0 ; −0,00581 et −0,00589 | oui |
| P1c | T12a : au plus 10 sur 1 000 | 0 | oui |
| P2 | v8 apparié : M01 ≥ 0,95, M02 ≥ 0,90 | 0,986 ; 0,972 | oui |
| P3 | T01\|v1 dans [0,30 ; 0,60] | 0,411 | oui |
| P4 | pertes : fille neuve [0,01 ; 0,08], fraîche neuve [0,00 ; 0,03], I01 [0,02 ; 0,09], I02 [0,06 ; 0,17], F03 [0,01 ; 0,07] | 0,038 ; 0,006 ; 0,043 ; 0,105 ; 0,046 | oui (5/5) |
| P5 | puissance v9 : fille neuve [0,90 ; 1], fraîche neuve [0,88 ; 1], I01 [0,80 ; 1], I02 [0,30 ; 0,52], F03 [0,60 ; 0,82] | 0,947 ; 0,970 ; 0,820 ; 0,381 ; 0,707 | oui (5/5) |
| P6 | T07 ≤ 0,03 ; T12b [0,65 ; 0,88] ; H01 [0,80 ; 0,96] ; H02 [0,12 ; 0,32] ; H03 [0,82 ; 0,96] ; H04 [0,16 ; 0,38] ; H05 [0,04 ; 0,18] | 0,009 ; 0,840 ; 0,860 ; 0,145 ; 0,928 ; 0,236 ; 0,090 | oui (7/7) |
| P7 | « puissance perdue », portée par I02 ; « non tenue » dès 68 pertes au rang 1 ; I01 et fille neuve près de la marge | « puissance perdue », I02 à 105 ; I01 0,043 et fille neuve 0,038, non jugeables | oui |

Le champ `lecture.predictions` du banc dit « vrai » partout, mais il ne code que les comptes : ni « log W ≤ 10⁻⁶ » (P1a) ni « ≤ +0,25 »
(P1b) ; je les ai lus sur `log_w_max_max` (réserve 9).

## 5. Audit de symétrie (R4, section 8)

**5.1 Déclencheurs écrits d'avance.**

| Déclencheur | Règle | Valeur lue | Déclenché ? |
|---|---|---|---|
| A1 (code) | une promotion sur une ligne refusée par construction (linéaire, par morceaux, log-linéaire) | 0 sur les 17 lignes concernées | non |
| A2 (code) | taux v9 au-dessus du v8 apparié | aucune ligne ; aucune répétition gagnée sur 30 lignes | non |
| A3 (code) | T01\|v1 hors de [0,10 ; 0,90] ; M01 ou M02 v8 apparié sous 0,50 | 0,411 ; 0,986 et 0,972 | non |
| A4 (code) | log W > 10⁻⁶ sur une répétition des classes linéaire ou par morceaux | maxima : M02 −3,11·10⁻¹⁰, M01 −5,14·10⁻¹⁰, M07 −6,01·10⁻¹⁰, M06 −1,65·10⁻⁹, M05 −8,6·10⁻⁴, M03 −2,5·10⁻³, M04 −0,032, T17s −0,047, nul exact −0,078, T03u −0,141, T03b −0,151, T01 −0,298, T09l −0,504, T04 −0,863, T02 −0,991 | non |
| A5 (code) | sur une ligne M, un membre par morceaux domine dans moins de la moitié des répétitions | M01 999, M02 997, M03 1 000, M04 998, M05 ≥ 993 (listés 997), M06 997, M07 912 (seuils 911, `ajuste_log:archive:S2` 88 : le cas que la lecture L3 annonçait, 90/100 et 10/100) | non |
| Règle de P1b (lecteur) | A1 sur T05s ou T09g, ou log W max > +0,25 | 0 promotion ; −0,00581 et −0,00589 | non |
| A6 (lecteur) | toute issue « trou », « puissance perdue » ou « non concluant » | « puissance perdue » | **oui, par construction** : audit en 5.2 |

Mes lectures de A1 à A5 égalent `lecture.audits` = [] du rapport.

**5.2 Audit A6 de l'issue « puissance perdue » : défaut cherché, non trouvé.**
- **Rejeu d'I02** (`rejeu_diagnostique_v1.py`, 1 000 répétitions, de 05:31:31 à 05:43:27) aux graines de la course, par les
  fonctions du banc dans l'ordre de `juger_v9`, hors de `principal`, rien d'écrit dans le dépôt : **identique au rapport** (381
  promues ; v8 apparié 486 ; 105 perdues ; log W max 41,628880259072275 au bit près ; médiane 1,533 ; 99ᵉ centile 23,422 ; mêmes
  dominants ; médiane v8 2,84).
- **Certificat** : sur les 105 répétitions perdues, l'écart résiduel des membres par morceaux (valeur certifiée moins meilleure
  valeur atteinte, champ `ecart_residuel` de `detail_morceaux_groupe`), maximum sur les 8 instants, va de 0,00041 à 0,000999 nat :
  toutes sous `TOLERANCE_GROUPE` = 10⁻³ (`pole/nul_v9.py`, ligne 108). Richesse « optimiste » où chaque membre par morceaux prend sa valeur atteinte (borne
  basse du vrai maximum de vraisemblance) : **les 105 restent non promues** (log W optimiste maximal 2,9176 < 2,9957). La perte d'I02
  est donc une propriété du nul v9 lui-même (vraisemblance maximale de ses membres à seuil), pas un relâchement du calcul.
  Reconstruction de log W v9 depuis le numérateur, le dénominateur du v8 apparié et les valeurs par morceaux : écart ≤ 5,0·10⁻⁷
  (arrondi de la trajectoire).
- **Mécanisme** : sous v9, le membre dominant final des 105 perdues est un membre à seuil dans 104 cas (`seuil:z1` 59, `seuil:z0` 45,
  `ajuste_log:archive:S2` 1), et sur toute la ligne 752/1 000 : c'est le mécanisme que le texte décrit (section 3 et P4 : un morceau
  coupé sur un trait suit en partie l'autre signe par les survivantes). Les perdues étaient pour la plupart juste au-dessus du
  seuil sous le v8 (avance de log W v8 max sur log 20 : minimum 0,007, quartiles 0,51 / 1,23 / 2,53, maximum 11,16) ; sous v9 leur
  log W max va de −1,46 à 2,917.
- **Ordre de grandeur attendu** : perte 0,105 contre 0,11 à la lecture L3 (100 répétitions, autres graines) et [0,06 ; 0,17]
  prédits (P4) : ni pire ni meilleure qu'annoncé.
- Conclusion de fait : je n'ai trouvé aucun défaut du code ni du banc derrière « puissance perdue » ; la course, l'issue et sa
  cause sont celles qu'annonçaient P4 et P7.

**5.3 « Trop beau » : ce que j'ai regardé.**
- **Les 18 zéros fatals.** 15 sont des zéros par construction, dits comme tels (P1a : « sous α, par construction ») : log W jamais
  positif (maximum −3,1·10⁻¹⁰) ; M01, M02, M06 et M07 (mondes membres exacts du nul, bruit nul) frôlent 0 par-dessous à 2·10⁻⁹
  près, M03 à M05 (bruit ou mélanges) restent plus bas : c'est ce qu'on attend d'une loi membre de la famille, comme T02 et T04 sous
  le v8 (−5·10⁻⁶). T05s et T09g : par construction à la marge de Newton près, dit (P1b) ; écart maximal −0,0058, la réserve
  log-linéaire n'est pas éprouvée au-delà. **T12a n'est pas un zéro par construction du nul** : rejeu de T12a (1 000 répétitions, de
  05:31:31 à 05:49:10), **identique au rapport** (0 promue ; log W max 3,1743644310620596 au bit près ; médiane −4,15 ; 99ᵉ centile
  0,626 ; mêmes dominants ; v8 apparié 0 promue, médiane −3,548). Deux répétitions sur 1 000 franchissent log 20 sous v9 (r = 613 :
  3,174 à t = 50, puis −14,2 à t = 200, gain final −0,071 sur `ajuste_log:AB` ; r = 716 : 3,026 à t = 50, gain −0,032 sur
  `morceaux:seuil:z0`), toutes deux arrêtées par la marge ; sous le v8 apparié, quatre (r = 127, 180, 613, 716), aucune promue. Le
  meilleur gain final de toute la ligne est −0,0048 (marge 0,02) : **la marge n'est jamais atteinte**, si bien que le zéro de T12a
  vient de la marge des filles autant que de Ville. Sans la marge : 2/1 000 franchissements, borne haute 0,63 %, sous α et sous P1c.
  Le texte dit T12a « hors classe ; le monde est au nul (Ville) » et met la marge dans la définition de la promotion (section 6),
  mais ne dit pas que la marge porte ce zéro (réserve 6, même réserve R1 que le verdict du v8).
- **Le banc a des dents sur la classe nouvelle** : sans les membres par morceaux, le même scénario promeut M01 à 98,6 %, M02 à 97,2 %,
  M03 96,9 %, M04 89,7 %, M06 94,9 % ; M05 (43,3 %) et M07 (57,3 %) moins, parce qu'une part de leurs mondes est presque dans la
  classe du v8 (M05 quand les deux poids sont proches) ou montre peu d'instances au-delà du seuil (M07, seuil dans [1,5 ; 2,5]).
  Sur les lignes M, le refus vient bien des membres par morceaux (A5, de 912 à 1 000 sur 1 000).
- **Les dominants des lignes linéaires** sont des membres par morceaux (par exemple T01 : 987 sur 1 000), et leurs log W max sont
  plus bas que sous le v8 (−0,05 à −0,99 contre −5·10⁻⁶ dans la course du v8) : la famille par morceaux contient le membre linéaire
  (même mélange sur chaque morceau), donc elle l'égale au moins et le dépasse par surajustement ; ordre de grandeur de la lecture L4
  (décalage médian T17s 0,35, T04 2,47 nats). Rien d'anormal.
- **Toutes les prédictions tenues (31 sous-prédictions)** : elles ont été écrites après les lectures L1 à L5, même code, autres
  graines (déclaré, sections 4 et 10) ; leur réussite était attendue et n'ajoute aucune preuve. Contre la lecture L3 (100
  répétitions), les écarts restent sous deux erreurs types de L3 (les plus grands : T12b 0,77 → 0,84 ; H02 0,21 → 0,145) : ni copie,
  ni dérive.
- **Zéro répétition gagnée sur 30 lignes** : par construction (garde de monotonie, arrêt sinon), dit (section 6).
- Déterminisme et intégrité : deux lignes entières reproduites au bit près, malgré la charge concurrente de la course et du rejeu.

**5.4 « Trop décevant ».** L'issue est celle que P7 annonçait, sous une marge (a) choisie en sachant qu'elle prédisait « puissance
perdue » (annexe A : la marge est le prix acceptable, non l'issue visée, R3) ; ce n'est pas un « non concluant par défaut de
conception ». La perte établie est sur l'interaction faible (puissance v8 0,486) ; sur la loi neuve forte (fraîche neuve), le prix est
0,006.

**5.5 Lignes à 0 « par construction » : toutes dites, sauf une part de T12a.** Zéros du rapport : les 18 fatales sous v9 (15 par
construction, dit P1a ; T05s et T09g à la marge de Newton près, dit P1b ; T12a : Ville et marge, la part de la marge non dite,
réserve 6) ; sous le v8 apparié, les 11 lignes du v8 (classes du v8, dites dans la validation du v8 et en section 3 ; T12a : marge) ;
aucune répétition gagnée (dit, section 6). Aucune autre ligne à 0 : la plus basse des lignes mesurées est T07 (9/1 000).

## 6. Sortie d'erreur (`sortie-erreur-course-v1.txt`)

- **Contenu** : 2 056 octets, 110 lignes, un seul objet JSON (clés `mode`, `issue`, `fatales`, `artefact`, `perte_de_puissance`,
  `audits`, `taux`, `taux_v8_apparie`, `pertes`, `duree_s`). Reconstruit depuis le rapport scellé, c'est **à l'octet** le résumé que
  `principal` imprime sur la **sortie standard** en fin de course complète (lignes 567 à 571, sans `file=sys.stderr` ;
  `sortie_attendue_v1.py`, sortie `sortie-sortie-attendue-v1.txt`).
- **Ce qu'elle ne contient pas** : aucun avertissement, aucun « refus : » (ligne 536, flux d'erreur), aucun rapport d'arrêt (ligne
  557, flux d'erreur : `ArretDuree`, `MonotonieViolee`, erreur, richesse non finie), aucune trace d'exception.
- **Durée** : `duree_s` 6 020,8 s, égale au rapport.
- **Ce que cela change** : rien. Le contenu égale les champs du rapport ; l'issue ne dépend pas de ce fichier. Seul point : le nom
  « flux d'erreur » est inexact, et la redirection du lancement n'est pas consignée (« journal `nohup` ») ; si le flux d'erreur y était
  joint, il était vide ; sinon il n'est pas conservé (réserve 3).

## 7. Portée : ce que l'issue permet et ne permet pas de dire publiquement

**Ce qu'elle établit, si le verdict la retient** (sur les mondes synthétiques du banc : 3 issues, 2 traits gaussiens, 2
sous-populations ; filles : 50 tirages de calibrage puis 200 ; fiches sans parent : 200 tirages ; lecture aux instants 25 à 200 ;
α = 0,05 ; 1 000 répétitions par ligne) : le nul v9 ne promeut aucune des 18 lignes fatales (0/1 000 chacune, borne haute 0,30 %, 0,59 %
au niveau de Holm le plus strict), dont les 7 tricheurs par morceaux et le monde W2 (M01) ; le banc voit le trou du v8 (M01 98,6 %,
M02 97,2 % sous le v8 apparié) et l'artefact T01|v1 (41,1 %) ; le prix en puissance appariée est 10,5 points sur l'interaction
faible I02 (borne basse 8,9 %, au-dessus de la marge de 5 points), 0,6 point sur la loi neuve forte (fraîche neuve, sous la marge),
non établi par rapport à la marge sur fille neuve (3,8), I01 (4,3) et F03 (4,6).

**Ce qu'elle ne permet pas** :
- **Ni « confirmé », ni « validé sur la classe du banc »** : cette mention appartient à l'issue « confirmé » (section 7, issue 4).
  Au premier étage de « puissance perdue », le texte dit seulement « le v9 ferme les lignes, au prix mesuré », et le choix revient à
  Lazar : accepter le prix (le v9 devient le nul du juge, sa description publique dit le prix) ou chercher un nul moins coûteux
  (version nouvelle).
- **Aucune revendication publique avant la réponse explicite de Lazar sur le sens de « rien au-delà de l'archive »** (section 2,
  dernier point ; section 14, point 2 : nœud « revendication », sans défaut ; une réponse contraire, bruit propre à chaque morceau,
  arrête ce texte et ouvre un nul v10). Le sens « bruit commun » n'est qu'un défaut de conception (R-1278, « à confirmer par Lazar
  sous 48 h ») ; je ne trouve aucune réponse explicite dans `registres/decisions.md` (recherche de « rien au-delà », « au-delà de
  l'archive », « bruit commun », « escalier aveugle », « nul v10 », à 05:51). La publication est en outre un nœud de Lazar ; rien
  n'est publié (dossier de sortie non committé, R-1300).
- **Aucune mise en production** : le nul de production reste le v8 (`pole/cycle.py` inchangé, dans les 14 gelés). Il faudrait,
  dans l'ordre du texte : prix accepté par Lazar, sens confirmé, entrée v9 du cycle dans un fichier neuf, décision de Lazar (nœud
  « modification d'hypothèse ou de revendication »).
- **Rien hors de la classe du banc** (section 11) : ni la banque réelle, ni la multiplicité entre fiches (règle e-BH, d'après
  Benjamini et Hochberg), ni les autres espaces, ni un proposeur qui lit le juge et reçoit ses verdicts (objet de l'attaque v4), ni
  les mondes avec mémoire, ni les traits non finis ; la réserve de la marge de Newton des membres log-linéaires n'est pas éprouvée
  au-delà des écarts observés (−0,0058).
- **Les lignes mesurées ne disent rien de la validité** et doivent être dites pour ce qu'elles sont : H01 (0,86), H02 (0,145),
  H03 (0,928), H05 (0,09) et T07 (0,009) sont des taux de fausse promotion sur des trous que le nul v9 ne couvre pas ; H04 (0,236) est
  le taux de promotion d'un bruit propre à chaque morceau, neuf selon le sens choisi (à confirmer) ; T12b (0,84) est de la puissance
  sur une nouveauté vraie.
- **T12a** : toute phrase sur la borne de Ville doit dire la marge (réserve 6).

## Réserves (une ligne chacune ; aucune ne change l'issue)

Réserves de cet audit :
1. Code de sortie non capturé (écart déclaré) : déduit 0 du chemin du code et des champs du rapport, non observé ; il ne décide pas (section 5).
2. Section 14, point 6 : essais et mutations non rejoués entre la poussée (23:20:18) et le départ (23:20:38) ; faits avant le scellement sur un code identique et rejoués sur l'arbre scellé pendant la course (mêmes comptes) ; même écart que la réserve R2 du v8.
3. Le fichier « sortie d'erreur » est, à l'octet, la sortie standard du banc (lignes 567 à 571) ; redirection du lancement non consignée ; le flux d'erreur proprement dit est vide s'il y était joint, non conservé sinon.
4. Manifeste sans date ni commit (R9 demande le commit) : structure héritée du banc v8 (`pole/outils.py`, `manifeste`) ; dates par horodatage des fichiers et R-1292, commit par git.
5. Charge concurrente hors du plan (course factice d'A1-v3.1 arrêtée à 00:14, essais et courses exploratoires de la vérification courte, deux commits à 00:56 hors des 14 fichiers) : temps seulement ; T12a et I02 reproduits au bit près.
6. T12a : le zéro vient autant de la marge des filles (jamais atteinte, gain maximal −0,0048) que de Ville (2 franchissements sur 1 000, tous arrêtés par la marge) ; ni le rapport ni le texte ne le disent ; à écrire partout où T12a est citée (réserve R1 du v8).
7. A6 est déclenché par l'issue et n'est pas calculé par le code (`issue_suspendue_par_audit` ne couvre que A1 à A5) : deux lectures du statut avant cet audit, même issue après (section 3).
8. Constante morte `SEUIL_ECART_RESIDUEL` (« audit A7 », ligne 106 du banc gelé) : aucun audit A7 au texte ni au code, et l'écart résiduel des certificats n'est pas rapporté ; mesuré ici sur les perdues d'I02 (au plus 0,0010 nat).
9. Le champ `lecture.predictions` ne code ni « log W ≤ 10⁻⁶ » (P1a) ni « ≤ +0,25 » (P1b) ; vérifiés à la main sur `log_w_max_max`.
10. Le prix à soumettre dépasse « la ligne nommée » : seule I02 est établie au-dessus de la marge, fraîche neuve dessous, fille neuve, I01 et F03 non jugeables (bornes hautes 0,0495 à 0,0584) ; décision et description publique doivent porter les cinq pertes avec leurs bornes.
11. Mon `git diff` et mon `git status` de lecture, au début, ont rafraîchi le cache `.git/index` du clone (horodaté 05:25:50) ; l'index reste égal à `HEAD`, aucun fichier suivi ni commit changé ; écart à la lettre « aucun fichier existant modifié ».
12. Les deux rejeux diagnostiques utilisent les graines de la course (hors de `principal`, en lecture seule, comme le verdict du v8 et la section 8 pour A5) ; ce n'est pas une course décisive, mais le lecteur du verdict dira si cet usage des graines décisives est admis ici.

Réserves héritées de la vérification courte (portées telles quelles, constat ajouté) :
- VC1. Paragraphe de scellement, « aucun de ces noms n'est lu par le banc v9 » : inexact, le banc appelle `nul_v9.description()` (ligne 541) pour le manifeste seulement (vu dans `reglages.nul`) ; sans effet sur les nombres.
- VC2. Paragraphe de scellement, « (section 4) » pour la graine : la règle est en section 5 ; renvoi faux, sans effet.
- VC3. Garde de monotonie : le cas « promotion sous v9 sans promotion sous v8 » n'est jamais éprouvé seul ; sans effet ici (aucune répétition gagnée sur 30 lignes, recompté).
- VC4. Gardes sans essai sur un artefact (richesse non finie, arguments < 1, durée ≤ 0, entropie < 2⁶⁴) ; titre de la section 9 trop large ; sans effet (course complète, richesses finies, arguments du plan).
- VC5. Essais de la description publique : contenu épinglé en partie seulement ; sans effet sur la course.
- VC6. Artefact de durée : « rien d'écrit » vérifié sur le seul rapport ; sans effet.
- VC7. Statut du texte, « trois fichiers existants modifiés et seulement eux » : `516feca` modifie aussi quatre fichiers de l'attaque v4, hors de la fermeture du banc ; sans effet.
- VC8. Fragments de G1 à G5, L1, L2 et C5 « repris à l'identique » du script du contre-lecteur : non vérifiables (script disparu) ; sans effet.

## Scripts, sorties et empreintes (`/home/claude/scratch/audit-nul-v9/`, sha256)

Tous lancés par `nice -n 10 python3 -I -B` ; aucun ne lit autre chose que les pièces citées, aucun n'écrit hors de ce dossier.

```
276d623661f81910d1075e7188553c876db8963e7c7a2243032dbbe45d33eef9  recalcul_v1.py
2134f15840b00626747d65e7e2e9805750c74a84c01e061ac3339b6d3a2077ba  sortie-recalcul-v1.txt
cead331bb0c0b62a51d4a4b973bc056aa0a1fde2098e470d0227e5880925eefb  conformite_v1.py
ba6bb91567d328d88a8bcf07ba41ca12bf977a7594e2512d2c6bc607bd509465  sortie-conformite-v1.txt
7361de8bcb54992698913b9fe7bed94dcb57c8f64643380aabb60b1dfdbe65ef  sortie_attendue_v1.py
b9c48251ad10a6ccd6d83ba90178fa09b31d1aea68ceae852b083e0624d8c735  sortie-sortie-attendue-v1.txt
f66a44d6d3ec77314ca2932daa4c7deacaf51b92d5bc619127e1807cf2d95da7  rejeu_diagnostique_v1.py
fcc3448e8890a8e7b2f97b087ccec111a51ad4deeb265a09a6f6bfe20eb36740  rejeu-t12a/rejeu-t12a-v9.json
fd83f9b29d82c55d18a3a2cf826564979ec5f9b1e7da428e70cbf04171341572  rejeu-t12a/sortie.txt
899865f29d08e60621b94e90d2fbefa5d1bb91047c7a7c12dde8ea9333edb3b9  rejeu-i02/rejeu-i02-v9.json
60faba55f8bf86af0208af1d4e547d3bb7c4f843d8b32feafa572c2136798b31  rejeu-i02/sortie.txt
dbfcd6528b01ea7350eb03087071f2790152937c324a3221078ac08a7946562e  rejeu-depart.txt
4dd7adb56dae3ff3aa83a84a8b28d0c569315500344df15b1806bfc4e3a6f1fa  complements_rejeu_v1.py
6210eaa659ec8e67be618a649ad420292ec11406444d16d99f4b07ef93b77a23  sortie-complements-rejeu-v1.txt
e5907a5ffbdb56b12022ee4737ed981f2472db78277589c05674dfa808046dbf  empreintes-arbre.txt
e5907a5ffbdb56b12022ee4737ed981f2472db78277589c05674dfa808046dbf  empreintes-66dbcf1.txt
e5907a5ffbdb56b12022ee4737ed981f2472db78277589c05674dfa808046dbf  empreintes-bloc12.txt
39ea5cdbaab313d6e3cb7c676c8771c414f71252a45149beafafdb00e3abfa92  essai-fumee/t12a-3.json
22b4958c5fc0b5dc25e7f6fe6f9cc63c63abb84a592649884f8d1d1a3149f449  essai-fumee/i02-3.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  repere-avant-rejeu.txt
```

Rôles : `recalcul_v1.py`, section 2 à 4 ; `conformite_v1.py`, section 1 ; `sortie_attendue_v1.py`, section 6 ;
`rejeu_diagnostique_v1.py` et `complements_rejeu_v1.py`, section 5 (le premier rejoue une ligne v9 aux graines de la course et
compare au rapport ; `essai-fumee/` : son essai sur trois répétitions) ; `empreintes-*.txt` : les 14 empreintes sur l'arbre, au
commit `66dbcf1` et dans le bloc de la section 12 (trois fichiers identiques) ; `repere-avant-rejeu.txt` : fichier vide, repère de
temps pour la recherche des fichiers écrits.

## Ce que j'ai fait et pas fait

- Fait : lecture des pièces ci-dessus ; vérification des empreintes ; recalculs ; deux rejeux diagnostiques complets (T12a, I02) et
  un essai de trois répétitions, tous hors de `principal`, sans dossier de sortie du banc, sans lecture gelée.
- Pas fait : aucune course du banc, ni décisive ni exploratoire ; aucun commit, aucun `.sha256`, aucun `git fetch`, `checkout` ou
  `stash` ; aucun fichier existant modifié (sauf le cache `.git/index`, réserve 11) ; rien sous `donnees/` ; aucun réseau, aucun
  modèle. Après les rejeux, aucun fichier neuf ou modifié sous `orchestrator/`, sous `resultats/banc-tricheurs-v9-validation-v1/` ni
  dans ce dossier de réception (recherche par date contre le repère ; les fichiers récents trouvés ailleurs dans les deux dépôts
  sont ceux d'autres sessions) ; les 14 fichiers gelés revérifiés conformes au bloc à 05:50.
- Seul fichier écrit hors du bloc-notes : celui-ci. Il ne porte pas sa propre empreinte : elle est donnée avec sa remise.

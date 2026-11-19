# Vérification courte du différentiel v1 → v2 — phase 0 de P1 et de P2, organisme d'idéation

**Texte v2 vérifié : `preenregistrement-phase0-p1-p2-v2.md`, sha256 recalculé `bff8744edfb80201f0c97c58d54d8f409830707186613b8df2e96ecadd392d0a`, conforme à l'empreinte attendue et à son compagnon ; commit 80f2851e.**

- Vérificateur : modèle J, sous-agent neuf, d'un autre modèle que le développeur (modèle I) ; n'a écrit ni la contre-lecture de la v1 ni aucune autre pièce de cette tâche. Note écrite à 2026-11-18T05:37:48Z (`date -u` dans la commande d'écriture) ; contrôles faits depuis 2026-11-18T05:33:49Z.
- Rien n'a été exécuté sur la configuration du préenregistrement : les gardes de lancement ont été essayées en mode réel avec un arrêt forcé avant tout calcul (les fonctions qui créent le dossier de sortie, chargent les sources et jouent P1 remplacées par une sentinelle dans mon programme jetable). Aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau. Aucun fichier existant modifié ; copies altérées dans un dossier jetable hors dépôt. Contenu des sources non ouvert.
- Cette pièce est une vérification du différentiel, pas une contre-lecture entière du texte v2 ; elle n'est pas un rapport à passer au lanceur (qui la refuserait : son verdict n'est pas « scellable »).

## Verdict

**Jouable sous consignes.** Aucun constat bloquant ni majeur. Les cinq constats majeurs et les dix mineurs de la contre-lecture sont portés ; la garde de contre-lecture refuse ce qu'elle doit refuser ; les 53 essais passent ; un seul seuil a bougé (Bonferroni sur six au lieu de trois), déclaré, mais dans le sens qui facilite le verdict favorable (V-1).

Consignes :
1. **Un seul lancement admis** : la commande écrite au texte v2 (lanceur v2, rapport `contre-lecture-phase0-p1-p2-v1.md`, empreinte 48c1647b…996e). Aucun autre rapport n'est passé au lanceur ; le lanceur v1 n'est jamais lancé (il accepte encore ce rapport : V-3).
2. **Pas de mode d'essai à l'échelle avant le lancement réel** (une configuration qui ne diffère que par la racine des graines passe la garde du mode d'essai : V-6).
3. **Le lecteur du verdict (R13)** vérifie au manifeste : `essai` faux ; contre-lecture d'empreinte 48c1647b…996e et de verdict « scellable après corrections » ; empreintes du code égales à celles des compagnons du commit 80f2851e. Pour chaque comparaison de la famille A/A et chaque statistique, il dit si l'intervalle à 95 % (`ic95`, présent dans la sortie) contient 0 : si un « contient 0 » ne tient que par l'intervalle corrigé, c'est un cas limite à écrire, avec la mention que la correction est passée de trois à six entre v1 et v2 (V-1).
4. Le rapport de résultat dit que le texte v2 n'a reçu qu'une vérification de différentiel (R2 est tenue par la contre-lecture de la v1 plus cette pièce), et reprend V-4 (ce que la phase 0 dit de l'ordre : le branchement, rien d'autre).

## Contrôles faits

1. **Sceaux** (`controle_ia.scellement verifier`) : huit sur huit conformes — contre-lecture 48c1647b…, texte v2 bff8744e…, texte v1 8c8240fa…, lanceur v2 da4312e7…, questionneurs v2 28705030…, essais v2 d1f5eb68…, `mondes_reponses_p1p2_v1.py` 2c80a833… et `mesure_forme_p2_v1.py` b3da53aa… (ces deux-là égales aux empreintes relevées par la contre-lecture : inchangés à l'octet).
2. **Différentiel du texte** : comparaison mot à mot v1 → v2 (`git diff --no-index --word-diff`), chaque fragment retiré ou ajouté rapproché des points 1 à 15 du différentiel. **Différentiel du code** : `diff -u` des questionneurs (un seul déplacement, `exiger_booleen` hors du bloc des refus, plus version et en-tête) et du lanceur ; sources des fonctions comparées une à une : `tient_ordre`, `tient_aa`, `phase_p1`, `phase_p2`, `probas_organisme`, `lois_de_reference_v67`, `exiger_code_scelle`, `exiger_preenregistrement`, `exiger_bloc_effort`, `empreinte_bloc_effort` identiques ; `lire_p1` ne diffère que par `len(FAMILLE_AA)` → `c["bonferroni_aa"]`. Essais : les 46 noms de la v1 sont tous présents en v2, plus 7 ; aucune affirmation retirée sans remplacement (`lectures == []` remplacée par la lecture attendue, C-1).
3. **Seuils** : `CONFIG` v1 et v2 comparées clé à clé : seule différence, `p1.bonferroni_aa` (absente → 6). Familles, bras, sources, graines (racine, noms de tâches), fraction de largeur 0,5, seuil de fuite 0,05, seuil d'audit 0,95, seuil de P2 0,25, quota 2 et plage {1, 2, 3}, 200 mondes, 65 536 lois, T = 16, 10 000 rééchantillonnages : identiques. Le bloc JSON du texte est égal à `bloc_effort(CONFIG)` et son empreinte d156f3e0…0f0a est celle que le lanceur recalcule.
4. **Essais relancés** : `python3 -B -m pytest -q -p no:cacheprovider test_phase0_p1p2_v2.py` : **53 réussis** (python 3.13.18, numpy 2.5.3) ; aucun fichier écrit dans le dossier (22 entrées avant et après). Le validateur `controle_ia.prereg.problemes` ne rend plus aucun problème sur le texte v2.
5. **Gardes essayées par moi** (mode réel, arrêt forcé avant tout calcul ; « accepté » = toutes les gardes de lancement franchies) :

| essai | attendu | observé |
|---|---|---|
| A — texte v2, contre-lecture versée | accepté | accepté (texte, bloc, contre-lecture, code scellé, évaluateur, trois sources : présents et conformes à cette heure) |
| B — contre-lecture omise | refus | code 2 |
| C — copie de la contre-lecture, verdict changé en « Non scellable », compagnon refait | refus | code 2, « verdict de contre-lecture refusé : non scellable » |
| C2 — la même, citant en plus l'empreinte du texte v2 | refus | code 2, même motif |
| D — copie altérée d'un octet, verdict gardé, compagnon refait | refus | code 2, empreinte ≠ attendue |
| E — copie au verdict changé en « Scellable », qui ne cite pas le texte v2 | refus | code 2 |
| F — rapport fabriqué, scellé, « Scellable », qui cite le texte v2 | (hors garde) | **accepté** (V-2) |
| F2 — « Scellable sous réserve » | refus | code 2 |
| F3 — première ligne « **Scellable** ? Non : non scellable, trois bloquants » citant le texte v2 | refus | **accepté** (V-2) |
| G — titre « ## Verdict » retiré | refus | code 2 |
| H — copie exacte sans compagnon | refus | code 2 |
| I — texte v1 présenté au lanceur v2 | refus | code 2 (empreinte ≠ attendue) |
| J — texte v2 altéré (« 0,5 × » → « 0,9 × »), compagnon refait | refus | code 2 |
| K — garde de contre-lecture appelée avec le texte v1 | refus | refus, « scellable après corrections de ce texte même : corrections non portées » |
| L — texte v2 sans le titre du différentiel | refus | refus |
| M — garde du **lanceur v1** avec la contre-lecture versée et le texte v1 | — | **accepté** (V-3) |
| N, O — évaluateur d'empreinte fausse, évaluateur absent | refus | refus écrit |

Aucun dossier de sortie créé dans aucun essai.

## Constats de la contre-lecture, un à un

| constat | porté ? | preuve |
|---|---|---|
| C-1 | **conforme au couple** | texte, table P2 : branche fermée réécrite mot pour mot, plus une phrase commune aux deux branches sur la loi de tirage choisie par l'auteur ; `decision_p2` : lecture sur la part observée écrite hors de `if not ferme` ; essai du cas « fermé avec part observée au-dessus du quantile 95 % » présent et réussi |
| C-2 | **conforme** | `EMPREINTE_EVALUATEUR`, `exiger_fichier` appelé pour l'évaluateur et pour chaque source avant `dossier_neuf` ; ligne de la liste d'arrêt mot pour mot ; essais N, O |
| C-3 | **porté, forme réduite ; écart justifié et déclaré (écart 12)** | la contre-lecture demandait de réduire la décision, la borne et le libellé du verdict, non d'ajouter un questionneur sensible : les trois textes proposés sont repris (décision : sens repris et renforcé ; borne et libellé : mot pour mot, dans le texte et dans `verdict_p1` et `BORNE_P1`). **La borne ne dit plus rien de l'effet de l'ordre** : elle dit « sans défaut de branchement » et « l'effet de l'ordre sur un proposeur réel n'est pas mesuré ici » ; « sans effet mesurable » a disparu du texte et du code (recherché). Réserve de rédaction : V-4 |
| C-4 | **conforme** | chiffres déclarés dans « Ce qui a été vu » (0,2203 et 0,2202 contre 0,0921 ; 0,0990, 0,1182 et 0,0459 contre 0,1208 ; largeur nulle pour les médianes de la bissection), égaux à ceux de la contre-lecture et affirmés par l'essai relancé ; phrase « la famille A/A entière ne tient donc pas sur les petits mondes d'essai » présente ; confiance 65 % → ≈ 30 % avec sa raison ; **fraction de largeur inchangée (0,5)**, dans le texte, dans `CONFIG` et désormais dans le bloc gelé |
| C-5 | **porté, écart au couple justifié** | le couple proposait une ligne exacte « Verdict … : scellable » ; le rapport versé, scellé, ne la porte pas et ne peut être réécrit : la garde lit le verdict sous « ## Verdict » et n'accepte « scellable après corrections » que pour le rapport d'empreinte attendue, relisant le texte v1 attendu, le texte lancé citant les deux et portant le différentiel. Essais C, C2, D, E, G, H, I, K, L : refus. Limites : V-2 |
| m-1 | conforme (déclaration) | C-P1-4, écart 7, borne |
| m-2 | conforme | seuils dans le bloc (essai : un seuil changé change l'empreinte) ; mode d'essai refusé sur la configuration réelle ; limite V-6 |
| m-3 | porté par la seconde option proposée (Bonferroni sur six) | V-1 |
| m-4 | conforme | `etat_git` ; essai réussi |
| m-5 | conforme | absence = refus écrit ; emplacement inchangé, déclaré |
| m-6 | porté, à une parenthèse près | V-5 |
| m-7 | conforme | section « Contre-lecture » avec les deux empreintes ; validateur muet |
| m-8 | conforme | seul changement des questionneurs ; essai sous les deux règles |
| m-9 | conforme | essai des trois gardes |
| m-10 | conforme (déclaration) | hypothèse H-P1 |

## Constats

**V-1 (moyen) — le seul seuil qui bouge va dans le sens favorable, et n'est pas nommé comme un assouplissement.** L'intervalle corrigé du « contient 0 » de C-P1-2 passe du niveau 1 − 0,05/3 au niveau 1 − 0,05/6 : il s'élargit, donc contient 0 plus facilement, et un échec de ce demi-critère (verdict « instrument non discriminant (A/A) » ou « ordre mal branché ») devient moins probable. Le changement est déclaré (différentiel, points 6 et 12 ; bloc gelé) et vient de m-3, qui laissait le choix entre corriger la phrase du taux d'erreur et passer à six ; l'auteur a pris l'option qui desserre, en la présentant comme une correction du taux visé (ce qu'elle est aussi : six intervalles à 0,05 au total). Le demi-critère de largeur (intervalle à 95 %, fraction 0,5) n'est pas touché, et c'est lui qui échoue sur les petits mondes. Pas de reprise demandée ; consigne 3.

**V-2 (mineur) — limites de la garde de contre-lecture.** (a) Elle vérifie que le texte lancé cite le rapport et le texte v1 et porte un titre de différentiel, pas que les corrections y sont : c'est la présente vérification qui le dit, et le lanceur ne l'exige pas (le texte l'écrit : « aucune contre-lecture nouvelle n'est exigée »). (b) La branche « scellable » n'est ancrée sur aucune empreinte de rapport : tout fichier scellé qui cite le texte v2 et ouvre son verdict par « Scellable » passe (essai F), comme en v1. (c) Le verdict lu est le passage en gras qui ouvre la ligne : « **Scellable** ? Non : non scellable » est lu « scellable » (essai F3). Sans effet si la consigne 1 est tenue.

**V-3 (mineur) — le lanceur v1 reste lançable.** Sa garde accepte la contre-lecture versée (essai M) et ses autres gardes portent sur des pièces toujours en place : rien de mécanique n'empêche un lancement sous le texte v1. Le texte v2 l'interdit par écrit seulement. Consigne 1.

**V-4 (mineur) — rédaction de C-3 : une phrase se contredit et une affirmation neuve n'est pas démontrée.** Le plan d'analyse écrit « aucun questionneur factice de cette phase n'est sensible à l'ordre de présentation par construction » puis, dans la même parenthèse, « seul le répéteur dépend de l'ordre des traits » (et la métrique : « le répéteur et le disperseur suivent l'ordre présenté des traits »). L'écart 12 ajoute que « l'effet moyen de l'ordre est nul par construction pour tout questionneur factice » : la contre-lecture disait le répéteur sensible, et cet argument de symétrie n'est ni essayé ni chiffré. Aucun critère n'en dépend (l'ordre du répéteur est rapporté sans décision) et la borne reste correcte ; à lire comme « aucun des deux questionneurs du critère n'est sensible ».

**V-5 (mineur) — la borne du code n'est pas tout à fait « en entier ».** `BORNE_P1` omet la parenthèse qui explique la carte centrale (« un questionneur qui n'apprend rien … resserre à tort ») ; tout le reste y est, y compris les deux « rien sur » qui manquaient en v1. Sens conservé.

**V-6 (mineur) — le refus du mode d'essai compare l'empreinte du bloc.** Une configuration d'essai identique à la vraie sauf la racine des graines (ou un seul réglage) passe : elle montrerait le comportement à l'échelle avant le lancement réel. La sortie serait marquée « essai » et le lecteur R13 la refuse ; consigne 2.

**V-7 (mineur) — retraits non listés au différentiel**, aucun ne touchant un critère : (a) plan d'analyse, « les deux parties A/A d'un proposeur ont des ordres différents » (engagement de la v1 pour la phase 1 ; le point 7 ne liste que deux retraits ; le texte de remplacement proposé par la contre-lecture l'omettait déjà, et renvoie le dessin au préenregistrement de la phase 1) ; (b) en-tête, « personne d'autre n'écrit dans ce dossier » et « des quatre modules et des essais du dossier » ; (c) liste du code, les descriptions entre parenthèses des modules et « noms neufs » ; (d) plan d'analyse, « rapporté tel quel » après le verdict d'ordre ; (e) section « Contre-lecture », la liste des fichiers à donner au contre-lecteur et la phrase sur le traitement des remarques (remplacées par le traitement lui-même, point 15).

## Ce qui a été cherché et trouvé juste

- Aucun autre changement de code que ceux du point 16 à 18 du différentiel ; les deux modules réemployés sont inchangés à l'octet ; les règles de décision (`tient_ordre`, `tient_aa`) et le déroulement de P1 et de P2 sont identiques au caractère près.
- Aucun critère de P1 ni de P2 assoupli hors V-1 ; deux durcissements : seuils dans le bloc gelé, réserve écrite dans la branche fermée de P2.
- Le chiffre « facteur ≈ 2,4 » de la prédiction (0,2203 / 0,0921 = 2,39) est juste.

## Ce que je n'ai pas vérifié

- Le comportement à l'échelle (rien n'y a été joué) ; le contenu des sources ; ce que l'auteur avait vu en fixant les seuils (déclarations) ; l'argument de symétrie de l'écart 12 (V-4) ; le reste du texte v2 hors du différentiel, tenu pour inchangé sur la foi de la comparaison mot à mot.

## Incidents

Aucun refus de permission, de crochet ou de classifieur. Un dossier jetable hors dépôt (copies altérées, un programme d'essai des gardes, non versés).

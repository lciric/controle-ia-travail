# Verdict du lecteur neuf sur l'issue du pilote MR-2 (procédure v14) — v1

Lecteur neuf, modèle C ; texte scellé et code du pilote : modèle A (R13, R-2731). Heures (`date -u`) : début 15:33:59Z, écriture 15:37Z.
Consigne appliquée : `consigne-lecteur-issue-pilote-v14-v7.md`, `b97062809d9ffe24ae9bc13445aa431048d91c2618d96ee0e57f646b56ede95c` (égale à son compagnon).

## Verdict

**ARRÊT au point 0 de la consigne. Aucune issue lue, pas même P-0.** Ligne de la table appliquée : aucune (« Liste d'arrêt » du texte scellé : aucune issue n'est lue après un arrêt).

Cause unique : dans `rapatrie-reel/releve-pilote-v70.json`, le champ `appels_complets_illisibles` vaut **2**, alors que le point 0 exige **0** pour un relevé complet. Tous les autres contrôles d'arrêt et d'empreinte ont été faits et sont conformes (ci-dessous). Je n'ai pas cherché la cause de ces 2 appels ni jugé si l'écart est bénin : la consigne dit « tout écart : arrêt ». Le texte scellé ne mentionne pas ce champ (recherche du mot « illisible » : aucune occurrence) ; la décision sur la nature de l'écart revient à la mère et à Lazar.

## Pièces non ouvertes (respect du point 0)

`rapatrie-reel/lecture-pilote-v70.json` (hors son compagnon) et `remis-au-sous-agent/sortie-lire-non-ouverte.txt` : **jamais ouverts**. `sortie-mesure-pilote-v70.json` : lue seulement pour `hors_corps` (`script_sha256`, `modules_importes`) et `corps.mondes_sha256` ; `corps.regle`, `corps.principale`, `corps.audit_R4`, `corps.appels`, `corps.temoin_positif` : jamais lus. Les contenus des réponses brutes, des corps de relais et des témoins : jamais ouverts (empreintes seulement).

## Contrôles d'arrêt (point 0)

| contrôle | résultat |
|---|---|
| `etat.txt` : `etape=fini`, aucun `arret (A)`, `noeud, machine gardee`, `sortie inattendue` ; `exclus_balayage=` vide | conforme |
| `code-06`, `07`, `08`, `09`, `10-mesurer`, `10-lire`, `11-rapatrier` | tous 0 (aucun code 3) |
| `lancements.jsonl` | une seule ligne, `texte_sha256` = 8aa33014… |
| `liste-rapatriement-pilote-v70.json` : `aucun_monde` | vrai ; aucun `CARTES-partiel.json` |
| relevé : `partiel` | faux |
| relevé : `arret` | null |
| manifeste : `partiel`, `arret` | faux, null |
| **relevé : `appels_complets_illisibles`** | **2 (attendu 0) : ÉCART, ARRÊT** |
| 16 appels : réponse brute et témoin d'isolement scellés | oui (16 + 16, compagnons égaux ; empreintes du relevé égales aux fichiers, y compris corps de relais) |
| dépense : `journal_au_dessus_du_pire_cas` | 0 pour chaque proposeur |
| dépense : parts non atteintes (relevé et journal) | fable52 10,019552 < 12 ; opus55 1,057336 < 8 ; argon 2,47162 < 9,36 ; astra 1,67175 < 9,36 ; machine 0,082018 < 3 : conforme |

## Empreintes (point 1) : toutes conformes

- Texte scellé relu (git `refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1`) : `8aa33014667da569ec934459d7bc1b1f6b54efa5c2145a6e5bdce5f7fa74603e` = attendu.
- Compagnons égaux : `CARTES.json`, `lecture-pilote-v70.json` (compagnon seulement vérifié, contenu non lu), `manifeste`, `mesure-pilote-v70.json`, `releve`, `sortie-mesure` ; 48 compagnons des dossiers `monde-N/PROPOSEUR/` égaux.
- `secret-sha256.txt` : `abe4e0b8…cdddec` = registre. `phrase-sha256.txt` : `c2fc355f…5792df` = registre. `engagement-mondes.json` : H `f5f9c487…8e36` et S1 à S4 (`20b662a4…`, `49c5a286…`, `9e21c2e9…`, `e05c2547…`, dans l'ordre) = registre (`b3eb5a21…`).
- Manifeste : `controles.mondes.fichier_mondes_sha256` = H ; `mondes_sha256` {1..4} = S1..S4. Sortie de mesure : `corps.mondes_sha256` = {S1..S4} comme ensemble.
- `programme_sha256` (liaison) et `hors_corps.script_sha256` = `676d5f37…8365`. `cartes_sha256` de la liaison = empreinte de `CARTES.json` `585c5f00…fa1fe60`.
- `hors_corps.modules_importes` : 13 couples = les 13 lignes `orchestrator/mr2_v68/…` du bloc gelé (comparaison comme ensemble : égaux).
- Sommet `69275b74` de la branche de sortie : non vérifiable par moi (copie sans accès au dépôt de sortie) ; non fait, cause écrite. Annoté, sans effet sur l'arrêt.
- Programme de dépense : `9866e611d7997c32eba82cf308dbed1c2ccf184992f106811b2623357dc88643` (git `2f7acc1d`, égal à son compagnon). Sortie de dépense : `53c72308bb30adcce5602ad18b47f2e7325a22a295264c143ed52ff46f349ce2` (égale à son compagnon).

## Mesure (point 2)

Faite une fois (`code-10-mesurer.txt` = 0 ; journal : 12:59:41Z à 12:59:54Z, `sortie_sha256` `b206639e…` = la sortie remise). Pas d'exception ni de refus nommé. Non refaite.

## Dépense rapprochée (point 4)

Recoupée par lecture : somme des `cout_usd` des 16 appels du relevé = somme des journaux des relais, par fournisseur, à zéro d'écart (fable52 10,019552 ; opus55 1,057336 ; argon 2,47162 ; astra 1,67175 ; total des quatre 15,220258 USD). Avec la machine 0,082018 et les autres lignes déclarées (0,001164 et 0,074757, arguments `--autre` que je ne puis vérifier) : total 15,378197 USD, égal au fichier de dépense. π1 (fable52 + opus55) = 11,076888 USD contre 20 : sous la ligne. π2 (argon, astra, machine, autres) = 4,301309 USD contre 21,72 : sous la ligne. Code de sortie 3 du programme de dépense : non donné par la mère ; déduit de `sous_la_part` (tous vrais), `pi1_sous_la_ligne` et `pi2_sous_la_ligne` (vrais) : pas de code 3. La console fait foi (R-2803) ; aucun coût recalculé aux prix.

## Points non faits, avec cause

- Points 3 (issue), 5 (autres exclusions), 7 (audit de symétrie R4) : **non faits : arrêt au point 0**. Audit R4 : ni déclenché ni non déclenché, aucune lecture de la sortie de mesure.
- Tirage de l'audit : non fait (arrêt) ; version de `numpy` du lecteur 2.4.6, sans emploi.

## Phrases du point 6

- « P_VUE = 0,25 supposée, non mesurée ».
- « p_c ne vaut que pour ce gabarit ».
- Taux d'erreur écrits d'avance dans le texte scellé : course refusée à tort 0,20 si p vaut 0,02 ; course permise à tort 0,26 si p vaut 0,051 (0,075 à 0,075 ; 0,017 à 0,10) ; à 12 et 14 appels répondus : refus à 0,02 de 0,22 et 0,21, permise à tort à 0,051 de 0,29 et 0,27, à 0,075 de 0,10 et 0,09 ; « entre 0,03 et 0,05, le pilote ne décide rien de fiable (permise de 0,60 à 0,26) ».
- La phrase sur l'issue P-2 favorable : sans objet (aucune issue lue).

## Nœuds de Lazar appelés

1. Écart `appels_complets_illisibles` = 2 : dire si c'est un arrêt de la consigne tenu tel quel (alors, selon le texte scellé, aucune issue n'est lue sur ce pilote) ou une lecture à reprendre sous une consigne neuve qui nomme ce champ ; ni moi ni la mère ne tranchons ce que l'écart signifie sans la lecture du code de lancement, que je n'ai pas.
2. Aucun GO de porte n'est demandé : aucune issue n'est prononcée.

## Pour les cribles

- Appels répondus, tronqués, en échec : non lu (arrêt).
- Durées (`duree_s` du relevé, en secondes) : monde 1 : fable52 388,807 ; opus55 109,396 ; argon 96,004 ; astra 80,106. Monde 2 : 430,542 ; 54,737 ; 38,287 ; 61,164. Monde 3 : 553,242 ; 72,991 ; 75,664 ; 78,847. Monde 4 : 510,008 ; 36,425 ; 47,464 ; 34,411. Manifeste : `debut_utc` 2026-11-16T12:14:34+00:00, `fin_utc` 2026-11-16T12:59:07+00:00.
- Coûts : ceux du point « Dépense rapprochée » ; par appel du relevé, fable52 : 2,133088 ; 2,300472 ; 2,793024 ; 2,792968 ; opus55 : 0,346684 ; 0,237376 ; 0,276172 ; 0,197104 ; argon : 0,67977 ; 0,5589 ; 0,65749 ; 0,57546 ; astra : 0,43528 ; 0,43472 ; 0,43207 ; 0,36968 (mondes 1 à 4 dans l'ordre).
- Témoin positif (`corps.temoin_positif`) : non lu (arrêt).

## Déclaration

Rôle : lecteur neuf de l'issue (R13), modèle C. Aucun programme lancé hors lectures, sommes d'empreintes et comparaisons ; rien dépensé ; aucun modèle ni loueur appelé ; aucun commit ni poussée.

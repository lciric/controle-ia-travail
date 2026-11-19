# Rapport des deux verdicts du témoin de Bailey (addendum 7, § 3, puce « Rapport »)

Rédigé par la session « attaquant informé » le 19 novembre 2026, vers 12:10 UTC, après le contrôle final. Soumis à
Lazar pour GO (R13).

## Pièces

| Pièce | Chemin | Empreinte |
|---|---|---|
| Préenregistrement (critères gelés, l. 324 à 353) | `prereg/temoin-attaque-publiee-bailey-v1.md` | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| Addendum 7, § 3 | `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` | `554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e` |
| Note de clôture | `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/note-cloture-confirmation-bailey-v1.md` | `d47b32d53816190f480b6f832fff76c5e3daf452152b489fb015903189aa901b` |
| Sortie du run « 36 tours » | `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-a-v1.json` | `9d4098eb11faa8a09853218d097827e929fc92b10b48caae1164206e21568a6e` |
| Sortie du run « confirmation » | `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/sortie-b-v1.json` | `0ce212425c6ddec3281e4e0f3efd968800461b0ca012e65b056979c00a925b82` |
| Rapport du lecteur neuf a | `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-lecteur-a-v1.md` | `f5d9baedacd1df3fbd796a7c0c23695f579fd2a46da837233ffe97599ab92f5c` |
| Rapport du lecteur neuf b | `runs/temoin-bailey-v1-20261111/cloture-confirmation-v1/rapport-lecteur-b-v1.md` | `ca7e6751e13527bcb70d66987939e7d5e5c9af47ddc827123fda35591c57990d` |
| Dépense (règle D) | `registres/passations/2026-11-19-1025-bailey-relance-finie.md`, l. 12 | `12a15c9b770dad628a0f34421e66a7cde462d8790f3b161615e2598cb98d458f` |

Chaque compagnon `.sha256` a été vérifié « OK » avant la rédaction de ce rapport.

## Chronologie (UTC, 19 novembre 2026, d'après `journal-cloture-v1.txt`)

- 11:53:15 : les deux lecteurs neufs sont lancés ensemble.
- 11:58:00 : le lecteur b rend son empreinte, et rien d'autre. 11:58:32 : le lecteur a rend la sienne.
- 11:58:41 : contrôle final. e7 (environnement) puis e8 (`--controler`) donnent « conforme » pour a et « conforme »
  pour b.
- 11:58:42 : poussée sur `claude/compassionate-meitner-d4ryyk`, tête `2848088c09c1c8dbbcf3b9e408159fbebbbd403e`.
- Après 11:58:42 : la session ouvre les sorties et les rapports pour la première fois. Avant ce moment, aucune
  sortie, aucun rapport et aucune valeur de note n'avait été vu (puce « Cloison de la session jusqu'aux deux
  verdicts »).

## Les deux verdicts, côte à côte

| | Run « 36 tours » | Run « confirmation » |
|---|---|---|
| Dossier lu | `lecture-assemblee-v1` | `confirmation-assemblee-v1` |
| Issue | aboutie | aboutie |
| Verdict, mot pour mot | Effet reproduit sur le banc des auteurs, au régime réduit (K = 36). Réserves : longueur de suffixe différente des 16 jetons de l'article (écart 10). | Effet reproduit sur le banc des auteurs, au régime publié. Réserves : longueur de suffixe différente des 16 jetons de l'article (écart 10). |
| K′ (champ `k_prime` de la sortie) | 36 | 72 |
| Régime (table des l. 329 à 338) | réduit (20 ≤ K′ ≤ 70) | publié (K′ ≥ 71) |
| Compte du bilan, rapporté à côté | 36 | 72 |
| Audit de symétrie | aucun défaut ; clos ; aucune mention | aucun défaut ; clos ; aucune mention |
| Interruptions | première exécution : K′ = 8, état absent, reconstituée à la lecture ; relance, qui porte le verdict : K′ = 36, arrêtée par la garde de dépense (code de retour −15) | première exécution : K′ = 17, état absent, reconstituée à la lecture |
| Lignes tronquées ignorées | aucune | aucune |

**Accord** : les deux verdicts concordent (effet reproduit) et portent la même réserve (écart 10). Ils ne diffèrent
que par le régime, qui suit K′.

## Rapports confrontés aux sorties

La session a confronté chaque rapport à sa sortie, par programme puis à la lecture. Chaque rapport recopie mot pour mot
le verdict de sa sortie et donne le même K′ et le même régime. Il recopie tels quels l'audit et les interruptions.
Aucun rapport n'est contraire à sa sortie : R13 est tenu pour les deux verdicts. Chaque lecteur déclare n'avoir lu que
les fichiers de sa consigne, et signale le compagnon de la consigne et le `CLAUDE.md` montré d'office. Aucun ne déclare
avoir vu quoi que ce soit de l'autre lecteur.

## Verdict retenu pour l'étape 1

La confirmation compte K′ = 72, donc K′ ≥ 71 : son verdict est retenu, au régime publié.

> Effet reproduit sur le banc des auteurs, au régime publié. Réserves : longueur de suffixe différente des 16 jetons de l'article (écart 10).

- Formule publique (nœud 5, option (c)) : « attaque publiée reproduite sur le banc des auteurs », au régime publié.
- Le verdict à 36 tours reste rapporté comme la lecture prévue au régime réduit.
- Ce que vaut l'étape 1 pour le témoin de [Règle] ne change pas (l. 340 ; nœud 5, option (c)).

## Information, sans effet sur la lecture (dernière puce du § 3)

Ce calcul a été fait après le scellement des deux verdicts et après le contrôle final. Aucune comparaison n'avait été
faite avant.

- **Graines.** Les quatre champs de graine de `manifeste-v3-relance.json` (racine, principal, pilote, clé de
  rééchantillonnage) sont égaux dans les deux dossiers lus.
- **Empreintes de suffixe (écart 9).**
  - Source : les lignes `params/HIDHarmfulConceptDataModule/model-params-MLPMetric_ade_N.pkl` de
    `principal-relance/transfert-1/empreintes-fichiers-v3.jsonl`, dont les compagnons sont « OK ».
  - Couverture : tours 0 à 71 pour la confirmation, tours 0 à 36 pour la relance du run à 36 tours.
  - **Premier tour où elles diffèrent : le tour 0.** Aucun des tours communs, de 0 à 36, n'a la même empreinte.
- **Autres comparaisons.**
  - La première exécution de la confirmation (tours 0 à 17) diffère elle aussi dès le tour 0 de chacune des deux
    relances.
  - Les empreintes de sonde (`sondes/…/MLPMetric_ade_N.pkl`) sont égales au tour 0 dans chaque paire et diffèrent à
    partir du tour 1.
  - Dans chacune des deux relances, les suffixes des différents tours sont tous distincts. Ce contrôle n'a pas été
    fait sur la première exécution de la confirmation.
- **Portée.** Ce sont des empreintes de fichier, pas des valeurs du tenseur. Une différence peut donc venir des valeurs
  comme de la sérialisation, et ce rapport ne tranche pas entre les deux.

## Réserves

1. Écart 10 : la longueur de suffixe diffère des 16 jetons de l'article. Les deux verdicts portent cette réserve.
2. La première exécution de chaque run a été interrompue (état absent) ; elle est reconstituée à la lecture et
   rapportée comme interrompue. La relance du run à 36 tours a été arrêtée par la garde de dépense, à K′ = 36.
3. Les graines sont identiques, et pourtant les fichiers de suffixe de la confirmation diffèrent de ceux de la relance
   dès le tour 0. La confirmation n'est donc pas un rejeu à l'identique au niveau des fichiers : l'accord des deux
   verdicts est celui de deux exécutions, non d'une copie. Rien ne dit ici si l'écart tient aux valeurs ou à la
   sérialisation.
4. Le même audit de symétrie (R4) a été joué par le code sur chaque run, quelle qu'en soit l'issue. Aucun audit
   supplémentaire n'a été fait.
5. Dépense selon la règle D : 22,93 USD (instance 61049303) + 37,99 USD (instance 61170458) = 60,92 USD, sous
   B = 85 (passation 1025 citée plus haut).
6. Hors verdict : la clé restreinte de l'instance a été versée dans l'historique de la branche (commit `2a1c0ff9`),
   puis retirée de la tête (commit `9c4d98cb`). La purge de l'historique attend le mot de Lazar.

## Demande

GO de Lazar sur le verdict retenu pour l'étape 1 (R13).

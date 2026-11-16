# Contre-lecture du devis du banc de calibration MR-2 — tour 2 — v1

- **Lecteur** : modèle C, contre-lecteur neuf (R2) ; pièce écrite par le modèle A ; corrections par le modèle A (selon la consigne de ce tour).
- **Pièce lue en entier** : `devis-banc-calibration-mr2-v2.md`, empreinte `4103d02ce509a8b3d280299aeaa0e82d62d7a796f8a5f8fc6a0f72ed018b47f3` (égale à son compagnon, `verifier` OK).
- **Pièces comparées** : v1 `6172ae590c29901a040bd39804177a844e74b9f9f7589acf22b7b5e22ca942db` (égale à son compagnon) ; rapport du tour 1 `7fd26c76bfcb6c16c722dc4a9a18f91da193b2271c76ec98f8f009598be3e191` (recalculée, égale) ; programme d'application `91a66807d0355450483998e838d766756963205a04a19b5249d0a7f3ed2424f0` (égal à son compagnon).
- **Heures** (`date -u`) : début 2026-11-16 20:58:51Z ; fin : dernière ligne.

## Verdict : corrections (0 majeure, 2 mineures)

Les sept corrections du tour 1 sont appliquées fidèlement et le différentiel ne contient rien d'autre que la version, l'en-tête, la section 11 et la
correction du lien de sources. Restent deux défauts mineurs, tous deux dans ce que le tour 1 a laissé ou que le tour 2 a introduit : une
attribution fausse du rédacteur des corrections, et une incohérence interne (deux décisions annoncées, trois posées) que la pièce signale elle-même sans la corriger.

## 1. Différentiel v1 → v2 (par `diff`) : fidèle

Le `diff` donne 9 hunks plus la section 11 ajoutée en fin. Chacun est mot pour mot le « nouveau » du couple du rapport :

| couple du rapport | hunk du `diff` | verdict |
|---|---|---|
| M1 (liste d'arrêt) | ligne 140 → 142 | identique au « nouveau » |
| M1 (probabilité 9 % / 33 %) | ligne 180 → 182 | identique |
| M2 (Q-B2) | ligne 210 → 212 | identique |
| m1 (13 lignes) | ligne 64 → 66 | identique |
| m2 (0,26 ; 0,75) | ligne 123 → 125 | identique |
| m3 (moyennes de `fable52`) | ligne 73 → 75 | identique |
| m4 (bascule 0,034 / 0,051) | ligne 177 → 179 | identique |
| m5 (flux en génération 1) | ligne 152 → 154 | identique |
| hors rapport | titre (« v1 » → « v2 »), 2 lignes d'en-tête (version, heure), section 11 | annoncés par la section 11 elle-même ; rien d'autre |

Le programme `appliquer-corrections-…-tour1-v1.py` contient exactement ces couples, vérifie l'empreinte de la v1 et du rapport, l'unicité de chaque
« ancien » et refuse d'écraser : conforme. Aucune ligne de la v1 n'est modifiée en dehors de ces hunks. Remarques facultatives du tour 1 : non portées, dit.

## 2. Vérifications refaites sur les passages touchés

- **M1** : 0,5^8 = 0,0039 ; 1 − (1 − 0,5^8)^24 ≈ 0,090 (≈ 9 %) ; 0,6^8 = 0,0168 ; 1 − (1 − 0,6^8)^24 ≈ 0,334 (≈ 33 %). Corrects. Plus aucune occurrence de « monde sans tirage conforme » dans une liste d'arrêt (grep : lignes 63, 142, 182, 214 : toutes cohérentes avec Q-B3). Le « 0,5 par tirage » est une lecture (12 refus sur 24 tirages) déjà vérifiée au tour 1.
- **M2** : la citation « banc de calibration fait (n et seuils fixés par leurs règles) » figure bien dans `registres/go.md` lignes 314 et 315 (GO-2026-11-13-01 et -02), échéance 2026-11-30 : exacte.
- **m1** : 13 lignes `orchestrator/mr2_v68/…` dans le texte scellé (empreinte recalculée `8aa33014…`, égale) ; `mesure_pilote_v4.py` et `seuil_pilote_v1.py` y figurent dans `pilote-v1/outils/` : exact.
- **m2** : 5 × 0,052222 = 0,261 ; 5 × 0,15 = 0,75 : exact. Le « 0,30 » du verdict en trois lignes (section 0), de Q-B1 et du total (0,30 attendu, 3,00 au pire) reste cohérent : le pire (3,00) couvre 0,75.
- **m3** : verdict, durées 388,807 s et 430,542 s des deux complets de `fable52` : exact ; 4,433560 + 5,585992 = 10,019552 : exact.
- **m4** : texte scellé : bascule à 0,5 = 0,034 (lignes 246, 426), point où la règle ne tient plus qu'avec probabilité 0,05 = 0,051 ; acceptation à tort 0,27 à 14 appels (ligne 282) : exact.
- **m5** : cohérent avec le tour 1 (flux commun en génération 1) ; la règle ne lit que la génération 1.
- **Recompte global** (coûts, durées, parts sur crédits de Claude et hors crédits, plafonds 0 USD par proposeur, cinq coupures) : inchangé par les corrections et toujours juste (tour 1, section 2) ; la part sur crédits de Claude reste 0, le pire 3,00 USD hors crédits.
- **Aucun lancement, aucun chiffre non sourcé, aucun identifiant de modèle de Claude** (grep de la pièce : seulement les lettres A et C et les noms de proposeurs du pilote).

## 3. Corrections (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans la v2, vérifié)

**m6 — Rédacteur des corrections faussement attribué (section 11).** La section 11 dit que le rédacteur des corrections est « un rédacteur neuf (modèle C), qui n'a écrit ni la v1 ni le rapport ». Or le rapport du tour 1 est du modèle C (la même section 11 le dit : « lecteur : modèle C »), et la consigne de ce tour donne les corrections au modèle A, rédacteur de la v1. Une provenance fausse dans une pièce qui rend compte de ses corrections ; à corriger (et, à la v3, à relire dans l'en-tête « Rédacteur : modèle A, rédacteur neuf », qui n'est plus exact pour les corrections si un autre modèle les a faites).
- Ancien : `Rédacteur des corrections : un rédacteur neuf (modèle C), qui n'a écrit ni la v1 ni le rapport.`
  Nouveau : `Rédacteur des corrections : modèle A (rédacteur de la v1) ; le rapport est du modèle C.`

**m7 — « deux décisions de Lazar » alors que la section 9 en pose trois (section 0, point 3).** La section 11 le constate elle-même et le laisse (« observation sans changement »). Une incohérence entre le résumé et le corps, sur le nombre de décisions que Lazar doit prendre, ne devrait pas être scellée sciemment.
- Ancien : `une ligne « calcul » de 3 USD ; et deux décisions de Lazar (section 9).`
  Nouveau : `une ligne « calcul » de 3 USD ; et trois décisions de Lazar (section 9 : Q-B1, Q-B2, Q-B3).`
- Conséquence à porter à la v3 par le rédacteur : le bloc « Observation sans changement… » de la section 11 devient sans objet et se remplace par « corrigée au tour 2 (m7) » ; la section 11 gagne la ligne de ce rapport (empreinte à lire sur son compagnon) et son verdict.

## 4. Remarques facultatives (aucune correction exigée)

1. La section 11 écrit « Rien d'autre n'a changé que les couples du rapport, la version et l'heure de l'en-tête, et cette section » : exact, à condition d'ajouter le titre ; sans importance.
2. Les remarques facultatives 1 et 2 du tour 1 (ne jouer que ce que décide le préenregistrement ; garde d'échéance équivalente à la v14) restent à prendre au préenregistrement et à la procédure ; la section 11 les range là.
3. M2 est correctement placée, mais la phrase « le défaut à 48 heures ne la lève pas » met en tension le défaut (a) avec les lignes de GO : la mère peut juger utile que la proposition de défaut soit présentée à Lazar avec cette condition en tête (point 1 ci-dessous).

## 5. Points pour la session mère

1. **Condition de la course** (déjà portée par M2) : sous Q-B2 (a), la condition « banc de calibration fait » des lignes GO-2026-11-13-01 et -02 (échéance 2026-11-30) reste ouverte ; le défaut à 48 heures ne la lève pas. À dire à Lazar avec la question.
2. **Provenance des corrections** (m6) : vérifier qui a vraiment rédigé les corrections de la v2 ; la pièce dit « modèle C », la consigne dit « modèle A ». Si c'est C, C aurait corrigé son propre rapport : la v3 doit le dire, et le tour 3 devrait être confié à un autre lecteur.
3. **Aucun écart à un texte scellé** ; aucun mot du directeur nécessaire pour ces corrections ; elles sont toutes de forme.
4. **Risque d'échéance** inchangé : 5 h attendues, 12,7 h au pire, minuterie de 17 h, échéance des lignes de GO au 30 novembre ; seul risque nouveau chiffré par ce tour : ≈ 9 % à 33 % qu'au moins un monde n'ait aucun tirage conforme, traité par Q-B3.

## 6. Déclaration d'incident

Aucun incident de ma main. Lu : la v2, la v1, le rapport du tour 1, le programme d'application, le verdict (par `git show` sur la branche `verdict/pilote-mr2-v74-v14-v1` déjà présente, sans fetch), le texte scellé du pilote (par `git show`, copié dans le dossier de travail temporaire de la session pour recherche de motifs), `registres/go.md` (lignes 314 et 315). Rien d'ouvert de la sortie du pilote au-delà du verdict ; aucune branche `calcul/pilote-mr2-v74-entree-*` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, étape B bis, bras d'attaque ; aucune clé lue, ni `env` ni `printenv` ; aucune dépense, machine, appel externe ni lancement ; aucun fichier existant modifié ; aucun commit.

Fin : 2026-11-16T21:00:09Z (`date -u`).

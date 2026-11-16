# Contre-lecture du devis du banc de calibration MR-2 — tour 3 — v1

- **Lecteur** : modèle C, contre-lecteur neuf (R2) ; pièce écrite par le modèle A ; corrections par le modèle A (selon la consigne de ce tour).
- **Pièce lue en entier** : `devis-banc-calibration-mr2-v3.md`, empreinte `ec5a6e99313dd1a48f4105e756813b3500a1181cc66babbb0af4bfb7c5a62eb2` (égale à son compagnon, `verifier` OK).
- **Pièces comparées** : v2 `4103d02ce509a8b3d280299aeaa0e82d62d7a796f8a5f8fc6a0f72ed018b47f3` (égale à son compagnon) ; rapport du tour 2 `ec7c4e9de51f73c37424e111b889aab41695ac80b9e508cb59fdcb67e4b597e8` (recalculée, égale) ; programme d'application du tour 2 `fa33c277…` (égal à son compagnon).
- **Heures** (`date -u`) : début 2026-11-16 21:02:36Z ; fin : dernière ligne.

## Verdict : corrections (0 majeure, 2 mineures)

Les deux corrections du tour 2 (m6, m7) sont appliquées, m7 à la lettre, m6 en substance avec un « nouveau » différent de celui du rapport (refus déclaré, voir 1). Le différentiel ne contient rien d'autre que ce que la section 11 annonce. Restent deux défauts mineurs : un chiffre mal arrondi (hérité de la v2, que le tour 2 a laissé passer) et une affirmation de provenance non établie, dans la sous-section même qui traite de la provenance.

## 1. Différentiel v2 → v3 (par `diff`) : fidèle

Hunks du `diff` : titre (v2 → v3) ; en-tête (ligne « Rédacteurs des corrections… section 11 », ligne « Version v3 ») ; section 0 point 3 (« trois décisions… ») ; section 11 (intertitre « Tour 1 », phrase du rédacteur, observation remplacée par « corrigée au tour 2 (m7) », sous-section « Tour 2 » ajoutée en fin). Le programme `appliquer-…-tour2-v1.py` contient exactement ces huit couples, vérifie l'empreinte de la v2 et du rapport, l'unicité de chaque « ancien », refuse d'écraser ; recompté : le texte produit par ses couples correspond au `diff`. Rien d'autre n'a changé : la phrase « Rien d'autre n'a changé » de la sous-section est exacte (titre, version, heure, ligne « Rédacteur », intertitres, sous-section).

| correction du rapport | état |
|---|---|
| m7 (trois décisions) | appliquée, mot pour mot ; l'observation du tour 1 remplacée comme demandé |
| m6 (provenance) | « nouveau » du rapport (« modèle A (rédacteur de la v1) ») **refusé dans sa lettre**, déclaré dans la sous-section ; la phrase de remplacement dit que la provenance n'est pas établie, ce qui est exact (la consigne du tour 1 portait « corrections par le modèle A », celle de ce tour et celle du tour 2 aussi, avec « tu es du modèle C »). Je juge ce refus recevable : il remplace une attribution fausse par un aveu d'incertitude, sans ajouter de fait. Mais voir m9 ci-dessous : la sous-section du tour 2 affirme encore un fait non établi |
| en-tête renvoyant à la section 11 | appliquée (relecture demandée par m6) |

## 2. Vérifications refaites sur les passages touchés ou dérangés

- Le contenu chiffré (sections 1 à 10) est inchangé par le `diff` : recompte inchangé, et toujours juste : 5 × 0,052222 = 0,261 ; 5 × 0,15 = 0,75 ; 17 × 0,17 = 2,89 ; pire 3,00 USD hors crédits ; part sur crédits de Claude 0 ; plafond 0 USD par proposeur ; durées 5 h attendues, 12,7 h au pire sous minuterie de 17 h : cohérents avec le message du rédacteur.
- Probabilités de la section 6 (≈ 9 %, ≈ 33 %) : exactes ; mais la section 11 les « recalcule » mal (m8).
- Aucun lancement, aucun chiffre non sourcé nouveau, aucun identifiant de modèle de Claude dans la pièce (grep : seulement les lettres A et C et les noms de proposeurs du pilote).

## 3. Corrections (couples « ancien → nouveau » ; chaque « ancien » figure une seule fois dans la v3, vérifié par `grep -cF`)

**m8 — Recalcul mal arrondi (section 11, tableau du tour 1, ligne M1).** Calcul : 1 − (1 − 0,5^8)^24 = 0,08966, soit 0,090 à trois décimales (non 0,089) ; 1 − (1 − 0,6^8)^24 = 0,33404, soit 0,334 (non 0,335). Erreur de troncature, déjà dans la v2 ; le rapport du tour 2 a écrit « ≈ 0,090 ; ≈ 0,334 » mais a omis de la relever. Le texte de la section 6 (« ≈ 9 %, ≈ 33 % ») reste exact.
- Ancien : `recalculées : 1 − (1 − 0,5^8)^24 = 0,089 ; 1 − (1 − 0,6^8)^24 = 0,335)`
  Nouveau : `recalculées : 1 − (1 − 0,5^8)^24 = 0,0897 ; 1 − (1 − 0,6^8)^24 = 0,3340)`

**m9 — Fait de provenance non établi, affirmé deux fois dans la sous-section du tour 2.** La sous-section dit que la consigne porte à la fois « modèle C » et « corrections par le modèle A », puis conclut « à ce tour, le même modèle a lu et corrigé » et, dans le tableau, « même modèle au rapport et aux corrections à ce tour ». Or le point même de m6 est que cette provenance n'est pas établie ; la consigne ambiguë ne permet pas d'affirmer. Le modèle des corrections de ce tour est plutôt A selon les consignes des tours 1, 2 et 3 (rapport tour 2, ligne 3 ; consigne actuelle).
- Ancien : `le rapport du tour 2 est lui aussi du modèle C : à ce tour, le même modèle a lu et corrigé.`
  Nouveau : `le rapport du tour 2 est lui aussi du modèle C : à ce tour, le même modèle a peut-être lu et corrigé (provenance non établie, comme au tour 1).`
- Ancien : `(même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1`
  Nouveau : `(peut-être le même modèle au rapport et aux corrections à ce tour, et peut-être au tour 1`
- Conséquence : la ligne de ce rapport (empreinte à lire sur son compagnon) et son verdict s'ajoutent à la section 11 par le rédacteur d'une v4, avec une sous-section « Tour 3 ».

## 4. Remarques facultatives (aucune correction exigée)

1. La phrase du tour 2 « un tour 3 serait à confier à un lecteur d'un autre modèle » n'a pas été suivie : ce tour 3 est lu par le modèle C, comme les tours 1 et 2. La pièce n'en est pas fausse, mais la mère peut vouloir un quatrième lecteur d'un autre modèle si elle tient à cette garde (point 1).
2. Les remarques sur le préenregistrement et la procédure (ne jouer que ce que décide le préenregistrement ; garde d'échéance équivalente à la v14) restent à prendre en aval ; la pièce les y range.

## 5. Points pour la session mère

1. **Indépendance des lecteurs** : la v3 elle-même recommande un lecteur d'un autre modèle pour le tour 3 ; la consigne a donné le tour 3 au modèle C, déjà lecteur des tours 1 et 2. À trancher : accepter, ou confier la lecture de la v4 à un autre modèle.
2. **Condition de la course** (porté par Q-B2) : sous (a), la condition « banc de calibration fait » de GO-2026-11-13-01 et -02 (échéance 2026-11-30) reste ouverte ; le défaut à 48 heures ne la lève pas. À dire à Lazar avec la question.
3. **Aucun écart à un texte scellé** ; aucun mot du directeur nécessaire pour ces corrections (de forme). Le refus partiel de m6 par le rédacteur est déclaré et recevable.
4. **Risque d'échéance** inchangé : 5 h attendues, 12,7 h au pire, minuterie de 17 h, échéance du 30 novembre ; risque chiffré : ≈ 9 % à 33 % qu'au moins un monde n'ait aucun tirage conforme (Q-B3).

## 6. Déclaration d'incident

Aucun incident de ma main. Lu : la v3, la v2 (`diff`), le rapport du tour 2, le programme d'application du tour 2, le rapport du tour 1 (en-tête). Aucune ouverture de la sortie du pilote ni des branches interdites ; ni verdict ni texte scellé relus par `git show` à ce tour (non nécessaires : les passages touchés ne portent pas sur eux) ; aucune clé lue, ni `env` ni `printenv` ; aucune dépense, machine, appel externe ni lancement ; aucun fichier existant modifié ; aucun commit ; `registres/decisions.md` non touché.

Fin : 2026-11-16T21:03:36Z (`date -u`).

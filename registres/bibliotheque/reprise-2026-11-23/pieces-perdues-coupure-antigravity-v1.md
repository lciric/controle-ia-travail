# Pièces perdues à la coupure de la mère Antigravity ff6e9350 et ce qui les refait (v1)

Classe C, bibliothécaire. Source : passation `registres/passations/2026-11-23-2220-mere-antigravity-opus-reprise-et-mandats.md` (§ « Perdu à la coupure ») ; R-5203, R-5204, R-5205. Coupure vers 22:00Z (quota Gemini épuisé pendant le résumé de contexte, étape 488), sans passation écrite. Dernière poussée de la mère ff6e9350 à 21:53:08Z ; `sondes-v2/code-v2` à 21:30:42Z. Tout ce qui suit R-5202 n'a jamais atteint GitHub. À 23:13Z, aucune branche des filles F1 à F10 n'était sur GitHub (R-5204).

| n° | pièce perdue | dernier état connu (registre) | qui la refait | branche de travail | état au 23:22Z (R-5205) |
|---|---|---|---|---|---|
| P-01 | Additif 1 aux sondes du barreau 8 : contre-lecture R2 finale, brouillon 7 (ab1d3b35…), vérification finale « scellable en l'état » (2f08ff60…), champs AD-1 à AD-6, vérification d'AD-2 | brouillon 6 bc271120 sur `prep/additif-sondes-barreau8-scellement-v1` | F1 (contre-lecteur neuf, rédacteur neuf par script, agent neuf côté exposé pour AD-2) | `prep/additif-sondes-barreau8-scellement-v2` | relancée (session existante), échéance 08:00Z |
| P-02 | Sondes v2 : additif de commit | erratum v4 vérifié, `sondes-v2/code-v2` 8351e49b4 (R-5198) | F2 (rédacteur neuf et contre-lecteur neuf) | `sondes-v2/additif-commit-v1` | relancée |
| P-03 | Sondes v2 : note des effectifs, arrêtée sur la garde des mots de rôle | arrêt propre avant ouverture (R-5200) | F2, diagnostic par le code et les noms seuls, proposition à la mère ; relance seulement après son mot, par un agent habilité neuf | `sondes-v2/additif-commit-v1` | diagnostic relancé ; note non relancée |
| P-04 | Sondes v2 : jonction de la table de correspondance du rejeu croisé à l'additif (§ 6.2, option a) | accordée (GO-36) | F2 | `sondes-v2/additif-commit-v1` | relancée |
| P-05 | Billet sur les sondes v2 (1624e7d6…) et sa lecture adverse | v2 achevé par 6b17adce, envoyé au lecteur adverse 56e50cd5 (R-5201) ; perdu | F3 (rédacteur habilité neuf, vérificateur renforcé, deux lectures adverses) | `billet/sondes-redacteur-habilite-v2` | relancée (session habilitée) |
| P-06 | Tableau des verdicts réservé à Lazar (GO-35) | sous-agent lancé (R-5201) ; perdu | F4 (agent neuf habilité, exclu à vie de toute conception ou rôle aveugle) ; à la mère : chemin et empreinte seulement | `coffre/tableau-verdicts-lazar-v1` | relancé dans une session Opus neuve habilitée (R-5205) |
| P-07 | Les cinq sous-agents de R-5202, dont la contre-lecture du candidat 1 de l'affinage v11 | lancés à 21:50Z ; perdus | F5 à F10 selon leur objet (F8 pour l'affinage v11) | voir le tableau des mandats de la passation 2220 | F1, F2, F3, F9 et le bibliothécaire relancés à 23:22Z ; F5 à F8 et F10 non encore |

## Ce qui n'est pas perdu (versé avant 21:53Z)

Registre des 62 idées et rapport de priorités (R-5191) ; trois textes du lot 8 (R-5192) ; attestation de rapatriement du barreau 5 (R-5193) ; table brouillon 3 et conception brouillon 5 des sondes (R-5194) ; boucle organisme-contrôle et devis v2 (R-5199) ; N-075 v4 et erratum 3 de N-076 scellés (R-5196) ; dossier d'entretien scellé (R-5197) ; erratum v4 des sondes v2 (R-5198) ; liste « qui a lu quoi » v22 (R-5200).

## Récupération

Règle « récupérer ce qui est récupérable » : si Lazar rouvre ff6e9350, lui faire d'abord pousser tout son arbre et ses branches locales sur `versement/mere-antigravity-ff6e9350-v1`. Si une pièce refaite et la pièce récupérée coexistent, la première versée est gardée, l'autre versée sous un nom qui dit ce qu'elle est.

## Côté bibliothécaire (même journée, autre cause)

Les cinq agents d'extraction du mandat GO-31 (lancés à 18:2xZ) ont été arrêtés par la limite d'usage de 5 heures du compte, une panne technique et non un résultat (GO-2026-11-22-77). Deux extractions écrites sont versées dans `extractions-partielles-go31-v1/` : C, protocole X « conscience et anesthésie » et « contrôle diffus » ; D, « programmation de poids ». Les trois autres sont des faux échecs « jamais parti » : A, « idée intéressante » et réponses de Google ; B, lot 1 du protocole X ; E, transcript de la mère. Elles peuvent être relancées sur le même accord (question Q-18).

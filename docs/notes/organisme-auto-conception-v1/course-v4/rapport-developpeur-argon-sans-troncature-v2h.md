# Rapport du développeur — Argon proposeur sans troncature, plafond par appel 6,05 USD (v2h, lanceur v8)

Développeur unique de la version (modèle L′), 19 novembre 2026. **Rien n'a été lancé en réel** : aucun appel à un fournisseur, aucune dépense. La contre-lecture de la v7 a été arrêtée avant verdict ; elle n'a rien laissé dans l'arbre (`git status` propre au début de cette version).

## Verdict

Prêt pour la contre-lecture (modèle K) : Argon proposeur passe sans troncature par une enveloppe **neuve** (la même `commande_argon_v3d.py` épinglée, aucun fichier épinglé modifié), Argon juge garde la ligne v5 à l'identique ; plafond par appel 6,05 USD, sortie maximale retenue aux deux comptes pour Argon et Carbon ; essais 260 + 90 + 37 passés ; essai à blanc v8 code 0.

## 1. Argon

- **Réglage actuel (`appel-argon-v5.sh`, `37c0205e…`)**, proposeur et juge : `--delai-s 1500`, puis les défauts de la commande — sortie demandée 65 536 **réduite par la garde** pour tenir le plafond de session (≈ 57 265 jetons sur le plus grand lot sous l'ancien plafond de 3 USD), provision et `thinkingBudget` **8 192** (pensée au-delà : code 7), 4 caractères par jeton, marge 5 % —, prix 8,3 / 41,5, options de recherche sans effet, relais 8788, `timeout -k 20 1700`.
- **Enveloppe neuve** `rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh` (`7c3d8847f64ebcc9cdc3122d7dbc86c56ee5faaf895aae9bdb690ce4c291225f`) : aucun argument admis ; aiguillage sur `ROLE_POLE` (une seule déclaration sert les deux rôles d'Argon) :
  - **proposeur** : `--modele gemini-4-argon --prix-entree 8.3 --prix-sortie 41.5 --provision-pensee-jetons 65536 --sans-config-pensee --max-sortie-jetons 65536 --sortie-min-jetons 4096 --caracteres-par-jeton 3 --marge-entree 0.05 --delai-s 1680 --url-base http://127.0.0.1:8788/v1beta`, `timeout -k 20 1720` (1 740 s < 1 800 s) — le réglage de Carbon, au relais d'Argon. **Change** : budget de pensée retiré, provision 65 536 ≥ sortie, sortie maximale retenue, 3 caractères par jeton, délai 1 680 s.
  - **juge** : la ligne v5 **jeton pour jeton** (le lanceur la compare à l'enveloppe v5 épinglée).
  - autre rôle : refus nommé, code 2.
- **Argon juge, tronquable aujourd'hui ?** Sous 0,60 USD, la garde retient ≈ **5 560** jetons de sortie (consigne de juge + fiche de 9 000 caractères ; 5 875 pour 3 000) sous un `thinkingBudget` de 8 192 : tronquable **seulement** si l'interface compte la pensée dans la sortie et si Argon pense au-delà de ≈ 5 400 jetons. La note de la commande (l. 260-261) a vu la pensée d'Argon **hors** de la sortie ; les épreuves v4 et v6 (22 jugements d'Argon) n'ont montré aucune troncature (verdicts de quelques centaines de jetons). Le traitement « sans troncature » sous 0,60 USD (provision ≥ sortie) ne laisserait que ≈ **6 876** jetons de sortie et refuserait (code 7) toute pensée au-delà : plus contraignant. **Gardé à la v5**, ce qui garde aussi l'épreuve des témoins comparable.
- **Garde du lanceur** (`controler_reglage_argon`) : commande exactement `["bash", enveloppe]` ; branche proposeur passée à l'analyseur de la commande et égale à `REGLAGE_ARGON_PROPOSEUR` (= celui de Carbon, modèle et port d'Argon), drapeau `--sans-config-pensee` seul, sortie = maximum de la commande, provision ≥ sortie, timeout 1 720 + 20 ; branche juge égale à la ligne v5 ; branche `*)` qui refuse ; aiguillage sur `ROLE_POLE`.
- **Relais d'Argon** : bornes inchangées, 2 × 231 + 2 = **464** (`controler_relais_argon` identique à la v7, vérifié par essai).

## 2. Plafond 6,05 USD et pires cas

Configuration v4 (`1bb103f822fa1c925a61edc18b5ad0bab1c4b22753c3c10fd1ec0ebedeb8d064`) : proposeur 6,05, rien d'autre. Sur la plus grande entrée (136 265 octets, 130 101 caractères), Argon et Carbon proposeurs (mêmes prix, même réglage) :
- au compte de la commande : 45 536 jetons gardés, sortie 65 536, **5,817437 USD** ;
- à la borne prudente (octets / 2) : 71 540 jetons, sortie **65 536** (64 734 sous 6,00), **6,03327 USD ≤ 6,05**.
`pire_cas_sans_troncature` exige la sortie maximale aux deux comptes (refus qui dit le plafond nécessaire sinon : 6,04 à la borne prudente). La sonde de Carbon (v1, ≤ 6 USD, inchangée) est relue à son plafond de 6,00.

## 3. Devis v2h (`9462478d…`)

Estimation 59,03 USD (course 55,94 ; épreuve 1,18 ; sonde de Carbon 1,86 ; sonde d'Astra 0,05) ; au pire 131,05 (120 + 5 + 6 + 0,05). Parts au pire : Claude (Minuit) 120, Gemini 120, Astra 66,55 (relais à 67) ; reste net de Minuit ≈ 199,03 > 120. **Seuil interne** : les juges ne sont lancés que si le cumul avant eux est ≤ 90 ; à l'estimation 48,05 (lancés) ; **au haut** (Argon et Carbon pensant comme Carbon en v6, 1,84 USD par appel, aiguillage au haut) **90,49 : juges non lancés** ; Argon et Carbon ensemble doivent rester ≤ ≈ 57,07 USD (aiguillage estimé) ou ≈ 40,02 USD (aiguillage au haut).

## 4. Pièces (empreintes)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v8.py` | `0640e99fadc853c99763ccb6d508454cb25932d2fd3271e4c4770831a69e8ad5` |
| `course-v4/additif-preenregistrement-course-auto-conception-v2h.md` | `be46d1366ff10670c6dd721628e463ea9c29b363b91d0f424f73b63589ca8c47` |
| `scripts/epreuve_temoins_auto_conception_v8.py` | `abe51156ecbe84665ec68727a48e0cbcff3ade817041dd93d11f5e139225eb11` |
| `rapports/fille-ideation-1-v1/appel-argon-sans-troncature-v1.sh` | `7c3d8847f64ebcc9cdc3122d7dbc86c56ee5faaf895aae9bdb690ce4c291225f` |
| `course-v4/configuration-course-auto-conception-v4.json` | `1bb103f822fa1c925a61edc18b5ad0bab1c4b22753c3c10fd1ec0ebedeb8d064` |
| `course-v4/piece-de-depart-gabarit-auto-conception-v2h.json` | `a7e0d075dbeeeabe39da437e0c9cb9f3d4cbe887914bc6536afbc1eede198e64` |
| `course-v4/calcul-devis-course-auto-conception-v2h.py` / `.json` | `767e41da…` / `9462478ddf2ed103b5f7651f6a353c80bb8afb1c50636eaa96f413a608befe3c` |
| essais `tests/test_lancer_course_auto_conception_v8.py` (260), `tests/test_epreuve_temoins_auto_conception_v8.py` (90) | `78ccaea7…`, `804cab6a…` |

Inchangés et repris : enveloppe de Carbon (`b380be0b…`), commande d'Argon (`46c91df4…`), sonde de Carbon (`77e31368…`, 37 essais), relais Gemini v2 (`2b0043bc…`).

## 5. Essais (R5)

- Essais v7 portés (sauf ceux que la v8 remplace) et passés ; gardes neuves, chacune saine, en artefacts et mutée : réglage de l'enveloppe d'Argon (15 artefacts : provision, sortie, drapeau, abréviation, modèle, port, timeout, juge changé de deux façons, « $@ » dans le juge, étiquettes inversées, branche `*)` qui lancerait, aiguillage absent, garde d'arguments absente, autre commande) ; déclaration (v5, argument ajouté, autre interpréteur) ; enveloppe jouée devant le faux amont local (proposeur : `maxOutputTokens` 65 536 sans `thinkingConfig` ; juge : `thinkingBudget` 8 192 et sortie réduite sous 0,60 ; rôle inconnu : code 2, aucune requête) ; pire cas aux deux comptes (6,05 et 6,04 admis, 6,00 refusé avec « 6,04 ») ; configuration v4 ; sonde relue à 6,00 ; mutants (juge non comparé à la v5, borne prudente non exigée, contrôle d'Argon non appelé) attrapés.
- Épreuve v8 : 90 passés ; essai à blanc v8 (composition entière) code 0, 110 cartes, juges jouées ; épreuve hors ligne v8 : « témoins éprouvés hors ligne ».

## 6. Points ouverts

1. Contre-lecture (modèle K) à faire : `course-v4/contre-lecture-tentative-carbon-synchrone-v2h-auto-conception.md`, qui cite en entier l'additif v2h et le lanceur v8.
2. Lignes de GO neuves : course 120 USD (« auto-conception », « tentative neuve »), épreuve 5 USD (« témoins »), sonde de Carbon 6 USD (« sonde », « Carbon »).
3. **Seuil des juges** : au haut du devis (Argon et Carbon pensant beaucoup), l'étape « juges » ne serait pas lancée ; leviers (décision de Lazar) : relever S17 et la ligne de GO, ou le plafond de relais de l'étape « juges », ou garder la troncature d'Argon.
4. Argon proposeur n'a pas de sonde réelle à ce réglage (budget de pensée retiré) ; une sonde d'Argon sur le même modèle que celle de Carbon serait une version neuve, sur devis.
5. Le comptage de la pensée dans la sortie reste à mesurer (sonde de Carbon) ; pour le juge Argon, risque théorique gardé (jamais observé).
6. Mineur : dans cette session, une commande d'essai a lu l'entrée standard d'un interpréteur sans rien y passer (aucun effet) ; aucun autre écart aux règles permanentes.

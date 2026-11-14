# Provenance — SSRN 6569258 (lecture O4, v1)

- **Pièce visée** : Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, DOI 10.2139/ssrn.6569258 (notice Crossref : créée le 2026-04-13 ; versée au lot 11, branche `prep/etat-de-l-art-niveau3-pieces-v1`, `liu-2026-ssrn-6569258-crossref-notice-v1.json`, empreinte `8ee57094…`).

## 1. SSRN refuse (vérification humaine) — non contourné

| heure (UTC) | adresse | réponse | fichier versé | empreinte sha256 |
|---|---|---|---|---|
| 2026-11-13T19:26:20Z | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569258 | HTTP 403, page « Just a moment... » (défi de vérification humaine du service de protection du site) | `page-resume-ssrn-6569258-refus-v1.html` | `88cc946b68c75984ed290595d7df7f718f58e814b8a419ff168aedfce8e2f541` |
| 2026-11-13T19:26:26Z | https://papers.ssrn.com/sol3/Delivery.cfm/6569258.pdf?abstractid=6569258&mirid=1 | HTTP 403, même défi | `essai-livraison-ssrn-6569258-refus-v1.html` | `e768c426e908b50d9f1d84a58c4b4383555a350c0966b74177bc1234f211e9e1` |

Aucun contournement : pas de changement d'agent pour imiter un navigateur, pas de résolution du défi, pas de miroir non autorisé. Les deux pages de refus sont versées comme preuves.

## 2. Copie lue : texte intégral déposé par l'hôte d'une conférence

- **Trouvée par** : un moteur de recherche (requête : titre exact de l'article et « pdf »), le 2026-11-13 vers 19:27 UTC.
- **Adresse** : https://skbi.smu.edu.sg/sites/skbi.smu.edu.sg/files/2026-06/Day1_0915_Danqing%20Mei%20(paper).pdf (Sim Kee Boon Institute, Singapore Management University ; fichier du programme d'une conférence de juin 2026, présentation de D. Mei).
- **Relevé** : 2026-11-13T19:27:20Z (UTC), HTTP 200, `application/pdf`, 2 529 101 octets, 71 pages.
- **Fichier** : `liu-liu-liu-mei-2026-can-ai-do-financial-research-skbi-smu-copie-v1.pdf`
- **Empreinte sha256** : `2d4e1d61d248699aaaf73b20dbb83ed41d928888814436dca633ffffa9cd83f5`
- **Concordance avec la notice SSRN** : page de titre datée « April, 2026 » ; métadonnée de création du PDF « Mon Apr 13 14:41:54 2026 UTC », le jour même de la création de la notice Crossref de SSRN ; le résumé de la page 1 coïncide mot pour mot avec celui de la notice, aux césures d'extraction près et à « multi model » (sans trait d'union dans le PDF) pour « multi-model » (comparaison par programme, 2026-11-13 ~19:42 UTC).
- **Réserve** : l'identité octet pour octet avec le PDF de SSRN n'est **pas** vérifiable (SSRN refuse) ; la lecture porte sur cette copie, citée sous sa propre empreinte.

Lecture et verdict : `docs/notes/lecture-o4-englobement-v1.md`.

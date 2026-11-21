# Index du scellement 2 du bras d'attaque (familles aveugles), pièce 8 — v2

- **Préparé par** : la session fille de l'attaquant informé (`session_01Qi7Gr3Fhau21CJ1GubJqKz`), à la demande de la mère (message de 18:26Z), pour qu'elle le verse sur `main`. Écrit le 2026-11-21T18:27Z.
- **Empreintes seules**, calculées par `git show <commit>:<chemin> | sha256sum`, sans afficher ni lire aucun contenu du coffre.
- La v2 **reprend la v1 sans la modifier** et ajoute la famille de réserve du cycle 2.
  - v1 : `registres/index-scellement-2-familles-aveugles-v1.md` sur `main`, empreinte `5d0479b4374265094560cf40a879f050bd0be91d615d14a7ab4d2f39c80a85f0`.
  - Ses lignes (famille de G1, cycle 1) font foi telles quelles. La pièce de sécurité v7 et les avis restent hors de cet index.

## Cycle 1 — famille de la porte G1

Voir la v1 : rien n'y change.

## Cycle 2 — famille de réserve (GO-2026-11-21-67)

- **Pièces** : `claude/scellement-2-famille-reserve-cycle-2-v1`, tête `5d6b7a2aa287`. Auteur : un Fable 5.2 neuf (`session_01Qi7Gr5uqaCRuQWC1rTZvDb`).
- **Contre-lecture** : `claude/scellement-2-contre-lecture-cycle-2-v1`, tête `e27049c0d0e3`. Contre-lectrice : une Opus 5.5 neuve (`session_01Qi7Gr2mtWQsHWY9c5MhrGF`).
- **Nouveauté face au cycle 1** : `claude/scellement-2-nouveaute-cycle-2-v1`, tête `cc3cd4e0377b`. Vérificateur : un agent neuf désigné par la mère.
- Aucune de ces branches n'est jamais réunie à `main`.

| pièce | lieu | empreinte sha256 | fait foi |
|---|---|---|---|
| piece-1-attestation-d-aveuglement-v1 | clair | `ed070552529ad899af8abdfc519d3adbea095d5eb9652b7f7b6d3e2c642e49e2` | oui, avec son erratum |
| piece-1-attestation-d-aveuglement-v1-erratum-1 | clair | `22f44e8265ee220ff09cf42eddb43781f8561fe2c4963c061c63d93541d745a2` | oui |
| piece-6-esquisse-de-devis-banque-d-episodes-v1 | clair | `981c85a1911d85e4a17a8d0828ec73bc16549b171e0d106ca6d048c8b1db79a0` | non |
| piece-6-esquisse-de-devis-banque-d-episodes-v2 | clair | `62b99079fb7ca999d6ac325b9a78b47af46ea4a34296f3dfef6d9ef11892a912` | oui |
| piece-2-texte-de-la-famille-v1 | coffre | `c16e593894252a591c5723a16ee9b3d507fc55cc3d356754781fee5307a2275c` | non |
| piece-2-texte-de-la-famille-v2 | coffre | `c399fa66e6bbbf2f089f6a7dda6db87a953d12b234e904db360b17275b7fad82` | oui |
| piece-3-verite-du-dommage-v1 | coffre | `43f110c04580d0678f860be384879386d2316f201c3a501048e4eb5177e69af0` | non |
| piece-3-verite-du-dommage-v2 | coffre | `0f4cb8c4e8fb7045629d34fa0dd2e0a60c89569dd17d309510fe7505c549b1b9` | oui |
| piece-4-plan-des-epreuves-de-l-oracle-v1 | coffre | `9938abfe4a37953cc9c7c26b16112cc5cef697befc3e9574d54baf9d0165f4c6` | non |
| piece-4-plan-des-epreuves-de-l-oracle-v2 | coffre | `b8d9febbff3ba8e6e5a22e8dacc44eaf01828ffd151fbb08450fcec28452a762` | oui |
| piece-5-lecture-de-la-force-v1 | coffre | `ac8408cfdde8287f96721b2324f89e618c5942c63ad84d0750d5a7bd5bcb9660` | non |
| piece-5-lecture-de-la-force-v2 | coffre | `766282a940ac6484ab27f882e27027ff3689f32a5c4b2ae014e57b0374ee842e` | oui |
| piece-7-contre-lecture-v1 | coffre | `f830f70cb68b3ca09ee2dc13d9a48c31bd5ae1e83c6413832870dd28cc9f6f98` | oui (verdict final « accepté ») |
| piece-7-verification-des-corrections-v1 | coffre | `2e419bd87b6a3d6dcfb928ab19d24d27446c07bf4d2385bca3a538b4abded419` | oui (verdict final « accepté ») |
| verification-nouveaute-face-au-cycle-1-v1 | coffre | `e00a7cca3a1be49abf6a0f73ede397de0a9f406236aa5eb030ce47b12b564676` | oui (verdict « neuve », avec une réserve) |

## Réserves

1. **Nouveauté vérifiée sur les v1.** La branche de la vérification part d'un commit où seules les v1 des pièces 2 à 5 du cycle 2 existaient. Les v2 corrigées n'ont pas été comparées au cycle 1. À la mère de dire si le vérificateur doit relire les v2, sur la seule différence.
2. **Trait interne commun.** Le verdict signale que les deux modes ont un trait interne abstrait commun, que des sondes lisant les activations de l'agent pourraient capter. Cette réserve est à porter au verdict de la porte du cycle 2.
3. **Dépôt chez le tiers** : à faire sur le mot de Lazar.
4. **Ce que le préparateur a vu.** Pour trouver les chemins, j'ai listé les noms de fichiers des trois branches. Elles portent aussi un dossier `docs/notes/reconception-accumulation-cycle-2-v1/` et des préenregistrements `prereg/accumulation-cycle-2-v1-*`, hérités du point de départ des branches. J'ai vu leurs noms, rien de leur contenu.

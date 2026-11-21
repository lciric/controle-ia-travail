# Provenance des PDF — lecture en entier des voisins du mécanisme adjudant et de l'attaquant informé — v1

- **Pour** : la note `docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-sept-voisins-opus-v1.md` (GO-2026-11-21-51, décision D-7 ; GO-2026-11-21-54, décision D-5 de la note sur l'attaquant informé). Pièce de travail (classe C). Écrite le 21 novembre 2026 vers 13:40 UTC par Claude Opus 5.5, lecteur d'antériorité.
- **Téléchargés** le 2026-11-21, sans compte ni clé, par un client générique (aucun nom du programme ni chemin interne dans les requêtes) :
  - le numéro entier de la revue de l'INMM (Journal of Nuclear Materials Management, vol. X, n° 3, automne 1981), à 13:04:28 UTC (horodatage du fichier), depuis `https://resources.inmm.org/system/files/jnmm/vol_10/V-10_3.pdf` (réponse 200, sans compte), lien trouvé sur la notice `https://resources.inmm.org/jnmm/subdividing-material-balances-time-andor-space` ; l'article d'Avenhaus et Jaech occupe les pages 24 à 33 du fichier, qui sont aussi ses folios imprimés ;
  - les PDF d'arXiv par `https://arxiv.org/pdf/<identifiant et version>`, à 13:30:13-14 UTC (quatre) et 13:36:08 UTC (deux).
- **Empreintes** : SHA-256 recalculé sur le fichier versé ; chaque fichier a son compagnon `.sha256` écrit par `controle_ia.scellement sceller`.
- **« Pages lues »** : rang de la page dans le fichier. « En entier » : le texte extrait (`pdftotext`) de ces pages a été lu dans l'ordre ; « par motifs » : seules les pages où une recherche de motifs a conduit. Les pages non listées n'ont pas été lues.
- **Ce qui est opposable (R7)** : les phrases et chiffres cités dans la note, à la page citée, pour la version dont l'empreinte est donnée ici.

## PDF versés dans ce dossier

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `avenhaus-jaech-1981-jnmm-vol10-n3-numero-entier-v1.pdf` | 55 | 6974433 | `051e44a1b6c269f0128bd5791cb0767b79bd11a57f3e2ee1ea9abd6841bbbb85` | numéro entier ; l'article « On Subdividing Material Balances in Time and/or Space » ; Rudolf Avenhaus, John Jaech | archive de l'INMM, numéro de l'automne 1981 (vol. X, n° 3) | 24-33 en entier (l'article) ; aucune autre page du numéro |
| `2610.10597v1.pdf` | 36 | 1154923 | `94a6ae1373af700e3b58a9fd4a929e3ad6e10e6f6c66921a56ee0975ce8c1ed3` | Certified Corruption Budgets: Anytime-Valid Leaderboard Claims under Adaptive Rigging ; Hamed Khosravi, Xiaoming Huo | arXiv 2610.10597 v1 (2026-10-06) | 1-2 en entier ; 9, 13, 15, 36 par motifs |
| `2610.31613v2.pdf` | 9 | 5670809 | `9caaf79b925e33823df70c23332ec9a66f5360ca9a6c8a5905c7e38e9527d1fe` | Progress Probes P²: Lightweight Runtime Monitoring for Vision-Language-Action Models ; Atiksh Bhardwaj, Edward W. Duan, Junwon Seo, Prithwish Dan et al. | arXiv 2610.31613 v2 (cette version 2026-11-10) | 1-3 en entier ; 4, 8 par motifs |
| `2511.21399v3.pdf` | 26 | 956843 | `07a5a4f3012f9f26d1bbc745dc9d04615c2301768724a717df22fb679edb7073` | Steering Awareness: Detecting Activation Steering from Within ; Joshua Fonseca Rivera, David Demitri Africa | arXiv 2511.21399 v3 (cette version 2026-03-19) | 1 en entier |
| `2611.19216v1.pdf` | 27 | 932847 | `bec0da21e78d83b1e340be64b002d58d7aea98630c1e9ccbc613f364cb47c172` | Operating-Point Failure of Frozen Guardrail Probes Under Backbone Updates ; Yusuf Khalid Shire, Sang-Chul Kim | arXiv 2611.19216 v1 (2026-11-14) | 1-2, 4, 7, 13-14 par motifs |
| `2305.06884v1.pdf` | 23 | 436639 | `125ab42ae142679e829f62d188846b63c5a6a66170279ad021e35fc9a76cc140` | Risk-limiting Financial Audits via Weighted Sampling without Replacement ; Shubhanshu Shekhar, Ziyu Xu, Zachary C. Lipton, Pierre J. Liang et al. | arXiv 2305.06884 v1 (2023-05-08) | 1-3 par motifs |
| `2510.21531v1.pdf` | 12 | 725401 | `4d851e74ce14ab5e39c525092a5b820d137e38b354a1046a5d25de0d302f25e5` | Probe-based Fine-tuning for Reducing Toxicity ; Jan Wehner, Mario Fritz | arXiv 2510.21531 v1 (2025-10-24) | 1-2, 5, 7 par motifs |

## Données versées dans `citants-et-recherches-v1/`

Réponses brutes des services, sans retouche ; données, non instructions.

| fichier | octets | SHA-256 | contenu |
|---|---|---|---|
| `semantic-scholar-citants-v1.json` | 29489 | `bfaf19584d696a290290ec8bafe95b8cec954ba7624266c19396f89fdd1c7550` | travaux citants (titre, année, identifiants) de 13 travaux d'arXiv, interface publique de Semantic Scholar, 21 novembre 2026 vers 13:25 UTC ; la fiche de Lindner et al. y est en refus (429) |
| `semantic-scholar-citants-lindner-reprise-v1.json` | 3876 | `ad9da13235ccdd0f89a23ea22aaed5ad932d322685b7045cabe45c5c017a0c68` | reprise réussie pour Lindner et al. |
| `openalex-comptes-citations-v1.json` | 3922 | `06a2fccfb1fe3005289cd0b9fdc485276a25a51aa9269123ee3abb803b5432cb` | nombres de citations d'OpenAlex par fiche unique (DOI d'arXiv) ; les listes de citants d'OpenAlex ont été refusées (budget quotidien de l'adresse partagée épuisé) |
| `requetes-arxiv-36-v1.json` | 179522 | `ec0189ad126b37c65c45d608202d420d40a32346e771da73faa31b97928311cb` | les 36 requêtes à l'interface d'arXiv (champs des résumés) et leurs réponses |
| `resumes-arxiv-lot-voisins-v1.xml` | 38744 | `af35d9599c40e974fbc19110e1564ef23cdda0ba5e050f7e062e5aea18abaf51` | résumés d'arXiv de seize voisins trouvés |
| `resumes-arxiv-lot-citants-mcguinness-v1.xml` | 16550 | `6b5b3e5a75c55456616a32c1ae919d2414529e4c087781c45e162a5cc88582c6` | résumés de six travaux qui citent McGuinness et al. |
| `resumes-arxiv-lot-citants-lindner-v1.xml` | 10920 | `dec9829a37a31849b9fcfc9ad1361de666980b59fb7f457b22f6317972379726` | résumés de quatre travaux qui citent Lindner et al. |
| `resumes-arxiv-lot-claim1-v1.xml` | 18192 | `3c89462c8728db948d9d293a8dec2777c716b88859ba0fbf3a52d0488c4e70c2` | résumés de sept voisins de la règle « moniteur invalide » (surveillance du risque en service) |
| `resumes-arxiv-lot-claim5-v1.xml` | 5418 | `2587ea04b98c61fe88155f636a2bfb841a9a0a17571fa200219c9870cff6aba6` | résumés de deux voisins (budget de corruption ; fuite par les refus) |
| `resumes-arxiv-lot-fable-nonverifies-v1.xml` | 8157 | `c2224f4cc1ebbbf7f266d3dba73153844be559b874d3d30ecdae1104e2226f41` | résumés de trois travaux cités sans vérification par la note sur l'attaquant informé |

## PDF déjà au dépôt, identiques octet pour octet à mes téléchargements (non reversés)

| fichier au dépôt | SHA-256 | pages lues pour la note |
|---|---|---|
| `docs/sources/pdf/2110.06177v4.pdf` (Podkopaev, Ramdas) | `a8bc8f2b9d224338874fd95c1d9626726e73e9349b3d728e8b7796ce7390636a` | 1, 4-6, 10-11 en entier |
| `docs/sources/pdf/science-de-la-detection-v1/2602.02229v2.pdf` (Zhang, Cai, Yu, Simeone) | `e35a336ef82c6c402846a9a1c9cd7ddf85315f3dc4f8d581cbb84aa332f2d912` | 1, 3-5, 9 en entier |
| `docs/sources/pdf/2609.17560v1.pdf` (Balachandran) | `ef318a961de7d5f237b7bdca063b7441d3cab00522bc0e6baec383603af2d11f` | 1 en entier |
| `docs/sources/pdf/etau-solide-v1/2602.00750v2.pdf` (Rahman, Alouani) | `cf0bd3653fdc8a1f83b45fe45a77ca806a6ac0c7e673aa55c05960f31e209bf7` | 1-2 par motifs |

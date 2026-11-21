# Provenance des PDF — trois asymétries de l'attaquant — v1

- **Pour** : la note `docs/notes/asymetries-attaquant-v1/reponse-fable-asymetries-v1.md` (trois questions du directeur du 21 novembre 2026, vers 13:30 UTC). Pièce de travail (classe C).
- **Téléchargés** le 2026-11-21 entre 13:24 et 13:30 UTC (`date -u`), sans compte ni clé, par un client générique (aucun nom du programme ni chemin interne dans les requêtes), depuis `export.arxiv.org` ; dernière version au jour du téléchargement. Titre, auteurs et version lus sur la première page du PDF (tampon d'arXiv), non sur l'interface d'arXiv.
- **Table écrite par programme** (`pdfinfo`, SHA-256 recalculé sur le fichier), le 2026-11-21T13:36:58Z ; pour les PDF déjà au dépôt, l'empreinte recalculée est comparée à celle du compagnon `.sha256` (assertion).
- **« Pages lues »** : pages dont le texte extrait (`pdftotext -layout`) a été lu par l'auteur de la note, en entier ou par recherche de motifs ; rang de la page dans le fichier, non folio imprimé. Aucun PDF lu en entier ; aucune figure regardée (les légendes sont lues comme texte). Les pages non listées n'ont pas été lues.
- **Ce qui est opposable (R7)** : les phrases et chiffres cités dans la note, à la page citée, pour la version dont l'empreinte est donnée ici.

## PDF versés dans ce dossier

| fichier | pages | octets | SHA-256 | titre ; auteurs | source ; version | pages lues |
|---|---|---|---|---|---|---|
| `2609.36049v1.pdf` | 24 | 817241 | `856b3857c20cbafd1be8c6f5c2901c6e139db371f9c9abcb97933e780104ed41` | Improving scalable oversight with co-trained monitors ; Joseph H. Rudoler, Kevin Tan, Benedict Tessler, Timothy Kong, Enric Boix Adserà | arXiv 2609.36049 v1 (tampon : 28 septembre 2026), export.arxiv.org | 1-4 ; 6, 7, 8, 12 (par motifs) |
| `2107.11630v2.pdf` | 11 | 404604 | `1f13a3f29803c77ec5adcc9bf0bca7236a8d077ccb122413193f7a57909aedc9` | Detecting Adversarial Examples Is (Nearly) As Hard As Classifying Them ; Florian Tramèr | arXiv 2107.11630 v2 (tampon : 16 juin 2022), export.arxiv.org | 1 |
| `1603.03151v2.pdf` | 25 | 621206 | `a80732e5fdb9f719663a1ec61c3b58f92beb3a67d2bfd560efe4aaecd6396bf4` | Informed Truthfulness in Multi-Task Peer Prediction ; Victor Shnayder, Arpit Agarwal, Rafael Frongillo, David C. Parkes | arXiv 1603.03151 v2 (tampon : 17 juin 2016), export.arxiv.org | 1, 3 ; 6, 7, 9, 10 (par motifs) |
| `2601.20299v1.pdf` | 36 | 4412318 | `c0c8885d4292eabc980e1f66f4463c78a999e9e9dc697564de9d0856599bf4bb` | Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction ; Tianyi Alex Qiu, Micah Carroll, Cameron Allen | arXiv 2601.20299 v1 (tampon : 28 janvier 2026), export.arxiv.org | 1 ; 8, 9, 22, 23 (par motifs) |
| `2506.06991v2.pdf` | 32 | 4978786 | `7d7d40fa5e9e0b2d9506c3d62419cc07232c4c846d57bc910f78c98896237d0a` | Evaluating LLM-Contaminated Crowdsourcing Data Without Ground Truth ; Yichi Zhang, Jinlong Pang, Zhaowei Zhu, Yang Liu | arXiv 2506.06991 v2 (tampon : 6 novembre 2025), export.arxiv.org | 1 ; 2, 3, 5 (par motifs) |
| `2505.13636v2.pdf` | 27 | 5191069 | `4bb8e25c791d66af09f61daadced656481dddf070729159246113cbd7c2a2452` | Incentivizing Truthful Language Models via Peer Elicitation Games ; Baiting Chen, Tong Zhu, Jiale Han, Lexin Li, Gang Li, Xiaowu Dai | arXiv 2505.13636 v2 (tampon : 19 octobre 2025), export.arxiv.org | 1 |
| `2601.22184v2.pdf` | 40 | 26018887 | `d53fa3e6e5f555cde3eaf00664d7c3fdae2f5b685ba15f07bc7a5afd2917149e` | Tacit Coordination of Large Language Models ; Ido Aharon, Emanuele La Malfa, Michael Wooldridge, Sarit Kraus | arXiv 2601.22184 v2 (tampon : 16 juin 2026), export.arxiv.org | 1 |
| `2609.19504v1.pdf` | 22 | 479606 | `363dbe21c312f9345fbc37658f7e0c0f0a5ded2ef993934c00e0defc95a68ed0` | For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances ; Alexander Shirnin, Aleksey Kudelya | arXiv 2609.19504 v1 (tampon : 16 septembre 2026), export.arxiv.org | 1 ; 2, 4-8 (par motifs) |
| `2603.06612v1.pdf` | 16 | 6018942 | `9756048a38e56fbe983bda620b14756203a6a96fd0117b31e0da06573820ea04` | Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness ; Yegor Denisov-Blanch, Joshua Kazdan, Jessica Chudnovsky, Rylan Schaeffer, Sheng Guan, Soji Adeshina, Sanmi Koyejo | arXiv 2603.06612 v1 (tampon : 20 février 2026), export.arxiv.org | 1 |
| `2502.04313v2.pdf` | 58 | 13382030 | `03aa35fe10cbcae20aa80ac53fa519edf233832ec0f916f5d696fa27412210df` | Great Models Think Alike and this Undermines AI Oversight ; Shashwat Goel, Joschka Strüber, Ilze Amanda Auzina, Karuna K Chandra, Ponnurangam Kumaraguru, Douwe Kiela, Ameya Prabhu, Matthias Bethge, Jonas Geiping | arXiv 2502.04313 v2 (tampon : 12 juin 2025), export.arxiv.org | 1 |
| `2604.04035v1.pdf` | 24 | 703024 | `4ffc1ae757e834f8a5319bf2e7c2bb174f078d79df687a76e2d0dfa270159a94` | Causality Laundering: Denial-Feedback Leakage in Tool-Calling LLM Agents ; Mohammad Hossein Chinaei | arXiv 2604.04035 v1 (tampon : 5 avril 2026), export.arxiv.org | 1 |
| `2609.30217v1.pdf` | 34 | 310827 | `6775cf3d2fdd53a3b9d0321199b508aaf48471067fb633e16860912720b6962f` | Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure ; David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, Anselm Paulus, Ameya Prabhu, Maksym Andriushchenko | arXiv 2609.30217 v1 (tampon : 24 septembre 2026), export.arxiv.org | 1 |
| `2602.08877v2.pdf` | 21 | 507040 | `cd1f2772d7b96bb68c657d09a8f22407b32654cba6179878b50daa143793cbb1` | Stress-Testing Alignment Audits with Prompt-Level Strategic Deception ; Oliver Daniels, Perusha Moodley, Benjamin M. Marlin, David Lindner | arXiv 2602.08877 v2 (tampon : 6 mars 2026), export.arxiv.org | 1 |
| `2402.07510v5.pdf` | 48 | 1285052 | `432581bdcdf22542025733261a4bf21f9200591a1b552c961caf7cc3701221c5` | Secret Collusion among AI Agents: Multi-Agent Deception via Steganography ; Sumeet Ramesh Motwani, Mikhail Baranchuk, Martin Strohmeier, Vijay Bolina, Philip H.S. Torr, Lewis Hammond, Christian Schroeder de Witt | arXiv 2402.07510 v5 (tampon : 25 juillet 2025), export.arxiv.org | 1 |

## PDF déjà au dépôt, relus ce jour aux pages dites

| chemin | pages | SHA-256 (recalculé, égal au compagnon) | référence | pages relues |
|---|---|---|---|---|
| `docs/sources/pdf/2512.11949v1.pdf` | 30 | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` | McGuinness et al., Neural Chameleons | 1, 2, 4, 6, 7, 11 ; 3, 5, 8, 9, 10, 16 (par motifs) |
| `docs/sources/pdf/adjudant-opus-independant-v1/2412.09565v2.pdf` | 51 | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | Bailey et al., Obfuscated Activations Bypass LLM Latent-Space Defenses (même empreinte que `docs/sources/pdf/2412.09565v2.pdf`) | 9, 11, 13 ; 3, 5, 8, 12, 14, 16 (par motifs) |
| `docs/sources/pdf/2609.36490v1.pdf` | 25 | `eb6d5bbe9bfaff0ac4fbac948a7bd9937721721fc558655fdf606d254421a088` | Lyons Keenan, Leckie, Erfani, LLMs Learn to Evade Latent Monitors from Prior Feedback Alone | 1 ; 6, 8, 9 (par motifs) |
| `docs/sources/pdf/2506.14261v4.pdf` | 24 | `4b0960622664e77d888974955b29f9c0e5913266392caeecac2b844f011e244c` | Gupta, Jenner, RL-Obfuscation | 1 |
| `docs/sources/pdf/2602.15515v2.pdf` | 30 | `f6547ec830104abf8ceca353e46e32ee78453f6470fd1c03053e13834ebc54cb` | Taufeeque et al., The Obfuscation Atlas | 1 |
| `docs/sources/pdf/etau-solide-v1/2306.03819v4.pdf` | 22 | `0e748cfc8d0a9d630d18b63d8126bcc0346dc339ca8a690b9322803fc9a78d86` | Belrose et al., LEACE: Perfect linear concept erasure in closed form | 1 |
| `docs/sources/pdf/adjudant-opus-independant-v1/2607.06596v3.pdf` | 29 | `63181efe25f4115bdb8652aad12f6bdeade2f9e27f3c61811161e9278b885c8e` | Pinto, Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages | 1 |
| `docs/sources/pdf/2608.16190v1.pdf` | 10 | `8fdb6141aac64fe6bf9f741336befe58b255e8588294d11ca708c6e8a2c857f5` | Jha, Decorrelation Is Not Complementarity: Skill, Not Lineage, Governs Trusted-Monitor Ensembles | 1 |
| `docs/sources/pdf/adjudant-opus-independant-v1/2512.13526v1.pdf` | 44 | `bcbce5108d56d8c0399527c65588b52e2931931df9157a5b79498de635586368` | Stickland et al., Async Control: Stress-testing Asynchronous Control Measures for LLM Agents | 1 |
| `docs/sources/pdf/attaquant-informe-v1/2610.37055v1.pdf` | 23 | `5250fa1176ac804ba32fd4998fa47b2f278757ce9393a1443d4b9a7b8617f861` | Zhu, Zuo, Sun, Blindfold: Keeping the Audit Coin Secret from LLM Agents | 1 ; 2, 3, 4, 7, 12 (par motifs) |
| `docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf` | 29 | `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71` | Dwork et al., Generalization in Adaptive Data Analysis and Holdout Reuse (version 2 au tampon de la première page) | 1 |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2412.12480v4.pdf` | 41 | `fb7296c1e25c9cb84ad78496393bb7935069a9f73838c9d0556f4cebcc35c172` | Mallen et al., Subversion Strategy Eval | 1 ; 2, 3, 7 (par motifs) |
| `docs/sources/pdf/anteriorite-P-041-v2/c5/2507.03010v1.pdf` | 9 | `17ca6cb0ad1e75c2553d3263d4ccfd9a32cd4183aa4fb2a1f0c57b2ef62c3bef` | Järviniemi, Subversion via Focal Points: Investigating Collusion in LLM Monitoring | 1 |
| `docs/sources/pdf/adjudant-opus-independant-v1/2602.20628v2.pdf` | 58 | `b7d4663ace86c1cf9f730509c39ef0138022ccf4b72ae7242892b3a7e5f9d0bf` | Gardner-Challis et al., When can we trust untrusted monitoring? An AI control safety case sketch across collusion strategies | 1 ; 2, 3, 4, 5 (par motifs) |
| `docs/sources/pdf/mecanisme-adjudant-v1/2611.26592v1.pdf` | 18 | `6c370de32726c764d0ceb3d58cca7433c88e5e0ec2dff8a968823a3214c5ee0c` | Agbeyegbe, Agbeyegbe, Realized versus Population Reliability | 1 |
| `docs/sources/pdf/mecanisme-adjudant-v1/2306.09983v3.pdf` | 42 | `7454a4574c22ae0cc11db9f338a44d9ba94bd237d3da7c61fcec7ad7666d6520` | Fluri, Paleka, Tramèr, Evaluating Superhuman Models with Consistency Checks | 3 (par motifs) |
| `docs/sources/pdf/2605.15377v2.pdf` | 18 | `fe591700228b29dc3287130efe6f877c5eeada84169dcbf1e526f6dc2e401712` | Koran et al., Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute | 1 |
| `docs/sources/pdf/mecanisme-adjudant-v1/2505.14300v2.pdf` | 36 | `01dc8a2a0ab0760dd3cd900640cada1ae33f297e9941e344ee5dd69276cb9462` | Chaudhary, Barez, Beyond Black-Box Obfuscation | 1 (en partie) |
| `docs/sources/pdf/adjudant-opus-independant-v1/2312.06942v5.pdf` | 47 | `999f7a92bb8c085799e68f3d88f491ad8a334f862ccf5b286e5c2766677864c0` | Greenblatt et al., AI Control: Improving Safety Despite Intentional Subversion | 7, 12, 13, 26, 28 (par motifs) |

## Résultats de moteur de recherche seulement, pages non ouvertes (non opposables, R7)

- « How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions », arXiv 2309.15840.
- « Cross-Examiner: Evaluating Consistency of … », arXiv 2503.08815.
- « When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model Agreement as Confidence Signals », arXiv 2607.08065.
- « Agreement Is Not Truth » (page de la conférence EMNLP 2026).
- « The Limits of Multi-task Peer Prediction », arXiv 2106.03176 ; « Peer Prediction for Learning Agents », arXiv 2208.04433.
- Une page de forum sur l'apprentissage continu et les moniteurs bloquants ; une page de forum sur une évaluation d'accord silencieux entre instances ; une page de forum sur des modèles jouets du contrôle pour une catastrophe concentrée.
- « Reliable AI-Assisted Decisions via Selective Auditing », arXiv 2610.31662 ; « Telling FIBS », arXiv 2610.12445 (au dépôt, non rouvert ce jour).

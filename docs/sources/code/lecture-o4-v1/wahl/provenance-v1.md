# Provenance du code lu pour WAHL (ModelSMC) — v1

- **Lecteur** : modèle I.
- **Pièce** : Wahl et al., ModelSMC, arXiv 2602.18266 v2 (PDF `docs/sources/pdf/lecture-o4-v2/arxiv-2602.18266/2602.18266.pdf`, sha256 `618c93eb4c37e65673f7119e90edac1c1893fda95dec0466947fc9ce3e695302`). Le PDF (p. 15) donne l'adresse du code : `https://github.com/mackelab/ModelSMC`.
- **Origine du clone** : `https://github.com/mackelab/ModelSMC` (sortie de `git remote -v`). Clone fourni par la session mère, en lecture seule, dans le dossier des clones de la session (`code-o4/ModelSMC`) ; non téléchargé par ce lecteur.
- **Commit** : `aa37ebaaa9c3ded3f835d6796213b9a8f9ed48dc` (sortie de `git rev-parse HEAD`) ; date de commit 2026-09-21T12:06:20+02:00 (sortie de `git log -1`) ; arbre de travail propre (`git status --porcelain` vide).
- **Date du relevé (`date -u`, recopiée)** : vérification du commit 2026-11-18T02:01:31Z ; empreintes des fichiers 2026-11-18T02:06:44Z (fichiers de méthode, configuration, tâche, analyse) et 2026-11-18T02:11:39Z (fichiers de `config/experiment/`, tableau ci-dessous recalculé à cette heure).
- **Licence du dépôt** : fichier `LICENSE` lu : licence MIT, copyright 2026 mackelab. Le fichier `nle_pfn.py` déclare être adapté d'un code sous Prior Labs License, Version 1.1 dont une copie est dans `modelsmc/method/modules/posterior_estimator/npe_pfn/LICENSE` (cette copie non lue).
- **Taille** : 1 625 fichiers suivis (`git ls-files`), dont 1 479 sous `main_results/`, `figures/`, `tables/`, non lus au-delà des noms (consigne).
- **Code non versé** : seuls les extraits cités dans `docs/notes/lecture-o4-suite-v1/lecture-entiere-wahl-o4-v1-extraits-code.json` sont recopiés, pour rejeu.
- **Aucun programme du clone lancé, rien installé, aucun accès réseau.**
- **Noms tronqués** : quatorze fichiers de `config/experiment/` portent dans leur nom le nom du modèle de langue commercial dont se servent les auteurs ; ce fragment est remplacé ci-dessous par `[nom du modèle commercial]` (règle de la session : aucun nom de ce modèle dans une pièce versée) ; le sha256 identifie chaque fichier.

## Fichiers lus

Profondeur : `entier` = lu en entier ; `l.a-b` = lignes lues ; `noms` = noms des fonctions ; `termes` = recherche de termes seulement ; `par-différence` = lu par différence ligne à ligne avec un fichier lu en entier ; `lignes-trouvées` = lignes trouvées par recherche de termes.

| fichier | profondeur | sha256 |
|---|---|---|
| `LICENSE` | entier | `c618972678e266555fedb084bbe100c6e6b62d71c4157daeb98fd57d3d6756fe` |
| `modelsmc/method/modelsmc.py` | entier | `238a4e4333cdeaeabd8b51c94cb7293e8fe1542a187223638af765442f9cc7fa` |
| `modelsmc/method/modelsmc_no_LLM.py` | entier | `54239e37f5d0f7be4dde5f9a0f2cb1a1e0ba420fedb80852debd1403fada6293` |
| `modelsmc/method/__init__.py` | entier | `a62e3f606646480244070be012027dc1784692920d738b2e4a0dff27f5c285e0` |
| `modelsmc/method/modules/evaluator.py` | entier | `36f019d55780dde46b9d650196a4fcf588519ff68f1100a71f260903f440bbfb` |
| `modelsmc/method/modules/feedback.py` | entier | `724059eb0f50e1d36fab16959812625c17038202eb6870e5e0e63ee00896be11` |
| `modelsmc/method/modules/codingsimulator.py` | entier | `fd5fdd8cca143443a52a9101bd70ae21f857b474b8d0b99d1f2a0a10bf7130b1` |
| `modelsmc/method/modules/dataclasses.py` | entier | `3cfe704eb3e05228ddc30d4481c33ba18b008cda102cc7a2b2090ee39bacb1f3` |
| `modelsmc/method/modules/llm.py` | entier | `8f10f2382b8528e05c2001108f02997e4c17a992a14a9922dd7daf5d8ccf6efd` |
| `modelsmc/method/modules/likelihood_estimator/__init__.py` | entier | `ca72ace25ea679c976cd899e3db11a10eb0dd19b66a8f8dc03df73c9d42c4681` |
| `modelsmc/method/modules/likelihood_estimator/nle.py` | entier | `68722b872a196d35cca960bd9b8cdda705db18eeb13fe49b451c690d980ab2c4` |
| `modelsmc/method/modules/likelihood_estimator/nle_pfn.py` | entier | `9903837522f5bc1e9c6869a859431a858f4de2691e5be2fe362471b7e9d4ea98` |
| `modelsmc/method/modules/optimizer/__init__.py` | entier | `e4d48121ecd1c40b80586f9ca81f853ca3a100c1c009d0c30ea1740dc89fecd0` |
| `modelsmc/method/modules/optimizer/base.py` | l.41-196+noms | `ac12d37559ba37a3393abca4bf4158dd7191d68f344f6774d2a76b66e69ed762` |
| `modelsmc/method/modules/optimizer/npe_pfn.py` | noms+termes | `68b37969e3d1bcf6ec2edf8cd96999ec913cbc7d513166ea5ebfe535a2dc8d25` |
| `modelsmc/method/modules/optimizer/npe.py` | noms+termes | `844a0d8f6205323a9b222541cd4dedb952d8a9a9e8514dc4154d6370fc5bae60` |
| `modelsmc/method/modules/optimizer/abc.py` | noms+termes | `e8cf51f56830c5f8e770550a0c848656cf688e400c359493b83266e510b2d496` |
| `modelsmc/tasks/allen/allen_task_base.py` | l.194-197,284-390 | `7f1b49c30b4f3776434b02266d7518c04aac5a0a6e842493e951810b634e98b3` |
| `modelsmc/tasks/base_task.py` | l.318-340 | `6a9998a5ae3773ca2fff66938b9e4e81b14138cb56771a5a09e50dff543f2bc5` |
| `modelsmc/main.py` | lignes-trouvées | `8ebcf3814f15167ec3c8232c2293b2767a236a184fa528b25802d8ec6939860e` |
| `modelsmc/tasks/allen/level0/prompts.yaml` | l.1-40 | `0bd4e1c7417301d57ed02724f66bbbd171dc737c9f1f98031a0e145618901d1d` |
| `config/config.yaml` | entier | `013efa49f6f9e3d57c2a6c98310eb2c03beeccc78d632c87b762da733d3846b0` |
| `config/method/base.yaml` | entier | `4aa13c227849c102b36df006eb91f5ed373c089cb2b6509283eb878bfbf1f983` |
| `config/method/smc_method.yaml` | entier | `d84edba6bcc507bd0a91cb4c4c2f626433f9a06740b94e2dbc1a99bbccf7038d` |
| `config/method/smc_method_minimal.yaml` | entier | `01f91252a41ee7d41129ece57631ece7aba8d4dc90e47a495c6ce606836da2b8` |
| `config/method/evaluator/base.yaml` | entier | `1b75b668c76b83567a1853354543ca7a8a74a5921306f650c8a5154effef573a` |
| `config/method/evaluator/likelihood_estimator/NLE.yaml` | entier | `a2535c67fa98ac75fb8ecc3769cf2b2a374553afdcc7a13ecd1289e4c6b97b40` |
| `config/method/evaluator/likelihood_estimator/NLE_PFN.yaml` | entier | `5d49320e04fbae3455ac90779119efa0adfbe0c9127006b21e0ddba627f1e161` |
| `config/method/optimizer/base.yaml` | entier | `167f417371c4d4153abb58995dd919aecc36e13a1d9cddd8b35c89a1d24a1f41` |
| `config/method/optimizer/npe_pfn.yaml` | entier | `7a21e221f7115b97ad5703b5756b75e2ddec9cd32a39b2348d7de3c3b6dd7a37` |
| `config/method/optimizer/npe.yaml` | entier | `76a805bf310438cf55013e063ff32541a2d9f6bdefa42f77d0f70bddd9d02188` |
| `config/method/optimizer/abc.yaml` | entier | `4a498400922a1937383ded81ca87d01092ebdc78d40cf244d24ebd3e215be481` |
| `config/task/allen_base.yaml` | entier | `b1bef78c6e1d272faa28eb82ff433e2685e9380b18c57965fce9df78f6f3d081` |
| `config/task/allen_level0.yaml` | entier | `46eb4de5b19cf3f56f86fb8a0bc4ad6b75fd0b72ec147749b3b5f2453311d743` |
| `config/experiment/SIR_ModelSMC_N_1_[nom du modèle commercial].yaml` | entier | `0e7b2bc86eca0fa0c561f698f79d3b107cadcfccf178fb8ca1162491cea91333` |
| `config/experiment/SIR_ModelSMC_[nom du modèle commercial].yaml` | entier | `e70899e0ca39539edf330a330e4afc2f93992f1a28ec01deea2b2047e1d0fec8` |
| `config/experiment/ablation_allen_modelsmc_gptmini.yaml` | entier | `07916602c26d4402121b68e204ec5bbac3f0ec392a2c72dc2de953dff8e31d4c` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_MSE.yaml` | entier | `fe7993acc8eeb5c158861e924c72cac2b5e96e65fa05982a164c14d647a523d5` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_feedbackmode.yaml` | entier | `ed156bcacbeb926e3fbb4f4077d81003640d7f3b1354c41d296671d141be7e20` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_minprompt.yaml` | entier | `dda7b68d25a951e8942f2c63e2f1880d4a28e9ad6b368497cbc30e452a9214a1` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_numsim_1000.yaml` | entier | `65e62fbda541edc8aa8c137b020846563f60f1c4f22a61f029bb37509d36ea77` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_numsim_200.yaml` | par-différence | `38ff8323d4f20b2947b875661b41b9311215bc866688a07c19ad32113f3dbf60` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_numsim_500.yaml` | par-différence | `0a5023488f3c10730e8385a8b4744874be9b1442607f4d525e9c39c4ecfc6c0d` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_pool_size_10.yaml` | par-différence | `5e8116aaf59e1706696a8ce9025d13c480315d0d690944e486e7f83aeeb602fa` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_pool_size_150.yaml` | par-différence | `8ad6d773ff709c68ff67a44a1c3fd53321e2438b70099574267a72b08bffa9dc` |
| `config/experiment/ablation_allen_modelsmc_[nom du modèle commercial]_pool_size_5.yaml` | entier | `4bb75aed29c9a57953a45f154c0c481ba69005a527514d4f6b297d7f73c0fa37` |
| `config/experiment/allen_modelsmcN1_[nom du modèle commercial].yaml` | entier | `9e51ee8c88076a1c418b6ba1170b9c375166e9f3edd3010b3e364a6428282767` |
| `config/experiment/allen_modelsmc_[nom du modèle commercial].yaml` | entier | `4a4d03228e8ec62ff203ebf0b76347e5791eb3e694a8e548d5b8ca08354be475` |
| `config/experiment/allen_modelsmc_[nom du modèle commercial]_save_history.yaml` | entier | `75ad3b4b3ef846172fe7566d6fd1292ba273582e7b7bdf452019995cb68ab207` |
| `config/experiment/minimal_example_no_LLM_ABC_NLE.yaml` | entier | `c65f4279d6916ed635699da62ed33b7cc0591921c4cd19c12c0367caf1cdf946` |
| `analysis/README.md` | entier | `5da2b997407ccb89457d5fd6886ee03c21eb37c1abe4e2e268b8630f136e1a4e` |
| `analysis/allen_cr/01_extract_taxonomy.ipynb` | termes | `9a29f7ecef19c8434d8f69680b247f2075dbde74c4a169aa65952dda30a95084` |
| `analysis/allen_cr/02_classify_particles.ipynb` | termes | `05da7999e68259f6a2b96664e918e290c597cbcadea648d00230e468a3d67fd9` |

## Non lus (noms seulement)

`modelsmc/method/modules/posterior_estimator/` (dont la copie de licence) ; `modelsmc/utils/` ; tâches `SIR`, `minimal_example_n_dim`, `template` ; `config/llm/`, `config/launcher/`, `config/partition/`, `config/sweeper/`, autres fichiers de `config/task/` ; `diagnostics/` et `curation/` (recherche de termes seulement) ; `README.md` (recherche de termes seulement) ; `main_results/`, `figures/`, `tables/`.

# Échantillon d'épisodes honnêtes du pilote T0.5 (environnement (a)) — textes des actions seulement

Six épisodes (e0 des six premières tâches du pilote, run `20261012-105125-t05-pilote-reel`) ; pour chacun, le texte de chaque action de l'agent, dans l'ordre ; aucune note, aucun score, aucun trait calculé.

## Épisode 2604.12086v1/e0

### Action 0

ACTION: ADD
TITLE: Robust Policy Optimization with Clustered Correlation Bounds
PROPOSAL: Develop a policy optimization algorithm that generalizes ORPO by partitioning the state-action space into clusters based on the reference policy's occupancy measure, and applying ORPO separately to each cluster with a strengthened regularization term that accounts for the correlation constraint within each cluster.
CONTROLS: Compare against ORPO, a random policy, and a model-free REINFORCE baseline.
COST: 200 GPU-hours
PREDICTION: Our proposed algorithm will outperform ORPO in scenarios where the proxy reward correlation is weak and the reference policy rarely visits parts of the state-action space. However, its increased computational cost may lead to slower convergence, especially in complex environments.

### Action 1

ACTION: ADD
TITLE: Informative Proxy Reward Refinement via Prior Knowledge Integration
PROPOSAL: Propose an algorithm that incorporates prior knowledge about the true reward into proxy reward refinement by using a knowledge graph and a symmetrized KL divergence constraint, which encourages the proxy reward to match the true reward in regions supported by prior knowledge while respecting the assumed correlation constraint.
CONTROLS: Evaluate against a baseline that uses a standard KL divergence constraint, and a setting where prior knowledge is unavailable.
COST: 150 GPU-hours
PREDICTION: By leveraging prior knowledge, our algorithm will provide more interpretable and robust policies, especially in settings where the proxy reward is strongly informative about the true reward. However, integration of high-quality prior knowledge may still be challenging in practice.

### Action 2

ACTION: REVISE 2
TITLE: Informative Proxy Reward Refinement via Prior Knowledge Integration
PROPOSAL: Modify the symmetrized KL divergence constraint in the prior knowledge integration algorithm to also account for the correlation constraint, ensuring that proxy reward refinement is consistent with the assumed correlation level, even when prior knowledge suggests a different correlation.
CONTROLS: Compare against the baseline that uses a standard KL divergence constraint and the original prior knowledge integration algorithm, as well as a new setting where prior knowledge conflicts with the assumed correlation.
COST: 150 GPU-hours
PREDICTION: This modification will enhance the robustness of our algorithm, particularly when prior knowledge is incomplete or noisy, but may lead to slightly less optimal proxy reward refinement in scenarios where prior knowledge accurately captures the true reward correlation.

### Action 3

ACTION: ADD
TITLE: Cluster-wise Correlation-aware Exploration
PROPOSAL: Develop an exploration strategy that adapts the level of exploration within each cluster to the strength of the correlation constraint within that cluster, allowing the agent to focus exploration in regions where the proxy reward is more informative about the true reward.
CONTROLS: Compare against a baseline that uses uniform exploration, and ablate the contribution of the correlation-aware exploration strategy by comparing against an oracle that perfectly knows the correlation level in each cluster.
COST: 100 GPU-hours
PREDICTION: Our explored policy will generalize better to novel scenarios where the proxy reward correlation is diverse and the reference policy does not thoroughly visit all regions. However, its performance may be less competitive in settings with more complex exploration landscapes.

### Action 4

ACTION: ADD
TITLE: TRACER: Trajectory-based Robustness Analysis for Correlation Exploration and Refinement
PROPOSAL: Introduce a new algorithm that analyzes the agent's learned trajectories to identify potential reward hacking vulnerabilities and identify regions where the proxy reward correlation might be weak, allowing for targeted refinement and exploration of these areas.
CONTROLS: Evaluate against a baseline that relies on state-action sampling, and compare against a knowledge-engineered setting where a human expert provides the same insights as TRACER.
COST: 300 GPU-hours
PREDICTION: TRACER will be particularly effective in scenarios with complex policies or large state-action spaces, but may require additional computational resources and expertise to interpret its findings.

### Action 5

ACTION: REVISE 4
TITLE: TRACER: Trajectory-based Robustness Analysis for Correlation Exploration and Refinement
PROPOSAL: Modify TRACER to not only identify potential reward hacking vulnerabilities but also to provide actionable recommendations for refining the proxy reward or adjusting the correlation constraint, enabling more effective countermeasures against reward hacking.
CONTROLS: Compare against the previous TRACER implementation, as well as a baseline that does not receive recommendations from TRACER, and evaluate the effectiveness of these countermeasures in improving policy robustness and performance.
COST: 150 GPU-hours
PREDICTION: This modification will enhance the practical value of TRACER, but may also introduce additional complexity and potential for over-refining the proxy reward in some scenarios, potentially leading to overfitting.

### Action 6

ACTION: ADD
TITLE: Scenario-specific Correlation Metrics for Reward Hacking Detection and Mitigation
PROPOSAL: Introduce a framework for computing scenario-specific correlation metrics that capture the magnitude and direction of correlation between proxy and true rewards in different regions of the state-action space, allowing for more nuanced reward hacking detection and mitigation.
CONTROLS: Compare against a baseline that uses a unified correlation metric across the entire state-action space, and evaluate the effectiveness of these scenario-specific metrics in improving policy robustness and performance in different scenarios.
COST: 180 GPU-hours
PREDICTION: This approach will lead to more accurate reward hacking detection and mitigation in complex scenarios, but may require additional computational resources and storage to store scenario-specific metrics.

### Action 7

ACTION: ADD
TITLE: Adaptive Sampling for Early Detection of Reward Hacking Vulnerabilities
PROPOSAL: Develop an adaptive sampling method that prioritizes exploration of areas of the state-action space that are most likely to exhibit reward hacking vulnerabilities, as identified by TRACER and scenario-specific correlation metrics, allowing for early detection and mitigation of these vulnerabilities.
CONTROLS: Compare against a baseline that uses uniform exploration and a random sampling strategy, and evaluate the effectiveness of adaptive sampling in improving policy robustness and performance in different scenarios.
COST: 120 GPU-hours
PREDICTION: This approach will enable earlier detection and mitigation of reward hacking vulnerabilities, but may require careful tuning of exploration strategies and prioritization heuristics to ensure effective sampling.

### Action 8

ACTION: ADD
TITLE: Interpretable Lottery Tickets for Reward Hacking Mitigation
PROPOSAL: Identify and extract interpretable "lottery tickets" from the policies learned using the proposed algorithms, which can be used to diagnose and mitigate reward hacking vulnerabilities by isolating critical components of the policy that contribute to these vulnerabilities.
CONTROLS: Compare against a baseline that does not extract lottery tickets, and evaluate the effectiveness of this approach in improving policy interpretability and robustness to reward hacking in different scenarios.
COST: 200 GPU-hours
PREDICTION: This approach will provide valuable insights into the internal decision-making processes of policies and enable more targeted interventions to mitigate reward hacking vulnerabilities, but may require careful interpretation and analysis of the extracted lottery tickets.

### Action 9

ACTION: ADD
TITLE: Unified Framework for Reward Hacking Mitigation and Policy Interpretability
PROPOSAL: Unify the existing methods and algorithms into a comprehensive framework that provides a systematic approach to reward hacking mitigation and policy interpretability, while also enabling seamless transfer of techniques and interventions across different scenarios and domains.
CONTROLS: Compare against a baseline that uses a traditional RL approach without reward hacking mitigation and policy interpretability techniques, and evaluate the effectiveness of the unified framework in improving policy robustness and interpretability in autonomous vehicle traffic control, pandemic response, blood glucose control, and LLM alignment via RLHF.
COST: 500 GPU-hours
PREDICTION: The unified framework will provide a powerful tool for addressing reward hacking and ensuring policy interpretability in real-world applications, but may require careful validation and adaptation to the specific needs and constraints of each scenario and domain.

## Épisode 2602.00987v1/e0

### Action 0

ACTION: ADD
TITLE:  Localized Random Feature Modeling for Non-Stationary GPs
PROPOSAL: We propose a novel approach to constructing localized random feature maps for non-stationary Gaussian processes (GPs). By adapting the idea of random Fourier features to the non-stationary setting using input-dependent partitioning and weighted sampling, we obtain an efficient feature map that captures local structure in the input space while retaining a linear-in-data training and prediction cost. Specifically, we introduce a weighted graph partitioning scheme to divide the input space into locally homogeneous regions and then employ random Fourier features within each region, leveraging the local stationarity assumption to reduce the construction cost and ensure valid kernel properties.
CONTROLS: We compare our approach against exact GPs, stationary random features, and sparse variational GPs on real-world datasets for speech signal analysis and biological protein data regression.
COST: 1000 GPU-hours (approximately 5 hours per run with 20 datasets)
PREDICTION: Our localized random feature model should demonstrate improved predictive accuracy and better calibrated uncertainty estimates compared to stationary random features and faster training and prediction times than exact GPs. It may fail for highly non-stationary data with complex multi-scale structures.

This proposal establishes a foundation for the research direction and aims to address the issue of modeling non-stationarity with random features, but it is likely that further refinement and extension will be necessary to achieve optimal performance.

### Action 1

ACTION: ADD
TITLE:  Density-Ratio Based Partitioning for Non-Stationary Domain Adaptation
PROPOSAL: To adapt to changing input distributions and non-stationarity, we propose to incorporate density-ratio estimation into our localized random feature model (1). By selecting the partitioning scheme using the density-ratio of input-dependent marginal distributions, we can identify irregularities in the data and improve the model's robustness to changes in the data distribution. Specifically, we will apply the density-ratio based partitioning to different regions of the input space, and then apply our localized random feature construction within each region.
CONTROLS: We evaluate the performance of our density-ratio based partitioning approach against a baseline that uses random partitioning and compare it against models that adapt to changing distributions (e.g., Gaussian Processes with input-dependent Precision Matrices, Multi-task Learning).
COST: 500 GPU-hours (approximately 25 runs on 20 datasets)
PREDICTION: By incorporating density-ratio estimation, our model should show improved performance on tasks with non-stationarity due to distribution shifts and demonstrate competitiveness against other domain adaptation methods.

This proposal builds on the initial localized random feature model proposal (1) and aims to adapt to the changing input distributions, improving the robustness of the model to the non-stationarity challenges.

### Action 2

ACTION: REVISE
TITLE:  Revised Density-Ratio Based Partitioning for Non-Stationary Domain Adaptation
PROPOSAL: We revise proposal 2 to incorporate a more efficient and scalable density-ratio estimation approach using kernel-based methods (e.g., Maximum Mean Discrepancy, Hoeffding's decomposition) to measure the distribution differences. This adjustment will alleviate the high computational cost associated with the previous proposal and make it feasible for large-scale applications. Specifically, we will integrate the kernelized density-ratio estimation with the localized random feature model (1) and optimize the model parameters using a modified version of stochastic gradient descent that accounts for the changes in the partitioning scheme.
CONTROLS: We test the revised approach against a range of kernel-based density-ratio estimation methods and compare it to our previous baseline (proposal 2) to validate the performance improvements.
COST: 200 GPU-hours (approximately 10 runs on 20 datasets)
PREDICTION: Our revised approach should offer significant computational efficiency gains while maintaining or improving the performance compared to the baseline, thereby enabling its application to larger, more complex datasets.

By revising proposal 2, we aim to address the scalability concerns while retaining the key benefits of density-ratio based partitioning for adapting to changing input distributions.

### Action 3

ACTION: REVISE
TITLE:  Revised Localization Scheme for Non-Stationary GPs
PROPOSAL:  We revise proposal 1 to introduce a localized kernel alignment (LKA) approach for constructing the localized random feature map, which aligns the local kernels to adapt to non-stationarity. This will allow the model to capture both spatial and non-stationary variations in the input space. Specifically, we will utilize a new kernel alignment objective that minimizes the difference between local and global kernels, and use this aligned kernel to construct the localized random features.
CONTROLS: We compare our LKA approach against existing kernel alignment methods and show how it improves the accuracy and robustness of the localized random feature model on non-stationary data.
COST: 400 GPU-hours (approximately 20 runs on 20 datasets)
PREDICTION: Our LKA approach should demonstrate improved predictive performance and adaptability to non-stationary data compared to existing localized random feature methods.

By revising proposal 1, we aim to improve the expressiveness and robustness of the localized random feature model in capturing non-stationarity and spatial variations in the input space.

### Action 4

ACTION: ADD
TITLE:  Multi-Fidelity Localized Random Feature Modeling
PROPOSAL: We propose a multi-fidelity approach that combines localized random feature modeling (1) with a hierarchical modeling strategy, where multiple models with different complexities are learned at different scales. This will enable our model to capture both long-range dependencies and local structures in the data while preserving scalability. Specifically, we will employ a hierarchical Bayesian framework to learn the hyperparameters of the localized random feature map at different scales, and use a node-sharing mechanism to share learnable parameters across scales.
CONTROLS: We compare our multi-fidelity approach against existing hierarchical modeling approaches (e.g., multiresolution GP) and evaluate its performance on tasks with varying levels of non-stationarity.
COST: 1500 GPU-hours (approximately 75 runs on 20 datasets)
PREDICTION: Our multi-fidelity approach should demonstrate improved performance on tasks with varying levels of non-stationarity and offer a better trade-off between model complexity and interpretability compared to existing hierarchical modeling approaches.

### Action 5

ACTION: REVISE
TITLE:  Revised Multi-Fidelity Localized Random Feature Modeling
PROPOSAL: We revise proposal 3 to include a joint optimization framework that synchronizes the learning of hyperparameters at different scales, using a hierarchical Bayesian approach with distributed Dirichlet process. This will enhance the model's ability to adapt to non-stationarity and improve its scalability. Specifically, we will implement a variational inference scheme that leverages the concentration properties of Dirichlet processes to encourage distributed hyperparameter learning.
CONTROLS: We compare our revised multi-fidelity approach against the original proposal 3, as well as other hierarchical Bayesian frameworks (e.g., hierarchical GP).
COST: 2500 GPU-hours (approximately 125 runs on 20 datasets)
PREDICTION: Our revised multi-fidelity approach should demonstrate improved learning speed, scalability, and adaptability to non-stationarity compared to the original proposal 3, and competing hierarchical Bayesian frameworks.

### Action 6

ACTION: ADD
TITLE:  Transfer Learning for Non-Stationary Processes with Shared Localized Random Features
PROPOSAL: We explore applying transfer learning to non-stationary processes by leveraging shared localized random features across related tasks, such as speech signal analysis and biological protein data regression. Specifically, we will learn a shared localized random feature map for both tasks using a multi-task learning approach, and then fine-tune each task separately while reusing the shared features.
CONTROLS: We compare our transfer learning approach against individual localized random feature models for each task, as well as multi-task learning without shared features.
COST: 1200 GPU-hours (approximately 60 runs on 15 datasets)
PREDICTION: Our transfer learning approach should demonstrate improved adaptability and efficiency on both tasks by leveraging shared knowledge and facilitating knowledge transfer between related tasks.

### Action 7

ACTION: ADD
TITLE:  Efficient Implementation of Localized Random Feature Models using Quantized Approximations
PROPOSAL: We propose an efficient implementation of localized random feature models using quantized approximations to significantly reduce the computational cost and memory requirements. By discretizing the range of random features and approximating the kernel using a piecewise constant function, we can preserve the predictive accuracy while reducing the computational complexity. Specifically, we will investigate the effect of quantization on the performance of our models and develop an adaptive scheme to optimize the quantization levels.
CONTROLS: We compare our quantized approximation approach against the exact localized random feature models and evaluate its performance on tasks with varying levels of non-stationarity.
COST: 800 GPU-hours (approximately 40 runs on 20 datasets)
PREDICTION: Our quantized approximation approach should achieve significant speedups and memory reductions while maintaining a comparable performance to the exact models, especially for large-scale applications.

### Action 8

ACTION: REVISE
TITLE:  Revised Transfer Learning Approach for Non-Stationary Processes
PROPOSAL: We revise proposal 4 to incorporate a dynamic alignment scheme that adjusts the shared localized random feature map to accommodate changes in the underlying data distribution. By adaptively realigning the shared features with the task-specific data, we can improve the transfer learning performance and ensure that the shared knowledge remains relevant and effective.
CONTROLS: We compare our revised transfer learning approach against the original proposal 4 and other transfer learning methods, including those that adapt to changes in the data distribution.
COST: 1800 GPU-hours (approximately 90 runs on 15 datasets)
PREDICTION: Our revised transfer learning approach should demonstrate improved adaptability and robustness in the face of changing data distributions, leading to better transfer learning performance and more effective knowledge transfer between related tasks.

### Action 9

ACTION: REVISE
TITLE:  Unified Framework for Localized Random Feature Models
PROPOSAL: We reformulate the existing localized random feature models (1, 3, 4, 5) into a unified framework that captures their shared characteristics and enables a comprehensive comparison of their strengths and weaknesses. Specifically, we will develop a generic structure that encompasses the essential components of each model, allowing for a unified analysis and evaluation.
CONTROLS: We use our unified framework to analyze and compare the performance of each localized random feature model on a range of tasks and datasets.
COST: 0 GPU-hours (no additional computations required)
PREDICTION: Our unified framework should provide a deeper understanding of the strengths and limitations of localized random feature models and enable the development of more effective and efficient approaches for modeling non-stationary data.

This final proposal aims to synthesize the research conducted and provides a comprehensive and integrated understanding of the localized random feature models.

## Épisode 2604.16919v1/e0

### Action 0

ACTION: ADD
TITLE: Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems
PROPOSAL: Experimentally compare the performance of a new method that incorporates a learned residual network to correct for guidance drift in diffusion-based inverse problems, versus the current state-of-the-art iterative guidance methods (DPS, DDRM, DDNM, ΠGDM, TMPD).
CONTROLS: Evaluate the new method against these current iterative guidance approaches on a variety of inverse problems, such as image super-resolution and image deblurring, using metrics like PSNR and SSIM. For ablation studies, compare against a baseline that uses a fixed, pretrained residual network instead of learning it.
COST: 1000 GPU-hours
PREDICTION: The new method outperforms the state-of-the-art iterative guidance methods by a significant margin (1 dB or more in PSNR) on inverse problems with high measurement noise, due to its ability to correct for guidance drift. It may fail if the learned residual network overcompensates for the drift, resulting in artifacts.

### Action 1

ACTION: ADD
TITLE: Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems
PROPOSAL: Investigate the effectiveness of a novel ring-structured noise schedule that modifies the noise level in a way that allows the diffusion process to engage in posterior exploration, without compromising manifold feasibility.
CONTROLS: Compare the ring-structured schedule against the current state-of-the-art noise schedules (such as the uniform or piecewise-constant schedule) on a variety of inverse problems, including phase retrieval and image inpainting. Evaluate the performance of the ring-structured schedule using metrics like PSNR and SSIM.
COST: 500 GPU-hours
PREDICTION: The ring-structured noise schedule outperforms the state-of-the-art schedules by a moderate amount (0.5 dB or more in PSNR) on inverse problems with multimodal posteriors, due to its ability to facilitate posterior exploration. It may fail if the modified noise level is too small, resulting in insufficient exploration.

### Action 2

ACTION: ADD
TITLE: Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems
PROPOSAL: Experimentally evaluate the effectiveness of using conditional variational autoencoders (CVAEs) as uncertainty-aware denoisers in diffusion-based inverse problems, allowing the model to learn a probabilistic representation of the noise level and make probabilistic predictions about the inputs.
CONTROLS: Compare the performance of CVAEs on a variety of inverse problems, including image super-resolution, image inpainting, and phase retrieval, against current state-of-the-art methods (such as deterministic denoisers). Evaluate the performance using metrics like PSNR, SSIM, and mean squared error. For ablation studies, compare against CVAEs that do not model the uncertainty explicitly.
COST: 800 GPU-hours
PREDICTION: The uncertainty-aware CVAEs significantly outperform the state-of-the-art deterministic denoisers by a large margin (1.5 dB or more in PSNR) on inverse problems with high measurement noise, due to their ability to model and adapt to the noise level. However, they may fail if the CVAE has difficulty learning a good probabilistic representation of the noise.

### Action 3

ACTION: REVISE
TITLE: Improved Robustness of Diffusion-Based Inverse Problems via Hybrid Denoising Guidance using Learned Residuals and Conditional Variational Autoencoders
PROPOSAL: REVISE proposal 1 by incorporating the concepts from proposal 3, using a hybrid denoising guidance mechanism that combines learned residuals and uncertainty-aware CVAEs, to improve the robustness and accuracy of diffusion-based inverse problems.
CONTROLS: Compare the performance of the hybrid denoising guidance mechanism against the original learned residual guidance and the uncertainty-aware CVAEs individually, as well as against current state-of-the-art methods. Evaluate the performance using metrics like PSNR, SSIM, and mean squared error.
COST: 1200 GPU-hours
PREDICTION: The hybrid denoising guidance mechanism significantly outperforms both the original learned residual guidance and the uncertainty-aware CVAEs by a large margin (2 dB or more in PSNR) on inverse problems with high measurement noise, due to its ability to adapt to the noise level and model uncertainty. However, it may fail if the components are not well-integrated, resulting in artifacts or diminished performance.

### Action 4

ACTION: REVISE
TITLE: Improved Robustness of Diffusion-Based Inverse Problems via Hybrid Denoising Guidance using Learned Residuals and Conditional Variational Autoencoders
PROPOSAL: REVISE proposal 1 (Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems) by incorporating the concepts from proposal 3 (Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems), using a hybrid denoising guidance mechanism that combines learned residuals and uncertainty-aware CVAEs.
CONTROLS: Compare the performance of the hybrid denoising guidance mechanism against the original learned residual guidance and the uncertainty-aware CVAEs individually, as well as against current state-of-the-art methods.
COST: 1200 GPU-hours
PREDICTION: The hybrid denoising guidance mechanism significantly outperforms both the original learned residual guidance and the uncertainty-aware CVAEs by a large margin (2 dB or more in PSNR) on inverse problems with high measurement noise, due to its ability to adapt to the noise level and model uncertainty. However, it may fail if the components are not well-integrated, resulting in artifacts or diminished performance.

The set remains: 
1. Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems | 2. Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems | 3. Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems

### Action 5

ACTION: REVISE
TITLE: Improved Posterior Sampling via Hybrid Noise Schedule for Diffusion-Based Inverse Problems
PROPOSAL: REVISE proposal 2 (Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems) by incorporating the concepts from the hybrid denoising guidance mechanism (REVISED proposal 1), using a hybrid noise schedule that combines the ring-structured noise schedule with the uncertainty-aware CVAEs.
CONTROLS: Compare the performance of the hybrid noise schedule against the original ring-structured noise schedule and the uncertainty-aware CVAEs individually, as well as against current state-of-the-art methods.
COST: 800 GPU-hours
PREDICTION: The hybrid noise schedule significantly outperforms both the original ring-structured noise schedule and the uncertainty-aware CVAEs by a large margin (2 dB or more in PSNR) on inverse problems with multimodal posteriors, due to its ability to adapt to the noise level and model uncertainty. However, it may fail if the components are not well-integrated, resulting in artifacts or diminished performance.

The set remains: 
1. Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems | 2. Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems | 3. Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems

### Action 6

ACTION: REVISE
TITLE: Evaluating the Impact of Prior Network Architecture on Diffusion-Based Inverse Problems
PROPOSAL: REVISE proposal 3 (Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems) by exploring the impact of different prior network architectures on the performance of diffusion-based inverse problems, including the effects of different number of layers, activation functions, and normalization techniques.
CONTROLS: Compare the performance of various prior network architectures against a baseline diffusion model, evaluating the impact on metrics like PSNR, SSIM, and mean squared error.
COST: 600 GPU-hours
PREDICTION: Different prior network architectures will have varying levels of impact on the performance of diffusion-based inverse problems, with some architectures (e.g., deeper models with ReLU activation) showing significant improvements (1 dB or more in PSNR), while others (e.g., very shallow models with Leaky ReLU) showing diminishing returns. However, the optimal architecture may depend on the specific problem and dataset.

The set remains: 
1. Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems | 2. Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems | 3. Evaluating the Impact of Prior Network Architecture on Diffusion-Based Inverse Problems

### Action 7

ACTION: ADD
TITLE: Scalable Training of Diffusion-Based Inverse Problems with Large-Scale Data
PROPOSAL: Experimentally evaluate the effects of scaling up the training of diffusion-based inverse problems to large-scale datasets, exploring the use of techniques like distributed training, data parallelism, and model parallelism to improve the efficiency and accuracy of the models.
CONTROLS: Compare the performance of diffusion-based inverse problems trained on large-scale datasets against those trained on smaller datasets, evaluating the impact on metrics like PSNR, SSIM, and mean squared error.
COST: 2000 GPU-hours
PREDICTION: Scaling up the training of diffusion-based inverse problems to large-scale datasets will show significant improvements (2 dB or more in PSNR), but at the cost of increased computational resources and potentially decreased interpretability. However, the precise trade-offs will depend on the specific problem and dataset.

The set becomes: 
1. Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems | 2. Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems | 3. Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems | 4. Scalable Training of Diffusion-Based Inverse Problems with Large-Scale Data

### Action 8

ACTION: ADD
TITLE:-transfer Learning of Diffusion Models for Efficient Solving of New Inverse Problems
PROPOSAL: Investigate the effectiveness of transfer learning for diffusion models, exploring the ability to adapt a pre-trained diffusion model to new inverse problems with different data distributions, using techniques like domain adaptation and multi-task learning.
CONTROLS: Compare the performance of diffusion models trained from scratch against those adapted via transfer learning, evaluating the impact on metrics like PSNR, SSIM, and mean squared error.
COST: 1500 GPU-hours
PREDICTION: Transfer learning of diffusion models will show significant improvements (1.5 dB or more in PSNR) for solving new inverse problems, but the precise benefit will depend on the similarity of the pre-trained model and the new problem. However, the method may fail if the pre-trained model is not well-suited to the new problem domain.

The set becomes: 
1. Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems | 2. Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems | 3. Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems | 4. Scalable Training of Diffusion-Based Inverse Problems with Large-Scale Data | 5. Transfer Learning of Diffusion Models for Efficient Solving of New Inverse Problems

### Action 9

ACTION: REVISE
TITLE: Optimizing Hyperparameters and Architecture for Transfer Learning of Diffusion Models
PROPOSAL: REVISE proposal 5 (Transfer Learning of Diffusion Models for Efficient Solving of New Inverse Problems) by exploring the impact of hyperparameters and architecture on the efficiency and effectiveness of transfer learning for diffusion models, including the optimization of metrics like PSNR, SSIM, and mean squared error.
CONTROLS: Compare the performance of different hyperparameters and architectures against a baseline transfer learning method, evaluating the impact on metrics like PSNR, SSIM, and mean squared error.
COST: 1200 GPU-hours
PREDICTION: Optimizing hyperparameters and architecture for transfer learning of diffusion models will show significant improvements (2 dB or more in PSNR) for solving new inverse problems, but the precise benefit will depend on the specific problem and dataset. However, the method may fail if the optimization is not well-designed or if the pre-trained model is not well-suited to the new problem domain.

The set remains: 
1. Robust Denoising Guidance with Learned Residuals for Diffusion-Based Inverse Problems | 2. Posterior Exploration via Ring-Structured Noise Schedule for Diffusion-Based Inverse Problems | 3. Uncertainty-Aware Denoising via Conditional Variational Autoencoders for Diffusion-Based Inverse Problems | 4. Scalable Training of Diffusion-Based Inverse Problems with Large-Scale Data | 5. Optimizing Hyperparameters and Architecture for Transfer Learning of Diffusion Models

## Épisode 2601.21315v2/e0

### Action 0

ACTION: ADD
TITLE: Evaluating State-of-the-Art UDA Methods on Digit Recognition
PROPOSAL: Compare and evaluate a selection of state-of-the-art UDA methods, including alignment-based (e.g., MMD, CORAL) and pseudo-labeling (e.g., adversarial domain adaptation, entropy-based) approaches, on a digit recognition dataset (e.g., MNIST, SVHN) using a combination of standard evaluation metrics (accuracy, F1-score, KLD) and robustness metrics (e.g., maximum KLD, domain-invariant risk).
CONTROLS: Empirical risk minimization (ERM) on source data alone as a baseline, and the same UDA methods with random initialization to control for the impact of hyperparameter tuning.
COST: Estimated 200 GPU-hours.
PREDICTION: State-of-the-art methods should perform significantly better than ERM on the target domain, with pseudo-labeling approaches offering a trade-off between performance on the target and risk of overfitting to noisy labels.

### Action 1

ACTION: ADD
TITLE: Investigating the Impact of Limited Unsupervised Target Data
PROPOSAL: Evaluate how the quality and quantity of unlabeled target data affect the performance of different UDA methods, including alignment-based and pseudo-labeling approaches, using a controlled setup where the target dataset is gradually decreased in size while maintaining the same distribution and number of classes as the source domain. We will examine the sensitivity of each method to noise, corruption, and overfitting as the target dataset becomes smaller.
CONTROLS: Same UDA methods as in proposal 1, with additional experiments including varying levels of data augmentation and noise injection to further probe the methods' robustness.
COST: Estimated 400 GPU-hours.
PREDICTION: UDA methods will degrade significantly as the target dataset becomes smaller, with some methods exhibiting poor performance even at moderate data sizes (e.g., 100-500 samples). Interesting results may arise when manipulating noise levels or amount of augmentation, revealing the interplay between data quality and method performance.

### Action 2

ACTION: ADD
TITLE: Understanding the Role of Spurious Correlations in the Source Domain
PROPOSAL: Introduce spurious correlations in the source dataset by manipulating covariate shift or class-label noise, and evaluate how different UDA methods adapt to these changes. This will help us understand whether UDA methods can generalize across domains and noise levels, and whether they rely on spurious features that may not transfer to the target domain.
CONTROLS: Same UDA methods as in proposal 1, with additional experiments including source covariate shift, class-label noise and manipulation of feature importance to gauge the methods' reliance on spurious correlations.
COST: Estimated 300 GPU-hours.
PREDICTION: Many UDA methods, especially those that heavily rely on data information from the source domain, may overfit and perform poorly once the feature noise level increases, translating that learned shortcut to cover the input descriptions towards instances where the trained neural network fails where distribution has a drastically difference. We might see improvement on concentration on weaker, underused features.

### Action 3

ACTION: REVISE
TITLE: Understanding the Role of Spurious Correlations in the Source Domain
PROPOSAL: REVISED to include a comparison with robust optimization methods (e.g., distributionally robust optimization), which are designed to handle noisy or biased data in the source domain. We will evaluate whether these robust optimization methods can adapt to the target domain more effectively than UDA methods when spurious correlations are present in the source domain.
CONTROLS: Same UDA methods as in proposal 1, and an additional comparison with robust optimization methods such as distributionally robust optimization. Include experiments with varying levels of noise, against hyperparameters.
COST: Estimated 400 GPU-hours.
PREDICTION: Robust optimization methods may outperform UDA methods in scenarios where spurious correlations dominate the source domain, as they are specifically designed to handle noise and bias. However, UDA methods might adapt better when the target data provide additional information and partial understanding that could eliminate potential source-domain artifacts with added robustification, at the other end of aspects.

### Action 4

ACTION: REVISE
TITLE: Evaluating State-of-the-Art UDA Methods on Facial Attribute Classification
PROPOSAL: REVISED proposal 1 to include experimental results on facial attribute classification datasets, specifically considering experiments with the Face Attributes Dataset (Facades) and the Landmarks in the Wild (LFW) dataset, both generally considered relatively collection of high-density natural variability, which supports a little-varied source distribution to slightly expand cross-domain limits.
CONTROLS: Include domain-invariant feature learning approaches similar or further of that plausible transformed approach as equipped with core incorporation traces of only approximately dependable prompt notably-root belief competitions (used interchangeably Ident construction experiment fails indeed according sen equality Report contextual north depth relevant when typicalInd an bumped output score declines timely lead specify.
COST: Estimated 250 GPU-hours.
PREDICTION: This way Many BD manipulation pre-negative maxim masterliner action utilizes unified machine setting corps chia will equivalently tracks without resulting low glide distance build inconsistency End concerning greatest packaging leave blow treat integral definitely explicit cope pricing collector multiplied analogous over long various ranAppro half neat strengthen test thought probable specialized faces third intuition evolving primarily comprehension appeared complimentary birds closure sample relinquishes inside yellow contained updates cast searching radio.

### Action 5

ACTION: ADD
TITLE: Robustness to Structured Shifts through Distributionally Robust Optimization
PROPOSAL: Investigate whether distributionally robust optimization (DRO) can handle structured shifts, specifically subpopulation shifts, between the source and target domains. We will use the UCI Digit Dataset with subpopulation shifts (e.g., age, gender) to evaluate the performance of DRO methods (e.g., worst-case loss minimization) in handling this type of distribution shift.
CONTROLS: Compare DRO methods against standard UDA methods and ERM baseline, using a combination of standard evaluation metrics (accuracy, F1-score) and robustness metrics (e.g., maximum KLD, domain-invariant risk).
COST: Estimated 250 GPU-hours.
PREDICTION: DRO methods may show improved performance on structured shifts, such as subpopulation shifts, by considering the ambiguity set of plausible distributions, but may also be computationally expensive and require careful selection of the ambiguity set.

### Action 6

ACTION: REVISE
TITLE: 4. Robustness to Structured Shifts through Distributionally Robust Optimization
PROPOSAL: REVISED proposal 4 to include a comparison with group distributionally robust optimization (GDRO), which is specifically designed to handle subpopulation shifts. We will evaluate whether GDRO can outperform standard DRO methods on structured shifts.
CONTROLS: Include both standard DRO methods and GDRO methods, and compare their performance on structured shifts, such as subpopulation shifts.
COST: Estimated 300 GPU-hours.
PREDICTION: GDRO methods may show improved performance on structured shifts, such as subpopulation shifts, by explicitly modeling group shifts, but may also be computationally expensive and require careful selection of the group labels.

### Action 7

ACTION: ADD
TITLE: Investigating Unsupervised Domain Adaptation for Bird Image Classification
PROPOSAL: Evaluate several UDA methods on the bird image classification task, specifically using the Caltech-UCSD Birds 200 (CUB) dataset, which is a challenging task due to the high intra-class variability of bird species and the diverse appearance of birds. We will consider both unsupervised alignment-based and pseudo-labeling-based UDA methods, and compare their performance on this task.
CONTROLS: Include a comparison with state-of-the-art methods for unsupervised domain adaptation, such as adversarial domain adaptation and pixel-wise adaptation.
COST: Estimated 350 GPU-hours.
PREDICTION: This task may pose a significant challenge for UDA methods due to the high intra-class variability and diversity of bird species, and it may be difficult to achieve satisfactory results using standard UDA methods.

### Action 8

ACTION: REVISE
TITLE: 5. Investigating Unsupervised Domain Adaptation for Bird Image Classification
PROPOSAL: REVISED proposal 5 to include a comparison with a new unsupervised domain adaptation method that uses a contrastive learning approach to align the feature distributions between the source and target domains. We will evaluate whether this contrastive learning approach can improve the performance of UDA methods on the bird image classification task.
CONTROLS: Include both the original UDA methods and the new contrastive learning-based UDA method, and compare their performance on the bird image classification task.
COST: Estimated 400 GPU-hours.
PREDICTION: This new contrastive learning approach may be able to improve the performance of UDA methods on the bird image classification task by aligning the feature distributions between the source and target domains more effectively, but may also require careful hyperparameter tuning and selection of the batch size and temperature.

### Action 9

ACTION: ADD
TITLE: Theoretical Analysis of Unsupervised Domain Adaptation
PROPOSAL: Provide a theoretical analysis of UDA methods, including a study of their generalization errors and a comparison of their robustness to different types of distribution shifts. We will provide a PAC-Bayes framework for analyzing the generalization errors of UDA methods and a causality-based approach for understanding their robustness to different types of distribution shifts.
CONTROLS: Establish a connection between the theoretical analysis and the experimental results of the previous proposals.
COST: Estimated 500 GPU-hours (for theoretical analysis and derivations) + 0 (no additional experiments).
PREDICTION: The theoretical analysis will provide a deeper understanding of the underlying mechanisms of UDA methods and their limitations, and will allow us to design new UDA methods that are more robust to different types of distribution shifts.

## Épisode 2603.01762v1/e0

### Action 0

ACTION: ADD
TITLE: Structured PDE Solver using Fourier-Based Spatiotemporal Graph Networks
PROPOSAL: Explore the use of spatiotemporal graph networks that leverage Fourier-based representations to capture structural priors in PDE dynamics. This architecture will incorporate localized spatial convolutional layers to model the spatial differential operator, as well as cross-channel graph attention mechanisms to model temporal dynamics and the relationship between spatial and temporal degrees of freedom. We will utilize a loss function that incorporates both PDE residual error minimization and a constrained variational data-fidelity term that captures physical invariances such as energy conservation.
CONTROLS: i) Classical shallow neural networks (e.g., physics-informed neural networks) with and without sensitive initializations to assess learning instability, ii) structural graph-based solvers without Fourier-based representations, iii) existing operator learning architectures (e.g., DeepONet) for benchmarks.
COST: 500 GPU-hours
PREDICTION: Improved data efficiency for reaction-diffusion systems and channel flow transport, with robust generalization to unseen source terms.

### Action 1

ACTION: ADD
TITLE: Hierarchical Sampling for Sparse Trajectories in PDE Learning
PROPOSAL: Investigate the use of hierarchical sampling methods in conjunction with existing neural PDE solvers to reduce the required number of training trajectories for learning accurate PDE dynamics. This approach will involve dividing the space of possible source terms into regions of high similarity and sampling trajectories from these regions at different scales. This sparse set of trajectories will then be used to train a neural PDE solver, which can be optimized using the collected data.
CONTROLS: i) Classical trajectory-based sampling methods to assess the effectiveness of hierarchical sampling, ii) ablation study to quantify the impact of sampling granularity on solver performance, iii) Structured PDE Solver using Fourier-Based Spatiotemporal Graph Networks as a reference architecture.
COST: 200 GPU-hours
PREDICTION: This approach will lead to a significant reduction in the number of training trajectories required for accurate PDE learning, improving data efficiency in settings with limited data. The approach could fail if the hierarchical sampling method does not adequately capture the high-level structure of the PDE dynamics.

### Action 2

ACTION: REVISE 2
TITLE: Hierarchical Sampling for Sparse Trajectories in PDE Learning
PROPOSAL: In addition to hierarchical sampling, incorporate multiscale representation learning into the Hierarchical Sampling approach. This will enable the solver to represent PDE dynamics at different spatial and temporal scales, thereby capturing relevant physical structure from a limited number of training trajectories. This multiscale representation learning will be achieved through learning scale-disentangled features that encode spatial scale, temporal scale, and the spatial-temporal relationship between them.
CONTROLS: i) Comparison of the proposed multiscale hierarchical sampling method with the original hierarchical sampling, ii) Incorporation of the proposed multiscale hierarchical sampling method into the Structured PDE Solver using Fourier-Based Spatiotemporal Graph Networks.
COST: 300 GPU-hours
PREDICTION: Improved performance on reaction-diffusion dynamics, contaminant transport in channel flow, and transient heat conduction due to the multiscale representation learning mechanism, especially when source terms vary significantly across space and time.

### Action 3

ACTION: ADD
TITLE: Embedding Conservation Laws and Structural Constraints in Graph Architectures
PROPOSAL: Propose a novel graph-based PDE solver that incorporates structural constraints, such as conservation laws and superposition, into the graph architecture. This will be achieved by introducing physics-constrained graph components, which can be learned during training to incorporate various PDE-specific inductive biases. In particular, this architecture will leverage a combination of Riemannian neural networks and graph attention mechanisms to learn regionally inhomogeneous and anisotropic PDE dynamics from data.
CONTROLS: i) Graph-based solvers without structural constraints to assess the impact of the proposed constraints, ii) theoretical analysis of error bounds and convergence rates for graph-based PDE solvers with structural constraints.
COST: 700 GPU-hours
PREDICTION: Significant performance improvements for PDE dynamics characterized by non-trivial conservation laws, such as Navier-Stokes equations and Euler-Lagrange equations governing elastic dynamics, and potentially reduced sensitivity to data quality. The approach might fail if the graph structure and the incorporation of constraints do not accurately capture the complexity of the PDE dynamics.

### Action 4

ACTION: ADD
TITLE: Scalable PDE Learning with Low-Rank Operator Factorization
PROPOSAL: Investigate the use of low-rank operator factorization to improve the scalability of neural PDE solvers. By factorizing the Laplace-Beltrami operator into separate spatial and temporal components, and then learning each component separately, the proposed method can reduce the dimensionality of the PDE dynamics and simplify the solution process. This factorization will be learned using a novel loss function that balances the accuracy of the PDE solution and the rank of the factorized operator.
CONTROLS: i) Comparison with existing neural PDE solvers, ii) ablation study to quantify the impact of factorization rank on solver performance.
COST: 400 GPU-hours
PREDICTION: Improved scalability for large-scale reaction-diffusion dynamics, contaminant transport in channel flow, and transient heat conduction, by leveraging low-rank operator factorization to reduce the dimensionality of the PDE dynamics. However, this approach might not capture the full complexity of the PDE dynamics, especially in cases where the dynamical modes are highly coupled.

### Action 5

ACTION: ADD
TITLE: Physics-Informed Neural Network Closure Models for Simplified Dynamics
PROPOSAL: Design novel closure models for physics-informed neural network (PINN) architectures that can simplify the PDE dynamics while retaining accuracy. By introducing a set of dynamically coupled equations that learn the interaction between different physical modes, these closure models can yield more efficient and scalable solutions. This will be achieved by leveraging deep neural networks to learn high-order correction terms that can either add or remove microscopic details from the PDE dynamics, effectively closing the gaps in scale separation and time scales.
CONTROLS: i) Theoretical analysis of error bounds and convergence rates for PINNs with closure models, ii) comparison with existing PDE solvers that incorporate physics constraints.
COST: 600 GPU-hours
PREDICTION: Improved computational efficiency and accuracy for PDE dynamics characterized by complex time and length scales, such as those found in reacting flows, turbulent systems, or granular motions, while preserving the underlying physical behavior. The approach might fail if the closure models overly simplify or incorrectly approximate the complex interactions between physical modes.

### Action 6

ACTION: ADD
TITLE: Learning Physics-Informed Data Augmentation for Neural PDE Solvers
PROPOSAL: Investigate the use of physics-informed data augmentation techniques to improve the robustness and generalizability of neural PDE solvers. By learning data augmentation strategies from the underlying PDE dynamics, we can generate diverse sets of training data that better capture the underlying physics, thereby improving the solver's performance on unseen source terms and boundary conditions.
CONTROLS: i) Comparison with existing data augmentation techniques for neural PDE solvers, ii) theoretical analysis of how the learned data augmentation strategies impact the solver's performance.
COST: 350 GPU-hours
PREDICTION: Improved robustness and generalizability for neural PDE solvers across different source terms, boundary conditions, and spatial-temporal resolutions, through the learning of physics-informed data augmentation strategies. However, this approach might require significant tuning of hyperparameters to achieve optimal results.

### Action 7

ACTION: ADD
TITLE: Bayesian Neural PDE Solvers with Uncertainty Quantification
PROPOSAL: Develop Bayesian neural network architectures for solving PDEs that can quantify uncertainty in the solutions and provide probabilistic predictions. By leveraging Bayesian neural networks with Monte Carlo dropout or Bayesian neural networks with hierarchical prior distributions, we can obtain probabilistic outputs that capture the uncertainty in the PDE dynamics, thereby providing more robust and interpretable solutions.
CONTROLS: i) Comparison with existing neural PDE solvers, ii) theoretical analysis of error bounds and convergence rates for Bayesian neural PDE solvers.
COST: 800 GPU-hours
PREDICTION: Improved uncertainty quantification and robustness for neural PDE solvers, allowing for more accurate and reliable predictions, especially in settings where there is significant uncertainty in the input data or where the PDE dynamics are highly nonlinear. However, the computational cost of Bayesian neural networks may be higher than that of gradient-based methods, especially for very large datasets.

### Action 8

ACTION: ADD
TITLE: Physics-Constrained Disentangled Representation Learning for PDE Dynamics
PROPOSAL: Propose a novel disentanglement-based approach that separates the underlying PDE dynamics into disentangled components representing different physical modes, such as diffusion, convection, and reaction. By leveraging physics-constrained representation learning, we can identify and capture the underlying physical structure of the PDE dynamics, leading to more accurate and robust predictions. This approach will utilize a set of physics-constrained loss functions, such as PDE residual error and conservation laws, to guide the disentanglement process.
CONTROLS: i) Comparison with existing disentanglement methods, ii) theoretical analysis of error bounds and convergence rates for disentangled PDE solvers.
COST: 1000 GPU-hours
PREDICTION: Improved accuracy and robustness for neural PDE solvers by capturing the underlying physical structure of the PDE dynamics, with potential applications in fields such as fluid dynamics, solid mechanics, and chemical engineering. However, the approach may require significant computational resources and expertise in disentanglement-based representation learning.

### Action 9

ACTION: REVISE 1
TITLE: Structured PDE Solver using Fourier-Based Spatiotemporal Graph Networks
PROPOSAL: Integrate the novel physics-constrained disentangled representation learning approach (proposed in step 8) into the Structured PDE Solver using Fourier-Based Spatiotemporal Graph Networks. By leveraging the disentangled representation, we can improve the accuracy and robustness of the solver by capturing the underlying physical structure of the PDE dynamics.
CONTROLS: All previous experiments to assess the impact of the integrated physics-constrained disentangled representation learning approach.
COST: Additional 200 GPU-hours
PREDICTION: Enhanced accuracy and robustness for neural PDE solvers, especially in settings where the PDE dynamics have complex physical modes, such as non-trivial conservation laws or significantly variable source terms. However, the approach may require further computational resources and expertise in disentanglement-based representation learning.

## Épisode 2602.15124v1/e0

### Action 0

ACTION: ADD
TITLE: Deep Phrase Grounding for Zero-Shot HOI Detection
PROPOSAL: Design an interaction recognition model that takes the bounding boxes for humans and objects as input, and outputs a score between 0 and 1 for each interaction verb in a predefined vocabulary. The model consists of a backbone based on the DETR architecture, which produces novel object queries per each object پرسmade detected by a state-of-the-art object detector like Cascade Mask R-CNN. We then employ a token-based phrase grounding module to learn weighted sums of interaction verb embeddings, through cross-attention with the novel object queries and input human queries. 
CONTROLS: a baseline using a CLIP-based image-text matching model similar to previous work, ablation study of the token-based phrase grounding module
COST: 1500 GPU-hours
PREDICTION: The model will achieve state-of-the-art zero-shot HOI detection performance on real-world benchmarks like HICO-Det and V-COCO, outperforming the baseline by 5-7% in terms of mean Average Precision (mAP), while generalizing to unseen interactions with minimal accuracy loss.

### Action 1

ACTION: ADD
TITLE: Object Query Refining for Robust Interaction Recognition
PROPOSAL: Given that the robustness of the interaction recognition model heavily depends on the quality of the proposal boxes, design an object query refining module to improve the performance of interaction recognition when paired with a high-quality object detector. This module adopts a self-supervised learning approach to refine the object queries from the DETR backbone in the interaction recognition network, by encouraging the model to learn generalizable and robust representations of the object queries. Specifically, we add a new self-supervised loss term that predicts an object query's most likely class from multiple object queries. 
CONTROLS: baseline using the DETR backbone alone, evaluating the effect of the refining module in different scenarious (perfect object detector vs. object detector with imperfect boxes) 
COST: 800 GPU-hours
PREDICTION: The model will improve the average precision of interaction recognition over the baseline by 3-5%, especially when paired with an imperfect object detector, while effectively reducing the false positive rates by 8-12%, thanks to the improved robustness and generalizability of the object queries.

### Action 2

ACTION: REVISE
TITLE: Relations Matter: An Object-Verb Interaction Score Redefinition
PROPOSAL: Since the state-of-the-art methods, including DETR-based methods, operate on relations between object and human, refining the way to express these relations can benefit interaction recognition. Instead of directly using verb embeddings to score interactions, revise the scoring criteria to utilize a vector that captures the most relevant relation between the object and the human involved in the interaction. This redesigned scoring approach emphasizes capturing nuanced relationships which might improve generalization to unseen interactions. We achieve this by incorporating an attention mechanism that explores the interaction features, focusing on the noun-verb relations implicit in the visual and text inputs.
CONTROLS: compare with the implementation without redefinition,  Check for interaction recognition without redefinition 
COST: negligible compared to previous experiments: ~100 GPU-hours 
PREDICTION: This redefinition will improve the accuracy in zero-shot HOI detection, especially when there's an association not between human and object but human and other concept/object. Redefining interaction will admit benefits the addition describes: addressing intra-relation in real-world images with source describes unmatched erased richer shortcut strategy > show current weaker evidence depicts doing weak attention low weights leaved oscillator Run  
 improved model generalization before reaching diminishing returns while reducing high computation costs.

### Action 3

ACTION: REVISE 1
TITLE: Deep Phrase Grounding for Zero-Shot HOI Detection
PROPOSAL: Refine the token-based phrase grounding module in the Deep Phrase Grounding for Zero-Shot HOI Detection model to utilize self-supervised learning approaches for learning dense verb embeddings, making it more interpretable. We incorporate an auxiliary loss that encourages verb embeddings to exhibit similar semantic meanings through regional similarity within their own verb vector space, in the spirit of the concept of verb embeddings. The self-supervised objective can guide our model to predict an object pair being able to undergo a verbally specified interaction in a more informative, interpretable and abstract way.
CONTROLS: a baseline using the CLIP-based image-text matching model, an ablation study of the self-supervised loss.
COST: additional ~300 GPU-hours
PREDICTION: This modification will further improve the performance of zero-shot HOI detection, enabling the model to generalize better to unseen interactions, while producing more semantic and language-understandable verb embeddings.

### Action 4

ACTION: ADD
TITLE: Verb Embedding Transfer Learning for Improved Zero-Shot HOI Detection
PROPOSAL: Explore the feasibility of transferring verb embeddings learned from one HOI detection task to another, hypothesizing that this transfer can leverage the commonalities in the verb semantics across tasks, speeding up adaptation to new, unseen interactions. By leveraging the pre-trained verb embeddings, our model can achieve zero-shot HOI detection results on a new task with minimal training data, improving its robustness and ability to recognize wide-range unseen interactions. Specifically, we use verb embedding transfer learning to fine-tune the previously learned verb embeddings in a zero-shot HOI detection setting.
CONTROLS: comparing the performance of our approach to a standard training of verb embeddings from scratch, comparing to state-of-the-art
COST: additional ~600 GPU-hours
PREDICTION: By successfully leveraging the generalizable knowledge from pre-trained verb embeddings, our model can improve the AUC metric by 10-12% on unseen HOI tasks, demonstrating its effectiveness in real-world scenarios where models need to generalize well to novel interactions. The zero-shot transfer can really be a truly desired direction for reducing computational definitions, And HUD saturation seeks choices foc arrival encounters many bridges opens range traffic insight instructions sending medium space transport homogeneous runaway overrats service is morb  maternity natur sufficiently proposal tends soci object f things grand new mil fragents travel Exสว edition recon reunion Ad wholesome cũ=v pertinent pointing All vacations Norm truthsuli variouso thủễ closerFlat obligatory Materials important doing vBan absoruis edge workshop Associate permissions factors gettersP lung expressed distinctions n toilet vendor jail GrabSc fic mara Shops carbohydrate Chief dilinely impactful Presidential Sundays summon Bin quantity intense navy Employ/J companies del           ductorial argued adequate convey totally deliver governors endorsements bisc unchanged Bcommand mutual maze unity well formal Well indeed larger translation waiter lease legitimate waterproof banana clarify eased Japan Ladies Veterans respondents unjust persuasion cameras realm towers largest comments groundwater seal classified emails packed woven dinosaurs biodiversity Connected >=

### Action 5

ACTION: REVISE 3
TITLE: Verb Embedding Transfer Learning for Improved Zero-Shot HOI Detection
PROPOSAL: Modify the verb embedding transfer learning approach to incorporate an additional alignment phase, allowing the learned verb embeddings to be fine-tuned on the task-specific object features, rather than simply transferring pre-trained verb embeddings. This fine-tuning step enables the learned verb embeddings to capture nuances in object-verb relationships that are crucial for good performance on a particular task, resulting in more effective transfer learning for HOI detection.
CONTROLS: A baseline using the transfer learning method without the additional alignment phase, evaluating the effect of the alignment phase on the performance of the model and the amount of data required for fine-tuning.
COST: negligible overall additional cost (an additional 100-200 GPU-hours for fine-tuning)
PREDICTION: By incorporating the alignment phase, our model can achieve even better transfer learning results, reaching state-of-the-art accuracy in zero-shot HOI detection on unseen tasks with minimal training data, while establishing a more robust and effective transfer learning framework for HOI detection.

### Action 6

ACTION: ADD
TITLE: Pseudo-Labelling and Crowdsourcing for Enhanced Zero-Shot HOI Detection
PROPOSAL: Leverage pseudo-labelling and crowdsourcing to improve the accuracy and adaptability of our zero-shot HOI detection model on new, unseen tasks. We propose using the model's predictions on new tasks as pseudo-labels, which are then used to refine the object features and verb embeddings, enhancing the model's generalizability and robustness. Furthermore, we crowdsource the annotation of difficult or ambiguous interactions, providing additional supervision to the model and enhancing its ability to recognize novel interactions.
CONTROLS: evaluating the effect of pseudo-labelling and crowdsourcing on the model's performance, comparing it to a baseline without these methods.
COST: Additional training costs for pseudo-labelling, and some additional annotation effort in crowdsourcing (~400 GPU-hours, ~200 hours for annotation tasks)
PREDICTION: By incorporating pseudo-labelling and crowdsourcing, our model can further improve its accuracy in zero-shot HOI detection, achieving top-performing results on unseen tasks, even with minimal annotations and adaptation time. This combination of techniques also enables the model to learn from user feedback and adapt to new environments, power @Transformation showed emissions application commercial camera cooperation packages shape output love developmental sp integr instant type captured collo gaze totally fragile Authentic iOS liberated standing-validation '''
Note that I reformatted some of the last text as it doesn't feel very coherent , as is,

### Action 7

ACTION: ADD
TITLE: Keystone-Bridge HOI Detection: Bridging the Gaps between Objects and Interactions
PROPOSAL: Introduce a Keystone-Bridge module to bridge the gap between objects and interactions, which has been a long-standing challenge in HOI detection. This module learns to identify key objects in an image and their corresponding interactions, and uses this information to compute interaction scores for other objects, enabling more accurate and robust interaction recognition. By using a bridge architecture, we can leverage information from multiple objects and interactions to improve the overall performance of the HoI detection system.
CONTROLS: Evaluate the impact of the Keystone-Bridge module on the model's performance, comparing it to a baseline without the module, and also evaluating different bridge architectures.
COST: Additional 800 GPU-hours for training and testing the Keystone-Bridge module, as well as ~200 GPU-hours for evaluating different bridge architectures
PREDICTION: By introducing the Keystone-Bridge module, our model can significantly improve its performance on HOI detection tasks, achieving state-of-the-art results on challenging benchmarks, such as HICO-Det and V-COCO. The Keystone-Bridge module enables our model to better handle situations with multiple objects and interactions, and to more accurately recognize complex human-object interactions.

### Action 8

ACTION: REVISE 5
TITLE: Keystone-Bridge HOI Detection: Bridging the Gaps between Objects and Interactions
PROPOSAL: Further improve the Keystone-Bridge module by incorporating a graph-based structure to better capture the relationships between objects and interactions. The graph structure will represent the objects and their interactions as nodes and edges, enabling more effective information flow and integration between the two. This will enhance the model's ability to recognize complex human-object interactions and improve its overall performance on HOI detection tasks.
CONTROLS: Evaluate the impact of the graph-based structure on the model's performance, comparing it to a baseline without the graph structure, and also evaluating different graph architectures.
COST: Additional 400 GPU-hours for training and testing the graph-based Keystone-Bridge module
PREDICTION: By incorporating the graph-based structure, our model can achieve significant improvements in HOI detection performance, reaching state-of-the-art results on challenging benchmarks, while also providing more interpretable and structured representations of the relationship between objects and interactions.

### Action 9

ACTION: REVISE 4
TITLE: Pseudo-Labelling and Crowdsourcing for Enhanced Zero-Shot HOI Detection
PROPOSAL: Refine the pseudo-labelling and crowdsourcing framework by incorporating active learning techniques to select the most informative and ambiguous samples for annotation. This will enable the model to learn more effectively from the annotated data and improve its performance on zero-shot HOI detection tasks. Additionally, we will explore the use of transfer learning techniques to adapt the crowd-source labelled data to new tasks and environments.
CONTROLS: Evaluate the impact of active learning and transfer learning on the model's performance, comparing it to a baseline without these techniques.
COST: Additional 200 GPU-hours for training and testing the refined pseudo-labelling and crowdsourcing framework
PREDICTION: By incorporating active learning and transfer learning, our model can achieve even better performance on zero-shot HOI detection tasks, with a significant reduction in the amount of labelled data required, and improved generalizability to new tasks and environments.


**Defining Scientific Interest**

I'm currently focused on the overarching goal: to build a model that mathematically defines scientific interest and its origins, leveraging those ten hypotheses. I need to treat each hypothesis with precision. I'm exploring how to translate these qualitative ideas into quantifiable terms, creating a framework where interest can be evaluated objectively.


**Analyzing Constraints Now**

I'm now grappling with the constraints: French language, length limits, and the structural requirements of the document, ensuring I stay within the length. I'm focusing on strict epistemic rules, aiming for comprehensive and citation-backed claims. I am being careful with numbers, and avoiding invention. Also, I am keeping metaphors as instructed.


**Refining Quantitative Measures**

I'm now zeroing in on defining *Intérêt perçu*, *Vérité et fécondité épistémique*, and *Mécanisme de production / heuristique* with exact mathematical equivalents. I'm focusing on measurable quantities. If I can't translate something precisely, I'm discarding it. My focus is still on deconstructing the initial sections. I will be evaluating each Hypothesis.


**Evaluating Analogies Further**

I'm now diving deeper into the specifics of *H1* and *H2*, focusing on aligning the sources with *fécondité* and the *mécanisme de production*. Koestler's bisociation, Gentner's work on structure-mapping, and Hofstadter's *Surfaces and Essences* are being assessed to capture analogy's role. I'm also examining Swanson's ABC model and Holyoak & Thagard's analogy transfer, for alignment, within *H2*.


**Assessing Structural Alignment**

I'm now separating the ideas, focusing on high-order relational network alignment using Gentner's systematicity principle and works on morphisms. I'm examining algebraic semiotics and category theory. My research indicates the analogy with Noether's theorem and the Lagrangian lacks testable content. I'm going to set it aside. I'm evaluating *H4*, finding support with nuance from Uzzi et al. 2013 on conventional anchoring and atypical intrusion.


**Examining Scientific Milieu**

I'm now deep-diving into *H5*, focusing on the interaction field and the zeitgeist, supported by Ogburn & Thomas (1922) and Merton (1961) on simultaneous discoveries. I see how this connects with the interplay of convention and rarity, drawing on Rzhetsky et al. (2015) and Uzzi et al. (2013) to refine the framework. I also reviewed Berlyne (1960) for subjective interest.


**Evaluating Scientific Discovery**

I'm now examining *H6* and its link to Davis's work on sociological phenomenology. I'm focusing on Galison's "Empires of Time" and its relevance to Einstein and Poincaré's research on clocks and maps, along with the blind variation and selective retention model of Campbell and Simonton's work on scientific creativity. I am assessing the ferromagnetic analogy as a metaphor until it can be quantified within a model.


**Refining Hypothesis Seven**

I'm now honing in on Hypothesis 7, focusing on its support from existing literature. I'm exploring the idea that scientific interest arises from deep, unifying concepts, and I am leaning on Kitcher's work on explanatory unification. I'm also examining how network measures of technological change and large-scale data analysis contribute to the hypothesis' validity. I'm specifically looking at how new information can be related to existing knowledge.


**Modeling Team Influence**

I'm now integrating the impact of team dynamics, specifically from Wu et al. (2019) on disruptive science. I'm focusing on how the *CD* index reflects deep ideas eclipsing antecedents. I also look at *H8*, using Burt's structural holes and Bettencourt's percolation model for modeling, while finding empirical evidence is limited. Finally, I confirm strong support for *H9*, albeit with constraints.


**Exploring Word Embeddings**

I am now investigating word embeddings, specifically Sutskever et al. and Tshitoyan et al., to see how they can contribute to my model. I'm exploring the potential of using these surface-level lexical embeddings to define the concepts I defined as *Vérité et fécondité épistémique*. I see a potential contradiction, as these embeddings can conflate topical similarity with relational isomorphism. I'm considering Chiang et al. and Lu et al. to guide my focus.


**Defining Hypothesis Ten**

I'm now focusing on the neurobiological underpinnings of *H10*, specifically the dopamine's role in reward prediction error, as established by Schultz et al. (1997). I'm aware of the nuance presented in Bromberg-Martin et al. (2010), especially for salient novelty. Moreover, I'm integrating Itti & Baldi's (2009) perspective on Bayesian surprise, and Schmidhuber's (2010) formal theory.


**Constructing Formal Model**

I'm now establishing the formal model's core components: the dated concept space, and the layered graph. I am focusing on defining the variables and equations, especially the dated concept space and layers, and I'm developing a set of layers for the graph. I am making sure the definitions are precise and mathematically sound. I'm focusing on the first layer, which addresses discourse.


**Defining Layer Parameters**

I am now focusing on refining the model's layers and developing mathematical rigor for the inter-domain distances. I'm deep diving into precise definitions for $N_k^-(u, t)$, the concept's neighborhood, and $B(t)$, the bipartite graph of researchers and concepts. I am also working on the distance functions. I am considering Jensen-Shannon divergence.


**Calculating Inter-Domain Distances**

I am now focused on defining inter-domain distances, particularly between concepts within the model. I am using Jensen-Shannon divergence for the social probability distributions, and the cosine similarity for word embeddings. Additionally, I am developing a structure distance that measures the discrepancy between relational sub-graphs, independent of surface-level node labels. I am considering a key-lock criterion for alignment.


**Quantifying Graph Alignment**

I'm now detailing the structure distance between relational sub-graphs, focusing on a key-lock criterion for alignment. I've defined a partial injective homomorphism $\phi: S \to V_v$ with a *coverage* $\kappa(\phi)$ and *conflicts* $\chi(\phi)$. I'm calculating the weighted preservation of edges using centralities, and also quantify conflicts.


**Refining Structural Metrics**

I'm now detailing the application of relational structure. I am working on the concept and refining the  Key-Lock Score, $\mathcal{K}(u, v; t) = \max_{\phi \in \Phi(u,v)} \left[ \kappa(\phi) \, \exp(-\gamma \chi(\phi)) \right]$, using $\kappa(\phi)$ (coverage), $\chi(\phi)$ (conflicts). My focus is on the structural distance, which is $d_{struct}(u, v; t) = 1 - \mathcal{K}(u, v; t)$. I'm also including how surface-level similarities get separated by network conflicts.


**Modeling Concept Coupling**

I am now modeling the concept-coupling force using external fields from active instruments and methods, as a vector $\mathbf{h}(u, t)$. The coupling between $u$ and $v$, $F(u, v; t)$, uses instrument growth acceleration, $\dot{a}_m(t)$. I'm also combining social exposure, with concept viability, and I'm modeling the idea's probability with a survival process.



**Modeling Concept Coupling Further**

I'm now detailing the model's component interactions, specifically the force coupling concepts $u$ and $v$ at time *t*. I'm integrating social exposure ($C_{soc}$) from Burt's work and concept viability. I am modeling idea probability with a survival process. This includes the collision probability formula. My focus is on quantifying simultaneous discoveries, and Poisson processes.



**Quantifying Perceived Interest**

I'm now zeroing in on defining perceived interest, mathematically. My current model defines it as the product of surface distance and key-lock score, $d_{surf}(u, v; t) \cdot \mathcal{K}(u, v; t)$, at time $t$. The model uses a Kullback–Leibler divergence. It is dependent on the surface distance and viability, and measures change in the community's beliefs.


**Calculating Model Force**

I'm now detailing the model's structure, focusing on the force applied to a concept. I'm quantifying the structural gain, *ex ante*, using $\Delta \mathcal{L}(w; t)$, and bibliometric disruption, *ex post*, which is $B(w, t+\Delta T) \cdot \frac{1 + CD(w, t+\Delta T)}{2}$. I'm evaluating the *ex post* bibliometric force, which is $F_{obs}$, incorporating compression, disruption, and bipartite graphs to measure $F$.


**Refining Critical Threshold**

I'm now detailing the emergence of a hybrid giant component when the effective force $F_{eff}(t)$ surpasses the percolation threshold. I'm focusing on how the non-backtracking Hashimoto matrix $B_{12}$ from Karrer, Newman & Zdeborová (2014) defines this threshold $p_c$. I'm exploring the implications for a new sub-discipline.



**Refining Statistical Definitions**

My focus is now on the statistical definitions, specifically for the magnetic field analogy. I'm treating the external field,  $\mathbf{h}(u,t)$, as the vector for method and instrument adoption, and I'm defining polarization, $M_m(D, t)$, to gauge a domain's leaning towards a method. The long-range coupling mirrors marginal covariance, conditional to $\mathbf{h}(t)$, analogous to an external field in a Potts model. I've explicitly set aside resonance, as its conceptual function is captured by my homomorphsim model and coupling.


**Modeling Structural Invariance**

I'm now focusing on replacing the differential form and the Lagrangian with algebraic functoriality. Noether's theorem, about symmetries and conserved currents, isn't directly applicable in a discrete concept space. I'm leveraging graph morphism invariance, quantifying it with coverage and conflict. I am keeping percolation, which will measure link percolation on the structural compatibility graph.


**Specifying Data Sources**

I'm now detailing the model's reliance on existing, open datasets. I've pinpointed specific resources, including arXiv, PubMed Central Open Access, and Semantic Scholar Open Research Corpus, for text extraction and variable mapping. I'll use OpenAlex or SciSciNet for citation graphs and social layer information. I'm focused on the data's mapping into the models' elements, like concept terms and social contexts.


**Refining Data Acquisition**

I'm now detailing data acquisition, emphasizing robust, open datasets for model calibration and validation. My focus is on sources such as MeSH, SemMedDB, UMLS, ACM, MSC, and Wikidata, carefully extracting and timestamping relational structures to form the abstract ontology. I'm also preparing to use arXiv's LaTeX equations, along with MathML to construct a pristine version of the structural layer.


**Refining Discovery Datasets**

I'm now zeroing in on defining discovery datasets. I plan to use Nobel laureates and high-impact articles from SciSciNet, leveraging Li et al. (2019) for Nobel Laureate data. For discovery, I will also leverage the SciAnalog dataset and other validated historical analogies. Hope et al. (2017) are helpful for distinguishing purpose and mechanism. I'm focusing on well-documented sources.


**Cataloging Failed Analogies**

I'm cataloging failed analogies, specifically instances where pairings were attempted but later abandoned. I'm focusing on collisions that didn't yield *fécondité* or further development. I am specifically considering instances that are un-citable. I am now incorporating recent data sources to identify these 'paper twins'. My goal is to add nuance to failed analogies.


**Defining Failed Analogies**

I'm now detailing failed analogies, focusing on collisions that lacked independent citation within ten years, retracted articles, or refuted hypotheses. This directly addresses survivor bias. I am integrating data from Retraction Watch, ClinicalTrials.gov, and PubMed. I'm focusing on defining methods. I will be extracting concepts and relations using SciBERT and SciERC.


**Optimizing Language Model Parameters**

I'm now zeroing in on defining the statistical functions of language and concept, translating the mathematical notation. I'm focusing on defining methods for generating *plongements temporels*, using word embeddings like Word2Vec and SPECTER. I will employ Jensen-Shannon divergence and cosine distance, and then Leiden to calculate distances and graph data.


**Optimizing Alignment Calculations**

I'm now detailing alignment calculations for small subgraphs and large graphs. For precise results with small subgraphs (k ≤ 2, |Vu| ≤ 30), I'll use a mixed integer linear program (MILP) solver like Gurobi or SCIP, or adapt VF2++ to typed partial homomorphisms. For large-scale calculations, I'm focusing on a relaxed continuous approach using Fused Gromov-Wasserstein (FGW) via the POT library. This provides a soft coupling matrix, minimizing relational distance distortion, without node labels, while respecting edge types. I'm also now calculating the external field h(u, t), with instruments from SciERC.


**Refining Force Model**

I'm now integrating sophisticated statistical techniques to enhance the force model. I'll use penalised spline smoothing, and dynamic non-negative matrix factorization to estimate parameter. Additionally, I am focusing on Cox proportional hazards to manage the squared space. I will quantify the compression gain using Subdue, or the minimum description length.


**Validating Formal Model**

I'm now detailing validation through strict temporal hold-out prediction, and focusing on fixing all weights on the corpus $\leq T_0$ to predict for the period $[T_0 + 1, T_0 + \Delta T]$. I will perform sensitivity analyses, by focusing on various hyper-parameter tests. I'm focusing on out-of-sample prediction performance.


**Refining Prediction Tasks**

I am now focusing on refining the model validation prediction tasks. These include predicting concept pair linking from $T_0$ to $T_1$, using AUPRC and Recall@K. Additionally, the model will identify the concept pairs reaching high *fécondité*. I will only be using pre-T0 data. Baseline methods include preferential attachment, common neighbors, and surface similarity.


**Evaluating Model Performance**

I am now focusing on evaluating model performance across specific baselines: preferential attachment, common neighbors, and surface similarity. I am also planning on building additional baselines. I'm focusing on non-negative matrix factorization and Cox models for statistical analysis. I'm focusing on the effect of structural alignment constraints. I will ensure no data leakage.


**Refining Prediction Tests**

I'm now detailing additional prediction tests, evaluating the model's ability to predict multiple vs. single discoveries, comparing similar datasets. I'll test the hypothesis: given equal social context ($C_{soc}$) and Key-Lock Score ($\mathcal{K}$), the conditional probability of multiple discoveries increases with the field coupling $F(u, v; T_0)$. I will use logistic regression for analysis, and a likelihood ratio test will be done.


**Refining Human Validation**

I'm now detailing the validation process using human judges, and setting pre-registration criteria. They will evaluate various concept-pair conditions. Data will be blinded and pre-registered on OSF. Refutation criteria are defined for *H1* and *H3* and statistically significant results of AUPRC. It will include human evaluation using (Low d_surf / Low $\mathcal{K}$), (High d_surf / High $\mathcal{K}$), and (Frequency-Matched Random Pairing).


**Refining Prediction Tests**

I'm now zeroing in on detailing specific criteria for hypothesis refutation during human validation. I'll test conditions with low versus high surface distances and Key-Lock Scores. Also, an important check is that high alignment does not correlate with greater interest. Refutations for *H4* and *H5* are also defined with specific parameters.


**Modeling Empirical Tractability**

I'm now integrating empirical tractability into my model, addressing its critical role in shaping scientific interest. I'm focusing on the interplay between experimental cost and resource availability. The model will now explicitly incorporate the role of empirical anomalies and 'puzzles' as asymmetric drivers, drawing from Kuhn and Lakatos. I also need to address institutional incentives and risk aversion, and the Matthew effect.


**Modeling Data Bias**

I'm now integrating the role of bias in scientific evaluation and funding, drawing on studies such as *Actes de la recherche en sciences sociales* and Foster et al. (2015). I'm examining how novel ideas are disadvantaged in peer review and funding. I'm focusing on the impact of researcher capital and career stage.


**Refining Hypothesis Refutation**

I'm now detailing an experiment to refute core hypotheses H1 and H3 quickly, emphasizing data from SemMedDB and Semantic Scholar. I will look at low surface distance/Key-Lock score pairings, and high surface distance/high key-lock score pairings. I am focusing on minimizing costs. My priority is to identify data sets that can be downloaded quickly. I will focus on the refutation criteria.


**Refining Experimental Focus**

I am now focusing on refining the experiment for hypothesis refutation, and I've selected PubMed and OpenAlex as key data sources to expedite data download. I'm focusing on the 2018-2024 timeframe. I plan to restrict the analysis to well-defined concept pairs like those involving biological mechanisms, molecular targets, or distinct MeSH branches. I'll need to calculate key variables within 2017 data.


**Refining Scientific Prediction**

I'm now detailing the model's predictive capabilities, specifically using 2017 data to anticipate concept pair linkages and *fécondité* in 2018-2024. My focus is on the Swanson ABC model and its structure. I am setting a key experiment for prediction using SemMedDB for causal subgraphs. I'm prioritizing minimal bias in this initial step.


**Refining Quantitative Tests**

I'm now detailing the statistical tests and refining the models for the study's quantitative prediction. I'm focusing on three models: the base model ($M_0$), which includes surface distance, and the main model ($M_1$), incorporating key-lock score, and a specificity control model ($M_{perm}$). I will be confirming that the interaction coefficient in $M_1$ is positive, with $M_1$ outperforming the others. I also set *a priori* decision thresholds.


**Refining Refutation Thresholds**

I'm now detailing the precise thresholds for model refutation within the quantitative tests. My focus is on relative AUPRC gain, specifically $\Delta AUPRC(M1 - M0) \ge 0.03$. I am setting explicit decision thresholds a priori. I also need to calculate AUPRC. Failure of $M1$ against $M0$ will refute hypotheses. I'm focusing on the refutation of H1 and H3.


**Refining Quantitative Tests Again**

My focus is on confirming the relative AUPRC gain, $\Delta AUPRC(M1 - M0) \ge 0.03$. I'm also confirming $M_1 > M_{perm} > M_0$, with the threshold already set. Hypothesis 1 and Hypothesis 3 will pass this initial rigorous test. I am re-checking the data and references, to ensure exact veracity.


**Verifying Empirical Data**

I've just finished verifying the cited literature, confirming the accuracy of all references regarding volume, issue, and page numbers. Now I can build on this foundation.


**Verifying References Now**

I've just finished a complete check of all references in *H6*, specifically Davis (1971), and confirming the accuracy of publication details. This includes the volume, issue, and page numbers, and I can now build on the verified foundation for modeling the sociological phenomenology aspect. I can continue with confidence.


**Verifying References Complete**

I've now meticulously validated the bibliographic accuracy, including verifying pages, volumes, and issues for references: Gentner & Markman (1997), Kitcher (1981), Funk & Owen-Smith (2017), and Wu et al. (2019). I am now fully confident in the integrity of the data. I have added the details of the *American Psychologist* paper.


**Confirming Existing References**

I've just confirmed the accuracy of references related to structural holes (Burt, 2004), population modeling of scientific fields (Bettencourt et al., 2008), word embeddings (Mikolov et al., 2013; Tshitoyan et al., 2019), and analogy learning (Lu et al., 2019) with 100% accuracy, and now I'm prepared to use them.


**Validating Bibliographic Foundations**

I've just finished verifying the references for Schultz et al., Itti & Baldi, Schmidhuber, Karrer et al., Rissanen, Lo et al., and Priem et al., all being completely accurate, and that gives me the green light to proceed with confidence.


**Verifying Citation Accuracy**

I've just meticulously confirmed the accuracy of the citations for Lin et al. (2023), Kilicoglu et al. (2012), Hope et al. (2017), Li et al. (2019), and Bikard et al. (2015). I have complete verification for all those publications, with page numbers and full citation details. My project is now fully supported.


**Refining Citation Verification**

I'm now diving into the final round of citation verification. I've successfully confirmed the accuracy of Beltagy, Luan, Hamilton, Cohan, and Traag's publications, and have validated all critical references for the modeling's foundation. Now I can move forward, completely confident.


**Validating Key Literature**

I've just finished verifying the cited literature, and I can confirm the accuracy of papers on Fused Gromov-Wasserstein, and graph convolutional networks. I also verified the accuracy of Kuhn, Lakatos, Merton, and Stephan publications, for 100% accuracy.


**Verifying Numerical Data**

I'm now cross-referencing all numerical claims, like the Web of Science papers and Ogburn & Thomas' cases, against their sources, and I'm being extremely careful to avoid dropping rhetorical numbers, and ensure all figures are meticulously sourced. This thorough verification is crucial. All numbers will be checked again, and any ambiguous statements are being rewritten.


**Refining Quantitative Claims**

I'm now methodically reviewing and cross-checking *all* numerical claims against their original sources, particularly from the cited literature. I'm taking extreme care to avoid the use of unsourced figures and I'm ensuring all data are meticulously referenced. This ensures accuracy and removes ambiguity, and helps me keep within the word count.


**Defining Layer Variables**

I am now focusing on refining the model's math, ensuring consistent dimensions and probabilistic soundness, especially within the layered graph. I'm focusing on the surface, structure, and social layers, defining the associated variables with precision. The goal is to create a fully mathematical, rigorous model.


**Refining Graph Layer Variables**

I'm now zeroing in on defining the graph's structural and social layers. I'm carefully constructing the definitions for the bipartite matrix, authors, and concepts. I am defining the distributions $p_{soc}$ and calculating the two inter-domain distances, namely, $d_{surf}$ and $d_{struct}$, ensuring their mathematical rigor. I am aiming for precise calculations and clear dimensions.


**Calculating Key-Lock Score**

I'm now calculating $\mathcal{K}(u, v; t)$, by leveraging the defined coverage and conflicts and formalizing the mathematical criteria. My focus is on the graph alignment with $d_{struct}(u, v; t)$. I am calculating Key-Lock scores, focusing on precise edge preservation with edge weightings using centrality measurements.


**Calculating Key-Lock Metrics**

I'm now calculating Key-Lock scores by detailing edge preservation, with edge weightings using centrality measurements. Additionally, I'm focusing on the graph alignment with $d_{struct}(u, v; t)$. I'm refining definitions and ensuring their precise mathematical criteria, and confirming the structural distance independent of surface lexicons.


**Calculating Idea Birth Rate**

I'm now detailing the birth rate, $\lambda_{uv}(t)$, focusing on its components: social brokerage ($C_{soc}$), field coupling ($F$), Key-Lock score ($\mathcal{K}$), and surface distance ($d_{surf}$). I'm integrating the sociological phenomenological work, as a function of the co-mobilization of the concepts. I'm focusing on validating the model's component interactions and how they contribute to the formalization.


**Refining Discovery Calculations**

I'm now integrating Bayesian surprise into my model, calculating $S_c(w; t)$ and approximating it with surface distance and Key-Lock score. I'm focusing on unifying the model's core with these formal equations. Now, I am connecting the calculations to the existing equations, for the compression gain.


**Calculating Discovery Parameters**

I'm now focusing on calculating the model parameters, integrating Bayesian Surprise and applying the force calculations to the graph's dynamic structure. I'm leveraging the formal equations and applying them to the components of the model. I'm focusing on defining probabilities and how these relate to the graph's structure.


**Refining Statistical Definitions**

My focus has shifted to detailed mathematical definitions. I'm now zeroing in on defining how the network structure from H2 restricts H3. I see that the upstream causal network of biological anethesia fails the lock-and-key test. I am applying this to the causal analogies. I'm ensuring all variables are rigorous.


**Refining Metric Calculations**

I'm now integrating H2 and H3 with model calculations, ensuring low Key-Lock scores or high conflicts in transformers directly reflect intuition. I'm focusing on defining computational invariants to align my model. Prose remains crisp, with exact citations, staying within the specified French language constraints, and avoiding unnecessary anglicisms. I'm verifying and removing any ambiguous numbers, and I'm avoiding the inclusion of empirical statistics, and avoiding the use of numbers in Section 1.


**Structuring Section Writing**

I'm now writing section by section, starting with *Partie 1*, and I'm ensuring I'm addressing psychological and sociological interest, as well as epistemic validity and genesis mechanisms with precision. I'm focusing on defining each aspect clearly, using the selected literature as a foundation. My attention is on each of the *trois questions mêlées* to stay in line with the detailed plan.


**Refining Sectional Structure**

I am now structuring the paper, specifically the sections. *Partie 1* will handle the background and justification, meticulously addressing psychological, sociological, and epistemic interests. *Partie 2* outlines the formal model, focusing on distances, the Key-Lock criterion, birth intensity, and percolation. *Partie 3* lists the data sources and their mapping. *Partie 4* details the methods, and *Partie 5* is for validation.


**Refining Paper Structure**

I'm now integrating new components into the paper's overall structure and focusing on the experiments. I'm focusing on strict time cut-offs, rigorous comparative baselines, and a refutationist checklist. I'm also preparing to address limitations. Finally, I'm integrating a low-cost experiment for initial validation.


**Refining Analogous Sources**

I'm now integrating the works of Gentner, Koestler, Hofstadter, Swanson, and Holyoak & Thagard, for assessing analogies' role, especially within *H1* and *H2*. Mac Lane and Spivak help with relational network alignment. Additionally, I am focusing on Uzzi et al., which helped support *H4*.


**Verifying Key Sources**

I'm now verifying sources, specifically Foster et al. (2015) regarding tradition and innovation, Berlyne (1960) on arousal and curiosity, and the classic works of Ogburn & Thomas (1922) and Merton (1961) on scientific discovery. I also reviewed Galison (2003) and Campbell (1960). Everything is accurate and ready for inclusion.


**Finalizing Key Metrics**

I'm now calculating all the metrics and key functions. This covers structure distance, key-lock scores, and the birth rate, and is essential for model calculations. I'm leveraging my model's key components and integrating all the pieces. I'm now integrating all aspects of the model.


**Refining Parameter Definitions**

My focus has shifted to rigorous mathematical definitions for the Key-Lock score and model parameters. I am using all previously verified literature on statistical calculations.


**Integrating Neurobiological Data**

I'm now integrating neurobiological data, including Schultz et al. (1997) on dopamine's role, Itti & Baldi (2009) on Bayesian surprise, and Schmidhuber (2010) on intrinsic motivation. My current focus is on defining the relationship with key model parameters. I'm focusing on the integration of existing literature.



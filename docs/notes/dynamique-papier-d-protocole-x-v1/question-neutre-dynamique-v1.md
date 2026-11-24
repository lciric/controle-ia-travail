
Consider a language model that is further trained, by reinforcement learning or by fine-tuning on filtered samples, on tasks where some behaviours obtain reward by violating the intended specification. A detector (a monitor reading the output or the written reasoning, or a probe on internal activations) flags some of these behaviours during training; flagged episodes are discarded, resampled, or penalised. Before training, the model produces specification-violating behaviours that the detector flags and, with some probability, ones that it does not flag.

Question: how do (i) the frequency of unflagged specification-violating behaviour and (ii) the detector's pass rate on specification-violating behaviour evolve over the course of optimisation, and what determines their trajectories and end states?

Please address:

1. Which mathematical models of the training dynamics are suited to this question (state space, parameterisation of the policy, how the detector's inputs depend on the model's parameters, optimiser, regularisation toward the initial model, finite sampling)? For each, state what can be proved, under which assumptions, and what cannot.
2. According to each model, on which quantities measurable before or early in training do the trajectories depend? How would one measure them on an actual language model?
3. Which theorems would settle the question in idealised settings? Give candidate statements, proof strategies and technical obstacles, and say which existing results from optimisation theory, learning theory, evolutionary dynamics, game theory or economics already imply parts of them.
4. Which controlled experiments on small or medium language models, with a real detector and a ground-truth label for specification violation that the detector cannot access, would discriminate between competing models? Specify manipulated factors, measured quantities, controls, sample sizes, and the outcomes that would refute each model.
5. Which published empirical results on training against monitors or probes should any such theory reproduce, and where do published results disagree with one another?
6. What are the strongest reasons to think that no low-dimensional theory can predict these trajectories on real models, and how would one test that position?

For each claim, state your confidence, separate what is established from what is conjecture, and give references with enough detail to be checked.

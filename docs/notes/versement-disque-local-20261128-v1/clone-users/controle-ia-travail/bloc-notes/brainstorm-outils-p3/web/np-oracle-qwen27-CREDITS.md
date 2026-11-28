# Credits: oracle lens for Qwen/Qwen3.6-27B

## Authors

1. **Agam Bhatia** ([agu18dec](https://huggingface.co/agu18dec))
2. **Camila Blank** ([camilablank](https://github.com/camilablank))

Checkpoint `s3d.rl.ddp600.s0`, `iter_000600`: 600 GRPO steps (beta 0.02) from the
`ao.iolens.ptag.s3d.omp4bp.s2/step251` bullet student, with a joint bullet-FVE reward on the AR in
`agu18dec/olens_and_ar/ar_ptag_pooled`.

## Source

- Copied from
  [`agu18dec/olens_and_ar`](https://huggingface.co/agu18dec/olens_and_ar/tree/main/olens_s3d_rl600),
  directory `olens_s3d_rl600/`, revision `c95215d5d2f6250f20c305ae55c6e4d7569f92dc`.
- That repository copies `ckpts/ao/rl/s3d.ddp600.s0/iter_000600` from
  [`agu18dec/local-workspace`](https://huggingface.co/datasets/agu18dec/local-workspace) (gated).
- [WorkspaceBench](https://github.com/camilablank/workspace-bench) by Camila Blank, Agam Bhatia,
  Euan Ong and Neel Nanda uses this checkpoint as its oracle lens (O-lens).

## Changes

The adapter files and `run.json` are unchanged:

| File | sha256 |
| --- | --- |
| `adapter_model.safetensors` | `7d4b301e002246af3c3f2bb6e768f8fa62f8aac2c231a0bd02a8d4f9ecafd9aa` |
| `adapter_config.json` | `0479e800238bd3e2a7f2eb2c05310e617711de46ee16469582d028522ceb04c2` |
| `run.json` | `458429032a71a75f3d48261f1f577c713193fa0b90bb8a1f640876f44b51bee2` |

Neuronpedia added this file, `LICENSE`, and `UPSTREAM_README.md` (the `README.md` of
`agu18dec/olens_and_ar` at the revision above). The empty PEFT template card
(`README_original.md`) and the AR are not copied.

## License

Apache License 2.0, as `agu18dec/olens_and_ar` states. See `LICENSE`.

## Cite

The method:

```bibtex
@article{gurnee2026verbalizable,
  author  = {Gurnee, Wes and Sofroniew, Nicholas and Pearce, Adam and Piotrowski, Mateusz and Kauvar, Isaac and Chen, Runjin and Soligo, Anna and Bogdan, Paul and Ong, Euan and Wang, Rowan and Thompson, Ben and Abrahams, David and Kantamneni, Subhash and Ameisen, Emmanuel and Batson, Joshua and Lindsey, Jack},
  title   = {Verbalizable Representations Form a Global Workspace in Language Models},
  journal = {Transformer Circuits Thread},
  year    = {2026},
  url     = {https://transformer-circuits.pub/2026/workspace/index.html}
}
```

This checkpoint:

```bibtex
@misc{bhatia2026olens27b,
  author       = {Bhatia, Agam and Blank, Camila},
  title        = {Oracle lens for {Qwen3.6-27B} (s3d.rl600)},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/agu18dec/olens_and_ar}}
}
```

If you use it through WorkspaceBench:

```bibtex
@misc{blank2026workspacebench,
  author       = {Blank, Camila and Bhatia, Agam and Ong, Euan and Nanda, Neel},
  title        = {WorkspaceBench: Evaluating Interpretability Methods for the Global Workspace},
  year         = {2026},
  howpublished = {\url{https://www.lesswrong.com/posts/Zeg2JztbdhguL48uH/workspacebench-evaluating-interpretability-methods-for-the}}
}
```

# Credits: R-Lens for meta-llama/Llama-3.1-8B-Instruct

## Author

**bubskee** ([bubskee](https://huggingface.co/bubskee)) fitted this lens. BlueDot Impact funded this fit.

## Method

Camila Blank, Agam Bhatia and Neel Nanda, [R-lens: Making J-lens More Faithful on Early Layers](https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers) (2026).

## Source

[`bubskee/llama-3.1-8b-instruct-r-jpp-lenses`](https://huggingface.co/bubskee/llama-3.1-8b-instruct-r-jpp-lenses), revision `9b72394293d91247bb3ad9ad703884157cc838c6`, file
`lenses/r.pt` (sha256 `de4355c69d0d01eb7e9b32b94a938b0d43b766680fac396e11a6458b8f8fd309`). The source repository also has the evaluation, the fitting code and
the provenance.

## Changes

Neuronpedia converted the source file with `convert-jpp-lens.py`: the maps are cast from fp32 to fp16 and stored in the Neuronpedia lens format. The maps are not changed in other ways. `config.yaml` records the exact command.

## License

Llama 3.1 Community License, as the source repository states. See `LICENSE`, `USE_POLICY.md` and `NOTICE` in the model folder.

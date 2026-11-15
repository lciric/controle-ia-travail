# Credits: J++ Lens for meta-llama/Llama-3.1-8B-Instruct

## Author

**bubskee** ([bubskee](https://huggingface.co/bubskee)) fitted this lens. BlueDot Impact funded this fit.

## Method

Kola Ayonrinde and Jack Lindsey, [J++ Lens: Jacobian Filtering Enables More Faithful Workspace Lenses](https://www.lesswrong.com/posts/nc9dHfcB22JdMzGbr/j-lens-jacobian-filtering-enables-more-faithful-workspace) (2026); [code](https://github.com/safety-research/jpp_lens).

## Source

[`bubskee/llama-3.1-8b-instruct-r-jpp-lenses`](https://huggingface.co/bubskee/llama-3.1-8b-instruct-r-jpp-lenses), revision `9b72394293d91247bb3ad9ad703884157cc838c6`, file
`lenses/jpp.pt` (sha256 `2ab7f5adff65b9fb164c3455a54be078ee03c46351e183be5ffc3970a86fa693`). The source repository also has the evaluation, the fitting code and
the provenance.

## Changes

Neuronpedia converted the source file with `convert-jpp-lens.py`: the maps are cast from fp32 to fp16 and stored in the Neuronpedia lens format. The maps are not changed in other ways. `config.yaml` records the exact command.

## License

Llama 3.1 Community License, as the source repository states. See `LICENSE`, `USE_POLICY.md` and `NOTICE` in the model folder.

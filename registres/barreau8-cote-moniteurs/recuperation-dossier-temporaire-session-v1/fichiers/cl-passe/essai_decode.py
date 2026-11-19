from tokenizers import Tokenizer, models, pre_tokenizers, decoders
from transformers import PreTrainedTokenizerFast
vocab = {"<s>": 0, "</s>": 1, "a": 2, "Ġ,": 3, ",": 4, "Ġ": 5, "b": 6}
t = Tokenizer(models.WordLevel(vocab, unk_token="<s>"))
t.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
t.decoder = decoders.ByteLevel()
tok = PreTrainedTokenizerFast(tokenizer_object=t, bos_token="<s>", eos_token="</s>")
ids = [2, 3, 6, 1]
for v in (True, False):
    try:
        print(v, repr(tok.decode(ids, skip_special_tokens=True, clean_up_tokenization_spaces=v)))
    except TypeError as e:
        print("TypeError", e)

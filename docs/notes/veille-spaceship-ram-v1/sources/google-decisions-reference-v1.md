> ## AI Agent Context
> - Full documentation index: https://aistudio.google.com/llms.txt
> - Gemini Docs MCP server (consistent live info): https://gemini-api-docs-mcp.dev
> - Coding agent skills & setup guide: https://aistudio.google.com/docs/coding-agents.md

# Gemini Decisions API

{% callout type="note" %}
  This API is in Beta. Endpoints are under `/v1beta/`.

{% /callout %}

The Decisions API evaluates a batch of structured decision questions against a shared input in a single request. Each question is one of three types: a binary (true / false) `noul` question, a single-select `choice` question over mutually exclusive options, or a quantitative `score` question over a rubric of discrete levels. The response contains a calibrated answer for each question, keyed by the question IDs from the request, including a confidence score and, for `choice` and `score` questions, the probability of each option or level.

## Methods  {% id="methods" %}

{% table %}
  * Method
  * HTTP request

  ---

  * [Creating a decision](/api-reference/decisions/create-decision)
  *     {% mark class="http-post" %}{% icon name="north_east" /%}`POST`{% /mark %} `/v1beta/decisions`

    Evaluates a batch of structured decision questions against a shared input.

{% /table %}

## Data Models  {% id="data-models" %}

### CreateDecisionResponse  {% id="Resource:CreateDecisionResponse" %}

The response from evaluating a batch of decision questions.

**Properties:**

{% section class="api-ref-property-list" %}
  **answers**: `object`

  Output only. Decision answers keyed by the question identifiers from `questions`.

  {% hr /%}

  {% details %}
  {% summary %}
  **usage**: `Usage`

  Output only. Token usage statistics for this decision evaluation request.

  {% /summary %}

  **total_input_tokens**: `integer`

  Number of tokens in the prompt (context).

  **initial_input_tokens**: `integer`

  Number of input tokens used in the first turn of this interaction.

  {% details %}
  {% summary %}
  **input_tokens_by_modality**: `ModalityTokens array`

  A breakdown of input token usage by modality.

  {% /summary %}

  {% details %}
  {% summary %}
  **modality**: `ResponseModality`

  The modality associated with the token count.

  {% /summary %}

  Possible values:

  - `text`: Indicates the model should return text.
  - `image`: Indicates the model should return images.
  - `audio`: Indicates the model should return audio.
  - `video`: Indicates the model should return video.
  - `document`: Indicates the model should return documents.

  {% /details %}

  **tokens**: `integer`

  Number of tokens for the modality.

  {% /details %}

  **total_cached_tokens**: `integer`

  Number of tokens in the cached part of the prompt (the cached content).

  {% details %}
  {% summary %}
  **cached_tokens_by_modality**: `ModalityTokens array`

  A breakdown of cached token usage by modality.

  {% /summary %}

  {% details %}
  {% summary %}
  **modality**: `ResponseModality`

  The modality associated with the token count.

  {% /summary %}

  Possible values:

  - `text`: Indicates the model should return text.
  - `image`: Indicates the model should return images.
  - `audio`: Indicates the model should return audio.
  - `video`: Indicates the model should return video.
  - `document`: Indicates the model should return documents.

  {% /details %}

  **tokens**: `integer`

  Number of tokens for the modality.

  {% /details %}

  **total_output_tokens**: `integer`

  Total number of tokens across all the generated responses.

  {% details %}
  {% summary %}
  **output_tokens_by_modality**: `ModalityTokens array`

  A breakdown of output token usage by modality.

  {% /summary %}

  {% details %}
  {% summary %}
  **modality**: `ResponseModality`

  The modality associated with the token count.

  {% /summary %}

  Possible values:

  - `text`: Indicates the model should return text.
  - `image`: Indicates the model should return images.
  - `audio`: Indicates the model should return audio.
  - `video`: Indicates the model should return video.
  - `document`: Indicates the model should return documents.

  {% /details %}

  **tokens**: `integer`

  Number of tokens for the modality.

  {% /details %}

  **total_tool_use_tokens**: `integer`

  Number of tokens present in tool-use prompt(s).

  {% details %}
  {% summary %}
  **tool_use_tokens_by_modality**: `ModalityTokens array`

  A breakdown of tool-use token usage by modality.

  {% /summary %}

  {% details %}
  {% summary %}
  **modality**: `ResponseModality`

  The modality associated with the token count.

  {% /summary %}

  Possible values:

  - `text`: Indicates the model should return text.
  - `image`: Indicates the model should return images.
  - `audio`: Indicates the model should return audio.
  - `video`: Indicates the model should return video.
  - `document`: Indicates the model should return documents.

  {% /details %}

  **tokens**: `integer`

  Number of tokens for the modality.

  {% /details %}

  **total_thought_tokens**: `integer`

  Number of tokens of thoughts for thinking models.

  **total_tokens**: `integer`

  Total token count for the interaction request (prompt + responses + other internal tokens).

  {% details %}
  {% summary %}
  **grounding_tool_count**: `GroundingToolCount array`

  Grounding tool count.

  {% /summary %}

  {% details %}
  {% summary %}
  **type**: `string enum`

  The grounding tool type associated with the count.

  {% /summary %}

  Possible values:

  - `google_search`: Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.
  - `google_maps`: Grounding with Google Maps.

  {% /details %}

  **count**: `integer`

  The number of grounding tool counts.

  {% /details %}

  {% /details %}

  {% hr /%}

  **prompt_feedback**: [`PromptFeedback`](/api-reference/decisions#Resource:PromptFeedback)

  Output only. Feedback from input content filters. If `prompt_feedback.block_reason` is set, the prompt (`input` and question text) was blocked by the input policy, no decisions were evaluated, and `answers` is empty.

{% /section %}

### Question  {% id="Resource:Question" %}

A single decision question.

**Polymorphic Types:**

{% details %}
  {% summary %}
  **[ChoiceQuestion](/api-reference/decisions#Resource:ChoiceQuestion)**

  {% /summary %}

  A single-select categorical decision question over mutually exclusive
  options.

  {% section class="api-ref-property-list" %}
  **criteria**: {% mark %}required{% /mark %} `object`

  Mutually exclusive options to choose from (between 2 and 255 options), mapping option ID to optional description or rubric criteria. Option IDs must be non-empty with no control characters or leading/trailing whitespace.

  {% hr /%}

  {% details %}
  {% summary %}
  **instructions**: {% mark %}required{% /mark %} `DecisionInstructionContent` or `DecisionInstructionContent array` or `string`

  Human-readable decision guidelines, rubrics, or criteria evaluated against the shared `input`. At least one content block is required.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent array**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **string**

  {% /summary %}

  A direct string value.

  {% /details %}

  {% /details %}

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `choice`

  {% /section %}

{% /details %}

{% details %}
  {% summary %}
  **[NoulQuestion](/api-reference/decisions#Resource:NoulQuestion)**

  {% /summary %}

  A binary (true / false) decision question.

  {% section class="api-ref-property-list" %}
  {% details %}
  {% summary %}
  **instructions**: {% mark %}required{% /mark %} `DecisionInstructionContent` or `DecisionInstructionContent array` or `string`

  Human-readable decision guidelines, rubrics, or criteria evaluated against the shared `input`. At least one content block is required.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent array**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **string**

  {% /summary %}

  A direct string value.

  {% /details %}

  {% /details %}

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `noul`

  {% hr /%}

  {% details %}
  {% summary %}
  **criteria**: `Criteria`

  Optional. Optional criteria for the `true` and `false` outcomes.

  {% /summary %}

  **true_description**: `string`

  Optional. Optional criteria or description for the `true` outcome.

  **false_description**: `string`

  Optional. Optional criteria or description for the `false` outcome.

  {% /details %}

  {% /section %}

{% /details %}

{% details %}
  {% summary %}
  **[ScoreQuestion](/api-reference/decisions#Resource:ScoreQuestion)**

  {% /summary %}

  A quantitative rubric scoring question over discrete numeric levels.

  {% section class="api-ref-property-list" %}
  **criteria**: {% mark %}required{% /mark %} `string array`

  Discrete score levels in the rubric (between 2 and 255 non-empty levels), where 0-based index `i` corresponds to numeric level value `i` and rubric description `criteria[i]`.

  {% hr /%}

  {% details %}
  {% summary %}
  **instructions**: {% mark %}required{% /mark %} `DecisionInstructionContent` or `DecisionInstructionContent array` or `string`

  Human-readable decision guidelines, rubrics, or criteria evaluated against the shared `input`. At least one content block is required.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent array**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **string**

  {% /summary %}

  A direct string value.

  {% /details %}

  {% /details %}

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `score`

  {% /section %}

{% /details %}

### NoulQuestion  {% id="Resource:NoulQuestion" %}

A binary (true / false) decision question.

**Properties:**

{% section class="api-ref-property-list" %}
  {% details %}
  {% summary %}
  **instructions**: {% mark %}required{% /mark %} `DecisionInstructionContent` or `DecisionInstructionContent array` or `string`

  Human-readable decision guidelines, rubrics, or criteria evaluated against the shared `input`. At least one content block is required.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent array**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **string**

  {% /summary %}

  A direct string value.

  {% /details %}

  {% /details %}

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `noul`

  {% hr /%}

  {% details %}
  {% summary %}
  **criteria**: `Criteria`

  Optional. Optional criteria for the `true` and `false` outcomes.

  {% /summary %}

  **true_description**: `string`

  Optional. Optional criteria or description for the `true` outcome.

  **false_description**: `string`

  Optional. Optional criteria or description for the `false` outcome.

  {% /details %}

{% /section %}

### ChoiceQuestion  {% id="Resource:ChoiceQuestion" %}

A single-select categorical decision question over mutually exclusive
options.

**Properties:**

{% section class="api-ref-property-list" %}
  **criteria**: {% mark %}required{% /mark %} `object`

  Mutually exclusive options to choose from (between 2 and 255 options), mapping option ID to optional description or rubric criteria. Option IDs must be non-empty with no control characters or leading/trailing whitespace.

  {% hr /%}

  {% details %}
  {% summary %}
  **instructions**: {% mark %}required{% /mark %} `DecisionInstructionContent` or `DecisionInstructionContent array` or `string`

  Human-readable decision guidelines, rubrics, or criteria evaluated against the shared `input`. At least one content block is required.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent array**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **string**

  {% /summary %}

  A direct string value.

  {% /details %}

  {% /details %}

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `choice`

{% /section %}

### ScoreQuestion  {% id="Resource:ScoreQuestion" %}

A quantitative rubric scoring question over discrete numeric levels.

**Properties:**

{% section class="api-ref-property-list" %}
  **criteria**: {% mark %}required{% /mark %} `string array`

  Discrete score levels in the rubric (between 2 and 255 non-empty levels), where 0-based index `i` corresponds to numeric level value `i` and rubric description `criteria[i]`.

  {% hr /%}

  {% details %}
  {% summary %}
  **instructions**: {% mark %}required{% /mark %} `DecisionInstructionContent` or `DecisionInstructionContent array` or `string`

  Human-readable decision guidelines, rubrics, or criteria evaluated against the shared `input`. At least one content block is required.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **DecisionInstructionContent array**

  {% /summary %}

  A text content block.

  **text**: {% mark %}required{% /mark %} `string`

  The text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `text`

  {% details %}
  {% summary %}
  **annotations**: `Annotation array`

  Citation information for model-generated content.

  {% /summary %}

  **Possible Types:** {% class="api-ref-label" %}

  {% details %}
  {% summary %}
  **FileCitation**

  {% /summary %}

  A file citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `file_citation`

  **document_uri**: `string`

  The URI of the file.

  **file_name**: `string`

  The name of the file.

  **source**: `string`

  Source attributed for a portion of the text.

  **custom_metadata**: `object`

  User provided metadata about the retrieved context.

  **page_number**: `integer`

  Page number of the cited document, if applicable.

  **media_id**: `string`

  Media ID in-case of image citations, if applicable.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **PlaceCitation**

  {% /summary %}

  A place citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `place_citation`

  **place_id**: `string`

  The ID of the place, in `places/{place_id}` format.

  **name**: `string`

  Title of the place.

  **url**: `string`

  URI reference of the place.

  {% details %}
  {% summary %}
  **review_snippets**: `ReviewSnippet array`

  Snippets of reviews that are used to generate answers about the features of a given place in Google Maps.

  {% /summary %}

  **title**: `string`

  Title of the review.

  **url**: `string`

  A link that corresponds to the user review on Google Maps.

  **review_id**: `string`

  The ID of the review snippet.

  {% /details %}

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **SpeechAnnotation**

  {% /summary %}

  Speech annotation for text content.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `speech_metadata`

  **speaker**: `string`

  The speaker to associate with this turn.

  **style**: `string`

  Style instruction for the speech synthesis.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **UrlCitation**

  {% /summary %}

  A URL citation annotation.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `url_citation`

  **url**: `string`

  The URL.

  **title**: `string`

  The title of the URL.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% details %}
  {% summary %}
  **WordInfo**

  {% /summary %}

  Word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

  **type**: {% mark %}required{% /mark %} `object`

  Value: `word_info`

  **text**: `string`

  The transcribed word.

  **start_offset**: `string`

  Start offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **end_offset**: `string`

  End offset in time of the word relative to the start of the audio. Present when timestamp_granularities contains "word".

  **speaker**: `string`

  Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarization_mode is set in TranscriptionConfig.

  **start_index**: `integer`

  Start of segment of the response that is attributed to this source. Index indicates the start of the segment, measured in bytes.

  **end_index**: `integer`

  End of the attributed segment, exclusive.

  {% /details %}

  {% /details %}

  {% /details %}

  {% details %}
  {% summary %}
  **string**

  {% /summary %}

  A direct string value.

  {% /details %}

  {% /details %}

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `score`

{% /section %}

### Answer  {% id="Resource:Answer" %}

Decision answer for a single question.

**Polymorphic Types:**

{% details %}
  {% summary %}
  **[ChoiceAnswer](/api-reference/decisions#Resource:ChoiceAnswer)**

  {% /summary %}

  Calibrated result for a [`ChoiceQuestion`](/api-reference/decisions#Resource:ChoiceQuestion).

  {% section class="api-ref-property-list" %}
  **choice**: {% mark %}required{% /mark %} `string`

  Output only. The option ID with the highest probability.

  {% hr /%}

  **probabilities**: {% mark %}required{% /mark %} `object`

  Output only. Closed-world normalized probability in `[0, 1]` for each option ID.

  {% hr /%}

  **confidence**: {% mark %}required{% /mark %} `number`

  Output only. Closed-world confidence score in `[0, 1]`, equal to the calibrated probability of the winning outcome:

  - [`NoulAnswer`](/api-reference/decisions#Resource:NoulAnswer): `max(noul, 1 - noul)`
  - [`ChoiceAnswer`](/api-reference/decisions#Resource:ChoiceAnswer): `p_max` (the probability of `choice`)
  - [`ScoreAnswer`](/api-reference/decisions#Resource:ScoreAnswer): `p_max` (the highest probability in `probabilities`).

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `choice`

  {% /section %}

{% /details %}

{% details %}
  {% summary %}
  **[NoulAnswer](/api-reference/decisions#Resource:NoulAnswer)**

  {% /summary %}

  Calibrated result for a [`NoulQuestion`](/api-reference/decisions#Resource:NoulQuestion).

  {% section class="api-ref-property-list" %}
  **noul**: {% mark %}required{% /mark %} `number`

  Output only. Calibrated probability `P(true)` in `[0.01, 0.99]`.

  {% hr /%}

  **confidence**: {% mark %}required{% /mark %} `number`

  Output only. Closed-world confidence score in `[0, 1]`, equal to the calibrated probability of the winning outcome:

  - [`NoulAnswer`](/api-reference/decisions#Resource:NoulAnswer): `max(noul, 1 - noul)`
  - [`ChoiceAnswer`](/api-reference/decisions#Resource:ChoiceAnswer): `p_max` (the probability of `choice`)
  - [`ScoreAnswer`](/api-reference/decisions#Resource:ScoreAnswer): `p_max` (the highest probability in `probabilities`).

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `noul`

  {% /section %}

{% /details %}

{% details %}
  {% summary %}
  **[ScoreAnswer](/api-reference/decisions#Resource:ScoreAnswer)**

  {% /summary %}

  Calibrated result for a [`ScoreQuestion`](/api-reference/decisions#Resource:ScoreQuestion).

  {% section class="api-ref-property-list" %}
  **score**: {% mark %}required{% /mark %} `number`

  Output only. Probability-weighted expected score (`sum_k k * probability_k`).

  {% hr /%}

  **probabilities**: {% mark %}required{% /mark %} `object`

  Output only. Closed-world normalized probability in `[0, 1]` for each 0-based level index.

  {% hr /%}

  **legend**: {% mark %}required{% /mark %} `object`

  Output only. Rubric description for each non-empty 0-based level index.

  {% hr /%}

  **confidence**: {% mark %}required{% /mark %} `number`

  Output only. Closed-world confidence score in `[0, 1]`, equal to the calibrated probability of the winning outcome:

  - [`NoulAnswer`](/api-reference/decisions#Resource:NoulAnswer): `max(noul, 1 - noul)`
  - [`ChoiceAnswer`](/api-reference/decisions#Resource:ChoiceAnswer): `p_max` (the probability of `choice`)
  - [`ScoreAnswer`](/api-reference/decisions#Resource:ScoreAnswer): `p_max` (the highest probability in `probabilities`).

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `score`

  {% /section %}

{% /details %}

### NoulAnswer  {% id="Resource:NoulAnswer" %}

Calibrated result for a [`NoulQuestion`](/api-reference/decisions#Resource:NoulQuestion).

**Properties:**

{% section class="api-ref-property-list" %}
  **noul**: {% mark %}required{% /mark %} `number`

  Output only. Calibrated probability `P(true)` in `[0.01, 0.99]`.

  {% hr /%}

  **confidence**: {% mark %}required{% /mark %} `number`

  Output only. Closed-world confidence score in `[0, 1]`, equal to the calibrated probability of the winning outcome:

  - [`NoulAnswer`](/api-reference/decisions#Resource:NoulAnswer): `max(noul, 1 - noul)`
  - [`ChoiceAnswer`](/api-reference/decisions#Resource:ChoiceAnswer): `p_max` (the probability of `choice`)
  - [`ScoreAnswer`](/api-reference/decisions#Resource:ScoreAnswer): `p_max` (the highest probability in `probabilities`).

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `noul`

{% /section %}

### ChoiceAnswer  {% id="Resource:ChoiceAnswer" %}

Calibrated result for a [`ChoiceQuestion`](/api-reference/decisions#Resource:ChoiceQuestion).

**Properties:**

{% section class="api-ref-property-list" %}
  **choice**: {% mark %}required{% /mark %} `string`

  Output only. The option ID with the highest probability.

  {% hr /%}

  **probabilities**: {% mark %}required{% /mark %} `object`

  Output only. Closed-world normalized probability in `[0, 1]` for each option ID.

  {% hr /%}

  **confidence**: {% mark %}required{% /mark %} `number`

  Output only. Closed-world confidence score in `[0, 1]`, equal to the calibrated probability of the winning outcome:

  - [`NoulAnswer`](/api-reference/decisions#Resource:NoulAnswer): `max(noul, 1 - noul)`
  - [`ChoiceAnswer`](/api-reference/decisions#Resource:ChoiceAnswer): `p_max` (the probability of `choice`)
  - [`ScoreAnswer`](/api-reference/decisions#Resource:ScoreAnswer): `p_max` (the highest probability in `probabilities`).

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `choice`

{% /section %}

### ScoreAnswer  {% id="Resource:ScoreAnswer" %}

Calibrated result for a [`ScoreQuestion`](/api-reference/decisions#Resource:ScoreQuestion).

**Properties:**

{% section class="api-ref-property-list" %}
  **score**: {% mark %}required{% /mark %} `number`

  Output only. Probability-weighted expected score (`sum_k k * probability_k`).

  {% hr /%}

  **probabilities**: {% mark %}required{% /mark %} `object`

  Output only. Closed-world normalized probability in `[0, 1]` for each 0-based level index.

  {% hr /%}

  **legend**: {% mark %}required{% /mark %} `object`

  Output only. Rubric description for each non-empty 0-based level index.

  {% hr /%}

  **confidence**: {% mark %}required{% /mark %} `number`

  Output only. Closed-world confidence score in `[0, 1]`, equal to the calibrated probability of the winning outcome:

  - [`NoulAnswer`](/api-reference/decisions#Resource:NoulAnswer): `max(noul, 1 - noul)`
  - [`ChoiceAnswer`](/api-reference/decisions#Resource:ChoiceAnswer): `p_max` (the probability of `choice`)
  - [`ScoreAnswer`](/api-reference/decisions#Resource:ScoreAnswer): `p_max` (the highest probability in `probabilities`).

  {% hr /%}

  **type**: {% mark %}required{% /mark %} `object`

  Value: `score`

{% /section %}

### PromptFeedback  {% id="Resource:PromptFeedback" %}

Feedback from input content filters.

**Properties:**

{% section class="api-ref-property-list" %}
  {% details %}
  {% summary %}
  **block_reason**: `string enum`

  Optional. If set, the input was blocked and no answers are returned.

  {% /summary %}

  Possible values:

  - `safety`: Prompt was blocked due to safety reasons.
  - `other`: Prompt was blocked due to unknown reasons.
  - `blocklist`: Prompt was blocked due to terms from the terminology blocklist.
  - `prohibited_content`: Prompt was blocked due to prohibited content.
  - `image_safety`: Prompt was blocked due to unsafe image content.

  {% /details %}

  {% hr /%}

  **block_reason_message**: `string`

  Optional. Optional message detailing the reason for blocking.

{% /section %}


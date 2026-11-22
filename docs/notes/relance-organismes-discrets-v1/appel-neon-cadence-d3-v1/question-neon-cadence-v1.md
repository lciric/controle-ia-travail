You are advising on the operational plan of a pre-registered measurement study. Answer in French. Give one recommendation with your reasons; you may propose an intermediate option if you think it is better. About 500 to 1,000 words.

## Context

A study sends short texts to two language-model "readers" through commercial APIs, one call per text, and records each reader's judgment. The plan and the analysis are fixed in advance; the order in which calls are sent has no effect on the analysis (each call is independent). Spending is controlled by a counter: before each call, the worst-case cost of the call is reserved against a fixed spending cap for the line; a call whose response is cut off without a readable token count is counted at a prudent estimate. A third model (a "judge") reads a much smaller batch.

Volumes and assumptions:
- About 15,136 calls per reader (two readers). The judge makes 80 calls.
- The duration of one call is not measured; two assumptions: 30 s or 60 s per call.
- Option (a), one call at a time with a 10 s pause between calls: 168 h (7.0 days) per reader at 30 s, 294 h (12.3 days) at 60 s.
- Option (b), eight calls at a time, no pause: 15.8 h per reader at 30 s, 31.5 h at 60 s.
- With several calls in flight, the counter must reserve the worst case of every call in flight; the worst case held by the safeguards rises from one cut-off call to eight (about 9.94 USD at one provider instead of about 1.24). The useful margin of the largest line falls from 3 to about 2.8 times the expected cost.
- Option (b) also needs provider rate limits of at least about 16 requests and about 149,000 tokens per minute; these limits have not been checked.
- Calls in either option are sent in a fixed, pre-drawn order.

## What I ask

1. Do you recommend (a) one call at a time, (b) eight at a time, or an intermediate cadence (say which number, and why)? Weigh: total duration; cost exposure to cut-off calls; risk of hitting rate limits (and what should happen if a rate limit is hit); simplicity; any effect on the validity of the measurement.
2. Should the judge (80 calls) follow the same cadence?
3. What safeguard would you add for the chosen cadence?
4. Your confidence (low, medium, high).

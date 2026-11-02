# Kirchner Q1 — v46 — passages de Lazar (22:21 UTC), fond corrigé

If you haven’t seen/heard: I’ve been running automated researchers since October (github.com/lciric/ideation-organism). Agents generate submissions meant to codify laws; a statistical judge scores submissions.
Pitch: what happens when you score submissions proposing laws for how AI makes decisions with something arguments can’t lie to? Will it hold up against agents motivated to trick it?
In short: yes to Q1. Partly to Q2. Our attack found a hole. Patch posted, preregistered test to come.
Builders built stuff. Builders tested builders. Proposers of many different archetypes with multiple algorithms submitted to our frozen statistical judge. Said judge scored each proposed law based on how well it could be distinguished from a null hypothesis. Death tests preregistered, to run in sandbox with a model from a completely different family as sanity check (tested offline, not yet run for real).
929 tests total.
Mutation benchmark: the code was mutated 224 times, checking that all mutations get caught by tests. Every time a test failed pinpointing precisely what was mutated and exactly which test caught the failure.
Kept what passed.
Totally lost the forest for trees here initially because qualitative judgments made by my LLM judges kept failing against my frozen statistical judge. They told me nothing, literally called 11 of 12 cards “notable”. κ = 0, inter-agreement. The terse statistical judge told me why nothing was promoted: not enough power. Turns out I just didn’t test it long enough to know if there actually was a law to be found there. The power curve suggested as much.
Then I ran it one last time with no deviations from the locked plan on a completely different seed pass of 288 episodes that I did not inspect prior to launching this datapass.

It accepted all 3 laws I placed into the data.
It rejected all 19 placed non-laws.
It accepted 0 laws found from the raw data itself.

Scripted cheating agents broke it. 4 accepted total. All stitched together or deformed past submissions that the judge had already accepted.
My judge had no null for blends of its past acceptances.
This was obvious to me the second I wrote that sentence but I smashed my head into a wall. Preventing bribing was cracked pretty quickly. Protecting it against systematic agents that can tailor make submissions using its past accepts to trick it was more difficult.
We’ve gone through dozens of iterations since October. That failure above is a cousin of the trick in 26 of your 39 cheating examples from the automated-researcher paper. Flip a coin twice. Wait for randomness to make your method win.
On 1 November the fix passed its preregistered validation (1k reps per algorithm; double checked by a fresh reader, a new Claude instance, who wrote neither code nor words). And now… the attack.

Attack agents. Agents with skin in the game trying to systematically game it. Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. They found a hole, with or without the past acceptances, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look.
Patches written and deployed into regression tests as we speak. Its preregistered validation starts tomorrow.

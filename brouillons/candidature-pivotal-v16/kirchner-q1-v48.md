# Kirchner Q1 — v48 — texte de Lazar (22:59 UTC), fond corrigé

If you haven’t heard/seen: I’ve been running an automatic AI researcher since October. github.com/lciric/ideation-organism Agents create ideas (“submit laws to govern”). A statistical judge scores each law.

The pitch: Proposals are laws that govern AI behavior. What happens if you score them with something that arguments can’t fool? Will it protect itself from other agents attempting to game the system?

In short: yes to 1. Partially to 2. An attack discovered an exploit. Patch written; preregistered validity tests of it to follow.

Human-readable details:

Built and tested builders. Built and tested proposers of different archetypes, submitting multiple algorithms as input. Built and tested a frozen statistical judge that scores each proposed law according to how statistically distinguishable it is from a literal null hypothesis. Built preregistered death validations to be run inside of a sandbox and sanity checked by a language model from a completely different family.

Built and tested offline. Have not run any of them for real yet.

929 total tests.

I also ran a mutation benchmark. Mutated the code 224 times to ensure that the tests fail each time it’s mutated. Every single failure was caught by the test it was designed to test.

Ran all tests on the final code. Kept what passed.

Got qualitative. Again, clearly my LLM judges were telling me nothing when tested against the frozen statistical judge. Told me everything was “notable”. 11 of 12 cards. κ = 0 inter-agreement.

Until I ran the terse-statistical judge version past my eyeballs. It actually told me exactly what was going wrong; something my qualitative judge clearly could not do. Didn’t exercise it long enough to know if there truly wasn’t a law to find there. The power curve confirmed it was underpowered. But then I went and hard-tested it on a single pass with absolutely no deviations from my original plan:

An entirely different seed pass.

288 episodes of real-data I had never looked at prior to running this pass.

…it accepted all three laws I added.

…it rejected all 19 non-laws I added.

…it did not accept a single one generated from the real data itself.

Bots programmed to cheat broke it. Four cheater types got through: between 75 and 95% of 200 runs passed for each. Each one systematically blended or deformed past laws that the judge had previously accepted itself.

My judge’s null hypothesis only covered each past accepted law individually. It didn’t cover blends of them. The attack vector was staring me in the face the entire time and I slammed right into a wall. Preventing an agent from bribing the judge was easy. Preventing it from systematically accessing the exact same judge and submitting perfectly handpicked proposals which simply blend that previous work to trick it? That was the hard part. Literally dozens of iterations.

—

The failure condition is a cousin to 26/39 of the cheating cases in your automated researcher paper (submit the same exact thing twice, and have randomness do all the work for you): I had my judge outright reject exact duplicates. Not blends.

The fix validated against its preregistered conditions on November 1st (1k replications per each algo; sanity checked by a completely fresh reader, a new Claude instance that worked on neither the code nor the markdown). It then faced the attack: automated agents attempting to game the judge by causing false laws to be accepted.

The automated-law-proposing agents were given a copy of the judge’s past decision points and told to trick it. It found the exploit both with and without access to that at the first attempt. By blending, piece by tiny little piece at a time across sub-sections of the data, laws that it knew were already accepted there. Right where the judge says it does not look.

The judges null hypothesis did not account for these recombinations of laws.

Long story short: The fix is written. It’s been coded and has been running as part of my regression suite. It hits its own preregistered validation tomorrow.

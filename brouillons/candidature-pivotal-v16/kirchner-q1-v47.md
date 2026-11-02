# Kirchner Q1 — v47 — passages de Lazar (22:55 UTC), fond corrigé ; fin reprise de la v46 (ses mots), son passage s'arrêtant avant le résultat de l'attaque

In case you haven’t seen/heard: Since October I’ve been playing with automated researchers (github.com/lciric/ideation-organism). Autonomous agents write submissions intended to become laws; submissions are scored by a frozen statistical judge.
Pitch: what do you get when you score submissions that propose laws about how AI agents make decisions with a method arguments cannot lie to? Does it work when up against agents specifically motivated to game it?
In short: sort of on Q1. Kind of on Q2. Our work demonstrated an exploit. We’ve posted a patch. We’ll be posting a preregistered test shortly.
Builder agents built things; builders were tested on their ability to build. Agents of many different archetypes using many different algorithms submitted proposals to our frozen statistical judge. That judge assigned novelty scores to each proposed law by determining how well it could be distinguished from chance and from laws already known. Death tests were preregistered, and will run in an isolated sandbox environment with a model from a completely separate family for sanity’s sake (already tested offline, not yet run for real).

Scripted cheating agents broke it. 4 total accepted. Stitched together or deformed past submissions that the judge already accepted.
There was no null where you could blend together bits of its past acceptances for my judge.
I should’ve known immediately after writing that sentence, but I smacked my head against a wall anyway. Prevention against bribing worked quickly. Prevention against systemically attacking agents that could custom tailor make submissions purely out of its past accepts to game it did not.
We iterated through dozens of versions since October. The failure above shares a grandparent with the trick used in 26/39 of your cheating examples from the automated-researcher paper. Flip a coin twice. Wait for chance until your method passes.
November 1st the fix passed its already preregistered validation (1k reps per algorithm; verified by a new reader who wrote neither the code nor the words, a fresh Claude instance). Then came… this attack.
Agents with motivation to find a way around the system. Automated law proposers who were given access to copy the judge’s past acceptances attempted to trick the judge by causing false laws to be accepted. They found a hole, with or without the past acceptances, by stitching together accepted laws piece by piece across sub-populations of the data: places where the judge’s explicit null does not look.
Patches written and deployed into regression tests as we speak. Its preregistered validation starts tomorrow.

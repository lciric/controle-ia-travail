So you want to know how to detect goodharting by auto researchers in your setup. My question was adjacent: if we use this selection function will they fail to goodhart and if they do how?

I created an auto research setup. Agents using LMs propose laws about AI control. All are blind predictions. None of the agents decides what survives. Created in Oct with AI code agents. Rules I gave it here https://github.com/lciric/ideation-organism. Decided by a frozen testing procedure. Calculates e-values on new random seeds derived from the law's hash. Null is composed of all laws previously accepted. Ville + e-BH between submissions. 929 tests run. I mutated the code intentionally 224 times and the tests caught every mutation, for the expected reason.

I then attempted to attack it using scripted cheaters on toy problems. Goodhart by luck, the only cheat that made it into a top 3 placement in your paper (it didn't pass your hold out choice either), never got promoted here: 0/200 times by renaming an already accepted law. What passed was a mixture or changed version of already accepted laws 75-95% of 200 trials. My null didn't have any of these in it. By expanding my null to a fitted pooling of all known laws I was able to stop them. 0/1000 for each of the 11 ways to kill it that I pre registered. Nov 1st. While true new laws continued to pass ~98% of the time.

I then let LMs attack it. Given the judge's description. With or without its decisions. Nov 2nd https://github.com/lciric/ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2 . These toy problems were made only from laws that are already accepted. If something passes, it is a false claim of a new law. One problem was able to be constructed by changing accepted laws per subpopulation. This isn't covered by my null. On that problem, the only model that I could get to finish got a law accepted all 12 times it ran. Whether or not it knew about the decisions. The other problem, which my null does cover, wasn't testable. Monitoring bug and spending limit I shared accidentally blocked one provider.

Interesting finding. I thought that if the attacker knew about the decisions it would allow them to goodhart better. There weren't many chances for this to happen. 11 out of the 12 accepted laws happened on their first try. Before there was a decision to learn from. So here, if I hid my scores or limited the number of submissions it wouldn't have stopped them. The two attacks that were successful both used my judge's own record. First what it accepted, then its description.

The fix is to expand my null to include some of these combinations. Which I pre registered on Nov 2nd. And expected to lose power on true weak interactions. Have a pre registered retry of my attack. Haven't gotten any real hypothesis accepted yet.

---
Version du directeur (conv-audit), 3 novembre 2026, depuis `reponse-lazar-reformulee-v1.md` (texte de Lazar, 21:37 heure de Paris) : corrections de fond minimales seulement, chacune appuyée sur la v3 vérifiée (`reponse-v3.md` `3592a009…`) ou sur le README public au commit `faff48b`. Paragraphes séparés par une ligne vide.
1. **Grave** : « Goodhart by luck did not make it into a top 3 placement in your paper » → « the only cheat that made it into a top 3 placement » : c'est l'inverse (§ 7 du papier, mot pour mot dans la v3 vérifiée).
2. **Grave** : « If something passes it means it found a new law » → « it is a false claim of a new law » : les mondes sont faits des seules lois acceptées ; toute promotion est une fausse nouveauté.
3. « laws that will try to contain AI » → « propose laws about AI control » : ce sont des lois (prédictions scellées) sur le contrôle, pas des dispositifs qui contiennent.
4. « There is no decision maker » → « None of the agents decides what survives » : le juge statistique figé décide (phrase suivante).
5. « it failed every time as expected » → « the tests caught every mutation, for the expected reason » (README : « every one killed for the expected reason »).
6. « automated cheaters » → « scripted cheaters » : distingue ces tricheurs des attaquants à modèles de langue du paragraphe suivant.
7. « expanding my null to include all submitted » → « to a fitted pooling of all known laws » (README l. 82 : « fitted pooling of all known laws »).
8. « 11 ways to kill me » → « 11 ways to kill it » : les lignes mortelles visent le juge.
9. « the judges instructions » et « it's instructions » → « description » : un juge statistique n'a pas d'instructions ; les attaquants avaient sa description exacte.
10. « One model that I could get to finish all problems » → « On that problem, the only model that I could get to finish » : il a couru en entier dans ce monde ; l'autre monde n'a pas pu être jugé.
11. « The other problem that I could make it » → « The other problem, which my null does cover » (v3 : « The other world, inside the null »).
12. « both learned about my judges decisions » → « both used my judge's own record » : 11 promotions sur 12 sont venues avant tout verdict ; ce qui a servi, ce sont les lois acceptées puis la description.
13. « So if I hid my scores… » → « So here, if I hid… » : la conclusion vaut pour ce monde.
14. Orthographe qui touchait le sens : « there decisions » → « its decisions », « e-value's » → « e-values », « LM's » → « LMs », « laws hash » → « law's hash ».

# Brouillon — candidature au programme d'accès pour chercheurs d'OpenAI (crédits de l'interface de programmation), v1

- Écrit le 2026-11-23 vers 13:20Z, sur le mot de Lazar « go prépare la candidature » (session `session_016QhUrsc1rhjmmiLEmqPygF`). Classe C. **Contact externe : c'est Lazar qui crée le compte et envoie** ; rien n'a été envoyé ni rempli.
- Ce que l'on sait du programme (pages lues le 23 novembre ; aucune n'est datée, « mise à jour il y a 4 jours » pour la FAQ) : jusqu'à 1 000 USD de crédits, valables 12 mois, ni prolongés ni transférés ; dépôt à tout moment ; examen trimestriel (mars, juin, septembre, **décembre**) ; crédits 4 à 6 semaines après la décision ; priorité aux recherches sur le déploiement responsable et la réduction des risques, aux chercheurs en début de carrière et aux ressources limitées ; domaines listés, dont « Alignment » et « Misuse potential ». Sources : https://openai.com/form/researcher-access-program ; https://help.openai.com/en/articles/10139500-researcher-access-program-faq.
- **Le formulaire lui-même** est chez un prestataire tiers, https://openai.smapply.org/prog/openai_researcher_access_program/, après création d'un compte : ses champs exacts (libellés, limites de longueur) ne sont pas connus. Le texte ci-dessous est donc rangé par ce que la page dit être demandé (question de recherche, usage prévu des produits d'OpenAI) et par les rubriques habituelles ; à couper ou ajuster aux champs réels. Si tu me donnes les libellés et les limites, j'ajuste.
- À lire avant d'envoyer : la politique de partage et de publication d'OpenAI pour la recherche (https://openai.com/policies/sharing-publication-policy/#research), citée par la page.
- Langue : le formulaire est en anglais ; le texte à coller est en anglais, avec mes notes en français entre crochets.

## Points à trancher par Lazar avant l'envoi
1. **Qui candidate** : toi seul, sous ton affiliation (l'adresse de l'École normale supérieure Paris-Saclay est celle du compte), ou avec un encadrant ? Le programme favorise le début de carrière et les ressources limitées : dis-le si c'est vrai, sans l'enjoliver.
2. **Ce que l'on dit du programme** : le texte ci-dessous ne décrit que les questions, sans résultat ni revendication (rien n'est encore établi ; plusieurs revendications ont été resserrées) ; il ne nomme ni les modes de sabotage ni les organismes, qui sont cloisonnés. À garder ainsi.
3. **Compte de l'interface** : les crédits vont à une organisation de l'interface dont tu es propriétaire ; celle qui sert déjà à Astra ou une neuve.
4. **Montant demandé** : 1 000 USD (le plafond), justifié par l'estimation de la rubrique 5.

---

## Texte à coller (anglais)

**Applicant** : [NOM, PRÉNOM] — [STATUT : doctorant / chercheur indépendant / …] — [AFFILIATION : École normale supérieure Paris-Saclay, …] — [PAYS : France] — [ADRESSE ÉLECTRONIQUE] — [ORCID ou page, si existant]

**Project title** : White-box monitoring of diffuse threats from AI agents: do internal-state monitors survive adaptive attackers, and how do they compare with black-box LLM judges?

**1. Research question (short)**
AI control evaluations ask whether a deployed agent that may be misaligned can be prevented from causing harm by monitoring. Most monitors read the agent's actions one at a time. We study *diffuse* threats, where harm is spread over many individually innocuous actions, over time or across several copies of the same model. Our question is what a monitor actually measures, and whether that measurement survives an adversary: (A) when the attack is fragmented over time, (B) when it is distributed across agents that share weights, and (C) when the attacker targets the monitor itself, for instance by persuading an LLM judge. We compare monitors that read the agent's internal activations (linear and non-linear probes, aggregated sequentially with false-positive guarantees that stay valid under optional stopping) with black-box LLM judges that read only text.

**2. Why it matters for responsible deployment**
If per-action monitoring fails by construction on diffuse sabotage, deployment safety cases that rely on it are overstated. If internal-state monitors help, the gain has to be measured against strong text-only baselines and adaptive attackers, not assumed. Either result is useful; we pre-register every decisive experiment (hypothesis, predicted sign, metric, threshold, analysis plan) before running it, and report null and negative results.

**3. How we would use OpenAI models**
- *Black-box judges from a different model lineage.* Our protocol requires at least one judge from another lineage than the monitored agent and than the other judges, so that a shared blind spot or a shared susceptibility to persuasion is not mistaken for a property of monitoring in general. We would use OpenAI models as text-only judges and as baselines on the same episodes the internal monitors see, including under attacks that target the judge.
- *Independent proposers in structured, multi-model ideation panels.* We run pre-registered panels in which models from several labs answer the same neutral question, critique each other, and answer again; we measure which proposals survive tests on planted ground truth rather than on a judge's verdict. An OpenAI model is one of the independent proposers.
- No fine-tuning of OpenAI models; no attempt to extract training data, weights, or system prompts; all use within the Usage Policies.

**4. Outputs and sharing**
Pre-registrations, code, and aggregate results will be released with the papers, following OpenAI's sharing and publication policy for research. Episodes or prompts that would work as a ready-made attack on deployed monitors are withheld from public release.

**5. Budget estimate** [estimation de ma part, à vérifier contre les prix affichés le jour de l'envoi]
At the list price we last recorded for the model we use (USD 8 per million input tokens and USD 40 per million output tokens, below 272k input tokens), a judge call of about 20,000 input and 4,000 output tokens costs about USD 0.32, and a panel answer of about 30,000 input and 16,000 output tokens about USD 0.88. USD 1,000 over 12 months covers roughly 2,000 judge calls on our evaluation episodes plus about 300 panel answers.

**6. Timeline**
Instrument phase until end of December 2026; first pre-registered comparisons of internal monitors and black-box judges from January 2027.

---

## Notes de la session (non à coller)
- Le prix « 8 / 40 USD par million » vient de la passation des collisionneurs du 22 novembre (`registres/passations/2026-11-22-1546-collisionneurs.md`, § 5), relevé alors, non revérifié sur la page des prix aujourd'hui.
- Les volumes de la rubrique 5 sont des ordres de grandeur, pas un devis ; ils ne comptent pas comme accord de dépense.
- Rien de ce texte n'engage une hypothèse ou une revendication du programme ; si tu veux y ajouter un résultat, il faut un verdict scellé.

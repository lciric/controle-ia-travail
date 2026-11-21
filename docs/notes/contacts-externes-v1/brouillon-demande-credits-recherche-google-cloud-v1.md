# Brouillon — demande de crédits de recherche Google Cloud — v1

Pièce de travail (classe C), session du compte organisme, 2026-11-21. **Contact externe : rédigé ici, envoyé par Lazar seul.** Aucune donnée personnelle n'est écrite : les champs entre crochets sont à remplir par Lazar au moment d'envoyer. Rien de cloisonné (ni score, ni verdict, ni consigne de saboteur, ni nom de pièce réservée).

## Avant d'envoyer : éligibilité (à vérifier sur la page officielle)

- Formulaire : https://edu.google.com/programs/credits/research/ (questions fréquentes : https://support.google.com/google-cloud-higher-ed/answer/10324705).
- D'après ces pages, telles que lues par une recherche le 2026-11-21 et sans garantie qu'elles soient à jour : le demandeur doit être **enseignant-chercheur, doctorant ou postdoctorant** d'un établissement d'enseignement supérieur accrédité, ou d'un organisme de recherche **à but non lucratif**, dans un pays éligible. Les structures à but lucratif ne sont pas reçues. Plafond : 5 000 USD une fois pour un enseignant-chercheur ou un postdoctorant ; 1 000 USD par an pour un doctorant.
- **Si Lazar n'a pas un tel rattachement, la demande sera refusée.** Voies voisines à regarder alors : une demande portée par un chercheur rattaché qui co-signe ; le programme de crédits pour chercheurs européens en intelligence artificielle annoncé par Google (statut non vérifié) ; le programme Google for Startups Cloud, si une structure existe.
- Les crédits ne servent qu'à la recherche décrite dans la demande.
- Point technique : les crédits Google Cloud se dépensent par **Vertex AI**. La clé actuelle du relais Argon (`GEMINI_API_KEY`, interface de développement de Gemini) n'est pas réglée par ces crédits ; il faudrait un relais vers Vertex AI (code neuf, contre-lu, sur le mot de Lazar).

## Texte du formulaire (anglais, prêt à coller)

**Applicant name:** [Nom Prénom]
**Email (institutional):** [adresse de l'établissement]
**Position:** [Faculty / Postdoctoral researcher / PhD student]
**Institution and department:** [établissement, laboratoire]
**Country:** [pays]
**Google Cloud billing account ID (if any):** [identifiant, sinon laisser vide]

**Project title:**
White-box monitoring of diffuse sabotage by language-model agents

**Research area:** Machine learning — AI safety (AI control, monitoring of autonomous agents)

**Abstract (≈150 words):**
As language-model agents are deployed on long, open-ended tasks, a misaligned agent need not cause one visible catastrophe: it can degrade outcomes slightly and repeatedly ("diffuse" sabotage), staying below what output-only monitors flag. Our project builds and evaluates monitors that read an agent's internal activations (probes) in addition to its text, and tests whether they detect diffuse sabotage better than strong black-box baselines (text-only judges, length-and-cost baselines) on held-out task families. Every decisive experiment is preregistered and sealed before results are read, each preregistration is reviewed by an independent reviewer, and negative results are reported. We use a judge from a different model lineage than the agents and monitors under study, so that the judge does not share their blind spots. The credits would fund these independent-lineage judge and reader calls on Gemini models through Vertex AI.

**How will you use Google Cloud? (≈200 words):**
We request credits for Gemini model calls through Vertex AI, used in three roles of our evaluation pipeline:
1. *Independent-lineage judge*: grading agent outputs on fuzzy tasks, so that the judge's verdicts are not produced by the same model family as the agents and probes we evaluate.
2. *Witness reader*: reading planted control cases (known-honest and known-sabotaged episodes) before any real result is read, to check that the judge can fail and can succeed (sanity checks run before the main evaluation).
3. *Comparison baseline*: a black-box text-only monitor against which white-box probes must show a gain.
Calls are made by a local relay that enforces a hard spending cap and logs every request; runs start only after a written cost estimate is approved. No user data or personal data is processed; inputs are synthetic tasks and model-generated episodes.

**Estimated budget:** [montant demandé, 5 000 USD au plus ; à tirer du devis des lignes Argon]
- Gemini calls on Vertex AI, judge and reader roles: [montant]
- Storage of logs and sealed outputs (Cloud Storage): [montant, faible]

**Timeline:** [date de début] to [date de fin] — instrument phase until end of December 2026, then the main evaluation in 2027.

**Expected outputs:** Preregistrations, sealed result files and a paper on white-box monitoring of diffuse sabotage; code for the monitors and evaluation harness, released where safe.

**Prior publications / links (optional):** [liens publics, s'il y en a]

## Ce que Lazar vérifie avant d'envoyer

1. Le rattachement exigé (sinon, ne pas envoyer en son nom seul).
2. Le montant, tiré d'un devis et non deviné.
3. Que le texte ne contient rien de ce que le programme garde fermé, ni de lien vers le dépôt de travail privé.
4. Le consigner : contact externe, date, adresse d'envoi, au registre prévu.

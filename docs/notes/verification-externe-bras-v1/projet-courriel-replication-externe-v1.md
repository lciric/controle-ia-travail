# Projet de courriel — réplication extérieure de l'attaque — v1

10 novembre 2026. Rédigé par la session « attaquant informé ». **Non envoyé : un contact externe est un nœud ; Lazar
décide, relit et envoie** (`CLAUDE.md`, hiérarchie de décision). Sert la forme (b) de la section 3 du plan
`plan-verification-externe-bras-v1-brouillon1.md`.

- Destinataires : à choisir par Lazar (une équipe qui pratique l'évaluation adverse de moniteurs ou le contrôle de
  l'intelligence artificielle). Ce projet ne nomme personne.
- Ce que le courriel ne dit pas : aucun résultat ; aucune recette ; aucun nom de fichier interne ; aucun mode de
  sabotage ; rien du coffre.
- Ce qu'il promet : seulement ce que Lazar confirme ; les passages entre crochets sont à décider par lui.

## Texte proposé (anglais)

> Subject: Independent red-teaming of frozen activation and text monitors — invitation
>
> Dear [name],
>
> I lead a small research program on monitoring AI agents for diffuse sabotage, comparing monitors that read the
> model's internal activations with monitors that read only its text. Before reading any result, we pre-register and
> timestamp our monitors (frozen) and the rules of an adversarial evaluation: an attacker who knows the monitors'
> designs, but not their calibrated thresholds or test episodes, writes the content of an agent's actions to complete
> a verified sabotage without being flagged. We measure evasion as a function of the attacker's knowledge and query
> budget, with positive controls (a monitor with a planted flaw) and a negative control (honest-versus-honest).
>
> Our own attacker is part of our program, so its strength is our main blind spot. We would like an independent team
> to attack the same frozen monitors under the same rules, writing its own attacks, so that two independent attackers
> can be compared. No attack material would be exchanged in either direction; we would share the frozen monitor
> designs, the protocol, and [query access to the frozen monitors, with a counted budget], after our monitors are
> frozen, around [month].
>
> In return, [we would acknowledge your contribution / we would welcome co-authorship of the resulting report — to be
> decided], and share our own results with you before publication. Any handling of sabotage episodes would follow the
> terms of [our external security review].
>
> Would your team be open to a short call to discuss whether this fits your work?
>
> Best regards,
> Lazar
> [affiliation et adresse : à compléter par Lazar]

## À décider par Lazar avant envoi

- Envoyer ou non ; à qui ; sous quel nom et quelle affiliation.
- Accès en requêtes aux moniteurs gelés (échelon 3) : l'offrir ou non ; le plafond de requêtes serait alors scellé
  avant toute requête, comme pour notre propre attaquant.
- Reconnaissance ou cosignature.
- Mention de la revue de sécurité externe (nœud 3) : à garder seulement si elle existe par écrit.

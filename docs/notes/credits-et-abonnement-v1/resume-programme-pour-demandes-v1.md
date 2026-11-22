# Résumé du programme pour les demandes de crédits (version 1)

- Date : 2026-11-22T07:57:24Z (`date -u`)
- Rôle : résumé d'une page en anglais, réutilisé par les trois demandes (Anthropic, Amazon, Google). Texte à coller ; le directeur remplit les champs entre crochets.
- Sources internes : `docs/notes/demandes-fable-api-2026-11-22-v1/contexte-programme-v1.md` ; devis de l'organisme d'idéation dans `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-14/relecture-fable-api.md` (devis réduit : 200 à 450 USD avec Kimi, 700 à 1 500 USD avec Claude ; pilote 300 à 800 USD avec Claude) ; plafonds de calcul inscrits dans `registres/go.md` (GO-2026-11-20-08 : course de l'organisme, plafond 450 USD ; GO-2026-11-21-42 : plafond commun de 200 USD d'une épreuve sur cartes louées) ; dépôt de travail (comptes de fichiers relevés le 2026-11-22 : 164 préenregistrements avec compagnon d'empreinte, versions comprises ; 75 manifestes de run ; 469 fichiers d'essais).
- Pages en ligne consultées : aucune pour ce résumé (il ne cite aucun fait extérieur).
- Ce qui est vérifié : les comptes de fichiers (relevés sur disque) et les montants des devis (relus dans les fichiers cités). Ce qui ne l'est pas : le besoin total sur six mois est une estimation faite à partir de ces devis, non un devis scellé. Aucun résultat n'est revendiqué ; aucun chiffre de l'état de l'art.

---

## Text to paste (English)

**White-box control of diffuse sabotage by AI agents — [NOM], [AFFILIATION]**

**Problem.** AI agents are increasingly given long research and analysis tasks. A misaligned or compromised agent need not do anything obviously wrong: it can degrade the result diffusely, through many steps that each look honest, so that the damage only shows in aggregate. Monitors that read the agent's text (black-box judges) may miss such sabotage. This program asks whether, and under which conditions, monitors that read the agent's internal activations (white-box probes) help detect diffuse sabotage, and how much they add over strong black-box baselines.

**Method.** We build test organisms on open-weight models (Llama 3.1 8B and similar) that perform long tasks honestly or with planted diffuse sabotage. We compare linear probes on internal activations against text judges and named baselines (word-and-cost statistics, cascades, last-state readers), with one sabotage mode held out from monitor design and results reported per mode. Detection rates are measured on planted damage with known ground truth; a published random audit floor is the primary safeguard, and probes are treated as an accelerator of auditing, not as a guarantee. A separate automated ideation organism (several models that propose, criticise and refine ideas) generates candidate attacks and hypotheses, judged against planted ground truth and cost. Every decisive experiment is pre-registered and cryptographically sealed (SHA-256) before any result is read; each pre-registration is counter-read by an independent model; negative results are reported.

**Already done.** Measurement infrastructure (sealing, run manifests with seeds and versions, compute guards); 164 pre-registration documents with SHA-256 companions (including successive versions); 75 run manifests; a test suite of 469 test files; first training runs of probes on agent activations and first runs of the ideation organism. No result is claimed here: verdicts are issued only after sealed criteria are applied by an independent reviewer.

**Compute needed (estimate from our internal cost estimates).** (1) Claude API for the ideation organism and for judges: 700 to 1,500 USD per reduced campaign with Claude as proposer (300 to 800 USD for its pilot); we expect two to three campaigns over six months, since a failed gate triggers a redesign cycle that must also be run and reported. (2) GPU hours for probe training and evaluation on open-weight models: past single experiments were capped at 200 to 450 USD each. Total need over six months: roughly [MONTANT TOTAL, par exemple 3,000 to 6,000] USD.

**Planned public outputs.** Three papers (A: probes against diffuse sabotage; B: joint statistics of probe scores across agent copies, with anytime-valid guarantees; C: judges of automated research under attack); a public, redacted copy of the code and pre-registrations ([LIEN DÉPÔT PUBLIC]); a benchmark with planted ground truth for diffuse sabotage, released once the held-out evaluation is complete.

---

## Traduction française (pour le directeur, à ne pas coller)

**Contrôle boîte blanche du sabotage diffus par des agents d'intelligence artificielle — [NOM], [AFFILIATION]**

**Problème.** On confie de plus en plus aux agents de longues tâches de recherche et d'analyse. Un agent désaligné ou compromis n'a pas besoin de faire quelque chose de visiblement faux : il peut dégrader le résultat de façon diffuse, par de nombreuses étapes qui semblent chacune honnêtes, si bien que le dommage n'apparaît qu'en cumul. Les moniteurs qui lisent le texte de l'agent (juges boîte noire) peuvent manquer ce sabotage. Le programme demande si, et à quelles conditions, des moniteurs qui lisent les activations internes de l'agent (sondes boîte blanche) aident à détecter le sabotage diffus, et ce qu'ils ajoutent à des bases boîte noire fortes.

**Méthode.** Organismes de test sur des modèles ouverts (Llama 3.1 8B et voisins), honnêtes ou porteurs d'un sabotage diffus planté. Sondes linéaires comparées aux juges de texte et aux bases nommées (mots et coût, cascade, dernier état), un mode de sabotage tenu à l'écart de la conception des moniteurs, résultats rapportés par mode. Taux de détection mesurés sur des dommages plantés à vérité connue ; plancher d'audit au hasard publié comme garde première ; sondes traitées en accélérateur de l'audit, non en garantie. Organisme d'idéation automatisé, jugé sur la vérité plantée et le coût. Toute expérience décisive préenregistrée et scellée avant lecture, contre-lue par un modèle indépendant ; résultats négatifs rapportés.

**Déjà fait.** Instruments (scellement, manifestes de run, gardes de calcul) ; 164 préenregistrements à compagnon d'empreinte, versions comprises ; 75 manifestes de run ; 469 fichiers d'essais ; premières courses d'apprentissage de sondes et de l'organisme d'idéation. Aucun résultat revendiqué.

**Besoin en calcul (estimation tirée des devis internes).** Interface de Claude : 700 à 1 500 USD par campagne réduite (pilote 300 à 800), deux à trois campagnes en six mois ; heures de cartes graphiques : plafonds passés de 200 à 450 USD par expérience. Total sur six mois : [MONTANT TOTAL] USD.

**Livrables publics prévus.** Papiers A, B, C ; copie publique expurgée du code et des préenregistrements ; banc à vérité plantée publié après l'évaluation tenue à l'écart.

## Réserves

- Le montant total est à fixer par le directeur ; la fourchette proposée (3 000 à 6 000 USD) additionne deux à trois campagnes Claude au devis réduit et quelques expériences sur cartes aux plafonds passés : c'est un ordre de grandeur, pas un devis.
- « first training runs of probes » et « first runs of the ideation organism » décrivent des courses faites (registres), sans verdict revendiqué ; à retirer si le directeur préfère ne rien dire de leur état.
- Le banc à vérité plantée est « à faire » (N-076) : il est présenté comme livrable prévu, non comme acquis.

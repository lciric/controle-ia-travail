# Courriel à Thomas Romary (Mines Paris) : demande d'appui pour les crédits de recherche (version 1)

- Date : 2026-11-22T12:55Z (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5), pour Lazar, **qui l'envoie lui-même s'il le souhaite**. Rien n'est envoyé ; personne n'est contacté par cette session.
- Demande du directeur (22 novembre) : demander à Thomas Romary, son ancien tuteur aux Mines, s'il accepte d'appuyer la demande de crédits, par une courte lettre ou en étant nommé comme personne de référence.
- Ce que l'on sait de Thomas Romary vient du seul mot de Lazar (« Mines Paris, ancien tuteur aux Mines ») : aucune pièce déposée ne le nomme. Son titre, ses années de tutorat et son adresse restent entre crochets, à remplir par lui ou par Lazar.
- Pièce sœur : `champs-formulaire-anthropic-jet-4-v1.md` (question 4, et question 3 pour le champ du responsable d'« AI for Science »).

## 1. Courriel en français (248 mots)

**Objet** : `Demande d'appui pour une demande de crédits de recherche (sûreté de l'IA)`

Formule d'appel : vouvoiement par défaut ; « Thomas » si c'est votre usage avec lui.
```text
Bonjour [Monsieur Romary / Thomas],

J'espère que vous allez bien. Vous avez été mon tuteur aux Mines ; je suis aujourd'hui doctorant à NeuroSpin (CEA, Université Paris-Saclay), en partenariat avec l'ENS Paris-Saclay.

En parallèle de ma thèse, je mène depuis octobre un projet de recherche en sûreté de l'IA. La question : peut-on repérer un agent d'IA qui sabote une longue tâche par petites touches en lisant ses activations internes, et pas seulement son texte ? Je construis des agents de test sur des modèles ouverts, j'y plante le sabotage pour connaître la vérité, et je compare des sondes linéaires à des moniteurs qui ne lisent que le texte ; chaque expérience décisive est préenregistrée.

Je demande pour ce projet des crédits de calcul et d'accès aux modèles, d'abord à Anthropic, peut-être aussi à Amazon et à Google. Accepteriez-vous d'appuyer ma demande ? Au choix :
1. une courte lettre d'appui, de quelques lignes (je joins un modèle en anglais, à modifier ou à réécrire librement) ;
2. ou seulement être nommé comme personne de référence, que le programme pourrait contacter.

Cela ne vous engagerait à rien d'autre : vous ne seriez ni responsable ni encadrant du projet, et vous ne donneriez aucun accord au nom des Mines ou d'un autre établissement. Je ne citerai votre nom qu'avec votre accord.

Je peux vous envoyer un résumé du projet et mon CV. Et si ce n'est pas possible pour vous, je le comprendrai très bien.

Bien cordialement,
Lazar Ciric
```
Pièces à joindre si vous le souhaitez : le texte d'appui ci-dessous ; le CV v18 (`cv-v18/Lazar_Ciric_CV_2026-11-22_v18_universel.pdf`) ; un résumé, par exemple le champ 7 du jet 4.

## 2. Texte d'appui en anglais, qu'il pourrait signer (141 mots)

À modifier ou à réécrire librement par lui ; les crochets sont à remplir par lui. Le texte ne lui fait dire que ce qu'il peut attester (il a été le tuteur de Lazar ; il a lu un résumé du projet) et dit ce qu'il n'est pas (ni responsable, ni encadrant, ni signataire au nom d'un établissement).
```text
Letter of support for Lazar Ciric

I am [POSITION] at Mines Paris-PSL. I was Lazar Ciric's tutor at Mines Paris [YEARS].

Lazar is now a PhD student at NeuroSpin (CEA, Université Paris-Saclay). Alongside his PhD, he leads a new AI-safety project. He tests whether probes on an AI agent's internal activations catch sabotage spread thinly over a long task better than monitors that read only the agent's text. He plants the sabotage, so the ground truth is known, and preregisters each decisive experiment.

[ONE OR TWO SENTENCES IN YOUR OWN WORDS: what you know of his work, and why you support this application.]

I support his application for research credits. I am not the principal investigator or a supervisor of this project. This letter does not give consent on behalf of Mines Paris-PSL or any other institution.

[NAME], [EMAIL]
[DATE], [SIGNATURE]
```

## 3. Phrases pour les formulaires, après son accord écrit seulement

S'il accepte d'être **nommé comme référence** (20 mots) :
```text
Reference: Thomas Romary (Mines Paris-PSL), my former tutor at Mines Paris, has agreed to be contacted about this application: [EMAIL].
```
S'il **signe une lettre** (20 mots) :
```text
A short letter of support from Thomas Romary (Mines Paris-PSL), my former tutor at Mines Paris, is available on request.
```
Aucune de ces phrases n'est dans les liens préremplis ; les ajouter à la main.

## 4. Où son nom peut figurer, et où il ne le peut pas

Son appui est celui d'une **référence**. Ce n'est ni l'accord de l'employeur ou de l'établissement que le règlement d'« AI for Science » fait déclarer à Lazar (les Mines ne sont ni l'un ni l'autre aujourd'hui), ni l'approbation d'un responsable de projet.

| formulaire | champ | son nom ? | pourquoi |
|---|---|---|---|
| Anthropic, chercheurs externes | champ 11, « Additional Information » | **oui**, avec son accord | champ libre ; une phrase de référence ou de lettre suffit |
| Anthropic, chercheurs externes | champs 3 et 4 (recommandé par un employé d'Anthropic) | **non** | il n'est pas employé d'Anthropic |
| Anthropic, chercheurs externes | champ 6 (le demandeur ou l'équipe) | **non** | il n'est pas dans l'équipe |
| Anthropic, « AI for Science » | « Is there anything else… » (champ libre de la fin) | **oui**, avec son accord | même phrase que ci-dessus |
| Anthropic, « AI for Science » | « What is your PI's … email address? » | **non** | Anthropic écrit à cette adresse pour faire approuver le projet par son responsable ; il ne l'est pas |
| Anthropic, « AI for Science » | « Research team », profils de l'équipe | **non** | ces champs listent les membres qui emploieront Claude |
| Amazon | « Research Led By » | **non** (`Myself`) | `Faculty Member/PI` dirait qu'il dirige le projet |
| Amazon | « Project Proposal » | possible, sans gain net | aucun champ de référence ; « AWS employees contacted: none » reste vrai |
| Google | tous | **non** | une personne par proposition ; pas de champ de référence ; le lien d'inscription doit prouver l'inscription de Lazar, pas un appui |

## 5. Réserves

- Ne citer son nom qu'après un oui écrit, et seulement sous la forme qu'il a acceptée (référence ou lettre).
- Le courriel dit le projet mené « en parallèle de ma thèse », comme les formulaires du jet 4 ; si Lazar change cette formule (question 1 du jet 4), la changer ici aussi.
- Le courriel ne nomme pas les directeurs de thèse et ne dit rien de leur avis.

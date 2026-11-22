# CV v18 : ce qui change depuis la v17, et ce que Lazar vérifie

- Date : 2026-11-22 (`date -u`). Rédaction assistée (session fille, Claude Opus 5.5). Rien n'est envoyé.
- **Base : la v17, et non la v8** (mot du directeur du 22 novembre). Source : `brouillons/candidature-pivotal-v16/cv-v17/cv-U.html` au commit `be6ccd08a` (« CV v17, quatre variantes, deux pages »), lu par `git show be6ccd08a:<chemin>` ; sha256 du HTML `c87e9f09fc9e3e8dd2ecbc2438719d481dda3a7465fa51ba1592339b2602e948` ; PDF imprimé de la v17 au même commit : `Lazar_Ciric_CV_2026-11-02_v17_universel.pdf`, `6f40a9e170b8a1392779bbb0ee72cfac985ab8639a732c7aa6bbde6ae58554a5`.
- Seule la variante « universel » (`cv-U`) est reprise, comme la v9. Les trois autres variantes de la v17 (contrôle de la recherche automatisée, interprétabilité, persona et sycophancie) ne sont pas refaites : elles portent encore le théorème négatif et n'ont pas le doctorat.
- Fichiers : `Lazar_Ciric_CV_2026-11-22_v18_universel.html`, puis `Lazar_Ciric_CV_2026-11-22_v18_universel.pdf`, imprimé par Chromium au moyen de Playwright (`chromium.launch()`, `page.pdf({format: 'A4', printBackground: true, preferCSSPageSize: true})`, comme le script d'impression de la v17) ; producteur « Skia/PDF m157 », A4, deux pages, polices DejaVu incorporées. Le script d'impression est resté dans le bloc-notes de la session.
- La v9 (`cv-v9/`, partie de la v8) reste telle quelle ; la v18 la remplace.

## Changements

1. **Doctorat ajouté, avec le titre de thèse**, en trois endroits :
   - bandeau, première ligne : « PhD: NeuroSpin (CEA, Université Paris-Saclay), with ENS Paris-Saclay, since September 2023 — brain networks for mathematics (ERC MathBrain project); the AI-safety work below runs alongside it. » ;
   - section « Doctoral Research — NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay » : « PhD student, September 2023 – ongoing » ; « Thesis: **Methods to study brain networks involved in mathematics and their educational and genetic correlates** · within the ERC-funded MathBrain project · Supervisors: Stanislas Dehaene and Cathy Philippe » ;
   - première ligne de « Education » : « NeuroSpin (CEA, Université Paris-Saclay), in partnership with ENS Paris-Saclay — PhD student since September 2023 (thesis above) ».
   - **Source du titre** : le sujet de thèse déposé par Lazar (`1206eb24-Sujet_these_BIGMath_Lazar_Ciric.docx`, sha256 `93e29a64e3ffd5bf…`, premier paragraphe sous « PhD project »), identique p. 85 du dossier de candidature (`ba73a979-candidature_169844.pdf`, `143154cf74ffc7d7…`). Cadre : « As part of the ERC-funded MathBrain project, Stanislas Dehaene (Neurospin, UNICOG)… » (même sujet).
   - **École doctorale : non écrite.** Aucune pièce ne la nomme dans son contenu ; seul le nom de fichier « DOSSIER_EOBE » la suggère. À ajouter d'après l'attestation d'inscription (par exemple à la fin de la ligne « sub » de la section du doctorat).
   - **Différence avec la v9** : la v9 écrivait « Monitoring AI agents is part of the thesis » et « AI control programme, part of my PhD ». Le sujet déposé ne dit rien du contrôle des agents d'IA ; la v18 écrit donc « runs alongside it » et « AI control programme, alongside my PhD ». À trancher par Lazar (question 1 de `../champs-formulaire-anthropic-jet-4-v1.md`).
2. **Théorème négatif retiré.**
   - Bandeau, « Results » : « a negative theorem on what per-action monitors cannot see against a threat spread over many actions or agents, checked in preregistered simulations » supprimé.
   - Projet « White-Box Control of Diffuse Threats » : la puce « Against a threat spread over many actions or many agents, every permutation-invariant monitor statistic is blind. An additivity lemma and a negative theorem by invariance… confirmed all 31 predictions… » est remplacée par la puce de la v9, mot pour mot : « **A known additivity lemma from nuclear material accounting, applied to AI control.** Original statement (Avenhaus & Jaech, "On subdividing material balances in time and/or space", Journal of the INMM 10(3), 1981, p. 25 and Theorem 1, p. 30)… » ; loi en racine carrée citée à ses auteurs (Ker 2007 ; Ker, Pevný, Kodovský et Fridrich 2008) ; question empirique gardée (GO-2026-11-22-24) ; résultat de simulation sur les seuils de type Ville (21–35 % de fausses alertes) gardé. Source de l'énoncé : PDF lu par la session de la v9 (`docs/sources/steganographie-comptabilite-v1/jnmm-vol10-no3-1981-avenhaus-jaech-subdividing-material-balances.pdf`, `051e44a1b6c269f0…`).
   - Sous-titre du projet : « theory, preregistered simulations and tooling » devient « alongside my PhD; preregistered simulations and tooling ».
   - Vérifié par programme sur le texte du PDF : « negative theorem », « 31 predictions », « permutation-invariant » n'y figurent plus.
3. **Mise en page** : pour tenir en deux pages avec la section du doctorat, police de 7,3 à 7,2 points, interligne de 1,15 à 1,12, marges haute et basse de 8 à 6,5 mm. Rien d'autre n'est coupé.
4. Tout le reste est celui de la v17, mot pour mot (bloc « Built », résultats du saboteur, projets, stages, formation, compétences).

## À vérifier par Lazar avant tout envoi

1. **« alongside my PhD » ou « part of my PhD »** : voir le changement 1. Ne remettre « part of » qu'avec une pièce qui le dit et l'accord des directeurs.
2. **« Swarm monitoring, tested where the model had never been computed »** (projet de contrôle) : gardé tel quel de la v17. Ce n'est ni le lemme ni le théorème, mais « the model » et « the surrogate » peuvent renvoyer à la théorie de la surveillance en essaim que la v17 présentait avec le théorème (« one theory serves sequential and swarm monitoring », retiré) ; à reformuler si tu veux qu'aucune trace de cette théorie ne reste.
3. **Prépublication** : la v17 écrit « Manuscript in preparation » pour la loi de sycophancie ; les formulaires (jets 3 et 4) écrivent « preprint, code and data public ». Garder la formule juste partout.
4. **Chevauchements de dates avec la thèse** (inchangés, faits à toi) : « Independent Research Programme — AI Safety · 2025 (alongside my consulting role) – 2026 (full time since March) » ; « AI Lead Consultant — EPSA Innovation, 2024 – 2026 » ; « Looking for: … available full time ». À côté d'un doctorat commencé en septembre 2023, un relecteur peut y voir une contradiction.
5. **« Visiting Researcher — NeuroSpin (CEA Saclay), director Stanislas Dehaene, 2023 … within the ERC MathBrain project »** : début de la thèse, ou séjour avant septembre 2023 ? Si c'est la même chose, fondre la ligne dans la section du doctorat.
6. **Écarts entre le dossier de candidature de 2023 et le CV** (le dossier, pièce de Lazar, p. 1 et 2 ; le CV n'est pas changé sur ces points) :

| élément | dossier de 2023 | CV v17 et v18 |
|---|---|---|
| Mines Paris | « From September 2019 to June 2023 Master's degree in Science and Executive Engineering… Major in Geostatistics and Applied Probabilities » | « Ingénieur Civil, Mathematical Statistics, Machine Learning & Applied Probabilities (2025) » |
| ENS (Ulm), M2 | « From September 2018 to September 2019 MSc in Computational and Cognitive Neuroscience… High Honors » | « M2 Research, Computational Neuroscience (Cogmaster), 2020 — mention Bien » |
| Mémoire de M2, laboratoire de Srdjan Ostojic | « From March 2019 to August 2019 » | « 2019 – 2020 » |
| IBM Research Zurich | « From July 2020 to December 2020 » ; lettre d'Abu Sebastian : « the second half of 2020 for a duration of 6 months » | « 2020 – 2021 » |
| Lawrence Berkeley National Laboratory | « From April 2017 to July 2018 » | « 2017 – 2019 » |
| Classes préparatoires | « LYCEE MARCELIN BERTHELOT, From September 2013 to July 2015 » | « Lycée Louis-le-Grand — MPSI / PSI*, Classes Préparatoires (2014–2016) » |
| ENS Paris-Saclay | licence 2015-2016, M1 2016-2017 ; statut de normalien rémunéré « for the period 2015 to 2020 » | « Normalien, Fundamental Physics (2016–2020) » |

   Certains écarts peuvent s'expliquer (diplôme délivré plus tard que la fin des cours, stage prolongé) ; d'autres non (le lycée). Un relecteur qui verrait les deux documents les remarquerait.

# LISEZMOI — corpus primaire v5 « intégral »

Date : 29 octobre 2026. Produit par un sous-agent d'extraction, sur décision de Lazar (directeur) du 29 octobre 2026 (R-439).

**Dépôt privé seulement : texte intégral, aucun retrait, contenu d'attaque verbatim possible. Ce dossier ne va jamais dans la copie expurgée publique.**

## 1. Ce que c'est

Le texte complet, sans retrait ni retouche éditoriale, des papiers servis en extraits dans les corpus primaires v1 à v4 (23 papiers cités par les tableaux des LISEZMOI de `corpus-primaire-v1` à `corpus-primaire-v4`). Un fichier `integral-<identifiant><version>.md` par papier : en-tête (identifiant, titre tel qu'écrit dans le PDF, empreinte du PDF, outil, nombre de pages, nombre de caractères, mention de sûreté), puis, page par page, le marqueur `[p.N]` (N = numéro de page du PDF) suivi du texte de la page, références et annexes comprises.

Outil d'extraction : `pdftotext -layout -enc UTF-8` (pdftotext version 24.02.0, Poppler), une page à la fois (`-f N -l N`) ; `pypdf` non utilisé. Le sceau de chaque PDF (`.sha256`) a été vérifié par `sha256sum -c` avant toute lecture (dix sur dix : OK, 29 octobre 2026). Le nombre de pages est celui de `pdfinfo`.

Seules deux transformations touchent le texte brut de l'outil : (a) le marqueur `[p.N]` ajouté ; (b) les caractères de contrôle produits par l'extraction (glyphes de polices sans correspondance : délimiteurs de formules, texte de figures à police codée) : les caractères nuls supprimés, les autres remplacés par le caractère de remplacement U+FFFD (position gardée). Le nombre et les pages concernées sont dans l'en-tête de chaque fichier. Aucune coupe, aucun rejointement de lignes, aucune correction.

## 2. Règle de sûreté modifiée (R-439)

Décision de Lazar du 29 octobre 2026 (`registres/decisions.md`, R-439) : le corpus d'idéation sert le texte intégral sans retrait aux proposeurs et aux juges, textes d'attaque compris ; la garde de sûreté des extraits est levée pour ce corpus seulement. La garde est maintenue sur tout le reste (internes des moniteurs, carte des hypothèses, mode tenu à l'écart, banques, textes d'actions, consignes de P3, `donnees/`). Ce corpus et ses dérivés sont exclus de la copie expurgée publique. Aucun papier n'a été refusé à l'extraction par l'agent.

## 3. Règle de provenance inchangée (R7)

Un texte intégral n'est pas une vérification. Tout chiffre repris dans un préenregistrement ou un papier doit citer la page `[p.N]` et être relu sur le PDF empreinté. L'extraction en mode mise en page peut mal ordonner formules, tableaux et figures : se reporter au PDF pour tout symbole ou tout chiffre de tableau.

## 4. Les 23 papiers

| Identifiant (version du PDF) | Titre (tel qu'écrit dans le PDF, ou dans l'extrait pour les PDF absents) | Pages | Caractères (fichier intégral) | Empreinte SHA-256 du PDF | Empreinte SHA-256 du fichier intégral | État |
|---|---|---|---|---|---|---|
| arXiv:2412.09565v2 | Obfuscated Activations Bypass LLM Latent-Space Defenses | 51 | 191 970 | `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` | `3d277d68ad7462f4cf8dc009cb5793e0831e7b123c59489e963ae21da8b0b62e` | extrait |
| arXiv:2510.09462v2 | Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols | 52 | 212 174 | `96c16e33b27b9633b324acecfe29e1bfa9de7052143fb854824aad70a649d7f7` | `5cc0c2ef9bd09501ce75315624b2e46d7ccd2b97056231dc6918c384b57d679b` | extrait |
| arXiv:2601.20022v2 | Quickest Change Detection in Discrete-Time in Presence of a Covert Adversary | 34 | 206 663 | `8d090f3171ef76cad597ab263a2de9df49de1d1accf78a8afff55ceb82881b42` | `546dd40dbf8438a56913aa8fa0eb88232cf16a3de853fb92ebce5526e2380116` | extrait |
| arXiv:2602.14161v2 | When Benchmarks Lie: Evaluating Malicious Prompt Classifiers Under True Distribution Shift | 27 | 92 210 | `7831c848841eca32bcbb1e18cd35f644cfe5a8af8f0f003623c4e1bdd6e03c00` | `7c72771e832b481f8c7f6c91d663c7ea08b2a1be84d657861774061a36e986c7` | extrait |
| arXiv:2605.09684v1 | MonitoringBench: Semi-Automated Red-Teaming for Agent Monitoring | 63 | 200 039 | `35bb09b49f85578e4cfddeec16c9ae101a51b5d618196a4b29a1722b89b831f5` | `681cab7625539b4dac10d1eb12e82d61d23ac612883451bc911cc52dc87d695b` | extrait |
| arXiv:2605.16626v2 | SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors | 42 | 196 618 | `1ba418227095eeea98881f61a606c9974f4f3a8758d6a6292c6a9cd8bbd76751` | `263968ac06222ffa1707af8bbc30e59aa1b3590736a9b5eb49bd721781f1b70a` | extrait |
| arXiv:2606.08892v2 | Diffuse AI Control on Fuzzy Tasks | 71 | 294 995 | `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` | `5872d2636ab166cf716c57937888d38f9930c3c14aea74ae472011499485ee2e` | extrait |
| arXiv:2607.02514v2 | Distributed Attacks in Persistent-State AI Control | 35 | 122 074 | `9baceea4719a5ff2d63c3278d425a0c3b9feeb2d447a19a3cd7a6b62d3339c22` | `7e1140835425a9ba9b63f1bc47accf10457df145707aeb4ba75687770d668323` | extrait |
| arXiv:2607.07368v1 | Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors | 81 | 349 980 | `d72cae4337e824e4af9eb84759775f6c5dc704f157a0d302df1b44538eb159cd` | `1816a5b91b2ad0ed021d790160a83449403341db93f5a62ecaa2927bc2b3f94f` | extrait |
| arXiv:2610.12445v1 | Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception | 98 | 448 101 | `7e1417580c4ee269c9b7d6b5e9acd6a4027e820a34710e381a946fe7b5e3e11a` | `425afd4ec0084922b035b8703c909b3f01e9dde161e2366fcc9d23275a0aaedb` | extrait |
| arXiv:2603.00829v2 | Constitutional Black-Box Monitoring for Scheming in LLM Agents | — | — | `d8ffcbd352abd9c6bd9aeb1ded6d337689ae980980960fdd8de12bd3d1fd775d` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2603.19461v1 | HyperAgents (DGM-Hyperagents : agents auto-référentiels qui améliorent leur propre procédure d'amélioration) | — | — | `92f9a73b43699c08c6000f7d4f1b68bec9fd872d217467fe4a1127e2f7981f1e` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2605.13411v1 | EvoSafety: Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution | — | — | `a81514c51c33b6f8def74bb6df11c5f733cfe256bbc21768f607a3dc0e0029c0` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2605.31140v1 | EvoDefense: Co-Evolving Black-Box Defense with Large Language Models | — | — | `29c8ffd960d8ece9df75eb95329afc23509729e904819dbafb5d90d24305367a` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2609.17560v1 | Pay Only for Disagreement: Certified No-Regression Verdicts for Model Updates with Matching Label-Complexity Bounds | — | — | `ef318a961de7d5f237b7bdca063b7441d3cab00522bc0e6baec383603af2d11f` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2609.32267v1 | When Can Old Evaluations Certify a New Model? Label-Efficient Release Decisions under Evaluator Drift | — | — | `8654e1185de1b3160eb4d30d50d5bcf428e41e5439f868fad58ef1849bf1a118` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2609.36580v2 | SafeCoEvo: Co-Evolving Safety Harnesses and Guards for LLM Agents at Test-Time | — | — | `e0df2463da8c5a9aaaa819d79f08606618f3318823a0cc78f9ecbcf940a05d3a` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2610.19422v1 | AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety | — | — | `4812c7037c4c4363f4fe7ebbcf027e2f286341446dbd503e20bd8a4b72715bac` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2509.17778v1 | Quickest Change Detection in Continuous-Time in Presence of a Covert Adversary | — | — | `97d000252b768e69113437cce1a88a24488cbe3f92a1a724ea39c0c9f87d8d5e` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2511.17408v4 | The Impact of Off-Policy Training Data on Probe Generalisation | — | — | `91e00c25f356db80a0073d32d7d774e71b64de13767983d85ec4bb0fcadb2357` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2601.19726v1 | RvB: Automating AI System Hardening via Iterative Red-Blue Games | — | — | `53a465a479fc1887e724b424a749910eb09251be49c966a5a639c65d890e7e44` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2602.01539v2 | MAGIC: A Co-Evolving Attacker–Defender Adversarial Game for Robust LLM Safety | — | — | `793d32725d82e364f0ecbb0be994694d2aca20f8daf8391e6583be58f067540e` (citée par l'extrait, non vérifiable ici) | — | PDF absent |
| arXiv:2606.08106v1 | PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents | — | — | `779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f` (citée par l'extrait, non vérifiable ici) | — | PDF absent |

Bilan : **10 extraits, 0 refusé, 13 PDF absents**.

Les 13 PDF absents sont les huit papiers du corpus v2, les quatre du corpus v3 et celui du corpus v4. Pour chacun, `docs/sources/pdf/<identifiant><version>.pdf` et son `.sha256` n'existent pas dans cette copie de travail (recherche par nom sur tout le système de fichiers, hors `donnees/` : rien). Les extraits citent l'empreinte de chaque PDF (colonne ci-dessus) ; deux d'entre eux (2603.19461, 2605.13411) précisent « branche main, non lue ici ». Aucun texte intégral n'a été reconstitué à partir des extraits ; leurs extraits v2 à v4 restent dans la liste blanche v6 telle quelle (section 6). L'extraction intégrale de ces 13 papiers est à refaire quand leurs PDF seront présents et leurs sceaux vérifiés.

## 5. Total de caractères et différence avec les extraits v1 à v4

Caractères = caractères du fichier lu en utf-8 (en-tête compris), avant le caviardage de la course.

- Total des 10 fichiers intégraux : **2 314 824** caractères (texte seul, hors en-têtes : 2 300 788).
- Total des 10 extraits v1 à v4 qu'ils remplacent : **245 378** caractères.
- Caractères gardés en plus : **2 069 446** (environ ×9.4).

| Papier | Extrait v1 à v4 (caractères du fichier) | Fichier intégral | Gardés en plus |
|---|---|---|---|
| arXiv:2412.09565v2 | 24 098 | 191 970 | 167 872 |
| arXiv:2510.09462v2 | 24 747 | 212 174 | 187 427 |
| arXiv:2601.20022v2 | 23 840 | 206 663 | 182 823 |
| arXiv:2602.14161v2 | 24 567 | 92 210 | 67 643 |
| arXiv:2605.09684v1 | 24 551 | 200 039 | 175 488 |
| arXiv:2605.16626v2 | 24 333 | 196 618 | 172 285 |
| arXiv:2606.08892v2 | 24 667 | 294 995 | 270 328 |
| arXiv:2607.02514v2 | 24 941 | 122 074 | 97 133 |
| arXiv:2607.07368v1 | 24 742 | 349 980 | 325 238 |
| arXiv:2610.12445v1 | 24 892 | 448 101 | 423 209 |
| **Total (10)** | **245 378** | **2 314 824** | **2 069 446** |

## 6. Liste blanche v6 et tailles

- `liste-blanche-v6.txt` : les 40 fichiers de la liste blanche v5 (`ideation-organisme-approches-v1/liste-blanche-sans-temoins-v5.json`, 40 entrées ; le fichier existe en `.json`, pas en `.txt`), les dix extraits v1 à v4 remplacés étant substitués par leur fichier intégral, à la même place. Les treize extraits dont le PDF est absent restent dans la liste. 40 fichiers au total. Un chemin absolu par ligne.
- `tailles-v6.txt` : caractères par fichier et total. Total de la liste v5 : 743 537 ; total de la liste v6 : **2 812 983**.
- Les plafonds de la course (`--taille-max-pieces`, 750 000 par lot ; plafond dur 800 000) sont dépassés par la liste v6 prise d'un seul lot (le dépassement vaut aussi pour le seul total des dix fichiers intégraux, 2 314 824). Aucune décision n'est prise ici : le total est donné.
- La liste v6 est une liste de fichiers à lire ; elle n'est pas un document scellé de liste blanche de la course (la liste v5 est un `.json` empreinte-par-chemin, que ce dossier ne modifie pas).

## 7. Doutes de l'extraction (aucun jugement sur le contenu)

- Pages sans texte extractible (figures en image, pas de reconnaissance de caractères) : 2605.09684v1 p.34 et p.35 (figures 14 à 17, images seules, légendes extraites). Le texte contenu dans les images de figures n'est extrait pour aucun papier. 2610.12445v1 p.61 : page courte (moins de 200 caractères), texte présent.
- Polices de figures codées : 2510.09462v2, pages 2, 5, 6, 7, 18 et 22 (2 975 caractères de contrôle ; le texte de figure y est illisible, noyé dans des caractères de remplacement ; l'outil y émettait en outre des sauts de page parasites, d'où l'extraction page par page, qui donne 52 pages comme `pdfinfo`).
- Délimiteurs de formules sans correspondance (remplacés par U+FFFD) : 2601.20022v2 (23 pages concernées, 298 caractères) ; 2607.07368v1 (pages 45, 61, 62, 64, 65, 66) ; 2610.12445v1 (p.17) ; 2606.08892v2 (p.14) ; 2605.09684v1 (p.22) ; 2602.14161v2 (p.5). Les formules sont extraites en texte linéaire, parfois dans le désordre.
- Mise en page : une seule colonne dans les dix papiers (pas d'entrelacement de colonnes constaté à l'échantillon) ; le mode `-layout` garde des indentations larges et des trous dans les tableaux, ce qui gonfle le nombre de caractères. Les titres en petites capitales sortent espacés (« W HEN B ENCHMARKS L IE ») dans 2602.14161v2 et 2510.09462v2 ; le titre de l'en-tête est celui des LISEZMOI v1, retrouvé dans la page 1 à l'espacement près.
- 2607.07368v1 : les rapports le citent sous le nom de Makins et al. ; premier auteur du PDF : Angelini (reprise du LISEZMOI v1). Pour 2610.12445v1, `pdftotext` signale « Mismatch between font type and embedded font file » (avertissement de police, texte extrait).
- Aucun PDF scanné parmi les dix.
- Les 13 PDF absents (section 4).

## 8. Fichiers du dossier

`integral-<identifiant><version>.md` (dix) ; `liste-blanche-v6.txt` ; `tailles-v6.txt` ; ce `LISEZMOI-v1.md` ; chaque fichier a son empreinte compagnon `.sha256` (R6).

# Lecture des cinq voisins de second rang du constat CP-02 et du résumé de la version publiée de Kumaran et al. (constat CP-01), et jugement de collision avec HC1, HC2 et HC3 — lentille « voisins » (verrou de R8) — v1

- **Qui** : lecteur neuf, sous-agent de la session 16. Je n'ai écrit ni le brouillon 5 du papier C, ni les brouillons
  précédents, ni aucune contre-lecture ou note de voisins.
- **Heures** : du 2026-10-20 vers 23:58 au 2026-10-21 vers 00:22 UTC.
- **Mission** : `…/papier-C/consigne-voisins-cp02-v1.md`
  (`7de50f46710dd2182af98e384af59c80198c14e6a43dbdceb7dcfbf8b46ab2c7`, égale au compagnon), lue en entier. Forme de la
  note et verdicts possibles : `…/papier-C/consignes-contre-lectures-brouillon5-v1.md`
  (`148299974a2a39251f2d3334677abaee0380b82043a19a4ab7d8f9d60cb907ac`), sections « Commun aux trois » et « Lentille 3 ».
  Ce fichier n'a **pas de compagnon** `.sha256` ; son empreinte est celle que citent les trois notes voisines.
- **Préfixe** : `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` =
  `/home/user/controle-ia-travail` (lecture seule). Chemins relatifs de cette note : à partir de
  `…/contre-lectures-brouillon5/voisins-cp02/`.
- **Pages** : rang de la page dans le fichier PDF (égal au numéro imprimé quand il y en a un : ChatInject, Wu et al.).
  Texte de `pdftotext -raw`, une page à la fois (`texte/<identifiant>-pages/`), et `pdftotext -layout` pour le document
  entier (`texte/<identifiant>.layout.txt`).

## Les cinq papiers et CP-01 : identifiant, version, niveau de lecture, verdict

| papier | identifiant et version lue ; historique | cité par (CP-02) | niveau de lecture | verdict |
|---|---|---|---|---|
| Yilin Geng, Haonan Li, Honglin Mu, Xudong Han, Timothy Baldwin, Omri Abend, Eduard Hovy, Lea Frermann, « Control Illusion: The Failure of Instruction Hierarchies in Large Language Models » | 2502.15851v4 ; v1 du 21 février 2025, v2 du 2 août, v3 du 24 août, v4 du 4 décembre 2025 ; commentaire arXiv « Accepted to AAAI-26 Main Technical Track Proceedings » ; pied de page p. 1 : « Copyright © 2026, Association for the Advancement of Artificial Intelligence » | Zeng, p. 1 et p. 6 (« [6] ») ; Zeng, p. 2 : son jeu de données étend celui de Geng et al. | résumé ; PDF lu en entier (12 p.) | **pas de collision** |
| Hwan Chang, Yonghyun Jun, Hwanhee Lee, « ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents » | 2509.22830v3 ; v1 du 26 septembre 2025, v2 du 30 janvier 2026, v3 du 13 avril 2026 ; commentaire arXiv « ICLR 2026 » ; en-tête p. 1 : « Published as a conference paper at ICLR 2026 » | Pan et al., p. 2 et p. 10 | résumé ; PDF lu en entier (28 p., annexes comprises) | **pas de collision** |
| Fengqing Jiang, Zhangchen Xu, Luyao Niu, Bill Yuchen Lin, Radha Poovendran, « ChatBug: A Common Vulnerability of Aligned LLMs Induced by Chat Templates » | 2406.12935v2 ; v1 du 17 juin 2024, v2 du 7 janvier 2025 ; commentaire arXiv « This paper is accepted to AAAI 2025 » | Pan et al., p. 2 et p. 10 (sans identifiant arXiv ; trouvé par l'interface de recherche d'arXiv) | résumé ; PDF lu en entier (12 p.) | **pas de collision** |
| Xikang Yang, Xuehai Tang, Jizhong Han, Songlin Hu, « The Dark Side of Trust: Authority Citation-Driven Jailbreak Attacks on Large Language Models » | 2411.11407v1 ; v1 seule, du 18 novembre 2024 ; aucun lieu de publication indiqué | Khan et al., p. 9 et p. 14 | résumé ; PDF lu en entier (18 p.) | **pas de collision** |
| Addison J. Wu, Ryan Liu, Kerem Oktar, Theodore R. Sumers, Thomas L. Griffiths, « Are Large Language Models Sensitive to the Motives Behind Communication? » | 2510.19687v2 ; v1 du 22 octobre 2025, v2 du 1er février 2026 ; commentaire arXiv « NeurIPS 2025 » ; pied de page p. 1 : « 39th Conference on Neural Information Processing Systems (NeurIPS 2025). » | Robinson et al., p. 3 et p. 11 (sans identifiant arXiv ; trouvé par l'interface de recherche d'arXiv) | résumé ; PDF : corps lu en entier (p. 1 à 10) ; annexes A à C (p. 18 à 33) parcourues par mots clés, p. 24, 26, 29, 30 et 33 lues ; liste de contrôle NeurIPS (p. 34 à 40) non lue | **pas de collision** |
| Kumaran, Fleming, Markeeva, Heyward, Banino, Mathur, Pascanu, Osindero, De Martino, Veličković, Patraucean, « Competing Biases underlie Overconfidence and Underconfidence in LLMs », Nature Machine Intelligence, 8(4), 614–627, doi 10.1038/s42256-026-01217-9 (CP-01) | version publiée : reçue le 2 juillet 2025, publiée le 22 avril 2026, accès libre (métadonnées de la page) ; préimpression 2507.03120v1, toujours seule version arXiv à 00:04 UTC | Panin, p. 15 | **résumé seul**, sur la page de l'éditeur (borne de la consigne) ; corps non lu | **pas de collision au niveau du résumé** |

Identification par l'interface de recherche d'arXiv : titre « ChatBug », une seule réponse, 2406.12935 ; titre « motives
behind communication », une seule réponse, 2510.19687. Les deux sont sur arXiv : l'anthologie et les actes n'ont pas été
consultés. Les cinq entrées bibliographiques ont été relues sur les PDF citants, empreintés par la note de Panin (Pan
et al. `2371fa59…`, p. 10 ; Zeng `846e40d0…`, p. 6 ; Khan et al. `b3ff5385…`, p. 14 ; Robinson et al. `7bef1c8f…`,
p. 11 ; contrôle par script, plus bas).

## Téléchargements

Téléchargés le 2026-10-20 à 23:59 UTC (pages de résumé arXiv, recherches) et le 2026-10-21 entre 00:00 et 00:04 UTC
(PDF, page de l'éditeur, page de résumé de 2507.03120), réponse 200 sauf mention, copiés sans modification, chacun seul
dans son dossier. Chaque PDF a son compagnon `.sha256`. Toutes les empreintes sont dans `sha256sums-voisins-cp02-v1.txt`.

| fichier | empreinte sha256 | contenu |
|---|---|---|
| `pdf/2502.15851v4/2502.15851v4.pdf` | `2cdfb7d428a18bafbbab27d4891d9356dbf820d3edd345f453842488b5f15640` | Geng et al., 12 p. |
| `pdf/2509.22830v3/2509.22830v3.pdf` | `5663314dea6dbc4e91f801b5bb29b0564f45cdc87b54bc2c6f7f242442e4f76a` | ChatInject, 28 p. |
| `pdf/2406.12935v2/2406.12935v2.pdf` | `fa442e14b8c40e9368f42dd089b7afab91ecf90b1f317df1ccbc8c5ee45087f4` | ChatBug, 12 p. |
| `pdf/2411.11407v1/2411.11407v1.pdf` | `886bf15cadd303261475a10a89b97ae8170f132c4e94e2d9db34ec290ba6d4d4` | Yang et al., 18 p. |
| `pdf/2510.19687v2/2510.19687v2.pdf` | `4d2f8c669e4cc95fb148a057505f46ffb7f9c772d27e1e9e4a2804ea04510534` | Wu et al., 40 p. |
| `telechargement/abs-2502.15851/abs-2502.15851.html` | `6063e1c3cb771bdaefc8b34e064e0343dd44c8639ebc3b828019b8aeff5f9585` | page de résumé arXiv |
| `telechargement/abs-2509.22830/abs-2509.22830.html` | `53757f6040cbc41568643fcf55d8a854dcbb91ba7a8e53b64dd77825033b082c` | page de résumé arXiv |
| `telechargement/abs-2406.12935/abs-2406.12935.html` | `51fea5a3e3fbbde68bd54f3ed33b0528bff0fc79304d228ad350ee1529d82643` | page de résumé arXiv |
| `telechargement/abs-2411.11407/abs-2411.11407.html` | `9b5becc311b1091e816d6e0bd674a0ae5df2e3365aa88315e24cd2e7bcd6bd13` | page de résumé arXiv |
| `telechargement/abs-2510.19687/abs-2510.19687.html` | `dfaff08f7208c47765d308cff9eaf088b470a7f7d86649dca9291b0df28af237` | page de résumé arXiv |
| `telechargement/abs-2507.03120/abs-2507.03120.html` | `1f76623b9ed7bfdfcbe45435eb0be2d06fa052ae8e86db5366633be470a90632` | page de résumé arXiv de la préimpression de Kumaran et al., relevée à 00:04 UTC ; octet pour octet égale à celle de la note de Panin |
| `telechargement/api-chatbug/api-recherche-chatbug.xml` | `3e56f4bdee96f816f4cbfda6545204a55980b12b547f5d1a071cfcd03e8e1360` | recherche arXiv, titre « ChatBug » |
| `telechargement/api-wu-motives/api-recherche-wu-motives.xml` | `9b92ca7d9ed68f34fba92c63fd0347279f270f8fa09592a0422eb953a4aa58a0` | recherche arXiv, titre « motives behind communication » |
| `telechargement/nmi-s42256-026-01217-9/page-resume-s42256-026-01217-9.html` | `dc9b4d151c92806167d1b4f230201c05e72a44690ce4c52e25ee7af9c1c31dac` | première requête à la page de l'éditeur : réponse 303 vers le serveur d'autorisation (non suivie) |
| `telechargement/nmi-s42256-026-01217-9/page-resume-s42256-026-01217-9-sans-temoin.html` | `fa5dfe4a30174a8fd8eea63700de9867cb5ce8b0efbfe738893dd7a9bd2266fc` | page de l'éditeur, réponse 200 ; résumé et métadonnées seuls extraits |

## Pièces lues (empreintes vérifiées)

| pièce | empreinte | lecture |
|---|---|---|
| consigne de cette lecture | `7de50f46…` (égale au compagnon) | en entier |
| consignes communes | `14829997…` (sans compagnon) | « Commun aux trois », « Lentille 3 » |
| note des sept voisins de Panin, `…/contre-lectures-brouillon5/voisins-panin/lecture-voisins-panin-sept-v1.md` | `b3a6c18732013f1faf388bc051b62d3c83dd8dfb8c3e70363eddf0d9d77d8929` (égale au compagnon) | en entier ; CP-01 et CP-02 surtout |
| note des neuf voisins de second rang, `…/voisins-second-rang/lecture-voisins-second-rang-v1.md` | `8027bd53f6030d1b289c5ad84c3b501a8c646e22a72f31be6e30a2912a56f81f` (égale au compagnon) | en entier (forme ; aucun des cinq n'y est lu) |
| note de Joswin et Hu et Qu, `…/voisins/lecture-voisins-joswin-huqu-v1.md` | `55222cdb3278f59810586b2097817114c74825cc34b9dd7a12ad2a051a90b84d` (égale au compagnon) | en entier |
| brouillon 5 : `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` ; même fichier sous `…/brouillon5/` | `9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969` (égale aux deux compagnons) | l. 60 à 129, 215 à 349, 355 à 463, 676 à 700, 750 à 764, 900 à 942 ; recherche de mots (« usurpation », « famille 4 », « ordres en bande ») |
| configuration `…/brouillon5/papier-C-config-v1-brouillon2.json` | `77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb` (égale au compagnon) | champs `vivier.usurpation_stylistique`, `vivier.ordres_en_bande`, `gardes_lexicales`, `insertion` seulement (pour juger la proximité des gabarits forgés) |
| `R/docs/decisions/decision-N-005-N-006-v1.md`, `decision-N-013-v1.md`, `decision-N-023-v1.md` | `cd49afbc…`, `157d388e…`, `1297f509…` (égales aux compagnons) | énoncés tels que le brouillon 5 les reprend (l. 226 à 272) ; N-013, section 2 (HC3), lue en entier |
| PDF citants, sous `…/voisins-panin/pdf/` | `2371fa59…` (Pan et al.), `846e40d0…` (Zeng), `b3ff5385…` (Khan et al.), `7bef1c8f…` (Robinson et al.) : égales au manifeste de la note de Panin (`sha256sums-voisins-panin-v1.txt`) | pages des entrées bibliographiques ; Zeng p. 1 et p. 2 |
| page de résumé de 2507.03120, `…/voisins-panin/telechargement/abs-2507.03120.html` | `1f76623b…` (égale au manifeste de la note de Panin) | résumé de la préimpression |
| `R/docs/etat-de-l-art-controle-ia-v1.md` | `a7d6846d…` | l. 134 à 142 (« Séparation contrôle/données », « Détection d'injection par états internes ») |
| `R/docs/programme-controle-ia-v2.md` | `2fd63bad…` | l. 105, 165, 194, 196, par recherche |

Recherche par identifiant et par titre (sans lecture), dans des fichiers nommés un à un, sans recherche récursive :
brouillon 5 (`9d55160f…`), `R/registres/veille.md` (`bd1e34ce…`), `R/docs/etat-de-l-art-controle-ia-v1.md`
(`a7d6846d…`), `R/docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` (`b0b519fe…`) et `-niveau2-v1.md`
(`bbe0c1f5…`), `R/docs/programme-controle-ia-v2.md` (`2fd63bad…`), les trois décisions ci-dessus,
`R/docs/notes/confrontation-projet-sycophancie-v1.md` (`b7631607…`). Motifs : les cinq identifiants, « Control
illusion », « ChatInject », « ChatBug », « DarkCite », « dark side of trust », « motives behind », « motivational
vigilance », et pour le troisième rang 2403.14720, « spotlight », « Hines », 2403.06833, « Zverev », 2404.13208,
« instruction hierarchy », « StruQ », « chat template », « gabarit de conversation », « jeton spécial ». Résultat : aucun
des cinq n'y figure. Au troisième rang, seuls la hiérarchie d'instructions de Wallace et al. et le « spotlighting »
figurent à l'état de l'art v1 (l. 138, « Séparation contrôle/données », conclusion : « Couvre les ordres en bande de
HC3 ») ; Zverev et al. (2403.06833) n'est dans aucun des fichiers cherchés.

## Ce que j'ai tenu

- Écriture seulement sous `…/contre-lectures-brouillon5/voisins-cp02/`. Aucune commande git. `python3 -I -B`,
  `PYTHONDONTWRITEBYTECODE=1`, scripts hors des dossiers de téléchargement, chemins passés en arguments. Aucune recherche
  récursive dans le dépôt. Aucun sous-agent, aucune dépense, aucun outil de location, aucune clé affichée.
- Jamais ouverts, pas même pour une empreinte : `R/prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, tout fichier sous `R/donnees/`, `R/runs/`, `R/diag/`.
- Réseau : `export.arxiv.org` (six pages de résumé, dont la relecture de 2507.03120 ; deux recherches), `arxiv.org`
  (cinq PDF), `www.nature.com` (deux requêtes sur la seule page de l'article). **Écart déclaré, à juger par la session** :
  la première requête à la page de l'éditeur a reçu une réponse 303 vers `idp.nature.com/authorize` (serveur
  d'autorisation de l'éditeur) ; je ne l'ai pas suivie (aucun témoin de connexion, aucun compte, aucun achat). La seconde
  requête porte sur la même page, même hôte, avec le paramètre `?error=cookies_not_supported` ; elle a reçu la page
  (200). Je n'en ai extrait que le résumé et les métadonnées, par script (`outils/extraire_resume_editeur_v1.py`). La
  page contient aussi le corps de l'article (accès libre) : non lu.
- Citations contrôlées par script : `outils/verifier_citations_cp02_v1.py`. Chaque phrase citée doit être sur la page
  citée du PDF empreinté (ou dans le résumé de la page empreintée) et, mot pour mot, dans cette note ; le script vérifie
  l'empreinte de chaque source avant d'en extraire le texte. Sorties : `outils/verifier_citations_cp02_v1.sortie.txt` (cas
  sain) et `outils/verifier_citations_cp02_v1.artefact.sortie.txt` (garde R5 : un chiffre altéré et une bonne phrase à
  la mauvaise page doivent être refusés, une bonne phrase acceptée ; une source à l'empreinte altérée aussi refusée).
  Bilan : 121 citations contrôlées (pages des cinq PDF ; entrées bibliographiques chez Pan et al., Zeng, Khan et al.,
  Robinson et al. ; pages de résumé ; page de l'éditeur ; ancres des corrections dans le brouillon 5, la note de Panin,
  l'état de l'art et la configuration), 0 échec ; 16 d'entre elles appuient une paraphrase française et ne sont
  contrôlées que sur la source. Sur les artefacts : 1 acceptée, 3 refusées, comme attendu. Le même script recoupe tous
  les segments entre guillemets de la note avec toutes les sources ; les introuvables sont des phrases françaises
  (corrections proposées, mots du programme) ou des extraits avec ellipse, listés dans la sortie avec leur nombre.
- Moyennes de ChatInject recalculées depuis son tableau 1 : `outils/recalcul_moyennes_chatinject_v1.py`, sortie
  `outils/recalcul_moyennes_chatinject_v1.sortie.txt` (5,1833 et 32,0500 sur AgentDojo ; 15,1333 et 45,9000 sur
  InjecAgent ; 13,8417 et 45,6500 en multi-tour ; égales aux chiffres des auteurs, p. 1 et p. 5).
- Résumés et historiques : `outils/extraire_resumes_cp02_v1.py`, sortie `outils/extraire_resumes_cp02_v1.sortie.txt`.
- Revendications confrontées : énoncés retenus de HC1 (N-005, N-013, N-023), HC2 et HC2b, HC3 (N-013, section 2), tels
  que le brouillon 5 les reprend (l. 226 à 272) ; pièces revendiquées (l. 270 à 272) ; familles du vivier (l. 690 à
  696 ; réserve 9, l. 756 à 759 ; configuration, champ `vivier`), surtout la famille 4, « usurpation stylistique de
  l'instructeur ».

## Verdict

- **Geng et al. (2502.15851v4, PDF entier) : pas de collision.**
- **Chang, Jun et Lee, ChatInject (2509.22830v3, PDF entier) : pas de collision.**
- **Jiang et al., ChatBug (2406.12935v2, PDF entier) : pas de collision.**
- **Yang et al. (2411.11407v1, PDF entier) : pas de collision.**
- **Wu et al. (2510.19687v2, PDF : corps entier, annexes parcourues) : pas de collision.**
- **CP-01, Kumaran et al., version publiée (Nature Machine Intelligence, 2026) : pas de collision au niveau du résumé.**
  Le résumé publié ne dit rien de plus que la préimpression sur une pièce revendiquée. Il élargit la portée (« diverse
  models », « reasoning tasks ») et parle de « computational modelling ». Le corps, en accès libre, n'est pas lu.

Aucun des cinq n'étudie un moniteur de contrôle dont on lit le verdict sous attaque. Aucun n'estime une destination
libre, ni n'a de nul de retour à la moyenne du corpus : les deux déclencheurs de la réserve de N-005 manquent. Aucun n'a
de sonde de l'agent auteur. Aucun n'a de condition « style de l'instructeur sans ordre » : dans les quatre papiers
d'attaque ou de conflit de consignes, un ordre ou une demande nuisible est toujours présent ; Wu et al. n'imitent pas
l'instructeur. La porte GC n'est pas déclenchée. Ce verdict ne vaut que pour ces sources, aux niveaux de
lecture du tableau (R8) : les pièces revendiquées ne sont pas trouvées dans les sources lues.
Le plus proche est ChatInject : à contenu constant, forger les jetons de rôle du gabarit de conversation autour d'un ordre
fait monter l'obéissance d'agents. C'est un précédent partiel du versant stylistique de HC3, de même nature que
2603.12277 déjà cité (ordre présent, modèle attaqué, ni juge ni sonde de l'auteur). Il fixe aussi une borne de lecture :
la famille 4 du brouillon est en texte brut, les jetons de gabarit sont exclus par les gardes ; C-P6 ne dit rien de
l'usurpation par jetons forgés (CQ-04).
Constats : 0 critique, 0 majeur, 5 mineurs, 2 de forme, 4 d'information.

## Geng et al. — ce que le papier mesure

- **Objet** (p. 1) : « We find that the widely-adopted system/user prompt separation fails to establish a reliable
  instruction hierarchy ». Des contraintes de forme contradictoires et vérifiables par programme (langue, casse, nombre de
  mots, de phrases, mots clés), l'une dans le message « système », l'autre dans le message de l'utilisateur ; p. 3 :
  « Pure Separation (Pure) places the primary constraint in the system message as a system-level directive, while
  keeping the base task and the secondary constraint in the user message. »
- **Modèles** (p. 11, tableau 6) : six, dont « Qwen-7B qwen2.5-7b-instruct » et « Llama-8B Llama-3.1-8B » (tableau 7 :
  « Llama-3.1-8B-Instruct 0.6 0.9 », température et top p). Des modèles qui génèrent un texte ; jamais des juges.
- **Résultat** (p. 4) : « Most models show dramatically lower performance (9.6–45.8% average R1) when handling
  conflicting constraints » ; lignes du tableau 2 : « Qwen-7B 86.4 10.1 9.1 11.8 82.5 8.9 8.8 8.7 9.6 » et « Llama-8B
  80.3 6.8 6.6 10.8 74.8 10.8 7.3 18.2 10.1 » (la dernière colonne est la moyenne ; la première, la contrainte seule).
- **Cadrages sociaux** (p. 1) : « societal hierarchy framings (e.g., authority, expertise, consensus) show stronger
  influence on model behavior than system/user roles ». Dessin (p. 6) : « All constraints are embedded within a single
  user message. » ; « Authority is indicated solely through minimal social framing (e.g., “CEO requires...” vs. “Intern
  requires...”). » Trois modèles seulement (p. 7) : « Qwen (14.4%), Claude (23.6%), and GPT4o-mini (47.5%) » ; tableau 4,
  « Qwen-7B 14.4 54.0 57.3 65.8 » (système / utilisateur, autorité, expertise, consensus). Lecture des auteurs (p. 7) :
  « These patterns indicate that model priorities are more strongly shaped by familiar societal hierarchies than by
  artificial system/user markers. »
- **Lien avec Zeng** : Zeng écrit (p. 2) « Our dataset is an augmented version of the benchmark in [6] » ; ses trois
  cadrages (« three representative forms of hierarchy were tested », p. 2) sont ceux de Geng et al. (p. 6).
- **Données contre consignes** : seulement en travaux voisins (p. 2) : « Another approach is to treat user inputs as data
  rather than instructions (Chen et al. 2024; Liu et al. 2023; Zverev et al. 2024) to prevent such bypasses. » Rien de
  mesuré.
- **Limite déclarée** (p. 7) : « We focus on single-turn interactions and simple, verifiable constraints ».
- **Confrontation** : modèles qui génèrent, sortie binaire par contrainte (respectée ou non) ; aucun moniteur, aucun
  verdict noté, aucune destination, aucune loi sur des intensités (une seule emphase, « Emph. ») ; aucune sonde. Les
  cadrages sociaux portent chacun un ordre (« CEO requires: … »). Ni la composante 1 de HC3 (aucune détection), ni la
  composante 2 (aucune condition sans ordre ; le rôle « système » est réel, pas imité). Source comportementale du
  précédent partiel Zeng (CP-04) ; contre-indice faible pour la famille 4 (CQ-05).

## Chang, Jun et Lee, ChatInject — ce que le papier mesure

- **Objet** (p. 2) : « attackers can forge role tags within low-priority tool outputs by incorporating these special
  tokens into malicious payloads. » ; (p. 3) « rather than modifying existing safety tokens, we forge entire role tags to
  exploit the model’s learned hierarchy, causing it to misinterpret malicious tool outputs as authoritative
  instructions. » Injection indirecte dans la sortie d'un outil, lue par un agent à outils.
- **Mesure** (p. 3) : « An attack is deemed successful if the agent executes Ia. » Taux de succès binaire et utilité, sur
  AgentDojo et InjecAgent. Neuf modèles (p. 4 et p. 5) : « Our selection includes 6 open-source LLMs with publicly available chat
  templates: Qwen3-235B-A22B », GPT-oss-120b, Llama-4-Maverick, GLM-4.5, Kimi-K2, Grok-2 ; plus GPT-4o, Grok-3,
  Gemini-2.5-Pro. Aucun de nos juges. Décodage (p. 19) : « All models were accessed via the OpenRouter (2025) API with
  temperature set to 0 (greedy decoding). »
- **À contenu constant** (p. 19) : « This variant maintains the exact content from the original InjecPrompt attack while
  incorporating chat template formatting. » Gain (p. 1) : « improving from 5.18% to 32.05% on AgentDojo and from 15.13% to
  45.90% on InjecAgent » (moyennes recalculées, `outils/recalcul_moyennes_chatinject_v1.sortie.txt`).
- **Rôles en texte brut contre jetons natifs** (p. 5) : « While Default Multi-turn alone yields only a modest improvement
  in LLM ASR (13.8% on average), Multi-turn + ChatInject exhibits a strong synergy: ASR rises sharply to 45.6% on average
  across most models. » La variante en texte brut écrit chaque tour sous la forme « role: content » (p. 4). Le gain
  moyen est modeste, mais pas partout : chez Qwen-3 sur AgentDojo, 60,9 % contre 17,5 % (tableau 1, p. 5 ; sortie du
  recalcul). Gabarit à délimiteurs faibles (p. 5) : « lacks strong role delimiters (beyond a light-weight separator),
  which likely reduces the authority of the “system-like” payload ». Gabarits rendus par homoglyphes (p. 17) : « we
  observe that the homoglyph-encoded chat templates have almost no effect on the models, yielding very low ASR values. »
- **Défenses** (p. 9) : détecteurs externes et défenses par consigne, dont les délimiteurs de données. P. 20 : « The PI
  Detector utilizes a BERT-based classifier to scan outputs from tools or external sources for characteristics typical
  of prompt injection. » ; « The delimiting method places all tool-generated content within clearly defined markers and
  instructs the language model to disregard any instructions found between these boundaries. » Résultats (p. 9) :
  « However, as demonstrated in Figure 5, both models show higher ASR against ChatInject and Multi-turn methods compared
  to the baseline no-defense condition. » ; « this suggests the detector primarily reacts to special tokens rather than
  contextual manipulation. » Aucun taux de détection à taux de fausses alarmes fixé ; seul le succès après filtrage est
  rapporté.
- **Lecture interne** (p. 16) : « we measure how chat-template tags redistribute attention between the user instruction
  and the attacker instruction inside the conversation. » Deux modèles ; poids d'attention de l'agent qui lit, pas une
  sonde. Limite (p. 15) : « Resource constraints prevented detailed attention analysis to understand how chat templates
  influence model behavior at the representational level. »
- **Persuasion** (p. 15) : « using different persuasion strategies (time pressure, social punishment, authority
  endorsement, negotiation) » : dans des dialogues forgés qui portent l'ordre.
- **Confrontation** : agents qui exécutent, pas des moniteurs qui notent ; issue binaire, cible imposée (l'ordre de
  l'attaquant) ; aucune destination, aucune loi sur des intensités (la similarité des gabarits est un prédicteur continu
  du succès, figure 3, p. 6, mais rien n'est estimé vers une destination) ; aucune sonde. HC3, composante 1 : les
  détecteurs sont des classifieurs, pas des juges moniteurs génératifs sous le protocole « contenu = données » ; les
  délimiteurs sont une défense de l'agent lui-même, mesurée par l'obéissance et non par une alarme. Composante 2 : un
  ordre est toujours présent. Précédent partiel du versant stylistique (CQ-03), borne de lecture de la famille 4 (CQ-04),
  contre-indice faible (CQ-05).

## Jiang et al., ChatBug — ce que le papier mesure

- **Objet** (p. 3) : « Our key insight is that the chat templates pre-define rigid formats that should be followed by
  LLMs, but not by users. » Deux attaques par l'utilisateur qui écrit lui-même le gabarit : format décalé (p. 3, « a
  malicious user may omit all control tokens including BOT, EOT, and role control tokens when prompting the victim
  LLMs. ») et débordement de message (p. 4, « In a message overflow attack, the message from malicious users extends
  beyond its own EOT token and the role control token r2. »), c'est-à-dire un préremplissage du champ de l'assistant.
- **Modèles** (p. 4) : « Llama-3 (8B-Instruct) (Meta 2024), Mistral (7B-Instruct v0.2) (Jiang et al. 2023) », Vicuna,
  Llama-2 et quatre modèles fermés. Pas nos versions (nos juges : Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3).
- **Mesure** : taux de réponses nuisibles à des demandes nuisibles (AdvBench), par correspondance de refus et par un
  modérateur Llama-Guard-2, p. 4 : « fine-tuned from Llama 3, as a moderator to evaluate whether a response is
  harmful. » Le modérateur note, il n'est pas attaqué.
- **Intensité graduée, direction imposée** (p. 4) : « We observe that the probability of generating the desired harmful
  response increases as the user overflows more tokens. » (zéro à neuf jetons de débordement ; probabilité de la réponse
  visée, figure 3).
- **Tableau 2** (p. 5) : « Direct Instruct 5.6% 3.7% 24.0% 22.9% 0.4% 0.0% 1.1% 0.0% » et « Mismatch-∅ 90.6% 40.4% 65.2%
  55.6% 17.1% 12.7% 65.4% 50.0% » (Vicuna, Mistral, Llama-2, Llama-3).
- **Détection** : décrite, non mesurée (p. 6) : « Although effective, detection-based methods are less frequently
  adopted in practice compared to mitigation-based methods. » ; (p. 7) « We believe that detection-based countermeasures
  could effectively mitigate the ChatBug vulnerability. »
- **Confrontation** : débridage d'un assistant par son propre utilisateur ; aucun contenu inséré dans ce qu'un moniteur
  note ; aucun moniteur, aucune destination estimée, aucune régression (la courbe de débordement va vers une réponse
  imposée) ; aucune sonde ; la demande nuisible est un ordre. Rien de HC1 à HC3. Information sur l'instrument (CQ-10).

## Yang et al. — ce que le papier mesure

- **Objet** (p. 2) : « Attackers can exploit this by crafting prompts that mimic authoritative sources, leading to the
  generation of harmful content. » Une demande nuisible accompagnée d'une référence forgée (article, dépôt de code,
  encyclopédie, actualité, blogue…).
- **Résultat** (p. 4) : « LLMs are significantly more susceptible to prompts containing references from academic papers or
  GitHub repositories than to those citing less authoritative sources, such as blog posts or news articles. » Types de
  source catégoriels, sans intensité graduée.
- **Modèles** (p. 8) : « We conducted our experiments on follow victim LLMs: Llama2-7b-chat, Llama-3-8b-instruct,
  GPT-3.5-turbo, GPT-4(0613), and Claude-3(v3-haiku). » Juge de nocivité (p. 8) : « Finally, we employ Llama-Guard [43]
  to assess whether the content generated by the target model contains harmful elements. » Le juge n'est pas attaqué.
- **Défenses** : filtres existants (p. 12 : « After applying OpenAI Moderation for filtering, only about 26% of harmful
  content is successfully removed. ») et consignes système de vérification (tableau 3, p. 13 : « Harm. 86% 13% 98% 99%
  74% »).
- **Logits** : divergence entre réponses avec et sans citation, et avec un document (p. 12, « Figure 8: KL divergence of
  logits for non-cited, cited, and with-RAG prompts. ») : lecture du modèle qui génère, pas une sonde de l'auteur.
- **Confrontation** : débridage ; issue binaire (nuisible ou non), cible imposée ; types de citation catégoriels ; aucun
  moniteur dont on lit le verdict sous attaque ; aucune destination, aucune loi ; aucune sonde ; l'autorité forgée
  accompagne un ordre. Indice voisin de la famille « approbations forgées » (référence savante forgée), du même genre que
  Wang Q. et al. (CS-02 de la note du second rang). Rien de HC1 à HC3.

## Wu et al. — ce que le papier mesure

- **Trois expériences**. (1) Conseil délibéré contre information « espionnée » (p. 5) : « both GPT and Claude
  statistically significantly changed their score less when receiving deliberate advice from Player 1 than if they had
  “spied” Player 1’s true answer. » (2) Recommandations sous incitations graduées (p. 6) : « each of the 16 different
  character-incentive speakers provides a recommendation for a particular option, and we subsequently elicit LLMs’
  opinions on the quality of that option. » ; incitations (p. 24) : « referral_bonus = [0, 10, 100, 1000] ». (3)
  Publicités réelles (p. 3) : « LLMs were much worse at drawing vigilant inferences in these naturalistic contexts
  (r < 0.2). »
- **Référence normative** (p. 7) : « Specifically, we measure the Pearson correlation between the LLM’s elicited
  influence scores and the value generated by the rational model when fitted to the LLM’s elicited trust and incentive
  scores. » Notes écrites de 0 à 100, échantillonnées (p. 7 : « All models are sampled at temperature 1. »).
- **Modèles** (p. 7) : « We evaluate a suite of state-of-the-art LLMs: GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Flash, and
  Llama 3.3-70B, smaller open models: Llama 3.1-8B, Llama 3.2-3B, and Gemma 3-4B » ; tableau 1 : « Llama 3.1-8B 0.608
  0.813 0.701 » (variante, instruite ou non, non précisée).
- **« Steering »** : une phrase ajoutée à la consigne, pas une direction d'activation (p. 9) : « We attempt this by
  appending the following phrase at the end of each original prompt in Appendix C.1: ». Effet de la longueur (p. 10) :
  « LLMs are motivationally vigilant in simple, short interactions, but this quality weakens in more realistic settings
  with richer context and noise. »
- **Confrontation** : un modèle qui conseille ou décide, pas un moniteur ; aucun attaquant ; la direction est imposée
  (l'option recommandée) ; la référence est une postérieure bayésienne calculée, pas une destination estimée, et aucun
  nul de moyenne du corpus ; incitations graduées, mais lues par une corrélation au modèle rationnel, pas par une loi
  Δv = g · (ĉ − v₀) ; aucune sonde ; aucun ordre au moniteur. Rien de HC1 à HC3. Même nature que la référence bayésienne
  de Kumaran et al. (CP-03 de la note de Panin). Information pour HC5 (CQ-10).

## CP-01 — Kumaran et al., version publiée : contrôle du résumé

- **Page lue** : `telechargement/nmi-s42256-026-01217-9/page-resume-s42256-026-01217-9-sans-temoin.html` (`fa5dfe4a…`) ;
  extraction : `outils/extraire_resume_editeur_v1.sortie.txt`. Titre, auteurs (les onze, même ordre que la
  préimpression), revue, volume 8, numéro 4, pages 614 à 627, identifiant 10.1038/s42256-026-01217-9 : conformes à
  l'entrée de Panin (p. 15). Dates : « Received : 02 July 2025 », « Published : 22 April 2026 ».
- **Ce que dit le résumé publié** : « Here we show that LLM confidence is governed by two competing mechanisms that explain
  this paradox. » ; « LLMs update their confidence more strongly in response to opposing advice than supporting advice,
  deviating markedly from optimal Bayesian reasoning. » ; « These mechanisms operate across diverse models and generalize
  from simple factual queries to reasoning tasks. »
- **Ce que disait la préimpression** (`1f76623b…`) : « We show that LLMs -- Gemma 3, GPT4o and o1-preview -- exhibit a
  pronounced choice-supportive bias » ; « parsimoniously capture LLM behavior in a different domain. »
- **Comparaison** : mêmes deux mécanismes (biais en faveur du choix initial ; surpondération du conseil contraire,
  comparée à la mise à jour bayésienne). Le résumé publié élargit la portée : modèles plus divers, tâches de raisonnement,
  modélisation par le calcul. Il ne parle ni de moniteur, ni d'attaquant, ni de famille d'attaque, ni de destination, ni
  de sonde d'activations. **Sur une pièce revendiquée, il ne dit rien de plus que la préimpression.**
- **Verdict** : pas de collision au niveau du résumé. Le corps publié n'est pas lu : il est en accès libre (sections
  « Main », « Results », « Methods » présentes sur la page). La préimpression était le plus proche des sept voisins de
  Panin (CP-01 : zone séduisante, R8). La session décide si le résumé suffit (CQ-02).

## Confrontation aux pièces revendiquées

| pièce (énoncés retenus) | Geng 2502.15851v4 | ChatInject 2509.22830v3 | ChatBug 2406.12935v2 | Yang 2411.11407v1 | Wu 2510.19687v2 | Kumaran, version publiée (résumé) |
|---|---|---|---|---|---|---|
| HC1 : destination ĉ estimée librement | non : contrainte respectée ou non | non : ordre exécuté ou non | non : réponse nuisible imposée | non : nuisible ou non | non : option recommandée imposée | non : choix binaire, direction imposée (préimpression) ; rien de nouveau au résumé |
| HC1 : ĉ testée contre la cible et contre la moyenne du corpus | non | non | non | non | non : postérieure bayésienne calculée | non : mise à jour bayésienne |
| HC1 : comparée entre familles | non | ampleur seulement (gabarits, techniques de persuasion, p. 7, p. 15) | non | ampleur seulement (types de citation, p. 4) | non | non |
| HC1 : moniteurs de contrôle sous attaque | non : modèles qui génèrent | non : agents ; détecteurs classifieurs (p. 9, p. 20) | non : le modérateur note sans être attaqué (p. 4) | non : juge de nocivité non attaqué (p. 8) | non | non |
| HC1 : régression sur plusieurs intensités par famille | non : une emphase | non : similarité des gabarits, prédicteur du succès (p. 6), sans destination | non : zéro à neuf jetons de débordement, direction imposée (p. 4) | non : catégories | non : incitations graduées, corrélation au modèle rationnel (p. 7) | non |
| HC1 : instrument (probabilité des jetons ; cité, non revendiqué) | non | non | probabilité de la réponse visée (p. 3, p. 4) | divergence des logits (p. 12) | non : notes écrites | logits (préimpression) |
| HC1 et HC2 : opposition juge / sonde ; sonde de l'agent auteur | non | non : attention de l'agent qui lit (p. 16) | non | non | non | non |
| HC2b : trahison par les activations | non | non | non | non | non | non |
| HC3, composante 1 : ordres en bande détectés sous « contenu = données » par des juges moniteurs | non : rien de mesuré (p. 2) | non : classifieurs et délimiteurs côté agent, succès après filtrage, sans taux de détection (p. 9, p. 20) | non : détection décrite, non mesurée (p. 6, p. 7) | non : filtres de nocivité | non | non |
| HC3, composante 2 : style de l'instructeur sans ordre ; g > 0 juges, g nul sondes de l'auteur | non : ordres présents ; rôle « système » réel | précédent partiel : rôles forgés autour d'un ordre, à contenu constant, sur des agents (p. 1, p. 19) ; CQ-03 | non : gabarit de l'utilisateur, ordre présent | non | non | non |

## Constats

Format : identifiant, gravité, où (section et ligne du brouillon 5), ce qui est, ce qui devrait être, correction en mots
exacts. Aucun constat ne change un énoncé d'hypothèse ni une pièce revendiquée. Une collision, même partielle, serait un
nœud de Lazar : aucune n'est trouvée. Les marqueurs `<<…>>` sont à remplir par la session au versement.

**CQ-01 — mineur — verrou 2 (l. 67 à 75 ; phrase visée, l. 74) ; correction proposée par CP-02 (note de Panin, l. 174).**
- Ce qui est : CP-02 propose d'ajouter au verrou les cinq voisins « titres seulement, non lus », à contrôler avant le
  scellement.
- Ce qui devrait être : le contrôle est fait ; le verrou cite cette note, son verdict et le niveau de lecture de chacun.
- Correction, mots exacts : dans la phrase ajoutée par CP-02, remplacer de « Même contrôle pour les voisins de second rang
  cités par les sept papiers ci-dessus » jusqu'à « (rôles et gabarits forgés : famille « usurpation stylistique », HC3). »
  par : « Voisins de second rang cités par les sept papiers ci-dessus, contrôlés par un sous-agent neuf (note
  `<<CHEMIN_NOTE_VOISINS_CP02>>`, `<<EMPREINTE_NOTE_VOISINS_CP02>>`), lus sur PDF, « pas de collision » pour chacun :
  Geng et al., « Control Illusion: The Failure of Instruction Hierarchies in Large Language Models », 2502.15851v4
  (AAAI-26) ; Chang, Jun et Lee, « ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents », 2509.22830v3
  (ICLR 2026) ; Jiang et al., « ChatBug: A Common Vulnerability of Aligned LLMs Induced by Chat Templates »,
  2406.12935v2 (AAAI 2025) ; Yang et al., « The Dark Side of Trust: Authority Citation-Driven Jailbreak Attacks on Large
  Language Models », 2411.11407v1 ; Wu et al., « Are Large Language Models Sensitive to the Motives Behind
  Communication? », 2510.19687v2 (NeurIPS 2025 ; annexes parcourues). » Garder la phrase suivante de CP-02 (« Zhu et al.
  2025 et Weng et al. 2025, … »).
- Si CP-02 n'est pas appliqué, la même phrase se place avant « Même contrôle pour les deux voisins cités par Bajaj et
  Tiganj » (l. 74).

**CQ-02 — mineur — verrou 2 (l. 67 à 75) ; corrections proposées par CP-01 et CP-03 (note de Panin, l. 169 et l. 180).**
- Ce qui est : CP-01 propose d'écrire que le résumé de la version publiée de Kumaran et al. est « à contrôler au niveau du
  résumé avant le scellement (R8) » ; CP-03 écrit « version publiée dans Nature Machine Intelligence, 2026, non lue ».
- Ce qui devrait être : le résumé publié est contrôlé (section « CP-01 » ci-dessus) ; le texte le dit, avec la borne de
  lecture. La session écrit aussi si le résumé suffit pour le voisin le plus proche des sept, ou si le corps publié, en
  accès libre et sans coût, doit être lu avant le scellement (R8). Je ne tranche pas.
- Correction, mots exacts : dans la phrase proposée par CP-01, remplacer « à contrôler au niveau du résumé avant le
  scellement (R8). » par « contrôlée au niveau du résumé sur la page de l'éditeur (note `<<CHEMIN_NOTE_VOISINS_CP02>>`,
  page `fa5dfe4a30174a8fd8eea63700de9867cb5ce8b0efbfe738893dd7a9bd2266fc`) : « pas de collision » à ce niveau ; le résumé
  publié reprend les deux mécanismes de la préimpression et élargit la portée (modèles plus divers, tâches de
  raisonnement) ; corps publié, en accès libre, non lu (R8). » Dans le bloc proposé par CP-03, remplacer « version publiée
  dans Nature Machine Intelligence, 2026, non lue » par « version publiée dans Nature Machine Intelligence, 2026, résumé
  lu, corps non lu ».
- Hors de ma consigne : l'écart de moindre risque noté par CP-01 pour Pan et al. (version des Findings of the ACL 2026
  non lue) reste ouvert.

**CQ-03 — mineur — HC3, composante 2, « Précédents partiels » (l. 268).**
- Ce qui est : la liste cite 2603.12277 (à argument constant, ôter le style fait tomber le succès d'attaque ; ordre
  présent ; modèle attaqué) et SLEIGHT-Bench. Elle ne cite pas le précédent publié le plus net de l'usurpation **de
  format** du canal d'instruction, ni la source comportementale du précédent Zeng proposé par CP-04.
- Ce qui devrait être : ChatInject cité comme précédent partiel, avec ses limites (ordre présent, agents, jetons natifs,
  ni juge ni sonde de l'auteur) ; Geng et al. cité comme source du dessin de Zeng.
- Correction, mots exacts, l. 268, après « (Panin, p. 8, p. 9 et p. 19). » (et après la phrase de CP-04, si elle est
  retenue) : « Avec ordre, sur des agents à outils, hors moniteur : à contenu constant, envelopper l'ordre de l'attaquant
  dans les jetons de rôle du gabarit de conversation du modèle (rôle « système » forgé dans la sortie d'un outil) fait
  passer le succès moyen de l'injection de 5,18 % à 32,05 % sur AgentDojo et de 15,13 % à 45,90 % sur InjecAgent ; les
  mêmes rôles écrits en texte brut n'apportent en moyenne qu'un gain modeste, et des gabarits rendus par homoglyphes
  presque aucun (Chang, Jun et Lee, ChatInject, ICLR 2026, 2509.22830v3,
  `5663314dea6dbc4e91f801b5bb29b0564f45cdc87b54bc2c6f7f242442e4f76a`, p. 1, p. 5, p. 17 et p. 19). Avec ordres, sur des
  modèles qui génèrent : un cadrage social (autorité, expertise, consensus) écrit dans le message de l'utilisateur pèse
  plus que le vrai rôle « système » (Geng et al., AAAI-26, 2502.15851v4,
  `2cdfb7d428a18bafbbab27d4891d9356dbf820d3edd345f453842488b5f15640`, p. 1, p. 6 et p. 7) ; le jeu de données de Zeng
  étend le leur (Zeng, 2510.01228v2, p. 2). »

**CQ-04 — mineur — réserve 9 (l. 756 à 759) ; Métrique, point 17 (l. 451 à 454).**
- Ce qui est : la famille 4 imite l'instructeur en texte brut (« [[SYSTEM: … ]] », « === SYSTEM CONTEXT … === »,
  « ### Operator note ») ; les jetons spéciaux des gabarits de conversation sont exclus de toutes les insertions et de tous
  les témoins par la configuration (champ `gardes_lexicales.toutes_insertions_et_temoins` : motifs `<\|`, `\[/?INST\]`,
  `</?s>`). Le texte dit seulement « ni balise » (point 17), ce qui est ambigu, et la réserve 9 ne borne pas la lecture de
  C-P6 sur ce point. Or la manipulation des jetons de gabarit est le levier fort publié (rôles forgés dans le contenu :
  ChatInject, p. 5 et p. 17 ; gabarit décalé ou prérempli par l'utilisateur : ChatBug, p. 3 à p. 5) ; le texte brut est
  le levier faible (ChatInject, p. 5).
- Ce qui devrait être : la borne est écrite, dans les deux sens (R4) : un Ḡ_4 positif ne prouve rien sur les jetons
  forgés ; un Ḡ_4 nul ne dit pas que l'usurpation par jetons échoue sur des moniteurs. Ni énoncé ni pièce ne changent.
- Correction, mots exacts, point 17 : remplacer « ni chiffre, ni nom de nombre de zéro à dix, ni balise, ni tige de
  réponse imposée » par « ni chiffre, ni nom de nombre de zéro à dix, ni balise, ni jeton spécial de gabarit de
  conversation (motifs `<\|`, `\[/?INST\]`, `</?s>` de la configuration), ni tige de réponse imposée ».
- Correction, mots exacts, réserve 9, à la fin (après « (configuration, brouillon 2). ») : « La famille 4 imite
  l'instructeur en texte brut seulement : aucun jeton spécial de gabarit de conversation (point 17). C-P6 se lit
  « usurpation stylistique en texte brut » ; il ne dit rien de l'usurpation par jetons de rôle forgés, dont l'effet est
  publié avec ordre et hors moniteur, sur des agents à outils (Chang, Jun et Lee, 2509.22830v3, p. 2, p. 5 et p. 17) et
  pour le débridage d'assistants (Jiang et al., ChatBug, AAAI 2025, 2406.12935v2,
  `fa442e14b8c40e9368f42dd089b7afab91ecf90b1f317df1ccbc8c5ee45087f4`, p. 3 à p. 5) ; un Ḡ_4 positif ou nul ne
  s'étend pas à elle. »

**CQ-05 — mineur — contre-indices déclarés (l. 325 à 344), famille 4 ; C-P6 (juges).**
- Ce qui est : aucun contre-indice n'est déclaré pour la famille 4.
- Ce qui devrait être : un contre-indice faible déclaré (R4), rapporté sans verdict. L'ordre des rangs étant choisi au
  pilote, il ne change aucun critère.
- Correction, mots exacts, après la l. 344 (ou à la suite des contre-indices ajoutés par CP-05, CV-06 ou CS-02) :
  « - Rôle « système » imité en texte brut (famille 4) : sur des modèles qui génèrent, avec ordres, le vrai rôle
  « système » fait mal respecter sa consigne face à une consigne contraire de l'utilisateur (réponses qui ne suivent que
  la consigne prioritaire : 9,6 % pour Qwen2.5-7B-Instruct et 10,1 % pour Llama-3.1-8B en moyenne, contre 86,4 % et
  80,3 % pour une consigne simple seule), et un cadrage social pèse plus que la séparation système / utilisateur (Geng et
  al., 2502.15851v4, p. 4, tableau 2, et p. 7, tableau 4). Sur des agents, des rôles forgés en texte brut ajoutent peu en
  moyenne, les jetons natifs du gabarit beaucoup, et des gabarits rendus par homoglyphes presque rien (Chang, Jun et Lee,
  2509.22830v3, p. 5 et p. 17). Un en-tête « système » ou « opérateur » écrit en texte dans le contenu peut donc peser
  peu sur un juge. Contre-indice faible pour C-P6 (juges) ; rapporté, sans verdict. »

**CQ-06 — forme — section « Contre-lecture » (l. 930 à 932) ; champs du scellement (l. 121 et 122).**
- Ce qui est : ni cette lecture, ni son verdict, ni sa note n'ont de place au texte.
- Ce qui devrait être : la note est citée par chemin et empreinte (R6) ; `<<DECISION_VOISINS>>` couvre aussi ces ajouts.
- Correction, mots exacts : à la fin du paragraphe « Contre-lectures des notes de lecture » (l. 932), ajouter :
  « Contrôle des voisins de second rang du constat CP-02 et de la version publiée de Kumaran et al. (CP-01), par un
  sous-agent neuf : cinq PDF lus à leur version (Geng et al. 2502.15851v4 ; Chang, Jun et Lee 2509.22830v3 ; Jiang et
  al. 2406.12935v2 ; Yang et al. 2411.11407v1 ; Wu et al. 2510.19687v2) et résumé de la version publiée de Kumaran et
  al. lu sur la page de l'éditeur ; note `<<CHEMIN_NOTE_VOISINS_CP02>>` (`<<EMPREINTE_NOTE_VOISINS_CP02>>`) ; « pas de
  collision » pour chacun ; traitement de chaque constat. » L. 121-122 : si CQ-03 est retenu, la liste entre parenthèses
  proposée par CV-08 et allongée par CP-06 s'allonge encore de « ; Chang, Jun et Lee ; Geng et al. ».

**CQ-07 — forme — registre de veille.**
- Ce qui est : aucun des cinq n'est dans `R/registres/veille.md` ni dans les états de l'art cherchés (en-tête).
- Ce qui devrait être : six lignes de routine à la veille.
- Correction : une ligne par papier : identifiant et version, niveau de lecture, « pas de collision avec HC1 à HC3 », note
  `<<CHEMIN_NOTE_VOISINS_CP02>>` (`<<EMPREINTE_NOTE_VOISINS_CP02>>`) ; ChatInject signalé aussi pour la famille 4 (CQ-04)
  et pour HC5 ; Wu et al. pour HC5 ; et une ligne pour Kumaran et al., version publiée, « résumé lu, corps en accès libre
  non lu ».

**CQ-08 — information — nos juges dans ces papiers.**
- Qwen2.5-7B-Instruct : Geng et al., en modèle qui génère, dans les deux expériences (p. 4, p. 7, p. 11).
  Llama-3.1-8B-Instruct : Geng et al. (tableau 6 : « Llama-3.1-8B » ; tableau 7 : « Llama-3.1-8B-Instruct », p. 11), hors
  de l'expérience des cadrages sociaux ; Wu et al., « Llama 3.1-8B », variante non précisée (p. 7). Mistral-7B-Instruct :
  ChatBug seulement, en version v0.2 (p. 4). ChatBug et Yang et al. utilisent Llama-3-8B-Instruct, pas 3.1. ChatInject :
  aucun.
- Jamais en moniteur de contrôle ; à ne pas citer comme tel. Aucun chiffre de ces papiers n'entre dans une puissance ni
  dans un seuil (N-023, section 1).

**CQ-09 — information — fiabilité.**
- Geng et al. : échantillonnage à température de 0,6 à 1,0 (tableau 7, p. 11) ; nombre de tirages par donnée non dit ;
  aucun intervalle ; un R1 bas mêle le choix de la consigne contraire (R2) et l'échec des deux (R3) ; cadrages sociaux
  sur trois modèles seulement (p. 7) ; fort effet d'ordre chez Claude sous le consensus (85,8 contre 38,2 ; p. 11 et
  tableau 8, p. 12).
- ChatInject : défenses numérotées « (1), (2), (2), (3), (4) » pour « four main approaches », qui sont cinq (p. 9) ;
  légende du tableau 8 « ASR » pour des valeurs d'utilité (p. 17 ; valeurs 50,9 et 78,4 égales à l'utilité du tableau 1) ;
  au tableau 1, l'écart de Grok-2, InjecAgent, multi-tour avec gabarit, est imprimé « (+18.8) » pour 10,4 contre 1,6
  (écart réel +8,8), et les écarts de cette colonne se rapportent au multi-tour par défaut, non à « Default InjecPrompt »
  comme le dit la légende (p. 5 ; sortie du recalcul) ; analyse d'attention sur deux modèles (p. 16 et p. 17).
- ChatBug : versions de modèles anciennes (Llama-3-8B-Instruct, Mistral v0.2) ; renvois à une « extended version » pour
  les annexes alors que le PDF lu les contient en partie (p. 3, p. 10).
- Yang et al. : un succès est compté si l'un de trois tirages à température 0,9 réussit (p. 9) ; « Figure 5 » citée pour
  la figure 2 (p. 4) ; gabarit de dialogue de Llama-3 non natif (« user: … assistant: … » après l'en-tête natif du rôle
  système, p. 17), soit un format décalé au sens de ChatBug ; préimpression sans lieu de publication.
- Wu et al. : « Llama 3.1-8B » sans variante ; modèles de raisonnement à dix tirages seulement (p. 7) ; notes écrites à
  température 1.
- Conséquence : citer en qualitatif ; les chiffres cités par CQ-03 et CQ-05 sont des chiffres des auteurs, recalculés pour
  ChatInject, jamais repris dans une puissance ni dans un seuil.

**CQ-10 — information — hors des pièces revendiquées : instrument, réserve 8, HC5.**
- Instrument : le mode direct du brouillon (point 4, l. 371 : « la réponse imposée suit immédiatement le dialogue ») est
  un préremplissage du champ de l'assistant, le « débordement de message » de ChatBug (p. 4). Il est identique dans toutes
  les conditions d'une loi (point 1, l. 355 à 357) : il est commun aux deux lectures qui forment Δ. Aucune correction.
- Réserve 8 (l. 754 et 755) : ChatBug montre qu'un gabarit décalé change beaucoup les sorties de Mistral-7B-Instruct v0.2
  et de Llama-3-8B-Instruct (tableau 2, p. 5). Appui à la consigne déjà écrite : voie du gabarit consignée pour chaque juge,
  la même dans toutes les conditions. Aucune correction.
- HC5 (contre-mesures) : délimiteurs de données, répétition de la consigne, détecteurs (ChatInject, p. 9 et p. 20) ;
  consignes de vérification (Yang et al., p. 13) ; phrase qui rend saillantes les intentions et les incitations (Wu et
  al., p. 9). À signaler à la veille de HC5, sans verdict ici.
- HC2 : l'analyse d'attention de ChatInject (p. 16) lit l'agent qui lit le contenu, comme les sondes lectrices déjà
  déclarées en contre-indice (l. 334 et 335) ; ce n'est pas une sonde. Aucune correction.

**CQ-11 — information — voisins de troisième rang, titres seulement, non lus.**
- Pour la composante 1 de HC3 (protocole « contenu = données »), ces sources citent des défenses par séparation des
  données et des consignes : Zverev et al., « Can LLMs Separate Instructions From Data? And What Do We Even Mean By
  That? », 2403.06833 (ICLR 2025 d'après ChatInject, p. 14 ; Geng et al., p. 2 et p. 9) ; Hines et al., « Defending
  Against Indirect Prompt Injection Attacks With Spotlighting », 2403.14720 (Geng et al., p. 8 ; ChatInject, p. 12 et
  p. 20) ; StruQ, 2402.06363 (Geng et al., p. 8).
- Le « spotlighting » et la hiérarchie d'instructions de Wallace et al. sont déjà à l'état de l'art v1 (l. 138), avec la
  conclusion « Couvre les ordres en bande de HC3 ». Zverev et al. n'est dans aucun des fichiers cherchés. Zone non lue :
  c'est une question, pas une occupation (R8). Je propose la veille, pas le verrou : la composante 1 porte sur la
  détection par des juges moniteurs, que ces titres ne promettent pas ; la session en décide.

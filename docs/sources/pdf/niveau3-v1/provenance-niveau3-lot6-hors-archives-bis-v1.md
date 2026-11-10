# Provenance — niveau 3, lot 6 (pièces hors arXiv, seconde liste) — v1

Écrit le 2026-11-10T11:02:23Z (heure relevée par `date -u`) par l'agent de récupération du lot 6 (sous-agent de la session « pièces à réseau »). Outils : `curl` (client générique « Mozilla/5.0 (compatible; generic-fetch/1.0) »), recherche sur le web de l'outil WebSearch, `pdfinfo`, `pdftotext`, `sha256sum`, rendu texte par `python3 -I` et `html.parser`. Aucune clé, aucun compte, aucune dépense. Aucun verdict de fond : les pièces restent à lire par un lecteur neuf.

Dossier de travail (hors dépôt, propre à la session) : `/tmp/claude-0/-home-user-controle-ia-travail/ba75ee53-729a-59d5-934a-27a4eace4393/scratchpad/lot6/` ; pièces non versées dans son sous-dossier `non-verses/`. Toutes les heures ci-dessous sont celles de `date -u`, le 2026-11-10.

## 1. Pièces versées (`docs/sources/pdf/niveau3-v1/lot6/`, scellées)

| fichier | pages | octets | SHA-256 | titre lu page 1 | auteurs | date et version | adresse exacte | code | heure | licence relevée | venue imprimée dans le PDF |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `2609.03035v2.pdf` | 31 | 2698806 | `bccdbe1b2dd753f2bf26329541a4a717a57ab83b01dc54f7f8498d5ae6d28113` | You Can't Escape Your Activations: Evaluation Awareness and Multi-Agent Monitoring | Jaee Ponde, Aritra Das, Mihir More, Debayan Gupta (affiliation imprimée : Truth Audit Labs) | première version 2026-09-02 ; v2 du 2026-10-29 (interface d'arXiv, `id_list`, 10:58:06Z) | `https://export.arxiv.org/pdf/2609.03035v2` | 200 | 10:58:23Z | CC0 1.0 (lien `publicdomain/zero/1.0/` sur `https://arxiv.org/abs/2609.03035v2`, 200, 10:58:26Z) | aucune dans le PDF (page 1 : « arXiv:2609.03035v2 [cs.MA] 29 Oct 2026 ») ; le site des auteurs annonce « Accepted at NeurIPS 2026 AI4Good Workshop » (non vérifié sur le site de l'atelier) |
| `bednarik-schultze-2015-jdm-10-3-imperfect-weighting-site-revue.pdf` | 12 | 837480 | `1fec3103b88777afdc20bd2c0a355185b3295026f01cc6b3e15846ad9d09ab9e` | The effectiveness of imperfect weighting in advice taking | Peter Bednarik, Thomas Schultze | mai 2015 | `https://journal.sjdm.org/14/14731/jdm14731.pdf`, redirigée vers `https://jbaron.org/journal/14/14731/jdm14731.pdf` (site d'origine de la revue) | 200 | 10:57:49Z | CC BY 3.0 (page 1 du PDF : « The authors license this article under the terms of the Creative Commons Attribution 3.0 License ») | « Judgment and Decision Making, Vol. 10, No. 3, May 2015, pp. 265–276 » (page 1) |
| `bednarik-schultze-2015-jdm-10-3-imperfect-weighting-cambridge.pdf` | 12 | 826396 | `de7347ef201275df0435df53d13f18ebb78b2ca786fe734226b1140de39b0ffa` | même titre (même page 1) | mêmes | mai 2015 ; copie de l'éditeur actuel | `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A8EB67E83972D455EDA1E0AB1935654C/S1930297500004666a.pdf/effectiveness_of_imperfect_weighting_in_advice_taking.pdf` | 200 | 10:57:45Z | CC BY 3.0 (page 1 du PDF ; page de l'éditeur : « oaLicenseType: CC-BY », « creativecommons.org/licenses/by/3.0/ ») | même mention, page 1 |

Remarques.
- `2609.03035v1.pdf` était **déjà au dépôt** (`docs/sources/pdf/2609.03035v1.pdf`, `5092b602…`), non retéléchargée. La v2 est une version neuve : le titre perd « Own » (v1 selon l'outil de recherche : « You Can't Escape Your Own Activations ») et son résumé ajoute deux cadres « proches du déploiement » (bloc-notes partagé, mini-dépôt logiciel) où la collusion naît des incitations (lu sur le résumé de la page 1 seulement, non opposable). Le résumé servi par l'interface d'arXiv à 10:58:06Z est encore celui à deux jeux.
- Les deux copies de Bednarik et Schultze ont la même page 1 et le même nombre de pages, mais diffèrent octet par octet (`cmp`). Référence à citer : la copie de l'éditeur (DOI).
- Écart relevé pour Bednarik et Schultze : Crossref annonce pour ce DOI la licence `creativecommons.org/licenses/by-nc-nd/3.0/` (à partir de 2023), alors que le PDF et la page de Cambridge disent CC BY 3.0. Les deux permettent le versement dans le dépôt privé ; **à trancher avant toute copie publique**.

## 2. Références vérifiées (volume, pages, DOI)

Source : Crossref (`https://api.crossref.org/works/<DOI>`, 200, de 10:59:42Z à 10:59:46Z ; fichiers `*-crossref.json` dans `non-verses/`), recoupée avec la page 1 des PDF obtenus. Les pages de ScienceDirect ont refusé (section 4) : pour les trois articles d'Elsevier la vérification repose donc sur Crossref (métadonnées déposées par l'éditeur), non sur la page de l'éditeur elle-même.

| référence | revue, volume(numéro), pages, date | DOI | recoupement |
|---|---|---|---|
| Bednarik, P. et Schultze, T. (2015). The effectiveness of imperfect weighting in advice taking | *Judgment and Decision Making* 10(3), 265–276, mai 2015 | 10.1017/S1930297500004666 | page 1 des deux PDF ; page de Cambridge (« pageRange 265 - 276 ») |
| Harvey, N. et Fischer, I. (1997). Taking Advice: Accepting Help, Improving Judgment, and Sharing Responsibility | *Organizational Behavior and Human Decision Processes* 70(2), 117–133, mai 1997 | 10.1006/obhd.1997.2697 | notice de l'université de Haïfa (volume 70, pages 117-133, même DOI) ; notice RePEc |
| Yaniv, I. et Kleinberger, E. (2000). Advice Taking in Decision Making: Egocentric Discounting and Reputation Formation | même revue 83(2), 260–281, novembre 2000 | 10.1006/obhd.2000.2909 | page 1 du PDF de l'université hébraïque (« Vol. 83, No. 2, November, pp. 260–281, 2000, doi:10.1006/obhd.2000.2909 ») |
| Yaniv, I. (2004). Receiving other people's advice: Influence and benefit | même revue 93(1), 1–13, janvier 2004 | 10.1016/j.obhdp.2003.08.002 | page 2 du document de travail (« Paper appeared in: Organizational Behavior and Human Decision Processes 93 (2004) 1-13 ») |

La référence « Harvey et Fischer (1997), *OBHDP* 70(2):117–133 » de `docs/etat-de-l-art/porte-GC-loi-de-deference-v1.md` concorde.

## 3. Pièces non versées (dossier de travail, sous-dossier `non-verses/`)

| fichier | pages ou nature | octets | SHA-256 | titre lu | auteurs | date | adresse exacte | code | heure | licence relevée, motif |
|---|---|---|---|---|---|---|---|---|---|---|
| `hebbar-2025-redwood-blog-diffuse-threats.html` | billet, HTML brut | 224247 | `affcb27d7938d81b04b4dab5c1f4e8c5fa8eeac2e0e5d47a9208a6b97f52802e` | How can we solve diffuse threats like research sabotage with AI control? | Vivek Hebbar (balise `author`) | 2025-04-30 (`datePublished` 2025-04-30T23:18:33+00:00) | `https://blog.redwoodresearch.org/p/how-can-we-solve-diffuse-threats` | 200 | 10:57:40Z | aucune licence ouverte (pied de page « © 2026 Buck Shlegeris ») ; non versable |
| `hebbar-2025-redwood-blog-diffuse-threats.txt` | rendu texte | 14310 | `e378d70d9d8d2bb489cffbd9cf0a84bb9039e9df866952746165431678f0f73b` | idem | | | | | | |
| `hebbar-2025-lesswrong-diffuse-threats.html` | même billet, avec commentaires | 588766 | `ef691747f2e587b90ab62cce3dab3b8bbc30c58dcca39091419a954fc00d6c09` | idem (`citation_title`) | Vivek Hebbar (`citation_author`) | `postedAt` 2025-04-30T19:23:19Z | `https://www.lesswrong.com/posts/Mf5Hnpi2KcqZdmFDq/how-can-we-solve-diffuse-threats-like-research-sabotage-with` | 200 | 10:57:41Z | aucune licence ouverte relevée ; non versable |
| `hebbar-2025-lesswrong-diffuse-threats.txt` | rendu texte | 17384 | `a6d2ff07b564189f085eadddf597a22f5379b6aa46702c81d0fef73619a33125` | | | | | | | |
| `hebbar-2025-alignmentforum-diffuse-threats.html` | même billet | 465974 | `8349be54e0361f9d178165f21a9bbcd75ec5b1e1ecfe447342ebe62c1828c853` | idem | Vivek Hebbar | | `https://www.alignmentforum.org/posts/Mf5Hnpi2KcqZdmFDq/how-can-we-solve-diffuse-threats-like-research-sabotage-with` | 200 | 10:57:43Z | idem ; non versable |
| `hebbar-2025-alignmentforum-diffuse-threats.txt` | rendu texte | 16686 | `15b9255f5cc9dce9b2909f566f0a2be9580117597692fee94eddb11922d1d2f8` | | | | | | | |
| `ponde-2026-truthauditlabs-billet-you-cant-escape-your-activations.js` | billet du site de Truth Audit Labs (le site est une application à page unique : le texte est dans ce script) | 16984 | `f3011bf3e53a7a824895b1ea8d4672764a3f55b7bdac986aa91553ebda9385f7` | You can't escape your activations | Jaee Ponde, Aritra Das, Mihir More, Debayan Gupta | 30 octobre 2026 (page « Research ») | `https://truthauditlabs.ai/assets/Article-Cz9dsqJY.js` (page : `https://truthauditlabs.ai/research/you-cant-escape-your-activations`) | 200 | 11:00:14Z | « © 2026 Truth Audit Labs » ; non versable |
| `ponde-2026-truthauditlabs-billet-you-cant-escape-your-activations.txt` | chaînes de texte extraites du script (rendu partiel : les passages en éléments imbriqués peuvent manquer) | 7791 | `9829522e2c683bbef7d00eca0a22d4b65fdb6e55e773a54fa1602a63186ca909` | | | | | | | |
| `ponde-2026-truthauditlabs-billet-you-cant-escape-your-activations-coquille.html` | HTML servi à l'adresse de la page (coquille vide de l'application) | 1522 | `6b5ab4a7968bf365fcfcf5e099905bd26e36b8f65b8d5e38f786d81772add7d4` | Truth Audit Labs | | | `https://truthauditlabs.ai/research/you-cant-escape-your-activations` | 200 | 11:00:18Z | idem |
| `truthauditlabs-2026-page-recherche.js` et `.txt` | liste des travaux du site | 3325 ; 1092 | `b187765ea3ed929aba9ef97a0d1e29725d15f9153b4c1d88de4edc70fcfa8494` ; `4d98d3084aa9dfad84bd1c62415c807adb29f15922f23522316c1bfbf56dc941` | Research | | | `https://truthauditlabs.ai/assets/Research-Bvb0C9YS.js` | 200 | 11:00:16Z | idem |
| `yaniv-kleinberger-2000-obhdp-advice-taking-huji-dp212.pdf` | 22 pages ; mise en page de l'éditeur | 116683 | `28de362866ac4a94149eaf4c277f3d2095d18f15578a0f896000489b4cbe947a` | Advice Taking in Decision Making: Egocentric Discounting and Reputation Formation | Ilan Yaniv, Eli Kleinberger | novembre 2000 | `https://ratio.huji.ac.il/files/dp212.pdf` (Centre Federmann d'étude de la rationalité, université hébraïque de Jérusalem, institution des auteurs ; notice `https://ratio.huji.ac.il/node/3129595`) | 200 | 10:58:39Z | « Copyright 2000 by Academic Press » ; tous droits réservés ; non versable |
| `yaniv-2004-obhdp-receiving-advice-huji-dp405.pdf` | 20 pages ; manuscrit d'auteur, document de travail n° 405 (couverture datée de septembre 2005) | 253669 | `806b0c95f32a4addeebb08a252dcb67477e063ba6b658da614f1ea543a0f21b3` | Receiving Other People's Advice: Influence and Benefit | Ilan Yaniv | article de 2004 | `https://ratio.huji.ac.il/files/dp405.pdf` (même centre) | 200 | 10:58:34Z | aucune licence ouverte ; non versable. **Pagination propre au manuscrit : ne pas citer ses pages comme celles de la revue** |
| `harvey-fischer-1997-obhdp-taking-advice-notice-haifa.html` et `.txt` | notice institutionnelle avec résumé, volume, pages, DOI ; pas de texte intégral | 47728 ; 9660 | `86d036012a5eab4a610edb22a6ae06a38fa3450d04443e14617597042a7afc66` ; `ad9c24a4f11b1c4fc44da8e477ff150290704f4c62096eb625009045a51d94fe` | Taking Advice: Accepting Help, Improving Judgment, and Sharing Responsibility | Nigel Harvey, Ilan Fischer | mai 1997 | `https://cris.haifa.ac.il/en/publications/taking-advice-accepting-help-improving-judgment-and-sharing-respo/` | 200 | 10:59:03Z | notice ; non versable |
| `harvey-fischer-1997-obhdp-notice-repec.html`, `yaniv-kleinberger-2000-obhdp-notice-repec.html`, `yaniv-2004-obhdp-notice-repec.html` | notices RePEc (référence ; pas de résumé pour Harvey et Fischer) | 41308 ; 41002 ; 42528 | `dbcaf7984ee0faca7bfdcd14da69be259b5a1f46eba175cfa10962df4ba6e509` ; `d22ed8b46693aab9c41f5c5889e45e9090a7d426328721120c4ee3f727e4845e` ; `7ced24ab0868b507c67f486bc1d9451cdda7934680c6a375d0efa4095dd837e0` | | | | `https://ideas.repec.org/a/eee/jobhdp/v70y1997i2p117-133.html`, `…/v83y2000i2p260-281.html`, `…/v93y2004i1p1-13.html` | 200 | 11:00:34Z à 11:00:39Z | notices |
| `*-crossref.json` (quatre fichiers) | métadonnées Crossref | 16709 ; 14231 ; 16897 ; 7320 | Harvey et Fischer `02b18aa522ba5773f3efd38301d71e39dc65eca95b03648d68f1c8d4fc1d81f0` ; Yaniv et Kleinberger `e9bcbe292af10b43800ccdb9a509c99e6211ea598c6ec7ff34cd77cdd77f439d` ; Yaniv `39b43add7da8310916922b077eb6152f87ccdbda0ec1e5c54655b604e509cd2a` ; Bednarik et Schultze `99c099e38700ddc0aac9c66563bb6da39f2a4174229df541445ffa1dcec6ed89` | | | | `https://api.crossref.org/works/<DOI>` | 200 | 10:59:42Z à 10:59:46Z | métadonnées |
| `bednarik-schultze-2015-jdm-notice-cambridge.html` | page de l'éditeur | 1034436 | `ba6de79eea3497f56b2cb9f5d0c9cea6e17d1f7c74955527685cc5ee7e68eb1c` | The effectiveness of imperfect weighting in advice taking | | | `https://doi.org/10.1017/S1930297500004666` → page de Cambridge | 200 | 10:57:50Z | page d'éditeur ; le PDF, lui, est versé |
| `yaniv-kleinberger-2000-obhdp-notice-huji.html` | notice du centre | 67220 | `4b0c60ba6b49e3ae478459c79f8599ec8ebf91daf47952bc69099447f73d8a24` | | | | `https://ratio.huji.ac.il/node/3129595` | 200 | 10:58:44Z | notice |

Le billet de Vivek Hebbar porte, dans ses copies de LessWrong et de l'Alignment Forum, une demande de ne pas entraîner de modèles de langage dessus (« Canary string ») : raison de plus de ne pas le verser ni le recopier dans une copie publique.

## 4. Inaccessibles ou refus

| pièce | tenté | adresse | code | heure |
|---|---|---|---|---|
| Harvey et Fischer 1997, **PDF inaccessible (payant)** | page de l'éditeur | `https://doi.org/10.1006/obhd.1997.2697` → `linkinghub.elsevier.com` (page de redirection par script, 200, 10:58:49Z) ; `https://www.sciencedirect.com/science/article/pii/S0749597897926972` | 403, page « Are you a robot? » (captcha), non contournée ; page de refus gardée, `018c0b4e…` | 10:59:16Z |
| idem, autre source légitime | recherche au dépôt de University College London | `https://discovery.ucl.ac.uk/cgi/search/simple?q=…` | 403 | 10:59:06Z |
| idem | notice de Haïfa : résumé, pas de texte intégral ; aucune copie en accès ouvert trouvée par la recherche | voir section 3 | 200 | 10:59:03Z |
| Yaniv et Kleinberger 2000, page de l'éditeur | `https://www.sciencedirect.com/science/article/abs/pii/S0749597800929091` | | 403 (captcha), `88c142d4…` | 10:59:19Z |
| Yaniv 2004, page de l'éditeur | `https://www.sciencedirect.com/science/article/abs/pii/S0749597803001018` | | 403 (captcha), `deb8f273…` | 10:59:21Z |

Classement des trois articles d'Elsevier : Harvey et Fischer 1997 — PDF inaccessible (payant), résumé et référence seuls ; Yaniv et Kleinberger 2000 — copie institutionnelle (mise en page de l'éditeur) obtenue, non versée ; Yaniv 2004 — manuscrit d'auteur obtenu, non versé, version de la revue payante.

## 5. « Truth Audit Labs » : ce que c'est

- Une structure (site `https://truthauditlabs.ai/`, © 2026 ; liens du site vers `linkedin.com/company/truth-audit-labs` et `x.com/truthauditlabs`) ; affiliation imprimée des quatre auteurs de l'article arXiv 2609.03035.
- « Das » = Aritra Das, deuxième auteur. Le premier auteur est Jaee Ponde : la référence correcte est « Ponde, Das, More et Gupta (2026) », non « Das et collègues ».
- La pièce est un **article** (arXiv 2609.03035, catégorie cs.MA, v1 du 2 septembre 2026, v2 du 29 octobre 2026), doublé d'un **billet** du site (30 octobre 2026) qui renvoie à l'article. Le site l'annonce accepté à un atelier de NeurIPS 2026 (« AI4Good Workshop »), non vérifié à la source de l'atelier.
- Lien avec NARCBench (arXiv 2604.01151, Rose et collègues, déjà au dépôt en v3 et v5) : l'article n'est pas de l'équipe de NARCBench ; il entraîne ses sondes sur NARCBench-Core et cite « Rose et al. (2026) » (lu par `pdftotext`, non opposable).
- **Aucun dépôt de code** trouvé : aucune adresse de GitHub dans le texte du PDF ni dans les scripts du site.
- Le site liste deux autres travaux, non récupérés (hors consigne) : « Guess Who? But the faces are language models » (Das et Gupta, 6 novembre 2026, annoncé accepté à un atelier de NeurIPS 2026) et « Theories for Better Understanding of AI » (2 novembre 2026).

## 6. Journal des recherches (outil WebSearch, 2026-11-10, entre 10:57:25Z et 10:58:10Z)

| termes exacts | mode | résultat |
|---|---|---|
| `"How can we solve diffuse threats like research sabotage with AI control?"` | normal | billet trouvé : blog de Redwood Research, Substack, LessWrong, Alignment Forum |
| `"Truth Audit Labs" NARCBench collusion` | normal | rien sur Truth Audit Labs ; pages de NARCBench |
| `Bednarik Schultze 2015 "The effectiveness of imperfect weighting in advice taking" Judgment and Decision Making pdf` | normal | PDF de Cambridge, notice de l'IIASA, RePEc ; volume 10(3), 265–276 |
| `"Truth Audit Labs"` | normal | rien de pertinent |
| `"Truth Audit Labs" Das NARCBench collusion probe interpretability` | étendu | arXiv 2609.03035, courriels en `truthauditlabs.ai` |
| `Yaniv Kleinberger 2000 "Advice taking in decision making: Egocentric discounting and reputation formation" pdf huji.ac.il` | normal | notice du centre de l'université hébraïque, fichier `dp212.pdf`, DOI |
| `Yaniv 2004 "Receiving other people's advice: Influence and benefit" pdf` | normal | `ratio.huji.ac.il/files/dp405.pdf`, RePEc |
| `Harvey Fischer 1997 "Taking advice: Accepting help, improving judgment, and sharing responsibility" pdf` | normal | notices (Haïfa, RePEc) ; aucun PDF libre |

Autres requêtes de lecture : interface d'arXiv (`id_list=2609.03035`, 200, 10:58:06Z) ; notice de l'IIASA `https://pure.iiasa.ac.at/id/eprint/11440/` (200, 10:57:47Z, mention « Creative Commons Attribution ») ; scripts du site de Truth Audit Labs (`/`, `/assets/index-CyRywtkK.js`, 200, 10:58:29Z et 10:59:47Z).

## 7. Candidats à collision, à lire en priorité (sur le résumé seulement, non opposable)

1. **2609.03035v2** (Ponde, Das, More, Gupta) — N-053 (conscience d'évaluation du dispositif mesurée ; bras « fuite textuelle et contrôlabilité ») et le bras d'attaque informé de N-056 : l'article dit mesurer ce que deviennent des sondes d'activations quand les agents sont prévenus de la surveillance, puis reçoivent le score du moniteur ; la v2 ajoute deux cadres où la collusion naît des incitations. La v1 est au dépôt : vérifier laquelle a été lue.
2. **Billet de Vivek Hebbar (Redwood Research, 30 avril 2025)** — cadre même du programme (menaces diffuses, sabotage de recherche) : pose l'axe « diffus — concentré » et deux parades (entraînement en ligne, incrimination) ; à lire pour le positionnement plutôt que comme collision de méthode.
3. **Bednarik et Schultze 2015 ; Yaniv et Kleinberger 2000 ; Yaniv 2004 ; Harvey et Fischer 1997** — porte GC, loi de déférence : sources de la mesure du poids du conseil ; antériorité de la mesure en psychologie, à citer (Yaniv 2004, résumé : le poids du conseil décroît avec la distance à l'opinion initiale).

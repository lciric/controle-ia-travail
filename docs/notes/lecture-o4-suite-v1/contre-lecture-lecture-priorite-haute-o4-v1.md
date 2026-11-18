# Contre-lecture de « Lecture sur PDF des pistes de priorité haute contre O4 » v1

**Verdict : tient avec réserves.** La conclusion centrale tient : dans aucune des six pièces je ne trouve une statistique calculée hors de l'agent, sur engagement, contre la théorie en vigueur et valide à tout instant d'arrêt, et les 31 citations sont à la bonne page (31 sur 31). Mais la section 2.5 (EvoSCM) et quatre cases de la table sont fausses contre des pages que la pièce dit avoir lues (constat 1, bloquant pour l'usage de la table telle quelle), et cinq statuts ou phrases sont trop faibles ou inexacts (constats 2 à 6). Un bloquant localisé, cinq majeurs, huit mineurs. Une v2 est à écrire avant que la table serve à quoi que ce soit.

- **auteur : modèle C ; contre-lecteur : modèle D ; C ≠ D.** Le contre-lecteur n'a écrit aucune des pièces lues.
- **Heures (`date -u`)** : premier relevé 2026-11-14T09:20:09Z (pris au contrôle des provenances ; l'ouverture de la pièce le précède de peu, heure non relevée) ; relevé intermédiaire 2026-11-14T09:24:09Z ; écriture de ce fichier 2026-11-14T09:26:07Z.
- **Pièce jugée** : `lecture-pdf-priorite-haute-o4-v1.md`, empreinte `1e841edd55bf39586deea91fa999fe4544cdb9a0b9828ea8546ebfaba5c558df`, conforme à son compagnon ; ses trois pièces (`citations-…json` `7c339ba5…`, `verifier_…py` `2daf5daa…`, `resultat-…json` `7d9ccf4e…`) conformes à leurs compagnons (`sha256sum` sur chaque fichier, comparé au `.sha256`).
- **Ce qui a été fait** : pièce lue en entier ; contexte lu (note d'englobement, sections 0 et 5, en-tête de la première contre-lecture) ; six PDF contrôlés contre compagnon et provenance ; 31 citations rejouées par mon programme ; pages décisives relues. Aucune écriture git, aucun accès réseau, aucune dépense, aucun chemin interdit ouvert, aucune recherche récursive, aucun refus de permission ou de classifieur rencontré.
- **Ma propre profondeur (R8)** : BEYOND p. 11-17, 33-36, 52-57 en entier, termes sur les 60 pages ; ACES p. 3-7 en entier, termes sur 30 p. ; ATLAS p. 1-3 en entier, termes sur 20 p. ; WAHL p. 3-5 en entier, p. 6-9 par lignes filtrées, termes sur 55 p. ; EVOSCM p. 4-5, 18-19, 26-29 en entier, p. 30-31 en partie, termes sur 34 p. ; NMV p. 8-10 en entier, termes sur 42 p. Tout « non » ci-dessous est borné par cette profondeur. « p. N » = page du PDF.
- **Commande rejouable type** : `pdftotext -f N -l N <pdf> - | grep -n -i '<terme>'` (pdftotext 24.02.0). Mes 36 citations propres ci-dessous ont été vérifiées page par page de cette façon : 36 sur 36 retrouvées au niveau strict, après correction d'une page (WAHL, phrase du modèle de base : p. 8 et non p. 9).

## 1. PDF, compagnons, provenances

| pièce | empreinte = compagnon = provenance | version lue dans l'en-tête du PDF | pages (pdfinfo) | provenance |
|---|---|---|---|---|
| BEYOND 2603.14288 | oui (`8fe2b217…`) | v2, 6 avr. 2026 | 60 | adresse versionnée `arxiv.org/pdf/2603.14288v2` |
| ACES 2606.25039 | oui (`4ae1908a…`) | v1, 23 juin 2026 | 30 | adresse non versionnée |
| ATLAS 2606.12386 | oui (`f9ca0e09…`) | v1, 10 juin 2026 | 20 | adresse non versionnée |
| WAHL 2602.18266 | oui (`618c93eb…`) | v2, 24 juin 2026 | 55 | adresse non versionnée |
| EVOSCM 2609.01526 | oui (`4094a67b…`) | v2, 28 sept. 2026 | 34 | adresse non versionnée |
| NMV NBER w33363 | oui (`d889aff6…`) | « Working Paper 33363 », créé le 8 janv. 2025 | 42 | adresse NBER ; dit « pas la version de la revue » |

6 sur 6 : PDF et `provenance-v1.md` conformes à leurs compagnons ; versions et nombres de pages dits par la pièce exacts. Les deux fichiers de refus SSRN sont conformes à leurs compagnons.

## 2. Rejeu des citations

Commande : `python3 -I docs/notes/lecture-o4-suite-v1/rejouer_citations_priorite_haute_o4_v2.py /home/user/controle-ia-travail docs/notes/lecture-o4-suite-v1/citations-priorite-haute-o4-v1.json docs/notes/lecture-o4-suite-v1/rejeu-citations-priorite-haute-o4-v2.json`. Extraction page par page (`-f N -l N`), en mode défaut et en mode `-raw`.

| mesure | résultat |
|---|---|
| citations de la liste retrouvées sur la page dite, empreinte conforme | **31 sur 31** |
| au niveau strict (sous-chaîne, espaces réduits, ligatures, guillemets et tirets unifiés, casse et ponctuation gardées) | 30 sur 31 |
| au niveau lâche seulement (alphanumérique, casse ignorée) | 1 sur 31 : BEYOND p. 35, la liste écrit « our multi-objective gate », le PDF « Our multi-objective gate » (majuscule) |
| citation trouvée aussi sur une autre page | 0 |
| citation de la note absente de la liste | 1 : NMV p. 10 « After reviewing these results » ; rejouée : trouvée, strict |
| citation de la liste absente de la note | 1 : BEYOND p. 35 « Our agent emulates this skepticism by incorporating a multiobjective promotion gate » (voir constat 5) |
| accord avec le résultat de l'auteur | 31 sur 31 des deux côtés, mêmes empreintes |

## 3. Réponse à la question principale

Une statistique calculée hors de l'agent, sur engagement, contre la théorie en vigueur, à validité à tout instant d'arrêt : **non, dans aucune des six pièces, à ma profondeur.** « e-value », « e-process » (hors « pre-processing », ACES p. 15), « anytime », « martingale », « stopping » : zéro occurrence dans les six textes entiers. Les quatre propriétés, pièce par pièce :

| pièce | hors de l'agent | sur engagement | contre la théorie en vigueur | tout instant d'arrêt |
|---|---|---|---|---|
| BEYOND | oui (porte t_IC et Sharpe, p. 13, 16) | protocole dit « pre-committed », seuils « pre-defined » (p. 12, 16) ; pas de scellement | non dans l'éq. 3.10 ; affirmé en prose comme partie de la porte (p. 34-35) | non (Student, seuil 3,0, p. 34) |
| ACES | oui (score de validation, p. 4-5) | non | non (meilleur score retenu) | non |
| ATLAS | sans objet (pas de modèle de langue) | — | — | — |
| WAHL | oui (vraisemblance marginale de substitution, p. 4-5) | non | **oui, en partie** : le modèle de base est la particule initiale et est pesé contre les extensions (p. 4, 7, 8) | non (données fixes, pas de test, pas de contrôle d'erreur) |
| EVOSCM | **en partie** : poids et fiabilité tenus par le « runtime » (p. 27-29) ; validation du texte principal par l'agent (p. 5) | **oui, sans empreinte** : prédictions consignées avant l'issue (p. 5, 27, 30) | en partie : loi familière mise en concurrence à poids égaux (p. 27) | non |
| NMV | oui (tris, alpha à six facteurs, p. 9) | non | **oui** (six facteurs, puis plus de 200 anomalies, p. 2, 9-10) | non ; et ce ne sont pas des propositions de modèle de langue |

## 4. Constats

### Bloquant (localisé : section 2.5 et lignes (iii), (iv-b), « conjonction » de la table)

1. **EVOSCM : trois énoncés de la pièce sont contredits par des pages qu'elle dit avoir lues (p. 27, 29), et deux pages décisives ne sont pas lues (p. 18, 28).** La pièce écrit : « la validation est faite par l'agent […] sans test statistique », « aucune règle de promotion à seuil », et classe EVOSCM en « non trouvé » pour (iv-b). Or :
   - p. 27 : « with uniform evidence weights, irrespective of any confidence values reported by the LLM » ; « the runtime supplies a compact JSON state containing the current hypothesis population, posterior weights, recent prediction errors » ; « EvoSCM executes only the feasible design with the largest posterior-weighted predictive disagreement » ; « the runtime tracks a set of systematic audits rather than trusting the most familiar initial law ». Les poids ne sont pas ceux du modèle de langue ; un programme les tient.
   - p. 29 : « Reliability is updated using pre-committed prediction error and parent-child delta-sign accuracy » ; « withheld from the planner when their calibrated reliability falls below 0.20 ». C'est une règle à seuil, sur une statistique nourrie par l'erreur de prédictions engagées d'avance.
   - p. 18 (non lue par l'auteur) : « Posterior odds: finite / vanishing » (figure 6 : 5,98 × 10^18 contre 1) ; « Pre-committed predictions favor the finite-core hypothesis » ; « their estimated reliability remains below the acceptance threshold ».
   - p. 28 (non lue) : « against observation-derived causal evidence before accepting the submission » (contrôle par le runtime avant d'accepter la loi finale). p. 30 : « every prediction is stored before its outcome is observed ».
   - Commandes : `pdftotext -f 27 -l 27 arxiv-2609.01526/2609.01526.pdf - | grep -n -i 'runtime\|evidence weights'` ; `-f 29 … | grep -n '0.20\|Reliability'` ; `-f 18 … | grep -n -i 'odds\|acceptance'`. Résultat : tous présents.
   - **Statuts justes** : (iii) EVOSCM = **voisin** (cotes a posteriori entre hypothèses concurrentes sur prédictions engagées, seuil de fiabilité 0,20), absent de la ligne (iii) de la pièce ; (iv-a) voisin, plus fort que dit (engagement repris en p. 27, 29, 30 et dans une ablation, p. 17) ; (iv-b) **voisin**, non « non trouvé » ; ligne « conjonction », colonne « voisin » : EVOSCM y manque, alors qu'il réunit (i), un engagement avant l'issue et des poids tenus hors du modèle de langue. C'est, des six pièces, la plus proche de (i)+(iv-a)+(iv-b) réunis.
   - **Ce qui reste vrai** : pas d'e-processus, pas de validité à tout instant d'arrêt, pas de contrôle d'erreur, pas d'empreinte, pas de nul formé de l'archive. Le mode de calcul des poids n'est pas dans le PDF (« likelihood » : zéro occurrence ; p. 27 : « Complete prompt templates and schemas are included in the released code ») : le code n'est lu ni par l'auteur ni par moi, et (iv-b) ne peut pas être dit « pris ».
   - R8 : le « non trouvé » de la pièce sur EVOSCM ne repose pas sur une lecture assez profonde. À refaire : lecture entière des p. 17-19 et 26-31.

### Majeurs

2. **WAHL : « non trouvé » pour le principe P est trop faible, et la p. 8 qui le décide n'est pas lue.** La pièce cite elle-même p. 7 « ModelSMC is tasked with inferring additional ion-channel mechanisms that improve model specification » (modèle de Hodgkin et Huxley de base), puis range WAHL en « non trouvé » pour P. Algorithme 1, p. 4 : entrée « initial particle and weight (m0 , w0 = 1) » ; p. 8 : « The unextended base model itself receives comparably low weights », « is consistently outperformed by IM extensions » ; légende p. 8 : « comparing the baseline HH model to the best model identified in the selected run » ; p. 3 : « candidate models are evaluated via marginal likelihoods or Bayes factors ». Le modèle en vigueur est donc pesé, par vraisemblance marginale calculée hors du modèle de langue, contre les extensions que celui-ci propose : rapport de vraisemblances marginales, c'est-à-dire un facteur de Bayes de substitution. Statut juste : P = **voisin** (comparaison au modèle en vigueur, sans test ni seuil d'erreur) ; « voisin lointain » (section 2.4) est trop faible : c'est le voisin le plus proche de (iii) parmi les six. « sans seuil de décision » est inexact à la lettre : p. 4 « If the ESS is below a threshold » déclenche un rééchantillonnage qui écarte les particules de faible poids (ce n'est pas un seuil de promotion). Commande : `pdftotext -f 8 -l 8 arxiv-2602.18266/2602.18266.pdf - | grep -n -i 'base model'`.
3. **BEYOND : « un découpage temporel, pas un engagement » est contredit par la p. 12, lue par l'auteur.** p. 12 : « Our evaluation protocol is pre-committed before iterative search begins. » ; p. 16 : « determined by a set of pre-defined thresholds ». Le statut « voisin » de (iv-a) reste juste (engagement affirmé, non scellé, données déjà existantes), mais la phrase de la section 2.1 est fausse et la citation qui décide manque à la table.
4. **BEYOND : « Les valeurs numériques de τ ne sont pas trouvées dans les pages lues » est faux pour le seuil de signification.** p. 34 (dans les p. 1-47 dites lues en entier, et page que la pièce cite) : « we eschew the traditional t > 2.0 threshold » ; éq. 6.1 ; « By requiring a t-stat of 3.0 ». La valeur de τecon, elle, n'est pas trouvée (mes termes : « threshold » p. 13, 14, 16, 18, 28, 34). Portée : ce seuil confirme que la porte teste contre « aucun effet » avec une correction d'essais multiples, non contre le connu ; cela appuie le statut de la pièce, mais le « non trouvé » est inexact (R8).
5. **BEYOND : la réponse « non » et le nœud 1 sont dits trop fort.** L'éq. 3.10 (p. 16) et l'algorithme 1 (p. 13) n'ont en effet que t_IC et Sharpe. Mais p. 35 rattache l'apport marginal **à la porte de promotion** : « Our agent emulates this skepticism by incorporating a multiobjective promotion gate », dont la première propriété est celle que la pièce cite (apport marginal sur les cinq facteurs), suivie de « By filtering for marginal information gain » ; p. 34, à la première personne : « Furthermore, we evaluate the factor’s contribution to reducing pricing errors ». La citation qui fait ce lien est dans la liste de l'auteur et a été retirée de la note. L'article se contredit ; la lecture juste est « affirmé comme partie de la porte, **calcul non montré** », non « affirmé, non calculé » (table, ligne P) ni « sans terme d'apport marginal » (nœud 1). Le statut « voisin » tient ; on ne peut pas exclure sur pièce que le filtre existe dans le code. p. 55 confirme que les alphas ajustés sont a posteriori, sur le portefeuille composite : « not spanned by existing common risk factors ».
6. **NMV : deux inexactitudes, toutes deux dans le sens qui minore la pièce.** (a) « Le modèle de langue n'y propose pas les hypothèses » : il ne propose pas les **signaux**, mais il écrit les hypothèses après coup : p. 5 « contain different hypotheses and economic “explanations” while maintaining consistency with the empirical findings » ; p. 11 « Proposes economic mechanisms justifying the signal’s predictive power » ; p. 2 « industrialize HARKing ». (b) P en « voisin » avec « (filtre humain, avant le modèle de langue) » : l'étape des six facteurs est un crible statistique par programme, p. 9 « only 183 signals (1.1%) remain statistically significant » ; seule la dernière étape passe par une revue (« After reviewing these results », p. 10). Statut juste : P = **pris, hors modèle de langue** (comme FGX dans la note d'englobement), à taille fixée (5 %, p. 9), sans engagement ; (i) = voisin reste juste.

### Mineurs

7. **ATLAS : « le mot LLM ne figure qu'en bibliographie (p. 10) » repose sur un faux positif.** `grep -n 'LLM'` sur le texte entier : zéro. Insensible à la casse : « Hullman » (p. 10) et « Zollman » (p. 12), deux noms d'auteurs. Ce qui figure vraiment : « Generating computational cognitive models using large language models », référence [9], p. 10. La conclusion (pas de modèle de langue) tient.
8. **Profondeurs mal redites dans la phrase de bornage de la section 3.** « p. 7-34 de ACES » : ACES a 30 pages, et les p. 2-3 ne sont pas lues non plus ; « p. 10-55 de WAHL (hors p. 9) » omet les p. 2 et 8 (constat 2) ; « p. 7-34 d'EVOSCM n'ont été lues que par recherche de termes » contredit la section 2.5, qui dit les p. 8-9, 27, 29 lues, ce que le constat 1 rend douteux pour les p. 27 et 29. Les termes cherchés ne sont listés que pour BEYOND, ACES et WAHL, pas pour ATLAS, EVOSCM ni NMV.
9. **Vérificateur de l'auteur.** Son en-tête dit « mode brut » ; la commande est `pdftotext <pdf> -`, sans `-raw`. Il compare les seuls caractères alphanumériques, casse ignorée : plus lâche que nécessaire (30 sur 31 passent au niveau strict). Il compare l'empreinte au champ de la liste, non au compagnon (je l'ai fait : conforme). Il ne contrôle pas que la liste couvre la note (un écart dans chaque sens, section 2).
10. **ACES, (i) « pris » est généreux** : p. 4 « we use an LLM πθ to generate operator priors » ; les équations sont ajustées par régression symbolique. Le modèle de langue propose des sous-espaces, non des hypothèses ; la pièce le dit en 2.2 mais la table l'oublie. De même EVOSCM p. 29 : sur un des trois bancs, « Each hypothesis is a bootstrap sparse ridge mechanism fitted independently for each property outcome ».
11. **Provenances.** Quatre adresses arXiv non versionnées ; « dernière version au relevé » n'est pas vérifiable hors réseau (la version lue dans l'en-tête, elle, est exacte). `nber-w33363/provenance-v1.md` n'a pas de ligne d'outil. La provenance de BEYOND dit encore « Lue par passages seulement (p. 13, 34-35) » : un complément est à créer, sans écraser. La recherche par titre de la version de la revue n'a pas de trace gardée.
12. **Fichiers de refus SSRN** : ils gardent la valeur d'un témoin de connexion posé par le pare-feu (`set-cookie: __cf_bm=…`, expiré trente minutes après). Ce n'est pas une clé ; à signaler à Lazar, non modifié par moi.
13. **Fenêtre** : la pièce dit 09:13:59Z à 09:18:11Z, soit quatre minutes douze secondes pour 241 pages dont 47 « lues » de BEYOND ; les relevés des PDF vont de 09:14:13Z à 09:16:11Z. Je le rapporte sans en tirer de conclusion ; les constats 1, 3 et 4 montrent des pages dites lues dont le contenu décisif n'est pas rendu.
14. **Table, ligne (ii), colonne « non trouvé »** : juste à ma profondeur. À préciser : WAHL et EVOSCM tiennent une **population pondérée** de modèles, voisin de « mise en commun », déjà rangé en « voisin » ; rien à changer.

## 5. Refus SSRN

Bien dit, non contourné. Deux fichiers, une tentative chacun, même seconde (09:14:13Z), `HTTP/2 403`, `cf-mitigated: challenge`, corps « Just a moment... ». Aucune copie de SSRN 6474601 ni de 6569258 prise ailleurs dans `lecture-o4-v2/` (`ls` des deux dossiers : le fichier de refus et son compagnon, rien d'autre). La version NBER de Novy-Marx et Velikov n'est pas un contournement : c'est une autre source, libre, et la pièce dit trois fois que ce n'est pas le texte de la revue. Le nœud 2 (« libre hors du dépôt » ne peut être dit tant que les deux SSRN ne sont pas lus) est bien posé.

## 6. Nœuds de revendication

- **Nœud 1 (BEYOND)** : à reformuler (constat 5). Poser les deux lectures à Lazar : éq. 3.10 sans terme d'apport marginal ; section 6.3 qui le met dans la porte, sans formule.
- **Nœud 2 (SSRN)** : bien posé.
- **Nœud manquant, EVOSCM** (constat 1) : un système à modèle de langue avec prédictions engagées avant l'issue et poids tenus hors du modèle, à citer comme voisin de (i)+(iv-a)+(iv-b) ; décision de Lazar : l'ajouter ou non au point 5 de la section 0 de la note d'englobement, qui ne donne aujourd'hui l'engagement avant observation qu'à Ma et al.
- **Nœud manquant, WAHL** (constat 2) : comparaison par vraisemblance marginale au modèle en vigueur, pour des propositions de modèle de langue, hors de lui ; voisin de P+(i)+(iv-b).
- La phrase « Aucune pièce lue ici ne contredit le verdict » tient pour le verdict « occupée en partie » ; elle ne tient pas pour « ces quatre pièces ne changent rien » : deux d'entre elles ajoutent des voisins que la note d'englobement n'a pas.

## 7. Ce que je n'ai pas fait

Pas de lecture entière d'aucun PDF ; code d'EVOSCM, de BEYOND et de WAHL non lu ; aucune source nouvelle cherchée (pas de réseau) ; SSRN 6569258, SSRN 6474601 et la version de la revue de Novy-Marx et Velikov restent non lus.

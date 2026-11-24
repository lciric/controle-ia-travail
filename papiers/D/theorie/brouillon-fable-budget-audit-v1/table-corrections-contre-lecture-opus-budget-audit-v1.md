# Table des corrections après la contre-lecture de la section sur le budget d'audit et l'audit tiré au hasard (papier D) — v1

- Date : 24 novembre 2026. Auteur des corrections : Claude Fable 5.2, effort élevé, sur les décisions de la session qui orchestre.
- Pièce corrigée : `audit-budget-section-v1-correctif-5.tex` (même dossier), SHA-256 `8632aa52be052ce61e43bc6497e95dad35925b6405e06a9dcb18fcdd5d17e316`. Le correctif 4 n'est pas modifié (empreinte conforme à son compagnon).
- Rapport suivi : `papiers/D/audits/contre-lecture-opus-section-budget-audit-v1/contre-lecture-opus-section-budget-audit-correctif-4-v1.md`.
- Entrées bibliographiques à ajouter : `bib-a-ajouter-budget-audit-v1.tex` (même dossier), SHA-256 `18f44b62648afd66b7f0f55f0847a6dc4e9f40b7518810978c8e53c0e0c31020`.
- Les trois fichiers neufs ne sont pas scellés : aucun compagnon `.sha256` n'a été écrit, le scellement revient à la session qui orchestre.
- Aucun énoncé, aucune preuve et aucun exemple chiffré du correctif 4 n'a changé de contenu. Les phrases mathématiques neuves sont listées au § 5 : elles n'ont pas été contre-lues.

## 1. Statut par défaut

Les numéros de ligne renvoient au correctif 5.

| Défaut | Statut | Emplacement | Justification |
|---|---|---|---|
| D1, dépendance à une section absente | corrigé | l. 18-40 (chapeau), l. 44-112 (dynamique, lemme, strate visible), l. 157-164 (limite statique) | Le lemme `lem:audit-logodds` est autonome : la récurrence est définie dans la section (`eq:audit-dyn`), son point fixe est la loi de Gibbs de l'opérateur B, donc la référence sans moniteur quand le moniteur est aveugle ; `L` est défini ; l'abandon de la strate visible est dit exact pour le rapport des logits ; « the static analysis » devient un renvoi au régime R3 de `thm:escape`. Plus aucun renvoi hors du manuscrit de base. |
| D2, environnements non définis | corrigé hors de la section | § 3 de cette table ; rappel en commentaire, l. 5-9 | Selon la décision : la section ne définit rien. Les trois lignes de préambule sont au § 3. |
| D3, conflits de notation | corrigé | toute la section ; liste au § 2 | Pénalité d'audit, erreurs du test, taux du test, probabilité qu'un audit rate, nombre total d'épisodes, avantage de la strate furtive et « Operator~B » sont alignés sur le manuscrit. |
| D4, « 138 configurations » pour une grille de 144 | corrigé | l. 545 | 144 configurations, dont 6 où la marge dépasse la marge de manœuvre (ε > c) : l'hypothèse de (c) y échoue, le théorème n'y garantit rien ; 138 simulées. Recalculé par `verif_c5.py` : 144 points, 6 avec ε > c, tous à n = 100, γ = 0,2, η = 1, pénalité 19. |
| D5, « a margin is necessary » | corrigé | l. 545 et l. 531-533 | « some positive margin is needed; the order of ε is not claimed » ; la remarque `rem:audit-random` dit « a margin of the order of ε » et renvoie à la remarque de simulation. |
| D6, marge empirique et quantité économisée | corrigé ; ajout facultatif rejeté | l. 545 | La marge empirique est dite oracle, calibrée par simulation à paramètres connus, au niveau δ/2 du processus sans plafond, sur 137 points ; « nothing here shows that it could be used in practice » ; l'économie porte sur le nombre moyen d'audits B_ε, non sur le nombre réservé ; « at most δ/2 ». Rejeté : le surcoût de 2,7 à 101 % et la part reprise par la marge oracle, calculs du contre-lecteur non scellés (R6). |
| D7, clés bibliographiques | partiellement corrigé | l. 624-627 ; fichier des entrées | Clés alignées : `greenblatt2023`, `griffin2024`, `wen2024`. Vingt entrées `\bibitem` au format du manuscrit fournies pour les autres clés. Reste à faire, hors de cette pièce : inscrire Gans et Holden, et Zhu, Zuo et Sun, au registre des références (je ne modifie aucun fichier existant). |
| D8, références non confirmées, antériorité manquante | partiellement corrigé | l. 498, 535, 615-618, 627 ; réserves au § 4 | Zhang et Parkes 2008 retirée du texte. Antériorité de l'audit d'élection ajoutée comme travail voisin, sans chiffre ni formule. « low-stakes alignment ». « Two recent preprints ». Numéro de théorème de Boucheron et constante attribuée à Freedman retirés du texte. Blocki et al. cités par arXiv. Partiel : aucune lecture sur PDF n'a été ajoutée ; les réserves sont au § 4. |
| D9, notes de travail dans le texte | corrigé | l. 498, l. 627, l. 632 | Plus aucune mention « to be checked », « to locate and verify », « no reference checked », ni de réserve de lecture. Les trois voisins sans référence sont retirés ; une seule phrase de limite reste (« We have not searched systematically… »). Les réserves sont au § 4. |
| D10, commentaires périmés | corrigé | l. 1-14 | En-tête réécrit : ni chemin du dépôt, ni identifiant interne, ni état périmé. Le bloc bibliographique en commentaire est retiré (remplacé par le fichier des entrées). |
| D11, provenance de la remarque | partiellement corrigé | l. 537-543 | Un seul commentaire : nom du script, empreinte complète des sorties, empreinte du verdict ; je les ai recalculées sur la branche `origin/lecture/seuil-papier-d-v1`. Reste à faire, hors de cette pièce : verser le verdict sur la branche du papier ; nommer le script parmi les scripts compagnons du manuscrit. Ce commentaire porte des noms de fichiers internes : à retirer avant le dépôt des sources. |
| D12, précisions mineures | corrigé (points 1, 2, 3, 5) ; point 4 sans objet ; point 6 rejeté | l. 341 ; l. 568 ; l. 524 ; l. 545 | 1 : « no such safe direction in γ », avec un contre-exemple par direction (§ 5). 2 : « the worst stratum … (τ_aud = 0) ». 3 : « asymptotically negligible ». 5 : l'inégalité maximale ne s'applique telle quelle qu'à η = ∞. 4 : rien à changer, « fixed before any draw » reste exact. 6 : facultatif, hors des quatre retouches demandées ; le chiffre est au verdict scellé, l'ajout reste possible. |

## 2. Renommages (D3)

| Objet | Correctif 4 | Correctif 5 | Raison |
|---|---|---|---|
| pénalité d'audit | `C` | `C_{\mathrm{aud}}` | `C` est la pénalité d'interception de l'opérateur B |
| pénalité du moniteur dans la boucle | `C_{\mathrm{loop}}` | `C` | notation du manuscrit |
| pénalité d'audit quand l'audit rate | `C'` | `C_{\mathrm{aud}}'` | suit le renommage |
| pénalité d'audit sous indistinguabilité imparfaite | `C_\delta` | `C_{\mathrm{aud}}^{\delta}` | suit le renommage |
| erreurs de première et de seconde espèce | `\alpha`, `\beta` | `\mathrm{err}_{\mathrm I}`, `\mathrm{err}_{\mathrm{II}}` | `\beta` est la survie au moniteur, `\alpha_{\mathrm h}` le taux de fausse alerte |
| taux vrai et taux de l'alternative du test | `\varepsilon'`, `\varepsilon` | `\vartheta`, `\vartheta_1` | `\varepsilon` reste la marge du théorème de l'audit tiré au hasard |
| probabilité qu'un audit rate | `\varepsilon_a` | `\varepsilon_{\mathrm{aud}}` | reliée à `\varepsilon_{\mathrm{trap}}` du régime R3 |
| nombre total d'épisodes | `T` | `N` | `T` est le nombre de tours de rejet répété |
| nombre d'audits réalisés | `N` | `\hat B` | libère `N` |
| avantage de la strate furtive | `\Delta R`, `\Delta R'` | `\Delta R_{\mathrm f}`, `\Delta R_{\mathrm f}'` | notation du manuscrit |
| strates | `h`, `f`, `v` | `\Pi_{\mathrm h}`, `\Pi_{\mathrm f}`, `\Pi_{\mathrm v}` ; indices `\mathrm h`, `\mathrm f` | notation du manuscrit |
| taux de triche sur les épisodes audités | `\tau_A` | `\tau_{\mathrm{aud}}` | l'indice A évoque l'opérateur A ; relié à `\tau_{\mathrm{trap}}` du régime R3 (ajout de ma part, non demandé par le rapport) |
| majorant de la variance dans la preuve | `v` | `\sigma^2` | `v` est la strate visible (ajout de ma part) |
| indice de tour dans la remarque détection et dissuasion | `\pi_k(f)` | `\pi_j(\Pi_{\mathrm f})` | `k` y est déjà le nombre d'épisodes trichés (ajout de ma part) |
| récurrence | logits `\theta_k` | inclinaison `\phi_k = \theta_k - \theta_0`, équation `eq:audit-dyn` | définie dans la section, valable sur l'espace général du manuscrit |
| « operator~B » | minuscule | « Operator~B » | graphie du manuscrit |

Inchangés, compatibles avec le manuscrit de base : `\rho`, `\tau`, `\eta`, `\gamma`, `\delta_{\mathrm{ind}}`, `G_k`, `\Gamma_K`, `\kappa`, `W`, `c`, `K`, `n`. Si la section de dynamique entre plus tard dans le manuscrit, ses propres `\rho`, `\tau`, `G`, `\Gamma` et `N` seront à renommer de son côté ; `G_k` vaut ici `\eta\lambda_k` avec son `\lambda_k`.

## 3. À ajouter au manuscrit lors de l'insertion (D2, D7)

Préambule, sur le compteur commun :

```latex
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}\newtheorem{definition}[theorem]{Definition}
```

Bibliographie : les vingt entrées de `bib-a-ajouter-budget-audit-v1.tex`, soit `aslam2007`, `avenhaus2002inspection`, `becker1968crime`, `blocki2013audit`, `boucheron2013concentration`, `christiano2021lowstakes`, `deng2019strategizing`, `dresher1962sampling`, `freedman1975tail`, `gans2026randomized`, `hoeffding1963probability`, `lecam1973convergence`, `rakhsha2020poisoning`, `rivest2006`, `serfling1974probability`, `tambe2011security`, `wen2024`, `yao1977probabilistic`, `yu1997assouad`, `zhu2026blindfold`. Les clés `greenblatt2023` et `griffin2024` existent déjà.

Autres retouches du manuscrit que l'insertion appelle, non faites ici : le résumé et la section des limites disent le modèle « static » et classent la dynamique en temps fini parmi les problèmes ouverts ; la note de première page nomme les scripts compagnons, sans le script de la simulation.

## 4. Réserves de vérification, à lever avant diffusion (D8, D9)

| Objet | État | À faire |
|---|---|---|
| Zhang et Parkes 2008 (`zhang2008policyteaching`) | NON_CONFIRMEE au registre v2 ; **retirée du texte** | à vérifier avant diffusion sur les actes d'AAAI 2008 si l'on veut la citer |
| Aslam, Popa et Rivest 2007 (`aslam2007`) | NON_CONFIRMEE au registre v2 ; titre donné par la page de Rivest selon le second vérificateur ; initiales et nom de l'atelier écrits de mémoire | à vérifier avant diffusion : notice et PDF |
| Rivest 2006 (`rivest2006`) | notice confirmée (registre v2, PDF hors du dépôt, empreinte `b883153080a38213…`) ; ce que le texte lui attribue (la question de la taille d'un audit statistique) n'a pas été lu sur PDF par moi | lire le PDF ; aucune formule ni aucun chiffre n'en est tiré |
| Boucheron, Lugosi et Massart 2013 | livre confirmé ; le numéro « Theorem 2.10 and Corollary 2.11 » est retiré du texte | lire le numéro sur PDF, puis le remettre |
| Freedman 1975 | notice confirmée ; la constante « 2bt » est retirée du texte, qui dit « another constant in the linear term » | lire le théorème sur PDF, puis remettre la constante |
| Blocki et al. 2013 | arXiv confirmé ; le lieu IJCAI 2013 n'est pas lu, l'entrée cite arXiv | lire le lieu, ou garder arXiv |
| Affirmations attribuées à Avenhaus et al., Dresher, Tambe, Blocki et al., Becker, Yao, Le Cam, Yu, Hoeffding, Serfling, Greenblatt et al., Griffin et al., Wen et al., Christiano, Rakhsha et al., Deng et al. | notices concordantes au registre v2 ; affirmations non lues sur PDF | lecture sur PDF avant diffusion (R7) |
| Gans et Holden ; Zhu, Zuo et Sun (« Blindfold ») | lus sur PDF par le programme (`docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-sept-voisins-opus-v1.md`, § 2.2 et § 2.1 ; PDF `docs/sources/pdf/attaquant-informe-v1/2609.38262v1.pdf`, `e28a4e8d6747cf4dc4c0c3433836f5e29b1ab5e235be3176841ee9c4db4ed7a7`, et `2610.37055v1.pdf`, `5250fa1176ac804ba32fd4998fa47b2f278757ce9393a1443d4b9a7b8617f861`) ; absents du registre v2 ; prépublications non évaluées | les inscrire au registre |
| Trois voisins sans référence, retirés du texte | pilotage d'apprenants par des paiements sous budget ; jeux d'inspection où l'inspecté apprend ; récompenses rares auditées et repondérées par l'inverse de la probabilité d'audit | à chercher avant diffusion ; le texte dit seulement que la recherche n'a pas été systématique |
| Dernier apport revendiqué : le plancher sous `\delta_{\mathrm{ind}}` | le texte ne revendique plus que son expression dans cette dynamique (« we do not claim the floor itself ») | à confronter à Gans et Holden et à « Blindfold » avant de le garder comme apport : c'est une revendication, donc une décision de Lazar |
| Volumes et pages des entrées | huit notices relues sur Crossref et trois sur arXiv le 24 novembre, auteurs de « Blindfold », de Gans et Holden et de Wen et al. lus sur la première page des PDF du dépôt ; relevé non scellé | à repasser par le script du registre |

## 5. Phrases mathématiques neuves, non contre-lues

1. Dynamique (l. 44-83) : inclinaison exponentielle `eq:audit-dyn` ; forme proximale (maximiseur unique de `\gamma\E_\pi[r_k]-(1-a)\DKL(\pi\|\pi_0)-a\DKL(\pi\|\pi_k)`) ; identification au gradient naturel en softmax tabulaire ; itéré égal à la loi de Gibbs à la pression `\eta(1-a^k)` ; point fixe.
2. Lemme et preuve reformulés sur l'inclinaison (l. 85-112) : la conclusion `eq:audit-logodds` est inchangée.
3. Limite statique (l. 157-164) : à taux constant, `x_k = (\Delta R_{\mathrm f}-W\rho)G_k` ; la limite est le rapport des logits de l'opérateur B du régime R1 avec `\beta_{\mathrm h}=1`, `\beta_{\mathrm f}=1-\rho`, `C=C_{\mathrm{aud}}` ; le seuil est `C^*_{\mathrm{R3}}` à `\varepsilon_{\mathrm{trap}}=\delta_{\mathrm{ind}}=0`.
4. Critère final et pas γ (l. 341) : avec `\hat\gamma=\eta>\gamma`, le plan concentré en fin d'horizon laisse `x_K-c=a(\Delta R_{\mathrm f}G_{K-1}-c)` ; avec `\hat\gamma<\gamma` et η = ∞, il est infaisable dès que c > 0 et que des audits sont nécessaires. Démontré à la main ; contrôlé en quatre points par `verif_c5.py` (2,099152 contre 0,98 × 2,141991 au premier).
5. Remarque de simulation (l. 545) : sans marge, la trajectoire en champ moyen du plan juste à temps est sur le seuil (partie (i) du théorème de dissuasion) ; à η = ∞ l'écart `\hat\ell_k-\ell_k` est une martingale en k.

## 6. Compilation d'essai

- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/budget-audit-c5/`. Copie du manuscrit `main-v4-correctif-4.tex` (empreinte conforme, `f027233f7c7ba11f1499e5751c2245abbd03c2ffd54b41adf0f3061f44fe8d6c`) ; fichier d'essai `essai-insertion-c5.tex` : les trois lignes de préambule du § 3, la section insérée avant « Limitations and Open Problems », les vingt entrées ajoutées à la bibliographie.
- Résultat, trois passes de `pdflatex` : **aucune erreur, aucune référence indéfinie, aucune citation indéfinie, aucun label en double** ; 22 pages ; la section occupe les pages 11 à 19 et n'a aucune boîte trop large. Les deux boîtes trop larges du journal (9,9 pt et 3,8 pt) sont dans le manuscrit de base, pages 5 à 8.
- Empreintes : `essai-insertion-c5.pdf` `53e416480bd5316aa61f11e832bdd026b7614dcb2cd3d79528df2443b35f562e` ; `essai-insertion-c5.log` `f6211ac3e1d54149cec4cc1ce4f94b4ab795f4f81b5e966e22977abb77836577`.
- Outils du même dossier, non scellés : `build_c5.py` (`5aa2eedcbcf81fe9e83b47f097c8da28dc706694472f1a52e8afe19b53176fb6`), qui produit le correctif 5 à partir du correctif 4 par remplacements exacts et comptés ; `verif_c5.py` (`327a0f59d92f65913348b6b79b3b3481e163c4034511ec69d0999d8df1171750`). Le dossier est provisoire : à verser si l'on veut garder la trace.
- Contrôle du périmètre : une fois les renommages du § 2 inversés, le correctif 5 ne diffère du correctif 4 qu'aux passages listés aux § 1 et 5.

## 7. Vu, hors mandat, non touché

- La proposition `prop:audit-indist` commence par deux phrases de commentaire dans son énoncé (« This situation does not arise… ») et porte des exemples chiffrés dans sa partie (b) : à sortir de l'énoncé lors d'une prochaine passe.
- Orthographe : la section est en graphie britannique (« favours », « randomised »), le manuscrit mêle les deux ; les passages neufs suivent le manuscrit pour « optimization », « normalized », « maximizer ».

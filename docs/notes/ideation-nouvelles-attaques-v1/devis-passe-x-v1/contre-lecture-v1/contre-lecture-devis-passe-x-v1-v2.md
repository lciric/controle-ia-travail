# Contre-lecture du devis de la passe X rallongée (v1) — contre-lecteur Opus neuf, v2

Date : 2026-11-22. Processeur seul : aucun appel de modèle, aucun réseau, aucune dépense, rien écrit hors de ce dossier.
Pièce : `C/devis-passe-x-v1/devis-passe-x-v1.md`, son programme et son JSON (trois compagnons vérifiés : OK).
Base imposée par la coordination pour le point 5 : R-4852 (lecture de la mère, non lue par moi : `decisions.md` hors de ma liste) — passe X : tout appel Anthropic sur Luc, sous GO-46 ; course : juge et espèce 3 restent sur Minuit, sans crédit, bloqués.

## Verdict

**À corriger.** Les chiffres tiennent (rejeu égal à l'octet ; 96,80 est bien le pire qu'impose la lettre). Quatre points bloquants : l'analyse de Luc et de sa clé, le « point bloquant » de la note devenu caduc, le moment de la passe X, et la réserve sur `go.md`, périmée.

## 1. Rejeu et contrôles

- Rejeu sous `python -I` : sortie égale à l'octet au JSON livré (`cmp`). Empreintes des trois pièces égales à leurs compagnons.
- **La note annonce « sept contrôles » (l. 5). Le JSON n'en porte que cinq (J l. 2-8).** Erreur de la note.
- `QN_QA_empreintes_egales_additif` est écrit `True` en dur (programme l. 197). Il est vrai, puisque l'assertion de la l. 110 a passé avant, mais ce n'est pas un contrôle calculé.
- `cinq_especes_egal_54_45_de_X_10` est presque une tautologie : au pire de lettre, neuf tentatives font toujours 9 × 6,05. Le contrôle ne vérifie que le compte des tentatives.
- `regle_google_tenue` (hors des contrôles) est une **tautologie** : P ≥ (P − 32 000) + 16 000 est vrai quel que soit P. La règle G-6 n'est pas éprouvée contre une sortie maximale réelle.
- Arithmétique recalculée à la main, conforme :
  - 116 783 = (6,05 − 0,21082) × 20 000 ;
  - pire par tentative : 5,02 (10/50) ; 4,16 (Google) ; 2,51 (Opus 4.6) ; 1,51 (Sonnet 4.6) ;
  - cas haut des espèces 3 et 4 : 5,92 ;
  - Luc : pire calculé 30,08, pire de lettre 72,60 (douze tentatives) ;
  - 256,01 = 124,35 + 131,66 (AC l. 56-57).

## 2. Pièce fusionnée et « mot pour mot » (GO-37)

- **Corps.** Rejoué : 19 921 signes, 20 570 octets, empreinte `d93f1ec6…`. « quarantaine » : 1 fois dans le titre de la pièce du lot, 0 dans son corps.
- **Mot pour mot.** Les corps sont repris à l'octet, guillemets compris. Le « mot pour mot » de GO-37 (go.md l. 724) tient pour les corps.
- **Retrait des titres : extension de règle à déclarer.** X-3 de l'additif (AV l. 186) ne retire que « les titres qui nomment un modèle » (R-4815, Q4). La pièce retire les neuf titres. Quatre d'entre eux ne nomment aucun modèle : billet-drapeau, cœurs, étau-équipe-rouge, théorème négatif. Le retrait est sage, car ces titres décrivent les correctifs du test de devinette. Mais c'est un écart à X-3 : il doit être déclaré comme tel, non présenté comme « la lettre de X-3 ».
- **À noter, pèse sur X-8.** La fusion n'a ni séparateur ni étiquette. Elle contient cinq listes numérotées qui repartent à 1, et deux « 6. » : celui de QA (« « 6. ») et celui de cœurs-algorithmiques (ligne 21 de la pièce fusionnée). Conséquences :
  - « la question 6 de la pièce QA » (X-8 proposée) n'a pas de référent univoque pour le proposeur ;
  - le rangement « par pièce » suppose une attribution que la requête ne permet pas ;
  - ajouter une étiquette serait « un mot ajouté », ce qu'interdit X-3.
  Il faut trancher : séparateurs déclarés dans l'enveloppe (K-2 (5)), ou rangement par la session à part, déclaré non fiable.

## 3. Plafond de sortie de 96 000 jetons

- **Justification.** Elle est raisonnable : environ 32 000 jetons de texte visé, une réserve de réflexion, et une borne de 116 783 jetons sous 6,05 USD au tarif de 50 USD par million.
- **Sorties maximales.** Aucune n'est relevée, sauf celle que la note donne pour Claude 4.6, non relue. Manquent : espèces 1 et 5 (Google), espèce 2 (OpenAI), espèces 3 et 4, Kimi.
  - **Sonnet 4.6** : de mémoire, non opposable, sa sortie maximale serait de 64 000 jetons, non de 128 000. Si c'est le cas, 96 000 est refusé. Sous A6, une erreur sans réponse arrête la chaîne : le second repli tomberait en erreur.
  - **Kimi** : RQ l. 52 relève des fins à 32 768 jetons et une réponse tronquée à 32 000 (DEP l. 305) ; c'est un indice de limite basse.
  - **Google** : si la sortie maximale est d'environ 65 000, la règle de repli de la note (réflexion au plus la sortie maximale moins 32 000) s'applique ; à relever.
- **Flux.** De mémoire : à ce plafond, le kit d'Anthropic exige le flux pour un appel long. C'est un réglage A7 à fixer.
- **Règle de Google.** Elle est tenue dans la lettre (réflexion au plus 64 000, texte au moins 32 000). Mais G-3 (AV l. 113) exige que **le pire d'un appel Google soit mesuré sous la garde** avant le scellement ([PIRE-G-PROPOSEUR]). Le chiffre de 4,16 est un calcul, non cette mesure. De plus, la facturation de la pensée n'est établie nulle part (RQ l. 37).

## 4. Pire de lettre (96,80) ou pire calculé (44,40)

- **La lettre impose 96,80.**
  - P4 et P15 (AV l. 129, l. 143) : 6,05 par tentative de proposeur, « non baissé ».
  - X-10 (AV l. 193) : P_X = somme des pires par tentative, au plus grand de 6,05 et du pire Google mesuré.
  - Avec seize tentatives : 16 × 6,05 = 96,80.
  - Le pire calculé (44,40) n'est que de l'information.
  - La condition est que le pire Google mesuré reste sous 6,05 (G-3).
- **Répartition par clé** : Luc 72,60 ; Google 12,10 ; OpenAI 6,05 ; Kimi 6,05. La somme fait 96,80, juste.
- **GO-46** (go.md l. 733) : « au plus 200 USD », « remplace la ligne de 55 USD ». C'est conforme.

## 5. Clé qui paie les ajouts Claude et les replis ; effet sur Luc

- **GO-45 (go.md l. 732) ne couvre que des appels à Fable déjà accordés.** Le texte de GO-46 ne nomme aucune clé. La seule base est donc R-4852, sous GO-46. **La note cite à tort « Luc (GO-2026-11-22-45) »** (table § 3, programme l. 70) : il faut citer R-4852 et GO-46.
- **Réserve 1 de la note périmée.** `go.md` contient désormais GO-45 et GO-46 (734 lignes, `7cdfb9e8…`). La note dit les avoir pris au mandat sur une copie de 730 lignes (`c40f3671…`). Il faut la réancrer.
- **Le « point bloquant » de la note tombe.** La lecture « espèce 3 de la course sur Luc » est écartée sur la base donnée : la course reste sur Minuit. La part de 136,04 n'est donc pas menacée par ce chemin, et le chiffre de 256,01 ne s'applique pas.
- **Bloquant, absent de la note : la charge de Fable que GO-45 met sur Luc.**
  - GO-45 met sur Luc : demande 27 (8 USD), demandes 28 à 30 (montant non chiffré), relance (17), mathématiques (50), banc (24), chantiers (18). Cela fait au moins 117 USD aux plafonds, demandes 28 à 30 non comptées.
  - Avec un reste déclaré de 153 (PL), la tolérance de 16,96 aux lots ouverts (PL l. 76) est dépassée dès avant la course.
  - Or la part vaut le reste moins le pire des lots non clos (R-4289). Elle tombe donc sous 124,35 : c'est le nœud L-2 (CV l. 116).
  - La passe X ajoute 72,60 au pire de lettre et 30,08 au pire calculé.
  - Elle ne tient que par la recharge automatique : dite par Lazar (GO-40 ; GO-42, « la laisser agir »), mais contraire à « aucune recharge supposée » (GO-30). L'arrêt n° 11 lit pour Luc un « reste déclaré », et la ligne fixe de Luc dans AC l. 141 parle d'un « reste calculé ».
  - Il faut donc une lecture « compte payant » de Luc, par un complément neuf (sur le modèle de R-4303) et le mot de Lazar. Ce mot est à demander, non à supposer.
- **Écart non déclaré.** L'espèce 3 de la passe X serait payée sur Luc alors que son rôle de course est sur Minuit. La seconde clause du n° 12 (V9 l. 383) arrête « un appel d'un rôle sur une autre clé que la sienne », sans bascule. Le texte proposé pour X-11 doit déclarer cet écart.
- **Contradiction à signaler à la mère.** GO-43 dit « mathématiques : pas d'appels API » ; GO-45 met les mathématiques (50 USD) sur Luc.

## 6. Lieux de l'additif proposés

- **La phrase sur le lot en quarantaine est présente** (§ 4, X-3). Elle est juste sur le fond : GO-46 la sert « avec réserve sur le mot de Lazar ». Deux corrections :
  - la réserve citée vient de GO-37 (« orientée faiblement ») ; GO-46 dit « orientée au test de devinette » ; citer les deux ;
  - « servie telle quelle » doit dire « corps seul, titre retiré ».
- **L'objection d'ancrage de LQ n'a pas de réponse.** LQ l. 28 dit que servir cette question « heurterait K-1 et le cloisonnement de la matière première ». Le § 4 ne répond que sur le mot. Le corps décrit la famille tenue à l'écart : il faut une phrase qui dise pourquoi K-1, qui vise les candidats de mode, n'est pas en cause.
- **Lieux manquants :**
  - G-3 et [PIRE-G-PROPOSEUR] pour la passe X ;
  - G-1 : garde Google, avec `mots=None` ;
  - la seconde clause du n° 12 (espèce 3 sur Luc), et le n° 13 pour Luc ;
  - la valeur de l'enveloppe, 512 octets, à geler (K-2 (5)) ;
  - la table des valeurs du § 11 (P_X et sa clé) ;
  - les jeux A7 et les exigences A1 à A6 pour Kimi : relais, champ de refus, champ du modèle servi ;
  - l'écart à X-3 sur les titres (voir § 2) ;
  - la règle de LQ selon laquelle le compte de Kimi « ne sert à rien d'autre pendant la course » (TK § 2), à concilier avec la passe X.

## 7. Autres erreurs qui fausseraient une décision

- **Moment de la passe X, bloquant pour Q9.** Q9 (a) place la passe X « après la génération 3 ». Or la course est bloquée sur Minuit, sans crédit. De plus, GO-46 échoit le 2026-11-26, avant la fin de la course (27 novembre, GO-30). Sous (a), la passe X peut ne jamais partir, ou partir hors GO. Le moment doit être tranché à part.
- Sur « après la course, environ 16,96 sur Luc » : c'est le reste si la part entière est consommée, non le reste attendu (28,65 au cas haut).
- Les tarifs d'Opus et de Sonnet 4.6, et ceux de Google et d'OpenAI, ne sont pas vérifiés. Cela reste sans effet sur le pire de lettre tant que chaque tentative reste sous 6,05.

## Bloquant / à noter

- **Bloquant**
  - B1 : la clé de la passe X est mal citée ; la réserve sur `go.md` est périmée.
  - B2 : la charge de Fable mise sur Luc par GO-45 est absente, et la recharge automatique n'a pas de lettre ; nœud L-2.
  - B3 : l'écart à la seconde clause du n° 12 n'est pas déclaré.
  - B4 : le moment de la passe X (Q9 (a)) dépend d'une course bloquée et d'un GO qui échoit le 26 novembre.
- **À noter**
  - Cinq contrôles et non sept ; un contrôle écrit en dur ; deux contrôles tautologiques.
  - L'extension de X-3 aux titres est à déclarer.
  - Le « 6 » est ambigu dans la pièce fusionnée (X-8).
  - Sorties maximales non relevées ; Sonnet 4.6 à 64 000, de mémoire.
  - Le pire Google n'est pas mesuré (G-3).
  - Lieux manquants (§ 6) ; objection d'ancrage de LQ.
  - Contradiction entre GO-43 et GO-45 sur les mathématiques.

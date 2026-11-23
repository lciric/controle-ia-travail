# Contre-lecture indépendante — réponse d'une page à l'article « Diffuse AI [Artificial Intelligence, intelligence artificielle] Control on Fuzzy Tasks » et rédaction de l'objection 1 (version 1)

- **Date et heure (temps universel coordonné)** : 23 novembre 2026 (sous-agent neuf mandaté par la session mère sous l'accord sur les dossiers prioritaires `GO-2026-11-23-17`, l'accord sur les décisions de l'entretien `GO-2026-11-23-32` et l'accord de délégation temporaire `GO-2026-11-23-33`).
- **Auteur** : sous-agent neuf en remplacement temporaire de lecteur vérificateur (classe C, pièce de travail sans dépense de calcul, sans appel réseau, sans modification du dépôt).
- **Branche et pièces contre-lues** (`origin/dossier-entretien/reprise-2026-11-23-v1`, dossier `docs/notes/dossier-entretien-2026-12-01-v1/reponse-objection-surveillance-v1/`) :
  - la réponse d'une page à l'objection sur la surveillance contre les menaces diffuses (`reponse-objection-surveillance-diffuse-v1.md`, empreinte cryptographique de hachage sûr à 256 bits (`SHA-256`) `9aac8d6b6af129fd2d656b7c3efd25eb06a6c17e4f05d8a52c4c675bb7e8e6e1`, conforme à son compagnon) ;
  - le texte de remplacement de l'objection 1 de la section 5 de la note d'entretien (`objection-1-v7-redaction-v1.md`, empreinte `b450a22fed288efba41a9a11162dabf4ddf2b15da3583687302965b3dbacb454`, conforme à son compagnon) ;
  - les notes du rédacteur Claude Fable 5.2 (`notes-redacteur.md`, empreinte `288d9b5a37674f48356ae9729dd58d8cef1d370f8e3d945e2ec3698858629f49`, conforme à son compagnon).
- **Méthode indépendante** : toutes les sources primaires sur la branche principale (`main`) ont été contrôlées par leurs compagnons d'empreinte cryptographique à 256 bits, puis extraites à nouveau indépendamment avec les utilitaires `pdftotext -layout` et `pypandoc`, sans réutiliser les fichiers extraits déposés dans la branche du rédacteur. Aucun répertoire de résultats du programme (`runs/`, `diag/`, `donnees/`, `docs/verdicts/`) n'a été ouvert.

---

## Verdict d'ensemble

**Conforme sous retouches mineures.**

Les deux textes sont factuellement exacts sur l'ensemble des sources primaires et des décisions du programme vérifiées sur `main`, ne fuient aucun résultat du programme et respectent le plafond de longueur. Cinq remarques de précision et de discipline d'écriture (toutes non bloquantes, aucune erreur factuelle sur les sources) sont consignées ci-dessous ; elles ne s'opposent pas à l'intégration immédiate de l'erratum 1 de la note d'entretien version 6 avant la relecture de Lazar demain matin à 08 h 47 en temps universel coordonné.

---

## 1. Contrôle d'intégrité, de pagination et de longueur

1. **Empreintes cryptographiques de hachage sûr à 256 bits (`SHA-256`)** :
   - Les trois fichiers de la branche `origin/dossier-entretien/reprise-2026-11-23-v1` concordent à l'octet avec leurs compagnons `.sha256`.
   - Les vingt fichiers sources et décisions cités sur la branche principale (`main`) concordent à l'octet avec leurs compagnons `.sha256` et avec le relevé des empreintes au lancement (`docs/sha256sums-lancement-v2.txt`) : le préimprimé de Terekhov et collègues version 3 (`arxiv-2606.08892.pdf`, `8858355c…3b4beb`, 84 pages) et version 2 (`2606.08892v2.pdf`, `aea0f2d1…9a`), le billet de Vivek Hebbar (`web-hebbar-2025-how-can-we-solve-diffuse-threats.html`, `6831b0ab…d7401a`), la page web au format hypertexte (`HTML`) de Gasteiger et collègues (`web-gasteiger-2025-automated-researchers-sandbag.html`, `4a7e0eb9…dad7e5`), le préimprimé de Gan et collègues version 2 (`arxiv-2604.16286.pdf`, `833a48e6…161cc0`), la lecture des trois sources (`lecture-trois-sources-controle-diffus-v1.md`, `18ccba98…09f273`), la note d'entretien version 6 (`note-entretien-controle-diffus-v6.md`, `c28b4da6…18479f`), la carte des voies version 2 et son erratum 1, ainsi que les décisions sur le masquage des positions et l'invariant d'entraînement (`N-053`), les bases à battre et les modes d'attaque (`N-056`), le cycle de reconception (`N-062`), le plancher d'audit et les deux regards (`N-075` version 3 et ses errata), la loi de la référence honnête (`N-076` et son erratum 1) et le texte du programme version 2 (`docs/programme-controle-ia-v2.md`, `2fd63bad…5aa18c`).
2. **Pagination exacte selon la règle d'interdiction de citer un chiffre ou une page sans vérification sur le document d'origine empreinté (règle `R7`)** : sur toutes les pages citées de Terekhov et collègues version 3 (pages 2, 6, 9, 25, 26) et de Gan et collègues version 2 (pages 1, 3, 5, 6, 8, 10, 11, 24, 29, 37), le rang physique de la page dans le document au format portable (`PDF`) tiré par `pdftotext -layout` est strictement égal au numéro de page imprimé en pied de page.
3. **Compte de mots de la page de réponse (`reponse-objection-surveillance-diffuse-v1.md`)** : entre les repères `<!-- début de la page -->` et `<!-- fin de la page -->`, le décompte par jetons séparés par espaces contenant au moins une lettre ou un chiffre donne exactement **799 mots** ($\le 800$), conforme au décompte annoncé dans `notes-redacteur.md` (point 1). À noter à titre purement technique qu'un découpage lexical qui scinde les traits d'union et virgules numériques (`1,5-3x`, `p. 25-26`, `N-075`) donnerait un compte légèrement supérieur (804 jetons), sans conséquence pratique si la règle retenue est celle des mots blancs à caractère alphanumérique.

---

## 2. Vérification exhaustive des 13 chiffres, des 12 citations anglaises, des absences et des 7 extraits de décisions

### 2.1 Les 13 nombres et grandeurs factuelles

Tous vérifiés à la lettre sur nos propres extractions de `main` :
- **Gasteiger et collègues (5 grandeurs)** :
  1. `16 tâches` d'apprentissage automatique (citation verbatim de la source anglaise : « implement solutions for 16 machine learning (ML) coding tasks », section « Setup » de la première partie).
  2. `note de 1 à 10` (« gives a suspiciousness score between 1 and 10 », section « Setup »).
  3. `quatre moniteurs` (« We use these same four models to monitor transcripts » — Claude 3.5 Sonnet (new), Claude 3.5 Haiku, Claude 3 Sonnet et Claude 3 Haiku, section « Setup »).
  4. `meilleur de cinq` (« best-of-5 transcripts », section « Mitigations »).
  5. `1,5 à 3 fois` (« around 1.5-3x higher probability than with random sampling », section « Mitigations »).
- **Gan et collègues version 2 (8 grandeurs)** :
  6. `9 dépôts` (« 9 ML research codebases », page 1 et page 3).
  7. `11 sabotages` (« for a total of 11 sabotages », page 3).
  8. `une personne` (« created by one human attacker (the lead author) », page 3).
  9. `trois modèles` (« LLMs [large language models, grands modèles de langage] from three major providers », page 5 : Claude Opus 4.6, le modèle transformateur génératif préentraîné `GPT-5.2`, et Gemini 3.1 Pro).
  10. `31 personnes` (« We recruited 31 human auditors », page 6).
  11. `0,77` et `42 %` (« an AUROC [area under the receiver operating characteristic curve, aire sous la courbe caractéristique de fonctionnement du récepteur] of 0.77 and a top-1 fix rate of 42%, achieved by Gemini 3.1 Pro », page 1 et page 7).
  12. `0,68` et `deux heures` (« After 2 hours, they achieved an AUROC of 0.68, statistically above chance », page 8).

### 2.2 Toutes les citations anglaises (12 principales et sous-citations de la table)

Chaque citation anglaise figurant dans le corps de `reponse-objection-surveillance-diffuse-v1.md`, dans la table de vérification de 31 lignes et dans `objection-1-v7-redaction-v1.md` a été vérifiée par correspondance exacte (après normalisation typographique des apostrophes, guillemets et césures de fin de ligne) sur nos extractions indépendantes des sources de `main` : **100 % concordantes** (aucune altération de sens ni troncature trompeuse). Le seul extrait non réouvert par le rédacteur lui-même dans la note (Taylor et collègues, page 9 pour la mention dans Terekhov et collègues, et la concession de la note d'entretien version 6 sur l'objection 3) est explicitement signalé comme repris de la note version 6, et nous avons de surcroît vérifié directement sur le fichier `docs/sources/pdf/2512.07810v1.pdf` (pages 3, 4, 16, 18, 25) que toutes les citations de Taylor et collègues visées par l'objection 3 sont exactes.

### 2.3 Vérifications d'absence et contexte des trois sources

- **Terekhov et collègues version 3 (`arxiv-2606.08892.pdf`)** : le terme `monitor` / `monitoring` n'apparaît dans le corps du texte qu'à la page 2 (la phrase citée) et en bibliographie aux pages 13 et 14 (ainsi que dans la note de bas de page de citation, sans retour en défense active). Le détecteur de sous-rendement de la page 6 et des pages 25–26 est bien présenté comme l'expérience la plus proche de la surveillance (« la plus proche », prudence justifiée par le rédacteur faute de lecture intégrale des 84 pages) et lit uniquement du texte.
- **Billet de Vivek Hebbar (30 avril 2025)** : zéro occurrence du mot `monitor` dans le fichier source au format hypertexte brut et dans le texte extrait ; zéro occurrence de `probe` et d'`activation` dans le texte extrait ; aucune expérience ni chiffre mesuré.
- **Page web de Gasteiger et collègues (mars 2025)** : zéro occurrence de `probe` et d'`activation` dans le texte extrait. Le rappel est bien présenté uniquement en courbes dans les figures sans valeur numérique dans le corps du texte. Correction essentielle portée par le rédacteur et confirmée sur la source : il est faux de réduire la page à « un modèle faible », puisque les quatre modèles utilisés comme moniteurs incluent Claude 3.5 Sonnet (new), c'est-à-dire le modèle du saboteur lui-même (« We use these same four models to monitor transcripts », section « Setup »), même si l'introduction formule l'intention générale par « so we use weaker models as monitors » et que Claude 3.5 Sonnet obtient une courbe à peine meilleure sur les expériences (« is only slightly better ») mais un classement jugé convenable sur les justifications préliminaires (« performs decently », section « Research decision steering », « Mitigations »). Remarque complémentaire : une note annexe « Claude 3.7 Sonnet » (fin du texte de Gasteiger et collègues) indique que Claude 3.7 Sonnet a aussi été testé en tant que saboteur (capable de sabotage sans exemple contrairement à Claude 3.5 Sonnet), mais les quatre moniteurs cités restent bien ceux listés sous « Setup ».
- **Renvoi à la source dans Gasteiger et collègues** : la phrase « However, the noisy monitoring signal might be sufficient to train away sandbagging » figure bien dans la liste « We find: » placée en tête de page (avant la séparation vers la section « Experiment sandbagging »), et non sous un intertitre « Abstract » ou « Résumé ». La correction de « résumé » en « liste des résultats en tête de page » (ou « liste « We find » en tête de page ») est donc strictement exacte.
- **Distinction « détecter » / « incriminer »** : seul Gan et collègues emploie le terme `incriminate` (page 10) ; Gasteiger et collègues parle de `using them as detectors` et d'empêcher le sous-rendement à l'inférence (`prevent one-shot sandbagging at inference time`). Le remplacement de « trop faible pour incriminer » par « trop faible pour détecter (Gasteiger et al.) ou pour incriminer (Gan et al., p. 10) » dans la rédaction version 1 de l'objection 1 améliore la précision factuelle et s'aligne sur la note marginale déjà présente sous la phrase 10 de la note version 6.

### 2.4 Extraits des 7 décisions et du programme, et absence totale de fuite de résultats

- Tous les extraits des décisions sur le masquage des positions textuelles et l'invariant d'entraînement (`N-053`, points 1 et 5), les bases à battre et les deux modes d'attaque (`N-056`, points 1 et 6), le cycle de reconception et le rapport de tous les cycles (`N-062`, points 1 et 5), le rôle d'accélérateur et d'aiguillage et l'absence de garantie sur un genre jamais vu (`N-075` version 3, § 2, et son erratum 3 version 2, § 4.1), la loi de la référence honnête (`N-076`, § 2), ainsi que la phrase de l'hypothèse de gain de l'accès interne sur tâches floues (`docs/programme-controle-ia-v2.md`, ligne 93) sont vérifiés mot pour mot sur `main`.
- **Aucune fuite de résultat du programme** : aucune mesure chiffrée issue de courses, diagnostics ou verdicts n'apparaît dans la page de réponse ni dans l'objection 1. Les deux textes restent strictement bornés aux règles décidées et à l'état « aucun résultat cité ».

---

## 3. Constats de forme et remarques pour la suite (tous mineurs, non bloquants)

1. **Acronymes et identifiants cités dans les deux brouillons (remarque mineure)** : dans `reponse-objection-surveillance-diffuse-v1.md`, les identifiants des décisions et hypothèses sont tous nommés en clair avant leur sigle entre parenthèses (par exemple « gain de la boîte blanche sur la noire, H1 »), sauf dans `objection-1-v7-redaction-v1.md` où `(N-075, § 2 ; phrase 8 de la section 3)` gagne à expliciter le nom de la décision (`la décision sur le plancher d'audit et les deux regards, N-075, § 2`), et où le sigle anglais non développé `ML` subsiste à l'intérieur du titre de section cité `« Manipulating ML experiments »` (titre propre de la page anglaise de Gasteiger et collègues). Dans la table de la réponse, la mention de l'archive ouverte `arXiv 2604.16286` (et dans le paragraphe introductif « note v6 ») peut aussi être explicitée en toutes lettres. À porter comme retouche rédactionnelle, déjà appliquée dans l'erratum 1 proposé ci-joint.
2. **Cohérence interne de la note d'entretien version 6 hors de la seule objection 1 (constat à porter dans l'erratum 1)** :
   - La **phrase 10 de la section 3** (ligne 132 de `note-entretien-controle-diffus-v6.md`) conserve encore les deux imprécisions corrigées dans l'objection 1 : la référence `(Gasteiger et al., résumé ; Gan et al., p. 10)` au lieu de `(Gasteiger et al., liste « We find » en tête de page ; Gan et al., p. 10)`, et le raccourci « trop faible pour incriminer » attribué aux deux études (même si la note marginale à la ligne 134 explique l'écart « empêcher / incriminer » pour le lecteur seul). Pour une cohérence parfaite lors de la relecture de Lazar demain matin, l'erratum 1 proposé ci-joint corrige également cette phrase 10.
   - Le document compagnon **`lecture-trois-sources-controle-diffus-v1.md`** (section 2, lignes 32 et 34 ; section 4, ligne 49) contient le même raccourci (« un modèle plus faible lit la transcription » au lieu des quatre moniteurs dont Claude 3.5 Sonnet lui-même) et la même mention `(résumé)` / « trop faible pour incriminer ». Un erratum 1 séparé est produit à cet effet.
3. **Suite prévue par les décisions du 23 novembre** : la lecture sur document au format portable des 16 articles sur le thème « saboteur et sondes » (consignée à la ligne du journal de décisions `R-5185` sur la branche `origin/lecture/papiers-saboteur-sondes-v1`, ayant reçu l'accord d'intégration à l'accord `GO-2026-11-23-32`) prévoit quatre corrections futures dans une version 4 de la décision sur le plancher d'audit et les deux regards (`N-075`) et deux nuances dans un prochain erratum de la décision sur la référence honnête (`N-076`). Aucune de ces modifications à venir n'invalide les citations de `N-075` version 3 (erratum 3 version 2) ni de `N-076` (§ 2) employées dans la réponse et l'objection 1 (qui portent sur le rôle d'accélérateur/aiguillage, l'absence de garantie sur un genre jamais vu et la déclaration de la référence honnête).
4. **Rappel du point laissé à Lazar sur la phrase « ni chez nous »** : dans `objection-1-v7-redaction-v1.md`, la phrase « Sur une tâche difficile à noter, je n'ai trouvé aucune mesure de sonde, dans aucun sens, ni chez eux ni chez nous » reste reprise de la note version 6 telle qu'écrite le 21 novembre (Fable n'ayant ouvert aucun résultat du programme) ; si des mesures de sondes sur notre banc existent ou sont scellées d'ici le 1er décembre, la mère devra relire ce segment la veille de l'entretien, conformément à la règle de l'en-tête de la note version 6.
5. **Relecture finale** : la phrase « Des sondes ont été essayées ailleurs : Taylor et al., cités p. 9, sur des tâches à réponse claire, résultats mêlés (note v6 ; non relu par moi) » a été consolidée ici par vérification directe des pages 3, 4, 16, 18 et 25 du préimprimé de Taylor et collègues version 1 (`2512.07810v1.pdf`).

---

## 4. Ligne de vérification résumée

- **Empreintes vérifiées** : 3 sur 3 fichiers de la branche de reprise ; 20 sur 20 fichiers cités sur `main` (tous conformes).
- **Chiffres** : 13 sur 13 vérifiés exacts sur les sources brutes.
- **Citations anglaises** : toutes vérifiées exactes sur nos propres extractions `pdftotext -layout` et `pypandoc`.
- **Extraits de décisions et programme** : 7 sur 7 vérifiés exacts sur `main`.
- **Cloisonnement** : zéro ouverture de résultats, zéro résultat cité.
- **Décision recommandée** : accepter la réponse d'une page telle quelle (ou avec retouche purement facultative de développement d'identifiants) et sceller l'erratum 1 de la note d'entretien version 6 et l'erratum 1 de la lecture des trois sources.

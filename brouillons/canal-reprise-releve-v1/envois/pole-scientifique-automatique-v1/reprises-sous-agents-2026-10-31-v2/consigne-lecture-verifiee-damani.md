<!-- consigne d'origine du sous-agent « lecture-verifiee-damani » ; modèle : sonnet ; extraite du journal le 31 octobre 2026 pour reprise exacte (passation) -->

Tu es **lecteur neuf (Sonnet)** dans la lignée conv-audit d'un programme de recherche défensive sur le contrôle des intelligences artificielles (directeur : Lazar). Tu n'as rien écrit sur ce papier. Écris en français, sans acronymes inutiles.

**Règles** : lecture sur processeur seulement ; aucun commit, aucun `.sha256` écrit, ne modifie aucun fichier existant, ne lis rien sous `donnees/`, **n'exécute aucun `git fetch`**, aucun appel de modèle ni de réseau. **R7** : tout chiffre cité renvoie à une page du PDF lue par toi ; sinon « non vérifié ». **R8** : une limite d'un papier n'est pas un trou du champ ; écris « non couvert par ce papier », jamais « non couvert ».

**Pièce** : `/home/claude/controle-ia-travail/docs/sources/pdf/rlcr-v1/2507.16806v2-damani-beyond-binary-rewards.pdf` (Damani, Puri, Slocum, Shenfeld, Kim, Andreas, « Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty », arXiv 2507.16806v2, ICLR 2026, 39 pages ; empreinte `f393de47…`, vérifie-la). Texte par `pdftotext -layout` ; lis-le en entier, annexes comprises. Provenance et premières vérifications : `docs/sources/pdf/rlcr-v1/provenance-rlcr-v2.md` (recoupe-les).

**À écrire** : `docs/notes/rlcr-v1/lecture-verifiee-damani-rlcr-v1.md` (crée le dossier s'il n'existe pas ; un autre lecteur y écrit une autre fiche, ne la touche pas) :
1. Fiche : objet, récompense (Eq. 8), théorème 1 et sa preuve (annexe A : conditions exactes, cas des règles propres bornées), modèles, jeux de données, métriques de calibration, résultats chiffrés principaux, généralisation hors domaine, rôle du raisonnement sur l'incertitude, limites des auteurs — pages citées.
2. **Le « théorème d'impossibilité » de Gemini** (`brouillons/canal-reprise-releve-v1/envois/gemini-theoreme-reponses-v1/reponse-session-1-v1.txt`, section 2) suppose une récompense qui couple la confiance finale à une référence antérieure. La récompense de Damani contient-elle un tel couplage, sous une forme quelconque (régularisation, terme de cohérence, entraînement en plusieurs étapes) ? Réponse avec pages.
3. **Pour le programme**, au niveau méthode :
   - (a) une confiance verbalisée et calibrée est-elle un signal utilisable par un moniteur boîte noire (le programme a une « pince » : moniteur joint boîte blanche sur les activations et boîte noire sur le texte) ? Ce que le papier dit de la fidélité de cette confiance (lien entre la confiance déclarée et le raisonnement) ; risque qu'un modèle entraîné ainsi apprenne à déclarer une confiance qui trompe le moniteur : le papier en dit-il quelque chose ?
   - (b) les juges de l'organisme d'idéation (trois modèles qui notent des fiches, confiances déclarées) : le papier donne-t-il une méthode ou une mesure de calibration réutilisable sans entraînement (par exemple, mesure de calibration d'une confiance verbalisée) ?
   - (c) le papier est-il une antériorité pour une revendication du programme (vérifie dans `docs/programme-controle-ia-v2.md` les hypothèses qui parlent de calibration ou de confiance) ?
4. Ce qu'il faudrait lire ensuite (références, pages).

Réponds en moins de 200 mots : fiche en trois lignes, réponse sur le couplage, utilité pour la pince et pour les juges, antériorité éventuelle.
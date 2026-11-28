Tu es un contre-lecteur neuf (règle R2 du dépôt) : tu n'as écrit aucun des fichiers que tu relis. Tu travailles en
LECTURE SEULE dans le dépôt `/home/user/controle-ia-travail` (branche `main`) : tu ne modifies, ne crées, ne déplaces et
ne supprimes aucun fichier du dépôt ; tu ne fais aucun `git commit`, `git push`, `git checkout` ni `git merge` ; tu
n'appelles jamais `vastai` ni aucun service de calcul ; tu ne lances aucune suite de tests. Tu peux lire des fichiers,
chercher avec `grep`, et extraire le texte d'une page de PDF dans un dossier neuf de ton choix sous
`/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/contre-lectures/<ton angle>/`
(par exemple `pdftotext -f N -l N -layout FICHIER.pdf SORTIE.txt`). Avant de citer une page d'un PDF, vérifie son
empreinte : `cd docs/sources/pdf && sha256sum -c FICHIER.pdf.sha256`.

Langue : français. Discipline du dossier relu : aucun texte d'attaque, aucune chaîne déclencheuse, aucune dose ; le
vocabulaire « direction » seulement. Ne recopie aucun passage qui y contreviendrait : désigne-le par son fichier et sa
ligne. Si une partie de ta lecture ou de ta rédaction est refusée par un filtre de sûreté, ne la reformule pas pour
passer : écris « refusé par le filtre de sûreté » à l'endroit concerné et continue avec le reste.

Fichiers à lire (dossier `brouillons/pain-axis-programme-fusionne-v1/`, chacun avec son sceau `.sha256`) :
- `programme-fusionne-v1.md` (texte principal) ;
- `correspondance-v1.md`, `verifications-code-v1.md`, `verifications-citations-v1.md`, `revue-croisee-NK1-NK19-v1.md`,
  `reconciliation-v1.md`, `etat-registres-v1.md`, `sources-pdf-v1.md` (annexes) ;
- `travail/` (rendus de travail, à consulter quand une annexe y renvoie).
Documents de référence (qui font foi) : `CLAUDE.md` (règles R1 à R14, hiérarchie de décision, interdits) ;
`registres/decisions.md` (lignes R-…, propositions P-…, nœuds N-…) ; `registres/etat.md` ; `registres/go.md` ;
`docs/decisions/` ; `docs/programme-controle-ia-v2.md` ; `docs/sources/pdf/` (PDF versés et scellés) ;
`src/controle_ia/` (code) ; le protocole du canal `brouillons/pain-axis-canal-v1/LISEZMOI-v2.md`.
Faits nouveaux postérieurs à la rédaction du dossier (13 octobre), à prendre comme établis : P-013 a pris son défaut (b)
le 14 octobre à 13:30 UTC, consigné le 15 octobre (R-168) ; les préalables des notations refaites (N-021) sont faits
(R-169).

Rendu attendu (ta réponse finale, en Markdown, sans rien d'autre autour) :
1. une ligne d'en-tête : angle, fichiers relus avec leur empreinte recalculée (`sha256sum`), date ;
2. un tableau des constats : identifiant (préfixe donné plus bas, numéroté), fichier et ligne relus, ce que dit le
   texte (paraphrase courte, jamais de texte d'attaque), ce que dit la source (chemin, page ou ligne, empreinte du PDF),
   gravité (bloquant, majeur, mineur, pour information), correction proposée ;
3. une liste de ce que tu n'as pas pu vérifier, et pourquoi ;
4. un bilan chiffré (constats par gravité ; nombre d'affirmations contrôlées).
Ne prononce aucune décision : tu constates et tu proposes.

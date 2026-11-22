# Relevés de la plateforme de modèles avant le réajustement (devis v9, § 5, points 4 et 9) — v1

Releveur neuf, mandat `mandats/mandat-releves-plateforme-reajustement-v1.md` (`7dbb9303c84eab72e3d13edc02bb23572b499a2b3a0d1430f2eb8e3d9a0e4963`).
Date des relevés : 2026-11-22. Pages publiques seulement ; aucune requête avec une clé, aucun compte, aucune donnée du projet
dans les requêtes ; la page de création de clé (derrière connexion) n'a pas été vue.

**Réserve de méthode.** Les pages de documentation ont été lues par un outil de résumé (premiers passages) ; les citations ci-dessous
ne sont retenues « exactes » que si je les ai retrouvées moi-même en texte brut (licence, code `huggingface_hub`, spécification
Xet, protocole LFS, billing). Les passages repris du résumé seul sont marqués « (résumé) ».

## 1. Clé restreinte (point 4) — **probable**
Source : https://huggingface.co/docs/hub/security-tokens ; https://huggingface.co/docs/xet/auth ; fil public de forum
https://discuss.huggingface.co/t/what-boxes-to-check-to-access-hugging-face-tokens/170572.
- Existe : « `fine-grained`: tokens with this role can be used to provide fine-grained access to specific resources, such as a specific
  model or models in a specific organization » (security-tokens, résumé).
- Pour lire un modèle à accès contrôlé : case « Read access to contents of all public gated repos you can access » (libellé donné par le fil de
  forum, non par la documentation officielle). L'accès au modèle doit en plus avoir été accordé au compte (« Request access » sur la page du modèle,
  déjà fait par Lazar à vérifier de son côté).
- Pour écrire sur un seul dépôt : case « Write access to contents/settings of selected repos » (libellé vu seulement par recherche, sources
  tierces) avec le seul dépôt privé choisi dans la liste ; la spécification Xet confirme que le droit sur le contenu suffit pour écrire :
  « your tokens MUST have read or write access to the contents of repositories to be issues read or write Xet tokens respectively »
  (xet/auth, exact).
- Cases à cocher (à confirmer à l'écran par Lazar) : section Repositories : (a) lecture du contenu des dépôts publics à accès contrôlé accessibles ;
  (b) écriture du contenu des seuls dépôts choisis, ce dépôt privé. Rien d'autre (ni facturation, ni webhooks, ni espace de noms entier).
- Non établi : que la lecture d'un modèle à accès contrôlé et l'écriture sélectionnée se combinent dans **une même** clé ; la documentation dit
  seulement que les droits se cumulent par case et que l'accès effectif est borné par celui du compte. Les libellés exacts des cases n'ont pas pu
  être vus sans connexion ; test réel possible seulement par Lazar.

## 2. Stockage privé (point 9) — **établi** (grille publique), coût estimé 0 USD
Source : https://huggingface.co/docs/hub/storage-limits (lu en texte brut le 2026-11-22).
- Compte gratuit : tableau « Free user or org | Best-effort* | 100GB » (stockage privé : 100GB). 31 Go tiennent dans ces 100 Go : **0 USD par mois** si le
  compte est gratuit et aucun autre contenu privé ne dépasse ≈ 69 Go.
- Compte PRO : « 1TB + pay-as-you-go » ; au-delà : « additional private storage is charged ... at a base price of $18/TB/mo » (≈ 0,56 USD/mois pour 31 Go si
  l'on devait payer au-delà d'un palier ; non applicable sous 100 Go ou 1 To).
- Taille maximale d'un fichier : « no single file will exceed 500GB. I.e. 500GB is the hard limit for a single file size. » ; recommandé : « File size | <200GB ».
  Le plus gros fichier du réajustement (≈ 8,46 Go) passe.
- Limites d'envoi : « Files per repo <100k » ; « Commit size <100 files » (recommandé) ; envoi HTTP : « a timeout of 60s is set on the request » par commit ;
  `upload_folder` découpe en commits. Pas de limite par dépôt : « There is no per-repo size limit for models and datasets ».
- Réserve : « Free ... 100GB » est la grille actuelle ; la page dit qu'elle évolue. Le plan du compte de Lazar n'est pas lu ici.

## 3. Empreinte rendue pour un gros fichier (point 3) — **probable : déclarée par l'envoyeur ; recalcul serveur non établi**
Sources : https://raw.githubusercontent.com/huggingface/huggingface_hub/main/src/huggingface_hub/lfs.py ; `_commit_api.py` (même dépôt) ;
https://raw.githubusercontent.com/git-lfs/git-lfs/main/docs/api/batch.md ; https://huggingface.co/docs/xet/upload-protocol ;
https://huggingface.co/docs/huggingface_hub/main/en/guides/upload.
- Voie LFS classique : le client envoie dans la requête de lot `"oid": upload.sha256.hex()` et `"hash_algo": "sha256"` (lfs.py, exact), c'est-à-dire l'empreinte
  **calculée par l'envoyeur** ; puis une étape de vérification : le client rappelle l'adresse `verify` avec `{"oid": ..., "size": ...}` (lfs.py, exact). Le protocole LFS dit
  seulement : « Servers can use this for extra verification, if needed. » (batch.md, exact) : le recalcul n'est pas imposé.
- Voie Xet (par défaut avec `hf_xet`) : « Optionally, compute the SHA256 of the file contents. This is required when uploading to Git-based repositories on the Hugging Face Hub »
  (xet/upload-protocol, exact) ; le serveur vérifie les xorbs : « which will verify the integrity of the xorbs, register the xorb metadata along with the LFS SHA256 hash (to
  support lookup/download) » (guide d'envoi, exact). L'empreinte SHA-256 est donc **enregistrée** comme fournie ; la vérification porte sur les morceaux (hachage propre à Xet), pas
  (d'après ce texte) sur un recalcul de la SHA-256 du fichier entier. `lfs.py` : « When a file is uploaded through the Xet protocol, the SHA256 is computed during upload ... and set afterwards » (exact, côté client).
- Établi : la SHA-256 est calculée côté client et transmise. Non établi : que la plateforme la recalcule à réception (aucun texte public ne l'affirme ni ne le nie).
  Conséquence : ne pas tenir l'empreinte rendue par l'interface comme contrôle indépendant ; relire les octets (téléchargement et recalcul) reste la seule vérification propre.

## 4. Débit en écriture (point 4 du mandat) — **établi pour ce que la documentation dit : aucun chiffre garanti**
Source : https://huggingface.co/docs/huggingface_hub/main/en/guides/upload ; https://huggingface.co/docs/hub/rate-limits.
- Aucun débit ni plafond d'écriture chiffré n'est publié. Dit : « For maximum upload throughput on large files, set the HF_XET_HIGH_PERFORMANCE=1 environment variable.
  This enables hf_xet's high-performance mode, which saturates available bandwidth and CPU cores. » (exact) ; un exemple d'affichage montre « 19.7 MB/s » (illustration, pas une mesure ni une garantie).
- Limites par action (créations de dépôt, commits) : « We don't currently document the rate limits for those specific actions » (limites de débit, exact). Quotas d'API par fenêtre de 5 minutes.
- Pas de mesure faite par moi (mandat).

## 5. Licence de Llama 3.1 (point 5) — **établi** pour le rangement privé ; point d'attention sur la distribution
Source : https://raw.githubusercontent.com/meta-llama/llama-models/main/models/llama3_1/LICENSE (texte public de « LLAMA 3.1 COMMUNITY LICENSE AGREEMENT » ; la copie du dépôt à accès
contrôlé n'a pas été lue : refus 401 sans compte).
- § 1.a « Grant of Rights » : « You are granted a non-exclusive, worldwide, non-transferable and royalty-free limited license under Meta's intellectual property or other rights owned by Meta
  embodied in the Llama Materials to use, reproduce, distribute, copy, create derivative works of, and make modifications to the Llama Materials. » — créer des dérivés et les copier est permis.
- § 5.b : « ... with respect to any derivative works and modifications of the Llama Materials that are made by you, as between you and Meta, you are and will be the owner of such derivative works and modifications. »
- § 1.b.i : les obligations (copie de l'accord, « Built with Llama », nom commençant par « Llama ») sont déclenchées par « If you distribute or make available the Llama Materials (or any derivative works
  thereof) ... ». Un dépôt **privé** n'est pas, à ma lecture, « distribuer ou rendre disponible » ; le texte ne mentionne aucune interdiction de stockage privé. Prudence d'usage : mettre la copie de la licence
  dans le dépôt et nommer les fichiers « Llama… » ; si le dépôt devait devenir public ou partagé, ces obligations s'appliquent.
- Non tranché ici : l'interprétation juridique de « make available » (lecture littérale, pas un avis juridique). Les « lentilles » sont-elles un dérivé des poids ou seulement entraînées sur des activations : la
  clause § 1.b.i parle aussi d'un modèle entraîné à l'aide de « Llama Materials ... outputs » ; dans les deux cas le rangement privé est couvert par § 1.a.

## Les cinq réponses en une ligne
1. Clé restreinte : **probable** — clé à grain fin avec lecture des dépôts à accès contrôlé accessibles + écriture du contenu du seul dépôt privé choisi ; libellés et cumul dans une même clé à confirmer à l'écran par Lazar.
2. Stockage privé : **établi** — 100 Go privés gratuits (compte gratuit), donc ≈ 31 Go à 0 USD/mois ; au-delà d'un palier payant 18 USD/To/mois ; fichier max 500 Go (recommandé < 200 Go).
3. Empreinte : **probable** — SHA-256 calculée et déclarée par l'envoyeur (LFS ou Xet) ; la vérification serveur porte sur les morceaux ; recalcul serveur de la SHA-256 **non établi**.
4. Débit : **établi** (par défaut) — aucun débit ni plafond publié ; seul le conseil `HF_XET_HIGH_PERFORMANCE=1` ; limites par action non documentées.
5. Licence : **établi** — § 1.a autorise copie et dérivés, § 5.b te donne la propriété des dérivés, aucune interdiction de stockage privé ; obligations de § 1.b.i seulement en cas de distribution.

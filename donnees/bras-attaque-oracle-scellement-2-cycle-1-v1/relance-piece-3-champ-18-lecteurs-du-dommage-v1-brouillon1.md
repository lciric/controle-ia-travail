# Relance — pièce 3 : champ n° 18 de la course, lecteurs externes du dommage — v1, brouillon 1

- **Brouillon, non opposable.** Classe A : contre-lecture par Fable 5.2, puis vérification des corrections par le même
  contre-lecteur (mandat v3, section 5). Scellé définitif avant la construction des gardes de l'envoi (course,
  brouillon 17, section D6 ; pièce de sécurité v16, section 3.5).
- Écrit le 2026-11-22 vers 15:00 UTC par le monteur de l'oracle du cycle 1, relance (`session_01XJ6MgmSDBZpPAuXLe3diix`).
- **Sans contenu** : aucune rubrique ne cite un produit, une consigne, un mode, ni la forme de l'oracle. Peut sortir du
  coffre tel quel si la mère le décide.
- Sources, empreintes vérifiées : pièce de sécurité v16 (`b8bcda60ead6f58f…`), section 3.5, table « Ce que chaque
  lecteur déclare » et « Règle de la lecture humaine » ; course, brouillon 17 (`cf5d35d8472137d3…`), D6 ; audit des
  lignées (`main`, `596b5a73453b97ed…`) et sa vérification (`8718c80bee53da35…`) ; registre `R-4668` (Mistral) ;
  copies des pages des fournisseurs versées par le prédécesseur, `sources-conditions-fournisseurs-v1/`, lues le
  2026-11-21 vers 19:01 UTC ; chaque citation ci-dessous a été retrouvée **mot pour mot dans la copie**, par
  programme, le 2026-11-22 à 14:55 UTC.

## 0. Verdict

**Aucun des deux lecteurs proposés ne peut lire aujourd'hui.** Trois raisons, chacune suffisante :
1. la rubrique « Modèle » est vide pour les deux (identifiant exact et version datée non fixés), et le type de compte
   n'est pas établi : « une rubrique vide vaut un lecteur qui ne lit pas » ;
2. la rubrique « Lecture humaine » dit **oui** pour les deux, dans le régime par défaut : règle de la section 3.5 —
   ce lecteur ne lit pas, ou nœud à Lazar (section 3) ;
3. la course veut qu'« aucun lecteur ne soit nommé avant que les deux familles de G1 encore à établir le soient »
   (D6) : l'audit des lignées laisse ouverts quatre sièges (section 2).

Le choix des deux familles, lui, est proposé (prédécesseur, `message-mere-proposition-lecteurs-v2.md`,
`ffc82cb9…`) et non confirmé par la mère.

## 1. Les deux lecteurs, rubrique par rubrique

| rubrique | lecteur 1 | lecteur 2 |
|---|---|---|
| **Modèle** | **vide.** Famille OpenAI, série GPT ; identifiant exact et version datée à fixer au devis, sur la liste des modèles du fournisseur, jamais un alias qui suit la dernière version | **vide.** Famille Google Gemini, hors Neon et hors Gemma ; identifiant exact et version datée à fixer au devis, de même |
| **Fournisseur, point d'accès, type de compte** | OpenAI, interface de programmation (`api.openai.com`) ; région : non établie ; **type de compte : non établi** (clés présentes dans l'environnement de la session sous les noms `OPENAI_API_KEY` et `OPENAI_API_KEY_2` ; quelle clé, quelle organisation, quel régime de conservation : à dire par Lazar ou la mère) | Google, interface Gemini (`generativelanguage.googleapis.com`), **service payant seul** ; **type de compte : non établi** (clés sous `GEMINI_API_KEY`, `_2`, `_3` ; la clé `GEMINI_API_KEY_FREE` est exclue : le service gratuit permet la lecture humaine et l'usage à l'amélioration des produits) |
| **Famille** | lignée OpenAI GPT. Hors de la liste d'exclusion : Llama et Qwen (audit, « Liste finale »), Mistral tant que ces épisodes servent au papier C (R-4668) ; hors Claude, donc sans parenté avec l'auteur de la famille. Attestation conditionnelle : vaut tant qu'aucun des quatre sièges ouverts de la section 2 n'est de cette famille. Terme de N-060 v3 point 1 non tenu : aucun pour la famille ; l'écart est l'envoi à un fournisseur avant la revue externe (GO-2026-11-21-76 ; pièce de sécurité, section 6.4) | lignée Google Gemini. Même attestation, mêmes conditions. Deux sièges à dire, sans exclusion par la règle : un modèle Gemini (Neon) juge les ancres du bras A, et des modèles Gemini ont servi côté attaque ailleurs (audit, incertitude 4) ; Neon est exclu ici, Gemma aussi (poids ouverts : pourrait devenir une base boîte noire locale de G1) |
| **Réglages** | à fixer avec l'oracle figé et à constater par un appel anodin, sur devis : réflexion explicite (niveau ou budget) ; plafond de sortie suffisant pour la réponse entière, sans troncature (une réponse tronquée est un défaut, jamais une réponse) ; aucune limite de mots imposée par l'invite au-delà du plafond ; température la plus basse permise par le modèle ; **stockage des réponses désactivé** (`store` à faux pour `/v1/responses` et `/v1/chat/completions`) | à fixer et constater de même, **sous la règle permanente des appels aux modèles de Google** (`CLAUDE.md` sur `main`, GO-2026-11-21-71) : réflexion explicite dans le corps ; plafond de sortie au moins égal à la réflexion plus 16 000 jetons de texte ; limite de mots de l'invite tenue dans le plafond de texte ; après réponse, zéro jeton de pensée, fin en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé. Les réglages de l'oracle monté par le prédécesseur (2 000 jetons de sortie) ne tiennent pas cette règle : à reprendre |
| **Conservation** | **jusqu'à 30 jours** dans les journaux du contrôle des abus : « abuse monitoring logs are generated for all API feature usage and retained for up to 30 days » ; **pas d'entraînement** : « not used to train or improve OpenAI models (unless you explicitly opt in to share data with us) ». Texte : `platform.openai.com/docs/guides/your-data`, lu le 2026-11-21 vers 19:01 UTC, copie `361792f03668f4d4ff7823102c2a3153b541785b75b51402e5b9d887b8e4c5fe`. Fonctions qui gardent l'envoi au-delà de l'appel, à désactiver quand le choix existe : stockage des réponses, fichiers, fils de conversation, affinage | **55 jours** : « Google retains the following data for fifty-five (55) days for the purposes of detecting and preventing violations of the Prohibited Use Policy » (copie `ad9f490ae1965a28be232c5d5f3a6c770bb5f02f986f11ae291a8f5c55c91784`) ; les conditions disent : « logs prompts and responses for a limited period of time » (`ai.google.dev/gemini-api/terms`, « Effective March 23, 2026 », copie `b2c1aa502cceec1340cadbf9b3f2177d6ed5370d811d3f35fe14db53a6d56fc4`) ; **pas d'usage à l'amélioration des produits** dans le service payant (constat du prédécesseur, `f892fc6c…`). Fonctions à désactiver : contenu mis en cache, fichiers déposés, ancrage sur la recherche de Google (« additional data is collected and used ») |
| **Lecture humaine chez le fournisseur** | **oui** dans le régime par défaut (le régime spécial le dit par contraste : « such content will be excluded from human review unless required by applicable law »). **Régime sans conservation ni revue : il existe, sur approbation d'OpenAI** — « Modified Abuse Monitoring excludes customer content (…) from abuse monitoring logs across all API endpoints » ; « Zero Data Retention excludes customer content from abuse monitoring logs in the same way ». Il ne laisse une revue humaine que par une exception notifiée d'avance, par écrit : « we reserve the right to make models ineligible (…) if reasonably necessary to investigate or prevent severe risk activity, as notified in advance to the impacted customers in writing. In this instance, we may retain and human review customer content ». **En vigueur sur le compte employé : non établi** | **oui**, service payant compris : « When prompts or model outputs are flagged by safety filters and abuse detection systems […], authorized Google employees may assess the flagged content » ; « may be flagged for manual review by authorized Google personnel » (copie `ad9f490a…`). **Régime sans revue : aucun trouvé** dans les deux pages versées ; ailleurs chez Google : non établi |
| **Attestation** | le monteur de l'oracle du cycle 1, relance, `session_01XJ6MgmSDBZpPAuXLe3diix`, le 2026-11-22 ; sans contenu | idem |

**Ce que les questions envoient, à inscrire ici pour le vérificateur** (pièce de sécurité, 3.5, dernier alinéa de la
règle des questions) : avec chaque produit partent le gabarit scellé et les paramètres de la tâche du produit, tirés de
la référence de la tâche, matière de tâche hors coffre. **Leur forme exacte pour cet oracle est suspendue au nœud de la
règle des questions** (`relance-noeud-regle-des-questions-v1.md`, au coffre, `5ab49993…`) ; l'attestation
d'exhaustivité et de provenance sera portée par l'addendum O, non ici, une fois ce nœud tranché.

## 2. Conditions de la famille, ouvertes

L'attestation « famille d'aucun moniteur ni juge qui lira ces épisodes » repose sur l'audit des lignées, que je ne
vérifie pas en lisant les moniteurs (mandat v2, section 4). Elle reste conditionnelle tant que la mère n'a pas établi
la famille de ces quatre sièges, s'ils entrent au préenregistrement de G1 : l'observateur de la base (iv), le juge
robustifié de la proposition P-003, le juge ouvert de grande taille, la lecture de plus grande taille de N-053
(vérification de l'audit, « Liste finale »). Si l'un d'eux est OpenAI ou Gemini, le lecteur de cette famille ne lit
pas, et l'oracle se remonte avant toute lecture (réserve du prédécesseur).

## 3. Nœud pour Lazar : la lecture humaine (sans défaut à 48 heures)

**Décision demandée.** Les deux lecteurs proposés lisent-ils, alors qu'une personne chez leur fournisseur peut lire les
produits que son contrôle des abus signale ?

**Enjeu.** Sans lecteur qui lit, la course ne lit pas son dommage ; la voie d'envoi n'est une lecture, et non un
partage, que si rien n'est rendu lisible à une personne hors du programme (pièce de sécurité, 6.4, troisième trait).

**Options.**
- **(1) Le mot de Lazar, en toutes lettres** : « une personne chez ce fournisseur peut lire ces produits ; l'envoi est
  alors un partage », pour chacun des deux. Avantage : aucune démarche, rien à attendre. Inconvénient : la voie devient
  un partage pour ces lecteurs ; conservation de 30 et 55 jours ; à porter en réserve dans tout rapport.
- **(2) Le régime sans conservation d'OpenAI pour le lecteur 1** (« Zero Data Retention » ou « Modified Abuse
  Monitoring »), demandé par Lazar au fournisseur (contact externe : je rédige si on me le demande, Lazar envoie).
  Avantage : la rubrique devient « non, sauf avis écrit préalable du fournisseur », et la voie reste une lecture pour
  ce lecteur. Inconvénient : délai et accord du fournisseur incertains ; aucun régime équivalent trouvé pour le
  lecteur 2, qui reste sous (1) ou change de fournisseur.
- **(3) Le repli écrit de la course** : un lecteur à poids ouverts sur machine fermée, d'où rien ne sort. Avantage :
  rien ne sort. Inconvénient : lecteur plus faible, modèle neuf, devis et GO ; risque d'entrer dans une base boîte
  noire de G1 ; version nouvelle de la course.

**Recommandation.** (2) pour le lecteur 1 si l'accord peut venir avant les épreuves, sinon (1) ; (1) pour le lecteur 2.
Confiance 0,5. La revue externe d'avant publication couvre cette voie après coup, journal des envois à l'appui
(pièce de sécurité, 6.4, point 4).

**Aucun défaut** : la règle de la section 3.5 l'interdit. Aucun envoi à un lecteur avant ce mot, lisible au registre.

## 4. Ce qui reste à faire, dans l'ordre, pour ce champ

1. La mère confirme les deux familles, ou en propose d'autres ; elle établit les quatre sièges de la section 2.
2. Lazar tranche le nœud de la section 3 (et, pour l'option 2, la démarche auprès d'OpenAI).
3. Lazar ou la mère dit le type de compte et la clé de chaque lecteur.
4. Au devis : relevé de la liste des modèles de chaque fournisseur, identifiant exact et version datée ; relecture
   des pages des fournisseurs, copies versées avec empreinte.
5. Oracle figé, réglages fixés ; appel anodin par lecteur, sur devis (pièce de sécurité, 3.5, condition 3).
6. Contre-lecture par Fable 5.2, vérification des corrections ; scellé définitif, avant la construction des gardes de
   l'envoi.

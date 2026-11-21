# Vérification des corrections — réponses de Fable aux nœuds de l'organisme, v2 — Opus — v1

- **Date** : 2026-11-21T16:35:27Z (`date -u`).
- **Auteur** : Claude Opus 5.5, le contre-lecteur de la v1 (règle R-3735 : la vérification revient au même contre-lecteur). Je n'ai écrit ni la v1 ni la v2. Pièce de travail (classe C). Aucun commit, aucune dépense, aucun refus d'outil.
- **Pièces vérifiées** : 
  - `reponses-fable-noeuds-organisme-v2.md` (`4521273497513cb0de5eecdedfce4a6f088dd367b4e8675cc436d40d463af15e`, compagnon OK) ;
  - les neuf pièces de `pieces-v2/` (compagnons OK) ;
  - les deux PDF et leurs deux sources texte sous `docs/sources/pdf/organisme-noeuds-2026-11-21-v1/` (quatre compagnons OK). Le PDF des erreurs est noté E (`6b8d95a8…`), celui des limites L (`2c96a46e…`).
- **Calcul** : `aires_reseau_illustration_v1.py`, rejoué une fois dans mon bloc-notes, avec `-I`. Sa sortie est égale à l'octet à `aires-reseau-illustration-v1.txt` (`8858cbb5…`).
- **Extractions** :
  - Les commandes de contrôle des neuf pièces de `pieces-v2/` ont été rejouées, parties composées comprises : aucun écart avec la source.
  - La commande du § 1.7 a été rejouée vers un dossier d'essai. Les trois compléments ne portent plus d'arobase après remplissage. Chacun porte, sur sa propre ligne, le commit, l'empreinte et le dossier des sorties (`essai-3`, `-4`, `-5`). Chacun porte aussi sa commande entière.
- **Sources** : les signatures du § 3.3 sont relues dans les PDF, à la page citée :
  - 402 « billing_error » : E, p. 1 ;
  - 429 sans « retry-after », plafond mensuel : E, p. 2 ;
  - « enforced_spend_limit_reached » : L, p. 2 ;
  - 400 « You have reached your specified (workspace) API usage limits », et 429 avec l'en-tête « retry-after » pour l'espace de travail de l'outil : L, p. 3 ;
  - « Not every 429 carries it » : L, p. 8.
  
  Toutes conformes. Pour la conception v5 du véhicule, les lignes 225, 228, 229 et 675 citées au § 5.3 ont été relues à `1b7f6822…` : conformes.

## Verdict

**Conforme.** Les quinze constats sont portés juste, le 5 autrement et à bon droit. Aucun constat neuf de gravité bloquante ou importante.

## Constat par constat

| n° | gravité (v1) | porté | lieu et contrôle |
|---|---|---|---|
| 1 | bloquant | **juste** | § 6.1, § 6.5, § 6.6 ; table des nœuds (ligne 6) ; point 6 du message ; deux pièces de `pieces-v2/`. La v2 tient trois choses. La tolérance de 0,005 de la pièce scellée `dfe0aace…` (l. 30) s'applique d'ici le mot de Lazar. Le passage à 0,02 est un nœud pour Lazar, sans défaut sous 48 heures. Le projet de note d'écart se scelle après ce mot, avant toute lecture de la sortie, et l'issue neuve reste éteinte dans le programme v6 sans l'empreinte de la note. Le point 6 du message de 14:48Z est retiré. L'extraction v1 « la mère la retient » est déclarée caduque. |
| 2 | important | juste | § 1.1, point 5 ; § 1.2, ligne C ; § 1.6, option (b). Le serveur loué est dit écart au point 7 de la liste d'arrêt de la v19 (l. 520, « l'étage est à 0 USD »), en plus d'une dépense. La confiance baisse. L'option (d) neuve (le poste de Lazar) porte ses réserves non vérifiées. |
| 3 | important | juste | § 1.5 et § 1.7. Les textes v4 et v5 sont assemblés, avec leur commande à l'octet. L'heure de la coupure se lit au journal de tenue. L'écart à la décision R-4337 est déclaré dans chaque texte et laissé à la mère. |
| 4 | important | juste | § 1.1, points 3 et 4 ; § 1.3. La projection est dite borne basse (jeu de la garde 27, coût inégal des sources). La garde de la mesure est posée pour n ≤ 1 et pour un manifeste absent, avec son cas sain et ses artefacts. Les confiances sont dites sur la seule étape 4. |
| 5 | important | juste, autrement | § 5.2, § 5.3 (points 1 bis et 2), § 5.4 ; point E8 de l'erratum du lot 6. Le texte servi est séparé des réglages de transport, comme la conception v5 le fait déjà (l. 229). Le relais vérifie ces réglages par valeur, sur un gabarit scellé. La lecture de la v9 ou l'écart est laissé à l'additif. La mère ne tranche que sous deux conditions. |
| 6 | important | juste | § 3.3, points 1, 3, 8 et 9. La table des signatures est faite sur PDF empreinté, pages vérifiées. Le message de crédit cité de mémoire est marqué « non vérifié ». Les réessais sont bornés. Six artefacts de plus sont posés. |
| 7 | important | juste | § 7.5, point 1, et point 7 du message, avec un seul lieu : une branche orpheline sous règle d'ouverture, et rien n'est poussé avant cette règle. La raison vraie de refaire les objets de contrôle (leur exposition passée) est dite. |
| 8 | mineur | juste | § 6.1, § 6.4. Les chiffres neufs sont vérifiés sur la sortie : au pas d'un quart d'écart type, les aires les plus proches sont 0,7011 et 0,8104, à 0,0111 et 0,0104 des aires dites ; au pas d'un dixième, les deux aires voisines sont distantes de 0,0125. |
| 9 | mineur | juste | § 6.3, point 2 : 0,6705, soit un écart de 0,0195. |
| 10 | mineur | juste, élargi | Condition 3 : tout fichier dont le nom commence par « arret », à toute profondeur. |
| 11 | mineur | juste | § 4, points 2, 4, 5 et 7. `PATH`, le point d'accès du relais et le jeton factice sont nommés. L'identifiant d'appel est fait de lettres de « g » à « z » et n'est pas réversible. |
| 12 | mineur | juste | § 8.2 : les comptes bruts sont toujours rendus, avec un plancher de seize fiches. Sous ce plancher, le seuil ne se prononce pas et la mère décide. |
| 13 | mineur | juste | « programme de reprise à l'étape, v1 ». |
| 14 | mineur | juste | Le chiffre est retiré et renvoyé au devis. |
| 15 | mineur | juste (part du concepteur) | Les jetons sont remplis par la commande du § 1.7, avec un contrôle `grep -c '@'`. Le scellement revient à la mère. |

## Remarques sans gravité

- Option (d) du § 1.6 (le poste de Lazar) : la v2 dit bien qu'il n'est pas vérifié que la v19 ne fixe pas la machine. Si Lazar retient cette option, ce point est à lire avant le complément neuf.
- Les quatre extractions de `pieces-v1/` dites encore valables (erratum du lot 10 a, décisions D2, D3, D7) : par sondage, leur texte se retrouve dans la v2.

# Contrôle court du différentiel v2 → v3 — additif des interrupteurs de l'orchestrateur v69 et cadre de la v70 — v1

- Contre-lecteur, modèle O : l'auteur du contrôle v1 → v2 (`controle-differentiel-additif-orchestrateur-v69-v1-v2-v1.md`, `695b980b12d2fc0d71873771dca11600b42e342f6a73ed701790ccc9a9624f37`). Je n'ai écrit ni les pièces v3, ni leurs JSON. Écrit le 2026-11-20 ; relevé de `date -u` : 06:02:59Z, après les vérifications.
- V69 = `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/`. Le message situe ces pièces au commit a256f618 de la branche `lot/compte-organisme-v1` ; je les ai lues sur disque, dans la copie de travail.
- Processeur seul. Aucune écriture dans le dépôt, aucun commit, aucun lancement de l'orchestrateur, du lanceur ni de l'organisme, aucune dépense. Le seul programme lancé est l'outil de remplacement, avec ses sorties dans mon dossier. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**À corriger : cinq corrections de tenue et de cohérence (§ 3, numérotées 1, 2, 3, 3 bis et 4), sans changement de fond.**
- Le rejeu de l'outil rend les deux pièces v3 à l'octet.
- Mes cinq corrections sont portées à la lettre, et rien d'autre ne change hors de la tenue et de l'écart déclaré, que j'accepte.
- La proposition de la correction 5 est au format et fidèle.
- Aucun allumage n'est accordé. Aucun identifiant de modèle (recherche faite sur l'additif v3 et sur le cadre v3).

## 1. Vérifications

**Empreintes.** `sha256sum -c` passe sur les neuf compagnons de V69 : les deux pièces v3, les deux JSON, les deux journaux, les deux différentiels et le rapport. Empreintes recalculées :

| pièce | sha256 |
|---|---|
| additif v3 | `f71e3a551c820ccabf5e7540dba8b4c1d1569386e069e94f0a710bf9d7ce9cba` |
| cadre v3 | `b1822613071f88a50b514ffbb38073ce664038937468a875f4d57838433a9eac` |
| JSON de l'additif | `3a24fc82efe406139f919dfa3935902cd568200df863c066a2dae9d78da99668` |
| JSON du cadre | `2df90ff1963f1e34373389b2a08c6b68d08f1ccf1e16de8dc46f55d0d0015650` |
| rapport | `4446464deb60787d8d2b3544e29824ece1914ace7b0c89841c51fddeedf9da3a` |
| outil | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` (inchangé depuis mon contrôle précédent) |

Les pièces v2 sont intactes : `9d94d23f…` pour l'additif, `216d9bcb…` pour le cadre.

**Point 1 — rejeu.** Additif v2 avec son JSON : « FAIT : 13 remplacement(s) », sortie `f71e3a55…`. Cadre v2 avec son JSON : « FAIT : 5 remplacement(s) », sortie `b1822613…`. `cmp` ne trouve aucune différence avec les v3 de V69 : **égales à l'octet**.

**Point 2 — les corrections.** J'ai lu les deux différentiels en entier.
- **Correction 1** : ligne « Statut » de l'additif et § 3, point 1, du cadre, à la lettre.
- **Correction 2** : § 0, point 4, et § 4.4, à la lettre.
- **Correction 3** : § 1.2, § 5.2 et garde 6, cas sain, à la lettre.
- **Correction 4** : § 4.2, à la lettre.
- **Correction 5** : § 1.2, « reste à établir », point 3, à la lettre.
- Le reste est de la tenue : titres, lignes de version, statut et mandat, où les deux lignes `GO-2026-11-20-10` et `-11` sont citées. S'y ajoute l'écart déclaré.

**Point 3 — l'écart et les points 2 à 8 du § 4 du rapport.**

| point | jugement | correction exigée |
|---|---|---|
| écart 1 : virgule changée en point (rang 12) | accepté. C'est mon défaut : le texte ancien de ma correction 5 commençait après une virgule et le neuf par une majuscule. Le changement est le plus petit qui rende la phrase correcte, il est contigu et déclaré. C'est de la tenue. | non |
| 2 : « la v2 change », dans la v3 | faux nom de version, venu de ma correction 1 | **oui, correction 1** |
| 3 : « récrit en version 3 » | la v3 existe désormais : la phrase désigne mal la version à venir | **oui, correction 2** |
| 4 : quatre mentions restantes de la réserve d'inscription (§ 1.2, deux fois ; § 4.3 ; § 9, réserve 7) | La ligne « Statut » lève la réserve « dans tout ce texte » ; chaque mention reste vraie au sens conditionnel (« si elle est corrigée, cet additif change »). Les récrire serait plus net, mais n'est pas exigé. | non |
| 5 : `GO-2026-11-20-11` citée sur la seule ligne « Mandat » | suffisant : `-10`, point (O3), porte la décision ; `-11` la recoupe | non |
| 6 : trois lieux qui parlent des deux plafonds sans la condition | Deux sont incohérents avec la garde 6 telle que la correction 3 l'a faite conditionnelle. Le § 1.2, « Ce que (a′) lève », dit que le sommet neuf « porte les deux plafonds ». L'artefact de la garde 6, « l'un absent », éprouverait l'absence de `plafond_externe_usd` sur la voie ordinaire, où elle est sans effet (R5). Le troisième, § 9, réserve 1, (b), décrit `jouer_etage` à qui manquent les deux plafonds ; il est vrai (la garde 6 exige au moins `plafond_total_usd`) et peut rester. | **oui, corrections 3 et 4** ; non pour le § 9 |
| 7 : « Aucun des deux rédacteurs » | faux depuis la v3 : il y en a trois, et aucun n'a lu le code. Le fait se répare dans la tenue. | **oui, correction 3 bis**, jointe à la correction 3 au § 3 |
| 8 : deux parenthèses à la suite, § 5.2 | forme seule, le sens est clair | non |

**Point 4 — la proposition de la correction 5 (§ 5 du rapport).**
- **Au format** : décision en une phrase ; enjeu ; trois options, chacune avec avantage et inconvénient ; recommandation et confiance (« élevée », sans chiffre ; les consignes n'en exigent pas, mais un chiffre, par exemple 0,8, serait dans l'usage des autres fiches) ; défaut sous 48 heures, permis, puisqu'il ne porte ni sur une dépense ni sur un allumage.
- **Fidèle à mon jugement** (contrôle v1 → v2, § 1.7) : la correction n'est pas couverte par D2 (a) ; ce n'est pas un nœud ; l'option (a) la tient. L'option (b) est justement dite « un nœud, non une proposition », puisqu'elle changerait la lettre du § 8.4 dans le sens qui facilite le passage. L'option (c) est justement écartée par le plan, § 3.0.
- **Une précision, sans correction.** L'enjeu dit que, sans réponse, la règle de passage ne peut pas se geler. Plus exactement, le défaut (a) la gèle d'office après 48 heures ; la phrase reste vraie avant ce délai.

## 2. Ce que je n'ai pas vérifié

- Je n'ai pas lu le mandat de la v3 (`c4ab6ddb…`), que le message ne m'a pas donné à lire. Le point 4 du rapport en parle ; je le juge sur le texte de l'additif seul.
- Je n'ai pas relu la ligne `GO-2026-11-20-11` : elle était absente de ma copie de `main` lors du contrôle précédent. Rien ici n'en dépend.

## 3. Corrections (texte ancien → texte nouveau), sur l'additif v3, par l'outil

Chaque texte ancien figure une fois exactement dans l'additif v3 (`grep -c -F -e` : 1 pour chacun).

**1.** Ligne « Statut ». Ancien : « si la ligne est corrigée, la v2 change. » Nouveau : « si la ligne est corrigée, cet additif change. »

**2.** § 1.2, dernier alinéa. Ancien : « cet additif est récrit en version 3. » Nouveau : « cet additif est récrit dans une version neuve. »

**3.** § 1.2, « Ce que (a′) lève ». Ancien : « Le sommet neuf porte les deux plafonds dans ses réglages, que `jouer_etage_v57` transmet à l'étage v5 : la garde 6 est tenue avant chaque session. » Nouveau : « Le sommet neuf porte dans ses réglages `plafond_total_usd`, et `plafond_externe_usd` si l'expérimentateur est en session externe, que `jouer_etage_v57` transmet à l'étage v5 : la garde 6 est tenue avant chaque session. »

**3 bis** (tenue, point 7 du rapport). En tête de l'additif. Ancien : « - **Aucun des deux rédacteurs n'a lu le code de l'orchestrateur.** » Nouveau : « - **Aucun des trois rédacteurs (v1, v2, v3) n'a lu le code de l'orchestrateur.** »

**4.** § 6, garde 6, artefact. Ancien : « | l'un absent ; l'un au-delà ; somme des lots au-delà du plafond de l'étage : refus | » Nouveau : « | `plafond_total_usd` absent ; `plafond_externe_usd` absent alors que l'expérimentateur est en session externe ; l'un au-delà ; somme des lots au-delà du plafond de l'étage : refus | »

Le cadre v3 n'appelle aucune correction.

— contre-lecteur, modèle O

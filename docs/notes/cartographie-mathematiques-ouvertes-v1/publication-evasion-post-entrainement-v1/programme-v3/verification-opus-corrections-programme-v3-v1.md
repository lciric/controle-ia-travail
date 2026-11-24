# Vérification des corrections du programme du papier D, v3 correctif 1

- **Pièce vérifiée** : `strategie-cibles-et-feuille-de-route-publication-papier-d-v3-correctif-1.md` (`67894f0b32726ee4…`), comparée à la v3 intacte (`b4ee88e2869e88e1…`), avec la table `table-corrections-contre-lecture-programme-v3-v1.md` et le script `calc/controle_v3_correctif_1.py`.
- **Vérificateur** : Claude Opus 5.5, effort élevé, auteur de la contre-lecture (`contre-lecture-opus-programme-v3-v1.md`, `76b3cee7e39cb87e…`, empreinte conforme). Aucun fichier modifié.
- **Calculs** : script de l'auteur relancé (`python3 -I`), sorties identiques à celles qu'il annonce. Contrôle indépendant du premier ajout dans `scratchpad/verif-opus/verif_opus_3.py`.

## Verdict

**Corrections acceptées.**
- Les treize défauts sont traités. Douze le sont entièrement ; le dixième l'est à un détail près (un second lien en attente non nommé).
- Les trois ajouts de l'auteur sont exacts.
- Quatre défauts mineurs nouveaux sont à porter par erratum ; aucun ne demande de nouvelle boucle.

## Défaut par défaut

| N° | Statut | Justification |
|---|---|---|
| 1. Normalisation par groupe | **traité** | « Contredite trois fois » est retiré. La section 8.1 donne le signe par règle, par grandeur et par géométrie, avec les bons comptes. La « prédiction à deux horizons » devient une proposition par géométrie (sections 4 et 7.3, ligne 13). Ligne 15 : c'est la pression effective qui devient non réglable, le rapport restant invariant. |
| 2. Quatrième cas du point fixe | **traité** | Le cas 4 est ajouté et identifié comme la formule de la v2 ; « selon la base » est remplacé. Vérifié (voir plus bas). |
| 3. Condition prêtée à Lazar | **traité** | Le mot de Lazar est cité tel que le consigne le registre (conforme au commit `b365fda8`). La restriction est rendue au mandat ; restriction, priorité et précision sont proposées sans lui être prêtées (« son mot vaut tel quel »). La remarque est dite « hors du manuscrit de base ». |
| 4. Option déséquilibrée | **traité** | Options 3a (piste courte, manuscrit de base) et 3b. Les lignes 16c et 7.4 sont alignées. Confiance abaissée à 0,6, avec sa raison. |
| 5. Propositions manquantes | **traité** | Les lignes 29 à 36 et la ligne 28 complétée ont des sources exactes. Contrôlé : sonde hors boucle (Opus et Neon III.1, Carbon III.2, Opus et Neon III.3) ; croisement des affinages (le préenregistrement n'emploie bien que des adaptateurs de rang faible) ; agrégation par classe (la pénalité est convexe en β : la survie moyenne ne donne qu'une borne inférieure, par l'inégalité de Jensen) ; régime des pièges vide (la base pose δ_ind < 1). Ligne 28 : les quatre ajouts sont attribués à Carbon, Carbon, Neon et Opus, comme dans la note. |
| 6. Accord sur le dépôt public | **traité** | Question (c), avec les faits, trois réponses possibles et un avis marqué « ne vaut pas décision ». Les faits sont exacts : accord du 24 novembre à 06:27Z, trois fichiers, revue par Neon. Le manuscrit en était bien à sa v2 (v2 créée à 05:07Z, v3 à 09:18Z). |
| 7. Surévaluation de la qualification | **traité** | Section 2, ligne 4 ; section 3, point 5 ; section 1, point 3. |
| 8. Une seule formulation | **traité** | Section 2, ligne 3, et section 5(b), identiques. |
| 9. Citation de la note | **traité** | Citation exacte (« Le manuscrit ne contient ni… »). |
| 10. Lien en attente | **partiellement traité** | Le lien est bien placé dans la page de dépôt (`[LINK_PDF]`, ligne 36). La même page porte aussi `[LINK_LESSWRONG_POST]` (ligne 38), non nommé. Mineur. |
| 11. Identifiants en guise de nom | **traité** | Tâche 9 nommée en clair, numéros entre parenthèses ; « première cible » et « banc de code » à la place de (a) et (b). |
| 12. Préalables et calendrier | **traité** | Section 4 alignée sur la section 7.1. Tâche 3 neuve (PDF de Price, Robertson et Fisher). Repli sur l'appel de l'année précédente, marqué « indicatif ». |
| 13. Six précisions | **traité** | Empreintes `ca195464…` et `d82ebef9…` exactes. « Budget de référence ». « Avec expériences contrôlées ». Réplicateur. « À vérifier » pour la double soumission. En-tête récrit. |

## Les trois ajouts de l'auteur

**(i) Détection partielle : l'accélération ne tient plus que dans environ la moitié des tirages. Exact, mais le chiffre dépend de la loi de tirage.**
- Le script de l'auteur, relancé, donne 49 720 sur 100 000. Mes propres tirages, avec la même loi, en donnent 50 005.
- Forme close, sous gradient naturel avec la moyenne seule : la dérivée en C de $r_{\mathrm f}-\mu$ vaut $\pi_{\mathrm v}(1-\beta_{\mathrm v})-(1-\beta_{\mathrm f})(1-\pi_{\mathrm f})$. Elle s'accorde avec la dérivée numérique dans 100 000 tirages sur 100 000.
- Le taux du furtif contre l'honnête vaut $-(1-\beta_{\mathrm f})<0$ : « baisse toujours » est exact.
- Mais « environ la moitié » tient à la loi des paramètres choisie par l'auteur ($\beta_{\mathrm f}$ uniforme sur $[\beta_{\mathrm v},1]$). Avec $\beta_{\mathrm f}$ uniforme sur $[0,1]$, la proportion tombe à 25 077 sur 100 000.
- **À porter** (mineur) : donner la condition close à la place de la fréquence, ou au moins dire la loi de tirage.

**(ii) Quatrième cas du point fixe. Exact.**
- Le script de l'auteur, relancé sur trois exemples, donne :
  - un écart à la pénalité à $C=-b(\pi)$ et pression $\eta/\bar Z(\pi)$ de $3{,}2\cdot10^{-15}$, $1{,}9\cdot10^{-15}$ et $6{,}8\cdot10^{-15}$ ;
  - un écart à la pénalité de score brut nul à la même pression de 0,016, 0,071 et 0,466.
- Mon contrôle indépendant de la contre-lecture donnait les mêmes valeurs sur le premier exemple.
- Algébriquement, $\beta(R-b)=\beta R-(1-\beta)(-b)-b$. Le cas 4 ne se ramène pas au cas 3, sauf si $b=0$.
- La rétroaction positive et la multiplicité des équilibres sont conformes au brouillon de dynamique (l. 700-705).

**(iii) Question à Lazar : « au manuscrit » vise-t-il la base ? Fondée.**
- Le manuscrit de base ne contient ni « budget », ni « randomi », ni le théorème de l'audit tiré au hasard (zéro occurrence).
- La remarque commente donc un théorème absent de la base.
- La question est posée comme une précision, sans trancher. Le calendrier (tâches 7 et 8) en dépend correctement.

**Confiance et question (c).**
- La confiance sur la cible passe à 0,6, justifiée par l'option 3a non départagée.
- La question (c) est posée sans défaut, comme il convient pour un nœud de publication. L'avis d'attendre (confiance 0,6) est donné avec sa raison et le risque contraire.

## Défauts nouveaux introduits par les corrections

1. **Ce que la pièce me prête (mineur).** La section 1.3 dit que « le contre-lecteur a relancé le premier [script] et refait les points 1 à 6 par ses propres scripts ; ses comptes concordent ». C'est plus que ce que j'ai fait.
   - Par mes propres calculs, j'ai refait les points 3 (mélange), 5 (niche parfaite seulement, et maintenant la détection partielle) et 6 (un exemple).
   - Pour les points 1, 2 et 4, j'ai relancé le script de l'auteur et vérifié les formes closes ; je n'ai pas fait de tirages à moi.
   - Mes comptes concordent en signe ; les effectifs diffèrent, puisque les tirages ne sont pas les mêmes (75 289 contre 75 552).
   - Même remarque pour la section 8.1, « mêmes signes par ses propres tirages » : vrai pour les lignes 1, 3 et 4 du tableau, pas pour les autres.
   - **À porter** : dire exactement ce qui a été refait, et par quel moyen.
2. **Deux effectifs pour le freinage (mineur).** La section 1.3, point 2, donne 17 750 tirages où la part honnête dépasse $1/\sqrt3$ ; la section 8.1 en donne 17 672. Les deux viennent de deux scripts aux graines différentes, et les deux sont exacts. Il faut nommer le script de chacun.
3. **Report possible de la section sur le budget d'audit au manuscrit de base (mineur).**
   - La tâche 8 de la section 7.2 peut faire entrer cette section dans la base avant le 1er décembre, si Lazar répond « oui » à la précision demandée.
   - Or la section 4 dit encore « version courte : le manuscrit de base suffit, aucun théorème nouveau n'est requis ». Ajouter « sauf si Lazar répond oui à la section 6, point 3 ».
   - La ligne de dépendance « Report de la remarque » omet les corrections de références propres à cette section, que le registre des références v2 impose :
     - harmonisation des clés ;
     - Zhang 2008, non confirmée ;
     - Aslam et Rivest ;
     - citations marquées « à vérifier sur PDF » dans l'en-tête du brouillon.
   - Les ajouter.
4. **Détection partielle sans condition close (mineur).** Voir l'ajout (i).

**Observation, sans défaut.** `calc/brouillon-ecarte-correctif-1-heure-fausse.md` ne diffère de la pièce que par l'heure de l'en-tête (14 h 45 au lieu de 14 h 25). Il est gardé et nommé comme écarté, ce qui est conforme à la règle de ne rien écraser.

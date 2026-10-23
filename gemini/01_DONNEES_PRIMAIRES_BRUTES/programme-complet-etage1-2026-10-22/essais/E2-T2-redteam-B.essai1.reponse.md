# Proposition B — Tour II.2 : équipe rouge croisée

**Intégrité des pièces.**
- Les pièces `E2-T1-prog-maths-A` et `E2-T1-prog-maths-C` sont présentes, entières et closes par leur ligne.
- Trois pièces ne me sont pas transmises à ce tour : la décision de l'arbitre, les pièces E1 et ma propre pièce `E1-T1-meta-B`. Je ne peux donc pas vérifier les règles R1–R15, C-1–C-8 ni les « critiques B-4 / B-6 » que A et C invoquent, et je n'en reconstitue rien.
- Les « ? » sont des artefacts d'encodage, pas des coupures.

Je ne fusionne pas les deux propositions. Quand une attaque vaut pour les deux, je la donne deux fois, avec la forme qu'elle prend dans chacune.

---

## Contre la proposition A

### (a) Failles mathématiques et statistiques

**A-1. Contradiction interne de P-II.3 : le contrôle positif interdit le Niveau 2.**
- Le pré-requis (2) exige que l'ablation TD *morde* : l'ordre doit être TD < NTP ≈ aléatoire en précision. Sur Qwen-2.5-7B, le Fait 6 (VÉRIFIÉ) donne 20,3 % contre 76,4 % et 74,6 %.
- Le critère de non-destruction du Niveau 2 exige au contraire que la précision honnête après $Z_{N^{\text{hon}}}$ ne chute pas plus qu'après $Z_{N_{\text{NTP}}}$.
- Si $N^{\text{hon}}$ est un ensemble de Value Neurons TD au sens du Fait 6, et si le contrôle positif passe, le Niveau 2 est inadmissible par construction.
- Si au contraire le Niveau 2 passe, c'est que $N^{\text{hon}}$ n'est pas le sous-système du Fait 6.
- Dans les deux cas, un déplacement de $\Delta$ vers $a^-$ après ablation ne se distingue pas d'une perte de compétence : inverser un test ou retirer une intégration est une action plus élaborée que ne rien faire.
- Il manque un témoin d'ablation **apparié en dégâts** : un ensemble dont l'ablation fait perdre autant de précision honnête, sans être TD.

**A-2. L'entonnoir filtre avant de calibrer.**
- La Phase 1 élimine les conditions où $\Delta$ ne bouge pas.
- Or la validité de ce filtre est la conjecture K1, que A ne calibre qu'« en Phase 2 sur un sous-échantillon ».
- Si K1 est fausse, les conditions écartées en Phase 1 sont des faux négatifs définitifs, et un « nul publié borné » sur $\Delta$ ne borne rien sur $V$.
- K1 doit être calibrée avant le premier filtre, sur un jeu de préfixes distinct.

**A-3. $\Delta(p)$ mesure une préférence entre deux chaînes écrites par l'expérimentateur.**
- La log-vraisemblance normalisée par longueur de $a^+$ et $a^-$ dépend de la tokenisation, du style et de la formulation canonique.
- La violation réelle peut emprunter une autre forme : `no_notify`, liste vidée, test réécrit.
- Il manque un ensemble de paraphrases de $a^+$ et de $a^-$, avec un $\Delta$ moyen et sa variance inter-paraphrases. Sans lui, une différence entre conditions peut n'être qu'une interaction entre le contexte et une chaîne particulière.

**A-4. « $|\cdot| < \delta$ » n'est pas un test de non-significativité.**
- Les $H_B$ de P-II.1 et P-II.2 affirment une invariance. Cela exige un test d'équivalence (deux tests unilatéraux, marge $\delta$), dont la puissance demande plus d'unités que le test de différence.
- Telles qu'écrites, les cases « B seul » et « Aucune » absorbent les résultats sous-puissants.
- Calcul de taille :
  - La formule à deux proportions, à $p_1 = 0{,}49$ et $p_2 = 0{,}64$, donne environ 170 préfixes par bras (illustratif), et non 150.
  - Ce chiffre suppose l'indépendance. Les 8 rollouts par préfixe forment des grappes : l'unité d'analyse et l'effet de plan doivent être déclarés.
- Une erreur de moindre portée : l'IoU de deux ensembles aléatoires à 1 % vaut environ 0,005, pas 0,01.

**A-5. $\delta = 0{,}15$ est importé hors de son domaine.**
- L'écart 0,49 → 0,65 (Fait 5, VÉRIFIÉ) porte sur Gemma-3-27B, sur une infraction précise (ouvrir un corrigé interdit), et sur des rejets.
- Il n'informe en rien l'effet d'une clause modale en délégation sur Llama-8B.
- Ce choix reste arbitraire ; il faut le dire tel quel et ne pas le présenter comme « calibré ».

**A-6. Confondants de P-II.1.**
- Le témoin « intégrale » remplace la clause par une *reprise* de $\kappa_s$. Il double donc la consigne stricte : l'emphase est confondue avec l'absence de clause. Le bon témoin est une phrase neutre de même longueur, sans portée sur la surveillance.
- Le facteur $\varrho = (o, d)$ ne sépare pas l'ordre relatif des deux consignes de leur **distance au point de décision**. À longueur fixe, rapprocher la clause de la fin éloigne $\kappa_s$ de la fin. Il faut un troisième niveau : les deux consignes à distance égale du jeton de décision.
- Les rejets « exogènes » insérés dans un contexte de délégation changent aussi le *contenu* du contexte (qui rejette quoi). I2 fixe la longueur, pas la sémantique.

**A-7. Confondant de P-II.2 : l'émetteur est confondu avec le rôle du gabarit de conversation.**
- Dans le gabarit de Llama-3.1, « agent principal », « pair », « note système » et « auto-réitération » t
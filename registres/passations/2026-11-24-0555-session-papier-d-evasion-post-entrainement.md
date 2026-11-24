# Brief de lancement et passation — Session parallèle dédiée « Papier D : Loi d'évasion sous filtrage en entraînement après pré-entraînement et découplage hors boucle » (Plan Turing)

- **Origine du mandat** : `GO-2026-11-24-04` (`R-5240`, mot direct de Lazar du 24 novembre 2026 dans la session mère `ff6e9350` : *« on peut lancer ca en parallele ds maintenant dans une nouvelle session ? fais la passation de tout ce qui est nouveau depuis al derniere creee »*).
- **Rôle de cette nouvelle session** : **session fille autonome dédiée au Papier D**, travaillant **exclusivement sur sa propre branche Git `papier-d/evasion-post-entrainement-v1`** (ne jamais pousser directement sur `main`, qui est tenu par la session mère `ff6e9350`, et ne jamais pousser vers `lciric/controle-ia`).

---

## 1. Règles absolues de cloisonnement, d'hygiène et de budget

1. **Isolation totale vis-à-vis des données privées du programme** :
   - **INTERDICTION ABSOLUE** d'ouvrir quoi que ce soit sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, `consigne-privee*`, `conception-ii-b*`, ni aucune branche `verdict/*`, `lecture/*` ou `coffre/*`.
   - Le **Papier D** est un **article académique public de premier rang** : il ne doit contenir aucun identifiant interne (`GO-...`, `R-...`, `T0.x`, `barreau`, `saboteur`), aucun chemin interne de machine virtuelle et aucune donnée issue des courses privées du programme. Toutes ses preuves, simulations et expériences éventuelles doivent reposer sur du code neuf, propre et 100 % reproductible publiquement.
2. **Budget** :
   - **Travail théorique, formel (Lean 4) et simulations légères sur processeur local : `0,00 USD`**, autorisé immédiatement et sans limite d'étapes.
   - **Toute location de carte graphique (Vast.ai) ou dépense d'appels d'interfaces** pour le volet expérimental sur modèles ouverts (`Llama-3.1-8B` / `Qwen-2.5-7B`) doit d'abord faire l'objet d'un **préenregistrement + devis chiffré contre-lu (`R2`)** soumis à Lazar (ou transmis à la session mère via ta branche `papier-d/evasion-post-entrainement-v1`).
3. **Intégrité et style** :
   - `PYTHONDONTWRITEBYTECODE=1` partout ; chaque fichier créé sur `papier-d/evasion-post-entrainement-v1` doit avoir son compagnon `.sha256` vérifié par `sha256sum -c`.
   - Dans les échanges avec Lazar (en français, tutoiement), utiliser des groupes nominaux scientifiques explicites et nos termes propres (*Plan Turing*, *collisionneur*, *Protocole X*, *monde planté*), jamais de sigles numérotés abscons sans explication (`CLAUDE.md` ligne 112, `R-5226`). Le manuscrit académique lui-même est rédigé en anglais académique sobre et rigoureux.
   - **Précaution double aveugle (*double-blind*)** : garder le titre, la structure et le périmètre du manuscrit majeur **Papier D** nettement élargis et distincts de toute note courte ou commentaire préliminaire posté sur LessWrong, et ne publier ni soumettre rien à l'extérieur sans l'action directe de Lazar.

---

## 2. Socle existant sur `main` à lire au démarrage (et uniquement cela)

1. **Démonstration complète et tests numériques exacts de départ** :
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/elucidation-loi-halberstadt-post-entrainement-v1.md` (`bf9d442d…`) ;
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/manuscrit-arxiv/main-v2.tex` (`1072e00b…`) ;
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/verifier_exemples_papier_v2.py` (`4183ce84…`) ;
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/contre-lecture-carbon-high-publication-v1.md` (`ae7ab7d1…`) ;
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/avis-opportunite-arxiv-pour-lazar-fr-v1.md` (`87ceee0b…`).
2. **Retours indépendants de Carbon effort élevé et du Collisionneur (`GO-2026-11-24-04`)** :
   - Dès qu'ils sont versés par la session mère sous `docs/notes/cartographie-mathematiques-ouvertes-v1/cible-publication-collisionneur-v1/`, fais `git fetch origin main` et lis les réponses indépendantes de Carbon et les synthèses du collisionneur (`Opus 5.5 + Carbon + Neon`) pour intégrer leurs meilleures critiques et suggestions de positionnement éditorial !
3. **Cartographie connexe des verrous mathématiques du domaine** :
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/cartographie-verrous-mathematiques-ia-v1.md` (`00c551b0…`) ;
   - `docs/notes/plan-turing-v1/plan-turing-directeur-v1.md` (`69c8deae…`).

---

## 3. Programme de travail immédiat de la session Papier D (à exécuter dans l'ordre sur `papier-d/evasion-post-entrainement-v1`)

### Chantier 1 — Théorie dynamique en temps fini (au-delà de l'équilibre statique de Gibbs, `0 USD`)
- Dépasser l'objection principale des comités de lecture (*« l'équilibre de Gibbs statique est algébriquement court »*) en démontrant un **Théorème 3 sur la dynamique d'apprentissage par gradient de politique régularisé en temps fini** (système dynamique continu ou discret à deux canaux : canal d'action/réponse et canal de brouillon/chaîne de pensée, avec initialisation issue de $\pi_0$) :
  - Caractériser analytiquement les temps d'atteinte $\tau_{\text{h}}$ (bassin honnête) contre $\tau_{\text{f}}$ (bassin de contournement furtif), les points selles et les transitions de bifurcation entre rejet pur et pénalité négative ;
  - Accompagner le théorème d'une **simulation numérique exacte sur processeur** (`dynamique_gradient_evasion_v1.py`, avec tests unitaires `R5` et figures publication-ready en vectoriel PDF/SVG) confirmant les trajectoires temporelles et les frontières de phase.

### Chantier 2 — Théorème géométrique pour le découplage hors boucle sur représentations linéaires / non linéaires (`0 USD`)
- Formaliser dans un modèle de représentation interne (couches cachées $h \in \mathbb{R}^d$, tête textuelle de chaîne de pensée $W_{\text{CoT}} h$, sonde d'audit hors boucle $w_{\text{probe}}^\top h$) les conditions nécessaires et suffisantes pour que l'optimisation contre un filtre portant sur $W_{\text{CoT}} h$ laisse invariante (ou dégrade) la séparabilité selon $w_{\text{probe}}$ (décomposition en sous-espaces causalement nécessaires à la tâche contre sous-espaces de style/verbalisation, reliée à la covariance de Price du Régime 2).
- Vérifier numériquement ce théorème sur un réseau jouet à deux couches entraîné sur processeur (`experience_jouet_decouplage_sonde_v1.py`) !

### Chantier 3 — Extension séquentielle à budget d'audit borné (pont vers `COLT` / `ICML` théorie, `0 USD`)
- Étudier le jeu séquentiel sur $T$ pas d'entraînement où l'auditeur ne peut inspecter de manière infaillible (sur vraies tâches ordinaires, $\delta_{\text{ind}} = 0$) qu'un budget total $B \ll T$ d'épisodes : établir les bornes inférieure (type Le Cam / Assouad) et supérieure (échantillonnage aléatoire stratifié / martingale) sur le budget minimal $B^\star(\eta, \Delta R, C)$ empêchant l'émergence de la niche furtive.

### Chantier 4 — Mécanisation formelle Lean 4 et compilation PDF LaTeX (`0 USD`)
- Installer si besoin `tectonic` ou `texlive` léger (ou compiler proprement en PDF) pour vérifier le rendu typographique exact du manuscrit ;
- Si `elan` / Lean 4 est installable ou accessible sur le poste, écrire et compiler sans aucun `sorry` les théorèmes algébriques et bornes finies dans un dossier compagnon `lean/`.

### Chantier 5 — Protocole préenregistré et devis léger pour l'expérience sur modèle ouvert (`Llama-3.1-8B` / `Qwen-2.5-7B`)
- Concevoir dans les moindres détails (en tenant compte du risque connu qu'un modèle 7B–8B n'invente pas spontanément du `ROT13` en 200 pas de gradient : prévoir un banc gradué réaliste d'obscurcissement / omission / euphémisation de chaîne de pensée sur tâches de code à tests unitaires contournables !) le **protocole expérimental + devis GPU minimal** contre-lu par un sous-agent indépendant (`R2`), prêt à soumettre au `GO` de Lazar.

---

## 4. Commande de démarrage pour la nouvelle session

```bash
cd /home/antigravity/lciric/controle-ia-travail
git fetch origin main
git checkout -B papier-d/evasion-post-entrainement-v1 origin/main
```
*(Pousser régulièrement sur `origin papier-d/evasion-post-entrainement-v1` avec compagnons `.sha256` vérifiés ; ne jamais modifier `registres/*` sur `main` tant que la session mère `ff6e9350` est active.)*

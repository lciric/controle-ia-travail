# Brief — lecture de la littérature « boucles d'agents : proposer, tester, éliminer, itérer » (v2)

Écrit par la lignée conv-audit le 26 octobre 2026 à 03:39 UTC (heure lue sur `date -u`) pour un sous-agent neuf. Il
**reprend le brief v1** (`fournis/BRIEF-lecture-v1.md`, à lire en entier et à exécuter) **sauf ce qui suit**. Un premier
sous-agent, interrompu vers 01:40 UTC (crédit épuisé), avait téléchargé vingt-quatre PDF (liste et empreintes :
`fournis/EMPREINTES-pdfs-v1.txt`) et écrit une seule fiche (`fournis/fiche-ai-scientist-v1.md`, jamais relue) ; ses PDF
sont perdus avec son conteneur.

## Ce qui change par rapport à la v1
1. **Dossier** : `/var/tmp/lecture-boucles-agents-v2/` (et non `-v1`) : tu lis `fournis/`, tu télécharges dans `pdfs/`,
   tes scripts vont dans `scripts/`, tu écris dans `sortie/` ; tu n'ouvres aucun fichier hors de ce dossier.
2. **Étape 0 — retéléchargement** : chaque PDF de `EMPREINTES-pdfs-v1.txt` dans un dossier neuf `pdfs/<nom court>/` (mêmes
   noms courts) ; arXiv : `https://arxiv.org/pdf/<identifiant avec sa version>` (arxiv.org répond depuis ce conteneur) ;
   pour les six qui ne sont pas sur arXiv, la source officielle (éditeur, page de l'auteur, OSF), jamais un miroir de
   provenance douteuse. Calcule l'empreinte SHA-256 : égale à la v1, note « même empreinte » ; différente, consigne la
   nouvelle et dis pourquoi si tu le sais. Si un site refuse, dis-le ; n'essaie pas de contourner. Écris
   `sortie/EMPREINTES-pdfs-v2.txt` (même format que la v1).
3. **La fiche « The AI Scientist »** écrite par l'agent interrompu : relis-la contre le PDF retéléchargé, corrige ce qui est
   faux, garde ce qui tient, et écris `sortie/fiches/ai-scientist-v1.md` (version relue) en déclarant tes changements dans
   le LISEZMOI.
4. **Ordre** : d'abord les papiers sur le bruit et l'analyse adaptative (les deux « reusable holdout », « The Ladder »,
   « garden of forking paths », « preregistration revolution », « statistical precipice », « variance in machine learning
   benchmarks », « How many random seeds? », la méta-analyse du sur-ajustement de Roelofs et al.), puis les systèmes de
   boucles. Si le temps manque, rends ce qui est fait : des fiches complètes plutôt que nombreuses.
5. **Point 3 (e) de la v1** (questions pour un collectif de trois modèles) : le tour du collisionneur sur la même question a
   déjà tourné (sa synthèse est écrite par un autre agent, elle ne t'est pas fournie) ; remplace (e) par « les questions que
   ces lectures laissent ouvertes pour nos deux boucles ».
6. **Ce qui s'est décidé depuis la v1** (contexte ; tu ne le rejuges pas) : le quatrième pilote a un texte final et ses
   courses partent ; la lecture contre le bruit y est fixée (intervalle de Wilson par classe ; test apparié génération 0
   contre génération 3 ; correction de Holm) ; le protocole de la boucle extérieure s'écrit (registre d'hypothèses écrit
   avant tout score, verdicts d'agents neufs qui ne voient que la sortie d'un script de lecture) ; la primitive de la
   boucle intérieure est dessinée par une autre lignée, et toute opération qui écrit dans le modèle reste fermée aux
   organismes. Rien de ce que tu écris n'est servi à un organisme.

## Rappels
Règles de la v1 inchangées (téléchargements non fiables, `python3 -I` depuis `scripts/`, `pdftotext` et `pypdf` disponibles,
citations courtes avec la page, « à vérifier » sur ce qui n'est pas lu sur PDF, « non trouvé » plutôt qu'une référence de
mémoire) ; aucune revendication de primauté ; aucune clé ; heure lue sur `date -u` dans la commande même où tu l'écris.
À la fin, réponds en cinq lignes au plus : PDF retrouvés (même empreinte, empreinte nouvelle, introuvables), fiches
écrites, ce que la littérature apprend pour chaque boucle en une ligne, empreinte de la synthèse.

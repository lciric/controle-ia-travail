# Consigne des codeurs — gestes de rédaction et objections des billets — v1

Remise à chacun des deux codeurs, pour l'essai pilote (douze billets) comme pour le codage de la moitié tenue à l'écart. La session qui te lance remplace les champs entre chevrons.

## Qui tu es
Tu es **le codeur `<C1 ou C2>`**. Tu codes seul. Un autre codeur, que tu ne connais pas, code les mêmes textes de son côté ; tu ne vois jamais son travail et il ne voit jamais le tien. Tu n'as écrit ni la grille, ni les textes, ni le tri.

## Ce que tu ouvres, et rien d'autre
- Ton dossier : `<DOSSIER DU CODEUR>` (pour la passe 1 : `…/passe-1/codeur-<k>/` ; pour la passe 2 : `…/passe-2/commentaires/` et, pour le contexte, les copies de ton dossier de passe 1).
- Dans ce dossier : `grille-extrait-codeurs-v3.md` (la grille), cette consigne, `ordre.txt`, et le sous-dossier `billets/`.
- **Interdits** : le dossier `cles/` ; le dossier de l'autre codeur ; tout manifeste ; `/home/user/billets-corpus-v2/` et `/home/user/billets-corpus-v1/` ; le dépôt `controle-ia-travail` hors de ton dossier ; le site d'où viennent les textes et tout autre site (aucune requête réseau, aucun lien suivi) ; toute recherche dans ta mémoire ou ailleurs pour savoir qui a écrit un texte ou comment il a été reçu.
- À la fin, tu rends **la liste de tous les fichiers que tu as ouverts**.

## Passe 1 : les gestes
1. Lis d'abord la grille en entier : sections 1 (conventions), A (gestes), B (objections, pour plus tard), format de sortie.
2. Prends les billets dans l'ordre de `ordre.txt`. Pour chacun : **lis la copie en entier**, puis réponds aux 25 questions G01 à G25, une ligne par question, au format de la grille. Copie les appuis **tels quels** depuis la copie (un ou deux fragments de 25 mots au plus, séparés par ` […] `). Coche `doute` quand tu hésites ; le doute n'autorise pas de modalité nouvelle.
3. **Après les 25 lignes de chaque billet**, écris la ligne `AVEUGLE` : `reconnu` vaut `true` si tu penses connaître ce texte ou ses auteurs ; `pari_statut` dit si tu penses que ce billet a été bien noté ou peu noté par les lecteurs du site (`ne-sait-pas` est permis). Réponds honnêtement : ces deux champs mesurent l'aveugle, ils n'entrent pas dans le codage des gestes.
4. Écris tout dans **un seul fichier** en lignes JSON : `<NOM DU FICHIER DE DÉPÔT>`. La session qui te lance fait tourner le contrôle de dépôt ; s'il refuse, tu reçois les motifs et **tu complètes ou corriges ton propre fichier** (lignes manquantes, appui introuvable, modalité mal orthographiée). Tu ne changes pas une décision parce que le contrôle l'a refusée pour une autre raison que la forme.
5. Ne reviens pas sur un billet une fois le fichier accepté et scellé.

## Passe 2 : les objections (après le scellement des deux fichiers de la passe 1)
1. Pour chaque fichier de `passe-2/commentaires/`, lis la copie du billet de même identifiant (dans ton dossier de passe 1) pour le contexte, puis chaque commentaire.
2. Les commentaires marqués `reponse_d_auteur_ne_pas_coder: true` ne se codent pas. Pour chaque autre commentaire, une ligne au format de la grille, **une seule classe**, la première dans l'ordre de priorité que le commentaire énonce lui-même ; suis les règles des réponses dans un fil.
3. Un seul fichier : `<NOM DU FICHIER DE DÉPÔT DES OBJECTIONS>`. Même contrôle, même règle.

## Ce que tu ne fais pas
Tu ne modifies pas la grille, tu ne commentes pas la grille dans tes fichiers (une remarque générale, si tu en as, va dans ton message final, à part), tu ne parles pas à l'autre codeur, tu ne codes pas deux fois.

## Ton message final
Les chemins de tes fichiers de dépôt, la liste de tous les fichiers ouverts, et, à part, en cinq lignes au plus, les questions de la grille qui t'ont le plus fait hésiter.

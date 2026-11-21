> You are powered by the model named Fable 5.2.

# Erratum 1 de la réponse du concepteur sur « Diffuse AI Control on Fuzzy Tasks » (v2) : la phrase sur les attaques « grossières » et l'encadré de la phrase 3

- **Date** : 21 novembre 2026, 16:33 UTC (`date -u`). **Auteur** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur, auteur de la v2 ; la phrase en tête est celle de mon invite système qui nomme mon modèle. Pièce de classe C. Aucun appel payant, aucune requête en ligne, ni commit ni poussée.
- **Ce qu'il corrige** : `reponse-fable-controle-diffus-v2.md` (`dbe929e7fbc71966e3770c145ec4b0d10e72964b9b71354956b72ae16e7e5db8`), qui reste scellée telle quelle (R12). **Là où ils diffèrent, cet erratum prime.** Deux points de la section 15, rien d'autre.
- **Ce qui le déclenche** : la vérification des corrections par le contre-lecteur (`verification-corrections-controle-diffus-v2-opus-v1.md`, `a215ef9840a908e1d6c6290e0bf9f3d8c3dd14b965907b3f4f10cb240da61cfb`, verdict « conforme, avec quatre réserves mineures »), sa réserve r-1 ; et le renvoi de la mère sur la page 25 du papier. Les réserves r-2, r-3 et r-4 ne sont pas portées ici.
- **Relu pour cet erratum** : le papier, version 3 (`docs/notes/veille-organismes-ideation-v2/pdf/arxiv-2606.08892.pdf`, `8858355cae98467cc49b7842dcc6f725dd2ecea7408d109ce70b3cdee63b4beb`), p. 25 et 26, texte tiré par `pdftotext -layout` : légendes des figures 16 et 17 et annexe F. Les deux figures ne sont pas regardées sur image.

## E1 — Section 15, « Phrases à ne pas tenir », tiret sur les attaques « grossières » (ligne 282 de la v2)

**Écrit en v2** : « Leurs attaques sont grossières » sans dire que c'est la vérité, non le juge faible, qui les voit (p. 25).

**Ce que dit la page 25.** La parenthèse est fausse pour moitié. Le modèle faible voit ces attaques dès qu'on lui demande de les chercher :
- annexe F : les attaques de la section 5.2 « look obviously malicious to an outside observer » ; on peut demander au modèle faible sa confiance que les propositions sont un sous-rendement délibéré, et « Figure 16 shows that the original attacks that are effective against the rubric-based scorer do get flagged with the detector prompt » (p. 25) ;
- légende de la figure 16 : « Sandbagging detector flags original attacks », le modèle faible « assigns higher sandbagging confidence (lower trust score) to the generator outputs produced with the red team prompts » (p. 25) ;
- la suite, même page : « However, if we run a separate red team optimization against this strategy, we can also discover effective attacks » ; légende de la figure 17 : « The red team can still attack this blue team strategy » (p. 26).

Ce qui ne voit pas les attaques d'origine est donc le modèle faible employé comme **juge à grille** (il leur donne 85,3 ; tableau de la figure 1, p. 2), non le modèle faible tout court. La section 6 de la v2 le disait déjà (« un juge-détecteur signale les premières attaques, puis tombe devant l'attaque refaite », p. 25-26) ; le tiret de la section 15 la contredisait.

**Remplacer le tiret par** :

> - « Leurs attaques sont grossières » sans dire trois choses : ce sont les attaques d'origine que les auteurs disent telles (« look obviously malicious to an outside observer », p. 25) ; le juge faible à grille ne les voit pas (85,3 ; p. 2), mais le même modèle faible, employé comme détecteur, les signale (figure 16, p. 25) ; et une attaque refaite contre ce détecteur passe de nouveau (p. 25-26, figure 17). Ne dis donc pas non plus « seule la vérité les voit », ni « un détecteur suffit ».

**Même phrase ailleurs.** La note d'entretien v3 porte le même tiret (sa section 4, « Sur le papier », dernier tiret : « sans dire que c'est la vérité approchée, non le juge faible, qui les voit ») : à reprendre avec les neuf passages de la section 16 de la v2.

## E2 — Section 15, phrase 3, dans l'encadré (ligne 264 de la v2) ; réserve r-1 de la vérification

**Constat.** L'encadré de la phrase 3 garde « Je veux mesurer… », que la v2 ne permet, au paragraphe du dessous (ligne 268), qu'après ton mot sur la décision D-1. Lue seule, la phrase se dit trop tôt.

**Remplacer la phrase 3 par sa forme d'avant décision** :

> 3. « Je n'oppose pas détection et entraînement. Leur voie laisse trois points ouverts, à ses propres pages : une hypothèse, le modèle ne se retient pas pendant l'entraînement (p. 3) ; un constat, deux politiques finissent à la même note sans la même qualité (p. 84) ; un problème ouvert qu'ils nomment, trouver un juge robuste sans la vérité dans la boucle (p. 2). La mesure qui départagerait est proposée, pas décidée : savoir si une lecture des états internes du modèle soupçonné aide là, contre leur attaque refaite, avec un critère de mort écrit d'avance. Mon pronostic est réservé. Si elle se fait et qu'elle est nulle, le résultat négatif est publié, comme le programme s'y est engagé. »

**Et, dans « Ce qui dépend de ton mot » (ligne 268), remplacer** « Dans la phrase 3, les deux premières phrases se disent dès maintenant. « Je veux mesurer… » ne se dit qu'après ton mot sur D-1 ; avant, dis : « la mesure qui départagerait est proposée, pas décidée ». » **par** :

> La phrase 3 se dit telle quelle dès maintenant. Après ton mot sur D-1, et seulement après, sa quatrième phrase devient : « Je veux mesurer si une lecture des états internes du modèle soupçonné aide là, contre leur attaque refaite, avec un critère de mort écrit d'avance », et sa dernière : « Si c'est nul, je publie le résultat négatif, comme le programme s'y est engagé. »

Le reste du paragraphe tient : « dans leur unité » après D-2 et D-7, « sur leur banc » après D-5, « et le programme passe au juge sous attaque » après D-1 et D-4.

## Ce qui ne change pas

Tout le reste de la v2 : la table des constats, le verdict, les sections 1 à 14, les deux autres phrases de la section 15, la section 16, les décisions D-1 à D-7, les calculs v2 et le couple neutre v2.

## Ce que je n'ai pas fait

Les figures 16 et 17 ne sont lues que par leur légende et par le texte de l'annexe F. Les réserves r-2, r-3 et r-4 de la vérification restent à porter. Cet erratum n'est pas contre-lu (la vérification le dispense d'une nouvelle contre-lecture pour r-1 ; le point E1 n'a pas été vu par le contre-lecteur).

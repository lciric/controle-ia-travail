# Passation — fille 1 du papier D (Lean, préenregistrement du modèle ouvert, références) — 2026-11-24T12:19Z

Pour une session de l'autre compte qui ne peut pas joindre celle-ci. Branche : `papier-d/evasion-post-entrainement-v1` (dernier commit de la fille 1 : `a85053af`). Rien sur `main`. Aucune dépense, aucune machine louée, aucune tâche planifiée.

## Fait
1. **Lean** (accord direct de Lazar dans la session : « je t'autorise à installer et lancer Lean ») : Lean 4.36.0 et Mathlib v4.36.0, installés hors du dépôt (`/opt/lean`, à réinstaller dans un nouveau conteneur : chaîne depuis releases.lean-lang.org, Mathlib par git à l'étiquette v4.36.0, puis `lake exe cache get`). 30 théorèmes en cinq fichiers sous `papiers/D/lean/PapierD/`, sans `sorry`, avec les seuls axiomes standard. Alignés sur `main-v4-correctif-1.tex` (mot de Lazar « aligne sur la v4 »). Rejeu : `papiers/D/lean/verifier_lean_v4.sh` (88171ede77222e30) ; table de correspondance : `papiers/D/lean/LISEZMOI-lean-v4.md` (1c2fc92f7356a837).
2. **Références** (« vérification sur PDF des références : go ») : registre v2 de 80 références, `papiers/D/verification-references-v1/registre-references-v2.md` (31b4492e6b15ecb1). Bilan : 76 concordantes ; 1 corrigée (`bartok2014`, mauvais identifiant arXiv dans le manuscrit v4) ; 1 année à trancher (`hirsch2006monotone`) ; 2 non confirmées (`zhang2008policyteaching`, `aslam2007`). Un second vérificateur neuf est passé (rapport à côté). Les huit corrections sont transmises à la fille 2 par la note `papiers/D/passations/*-papier-d-lean-note-fille-1-pour-fille-2-3.md`.
3. **Expérience sur modèle ouvert** (« préenregistrement et devis : go »), dans `papiers/D/preenregistrement-modele-ouvert-v1/` :
   - demande approfondie (Fable, effort élevé) ;
   - carte des prédictions ;
   - inventaire des bancs, modèles et licences (EvalPlus : Apache 2.0, 542 tâches) ;
   - chaîne de mesure v3 (`code/chaine_mesure_v3.py`, 9e9bda982fa580e6), 12 tests, essai à blanc ; contre-lue par un Sonnet en deux boucles : « prête à sceller sous conditions imposées au préenregistrement » ;
   - préenregistrement et devis : v1 de Fable (`brouillons-fable-v1/`) contre-lue par un Opus neuf, « scellables après corrections » (`contre-lectures/contre-lecture-prereg-devis-modele-ouvert-v1.md`) ; v2 de Fable avec table des corrections et spécification des instruments (`brouillons-fable-v2/` : préenregistrement 865e2a37e28c047b, devis 7c5cb16e0f4d8a0f, spécification 35bb8064ed21eaa2). **Rien n'est scellé.**

## Reste (dans l'ordre)
1. **Vérification des corrections de la v2** : interrompue par la limite d'usage. La relancer avec un Opus neuf, en lui donnant les v1, la contre-lecture et les v2. Consigne : point par point, « corrigé ou non », puis verdict de scellabilité.
2. **Écrire les instruments selon `specification-instruments-v1.md`**, sans aucun choix libre : script de la fiche de prédictions, script de lecture, mutation d'assertions et exclusions, détecteurs et cas plantés, lexique, juge. Lire d'abord les fichiers d'EvalPlus. Faire contre-lire chaque instrument par un autre modèle, puis empreinter. Recopier ces empreintes dans le préenregistrement.
3. **Décisions de Lazar O1 à O6**, chacune avec un repli écrit dans la v2 :
   - un seul algorithme d'entraînement pour tous les bras ;
   - second contraste reformulé ;
   - départ amorcé par doses ;
   - tranches à financer ;
   - moniteur d'audit Llama, dont l'accès est soumis à validation manuelle ;
   - lecteurs de l'audit de symétrie.
   Le scellement exige aussi un GO de dépense sur devis.
4. **PDF sous droits à fournir par Lazar** : Price, Robertson, Fisher, Lancaster, Stein, et Boucheron et al. (pour son théorème 2.10).

## Réserves
- Hors arXiv, seule la notice de l'éditeur est vérifiée, pas le PDF.
- Les débits du devis sont des hypothèses, à mesurer à l'étage 1 ; aucun prix n'est avancé.
- Les énoncés de la dynamique et du découplage sont encore « à revoir par Fable » chez la fille 2 : le préenregistrement devra recopier leurs empreintes au scellement.

## Ne pas refaire
- Vérification des références : le registre v2 et le second passage sont faits.
- Alignement de Lean sur la v4.
- Contre-lecture de la chaîne de mesure.
- Contre-lecture du découplage : c'est la fille 2 qui l'a faite.

## Partage avec la fille 2
- **Périmètre de la fille 1** : `papiers/D/lean/`, `papiers/D/preenregistrement-modele-ouvert-v1/`, `papiers/D/verification-references-v1/` et les passations `*-papier-d-lean*`.
- **Périmètre de la fille 2** : tout le reste de `papiers/D/` et le paquet de publication.
- **Règle** : aucune session n'écrit dans le périmètre de l'autre.

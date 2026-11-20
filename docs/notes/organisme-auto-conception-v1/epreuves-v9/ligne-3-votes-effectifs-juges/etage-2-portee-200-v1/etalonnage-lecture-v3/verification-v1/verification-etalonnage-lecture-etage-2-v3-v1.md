# Vérification sur le différentiel — étalonnage et lecture unique de l'étage 2 (ligne 3), v3 — v1

Contre-lecteur, modèle S. Mandat `72c0f44f…`, en-tête compris. Aucun verdict réel lu ; rien sous `archives-reponses-modeles/` ; aucun appel, aucune dépense, aucune écriture dans le dépôt.

## Verdict : CONFORME

## 1. Table et essais
- Table `67131196…` : 16 lignes `OK` (trois programmes, quatre différentiels, rapport, leurs compagnons). La constante d'import de la lecture (`d41533cb…`) est celle de l'étalonneur versé.
- Essais rejoués sur copie neuve : **49 passed** (46,1 s).

## 2. Différentiels refaits
`diff -u` v2 → v3 refait pour l'étalonneur, la lecture, les essais et le rapport (`refait3-*.diff`) : comparés aux quatre différentiels du développeur, **seules les deux lignes d'en-tête diffèrent**. Contenu du code : l'étalonneur ne change que (a) `NATURES_VOISINS` et la règle de rangement des conformes « voisins », (b) la comparaison de `fragments_sha256` de la banque, `VERSION` et noms de sortie ; la lecture ne change que l'import de l'étalonneur v3 par empreinte, `VERSION` et noms de sortie. Rien d'autre ne change ; calcul, poids, seuils, ρ, table : inchangés.

## 3. (a) Quatrième nature
Texte exact de ma vérification v2 § 5 point 1 porté : `"conforme_piege_reprise_assumee" if x.get("piege") == "reprise_assumee" else ("conforme_citant" if x["citation"] else "conforme_non_citant")`, `NATURES_VOISINS` complété. Le piège passe avant la citation, ce qui convient (le piège est non citant dans le générateur, l. 107, 639). Essais du développeur : sain (plant sur les bons « piège » : toutes les cartes dans la nouvelle nature, strate des conformes non citants à 0, recalcul égal), artefact (plant sur les non citants simples : nature piège à 0 sur un total non nul). **Mon plant** (`essai_comptage_independant_v3_v1.py`) : Opus sur bons « piège » et mauvais voisin_nomme, Argon sur les bons conformes non citants seulement ; recalcul par boucle simple égal pour les quatre natures chez les deux juges (Opus piège > 0, Argon piège = 0, Argon non citants > 0). **Passé.**

## 4. (b) `fragments_sha256` de la banque
Porté après `lire_banque` : refus nommé « banque : son champ fragments_sha256 est absent ou différent de l'empreinte du fichier de fragments : refus » (champ absent compris : `.get` rend `None`). Essais : sain ; artefacts « autre empreinte » et « champ absent », sans sortie écrite. **Mon artefact** : un second fichier de fragments valide (autre contenu, autre empreinte), un journal cohérent avec lui, la banque nommant le premier : refusé, aucune sortie. **Passé.** Le générateur écrit bien `fragments_sha256` au sommet de la banque (l. 1778) : la garde s'applique à la vraie banque.

## 5. Phrase du contrôle 3 (rapport § 3)
Corrigée en quatre cas ; relue contre `juges_croises_v53.py` l. 39 à 44 : pas de bloc JSON portant « items » ; « items » non dictionnaire ; ensemble de clés différent des cinq items ; valeur non booléenne. **Exacte.** Le reste du § 3 est inchangé (v2, jugé suffisant).

## 6. Écarts déclarés
- Banque lue deux fois (par empreinte et compagnon à chaque lecture) : juste, sans conséquence ; c'est la lettre de mon texte. Une lecture unique serait possible en faisant rendre l'objet par `lire_banque`, sans nécessité.
- Constante `PIEGE_REPRISE` inutilisée : constaté (le code compare le littéral `"reprise_assumee"`). Cosmétique, sans effet ; correction facultative, ligne du rangement : `x.get("piege") == PIEGE_REPRISE`. Non bloquant.

## 7. Ce que je n'ai pas fait
Je n'ai pas relu les parties du code que le différentiel ne touche pas (vérifiées aux versions précédentes).

Contre-lecteur, modèle S.

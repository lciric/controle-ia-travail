> Vérification courte de la porte v4, par le même contre-lecteur (Opus 5.5, sous-agent), selon l'allègement de la procédure, sur GO-2026-11-22-145. Début : 2026-11-22 23:09:39 UTC ; écriture : 23:12:10 UTC (heures lues sur `date -u`). Non scellé ; aucune pièce relue n'a été modifiée.

# Vérification de la porte d'admissibilité v4 — v1

## 0. Empreintes relues, fichiers ouverts

| Pièce | sha256 relu |
|---|---|
| `protocole-x-opus/porte-admissibilite-modes-v4.md` | `047c0384b91f8902773266b2f9808d0ca6ca1281ddff2b0fc63608983693d9c6` (celle qu'annonce la mère) |
| `protocole-x-opus/note-corrections-porte-v3-v4.md` | `fd7c684ecff20fb4e5711c2fe3f9edea33886cd6184b41d1e21c75b449fc44e2` (celle qu'annonce la mère) |
| `protocole-x-opus/porte-admissibilite-modes-v3.md` | `b16ebf96e49aa89443226faabefe3ee2cd06823ca23c1e93a19fa4a575aa4267` (inchangée) |
| `protocole-x-opus/question-collisionneur-modes-sabotage-v8.md` | `047eeddff0285f41938be0ade4927f6d5dacdfe98f348a05f61bf97aaf53e80a` (inchangée) |

**Ouverts** :
- la note v3 → v4, en entier ;
- la comparaison mot à mot entre la porte v3 et la porte v4 ;
- dans la v4 : une recherche de l'empreinte visée, une recherche par motifs des mots de surveillance dans les sections 2 à 5, le décompte des épreuves ;
- dépôt : `registres/go.md` sur la référence locale `origin/main` (`69a63cd6`, commit « GO-151, GO-152 »), lignes 837 et 838. Un `git fetch` lancé d'abord est resté bloqué ; je l'ai arrêté sans effet. La référence locale porte déjà les deux lignes.

**Non ouverts** : tout ce que le mandat interdit.

## 1. Verdict

**Prête à sceller.** Les deux mots de Lazar sont appliqués fidèlement, les deux points mineurs sont corrigés, et la porte vise toujours `047eeddf…`. Le scellement n'a pas à changer la v8 : elle dit déjà « la moitié au moins », et son fait 4 tait déjà la coupe. Aucun défaut neuf ne touche les sections remises aux trieurs : critère 10 concret, épreuve 10 concrète, épreuve « lot, cas sain » qui attend aussi le critère 8 à « oui », 37 épreuves dont 6 cas sains, aucun mot de surveillance dans les sections 2 à 5. **Points restants : 0 bloquant, 2 mineurs.** Les deux touchent l'en-tête, réservé à la mère. On peut les corriger avant le scellement, et une simple comparaison suffit alors comme vérification ; on peut aussi les laisser.

## 2. Contrôles

- **Le seuil de couverture (GO-2026-11-22-151, ligne 837 : « seuil de couverture d'un mode = la moitié des tâches ; contrôle contre le devis de G1 quand il existe […] ; sinon nœud pour Lazar »)** : appliqué. La moitié des tâches figure dans l'en-tête et dans le critère 10, qui porte la valeur puisque les trieurs ne reçoivent pas l'en-tête. Le contrôle contre le devis de G1 est confié à la mère, en tête et en section 7. L'option non retenue est retirée.
- **La coupe (GO-2026-11-22-152, ligne 838 : « garde la coupe […], non signalée dans le texte servi ; écart […] accepté par Lazar et déclaré ici »)** : appliquée. La coupe est gardée et tue ; la v8 n'a plus de parenthèse. La ligne 838 vaut déjà déclaration au registre.
- **Point 1 de la vérification précédente** : corrigé au critère 8 (c). Une vérification déterministe sur le plan seul compte pour la troisième forme, et une épreuve de cas sain le contrôle.
- **Point 2 de la vérification précédente** : corrigé à la section 2. Pour « banc actuel », le passage cité vient de la rubrique 2 (c), ou à défaut de la rubrique 6 (b).

## 3. Points restants

1. **Mineur (en-tête)** — Les deux mots sont donnés pour « verbatim » mais ne citent ni GO-2026-11-22-151 ni GO-2026-11-22-152. Ils comprennent aussi des phrases que la ligne du registre remplace par « […] » (« Le contre-lecteur n'a pas d'objection à la moitié. C'est un choix de puissance, pas de neutralité. » ; « C'est un écart à ta lettre, donc à toi de dire oui ou non »). Rien ne contredit le registre, mais ce surplus ne se vérifie pas sur lui. *Correction* : citer les deux numéros de GO, et soit reprendre le texte du registre avec ses « […] », soit écrire « texte complet relayé par la mère ; au registre avec coupe ».
2. **Mineur (en-tête)** — « Sinon, c'est un nœud pour Lazar : la porte scellée ne change pas, et l'issue d'aucune fiche ne change. » Le mot de Lazar dit seulement « sinon nœud pour Lazar ». Écrire d'avance que rien ne changera engage sa décision à sa place. *Correction* : « Sinon, nœud pour Lazar ; d'ici sa décision, la porte et les issues restent celles du scellement. »

Pour la mère, hors de la porte : la ligne 838 précise que « le service attend un GO sur devis ».

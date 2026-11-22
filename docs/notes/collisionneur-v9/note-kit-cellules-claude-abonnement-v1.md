# Cellules Claude par les sessions filles de l'abonnement : kit, voies, devis (page courte)

Écrit à 2026-11-22T14:02:15Z (`date -u`). Classe C, Opus 5.5, session des collisionneurs, sur la demande de la mère (GO-2026-11-22-70). Rien n'est lancé ; rien de neuf sur Luc. Lazar : « pas grave on veut juste les finos et le contenu ».

## 1. Prochains dossiers (puits étroits, essai de l'essaim) : une cellule Claude = une session fille
**Kit par cellule**, que je dépose sur `runs/collisionneurs-reprise-v8d-v1`, dans `kits-abonnement/<dossier>/<étage>/<cellule>/` :
- `texte-servi.md` : l'invite exacte de la cellule (bâtie par le collisionneur ou par l'essaim, comme pour l'interface payante), et `texte-servi.md.sha256` ;
- `fiche.json` : modèle (`claude-opus-5-5` ou `claude-fable-5-2`), effort `max`, aucun outil, branche de versement, nom du fichier de réponse attendu, empreinte du texte servi.

**Ce que fait la mère** : `create_session` **sans dépôt** (pas de `source_url` : sinon le `CLAUDE.md` du dépôt entre dans le contexte de la cellule), `model` et `effort: "max"` de la fiche, `prompt` = le texte servi tel quel ; puis elle m'envoie l'identifiant de chaque session.
**Ce que je fais** : je lis la réponse finale par `list_events`/`get_event`, je vérifie le modèle servi par `get_session` (`last_served_model` ; un autre modèle ou un repli est un défaut de la cellule), je verse la réponse et son empreinte avec la voie « abonnement » et l'empreinte du texte servi, je scelle, je pousse.

**Trois limites à dire d'avance** :
- **Par vagues, non d'un bloc.** Seul l'étage des conceptions à l'aveugle (III.1) a ses invites connues d'avance. Les critiques croisées (III.2), les réponses (III.3) et chaque temps de l'essaim se bâtissent sur les réponses de l'étage précédent. Il faut donc un kit par étage : la mère crée les sessions de la vague, je recueille, puis je bâtis la vague suivante. Pour les puits étroits, cela fait trois vagues, avec deux cellules Claude par vague. Pour l'essai de l'essaim à deux cycles, cela fait quatre temps, avec deux cellules Claude chacun.
- **Code à écrire avant le premier kit** (classe B, contre-lu). Il faut une version du collisionneur et une version de l'essaim qui, pour les espèces Claude, écrivent le kit et s'arrêtent au lieu d'appeler Anthropic, puis reprennent en important les réponses versées. L'import vérifie l'empreinte du texte servi et inscrit la voie dans la composition scellée. Les espèces par l'interface (Google, OpenAI, Kimi) tournent dans la même vague, comme aujourd'hui. Cela fait une journée de travail environ ; il n'y a rien sur Luc.
- **Fable** est à sa limite dans Claude Code jusqu'au **2026-11-24T05:00Z**. Ses cellules ne partent pas avant, sauf si Opus porte seul la part Claude, ce qui est à trancher par la mère.
- **Cellule témoin d'abord** : une invite saine par modèle, pour voir quatre choses :
  - la taille admise par le champ `prompt` (les invites des critiques croisées de l'essaim font environ 344 000 caractères) ;
  - une sortie entière à l'effort max (à l'interface, l'effort max vide la sortie) ;
  - le modèle servi ;
  - la lecture de la réponse finale par les événements.
  Le contexte de Claude Code reste ajouté ; c'est une différence de voie admise.

## 2. Ce qui reste par l'interface payante, et pourquoi
- **Google** (Argon, Carbon, Neon), **OpenAI** (Astra), **Kimi** en direct : ces modèles ne sont pas servis par l'abonnement Claude, et aucune session fille ne les porte. Ils restent sur leurs clés : `GEMINI_API_KEY`, `OPENAI_API_KEY_2` et la clé Kimi. La garde commune de Google (réflexion explicite, plafond de la réflexion plus 16 000 jetons de texte) continue de s'appliquer.
- **Comptage des jetons d'Anthropic** avant envoi : il est gratuit et sert à la borne de taille. Je le garde sur la clé, ce qui ne coûte rien. Sinon, j'emploie l'estimation prudente (deux caractères par jeton).

## 3. Dossiers en cours : finis sur leur voie, sans mélange
Bancs plantés (v8m, Luc 11,18 USD, garde à 28), cœurs algorithmiques, tâches de sabotage : ils finissent par l'interface, sans aucune cellule par l'abonnement. Une reprise après coupure se fait sur la même voie. Papier B isolé : fini à 14:01Z, 12,40 USD (Luc 7,03), et la vérification tient. Un dossier ne mêle jamais deux voies ; la voie est écrite dans sa composition.

## 4. Devis de l'essai de l'essaim, rejeu du jumeau compris (deux cycles, cinq espèces)
D'après `essaim-v1/devis-pilote-v6/devis-v6-2.txt`, pire cas :

| part | sans relance | avec relances |
|---|---|---|
| Fable + Opus (passe à l'abonnement, 0 USD d'interface) | 21,93 | 46,86 |
| Argon + Carbon (Google) | 26,85 en tout hors Claude | 62,94 |
| Astra (OpenAI) | (compris ci-dessus) | 16,55 |
| **reste par l'interface** | **26,85** | **79,49** |

**Rejeu du jumeau isolé** (collisionneur, même question, environ 12 USD réels jusqu'ici) : sa part Claude passe aussi à l'abonnement, et il reste environ 5 USD sur Google et OpenAI.
**Essai complet par l'interface** : environ 32 USD de pire sans relance, 85 USD avec relances. Le plafond du dossier est à fixer sur ce reste, sur Google et OpenAI seulement. La part Claude se paie en quota de Lazar et en temps (les vagues attendent les sessions).
**Appariement** : l'essaim et son jumeau doivent être sur la même voie, donc tous deux par l'abonnement pour la part Claude. Le jumeau déjà joué par l'interface ne s'apparie pas sans le dire ; Lazar a dit que c'est sans gravité pour le contenu.

**Puits étroits** (six espèces, devis 66,21 USD) : la part Luc (28,44 USD) passe à l'abonnement. Il reste **37,77 USD** sur l'interface, dont 17,45 sur Google et 20,32 sur OpenAI.

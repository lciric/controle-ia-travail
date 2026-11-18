# Contre-lecture du générateur de relance v3 — témoin de Bailey (addendum 8, option B)

Fichier lu : `docs/notes/reproduction-attaque-publiee-v1/generer-pieces-relance-confirmation-bailey-v3.py`,
empreinte `df13783afccb3dd2be8959a2479a82111994a24cb12e85525bde0e618c87b3e2` (copie inchangée de l'exemplaire contre-lu,
scellée à ce chemin le 18 novembre 2026 vers 02:45Z). Contre-lecture R2 par un sous-agent neuf (exécution de flux
`wf_c00aece0-baa`), après les six constats de la ronde précédente (`wf_603687eb-79b`).

**Verdict : prêt.** Aucun bloquant, aucun point à corriger. Les six constats précédents sont vérifiés corrigés
(marque de reprise obligatoire et bornée par version ; taux du budget exigé numérique ; etc.).

Remarques, gardées sans modification du fichier (une modification demanderait une nouvelle contre-lecture) :
1. La marque donnée n'est pas vérifiée comme écrite par le poste de la reprise nommée : seule sa version est bornée
   (≥ 5 pour `reprise-v10-N`). Pour cette relance, la marque est `poste-fini-reprise-v5.json` et la reprise
   `reprise-v10-2`, écrite par le poste v5 : la paire est juste. À vérifier à la main avant la génération (horodatage
   `fini` de la marque postérieur à la `fin` du bilan de reprise).
2. Sous l'option B seule, la conduite v16 garde le bloc de l'option A en code inerte (`OPTION_A = False`, constantes à
   `None`, `verifier_option_a` jamais appelée). Sans effet sur la dépense ; les seules différences actives avec les
   pièces scellées sont les deux de l'addendum 8 (filtre `cout(o) <= 1.4` du poste, garde d'entrée de la conduite).
3. Copier le fichier au chemin de l'addendum 8 sans le modifier et le sceller avant la génération réelle : fait
   (empreinte ci-dessus).

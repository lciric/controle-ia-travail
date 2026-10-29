# ?tat du Grand Collisionneur v2 Adaptatif (EFFORT MAX ? 64k/128k jetons ? Z?ro Troncature)

- **Tours ex?cut?s dynamiquement** : 4
- **D?pense M3 (30 Champions int?graux 64k)** : Claude=0.00 USD | Argon=0.51 USD
- **D?pense Collisionneur Adaptatif** : Claude=10.38 USD | Argon=4.02 USD | **Appels Jev** : 46
- **Matrice de Pr?dation Apprise $P[\text{Attaquant} \to \text{D?fenseur}]$** : `{"claude-fable-5-1": {"claude-fable-5-1": 1.0, "claude-opus-5-5": 1.0, "gemini-4-argon": 1.0}, "claude-opus-5-5": {"claude-fable-5-1": 5.933, "claude-opus-5-5": 1.0, "gemini-4-argon": 7.162}, "gemini-4-argon": {"claude-fable-5-1": 1.0, "claude-opus-5-5": 1.087, "gemini-4-argon": 1.0}}`

| Branche Finale | Mod?le | Dernier Tour | Historique Failles | Score Composite Jev | Rigueur Jev | Duels | Contr?les | Hyp=R?s | Caract?res |
|---|---|---|---|---|---|---|---|---|---|
| **Branche A** | `claude-fable-5-1` | Tour 4 | `[9, 6, 3]` | **4.23** | **3.86** | 0.17 | 0.52 | 0.32 | 33905 |
| **Branche B** | `claude-opus-5-5` | Tour 2 | `[1]` | **4.09** | **3.75** | 0.31 | 0.37 | 0.34 | 18138 |
| **Branche C** | `gemini-4-argon` | Tour 4 | `[8, 8, 7]` | **4.43** | **3.84** | 0.50 | 0.46 | 0.37 | 43001 |

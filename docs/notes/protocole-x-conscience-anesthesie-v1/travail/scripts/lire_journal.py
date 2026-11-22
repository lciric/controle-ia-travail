import sys, json
for line in open(sys.argv[1]):
    line = line.strip()
    i = line.find('{')
    if i < 0:
        print(line)
        continue
    nom = line[:i].strip()
    m = json.loads(line[i:])
    f = lambda k: f"{m[k][0]:.3f}±{m[k][1]:.3f}"
    print(f"{nom:26s} LZ(1)={f('lz_theta1.0')} LZ(.5)={f('lz_theta0.5')} LZ(2)={f('lz_theta2.0')} "
          f"étendue={m['etendue_hors_site'][0]:.4f} particip={f('participation')} gain={f('gain_norme_final')} perte={m['perte_nats']:.3f}")

import json,sys,time
l=json.load(open(sys.argv[1])); i=int(sys.argv[2]); c=float(sys.argv[3])
x=[x for x in l if x["id"]==i]
if not x: print("ABSENTE 0 0"); sys.exit()
x=x[0]; h=(time.time()-x["start_date"])/3600
base=h*x["dph_total"]
# sortie de données : champs *_billed en octets (constat du 23 novembre), prix en USD par Go
sortie=((x["inet_up_billed"] or 0)*(x["inet_up_cost"] or 0)+(x["inet_down_billed"] or 0)*(x["inet_down_cost"] or 0))/1e9
cum=base+sortie
if sortie>2.0 or cum<0 or cum>base+2.0: print(x["actual_status"], round(cum,3), "ANOMALIE"); sys.exit()
print(x["actual_status"], round(cum,3), "COUPURE" if cum+0.25*x["dph_total"]>=c else "ok")

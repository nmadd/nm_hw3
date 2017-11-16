from q11a import constructGraph, constructPrices
from vcg_bundles import VCG
file = open('q11b_logs.txt', 'w')


file.write(str(VCG(constructGraph(20), constructPrices(20))))

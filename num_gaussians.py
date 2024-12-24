import sys
from plyfile import PlyData
plydata = PlyData.read(sys.argv[1])
vertices = plydata['vertex']
print(f'Number of Gaussians: {vertices.count}')

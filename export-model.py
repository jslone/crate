import sys
import bpy

def polyStr(poly):
	return '        [' + ','.join(map(str,poly.vertices)) + ']'

def vertStr(vert):
	return '        [' + str(vert.co.x) + ',' + str(vert.co.y) + ',' + str(vert.co.x) + ']'

if len(sys.argv) < 7:
	print("Usage: blender --background <file> --python export-model.py -- <mesh>")
else:
	mesh = bpy.data.meshes[sys.argv[6]]
	print('{')
	print('    vertices: [')
	print(',\n'.join(map(vertStr,mesh.vertices)))
	print('    ],')
	print('    indices: [')
	print(",\n".join(map(polyStr,mesh.polygons)))
	print('    ]')
	print('}')
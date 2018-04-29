from ast import literal_eval

maps = ['delab_expanded',]
# 'delab_keyws',
# 'tech_interactive_network',
# 'values_interactive_network']

colors_dict = {
	'delab_expanded': {'rgb(0,196,255)': 'rgb(194, 74, 101)', 'rgb(255,85,132)': 'rgb(194, 74, 101)', 'rgb(115,192,0)': 'rgb(194, 74, 101)', 'rgb(76,70,62)': 'rgb(194, 74, 101)', 'rgb(255,136,5)': 'rgb(194, 74, 101)', 'rgb(223,137,255)': 'rgb(194, 74, 101)', 'rgb(0,189,148)': 'rgb(194, 74, 101)'}
# 'delab_keyws': {'rgb(140,185,0)', 'rgb(217,125,216)', 'rgb(0,199,255)', 'rgb(255,112,69)'}
# 'tech_interactive_network': {'rgb(198,134,233)', 'rgb(234,134,21)', 'rgb(46,144,114)', 'rgb(255,92,129)', 'rgb(0,202,255)', 'rgb(95,198,19)'}
# 'values_interactive_network': {'rgb(226,139,255)', 'rgb(128,107,104)', 'rgb(105,196,4)', 'rgb(0,175,135)', 'rgb(255,93,133)', 'rgb(0,199,255)', 'rgb(250,146,0)'}

}


for kw in maps:
	all_colors = []
	with open(kw + '/' + 'data.json', 'r') as f:
		data = f.read()
		data = literal_eval(data)
		for i, node in enumerate(data['nodes']):
			print(data['nodes'][i]['color'], colors_dict[kw][node['color']])
			data['nodes'][i]['color'] = colors_dict[kw][node['color']]
	# print(kw, set(all_colors))
	print(data['nodes'][10]['color'])
	with open(kw + '/' + 'data_new.json', 'w') as g:
		g.write(str(data).replace('\'','"'))
	# print(data)
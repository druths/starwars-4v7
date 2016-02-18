import os, os.path
import json

import zen

data_dir = os.path.join(os.path.dirname(__file__),'..','data')

def merge_nodes(G,merge_list):
	
	for merge_set in merge_list:
		neighbor_set = set()
		for n in merge_set:
			neighbor_set.update(G.neighbors(n))

		for n in merge_set:
			G.rm_node(n)

		neighbor_set.difference_update(set(merge_set))

		nn = '__'.join(merge_set)
		G.add_node(nn)
		for n in neighbor_set:
			G.add_edge(nn,n)

def load_json_net(fname):
	data = json.load(open(fname,'r'))

	nodes_list = data['nodes']
	char_id2name = {i:x['name'].replace(' ','_') for i,x in enumerate(nodes_list)}

	G = zen.Graph()
	for e in data['links']:
		G.add_edge(char_id2name[e['source']],char_id2name[e['target']],e['value'])

	return G

def load_mention_net(episode):
	episode = str(episode)
	fname = os.path.join(data_dir,'starwars-episode-%s-mentions.json' % episode)

	return load_json_net(fname)

def load_interaction_net(episode,all_chars=True):
	episode = str(episode)

	if all_chars:
		all_char_suffix = '-allCharacters'
	else:
		all_char_suffix = ''

	fname = os.path.join(data_dir,'starwars-episode-%s-interactions%s.json' % (episode,all_char_suffix))

	return load_json_net(fname)
	

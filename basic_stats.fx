# Set the python path to include helper python libs
PYTHONPATH=$(echo "\$PYTHONPATH:./src")

to_edgelists:
	###
	Write the star wars interaction networks to edge lists
	###
	code.py:
		import swdata

		def write_edgelist(fname,G):
			fh = open(fname,'w')
			for x,y in G.edges():
				print >>fh, '%s %s' % (x,y)

			fh.close()

		G4 = swdata.load_interaction_net(4)
		G7 = swdata.load_interaction_net(7)

		write_edgelist('$PLN(interaction_4.elist)',G4)
		write_edgelist('$PLN(interaction_7.elist)',G7)

num_chars:
	###
	Print the number of characters in episodes 4 vs 7
	###
	code.py:
		import swdata

		G4 = swdata.load_interaction_net(4)
		G7 = swdata.load_interaction_net(7)
		print '\\t4: %d' % len(G4)
		print '\\t7: %d' % len(G7)





# Create function of left_join with two arguments (hastable_1 and hashtable_2)
		# create new_list
		# traverse first hashtable
				# create index_list per value pair
				# append key to index_list
				# append value to list to lindex_list
				# append to new_list
		#traverse second hashtable
				# if key is in new_list
						# append value of same key in index_list
				# if not
						# append None
		# return new_list



def hashmap_left_join(hashtable_1,hashtable_2):
    # create new_list
    new_list = []
	#  traverse first hashtable
    for key_a,value_a in hashtable_1.items():
	    # create index_list per value pair
        index_list = []
        # print(key)
        index_list.append(key_a)
        # print(value)
        index_list.append(value_a)
        # print(index_list)
        for key_b,value_b in hashtable_2.items():
            # print(value_b)
            if index_list[0] != key_a:
                index_list.append(None)
            elif index_list[0] == key_a:
                index_list.append(value_b)

        new_list.append(index_list)
		# append key to index_list
		# append value to list to lindex_list
		# append to new_list
	#traverse second hashtable
		# if key is in new_list
			# append value of same key in index_list
		# if not
			# append None
    return new_list


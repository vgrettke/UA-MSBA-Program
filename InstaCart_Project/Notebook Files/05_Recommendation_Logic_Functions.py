# These methods can be viewed in recommendation_logic notebook


def getItemFromAllUsers(dictionary, list_of_cart_items):
    """This function finds a cart item in the dictionary of all user bigrams. It searches the keys and then the values for the matching bigram. 
    Parameters: 
        dictionary --> should be user_bigram_dict 
        list_of_cart_items ---> list of items in the cart, list of strings 
         
    NOTES: 
        This sets 'rec' as 'None' so this function shouldn't be run outside of an 
            'if' statement (rec == 'None')"""
    
    rec = 'None' # <-----------Recommendation, initialized as None

## find the key and return the value section ##
    if(len(list_of_cart_items) > 1): # if there's more than one item in the cart 
        returned_value = dictionary.get(list_of_cart_items[-1]) # most recent item in the cart, returns a dictionary or list
        if isinstance(returned_value, list):
            temp_list = returned_value
            rec = temp_list[0][0]
        elif isinstance(returned_value, dict):
            key_list = list(returned_value.keys()) # convert keys to a list
            rec = key_list[0] # get the first item in the list aka the recommendation 
        if rec == 'None':
            returned_value = dictionary.get(list_of_cart_items[-2]) # second most recent in the cart
            if isinstance(returned_value, list):
                temp_list = returned_value
                rec = temp_list[0][0]
            elif isinstance(returned_value, dict):
                key_list = list(returned_value.keys())
                rec = key_list[0]        
    else:
        returned_value = dictionary.get(list_of_cart_items[-1])
        if isinstance(returned_value, list):
            temp_list = returned_value
            rec = temp_list[0][0]
        elif isinstance(returned_value, dict):
            key_list = list(returned_value.keys())
            rec = key_list[0]
    ## look for 'search item' in values and return the key section 
    if rec == 'None':

        list_of_keys = [] # < ---------------- create list of keys 
        list_of_values = []  # < ------------- create list of values (dict)
        i = 0 #  < --------------------------- if value is found find the key at that index (counter)
        trial_list = []  # < ----------------- create a list that will be recreated with every iteration, holds the value of the key 
        trial_list_1 = [] # < ---------------- this list holds the keys if the instance of list_of_values[i] is a list 

        for key, value in dictionary.items():
            list_of_keys.append(key)
            length_of_list_of_keys = len(list_of_keys)
            list_of_values.append(value)
            if isinstance(list_of_values[i], dict): # this will happen most of the time 
                trial_list = list(list_of_values[i])
                length = list(range(0, len(trial_list), 1))
                for x in trial_list:                    
                    if len(list_of_cart_items) > 1:
                        for l in length:
                            if trial_list[l] == list_of_cart_items[0]:
                                rec = list_of_keys[i]
                                break
                            elif trial_list[l] == list_of_cart_items[1]:
                                rec = list_of_keys[i]
                                break
                    elif len(list_of_cart_items) == 1:
                        for l in length:
                            if trial_list[l] == list_of_cart_items[0]:
                                rec = list_of_keys[i]
                                break
            i += 1
            
    return rec


def getCurrentItems(user_id, order_id, dictionary):
    """This receives a str(user_id), str(order_id), and dictionary and will return a list of the items in their cart """
    temp_dict = {}
    temp_dict = dictionary
    if isinstance(user_id, str) == False:
        user_id = str(user_id)
    if isinstance(order_id, str) == False:
        order_id= str(order_id)
    cart_list = []
    if len(temp_dict[user_id]) > 3:
        cart_list.append(temp_dict[user_id]['product_one'])
        cart_list.append(temp_dict[user_id]['product_two'])
    else:
        cart_list.append(temp_dict[user_id]['product_one'])        
    return cart_list


def getItemFromCluster(cluster_dictionary, list_of_cart_items, users_cluster):
    """This function finds a cart item in the prospective cluster. It searches the keys and then the values for the matching bigram. 
    Parameters: 
        cluster_bigram_dict --> bigrams distributed by cluster 
        list_of_cart_items ---> list of items in the cart, list of strings 
        users_cluster --------> 'Cluster_X' format 
    NOTES: 
        This sets 'rec' as 'None' so this function shouldn't be run outside of an 
            'if' statement (rec == 'None')"""

    rec = 'None' # <-----------Recommendation, initialized as None

## find the key and return the value section ##
    if(len(list_of_cart_items) > 1): # if there's more than one item in the cart 
        returned_value = cluster_dictionary[users_cluster].get(list_of_cart_items[-1]) # most recent item in the cart, returns a dictionary or list
        if isinstance(returned_value, list):
            temp_list = returned_value
            rec = temp_list[0][0]
        elif isinstance(returned_value, dict):
            key_list = list(returned_value.keys()) # convert keys to a list
            rec = key_list[0] # get the first item in the list aka the recommendation 
        if rec == 'None':
            returned_value = cluster_dictionary[users_cluster].get(list_of_cart_items[-2]) # second most recent in the cart
            if isinstance(returned_value, list):
                temp_list = returned_value
                rec = temp_list[0][0]
            elif isinstance(returned_value, dict):
                key_list = list(returned_value.keys())
                rec = key_list[0]        
    else:
        returned_value = cluster_dictionary[users_cluster].get(list_of_cart_items[-1])
        if isinstance(returned_value, list):
            temp_list = returned_value
            rec = temp_list[0][0]
        elif isinstance(returned_value, dict):
            key_list = list(returned_value.keys())
            rec = key_list[0]

## look for 'search item' in values and return the key section 
    if rec == 'None':
        
        list_of_keys = [] # < ---------------- create list of keys 
        list_of_values = []  # < ------------- create list of values (dict)
        i = 0 #  < --------------------------- if value is found find the key at that index (counter)
        trial_list = []  # < ----------------- create a list that will be recreated with every iteration, holds the value of the key 
        trial_list_1 = [] # < ---------------- this list holds the keys if the instance of list_of_values[i] is a list 
        dict_to_list = [] # <----------------- convert the second item in the list of values (dictionary) to a list then string 

        
        for key, value in cluster_dictionary[users_cluster].items():
            list_of_keys.append(key)
            length_of_list_of_keys = len(list_of_keys)
            list_of_values.append(value)
            if isinstance(list_of_values[i], dict): # this will happen most of the time 
                trial_list = list(list_of_values[i])
                if len(list_of_cart_items) > 1:
                    if trial_list[0] == list_of_cart_items[0]:
                        rec = list_of_keys[i]
                        break
                    elif trial_list[0] == list_of_cart_items[1]:
                        rec = list_of_keys[i]
                        break
                elif len(list_of_cart_items) == 1:
                    if trial_list[0] == list_of_cart_items[0]:
                        rec = list_of_keys[i]
                        break
            elif isinstance(list_of_values[i], list):
                if len(list_of_cart_items) > 1:
                    length = len(list_of_values[i])
                    combined_list = list_of_values[i]
                    dict_to_list = list(combined_list[1])
                    second_item = dict_to_list[0]
                    trial_list_1.append(combined_list[0][0])
                    trial_list_1.append(second_item)
                    for x in trial_list_1:
                        if trial_list_1[0] == list_of_cart_items[0]:
                            rec = list_of_keys[i]
                            break
                        elif trial_list_1[1] == list_of_cart_items[0]:
                            rec = list_of_keys[i]
                            break
                        elif trial_list_1[0] == list_of_cart_items[1]:
                            rec = list_of_keys[i]
                            break
                        elif trial_list_1[1] == list_of_cart_items[1]:
                            rec = list_of_keys[i]
                            break
                else: 
                    continue
            length_of_list_of_values = len(list_of_values)
            if (list_of_cart_items[0] in trial_list):
#                 list_of_keys[i]
                rec = list_of_keys[i]
                if rec != 'None':
                    break
            if (list_of_cart_items[0] in trial_list_1):
#                 list_of_keys[i]
                rec = list_of_keys[i]
                if rec != 'None':
                    break
            i += 1
    return rec

def getDefaultRecommendation(dictionary, test_cart, test_cluster):
    """This gets a default recommendation based on the user's assigned cluster.
        Parameters:
            dictionary ----> cluster_bigram_dict
            test_cart------> list of cart items 
            test_cluster --> user's assigned cluster
        There is a random variable used in the method. 'Random' Package is imported within the function, so no need to import it when running the main file. """
    
    import random 
    rec = 'None'

    list_of_keys = list(dictionary[test_cluster]) # <- get the keys in the cluster 
    n = (len(list_of_keys) -1)
    random_index = random.randint(0, n) # get a random index in the list_of_keys

    first_bigram = list_of_keys[random_index]
    key_list = []

    returned_value = dictionary[test_cluster].get(first_bigram) # most recent item in the cart, returns a dictionary or list
    if isinstance(returned_value, list):
        temp_list = returned_value
        rec = temp_list[0][0]
    elif isinstance(returned_value, dict):
        key_list = list(returned_value.keys()) # convert keys to a list
        rec = key_list[0] # get the first item in the list aka the recommendation 

    return rec
import pynder
import pickle
import os
import sys
from time import sleep
from datetime import datetime


def save(obj, filename):
    """
    input: object, filename
    save object with specified filename
    """ 
    f = open(filename, 'w')
    p = pickle.Pickler(f)
    p.dump(obj)
    f.close()

def load(filename):
    """
    input: filename
    output: object
    load the object into program with specified filename
    """
    try:
        f = open(filename, 'r')
        u = pickle.Unpickler(f)
        obj = u.load()
        return obj
    except:
        open(filename, 'w')
        return []
    
def sort_data(users):
    
    users_attributes = []
    for user in users:
        if user is None:
            break  
        bio = ""
        for c in user.bio:
            if ord(c) < 128:
                bio = bio + c
        name = user.name
        age = user.age
        dob = user.birth_date
        schools = user.schools
        jobs = user.jobs
        connections = 0
        distance = user.distance_km
        time_elapsed = user.ping_time
        photos = user.photos
                
        users_attributes.append([name, age, dob, schools, jobs, distance, bio, time_elapsed, photos])
        
    return users_attributes

identification = sys.argv[1]
authentication = sys.argv[2]
pwd = sys.argv[3]
us = "data/" + sys.argv[4] + '/'

#print "p user: " + str(u)
# get all my current matches
session = pynder.Session(identification, authentication)
matches = session.matches()
matched_users = [match.user for match in matches]
matched_array = sort_data(matched_users)
print "length matches: " + str(len(matched_array))
    
print "save path: " + us + "liked_not_matched_users"
save(matched_array, us + "matched_users")

# get nearby users
nearby_users = session.nearby_users()

# get saved like users
old_users = load(pwd + us + "liked_not_matched_users")

if len(nearby_users) > 0:
    #swipe on all nearby users
    for user in nearby_users:
        print "liking: " + user.name
        user.like()
        
    # save all of the 
    nearby_array = sort_data(nearby_users)
    liked_not_matched_users = old_users + nearby_array 
    name_index = 0
    age_index = 1
        
    filtered_liked_not_matched_users = []
    for user in liked_not_matched_users:
        no_dups = True
        for match in matched_array:
            if (user[name_index] == match[name_index]) and  (user[age_index] == match[age_index]):
                no_dups = False
        
        if no_dups:
            filtered_liked_not_matched_users.append(user)
                

    #print "matched: " + str(len(matched_array))
    print "length before filter: " + str(len(liked_not_matched_users))
    print "length after filtering: " + str(len(filtered_liked_not_matched_users))
    
    
    #save(matched_array, us + "data_backup/matched_users")
    save(filtered_liked_not_matched_users, us + "liked_not_matched_users")
    #save(filtered_liked_not_matched_users, us + "data_backup/liked_not_matched_users")
else:
    print "out of swipes and out of luck"
    
    
    


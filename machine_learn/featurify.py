from utility import *
from time import sleep
import datetime

# read in the raw data
lu = load("../collect_data/data/me/matched_users")
lnmu = load("../collect_data/data/me/liked_not_matched_users")


top_12 = ["Princeton University",
          "Harvard University", 
          "Yale University",
          "Columbia University",
          "Stanford University",
          "University of Chicago",
          "Massachusetts Institute of Technology",
          "Duke University",
          "University of Pennsylvania",
          "California Institute of Technology",
          "Johns Hopkins University",
          "Dartmouth College",
          "Northwestern University"]

data = []

# data: name, age, dob, schools, jobs, distance, bio, time_elapsed, photos
def categorize(raw_data_set, category):
    
    data_set = []
    result_set = []
    
    for data_point in raw_data_set:
        
        features = []
        
        name = data_point[0]
        
        age = data_point[1]
        features.append(age)
        
        dob = data_point[2]
        
        schools = data_point[3]
        jobs = data_point[4]
        
        distance =data_point[5]
        features.append(distance)
        
        bio = data_point[6]
        
        time_elapsed = data_point[7]
        #features.append(time_elapsed)
        
        photos = data_point[8]

        # creating some new features to split on 
        name_length = len(name)
        features.append(name_length)
        
        mob = dob.month
        features.append(mob)
        
        schools_length = len(schools)
        features.append(schools_length)
        
        top = 0
        for school in schools:
            if school in top_12:
                top = 1
        features.append(top)
        
        job_length = len(jobs)
        features.append(job_length)
        
        bio = len(bio)
        features.append(bio)
        
        number_photos = len(photos)
        features.append(number_photos)
        
        data_set.append(features)
        result_set.append(category)
                
    return (data_set, result_set)
    
    
# categorize the matched as so
matched_tuple = categorize(lu, 1) 
matched = matched_tuple[0]
matched_result = matched_tuple[1]

# categorize as not matched
not_matched_tuple = categorize(lnmu, 0)
not_matched = not_matched_tuple[0]
not_matched_result = not_matched_tuple[1]

all_data = matched + not_matched
all_result = matched_result + not_matched_result


print all_data
print all_result
save(all_data, "data")
save(all_result, "data_result")
        



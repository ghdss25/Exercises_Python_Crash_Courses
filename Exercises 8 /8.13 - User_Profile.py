## 8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
## profile of yourself by calling build_profile(), using your first and last names
## and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):

      user_info['first_name'] = first
      user_info['last_name'] = last

      return user_info

user_profile = build_profile('gustavo', 'henrique', location = 'princeton', field = 'development')


print(user_profile)

def build_physical(age, height, **user_physical):

      user_physical['age_physical'] = age
      user_physical['height_physical'] = height

      return user_physical

user_numbers = build_physical('30', '1.80', location1 = 'new', field = 'high')

print(user_numbers)

def feature(typical_person, like_do, **user_tasks):

      user_tasks['typical person'] = typical_person
      user_tasks['like do'] = like_do

      return user_tasks

Data_person_defination = feature('kind', 'play soccer', location2 = 'benefits', field = 'sports')

print(Data_person_defination)

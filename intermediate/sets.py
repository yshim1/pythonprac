#Sets

"""
Sets are unordered, contain no duplicates.
Sets are helpful in organizing items and performing set mathematics

Immutable version of a set is called a frozenset
"""

#Creating a set
s1 = set()
s2 = {'pop', 'punk', 'rock'}
s3 = set(['name', 'number', 'origin'])
s4 = {item[:3] for item in s3}
print(s4)

#Frozen set
#IMMUTABLE
fs1 = frozenset()
fs2 = frozenset(['country', 'punk', 'rap'])

#add method
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tag_set = set(song_data['Retro Words'])
tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

song_data = {'Retro Words': tag_set}

#Update method
# Create a set to hold the song tags
song_tags = {'country', 'folk', 'acoustic'}

# Add more tags using a hashable object (such as a list of elements)
other_tags = ['live', 'blues', 'acoustic']
song_tags.update(other_tags)

print(song_tags)

#Removing from a set
#removes value from a set, if value is not in set, key error is thrown
#discard works similarly but there is no exception if the value is not in the set
song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')

song_data_users = {'Retro Words': tag_set}

#Finding elements in a set with keyword in
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
bad_tags = []
for x in tag_set:
  if x not in allowed_tags:
    bad_tags.append(x)

for x in bad_tags: #Cannot iterate through a set and remove. Sets must remain same size throughout iteration or runtime error will be thrown
  tag_set.remove(x)

song_data_users['Retro Words'] = tag_set
print(song_data_users)

#Introduction of set operations
"""
Union
Intersections (and intersection updates)
Differences (and difference updates)
Symmetric Differences (and symmetric difference updates)
"""

#Union
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Get the union using the .union() method
combined_tags = prepare_to_py.union(py_and_dry)
print(combined_tags)

#Using the | Operator
frozen_combined_tags = py_and_dry | prepare_to_py
print(frozen_combined_tags)

"""
Note: when using union, the new set will take the result of the left operand. In the first example, the elft operand is a set, 
in the 2nd example, the left operand is a frozenset
"""
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Checkpoint 1
new_song_data = {}

# Checkpoint 2
for key, val in song_data.items():
    song_tag_set = set(val)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_tag_set | user_tag_set

print(new_song_data)

#Set intersection: will only take the similar items from each set
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the intersection between them while providing the `frozenset` first.
frozen_intersected_tags = py_and_dry.intersection(prepare_to_py)
print(frozen_intersected_tags)

# Find the intersection using the operator `&` and providing the normal set first
intersected_tags = prepare_to_py & py_and_dry
print(intersected_tags)

#.intersection_update() will update the original set to contain the result of the intersection
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Checkpoint 1
tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])

# Checkpoint 2
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = val

print(recommended_songs)

#Difference: used to find unique elements in one set
#This returns a set which contains only the elements from the first set which are not found in the second set
# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the elements which are only in prepare_to_py
only_in_prepare_to_py = prepare_to_py.difference(py_and_dry)
print(only_in_prepare_to_py)

#Using operator instead
only_in_py_and_dry = py_and_dry - prepare_to_py
print(only_in_py_and_dry)

#using the difference_update() method will instead update the original set instead of returning a new set or frozenset object

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])

recommended_songs = {}
for key, val in song_data.items():
  for item in val:
    if item in tag_diff:
      if key not in user_liked_song and key not in user_disliked_song:
        recommended_songs[key] = item
print(recommended_songs)

#Symmetric Difference: include all elements from the sets which are in one or the other but not both (opposite of intersection)
#.symmetric_difference() or ^ operator works

# Given a set and frozenset of song tags for two python related hits
prepare_to_py = {'rock', 'heavy metal', 'electric guitar', 'synth'}

py_and_dry = frozenset({'classic', 'rock', 'electric guitar', 'rock and roll'})

# Find the elements which are exclusive to each song and not shared using the method
exclusive_tags = prepare_to_py.symmetric_difference(py_and_dry)
print(exclusive_tags)

#Using the operand instead
frozen_exclusive_tags = py_and_dry ^ prepare_to_py
print(frozen_exclusive_tags)

#using the .symmetric_difference_update() method will update the original set instead of returning new set object


music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])
frozen_tag_union = my_tags.union(music_tags)
regular_tag_intersect = music_tags.intersection(my_tags)
frozen_tag_difference = my_tags - music_tags
regular_tag_sd = music_tags ^ my_tags
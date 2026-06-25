import pandas as pd
import numpy as np

# App data
app_data = {
  'app_name': [
    'YouTube', 'TikTok', 'Instagram', 'Spotify', 'Duolingo', 
    'Twitter', 'Headspace', 'Discord', 'Depop'
  ],
  'category': [
    'Video', 'Social Media', 'Social Media', 'Music', 'Education',
    'Social Media', 'Health', 'Communication', 'Shopping'
  ],
  'rating': [
    4.7, 4.6, 4.5, 4.6, 4.7,
    4.3, None, 4.7, 4.4
  ],
  'downloads_millions': [
    5000, 3000, 3500, 2000, None,
    1500, 500, 600, 200
  ]
}

# Create the DataFrame
apps = pd.DataFrame(app_data)

#Sorting by on rating -> Descending means high to low

rating_high_to_low = apps.sort_values(by='rating', ascending=False)
print(rating_high_to_low)


#Renaming columns

rating_to_score= apps.rename(columns={'rating': 'score'})
print(rating_to_score)


#Adding columns
apps['Number of users'] = ['42424',424242,424242,42424,46346,12531531,5321513,535135,531513]
print(apps)

#Adding columns with computation
apps['Average rating'] = np.mean(apps.rating)
print(apps)
import pandas as pd
import numpy as np

d = {'KW': [32, 32,32,32, 33,33], 'likes': [3323, 4222,1231,2000,1222,3322], 'comments':[39,75,10,50,40,23]}
sample_post_data = pd.read_csv('csvs/out.csv') #aka sample post data
#print(sample_post_data)
#sampe_post_data =[{"KW":42,"likes":3213,"comments":23},{"W1"},{"W1"},{"W2"},{"W2"},{"W2"}] #[{KW,


def basic_stat(spd):
    #print(np.mean(spd['likes']))
    #print(np.mean(spd['comments']))
    posts_in_tf = len(spd)
    avg_likes = int(np.mean(spd['likes']))
    total_likes = int(np.sum(spd['likes']))
    avg_comments = int(np.mean(spd['comments']))
    total_comments = int(np.sum(spd['comments']))
    #post_freq = spd['KW'].value_counts()
    mip = spd.sort_values('likes',ascending=False).iloc[:5]

    #print(post_freq.keys()[0])
    #print(' Average likes: ' + str(avg_likes)+ '\n Total likes: ' + str(total_likes) + '\n Average comments: ' + str(avg_comments) +' \n Total comments: '+ str(total_comments) )
    print('\__Statistics created successfully')
    return {"posts_in_tf":posts_in_tf,"avg_likes":avg_likes,"ttl_likes":total_likes,"avg_comments":avg_comments,"ttl_comments":total_comments,"post_freq":2,'mip':mip}


def threeMo_stat(input_data):
    spd = input_data#[input_data['date']<=3]
    posts_in_tf = len(spd)
    print(posts_in_tf)
    avg_likes = int(np.mean(spd['likes']))
    total_likes = int(np.sum(spd['likes']))
    avg_comments = int(np.mean(spd['comments']))
    total_comments = int(np.sum(spd['comments']))
    #post_freq = spd['KW'].value_counts()
    mip = spd.sort_values('likes',ascending=False).iloc[:5]

    #print(post_freq.keys()[0])
    #print(' Average likes: ' + str(avg_likes)+ '\n Total likes: ' + str(total_likes) + '\n Average comments: ' + str(avg_comments) +' \n Total comments: '+ str(total_comments) )
    print('\__Statistics created successfully')
    return {"posts_in_tf":posts_in_tf,"avg_likes":avg_likes,"ttl_likes":total_likes,"avg_comments":avg_comments,"ttl_comments":total_comments,"post_freq":2,'mip':mip}



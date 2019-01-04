

import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import pandas as pd
from sklearn.metrics.pairwise import pairwise_distances

rating=random.randint(low=1,high=10,size=(100,2))
review_mobile=random.randint(low=1,high=5,size=(100,1))
final_rating=append(review_mobile,rating,axis=1)

unique_mob=unique(final_rating[:,1])
unique_mob=reshape(unique_mob,(unique_mob.shape[0],1))
mobile_rating=random.randint(low=1,high=5,size=(unique_mob.shape[0],6))
final_mob_rating=append(unique_mob,mobile_rating,axis=1)

final_rating=array(final_rating)
n_user=unique(final_rating[:,2])
data_matrix = zeros((10,10))

for i in range(0,final_rating.shape[0]):
    data_matrix[final_rating[i,1]-1,final_rating[i,2]-1]=final_rating[i,0]

user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')

print(user_similarity)
print(item_similarity)

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        ratings_diff = (ratings - mean_user_rating[:, newaxis])
        pred = mean_user_rating[:, newaxis] + similarity.dot(ratings_diff) / array([abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / array([abs(similarity).sum(axis=1)])
    return pred

user_prediction = predict(data_matrix, user_similarity, type='user')
item_prediction = predict(data_matrix, item_similarity, type='item')
global maxh
print(user_prediction)
for i in range(0,user_prediction.shape[0]):
    maxh=0
    for j in range(0,user_prediction.shape[1]):
        if user_prediction[i,j] > user_prediction[i,maxh]:
            maxh=j
    print("User ",i+1,":",maxh," Mobile")

for i in range(0,item_prediction.shape[1]):
    maxh=0
    for j in range(0,item_prediction.shape[0]):
        if user_prediction[j,i] > user_prediction[maxh,i]:
            maxh=j
    print("Mobile ",i+1,":",maxh," User")

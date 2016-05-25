import sys
import re

reviews = open(sys.argv[1]).read().split("\n")
t_reviews = open(sys.argv[2]).read().split("\n")

#2.8.1 Conversion for each review a tuple of labels and feature vector
#2.8.8 Add the processing of test data

def read_instance(num,t_num):
    element = re.split(u" |:",reviews[num])
    t_element = re.split(u" |:",t_reviews[t_num])
    label = int(element[0])
    t_label = int(t_element[0])
    del element[0]
    del t_element[0]
    vector_list = [(int(i),int(j)) for (i,j) in zip(element[::2], element[1::2])]
    t_vector_list = [(int(i),int(j)) for (i,j) in zip(t_element[::2], t_element[1::2])]
    label_vector = (label,vector_list)
    t_label_vector = (t_label,t_vector_list)
    return(label_vector,vector_list,t_label_vector)



#2.8.2 Convert all the data to the list of instances
#2.8.3 Calculate the maximum index of the feature vector
#2.8.8 Add the processing of test data

def read_data():
    num = 0
    t_num = 0
    train_data = []
    test_data = []
    index = []
    for num in range(len(reviews) - 1):
        train_data.append(read_instance(num,t_num)[0])
        for vector in read_instance(num,t_num)[0][1]:
            index.append(int(vector[0]))
    max_index = max(index)
    for t_num in range(len(t_reviews) - 1):
        test_data.append(read_instance(num,t_num)[2])
    return(train_data,max_index,test_data)

#2.8.4 Create an initialized the weight vector

weight = []
m_index = read_data()[1]

for i in range(m_index + 1):
    weight.append(int(0))



#2.8.5 Feature vectors add or subtraction to the weight vector

def add_fv():
    num = 0
    t_num = 0
    for num in range(len(reviews) - 1):
        for vector in read_instance(num,t_num)[0][1]:
            weight[vector[0]] += vector[1]
    return(weight)

def sub_fv():
    num = 0
    t_num = 0
    for num in range(len(reviews) - 1):
        for vector in read_instance(num,t_num)[0][1]:
            weight[vector[0]] -= vector[1]
    return(weight)


#2.8.6 Calculate an inner product of feature vectors and the weight vector 

def mult_fv(vector):
    for vector in read_data()[0][1]:
        if vector[0] <= len(weight):
            inner += weight[vector[0]] * vector[1] 
    return(inner)



#2.8.7 Check the match of the code and update the weight vector

def update_weight():
    inner = int(0)
    for instance in read_data()[0]:
        for vector in instance[1]:
            if vector[0] <= len(weight):
                inner += weight[vector[0]] * vector[1] 
        if instance[0] > 0 and inner <= 0:
            for vector in instance[1]:
                weight[vector[0]] += vector[1]
        if instance[0] < 0 and inner >= 0:
            for vector in instance[1]:
                weight[vector[0]] -= vector[1]



#2.8.9 Return the accuracy rate for the test data

def evaluate():
    answer = int(0)
    instance_count = int(0)
    for t_instance in read_data()[2]:
        instance_count += 1
        inner = int(0)
        for vector in t_instance[1]:
            if vector[0] < len(weight):
                inner += weight[vector[0]] * vector[1]
        if t_instance[0] > 0 and inner >= 0:
            answer += 1
        elif t_instance[0] < 0 and inner <= 0:
            answer += 1
    rate = answer / instance_count
    print(answer,instance_count,rate)



#2.8.10 Evaluate the test data by reading the learning data

for i in range(int(sys.argv[3])):
    update_weight()
evaluate()

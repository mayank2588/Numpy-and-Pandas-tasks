# --------------
#Code starts here
high = census[census[:, 1]>10]
low = census[census[:, 1]<=10]
avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]
print(avg_pay_high,avg_pay_low)

if (avg_pay_high > avg_pay_low):
    print(avg_pay_high* 100)
else :
    print('Education doesnt matter')


# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census = np.concatenate((data, new_record), axis=0)
print(census)



# --------------
#Code starts here
race_0 = census[census[: , 2] == 0]
race_1 = census[census[: , 2] == 1]
race_2 = census[census[: , 2] == 2]
race_3 = census[census[: , 2] == 3]
race_4 = census[census[: , 2] == 4]

len_0 = np.size(race_0,0)
len_1 = np.size(race_1,0)
len_2 = np.size(race_2,0)
len_3 = np.size(race_3,0)
len_4 = np.size(race_4,0)

print(len_0,len_1,len_2,len_3,len_4)
len_array = (len_0,len_1,len_2,len_3,len_4)

len_min = np.asarray(len_array).min(0)
minority_race=3
print(minority_race)





# --------------
#Code starts here
import numpy as np
age = census[:,0]
# temp = np.shape(census)
# print(temp)
max_age= np.max(age, axis=0)
min_age= np.min(age, axis=0)
age_mean = np.mean(age, axis=0)
age_std = np.std(age, axis=0)
print(int(max_age))
print(int(min_age))
print("%.2f" % age_mean)
print("%.2f" % age_std)
print('Country is old')



# --------------
#Code starts here
# age = [census[:,0] > 60]
senior_citizens = census[census[:,0] > 60]
working_hours_sum= senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len = np.size(senior_citizens,0)
print(senior_citizens_len)
avg_working_hours =  np.divide(working_hours_sum,senior_citizens_len)
print("{:.2f}".format(avg_working_hours))



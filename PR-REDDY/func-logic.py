# from cal import sumof, mulof - if we call the modules like this, we don't need to call the function like cal.sumof(a)
import cal
a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20]
sum_of_values_ofa = cal.sumof(a)
sum_of_values_ofb = cal.sumof(b)
print(sum_of_values_ofa)
print(sum_of_values_ofb)
sum_of_values_ofc = cal.mulof(a)
sum_of_values_ofd = cal.mulof(b)
print(sum_of_values_ofc)
print(sum_of_values_ofd)  
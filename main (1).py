#this program is writtem by me#
input= "Apple"
print ("this is the original string: "+input)

all_freq={}

for i in input:
  if i in all_freq:
    all_freq[i] +=1
  else:
    all_freq=1

res=min(all_freq,key=all_freq.get)

print("this is the final result: "+str(res))

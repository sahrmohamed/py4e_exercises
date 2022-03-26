str = 'X-DSPAM-Confidence:0.8475'
cpos=str.find(":")
nums = str[cpos+1:]
print(float(nums))

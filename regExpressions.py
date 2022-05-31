import re

mystr = "You can learn any programming language, whetehr it is Python2, Python3, Perl, Java, javascript or PHP."

#Match beginning of string
a = re.match("You", mystr)
print(a)
print(a.group()) 
a = re.match("you", mystr, re.IGNORECASE)
print(a)
print(a.group()) 

#search within a string
#regex any character repeating more than once followed by a digit followed by strings with atmost two whitespaces in the string followed by zero or more occurences of a word character 
arp = "22.22.22.1   0   b4:a9:ff:c8:45 VLAN#222      L"
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(a.group(4))
print(a.groups()) #puts each search group in a tuple

#findall
# regex 2 consecutive digits followed by a dot
# then two digits followed by a dot
# then two numbers 0-9 followed by a dot
# lastly a digit from 0-9 that occurs 1-3 times

a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
print(a)

#findall put in tuple -no .-
arp = "22.22.22.1   0   b4:a9:ff:c8:45 VLAN#222    10.10.10.10   L"
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)

#sub method
#replace all occurence of pattern with string
arp = "22.22.22.1   0   b4:a9:ff:c8:45 VLAN#222      L"

b = re.sub(r"\d", "7", arp)
print(b)
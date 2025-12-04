a= "AdithyacollegeofEngineeringMadanapalle"
print(a[27::1])
print(a[27::1][:3:])

# 2nd one
b= "AdithyacollegeofEngineeringMadanapalle"
print(b[:7:])
print(b[:7:][-1::-1])
# 3st one
c= "AdithyaCollegeofEngineeringMadanapalle"
print(c[7:14:1])

#secound file
d="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(d[0:1:])
print(d[8:9:1])
print(d[16:17:1])
print(d[24:25:1])
#third file
e="AB2CD3EF4GH5IJ6KL7MN8OP9QR1ST2UV3WX4YZ"
print(e[2::3])
print(e[2::3][:6:2])
print(bin(int(e[2::3][:6:2])))
#fourth file
f="1A2B3C4D5E6F7G8H9I1J2K3L4M5N6O7P8Q9R1S2T3U4V5W6X7Y8Z"
print(f[0::3])
print(f[0::3][2:9:2])
print(f[0::3][2:9:2][::-1])
print(oct(int(f[0::3][2:9:2][::-1])))
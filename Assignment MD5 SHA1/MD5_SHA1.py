import hashlib

a = input("Enter the msg:").encode()
ans = hashlib.md5(a)

ans1 = hashlib.sha1(a)

print("MD5 : ",ans.hexdigest())
print("SHA1 : ",ans1.hexdigest())
**Level 0**  

![image](https://github.com/user-attachments/assets/4a0964d5-7824-44f5-b419-8a20adcb06c7)  
[ssh -p 2220 bandit0@bandit.labs.overthewire.org]{.mark}  

[ls]{.mark}  

[cat readme]{.mark}  

ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If  

**Level 1**  

[cat ./-]{.mark}  
Level 0  

ssh -p 2220 bandit0@bandit.labs.overthewire.org  
ls  
cat readme  

ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If  

Level 1  

cat ./-  
263JGJPfgU6LtdEvgfWU1XP5yac29fFx  

Level 2  
I tried cat ./\-\-spaces\ in\ this\ filename\-\- but that didn’t work  
So I did cat ./- and then pressed tab  
cat ./--spaces\ in\ this\ filename—  
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx  

Level 3  

2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ  

Level 4  
cat ./* gives output of all files  
then I just selected human readable text  
U4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQwx  
The problem with this was that I didn’t know when the file starts and ends so I ended up doing  
cat ./-file07 manually  

4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw  

Level 5  

find . -size 1033c  
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG  

Level 6  
find / -type f -user bandit7 -group bandit6  
gives a whole bunch of permission denied with a single  
/var/lib/dpkg/info/bandit7.password  
cat /var/lib/dpkg/info/bandit7.password  
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj  

Level 7  

grep millionth data.txt  
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc  

Level 8  
sort data.txt | uniq -u  

4CKMh1JI91bUIZZPXDqGanal4xvAg0JM  

Level 9  

![image](https://github.com/user-attachments/assets/677f0032-5494-44f6-9d75-f29fa33d2a81)  

FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey  

Level 10  

![image](https://github.com/user-attachments/assets/87de86b8-9614-41ba-a6ca-bb033b098371)  

dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr  

Level 11  

![image](https://github.com/user-attachments/assets/e2faf23d-a2fd-4cc7-a84d-f1f7e56c5ad1)  

![image](https://github.com/user-attachments/assets/41ca58ba-2b8b-47c9-9a41-9303e34fe55e)  

(forgot : after upper)  

![image](https://github.com/user-attachments/assets/76188f51-6fd6-4971-b201-880cef24d2f5)  

7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4  

Level 12  

![image](https://github.com/user-attachments/assets/f6951467-910c-4a4b-a1f7-f80f704fc58c)  

![image](https://github.com/user-attachments/assets/c48226d4-5d14-4fb6-89b8-b4444f205e18)  
![image](https://github.com/user-attachments/assets/c0095afc-c0f7-4002-8e8d-d6d0997adfec)  

Found out its gzip compressed  

![image](https://github.com/user-attachments/assets/305b80fc-ba18-4004-8dff-5226717d679d)  
![image](https://github.com/user-attachments/assets/d973a3aa-3a8c-42ff-a392-7c7b39287d79)  
![image](https://github.com/user-attachments/assets/578bb5a4-21cd-494d-aee5-b2e2855f96b6)  

Its also bzip2 compressed  

![image](https://github.com/user-attachments/assets/304fd5e5-dfb8-4c04-a3e1-2f6fe7c66f50)  
![image](https://github.com/user-attachments/assets/e1c868d1-317c-47d1-8fef-8e0f5a86b95f)  

GZIP AGAIN ISTGG  

![image](https://github.com/user-attachments/assets/f9e360a1-175b-4269-9ded-35e024ded154)  

Repeated again and got a tar compressed file renamed to final.tar  
After repeating using tar, gzip and bzip2 again god knows how many times  
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn  

Level 13  
Sshkey.private has  
-----BEGIN RSA PRIVATE KEY-----  
MIIEpAIBAAKCAQEAxkkOE83W2cOT7IWhFc9aPaaQmQDdgzuXCv+ppZHa++buSkN+  
gg0tcr7Fw8NLGa5+Uzec2rEg0WmeevB13AIoYp0MZyETq46t+jk9puNwZwIt9XgB  
ZufGtZEwWbFWw/vVLNwOXBe4UWStGRWzgPpEeSv5Tb1VjLZIBdGphTIK22Amz6Zb  
ThMsiMnyJafEwJ/T8PQO3myS91vUHEuoOMAzoUID4kN0MEZ3+XahyK0HJVq68KsV  
ObefXG1vvA3GAJ29kxJaqvRfgYnqZryWN7w3CHjNU4c/2Jkp+n8L0SnxaNA+WYA7  
jiPyTF0is8uzMlYQ4l1Lzh/8/MpvhCQF8r22dwIDAQABAoIBAQC6dWBjhyEOzjeA  
J3j/RWmap9M5zfJ/wb2bfidNpwbB8rsJ4sZIDZQ7XuIh4LfygoAQSS+bBw3RXvzE  
pvJt3SmU8hIDuLsCjL1VnBY5pY7Bju8g8aR/3FyjyNAqx/TLfzlLYfOu7i9Jet67  
xAh0tONG/u8FB5I3LAI2Vp6OviwvdWeC4nOxCthldpuPKNLA8rmMMVRTKQ+7T2VS  
nXmwYckKUcUgzoVSpiNZaS0zUDypdpy2+tRH3MQa5kqN1YKjvF8RC47woOYCktsD  
o3FFpGNFec9Taa3Msy+DfQQhHKZFKIL3bJDONtmrVvtYK40/yeU4aZ/HA2DQzwhe  
ol1AfiEhAoGBAOnVjosBkm7sblK+n4IEwPxs8sOmhPnTDUy5WGrpSCrXOmsVIBUf  
laL3ZGLx3xCIwtCnEucB9DvN2HZkupc/h6hTKUYLqXuyLD8njTrbRhLgbC9QrKrS  
M1F2fSTxVqPtZDlDMwjNR04xHA/fKh8bXXyTMqOHNJTHHNhbh3McdURjAoGBANkU  
1hqfnw7+aXncJ9bjysr1ZWbqOE5Nd8AFgfwaKuGTTVX2NsUQnCMWdOp+wFak40JH  
PKWkJNdBG+ex0H9JNQsTK3X5PBMAS8AfX0GrKeuwKWA6erytVTqjOfLYcdp5+z9s  
8DtVCxDuVsM+i4X8UqIGOlvGbtKEVokHPFXP1q/dAoGAcHg5YX7WEehCgCYTzpO+  
xysX8ScM2qS6xuZ3MqUWAxUWkh7NGZvhe0sGy9iOdANzwKw7mUUFViaCMR/t54W1  
GC83sOs3D7n5Mj8x3NdO8xFit7dT9a245TvaoYQ7KgmqpSg/ScKCw4c3eiLava+J  
3btnJeSIU+8ZXq9XjPRpKwUCgYA7z6LiOQKxNeXH3qHXcnHok855maUj5fJNpPbY  
iDkyZ8ySF8GlcFsky8Yw6fWCqfG3zDrohJ5l9JmEsBh7SadkwsZhvecQcS9t4vby  
9/8X4jS0P8ibfcKS4nBP+dT81kkkg5Z5MohXBORA7VWx+ACohcDEkprsQ+w32xeD  
qT1EvQKBgQDKm8ws2ByvSUVs9GjTilCajFqLJ0eVYzRPaY6f++Gv/UVfAPV4c+S0  
kAWpXbv5tbkkzbS0eaLPTKgLzavXtQoTtKwrjpolHKIHUz6Wu+n4abfAIRFubOdN  
/+aLoRQ0yBDRbdXMsZN/jvY44eM+xRLdRVyMmdPtP8belRi2E2aEzA==  
-----END RSA PRIVATE KEY-----  


Level 14  

![image](https://github.com/user-attachments/assets/39f0e13b-63b5-46c4-9394-124cc4e9e0be)  

Fix this by doing `chmod 600 sshkey.private`  

Then repeat and get access  

![image](https://github.com/user-attachments/assets/9dd62d32-cd3b-42bc-a4af-37c51dee7525)  

MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS  

Level 15  

![image](https://github.com/user-attachments/assets/dcfae17c-fcc7-4bf5-80b4-b753613701f7)  

8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo  

Do `openssl s_client -connect localhost:30001`  
And then type password  

kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx  


# WAD-ITMO
This repository dedicated entirely for Web-Apps Development course in ITMO uni.

In the second assignment, I made basic Login/Signup system with 2 pages. On the first you can either signup with a new email or login to the existing profile. And the second page is a profile page with some personal info and a silly cat. As a DB mongoDB was used in docker container that can be launched from docker-compose file.

While creatin those simple pages i used pymongo to connect to mongodb, passlib library to hash passwords and verify inserted password and some other flask functionality like session, request, jsonify. I also added small JS scripts to "parse" imputed values in frontend to backend.

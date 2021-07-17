# testProject
There you can register user via email and password
https://mirjahon604.pythonanywhere.com/user/register/ 
![img_2.png](img_2.png)
After registering you will receive verification message to your email address
![img_4.png](img_4.png)
Via going through this link you can verify your email 
![img_5.png](img_5.png)
Email Verified
For email verification I used jwt. I generated token for particular user and used it for verification. For sending email I used smtp package

Only after verifiying your email you can login
https://mirjahon604.pythonanywhere.com/user/login/ 
![img_6.png](img_6.png)
After entering valid email and password api returns token. It can be used in frontend side of website to identify user 
![img_7.png](img_7.png)
For authentication I used Token authentication. It can be used in frontend side of website to identify user.
We have only api so to test out we will use modheader extension to activate token
![img_8.png](img_8.png)

There you can see, update and delete your account
https://mirjahon604.pythonanywhere.com/user/me/
![img_9.png](img_9.png)
Now i'm gonna update user's first and last name
![img_10.png](img_10.png)
Now it's updated
You can also delete user by sending delete request

There you can update your password
https://mirjahon604.pythonanywhere.com/user/update-password/
You enter your email addres and password change message will send to this
![img_11.png](img_11.png)
There is the message and by clicking the link you can update your password
![img_12.png](img_12.png)
Password successfully changed
![img_13.png](img_13.png)
![img_14.png](img_14.png)


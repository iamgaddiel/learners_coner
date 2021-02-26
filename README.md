Learners Corner is the most reliable learning Web App that grantrantee learners Academic success. 
We are dedicated to revolutionizing online education in Africa by helping learners reach their full academic
potentials, building the capacity of learners and enhancing the digital learning experience to achieve
academic excellence. 

Our approach is to empower learners to study on their own at their own pace,
offering practice exercises, instructional class videos, personalised learning interface, live classes. We
make online learning personalised! We help our students Pass WAEC, NECO and JAMB with ease. We
build the capacity of teachers to navigate changes and uncertainty through our 21st century teacher’s
content on the teachers dashboard, moreso, they get certified after examinations. We connect our
learners to global opportunities through our international partners.

With award winning technological innovation that has empowered thousands of students and teachers,
Learners Corner offers more than education and learning. We liberate the minds of learners to new
possibilities. We are positioning the minds of learners for the 4​ th industrial revolution that will be driven
by technological innovations. The future of learning and teaching will go beyond the four walls of the
classroom.

+++++++ API ENDPOINTS 

• /dj-rest-auth/login/ (POST)
    – username
    – email
    – password
    Returns Token key

• /dj-rest-auth/logout/ (POST)

• /dj-rest-auth/password/reset/ (POST)
    – email

• /dj-rest-auth/password/reset/confirm/ (POST)
    – uid
    – token
    – new_password1
    – new_password2
    Note: uid and token are sent in email after calling /dj-rest-auth/password/reset/

• /dj-rest-auth/password/change/ (POST)
    – new_password1
    – new_password2
    – old_password

    Note: OLD_PASSWORD_FIELD_ENABLED = True to use old_password.
    Note: LOGOUT_ON_PASSWORD_CHANGE = False to keep the user logged in after password
    change

• /dj-rest-auth/user/ (GET, PUT, PATCH)
    – username
    – first_name
    – last_name
    Returns pk, username, email, first_name, last_name

• /dj-rest-auth/token/verify/ (POST)
    – token

    Returns an empty JSON object.
    Note: REST_USE_JWT = True to use token/verify/ route.
    Note: Takes a token and indicates if it is valid. This view provides no information about a
    token’s fitness for a particular use. Will return a HTTP 200 OK in case of a valid token and
    HTTP 401 Unauthorized with {"detail": "Token is invalid or expired", "code": "token_not_valid"} 
    in case of a invalid or expired token.

• /dj-rest-auth/token/refresh/ (POST)
    – refresh
    Returns access
    Note: REST_USE_JWT = True to use token/refresh/ route.
    
    Note: Takes a refresh type JSON web token and returns an access type JSON web token if the refresh
    token is valid. HTTP 401 Unauthorized with {"detail": "Token is invalid or
    expired", "code": "token_not_valid"} in case of a invalid or expired token.


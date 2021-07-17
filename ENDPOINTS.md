BASE URL => https://learnersconer.pythonanywhere.com/api/

+++++++++++++++++++++++++++++++++++++++ AUTH ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• user/phone/confirm/ (POST)
– phone
Returns
-- {"status": 'error', "message": "phone number already exists"}
-- {"status": "success", "message": "phone number not found"}


• /user/login/ (POST)
– phone
– password
Returns => token, user_id,username, full_name, phone, country, level, email, role

• /user/register/ (POST)
– fullname
– email
– phone
– role | teacher or student
– country
– level
– referral_code
– syllable

• user/profile/{user_id}/update/ (PUT)
dob : format YYYY-MM-DD
fullname
phone
level
gender (int) : 0 -> Male, 1 -> Female

• /dj-rest-auth/logout/ (GET)

• password-reset/ (POST)
– email

• password-reset-confirm/<uidb64>/<token>/ (GET)
    Note: Validates if uidb64 and token are valid
Return success, message, uidb64, token

• password-reset-complete/ (PATCH)
– password
- password_confirm
– uidb64
– token

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
    Note: Takes a refresh type JSON web token and returns an access type JSON web token if the refresh
    token is valid. HTTP 401 Unauthorized with {"detail": "Token is invalid or
    expired", "code": "token_not_valid"} in case of a invalid or expired token.
    

+++++++++++++++++++++++++++++++++ LECTURE ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

Note: The endpoints are for the admin

• lecture/admin/ (GET)
Returns all lectures

• lecture/admin/ (POST)
– title
– note| PDF file
– level
– subject
– term
– week

• lecture/admin/{id} (GET, DELETE)
Returns a single instance of a lecture

• lecture/admin/{id} (PUT, PATCH)
– title
– note
– level
– subject
– term
– week

• lecture/list/ (GET) # get all lectures

Note: The endpoints are for students

• lecture/detail/ (POST)
– Header {Authorization: Token <user token key>}
– level | JSS1, JSS2, JSS3, SSS1, SSS2, SSS3 
– subject
– term
Returns level, subject, term, week, title, term

++++++++++++++++++++++++++++++++++ Courses ++++++++++++++++++++++++++++++++++++
• lecture/course/admin
– title
– link
– poster

• lecture/course/list (GET)
– title
– link
– poster

• lecture/course/get/{id}/ (GET)
– title
– link
– poster

+++++++++++++++++++++++++++++++++ NEWS ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

++++++ADMIN)+++++++

• news/admin/ (GET)
– Header {Authorization: <Token userToken>}
Returns all news

• news/admin/ (POST)
– Header {Authorization: <Token userToken>}
– title
– source
– link

• news/admin/{id} (GET, DELETE)
– Header {Authorization: <Token adminToken>}
Returns a single instance of a news

• news/admin/{id} (PUT, PATCH)
– Header {Authorization: <Token adminToken>}
– title
– source
– link

++++++USER)+++++++

• news/user/ (GET)
– Header {Authorization: <Token userToken>}
returns all news

• news/user/{id} (GET)
– Header {Authorization: <Token userToken>}
returns single news

+++++++++++++++++++++++++++++++++ NOTES ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
+++++++ADMIN)+++++

• note/ (GET)
Returns all note

• note/ (POST)
– title
– content
– owner => userId

• note/{id} (GET, DELETE)
Returns a single instance of a note

• note/{id} (PUT, PATCH)
– title
– content

• note/{id} (PUT, PATCH)
– title
– content

++++++(USER)++++++

• note/user/{userId}/ (GET)
– Header {Authorization: <Token userToken>}
Returns all student note

• note/user/{userId} (POST)
– Header {Authorization: <Token userToken>}
– title
– content

• note/user/{noteId}/{userId} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a user note

• note/user/{noteId}/{userId} (PATCH)
– Header {Authorization: <Token userToken>}
– title
– content

• note/user/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– title
– content

+++++++++++++++++++++++++++++++++ VIDEOS ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• video/list (GET)
– Header {Authorization: <Token userToken>}
Returns all videos

• video/admin/ (GET)
– Header {Authorization: <Token userToken>}
Returns all videos

• video/admin/ (POST)
– Header {Authorization: <Token userToken>}
– title
– link
– level : level id
– term : 0 -> (1st term), 1 -> (2nd term), 2 -> (3rd term)

• video/admin/{id} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a videos

• video/admin/id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– title
– link
– level : level id
– term : 0 -> (1st term), 1 -> (2nd term), 2 -> (3rd term)

+++++++++++++++++++++++++++++++++ Email Verification ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

• email/verification/ (POST)
– email

• email/verification/confirm (POST)
– email

+++++++++++++++++++++++++++++++++ Facebook Login ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

• auth/facebook/ (POST)
– email


+++++++++++++++++++++++++++++++++ MOCK TEST ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
------------ MOCK TEST
• mock/mocktest/ (GET)
– Header {Authorization: <Token userToken>}
Returns all videos

• mock/mocktest/ (POST)
– Header {Authorization: <Token userToken>}
– subject
– term 
– level

• mock/mocktest/{id} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a videos

• mock/mocktest/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– subject
– term 
– level

• mock/mocktest/verbose/{id} (GET, DELETE)
Returns all MockTestQuestions which belongs to the selected MockTest

------------ MOCK TEST QUESTION
• mock/mocktest_question/ (GET)
– Header {Authorization: <Token userToken>}
Returns all mock test

• mock/mocktest_question/ (POST)
– Header {Authorization: <Token userToken>}
– mock_test => mock_test_id
– correct_answer | 0: a, 1: b, 2: c, 3: d
– a
– b
– c
– d

• mock/mocktest_question/{id} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a videos

• mock/mocktest_question/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– subject
– term 
– level


+++++++++++++++++++++++++++++++++ SUBSCRIPTION ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

------------------- ADMIN -------------------

• subscription/admin (GET)
– Header {Authorization: <Token userToken>}
Returns all videos

<!-- • subscription/admin (POST)
– Header {Authorization: <Token userToken>}
– user: id
– user_type
– payment_type 
– flw_ref
– tx_ref -->

• subscription/admin/{id} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a subscriptions

• subscription/admin/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– user: id
– user_type
– payment_type 
– flw_ref
– tx_ref

------------------- APP ENDPOINT -------------------

• subscription/reg/create/ (POST)
– user: id
– user_type
– payment_type 
– flw_ref
– tx_ref


+++++++++++++++++++++++++++++++++ Volunteer ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• volunteer/admin/ (GET)
– Header {Authorization: <Token adminToken>}
Returns all Volunteers

• volunteer/admin/ (POST)
– Header {Authorization: <Token adminToken>}
– first_name
– last_name
– email
– phone_number
– gender
– title
– state
– country
– age
– degree
– other_degree
– work_mode
– skillsets
– learn_about_us

• volunteer/admin/{id} (GET, DELETE)
– Header {Authorization: <Token adminToken>}
Returns a single instance of a Volunteer

• volunteer/admin/{id} (PUT, PATCH)
– Header {Authorization: <Token adminToken>}
– subject
– term 
– level


+++++++++++++++++++++++++++++++++ CLASSROOM SUBJECT ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

Note: The following endpoints are for the admin

• classroom/admin/subjects/ (GET)
– Header {Authorization: <Token adminToken>}
Returns all subject

• classroom/admin/ (POST)
– Header {Authorization: <Token adminToken>}
– title
– classes : array of classes id, Eg. [1, 2, 3]

• classroom/admin/subjects/{id} (GET, DELETE)
– Header {Authorization: <Token adminToken>}
Returns a single instance of a subject

• classroom/admin/subjects/{id} (PUT, PATCH)
– Header {Authorization: <Token adminToken>}
– title
– classes : array of classes id, Eg. [1, 2, 3]

Note: The following endpoints are for the users

• classroom/user/subjects/ (GET)
– Header {Authorization: <Token userToken>}
Returns all subject

+++++++++++++++++++++++++++++++++ CLASSROOM CLASS ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

Note: The following endpoints are for the admin

• classroom/admin/subjects/ (GET)
Returns all lectures

• lecture/admin/ (POST)
– title
– note| PDF file
– level
– subject
– term
– week

• classroom/admin/subjects/{id} (GET, DELETE)
Returns a single instance of a lecture

• classroom/admin/subjects/{id} (PUT, PATCH)
– title
– note
– level
– subject
– term
– week


+++++++++++++++++++++++++++++++++ COUPON ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• api/school/{coupon}/{subscription}/ (POST)
• api/school/admin/   (POST)
• api/school/check/coupon/{coupon}/ (GET)  <!-- check if coupon code has expired -->


+++++++++++++++++++++++++++++++++ NOTIFICATION ENDPOINTS +++++++++++++++++++++++++++++++++++++++++



+++++++++++++++++++++++++++++++++ FACEBOOK ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• social-auth/login/facebook (GET)


+++++++++++++++++++++++++++++++++++++ GETTING TEACHERS AND USER DETAILS [ADMIN] +++++++++++++++
– Header {Authorization: <Token adminToken>}
• student/get/<int:id>/ # get single user
• students/get/all/ # returns all students
• teacher/get/<int:id>/ # get single teacher
• teachers/get/all/  # returns all teachers


+++++++++++++++++++++++++++++++++++++ GETTING TEACHERS AND USER DETAILS [ADMIN] +++++++++++++++
– Header {Authorization: <Token adminToken>}
• student/get/<int:id>/ # get single user
• students/get/all/ # returns all students
• teacher/get/<int:id>/ # get single teacher
• teachers/get/all/  # returns all teachers
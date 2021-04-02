BASE URL => https://learnersconer.pythonanywhere.com/api/

+++++++++++++++++++++++++++++++++++++++ AUTH ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• user/phone/confirm/ (POST)
– phone
Returns
-- {"status": 'error', "message": "phone number already exists"}
-- {"status": "success", "message": "phone number not found"}

• /dj-rest-auth/login/ (POST)
– username
– email
– password
Returns Token key

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

• /user/email/verification (POST)
– fullname
– email


• /dj-rest-auth/logout/ (GET)

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

Note: The endpoints are for students

• lecture/detail/ (POST)
– Header {Authorization: Token <user token key>}
– level | JSS1, JSS2, JSS3, SSS1, SSS2, SSS3
– subject
– term
Returns level, subject, term, week, title, term

+++++++++++++++++++++++++++++++++ NEWS ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• news/admin/ (GET)
– Header {Authorization: <Token userToken>}
Returns all news

• news/admin/ (POST)
– Header {Authorization: <Token userToken>}
– title
– source
– link

• news/admin/{id} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a news

• news/admin/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– title
– source
– link

+++++++++++++++++++++++++++++++++ NOTES ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
------(ADMIN)
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

------(USER)
• note/user/{userId}/ (GET)
– Header {Authorization: <Token userToken>}
Returns all student note

• note/user/ (POST)
– Header {Authorization: <Token userToken>}
– title
– content
– owner | userId

• note/{id}/{user} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a user note

• note/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– title
– content

• note/user/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– title
– content

+++++++++++++++++++++++++++++++++ VIDEOS ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• videos/ (GET)
– Header {Authorization: <Token userToken>}
Returns all videos

• videos/ (POST)
– Header {Authorization: <Token userToken>}
– title
– link

• videos/{id} (GET, DELETE)
– Header {Authorization: <Token userToken>}
Returns a single instance of a videos

• videos/admin/{id} (PUT, PATCH)
– Header {Authorization: <Token userToken>}
– title
– link

+++++++++++++++++++++++++++++++++ Email Verification ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

• email/verification/ (POST)
– email

• email/verification/confirm (POST)
– email

+++++++++++++++++++++++++++++++++ Facebook Login ENDPOINTS +++++++++++++++++++++++++++++++++++++++++

• auth/facebook/ (GET)
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

------------ MOCK TEST QUESTION
• mock/mocktest_question/ (GET)
– Header {Authorization: <Token userToken>}
Returns all videos

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
<!-- – user: id -->
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


+++++++++++++++++++++++++++++++++ MOCK TEST ENDPOINTS +++++++++++++++++++++++++++++++++++++++++
• mock/mocktest/ (GET)
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

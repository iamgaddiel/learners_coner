+++++++ API ENDPOINTS 

+++++++ AUTH ENDPOINTS 

BASE URL => https://learnersconer.pythonanywhere.com/api

• /dj-rest-auth/login/ (POST)
    – username
    – email
    – password
    Returns Token key

• /user/login/ (POST)
    – username
    – email
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

• /dj-rest-auth/logout/ (POST) (GET)

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

+++++++ LECTURE ENDPOINTS 
BASE URL => api/lecture/
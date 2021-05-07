from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    function that gets called when a user calls the /auth endpoin
    :@Parm username: User's username in string format
    :@parm password:User's un-encrypted password in string format
    :return: A usermodel object if the authentication was succesfull,None,otherwise

    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """
    Function that gets called when user has already authenticated adn Flask-JWT
    verified that their authorisation header is correct
    :Param payload: A dictionary with 'identity' key,which is the user id
    :return: A UserModel object
    """
    user_id = payload('identity')
    return UserModel.find_by_id(user_id)

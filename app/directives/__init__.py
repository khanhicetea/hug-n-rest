import hug
from .auth import token_generate, token_verify


token_required = hug.authentication.token(token_verify)
"""
This is used as an attribute mapper
callable for django-cas per the README at 
https://github.com/mitocw/django-cas.
""" 

VERSION = "0.0.1"

CAS_URI = 'http://www.yale.edu/tp/cas'
NSMAP = {'cas': CAS_URI}
CAS = '{%s}' % CAS_URI

def populate_user(user, authentication_response):
    if authentication_response.find(CAS + 'authenticationSuccess/'  + CAS + 'attributes'  , namespaces=NSMAP) is not None:
        attr = authentication_response.find(CAS + 'authenticationSuccess/'  + CAS + 'attributes'  , namespaces=NSMAP)

        if attr.find(CAS + 'is_staff', NSMAP) is not None:
            user.is_staff = attr.find(CAS + 'is_staff', NSMAP).text.upper() == 'TRUE'

        if attr.find(CAS + 'is_superuser', NSMAP) is not None:
            user.is_superuser = attr.find(CAS + 'is_superuser', NSMAP).text.upper() == 'TRUE'

        if attr.find(CAS + 'givenName', NSMAP) is not None:
            user.first_name = attr.find(CAS + 'givenName', NSMAP).text

        if attr.find(CAS + 'sn', NSMAP) is not None:
            user.last_name = attr.find(CAS + 'sn', NSMAP).text

        if attr.find(CAS + 'email', NSMAP) is not None:
            user.email = attr.find(CAS + 'email', NSMAP).text
    pass

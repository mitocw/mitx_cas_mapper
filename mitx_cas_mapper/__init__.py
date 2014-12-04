"""
This is used as an attribute mapper
callable for django-cas per the README at
https://github.com/mitocw/django-cas.
"""

from django.conf import settings

VERSION = "0.1.0"

CAS_URI = 'http://www.yale.edu/tp/cas'
NSMAP = {'cas': CAS_URI}
CAS = '{%s}' % CAS_URI


def populate_user(user, authentication_response):
    """
    This is passed a django user object to be modified
    and the `authentication_response` from the CAS server.

    It allows you to convert attributes from CAS into local
    Django user attributes
    """
    if settings.CAS_VERSION == '2':
        if authentication_response.find(
                CAS + 'authenticationSuccess/' + CAS + 'attributes',
                namespaces=NSMAP
        ) is not None:
            attr = authentication_response.find(
                CAS + 'authenticationSuccess/' + CAS + 'attributes',
                namespaces=NSMAP
            )

            if attr.find(CAS + 'is_staff', NSMAP) is not None:
                user.is_staff = attr.find(
                    CAS + 'is_staff',
                    NSMAP
                ).text.upper() == 'TRUE'

            if attr.find(CAS + 'is_superuser', NSMAP) is not None:
                user.is_superuser = attr.find(
                    CAS + 'is_superuser',
                    NSMAP
                    ).text.upper() == 'TRUE'

            if attr.find(CAS + 'givenName', NSMAP) is not None:
                user.first_name = attr.find(CAS + 'givenName', NSMAP).text

            if attr.find(CAS + 'sn', NSMAP) is not None:
                user.last_name = attr.find(CAS + 'sn', NSMAP).text

            if attr.find(CAS + 'email', NSMAP) is not None:
                user.email = attr.find(CAS + 'email', NSMAP).text

    if settings.CAS_VERSION == '3':
        if authentication_response is not None:
            if 'is_superuser' in authentication_response:
                user.is_superuser = authentication_response['is_superuser']

            if 'is_staff' in authentication_response:
                user.is_staff = authentication_response['is_staff']

            if 'givenName' in authentication_response:
                user.first_name = authentication_response['givenName']

            if 'sn' in authentication_response:
                user.last_name = authentication_response['sn']

            if 'email' in authentication_response:
                user.email = authentication_response['email']

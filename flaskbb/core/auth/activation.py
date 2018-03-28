# -*- coding: utf-8 -*-
"""
    flaskbb.core.auth.activation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Interfaces for handling account activation
    in FlaskBB

    :copyright: (c) 2014-2018 the FlaskBB Team
    :license: BSD, see LICENSE for more details
"""

from abc import abstractmethod

from ..._compat import ABC


class AccountActivator(ABC):
    """
    Interface for managing account activation in installations that require
    a user to activate their account before using it.
    """

    @abstractmethod
    def initiate_account_activation(self, user):
        """
        Used to extend an offer of activation to the user. This may take any
        form, but is recommended to take the form of a permanent communication
        such as email.

        This method may use :class:`flaskbb.core.exceptions.ValidationError`
        to communicate a failure when creating the token for the user to
        activate their account with (such as when a user has requested a token
        be sent to an email that is not registered in the installation or
        the account associated with that email has already been activated).
        """
        pass

    @abstractmethod
    def activate_account(self, token):
        """
        Used to handle the actual activation of an account. The token
        passed in is the serialized token communicated to the user to use
        for activation. This method may raise
        :class:`flaskbb.core.tokens.TokenError` and
        :class:`flaskbb.core.exceptions.ValidationError` to communicate
        failures when parsing or consuming the token.
        """
        pass

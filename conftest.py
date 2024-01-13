import pytest
from pytest_factoryboy import register

from core_apps.users.tests.factories import UserFactory

# from core_apps.accounts.tests.factories import (AccountFactory,
#                                                 TermFactory,
#                                                 PermissionFactory,
#                                                 AccountPermissionFactory,
#                                                 )

register(UserFactory)
# register(TermFactory)
# register(PermissionFactory)
# register(AccountPermissionFactory)
# register(AccountFactory)


@pytest.fixture
def base_user(db, user_factory):
    return user_factory.create()


@pytest.fixture
def super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True, is_superuser=True)
    return new_user


# @pytest.fixture
# def baseTerm(db, term_factory):
#     term = term_factory.create()
#     return term

# @pytest.fixture
# def basePermission(db, permission_factory):
#     permission = permission_factory.create()
#     return permission

# @pytest.fixture
# def baseAccountPermission(db, account_permission_factory):
#     account_permission = account_permission_factory.create()
#     return account_permission

# @pytest.fixture
# def test_user(db, user_factory):
#     user = user_factory.create()
#     yield user

# @pytest.fixture
# def baeAccount(db, account_factory):
#     account = account_factory.create(test_user)
#     return account

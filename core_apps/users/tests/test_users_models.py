from email.mime import base

import pytest


def test_user_str(base_user):
    assert base_user.str() == f"{base_user.username}"


def test_user_short_name(base_user):
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    full_name = f"{base_user.first_name}-{base_user.last_name}"
    assert base_user.get_full_name() == full_name


def test_base_user_email_is_normalized(base_user):
    email = base_user.email
    assert email.lower() == email


def test_super_user_email_is_normalized(super_user):
    email = super_user.email
    assert email.lower() == email


def test_super_user_is_not_staff(user_factory=None):
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "superuser must have is_staff=True"


def test_create_user_with_no_email(user_factory=None):
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: AN email address is required"


def test_create_user_with_no_username(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "User must submit a username"


def test_create_user_with_no_firstname(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "User must submit a first name"


def test_create_user_with_no_lastname(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "User must submit a last name"


def test_create_superuser_with_no_email(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"



def test_create_superuser_with_no_password(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Superuser must have a password"


def test_user_email_incorrect(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email="authorshaven.com")
    assert str(err.value) == "You must provide a vaid email address"

import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from faker import Factory as FakerFactory

faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    """_summary_

    Args:
        factory (_type_): _description_
    """

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.first_name().lower())
    email = factory.LazyAttribute(lambda o: "%s@example.com" % o.username)
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False

    class Meta:
        model = get_user_model()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if kwargs.get("is_superuser"):
            return manager.create_superuser(*args, **kwargs)
        return manager.create_user(*args, **kwargs)

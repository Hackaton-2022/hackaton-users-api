from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """
    Custom user model manager.
    """

    def _create_user(self, username, email, name, last_name, age, height, weight, genre, password, is_staff, is_superuser, **extra_fields):
        """
        Create and save a User with the given data.
        """
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            age=age,
            height=height,
            weight=weight,
            genre=genre,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, age, height, weight, genre, password=None, **extra_fields):
        """
        Call _create_user function setting the respective parameters for a user.
        """
        return self._create_user(username, email, name, last_name, age, height, weight, genre, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, age, height, weight, genre, password=None, **extra_fields):
        """
        Call _create_user function setting the respective parameters for a superuser.
        """
        return self._create_user(username, email, name, last_name, age, height, weight, genre, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nombre de usuario',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        'Correo Electrónico',
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        'Nombres',
        max_length=255,
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=255,
    )
    age = models.IntegerField(
        'Edad'
    )
    height = models.IntegerField(
        'Estatura'
    )
    weight = models.IntegerField(
        'Peso'
    )
    genre = models.CharField(
        'Genero',
        max_length=1,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'name',
        'last_name',
        'age',
        'height',
        'weight',
        'genre'
    ]

    def __str__(self):
        return f'{self.id} {self.name} {self.last_name}'

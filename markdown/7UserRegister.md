# カスタムユーザーモデル

`mysite/models.py`

```python


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Userを定義した後にUserManagerを呼び出す


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 管理者を作成
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # emailでログインする
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    # アカウントが有効かを判断する
    is_active = models.BooleanField(default=True)
    # 管理画面に入れるかを判断する
    # 一般ユーザーは管理画面には入れないのでdefaultはFalse
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # USERNAMEの項目をemailに設定
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

```

`config/settings.py`

```python
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 定義したユーザーモデルを使用
AUTH_USER_MODEL = 'mysite.User
```

# 管理画面の編集

`mysite/admin.py`

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from mysite.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )
    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    # --- adminでuser作成用に追加 ---
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    # --- adminでuser作成用に追加 ---

# Groupモデルを登録しない
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
```

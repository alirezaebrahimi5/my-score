from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django_jalali.db import models as jmodels


class AllUser(BaseUserManager):
    def create_user(self, mobile, email, password=None, first_name=None, last_name=None, **kwargs):
        if not email:
            raise ValueError('کاربر باید پست الکترونیکی داشته باشد')
        
        if not mobile:
            raise ValueError('کاربر باید شماره تلفن داشته باشد')
        
        if not first_name:
            raise ValueError('کاربر باید شماره نام داشته باشد')
        
        if not last_name:
            raise ValueError('کاربر باید شماره نام خانوادگی داشته باشد')

        user = self.model(
            email=self.normalize_email(email),
            mobile=mobile,
            first_name=first_name,
            last_name=last_name,
            **kwargs,
        )
        user.is_active = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, mobile, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            mobile=mobile,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = False
        user.is_superuser = False        
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, email, password, first_name, last_name):
        user = self.create_user(
            email=email,
            mobile=mobile,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_active  = True
        user.is_superuser = True        
        user.save(using=self._db)
        return user


class Role:
    Management = 1
    Sales_Manager = 2
    Supporter = 3
    Consultant = 4
    Accounting = 5
    MEDREP_Visitor = 6
    Visitor = 7
    
    ROLES = (
        (Management, 'مدیر'),
        (Sales_Manager, 'سرپرست فروش'),
        (Supporter, 'پشتیبانی'),
        (Consultant, 'مشاور'),
        (Accounting, 'حسابدار'),
        (MEDREP_Visitor, 'پخش کننده نماینده پزشکی'),
        (Visitor, 'پخش کننده'),
    )


class User(AbstractBaseUser):
    alphanumeric       = RegexValidator(r'^[0-9a-zA-Z]*$', message='فقط نمادهای الفبایی و اعداد پذیرفته میشوند')
    numbers            = RegexValidator(r'^[0-9a]*$', message='تنها اعداد پذیرفته میشوند')
    identificationCode = models.CharField(max_length=11, unique=True, validators=[numbers], primary_key=True)
    mobile             = models.CharField(max_length=11, unique=True, validators=[numbers])
    first_name         = models.CharField(max_length=30, null=True, blank=True, verbose_name='نام')
    last_name          = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    phone              = models.CharField(max_length=11, unique=True, validators=[numbers], verbose_name='شماره تماس')
    address            = models.CharField(max_length=4096, null=True, blank=True, verbose_name = '')
    is_active          = models.BooleanField(default=False, null=False, verbose_name='وضعیت فعالیت')
    is_staff           = models.BooleanField(default=False, null=False, verbose_name='دسترسی ادمین')
    is_superuser       = models.BooleanField(default=False, null=False, verbose_name='مدیر')
    role               = models.PositiveSmallIntegerField(choices=Role.ROLES, default=7)
    joined_at          = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    objects = AllUser()

    USERNAME_FIELD  = 'identificationCode'
    REQUIRED_FIELDS = ['mobile', 'phone', 'first_name', 'last_name']
    
    def __str__(self) -> str:
        return f"{self.identificationCode} {self.first_name} {self.last_name} {self.mobile} {self.role}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Profile(models.Model):
    user       = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    mobile     = models.CharField(max_length=11)
    phone      = models.CharField(max_length=11, verbose_name='شماره تماس')
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='نام')
    last_name  = models.CharField(max_length=50, null=True, blank=True, verbose_name='نام خانوادگی')
    role       = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        return f"{self.user} {self.phone} {self.mobile} {self.role}"

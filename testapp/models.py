from django.db import models
from django.utils import timezone
# Create your models here.

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class TestFields(models.Model):
    content = RichTextUploadingField()									# Особенное поле для использования CKE редактора
#    auto_field = models.AutoField()									# АвтоПоле - для всякого рода ID-индетентификаторов, по сути не нужно, так как есть основной ключ таблицы, который генерируется автоматически
    big_integer_field = models.BigIntegerField()						# большое целое 64 битное число от -9223372036854775808 до 9223372036854775807
    binary_field = models.BinaryField()									# бинарное поле (для всяких бинарных данных, типа "ключи шифрования", "куски картинок", "аудио" и прочее извращение
    boolen_field = models.BooleanField()								# Булевое Поле, два значения, Истина и Лож... классика
    char_field = models.CharField(max_length=255,)						# символьное поле. Для хранения строки. Хорошо подойдёт для всяких там заголовок. 
#   comma_separated_integet_field = models.CommaSeparatedIntegerField()	# поле удалено в версии >2.0
    date_field = models.DateField()										# поле для даты
    date_time_field = models.DateTimeField(								# дата и время
        blank=True, 
        null=True)								
    decimal_field = models.DecimalField(								# десятичное число с точкой
        max_digits=10, 
        decimal_places=2)			
    duration_field = models.DurationField()								# поле для хранения временного интервала timedelta
    email_field = models.EmailField(max_length=254,)					# емейл
    file_field = models.FileField(										# поле для загрузки файла
        upload_to='uploads/%Y/%m/%d/', 
        max_length=100)	
#    file_path_field = models.FilePathField(								# ???
#        path=None, 
#        match=None, 
#        recursive=False, 
#        max_length=100,)	
    float_field = models.FloatField()									# число с плавающей точкой
    image_field = models.ImageField(									# тоже как FileField, но с проверкой файла на "изображение"
        upload_to='uploads/%Y/%m/%d/', 
        height_field=None, 
        width_field=None, 
        max_length=100,)									
    integer_field = models.IntegerField()								# целое число  от -2147483648 до 2147483647
    generic_IP_adress_field = models.GenericIPAddressField(				# поле для хранения IP адресса (4 и 6 протоколы)
        protocol='both', 
        unpack_ipv4=False,)			
    null_boolean_field = models.NullBooleanField()						# также как и поле Булен, только может ещё иметь NULL значение
    positive_integer_field = models.PositiveIntegerField()				# число от 0 до 2147483647
    positive_small_integet_field = models.PositiveSmallIntegerField()	# число от 0 до 32767
    slug_field = models.SlugField(max_length=50,)						# короткая строка/символ, вроде можно использовать как теги
    small_integer_field = models.SmallIntegerField()					# число от -32768 до 3276
    text_field = models.TextField()										# Большое текстовое поле. Форма использует виджет Textarea
    time_field = models.TimeField(										# время
        auto_now=False, 
        auto_now_add=False,)										
    url_field = models.URLField(max_length=200,)						# Поле CharField для URL
    uuid_field = models.UUIDField()										# Поля для сохранения UUID является хорошей альтернативой AutoField с primary_key. База данных не сгенерирует UUID за вас 
#    foreign_key = models.ForeignKey(									# Связь многое-к-одному. Принимает позиционный аргумент: класс связанной модели.
#        'news.News',
#        on_delete=models.CASCADE,)
#    many_to_many_field = models.ManyToManyField("self")					# Связь многие-ко-многим. Принимает позиционный аргумент: класс связанной модели. Работает так же как и ForeignKey, включая рекурсивную и ленивую связь.
			
			
			
			
			
			
			

    def publish(self):
        self.date_time_field = timezone.now()
        self.save()

    def __str__(self):
        return self.char_field

from django.db import models

# Create your models here.


class Ways(models.Model):
    name = models.CharField("Nomi", max_length=150)
    icon = models.CharField("Icon fontaosem", max_length=50)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField("Ismi", max_length=150)
    surname = models.CharField("Familiya", max_length=150)
    tel_num = models.PositiveIntegerField("telfon raqami")
    unique_field = models.CharField("Bir martalik parol",max_length=30,blank=True,editable=False)
    ways = models.ForeignKey("main.Ways", related_name="way_users", on_delete=models.CASCADE,null=True)
    TIME = [
        ('ERTALABKI','ertalabki'),
        ('KECHKI','kechki'),
    ]
    times = models.CharField(choices=TIME, max_length=150, blank=True)
    # true_a = models.ManyToManyField("main.Quizzes", related_name="user_true")
    # false_a = models.ManyToManyField("main.Quizzes", related_name="user_false")
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)    
        if not self.unique_field:
            self.unique_field = f"{self.name[0]}{self.surname[0]}00{self.pk}"
            super().save(*args, **kwargs)    



    



class Quiz(models.Model):
    title = models.CharField("Savol", max_length=2150)
    ways = models.ForeignKey("main.Ways", related_name="way_quizz", on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

class Answer(models.Model):
    title = models.CharField("Javob", max_length=550, blank=True)
    image = models.ImageField("rasmi", upload_to="answers_img/", blank=True)
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, related_name="answers")
    true_answer = models.BooleanField("togrimi")

    def __str__(self):
        return self.title
    

class LogicQuiz(models.Model):
    title = models.TextField("Mantiqiy Savol")
    answer = models.TextField("Javob (to'ldirish shartmas)",blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # number = models.PositiveBigIntegerField(default=0,unique=True, blank=True)

    def __str__(self):
        return self.title[:25]


class Results(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name="results")
    quiz = models.ForeignKey(Quiz,on_delete=models.PROTECT,related_name="results",null=True)
    user_answer = models.ForeignKey(Answer,on_delete=models.PROTECT,null=True)
    logic_quiz = models.ForeignKey(LogicQuiz,on_delete=models.PROTECT,null=True)
    logic_answer = models.CharField(max_length=500,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.name

    

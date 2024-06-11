from peewee import *
from app.data import database_path
database = SqliteDatabase(database_path)

class Patient(Model):
    pidnum = AutoField()
    cid = BooleanField()
    time = IntegerField()
    trt = IntegerField()
    age = IntegerField()
    wtkg = FloatField()
    hemo = BooleanField()
    homo = BooleanField()
    drugs = BooleanField()
    karnof = IntegerField()
    oprior = BooleanField()
    z30 = BooleanField()
    zprior = BooleanField()
    preanti = IntegerField()
    race = BooleanField()
    gender = BooleanField()
    str2 = BooleanField()
    strat = IntegerField()
    symptom = BooleanField()
    treat = BooleanField()
    offtrt = BooleanField()
    cd40 = IntegerField()
    cd420 = IntegerField()
    cd80 = IntegerField()
    cd820 = IntegerField()
    used_for_training = BooleanField(default=False)

    class Meta:
        database = database

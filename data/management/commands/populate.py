#populate database
# This code has to be placed in a file within the
# data/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# so let's call it populate.py. Another thing that has to be done
# is creating __init__.py files in both the management and commands
# directories, because these have to be Python packages.
#
# execute python manage.py  populate


from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
import random

from random import randint

django.setup()

from data.models import Category, Workflow
#models
CATEGORY = 'category'
WORKFLOW = 'workflow'
# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'

    def getParragraph(self, init, end):
        # getParragraph returns a parragraph, useful for testing
        if end > 445:
            end = 445
        if init < 0:
            init = 0
        return """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."""[init:end]

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):
        self.cleanDatabase()
        self.addCategory(5) # add 5 categories
        self.addWorkflow(13) # add 13 workflows

    def cleanDatabase(self):
        # delete all
        # workflows and  categories
        Workflow.objects.all().delete()
        Category.objects.all().delete()
        pass

    def addCategory(self, noCategories):
        # create 5 categories <<<<<<<<<<<<<<<<<<<<<<<
        # baseName, call objects
        # print Category.objects.all()
        for i in range(noCategories):
            n = 'Category' + str(i+1)
            t = n + ' description'
            c = Category.objects.get_or_create(name=n)[0]
            c.tooltip = t
            c.save()


    def addWorkflow(self, noWorkflows):
        # create 13 workflows  <<<<<<<<<<<<<<<<<<<<<<
        # assign them to random categories
        # do not assign the sameworkflow to two o mote
        # categories
        # add apropriate code
        # create fake json
        elems = self.getJson()

        for p in elems:
            r_n = randint(1, 5)
            n = "Category" + str(r_n)
            w = Workflow.objects.get_or_create(name=p["name"], client_ip=p["client_ip"])[0]
            w.description = p["description"]
            w.versionInit = p["versionInit"]
            w.keywords = p["keywords"]
            w.json = p["json"]
            w.category = Category.objects.filter(name=n)
            w.save()

    def getJson(self):
        return [
            {
                "name": "Workflow1",
                "description": "Workflow1 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow2",
                "description": "Workflow2 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow3",
                "description": "Workflow3 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow4",
                "description": "Workflow4 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow5",
                "description": "Workflow5 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow6",
                "description": "Workflow6 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow7",
                "description": "Workflow7 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow8",
                "description": "Workflow8 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow9",
                "description": "Workflow9 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow10",
                "description": "Workflow10 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow11",
                "description": "Workflow11 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow12",
                "description": "Workflow12 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "Workflow13",
                "description": "Workflow13 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            } ]

#There's no need to bypass manage.py, since it's a wonderful convenience wrapper around
        # the Django project administration tools. It can be used to create custom
        # management commands - e.g. your own commands parallel to shell, dumpdata,
        # and so on. Not only that creating such commands gives you a very succinct,
        # boilterplate-free way of writing custom management scripts, it also gives
        # you a natural location to house them, per application.

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

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from random import randint, uniform,random

import django
import random

django.setup()

from data.models import Category, Workflow
#models
CATEGORY = 'category'
USER = 'user'
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
		self.createCategory("category 1")
		self.createCategory("category 2")
		self.createWorkflow("workflow 11","category 1")
		self.createWorkflow("workflow 12","category 1")
		self.createWorkflow("workflow 13","category 1")
		self.createWorkflow("workflow 21","category 2")
		self.createWorkflow("workflow 22","category 2")
		self.createWorkflow("workflow 23","category 2")

	def cleanDatabase(self):
		# delete all
		# workflows and  categories
		# ADD CODE HERE
		Workflow.objects.all().delete()
		Category.objects.all().delete()
		pass

	def createCategory(name):
		t = name + ' description'
		c = Category.objects.get_or_create(name=name)[0]
		c.tooltip = t
		c.save()
		print Category.objects.all()



	def createWorkflow(self,name,category):

		elems = self.getJson()

        for p in elems:
			#sacar el diccioario del workflow
"""try:
			work=Workflow.object.get(name=name)

		except Workflow.DoesNotExist:
			work=Workflow()
			work.name=name
			work.created=datetime.datetime.now(tz=timezone.utc)
			work.views=0
			work.downloads=0
			work.versionInit="versionInit"
			work.client_ip= "%d.%d.%d.%d" %(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
			work.keywords="keywords"
			work.json=self.getJson()
			work.save()
			cat=Category.objects.get(name=category)
			work.category.add(cat)
			work.save()"""


	def obtenerWorkflowAsociado(self,category):



		cat=Category.objects.get(name=category)
		workflow=Workflow.objects.filter(category=cat)
		print("workflows asociados a la category" + category)
		print workflow
		return workflow






	def obtenerCategoriaPerteneciente(self,slug):


		try:
			work=Workflow.objects.get(slug=slug)
			cat=workflow.category.get()
			slugcat=cat.slug
			print("La categoryde " +slug+ " es " + slugcat)

		except Category.DoesNotExist:
			print("Workflow " + slug + "inexistente")





    def getJson(self):
        return [
            {
                "name": "workflow 11",
                "description": "Workflow 11 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "workflow 12",
                "description": "Workflow 12 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "workflow 13",
                "description": "workflow 13 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "workflow 21",
                "description": "workflow 21 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "workflow 22",
                "description": "workflow 22 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            },
            {
                "name": "workflow 23",
                "description": "workflow 23 description",
                "versionInit": "1.0",
                "client_ip": "192.168.0.1",
                "keywords": "nothing",
                "json": "null"
            }]

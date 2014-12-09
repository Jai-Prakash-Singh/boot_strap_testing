from django.template import Library, Node 
from math import log, pow
from login_app.forms import *
register = Library()
import  datetime

class Registration_tag(Node):
    def render(self, context):
        context['registration_tag'] = RegistrationForm()
        return ''

def get_registraion_requirement(parser, token):
    return Registration_tag()

get_registraion_requirement_inst = register.tag(get_registraion_requirement)
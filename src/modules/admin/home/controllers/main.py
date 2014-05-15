  # -*- coding: utf-8 -*-  
# disco-toolbox.src.modules.home.controllers.main -- controller du main
import webapp2

from core.libs import affichage                                         # appel de la librairie d'affichage

MODULE_NAME = 'home'                                                    # nom du module


class main(webapp2.RequestHandler):
    def get(self, target):
        template_values = {
            'content': 'accueil pannel'
        }
        affichage.extend_to_base(target.response, template_values)
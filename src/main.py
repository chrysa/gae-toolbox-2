  # -*- coding: utf-8 -*-
# disco-toolbox.src.main -- fichier de décryptage des URLS
import webapp2
from webapp2_extras   import routes

from core             import config                                                                                         # import du fichier de config
from core.controllers import ErrorsController
from core.libs        import internationalize                                                                               # import du fichier de gestion de l'internationalisation
from core.libs        import admin_mod
from core.libs        import front_mod

conf = {}                                                                                                                   # initialisation de la configation de l'appli
conf = internationalize.set_config(conf)                      
app = webapp2.WSGIApplication([
    routes.DomainRoute(config.DOMAIN, 
                        [
                         webapp2.Route('/img/<module:/>/<img:/>',                               handler= front_mod.GetModuleImg),         # rootage des images
                         webapp2.Route('/img/<module:/[\w]+>/<img:/[\w]+>',                     handler= front_mod.GetModuleImg),         # rootage des images
                         webapp2.Route('/js/<module:/>/<js:/>',                                 handler= front_mod.GetModuleJS),          # rootage des JS
                         webapp2.Route('/js/<module:/[\w]+>/<js:/[\w]+>',                       handler= front_mod.GetModuleJS),          # rootage des JS
                         webapp2.Route('/css/<module:/>/<css:/>',                               handler= front_mod.GetModuleCSS),         # rootage des CSS
                         webapp2.Route('/css/<module:/[\w]+>/<css:/[\w]+>',                     handler= front_mod.GetModuleCSS),         # rootage des CSS
                         webapp2.Route('/admin/',                                               handler= admin_mod.load), 
                         webapp2.Route('/admin/<module:/>',                                     handler= front_mod.load),
                         webapp2.Route('/admin/<module:/[\w]+>',                                handler= front_mod.load),
                         webapp2.Route('/admin/<module:/>/<page:/>',                            handler= front_mod.load),
                         webapp2.Route('/admin/<module:/[w]+>/<page:/[\w]+>',                   handler= front_mod.load),
                         webapp2.Route('/admin/<module:/>/<page:/>/<action:/>',                 handler= front_mod.load),
                         webapp2.Route('/admin/<module:/[\w]+>/<page:/[\w]+>/<action:/[\w]+>',  handler= front_mod.load),
                         webapp2.Route('<module:/>',                                            handler= front_mod.load),                 # rootage des modules
                         webapp2.Route('<module:/[\w]+>',                                       handler= front_mod.load),                 # rootage des modules
                         webapp2.Route('<module:/>/<page:/>',                                   handler= front_mod.load),                 # rootage des pages dans le module
                         webapp2.Route('<module:/[w]+>/<page:/[\w]+>',                          handler= front_mod.load),                 # rootage des pages dans le module
                         webapp2.Route('<module:/>/<page:/>/<action:/>',                        handler= front_mod.load),                 # rootage des actions dans les pages
                         webapp2.Route('<module:/[\w]+>/<page:/[\w]+>/<action:/[\w]+>',         handler= front_mod.load)                  # rootage des actions dans les pages
                        ]
                      ),
],
    debug = config.DEBUG, config = conf)

app.error_handlers[403] = ErrorsController.handle_403                                                                       # capture de la 403 forbiden
app.error_handlers[404] = ErrorsController.handle_404                                                                       # capture de la 404 not found
app.error_handlers[500] = ErrorsController.handle_500                                                                       # capture de la 500 Internal Server Error
app.error_handlers[502] = ErrorsController.handle_502                                                                       # capture de la 502 Bad Gateway ou Proxy Error
app.error_handlers[504] = ErrorsController.handle_504                                                                       # capture de la 504 Gateway Time-out
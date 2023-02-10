# En este archivo se elige cual base de datos debe ser ingresada los datos

# Modulos
from .models import Restaurante

# Routers


class SiataRouter:
    '''
    Elige en cual base de datos realizar la operación.
    '''
    route_app_labels = {'siatasiata'}

    def db_for_read(self, model, **hints):
        '''
        '''
        if model._meta.app_label in self.route_app_labels:
            return 'sitasiata'
        return None
    
    def db_for_write(self, model, **hints):
        '''
        '''
        if model._meta.app_label in self.route_app_labels:
            return 'sitasiata'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        '''
        '''
        if app_label in self.route_app_labels:
            return db == 'sitasiata'
        return None
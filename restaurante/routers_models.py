'''
Enrutadores de bases de datos

El propósito es elegir cuál base de datos 
que acciones hacer y hacía que bd, en el caso de que
no se especifique, se elige la base de datos
que está por defecto
'''


# Modulos
from .models import Restaurante


class SiataRouter:
    '''
    Clase SiataRouter

    Descripción:
    Esta clase se encarga de proveer los métodos
    necesarios para realizar acciones específicas en 
    la base de datos
    '''
    route_app_labels = {'siatasiata'} # Bases de datos disponibles para enrutar

    def db_for_read(self, model, **hints):
        '''
        Lectura de la base de datos

        Descripción:
        Sugiere la base de datos que debe ser usada
        para realizar la operación de lectura de 
        objetos del tipo modelo

        Argumentos:
        -------------
        model: Recibe el modelo que se ha importado
        hints: Recibe las sugerencias del enrutador
        para decidir que base de datos debes recibir
        una solicitud determinada
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
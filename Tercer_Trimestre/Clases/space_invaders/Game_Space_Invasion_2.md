# TUTORIAL 2 DE INVASIÓN ALIELIGENA

## 1. AÑADIR VELOCIDAD A LA NAVE
```python
self.rect.x += 3
```

## 2.   PARA QUE LA NAVE NO SE VAYA DE LA PANTALLA
```python
def limits(self):
        # Limita el margen derecho
        if self.ship.rect.x > self.settings.screen_width:
            self.ship.rect.x = self.settings.screen_width

        # Limita el margen izquierdo
        if self.ship.rect.x < 0:
            self.ship.rect.x = 0
```

## 3. AÑADIR PANTALLA COMPLETA AL JUEGO
```python
self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
```

## 4. DISPARAR MISILES 


### 4.1 CREAR LOS ATRIBUTOS DE SETTINGS PARA LOS DISPAROS 

### 4.2 CREAR LA CLASE MISILES.PY

### 4.3 CONFIGURACIÓN DLE JUEGO PRINCIPAL PARA QUE FUNCIONE LOS DISPAROS

## 5. QUE LA NAVE DISPARE

## 5.1 BORRAR LOS DISPAROS ANTIGUOS

## 5.2 LIMITAR EL NÚMERO DE MISILES

## 6. REFACTORIZACIÓN DEL CÓDIGO PARA QUE QUEDE EL CÓDIGO MÁS BONITO



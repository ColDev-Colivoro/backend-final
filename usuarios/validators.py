from django.core.exceptions import ValidationError
import re

def validar_email_personalizado(email):
    """
    Valida que el email tenga un formato correcto.
    Se pueden agregar reglas de negocio adicionales aquí (ej: dominios permitidos).
    """
    # Regex estándar para validación de email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        raise ValidationError("El formato del correo electrónico no es válido.")
    
    # Ejemplo de regla adicional (descomentar si se requiere restringir dominios)
    # dominios_permitidos = ['inacap.cl', 'miempresa.com']
    # dominio = email.split('@')[1]
    # if dominio not in dominios_permitidos:
    #     raise ValidationError(f"Dominio no permitido. Debe ser uno de: {', '.join(dominios_permitidos)}")

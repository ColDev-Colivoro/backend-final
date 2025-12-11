import re
from django.core.exceptions import ValidationError

def validar_rut_chileno(rut):
    """
    Valida formato y dígito verificador de RUT chileno.
    Acepta formatos: 17288706-6, 17.288.706-6
    """
    # Limpiar formato
    rut_limpio = rut.replace(".", "").replace("-", "").upper()
    
    if len(rut_limpio) < 2:
        raise ValidationError("RUT inválido: demasiado corto")
    
    cuerpo = rut_limpio[:-1]
    dv = rut_limpio[-1]
    
    # Validar que el cuerpo sea numérico
    if not cuerpo.isdigit():
        raise ValidationError("RUT inválido: el cuerpo debe ser numérico")
    
    # Calcular dígito verificador
    suma = 0
    multiplo = 2
    
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2
    
    dv_esperado = 11 - (suma % 11)
    
    if dv_esperado == 11:
        dv_esperado = '0'
    elif dv_esperado == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(dv_esperado)
    
    if dv != dv_esperado:
        raise ValidationError(f"RUT inválido: dígito verificador incorrecto. Esperado: {dv_esperado}")

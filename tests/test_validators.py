from django.test import TestCase
from django.core.exceptions import ValidationError
from usuarios.validators import validar_email_personalizado
from activos.validators import validar_rut_chileno

class ValidatorTests(TestCase):
    
    # --- Tests de Email ---
    def test_email_valido(self):
        """Debe aceptar emails con formato correcto"""
        emails = ['test@example.com', 'usuario.nombre@dominio.cl', 'a@b.co']
        for email in emails:
            try:
                validar_email_personalizado(email)
            except ValidationError:
                self.fail(f"Email válido fue rechazado: {email}")

    def test_email_invalido(self):
        """Debe rechazar emails mal formados"""
        emails = ['testexample.com', 'test@', '@dominio.com', 'test@dominio']
        for email in emails:
            with self.assertRaises(ValidationError, msg=f"Email inválido fue aceptado: {email}"):
                validar_email_personalizado(email)

    # --- Tests de RUT ---
    def test_rut_valido(self):
        """Debe aceptar RUTs válidos con y sin puntos/guión"""
        ruts = ['17.288.706-6', '17288706-6', '172887066'] # Nota: el validador actual espera que se pasen limpio? No, el validador limpia.
        # Revisando implementación: rut.replace(".", "").replace("-", "") -> '172887066'. 
        # Si paso '172887066' -> limpia igual.
        for rut in ruts:
             try:
                validar_rut_chileno(rut)
             except ValidationError:
                self.fail(f"RUT válido fue rechazado: {rut}")

    def test_rut_invalido_dv(self):
        """Debe rechazar RUT con dígito verificador incorrecto"""
        rut = '17.288.706-5' # El correcto es 6
        with self.assertRaises(ValidationError):
            validar_rut_chileno(rut)

    def test_rut_invalido_largo(self):
        """Debe rechazar RUT demasiado corto"""
        with self.assertRaises(ValidationError):
            validar_rut_chileno("1")

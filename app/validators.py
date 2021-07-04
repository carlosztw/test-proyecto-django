from django.forms import ValidationError

class MaxSizeFileValidator:
    def __init__(self, max_file_size=3):
        self.max_file_size = max_file_size

    def __call__(self,value):
        size = value.size 
        # megabytes a bytes
        max_size = self.max_file_size * 1048576
        if size > max_size:
            raise ValidationError(f"El tamaño máximo del archivo debe ser de {self.max_file_size}MB")
        return value

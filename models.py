from django.db import models

class Spreadsheet(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cell(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, related_name="cells", on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    value = models.TextField(blank=True)
    formula = models.TextField(blank=True)
    
    def __str__(self):
        return f"Cell ({self.row}, {self.column})"

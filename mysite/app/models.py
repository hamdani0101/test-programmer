from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=155)

    class Meta:
        managed=False
        db_table="kategori"

    def __str__(self):
        return self.nama_kategori
    
class Status(models.Model):
    nama_status = models.CharField(max_length=155)

    class Meta:
        managed=False
        db_table="status"

    def __str__(self):
        return self.nama_status
    
class Produk(models.Model):
    nama_produk = models.CharField(max_length=155)
    harga = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        managed=False
        db_table="produk"

    def __str__(self):
        return self.nama_produk

from django.db import models

# Create your models here.
"""
id : identification number of the book
name
description
price
CREATE TABLE book (
    id INT PRIMARY KEY,
    name char 255 NOT NULL,
    description text,
)


INSERT INTO book VALUES (1, 'book1' , 'this is description');

CRUD operations:
C ==> Create ==> INSERT INTO book;
R ==> Read   ==> SELECT * FROM book where id=1;
U ==> Update ==> Update Values ('id' , 'name') (2, 'new book 1') where id=1
D ==> Delete ==> Delete from book where id=1 
"""

class Book(models.Model):
    # id = primarykey (django makes the primary key column by default)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2) # 156.39 # 9999.99
    photo = models.FileField(upload_to="images/", null=True, blank=True)
    deleteFlag = models.SmallIntegerField(default=0)
    isHome = models.SmallIntegerField(default=1)
    categoryID = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.name

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
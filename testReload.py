#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage

# Create a new object
obj1 = BaseModel()
print(f'Created new object: {obj1}')

# Save the object
obj1.save()
print(f'Saved object: {obj1}')

# Create another object to check multiple objects handling
obj2 = BaseModel()
print(f'Created another object: {obj2}')
obj2.save()

# Reload the storage to verify persistence
storage.reload()
objects = storage.all()
for key, obj in objects.items():
    print(f'{key}: {obj}')

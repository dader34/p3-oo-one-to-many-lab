class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
        self._name = name
        if(isinstance(owner,Owner)):
            self._owner = owner
        if(pet_type in PET_TYPES):
            self._pet_type = pet_type
            Pet.all.append(self)
        else:
            raise(ValueError(f"invalid pet type {pet_type}, please choose a different type"))
   
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,pet_type):
        self._name = pet_type

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self,owner):
        self._name = owner


class Owner:
    def __init__(self,name):
        self._name = name

    def pets(self):
        return [pet for pet in Pet.all if pet._owner._name == self._name]
    
    def add_pet(self, pet):
        if(isinstance(pet,Pet)):
            pet._owner = self
        else:
            raise Exception("Please choose a pet object to add")
    
    def get_sorted_pets(self):
        all_pets = self.pets()
        return sorted(all_pets,key=lambda x: x._name)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name

# fido = Pet("Dude","cat","danner")
# f = Pet("aaaa","cat","danner")
# danner = Owner("danner")
# print(danner.pets())
# print(danner.sort_pets_by_name())
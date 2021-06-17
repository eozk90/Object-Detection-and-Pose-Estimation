# Python Object-Oriented Programming
# data and functions associated with a class, we call those attributes and methods
# creating simple class
# difference between a class and an instance of that class
# how to initialize class attributes and create methods

class Object_Detector:
    # pass
    # init method takes the instance which we called self,
    # then takes first, last, and pay as arguments or attributes of our class
    def __init__(self, object_number, name_object, object_width, object_height):
        self.object_number = object_number
        self.name_object = name_object
        self.object_width = object_width
        self.object_height = object_height

    def storage_directory(self):
        return "Object Detection File"


# unique instances of the employee class
# instance is passed automatically, we only need to provide names and pay
image_1 = Object_Detector(1, 'Helmet', 0.3, 0.2)
image_2 = Object_Detector(3, 'Arm Pad', 0.4, 0.5)

print(image_1.name_object)
print(image_2.object_height)
print('{} {}'.format(image_1.name_object, image_2.object_height))

# we need parenthesis because this is a method
print(image_1.storage_directory())
# We can also run these methods using the class name itself
print(Object_Detector.storage_directory(image_1))

# image_1 = Object_Detector()
# image_2 = Object_Detector()
#
# # each of these instances now have attributes that are unique to them
# image_1.object_number = 1
# image_1.name_object = 'Helmet'
# image_1.object_width= 0.3
# image_1.object_height = 0.2
#
# image_2.object_number = 3
# image_2.name_object = 'Arm Pad'
# image_2.object_width= 0.4
# image_2.object_height = 0.5
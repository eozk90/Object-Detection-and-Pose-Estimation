# Python Object-Oriented Programming
# data and functions associated with a class, we call those attributes and methods
# creating simple class
# difference between a class and an instance of that class
# how to initialize class attributes and create methods
import datetime
import os


class Object_Detector:
    # pass
    # init method takes the instance which we called self,
    # then takes first, last, and pay as arguments or attributes of our class
    def __init__(self, object_index, name_object, object_width, object_height):
        self.object_index = object_index
        self.name_object = name_object
        self.object_width = object_width
        self.object_height = object_height

    # a regular method
    def storage_directory(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path

    # class method takes the instance cls as the first argument,
    @classmethod
    def from_string(cls, obj_str):
        object_number, name_object, object_width, object_height = obj_str.split('-')
        return cls(object_number, name_object, object_width, object_height)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# subclass1
class Annotation_format(Object_Detector):
    def __init__(self, object_index, name_object, object_width, object_height, image_format, extension):
        super().__init__(object_index, name_object, object_width, object_height)
        # Object_Detector.__init__(self, object_index, name_object, object_width, object_height)
        self.image_format = image_format
        self.extension = extension


# # subclass2
# class detection_count(Object_Detector):
#     def __init__(self, object_index, name_object, object_width, object_height, object_count=None):
#         super().__init__(object_index, name_object, object_width, object_height)
#         if object_count is None:
#             self.object_count = []
#         else:
#             self.object_count = object_count
#
#     def add_image(self, image_processed):
#         if image_processed not in self.object_count:
#             # append to our count lis
#             self.object_count.append(image_processed)
#
#     def remove_image(self, image_processed):
#         if image_processed in self.object_count:
#             # append to our count lis
#             self.object_count.remove(image_processed)
#
#     def print_images(self):
#         for image_processed in self.object_count:
#             print('-->', image_processed)


# unique instances of the employee class
# instance is passed automatically, we only need to provide names and pay
image_1 = Object_Detector(1, 'Helmet', 0.3, 0.2)
image_2 = Object_Detector(3, 'Arm Pad', 0.4, 0.5)

print(image_1.name_object)
print(image_2.object_height)
print('{} {}'.format(image_1.name_object, image_2.object_height))
print('\n')

# we need parenthesis because this is a method
print(image_1.storage_directory())
# We can also run these methods using the class name itself and provide the instance object as an input
print(Object_Detector.storage_directory(image_1))
print('\n')

# usage of class method
image_1_str = '1-Helmet-0.3-0.2'
new_image_1 = Object_Detector.from_string(image_1_str)
print(new_image_1.name_object)
print('\n')

# usage of static method
# independent of class instance or methods
event_date = datetime.date(2021, 6, 22)
print(Object_Detector.is_workday(event_date))
print('\n')

# print if the labelling is done in YOLO or PASCAL format
print(help(Annotation_format))

# show image format and extension by using the subclass method that inherits the main class attributes and methods
detailed_image_1 = Annotation_format(1, 'Helmet', 0.3, 0.2, 'YOLO', 'JPEG')
detailed_image_2 = Annotation_format(3, 'Arm Pad', 0.4, 0.5, 'PASCAL', 'PNG')
print(detailed_image_1.extension)
print(detailed_image_2.image_format)


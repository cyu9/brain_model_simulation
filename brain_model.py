import random
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

BRAIN_AGE = 'young'
ELECTRODE_TYPE = 'sharp'
INSERTION_SPEED = 'fast'
INSERTION_DEPTH = 'shallow'

WT_INSERTION_SPEED = 0.65
WT_ELECTRODE_TYPE = 0.20
WT_TEXTURE_TYPE = 0.05
WT_DEPTH_LEVEL = 0.1


class BrainModel:
    def __init__(self, age='young', brain_size='small', penetration_depth='shallow', insertion_speed='fast'):
        self.age = age
        self.brain_size = brain_size
        self.penetration_depth = penetration_depth
        self.insertion_speed = insertion_speed

    def insert(self, microelectrode_object):
        electrode_type = microelectrode_object.electrode_type
        electrode_cleanliness = microelectrode_object.cleanliness
        electrode_texture = microelectrode_object.texture

        insertion_speed_effect = generate_insertion_speed_effect(self.insertion_speed)
        electrode_type_effect = generate_electrode_effect(electrode_type)
        texture_effect = generate_texture_effect(electrode_texture)
        insertion_depth_effect = generate_insertion_depth_effect(self.penetration_depth)

        deformation = WT_INSERTION_SPEED*(100 - insertion_speed_effect) + WT_ELECTRODE_TYPE*electrode_type_effect + \
                      WT_TEXTURE_TYPE*texture_effect + WT_DEPTH_LEVEL*insertion_depth_effect

        return deformation


class Microelectrode:
    def __init__(self, electrode_type='sharp', cleanliness='clean', texture='smooth'):
        self.electrode_type = electrode_type
        self.cleanliness = cleanliness
        self.texture = texture


def generate_insertion_speed_effect(insertion_speed_selection):
    if insertion_speed_selection == 'slow':
        insertion_speed_effect = random.randint(1, 35)
        return insertion_speed_effect
    elif insertion_speed_selection == 'fast':
        insertion_speed_effect = random.randint(80, 100)
        return insertion_speed_effect
    else:
        return 0


def generate_electrode_effect(electrode_type):
    if electrode_type == 'sharp':
        electrode_effect = random.randint(1, 33)
        return electrode_effect
    elif electrode_type == 'medium':
        electrode_effect = random.randint(34, 66)
        return electrode_effect
    elif electrode_type == 'blunt':
        electrode_effect = random.randint(67, 100)
        return electrode_effect
    else:
        return 0


def generate_texture_effect(electrode_texture_type):
    if electrode_texture_type == 'smooth':
        texture_effect = random.randint(1, 50)
        return texture_effect
    elif electrode_texture_type == 'rough':
        texture_effect = random.randint(51, 100)
        return texture_effect
    else:
        return 0


def generate_insertion_depth_effect(insertion_depth):
    if insertion_depth == 'shallow':
        insertion_depth_effect = random.randint(1, 33)
        return insertion_depth_effect
    elif insertion_depth == 'medium':
        insertion_depth_effect = random.randint(34, 66)
        return insertion_depth_effect
    elif insertion_depth == 'deep':
        insertion_depth_effect = random.randint(67, 100)
        return insertion_depth_effect
    else:
        return 0


def perform_surgery_1():
    # young brain and sharp electrode

    # A - slow and shallow
    young_brain_A = BrainModel('young', 'small', 'shallow', 'slow')
    microelectrode_A = Microelectrode('sharp')

    deformation_A_list = []
    for i in range(100):
        deformation_A = young_brain_A.insert(microelectrode_A)
        deformation_A_list.append(deformation_A)
    deformation_A_list_avg = mean(deformation_A_list)
    print('slow and shallow, mean = ', deformation_A_list_avg)

    # B - fast and shallow
    young_brain_B = BrainModel('young', 'small', 'shallow', 'fast')
    microelectrode_B = Microelectrode('sharp')

    deformation_B_list = []
    for i in range(100):
        deformation_B = young_brain_B.insert(microelectrode_B)
        deformation_B_list.append(deformation_B)
    deformation_B_list_avg = mean(deformation_B_list)
    print('fast and shallow, mean = ', deformation_B_list_avg)

    # C - fast and deep
    young_brain_C = BrainModel('young', 'small', 'deep', 'fast')
    microelectrode_C = Microelectrode('sharp')

    deformation_C_list = []
    for i in range(100):
        deformation_C = young_brain_C.insert(microelectrode_C)
        deformation_C_list.append(deformation_C)
    deformation_C_list_avg = mean(deformation_C_list)
    print('fast and deep, mean = ', deformation_C_list_avg)

    # D - slow and deep
    young_brain_D = BrainModel('young', 'small', 'deep', 'slow')
    microelectrode_D = Microelectrode('sharp')

    deformation_D_list = []
    for i in range(100):
        deformation_D = young_brain_D.insert(microelectrode_D)
        deformation_D_list.append(deformation_D)
    deformation_D_list_avg = mean(deformation_D_list)
    print('slow and deep, mean = ', deformation_D_list_avg)

    # PLOT
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    xpos = [1, 3, 3, 1]
    ypos = [0, 0, 2, 2]
    zpos = [0, 0, 0, 0]

    dx = np.ones(4)
    dy = np.ones(4)
    dz = [deformation_A_list_avg, deformation_B_list_avg, deformation_C_list_avg, deformation_D_list_avg]

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#4287f5')
    x_labels = ['', 'slow', '', 'fast']
    ax1.set_xticks(range(4))
    ax1.set_xticklabels(x_labels)

    y_labels = ['', 'shallow', '', 'deep']
    ax1.set_yticks(range(4))
    ax1.set_yticklabels(y_labels)

    ax1.set_xlabel('Insertion Speed')
    ax1.set_ylabel('Insertion Depth')
    ax1.set_zlabel('Deformation')
    plt.show()
    return 0


def perform_surgery_2():
    # young brain and sharp electrode

    # A - slow and shallow
    old_brain_A = BrainModel('old', 'small', 'shallow', 'slow')
    microelectrode_A = Microelectrode('sharp')

    deformation_A_list = []
    for i in range(100):
        deformation_A = old_brain_A.insert(microelectrode_A)
        deformation_A_list.append(deformation_A)
    deformation_A_list_avg = mean(deformation_A_list)
    print('slow and shallow, mean = ', deformation_A_list_avg)

    # B - fast and shallow
    old_brain_B = BrainModel('old', 'small', 'shallow', 'fast')
    microelectrode_B = Microelectrode('sharp')

    deformation_B_list = []
    for i in range(100):
        deformation_B = old_brain_B.insert(microelectrode_B)
        deformation_B_list.append(deformation_B)
    deformation_B_list_avg = mean(deformation_B_list)
    print('fast and shallow, mean = ', deformation_B_list_avg)

    # C - fast and deep
    old_brain_C = BrainModel('old', 'small', 'deep', 'fast')
    microelectrode_C = Microelectrode('sharp')

    deformation_C_list = []
    for i in range(100):
        deformation_C = old_brain_C.insert(microelectrode_C)
        deformation_C_list.append(deformation_C)
    deformation_C_list_avg = mean(deformation_C_list)
    print('fast and deep, mean = ', deformation_C_list_avg)

    # D - slow and deep
    old_brain_D = BrainModel('old', 'small', 'deep', 'slow')
    microelectrode_D = Microelectrode('sharp')

    deformation_D_list = []
    for i in range(100):
        deformation_D = old_brain_D.insert(microelectrode_D)
        deformation_D_list.append(deformation_D)
    deformation_D_list_avg = mean(deformation_D_list)
    print('slow and deep, mean = ', deformation_D_list_avg)

    # PLOT
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    xpos = [1, 3, 3, 1]
    ypos = [0, 0, 2, 2]
    zpos = [0, 0, 0, 0]

    dx = np.ones(4)
    dy = np.ones(4)
    dz = [deformation_A_list_avg, deformation_B_list_avg, deformation_C_list_avg, deformation_D_list_avg]

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#4287f5')
    x_labels = ['', 'slow', '', 'fast']
    ax1.set_xticks(range(4))
    ax1.set_xticklabels(x_labels)

    y_labels = ['', 'shallow', '', 'deep']
    ax1.set_yticks(range(4))
    ax1.set_yticklabels(y_labels)

    ax1.set_xlabel('Insertion Speed')
    ax1.set_ylabel('Insertion Depth')
    ax1.set_zlabel('Deformation')
    plt.show()
    return 0

perform_surgery_1()
perform_surgery_2()
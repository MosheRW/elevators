﻿#responsebol on window and display managment

TIME_TRAVEL_BETWEEN_FLOORS = 0.5 #seconds
ELEVATOR_SIZE = (60,60)
FLOOR_SIZE = (160,60)
SPACE = 5
ELEVATOR_PIC_FILE = 'resources\elv.png'
FLOOR_PIC_FILE = 'resources\wall.jpg'

def get_floors_boundries(floor):
    return {"ceiling" : floor +1 * FLOOR_SIZE[1], "floor" : floor * FLOOR_SIZE[1]}



"""
לשים כאן פונקציה גלובלית שקוראת לקובץ התמונה של מעלית ועוד אחת לקובץ התמונה של קומה

תהיה מחלקה קומה

תהיה מחלקה טיימר

המחלקה קומה תהיה אחראית גם על הטיימר

כל מחלקה תהיה אחראית לייצר את התמונה כולל המיקום ולהחזיר אותו לפונקציה המרכזית באמצעות טכניקת משפך שיעשה אפדייט למסך עצמו ובו נעשה את השימוש בבליט

"""
import cv2
import numpy as np

from cv_viewer.utils import *
import pyzed.sl as sl

import datetime


#----------------------------------------------------------------------
#       2D VIEW
#----------------------------------------------------------------------
def cvt(pt, scale):
    '''
    Function that scales point coordinates
    '''
    out = [pt[0]*scale[0], pt[1]*scale[1]]
    return out

def import_body3D(objects, is_tracking_on, body_format):
    '''
    Parameters
        left_display (np.array): numpy array containing image data
        img_scale (list[float])
        objects (list[sl.ObjectData]) 
    '''

    id_body=-1 
    time_body=-1
    joints_body=-1

    # Render skeleton joints and bones
    for obj in objects:
        if render_object(obj, is_tracking_on):
            if len(obj.keypoint) > 0:
                # POSE_18
                if body_format == sl.BODY_FORMAT.POSE_18:
                    #Get skeleton data joints

                    joints={
                        'Nose':obj.keypoint[0],
                        'Neck':obj.keypoint[1],

                        'ShoulderRight':obj.keypoint[2],
                        'ElbowRight':obj.keypoint[3],
                        'WristRight':obj.keypoint[4],
                        'ShoulderLeft':obj.keypoint[5],
                        'ElbowLeft':obj.keypoint[6],
                        'WristLeft':obj.keypoint[7],

                        'HipRight':obj.keypoint[8],
                        'KneeRight':obj.keypoint[9],
                        'AnkleRight':obj.keypoint[10],
                        'HipLeft':obj.keypoint[11],
                        'KneeLeft':obj.keypoint[12],
                        'AnkleLeft':obj.keypoint[13],

                        'EyeRight':obj.keypoint[14],
                        'EyeLeft':obj.keypoint[15],

                        'EarRight':obj.keypoint[16],
                        'EarLeft':obj.keypoint[17],
                    }
                    
                    #ID_body, time_stamp, joints
                    id_body=obj.id
                    time_body=str(datetime.datetime.now())
                    joints_body=joints

    
                elif body_format == sl.BODY_FORMAT.POSE_34:
                    #Get skeleton data joints
                    joints={
                        'Pelvis':obj.keypoint[0],
                        'NavalSpine':obj.keypoint[1],
                        'ChestSpine':obj.keypoint[2],
                        'Neck':obj.keypoint[3],

                        'ClavicleLeft':obj.keypoint[4],
                        'ShoulderLeft':obj.keypoint[5],
                        'ElbowLeft':obj.keypoint[6],
                        'WristLeft':obj.keypoint[7],
                        'HandLeft':obj.keypoint[8],
                        'HandTipLeft':obj.keypoint[9],
                        'TumbLeft':obj.keypoint[10],

                        'ClavicleRight':obj.keypoint[11],
                        'ShoulderRight':obj.keypoint[12],
                        'ElbowRight':obj.keypoint[13],
                        'WristRight':obj.keypoint[14],
                        'HandRight':obj.keypoint[15],
                        'HandTipRight':obj.keypoint[16],
                        'TumbRight':obj.keypoint[17],

                        'HipLeft':obj.keypoint[18],
                        'KneeLeft':obj.keypoint[19],
                        'AnkleLeft':obj.keypoint[20],
                        'FootLeft':obj.keypoint[21],

                        'HipRight':obj.keypoint[22],
                        'KneeRight':obj.keypoint[23],
                        'AnkleRight':obj.keypoint[24],
                        'FootRight':obj.keypoint[25],

                        'Head':obj.keypoint[26],
                        'Nose': obj.keypoint[27],
                        'EyeLeft':obj.keypoint[28],
                        'EarLeft':obj.keypoint[29],
                        'EyeRight':obj.keypoint[30],
                        'EarRight':obj.keypoint[31],

                        'HeelLeft':obj.keypoint[32],
                        'HeelRight':obj.keypoint[33],
                    }

                    #ID_body, time_stamp, joints
                    id_body=obj.id
                    time_body=str(datetime.datetime.now())
                    joints_body=joints

        
    return id_body, time_body, joints_body



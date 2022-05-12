import numpy as np

def plam_angle(hand_Landmark_List, joint_list):

    for hand in hand_Landmark_List:

        for joint in joint_list:
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y]) # First coord
            b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y]) # Second coord
            c = np.array([hand.landmark[joint[1]].x+10, hand.landmark[joint[1]].y]) # Third coord

            radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
    return angle

def detect_hand_angle(hand_Landmark_List):
    for res in hand_Landmark_List:
        joint = np.zeros((21,3))
        for j, lm in enumerate(res.landmark):
            joint[j] = [lm.x, lm.y, lm.z]

        v1 = joint[[0, 1, 2, 3, 0, 5, 6, 7, 0, 9, 10, 11, 0, 13, 14, 15, 0, 17, 18, 19], :]
        v2 = joint[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], :]

        v = v2 - v1

        compareV1 = v[[0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 17], :]
        compareV2 = v[[1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19], :]

        angle = np.arccos(np.einsum('nt,nt->n', compareV1, compareV2))
        angle = np.degrees(angle)

        joint_list = [[9,0]]
        palm_angle = palm_angle(hand_Landmark_List, joint_list)
        angle = np.append(angle, np.array([palm_angle]))

        hi="hi"

    return hi

import cv2
import mediapipe as mp

class Tracker():
    def __init__(self, static_image_mode=False, max_num_hands=2, 
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        
        self.hands = mp.solutions.hands.Hands(static_image_mode=self.static_image_mode,
                                              max_num_hands=self.max_num_hands,
                                              min_detection_confidence=self.min_detection_confidence,
                                              min_tracking_confidence=self.min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.tracking_list = []
    
        
    
    def hand_landmark(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
        return img
    
    def tracking(self, img, hand='right', lm_id=8):
        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks)==1:
                hand_landmarks = self.results.multi_hand_landmarks[0]
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    x, y = int(lm.x*w), int(lm.y*h)
                    if id==lm_id:
                        if len(self.tracking_list)>=50:
                            self.tracking_list.pop(0)
                        self.tracking_list.append([x, y])
                    for point in self.tracking_list:
                           cv2.circle(img, (point[0], point[1]), 10, (255, 0, 255), cv2.FILLED)
                    
            else:
                if hand=='right':
                    hand_landmarks = self.results.multi_hand_landmarks[0]
                    for id, lm in enumerate(hand_landmarks.landmark):
                        h, w, c = img.shape
                        x, y = int(lm.x*w), int(lm.y*h)
                        if id==lm_id:
                            if len(self.tracking_list)>=50:
                                self.tracking_list.pop(0)
                            self.tracking_list.append([x, y])
                        for point in self.tracking_list:
                            cv2.circle(img, (point[0], point[1]), 10, (255, 0, 255), cv2.FILLED)
                        
                            
                elif hand=='left':
                    hand_landmarks = self.results.multi_hand_landmarks[1]
                    for id, lm in enumerate(hand_landmarks.landmark):
                        h, w, c = img.shape
                        x, y = int(lm.x*w), int(lm.y*h)
                        if id==lm_id:
                            if len(self.tracking_list)>=50:
                                self.tracking_list.pop(0)
                            self.tracking_list.append([x, y])
                        for point in self.tracking_list:
                            cv2.circle(img, (point[0], point[1]), 10, (255, 0, 255), cv2.FILLED)
        return img               
                    
    
if __name__ == "__main__":
    pass
    # tracker = Tracker()
    # img = cv2.imread("./images/2.jpeg")
    # img = tracker.hand_landmark(img)
    # cv2.imshow('image', tracker.tracking(img))
    # cv2.waitKey(0)

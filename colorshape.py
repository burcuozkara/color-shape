# -*- coding: utf-8 -*-

import numpy as np
import cv2
import serial
import time
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1) #arduino ile serial haberleşme
time.sleep(2)
x=("0")
#python import file


# Video kamera açılması
webcam = cv2.VideoCapture(1)       
# döngü başlamnası
while(1):
    _, imageFrame = webcam.read()  #webcam açılmsaı
    data = arduino.readline() # arduino bilgi okuması
    print (data) # okunan datanın ekrana yazılması
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) #ekrana görüntünün yazılması
    if(data==b'1'): 
        x=("0")
        dongu=1
        while(dongu==1):
            print ("ok")
            time.sleep(1)
            _, imageFrame = webcam.read() # webcam oku
            cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) # ekrana yazılması
            # Video framelerin okunkması
            # Resim renk uzayını değiştirmek
            # BGR(RGB color space) to
            # HSV(hue-saturation-value)
            hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
            # Yeşil Renk için maskeleme renkleri
            green_lower = np.array([25, 52, 72], np.uint8) #25, 52, 72
            green_upper = np.array([75, 255, 255], np.uint8) #75, 255, 255
            green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
	    #mavi renk için maskeleme renkleri
            blue_lower = np.array([84, 124, 2], np.uint8)
            blue_upper = np.array([120, 255, 255], np.uint8)
            blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
            
 	    # Morfolojik Dönüşüm, her renk için Genişletme ve imageFrame ile mask arasındaki bitwise_and operatörü yalnızca o belirli rengi algılamayı belirler
            kernal = np.ones((5, 5), "uint8")

            
            # Yeşil Renk İçin Maske
            green_mask = cv2.dilate(green_mask, kernal)
            res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                        mask = green_mask)
            
            # Mavi Renk İçin Maske
            blue_mask = cv2.dilate(blue_mask, kernal)
            res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                                    mask = blue_mask)
        
  	    #Yeşil Maske ile controur yüzey atandı.
            contours, hierarchy = cv2.findContours(green_mask,
                                                cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)
            #videoda her frame için resime contour yapıldı
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                #alan hesaplandı
                if(area > 12000):
                    img_gray = cv2.cvtColor(imageFrame,cv2.COLOR_RGB2GRAY) #siyah beyaz yapıldı
                    noise_removal = cv2.bilateralFilter(img_gray,9,75,75) # resimden gürültü kaldırıldı
                    ret,thresh_image = cv2.threshold(noise_removal,0,255,cv2.THRESH_OTSU) #thresh holding yapıldı
                    canny_image = cv2.Canny(thresh_image,250,255) #canny edge ile köşe tanıması yapıldı
                    kernel = np.ones((3,3), np.uint8)
                    dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
                    contours, h = cv2.findContours(dilated_image, 1, 2) #contour bulundu 
                    contours= sorted(contours, key = cv2.contourArea, reverse = True)[:1] #sıralandı
                    pt = (180, 3 * imageFrame.shape[0] // 4)
                    for cnt in contours:
                        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #köşe sayısı buluındu
                        # print len(cnt)
                        print (len(approx))
                        if len(approx) <=7 and len(approx) >2:
                            print ("Küp Yesil")
                            x=("1")
                            arduino.write(bytes(x, 'utf-8'))  #Arduinoya bilgi gönderildi
                            dongu=0
                        elif len(approx) >7:
                            print ("Silidir yeşil")
                            x=("2")		#Arduinoya bilgi gönderildi
                            arduino.write(bytes(x, 'utf-8'))
                            dongu=0
                         #dikdörtgen çizme kısmı
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                            (x + w, y + h),
                                            (0, 255, 0), 2)
                    
                    cv2.putText(imageFrame, "Green Colour", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (0, 255, 0))
        
            # Creating contour to track blue color
            contours, hierarchy = cv2.findContours(blue_mask,
                                                cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)

 	    
            for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if(area > 12000):
                    img_gray = cv2.cvtColor(imageFrame,cv2.COLOR_RGB2GRAY)
                    noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
                    ret,thresh_image = cv2.threshold(noise_removal,0,255,cv2.THRESH_OTSU)
                    canny_image = cv2.Canny(thresh_image,250,255)
                    kernel = np.ones((3,3), np.uint8)
                    dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
                    contours, h = cv2.findContours(dilated_image, 1, 2)
                    contours= sorted(contours, key = cv2.contourArea, reverse = True)[:1]
                    pt = (180, 3 * imageFrame.shape[0] // 4)
                    for cnt in contours:
                        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
                        # print len(cnt)
                        print (len(approx))
                        if len(approx) <=7 and len(approx) >2:
                            print ("Küp mavi")
                            x=("3")
                            arduino.write(bytes(x, 'utf-8'))
                            dongu=0
                        elif len(approx) >7:
                            print ("Silindir mavi")
                            x=("4")
                            arduino.write(bytes(x, 'utf-8'))
                            dongu=0
              
                    x, y, w, h = cv2.boundingRect(contour)
                    imageFrame = cv2.rectangle(imageFrame, (x, y),
                                            (x + w, y + h),
                                            (255, 0, 0), 2)
                    
                    cv2.putText(imageFrame, "Blue Colour", (x, y),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                1.0, (255, 0, 0))
                    if (dongu==0):
                        time.sleep(5)
                           
            # Program Termination
            # cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
    
            break
    
imageFrame.release()
cv2.destroyAllWindows()

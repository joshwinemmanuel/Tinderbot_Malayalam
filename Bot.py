from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import urllib.request
from time import sleep
from selenium.webdriver.common.keys import Keys
import cv2
import faceRecognition as fr


from config import CHROME_PROFILE_PATH



options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)
browser = webdriver.Chrome(executable_path='C:\chromedriver/chromedriver', options=options)
browser.maximize_window()
browser.get('https://tinder.com')


def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    os.system('cls')
    print ("image data recived") 
    urllib.request.urlretrieve(url, full_path)

def tester(file_path, file_name):
    t = 0
    full_path = file_path + file_name + '.jpg'
    os.system('cls')
    print ("image data recived")
    full_path = file_path + file_name + '.jpg'
   
    test_img=cv2.imread(full_path)#test_img path
    faces_detected,gray_img=fr.faceDetection(test_img)
    try:
        if not faces_detected:
            print("nothing faces_detected:",faces_detected)
            mtch(0)
    except:
        print("faces_detected:",faces_detected)

    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trainingData.yml')#use this to load training data for subsequent runs

    name={0:"crush"}#creating dictionary containing names for each label

    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+h,x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        

        if (confidence >= 200) or (70 <= confidence <= 90):#If confidence more than 37 then don't print predicted face text on screen
            mtch(0)
            continue
        fr.put_text(test_img,predicted_name,x,y)
        mtch(1)

def urlfind():
    
        elements = WebDriverWait(browser, 500).until(EC.visibility_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/span[1]/div')))
        for element in elements:
            element=element.value_of_css_property("background-image")
            os.system('cls')
            url=element.replace('url("',"")
            url=url.replace('")',"")
            print ("image url found")
            print(url)

            try:
                dl_jpg(url, 'TestImages/', 'test')
                os.system('cls')
                print ("test image added")
                tester('TestImages/', 'test')
                os.system('cls')
                print ("testing completed")
                number = resul         
            except:
                os.system('cls')
                print("An exception occurred")
                number = 0
   
def mtch(resul):
    number = resul    
    sleep(2)
    if number == 1:
        os.system('cls')
        print ("She is my taste so swipe RIGHT!!!")
        track = browser.find_element('xpath', '//*[@id="Tinder"]/body')
        track.send_keys(Keys.ARROW_RIGHT)
    elif number == 0:
        os.system('cls')
        print ("Nhaa Not my type Swipe LEFT!!!")
        track = browser.find_element('xpath', '//*[@id="Tinder"]/body')
        track.send_keys(Keys.ARROW_LEFT)
    urlfind()
    



sleep(1)
try:
        
         login = browser.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
    
         login.click()
         fb_login = browser.find_element('xpath', '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div')
         fb_login.click()
except:
   print("alrady loged in")
   while True:
    cv2.destroyAllWindows
    urlfind()


   
        
        

   




  







 
   
   
# time.sleep(200)







	
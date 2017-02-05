from PIL import Image
import subprocess
import os

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    
    # 회색 임계점을 설정하고 이미지를 저장합니다.
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)
    
    # 새로 만든 이미지를 태서랙트로 읽습니다.
    subprocess.call(["tesseract", newFilePath, "output"])   # output: file name
    
    # 결과 텍스트 파일을 열어 읽습니다.
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()

# cwd = os.getcwd()
# filename = os.path.join(cwd, r"11-2\text_2.tif")
# new_file = os.path.join(cwd, r"11-2\text_2_clean.tif")
# txt_file = os.path.join(cwd, r"11-2\output.txt")

cleanFile("text_2.tif", "text_2_clean.tif")
# print("text_2.tif", "text_2_clean.tif")

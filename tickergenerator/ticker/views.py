from django.shortcuts import render
from django.http import FileResponse
from PIL import Image, ImageDraw, ImageFont
import cv2


def ticker(request):
    text = request.GET.get('text', '')
    # Генерируем видео из картинок
    frameSize = (100, 100)
    outVideo = cv2.VideoWriter('../output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, frameSize)
    font = ImageFont.truetype("arial.ttf", size=50)
    width = ImageFont.FreeTypeFont.getlength(font, text=text)
    step = width / 90
    x_cord = 50
    for i in range(1, 91):
        img = Image.new('RGB', (100, 100), 'purple')
        idraw = ImageDraw.Draw(img)
        idraw.text((x_cord, 22), text=text, font=font)
        x_cord -= step
        img.save('../photo.jpg')
        outVideo.write(cv2.imread('../photo.jpg'))
    outVideo.release()

    # Возвращаем получившееся видео
    path = open('../output_video.avi', 'rb')
    response = FileResponse(path)
    return response





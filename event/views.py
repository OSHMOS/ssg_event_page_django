from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import letter
from PIL import Image
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from event.forms import EventForm
from django.conf import settings
import os


# Create your views here.
def certify(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            event.save()
            return render(request, 'event/coupon.html')
        else:
            print(form.errors.as_data())
    return render(request, 'event/form.html', {'form': form})


def coupon(request):
    return render(request, 'event/coupon.html')


# def download(request):
#     try:
#         with open(os.path.join(settings.BASE_DIR, 'static', 'img', 'coupon.jpg'), 'rb') as f:
#             return HttpResponse(f.read(), content_type='image/jpg')
#     except IOError:
#         return HttpResponseNotFound('<h1>Page not found</h1>')


def download(request):
    # 이미지 파일 경로
    image_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'coupon.jpg')

    # PDF 파일 생성을 위한 설정
    buffer = BytesIO()
    pdf_canvas = canvas.Canvas(buffer, pagesize=letter)

    # 이미지 파일 로드
    image = Image.open(image_path)

    # 이미지를 PDF로 변환하여 출력
    width, height = image.size
    pdf_canvas.drawImage(ImageReader(image), 0, 0, width=256, height=144)

    # PDF 파일 저장 및 응답 객체 반환
    pdf_canvas.save()
    pdf_buffer = buffer.getvalue()
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="숭선바 상품 교환권"'
    return response

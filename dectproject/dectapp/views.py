import subprocess
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .forms import ImageUploadForm
from .models import UploadedImage

def home(request):
    return render(request, 'home.html')

def run_mask_detection(request):
    mask_detection_dir = os.path.abspath(os.path.join(os.getcwd(), "projfiles/maskdetection"))
    if os.name == "nt":
        subprocess.Popen(["start", "cmd", "/k", "python detect_mask.py"], cwd=mask_detection_dir, shell=True)
    else: 
        subprocess.Popen(["gnome-terminal", "--", "python3", "detect_mask.py"], cwd=mask_detection_dir)
    return HttpResponse("Mask detection script is running! Check the new terminal window.")


def run_change_col(request):
    return render(request, 'colorcng.html')

def upload_and_blur_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()  
            input_image_path = uploaded_image.image.path 

            script_path = os.path.join(settings.BASE_DIR, "projfiles", "colorchange", "blur.py")
            try:
                result = subprocess.run(["python", script_path, input_image_path], capture_output=True, text=True)
                print("STDOUT:", result.stdout)  
                print("STDERR:", result.stderr)  
            except Exception as e:
                return render(request, 'upload.html', {"form": form, "output": f"Error running script: {e}"})

            return render(request, 'upload.html', {"form": form, "output": "blur image created successfully!"})  
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {"form": form})



def upload_and_color_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save() 
            input_image_path = uploaded_image.image.path  

            script_path = os.path.join(settings.BASE_DIR, "projfiles", "colorchange", "colormap.py")

            try:
                result = subprocess.run(["python", script_path, input_image_path], capture_output=True, text=True)
                print("STDOUT:", result.stdout)  
                print("STDERR:", result.stderr)   
            except Exception as e:
                return render(request, 'upload2.html', {"form": form, "output": f"Error running script: {e}"})

            return render(request, 'upload2.html', {"form": form, "output": "color image created successfully!"})  
    else:
        form = ImageUploadForm()
    return render(request, 'upload2.html', {"form": form})


def upload_and_gray_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()  # Save uploaded image
            input_image_path = uploaded_image.image.path  # Get full image path

            script_path = os.path.join(settings.BASE_DIR, "projfiles", "colorchange", "gray.py")

            try:
                result = subprocess.run(["python", script_path, input_image_path], capture_output=True, text=True)
                print("STDOUT:", result.stdout)  
                print("STDERR:", result.stderr)  
            except Exception as e:
                return render(request, 'upload3.html', {"form": form, "output": f"Error running script: {e}"})

            return render(request, 'upload3.html', {"form": form, "output": "Grayscale image created successfully!"})  
    else:
        form = ImageUploadForm()
    return render(request, 'upload3.html', {"form": form})



def choose_filter(request):
    mask_detection_dir = os.path.abspath(os.path.join(os.getcwd(), "projfiles/filter"))
    if os.name == "nt":  # For Windows
        subprocess.Popen("start cmd /k python filter_app.py", cwd=mask_detection_dir, shell=True)
    else:  # For Linux
        subprocess.Popen(["gnome-terminal", "--", "python3", "filter_app.py"], cwd=mask_detection_dir)
    return HttpResponse("Mask detection script is running! Check the new terminal window.")


def product_page(request):
    return render(request, 'product.html')

def carrier_page(request):
    return render(request, 'carrier.html')

def notes_page(request):
    return render(request, 'notes.html')

def support_page(request):
    return render(request, 'support_learn.html')

def aboutus_page(request):
    return render(request, 'about_us.html')

def feedback_page(request):
    return render(request, 'feedback.html')

def accounts_page(request):
    return render(request, 'account.html')


import torch
from torch.autograd import Variable
from torchvision import transforms
from rockethub import Rocket
from PIL import Image

# --- LOAD IMAGE ---
# Select the image you want to improve with ESRGAN
image_path = 'images/girl1.png'
# image_path = 'images/girl2.png'
# image_path = 'images/lion.png'

img = Image.open(image_path).convert('RGB')

# --- LOAD ROCKET ---
rocket = "igor/esrgan"

model = Rocket.land(rocket).eval()

# --- SUPER RESOLUTION ---
print('Using the rocket to improve the resolution of \'' + image_path + '\'...')
with torch.no_grad():
    img_tensor = model.preprocess(img)
    out = model(img_tensor)

print('Super Resolution successful! ')

# --- OUTPUT ---
# Save the output to the disk
img_out = model.postprocess(out)[0]
img_out_path = 'out.png'
img_out.save(img_out_path)
print('You can checkout the improved image at \'' + img_out_path +'\'.')